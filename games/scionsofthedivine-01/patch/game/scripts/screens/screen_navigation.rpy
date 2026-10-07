init offset = -1

screen navigation():

    if renpy.get_screen("main_menu"):
        style_prefix "mm_navigation"

        vbox:
            xalign 0.05
            yalign 0.49
            spacing gui.navigation_spacing

            frame:
                style "empty"
                xysize (300, 70)
                textbutton _("开始"):
                    action Start()
                    at shiftr_hover
                    activate_sound "ui/Start - Alt.ogg"

            frame:
                style "empty"
                xysize (300, 70)
                textbutton _("读取"):
                    action ShowMenu("load")
                    at shiftr_hover

            frame:
                style "empty"
                xysize (300, 70)
                textbutton _("档案"):
                    action ShowMenu("profilesel")
                    at shiftr_hover
        
            frame:
                style "empty"
                xysize (300, 70)
                textbutton _("设置"):
                    action ShowMenu("preferences")
                    at shiftr_hover

            frame:
                style "empty"
                xysize (300, 70)
                textbutton _("制作人员"):
                    action ShowMenu("credits")
                    at shiftr_hover

            if renpy.variant("pc"):
                frame:
                    style "empty"
                    xysize (300, 70)
                    textbutton _("退出"):
                        action Quit(confirm=not main_menu)
                        at shiftr_hover

    elif not main_menu:
        style_prefix "gm_navigation"

        vbox:
            xalign 0.05
            yalign 0.5
            spacing gui.navigation_spacing

            if _in_replay:
                frame:
                    style "empty"
                    xysize (300, 70)
                    textbutton _("结束回放"):
                        action EndReplay(confirm=True)
                        at shiftr_hover

            frame:
                style "empty"
                xysize (300, 70)
                textbutton _("保存"):
                    action ShowMenu("save")
                    at shiftr_hover

            frame:
                style "empty"
                xysize (300, 70)
                textbutton _("读取"):
                    action ShowMenu("load")
                    at shiftr_hover

            frame:
                style "empty"
                xysize (300, 70)
                textbutton _("档案"):
                    action ShowMenu("profilesel")
                    at shiftr_hover

            frame:
                style "empty"
                xysize (300, 70)
                textbutton _("设置"):
                    action ShowMenu("preferences")
                    at shiftr_hover

            frame:
                style "empty"
                xysize (300, 70)
                textbutton _("主菜单"):
                    action MainMenu()
                    at shiftr_hover

            if renpy.variant("pc"):
                frame:
                    style "empty"
                    xysize (300, 70)
                    textbutton _("退出"):
                        action Quit(confirm=not main_menu)
                        at shiftr_hover

style mm_navigation_button is gui_button
style mm_navigation_button_text is gui_button_text

style mm_navigation_button:
    size_group "mm_navigation"
    properties gui.button_properties("navigation_button")
    align (0.5, 0.5)

style mm_navigation_button_text:
    properties gui.text_properties("navigation_button")
    font zh_display_font
    bold False
    size 52

style gm_navigation_button is gui_button
style gm_navigation_button_text is gui_button_text

style gm_navigation_button:
    size_group "gm_navigation"
    properties gui.button_properties("navigation_button")
    align (0.5, 0.5)

style gm_navigation_button_text:
    properties gui.text_properties("navigation_button")
    font zh_display_font
    bold False