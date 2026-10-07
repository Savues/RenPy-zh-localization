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

    frame:
        background "gui/msp1/main_menu/plate.png"
        xysize (96 , 242)
        align  (1.0,  .0)
        offset (-94,  96)
        vbox:
            xysize (66, 214)
            align  (.5, .5)
            spacing 9

            use scr_mm_soc(OpenURL("https://www.patreon.com/cosycreator?utm_source=in-game&utm_medium=about-button"), 'gui/msp1/main_menu/patreon.png', 66, 64)
            use scr_mm_soc(OpenURL("https://subscribestar.adult/cosy-creator")                                      , 'gui/msp1/main_menu/substar.png', 66, 66)
            use scr_mm_soc(OpenURL("https://discord.gg/U9CwvDf2vV")                                                 , 'gui/msp1/main_menu/discord.png', 60, 66)

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
                use scr_mm_btn(Start()                                                                 , "开始游戏"  , '开始故事。'                , "gui/msp1/main_menu/main.png"   , 'main', 407, 250, 1)
                use scr_mm_btn(ShowMenu('load')                                                        , "读取存档"   , '读取已保存的存档。'              , "gui/msp1/main_menu/load.png"   , 'sub' , 407, 124, 2)
                use scr_mm_btn(Show("gallery_pre")                                                     , "画廊", '查看插画与场景。'        , "gui/msp1/main_menu/gallery.png", 'sub' , 407, 124, 3)
                use scr_mm_btn([ ShowMenu('bios'), Function(refresh_character_stats) ]                 , "角色档案"   , '阅读角色档案。'        , "gui/msp1/main_menu/bios.png"   , 'sub' , 407, 124, 4)
                use scr_mm_btn([ ShowMenu('preferences'), Show('prf_general'), Hide('prf_appearance') ], "选项", '修改设置与偏好。', "gui/msp1/main_menu/prefs.png"  , 'sub' , 407, 124, 5)

            hbox:

                spacing 8

                frame:

                    xysize (200, 30)

                    button:

                        align  (.5 , .5)
                        xysize (200, 30)

                        focus_mask True
                        action ShowMenu('about')

                        image "gui/msp1/main_menu/about.png" align (.5, .5):
                            at transform:
                                on idle:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#000", "#fff")
                                on hover:
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#ffb1df", "#ffffff")


                        tooltip "了解游戏与制作人员。"
                        alt "了解游戏与制作人员。"

                    at fade_in(.0)

                if renpy.variant('pc'):

                    frame:

                        xysize (200, 30)

                        button:

                            xysize (200, 30)
                            align  (.5 , .5)

                            focus_mask True

                            action Quit(confirm=True)

                            image "gui/msp1/main_menu/quit.png" align (.5, .5):
                                at transform:
                                    on idle:
                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#000", "#fff")
                                    on hover:
                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#ffb1df", "#ffffff")

                            tooltip "退出游戏。"
                            alt "退出游戏。"

                        at fade_in(.0)

                else:

                    null width 200 height 30