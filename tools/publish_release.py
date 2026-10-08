# -*- coding: utf-8 -*-
"""Publish every game's patch to one GitHub release.

    python tools/publish_release.py [--version v1.0.0] [--repo OWNER/NAME]
    python tools/publish_release.py --dry-run

A release is the *collection*, not a single game: adding a second game to the
repository must not turn into a second release, so this walks games/ , builds
each patch, and attaches them all under the same tag.

The release body stays generic on purpose. It lists which games are in the
collection and how to install a patch; per-game detail (coverage counts,
screens, credits) belongs in the game's own README inside the zip and in the
repository, where it can be updated without rewriting a published release.

Re-running is safe: assets are matched by name, replaced when they differ, and
removed when the game they belonged to is gone. The tag is only ever moved when
it does not exist yet -- an existing tag is left alone so that a published
version keeps pointing at the commit it was published from.

The token is read from the git credential store (see README, "推送凭据") and is
never printed.
"""
import argparse
import hashlib
import io
import json
import os
import ssl
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games              # noqa: E402
import package_release    # noqa: E402

API = "https://api.github.com"
UPLOADS = "https://uploads.github.com"

# Windows is the only platform this has been exercised on; the credential file
# layout is git's, so the same parsing works anywhere git wrote one.
CRED_HINT = os.path.expanduser("~/.renpy-zh-credentials")


def ssl_context():
    """The interpreter these tools run under is a mingw build: it has no CA
    file and no Windows certificate store to fall back on, so every HTTPS
    call dies on certificate verification. certifi ships in the same tree."""
    if os.environ.get("SSL_CERT_FILE"):
        return None
    try:
        import certifi
    except ImportError:
        return None
    return ssl.create_default_context(cafile=certifi.where())


SSL = ssl_context()


class GitHub(object):
    def __init__(self, repo, token):
        self.repo = repo
        self.token = token

    def _call(self, url, method="GET", payload=None, raw=None, ctype=None):
        hdr = {
            "Authorization": "token " + self.token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "renpy-zh-localization",
        }
        body = None
        if raw is not None:
            body, hdr["Content-Type"] = raw, ctype
        elif payload is not None:
            body, hdr["Content-Type"] = json.dumps(payload).encode("utf-8"), \
                "application/json"
        req = urllib.request.Request(url, data=body, headers=hdr, method=method)
        try:
            with urllib.request.urlopen(req, context=SSL) as r:
                text = r.read().decode("utf-8")
                return r.status, (json.loads(text) if text else {})
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            try:
                return e.code, json.loads(body)
            except ValueError:
                return e.code, body

    def release_by_tag(self, tag):
        return self._call("%s/repos/%s/releases/tags/%s"
                          % (API, self.repo, tag))

    def create_release(self, tag, sha, name, body):
        return self._call("%s/repos/%s/releases" % (API, self.repo), "POST", {
            "tag_name": tag, "target_commitish": sha,
            "name": name, "body": body,
            "draft": False, "prerelease": False,
        })

    def update_release(self, rid, **fields):
        return self._call("%s/repos/%s/releases/%s" % (API, self.repo, rid),
                          "PATCH", fields)

    def delete_asset(self, aid):
        return self._call("%s/repos/%s/releases/assets/%s"
                          % (API, self.repo, aid), "DELETE")

    def upload(self, rid, path, name, data):
        url = "%s/repos/%s/releases/%s/assets?name=%s" % (
            UPLOADS, self.repo, rid, urllib.parse.quote(name))
        return self._call(url, "POST", raw=data, ctype="application/zip")


def read_token():
    """Pull the token out of the git credential store file.

    git's store helper writes:
        protocol=https
        host=github.com
        username=x-access-token
        password=<TOKEN>
    """
    path = os.environ.get("GITHUB_CREDENTIAL_FILE") or CRED_HINT
    if not os.path.isfile(path):
        sys.exit("no credential file at %s -- see README, 推送凭据" % path)
    text = io.open(path, encoding="utf-8").read()
    for line in text.splitlines():
        if line.lower().startswith("password="):
            tok = line.split("=", 1)[1].strip()
            if tok:
                return tok
        # also accept the one-line URL form: https://user:TOKEN@host
        if "@" in line and "://" in line:
            tok = line.split("://", 1)[1].split(":", 1)[-1].split("@", 1)[0]
            if tok:
                return tok
    sys.exit("no token found in %s" % path)


