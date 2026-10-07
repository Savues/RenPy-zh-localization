# 新增一个游戏的汉化

目标：让 `games/<slug>/` 成为下一个收录的游戏，**不改动 `tools/` 里的任何代码**。

## 先选方案

仓库里有两种打补丁的方式，各有各的适用场景，**没有哪条是标准、哪条是例外**。
`game.json` 的 `patch_layout` 字段声明用哪种，工具链据此分支，不会替你猜。

| `patch_layout` | 什么时候用 | 补丁长什么样 |
|---|---|---|
| `tl-blocks`（缺省） | 游戏发行包里有 `game/tl/<lang>/` 翻译模板 | `patch/tl/<lang>/` 下是生成的 `translate` 块 |
| `script-override` | 游戏根本没做多语言结构，发行包里没有翻译模板 | `patch/game/` 直接顶掉游戏自己的 `.rpy` |

判断方法就是看一眼发行包：

```bash
dir "<游戏目录>\game\tl\schinese"
```

有内容 → `tl-blocks`。没有（只有 `game/tl/None/common.rpym` 之类）→ `script-override`。

两条路的**取舍**：

- `tl-blocks` 覆盖率可以机器验：`data/tl_trans.json` 是构建输入，`check.py` 拿它和英文
  原文逐条比，未译条目报错。代价是必须依赖游戏发翻译模板——有些游戏不发。
- `script-override` 没有这个依赖，但也没有基准可比：译文直接在脚本里，覆盖率只能靠
  提取阶段的数字**断言**在 `game.json` 里，`check.py` 不会从译文库推导，也不会假装能
  判断覆盖率。代价是补丁体积更大（整个脚本而不是几个块），且装错一层目录会被
  Ren'Py **静默忽略**。

`script-override` 的完整取舍和踩过的坑，见
[`games/cosycafe-0142/docs/approach.md`](../games/cosycafe-0142/docs/approach.md)——
那份文档是这条路的第一手记录，从它开始读比自己摸索快。

## 1. 建目录和元数据

```bash
mkdir games/<slug>
```

`<slug>` 用小写字母和连字符，例如 `eden-chapter5`、`some-vn-2024`。

写 `games/<slug>/game.json`：

```json
{
  "slug": "eden-chapter5",
  "title": "Eden Chapter 5",
  "author": "FnB Productions",
  "renpy_version": "8.4.1",
  "language": "schinese",
  "language_name": "简体中文",
  "patch_layout": "tl-blocks",
  "installer": "py",
  "shim": "zz_zh_locale.rpy",
  "patch_font": "zh.ttf",
  "font_strategy": "shadow",
  "font_shadow": [
    "comfortaa.ttf",
    "CinzelDecorative.ttf",
    "MichromaRegular.ttf",
    "PacificoRegular.ttf"
  ],
  "font_asset": "assets/fonts/MiSans-Regular.ttf",
  "font_license": "assets/fonts/LICENSE-MiSans.txt",
  "font_credit": "MiSans Regular (c) 2020-2021 Beijing Xiaomi Mobile Software Co., Ltd."
}
```

| 字段 | 必填 | 说明 |
|---|---|---|
| `slug` | ✅ | 必须和 `games/` 下的文件夹同名 |
| `title` | ✅ | 玩家 README 和 Release 列表里显示的名字 |
| `author` | ✅ | 原作作者，写进版权声明 |
| `renpy_version` | ✅ | 原版引擎版本，玩家对不上号时报错时用得上 |
| `language` | ✅ | Ren'Py 语言代码，中文简体固定 `schinese` |
| `language_name` | ✅ | 面向玩家显示的语言名 |
| `patch_layout` | | `tl-blocks`（缺省）或 `script-override`，见上面的「先选方案」 |
| `installer` | | `py`（缺省，用 `tools/install.py`）或 `ps1`（游戏自带安装器）。只服务 `tl-blocks` 的是 `py`；`script-override` 必须写 `ps1` 并在 `games/<slug>/tools/` 下自带一个 |
| `coverage` | | `script-override` 必填：`{"translated": N, "total": N}`。这是**断言**，不是推导出来的——工具不会重算它，写错了也没人会发现，所以数字要有出处（写进 `_coverage_note`） |
| `extra_checks` | | 这个游戏自己要额外跑的命令，`cwd` 是游戏目录。`script-override` 常需要，见下 |
| `shim` | ✅ | 语言补丁文件名。至少要设 `config.language`，字体注册和角色名映射也放这里 |
| `patch_font` | ✅ | 中文字体在游戏里落地的文件名 |
| `font_strategy` | | `shadow`（缺省）或 `fallback`，见下 |
| `font_shadow` | | 游戏硬编码的字体文件名。**只有 `shadow` 策略才用得上** |
| `font_asset` | | 仓库里打包的那份字体，见下。字体不止一份时改用 `font_assets` |
| `font_assets` | | 一般形式：`[{"path": ..., "names": [...]}, ...]`，一份文件可以写成多个游戏里会去找的名字。`font_asset` / `patch_font` / `font_shadow` 三件套是它的简写，仍然可用 |
| `font_license` | ✅ | 字体授权声明，打包时以 `FONT-LICENSE.txt` 放进压缩包根目录 |
| `font_credit` | ✅ | 玩家 README 里显示的字体署名 |

