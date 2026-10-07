# -*- coding: utf-8 -*-
"""Validate the translation database and the built patch.

    python tools/check.py

Run this before every release. Exit code 0 = clean, 1 = problems found.

Length is measured in *rendered columns*, not characters: a CJK glyph renders
about twice as wide as a Latin one, so "H-how..." (6 columns) legitimately
becomes 12 columns of Chinese without any risk of overflow. What would
actually break a line is a translation that outgrows the box, so that is what
gets flagged:

  * short source -> translation wider than ABS_MAX columns
  * medium source -> translation more than REL_MAX times wider

Two kinds of source are exempt: long-form prose (>= PROSE_MIN columns, i.e.
Codex entries that live in a scrollable pane) and anything carrying an explicit
newline (multi-line system messages that are already broken up).

"Untranslated" means the value is byte-identical to an English prose string.
Values that merely contain no ideographs -- "...", "Esc", "[playername]..." --
are fine: they were still localised (ellipsis form, key label, tag).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games  # noqa: E402

TAGS = ["i", "b", "u", "s"]
CJK = re.compile(r"[\u2e80-\u9fff\uac00-\ud7af\u3000-\u303f\uff00-\uffef]")

ABS_MAX = 130        # columns one dialogue line holds at 1080p
REL_MAX = 2.0        # tolerated growth for short/medium lines
PROSE_MIN = 200      # >= this many source columns == Codex-style prose

# Kept verbatim on purpose: mirror-writing props, third-party module credits,
# Patreon/supporter names and font names. These are names, not prose.
KEEP_EXACT = {
    "Nuqien sere?", "On em sentiende?", "Nev ereh",
    "DejaVu Sans", "Opendyslexic", "FnB Productions",
    # the game's own title, the studio's initials, and keyword names that show
    # up inside the bundled Kinetic Text Tags documentation code samples
    "Eden", "FnB", "F", "B", "color=", "size=", "font=",
    # a cat noise kept in its original language on purpose
    "MIAU",
    "Kinetic Text Tags Ren'Py Module 2021 Daniel Westfall "
    "<SoDaRa2595@gmail.com>",
    "ATL Text Tags Ren'Py Module 2021 Daniel Westfall "
    "<SoDaRa2595@gmail.com>",
    "Mr. Ovis", "Bradley Lowe", "The Neuronaut", "Howl Pendragon",
    "John Israel", "Aern Drath", "Morte Nera", "Vic Hedges",
    "Simon M\u00e4gi", "Chris Baylock", "frodo gamgee", "26TriAxis",
    "Kevin F\u00f6rster", "Pickle (Great hair mods btw!)",
    "Hesby's femboy factory",
}

# Shapes that must survive verbatim even though they look translatable.
KEEP = re.compile(
    r"^(\s*(\[.+\]|\{.+\}))+(\\n)?\s*$"        # [playername] / {font=...}
    r"|^\{.+\}%[A-Za-z%]"                        # strftime template
    r"|^\d[\d\s.,:/+-]*$"                       # pure numeric combo
    r"|^%\(?[a-zA-Z]"                          # printf-style
    r"|^https?://"
    r"|^[A-Za-z]:[\\/]"
    r"|^[\w./\\-]*\.(py|rpy|json|png|jpg|mo3|mp|txt|ttf|otf|ttc|ini|cfg)$"
    r"|^(Ctrl|Shift|Alt|Enter|Tab|Esc|Escape|Page Up|Page Down|Home|End)$"
    r"|^(Shift|Ctrl|Alt)\+[A-Za-z]$"
    r"|^[\u2b00-\u2bff\u2190-\u21ff\u2026\s]+$"
    r"|^(?=.*[0-9%:/\\.])[A-Za-z0-9%.:#,/*+_=<>()\[\]{}-]+$"
)

fail = 0


def bad(msg):
    global fail
    fail += 1
    print("FAIL  " + msg)


def width(s):
    return sum(2 if CJK.match(ch) else 1 for ch in str(s))


def keep(k, v):
    return k == v and (k in KEEP_EXACT or KEEP.search(k) is not None)


def exempt(k):
    return width(k) >= PROSE_MIN or "\\n" in k or "\n" in k


def check_glossary(tr, glossary):
    """docs/glossary.json pins the wording of proper nouns.

    The game script itself calls Divinarch and Celestiarch by two different
    English names for the same six beings; nothing but a pinned glossary stops
    a future pass from splitting them into two Chinese words again.
    """
    if not os.path.isfile(glossary):
        bad("%s is missing" % os.path.relpath(glossary, games.ROOT))
        return
    g = json.load(open(glossary, encoding="utf-8-sig"))
    for section, terms in g.items():
        if section.startswith("_"):
            continue
        for en, spec in terms.items():
            canonical = spec["zh"]
            for variant in spec.get("banned", []):
                hits = [k for k, v in tr.items()
                        if variant in str(v).replace(canonical, "")]
                if hits:
                    bad("%s: %r should be %r, found %r in %d entry/entries "
                        "(e.g. %r)"
                        % (section, variant, canonical, variant,
                           len(hits), hits[0][:50]))


def check_doubling(tr, glossary):
    """Catch terms whose last character got typed twice, e.g. 神谕者者.

    Driven off the game's own docs/glossary.json. Only the exact shape "term + term's last
    character" counts -- a bare "CC" scan would flag 克拉拉, 莉莉 and 谢谢.
    """
    if not os.path.isfile(glossary):
        return
    g = json.load(open(glossary, encoding="utf-8-sig"))
    seen = set()
    for section, terms in g.items():
        if section.startswith("_"):
            continue
        for en, spec in terms.items():
            z = spec["zh"]
            if len(z) < 2 or z in seen:
                continue
            seen.add(z)
            tail = z + z[-1]
            hits = [k for k, v in tr.items() if tail in str(v)]
            if hits:
                bad("doubled term %r (from %r) in %d entry/entries, e.g. %r"
                    % (tail, en, len(hits), hits[0][:50]))


def main(argv):
    slug, _ = games.take_slug(argv)
    game, manifest = games.manifest(slug)
    lang = manifest["language"]
    trans = games.path_of(game, "data", "tl_trans.json")
    out = games.path_of(game, "patch", "tl", lang)
    shim = games.path_of(game, "patch", manifest["shim"])
    glossary = games.path_of(game, "docs", "glossary.json")

    tr = json.load(open(trans, encoding="utf-8"))

    empty = [k for k, v in tr.items() if not str(v).strip()]
    if empty:
        bad("%d empty translation(s): %r" % (len(empty), empty[:5]))

    moji = [k for k, v in tr.items() if "\ufffd" in str(v)]
    if moji:
        bad("%d translation(s) contain U+FFFD: %r" % (len(moji), moji[:3]))

    untranslated = [k for k, v in tr.items() if not keep(k, v) and v == k]
    if untranslated:
        bad("%d entry/entries still in English: %r"
            % (len(untranslated), untranslated[:8]))

    doubles = [(k, v) for k, v in tr.items()
               if re.search(r"[\u4e00-\u9fff]  +[\u4e00-\u9fff]", str(v))]
    if doubles:
        bad("%d translation(s) with a doubled space: %r"
            % (len(doubles), [k[:40] for k, _ in doubles[:3]]))

    overflow, stretched = [], []
    for k, v in tr.items():
        if not CJK.search(str(v)) or exempt(k):
            continue
        wk, wv = width(k), width(v)
        if wv > ABS_MAX:
            overflow.append((k, v))
        elif wk >= 12 and wv > wk * REL_MAX:
            stretched.append((k, v))
    if overflow:
        bad("%d translation(s) wider than %d columns: %r"
            % (len(overflow), ABS_MAX, [k[:40] for k, _ in overflow[:3]]))
    if stretched:
        bad("%d translation(s) over %gx the source width: %r"
            % (len(stretched), REL_MAX, [k[:40] for k, _ in stretched[:3]]))

    nfiles = nlines = 0
    for dirpath, _, fns in os.walk(out):
        for fn in sorted(fns):
            if not fn.endswith(".rpy"):
                continue
            nfiles += 1
            rel = os.path.relpath(os.path.join(dirpath, fn), out)
            rel = rel.replace(os.sep, "/")
            text = open(os.path.join(dirpath, fn), encoding="utf-8-sig").read()
            nlines += text.count("\n")
            for tag in TAGS:
                n = len(re.findall(r"\[/?%s\]" % tag, text))
                if n % 2:
                    bad("%s: unbalanced [%s] tags (%d)" % (rel, tag, n))

    check_glossary(tr, glossary)
    check_doubling(tr, glossary)

    if not os.path.isfile(shim):
        bad("%s is missing" % os.path.relpath(shim, games.ROOT))

    print("%s [%s]" % (manifest["title"], lang))
    print("translations: %d" % len(tr))
    print("patch files:  %d" % nfiles)
    print("patch lines:  %d" % nlines)
    print("")
    print("all checks passed" if not fail else "%d problem(s)" % fail)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
