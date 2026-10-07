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
    style_prefix "say"

    window:
        id "window"
        background Transform(Frame("gui/textbox.png",xalign=0.5, yalign=1.0), alpha=persistent.dialogueBoxOpacity)

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


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

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

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

    adjust_spacing False
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
    xalign 1.0
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "audio/pistoldraw1.ogg"
    #activate_sound "audio/heartbeat2.ogg"


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
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("快速保存") action QuickSave()
            textbutton _("快速读取") action QuickLoad()
            textbutton _("偏好设置") action ShowMenu('preferences')


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

            imagebutton auto ("gui/patreon_%s.png"):
                action OpenURL("https://www.patreon.com/lazybloodlines")
                at patreonbutton
                
            imagebutton auto ("gui/discord_%s.png"):
                action OpenURL("https://discord.gg/jG7Q2WFfTU")
                at discordbutton

            textbutton _("开始游戏") action Start()
            
            button:
                text _("画廊")
                action ShowMenu("replay_gallery")


        else:

            imagebutton auto ("gui/patreon_%s.png"):
                action OpenURL("https://www.patreon.com/lazybloodlines")
                at patreonbutton
                
            imagebutton auto ("gui/discord_%s.png"):
                action OpenURL("https://discord.gg/jG7Q2WFfTU")
                at discordbutton

            textbutton _("历史记录") action ShowMenu("history")

            textbutton _("保存") action ShowMenu("save")

        textbutton _("读取") action ShowMenu("load")

        textbutton _("偏好设置") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("主菜单") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("退出") action Quit(confirm=not main_menu)


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

transform patreonbutton:
    xalign 0.05
    yalign 0.05

