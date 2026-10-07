# 翻译档案 — Scions of the Divine 0.1

全部 5,094 条译文人工逐条撰写，**未使用任何机器翻译、在线翻译 API 或离线翻译模型**。

## 术语决策

完整术语表在 [`glossary.json`](glossary.json)，这里是决策本身。

### 角色名

英文 key 取自游戏自己的 `define <var> = Character("...")`（`scripts/systems/definitions.rpy`），
中文取自 `CHARACTER_DATA` 的显示名，所以每一条都能对回源码。

| 英文 | 中文 | 备注 |
|---|---|---|
| Sarah | 莎拉 | 主角的母亲 |
| Layla | 莱拉 | 酒吧老板娘 |
| Astara | 阿斯塔拉 | 神裔 |
| Christine | 克里斯汀 | 神裔 |
| Rayne | 雷恩 | 神裔 |
| Veronica | 维罗妮卡 | 调查员 |
| Melany | 梅拉妮 | 妮可的母亲 |
| Silas | 塞拉斯 | 塞拉斯的姓与"塞拉斯"同源，全篇统一 |
| King Nasos | 纳索斯国王 | 称号不译 |
| Queen Annis | 安妮丝女王 | 称号不译 |

主角 `mc` 的显示名是 `[mc_name]`——玩家自己输入。默认名 **弗林**（Flynn），
只在 `misc.json` 的输入提示里出现一次，所以是提示文案而不是台词。

### 世界观名词

| 英文 | 中文 | 决定 |
|---|---|---|
| Scion | 神裔 | 不译"神子"。"神子"在中文里指神的儿子，与设定里"被神力选中的凡人"不是一回事 |
| deity / god | 神明 | 统一用一个词。"神"单用会和"神裔""神力"混 |
| Divine Power | 神力 | |
| Primordial One | 原初者 | 不是"太初"/"元初"——后者在中文里偏褒义 |
| Sentinel | 守望者 | 三种颜色（Sentinel 有 sentl/sentm/ssent 三个变量）共用同一个词，靠颜色区分 |
| The Last God | 最后的真神 | |
| Reshmun | 雷什蒙 | 地名，音译 |
| Vextross | 韦克斯特罗斯 | 姓氏，音译 |
| BFC | 残暴格斗锦标赛 | 缩写首次出现处展开 |
| Sector | 区块 | 不是"扇区"，后者是计算机术语 |
| realm | 领域 | 不是"境界" |

### 数值单位

角色档案里的身高体重原作是英制（`5'7"` / `130 lbs`）。改成 **厘米 / 公斤**
（`170 cm` / `61 kg`），整表统一，不混用。理由是中文玩家对英制没有 直觉，
而档案页是数值比较页面，单位必须一眼可比。

## 短句的语境化处理

`data/tl_trans.json` 合并时能看出：115 个英文句子在补丁里有不止一种中文译法。
全部是短感叹语，**不是不一致，是有意按上下文分的**：

| 英文 | 出现的几种中文 |
|---|---|
| `Yeah.` | 对。（×12）/ 嗯。（×3）/ 好。/ 认识。 |
| `No.` | 不。/ 没有。/ 不是。/ 不行。/ 才不是。/ 不对。 |
| `Sure.` | 随时。/ 有。/ 当然。 |
| `Why not?` | 为什么？/ 为什么不？/ 为什么不行？/ 有什么不行呢？ |

`Yeah.` 译成"认识。"的那一处，上一句是自我介绍，答的是"你认识我？"，跟答"嗯"不是
一回事。这类地方正是逐句翻译和查表机译的分界线。

代价是 `data/tl_trans.json` 装不下全部：它是一张扁平的 `en -> zh` 表，
4,630 条去重条目里有 115 个 key 只能保留第一次出现的那个译法，184 个译法因此
不在表里。该文件对 `script-override` 方案本来就不是构建输入，`check.py` 不读它，
但改补丁时要知道它是有损的，别拿它当权威。

## 修过的问题

早期用批量字符串替换回写译文，撞出了一批结构性问题，全部已修并验证。

