# DropOut Saga 0.12.0b  --  replaces the mod's "modmenu" and "quick_menu"
#
# Two screens of the mod are replaced here, without touching its .rpyc:
#   modmenu     -- the 0.6.9a tab bar whose layout falls apart on 0.12.0b
#   quick_menu  -- the blue "Mod" image button and the "Shawn's Mod" entry
# What they became: the generated walkthrough (002_zh_guide_ui.rpy) plus two
# things the mod never had -- a stat editor and a scene launcher.
#
# HOW A SCREEN GETS OVERRIDDEN -- init priority first, filename only on a tie.
# The mod is not uniform about this:
#   modmenu, main_menu   top level, i.e. init 0
#   quick_menu           inside an "init 969:" block in Shawn_Overrides.rpy
# So a plain top-level screen here beats the first pair on the file-order tie
# (hence the zz_ prefix, game/zz_... sorts after game/mod/...) but loses to
# quick_menu outright, no matter what the file is called.  Everything below
# therefore sits in "init 999:".  Both variants are overridden, because the mod
# and the game each declare a touch one too and the touch variant would
# otherwise win on any build that puts "touch" in config.variants.
#
# On jumping: Call(label), not Jump.  Call pushes a return point, so a scene
# that ends with a return statement lands back where you were instead of
# unwinding the whole context stack.  Note that jumping into a mid-story
# label skips the scene setup its parent label did, so some entries open on a
# bare background.

default zh_tab = "guide"
default zh_jump_group = 0
default zh_jump_q = ""

# Only the variables 0.12.0b actually reads (tools/gates.py: 106 live of 217
# declared).  love_points / corruption_points are derived totals, and the 111
# dead ones -- every event_*, *_office, loyalty_*, and all *_power -- are not
# worth showing because nothing would ever read them back.
define zh_stats = [
    ("爱意 · 莱拉", "love_lila"),
    ("爱意 · 索菲娅", "love_sophia"),
    ("爱意 · 艾娃", "love_ava"),
    ("爱意 · 阿什莉", "love_ash"),
    ("爱意 · 亚苏娜", "love_asuna"),
    ("爱意 · 贾丝敏", "love_jas"),
    ("爱意 · 朱莉", "love_ju"),
    ("爱意 · 伊莎贝拉", "love_isa"),
    ("堕落 · 莱拉", "corruption_lila"),
    ("堕落 · 索菲娅", "corruption_sophia"),
    ("堕落 · 艾娃", "corruption_ava"),
    ("堕落 · 阿什莉", "corruption_ash"),
    ("堕落 · 贾丝敏", "corruption_jas"),
    ("总体堕落", "corruption"),
    ("善良", "goodness"),
    ("现金", "cash"),
    ("恐惧", "fear"),
    ("警方", "police"),
    ("平民", "civilians"),
    ("小势力声望", "newcomers"),
    ("群体", "herd"),
    ("天数", "day"),
]

init -18 python:

    def zh_stat(name):
        """Current value, tolerant of the pre-new-game state where default
        statements have not run yet."""
        return int(globals().get(name, 0) or 0)

    def zh_bump(name, delta):
        return zh_stat(name) + delta

    class ZhInputValue(InputValue):
        """Binds an input displayable to a store variable.

        InputValue is what an input's "value" has to be: Ren'Py grabs its
        .set_text as the changed hook (renpy/display/behavior.py, Input.__init__:
        "if value: ... changed = value.set_text").  Passing a plain string there
        dies with "'str' object has no attribute 'set_text'".

        Writing through globals() is deliberate.  That dict is
        store_dicts["store"] -- the same one the game reads -- whereas Ren'Py's
        own VariableInputValue goes through setattr on the store module, which
        is a different object (verified: renpy.store is not
        renpy.python.store_dicts["store"]).

        cast=int keeps the variable an int.  VariableInputValue would write the
        raw string, and the game evaluates things like "love_sophia > 50",
        which raises TypeError against a str in Python 3.
        """

        def __init__(self, variable, cast=None):
            self.variable = variable
            self.cast = cast

        def get_text(self):
            current = globals().get(self.variable, "")
            return "" if current is None else str(current)

        def set_text(self, s):
            text = s.strip()
            if text and (self.cast is None or text.lstrip("+-").isdigit()):
                globals()[self.variable] = (int(text) if self.cast is int else text)
            renpy.restart_interaction()

    def zh_jump_items():
        """Entries of the selected group, filtered by the search box; a blank
        query matches everything."""
        if not zh_jump_groups:
            return []
        group = zh_jump_groups[min(zh_jump_group, len(zh_jump_groups) - 1)]
        query = zh_jump_q.strip().lower()
        if not query:
            return group['items']
        return [it for it in group['items']
                if query in it['l'].lower() or query in it['d'].lower()]



