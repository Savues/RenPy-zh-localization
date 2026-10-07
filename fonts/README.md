# 字体 / Fonts

这个目录**故意不放任何字体文件**。

中文补丁要显示中文，就必须替换游戏硬编码的那 4 个字体文件名。Windows 自带的
微软雅黑（`msyh.ttc`）、黑体（`simhei.ttf`）、等线（`Deng.ttf`）都是**微软的专有
字体**，没有再分发授权；开源的思源黑体 / Noto Sans CJK 单个文件就有 15–20 MB，
塞进仓库不合适。所以补丁改为**在用户机器上现找**。

## 你需要做什么

大多数情况下：**什么都不用做**。

`tools/install.py` 会按这个顺序找一款能显示中文的字体：

1. `fonts/zh.ttf`（如果你放了）
2. 微软雅黑 → 微软雅黑 Light → 黑体 → 宋体 → 等线
3. macOS：苹方 → 冬青黑体简 → Arial Unicode
4. Linux：Noto Sans CJK → 文泉驿微米黑 / 正黑

找到哪款用哪款。Windows 和主流 Linux 发行版都自带中文字体，所以绝大多数用户
直接装就行。

## 想固定用某一款

把字体文件放到 `fonts/zh.ttf`，或者安装时直接指定：

```bash
python tools/install.py "C:\Games\Eden-Chapter5-pc" --font "/path/to/YourFont.ttf"
```

注意：放进 `fonts/` 的文件不会被提交（见 `.gitignore`），因为**你需要自己确认
这款字体的再分发授权**。SIL OFL 授权的思源黑体 / Noto Sans CJK 可以自由使用
和再分发。

## 为什么是覆盖文件名，而不是改配置

游戏脚本里到处硬编码了字体**文件名**：

- `comfortaa.ttf` —— 对话框正文
- `CinzelDecorative.ttf` —— 标题 / 词条名
- `MichromaRegular.ttf` —— 数值与状态
- `PacificoRegular.ttf` —— 强调

它们同时出现在 `{font=...}` 标签、界面样式表和 `gui.*_font` 设置里。Ren'Py 虽然
有 `config.font_replacement_map`，但逐个去覆盖磁盘上的同名文件，是唯一能一次覆盖
所有引用、且**完全不需要改动游戏脚本**的做法——包括那些游戏运行时才拼出来的
`{font=...}` 标签。卸载脚本会把原文件从备份里还原回来。
