init offset = -1

################################################################################

style default:
    properties gui.text_properties()
    language gui.language
    outlines [(absolute(1), "#000", absolute(1), absolute(1))]

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################


screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            if not renpy.variant("small"):
                add SideImage() xalign 0.0 yalign 1.0
            background Image("gui/textbox.png", xalign=0.0, yalign=1.0)
            if renpy.variant("small"):
                add SideImage() xalign 0.0 yalign 1.085
                background Image("gui/textbox_small.png", xalign=0.0, yalign=1.0)
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## Если есть боковое изображение ("голова"), показывает её поверх текста.
    ## По стандарту не показывается на варианте для мобильных устройств — мало
    ## места.
#    if not renpy.variant("small"):
#        add SideImage() xalign 0.0 yalign 1.0
#    if renpy.variant("small"):
#        add SideImage():
#            ypos -60
            #xalign 0.0
            #yalign 1.0
    
    if skip_dialogue == True:
        imagebutton:
            at alpha_dissolve
            focus_mask True
            idle "gui/skip_dialogue/skip_dialogue_idle.png"
            hover "skip_dialogue_hover"
            hover_sound "audio/menu/buttonhoversound.ogg"
            activate_sound "audio/menu/buttonactionsound.ogg"
            action [SetVariable("skip_dialogue_label", None), Jump(skip_dialogue_label)]

## Делает namebox доступным для стилизации через объект Character.
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

    #background Image("gui/textbox.png", xalign=0.5, yalign=1.0) ## Фон текста

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    #background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
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

################################################################################

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


################################################################################


#Timer
screen countdown:
    #timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    timer 0.01 repeat True action If(timez > 0, true=SetVariable('timez', timez - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar:
        xsize 700
        ysize 10
        xalign 0.5
        yalign 0.1
        at alpha_dissolve
        value AnimatedValue(value=timez, range=timer_range, delay=1.0)

transform choice_dissolve:
    alpha 0
    linear 0.3 alpha 1
    on hide:
        alpha 1
        linear 0.3 alpha 0

transform rs_notify:
    subpixel True
    yanchor 0.5
    xalign 0.5
    ypos -82
    alpha 0.0
    ease 0.6 ypos 82 alpha 1.0
    on idle:
        ease .3 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
    on hide:
        ease .3 zoom 1.0 alpha 0 ypos -82 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)

transform nav_tasksmenu:
    subpixel True
    anchor (0.5, 0.5)
    xpos 0
    ypos 61
    alpha 0.0
    ease 0.3 xpos 160 alpha 0.8
    on idle:
        ease .3 zoom 1.0 alpha 0.8 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 alpha 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)

transform nav_navmenu:
    subpixel True
    anchor (0.5, 0.5)
    xpos -70
    ypos 61
    alpha 0.0
    ease 0.3 xpos 70 alpha 0.8
    on idle:
        ease .3 zoom 1.0 alpha 0.8 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 alpha 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)

transform nav_menu:
    subpixel True
    xpos -600
    alpha 0.0
    ease 0.5 xpos 0 alpha 1.0

transform nav_rs:
    subpixel True
    yanchor 0.5
    xpos -250
    ypos 210
    alpha 0.0
    ease 0.3 xpos 00 alpha 1.0
    on idle:
        ease .3 zoom 1.0 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)
        
transform nav_gallery:
    subpixel True
    yanchor 0.5
    xpos -300
    ypos 306
    alpha 0.0
    ease 0.4 xpos 00 alpha 1.0
    on idle:
        ease .3 zoom 1.0 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)
        
transform nav_save:
    subpixel True
    yanchor 0.5
    xpos -350
    ypos 402
    alpha 0.0
    ease 0.5 xpos 00 alpha 1.0
    on idle:
        ease .3 zoom 1.0 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)
        
transform nav_load:
    subpixel True
    yanchor 0.5
    xpos -400
    ypos 498
    alpha 0.0
    ease 0.6 xpos 00 alpha 1.0
    on idle:
        ease .3 zoom 1.0 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)
        
transform nav_options:
    subpixel True
    yanchor 0.5
    xpos -450
    ypos 594
    alpha 0
    ease 0.7 xpos 00 alpha 1.0
    on idle:
        ease .3 zoom 1.0 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)
        
transform nav_main:
    subpixel True
    yanchor 0.5
    xpos -500
    ypos 690
    alpha 0.0
    ease 0.8 xpos 00 alpha 1.0
    on idle:
        ease .3 zoom 1.0 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)
        
transform nav_quit:
    subpixel True
    yanchor 0.5
    xpos -550
    ypos 916
    alpha 0.0
    ease 0.9 xpos 00 alpha 1.0
    on idle:
        ease .3 zoom 1.0 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 xpos 00 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)
        
transform options_general:
    subpixel True
    yanchor 0.5
    xpos 142
    ypos 252
    alpha 0.0
    ease 0.3 alpha 1.0
    on idle:
        ease .3 zoom 1.0 xpos 142 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 xpos 142 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
        
transform options_audio:
    subpixel True
    yanchor 0.5
    xpos 142
    ypos 332
    alpha 0.0
    ease 0.3 alpha 1.0
    on idle:
        ease .3 zoom 1.0 xpos 142 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 zoom 1.06 xpos 142 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
        
transform saveloadslot:
    subpixel True
    zoom 0.6
    alpha 0.0
    ease 0.3 zoom 1.0 alpha 1.0
    on idle:
        ease .3 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
        
transform saveloadtab:
    subpixel True
    zoom 0.6
    alpha 0.0
    ease 0.3 zoom 1.0 alpha 1.0
    on idle:
        ease .3 alpha 0.6 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 alpha 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)
        

transform quickmenu_smooth:
    subpixel True
    alpha 0
    ypos 100
    ease .3 alpha 1 ypos 0
    on idle:
        ease .3 alpha 1 ypos 0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .3 alpha 1 ypos -5 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.3)
    on hide:
        ease .3 alpha 0 ypos -100

transform rs_button_may:
    subpixel True
    anchor (0.5, 0.5)
    ypos 582
    xpos 2000
    alpha 0.0
    ease 0.5 xpos 290 ypos 582 alpha 1.0
    on idle:
        ease .5 ypos 582 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .3 ypos 600 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.10)
        
transform rs_button_lillian:
    subpixel True
    anchor (0.5, 0.5)
    ypos 582
    xpos 2500
    alpha 0.0
    ease 0.55 xpos 558 ypos 582 alpha 1.0
    on idle:
        ease .5 ypos 582 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .3 ypos 600 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.10)

transform rs_button_minami:
    subpixel True
    anchor (0.5, 0.5)
    ypos 582
    xpos 3000
    alpha 0.0
    ease 0.6 xpos 826 ypos 582 alpha 1.0
    on idle:
        ease .5 ypos 582 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .3 ypos 600 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.10)

transform rs_button_izumi:
    subpixel True
    anchor (0.5, 0.5)
    ypos 582
    xpos 3500
    alpha 0.0
    ease 0.65 xpos 1094 ypos 582 alpha 1.0
    on idle:
        ease .5 ypos 582 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .3 ypos 600 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.10)

