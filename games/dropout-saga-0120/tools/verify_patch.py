#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DropOut Saga patch self-check -- the "syntactically valid, semantically wrong"
class of bug that no shared linter can see.

check.py already guards the whole patch against mojibake, doubled spaces, banned
glossary variants, doubled terms and unbalanced [i]/[b]/[u]/[s] tags.  What it
cannot do is judge a script whose text was rewritten in place.  Four things went
wrong that way while this patch was being built, and each one is now a check:

  1. A literal written one column off.  Cosy Cafe's WeekDays index 3 was written
     with index 2's value, which no rule can see because the file still parses.
     Here the equivalent signal is two adjacent Chinese literals on one line being
     identical, plus per-file literal counts that must not move.
  2. A near-miss character.  The corruption label was written with U+581D instead
     of the game's own U+5815 -- left radical 土 instead of 阝.  It renders as a
     near-copy of the right character, so it survives review and passes every other
     check.  The toolbox title is now built from config.name, and the code points
     are asserted here so the class cannot come back through a hardcoded string.
  3. A name written with another character's name in it.  love_ava and
     corruption_ava were both 艾 + the 娅 from 索菲娅, while the guide data had
     索菲娅 correct, so reading either table alone showed nothing wrong.  Every
     character name the patch displays is compared against script.rpy's own
     Character() definitions.
  4. Coverage asserted and never recomputed.  data/coverage.json records the
     measured numbers; the arithmetic and the per-file counts are re-derived here.

Run:  python tools/verify_patch.py     (check.py runs it from the game directory)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.dirname(HERE)                      # games/dropout-saga-0120
PATCH = os.path.join(GAME, "patch", "game")
SHIM = os.path.join(GAME, "patch", "000_zh_fonts.rpy")

errors = []


def bad(msg):
    errors.append(msg)


# The extraction pass's tokeniser and asset rule, copied rather than reimplemented.
# A second tokenizer would count differently and the recorded baselines would be
# meaningless; if that upstream rule ever changes, change it here in the same commit.
TRIPLE_RE = re.compile(r'"""(.*?)"""', re.S)
STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
ASSET_EXT = ('.ogg', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.avi', '.webm',
             '.mp4', '.wav', '.mp3', '.opus', '.ttf', '.rpy', '.rpyc')


def is_asset(t):
    """True for resource paths, hex colours, image tags and bare identifiers."""
    if not t:
        return True
    low = t.lower()
    if re.fullmatch(r'#[0-9a-fA-F]{3,8}', t):
        return True
    if any(low.endswith(e) for e in ASSET_EXT):
        return True
    if ('/' in t or '\\\\' in t) and ' ' not in t:
        return True
    if re.fullmatch(r'(\{image=[^}]*\}\s*)+', t):
        return True
    if ' ' not in t and re.fullmatch(r'[a-z0-9_.]+', t):
        return True
    return False


def has_cjk(t):
    return any('\u4e00' <= c <= '\u9fff' for c in t)


def line_offsets(text):
    offs, pos = [], 0
    for line in text.split('\n'):
        offs.append(pos)
        pos += len(line) + 1
    return offs


def line_of(offs, off):
    lo, hi = 0, len(offs) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if offs[mid] <= off:
            lo = mid
        else:
            hi = mid - 1
    return lo


def regions(lines):
    """Which lines sit inside a screen body or a menu block."""
    screen_lines, menu_lines = set(), set()
    for i, l in enumerate(lines):
        s = l.strip()
        if re.match(r'^screen\s+\w+', s):
            for j in range(i, min(i + 500, len(lines))):
                screen_lines.add(j)
                if j > i and re.match(r'^(screen|label|init|define|default|image|transform|translate|menu)\b', lines[j].strip()):
                    screen_lines.discard(j)
                    break
        if s.startswith('menu:'):
            for j in range(i, min(i + 300, len(lines))):
                menu_lines.add(j)
                if j > i and re.match(r'^\S', lines[j]):
                    menu_lines.discard(j)
                    break
    return screen_lines, menu_lines


