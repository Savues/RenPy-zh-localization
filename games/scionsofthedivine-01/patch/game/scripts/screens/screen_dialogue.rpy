init offset = -1

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        background Transform(style.window.background, alpha=persistent.textbox_opacity)

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who":
                    if persistent.outlinesize > 1:
                        outlines [(1 + persistent.outlinesize, "#000000", 0, 0)]
                    else:
                        outlines [(persistent.outlinesize, "#000000", 0, 0)]

        text what id "what":
            size persistent.text_size
            outlines [(persistent.outlinesize, "#000000", 0, 0)]


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


screen center_say(who, what):
    style_prefix "center_say"
    text what id "what":
        outlines [(persistent.outlinesize, "#000000", 0, 0)]
        xalign 0.5
        yalign 0.5
        text_align 0.5
        font zh_display_font
        size 52