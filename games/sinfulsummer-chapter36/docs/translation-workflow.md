# Sinful Summer Chapter 3.6 — 汉化流程存档

这一份记的是**过程和踩过的坑**：接手这个项目的人最需要的就是这部分，而不是译文本身。
术语决策与最终数据在 [`translation-log.md`](translation-log.md)。

## 这个游戏的特别之处

**1. 脚本全部打包在 `archive.rpa` 里，游戏目录没有任何 `.rpy`／`.rpyc`。**

3.5 GB 的 RPA-3.0 归档，`script_base.rpyc`、`script_chapter2.rpyc` 等全部是编译过的字节码。
所以：

- `tools/template.py` 走不通（它要的是 `game/tl/<lang>` 下的模板，而游戏目录里没有）
- `tools/install.py` 的 `options.rpy` 存在性检查会误判这不是游戏目录
- 提取原文只能走 `tools/rpa.py` + 反编译 `.rpyc` AST

**2. 本项目没有走「英文模板 + 译文库 → 重建补丁」的路线。**

原文与译文是一开始就按块 ID（`story30_Erik_Helga_a598e32a` 这种 Ren'Py 翻译标识）对齐的，
`patch/` 直接由 `tools/generate.py` 生成并提交。`data/tl_trans.json` 是**事后**从补丁反推出来的
检索 / 校对用数据库，不是构建输入。原因见 `translation-log.md` 末节。

## 工具链（游戏目录之外，在 SinfulSummer-zh 工作区）

| 脚本 | 作用 |
|---|---|
| `tools/rpa.py` | 独立的 RPA-3.0 读写器，不依赖 Ren'Py 运行时 |
| `tools/generate.py` | `build/workbook.json` + `build/batches/*.tsv` → `game/tl/schinese/*.rpy` |
| `tools/audit_tags.py` | 逐块比对中英文的 Ren'Py 标记序列 |
| `tools/fontcheck.py` | 纯标准库解析 ttf 的 cmap，核对字形覆盖 |
| `tools/sync_repo_patch.py` | 把生成结果同步进本仓库的 `patch/`，并做规范化 |

批次文件按文件名排序加载，**后者覆盖前者**，所以修正写成 `9xxx_fix_*.tsv` 即可，
不用回头改已经翻完的大批次。

## 坑一：TSV 多了一列，2261 行游戏里显示成 `em "em"`

早期有 2262 行被写成**四列** TSV，而 `generate.py` 只取 `parts[2]`，
于是译文整列丢失、游戏里显示成变量名。现在生成器用 `chr(9).join(parts[2:])` 兜住多余的列。

**教训**：写中文补丁一律**直接写中文字符**，不要用 Python `\uXXXX` 转义。
早期用转义写入造成过棓 / 漉 / 罪贼 / 裸裴 这类批量错字，后来全部改成直接写。
PowerShell 落盘用
`[System.IO.File]::WriteAllText($p, $c, (New-Object System.Text.UTF8Encoding($false)))`
（`.NET` 不跟随 PowerShell 的相对 cwd，路径必须给绝对的）。

## 坑二：中文全是方块

### 根因

Ren'Py 在**渲染时**才查 `renpy.config.font_name_map`（`renpy/text/text.py:254, 296, 1391`）。
游戏自带的 5 个字体全是纯拉丁字体：

| 字体 | 码位数 | 缺译文字符 |
|---|---|---|
| DejaVuSans.ttf | 5919 | 2497 |
| DejaVuSans-Oblique.ttf | 5284 | 2497 |
| Poppins-Light.ttf / Italic | 471 | 2499 |
| BebasNeue-Regular.ttf | 461 | 2498 |
| Roboto-Black.ttf | 922 | 2498 |

脚本只给 **328 行**对白打了 `{font=font_narration}` 标签，其余 22,000+ 行和全部菜单、
按钮、设置界面都走默认样式字体 `DejaVuSans.ttf`。
**只映射 `font_narration` 这类别名是不够的**，必须把字体文件名本身也注册进映射表。

硬证据：size 32 下渲染 `中文测试`，MiSans 每字 advance = 32.0（正好 1 em，全角等宽），
DejaVuSans 每字 19.2 —— 那是 `.notdef` 空心框的宽度。

