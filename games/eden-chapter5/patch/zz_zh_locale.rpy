# Chinese localization shim.
# 1) Force the Chinese translation to be the active language.
# 2) Point the game's fonts at a CJK-capable face.
# 3) Localize the dynamic speaker-name variables (variables.rpy + runtime assigns).
#
# NOTE: renpy/common/00start.rpy sets config.language = None inside an
# `init -1600 python hide:` block, so this has to run at a *later* priority.

init python:

    config.language = "schinese"
    config.default_language = "schinese"

init -1 python:

    gui.text_font = "fonts/zh.ttf"
    gui.name_text_font = "fonts/zh.ttf"
    gui.interface_text_font = "fonts/zh.ttf"
    gui.button_text_font = "fonts/zh.ttf"
    gui.choice_button_text_font = "fonts/zh.ttf"


## Dynamic speaker names ####################################################
# The scripts do `$ ravena_name = "Ravena"` style assignments at runtime, so
# overriding the `default` values alone is not enough; remap before every say.

init python:

    _zh_name_map = {
        "Ravena": "拉维娜",
        "Gianna": "吉安娜",
        "Yuki": "由纪",
        "Mai": "梅",
        "Tobias the traveler": "旅行家托拜厄斯",
        "Tobias the Traveller": "旅行家托拜厄斯",
        "Tobias the Prisoner": "囚犯托拜厄斯",
        "Sophia": "索菲娅",
        "Vela": "薇拉",
        "Lily": "莉莉",
        "Aqua": "阿库娅",
        "Luminox": "露米诺克斯",
        "Mysterious Man": "神秘男子",
        "Mysterious Witch": "神秘魔女",
        "Witch of Darkness": "暗之魔女",
    }

    _zh_name_vars = (
        "ravena_name", "gianna_name", "yuki_name", "mai_name",
        "tobias_name", "sophia_name", "vela_name", "lily_name",
        "aqua_name", "luminox_name", "wayfarer_name",
    )

    def _zh_localize_names():
        for var in _zh_name_vars:
            value = getattr(renpy.store, var, None)
            if isinstance(value, str) and value in _zh_name_map:
                setattr(renpy.store, var, _zh_name_map[value])

    # renpy.exports.say calls config.say_arguments_callback(who, *args, **kwargs)
    # and expects (args, kwargs) back.
    _zh_prev_say_callback = config.say_arguments_callback

    if _zh_prev_say_callback is None:
        def _zh_say_callback(who, *args, **kwargs):
            _zh_localize_names()
            return args, kwargs
    else:
        def _zh_say_callback(who, *args, **kwargs):
            _zh_localize_names()
            args, kwargs = _zh_prev_say_callback(who, *args, **kwargs)
            return args, kwargs

    config.say_arguments_callback = _zh_say_callback


## Fallback defaults, so the very first say already renders a Chinese name. #####

default ravena_name = "拉维娜"
default gianna_name = "吉安娜"
default yuki_name = "由纪"
default mai_name = "梅"
default tobias_name = "旅行家托拜厄斯"
default sophia_name = "索菲娅"
default vela_name = "薇拉"
default lily_name = "莉莉"
default aqua_name = "阿库娅"
default luminox_name = "露米诺克斯"
default wayfarer_name = "神秘男子"
