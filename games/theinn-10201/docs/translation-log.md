# The Inn 1.02.01-2 — 翻译档案

原作：theinn ｜ 引擎：Ren'Py 8.5.0 ｜ 语言：`simplified_chinese`

## 方案

`tl-blocks`。游戏的脚本全在 `.rpa` 里，翻译走 Ren'Py 官方机制，
`patch/tl/simplified_chinese/` 直接落进游戏的 `game/tl/simplified_chinese/`，
不顶掉任何原版文件。

## 规模

| | |
|---|---|
| 翻译条目 | 5,421 条（唯一英文原文） |
| 原文引用 | 5,718 处（界面 1,761 + 对白 3,957） |
| 补丁文件 | 89 个 `.rpy`，29,994 行（另有 1 个 shim） |
| 覆盖率 | 100%（11 条保留原文，登记在 `glossary.json` 的 `_kept_verbatim`） |
| 角色名 | 表在术语表里，但**尚未接进游戏**，见下 |

保留原文的 11 条，五条是插值骨架（`$: {:,}`、`[gametime.weekday_name!t] / {:02d}:{:02d}`、
`{}`、`{}-{}!`、`{}{}!`）——周围的词翻了，里面的 `{:02d}` 不是词。两个字体名
（`DejaVu Sans`、`Opendyslexic`）是字体选择器里的族名，改了别的工具就认不出。
`I`、`V`、`{#auto_page}A`、`{#quick_page}Q` 是存档信息界面的按键提示，翻译字母
等于什么都没告诉玩家。

## 英文原注释是补回去的，不是本来就有的

这份补丁是按源文件分目录批量生成的，生成时**每条对白上面的英文注释都被剥掉了**。
没有那行注释，一个 `.rpy` 就只是「一堆没有原文的中文」，任何工具都无法把它和
英文对上——`pack.py` 跑出来是 4,001 行对白全部 unpaired。

英文从 `theinn_work/dialogue.json` 找回：那份文件按 `translate` 块 id 存了每块
的原始文件名与行号以及英文台词。补回去的校验：

- 3,957 个对白块，**全部**在 `dialogue.json` 里按 id 命中，0 缺失；
- 3,957 块的说话人与英文那一行的说话人**全部一致**，0 不符；
- 重建只插入不删除——88 个文件的每一行原样按序保留，净增 3,957 行注释。

现在是标准 Ren'Py 形态：

```
# game/navigation/linda_house/interactables_labels.rpy:9
translate simplified_chinese lm_kitchen_basket_9ca452ef:
    # lm "What're you lookin' at?"
    lm "你在看什么呢？"
```

## 角色名还没接进游戏

**这一条要写清楚：游戏里对白上方的姓名牌现在还是英文。**

姓名是以变量的形式送到屏幕的——`theinn_work/char_map.json` 里 `lm` 对应
`"[linda.name]"`、`gy` 对应 `"[gyna.name]"`、`kuro` 对应 `"[lu_cat.name]"`——
而游戏自己的英文 `tl/None` 里没有任何单名条目可供翻译。补丁里自然也没有一行
带 `Linda` 或 `Valentina`。

所以现在的状态是：**选人界面是中文**（那些标签在 `ui/characters/*.rpy`，已经翻了），
**对白里的姓名牌是英文**。

`docs/glossary.json` 的 `characters` 表给出的是接上去时要用的写法，附
`_names_are_not_translated` 说明为什么它现在还只是词表。真正接上去要做的是改写
姓名变量，不是翻字符串——相当于 Por(n)tals 用 shim 重映射 `Character()` 的做法。
这一版没有做：它会改变游戏的运行行为，而这台机器上做不了目视验证
（`README_zh.md` 记了同一个限制：窗口捕获拿不到 OpenGL 画面）。

## 收尾时补的漏译与超宽

| 位置 | 英文原文 | 错成 / 问题 | 改成 |
|---|---|---|---|
| `ui/wwd/wwd_displayable.rpy` | `{#wwd}GOOD` | 未译（旁边的 `HITS` 译了） | `{#wwd}好` |
| `ui/wwd/wwd_displayable.rpy` | `{#wwd}MISS!` | 只把 `!` 换成了全角 | `{#wwd}失误！` |
| `ui/special_screens/load_metadata.rpy` | `{#cw}Superbad` | 未译（旁边八部电影都译了） | `{#cw}超级坏蛋` |
| `ui/special_screens/load_metadata.rpy` | `{#cw}This Means\nWar` | 未译 | `{#cw}开战` |
| `1_01_01/...` | `¡Señorita Linda!` | 未译 | `¡Señorita Linda！——琳达小姐！` |

存档槽的电影标题一共十条，**只有这两条**漏了——`遇见\n斯巴达人`、`妈妈\n咪呀！`、
`终结者2：\n审判日`、`第一滴血`、`够爱你\n一万年`、`绝地战警\n2`、
`史密斯\n夫妇`、`银河护卫队\n2` 都在。四条超宽：

| 英文原文 | 改前 | 改后 |
|---|---|---|
| `lm "Mi casa és su casa!"` | 42 列 | 36 列 |
| `mar "Señorita Linda? Are you comin'?"` | 63 列 | 61 列 |
| `maralt "¡Señorita Linda!"` | 未译，补注后 40 列 | 29 列 |

