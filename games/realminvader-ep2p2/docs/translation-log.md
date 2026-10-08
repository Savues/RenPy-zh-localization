# Realm Invader Episode 2 Part 2 — 翻译档案

原作：Realm Invader ｜ 引擎：Ren'Py 7.4.11 ｜ 语言：`schinese`

## 方案

`tl-blocks`。游戏发行包里带着 `game/tl/schinese/` 模板，正文、界面、角色名全部走
Ren'Py 官方翻译机制；补丁只放翻译块与一个 shim，不顶掉任何原版脚本。
`archive.rpa` 原封未动。

## 规模

| | |
|---|---|
| 翻译条目 | 16,183 条（唯一英文原文） |
| 原文引用 | 19,214 处 |
| 补丁文件 | 8 个 `.rpy`，113,057 行（另有 1 个 shim） |
| 覆盖率 | 100%（7 条刻意保留原文，登记在 `glossary.json` 的 `_kept_verbatim`） |
| 角色名 | 80 条 |

保留原文的七条：

- `DejaVu Sans`、`Opendyslexic`——字体名。字体选择界面和版权页上会出现它们，
  翻成中文之后别的工具再也认不出这两款字体；
- `a`、`q`——按键提示里的单个键名，周围的句子已经带足了意思；
- `★.`、`♥♥♥`、`♥♥♥♥♥♥♥`——纯符号的装饰性占位，玩家读的是节奏不是字，没有可译的成分。

## 角色名

名字是**重映射**，不是翻译。Ren'Py 不把 `Character("Ashley")` 送进翻译流程，
所以 `tl/schinese/characters.rpy` 里用一张 `_realm_invader_name_replacements`
替换表在显示前改名，80 条，和对白写在同一个文件里。

这一款没有像 Por(n)tals 那样把名字表放进 shim——表本来就住在翻译文件里，
Ren'Py 自己会加载它，再抄一份到 shim 反而有两个可能漂移的地方。

`docs/glossary.json` 里的角色表是从那张替换表直接读出来的，两边不会漂。
一条 `banned` 都没写：check.py 是纯子串匹配，而这些名字大半同时是普通中文词
（孩子、学生、老师、陌生人、安保人员），一封就误伤正文。

## 两处译文整段贴错了行

`check.py` 查得出未译、乱码、叠字、行宽，查不出**内容对不上**。有人把隔壁那行
整段粘过来，两处都能通过全部校验——因为语法合法、长度合格、没有未译标记。

| 位置 | 英文原文 | 错成了 |
|---|---|---|
| `script2_2.rpy:39767` | `a "Oh, wow, you remembered my name."` | 后面 `script2_2.rpy:39851` 那段「我告诉他们我是来寻仇的……」 |
| `script2_2.rpy:37157` | `g "Wha- M-my legs! They've gone weak!"` | 下一行 `g "[name], you idiot! You fingered me so hard..."` 的译文 |

第一处尤其能骗过检查：那段长译文在**它自己的位置上完全正确**（39851 行），
所以整份文件里两次都查得到它，只是挂错了行号。肉眼顺着念英文注释就能发现。

`tools/audit_paste.py` 就是为这一类写的：把译文按中文分组，同一个中文挂在两个
英文相似度低于阈值的原文上，就报出来人看。纯等值查重抓不住这两处——它们的中文
彼此差几个字（`插我插得太狠了` / `那几下指交太狠了`），得用近似查重。
同一个工具在 AcademyLive 里又找出一处，已在那边记录。

```
python tools/audit_paste.py --game realminvader-ep2p2
```

跑完还有 14 条待读，全是近义合并：`I knew it.`（认同预言）和
`Wouldn't expect anything less.`（对死对头）共用「我就知道会这样」是对的；
`*GASP*` 和 `*Gasp*` 共用「*倒吸一口气*」也是对的。这类必须留给人判断，
所以工具默认只打印报告、不返回失败。

## 三条超宽

| 英文原文 | 改前 | 改后 |
|---|---|---|
| `c "And cuddly..."` | 而且还要能让人想抱在怀里的…… | 而且还要毛茸茸的…… |
| `m "Imagine C-ing D-z nuts."` | 想象一下「C-ing D-z nuts」（谐音梗：想象一下看到我的蛋蛋）。 | 想象「C-ing D-z nuts」（seein' nuts）。 |
| `Still, she boldly smiles at you...` | 136 列 | 118 列 |

