# 方案说明

## translate 路线的三个前提，0.12.0b 一个都不满足

1. **要有 `game/tl/<lang>/` 模板。** 发布包里只有
   `game/tl/None/common.rpym` —— 一个占位符。`build_tl.py` 没有输入可编译。
2. **模板必须由源码生成。** 翻译是在解析期套用的，而补丁要替换的正是解析期之前
   就存在的脚本本身。没有源，就没有能生成模板的东西。
3. **共享安装器只认语言树。** `install.py` 会放 `game/tl/`、shim 和字体，
   不会去覆盖游戏自己的 `.rpy`。

所以走脚本覆盖：`patch/game/` 里放替换后的脚本，装进游戏的 `game/`。

## 为什么不打包 5 个没改过的文件

`Bust_Char.rpy`、`images.rpy`、`myscreens.rpy`、`PhoneTexting.rpy`、
`replay_scenes.rpy` 一开始被打进了补丁，因为提取器在它们里面找到了字符串。
但逐字比对 SHA-256 之后发现，它们和 0.12.0b 原版**逐字节相同** ——
七条字符串全是资源名、样式前缀、颜色值。

结果之一是仓库通用的 `check.py` 在 `Bust_Char.rpy` 上报了
「unbalanced `[i]` tags」：这行根本不是标签，是 Python 下标

```renpy
idle "LIinfo/" + LI + "_char_bio" + str(busts[LI][i]) + ".png"
                              ^^^^^^
```

`check.py` 的标签配对是整文件文本计数，看不见字符串和代码的区别。诚实的修法是
不要发布没改过的文件，而不是去改一个为另外六个游戏服务的检查规则。
删掉之后 `check.py` 自然就绿了。

## 为什么 MOD 必须在游戏自带的 Python 3.9 下重建

Shawn's Mod 在任何分发里都只有 `.rpyc`：官网下载和游戏目录里都是 6 个文件，
一份源码都没有。`translate schinese` 对它无效 —— `.rpyc` 已经是编译后的 AST，
翻译早就套过了，没有东西可翻。

于是 `tools/mod_translate.py` 反过来做：解开 `.rpyc` 的 slot 1 和 slot 2，
就地改 AST 里的字符串，再重新 pickle。麻烦就出在 pickle 上。

`renpy/object.py` 用 Python 写了自己的 `__getstate__` / `__setstate__`。
Python 3.11 起，`object.__getstate__` 默认返回 `(instance_dict, slot_dict)` 二元组，
3.9 不认。在 3.12 上重新 pickle 出来的文件，3.9 读不了 ——
而且是**静默失败**：`renpy/script.py` 把加载包在 `except Exception: pass` 里，
最后只报一句 `Could not load file ...rpyc`。所以重写必须在将来读它的那个解释器上做。

### 为什么分发译文而不是 .rpyc

MOD 的构建在漂移：为 0.6.9a 发布的拷贝和这个补丁开发时对照的拷贝不是同一份字节
（`Shawn_Cheats.rpyc` 一个 3,044 一个 3,186）。提交我们那份二进制，
等于只对其中一种构建有效。所以仓库里放的是
[`data/mod_zh.json`](../data/mod_zh.json)（1,273 条）加一个重建工具，
对着玩家实际拥有的那份 MOD 现场重建。仓库里 7 个游戏一个 `.rpyc` 都没提交。

### meeting_1_m 为什么不翻

MOD 里 `meeting_1_m` 那 1,028 句是作者为 0.6.9a 写的 Day 1 替代线。
它的挂载点 `label meeting_1` 在 0.12 里被整条删除了，游戏里 97% 的地方不存在
这条线。翻它等于翻一段不可达的文字。

## 攻略工具为什么自己抽数据

MOD 自带的 9 个攻略屏骨架围绕 0.6.9a 的变量写的：0.12 里有 **217 个声明变量，
其中 111 个是死的** —— 全部 `event_*`、`*_office`、`*_text`、
`loyalty_*`、`pregnancy_chance_*`，以及所有 `*_power`。
直接挂上去就是 `NameError`。

所以攻略点是从 0.12 源码里抽的，只有真正活着的变量算数：
`day`、`goodness` / `corruption`、`cash`、`fear`、
六个角色的 `love_*` / `corruption_*`、四个阵营声望，以及 `nickname_*1` 隐藏昵称。

`love_*` 和 `corruption_*` 确实在门控内容，可以举证：

```
day1_update.rpy:1149   "Grope."     if (love_sophia > 50)
day1_update.rpy:1214   "Grinding."  if (love_sophia > 51 and corruption_sophia > 0)
day1_update.rpy:1210   if love_sophia < 52:      <- 整个选项被门控
day1_update.rpy:1324   if corruption_sophia < 2: <- 黑化路线专属
```

界面挂进 MOD 现成的 `modmenu`（这个屏在 0.12 上是好的）。Ren'Py 解析同名屏幕时
先比 init 优先级，再比文件名，所以那两个屏用 `init 999`（MOD 的 `modmenu` 是
`init 0`、`quick_menu` 是 `init 969`）加 `zz_` 文件名。1000 以上也能赢，
但会让 lint 报优先级越界。

## 屏幕探针能证明什么，不能证明什么

`tools/verify_screens_probe.rpy` 挂在 `config.overlay_screens` 上，
在真实交互期逐个调 `ScreenDisplayable.update()`。这能证明「这个屏能被构造出来」，
修完 6 个 `NameError` 之后 18 屏全 OK。

它**不能**证明文字排版对不对、键盘能不能操作。那部分只能靠实机。

## 已知的坑

### 覆盖确认框改不动

`gui.ARE_YOU_SURE` 这类字符串在 `init -1149` 覆盖没有效果。全引擎没有任何地方
读 `gui` 上的这六个值；真正传给屏幕的是 `00action_file.rpy:408` 的
`layout.OVERWRITE_SAVE`，而 `layout` 是 `00layout.rpy:41` 建的
`Layout()` 实例 —— 和 `gui` 不是同一个命名空间。
要修就把那六个字符串再覆盖一次 `layout.*`。
同一个 `init -1149` 也可以挪到 `init -999`（引擎是 -1150，这些串只在运行时被读），
消掉唯一一条自有 lint 警告。

### 屏幕探针不覆盖模态屏

探针走的是 `update()`，能发现构造期异常，发现不了「打开之后排版错位」这类问题。
MOD 原版的 `modmenu` 排版错误就是这样漏过去的。
