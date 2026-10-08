# -*- coding: utf-8 -*-
"""Rebuild Clown Squad's *English* tl_template/ from the one the game ships.

    python games/clownsquad-01-part1/tools/make_template.py "<path-to-the-game>"

Why this game needs its own template builder
--------------------------------------------
`tools/template.py` refuses to import `game/tl/schinese` because it finds CJK
in it -- correctly, since it is guarding against importing an already-patched
game as if it were a source template.  Clown Squad is the awkward case the
guard cannot tell apart: the archive ships a *community Chinese* translation
that has been shipping with the game, not an English template, and this patch
has to replace it rather than fill it in.

The original English is still there.  Ren'Py's language tool writes the
pre-translation statement above every block it emits:

    translate schinese story01en_cab3a47c:

        # mc "(Y'know what the difference is ordinary people and heroes?)"
        mc "（你知道普通人和英雄之间有什么区别吗？）"

so the English template is the shipped file with each translated literal
swapped back for the one quoted in the comment directly above it.  Code, block
ids, attributes and speaker names are untouched, which is exactly what
`tools/build_tl.py` needs to regenerate the patch from data/tl_trans.json.

Two blocks need more than a straight swap.  Ren'Py's language tool splits a
multi-sentence `nvl` line into several statements inside one block but keeps a
single original line in the comment, so those are spelled out in NVL_SPLITS
below.  Everything else is mechanical, and `--report` prints what it had to
treat specially.
"""
from __future__ import print_function

import argparse
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GAME_DIR = os.path.dirname(HERE)

# Blocks whose comment holds one English line but whose body holds several
# statements.  key -> (english parts, note).  The english parts must be the
# original sentences in order; build_tl.py looks the Chinese up by each part.
NVL_SPLITS = {
    "story01_2_d1e81074": (
        "You either pass the exam, ",
        "or you don't.",
        'Mi "You either pass the exam, or you don\'t." -> "要么通过考试，" + "要么通不过。"',
    ),
    "story01_3_d1e05bc7": (
        "Rude.",
        "But fair.",
        'mc "Rude. But fair." -> "话说得难听。" + "不过倒也没错。"',
    ),
}

# One line in script.rpy carries two string literals:
#
#     L "Getting ready." with CropMove(time=0.1, mode='slideleft')
#
# tools/tlparse.py reports both, and tools/build_tl.py writes each replacement
# back into the line it has already shortened, so the second one is written at a
# stale offset and the built patch grows a stray identifier glued onto the end
# of the statement.  tools/ cannot be changed here, so the fix has to live in
# the template: naming the mode leaves one literal on the line and changes
# nothing about the transform.  The value cannot simply be dropped --
# 'slideleft' is NOT CropMove's default, the default is 'slideright' (checked
# against renpy.display.transition.CropMove.__init__ in this game's own
# engine) -- so it stays, it just stops being a literal.
MODE_NAMED = {
    'L "Getting ready." with CropMove(time=0.1, mode=\'slideleft\')':
        'L "Getting ready." with CropMove(time=0.1, mode=ZH_SLIDELEFT)',
    }

# Prepended to a file that used MODE_NAMED, so the name is in scope by the time
# the line runs.  It sits above the first `translate` block, which is exactly
# where tools/tlparse.py stops looking for strings.
MODE_NAMED_PREAMBLE = """\
# This file has one line that used to spell its CropMove mode out as the literal
# 'slideleft'.  tools/build_tl.py rewrites every string on a line into the line
# it has already shortened, so a second literal on the same line gets written at
# a stale offset.  Naming the mode is the fix, and the value cannot be dropped:
# 'slideleft' is not CropMove's default, the default is 'slideright'.
init python:
    ZH_SLIDELEFT = "slideleft"
"""

BLOCK_RE = re.compile(r"^translate\s+(\S+)\s+(\S+):")
# "# game/story01en.rpy:9" -- the file/line header Ren'Py puts *above* a block.
HEADER_RE = re.compile(r"^#\s*[\w./\\-]+\.rpyc?\s*:\s*\d+\s*$")

CJK = re.compile(u"[\u4e00-\u9fff]")


def find_literals(line):
    """-> [(start, end_after_quote, quote_char, raw_text)] for one source line.

    Honours backslash escapes and stops at a '#', exactly like tools/tlparse.py,
    so this and the build step agree on what a string is.
    """
    out = []
    i, n = 0, len(line)
    while i < n:
        c = line[i]
        if c == "#":
            break
        if c in "\"'":
            quote = c
            j = i + 1
            while j < n:
                ch = line[j]
                if ch == "\\" and j + 1 < n:
                    j += 2
                    continue
                if ch == quote:
                    break
                j += 1
            out.append((i, j + 1, quote, line[i + 1:j]))
            i = j + 1
        else:
            i += 1
    return out


def comment_literal(comment):
    """-> (prefix, raw_text) for the first string literal in a `# ...` comment.

    A statement can carry more than one literal -- `L "Getting ready." with
    CropMove(time=0.1, mode='slideleft')` has two -- so both sides of the swap
    take the *first* literal and the text in front of it has to match.  That
    prefix (speaker, keyword) is what proves the comment really is the original
    of this statement and not some neighbouring line.
    """
    body = comment[1:].lstrip()
    lits = find_literals(body)
    if not lits:
        return None
    start, _end, _quote, raw = lits[0]
    return body[:start].strip(), raw


