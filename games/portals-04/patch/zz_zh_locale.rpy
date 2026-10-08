# ===========================================================================
#  Por(n)tals 0.4 -- Simplified Chinese, single shim.
#
#  This file is the concatenation of the two shims the patch shipped as:
#
#      zz_zh_setup.rpy   engine/compat fix, language, font registration
#      zz_zh_names.rpy   character-name remapping
#
#  The repository's tools carry exactly one shim per game -- games.patch_entries()
#  reads game.json's `shim` and package_release.py writes that one file -- so the
#  two were merged rather than left as a pair a player would have to copy by hand
#  and a packager would silently drop one of.
#
#  The merge is a straight concatenation and is order-safe. Both files used
#  `init 999 python:`; Ren'Py allows several blocks at one priority and runs them
#  in file order, and the other priorities are distinct anyway:
#
#      -4000  zz_zh_setup.rpy   patch renpy.* so the distribution boots
#       -300  zz_zh_names.rpy   wrap Character() and remap names
#       -100  zz_zh_setup.rpy   font registration and language selection
#        999  both files        late screen/override work
#
#  One change beyond concatenation: the bundled face is referenced as
#  `fonts/NotoSansSC-VF.ttf` rather than `Fonts/NotoSansSC-VF.ttf`, because
#  tools/install.py and tools/package_release.py can only write game/fonts/.
#  Same file, one directory; Ren'Py resolves both against game/.
# ===========================================================================

# ===========================================================================
#  Por(n)tals 0.4 -- Simplified Chinese support.
#
#  Written against the Ren'Py 8.2 engine shipped in this game. Verified by
#  reading: renpy/config.py, renpy/ast.py, renpy/loader.py, renpy/python.py,
#  renpy/text/font.py, renpy/text/text.py, renpy/sl2/slproperties.py,
#  renpy/translation/*.
# ===========================================================================


# ---------------------------------------------------------------------------
#  0. SHIM FOR A PRE-EXISTING BOOT FAILURE IN THIS DISTRIBUTION.
#
#     Not localisation related -- the stock game fails to start, with or
#     without any of our files:
#
#         renpy/common/00layout.rpy:124
#             if renpy.has_screen("main_menu"):
#         AttributeError: module 'renpy' has no attribute 'has_screen'
#
#     In stock Ren'Py, script code sees the name `renpy` bound to the
#     renpy.exports MODULE (renpy/defaultstore.py:465 and renpy/minstore.py:66
#     both do `globals()["renpy"] = renpy.exports`), and exports.py imports
#     has_screen from renpy.display.screen. Here `renpy` resolves to the
#     renpy PACKAGE, so `renpy.<exported function>` does not resolve.
#
#     We could not simply re-point the store: script globals are
#     renpy.python.store_dicts["store"], a StoreDict that is rebuilt from
#     renpy.minstore during bootstrap, and renpy.store is only a module proxy
#     around it. So patch the package, in two careful steps.
#
#     Delete this block if you swap in a stock Ren'Py 8.2 engine.
# ---------------------------------------------------------------------------
init -4000 python:

    import renpy
    import renpy.exports

    # 1. Names the package does not have at all: take the export.
    #    (This is what fixes has_screen.)
    for _zh_name, _zh_value in list(renpy.exports.__dict__.items()):
        if _zh_name.startswith("__"):
            continue
        if not hasattr(renpy, _zh_name):
            setattr(renpy, _zh_name, _zh_value)

    # 2. Names where the package owns a SUBMODULE that shadows an exported
    #    function. Only override the ones scripts call as functions -- an
    #    earlier blanket "module -> function" pass broke the engine itself,
    #    because renpy/main.py calls renpy.log.post_init() and
    #    renpy/bootstrap.py calls renpy.error.report_exception().
    #
    #    The whole collision set is only three names (67 submodules vs 199
    #    exported functions), and each one was checked individually:
    #
    #      rollback  SAFE to replace. renpy/common/00keymap.rpy:423 builds the
    #                default keymap at init -1100 (this shim runs at -4000, so
    #                it wins the race) and reads `rollback = renpy.rollback`.
    #                In stock Ren'Py that is renpy.exports.rollback, the
    #                function; here it resolved to the rollback SUBMODULE, so
    #                Keymap.event -> behavior.run() called a module and raised
    #                TypeError: 'module' object is not callable the moment the
    #                player pressed 回退. Every module-style use of
    #                renpy.rollback.* in the engine (defaultstore.py:238,
    #                display/particle.py:352) happens at import time, i.e.
    #                before this shim runs.
    #
    #      error     MUST stay a module. execution.py:614 calls
    #                renpy.error.report_exception() at RUNTIME from the
    #                interpreter's exception handler.
    #      log       MUST stay a module. main.py:543 calls
    #                renpy.log.post_init(), and display/__init__.py binds
    #                renpy.log.open(...) into several modules.
    for _zh_name in ("curry", "rollback"):
        setattr(renpy, _zh_name, getattr(renpy.exports, _zh_name))

    # 3. Names where the package is shadowed by a __future__ import.
    #    renpy/__init__.py:25 does
    #        from __future__ import division, absolute_import, with_statement, ...
    #    so the package binds with_statement to a __future__._Feature INSTANCE.
    #    hasattr() is therefore True, step 1 skips it, and script code that
    #    calls renpy.with_statement(...) dies with
    #        TypeError: '_Feature' object is not callable
    #    (first hit: game/tl/schinese/script.rpy "startGuy ... with dis",
    #     via renpy/common/000window.rpy _window_show -> renpy.with_statement).
    #    Replace every _Feature shadow with the real export. Only these five
    #    names can be affected and only with_statement is a function, so this
    #    cannot touch the submodules the engine relies on.
    import __future__ as _zh_future
    _zh_feature_cls = type(_zh_future.division)
    for _zh_name, _zh_value in list(renpy.exports.__dict__.items()):
        if _zh_name.startswith("__"):
            continue
        if isinstance(getattr(renpy, _zh_name, None), _zh_feature_cls):
            setattr(renpy, _zh_name, _zh_value)


