# -*- coding: utf-8 -*-
"""Report translations that were pasted onto the wrong line.

    python tools/audit_paste.py --game <slug> | --all [--sim 0.55] [--fail]

check.py answers "is this line translated, and does it fit". It cannot answer
"does this line mean what it says" -- a translation copied over from its
neighbour passes every check there is. Three shipped that way before this tool
existed, in two different games.

The tell is the same Chinese wording sitting on two English lines that have
nothing to do with each other. Near-synonym collapses ("I know, I know." /
"Yeah, yeah.") look identical from the Chinese side, so the English similarity
decides: below --sim the pair is worth a human read, above it the translator
was simply being economical.

Pairing is by (line number, ordinal within the line), because that is the only
slot that survives translation. build_tl.py rewrites the text inside the quotes
and leaves the rest of the line alone, so line N's second quoted run is line N's
second quoted run in both trees -- but its start and end offsets are not, since
Chinese and English are different lengths. Keying on offsets matches almost
nothing; pairing a whole line against another whole line cross-multiplies the
slots and turns every two-string line into four bogus pairs.

Every hit needs a human decision, so this prints a report and exits 0; --fail
turns a hit into an error.
"""
import argparse
import collections
import os
import re
import sys
from difflib import SequenceMatcher

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check           # noqa: E402
import games           # noqa: E402
import tlparse         # noqa: E402

PUNCT = re.compile(r"[\s，。、！？…—\"',.;:!?“”‘’()（）\-~～…]+")


def norm(text):
    """Fold punctuation and spacing away so only the wording is compared."""
    return PUNCT.sub("", text)


def pairs(game_dir, manifest):
    """-> [(english, chinese, "rel:line")] or None when there is no template."""
    template = games.path_of(game_dir, "tl_template")
    patch = games.path_of(game_dir, "patch", "tl", manifest["language"])
    if not os.path.isdir(template):
        return None
    tmpl = tlparse.load(template)[0]
    done = tlparse.load(patch)[0]
    out = []
    for rel, (_, edits) in tmpl.items():
        if rel not in done:
            continue
        slots = collections.defaultdict(list)
        for (i, _s, _e, _q, text) in done[rel][1]:
            slots[i].append(text)
        seen_lines = collections.defaultdict(int)
        for (i, _s, _e, _q, en) in edits:
            nth = seen_lines[i]
            seen_lines[i] = nth + 1
            column = slots.get(i, ())
            if nth < len(column):
                out.append((en, column[nth], "%s:%d" % (rel, i + 1)))
    return out


def report(game_dir, manifest, sim, min_len, verbose):
    slug = manifest["slug"]
    ps = pairs(game_dir, manifest)
    if ps is None:
        print("%-20s skipped: no tl_template/ (not a tl-blocks game)" % slug)
        return 0

    # key on the Chinese, then keep only pairs where the Chinese is actually
    # prose: no CJK means it is a colour literal or a code snippet, and two
    # files agreeing on "#ff00f0" is not a translation problem.
    buckets = {}
    for en, zh, where in ps:
        key = norm(zh)
        if not check.CJK.search(zh) or len(key) < min_len:
            continue
        buckets.setdefault(key, {}).setdefault(en, []).append(where)

    seen, hits = set(), []
    for key, by_en in buckets.items():
        items = sorted(by_en.items())
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                (ea, wa), (eb, wb) = items[i], items[j]
                r = SequenceMatcher(None, ea, eb).ratio()
                if r >= sim:
                    continue
                fingerprint = (key, tuple(sorted((ea, eb))))
                if fingerprint in seen:
                    continue
                seen.add(fingerprint)
                hits.append((r, key, ea, wa, eb, wb))
    hits.sort()

    print("%-20s %6d pairs, %d distinct pairs to read (English similarity < %.2f)"
          % (slug, len(ps), len(hits), sim))
    for r, key, ea, wa, eb, wb in hits[:None if verbose else 15]:
        print("  sim=%.2f  同一个译文挂在两句无关的原文上" % r)
        print("    EN %-72s %s" % (ea[:72], wa[0] if len(wa) == 1 else "%d 处" % len(wa)))
        print("    ZH %s" % key[:72])
        print("    EN %-72s %s" % (eb[:72], wb[0] if len(wb) == 1 else "%d 处" % len(wb)))
    if len(hits) > 15 and not verbose:
        print("  ... %d more; pass --all-hits to see them" % (len(hits) - 15))
    return len(hits)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--game", help="audit one game")
    ap.add_argument("--all", action="store_true", help="audit every game in the repo")
    ap.add_argument("--sim", type=float, default=0.55,
                    help="flag English lines less similar than this (default 0.55)")
    ap.add_argument("--min-len", type=int, default=6,
                    help="ignore Chinese shorter than this after folding (default 6)")
    ap.add_argument("--all-hits", action="store_true", help="do not truncate the report")
    ap.add_argument("--fail", action="store_true", help="exit 1 when anything is flagged")
    args = ap.parse_args(argv)
    if not args.game and not args.all:
        ap.error("pass --game <slug> or --all")

    total = 0
    for slug in (games.slugs() if args.all else [args.game]):
        game_dir, manifest = games.manifest(slug)
        total += report(game_dir, manifest, args.sim, args.min_len, args.all_hits)
        print()
    return 1 if (args.fail and total) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
