# Realm Invader Episode 2 Part 2 — 简体中文补丁

| | |
|---|---|
| 游戏 | Realm Invader Episode 2 Part 2 |
| 原作 | Realm Invader |
| 引擎 | Ren'Py 7.4.11 |
| 语言 | 简体中文（`schinese`） |
| 译文量 | **16,183 条**，覆盖率 100%（7 条保留原文） |
| 翻译方式 | 全部人工撰写，**未使用任何机器翻译或在线翻译 API** |

```
realminvader-ep2p2/
├── game.json           本游戏的元数据
├── assets/fonts/       随补丁分发的 Noto Sans SC + 授权声明
├── data/tl_trans.json  译文词表：以英文原文为 key
├── docs/
│   ├── glossary.json           角色名表 + 保留原文的 7 条
│   └── translation-log.md      翻译档案
└── patch/
    ├── tl/schinese/       8 个翻译后的 .rpy
    └── zz_zh_locale.rpy   语言 + 字体 + 主菜单文字
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
python tools/install.py "C:\Games\RealmInvader-Episode_2_Part_2_1080p-pc" --game realminvader-ep2p2
python tools/uninstall.py "C:\Games\RealmInvader-Episode_2_Part_2_1080p-pc" --game realminvader-ep2p2
```

---

## 这个游戏特有的四个坑

**1. 不要重跑 `build_tl.py`。** 174 条英文原文按上下文该有两种译法，扁平译文库存不下，
重建会改掉 420 行正文。`patch/` 是成品，改完直接跑 `check.py` 就行。

**2. `build_tl.py` 在这一款上一定返回 1，这是正常的。** 那 167 条「未译」全是
`characters.rpy` 里角色名替换表的引号内容，不是对白，查不到就被跳过，而那行本来
就是成品的中文表。详见 [`docs/translation-log.md`](docs/translation-log.md)。

**3. 补丁原本是两个 shim，这里合成一个。** `zz_zh_cn.rpy` 和 `zz_zh_cn_menu.rpy`
合并成 `zz_zh_locale.rpy`——仓库的打包器每个游戏只认一个 shim，两个文件它只会带走
一个。

**4. 原版主菜单的文字在本机是看不见的。** 发行版用自制着色器画菜单文字，在白底板
上渲染成接近白色：按钮点得到、字看不见。shim 里的 `screen main_menu()` 保留原布局、
美术和 action，只把文字换成普通高对比度文本。

**另外：想用 MiSans 的话自己放。** shim 会在 `game/Fonts/` 里找到 MiSans 时自动启用，
但补丁不附带字体文件——MiSans 没有可援引的再分发授权。要用就自己把
`MiSans-Regular.ttf` / `MiSans-Bold.ttf` 丢进游戏的 `game/Fonts/`。

---

## 版权

游戏版权归 Realm Invader 所有。本目录**不包含**游戏的任何程序文件、图像、音频或
原始脚本，只包含翻译补丁与构建工具。字体 Noto Sans SC 以 SIL OFL 1.1 再分发，
声明见 `assets/fonts/LICENSE-NotoSansSC.txt`。与 Realm Invader 无任何关联。
