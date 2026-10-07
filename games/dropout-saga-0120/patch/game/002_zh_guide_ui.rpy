# DropOut Saga 0.12.0b  --  walkthrough panel
#
# The mod's own nine walkthrough screens are built around 0.6.9a story-step
# counters that no longer exist in 0.12.0b.  Rather than resurrect those, this
# panel is generated from what the 0.12.0b scripts actually gate on: the
# option -> stat deltas and the numeric thresholds, extracted by tools/gates.py.
#
# It is the first tab of screen modmenu (see zz_zh_tools_ui.rpy, which replaces
# the mod's own modmenu).  Scene jumping used to be a third tab; it now lives
# here -- the switch in the header row swaps this panel for the scene list, and
# every entry below carries a jump button, so you go from "what does this
# choice do" to "put me in that scene" without leaving the page.
#
# Two Ren'Py notes that cost time here:
#   - Show("x") takes a SCREEN NAME, not a tag.  The screen is named zhguide
#     and uses no tag so that the ordinary Show/Hide calls just work.
#   - The entry is unconditional: this build has no game/main.rpy, so Ren'Py's
#     main_menu flag is never set, and renpy.get_screen() returns None while
#     overlay screens are still being built.

default zh_guide_day = 1
default zh_guide_sel = 0
default zh_guide_list = False

init -19 python:

    import re

    def zh_sub(text):
        """nickname_sophia1 is a store variable -- "亲爱的" by default, whatever
        the player has been called since -- so the generated data keeps the bare
        name and it gets swapped in here, at display time.

        The lookup goes through globals() because that dict IS the store:
        Ren'Py execs init python blocks with store_dicts["store"] as globals,
        so zh_sub.__globals__ tracks every later change.  getattr on
        renpy.store does not work -- that is not the store dict.
        """
        scope = globals()
        def repl(match):
            value = scope.get(match.group(0))
            return value if isinstance(value, str) and value else match.group(0)
        return re.sub(r'\bnickname_\w+\b', repl, text)

    def zh_guide_cur():
        """The record for the day currently being browsed, index-safe."""
        for entry in zh_guide_days:
            if entry['day'] == zh_guide_day:
                return entry
        return zh_guide_days[0] if zh_guide_days else {'day': zh_guide_day,
                                                        'c': [], 'g': [], 'a': []}

    def zh_guide_sel_of(entry):
        if not entry['c']:
            return None
        return entry['c'][min(zh_guide_sel, len(entry['c']) - 1)]


init -5 python:
    if 'zh_guide_entry' not in config.overlay_screens:
        config.overlay_screens.append('zh_guide_entry')


screen zh_guide_entry():
    zorder 4000

    key "K_F4" action Show("modmenu")

    if not renpy.get_screen("modmenu"):
        textbutton "攻略":
            xalign 0.985
            yalign 0.80
            xpadding 20
            ypadding 8
            text_size 20
            text_color "#e8e4f0"
            hover_background Solid("#3a3450")
            background Solid("#241f2cd0")
            action Show("modmenu")


