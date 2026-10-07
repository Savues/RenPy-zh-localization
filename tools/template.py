# -*- coding: utf-8 -*-
"""Import the game's own (untranslated) Ren'Py language templates.

    python tools/template.py "<path-to-Eden-Chapter5-pc>"

Copies `<game>/game/tl/schinese` -> `tl_template/`. The templates are the
original English script wrapped in `translate schinese ...` blocks; they are
part of the game and are therefore NOT committed to this repository
(see .gitignore). Only the translated output (patch/) and the translation
database (data/tl_trans.json) are tracked.
"""
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(ROOT, "tl_template")

CJK = re.compile(r"[\u4e00-\u9fff]")


def game_dir(arg):
    path = os.path.abspath(arg)
    if os.path.isdir(os.path.join(path, "game")):
        return path
    if os.path.basename(path) == "game":
        return os.path.dirname(path)
    sys.exit("not a Ren'Py game directory: %s" % arg)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    game = game_dir(sys.argv[1])
    src = os.path.join(game, "game", "tl", "schinese")
    if not os.path.isdir(src):
        sys.exit("no game/tl/schinese in %s -- run the Ren'Py SDK's "
                 "languagetool on this game first" % game)

    # Guard against importing an already-patched game as if it were a template.
    probe = [os.path.join(src, n) for n in ("common.rpy", "options.rpy")]
    probe = [p for p in probe if os.path.exists(p)]
    for p in probe:
        head = open(p, encoding="utf-8-sig", errors="replace").read(40000)
        if CJK.search(head):
            sys.exit("%s already contains Chinese -- point this at a clean, "
                     "unpatched copy of the game" % p)

    if os.path.isdir(DEST):
        shutil.rmtree(DEST)
    shutil.copytree(src, DEST, ignore=shutil.ignore_patterns("*.rpyc", "*.rpymc"))

    files = [os.path.relpath(os.path.join(d, f), DEST)
             for d, _, fs in os.walk(DEST) for f in fs if f.endswith(".rpy")]
    print("imported %d template files into tl_template/" % len(files))
    with open(os.path.join(DEST, ".source.json"), "w", encoding="utf-8") as f:
        json.dump({"game": game, "files": len(files)}, f, indent=2)


if __name__ == "__main__":
    main()
