# 汉化工作流（本次记录）

**这是 Eden Chapter 5 这次汉化的过程存档**，目的只是记录当时是怎么做的、
踩了哪些坑——不是给下一个项目当通用参考的。

内容分两块，读者按需取用：

- **一、二节** —— Ren'Py 这套引擎本身的坑。换个游戏依然成立，值得先读。
- **三、四节** —— 校验器的设计陷阱和几条经验。这些结论本身也来自这次翻译，
  具体例子都取自本作。

翻译内容本身的档案（术语决策、修过的问题、最终数据）在
[`translation-log.md`](translation-log.md)。

---

## 一、整体流程

```
游戏原版 game/tl/<lang>/*.rpy         （英文模板，含 translate 块）
        │  tools/template.py
        ▼
    games/<slug>/tl_template/           英文原文模板，不提交
        │  人工翻译 + 录入 data/tl_trans.json
        ▼
    games/<slug>/data/tl_trans.json     以英文原文为 key 的译文库
        │  tools/build_tl.py
        ▼
    games/<slug>/patch/tl/<lang>/*.rpy  翻译后的脚本（构建产物，提交）
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

正确做法：放进 `game/tl/<lang>/`，并**删掉同名的旧 `.rpyc`**。

### 2. `config.language` 会被游戏自己清掉

`renpy/common/00start.rpy` 里有一段：

```renpy
init -1600 python hide:
    config.language = None
```

优先级 `-1600` 意味着它**最后**执行。所以补丁里的 `config.language = "<lang>"`
必须放在**普通的** `init python:` 块里（默认优先级 0，比 -1600 高、先执行），
写在低优先级块里会被这行覆盖掉。

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
Ren'Py 用 `__getattr__` 统一抛 `Exception`。正确做法是查 Ren'Py 文档确认属性名，
不要靠 try/except 试探。

### 5. 角色名牌是运行时变量

脚本里有这类写法：

```renpy
$ <name>_var = "Ravena"
pr "..."
```

只改 `default <name>_var = "中文名"` 完全没用，因为运行时会重新赋值。
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
卸载时从备份还原即可。各游戏硬编码了哪些字体名，写在自己的 `game.json` 的
`font_shadow` 字段里——用 `grep -rn "font=" <游戏>/game --include=*.rpy` 找。

---

## 三、校验器的设计陷阱

写校验器比想校验器难。下面每一条都是**实际踩过**的，包括校验器自己的坑。
`tools/selftest.py` 就是为了守住这些而写的。

### 行宽必须按渲染列宽算，不能按字符数

第一版用 `len(译文) > len(原文) * 1.15`，立刻报了 109 条。逐条看全是误报：

```
'H-how…'      (6 字符) → '怎、怎么会……'    (7 字符)    1.17x  ← 误报
'Needy.'      (6)       → '……产生心理阴影。'(8)         1.33x  ← 误报
'Mainly RPGs.'(12)      → '主要是角色扮演游戏。'(10)     0.83x
```

一个汉字渲染宽度约等于两个拉丁字符，但承载的信息量约 1.6–1.8 个拉丁字符。
所以中文比英文「短」是常态，比例阈值定在 1.5 只会制造噪音。**改成 2.0 之后
误报归零**。

真正该拦的是绝对宽度：给一个 `ABS_MAX`（1080p 下单行能放下的列数）。
并且要豁免两类：长文本（源码 ≥200 列，通常是图鉴/词条，在可滚动面板里显示）
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

生成术语表时我用了 `\u795e\u8bba\u8005\u8005` 想表达「神谕者者」，
但码位敲错了几个字（`\u8baf` 是「讯」不是「谕」）。结果是：守卫字符串变成了
「神讯者者」，**永远不会匹配到任何东西**，于是 `check.py` 一直报
「all checks passed」——一个完全失效的检查。

现在所有涉及中文的脚本一律用**字面汉字**，不用手写码位。
这个 bug 之所以能潜伏，是因为**没人验证过守卫真的会触发**。

### 反向测试脚本自己会污染数据

`tools/selftest.py` 最早的版本，`finally` 里写了：

```python
shutil.copyfile(DB, BAK)   # ← 把已经被污染的 DB 覆盖掉了完好的备份
```

于是「恢复」实际上恢复的是**最后一次注入的脏数据**。

现在原始副本全程**只存在内存里**，并且结束时断言数据库字节级还原成功。

---

## 四、几条经验

- **术语先定稿再动笔。** 专名表定死之后再开始翻译，比翻译完再回头统一便宜得多。
- **长文本条目要通读。** 「并不不幸福」这类语义错误自动检查抓不到，图鉴/词条
  那些超长段落值得人工过一遍。
- **每个检查项都要有反向测试。** 没有反向测试的检查，随时可能已经失效了
  而你不知道——上面那个「神讯者者」就是这么活下来的。
- **不确定就先建最小样例验证。** 引擎行为、回调签名、优先级规则，用一段十行的
  测试脚本比读十遍文档快，而且不会读错。

---

## 相关文档

- 本游戏的翻译档案：[`translation-log.md`](translation-log.md)
- 安装 / 卸载 / 重建步骤：[`../README.md`](../README.md)
- 新增一个游戏：[`adding-a-game.md`](../../../docs/adding-a-game.md)
- 字体机制、换字体与授权：[`fonts.md`](../../../docs/fonts.md)
