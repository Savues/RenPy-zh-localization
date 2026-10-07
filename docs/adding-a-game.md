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
  "font_shadow": ["comfortaa.ttf", "CinzelDecorative.ttf"]
}
```

| 字段 | 说明 |
|---|---|
| `language` | Ren'Py 语言代码。中文简体固定是 `schinese` |
| `shim` | 语言补丁文件名。至少要设 `config.language`，字体覆盖和角色名映射也放这里 |
| `patch_font` | 中文字体在游戏里落地的文件名 |
| `font_shadow` | **游戏硬编码的字体文件名**。中文补丁靠覆盖这些同名文件来生效 |

### `font_shadow` 怎么找

在游戏的 `.rpy` 里搜 `gui.text_font`、`gui.name_text_font` 和 `{font=`：

```bash
grep -rn "font=" "C:\Games\你的游戏\game" --include=*.rpy
grep -rn "_font *=" "C:\Games\你的游戏\game" --include=*.rpy
```

把所有出现过的字体文件名都列进去——包括藏在 `{font=...}` 标签里的，那些是运行时拼出来的，改配置改不掉。

## 2. 导入模板并提取待译条目

```bash
python tools/template.py "C:\Games\你的游戏"
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

在仓库根 `README.md` 的「已收录」表格里加一行，链到 `games/<slug>/README.md`。

## 7. 验证

```bash
# 装到一份干净的游戏副本
python tools/install.py "C:\Games\你的游戏" --game <slug>
# 启动游戏，确认中文生效且没有 errors.txt
# 再卸回来，确认原文件逐字节还原
python tools/uninstall.py "C:\Games\你的游戏" --game <slug>
```

最后跑一遍 `check.py`，确认仓库里所有游戏都还是干净的。

---

## 常见问题

**装了补丁但游戏里还是英文**
Ren'Py 优先加载 `.rpyc`。检查 `game/tl/schinese/` 里有没有残留的旧 `.rpyc`，`install.py` 会自动清理，但手动拷贝时容易漏。

**中文显示成方块**
`font_shadow` 漏了某个字体文件名。用 `install.py --font <路径>` 手动指定一款字体确认一下是不是字体问题。

**启动就崩，报 `A translation for "X" already exists`**
译文库里同一个英文原文出现了两次，`check.py` 会拦；如果是手动合并的补丁，检查一下是不是从多个来源合并时重复了。

**游戏把 `config.language` 重置成 `None`**
有些游戏在 `init -1600 python hide:` 里重置语言。`<shim>` 里的赋值必须放在**普通的** `init python:` 块里，优先级比它高、后执行。
