# 这个游戏怎么打补丁（以及为什么它的模板是造出来的）

`docs/adding-a-game.md` 里的两条路线，Clown Squad 两条都不完全适用。这份文档记录
它实际是怎么做的，以及每一步为什么必须那样做。

## 1. 发行包里没有英文模板，只有一套已经翻好的社区中文

`archive.rpa` 里带着 `tl/schinese/`（外加 `tl/russian/`），而且 `tl/schinese/` 里
**已经是中文**：

```
translate schinese story01en_cab3a47c:

    # mc "(Y'know what the difference is between ordinary people and heroes?)"
    mc "（你知道普通人和英雄之间有什么区别吗？）"
```

它不是模板，是**随游戏一起发行的社区翻译**。`tools/template.py` 看到中文会直接报错退出
（那条保护是为了防止把打过补丁的游戏当成模板导进来），所以标准流程走不通。

## 2. 英文原文还在，只是搬到了注释里

Ren'Py 的语言工具在它生成的每一个块上方都留了一行**翻译前的原始语句**。把上面那行
`mc "（…）"` 换回注释里的 `mc "(…)"`，代码骨架、块 id、说话人、属性全都不动——这正好
就是 `tools/build_tl.py` 需要的东西。

`tools/make_template.py` 干的就是这件事：

```bash
python games/clownsquad/tools/make_template.py "<游戏目录>"
python tools/build_tl.py --game clownsquad
```

配对时比对的不是行号，是**字符串前面那段文字**（说话人 / 关键字）。注释和语句的
前缀必须一致，否则拒绝替换。这样一条注释不可能被配到相邻块的语句上。

```
script.rpy      12577 lines   lines still holding CJK: 0   empty-say blocks dropped: 3
story01en.rpy   19872 lines   lines still holding CJK: 0   empty-say blocks dropped: 0
```

模板是 gitignore 的（`games/*/tl_template/`），和仓库里其他游戏一样不进版本库。

### 三处必须手写的地方

**a. `NVL_SPLITS`：一句英文被拆成两条语句**

Ren'Py 把一句多句的 `nvl` 台词按句拆开，但注释里仍然只有一句原文。这种块整个游戏
只有两个，都写在 `NVL_SPLITS` 里：

| 块 | 英文 | 中文 |
|---|---|---|
| `story01_2_d1e81074` | `You either pass the exam, ` + `or you don't.` | `要么通过考试，` + `要么通不过。` |
| `story01_3_d1e05bc7` | `Rude.` + `But fair.` | `话说得难听。` + `不过倒也没错。` |

不拆的话，玩家会读到「你要么通过考试，要么没有。**要么通不过。**」——同一句话说两遍。

**b. `drop_empty_says`：三个整块就是一句空台词**

`cafe_0ae9bcd0`、`two_sisters_0ae9bcd0`、`two_sisters_0ae9bcd0_1` 的块体只有一个
`""`。它们没有任何玩家可见的文字，而译文库里不能有空值——空翻译正是没干完的活藏身的
地方——所以它们不进模板。反正是一句空台词，少一句没有代价。

**c. `MODE_NAMED`：一行里有两个字符串字面量**

```python
L "Getting ready." with CropMove(time=0.1, mode='slideleft')
```

`tools/tlparse.py` 会把 `'slideleft'` 也当成一条待译条目，而 `tools/build_tl.py` 是把
替换写回**已经被上一处改短了的那一行**，第二处的偏移就过期了，构建产物会多出一个
`slideleft` 标识符粘在句尾。

`tools/` 不能改，所以修法得落在模板上：把那个模式值改成一个常量名，一行就只剩一个
字面量，而 transform 行为分毫不差。

```python
init python:
    ZH_SLIDELEFT = "slideleft"

    # ...
    L "准备。" with CropMove(time=0.1, mode=ZH_SLIDELEFT)
```

