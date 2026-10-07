# 为什么 TOXICity 不用 translate 补丁

仓库另外两款游戏（Eden Chapter 5、Sinful Summer 3.6）走标准的 Ren'Py 翻译块路线。
本作和 Cosy Cafe 一样偏离了这条路，原因是硬约束，不是偏好 —— 而且本作比 Cosy Cafe
多一个理由：**补丁里还塞着一个第三方 Mod**。

---

## 一、发行包没有 `game/tl/` 模板

`tools/build_tl.py` 的输入是 `games/<slug>/tl_template/`，而 `tools/template.py` 负责从
`<游戏>/game/tl/<lang>/` 把这份**英文原文**模板拷进来。

TOXICity 0.22.0 的 `game/` 下有 `tl/` 目录，但里面没有任何语言模板 —— 没有
`tl/schinese/`，也没有可导入的 `translate` 块。开发者根本没做多语言结构。
没有模板，`build_tl.py` 直接 `sys.exit`。

顺带一提：本作**原版就自带中文字体** `fonts/msyh.ttc`（微软雅黑），而且
`define_default.rpy` 里的角色名本来就是中文（`define k = Character("卡莉")`）。
它是一个「中文可玩、但没有做翻译块」的发行版。所以
`options.rpy` 里的 `config.name = _("TOXICity")` 这类 `_()` 包装其实是从未启用过的机制。

## 二、补丁要带的 Mod 根本不在 `game/tl/` 里

这是本作独有的问题。Gugatron Mod 的三个脚本
（`mod/GugatronCheats.rpy`、`mod/GugatronUnlock.rpy`、`mod/mod.rpy`）
是**独立文件**，靠 `mod/` 目录和颜色宏（`gr` / `rd` / `rgr` …）驱动，
和游戏主脚本之间没有任何 `translate` 块关系。

一份 translate 补丁能表达的只有「往 `game/tl/<lang>/` 放一棵翻译树」。
Mod 的脚本、Mod 的按钮、Mod 在 `script*.rpy` 里插入的增量剧情，
这些都表达不了。要收录 Mod，就只能整体替换 `.rpy`。

## 三、`tools/install.py` 没有覆盖游戏脚本的能力

它的全部动作只有三样：`game/tl/<lang>/`、`game/<shim>.rpy`、`game/fonts/*`。
本作 28,524 条含中文的字面量分布在游戏自己的 13 个 `.rpy` 和 Mod 的 3 个 `.rpy` 里，
只能整体替换。

**因此安装请用 `tools/install.ps1`，不要用 `tools/install.py`。**
这与 `cosycafe-0142` 的做法一致。

---

## 实际采用的方案

用中文版 `.rpy` 整体替换脚本（`patch/game/`），配一个字体接管脚本
`patch/zzz_font_misans.rpy`，用 `tools/install.ps1` 安装。

### 增量剧情是怎么合并的

Mod 会往 `script.rpy` / `script2.rpy` / `script3.rpy` 里插入新剧情。
采用的策略是 **以已汉化脚本为主体，按 diff 定向移植增量**，
而不是拿英文重新翻译一遍：

1. 取出 Mod 包里的英文 `script*.rpy`（含增量）与此前的汉化版 `script*.rpy`；
2. 行级 diff 对齐两者，重建「英文原文 → 汉化行」的映射；
3. 只对 Mod 新插入的 134 行写新译文，其余原样保留既有译文；
4. 重新编译并实机验证。

这样做的好处是**存量译文零回归** —— 27,150 句已翻内容一个字节都没动，
新增部分才需要新译。

---

## 字体：既不是 shadow，也不是 fallback

仓库文档里的 `font_strategy` 只有两种取值，本作两种都不完全对得上，所以
`game.json` 里记的是 `fallback`（更接近的那个），并另加了 `_font_mechanism` 说明实情。

**本作原版就自带 `fonts/msyh.ttc`（微软雅黑），中文字形是全的。**
换句话说：装补丁之前中文就能正常显示，MiSans 是**排印升级**，不是补方块。
所以补丁**一个字体文件都不覆盖**，卸载后玩家拿回的是游戏自己的字体，而不是被改过的。

实际做法是在启动期改写字体请求：

| 原本请求 | 出现次数 | 接管后 |
|---|---|---|
| `fonts/msyh.ttc` | 291 | `fonts/MiSans-Regular.ttf` |
| `fonts/msyh.ttc`（粗体） | 约 90 处 `<b>` | `fonts/MiSans-Bold.ttf` |
| `fonts/DCC - Ash.otf` | 5 | MiSans |
| `mod/Monster Racing - Personal Used.otf` | Mod 装饰字体 | MiSans |

接管由两个脚本完成，都写 `config.font_replacement_map`：

- `patch/zzz_font_misans.rpy` —— 接管 `fonts/msyh.ttc`（291 处引用全部指向这一个字面量，
  包括 `gui.text_font` / `name_text_font` / `interface_text_font`、`Character(what_font=)`
  和行内 `{font=...}` 标签）
- `patch/game/mod/zzz_zh_font.rpy` —— 接管 Mod 那两款只有一百多个码位、
  完全不含中文的装饰字体

