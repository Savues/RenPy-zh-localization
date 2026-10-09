# 方案说明 —— 60 Days Of Us 3.1.3

## 文件落在哪里

```
patch/game/tl/Chinese/*.rpy   →   <游戏>/game/tl/Chinese/*.rpy
patch/zz_zh_locale.rpy        →   <游戏>/game/zz_zh_locale.rpy
game/archive.rpa             →   索引里 24 条 tl/Chinese/* 被摘掉，其余一个字节不动
```

路径原样落地，**不多一层**。Ren'Py 对多一层的补丁是静默忽略的：不报错、不提示，
只是那份补丁从来没被加载过。

语言代码是 `Chinese`（首字母大写），因为游戏自带的中文就叫这个。
写成 `schinese` 的话，语言菜单里会多出一份没人用的中文，而玩家选的那一份
仍然是归档里没被修过的原文。

## 唯一必须动归档的那一个游戏

其余 15 个游戏的补丁都是「把文件放进去」。这一个不行，原因值得完整写下来。

### 故障链

1. 下载包自带简体中文，位置在 `game/archive.rpa` 里的 `tl/Chinese/`。
2. Ren'Py 收集翻译时，磁盘上的文件和归档里的条目**各走一条路径、互不覆盖**。
   `loader.py` 虽然注释着「磁盘上的文件应该优先于归档」，但翻译走的是
   `list_files()`，两份都收。
3. 于是散落文件**不是替换归档里的同名文件，是多了一份**。
4. `translate Chinese strings:` 块里的 `old` 键在 `TranslationStringRegistry`
   里必须全局唯一：

   ```
   if old in self.translations:
       raise Exception('A translation for "%s" already exists.' % old)
   ```

5. 结果是**启动即崩**，玩家连主菜单都进不去，报的还是一条 `traceback.txt`。

最阴的地方是 `lint` 当时是「通过」的，而统计显示 `Chinese = 15,586 块 = 7,793 × 2`：
普通 `translate Chinese <id>:` 块按 (id, language) 建字典，**重复会静默覆盖**，
只有 `strings:` 块会抛异常。所以这个 bug 看起来「时有时无」。

### 为什么不能靠覆盖解决

`game/tl/Chinese/script.rpy` 盖在归档里的同名文件上，Ren'Py 依然两个都读。
覆盖只改变「哪一份排在前面」，不改变「两份都被收集」。**唯一的解法是删掉归档那份。**

### 为什么不能删文件、只能改索引

RPA-3 把条目数据**原样存在归档文件里**，索引单独记录每个条目的名字与偏移。
`tl/Chinese/*` 是 24 条（12 个 `.rpy` 各自的 `.rpy` 与 `.rpyc`）。
`tools/rpa_drop_prefix.py` 做的事只有三步：

1. 读出索引，剔掉 24 条 `tl/Chinese/*`；
2. 把重建的索引**追加到文件末尾**；
3. 就地改掉 34 字节的文件头里那个索引偏移。

每一条存活条目的偏移量原封不动，所以 2.5 GB 的图片和音频既没有搬动、
也没有重新压缩。代价是 O(索引大小)：本版本追加约 84 KB（6,956 → 6,932 条）。

脚本的默认动作是 **dry run**：只打印会删什么，不写任何东西。`--apply` 才落盘，
落盘前先备份，落盘后**按 Ren'Py 的读法重新读一遍**，对不上就直接失败。
安装器先跑 dry run，再整体备份归档，最后才 `--apply --no-backup --verify 12`——
抽样 12 个条目与打补丁之前的读法逐字节比对。

### 为什么借用游戏自带的 Python

索引是 zlib 压缩 + Python `pickle` 序列化的。PowerShell 有 `System.IO.Compression`
但没有能安全往返二进制 pickle 的东西，而「请玩家自己装 Python」会打破这个仓库
对每个游戏许下的承诺。Ren'Py 自己的运行时就在游戏目录里：

```
lib/py3-windows-x86_64/python.exe
```

本版本实测为 Python 3.12.7，自带 zlib 与 pickle。安装器去找这个文件，
找不到就停下报错，不猜。

## 备份与还原

安装器在动归档的**第一个字节之前**，先把整个 `archive.rpa` 复制到
`game/.zh_patch_backup/archive.rpa`（2.5 GB，是实打实的开销，但这是唯一能还原的办法）。
同时备份每个被写文件的 `.rpyc`，并把清单写进 `game/.zh_patch_backup/manifest.json`
（`files` / `compiled` / `introduced` 三类）。

`tools/uninstall.ps1` 把备份盖回去并删掉 `game/tl/`。因为归档只是被追加了新索引，
盖回原始文件后长度精确回到 2,550,180,180 字节。

## `.rpyc` 这一步不能省

下载包在每个 `.rpy` 旁边都放了编译好的 `.rpyc`，而 **Ren'Py 优先加载字节码**。
把中文 `.rpy` 盖上去却留着原来的 `.rpyc`，游戏会照旧跑归档里的翻译，
而且**不报任何错**。安装器逐文件备份后删除它们。手动装的话请自己确认
`game/tl/Chinese/` 下没有残留的 `.rpyc`。

## 为什么是 `script-override`

和 `between-humanity-033`、`newteacher-090` 同一个理由：译文树是手工维护的，
不是从字典生成的。`tl-blocks` 的前提是 `data/tl_trans.json` 是**构建输入**，
`check.py` 拿它和英文逐条比对。这里没有构建输入——树是一行行改出来的，
拿一个反向推出来的字典去打分，等于补丁自己给自己判卷。

所以不建译文库。`game.json` 的 `coverage` 断言覆盖率，`tools/verify_patch.cjs`
每次都从补丁重新数一遍，对不上就失败。

## `verify_patch.cjs` 查六件事

| # | 查什么 | 为什么 |
|---|---|---|
| 1 | 12 个文件都在，且 `12 × 2 == game.json 的 archive_prefix_entries` | 少一个就说明补丁和索引手术对不上号，归档里会留下一个还在生效的旧文件 |
| 2 | `translate Chinese strings:` 的 `old` 键全局唯一 | 重复就是上面那条启动即崩 |
| 3 | 具名 `translate Chinese python:` 块只允许有一个 | 同名的后加载的顶掉先加载的，而注册思源宋体的那个不能被遮住 |
| 4 | `old` 键里不许有汉字 | 非 ASCII 键永远匹配不上英文原文 |
| 5 | 覆盖率重新提取，与 `game.json` 逐项比对 | 断言不能只写不用 |
| 6 | 有意保留原文的必须在 `_kept_verbatim` 里逐条登记 | 没登记的漏译不许混进来 |

第 3 条是照着 `between-humanity-033` 的教训来的：那里有一个注释加 `pass` 的
`translate chinese python:` 块遮住了 `style.rpy` 里注册中文字体的同名块，
一旦加载顺序不利就全篇方块。这个游戏目前只有一个具名 `python` 块，
检查是为了让它以后也只有一个。

## shim 只做一件事

```renpy
init python:
    config.language = "Chinese"
```

不碰字体表、不碰语言菜单、不碰任何界面文案。游戏自己的
`th_font_map["Chinese"]` 已经指向它自带的思源宋体 CJK，够用了。
