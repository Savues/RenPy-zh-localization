init offset = -1

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/menus/confirm.png"

    if message == "Are you sure you want to quit?":

        frame:
            background Frame("gui/frame4.webp", 10, 10)

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 45

                label _(confirm_zh(message)):
                    style "confirm_prompt"
                    xoffset 12

                hbox:
                    xoffset -16
                    xalign 0.5
                    spacing 150

                    frame:
                        style "empty"
                        xysize (250, 100)
                        button:
                            xysize (200, 60)
                            background "gui/frame5.webp"
                            text "是": 
                                align (0.5, 0.5)
                                outlines [(2, "#000000", 0, 0)]
                                selected_outlines [(2, "#000000ff", 0, 0)]
                                hover_outlines [(2, persistent.theme_color, 0, 0)]
                            action yes_action
                            at center_hover
                        
                    frame:
                        style "empty"
                        xysize (250, 100)
                        button:
                            xysize (200, 60)
                            background "gui/frame6.webp"
                            text "否":
                                align (0.5, 0.5)
                                outlines [(2, "#000000", 0, 0)]
                                selected_outlines [(2, "#000000ff", 0, 0)]
                                hover_outlines [(2, persistent.theme_color, 0, 0)]
                            action no_action
                            at center_hover

    else:
        frame:
            background Frame("gui/frame4.webp", 10, 10)

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 45

                label _(confirm_zh(message)):
                    style "confirm_prompt"
                    xoffset 12

                hbox:
                    xoffset -16
                    xalign 0.5
                    spacing 150

                    frame:
                        style "empty"
                        xysize (250, 100)
                        button:
                            xysize (200, 60)
                            background "gui/frame5.webp"
                            text "是": 
                                align (0.5, 0.5)
                                outlines [(2, "#000000", 0, 0)]
                                selected_outlines [(2, "#000000ff", 0, 0)]
                                hover_outlines [(2, persistent.theme_color, 0, 0)]
                            action yes_action
                            at center_hover
                        
                    frame:
                        style "empty"
                        xysize (250, 100)
                        button:
                            xysize (200, 60)
                            background "gui/frame6.webp"
                            text "否":
                                align (0.5, 0.5)
                                outlines [(2, "#000000", 0, 0)]
                                selected_outlines [(2, "#000000ff", 0, 0)]
                                hover_outlines [(2, persistent.theme_color, 0, 0)]
                            action no_action
                            at center_hover

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
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")