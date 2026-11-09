# =========================================================
# Cheat Menu - Wild Cats (中文汉化适配版)
# =========================================================

default persistent.wt_gallery_backup = None
default persistent.wt_selfies_backup = None

init -1 python:
    def _find_cheat_font():
        font_candidates = [
            "tl/chinese/font/LXGWWenKaiGB-Medium.ttf",
            "tl/chinese/font/FZLB.ttf",
            "tl/chinese/font/chinafont.ttf",
            "tl/chinese/chinese1.ttf",
            getattr(gui, "interface_text_font", None),
            getattr(gui, "text_font", None),
        ]
        for f in font_candidates:
            if f and renpy.loadable(f):
                return f
        return getattr(gui, "text_font", "DejaVuSans.ttf")

define cheat_font = _find_cheat_font()

init 1 python:

    CHEAT_AFF_MIN = 0
    CHEAT_AFF_MAX = 30
    CHEAT_AFF_FULL = 20

    cheat_girls = [
        ("eve",     "伊芙 (Eve)",       "eve_affection",     "eve_status"),
        ("zoe",     "佐伊 (Zoe)",       "zoe_affection",     "zoe_status"),
        ("desiree", "黛丝瑞 (Desiree)",   "Desiree_affection", "Desiree_status"),
        ("fiona",   "菲奥娜 (Fiona)",     "Fiona_affection",   "Fiona_status"),
        ("saki",    "纱纪 (Saki)",      "Saki_affection",    "Saki_status"),
        ("lexi",    "莱茜 (Lexi)",      "Lexi_affection",    "Lexi_status"),
    ]

    cheat_statuses = [
        ("Acquaintance", "相识"),
        ("Platonic",     "知己"),
        ("Romantic",     "浪漫"),
    ]
    cheat_status_dict = dict(cheat_statuses)

    cheat_scene_flags = [
        ("伊芙特殊剧情已触发 (Eve H1)",     "eveH1"),
        ("佐伊特殊剧情已触发 (Zoe H1)",     "ZoeH1"),
        ("黛丝瑞特殊剧情已触发 (Desiree H1)", "desireeH1"),
        ("纱纪特殊剧情已触发 (Saki H1)",    "SakiH1"),
        ("莱茜特殊剧情1已触发 (Lexi H1)",   "lexiH1"),
        ("莱茜特殊剧情2已触发 (Lexi H2)",   "lexiH2"),
    ]

    def cheat_get(name, default=0):
        return getattr(renpy.store, name, default)

    def cheat_set(name, value):
        setattr(renpy.store, name, value)

    def cheat_sync_profiles():
        fn = getattr(renpy.store, "init_char", None)
        if fn is not None:
            try:
                fn()
            except Exception:
                pass

    def cheat_adjust_affection(var, delta):
        value = cheat_get(var, 0) + delta
        cheat_set(var, max(CHEAT_AFF_MIN, min(CHEAT_AFF_MAX, value)))
        cheat_sync_profiles()

    def cheat_set_status(var, status):
        cheat_set(var, status)
        cheat_sync_profiles()

    def cheat_max_all_affection():
        for gid, name, aff, status in cheat_girls:
            cheat_set(aff, CHEAT_AFF_FULL)
        cheat_sync_profiles()
        renpy.notify("全员好感度已设为 " + str(CHEAT_AFF_FULL))

    def cheat_reset_all_affection():
        for gid, name, aff, status in cheat_girls:
            cheat_set(aff, 0)
            cheat_set(status, "")
        cheat_sync_profiles()
        renpy.notify("全员好感度已重置")

    def cheat_set_all_status(status):
        for gid, name, aff, st in cheat_girls:
            cheat_set(st, status)
        cheat_sync_profiles()
        renpy.notify("全员关系已设为 " + cheat_status_dict.get(status, status))

    def cheat_adjust_var(name, delta, low=0):
        cheat_set(name, max(low, cheat_get(name, 0) + delta))

    def cheat_toggle_var(name):
        cheat_set(name, not cheat_get(name, False))

    # ---- 画廊解锁 ----
    def gallery_labels():
        return [s[0] for scenes in character_scenes.values() for s in scenes]

    def gallery_all_unlocked():
        return all(renpy.seen_label(l) for l in gallery_labels())

    def unlock_gallery_all():
        seen = renpy.game.persistent._seen_ever
        if persistent.wt_gallery_backup is None:
            persistent.wt_gallery_backup = [l for l in gallery_labels() if l in seen]
        for l in gallery_labels():
            seen[l] = True
        renpy.notify("全CG画廊已解锁")

    def lock_gallery_all():
        seen = renpy.game.persistent._seen_ever
        keep = persistent.wt_gallery_backup or []
        for l in gallery_labels():
            if l not in keep:
                seen.pop(l, None)
        persistent.wt_gallery_backup = None
        renpy.notify("画廊记录已恢复")

    def cheat_toggle_gallery():
        if gallery_all_unlocked():
            lock_gallery_all()
        else:
            unlock_gallery_all()

    # ---- 自拍解锁 ----
    cheat_selfies_all = [
        ('lexi', 'horizontal', 'gui/selfies/lexi1.webp'),
        ('lexi', 'horizontal', 'gui/selfies/lexi2.webp'),
        ('eve', 'horizontal', 'gui/selfies/eve1.webp'),
        ('lexi', 'horizontal', 'gui/selfies/lexi3.webp'),
        ('lexi', 'horizontal', 'gui/selfies/lexi4.webp'),
        ('lexi', 'horizontal', 'gui/selfies/lexi6.webp'),
        ('lexi', 'horizontal', 'gui/selfies/lexi5.webp'),
        ('lexi', 'horizontal', 'gui/selfies/lexi7.webp'),
        ('lexi', 'horizontal', 'gui/selfies/lexi8.webp'),
        ('lexi', 'horizontal', 'gui/selfies/lexi9.webp'),
        ('desiree', 'horizontal', 'gui/selfies/desiree1.webp'),
        ('eve', 'horizontal', 'gui/selfies/eve2.webp'),
        ('zoe', 'horizontal', 'gui/selfies/zoe1.webp'),
        ('zoe', 'horizontal', 'gui/selfies/zoe2.webp'),
        ('zoe', 'horizontal', 'gui/selfies/zoe3.webp'),
        ('saki', 'horizontal', 'gui/selfies/saki1.webp'),
        ('zoe', 'horizontal', 'gui/selfies/zoe4.webp'),
        ('lexi', 'horizontal', 'gui/selfies/lexi10.webp'),
        ('desiree', 'horizontal', 'gui/selfies/desiree3.webp'),
        ('desiree', 'horizontal', 'gui/selfies/desiree2.webp'),
        ('eve', 'horizontal', 'gui/selfies/eve4.webp'),
        ('eve', 'horizontal', 'gui/selfies/eve3.webp'),
        ('saki', 'horizontal', 'gui/selfies/saki3.webp'),
        ('saki', 'horizontal', 'gui/selfies/saki2.webp'),
        ('zoe', 'horizontal', 'gui/selfies/zoe6.webp'),
        ('zoe', 'horizontal', 'gui/selfies/zoe5.webp'),
        ('fiona', 'horizontal', 'gui/selfies/fiona1.webp'),
        ('fiona', 'horizontal', 'gui/selfies/fiona2.webp'),
        ('desiree', 'horizontal', 'gui/selfies/desiree4.webp'),
    ]

    def selfies_have(name, orient, path):
        lst = (persistent.character_selfies or {}).get(name, [])
        return any(len(e) > 1 and e[0] == orient and e[1] == path for e in lst)

    def selfies_all_unlocked():
        if persistent.character_selfies is None:
            return False
        return all(selfies_have(n, o, p) for n, o, p in cheat_selfies_all)

    def unlock_selfies_all():
        store_dict = persistent.character_selfies
        if store_dict is None:
            return
        if persistent.wt_selfies_backup is None:
            persistent.wt_selfies_backup = dict((k, [list(e) for e in v]) for k, v in store_dict.items())
        for n, o, p in cheat_selfies_all:
            lst = store_dict.setdefault(n, [])
            if not selfies_have(n, o, p):
                lst.append([o, p])
        renpy.save_persistent()
        renpy.notify("自拍照片已全部解锁")

    def lock_selfies_all():
        store_dict = persistent.character_selfies
        backup = persistent.wt_selfies_backup
        if store_dict is None or backup is None:
            return
        for k in list(store_dict.keys()):
            store_dict[k][:] = [list(e) for e in backup.get(k, [])]
        persistent.wt_selfies_backup = None
        renpy.save_persistent()
        renpy.notify("自拍照片记录已恢复")

    def cheat_toggle_selfies():
        if selfies_all_unlocked():
            lock_selfies_all()
        else:
            unlock_selfies_all()

    def cheat_toggle_hints():
        persistent.wt_hints_on = not persistent.wt_hints_on

    def cheat_value_text(value):
        return "{color=#ff9a3c}" + str(value) + "{/color}"

