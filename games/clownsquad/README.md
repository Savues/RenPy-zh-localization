# Clown Squad 简体中文补丁

| | |
|---|---|
| 游戏 | Clown Squad（中文译名《弄臣本色》） |
| 原作 | Astreon |
| 引擎 | Ren'Py 8.3.4 |
| 语言 | 简体中文（启动时自动启用，不需要在设置里切换） |
| 译文量 | 5,406 个对白块 / 5,408 句 + 20 条界面字符串覆盖 |
| 覆盖率 | 对白 100%，未译 0 |
| 翻译方式 | 逐条人工翻译，**未使用任何机器翻译或在线翻译 API** |
| 中文字体 | MiSans（小米字体），已随包分发 |

补丁目录（玩家要的就是这些）：

```
game/tl/schinese/story01en.rpy   主线剧情 3,311 块
game/tl/schinese/script.rpy      支线与后日谈 2,095 块
game/zz_zh_locale.rpy            语言切换、字体映射、界面残留覆盖
game/fonts/MiSans-Regular.ttf    中文字体
game/fonts/MiSans-Bold.ttf       中文字体（真 Bold 字重）
```

---

## 安装

**不需要 Python，不需要安装器，不需要联网，也不用自己找字体。** 三步：

1. 把游戏**完全关闭**
2. 解压补丁包
3. 把解压出来的 `game` 文件夹里的**全部内容**复制到游戏的 `game` 文件夹，选择**覆盖**

```
要复制的东西                              复制到哪里
game/tl/schinese/story01en.rpy      →    <游戏目录>/game/tl/schinese/
game/tl/schinese/script.rpy         →    <游戏目录>/game/tl/schinese/
game/zz_zh_locale.rpy               →    <游戏目录>/game/
game/fonts/MiSans-Regular.ttf      →    <游戏目录>/game/fonts/
game/fonts/MiSans-Bold.ttf         →    <游戏目录>/game/fonts/
```

装完直接启动游戏。

> **只覆盖 `.rpy`，不要把 `.rpyc` 一起复制过去。** Ren'Py 优先加载 `.rpyc`，
> 残留的旧字节码会静默盖过新脚本。如果游戏目录里已经有旧补丁留下的 `.rpyc`，
> 先把 `game/tl/schinese/` 整个删掉再复制。

也提供脚本版：

```bash
python tools/install.py   "<游戏目录>" --game clownsquad
python tools/uninstall.py "<游戏目录>" --game clownsquad
```

想退回英文版：删掉 `game/zz_zh_locale.rpy`，或者把里面的 `zh_language` 改成 `None`。

---

## 这个游戏特有的坑

### 1. 游戏自带一套中文翻译，而且它在 archive.rpa 里

`archive.rpa` 里的 `tl/schinese/` **已经是中文**（随游戏一起发行的社区翻译），
`tl/russian/` 也在。这带来三个后果：

- **不能靠放新的 `translate schinese strings:` 块来改界面。** Ren'Py 对同一个原文字符串
  只允许注册一次翻译，归档先注册、松散文件后注册的话，启动时会抛
  `A translation for "..." already exists`。所以对白补丁用的是**与归档同名的文件**去
  盖住它（Ren'Py 只加载一份），剩下的 20 条界面残留由 `zz_zh_locale.rpy` 在 `init 999`
  直接改写已经建好的翻译表。**那份代码必须用 `dict.update()`**，
  `translations.add()` 遇到已存在的键会抛同一个错。
- **装补丁前必须先删掉旧补丁。** 再打一份会重复注册 `schinese`。
- **`tools/template.py` 导不进这个游戏。** 它看到中文就报错退出（那是防止把打过补丁的
  游戏当模板导进来）。英文模板是用 `games/clownsquad/tools/make_template.py` 从注释里
  还原出来的，过程见 [`docs/approach.md`](docs/approach.md)。

### 2. 字体必须走 `font_name_map`，不能覆盖字体文件

游戏自己的正文字体 `DejaVuSans.ttf`、`font/Bear Days.ttf` 都是纯拉丁字体，盖文件只会
把英文也一起换掉。`zz_zh_locale.rpy` 把每个字体名注册成 `FontGroup`：拉丁文保持游戏
原样，只有画不出的汉字和中文标点交给 MiSans。

归档自带的社区翻译里还有一段 `translate schinese python:` 会把 `gui.text_font` 指向
`tl/schinese/fonts/`。它在 init 的哪一步执行不该拿来赌字体，所以那几个字体名也一并
注册了——不管哪一套胜出，中文都走 MiSans。设置界面写死的 `font/NotoSansSC-Black.ttf`
本来就有完整中文覆盖，故意的没有动它。

如果看到方块，先确认 `game/fonts/MiSans-Regular.ttf` 在（约 7.7 MB），再确认
`game/zz_zh_locale.rpy` 在**游戏目录的 `game/` 下**，不是游戏根目录。

### 3. 一句英文只能有一个中文

`data/tl_trans.json` 以英文原文为 key，是 `build_tl.py` 的构建输入，所以同一句英文在
游戏里出现多次也只能有一个译法。有 34 组短叹词原本是分场景译的，逐条看过上下文之后
统一了，理由逐条写在 [`docs/translation-log.md`](docs/translation-log.md)。
Ren'Py 本身其实能表达一句英文在不同块里译得不同（游戏自带那套就是这么做的），
但仓库的构建工具表达不了。

### 4. 语言要强制

游戏把语言选择留给玩家，不装补丁第一次进的是英文原文。`zz_zh_locale.rpy` 设
`config.default_language`，并往 `config.start_callbacks` 里挂一个回调，
让**已有的存档**在下次启动时也切回简体中文。

---

## 校验

```bash
python tools/build_tl.py  --game clownsquad   # 从模板 + 译文库重建补丁，5408/5408
python tools/check.py     --game clownsquad   # 译文库 + 补丁 + 术语表
python tools/selftest.py  --game clownsquad   # 证明上面这些检查真的会报错
python tools/check_links.py
```

游戏侧另跑一次 Ren'Py 自带 lint，`tl/schinese` 的问题数必须是 0。

---

## 版权与免责

游戏版权归 **Astreon** 所有。本汉化补丁是**非官方的同人翻译作品**，与原作方无任何关联，
仅供学习交流使用。

本目录**不包含**任何游戏程序文件、图像、音频或原始脚本，只包含翻译补丁与中文字体。
请勿将本补丁与游戏本体一同分发。

中文字体的版权与授权见 [`assets/fonts/LICENSE-MiSans.txt`](assets/fonts/LICENSE-MiSans.txt)。
