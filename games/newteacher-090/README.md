# That New Teacher 0.9.0 —— 简体中文补丁

原作：RogueOne ｜ 引擎：Ren'Py 8.3.7 ｜ 补丁版本：v1

## 这个补丁是什么

**它是发行方自带中文的修订版，不是从零翻译。**

下载包里本来就有一份简体中文，在 `game/tl/chinese/`（19,402 个 translate 块）。
这个补丁把那棵树原路顶回去、改掉其中 43 个文件，剩下 8 个文件与下载包逐字节相同，
一并随包发布是为了让整棵树保持完整。改动的规模是 43,108 行里的 **13,372 行（31.0%）**。

游戏自己的语言菜单会给中文标一个机器人图标，写着「标有机器人图标的语言为机器翻译」。
**本补丁不去掉那个标记**：它改的是机翻的译文，不是重译，标记依然属实。

如果你要的是一份全新的中文翻译，这个包不是；你要的是把机翻改到能看，它就是。

## 安装

关掉游戏，解压，把 `game/` 文件夹里的**全部内容**复制到游戏的 `game/` 里，
选择覆盖。不用装 Python，不用跑脚本，不用联网。

命令行安装器（会先备份，出错可回滚）：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "D:\Games\That_New_Teacher"
```

还原：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\uninstall.ps1 "D:\Games\That_New_Teacher"
```

装完直接启动游戏即可——不需要去语言菜单里选，中文已经是默认。
第一次启动会重新编译脚本，会卡一会儿且没有任何输出，这是正常的。

## 装之前要知道的两件事

1. **一定要先删掉旧的 `.rpyc`。** Ren'Py 优先加载编译好的字节码；把中文 `.rpy` 盖上去
   却留着原来的 `.rpyc`，游戏会照旧跑发行方的文本，而且**不报任何错**。安装器已经
   替你删了；手动复制文件夹的话请自己确认 `game/tl/chinese/` 下没有残留的 `.rpyc`。
2. **游戏必须已经打过一次补丁以外的原始状态。** 这个包是「顶掉发行方的中文」，
   不是「再加一种语言」。在已经装过别的汉化补丁的目录上装，会得到两份注册同名
   `old` 键的翻译，启动即崩。

## 改了什么

见 [`docs/translation-log.md`](docs/translation-log.md)。其中影响最大的一条：

发行方把两位女主 **Sophia 和 Suzie 都译成了「苏西」**，玩家在正文里分不出这两个人。
本补丁把 Sophia 定为 **索菲娅**、Suzie 保留 **苏西**，连带改掉 35 处硬编码和 3 处
「苏茜」。`tools/verify_patch.cjs` 每次运行都会数这两个名字的次数，
任何一个归零就失败。

术语对照表在 [`docs/glossary.json`](docs/glossary.json)，技术说明在
[`docs/approach.md`](docs/approach.md)。

## 版权

游戏本体、美术与音频版权归 RogueOne 所有。游戏自带的机翻中文版权归发行方所有，
本补丁在它的基础上修订。补丁不附带任何字体：游戏自带的 CJK 字体本来就够用。
