# -*- coding: utf-8 -*-
## Cosy Cafe 0.14.2 - Simplified Chinese font safety net.
##
## This patch does NOT rely on Ren'Py translations: patch/game/ replaces 27 of
## the game's own .rpy files with Chinese ones outright, so there is no
## config.language to force and no translate block to register.  Everything
## player-visible already lives in those replaced scripts.
##
## What is left for this file is the one failure mode an outright overwrite
## cannot cover on its own.  patch/game/gui.rpy already points every font slot
## at fonts/MiSans-Regular.ttf, but any screen that still asks for one of the
## game's bundled Latin-only faces -- centurygothic.ttf, gensans.otf,
## gensanslight.otf, Tungsten.ttf -- would fall through to DejaVuSans.ttf,
## which has no CJK glyphs, and draw tofu boxes.  Mapping those names onto a
## FontGroup closes the hole: the game's own face draws everything it has a
## glyph for, MiSans draws the CJK ranges.

## Set to None to fall back to whatever the scripts currently say.
define zh_fallback_font = "MiSans-Regular.ttf"

define zh_fallback_bold = "MiSans-Bold.ttf"

define zh_cjk_ranges = [
    (0x2014, 0x2014),   # em dash, used by the Chinese punctuation
    (0x2026, 0x2026),   # horizontal ellipsis, half of a Chinese ……
    (0x2E80, 0x2FDF),   # CJK radicals supplement, Kangxi radicals
    (0x3000, 0x303F),   # CJK symbols and punctuation
    (0x3040, 0x30FF),   # Hiragana, Katakana
    (0x31F0, 0x31FF),   # Katana phonetic extensions
    (0x3200, 0x33FF),   # Enclosed CJK letters, CJK compatibility
    (0x3400, 0x4DBF),   # CJK unified ideographs extension A
    (0x4E00, 0x9FFF),   # CJK unified ideographs
    (0xF900, 0xFAFF),   # CJK compatibility ideographs
    (0xFE10, 0xFE4F),   # vertical forms
    (0xFF00, 0xFFEF),   # halfwidth and fullwidth forms
    ]

## Latin-only faces this game ships.  Listed explicitly so a renamed file
## cannot silently fall back to tofu.
define zh_latin_only_fonts = [
    "gui/msp1/centurygothic.ttf",
    "gui/msp1/gensans.otf",
    "gui/msp1/gensanslight.otf",
    "gui/msp1/Tungsten.ttf",
    "DejaVuSans.ttf",
    ]

init 999 python:

    if zh_fallback_font is None:
        pass
    else:
        def _zh_group(base_font):
            group = FontGroup()
            group.add(base_font, None, None)
            for _start, _end in zh_cjk_ranges:
                group.add(zh_fallback_font, _start, _end)
            return group

        # Build the groups first: FontGroup.add refuses a name already present
        # in font_name_map, and most bases are keys of that very mapping.
        _zh_groups = {}
        for _name in zh_latin_only_fonts:
            _groups = _zh_group(_name)
            if _groups is not None:
                _zh_groups[_name] = _groups
        renpy.config.font_name_map.update(_zh_groups)

        # get_font() applies the replacement map before loading a face, so a
        # bold CJK run gets MiSans Bold rather than a synthetic embolden.
        if renpy.loader.loadable(zh_fallback_bold, directory="fonts"):
            renpy.config.font_replacement_map[(zh_fallback_font, True, False)] = (
                zh_fallback_bold, False, False)
