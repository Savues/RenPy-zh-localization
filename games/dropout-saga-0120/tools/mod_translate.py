# -*- coding: utf-8 -*-
r"""Translate Shawn's Mod into Chinese, into a separate build.

MUST be run with the interpreter that ships inside the game:

    <game>\lib\py3-windows-x86_64\python.exe tools\mod_translate.py <game dir> [mod_zh.json] [outdir] [mod dir]

mod_zh.json defaults to data/mod_zh.json next to this file and outdir defaults
to out/mod.  The mod directory defaults to <game>\game\mod and is only read:
every .rpyc it holds is copied to outdir and rewritten there, so a mistake
costs a re-run and never the mod itself.

Why it cannot run on a normal Python
------------------------------------
The translation is applied by unpickling slot 1 and slot 2 of each .rpyc,
editing the AST in place and pickling it again.  That pickle has to be
readable by the engine, and the engine is Ren'Py 8.3 on Python 3.9.

renpy/object.py defines __getstate__/__setstate__ in Python, and on 3.11+
object.__getstate__ starts returning a (instance_dict, slot_dict) pair that
3.9 does not understand.  Re-pickling the same objects on 3.12 therefore
produces a file the game cannot load -- and it fails *silently*, because
renpy/script.py wraps the load in "except Exception: pass" and then reports
"Could not load file ...rpyc".  So the rewrite has to happen on the same
interpreter that will read the result.
"""
import glob
import hashlib
import json
import os
import shutil
import struct
import sys
import zlib

USAGE = "mod_translate.py <game dir> [mod_zh.json] [outdir] [mod dir]"

if len(sys.argv) < 2:
    sys.stderr.write(USAGE + "\n")
    sys.exit(2)

GAME = os.path.abspath(sys.argv[1])
if not os.path.isdir(os.path.join(GAME, "game")):
    sys.stderr.write("%s is not a Ren'Py game directory\n" % GAME)
    sys.exit(2)

MOD = os.path.join(GAME, "game", "mod")
HERE = os.path.dirname(os.path.abspath(__file__))
ZH = os.path.abspath(sys.argv[2] if len(sys.argv) > 2
                     else os.path.join(HERE, os.pardir, "data", "mod_zh.json"))
OUT = os.path.abspath(sys.argv[3] if len(sys.argv) > 3
                      else os.path.join(HERE, os.pardir, "out", "mod"))
MOD = os.path.abspath(sys.argv[4]) if len(sys.argv) > 4 else MOD

sys.path.insert(0, GAME)
os.chdir(GAME)


def boot_renpy():
    """Import enough of Ren'Py that every pickled class can be resolved.

    Ren'Py's modules import each other in a fixed order; importing them in the
    wrong order trips AttributeError on a partially initialised parent package.
    Rather than hard-coding that order, keep importing whatever module the
    error names until it settles.
    """
    import renpy  # noqa: F401
    wanted = [
        "renpy.config", "renpy.object", "renpy.revertable", "renpy.rollback",
        "renpy.python", "renpy.util", "renpy.game", "renpy.ast", "renpy.parser",
        "renpy.translation", "renpy.atl", "renpy.style", "renpy.color",
        "renpy.easy", "renpy.display.displayable", "renpy.display.core",
        "renpy.display.layout", "renpy.display.transform", "renpy.text.font",
        "renpy.text.textsupport", "renpy.text.text", "renpy.ui",
        "renpy.sl2.slast", "renpy.script", "renpy.loader",
        "renpy.compat.pickle",
    ]
    done = set()
    for _ in range(400):
        try:
            for name in wanted:
                if name not in done:
                    __import__(name)
                    done.add(name)
            return
        except AttributeError as e:
            parts = str(e).split("'")
            if len(parts) < 4:
                raise
            full = parts[1] + "." + parts[3]
            if full in done:
                raise
            __import__(full)
            done.add(full)
    raise RuntimeError("Ren'Py import did not settle")


boot_renpy()

