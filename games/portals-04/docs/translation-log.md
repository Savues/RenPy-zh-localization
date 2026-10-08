# Por(n)tals 0.4 — 翻译档案

原作：onehend ｜ 引擎：Ren'Py 8.2.0 ｜ 语言：`schinese`

## 方案

`tl-blocks`。游戏自带 `game/tl/schinese/` 模板，补丁只放翻译块与一个 shim，
不顶掉任何原版脚本。

## 规模

| | |
|---|---|
| 翻译条目 | 23,910 条（唯一英文原文） |
| 补丁文件 | 12 个 `.rpy`，148,832 行 |
| 覆盖率 | 100%（3 条保留原文） |

保留原文的三条，都是「保留英文才对」：

- `Kinetic Text Tags Ren'Py Module 2021 Daniel Westfall <SoDaRa2595@gmail.com>`
  ——第三方 Ren'Py 模块的版权行，属于它的作者，不是本作界面文案；
- `Wyr nyat dyunn yeth...`——康沃尔语，是这句台词的梗本身，旁边的角色是在对这个
  语言起反应，译掉就把笑点译没了；
- `{sc=2}{size=*1.2}KURWAAAAAAAAAAA!`——喊叫，它的值就是拼写。

## 角色名

Ren'Py **不把 `Character("Mom")` 送进翻译系统**，所以名字是重映射而不是翻译：
`init -300` 包住 `Character()`，构造一个就改一个，之后再把已经在 store 里的对象
扫一遍。名字表在 `patch/zz_zh_locale.rpy` 的 `ZH_CHARACTER_NAMES` 里，共 124 条。
表达式形式的名字（`[mc_name]`，玩家自己输入的名字）**故意不在表里**——它们必须继续求值。

`docs/glossary.json` 里的角色表是从 shim 的 `ZH_CHARACTER_NAMES` 直接读出来生成的，
两边不会漂。一条 `banned` 都没写：check.py 是纯子串匹配，而这些名字大半同时是普通
中文词（女孩、学生、老师、人群），一封就误伤正文。本游戏姓名的强制点是 shim 里那张表。

## 不要重跑 build_tl.py

**1,790 条**英文原文按上下文该有两种译法：`What?` 回别人的话是「什么？」，重复别人的
话是「怎么了？」；`Great.` 对朋友是「太好了。」，对陌生人是「我很高兴。」。
扁平译文库存不下，重建会把它们全塌缩掉——实测 **2,397 行**正文被改。
`patch/tl/schinese/` 是成品，要改直接改它，改完跑
`python tools/check.py --game portals-04`。

## 这个发行版开不了机

原版发行包**不装补丁也起不来**：`renpy/common/00layout.rpy:124` 调用
`renpy.has_screen()`，而这个发行版里 `renpy` 解析到的是 renpy **包**而不是
`renpy.exports`，直接 `AttributeError`。

shim 第 0 节分两步修：先把包上缺失的导出名从 `renpy.exports` 补齐（`has_screen`
就是这样回来的），再覆盖三个「子模块挡住了导出函数」的名字。不能一把梭全覆盖——
`renpy.main` 要调 `renpy.log.post_init()`，`renpy.bootstrap` 要调
`renpy.error.report_exception()`，早先的全量替换把引擎自己弄坏了。
那三处每一个都单独查过。

**换成原版 Ren'Py 8.2 引擎时把第 0 节删掉。**
