# 汉化工作流

这份文档记录 Eden Chapter 5 汉化的完整流程，以及过程中真正卡住过的地方。
写下来不是为了留档，是因为下面每一条都是**实际踩过**的——包括工具链自己踩的坑。

---

## 一、整体流程

```
游戏原版 game/tl/schinese/*.rpy        （英文模板，含 translate 块）
        │  tools/template.py
        ▼
    tl_template/                          英文原文模板，不提交
        │  人工翻译 + 录入 tl_trans.json
        ▼
    data/tl_trans.json                    以英文原文为 key 的译文库
        │  tools/build_tl.py
        ▼
    patch/tl/schinese/*.rpy               翻译后的脚本（构建产物，提交）
        │  tools/check.py + tools/selftest.py
        ▼
    tools/install.py → 用户的游戏目录
```

翻译**不是**在 `.rpy` 文件上直接改的。所有改动都落在 `tl_trans.json`，
`.rpy` 永远是构建产物。好处是可复现、可 diff、可校验，而且换一台机器重新
build 出来的结果和提交的一模一样。

---

## 二、Ren'Py 引擎本身的坑

这一节与具体游戏无关，换任何 Ren'Py 游戏都会遇到。

### 1. 翻译必须放在 `game/tl/<lang>/` 里

Ren'Py 加载脚本时**优先用 `.rpyc`**，`.rpy` 只是源码。如果把翻译后的文件
随便丢在 `game/` 根目录，运行时读到的还是已编译的旧字节码——表现是「文件明明
改了，游戏里没变化」。

正确做法：放进 `game/tl/schinese/`，并**删掉同名的旧 `.rpyc`**。

### 2. `config.language` 会被游戏自己清掉

`renpy/common/00start.rpy` 里有一段：

```renpy
init -1600 python hide:
    config.language = None
```

优先级 `-1600` 意味着它**最后**执行。所以补丁里的
`config.language = "schinese"` 必须放在**普通的** `init python:` 块里
（默认优先级 0，比 -1600 高、先执行），写在低优先级块里会被这行覆盖掉。

### 3. `config.say_arguments_callback` 是单个可调用对象

三个独立的坑，串在一起：

```python
# ✗ 它默认是 None，不是 list —— .append() 直接 AttributeError
config.say_arguments_callback.append(my_hook)

# ✗ 签名不接受 who 关键字参数
def hook(who, interact=False): ...

# ✓ 正确形态：返回传给 say 的位置参数与关键字参数，不是 (who, what)
def hook(who, *args, **kwargs):
    return args, kwargs

# ✓ 要链上原有的回调（如果游戏自己设过）
prev = config.say_arguments_callback
def hook(who, *args, **kwargs):
    if prev:
        args, kwargs = prev(who, *args, **kwargs)
    return args, kwargs
config.say_arguments_callback = hook
```

### 4. 不存在的配置项会抛 `Exception` 而不是 `AttributeError`

想判断某个 `config.xxx` 是否存在时，`getattr(config, "xxx", None)` **兜不住**——
Ren'Py 用 `__getattr__` 统一抛 `Exception`。这次就撞上了
`config.after_load_transient_callback`，正确做法是查 Ren'Py 文档确认属性名，
不要靠 try/except 试探。

### 5. 角色名牌是运行时变量

脚本里有这类写法：

```renpy
$ ravena_name = "Ravena"
pr "..."
```

只改 `default ravena_name = "拉维娜"` 完全没用，因为运行时会重新赋值。
解法是用 `config.say_arguments_callback` 钩子，在**每次 say 之前**扫一遍
角色名变量，把值映射成中文：

```python
def localize_names():
    for var in NAME_VARS:
        v = getattr(renpy.store, var, None)
        if isinstance(v, str) and v in NAME_MAP:
            setattr(renpy.store, var, NAME_MAP[v])
```

### 6. 字体要覆盖**文件名**，不是改配置

游戏里到处硬编码字体文件名，包括 `{font=...}` 标签、界面样式表，
甚至运行时拼出来的字符串。改 `gui.text_font` 覆盖不全。

在磁盘上用中文字体覆盖同名文件，才是一次性覆盖所有引用的唯一办法。
卸载时从备份还原即可。

> Eden Chapter 5 硬编码了 4 个：`comfortaa.ttf`、`CinzelDecorative.ttf`、
> `MichromaRegular.ttf`、`PacificoRegular.ttf`。这些写在各游戏的 `game.json`
> 的 `font_shadow` 里。

---

## 三、译文本身的坑

### 术语分裂：原脚本自己就不统一

Eden 的脚本用 **Divinarch** 和 **Celestiarch** 两个不同的英文词指同一批存在
（六位飞升者）：

```
There are far more Divinarchs than the Six.
There are six Celestiarchs, each representing one of the Spiritual Energies.
One of the six Divinarchs. /  One of the six Celestiarchs.
```

中文初版一个翻成「神架构师」、一个翻成「天枢」，同一批角色出现两个名字。
**原脚本用了两个词，不代表它们是两个概念。** 后来统一取「天枢」。

这类问题光看译文是发现不了的，得回到英文原文去对照。所以术语表要登记**禁用译名**，
而不是只登记正确译名。

