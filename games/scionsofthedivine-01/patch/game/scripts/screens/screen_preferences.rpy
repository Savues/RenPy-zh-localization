init offset = -1

init -2 python:
    gui_theme_colors = [
        ("#0066cc", "Blue"),
        ("#d10000", "Red"),
        ("#00cc00", "Green"),
        ("#7f00be", "Purple"),
        ("#c04d00", "Orange"),
        ("#c40062", "Pink")
    ]

    def cycle_theme_color():
        """Cycles through preset theme colors"""
        current = persistent.theme_color
        current_index = -1
        for i, (color, name) in enumerate(gui_theme_colors):
            if color == current:
                current_index = i
                break
        if current_index == -1:
            persistent.theme_color = gui_theme_colors[0][0]
        else:
            next_index = (current_index + 1) % len(gui_theme_colors)
            persistent.theme_color = gui_theme_colors[next_index][0]

        gui.rebuild()
    
    def set_theme_color(color):
        persistent.theme_color = color
        gui.rebuild()

screen preferences():
    tag menu
    $ pref_null = 200
    if mm_var:
        add "fog_effect"
        add "magic_effect" at theme_ember
    use game_menu(_("设置"), scroll="viewport"):

        vbox:
            xoffset 100
            style_prefix "pref"

            label _("屏幕")

            if renpy.variant("pc") or renpy.variant("web"):

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "显示模式"
                        null width pref_null
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")

            frame:
                background Frame("gui/frame3.webp", 10, 10)
                xysize (1200, 50)
                hbox:
                    frame:
                        style "empty"
                        xsize 400
                        text "回退显示侧"
                    null width pref_null
                    textbutton _("禁用") action Preference("rollback side", "disable")
                    textbutton _("左") action Preference("rollback side", "left")
                    textbutton _("右") action Preference("rollback side", "right")

            frame:
                background Frame("gui/frame3.webp", 10, 10)
                xysize (1200, 50)
                hbox:
                    frame:
                        style "empty"
                        xsize 400
                        text "转场特效"
                    null width pref_null
                    imagebutton:
                        background "gui/button/check.png"
                        idle "gui/button/check_idle.png"
                        hover "gui/button/check_idle.png"
                        selected_idle At("gui/button/check_selected.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
                        selected_hover At("gui/button/check_selected.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
                        action Preference("transitions", "toggle")
                        at pref_buttons

            vbox:
                label _("界面")

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "主题配色"
                        null width pref_null
                        hbox:
                            spacing 10
                            for color, name in gui_theme_colors:
                                textbutton "":
                                    background Solid(color)
                                    yoffset 4
                                    xsize 32
                                    ysize 32
                                    action Function(set_theme_color, color)
                                    at pref_buttons
                
                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "快捷按钮"
                        null width pref_null
                        imagebutton:
                            background "gui/button/check.png"
                            idle "gui/button/check_idle.png"
                            hover "gui/button/check_idle.png"
                            selected_idle At("gui/button/check_selected.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
                            selected_hover At("gui/button/check_selected.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
                            action ToggleVariable("quick_menu", true_value=True, false_value=False)
                            at pref_buttons
                
                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "解锁通知"
                        null width pref_null
                        imagebutton:
                            background "gui/button/check.png"
                            idle "gui/button/check_idle.png"
                            hover "gui/button/check_idle.png"
                            selected_idle At("gui/button/check_selected.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
                            selected_hover At("gui/button/check_selected.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
                            action ToggleVariable("persistent.notifications_unlocks", true_value=True, false_value=False)
                            at pref_buttons
            vbox:

                label _("秘技")

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "流程模式"
                        null width pref_null
                        imagebutton:
                            background "gui/button/check.png"
                            idle "gui/button/check_idle.png"
                            hover "gui/button/check_idle.png"
                            selected_idle At("gui/button/check_selected.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
                            selected_hover At("gui/button/check_selected.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
                            action ToggleVariable("persistent.walkthrough_mode", true_value=True, false_value=False)
                            at pref_buttons

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "开发菜单"
                        null width pref_null
                        imagebutton:
                            background "gui/button/check.png"
                            idle "gui/button/check_idle.png"
                            hover "gui/button/check_idle.png"
                            selected_idle At("gui/button/check_selected.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
                            selected_hover At("gui/button/check_selected.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
                            action ToggleVariable("persistent.dev_menu", true_value=True, false_value=False)
                            at pref_buttons

            vbox:
                style_prefix "bar"

                label _("对话")

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "自动快进"
                        null width pref_null
                        textbutton _("未读文本") action Preference("skip", "toggle") style "pref_wordbutton"
                        textbutton _("选择后") action Preference("after choices", "toggle") style "pref_wordbutton"

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "文字速度"
                        null width pref_null
                        bar value Preference("text speed") style "bar_bar" at pref_buttons

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            hbox:
                                text "文字大小（[persistent.text_size]/48）"
                        null width pref_null
                        bar value FieldValue(persistent, "text_size", min=16, max=48) style "bar_bar" at pref_buttons yoffset -6
                        textbutton _("默认") action SetVariable("persistent.text_size", 32)

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            hbox:
                                text "文字描边（[persistent.outlinesize]/5）"
                        null width pref_null
                        bar value FieldValue(persistent, "outlinesize", offset=0, range=5) style "bar_bar" at pref_buttons yoffset -6
                        textbutton _("默认") action SetVariable("persistent.outlinesize", 2)

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            hbox:
                                text "文本框不透明度"
                        null width pref_null
                        bar value FieldValue(persistent, "textbox_opacity", offset=0.0, range=1.0) style "bar_bar" at pref_buttons yoffset -6
                        textbutton _("默认") action SetVariable("persistent.textbox_opacity", 0.7)

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            hbox:
                                text "自动快进速度"
                        null width pref_null
                        bar value Preference("auto-forward time") style "bar_bar" at pref_buttons

            vbox:
                style_prefix "bar"
                spacing 0

                label _("音频")

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "总音量"
                        null width pref_null
                        bar value Preference("main volume") style "bar_bar" at pref_buttons

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "音乐音量" xsize 400
                        null width pref_null
                        bar value Preference("bgm volume") style "bar_bar" at pref_buttons

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "环境音量" xsize 400
                        null width pref_null
                        bar value Preference("bgs volume") style "bar_bar" at pref_buttons

                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "音效音量" xsize 400
                        null width pref_null
                        bar value Preference("sfx volume") style "bar_bar" at pref_buttons
                
                frame:
                    background Frame("gui/frame3.webp", 10, 10)
                    xysize (1200, 50)
                    hbox:
                        frame:
                            style "empty"
                            xsize 400
                            text "通知音量" xsize 400
                        null width pref_null
                        bar value Preference("notif volume") style "bar_bar" at pref_buttons

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_button is gui_button
style pref_button_text is gui_button_text
style pref_wordbutton is gui_button
style pref_wordbutton_text is gui_button_text
style bar_label is pref_label
style bar_label_text is pref_label_text
style bar_bar is gui_bar
style bar_button is gui_button
style bar_button_text is gui_button_text

style pref_text:
    xoffset 12
    yoffset -4
    outlines [(2, "#000000", 0, 0)]

style pref_text2:
    yoffset -4
    outlines [(2, "#000000", 0, 0)]

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0
    font zh_display_font

style pref_button:
    yalign 0.5
    
style pref_button_text:
    yoffset -6
    size 24

style pref_image_button:
    xoffset -2

style pref_wordbutton:
    yalign 0.5
    
style pref_wordbutton_text:
    yoffset -6
    size 24

style bar_text:
    xoffset 12
    yoffset -4
    outlines [(2, "#000000", 0, 0)]

style bar_bar:
    yalign 0.5
    xsize 400
    ysize 20
    left_bar At("gui/bar/pref_left.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)))
    hover_left_bar At("gui/bar/pref_left.png", Transform(matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.6)))
    right_bar "gui/bar/pref_right.png"
    thumb None

style bar_button:
    yalign 0.5
    left_margin 15

style bar_button_text:
    italic True
    yoffset -6
    size 24

style theme_preview_frame:
    background persistent.theme_color
    xalign 0.0
    yalign 0.5
