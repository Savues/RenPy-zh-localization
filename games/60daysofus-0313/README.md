# 60 Days Of Us 3.1.3 (EarlyAccess) —— 简体中文补丁

原作：60 Days Of Us ｜ 引擎：Ren'Py 8.5.4 ｜ 补丁版本：v1

## 这个补丁是什么

**它是发行方自带中文的修订版，不是从零翻译。**

下载包的中文**打包在 `game/archive.rpa` 里**，路径 `tl/Chinese/`，共 12 个文件
（树头标着 `Translation updated at 2026-09-18`）。这个补丁把那棵树原路顶回去，
16,922 行有效文本里改了 **1,376 行**，分布在 12 个文件中的 9 个——
每一行都是玩家会读到的文本，没有一行是结构改动。

改动分三轮：先查错、对术语，再逐个角色调语气，最后通篇润色到「念出来像人话」。
逐条记录在 [`docs/translation-log.md`](docs/translation-log.md)。

## 安装

**先关掉游戏。** 然后：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "D:\Games\60DaysOfUs-Build3.1.3(EarlyAccess)-pc"
```

还原：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\uninstall.ps1 "D:\Games\60DaysOfUs-Build3.1.3(EarlyAccess)-pc"
```

装完直接启动即可，不用去语言菜单里选。第一次启动会重新编译脚本，会卡一会儿且无输出。

安装器会先把整个 `archive.rpa`（2.5 GB）复制一份到 `game/.zh_patch_backup/`
再动任何东西。只想撤销的话，把那份备份盖回 `archive.rpa`、删掉 `game/tl` 即可，
文件长度会精确回到原始的 2,550,180,180 字节。

## 装之前一定要知道的一件事

**这个补丁不能靠手动复制文件夹来装。** 别的游戏都是复制文件，只有这一个不行。

原因在 `archive.rpa`：游戏自带的那份中文就在归档里。Ren'Py 收集翻译时，
磁盘上的文件和归档里的条目**各收一遍，互不覆盖**。你把 `game/tl/Chinese/*.rpy`
盖上去，不是替换，而是多了一份——每一对 `translate Chinese strings:` 的
`old`/`new` 都被注册两次，于是启动时直接抛异常：

```
Exception: A translation for "Take my sister with you." already exists
```

玩家连主菜单都进不去，而且**报的是 traceback、不是「翻译冲突」**，很难自己查。
散落的 `foo.rpy` 也不会遮住归档里的 `foo.rpy`，两个都会被读。

所以安装器要先做一次 **RPA-3 索引手术**：把归档索引里那 24 条 `tl/Chinese/*`
（12 个 `.rpy` 加各自的 `.rpyc`）摘掉，再把重建的索引追加到文件末尾并改掉
34 字节的文件头。**归档里每一条存活的条目都保持原偏移，2.5 GB 的图和音频一个字节没动**，
整个操作只追加约 84 KB。

手术需要 `zlib` 和 Python 的 `pickle`，PowerShell 没法安全地往返二进制 pickle。
本仓库对每个游戏的承诺都是「玩家不用自己装 Python」，所以这里借用**游戏自己带的**
`lib/py3-windows-x86_64/python.exe`（本版本实测为 Python 3.12.7，自带 zlib 与 pickle）。
找不到这个解释器时安装器会停下报错，而不是猜一个。

## 这个补丁修掉的真问题

以下都是发行方原文里实际存在的问题，`tools/verify_patch.cjs` 与
`docs/glossary.json` 会持续盯着它们不再回来：

| 位置 | 问题 | 处理 |
|---|---|---|
| `script.rpy` 军衔（12 处） | 机翻把 `Sergeant` 一律压成「军士长」。但游戏**自己的名字框**写着 `old "SSG.Turner"` → 特纳上士、`old "CSM Graves"` → 格雷夫斯一级军士长，英文自我介绍也是 `Staff Sergeant Joseph Turner.` 屏幕上的名字框与念出来的军衔自相矛盾 | 按游戏自身数据定：泛称 `Sergeant` / `Sarge.` = 中士，`Staff Sergeant` / `SSG` = 上士，`Sergeant Major`（称呼 Graves）= 一级军士长 |
| `script.rpy:42757` 及邻近 | `e8 "Talk 1/2" nointeract` 的正文被机翻**整条吞成空串**（俄语版是正常的） | 补回 `对话 1/2` / `对话 2/2` |
| `Define.rpy:107` | 名字框是 `克雷格`，四句台词却是 `克莱格`。而 `克雷格` 与 `格雷格`（Greg）只差一字 | 统一为 `克莱格` |
| 全库 39 处 | 城市名 `Los Suenos` 译成 `洛圣都`。但游戏原句是 `This is Los Suenos. The city of dreams.`，`Sueños` 是「梦」，同一句里「梦想之城」和「洛圣都」自相矛盾；全库 39 处没有一处英文是 `Los Santos` | 改回 `洛斯苏埃诺斯` |
| `script.rpy` 代号 | 行动代号 `Greyhound` 译成「灰犬」 | 改为 `灵缇` |
| `script.rpy` 平行对白 | 同一句英文在全库有 33 组中文各不相同，最大的两组是同一段新闻广播在游戏里出现两次（2292–2309 与 4512–4529） | 33 组降到 10 组，剩下的都是跨场景、不同对象、语气差异的合理变体 |

还有一批 A 级硬伤：漏译（`#1216` 英文三句中文丢两句）、历史补丁回归把
`But this is worse.` / `It's true.` 吞掉、`Yeah, I do.` 助动词当实义词、
`'round here`（这一带）同音误听成「这年头」、`Last flight` 在直升机上下文里译成「飞机」等。
完整清单见 [`docs/translation-log.md`](docs/translation-log.md)。

## 刻意**不**统一的三处

看着像不一致，其实在英文里就是两回事，合并才是错的：

- **`zombies` 丧尸 / `infected` 感染者**——威尔开场按大众说法叫「丧尸」
  （`Zombies. You've seen them in movies before, right?`），知道之后改用准确的
  「感染者」（`Visual confirmed... infected.`）。剧本里有一句
  `Technically, they're zombies, not vampires.` 就是游戏自己在区分这两个词。
- **`vampires` 吸血鬼**——共 2 处，指的是吸血鬼，不是感染者。
- **`squad` 班 / `team` 小队**——`script.rpy:1537` 的英文是 `Irene's team`，是「小队」不是「班」。

## 版权

游戏本体版权归发行方所有。游戏自带的简体中文版权归发行方所有，本补丁在它的基础上修订。
补丁不附带任何字体：游戏自己的 `th_font_map["Chinese"]` 指向它自带的思源宋体 CJK，
直接用即可。

技术说明见 [`docs/approach.md`](docs/approach.md)，术语对照在
[`docs/glossary.json`](docs/glossary.json)。
