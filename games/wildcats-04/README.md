# WildCats 0.4 — 多功能模组中文汉化版 (BladeSSR Multi-Mod)

《WildCats》0.4 版本的综合辅助模组（Multi-Mod），基于原作者 **BladeSSR** 的模组二次开发汉化与适配，完全兼容游戏官方中文语言。

| 项目 | 数值 |
|---|---|
| 原引擎版本 | Ren'Py 8.2.0 |
| 补丁方案 | 脚本覆盖（`patch_layout: script-override`） |
| 模组内容 | 作弊菜单（Cheat Menu）+ 选项攻略提示（Walkthrough Hints） |
| 可翻译选项与词条 | 150 |
| 已翻译 | **150（100%）** |
| 字体方案 | 继承游戏客户端官方中文字体（LXGW WenKai / FZLB / chinafont） |

## 模组功能特性

1. **选项攻略提示（Walkthrough Hints）**
   - 提取自游戏官方中文语言包，选项无论是中文还是英文均能自动匹配。
   - 选项后附加好感度增减、心情变化、恋爱/知己分支路线、坏结局预警、特殊剧情(H)及彩蛋提示。
   - 完美适配长选项文本与紧凑模式，支持直接在作弊菜单中一键开/关。

2. **作弊菜单（Cheat Menu）**
   - 呼出方式：底栏快捷菜单中的“作弊”按钮，或全局快捷键 `Alt + C`。
   - **角色好感与状态**：单独或一键调整角色好感（支持最大值）、关系状态（相识/知己/浪漫），数据与个人资料档案双向同步。
   - **剧情与全局解锁**：调整伊芙心情（Eve Mood）、一键解锁/恢复全 CG 画廊回忆、一键解锁/恢复全角色自拍照片。
   - **场景旗标**：各角色特殊剧情判定旗标开关。

## 安装方法

### 自动化安装（推荐）
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\install.ps1 "你的游戏根目录路径"
```

### 手动安装
将 `patch/game/BladeSSRMod` 目录直接复制到游戏的 `game/` 文件夹下即可。
