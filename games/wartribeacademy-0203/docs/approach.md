# 为什么 Wartribe Academy 不用 translate 补丁

仓库里有两种打补丁的方式。Eden Chapter 5 和 Sinful Summer 3.6 用 Ren'Py 的
`translate` 块，本作用脚本覆盖。两条都是仓库认的方案，`game.json` 的
`patch_layout` 声明用哪条 —— 选这条的原因是硬约束，不是偏好。

## translate 路线的前提

`tools/build_tl.py` 的输入是 `games/<slug>/tl_template/` —— 一份**英文原文**、且已经包在
`translate <lang> ...:` 块里的脚本。`tools/template.py` 负责从 `<游戏>/game/tl/<lang>/`
把这份模板拷进来。

Wartribe Academy 2.0.3 发行包里 **`game/tl/` 几乎是空的**：

```
game/tl/None/common.rpym     36,561 bytes
game/tl/None/common.rpymc    28,888 bytes
```

只有 `None` 这一档 —— 那是 Ren'Py 自己在打包时生成的空翻译树，不是任何语言的模板。
**没有任何 `game/tl/<lang>/` 可用**，`tools/build_tl.py` 在
`tools/build_tl.py:52` 直接 `sys.exit("%s is missing -- run: python tools/template.py ...")`。

## 即使能生成，也装不进去

块 ID 不是随便起的。`renpy/translation/__init__.py` 的 `create_translate()`：

```python
def create_translate(self, block):
    md5 = hashlib.md5()
    for i in block:
        code = i.get_code()
        md5.update((code + "\r\n").encode("utf-8"))
    digest = md5.hexdigest()[:8]
    identifier = self.unique_identifier(self.label, digest)
```

`ast.Say.get_code()` 把 `who`、`encode_say_string(what)` 和 `with` 等尾巴用单空格拼起来。
也就是说 **块 ID 是英文原句的哈希** —— 中文语句永远算不出能和游戏对上号的 ID，
必须拿英文原文去算。这条路对得上，但对上没有模板就无从谈起。

安装侧还有第二道墙：`tools/install.py` 的全部动作只有三样 —— `game/tl/<lang>/`、
`game/<shim>.rpy`、`game/fonts/*`（`tools/install.py:9-10`）。**它没有覆盖游戏脚本的能力。**
本作的 61,417 条字面量分布在游戏自己的 15 个 `.rpy` 里，只能整体替换。

## 实际采用的方案

用中文版 `.rpy` 整体替换游戏脚本，配 `zz_zh_locale.rpy` 做字体兜底。
`patch/game/` 与游戏的 `game/` 目录一一对应（`replay_data.rpy` 是补丁新增，
游戏原版没有这个文件）。

替换过程做过严格的结构校验：拿英文原版的**遮蔽骨架**逐行比对字符串字面量的
**行号、列号、引号类型、是否三引号**，语句关键字序列一致 ——
14 个文件、66,411 个字符串字面量全部通过，只允许字面量**内容**不同。

## 为什么校验要拿「遮蔽骨架」当基准

脚本覆盖真正的死穴是「按文件 + 行号 + 列号定位字面量回写」。中文比英文短，
同一行里靠后的字面量整体左移，第二次跑就会写错位置 —— 而这种改动
**语法完全合法**，没有任何通用 linter 看得出来。Cosy Cafe 的 `WeekDays` 枚举
就是这么把星期四写成了星期三的。

所以本补丁不抽查已知枚举，而是把英文脚本里每个字面量替换成只记录引号样式的标记
（`@S` / `@Q` / `@T3` / `@T3'`），注释一并抹除，得到一份纯代码骨架；再逐行比对。
骨架里**没有一句英文原文**，所以校验只凭本仓库的克隆就能跑，不必再附带一份原作的散文 ——
这份校验基准本身只有 3,501,674 字节骨架 + 66,411 字节 flags。

## gui.rpy 是唯一允许结构分歧的文件

它必须分歧：`gui.text_font` / `gui.name_text_font` / `gui.interface_text_font`
三行 define 要被替换成一个 FontGroup 接线，否则中文全是方块。

对它 `tools/verify_patch.cjs` 换用更精确的检查：先确认英文侧恰好命中那三行 define，
把它们**连同区间**切掉；再确认中文侧存在 `def _localised_font(` 与
`gui.interface_text_font = _localised_font(` 标记，把这个块切掉；然后比较**剩下的部分**
必须与英文版一致（逐行、含空行）。同时逐条检查那五个接线标记都还在。

这样「结构分歧」被限制成一个已知且被显式声明的块，其余每一行仍然对得上。

## 校验为什么查不到覆盖率以外的东西

覆盖率写在 `game.json` 的 `coverage` 里，**是断言不是推导**：

```json
"coverage": { "translated": 61294, "total": 61417 }
```

`check.py` 只负责把它打印出来，不会重算，也不会因为对不上而报错。

真正的覆盖率由 `tools/verify_patch.cjs` 现算，但它的**分母不是从中文脚本里数的**，
而是来自 `data/en_masked/<file>.flags` —— 每个英文字面量一个标记，分类为
`p`（玩家可见）/ `a`（资源路径）/ `s`（纯替换）/ `n`（其它）。
翻译是从这份英文清单驱动的，所以「原文有多少条」是外部事实，不是补丁自证的。

`p` 一共 61,417 条，其中 61,294 条带汉字，123 条没有。这 123 条必须在
`docs/glossary.json` 的 `_kept_verbatim` 里登记过，否则校验失败；只由 Ren'Py
变量与标签构成、根本没有英文可译的字面量不算在内。

## replay_data.rpy 的诚实处理

这个文件在补丁存在**之前**就已经就地汉化过了，仓库里没有它的英文原版。
所以它：

- 不参与逐行结构比对（没有基准可比）
- 不计入 61,417 / 61,294 这两个数字
- 但仍然接受字体覆盖和资源键检查

`tools/verify_patch.cjs` 每次运行都会打印这一条 note。**把它悄悄当成 0 覆盖率报出去，
或者假装它被检查过，都是撒谎**，所以脚本选择说出来。

## 安装器为什么要自己带一个

`tools/install.py` 只会摆三样东西，摆不进脚本覆盖。而脚本覆盖必须处理几件
`install.py` 抽象不到的事：

- **只备份一次**。反复安装不能把第一次的备份冲掉，否则卸载时就回不去了。
- **删陈旧字节码**。Ren'Py 优先加载 `.rpyc` / `.rpymc`；换了 `.rpy` 却留着旧字节码，
  中文会**静默失效** —— 游戏照常启动，只是没汉化。
- **记录哪些文件是补丁引入的**（`zz_zh_locale.rpy` 和三个字体）。卸载时这些要删掉，
  而不是「还原」。

所以 `tools/install.ps1` / `tools/uninstall.ps1` 自带 manifest（version 2，
含 `files` 与 `introduced` 两张表），比通用安装器多知道一件事：哪些文件本来不属于游戏。