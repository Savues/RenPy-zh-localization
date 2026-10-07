screen scr_mm_soc(action, thumb, x, y):

    frame:
        
        align (.5, .5)
        xysize (x, y)

        button:

            align  (.5, .5)
            xysize (x, y)

            action action

            image thumb offset (-6, -6):
                at transform:

                    on idle:

                        easein_quint (.3 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)

                    on hover:

                        easein_quint (.3 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.125)

            at transform:

                subpixel  True

                xycenter (.5, .5)

                on hover:

                    easein_quint (.3 * persistent.ui_speed_multiplier) xzoom .95 yzoom .95

                on idle:

                    easein_quint (.3 * persistent.ui_speed_multiplier) xzoom 1.0 yzoom 1.0

screen scr_mm_btn(action, text, tooltip, thumb, kind, x, y, interval=0):

    frame:

        xysize (x, y)

        button:

            align  (.5, .5)
            xysize (x ,  y)

            focus_mask True
            
            action action
            
            image AlphaMask(thumb, 'gui/msp1/main_menu/Main_m.png' if kind == 'main' else 'gui/msp1/main_menu/Sub1_m.png') offset (-6, -6)
            image AlphaMask(im.Blur(thumb, 2), 'gui/msp1/main_menu/Main_m.png' if kind == 'main' else 'gui/msp1/main_menu/Sub1_m.png') offset (-6, -6):
                at transform:
                    on idle:
                        easein_quint (.5 * persistent.ui_speed_multiplier) alpha 0
                    on hover:
                        easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0

            text text.upper() font "fonts/MiSans-Regular.ttf" size 48 align (.0, 1.0) offset (25, -5) at button_text_enlarge()

            tooltip tooltip

            alt text + tooltip

        at button_cascade(interval*.05)

screen scr_nav_btn(action, text, interval=0):

    button:

        xysize (None, 50)
        align  (.5  , .5)

        action [ action, SetVariable('nav_active', True) ]

        alt text

        fixed:
            align (.5, .5)
            ymaximum 50
            xfit True
            yfit True

            frame:
                ymaximum 50
                background Frame('gui/msp1/nav/nav_btn.png', Borders(24, 24, 24, 24))
                padding (18, 24, 18, 24)

                text text.upper() font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) offset (0, -2) at transform:
                    alpha .0
                at transform:
                    on idle:
                        easein_quint (.5 * persistent.ui_speed_multiplier) alpha .0
                    on hover:
                        easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0

            frame:
                ymaximum 50
                padding (18, 24, 18, 24)

                text text.upper() font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) offset (0, -2)

        if not nav_active:
            
            at cascade_navigation(interval*.05)

screen scr_nav_btn_1(action, text, interval=0):

    button:

        xysize (None, 50)
        align  (.5  , .5)

        action [ action, SetVariable('nav_active', True) ]

        alt text

        fixed:
            align (.5, .5)
            ymaximum 50
            xfit True
            yfit True

            frame:
                ymaximum 50
                background Frame('gui/msp1/nav/nav_btn.png', Borders(24, 24, 24, 24))
                padding (18, 24, 18, 24)
                hbox:
                    align (.5, .5)
                    spacing 8
                    image "gui/msp1/nav/home.png" align (.5, .5)
                    text text.upper() font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) offset (0, -2) at transform:
                        alpha .0
                at transform:
                    on idle:
                        easein_quint (.5 * persistent.ui_speed_multiplier) alpha .0
                    on hover:
                        easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0

            frame:
                ymaximum 50
                padding (18, 24, 18, 24)
                hbox:
                    align (.5, .5)
                    spacing 8
                    image "gui/msp1/nav/home.png" align (.5, .5)
                    text text.upper() font "fonts/MiSans-Regular.ttf" xycenter (.5, .5) offset (0, -2)

        if not nav_active:
            
            at cascade_navigation(interval*.05)

screen scr_bios_draw(action, thumb, alt, interval=0):

    frame:

        xysize (267, 115)

        button:

            align (.5, .5)
            
            focus_mask True

            action action

            alt alt
            
            xysize (267, 115)

            image thumb align (.5, .5):

                at transform:

                    on idle:

                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#000", "#ffffff")

                    on hover:
        
                        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#ffb1df", "#ffffff")

            at bios_draw(interval*.05)


screen smp_btn(action, text):

    button:

        xysize (180, 64)

        action action

        at transform:

            on idle:
                easein_quart .5 matrixcolor BrightnessMatrix(.0) * ColorizeMatrix('#000', '#fff')
            on hover:
                easein_quart .5 matrixcolor BrightnessMatrix(.5) * ColorizeMatrix('#000', '#ffb1df')
            on selected_idle:
                easein_quart .5 matrixcolor BrightnessMatrix(.5) * ColorizeMatrix('#000', '#ffb1df')

        background Frame('gui/msp1/story_sel/day_btn.png', Borders(19, 15, 19, 23))

        padding (19, 15, 19, 23)

        text text size 24 font "fonts/MiSans-Regular.ttf" align (.5, .5)