# ---------------------------------------------------------------------------
#  1. FONT.
#
#     Every font this game uses is Latin-only (Roboto, CourageRoad,
#     Montserrat, KeepSinging, DejaVu), so Chinese renders as tofu boxes.
#
#     Ren'Py 8.2 keys font_replacement_map on (filename, bold, italic) and
#     the value is a 3-tuple of the same shape -- renpy/text/font.py:714 does
#     `fn, bold, italics = renpy.config.font_replacement_map.get(t, t)`.
#     A FontGroup is NOT accepted here; use it as a style font instead.
#     NB: renpy.loadable does not exist in 8.2, it is renpy.loader.loadable.
# ---------------------------------------------------------------------------
init -100 python:

    ZH_FONT = "fonts/NotoSansSC-VF.ttf"

    if renpy.loader.loadable(ZH_FONT):
        #  NB: screens.rpy:1324 pins style.skip_triangle to "DejaVuSans.ttf",
        #  which this distribution does not actually ship (archive.rpa holds
        #  only CourageRoad, KeepSinging, Montserrat, Roboto-Regular and
        #  Roboto-Thin). Remapping it here is what stops the reference from
        #  dangling, so it stays in the list; the arrow glyph itself is fixed
        #  in the skip_indicator screen override at the end of this file.
        for _zh_old in ("Roboto-Regular.ttf",
                        "Roboto-Thin.ttf",
                        "CourageRoad.ttf",
                        "Montserrat.ttf",
                        "KeepSinging.ttf",
                        "DejaVuSans.ttf",
                        "DejaVuSans-Bold.ttf"):
            for _zh_bold in (False, True):
                for _zh_italic in (False, True):
                    renpy.config.font_replacement_map[
                        (_zh_old, _zh_bold, _zh_italic)] = (ZH_FONT, _zh_bold, _zh_italic)


