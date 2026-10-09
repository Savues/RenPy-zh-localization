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
    game/<...>         the patch itself, laid out exactly as it has to sit in
                       the game's own game/ directory
    game/fonts/*       the bundled faces, each under every filename the game
                       looks it up under -- a Chinese face has to sit at those
                       paths or the text renders as tofu

The patch layout comes from game.json's patch_layout, because the two shapes
are not interchangeable. "tl-blocks" puts generated translate blocks under
game/tl/<lang>/. "script-override" replaces the game's own scripts instead, so
patch/game/ mirrors the game's game/ directory and every file has to land one
directory higher than "game/ + patch-relative path" would put it. A
script-override patch packaged one directory too deep is silently ignored by
Ren'Py: no error anywhere, just an untranslated game.

The 1.2 MB English source database, the glossary and the build/verify tooling
stay in the repository -- a player has no use for the original strings, and
shipping them would blur the line between "a patch" and "a derivative of the
game script".

The version in the file name is the game's own `patch_version` from game.json,
-- never the release tag. A release is a batch that collects every game, so
its tag moves whenever any one of them changes; putting that number into the
packages would rename and rebuild all of them each batch, including the ones
whose bytes did not move. Nothing in here may read the batch: a package whose
contents depend on it churns even when its own patch is untouched.

A game may also declare `extras`: optional packages that ship as their own
zip beside the patch, so the player takes them or leaves them. Nothing in the
patch needs them -- a third-party mod's translation is exactly the sort of
thing that has to be a separate download the player opts into. Extras are
built by the same script and attached to the same release; see build_extras().

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


def zip_name(slug, lang, version):
    return "%s-%s-patch-%s.zip" % (slug, lang, version)


def extra_zip_name(slug, lang, extra, version):
    return "%s-%s-%s-%s.zip" % (slug, lang, extra["id"], version)



# How the bundled face reaches the screen. A game that hardcodes font *files*
# has the patch overwrite them ("shadow"); a game reached through
# renpy.config.font_name_map only needs the one file ("fallback"). game.json
# picks with "font_strategy"; absent means "shadow", which is what Eden wants.
FONT_STRATEGY = {
    "shadow": {
        "note": ("中文字体已经在包里了。游戏把字体**文件名**写死了，"
                 "所以同一份字体会以它要的每个文件名各存一份放进 "
                 "`game/fonts/`\n（共 {n} 个文件），游戏自带的同名西文字体会被替换掉。"),
        "tree": "中文字体（同一份字体的 {n} 个副本）",
    },
    "game-bundled": {
        "note": ("**这个补丁不附带任何字体，也不需要。** 游戏原版就带着能用的简体中文字体，\n"
                 "它自己的字体映射已经指向那份字库了。补丁不重新分发字体文件，\n"
                 "省下的体积正好用来装汉化脚本。"),
        "tree": "（没有 fonts/ —— 字体由游戏自带）",
        "trouble": ("原版游戏的中文本来就是好的，所以出现方块说明**装坏了**，不是缺字体。\n"
                    "先确认 `game/` 下的脚本被完整覆盖（同名逐个覆盖、别漏目录），\n"
                    "再确认 `game/cache/` 里的 `bytecode-*.rpyb` 和 `screens.rpyb` 已删。\n"
                    "仍然方块的话，卸载后在一份干净的原版上重装一次。"),
    },
    "fallback": {
        "note": ("中文字体已经在包里了，共 {n} 个字体文件。本补丁通过\n"
                 "`renpy.config.font_name_map` 把它们注册为**回退**字体：游戏原有的"
                 "西文字体照常绘制英文，\n只有它画不出的汉字和中文标点才交给中文字体。"
                 "\n游戏自带的字体文件**不会**被替换。"),
        "tree": "中文字体（回退用，游戏原字体保留）",
    },
}


def font_bits(manifest):
    """-> (note, tree, trouble) rendered from the game's actual font plan.

    The counts and names come from game.json rather than being written into
    the prose, so adding a second face to a game does not leave the player
    README claiming there is only one.
    """
    plan = games.font_plan(manifest)
    names = [n for _, ns in plan for n in ns]
    primary = names[0] if names else ""
    style = FONT_STRATEGY[manifest.get("font_strategy", "shadow")]
    # A strategy that ships no font has to answer the "boxes instead of Han"
    # question differently: telling such a player to check game/fonts/ would
    # send them looking for a directory that was never in the zip.
    trouble = style.get("trouble")
    if trouble is None:
        trouble = (
            "`game/fonts/` 没复制全。确认那 %d 个字体文件都在、大小一致（约 8 MB）。"
            % len(names) if len(names) > 1 else
            "`game/fonts/` 没复制全。确认 `%s` 在（约 7.7 MB）。"
            "若仍显示方块，请检查 `%s` 是否放在游戏的 `game/` 目录下。"
            % (primary, manifest["shim"]))
    return (style["note"].format(n=len(names)),
            style["tree"].format(n=len(names)),
            trouble)


def fontrow_bits(manifest):
    """-> the two README claims that only some games can make."""
    shipped = games.font_plan(manifest)
    if shipped:
        return {
            "{{fontrow}}": "%s（已打包）" % manifest.get("font_credit", ""),
            "{{fontfaq}}": (
                "**启动时报 `Could not find font`**\n"
                "`game/fonts/` 被删过或没复制全。把包里的 `game/fonts/` 整个再复制一次。"),
            "{{fontclose}}": "中文字体的版权与授权见 `FONT-LICENSE.txt`。",
            "{{packcontains}}": (
                "本包**不包含**任何游戏程序文件、图像、音频或原始脚本，"
                "只包含翻译补丁与中文字体。"),
            "{{fontlicenserow}}": ("├── FONT-LICENSE.txt       "
                                   "中文字体的版权声明\n"
                                   if manifest.get("font_license") else ""),
        }
    return {
        "{{fontrow}}": "游戏自带，补丁不附带任何字体文件",
        "{{fontfaq}}": "",
        "{{fontclose}}": "",
        "{{packcontains}}": (
            "本包**不包含**任何游戏程序文件、图像、音频、原始脚本或字体，"
            "只包含汉化脚本。"),
        "{{fontlicenserow}}": "",
    }


def howtranslated_bits(manifest):
    """-> {{howtranslated}}, which is not the same sentence for every game.

    Most of the collection is translated from the English. Some entries are
    revisions of a translation the developer already ships, and claiming those
    were written from the English would be a provenance claim the repository
    does not stand behind.
    """
    base = manifest.get("base_translation")
    if base:
        return ("**%s** —— 不是从英文重新翻译，改动是在发行方那一版上做的。"
                % base)
    return "逐条人工翻译，没有使用任何机器翻译或在线翻译 API"


def installer_bits(manifest, fields):
    """-> how the player actually installs, which is not always "copy".

    A ps1 game needs its own installer in the zip and a PowerShell command
    instead of a copy table; sending such a player through the generic three
    steps would leave them with a patch half-installed and no clue why.

    fields is passed in because these fragments quote {{zipname}} and
    {{copylist}}: render_readme substitutes in insertion order, so a nested
    token spelled literally here would already have been consumed and would
    ship to the player as the text "{{copylist}}". Embedding the rendered
    values instead keeps the one-pass substitution correct.
    """
    zipname = fields["{{zipname}}"]
    copylist = fields.get("{{copylist}}", "")
    if manifest.get("installer") == "ps1":
        return {
            "{{installintro}}": (
                "**需要 PowerShell（Windows 自带），不需要自己装 Python，也不需要联网。**\n"
                "解压后在解压出来的目录里跑安装器，把游戏目录作为参数传进去："),
            "{{installsteps}}": (
                "1. 把游戏**完全关闭**\n"
                "2. 解压 `%s`，在解压出来的目录里打开 PowerShell\n"
                "3. 跑这一条：\n"
                "\n"
                "```\n"
                "powershell -NoProfile -ExecutionPolicy Bypass "
                "-File tools\\install.ps1 \"<游戏目录>\"\n"
                "```\n"
                "\n"
                "安装器会先做一次**什么都不写**的试运行，再把要改动的文件完整备份到\n"
                "`<游戏目录>/game/.zh_patch_backup/`，最后才落盘。\n"
                "\n"
                "删掉这个补丁就跑卸载器，它把备份原样盖回去：\n"
                "\n"
                "```\n"
                "powershell -NoProfile -ExecutionPolicy Bypass "
                "-File tools\\uninstall.ps1 \"<游戏目录>\"\n"
                "```" % zipname),
        }
    return {
        "{{installintro}}": (
            "**不需要 Python，不需要安装器，不需要联网，也不用自己找字体。** 三步："),
        "{{installsteps}}": (
            "1. 把游戏**完全关闭**\n"
            "2. 解压 `%s`\n"
            "3. 把解压出来的 `game` 文件夹里的**全部内容**复制到游戏的 `game` 文件夹里，\n"
            "   选择**覆盖**\n"
            "\n"
            "```\n"
            "%s\n"
            "```" % (zipname, copylist)),
    }


def _tree_row(glyph, name, desc, col=36):
    return "%s%s%s%s" % (glyph, name, " " * max(1, col - len(name)), desc)

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

    # games.patch_entries() already returns paths relative to the game's own
    # game/ directory, so the only thing left to do is prefix "game/".
    for src, rel in games.patch_entries(repo, manifest):
        out.append(("game/" + rel, src, None))

    for asset, names in games.font_plan(manifest):
        src = games.path_of(repo, asset.replace("/", os.sep))
        if not os.path.isfile(src):
            raise SystemExit("%s: font asset %s is missing" % (slug, asset))
        for name in names:
            out.append(("game/fonts/" + name, src, None))

    out.extend(installer_entries(repo, manifest))

    return sorted(out, key=lambda r: r[0])


def installer_of(manifest):
    """How this game is installed: a script the player runs, or a plain copy."""
    return manifest.get("installer") or "py"


def installer_entries(repo, manifest):
    """-> [(arcname, source, None)] for the files a ps1 installer needs.

    Shipping the scripts is not optional for an installer game: the player
    README tells them to run tools/install.ps1, so a zip without tools/ is a
    README pointing at nothing. The repo-side checkers named in extra_checks
    are the one thing left out -- they need node and a checkout, and a player
    has neither.
    """
    if installer_of(manifest) != "ps1":
        return []
    skip = set()
    for _cmd, script in (manifest.get("extra_checks") or ()):
        skip.add(os.path.basename(script))
    out = []
    tdir = os.path.join(repo, "tools")
    if not os.path.isdir(tdir):
        raise SystemExit("%s: installer is ps1 but tools/ is missing"
                         % os.path.basename(repo))
    for name in sorted(os.listdir(tdir)):
        if name in skip:
            continue
        src = os.path.join(tdir, name)
        if os.path.isfile(src):
            out.append(("tools/" + name, src, None))
    return out


def layout_bits(manifest):
    """-> the player-README fragments that differ between the patch layouts.

    Keys come back as {{token}} strings so they can be merged straight into
    render_readme's substitution table. Getting these wrong is not cosmetic:
    the copy table *is* the install instruction, and it names real paths.
    """
    lang = manifest["language"]
    shim = manifest["shim"]
    has_font = bool(games.font_plan(manifest))

    # The tree is assembled as a list and only then given its branch
    # characters, so dropping the fonts row (a game-bundled game has none) or
    # adding the tools row (a ps1 game has one) leaves the last row last.
    def tree(rows):
        return "\n".join(
            _tree_row("    %s " % ("\u2514\u2500\u2500" if n == len(rows) - 1
                                   else "\u251c\u2500\u2500"),
                      name, desc)
            for n, (name, desc) in enumerate(rows))

    tool_rows = ([("tools/", "安装器与卸载器（需要 PowerShell）")]
                 if installer_of(manifest) == "ps1" else [])
    font_rows = [("fonts/", "{{fonttree}}")] if has_font else []

    def toolrow():
        return ("\u251c\u2500\u2500 tools/                 安装器与卸载器\n"
                if tool_rows else "")

    def gamehint():
        return ("\u2190 安装器会把这里的内容装进游戏的 game/ 里" if tool_rows
                else "\u2190 把这个文件夹里的内容复制到游戏的 game/ 里")

    if games.layout(manifest) == "script-override":
        return {
            "{{countlabel}}": "个玩家可见字面量",
            "{{toolrow}}": toolrow(),
            "{{gamehint}}": gamehint(),
            # tools/ is a sibling of game/, not one of its children, so it
            # comes from {{toolrow}} above and stays out of this list.
            "{{packtree}}": tree(
                [("scripts/、gui.rpy 等", "中文脚本，覆盖游戏自带的同名文件"),
                   (shim, "语言与字体补丁")]
                + font_rows),
            "{{conflictfaq}}": conflict_faq(manifest),
            "{{copylist}}": (
                "要复制的东西                        复制到哪里\n"
                "game/ 里的全部内容                  <游戏目录>/game/"
                "   （逐个覆盖同名文件）"
                + ("\n"
                   "game/fonts/*                        <游戏目录>/game/fonts/"
                   if has_font else "")),
            "{{stalebytecode}}": ("删掉 `game/` 下与包内脚本同名的所有 `.rpyc` 再启动。"
                                  "原版游戏不会有这个问题。"),
        }

    return {
        "{{countlabel}}": "条",
        "{{toolrow}}": toolrow(),
        "{{gamehint}}": gamehint(),
        "{{packtree}}": tree(
            [("tl/%s/" % lang, "translate 翻译块"),
               (shim, "语言与字体补丁")]
            + font_rows),
        "{{conflictfaq}}": (
            "**启动时报 `A translation for \"X\" already exists`**\n"
            "游戏里已经打过别的汉化补丁，两份翻译冲突。先卸载那个补丁，或者在一份干净的"
            "原版\n上重新复制。"),
        "{{copylist}}": (
            "要复制的东西                        复制到哪里\n"
            "game/tl/%s/%s<游戏目录>/game/tl/%s/\n"
            "game/%s%s<游戏目录>/game/%s"
            % (lang, " " * 21, lang, shim, " " * max(1, 26 - len(shim)), shim)
        ) + (
            "\ngame/fonts/*%s<游戏目录>/game/fonts/" % (" " * 24)
            if has_font else ""),
        "{{stalebytecode}}": ("删掉 `game/tl/%s/` 里所有 `.rpyc` 再启动。"
                              "原版游戏不会有这个问题。" % lang),
    }


def conflict_faq(manifest):
    """-> the failure a script-override player is most likely to actually hit.

    A game whose translation also lives inside an archive has a failure mode
    that no amount of copying fixes, and it is the one thing worth warning
    about up front: hand-copying the files leaves both copies registered.
    """
    if manifest.get("archive_prefix_removed"):
        return (
            "**启动时报 `A translation for \"X\" already exists`**\n"
            "这个游戏的简体中文**打包在 `game/archive.rpa` 里**，而不是散在 `game/tl/`。\n"
            "Ren'Py 会同时收集磁盘上的文件和归档里的条目，两份都收，所以手动复制\n"
            "翻译文件只会让每一对 `old`/`new` 都被注册两遍，启动时直接抛这个异常——\n"
            "游戏连主菜单都进不去。**必须跑 `tools/install.ps1`**：它先从归档索引里\n"
            "摘掉自带的那一份，再放本补丁的文件。散落的 `foo.rpy` 也不会遮住归档里的\n"
            "同名文件，两个都会被读。")
    return (
        "**启动时报 `Parsing the script failed` 或 `The label X is defined twice`**\n"
        "游戏里已经打过另一份汉化补丁，两套脚本同时躺在 `game/` 里。先卸载那一份，\n"
        "或者在一份干净的原版上重新复制。本补丁整体替换脚本、不注册 translate 块，\n"
        "所以冲突时报的不是 `A translation for \"X\" already exists`。")


def extras_of(manifest):
    """The optional packages a game declares, or [] when it has none."""
    return manifest.get("extras") or []


def extra_bits(manifest, slug):
    """-> the player-README fragments that introduce the optional packages.

    Both fragments come back as empty strings for a game with no extras, so
    PLAYER_README can name the tokens unconditionally: it is shared by every
    game in the collection and a per-game template would drift.
    """
    extras = extras_of(manifest)
    if not extras:
        return {"{{extranote}}": "", "{{extratree}}": ""}

    lang = manifest["language"]
    version = games.package_version(manifest)
    note = []
    tree = []
    for e in extras:
        label = e.get("label") or e["id"]
        zipn = extra_zip_name(slug, lang, e, version)
        note.append(
            "### 可选：%s\n\n"
            "另有一个**独立**的压缩包 `%s`。它和主补丁没有任何依赖关系，"
            "不装它主补丁照样完整可用；只有你装了对应 MOD 的玩家才需要它。\n\n"
            "解压后照里面 `README.md` 的说明操作即可。\n" % (label, zipn))
        tree.append(
            "可选包不在本包内，是一个独立压缩包：\n\n"
            "- `%s` —— %s" % (zipn, label))
    return {"{{extranote}}": "\n\n".join(note),
            "{{extratree}}": "\n\n".join(tree)}


def render_extra_readme(repo, manifest, slug, extra, version):
    """Fill an optional package's own README from its template.

    Same literal {{token}} substitution as render_readme, and the same reason
    for it.
    """
    counts = extra.get("counts") or {}

    # The pair count is cross-checked against the table actually shipped in
    # the zip rather than trusted from game.json. This README tells a player
    # how much is in the package; the package is the table. If the two drift,
    # the honest thing is to fail the build.
    table = next((f for f in extra.get("files", [])
                  if f.endswith(".json")), None)
    if table and "pairs" in counts:
        db = games.path_of(repo, table.replace("/", os.sep))
        actual = len(json.load(io.open(db, encoding="utf-8")))
        if actual != int(counts["pairs"]):
            raise SystemExit("%s: %s holds %d pairs but game.json says %s"
                             % (slug, table, actual, counts["pairs"]))

    fields = {
        "{{title}}": manifest["title"],
        "{{author}}": manifest["author"],
        "{{renpy}}": manifest["renpy_version"],
        "{{lang}}": manifest["language"],
        "{{langname}}": manifest["language_name"],
        "{{slug}}": slug,
        "{{version}}": version,
        "{{zipname}}": extra_zip_name(slug, manifest["language"], extra,
                                      version),
        "{{batname}}": extra.get("bat", "translate_mod.bat"),
        "{{modcount}}": "{:,}".format(int(counts.get("pairs", 0))),
        "{{modfiles}}": str(counts.get("modfiles", "")),
    }

    tpl = games.path_of(repo, extra["readme"].replace("/", os.sep))
    text = io.open(tpl, encoding="utf-8").read()
    for token, value in fields.items():
        text = text.replace(token, value)
    if "{{" in text:
        raise SystemExit("unfilled token left in %s" % extra["readme"])
    return text


def collect_extra(repo, manifest, slug, extra, version):
    """-> [(arcname, source_path_or_None, bytes)] in a stable order.

    A "flat" extra is laid out at the zip root instead of under a folder. Its
    README tells the player to drag the game's .exe onto the .bat, and a .bat
    locates its own translator and table with %~dp0 -- which only works if
    they sit beside it.
    """
    out = [("README.md", None,
            render_extra_readme(repo, manifest, slug, extra, version)
            .encode("utf-8"))]
    for rel in extra["files"]:
        src = games.path_of(repo, rel.replace("/", os.sep))
        if not os.path.isfile(src):
            raise SystemExit("%s: extra file %s is missing" % (slug, rel))
        arc = os.path.basename(rel) if extra.get("flat") else rel
        if arc.lower().endswith((".bat", ".cmd")):
            # cmd.exe cannot reliably parse a batch file whose lines end in
            # bare LF: it drops the "rem"/"echo" prefix and tries to run the
            # rest of the line as a command. Catch it here rather than let a
            # player find it.
            blob = io.open(src, "rb").read()
            if b"\n" in blob.replace(b"\r\n", b""):
                raise SystemExit("%s: %s needs CRLF line endings"
                                 % (slug, rel))
        out.append((arc.replace(os.sep, "/"), src, None))
    return sorted(out, key=lambda r: r[0])


def _write_zip(path, entries):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for arc, src, blob in entries:
            data = blob if blob is not None else io.open(src, "rb").read()
            info = zipfile.ZipInfo(arc, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)


def build_extras(slug):
    """Build every optional package a game declares.

    -> [{path, entries, meta}]; an empty list for a game without extras, so
    the caller can handle one shape across the whole collection.
    """
    repo, manifest = games.manifest(slug)
    slug = os.path.basename(repo)
    lang = manifest["language"]
    version = games.package_version(manifest)

    out_dir = os.path.join(games.ROOT, "dist")
    os.makedirs(out_dir, exist_ok=True)

    built = []
    for extra in extras_of(manifest):
        entries = collect_extra(repo, manifest, slug, extra, version)
        path = os.path.join(out_dir,
                            extra_zip_name(slug, lang, extra, version))
        _write_zip(path, entries)
        built.append({
            "path": path,
            "entries": entries,
            "meta": {"id": extra["id"],
                     "label": extra.get("label") or extra["id"],
                     "asset": os.path.basename(path)},
        })
    return built


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

    names = [n for _, ns in games.font_plan(manifest) for n in ns]
    note, tree, trouble = font_bits(manifest)
    fields.update(layout_bits(manifest))
    fields.update(fontrow_bits(manifest))
    fields.update(extra_bits(manifest, slug))
    # {{howtranslated}} and the install sentences come last: they are the ones
    # that embed tokens filled in above.
    fields["{{howtranslated}}"] = howtranslated_bits(manifest)
    fields.update(installer_bits(manifest, fields))
    # {{fontnote}} and {{packtree}} embed {{fonttree}} / {{patchfont}}, and the
    # loop below substitutes in insertion order, so those have to come first.
    fields.update({
        "{{fontnote}}": note,
        "{{fonttree}}": tree,
        "{{fonttrouble}}": trouble,
        "{{patchfont}}": names[0] if names else "",
    })
    text = PLAYER_README
    for token, value in fields.items():
        text = text.replace(token, value)
    if "{{" in text:
        raise SystemExit("unfilled token left in the player README")
    # A game with no extras leaves {{extranote}} empty, which would otherwise
    # leave a blank line where that section would have been.
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    return text


PLAYER_README = """# {{title}} — {{langname}}汉化补丁 {{version}}

| | |
|---|---|
| 游戏 | {{title}} |
| 原作 | {{author}} |
| 引擎 | Ren'Py {{renpy}} |
| 语言 | {{langname}}（启动时自动启用，不需要在设置里切换） |
| 译文 | {{count}} {{countlabel}}，覆盖率 100%，没有未译条目 |
| 翻译方式 | {{howtranslated}} |
| 中文字体 | {{fontrow}} |

---

## 安装

{{installintro}}

{{installsteps}}

装完直接启动游戏，{{langname}}会自动启用。

{{fontnote}}

{{extranote}}

---

## 常见问题

**装完还是英文**
游戏目录里残留了旧的 `.rpyc` 编译文件。Ren'Py 优先加载 `.rpyc`，旧的会盖过新脚本。
{{stalebytecode}}

**中文显示成方块**
{{fonttrouble}}

{{conflictfaq}}

{{fontfaq}}

**启动时报 `config.say_arguments_callback` 相关错误**
本补丁的语言脚本依赖 Ren'Py 8.x 的回调接口。原版游戏用的是 {{renpy}}，其它版本
如果报错请反馈。

---

## 关于这个压缩包

```
{{zipname}}
├── README.md              本文件
├── LICENSE                汉化补丁的许可
{{fontlicenserow}}{{toolrow}}└── game/                  {{gamehint}}
{{packtree}}
```

{{extratree}}

## 版权与免责

游戏版权归 {{author}} 所有。本汉化补丁是**非官方的同人翻译作品**，与原作方无任何
关联，仅供学习交流使用。请自行确认当地法律与原作方的授权状况。

{{packcontains}}
请勿将本补丁与游戏本体一同分发。

{{fontclose}}
"""


def build(slug):
    repo, manifest = games.manifest(slug)
    # games.manifest() tolerates slug=None and picks the only game in the
    # repository; from here on the resolved folder name is what we need.
    slug = os.path.basename(repo)
    lang = manifest["language"]
    version = games.package_version(manifest)

    # A script-override game has no build input to count: its data/tl_trans.json
    # is reverse-derived from the finished scripts, so its size says nothing
    # about the patch. game.json carries the real number instead.
    cov = manifest.get("coverage")
    if cov:
        count = int(cov["translated"])
    else:
        db = games.path_of(repo, "data", "tl_trans.json")
        count = len(json.load(open(db, encoding="utf-8"))) if os.path.isfile(db) else 0

    entries = collect(repo, slug, manifest, version, count)

    out_dir = os.path.join(games.ROOT, "dist")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, zip_name(slug, lang, version))

    _write_zip(out, entries)

    return out, entries, manifest


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--game", default=None,
                    help="games/ subfolder name; omit when there is only one")
    args = ap.parse_args()

    out, entries, manifest = build(args.game)
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

    for extra in build_extras(args.game):
        with io.open(extra["path"], "rb") as f:
            data = f.read()
        print("optional %-38s %8.2f MB  %s"
              % (extra["meta"]["asset"], len(data) / 1048576,
                 hashlib.sha256(data).hexdigest()[:16]))
        print("         %d entries" % len(extra["entries"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
