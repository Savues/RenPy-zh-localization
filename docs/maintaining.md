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

```bash
# 1. 先只构建、不联网，确认包的内容和体积
python tools/publish_release.py --version v1.0.0 --dry-run

# 2. 正式上传
python tools/publish_release.py --version v1.0.0
```

只需要某一个游戏的包时，走 `package_release.py`：

```bash
python tools/package_release.py --game <slug> --version v1.0.0
```

写到 `dist/`，不联网。

### 重跑是安全的

- 资产按**文件名**匹配：内容一样就跳过（判定看的是文件大小），不一样就替换。
- 仓库里删掉的游戏，对应资产会被从 Release 上摘掉。
- **tag 只在不存在时创建**。已存在的 tag 不会被移动，所以一个已发布的版本永远指向它
  当时发布的那次提交。确实要让 tag 跟到最新提交，得自己动手：

  ```bash
  git tag -f v1.0.0 && git push -f origin v1.0.0
  ```

## 改动译文后的标准流程

```bash
python tools/build_tl.py --game <slug> \
  && python tools/check.py --game <slug> \
  && python tools/selftest.py --game <slug>
```

`build_tl.py` 不保证逐字节可复现：有些英文原文在译文库里登记了多个有意译法
（按上下文挑选），重建结果会随选择变化。`data/tl_trans.json` 和
`data/per_block_variants.json` 是这类决策的记录。

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
