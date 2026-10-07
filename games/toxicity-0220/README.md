# TOXICity 0.22.0 — 简体中文（含 Gugatron Mod）

Ren'Py 视觉小说 **TOXICity 0.22.0** 的完整中文本地化，并**一并收录 Gugatron Mod**。
全部译文人工逐条撰写，未使用任何机器翻译或在线翻译 API。

| 项目 | 数值 |
|---|---|
| 原引擎版本 | Ren'Py **7.4.5**（注意不是 8.x） |
| 含中文的字面量 | 28,524 |
| 剧情类 | 27,150 句，100% |
| `data/tl_trans.json` 去重条目 | 25,300 |
| 出货 `.rpy` | 17 个，57,796 行 |
| 补丁体积 | 3.75 MB 脚本 + 15.29 MB 字体 |
| 内置 Mod | GugatronCheats / GugatronUnlock / mod.rpy（已汉化） |

---

## 这个补丁做了什么

**1. 汉化游戏本体。** 主线、五个角色的个人线、支线、图鉴、成就、
菜单、日期标题卡全部中文化。

**2. 收录并汉化 Gugatron Mod。** 这是本作原本没有的内容，
补丁把 Mod 的三个脚本一并带上（`patch/game/mod/`），
并在 `screens.rpy` 的快速菜单里加了一个 **作弊** 按钮。

> ⚠️ Mod 会往存档里写解锁标记。想完全还原成没装 Mod 的状态，
> 见下面的「卸载」—— `uninstall.ps1` 会逐字节还原。

**3. 换字体。** 把界面的微软雅黑换成 MiSans（真 Bold 字重，不是合成粗体）。
**不覆盖任何字体文件**，详见下面的「字体」。

---

## 安装

**不需要 Python，不需要联网，不用自己找字体。** 三步：

1. **完全关闭**游戏（托盘里也要退干净）
2. 解压补丁
3. 把 `game` 文件夹里的**全部内容**复制到游戏的 `game` 文件夹，选择**覆盖**

```
要复制的东西                复制到哪里
game/*.rpy                  →  <游戏目录>/game/
game/mod/*.rpy              →  <游戏目录>/game/mod/
game/zzz_font_misans.rpy    →  <游戏目录>/game/
game/fonts/*.ttf           →  <游戏目录>/game/fonts/
```

或者用自带的安装脚本（会自动备份被覆盖的文件）：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "D:\Games\TOXICity-0.22.0-pc"
```

> **请用 `tools/install.ps1`，不要用仓库根目录的 `tools/install.py`。**
> 原因见 [docs/approach.md](docs/approach.md)：这个补丁是整体替换游戏脚本，
> 而 `install.py` 只能放 `game/tl/<lang>/`、shim 和字体，放不下。

装完直接启动，Ren'Py 首次启动会自动重新编译。

### 安装器做了什么

1. 16 个中文 `.rpy` 覆盖到 `game/`
2. `zzz_font_misans.rpy` 字体接管脚本
3. `MiSans-Regular.ttf` / `MiSans-Bold.ttf` 进 `game/fonts/`
4. **删除**有对应 `.rpy` 的陈旧 `.rpyc` —— Ren'Py 优先加载 `.rpyc`，
   留着旧的会让中文**静默失效**。没有对应源文件的孤儿字节码保留不动。
5. 备份到 `game/.zh_patch_backup/`，只备份一次，重复安装不会冲掉备份

---

## 卸载

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\uninstall.ps1 "D:\Games\TOXICity-0.22.0-pc"
```

逐字节还原英文原版，清掉重编译产生的字节码，并删掉补丁自带的
`zzz_font_misans.rpy`、Mod 脚本和 MiSans 字体。
Mod 的 `game/mod/images/`、`GugaTablet.png` 等**原版就有的素材原样保留** ——
补丁只碰 `.rpy`，不碰图片。

---

## 字体

**和这个仓库里另外两款游戏不一样，TOXICity 的字体策略是「什么都不覆盖」。**

原作 `game/fonts/msyh.ttc`（微软雅黑）本身就带完整中文字形，
**装补丁之前中文就已经能正常显示**。MiSans 是排印升级，不是补方块。

所以补丁不覆盖任何字体文件，而是在启动时改写字体请求：

