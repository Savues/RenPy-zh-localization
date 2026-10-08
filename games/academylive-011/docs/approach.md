# 方案记录：怎么把一个已装好的补丁收进这个仓库

这份记录写在**第二个**游戏进场之前，写给下一个要收游戏的人看。

## 已装补丁本身就带英文

Ren'Py 的翻译文件自带重建所需的全部英文，不需要回去挖 `.rpa`：

- `translate <lang> strings:` 块里，`old "..."` 是英文原文，`new "..."` 是译文；
- 每一个对白块，被译的那一行**上面**就是原文注释：

```renpy
# game/events.rpy:34
translate schinese kiyomi_first_office_talk_b79ba5e8:

    # mc "Yeah, what exactly should I be doing here?" with d
    mc "有，我到底该在这里做什么？" with d
```

于是 `patch/tl/<lang>/` 直接从游戏目录整棵复制，`tl_template/` 用注释里的英文
就地重建，`data/tl_trans.json` 由英文↔中文按行配对得到。**英文原文一步都不用
解包 `.rpa`。**

## 重建的可验证性

`tl_template/` 被 `.gitignore` 排除（那是原作，不该进仓库），但它必须在本地能重建出
补丁。重跑 `tools/build_tl.py` 之后逐文件比对，结果就是 §「不要重跑 build_tl.py」
里那两个数字——这是**量**出来的，不是推断的。

## 配对规则与它的边界

按「上一条注释 + 当前行」配对，要求两行的引号数相同。63 个文件 25,803 条对白里
**只有 6 行**配不上，都是 `{w}`、`nvltext` 这类跨行语句，落到 `tl_template/` 里仍是
英文原样，不影响覆盖率。

## 字体

游戏把 `gui.*_font` 指向 `gui/fonts/NotoSansSC-VariableFont_wght.ttf`。但
`tools/install.py` 和 `tools/package_release.py` 只会写 `game/fonts/`，而
[`docs/adding-a-game.md`](../../../docs/adding-a-game.md) 明说新增游戏不许改 `tools/`。
所以把 shim 里的路径改成 `fonts/NotoSansSC-VariableFont_wght.ttf`——同一个文件，
换个目录，Ren'Py 两个都按 `game/` 解析。

西文字体不覆盖，而是靠 `config.font_replacement_map` 把脚本里写死的五个字体名
（`DejaVuSans.ttf`、`AtkinsonHyperlegible-Bold.ttf`、`CrimsonText-SemiBold.ttf`、
`JosefinSans-SemiBold.ttf`、`YsabeauOffice-Regular.ttf`）统一指到中文字体上。
