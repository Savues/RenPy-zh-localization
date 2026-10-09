# Between Humanity 0.3.3 —— 简体中文补丁

原作：Between Humanity ｜ 引擎：Ren'Py 8.3.7 ｜ 补丁版本：v1

## 这个补丁是什么

**它是发行方自带中文的修订版，不是从零翻译。**

下载包里本来就有一份简体中文，在 `game/tl/chinese/`（8,940 个 translate 块）。
这个补丁把那棵树原路顶回去、改掉其中 105 个文件，其余 29 个文件与下载包逐字节相同，
一并随包发布是为了让整棵树保持完整。改动规模是 21,108 行里的 **4,208 行（19.9%）**。

关于这份中文的来源，游戏自己有两处说法，本补丁如实记录、都不改：

- `game/scripts/screens/languageSelection.rpy`：「有些语言是部分或全部使用AI翻译的，
  所以可能不完美。请在游玩时记住这一点。如果你想帮助改进翻译，你可以在本地或我们的
  Discord上找到文件。」
- `CUSTOMS.rpy` 头部把 `languages["chinese"]` 标为 `TranslationState.HUMAN_100`；
  致谢页点名了贡献者。

两句话都没错：一部分语言是机翻，中文这一份被发行方自己标为 100% 人工。
这个补丁做的是**修订**，不是重译，所以 shim 不去动语言菜单里那句提示。

## 安装

关掉游戏，解压，把 `game/` 文件夹里的**全部内容**复制到游戏的 `game/` 里，选择覆盖。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "D:\Games\Between-Humanity-0.3.3-pc"
```

还原：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\uninstall.ps1 "D:\Games\Between-Humanity-0.3.3-pc"
```

装完直接启动即可，不需要去语言菜单里选。第一次启动会重新编译脚本，会卡一会儿且无输出。

## 装之前要知道的一件事

**一定要先删掉旧的 `.rpyc`。** Ren'Py 优先加载编译好的字节码；把中文 `.rpy` 盖上去
却留着原来的 `.rpyc`，游戏会照旧跑发行方的文本，而且**不报任何错**。安装器已经替你
删了；手动复制文件夹的话请自己确认 `game/tl/chinese/` 下没有残留的 `.rpyc`。

## 这个补丁修掉的三个真问题

都是发行方原文里的，本补丁顺手修掉，`tools/verify_patch.cjs` 会持续盯着它们不再回来：

| 位置 | 问题 | 处理 |
|---|---|---|
| `scripts/functions/enums.rpy` | `old "Acqu机翻ntance"` —— 机翻把「机翻」两个字打进了英文原句中间，这条永远匹配不上 | **删掉**这条死条目。注意不能「修好」它：同文件 160 行外已有正确的 `old "Acquaintance"`，修好就是两条同键，启动即崩 |
| `CUSTOMS.rpy` | 第二个 `translate chinese python:` 块，全是注释加 `pass`，却和 `style.rpy` 里注册中文字体的那个块同名 | 删掉。它一旦排在后面，全篇中文会变成方块 |
| `chapters/01/ch_01_24.rpy` | 同一句英文在 `:177` 和 `:416` 各出现一次，Ren'Py 哈希成同一个 id，两处中文却不同 | 统一成忠实于 "now using both hands" 的那个写法 |

细节见 [`docs/translation-log.md`](docs/translation-log.md)，技术说明见
[`docs/approach.md`](docs/approach.md)，术语对照在 [`docs/glossary.json`](docs/glossary.json)。

## 版权

游戏本体版权归发行方所有。游戏自带的简体中文版权归发行方所有，本补丁在它的基础上修订。
补丁不附带任何字体：`game/tl/chinese/font/` 里的字体游戏本来就带着，直接用。
