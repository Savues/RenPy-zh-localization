# 为什么 Scions of the Divine 不用 translate 补丁

仓库里有两种打补丁的方式。Eden Chapter 5 和 Sinful Summer 3.6 用 Ren'Py 的
`translate` 块，Cosy Cafe 和 TOXICity 用脚本覆盖。两条都是仓库认的方案，
`game.json` 的 `patch_layout` 声明用哪条——选这条的原因是硬约束，不是偏好。

## translate 路线的前提

`tools/build_tl.py` 的输入是 `games/<slug>/tl_template/`——一份**英文原文**、且已经
包在 `translate <lang> ...:` 块里的脚本。`tools/template.py` 负责从
`<游戏目录>/game/tl/<lang>/` 把这份模板拷进来。

本作发行包的 `game/tl/` 里**只有 `None/common.rpym`**——那是 Ren'Py 自己写出来的
运行时文件，不是翻译模板。没有任何 `game/tl/schinese/`，也没有 `renpy/common`
的字符串导出。开发者根本没做多语言结构。没有模板，`build_tl.py` 直接 `sys.exit`。

## 即使能生成，也装不进去

块 ID 不是随便起的。`renpy/translation/__init__.py` 的 `create_translate()`：

```python
for i in block:
    code = i.get_code()
    md5.update((code + "\r\n").encode("utf-8"))
digest = md5.hexdigest()[:8]
identifier = self.unique_identifier(self.label, digest)
```

`ast.Say.get_code()` 把 `who`、`encode_say_string(what)` 和 `with` 等尾巴用单空格
拼起来。也就是说 **块 ID 是英文原句的哈希**——中文语句永远算不出能和游戏对上号的
ID，必须拿英文原文去算。这条路对得上，但对上没有模板就无从谈起。

安装侧还有第二道墙：`tools/install.py` 的全部动作只有三样——
`game/tl/<lang>/`、`game/<shim>.rpy`、`game/fonts/*`。**它没有覆盖游戏脚本的能力。**
本作的 5,094 条译文分布在游戏自己的 27 个 `.rpy` 里，只能整体替换。

## 实际采用的方案

用中文版 `.rpy` 整体替换游戏脚本，配 `zh_font.rpy` 做字体注册、`zh_ui.rpy` 做
界面内部值的显示时映射。

**archive.rpa 一个字节都没改。** Ren'Py 加载脚本时，磁盘上的
`game/<path>.rpy` 优先于 `archive.rpa` 里的同名条目，所以把中文脚本放进
`game/scripts/` 就顶掉了归档里的英文原稿。1.1 GB 的 `archive.rpa` 保持原样，
卸载时把这 28 个文件删掉就回到原版——不需要动那个大文件，也不需要重新打包。

这也是这个安装器和 Cosy Cafe 那份的一个实质差别：本作发行时**磁盘上没有任何
松散的 `.rpy`**（27 个脚本全在归档里），所以安装器写的每一个文件都是"新文件"
而不是"覆盖"。`Backup-Once` 因此一条备份都不会写，卸载时全部按"补丁引入的文件"
删掉。`uninstall.ps1` 读 `manifest.json` 的 `files` 列表逐条判断——有备份就还原，
没有就删除——而不是遍历备份目录，因为遍历备份目录会漏掉全部 28 个。

## 覆盖率为什么只能断言

`data/tl_trans.json` 是从最终 `.rpy` **反向**导出的：它是成品脚本的副产品，
不是构建输入。拿它算覆盖率，等于让补丁给自己判卷——它会忠实地把脚本里的任何
错误一并记进去，然后报告一个漂亮的 100%。

所以覆盖率写在 `game.json` 的 `coverage` 里，**是断言不是推导**：

```json
"coverage": { "translated": 5094, "total": 5094 }
```

数字来自提取阶段对英文原文的统计：27 个替换脚本里每一条 say 语句、
`text` / `textbutton` / `label` / `caption` / `title` 的参数、每一个菜单选项、
每一个 `Character(...)` 名字和界面字符串，共 5,094 条。`check.py` 只负责把它
打印出来，不会重算，也不会因为对不上而报错。

**这条断言刚开始是对不上的。** 第一次写 `game.json` 时实测只有 5,058 条有中文，
差的 36 处全在开发者菜单（`screen_dev.rpy`）—— 那块界面是分两批做的，第一批翻了
标题和分组名（`开发菜单` / `章节选择` / `全部档案` / `善恶值` / `紧急更新` …），
第二批漏了 12 个动作标签（`Jump` / `Unlock` / `Lock` / `Outfit` …）。

