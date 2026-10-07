init offset = -1

default quick_menu = True
default quick_menu_disable = False

screen quick_menu():
    zorder 100

    if quick_menu and not quick_menu_disable:

        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0

            textbutton _("返回") action Rollback()
            textbutton _("历史记录") action ShowMenu('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("快速保存") action QuickSave()
            textbutton _("快速读取") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')
            if persistent.dev_menu:
                textbutton _("开发菜单"):
                    if renpy.get_screen("dev_menu"):
                        action Hide("dev_menu")
                    else:
                        action Show("dev_menu")


init python:
    config.overlay_screens.append("quick_menu")


style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
    size 16
