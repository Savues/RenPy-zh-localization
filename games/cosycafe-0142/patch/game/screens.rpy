################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")
    hover_sound "gui/msp1/hover.mp3"
    activate_sound "gui/msp1/click.mp3"

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    # Dialogue box opacity
    window

    style_prefix "say"

    window:
        id "window"

        # Dialogue box opacity
        if renpy.variant("pc"):
            background Transform(Frame("gui/textbox.png",xalign=0.5, yalign=1.0, ysize=278), alpha=persistent.dialogueBoxOpacity)
        else:
            background Transform(Frame("gui/phone/textbox.png",xalign=0.5, yalign=1.0), alpha=persistent.dialogueBoxOpacity)

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who" outlines [ (persistent.border_thickness, persistent.border_colour, 1, 1.2) ] size persistent.text_size

        text what id "what" outlines [ (persistent.border_thickness, persistent.border_colour, 1, 1.2) ] size persistent.text_size


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    #background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style block1_multiple2_say_window:
    xalign 0.5
    xfill True
    yalign 0.91
    ysize gui.textbox_height

style block2_multiple2_say_window:
    xalign 0.5
    xfill True
    yalign 1.07
    ysize gui.textbox_height

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input


screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("返回") action Rollback()
            textbutton _("历史记录") action ShowMenu('history')
            textbutton _("跳过") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("快速保存") action QuickSave()
            textbutton _("快速读取") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')
            textbutton _("隐藏界面") action HideInterface()
            textbutton _("静音") action Preference("all mute", "toggle")

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

#------------------------ Rob TopGUI ---------------------------------------------------------------------------------
init python:
    config.overlay_screens.append("TopGUI")



################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("开始游戏") action Start()

        else:

            textbutton _("历史记录") action ShowMenu("history")

            textbutton _("保存") action ShowMenu("save")

        textbutton _("读取") action ShowMenu("load")

        textbutton _("偏好设置") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("主菜单") action MainMenu()

        if main_menu:

            textbutton _("关于") action ShowMenu("about")

        textbutton _("角色档案") action [ ShowMenu("bios"), Function(refresh_character_stats) ]

        if main_menu:

            textbutton _("回放画廊") action ShowMenu("gallery")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("帮助") action ShowMenu("help")

        textbutton _("Patreon") action OpenURL("https://www.patreon.com/cosycreator?utm_source=in-game&utm_medium=menu-button")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("退出") action Quit(confirm=not main_menu)

    ##/// ROB NOTE - Main Menu Version Number
    if main_menu:
        vbox:
            xalign 0.99
            yalign 0.01
            text "版本 0.8.1 — 制作：Cosy Creator" size 20 color ("#b0b0b0")

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

default scroll = 0

