# The Inn 1.02.01-2 — 简体中文补丁

| | |
|---|---|
| 游戏 | The Inn 1.02.01-2 |
| 原作 | theinn |
| 引擎 | Ren'Py 8.5.0 |
| 语言 | 简体中文（`simplified_chinese`） |
| 译文量 | **5,421 条**，覆盖率 100%（11 条保留原文） |
| 翻译方式 | 全部人工撰写，**未使用任何机器翻译或在线翻译 API** |

```
theinn-10201/
├── game.json           本游戏的元数据
├── assets/fonts/       随补丁分发的 Noto Sans SC + 授权声明
├── data/tl_trans.json  译文词表：以英文原文为 key
├── docs/
│   ├── glossary.json           术语表 + 保留原文的 11 条 + 标签豁免
│   └── translation-log.md      翻译档案
└── patch/
    ├── tl/simplified_chinese/   89 个翻译后的 .rpy（含字体映射）
    └── zz_zh_locale.rpy        把语言钉死在简体中文
```

---

## 安装（方式一：直接覆盖，不需要 Python）

从 [Releases](https://github.com/Savues/RenPy-zh-localization/releases) 下载，三步：
关掉游戏 → 解压 → 把解压出来的 `game/` 文件夹里的**全部内容**复制到游戏的 `game/`
文件夹，选择覆盖。**中文字体已经打包在补丁里。**

```
game/tl/simplified_chinese/               ->  <游戏目录>/game/tl/simplified_chinese/
game/zz_zh_locale.rpy                     ->  <游戏目录>/game/zz_zh_locale.rpy
game/fonts/NotoSansSC-Regular.ttf         ->  <游戏目录>/game/fonts/
```

## 安装（方式二：脚本）

```bash
python tools/install.py "C:\Games\TheInn-1.02.01-2-pc" --game theinn-10201
python tools/uninstall.py "C:\Games\TheInn-1.02.01-2-pc" --game theinn-10201
```

---

## 三个必须知道的限制

**1. 对白上方的姓名牌还是英文。** 界面文本、选人界面、正文全是中文，
但说话人姓名是以变量送到屏幕的（`[linda.name]`），游戏自己的英文模板里没有
单名条目可翻，所以补丁里也没有一行带 `Linda`。要接上去得改写姓名变量，
相当于 Por(n)tals 用 shim 重映射 `Character()`。写法和原因记在
[`docs/glossary.json`](docs/glossary.json) 的 `_names_are_not_translated`。

**2. 语言必须钉死。** 游戏没有语言选择入口，而且启动画面会把语言改回英文
（`auto_lang()` → `renpy.change_language("english")`），老存档里记着的
`language` 也让 `config.default_language` 失效。`zz_zh_locale.rpy` 里两段代码
分别处理这两件事。

**3. 不要重跑 `build_tl.py`。** 61 条英文原文按上下文该有两种译法，扁平译文库
存不下，重建会改掉 190 行正文、另 10 行只差空格。`patch/` 是成品，
改完直接跑 `check.py` 就行。

顺带说明：`build_tl.py` 在这一款上**一定**返回 1 并报「未译 40 条」，那是
`zzz_fonts.rpy` 里的字体名列表，不是漏译。

---

## 版权

游戏版权归 theinn 所有。本目录**不包含**游戏的任何程序文件、图像、音频或原始脚本，
只包含翻译补丁与构建工具。字体 Noto Sans SC 以 SIL OFL 1.1 再分发
（改动说明见 `assets/fonts/LICENSE-NotoSansSC.txt`）。与 theinn 无任何关联。