transform rs_button_asami:
    subpixel True
    anchor (0.5, 0.5)
    ypos 582
    xpos 4000
    alpha 0.0
    ease 0.7 xpos 1362 ypos 582 alpha 1.0
    on idle:
        ease .5 ypos 582 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .3 ypos 600 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.10)

transform rs_button_nao:
    subpixel True
    anchor (0.5, 0.5)
    ypos 582
    xpos 4500
    alpha 0.0
    ease 0.75 xpos 1630 ypos 582 alpha 1.0
    on idle:
        ease .5 ypos 582 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .3 ypos 600 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.10)
        
transform rs_icon:
    subpixel True
    xpos -200
    alpha 0.0
    ease 0.75 xpos 40 alpha 1.0
    on idle:
        ease .5 xpos 40 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .3 xpos 50 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.08)

transform rs_return:
    subpixel True
    xpos -260
    alpha 0.0
    ease 0.75 xpos 00 alpha 0.8
    on idle:
        ease .5 xpos 00 alpha 0.8 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .3 xpos 00 alpha 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
        
transform rs_return_nav:
    subpixel True
    alpha 0.0
    on idle:
        ease .5 alpha 0.8 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .3 alpha 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)

transform rs_bright:
    subpixel True
    top
    alpha 0.0
    ypos 200
    zoom 1.5
    ease 0.6 ypos 0 zoom 1 alpha 1.0
    on idle:
        ease .3 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.4)
    on hide:
        ease 0.5 ypos -100 zoom 1.5 alpha 0
        
transform rs_bright_2:
    subpixel True
    top
    alpha 0.0
    ypos 200
    zoom 1.5
    ease 0.6 ypos 0 zoom 1 alpha 1.0
    on idle:
        ease .3 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease 0.5 ypos -100 zoom 1.5 alpha 0
        
transform bright_button_main:
    subpixel True
    anchor (0.5, 0.5)
    xpos 1372
    ypos 79
    on idle:
        ease .3 alpha 0.6 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 alpha 1.0 zoom 1.006 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.4)
        
transform bright_button_others:
    subpixel True
    anchor (0.5, 0.5)
    xpos 1640
    ypos 79
    on idle:
        ease .3 alpha 0.6 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 alpha 1.0 zoom 1.006 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.4)
        
transform others_bright:
    subpixel True
    alpha 0
    xpos 100
    ease .3 alpha 1 xpos 0
    on idle:
        ease .3 alpha 1 xpos 0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 alpha 1 xpos 0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
    on hide:
        ease .2 alpha 0 xpos -100
        
transform just_bright:
    subpixel True
    on idle:
        ease .3 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
        
transform others_gallery:
    subpixel True
    alpha 0
    xanchor 0.5
    yanchor 0.5
    xpos 1723
    ypos 985
    zoom 1
    ease .3 alpha 1 xpos 1623
    on idle:
        ease .3 alpha 1 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 alpha 1 zoom 1.05 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
    on hide:
        ease .2 alpha 0 xpos 1523
 
transform choice_bright_patreon:
    subpixel True
    on idle:
        ease .3 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.4)
        
transform choice_bright_url_button_1:
    subpixel True
    alpha 0.0
    xanchor 0.5
    yanchor 0.5
    xsize 80
    ysize 80
    xpos 2000
    ease 0.4 alpha 0.6 xpos 1836
    on idle:
        ease .3 alpha 0.6 xsize 80 ysize 80 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 alpha 1.0 xsize 90 ysize 90 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease 0.5 alpha 0
        
transform choice_bright_url_button_2:
    subpixel True
    alpha 0.0
    xanchor 0.5
    yanchor 0.5
    xsize 80
    ysize 80
    xpos 2100
    ease 0.6 alpha 0.6 xpos 1836
    on idle:
        ease .3 alpha 0.6 xsize 80 ysize 80 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 alpha 1.0 xsize 90 ysize 90 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease 0.5 alpha 0
 
transform choice_bright:
    subpixel True
    alpha 0.0
    ease 0.6 alpha 1.0
    on idle:
        ease .3 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.4)
    on hide:
        ease 0.5 alpha 0
        
transform choice_bright_2:
    subpixel True
    alpha 0.0
    ease 0.6 alpha 1.0
    on idle:
        ease .3 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease 0.5 alpha 0
 
transform gallery_button_1:
    subpixel True
    xpos 2000
    alpha 0.0
    ease 0.5 xpos 355 alpha 1.0
    zoom 1
    on idle:
        ease .5 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
        
transform gallery_button_2:
    subpixel True
    xpos 2000
    alpha 0.0
    ease 0.6 xpos 355 alpha 1.0
    zoom 1
    on idle:
        ease .5 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
 
transform gallery_button_3:
    subpixel True
    xpos 2000
    alpha 0.0
    ease 0.7 xpos 355 alpha 1.0
    zoom 1
    on idle:
        ease .5 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
 
transform gallery_button_4:
    subpixel True
    xpos 2000
    alpha 0.0
    ease 0.8 xpos 355 alpha 1.0
    zoom 1
    on idle:
        ease .5 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
 
transform gallery_button_5:
    subpixel True
    xpos 2000
    alpha 0.0
    ease 1.0 xpos 355 alpha 1.0
    zoom 1
    on idle:
        ease .5 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
        
transform gallery_button_6:
    subpixel True
    xpos 2000
    alpha 0.0
    ease 1.0 xpos 355 alpha 1.0
    zoom 1
    on idle:
        ease .5 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
        
transform gallery_button_7:
    subpixel True
    xpos 2000
    alpha 0.0
    ease 1.0 xpos 355 alpha 1.0
    zoom 1
    on idle:
        ease .5 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
 
transform gallery_button_8:
    subpixel True
    xpos 2000
    alpha 0.0
    ease 1.0 xpos 355 alpha 1.0
    zoom 1
    on idle:
        ease .5 zoom 1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
 
 
transform fromBottom:
    subpixel True
    alpha 0.0 yalign 1.0 yanchor 0.0
    parallel:
        easein 0.6 alpha 1.0
    parallel:
        easein 0.4 yalign 0.7
    on hide:
        alpha 1 zoom 1 xanchor 0.5 yanchor 0.7
        block:
            easein 0.1 zoom 1.1
            easein 0.4 alpha 0 zoom 0.5
            
transform fromRight:
    subpixel True
    alpha 0.0 xpos 2060 xanchor 0.0
    parallel:
        easein 0.6 alpha 1.0
    parallel:
        easein 0.4 xpos 1060
    on hide:
        alpha 1 zoom 1 xpos 1060 yanchor 0.5
        block:
            easein 0.1 zoom 1.1
            easein 0.4 alpha 0 zoom 0.6 xpos 1060
            
transform fromLeft:
    subpixel True
    alpha 0.0 xpos 0 xanchor 0.0
    parallel:
        easein 0.6 alpha 1.0
    parallel:
        easein 0.4 xpos 260
    on hide:
        alpha 1 zoom 1 xpos 260 yanchor 0.5
        block:
            easein 0.1 zoom 1.1
            easein 0.4 alpha 0 zoom 0.6 xpos 260

