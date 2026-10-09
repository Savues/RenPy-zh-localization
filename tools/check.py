# -*- coding: utf-8 -*-
"""Validate the patch a game actually ships, in the shape that game is patched.

    python tools/check.py --game <slug>

Run this before every release. Exit code 0 = clean, 1 = problems found.

Two patch layouts live under games/ and they are not checked the same way,
because "the translation" is a different object in each one -- docs/adding-a-game.md
says when to pick which, and no rule here assumes the first one:

  tl-blocks       patch/tl/<lang>/ holds generated `translate` blocks and
                  data/tl_trans.json is the input build_tl.py compiles. Six
                  checks run over that database -- empty, mojibake,
                  untranslated, doubled space and two width rules -- and the
                  glossary is enforced against the same database.

  script-override the game ships no translation templates, so the patch
                  replaces the game's own scripts and any data/tl_trans.json
                  is a by-product reverse-derived from the finished scripts,
                  not a build input. Grading that dictionary would be the
                  patch marking its own homework, so it is not read at all.
                  The shipped scripts are checked instead: mojibake and
                  doubled spaces across the whole patch, then the same
                  glossary and doubling rules. Everything that needs the
                  English original to judge -- "is this line translated?",
                  "did it outgrow its box?" -- is deliberately NOT asserted
                  here. game.json's coverage field carries that number instead.

Either way the patch tree is enumerated through games.patch_entries(). An
earlier version walked patch/tl/<lang>/ directly, which is why the
script-override game reported "patch files: 0" and had tag balance never run
against the 27 files it actually ships.

Length is measured in *rendered columns*, not characters: a CJK glyph renders
about twice as wide as a Latin one, so "H-how..." (6 columns) legitimately
becomes 12 columns of Chinese without any risk of overflow. What would
actually break a line is a translation that outgrows the box, so that is what
gets flagged:

  * translation both wider than ABS_MAX columns AND wider than its source
  * medium source -> translation more than REL_MAX times wider

The first rule only fires on growth: a Chinese line of 138 columns is 69
ideographs, which fits. If the English line it replaces already rendered at
194 columns, the shorter Chinese is not an overflow.

Two kinds of source are exempt: long-form prose (>= PROSE_MIN columns, i.e.
Codex entries that live in a scrollable pane) and anything carrying an explicit
newline (multi-line system messages that are already broken up).

"Untranslated" means the value is byte-identical to an English prose string.
Values that merely contain no ideographs -- "...", "Esc", "[playername]..." --
are fine: they were still localised (ellipsis form, key label, tag). Strings a
patch leaves in English on purpose are listed per game under _kept_verbatim in
that game's own docs/glossary.json, never here: a shared table drifted into
counting one game's supporter credits and another game's RGB picker format
strings as prose, which is the kind of cross-game rule this split removes.
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games  # noqa: E402

TAGS = ["i", "b", "u", "s"]
CJK = re.compile(r"[\u2e80-\u9fff\uac00-\ud7af\u3000-\u303f\uff00-\uffef]")

ABS_MAX = 130        # columns one dialogue line holds at 1080p
REL_MAX = 2.0        # tolerated growth for short/medium lines
PROSE_MIN = 200      # >= this many source columns == Codex-style prose

# Verbatim on every game, because these are Ren'Py conventions rather than any
# one game's wording. Keep this list that short: anything a particular patch
# keeps in English belongs in that game's docs/glossary.json, where the reason
# for it is written down next to the other terminology decisions.
KEEP_EXACT = {"<", ">"}

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


# scan() collects every hit so a game can exempt specific places by name;
# this bounds the list when a banned variant has gone badly wrong.
WHERE_CAP = 2000


def keep(k, v, exact=()):
    """True when k == v reads as a decision instead of an unfinished line."""
    if k != v:
        return False
    return k in exact or k in KEEP_EXACT or KEEP.search(k) is not None


def exempt(k):
    return width(k) >= PROSE_MIN or "\\n" in k or "\n" in k


# ---------------------------------------------------------------------------
# What the glossary rules are matched against. A tl-blocks game is checked
# through its translation database; a script-override game through the scripts
# it ships. Both answer the same one question -- "does this needle appear in
# the text the player sees?" -- so both expose the same scan() signature.
# ---------------------------------------------------------------------------
def db_corpus(tr):
    """-> scan(needle, strip) -> (hits, [where it was found]).

    strip is the glossary's own canonical spelling, removed before searching:
    otherwise a banned variant that is merely a prefix of the canonical (艾莉
    inside 艾莉森) fires on every correct spelling.
    """
    def scan(needle, strip=None):
        hits, where = 0, []
        for k, v in tr.items():
            text = str(v)
            if strip:
                text = text.replace(strip, "")
            if needle in text:
                hits += 1
                if len(where) < WHERE_CAP:
                    where.append(k)
        return hits, where
    return scan


def script_corpus(scripts):
    """Same signature as db_corpus, over every .rpy the patch ships."""
    def scan(needle, strip=None):
        hits, where = 0, []
        for rel, text in scripts:
            if strip:
                text = text.replace(strip, "")
            hits += text.count(needle)
            at = 0
            while True:
                i = text.find(needle, at)
                if i < 0:
                    break
                if len(where) < WHERE_CAP:
                    where.append("%s:%d" % (rel, text.count("\n", 0, i) + 1))
                at = i + len(needle)
        return hits, where
    return scan


def load_scripts(entries):
    """-> [(relative path, text)] for every script in the patch."""
    out = []
    for src, rel in entries:
        if src.endswith(".rpy"):
            with open(src, encoding="utf-8-sig") as f:
                out.append((rel, f.read()))
    return out


def check_database(tr, exact):
    """The six checks that only a build input can answer. tl-blocks only."""
    empty = [k for k, v in tr.items() if not str(v).strip()]
    if empty:
        bad("%d empty translation(s): %r" % (len(empty), empty[:5]))

    moji = [k for k, v in tr.items() if "\ufffd" in str(v)]
    if moji:
        bad("%d translation(s) contain U+FFFD: %r" % (len(moji), moji[:3]))

    untranslated = [k for k, v in tr.items() if not keep(k, v, exact) and v == k]
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
        if wv > ABS_MAX and wv > wk:
            overflow.append((k, v))
        elif wk >= 12 and wv > wk * REL_MAX:
            stretched.append((k, v))
    if overflow:
        bad("%d translation(s) wider than %d columns: %r"
            % (len(overflow), ABS_MAX, [k[:40] for k, _ in overflow[:3]]))
    if stretched:
        bad("%d translation(s) over %gx the source width: %r"
            % (len(stretched), REL_MAX, [k[:40] for k, _ in stretched[:3]]))


def check_scripts(scripts):
    """The same two checks, run on finished scripts instead of a database.

    A space between two ideographs cannot happen in Ren'Py's ASCII code, so
    this stays a dialogue-line check even though it sees whole files.
    """
    moji = [(rel, text.count("\ufffd"))
            for rel, text in scripts if "\ufffd" in text]
    if moji:
        bad("%d script(s) contain U+FFFD: %r" % (len(moji), moji[:3]))

    doubles = []
    for rel, text in scripts:
        for i, line in enumerate(text.split("\n"), 1):
            if re.search(r"[\u4e00-\u9fff]  +[\u4e00-\u9fff]", line):
                doubles.append("%s:%d" % (rel, i))
    if doubles:
        bad("%d script line(s) with a doubled space: %r"
            % (len(doubles), doubles[:5]))


def check_glossary(scan, glossary):
    """docs/glossary.json pins the wording of proper nouns.

    The game script itself calls Divinarch and Celestiarch by two different
    English names for the same six beings; nothing but a pinned glossary stops
    a future pass from splitting them into two Chinese words again.

    A banned variant is matched as a bare substring, so it also fires on a
    longer correct term that merely contains it -- 军士长 inside 一级军士长
    (Command Sergeant Major, a different rank) is the case that needed it. Such
    a game lists the exact places under _banned_exempt, keyed by the variant,
    each with the reason; anywhere else still fails.
    """
    if not os.path.isfile(glossary):
        bad("%s is missing" % os.path.relpath(glossary, games.ROOT))
        return
    g = json.load(open(glossary, encoding="utf-8-sig"))
    exempt = g.get("_banned_exempt") or {}
    for section, terms in g.items():
        if section.startswith("_") or not isinstance(terms, dict):
            continue
        for en, spec in terms.items():
            canonical = spec["zh"]
            for variant in spec.get("banned", []):
                # Strip the canonical first so that its own occurrences do not
                # count -- but only when the variant does not build on it, or
                # "熟女少妇" would be reduced to "少妇" and never match.
                strip = None if canonical in variant else canonical
                hits, where = scan(variant, strip)
                allow = set(exempt.get(variant, {}).get("at", ()))
                if allow and hits <= len(where):
                    if len([w for w in where if w in allow]) == hits:
                        continue
                if hits:
                    bad("%s: %r should be %r, found %r in %d place(s) (e.g. %s)"
                        % (section, variant, canonical, variant, hits, where[0]))


def check_doubling(scan, glossary, skip=()):
    """Catch terms whose last character got typed twice, e.g. 神谕者者.

    Driven off the game's own docs/glossary.json. Only the exact shape "term +
    term's last character" counts -- a bare "CC" scan would flag 克拉拉, 莉莉 and
    谢谢. Two-character terms are the ones that lie: 「校长 长得」reads as 校长长
    and 「把莎拉拉近一点」is 莎拉 + 拉近. A game lists those under
    _doubling_exempt with the reason, rather than this check guessing.
    """
    if not os.path.isfile(glossary):
        return
    g = json.load(open(glossary, encoding="utf-8-sig"))
    seen = set()
    for section, terms in g.items():
        if section.startswith("_") or not isinstance(terms, dict):
            continue
        for en, spec in terms.items():
            z = spec["zh"]
            if len(z) < 2 or z in seen or z in skip:
                continue
            seen.add(z)
            tail = z + z[-1]
            hits, where = scan(tail)
            if hits:
                bad("doubled term %r (from %r) in %d place(s), e.g. %s"
                    % (tail, en, hits, where[0]))


def check_patch(entries, exempt=()):
    """Tag balance over the patch tree, whichever layout produced it.

    Lines listed in the game's _tag_exempt are left out of the tally, so what
    is reported is the imbalance the patch introduced rather than the one the
    game's own English shipped with. Counting stays whole-file: a tag opened on
    one line and closed on another still balances.
    """
    skip = set(exempt)
    nfiles = nlines = 0
    for src, rel in entries:
        if not src.endswith(".rpy"):
            continue
        nfiles += 1
        with open(src, encoding="utf-8-sig") as f:
            text = f.read()
        nlines += text.count("\n")
        for tag in TAGS:
            pattern = re.compile(r"\[/?%s\]" % tag)
            n = sum(len(pattern.findall(line)) for line in text.split("\n")
                    if line.strip() not in skip)
            if n % 2:
                bad("%s: unbalanced [%s] tags (%d)" % (rel, tag, n))
    return nfiles, nlines


def check_shipping(game, manifest):
    """The files a player has to be able to find after unpacking."""
    shim = games.path_of(game, "patch", manifest["shim"])
    if not os.path.isfile(shim):
        bad("%s is missing" % os.path.relpath(shim, games.ROOT))
    for asset, names in games.font_plan(manifest):
        src = games.path_of(game, *asset.split("/"))
        if not os.path.isfile(src):
            bad("font asset %s is missing (should ship as %s)"
                % (asset, ", ".join(names)))


def run_extra_checks(game, manifest):
    """Run whatever game.json lists in extra_checks, from the game's own dir.

    A patch layout only needs the checks that layout can answer. A
    script-override game additionally knows things about its own scripts that
    no shared rule has any business guessing -- this repository's Cosy Cafe
    patch checks the WeekDays enum there, because the bug that produced it was
    a write-back script mis-placing a literal and no generic linter can see
    that. Each game owns that script; game.json only says how to run it.
    """
    for argv in manifest.get("extra_checks", []):
        argv = list(argv)
        r = subprocess.run(argv, cwd=game, capture_output=True,
                           encoding="utf-8", errors="replace")
        if r.returncode:
            bad("extra check failed: %s (exit %d)\n%s"
                % (" ".join(argv), r.returncode,
                   (r.stdout + r.stderr).strip()[-2000:]))
        else:
            print("extra: %s -- %s"
                  % (" ".join(argv), (r.stdout or "").strip().split("\n")[-1][:100]))


def main(argv):
    slug, _ = games.take_slug(argv)
    game, manifest = games.manifest(slug)
    shape = games.layout(manifest)
    exact = games.kept_verbatim(game)
    entries = games.patch_entries(game, manifest)
    scripts = load_scripts(entries)

    if shape == "tl-blocks":
        trans = games.path_of(game, "data", "tl_trans.json")
        if not os.path.isfile(trans):
            bad("%s is missing" % os.path.relpath(trans, games.ROOT))
            tr = {}
        else:
            tr = json.load(open(trans, encoding="utf-8"))
        check_database(tr, exact)
        scan = db_corpus(tr)
        ntr = len(tr)
    else:
        # Not a judgement about quality: with no build input there is nothing to
        # compare a line against, and reverse-derived data would only ever
        # agree with the patch by construction.
        check_scripts(scripts)
        scan = script_corpus(scripts)
        ntr = 0

    nfiles, nlines = check_patch(entries, games.tag_exempt(game))
    check_glossary(scan, games.path_of(game, "docs", "glossary.json"))
    check_doubling(scan, games.path_of(game, "docs", "glossary.json"),
                   games.doubling_exempt(game))
    check_shipping(game, manifest)
    run_extra_checks(game, manifest)

    print("%s [%s]  (%s)" % (manifest["title"], manifest["language"], shape))
    if ntr:
        print("translations: %d" % ntr)
    else:
        cov = manifest.get("coverage")
        print("coverage:     %s (asserted in game.json, not re-derived here)"
              % ("%d / %d" % (cov["translated"], cov["total"]) if cov else "n/a"))
    print("package:      %s (this game's own version, not the release tag)"
          % games.package_version(manifest))
    print("patch files:  %d" % nfiles)
    print("patch lines:  %d" % nlines)
    print("")
    print("all checks passed" if not fail else "%d problem(s)" % fail)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