transform discordbutton:
    xalign 0.05
    yalign 0.05

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"
    add "gui/gallery/main-menu-overlay.png"


    #add gui.main_menu_background
    # This ensures that any other menu screen is replaced.

    add Movie(size=(1920, 1080))
    on "show" action Play("movie", "gui/moviefinal.webm", loop=True)
    on "hide" action Stop("movie")
    on "replace" action Play("movie", "gui/moviefinal.webm", loop=True)
    on "replaced" action Stop("movie")


    #imagebutton auto "gui/patreon_%s.png" :
    #    action OpenURL("https://www.patreon.com/lazybloodlines")
    #    at patreonbutton

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


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


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


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
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\\n"

            text _("使用 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 制作。\\n\\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


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

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y年%m月%d日 %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


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
    text_align 0.5
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


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("偏好设置"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("快进")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选择之后") action Preference("after choices", "toggle")
                    textbutton _("转场特效") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.
                vbox: #add these 3 lines
                    label _("对话框不透明度")
                    bar value FieldValue(persistent, "dialogueBoxOpacity", range=1.0, style="slider")

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字显示速度")

                    bar value Preference("text speed")

                    label _("自动前进等待时间")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("音乐音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("音效音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("语音音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


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

    use game_menu(_("历史记录"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("对话记录为空。")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
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

style history_label:
    xfill True

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

    use game_menu(_("帮助"), scroll="viewport"):

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
        label _("回车")
        text _("推进对话并激活界面按钮。")

    hbox:
        label _("空格键")
        text _("推进对话，但不选择选项。")

    hbox:
        label _("方向键")
        text _("在界面中移动选择。")

    hbox:
        label _("Esc 键")
        text _("打开游戏菜单。")

    hbox:
        label _("Ctrl 键")
        text _("按住时快进对话。")

    hbox:
        label _("Tab 键")
        text _("切换对话快进。")

    hbox:
        label _("向上翻页")
        text _("回退到之前的对话。")

    hbox:
        label _("向下翻页")
        text _("前进到之后的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截取屏幕截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}朗读{/a}功能。")

    hbox:
        label "Shift+A"
        text _("打开无障碍菜单。")


screen mouse_help():

    hbox:
        label _("鼠标左键")
        text _("推进对话并激活界面按钮。")

    hbox:
        label _("鼠标中键")
        text _("隐藏用户界面。")

    hbox:
        label _("鼠标右键")
        text _("打开游戏菜单。")

    hbox:
        label _("滚轮上滑\\n点击回退侧")
        text _("回退到之前的对话。")

    hbox:
        label _("滚轮下滑")
        text _("前进到之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机\\nA／下方按钮")
        text _("推进对话并激活界面按钮。")

    hbox:
        label _("左扳机\\n左肩键")
        text _("回退到之前的对话。")

    hbox:
        label _("右肩键")
        text _("前进到之后的对话。")


    hbox:
        label _("十字键，摇杆")
        text _("在界面中移动选择。")

    hbox:
        label _("Start 键，Guide 键")
        text _("打开游戏菜单。")

    hbox:
        label _("Y／上方按钮")
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

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("是") action yes_action
                textbutton _("否") action no_action

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

            text _("快进中")

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
    font "DejaVuSans.ttf"


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

    #### ADD THIS TO MAKE THE PHONE WORK!! :) ###
    if nvl_mode == "phone":
        use PhoneDialogue(dialogue, items)
    else:
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
            ## config.narrator_menu is set to True.
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
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

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


#### CUSTOM MADE SCREENS

screen LIinfo():
    imagebutton auto "LIinfo/girlbio1_%s.png":
        focus_mask True
        hover_sound("audio/pistoldraw1.ogg")
        action [Play("soundlow", "audio/heartbeat2.ogg"), ShowMenu('LI_info')]
        
screen LI_info():
    modal True
    style_prefix "LIinfo/LI_select.png"
    
    add "LIinfo/LI_select.png"
    
    
    
    imagemap:
        ground "LIinfo/LI_select.png"
        idle "LIinfo/LI_select_2.png"
        hover "LIinfo/LI_select_3.png"
        
        #Return
        hotspot (1586, 801, 176, 175):
            action Return()
        
        #Next Page
        hotspot (1593, 552, 154, 190):
            action Return() #Show('LI_info_page2', transition=dissolve)
            text "{color=#f00}尚未实现。"
        
        
        #
        # Lila
        #(346, 5, 276, 486)
        hotspot (45, 6, 282, 490):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0),  Show('bio_LI', LI="lila", transition=dissolve)]
            #action [ Play("soundlow", audio.beat),
            #        SetVariable("current_look", renpy.random.randint(0, len(looks["annie"])-1)),
            #        Show('bios', girl="annie", transition=dissolve) ]
            
        #
        # Asuna
        #
        hotspot (346, 5, 276, 486):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_LI', LI="asuna", transition=dissolve)]
        #
        # Ashley
        #
        hotspot (640, 0, 291, 489):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_LI', LI="ash", transition=dissolve)]
            
        # Jasmin
        #
        hotspot (911, 0, 302, 492):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_LI', LI="jas", transition=dissolve)]
            
        # Julie
        #
        hotspot (1234, 3, 278, 490):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_LI', LI="ju", transition=dissolve)]
            
        # Lori
        #
        hotspot (1527, 4, 278, 489):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_LI', LI="lori", transition=dissolve)]
            
        # Isabella
        #
        hotspot (46, 515, 281, 451):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_LI', LI="isa", transition=dissolve)]
            
        # Sophia
        #
        hotspot (346, 519, 275, 446):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_LI', LI="sophia", transition=dissolve)]
            
        # Ava
        #
        hotspot (641, 519, 277, 448):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_LI', LI="ava", transition=dissolve)]
            
        # Grace
        #
        hotspot (937, 517, 276, 447):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_LI', LI="grace", transition=dissolve)]
            
        # Ingrid
        #
        hotspot (1235, 516, 275, 448):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_LI', LI="ingrid", transition=dissolve)]
            
            
screen bio_LI(LI):
    modal True
    style_prefix "LIinfo/bio_info.png"
    
    add "LIinfo/bio_info.png"


    
    #Love Interest Char image
    
    imagemap:
        ground "LIinfo/" + str(LI_bust_background[LI]) + str(biopage[LI]) + ".png"
        idle "LIinfo/" + str(LI_bust_background[LI]) + str(biopage[LI]) + ".png"
        hover "LIinfo/" + LI + "_bio2.png"
        
        #Return button
        hotspot (1718, 7, 191, 203):
            action Hide('bio_LI', transition=dissolve)
        #Change LI char
        hotspot (1542, 6, 171, 210):
            action Return()
     
    #Love Interest Char image
    #add "LIinfo/" + LI + "_char_bio" + 
    
    default ingrid_alive2 = getattr(store, "ingrid_alive")
    
    imagebutton:
        #idle "LIinfo/" + LI + "_char_bio" + str(busts[LI][current_bust]) + ".png"
        if ingrid_alive2 == False and LI == "ingrid":
            idle Transform("LIinfo/" + LI + "_char_bio" + str(current_bust_LI[LI][0]) + ".png", matrixcolor=SaturationMatrix(0.1))
        else:
            idle "LIinfo/" + LI + "_char_bio" + str(current_bust_LI[LI][0]) + ".png"
        if ingrid_alive2 == False and LI == "ingrid":
            hover Transform("LIinfo/" + LI + "_char_bio" + str(current_bust_LI[LI][0]) + ".png", matrixcolor=SaturationMatrix(0.1)*BrightnessMatrix(0.1))
        else:
            hover Transform("LIinfo/" + LI + "_char_bio" + str(current_bust_LI[LI][0]) + ".png", matrixcolor=BrightnessMatrix(0.1))
        focus_mask True
        action [Show("bust_choice", LI=LI, transition=dissolve)]
        
        
    #Setting the Corruption and Love Points
    default love_points = getattr(store, "love_" + LI)
    default corruption_points = getattr(store, "corruption_" + LI)


    #LOVE HEARTS HBOX
    hbox:
        pos (1315, 930)
        spacing 0

        #First
        if love_points > 0:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_love_heart_off.png"
        # Second heart
        if LI_love_hearts[LI].love_hearts2 != -1 and love_points >= LI_love_hearts[LI].love_hearts2:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_love_heart_off.png"
        # Second heart
        if LI_love_hearts[LI].love_hearts3 != -1 and love_points >= LI_love_hearts[LI].love_hearts3:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_love_heart_off.png"
        # Second heart
        if LI_love_hearts[LI].love_hearts4 != -1 and love_points >= LI_love_hearts[LI].love_hearts4:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_love_heart_off.png"
        # Second heart
        if LI_love_hearts[LI].love_hearts5 != -1 and love_points >= LI_love_hearts[LI].love_hearts5:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_love_heart_off.png"
        # Second heart
        if LI_love_hearts[LI].love_hearts6 != -1 and love_points >= LI_love_hearts[LI].love_hearts6:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_love_heart_off.png"
        # Second heart
        if LI_love_hearts[LI].love_hearts7 != -1 and love_points >= LI_love_hearts[LI].love_hearts7:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_love_heart_off.png"
        # Second heart
        if LI_love_hearts[LI].love_hearts8 != -1 and love_points >= LI_love_hearts[LI].love_hearts8:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_love_heart_off.png"
        # Second heart
        if LI_love_hearts[LI].love_hearts9 != -1 and love_points >= LI_love_hearts[LI].love_hearts9:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_love_heart_off.png"
        # Second heart
        if LI_love_hearts[LI].love_hearts10 != -1 and love_points >= LI_love_hearts[LI].love_hearts10:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_love_heart_off.png"
            
    #CORRUPTION HEARTS HBOX
    hbox:
        pos (1310, 980)
        spacing 0 

        #First
        if corruption_points >= 0:
            add "LIinfo/LI_corruption_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_off.png"
        # Second heart
        if LI_corruption_hearts[LI].corruption_hearts2 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts2:
            add "LIinfo/LI_corruption_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_off.png"
        # Second heart
        if LI_corruption_hearts[LI].corruption_hearts3 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts3:
            add "LIinfo/LI_corruption_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_off.png"
        # Second heart
        if LI_corruption_hearts[LI].corruption_hearts4 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts4:
            add "LIinfo/LI_corruption_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_off.png"
        # Second heart
        if LI_corruption_hearts[LI].corruption_hearts5 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts5:
            add "LIinfo/LI_corruption_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_off.png"
        # Second heart
        if LI_corruption_hearts[LI].corruption_hearts6 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts6:
            add "LIinfo/LI_corruption_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_off.png"
        # Second heart
        if LI_corruption_hearts[LI].corruption_hearts7 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts7:
            add "LIinfo/LI_corruption_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_off.png"
        # Second heart
        if LI_corruption_hearts[LI].corruption_hearts8 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts8:
            add "LIinfo/LI_corruption_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_off.png"
        # Second heart
        if LI_corruption_hearts[LI].corruption_hearts9 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts9:
            add "LIinfo/LI_corruption_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_off.png"
        # Second heart
        if LI_corruption_hearts[LI].corruption_hearts10 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts10:
            add "LIinfo/LI_corruption_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_off.png"
    key "game_menu" action Hide("bio_LI", transition=dissolve)


screen LI_info_page2():
    modal True
    style_prefix "LIinfo/LI_select.png"
    
    add "LIinfo/LI_select.png"
    
    imagemap:
        ground "LIinfo/LI_select.png"
        idle "LIinfo/LI_select_page2_2.png"
        hover "LIinfo/LI_select_page2_3.png"
        
        #Return
        hotspot (1586, 801, 176, 175):
            action Return()
        
        #Previous Page
        hotspot (1593, 552, 154, 190):
            action Hide("LI_info_page2", transition=dissolve)
        
        
        #
        # Lila
        #(346, 5, 276, 486)
        hotspot (45, 6, 282, 490):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0),  Show('bio_MC', MC="MC", transition=dissolve)]
        #
        # Asuna
        #
        hotspot (346, 5, 276, 486):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_factions', faction="wolfpack", transition=dissolve)]
        #
        # Ashley
        #
        hotspot (640, 0, 291, 489):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_factions', faction="russians", transition=dissolve)]
            
        # Jasmin
        #
        hotspot (911, 0, 302, 492):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_factions', faction="herd", transition=dissolve)]
            
        # Julie
        #
        hotspot (1234, 3, 278, 490):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_factions', faction="germans", transition=dissolve)]
            
        # Lori
        #
        hotspot (1527, 4, 278, 489):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_factions', faction="newcomers", transition=dissolve)]
            
        # Isabella
        #
        hotspot (46, 515, 281, 451):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_factions', faction="police", transition=dissolve)]
            
        # Sophia
        #
        hotspot (346, 519, 275, 446):
            action [ Play("soundlow", "audio/heartbeat2.ogg"), SetVariable("current_bust", 0), Show('bio_factions', faction="newcomers", transition=dissolve)]
            

screen bio_MC(MC):
    modal True
    style_prefix "LIinfo/bio_info.png"
    
    add "LIinfo/bio_info.png"


    
    #Love Interest Char image
    
    imagemap:
        ground "LIinfo/" + str(MC_bust_background[MC]) + ".png"
        idle "LIinfo/" + str(MC_bust_background[MC]) + ".png"
        hover "LIinfo/" + MC + "_bio2.png"
        
        #Return button
        hotspot (1718, 7, 191, 203):
            action Hide("bio_MC", transition=dissolve)
        #Change LI char
        hotspot (1542, 6, 171, 210):
            action Return()
            
    
    #Love Interest Char image
    add "LIinfo/" + MC + "_char_bio0.png"
        
    #imagebutton:
    #    idle "LIinfo/" + mc + "_char_bio" + str(busts[MC][current_bust]) + ".png"
    #    hover Transform("LIinfo/" + MC + "_char_bio" + str(busts[MC][current_bust]) + ".png", matrixcolor=BrightnessMatrix(0.1))
    #    focus_mask True
    #    action [Show("bust_choice", MC=MC, transition=dissolve)]
        
        
    #Setting the Money and Goodness Points
    default money_points = getattr(store, "cash")
    default goodness_points = getattr(store, "goodness")


    #GOODNESS BOX
    hbox:
        pos (1315, 930)
        spacing 0

        # First
        if goodness_points >= 0:
            add "LIinfo/LI_love_heart_on.png"
        else:
            add "LIinfo/LI_corruption_heart_on.png"
            
        # Second 
        if goodness_points >= 0:
            if goodness_points >= MC_goodness_points[MC].goodness_points2:
                add "LIinfo/LI_love_heart_on.png"
            else:
                add "LIinfo/LI_love_heart_off.png"
        else:
            if (-1*goodness_points) >= MC_goodness_points[MC].goodness_points2:
                add "LIinfo/LI_corruption_heart_on.png"
            else:
                add "LIinfo/LI_corruption_heart_off.png"
            
        # Third 
        if goodness_points >= 0:
            if goodness_points >= MC_goodness_points[MC].goodness_points3:
                add "LIinfo/LI_love_heart_on.png"
            else:
                add "LIinfo/LI_love_heart_off.png"
        else:
            if (-1*goodness_points) >= MC_goodness_points[MC].goodness_points3:
                add "LIinfo/LI_corruption_heart_on.png"
            else:
                add "LIinfo/LI_corruption_heart_off.png"
            
        # Fourth 
        if goodness_points >= 0:
            if goodness_points >= MC_goodness_points[MC].goodness_points4:
                add "LIinfo/LI_love_heart_on.png"
            else:
                add "LIinfo/LI_love_heart_off.png"
        else:
            if (-1*goodness_points) >= MC_goodness_points[MC].goodness_points4:
                add "LIinfo/LI_corruption_heart_on.png"
            else:
                add "LIinfo/LI_corruption_heart_off.png"
            
        # Fifth 
        if goodness_points >= 0:
            if goodness_points >= MC_goodness_points[MC].goodness_points5:
                add "LIinfo/LI_love_heart_on.png"
            else:
                add "LIinfo/LI_love_heart_off.png"
        else:
            if (-1*goodness_points) >= MC_goodness_points[MC].goodness_points5:
                add "LIinfo/LI_corruption_heart_on.png"
            else:
                add "LIinfo/LI_corruption_heart_off.png"
            
        # Sixth 
        if goodness_points >= 0:
            if goodness_points >= MC_goodness_points[MC].goodness_points6:
                add "LIinfo/LI_love_heart_on.png"
            else:
                add "LIinfo/LI_love_heart_off.png"
        else:
            if (-1*goodness_points) >= MC_goodness_points[MC].goodness_points6:
                add "LIinfo/LI_corruption_heart_on.png"
            else:
                add "LIinfo/LI_corruption_heart_off.png"
            
        # Seventh 
        if goodness_points >= 0:
            if goodness_points >= MC_goodness_points[MC].goodness_points7:
                add "LIinfo/LI_love_heart_on.png"
            else:
                add "LIinfo/LI_love_heart_off.png"
        else:
            if (-1*goodness_points) >= MC_goodness_points[MC].goodness_points7:
                add "LIinfo/LI_corruption_heart_on.png"
            else:
                add "LIinfo/LI_corruption_heart_off.png"
            
        # Eighth 
        if goodness_points >= 0:
            if goodness_points >= MC_goodness_points[MC].goodness_points8:
                add "LIinfo/LI_love_heart_on.png"
            else:
                add "LIinfo/LI_love_heart_off.png"
        else:
            if (-1*goodness_points) >= MC_goodness_points[MC].goodness_points8:
                add "LIinfo/LI_corruption_heart_on.png"
            else:
                add "LIinfo/LI_corruption_heart_off.png"
            
        # Nineth 
        if goodness_points >= 0:
            if goodness_points >= MC_goodness_points[MC].goodness_points9:
                add "LIinfo/LI_love_heart_on.png"
            else:
                add "LIinfo/LI_love_heart_off.png"
        else:
            if (-1*goodness_points) >= MC_goodness_points[MC].goodness_points9:
                add "LIinfo/LI_corruption_heart_on.png"
            else:
                add "LIinfo/LI_corruption_heart_off.png"
            
        # Tenth 
        if goodness_points >= 0:
            if goodness_points >= MC_goodness_points[MC].goodness_points10:
                add "LIinfo/LI_love_heart_on.png"
            else:
                add "LIinfo/LI_love_heart_off.png"
        else:
            if (-1*goodness_points) >= MC_goodness_points[MC].goodness_points10:
                add "LIinfo/LI_corruption_heart_on.png"
            else:
                add "LIinfo/LI_corruption_heart_off.png"

    #MONEY BOX
    hbox:
        pos (1315, 870)
        spacing 0

        # First
        if money_points >= 0:
            add "LIinfo/MC_money_on.png"
        else:
            add "LIinfo/MC_money_off.png"
            
        # Second 
        if money_points >= MC_money_points[MC].money_points2:
            add "LIinfo/MC_money_on.png"
        else:
            add "LIinfo/MC_money_off.png"
            
        # Third 
        if money_points >= MC_money_points[MC].money_points3:
            add "LIinfo/MC_money_on.png"
        else:
            add "LIinfo/MC_money_off.png"
            
        # Second 
        if money_points >= MC_money_points[MC].money_points4:
            add "LIinfo/MC_money_on.png"
        else:
            add "LIinfo/MC_money_off.png"
            
        # Second 
        if money_points >= MC_money_points[MC].money_points5:
            add "LIinfo/MC_money_on.png"
        else:
            add "LIinfo/MC_money_off.png"
            
        # Second 
        if money_points >= MC_money_points[MC].money_points6:
            add "LIinfo/MC_money_on.png"
        else:
            add "LIinfo/MC_money_off.png"
            
        # Second 
        if money_points >= MC_money_points[MC].money_points7:
            add "LIinfo/MC_money_on.png"
        else:
            add "LIinfo/MC_money_off.png"
            
        # Second 
        if money_points >= MC_money_points[MC].money_points8:
            add "LIinfo/MC_money_on.png"
        else:
            add "LIinfo/MC_money_off.png"
            
        # Second 
        if money_points >= MC_money_points[MC].money_points9:
            add "LIinfo/MC_money_on.png"
        else:
            add "LIinfo/MC_money_off.png"
            
        # Second 
        if money_points >= MC_money_points[MC].money_points10:
            add "LIinfo/MC_money_on.png"
        else:
            add "LIinfo/MC_money_off.png"
            
            
    key "game_menu" action Hide("bio_MC", transition=dissolve)
        
screen bio_factions(faction):
    modal True
    style_prefix "LIinfo/bio_info.png"
    
    add "LIinfo/bio_info.png"


    
    #Love Interest Char image
    
    imagemap:
        ground "LIinfo/" + str(factions_background[faction]) + ".png"
        idle "LIinfo/" + str(factions_background[faction]) + ".png"
        hover "LIinfo/" + faction + "_bio2.png"
        
        #Return button
        hotspot (1718, 7, 191, 203):
            action Hide("bio_factions", transition=dissolve)
        #Change LI char
        hotspot (1542, 6, 171, 210):
            action Return()
            
    
    #Faction Char image
    #add "LIinfo/" + faction + "_char_bio0.png"
        
    #imagebutton:
    #    idle "LIinfo/" + mc + "_char_bio" + str(busts[MC][current_bust]) + ".png"
    #    hover Transform("LIinfo/" + MC + "_char_bio" + str(busts[MC][current_bust]) + ".png", matrixcolor=BrightnessMatrix(0.1))
    #    focus_mask True
    #    action [Show("bust_choice", MC=MC, transition=dissolve)]
        
        
    #Setting the Money and Goodness Points
    default rep_points = getattr(store, faction)
    default power_points = getattr(store, faction + "_power")


    #REPUTATION BOX
    hbox:
        pos (1315, 690)
        spacing 0

        # First
        if rep_points >= 0:
            add "LIinfo/factions_rep_on.png"
        else:
            add "LIinfo/factions_rep_neg_on.png"
            
        # Second 
        if rep_points >= 0:
            if rep_points >= faction_rep_points[faction].faction_reputation2:
                add "LIinfo/factions_rep_on.png"
            else:
                add "LIinfo/factions_rep_off.png"
        else:
            if (-1*rep_points) >= faction_rep_points[faction].faction_reputation2:
                add "LIinfo/factions_rep_neg_on.png"
            else:
                add "LIinfo/factions_rep_neg_off.png"
            
        # Second 
        if rep_points >= 0:
            if rep_points >= faction_rep_points[faction].faction_reputation3:
                add "LIinfo/factions_rep_on.png"
            else:
                add "LIinfo/factions_rep_off.png"
        else:
            if (-1*rep_points) >= faction_rep_points[faction].faction_reputation3:
                add "LIinfo/factions_rep_neg_on.png"
            else:
                add "LIinfo/factions_rep_neg_off.png"
            
        # Second 
        if rep_points >= 0:
            if rep_points >= faction_rep_points[faction].faction_reputation4:
                add "LIinfo/factions_rep_on.png"
            else:
                add "LIinfo/factions_rep_off.png"
        else:
            if (-1*rep_points) >= faction_rep_points[faction].faction_reputation4:
                add "LIinfo/factions_rep_neg_on.png"
            else:
                add "LIinfo/factions_rep_neg_off.png"
            
        # Second 
        if rep_points >= 0:
            if rep_points >= faction_rep_points[faction].faction_reputation5:
                add "LIinfo/factions_rep_on.png"
            else:
                add "LIinfo/factions_rep_off.png"
        else:
            if (-1*rep_points) >= faction_rep_points[faction].faction_reputation5:
                add "LIinfo/factions_rep_neg_on.png"
            else:
                add "LIinfo/factions_rep_neg_off.png"
            
        # Second 
        if rep_points >= 0:
            if rep_points >= faction_rep_points[faction].faction_reputation6:
                add "LIinfo/factions_rep_on.png"
            else:
                add "LIinfo/factions_rep_off.png"
        else:
            if (-1*rep_points) >= faction_rep_points[faction].faction_reputation6:
                add "LIinfo/factions_rep_neg_on.png"
            else:
                add "LIinfo/factions_rep_neg_off.png"
            
        # Second 
        if rep_points >= 0:
            if rep_points >= faction_rep_points[faction].faction_reputation7:
                add "LIinfo/factions_rep_on.png"
            else:
                add "LIinfo/factions_rep_off.png"
        else:
            if (-1*rep_points) >= faction_rep_points[faction].faction_reputation7:
                add "LIinfo/factions_rep_neg_on.png"
            else:
                add "LIinfo/factions_rep_neg_off.png"
            
        # Second 
        if rep_points >= 0:
            if rep_points >= faction_rep_points[faction].faction_reputation8:
                add "LIinfo/factions_rep_on.png"
            else:
                add "LIinfo/factions_rep_off.png"
        else:
            if (-1*rep_points) >= faction_rep_points[faction].faction_reputation8:
                add "LIinfo/factions_rep_neg_on.png"
            else:
                add "LIinfo/factions_rep_neg_off.png"
            
        # Second 
        if rep_points >= 0:
            if rep_points >= faction_rep_points[faction].faction_reputation9:
                add "LIinfo/factions_rep_on.png"
            else:
                add "LIinfo/factions_rep_off.png"
        else:
            if (-1*rep_points) >= faction_rep_points[faction].faction_reputation9:
                add "LIinfo/factions_rep_neg_on.png"
            else:
                add "LIinfo/factions_rep_neg_off.png"
            
        # Second 
        if rep_points >= 0:
            if rep_points >= faction_rep_points[faction].faction_reputation10:
                add "LIinfo/factions_rep_on.png"
            else:
                add "LIinfo/factions_rep_off.png"
        else:
            if (-1*rep_points) >= faction_rep_points[faction].faction_reputation10:
                add "LIinfo/factions_rep_neg_on.png"
            else:
                add "LIinfo/factions_rep_neg_off.png"


    #POWER BOX
    hbox:
        pos (1315, 740)
        spacing 0

        # First
        if power_points >= 0:
            add "LIinfo/factions_power_on.png"
        else:
            add "LIinfo/factions_power_off.png"
            
        # Second 
        if power_points >= faction_power_points[faction].faction_power2:
            add "LIinfo/factions_power_on.png"
        else:
            add "LIinfo/factions_power_off.png"
            
        # Second 
        if power_points >= faction_power_points[faction].faction_power3:
            add "LIinfo/factions_power_on.png"
        else:
            add "LIinfo/factions_power_off.png"
            
        # Second 
        if power_points >= faction_power_points[faction].faction_power4:
            add "LIinfo/factions_power_on.png"
        else:
            add "LIinfo/factions_power_off.png"
            
        # Second 
        if power_points >= faction_power_points[faction].faction_power5:
            add "LIinfo/factions_power_on.png"
        else:
            add "LIinfo/factions_power_off.png"
            
        # Second 
        if power_points >= faction_power_points[faction].faction_power6:
            add "LIinfo/factions_power_on.png"
        else:
            add "LIinfo/factions_power_off.png"
            
        # Second 
        if power_points >= faction_power_points[faction].faction_power7:
            add "LIinfo/factions_power_on.png"
        else:
            add "LIinfo/factions_power_off.png"
            
        # Second 
        if power_points >= faction_power_points[faction].faction_power8:
            add "LIinfo/factions_power_on.png"
        else:
            add "LIinfo/factions_power_off.png"
            
        # Second 
        if power_points >= faction_power_points[faction].faction_power9:
            add "LIinfo/factions_power_on.png"
        else:
            add "LIinfo/factions_power_off.png"
            
        # Second 
        if power_points >= faction_power_points[faction].faction_power10:
            add "LIinfo/factions_power_on.png"
        else:
            add "LIinfo/factions_power_off.png"
#            
#        # Third 
#        if money_points >= MC_money_points[MC].money_points3:
#            add "LIinfo/MC_money_on.png"
#        else:
#            add "LIinfo/MC_money_off.png"
#            
#        # Second 
#        if money_points >= MC_money_points[MC].money_points4:
#            add "LIinfo/MC_money_on.png"
#        else:
#            add "LIinfo/MC_money_off.png"
#            
#        # Second 
#        if money_points >= MC_money_points[MC].money_points5:
#            add "LIinfo/MC_money_on.png"
#        else:
#            add "LIinfo/MC_money_off.png"
#            
#        # Second 
#        if money_points >= MC_money_points[MC].money_points6:
#            add "LIinfo/MC_money_on.png"
#        else:
#            add "LIinfo/MC_money_off.png"
#            
#        # Second 
#        if money_points >= MC_money_points[MC].money_points7:
#            add "LIinfo/MC_money_on.png"
#        else:
#            add "LIinfo/MC_money_off.png"
#            
#        # Second 
#        if money_points >= MC_money_points[MC].money_points8:
#            add "LIinfo/MC_money_on.png"
#        else:
#            add "LIinfo/MC_money_off.png"
#            
#        # Second 
#        if money_points >= MC_money_points[MC].money_points9:
#            add "LIinfo/MC_money_on.png"
#        else:
#            add "LIinfo/MC_money_off.png"
#            
#        # Second 
#        if money_points >= MC_money_points[MC].money_points10:
#            add "LIinfo/MC_money_on.png"
#        else:
#            add "LIinfo/MC_money_off.png"
        
#            
#    #CORRUPTION HEARTS HBOX
#    hbox:
#        pos (1310, 980)
#        spacing 0 
#
#        #First
#        if corruption_points >= 10:
#            add "LIinfo/LI_corruption_heart_on.png"
#        else:
#            add "LIinfo/LI_corruption_heart_off.png"
#        # Second heart
#        if LI_corruption_hearts[LI].corruption_hearts2 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts2:
#            add "LIinfo/LI_corruption_heart_on.png"
#        else:
#            add "LIinfo/LI_corruption_heart_off.png"
#        # Second heart
#        if LI_corruption_hearts[LI].corruption_hearts3 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts3:
#            add "LIinfo/LI_corruption_heart_on.png"
#        else:
#            add "LIinfo/LI_corruption_heart_off.png"
#        # Second heart
#        if LI_corruption_hearts[LI].corruption_hearts4 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts4:
#            add "LIinfo/LI_corruption_heart_on.png"
#        else:
#            add "LIinfo/LI_corruption_heart_off.png"
#        # Second heart
#        if LI_corruption_hearts[LI].corruption_hearts5 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts5:
#            add "LIinfo/LI_corruption_heart_on.png"
#        else:
#            add "LIinfo/LI_corruption_heart_off.png"
#        # Second heart
#        if LI_corruption_hearts[LI].corruption_hearts6 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts6:
#            add "LIinfo/LI_corruption_heart_on.png"
#        else:
#            add "LIinfo/LI_corruption_heart_off.png"
#        # Second heart
#        if LI_corruption_hearts[LI].corruption_hearts7 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts7:
#            add "LIinfo/LI_corruption_heart_on.png"
#        else:
#            add "LIinfo/LI_corruption_heart_off.png"
#        # Second heart
#        if LI_corruption_hearts[LI].corruption_hearts8 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts8:
#            add "LIinfo/LI_corruption_heart_on.png"
#        else:
#            add "LIinfo/LI_corruption_heart_off.png"
#        # Second heart
#        if LI_corruption_hearts[LI].corruption_hearts9 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts9:
#            add "LIinfo/LI_corruption_heart_on.png"
#        else:
#            add "LIinfo/LI_corruption_heart_off.png"
#        # Second heart
#        if LI_corruption_hearts[LI].corruption_hearts10 != -1 and corruption_points >= LI_corruption_hearts[LI].corruption_hearts10:
#            add "LIinfo/LI_corruption_heart_on.png"
#        else:
#            add "LIinfo/LI_corruption_heart_off.png"
    key "game_menu" action Hide("bio_factions", transition=dissolve)
    