def literals(path):
    """[(line, kind, text)] using the extraction pass's own rules."""
    src = open(path, encoding='utf-8', errors='replace').read()
    lines = src.split('\n')
    offs = line_offsets(src)
    screen_lines, menu_lines = regions(lines)
    out = []
    for m in TRIPLE_RE.finditer(src):
        out.append((line_of(offs, m.start()) + 1, 'triple', m.group(1)))
    for m in STR_RE.finditer(src):
        ln = line_of(offs, m.start())
        st = lines[ln].strip() if ln < len(lines) else ''
        kind = 'say'
        pre = src[max(0, m.start() - 3):m.start()]
        if pre.endswith('_(') or pre.endswith('_p('):
            kind = 'ui'
        if ln in menu_lines:
            kind = 'menu'
        elif ln in screen_lines:
            kind = 'screen'
        elif st.startswith(('define', 'default')):
            kind = 'define'
        elif st.startswith('#'):
            kind = 'comment'
        out.append((ln + 1, kind, m.group(1)))
    return out


def prose_of(items):
    return [(ln, k, t) for ln, k, t in items
            if k != 'comment' and not is_asset(t)]

# ---- 1. the file set -----------------------------------------------------
# The patch replaces 14 of the game's own scripts and adds five more. A file that
# goes missing loads nothing and Ren'Py reports no error, so its absence is
# checked. The other five release scripts are absent on purpose: Bust_Char.rpy,
# images.rpy, myscreens.rpy, PhoneTexting.rpy and replay_scenes.rpy carry no
# translatable text -- asset names, style prefixes, colour values -- and were
# shipping here byte-identical to the release, so they only added surface area.
GAME_FILES = ['day1_update.rpy', 'day2_update.rpy', 'day3_update.rpy',
              'day4_update.rpy', 'day5_update.rpy', 'day6_update.rpy',
              'day7_update.rpy', 'day8_update.rpy', 'gui.rpy',
              'options.rpy', 'patreonmenu.rpy', 'replay_gallery.rpy',
              'screens.rpy', 'script.rpy']
TOOL_FILES = ['000_zh_modcompat.rpy', '001_zh_guide_data.rpy',
              '002_zh_guide_ui.rpy', '003_zh_tools_data.rpy', 'zz_zh_tools_ui.rpy']

if not os.path.isfile(SHIM):
    bad('patch/000_zh_fonts.rpy is missing')
for f in GAME_FILES + TOOL_FILES:
    if not os.path.isfile(os.path.join(PATCH, f)):
        bad('patch/game/%s is missing' % f)


# ---- 2. per-file baselines ----------------------------------------------
# Line and literal counts must not move. Chinese is shorter than English, so a
# write-back that re-finds a literal by column instead of by index lands on the
# wrong one and can leave both counts intact -- which is why the adjacency check
# below exists too. Neither check sees everything; between them they cover the
# two shapes this patch's history actually produced.
cov = json.load(open(os.path.join(GAME, 'data', 'coverage.json'), encoding='utf-8'))
base = cov['patch']['files']
prose_total = zh_total = 0

for f in GAME_FILES:
    p = os.path.join(PATCH, f)
    if not os.path.isfile(p):
        continue
    items = literals(p)
    prose = prose_of(items)
    zh = [t for _, _, t in prose if has_cjk(t)]
    nlines = len(open(p, encoding='utf-8', errors='replace').read().split('\n'))
    prose_total += len(prose)
    zh_total += len(zh)
    want = base.get(f)
    if not want:
        bad('%s has no recorded baseline' % f)
        continue
    for key, got in (('lines', nlines), ('literals', len(items)),
                     ('prose', len(prose)), ('chinese', len(zh))):
        if got != want[key]:
            bad('%s: %s is %d, baseline says %d' % (f, key, got, want[key]))

for key, got in (('prose', prose_total), ('chinese', zh_total),
                 ('non_cjk_prose', prose_total - zh_total)):
    if got != cov['patch'][key]:
        bad('patch total %s is %d, baseline says %d' % (key, got, cov['patch'][key]))


# ---- 3. the coverage arithmetic ------------------------------------------
# These three numbers come from the English release, which this repository does
# not redistribute, so they cannot be recomputed here -- only their sum can be
# checked, and only the patch side can be re-derived. That asymmetry is written
# into data/coverage.json rather than left for a reader to discover.
c = cov['coverage']
if c['translated'] + c['verbatim'] != c['english_total']:
    bad('coverage arithmetic: %d + %d != %d'
        % (c['translated'], c['verbatim'], c['english_total']))


