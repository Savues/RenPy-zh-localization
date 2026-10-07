# -*- coding: utf-8 -*-
"""Remove an installed patch and restore the original files.

    python tools/uninstall.py "<path-to-the-game>" [--game <slug>]
    python tools/uninstall.py "<path-to-the-game>" --purge-backup

The list of touched files comes from the manifest install.py wrote into
game/.zh_patch_backup/, so this works even for a game whose folder has since
been renamed or whose manifest has drifted.
"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games  # noqa: E402

BACKUP = ".zh_patch_backup"


def die(msg):
    sys.exit("error: " + msg)


def resolve_game(arg):
    path = os.path.abspath(arg)
    if os.path.isdir(os.path.join(path, "game")):
        return os.path.join(path, "game")
    if os.path.basename(path) == "game":
        return path
    die("not a Ren'Py game directory: %s" % arg)


def touched(game):
    """Paths install.py may have written, relative to the game folder."""
    mpath = games.path_of(game, BACKUP, "manifest.json")
    if os.path.isfile(mpath):
        with open(mpath, encoding="utf-8") as f:
            m = json.load(f)
        return ["tl/%s" % m["lang"], m["shim"]] + ["fonts/%s" % n
                                                    for n in m["fonts"]], m
    # no manifest: fall back to whatever is lying around
    return (["tl/schinese", "zz_zh_locale.rpy"]
            + ["fonts/%s" % n for n in
               ("zh.ttf", "comfortaa.ttf", "CinzelDecorative.ttf",
                "MichromaRegular.ttf", "PacificoRegular.ttf")], {})


def restore(game, rel):
    """Put back game/<rel> from the backup, or delete it if there was none."""
    dst = games.path_of(game, rel)
    src = games.path_of(game, BACKUP, rel.replace("/", os.sep))
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


def main(argv):
    purge = "--purge-backup" in argv
    slug, rest = games.take_slug(argv)
    rest = [a for a in rest if a != "--purge-backup"]
    if len(rest) != 1:
        sys.exit(__doc__)

    game = resolve_game(rest[0])
    bdir = games.path_of(game, BACKUP)
    if not os.path.isdir(bdir):
        die("no %s in %s -- this game does not look patched by us"
            % (BACKUP, game))

    rels, manifest = touched(game)
    label = ""
    if manifest.get("game"):
        label = "  (%s)" % manifest["game"]

    print("removing patch from %s%s" % (game, label))
    for rel in rels:
        restore(game, rel)

    left = [r for r in os.listdir(bdir) if r != "manifest.json"]
    if purge or not left:
        shutil.rmtree(bdir)
        print("  removed   %s/" % BACKUP)
    else:
        print("\nkept %d backed-up originals in %s/ (%s)"
              % (len(left), BACKUP, ", ".join(sorted(left))))


if __name__ == "__main__":
    main(sys.argv[1:])
