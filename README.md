# Ren'Py 游戏中文本地化

Ren'Py（视觉小说）游戏的中文汉化补丁。每个游戏一个独立目录，共用同一套工具链。

所有译文均由人工逐条撰写，**未使用任何机器翻译或在线翻译 API**。

## 已收录

| 游戏 | 原作 | 语言 | 状态 | 译文量 |
|---|---|---|---|---|
| [Eden Chapter 5](games/eden-chapter5/) | FnB Productions | 简体中文 | ✅ 100% | 15,713 条 |
| [Sinful Summer Chapter 3.6](games/sinfulsummer-chapter36/) | Ruykiru | 简体中文 | ✅ 100% | 22,430 条 |
| *（来加一个？）* | | | | |

> 覆盖率 = 已译条目 ÷ 全部可译条目。`check.py` 会强制要求 100%，未译条目直接报错。

---

## 下载安装（不需要 Python）

[Releases](https://github.com/Savues/RenPy-zh-localization/releases) 里的压缩包是**直接
覆盖**用的，三步：关掉游戏 → 解压 → 把解压出来的 `game/` 文件夹里的**全部内容**复制到
游戏的 `game/` 文件夹，选择覆盖。不用装 Python，不用跑脚本，不用联网，**也不用自己找
字体**——中文字体已经打进包里了。

```
game/tl/schinese/      →  <游戏目录>/game/tl/schinese/
game/zz_zh_locale.rpy  →  <游戏目录>/game/zz_zh_locale.rpy
game/fonts/*           →  <游戏目录>/game/fonts/
```

中间那个 `zz_zh_locale.rpy` 是语言与字体补丁，文件名以各游戏 `game.json` 里的 `shim`
为准。每个游戏自己的 `README.md` 写明了它的确切文件清单。

装完直接启动游戏，中文自动启用。完整说明在补丁包内的 `README.md`。

仓库里的 `tools/install.py` 是同一件事的自动化版本，适合愿意跑脚本的人。
两者装出来的东西完全一样。

---

## 目录结构

```
RenPy-zh-localization/
├── games/
│   └── <slug>/               ← 每个游戏一个独立目录
│       ├── README.md             该游戏的安装/卸载/重建说明
│       ├── game.json             元数据：引擎版本、语言、字体方案、要带的字体文件
│       ├── assets/fonts/         随补丁分发的中文字体 + 授权声明
│       ├── data/tl_trans.json    译文数据库（以英文原文为 key）
│       ├── docs/
│       │   ├── glossary.json           术语表，由 check.py 强制执行
│       │   ├── translation-log.md      翻译档案：术语决策与修过的问题
│       │   └── translation-workflow.md 本次汉化的过程存档
│       └── patch/                构建产物，已提交，可直接安装
│           ├── tl/<lang>/           翻译后的 .rpy
│           └── <shim>               语言与字体补丁
├── tools/                    共用工具链（与具体游戏无关）
│   ├── install.py  uninstall.py     装 / 卸补丁
│   ├── template.py  build_tl.py     导入模板 / 构建补丁
│   ├── check.py    selftest.py      校验 / 反向验证校验
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

`--game <slug>` 用来指定操作哪个游戏。仓库里只有一个游戏时可以省略；现在有两个，
`games.py`、`check_links.py`、`publish_release.py` 之外的工具**必须带上**，否则会报错
并列出可用的 slug。

| 命令 | 作用 |
|---|---|
| `python tools/install.py <游戏目录> --game <slug>` | 安装补丁 |
| `python tools/uninstall.py <游戏目录> --game <slug> [--purge-backup]` | 卸载并还原 |
| `python tools/template.py <游戏目录> --game <slug>` | 导入英文原文模板（仅首次） |
| `python tools/build_tl.py --game <slug>` | 由模板 + 译文库重新构建补丁 |
| `python tools/check.py --game <slug>` | 校验译文库与补丁 |
| `python tools/selftest.py --game <slug>` | 反向验证 `check.py` 的每一项检查都会真的报错 |
| `python tools/games.py` | 列出仓库里的游戏（不需要 `--game`） |
| `python tools/package_release.py --game <slug> [--version v1.0.0]` | 生成单个游戏的覆盖安装包（写到 `dist/`） |
| `python tools/publish_release.py [--version v1.0.0] [--dry-run]` | 打包全部游戏并挂到同一个 GitHub Release（不需要 `--game`） |
| `python tools/check_links.py` | 检查文档之间的相对链接没断（不需要 `--game`） |

某个游戏自己的档案都在它目录下的 `docs/` 里。以 Eden Chapter 5 为例：

- [`translation-log.md`](games/eden-chapter5/docs/translation-log.md)——
  术语决策、修过的问题、最终数据
- [`translation-workflow.md`](games/eden-chapter5/docs/translation-workflow.md)——
  这次汉化的过程存档，含 Ren'Py 引擎本身的坑

跨游戏复用的通用说明在 [`docs/`](docs/)：怎么新增一个游戏、字体是怎么解决的、
维护者怎么发版。

改动译文后的标准流程：

```bash
python tools/build_tl.py --game <slug> \
  && python tools/check.py --game <slug> \
  && python tools/selftest.py --game <slug>
```

### 校验查什么

`tools/check.py` 覆盖九类问题：

- **未译条目** —— 值与英文原文完全相同，且又不是变量 / 标签 / 按键名之类必须保留的东西
- **空译文** —— 值是空串或纯空白
- **乱码** —— U+FFFD 等替换字符
- **重复空格** —— 两个汉字之间多打了一个空格
- **叠字错误** —— 术语多打一个字，例如把「神谕者」写成「神谕者者」
- **术语冲突** —— `docs/glossary.json` 里登记的禁用译名
- **行宽溢出** —— 按*渲染列宽*算，一个汉字算两列
- **标签不闭合** —— `[i]` `[b]` 等成对标签数量为奇数
- **文件缺失** —— `docs/glossary.json` 或语言补丁 `shim` 不在

> **行宽为什么按列宽算**：`H-how…` 只有 6 列，翻成「怎、怎么会……」是 12 列——看着涨了一倍，其实一个汉字也就占两列，离对话框容量还差得远。真正会撑破对话框的是长句子，所以豁免了本来就长、且在可滚动面板里显示的文本（比如 Eden 的 Codex 词条）。

> **`selftest.py` 是干什么的**：一个不会报警的检查等于没有检查。这个命令会往译文库里逐条注入已知错误，要求 `check.py` 每次都以非零码退出，最后再把数据库**逐字节**还原并校验。改阈值或改规则之后跑一次，就知道有没有把哪项检查改瞎了。

---

## 命名

仓库名 `RenPy-zh-localization` 里的 `RenPy` 就是游戏引擎 **Ren'Py** 的官方拼法。正文里始终写完整的 `Ren'Py`（含撇号）；只在仓库名、路径、URL 这些地方才省掉撇号写成 `RenPy`。

## 字体

中文字体打包进补丁里，玩家解压就能用，不用自己去装字体。目前两款游戏都用 MiSans，
但**生效方式**不同，因为它们对字体的要求不一样：

- **Eden Chapter 5** 把中文字体以游戏硬编码的每个文件名各存一份，覆盖原有的西文字体——
  一个游戏 5 份约 25.7 MB，这是 Release 体积的主要来源。
- **Sinful Summer Chapter 3.6** 只放**一份** MiSans（约 7.7 MB），由 `zz_zh_locale.rpy` 注册到
  `renpy.config.font_name_map`。原作为 `FontGroup`：游戏原字体绘它有字形的部分，MiSans 给中文。
  中文能正常显示，拉丁文又保留了原来的字体外观——这是覆盖字体文件做不到的。

字体机制、怎么换一款、以及 MiSans 的再分发授权情况，详见 [`docs/fonts.md`](docs/fonts.md)。

---

## 版权声明

- 本仓库的**代码与工具链**以 MIT 协议发布，见 [`LICENSE`](LICENSE)。
- **各游戏本身**的版权归各自作者所有。本仓库**不包含**游戏的任何程序文件、图像、音频或原始脚本；导入用的英文原文（`games/*/tl_template/`）也已被 `.gitignore` 排除。
- `games/*/data/` 与 `games/*/patch/` 属于**同人翻译作品**，仅供学习交流使用。请自行确认当地法律与原作方的授权状况。译文不能整包塞回游戏目录再传给别人。
- 本项目与任何游戏厂商无任何关联。

## 贡献翻译

- 各游戏的翻译档案：`games/<slug>/docs/translation-log.md`（术语、修过的问题）
- 各游戏的流程存档：`games/<slug>/docs/translation-workflow.md`（引擎的坑、校验器设计）
- 新增一个游戏：[`docs/adding-a-game.md`](docs/adding-a-game.md)
- 发版、打包、推送凭据：[`docs/maintaining.md`](docs/maintaining.md)
