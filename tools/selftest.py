# -*- coding: utf-8 -*-
"""Prove the guards in check.py actually fire.

    python tools/selftest.py

Every check in check.py is only worth having if it fails when it should. This
script injects one known-bad value per guard into a throwaway copy of the
database, runs check.py against it, and requires a non-zero exit each time.
Finally it restores the database and asserts the file is byte-identical to
what it was at the start.

The pristine copy is held in memory for the whole run. An earlier version of
this script backed the database up to a temp file and then re-copied that file
over itself in the cleanup, which silently persisted the corruption -- so the
restore path is asserted explicitly at the end.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "tl_trans.json")
GLOSSARY = os.path.join(ROOT, "docs", "glossary.json")
CHECK = os.path.join(ROOT, "tools", "check.py")
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")


def run_check():
    r = subprocess.run([sys.executable, CHECK], capture_output=True, env=ENV)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def write_db(tr):
    io.open(DB, "w", encoding="utf-8", newline="\n").write(
        json.dumps(tr, ensure_ascii=False))


def main():
    with open(DB, "rb") as f:
        pristine = f.read()
    base = json.loads(pristine.decode("utf-8"))

    # a short key: long enough for the width ratio rule, short enough not to be
    # exempt as prose
    short = next(k for k, v in base.items()
                 if 12 <= len(k) < 60
                 and any("\u4e00" <= c <= "\u9fff" for c in str(v)))
    cases = []

    g = json.loads(io.open(GLOSSARY, encoding="utf-8-sig").read())
    for section, terms in g.items():
        if section.startswith("_"):
            continue
        for en, spec in terms.items():
            for v in spec.get("banned", []):
                cases.append(("term", en, v))
            if len(spec["zh"]) >= 2:
                cases.append(("doubled", en, spec["zh"] + spec["zh"][-1]))

    cases += [
        ("mojibake", "mojibake", "\ufffd"),
        ("empty", "empty", "   "),
        ("untranslated", short, short),
        ("overflow", short, "\u4f60" * 80),
        ("doubled-space", short, "\u4f60\u4f60  \u4f60\u4f60"),
    ]

    missed = []
    try:
        for kind, label, payload in cases:
            tr = json.loads(pristine.decode("utf-8"))
            # every guard scans all values, so one throwaway entry is enough
            tr[short] = payload
            write_db(tr)
            code, _ = run_check()
            if code == 0:
                missed.append((kind, label, payload[:20]))
                print("  MISSED  %-13s %s" % (kind, label))
    finally:
        with open(DB, "wb") as f:
            f.write(pristine)

    code, _ = run_check()
    with open(DB, "rb") as f:
        intact = f.read() == pristine

    print("")
    print("guards fired on %d of %d injected faults"
          % (len(cases) - len(missed), len(cases)))
    print("database restored byte-identical: %s" % intact)
    print("check.py on the real database exits %d" % code)
    if missed or not intact or code != 0:
        return 1
    print("\nselftest passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