# Split in two so the modmenu shell can Use it: the body has no frame, no
# zorder and no key handling, only the content.
screen zhguide_body():
    $ cur = zh_guide_cur()
    $ sel = zh_guide_sel_of(cur)
    $ switch = "返回内容" if zh_guide_list else "场景列表"

    vbox:
        xfill True
        yfill True
        spacing 10

        # ---- day tabs, or the scene-list switch ----------------------
        hbox:
            spacing 6
            if not zh_guide_list:
                for entry in zh_guide_days:
                    $ tabbg = Solid("#4a3f68") if zh_guide_day == entry['day'] else Solid("#241f2c")
                    textbutton ("第%d天  %d项" % (entry['day'], len(entry['c']))):
                        action [SetVariable("zh_guide_day", entry['day']),
                                SetVariable("zh_guide_sel", 0)]
                        background tabbg
                        hover_background Solid("#4a3f68")
                        text_size 18
                        text_color "#f0ecf6"
                        xpadding 16
                        ypadding 7
            else:
                text "场景列表" size 19 color "#f0ecf6" yalign 0.7
            null width 1
            textbutton switch:
                action SetVariable("zh_guide_list", not zh_guide_list)
                background Solid("#241f2c")
                hover_background Solid("#4a3f68")
                text_size 17
                text_color "#cfc8dd"
                xpadding 16
                ypadding 7

        if zh_guide_list:
            # The old third tab, now a view of this one.
            use zh_jump_body

        else:
            null height 2

            # ---- choices ---------------------------------------------
            hbox:
                spacing 14
                ysize 440

                vpgrid:
                    xsize 540
                    ysize 440
                    cols 1
                    spacing 6
                    scrollbars "vertical"
                    vscrollbar_xsize 10
                    vscrollbar_base_bar Solid("#2a2436")
                    vscrollbar_thumb Solid("#6f5fa8")
                    mousewheel True
                    for i, ch in enumerate(cur['c']):
                        $ rowbg = Solid("#3a3350") if zh_guide_sel == i else Solid("#1e1a24")
                        $ dtxt = "、".join(ch.get('d', []))
                        button:
                            xfill True
                            background rowbg
                            hover_background Solid("#2e2840")
                            action SetVariable("zh_guide_sel", i)
                            frame:
                                xfill True
                                padding (12, 8)
                                background None
                                vbox:
                                    spacing 2
                                    hbox:
                                        spacing 8
                                        text ch['t'] size 18 color "#eee9f6"
                                        null width 1
                                        text dtxt size 15 color "#7fd18a" xalign 1.0
                                    if ch.get('k'):
                                        text ("需要：" + " 且 ".join(ch['k'])) size 14 color "#e0a95f"
                                    if ch.get('p'):
                                        text zh_sub(ch['p'][0]) size 14 color "#9891a8"

                frame:
                    xsize 566
                    background Solid("#1c1822")
                    padding (16, 14)
                    vbox:
                        spacing 8
                        if sel is None:
                            text "这一天没有影响数值的选项。" size 18 color "#7c7689"
                        else:
                            text sel['t'] size 23 color "#f0ecf6"
                            if sel.get('d'):
                                $ dsel = "、".join(sel['d'])
                                hbox:
                                    spacing 6
                                    text "数值：" size 16 color "#8b8599"
                                    text dsel size 17 color "#7fd18a"
                            if sel.get('k'):
                                text ("解锁条件：" + " 且 ".join(sel['k'])) size 16 color "#e0a95f"
                            text "场景：%s（第 %s 行）" % (sel['s'] or '主流程', sel['l']) size 13 color "#6f6980"
                            if sel['s']:
                                textbutton "跳到这个场景":
                                    action [Hide("modmenu"), Call(sel['s'])]
                                    text_size 15
                                    text_color "#7fd18a"
                                    hover_background Solid("#2f3a35")
                                    background Solid("#241f2c")
                                    xpadding 16
                                    ypadding 4
                            null height 4
                            viewport:
                                ysize 300
                                mousewheel True
                                scrollbars "vertical"
                                vscrollbar_xsize 10
                                vscrollbar_base_bar Solid("#2a2436")
                                vscrollbar_thumb Solid("#6f5fa8")
                                vbox:
                                    spacing 6
                                    for line in sel.get('p', []):
                                        text zh_sub(line) size 16 color "#c9c2d6"

            # ---- thresholds and story-driven changes -------------------
            hbox:
                spacing 14
                ysize 130

                frame:
                    xsize 553
                    ysize 130
                    background Solid("#1c1822")
                    padding (14, 10)
                    vbox:
                        spacing 4
                        text "数值门控" size 17 color "#e0a95f"
                        if not cur['g']:
                            text "无" size 15 color "#6f6980"
                        else:
                            viewport:
                                ysize 82
                                mousewheel True
                                scrollbars "vertical"
                                vscrollbar_xsize 10
                                vscrollbar_base_bar Solid("#2a2436")
                                vscrollbar_thumb Solid("#6f5fa8")
                                vbox:
                                    spacing 2
                                    for g in cur['g']:
                                        hbox:
                                            spacing 8
                                            text ("· 第%d天  %s" % (cur['day'], g['c'])) size 14 color "#d6cfa4" xsize 420
                                            if g['s']:
                                                textbutton "跳转":
                                                    action [Hide("modmenu"), Call(g['s'])]
                                                    text_size 12
                                                    text_color "#7fd18a"
                                                    hover_background Solid("#2f3a35")
                                                    background Solid("#241f2c")
                                                    xpadding 10
                                                    ypadding 2

                frame:
                    xsize 553
                    ysize 130
                    background Solid("#1c1822")
                    padding (14, 10)
                    vbox:
                        spacing 4
                        text "剧情自动变化" size 17 color "#8b8599"
                        if not cur['a']:
                            text "无" size 15 color "#6f6980"
                        else:
                            viewport:
                                ysize 82
                                mousewheel True
                                scrollbars "vertical"
                                vscrollbar_xsize 10
                                vscrollbar_base_bar Solid("#2a2436")
                                vscrollbar_thumb Solid("#6f5fa8")
                                vbox:
                                    spacing 2
                                    for a in cur['a']:
                                        hbox:
                                            spacing 8
                                            text ("· " + a['t']) size 14 color "#b6afc4" xsize 420
                                            if a['s']:
                                                textbutton "跳转":
                                                    action [Hide("modmenu"), Call(a['s'])]
                                                    text_size 12
                                                    text_color "#7fd18a"
                                                    hover_background Solid("#2f3a35")
                                                    background Solid("#241f2c")
                                                    xpadding 10
                                                    ypadding 2


screen zhguide():
    zorder 5000
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1160
        ysize 740
        padding (20, 16)
        background Solid("#141217f2")

        vbox:
            spacing 10
            hbox:
                spacing 12
                text "堕落学园 0.12.0b 攻略" size 28 color "#f0ecf6"
                text "选项 · 数值 · 解锁条件" size 16 color "#8b8599" yalign 0.8
                null width 1
                textbutton "返回 (Esc)":
                    action Hide("zhguide")
                    xalign 1.0
                    text_size 19
                    text_color "#cfc8dd"
                    hover_background Solid("#3a3450")
                    background Solid("#241f2c")
                    xpadding 18
                    ypadding 6

            use zhguide_body

    key "K_ESCAPE" action Hide("zhguide")
    key "game_menu" action Hide("zhguide")