style cheat_panel:
    background Frame("BladeSSRMod/CheatUI/panel_dark.png", 36, 36)
    padding (0, 0)

style cheat_sidebar:
    background Frame("BladeSSRMod/CheatUI/panel_side.png", 30, 30)
    padding (22, 24)

style cheat_card:
    background Frame("BladeSSRMod/CheatUI/card_bg.png", 22, 22)

style cheat_brand:
    font cheat_font
    size 34
    color "#ff9a3c"
    outlines [(2, "#000000aa", 0, 0)]

style cheat_brand_sub:
    font cheat_font
    size 20
    color "#7d818c"

style cheat_credit:
    font cheat_font
    size 28
    color "#ff9a3c"
    outlines [(2, "#000000aa", 0, 0)]

style cheat_heading:
    font cheat_font
    size 36
    color "#e8e6e2"
    outlines [(2, "#000000aa", 0, 0)]

style cheat_label:
    font cheat_font
    size 24
    color "#e8e6e2"

style cheat_name:
    font cheat_font
    size 24
    color "#e8e6e2"

style cheat_tag:
    font cheat_font
    size 18
    color "#7d818c"

style cheat_value:
    font cheat_font
    size 26
    text_align 0.5

style cheat_tab_button:
    xsize 216
    ysize 56
    background Frame("BladeSSRMod/CheatUI/pill_idle.png", 26, 26)
    hover_background Frame("BladeSSRMod/CheatUI/pill_hover.png", 26, 26)
    selected_background Frame("BladeSSRMod/CheatUI/pill_selected.png", 26, 26)
    padding (20, 12)
    margin (0, 5)

