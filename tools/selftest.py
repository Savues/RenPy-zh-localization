# -*- coding: utf-8 -*-
"""Prove the guards in check.py actually fire.

    python tools/selftest.py --game <slug>

A check that never fails is decoration. This script runs check.py against the
real tree once and refuses to go further unless that exits 0. An earlier version
skipped the step, so it cheerfully reported "guards fired on 93 of 93 injected
faults" while check.py was already exiting 1 for an unrelated reason -- every
injection "worked" because the baseline was broken, and the number proved
nothing. That is how a glossary full of false positives survived a green
selftest.

It then injects one known-bad value per guard into a throwaway copy of the file
that guard actually reads, requires a non-zero exit each time, and finally
restores that file and asserts it is byte-identical to what it was at the start.
The pristine copy is held in memory for the whole run: an even earlier version
backed the database up to a temp file and then re-copied that file over itself
in the cleanup, which silently persisted the corruption -- so the restore path
is asserted explicitly, not assumed.

Where the injection goes depends on the game's patch layout, because the layout
is what decides which file each guard reads:

  tl-blocks       data/tl_trans.json for the database guards, plus one shipped
                  script for the tag-balance guard.
  script-override the shipped script for everything. There is no build input to
                  corrupt, which is the whole reason those games are not checked
                  through a database.

The case list comes from the game's own docs/glossary.json, minus whatever it
lists in _doubling_exempt: injecting a term the game has already declared
collides with ordinary prose would test the wrong thing.
"""
import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import games  # noqa: E402

CHECK = os.path.join(games.ROOT, "tools", "check.py")
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")

# Appended to the end of a shipped script. Column 0, a plain assignment, so the
# file stays a loadable Ren'Py script while check.py reads it as plain text.
LINE = '\nzz_selftest_probe = "%s"\n'


def run_check(slug):
    cmd = [sys.executable, CHECK] + (["--game", slug] if slug else [])
    r = subprocess.run(cmd, capture_output=True, env=ENV)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def read(p):
    with open(p, "rb") as f:
        return f.read()


def write(p, data):
    with open(p, "wb") as f:
        f.write(data)


def load_glossary(game):
    g = games.glossary(game)
    bad = [k for k, v in g.items()
           if not k.startswith("_") and not isinstance(v, dict)]
    if bad:
        sys.exit("%s: glossary sections must be objects, got %r"
                 % (game, bad))
    return g


def glossary_cases(game):
    """-> [(kind, label, payload)] harvested from the game's own glossary."""
    g = load_glossary(game)
    skip = set(games.doubling_exempt(game))
    cases = []
    for section, terms in g.items():
        if section.startswith("_") or not isinstance(terms, dict):
            continue
        for en, spec in terms.items():
            for variant in spec.get("banned", []):
                cases.append(("term", en, variant))
            z = spec["zh"]
            if len(z) >= 2 and z not in skip:
                cases.append(("doubled", en, z + z[-1]))
    return cases


def main(argv):
    slug, _ = games.take_slug(argv)
    game, manifest = games.manifest(slug)
    shape = games.layout(manifest)
    db = games.path_of(game, "data", "tl_trans.json")
    if shape == "tl-blocks" and not os.path.isfile(db):
        sys.exit("%s: a tl-blocks game needs %s" % (manifest["slug"], db))

    code, out = run_check(slug)
    if code:
        print("check.py on the real tree already exits %d. Fix that first --"
              " every injection below would 'fail' for that reason alone."
              % code)
        print(out)
        return 1

    entries = [e for e in games.patch_entries(game, manifest)
               if e[0].endswith(".rpy")]
    if not entries:
        sys.exit("no .rpy in the patch tree; nothing to inject into")
    probe_src, probe_rel = max(entries, key=lambda e: os.path.getsize(e[0]))

    # The glossary is enforced against the database for a tl-blocks patch and
    # against the shipped scripts for a script-override one, so the case has to
    # land in whichever file that patch is actually read from.
    target = "db" if shape == "tl-blocks" else "rpy"
    cases = [(kind, "glossary: " + label, target, payload)
             for kind, label, payload in glossary_cases(game)]
    cases.append(("tag", "unbalanced [i]", "rpy", "[i]probe"))

    if shape == "tl-blocks":
        base = json.loads(read(db).decode("utf-8-sig"))
        # long enough to be measured against its own width, short enough not to
        # be exempt as prose
        short = next(k for k, v in base.items()
                     if 12 <= len(k) < 60
                     and any("\u4e00" <= c <= "\u9fff" for c in str(v)))
        cases += [
            ("empty", "empty string", "db", "   "),
            ("mojibake", "U+FFFD", "db", "\ufffd"),
            ("untranslated", "value equals key", "db", short),
            ("overflow", "80 ideographs", "db", "\u4f60" * 80),
            ("doubled-space", "space between ideographs", "db", "\u4f60\u4f60  \u4f60\u4f60"),
        ]
    else:
        cases += [
            ("mojibake", "U+FFFD in a shipped script", "rpy", "\ufffd"),
            ("doubled-space", "space between ideographs", "rpy", "\u4f60\u4f60  \u4f60\u4f60"),
        ]

    pristine = {"db": read(db) if shape == "tl-blocks" else None,
                "rpy": read(probe_src)}
    missed = []
    try:
        for kind, label, where, payload in cases:
            if where == "db":
                tr = json.loads(pristine["db"].decode("utf-8-sig"))
                tr[short] = payload          # every guard scans every value
                io.open(db, "w", encoding="utf-8", newline="\n").write(
                    json.dumps(tr, ensure_ascii=False))
            else:
                text = pristine["rpy"].decode("utf-8-sig")
                io.open(probe_src, "w", encoding="utf-8", newline="\n").write(
                    text + LINE % payload)
            code, _ = run_check(slug)
            if code == 0:
                missed.append((kind, label))
                print("  MISSED  %-13s %s" % (kind, label))
    finally:
        if pristine["db"] is not None:
            write(db, pristine["db"])
        write(probe_src, pristine["rpy"])

    intact = all(read(p) == b for p, b in
                 ((db, pristine["db"]), (probe_src, pristine["rpy"]))
                 if b is not None)
    code, _ = run_check(slug)

    print("")
    print("injected into: %s%s" % (
        probe_rel, " + data/tl_trans.json" if shape == "tl-blocks" else ""))
    print("guards fired on %d of %d injected faults"
          % (len(cases) - len(missed), len(cases)))
    print("files restored byte-identical: %s" % intact)
    print("check.py on the real tree exits %d" % code)
    if missed or not intact or code != 0:
        return 1
    print("\nselftest passed")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
