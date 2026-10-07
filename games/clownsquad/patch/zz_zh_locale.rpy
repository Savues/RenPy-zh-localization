# -*- coding: utf-8 -*-
## Clown Squad - Simplified Chinese: language, font and UI-string shim.
##
## Three jobs, all of them things the shipped game cannot do on its own.
##
## 1. Language.  The archive carries a Russian and a community Chinese
##    translation and leaves the choice to the player, so a fresh install opens
##    in the untranslated original.  This patch is the Chinese one; it asks for
##    schinese, and also switches an existing save over on the next start.
##
## 2. Fonts.  Ren'Py resolves a font name through renpy.config.font_name_map
##    at render time (renpy/text/text.py).  The game's own text fonts -
##    DejaVuSans.ttf and font/Bear Days.ttf - are Latin-only, so without the
##    mapping below every Chinese character falls through to a face with no CJK
##    glyphs and draws a tofu box.
##
##    The archive's own community translation ships a `translate schinese
##    python:` block (tl/schinese/base/style.rpy) that repoints gui.text_font
##    and friends at fonts inside tl/schinese/fonts/.  Whether that block runs
##    before or after init is not something to bet a font on, so every name it
##    can select is mapped too: whichever one wins, the Chinese comes from
##    MiSans and the Latin keeps the face the game chose.
##
##    The settings and credits screens ask for font/NotoSansSC-Black.ttf by
##    name.  That face already has full CJK coverage, so it is deliberately
##    left alone.
##
## 3. UI strings.  See _ZH_UI_OVERRIDES below.
##
## Set zh_language to None to play the original English instead.

## Set this to None to play the original English instead.
define zh_language = "schinese"

## Fallback for the characters the game's own fonts cannot draw.  Bare file
## name: Ren'Py resolves font names inside the fonts directory.
define zh_cjk_font = "MiSans-Regular.ttf"

## The same family's real bold weight, instead of Ren'Py's synthetic embolden.
## Applied only when the file is present, so a one-face install still works.
define zh_cjk_font_bold = "MiSans-Bold.ttf"

## Code point ranges that have to come from the CJK font.
##
## This is not a guess at "all of Unicode CJK": it is the measured set.  The
## 2042 distinct non-ASCII code points in data/tl_trans.json are 2023 CJK
## ideographs, U+3001/U+3002/U+300A-U+300D, seven fullwidth forms,
## U+2014/U+201C/U+201D/U+2026, and one MIDDLE DOT plus one GREEK SMALL
## LETTER PI.  Nothing in the patch needs a dingbat or an arrow, and a range
## the patch does not use is a range nobody checked.
define zh_cjk_ranges = [
    (0x00B7, 0x00B7),   # MIDDLE DOT, in a few names and ratings
    (0x03C0, 0x03C0),   # GREEK SMALL LETTER PI, once
    (0x2014, 0x2014),   # Em dash, the Chinese punctuation uses it throughout
    (0x201C, 0x201D),   # Curly double quotes
    (0x2026, 0x2026),   # Horizontal ellipsis, half of a Chinese ……
    (0x3000, 0x303F),   # CJK symbols and punctuation: 。、，「」《》
    (0x3400, 0x4DBF),   # CJK unified ideographs extension A
    (0x4E00, 0x9FFF),   # CJK unified ideographs
    (0xF900, 0xFAFF),   # CJK compatibility ideographs
    (0xFF00, 0xFFEF),   # Halfwidth and fullwidth forms: ，！？：（）
    ]

## Every font name this game can ask for text in -> the font that draws its
## Latin.  A FontGroup is built per entry: the game's own face first, MiSans
## for the ranges above.
##
## `tl/schinese/fonts/*` are what the archive's own translation selects; they
## are mapped rather than trusted so the Chinese face does not depend on which
## of them wins.  The two MiSans entries resolve to the faces this patch ships,
## so the community's MiSans and ours are one font as far as rendering goes.
define zh_font_bases = {
    "DejaVuSans.ttf": "DejaVuSans.ttf",
    "font/Bear Days.ttf": "font/Bear Days.ttf",

    "tl/schinese/fonts/SourceHanSansCN-Bold.ttf":
        "tl/schinese/fonts/SourceHanSansCN-Bold.ttf",
    "tl/schinese/fonts/KNMaiyuan-Regular.ttf":
        "tl/schinese/fonts/KNMaiyuan-Regular.ttf",
    "tl/schinese/fonts/ysbth.ttf": "tl/schinese/fonts/ysbth.ttf",
    "tl/schinese/fonts/MiSans-Regular.ttf": "MiSans-Regular.ttf",
    "tl/schinese/fonts/MiSans-Bold.ttf": "MiSans-Bold.ttf",
    }


