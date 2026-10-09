# 维护者流程

面向仓库维护者。玩家看 [`../README.md`](../README.md)，新增游戏看
[`adding-a-game.md`](adding-a-game.md)。

## 跑工具用什么 Python

仓库不绑定解释器，`python` 指向哪都行。唯一要留意的是 **TLS 验签**：mingw 构建的
CPython（如 Ren'Py 自带的那份）既没有 CA 文件也不读 Windows 证书库，
`publish_release.py` 的 HTTPS 调用会在握手阶段报 `CERTIFICATE_VERIFY_FAILED`。
该工具已经缺省用 `certifi` 建 context；自己另写的联网脚本记得也带上，或者设
`SSL_CERT_FILE` 指向一份 CA bundle。

## 发一个版本

一个 Release 收录**全部**已收录游戏，每个游戏一个独立压缩包。新增游戏只会往资产列表里
加一项，不会多出一个 Release。

`--version` 是**发布批次**（也就是 tag），只出现在 Release 的标题和正文里，**不进压缩包**。
每个游戏压缩包用的是自己 `game.json` 里的 `patch_version`，见下面一节。

```bash
# 1. 先只构建、不联网，确认包的内容和体积
python tools/publish_release.py --version v1.0.0 --dry-run

# 2. 正式上传
python tools/publish_release.py --version v1.0.0
```

只需要某一个游戏的包时，走 `package_release.py`：

```bash
python tools/package_release.py --game <slug>
```

写到 `dist/`，不联网。

### 版本号：批次 vs 汉化包

仓库里有**两个**版本号，别混：

| | 在哪 | 什么时候变 |
|---|---|---|
| 发布批次 | Release 标题、tag、`publish_release.py --version` | 一批一起发 |
| 汉化包版本 | `game.json` 的 `patch_version`，进压缩包文件名和包内 README | **只**在这个游戏的补丁动过时才变 |

这么分是因为一个 Release 收全部游戏：批次号一动，**每个**包的字节都会跟着变（包内 README
印着版本号和包名），于是每个游戏每次都被改名 + 重新上传，哪怕它一个字都没改。历史上
`sinfulsummer-chapter36` 的包连续四个 Release 字节完全相同，纯粹是被迫换个文件名重传。

现在的规则：

- **改了某个游戏的补丁，就把它的 `patch_version` 加一。** 别的游戏不动。
- 补丁没动的游戏，文件名和字节都不变，`publish_release.py` 判定为 unchanged，
  **一个字节都不上传**，旧下载链接继续有效。
- 漏加的情况工具会报：同名包和上一个 Release 里的字节数对不上时，打印 `!!` 警告。
- **`package_release.py` 故意没有 `--version`。** 它没有批次可读；给这个开关等于
  留一个把批次号打进包里的入口。

### 压缩包里装不装安装器：`installer` 字段

`game.json` 的 `installer` 有两个值，玩家拿到的压缩包因此不一样：

| | `installer: "py"`（默认） | `installer: "ps1"` |
|---|---|---|
| 安装方式 | 手动把 `game/` 的内容复制进游戏目录 | 跑压缩包里的 `tools/install.ps1` |
| 压缩包里有 `tools/` | 否 | **是**（安装器、卸载器、以及它需要的辅助脚本） |
| 玩家 README 的安装段 | 复制表 | PowerShell 命令 |

`installer: "ps1"` 的游戏**必须**把 `tools/` 打进包里：README 让玩家跑
`tools\install.ps1`，包里没有 `tools/` 就是一份指向空处的说明。`tools/` 里唯一不打进去的
是 `game.json` 的 `extra_checks` 点名的校验脚本——那东西要 node 和一份仓库，玩家两样都没有。

`font_strategy: "game-bundled"` 的游戏同样要留意：它不带字体，所以压缩包里没有
`fonts/`、没有 `FONT-LICENSE.txt`，README 也不能再说「中文字体已打包」。这类游戏
的 README 还得按 `base_translation` 改口径：写明是**修订发行方自带的中文**，
而不是从英文重译。仓库自己的根 `README.md` 用 ` †` 标的就是这些。

这三段（安装方式、字体、翻译口径）都是 `PLAYER_README` 里的 `{{...}}`，
由 `layout_bits()` / `installer_bits()` / `fontrow_bits()` / `font_bits()` 渲染。
改模板会影响**所有**游戏的压缩包字节：改完先确认只想变的那些变了——

```python
# 改模板前后各跑一次，比对 renderer 的输出
import hashlib, package_release
print(hashlib.sha256(package_release.render_readme(m, slug, v, n).encode()).hexdigest())
```

### 可选包（`extras`）

