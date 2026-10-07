# Sinful Summer Chapter 3.6 — 翻译档案

简体中文本地化的术语决策、修过的问题与最终数据。**全部逐条人工翻译，未使用任何机器翻译或在线翻译 API。**

## 覆盖情况

| 项目 | 数量 |
|---|---|
| 对白行 | 22,480 / 22,480（100%） |
| 系统字符串 | 281 / 297 |
| 角色名 | 19 / 19 |
| 译文字符 | 约 43.8 万 |

保留英文的 17 条系统字符串分三类，都不该翻：

- **按键名**：`<` `>` `Ctrl` `H` `Page Down` `Page Up` `S` `Shift+A` `Tab` `V`
- **平台 / 品牌名**：`{b}Discord` `{b}F95zone` `{b}SubscribeStar` `{b}Unifans`
- **格式串**：`{font=font_title}{size=+20}{i}{outlinecolor=#000000}[config.version]`、`{size=-8}{color=#ccfdff}Ctrl / Tab`、`{size=-8}{color=#ccfdff}S`

## 角色名

| 变量 | 英文 | 中文 |
|---|---|---|
| `l` / `l_nvl` / `lmc_nvl` | Lyna | 莱娜 |
| `lm` | Lyna（心声） | {i}（莱娜） |
| `e` / `e_nvl` / `emc_nvl` | Erik | 埃里克 |
| `em` | Erik（心声） | {i}（埃里克） |
| `h` / `h_nvl` / `hmc_nvl` | Helga | 赫尔加 |
| `hm` | Helga（心声） | {i}（赫尔加） |
| `j` | Johan | 约翰 |
| `j_nvl` | ——（原版此处复用同一变量） | 朱丽叶特 |
| `lf` | Juliette | 朱丽叶特 |
| `a` | Anna | 安娜 |
| `sk` | Shopkeeper | 店主 |
| `au` | ——（原版刻意不揭晓） | `???` |
| `u_nvl` | Unknown | 未知 |

> `j` 与 `j_nvl` 在原版里指代不同角色，这是原作的变量复用，不是翻译错误，保持原样。

## 术语

| 英文 | 中文 | 说明 |
|---|---|---|
| MILF | 熟女 | 不用「少妇」「人妻」 |
| incest | 乱伦 | |
| Mom / Mother | 妈妈 | 不用「母亲大人」 |
| Dad | 爸爸 | |
| twin | 双胞胎 | 「孪生妹妹」「孪生的灵魂」在行文中自然，未禁用 |
| sister（指 Lyna） | 妹妹 | 全篇统一，不用「小姐姐」 |
| pussy / cunt | 骚穴 | |
| tits / boobies | 奶子 / 胸 | |
| dick / cock | 鸡巴 | |
| Lyns（Lyna 的昵称） | 小莱娜 | |

`sister` 固定译「妹妹」：Lyna 是 Erik 的双胞胎妹妹，译成「姐妹」会丢失长幼关系。

正式约束见 [`glossary.json`](glossary.json)，由 `tools/check.py` 强制执行。

## 文体决定

- **心声**（`lm` / `em` / `hm`）：角色名渲染成 `{i}（莱娜）`，与原作斜体+括号的心声格式一致。
- **场景分隔旁白**（`centered`，带 `{font=font_narration}{cps=…}{color=…}` 前缀）：只译正文，前缀原样保留。
- **内心独白**：一律用「他／她」指代本人，中文里不会出现英文的第三人称歧义。
- **拟声与口吃**：`*hic*` → `*打嗝*`；`Mmphh...!` 一类按语气译成「唔嗯……！」而不是逐音拟声。
- **英文脏话**：保留口语强度（goddamn → 「他妈的」），不弱化也不加码。

## 审计中发现并修掉的问题

### 1. 两行拿到了相邻行的译文

| 块 ID | 英文 | 修之前 | 修之后 |
|---|---|---|---|
| `hscene32_Lyna_Helga_a9f68e8a` | This is my goddamn fault! | 现在她对我发展出这种不健康的依恋…… | 这他妈的都怪我！ |
| `hscene12_Lyna_Helga_e44b54a1` | Mom...! Why are you grabbing my ass?! | 嘿，这本来是为了帮你！ | 妈妈……！你干嘛抓我屁股啊？！ |

第二行的译文属于同一场景里的 `hscene12_Lyna_Helga_d021277c`（"Hey, it's supposed to help you!"）。
两条都在 `build/batches/9017_fix_misfiled.tsv` 里改正。

### 2. 一条漏译

`stridx 22` 的 `SUPPORT ME <-` 原样留在英文（对应 Patreon 按钮），已改为「支持我 <-」。

### 3. 一处术语不一致

`story30_Erik_Helga_a598e32a` 用了「双胞胎**姐妹**」，而全篇统一称 Lyna 为「妹妹」。已改为「双胞胎妹妹」。

### 4. 中文显示为方块

游戏自带 5 个字体全是纯拉丁字体，2497 个译文字符没有字形。详见
[`translation-workflow.md`](translation-workflow.md) 与 [`../patch/zz_zh_locale.rpy`](../patch/zz_zh_locale.rpy)。

## 逐块差异译法

有 **84 个英文原文**在游戏里被译成了 2–4 种不同措辞，共影响 **263 行（1.17%）**，全部是短促的感叹与追问：

```
EN 'Ahhh...'          -> 啊啊！ / 啊——！
EN 'And that is...?'  -> 那就是……？ / 那是什么……？ / 是什么……？
EN 'Uh-huh.'          -> 嗯。 / 嗯哼。 / 在。
```

这是**有意为之**：同一个人物在同一场景里前后语气不同，用同一句会显得复读。
`data/tl_trans.json` 以英文原文为 key，表达不了这种逐块差异，因此它对每条取出现次数最多的那个译法
（覆盖 22,292 / 22,480 行）。全部变体保存在 [`../data/per_block_variants.json`](../data/per_block_variants.json)。

**后果**：`tools/build_tl.py` 的模板 + 译文库重建流程对这个游戏**不是逐字节可复现的**——
重建出来的 263 行会用上最高频译法。`patch/` 才是发布的产物，以它为准。