### 先定字体策略

`font_strategy` 决定中文字体怎么进到屏幕上，动手写 `<shim>` 之前就得定下来。

**`shadow`（缺省）** —— 游戏把字体**文件名**写死，补丁直接覆盖磁盘上那几个同名文件。
`font_shadow` 要列全所有会被覆盖的名字，打包时同一份字体会按这些名字各存一份放进
`game/fonts/`。Eden Chapter 5 走这条：一个游戏 5 份字体，约 25.7 MB。

**`fallback`** —— 绝大多数文本走默认字体，覆盖文件没有意义（Sinful Summer 只有 328 行
打了 `{font=...}` 标签，其余两万行和全部界面都是默认字体）。改成在 `<shim>` 里用
`renpy.config.font_name_map` 把字体注册成 `FontGroup`，**只接管游戏原字体画不出的汉字和
中文标点**。包里只有一份字体，游戏自带的字体文件原封不动。

判断方法：统计 `{font=` 在游戏脚本里出现的行数。绝大多数文本走默认字体的用 `fallback`，
对话框、界面、脚本都写死字体文件名的用 `shadow`。写法细节和踩过的坑见
[fonts.md](fonts.md#两种接入方式)。

### 打包要用的字体字段

`font_asset` / `font_license` / `font_credit` 三个不填，游戏里照样能显示中文——但玩家的
压缩包里**没有字体，也没有授权声明**。字体放这里：

```
games/<slug>/assets/fonts/<字体>.ttf
games/<slug>/assets/fonts/LICENSE-<字体>.txt
```

`package_release.py` 按 `font_plan()` 决定放几份、叫什么名字：`font_assets` 优先，
否则退回 `font_asset` + `patch_font` + `font_shadow`。`shadow` 策略下名字必须和游戏
实际会去找的文件名一一对应；字体文件缺失时打包直接报错，不会打出一个装上去没字体的包。

### `font_shadow` 怎么找

只在 `shadow` 策略下需要。在游戏的 `.rpy` 里搜 `gui.text_font`、`gui.name_text_font`
和 `{font=`：

```bash
grep -rn "font=" "C:\Games\你的游戏\game" --include=*.rpy
grep -rn "_font *=" "C:\Games\你的游戏\game" --include=*.rpy
```

把所有出现过的字体文件名都列进去——包括藏在 `{font=...}` 标签里的，那些是运行时拼出来的，改配置改不掉。

## 2. 导入模板并提取待译条目（`tl-blocks` 方案）

`script-override` 的游戏跳过本节和第 3 节——它没有模板可以导入，也没有译文库要建。

```bash
python tools/template.py "C:\Games\你的游戏" --game <slug>
```

会把 `game/tl/schinese` 复制到 `games/<slug>/tl_template/`。这个目录是**游戏的原始英文脚本**，已被 `.gitignore` 排除，不要提交。

脚本会拒绝指向已打过补丁的游戏（检测到中文就报错），免得把译文当成模板导进去。

跑完用这段看看有多少条目要翻：

```python
import sys; sys.path.insert(0, "tools")
import tlparse
files, order = tlparse.load("games/<slug>/tl_template")
texts = tlparse.unique_texts(files)
print(len(texts), "unique strings")
```

## 3. 写译文

建 `games/<slug>/data/tl_trans.json`，以**英文原文为 key**：

```json
{
  "Hello, world.": "你好，世界。",
  "Are you sure?": "你确定吗？"
}
```

以下内容**不要**翻译，`check.py` 会拦住：

- Ren'Py 变量与标签：`[playername]`、`{size=32}`、`{#filetime}%A, %B`
- 按键名与格式串：`Ctrl`、`Esc`、`%b %d, %H:%M`
- URL 与文件路径
- 角色名牌（放在 `patch/<shim>` 的名字映射里，不是译文库）

新建术语记得登记到 `games/<slug>/docs/glossary.json`，否则可能被后续润色改回别的译名。

### `script-override` 方案怎么写译文

不建译文库，直接改 `patch/game/` 下对应脚本里的字符串字面量。两件事必须做：

**一、逐文件核对结构。** 字符串字面量的行号、列号、引号类型、是否三引号、语句关键字
序列、把所有字符串遮蔽后的代码骨架，都要和原版一致，只允许字面量**内容**不同。
写个脚本比手看可靠——`games/cosycafe-0142/tools/verify_patch.cjs` 是现成的例子。

**二、写一个 `extra_checks` 挂上去。** 这一步不是可选的。共享的检查只看得出乱码、
叠字、术语冲突，看不出一段脚本**被改坏**了。`script-override` 补丁的经典事故是按
「文件 + 行号 + 列号」定位字面量回写，中文比英文短，同一行里靠后的字面量整体左移，
再跑一次就写错位置——Cosy Cafe 的 `WeekDays` 就这样把星期四写成了星期三，
没有任何通用 linter 能看出来，因为语法完全合法。

```json
"extra_checks": [["node", "tools/verify_patch.cjs"]]
```

`cwd` 是游戏目录。检查什么由你自己定：已知枚举的完整值、同一行里相邻中文字面量是否
重复、关键变量的取值范围——凡是「结构合法但内容错了」的东西，都归它管。

`check.py` 会自动跑 `extra_checks`，非零退出就算失败。

### `coverage` 怎么填

`script-override` 的覆盖率是从**英文原文**统计出来的玩家可见字面量数，不是从译文库
统计的（那份库是从做完的中文脚本反向导出的副产品，拿它算覆盖率等于让补丁给自己判卷）。
所以：

- `total` = 提取阶段认定的全部玩家可见字面量
- `translated` = 补丁里实际写了中文的条数
- 两者相等才写 100%，并把统计口径写进 `game.json` 的 `_coverage_note`

`check.py` 不会重算这两个数字，也不会因为它们不符而报错——它只负责把它们打印出来。
**写错没人会发现**，所以数字要有出处。

## 4. 构建并校验

```bash
# tl-blocks：从模板 + 译文库重建补丁
python tools/build_tl.py --game <slug>

# 两种方案都要跑
python tools/check.py --game <slug>
python tools/selftest.py --game <slug>
```

`tl-blocks` 的 `check.py` 要求未译条目为 0，这是硬性门槛。`script-override` 不查这一项
（没有英文原文可比），改查乱码、重复空格、叠字、术语冲突、标签闭合、文件缺失，
外加你的 `extra_checks`。

## 5. 写游戏自己的 README

`games/<slug>/README.md` 至少要有：

- 一张概览表（游戏 / 原作 / 引擎 / 语言 / 译文量 / 覆盖率）
- 安装与卸载命令（带 `--game <slug>`）
- **这个游戏特有的坑**——引擎版本、硬编码字体名、角色名机制等等。别人接手时最需要的就是这部分
- 版权说明

## 6. 更新根 README 的索引表

```bash
python tools/games.py --readme
```

根 `README.md` 的「已收录」表格是从 `games/` 生成的，两个 `<!-- games:start -->` 标记
之间的内容不要手改。`check_links.py` 会核对它有没有过期。

## 7. 验证

`installer` 是 `py`：

```bash
# 装到一份干净的游戏副本
python tools/install.py "C:\Games\你的游戏" --game <slug>
# 启动游戏，确认中文生效且没有 errors.txt
# 再卸回来，确认原文件逐字节还原
python tools/uninstall.py "C:\Games\你的游戏" --game <slug>
```

`installer` 是 `ps1`（`script-override` 必走这条）：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File games\<slug>\tools\install.ps1 "C:\Games\你的游戏"
# 启动游戏，确认中文生效且没有 errors.txt
# 再卸回来
powershell -NoProfile -ExecutionPolicy Bypass `
  -File games\<slug>\tools\uninstall.ps1 "C:\Games\你的游戏"
```

安装器必须做到三件事，缺一件就等于埋雷：

- **先备份**每个会被覆盖的文件，且**只备份一次**（重复安装不能把玩家的备份冲掉）
- **删除**失去源文件的陈旧 `.rpyc` / `.rpymc`。Ren'Py 优先加载字节码，留着旧的会让
  中文静默失效，而且没有任何报错
- 写一份 **manifest**（写了哪些文件、备份在哪），让 `uninstall.py` 能跨安装器还原。
  两边对「原本就不存在的文件」必须用同一个约定——本仓库的约定是**不写 0 字节占位
  文件**，而是让备份函数返回「原本不存在」

备份目录记得**自底向上剪空目录**，否则卸载完会留一串空壳。

最后对每个游戏跑一遍 `python tools/check.py --game <slug>`，确认仓库里所有游戏都还是干净的。

---

## 常见问题

**装了补丁但游戏里还是英文**
两种可能，先看是哪种：

1. Ren'Py 优先加载 `.rpyc`。检查补丁目录里有没有失去 `.rpy` 源文件的残留字节码，
   安装器会自动清理，手动拷贝时容易漏。
2. **目录多了一层。** `script-override` 的补丁必须**原样**放进游戏的 `game/`：
   `patch/game/gui.rpy` → `game/gui.rpy`，不是 `game/game/gui.rpy`。多一层 Ren'Py
   **不报错**，只是不加载，玩家看到的就是一份原版英文游戏。这是本仓库曾经真实
   发出去过的包级 bug，`package_release.py` 现在统一走 `games.patch_entries()`，
   目的就是让这种错不可能再发生。

**`build_tl.py` 报缺 `tl_template/`**
`patch_layout` 声明错了。这个游戏没有翻译模板可编译，补丁应该是直接改写脚本做出来的
（`script-override`），改 `game.json` 而不是去造一个模板。

**`install.py` 提示这个游戏不该用它**
`installer` 声明的是 `ps1`。它只会摆译文树、`shim` 和字体，顶不掉游戏自己的脚本，
这类游戏在 `games/<slug>/tools/` 下自带安装器，照那个游戏的 `README.md` 走。

**`check.py` 报术语冲突，但那句话没问题**
`banned` 是**纯子串匹配**。一个同时也是普通中文词、或者另一个名字的一部分的写法，没法
放进 `banned`——本仓库的三个游戏都踩过（`红` 出现在 272 行、`埃莉` 是 `埃莉森` 的
前缀、`女校长` 是游戏自己对校长的称呼）。遇到这种就在 `glossary.json` 里写一条
`_banned_is_a_blunt_substring_match` 说明它是靠注释钉住的，而不是靠禁用词。
两个汉字的术语还会撞上叠字检查（`校长 长得` 读起来就是 `校长长`），这类写进
`_doubling_exempt`。

**中文显示成方块**
`shadow` 策略下是 `font_shadow` 漏了某个字体文件名；`fallback` 策略下检查 `<shim>` 有没有
复制到游戏的 `game/` 目录、以及 `game/fonts/` 里的字体在不在。先用
`install.py "<游戏目录>" --font <路径>` 手动指定一款字体，确认是不是字体问题。

**启动就崩，报 `A translation for "X" already exists`**
几乎总是因为游戏里已经打过**另一份**汉化补丁，两份都注册了 `schinese`。先卸掉那一份，
或者在一份干净的原版上重新复制。译文库本身不会造成这个错——它以英文原文为 key，
`build_tl.py` 从字典生成脚本，同一句原文只会产出一个 translate 块。

**游戏把 `config.language` 重置成 `None`**
有些游戏在 `init -1600 python hide:` 里重置语言。`<shim>` 里的赋值必须放在**普通的** `init python:` 块里，优先级比它高、后执行。