`game.json` 里可以给游戏加 `extras`，为它额外打一个**独立压缩包**，和主包一起挂到同一个 Release。第三方 MOD 的汉化就该走这条路：主补丁不能依赖它，玩家装不装 MOD 都得是一个完整可用的游戏。

```json
"extras": [
  {
    "id": "mod-zh",
    "label": "Shawn's Mod 汉化（可选）",
    "readme": "docs/mod-readme.md",
    "flat": true,
    "counts": { "pairs": 1273, "modfiles": 6 },
    "files": ["data/mod_zh.json", "tools/mod_translate.py", "tools/translate_mod.bat"]
  }
]
```

- `readme` 是一份 `{{token}}` 模板，玩家拿到的 README 从它渲染；哪个 token 没填上，打包就直接失败，不会把 `{{...}}` 发出去。
- `counts.pairs` 会和实际打进去的那个 `.json` 的条数**对账**，对不上直接失败——那个数字是要印给玩家看的。
- `flat: true` 表示文件平铺到压缩包根目录。`.bat` 靠 `%~dp0` 找同目录的脚本和译文表，所以这类包必须平铺。
- `.bat` / `.cmd` 会检查行尾是不是 CRLF：cmd 读 LF 的批处理会把 `rem` / `echo` 的后半句当命令执行，玩家那边看到的是一串莫名其妙的报错。

没有 `extras` 的游戏走的是同一条路径，`package_release.py` 只是什么都不打。

### 重跑是安全的

- 资产按**文件名**匹配：内容一样就跳过（判定看的是文件大小），不一样就替换。
- 文件名里带的是**汉化包自己的版本**，所以「换名」= 「这个游戏的补丁更新了」，「同名换内容」会被当成漏改版本号报出来。
- 仓库里删掉的游戏，对应资产会被从 Release 上摘掉。
- **tag 只在不存在时创建**。已存在的 tag 不会被移动，所以一个已发布的版本永远指向它
  当时发布的那次提交。确实要让 tag 跟到最新提交，得自己动手：

  ```bash
  git tag -f v1.0.0 && git push -f origin v1.0.0
  ```

## 改动译文后的标准流程

后两步所有游戏一样，第一步看 `game.json` 的 `patch_layout`：

```bash
# tl-blocks：从模板 + 译文库重建补丁
python tools/build_tl.py --game <slug>

# 两种方案都要跑
python tools/check.py --game <slug> \
  && python tools/selftest.py --game <slug>
```

`script-override` 的游戏不跑 `build_tl.py`：它没有 `tl_template/`，那一步只会得到一句
「缺目录」。那个方案下 `patch/` 里的脚本**就是成品**，改完直接校验。

`build_tl.py` 不保证逐字节可复现：有些英文原文在译文库里登记了多个有意译法
（按上下文挑选），重建结果会随选择变化。`data/tl_trans.json` 和
`data/per_block_variants.json` 是这类决策的记录。

### 覆盖率数字不是工具算出来的

`script-override` 的 `coverage` 写在 `game.json` 里，是**断言**。`check.py` 只会把它
打印出来，不会重算，也不会因为对不上而报错。要动这个数字，改的是提取阶段的统计口径，
改完记得同步更新 `_coverage_note`——不然下一个接手的人只会看到一个没有出处的数字。

同理，`script-override` 游戏的 `data/tl_trans.json` 是从做完的中文脚本**反向**导出的
副产品，不是构建输入。拿它算覆盖率或跑覆盖率检查，等于让补丁给自己判卷。

改完跑一次 `check_links.py`：它检查所有相对链接，也核对根 `README.md` 的「已收录」表格
和 `games/` 一致（不一致就 `python tools/games.py --readme` 重写）。新增游戏后同样要跑
——那张表是生成的，不要手改。

## 推送凭据

这台机器没装 Git Credential Manager，所以把凭据交给 git 自带的 `store`
helper，并落到**仓库外**的独立文件：

```bash
git config --global credential.helper "store --file=$HOME/.renpy-zh-credentials"

printf 'protocol=https
host=github.com
username=x-access-token
password=<TOKEN>

' \
  | git credential approve
```

之后 `git push` 直接可用，token 不必再出现在命令行里，`publish_release.py` 也会从
同一个文件读。

> `store` helper 是**明文**存储的。它比写进 `.git/config` 或每次命令行参数
> 干净一点（仓库里查不到、命令历史里查不到），但仍然不是加密存储。Windows 上
> 如果能用 Git Credential Manager 或 WinCred，优先用它们——凭据会进系统凭据库。

确认当前用的是哪个 helper：

```bash
git config --global --get credential.helper
```

撤销：

```bash
git config --global --unset credential.helper
Remove-Item -LiteralPath "$HOME/.renpy-zh-credentials"
```
