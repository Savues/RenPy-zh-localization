# -*- coding: utf-8 -*-
"""Build a game's patch/tl/<lang>/ from its tl_template/ + data/tl_trans.json.

    python tools/build_tl.py [--game <slug>]

Requires the game folder to contain tl_template/ (the original English
templates, imported by tools/template.py).
"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games          # noqa: E402
import tlparse        # noqa: E402


def esc(s, q):
    """Escape bare quote characters; leave existing \\X escape pairs intact."""
    out = []
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c == "\\" and i + 1 < n:
            out.append(s[i:i + 2])
            i += 2
            continue
        out.append("\\" + q if c == q else c)
        i += 1
    return "".join(out)


def main(argv):
    slug, _ = games.take_slug(argv)
    game, manifest = games.manifest(slug)
    lang = manifest["language"]

    template = games.path_of(game, "tl_template")
    out = games.path_of(game, "patch", "tl", lang)
    trans = games.path_of(game, "data", "tl_trans.json")

    if not os.path.isdir(template):
        if games.layout(manifest) != "tl-blocks":
            sys.exit(
                "%s is patched by script override (patch_layout=script-override).\n"
                "  patch/ already holds the finished scripts, so there is nothing\n"
                "  to compile. Run:\n"
                "    python tools/check.py --game %s\n"
                "  See docs/adding-a-game.md."
                % (manifest["title"], manifest["slug"]))
        sys.exit("%s is missing -- run: python tools/template.py <renpy-game-dir>"
                 " --game %s" % (template, manifest["slug"]))

    files, order = tlparse.load(template)
    tr = json.load(open(trans, encoding="utf-8")) if os.path.exists(trans) else {}

    if os.path.isdir(out):
        shutil.rmtree(out)
    applied = missing = missing_chars = 0
    for rel in order:
        lines, edits = files[rel]
        lines = list(lines)
        for (i, s, e, q, text) in edits:
            z = tr.get(text)
            if not z:
                missing += 1
                missing_chars += len(text)
                continue
            lines[i] = lines[i][:s] + esc(z, q) + lines[i][e:]
            applied += 1
        dest = os.path.join(out, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8", newline="\n") as f:
            f.write("\ufeff")
            f.write("\n".join(lines))

    total = sum(len(edits) for _, edits in files.values())
    print("%s [%s]" % (manifest["title"], lang))
    print("applied: %d / %d" % (applied, total))
    print("still untranslated: %d (%d chars)" % (missing, missing_chars))
    print("written to %s" % os.path.relpath(out, games.ROOT))
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