# ---- 4. adjacent duplicate Chinese literals ------------------------------
# Two identical Chinese literals next to each other on one line is what a
# column-shifted write-back looks like where the target happened to repeat.
dupes = 0
for f in GAME_FILES + TOOL_FILES + ['000_zh_fonts.rpy']:
    p = SHIM if f == '000_zh_fonts.rpy' else os.path.join(PATCH, f)
    if not os.path.isfile(p):
        continue
    per = {}
    for ln, _, t in literals(p):
        per.setdefault(ln, []).append(t)
    for ln, arr in per.items():
        for k in range(1, len(arr)):
            if arr[k] and arr[k] == arr[k - 1] and has_cjk(arr[k]):
                dupes += 1
                bad('%s:%d adjacent Chinese literals repeat: %r' % (f, ln, arr[k]))


# ---- 5. character names against the game's own definitions ---------------
# script.rpy is the authority: every Character() carries the spelling the game
# itself displays. Anything the patch shows has to match it exactly. Reading a
# single table is not enough -- love_ava and corruption_ava were both written
# with the ya from Sophia's name while the guide data had Sophia correct.
script_src = open(os.path.join(PATCH, 'script.rpy'), encoding='utf-8').read()
canon = {c for c in re.findall(r'Character\(\s*"([^"]*)"', script_src) if has_cjk(c)}
if len(canon) < 15:
    bad('only %d character names recovered from script.rpy; the parse is wrong' % len(canon))

ui_src = open(os.path.join(PATCH, 'zz_zh_tools_ui.rpy'), encoding='utf-8').read()
for label, var in re.findall(r'\("([^"]*)",\s*"((?:love|corruption)_\w+)"\)', ui_src):
    name = label.split('·')[-1].strip()
    if name and name not in canon:
        bad('%s is labelled %r, which script.rpy does not define' % (var, name))


# ---- 6. the toolbox title's code points ----------------------------------
# The title must come from config.name, not from a literal someone typed. If it
# ever goes back to a hardcoded string the trap is a character that renders as a
# near-copy of the right one: U+581D, whose left radical is 土 where the game's
# U+5815 has 阝. Nothing else in this repository can see that difference.
m = re.search(r'define zh_toolbox_title\s*=\s*(.+)', ui_src)
if not m:
    bad('zh_toolbox_title is not defined in zz_zh_tools_ui.rpy')
else:
    if 'config.name' not in m.group(1):
        bad('zh_toolbox_title no longer derives from config.name: %r' % m.group(1).strip())
if '堝' in ui_src:
    bad('U+581D is in zz_zh_tools_ui.rpy; the game uses U+5815')


# ---- 7. the mod translation table ----------------------------------------
mod = json.load(open(os.path.join(GAME, 'data', 'mod_zh.json'), encoding='utf-8'))
if not mod:
    bad('data/mod_zh.json is empty')
# "Has a CJK ideograph" is the wrong test.  A finished translation can be pure
# punctuation or a reordered format string -- "..." -> "……", "Day: [daytext]"
# -> "[daytext]", "{i}[name!u]!!{/i}" -> "{i}[name!u]！！{/i}".  Eight of the 1273
# pairs are like that and are all correct.  The defect that actually happened was
# an empty value, so that is what is asserted.
empty = [k for k, v in mod.items() if not str(v).strip()]
if empty:
    bad('%d empty mod translations, e.g. %r' % (len(empty), empty[:3]))
mod_zh = sum(1 for v in mod.values() if has_cjk(str(v)))


if errors:
    sys.stderr.write('✗ %d problem(s)\n\n' % len(errors))
    for e in errors:
        sys.stderr.write('  ' + e + '\n')
    sys.exit(1)

print('✓ %d scripts + 1 font shim, %d lines, %d prose literals (%d Chinese, %d verbatim)'
      % (len(GAME_FILES) + len(TOOL_FILES) + 1,
         sum(base[f]['lines'] for f in GAME_FILES),
         prose_total, zh_total, prose_total - zh_total))
print('✓ %d character names match script.rpy; toolbox title derives from config.name'
      % len(canon))
print('✓ mod_zh.json: %d pairs, none empty (%d carry Han characters)'
      % (len(mod), mod_zh))
