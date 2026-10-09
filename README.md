# Ren'Py 游戏中文本地化

Ren'Py（视觉小说）游戏的中文汉化补丁。每个游戏一个独立目录，共用同一套工具链。

本仓库自己写下的每一句译文都由人工逐条撰写，**未使用任何机器翻译或在线翻译 API**。

多数游戏的译文是从英文重译的。有两款不同：表中标 † 的 **That New Teacher** 和
**Between Humanity** 是**发行方自带中文的修订版**——它们的基线是发行方自己随包发布的
中文，本仓库做的是在基线上改错、统一术语和润色，不是从零重译。发行方对这两份基线的
说法也不一样（That New Teacher 标了机翻图标，Between Humanity 自己标 `HUMAN_100`），
两个补丁都照原样记录、各自的 `docs/translation-log.md` 里写清楚，**都不替发行方改口**。

## 已收录

<!-- games:start -->
| 游戏 | 原作 | 语言 | 方案 | 状态 | 译文量 |
|---|---|---|---|---|---|
| [AcademyLive 0.11](games/academylive-011/) | passhonQ | 简体中文 | translate 块 | ✅ 100% | 24,002 条 |
| [Between Humanity 0.3.3](games/between-humanity-033/) | Between Humanity | 简体中文 | 脚本覆盖 † | ✅ 100%（6 条保留原文） | 9,926 条 |
| [City Devil: Restart 0.4.0](games/citydevilrestart-040/) | Sabirow | 简体中文 | 脚本覆盖 | ✅ 100%（10 条保留原文） | 7,792 条 |
| [Clown Squad 0.1 Part 1](games/clownsquad-01-part1/) | Astreon | 简体中文 | translate 块 | ✅ 100% | 5,034 条 |
| [Cosy Cafe 0.14.2](games/cosycafe-0142/) | Cosy Creator | 简体中文 | 脚本覆盖 | ✅ 100% | 32,639 条 |
| [DropOut Saga 0.12.0b](games/dropout-saga-0120/) | LazyBloodLines | 简体中文 | 脚本覆盖 | ✅ 100%（273 条保留原文） | 15,214 条 |
| [Eden Chapter 5](games/eden-chapter5/) | FnB Productions | 简体中文 | translate 块 | ✅ 100% | 15,713 条 |
| [That New Teacher 0.9.0](games/newteacher-090/) | RogueOne | 简体中文 | 脚本覆盖 † | ✅ 100%（123 条保留原文） | 19,112 条 |
| [Por(n)tals 0.4](games/portals-04/) | onehend | 简体中文 | translate 块 | ✅ 100% | 23,910 条 |
| [Realm Invader Episode 2 Part 2](games/realminvader-ep2p2/) | Realm Invader | 简体中文 | translate 块 | ✅ 100% | 16,183 条 |
| [Scions of the Divine 0.1](games/scionsofthedivine-01/) | Dark Seraph Productions | 简体中文 | 脚本覆盖 | ✅ 100% | 5,094 条 |
| [Sinful Summer Chapter 3.6](games/sinfulsummer-chapter36/) | Ruykiru | 简体中文 | translate 块 | ✅ 100% | 22,430 条 |
| [The Inn 1.02.01-2](games/theinn-10201/) | theinn | 简体中文 | translate 块 | ✅ 100% | 5,421 条 |
| [TOXICity 0.22.0](games/toxicity-0220/) | Ils Productions | 简体中文 | 脚本覆盖 | ✅ 100% | 28,524 条 |
| [Wartribe Academy 2.0.3](games/wartribeacademy-0203/) | 3 Pood Productions | 简体中文 | 脚本覆盖 | ⚠️ 123 条未译 | 61,417 条 |
| *（来加一个？）* | | | | | |
<!-- games:end -->

> 覆盖率 = 已译条目 ÷ 全部可译条目。「方案」一列说明这款游戏用哪种方式打补丁：
> `translate 块` 是游戏自带翻译模板时的做法，译文库是**构建输入**，`check.py` 能拿它
> 和英文原文逐条比对，未译条目直接报错。`脚本覆盖` 是游戏压根不带模板时的做法，补丁
> 直接替换游戏自己的脚本——这时没有构建输入可比，覆盖率由 `game.json` 的 `coverage`
> 断言，`check.py` 不再从译文库推导，也**不会**假装能替它判断覆盖率。
>
> 两种都是这个仓库认的方案，不存在哪条是标准、哪条是例外。新游戏选哪条，见
> [`docs/adding-a-game.md`](docs/adding-a-game.md)。
>
> † 方案列带 † 的两款不是重译，是发行方自带中文的修订版。覆盖率的分母是那棵
>
> 上面这张表由 `python tools/games.py --readme` 从 `games/` 生成，两个标记之间的内容不要手改。
> `check_links.py` 会核对它有没有过期。