**值不能直接删掉。** 听起来「`slideleft` 大概是默认值吧」很合理，但它不是。对着这个
游戏自带的引擎查一下就知道：

```
renpy.display.transition.CropMove.__init__
  params   ['self', 'time', 'mode', 'startcrop', 'startpos', 'endcrop',
            'endpos', 'topnew', 'old_widget', 'new_widget']
  defaults ('slideright', (0.0, 0.0, 0.0, 1.0), (0.0, 0.0), (0.0, 0.0, 1.0, 1.0),
            (0.0, 0.0), True, None, None)
```

默认值是 **`'slideright'`**。省掉这个参数会把过场动画从向左滑变成向右滑——这种错误
不会报错，lint 也不会报，只有玩到那一场才发现。

## 3. 补丁靠「同名文件盖住归档」生效

Ren'Py 对同一个原文字符串只允许注册一次翻译。本游戏在 `archive.rpa` 里已经注册了一整套
`schinese`，补丁再放一份会直接抛：

```
A translation for "..." already exists
```

所以：

- **对白**：`patch/tl/schinese/story01en.rpy` 和 `script.rpy` 与归档里的文件**同名**。
  松散文件盖住归档里的同路径文件，Ren'Py 只加载一份，不存在第二次注册。
- **界面残留**：归档里那些没有同名文件可盖的（选项、菜单、制作人员等），在
  `zz_zh_locale.rpy` 的 `init 999 python:` 里直接改写已经建好的翻译表。
  **必须用 `dict.update()`**：`translations` 的 `add()` 遇到已存在的键会抛同一个错。

## 4. 译文库以英文原文为 key，所以一句英文只能有一个译法

`data/tl_trans.json` 是 `build_tl.py` 的输入，它按英文原文查表。同一句英文在游戏里
出现 100 次，就只能有一个中文。Clown Squad 里 34 句短叹词原本是分场景译的，逐条看过
上下文之后统一了，理由逐条写在 [`translation-log.md`](translation-log.md)。

这是本仓库路线和「逐块差异化译法」之间的取舍：Ren'Py 本身其实**能**表达一句英文在不同
块里译得不同（社区那套就是这么做的），但 `build_tl.py` 表达不了。想恢复逐块差异，只能
直接改 `patch/tl/schinese/*.rpy`，那样补丁就不再能从 `data/tl_trans.json` 重建了。

## 5. 字体走 `font_name_map` 回退

游戏自己的正文字体 `DejaVuSans.ttf`、`font/Bear Days.ttf` 都是纯拉丁的，盖文件没有意义。
`zz_zh_locale.rpy` 把每个字体名注册成 `FontGroup`：游戏原字体画拉丁文，
`zh_cjk_ranges` 里的码位交给 MiSans。

归档里自带的社区翻译还有一段 `translate schinese python:`（`tl/schinese/base/style.rpy`）
会把 `gui.text_font` 指向 `tl/schinese/fonts/` 里的字体。它在 init 的哪一步执行不该拿来
赌字体，所以那几个名字也一并注册了——不管哪一套胜出，中文都走 MiSans。

`zh_cjk_ranges` 不是「大概的 CJK 范围」，是量出来的：`data/tl_trans.json` 里 2042 个
不同的非 ASCII 码位，正好落在这些区间内，两个字重的 MiSans 都 100% 覆盖。
设置界面写死的 `font/NotoSansSC-Black.ttf` 本来就有完整中文覆盖，故意的没有动它。

## 校验

```bash
python games/clownsquad/tools/make_template.py "<干净的游戏目录>"
python tools/build_tl.py --game clownsquad     # applied 5408 / 5408，退出码 0
python tools/check.py    --game clownsquad     # all checks passed
python tools/selftest.py --game clownsquad     # 101 / 101 条守卫都会报错
```

游戏侧另外跑一次 Ren'Py 自带 lint，`tl/schinese` 的问题数必须是 0。

