# Por(n)tals 0.4 — 简体中文补丁

| | |
|---|---|
| 游戏 | Por(n)tals 0.4 |
| 原作 | onehend |
| 引擎 | Ren'Py 8.2.0 |
| 语言 | 简体中文（`schinese`） |
| 译文量 | **23,910 条**，覆盖率 100%（3 条保留原文） |
| 翻译方式 | 全部人工撰写，**未使用任何机器翻译或在线翻译 API** |

```
portals-04/
├── game.json           本游戏的元数据
├── assets/fonts/       随补丁分发的 Noto Sans SC + 授权声明
├── data/tl_trans.json  译文词表：以英文原文为 key
├── docs/
│   ├── glossary.json           角色名表（由 shim 生成）
│   └── translation-log.md      翻译档案
└── patch/
    ├── tl/schinese/       12 个翻译后的 .rpy
    └── zz_zh_locale.rpy   开机修复 + 语言 + 字体 + 角色名重映射
```

---

## 安装（方式一：直接覆盖，不需要 Python）

从 [Releases](https://github.com/Savues/RenPy-zh-localization/releases) 下载，三步：
关掉游戏 → 解压 → 把解压出来的 `game/` 文件夹里的**全部内容**复制到游戏的 `game/`
文件夹，选择覆盖。**中文字体已经打包在补丁里。**

```
game/tl/schinese/              ->  <游戏目录>/game/tl/schinese/
game/zz_zh_locale.rpy          ->  <游戏目录>/game/zz_zh_locale.rpy
game/fonts/NotoSansSC-VF.ttf   ->  <游戏目录>/game/fonts/
```

## 安装（方式二：脚本）

```bash
python tools/install.py "C:\Games\Por(n)tals-0.4-pc" --game portals-04
python tools/uninstall.py "C:\Games\Por(n)tals-0.4-pc" --game portals-04
```

---

## 这个游戏特有的四个坑

**1. 原版发行包装不上补丁也起不来。**
`renpy/common/00layout.rpy:124` 调 `renpy.has_screen()`，而这里的 `renpy` 是包不是
`renpy.exports`，`AttributeError`。shim 第 0 节修掉它，**换成原版 Ren'Py 8.2 时删掉那一节**。

**2. 补丁原本是两个文件，这里合成一个。**
`zz_zh_setup.rpy`（开机修复 + 语言 + 字体）和 `zz_zh_names.rpy`（角色名）合并成
`zz_zh_locale.rpy`——仓库的打包器每个游戏只认一个 shim，两个文件它只会带走一个。
直接拼接是安全的：两个文件都用过 `init 999 python:`，Ren'Py 允许同优先级多次并按文件
顺序执行，其余优先级互不相同（-4000 / -300 / -100）。

**3. 角色名不走翻译系统。**
Ren'Py 不把 `Character("Mom")` 送进翻译流程。做法是 `init -300` 包住 `Character()`
在构造时改名字，再扫一遍 store。玩家自己输入的名字（`[mc_name]`）**故意不映射**。

**4. 补丁目录不能多一层。**
`patch/tl/schinese/` 必须原样进 `game/tl/schinese/`。多一层 Ren'Py 不报错，只是不加载。

**另外：不要重跑 `build_tl.py`。** 1,790 条英文原文按上下文该有两种译法，扁平译文库
存不下，重建会改掉 2,397 行正文。`patch/` 是成品，改完跑 `check.py` 就行。详见
[`docs/translation-log.md`](docs/translation-log.md)。

---

## 版权

游戏版权归 onehend 所有。本目录**不包含**游戏的任何程序文件、图像、音频或原始脚本，
只包含翻译补丁与构建工具。字体 Noto Sans SC 以 SIL OFL 1.1 再分发，声明见
`assets/fonts/LICENSE-NotoSansSC.txt`。与 onehend 无任何关联。
