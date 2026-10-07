#default preferences.afm_time = 15
default persistent.text_size = 33

screen preferences():

    tag menu

    on "show":
        action Show("prf_general")

    on "hide":
        action [ Hide("prf_general"), Hide("prf_appearance") ]

    use game_menu('options', scroll='frame'):

        frame background None:
            align  (1.0, .0 )
            xysize (307, 208)
            offset (6  , -6 )
            vbox:
                xycenter (.5, .5)
                spacing 8
                frame background None:
                    xysize   (307, 100)
                    xycenter (.5 , .5 )
                    button:

                        action [ Show("prf_general"), Hide("prf_appearance") ]

                        alt 'General'

                        frame background None:
                            xysize   (307, 100)
                            align    (.5 , .5 )
                            image "gui/msp1/options/general.png" align (.5, .5):
                                at transform:
                                    on idle:

                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                                    on hover:

                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.1)

                        xycenter (.5 , .5 )
                frame background None:
                    xysize   (307, 100)
                    xycenter (.5 , .5 )
                    button:

                        action [ Show("prf_appearance"), Hide("prf_general") ]

                        alt 'Appearance'

                        frame background None:
                            xysize   (307, 100)
                            align    (.5 , .5 )
                            image "gui/msp1/options/appearance.png" align (.5, .5):
                                at transform:
                                    on idle:

                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                                    on hover:

                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.1)

                        xycenter (.5 , .5 )

