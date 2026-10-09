# City Devil: Restart 0.4.0 —— 做法

## 为什么是脚本覆盖

`archive.rpa` 里 8,904 个条目，其中顶层有 15 个脚本（每个都同时带 `.rpy` 和
`.rpyc`），`tl/` 下有 17 种语言。零售版 `game/` 里除了 `archive.rpa`、
两张 presplash、`script_version.txt` 和 `cache/build_info.json` 之外什么都没有。

所以游戏本来是**可以**用 translate 块的：发行方自己做官方中文就是这么做的。但那条路
要求玩家把中文塞进 `game/tl/schinese/`，而这个补丁要的是"装上就是中文、不用改语言
设置"，把英文脚本本身换掉更直接，也让校验器能逐行证明"除了译文什么都没动"。

`patch/game/` 一比一镜像 `game/`：8 个文件，没有 `data/tl_trans.json`，因为这里没有
任何东西需要从一个数据库生成 translate 块。

## `.rpyc` 影子文件

安装器最关键的五行。依据都在引擎源码里，不是猜的：

1. `renpy/loader.py:336` 的 `add()` 用一个 `seen` 集合去重，键是**完整文件名**；
   `scandirfiles_callbacks` 里 `scandirfiles_from_filesystem`（:430）先注册，
   `scandirfiles_from_archives`（:445）后注册，所以 `game/` 优先，但只对**同名**生效。
2. `renpy/script.py:273-282` 建脚本清单时按后缀分流：archive 里的 `.rpy` 直接
   `continue` 跳过，`.rpyc` 则照收；`:296` 的去重键是 `(stem, dir)`。
3. 于是一个松散的 `game/cdr_1.rpy` 加上归档里的 `cdr_1.rpyc`，产生
   `("cdr_1", "game")` 和 `("cdr_1", None)` 两条，两个不同的键，都会被加载。
4. `load_appropriate_file`（`script.py:838`）在 `dir` 非空时读
   `.rpyc` 末尾 16 字节的 md5；`:889-897` 整段包在 `try/except` 里，
   **空文件读不出 md5，就当作没有**，于是走 `:929` 从 `.rpy` 重新编译。

所以安装器给每个被替换的脚本写一个 0 字节的同名 `.rpyc`。这不是权宜之计，是这一行
游戏唯一正确的做法，`game.json` 的 `archive_shadowed` 把这 8 个文件名钉死，
`verify_patch.cjs` 会检查 `patch/game/` 与该列表是否一致。

## 字体为什么在 init 999

`gui.rpy` 顶部是 `init offset = -2`，它里面的 `gui.*_font` 定义因此在 init -2
执行。想覆盖字体就得比它晚，否则被反向覆盖；但**同样的 init 数值不行**——
`gui.rpy` 自己注册了一个同名的 `@gui.variant`，会顶掉我们那份，两条分支最后都用
拉丁字体，中文渲染成空白。

shim 因此全部放在 `init 999`，并且做两件事：改写 `gui.*_font` 变量，再逐个显式
给默认样式和所有文本样式设 `font`。第二步不能省：`say_dialogue` 这些样式在 gui
初始化时就已经各自持有当时的（拉丁）字体值，只改 `gui` 变量不会追溯更新。

改 `gui.rpy` 本身是另一个选择，但那个文件一个字对白都没有，为了字体去动它不值当，
而且 `_why_unity` 里记着原因。

## 遮蔽骨架

`data/en_masked/<file>.masked` 是英文脚本，每个字符串字面量被换成只记录引号样式的
标记（`@S` / `@Q` / `@T3` / `@T3'`），其余原样。`<file>.flags` 是同样顺序下每个
字面量一个字符的分类：

| 标记 | 含义 |
|---|---|
| `p` | 玩家可见文本，计入覆盖率分母 |
| `a` | 资源路径、图像标签、音频文件 |
| `n` | 引擎 API 的键（`Preference("text speed")` 之类）、裸标识符 |
| `s` | 只有 Ren'Py 替换和标签、没有散文（`[gg]...`、`{cps=5}...{/cps}`、`#rrggbb`） |

骨架里没有一句英文原文，所以仓库不需要附带第二份原作散文就能证明"改的只有译文"。

生成脚本在仓库外（`cdr_zh/mk/mk_en_masked.py`），因为它要读英文原版；产物提交进仓库，
校验只读仓库。`verify_patch.cjs` 里重新实现了一遍同样的 `scan()`，两边必须保持一致，
所以注释里互相点名。

## 三处 structure_exceptions

骨架比对有且只有三行允许不同，`game.json` 里连同英文和中文两边的原文一起写死：

- `options.rpy:126` `preferences.text_cps` 33 → 45。中文一个字约等于两个拉丁字母宽，
  英文的语速让中文还没读完就滚走了。
- `options.rpy:132` `preferences.afm_time` 15 → 12。秒，中文读得比英文快。
- `script.rpy:40` 删掉 `allow=`。这是一个只含拉丁和西里尔字母的白名单，
  `renpy.input` 会用它过滤输入——中文补丁里等于禁止玩家输入中文名字。发行方自己的
  `schinese` 分支（`script.rpy:32`）就没有这个参数。

第三处顺带解释了为什么校验器的覆盖率对位不能按下标做：这一行比原版少一个字面量，
按 `(行号, 位置)` 对位才不会把后面每一行都错开。少几个、对在哪里，是从
`structure_exceptions` 里那条声明的 en/zh 字符串数引号标记数出来的，
所以那个数字没法和它所描述的东西脱节。

## 覆盖率怎么算的

7,792 条玩家可见字面量来自英文原版，7,782 条带汉字（99.87%）。

"带汉字"不是唯一的判据：一个字符串**含汉字**，或者**含中文标点且一个拉丁字母都没有**，
才算已译。这条第二条是必要的——`Start、Guide` 夹着一个中文顿号，
只查汉字会把它算成已译，而它其实是漏译（本补丁已经修掉）。

剩下 10 条登记在 `docs/glossary.json` 的 `_kept_verbatim`：四个网址、一个按键名、
Ren'Py 自己的 `[gui.about!t]` 插值、一个刻意保留拉丁写法的专有名词，
以及游戏自带俄语分支里的两处俄文（只有玩家在语言菜单里选俄语才会走到）。

## 另外 7 个脚本

`archive.rpa` 里一共有 15 个脚本，补丁替换其中 8 个——因为只有这 8 个含玩家可见文本。
剩下 7 个（`gui.rpy`、`parallax.rpy`、`relationships.rpy`、`fight_screens.rpy`、
`freeroam_screens.rpy`、`relupdown.rpy`、`cdr_4.rpy`，共约 3,300 个字面量）同样
提交了英文骨架和分类文件，并被 `verify_patch.cjs` 用**更严**的规则管着：
一个 `p` 都不许有。

这不是多此一举。它把"7,792 就是全部"从一句查过一次的话，变成每次构建都会查的事：
哪天有人把一段对白挪进 `relationships.rpy`，构建会失败，直到有人决定怎么办。

## 不带 `tl/schinese/` 的原因

发行方的官方中文完整地躺在 `archive.rpa` 的 `tl/schinese/` 里，包含 translate 块、
两张字体和整套本地化图片。本补丁**不合并、不转发**它，原因有三：

- 它和本仓库的译文是两份独立的工作，只有一成左右的行重合，合并等于把两份翻译搅在一起；
- 字体不归我们转发（`README.md` 里说了）；
- 放进松散的 `game/tl/schinese/` 没有意义——本补丁的脚本本来就是中文，
  再叠一层只会让 lint 报出几百条重复定义。