transform zoom_button_right:
    subpixel True
    left
    on idle:
        linear .1 zoom 1.0
    on hover:
        linear .1 zoom 1.1

transform choice_sex_1:
    subpixel True
    yanchor 0.5
    alpha 0 xpos 1940
    ease .5 alpha 1 xpos 1410
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 3140 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform choice_sex_2:
    subpixel True
    yanchor 0.5
    alpha 0 xpos 2040
    ease .6 alpha 1 xpos 1410
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 2940 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform choice_sex_3:
    subpixel True
    yanchor 0.5
    alpha 0 xpos 2140
    ease .7 alpha 1 xpos 1410
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 2740 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform choice_sex_4:
    subpixel True
    yanchor 0.5
    alpha 0 xpos 2240
    ease .8 alpha 1 xpos 1410
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 2540 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform choice_sex_5:
    subpixel True
    yanchor 0.5
    alpha 0 xpos 2340
    ease .9 alpha 1 xpos 1410
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 2340 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform choice_sex_6:
    subpixel True
    yanchor 0.5
    alpha 0 xpos 2440
    ease 1 alpha 1 xpos 1410
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 2140 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform choice_sex_7:
    subpixel True
    yanchor 0.5
    alpha 0 xpos 2540
    ease 1.1 alpha 1 xpos 1410
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 1940 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)


transform gallery_choice_sex_1:
    subpixel True
    yanchor 0.5
    xanchor 0.5
    alpha 0 xpos 1940
    ease .5 alpha 1 xpos 1510
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 3140 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform gallery_choice_sex_2:
    subpixel True
    yanchor 0.5
    xanchor 0.5
    alpha 0 xpos 2040
    ease .6 alpha 1 xpos 1510
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 2940 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform gallery_choice_sex_3:
    subpixel True
    yanchor 0.5
    xanchor 0.5
    alpha 0 xpos 2140
    ease .7 alpha 1 xpos 1510
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 2740 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform gallery_choice_sex_4:
    subpixel True
    yanchor 0.5
    xanchor 0.5
    alpha 0 xpos 2240
    ease .8 alpha 1 xpos 1510
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 2540 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform gallery_choice_sex_5:
    subpixel True
    yanchor 0.5
    xanchor 0.5
    alpha 0 xpos 2340
    ease .9 alpha 1 xpos 1510
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 2340 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform gallery_choice_sex_6:
    subpixel True
    yanchor 0.5
    xanchor 0.5
    alpha 0 xpos 2440
    ease 1 alpha 1 xpos 1510
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 2140 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)

transform gallery_choice_sex_7:
    subpixel True
    yanchor 0.5
    alpha 0 xpos 2540
    ease 1.1 alpha 1 xpos 1510
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.1 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos 1940 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        

transform choice_sex_leave:
    subpixel True
    alpha 0 xpos 140
    ease .5 alpha 1 xpos 110
    on idle:
        ease .5 xpos 110 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
        ease .3 xpos 80
        ease .3 xpos 130
        repeat
        
transform leave_right:
    subpixel True
    alpha 0 xpos 1550
    ease .5 alpha 1 xpos 1510
    on idle:
        ease .5 xpos 1510 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
        ease .3 xpos 1480
        ease .3 xpos 1530
        repeat
        
transform leave_left:
    subpixel True
    alpha 0 xpos 140
    ease .5 alpha 1 xpos 110
    on idle:
        ease .5 xpos 110 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
        ease .3 xpos 80
        ease .3 xpos 130
        repeat
        
transform choice_sex_cum_1:
    subpixel True
    alpha 0 xpos 210
    ease .5 alpha 1 xpos 120
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos -200 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        
transform choice_sex_cum_2:
    subpixel True
    alpha 0 xpos 260
    ease .55 alpha 1 xpos 120
    on idle:
        ease .5 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 zoom 1.03 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
    on hide:
        ease .5 alpha 0 xpos -200 zoom 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)

##########   DATE EVENT BUTTON    ##########

transform date_choice_button_1:
    subpixel True
    ypos -50
    alpha 0.0
    ease 0.5 ypos 0 alpha 1.0
    zoom 1
    on idle:
        ease .5 ypos 0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 ypos 10 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
        
transform date_choice_button_2:
    subpixel True
    ypos -100
    alpha 0.0
    ease 0.6 ypos 0 alpha 1.0
    zoom 1
    on idle:
        ease .5 ypos 0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 ypos 10 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)
        
transform date_choice_button_3:
    subpixel True
    ypos -150
    alpha 0.0
    ease 0.7 ypos 0 alpha 1.0
    zoom 1
    on idle:
        ease .5 ypos 0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 ypos 10 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.15)

transform date_choice_nextday:
    subpixel True
    xpos 1200
    alpha 0
    ease 1.2 alpha 1 xpos 0
    on idle:
        ease .5 xpos 0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .5 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.2)
        ease .3 xpos -10
        ease .3 xpos 10
        repeat

transform date_choice_title:
    xpos 1400
    alpha 0.0
    ease 1 xpos 0 alpha 1.0

transform date_choice_line_1:
    xpos 1200
    alpha 0.0
    ease 1.1 xpos 0 alpha 1.0
    
transform date_choice_line_2:
    ypos 40
    alpha 0.0
    ease 0.8 ypos 0 alpha 1.0
    
transform date_choice_line_3:
    xpos 1400
    alpha 0.0
    ease 1.4 xpos 0 alpha 1.0

##########################################

transform animated_button_show_center(time_delay):
    subpixel True
    top
    alpha 0.0
    yoffset 200
    pause time_delay
    parallel:
        ease 0.41 yoffset 0
    parallel:
        easeout 0.23 alpha 1.0
    on idle:
        linear .1 zoom 1.0
    on hover:
        linear .1 zoom 1.1
    on hide:
        alpha 1 zoom 1 xanchor 0.5 yanchor 0.7
        block:
            easein 0.1 zoom 1.1
            easein 0.4 alpha 0 zoom 0.5
            
transform animated_button_show_right(time_delay):
    subpixel True
    left
    alpha 0.0
    xoffset 200
    pause time_delay
    parallel:
        ease 0.41 xoffset 0
    parallel:
        easeout 0.23 alpha 1.0
    on idle:
        linear .1 zoom 1.0
    on hover:
        linear .1 zoom 1.1
    on hide:
        alpha 1 zoom 1 yanchor 0.5
        block:
            easein 0.1 zoom 1.1
            easein 0.4 alpha 0 zoom 0.6
            
transform animated_button_show_left(time_delay):
    subpixel True
    left
    alpha 0.0
    xoffset -200
    pause time_delay
    parallel:
        ease 0.41 xoffset 0
    parallel:
        easeout 0.23 alpha 1.0
    on idle:
        linear .1 zoom 1.0
    on hover:
        linear .1 zoom 1.1
    on hide:
        alpha 1 zoom 1 yanchor 0.5
        block:
            easein 0.1 zoom 1.1
            easein 0.4 alpha 0 zoom 0.6

transform game_help:
    subpixel True
    alpha 0 xpos 30
    ease .5 alpha 1 xpos 00


init: ##
    $ choice_var = 0 ##

