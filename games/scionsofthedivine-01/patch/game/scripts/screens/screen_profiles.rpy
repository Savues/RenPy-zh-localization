init offset = -1

screen profile(chara_id):
    zorder 101
    style_prefix "profiles"
    $ profile = chara[chara_id]

    vbox:

        label profile.name:
            text_color profile.color
            at bio_transform
        
        frame:
            at bio_transform2
            background Frame("gui/frame2.webp", 10, 10)
            ypos 40
            xsize 450
                
            vbox:
                xpos 28
                style_prefix "bio1"

                hbox:
                    text "年龄："
                    text "[profile.get_bio_info('age')]" bold False
                hbox:
                    text "身高："
                    text "[profile.get_bio_info('height')]" bold False
                hbox:
                    text "体重："
                    text "[profile.get_bio_info('weight')]" bold False

        frame:
            at bio_transform3
            background Frame("gui/frame2.webp", 10, 10)
            ypos 36
            xsize 450

            hbox:

                side "c l":

                    viewport id "bio_vp":
                        xysize (410, 300)
                        xpos 10
                        mousewheel True
                        draggable True
                        pagekeys True
                        yinitial 0.0
                        style_prefix "bio2"

                        vbox:
                            spacing 10
                            xalign 0.0
                            $ visible_bios = profile.get_visible_bios()
                            if visible_bios:
                                for description in visible_bios:
                                    text description
                            else:
                                text "暂无数据"

                    vbar value YScrollValue("bio_vp") unscrollable "hide"
        
        if chara_id in chara and "Romanceable" in profile.tags and not mm_var:

            vbox:
                at bio_transform4
                style_prefix "profiles"
                ypos 36
                xysize (455, 30)

                text "好感度：":
                    bold True
                    color "#ff8bdd"
                    outlines [ (3, "#000000") ]

                frame:
                    style "empty"
                    xysize (368, 42)
                    add "gui/menus/profile_stat_bar.webp"
                    bar:
                        xmaximum 368
                        ymaximum 42
                        value profile.get_stat("affection")
                        range 100
                        left_bar Frame("gui/menus/profile_affection_bar.webp", 0, 0)
                        right_bar Solid("#00000000")
                        
        if chara_id in chara and "Karma" in profile.tags and not mm_var:

            vbox:
                at bio_transform4
                style_prefix "profiles"
                ypos 36
                xysize (455, 30)

                $ karma_value = profile.get_stat("karma")

                hbox:
                    text "善恶值：":
                            bold True
                            color "#ffffff"
                            outlines [ (3, "#000000") ]

                    if -40 < karma_value < 40:
                        text "中立：":
                            bold True
                            color "#b3b3b3"
                            outlines [ (3, "#000000") ]
                    elif karma_value > 40:
                        text "善良：":
                            bold True
                            color "#e2ff92"
                            outlines [ (3, "#000000") ]
                    else:
                        text "邪恶：":
                            bold True
                            color "#aa2626"
                            outlines [ (3, "#000000") ]

                frame:
                    style "empty"
                    xysize (368, 42)
                    add "gui/menus/profile_stat_bar.webp"
                    fixed:
                        xysize (368, 42)
                        bar:
                            xmaximum 184
                            ymaximum 42
                            xpos 1
                            right_bar (
                                Frame("gui/menus/profile_malevolence_bar.webp", 0, 0) if karma_value <= -40 else
                                Frame("gui/menus/profile_ambivalence_bar.webp", 0, 0) if -40 < karma_value < 0 else
                                "#00000000"
                            )
                            left_bar Solid("#00000000")
                            bar_invert True
                            value max(0, -karma_value)
                            range 100
                        bar:
                            xmaximum 183
                            ymaximum 42
                            xpos 184
                            left_bar (
                                Frame("gui/menus/profile_benevolence_bar.webp", 0, 0) if karma_value >= 40 else
                                Frame("gui/menus/profile_ambivalence_bar.webp", 0, 0) if 0 < karma_value < 40 else
                                "#00000000"
                            )
                            right_bar Solid("#00000000")
                            value max(0, karma_value)
                            range 100

        hbox:
            at bio_transform5
            ypos 36
            if chara_id in chara and "Memories" in profile.tags:
                textbutton "回忆":
                    style_prefix "memories"
                    xoffset -10
                    action Show("memories", chara_id=chara_id, transition=dissolve)

    if chara_id in chara and "Outfits" in profile.tags:
        python:
            outfit_to_display = profile.selected_outfit
            if not profile.is_outfit_unlocked(outfit_to_display):
                outfit_to_display = 0
                profile.selected_outfit = 0
        
        imagebutton:
            xpos 800
            idle f"{chara_id}_outf{outfit_to_display}"
            hover Fixed(
                At(Transform(
                    f"{chara_id}_outf{outfit_to_display}",
                    matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(1.0),
                    additive=0.4,
                    blur=15.0,
                    alpha=1.0
                ), Position(xoffset=-5, yoffset=0)),
                f"{chara_id}_outf{outfit_to_display}",
                fit_first=True,
                xalign=0.5,
                yalign=0.5
            )
            focus_mask True
            hovered SetVariable("outf_hovered", True)
            unhovered SetVariable("outf_hovered", False)
            action Show("outfit_picker", chara_id=chara_id, transition=dissolve)
            at portrait_transform

        $ total_outfits = profile.get_total_outfits()
        $ unlocked_outfits = profile.unlocked_outfits

        if len(unlocked_outfits) > 1 and outf_hovered:
            key ["rollback"] action [
                SetField(
                    profile, 
                    "selected_outfit", 
                    unlocked_outfits[(unlocked_outfits.index(outfit_to_display) - 1) % len(unlocked_outfits)]
                ),
                SetDict(persistent.outfit_selections, chara_id, 
                    unlocked_outfits[(unlocked_outfits.index(outfit_to_display) - 1) % len(unlocked_outfits)]
                )
            ]

        if len(unlocked_outfits) > 1 and outf_hovered:
            key ["rollforward"] action [
                SetField(
                    profile, 
                    "selected_outfit", 
                    unlocked_outfits[(unlocked_outfits.index(outfit_to_display) + 1) % len(unlocked_outfits)]
                ),
                SetDict(persistent.outfit_selections, chara_id, 
                    unlocked_outfits[(unlocked_outfits.index(outfit_to_display) + 1) % len(unlocked_outfits)]
                )
            ]

    else:
        add f"{chara_id}_outf0" xpos 800 at portrait_transform


style profiles_label is gui_label
style profiles_label_text is gui_label_text
style bio1_text is gui_text
style bio2_text is gui_text
style memories_button is gui_button
style memories_button_text is gui_button_text

style profiles_label:
    xpos 10
    ypos 40

style profiles_label_text:
    font zh_display_font
    size 64
    xalign 0.5
    outlines [ (3, "#000000") ]

style bio1_text:
    size 24
    ypos -4
    xalign 0.0
    bold True
    outlines [(2, "#000000", 0, 0)]

style bio2_text:
    size 18
    xalign 0.0
    text_align 0.0
    outlines [(2, "#000000", 0, 0)]

style memories_button_text:
    bold True
    size 36