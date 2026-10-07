# 翻译记录

## 总体

| 项 | 数值 |
|---|---|
| 可翻译字面量 | 32,639 |
| 已翻译 | 32,639（100%） |
| 去重后英文 key | 25,828 |
| 批次 | 001–236，每批 150 条 |
| 翻译方式 | 人工逐条撰写，未使用任何机器翻译或在线 API |

## 按文件

| 文件 | 条数 |
|---|---|
| `scripts/story.rpy` | 19,651 |
| `scripts/gallery.rpy` | 3,341 |
| `scripts/story 0.12.rpy` | 2,977 |
| `scripts/story 0.14.rpy` | 2,911 |
| `scripts/story 0.13.rpy` | 2,827 |
| `scripts/characters.rpy` | 376 |
| `scripts/bios.rpy` | 247 |
| `script.rpy` | 121 |
| `screens.rpy` | 69 |
| `scripts/gallery_pax.rpy` | 69 |
| `scripts/preferences.rpy` | 25 |
| `scripts/flags.rpy` | 14 |
| `scripts/01story_sel.rpy` | 4 |
| `scripts/presplash.rpy` | 4 |
| `scripts/socials.rpy` | 3 |

另有约 100 处不在上述统计内（主菜单、章节选择、`Character()` 定义、`default` 列表等），
由提取器之外的流程手工补译。

## 术语

角色名沿用游戏自带 `script.rpy` 中官方已有的中文定义（`define X = Character("名字")`），
保证对话框与角色档案一致。完整表见 [`glossary.json`](glossary.json)。

关键几条：

| 英文 | 中文 |
|---|---|
| Lucy | 露西 |
| Victoria / Vicky | 维多利亚 / 薇琪 |
| Sarah | 莎拉 |
| Akatsuki | 晓月 |
| Akane（晓月之母） | 茜 |
| Misaki / Miss Takamura | 美咲 / 高村小姐 |
| Foundsborough College | 芬兹伯勒学院 |
| Founding Families | 开拓家族 |
| the shrimp / shrimplet（Sarah 绰号） | 小虾米 |

成人场景用语：`pussy` 小穴、`clit` 阴蒂、`fingering` 手活、`blowjob` 口交、
`handjob` 手交、`butt plug` 肛塞、`gag` 口球、`bondage` 束缚、`threesome` 三P。

## 翻译规则

1. 译文里不出现半角 `"` / `'` —— 会提前终止字面量，用 `「」` `『』` `’`
2. `[PlayerName]` `[Day]` `{color=#fff}` `{i}…{/i}` 等占位符与标签原样保留，数量与顺序不变
3. 半角 `~` 一律写全角 `～`
4. Ren'Py 的 `{tag}` 标记不能删

## 校验

- 结构校验：27 个文件、40,895 个字符串字面量，行号/列号/引号类型/三引号/语句关键字/遮蔽后骨架全部一致 → **PASS**
- 字形覆盖：517,804 汉字 + 88,123 中文标点，MiSans 全部命中 → **0 缺字**
- 实机运行：Ren'Py 重编译成功，界面启动无 error/warning

已知未修问题见 [approach.md](approach.md#已知的坑)。