screen choice(items):
    style_prefix "choice"
    default time_delay = 0.16
    if choice_var == 0: ##
        vbox:
            at fromBottom
            ypos 1560
            yalign 0.5
            for i, item in enumerate(items, start=1):
                textbutton item.caption:
                    action item.action
                    at animated_button_show_center(i * time_delay)
    default time_delay = 0.16
    if choice_var == 1: ##
        vbox:
            xfill True
            at fromRight
            xalign 0.0
            xpos 1060
            spacing 8
            for i, item in enumerate(items, start=1):
                button:
                    minimum 600, 68
                    #idle_background "gui/button/choice_idle_background_1.png" focus_mask True
                    #hover_background "gui/button/choice_hover_background_1.png"
                    idle_background "gui/button/choice_idle_background_1.png" focus_mask True
                    hover_background "gui/button/choice_hover_background_1.png"
                    text item.caption #yalign .5
                    action item.action
                    at animated_button_show_right(i * time_delay)
    if choice_var == 2: ##
        vbox:
            xfill True
            at fromLeft
            xalign 0.0
            xpos 260
            spacing 8
            for i, item in enumerate(items, start=1):
                button:
                    minimum 600, 68
                    #idle_background "gui/button/choice_idle_background_1.png" focus_mask True
                    #hover_background "gui/button/choice_hover_background_1.png"
                    idle_background "gui/button/choice_idle_background_1.png" focus_mask True
                    hover_background "gui/button/choice_hover_background_1.png"
                    text item.caption #yalign .5
                    action item.action
                    at animated_button_show_left(i * time_delay)
#screen choice(items):
#    style_prefix "choice"
#    
#    vbox:
#        for i in items:
#            textbutton i.caption action [SetVariable("timeout", 10), SetVariable("timeout_label", None), Function(narrator.add_history, kind="adv", who="{b}>>>{/b}", what="{b}" + i.caption + "{/b}"), i.action]
#    if timeout_label is not None:
#        bar:
#            xalign 0.5
#            ypos 50
#            xsize 740
#            value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
#        timer timeout action [SetVariable("timeout", 10), SetVariable("timeout_label", None), Jump(timeout_label)]


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
  #  ypos 405
  #  ypos 700
    ypos 666
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "audio/menu/buttonhoversound.ogg"
    activate_sound"audio/menu/buttonactionsound.ogg"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


################################################################################

screen quick_menu():

    zorder 100

    if quick_menu:

        imagebutton auto "gui/button/pc/pc_back_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Rollback() at quickmenu_smooth
        imagebutton auto "gui/button/pc/pc_skip_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Skip() alternate Skip(fast=True, confirm=True) at quickmenu_smooth
        imagebutton auto "gui/button/pc/pc_auto_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Preference("auto-forward", "toggle") at quickmenu_smooth
        imagebutton auto "gui/button/pc/pc_qsave_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action QuickSave() at quickmenu_smooth
        imagebutton auto "gui/button/pc/pc_qload_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action QuickLoad() at quickmenu_smooth
        imagebutton auto "gui/button/pc/pc_hide_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action HideInterface() at quickmenu_smooth


## Данный код гарантирует, что экран быстрого меню будет показан в игре в любое
## время, если только игрок не скроет интерфейс.
init python:
    config.overlay_screens.append("quick_menu")
    
transform with_Blur:
    blur 10
    alpha 0.8
transform no_Blur:
    blur 0
    alpha 1.0
    
default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Экраны Главного и Игрового меню
################################################################################

## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

screen navigation():
    tag nav_screen
    on "show" action Function(renpy.show_layer_at, with_Blur, layer="master")
    on "hide" action Function(renpy.show_layer_at, no_Blur, layer="master")
    if main_menu:
        imagebutton idle "gui/button/back/back_1.png" hover "back_return" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Return() activate_sound "audio/menu/buttonactionsound.ogg" at rs_return
    else:
        add 'gui/menu/game_menu.png' at nav_menu
        imagebutton idle "gui/button/back/back_1.png" hover "back_return" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Return() activate_sound "audio/menu/buttonactionsound.ogg" at rs_return
        imagebutton auto "gui/menu/menu_relationships_%s.png" hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu('girls_menu') activate_sound "audio/menu/buttonactionsound.ogg" at nav_rs
        imagebutton auto "gui/menu/menu_gallery_%s.png"  hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu('gallery_list_all') activate_sound "audio/menu/buttonactionsound.ogg" at nav_gallery
        imagebutton auto "gui/menu/menu_save_%s.png" hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu("save") activate_sound "audio/menu/buttonactionsound.ogg" at nav_save
        imagebutton auto "gui/menu/menu_load_%s.png" hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu("load") activate_sound "audio/menu/buttonactionsound.ogg" at nav_load
        imagebutton auto "gui/menu/menu_options_%s.png" hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu("preferences") activate_sound "audio/menu/buttonactionsound.ogg" at nav_options
        
        imagebutton auto "gui/menu/menu_mainmenu_%s.png" hover_sound "audio/menu/buttonhoversound.ogg" action MainMenu() activate_sound "audio/menu/buttonactionsound.ogg" at nav_main
        imagebutton auto "gui/menu/menu_quit_%s.png" hover_sound "audio/menu/buttonhoversound.ogg" action Quit(confirm=not main_menu) activate_sound "audio/menu/buttonactionsound.ogg" at nav_quit
    
  #  imagebutton auto "gui/menu/menu_patreon_%s.webp" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action OpenURL("https://www.patreon.com/sabirow") activate_sound "audio/menu/buttonactionsound.ogg"


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

## Экран отношений, сердце, девушки

screen girls():
    zorder 100
    imagebutton idle "gui/button/navmenu/nav_1.png" hover "navmenu" hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu('navigation') activate_sound "audio/menu/buttonactionsound.ogg" at nav_navmenu

################################################################################

screen main_menu():
    tag menu
    add gui.main_menu_background
    add 'gui/mainmenu/bgmainmenu.png'
    add "gui/mainmenu/logomainmenu.png"
    imagebutton idle "gui/mainmenu/menu_play_idle.png" hover "menu_play_hover" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Start() activate_sound "audio/menu/buttonactionsound.ogg"
    imagebutton idle "gui/mainmenu/menu_load_idle.png" hover "menu_load_hover" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu("load") activate_sound "audio/menu/buttonactionsound.ogg"
    imagebutton idle "gui/mainmenu/menu_options_idle.png" hover "menu_options_hover" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu("preferences") activate_sound "audio/menu/buttonactionsound.ogg"
    imagebutton idle "gui/mainmenu/menu_extras_idle.png" hover "menu_extras_hover" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu("extras") activate_sound "audio/menu/buttonactionsound.ogg"
    imagebutton idle "gui/mainmenu/menu_quit_idle.png" hover "menu_quit_hover" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Quit(confirm=not main_menu) activate_sound "audio/menu/buttonactionsound.ogg"
    
    
    imagebutton idle "gui/mainmenu/menu_patreon.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action OpenURL("https://www.patreon.com/sabirow") activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright_patreon
    
    imagebutton idle "gui/mainmenu/button_itch.png" hover_sound "audio/menu/buttonhoversound.ogg" action OpenURL("https://sabirow.itch.io/cdr") activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright_url_button_1:
        ypos 204
    imagebutton idle "gui/mainmenu/button_discord.png" hover_sound "audio/menu/buttonhoversound.ogg" action OpenURL("https://discord.gg/kSREGQuhht") activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright_url_button_2:
        ypos 312

## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None, или "viewport", или "vpgrid", когда этот
## экран предназначается для использования с более чем одним дочерним экраном,
## включённым в него.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

#    if main_menu:
#        add gui.main_menu_background
#    else:
#        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Резервирует пространство для навигации.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation
#
#    textbutton _("Вернуться"):
#        style "return_button"
#
#        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

#style game_menu_label is gui_label #etoubralhz
#style game_menu_label_text is gui_label_text #etoubralhz

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    #background "gui/menu/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.

screen about():

    tag menu

    ## Этот оператор включает игровое меню внутрь этого экрана. Дочерний vbox
    ## включён в порт просмотра внутри экрана игрового меню.
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            ## gui.about обычно установлено в options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("使用 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 制作。\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

screen save():

    modal True
    zorder 2
    
    add 'gui/mainmenu/pref_black.png'
    imagebutton idle "gui/button/back/back_1.png" hover "back_return" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Return() activate_sound "audio/menu/buttonactionsound.ogg" at rs_return_nav
    
    add 'gui/mainmenu/save_text.png'
    use file_slots(_(""))


screen load():

    modal True
    zorder 2
    
    tag menu
    if main_menu:
        add 'pref_bg'
        add 'gui/mainmenu/pref_black.png' alpha 0.8

    else:
        add 'gui/mainmenu/pref_black.png'
        
    add 'gui/mainmenu/load_text.png'
    imagebutton idle "gui/button/back/back_1.png" hover "back_return" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Return() activate_sound "audio/menu/buttonactionsound.ogg" at rs_return_nav
    
    use file_slots(_(""))
    
image pref_bg = Movie(size=(1920,1080), channel ="movie", play="gui/mainmenu/pref_bg.webm", loop=True)

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动"), quick=_("快速"))

    fixed:

        ## Это гарантирует, что ввод будет принимать enter перед остальными
        ## кнопками.
        order_reverse True

        ## Номер страницы, который может быть изменён посредством клика на
        ## кнопку.
        button at saveloadslot:
            style "page_label"

            key_events True
            if renpy.variant("pc"):
                xalign 0.5
                ypos 140
            if renpy.variant("touch"):
                xpos 0.5
                ypos 140
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value
        ## Таблица слотов.
        grid 3 2:
            style_prefix "slot"
            if renpy.variant("pc"):
                xalign 0.5
                yalign 0.5
            if renpy.variant("touch"):
                xalign 0.5
                yalign 0.5
            spacing 40#gui.slot_spacing

            for i in range(6):

                $ slot = i + 1
                
                button at saveloadslot:
                    action FileAction(slot)
                    
                    xysize (430, 290)
                    hover_background "gui/menu/panel_hover.png"
                    background "gui/menu/panel_save.png"
                    insensitive_background "gui/menu/panel.png"
                    
                    add FileScreenshot(slot) xalign 0.5 xsize 400 ysize 224 ypos 10
                    add "gui/menu/panel_save_dirt.png" xalign 0.5 yalign 0.5
                    
                    text FileTime(slot, format=_("{#file_time}%d 年 %m 月 %d 日 %H:%M")):
                        style "slot_time_text"
                        ypos 246
                        xalign 0.5
                        
                    
                    #text FileSaveName(slot):
                        #style "slot_name_text"
                    
                    key "save_delete" action FileDelete(slot)

        ## Кнопки для доступа к другим страницам.
        hbox:
            xalign 0.5
            ypos 920
            spacing 10

            imagebutton at saveloadtab:
                idle "gui/menu/prev_tab_idle.png"
                action FilePagePrevious()
                yalign 0.5
                xpos -8

            if config.has_autosave:
                button at saveloadslot:
                    style "slot_button"
                    text "A" align (0.5, 0.5) style "slot_button_text"
                    action FilePage("auto")

            if config.has_quicksave:
                button at saveloadslot:
                    style "slot_button"
                    text "Q" align (0.5, 0.5) style "slot_button_text"
                    action FilePage("quick")

            for page in range(1, 7):
                button at saveloadslot:
                    style "slot_button"
                    text "[page]" align (0.5, 0.5) style "slot_button_text"
                    action FilePage(page)

            imagebutton at saveloadtab:
                idle "gui/menu/next_tab_idle.png"
                yalign 0.5
                xpos 8
                action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button2_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 0
    ypadding 0

style page_label_text:
    size 38
    text_align 0.5
    color "#ffffff"
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    #properties gui.button_properties("slot_button")
    xysize (80, 80)
    idle_background "gui/menu/save_tab_unselected.png"
    hover_background "gui/menu/save_tab_selected.png"
    selected_idle_background "gui/menu/save_tab_selected.png"

style slot_button1_text:
    font "tl/schinese/schinese.ttf"
    size 32
    color "#ffffff"

style slot_button2_text:
    #properties gui.button_text_properties("slot_button")
    #font "gui/ttf/Titillium-Regular.otf"
    size 23
    color "#ffffff"
    xalign 1.0
    yalign 0.2


## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

## Экран Экстрас
screen extras():
    tag menu
    modal True
    zorder 2
    add 'pref_bg'
    #add "gui/mainmenu/extras_text.png"
    imagebutton idle "gui/extras/extras_return.png" action Return()
    add "gui/extras/extras_window.png"
    imagebutton auto "gui/extras/extras_gallery_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu('gallery_list_all') activate_sound "audio/menu/buttonactionsound.ogg"
    imagebutton auto "gui/extras/extras_credits_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Jump('credits') activate_sound "audio/menu/buttonactionsound.ogg"
    #imagebutton auto "gui/mainmenu/return_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Return() activate_sound "audio/menu/buttonactionsound.ogg"

## Экран задач/телефона
screen phone1():
    zorder 100
    imagebutton idle "gui/button/tasks/tasks_1.png" hover "tasksmenu" hover_sound "audio/menu/buttonhoversound.ogg" action ShowMenu('tasks1') activate_sound "audio/menu/buttonactionsound.ogg" at nav_tasksmenu

