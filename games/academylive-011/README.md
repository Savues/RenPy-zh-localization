# AcademyLive 0.11 — 简体中文补丁

| | |
|---|---|
| 游戏 | AcademyLive 0.11 |
| 原作 | passhonQ |
| 引擎 | Ren'Py 8.1.3 |
| 语言 | 简体中文（`schinese`） |
| 译文量 | **24,002 条**，覆盖率 100%（43 条保留原文） |
| 翻译方式 | 全部人工撰写，**未使用任何机器翻译或在线翻译 API** |

```
academylive-011/
├── game.json           本游戏的元数据（引擎版本、字体、方案、坑）
├── assets/fonts/       随补丁分发的 Noto Sans SC + 授权声明
├── data/tl_trans.json  译文词表：以英文原文为 key
├── docs/
│   ├── glossary.json           术语表，由 check.py 强制执行
│   ├── translation-log.md      翻译档案：术语决策与修过的问题
│   └── approach.md             怎么把已装好的补丁收进这个仓库
└── patch/              构建产物（已提交，可直接安装）
    ├── tl/schinese/       63 个翻译后的 .rpy
    └── zh_patch.rpy       语言强制切换 + 字体注入 + 角色名显示层映射
```

---

## 安装（方式一：直接覆盖，不需要 Python）

从 [Releases](https://github.com/Savues/RenPy-zh-localization/releases) 下载补丁包，
三步：关掉游戏 → 解压 → 把解压出来的 `game/` 文件夹里的**全部内容**复制到游戏的
`game/` 文件夹，选择覆盖。

**中文字体已经打包在补丁里**，不用自己找、不用自己改文件名：

```
game/tl/schinese/                  →  <游戏目录>/game/tl/schinese/
game/zh_patch.rpy                  →  <游戏目录>/game/zh_patch.rpy
game/fonts/NotoSansSC-VariableFont_wght.ttf
                                   →  <游戏目录>/game/fonts/
```

装完直接启动，**不需要**在设置里切语言。

## 安装（方式二：脚本）

```bash
python tools/install.py "C:\Games\AcademyLive-0.11-pc" --game academylive-011
```

脚本做三件事：`patch/tl/schinese` 放进游戏的同名目录、`zh_patch.rpy` 放进 `game/`、
把 `assets/fonts/` 里的 Noto Sans SC 写进 `game/fonts/`。被覆盖的原始文件全部备份到
`game/.zh_patch_backup/`。

## 卸载

```bash
python tools/uninstall.py "C:\Games\AcademyLive-0.11-pc" --game academylive-011
```

从备份逐字节还原。确认无误后加 `--purge-backup` 一并删掉备份目录。

---

## 这个游戏特有的三个坑

**1. 角色名不能直接改成中文。**
游戏在八处拿角色变量和英文名做相等比较（`events.rpy`：`if em.name == "Emiko":`）。
把 `name` 赋成中文等于把这些分支全改坏。`zh_patch.rpy` 的做法是在**显示层**换成一个
`str` 子类：显示中文，`==` 仍与英文原名相等。名牌和 `[x.name]` 插值显示中文，
比较、字典查找、拼接的行为一个字不变。

**2. 字体注入只能用 `init -1`。**
`gui.*_font` 是被 `gui.text_properties()` 读进样式的，样式一旦建好就固化在内存里，
改变量不再生效。本作 `gui.rpy` 是 `init offset = -2`，`screens.rpy` 的 style 语句在
`init 0`——所以 `-1` 是**唯一**既能盖过 `gui.rpy` 的 define、又早于全部 style 的时机。
改到 `-2` 会掉回英文字体，中文全渲染成方块。脚本写死西文字体名的地方，再用
`config.font_replacement_map` 统一指向中文字体（该映射在字体加载时生效，所以盖得住
引擎在 `renpy/common/00style.rpy:139` 写死的 `DejaVuSans`）。

**3. 补丁目录不能多一层。**
`patch/tl/schinese/` 必须**原样**进 `game/tl/schinese/`，不是 `game/game/tl/schinese/`。
多一层 Ren'Py **不报错**，只是不加载，玩家看到的就是一份原版英文游戏。

另外，`zh_patch.rpy` 会删除失去 `.rpy` 源文件的陈旧 `.rpyc`——Ren'Py 优先加载字节码，
留着旧字节码会让中文静默失效，而且没有任何报错。

---

## 这个游戏的一条特殊规则：不要重跑 `build_tl.py`

`data/tl_trans.json` 是按英文原文做 key 的扁平字典，而本作有 **513 条**英文原文按上下文
该有两种译法（`Of course.` 回谢谢是「不客气。」，接提议是「好的。」）。扁平字典只能存
一种，重跑 `tools/build_tl.py` 会把它们全部塌缩掉，实测 **1,317 行**正文被改。

所以本目录的 `patch/` 是**成品**，不是 `build_tl.py` 的产物。要改哪句就直接改
`patch/tl/schinese/`，改完跑 `python tools/check.py --game academylive-011`。
译文库仍然查未译、乱码、叠字、行宽和术语，只是不当构建输入用。完整说明见
[`docs/translation-log.md`](docs/translation-log.md) 和 `game.json` 的
`_do_not_run_build_tl`。

---

## 版权

游戏版权归 passhonQ 所有。本目录**不包含**游戏的任何程序文件、图像、音频或原始脚本，
只包含翻译补丁与构建工具。字体 Noto Sans SC 以 SIL OFL 1.1 再分发，声明见
`assets/fonts/LICENSE-NotoSansSC.txt`。与 passhonQ 无任何关联。
