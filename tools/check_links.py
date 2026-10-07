# -*- coding: utf-8 -*-
"""Check every relative markdown link in the repo resolves."""
import io, os, re, glob

LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
docs = glob.glob("**/*.md", recursive=True)
bad = 0
checked = 0
for src in docs:
    if ".git" in src or "tl_template" in src:
        continue
    base = os.path.dirname(src)
    for label, target in LINK.findall(io.open(src, encoding="utf-8-sig").read()):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path = target.split("#", 1)[0]
        if not path:
            continue
        checked += 1
        full = os.path.normpath(os.path.join(base, path))
        if not os.path.exists(full):
            print("  BROKEN  %s -> %s" % (src, target))
            bad += 1
print("checked %d relative links, %d broken" % (checked, bad))