第二条那行是接在「Imagine Dragons 的 CD 有多尴尬」后面的双关。原译把梗解释成了
「看到我的蛋蛋」，等于把包袱拆了说；改成给出 `seein' nuts` 这个谐音本身，
读者自己听得出来，宽度也从 62 列降到 41 列。

## 不要重跑 build_tl.py

`data/tl_trans.json` 是按英文原文做 key 的**扁平字典**。本作有 **174 条**英文原文
按上下文该有两种译法，扁平字典只能存一种。重跑 `tools/build_tl.py` 会把它们
全部塌缩成最后见到的那一种，实测 **420 行**正文被改掉。

所以本目录的 `patch/tl/schinese/` 是**成品**，不是 `build_tl.py` 的产物，**不要重跑**。
要改哪句就直接改 `patch/tl/schinese/`，改完跑
`python tools/check.py --game realminvader-ep2p2`。译文库在这里仍然有用——
它负责查未译、乱码、叠字、行宽和术语——只是它当词表用，不当构建输入用。

`build_tl.py` 在这一款上还会报 `still untranslated: 167` 并返回 1。这 167 条全是
`characters.rpy` 里 `_realm_invader_name_replacements` 那张表的引号内容，80 个英文
键加 80 个中文值，不是对白。`tl_trans.json` 故意不收它们，`build_tl` 遇到查不到的
条目会跳过、把这行原样留着，而模板里那行本来就是中文的成品表。真正会被它改写的
只有一行：`("???", "？？？")`——它连英文键一起替换成「？？？」，替换表就再也匹配不上
`Character("???", ...)`，那一个说话人名字会退回 `???`。

细节记在 `game.json` 的 `_do_not_run_build_tl` 与 `_build_tl_harmless_failures`。

## 主菜单文字看不见，这是发行版的问题

原版主菜单用自制的 `MakeVisualNormals.SimulatedLighting` 着色器画标题和按钮。
在这台机器上那个着色器把字形渲染成接近白色，而菜单底板是白的——按钮点得到、
字看不见，而且前两秒 alpha 还是 0。

`zz_zh_cn_menu.rpy` 保留了原来的布局、美术和 action，只把文字换成普通的高对比度
文本。这是渲染绕行，不是改版式。

## 两个 shim 合成一个

补丁原本是 `zz_zh_cn.rpy`（语言、字体组、`font_transform`）和 `zz_zh_cn_menu.rpy`
（主菜单文字）两个文件。`games.patch_entries()` 每个游戏只认一个 shim，
`package_release.py` 也只写那一个，两个文件它只会带走一个，所以合成
`zz_zh_locale.rpy`。直接拼接是安全的：`init 100` 和 `init 1501` 只出现在前一个文件里，
后一个根本没有 `init` 块，只有一个 `transform` 和 `screen main_menu()`，
而屏幕是首次显示时才求值的，远在 `init 100` 绑定完 `_ZH_CN_FONT` 之后。

## 字体

自带 **Noto Sans SC**（SIL OFL 1.1，可再分发），放在 `assets/fonts/`，
shim 里按 `fonts/NotoSansSC-VF.ttf` 引用——原补丁写的是 `Fonts/NotoSansSC-VF.ttf`，
但 `tools/install.py` 和 `tools/package_release.py` 只会写 `game/fonts/`，
同一个文件、上一层目录，Ren'Py 两个都认。

shim 里还有 MiSans 分支，**故意不附带**：MiSans 的名称表里既没有许可证描述也没有
许可证网址，版权行结尾是 All Rights Reserved，没有可援引的再分发授权，把字体文件
打进公开的 release 那是替作者做的判断，这个仓库不替作者做。MiSans 分支原样保留——
玩家自己把 `MiSans-Regular.ttf` / `MiSans-Bold.ttf` 放进游戏的 `game/Fonts/`，
脚本会自动启用，一个字都不用改。

## 这是仓库里最老的引擎

7.4.11。shim 用到的 `config.font_transforms` 和 `config.change_language_callbacks`
在 7.4 里都有，但别默认 8.x 才有的 API 在这里也能用。