init 999 python:

    def _zh_font_group(base_font):
        group = FontGroup()
        # add(base, None, None) claims everything the narrower adds below do
        # not, so the ranges have to be registered after it, not before.
        group.add(base_font, None, None)
        for _start, _end in zh_cjk_ranges:
            group.add(zh_cjk_font, _start, _end)
        return group

    # Every group is built before font_name_map is touched: FontGroup.add
    # refuses a font name that is already a key of that mapping, and most of the
    # base fonts are keys of it.
    _zh_groups = dict((_name, _zh_font_group(_base))
                      for _name, _base in zh_font_bases.items())
    renpy.config.font_name_map.update(_zh_groups)

    # get_font() consults this map before it loads a face, so a bold Chinese run
    # gets MiSans Bold rather than an emboldened MiSans Regular.
    if renpy.loader.loadable(zh_cjk_font_bold, directory="fonts"):
        for _name in ("MiSans-Regular.ttf", "MiSans-Bold.ttf"):
            renpy.config.font_replacement_map[(_name, True, False)] = (
                zh_cjk_font_bold, False, False)
            renpy.config.font_replacement_map[(_name, True, True)] = (
                zh_cjk_font_bold, False, True)

    def _zh_force_language():
        if (zh_language is not None
                and renpy.game.preferences.language != zh_language):
            renpy.translation.change_language(zh_language)

    if zh_language is not None:
        # Covers a fresh install; the start callback covers an existing save.
        renpy.config.default_language = zh_language
        if renpy.config.start_callbacks is not None:
            renpy.config.start_callbacks.append(_zh_force_language)


## ---------------------------------------------------------------------------
## UI strings.
##
## Ren'Py registers one translation per original string, and this game already
## registers `schinese` from inside archive.rpa.  A second `translate schinese
## strings:` block that claimed any of these originals would raise
## "A translation for ... already exists" at startup, which is why this patch
## ships its dialogue as same-named files that shadow the archive's instead
## (see the game README) and the leftovers below are applied to the finished
## table at init 999 instead of being registered again.
##
## The dict MUST be applied with .update().  translations is a dict-like whose
## add() refuses an existing key and raises the same "already exists" error.
## ---------------------------------------------------------------------------
define _ZH_UI_OVERRIDES = {
    # Character name: the shipped translation says 爱丽丝, which is Alice.
    "Alicia": "艾丽西亚",

    # Mistranslation: the original is about only fast-forwarding read text.
    "Skips only the text that has been read.": "仅快进已读过的文本。",

    # Credits entries the shipped translation left untranslated.
    "0.1 Part 1": "0.1 第一部分",
    "Translations": "翻译",
    "CH Translation - 初夏子涛": "中文翻译 - 初夏子涛",
    "RU Translation - Debios": "俄语翻译 - Debios",
    "Благодарность переводчику, за его труд!": "感谢译者的辛勤付出！",
    "Special thanks to": "特别鸣谢：",
    "W.M, Duve, JazzPourer, Unknown, and all other who help me.": "W.M、Duve、JazzPourer、Unknown，以及所有帮助过我的其他人。",
    "Supporters": "支持者们",
    "A huge thank you to my discord moderators.": "特别感谢我的 Discord 管理员。",
    "To my testers who helped to improve and fix bugs in this game, thank you.": "感谢所有帮助改进本游戏并修复问题的测试人员，谢谢你们！",
    "Licensed under Creative Commons: By Attribution 3.0": "依据知识共享 署名 3.0 许可协议授权",

    # Strings the shipped translation never covered, so these still render in
    # English in-game.
    "Note: You can move between": "提示：你可以用",
    "saves using the A - D keys.": "A - D 键在存档之间切换。",
    "Text speed: ([preferences.text_cps] /300": "文字速度：([preferences.text_cps] /300",
    "Enable NSFW content?": "是否启用成人内容？",
    "You can always change this in the settings.": "之后随时都可以在设置中更改。",
    "Change language": "更改语言",

    # Wording aligned with the glossary while we are here.
    "Skip (A)": "快进 (A)",
    }


init 999 python:

    try:
        _zh_strings = renpy.game.script.translator.strings["schinese"]
    except Exception:
        _zh_strings = None

    if _zh_strings is None:
        renpy.log("zh-UI: the schinese translator is missing; %d UI strings "
                  "were not applied." % len(_ZH_UI_OVERRIDES))
    else:
        _zh_strings.translations.update(_ZH_UI_OVERRIDES)
        renpy.log("zh-UI: applied %d string overrides." % len(_ZH_UI_OVERRIDES))