这类补丁的结构性弱点就在这里：通用检查器对 `script-override` 方案**不读**
`data/tl_trans.json`，也就没有任何一处拿英文原文跟成品脚本逐条比对，
所以"开发者菜单只翻了一半"这种状态，在 `check.py` 眼里完全正常。是打包时那句
"coverage 只能断言"逼着人把英文原文重新数了一遍，才数出来的。
`tools/verify_patch.cjs` 里为此加了一条：12 个标签要么全是英文，要么全都不是，
中间状态直接报错；补完之后这条检查也顺手改了写法——只认**显示位置**的英文，
因为 `default dev_char_list = ["All"]` 这种机器值留在文件里是应该的，
早先那版用 `includes('"All"')` 会把它误判成没翻。

## 字体：为什么是 fallback 而不是 shadow

原作自带三款拉丁字体，全在 `archive.rpa` 里：`fonts/IMMORTAL.ttf`（标题/按钮）、
`fonts/PlaypenSans-VariableFont_wght.ttf`（正文手写体）、`fonts/rune.ttf`（符文）。
三款**一个汉字字形都没有**。

`shadow` 策略（覆盖同名文件）在这里技术上可行——松散文件优先于归档——但会让
卸载无法逐字节还原：游戏原本的字体被 MiSans 覆盖之后，备份目录里存的是 MiSans，
不是原作那三款。玩家卸完补丁拿到的是一款被换过的字体，不属于自己的游戏。

所以走 `fallback`：`patch/zh_font.rpy` 在 `init -999` 里把三个字体变量全部指向
`fonts/MiSans-Regular.ttf`，并用 `config.font_replacement_map` 把粗体请求映射到
真实的 `MiSans-Bold.ttf`。调用点（`gui.rpy` 的 `text_font` / `name_text_font`、
7 处 `font zh_display_font`、`prim` 的 `what_font`）自动继承，一处都不用改。
MiSans 走的是**全码位接管**，不是 FontGroup 兜底：拉丁字母和数字也由 MiSans 画，
全游戏观感统一。

### 一个必须显式豁免的字

快进指示的三角箭头 `▸`（U+25B8）**MiSans 两个字重都没有**。原作的
`style skip_triangle` 本来就特意指定 `DejaVuSans.ttf`，源码注释写得很清楚：
"We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE glyph
in it."。改 MiSans 时那一行被一起改成了 `font zh_text_font`，箭头就画不出来了。

这是全补丁**唯一**一处不是 MiSans 的字体，已登记在
`tools/verify_patch.cjs` 的 `FONT_EXCEPTIONS` 里，附渲染字体和原因。
`verify_patch.cjs` 的第三项检查（字形覆盖）会扫全部 29 个 `.rpy` 的 58,444 个
非 ASCII 码位，任何 MiSans 画不出的字直接报错——这一项当初就是抓着这个 bug 写的。

## 已知的坑

### 一个字面量都不要用列号定位

回写译文时按「文件 + 行号 + 列号」定位字面量是错的：中文普遍比英文短，同一行
前面某个字面量一旦变短，后面的全部左移，再跑一次就错位。本作的替换全程以
**字符串内容**对齐，`verify_patch.cjs` 的第二项检查（相邻重复的中文字面量）
就是防这个——自然中文枚举不会在同一行相邻重复两次。

### 界面内部值不能翻

`profile_filters` 是 `(显示用中文, 引擎用的英文)` 的二元组列表，
`STAT_COLORS` 的键是 `affection` / `karma`，`Preference("text speed")`、
`SetVariable("sort_profile", "A-Z")` 的参数、`get_memory_description()` 的返回值，
全是引擎拿来比对的机器值。翻掉任何一个的表现都是**静默失灵**：筛选菜单点了没反应、
好感度条不画，而且 `errors.txt` 里什么都没有。

`patch/game/zh_ui.rpy` 就是为此存在的：`filter_label()` / `memory_tag_zh()` /
`confirm_zh()` 在**显示时**把内部值映射成中文，内部值一个字不动。
`verify_patch.cjs` 的第一项检查把这些机器值钉死。

### 别忘了 Ren'Py 自己的确认对话框

`Are you sure you want to quit?` 这类提示是引擎在运行时生成的，脚本里根本没有，
翻译脚本碰不到。`confirm_zh()` 映射了本作用到的 9 条。

### 启动画面是图片

标题 `Scions of the Divine` 和内容警告（Content Warning）在原作里是预渲染图片
（`splashname` / `splashcw`），换字体不会影响它们。补丁里这两处仍然是英文，
这不是遗漏。