| 原本请求 | 次数 | 接管后 |
|---|---|---|
| `fonts/msyh.ttc` | 291 处 | `fonts/MiSans-Regular.ttf` |
| `fonts/msyh.ttc`（粗体） | 约 90 处 `<b>` | `fonts/MiSans-Bold.ttf` |
| `fonts/DCC - Ash.otf` | 5 处 | MiSans |
| `mod/Monster Racing - Personal Used.otf` | Mod 装饰字体 | MiSans |

后两款是 Mod 带来的装饰字体，各只有一百多个码位、**完全不含中文**，
不接管的话 Mod 界面会全是豆腐块。

**把 `game/fonts/*.ttf` 删掉游戏照样能跑** —— 接管脚本会检测字体是否存在，
缺了就整体跳过，字体回落成微软雅黑。想切回去也可以，
把 `zzz_font_misans.rpy` 里的 `ZH_FONT_USE_MISANS` 改成 `False`。

字形覆盖已实测：译文用到 2,956 个非 ASCII 字符，MiSans 命中 2,955 个
（唯一未覆盖的是 U+FEFF 零宽字符），零豆腐块。

字体授权见 [assets/fonts/LICENSE-MiSans.txt](assets/fonts/LICENSE-MiSans.txt)。

---

## 可选：Mod 的存档页覆盖

`patch/optional/Save_Name.rpy` 是 Mod 包里附带的 Ren'Py 存档页替换
（重写了 `FilePage`，会顶掉引擎自带的存档分页，并加一个文件名输入）。

**实测这个游戏用不到它**，所以安装器不会自动装。想试的话：

```powershell
Copy-Item patch\optional\Save_Name.rpy "<游戏目录>\game\Save_Name.rpy" -Force
```

删掉该文件即可还原。

---

## 这个游戏特有的坑

给以后接手的人：

1. **Ren'Py 是 7.4.5，不是 8.x。** `renpy.loadable()` 和
   `config.font_replacement_map` 在 7.4.5 里都有，但
   `renpy.loader.loadable` 是 8.x 的写法 —— **不要照抄 Cosy Cafe 的 shim**。
2. **原版自带中文字体和中文角色名。** `define_default.rpy` 里
   `define k = Character("卡莉")`，`options.rpy` 里有 `_()` 包装 ——
   但游戏**从没启用过**翻译系统，`game/tl/` 是空的。别被 `_()` 误导。
3. **Mod 会往 `script*.rpy` 里插剧情。** 以后 Mod 更新了，
   别拿英文重译，按 [docs/approach.md](docs/approach.md) 里的 diff 移植流程走。
4. **`screens.rpy` 第 267 行的「作弊」按钮是补丁加的**，原版没有。
   更新游戏时这个插入点会失效，要重新对位。
5. **`scenes_harem.rpy` 第 17 章曾经整段错位一格**（每行装的是下一行的译文），
   结构完全正常、任何 diff 校验都发现不了。现已修复，
   详见 [docs/approach.md](docs/approach.md#校验时发现的四个真实缺陷)。
   以后改这个文件请跑一遍内容层校验。

---

## 维护

- `data/tl_trans.json` —— 25,300 条去重的英文原文 → 中文映射。
  **事后从成品脚本反推生成**，和 `patch/game/` 里的实际文字永远一致。
  改译文请直接改 `patch/` 下的 `.rpy`，再重新生成数据库。
- `docs/glossary.json` —— 角色名、数值标签、场所。
  `banned` 列表会在 `check.py` 里被强制执行，防止以后润色改口。
- `docs/translation-log.md` —— 翻译档案与风格说明
- [docs/approach.md](docs/approach.md) —— 为什么偏离仓库标准做法，以及校验时发现的缺陷
- `patch/optional/Save_Name.rpy` —— 不自动安装的可选文件

校验：

```bash
python tools/check.py --game toxicity-0220
```

---

## 版权

- 原作 **TOXICity** © Ils Productions。本仓库只收录汉化补丁，不含任何原版素材。
- **Gugatron Mod** 为第三方 Mod，其著作权归原作者所有。
  本仓库提供的是该 Mod 的**中文翻译**，不主张对 Mod 本体的任何权利。
- 中文译文为本仓库贡献。
- 字体 MiSans © 2020-2021 北京小米移动软件有限公司。

请勿将本补丁与游戏本体一同分发。
