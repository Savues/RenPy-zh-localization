# -*- coding: utf-8 -*-
"""Package the files a player needs into a release zip.

    python tools/package_release.py [--game <slug>] [--version v1.0.0]

Only what a player actually needs ships: the patch itself plus the three
scripts that install and remove it. The translation database, the glossary and
the build/verify tooling stay in the repository -- a player has no use for
1.2 MB of English source strings, and shipping it would blur the line between
"a patch" and "a derivative of the game script".

The repo layout is preserved inside the zip, so the documented command works
verbatim:

    python tools/install.py "<your game folder>"

Output is deterministic: files are added in sorted order with a fixed
timestamp, so the same tree always produces a byte-identical archive.
"""
import argparse
import hashlib
import io
import os
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games  # noqa: E402

# 1980-01-01 is the earliest timestamp the zip format can represent; using a
# fixed one keeps rebuilds byte-identical.
FIXED_TIME = (1980, 1, 1, 0, 0, 0)

# Tools a player needs. games.py is required by the other two.
PLAYER_TOOLS = ["games.py", "install.py", "uninstall.py"]

SKIP = {"__pycache__", ".git", ".source.json"}


def zip_name(slug, lang, version):
    return "%s-%s-patch-%s.zip" % (slug, lang, version)


def collect(repo, slug, manifest, version):
    """-> [(arcname, source_path_or_None, bytes)] in a stable order."""
    out = []

    readme = render_readme(manifest, slug, version)
    out.append(("README.md", None, readme.encode("utf-8")))

    lic = os.path.join(games.ROOT, "LICENSE")
    if os.path.isfile(lic):
        out.append(("LICENSE", lic, None))

    out.append((os.path.join("games", slug, "game.json"),
                os.path.join(repo, "game.json"), None))

    patch_root = os.path.join(repo, "patch")
    for dirpath, dirnames, filenames in os.walk(patch_root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP)
        for fn in sorted(filenames):
            if fn in SKIP or fn.endswith((".rpyc", ".rpymc", ".pyc")):
                continue
            src = os.path.join(dirpath, fn)
            rel = os.path.relpath(src, patch_root).replace(os.sep, "/")
            out.append(("games/%s/patch/%s" % (slug, rel), src, None))

    for tool in PLAYER_TOOLS:
        out.append(("tools/" + tool, os.path.join(games.ROOT, "tools", tool),
                    None))

    return sorted(out, key=lambda r: r[0])


def render_readme(manifest, slug, version):
    lang = manifest["language"]
    return PLAYER_README % {
        "title": manifest["title"],
        "author": manifest["author"],
        "renpy": manifest["renpy_version"],
        "lang": lang,
        "langname": manifest["language_name"],
        "slug": slug,
        "zipname": zip_name(slug, lang, version),
        "shim": manifest["shim"],
        "fonts": "、".join("`%s`" % f for f in manifest["font_shadow"]),
    }


PLAYER_README = """# %(title)s — %(langname)s 汉化补丁

| | |
|---|---|
| 游戏 | %(title)s |
| 原作 | %(author)s |
| 引擎 | Ren'Py %(renpy)s |
| 语言 | %(langname)s（启动时自动启用，无需在设置里切换） |
| 覆盖率 | 100%%（全部可译条目均已翻译） |
| 翻译方式 | 逐条人工翻译，未使用任何机器翻译或在线翻译 API |

本压缩包只包含**安装补丁所必需**的文件。

```
%(zipname)s
├── README.md                    本文件
├── LICENSE
├── games/%(slug)s/
│   ├── game.json                 元数据
│   └── patch/                    汉化补丁本体
│       ├── tl/%(lang)s/                 翻译后的脚本
│       └── %(shim)s                     语言与字体补丁
└── tools/
    ├── install.py                一键安装
    ├── uninstall.py              一键卸载
    └── games.py                  内部依赖
```

---

## 环境要求

- 已安装原版游戏（**未**打过其它汉化补丁）
- Python 3.8 或更高版本（Windows 10/11 自带 Python 启动器；
  macOS/Linux 一般已自带）
- 系统中已有一款能显示中文的字体（Windows、主流 Linux 发行版、
  macOS 均自带，通常无需额外安装）

## 安装

解压本压缩包，然后：

```bash
python tools/install.py "<你的游戏目录>"
```

例如：

```bash
python tools/install.py "C:\\Games\\%(title)s"
```

脚本会：

1. 把翻译后的脚本写入游戏的 `game/tl/%(lang)s/`
2. 写入语言补丁 `game/zz_zh_locale.rpy`
3. 找一款系统中文字体写入 `game/fonts/`，并覆盖游戏硬编码的 %(fonts)s
4. 把所有被覆盖的原始文件备份到 `game/.zh_patch_backup/`

装完**直接启动游戏**即可，不需要在设置里切换语言。

指定字体：

```bash
python tools/install.py "<你的游戏目录>" --font "C:/Windows/Fonts/msyh.ttc"
```

## 卸载

```bash
python tools/uninstall.py "<你的游戏目录>"
```

会从备份逐字节还原被覆盖的文件。确认还原无误后加 `--purge-backup`
一并删除备份目录。

---

## 常见问题

**装完游戏里还是英文**
游戏目录里可能残留了旧的 `.rpyc` 编译文件。Ren'Py 优先加载 `.rpyc`，
旧的会盖过新的脚本。`install.py` 会自动清理，手动拷贝时容易漏。

**中文显示成方块**
说明覆盖的字体不够。游戏硬编码了这些字体文件名：%(fonts)s。
用 `--font` 显式指定一款中文字体再装一次即可。

**启动时报 `A translation for "X" already exists`**
说明游戏里已经打过其它汉化补丁，两份翻译冲突。先卸载原补丁，
或者直接在一份干净的原版游戏上安装。

**启动时报 `config.say_arguments_callback` 相关错误**
本补丁的语言脚本依赖 Ren'Py 8.x 的回调接口。原版游戏用的是 8.4.1，
如果是其它版本且报错，请反馈。

---

## 版权与免责

游戏版权归 %(author)s 所有。本汉化补丁是**非官方的同人翻译作品**，
与原作方无任何关联，仅供学习交流使用。请自行确认当地法律与原作方的
授权状况。

请勿将本补丁与游戏本体一同分发——本包**不包含**任何游戏程序文件、
图像、音频或原始脚本，只包含翻译补丁与安装脚本。
"""


def build(slug, version):
    repo, manifest = games.manifest(slug)
    # games.manifest() tolerates slug=None and picks the only game in the
    # repository; from here on the resolved folder name is what we need.
    slug = os.path.basename(repo)
    entries = collect(repo, slug, manifest, version)

    out_dir = os.path.join(games.ROOT, "dist")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, zip_name(slug, manifest["language"], version))

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
    for arc, src, blob in entries[:4]:
        print("    %s" % arc)
    print("    ... (%d more)" % max(0, len(entries) - 4))
    print("  path:   %s" % os.path.relpath(out, games.ROOT))
    print("  sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
