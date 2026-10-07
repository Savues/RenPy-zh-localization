init offset = -1

default outf_hovered = False

screen outfit_picker(chara_id):
    style_prefix "outfit_picker"
    zorder 102
    modal True
    add Solid("#0000009f")

    if chara_id in chara and "Outfits" in chara[chara_id].tags:
        $ character = chara[chara_id]
        $ total_outfits = character.get_total_outfits()
        
        vpgrid:
            align (0.5, 0.5)
            cols 5
            spacing 20
            draggable True
            mousewheel True
            ymaximum 1012
            scrollbars "vertical"
            side_spacing 20

            for i in range(0, total_outfits):
                vbox:
                    imagebutton:
                        if character.is_outfit_unlocked(i):
                            idle Transform(
                                f"{chara_id}_outf{i}",
                                crop=(450, 43, 1020, 1020),
                                zoom=0.3
                            )
                            hover Fixed(
                                At(Transform(
                                    f"{chara_id}_outf{i}",
                                    matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(1.0),
                                    additive=1.0,
                                    blur=5.0,
                                    alpha=1.0,
                                    crop=(450, 43, 1020, 1020),
                                    zoom=0.3
                                ), Position(xoffset=-3, yoffset=0)),
                                Transform(
                                    f"{chara_id}_outf{i}",
                                    crop=(450, 43, 1020, 1020),
                                    zoom=0.3
                                ),
                                fit_first=True,
                                xalign=0.5,
                                yalign=0.5
                            )
                            selected False
                            action [ 
                                SetField(character, "selected_outfit", i),
                                SetDict(persistent.outfit_selections, chara_id, i),
                                Hide("outfit_picker", transition=dissolve) 
                            ]
                        else:
                            idle Fixed(
                                At(Transform(
                                    f"{chara_id}_outf{i}",
                                    matrixcolor=TintMatrix("#ffffff") * BrightnessMatrix(1.0),
                                    additive=1.0,
                                    blur=0.0,
                                    alpha=1.0,
                                    crop=(450, 43, 1020, 1020),
                                    zoom=0.3
                                ), Position(xoffset=0, yoffset=0)),
                                Transform(
                                    f"{chara_id}_outf{i}",
                                    matrixcolor=TintMatrix("#000000") * BrightnessMatrix(1.0),
                                    crop=(450, 43, 1020, 1020),
                                    zoom=0.3
                                ),
                                fit_first=True,
                                xalign=0.5,
                                yalign=0.5
                            )
                    if not character.is_outfit_unlocked(i):
                        text "暂无数据"

    key "game_menu" action Hide("outfit_picker", transition=dissolve)

    textbutton _("返回"):
        style "outf_return_button"
        action Hide("outfit_picker", transition=dissolve)


style outf_return_button is gui_button
style outf_return_button_text is gui_button_text

style outfit_picker_vscrollbar is vscrollbar:
    unscrollable "hide"

style outfit_picker_text:
    properties gui.text_properties("slot_button")
    xalign 0.5
    ypos -162

style outf_return_button:
    properties gui.button_properties("navigation_button")
    xalign 0.05
    yalign 0.95

style outf_return_button_text:
    properties gui.text_properties("navigation_button")
    bold True