style cheat_tab_button_text is default:
    outlines []
    yalign 0.5
    font cheat_font
    size 24
    color "#7d818c"
    selected_color "#ff9a3c"
    hover_color "#ffb15c"
    xalign 0.0

style cheat_action_button is button:
    background Frame("BladeSSRMod/CheatUI/pill_idle.png", 26, 26)
    hover_background Frame("BladeSSRMod/CheatUI/pill_hover.png", 26, 26)
    selected_background Frame("BladeSSRMod/CheatUI/pill_selected.png", 26, 26)
    padding (22, 10)

style cheat_action_button_text is default:
    outlines []
    yalign 0.5
    font cheat_font
    size 22
    color "#e8e6e2"
    hover_color "#ffb15c"
    selected_color "#ff9a3c"

style cheat_mini_button is button:
    xysize (46, 40)
    background Frame("BladeSSRMod/CheatUI/pill_idle.png", 18, 18)
    hover_background Frame("BladeSSRMod/CheatUI/pill_hover.png", 18, 18)
    selected_background Frame("BladeSSRMod/CheatUI/pill_selected.png", 18, 18)
    padding (0, 0)

style cheat_mini_button_text is default:
    outlines []
    font cheat_font
    size 22
    color "#e8e6e2"
    hover_color "#ffb15c"
    selected_color "#ff9a3c"
    xalign 0.5
    yalign 0.5

style cheat_mini_wide_button is cheat_mini_button:
    xsize 130

style cheat_status_button is cheat_mini_wide_button:
    xsize 156

style cheat_status_button_text is cheat_mini_button_text:
    size 20

style cheat_close_button is button:
    background Frame("BladeSSRMod/CheatUI/pill_idle.png", 22, 22)
    hover_background Frame("BladeSSRMod/CheatUI/pill_hover.png", 22, 22)
    padding (18, 8)

style cheat_close_button_text is default:
    outlines []
    yalign 0.5
    font cheat_font
    size 22
    color "#e8e6e2"
    hover_color "#ffb15c"

transform cheat_panel_appear:
    alpha 0.0
    zoom 0.94
    ease 0.30 alpha 1.0 zoom 1.0

transform cheat_scrim_appear:
    alpha 0.0
    ease 0.22 alpha 1.0

screen cheat_overlay():
    zorder 190
    key "alt_K_c" action ShowMenu("cheatmenu")

init 2 python:
    if "cheat_overlay" not in config.overlay_screens:
        config.overlay_screens.append("cheat_overlay")

