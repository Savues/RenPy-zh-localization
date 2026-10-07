# 字体 / Fonts

中文字体**在仓库里**：每个游戏一份，放在 `games/<slug>/assets/fonts/`。安装补丁时它会
被复制成游戏硬编码的那几个文件名放进 `game/fonts/`，玩家不需要自己找字体，也不需要
往补丁里塞任何需要授权的东西。

## 为什么必须换字体

游戏脚本里到处写死了字体**文件名**——对话框正文、标题、数值、强调，各用一个。
Ren'Py 是按文件名找字体文件的，不是按字体内部的 family 名。所以中文补丁必须让一款
含中文字形的字体出现在那几个路径上，否则正文渲染出来是一片方块。

这些名字同时出现在 `{font=...}` 标签、界面样式表和 `gui.*_font` 设置里，有些还是
运行时才拼出来的字符串。逐个去改脚本既慢又脆；Ren'Py 虽然有
`config.font_replacement_map`，但**直接覆盖磁盘上的同名文件**是唯一能一次盖住所有
引用、且完全不需要改动游戏脚本的做法。

**具体是哪几个文件名取决于游戏**，记录在 `games/<slug>/game.json`：

| 字段 | 含义 |
|---|---|
| `patch_font` | 补丁自造的名字，原版游戏里没有这个文件 |
| `font_shadow` | 游戏自带的西文字体，会被覆盖 |
| `font_asset` | 仓库里打包的那份字体 |
| `font_license` | 字体授权声明，打包时以 `FONT-LICENSE.txt` 放进压缩包根目录 |
| `font_credit` | 玩家 README 里显示的署名 |

给新游戏找字体名，两条 grep 都要跑：

```bash
grep -rn "font=" "<游戏目录>/game" --include=*.rpy
grep -rn "_font *=" "<游戏目录>/game" --include=*.rpy
```

第一条抓 `{font=...}` 标签里的运行时引用，第二条抓界面配置。漏掉任何一个，就会有一
部分文字仍然是方块。

## 同一份字体为什么要存好几份

游戏要 N 个文件名，压缩包和 `install.py` 就放 N 份内容相同的文件。字体已经是压缩过
的格式（ttf 内部自带压缩），压不动，所以这一块体积是线性增长的：Eden Chapter 5 一个
游戏就是 5 份 × 5.14 MB ≈ 25.7 MB，加上 1.6 MB 的脚本，总共 27.3 MB。

Release 要放很多个游戏的汉化包时，这一项是主要成本。

另一种做法是只放 `zh.ttf` 一份，再把译文里剩下的 `{font=CinzelDecorative.ttf}`
之类的标签统一改写成 `{font=zh.ttf}`。渲染结果**完全一样**——那 4 个名字里放的本来
就是同一份字体——包能缩到约 7 MB，代价是要改译文数据库并重建补丁。Eden Chapter 5
里这样的标签有 13 处。

没有这么做，是因为要让「只放一份」这件事对**每个游戏**都成立，就得在译文里统一改写
字体标签并把它当成一条硬规则，而这是翻译产物该管的事、不是打包该管的事。纯靠文件覆
盖的方案新增游戏零成本，代价只是压缩包大一点。

## 想换一款字体

替换 `games/<slug>/assets/fonts/` 里的文件，同步更新 `game.json` 的 `font_asset`、
`font_license`、`font_credit`，重新打包即可。新字体要能显示中文，且它的授权允许随
补丁一起分发。

只想临时换一款：

```bash
python tools/install.py "<游戏目录>" --font "/path/to/YourFont.ttf"
```

脚本默认用仓库里打包的那一份（和压缩包里的是同一个文件，所以脚本安装和解压安装
渲染结果一致）；系统字体列表只在仓库缺了字体资源时兜底。

## MiSans 的授权情况

`assets/fonts/MiSans-Regular.ttf` 取自小米官网的公开字体下载地址。字体内部 name 表
的内容是：

```
family      MiSans
version     2.000
copyright   Copyright (c) 2020-2021 Beijing Xiaomi Mobile Software Co.,Ltd. All Rights Reserved.
vendor url  https://www.hanyi.com.cn/
```

需要注意：**name 表里没有 nameID 13 的授权文本，也没有授权 URL**，版权行本身写的是
All Rights Reserved。小米官网把它列在「免费商用字体」里，但字体文件自身没有附带任何
可再分发的授权声明。

把这样一份文件打进汉化补丁再分发出去，是有风险的。作为缓解，压缩包里放了
`FONT-LICENSE.txt`，玩家 README 里也署了名，让收到的人知道这是什么、来自哪里。要彻底
消除这个风险，把 `assets/fonts/` 换成 SIL OFL 授权的字体（思源黑体 / Noto Sans CJK）
就行——字段结构一个字都不用改，只是 OFL 版本的文件要大不少。

> 这是**已知并接受的取舍**，不是疏忽。相关决定记在
> [`games/eden-chapter5/docs/translation-log.md`](../games/eden-chapter5/docs/translation-log.md)。

## 字体缺字形的问题

MiSans 覆盖 28,968 个码位，中文正文够用，但**符号区基本是空的**——U+2764 `❤️`、
U+2665 `♥`、U+2663 `❣`、U+2661 `♡` 和整个 Dingbats 区都没有。能用的只有 `● ■ ★ ☆
▲` 这类几何图形。

翻译里不要用 emoji，这是硬约束而不是风格偏好。具体踩到的例子见 Eden Chapter 5 的
[翻译档案](../games/eden-chapter5/docs/translation-log.md)。

## 不做「退回英文版」

本项目不以「退回原版」为设计目标。安装就是覆盖，包括游戏自带的西文字体。想换回英文
版就重新解压一次游戏——比在补丁里维护一套还原逻辑省事，也不会让安装多出「先备份」这
种容易漏掉的前置条件。

`install.py` 仍然会备份被覆盖的文件，`uninstall.py` 仍然能从备份逐字节还原，只是不把
它当成主路径来设计。
