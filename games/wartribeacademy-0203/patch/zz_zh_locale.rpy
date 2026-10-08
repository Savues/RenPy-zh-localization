# -*- coding: utf-8 -*-
## Wartribe Academy 2.0.3 - Simplified Chinese.
##
## This patch does NOT use Ren'Py translations.  The game ships no
## game/tl/<lang>/ templates -- only game/tl/None/common.rpym -- so there is
## nothing for tools/build_tl.py to compile.  patch/game/ instead replaces 15 of
## the game's own .rpy files with Chinese ones, and those scripts are the patch.
## No config.language needs forcing and no translate block needs registering.
##
## Fonts live in the patched patch/game/gui.rpy.  The game ships exactly one
## typeface of its own, gui/fonts/Nunito-Bold.ttf, and its cmap has zero
## codepoints in U+3400-U+9FFF -- Latin only.  gui.rpy now builds a FontGroup
## per slot: MiSans is the default, and the two code points MiSans lacks
## (U+25B8, the animated skip triangle, and U+266A, MUSIC NOTE) fall back to
## DejaVuSans.
##
## What is left for this file is the failure mode an outright overwrite cannot
## cover on its own.  gui.rpy covers gui.text_font, gui.name_text_font and
## gui.interface_text_font, and gui.button_text_font / gui.choice_button_text_font
## alias those two.  Anything still asking for the game's bundled Latin-only
## face -- a screen hardcoding it, or a third-party mod -- would fall through to
## DejaVuSans, whose cmap holds just 64 codepoints in U+3400-U+9FFF, which for a
## Chinese UI is the same as none.  Mapping those names onto the same FontGroup
## closes the hole.

## Set to None to stop the safety net and use whatever the scripts ask for.
define zh_fallback_font = "fonts/MiSans-Regular.ttf"

define zh_fallback_bold = "fonts/MiSans-Bold.ttf"

## Faces this game ships that have no CJK coverage.  Listed explicitly so a
## renamed file cannot silently fall back to tofu.
define zh_latin_only_fonts = [
    "gui/fonts/Nunito-Bold.ttf",
    "Nunito-Bold.ttf",
    ]

init 999 python:

    if zh_fallback_font is None:
        pass
    elif not renpy.loader.loadable(zh_fallback_font, directory="fonts"):
        # Fonts are missing; the patched gui.rpy will fail on its own and say so.
        pass
    else:

        def _zh_group(base_font):
            group = FontGroup()
            # First .add() wins, so the two fallback code points have to be
            # registered before the default face.
            if renpy.loader.loadable("fonts/DejaVuSans.ttf", directory="fonts"):
                group.add("fonts/DejaVuSans.ttf", 0x25b8, 0x25b8)
                group.add("fonts/DejaVuSans.ttf", 0x266a, 0x266a)
            group.add(base_font, None, None)
            return group

        _zh_group_cache = { }
        for _name in zh_latin_only_fonts:
            # FontGroup.add refuses a name already in font_name_map, so build
            # every group before installing any of them.
            if _name in renpy.config.font_name_map:
                continue
            if not renpy.loader.loadable(_name, directory="fonts"):
                continue
            _zh_group_cache[_name] = _zh_group(_name)

        if _zh_group_cache:
            renpy.config.font_name_map.update(_zh_group_cache)

        # get_font() applies the replacement map before loading a face, so a bold
        # CJK run gets MiSans Bold rather than a synthetic embolden.
        if renpy.loader.loadable(zh_fallback_bold, directory="fonts"):
            renpy.config.font_replacement_map[(zh_fallback_font, True, False)] = (
                zh_fallback_bold, False, False)