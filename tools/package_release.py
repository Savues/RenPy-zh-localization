# -*- coding: utf-8 -*-
"""Package the files a player needs into a release zip.

    python tools/package_release.py [--game <slug>] [--version v1.0.0]

The archive is a plain folder tree, not a program: extracting it yields a
`game/` directory whose contents are meant to be copied straight over the
game's own `game/` directory. Nothing in it needs Python, an installer, a
command line, a network connection -- or a font the player has to go and find.

What ships:

    README.md          player instructions (generated below)
    LICENSE            this repository's licence
    FONT-LICENSE.txt   attribution for the bundled CJK face
    game/tl/<lang>/    the translated scripts
    game/<shim>        language/hook script
    game/fonts/*       the bundled face, under every filename the game asks
                       for (patch_font plus font_shadow) -- the game hardcodes
                       those names, and a Chinese face has to sit at those
                       paths or the text renders as tofu

The 1.2 MB English source database, the glossary and the build/verify tooling
stay in the repository -- a player has no use for the original strings, and
shipping them would blur the line between "a patch" and "a derivative of the
game script".

Output is deterministic: files are added in sorted order with a fixed
timestamp, so the same tree always produces a byte-identical archive.
"""
import argparse
import hashlib
import io
import json
import os
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games  # noqa: E402

# 1980-01-01 is the earliest timestamp the zip format can represent; using a
# fixed one keeps rebuilds byte-identical.
FIXED_TIME = (1980, 1, 1, 0, 0, 0)

SKIP = {"__pycache__", ".git", ".source.json"}


def zip_name(slug, lang, version):
    return "%s-%s-patch-%s.zip" % (slug, lang, version)


def font_names(manifest):
    """Every filename the game will look the bundled face up under."""
    names = [manifest.get("patch_font", "zh.ttf")]
    for n in manifest.get("font_shadow", []):
        if n not in names:
            names.append(n)
    return names


def collect(repo, slug, manifest, version, count):
    """-> [(arcname, source_path_or_None, bytes)] in a stable order."""
    out = [("README.md", None, render_readme(manifest, slug, version, count)
            .encode("utf-8"))]

    lic = os.path.join(games.ROOT, "LICENSE")
    if os.path.isfile(lic):
        out.append(("LICENSE", lic, None))

    fl = manifest.get("font_license")
    if fl:
        out.append(("FONT-LICENSE.txt",
                    games.path_of(repo, fl.replace("/", os.sep)), None))

    patch_root = games.path_of(repo, "patch")
    for dirpath, dirnames, filenames in os.walk(patch_root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP)
        for fn in sorted(filenames):
            if fn in SKIP or fn.endswith((".rpyc", ".rpymc", ".pyc")):
                continue
            src = os.path.join(dirpath, fn)
            rel = os.path.relpath(src, patch_root).replace(os.sep, "/")
            out.append(("game/" + rel, src, None))

    fa = manifest.get("font_asset")
    if fa:
        src = games.path_of(repo, fa.replace("/", os.sep))
        for name in font_names(manifest):
            out.append(("game/fonts/" + name, src, None))

    return sorted(out, key=lambda r: r[0])


def render_readme(manifest, slug, version, count):
    """Fill the player README from the manifest.

    Uses literal {{token}} replacement rather than %- or .format()-style
    interpolation: the template is full of things both of those would try to
    read as markup, and a silent mangling here ships to players.
    """
    fields = {
        "{{title}}": manifest["title"],
        "{{author}}": manifest["author"],
        "{{renpy}}": manifest["renpy_version"],
        "{{lang}}": manifest["language"],
        "{{langname}}": manifest["language_name"],
        "{{slug}}": slug,
        "{{version}}": version,
        "{{zipname}}": zip_name(slug, manifest["language"], version),
        "{{shim}}": manifest["shim"],
        "{{fontcredit}}": manifest.get("font_credit", ""),
        "{{count}}": "{:,}".format(count),
    }
    text = PLAYER_README
    for token, value in fields.items():
        text = text.replace(token, value)
    if "{{" in text:
        raise SystemExit("unfilled token left in the player README")
    return text


