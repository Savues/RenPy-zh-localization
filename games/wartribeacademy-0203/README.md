# Wartribe Academy 2.0.3 — 简体中文

Ren'Py 视觉小说 **Wartribe Academy 2.0.3**（3 Pood Productions）的完整中文本地化。
全部译文人工逐条撰写，未使用任何机器翻译或在线翻译 API。

| 项目 | 数值 |
|---|---|
| 原引擎版本 | Ren'Py 8.3.4 "Second Star to the Right" |
| 补丁方案 | 脚本覆盖（`patch_layout: script-override`） |
| 可翻译字面量 | 61,417 |
| 已翻译 | **61,294（99.79%）** |
| 去重后中文译文条目 | 53,424 |
| 替换的脚本文件 | 15 个 `.rpy`，181,959 行 |
| 补丁体积 | 5.9 MB 脚本 + 16.0 MB 字体 |

剩余 123 条**故意**保留英文，逐条登记在 [`docs/glossary.json`](docs/glossary.json) 的
`_kept_verbatim`，分四类：Ren'Py 自己的 about 页与按键名、`WartribeAcademy` 存档目录名、
`*GASP*` 形式的舞台指示、以及脚本自己明说「没人听得懂」的部族语。校验脚本会拒绝任何
**没有**登记、又不只是 Ren'Py 变量/标签的未翻译字面量，所以这 123 条是封死的，不是漏网的。

## 这个游戏为什么用脚本覆盖

仓库里有两种打补丁的方式。Eden 和 Sinful Summer 走 Ren'Py 的 `translate` 块：
`data/tl_trans.json` 存英文原文，`tools/build_tl.py` 生成 `game/tl/schinese/`。
**这个游戏走不了那条**，原因写在 [docs/approach.md](docs/approach.md)，一句话版本：

- 发行包**不带** `game/tl/` 翻译模板（只有 `game/tl/None/common.rpym`），没有模板就无法生成翻译块
- 仓库的 `tools/install.py` 只能放三样东西：`game/tl/<lang>/`、`game/<shim>.rpy`、`game/fonts/*`，
  它**无法覆盖游戏自己的脚本**

所以这个补丁直接用中文版 `.rpy` **整体替换**游戏自己的 15 个脚本。`patch/game/` 与游戏的
`game/` 目录一一对应，英文骨架逐行比对通过，启动日志无 error，实机运行确认。

两条路都是仓库认的方案，`game.json` 的 `patch_layout` 声明用哪条，工具链据此分支。

**安装请用 `tools/install.ps1`。** 仓库的 `tools/install.py` 只会摆译文树、`shim`
和字体，顶不掉游戏自己的脚本；对着这个游戏跑它会直接告诉你该用哪个安装器。

## 安装

不需要 Python。

```powershell
# 关掉游戏，然后：
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "D:\Games\WartribeAcademy-2.0.3-pc"
```

或者手动（等价）：

```
patch/game/**            →  <游戏目录>/game/     全部覆盖
patch/zz_zh_locale.rpy   →  <游戏目录>/game/zz_zh_locale.rpy
assets/fonts/*.ttf       →  <游戏目录>/game/fonts/
```

装完启动游戏即可，Ren'Py 首次启动会自动重新编译。**不需要自己装字体**。

安装器会把被覆盖的每个文件先备份到 `game/.zh_patch_backup/`，并且只备份一次 ——
重复安装不会把你的备份冲掉。