### 引号被吃掉（17 处，`screen_preferences.rpy`）

`text "..."` 变成了裸的 `text ...`，Ren'Py 报 `NameError: name 'xxx' is not defined`。
17 处全部补回引号。

### 机器参数被翻译（14 处）

- `screen_preferences.rpy` 7 处：`Preference("文字速度")` → `Preference("text speed")`
- `screen_controls.rpy`：`SetScreenVariable("device", ...)` 的参数
- `screen_save.rpy`：`FileTime` 的 format 与空位置参数对调
- `screen_save.rpy`：`{#auto_page}` 字形被吞、`FilePageLabel("auto")` 被改

这些都不会报错，只是功能坏掉，属于最难发现的一类。`tools/verify_patch.cjs`
第一项现在把 `profile_filters` / `STAT_COLORS` 的机器值钉死了。

### 标签串位（5 处）

同一行上有多个带引号的字符串，替换时抓错了那一个：

| 被当成标签抓走的 | 实际标签 | 结果 |
|---|---|---|
| `"Controls"` | `"viewport"` | 键位表跳错屏 |
| `"History"` | `"vpgrid"` | 同上 |
| `"Close"` | `"game_menu"` | |
| `"Preferences"` | `"viewport"` | |
| `"Unseen Text"` | `"pref_wordbutton"` | |

### 属性块结尾多一个冒号

`text "好感度:"` 这种把结构冒号一起吃掉的写法，在角色档案的好感度/中立/善良/
邪恶四行和回忆录的筛选行。修的时候自己又手滑写出一个双冒号 `text "筛选："::`，
一并修掉了。

### 台词错位与误译

| 位置 | 问题 | 改后 |
|---|---|---|
| `0_1.rpy` L31 | `你想听那个故事都听到每晚了`（语序塌了） | `你每晚都想听那个故事` |
| `0_1.rpy` L1255 | `I'll take what I can get` 直译 | `那我就却之不恭了` |
| `0_1.rpy` L1962 | `Sounds good to me` | `听着不错` |
| `0_1.rpy` L2840 | brunette 误译成"金发妞" | `她把那个棕发的家伙狠狠揍了一顿` |
| `0_1.rpy` L3132 | `I think so...` 语气不对 | `我想是的……` |
| `0_1.rpy` L6660/6661 | 相邻两行错位，独白被并进上一句，下一句只剩 `（算了。）` | 两行各自还原 |
| `classes.rpy` | `.get(key, "Unknown")` 的默认值被翻 | 改回英文 |
| `classes.rpy` | 档案占位符 `placeholder` 被当英文翻 | `（暂无内容）` |

### 字形：▸

MiSans 换成主字体之后，快进指示的三角箭头 `▸`（U+25B8）画不出来——
两个 MiSans 字重都没有这个码位。原作的 `style skip_triangle` 本来就指定
`DejaVuSans.ttf`，换字体时被一起改掉了。已改回，理由写进
[`approach.md`](approach.md) 和 `tools/verify_patch.cjs` 的 `FONT_EXCEPTIONS`。

## 已知未译

**开发者菜单（`screen_dev.rpy`）只翻了一半。** 12 个标签、36 处仍是英文：
`Jump`、`Variables`、`Profiles`、`All`、`Unlock`、`Lock`、`Everything`、
`Outfit`、`Profile`、`Memory`、`Affection: `、`Utilities`。

同一文件里 `开发菜单`、`章节选择`、`变量项`、`全部档案`、`全部服装`、`全部回忆`、
`善恶值`、`紧急更新` 已经是中文，所以这是**翻到一半停了**，不是"整个菜单不翻"的
统一决定。`game.json` 的 `coverage` 已经把这 36 处扣掉
（5058 / 5094），`verify_patch.cjs` 会挡住中间状态。

**启动画面是图片。** 标题 `Scions of the Divine` 和内容警告（Content Warning）
在原作里是预渲染图片，换字体不影响。补丁里这两处仍是英文，不是遗漏。