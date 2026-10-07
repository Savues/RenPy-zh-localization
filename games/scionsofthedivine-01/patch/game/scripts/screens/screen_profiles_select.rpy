init offset = -1

init python:
    import re

    def get_sortable_name(name):
        evaluated_name = renpy.substitute(name)
        cleaned_name = re.sub(r'\[.*?\]', '', evaluated_name)
        return cleaned_name.lower()

    def filter_profiles(characters, active_filter):
        if not active_filter:
            return characters
        
        filtered = {}
        for key, value in characters.items():
            if active_filter in value.tags:
                filtered[key] = value
        return filtered

    def sort_profiles(characters, sort_type):
        special_profile_id = "mc"

        if sort_type == "A-Z":
            sorted_characters = dict(sorted(characters.items(), key=lambda x: get_sortable_name(x[1].name)))
        elif sort_type == "Age":
            sorted_characters = dict(sorted(characters.items(), key=lambda x: x[1].bio_info["age"]))
        elif sort_type == "Affection":
            #romanceable = {k: v for k, v in characters.items() if "Romanceable" in v.tags}
            sorted_characters = dict(sorted(characters.items(), key=lambda x: x[1].affection, reverse=True))
        else:
            order = getattr(store, "all_characters_order", list(characters.keys()))
            sorted_characters = {cid: characters[cid] for cid in order if cid in characters}

        if special_profile_id in sorted_characters:
            special_profile = {special_profile_id: sorted_characters.pop(special_profile_id)}
            sorted_characters = {**special_profile, **sorted_characters}

        return sorted_characters

    def clear_filters():
        global filter_profile
        filter_profile = ""
        renpy.restart_interaction()

default selected_chara = None
default filter_profile = ""
default sort_profile = "Default"
default profile_filters = [
        ("全部", ""),  # (Button label, filter value)
        ("女性", "Women"),
        ("男性", "Men"),
        ("可攻略", "Romanceable"),
        ("法师", "Mages"),
        # Add more as needed
    ]

screen filter_profile():
    style_prefix "filter_profile"
    modal True

    frame:
        align (0.5, 0.5)

        vbox:
            spacing 15

            viewport:
                mousewheel True
                draggable True

                vbox:
                    for label, value in profile_filters:
                        if value == "":
                            textbutton _(label) action [Function(clear_filters), Hide("filter_profile")]
                        else:
                            textbutton _(label) action [SetVariable("filter_profile", value), Hide("filter_profile")]

            textbutton _("关闭") keysym "game_menu" action Hide("filter_profile")


style filter_profile_viewport is viewport
style filter_profile_vscrollbar is vscrollbar
style filter_profile_button is gui_button
style filter_profile_button_text is gui_button_text

style filter_profile_viewport:
    xsize 200
    yfill False

style filter_profile_button:
    xysize (200, 40)

style filter_profile_button_text:
    properties gui.text_properties("navigation_button")
    xalign 0.5
    size 24
    outlines [(2, "#000000", 0, 0)]
    hover_outlines [(2, persistent.theme_color, 0, 0)]
    selected_outlines [(2, persistent.theme_color, 0, 0)]