## 卸载

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\uninstall.ps1 "D:\Games\WartribeAcademy-2.0.3-pc"
```

逐字节还原英文原版，并清掉重编译产生的字节码。安装时补丁**引入**的文件
（`zz_zh_locale.rpy` 和三个字体）会被直接删除；补丁没有覆盖的文件原样保留。

## 安装器做了什么

1. 15 个中文 `.rpy` 覆盖到 `game/`
2. `zz_zh_locale.rpy` 字体兜底（见下）
3. `MiSans-Regular.ttf` / `MiSans-Bold.ttf` / `DejaVuSans.ttf` 进 `game/fonts/`
4. **删除**有对应 `.rpy` 的陈旧 `.rpyc` / `.rpymc` —— Ren'Py 优先加载 `.rpyc`，
   留着旧的会让中文静默失效。没有对应源文件的孤儿字节码保留不动。

## 字体

游戏自带的字体 `gui/fonts/Nunito-Bold.ttf` 的 cmap 在 `U+3400-U+9FFF` 区间里有
**0 个码位** —— 纯拉丁字体，直接显示中文就是方块。

`patch/game/gui.rpy` 把 `gui.text_font` / `gui.name_text_font` / `gui.interface_text_font`
三个 define 换成一个 FontGroup：MiSans 是默认字体，MiSans 唯一缺的两个码位
（`▸` U+25B8，跳过动画指示符；`♪` U+266A，MUSIC NOTE）回退到 DejaVuSans。


字形覆盖已实测：补丁脚本内 **3,201 个不同非 ASCII 字符，缺字 0 个**。

### 兜底字体为什么还要再兜一层

`gui.rpy` 覆盖的是 `gui.text_font` / `gui.name_text_font` / `gui.interface_text_font`
三个槽位，而 `gui.button_text_font` / `gui.choice_button_text_font` 只是前两者的别名。
万一还有哪个界面硬编码了 `gui/fonts/Nunito-Bold.ttf`，未登记的名字会掉回 Ren'Py 默认字体
DejaVuSans —— 它的 cmap 在同一区间只有 64 个码位，对中文界面等于没有。

所以 `zz_zh_locale.rpy` 把这些拉丁字体名也映射进同一个 FontGroup，堵掉这个洞。

## 回放图鉴：修掉一个原版 bug

原版 `replay_data.rpy` 的 `replay_make_titles` 把**显示名**当成了图片名去拼，
于是每个回放条目都会去找 `<显示名>_gallery` / `<显示名>_replay_bg`，
弹出 `Image 'XXX_gallery' not found`。

补丁把这些条目改成显式的 `(显示名, 资源键)` 元组：显示名随便用中文，图片名仍是原版的
资源键。改动位置在 `tools/verify_patch.cjs` 的 `KEY_CHECKS` 里盯着 ——
`replay title key` 位置一旦出现非 ASCII 就报错。

另外 `leona_locked.webp` **原版就没有**（英文版同样缺）。Leona 有 `leona_gallery`
和 `leona_replay_bg`，唯独没有 `_locked`，所以悬停她的锁定回放卡片会报缺图。
`tools/verify_patch.cjs` 只读本仓库（`patch/`、`data/en_masked/`、`assets/fonts/`、`docs/glossary.json`），**从不读取已安装的游戏目录**，所以它既不能确认也不能否认某个素材存在 —— 校验脚本不会假装自己查过。这条原版缺口只记录在这里和 `game.json` 的 `_known_upstream_gap` 里。

## 维护

- `docs/glossary.json` —— 113 个角色 + 161 条术语，钉死译名防止后续润色改口
- `docs/translation-log.md` —— 翻译记录与逐文件统计
- [docs/approach.md](docs/approach.md) —— 为什么这个游戏偏离仓库标准做法
- `data/en_masked/` —— 英文脚本的**遮蔽骨架**（每个字面量换成 `@S`/`@Q`/`@T3` 标记）
  加一份逐字面量分类 `flags`。骨架里没有一句英文原文，所以校验只凭本仓库就能跑，
  不用再附带一份原作文本
- `tools/verify_patch.cjs` —— 补丁结构自检（已挂在 `game.json` 的 `extra_checks` 上）

### 校验查什么

```bash
node tools/verify_patch.cjs                        # 已挂在 game.json 的 extra_checks 上
python ../../tools/check.py --game wartribeacademy-0203
python ../../tools/selftest.py --game wartribeacademy-0203
```

`verify_patch.cjs` 做四件事，全部基于遮蔽骨架而非通用 linter：

1. **结构对齐** —— 14 个文件与英文骨架**逐行**一致，字面量个数、引号类型、三引号一一对应；
   `gui.rpy` 是唯一允许分歧的文件（三行 font define 被字体接线取代），对它改成
   「切掉该块后仍须与英文版一致」这种更精确的检查
2. **覆盖率** —— 按 `flags` 的 `p` 标记算出 61,294 / 61,417，并核对未译的每一条都在
   `_kept_verbatim` 里登记过
3. **字体覆盖** —— 实际解析三个 `.ttf` 的 cmap，验证 3,201 个非 ASCII 字符都有字形，
   并验证标去 DejaVuSans 的码位 DejaVu 真的有
4. **资源键** —— 中文被误用在 `renpy.image()` 名、`replay_make_titles()` 键位等位置时报警

脚本覆盖真正的风险是「按行号 + 列号定位字面量回写」：中文比英文短，同一行里靠后的
字面量整体左移，再跑一次就写错位置 —— 而这种改动**语法完全合法**，没有任何 linter
看得出来。所以这里不抽查已知枚举，而是拿英文骨架逐行比对。

覆盖率在 `game.json` 的 `coverage` 里是**断言不是推导**，`check.py` 只打印不重算；
真正的覆盖率由上面第 2 条从 `flags` 现算，口径记在 `game.json` 的 `_coverage_note`。

### `replay_data.rpy` 的诚实说明

`replay_data.rpy` 在本补丁存在**之前**就已经就地汉化过了，仓库里没有它的英文原版，
所以它无法参与第 1 条的逐行比对，也不在 61,417 这个统计口径里。
校验脚本每次运行都会**明确打印这一条**，不会假装它被检查过。
字形覆盖和资源键检查对它依然有效。

## 版权

- 原作 **Wartribe Academy** © 3 Pood Productions。本仓库只收录汉化补丁，不含任何原版素材。
- 中文译文为本仓库贡献。
- 字体 MiSans © 2020-2021 北京小米移动软件有限公司；DejaVu Sans 作为两个码位的兜底。
  授权全文见 [assets/fonts/LICENSE-CJK.txt](assets/fonts/LICENSE-CJK.txt)。