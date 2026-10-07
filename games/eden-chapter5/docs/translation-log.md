# Eden Chapter 5 汉化记录

这一份是**这个游戏**的翻译档案：做了什么、遇到什么、怎么定的。

同目录下的 [`translation-workflow.md`](translation-workflow.md) 记的是这次汉化的
**过程**（引擎的坑、校验器设计陷阱）；安装/卸载/重建步骤见
[本目录的 README](../README.md)。

---

## 概况

| 项 | 数值 |
|---|---|
| 原作 | Eden Chapter 5（FnB Productions） |
| 引擎 | Ren'Py 8.4.1 |
| 目标语言 | 简体中文（`schinese`） |
| 译文条目 | **15,713** |
| 构建应用点 | **34,796**（未译 0） |
| 补丁文件 | 19 个 `.rpy`，共 206,940 行 |
| 角色名牌 | 75 / 75 已译 |
| 译文行宽中位数 | 20 列（对话框上限 130 列） |
| 翻译方式 | 逐条人工撰写，**未使用任何机器翻译或在线翻译 API** |

译文全部存放在 `../data/tl_trans.json`，以英文原文为 key。
`.rpy` 是构建产物，不直接手改。

---

## 术语决策

专名和设定的中文写法登记在 [`glossary.json`](glossary.json)，由 `tools/check.py`
强制执行——登记**禁用译名**，而不只是正确译名，这样后续润色改回别的写法会被拦下。

### 原脚本自己就不统一：`Divinarch` 与 `Celestiarch`

这是本作最容易出错的地方。两个英文词在原脚本里指**同一批存在**（六位飞升者）：

```
There are far more Divinarchs than the Six.
There are six Celestiarchs, each representing one of the Spiritual Energies.
One of the six Divinarchs.  /  One of the six Celestiarchs.
```

初版中文一个翻成「神架构师」、一个翻成「天枢」，于是同一批角色出现了两个名字，
共 10 处。**原脚本用了两个词，不代表它们是两个概念**——光看译文是发现不了的，
得回到英文原文去对照。

最终统一取 **天枢**，理由：

- 用量已经占优（29 处 vs 10 处），改动面小
- 能自然支撑 `光之天枢` / `暗之天枢` / `风之天枢` / `雷霆天枢` 的构词
- 「神架构师」是硬译，读起来别扭

### 术语表全貌

| 英文 | 中文 | 备注 |
|---|---|---|
| Divinarch / Celestiarch | 天枢 | 同物两名，必须统一 |
| Oracle | 神谕者 | 曾误写成「神谕者者」 |
| Circle of Eden | 伊甸之环 | 曾混用「伊甸圆环」 |
| Luminox | 露米诺克斯 | 神祇，全书 161 处 |
| Witch of Darkness | 暗之魔女 | 不译「黑暗魔女」 |
| Time Pocket | 时间口袋 | 不译「时间夹缝」 |
| End of Times | 时间尽头 | 不译「时端」 |
| Wayfarer | 游荡者 | |
| Spiritual Energy | 灵力 | 全书核心概念 |
| Temporia / Thallum / Lunebrook / Brookdale / Meliode | 坦皮奥拉 / 萨勒姆 / 卢恩布鲁克 / 布鲁克代尔 / 梅利奥德 | 地名 |

### 人名

角色名牌 75 个全部已译。有昵称的单独标注在术语表里：

| 英文 | 中文 | 昵称 |
|---|---|---|
| Natasha | 娜塔莎 | 娜塔 |
| Milena | 米莱娜 | 米莉 |

### 刻意不译的内容

这些在译文库里保持原样，`check.py` 有专门规则放行：

- **Patreon 支持者名单**：`Mr. Ovis`、`Bradley Lowe`、`Hesby's femboy factory` 等——
  是真人真名，不该翻
- **镜像倒写的道具文字**：`Nev ereh`、`Nuqien sere?`、`On em sentiende?`——
  剧情伏笔，原样保留
- **第三方模块版权声明**：Kinetic Text Tags / ATL Text Tags 的作者署名
- **按键名与格式串**：`Ctrl`、`Esc`、`%b %d, %H:%M`

---

## 译文层面修过的问题

最后一轮润色修了 22 处：

### 叠字（9 处）

批量替换术语时把「神谕者」写成「神谕者**者**」，散布在
`zz_extra.rpy`、`chapter_four.rpy` 等文件里。

这类错误肉眼读代码很难发现，是靠对全库做叠字扫描抓出来的。合法叠词
（咯咯、谢谢、看看、克拉拉、莉莉）会误报，所以扫描规则最终收窄成
「术语 + 术语末字」这个精确形状。

