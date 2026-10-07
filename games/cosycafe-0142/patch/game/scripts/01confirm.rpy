screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png" at transform:
        alpha .0
        easein_quint (.75 * persistent.ui_speed_multiplier) alpha .8

    frame:
        background Frame(Transform("gui/msp1/confirm/message.png", matrixcolor = BrightnessMatrix(-.05)), 61, 61, 61, 61)
        padding (128, 48, 128, 48)
        align   (.5     ,      .5)

        at transform:

            subpixel True
            alpha   .0
            
            easein_quint (.75 * persistent.ui_speed_multiplier) alpha 1.0

        vbox:
            align (.5 ,.5)
            spacing 48
            text message size 36 font "fonts/MiSans-Regular.ttf" text_align .5 xycenter (.5, .5) offset (0, -2)

            hbox:
                align (.5, .5)
                spacing 24
                frame background None:

                    xysize (120, 50)
                    button:

                        align (.5, .5)
                        xysize (120, 50)

                        action yes_action

                        background Frame("gui/msp1/confirm/button.png", Borders(16, 16, 16, 16))
                        text "确认".upper() size 24 font "fonts/MiSans-Regular.ttf" text_align .5 align (.5, .5)

                        at transform:

                            matrixcolor ColorizeMatrix('#000', '#fff')

                            on idle:
                                easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor InvertMatrix(.0)
                            on hover:
                                easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor InvertMatrix(1.0)

                frame background None:

                    xysize (120, 50)

                    button:

                        align (.5, .5)
                        xysize (120, 50)

                        action no_action

                        background Frame("gui/msp1/confirm/button.png", Borders(16, 16, 16, 16))
                        text "取消".upper() size 24 font "fonts/MiSans-Regular.ttf" text_align .5 align (.5, .5)

                        at transform:

                            matrixcolor ColorizeMatrix('#000', '#fff')

                            on idle:
                                easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor InvertMatrix(.0)
                            on hover:
                                easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor InvertMatrix(1.0)