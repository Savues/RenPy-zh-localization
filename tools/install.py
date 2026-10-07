# -*- coding: utf-8 -*-
"""Install a game patch from this repository into a Ren'Py game directory.

    python tools/install.py "<path-to-the-game>" [--game <slug>]
    python tools/install.py "<path-to-the-game>" --font "C:/Windows/Fonts/msyh.ttc"

What it does, for a game whose game.json says installer="py":
    1. game/tl/<lang>     <- games/<slug>/patch/tl/<lang>
    2. game/<shim>         <- games/<slug>/patch/<shim>
    3. game/fonts/*        <- the CJK faces bundled in the repo, written under
                              every filename the game looks them up under
                              (game.json), so script and release-zip installs
                              render identically

Anything it overwrites is copied to game/.zh_patch_backup/ first; run
tools/uninstall.py to put the game back exactly as it was.

A game whose game.json says installer="ps1" ships its own installer next to
its patch -- either because its patch is not a translation tree (see
patch_layout) or because it needs a bespoke uninstaller too. This script
refuses those rather than half-installing them.
"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games  # noqa: E402

BACKUP = ".zh_patch_backup"

# Last-resort fallback; see docs/fonts.md.
REPO_FONT = os.path.join(games.ROOT, "fonts", "zh.ttf")

SYSTEM_FONTS = [
    # Windows
    r"C:\Windows\Fonts\msyh.ttc", r"C:\Windows\Fonts\msyhl.ttc",
    r"C:\Windows\Fonts\simhei.ttf", r"C:\Windows\Fonts\simsun.ttc",
    r"C:\Windows\Fonts\Deng.ttf", r"C:\Windows\Fonts\Dengb.ttf",
    # macOS
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    # Linux
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJKsc-Regular.otf",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
]


def die(msg):
    sys.exit("error: " + msg)


def resolve_game(arg):
    path = os.path.abspath(arg)
    if os.path.isdir(os.path.join(path, "game")):
        return os.path.join(path, "game")
    if os.path.basename(path) == "game":
        return path
    die("not a Ren'Py game directory: %s" % arg)


def pick_font(override, asset, repo):
    """The bundled face wins over any system font, on purpose.

    game.json's font asset is the exact file the release zip ships, so a
    script install and an unzip-the-zip install put the same glyphs on
    screen. The system list is only a fallback for a checkout that is
    missing the asset.
    """
    cands = [override]
    if asset:
        cands.append(games.path_of(repo, asset.replace("/", os.sep)))
    cands.append(REPO_FONT)
    cands += SYSTEM_FONTS
    for cand in cands:
        if cand and os.path.isfile(cand):
            return cand
    return None


def back_up(game, rel):
    """Copy game/<rel> into the backup dir the first time it is touched.

    tl/<lang> is a directory (the game ships its own templates there), so this
    has to cope with both files and trees.
    """
    src = os.path.join(game, rel)
    dst = os.path.join(game, BACKUP, rel.replace("/", os.sep))
    if os.path.exists(dst):
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.isdir(src):
        shutil.copytree(src, dst,
                        ignore=shutil.ignore_patterns("*.rpyc", "*.rpymc"))
    elif os.path.exists(src):
        shutil.copy2(src, dst)


def clear_compiled(game, rel):
    """Ren'Py prefers .rpyc; a stale one silently wins over our .rpy."""
    base = os.path.splitext(os.path.join(game, rel))[0]
    for ext in (".rpyc", ".rpymc"):
        if os.path.exists(base + ext):
            os.remove(base + ext)


def install_script(game, repo, lang):
    src = games.path_of(repo, "patch", "tl", lang)
    dst = games.path_of(game, "tl", lang)
    if not os.path.isdir(src):
        die("%s is missing" % src)
    back_up(game, "tl/%s" % lang)
    if os.path.isdir(dst):
        for d, _, fs in os.walk(dst):
            for f in fs:
                if f.endswith((".rpyc", ".rpymc")):
                    os.remove(os.path.join(d, f))
        shutil.rmtree(dst)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("*.rpyc", "*.rpymc"))
    print("  game/tl/%-10s   %d files"
          % (lang, sum(len(f) for _, _, f in os.walk(dst))))
    return ["tl/%s" % lang]


