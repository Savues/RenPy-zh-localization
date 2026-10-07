init offset = -1

screen help():
    tag menu
    default device = "keyboard"

    use game_menu(_("控制"), scroll="viewport"):
        style_prefix "help"

        vbox:
            spacing 23
            xpos 100

            hbox:
                xalign 0.47

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")

                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("推进对话，不选择选项。")

    hbox:
        label _("方向键")
        text _("操作界面。")

    hbox:
        label _("Esc")
        text _("打开游戏菜单。")

    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("Page Up")
        text _("回退到之前的对话。")

    hbox:
        label _("Page Down")
        text _("快进到之后的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")

    hbox:
        label "Shift+A"
        text _("打开无障碍菜单。")


screen mouse_help():

    hbox:
        label _("左键")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键")
        text _("隐藏用户界面。")

    hbox:
        label _("右键")
        text _("打开游戏菜单。")

    hbox:
        label _("滚轮上")
        text _("回退到之前的对话。")

    hbox:
        label _("滚轮下")
        text _("快进到之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机 / A键（下）")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机 / L键")
        text _("回退到之前的对话。")

    hbox:
        label _("R键")
        text _("快进到之后的对话。")

    hbox:
        label _("十字键、摇杆")
        text _("操作界面。")

    hbox:
        label _("Start、Guide、B键（右）")
        text _("打开游戏菜单。")

    hbox:
        label _("Y键（上）")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0