screen prf_general():

    default edit_mode = False

    frame id 'plate':
        background None
        xysize   (1920, 1080)
        xycenter (.5  , .5  )
        frame id 'content plate':
            background None
            xysize (1920, 1005)
            align  (.5  , 1.0 )
            offset (0   , 6   )
            frame id 'content':
                background None
                xysize   (1770, 855)
                xycenter (.5  , .5 )

                hbox:
                    # if active_page == "general":
                    #     at transform:
                    #         ease_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 zoom 1.0 yoffset 0 
                    # elif active_page == "appearance":
                    #     at transform:
                    #         ease_quint (.5 * persistent.ui_speed_multiplier) alpha .0 zoom .75 yoffset -512
                    # else:
                    #     at transform:
                    #         zoom .0 alpha .0
                    offset  (-6, -6)
                    spacing 8
                    vbox:
                        spacing 8
                        use scr_prf_sld('text speed', 'Determines how quickly text appears on the screen during dialogue and narration.', Preference("text speed"), Preference("text speed", 100), .05)
                        use scr_prf_sld('auto-forward speed', 'Adjusts the speed at which text automatically advances when using the auto-forward feature.', Preference("auto-forward time"), Preference("auto-forward time", 15), .1)
                        use scr_prf_sld('music volume', 'Adjusts the volume of the background music in the game.', Preference("music volume"), Preference("music volume", .1), .15)
                        use scr_prf_sld('sound volume', 'Controls the volume of sound effects, such as button clicks and environmental sounds.', Preference("sound volume"), Preference("sound volume", .1), .2)
                        use scr_prf_sld('ambiance volume', 'Sets the volume for ambient sounds, such as background noises and environmental audio.',  Preference("ambiance volume"), Preference("ambiance volume", .1), .25)
                        frame background None:
                            xysize (680, 40)
                            image "gui/msp1/options/mute_all.png" xycenter (.5, .5)
                            at cascade_options(.3)
                            textbutton "全部静音".upper() action Preference("all mute", "toggle") text_font "fonts/MiSans-Regular.ttf" text_align 1.0 align (1.0, .5) offset (-6, -2) text_size 20
                            
                    vbox:
                        spacing 8
                        frame background None:
                            xysize (576, 155)
                            image "gui/msp1/options/options_plate_2.png" xycenter (.5, .5)
                            at cascade_options(.35)
                            frame background None:  # label
                                xysize (None, 26)
                                offset (10  , 10)
                                align  (.0  , .0)
                                text "回滚区域".upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
                            frame background None:  # description
                                xysize (544, 39)
                                offset (0  , 94)
                                align  (.5 , .0)
                                text _p("设置点击或触摸屏幕的哪一侧可以触发回滚功能。") size 16 font "fonts/MiSans-Regular.ttf" text_align .0 align (.0 ,.0) offset (-6, -12)
                            frame background None:  # buttons
                                xysize (544, 26)
                                offset (0  , 52)
                                align  (.5 , .0)
                                hbox:
                                    offset (-6, -6)
                                    spacing 8
                                    use scr_prf_btn('normal', 'disable', Preference("rollback side", "disable"))
                                    use scr_prf_btn('normal', 'left', Preference("rollback side", "left"))
                                    use scr_prf_btn('normal', 'right', Preference("rollback side", "right"))

                        frame background None:
                            xysize (576, 155)
                            image "gui/msp1/options/options_plate_2.png" xycenter (.5, .5)
                            at cascade_options(.4)
                            frame background None:  # label
                                xysize (None, 26)
                                offset (10  , 10)
                                align  (.0  , .0)
                                text "skip".upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
                            frame background None:  # description
                                xysize (544, 39)
                                offset (0  , 94)
                                align  (.5 , .0)
                                text _p("设置跳过功能，用来快进已经读过的文本。") size 16 font "fonts/MiSans-Regular.ttf" text_align .0 align (.0 ,.0) offset (-6, -12)
                            frame background None:  # buttons
                                xysize (544, 26)
                                offset (0  , 52)
                                align  (.5 , .0)
                                hbox:
                                    offset (-6, -6)
                                    spacing 8
                                    use scr_prf_btn('normal', 'unseen text', Preference("skip", "toggle"))
                                    use scr_prf_btn('normal', 'after choices', Preference("after choices", "toggle"))
                                    use scr_prf_btn('normal', 'transitions', InvertSelected(Preference("transitions", "toggle")))

                        frame background None:
                            xysize (576, 155)
                            image "gui/msp1/options/options_plate_2.png" xycenter (.5, .5)
                            at cascade_options(.45)
                            frame background None:  # label
                                xysize (None, 26)
                                offset (10  , 10)
                                align  (.0  , .0)
                                text "日期与时间".upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
                            frame background None:  # description
                                xysize (544, 39)
                                offset (0  , 94)
                                align  (.5 , .0)
                                text _p("显示或隐藏位于屏幕左上角的日期与时间。") size 16 font "fonts/MiSans-Regular.ttf" text_align .0 align (.0 ,.0) offset (-6, -12)
                            frame background None:  # buttons
                                xysize (544, 26)
                                offset (0  , 52)
                                align  (.5 , .0)
                                hbox:
                                    offset (-6, -6)
                                    spacing 8
                                    use scr_prf_btn('wide', 'hide', SetField(persistent, 'date', False))
                                    use scr_prf_btn('wide', 'show', SetField(persistent, 'date', True))

                        if renpy.variant("pc"):
                            frame background None:
                                xysize (576, 155)
                                image "gui/msp1/options/options_plate_2.png" xycenter (.5, .5)
                                at cascade_options(.5)
                                frame background None:  # label
                                    xysize (None, 26)
                                    offset (10  , 10)
                                    align  (.0  , .0)
                                    text "display".upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
                                frame background None:  # description
                                    xysize (544, 39)
                                    offset (0  , 94)
                                    align  (.5 , .0)
                                    text _p("切换显示模式，在窗口与全屏之间选择。") size 16 font "fonts/MiSans-Regular.ttf" text_align .0 align (.0 ,.0) offset (-6, -12)
                                frame background None:  # buttons
                                    xysize (544, 26)
                                    offset (0  , 52)
                                    align  (.5 , .0)
                                    hbox:
                                        offset (-6, -6)
                                        spacing 8
                                        use scr_prf_btn('wide', 'fullscreen', Preference("display", "fullscreen"))
                                        use scr_prf_btn('wide', 'windowed', Preference("display", "window"))

                        if _in_replay:
                            frame background None:
                                xysize (576, 155)
                                image "gui/msp1/options/options_plate_2.png" xycenter (.5, .5)
                                at cascade_options(.5)
                                frame background None:  # label
                                    xysize (None, 26)
                                    offset (10  , 10)
                                    align  (.0  , .0)
                                    text "修改昵称".upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
                                frame background None:  # description
                                    xysize (544, 39)
                                    offset (0  , 94)
                                    align  (.5 , .0)
                                    text _p("修改昵称，打造专属体验。") size 16 font "fonts/MiSans-Regular.ttf" text_align .0 align (.0 ,.0) offset (-6, -12)
                                frame background None:  # buttons
                                    xysize (544, 26)
                                    offset (0  , 52)
                                    align  (.5 , .0)
                                    if not edit_mode:
                                        frame background None:

                                            xysize (544, 26)
                                            button:
                                                action SetScreenVariable('edit_mode', True)

                                                frame background None:
                                                    image Frame("gui/msp1/options/options_button.png", 5, 5, 5, 5) xysize (544, 26) xycenter (.5, .5):
                                                        at transform:
                                                            on hover:
                                                                easein_quint .5 matrixcolor BrightnessMatrix(1.0)
                                                            on idle:
                                                                easein_quint .5 matrixcolor BrightnessMatrix(.0)
                                                            on selected_hover:
                                                                ease 1.0 matrixcolor BrightnessMatrix(1.0)
                                                                ease 1.0 matrixcolor BrightnessMatrix(.5)
                                                                repeat
                                                            on selected_idle:
                                                                easein_quint .5 matrixcolor BrightnessMatrix(1.0)
                                                    text persistent.replay_PlayerName size 20 font "fonts/MiSans-Regular.ttf" align (.5 ,.5) offset (0, -1)

                                                    xysize (544, 26)
                                                    xycenter (.5 , .5)
                                                xysize (544, 26)
                                                xycenter (.5 , .5)

                                            xycenter (.5, .5)
                                    else:
                                        key 'dismiss' action SetScreenVariable('edit_mode', False)
                                        key 'input_enter' action SetScreenVariable('edit_mode', False)
                                        frame background None:
                                            image Frame("gui/msp1/options/options_button.png", 5, 5, 5, 5) xysize (544, 26) xycenter (.5, .5):
                                                at transform:
                                                    on hover:
                                                        easein_quint .5 matrixcolor BrightnessMatrix(1.0)
                                                    on idle:
                                                        easein_quint .5 matrixcolor BrightnessMatrix(.0)
                                                    on selected_hover:
                                                        ease 1.0 matrixcolor BrightnessMatrix(1.0)
                                                        ease 1.0 matrixcolor BrightnessMatrix(.5)
                                                        repeat
                                                    on selected_idle:
                                                        easein_quint .5 matrixcolor BrightnessMatrix(1.0)
                                            input value FieldInputValue(persistent, 'replay_PlayerName', returnable=True) size 20 color '#fff' font "fonts/MiSans-Regular.ttf" align (.5 ,.5) offset (0, -1)

                                            xysize (544, 26)
                                            xycenter (.5 , .5)
