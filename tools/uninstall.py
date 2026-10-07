# -*- coding: utf-8 -*-
"""Remove an installed patch and restore the original files.

    python tools/uninstall.py "<path-to-the-game>" [--game <slug>]
    python tools/uninstall.py "<path-to-the-game>" --purge-backup

The list of touched files comes from the manifest the installer wrote into
game/.zh_patch_backup/, so this works even for a game whose folder has since
been renamed or whose manifest has drifted. It reads installers other than
this repository's own too: a game that ships its own install.ps1 records the
same "files" list, and uninstall.py will happily undo it.
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


def touched(game, repo, manifest):
    """Paths an installer may have written, relative to the game folder.

    Three cases, in decreasing order of trust:

      * "files"  -- written by install.py v2 and by the game-local install.ps1
        scripts. Exactly what was written, so it is right for a
        script-override patch and for a translation tree alike.
      * the v1 shape -- lang/shim/fonts from the old install.py. Kept so a
        game installed before the bump still uninstalls.
      * nothing  -- the patch was copied over by hand. Fall back to "every
        path this game's patch would place", derived from game.json rather
        than from a hardcoded list that only ever matched one game.
    """
    mpath = games.path_of(game, BACKUP, "manifest.json")
    if os.path.isfile(mpath):
        with open(mpath, encoding="utf-8-sig") as f:
            m = json.load(f)
        if isinstance(m.get("files"), list):
            return list(m["files"]), m
        lang = m.get("lang", manifest["language"])
        shim = m.get("shim", manifest["shim"])
        fonts = m.get("fonts")
        return (["tl/%s" % lang, shim]
                + ["fonts/%s" % n for n in (fonts if isinstance(fonts, list)
                                            else [])],
                m)

    expected = [rel for _, rel in games.patch_entries(repo, manifest)]
    expected += ["fonts/%s" % n for _, ns in games.font_plan(manifest)
                 for n in ns]
    return expected, {}


def restore(game, rel):
    """Put back game/<rel> from the backup, or delete it if there was none.

    A zero-byte backup counts as "there was none". install.py records nothing
    at all for a file the patch introduced; the game-local install.ps1 scripts
    drop a zero-byte placeholder instead. Treating both the same way is what
    keeps uninstall from leaving stray empty scripts behind -- a 0-byte .rpy
    is not something a Ren'Py game ships.
    """
    dst = games.path_of(game, rel)
    src = games.path_of(game, BACKUP, rel.replace("/", os.sep))
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    if os.path.isdir(src):
        shutil.copytree(src, dst,
                        ignore=shutil.ignore_patterns("*.rpyc", "*.rpymc"))
        print("  restored  %s/" % rel)
    elif os.path.isfile(src) and os.path.getsize(src):
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

    repo, m = games.manifest(slug)
    game = resolve_game(rest[0])
    bdir = games.path_of(game, BACKUP)
    if not os.path.isdir(bdir):
        die("no %s in %s -- this game does not look patched by us"
            % (BACKUP, game))

    rels, manifest = touched(game, repo, m)
    label = ""
    if manifest.get("game"):
        label = "  (%s)" % manifest["game"]

    print("removing patch from %s%s" % (game, label))
    for rel in rels:
        restore(game, rel)

    # Restoring can empty out directories the installer created. Prune them
    # bottom-up so "is anything left to keep?" asks about real backups rather
    # than about folder scaffolding.
    for dirpath, _, _ in os.walk(bdir, topdown=False):
        if dirpath != bdir and not os.listdir(dirpath):
            os.rmdir(dirpath)

    left = [r for r in os.listdir(bdir) if r != "manifest.json"]
    if purge or not left:
        shutil.rmtree(bdir)
        print("  removed   %s/" % BACKUP)
    else:
        print("\nkept %d backed-up originals in %s/ (%s)"
              % (len(left), BACKUP, ", ".join(sorted(left))))


if __name__ == "__main__":
    main(sys.argv[1:])