init 1:
    screen quick_menu():
        zorder 100
        if quick_menu:
            hbox:
                style_prefix "quick"
                xalign 0.5
                yalign 1.0
                textbutton _("Back") action Rollback()
                textbutton _("History") action ShowMenu('history')
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Save") action ShowMenu('save')
                textbutton _("Q.Save") action QuickSave()
                textbutton _("Q.Load") action QuickLoad()
                textbutton _("Prefs") action ShowMenu('preferences')
                textbutton "作弊" action ShowMenu('cheatmenu')
            frame:
                background None
                xysize (108 , 134)
                align  (1.0 , .0 )
                offset (-100, 100)
                button:
                    xysize   (108, 134)
                    xycenter (.5 , .5 )
                    action [ ShowMenu('points'), Function(init_char) ]
                    image 'gui/clipboard.png' xycenter (.5, .5) alpha .5:
                        at transform:
                            subpixel True
                            on idle:
                                easein_quint 1.0 rotate 0  zoom 1.0
                            on hover:
                                easein_quint 1.0 rotate 15 zoom 1.25
                    activate_sound 'audio/ui/click.wav'
                    hover_sound    'audio/ui/hover.mp3'

    screen quick_menu():
        variant "touch"
        zorder 100
        if quick_menu:
            hbox:
                style_prefix "quick"
                xalign 0.5
                yalign 1.0
                textbutton _("Back") action Rollback()
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Menu") action ShowMenu()
                textbutton "作弊" action ShowMenu('cheatmenu')
            frame:
                background None
                xysize (108 , 134)
                align  (1.0 , .0 )
                offset (-100, 100)
                button:
                    xysize   (108, 134)
                    xycenter (.5 , .5 )
                    action ShowMenu('points')
                    image 'gui/clipboard.png' xycenter (.5, .5):
                        at transform:
                            subpixel True
                            on idle:
                                easein_quint 1.0 rotate 0  zoom 1.0
                            on hover:
                                easein_quint 1.0 rotate 15 zoom 1.25
                    activate_sound 'audio/ui/click.wav'
                    hover_sound    'audio/ui/hover.mp3'

