init offset = -1

define memories = [
    # id, thumbnail, label, characters, description, tags
    ["astarayngbg", "c1p4b1s1 5", "astarayngbg", ["asta", "rayn"], ["少女的玩闹"], ["None"]],
    ["soulskinnydip", "c1p4b2s1 20", "soul_skinnydipping", ["soul"], ["与索尔的默契"], ["None"]],
    ["rayngw", "c1p6b1s1 41", "rayn_gettinwet", ["rayn"], ["魅惑淋浴"], ["Blowjob"]],
    ["laylconfess", "c1p7b1s1 6", "laylconfess", ["layl"], ["渴望之夜"], ["Fingering", "Squirting"]],
    # ["","","",[""],[""],[""]],
]
default memory_filter = None

screen filter_memory():
    style_prefix "filter_memory"
    zorder 103
    modal True

    frame:
        align (0.5, 0.5)

        vbox:
            spacing 15

            viewport:
                mousewheel True
                draggable True

                vbox:
                    textbutton _("全部"):
                        style "filter_memory_button"
                        action [SetVariable("memory_filter", None), Hide("filter_memory")]
                    textbutton _("口交"):
                        style "filter_memory_button"
                        action [SetVariable("memory_filter", "Blowjob"), Hide("filter_memory")]
                    textbutton _("手交"):
                        style "filter_memory_button"
                        action [SetVariable("memory_filter", "Fingering"), Hide("filter_memory")]
                    textbutton _("潮吹"):
                        style "filter_memory_button"
                        action [SetVariable("memory_filter", "Squirting"), Hide("filter_memory")]

            textbutton _("关闭") keysym "game_menu" action Hide("filter_memory")


style filter_memory_viewport is viewport
style filter_memory_vscrollbar is vscrollbar
style filter_memory_button is gui_button
style filter_memory_button_text is gui_button_text

style filter_memory_viewport:
    xsize 200
    yfill False

style filter_memory_button:
    xysize (200, 40)

style filter_memory_button_text:
    properties gui.text_properties("navigation_button")
    xalign 0.5
    size 24
    outlines [(2, "#000000", 0, 0)]
    hover_outlines [(2, persistent.theme_color, 0, 0)]
    selected_outlines [(2, persistent.theme_color, 0, 0)]

screen memories(chara_id):
    style_prefix "memories_select"
    zorder 102
    modal True
    add Solid("#0000009f")

    hbox:
            xpos 660
            ypos 40

            text "筛选：":
                ypos 14
                bold True
                size 24
                color persistent.theme_color
                outlines [(2, "#000000", 0, 0)]

            textbutton _(memory_tag_zh(memory_filter) if memory_filter else "全部"):
                ypos 8
                style "memory_filter_button"
                action Show("filter_memory")

    vpgrid:
        xsize 1920
        align (0.5, 0.045)
        yoffset 50
        xoffset 20
        cols 4
        spacing 25
        draggable True
        mousewheel True
        scrollbars "vertical"
        side_spacing 20

        for r in memories:
            if chara_id in r[3] and (memory_filter is None or memory_filter in r[5]):
                $ memory_id = r[0]
                if not chara[chara_id].has_memory(memory_id):
                    frame:
                        style "empty"
                        xysize (440, 350)
                        button:
                            align (0.5, 0.5)
                            sensitive gui_nullbutton
                            action NullAction()
                            text "暂无数据":
                                style "memories_select_button_text"
                                yalign 0.37
                else:
                    frame:
                        style "empty"
                        xysize (440, 350)
                        button:
                            align (0.5, 0.5)
                            style "memories_select_button2"
                            action Replay(r[2], locked=False)
                            has vbox
                            add Transform(f"{r[1]}", size=(384, 216))
                            text r[4]:
                                style "memories_select_button_text"
                                yalign 1.2
                            at memory_hover
    
    key "game_menu" action Hide("memories", transition=dissolve)

    textbutton _("返回"):
        style "mem_return_button"
        action Hide("memories", transition=dissolve)
                        

style memories_select_button is gui_button
style memories_select_button_text is gui_button_text
style mem_return_button is gui_button
style mem_return_button_text is gui_button_text

style memories_select_vscrollbar is vscrollbar:
    unscrollable "hide"

style memories_select_button:
    properties gui.button_properties("slot_button")
    xalign 0.5
    yalign 0.5
    idle_background "gui/button/slot.png"
    hover_background Fixed(
        At(Transform(
            "gui/button/slot.png",
            matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(1.0),
            additive=2.0,
            blur=5.0,
            alpha=1.0
        ), Position(xoffset=-1.5, yoffset=-1.5)),
        "gui/button/slot.png",
        fit_first=True
    )
    background "gui/button/slot.png"

style memories_select_button2:
    properties gui.button_properties("slot_button")
    xalign 0.5
    yalign 0.5
    hover_background Fixed(
        At(Transform(
            "gui/button/slot.png",
            matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(1.0),
            additive=2.0,
            blur=5.0,
            alpha=1.0,
            zoom=1.116
        ), Position(xoffset=-25, yoffset=-17)),
        fit_first=True
    )

style memories_select_button_text:
    properties gui.text_properties("slot_button")

style mem_return_button:
    properties gui.button_properties("navigation_button")
    xalign 0.05
    yalign 0.95

style mem_return_button_text:
    properties gui.text_properties("navigation_button")
    bold True

style memory_filter_button is gui_button
style memory_filter_button_text is gui_button_text

style memory_filter_button_text:
    bold True
    size 24