import renpy.ast
import renpy.compat.pickle as rpickle
import renpy.game
import renpy.sl2.slast as slast


# PyExpr.__new__ pushes itself onto renpy.game.script.all_pyexpr; outside a real
# bootstrap there is no Script object, so stand one up.
class _NoScript(object):
    all_pyexpr = None
    all_pycode = None
    seen_pycode = set()
    record_pycode = False
    pycode_list = []
    seen_statement = False
    compiling = False


# renpy.revertable's mutator wrapper reads renpy.game.log.mutated on every
# in-place container mutation, and unpickling a RevertableDict is exactly
# that.  No real log exists outside bootstrap, so give it an empty one.
class _NoLog(object):
    mutated = {}
    hard_rollback = False
    rollback = None
    is_rollback = False


if renpy.game.script is None:
    renpy.game.script = _NoScript()
if renpy.game.log is None:
    renpy.game.log = _NoLog()

PyExpr = renpy.ast.PyExpr
RPYC2_HEADER = b"RENPY RPC2"

TEXT_KEYS = ("text", "text_button", "tooltip", "alt_text", "label", "title")
TEXT_DISPLAYABLES = ("text", "textbutton", "label", "key", "input")


# ---------------------------------------------------------------- container

def read_slots(path):
    """Return ({slot: compressed payload}, trailing md5, header block)."""
    size = hashlib.md5().digest_size
    with open(path, "rb") as f:
        raw = f.read()
    tail = raw[-size:]
    body = raw[:-size]
    slots = {}
    pos = len(RPYC2_HEADER)
    while True:
        slot, start, length = struct.unpack("III", body[pos:pos + 12])
        pos += 12
        if slot == 0:
            break
        slots[slot] = body[start:start + length]
    # pos must land past the zero terminator: Ren'Py's reader walks slot entries
    # until it meets slot 0, so a header without it is malformed.
    return slots, tail, body[:pos]


def write_slots(path, payloads, tail, header):
    """Mirror renpy/script.py write_rpyc_header/write_rpyc_data/write_rpyc_md5."""
    with open(path, "wb") as f:
        f.write(header)
        for slot in (1, 2):
            f.seek(0, 2)
            start = f.tell()
            data = zlib.compress(payloads[slot], 3)
            f.write(data)
            f.seek(len(RPYC2_HEADER) + 12 * (slot - 1), 0)
            f.write(struct.pack("III", slot, start, len(data)))
        f.seek(0, 2)
        f.write(tail)


def load_slots(path):
    slots, tail, header = read_slots(path)
    out = {}
    for slot in (1, 2):
        if slot in slots:
            out[slot] = rpickle.loads(zlib.decompress(slots[slot]))
    return out, tail, header


# ------------------------------------------------------------------- strings

def string_literals(expr):
    import ast as pyast
    if not isinstance(expr, str):
        return []
    try:
        tree = pyast.parse(expr.strip(), mode="eval")
    except (SyntaxError, ValueError):
        return []
    return [n.value for n in pyast.walk(tree)
            if isinstance(n, pyast.Constant) and isinstance(n.value, str)
            and n.value.strip()]


def rewrite_literals(expr, mapping):
    """Swap string constants inside an expression, leaving the rest untouched."""
    import ast as pyast
    if not isinstance(expr, str):
        return expr
    src = expr.strip()
    try:
        tree = pyast.parse(src, mode="eval")
    except (SyntaxError, ValueError):
        return expr
    if not isinstance(tree.body, pyast.Constant):
        return expr
    old = tree.body.value
    if not isinstance(old, str) or old not in mapping:
        return expr
    new = mapping[old]
    if new == old:
        return expr
    q = '"' if ('"' not in new and "\\" not in new) else "'"
    if q in new or "\\" in new:
        new = new.replace("\\", "\\\\").replace(q, "\\" + q)
    return q + new + q