# 999 rather than 1000: priorities outside -999..999 are out of the
# documented range, and lint nags about it while still exiting 0.
init 999:

    # config.name is already the full "堕落学园 0.12.0b" (options.rpy:15).
    # Building the title from it means a wrong glyph cannot be typed here.
    define zh_toolbox_title = renpy.config.name + " 工具箱"

    screen modmenu():
        zorder 5000
        modal True

        $ tabs = [("guide", "攻略"), ("stats", "属性")]

        frame:
            xalign 0.5
            yalign 0.5
            xsize 1160
            ysize 740
            padding (20, 16)
            background Solid("#141217f2")

            vbox:
                spacing 10
                xfill True
                yfill True

                hbox:
                    spacing 12
                    text zh_toolbox_title size 28 color "#f0ecf6"
                    null width 1
                    for tabkey, tabtext in tabs:
                        $ tabbg = Solid("#4a3f68") if zh_tab == tabkey else Solid("#241f2c")
                        textbutton tabtext:
                            action SetVariable("zh_tab", tabkey)
                            background tabbg
                            hover_background Solid("#4a3f68")
                            text_size 20
                            text_color "#f0ecf6"
                            xpadding 22
                            ypadding 6
                    null width 1
                    textbutton "返回 (Esc)":
                        action Hide("modmenu")
                        text_size 19
                        text_color "#cfc8dd"
                        hover_background Solid("#3a3450")
                        background Solid("#241f2c")
                        xpadding 18
                        ypadding 6

                null height 2

                if zh_tab == "guide":
                    use zhguide_body
                elif zh_tab == "stats":
                    use zh_stats_body
                else:
                    use zh_jump_body

        key "K_ESCAPE" action Hide("modmenu")
        key "game_menu" action Hide("modmenu")


    screen zh_stats_body():
        vbox:
            spacing 8
            xfill True
            yfill True

            text "属性编辑。点数值可以手输入精确值；改动立即生效，开始新存档前请确认。" size 15 color "#8b8599"

            viewport:
                ysize 596
                mousewheel True
                scrollbars "vertical"
                vscrollbar_xsize 10
                vscrollbar_base_bar Solid("#2a2436")
                vscrollbar_thumb Solid("#6f5fa8")

                vpgrid:
                    xsize 1090
                    cols 2
                    spacing 8

                    for disp, name in zh_stats:
                        frame:
                            xsize 538
                            background Solid("#1c1822")
                            padding (12, 7)
                            hbox:
                                spacing 6
                                text disp size 16 color "#cfc8dd" xsize 196
                                frame:
                                    xsize 78
                                    background Solid("#2a2436")
                                    padding (4, 2)
                                    input:
                                        value ZhInputValue(name, int)
                                        allow "-0-9"
                                        size 17
                                        color "#7fd18a"
                                        xalign 0.5
                                for delta, tint in ((-10, "#3a2f3f"), (-1, "#3a2f3f"), (1, "#2f3a35"), (10, "#2f3a35")):
                                    textbutton ("%+d" % delta):
                                        xsize 46
                                        action SetVariable(name, zh_bump(name, delta))
                                        background Solid(tint)
                                        hover_background Solid("#4a3f68")
                                        text_size 15
                                        text_color "#e8e4f0"


    screen zh_jump_body():
        $ items = zh_jump_items()

        vbox:
            xfill True
            yfill True
            spacing 10

            hbox:
                spacing 6
                for i, grp in enumerate(zh_jump_groups):
                    $ gbg = Solid("#4a3f68") if zh_jump_group == i else Solid("#241f2c")
                    textbutton grp['name']:
                        action SetVariable("zh_jump_group", i)
                        background gbg
                        hover_background Solid("#4a3f68")
                        text_size 17
                        text_color "#f0ecf6"
                        xpadding 14
                        ypadding 5
                null width 1
                $ count = "共 %d 个场景" % len(items)
                text count size 15 color "#7c7689" yalign 0.6

            hbox:
                spacing 8
                text "过滤" size 16 color "#8b8599" yalign 0.5
                frame:
                    xsize 360
                    background Solid("#241f2c")
                    padding (10, 4)
                    input:
                        value ZhInputValue("zh_jump_q")
                        size 16
                        color "#f0ecf6"
                textbutton "清除":
                    action SetVariable("zh_jump_q", "")
                    yalign 0.5
                    text_size 15
                    text_color "#cfc8dd"
                    hover_background Solid("#3a3450")
                    background Solid("#241f2c")
                    xpadding 14
                    ypadding 4
                null width 1
                text "输入场景名、label 或对白关键词，回车即生效" size 13 color "#6f6980" yalign 0.5

            null height 2

            # Explicit sizes all the way down: with yfill on the vboxes the
            # spare height was being spread between the rows, which left the
            # list floating in the middle of the panel.
            frame:
                xsize 1096
                ysize 540
                background Solid("#1c1822")
                padding (8, 8)

                vpgrid:
                    xsize 1080
                    ysize 524
                    cols 2
                    spacing 6
                    scrollbars "vertical"
                    vscrollbar_xsize 10
                    vscrollbar_base_bar Solid("#2a2436")
                    vscrollbar_thumb Solid("#6f5fa8")
                    mousewheel True

                    for it in items:
                        $ dtxt = it['d'][:42] if it['d'] else "（无对白）"
                        button:
                            xfill True
                            background Solid("#241f2c")
                            hover_background Solid("#2e2840")
                            action [Hide("modmenu"), Call(it['l'])]
                            frame:
                                xfill True
                                padding (12, 7)
                                background None
                                vbox:
                                    spacing 1
                                    text dtxt size 16 color "#eee9f6"
                                    text it['l'] size 12 color "#7c7689"


    # ---------------------------------------------------------------------------
    # quick_menu: drop the two mod buttons, keep the rest
    #
    # The mod replaced the game's quick_menu (screens.rpy:247) with an imagebutton
    # -- mod/images/btn_mod_%s.png, the blue "Mod" in the top right corner -- plus a
    # column of textbuttons whose first entry was "Shawn's Mod".  Both only ever
    # opened screen modmenu, which is the toolbox above, so they were clutter.
    #
    # Screen language cannot delete a child from somebody else's screen, so the
    # whole screen is replaced here.  What it keeps is the part of the mod's column
    # that is actually Ren'Py functionality: skip / auto / save, using the same
    # actions the game's own quick_menu uses.  The default quick_menu variable and
    # the overlay registration in screens.rpy are untouched.
    #
    # quick_menu is an overlay screen (screens.rpy: "config.overlay_screens.append
    # ('quick_menu')"), so it needs no Show call of its own.
    screen quick_menu():
        zorder 100

        if quick_menu:

            vbox:
                xalign 0.985
                yalign 1.0
                yoffset -16
                spacing 2

                textbutton "快进" action Skip() alternate Skip(fast=True, confirm=True)
                textbutton "自动" action Preference("auto-forward", "toggle")
                textbutton "保存" action ShowMenu("save")


    # The game's own screens.rpy declares a touch variant of every screen it owns,
    # and the mod overrode that one too, so override it as well or it would win on
    # any build that puts "touch" in config.variants.
    screen quick_menu():
        variant "touch"

        zorder 100

        if quick_menu:

            vbox:
                xalign 0.985
                yalign 1.0
                yoffset -16
                spacing 2

                textbutton "快进" action Skip() alternate Skip(fast=True, confirm=True)
                textbutton "自动" action Preference("auto-forward", "toggle")
                textbutton "保存" action ShowMenu("save")