screen profilesel():
    tag menu
    if mm_var:
        add "fog_effect"
        add "magic_effect" at theme_ember
    else:
        add Solid("#0000009f")
    add "gui/menus/menu.webp"
    modal True

    on "hide":
        action [
            SetVariable("selected_chara", None),
            Function(clear_filters),
            SetVariable("sort_profile", "Default"),
            Hide("profile")
        ]
    on "replaced":
        action [
            SetVariable("selected_chara", None),
            Hide("profile")
        ]

    fixed:
        order_reverse True

        style_prefix "profilesel"

        hbox:
            xpos 660
            ypos 40

            text "筛选：":
                bold True
                size 24
                color persistent.theme_color
                outlines [(2, "#000000", 0, 0)]

            textbutton _(filter_label(filter_profile) if filter_profile else "全部"):
                ypos 8
                style "profilesel_filter_button"
                action Show("filter_profile")
        
        hbox:
            xpos 1125
            ypos 40
            text "排序：":
                bold True
                size 24
                color persistent.theme_color
                outlines [(2, "#000000", 0, 0)]

            textbutton _("[sort_profile]"):
                ypos 8
                style "profilesel_filter_button"
                action [
                    If(sort_profile == "Default", SetVariable("sort_profile", "A-Z"),
                    If(sort_profile == "A-Z", SetVariable("sort_profile", "Age"),
                    If(sort_profile == "Age", [SetVariable("sort_profile", "Affection"), SetVariable("filter_profile", "Romanceable")],
                    [SetVariable("sort_profile", "Default"), Function(clear_filters)])))
                ]

        $ filtered_profiles = filter_profiles(chara, filter_profile)
        $ displayed_characters = sort_profiles(filtered_profiles, sort_profile)
        $ num_profiles = len(displayed_characters)
        $ rows = (num_profiles + 6 - 1) // 6
        
        grid 6 rows:
            style "empty"
            xalign 0.5
            ypos 100
            spacing 0
            
            for chara_id, profile in displayed_characters.items():
                frame:
                    style "empty"

                    if profile.profile:
                        frame:
                            style "empty"
                            xysize (100, 100)
                            button:
                                xysize (100, 100)
                                background f"profile_{chara_id}"
                                hover_background Transform(
                                    f"profile_{chara_id}",
                                    matrixcolor=TintMatrix('#ffffff') * BrightnessMatrix(0.1),
                                    )
                                selected_background Fixed(
                                        At(Transform(
                                            f"profile_{chara_id}",
                                            alpha=0.5,
                                            zoom=0.98
                                            )
                                        ),
                                        fit_first=True,
                                        xalign=0.5,
                                        yalign=0.5
                                )
                                idle_foreground "gui/database/profilefg.webp"
                                hover_foreground Transform(
                                    "gui/database/profilefg.webp",
                                    matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(1.0)
                                    )
                                selected_foreground Fixed(
                                        At(Transform(
                                            "gui/database/profilefg.webp",
                                            matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5),
                                            zoom=0.98
                                            )
                                        ),
                                        fit_first=True,
                                        xalign=0.5,
                                        yalign=0.5
                                )
                                selected selected_chara == chara_id
                                action [
                                    Hide('profile'),
                                    Show('profile', chara_id=chara_id, transition=dissolve),
                                    SetVariable("selected_chara", chara_id),
                                ]
                    else:
                        frame:
                            style "empty"
                            xysize (100, 100)
                            button:
                                xysize (100, 100)
                                background "gui/database/profile_nodata.webp"
                                foreground "gui/database/profilefg.webp"
                                focus_mask True
                                sensitive gui_nullbutton
                                action NullAction()
                                text "暂无数据" yalign 0.55
    if mm_var:
        key "game_menu" action Return()
        textbutton _("返回"):
            style "prof_return_button"
            action Return()
    else:
        key "game_menu" action ShowMenu("save")
        textbutton _("返回"):
            style "prof_return_button"
            action ShowMenu("save")
       

style profilesel_button is gui_button
style profilesel_text is gui_button_text
style prof_return_button is gui_button
style prof_return_button_text is gui_button_text

style profilesel_button:
    xysize (400, 400)

style profilesel_text:
    properties gui.text_properties("slot_button")
    xalign 0.5
    yalign 1.2
    outlines [(2, "#000000", 0, 0)]

style profilesel_filter_button is gui_button
style profilesel_filter_button_text is gui_button_text

style profilesel_filter_button_text:
    bold True
    size 24

style prof_return_button:
    properties gui.button_properties("navigation_button")
    xalign 0.05
    yalign 0.95

style prof_return_button_text:
    properties gui.text_properties("navigation_button")
    bold True