### 重复否定（1 处）

```
原文： Your people do not seem unhappy…
初版： 你的人民看起来并不不幸福……
修正： 你的人民看起来并不幸福……
```

`不` 打重了。**任何自动检查都只能靠通读发现这种语义错误**——所以那些
超长的 Codex 词条值得人工过一遍。

### 双空格（1 处）

Ren'Py 的许可声明里 `GNU LGPL␣␣Lesser` 有两个空格，顺手规范成
`GNU LGPL（Lesser）通用公共许可证`。

### 术语分裂（11 处）

- `Divinarch` → 「神架构师」改「天枢」，10 处
- `Circle of Eden` → 「伊甸圆环」改「伊甸之环」，1 处

### 缺字形（1 处）

制作人员名单结尾的 `❤️`（U+2764）删掉了。原因是**它本来就显示不出来**：游戏把字体
文件名写死，中文只能走那几个字体名，而补丁用的中文字体——无论是当初从系统里现找的
等线 / 微软雅黑 / 黑体 / 宋体，还是后来打包进来的 MiSans——cmap 里**都没有** U+2764，
连同族的 `♥`(U+2665)、`❣`(U+2763)、`♡`(U+2661) 和四种梅花砖也一个都没有。
能用的只有 `● ■ ★ ☆ ▲` 这类几何图形。

也就是说这不是汉化引入的问题，是原文本里的一个 emoji 在 Ren'Py 的强制字体下必然
变方块。删掉比换个同样缺字形的符号更干净。

> 顺带记一笔：查 cmap 的时候别只看「字体支不支持中文」。中文字体普遍**不含符号区**
> （Geometric Shapes 之外的 Dingbats 基本都是空的），翻译里用到 emoji 是要出事的。

---

## 这个游戏专属的技术注意事项

完整版在[本目录的 README](../README.md#这个游戏特有的三个坑)，这里只列清单：

1. **翻译必须放 `game/tl/schinese/`**，且删掉同名旧 `.rpyc`
2. **`config.language` 会被 `renpy/common/00start.rpy` 重置为 `None`**
   （`init -1600 python hide:`），赋值必须放普通 `init python:` 块
3. **角色名牌是运行时变量**（`$ ravena_name = "Ravena"`），要靠
   `config.say_arguments_callback` 每次 say 之前映射
4. **硬编码了 4 个字体文件名**：`comfortaa.ttf`、`CinzelDecorative.ttf`、
   `MichromaRegular.ttf`、`PacificoRegular.ttf`，记录在
   [`../game.json`](../game.json) 的 `font_shadow` 里
5. **角色名有运行时改写**：`patch/zz_zh_locale.rpy` 里的名字映射表覆盖了
   14 个名字（含 `Witch of Darkness` 这类非人名头衔）
6. **中文字体随补丁分发**：MiSans 放在 `games/eden-chapter5/assets/fonts/`，打包时按游戏硬编码的 5 个字体文件名
   各存一份。机制、体积与授权情况见 [`../../docs/fonts.md`](../../../docs/fonts.md)

### 字体的授权是一个已知并接受的取舍

MiSans 的 name 表里**没有 nameID 13 的授权文本，也没有授权 URL**，copyright 行本身写的是
`All Rights Reserved`。小米官网把它列在「免费商用字体」里，但字体文件自身没有附带任何可再分发的授权声明。

把这样一份文件打进补丁、由补丁分发出去，是有风险的。决定是仍然打包，以免玩家被「自己去找一款中文字体」
骜上堆一个无不可可的问题。缓解措施是：压缩包里放 `FONT-LICENSE.txt`，玩家 README 里署名，让收到的人知道这是什么、来自哪里。
要根除风险，把 `assets/fonts/` 换成 SIL OFL 授权的思源黑体 / Noto Sans CJK 即可，字段结构一个字都不用改。

---

## 验证

每次改动译文后跑这三条，全过才算完成：

```bash
python tools/build_tl.py     # 34,796 / 34,796，0 未译
python tools/check.py        # 7 类检查全过
python tools/selftest.py     # 63 个注入故障全部被拦下
```

`selftest.py` 是 `check.py` 的反向测试。写它是因为有一次术语守卫因为
码位敲错变成了永远匹配不到的字符串，而 `check.py` 一直报「全部通过」——
**一个从未被反向测试验证过的检查项，可能已经悄悄失效很久而没人察觉。**

---

## 版权

游戏版权归 FnB Productions 所有。本目录**不包含**游戏的任何程序文件、
图像、音频或原始脚本（`tl_template/` 已被 `.gitignore` 排除），只包含
翻译补丁与构建工具。与 FnB Productions 无任何关联。
