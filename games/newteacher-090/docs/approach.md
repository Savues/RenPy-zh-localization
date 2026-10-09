# 方案说明 —— That New Teacher 0.9.0

## 这个补丁落在哪里

```
patch/game/tl/chinese/**.rpy   →   <游戏>/game/tl/chinese/**.rpy
patch/zz_zh_locale.rpy         →   <游戏>/game/zz_zh_locale.rpy
```

文件路径是原样落地的，**不多一层**。Ren'Py 对多一层的补丁是**静默忽略**的：
不报错、不提示，只是那份补丁从来没被加载过。这个仓库曾经真的发出去过一版
包级 bug，就是因为这个。

## 为什么是 `script-override`，不是 `tl-blocks`

两个方案在仓库里都成立，选哪个取决于补丁是怎么做出来的，不是哪个更正统。

`tl-blocks` 的前提是 `data/tl_trans.json` 是**构建输入**——译文从字典生成，
`check.py` 拿字典和英文原文逐条比对，未译就报错。这个游戏的译文不是生成出来的：

- 195 条英文原句在补丁里**合法地有多个译法**。同一句短台词，不同角色在不同场景
  说出来就是不一样——`Huh, what's this?` 一处是「嗯，这是什么？」，另一处是
  「咦，这是什么？」。这不是错译，是这一版刻意保留的区分。
- 字典是 `{英文: 中文}`，一个英文只能存一个中文。要把它建成字典，就得丢掉那 195 条里
  的 194 条，然后 `check.py` 拿去打分的就只剩下**它自己挑的那一份**，而不是玩家
  真正读到的那一份。那是补丁自己给自己判卷。

所以这里没有译文库。改用 `script-override`，`check.py` 直接检查补丁实际发布的
51 个脚本。**这让术语检查更严，不是更松**：那 195 条的每一个译法都会被扫到禁用变体，
字典方案只能扫到一个。

代价是 `game.json` 的 `coverage` 变成**断言**——工具不会重算它。所以
`tools/verify_patch.cjs` 每次都从补丁里把三个数字重新数一遍，对不上就失败。

## 为什么需要自带安装器

`tools/install.py` 装不了这个游戏，三条原因：

1. 它要求 `game.json` 声明字体资源，没有就直接 `die`。这个补丁不带字体——
   游戏自带的 CJK 字体本来就够用，带一份只会多出体积和一份授权要交代。
2. 它靠游戏目录下**散落的 `options.rpy`** 判断「这是不是一个游戏目录」。这个游戏的
   89 个英文脚本全在 `archive.rpa` 里，`options.rpy` 并不散落，一装就报
   「no options.rpy -- is this really the game directory?」。
3. 它会 `shutil.rmtree` 整个 `game/tl/<lang>` 再复制。这个补丁发布的 51 个文件
   虽然覆盖了整棵树，但如果哪天少带一个，整目录被删掉之后那个文件就没了。

`tools/install.ps1` 因此逐文件覆盖，并且额外做一件 `install.py` 不做的事：
**把每个被写文件的 `.rpyc` 先备份再删掉**。下一节解释为什么这步不能省。

## 那个 `.rpyc` 是这个补丁唯一会静默失败的地方

下载包里 `game/tl/chinese/` 下每个 `.rpy` 旁边都配了一个编译好的 `.rpyc`。
**Ren'Py 优先加载字节码。**

把中文 `.rpy` 盖上去、旧 `.rpyc` 留着，游戏会照旧跑发行方的文本，
**全程没有任何报错**：没有异常、没有 traceback、语言也确实是「中文」，
只是内容没变。这种失败玩家根本看不出哪里出了问题。

`install.py` 其实有 `clear_compiled()` 处理这件事，但如上所述这个游戏走不到那里，
所以 `install.ps1` 里重做了一遍。手动复制文件夹的玩家请自己确认
`game/tl/chinese/` 下没有残留的 `.rpyc`。

## 语言代码用 `chinese` 而不是 `schinese`

游戏自带的中文就叫 `chinese`（`game/tl/chinese/`，
`fullLanguageList["chinese"] = ["中文", ...]`）。这个补丁修订的是那棵树，
不是新增一种语言。

Ren'Py 的翻译目录是按语言代码取的。如果补丁写成 `game/tl/schinese/`，
结果是两份中文并存：语言菜单里选「中文」还是发行方那一份，修订过的文本躺在旁边
永远不被加载——而且两个 `old` 键相同的话还会直接崩。

所以 `game.json` 的 `language` 必须是 `chinese`，`install.ps1` 启动时会核对，
不是就报错退出。

## `.rpyc` 影子文件在这里不需要

City Devil 那个补丁要额外写一堆空的 `.rpyc` 影子（见那个游戏的
`docs/approach.md`），因为它的脚本**全部**封在 `archive.rpa` 里，松散的
`.rpy` 盖不住归档里的 `.rpyc`。

这个游戏不一样：`game/tl/chinese/` 本来就是散落的，直接覆盖即可，
只要把旧的 `.rpyc` 删掉。`archive_shadowed` 因此是空的。

## shim 只做一件事

```renpy
init python:
    config.language = "chinese"
```

放在普通的 `init python:` 块里是必须的：这个游戏没有在 `init -1600` 之类的地方
重置语言，但把 shim 放在任何更早的 init 都会让游戏自己的初始化跑在它后面。

shim 刻意**不去改** `fullLanguageList` 里 `chinese` 的机翻标记。
那属于发行方的界面，也属于本补丁修订的基线文本；标记还成立，就不该动。
