init offset = -1

screen credits():
    tag menu
    style_prefix "credits"

    add "fog_effect"
    add "magic_effect" at theme_ember

    add "gui/menus/menu.webp"
    add "gui/menus/main_menu.webp"
    add Transform(
        "gui/menus/main_menu2.webp",
        matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(0.5)
    )

    label "[config.version!t]":
        align (0.95, 0.15)

    frame:
        align (1.0, 0.8)
        style "credits_frame"

        frame:
            style "credits_content_frame"

            hbox:
                xmaximum 1400

                side "c r":

                    viewport id "credits_vp":
                        xysize (1400, 650)
                        mousewheel True
                        draggable True
                        pagekeys True
                        yinitial 0.0

                        vbox:
                            xpos 500
                            ypos 125
                            label "制作："
                            text _("Dark Seraph Productions")
                            text _("")
                            hbox:
                                ysize 60
                                label "关注／支持我：" align (0.5, 0.5)
                                textbutton "Patreon":
                                    action OpenURL("https://www.patreon.com/DarkSeraphProd")
                                label " 或 " align (0.5, 0.5)
                                textbutton "Itch":
                                    action OpenURL("https://darkseraphavn.itch.io")
                            text _("")
                            label "视觉："
                            text _("Honey Select 2 与 Studio Neo（Illusion）")
                            text _("HS2 在 Illusion Discord 与 Patreon 上的模组社区")
                            text _("部分自制材质与全部 UI：Dark Seraph")
                            text _("")
                            label "音频："
                            text _("音乐由 suno.ai 生成，后期与歌词：Dark Seraph")
                            text _("")
                            label "代码："
                            text _("SoDaRa（Kinetic Text Tags）")
                            text _("Stella@MakeVisualNovels（Text Shader Tags）")
                            text _("Python 与 UI 代码：Dark Seraph")
                            text _("使用 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 制作。\n\n    [renpy.license!t]")
                    
                    vbar value YScrollValue("credits_vp") unscrollable "hide"

    textbutton _("返回"):
        style "credits_return_button"
        action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style credits_frame is empty
style credits_content_frame is empty
style credits_label is gui_label
style credits_label_text is gui_label_text
style credits_text is gui_text
style credits_return_button is gui_button
style credits_return_button_text is gui_button_text
style credits_button is gui_button
style credits_button_text is gui_button_text

style credits_content_frame:
    left_margin 40
    right_margin 40
    top_margin 20
    bottom_margin 20

style credits_label_text:
    size 40
    font zh_display_font

style credits_return_button:
    properties gui.button_properties("navigation_button")
    xalign 0.05
    yalign 0.95
    size_group "prof_nav"

style credits_return_button_text:
    properties gui.text_properties("navigation_button")
    bold True
    size 40
    xpos -4

style credits_button:
    align (0.5, 0.5)
    
style credits_button_text:
    properties gui.button_properties("navigation_button")
    align (0.5, 0.5)
    font zh_display_font
    size 40
    underline True