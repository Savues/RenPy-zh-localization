# -*- coding: utf-8 -*-
"""Locate a game folder inside games/ and read its manifest.

Every tool takes the same optional --game <slug>; with a single game in the
repository the slug can be omitted. Adding a second game means dropping a new
folder under games/ with a game.json -- no tool changes required.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAMES = os.path.join(ROOT, "games")


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


if __name__ == "__main__":
    for s in slugs():
        _, m = manifest(s)
        print("%-20s %s (%s)" % (s, m["title"], m["language_name"]))
