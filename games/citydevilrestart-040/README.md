# City Devil: Restart 0.4.0 — 简体中文

- **原作**：Sabirow ｜ **引擎**：Ren'Py 8.3.4
- **译文量**：7,782 / 7,792 条玩家可见文本（99.87%），另有 10 条有意保留原文
- **方案**：脚本覆盖（`script-override`）—— 补丁替换游戏自己的 8 个脚本

City Devil: Restart 把全部 15 个脚本都塞在 `game/archive.rpa` 里，`game/`
目录下原本一个松散的脚本都没有。所以它的"汉化"不是往 `tl/` 里塞 translate 块，
而是**把英文脚本换成中文脚本**：补丁往 `game/` 里放 8 个中文 `.rpy` 加一个字体
接线的 shim。

## 安装

关掉游戏，然后：

~~~powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "D:\Games\CityDevilRestart-0.4.0-pc"
~~~

不需要 Python，不需要联网。

不想用脚本的话，手动做也行——把下面这些复制到 `<游戏目录>\game\`：

| 从 | 到 |
|---|---|
| `patch/game/*.rpy`（8 个文件） | `game/` 同名 |
| `patch/zz_zh_ui.rpy` | `game/zz_zh_ui.rpy` |

然后**为那 8 个 `.rpy` 各建一个同名的空 `.rpyc` 文件**，删掉 `game/cache/`
里的 `bytecode-*.rpyb` 和 `screens.rpyb`，启动游戏。空 `.rpyc` 这一步不能省，
原因见下一节。

## 卸载

~~~powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\uninstall.ps1 "D:\Games\CityDevilRestart-0.4.0-pc"
~~~

## 安装器在做什么，以及为什么需要 .rpyc 影子文件

这是这个游戏最容易装错的地方，值得说清楚。

`archive.rpa` 里每个脚本都有**两份**：`cdr_1.rpy` 和 `cdr_1.rpyc`。Ren'Py 收集
脚本清单时按文件名去重（`renpy/loader.py` 的 `seen` 集合），`game/` 先于
archive 扫描——但去重的键是**完整文件名**，`cdr_1.rpy` 和 `cdr_1.rpyc` 是两个
不同的名字。所以只丢一个松散的 `cdr_1.rpy` 进去，归档里的 `cdr_1.rpyc` 照样会被
加载：脚本清单里于是出现 `("cdr_1", None)`（来自 archive）和 `("cdr_1", "game")`
（来自 game）两条，而 `renpy/script.py` 的去重键是 `(名字, 目录)`，两条都留下，
同一个文件被加载两遍，里面每个 label 都定义两次。

解法是再放一个**空的** `cdr_1.rpyc`。名字被 game 目录占住，归档那份就被跳过；
Ren'Py 随后去读 `.rpyc` 末尾 16 字节的 md5（`script.py` 的
`load_appropriate_file`），空文件读不出来，`try/except` 把它当成"没有摘要"，
于是发现它和 `.rpy` 对不上，改从中文源码重新编译。空文件是刻意的，不是残留。

游戏首次启动会安静地重新编译这 8 个脚本，花一会儿时间，屏幕上没有提示，这是正常的。

## 字体：补丁一个字体都不带

shim 把界面字体指向 `tl/schinese/schinese.ttf` 和 `tl/schinese/schinese2.ttf`。
这两个文件本来就在 `archive.rpa` 里（发行方做官方中文时放的），Ren'Py 找资源先找
`game/` 再找 archive，所以直接就能读到。补丁既不需要复制，也**不应该**复制：
其中 `schinese2.ttf`（平方造字）是商用字体，不在开源许可内，转发它不关这个补丁的事。

所以 `game.json` 里 `font_assets` 是空的，安装器如果发现有字体要装会直接报错退出。

## 语言菜单会怎样

游戏的语言菜单（`游戏菜单 → 语言`）里列了 17 种语言，包括"简体中文"。这个补丁是
脚本覆盖，`_preferences.language` 默认是 `None`，游戏从头到尾跑的就是中文脚本。

如果玩家在菜单里点了别的语言：Ren'Py 会加载 `archive.rpa` 里发行方那套
`tl/<语言>/` 的 translate 块。那些块的 `old` 是英文原文，而现在脚本里已经是中文，
一条都对不上，于是全部落空——**画面不会变**，也不会崩。想切回英文请重装游戏。

这不是补丁的缺陷，是"用脚本覆盖换语言"这条路本身没有语言切换可言。

## 维护

~~~powershell
python tools\check.py --game citydevilrestart-040     # 仓库通用检查
node tools\verify_patch.cjs                            # 本补丁自己的结构自检
~~~

`verify_patch.cjs` 拿英文原版的**遮蔽骨架**逐行比对：每个字符串字面量被换成只记录
引号样式的标记，剩下的纯代码骨架必须和英文版一模一样。它查的东西包括：

- 8 个被替换的脚本，除 `game.json` 里逐行写死的 3 处例外外，骨架必须逐行等于英文版；
- 另外 7 个脚本**不含任何玩家可见文本**——这是"覆盖率里的 7,792 条就是全部"这句话的
  依据，不是谁拍脑袋说的；
- 覆盖率：按 `data/en_masked/*.flags` 逐个字面量算，有意保留原文的必须登记在
  `docs/glossary.json` 的 `_kept_verbatim` 里；
- 资源键位置（`image` / `scene` / `define` / `label` …）不许出现非 ASCII——中文写进
  标识符不会报错，只会让图裂掉；
- 每个被替换的文件都得在 `archive_shadowed` 里登记，否则安装器不会给它补 `.rpyc`。

## 版权

- 原作 © Sabirow。本补丁只包含汉化文本与其接线脚本，不含任何原作美术、音频或
  `archive.rpa` 内的资源。
- 字体沿用发行方随游戏分发的两份（未来圆SC Medium，SIL OFL 1.1；平方造字，商用），
  本仓库不转发它们。
- 原作自带的官方简体中文（`archive.rpa` 里的 `tl/schinese/`）同样不被转发、不被合并；
  本补丁的译文是另一份独立的翻译，与它只有约 1% 的行重合。
