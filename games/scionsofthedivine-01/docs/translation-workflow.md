# 汉化流程存档 — Scions of the Divine 0.1

这一份记录的是**怎么做**的：引擎的坑、提取和回写脚本的设计、以及那些校验器
为什么长成那样。做了什么决定看 [`translation-log.md`](translation-log.md)，
为什么走脚本覆盖看 [`approach.md`](approach.md)。

## 起点：脚本在 archive.rpa 里

发行包的 `game/` 根目录只有：

```
archive.rpa            1.1 GB，3360 个条目，全部脚本和素材都在里面
presplash_background.png
presplash_foreground.png
script_version.txt
cache/  fonts/  saves/  shaders/  tl/
```

磁盘上**没有一个松散的 `.rpy`**。`tools/template.py` 和 `tools/build_tl.py` 在这种
结构下没有输入可用，所以这条路一开始就不成立——但还是得先把脚本从归档里取出来
才知道这一点。

取出用的是自己写的 `rpyc_tool`：读 `archive.rpa` 尾部的索引 pickle，按名字取出
`.rpy` 条目写到本地。1.1 GB 的归档只按索引取需要的那 46 个 `.rpy`，不解包全部。

取出后逐个和 `extract_rpyc.py` 从 `.rpyc` 反编译的结果对照，确认取到的确实是
**源码**而不是字节码——归档里两样都有（`shaders/*.rpy` 和 `shaders/*.rpyc` 同时
在索引里），拿错了后面每一步都白做。

## 提取：什么算「玩家看得见的文本」

脚本覆盖方案没有翻译模板，所以**所有可译字符串都要自己找出来**。第一版提取器
只认 say 语句，漏掉了一大批：主菜单与设置界面、章节/日期选择、回忆录的场景列表、
`CHARACTER_DATA` 里的档案字段、`define <x> = Character("名字")`。
后期手工补了约 100 处。

最后落到 5,094 条，按文件分批：

| 批次 | 文件 | 条数 |
|---|---|---|
| 主剧情 | `scripts/game/v0.1/0_1.rpy` | 4,166 |
| 回忆录 | `scripts/game/universal/memories.rpy` | 279 |
| 通用对话 | `layl.rpy` / `primordial.rpy` / `sara.rpy` / `rayn.rpy` | 377 |
| 界面 / 菜单 / 档案 / 角色表 | 18 个 `screens/` 与 `systems/` 文件 | 260 |
| 其他（输入提示、名字表、库文件头） | — | 12 |

**提取阶段就定死了覆盖率的口径**，因为事后没人能再从成品脚本里反推出来：每个
say 语句、每个 `text` / `textbutton` / `label` / `caption` / `title` 的参数、
每个菜单选项、每个 `Character(...)` 名字、每个界面字符串，各算一条。这个数字
最后写进 `game.json` 的 `coverage`。

明确**不算**的：docstring、dict 键、`Preference("...")` 这类机器参数、素材路径、
色值、f-string 格式模板。这些改错了不会显示错字，只会静默失灵——那是另一类
问题，靠 `verify_patch.cjs` 查，不靠覆盖率查。

## 回写：绝不用列号定位

第一次回写按「文件 + 行号 + 列号」定位字面量。翻车了：中文普遍比英文短，
同一行前面某个字面量一旦变短，后面的全部左移。实际后果是
`text "..."` 的引号被吃掉、`Preference("文字速度")` 这种机器参数被一起翻掉、
同一行多个带引号的字符串抓错了那一个。

改成**以字符串内容对齐**：提取时记下 `file + line + src`（整行原文），回写时按
`src` 反查该行里第几个字面量，再按序号写回。内容对不上就报错停下，不猜。

之后所有批量修复脚本都是同一套约定，并且每次改完都跑一遍字面量配对检查：

```
EN 字面量个数 == ZH 字面量个数（且按顺序逐个对应）
```

