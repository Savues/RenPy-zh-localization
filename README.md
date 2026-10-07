# Ren'Py 游戏中文本地化

Ren'Py（视觉小说）游戏的中文汉化补丁。每个游戏一个独立目录，共用同一套工具链。

所有译文均由人工逐条撰写，**未使用任何机器翻译或在线翻译 API**。

## 已收录

| 游戏 | 原作 | 语言 | 状态 | 译文量 |
|---|---|---|---|---|
| [Eden Chapter 5](games/eden-chapter5/) | FnB Productions | 简体中文 | ✅ 100% | 15,713 条 |
| *（来加一个？）* | | | | |

> 覆盖率 = 已译条目 ÷ 全部可译条目。`check.py` 会强制要求 100%，未译条目直接报错。

---

## 目录结构

```
RenPy-zh-localization/
├── games/
│   └── eden-chapter5/        ← 每个游戏一个独立目录
│       ├── README.md             该游戏的安装/卸载/重建说明
│       ├── game.json             元数据：引擎版本、语言、要覆盖的字体文件名
│       ├── data/tl_trans.json    译文数据库（以英文原文为 key）
│       ├── docs/glossary.json    术语表，由 check.py 强制执行
│       ├── patch/                构建产物，已提交，可直接安装
│       │   ├── tl/schinese/         翻译后的 .rpy
│       │   └── zz_zh_locale.rpy     语言与字体补丁
│       └── tl_template/        英文原文模板（本地生成，不提交）
├── tools/                    共用工具链（与具体游戏无关）
│   ├── install.py  uninstall.py     装 / 卸补丁
│   ├── template.py  build_tl.py     导入模板 / 构建补丁
│   ├── check.py    selftest.py      校验 / 反向验证校验
│   ├── games.py                     按 slug 定位游戏目录
│   └── tlparse.py                   Ren'Py 翻译模板解析器
└── docs/
    ├── translation-workflow.md  汉化流程 + Ren'Py 引擎的坑（必读）
    ├── adding-a-game.md         怎么新增一个游戏的汉化
    └── fonts.md                 中文字体为什么不放进仓库
```

游戏目录和工具链是分开的：加新游戏只需要在 `games/` 下建一个新文件夹，**不用改任何工具代码**。

---

## 快速上手

```bash
git clone https://github.com/Savues/RenPy-zh-localization.git
cd RenPy-zh-localization

# 安装某个游戏的汉化补丁
python tools/install.py "C:\Games\Eden-Chapter5-pc"
```

装完直接启动游戏，不用在设置里切语言。卸载：

```bash
python tools/uninstall.py "C:\Games\Eden5-pc"
```

每个游戏的具体说明在它自己的目录里。

## 工具链

所有工具都接受可选的 `--game <slug>`。仓库里只有一个游戏时可以省略。

| 命令 | 作用 |
|---|---|
| `python tools/install.py <游戏目录> [--game <slug>]` | 安装补丁 |
| `python tools/uninstall.py <游戏目录> [--purge-backup]` | 卸载并还原 |
| `python tools/template.py <游戏目录>` | 导入英文原文模板（仅首次） |
| `python tools/build_tl.py` | 由模板 + 译文库重新构建补丁 |
| `python tools/check.py` | 校验译文库与补丁 |
| `python tools/selftest.py` | 反向验证 `check.py` 的每一项检查都会真的报错 |
| `python tools/games.py` | 列出仓库里的游戏 |
| `python tools/check_links.py` | 检查文档之间的相对链接没断 |

想了解整个流程、Ren'Py 引擎本身的坑，以及校验器是怎么被自己的误报逼出来的，
看 [`docs/translation-workflow.md`](docs/translation-workflow.md)。

改动译文后的标准流程：

```bash
python tools/build_tl.py && python tools/check.py && python tools/selftest.py
```

### 校验查什么

`tools/check.py` 覆盖七类问题：

- **重复翻译键** —— Ren'Py 遇到重复会在启动时直接抛异常崩溃
- **未译条目** —— 值与英文原文完全相同，且又不是变量 / 标签 / 按键名之类必须保留的东西
- **乱码** —— U+FFFD 等替换字符
- **叠字错误** —— 术语多打一个字，例如把「神谕者」写成「神谕者者」
- **术语冲突** —— `docs/glossary.json` 里登记的禁用译名
- **行宽溢出** —— 按*渲染列宽*算，一个汉字算两列
- **标签不闭合** —— `[i]` `[b]` 等成对标签数量为奇数

> **行宽为什么按列宽算**：`H-how…` 只有 6 列，翻成「怎、怎么会……」是 12 列——看着涨了一倍，其实一个汉字也就占两列，离对话框容量还差得远。真正会撑破对话框的是长句子，所以豁免了 Codex 词条这类本来就长、且在可滚动面板里显示的文本。

> **`selftest.py` 是干什么的**：一个不会报警的检查等于没有检查。这个命令会往译文库里逐条注入已知错误，要求 `check.py` 每次都以非零码退出，最后再把数据库**逐字节**还原并校验。改阈值或改规则之后跑一次，就知道有没有把哪项检查改瞎了。

---

## 命名

仓库名 `RenPy-zh-localization` 里的 `RenPy` 就是游戏引擎 **Ren'Py** 的官方拼法。正文里始终写完整的 `Ren'Py`（含撇号）；只在仓库名、路径、URL 这些地方才省掉撇号写成 `RenPy`。

## 字体

仓库**不放任何字体文件**，原因是版权和体积：微软雅黑、等线是微软的专有字体没有再分发授权；开源的思源黑体单个就 15–20 MB。`install.py` 改为在用户机器上现找一款能显示中文的。详见 [`docs/fonts.md`](docs/fonts.md)。

---

## 版权声明

- 本仓库的**代码与工具链**以 MIT 协议发布，见 [`LICENSE`](LICENSE)。
- **各游戏本身**的版权归各自作者所有。本仓库**不包含**游戏的任何程序文件、图像、音频或原始脚本；`tl_template/` 已被 `.gitignore` 排除。
- `games/*/data/` 与 `games/*/patch/` 属于**同人翻译作品**，仅供学习交流使用。请自行确认当地法律与原作方的授权状况。
- 本项目与任何游戏厂商无任何关联。

## 贡献翻译

- 流程与引擎注意事项：[`docs/translation-workflow.md`](docs/translation-workflow.md)
- 术语约定：[Eden Chapter 5 的 README](games/eden-chapter5/README.md#术语表约定)
- 新增一个游戏：[`docs/adding-a-game.md`](docs/adding-a-game.md)

### 推送凭据

这台机器没装 Git Credential Manager，所以把凭据交给 git 自带的 `store`
helper，并落到**仓库外**的独立文件：

```bash
git config --global credential.helper "store --file=$HOME/.renpy-zh-credentials"

printf 'protocol=https
host=github.com
username=x-access-token
password=<TOKEN>

' \
  | git credential approve
```

之后 `git push` 直接可用，token 不必再出现在命令行里。

> `store` helper 是**明文**存储的。它比写进 `.git/config` 或每次命令行参数
> 干净一点（仓库里查不到、命令历史里查不到），但仍然不是加密存储。Windows 上
> 如果能用 Git Credential Manager 或 WinCred，优先用它们——凭据会进系统凭据库。
> 详见仓库根目录下的 `.renpy-zh-credentials` 是否存在，以及 `git config
> --global --unset credential.helper` 如何撤销。
