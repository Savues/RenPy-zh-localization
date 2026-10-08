# DropOut Saga 0.12.0b — 简体中文

LazyBloodLines / Ren'Py 8.3.3 / Windows

15,214 条可翻译字面量全部处理：14,941 条中文，273 条按[术语表](docs/glossary.json)保留原文
（纯插值串、Ren'Py Preference 键名、引擎标识，以及游戏内出现的德语／俄语／法语）。
译文全部人工撰写，没有用过任何机器翻译或在线 API。

除了主汉化，补丁还带三样东西：一份 0.12 可用的**攻略工具**、一个**属性点编辑与场景跳转
工具箱**，以及 Shawn's Mod 的**兼容补丁**与可选汉化。

## 这个游戏为什么用脚本覆盖

0.12.0b 的发布包里只有 `game/tl/None/common.rpym` —— 没有任何语言模板。
`build_tl.py` 没有输入，`install.py` 没有东西可放。
所以补丁直接替换游戏自己的 14 个 `.rpy`，脚本本身就是补丁。详见 [approach.md](docs/approach.md)。

## 安装

先关掉游戏，然后：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "D:\Games\DropOutSaga-0.12.0b-pc"
```

只用 PowerShell，不需要 Python。它会备份被覆盖的文件到
`game/.zh_patch_backup/`，删掉会盖过新脚本的旧 `.rpyc`，并把 MiSans 装进
`game/Fonts/`。首次启动时 Ren'Py 会重新编译中文脚本。

### 顺便把 Shawn's Mod 也汉化（可选）

MOD 是玩家自己装的第三方内容，补丁不分发它。加 `-WithMod`：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "D:\Games\DropOutSaga-0.12.0b-pc" -WithMod
```

这会用**游戏自带的 Python 3.9** 读取你那份 `game/mod/*.rpyc`，按
[`data/mod_zh.json`](data/mod_zh.json) 的 1,273 条译文重建一份中文版，再覆盖回去。
必须用游戏里的解释器，原因见 [approach.md](docs/approach.md#为什么-mod-必须在游戏自带的-python-39-下重建)。

> 如果你还没装 MOD，`-WithMod` 会报错退出。先装 MOD，再回来跑一次。

## 卸载

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\uninstall.ps1 "D:\Games\DropOutSaga-0.12.0b-pc"
```

备份树里有什么就还原什么，补丁新增的文件删掉，游戏回到未打补丁的状态。
MOD 的英文 `.rpyc` 也在同一棵备份树里，所以一并还原。

## 补丁里有什么

| 文件 | 作用 |
|---|---|
| `patch/game/day1_update.rpy` … `day8_update.rpy` | 八天主线 |
| `patch/game/script.rpy` | `Character()` 定义与开场，角色名的唯一权威 |
| `patch/game/gui.rpy` `options.rpy` `screens.rpy` | 界面与选项 |
| `patch/game/patreonmenu.rpy` `replay_gallery.rpy` | 作者菜单与回放库 |
| `patch/000_zh_fonts.rpy` | 字体映射 shim，放在 game 根目录，必须先于 `gui.rpy` 求值 |
| `patch/game/000_zh_modcompat.rpy` | MOD 兼容：补 4 个缺失变量、修 6 个会 `NameError` 的攻略屏 |
| `patch/game/001_zh_guide_data.rpy` `002_zh_guide_ui.rpy` | 攻略数据与界面（22 个 label） |
| `patch/game/003_zh_tools_data.rpy` `zz_zh_tools_ui.rpy` | 工具箱：属性点编辑、场景跳转 |

发布包里另外 5 个脚本（`Bust_Char.rpy`、`images.rpy`、`myscreens.rpy`、
`PhoneTexting.rpy`、`replay_scenes.rpy`）**故意不打包**：它们一共只有 7 条字符串，
全是资源名、样式前缀和颜色值，而且和原版逐字节相同 —— 复制一个自己没改过的文件，
是脚本覆盖补丁唯一一件翻译补丁绝不会做的事。

## 字体

MiSans Regular / Bold（小米，MIT），通过 `config.font_replacement_map`
替换 35 个字体映射。授权见 [`LICENSE-MiSans.txt`](assets/fonts/LICENSE-MiSans.txt)。

两个 ttf 与仓库里另外四个游戏（Clown Squad、Cosy Cafe、Scions of the Divine、
TOXICity）的 Regular 完全同一份字节；Eden Chapter 5 的 Regular 是另一个构建，
已在授权说明里明确排除。

## 已知问题

- **主菜单没有背景。** 发布包缺 `gui/main_menu.png`，`images.rpa` 的 6,279 个条目里也没有。
  这是发行包的缺陷，不是补丁造成的。
- **MOD 的 `meeting_1_m` 支线没翻。** 那 1,028 句是作者为 0.6.9a 写的 Day 1 替代线，
  挂载点 `label meeting_1` 在 0.12 已被整条删除，游戏里 97% 的地方不存在这条线。
  其余 MOD 内容都已翻译且可达。
- 屏幕探针只能证明界面能构建，不能证明排版和键盘交互正确 —— 这部分靠实机。

## 维护

```powershell
python tools\check.py --game dropout-saga-0120
python games\dropout-saga-0120\tools\verify_patch.py
```

安装/卸载的往返由 [`tools/roundtrip_test.ps1`](tools/roundtrip_test.ps1) 验：
它把夹具重置成原版英文，跑一遍安装（含 `-WithMod`）再卸载，
然后逐文件比 SHA-256。夹具不在仓库里 —— 它需要游戏自带的 `renpy/` 和
`lib/python3.9`（解释器靠它们启动）以及本仓库不分发的英文原版脚本，
所以脚本头部写了怎么搭一次。

### 校验查什么

仓库通用的 `check.py` 查乱码、双空格、术语表禁用变体、双字叠词、`[i]`/`[b]`
标签配对。`verify_patch.py` 查通用工具看不见的那一类 —— **语法合法但语义写错**：

1. **列号偏移。** 中文比英文短，按列号写回会落到错的字面量上；表现是同一行相邻两个
   中文串完全相同，或者每个文件的字面量总数发生位移。两项都比对基线。
2. **形近字。** 工具箱标题里的「堕」曾被写成 U+581D「堝」（左土而不是左阝），
   渲染出来几乎一样，能躲过人工复核和所有其他检查。现在标题由 `config.name` 派生，
   码位直接断言。
3. **名字里混进别人的名字。** `love_ava` 和 `corruption_ava` 曾经都写成「艾」+「娅」，
   而攻略数据里的「索菲娅」是对的 —— 单看任何一张表都看不出问题。
   现在补丁显示的每个角色名都和 `script.rpy` 自己的 `Character()` 全等比对。
4. **覆盖率只声明不重算。** `data/coverage.json` 里的数字会被重新推导，
   算术和每个文件的行数／字面量数都会验。

## 版权

游戏本身 © LazyBloodLines。本仓库只发布补丁，不含任何原版脚本、图片或音频。
译文与补丁代码可自由使用。MiSans © 2020-2021 北京小米移动软件有限公司，MIT。
