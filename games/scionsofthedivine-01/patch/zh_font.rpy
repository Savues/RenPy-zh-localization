# -*- coding: utf-8 -*-
# Chinese localization font config.
#
# MiSans is now the PRIMARY font for the whole game (ASCII + CJK), replacing the
# original Latin display/handwriting fonts. Previously those were kept for ASCII
# and MiSans only filled in CJK; now everything renders in MiSans for a uniform
# look. Chinese already fell back to MiSans, so this mainly changes how Latin
# letters/numbers render.
#
# MiSans-Regular is a *static* font (correct weight). NotoSansSC-VF.ttf and
# friends default to wght=100 (Thin) in their fvar table and render almost
# invisible unless font_transforms are wired up, so MiSans is used on purpose.

init -999 python:
    zh_cjk = "fonts/MiSans-Regular.ttf"
    zh_cjk_bold = "fonts/MiSans-Bold.ttf"

    # Primary font everywhere.
    zh_text_font = zh_cjk
    zh_display_font = zh_cjk
    zh_rune_font = zh_cjk

    # Real bold face instead of Ren'Py synthetic emboldening, which smears
    # dense hanzi badly.
    config.font_replacement_map[(zh_cjk, True, False)] = (zh_cjk_bold, False, False)
