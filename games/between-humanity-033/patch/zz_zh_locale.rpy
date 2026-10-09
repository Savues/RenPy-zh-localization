# Between Humanity 0.3.3 -- 简体中文补丁 / Simplified Chinese patch
#
# The game already ships a Chinese translation under game/tl/chinese/, so this
# patch does not add a language -- it replaces that tree and makes it the
# default so the player does not have to go through the language picker first.
#
# Deliberately NOT touched: game/scripts/screens/languageSelection.rpy tells the
# player that some languages are partly or wholly AI-translated. That is still
# true of the base text this patch revises, so the notice stays.

init python:

    config.language = "chinese"


# The game's own preferences screen only offers the languages it finds under
# game/tl/. Replacing that tree in place keeps the list intact, so nothing else
# has to be registered here.