def head_sha():
    return subprocess.run(["git", "-C", games.ROOT, "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def git_remote_repo():
    url = subprocess.run(
        ["git", "-C", games.ROOT, "remote", "get-url", "origin"],
        capture_output=True, text=True).stdout.strip()
    url = url[:-4] if url.endswith(".git") else url
    return url.split("github.com/")[-1].strip("/")


def render_body(rows, version, repo):
    """Generic on purpose -- see the module docstring."""
    lines = [
        "## Ren&#39;Py 游戏中文汉化补丁 %s" % version,
        "",
        "一个 Release 收录**全部**已收录游戏的汉化补丁，每个游戏一个独立压缩包。",
        "新增游戏只会往这个列表里加一行，不会多出一个 Release。",
        "",
        "| 类型 | 游戏 | 内容 | 语言 | 压缩包 |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        if r["kind"] == "patch":
            lines.append("| 主包 | %s | 完整汉化补丁 | %s | `%s` |"
                         % (r["title"], r["language_name"], r["asset"]))
        else:
            lines.append("| 可选包 | %s | %s | %s | `%s` |"
                         % (r["for_title"], r["label"], r["language_name"],
                            r["asset"]))

    optional = any(r["kind"] == "extra" for r in rows)
    lines += [
        "",
        "### 安装",
        "",
        "**主包**是直接覆盖用的：解压后把里面的 `game/` 文件夹内容复制到游戏的",
        "`game/` 文件夹，选择覆盖即可。不需要 Python、安装器或联网，中文字体已包含在",
        "包内。每个包里的 `README.md` 写有该游戏的详细步骤与常见问题。",
        "",
    ]
    if optional:
        lines += [
            "**可选包**是第三方 MOD 的汉化，与主补丁**没有依赖关系**，装不装都行，",
            "各装各的。它们不是让你覆盖 `game/` 的，解压后按里面 `README.md` 的说明",
            "操作即可；没装对应 MOD 的玩家直接忽略。",
            "",
        ]
    lines += [
        "### 版权与免责",
        "",
        "游戏版权归各自作者所有。本仓库收录的汉化补丁均为**非官方的同人翻译作品**，",
        "与任何游戏厂商无任何关联，仅供学习交流使用，请自行确认当地法律与原作方的",
        "授权状况。",
        "",
        "各压缩包不包含游戏的程序文件、图像、音频或原始脚本，只包含翻译补丁与中文字体。",
        "请勿将补丁与游戏本体一同分发。中文字体的版权声明见各包内的 `FONT-LICENSE.txt`。",
        "",
        "---",
        "",
        "翻译过程与术语记录见仓库",
        "[`games/`](https://github.com/%s/tree/main/games)。" % repo,
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--version", default="v1.0.0")
    ap.add_argument("--repo", default=None,
                    help="OWNER/NAME; defaults to the origin remote")
    ap.add_argument("--dry-run", action="store_true",
                    help="build the zips and print the plan, touch nothing")
    args = ap.parse_args()

    repo = args.repo or git_remote_repo()
    slugs = games.slugs()
    if not slugs:
        sys.exit("no games under %s" % games.GAMES)

    rows = []
    for slug in slugs:
        _, m = games.manifest(slug)
        out, entries, _ = package_release.build(slug, args.version)
        with io.open(out, "rb") as f:
            data = f.read()
        rows.append({
            "slug": slug, "manifest": m, "path": out, "data": data,
            "asset": os.path.basename(out),
            "title": m["title"], "author": m["author"],
            "language_name": m["language_name"],
            "sha256": hashlib.sha256(data).hexdigest(),
            "size": len(data), "files": len(entries),
            "kind": "patch",
        })
        print("built %-42s %8.2f MB  %s"
              % (rows[-1]["asset"], len(data) / 1048576, rows[-1]["sha256"][:16]))

        # Optional packages ride along in the same release: a player who wants
        # the mod translation should not have to find a second page.
        for extra in package_release.build_extras(slug, args.version):
            with io.open(extra["path"], "rb") as f:
                edata = f.read()
            rows.append({
                "slug": slug, "manifest": m, "path": extra["path"],
                "data": edata, "asset": extra["meta"]["asset"],
                "for_title": m["title"], "label": extra["meta"]["label"],
                "language_name": m["language_name"],
                "sha256": hashlib.sha256(edata).hexdigest(),
                "size": len(edata), "files": len(extra["entries"]),
                "kind": "extra",
            })
            print("opt    %-42s %8.2f MB  %s"
                  % (rows[-1]["asset"], len(edata) / 1048576,
                     rows[-1]["sha256"][:16]))

    body = render_body(rows, args.version, repo)
    tag = args.version
    print("\nrelease %s -> %d game(s), %d package(s)"
          % (tag, len(slugs), len(rows)))

    if args.dry_run:
        print("\n--- body ---\n" + body)
        return 0

    gh = GitHub(repo, read_token())
    sha = head_sha()

    st, rel = gh.release_by_tag(tag)
    if st == 200:
        rid = rel["id"]
        print("updating release %d" % rid)
        st, _ = gh.update_release(
            rid, name="Ren'Py 游戏中文汉化补丁 %s" % tag, body=body)
        if st not in (200, 201):
            sys.exit("update failed: %s" % st)
        have = {a["name"]: a for a in rel.get("assets", [])}
    elif st == 404:
        st, rel = gh.create_release(
            tag, sha, "Ren'Py 游戏中文汉化补丁 %s" % tag, body)
        if st not in (200, 201):
            sys.exit("create failed: %s\n%s" % (st, rel))
        rid = rel["id"]
        print("created release %d  %s" % (rid, rel["html_url"]))
        have = {}
    else:
        sys.exit("cannot read release: %s\n%s" % (st, rel))

    wanted = {r["asset"]: r for r in rows}
    for name, a in have.items():
        if name not in wanted:
            print("  drop   %s" % name)
            gh.delete_asset(a["id"])

    for name, r in sorted(wanted.items()):
        old = have.get(name)
        if old and old.get("size") == r["size"]:
            print("  keep   %s (unchanged)" % name)
            continue
        if old:
            print("  replace %s" % name)
            gh.delete_asset(old["id"])
        st, asset = gh.upload(rid, r["path"], name, r["data"])
        if st not in (200, 201):
            sys.exit("upload failed: %s\n%s" % (st, asset))
        print("  upload %s  %d bytes" % (name, asset["size"]))

    print("\ndone: https://github.com/%s/releases/tag/%s" % (repo, tag))
    return 0


if __name__ == "__main__":
    sys.exit(main())
