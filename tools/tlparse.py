# -*- coding: utf-8 -*-
"""Parse Ren'Py translation templates into editable lines + translatable units."""
import os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TL = os.path.join(ROOT, "tl_template")


def find_strings(line):
    out, i, n = [], 0, len(line)
    while i < n:
        c = line[i]
        if c == "#":
            break
        if c in "\"'":
            q = c
            j, buf = i + 1, []
            while j < n:
                ch = line[j]
                if ch == "\\" and j + 1 < n:
                    buf.append(line[j:j+2]); j += 2; continue
                if ch == q:
                    break
                buf.append(ch); j += 1
            out.append((i, j + 1, q, "".join(buf)))
            i = j + 1
        else:
            i += 1
    return out


def unescape(s):
    out, i, n = [], 0, len(s)
    while i < n:
        if s[i] == "\\" and i + 1 < n:
            out.append(s[i+1]); i += 2
        else:
            out.append(s[i]); i += 1
    return "".join(out)


def parse(rel):
    """-> (lines, edits) where edits = [(line_idx, start, end, quote, text)]"""
    path = os.path.join(TL, rel.replace("/", os.sep))
    lines = open(path, encoding="utf-8-sig").read().split("\n")
    edits = []
    block_id = None
    for i, line in enumerate(lines):
        m = re.match(r'^translate\s+schinese\s+(\S+):', line)
        if m:
            block_id = m.group(1)
            continue
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or block_id is None:
            continue
        if block_id == "strings":
            mm = re.match(r'^(\s*new\s+")((?:[^"\\]|\\.)*)("\s*)$', line)
            if mm:
                edits.append((i, mm.start(2), mm.end(2), '"', mm.group(2)))
            continue
        for (s, e, q, raw) in find_strings(line):
            edits.append((i, s + 1, e - 1, q, raw))
    return lines, edits


def iter_all():
    for dirpath, _, fns in os.walk(TL):
        for fn in sorted(fns):
            if fn.endswith(".rpy"):
                p = os.path.join(dirpath, fn)
                yield os.path.relpath(p, TL).replace(os.sep, "/")


def load():
    """-> {rel: (lines, edits)} and a flat unique-text index."""
    files = {}
    order = []
    for rel in iter_all():
        lines, edits = parse(rel)
        files[rel] = (lines, edits)
        order.append(rel)
    return files, order


def unique_texts(files):
    """Ordered unique translatable texts, tagged with where they first occur."""
    seen, out = set(), []
    for rel, (_, edits) in files.items():
        for (_, _, _, _, text) in edits:
            if text in seen:
                continue
            seen.add(text)
            out.append((text, rel))
    return out