**例外要单独说明。** 换成 MiSans 时删掉了几个字体路径字面量
（`font "fonts/IMMORTAL.ttf"` 变成 `font zh_display_font`），所以 9 个文件的
字面量总数对不上。检查脚本改成：把 EN 侧**确实在 ZH 侧找不到对应项**的字体字面量
剔掉，再配对。这样"字体替换导致的减少"不会掩盖"引号被吃掉导致的减少"——
后者才是 bug。配对结果：27 个文件、7,307 个带拉丁字母的字面量、全部对齐。

## 校验：三层

### 第一层 — 通用：`tools/check.py`

跑 `python tools/check.py --game scionsofthedivine-01`。对 `script-override`
方案它不读译文库，查的是实际发出去的 29 个 `.rpy`：乱码、汉字之间的重复空格、
术语冲突（`glossary.json` 的 `banned`）、叠字、标签闭合、shim 与字体是否在位。

### 第二层 — 本游戏：`tools/verify_patch.cjs`

挂在 `game.json` 的 `extra_checks` 上，`check.py` 每次都会跑。四项：

1. **机器值不许被翻** —— `profile_filters` 的十项、`STAT_COLORS` 的键和值，
   外加"`zh_ui.rpy` 仍然映得到每一个筛选值"这条反向检查。
2. **相邻重复的中文字面量** —— 防按列号回写造成的 index 错位。
3. **字形覆盖** —— 解析 `MiSans-Regular.ttf` 的 cmap，把 29 个 `.rpy` 里
   58,444 个非 ASCII 码位逐个对一遍，MiSans 画不出的直接报错。
   显式豁免只有一条（`▸` 由 `DejaVuSans.ttf` 渲染），附原因。
4. **开发者菜单的完整性** —— 12 个标签要么全英文要么全翻完，中间状态报错。
   判定只认**显示位置**（语句关键字后面紧跟的那个字面量）：这一屏里
   `default dev_char_list = ["All"]` 和各角色 `tags` 是机器值，必须留在英文。
   早先那版用 `text.includes('"All"')` 判断，会把机器值误报成"没翻完"，
   改成按显示位置匹配后才真正有效——两个方向都自测过：现状 0 个未译，
   把任意一个标签改回英文立刻报出来。

第 3 项是自己写 cmap 解析器（格式 4 和 12）的原因：仓库里没有字体库依赖，
而"字体换了但某个符号画不出来"是换字体时最容易漏、且**只在运行时才看得见**的一类
问题。29 个文件跑完不到 1 秒，值得自带一个 60 行的解析器。

### 第三层 — 实机

启动游戏看 `log.txt` 无 traceback，主菜单/设置/档案/回忆录/制作人员逐屏确认，
再进正文确认对白渲染正常。

## 换字体的顺序

MiSans 是最后一步换上去的，因为它会动到 `init -999` 里的字体变量和所有
`font "..."` 字面量，混在翻译中间改不好定位。顺序是：

1. 翻译全部文本
2. 结构校验（字面量配对、机器参数、引号）
3. 实机跑通
4. 换字体（本步）
5. **字形覆盖检查**（第 3 项就是为这一步写的）
6. 再实机跑一遍主菜单和快进指示

第 4 步唯一改了字面量数量的地方就是 `font "xxx.ttf"` → `font zh_*_font`，
这也是字面量配对检查里那个"例外"的确切来源。

## 打包进仓库时改了什么

**翻译内容一个字没改。** 打包只做了三件事：

- 把 27 个改动过的 `.rpy` 复制到 `patch/game/` 下相同的相对路径，
  加 `zh_ui.rpy`（共 28 个），未改动的 17 个 `.rpy`（含 3 个 shader 和 5 个
  原本就是 0 字节的占位文件）不打包——它们在 `archive.rpa` 里，不需要动
- `zh_font.rpy` 放到 `patch/` 根上当 `shim`，两个 MiSans 放进 `assets/fonts/`
- 新写 `game.json`、安装器/卸载器、`verify_patch.cjs` 和这几份文档

打包过程中改过补丁的只有两处，都是 bug 修复：`screen_skip.rpy` 的 `▸`
（见 [`translation-log.md`](translation-log.md)）和 `verify_patch.cjs` 自身。