def install_shim(game, repo, shim_name):
    src = games.path_of(repo, "patch", shim_name)
    if not os.path.isfile(src):
        die("%s is missing" % src)
    back_up(game, shim_name)
    clear_compiled(game, shim_name)
    shutil.copyfile(src, games.path_of(game, shim_name))
    print("  game/%s" % shim_name)
    return [shim_name]


def install_fonts(game, repo, plan, override):
    """Write every face in the manifest's font plan.

    A --font override only makes sense when the game ships a single face;
    with several, "the" font is ambiguous, so say so instead of guessing.
    """
    if override and len(plan) > 1:
        die("--font cannot be used with %s: it ships %d different faces"
            % (repo, len(plan)))
    fdir = games.path_of(game, "fonts")
    os.makedirs(fdir, exist_ok=True)
    written = []
    for asset, names in plan:
        font = pick_font(override, asset, repo)
        if not font:
            die("no CJK font found for %s. Restore it, or pass --font <path>. "
                "See docs/fonts.md." % asset)
        for name in names:
            rel = "fonts/" + name
            back_up(game, rel)
            clear_compiled(game, rel)
            shutil.copyfile(font, os.path.join(fdir, name))
            written.append(rel)
        print("  game/fonts/       %s <- %s" % (", ".join(names), font))
    return written


def main(argv):
    slug, rest = games.take_slug(argv)
    font_override = None
    if "--font" in rest:
        i = rest.index("--font")
        if i + 1 < len(rest):
            font_override = rest[i + 1]
            del rest[i:i + 2]
    elif any(a.startswith("--font=") for a in rest):
        a = [x for x in rest if x.startswith("--font=")][0]
        font_override = a.split("=", 1)[1]
        rest = [x for x in rest if not x.startswith("--font=")]
    if len(rest) != 1:
        sys.exit(__doc__)

    repo, manifest = games.manifest(slug)
    lang = manifest["language"]

    if games.installer(manifest) != "py":
        # A script-override patch is not a translation tree, so there is
        # nothing for install_script() to copy and half a patch is worse than
        # none: point at the installer that actually understands this game.
        sys.exit(
            "%s is installed with its own installer, not this one.\n"
            "  game.json: patch_layout=%s, installer=%s\n"
            "  run:  powershell -NoProfile -ExecutionPolicy Bypass -File \"%s\""
            % (manifest["title"], games.layout(manifest),
               games.installer(manifest),
               os.path.join(repo, "tools", "install.%s"
                            % games.installer(manifest))))

    game = resolve_game(rest[0])
    if not os.path.exists(games.path_of(game, "options.rpy")) and \
       not os.path.exists(games.path_of(game, "options.rpyc")):
        die("no options.rpy in %s -- is this really the game directory?" % game)

    plan = games.font_plan(manifest)
    if not plan:
        die("%s declares no font asset in game.json" % manifest["slug"])

    print("%s [%s] -> %s" % (manifest["title"], lang, game))
    touched = []
    touched += install_script(game, repo, lang)
    touched += install_shim(game, repo, manifest["shim"])
    touched += install_fonts(game, repo, plan, font_override)

    with open(games.path_of(game, BACKUP, "manifest.json"), "w",
              encoding="utf-8") as f:
        json.dump({"version": 2, "game": manifest["slug"], "lang": lang,
                   "shim": manifest["shim"], "files": sorted(touched)},
                  f, indent=2)

    print("\ndone. launch the game; %s is forced on at startup.\n"
          "to undo:  python tools/uninstall.py \"%s\" --game %s"
          % (manifest["language_name"], game, manifest["slug"]))


if __name__ == "__main__":
    main(sys.argv[1:])