screen main_menu():

    tag menu

    add gui.main_menu_background
    add "gui/msp1/main_menu/bg.png":
        at transform:

            xycenter (.5, .5)
            zoom      .6
            blur       5

            ease_quint (1.0 * persistent.ui_speed_multiplier) zoom .5 blur .0
    add "gui/msp1/main_menu/title.png"
    default b_hovered = None

    default button1_h = None
    default button2_h = None
    default button3_h = None
    default button4_h = None
    default button5_h = None
    default button6_h = None
    default button7_h = None

    $ tooltip = GetTooltip()

    if tooltip:
        frame:
            background None
            xysize (407, 250)
            pos    (515, 132)
            text tooltip.upper() font "fonts/MiSans-Regular.ttf" size 24 offset (25, 15)
            at transform:

                alpha   .0
                xoffset -250

                easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 xoffset .0 blur .0

    default patreon_h = None
    default substar_h = None
    default discord_h = None
    frame:
        background "gui/msp1/main_menu/plate.png"
        xysize (96  , 242)
        pos    (1724, 419)
        vbox:
            xysize (66, 214)
            align  (.5, .5)
            spacing 9
            frame:
                background None
                xalign .5
                button:

                    hovered   [ SetScreenVariable("patreon_h", 1) ]
                    unhovered [ SetScreenVariable("patreon_h", 0) ]

                    action OpenURL("https://www.patreon.com/cosycreator?utm_source=in-game&utm_medium=about-button")

                    image "gui/msp1/main_menu/patreon.png" xycenter (.5, .5)
                    image im.MatrixColor("gui/msp1/main_menu/patreon.png", im.matrix.colorize("#161616", "#ffb1df")) xycenter (.5, .5):
                        if patreon_h == 1:
                            at BAPR()
                        elif patreon_h == 0:
                            at BDPR()
                        else:
                            at BNT()

                    align  (.5, .5)
                    xycenter (.5, .5)
                    xysize (66, 64)

                    at transform:

                        subpixel  True

                        xycenter (.5, .5)

                        on hover:

                            easein_quint (.3 * persistent.ui_speed_multiplier) xzoom .95 yzoom .95

                        on idle:

                            easein_quint (.3 * persistent.ui_speed_multiplier) xzoom 1.0 yzoom 1.0

                xysize (66, 64)
            frame:
                background None
                xalign .5
                button:

                    hovered   [ SetScreenVariable("substar_h", 1) ]
                    unhovered [ SetScreenVariable("substar_h", 0) ]

                    action OpenURL("https://subscribestar.adult/cosy-creator")

                    image "gui/msp1/main_menu/substar.png" xycenter (.5, .5)
                    image im.MatrixColor("gui/msp1/main_menu/substar.png", im.matrix.colorize("#161616", "#ffb1df")) xycenter (.5, .5):
                        if substar_h == 1:
                            at BAPR()
                        elif substar_h == 0:
                            at BDPR()
                        else:
                            at BNT()

                    align  (.5, .5)
                    xycenter (.5, .5)
                    xysize (66, 66)

                    at transform:

                        subpixel  True

                        xycenter (.5, .5)

                        on hover:

                            easein_quint (.3 * persistent.ui_speed_multiplier) xzoom .95 yzoom .95

                        on idle:

                            easein_quint (.3 * persistent.ui_speed_multiplier) xzoom 1.0 yzoom 1.0

                xysize (66, 66)
            frame:
                background None
                xalign .5
                button:

                    hovered   [ SetScreenVariable("discord_h", 1) ]
                    unhovered [ SetScreenVariable("discord_h", 0) ]

                    action OpenURL("https://discord.gg/U9CwvDf2vV")

                    image "gui/msp1/main_menu/discord.png" xycenter (.5, .5)
                    image im.MatrixColor("gui/msp1/main_menu/discord.png", im.matrix.colorize("#161616", "#ffb1df")) xycenter (.5, .5):
                        if discord_h == 1:
                            at BAPR()
                        elif discord_h == 0:
                            at BDPR()
                        else:
                            at BNT()

                    align  (.5, .5)
                    xycenter (.5, .5)
                    xysize (60, 66)

                    at transform:
                    
                        subpixel  True

                        xycenter (.5, .5)

                        on hover:

                            easein_quint (.3 * persistent.ui_speed_multiplier) xzoom .95 yzoom .95

                        on idle:

                            easein_quint (.3 * persistent.ui_speed_multiplier) xzoom 1.0 yzoom 1.0

                xysize (60, 66)
    frame:
        background None
        align      (.0, .5)
        xysize     (407, 816)
        xoffset    100
        vbox:
            align (.5, .5)
            spacing 8
            vbox:

                spacing 8
                frame:
                    background None
                    xysize (407, 250)
                    button:

                        focus_mask True

                        hovered   [ SetScreenVariable("b_hovered", "main"), SetScreenVariable("button1_h", 1) ]
                        unhovered [ SetScreenVariable("b_hovered", None), SetScreenVariable("button1_h", 0) ]

                        action Start()


                        frame:
                            image AlphaMask(At("gui/msp1/main_menu/main.png", button_image_mm()), "gui/msp1/main_menu/Main_m.png") offset (-6, -6)
                            image AlphaMask(At("gui/msp1/main_menu/main.png", button_image_mm()), "gui/msp1/main_menu/Main_m.png") offset (-6, -6):
                                if button1_h == 1:
                                    at BAPR()
                                elif button1_h == 0:
                                    at BDPR()
                                else:
                                    at BNT()
                            background None
                            xysize (407, 250)
                            xycenter (.5, .5)


                        text "开始游戏".upper() font "fonts/MiSans-Regular.ttf" size 48 align (.0, 1.0) offset (25, -5) at button_text_enlarge()

                        tooltip "开始故事。"

                        xycenter (.5, .5)
                        xysize (407, 250)
                    at button_cascade(.0)
                frame:
                    background None
                    xysize (407, 124)
                    button:

                        focus_mask True

                        hovered   [ SetScreenVariable("b_hovered", "load"), SetScreenVariable("button2_h", 1) ]
                        unhovered [ SetScreenVariable("b_hovered", None), SetScreenVariable("button2_h", 0) ]

                        action ShowMenu('load')

                        frame:
                            image AlphaMask(At("gui/msp1/main_menu/load.png", button_image_mm()), "gui/msp1/main_menu/Sub1_m.png") offset (-6, -6)
                            image AlphaMask(At("gui/msp1/main_menu/load.png", button_image_mm()), "gui/msp1/main_menu/Sub1_m.png") offset (-6, -6):
                                if button2_h == 1:
                                    at BAPR()
                                elif button2_h == 0:
                                    at BDPR()
                                else:
                                    at BNT()
                            background None
                            xysize (407, 124)
                            xycenter (.5, .5)


                        text "读取存档".upper() font "fonts/MiSans-Regular.ttf" size 48 align (.0, 1.0) offset (25, -5) at button_text_enlarge()

                        tooltip "读取已保存的存档。"

                        xycenter (.5, .5)
                        xysize (407, 124)
                    at button_cascade(.05)
                frame:
                    background None
                    xysize (407, 124)
                    button:

                        focus_mask True

                        hovered   [ SetScreenVariable("b_hovered", "gallery"), SetScreenVariable("button3_h", 1) ]
                        unhovered [ SetScreenVariable("b_hovered", None), SetScreenVariable("button3_h", 0) ]

                        action Show("gallery_pre")

                        frame:
                            image AlphaMask(At("gui/msp1/main_menu/gallery.png", button_image_mm()), "gui/msp1/main_menu/Sub1_m.png") offset (-6, -6)
                            image AlphaMask(At("gui/msp1/main_menu/gallery.png", button_image_mm()), "gui/msp1/main_menu/Sub1_m.png") offset (-6, -6):
                                if button3_h == 1:
                                    at BAPR()
                                elif button3_h == 0:
                                    at BDPR()
                                else:
                                    at BNT()
                            background None
                            xysize (407, 124)
                            xycenter (.5, .5)


                        text "画廊".upper() font "fonts/MiSans-Regular.ttf" size 48 align (.0, 1.0) offset (25, -5) at button_text_enlarge()

                        tooltip "查看插画与场景。"

                        xycenter (.5, .5)
                        xysize (407, 124)
                    at button_cascade(.1)
                frame:
                    background None
                    xysize (407, 124)
                    button:

                        focus_mask True

                        hovered   [ SetScreenVariable("b_hovered", "bios"), SetScreenVariable("button4_h", 1) ]
                        unhovered [ SetScreenVariable("b_hovered", None), SetScreenVariable("button4_h", 0) ]

                        action [ Function(refresh_character_stats), ShowMenu("bios") ]

                        frame:
                            image AlphaMask(At("gui/msp1/main_menu/bios.png", button_image_mm()), "gui/msp1/main_menu/Sub1_m.png") offset (-6, -6)
                            image AlphaMask(At("gui/msp1/main_menu/bios.png", button_image_mm()), "gui/msp1/main_menu/Sub1_m.png") offset (-6, -6):
                                if button4_h == 1:
                                    at BAPR()
                                elif button4_h == 0:
                                    at BDPR()
                                else:
                                    at BNT()
                            background None
                            xysize (407, 124)
                            xycenter (.5, .5)


                        text "角色档案".upper() font "fonts/MiSans-Regular.ttf" size 48 align (.0, 1.0) offset (25, -5) at button_text_enlarge()

                        tooltip "阅读角色档案。"

                        xycenter (.5, .5)
                        xysize (407, 124)
                    at button_cascade(.15)
                frame:
                    background None
                    xysize (407, 124)
                    button:

                        focus_mask True

                        hovered   [ SetScreenVariable("b_hovered", "prefs"), SetScreenVariable("button5_h", 1) ]
                        unhovered [ SetScreenVariable("b_hovered", None), SetScreenVariable("button5_h", 0) ]

                        action [ SetVariable('nav_active_screen', 'preferences'), ShowMenu('preferences')]

                        frame:
                            image AlphaMask(At("gui/msp1/main_menu/prefs.png", button_image_mm()), "gui/msp1/main_menu/Sub1_m.png") offset (-6, -6)
                            image AlphaMask(At("gui/msp1/main_menu/prefs.png", button_image_mm()), "gui/msp1/main_menu/Sub1_m.png") offset (-6, -6):
                                if button5_h == 1:
                                    at BAPR()
                                elif button5_h == 0:
                                    at BDPR()
                                else:
                                    at BNT()
                            background None
                            xysize (407, 124)
                            xycenter (.5, .5)


                        text "选项".upper() font "fonts/MiSans-Regular.ttf" size 48 align (.0, 1.0) offset (25, -5) at button_text_enlarge()

                        tooltip "修改设置与偏好。"

                        xycenter (.5, .5)
                        xysize (407, 124)
                    at button_cascade(.2)
            hbox:

                spacing 8
                frame:
                    background None
                    xysize (200, 30)
                    button:

                        focus_mask True

                        hovered   [ SetScreenVariable("button6_h", 1) ]
                        unhovered [ SetScreenVariable("button6_h", 0) ]

                        action ShowMenu('about')

                        frame:
                            background None
                            image "gui/msp1/main_menu/about.png" xycenter (.5, .5)
                            image im.MatrixColor("gui/msp1/main_menu/about.png", im.matrix.colorize("#ffb1df", "#ffffff")) xycenter (.5, .5):
                                if button6_h == 1:
                                    at BAPR()
                                elif button6_h == 0:
                                    at BDPR()
                                else:
                                    at BNT()
                            xysize (200, 30)

                        tooltip "了解游戏与制作人员。"

                        xycenter (.5, .5)
                    at fade_in(.0)
                if renpy.variant('pc'):
                    frame:
                        background None
                        xysize (200, 30)
                        button:

                            focus_mask True

                            hovered   [ SetScreenVariable("button7_h", 1) ]
                            unhovered [ SetScreenVariable("button7_h", 0) ]

                            action Quit(confirm=True)

                            frame:
                                background None
                                image "gui/msp1/main_menu/quit.png" xycenter (.5, .5)
                                image im.MatrixColor("gui/msp1/main_menu/quit.png", im.matrix.colorize("#ffb1df", "#ffffff")) xycenter (.5, .5):
                                    if button7_h == 1:
                                        at BAPR()
                                    elif button7_h == 0:
                                        at BDPR()
                                    else:
                                        at BNT()
                                xysize (200, 30)

                            tooltip "退出游戏。"

                            xycenter (.5, .5)
                        at fade_in(.0)
                else:
                    null width 200 height 30