**为什么不改脚本里的 291 处 `fonts/msyh.ttc` 字面量**：改一个开关就能整体切回；
不动脚本文本意味着译文与标签校验完全不受影响；而且能拿到 MiSans 的**真 Bold 字重**，
而不是 Ren'Py 合成的假粗体。

### 缺字体不会炸

`renpy.loadable()` 探测在 `_apply_zh_font()` 最前面就return 掉。
删掉 `assets/fonts/*.ttf` 再启动，游戏照常跑，只是字体回落成微软雅黑。
这是刻意的：MiSans 的再分发授权并不干净（见 `assets/fonts/LICENSE-MiSans.txt`），
补丁不该因为玩家手里没有这个字体就拒绝启动。

### Ren'Py 7.4.5 的坑

本作跑的是 **Ren'Py 7.4.5**，不是 8.x。`renpy.loadable()` 和
`config.font_replacement_map` 在 7.4.5 里都存在
（引擎自己的 `renpy/common/00voice.rpy` 就在调 `renpy.loadable`），
但 `renpy.loader.loadable` 这种写法是 8.x 的形状，**不要照抄 Cosy Cafe 的 shim**。

---

## `data/tl_trans.json` 是怎么来的

它不是翻译时同步产出的数据库，而是**事后从成品脚本反推**出来的，
这样它和 `patch/game/` 里实际存在的文字永远一致。

做法是把每份**英文原版**和**出货的中文脚本**逐行对齐：

1. 行级匹配用的是「骨架」—— 把行里所有字符串字面量挖空后剩下的部分；
2. 只有骨架相同的行才会配对，所以配出来的对子结构上必然对应；
3. 配对后再按规则过滤：中文侧必须真的含汉字、两侧不能字面相同。

结果：39,000+ 个中英配对候选 → 过滤后 **25,300 条**入库。
另有 3,898 条被丢弃，全部是「中文侧不含汉字」的项 —— 资源路径、内部标识符、
以及刻意保留英文的内容（见 `docs/glossary.json` 的 `_kept_verbatim`）。

**这份数据库只用于记录和校验，不参与打包。**
出货的是 `patch/` 下的成品 `.rpy`，玩家拿到的是脚本，不是数据库。

---

## 校验时发现的四个真实缺陷

结构对齐看不出内容错位，所以定稿前专门做了内容层的检查。
以下四类问题都已修复：

### 1. 行号泄漏进台词（3 处，`scenes_kallie.rpy`）

粘贴时把源文件的行号标记带进了字符串：

```
k "唔唔~~~ 唔唔嗯~~~~ 哦对~~~1392|有那么一瞬间我意识到……"
```

`1392|` 后面整段是**下一行旁白**的内容，被并进了这句拟声词里。
同样的问题还有 `1396|` 和 `1399|`，三处都在 `scenes_harem` 场景的第 16 章。

### 2. 整段台词错位一格（`scenes_harem.rpy` 第 17 章，19 行）

比第 1 类严重得多，而且**结构完全正常** —— 行数对得上、说话人前缀对得上、
引号对得上，所以任何基于 diff 的校验都发现不了。

实际情况是每一行都装进了**下一行**的译文：卡莉和雪莉在念旁白，
旁白格里塞的是呻吟声。整段从第 329 行到第 353 行，最后一行 369 重复了 370 的旁白，
而 353 行当时正攥着 369 行那句 `哦呜~~~ *喘气* *喘气* 哦呜~~~`。

修法是**把已有译文整体挪回去**，一个字都没重写；
只有第 329 行那句 `k "Haaaa~~~~ haaa~~~~"` 的译文确实丢了，
由第 320 行 `k "Ahhhh~~~ ahhhh~~~~"` 的译文交换波浪号长度生成。

### 3. 角色名不一致（25 处）

`Nancy` 在游戏自己的 `define_default.rpy` 里是 `南希`，但译文里有 24 处写成 `南茜`；
`Keith` 是 `基思`，有 1 处写成 `基斯`。已统一。
现在 `docs/glossary.json` 把这些变体列入 `banned`，以后再漂移会被 `check.py` 拦下。

### 4. 一处术语不统一（1 处）

Mod 增量剧情里有一句 `女士洗手间`，其余各处一律是 `洗手间`。
统一成 `洗手间`，并把 `女士洗手间` 加进 glossary 的 `banned`。

---

## 已知不做的事

- **`dump.rpy` 不翻译。** 那是开发者的草稿脚本，游戏从不调用；
  补丁给它加了 `if False:` 兜底，免得它在 lint 时报错。
- **17 个 OST 曲目名保留英文。** 专辑 / 曲目名是名字不是散文，
  翻了就没法对着原声带找了。
- **`patch/optional/Save_Name.rpy` 不自动安装。** 它是 Mod 包里附带的
  Ren'Py 存档页覆盖（`class FilePage`），会顶掉引擎自带的存档分页。
  实测本作用不到它，所以放进 `optional/` 由玩家自己决定，
  装法见 `README.md`。
- **`options.rpy` 的制作人员名单保留原名**（`shreek`、`Anime Sins`、`Mordred93`），
  背景音乐 / 音效来源同理。