### 叠字和重复

批量替换术语时最容易出的错：

| 错误 | 正确 | 发现方式 |
|---|---|---|
| 神谕者**者** | 神谕者 | 叠字扫描 |
| 并**不不**幸福 | 并不幸福 | 重复否定，肉眼读代码段时发现 |
| GNU LGPL␣␣Lesser | 单空格 | 全角/半角规范化扫描 |

「并不不幸福」这种重复否定是语义错误，任何自动检查都只能靠**通读**发现。
所以 `patch/` 里那些长文本条目是值得人工过一遍的。

---

## 四、校验器：以及它自己踩的坑

`tools/check.py` 是发布前的关卡。写它比想它难——下面是它**误报和漏报**的真实记录。

### 行宽必须按渲染列宽算，不能按字符数

第一版用 `len(译文) > len(原文) * 1.15`，立刻报了 109 条。逐条看全是误报：

```
'H-how…'    (6 字符) → '怎、怎么会……'   (7 字符)   1.17x  ← 误报
'Needy.'    (6)       → '……产生心理阴影。'(8)        1.33x  ← 误报
'Mainly RPGs.' (12)   → '主要是角色扮演游戏。'(10)     0.83x
```

一个汉字渲染宽度约等于两个拉丁字符，但承载的信息量约 1.6–1.8 个拉丁字符。
所以中文比英文「短」是常态，比例阈值定在 1.5 只会制造噪音。**改成 2.0 之后
误报归零**。

真正该拦的是绝对宽度：`ABS_MAX = 130` 列（1080p 下单行能放下的量）。
并且要豁免两类：长文本（源码 ≥200 列，是 Codex 词条，在可滚动面板里显示）
和带显式换行符的系统消息。

### 禁用译名不能是正确译名的子串

```
正确：神谕者
禁用：谕者      ← 「谕者」是「神谕者」的子串！
```

朴素子串匹配会把**每一条正确译文**都报成错误。修法是先把正确译名从文本里
剔除，再在剩下的部分里找禁用译名。

同理，叠字检查也不能扫任意 `CC`——那会把「克拉拉」「莉莉」「谢谢」全报一遍。
只匹配 `术语 + 术语末字` 这个精确形状才既准确又不吵。

### 纯字母的英文 UI 词曾被当成技术符号放过

```python
# ✗ 只要求「含任意字母数字」，于是 "Back"、"Start"、"Quit" 全部豁免
r"|^(?=.*[A-Za-z0-9])[A-Za-z0-9%.:#,...]+$"

# ✓ 要求含数字或路径/格式字符，这才是这条规则的本意
r"|^(?=.*[0-9%:/\\.])[A-Za-z0-9%.:#,...]+$"
```

这是靠**反向测试**发现的：往译文库里注入 `Back` 原文当译文，`check.py` 应该
报错却没报。

### 手写 `\uXXXX` 转义是个陷阱

生成 `glossary.json` 时我用了 `\u795e\u8bba\u8005\u8005` 想表达「神谕者者」，
但码位敲错了几个字（`\u8baf` 是「讯」不是「谕」，`\u8baf`→实际该是 `\u8bba`
或 `\u8c15`）。结果是：守卫字符串变成了「神讯者者」，**永远不会匹配到任何东西**，
于是 check.py 一直报「all checks passed」——一个完全失效的检查。

现在所有涉及中文的脚本一律用**字面汉字**，不用手写码位。
这个 bug 之所以能潜伏，是因为**没人验证过守卫真的会触发**。

### 反向测试脚本自己会污染数据

`tools/selftest.py` 最早的版本，`finally` 里写了：

```python
shutil.copyfile(DB, BAK)   # ← 把已经被污染的 DB 覆盖掉了完好的备份
```

于是「恢复」实际上恢复的是**最后一次注入的脏数据**。真实后果：有一条
Ren'Py 版本号字符串在数据库里变成了 80 个重复的「你」字，直到靠重建产物比对
才发现。

现在原始副本全程**只存在内存里**，并且结束时断言数据库字节级还原成功。

---

## 五、最终数据

| 项 | 数值 |
|---|---|
| 译文条目 | 15,713 |
| 构建应用点 | 34,796（未译 0） |
| 补丁文件 | 19 个 `.rpy` |
| 补丁行数 | 206,940 |
| 角色名牌 | 75 / 75 已译 |
| 译文行宽中位数 | 20 列（远低于 130 上限） |
| 校验类别 | 7 类 |
| 反向测试用例 | 63 个，全部确认会报错 |

最后一轮润色修了 22 处：叠字 9、重复否定 1、双空格 1、术语分裂 11。

## 六、下次会怎么做

- **术语先定稿再动笔。** 这一轮 11 处问题全部出在术语统一阶段。先把专名表
  定死再开始翻译，比翻译完再回头统一便宜得多。
- **长文本条目要通读。** 「并不不幸福」这类语义错误自动检查抓不到，
  Codex 词条那些超长段落值得人工过一遍。
- **每个检查项都要有反向测试。** 没有反向测试的检查，随时可能已经失效了
  而你不知道——`神讯者者` 就是这么活下来的。
