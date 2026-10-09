# -*- coding: utf-8 -*-
"""Locate a game folder inside games/ and read its manifest.

Every tool takes the same optional --game <slug>; with a single game in the
repository the slug can be omitted. Adding a second game means dropping a new
folder under games/ with a game.json -- no tool changes required.

Running this file rewrites the "already in" table in the root README from
whatever is under games/:

    python tools/games.py --readme

check_links.py fails when that table has drifted, so the table cannot rot
unnoticed when a game is added.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAMES = os.path.join(ROOT, "games")
README = os.path.join(ROOT, "README.md")

# The generated block of README.md. Everything between the two markers is
# owned by table() below and must not be hand-edited.
START = "<!-- games:start -->"
END = "<!-- games:end -->"


def slugs():
    if not os.path.isdir(GAMES):
        return []
    return sorted(
        name for name in os.listdir(GAMES)
        if os.path.isfile(os.path.join(GAMES, name, "game.json")))


def resolve(slug=None):
    """-> absolute path of games/<slug>."""
    available = slugs()
    if not available:
        sys.exit("no games found under %s" % GAMES)
    if slug:
        path = os.path.join(GAMES, slug)
        if slug not in available:
            sys.exit("unknown game %r; available: %s" % (slug, ", ".join(available)))
        return path
    if len(available) == 1:
        return os.path.join(GAMES, available[0])
    sys.exit("this repository has %d games (%s); pass --game <slug>"
             % (len(available), ", ".join(available)))


def manifest(slug=None):
    """-> (game_dir, parsed game.json)."""
    game = resolve(slug)
    with open(os.path.join(game, "game.json"), encoding="utf-8-sig") as f:
        return game, json.load(f)


def path_of(game_dir, *parts):
    return os.path.join(game_dir, *parts)


def take_slug(argv, flag="--game"):
    """Pull --game <slug> out of argv, whatever order it appears in."""
    slug = None
    rest = []
    i = 0
    while i < len(argv):
        if argv[i] == flag:
            if i + 1 >= len(argv):
                sys.exit("%s needs a value" % flag)
            slug = argv[i + 1]
            i += 2
            continue
        if argv[i].startswith(flag + "="):
            slug = argv[i].split("=", 1)[1]
            i += 1
            continue
        rest.append(argv[i])
        i += 1
    return slug, rest


def translations(game_dir):
    """-> {english: chinese}, or {} when the game has no database yet."""
    db = path_of(game_dir, "data", "tl_trans.json")
    if not os.path.isfile(db):
        return {}
    with io.open(db, encoding="utf-8-sig") as f:
        return json.load(f)


def glossary(game_dir):
    """-> the parsed docs/glossary.json, or {} when the game has none."""
    path = path_of(game_dir, "docs", "glossary.json")
    if not os.path.isfile(path):
        return {}
    with io.open(path, encoding="utf-8-sig") as f:
        return json.load(f)


def _list_section(game_dir, key):
    """-> the strings in one _-prefixed list section of the glossary."""
    v = glossary(game_dir).get(key)
    return [x for x in v if isinstance(x, str)] if isinstance(v, list) else []


def kept_verbatim(game_dir):
    """-> strings this game keeps in English on purpose.

    Per game, because the reason is per game: Eden keeps its supporter
    credits, Sinful Summer keeps its key hints, Cosy Cafe keeps its RGB
    picker format strings. A shared table used to hold all of them at once and
    each game's oddities counted as the other two games' prose.
    """
    return _list_section(game_dir, "_kept_verbatim")


def tag_exempt(game_dir):
    """-> exact patch lines whose unbalanced tags are the game's own fault.

    The Inn ships `old "Calibrating [name] ([i]/[total])"`: [i] there is a
    variable, not italics, and the warning it produces cannot be removed from
    the translation without breaking the match. Lines are listed verbatim,
    stripped, so the exemption is as narrow as the defect.
    """
    return _list_section(game_dir, "_tag_exempt")


def doubling_exempt(game_dir):
    """-> canonical terms whose "<term><last char>" shape is ordinary prose.

    「校长 长得」reads as 校长长, 「把莎拉拉近一点」is 莎拉 + 拉近. The game
    names those; the checker does not try to tell them apart on its own.
    """
    return _list_section(game_dir, "_doubling_exempt")


# ---------------------------------------------------------------------------
# How a game gets patched. The two shapes that exist in the wild are not
# interchangeable, so game.json declares which one it is and the tools branch
# on it instead of guessing from whatever happens to be under patch/.
#
#   tl-blocks       the stock route. patch/tl/<lang>/ holds generated
#                   `translate` blocks, and data/tl_trans.json is the input
#                   build_tl.py consumes.
#   script-override the game ships no translation templates, so the patch
#                   replaces the game's own scripts instead. patch/game/
#                   mirrors the game's game/ directory, and any
#                   data/tl_trans.json is a by-product of the finished scripts
#                   rather than something anything builds from.
#
# "installer" says which installer the docs should send people to. The shared
# tools/install.py only knows how to place a tl tree, a shim and fonts; a
# script-override game needs its own installer next to its patch.
# ---------------------------------------------------------------------------
LAYOUTS = ("tl-blocks", "script-override")

# How each one is described in the README table. Both exist on purpose and
# neither is the default to steer people towards.
SHAPE_LABEL = {"tl-blocks": "translate 块",
               "script-override": "脚本覆盖"}


def patch_version(manifest):
    """-> this game's own package version, as an int. Absent means 1.

    Deliberately not the release tag. A release collects every game in the
    repository, so its tag moves whenever any one of them changes; stamping
    that number on every package would rename and rebuild all of them each
    time, including the ones whose bytes did not move at all. The batch lives
    in the release, the version lives here, and nothing inside a package is
    allowed to depend on the batch.
    """
    raw = manifest.get("patch_version", 1)
    try:
        v = int(raw)
    except (TypeError, ValueError):
        v = 0
    if v < 1:
        sys.exit("%s: patch_version must be an integer >= 1, not %r"
                 % (manifest.get("slug", "?"), raw))
    return v


def package_version(manifest):
    """-> "v3": the label that goes into the package name and its README."""
    return "v%d" % patch_version(manifest)


def layout(manifest):
    """-> 'tl-blocks' or 'script-override'. Exits on anything undeclared."""
    v = manifest.get("patch_layout", "tl-blocks")
    if v not in LAYOUTS:
        sys.exit("%s: patch_layout must be one of %s, not %r"
                 % (manifest.get("slug", "?"), ", ".join(LAYOUTS), v))
    return v


def installer(manifest):
    """-> 'py' (the shared tools/install.py) or 'ps1' (a game-local one)."""
    return manifest.get("installer", "py")


def font_plan(manifest):
    """-> [(repo-relative asset path, [filenames to write it under)].

    font_assets is the general form: one entry per face, each naming every
    filename the game looks that face up under. The older font_asset +
    patch_font + font_shadow triple says the same thing for the common case of
    one face that has to be shadowed under several names, and still works.
    """
    rich = manifest.get("font_assets")
    if rich:
        return [(a["path"], list(a["names"])) for a in rich]
    asset = manifest.get("font_asset")
    if not asset:
        return []
    names = [manifest.get("patch_font", "zh.ttf")]
    for n in manifest.get("font_shadow", []):
        if n not in names:
            names.append(n)
    return [(asset, names)]


SKIP_SUFFIX = (".rpyc", ".rpymc", ".rpyb", ".pyc")


def patch_entries(repo, manifest):
    """-> [(absolute source path, path relative to the game's game/ dir)].

    The second element is always game-relative, so packaging only has to
    prefix "game/" and both layouts land in the right place. Getting this
    wrong is not cosmetic: a script-override patch one directory too deep is
    silently ignored by Ren'Py, and the player just gets the untranslated game
    with no error anywhere.
    """
    patch_root = path_of(repo, "patch")
    lang = manifest["language"]
    out = []

    # The shim always sits at patch/<shim> and lands at the game root.
    shim = manifest["shim"]
    shim_src = path_of(patch_root, shim)
    if os.path.isfile(shim_src):
        out.append((shim_src, shim))

    if layout(manifest) == "script-override":
        # patch/game/ *is* the game's own game/ directory, contents and all.
        sub = path_of(patch_root, "game")
        prefix = ""
    else:
        sub = path_of(patch_root, "tl", lang)
        prefix = "tl/%s/" % lang

    for dirpath, dirnames, filenames in os.walk(sub):
        dirnames[:] = sorted(d for d in dirnames
                             if d not in ("__pycache__", ".git"))
        for fn in sorted(filenames):
            if fn.startswith(".") or fn.endswith(SKIP_SUFFIX):
                continue
            src = os.path.join(dirpath, fn)
            rel = os.path.relpath(src, sub).replace(os.sep, "/")
            out.append((src, prefix + rel))

    return sorted(out, key=lambda e: e[1])


def row(slug):
    """-> one markdown row describing games/<slug> for the root README."""
    game, m = manifest(slug)
    shape = layout(m)
    cov = m.get("coverage")
    if cov:
        # A game that does not build from a translation database cannot have
        # its coverage derived from one. Counting a by-product dictionary
        # reports a number with nothing to do with what actually ships -- and,
        # worse, one that stays green no matter what is wrong with the patch.
        total = int(cov["total"])
        left = max(0, total - int(cov["translated"]))
        # "verbatim" is for the strings a script-override patch deliberately
        # leaves in English: interpolation-only text, Ren'Py's own Preference
        # keys, in-world German. They are counted as coverage because the
        # English release counted them, and calling them untranslated would be
        # the one thing this table must never do. Only games that measure
        # coverage themselves can set it; a database-built game derives the
        # same set from the database instead.
        kept = int(cov.get("verbatim") or 0)
    else:
        tr = translations(game)
        # Imported here rather than at module level: check.py imports games, so
        # a top-level import would be circular. Only this one test needs it, and
        # it has to be check.py's own -- a second copy of KEEP/keep() here would
        # drift, and a drifted copy does not stay harmless, it quietly starts
        # calling finished translations untranslated.
        import check
        exact = kept_verbatim(game)
        total = len(tr)
        left = sum(1 for k, v in tr.items()
                   if not check.keep(k, v, exact) and v == k)
        kept = 0
    # A game added before any translating has no numbers yet. Reporting that
    # as ✅ 100% would be a lie that also passes check_links.py.
    if not total:
        state = "\U0001f6a7 待翻译"
    elif kept and left <= kept:
        state = "✅ 100%%（%s 条保留原文）" % "{:,}".format(kept)
    elif left:
        state = "⚠️ %d 条未译" % left
    else:
        state = "✅ 100%"
    # A patch that revises a translation the publisher already ships is not
    # the same thing as one translated from the English, and a table that calls
    # both "100%" says nothing about which is which. Game.json opts in with
    # base_translation; games without it render exactly as before.
    shape_label = SHAPE_LABEL[shape]
    base = m.get("base_translation")
    if base:
        shape_label += " †"
    return "| [%s](games/%s/) | %s | %s | %s | %s | %s 条 |" % (
        m["title"], slug, m["author"], m["language_name"],
        shape_label, state, "{:,}".format(total))


def table():
    """-> the markdown block that belongs between the README's markers."""
    return "\n".join(
        ["| 游戏 | 原作 | 语言 | 方案 | 状态 | 译文量 |",
         "|---|---|---|---|---|---|"]
        + [row(s) for s in slugs()]
        + ["| *（来加一个？）* | | | | | |"])


def splice(text, block):
    """-> text with everything between the markers replaced by block."""
    i = text.index(START)
    j = text.index(END, i)
    return text[:i + len(START)] + "\n" + block + "\n" + text[j:]


def write_readme():
    with io.open(README, encoding="utf-8") as f:
        text = f.read()
    new = splice(text, table())
    if new == text:
        print("README.md 的已收录表格已经是最新的")
    else:
        with io.open(README, "w", encoding="utf-8", newline="") as f:
            f.write(new)
        print("README.md 的已收录表格已重写")
    print("%d 个游戏" % len(slugs()))
    return 0


if __name__ == "__main__":
    if "--readme" in sys.argv[1:]:
        sys.exit(write_readme())
    for s in slugs():
        _, m = manifest(s)
        print("%-20s %s (%s)" % (s, m["title"], m["language_name"]))
