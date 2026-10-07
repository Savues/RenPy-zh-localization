image guga_tablet = "mod/images/GugaTablet.png"

screen cheatmodnavigation():
    modal True
    add Transform("guga_tablet", size=(2500, 2050)) alpha 0.95 xalign 0.5 yalign 0.5
    text "{size=80}Gugatron 作弊面板" color "#00bfff" font "mod/Monster Racing - Personal Used.otf" xcenter 0.5 ypos 145 outlines [(3, "#000", 0, 3)]

screen cheatmenu():
    tag menu
    use cheatmodnavigation
    vpgrid:
        xcenter 0.5
        ypos 260
        cols 5
        xspacing 10
        yspacing 5
        vbox:
            spacing 10
            text"{color=#D8DB09FF}{size=20}卡莉 信任" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("k_trust", 100)
                text "[gr][k_trust]{/color=#D8DB09FF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#DB103CFF}{size=20}卡莉 欲望" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("k_desire", 100)
                text "[gr][k_desire]{/color=#DB103CFF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]
        vbox:
            spacing 10
            text"{color=#E71EC6FF}{size=20}卡莉 爱意" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("k_love", 100)
                text "[gr][k_love]{/color=#E71EC6FF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0,2)]

        vbox:
            spacing 10
            text"{color=#0EDF8FFF}{size=20}卡莉 友情" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("k_friend", 100)
                text "[gr][k_friend]{/color=#0EDF8FFF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]
    
        vbox:
            spacing 10
            text"{color=#2110C0DE}{size=20}卡莉 焦虑" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("k_anxiety", 100)
                text "[gr][k_anxiety]{/color=#2110C0DE}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#D8DB09FF}{size=20}劳拉 信任" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("l_trust", 100)
                text "[gr][l_trust]{/color=#D8DB09FF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#DB103CFF}{size=20}劳拉 欲望" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("l_desire", 100)
                text "[gr][l_desire]{/color=#DB103CFF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]
            
        vbox:
            spacing 10
            text"{color=#E71EC6FF}{size=20}劳拉 爱意" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("l_love", 100)
                text "[gr][l_love]{/color=#E71EC6FF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#0EDF8FFF}{size=20}劳拉 友情" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("l_friend", 100)
                text "[gr][l_friend]{/color=#0EDF8FFF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#2110C0DE}{size=20}劳拉 焦虑" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("l_anxiety", 100)
                text "[gr][l_anxiety]{/color=#2110C0DE}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#D8DB09FF}{size=20}雪莉 信任" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("s_trust", 100)
                text "[gr][s_trust]{/color=#D8DB09FF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#DB103CFF}{size=20}雪莉 欲望" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("s_desire", 100)
                text "[gr][s_desire]{/color=#DB103CFF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#E71EC6FF}{size=20}雪莉 爱意" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("s_love", 100)
                text "[gr][s_love]{/color=#E71EC6FF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#0EDF8FFF}{size=20}雪莉 友情" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("s_friend", 100)
                text "[gr][s_friend]{/color=#0EDF8FFF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#2110C0DE}{size=20}雪莉 焦虑" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("s_anxiety", 100)
                text "[gr][s_anxiety]{/color=#2110C0DE}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#D8DB09FF}{size=20}伊芙 信任" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("e_trust", 100)
                text "[gr][e_trust]{/color=#D8DB09FF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 10
            text"{color=#DB103CFF}{size=20}伊芙 欲望" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("e_desire", 100)
                text "[gr][e_desire]{/color=#DB103CFF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]
        vbox:
            spacing 10
            text"{color=#E71EC6FF}{size=20}伊芙 爱意" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("e_love", 100)
                text "[gr][e_love]{/color=#E71EC6FF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0,2)]

        vbox:
            spacing 10
            text"{color=#0EDF8FFF}{size=20}伊芙 友情" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("e_friend", 100)
                text "[gr][e_friend]{/color=#0EDF8FFF}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]
    
        vbox:
            spacing 10
            text"{color=#2110C0DE}{size=20}伊芙 焦虑" font "mod/Monster Racing - Personal Used.otf" outlines [(2, "#000", 0, 2)]
            fixed:
                xysize(315,80)
                bar value VariableValue("e_anxiety", 100)
                text "[gr][e_anxiety]{/color=#2110C0DE}" xcenter 0.5 ycenter 0.3 outlines [(2, "#000", 0, 2)]


    textbutton "{size=50}返回" xalign 0.5 yalign 0.85 text_color "#F0F0F0" text_hover_color "#75E6DA" action Return()

    textbutton ("图库解锁：[rd]关" if not unlocked else "图库解锁：[gr]开") action [SetVariable("unlocked", not unlocked), Function(toggle_gallery)] xalign 0.7 yalign 0.75 text_size 50 text_color "#F0F0F0" text_hover_color "#75E6DA"

    textbutton "改名" action ui.callsinnewcontext("rename") xalign 0.3 yalign 0.75 text_size 50 text_color "#F0F0F0" text_hover_color "#75E6DA"


    imagebutton:
        align(0.10,0.85)
        idle Transform("mod/images/F95/F95_Button.png", zoom=0.8)
        hover Transform("mod/images/F95/F95_Button_Hover.png", zoom=0.8)
        action OpenURL("https://f95zone.to/members/gugatron.328002/")

    imagebutton:
        align(0.90,0.85)
        idle Transform("mod/images/Patreon/Patreon_Button.png", zoom=0.8)
        hover Transform("mod/images/Patreon/Patreon_Button_Hover.png", zoom=0.8)
        action OpenURL("https://patreon.com/gugatron")





label rename:
    $ ui.text("{size=+10}{font=fonts/DCC - Ash.otf}请输入名字(默认：约翰){/font}{/size}", xalign=0.5, yalign=0.4)
    $ ui.input('', xalign=0.5, yalign=0.5)
    $ player_name = ui.interact()
    if player_name == '':
        $ player_name = '约翰'
    $ ui.text("{size=+10}{font=fonts/DCC - Ash.otf}请输入姓氏(默认：休斯顿){/font}{/size}", xalign=0.5, yalign=0.4)
    $ ui.input('', xalign=0.5, yalign=0.5)
    $ player_lastname = ui.interact()
    if player_lastname == '':
        $ player_lastname = '休斯顿'

    return