def restr(value, new):
    """Rebuild a PyExpr in place of the old value, keeping its source location."""
    if isinstance(value, PyExpr):
        return PyExpr(new, value.filename, value.linenumber, value.py)
    return new


def replace_tuple_item(items, index, sub, new):
    """items[i][sub] = new -- menu captions are 3-tuples, so rebuild the tuple."""
    item = list(items[index])
    item[sub] = new
    items[index] = tuple(item)


# ---------------------------------------------------------------------- walk

SKIP_FIELDS = ("next", "statement_start", "after", "parsed", "alt", "source",
               "location", "filename", "linenumber", "name")


def slots_of(cls):
    """Every __slots__ name reachable through cls, nearest class first."""
    out = []
    for k in cls.__mro__:
        s = k.__dict__.get("__slots__")
        if s is None:
            continue
        if isinstance(s, str):
            s = (s,)
        out.extend(s)
    return out


_SLOT_CACHE = {}


def fields(node):
    """Every readable attribute of node.

    Ren'Py's AST and screen-language nodes all declare __slots__, so vars()
    raises TypeError on them; the dict entries (when any) are merged in.
    """
    d = {}
    try:
        d.update(vars(node))
    except TypeError:
        pass
    cls = type(node)
    names = _SLOT_CACHE.get(cls)
    if names is None:
        names = _SLOT_CACHE[cls] = slots_of(cls)
    for name in names:
        if name in ("__dict__", "__weakref__"):
            continue
        try:
            d[name] = getattr(node, name)
        except AttributeError:
            pass
    return d


def scan(stmts):
    """Yield (node, field, index, sub, kind, text) for every editable string.

    Mirrors tools/mod_strings.py exactly, so the extraction that produced
    mod_units.json and this rewriter address the same slots.
    """
    seen = set()

    def visit(node):
        if isinstance(node, PyExpr):
            return
        if isinstance(node, dict):
            if id(node) in seen:
                return
            seen.add(id(node))
            for v in node.values():
                for x in visit(v):
                    yield x
            return
        if isinstance(node, (list, tuple, set, frozenset)):
            if id(node) in seen:
                return
            seen.add(id(node))
            for v in node:
                for x in visit(v):
                    yield x
            return
        if id(node) in seen:
            return
        seen.add(id(node))

        st = fields(node)
        if not st:
            return

        cls = type(node)

        if isinstance(node, renpy.ast.PyCode):
            source = getattr(node, "source", None)
            if isinstance(source, str) and source.strip():
                yield (node, "source", None, None, "python", source)

        elif isinstance(node, renpy.ast.Say):
            what = st.get("what")
            if isinstance(what, str):
                yield (node, "what", None, None, "say", what)
            elif isinstance(what, list):
                for i, part in enumerate(what):
                    if isinstance(part, str):
                        yield (node, "what", i, None, "say", part)
            for key in ("attributes", "temporary_attributes"):
                v = st.get(key)
                if isinstance(v, list):
                    for i, part in enumerate(v):
                        if isinstance(part, str):
                            yield (node, key, i, None, "attr", part)
                elif isinstance(v, str):
                    yield (node, key, None, None, "attr", v)

        elif isinstance(node, renpy.ast.Menu):
            for i, it in enumerate(st.get("items") or []):
                if isinstance(it, tuple) and it and isinstance(it[0], str):
                    yield (node, "items", i, 0, "menu", it[0])
            if isinstance(st.get("set"), str):
                yield (node, "set", None, None, "menu_set", st["set"])

        elif isinstance(node, renpy.ast.UserStatement):
            line = st.get("line")
            if isinstance(line, str):
                yield (node, "line", None, None, "userstatement", line)

        elif isinstance(node, renpy.ast.Style):
            for k, v in sorted((st.get("properties") or {}).items()):
                if isinstance(v, str):
                    yield (node, "properties", None, k, "style", k + "\x00" + v)

        elif isinstance(node, slast.SLDisplayable):
            if st.get("name") in TEXT_DISPLAYABLES:
                for i, e in enumerate(st.get("positional") or []):
                    yield (node, "positional", i, None, "expr", e)
            for i, kw in enumerate(st.get("keyword") or []):
                if isinstance(kw, tuple) and len(kw) == 2 and kw[0] in TEXT_KEYS:
                    yield (node, "keyword", i, 1, "expr", kw[1])
            for k in sorted(st.get("default_keywords") or {}):
                if k in TEXT_KEYS:
                    yield (node, "default_keywords", k, None, "expr",
                           st["default_keywords"][k])

        elif isinstance(node, slast.SLIf):
            for i, it in enumerate(st.get("entries") or []):
                if isinstance(it, tuple) and isinstance(it[0], str):
                    yield (node, "entries", i, 0, "expr", it[0])

        elif isinstance(node, slast.SLDefault):
            e = st.get("expression")
            if isinstance(e, PyExpr):
                yield (node, "expression", None, None, "expr", str(e))

        for k, v in st.items():
            if k in SKIP_FIELDS:
                continue
            for x in visit(v):
                yield x

    for s in stmts or ():
        for item in visit(s):
            yield item