init 999 python:

    import renpy.store

    # -----------------------------------------------------------------------
    #  2. WEIGHT PIN.
    #
    #     NotoSansSC-VF.ttf is a VARIABLE font and its fvar table says
    #     wght: min=100 default=100 max=900, i.e. the default instance is
    #     Thin -- body text renders hairline-thin and is hard to read. The
    #     name table calls itself "Thin" too, but fvar is the authority.
    #
    #     Ren'Py 8.2 exposes variable axes as the `axis` style property
    #     (registered in renpy/sl2/slproperties.py) and as an {axis:...}
    #     text tag. Setting it on the root style covers every style that does
    #     not override it; HarfBuzz ignores axes a font does not have, so this
    #     is safe for the remaining non-variable fonts.
    # -----------------------------------------------------------------------
    if renpy.loader.loadable("fonts/NotoSansSC-VF.ttf"):
        renpy.store.style.default.axis = { "wght": 400 }

    # -----------------------------------------------------------------------
    #  3. DEFAULT LANGUAGE.
    #
    #     config.default_language cannot be used: renpy/common/00defaults.rpy
    #     assigns it to None at init -1500 and consumes it inside that same
    #     block, so a later `define config.default_language = ...` is ignored.
    #     _preferences.language is what actually selects the language, and it
    #     is persistent -- so this only forces Chinese on a fresh install.
    #
    #     The game ships no renpy/common/00language.rpy, so there is no
    #     in-game language picker. To go back to English, use the console:
    #         renpy.change_language(None)
    # -----------------------------------------------------------------------
    if renpy.store._preferences.language is None:
        renpy.store._preferences.language = "schinese"


# ---------------------------------------------------------------------------
#  4. SKIP INDICATOR GLYPH.
#
#     screens.rpy:1278 draws three animated arrows next to "Skipping":
#
#         text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
#         text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
#         text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"
#
#     U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE is the one character in the
#     whole game that NotoSansSC-VF has no glyph for. Sweeping every glyph the
#     game can render -- all 29620 translated lines plus every string literal in
#     the script sources -- turns up nothing else, so the skip indicator is the
#     only place that needs attention and no font fallback is required.
#
#     The style points at "DejaVuSans.ttf", which this distribution does not
#     ship, so the intended font cannot be reached anyway. U+25B6 BLACK
#     RIGHT-POINTING TRIANGLE is the same shape one step up in the block and IS
#     present in NotoSansSC-VF, so the arrows are redrawn with it.
# ---------------------------------------------------------------------------
screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("跳过中")

            text "▶" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▶" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▶" at delayed_blink(0.4, 1.0) style "skip_triangle"


# --------------------------------------------------------------------------
#  zz_zh_names.rpy, verbatim from here down.
# --------------------------------------------------------------------------

# ===========================================================================
#  Por(n)tals 0.4 -- character name localisation.
#
#  Ren'Py does not route Character("Mom") through the translation system, so
#  the names are remapped instead: every ADVCharacter is rewritten as it is
#  constructed, and anything already living in the store is swept afterwards.
#
#  Keys are the exact literal strings used in the game's define statements.
#  Names that are expressions (e.g. "[mc_name]", the player's own name) are
#  deliberately absent -- they must keep evaluating.
# ===========================================================================