### 修法

[../patch/zz_zh_locale.rpy](../patch/zz_zh_locale.rpy) 把 11 个字体名（5 个别名 + 6 个文件名）
各自映射成一个 `FontGroup`：游戏原字体负责它有字形的部分，MiSans 负责 `zh_cjk_ranges` 里的码位区间。
拉丁文因此保持原样——这是「覆盖字体文件」的做法做不到的。

三个必须遵守的细节：

1. **先建完所有 FontGroup 再写 `font_name_map`。**
   `FontGroup.add()` 在字体名已经是该字典的键时会抛异常（`renpy/text/font.py:870`），
   而这里的 base font 本身就是键。
2. **字体用裸文件名。** `renpy.loader.load()` 会先试空前缀再试 `fonts/` 前缀
   （`renpy/loader.py:640-664`），裸名和 `fonts/xxx.ttf` 都能加载，裸名更符合引擎预期。
3. `……`(U+2026) 和 `—`(U+2014) 也划给 MiSans，让中文标点与汉字同源。

### 选字体时踩的坑

最初用的是系统里现成的 `NotoSansSC.ttf`。它覆盖 100%，但读完 name 表才发现
**它是可变字体，默认实例是 `wght=100`（Thin）**——中文会比英文正文明显偏细。
改用静态的 MiSans Regular（`usWeightClass=330`），粗细才对得上。

判断方法（`tools/fontcheck.py` 同款思路）：读 ttf 的 `fvar` 表看 `wght` 轴的 `default` 值，
别只看文件名和族名。

## 坑三：`check.py` 的两条规则对不上这个游戏

收录进仓库时 `tools/check.py` 报了两类问题，都需要改规则而不是改译文：

1. **绝对列宽上限误报。** `ABS_MAX=130` 是按 Eden 的对话框定的，
   但它对「译文比英文原文**更短**」的情况也报警。
   Sinful Summer 有 7 条旁白被这样误判（例如英文 194 列、译文 138 列）。
   138 列的中文就是 69 个汉字，完全放得下。规则改为**只在译文比原文更宽时才报**，
   抓的仍然是「撑破对话框」这种真正的问题。Eden 复测无回归（63/63 守卫仍然生效）。

2. **术语守卫对「包含规范词」的禁用译名完全失效。**
   原来的写法是 `variant in value.replace(canonical, "")`：
   规范词 `熟女`、禁用译名 `熟女少妇`，去掉规范词后剩下 `少妇`，永远匹配不上。
   改成——只有当禁用译名**不包含**规范词时才做剔除。修好后 Sinful Summer 的
   selftest 从 43/48 变成 48/48。

## 译文对齐审计方法

「中文跟英文对不上」是最难自动发现的一类错误。这里用的两个检测器：

1. **列宽比**。`tools/check.py` 的 `REL_MAX` 规则会报出「短英文 + 长中文」，
   `This is my goddamn fault!`（25 列）配上一句 58 列的中文就是这么找到的。
2. **长译文重复**。取英文原文在脚本中唯一、而中文译文相同的块组——
   两句不同的英文不可能共用一句具体的中文，那就是放错了。
   阈值要卡住长度（≥ 12 列），否则 `嗯？` `是啊？` 这类短句会淹没结果。

两个检测器合起来找到 2 处真实错配。**它们不保证召回率**：
22,480 行没有做过逐条双语复核，仍可能有漏网的。
接手的人如果要重跑，这两段逻辑在提交记录里。

## 交付前检查

```bash
python tools/check.py    --game sinfulsummer-chapter36   # 必须 all checks passed
python tools/selftest.py --game sinfulsummer-chapter36   # 必须 48/48
python tools/check_links.py                              # 文档链接没断
```

游戏侧还要跑一次 Ren'Py 自带的 lint（用游戏自带的 python），
`tl/schinese` 问题数必须是 0：

```powershell
& "$game\lib\py3-windows-x86_64\python.exe" "$game\SinfulSummer.py" $game lint
```

> 只复制 `.rpy`，**绝不复制 `.rpyc`**——Ren'Py 优先加载 `.rpyc`，
> 残留的旧字节码会静默盖过新脚本。