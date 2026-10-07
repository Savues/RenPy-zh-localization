# -*- coding: utf-8 -*-
"""Build patch/tl/schinese from tl_template/ + data/tl_trans.json.

    python tools/build_tl.py

Requires tl_template/ (the game's own untranslated game/tl/schinese/*.rpy).
Run `python tools/template.py <game-dir>` first if you do not have it.
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tlparse  # noqa: E402

OUT = os.path.join(tlparse.ROOT, "patch", "tl", "schinese")
TRANS = os.path.join(tlparse.ROOT, "data", "tl_trans.json")
TEMPLATE = os.path.join(tlparse.ROOT, "tl_template")


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


def main():
    if not os.path.isdir(TEMPLATE):
        sys.exit("tl_template/ missing -- run: python tools/template.py <game-dir>")
    tlparse.TL = TEMPLATE

    files, order = tlparse.load()
    tr = {}
    if os.path.exists(TRANS):
        import json
        tr = json.load(open(TRANS, encoding="utf-8"))

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
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
        dest = os.path.join(OUT, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8", newline="\n") as f:
            f.write("\ufeff")
            f.write("\n".join(lines))

    total = sum(len(edits) for _, edits in files.values())
    print("applied: %d / %d" % (applied, total))
    print("still untranslated: %d (%d chars)" % (missing, missing_chars))
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
