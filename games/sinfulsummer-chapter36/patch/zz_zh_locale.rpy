# -*- coding: utf-8 -*-
## Sinful Summer (Chapter 3.6) - Simplified Chinese: language + font shim.
##
## Ren'Py resolves a font name through `renpy.config.font_name_map` at render
## time (renpy/text/text.py).  Every font this game ships with is Latin-only,
## so without the mapping below every Chinese character falls through to
## DejaVuSans.ttf -- which has no CJK glyphs -- and draws a tofu box.
##
## Each entry in `zh_font_bases` becomes a FontGroup: the game's own font draws
## everything it has a glyph for, and MiSans draws the ranges listed in
## `zh_cjk_ranges`.  Latin text therefore keeps its original look, which
## font-file shadowing could not do.
##
## Note: no `import` statements in here on purpose.  Ren'Py 8.3 mis-tracks its
## own lazily-created `renpy.*` module attributes when a late `init python:`
## block contains an import, which breaks the audio subsystem.

## Set this to None to play the original English instead.
define zh_language = "schinese"

## Fallback font for characters the game's own fonts cannot draw.  Bare file
## name: Ren'Py resolves font names inside the fonts directory.
define zh_cjk_font = "MiSans-Regular.ttf"

## Real bold weight for the same family, instead of Ren'Py's synthetic embolden.
## Applied only when the file is actually present, so a single-font install
## still works.
define zh_cjk_font_bold = "MiSans-Bold.ttf"

## Code point ranges that have to come from the CJK font.
define zh_cjk_ranges = [
    (0x2014, 0x2014),   # Em dash, used by the Chinese punctuation
    (0x2026, 0x2026),   # Horizontal ellipsis, half of a Chinese ……
    (0x2E80, 0x2FDF),   # CJK radicals supplement, Kangxi radicals
    (0x3000, 0x303F),   # CJK symbols and punctuation
    (0x3040, 0x30FF),   # Hiragana, Katakana
    (0x31F0, 0x31FF),   # Katakana phonetic extensions
    (0x3200, 0x33FF),   # Enclosed CJK letters, CJK compatibility
    (0x3400, 0x4DBF),   # CJK unified ideographs extension A
    (0x4E00, 0x9FFF),   # CJK unified ideographs
    (0xF900, 0xFAFF),   # CJK compatibility ideographs
    (0xFE10, 0xFE4F),   # Vertical forms
    (0xFF00, 0xFFEF),   # Halfwidth and fullwidth forms
    ]

## Every font name the game can ask for -> the font that draws its Latin text.
## Both halves matter.  The script tags some dialogue with
## `{font=font_narration}`, but every other style -- menus, buttons, settings,
## and all dialogue that carries no font tag -- falls back to the plain
## `DejaVuSans.ttf` default.  Mapping only the aliases would leave the bulk of
## the script rendering as tofu.
define zh_font_bases = {
    "font_narration": "DejaVuSans-Oblique.ttf",
    "font_talking": "DejaVuSans.ttf",
    "font_thinking": "DejaVuSans-Oblique.ttf",
    "font_title": "BebasNeue-Regular.ttf",
    "font_phone": "Roboto-Black.ttf",

    "BebasNeue-Regular.ttf": "BebasNeue-Regular.ttf",
    "DejaVuSans.ttf": "DejaVuSans.ttf",
    "DejaVuSans-Oblique.ttf": "DejaVuSans-Oblique.ttf",
    "Poppins-Light.ttf": "Poppins-Light.ttf",
    "Poppins-LightItalic.ttf": "Poppins-LightItalic.ttf",
    "Roboto-Black.ttf": "Roboto-Black.ttf",
    }

init 999 python:

    def _zh_font_group(base_font):
        group = FontGroup()
        group.add(base_font, None, None)
        for _start, _end in zh_cjk_ranges:
            group.add(zh_cjk_font, _start, _end)
        return group

    # Build every group before touching font_name_map: FontGroup.add refuses a
    # font name that is already registered there, and most of the base fonts
    # are keys of that very mapping.
    _zh_groups = { }
    for _name, _base in zh_font_bases.items():
        _zh_groups[_name] = _zh_font_group(_base)
    renpy.config.font_name_map.update(_zh_groups)

    # get_font() applies this map before it loads a face, so a bold CJK run gets
    # MiSans Bold rather than a synthetically emboldened MiSans Regular.
    if renpy.loader.loadable(zh_cjk_font_bold, directory="fonts"):
        renpy.config.font_replacement_map[(zh_cjk_font, True, False)] = (
            zh_cjk_font_bold, False, False)

    def _zh_force_language():
        if zh_language is not None and renpy.game.preferences.language != zh_language:
            renpy.translation.change_language(zh_language)

    if zh_language is not None:
        # Covers fresh installs; the start callback covers existing saves.
        renpy.config.default_language = zh_language
        if renpy.config.start_callbacks is not None:
            renpy.config.start_callbacks.append(_zh_force_language)


init 999 python:

    ## Speaker names.  `{i}` marks the italic "inner voice" variants.
    l.name = "莱娜"
    lm.name = "{i}（莱娜）"
    e.name = "埃里克"
    em.name = "{i}（埃里克）"
    h.name = "赫尔加"
    hm.name = "{i}（赫尔加）"
    j.name = "约翰"
    lf.name = "朱丽叶特"
    sk.name = "店主"
    a.name = "安娜"
    au.name = "???"
    l_nvl.name = "莱娜"
    lmc_nvl.name = "莱娜"
    e_nvl.name = "埃里克"
    emc_nvl.name = "埃里克"
    h_nvl.name = "赫尔加"
    hmc_nvl.name = "赫尔加"
    j_nvl.name = "朱丽叶特"
    u_nvl.name = "未知"