screen tasks1():
    tag menu
    on "show" action Function(renpy.show_layer_at, with_Blur, layer="master")
    on "hide" action Function(renpy.show_layer_at, no_Blur, layer="master")
    modal True
    zorder 2
    imagebutton idle "gui/button/back/back_1.png" hover "back_return" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Return() activate_sound "audio/menu/buttonactionsound.ogg" at rs_return_nav
    add "gui/notes/phonenote.webp"
    if school_stolen_time == 0:
        add "gui/notes/times1/1.webp"
    if school_stolen_time == 1:
        add "gui/notes/times1/2.webp"
    if school_stolen_time == 2:
        add "gui/notes/times1/3.webp"
    if school_stolen_time == 3:
        add "gui/notes/times1/4.webp"
    if school_stolen_time == 4:
        add "gui/notes/times1/5.webp"
    if school_stolen_time == 5:
        add "gui/notes/times1/6.webp"
    if school_stolen_time == 6:
        add "gui/notes/times1/7.webp"
    if school_stolen_time == 7:
        add "gui/notes/times1/8.webp"

    if school_stolen_chara_daimez == True:
        add "gui/notes/school_stolen/task1f.webp"
    else:
        add "gui/notes/school_stolen/task1.webp"
    if school_stolen_chara_leah == True:
        add "gui/notes/school_stolen/task2f.webp"
    else:
        add "gui/notes/school_stolen/task2.webp"
    if school_stolen_chara_ken == True:
        add "gui/notes/school_stolen/task3f.webp"
    else:
        add "gui/notes/school_stolen/task3.webp"
    if school_stolen_chara_ry == True:
        add "gui/notes/school_stolen/task4f.webp"
    else:
        add "gui/notes/school_stolen/task4.webp"
    if school_stolen_chara_da == True:
        add "gui/notes/school_stolen/task5f.webp"
    else:
        add "gui/notes/school_stolen/task5.webp"
        
    if school_stolen_locker == True and school_stolen_locker_daimez == True:
        add "gui/notes/school_stolen/task6f.webp"
    elif school_stolen_locker == True and school_stolen_locker_daimez == False:
        add "gui/notes/school_stolen/task6.webp"
        
    if school_stolen_locker == True and school_stolen_locker_ry == True:
        add "gui/notes/school_stolen/task7f.webp"
    elif school_stolen_locker == True and school_stolen_locker_ry == False:
        add "gui/notes/school_stolen/task7.webp"
        
## Экран опций

screen preferences():

    tag menu
    modal True
    zorder 2
    if main_menu:
        add 'pref_bg'
        add 'gui/mainmenu/pref_black.png' alpha 0.8
    else:
        add 'gui/mainmenu/pref_black.png'
    add 'gui/options/options_text.png'

    if _preferences.language == 'spanish':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'portugese':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'french':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'german':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'italian':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'polish':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'czech':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'dutch':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'japanese':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'korean':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'thai':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'vietnamese':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'indonesian':
        add "gui/options/lang_warning_using_mt.webp"
    elif _preferences.language == 'turkish':
        add "gui/options/lang_warning_using_mt.webp"
    
    imagebutton idle "gui/button/back/back_1.png" hover "back_return" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Return() activate_sound "audio/menu/buttonactionsound.ogg" at rs_return_nav
    
    imagebutton auto "gui/options/general_%s.png" action ShowMenu('preferences') hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at options_general
    imagebutton auto "gui/options/audio_%s.png" action ShowMenu('preferences_audio') hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at options_audio
    
    imagebutton auto "gui/options/switch_sitt_%s.png" selected preferences.fullscreen action If(preferences.fullscreen, Preference("display", "window"), Preference("display", "fullscreen")) hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright:
        xpos 740
        ypos 289
        
    imagebutton auto "gui/options/switch_sitt_%s.png" action Preference("skip", "toggle") hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright:
        xpos 740
        ypos 418
        
    imagebutton auto "gui/options/switch_sitt_%s.png" action Preference("after choices", "toggle") hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright:
        xpos 740
        ypos 480
    
    imagebutton auto "gui/options/switch_sitt_%s.png" action InvertSelected(Preference("transitions", "toggle")) hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright:
        xpos 740
        ypos 542
            

    bar value Preference("text speed") at choice_bright_2:
        xsize 430
        ysize 60
        yanchor 0.5
        xpos 1400
        ypos 701
        left_bar Frame("gui/bar/options_left.png")
        right_bar Frame("gui/bar/options_right.png")
        thumb None

    bar value Preference("auto-forward time") at choice_bright_2:
        xsize 430
        ysize 60
        yanchor 0.5
        xpos 1400
        ypos 763
        left_bar Frame("gui/bar/options_left.png")
        right_bar Frame("gui/bar/options_right.png")
        thumb None

    imagebutton:
        if _preferences.language == 'schinese':
            idle "gui/options/imgbtn_lang_schinese.png"
        elif _preferences.language == 'russian':
            idle "gui/options/imgbtn_lang_russian.png"
            
        elif _preferences.language == 'spanish':
            idle "gui/options/imgbtn_lang_spanish.png"
        elif _preferences.language == 'portugese':
            idle "gui/options/imgbtn_lang_portugese.png"
        elif _preferences.language == 'french':
            idle "gui/options/imgbtn_lang_french.png"
        elif _preferences.language == 'german':
            idle "gui/options/imgbtn_lang_german.png"
        elif _preferences.language == 'italian':
            idle "gui/options/imgbtn_lang_italian.png"
        elif _preferences.language == 'polish':
            idle "gui/options/imgbtn_lang_polish.png"
        elif _preferences.language == 'czech':
            idle "gui/options/imgbtn_lang_czech.png"
        elif _preferences.language == 'dutch':
            idle "gui/options/imgbtn_lang_dutch.png"
        elif _preferences.language == 'japanese':
            idle "gui/options/imgbtn_lang_japanese.png"
        elif _preferences.language == 'korean':
            idle "gui/options/imgbtn_lang_korean.png"
        elif _preferences.language == 'thai':
            idle "gui/options/imgbtn_lang_thai.png"
        elif _preferences.language == 'vietnamese':
            idle "gui/options/imgbtn_lang_vietnamese.png"
        elif _preferences.language == 'indonesian':
            idle "gui/options/imgbtn_lang_indonesian.png"
        elif _preferences.language == 'turkish':
            idle "gui/options/imgbtn_lang_turkish.png"
            
        else:
            idle "gui/options/imgbtn_lang_english.png"
            
        hover_sound "audio/menu/buttonhoversound.ogg"
        activate_sound "audio/menu/buttonactionsound.ogg"
        at choice_bright
        xpos 740
        ypos 795
        
        #action ToggleFocus('list')
        action ShowMenu("language_selector")

    nearrect:
        
        focus "list"
 
        add "gui/options/language_box.png" at language_box

 
    nearrect:
        
        focus "list"
        
        has vbox at language_buttons
        
        dismiss action ClearFocus("list")
        
   #     imagebutton idle "gui/options/lang/imgbtn_lang_english.png" action [Language(None), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_russian.png" action [Language('russian'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_schinese.png" action [Language('schinese'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_spanish.png" action [Language('spanish'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_portugese.png" action [Language('schinese'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_french.png" action [Language('french'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_german.png" action [Language('schinese'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_italian.png" action [Language('italian'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_german.png" action [Language('german'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_ukrainian.png" action [Language('ukrainian'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_czech.png" action [Language('czech'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
    #    imagebutton idle "gui/options/lang/imgbtn_lang_dutch.png" action [Language('dutch'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
    #    imagebutton idle "gui/options/lang/imgbtn_lang_japanese.png" action [Language('japanese'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_korean.png" action [Language('korean'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_thai.png" action [Language('thai'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_vietnamese.png" action [Language('vietnamese'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_indonesian.png" action [Language('indonesian'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_turkish.png" action [Language('turkish'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
   #     imagebutton idle "gui/options/lang/imgbtn_lang_hindi.png" action [Language('schinese'), ClearFocus("list")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright


