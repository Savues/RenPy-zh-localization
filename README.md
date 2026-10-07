# 第三方的 Ren'Py 汉化补丁仓库

本仓库收录 Ren'Py 游戏的**中文汉化补丁**。目前收录：

| 游戏 | 语言 | 状态 |
|---|---|---|
| **Eden Chapter 5** (FnB Productions) | 简体中文 | ✅ 100%（15,713 条） |

所有译文均由人工逐条撰写，**未使用任何机器翻译或在线翻译 API**。

---

## 命名

仓库名 `RenPy-zh-localization` 里的 `RenPy` 就是游戏引擎 **Ren’Py** 的官方拼法。正文里始终写完整的 `Ren’Py`（含撇号）；只在仓库名、路径、URL 这些地方才省掉撇号写成 `RenPy`。

## 目录结构

```
data/tl_trans.json     译文数据库：以英文原文为 key 的 JSON
patch/                 可直接安装的补丁产物（构建产物，已提交）
  tl/schinese/           翻译后的 Ren'Py 脚本（19 个 .rpy）
  zz_zh_locale.rpy       语言与字体补丁
tools/                构建与安装工具链
docs/glossary.json     术语表（check.py 强制执行）
fonts/                字体放置目录（不放二进制，见下）
tl_template/          英文原文模板（本地生成，不提交）
```

---

## 安装补丁

下载或克隆本仓库，然后：

```bash
python tools/install.py "C:\Games\Eden-Chapter5-pc"
```

脚本会：

1. 把 `patch/tl/schinese` 写入游戏的 `game/tl/schinese`
2. 写入 `game/zz_zh_locale.rpy`
3. 找一款系统中文字体，写入 `game/fonts/`，并覆盖游戏硬编码的 4 个字体文件名
4. 把所有被覆盖的原始文件备份到 `game/.zh_patch_backup/`

装完直接启动游戏即可，**不需要**在设置里切换语言——补丁会在启动时强制启用简体中文。

指定字体：

```bash
python tools/install.py "C:\Games\Eden-Chapter5-pc" --font "C:\Windows\Fonts\msyh.ttc"
```

## 卸载补丁

```bash
python tools/uninstall.py "C:\Games\Eden-Chapter5-pc"
```

会从备份原样还原被覆盖的文件。确认无误后加 `--purge-backup` 一并删掉备份目录。

---

## 从源码重建

译文改动后重新构建补丁：

```bash
python tools/template.py "C:\Games\Eden-Chapter5-pc"   # 仅首次：导入英文模板
python tools/build_tl.py                                # 生成 patch/tl/schinese
python tools/check.py                                   # 校验
```

`tools/build_tl.py` 只做一件事：读 `tl_template/` 的英文模板，把 `data/tl_trans.json` 里对应的中文填回去。它不会改动任何结构性的东西，所以重建结果一定是可复现的。

### 校验都查什么

`tools/check.py` 是发布前的关卡，目前覆盖：

- **重复翻译键** —— Ren'Py 在启动时遇到重复会直接抛异常崩溃
- **未译条目** —— 值与英文原文完全相同、且又不是变量 / 标签 / 按键名之类必须保留的东西
- **乱码** —— U+FFFD 等替换字符
- **叠字错误** —— 例如把「神谕者」写成「神谕者者」
- **术语冲突** —— `docs/glossary.json` 里登记的禁用译名
- **行宽溢出** —— 按*渲染列宽*（一个汉字算两列）算，而不是字符数
- **叠字错误** —— 术语被多打一个字，例如把「神谕者」写成「神谕者者」
- **标签不闭合** —— `[i]` `[b]` 等成对标签数量为奇数

> 行宽检查为什么按列宽：`H-how…` 只有 6 列，翻成「怎、怎么会……」是 12 列——看着涨了一倍，其实一个汉字也就占两列，离对话框的容量还差得远。真正会撑破对话框的是长句子，所以豁免了 Codex 词条这类本来就长、且在可滚动面板里显示的文本。

---

## 关于字体

`fonts/` 目录**不提交任何字体文件**。原因很简单：微软雅黑、等线这些中文字体是**微软的专有字体**，没有再分发授权，放进公开仓库会带来版权问题。

`tools/install.py` 的做法是：先找 `fonts/zh.ttf`，找不到就在系统字体目录里挑一款能显示中文的（微软雅黑 → 黑体 → 苹方 → 思源黑体 / Noto Sans CJK → 文泉驿）。**绝大多数系统都自带一款**，所以大多数用户什么都不用做。

想固定使用某一款字体，把文件放到 `fonts/zh.ttf` 即可（注意该文件需要你自己确认再分发授权）。

> 为什么覆盖字体**文件名**而不是改游戏配置：游戏脚本里到处硬编码了 `comfortaa.ttf`、`CinzelDecorative.ttf`、`MichromaRegular.ttf`、`PacificoRegular.ttf` 这四个名字，包括 `{font=...}` 标签和各个界面样式。在磁盘上用中文字体覆盖同名文件，是唯一能一次性覆盖所有这些引用、且不改动游戏脚本的做法。

---

## 版权声明

- 本仓库的**代码与工具链**以 MIT 协议发布，见 [`LICENSE`](LICENSE)。
- **游戏本身**（Eden Chapter 5）的版权归 FnB Productions 所有。本仓库**不包含**游戏的任何程序文件、图像、音频或原始脚本。
- `data/tl_trans.json` 与 `patch/` 属于**同人翻译作品**，仅供学习交流使用。请先自行确认当地法律与原作方的授权状况。
- 本项目与 FnB Productions 无任何关联。

---

## 贡献翻译

1. 从 `data/tl_trans.json` 里挑一个英文原文当 key，写上中文，写回同一个文件。
2. **不要**翻译这些（校验器会拦住）：
   - Ren'Py 变量与标签：`[playername]`、`{size=32}`、`{#filetime}%A, %B`
   - 按键名与格式串：`Ctrl`、`Esc`、`%b %d, %H:%M`
   - URL 与文件路径
   - 括号、花括号内的样式标记
3. 新术语请登记到 `docs/glossary.json`，否则可能被后续的润色轮次改回别的译法。
4. 跑下面三条命令，全过再提 PR：

```bash
python tools/build_tl.py     # 重新生成补丁
python tools/check.py        # 校验译文
python tools/selftest.py     # 反向验证：确保上面每一项检查都真的会报错
```

`selftest.py` 是给 `check.py` 做的反向测试。它会往数据库里逐条注入已知错误
（错误术语、叠字、乱码、超宽、空译文……），要求 `check.py` 每次都以非零码退出，
最后再把数据库**逐字节**还原并校验。

> 一个不会报警的检查等于没有检查。这条命令存在的意义，是让「检查项失效」这件事
> 本身变成可检测的——改阈值或改规则之后跑一次，就知道有没有把哪项检查改瞎了。
