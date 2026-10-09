# 翻译日志 —— Between Humanity 0.3.3

## 译文来源

这一份汉化是**对发行方自带中文的修订**，不是从英文重译。

基线是下载包里 `game/tl/chinese/` 的那 8,940 个 translate 块。关于它的来源，游戏里有
两处自述，本补丁如实记录，两处都不改：

| 出处 | 原文 |
|---|---|
| `scripts/screens/languageSelection.rpy` | 有些语言是部分或全部使用AI翻译的，所以可能不完美。……如果你想帮助改进翻译，你可以在本地或我们的Discord上找到文件。 |
| `CUSTOMS.rpy` 头部 | `languages["chinese"] = {"translation_state": TranslationState.HUMAN_100, "version": "1.1"}` |
| `scripts/core/screens/about.rpy` | 0.3.1 版本加入了许多新语言，虽然大部分都是机翻。……特别是 Fa1con Eye、Shark7、予澈和 LayKoZ！ |

两句话并不矛盾：**部分**语言是机翻，中文这一份被发行方自己标为 `HUMAN_100`。
本补丁做的是修订，所以语言菜单里那句提示原样留着，shim 也不去动它。

## 覆盖

| 口径 | 数量 |
|---|---|
| translate 块 | 8,940 |
| 玩家可见字符串（对白 + UI 串） | 9,926 |
| 已本地化 | **9,920（99.94%）** |
| ├─ 含汉字 | 9,847 |
| └─ 只改了标点 | 73 |
| 有意保留原文 | 6 |

保留原文的 6 条全是 Ren'Py 手机文本的插值：`[_text]`、`[_text2]`、`[_gt!t]`、
`[random_whisper]`、`[_naomiText._text!i]{w=3}{nw}`、`[lilithShort]-{w=1.5}{nw}`。
句子是运行时拼出来的，这些串里根本没有英文，逐条登记在
`docs/glossary.json` 的 `_kept_verbatim`。

## 改动的规模

| 口径 | 数字 |
|---|---|
| 文件 | 134 个里改了 105 个 |
| 活动行 | 21,108 行里改了 4,208 行（19.9%） |

改动最重的几个文件：

| 文件 | 改动 / 总行 |
|---|---|
| `chapters/02/ch_02_21-Tuesday-Stripclub.rpy` | 200 / 757 |
| `chapters/03/ch_03_04-Swimming.rpy` | 190 / 1,181 |
| `chapters/03/ch_03_09-AnyasPlan.rpy` | 174 / 942 |
| `chapters/03/ch_03_10-GrandmasHome.rpy` | 160 / 707 |
| `chapters/01/ch_01_16.rpy` | 152 / 535 |

## 顺手修掉的三个真问题

这三条都在发行方原文里，属于「译文根本没生效」而不是「译得不好」，所以单独记。

### 1. `old "Acqu机翻ntance"` —— 机翻把字打进了英文原句

`scripts/functions/enums.rpy` 的第一个 `translate chinese strings:` 块里有一条：

```
    # game/scripts/functions/enums.rpy:32
    old "Acqu机翻ntance"
    new "熟人"
```

`old` 必须是游戏里的英文原文，Ren'Py 靠它逐字匹配。这条键里混进了「机翻」两个字，
**永远匹配不上**，所以这条译文是死的。

要紧的是**不能顺手把它改对**：同一文件往下 160 行还有一条正确的
`old "Acquaintance"`。改对之后两条键一模一样，
`TranslationStringRegistry.add()` 会抛
`A translation for "Acquaintance" already exists`，**游戏启动即崩**。

所以处理是**删掉死的那条**，正确的 `Acquaintance → 熟人` 留着。
`tools/verify_patch.cjs` 现在有一条守卫：`old` 键里出现汉字就失败——
这类脏键不可能匹配英文，而它最可能被下一个人「修好」成一颗启动炸弹。

### 2. 同名的 `translate chinese python:` 块遮住了字体注册

```
CUSTOMS.rpy                     style.rpy
translate chinese python:       translate chinese python:
    #gui.text_font = ...            gui.text_font = "tl/chinese/font/JiYingHuiPianHeYuan.ttf"
    pass                            gui.name_text_font = ...（共 9 行）
```

两个块同名。Ren'Py 的翻译块按名字登记，后加载的覆盖先加载的——**而加载顺序取决于
文件顺序，不是取决于哪个块有用**。如果 `CUSTOMS.rpy` 排在 `style.rpy` 后面，
注册中文字体的那 9 行就被一个 `pass` 顶掉，全篇中文变方块。

`CUSTOMS.rpy` 那个块整个是注释加 `pass`，没有任何内容，删掉它没有代价。
本补丁删的正是它，不是改顺序——顺序依赖不是能靠约定稳住的东西。

### 3. 同一句英文的两处中文不一致

`chapters/01/ch_01_24.rpy` 的 `:177` 和 `:416` 是同一句英文：

```
n "You feel [amber.ColoredName] now using both hands... and spit?"
```

Ren'Py 的 translate id 是从英文字符串哈希出来的，同一句必然同一个 id。
两处中文却写得不一样：

| 行 | 原文 |
|---|---|
| 217 | 你感觉到[amber.ColoredName]**现在双管齐下**……并吐了口唾沫？ |
| 571 | 你感觉到[amber.ColoredName]**开始用上了双手**……并且吐了口唾沫？ |

同一个 id 只能登一条，玩家**永远只看得到后注册的那份**，
也就是 `:571` 的「开始用上了双手」。`"using both hands"` 对「用上了双手」，
比「双管齐下」忠实，所以本补丁把 `:217` 统一成同一句，让文件自身一致——
这样无论加载顺序如何，玩家读到的都是这一句。

剩下 10 处同 id 的重复是**无害**的：翻译导出器同时读了 `foo.rpy` 和 `foo.rpyc`，
把同一段导出了两遍，两份文字逐字相同，玩家看到哪份都一样。
verifier 仍然数它们，但只对**文字不一致**的那种报错。

## 译法统一

- 角色名（见 `docs/glossary.json`）：帕克夫人 / 泰勒老师 / 露西 / 安雅 / 克莱尔 /
  西蒙 / 莉莉丝 / 内奥米 / 马库斯 / 里奥。
- 口吃标记按角色分开：帕克夫人 `帕-帕克夫人`、西蒙 `西-蒙`、莉莉丝 `莉莉丝-`。
  原文里 Lilith 的口吃有一处被机翻成拉丁 `Lili-`，本补丁统一回 `莉莉丝-`，
  免得口吃变成英文。
- 身高体重保留英制原值并补公制：`1.75m (5'9")` → `1.75米（5'9"）`。
- `Doctor` / `Doc` / `doctor` 三种写法统一译「医生」。

## 没改的，和为什么

- **语言菜单里那句机翻提示。** 它对发行方原文成立，而本补丁是修订不是重译。
- **`HUMAN_100` 标记。** 同上，那是发行方对自己这份译文的标注。
- **`CUSTOMS.rpy` 里注释掉的 `translationUpdates` 标签。** 发行方留给翻译者的钩子，
  里面是注释，删了没有意义。
