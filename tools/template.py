# -*- coding: utf-8 -*-
"""Import a game's own (untranslated) Ren'Py language templates.

    python tools/template.py "<path-to-the-game>" [--game <slug>]

Copies `<renpy-game>/game/tl/<lang>` -> `games/<slug>/tl_template/`. The
templates are the original English script wrapped in `translate <lang> ...`
blocks; they belong to the game and are therefore NOT committed (see
.gitignore). Only the translated output (patch/) and the translation database
(data/tl_trans.json) are tracked.
"""
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games  # noqa: E402

CJK = re.compile(r"[\u4e00-\u9fff]")


def renpy_game_dir(arg):
    path = os.path.abspath(arg)
    if os.path.isdir(os.path.join(path, "game")):
        return path
    if os.path.basename(path) == "game":
        return os.path.dirname(path)
    sys.exit("not a Ren'Py game directory: %s" % arg)


def main(argv):
    slug, rest = games.take_slug(argv)
    if len(rest) != 1:
        sys.exit(__doc__)
    game, manifest = games.manifest(slug)
    lang = manifest["language"]

    src = os.path.join(renpy_game_dir(rest[0]), "game", "tl", lang)
    if not os.path.isdir(src):
        sys.exit("no game/tl/%s there -- run the Ren'Py SDK's languagetool "
                 "on this game first" % lang)

    # Guard against importing an already-patched game as if it were a template.
    probe = [os.path.join(src, n) for n in ("common.rpy", "options.rpy")]
    for p in [p for p in probe if os.path.exists(p)]:
        head = open(p, encoding="utf-8-sig", errors="replace").read(40000)
        if CJK.search(head):
            sys.exit("%s already contains Chinese -- point this at a clean, "
                     "unpatched copy of the game" % p)

    dest = games.path_of(game, "tl_template")
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest,
                    ignore=shutil.ignore_patterns("*.rpyc", "*.rpymc"))

    files = [os.path.relpath(os.path.join(d, f), dest)
             for d, _, fs in os.walk(dest) for f in fs if f.endswith(".rpy")]
    print("imported %d template files into %s"
          % (len(files), os.path.relpath(dest, games.ROOT)))
    with open(os.path.join(dest, ".source.json"), "w", encoding="utf-8") as f:
        json.dump({"renpy_game": os.path.abspath(rest[0]), "files": len(files)},
                  f, indent=2)


if __name__ == "__main__":
    main(sys.argv[1:])
