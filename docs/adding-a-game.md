# 新增一个游戏的汉化

目标：让 `games/<slug>/` 成为下一个收录的游戏，**不改动 `tools/` 里的任何代码**。

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
| `shim` | ✅ | 语言补丁文件名。至少要设 `config.language`，字体注册和角色名映射也放这里 |
| `patch_font` | ✅ | 中文字体在游戏里落地的文件名 |
| `font_strategy` | | `shadow`（缺省）或 `fallback`，见下 |
| `font_shadow` | | 游戏硬编码的字体文件名。**只有 `shadow` 策略才用得上** |
| `font_asset` | ✅ | 仓库里打包的那份字体，见下 |
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

`package_release.py` 会把 `font_asset` 按 `patch_font` 加 `font_shadow` 里的每个名字各复制
一份到 `game/fonts/`，所以 `shadow` 策略下这个列表必须和游戏实际会去找的文件名一一对应。

### `font_shadow` 怎么找

只在 `shadow` 策略下需要。在游戏的 `.rpy` 里搜 `gui.text_font`、`gui.name_text_font`
和 `{font=`：

```bash
grep -rn "font=" "C:\Games\你的游戏\game" --include=*.rpy
grep -rn "_font *=" "C:\Games\你的游戏\game" --include=*.rpy
```

把所有出现过的字体文件名都列进去——包括藏在 `{font=...}` 标签里的，那些是运行时拼出来的，改配置改不掉。

## 2. 导入模板并提取待译条目

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

新建术语记得登记到 `games/<slug>/docs/glossary.json`，否则可能被后续润色改回别的译法。

## 4. 构建并校验

```bash
python tools/build_tl.py --game <slug>
python tools/check.py --game <slug>
python tools/selftest.py --game <slug>
```

`check.py` 要求未译条目为 0，这是硬性门槛。

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

```bash
# 装到一份干净的游戏副本
python tools/install.py "C:\Games\你的游戏" --game <slug>
# 启动游戏，确认中文生效且没有 errors.txt
# 再卸回来，确认原文件逐字节还原
python tools/uninstall.py "C:\Games\你的游戏" --game <slug>
```

最后对每个游戏跑一遍 `python tools/check.py --game <slug>`，确认仓库里所有游戏都还是干净的。

---

## 常见问题

**装了补丁但游戏里还是英文**
Ren'Py 优先加载 `.rpyc`。检查 `game/tl/schinese/` 里有没有残留的旧 `.rpyc`，`install.py` 会自动清理，但手动拷贝时容易漏。

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
