# -*- coding: utf-8 -*-
"""Install a game patch from this repository into a Ren'Py game directory.

    python tools/install.py "<path-to-the-game>" [--game <slug>]
    python tools/install.py "<path-to-the-game>" --font "C:/Windows/Fonts/msyh.ttc"

What it does
    1. game/tl/<lang>     <- games/<slug>/patch/tl/<lang>
    2. game/<shim>         <- games/<slug>/patch/<shim>
    3. game/fonts/*        <- a CJK-capable face, shadowing the font filenames
                              the game hardcodes (see game.json)

Anything it overwrites is copied to game/.zh_patch_backup/ first; run
tools/uninstall.py to put the game back exactly as it was.
"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games  # noqa: E402

BACKUP = ".zh_patch_backup"

# Optional override shipped with the repo; see docs/fonts.md.
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


def pick_font(override=None):
    for cand in [override, REPO_FONT] + SYSTEM_FONTS:
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


def install_shim(game, repo, shim_name):
    src = games.path_of(repo, "patch", shim_name)
    if not os.path.isfile(src):
        die("%s is missing" % src)
    back_up(game, shim_name)
    clear_compiled(game, shim_name)
    shutil.copyfile(src, games.path_of(game, shim_name))
    print("  game/%s" % shim_name)


def install_fonts(game, font, names):
    fdir = games.path_of(game, "fonts")
    os.makedirs(fdir, exist_ok=True)
    for name in names:
        rel = "fonts/" + name
        back_up(game, rel)
        clear_compiled(game, rel)
        shutil.copyfile(font, os.path.join(fdir, name))
    print("  game/fonts/       %d files <- %s" % (len(names), font))


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
    game = resolve_game(rest[0])
    if not os.path.exists(games.path_of(game, "options.rpy")) and \
       not os.path.exists(games.path_of(game, "options.rpyc")):
        die("no options.rpy in %s -- is this really the game directory?" % game)

    names = [manifest.get("patch_font", "zh.ttf")] + manifest["font_shadow"]
    font = pick_font(font_override)
    if not font:
        die("no CJK font found. Put one at fonts/zh.ttf, or pass --font <path>. "
            "See docs/fonts.md.")

    print("%s [%s] -> %s" % (manifest["title"], lang, game))
    install_script(game, repo, lang)
    install_shim(game, repo, manifest["shim"])
    install_fonts(game, font, names)

    with open(games.path_of(game, BACKUP, "manifest.json"), "w",
              encoding="utf-8") as f:
        json.dump({"version": 1, "game": manifest["slug"], "lang": lang,
                   "shim": manifest["shim"], "font": font, "fonts": names},
                  f, indent=2)

    print("\ndone. launch the game; %s is forced on at startup.\n"
          "to undo:  python tools/uninstall.py \"%s\" --game %s"
          % (manifest["language_name"], game, manifest["slug"]))


if __name__ == "__main__":
    main(sys.argv[1:])
