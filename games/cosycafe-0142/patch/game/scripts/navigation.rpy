init -10:
    $ nav_active         = False
    $ nav_active_screen  = None

screen game_menu(title=None, scroll=None, yinitial=0.0):

    if main_menu:
        add "gui/msp1/main_menu/bg.png" zoom .5

    add "gui/msp1/nav/nav_bg.png":
        at transform:
            alpha .0
            blur   5

            easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 blur 0
    
    style_prefix 'nav_new'

    frame id 'plate':
        background None
        xysize   (1920, 1080)
        xycenter (.5  , .5  )
        frame id 'navigation':
            background None
            image "gui/msp1/nav/nav_main.png" offset (-6, -6)
            xysize (1920, 75)
            align  (.5  , .0)
            offset (0   , -6)
            if not nav_active:
                at transform:
                    alpha   .0
                    yoffset -250
                    blur     5
                    easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 yoffset 0 blur .0
            frame id 'coffee':
                background None
                image "gui/msp1/nav/coffee.png" xycenter (.5, .5)
                xysize (75, 75)
                align  (.0, .5)
                offset (-6, 0 )
            frame id 'nav':
                background None
                xysize (960 , 75)
                offset (69  , 0 )
                align  (None, .5)
                hbox:
                    spacing 8
                    offset  (8  , 0 )
                    align   (.0 , .5)
                    if not main_menu:
                        use scr_nav_btn([ShowMenu('save'), Hide("prf_general"), Hide("prf_appearance")], 'save', 0)
                    use scr_nav_btn([ShowMenu('load'), Hide("prf_general"), Hide("prf_appearance")], "load", 1)
                    if not main_menu:
                        use scr_nav_btn([ShowMenu('history'), Hide("prf_general"), Hide("prf_appearance")], "history", 2)
                    use scr_nav_btn([ShowMenu('preferences'), Show('prf_general'), Hide('prf_appearance')], "options", 3)
                    if not main_menu:
                        use scr_nav_btn([ShowMenu('bios'), Hide("prf_general"), Hide("prf_appearance"), Function(refresh_character_stats)], "bios", 4)
                        use scr_nav_btn([ShowMenu('gallery_pre'), Hide("prf_general"), Hide("prf_appearance")], "gallery", 5)

            frame id 'nav right':
                background None
                xysize (544 , 75)
                offset (-69 , 0 )
                align  (1.0 , .5)
                hbox:
                    align  (1.0, .5)
                    spacing 30
                    if not main_menu and not _in_replay:
                        use scr_nav_btn_1(MainMenu(confirm=True), 'main menu', 6)
                    elif _in_replay:
                        use scr_nav_btn_1(EndReplay(confirm=True), 'end replay', 6)
                    frame id 'socials':
                        background None
                        xysize (225, 50)
                        offset (6  , 0 )
                        button:

                            xysize (225, 50)
                            align  (.5, .5)

                            action [ ShowMenu('socials'), SetVariable('nav_active', True), Hide("prf_general"), Hide("prf_appearance") ]

                            image "gui/msp1/nav/socials.png" align (.5, .5):
                                at transform:

                                    on idle:

                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#000', '#fff')

                                    on hover:

                                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#ffb1df', '#fff')

                            if not nav_active:
                                at cascade_navigation(.35)
        frame id 'content plate':
            background None
            xysize (1920, 1005)
            align  (.5  , 1.0 )
            offset (0   , 6   )
            if not nav_active:
                at transform:
                    alpha  .0
                    blur    5
                    easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 blur 0
            frame id 'content nav':
                background None
                xysize   (885 , 59 )
                offset   (69  , 4  )
            frame id 'content title':
                background None
                xysize   (444 , 59 )
                align    (1.0 , 0  )
                offset   (-69 , 4  )
                # image Transform(Frame('gui/msp1/nav/nav_title.svg', 11, 11, 11, 11), matrixcolor = ColorizeMatrix("#fff", "#000")) xycenter (.5, .5) xysize (444 , 59 )
                padding (8, 8, 8, 8)
                if title:
                    text title.upper() align (1.0, .5) offset (0, -3) font "fonts/MiSans-Regular.ttf" size 60:
                        at transform:
                            alpha .0
                            zoom  .0
                            xoffset 250
                            easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 zoom 1.0 xoffset 0
            frame id 'content':
                background None
                xysize   (1770, 855)
                xycenter (.5  , .5 )
                at transform:
                    zoom .0
                    alpha  .0
                    blur    5
                    yoffset 500
                    easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 blur 0 yoffset 0 zoom 1.0
                if scroll == "viewport":
                    
                    padding (8, 8, 8, 8)
                    viewport id 'nav viewport':
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                    vbar value YScrollValue ('nav viewport') xalign 1.0 xysize (8, 774)

                elif scroll == "vpgrid":

                    padding (8, 8, 8, 8)
                    vpgrid id 'nav vpgrid':
                        cols 1
                        yinitial yinitial
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude
                    
                    vbar value YScrollValue ('nav vpgrid') xalign 1.0 xysize (8, 774)

                elif scroll == "frame":
                    
                    transclude

                else:

                    padding (8, 8, 8, 8)
                    viewport:
                        mousewheel True
                        draggable True
                        pagekeys True
                        transclude

            frame background None: # ABSOLUTE
                xysize (95 , 57 )
                align  (1.0, 1.0)
                if nav_active_screen == "preferences":
                    offset (-69, -69)
                else:
                    offset (-75, -75)
                button:

                    xysize (95, 57)
                    align  (.5, .5)
                    
                    focus_mask True

                    if main_menu:
                        action [ SetVariable('nav_active_screen', None), ShowMenu("main_menu"), SetVariable('nav_active', False), Hide("prf_general"), Hide("prf_appearance") ]
                    else:
                        action [ SetVariable('nav_active_screen', None), Return(), SetVariable('nav_active', False), Hide("prf_general"), Hide("prf_appearance") ]

                    image "gui/msp1/nav/return_nav.png" align (.5, .5) alpha .5:
                        at transform:

                            on idle:

                                easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#000', '#fff')

                            on hover:

                                easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#ffb1df', '#fff')

                    if not nav_active:
                        at transform:
                            zoom .0
                            alpha .0
                            easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 zoom 1.0

    if main_menu:
        key "game_menu" action [ SetVariable('nav_active_screen', None), ShowMenu("main_menu"), SetVariable('nav_active', False), Hide("prf_general"), Hide("prf_appearance") ]
    else:
        key "game_menu" action [ SetVariable('nav_active_screen', None), Return(), SetVariable('nav_active', False), Hide("prf_general"), Hide("prf_appearance") ]

style nav_new_text:
    size 33
style nav_new_text:
    variant 'mobile'
    size 33