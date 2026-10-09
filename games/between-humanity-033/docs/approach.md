# 方案说明 —— Between Humanity 0.3.3

## 文件落在哪里

```
patch/game/tl/chinese/**.rpy   →   <游戏>/game/tl/chinese/**.rpy
patch/zz_zh_locale.rpy         →   <游戏>/game/zz_zh_locale.rpy
```

路径原样落地，**不多一层**。Ren'Py 对多一层的补丁是静默忽略的：不报错、不提示，
只是那份补丁从来没被加载过。

## 为什么是 `script-override`

和 `newteacher-090` 同一个理由：译文树是手工维护的，不是从字典生成的。

`tl-blocks` 的前提是 `data/tl_trans.json` 是**构建输入**，`check.py` 拿它和英文逐条
比对。这里没有构建输入——树是人一条条改出来的，拿一个反向推出来的字典去打分，
等于补丁自己给自己判卷。所以不建译文库，直接检查补丁实际发布的 134 个脚本，
覆盖率由 `game.json` 的 `coverage` 断言，并由 `tools/verify_patch.cjs` 每次重算。

## 为什么需要自带安装器

`tools/install.py` 装不了：它要求 `game.json` 声明字体资源（这个补丁不带字体，
游戏自带 `tl/chinese/font/`），又靠散落的 `game/options.rpy` 判断游戏目录
（这个游戏的脚本全在 `scripts.rpa` 里），还会把整个 `game/tl/<lang>` 删掉再复制。

`tools/install.ps1` 逐文件覆盖，并且额外把每个被写文件的 `.rpyc` 先备份再删。
**这一步不能省**：下载包里 `game/tl/chinese/` 下每个 `.rpy` 旁边都有编译好的
`.rpyc`，而 Ren'Py 优先加载字节码。留着它，中文 `.rpy` 永远不会被读，游戏照旧跑
发行方的文本且**全程不报错**。

## 语言代码用 `chinese`

游戏自带的中文就叫 `chinese`（`game/tl/chinese/`）。补丁修订的是那棵树，
不是新增一种语言。写成 `schinese` 的结果是两份中文并存：语言菜单里选「中文」
还是发行方那一份，而修订过的文本躺在旁边永远不被加载。

## 这个游戏特有的三类坑，`verify_patch.cjs` 各查一条

Ren'Py 的翻译注册表对「同名」的处理分两种，行为完全不同，这个补丁里三种都撞上了：

| 机制 | 行为 | 本补丁的守卫 |
|---|---|---|
| `strings:` 块的 `old` 键 | **重复直接抛异常**，游戏启动即崩 | 重复 `old` 键 → 失败 |
| `translate <id>:` 块的 id | 按 (id, language) 建字典，**静默覆盖**，先注册的那条永远看不到 | 同 id 文字不一致 → 失败 |
| `translate python:` 块 | 按块名登记，后加载的顶掉先加载的 | 同名 `python` 块 → 失败 |

三条都不是猜的，是这份译文里真实存在的：

1. `old "Acqu机翻ntance"` 是一条永远匹配不上的死键。**删**掉，不能改对——
   同文件有正确的 `old "Acquaintance"`，改对就撞车、直接崩。守则是：`old` 键含汉字 → 失败。
2. `ch_01_24.rpy` 里同一句英文的两处中文不一致，同 id 只登一条。已统一；
   守则是：同 id 但文字不同 → 失败。
3. `CUSTOMS.rpy` 那个注释加 `pass` 的 `translate chinese python:` 会遮住
   `style.rpy` 里注册中文字体的同名块，一旦加载顺序不利就全篇方块。已删；
   守则是：同名 `python` 块 → 失败。

剩下的 10 处同 id 重复**无害**：翻译导出器同时读了 `.rpy` 和 `.rpyc`，
同一段导出两遍且逐字相同。verifier 数它们但只打印，不报错。

## 134 个文件全部发布

这个补丁只改了 105 个文件，但发布的是全部 134 个。没改的 29 个与下载包逐字节相同，
一并发布是为了让整棵树保持完整——安装器逐文件覆盖，不需要去判断玩家手上原本有什么，
也不会因为少带一个文件就把整棵树搞残。

## shim 只做一件事

```renpy
init python:
    config.language = "chinese"
```

刻意**不去改**语言菜单里那句「有些语言是部分或全部使用AI翻译的」。
那句对发行方原文成立，而本补丁是修订不是重译。
