# Sinful Summer Chapter 3.6 简体中文补丁

| | |
|---|---|
| 游戏 | Sinful Summer Chapter 3.6 |
| 原作 | Ruykiru（协作：Alex-Productions） |
| 引擎 | Ren'Py 8.3.4 |
| 语言 | 简体中文（启动时自动启用，不需要在设置里切换） |
| 译文量 | 22,480 行对白 + 281 条系统字符串 + 19 个角色名 |
| 覆盖率 | 对白 100%，系统字符串 280/297（余 17 条为按键名、品牌名与格式串，不译） |
| 翻译方式 | 逐条人工翻译，**未使用任何机器翻译或在线翻译 API** |
| 中文字体 | MiSans（小米字体），已随包分发 |

补丁目录（玩家要的就是这些）：

```
game/tl/schinese/      20 个翻译脚本，22,480 个 translate 块
game/zz_zh_locale.rpy  语言切换、字体映射、角色名
game/fonts/MiSans-Regular.ttf   中文字体
```

---

## 安装

**不需要 Python，不需要安装器，不需要联网，也不用自己找字体。** 三步：

1. 把游戏**完全关闭**
2. 解压补丁包
3. 把解压出来的 `game` 文件夹里的**全部内容**复制到游戏的 `game` 文件夹，选择**覆盖**

```
要复制的东西                        复制到哪里
game/tl/schinese/        →      <游戏目录>/game/tl/schinese/
game/zz_zh_locale.rpy    →      <游戏目录>/game/zz_zh_locale.rpy
game/fonts/MiSans-Regular.ttf →  <游戏目录>/game/fonts/
```

装完直接启动游戏。

> **只覆盖 `.rpy`，不要把 `.rpyc` 一起复制过去。** Ren'Py 优先加载 `.rpyc`，
> 残留的旧字节码会静默盖过新脚本。如果游戏目录里已经有旧补丁留下的 `.rpyc`，
> 先把 `game/tl/schinese/` 整个删掉再复制。

也提供脚本版：

```bash
python tools/install.py   "<游戏目录>" --game sinfulsummer-chapter36
python tools/uninstall.py "<游戏目录>" --game sinfulsummer-chapter36
```

---

## 这个游戏特有的坑

### 1. 游戏目录里没有任何脚本文件

原作把所有 `.rpyc` 打进了 3.5 GB 的 `archive.rpa`，`game/` 下只有图片和字体。
因此 `tools/install.py` 的 `options.rpy` 存在性检查会误判这个目录不是游戏目录，
`tools/template.py` 也取不到英文模板。

本补丁因此**不走**「英文模板 + 译文库 → 重建补丁」的路线：`patch/` 是构建产物并已提交，
`data/tl_trans.json` 是事后从补丁反推出来的检索 / 校对数据库。

### 2. 中文字体必须走 `font_name_map`，不能覆盖字体文件

Ren'Py 在**渲染时**才查 `renpy.config.font_name_map`（`renpy/text/text.py`）。
脚本只给 328 行对白打了 `{font=font_narration}` 标签，其余 22,000+ 行以及全部菜单、
按钮、设置界面都走默认样式字体 `DejaVuSans.ttf`——**只映射别名是不够的**，
必须把字体文件名本身也注册进去，否则满屏方块。

`zz_zh_locale.rpy` 用 `FontGroup` 把 11 个字体名（5 个别名 + 6 个文件名）各自接上 MiSans：
拉丁文保持原样，中文走 MiSans。这是「用中文字体覆盖游戏字体文件」做不到的，
后者会把英文也一起换成中文字体。

如果看到方块，先确认 `game/fonts/MiSans-Regular.ttf` 在（7.7 MB），再确认
`game/zz_zh_locale.rpy` 在**游戏目录的 `game/` 下**，不是游戏根目录。

### 3. 语言要强制

原作会在 `init 999` 里把 `config.language` 改回去，`zz_zh_locale.rpy` 同样用
`init 999 python:` 注册 `config.start_callbacks`，每次启动都重新切回简体中文。

想退回英文版，把 `zz_zh_locale.rpy` 里的 `zh_language` 改成 `None`，
或者直接删掉这个文件。

### 4. 逐块差异译法

有 84 个英文原文在游戏里被译成了 2–4 种不同措辞（全是「嗯。」「啊——！」这类短感叹，
共 263 行）。这是有意为之，不是错误。详见
[`docs/translation-log.md`](docs/translation-log.md)。

---

## 校验

```bash
python tools/check.py    --game sinfulsummer-chapter36   # 译文库 + 补丁
python tools/selftest.py --game sinfulsummer-chapter36   # 证明上面这些检查真的会报错
python tools/check_links.py
```

游戏侧另跑一次 Ren'Py 自带 lint，`tl/schinese` 问题数必须是 0。

---

## 版权与免责

游戏版权归 **Ruykiru** 所有，渲染素材基于 Illusion 社的 HoneySelect2 与各位模组作者的成果。
本汉化补丁是**非官方的同人翻译作品**，与原作方无任何关联，仅供学习交流使用。

本目录**不包含**任何游戏程序文件、图像、音频或原始脚本，只包含翻译补丁与中文字体。
请勿将本补丁与游戏本体一同分发。

中文字体的版权与授权见 [`assets/fonts/LICENSE-MiSans.txt`](assets/fonts/LICENSE-MiSans.txt)。