这一款有个特殊人物 **Mário**：他通篇夹西班牙语，每句都在句尾用 `{i}(中文){/i}`
补一句解释。补注本身就要占宽度，所以他的台词普遍比原文长——`¿Qué?` 译成
`¿Qué?\n\n{i}(什么？){/i}`。宽度检查盯的就是这种行：补注要留，但一行塞不下就得收，
收到原文两倍以内为止。`¡Señorita Linda!` 为了塞下补注，从 `\n\n{i}(...){/i}`
的整句式换成了与相邻 `Mi casa` 那行一致的破折号式。

## 一个必须写下来的坑：不要重跑 build_tl.py

`data/tl_trans.json` 是按英文原文做 key 的**扁平字典**。本作有 **61 条**英文原文
按上下文该有两种译法——`What?` 回陌生人的话是「什么？」，被质问「你这话什么意思」
时是「什么话？」；`Sure!` 热情附和是「好啊！」，随口应一声是「好！」。扁平字典
只能存一种。重跑 `tools/build_tl.py` 会把它们全部塌缩成最后见到的那一种，实测
**190 行**正文被改掉，另有 10 行只差空格。

所以本目录的 `patch/tl/simplified_chinese/` 是**成品**，不是 `build_tl.py` 的产物，
**不要重跑**。要改哪句就直接改 `patch/tl/simplified_chinese/`，改完跑
`python tools/check.py --game theinn-10201`。

`build_tl.py` 在这一款上一定返回 1，报 `still untranslated: 40`。那 40 条全是
`zzz_fonts.rpy` 里 `translate simplified_chinese python:` 块的引号内容——游戏那 39 个
西文字体名加上中文字体路径，没有英文原文、也不是对白，词库故意不收。`build_tl`
遇到查不到的条目会跳过、把这行原样留着，而那行本来就是成品表。

## 语言必须钉死，有两个原因

游戏没有可用的语言选择入口，`config.enable_language_autodetect` 也是关的。
`zz_zh_locale.rpy` 里两段代码各解决一个问题：

1. **`config.default_language` 不够。** `_apply_default_preferences()`（init 1500）
   只在玩家**第一次运行**时把 `default_language` 写进 `_preferences.language`。
   已经玩过的存档里早就记成 `english` 了，单独写 `default_language` 对老存档无效。
   所以 init 1999 直接写 `_preferences.language`。
2. **启动画面会把语言改回英文。** `label _start` 在 `_init_language()` 之后还会走
   启动画面，`game/game_splashscreen.rpy:9` 调 `auto_lang()`，它内部执行
   `renpy.change_language("english")`，把刚设好的中文覆盖回去——1,761 条中文界面
   文本全部退回英文，字体映射同时被清掉。init 2999 给 `renpy.change_language`
   包一层，把这个回退请求改写回简体中文。

## 字体为什么不能挪出 tl 目录

`zzz_fonts.rpy` 用 `renpy.config.font_name_map` 把游戏用到的 **39 个**字体名全部
指向同一个中文字体。它必须留在 `tl/simplified_chinese/` 里、必须留在
`translate <lang> python:` 块里——**`renpy.change_language()` 会清空
`config.font_name_map`**，从普通 `init` 块装上的映射在语言切换那一刻就被抹掉了。
`translate` 块每次加载语言都会重新执行，正好是这里需要的语义。

字体名清单是审出来的，不是猜的：第一版漏了 `fonts/computer_pixel-7.ttf` 和
`fonts/SawarabiMincho-Regular.ttf`，补上之后 36 → 39 全覆盖。

字体是 Noto Sans SC 的**改动版**：`fvar` 表里 `wght` 轴的默认值由 100 改成 400，
其余一个字节没动，`fvar`/`gvar` 仍在，所以整条字重轴照常可用——只是不给轴坐标
时默认落在 Regular 400，而这 39 个字体名最后全都是这种情况。上游没有声明
Reserved Font Name，OFL 1.1 第 3 条因此不要求改名。详见
`assets/fonts/LICENSE-NotoSansSC.txt`。

## 工具上的一处改动：_tag_exempt

`check.py` 一直检查 `[i]` 这类标签在补丁文件里是否配对。这一款过不了，因为游戏
自己的英文就是：

```
old "Calibrating [name] ([i]/[total])"
```

这里的 `[i]` 是计数器变量，不是斜体标签。Ren'Py 把它当成斜体开头、找不到
`[/i]`、报一次警告。译文去不掉：Ren'Py 按 `old` 行**逐字**匹配 `strings:` 块，
`old` 必须是游戏自己的原文，`new` 也必须代入同一个变量。留着 `[i]` 反而正是
计数器能正常显示的原因。

照 `_doubling_exempt` 的体例加了 `_tag_exempt`，登记**逐行**豁免而不是整文件——
`selftest.py` 会往补丁里最大的那个文件追加一行 `[i]probe` 并要求守卫仍然报错，
整文件豁免会把探针一起吞掉，那样这道守卫就再也没被测到。

