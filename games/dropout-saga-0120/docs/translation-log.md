# 翻译记录

## 总体

| 项 | 数值 |
|---|---|
| 原版可翻译字面量 | 15,214 |
| 已翻译为中文 | 14,941 |
| 按清单保留原文 | 273 |
| MOD 译文 | 1,273 条（6 个 `.rpyc`） |
| 翻译方式 | 人工逐条撰写，未使用任何机器翻译或在线 API |

补丁侧口径另算：14 个脚本、14,617 条 prose 字面量，其中 14,353 条中文、264 条非中文。
两个分母差 590，原因是 `options.rpy` 的行号相对原版偏移 1 行，
两个条目换了桶。两个口径**不能统一**，说明写在
[`data/coverage.json`](../data/coverage.json) 的 `_what_these_numbers_are` 里。

## 按文件

| 文件 | 字面量 | 中文 | 保留原文 |
|---|---|---|---|
| `day4_update.rpy` | 2,438 | 2,408 | 30 |
| `day5_update.rpy` | 2,359 | 2,345 | 14 |
| `day3_update.rpy` | 2,340 | 2,323 | 17 |
| `day6_update.rpy` | 1,978 | 1,965 | 13 |
| `day7_update.rpy` | 1,877 | 1,836 | 41 |
| `day2_update.rpy` | 1,778 | 1,698 | 80 |
| `day1_update.rpy` | 1,229 | 1,213 | 16 |
| `patreonmenu.rpy` | 301 | 297 | 4 |
| `script.rpy` | 165 | 155 | 10 |
| `screens.rpy` | 131 | 100 | 31 |
| `replay_gallery.rpy` | 14 | 10 | 4 |
| `options.rpy` | 5 | 1 | 4 |
| `day8_update.rpy` | 2 | 2 | 0 |
| `gui.rpy` | 0 | 0 | 0 |

另有攻略工具、工具箱、MOD 兼容补丁共 5 个新增脚本，不在上述统计内。

## 术语

角色名的唯一权威是 `script.rpy` 自己的 `Character()` 定义，
补丁显示的每个名字都和它全等比对（`verify_patch.py` 第 5 项检查）。
完整表见 [glossary.json](glossary.json)，21 个角色：

| 英文 | 中文 | 英文 | 中文 |
|---|---|---|---|
| Sophia | 索菲娅 | Isabella | 伊莎贝拉 |
| Ava | 艾娃 | Jasmine | 贾丝敏 |
| Ashley | 阿什莉 | Ingrid | 英格丽 |
| Asuna | 亚苏娜 | Kayle | 凯尔 |
| Lila | 莱拉 | Jennifer | 珍妮弗 |
| Loli | 洛莉 | Mika | 米卡 |
| Julie | 朱莉 | Norman | 诺曼 |
| Kane | 凯恩 | Peter | 彼得 |
| Chloe | 巧琪 | Hina | 希娜 |
| Tom | 汤姆 | Grace | 格雷丝 |

状态词：`corruption` 堕落、`goodness` 善良、`herd` 群体、
`newcomers` 小势力声望。

### 为什么有 273 条没翻

它们在 `glossary.json` 的 `_kept_verbatim` 里逐条列了名字（105 条去重后的串），
分三类：

1. **纯插值** —— 只有 `[name]`、`[daytext]` 这种占位符，没有可翻的词。
   翻译它只会让 Ren'Py 的插值看起来更奇怪。
2. **Ren'Py Preference 键名** —— `text speed`、`music volume`、`all mute`、
   `after choices`、`auto-forward`。这些是引擎内部用来存取偏好的键，
   改了 Preferences 就读不到玩家设的值。它们旁边的**可见标签**已经翻了。
3. **游戏内的德语／俄语／法语** —— 角色真的在说那些语言。

注意第 2 类的反面：`screens.rpy:265-266` 的 `Q.Save` / `Q.Load`
**不是** Preference 键，是两个可见的按钮文字，当时漏翻了，已补成
「快速保存」/「快速读取」。同一个数组里第 337 行的 `Load` 早就翻成了「读取」，
正是这个不一致让 `verify_patch.py` 的第 4 项检查把它抓了出来。

## 翻译规则

1. 译文里不出现半角 `"` / `'` —— 会提前终止字面量，用 「」 『』 ’
2. `[PlayerName]` `[Day]` `{color=#fff}` `{i}…{/i}` 等占位符与标签原样保留，
   数量与顺序不变
3. 半角 `~` 一律写全角 `～`
4. Ren'Py 的 `{tag}` 标记不能删
5. 专有名词在第一次出现处给全称，之后用简称

## 本轮修掉的四处缺陷

都不是校验能自动发现的，靠人工比对英文原文才发现：

| 位置 | 错的 | 对的 | 依据 |
|---|---|---|---|
| `day6_update.rpy` ×2 | 亚苏娟 | 亚苏娜 | `Asuna is... half-Japanese` |
| `day7_update.rpy:2415` | 阿什丽 | 阿什莉 | `When Ashley got hurt` |
| `screens.rpy:265-266` | `Q.Save` / `Q.Load` | 快速保存 / 快速读取 | 见上文 |
| `zz_zh_tools_ui.rpy` ×7 | 堝 U+581D | 堕 U+5815 | 裁图放大 6 倍对比窗口标题 |

最后一条的教训：`unicodedata.name()` 对 CJK 只返回算法名，查不到。
当时差点凭记忆把游戏自己用对的「堕」反向扩散成「堝」—— 是截图纠正的。
左边的「阝」不是「土」，这个区别肉眼要放大才看得出。

`山姆`（独立角色 Sam，82 次）和 `莉拉`（`script.rpy:993`，Lila 念名字时
结巴的 `Lee-lah?` → 「莉、莉拉」）是有意为之，不算错。

## 校验

- 仓库通用：`python tools/check.py --game dropout-saga-0120` → **all checks passed**
- 补丁专用：`python games/dropout-saga-0120/tools/verify_patch.py`
  → 20 个脚本 + 1 个字体 shim、40,739 行、14,617 条 prose 字面量，
    22 个角色名与 `script.rpy` 全等，`mod_zh.json` 1,273 条无空值
- 实机：Ren'Py lint 退出码 0，无 error 无 traceback；屏幕探针逐屏实例化，
  攻略工具 12 屏 + MOD 屏 18 屏全绿，22 个攻略 label 全部存在
- 安装器：`tools/roundtrip_test.ps1` 往返测试，1,558 个文件逐字节还原

往返测试不是走过场 —— 它在写下这行之前抓到过三个真问题：`font_assets.names`
带了目录前缀导致字体装到 `game/Fonts/Fonts/`；删除陈旧 `.rpyc` 时没备份，
卸载后原版字节码找不回来；以及那次扫描把**刚建好的备份目录**也扫了进去，
19 个文件报成 33 个，还顺手删掉了自己刚做的备份。

已知未修问题见 [approach.md](approach.md#已知的坑)。