init -3000 python:

    ZH_CHARACTER_NAMES = {
        "Mom": "妈妈",
        "Dad": "爸爸",
        "Riley's mom": "莱莉的妈妈",
        "Riley's dad": "莱莉的爸爸",
        "Mr. Bradford": "布拉德福德先生",
        "Bodyguard": "保镖",
        "Dave": "戴夫",
        "Kate": "凯特",
        "Alice": "爱丽丝",
        "Riley": "莱莉",
        "Vanessa": "瓦妮莎",
        "Chad": "查德",
        "Chad's sister": "查德的妹妹",
        "Mr. Dyck": "戴克先生",
        "Elliot": "埃利奥特",
        "Ms. Bowers": "鲍尔斯女士",
        "Samantha": "萨曼莎",
        "Classmates": "同学们",
        "Man": "男人",
        "Woman": "女人",
        "Boy": "男孩",
        "Girl": "女孩",
        "Girls": "女孩们",
        "Shirtless guy": "光膀子男人",
        "Pantsless guy": "光屁股男人",
        "Fatty": "死胖子",
        "Horny guy": "色狼",
        "Eira": "艾拉",
        "Hostess": "女招待",
        "Host": "主持人",
        "Silver hair girl": "银发女孩",
        "Black hair girl": "黑发女孩",
        "Purple hair girl": "紫发女孩",
        "Green hair girl": "绿发女孩",
        "Blue hair woman": "蓝发女人",
        "Black hair woman": "黑发女人",
        "Middle-aged woman": "中年妇女",
        "Running girl": "跑步的女孩",
        "Pretty girl": "漂亮女孩",
        "Man with a dog": "牵狗的男人",
        "Man in hoodie": "连帽衫男人",
        "Man in red shirt": "红衬衫男人",
        "Bookworm": "书虫",
        "Student": "学生",
        "Teacher": "老师",
        "Merchant": "商人",
        "Beggar": "乞丐",
        "Nobleman": "贵族",
        "Prostitute": "妓女",
        "Knight 1": "骑士1",
        "Knight 2": "骑士2",
        "Sir Allone": "阿隆爵士",
        "Sir Enolla": "伊诺拉爵士",
        "Driver": "司机",
        "Crowd": "人群",
        "Hayden": "海登",
        "Drunk guy": "醉汉",
        "Drunkard": "酒鬼",
        "Fae": "仙灵",
        "Boss": "老板",
        "Valen": "瓦伦",
        "Tom": "汤姆",
        "Painter": "画家",
        "Both": "两人",
        "Porter": "搬运工",
        "Gangster 1": "混混1",
        "Gangster 2": "混混2",
        "Device": "设备",
        "Lucy": "露西",
        "Angel 1": "天使1",
        "Angel 2": "天使2",
        "Angel 3": "天使3",
        "Angel 4": "天使4",
        "Angel 5": "天使5",
        "Ad": "广告",
        "Muscular guy": "肌肉男",
        "Registrar": "教务处",
        "Guardian": "守护者",
        "Wizard": "巫师",
        "Theron": "西隆",
        "Adora": "阿多拉",
        "Jenna": "珍娜",
        "Troy": "特洛伊",
        "Marie": "玛丽",
        "Azalea": "杜鹃",
        "Primrose": "樱草",
        "Junkie": "瘾君子",
        "Ethan": "伊森",
        "Josh": "乔什",
        "Freddie": "弗雷迪",
        "Lexi": "莱克西",
        "Selena": "赛琳娜",
        "Ashley": "阿什莉",
        "Chester": "切斯特",
        "Emily": "艾米莉",
        "Kimberly": "金伯莉",
        "Maya": "玛雅",
        "Caleb": "凯莱布",
        "Olivia": "奥利维亚",
        "Mysterious man": "神秘男子",
        "Jayden": "杰登",
        "Adam": "亚当",
        "Police officer": "警察",
        "Candice": "坎迪斯",
        "Diana": "黛安娜",
        "Waitress": "女服务员",
        "Mage": "法师",
        "Mage 1": "法师1",
        "Mage 2": "法师2",
        "Eagle statue": "鹰雕像",
        "Human statue": "人雕像",
        "Ms. Korrin": "科林女士",
        "Ms. Lunareth": "露娜瑞丝女士",
        "Mr. Varyn": "瓦林先生",
        "Mr. Morgrave": "莫格瑞夫先生",
        "Mr. Bumblewise": "邦布尔怀斯先生",
        "Demon": "恶魔",
        "Elaris": "艾拉里斯",
        "Hero": "英雄",
        "Daphne": "达芙妮",
        "Andy": "安迪",
        "Mark": "马克",
        "Max": "马克斯",
        "Question [test_question_number]": "问题 [test_question_number]",
    }

    import renpy.character

    _zh_map = ZH_CHARACTER_NAMES
    _zh_adv_init = renpy.character.ADVCharacter.__init__

    def _zh_adv_init_zh(self, *args, **kwargs):
        if args and isinstance(args[0], str):
            args = (_zh_map.get(args[0], args[0]),) + args[1:]
        elif isinstance(kwargs.get("name"), str):
            kwargs["name"] = _zh_map.get(kwargs["name"], kwargs["name"])
        _zh_adv_init(self, *args, **kwargs)

    renpy.character.ADVCharacter.__init__ = _zh_adv_init_zh


init 999 python:

    import renpy.character, renpy.store

    def _zh_sweep(obj, depth, seen):
        if depth > 3:
            return
        if isinstance(obj, renpy.character.ADVCharacter):
            n = getattr(obj, "name", None)
            if isinstance(n, str) and n in _zh_map:
                obj.name = _zh_map[n]
            return
        if isinstance(obj, (list, tuple, set)):
            for x in obj:
                _zh_sweep(x, depth + 1, seen)
        elif isinstance(obj, dict):
            for x in obj.values():
                _zh_sweep(x, depth + 1, seen)

    for _k, _v in list(vars(renpy.store).items()):
        _zh_sweep(_v, 0, set())