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


def row(slug):
    """-> one markdown row describing games/<slug> for the root README."""
    game, m = manifest(slug)
    tr = translations(game)
    # Imported here rather than at module level: check.py imports games, so a
    # top-level import would be circular. Only this one test needs it, and it
    # has to be check.py's own test -- a second copy of KEEP/KEEP_EXACT here
    # would drift and quietly start calling finished translations untranslated.
    import check
    left = sum(1 for k, v in tr.items() if not check.keep(k, v) and v == k)
    # A game added before any translating has no database yet. Reporting that
    # as ✅ 100% would be a lie that also passes check_links.py.
    if not tr:
        state = "🚧 待翻译"
    elif left:
        state = "⚠️ %d 条未译" % left
    else:
        state = "✅ 100%"
    return "| [%s](games/%s/) | %s | %s | %s | %s 条 |" % (
        m["title"], slug, m["author"], m["language_name"],
        state, "{:,}".format(len(tr)))


def table():
    """-> the markdown block that belongs between the README's markers."""
    return "\n".join(
        ["| 游戏 | 原作 | 语言 | 状态 | 译文量 |",
         "|---|---|---|---|---|"]
        + [row(s) for s in slugs()]
        + ["| *（来加一个？）* | | | | |"])


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