# --------------------------------------------------------------------- apply

def _store(node, field, index, sub, value):
    if sub == 0 and field in ("items", "entries"):
        replace_tuple_item(getattr(node, field), index, sub, restr(None, value))
    elif sub == 1 and field == "keyword":
        replace_tuple_item(node.keyword, index, sub, restr(None, value))
    elif index is None:
        setattr(node, field, restr(getattr(node, field, None), value))
    else:
        container = getattr(node, field)
        container[index] = restr(container[index], value)
        setattr(node, field, container)


def apply_to(path, table, outpath):
    """Rewrite both slots of one .rpyc into outpath using the table."""
    objs, tail, header = load_slots(path)
    counts = {}
    for slot in (1, 2):
        if slot not in objs:
            continue
        data, stmts = objs[slot]
        for node, field, index, sub, kind, text in scan(stmts):
            if kind == "expr":
                mapping = {}
                for lit in string_literals(text):
                    t = table.get(lit)
                    if t and t != lit:
                        mapping[lit] = t
                if not mapping:
                    continue
                new = rewrite_literals(text, mapping)
                if new == text:
                    continue
                _store(node, field, index, sub, new)
                counts[kind] = counts.get(kind, 0) + 1
                continue
            if kind == "style":
                prop, _, val = text.partition("\x00")
                t = table.get(val)
                if not t or t == val:
                    continue
                props = dict(node.properties)
                props[prop] = t
                node.properties = props
                counts[kind] = counts.get(kind, 0) + 1
                continue
            t = table.get(text)
            if not t or t == text:
                continue
            _store(node, field, index, sub, t)
            counts[kind] = counts.get(kind, 0) + 1

    payloads = {slot: rpickle.dumps(objs[slot]) for slot in objs}
    write_slots(outpath, payloads, tail, header)
    return counts


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if not os.path.isdir(MOD):
        sys.stderr.write("no mod directory at %s\n" % MOD)
        sys.stderr.write("install Shawn's Mod into game/mod first\n")
        sys.exit(2)
    sources = sorted(glob.glob(os.path.join(MOD, "*.rpyc")))
    if not sources:
        sys.stderr.write("%s holds no .rpyc\n" % MOD)
        sys.exit(2)

    table = json.load(open(ZH, encoding="utf-8"))
    print("table   %s (%d pairs)" % (ZH, len(table)))
    print("source  %s (%d files)" % (MOD, len(sources)))

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(MOD, OUT)
    total = {}
    for path in sources:
        dst = os.path.join(OUT, os.path.basename(path))
        counts = apply_to(path, table, dst)
        for k, v in counts.items():
            total[k] = total.get(k, 0) + v
        print("  %-26s %s" % (os.path.basename(path), counts or "-"))
    print("total rewritten:", total)
    print("built ->", OUT)


if __name__ == "__main__":
    main()
