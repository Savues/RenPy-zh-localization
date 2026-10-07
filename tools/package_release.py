# -*- coding: utf-8 -*-
"""Package the files a player needs into a release zip.

    python tools/package_release.py [--game <slug>] [--version v1.0.0]

The archive is a plain folder tree, not a program: extracting it yields a
`game/` directory whose contents are meant to be copied straight over the
game's own `game/` directory. Nothing in it needs Python, an installer or a
command line.

What ships and what does not:

    README.md          player instructions (generated below)
    LICENSE            this repository's licence
    game/tl/<lang>/    the translated scripts
    game/<shim>        language/hook script

The font is deliberately *not* in here. The game hardcodes five font file
names and the translations render through them, so a CJK face has to sit at
those paths -- but every redistributable CJK face is 8 MB or more and every
convenient system one (Microsoft YaHei, SimHei, DengXian, SimSun) is
proprietary and cannot be redistributed in a public release. The README
therefore walks the player through copying a font from their own machine,
which is the same thing tools/install.py does automatically for anyone who
does have Python.

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


def collect(repo, slug, manifest, version, count):
    """-> [(arcname, source_path_or_None, bytes)] in a stable order."""
    out = [("README.md", None, render_readme(manifest, slug, version, count)
            .encode("utf-8"))]

    lic = os.path.join(games.ROOT, "LICENSE")
    if os.path.isfile(lic):
        out.append(("LICENSE", lic, None))

    patch_root = games.path_of(repo, "patch")
    for dirpath, dirnames, filenames in os.walk(patch_root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP)
        for fn in sorted(filenames):
            if fn in SKIP or fn.endswith((".rpyc", ".rpymc", ".pyc")):
                continue
            src = os.path.join(dirpath, fn)
            rel = os.path.relpath(src, patch_root).replace(os.sep, "/")
            out.append(("game/" + rel, src, None))

    return sorted(out, key=lambda r: r[0])


def render_readme(manifest, slug, version, count):
    """Fill the player README from the manifest.

    Uses literal {{token}} replacement rather than %- or .format()-style
    interpolation: the template is full of things both of those would try to
    read as markup, and a silent mangling here ships to players.
    """
    shadow = "\n".join(
        "| `%s` |" % n
        for n in [manifest.get("patch_font", "zh.ttf")] + list(
            manifest.get("font_shadow", [])))
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
        "{{patchfont}}": manifest.get("patch_font", "zh.ttf"),
        "{{shadowtable}}": shadow,
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

---

## 安装

**不需要 Python，不需要安装器，不需要联网。** 两步。

### 第一步：中文字体

游戏脚本把字体**文件名**写死了，中文必须通过这几个文件渲染。Windows 自带的
这几款都能显示中文，任选一款：

```
C:\\Windows\\Fonts\\msyh.ttc     微软雅黑
C:\\Windows\\Fonts\\simhei.ttf   黑体
C:\\Windows\\Fonts\\Deng.ttf     等线
C:\\Windows\\Fonts\\simsun.ttc   宋体
```

macOS 用 `/System/Library/Fonts/PingFang.ttc`（苹方），Linux 用
`/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc`。

把选中的那个字体文件复制到游戏的 `game/fonts/` 目录下，**复制成下面这些名字**
（内容完全一样，只是文件名不同）：

| 复制成的文件名 |
|---|
{{shadowtable}}

### 第二步：复制补丁文件

1. 把游戏**完全关闭**
2. 解压 `{{zipname}}`
3. 把解压出来的 `game` 文件夹里的**全部内容**复制到游戏的 `game` 文件夹里，
   选择**覆盖**

```
要复制的东西                        复制到哪里
game/tl/{{lang}}/        →      <游戏目录>/game/tl/{{lang}}/
game/{{shim}}             →      <游戏目录>/game/{{shim}}
```

装完直接启动游戏，{{langname}}会自动启用。

## 常见问题

**装完还是英文**
游戏目录里残留了旧的 `.rpyc` 编译文件。Ren'Py 优先加载 `.rpyc`，旧的会盖过新
脚本。删掉 `game/tl/{{lang}}/` 里所有 `.rpyc` 再启动。原版游戏不会有这个问题。

**中文显示成方块**
第一步的字体没放对。确认 `game/fonts/` 下那 5 个文件都存在，而且不是 0 字节。

**某个界面（比如章节选择、存档界面）的字不对**
那几个界面在原文里带 `{font=...}` 标记，用的是字体文件名而不是默认字体。
第一步如果只放了 `{{patchfont}}` 一个文件，这些地方就会出问题——5 个都要放。

**启动时报 `A translation for "X" already exists`**
游戏里已经打过别的汉化补丁，两份翻译冲突。先卸载那个补丁，或者在一份干净的
原版上重新复制。

**启动时报 `config.say_arguments_callback` 相关错误**
本补丁的语言脚本依赖 Ren'Py 8.x 的回调接口。原版游戏用的是 {{renpy}}，
其它版本如果报错请反馈。

---

## 关于这个压缩包

```
{{zipname}}
├── README.md              本文件
├── LICENSE                汉化补丁的许可
└── game/                  ← 把这个文件夹里的内容复制到游戏的 game/ 里
    ├── tl/{{lang}}/           翻译后的脚本
    └── {{shim}}               语言与字体补丁
```

## 版权与免责

游戏版权归 {{author}} 所有。本汉化补丁是**非官方的同人翻译作品**，与原作方无
任何关联，仅供学习交流使用。请自行确认当地法律与原作方的授权状况。

本包**不包含**任何游戏程序文件、图像、音频、原始脚本或字体文件，只包含翻译
补丁与安装说明。请勿将本补丁与游戏本体一同分发。
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
    print("  %d files, %.2f MB" % (len(entries), os.path.getsize(out) / 1048576))
    for arc, src, blob in entries[:5]:
        print("    %s" % arc)
    print("    ... (%d more)" % max(0, len(entries) - 5))
    print("  path:   %s" % os.path.relpath(out, games.ROOT))
    print("  sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())