screen preferences():
    variant "touch"
    tag menu
    modal True
    zorder 2
    if main_menu:
        add 'pref_bg'
        add 'gui/mainmenu/pref_black.png' alpha 0.8
    else:
        add 'gui/mainmenu/pref_black.png'
    add 'gui/options/m_options_text.png'
    imagebutton idle "gui/button/back/back_1.png" hover "back_return" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Return() activate_sound "audio/menu/buttonactionsound.ogg" at rs_return_nav
    
    imagebutton auto "gui/options/general_%s.png" action ShowMenu('preferences') hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at options_general
    imagebutton auto "gui/options/audio_%s.png" action ShowMenu('preferences_audio') hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at options_audio
            
    imagebutton auto "gui/options/switch_sitt_%s.png" action Preference("skip", "toggle") hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright:
        xpos 740
        ypos 289
        
    imagebutton auto "gui/options/switch_sitt_%s.png" action Preference("after choices", "toggle") hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright:
        xpos 740
        ypos 351
    
    imagebutton auto "gui/options/switch_sitt_%s.png" action InvertSelected(Preference("transitions", "toggle")) hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright:
        xpos 740
        ypos 413
            

    bar value Preference("text speed") at choice_bright_2:
        xsize 430
        ysize 60
        yanchor 0.5
        xpos 1400
        ypos 572
        left_bar Frame("gui/bar/options_left.png")
        right_bar Frame("gui/bar/options_right.png")
        thumb None

    bar value Preference("auto-forward time") at choice_bright_2:
        xsize 430
        ysize 60
        yanchor 0.5
        xpos 1400
        ypos 634
        left_bar Frame("gui/bar/options_left.png")
        right_bar Frame("gui/bar/options_right.png")
        thumb None

    imagebutton:
        if _preferences.language == 'schinese':
            idle "gui/options/imgbtn_lang_schinese.png"
        elif _preferences.language == 'russian':
            idle "gui/options/imgbtn_lang_russian.png"
            
        elif _preferences.language == 'spanish':
            idle "gui/options/imgbtn_lang_spanish.png"
        elif _preferences.language == 'portugese':
            idle "gui/options/imgbtn_lang_portugese.png"
        elif _preferences.language == 'french':
            idle "gui/options/imgbtn_lang_french.png"
        elif _preferences.language == 'german':
            idle "gui/options/imgbtn_lang_german.png"
        elif _preferences.language == 'italian':
            idle "gui/options/imgbtn_lang_italian.png"
        elif _preferences.language == 'polish':
            idle "gui/options/imgbtn_lang_polish.png"
        elif _preferences.language == 'czech':
            idle "gui/options/imgbtn_lang_czech.png"
        elif _preferences.language == 'dutch':
            idle "gui/options/imgbtn_lang_dutch.png"
        elif _preferences.language == 'japanese':
            idle "gui/options/imgbtn_lang_japanese.png"
        elif _preferences.language == 'korean':
            idle "gui/options/imgbtn_lang_korean.png"
        elif _preferences.language == 'thai':
            idle "gui/options/imgbtn_lang_thai.png"
        elif _preferences.language == 'vietnamese':
            idle "gui/options/imgbtn_lang_vietnamese.png"
        elif _preferences.language == 'indonesian':
            idle "gui/options/imgbtn_lang_indonesian.png"
        elif _preferences.language == 'turkish':
            idle "gui/options/imgbtn_lang_turkish.png"
            
        else:
            idle "gui/options/imgbtn_lang_english.png"
            
        hover_sound "audio/menu/buttonhoversound.ogg"
        activate_sound "audio/menu/buttonactionsound.ogg"
        at choice_bright
        xpos 740
        ypos 666
        
        #action ToggleFocus('list')
        action ShowMenu("language_selector")

    nearrect:
        
        focus "list"
 
        add "gui/options/language_box.png" at language_box

 
    nearrect:
        
        focus "list"
        
        has vbox at language_buttons
        
        dismiss action ClearFocus("list")
        