screen gallery_pre():

    modal True

    imagebutton:
        idle "gui/overlay/confirm.png"
        action Hide('gallery_pre')
        hover_sound None
        at fade_in()

    default galleryi_h = None
    default gallerys_h = None
    hbox:
        align (.5, .5)
        frame:
            background None
            xysize (498, 815)
            button:

                focus_mask True

                hovered   [ SetScreenVariable("galleryi_h", 1) ]
                unhovered [ SetScreenVariable("galleryi_h", 0) ]

                action [ Hide("gallery_pre"), ui.callsinnewcontext("gallery_name"), ShowMenu('replay_gallery'), SetVariable('nav_active', False), Function(refresh_replay_gallery_content) ]

                frame:
                    image AlphaMask(At("gui/msp1/gallery_ui/replay.png", button_image_mm()), "gui/msp1/gallery_ui/gallery_button.png") offset (-6, -6)
                    image AlphaMask(At("gui/msp1/gallery_ui/replay.png", button_image_mm()), "gui/msp1/gallery_ui/gallery_button.png") offset (-6, -6):
                        if galleryi_h == 1:
                            at BAPR()
                        elif galleryi_h == 0:
                            at BDPR()
                        else:
                            at BNT()
                    background None
                    xysize (445, 762)
                    xycenter (.5, .5)


                text "场景".upper() font "fonts/MiSans-Regular.ttf" size 48 align (.5, 1.0) offset (0, -55) at button_text_enlarge() text_align .5 color "#161616"

                xycenter (.5, .5)
                xysize (498, 815)
            at button_cascade_bottom(.0)
        frame:
            background None
            xysize (498, 815)
            button:

                focus_mask True

                hovered   [ SetScreenVariable("gallerys_h", 1) ]
                unhovered [ SetScreenVariable("gallerys_h", 0) ]

                action [ Hide("gallery_pre"), ShowMenu('photo_gallery'), SetVariable('nav_active', False), Function(refresh_images), Function(init_images) ]

                frame:
                    image AlphaMask(At("gui/msp1/gallery_ui/images.png", button_image_mm()), "gui/msp1/gallery_ui/gallery_button.png") offset (-6, -6)
                    image AlphaMask(At("gui/msp1/gallery_ui/images.png", button_image_mm()), "gui/msp1/gallery_ui/gallery_button.png") offset (-6, -6):
                        if gallerys_h == 1:
                            at BAPR()
                        elif gallerys_h == 0:
                            at BDPR()
                        else:
                            at BNT()
                    background None
                    xysize (445, 762)
                    xycenter (.5, .5)


                text "图片".upper() font "fonts/MiSans-Regular.ttf" size 48 align (.5, 1.0) offset (0, -55) at button_text_enlarge() text_align .5 color "#161616"

                xycenter (.5, .5)
                xysize (498, 815)
            at button_cascade_bottom(.0)

    # use navigation

    # if gui.show_name:

    #     vbox:
    #         style "main_menu_vbox"

    #         text "[config.name!t]":
    #             style "main_menu_title"

    #         text "[config.version]":
    #             style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu():

        style_prefix "about"

        vbox:

            label "[config.name!t]" text_color "#f1f1f1" text_size 96
            text _("版本 [config.version!t]\n")

            text _("制作：Cosy Creator") size 48
            text _("{a=https://www.patreon.com/cosycreator}{color=#ffaeae}Patreon{/color}{/a} - {a=https://subscribestar.adult/cosy-creator}{color=#00db90}SubscribeStar{/color}{/a} - {a=https://discord.gg/U9CwvDf2vV}{color=#7289da}Discord{/color}{/a}\n") size 43

            text _("{size=38}创始人{/size}\nJovian Hart、Foxhound7231、Gem Dragon、SenMaster、Integral、Kaseval、Versalen、TeenTitan64、Supreme Idiot、Aern Drath\n") size 28

            text _("{size=38}测试与校对{/size}\nAbs、Integral、Segasuas、moderateUtopia、TeenTitan、Kaseval、Hurley、Mordred、Aern Drath、CosyArchivist\n") size 28

            text _("Pax of Misfits Creatives（UI 设计） - {a=https://www.patreon.com/misfitscreatives}{color=#ffaeae}Patreon{/color}{/a}")

            text _("ChainZ（HS2／画面建议） - {a=https://www.patreon.com/cw/SonderTalesVN}{color=#ffaeae}Patreon{/color}{/a}\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("使用 {a=https://www.renpy.org/}Ren’Py{/a} [renpy.version_only] 制作。\n[renpy.license!t]") size 16


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
    font "fonts/MiSans-Regular.ttf"

style about_text:
    font "fonts/MiSans-Regular.ttf"


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存"))


screen load():

    tag menu

    use file_slots(_("读取"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("PAGE {}".upper()), auto=_("Automatic saves".upper()), quick=_("Quick saves".upper()))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            add "gui/msp1/fileslots/bar.png" align (.5, .0) offset (0, 749):
                at transform:
                    alpha  .0
                    blur    25
                    zoom   .0

                    easein_quint (.75 * persistent.ui_speed_multiplier) alpha 1.0 blur 0 zoom 1.0

            ## The page name, which can be edited by clicking on a button.
            frame background None:
                xysize (215, 36)
                align  (1.0, .0)
                button:

                    align (1.0, .0)
                    offset (12, -18)
                    key_events True
                    action page_name_value.Toggle()

                    input:
                        value page_name_value
                        font "fonts/MiSans-Regular.ttf"
                        size 32
                        align  (1.0, .0)
                        text_align 1.0
                        color "#f1f1f1"

            ## The grid of file slots.
            frame background None:
                xysize (1291, 733)
                align  (.5  , .0 )
                grid 3 3:
                    xycenter (.5, .5)

                    spacing 8

                    for i in range(3 * 3):

                        $ slot = i + 1

                        frame background None:
                            xysize (425, 239)
                            button:
                                xycenter (.5 , .5 )
                                action FileAction(slot)

                                frame background None:
                                    xysize (425, 239)
                                    offset (-6 , -6)
                                    image "gui/msp1/fileslots/fileslot.png"
                                    image AlphaMask(FileScreenshot(slot), Transform("gui/msp1/fileslots/fileslot_alpha.png", matrixcolor = ColorizeMatrix("#fff", "#fff")))
                                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M").upper(), empty=_("empty slot".upper())) font "fonts/MiSans-Regular.ttf" size 18 align (.0, 1.0) offset (24, 0)
                                    # text FileSaveName(slot)
                                key "save_delete" action FileDelete(slot)
                                at transform:
                                    matrixcolor BrightnessMatrix(.0)
                                    on hover:
                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.2)
                                    on idle:
                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                            at transform:
                                alpha .0
                                blur   25
                                zoom  .0
                                
                                pause ((i*.05) * persistent.ui_delay_multiplier)

                                easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 blur 0 zoom 1.0

                ## Buttons to access other pages.
            frame background None:
                xysize (1240, 70 )
                align  (.5  , 1.0)

                hbox:

                    xycenter (.5, .5)

                    spacing 8

                    at transform:
                        alpha  .0
                        blur    25
                        zoom   .0

                        easein_quint (.75 * persistent.ui_speed_multiplier) alpha 1.0 blur 0 zoom 1.0

                    # # Disable << on auto page
                    # if (FileCurrentPage() == "auto"):
                    #     textbutton "<<" action() sensitive(False)

                    # # Make << send to auto page if on quick page
                    # if (FileCurrentPage() == "quick"):
                    #     textbutton "<<" action FilePage("auto")

                    # elif (FileCurrentPage() != "auto" and FileCurrentPage() != "quick"):

                    #     # Make << send to auto page if below page 10
                    #     if int(FileCurrentPage()) <= 9:
                    #         textbutton "<<" action FilePage("auto")

                    #     # Make << send to quick page if on page 10
                    #     elif int(FileCurrentPage()) == 10:
                    #         textbutton "<<" action FilePage("quick")

                    #     # Make << decrement page count by 10
                    #     else:
                    #         textbutton "<<" action FilePage(int(FileCurrentPage()) - 10)


                    frame background None:
                        xysize (70, 70)
                        button:
                            xycenter (.5, .5)
                            at transform:
                                matrixcolor BrightnessMatrix(.0)
                                on hover:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.2)
                                on idle:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                            frame:
                                background "gui/msp1/fileslots/indicator.png"
                                xycenter (.5, .5)
                                xysize (70, 70)
                                text _("<<") align (.5, .5) offset (0, 0) size 32 font "fonts/MiSans-Regular.ttf"
                            if (FileCurrentPage() == "auto"):
                                action NullAction()
                            if (FileCurrentPage() == "quick"):
                                action FilePage("auto")
                            elif (FileCurrentPage() != "auto" and FileCurrentPage() != "quick"):
                                if int(FileCurrentPage()) <= 9:
                                    action FilePage("auto")
                                elif int(FileCurrentPage()) == 10:
                                    action FilePage("quick")
                                else:
                                    action FilePage(int(FileCurrentPage()) - 10)
                    frame background None:
                        xysize (70, 70)
                        button:
                            xycenter (.5, .5)
                            at transform:
                                matrixcolor BrightnessMatrix(.0)
                                on hover:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.2)
                                on idle:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                            frame:
                                background "gui/msp1/fileslots/indicator.png"
                                xycenter (.5, .5)
                                xysize (70, 70)
                                text _("<") align (.5, .5) offset (0, 0) size 32 font "fonts/MiSans-Regular.ttf"
                            action FilePagePrevious()

                    if config.has_autosave:
                        frame background None:
                            xysize (70, 70)
                            button:
                                xycenter (.5, .5)
                                at transform:
                                    matrixcolor BrightnessMatrix(.0)
                                    on hover:
                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.2)
                                    on idle:
                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                                frame:
                                    background "gui/msp1/fileslots/indicator.png"
                                    xycenter (.5, .5)
                                    xysize (70, 70)
                                    text _("{#auto_page}A") align (.5, .5) offset (0, 0) size 32 font "fonts/MiSans-Regular.ttf"
                                action FilePage("auto")

                    if config.has_quicksave:
                        frame background None:
                            xysize (70, 70)
                            button:
                                xycenter (.5, .5)
                                at transform:
                                    matrixcolor BrightnessMatrix(.0)
                                    on hover:
                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.2)
                                    on idle:
                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                                frame:
                                    background "gui/msp1/fileslots/indicator.png"
                                    xycenter (.5, .5)
                                    xysize (70, 70)
                                    text _("{#quick_page}Q") align (.5, .5) offset (0, 0) size 32 font "fonts/MiSans-Regular.ttf"
                                action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        frame background None:
                            xysize (70, 70)
                            button:
                                xycenter (.5, .5)
                                at transform:
                                    matrixcolor BrightnessMatrix(.0)
                                    on hover:
                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.2)
                                    on idle:
                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                                frame:
                                    background "gui/msp1/fileslots/indicator.png"
                                    xycenter (.5, .5)
                                    xysize (70, 70)
                                    text "[page]" align (.5, .5) offset (0, 0) size 32 font "fonts/MiSans-Regular.ttf"
                                action FilePage(page)

                    frame background None:
                        xysize (70, 70)
                        button:
                            xycenter (.5, .5)
                            at transform:
                                matrixcolor BrightnessMatrix(.0)
                                on hover:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.2)
                                on idle:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                            frame:
                                background "gui/msp1/fileslots/indicator.png"
                                xycenter (.5, .5)
                                xysize (70, 70)
                                text _(">") align (.5, .5) offset (0, 0) size 32 font "fonts/MiSans-Regular.ttf"
                            action FilePageNext()
                    frame background None:
                        xysize (70, 70)
                        button:
                            xycenter (.5, .5)
                            at transform:
                                matrixcolor BrightnessMatrix(.0)
                                on hover:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.2)
                                on idle:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                            frame:
                                background "gui/msp1/fileslots/indicator.png"
                                xycenter (.5, .5)
                                xysize (70, 70)
                                text _(">>") align (.5, .5) offset (0, 0) size 32 font "fonts/MiSans-Regular.ttf"
                            if (FileCurrentPage() != "auto" and FileCurrentPage() != "quick"):
                                action FilePage(int(FileCurrentPage()) + 10)
                            else:
                                action FilePage(10)

            key 'any_K_RIGHT' action FilePageNext()
            key 'any_K_LEFT'  action FilePagePrevious()
            if (FileCurrentPage() != "auto" and FileCurrentPage() != "quick"):
                key 'any_K_UP' action FilePage(int(FileCurrentPage()) + 10)
            else:
                key 'any_K_UP' action FilePage(10)
            # Disable << on auto page
            if (FileCurrentPage() == "auto"):
                key 'any_K_DOWN' action NullAction()

            # Make << send to auto page if on quick page
            if (FileCurrentPage() == "quick"):
                key 'any_K_DOWN' action FilePage("auto")

            elif (FileCurrentPage() != "auto" and FileCurrentPage() != "quick"):

                # Make << send to auto page if below page 10
                if int(FileCurrentPage()) <= 9:
                    key 'any_K_DOWN' action FilePage("auto")

                # Make << send to quick page if on page 10
                elif int(FileCurrentPage()) == 10:
                    key 'any_K_DOWN' action FilePage("quick")

                # Make << decrement page count by 10
                else:
                    key 'any_K_DOWN' action FilePage(int(FileCurrentPage()) - 10)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 1.0
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        for h in _history_list:

            window:
                hbox:
                    spacing 24

                    if h.who:

                        label [h.who]:
                            style "history_name"
                            substitute False

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                            text_font "fonts/MiSans-Regular.ttf"

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False
                        font "fonts/MiSans-Regular.ttf"

            if not _history_list:
                label _("The dialogue history is empty.")
    # vbar value YScrollValue('history') xysize (16, 805) align (1.0, .5) offset (-6, 0)
        # for h in _history_list:

        #     window:
        #         xysize (1651, 156)
        #         vbox:
        #             spacing 8
        #             $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
        #             if h.who:

        #                 label h.who:
                            
        #                     substitute False

        #                     text_size 37
        #                     text_font "fonts/MiSans-Regular.ttf"
        #                     ## Take the color of the who text from the Character, if
        #                     ## set.
        #                     if "color" in h.who_args:
        #                         text_color h.who_args["color"]

        #                 text what:
        #                     substitute False
        #                     font "fonts/MiSans-Regular.ttf"
        #             else:
        #                 text _p("{space=60}"+"{}".format(what)):
        #                     substitute False
        #                     font "fonts/MiSans-Regular.ttf"

        # if not _history_list:
        #     label _("The dialogue history is empty.")

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    # xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