screen cheatmenu():
    tag menu
    modal True
    default tab = "girls"
    key "game_menu" action Return()
    add "#000000b0" at cheat_scrim_appear

    frame:
        style "cheat_panel"
        xysize (1480, 900)
        xalign 0.5
        yalign 0.5
        at cheat_panel_appear

        textbutton "关闭":
            style "cheat_close_button"
            text_style "cheat_close_button_text"
            xalign 1.0
            yalign 0.0
            xoffset -18
            yoffset 16
            action Return()

        hbox:
            spacing 0
            xysize (1480, 900)

            frame:
                style "cheat_sidebar"
                xysize (260, 900)
                fixed:
                    xysize (216, 852)
                    vbox:
                        pos (0, 0)
                        spacing 2
                        text "Wild Cats" style "cheat_brand"
                        text "作弊菜单" style "cheat_brand_sub"

                    vbox:
                        xsize 216
                        yalign 1.0
                        spacing 4
                        text "模组原作者" style "cheat_brand_sub" xalign 0.5
                        text "BladeSSR" style "cheat_credit" xalign 0.5
                        imagebutton:
                            xalign 0.5
                            idle Transform("BladeSSRMod/CheatUI/F95_Button.png", zoom=0.6)
                            hover Transform("BladeSSRMod/CheatUI/F95_Button_Hover.png", zoom=0.6)
                            action OpenURL("https://f95zone.to/members/bladessr.2806260/")

                    vbox:
                        pos (0, 90)
                        spacing 8
                        textbutton "角色好感":
                            style "cheat_tab_button"
                            text_style "cheat_tab_button_text"
                            selected (tab == "girls")
                            action SetScreenVariable("tab", "girls")

                        textbutton "剧情解锁":
                            style "cheat_tab_button"
                            text_style "cheat_tab_button_text"
                            selected (tab == "story")
                            action SetScreenVariable("tab", "story")

                        textbutton "场景旗标":
                            style "cheat_tab_button"
                            text_style "cheat_tab_button_text"
                            selected (tab == "scenes")
                            action SetScreenVariable("tab", "scenes")

            vbox:
                pos (40, 30)
                spacing 22
                xsize 1160

                if tab == "girls":
                    text "角色好感与状态" style "cheat_heading"
                    grid 2 3:
                        spacing 16
                        for gid, gname, avar, svar in cheat_girls:
                            $ aff = cheat_get(avar, 0)
                            $ stat = cheat_get(svar, "")
                            $ pct = max(0.0, min(1.0, aff / float(CHEAT_AFF_FULL)))
                            $ display_stat = cheat_status_dict.get(stat, stat) if stat else "暂无关系状态"

                            frame:
                                style "cheat_card"
                                xysize (544, 216)
                                padding (22, 16)
                                vbox:
                                    spacing 10
                                    fixed:
                                        xsize 500
                                        ysize 36
                                        text "[gname]" style "cheat_name"
                                        text "[display_stat]" style "cheat_tag" xalign 1.0 yalign 0.5

                                    hbox:
                                        spacing 12
                                        yalign 0.5
                                        fixed:
                                            xysize (330, 16)
                                            yalign 0.5
                                            add Solid("#00000080") xysize (330, 16)
                                            add Solid("#e08c3e") xysize (max(4, int(330 * pct)), 16)
                                        text cheat_value_text(aff) style "cheat_value" xsize 60

                                    hbox:
                                        spacing 8
                                        style_prefix "cheat_mini"
                                        textbutton "−" action Function(cheat_adjust_affection, avar, -1)
                                        textbutton "+" action Function(cheat_adjust_affection, avar, 1)
                                        textbutton "+5" action Function(cheat_adjust_affection, avar, 5)
                                        textbutton "最大":
                                            style "cheat_mini_wide_button"
                                            text_style "cheat_mini_button_text"
                                            action Function(cheat_set, avar, CHEAT_AFF_FULL)

                                    hbox:
                                        spacing 6
                                        style_prefix "cheat_mini"
                                        for st_val, st_lbl in cheat_statuses:
                                            textbutton st_lbl:
                                                style "cheat_status_button"
                                                text_style "cheat_status_button_text"
                                                selected (stat == st_val)
                                                action Function(cheat_set_status, svar, st_val)

                    hbox:
                        spacing 18
                        style_prefix "cheat_action"
                        textbutton "全员好感最大" action Function(cheat_max_all_affection)
                        textbutton "重置全员好感" action Function(cheat_reset_all_affection)
                        textbutton "全员浪漫关系" action Function(cheat_set_all_status, "Romantic")

                elif tab == "story":
                    text "剧情与全局解锁" style "cheat_heading"
                    frame:
                        style "cheat_card"
                        xsize 1120
                        padding (26, 18)
                        hbox:
                            spacing 20
                            yalign 0.5
                            text "伊芙心情 (Eve Mood)" style "cheat_label" xsize 320
                            text cheat_value_text(cheat_get("evemood", 0)) style "cheat_value" xsize 60
                            hbox:
                                spacing 8
                                style_prefix "cheat_mini"
                                textbutton "−" action Function(cheat_adjust_var, "evemood", -1, -10)
                                textbutton "+" action Function(cheat_adjust_var, "evemood", 1, -10)
                                textbutton "重置":
                                    style "cheat_mini_wide_button"
                                    text_style "cheat_mini_button_text"
                                    action Function(cheat_set, "evemood", 0)

                    frame:
                        style "cheat_card"
                        xsize 1120
                        padding (26, 18)
                        hbox:
                            spacing 20
                            yalign 0.5
                            text "选项攻略提示" style "cheat_label" xsize 320
                            textbutton ("已开启" if persistent.wt_hints_on else "已关闭"):
                                style "cheat_action_button"
                                text_style "cheat_action_button_text"
                                selected persistent.wt_hints_on
                                action Function(cheat_toggle_hints)

                    frame:
                        style "cheat_card"
                        xsize 1120
                        padding (26, 18)
                        hbox:
                            spacing 20
                            yalign 0.5
                            text "全CG回忆画廊" style "cheat_label" xsize 320
                            textbutton ("已解锁" if gallery_all_unlocked() else "未解锁"):
                                style "cheat_action_button"
                                text_style "cheat_action_button_text"
                                selected gallery_all_unlocked()
                                action Function(cheat_toggle_gallery)

                    frame:
                        style "cheat_card"
                        xsize 1120
                        padding (26, 18)
                        hbox:
                            spacing 20
                            yalign 0.5
                            text "自拍照片全收集" style "cheat_label" xsize 320
                            textbutton ("已解锁" if selfies_all_unlocked() else "未解锁"):
                                style "cheat_action_button"
                                text_style "cheat_action_button_text"
                                selected selfies_all_unlocked()
                                action Function(cheat_toggle_selfies)

                elif tab == "scenes":
                    text "场景旗标" style "cheat_heading"
                    text "这些旗标会影响后续对话判定。若要解锁全部CG画廊与自拍照片，请使用【剧情解锁】标签页。" style "cheat_tag"
                    grid 2 3:
                        spacing 16
                        for flabel, fvar in cheat_scene_flags:
                            frame:
                                style "cheat_card"
                                xysize (544, 96)
                                padding (26, 18)
                                hbox:
                                    spacing 20
                                    yalign 0.5
                                    text "[flabel]" style "cheat_label" xsize 360
                                    textbutton ("已看" if cheat_get(fvar, False) else "未看"):
                                        style "cheat_mini_wide_button"
                                        text_style "cheat_mini_button_text"
                                        selected cheat_get(fvar, False)
                                        action Function(cheat_toggle_var, fvar)
