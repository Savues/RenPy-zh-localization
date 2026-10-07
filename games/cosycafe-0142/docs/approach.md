# 为什么 Cosy Cafe 不用 translate 补丁

仓库另外两款游戏（Eden Chapter 5、Sinful Summer 3.6）走标准的 Ren'Py 翻译块路线。
本作偏离了，原因是硬约束，不是偏好。

## translate 路线的前提

`tools/build_tl.py` 的输入是 `games/<slug>/tl_template/` —— 一份**英文原文**、且已经包在
`translate <lang> ...:` 块里的脚本。`tools/template.py` 负责从 `<游戏>/game/tl/<lang>/`
把这份模板拷进来。

Cosy Cafe 发行包里 **`game/tl/` 是空的**：只有 `game/tl/None/common.rpym` 和它的字节码，
没有任何 `game/tl/schinese/` 模板，也没有 `renpy/common` 的字符串导出。开发者根本没做多语言结构。
没有模板，`build_tl.py` 直接 `sys.exit`。

## 即使能生成，也装不进去

块 ID 不是随便起的。`renpy/translation/__init__.py` 的 `create_translate()`：

```python
for i in block:
    code = i.get_code()
    md5.update((code + "\r\n").encode("utf-8"))
digest = md5.hexdigest()[:8]
identifier = self.unique_identifier(self.label, digest)
```

`ast.Say.get_code()` 把 `who`、`encode_say_string(what)` 和 `with` 等尾巴用单空格拼起来。
也就是说 **块 ID 是英文原句的哈希** —— 中文语句永远算不出能和游戏对上号的 ID，
必须拿英文原文去算。这条路对得上，但对上没有模板就无从谈起。

安装侧还有第二道墙：`tools/install.py` 的全部动作只有三样 ——
`game/tl/<lang>/`、`game/<shim>.rpy`、`game/fonts/*`。**它没有覆盖游戏脚本的能力。**
本作的 32,639 条译文分布在游戏自己的 27 个 `.rpy` 里，只能整体替换。

## 实际采用的方案

用中文版 `.rpy` 整体替换游戏脚本，配 `zz_zh_locale.rpy` 做字体兜底。

替换过程做过严格的结构校验：逐文件比对替换前后，字符串字面量的**行号、列号、引号类型、
是否三引号**完全一致，语句关键字序列一致，把所有字符串遮蔽后的代码骨架逐行一致 ——
27 个文件、40,895 个字符串字面量全部通过，只允许字面量**内容**不同。

## 已知的坑

### 列号会漂移

早期版本的回写脚本按「文件 + 行号 + 列号」定位字面量。中文普遍比英文短，
一旦同一行前面某个字面量变短，后面的字面量全部左移，再跑一次就会错位。

实际翻车案例，`scripts/flags.rpy`：

```
原始  : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
错误后: ["星期一", "星期二", "星期三", "星期三", "星期五", "星期六", "星期日"]
                                       ^^^^^^^ 应该是 星期四
```

**改动本补丁时务必用行内序号或字符串内容对齐，不要用列号。**

注意 `data/tl_trans.json` 是从最终 `.rpy` **反向**导出的，位置信息在那里已经丢失，
所以它会忠实地把错误一并记下来 —— 当初 `"Thursday": "星期三"` 就是这样被带进去的。
改完 `.rpy` 记得同步改这个文件。

### 提取器会漏

最初的提取器只认「玩家可见文本」，漏掉了：主菜单按钮与 tooltip、章节/日期选择界面、
`gallery_pax.rpy` 的场景列表、`flags.rpy` 的 `default` 列表、`define X = Character("名字")`。
这些是后期手工补的，共约 100 处。

### 已修：WeekDays 星期四缺失

`scripts/flags.rpy` 的 `WeekDays[3]` 曾被写成「星期三」。第 6 / 13 / 20 / 27 天都是
`CurrentWeekDay = 3`，于是 HUD（`screens.rpy:2234`）和章节标题（`functions.rpy:127`）
把星期四显示成了星期三。

修复范围：`patch/game/scripts/flags.rpy` 与 `data/tl_trans.json` 各一处。

全量复查以提取阶段的英文清单（`file#line:col` → 英文原文）为基准，逐文件自动求出行偏移后
再与译文映射表对账：**32,639 条字面量全部命中，32,637 条内容一致**。剩下 2 条是
`Wong's` → `Wong’s` 的弯引号，两处写法一致，属排版选择而非错位。

为防复发，`tools/verify_patch.cjs` 查两件事：已知枚举（`WeekDays` / `Time`）的完整值，
以及同一行里相邻中文字面量是否重复。它不依赖英文原文，改完补丁跑一遍即可：

```
node games/cosycafe-0142/tools/verify_patch.cjs
```