---

## 下载安装（不需要 Python）

[Releases](https://github.com/Savues/RenPy-zh-localization/releases) 里的压缩包是**直接
覆盖**用的，三步：关掉游戏 → 解压 → 把解压出来的 `game/` 文件夹里的**全部内容**复制到
游戏的 `game/` 文件夹，选择覆盖。不用装 Python，不用跑脚本，不用联网，**也不用自己找
字体**——中文字体已经打进包里了。

包里 `game/` 的内容和游戏的 `game/` 是**一一对应**的，整体复制、选择覆盖即可。
具体对应关系取决于那个游戏用哪种方案：

**`translate 块` 补丁**（多一层 `tl/<lang>/`）：

```
game/tl/schinese/      →  <游戏目录>/game/tl/schinese/
game/zz_zh_locale.rpy  →  <游戏目录>/game/zz_zh_locale.rpy
game/fonts/*           →  <游戏目录>/game/fonts/
```

**`脚本覆盖` 补丁**（直接顶掉游戏自己的 `.rpy`，不多一层）：

```
game/gui.rpy           →  <游戏目录>/game/gui.rpy
game/scripts/*.rpy     →  <游戏目录>/game/scripts/
game/zz_zh_locale.rpy  →  <游戏目录>/game/zz_zh_locale.rpy
game/fonts/*           →  <游戏目录>/game/fonts/
```

差一层目录不会被 Ren'Py 报错，只会**静默忽略**——补丁装上了，游戏还是英文。
所以每个游戏自己的 `README.md` 都写死了它的确切文件清单，别照着别的游戏抄。

`zz_zh_locale.rpy` 是语言与字体补丁，文件名以各游戏 `game.json` 里的 `shim` 为准。
装完直接启动游戏，中文自动启用。完整说明在补丁包内的 `README.md`。

`tools/install.py` 是这件事的自动化版本，适合愿意跑脚本的人，但它只会摆译文树、
`shim` 和字体这三样——**只服务 `installer` 为 `py` 的游戏**。`脚本覆盖` 的补丁要顶掉
游戏自己的脚本，仓库里那个脚本做不了，所以这类游戏自带一个安装器，
`game.json` 的 `installer` 字段写明用哪个（见各游戏的 `README.md`）。

---

## 目录结构

```
RenPy-zh-localization/
├── games/
│   └── <slug>/               ← 每个游戏一个独立目录
│       ├── README.md             该游戏的安装/卸载/重建说明
│       ├── game.json             元数据：方案、装法、覆盖率、字体、额外检查
│       ├── assets/fonts/         随补丁分发的中文字体 + 授权声明
│       ├── data/tl_trans.json    译文数据库（仅 translate 块方案是构建输入）
│       ├── docs/
│       │   ├── glossary.json           术语表，由 check.py 强制执行
│       │   ├── translation-log.md      翻译档案：术语决策与修过的问题
│       │   └── translation-workflow.md 本次汉化的过程存档
│       └── patch/                构建产物，已提交，可直接安装
│           ├── tl/<lang>/           translate 块方案：翻译后的 .rpy
│           ├── game/                脚本覆盖方案：顶掉游戏自己的 .rpy
│           └── <shim>               语言与字体补丁
├── tools/                    共用工具链（与具体游戏无关）
│   ├── install.py  uninstall.py     装 / 卸补丁（只服务 installer=py 的游戏）
│   ├── template.py  build_tl.py     导入模板 / 构建补丁（只服务 translate 块方案）
│   ├── check.py    selftest.py      校验 / 反向验证校验（按方案选检查集）
│   ├── games.py                     列出游戏、按 slug 定位目录
│   ├── package_release.py           生成给玩家用的覆盖安装包（写到 dist/）
│   ├── publish_release.py           把所有游戏的包挂到同一个 GitHub Release
│   ├── check_links.py               检查文档之间的相对链接没断
│   └── tlparse.py                   Ren'Py 翻译模板解析器
└── docs/                      跨游戏复用的说明
    ├── adding-a-game.md         怎么新增一个游戏的汉化
    ├── maintaining.md           维护者流程：发布、推送凭据
    └── fonts.md                 字体机制、换字体、授权情况
```

游戏目录和工具链是分开的：加新游戏只需要在 `games/` 下建一个新文件夹，**不用改任何工具代码**。

---

## 快速上手

```bash
git clone https://github.com/Savues/RenPy-zh-localization.git
cd RenPy-zh-localization

# 安装某个游戏的汉化补丁
python tools/install.py "C:\Games\Eden-Chapter5-pc" --game eden-chapter5
```

装完直接启动游戏，不用在设置里切语言。卸载（注意是同一个目录）：

```bash
python tools/uninstall.py "C:\Games\Eden-Chapter5-pc" --game eden-chapter5
```

每个游戏的具体说明在它自己的目录里。

## 工具链

`--game <slug>` 用来指定操作哪个游戏。仓库里只有一个游戏时可以省略；现在有三个，
`games.py`、`check_links.py`、`publish_release.py` 之外的工具**必须带上**，否则会报错
并列出可用的 slug。

| 命令 | 作用 |
|---|---|
| `python tools/install.py <游戏目录> --game <slug>` | 安装补丁（仅 `installer=py` 的游戏） |
| `python tools/uninstall.py <游戏目录> --game <slug> [--purge-backup]` | 卸载并还原（能读任一安装器写的 manifest） |
| `python tools/template.py <游戏目录> --game <slug>` | 导入英文原文模板（仅首次、仅 translate 块方案） |
| `python tools/build_tl.py --game <slug>` | 由模板 + 译文库重新构建补丁（仅 translate 块方案） |
| `python tools/check.py --game <slug>` | 校验译文库与补丁（按方案选检查集） |
| `python tools/selftest.py --game <slug>` | 反向验证 `check.py` 的每一项检查都会真的报错 |
| `python tools/games.py [--readme]` | 列出仓库里的游戏；`--readme` 重写本文件的「已收录」表格（不需要 `--game`） |
| `python tools/package_release.py --game <slug>` | 生成单个游戏的覆盖安装包（写到 `dist/`，版本号取自 `game.json` 的 `patch_version`） |
| `python tools/publish_release.py [--version v1.0.0] [--dry-run]` | 打包全部游戏并挂到同一个 GitHub Release（不需要 `--game`） |
| `python tools/check_links.py` | 检查文档里的相对链接，以及本文件「已收录」表格有没有过期（不需要 `--game`） |

某个游戏自己的档案都在它目录下的 `docs/` 里。以 Eden Chapter 5 为例：

- [`translation-log.md`](games/eden-chapter5/docs/translation-log.md)——
  术语决策、修过的问题、最终数据
- [`translation-workflow.md`](games/eden-chapter5/docs/translation-workflow.md)——
  这次汉化的过程存档，含 Ren'Py 引擎本身的坑

跨游戏复用的通用说明在 [`docs/`](docs/)：怎么新增一个游戏、字体是怎么解决的、
维护者怎么发版。

改动译文后的流程。后两步所有游戏都一样，第一步看方案：

```bash
# translate 块方案：从模板 + 译文库重建补丁
python tools/build_tl.py --game <slug>

# 脚本覆盖方案：patch/ 里就是成品脚本，改完直接校验

python tools/check.py --game <slug> \
  && python tools/selftest.py --game <slug>
```

对 `脚本覆盖` 的游戏跑 `build_tl.py` 只会得到一句「缺 `tl_template/`」：那个游戏没有
翻译模板可以编译，补丁是直接改写脚本做出来的。

### 校验查什么

`tools/check.py` 按方案选检查集。**两种方案都查**的：

- **乱码** —— U+FFFD 等替换字符
- **重复空格** —— 两个汉字之间多打了一个空格
- **叠字错误** —— 术语多打一个字，例如把「神谕者」写成「神谕者者」
- **术语冲突** —— `docs/glossary.json` 里登记的禁用译名
- **标签不闭合** —— `[i]` `[b]` 等成对标签数量为奇数
- **文件缺失** —— `docs/glossary.json`、语言补丁 `shim`、字体文件不在

**只有 `translate 块` 方案**查的（需要拿译文和英文原文比）：

- **未译条目** —— 值与英文原文完全相同，且又不是变量 / 标签 / 按键名之类必须保留的东西
- **空译文** —— 值是空串或纯空白
- **行宽溢出** —— 按*渲染列宽*算，一个汉字算两列

> **`脚本覆盖` 方案为什么少三项**：它没有译文库可读——`data/tl_trans.json` 是从
> 做完的中文脚本里反向导出来的副产品，拿它检查补丁等于让补丁给自己判卷。剩下三项
> 都得拿英文原文当基准，那种补丁本来就不依赖英文原文（游戏压根没发模板）。这一款
> 游戏自己需要验的东西，写进 `game.json` 的 `extra_checks`（Cosy Cafe 在那里查
> `WeekDays` 枚举有没有被写坏）。

> **行宽为什么按列宽算**：`H-how…` 只有 6 列，翻成「怎、怎么会……」是 12 列——看着涨了一倍，其实一个汉字也就占两列，离对话框容量还差得远。真正会撑破对话框的是长句子，所以豁免了本来就长、且在可滚动面板里显示的文本（比如 Eden 的 Codex 词条）。

> **有意保留英文的字符串**登记在**各游戏自己的** `docs/glossary.json` 的
> `_kept_verbatim` 里，不放在 `check.py` 的公共表里。公共表曾经把三款游戏的例外混在
> 一起，结果一款游戏的字体格式串要靠另外两款游戏的赞助者名单撑着才算合法。

> **`selftest.py` 是干什么的**：一个不会报警的检查等于没有检查。这个命令会**先在
> 干净树上跑一遍**并要求 `check.py` 退出 0（不然注入什么都「成功」，那个数字就没意义
> 了），再往译文库或脚本里逐条注入已知错误，要求每次都以非零码退出，最后把文件
> **逐字节**还原并校验。改阈值或改规则之后跑一次，就知道有没有把哪项检查改瞎了。

---

## 命名

仓库名 `RenPy-zh-localization` 里的 `RenPy` 就是游戏引擎 **Ren'Py** 的官方拼法。正文里始终写完整的 `Ren'Py`（含撇号）；只在仓库名、路径、URL 这些地方才省掉撇号写成 `RenPy`。

## 字体

中文字体打包进补丁里，玩家解压就能用，不用自己去装字体。目前三款游戏都用 MiSans，
但**生效方式**不同，因为它们对字体的要求不一样：

- **Eden Chapter 5** 把中文字体以游戏硬编码的每个文件名各存一份，覆盖原有的西文字体——
  一个游戏 5 份约 25.7 MB，这是 Release 体积的主要来源。
- **Sinful Summer Chapter 3.6** 只放**一份** MiSans（约 7.7 MB），由 `zz_zh_locale.rpy` 注册到
  `renpy.config.font_name_map`。原作为 `FontGroup`：游戏原字体绘它有字形的部分，MiSans 给中文。
  中文能正常显示，拉丁文又保留了原来的字体外观——这是覆盖字体文件做不到的。
- **Cosy Cafe 0.14.2** 同样是 `fallback`，但游戏里的 `[b]` 加粗是空的，得额外带一份
  `MiSans-Bold.ttf` 让粗体有字形可画；两份字体都只放一份，不覆盖任何原文件。

字体机制、怎么换一款、以及 MiSans 的再分发授权情况，详见 [`docs/fonts.md`](docs/fonts.md)。

---

## 版权声明

- 本仓库的**代码与工具链**以 MIT 协议发布，见 [`LICENSE`](LICENSE)。MIT 的适用范围只有
  `tools/` 里的工具链和仓库本身的骨架文件：**不**涉及补丁所针对的那些游戏，也不涉及
  译文所依据的原始脚本与素材——那些仍属各自作者。
- **各游戏本身**的版权归各自作者所有。本仓库**不包含**游戏的任何程序文件、图像、音频或原始脚本；导入用的英文原文（`games/*/tl_template/`）也已被 `.gitignore` 排除。走「脚本覆盖」方案的游戏，`games/*/patch/game/` 里是**被汉化改写过的**脚本（`define`、逻辑、变量名都还在），它们是翻译作品的产物、不是原版的复制品，但一样受各自作者的版权约束。
- `games/*/data/` 与 `games/*/patch/` 属于**同人翻译作品**，仅供学习交流使用。请自行确认当地法律与原作方的授权状况。译文不能整包塞回游戏目录再传给别人。
- 本项目与任何游戏厂商无任何关联。

## 贡献翻译

- 各游戏的翻译档案：`games/<slug>/docs/translation-log.md`（术语、修过的问题）
- 各游戏的流程存档：`games/<slug>/docs/translation-workflow.md`（引擎的坑、校验器设计）
- 新增一个游戏：[`docs/adding-a-game.md`](docs/adding-a-game.md)
- 发版、打包、推送凭据：[`docs/maintaining.md`](docs/maintaining.md)
