# -*- coding: utf-8 -*-
"""Remove the Eden Chapter 5 Chinese patch and restore the original files.

    python tools/uninstall.py "<path-to-game>"
    python tools/uninstall.py "<path-to-game>" --purge-backup
"""
import json
import os
import shutil
import sys

BACKUP = ".zh_patch_backup"
PATCHED = ["tl/schinese", "zz_zh_locale.rpy"]
PATCHED_FONTS = ["fonts/zh.ttf", "fonts/comfortaa.ttf",
                 "fonts/CinzelDecorative.ttf",
                 "fonts/MichromaRegular.ttf",
                 "fonts/PacificoRegular.ttf"]


def die(msg):
    sys.exit("error: " + msg)


def resolve_game(arg):
    path = os.path.abspath(arg)
    if os.path.isdir(os.path.join(path, "game")):
        return os.path.join(path, "game")
    if os.path.basename(path) == "game":
        return path
    die("not a Ren'Py game directory: %s" % arg)


def restore(game, rel):
    """Put back game/<rel> from the backup, or delete it if there was none."""
    dst = os.path.join(game, rel)
    src = os.path.join(game, BACKUP, rel.replace("/", os.sep))
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    if os.path.isdir(src):
        shutil.copytree(src, dst,
                        ignore=shutil.ignore_patterns("*.rpyc", "*.rpymc"))
        print("  restored  %s/" % rel)
    elif os.path.isfile(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print("  restored  %s" % rel)
    elif os.path.exists(dst):
        os.remove(dst)
        print("  removed   %s" % rel)
    for ext in (".rpyc", ".rpymc"):
        stale = os.path.splitext(dst)[0] + ext
        if os.path.isfile(stale):
            os.remove(stale)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    purge = "--purge-backup" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)

    game = resolve_game(args[0])
    bdir = os.path.join(game, BACKUP)
    if not os.path.isdir(bdir):
        die("no %s in %s -- this game does not look patched by us"
            % (BACKUP, game))

    print("removing patch from %s" % game)
    for rel in PATCHED + PATCHED_FONTS:
        restore(game, rel)

    left = [r for r in os.listdir(bdir) if r != "manifest.json"]
    if purge or not left:
        shutil.rmtree(bdir)
        print("  removed   %s/" % BACKUP)
    else:
        print("\nkept %d backed-up originals in %s/ (%s)"
              % (len(left), BACKUP, ", ".join(sorted(left))))


if __name__ == "__main__":
    main()