def statement_literal(statement):
    """-> (start, end, prefix, raw_text) for a statement's first string literal.

    `start`/`end` bracket the literal's *contents*, which is the span a
    translation has to be written back into.
    """
    lits = find_literals(statement)
    if not lits:
        return None
    start, end, _quote, raw = lits[0]
    return start + 1, end - 1, statement[:start].strip(), raw


def swap(text, report):
    """-> English template text. Records anything it could not do verbatim.

    Returns (english_text, dropped_empty_says).
    """
    lines = text.split("\n")
    lines_source = text
    out = list(lines)
    block_id = None
    pending = []          # comments seen since the block opened
    seen_statement = False
    statement_no = [0]

    for i, line in enumerate(lines):
        m = BLOCK_RE.match(line)
        if m:
            block_id = m.group(2)
            pending = []
            seen_statement = False
            statement_no[0] = 0
            continue
        if block_id is None:
            continue

        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            # Only comments *before* the first statement belong to this block;
            # the file/line header of the *next* block and the "# TODO:" markers
            # Ren'Py sprinkles around both land after it.
            if seen_statement or HEADER_RE.match(stripped):
                continue
            pending.append(stripped)
            continue

        lits = statement_literal(line)
        if lits is None:
            seen_statement = True
            continue
        start, end, prefix, _raw = lits

        parts = NVL_SPLITS.get(block_id)
        if parts is not None:
            # Multi-sentence nvl: the block keeps one original line in its
            # comment but the language tool emitted one statement per sentence,
            # so the original has to be handed out sentence by sentence.
            index = statement_no[0]
            if index < len(parts) - 1:
                out[i] = line[:start] + parts[index] + line[end:]
            elif CJK.search(line):
                report.append("%s: statement %d has no English in NVL_SPLITS"
                              % (block_id, index + 1))
            statement_no[0] += 1
            seen_statement = True
            continue

        if pending and not seen_statement:
            found = comment_literal(pending[-1])
            if found is not None and found[0] == prefix.strip():
                out[i] = line[:start] + found[1] + line[end:]
            elif CJK.search(line):
                report.append("%s: no matching original for %s"
                              % (block_id, prefix.strip()))
        statement_no[0] += 1
        seen_statement = True

    swapped = "\n".join(out)
    text = swapped
    used_preamble = False
    for old_line, new_line in MODE_NAMED.items():
        # Only worth complaining about in the file that was supposed to hold it.
        if old_line in lines_source and old_line not in text:
            report.append("MODE_NAMED matched the source but not the swap: %r"
                          % old_line)
        if old_line in text:
            used_preamble = True
        text = text.replace(old_line, new_line)
    if used_preamble:
        text = MODE_NAMED_PREAMBLE + "\n" + text
    text, dropped = drop_empty_says(text)
    return text, dropped


# `cafe_0ae9bcd0`, `two_sisters_0ae9bcd0` and `two_sisters_0ae9bcd0_1` are
# blocks whose whole body is an empty say.  They carry no text for the player,
# and a translation database is not allowed to hold an empty value -- an empty
# translation is how unfinished work hides -- so they are left out of the
# template instead.  A no-op line is cheaper to drop than to encode.
EMPTY_SAY_BLOCK = re.compile(
    r"^translate\s+\S+\s+\S+:\n\n\s*# \"\"\n\s*\"\"\n\n?", re.M)


def drop_empty_says(text):
    return EMPTY_SAY_BLOCK.subn("", text)


def renpy_game_dir(arg):
    path = os.path.abspath(arg)
    if os.path.isdir(os.path.join(path, "game")):
        return path
    if os.path.basename(path) == "game":
        return os.path.dirname(path)
    sys.exit("not a Ren'Py game directory: %s" % arg)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("game", help="path to a Clown Squad installation")
    ap.add_argument("--report", action="store_true",
                    help="print every block that needed special handling")
    args = ap.parse_args(argv)

    src = os.path.join(renpy_game_dir(args.game), "game", "tl", "schinese")
    if not os.path.isdir(src):
        sys.exit("no game/tl/schinese there -- is this Clown Squad?")

    dest = os.path.join(GAME_DIR, "tl_template")
    wanted = ["script.rpy", "story01en.rpy"]
    missing = [n for n in wanted
               if not os.path.isfile(os.path.join(src, n))]
    if missing:
        sys.exit("missing from %s: %s\nThe template has to come from an "
                 "unpatched copy -- this game's archive already carries a "
                 "community Chinese translation, so an installed patch will "
                 "have overwritten these two files."
                 % (src, ", ".join(missing)))

    if not os.path.isdir(dest):
        os.makedirs(dest)

    for name in wanted:
        report = []
        with io.open(os.path.join(src, name), encoding="utf-8-sig") as f:
            text = f.read()
        english, dropped = swap(text, report)
        with io.open(os.path.join(dest, name), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(english)
        left = sum(1 for line in english.split("\n") if CJK.search(line))
        print("%-14s %6d lines -> %s" % (name, english.count("\n"), dest))
        print("               lines still holding CJK: %d" % left)
        print("               empty-say blocks dropped: %d" % dropped)
        if report and args.report:
            for line in report[:20]:
                print("               ! " + line)

    print("")
    print("Blocks spelled out by hand (multi-sentence nvl, one original line,")
    print("several statements -- see NVL_SPLITS):")
    for key in sorted(NVL_SPLITS):
        print("  %-24s %s" % (key, NVL_SPLITS[key][2]))
    print("")
    print("Now: python tools/build_tl.py --game clownsquad-01-part1")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))









