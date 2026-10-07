# Scions of the Divine 0.1 — 简体中文

Ren'Py 视觉小说 **Scions of the Divine 0.1** 的中文本地化。全部 5,094 条译文人工
逐条撰写，未使用任何机器翻译或在线翻译 API。

| 项目 | 数值 |
|---|---|
| 原作 | Dark Seraph Productions |
| 原引擎版本 | Ren'Py 8.4.1 (2025-07-24 build) |
| 补丁方案 | 脚本覆盖（`patch_layout: script-override`） |
| 可翻译字符串 | 5,094 |
| 已翻译 | **5,094（100%）** |
| `data/tl_trans.json` 去重条目 | 4,630（有损，见下文） |
| 替换的脚本 | 27 个 `.rpy`（15,330 行）+ `zh_ui.rpy` |
| 补丁体积 | 0.59 MB 脚本 + 16.0 MB 字体 |

## 这个游戏为什么用脚本覆盖

仓库里有两种打补丁的方式。Eden 和 Sinful Summer 走 Ren'Py 的 `translate` 块；
这个游戏走不了，原因写在 [docs/approach.md](docs/approach.md)，一句话版本：

- 发行包把全部脚本压在 `game/archive.rpa` 里，`game/tl/` 只有
  `None/common.rpym`——那是 Ren'Py 自己写的运行时文件，不是翻译模板
- 仓库的 `tools/install.py` 只能放三样东西：`game/tl/<lang>/`、
  `game/<shim>.rpy`、`game/fonts/*`，它**无法覆盖游戏自己的脚本**

所以这个补丁直接用中文版 `.rpy` **整体替换**游戏自己的 27 个脚本。

**`archive.rpa` 一个字节都没改。** Ren'Py 加载脚本时磁盘上的 `game/<path>.rpy`
优先于归档里的同名条目，所以把中文脚本放进 `game/scripts/` 就顶掉了英文原稿。
1.1 GB 的归档保持原样。

**安装请用 `tools/install.ps1`。** 仓库的 `tools/install.py` 只会摆译文树、
`shim` 和字体，顶不掉游戏自己的脚本；对着这个游戏跑它会直接告诉你该用哪个安装器。

## 安装