# style history_label:
#     xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu():

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

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
        label _("Enter")
        text _("推进对话并激活界面。")

    hbox:
        label _("Space")
        text _("在不选择选项的情况下推进对话。")

    hbox:
        label _("Arrow Keys")
        text _("操作界面。")

    hbox:
        label _("Escape")
        text _("打开游戏菜单。")

    hbox:
        label _("Ctrl")
        text _("按住时跳过对话。")

    hbox:
        label _("Tab")
        text _("开关对话跳过。")

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
        text _("截取屏幕画面。")

    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")

    hbox:
        label "Shift+A"
        text _("打开辅助功能菜单。")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("推进对话并激活界面。")

    hbox:
        label _("Middle Click")
        text _("隐藏用户界面。")

    hbox:
        label _("Right Click")
        text _("打开游戏菜单。")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("回退到之前的对话。")

    hbox:
        label _("Mouse Wheel Down")
        text _("快进到之后的对话。")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("推进对话并激活界面。")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("回退到之前的对话。")

    hbox:
        label _("Right Shoulder")
        text _("快进到之后的对话。")


    hbox:
        label _("D-Pad, Sticks")
        text _("操作界面。")

    hbox:
        label _("Start, Guide")
        text _("打开游戏菜单。")

    hbox:
        label _("Y/Top Button")
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
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png" at transform:
        alpha .0
        easein_quint (.75 * persistent.ui_speed_multiplier) alpha .8

    frame background None:
        if message == gui.MAIN_MENU:
            xysize (1228, 255)
        elif message == gui.LOADING:
            xysize (928, 255)
        elif message == gui.FAST_SKIP_SEEN:
            xysize (728, 255)
        elif message == gui.FAST_SKIP_UNSEEN:
            xysize (928, 255)
        elif message == gui.UNKNOWN_TOKEN:
            xysize (1778, 255)
        elif message == gui.TRUST_TOKEN:
            xysize (1428, 255)
        else:
            xysize (628, 255)
        align  (.5 , .5 )
        at transform:
            yoffset  -512
            zoom    .0
            alpha   .0
            blur     25
            
            easein_quint (.75 * persistent.ui_speed_multiplier) yoffset 0 zoom 1.0 alpha 1.0 blur .0
        vbox:
            align    (.5, .0)
            xycenter (.5, .5)
            spacing    8
            frame background None:
                if message == gui.MAIN_MENU:
                    xysize (1228, 170)
                    image Frame("gui/msp1/confirm/message.png", 61, 61, 61, 61) xysize (889, 170) xycenter (.5, .5)
                elif message == gui.LOADING:
                    xysize (672, 170)
                    image Frame("gui/msp1/confirm/message.png", 61, 61, 61, 61) xysize (928, 170) xycenter (.5, .5)
                elif message == gui.FAST_SKIP_SEEN:
                    xysize (527, 170)
                    image Frame("gui/msp1/confirm/message.png", 61, 61, 61, 61) xysize (728, 170) xycenter (.5, .5)
                elif message == gui.FAST_SKIP_UNSEEN:
                    xysize (672, 170)
                    image Frame("gui/msp1/confirm/message.png", 61, 61, 61, 61) xysize (928, 170) xycenter (.5, .5)
                elif message == gui.UNKNOWN_TOKEN:
                    xysize (1284, 170)
                    image Frame("gui/msp1/confirm/message.png", 61, 61, 61, 61) xysize (1778, 170) xycenter (.5, .5)
                elif message == gui.TRUST_TOKEN:
                    xysize (1034, 170)
                    image Frame("gui/msp1/confirm/message.png", 61, 61, 61, 61) xysize (1428, 170) xycenter (.5, .5)
                else:
                    xysize (628, 170)
                    image "gui/msp1/confirm/message.png" xycenter (.5, .5)
                text message size 36 font "fonts/MiSans-Regular.ttf" text_align .5 xycenter (.5, .5) offset (0, -2)
            frame background None:
                xysize (628, 77)
                xycenter (.5, .5)
                hbox:
                    xycenter (.5, .5)
                    spacing 8
                    frame background None:
                        xysize (310, 77)
                        button:
                            xycenter (.5, .5)

                            # focus_mask True
                            
                            action yes_action

                            frame background None:
                                xysize (310, 77)
                                offset (0, -22)
                                image "gui/msp1/confirm/button.png" xycenter (.5, .5)
                                text "yes".upper() size 33 font "fonts/MiSans-Regular.ttf" text_align .5 xycenter (.5, .5) # offset (0, -2)

                            at transform:
                                on hover:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.5)
                                on idle:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                    frame background None:
                        xysize (310, 77)
                        button:
                            xycenter (.5, .5)

                            # focus_mask True
                            
                            action no_action

                            frame background None:
                                xysize (310, 77)
                                offset (0, -22)
                                image "gui/msp1/confirm/button.png" xycenter (.5, .5)
                                text "no".upper() size 33 font "fonts/MiSans-Regular.ttf" text_align .5 xycenter (.5, .5) offset (0, -2)

                            at transform:
                                on hover:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.5)
                                on idle:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
    # else:
    #     frame:

    #         vbox:
    #             xalign .5
    #             yalign .5
    #             spacing 45

    #             label _(message):
    #                 style "confirm_prompt"
    #                 xalign 0.5

    #             hbox:
    #                 xalign 0.5
    #                 spacing 150

    #                 textbutton _("Yes") action yes_action
    #                 textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("跳过中")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "fonts/MiSans-Regular.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("返回") action Rollback()
            textbutton _("跳过") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()
            textbutton _("隐藏界面") action HideInterface()


style window:
    variant "small"
    #background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

#TOP BAR

default persistent.date = True

screen TopGUI():
    zorder 98

    # ----- Left GUI

    if _in_replay and DateTime_Show == True:
        frame:
            padding(16, 8, 16, 8)
            background Frame('gui/top_gui.png', Borders(20, 20, 20, 20))
            alt ""
            text "回放" size 26 color ("#c0c0c0")        

    elif persistent.date and DateTime_Show == True:
        frame:
            padding(16, 8, 16, 8)
            background Frame('gui/top_gui.png', Borders(20, 20, 20, 20))
            alt ""
            text "第[Year]年 | [Month][Day]日 | [WeekDayOutput] | [TimeOutput]" size 26 color ("#c0c0c0")