screen language_selector():
    zorder 3
    modal True
    imagebutton idle "gui/options/black_tr.webp" action Hide("language_selector") activate_sound "audio/menu/buttonactionsound.ogg"
    add "gui/options/lang_selector.webp"
    add "gui/options/lang_warning.webp"
    hbox:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 900

        vbox:
            spacing 8
            yalign 0.5
            imagebutton idle "gui/options/lang/imgbtn_lang_english.png" action [Language(None), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_russian.png" action [Language('russian'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_schinese.png" action [Language('schinese'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_spanish.png" action [Language('spanish'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_portugese.png" action [Language('portugese'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_french.png" action [Language('french'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_german.png" action [Language('german'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_italian.png" action [Language('italian'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_polish.png" action [Language('polish'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            #imagebutton idle "gui/options/lang/imgbtn_lang_ukrainian.png" action [Language('ukrainian'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_czech.png" action [Language('czech'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_dutch.png" action [Language('dutch'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_japanese.png" action [Language('japanese'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_korean.png" action [Language('korean'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_thai.png" action [Language('thai'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_vietnamese.png" action [Language('vietnamese'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_indonesian.png" action [Language('indonesian'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_turkish.png" action [Language('turkish'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            #imagebutton idle "gui/options/lang/imgbtn_lang_hindi.png" action [Language('hindi'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            
            
###################################### LANGUAGE SELECTOR --- MOBILE
            
screen language_selector():
    variant "touch"
    zorder 3
    modal True
    imagebutton idle "gui/options/black_tr.webp" action Hide("language_selector") activate_sound "audio/menu/buttonactionsound.ogg"
    add "gui/options/lang_selector_m.webp"
    add "gui/options/lang_warning.webp"
    hbox:
        xalign 0.76
        yalign 0.5
        xsize 1000
        ysize 700

        vbox:
            spacing 26
            yalign 0.5
            imagebutton idle "gui/options/lang/imgbtn_lang_english.png" action [Language(None), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_russian.png" action [Language('russian'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_schinese.png" action [Language('schinese'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_spanish.png" action [Language('spanish'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_portugese.png" action [Language('portugese'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_french.png" action [Language('french'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_german.png" action [Language('german'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_italian.png" action [Language('italian'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_polish.png" action [Language('polish'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
        vbox:
            spacing 26
            yalign 0.5
            imagebutton idle "gui/options/lang/imgbtn_lang_czech.png" action [Language('czech'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_dutch.png" action [Language('dutch'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_japanese.png" action [Language('japanese'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_korean.png" action [Language('korean'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_thai.png" action [Language('thai'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_vietnamese.png" action [Language('vietnamese'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_indonesian.png" action [Language('indonesian'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            imagebutton idle "gui/options/lang/imgbtn_lang_turkish.png" action [Language('turkish'), Hide("language_selector")] hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright
            


transform language_box:
    on show:
        ease 0.3 xsize 500 ysize 760    ###  if 3 lang = 180 / +60 for next
    on hide:
        ease 0.3 ysize 1
                
transform language_buttons:
    #subpixel True
    
    on idle:
        ease .3 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.4)
    on show:
        ease 0.3 ypos 0 alpha 1.0 ysize 760 xsize 500    ###  if 3 lang = 180 / +60 for next / 760 if 40px for 19 lang
    on hide:
        ease 0.2 ypos -50 alpha 0.0 ysize 60

transform gallery_list_buttons:
    #subpixel True
    
    on idle:
        ease .3 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    on hover:
        ease .2 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.4)
    on show:
        ease 0.3 ypos 0 alpha 1.0 ysize 150
    on hide:
        ease 0.2 ypos -50 alpha 0.0 ysize 60
        

screen preferences_audio():

    tag menu
    modal True
    zorder 2
    if main_menu:
        add 'pref_bg'
        add 'gui/mainmenu/pref_black.png' alpha 0.8
    else:
        add 'gui/mainmenu/pref_black.png'
    add 'gui/options/options_text_audio.png'
    imagebutton idle "gui/button/back/back_1.png" hover "back_return" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Return() activate_sound "audio/menu/buttonactionsound.ogg" at rs_return_nav
    
    imagebutton auto "gui/options/general_%s.png" action ShowMenu('preferences') hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at options_general
    imagebutton auto "gui/options/audio_%s.png" action ShowMenu('preferences_audio') hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at options_audio

    bar value Preference("music volume") at choice_bright_2:
        xsize 430
        ysize 60
        yanchor 0.5
        xpos 1400
        ypos 256
        left_bar Frame("gui/bar/options_left.png")
        right_bar Frame("gui/bar/options_right.png")
        thumb None
        
    bar value Preference("sound volume") at choice_bright_2:
        xsize 430
        ysize 60
        yanchor 0.5
        xpos 1400
        ypos 318
        left_bar Frame("gui/bar/options_left.png")
        right_bar Frame("gui/bar/options_right.png")
        thumb None
        
    bar value Preference("voice volume") at choice_bright_2:
        xsize 430
        ysize 60
        yanchor 0.5
        xpos 1400
        ypos 380
        left_bar Frame("gui/bar/options_left.png")
        right_bar Frame("gui/bar/options_right.png")
        thumb None
        
    imagebutton auto "gui/options/switch_sitt_%s.png" action Preference("all mute", "toggle") hover_sound "audio/menu/buttonhoversound.ogg" activate_sound "audio/menu/buttonactionsound.ogg" at choice_bright:
        xpos 740
        ypos 412
    
    

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 600

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

## Экран истории ###############################################################
##
## Этот экран показывает игроку историю диалогов. Хотя в этом экране нет ничего
## особенного, он имеет доступ к истории диалогов, хранимом в _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Избегайте предсказывания этого экрана, так как он может быть очень
    ## массивным.
    predict False

    use game_menu(_("历史记录"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Это всё правильно уравняет, если history_height будет
                ## установлен на None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Берёт цвет из who параметра персонажа, если он
                        ## установлен.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("历史记录为空。")


## Это определяет, какие теги могут отображаться на экране истории.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Экран помощи ################################################################
##
## Экран, дающий информацию о клавишах управления. Он использует другие экраны
## (keyboard_help, mouse_help, и gamepad_help), чтобы показывать актуальную
## помощь.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并显示界面。")

    hbox:
        label _("空格")
        text _("推进对话，不进行选择。")

    hbox:
        label _("方向键")
        text _("操作界面。")

    hbox:
        label _("Esc")
        text _("打开游戏菜单。")

    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("上翻页键")
        text _("回退到之前的对话。")

    hbox:
        label _("下翻页键")
        text _("快进到之后的对话。")

    hbox:
        label "H"
        text _("隐藏界面。")

    hbox:
        label "S"
        text _("截取屏幕截图。")

    hbox:
        label "V"
        text _("切换辅助 {a=https://www.renpy.org/l/voicing}语音朗读{/a}。")

    hbox:
        label "Shift+A"
        text _("打开无障碍菜单。")


screen mouse_help():

    hbox:
        label _("鼠标左键")
        text _("推进对话并显示界面。")

    hbox:
        label _("鼠标中键")
        text _("隐藏界面。")

    hbox:
        label _("鼠标右键")
        text _("打开游戏菜单。")

    hbox:
        label _("滚轮上滚\n点击回退侧")
        text _("回退到之前的对话。")

    hbox:
        label _("滚轮下滚")
        text _("快进到之后的对话。")


screen gamepad_help():

    hbox:
        label _("RT 松机\nA／底部按键")
        text _("推进对话并显示界面。")

    hbox:
        label _("LT 松机\nLB 肩键")
        text _("回退到之前的对话。")

    hbox:
        label _("RB 肩键")
        text _("快进到之后的对话。")


    hbox:
        label _("十字键、摇杆")
        text _("操作界面。")

    hbox:
        label _("开始、指南")
        text _("打开游戏菜单。")

    hbox:
        label _("Y／顶部按键")
        text _("隐藏界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Дополнительные экраны
################################################################################


## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет спросить у игрока вопрос
## Да или Нет.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("是") action yes_action
                textbutton _("否") action no_action

    ## Правый клик и esc, как ответ "Нет".
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
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Экран индикатора пропуска ###################################################
##
## Экран индикатора пропуска появляется для того, чтобы показать, что идёт
## пропуск.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

#screen skip_indicator():

#    zorder 100
#    style_prefix "skip"

#    frame:

#        hbox:
#            spacing 9

#            text _("Skipping")
#
 #           text "▸" at delayed_blink(0.0, 0.5) style "skip_triangle"
#            text "▸" at delayed_blink(0.2, 0.5) style "skip_triangle"
#            text "▸" at delayed_blink(0.4, 0.5) style "skip_triangle"


## Эта трансформация используется, чтобы мигать стрелками одна за другой.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


## Экран уведомлений ###########################################################
##
## Экран уведомлений используется, чтобы показать игроку оповещение. (Например,
## когда игра автосохранилась, или был сделан скриншот)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Мобильные варианты
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Раз мышь может не использоваться, мы заменили быстрое меню версией,
## использующей меньше кнопок, но больших по размеру, чтобы их было легче
## касаться.
screen quick_menu():
    variant "touch"
    
    zorder 100

    if quick_menu:

        imagebutton auto "gui/button/m/m_back_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Rollback() at quickmenu_smooth
        imagebutton auto "gui/button/m/m_skip_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Skip() alternate Skip(fast=True, confirm=True) at quickmenu_smooth
        imagebutton auto "gui/button/m/m_auto_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action Preference("auto-forward", "toggle") at quickmenu_smooth
        imagebutton auto "gui/button/m/m_qsave_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action QuickSave() at quickmenu_smooth
        imagebutton auto "gui/button/m/m_qload_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action QuickLoad() at quickmenu_smooth
        imagebutton auto "gui/button/m/m_hide_%s.png" focus_mask True hover_sound "audio/menu/buttonhoversound.ogg" action HideInterface() at quickmenu_smooth

       #hbox:
            #style_prefix "quick"

            #xalign 0.5
            #yalign 1.0

            #textbutton _("Back") action Rollback()
            #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("Auto") action Preference("auto-forward", "toggle")
            #textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    #background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    #background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600
