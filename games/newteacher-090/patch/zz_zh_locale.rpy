# That New Teacher 0.9.0 -- 简体中文补丁 / Simplified Chinese patch
#
# The game already ships a Chinese translation under game/tl/chinese/, so this
# patch does not add a language -- it replaces that tree and makes it the
# default so the player does not have to go through the language picker first.
#
# Deliberately NOT touched: fullLanguageList in
# game/LanguageSelection/languageSelection.rpy marks Chinese with
# True == "machine translated" and draws a robot icon next to it. That flag
# belongs to the publisher's UI and to the base text this patch revises, so it
# stays as it is. See docs/translation-log.md.

init python:

    config.language = "chinese"


# The game's own preferences screen only offers the languages it finds under
# game/tl/. Replacing that tree in place keeps the list intact, so nothing else
# has to be registered here.