PLAYER_README = """# {{title}} — {{langname}}汉化补丁 {{version}}

| | |
|---|---|
| 游戏 | {{title}} |
| 原作 | {{author}} |
| 引擎 | Ren'Py {{renpy}} |
| 语言 | {{langname}}（启动时自动启用，不需要在设置里切换） |
| 译文条目 | {{count}} 条，覆盖率 100%，没有未译条目 |
| 翻译方式 | 逐条人工翻译，没有使用任何机器翻译或在线翻译 API |
| 中文字体 | {{fontcredit}}（已打包） |

---

## 安装

**不需要 Python，不需要安装器，不需要联网，也不用自己找字体。** 三步：

1. 把游戏**完全关闭**
2. 解压 `{{zipname}}`
3. 把解压出来的 `game` 文件夹里的**全部内容**复制到游戏的 `game` 文件夹里，
   选择**覆盖**

```
要复制的东西                        复制到哪里
game/tl/{{lang}}/        →      <游戏目录>/game/tl/{{lang}}/
game/{{shim}}             →      <游戏目录>/game/{{shim}}
game/fonts/*              →      <游戏目录>/game/fonts/
```

装完直接启动游戏，{{langname}}会自动启用。

中文字体已经在包里了。游戏把字体**文件名**写死了，所以同一份字体会以它要的每个
文件名各存一份放进 `game/fonts/`，游戏自带的同名西文字体会被替换掉。

---

## 常见问题

**装完还是英文**
游戏目录里残留了旧的 `.rpyc` 编译文件。Ren'Py 优先加载 `.rpyc`，旧的会盖过新脚本。
删掉 `game/tl/{{lang}}/` 里所有 `.rpyc` 再启动。原版游戏不会有这个问题。

**中文显示成方块**
`game/fonts/` 没复制全。确认那 5 个字体文件都在、大小一致（约 8 MB）。

**启动时报 `A translation for "X" already exists`**
游戏里已经打过别的汉化补丁，两份翻译冲突。先卸载那个补丁，或者在一份干净的原版
上重新复制。

**启动时报 `Could not find font`**
`game/fonts/` 被删过或没复制全。把包里的 `game/fonts/` 整个再复制一次。

**启动时报 `config.say_arguments_callback` 相关错误**
本补丁的语言脚本依赖 Ren'Py 8.x 的回调接口。原版游戏用的是 {{renpy}}，其它版本
如果报错请反馈。

---

## 关于这个压缩包

```
{{zipname}}
├── README.md              本文件
├── LICENSE                汉化补丁的许可
├── FONT-LICENSE.txt       中文字体的版权声明
└── game/                  ← 把这个文件夹里的内容复制到游戏的 game/ 里
    ├── tl/{{lang}}/           翻译后的脚本
    ├── {{shim}}               语言与字体补丁
    └── fonts/                 中文字体（同一份字体的多个副本）
```

## 版权与免责

游戏版权归 {{author}} 所有。本汉化补丁是**非官方的同人翻译作品**，与原作方无任何
关联，仅供学习交流使用。请自行确认当地法律与原作方的授权状况。

本包**不包含**任何游戏程序文件、图像、音频或原始脚本，只包含翻译补丁与中文字体。
请勿将本补丁与游戏本体一同分发。

中文字体的版权与授权见 `FONT-LICENSE.txt`。
"""


def build(slug, version):
    repo, manifest = games.manifest(slug)
    # games.manifest() tolerates slug=None and picks the only game in the
    # repository; from here on the resolved folder name is what we need.
    slug = os.path.basename(repo)
    lang = manifest["language"]

    db = games.path_of(repo, "data", "tl_trans.json")
    count = len(json.load(open(db, encoding="utf-8"))) if os.path.isfile(db) else 0

    entries = collect(repo, slug, manifest, version, count)

    out_dir = os.path.join(games.ROOT, "dist")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, zip_name(slug, lang, version))

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for arc, src, blob in entries:
            data = blob if blob is not None else io.open(src, "rb").read()
            info = zipfile.ZipInfo(arc, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)

    return out, entries, manifest


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--game", default=None,
                    help="games/ subfolder name; omit when there is only one")
    ap.add_argument("--version", default="v1.0.0",
                    help="version label embedded in the zip file name")
    args = ap.parse_args()

    out, entries, manifest = build(args.game, args.version)
    with io.open(out, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()

    print("packaged %s [%s] -> %s"
          % (manifest["title"], manifest["language_name"],
             os.path.basename(out)))
    print("  %d entries, %.2f MB" % (len(entries), os.path.getsize(out) / 1048576))
    for arc, src, blob in entries[:4]:
        print("    %s" % arc)
    print("    ... (%d more)" % max(0, len(entries) - 4))
    print("  path:   %s" % os.path.relpath(out, games.ROOT))
    print("  sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
