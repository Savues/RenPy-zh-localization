# Eden Chapter 5 — 简体中文补丁

| | |
|---|---|
| 游戏 | Eden Chapter 5 |
| 原作 | FnB Productions |
| 引擎 | Ren'Py 8.4.1 |
| 语言 | 简体中文（`schinese`） |
| 译文量 | **15,713 条**，覆盖率 100%（34,796 处引用） |
| 角色名牌 | 75 / 75 已译 |
| 翻译方式 | 全部人工撰写，**未使用任何机器翻译或在线翻译 API** |

```
eden-chapter5/
├── game.json           本游戏的元数据（引擎版本、字体文件名、语言等）
├── data/tl_trans.json  译文数据库：以英文原文为 key
├── docs/
│   ├── glossary.json           术语表，由 check.py 强制执行
│   ├── translation-log.md      翻译档案：术语决策与修过的问题
│   └── translation-workflow.md 本次汉化的过程存档
└── patch/              构建产物（已提交，可直接安装）
    ├── tl/schinese/       19 个翻译后的 .rpy
    └── zz_zh_locale.rpy   语言强制切换 + 字体覆盖 + 角色名映射
```

---

## 安装

先克隆仓库，然后：
## 安装（方式一：直接覆盖，不需要 Python）

从 [Releases](https://github.com/Savues/RenPy-zh-localization/releases) 下载
补丁包，解压后把里面的 `game/` 文件夹内容复制到游戏的 `game/` 文件夹，选择覆盖。

唯一的额外步骤是字体：游戏按文件名硬编码了 5 个字体，中文必须走它们，所以要先把
系统里的一款中文字体（微软雅黑 / 黑体 / 等线 / 宋体都行）复制成下面这些名字放进
游戏的 `game/fonts/`：

```
zh.ttf   comfortaa.ttf   CinzelDecorative.ttf
MichromaRegular.ttf   PacificoRegular.ttf
```


## 安装（方式二：脚本）

先克隆仓库，然后：

```bash
python tools/install.py "C:\Games\Eden-Chapter5-pc"
```

仓库里目前只有这一个游戏，所以不用带 `--game`；装了多个之后要补上：

```bash
python tools/install.py "C:\Games\Eden-Chapter5-pc" --game eden-chapter5
```

脚本做三件事：

1. `patch/tl/schinese` → 游戏的 `game/tl/schinese`（翻译后的脚本）
2. `patch/zz_zh_locale.rpy` → `game/zz_zh_locale.rpy`
3. 把一款系统中文字体写进 `game/fonts/`，并覆盖游戏硬编码的 4 个字体文件名

被覆盖的原始文件全部备份到 `game/.zh_patch_backup/`，装完直接启动即可，**不需要**在设置里切语言。

指定字体：

```bash
python tools/install.py "C:\Games\Eden-Chapter5-pc" --font "C:\Windows\Fonts\msyh.ttc"
```

## 卸载

```bash
python tools/uninstall.py "C:\Games\Eden-Chapter5-pc"
```

从备份逐字节还原。确认无误后加 `--purge-backup` 一并删掉备份目录。

---

## 这个游戏特有的三个坑

翻译过程中踩到的，写在这里免得后来者重蹈覆辙。

**1. 翻译必须放在 `game/tl/schinese/` 里。**
Ren'Py 会优先加载同名 `.rpyc`，散装在 `game/` 根目录的翻译文件会被已编译的字节码盖掉——表现是「文件明明改了，游戏里没变化」。

**2. `config.language` 会被游戏自己清掉。**
`renpy/common/00start.rpy` 在 `init -1600 python hide:` 里把 `config.language` 重置为 `None`。补丁里的 `config.language = "schinese"` 必须放在**普通的** `init python:` 块里（优先级更高、后执行），写在低优先级块里会被覆盖。

**3. 角色名牌是运行时变量，光改 `default` 没用。**
脚本里有 `$ ravena_name = "Ravena"` 这类运行时赋值。补丁靠 `config.say_arguments_callback` 钩子在每次 `say` 之前把变量值映射成中文。这个回调的签名是：

```python
callback(who, *args, **kwargs)  ->  (args, kwargs)
```

它返回的是**传给 say 的位置参数和关键字参数**，不是 `(who, what)`。而且 `config.say_arguments_callback` 是**单个可调用对象**、默认值为 `None`——对它调 `.append()` 会直接抛 `AttributeError`。

---

## 从源码重建
## 生成补丁包

```bash
python tools/package_release.py --version v1.0.0
```

输出 `dist/eden-chapter5-schinese-patch-v1.0.0.zip`：包含玩家向的 `README.md`、
`LICENSE`，以及一个可直接覆盖的 `game/` 目录。**不含字体**——可再分发的中文字体
都要 8 MB 以上，而好用的系统字体都是专有的，所以改成让玩家自己放（见上文）。

打包结果是确定性的：固定时间戳 + 排序写入，同一份代码树重复打包产出字节一致的 zip。

---

## 从源码重建

```bash
python tools/template.py "C:\Games\Eden-Chapter5-pc"   # 仅首次：导入英文模板
python tools/build_tl.py                                 # 生成 patch/tl/schinese
python tools/check.py                                    # 校验
python tools/selftest.py                                 # 反向验证检查项
```

`tl_template/` 会被 `.gitignore` 排除——那是游戏的原始英文脚本，属于原作，不该进仓库。

## 术语表约定

专名和设定的中文写法登记在 [`docs/glossary.json`](docs/glossary.json)，`check.py` 会
强制执行——它登记的是**禁用译名**，而不只是正确译名，所以后续润色改回别的写法会被拦下。

其中一条值得记下来：原脚本用 **Divinarch** 和 **Celestiarch** 两个不同的英文词指同一批
存在（六位飞升者），中文必须统一，本作取 **天枢**。

完整的术语决策、人名表、刻意不译的内容、以及最后一轮修过的 22 处问题，见
[`docs/translation-log.md`](docs/translation-log.md)；这次汉化踩到的 Ren'Py 引擎的坑
和校验器设计陷阱，见 [`docs/translation-workflow.md`](docs/translation-workflow.md)。

---

## 版权

游戏版权归 FnB Productions 所有。本目录**不包含**游戏的任何程序文件、图像、音频或原始脚本，只包含翻译补丁与构建工具。与 FnB Productions 无任何关联。