screen prf_appearance():

    frame id 'plate':
        background None
        xysize   (1920, 1080)
        xycenter (.5  , .5  )
        frame id 'content plate':
            background None
            xysize (1920, 1005)
            align  (.5  , 1.0 )
            offset (0   , 6   )
            frame id 'content':
                background None
                xysize   (1770, 855)
                xycenter (.5  , .5 )
                vbox:
                    xsize (1264)
                    offset  (-6, 0)
                    spacing 8
                    # if active_page == "general":
                    #     at transform:
                    #         ease_quint (.5 * persistent.ui_speed_multiplier) alpha .0 zoom .75 yoffset 512
                    # elif active_page == "appearance":
                    #     at transform:
                    #         ease_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 zoom 1.0 yoffset 0
                    # else:
                    #     at transform:
                    #         zoom .0 alpha .0
                    hbox:
                        offset  (0, -6)
                        spacing 8
                        vbox:
                            spacing 8

                            frame background None:
                                xysize (576, 408)
                                at cascade_options(.05)
                                image "gui/msp1/options/options_plate_3.png" xycenter (.5, .5)
                                frame background None:  # label
                                    xysize (None, 26)
                                    offset (10  , 10)
                                    align  (.0  , .0)
                                    text "对话框不透明度".upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
                                frame background None:  # preview
                                    xysize (544, 306)
                                    offset (0  , 80 )
                                    align  (.5 , .0 )
                                    image "gui/msp1/options/preview_bg.png" align (.5, .0) offset (0, -6)
                                    image "gui/msp1/options/preview.png" align (.5, 1.0) offset (0, 6) alpha persistent.dialogueBoxOpacity
                                    frame background None:  # preview text
                                        xysize (512, 74 )
                                        align  (.5 , .0 )
                                        offset (0  , 210)
                                        vbox:
                                            text "{color=#0059a7}杰克{/color}" size 26 font "fonts/MiSans-Regular.ttf" align (.0, .0) offset (8, -16) outlines [ (.5, "#161616", 1, 1.2) ]
                                            text _("这是用于测试的示例句子。") size 16 font "fonts/MiSans-Regular.ttf" align (.0, .0) offset (0, -16) outlines [ (.5, "#161616", 1, 1.2) ]

                                frame background None:  # default
                                    xysize (80 , 16)
                                    offset (-10, 10)
                                    align  (1.0, .0)
                                    textbutton "default".upper() action SetField(persistent, "dialogueBoxOpacity", 1.0) text_font "fonts/MiSans-Regular.ttf" text_size 20 align (1.0, .5) offset (12, -2)
                                bar value FieldValue(persistent, "dialogueBoxOpacity", range=1.0, style="slider") xysize (544, 12) align (.5, .0) offset (0, 52):
                                    thumb None
                                    left_bar  Frame("gui/msp1/options/bar_left.png", 6, 0, 6, 0)
                                    right_bar Frame("gui/msp1/options/bar_right.png", 6, 0, 6, 0)
                                    hover_left_bar  Transform(Frame("gui/msp1/options/bar_left.png", 6, 0, 6, 0), matrixcolor = BrightnessMatrix(.2))
                                    hover_right_bar Transform(Frame("gui/msp1/options/bar_right.png", 6, 0, 6, 0), matrixcolor = BrightnessMatrix(.2))

                            frame background None:
                                xysize (576, 200)
                                at cascade_options(.1)
                                image "gui/msp1/options/options_plate_4.png" xycenter (.5, .5)
                                default picker        = ColorPicker(432, 126, "#161616")
                                default picker_swatch = DynamicDisplayable(picker_color, picker=picker, xsize=64, ysize=64)
                                default picker_hex    = DynamicDisplayable(picker_hexcode, picker=picker)
                                frame background None:  # label
                                    xysize (None, 26)
                                    offset (10 , 10)
                                    align (.0, .0)
                                    text "边框颜色".upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
                                frame background None:  # set
                                    xysize (80, 16)
                                    offset (-90, 10)
                                    align (1.0, .0)
                                    $ hex_code = str(persistent.border_colour)[8:-1].upper()
                                    textbutton "default".upper() action SetField(persistent, "border_colour", "#161616") text_font "fonts/MiSans-Regular.ttf" text_size 20 align (1.0, .5) offset (6, -1) text_color '#fff' text_hover_color '#e066a3' text_insensitive_color '#8888887f'
                                frame background None:  # set
                                    xysize (80, 16)
                                    offset (-10, 10)
                                    align (1.0, .0)
                                    textbutton "set".upper() action [ SetField(persistent, "border_colour", picker.color) ] text_font "fonts/MiSans-Regular.ttf" text_size 20 align (1.0, .5) offset (13, -1) text_color '#fff' text_hover_color '#e066a3' text_insensitive_color '#8888887f'
                                frame background None:  # colour picker
                                    xysize (544, 126)
                                    offset (.0 , 52 )
                                    align  (.5 , .0 )

                                    hbox:
                                        xysize (544, 126)
                                        offset (8, 0)
                                        xycenter (.5, .5)
                                        spacing 16
                                        vbar value FieldValue(picker, "hue_rotation", 1.0) xysize (16, 126) base_bar At(Transform("#000", xysize=(16, 126)), spectrum(horizontal=False)) thumb "gui/msp1/options/thumb.png"

                                        add picker
                                        vbox:
                                            xsize 80 align (0.0, 0.0)

                                            add picker_swatch
                                            spacing 0

                                            text "R: [picker.color.rgb[0]:.2f]" size 16 font "fonts/MiSans-Regular.ttf"
                                            text "G: [picker.color.rgb[1]:.2f]" size 16 font "fonts/MiSans-Regular.ttf"
                                            text "B: [picker.color.rgb[2]:.2f]" size 16 font "fonts/MiSans-Regular.ttf"

                        vbox:
                            spacing 8
                            frame background None:
                                xysize (680, 200)
                                at cascade_options(.15)
                                image "gui/msp1/options/options_plate_5.png" xycenter (.5, .5)
                                frame background None:  # label
                                    xysize (None, 26)
                                    offset (10  , 10)
                                    align  (.0  , .0)
                                    text "界面速度倍率".upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
                                frame background None:  # description
                                    xysize (647, 67 )
                                    offset (0  , 111)
                                    align  (.5 , .0 )
                                    text _p("控制界面动画与转场的速度。调高可加快动画，调低则节奏更舒缓。") size 16 font "fonts/MiSans-Regular.ttf" text_align .0 align (.0 ,.0) offset (-6, -12)
                                frame background None:  # default
                                    xysize (80 , 16)
                                    offset (-10, 10)
                                    align  (1.0, .0)
                                    textbutton "default".upper() action [ SetField(persistent, "ui_speed_multiplier", 1.0), SetField(persistent, "temp_ui_speed_multiplier", .0) ] text_font "fonts/MiSans-Regular.ttf" text_size 20 align (1.0, .5) offset (12, -2)
                                frame background None:  # confirm
                                    xysize (80 , 16 )
                                    offset (-10, -10)
                                    align  (1.0, 1.0)
                                    textbutton "confirm".upper() action SetField(persistent, "ui_speed_multiplier", (1.0 - persistent.temp_ui_speed_multiplier)) text_font "fonts/MiSans-Regular.ttf" text_size 20 align (1.0, .5) offset (12, -2)
                                frame background None:  # preset
                                    xysize (647, 15)
                                    offset (0 , 82)
                                    align  (.5, .0)
                                    frame background None:
                                        align  (.0, .5)
                                        xysize (46, 15)
                                        textbutton "1x" action [ SetField(persistent, "temp_ui_speed_multiplier", .0) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (.5, .5) offset (0, -2)
                                    frame background None:
                                        align  (.25, .5)
                                        xysize (46 , 15)
                                        textbutton "1.33x" action [ SetField(persistent, "temp_ui_speed_multiplier", .25) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (.5, .5) offset (0, -2)
                                    frame background None:
                                        align  (.5, .5)
                                        xysize (46, 15)
                                        textbutton "2x" action [ SetField(persistent, "temp_ui_speed_multiplier", .5) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (.5, .5) offset (0, -2)
                                    frame background None:
                                        align  (.75, .5)
                                        xysize (46 , 15)
                                        textbutton "4x" action [ SetField(persistent, "temp_ui_speed_multiplier", .75) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (.5, .5) offset (0, -2)
                                    frame background None:
                                        align  (1.0, .5)
                                        xysize (46 , 15)
                                        textbutton "8x" action [ SetField(persistent, "temp_ui_speed_multiplier", 1.0) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (.5, .5) offset (0, -2)
                                bar value FieldValue(persistent, "temp_ui_speed_multiplier", min=.0, max=1.0, style="slider") xysize (648, 12) align (.5, .0) offset (0, 52):
                                    thumb None
                                    left_bar  Frame("gui/msp1/options/bar_left.png", 6, 0, 6, 0)
                                    right_bar Frame("gui/msp1/options/bar_right.png", 6, 0, 6, 0)
                                    hover_left_bar  Transform(Frame("gui/msp1/options/bar_left.png", 6, 0, 6, 0), matrixcolor = BrightnessMatrix(.2))
                                    hover_right_bar Transform(Frame("gui/msp1/options/bar_right.png", 6, 0, 6, 0), matrixcolor = BrightnessMatrix(.2))

                            frame background None:
                                xysize (680, 200)
                                at cascade_options(.2)
                                image "gui/msp1/options/options_plate_5.png" xycenter (.5, .5)
                                frame background None:  # label
                                    xysize (None, 26)
                                    offset (10  , 10)
                                    align  (.0  , .0)
                                    text "文字大小".upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
                                frame background None:  # description
                                    xysize (647, 67 )
                                    offset (0  , 111)
                                    align  (.5 , .0 )
                                    text _p("调整对话文字的大小。") size 16 font "fonts/MiSans-Regular.ttf" text_align .0 align (.0 ,.0) offset (-6, -12)
                                frame background None:  # default
                                    xysize (80 , 16)
                                    offset (-10, 10)
                                    align  (1.0, .0)
                                    textbutton "default".upper() action [ SetField(persistent, "text_size", 33) ] text_font "fonts/MiSans-Regular.ttf" text_size 20 align (1.0, .5) offset (12, -2)
                                frame background None:  # preset
                                    xysize (647, 15)
                                    offset (0 , 82)
                                    align  (.5, .0)
                                    frame background None:
                                        align  (.0, .5)
                                        xysize (46, 15)
                                        textbutton "small".upper() action [ SetField(persistent, "text_size", 20) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (.0, .5) offset (-15, -2)
                                    frame background None:
                                        align  (.5, .5)
                                        xysize (46, 15)
                                        textbutton "normal".upper() action [ SetField(persistent, "text_size", 33) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (.5, .5) offset (0, -2)
                                    frame background None:
                                        align  (1.0, .5)
                                        xysize (46 , 15)
                                        textbutton "large".upper() action [ SetField(persistent, "text_size", 53) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (1.0, .5) offset (15, -2)
                                bar value FieldValue(persistent, "text_size", min=1, max=100, style="slider") xysize (648, 12) align (.5, .0) offset (0, 52):
                                    thumb None
                                    left_bar  Frame("gui/msp1/options/bar_left.png", 6, 0, 6, 0)
                                    right_bar Frame("gui/msp1/options/bar_right.png", 6, 0, 6, 0)
                                    hover_left_bar  Transform(Frame("gui/msp1/options/bar_left.png", 6, 0, 6, 0), matrixcolor = BrightnessMatrix(.2))
                                    hover_right_bar Transform(Frame("gui/msp1/options/bar_right.png", 6, 0, 6, 0), matrixcolor = BrightnessMatrix(.2))

                            frame background None:
                                xysize (680, 200)
                                at cascade_options(.25)
                                image "gui/msp1/options/options_plate_5.png" xycenter (.5, .5)
                                frame background None:  # label
                                    xysize (None, 26)
                                    offset (10  , 10)
                                    align  (.0  , .0)
                                    text "边框粗细".upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
                                frame background None:  # description
                                    xysize (647, 67 )
                                    offset (0  , 111)
                                    align  (.5 , .0 )
                                    text _p("调整对话文字周围边框的粗细。") size 16 font "fonts/MiSans-Regular.ttf" text_align .0 align (.0 ,.0) offset (-6, -12)
                                frame background None:  # default
                                    xysize (80 , 16)
                                    offset (-10, 10)
                                    align  (1.0, .0)
                                    textbutton "default".upper() action [ SetField(persistent, "border_thickness", 3.0) ] text_font "fonts/MiSans-Regular.ttf" text_size 20 align (1.0, .5) offset (12, -2)
                                frame background None:  # preset
                                    xysize (647, 15)
                                    offset (0  , 82)
                                    align  (.5 , .0)
                                    frame background None:
                                        align  (.0, .5)
                                        xysize (46, 15)
                                        textbutton "hairline".upper() action [ SetField(persistent, "border_thickness", 1.0) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (.0, .5) offset (-15, -2)
                                    frame background None:
                                        align  (.5, .5)
                                        xysize (46, 15)
                                        textbutton "regular".upper() action [ SetField(persistent, "border_thickness", 3.0) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (.5, .5) offset (0, -2)
                                    frame background None:
                                        align  (1.0, .5)
                                        xysize (46 , 15)
                                        textbutton "thick".upper() action [ SetField(persistent, "border_thickness", 5.0) ] text_size 20 text_font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) align (1.0, .5) offset (15, -2)
                                bar value FieldValue(persistent, "border_thickness", min=1.0, max=5.0, style="slider") xysize (648, 12) align (.5, .0) offset (0, 52):
                                    thumb None
                                    left_bar  Frame("gui/msp1/options/bar_left.png", 6, 0, 6, 0)
                                    right_bar Frame("gui/msp1/options/bar_right.png", 6, 0, 6, 0)
                                    hover_left_bar  Transform(Frame("gui/msp1/options/bar_left.png", 6, 0, 6, 0), matrixcolor = BrightnessMatrix(.2))
                                    hover_right_bar Transform(Frame("gui/msp1/options/bar_right.png", 6, 0, 6, 0), matrixcolor = BrightnessMatrix(.2))

                    frame background None:
                        offset (0   , -6 )
                        xysize (1264, 231)
                        at cascade_options(.3)
                        image "gui/msp1/options/options_plate_6.png" xycenter (.5, .5)
                        frame background None:
                            xysize   (1232, 199)
                            xycenter (.5  , .5 )
                            vbox:
                                text "{color=#0059a7}杰克{/color}" size 45 font "fonts/MiSans-Regular.ttf" align (.0, .0) offset (8, -16) outlines [ (persistent.border_thickness, persistent.border_colour, 1, 1.2) ]
                                text _("敏捷的赤狐轻盈跃过沉睡的猎犬，灵活的松鼠则沿着高耸的橡树一路窜上树梢。") size persistent.text_size font "fonts/MiSans-Regular.ttf" align (.0, .0) offset (0, -16) outlines [ (persistent.border_thickness, persistent.border_colour, 1, 1.2) ]


screen scr_prf_btn(type, label, action):
    frame background None:
        if type == 'normal':
            xysize   (176, 26)
        elif type == 'wide':
            xysize (267, 26)
        button:

            action action

            frame background None:
                if type == 'normal':
                    image "gui/msp1/options/options_button.png" xycenter (.5, .5):
                        at transform:
                            on hover:
                                easein_quint .5 matrixcolor BrightnessMatrix(1.0)
                            on idle:
                                easein_quint .5 matrixcolor BrightnessMatrix(.0)
                            on selected_hover:
                                ease 1.0 matrixcolor BrightnessMatrix(1.0)
                                ease 1.0 matrixcolor BrightnessMatrix(.5)
                                repeat
                            on selected_idle:
                                easein_quint .5 matrixcolor BrightnessMatrix(1.0)
                elif type == 'wide':
                    image Frame("gui/msp1/options/options_button.png", 5, 5, 5, 5) xysize (267, 26) xycenter (.5, .5):
                        at transform:
                            on hover:
                                easein_quint .5 matrixcolor BrightnessMatrix(1.0)
                            on idle:
                                easein_quint .5 matrixcolor BrightnessMatrix(.0)
                            on selected_hover:
                                ease 1.0 matrixcolor BrightnessMatrix(1.0)
                                ease 1.0 matrixcolor BrightnessMatrix(.5)
                                repeat
                            on selected_idle:
                                easein_quint .5 matrixcolor BrightnessMatrix(1.0)
                text  label.upper() size 20 font "fonts/MiSans-Regular.ttf" align (.5 ,.5) offset (0, -1)
                if type == 'normal':
                    xysize   (176, 26)
                elif type == 'wide':
                    xysize (267, 26)
                xycenter (.5 , .5)

            xycenter (.5, .5)

screen scr_prf_sld(label, description, value, default, delay):

    frame background None:
        xysize (680, 155)
        image "gui/msp1/options/options_plate_1.png" xycenter (.5, .5)
        at cascade_options(delay)
        frame background None:  # label
            xysize (None, 26)
            offset (10  , 10)
            align  (.0  , .0)
            text label.upper() font "fonts/MiSans-Regular.ttf" size 35 align (.0, .5) offset (-6, -2)
        frame background None:  # description
            xysize (648, 53)
            offset (0  , 80)
            align  (.5 , .0)
            text _p(description) size 16 font "fonts/MiSans-Regular.ttf" text_align .0 align (.0 ,.0) offset (-6, -12)
        frame background None:  # default
            xysize (80 , 16)
            offset (-10, 10)
            align  (1.0, .0)
            textbutton "default".upper() action default text_font "fonts/MiSans-Regular.ttf" text_size 20 align (1.0, .5) offset (12, -2)
        bar value value xysize (648, 12) align (.5, .0) offset (0, 52):
            thumb None
            left_bar  "gui/msp1/options/bar_left.png"
            right_bar "gui/msp1/options/bar_right.png"
            hover_left_bar  Transform("gui/msp1/options/bar_left.png", matrixcolor = BrightnessMatrix(.2))
            hover_right_bar Transform("gui/msp1/options/bar_right.png", matrixcolor = BrightnessMatrix(.2))