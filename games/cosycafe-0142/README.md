# Cosy Cafe 0.14.2 — 简体中文

Ren'Py 视觉小说 **Cosy Cafe 0.14.2** 的完整中文本地化。全部译文人工逐条撰写，未使用任何机器翻译或在线翻译 API。

| 项目 | 数值 |
|---|---|
| 原引擎版本 | Ren'Py 8.3.2 (2024-09-09 build) |
| 可翻译字面量 | 32,639 |
| 已翻译 | **32,639（100%）** |
| `data/tl_trans.json` 去重条目 | 25,828 |
| 替换的脚本文件 | 27 个 `.rpy`，42,845 行主剧情 |
| 补丁体积 | 3.8 MB 脚本 + 15.3 MB 字体 |

## 这个游戏为什么不用 translate 补丁

仓库里另外两款游戏走的是 Ren'Py `translate` 块路线：`data/tl_trans.json` 存英文原文，
`tools/build_tl.py` 生成 `game/tl/schinese/`。**Cosy Cafe 走不了这条路**，原因写在
[docs/approach.md](docs/approach.md)，一句话版本：

- 发行包**不带** `game/tl/` 翻译模板（只有 `game/tl/None/common.rpym`），没有模板就无法生成翻译块
- 仓库的 `tools/install.py` 只能放三样东西：`game/tl/<lang>/`、`game/<shim>.rpy`、`game/fonts/*`，
  它**无法覆盖游戏自己的脚本**

所以这个补丁直接用中文版 `.rpy` **整体替换**游戏自己的 27 个脚本。它是经过验证的方案：
启动日志无 error、结构校验逐字节通过、实机运行确认。

**因此安装请用 `tools/install.ps1`，不要用 `tools/install.py`。**

## 安装

不需要 Python。

```powershell
# 关掉游戏，然后：
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "D:\Games\CosyCafe-0.14.2-pc"
```

或者手动（等价）：

```
patch/game/**            →  <游戏目录>/game/     全部覆盖
patch/zz_zh_locale.rpy   →  <游戏目录>/game/zz_zh_locale.rpy
assets/fonts/*.ttf       →  <游戏目录>/game/fonts/
```

装完启动游戏即可，Ren'Py 首次启动会自动重新编译。**不需要自己装字体**。

安装器会把被覆盖的每个文件先备份到 `game/.zh_patch_backup/`，并且只备份一次 ——
重复安装不会把你的备份冲掉。

## 卸载

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\uninstall.ps1 "D:\Games\CosyCafe-0.14.2-pc"
```

逐字节还原英文原版，并清掉重编译产生的字节码。补丁没有覆盖的文件
（例如游戏自带的 `gui/msp1/centurygothic.ttf`、`scripts/01never_touched.rpy`）原样保留。

## 安装器做了什么

1. 27 个中文 `.rpy` 覆盖到 `game/`
2. `zz_zh_locale.rpy` 字体兜底（见下）
3. `MiSans-Regular.ttf` / `MiSans-Bold.ttf` 进 `game/fonts/`
4. **删除**有对应 `.rpy` 的陈旧 `.rpyc` / `.rpymc` —— Ren'Py 优先加载 `.rpyc`，
   留着旧的会让中文静默失效。没有对应源文件的孤儿字节码保留不动。

## 字体

游戏自带的 `gui/msp1/centurygothic.ttf`、`gensans.otf`、`gensanslight.otf`、
`Tungsten.ttf` 以及 Ren'Py 的 `DejaVuSans.ttf` **都不含中文字形**，直接显示中文会变成方块。

补丁把 **130 处**字体引用（12 个文件）全部指向 `fonts/MiSans-Regular.ttf`，
并替换 `gui.rpy` 里的 `gui.text_font` / `gui.name_text_font` / `gui.interface_text_font`。

`patch/zz_zh_locale.rpy` 是第二道保险：如果哪个界面仍然请求了游戏自带的拉丁字体，
它会用 FontGroup 让该字体负责拉丁字符、MiSans 负责 CJK 码位区间，
避免漏网的界面画成豆腐块。

`MiSans-Bold.ttf` 目前**没有任何引用** —— 全游戏 `<b>` 标签数为 0，`gui.rpy` 也没定义
任何粗体样式。留着是为了以后加粗时不用重新找字体，不想要可以直接删。

字形覆盖已实测：游戏内 **517,804 个汉字 + 88,123 个中文标点，MiSans 全部命中，零缺字**。

`story 0.12/0.13/0.14.rpy` 里美咲的台词带少量 emoji（🥺 🫣 🥰 😟）。MiSans 不含 emoji 字形，
但 Ren'Py 8.3.2 自带 `renpy/common/TwemojiCOLRv0.ttf` 作兜底，会自动接管。

字体授权说明见 [assets/fonts/LICENSE-MiSans.txt](assets/fonts/LICENSE-MiSans.txt) ——
MiSans 可商用，但字体文件本身没有书面再分发授权，这一点在那个文件里写清楚了。

## 维护

- `data/tl_trans.json` —— 英文原文 → 中文，25,828 条去重映射。改这里，然后重新生成补丁
- `docs/glossary.json` —— 角色名与专有名词表，钉死译名防止后续润色改口
- `docs/translation-log.md` —— 分批翻译记录
- [docs/approach.md](docs/approach.md) —— 为什么这个游戏偏离仓库标准做法

有 8 条 `tl_trans.json` 的值和 key 完全相同，是**故意保留**的（平台名、游戏标题、
RGB 取色器格式串、缩放系数），不是漏译。`tools/check.py` 的 `KEEP` 规则匹配不到它们，
所以对本作跑 `check.py` 会报「未翻译」—— 这是预期行为，原因见 `docs/glossary.json`
的 `_kept_verbatim_note`。

## 版权

- 原作 **Cosy Cafe** © Cosy Creator。本仓库只收录汉化补丁，不含任何原版素材。
- 中文译文为本仓库贡献。
- 字体 MiSans © 2020-2021 北京小米移动软件有限公司。
