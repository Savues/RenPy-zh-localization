# -*- coding: utf-8 -*-
"""Install the Eden Chapter 5 Chinese patch into a game directory.

    python tools/install.py "<path-to-Eden-Chapter5-pc>"
    python tools/install.py "<path-to-game>" --font "C:/Windows/Fonts/msyh.ttc"

What it does
    1. game/tl/schinese      <- patch/tl/schinese   (translated script)
    2. game/zz_zh_locale.rpy  <- patch/zz_zh_locale.rpy
    3. game/fonts/*           <- a CJK-capable face, shadowing the four font
                                 filenames the game hardcodes

Anything it overwrites is copied to game/.zh_patch_backup/ first; run
tools/uninstall.py to put the game back exactly as it was.
"""
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATCH = os.path.join(ROOT, "patch")
BACKUP = ".zh_patch_backup"
SHIM = "zz_zh_locale.rpy"

# The game hardcodes these four filenames. Shadowing them on disk is what makes
# every text-facing font -- dialogue, {font=...} tags, screen styles -- render
# Chinese instead of falling back to tofu boxes.
FONT_NAMES = ["comfortaa.ttf", "CinzelDecorative.ttf",
              "MichromaRegular.ttf", "PacificoRegular.ttf"]

# Optional override shipped with the patch; see fonts/README.md.
BUNDLED_FONT = os.path.join(ROOT, "fonts", "zh.ttf")

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
    for cand in [override, BUNDLED_FONT] + SYSTEM_FONTS:
        if cand and os.path.isfile(cand):
            return cand
    return None


def back_up(game, rel):
    """Copy game/<rel> into the backup dir the first time it is touched.

    tl/schinese is a directory (the game ships its own templates there), so
    this has to cope with both files and trees.
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
    base = os.path.join(game, rel)
    for ext in (".rpyc", ".rpymc"):
        stale = os.path.splitext(base)[0] + ext
        if os.path.exists(stale):
            os.remove(stale)


def install_script(game):
    src = os.path.join(PATCH, "tl", "schinese")
    dst = os.path.join(game, "tl", "schinese")
    if not os.path.isdir(src):
        die("patch/tl/schinese is missing")
    back_up(game, "tl/schinese")
    if os.path.isdir(dst):
        for d, _, fs in os.walk(dst):
            for f in fs:
                if f.endswith((".rpyc", ".rpymc")):
                    os.remove(os.path.join(d, f))
        shutil.rmtree(dst)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("*.rpyc", "*.rpymc"))
    n = sum(len(f) for _, _, f in os.walk(dst))
    print("  game/tl/schinese      %d files" % n)


def install_shim(game):
    src = os.path.join(PATCH, SHIM)
    dst = os.path.join(game, SHIM)
    if not os.path.isfile(src):
        die("patch/%s is missing" % SHIM)
    back_up(game, SHIM)
    clear_compiled(game, SHIM)
    shutil.copyfile(src, dst)
    print("  game/%s" % SHIM)


def install_fonts(game, font):
    fdir = os.path.join(game, "fonts")
    os.makedirs(fdir, exist_ok=True)
    for name in ["zh.ttf"] + FONT_NAMES:
        rel = "fonts/" + name
        back_up(game, rel)
        clear_compiled(game, rel)
        shutil.copyfile(font, os.path.join(fdir, name))
    print("  game/fonts/           %d files <- %s" % (len(FONT_NAMES) + 1, font))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    font_override = None
    for a in sys.argv[1:]:
        if a.startswith("--font"):
            font_override = a.split("=", 1)[1] if "=" in a else \
                sys.argv[sys.argv.index(a) + 1]
    if len(args) != 1:
        sys.exit(__doc__)

    game = resolve_game(args[0])
    if not os.path.exists(os.path.join(game, "options.rpy")) and \
       not os.path.exists(os.path.join(game, "options.rpyc")):
        die("no options.rpy in %s -- is this really the game directory?" % game)

    font = pick_font(font_override)
    if not font:
        die("no CJK font found. Put one at fonts/zh.ttf, or pass --font <path>. "
            "See fonts/README.md.")

    print("installing into %s" % game)
    install_script(game)
    install_shim(game)
    install_fonts(game, font)

    with open(os.path.join(game, BACKUP, "manifest.json"), "w",
              encoding="utf-8") as f:
        json.dump({"version": 1, "font": font,
                   "fonts": FONT_NAMES + ["zh.ttf"]}, f, indent=2)

    print("\ndone. launch the game; Chinese is forced on at startup.\n"
          "to undo:  python tools/uninstall.py \"%s\"" % game)


if __name__ == "__main__":
    main()
