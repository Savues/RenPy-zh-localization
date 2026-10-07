# -*- coding: utf-8 -*-
"""Check the docs hold together.

Two things: every relative markdown link resolves, and the generated game
table in the root README still matches what is under games/.

    python tools/check_links.py

Exits non-zero on any problem so it can gate a release.
"""
import glob
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games  # noqa: E402

os.chdir(games.ROOT)          # the glob below is repo-wide, so run from anywhere

LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

checked = broken = 0
for src in glob.glob("**/*.md", recursive=True):
    if ".git" in src or "tl_template" in src:
        continue
    base = os.path.dirname(src)
    with io.open(src, encoding="utf-8-sig") as f:
        text = f.read()
    for label, target in LINK.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path = target.split("#", 1)[0]
        if not path:
            continue
        checked += 1
        if not os.path.exists(os.path.normpath(os.path.join(base, path))):
            print("  BROKEN  %s -> %s" % (src, target))
            broken += 1

stale = 0
with io.open("README.md", encoding="utf-8") as f:
    readme = f.read()
if games.splice(readme, games.table()) != readme:
    print("  STALE   README.md 的已收录表格和 games/ 对不上"
          "——跑 python tools/games.py --readme")
    stale += 1

print("checked %d relative links, %d broken" % (checked, broken))
if stale:
    print("%d generated block(s) out of date" % stale)
sys.exit(1 if broken or stale else 0)