不需要 Python。**先关掉游戏。**

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "D:\Games\ScionsoftheDivine-v0.1-pc"
```

或者手动（等价）：

```
patch/game/scripts/**   →  <游戏目录>/game/scripts/      27 个 .rpy，整体覆盖
patch/game/zh_ui.rpy    →  <游戏目录>/game/zh_ui.rpy
patch/zh_font.rpy       →  <游戏目录>/game/zh_font.rpy
assets/fonts/*.ttf      →  <游戏目录>/game/fonts/
```

装完启动游戏即可，Ren'Py 首次启动会自动重新编译。**不需要自己装字体。**

安装器会把被覆盖的每个文件先备份到 `game/.zh_patch_backup/`，并且只备份一次——
重复安装不会把你的备份冲掉。

> 这个游戏的磁盘上**原本没有任何松散的 `.rpy`**，所以安装器写的 29 个 `.rpy`
> 全部是"新文件"，一条备份都不会写。这是正常的，见 `docs/approach.md`。

## 卸载

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\uninstall.ps1 "D:\Games\ScionsoftheDivine-v0.1-pc"
```

逐字节还原英文原版。卸载器读 `manifest.json` 里安装器记下的文件清单逐条处理：
有备份就还原，没有就删除——所以那 29 个补丁引入的 `.rpy` 会被**删掉**，
而不是留下空壳或残留中文脚本。

## 安装器做了什么

1. 27 个中文 `.rpy` + `zh_ui.rpy` 覆盖到 `game/`
2. `zh_font.rpy` 字体注册（见下）
3. `MiSans-Regular.ttf` / `MiSans-Bold.ttf` 进 `game/fonts/`
4. **删除**有对应 `.rpy` 的陈旧 `.rpyc` / `.rpymc`——Ren'Py 优先加载 `.rpyc`，
   留着旧的会让中文静默失效。没有对应源文件的孤儿字节码保留不动。

## 字体

游戏自带三款拉丁字体（都在 `archive.rpa` 里）：

| 字体 | 用途 | 汉字 |
|---|---|---|
| `fonts/IMMORTAL.ttf` | 标题、按钮、标签 | **一个都没有** |
| `fonts/PlaypenSans-VariableFont_wght.ttf` | 正文手写体 | **一个都没有** |
| `fonts/rune.ttf` | 符文（`prim` 的台词） | **一个都没有** |

补丁把**全码位**交给 MiSans，不只是给中文兜底——拉丁字母和数字也由 MiSans 画，
全游戏观感统一。`patch/zh_font.rpy` 在 `init -999` 里把三个字体变量全部指向
`fonts/MiSans-Regular.ttf`：

```python
zh_text_font = zh_cjk        # 正文、界面
zh_display_font = zh_cjk     # 标题、按钮、标签
zh_rune_font = zh_cjk        # 符文
config.font_replacement_map[(zh_cjk, True, False)] = (zh_cjk_bold, False, False)
```

调用点（`gui.rpy` 的 `text_font` / `name_text_font`、7 处 `font zh_display_font`、
`prim` 的 `what_font`）全部自动继承，一处都不用单独改。

用真实的 `MiSans-Bold.ttf` 而不是 Ren'Py 的合成加粗：合成加粗会把密集的汉字
糊成一团。

**唯一一处不是 MiSans 的字体**：快进指示的三角箭头 `▸`（U+25B8）。MiSans 两个
字重都没有这个码位，原作的 `style skip_triangle` 本来就特意指定 `DejaVuSans.ttf`，
源码注释写明原因。已保留原样，并登记在 `tools/verify_patch.cjs` 的
`FONT_EXCEPTIONS` 里。

字形覆盖已实测：补丁里 29 个 `.rpy` 共 **58,444 个非 ASCII 码位，MiSans 全部命中，
零缺字**。这一项检查挂在 `verify_patch.cjs` 上，换字体后必跑。

字体授权说明见 [assets/fonts/LICENSE-MiSans.txt](assets/fonts/LICENSE-MiSans.txt) ——
MiSans 可商用，但字体文件本身没有书面再分发授权，这一点在那个文件里写清楚了。

## 启动画面仍是英文

**启动画面是图片。** 标题 `Scions of the Divine` 和内容警告（Content Warning）
在原作里是预渲染图片（`splashname` / `splashcw`），换字体不会影响它们。
这两处仍是英文，不是遗漏。

## 维护

- `data/tl_trans.json` —— 英文原文 → 中文，4,630 条去重映射。
  **它是有损的**：115 个英文句子在补丁里有不止一种中文译法（短感叹语按上下文
  分的，比如 `Yeah.` → 对。/ 嗯。/ 好。/ 认识。），扁平表只能保留第一次出现的
  那个。另外它对 `script-override` 方案**不是构建输入**，`check.py` 不读它。
- [`docs/glossary.json`](docs/glossary.json) —— 角色名与专有名词表，
  由 `check.py` 强制执行；`_developer_menu` 记着开发者菜单那 12 个标签和它们旁边的机器值
- [`docs/translation-log.md`](docs/translation-log.md) —— 术语决策、修过的问题
- [`docs/translation-workflow.md`](docs/translation-workflow.md) —— 引擎的坑、
  提取与回写脚本的设计、校验器为什么长成那样
- [`docs/approach.md`](docs/approach.md) —— 为什么这个游戏偏离仓库标准做法
- `tools/verify_patch.cjs` —— 补丁结构自检。改完 `.rpy` 跑一遍：
  `node tools/verify_patch.cjs`

### 校验查什么

```bash
node tools/verify_patch.cjs                                  # 挂在 extra_checks 上
python ../../tools/check.py --game scionsofthedivine-01
python ../../tools/selftest.py --game scionsofthedivine-01
```

`check.py` 对这个游戏**不查译文库**：这里的 `data/tl_trans.json` 是从做完的中文
脚本反向导出的副产品，拿它检查补丁等于让补丁给自己判卷。它查的是实际发出去的
29 个 `.rpy`——乱码、重复空格、叠字、术语冲突、标签闭合、文件缺失——然后跑
`extra_checks` 里的 `verify_patch.cjs`。覆盖率不重算，`game.json` 的 `coverage`
是断言。

## 版权

- 原作 **Scions of the Divine** © Dark Seraph Productions。本仓库只收录汉化
  补丁，不含任何原版素材、图像、音频或原始脚本。
- 中文译文为本仓库贡献。
- 字体 MiSans © 2020-2021 北京小米移动软件有限公司。