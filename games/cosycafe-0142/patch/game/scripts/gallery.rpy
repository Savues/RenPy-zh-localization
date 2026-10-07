screen gallery():

    tag menu
    use game_menu("画廊"):
        
        fixed:

            vbox:

                xalign 0.0
                yalign 0.0
                spacing 15

                textbutton _("露西") action Show("gallery_lucy", transition = dissolve) text_size 25

                textbutton _("维多利亚") action Show("gallery_victoria", transition = dissolve) text_size 25

                textbutton _("晓月") action Show("gallery_akatsuki", transition = dissolve) text_size 25

                textbutton _("莎拉") text_size 25

                textbutton _("瑞秋") text_size 25

                textbutton _("汉娜") text_size 25

                textbutton _("校长") action Show("gallery_headmistress", transition = dissolve) text_size 25

                textbutton _("高村小姐") action Show("gallery_taka", transition = dissolve) text_size 25

                textbutton _("明里") text_size 25

                textbutton _("凯瑟琳") text_size 25

                textbutton _("组合") action Show("gallery_group", transition = dissolve) text_size 25

#/////////////////////////////////////////////
#   LUCY GALLERY
#/////////////////////////////////////////////
screen gallery_lucy():

    tag menu
    use game_menu("露西"):
        
        # Character menu
        vbox:

            xalign 0.0
            yalign 0.0
            spacing 15

            textbutton _("露西") action Show("gallery_lucy", transition = dissolve) text_size 25

            textbutton _("维多利亚") action Show("gallery_victoria", transition = dissolve) text_size 25

            textbutton _("晓月") action Show("gallery_akatsuki", transition = dissolve) text_size 25

            textbutton _("莎拉") text_size 25

            textbutton _("瑞秋") text_size 25

            textbutton _("汉娜") text_size 25

            textbutton _("校长") action Show("gallery_headmistress", transition = dissolve) text_size 25

            textbutton _("高村小姐") action Show("gallery_taka", transition = dissolve) text_size 25

            textbutton _("明里") text_size 25

            textbutton _("凯瑟琳") text_size 25

            textbutton _("组合") action Show("gallery_group", transition = dissolve) text_size 25

        vbox:

            
            # xalign 0.0
            yalign 0.0
            xpos 230
            spacing 15

            hbox:
                spacing 15

            # Lucy1 -----------------------------------------------
                if persistent.gallery_lucy1 == True:
                    imagebutton auto "gallery_lucy1_%s":
                        focus_mask True
                        action Replay("replay_lucy1", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Lucy2 -----------------------------------------------
                if persistent.gallery_lucy2 == True:
                    imagebutton auto "gallery_lucy2_%s":
                        focus_mask True
                        action Replay("replay_lucy2", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Lucy3 -----------------------------------------------
                if persistent.gallery_lucy3 == True:
                    imagebutton auto "gallery_lucy3_%s":
                        focus_mask True
                        action Replay("replay_lucy3", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True



            hbox:
                spacing 15

            # Lucy4 -----------------------------------------------
                if persistent.gallery_lucy4 == True:
                    imagebutton auto "gallery_lucy4_%s":
                        focus_mask True
                        action Replay("replay_lucy4", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Lucy5 -----------------------------------------------
                if persistent.gallery_lucy5 == True:
                    imagebutton auto "gallery_lucy5_%s":
                        focus_mask True
                        action Replay("replay_lucy5", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Lucy6 -----------------------------------------------
                if persistent.gallery_lucy6 == True:
                    imagebutton auto "gallery_lucy6_%s":
                        focus_mask True
                        action Replay("replay_lucy6", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True
                

            hbox:
                spacing 15

            # Lucy7 -----------------------------------------------
                if persistent.gallery_lucy7 == True:
                    imagebutton auto "gallery_lucy7_%s":
                        focus_mask True
                        action Replay("replay_lucy7", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # # Lucy2 -----------------------------------------------
            #     if persistent.gallery_lucy2 == True:
            #         imagebutton auto "gallery_lucy2_%s":
            #             focus_mask True
            #             action Replay("replay_lucy2", locked=False)
            #     else:
            #         imagebutton auto "gallery_locked_%s":
            #             focus_mask True

            # # Lucy3 -----------------------------------------------
            #     if persistent.gallery_lucy1 == True:
            #         imagebutton auto "gallery_lucy1_%s":
            #             focus_mask True
            #             action Replay("replay_lucy1", locked=False)
            #     else:
            #         imagebutton auto "gallery_locked_%s":
            #             focus_mask True

        # hbox:
        #         style_prefix "page"

        #         xalign 0.5
        #         yalign 1.0

        #         spacing gui.page_spacing

        #         textbutton _("Lucy") action Show("gallery_lucy")

        #         textbutton _("Victoria") action Show("gallery_victoria")

#/////////////////////////////////////////////
#   VICTORIA GALLERY
#/////////////////////////////////////////////
screen gallery_victoria():

    tag menu
    use game_menu("维多利亚"):
        
        # Character menu
        vbox:

            xalign 0.0
            yalign 0.0
            spacing 15

            textbutton _("露西") action Show("gallery_lucy", transition = dissolve) text_size 25

            textbutton _("维多利亚") action Show("gallery_victoria", transition = dissolve) text_size 25

            textbutton _("晓月") action Show("gallery_akatsuki", transition = dissolve) text_size 25

            textbutton _("莎拉") text_size 25

            textbutton _("瑞秋") text_size 25

            textbutton _("汉娜") text_size 25

            textbutton _("校长") action Show("gallery_headmistress", transition = dissolve) text_size 25

            textbutton _("高村小姐") action Show("gallery_taka", transition = dissolve) text_size 25

            textbutton _("明里") text_size 25

            textbutton _("凯瑟琳") text_size 25

            textbutton _("组合") action Show("gallery_group", transition = dissolve) text_size 25

        vbox:

            
            # xalign 0.0
            yalign 0.0
            xpos 230
            spacing 15

            hbox:
                spacing 15

            # Victoria1 -----------------------------------------------
                if persistent.gallery_victoria1 == True:
                    imagebutton auto "gallery_victoria1_%s":
                        focus_mask True
                        action Replay("replay_victoria1", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Victoria2 -----------------------------------------------
                if persistent.gallery_victoria2 == True:
                    imagebutton auto "gallery_victoria2_%s":
                        focus_mask True
                        action Replay("replay_victoria2", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Victoria3 -----------------------------------------------
                if persistent.gallery_victoria3 == True:
                    imagebutton auto "gallery_victoria3_%s":
                        focus_mask True
                        action Replay("replay_victoria3", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True



            hbox:
                spacing 15

            # Victoria4 -----------------------------------------------
                if persistent.gallery_victoria4 == True:
                    imagebutton auto "gallery_victoria4_%s":
                        focus_mask True
                        action Replay("replay_victoria4", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Victoria5 -----------------------------------------------
                if persistent.gallery_victoria5 == True:
                    imagebutton auto "gallery_victoria5_%s":
                        focus_mask True
                        action Replay("replay_victoria5", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True



#/////////////////////////////////////////////
#   AKATSUKI GALLERY
#/////////////////////////////////////////////
screen gallery_akatsuki():

    tag menu
    use game_menu("晓月"):
        
        # Character menu
        vbox:

            xalign 0.0
            yalign 0.0
            spacing 15

            textbutton _("露西") action Show("gallery_lucy", transition = dissolve) text_size 25

            textbutton _("维多利亚") action Show("gallery_victoria", transition = dissolve) text_size 25

            textbutton _("晓月") action Show("gallery_akatsuki", transition = dissolve) text_size 25

            textbutton _("莎拉") text_size 25

            textbutton _("瑞秋") text_size 25

            textbutton _("汉娜") text_size 25

            textbutton _("校长") action Show("gallery_headmistress", transition = dissolve) text_size 25

            textbutton _("高村小姐") action Show("gallery_taka", transition = dissolve) text_size 25

            textbutton _("明里") text_size 25

            textbutton _("凯瑟琳") text_size 25

            textbutton _("组合") action Show("gallery_group", transition = dissolve) text_size 25

        vbox:

            
            # xalign 0.0
            yalign 0.0
            xpos 230
            spacing 15

            hbox:
                spacing 15

            # Akatsuki1 -----------------------------------------------
                if persistent.gallery_akatsuki1 == True:
                    imagebutton auto "gallery_akatsuki1_%s":
                        focus_mask True
                        action Replay("replay_akatsuki1", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Akatsuki2 -----------------------------------------------
                if persistent.gallery_akatsuki2 == True:
                    imagebutton auto "gallery_akatsuki2_%s":
                        focus_mask True
                        action Replay("replay_akatsuki2", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Akatsuki3 -----------------------------------------------
                if persistent.gallery_akatsuki3 == True:
                    imagebutton auto "gallery_akatsuki3_%s":
                        focus_mask True
                        action Replay("replay_akatsuki3", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True



            hbox:
                spacing 15

            # Akatsuki4 -----------------------------------------------
                if persistent.gallery_akatsuki4 == True:
                    imagebutton auto "gallery_akatsuki4_%s":
                        focus_mask True
                        action Replay("replay_akatsuki4", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Akatsuki5 -----------------------------------------------
                if persistent.gallery_akatsuki5 == True:
                    imagebutton auto "gallery_akatsuki5_%s":
                        focus_mask True
                        action Replay("replay_akatsuki5", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Akatsuki6 -----------------------------------------------
                if persistent.gallery_akatsuki6 == True:
                    imagebutton auto "gallery_akatsuki6_%s":
                        focus_mask True
                        action Replay("replay_akatsuki6", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True



#/////////////////////////////////////////////
#   HEADMISTRESS GALLERY
#/////////////////////////////////////////////
screen gallery_headmistress():

    tag menu
    use game_menu("埃莉森"):
        
        # Character menu
        vbox:

            xalign 0.0
            yalign 0.0
            spacing 15

            textbutton _("露西") action Show("gallery_lucy", transition = dissolve) text_size 25

            textbutton _("维多利亚") action Show("gallery_victoria", transition = dissolve) text_size 25

            textbutton _("晓月") action Show("gallery_akatsuki", transition = dissolve) text_size 25

            textbutton _("莎拉") text_size 25

            textbutton _("瑞秋") text_size 25

            textbutton _("汉娜") text_size 25

            textbutton _("校长") action Show("gallery_headmistress", transition = dissolve) text_size 25

            textbutton _("高村小姐") action Show("gallery_taka", transition = dissolve) text_size 25

            textbutton _("明里") text_size 25

            textbutton _("凯瑟琳") text_size 25

            textbutton _("组合") action Show("gallery_group", transition = dissolve) text_size 25

        vbox:

            
            # xalign 0.0
            yalign 0.0
            xpos 230
            spacing 15

            hbox:
                spacing 15

            # Headmistress1 -----------------------------------------------
                if persistent.gallery_headmistress1 == True:
                    imagebutton auto "gallery_headmistress1_%s":
                        focus_mask True
                        action Replay("replay_headmistress1", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

#/////////////////////////////////////////////
#   TAKA GALLERY
#/////////////////////////////////////////////
screen gallery_taka():

    tag menu
    use game_menu("高村小姐"):
        
        # Character menu
        vbox:

            xalign 0.0
            yalign 0.0
            spacing 15

            textbutton _("露西") action Show("gallery_lucy", transition = dissolve) text_size 25

            textbutton _("维多利亚") action Show("gallery_victoria", transition = dissolve) text_size 25

            textbutton _("晓月") action Show("gallery_akatsuki", transition = dissolve) text_size 25

            textbutton _("莎拉") text_size 25

            textbutton _("瑞秋") text_size 25

            textbutton _("汉娜") text_size 25

            textbutton _("校长") action Show("gallery_headmistress", transition = dissolve) text_size 25

            textbutton _("高村小姐") action Show("gallery_taka", transition = dissolve) text_size 25

            textbutton _("明里") text_size 25

            textbutton _("凯瑟琳") text_size 25

            textbutton _("组合") action Show("gallery_group", transition = dissolve) text_size 25

        vbox:

            
            # xalign 0.0
            yalign 0.0
            xpos 230
            spacing 15

            hbox:
                spacing 15

            # Taka1 -----------------------------------------------
                if persistent.gallery_taka1 == True:
                    imagebutton auto "gallery_taka1_%s":
                        focus_mask True
                        action Replay("replay_taka1", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Taka2 -----------------------------------------------
                if persistent.gallery_taka2 == True:
                    imagebutton auto "gallery_taka2_%s":
                        focus_mask True
                        action Replay("replay_taka2", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True



#/////////////////////////////////////////////
#   GROUP GALLERY
#/////////////////////////////////////////////
screen gallery_group():

    tag menu
    use game_menu("组合"):
        
        # Character menu
        vbox:

            xalign 0.0
            yalign 0.0
            spacing 15

            textbutton _("露西") action Show("gallery_lucy", transition = dissolve) text_size 25

            textbutton _("维多利亚") action Show("gallery_victoria", transition = dissolve) text_size 25

            textbutton _("晓月") action Show("gallery_akatsuki", transition = dissolve) text_size 25

            textbutton _("莎拉") text_size 25

            textbutton _("瑞秋") text_size 25

            textbutton _("汉娜") text_size 25

            textbutton _("校长") action Show("gallery_headmistress", transition = dissolve) text_size 25

            textbutton _("高村小姐") action Show("gallery_taka", transition = dissolve) text_size 25

            textbutton _("明里") text_size 25

            textbutton _("凯瑟琳") text_size 25

            textbutton _("组合") action Show("gallery_group", transition = dissolve) text_size 25

        vbox:

            
            # xalign 0.0
            yalign 0.0
            xpos 230
            spacing 15

            hbox:
                spacing 15

            # Group1 -----------------------------------------------
                if persistent.gallery_group1 == True:
                    imagebutton auto "gallery_group1_%s":
                        focus_mask True
                        action Replay("replay_group1", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True

            # Group2 -----------------------------------------------
                if persistent.gallery_group2 == True:
                    imagebutton auto "gallery_group2_%s":
                        focus_mask True
                        action Replay("replay_group2", locked=False)
                else:
                    imagebutton auto "gallery_locked_%s":
                        focus_mask True



# /// TEMPLATE ///



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
# label replay_lucy1:

    # $ PlayerName = persistent.replay_PlayerName

    # # content here

    # $ renpy.end_replay()


#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################

label replay_lucy1:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/lucy_theme.mp3" loop volume 1.2 fadeout 1.0 fadein 1.0

    scene img_black with hpunch
    Alarm "{b}{i}嘀！嘀！！嘀！！！{/i}{/b}"
    "床头柜上的闹钟刺耳地响着，你醒了。"
    scene img_main11_1 with fade
    "你一睁眼，昨晚和露西的那番对话就立刻变成了现实——因为映入眼帘的第一眼，就是你的新女友。"
    MC "早安。"
    Lucy "早上好。"
    scene img_main11_2 with dissolve
    Lucy "啊……你在笑！"
    MC "哦？干嘛那么惊讶？"
    scene img_main11_3 with dissolve
    Lucy "呃……虽然你偶尔会开玩笑，但你其实很少笑。"
    MC "真的吗？我觉得我笑得挺正常的。"
    scene img_main11_4 with dissolve
    Lucy "不、不是……我是说，不是那种。呃……我总觉得你笑只是为了转移别人的注意力。可刚才那个是真的。"
    MC "你有时候敏锐得有点吓人。总之，我刚才只是在想昨晚的事。"
    scene img_main11_5 with dissolve
    Lucy "啊……"
    MC "看，你又笑了。"
    scene img_main11_6 with dissolve
    Lucy "不、不是……"
    MC "好了，我们该准备上学了。"
    scene img_main11_3 with dissolve
    Lucy "非要吗？我们不能一整天都待在床上吗？"
    MC "哈，看样子你会成为我的坏榜样。再说了，你想想看，如果一整天都待在床上，我打算对你做的事可真不少。"
    scene img_main11_5 with dissolve
    Lucy "嗯……我、我不介意……"
    MC "哎呀，你这是要我的命。不过再翘课，校长真的会把我们吊起来的。"
    scene img_main11_3 with dissolve
    Lucy "那我还是该换衣服了……"
    scene img_main11_7 with dissolve
    "露西跪坐起来，慢慢把上衣拉到了胸口。"
    scene img_main11_8 with dissolve
    "她全程都故意直视着你，虽然显然还很害羞，但看得出来她是在努力变得诱惑。"
    MC "靠，你真是个小妖精。"    
    scene img_main11_9 with dissolve
    "你终于屈服于诱惑，把她推倒在床上，用自己的体型和体重把她压在身下。"
    scene img_main11_10 with dissolve
    Lucy "啊……"
    scene img_main11_11 with dissolve
    MC "现在再装无辜也晚了，我们要在床上整整做一天。"
    scene img_main11_12 with dissolve
    Lucy "我、我不是那个意思……"
    scene vid_main11_1 with dissolve
    "你吻住露西，堵住了她的话，她的嘴唇自然地分开，让你的舌头探入口中。"
    "这个吻如此激烈，露西轻轻哼了一声，等你终于放开她时，她几乎是一脸茫然。"
    scene img_main11_13 with dissolve
    Lucy "啊……哇……可、可是我们真的会惹上麻烦，而且……"
    scene vid_main11_1 with dissolve
    "你又一次堵住了她的话。"
    Lucy "嗯。"
    scene img_main11_12 with dissolve
    Lucy "我、我只是在逗你……"
    scene img_main11_14 with dissolve
    "你没有回答，而是从露西身上翻下来，手顺着她的身体往下滑，直到停在小腹最下方。"
    Lucy "啊……"
    "她意识到接下来要发生什么时，轻轻地倒吸了一口气。"
    scene vid_main11_2 with dissolve
    "你继续往下滑，直到隔着她那条薄薄的内裤揉弄她的小穴。"
    scene vid_main11_3 with dissolve
    "稍微用力一些，你的指尖完美地贴合着她小穴的轮廓，上下滑动。"
    scene vid_main11_4 with dissolve
    "你稍稍往里探了探，她嘴里溢出一声又惊又美的尖叫；每次你的手指擦过她的阴蒂，她整个人都会颤抖起来。"
    "没过多久，她的内裤就开始变得潮湿，甚至还有意无意地在你手上磨蹭起来。"
    scene vid_main11_2 with dissolve
    Lucy "嗯嗯……啊、啊……我、我是说……我只是在逗你！不、不可以！"
    MC "哈哈，这下知道别想跟我玩「谁先怂谁输」了吧。"
    Lucy "嗯呜呜……对、对不起！请、请原谅我！"
    Lucy "嗯……哈啊啊……[PlayerName]……嗯呜呜……"
    scene vid_main11_3 with dissolve
    "你又揉弄了好一会儿，才终于放过她。"
    scene img_main11_15 with dissolve
    Lucy "啊……"
    "你收回手，露西长长地叹了口气，那口气里混杂着快感、放松，以及对你停下来的失望。"
    scene img_main11_16 with dissolve
    MC "要是真让你那么舒服，我可以再开始。"
    "露西显然在和诱惑搏斗，但最后她似乎认命了。"
    scene img_main11_17 with dissolve
    Lucy "我、我们要迟到了……"
    MC "你说这怪谁？"
    scene img_main11_18 with dissolve
    Lucy "对、对不起……"
    MC "没事，我很喜欢你这一面，平时你都把它藏得严严实实的。"
    scene img_main11_19 with dissolve
    Lucy "真的吗？"
    MC "对啊。你还记得我们打扫咖啡馆的时候，你告诉我你的罩杯那次吗？"
    Lucy "呃，记得？"
    MC "那是我第一次觉得，我可能真的会喜欢上你。我本来就已经觉得你很可爱了，但你那害羞外表下爱闹的一面真是太好了。希望以后还能看到更多。"
    scene img_main11_20 with dissolve
    Lucy "啊……你害我好害羞……"
    scene img_main11_21 with dissolve
    "你没有回答，只是飞快地在露西嘴上啄了一下，然后站起身来。"
    MC "走吧，先收拾准备，然后我来做早餐。"
    MC "但别以为就这样完了，今晚我们会接着刚才的地方继续。乖的话，说不定我还会让你射出来。"
    Lucy "啊……"

    $ renpy.end_replay()

#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################

label replay_lucy2:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/night.mp3" loop fadeout 1.0 fadein 1.0

    scene img_main11_353 with dissolve
    pause
    scene img_main11_354 with dissolve
    MC "我记得今天早上去学校前，我们开了个头，还说好了今晚要把它做完。"
    scene img_main11_355 with dissolve
    Lucy "啊……"
    MC "不过首先，我觉得你该把裙子脱掉。可别把它弄脏了……"
    scene img_main11_356 with dissolve
    Lucy "我、我去把它放进洗衣机。"
    scene img_main11_357 with dissolve
    MC "不，就在这儿脱。"
    Lucy "好、好的……"
    scene img_main11_358 with dissolve
    pause 1
    scene img_main11_359 with dissolve
    "裙子刚一脱下，你就把她拽到床边轻轻一推，让她失去平衡。"

    play music "audio/bgm/lucy_theme.mp3" loop volume 1.2 fadeout 1.0 fadein 1.0

    scene img_main11_360 with dissolve
    "露西尖叫一声，仰面摔在了你面前。"
    scene img_main11_361 with dissolve
    MC "你现在是我的了，我们有一整晚可以玩。"
    scene img_main11_362 with dissolve
    Lucy "我、我……"
    "她有些犹豫，显然在这种情况下还是会紧张。不过过了一会儿，她似乎下定了决心，兴奋逐渐占了上风。"
    scene img_main11_363 with dissolve
    Lucy "好、好的……"
    scene img_main11_364 with dissolve
    "你照搬了今天早上的流程，先吻她，然后揉弄、抚摸她丰满身体的每一寸。"
    scene img_main11_365 with dissolve
    Lucy "嗯呜呜……啊！我、我……"
    scene img_main11_366 with dissolve
    MC "所以你喜欢我捏你的奶子？露西，你真是个小淫娃子。"
    scene img_main11_367 with dissolve
    Lucy "或、或许吧……对你来说的话……"
    scene img_main11_368 with dissolve
    "你伸手到她背后，解开她的胸罩。她立刻明白了你想要什么，不用你开口就把胸罩甩到了一边。"
    scene img_main11_369 with dissolve
    MC "乖女孩……"
    scene img_main11_370 with dissolve
    Lucy "啊啊啊……我、我的……"
    MC "露西，你的乳头硬了。"
    scene img_main11_371 with dissolve
    Lucy "啊，不、不是……"
    scene img_main11_372 with dissolve
    "你俯下身，把一颗挺立的乳头含进嘴里，她发出一声又惊又美的叫声。"
    Lucy "嗯……"
    "她也许确实很单纯，可那柔弱的呻吟与喘息却告诉你，她其实已经完全沉浸其中了。"
    scene img_main11_373 with dissolve
    MC "该接着今天早上的地方继续了。"
    scene img_main11_374 with dissolve
    "和刚才一样，你在她身边躺下，把手滑到她的腹部。"
    scene vid_main11_5 with dissolve
    "你先隔着她的内裤揉弄了一会儿。"
    scene vid_main11_6 with dissolve
    "但你很快就忍不住了，把内裤拨到一边，直接揉弄起她的小穴。"
    pause
    MCi "（不知道这样会不会太过分了？）"
    Lucy "啊、啊……"
    MC "露西，你已经湿透了。"
    Lucy "唔唔嗯……"
    scene vid_main11_7 with dissolve
    "你看着她的脸，手指上下滑动，细细品味她面对这全新体验时的反应。"
    Lucy "啊啊啊……嗯呜呜……[PlayerName]……我、我……"
    MC "如果想让我更进一步，你就得亲口说出来。"
    scene vid_main11_8 with dissolve
    Lucy "我、我……求你了……我想要更多……"
    scene vid_main11_9 with dissolve
    "你开始专注于她的阴蒂，让女孩发出甜美的呻吟与柔软的喘息。接着你又往更深处按压，第一次探索她未经人事的小穴。"
    pause
    scene vid_main11_10 with dissolve
    "你小心地不让动作过头，把中指与食指的指尖送进了她体内。"
    pause
    Lucy "嗯呜呜……天啊……[PlayerName]！"
    scene vid_main11_11 with dissolve
    "你就这样持续了很长一段时间，动作越来越快。"
    Lucy "啊嗯呜呜呜……我、我……"
    "最后，当你觉得她快要到达顶点时，你突然把手抽了回来。"
    scene vid_main11_12 with dissolve
    Lucy "啊啊啊，为、为什么停下？"
    scene vid_main11_13 with dissolve
    MC "想让我继续吗？"
    Lucy "想、想！"
    MC "那就好好求我。"
    scene vid_main11_14 with dissolve
    Lucy "我、我……求你了 [PlayerName]……"
    scene vid_main11_10 with dissolve
    "你重新开始，而你的指尖一进入她体内，她就彻底融化在狂喜之中。"
    pause
    scene vid_main11_11 with dissolve
    Lucy "啊嗯呜呜呜呜！"
    pause
    scene vid_main11_12 with dissolve
    "你又一次持续到她就在临界点上，然后停下。"
    scene vid_main11_14 with dissolve
    Lucy "啊，太过分了！求、求你了 [PlayerName]，求你啦——"
    "她的哀求用柔软的声音说出来，充满渴求、绝望、欲望与顺从。"
    MC "求什么？露西，你想让我做什么？"
    Lucy "求你……让、让我……呃……你知道吧……"
    MC "什么？你得说出来。"
    Lucy "求你让我高潮！"
    MC "你真是个坏女孩。不过我可不会这么快就结束……"
    MC "露西，我想和你做爱。"
    scene vid_main11_13 with dissolve
    Lucy "啊、啊……"
    "她抬起头望进你认真的脸庞，眼睛睁得大大的。"
    scene img_main11_375 with dissolve
    "过了片刻，她把视线移开——她实在害羞得没法当面说出口。"
    Lucy "我、我也想要……"
    scene img_main11_376 with dissolve
    Lucy "可、可是得等到星期天！"
    scene img_main11_377 with dissolve
    "你一边说，一边轻轻揉弄她的小穴。不足以让她高潮，却刚好能逼疯她。"
    scene img_main11_378 with dissolve
    Lucy "嗯呜呜……"
    MC "星期天？这么具体。为什么是星期天？"
    scene img_main11_379 with dissolve
    Lucy "啊、啊……"
    scene img_main11_380 with dissolve
    "你把中指探得比以往任何时候都更深，让她不由得叫出声来。"
    Lucy "唔唔嗯！"
    scene img_main11_381 with dissolve
    MC "为什么是星期天，露西？"
    scene img_main11_378 with dissolve
    "她在急促的呼吸与细碎的呻吟中艰难地开口，最后还是回答了。"
    scene img_main11_379 with dissolve
    Lucy "因、因为……那天我的避孕药才生效！"
    MC "哦？那就是不用戴套了？你已经想过这件事很多次了吧？"
    scene img_main11_382 with dissolve
    Lucy "不、不是……嗯呜呜。"
    scene img_main11_383 with dissolve
    "你再次停下手指上的动作，直视她的眼睛。"
    MC "说实话。"
    scene img_main11_379 with dissolve
    Lucy "啊……好、好的……"
    MC "在你的想象里，我会射在里面吗？"
    scene img_main11_375 with dissolve
    Lucy "那、那太难为情了！"
    MC "告诉我。"
    scene img_main11_376 with dissolve
    Lucy "想、想要……我想要……"
    MC "乖女孩，我想你值得一个奖励。"
    scene vid_main11_15 with dissolve
    "你把她的双腿分得更开一些，以便更好地动作，然后开始更用力地揉弄她的阴蒂、进入她的身体。"
    "她那细弱亲昵的呻吟，第一次比你预想中这个腼腆女孩发出的声音更大了一些。"
    Lucy "啊啊啊，[PlayerName]……"
    scene img_main11_383_1 with dissolve
    "在你反复挑逗之后，她终于崩溃地越过顶点，双腿夹紧你的手，小穴在你的手指间剧烈收缩，迎来猛烈的高潮。"
    Lucy "啊！"
    scene img_main11_383_2 with dissolve
    Lucy "啊啊啊！"
    scene img_main11_383_3 with dissolve
    Lucy "啊啊啊啊啊！！"
    scene img_main11_383_3 with vpunch
    Lucy "哦啊啊啊啊啊嗯！！"
    scene img_main11_384 with dissolve
    "当她的高潮终于平息，她瘫软在你身旁大口喘息，过了很久才平静到能开口说话。"
    scene img_main11_385 with dissolve
    Lucy "我、我从来没感受过……那样的感觉……"
    scene img_main11_386 with dissolve
    MC "你从没自己弄过吗？"
    scene img_main11_387 with dissolve
    Lucy "不、没有……我在家里根本没有机会……"
    MC "我明白了。习惯就好，后面还有得是。"
    scene img_main11_388 with dissolve
    Lucy "啊，我可永远习惯不了……"
    scene img_main11_389 with dissolve
    "你握住露西的手，放到自己两腿之间。"
    MC "现在轮到你了。"
    scene img_main11_390 with dissolve
    "她撑起身子，认真地看着你。"
    scene img_main11_391 with dissolve
    Lucy "是、是的……我也想让你舒服……"
    Lucy "呃，请躺下……"
    scene img_main11_392 with dissolve
    "你翻过身仰面躺下，露西小心地在你两腿之间坐好。"
    scene img_main11_393 with dissolve
    Lucy "那、那么……"
    scene img_main11_394 with dissolve
    "她手忙脚乱地摆弄你的裤子，你注意到她的手在发抖。最后她终于把你涨硬的鸡巴从束缚中释放出来。"
    scene img_main11_395 with dissolve
    Lucy "哦……比、比我想的要大得多……"
    "她似乎有点被吓住，于是你只是等着她先迈出第一步。"
    scene img_main11_396 with dissolve
    "她先伸出手碰了碰，但和薇琪不同，她一上来就用手握住。"
    MC "你可以握得再紧一点。"
    scene img_main11_398 with dissolve
    Lucy "好、好的……像这样？"
    scene img_main11_397 with dissolve
    MC "完美。"
    scene img_main11_399 with dissolve
    "她犹犹豫豫地开头，只是极短暂地舔了舔你鸡巴的前端。接着一点一点地，她开始用整条舌头舔舐"
    scene img_main11_400 with dissolve
    "等习惯了这个想法，她把嘴张到最大，让你的前端滑进她温暖湿润的嘴里。"
    Lucy "唔唔呃。"
    MC "乖女孩。现在试着动起来。"
    Lucy "唔嗯……"
    scene vid_main11_17 with dissolve
    "按你的指示，她俯下身，开始让嘴在你的鸡巴上下滑动。"
    Lucy "唔嗯呃唔。"
    "她柔软的双唇裹住前端、丝滑湿润的舌头抚弄着下侧的触感，简直让人头皮发麻。"
    scene img_main11_401 with dissolve
    "她小心不让前端滑出嘴外，抬眼看了看你。"
    "当她看到你的表情、察觉自己带来的效果时，整张脸都亮了起来。"
    scene vid_main11_18 with dissolve
    "感到害羞，她移开视线，更加卖力起来，开始让你在她嘴里进得深一些。"
    pause
    scene vid_main11_21 with dissolve
    "她显然一心想让你满意，越含越深，直到你的鸡巴抵到她的喉咙后壁。"
    Lucy "唔……唔……唔……唔唔唔！"
    scene vid_main11_19 with dissolve
    "因为经验不足而得意忘形，她含得太深，差点呛到。之后她退开了一点，但没有停下。"
    scene img_main11_401 with dissolve
    "你大概是发出了声音，因为她又抬头来寻求肯定。你们对上视线时她又移开目光，然后继续热情地为你口交。"
    scene vid_main11_19 with dissolve
    MC "乖女孩，别停。"
    Lucy "唔嗯。"
    scene vid_main11_21 with dissolve
    "露西继续吸吮着你，直到每一个神经末梢都因快感而嗡鸣。"
    "最后到了你再也坚持不住的地步。"
    MC "啊……露西，我要射了。"
    Lucy "唔哼……嗯。"
    scene vid_main11_22 with dissolve
    "听到你的预告，她吸得更加卖力，显然打定主意要在这结束之前给你尽可能多的快感。"

    menu:
        "射在她嘴里。":
            jump main_11_choice_3mouth_replay

        "射在她脸上。":
            jump main_11_choice_3face_replay

label main_11_choice_3mouth_replay:
    MC "再深一点，露西，我要你把每一滴都咽下去。"
    Lucy "唔嗯。"
    scene img_main11_402 with dissolve
    "她最后再一次把你的头按下去，然后一直保持在那里，直到你爆发。"
    scene img_main11_402 with vpunch
    pause 0.5
    scene img_main11_402 with vpunch
    pause 0.35
    scene img_main11_402 with vpunch
    pause 0.2
    scene img_main11_402 with vpunch
    pause 0.1
    scene img_main11_403 with vpunch
    pause 0.1
    scene img_main11_403 with flash
    Lucy "唔！"
    Lucy "唔唔……"
    "你一股股把精液射进她紧致的喉咙时，她有点呛，但直到你射完都没有松口。"
    scene img_main11_404 with dissolve
    "最后她退开，双唇顺着你的柱身缓缓上移。"
    scene img_main11_405 with dissolve
    "她在顶端停顿了好长一会儿，把你最后一点存货咽下去。"
    scene img_main11_411 with dissolve
    "全部咽完后，她抬头朝你露出一个不确定的笑容。"

    $ renpy.end_replay()
    
label main_11_choice_3face_replay:
    MC "往后靠，露西，我想射满你漂亮的脸。"
    Lucy "唔嗯。"
    scene img_main11_404 with dissolve
    "她退开，双唇顺着你的柱身缓缓上移。你的鸡巴一离开她的嘴，你就任由爆发开始。"
    scene img_main11_406 with vpunch
    pause 0.5
    scene img_main11_407 with vpunch
    pause 0.35
    scene img_main11_408 with vpunch
    pause 0.2
    scene img_main11_409 with vpunch
    pause 0.1
    scene img_main11_410 with vpunch
    pause 0.1
    scene img_main11_410 with flash
    "一股股黏稠的精液射满了她可爱的脸，而她全程都努力维持着与你的对视。"
    scene img_main11_412 with dissolve
    "当你终于在她脸上画完，她抬头朝你露出一个不确定的笑容。"

    $ renpy.end_replay()

#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_lucy3:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/night.mp3" loop fadeout 1.0 fadein 1.0

    MC "好了，你有多累？"
    scene img_main13_402 with dissolve
    Lucy "呃，有一点，怎么了？"
    MC "嗯，晓月一整天都在撩我，之后我又和你还有薇琪腻歪了几个小时。我有点憋得慌……"
    scene img_main13_403 with dissolve
    Lucy "我可以帮你……如果你愿意的话？"

    play music "audio/bgm/lucy_theme.mp3" loop volume 1.2 fadeout 1.0 fadein 1.0

    scene img_main13_404 with dissolve
    "你没有回答，而是把鸡巴从内裤里掏了出来。"
    scene img_main13_405 with dissolve
    Lucy "啊……"
    scene img_main13_406 with dissolve
    pause
    scene img_main13_407 with dissolve
    "她跪在你面前，试探性地用双手握住你的柱身。"
    scene img_main13_408 with dissolve
    MC "慢点，先把上衣脱掉。"
    scene img_main13_409 with dissolve
    Lucy "好、好的。"
    scene img_main13_410 with dissolve
    pause
    scene img_main13_411 with dissolve
    MC "操，你真美，露西。"
    scene img_main13_412 with dissolve
    Lucy "啊……"
    scene vid_main13_1 with dissolve
    "她的脸颊泛起红晕，开始不规律地上下撸动。"
    scene vid_main13_2 with dissolve
    "经过几个尴尬的动作之后，她找到了节奏，手感也开始变好了。"
    "她的手掌和手指在你柱身上围成一个舒服的环，小心地上下撸动。"
    scene vid_main13_3 with dissolve
    pause
    Lucy "这、这样可以吗……？"
    MC "你做得很好，露西。"
    scene vid_main13_4 with dissolve
    Lucy "呃……我在网上看到说，我应该要跟、跟你说话……"
    MC "跟我说话？"
    Lucy "呃，就是……骚话……但我不知道该说什么。"
    scene vid_main13_3 with dissolve
    "尽管说得犹犹豫豫，她还是继续轻柔地上下套弄你的鸡巴。"
    scene vid_main13_4 with dissolve
    MC "就说你在做什么、你有什么感觉，还有你想让我有什么感觉。"
    Lucy "我想让你舒服！"
    scene vid_main13_5 with dissolve
    "她握得更紧，动作也更快了。"
    scene vid_main13_6 with dissolve
    Lucy "我、我什么都愿意做，只为让你舒服……"
    scene vid_main13_7 with dissolve
    "她再次加快，用双手制造出的快感愈发强烈。"
    scene vid_main13_8 with dissolve
    Lucy "我想让你射出来。"
    scene vid_main13_9 with dissolve
    "你被她随着手活上下起伏的大胸吸引住了目光。"
    scene vid_main13_10 with dissolve
    "当你抬眼看回去，正好撞见她那双大眼睛直直地盯着你。"
    Lucy "拜、拜托，为我射出来……"
    scene vid_main13_11 with dissolve
    "她感到害臊，移开了视线，却一次也没有停下套弄你的鸡巴。"
    scene vid_main13_12 with dissolve
    "透过鸡巴传来的触感，你感受到了她那份体贴——她拼尽全力想让你射出来。"
    "她那份单纯想让你舒服的心意，混杂着一个性感女孩卖力为你手淫的肉体快感，把你推向了边缘。"
    scene img_main13_413 with dissolve
    "就在最后一刻，你伸手按住了她。"
    scene img_main13_414 with dissolve
    MC "躺下，躺平。"
    scene img_main13_415 with dissolve
    "她看起来有点困惑，但还是毫不犹豫地照做了。"
    scene img_main13_416 with dissolve
    "你跨坐在她身上，涨硬的鸡巴正好悬在她胸口上方。"
    scene img_main13_417 with dissolve
    MC "把手给我。"
    scene img_main13_418 with dissolve
    "你把她的手包在自己的鸡巴上，然后再用自己的手包住她的手，引导着上下移动。"
    scene img_main13_419 with dissolve
    "她的手在你涨硬的鸡巴上上下撸动，你准备着要射她一身。"
    scene img_main13_420 with dissolve
    pause
    scene img_main13_421 with dissolve
    Lucy "我、我感觉要来了……"
    scene img_main13_422 with dissolve
    Lucy "拜托为我射出来，[PlayerName]……"
    "她一边哀求一边上下套弄你的鸡巴，那语气终于让你越过了临界点……"
    scene img_main13_419 with dissolve
    pause 0.5
    scene img_main13_423 with dissolve
    pause 0.35
    scene img_main13_419 with dissolve
    pause 0.3
    scene img_main13_423 with dissolve
    pause 0.25
    scene img_main13_419 with dissolve
    pause 0.15
    scene img_main13_423 with dissolve
    pause 0.05
    scene img_main13_419 with vpunch
    pause 0.05
    scene img_main13_424 with vpunch
    pause 0.05
    scene img_main13_425 with vpunch
    pause 0.2
    scene img_main13_426 with vpunch
    pause 0.1
    scene img_main13_426 with flash
    "你射了她一脸一胸。"
    scene img_main13_427 with dissolve
    Lucy "唔，好多……"
    MC "对。你做得好，露西。"
    scene img_main13_428 with dissolve
    "你瘫回她身边，等了几秒让心率平复。"

    $ renpy.end_replay()

#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_victoria1:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/victoria_theme.mp3" loop volume 1.0 fadeout 1.0 fadein 1.0

    MC "脱。"
    scene img_main10_101 with dissolve
    Victoria "是，主人。"
    scene img_main10_102 with dissolve
    "薇琪往后退了几步，把裙子脱了下来。"
    scene img_main10_103 with dissolve
    pause
    scene img_main10_104 with dissolve
    pause
    scene img_main10_105 with dissolve
    pause
    scene img_main10_102 with dissolve
    MC "不够，我这些早就见过了。把内衣也脱掉。"
    scene img_main10_106 with dissolve
    "薇琪犹豫得太久了，于是……"
    scene img_main10_107 with vpunch
    "{b}*砰！！*{/b}"
    scene img_main10_108 with dissolve
    MC "你是我的。"
    scene img_main10_109 with dissolve
    Victoria "啊……是、是的，主人。"
    scene img_main10_110 with dissolve
    "你退后一步想看得更清楚，薇琪一边脱内衣一边脸红得厉害。"
    MC "你意外地很纯情嘛，薇琪，这真的是你第一次做这种事？"
    scene img_main10_111 with dissolve
    Victoria "当、当然了。我都说过我不是骚货！"
    MC "等我收拾完你，你就会是了，我的小骚货。"
    scene img_main10_110 with dissolve
    Victoria "..."
    scene img_main10_112 with dissolve
    "没等薇琪说出回答，你就把她按在墙上打断了她。"
    scene img_main10_113 with dissolve
    "她只维持了一瞬间的对视，就尴尬地移开了视线。"
    "当你发现她在为自己的天真回答露出得意的笑时，她正要开口，你又一次抢在她前面打断。"
    scene img_main10_114 with dissolve
    Victoria "唔唔……"
    scene img_main10_118 with dissolve
    MCi "（她连看都不敢看我，我一逼近她，她果然就和露西一样害羞。不知道那是不是她的初吻？）"
    scene img_main10_116 with dissolve
    Lucy "啊……"
    scene img_main10_117 with dissolve
    Lucy "（她、她看见我了吗？）"
    scene img_main10_115 with dissolve
    MC "该罚你了。"
    scene img_main10_119 with dissolve
    "你把手放在薇琪肩上，用刚好足以让她明白你意图的力道往下压。"
    scene img_main10_120 with dissolve
    "犹豫了片刻后，她屈服了，跪倒在你面前。"
    MC "解开我的裤子。"
    scene img_main10_121 with dissolve
    "她抬头看了你一眼，但还是照你说的做了。"
    scene img_main10_122 with dissolve
    Victoria "哦……"
    scene img_main10_123 with dissolve
    MC "你叫我基佬的时候，就是想让我用这个惩罚你，对吧？"
    scene img_main10_124 with dissolve
    Victoria "不、不是……"
    MC "得了吧，你的眼睛都黏在上面了。承认吧。"
    scene img_main10_125 with dissolve
    Victoria "闭、闭嘴！"
    MC "你不是该这么跟你的主人说话的。"
    scene img_main10_126 with dissolve
    Victoria "对、对不起，主人。"
    MC "乖女孩。你倒是让我看看你有多抱歉。"
    scene vid_main10_1 with dissolve
    "薇琪抬起一只手，不确定地碰了碰你的柱身。"
    "当她的指尖按上你硬实的肉柱时，她自己看起来几乎有些惊讶，于是开始试探性地四处摸索。"
    "她的手上下游走，用手指轻轻揉弄你的鸡巴，偶尔戳一下。但她始终不肯真的用整只手来握。"
    scene vid_main10_2 with dissolve
    "她的关注当然不算难受，但生涩的手法渐渐变成了无意识的挑逗，你想要更多的冲动开始变得难以遏制。"
    MC "你不太行啊，就这点本事我们得耗一整天。"
    scene img_main10_127 with dissolve
    Victoria "我、我知道，闭嘴！我还没开始呢……"
    scene img_main10_128 with dissolve
    Victoria "主人……"
    scene vid_main10_3 with dissolve
    pause
    "这次薇琪多用了一些手，开始有节奏地撸动你的前端"
    "她的手指落在你最敏感的部位上，那感觉格外强烈，而她一直动着，直到你的鸡巴开始不受控制地抽动。"
    "发现这一点后她僵住了一瞬，似乎被自己引发的反应吓到了。好在恐惧没有持续太久，她很快又继续按摩你的前端。"
    "不过，你还想要更多。"
    MC "现在用整只手握住它。"
    scene vid_main10_4 with dissolve
    pause
    "薇琪开始缓缓地沿你的柱身上下移动手掌。"
    "她柔软的手掌完全包裹住你的感觉妙极了，但想到她完全听命于你所带来的权力感，才真正令人战栗。"
    "美丽、自信、平日总是强势的女孩向你臣服，这让你的想象力在各种可能之间肆意狂奔。"
    "她撸动的手再往下一点，擦过你的蛋，你一下子被拉回现实。"
    MC "继续。想象一下我把它深深插进你体内时会是什么感觉。"
    Victoria "啊……"
    "她那双明亮的蓝眼睛盯着你的鸡巴，脸上交织着畏惧与兴奋，显然已经在想象那种感觉。"
    "与此同时她保持着顺滑的动作，手从根部移到顶端，轻轻拉扯着你的皮肤上下滑动。"
    MC "现在更快，更用力。"
    scene vid_main10_5 with dissolve
    pause
    "薇琪顺从地照做，手上的动作变得更短促、更快速。"
    "同时她收紧了握力，让手指沿着你柱身上的每一道细小曲线和轮廓上下描摹。"
    "有那么一瞬间，你沉浸在这种感觉里失去了自我。"
    Victoria "呃，我做得对吗，主人？"
    "她的声音里明显带着不安，于是你决定给她一点安抚。"
    MC "你做得很好，薇琪，继续。想象一下我把你按在床上狠狠干你的时候。"
    "薇琪的脸更红了，移开视线看了一会儿，显然招架不住脑海里那幅画面。"
    MC "看着我。"
    scene vid_main10_6 with dissolve
    "女孩重新对上你的视线，手上则一直不停地撸动你的鸡巴。"
    MC "乖女孩，照这个速度你说不定真能让我射出来。"
    Victoria "射、射出来？"
    MC "哈，你听起来好像很害怕。"
    Victoria "不、不是……我才没有！"
    MC "很好，那就准备好。"
    Victoria "呃，好的，主人……"
    pause

menu:
    "接下来做什么？"

    "让她专注于前端。":
        jump main10_choice_1_tip_replay

    "让她慢一点。":
        jump main10_choice_1_slow_replay

    "让她快一点。":
        jump main10_choice_1_fast_replay

    "射在她脸上":
        jump main10_choice_1_complete_replay


label main10_choice_1_tip_replay:
    MC "专注于前端。"
    Victoria "是，主人。"
    scene vid_main10_3 with dissolve
    "薇琪转而缓慢地按摩你的前端。她把注意力集中在神经密布的地方带来的强烈刺激，与之前更用力的撸动形成了鲜明对比。"
    pause

menu:
    "接下来做什么？"

    "让她慢一点。":
        jump main10_choice_1_slow_replay

    "让她快一点。":
        jump main10_choice_1_fast_replay

    "射在她脸上":
        jump main10_choice_1_complete_replay

label main10_choice_1_slow_replay:
    MC "现在慢一点。"
    Victoria "好。"
    scene vid_main10_4 with dissolve
    "薇琪垂下眼睛看着你的鸡巴，专注于用缓慢而有节奏的手法移动手掌。"
    Victoria "我、我不敢相信这么硬……"
    pause

menu:
    "接下来做什么？"

    "让她专注于前端。":
        jump main10_choice_1_tip_replay

    "让她快一点。":
        jump main10_choice_1_fast_replay

    "射在她脸上":
        jump main10_choice_1_complete_replay  

label main10_choice_1_fast_replay:
    MC "快点。"
    Victoria "好。"
    scene vid_main10_5 with dissolve
    "她仰头朝你笑了笑，你们对上视线，她再次开始用力地撸动。"
    pause
    scene vid_main10_6 with dissolve
    Victoria "这样很舒服吧，主人？"
    MC "还不错。继续。"
    Victoria "哼。"
    pause

menu:
    "接下来做什么？"

    "让她专注于前端。":
        jump main10_choice_1_tip_replay

    "让她慢一点。":
        jump main10_choice_1_slow_replay

    "射在她脸上":
        jump main10_choice_1_complete_replay

label main10_choice_1_complete_replay:
    MC "啊，操……"
    scene img_main10_129 with dissolve
    "你转向薇琪，她立刻僵住，就像正瞄着一支上了膛的枪口。"
    "她的手在你前端下方紧紧握住的感觉，足以把你推过临界点。"
    scene img_main10_129 with vpunch
    pause 0.5
    scene img_main10_129 with vpunch
    pause 0.35
    scene img_main10_129 with vpunch
    pause 0.2
    scene img_main10_129 with vpunch
    pause 0.1
    scene img_main10_130 with vpunch
    pause 0.1
    scene img_main10_130 with flash
    "一股股黏稠的白精射满了她的脸，一时间她看起来都呆住了。"
    Victoria "啊……"
    scene img_main10_131 with dissolve
    "你一手托住她的下巴，强迫她抬头看着你。"
    scene img_main10_132 with dissolve
    MC "你的主人给你东西的时候，你该说什么？"
    scene img_main10_133 with dissolve
    Victoria "谢、谢谢主人。"

    $ renpy.end_replay()

#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_victoria2:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/victoria_theme.mp3" loop volume 1.0 fadeout 1.0 fadein 1.0

    scene img_main12_209 with dissolve
    "你用双手攫取她的身体，比之前揉得更用力。"
    scene img_main12_210 with dissolve
    "她的裙子几乎兜不住那对大奶子，而当你的手指挤捏上去时，那层布料简直形同虚设。"
    scene img_main12_211 with dissolve
    Victoria "唔，[PlayerName]，你太粗暴了。"
    scene img_main12_212 with dissolve
    MC "从现在到我们走出这扇门之前，你只能叫我主人。"
    Victoria "唔嗯，好的，主人。"
    MC "转过去，靠在墙上。"
    scene img_main12_213 with dissolve
    Victoria "你要对我做什么？"
    MC "好吧，既然你没有乖乖听话，而是问了这个问题，那我第一件事就是打你的屁股。"
    scene img_main12_214 with dissolve
    Victoria "我的意思是……我不想在更衣室里失去处女之身……主人。"
    MC "哈，我本来没打算操你，薇琪。不过你真觉得我会试的时候你会拒绝吗？"
    scene img_main12_215 with dissolve
    Victoria "我、我……我想等到成为你女朋友之后再说！"
    MC "这倒是。不过你真觉得自己能等那么久吗？"
    scene img_main12_216 with dissolve
    Victoria "当然！你说呢？"
    MC "嗯，我们看看你的自信能撑多久。我要一直撩你，直到你求着我干你。"
    scene img_main12_217 with dissolve
    "她不服输地朝你咧嘴一笑，公然挑战。"
    Victoria "来啊。"
    MC "我记得我叫你转过去靠在墙上了。"
    scene img_main12_218 with dissolve
    Victoria "啊，是的，主人。"
    scene img_main12_219 with dissolve
    pause
    scene img_main12_220 with dissolve
    pause
    scene img_main12_221 with dissolve
    pause
    scene img_main12_222 with dissolve
    pause
    scene img_main12_223 with dissolve
    pause
    scene img_main12_224 with dissolve
    MC "该罚你了。"
    scene img_main12_225 with dissolve
    "你先捏了捏她圆润的屁股，她则挑衅地扭了扭作为回应。"
    scene img_main12_226 with dissolve
    Victoria "唔……嘿嘿，感觉主人你太分心了，都顾不上罚我了。"
    Victoria "我……"
    scene img_main12_225 with dissolve

    menu:
        "打她。":
            jump main_12_choice_3play1_spank_replay
        "跳过打屁股。":
            jump main_12_choice_3play1_skip_replay

label main_12_choice_3play1_spank_replay:   
    scene img_main12_227 with dissolve
    pause
    scene img_main12_228 with vpunch
    "{i}啪！{/i}"
    Victoria "啊！"
    scene img_main12_229 with dissolve
    Victoria "我……"
    scene img_main12_228 with vpunch
    "{i}啪！{/i}"
    scene img_main12_230 with dissolve
    Victoria "啊！"
    scene img_main12_231 with vpunch
    "{i}啪！{/i}"
    Victoria "咿呀！"
    MC "薇琪，我觉得是时候对你诚实了。你喜欢这样，对吧。"
    scene img_main12_232 with dissolve
    Victoria "不、不是，我……"
    scene img_main12_233 with vpunch
    "{i}啪！{/i}"
    Victoria "啊！"
    MC "你不会对我撒谎，对吧？"
    scene img_main12_234 with dissolve
    Victoria "我、我不知道什……"
    scene img_main12_235 with vpunch
    "{i}啪！{/i}"
    Victoria "啊唔嗯。"
    MC "那听起来可很像是呻吟啊，薇琪。你是不是被我打屁股打得很爽？"
    scene img_main12_233 with dissolve
    Victoria "才不是！"
    scene img_main12_231 with dissolve
    "薇琪绷紧身体，等着下一下。但它没有来。"
    scene img_main12_227 with dissolve
    "当你抬起手时，她期待地回头看着你……"
    scene img_main12_225 with dissolve
    "但你没有再打她，而是继续揉捏她的屁股。"
    jump main_12_choice_3play1_skip_replay

label main_12_choice_3play1_skip_replay:
    scene img_main12_226 with dissolve
    MC "在我允许之前不许把手从墙上拿开，明白了吗？"
    Victoria "我……"
    MC "明白了吗？"
    scene img_main12_232 with dissolve
    Victoria "明白了，主人。"
    MC "乖女孩。"
    scene img_main12_236 with dissolve
    "你把勃起的鸡巴从裤子里掏出来，抵在她丰满的屁股上。"
    scene img_main12_237 with dissolve
    Victoria "那是……？"
    MC "对。"
    scene img_main12_238 with dissolve
    pause
    scene img_main12_239 with dissolve
    "你把鸡巴往下滑，用前端挑起她的裙子，把她的内裤暴露得更多。"
    scene img_main12_240 with dissolve
    "依然只用前端，你开始把她那条小小的丁字裤压进她的屁股里。"
    scene img_main12_241 with dissolve
    "你稍微弯下腿以适应高度差，把身体挤进她的大腿之间，尽情享受她柔软肉感的肉体包裹住你柱身的感觉。"
    scene img_main12_242 with dissolve
    "稍微往上挪一点，你感到自己的鸡巴正抵在薇琪的小穴上。"
    scene img_main12_243 with dissolve
    Victoria "{i}*倒吸一口气{/i}天、天啊……"
    scene img_main12_244 with dissolve
    MC "好了薇琪，你要这样让我射出来。"
    scene img_main12_245 with dissolve
    Victoria "好、好的，主人。"
    scene img_main12_244 with dissolve
    "她似乎不太确定该怎么做，但还是先开始用大腿夹紧你的鸡巴。"
    Victoria "唔嗯……"
    scene vid_main11_23 with dissolve
    pause
    "一开始很慢，她开始沿着你的柱身上下磨蹭。"
    scene vid_main11_24 with dissolve
    "你俯身在她耳边低声说话。"
    MC "你湿了，薇琪，我能隔着内裤感觉到。"
    Victoria "我、我控制不住……"
    MC "你的身体知道自己想要什么，哪怕你自己还没准备好认输。"
    "薇琪用一种你从未听过的低沉撩人语调回应。"
    Victoria "唔嗯……"
    scene vid_main11_25 with dissolve
    pause
    "流到她大腿内侧的液体开始充当润滑，你决定是时候夺回主动权了。"
    scene vid_main11_26 with dissolve
    "你紧紧抓住她的屁股借力，有节奏地把她拉向你，朝她的小穴挺送——但因为她湿透的内裤太薄，你只是在她表面滑动而没法真的插进去。"
    Victoria "唔嗯……就是这样，主人……用我来让自己舒服……为我射出来……"
    scene vid_main11_27 with dissolve
    "她开始把屁股往你的裆部上磨，同时始终确保你的鸡巴被牢牢夹在她双腿之间。"
    "她肉感的大腿和不断滴水的淫穴组成的三角，完美地贴合着你的鸡巴，让你每次挺送都陷进去。"
    "她扭动腰肢时屁股在你身上弹跳的触感，足以把你推向临界点。"
    MC "操……我要射了……用手接住。"
    Victoria "好。"
    "你在她双腿之间最后狠狠挺送一次，她用大腿夹紧，把你的鸡巴锁在温暖柔软的肉质钳子里，彻底把你推过了临界点。"
    scene img_main12_247 with vpunch
    pause 0.5
    scene img_main12_247 with vpunch
    pause 0.35
    scene img_main12_247 with vpunch
    pause 0.2
    scene img_main12_247 with vpunch
    pause 0.1
    scene img_main12_247 with vpunch
    pause 0.1
    scene img_main12_247 with flash
    "你把精液全部射进她等着的手里，她顺从地试图全部接住。"
    scene img_main12_248 with dissolve
    "你长长地叹了口气，浑身的紧张都随之流走。"
    scene img_main12_249 with dissolve
    MC "乖女孩。现在可以把墙松开了。"
    scene img_main12_250 with dissolve
    "薇琪和你一样气喘吁吁，整个人瘫坐在长凳上。"
    
    $ renpy.end_replay()

#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_akatsuki1:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/akatsuki_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0

    scene img_main14_281 with dissolve
    "她像真正的猫一样轻盈地滑下台面，跪到你面前。"
    scene img_main14_282 with dissolve
    "你把鸡巴抽出来时，她开始仔细端详它。"
    scene img_main14_283 with dissolve
    Akatsuki "这是我弄的……"
    "那并不是疑问，她现在显然已经知道自己对你做了什么，但听起来还是有点惊讶。"
    scene img_main14_284 with dissolve
    "她伸出手，用指尖试探性地碰了碰它。"
    Akatsuki "好硬……"
    MC "对。那你打算怎么把你的奶弄出来？"
    scene img_main14_285 with dissolve
    "她抬头看了你一眼，然后舔了舔你鸡巴的前端。"
    scene img_main14_286 with dissolve
    Akatsuki "喵？"
    MC "乖小猫。"
    scene vid_main14_1 with dissolve
    "她开始舔你鸡巴的前端，就像猫在舔牛奶一样。"
    scene vid_main14_2 with dissolve
    "她湿润的舌头轻柔地抚过你前端敏感的皮肤，每舔一下都带来一阵麻酥酥的快感。"
    MC "用嘴吸，别只是舔。"
    scene vid_main14_3 with dissolve
    "她张开小嘴，然后缓缓地用双唇包裹住你的鸡巴。"
    Akatsuki "唔嗯……"
    "勉强才塞得下，而她温暖湿润的嘴感觉像是在把你的龟头彻底融化。"
    Akatsuki "唔唔……唔嗯……唔嗯……"
    MCi "（我他妈，这感觉真好……）"
    "你彻底迷失在她吸吮你鸡巴末端的快感里。"
    scene vid_main14_4 with dissolve
    "你低头看去，正要叫她快点，却有什么吸引了你的目光……"
    MCi "（哇，她居然在脸红……）"
    scene vid_main14_5 with dissolve
    "不用你说，她就开始更用力地上下点头。"
    MC "操……乖女孩。"
    Akatsuki "唔唔哼……唔嗯……"
    scene vid_main14_6 with dissolve
    "她的双唇沿着你的鸡巴上下滑动，努力榨出她的奶，而她第一次就意外地把你含得很深。"
    Akatsuki "唔嗯……"
    scene vid_main14_7 with dissolve
    MC "准备好领奖了吗？"
    Akatsuki "唔嗯……"
    scene img_main14_287 with dissolve
    "她用双唇紧紧裹住你鸡巴的前端，形成严密的封闭，开始疯狂地舔吸。"
    "只是一瞬间，你就在她嘴里爆发了。"
    scene img_main14_288 with dissolve
    Akatsuki "唔嗯……唔唔唔唔唔！！"
    scene img_main14_289 with dissolve
    pause 0.5
    scene img_main14_289 with vpunch
    pause 0.35
    scene img_main14_289 with vpunch
    pause 0.2
    scene img_main14_290 with vpunch
    pause 0.1
    scene img_main14_290 with vpunch
    pause 0.1
    scene img_main14_290 with flash
    "当你一股股射进她嘴里时，晓月贪婪地吞下每一滴你的精液。"
    Akatsuki "唔嗯……"
    MC "操……乖小猫。"
    scene img_main14_291 with dissolve
    "她站起来，双臂紧紧抱住你，顺便把你逐渐软下来的鸡巴夹在两人之间。"
    scene img_main14_292 with dissolve
    MCi "（真可爱，看来做完之后她有点黏人。）"

    $ renpy.end_replay()

#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_lucy4:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/lucy_theme.mp3" loop volume 1.2 fadeout 1.0 fadein 1.0
    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main15_489 with dissolve
    "她把胯抬离床面，好让你更容易把她拉下来。"
    scene img_main15_490 with dissolve
    MC "乖女孩。现在跪到我面前来。"
    Lucy "好的！"
    scene img_main15_491 with dissolve
    "露西爽快地跪下，你则把鸡巴从裤子里掏出来。"
    MC "现在你要给我一次你那些拿手的口交。"
    scene img_main15_492 with dissolve
    "她伸手开始撸动你的鸡巴，显然还是有些不熟练，但已经没几分钟前那么紧张了。"
    scene vid_main15_1 with dissolve
    "摸了一会儿之后，她俯下身，用双唇裹住你鸡巴的前端。"
    scene vid_main15_2 with dissolve
    Lucy "唔嗯……"
    MC "和之前不一样，这次你不用让我射出来，好吗？"
    scene vid_main15_3 with dissolve
    Lucy "唔哼？"
    MC "你要让我们两个都准备好。"
    scene vid_main15_4 with dissolve
    MC "想象你的嘴紧紧裹住我的鸡巴，上下移动，把它含进去。过一会儿，含进去的就是你那湿淋淋的小穴了。"
    Lucy "唔嗯嗯……"
    scene vid_main15_5 with dissolve
    "你把手放在她头上，引导她上下快一点。"
    Lucy "唔嗯……"
    scene vid_main15_6 with dissolve
    MC "你的内裤湿透了吗？"
    Lucy "唔哼……"
    scene vid_main15_5 with dissolve
    MC "乖女孩。那就该把你脱光了，接下来可不能让你的新衣服弄脏。"
    Lucy "唔嗯……"
    scene img_main15_493 with dissolve
    "露西把嘴从你的鸡巴上移开，下巴上留下几道细细的唾液痕迹，她尴尬地急忙抹掉。"
    MC "在我面前把衣服脱掉。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main15_494 with dissolve
    "她开始在你面前脱下她那身凌乱衣服最后的部分，全程避开你的目光。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main15_495 with dissolve
    MC "你还是会因为我看你裸体而害羞吗？"
    Lucy "有、有一点……一想到接下来要发生的事，我的心都快炸了……"
    scene img_main15_496 with dissolve
    "你开始把她推回床上，但她拦住了你。"
    scene img_main15_497 with dissolve
    Lucy "呃……"
    MC "怎么了，露西？"
    scene img_main15_498 with dissolve
    Lucy "你、你能……"
    scene img_main15_499 with dissolve
    "她伸出手，又开始手忙脚乱地解你的扣子，但手又抖了起来。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main15_500 with dissolve
    "看到这个情形，你帮她把衣服脱了下来。"
    Lucy "啊……"
    scene img_main15_501 with dissolve
    MC "现在中间什么都没有了。"
    scene img_main15_502 with dissolve
    "你把她进一步推到床上，然后压到她身上，俯身又给了她一个吻——上次这样似乎能让她平静下来。"
    scene img_main15_503 with dissolve
    Lucy "唔嗯嗯……"
    scene img_main15_504 with dissolve
    "你没有像上次那样揉她的胸，而是把手滑进她湿淋淋的大腿之间。"
    "你的手指碰到她的阴蒂，让她一阵战栗并轻轻抽气，但你没有停下。"
    scene img_main15_505 with dissolve
    "你先后滑进一根、两根手指，她一开始绷紧了身体。但过了一会儿就放松下来，甚至开始轻轻用胯磨蹭你的手。"
    Lucy "唔嗯……"
    scene img_main15_506 with dissolve
    "这样过了一会儿，你坐起身，把她的一条腿推开，让鸡巴对准她的小穴。"
    scene img_main15_507 with dissolve
    "你缓慢而刻意地向前顶了一点，刚好足以撩拨她。"
    Lucy "哦——哦……"
    scene img_main15_508 with dissolve
    "你能感觉到她的小穴将会把你的鸡巴裹得多温热，让你忍不住想插进去。"
    "但虽然这份期待对你来说几乎已经难以承受，对露西而言大概还要更甚。"
    scene img_main15_509 with dissolve
    MC "准备好了吗？"
    Lucy "唔嗯……"
    scene img_main15_510 with dissolve
    pause 0.4
    scene img_main15_511 with dissolve
    pause 0.4
    scene img_main15_510 with dissolve
    "你又用鸡巴在她穴口上下蹭了几下。"
    scene img_main15_509 with dissolve
    MC "你确定？"
    scene img_main15_512 with dissolve
    Lucy "是、是的！"
    MC "嗯……我可不觉得。要不要我再撩你一会儿？"
    scene img_main15_513 with dissolve
    Lucy "不、不要！求你了……我想要……我准备好了！"
    "所有的紧张都抛到脑后，露西看起来几乎急切地想让你进入她体内。"
    scene img_main15_514 with dissolve
    "没有再多说什么，你开始缓缓把鸡巴压进她体内。"
    scene img_main15_515 with dissolve
    Lucy "唔唔唔……"
    scene img_main15_516 with dissolve
    "当你插进这个脸红的处女体内时，她脸上浮现出快感与不适交织的神情。"
    scene img_main15_517 with dissolve
    "你小心地缓慢推进，却没有停下，一寸一寸地，你的鸡巴被她温暖湿润紧致的小洞吞没。"
    scene img_main15_518 with dissolve
    Lucy "啊啊啊……啊……"
    scene img_main15_519 with dissolve
    pause
    "她一开始有些挣扎，呼吸也变得急促，但看起来痛苦并没有难以忍受，很快你就整根没入了她体内。"
    scene img_main15_520 with dissolve
    Lucy "唔唔唔……啊……我、我做到了……我真的全部吞进去了……"
    MC "感觉怎么样？"
    scene img_main15_521 with dissolve
    Lucy "满满的……好烫……像是里面在燃烧……"
    MC "记住这种感觉；你现在真的完完全全是我的了。"
    Lucy "唔嗯……你的……永远都是……"
    scene vid_main15_7 with dissolve
    "你缓缓把鸡巴抽出来，再重新推回去，让她慢慢习惯这种感觉。"
    Lucy "唔嗯……啊啊啊……"
    scene vid_main15_8 with dissolve
    "你又用这个节奏持续了一会儿，然后觉得她已经可以承受更多了。"
    "你加快速度时她抽了一口气，你感觉到她的小穴在你柱身上收紧了。"
    scene vid_main15_9 with dissolve
    Lucy "哦……"
    MC "操，你感觉真好。"
    scene vid_main15_10 with dissolve
    "她对上你的视线，并没有像你预料的那样立刻移开，而是仿佛被迷住一般久久停留在你眼里。"
    MC "还紧张吗？"
    "她笑了笑，摇摇头。"
    Lucy "我、我……说不出来……唔嗯……"
    scene vid_main15_11 with dissolve
    "终于，一声轻轻的快感呻吟打断了她的话，她尴尬地移开视线。"
    scene vid_main15_12 with dissolve
    "判断她已经准备好，你开始用又深又快的抽插操她，这似乎让她彻底疯了。"
    Lucy "哈啊啊……你、如果你……我、我唔唔唔……"
    scene vid_main15_13 with dissolve
    MC  "嗯，你第一次就要为我射出来吗？"
    Lucy "我、我……唔嗯……是的！……"
    scene vid_main15_14 with dissolve
    "你继续动作，她的小穴顺从地容纳你鸡巴的每一次抽动，任你随心所欲。"

    menu:
        "慢一点。":
            jump main_15_choice2_slow_replay
        "快一点。":
            jump main_15_choice2_fast_replay
        "深一点。":
            jump main_15_choice2_deep_replay
        "结束。":
            jump main_15_choice2_finish_replay

label main_15_choice2_slow_replay:

    scene vid_main15_19 with dissolve
    pause
    Lucy "唔嗯……"
    Lucy "你、你……让我……唔嗯唔嗯……"

    menu:
        "慢一点。":
            jump main_15_choice2_slow_replay
        "快一点。":
            jump main_15_choice2_fast_replay
        "深一点。":
            jump main_15_choice2_deep_replay
        "结束。":
            jump main_15_choice2_finish_replay

label main_15_choice2_fast_replay:

    scene vid_main15_20 with dissolve
    pause
    Lucy "啊唔嗯！哦——哦……天……我、我的……神……"
    Lucy "[PlayerName]!!"

menu:
        "慢一点。":
            jump main_15_choice2_slow_replay
        "快一点。":
            jump main_15_choice2_fast_replay
        "深一点。":
            jump main_15_choice2_deep_replay
        "结束。":
            jump main_15_choice2_finish_replay
            
label main_15_choice2_deep_replay:

    scene vid_main15_21 with dissolve
    pause
    Lucy "啊唔唔唔唔唔我、我……唔嗯……是的！……"
    Lucy "我、我……好、好深……！"

menu:
        "慢一点。":
            jump main_15_choice2_slow_replay
        "快一点。":
            jump main_15_choice2_fast_replay
        "深一点。":
            jump main_15_choice2_deep_replay
        "结束。":
            jump main_15_choice2_finish_replay
            
label main_15_choice2_finish_replay:
    "没过多久，你感觉到她在你柱身上收紧，然后……"
    scene vid_main15_15 with dissolve
    MC "操……你感觉到了吗，露西。我要射进你体内深处了。"
    Lucy "是的是的唔唔唔……"
    scene vid_main15_16 with dissolve
    "这个念头似乎把她推过了临界点，她的小穴死死夹住你的鸡巴，整个身体都被快感席卷。"
    #pictures, wrap legs around you
    Lucy "唔嗯……唔嗯……我、我要……啊唔唔唔唔！"
    "露西在你鸡巴上高潮的感觉足以让你收尾，你最后又一次整根顶进她体内深处。"
    scene vid_main15_17 with flash
    pause
    "任由体重和肌肉接管，你把她的身体狠狠压进床里，在她痉挛的小穴深处爆发。"
    Lucy "哦唔唔唔唔唔唔唔……"
    scene vid_main15_18 with dissolve
    "你在她体内停留了很久，沐浴在你们共同高潮余韵渐退的感觉里。"
    scene img_main15_522 with dissolve
    "最后你缓缓把鸡巴抽出来，露出你弄出来的那一塌糊涂的精液。"
    Lucy "唔……"

    $ persistent.gallery_lucy4 = True
    $ persistent.replay_PlayerName = PlayerName

    play sound "audio/sounds/bed2.mp3" volume 4.0

    scene img_main15_523 with dissolve
    "心满意足之下，你躺到床上，伸手搂住她，把她拉近。"
    scene img_main15_524 with dissolve
    "她立刻尽可能紧地贴上来依偎着你，你们俩都花了一会儿才让心跳和呼吸恢复平稳。"
    scene img_main15_525 with dissolve
    Lucy "谢谢你……"
    MC "你是我女朋友，不用为和我上床道谢。"
    scene img_main15_526 with dissolve
    Lucy "不、不……谢谢你……让它这么美好……"
    MC "呵，既然你这么喜欢，那准备好第二回合了吗？"
    scene img_main15_527 with dissolve
    Lucy "我、我……如果你想的话……"
    MC "我开玩笑的，你确定没事吗？"
    scene img_main15_528 with dissolve
    Lucy "我、我有点酸痛……"
    MC "那今晚就到这儿吧。不必着急，以后我们会一直这样。"
    scene img_main15_529 with dissolve
    Lucy "嗯……希望如此……"

    $ renpy.end_replay()


#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################

label replay_headmistress1:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/alison_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0

    scene img_main17_133 with dissolve
    "女校长略一迟疑，走上前来，看向那台你还举在胸口的摄像机。"
    Headmistress "我叫埃莉森·吉尔伯特，斯特罗克学院的女校长。"

    $ persistent.characters_headmistress_name = True

    scene img_main17_134 with dissolve
    pause
    scene img_main17_135 with dissolve
    Headmistress "我打算就在这间校长室里，和我的一个学生好好爽一下。"
    scene img_main17_136 with dissolve
    "女校长在你面前跪下，然后抬眼看了你一眼，故意把紧张感拉长。"
    scene img_main17_137 with dissolve
    pause
    scene img_main17_138 with dissolve
    "最后她把你越来越胀的鸡巴从裤子里拉了出来。"
    scene img_main17_139 with dissolve
    Headmistress "嗯……你可真是个大男孩……"
    "她抬头看着你，脸上泛起淡淡的红晕。"
    MC "如果你做这一切是因为觉得这能改变什么，那你不如现在就停下。"
    scene img_main17_140 with dissolve
    Headmistress "嘘。你真是太不擅长服从命令了。"
    scene img_main17_141 with dissolve
    Headmistress "再说了，我很有信心能让你改变主意。"
    scene vid_main17_1 with dissolve
    "女校长最后又抬眼看了你一下，把你鸡巴的前端滑进她温暖湿润的口腔。"
    scene vid_main17_2 with dissolve
    Headmistress "唔嗯……"
    MCi "（我他妈，她技术真好……）"
    scene vid_main17_3 with dissolve
    "仿佛读懂了你的心思，女校长抬头看向你的脸。"
    "尽管她另有目的，但你能感觉到她也从自己口交对你的效果中获得了某种乐趣。"
    scene vid_main17_4 with dissolve
    "这只会促使她把你的鸡巴含得更深。"
    Headmistress "啊唔嗯……"
    "她湿润的嘴和舌头，还有喉咙紧紧箍住你鸡巴前端的收缩感……这真是让人头皮发麻的口交。"
    Headmistress "唔嗯——唔嗯——唔唔唔……"
    scene img_main17_142 with dissolve
    "这样过了一会儿，她停下来再次抬头看你，脸上挂着得意的笑容。"
    scene vid_main17_5 with dissolve
    "她挑衅的笑容触发了你更强势的一面，当她重新开始吮吸时，你不动声色地把手机塞进口袋，腾出一只手。"
    scene img_main17_143 with dissolve
    MC "好了，够了。"
    scene img_main17_144 with dissolve
    Headmistress "唔！啊唔……"
    "你说话时她含着你的鸡巴发出抽气声，而她朝你手上瞥了一眼，知道你已经没有在录了。"
    scene img_main17_145 with dissolve
    "她立刻想要退开，但一只按在她后脑的手拦住了她。"
    MC "你敢。"
    Headmistress "嗯？"
    MC "手放在身侧，埃莉森。"
    Alison "唔呃。"
    scene img_main17_146 with dissolve
    "你叫出她的名字时，她瞪了你一眼，但还是按命令把手放到了身侧。"
    scene img_main17_147 with dissolve
    MC "我觉得你该知道一些关于我的事。"
    Alison "嗯？"
    scene vid_main17_6 with dissolve
    "你把另一只手放在她头上，慢慢把你的鸡巴推进她的喉咙。"
    Alison "唔唔唔嗯！"
    MC "我不是那种因为你口交好就任你踩在头上的人。"
    MC "所以现在要按我的方式来。我们看看你能坚持多久才认输，如何？"
    Alison "唔嗯。"
    scene vid_main17_7 with dissolve
    "埃莉森同意了——至少在她的鸡巴完全卡在脖子里的情况下，她还能表示同意。"
    scene vid_main17_8 with dissolve
    "你逐渐加快、加深，等着她随时伸手把你推开，但她始终没有。"
    Alison "唔唔唔嗯？"
    scene vid_main17_9 with dissolve
    "你看不见埃莉森的脸，而且你确信现在她的表情一定是一塌糊涂、一点也不可爱，但从她发出的声音你能想象她在说「就这点本事？」"
    MCi "（我他妈，她好像根本没有呕吐反射一样。）"
    scene vid_main17_10 with dissolve
    "她深喉吞咽你鸡巴的感觉变得无比强烈，过了一会儿你能看出她开始有些吃力，尽管她不肯承认。"
    Alison "唔唔呃呃唔……"
    scene vid_main17_11 with dissolve
    MC "再坚持一下，埃莉森，我要射了。"
    Alison "唔唔呃呃……"
    "你感觉到她的喉咙开始在你鸡巴上收紧、抽搐，因为她终于开始呛了。"
    MC "操……"
    scene img_main17_148 with dissolve
    Alison "唔唔呃呃呃！！！"
    scene img_main17_149 with dissolve
    "就在你要射进她喉咙之前，埃莉森终于推开你大口喘气。而她对你鸡巴最后的吸吮与舔舐，逼得你把精液全射在她脸上。"
    scene img_main17_150 with vpunch
    pause 0.5
    scene img_main17_151 with vpunch
    pause 0.35
    scene img_main17_152 with vpunch
    pause 0.2
    scene img_main17_152 with vpunch
    pause 0.1
    scene img_main17_153 with vpunch
    pause 0.1
    scene img_main17_153 with flash
    pause
    scene img_main17_154 with dissolve
    "你一松手，她就瘫倒在地大口喘气。"
    Alison "啊——……啊——……啊啊唔……"
    "她瘫坐着深深呼吸了好一阵子，才终于缓过气能说话。"
    scene img_main17_155 with dissolve
    Alison "我他妈……你想狠起来还真狠……"

    $ renpy.end_replay()

#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################

label replay_victoria3:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/victoria_theme.mp3" loop volume 1.0 fadeout 1.0 fadein 1.0

    scene img_main16_424 with dissolve

    MC "准备好你的第一次口交了吗？"
    Victoria "唔嗯……你准备好了吗？"
    MC "当然。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main16_426 with dissolve
    "不用吩咐，薇琪就自己翻身坐下，脱掉高跟鞋和牛仔裤。"
    MC "有人有点太着急了。我可不想看见你没经允许就自己摸。"
    scene img_main16_427 with dissolve
    Victoria "你说什么都行，主人……"
    scene img_main16_428 with dissolve
    "她的声音渐渐低下去，你靠回沙发上，把勃起的鸡巴从牛仔裤里掏了出来。"
    MC "你在犹豫啊，薇琪。要不要我把露西叫下来示范给你看？"
    scene img_main16_429 with dissolve
    Victoria "哼呃。" 
    scene img_main16_430 with dissolve
    "薇琪气鼓鼓地哼了一声，张大嘴巴，第一次用双唇裹住你鸡巴的前端。"
    scene img_main16_431 with dissolve
    "有那么一瞬间，你迷失在她温暖湿润的舌头试探性抚过你鸡巴下侧的纯粹丝滑快感里。"
    scene vid_main16_1 with dissolve
    Victoria "唔嗯……"
    MC "操……乖女孩。"
    Victoria "唔嗯……"
    scene vid_main16_2 with dissolve
    MC "想试试再含深一点吗？"
    scene vid_main16_3 with dissolve
    Victoria "嗯？什、什么话……"
    MC "嘴里含着鸡巴说话的感觉还挺不赖……但我完全不知道你刚说了什么……"
    scene img_main16_432 with dissolve
    Victoria "啊……"
    Victoria "我说的是再深一点我就会『噎住』……"
    MC "那正是乐趣的一部分。"
    Victoria "抖M狂魔……"
    scene vid_main16_3 with dissolve
    Victoria "唔嗯……"
    MC "受虐狂。"
    Victoria "唔嗯……"
    scene vid_main16_4 with dissolve
    "薇琪试着含深了几次，每一次都能再深一点。"
    Victoria "唔嗯……"
    "她最终没能真的让自己噎到。不过作为第一次已经做得很好了，而她的嘴为你带来的快感令人陶醉。"
    scene img_main16_433 with dissolve
    "薇琪热切地为你口交时，你向后靠去，让那美妙的感觉将自己淹没……"
    scene img_main16_434 with dissolve
    "结果你的视线正好对上从上方偷看你的露西。"
    scene img_main16_435 with dissolve
    "她笑了笑，尴尬地移开视线，随即飞快地翻过栏杆，消失在卧室的黑暗里。"
    MCi "（先是晓月，现在又是薇琪。她喜欢看吗？）"
    scene vid_main16_5 with dissolve
    "你低头回看，发现薇琪的左手正在做不该做的事……"
    scene img_main16_437 with dissolve
    pause
    scene img_main16_438 with dissolve
    pause
    scene vid_main16_5 with dissolve
    MC "你现在纯粹是在求罚了，对吧？"
    Victoria "唔唔嗯？"
    "你感觉如果不是嘴里塞得这么满，她现在肯定正坏笑着。"
    scene img_main16_439 with dissolve
    "你的心思立刻飘到了沙发旁边的那个盒子上……"
    scene img_main16_440 with dissolve
    "你把手放在她脑袋侧面，把她的嘴从鸡巴上带开，薇琪没有反抗。"
    scene img_main16_441 with dissolve
    Victoria "啊……怎么了吗，主人？"
    MC "不听话的坏奴隶通常该受罚，不过我给你准备了个礼物。"
    scene img_main16_442 with dissolve
    "你滑到沙发一端，从玩具盒里拿出什么东西，全程不让她看见给她准备的是什么；她则带着调皮的微笑看着你。"
    MC "面朝前。"
    scene img_main16_443 with dissolve
    pause
    scene img_main16_444 with dissolve
    pause
    scene img_main16_445 with dissolve
    pause
    scene img_main16_446 with dissolve
    "她转过身，你蹲到她身边，在她耳边低声说。"
    MC "把手放到背后。"
    Victoria "唔嗯，好的，主人。"
    scene img_main16_447 with dissolve
    "她顺从地把双手放到背后，靠绷紧大腿的肌肉在没有支撑的情况下保持站立。"

    play sound "audio/sounds/handcuff.mp3" volume 2.0

    scene img_main16_448 with dissolve
    "过了一会儿，你把手铐套上她的手腕。"
    scene img_main16_449 with dissolve
    Victoria "这不公平，主人！"
    scene img_main16_450 with dissolve
    pause

    play sound "audio/sounds/spank_mid2.mp3"

    scene img_main16_451 with vpunch
    "{i}啪！{/i}"
    scene img_main16_452 with dissolve
    "你回到座位上，居高临下地朝被束缚的女奴女友咧嘴笑。"
    MC "我刚送了你一份礼物，你不该谢谢我吗？"
    scene img_main16_453 with dissolve
    "薇琪瞪了你一眼，然后再次俯身对上你的鸡巴。"
    scene img_main16_454 with dissolve
    Victoria "唔嗯……这样真的不一样……有点吓人……"
    scene img_main16_455 with dissolve
    "她只用了一瞬就克服了无法自控的处境，在把你重新弄回嘴里之前，先朝你投来一个凶悍的笑容——这次没有任何手可以借力。"
    scene vid_main16_6 with dissolve
    Victoria "唔嗯……"
    "她的嘴再次吞没你鸡巴的感觉让你完全没了继续玩下去的念头，现在你只想射在她湿润丝滑的嘴里。"
    scene vid_main16_7 with dissolve
    MC "操……乖女孩。"
    "没有手可以擦，薇琪的脸弄得一塌糊涂，唾液从嘴角溢出，双唇在你柱身前端上卖力地翻动。"
    scene vid_main16_8 with dissolve
    "有那么一瞬间你想伸手按住她的头把鸡巴强行插深，但你想起来这是她的第一次，或许该让她自己掌握节奏。"
    Victoria "唔唔唔……"
    MC "看着我。"
    scene vid_main16_9 with dissolve
    "尽管头还在你的鸡巴上上下起伏，她的眼睛还是抬起来对上了你的视线。"
    scene vid_main16_10 with dissolve
    "但她只维持了一瞬间的对视，就尴尬地低下头。"
    MC "那副害羞的样子他妈的太可爱了。"
    Victoria "唔呃……唔嗯……"
    scene vid_main16_11 with dissolve
    "想到你那嚣张下流的女孩，害羞的一面正暴露在你鸡巴的顶端，把你推向临界点……"
    scene vid_main16_12 with dissolve
    "但最终让她温暖湿润的嘴尽职服务你的感觉，让结局变得不可避免。"
    scene vid_main16_10 with dissolve
    MC "操……我快了……"
    Victoria "唔唔唔……"
    scene vid_main16_13 with dissolve
    "听到这话，薇琪加快了速度，替你擅自决定好是射脸上还是射嘴里。"
    scene vid_main16_14 with flash
    "她最后热情的吸吮逼得你在她嘴里爆发。"
    MC "操……"
    Victoria "唔嗯……"
    "你从高潮中缓下来，肌肉逐渐放松，薇琪则尽力把你的存货吞下去。"
    MC "你全吞下去了？"
    Victoria "唔嗯……"
    MC "给我看看。"
    scene img_main16_456 with dissolve
    "她从你的鸡巴上退开，张开嘴。"
    scene img_main16_457 with dissolve
    Victoria "啊……"
    MC "乖女孩。现在你只需要把我弄干净……"
    scene img_main16_458 with dissolve
    Victoria "手铐让这件事有点难办……"
    MC "我相信你想得出办法。"
    scene img_main16_459 with dissolve
    Victoria "唔嗯……"
    scene img_main16_460 with dissolve
    "她试探着俯身，舔了你渐渐软下去的鸡巴几下，然后又轻轻含吮了几下，尽力清理她第一次口交留下的痕迹。"
    MC "乖女孩，这样就行。"
    scene img_main16_461 with dissolve
    "最后，她做了一件意外亲密的事——亲了亲你鸡巴的前端，然后站了起来。"

    $ renpy.end_replay()

#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_akatsuki2:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0

    scene img_black with fade
    Lucy "小、小心点……你会把他吵醒的……"
    "你被露西轻声说话的声音弄醒了。"

    play sound "audio/sounds/bed.mp3" volume 4.0

    "过了一会儿，你感觉床垫一动，有人把体重压到了你旁边的床上。"
    scene img_main15_1 with fade
    "你睁开眼，映入眼帘的是晓月正小心地把你的鸡巴从内裤里掏出来。"
    scene img_main15_2 with dissolve
    MC "早安……"
    scene img_main15_3 with dissolve
    Lucy "啊……"
    scene img_main15_4 with dissolve
    "晓月没有回答，她嘴里已经塞满了。"
    scene img_main15_5 with dissolve
    Akatsuki "唔唔唔……"
    scene img_main15_6 with dissolve
    Lucy "呃……"
    MC "你好像很惊讶？放她进来的人可是你啊。"
    Lucy "我、我不知道她想要的是这个！"
    scene img_main15_8 with dissolve
    "晓月用她那张湿漉漉的小嘴在你的鸡巴上大显身手，你的注意力很快就被从露西身上拽走了。"
    scene img_main15_9 with dissolve
    Lucy "呃……那我去楼下等着。"
    scene img_main15_6 with dissolve
    MC "不行。过来。"
    scene img_main15_7 with dissolve
    Lucy "真、真的吗？"
    MC "对。坐到床上。"

    play sound "audio/sounds/bed2.mp3" volume 4.0

    scene img_main15_10 with dissolve
    Lucy "好、好的……"
    scene img_main15_11 with dissolve
    MC "还记得我告诉过你，如果我让你做任何你不舒服的事，要说出来吗？"
    Lucy "记得……"
    MC "记住这一点。现在，把上衣脱掉。晓月你也是。"

    
    play sound "audio/sounds/clothing.mp3" volume 3.0

    scene img_main15_12 with dissolve
    pause
    scene img_main15_13 with dissolve  
    "露西看起来有些犹豫，晓月却立刻照做。"
    scene img_main15_14 with dissolve
    MC "你对这种事倒是意外地自在嘛，晓月。"
    Akatsuki "唔嗯。"
    MC "别这样，我知道你想说的时候能说更多。"
    scene img_main15_15 with dissolve
    "偏偏让她开口说话就会让晓月脸红，于是她明显是想逃避继续开口，又低头去吸你的鸡巴。"
    Lucy "啊……呃……你看起来好舒服……"
    scene img_main15_16 with dissolve
    "你抬头看向露西，发现她正带着神秘的微笑打量你的脸。"
    scene img_main15_17 with dissolve
    Lucy "好、好的……"

    play sound "audio/sounds/clothing.mp3" volume 3.0

    scene img_main15_18 with dissolve
    "下定决心后，她把上衣从头上脱了下来。"
    scene img_main15_19 with dissolve
    MC "操……乖女孩。"
    Lucy "呃，然后呢？"
    MC "过来。"
    scene img_main15_20 with dissolve
    "露西俯下身，你把她拉进一个深吻。"
    scene img_main15_21 with dissolve
    "你把舌头伸进露西嘴里，与此同时晓月还在热情地为你口交。"
    scene img_main15_22 with dissolve
    Lucy "唔唔唔嗯……"
    scene img_main15_23 with dissolve
    Akatsuki "唔唔唔……"
    scene img_main15_24 with dissolve
    pause
    scene img_main15_25 with dissolve
    "过了很久你们才分开这个吻，露西坐直身子时立刻显得有些局促。"
    MC "你不喜欢这样吗？"
    scene img_main15_26 with dissolve
    Lucy "我、我……我最喜欢亲你了！"
    MC "但是？"
    scene img_main15_27 with dissolve
    Lucy "可、可是当着别人的面做这种事太羞人了！你们两个一点都不羞耻吗？"
    MC "不会。晓月呢？"
    scene img_main15_28 with dissolve
    Akatsuki "唔嗯……"
    MC "我猜那是否定的。"
    scene img_main15_29 with dissolve
    Lucy "我、我倒是……"
    MC "羞到连一分钟都不肯和晓月换位置吗？"
    scene img_main15_30 with dissolve
    Lucy "对！"
    scene img_main15_29 with dissolve
    Lucy "可、可是……我试试看……"
    MC "乖女孩。"
    scene img_main15_28 with dissolve
    MC "过来，小猫。"
    scene img_main15_31 with dissolve
    "晓月不情愿地把嘴从你鸡巴上移开，然后挪近你。"
    scene img_main15_32 with dissolve
    "露西迅速接过位置，用自己的双唇裹住你的鸡巴。"
    scene img_main15_33 with dissolve
    Lucy "唔嗯嗯……"
    "她的紧张显然很厉害，但感觉还是很好的。"
    scene img_main15_34 with dissolve
    MC "我不是在抱怨，不过现在还挺早的。你来这儿只是为了给我口交吗？"
    scene img_main15_35 with dissolve
    Akatsuki "唔嗯。"
    MC "把话说出来，小猫。"
    scene img_main15_36 with dissolve
    "她又一次脸红，移开了视线。"
    Akatsuki "我……喜欢。"
    MC "你喜欢我的鸡巴？"
    scene img_main15_37 with dissolve
    Akatsuki "唔嗯……那次我们玩卡牌、我坐在你身上的时候……我能感觉到……我一直忍不住想那件事……"
    scene img_main15_38 with dissolve
    MC "靠……听着真舒服，露西。"
    scene img_main15_39 with dissolve
    "发现你们俩都在低头看她，露西紧张了起来，停了下来。"
    scene img_main15_40 with dissolve
    Lucy "我、我没法在你们两个都看着的情况下做！"
    MC "好吧，换位置。"
    scene img_main15_41 with dissolve
    "两个女孩开心地换回位置，露西再一次坐到你身边。"
    scene img_main15_42 with dissolve
    MCi "（她也许不好意思自己做，但她的眼睛一刻也离不开正在做的晓月。）"
    MC "你喜欢看吗？"
    scene img_main15_43 with dissolve
    Lucy "我……喜欢她让你舒服的样子……"
    MC "靠，怎么会……"

    play sound "audio/sounds/phonecall.mp3" loop volume 3.0

    scene img_main15_44 with hpunch
    Phone "*嗡嗡嗡。嗡嗡嗡。嗡嗡嗡。*"

    stop sound

    MC "每天早上都这样！"
    scene img_main15_45 with dissolve
    MC "把手机给我，露西。"
    scene img_main15_46 with dissolve
    MC "是莎拉，先等一下，小猫。"

    stop sound

    scene img_main15_47 with dissolve
    "晓月停下，你接起电话……"
    scene img_main15_48 with dissolve
    "但你一接起，她立刻又开始吸你的鸡巴。"
    scene img_main15_49 with dissolve
    Akatsuki "唔唔唔……"
    scene img_main15_50 with dissolve
    MC "啊……操……"
    scene img_main15_51 with dissolve
    SarahPhone "这算哪门子打招呼？"
    scene img_main15_50 with dissolve
    MC "怎么了，莎拉？"
    scene img_main15_51 with dissolve
    SarahPhone "你还是会来陪我一起走吧？"
    scene img_main15_50 with dissolve
    MC "呃……会。"
    scene img_main15_51 with dissolve
    SarahPhone "你不用听起来这么不耐烦吧！我又没叫你来接我……"
    scene img_main15_50 with dissolve
    MC "啊……不是，我只是累了。"
    scene img_main15_51 with dissolve
    Akatsuki "{i}*啾{/i}唔嗯……"
    scene img_main15_50 with dissolve
    SarahPhone "那是什么声音？"
    scene img_main15_51 with dissolve
    MC "没什么……别管它。"
    scene img_main15_50 with dissolve
    SarahPhone "不许骗我！"
    scene img_main15_51 with dissolve
    MC "好吧，那是晓月吸我鸡巴的声音。我一小时后到。"
    scene img_main15_52 with dissolve
    SarahPhone "我的天！你太恶心了！我真不敢相信……"
    scene img_main15_53 with dissolve
    "你挂断了莎拉的电话。"
    scene img_main15_54 with dissolve
    Lucy "那、那样可以吗？"
    scene img_main15_55 with dissolve
    MC "操……没办法，我快了。"
    scene img_main15_56 with dissolve
    Akatsuki "唔嗯……"
    scene img_main15_42 with dissolve
    Lucy "我、我……"
    scene img_main15_57 with dissolve
    MC "过来。"
    scene img_main15_58 with dissolve
    "露西依偎进你怀里，你揉捏着她的一只大奶子，而晓月则把你推向终点。"
    scene img_main15_59 with dissolve
    Lucy "啊……"
    scene img_main15_60 with dissolve
    "出乎意料的是，露西似乎完全移不开盯着那只猫娘为你口交的目光，但晓月的服务让你太过分心，顾不上多想。"
    scene img_main15_61 with dissolve
    Akatsuki "唔嗯……"
    scene img_main15_62 with dissolve
    "她丝滑湿润的嘴在你的柱身上最后滑动了几下，然后你就在她体内爆发了。"
    scene img_main15_63 with dissolve
    pause 0.5
    scene img_main15_64 with dissolve
    pause 0.35
    scene img_main15_64 with vpunch
    pause 0.2
    scene img_main15_64 with vpunch
    pause 0.1
    scene img_main15_64 with vpunch
    pause 0.1
    scene img_main15_64 with flash
    Akatsuki "唔嗯。"
    scene img_main15_62 with dissolve
    Lucy "唔哼……"
    scene img_main15_61 with dissolve
    MC "操……"
    scene img_main15_65 with dissolve
    "你向后躺下，任高潮的剧烈感受慢慢退去，晓月则在露西的另一侧依偎过来。"

    $ renpy.end_replay()


#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_lucy5:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/lucy_theme.mp3" loop volume 1.2 fadeout 1.0 fadein 1.0

    Lucy "呃，我、我知道你讨厌紧身裤……所、所以……"
    scene img_main18_46 with dissolve
    "她一边说，一边把你的手拉到桌子底下，然后按在她的大腿上。"
    "薄薄的布料、厚实的肩带和柔软的裸肤，三种截然不同的触感同时冲击着你。"
    scene img_main18_47 with dissolve
    Lucy "我、我……这是买给你的……"
    MC "靠，你真是个了不起的女朋友。"
    scene img_main18_48 with dissolve
    Lucy "啊……"
    MC "但现在你最好专心听课，我们可不想让你漏掉作业上的内容，对吧？"
    scene img_main18_49 with dissolve
    Lucy "啊，对哦……"
    scene img_main18_50 with dissolve
    "露西假装当真，转头看向教室前方的田村老师……"
    scene img_main18_51 with dissolve
    "而桌子底下，你的手抚摸着她的腿，跨越着布料与肌肤的界线。"
    scene img_main18_52 with dissolve
    "这节课还长得很，所以你慢慢来，一次次让露西习惯你伸进她双腿之间的手，然后再用轻轻一捏提醒她。"
    scene img_main18_53 with dissolve
    "每一次似乎都让她重新受到一次冲击，强行把她的注意力从眼前乏味的课程，转移到下面那档感官活动上。"
    scene img_main18_54 with dissolve
    pause
    scene img_main18_55 with dissolve
    pause
    scene img_main18_56 with dissolve
    "最终，在上午课程过半时，你把手继续往她大腿上滑，享受着越往上她的皮肤越柔软、越敏感的感觉。"
    scene img_main18_57 with dissolve
    pause
    scene img_main18_56 with dissolve
    pause
    scene img_main18_57 with dissolve
    pause
    scene img_main18_58 with dissolve
    "当然，你的手最终到达了目的地，你慢慢从揉她的大腿内侧，转为隔着潮湿的内裤揉弄她小穴的边缘。"
    scene img_main18_59 with dissolve
    Lucy "啊唔……"
    scene img_main18_60 with dissolve
    "你再一次把撩拨拉长，注意到露西的呼吸在假装专心听田村老师讲话时微微变重。"
    scene img_main18_61 with dissolve
    "最后你把手指滑过她的小丘，开始隔着湿透的布料上下描摹她小穴的形状"
    scene img_main18_62 with dissolve
    pause
    scene img_main18_61 with dissolve
    pause
    scene img_main18_62 with dissolve
    pause
    scene img_main18_63 with dissolve
    pause
    scene img_main18_59 with dissolve
    Lucy "唔嗯嗯……"
    scene img_main18_63 with dissolve
    "你稍微用力按下去，指尖连同她的内裤陷得更深，露西专注的外表开始出现破绽。"
    scene img_main18_64 with dissolve
    "离午休还有大约二十分钟时，你终于把她的内裤拨到一边，露出下面湿淋淋的一团。"
    scene img_main18_65 with dissolve
    "你立刻转而揉弄她此刻暴露在外的小穴。"
    scene img_main18_66 with dissolve
    pause
    scene img_main18_65 with dissolve
    pause
    scene img_main18_66 with dissolve
    pause
    scene img_main18_67 with dissolve
    "露西的挣扎终于结束，她彻底放弃了听课，在偷看你和害羞地闭上眼睛之间来回切换。"
    scene img_main18_71 with dissolve
    pause
    scene img_main18_68 with dissolve
    "但当你把手指滑进她体内时，她的眼睛猛地睁开，发出了一声稍微大了点的抽气。"
    Lucy "啊唔嗯！"
    scene img_main18_70 with dissolve
    Lucy "在、在里面？"
    "她有些慌乱地低声对你说，因为你似乎比她预想的走得更远。"
    MC "对，就在这里。只剩二十分钟就午休了，我确定你能撑那么久，对吧？"
    scene img_main18_68 with dissolve
    Lucy "哦——天啊……"
    scene img_main18_72 with dissolve
    "作为回应，你开始缓缓地在她紧致的小穴里进出手指。"
    scene img_main18_73 with dissolve
    pause
    scene img_main18_72 with dissolve
    pause
    scene img_main18_73 with dissolve
    pause
    scene img_main18_74 with dissolve
    "下次你抬头看她的表情时，发现她正咬着笔，努力在满屋子的注视下被手指插入时保持尽可能安静。"
    scene img_main18_75 with dissolve
    "她与快感抗争的样子只会催你加快，但声响和动静都可能引人注目，于是你满足于缓慢而有意的节奏。"
    "不过提升强度还有别的办法，当你把第二根手指推进她紧致的小穴时，露西又发出一声压抑的抽气。"
    scene img_main18_76 with dissolve
    Lucy "唔唔……"
    scene img_main18_77 with dissolve
    "露西终于彻底放弃伪装，最后几分钟一直抱着你的手臂，拼尽全力只为在教室后排不被人察觉。"
    scene img_main18_78 with dissolve
    "不过她的努力并非完全成功，你注意到汉娜正用一种无法解读的表情盯着你。"
    MCi "（她肯定看得出我们在干什么……但只是汉娜而已，应该没问题，对吧？）"
    scene img_main18_79 with dissolve
    "关于汉娜的念头很快从你脑海中消散，你把全部注意力重新放回被压倒的女友身上，度过这节课最后几分钟。"
    scene img_main18_80 with dissolve
    "你温柔地勾动手指在她体内进出，她的小穴随之收缩，而她身体的其余部分则因禁忌的快感而绷紧颤抖。"
    scene img_main18_81 with dissolve
    "田村老师终于宣布午休开始，人们陆续走出教室。"
    scene img_main18_82 with dissolve
    "你看向汉娜原本坐的位置，发现她已经走了。取而代之的是，你的视线对上了薇琪，而露西还挂在你手臂上，你的手指仍深深留在她体内。"
    scene img_main18_83 with dissolve
    MC "抱歉，薇琪，今天你和别的姑娘们得自己吃午饭了，没我和露西陪。"
    scene img_main18_84 with dissolve
    Victoria "哈，好吧。玩得开心，主人……"
    scene img_main18_85 with dissolve
    Victoria "你也是，露西。"
    scene img_main18_86 with dissolve
    Lucy "啊……唔嗯……"
    scene img_main18_87 with dissolve
    "薇琪朝你露出一个心照不宣的笑容，独自走出了教室。"
    scene img_main18_88 with dissolve
    "最后在她脉动、丝滑湿润的小穴里深按了几下后，你把手指从露西体内抽离，她积蓄的紧张顿时像大坝决口一般爆发。"
    scene img_main18_89 with dissolve
    Lucy "啊……哦——哦我的天……"
    scene img_main18_90 with dissolve
    Lucy "唔嗯？"
    scene img_main18_91 with dissolve
    MC "跟我来。"
    scene img_main18_92 with dissolve
    "你把她拉起来，她看起来有点摇晃，但她任由你带她走出教室；一踏进拥挤的走廊，她又抱住了你的手臂。"
    scene img_main18_93 with dissolve
    pause

    play ambiance "audio/ambiance/school_corridor.mp3" volume 0.5 loop fadeout 1.0 fadein 1.0

    scene img_main18_94 with dissolve
    pause

    stop ambiance
    play sound "audio/sounds/door_delay.mp3"

    scene img_main18_95 with fade
    pause
    scene img_main18_96 with dissolve
    pause
    scene img_main18_97 with dissolve
    pause
    scene img_main18_98 with dissolve
    "你带她上楼，沿着那条熟悉的走廊，最后把她拉进那间熟悉的社团室。"
    MC "我真的很喜欢你送我的礼物。"
    scene img_main18_99 with dissolve
    Lucy "嘿嘿，我看出来了。"
    MC "而现在只剩我们两个了……"
    scene img_main18_100 with dissolve
    Lucy "唔嗯……"

    play sound "audio/sounds/bed2.mp3" volume 6.0

    scene img_main18_101 with dissolve
    "你在沙发上坐下，双手扶着她的胯，让露西站到你面前。"
    scene img_main18_102 with dissolve
    MC "现在，让我看看这里都有什么。"
    scene img_main18_103 with dissolve
    pause
    scene img_main18_104 with dissolve
    pause
    scene img_main18_105 with dissolve
    pause
    scene img_main18_106 with dissolve
    pause
    scene img_main18_107 with dissolve
    "你把她的裙子卷到足够高，好仔细看看她新买的连裤袜。"
    scene img_main18_108 with dissolve
    MC "靠……你以后再也不准穿紧身裤了。"
    scene img_main18_109 with dissolve
    Lucy "好、好的，再也不穿了。"
    MC "乖女孩。"
    scene img_main18_110 with dissolve
    "你用两根手指沿着她湿淋淋的大腿内侧向上滑，露西因这一触而轻轻战栗。"
    scene img_main18_111 with dissolve
    pause
    scene img_main18_112 with dissolve
    MC "看来你真的很喜欢今天上午那节课。"
    scene img_main18_113 with dissolve
    Lucy "啊……我一直好怕被人发现……脑子里什么都想不了……"
    MC "不过现在这里没有别人了。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main18_114 with dissolve
    "你一边说，一边轻轻把她的内裤往下拉，露西把双腿稍稍并拢，好让你更方便。"
    scene img_main18_115 with dissolve
    "最后她依次抬起双腿，让你把它们彻底脱下来扔到一旁。"
    scene img_main18_116 with dissolve
    Lucy "会、会有人进来的……"
    scene img_main18_117 with dissolve
    MC "确实。好吧，那你的裙子可以留着。"
    MC "转过来，坐到我腿上。"
    scene img_main18_118 with dissolve
    Lucy "好、好的……"
    scene img_main18_119 with dissolve
    pause
    scene img_main18_120 with dissolve
    pause
    scene img_main18_121 with dissolve
    pause   
    scene img_main18_122 with dissolve
    "露西面朝门坐在你腿上，你把硬得过分的鸡巴掏出来，让它抵住她的屁股。"
    scene img_main18_123 with dissolve
    Lucy "啊……"
    scene img_main18_124 with dissolve
    MC "准备好第二次了吗？"
    scene img_main18_125 with dissolve
    Lucy "可万一有人进来怎么办？"
    MC "会来这里的只有你和莎拉，对吧？"
    scene img_main18_126 with dissolve
    Lucy "大概吧……"
    MC "那就没问题。"
    MC "站起来。"
    scene img_main18_127 with dissolve
    Lucy "好……"
    scene img_main18_128 with dissolve
    "露西站在你面前，裙子还卷在毛衣下面。"
    scene img_main18_129 with dissolve
    pause
    scene img_main18_130 with dissolve
    "你用手扶着她的胯稍作引导，让她的小穴恰好悬在你涨硬鸡巴的前端上方。"
    scene img_main18_131 with dissolve
    MC "靠，我现在就想埋进你体内……但我想让你来掌握节奏，好吗？"
    Lucy "好、好的……呃……"
    scene img_main18_132 with dissolve
    "露西迟疑地往后挪，笨拙地体验着这些她从未有过的动作。"
    scene img_main18_133 with dissolve
    pause
    scene img_main18_134 with dissolve
    "她终于让前端抵在自己的穴口，然后缓缓地沿你的柱身往下坐。"
    pause
    scene img_main18_135 with dissolve
    pause
    "过去几个小时你一直在撩拨玩弄她，所以她早就准备好了，但被你撑开时她还是小小地抽了口气。"
    scene img_main18_136 with dissolve
    Lucy "啊啊啊……"
    scene img_main18_137 with dissolve
    "她继续痛苦地缓慢吞入，直到……"
    scene img_main18_138 with vpunch
    Lucy "啊唔唔唔！……哦——我的天……"
    "露西自己似乎变得不耐烦，最后干脆一下坐到底，把剩下的全都吞了进去。"
    "你的鸡巴被深爱你的女友温暖湿润的小穴吞没时，一阵兴奋贯穿全身。深埋在她体内的感觉实在令人战栗。"
    scene img_main18_139 with dissolve
    MC "疼吗？"
    Lucy "唔哼……有一点……"
    scene img_main18_140 with dissolve
    Lucy "我觉得我永远都习惯不了这个……"
    MC "好的那种习惯不了？"
    scene img_main18_141 with dissolve
    Lucy "唔哼……又感觉好满……"
    MC "这才是你该待的地方，我的鸡巴整根埋在你紧致的小穴里。"
    Lucy "唔嗯……是的。"
    scene img_main18_142 with dissolve
    MC "不过，有一件事还可以改进……"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main18_143 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main18_144 with dissolve
    "你伸手绕到露西身后，把她的校服拉上去，接着是那件蕾丝红内衣，释放出她那对惊人的巨乳。"
    scene img_main18_145 with dissolve
    Lucy "啊……"
    scene img_main18_146 with dissolve
    pause
    scene img_main18_147 with dissolve
    Lucy "唔嗯……"
    "你花了一点时间揉捏她沉甸甸的乳房，而露西就这样被你的鸡巴钉在原地，随着你双手调整她的重心轻轻前后摇晃。"
    scene img_main18_148 with dissolve
    MC "好了露西，准备好真正动起来了吗？这个姿势下你得自己费很多力气。"
    scene img_main18_149 with dissolve
    Lucy "唔嗯，好吧……"
    "你把手撤回到下面，让露西不受阻碍地沿你的鸡巴上下滑动。"

    # FIRST VIDEO START HERE

    scene vid_main18_1 with dissolve
    pause
    "一开始她动得很慢，每当鸡巴离开时都发出失望的声音，只有在重新坐下、被再次撑开时才会小小地抽气。"
    Lucy "啊……唔嗯……啊……啊唔嗯……"
    scene vid_main18_2 with dissolve
    pause
    "对你来说，她紧致、温暖、湿透的小穴上下滑动、里面紧绷着收缩着裹住你鸡巴的感觉，同样也让人难以招架。"
    scene vid_main18_3 with dissolve
    MC "操，露西……这感觉真爽。"
    Lucy "唔嗯……"

    play sound "audio/sounds/door.mp3"

    scene img_main18_150 with dissolve
    "就在你快要失去自我时，门被推开的声音让你们俩瞬间慌了神。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main18_151 with dissolve
    pause
    scene img_main18_152 with dissolve
    "露西还钉在你的鸡巴上，却猛地合拢双腿，手忙脚乱地把裙子拉下来。"
    scene img_main18_153 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main18_154 with dissolve
    "与此同时你迅速伸手把她的毛衣拉下来遮住胸口，虽然已经来不及整理她的内衣了。"
    scene img_main18_155 with dissolve
    pause
    scene img_main18_156 with dissolve
    "让你们俩都没想到的是，进来的并不是莎拉。"
    MCi "（操……）"
    scene img_main18_157 with dissolve
    Rachel "你们在干什么？"
    Lucy "啊，我、我……我……"
    "露西彻底慌了神，一个完整的词都说不出来。"
    MC "你想怎样，瑞秋？"
    scene img_main18_158 with dissolve
    Rachel "我要你被开除！"
    MC "我建议你去找女校长理论这件事。"
    scene img_main18_159 with dissolve
    Rachel "我会的！这次你别想逃过去！"
    MC "纯粹好奇一下，我到底被指称做了什么？"
    scene img_main18_160 with dissolve
    Rachel "你还不知道吧！我已经收到举报，说你今天上午在教室里对露西动手动脚！"
    "瑞秋喋喋不休时，一个淘气的念头掠过你的脑海……"
    scene img_main18_161 with dissolve
    pause
    scene img_main18_162 with dissolve
    "你轻轻向上顶了露西一下，足以让她感觉到，却不至于让瑞秋察觉。"
    scene img_main18_163 with dissolve
    Lucy "啊……哦唔……"
    scene img_main18_164 with dissolve
    Rachel "看吧，那个反应就是证据！"
    MC "证明什么？我刚才没在听……"
    scene img_main18_165 with dissolve
    pause
    scene img_main18_166 with dissolve
    "你又把鸡巴往上顶进露西体内，又引出一声压抑的呻吟。"
    scene img_main18_167 with dissolve
    Lucy "啊唔嗯……"
    scene img_main18_168 with dissolve
    Rachel "你傻了吗？我说了我收到举报，说你在教室里对露西动手动脚！"
    scene img_main18_169 with dissolve
    MC "我？我会对露西做那种事吗，宝贝？" 
    scene img_main18_170 with dissolve
    pause
    scene img_main18_171 with dissolve
    "{i}*顶了顶{/i}"
    scene img_main18_172 with dissolve
    Lucy "唔嗯……不、不！他不……啊唔嗯……他从来……啊……"
    scene img_main18_173 with dissolve
    Rachel "看！连替你辩解她都做不到！"
    scene img_main18_174 with dissolve
    "这句指控让露西的某根弦绷断，她提高了声音。"
    Lucy "不！……闭、闭嘴，别再缠着他！"
    scene img_main18_175 with dissolve
    Rachel "我……"
    scene img_main18_176 with dissolve
    Lucy "{b}滚出去！！{/b}"
    scene img_main18_177 with dissolve
    MC "你听见她说的了。想告状就去找女校长，我们俩都不在乎你要说什么。"
    scene img_main18_178 with dissolve
    pause
    scene img_main18_179 with dissolve
    "瑞秋哼了一声，脸上带着雷霆般的怒容走了。"
    scene img_main18_180 with dissolve
    Lucy "啊……我的天……"
    scene img_main18_181 with dissolve
    "压力从露西身上流走，她的肩膀垮了下来，长长地吐出一口憋了很久的气。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main18_182 with dissolve
    "当然，她在你鸡巴上挪动的感觉让你把她的裙子重新拉上来，开始更认真地操她。"
    scene img_main18_183 with dissolve
    pause
    scene img_main18_184 with dissolve
    Lucy "啊唔唔……"
    scene img_main18_185 with dissolve
    Lucy "我、我们……要、要继续下去？！"
    scene img_main18_186 with dissolve
    MC "对，看着你被我钉在鸡巴上还敢跟她顶回去，挺刺激的。在我射进你体内深处之前，我们不会停。"
    Lucy "啊唔嗯……"
    scene vid_main18_4 with dissolve
    "露西又花了点时间才从瑞秋闯入的震惊中恢复过来，然后重新开始在你的鸡巴上缓缓起伏。"
    scene img_main18_187 with dissolve
    "与此同时……"
    scene img_main18_188 with dissolve
    Rachel "{i}*喃喃自语*{/i}我就知道……他、他……在强暴她！现、现在就在学校里！"
    scene img_main18_189 with dissolve
    Rachel "想想被这么邪恶的男人强暴……多、多可怕啊……"
    scene vid_main18_5 with dissolve
    MC "操，你感觉真爽，露西。"
    Lucy "啊唔嗯……唔嗯……"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main18_190 with dissolve
    "你像之前一样伸手上去，释放出她的双乳。"
    scene img_main18_191 with dissolve
    MC "靠，你的乳头好硬。"
    Lucy "唔嗯……"
    scene img_main18_192 with dissolve
    MC "继续。"
    Lucy "好、好的！"
    scene vid_main18_6 with dissolve
    pause
    "她热情地重新在你腿上起伏，湿淋淋的小穴里的肌肉竭尽所能地按摩着你的鸡巴，进进出出。"
    Lucy "唔嗯嗯……我、我……啊唔嗯……"
    scene vid_main18_7 with dissolve
    Lucy "啊、我真的……做得还行吗……？"
    MC "唔嗯……你做得很好，露西，我保证。"
    scene vid_main18_8 with dissolve
    "听到这话似乎真的鼓舞了她，她快了一些，但对你来说还不够。"
    scene vid_main18_9 with dissolve
    Lucy "哦——哦唔我的天……唔嗯嗯……"
    "你收紧握在她胯上的手，开始更快更狠地把她上下抬起，每把她拉下来一次，就同时朝她小穴最深处挺送一次。"
    scene vid_main18_10 with dissolve
    pause
    "每次到底插进她体内，你都能感觉到她脉动的内壁在你柱身上收缩，逼出她不由自主的抽气与呻吟。"
    scene vid_main18_11 with dissolve
    "你们彼此的兴奋互相感染，速度进一步加快，快到你分不清到底是你在推动她，还是她在推动你。"
    Lucy "啊唔嗯！……唔嗯……啊……"
    MC "操……你太厉害了……"
    scene vid_main18_12 with dissolve
    Lucy "我、唔唔嗯嗯嗯……！拜、拜托，[PlayerName]，我想要……"
    MC "唔嗯，告诉我你想要什么，露西。"
    scene vid_main18_13 with dissolve
    Lucy "里、里面……我、我想让你射进我体内……"
    "她的请求时机刚刚好……"
    "强烈的快感开始传遍你全身，你的鸡巴在她体内不受控制地跳动起来，一场爆发式的高潮已不可避免。"
    "强烈的感觉把你的脑海烧成一片空白，最后一次挺送中你猛地把她拉下，把整根鸡巴埋进她体内深处。"
    scene vid_main18_15 with flash
    Lucy "唔唔嗯嗯，好、好的！"
    "你在她体内深处爆发时，她敏感的内壁在你柱身上抽搐，一股股精液灌满了她脉动的体内。"
    scene vid_main18_16 with dissolve
    Lucy "唔唔嗯嗯……那、那真是……谢谢你……"


    "你花了一会儿才把呼吸控制到能回话的程度。"
    "..."
    scene img_main18_193 with dissolve
    MC "呵……哈啊……你每次我射进你体内都要道谢吗？"
    scene img_main18_194 with dissolve
    Lucy "对……永远都是。"
    MC "靠，你太完美了。"
    scene img_main18_195 with dissolve
    Lucy "啊……不、不……"
    MC "嘘。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main18_196 with dissolve
    "你靠回沙发上，让露西从你的鸡巴上滑下来，开始整理自己的衣服。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main18_197 with dissolve
    "她整理完后靠过来亲密地抱住你，正好这时门又被推开了……"

    $ renpy.end_replay()


#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_victoria4:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/victoria_theme.mp3" loop volume 1.0 fadeout 1.0 fadein 1.0

    scene img_main19_229 with dissolve
    "听到那一个词，她就把你拉进那间到现在还没用过的卧室，你们在那里脱掉了最后的衣物。"
    scene img_main19_230 with dissolve
    pause
    scene img_main19_231 with dissolve
    pause
    scene img_main19_232 with dissolve
    "等两个人都彻底赤裸，薇琪向后一靠，抬头看着你，公然挑衅你出手。"

    play sound "audio/sounds/bed.mp3" volume 4.0

    scene img_main19_233 with dissolve
    "你当然不会等人吩咐，直接把她按倒在床上。"
    scene img_main19_234 with dissolve
    Victoria "哦，主人……你要对我做什么？"
    scene img_main19_235 with dissolve
    Victoria "唔嗯……求你了……唔嗯……"
    scene img_main19_236 with dissolve
    Victoria "主人……"
    scene img_main19_237 with dissolve
    pause
    scene img_main19_236 with dissolve
    Victoria "我……唔嗯……想要你……"
    scene img_main19_238 with dissolve
    "每当她试图说出一句完整的话，你就把舌头伸进她嘴里，让她一句也说不完。"
    scene img_main19_239 with dissolve
    "最后她试着把一只手从你的手里抽出来，你却收得更紧，她在你嘴里发出一声呻吟。"
    Victoria "唔嗯……"
    scene img_main19_241 with dissolve
    "最后你退开，俯视着她微笑——她正被彻底压在身下动弹不得。"
    MC "真想知道你打算用那只手做什么呢？"
    scene img_main19_242 with dissolve
    Victoria "松手我就告诉你。"
    scene img_main19_243 with dissolve
    "她没有松手，你反而把她更用力地压进床里，这似乎让她更加兴奋。"
    scene img_main19_244 with dissolve
    "过了一会儿，你松开了一只手……"
    scene img_main19_245 with dissolve
    pause
    scene img_main19_246 with dissolve
    pause
    scene img_main19_247 with dissolve
    "她立刻把那只手滑下去，握住你硬得像石头一样的鸡巴，扯动了几下。"
    scene img_main19_248 with dissolve
    "她开始正经地为你手淫，与此同时你把手顺着她的小腹滑下，用手指抚过她的阴蒂。"
    scene img_main19_249 with dissolve
    Victoria "唔嗯……"
    scene img_main19_250 with dissolve
    "挑逗了一会儿后，你看得出她急切地想要更多，于是把一根手指滑进她温暖湿透的小穴，引出一声小小的快感抽气。"
    scene img_main19_251 with dissolve
    "与此同时她的手一直上下滑动，挤压着、顺着你鸡巴的轮廓，让她的触碰不断激起一阵阵快感。"
    scene img_main19_252 with dissolve
    Victoria "唔嗯……还要更多……我不只要你的手指……"
    scene img_main19_253 with dissolve
    "你不理会她，把第二根手指滑进她处女的小穴，又从她嘴里引出一声小小的抽气。"
    scene img_main19_254 with dissolve
    Victoria "啊唔嗯嗯……"
    scene img_main19_255 with dissolve
    Victoria "别再撩我了！"
    scene img_main19_256 with dissolve
    Victoria "唔唔嗯！"
    scene img_main19_257 with dissolve
    "你又一次无视她，继续揉弄、插入，直到她放弃为你手淫，整个人融化在床铺里。"
    scene img_main19_258 with dissolve
    Victoria "唔嗯……你真是个坏蛋……"
    scene img_main19_259 with dissolve
    "最后，在你确定她已经完全准备好时，你坐起身推开她的双腿，露出她湿淋淋的小穴。"
    scene img_main19_260 with dissolve
    MC "这可能会疼，薇琪。"
    scene img_main19_261 with dissolve
    Victoria "唔哼……我能忍住。"
    scene img_main19_262 with dissolve
    "你又试着多撩了她一会儿……"
    scene img_main19_263 with dissolve
    "但她不愿再等，主动把胯抬起来，逼着前端进入。"
    scene img_main19_264 with dissolve
    Victoria "啊啊啊……"
    MC "你这么着急。好吧，我给你想要的。"
    scene img_main19_265 with dissolve
    "她只是把膝盖抬得更高，好让你进入得更方便。"
    scene img_main19_266 with dissolve
    "你小心地提醒自己她没有经验，缓缓把鸡巴引进她紧致的小洞。"
    scene img_main19_267 with dissolve
    "你第一次逐渐进入她的身体，尽情享受着她小穴在你鸡巴被撑开时紧紧夹住的感觉。"
    Victoria "啊唔唔……"
    scene img_main19_268 with dissolve
    "你抬眼看，薇琪看起来确实相当痛苦。"
    MC "靠，薇琪。你真的紧得要命。"
    scene img_main19_269 with dissolve
    "她痛苦的表情一瞬间被挑衅的笑容取代，虽然声音仍然绷着。"
    Victoria "看吧，我说过我不是骚货。"
    MC "我从没怀疑过你。"
    scene img_main19_270 with dissolve
    "你继续推进，害得她把眼睛紧紧闭上。"
    scene img_main19_271 with dissolve
    MC "没事吧？"
    scene img_main19_272 with dissolve
    Victoria "唔唔嗯……没、没事……"
    "你为自己这个嘴硬又倔强的女友的坚持感到好笑，尽管你也在后悔让她承受了这么多痛苦。"
    scene img_main19_273 with dissolve
    Victoria "啊啊啊……操……"
    scene img_main19_274 with dissolve
    "当你把鸡巴最后那一寸推进她那惊人的小穴时，她忍不住用咒骂来发泄疼痛。"
    scene img_main19_273 with dissolve
    MC "乖女孩。"
    scene img_main19_275 with dissolve
    "她终于稍稍睁开眼，疼痛在表情的控制上胜过了兴奋。"
    MC "比想象中更疼吗？"
    Victoria "唔哼……"
    scene img_main19_276 with dissolve
    Victoria "我、我们能……呃……就这样先待一会儿吗？"
    MC "当然。"
    scene img_main19_277 with dissolve
    "..."
    scene img_main19_278 with dissolve
    "你伸手下去揉捏她的一只乳房，让她露出一点笑容。"
    Victoria "你太大了。"
    MC "幸好你有受虐的倾向。"
    scene img_main19_279 with dissolve
    "她发出一声带着痛感的、气息般的笑。"
    scene img_main19_280 with dissolve
    Victoria "唔嗯……看来我们天生一对。"
    scene img_main19_281 with dissolve
    "你俯身想吻她，但这突然的动作让她痛得皱缩起来。"
    MC "靠，抱歉……你没事吧？"
    scene img_main19_282 with dissolve
    "她缓过那阵惊吓，轻轻咯咯笑起来。"
    scene img_main19_283 with dissolve
    Victoria "你刚才看起来好害怕。我从没见过你那样。"
    MC "我不想伤到你……伤得太重。"
    scene img_main19_284 with dissolve
    Victoria "唔嗯……要试试动起来吗？"
    scene vid_main19_1 with dissolve
    "不用你说第二遍，你就温柔地退出一点，然后再滑进她体内。"
    scene vid_main19_2 with dissolve
    "很显然她还相当疼，但她也露出了一点笑容。"
    MC "乖女孩。"
    Victoria "哈啊……唔哼……"
    "你保持这个痛苦而缓慢的节奏好一会儿，让她慢慢习惯。"
    scene vid_main19_3 with dissolve
    pause
    "薇琪或许正在受苦，你却只从她紧致湿透的小穴为了容纳你进出的鸡巴而撑开的质感中感到强烈的快感。"
    scene vid_main19_1 with dissolve
    MC "你感觉他妈的好极了，薇琪。"
    Victoria "唔嗯……"
    scene img_main19_285 with dissolve
    pause
    scene img_main19_286 with dissolve
    "你停下来，俯身看进她的眼睛。"
    MC "那么，你之前那股一被我插进来就会高潮的自信呢？"
    scene img_main19_287 with dissolve
    "她笑了一下，随即又痛得皱起脸。"
    Victoria "哈，操……"
    scene img_main19_288 with dissolve
    Victoria "现在别逗我笑。"
    MC "你每感到一次疼，就更属于我一点。明白了吗？"
    scene img_main19_289 with dissolve
    Victoria "唔嗯，看来我只能学着喜欢这种疼了。"
    scene img_main19_290 with dissolve
    MC "这才是我的女孩。"
    scene img_main19_291 with dissolve
    pause
    scene vid_main19_4 with dissolve
    "你立刻重新开始，稍微加快、加深。"
    Victoria "啊啊啊唔嗯……操……"
    scene vid_main19_5 with dissolve
    Victoria "哈啊……我真的完全是你的……彻底——啊……现在……"
    MC "对，你完全是。而我要射进你紧致的小穴里，把这事敲定。"
    scene vid_main19_6 with dissolve
    Victoria "唔哼……我想要……"
    MC "觉得自己能再快一点吗？"
    "她看起来很紧张，仍在和疼痛抗争，但还是点了点头。"
    MC "你确定？"
    Victoria "唔哼……别管我……就……啊唔嗯……操我吧……"
    scene vid_main19_7 with dissolve
    "你稍稍加快，把注意力集中在鸡巴在她体内进出的美妙感觉上。"
    scene vid_main19_8 with dissolve
    "你看着她那对惊人巨乳轻轻起伏……"
    scene vid_main19_9 with dissolve
    "然后抬头看向她痛苦却坚定的脸。"
    "她挤出一个微笑，示意你射在她体内。"
    Victoria "拜、拜托，[PlayerName]，你可以射进我体内……我需要……"
    "你感觉到压力开始累积……"
    "想到要射进她处女的身体深处，那股冲动压倒了一切……"
    scene vid_main19_10 with dissolve
    "你失去了自我，动作稍微重了些，但没有停下。"
    Victoria "啊啊啊唔嗯！！……"
    scene vid_main19_11 with flash
    Victoria "唔唔唔唔唔唔嗯嗯！！！"
    "当你顶到最深处并开始一股股把精液射进她颤抖的身体时，她发出一声混杂着疼痛、快感与兴奋的叫声。"
    scene img_main19_292 with dissolve
    "..."
    scene img_main19_293 with dissolve
    "你花了长长的几秒才从这震撼的感觉中缓过来，薇琪轻轻抚着你的手才终于把你带了回来。"
    scene img_main19_294 with dissolve
    "你缓缓把鸡巴抽出来，又引出一声小小的抽气，一小股混着血液的精液从她体内流出。"

    $ renpy.end_replay()


#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_group1:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/sexy.mp3" loop fadeout 1.0 fadein 1.0

    scene img_main20_544 with dissolve
    "你走进餐厅抓了把最近的椅子，回来放在薇琪正前方偏侧的位置，她一脸困惑地看着你。"
    scene img_main20_545 with dissolve
    MC "过来，露西。"
    scene img_main20_546 with dissolve
    "她走过来站在你身边，满脸好奇。"
    MC "你觉得自己该如何让薇琪见识一下，你给我口交的技术到底有多好？"
    scene img_main20_547 with dissolve
    "她看起来有点紧张，并瞥了一眼正在旁观的薇琪。"
    "你压低声音，低到薇琪听不见的程度。"
    scene img_main20_548 with dissolve
    MC "{i}*低语{/i}记住，露西，你永远不需要为了我去做任何你不舒服的事。"
    scene img_main20_549 with dissolve
    "她只是笑了笑点点头，然后跪了下来。"
    Lucy "我想……"
    scene img_main20_550 with dissolve
    pause
    scene img_main20_551 with dissolve
    pause
    scene img_main20_552 with dissolve
    pause
    scene img_main20_553 with dissolve
    Lucy "哦唔嗯……"
    scene img_main20_554 with dissolve
    Lucy "唔哼……"
    "没过多久，她就掏出你的鸡巴，用双唇裹了上去。"
    MC "操，你技术真好。"
    scene img_main20_555 with dissolve
    Lucy "唔唔嗯嗯……"
    scene img_main20_556 with dissolve
    MC "你已经习惯在别的女孩面前做了吗？"
    "她害羞地轻轻摇了摇头，但没有停止吸吮。"
    scene img_main20_557 with dissolve
    "你抬头看向薇琪，发现她正撅着嘴，嫉妒地看着。"
    scene img_main20_558 with dissolve
    Victoria "你好过分，主人！"
    MC "你说过你就是爱逗我，对吧？可我也爱逗你啊，薇琪。"
    scene img_main20_559 with dissolve
    "你把手放在露西轻轻起伏的头上，向后靠去，享受深爱你的女友用温暖湿润的嘴上下侍弄你涨硬鸡巴的感觉。"
    scene img_main20_560 with dissolve
    pause
    scene img_main20_561 with dissolve
    Lucy "唔唔嗯……唔嗯……"
    scene img_main20_562 with dissolve
    pause
    scene img_main20_563 with dissolve
    "这样在沉默中持续了几分钟，谁都没有说话，直到你感觉到露西的服务正逐渐把你推向临界点。"
    scene img_main20_564 with dissolve
    MC "你做得很好，这感觉太爽了。"
    scene img_main20_565 with dissolve
    Lucy "唔嗯嗯。"
    scene img_main20_566 with dissolve
    Victoria "主人……这不公平！"
    scene img_main20_567 with dissolve
    MC "你觉得呢，露西？愿意让她一起吗？"
    scene img_main20_568 with dissolve
    "露西大概早就料到了，她抬头朝你露出一个狡黠的笑，摇了摇头。"
    scene img_main20_567 with dissolve
    Lucy "哦唔嗯嗯……"
    scene img_main20_564 with dissolve
    pause
    scene img_main20_566 with dissolve
    MC "真遗憾，薇琪，她不愿意分享。"
    scene img_main20_569 with dissolve
    Victoria "不——你们两个太坏了！"
    MC "没错。"
    scene img_main20_570 with dissolve
    pause
    scene img_main20_571 with dissolve
    pause
    scene img_main20_570 with dissolve
    pause
    scene img_main20_571 with dissolve
    pause
    scene img_main20_570 with dissolve
    pause
    scene img_main20_571 with dissolve
    pause
    scene img_main20_572 with dissolve
    "又吸了一会儿，露西终于从她开始以来第一次退开坐下。"
    scene img_main20_573 with dissolve
    Lucy "呃……我、我不介意分享……"
    scene img_main20_574 with dissolve
    Victoria "谢谢你，露西！……主人？"
    MC "好吧，过来跪下。"
    scene img_main20_575 with dissolve
    "薇琪迫不及待地离开台面，跪到露西旁边，然后跪坐着等你的下一道命令。"
    scene img_main20_576 with dissolve
    MC "那就来吧，我让你把我弄到射出来。"
    scene img_main20_577 with dissolve
    "她一句话都没说，立刻接替了露西刚才的位置。"
    scene img_main20_578 with dissolve
    Victoria "唔嗯……唔嗯呜……唔……主……"
    MC "乖女孩。"
    scene img_main20_579 with dissolve
    "这一切发生的时候，露西在旁看着，在羞耻与着迷之间摇摆不定。"
    scene img_main20_580 with dissolve
    pause
    scene img_main20_581 with dissolve
    "她的视线和你相遇了一瞬，又害羞地移开，但没过多久她就又把目光投回薇琪身上。"
    scene img_main20_582 with dissolve
    pause
    scene img_main20_583 with dissolve
    pause
    scene img_main20_584 with dissolve
    "薇琪似乎一点也不在意观众，继续吸吮着，嘴唇和舌头的运用比露西更放荡一些。"
    scene img_main20_585 with dissolve
    MC "操，你想表现的时候真够淫荡的。"
    scene img_main20_586 with dissolve
    Victoria "唔哼……"
    MC "露西在这方面很厉害，但我觉得你可能一样厉害。"
    scene img_main20_587 with dissolve
    "这句夸奖似乎比什么都更让她高兴，你能感觉到她含着你的鸡巴在笑。"
    scene img_main20_591 with dissolve
    "之后没过多久，薇琪丝滑湿润的嘴就把你推过了临界点。"
    scene img_main20_592 with dissolve
    MC "操……乖乖的，把每一滴都给我咽下去。"
    scene img_main20_593 with dissolve
    Victoria "唔哼。"
    scene img_main20_594 with vpunch
    pause 0.5
    scene img_main20_594 with vpunch
    pause 0.35
    scene img_main20_594 with vpunch
    pause 0.2
    scene img_main20_595 with vpunch
    pause 0.1
    scene img_main20_595 with vpunch
    pause 0.1
    scene img_main20_595 with flash
    Victoria "唔唔嗯嗯嗯嗯！"
    "..."
    scene img_main20_596 with dissolve
    Victoria "唔嗯……"


    #insert cum in Victoria's mouth scene here.

    MC "操……你们两个最棒了。"
    scene img_main20_597 with dissolve
    Victoria "唔嗯嗯……"
    scene img_main20_598 with dissolve
    Lucy "嘿嘿……"

    $ renpy.end_replay()


#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_lucy6:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/lucy_theme.mp3" loop volume 1.2 fadeout 1.0 fadein 1.0

    scene img_main21_27 with dissolve
    MC "你知道，我在这儿最喜欢罚人，但我觉得乖女孩也该得到奖励。"
    scene img_main21_28 with dissolve
    Lucy "啊，嗯嗯……"
    scene img_main21_29 with dissolve
    "你把椅子往后挪了挪，给她留出一点站起来的空间。"
    scene img_main21_30 with dissolve
    MC "把衣服脱掉。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main21_31 with dissolve
    "她脸上挂着害羞的笑容，站起来开始脱衣服。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main21_32 with dissolve
    pause
    scene img_main21_33 with dissolve
    "等她脱完，你又把她拉下来坐在你的腿上。"
    scene img_main21_34 with dissolve
    pause
    scene img_main21_35 with dissolve
    MC "哈。我们一起做过这么多事了，你还会害羞？"
    scene img_main21_36 with dissolve
    pause
    scene img_main21_37 with dissolve
    "她意识到自己刚才在做什么，于是露出狡黠的笑容，然后把手臂抽出来环上你的肩膀，整个过程中把胸部完全露了出来。"
    scene img_main21_38 with dissolve
    MC "现在……"
    scene img_main21_39 with dissolve
    pause
    scene img_main21_40 with dissolve
    "你左手沿着她身体光滑的曲线向上滑动，挤捏她一只沉甸甸的乳房，同时右手顺着她的大腿往上摸。"
    scene img_main21_41 with dissolve
    "玩闹般摸了一会儿之后，你把她拉进另一个长吻。"
    scene img_main21_42 with dissolve
    Lucy "唔嗯……"
    scene img_main21_43 with dissolve
    "你没有中断这个吻，手沿着她大腿内侧柔软的肌肤缓缓上移，最后擦过她小穴的边缘。"
    scene img_main21_44 with dissolve
    Lucy "唔嗯……"
    scene img_main21_45 with dissolve
    "起初很轻，你开始用指尖揉弄那片敏感的区域。"
    scene img_main21_44 with dissolve
    "你缓慢而刻意地拉长这个过程，你能通过共同的吻感觉到她的兴奋在上升。"
    scene img_main21_45 with dissolve
    "最后，你把指尖滑过她阴蒂的小凸起，一股电流般的快感瞬间贯穿她的全身。"
    scene img_main21_46 with dissolve
    Lucy "唔唔嗯！"
    scene img_main21_47 with dissolve
    MC "你今天乖乖的吗？"
    Lucy "啊，唔嗯……"
    MC "你确定？"
    scene img_main21_48 with dissolve
    Lucy "唔嗯……我、我永远都会是你的乖女孩。"
    scene img_main21_49 with dissolve
    "作为回应，你把她的腿抬过你的腿。"
    scene img_main21_50 with dissolve
    Lucy "啊唔嗯……"
    scene img_main21_51 with dissolve
    Lucy "唔嗯嗯……"
    MC "你真是我的乖女孩，露西，所以现在我要让你为我高潮。听起来不错吧？"
    scene img_main21_52 with dissolve
    Lucy "是、是的……唔嗯……我想要……"
    scene img_main21_53 with dissolve
    MC "你想要什么？告诉我。"
    scene img_main21_54 with dissolve
    Lucy "我……唔嗯嗯……"
    scene img_main21_55 with dissolve
    "露西试图说话，但你的手指一直推进到指节，让她的句子死在嘴边。"
    scene img_main21_56 with dissolve
    Lucy "拜、拜托，[PlayerName]……我想为你高潮。"
    MC "乖女孩。"
    scene img_main21_55 with dissolve
    Lucy "唔嗯……我是你的乖女孩……"
    scene img_main21_57 with dissolve
    "你把第二根手指推进她温暖湿润的小穴，她的身体又是一阵战栗，你开始缓慢地勾动着它们进出。"
    scene img_main21_58 with dissolve
    Lucy "啊唔嗯嗯嗯……"
    scene img_main21_57 with dissolve
    "你们俩有很长一段时间都没说话，露西沉浸在欢愉的节奏里，你则愉快地观察着她的每一个反应，一点点把她推向临界点。"
    scene img_main21_58 with dissolve
    pause
    scene img_main21_57 with dissolve
    pause
    scene img_main21_58 with dissolve
    pause
    scene img_main21_57 with dissolve
    pause
    scene img_main21_58 with dissolve
    pause
    scene img_main21_59 with dissolve
    Lucy "唔唔嗯嗯……"
    "她柔软压抑的呻吟，以及无法与你对视，都说明残存的羞耻感还在；但你看得出她正越来越习惯这一切。"
    scene img_main21_60 with dissolve
    "她像是被突如其来的冲动淹没，主动凑进另一个深吻，与此同时你继续把手指在她的小穴里进进出出。"
    scene img_main21_61 with dissolve
    Lucy "唔嗯……"
    scene img_main21_62 with dissolve
    Lucy "唔唔嗯嗯唔嗯！！"
    scene img_main21_63 with dissolve
    "趁她分心时，你突然加快速度，突如其来的感觉让她在你嘴里呻吟起来。"
    scene img_main21_64 with dissolve
    Lucy "啊唔嗯……我、我……"
    scene img_main21_65 with dissolve
    Lucy "[PlayerName]!"
    scene img_main21_66 with dissolve
    pause
    Lucy "哦天啊……"
    scene img_main21_67 with dissolve
    "你进一步加大力度，每一次抽动都从她湿透的小穴里带出细小的水声。"
    scene img_main21_68 with dissolve
    Lucy "啊啊啊唔嗯！！唔嗯唔嗯……！"
    scene img_main21_67 with dissolve
    "你保持这个激烈的节奏又持续了一会儿，直到你开始感觉到她的身体绷紧，朝释放累积。"
    scene img_main21_68 with dissolve
    pause
    scene img_main21_67 with dissolve
    pause
    scene img_main21_68 with dissolve
    pause
    scene img_main21_67 with dissolve
    pause
    scene img_main21_69 with dissolve
    Lucy "哦——唔嗯嗯嗯……我、我的啊啊啊唔嗯嗯嗯"
    scene img_main21_70 with dissolve
    "当感觉变得压倒性时，她把眼睛紧紧闭上。"
    scene img_main21_71 with dissolve
    MC "{i}*低语{/i}为我高潮吧，露西。"
    Lucy "唔嗯唔嗯……是、是的唔嗯嗯！"
    scene img_main21_72 with dissolve
    pause
    scene img_main21_73 with dissolve
    pause
    scene img_main21_74 with dissolve
    pause
    scene img_main21_73 with dissolve
    pause
    scene img_main21_74 with dissolve
    "你用力抓住她的乳房，把她拉进怀里，在她体内又狠狠顶了几下手指，然后猛烈的高潮便击中了她。"
    scene img_main21_75 with dissolve
    Lucy "啊啊啊唔嗯……啊啊啊唔嗯嗯唔……唔啊啊啊唔！！"
    "她的背弓起，小穴随着每一波冲刷过她的快感在你手指上痉挛。"
    scene img_main21_76 with dissolve
    Lucy "啊唔唔唔唔唔唔嗯嗯嗯……"
    scene img_main21_77 with dissolve
    Lucy "哦啊啊——我的天啊啊啊……是的是的！！！"
    "..."

    scene img_main21_78 with dissolve
    "你紧紧抱住她，看着她逐渐放松、从这激烈的体验中缓过来，呼吸急促，眼睛仍闭着。"
    Lucy "哈啊啊啊……"
    "最后，她长长地、颤抖地吐出一口气，释放出最后几缕残留的极乐。"
    MC "乖女孩。"
    Lucy "唔嗯……"
    "..."
    "......"
    scene img_main21_79 with dissolve
    "最后她从你腿上滑落到地板，眼睛死死盯着你硬得像石头的鸡巴，它正抵着牛仔裤的缝隙鼓起。"
    scene img_main21_80 with dissolve
    Lucy "呃，轮到我了……"
    MC "我还要去赴莎拉的约，已经要迟到了……"
    scene img_main21_81 with dissolve
    "露西明白你的意思，看起来非常难过。"
    Lucy "可、可是……这不公平，你会憋得很难受的！"
    MC "哈，我觉得我能撑住。"
    scene img_main21_82 with dissolve
    Lucy "而、而且……我喜欢让你舒服。"
    MC "操，你这个小妖精真是不让人省心……"
    MC "但我真的得走了。"
    scene img_main21_83 with dissolve
    "露西虽然失望，却还是笑着站起来，在你脸颊上亲了一下。"
    scene img_main21_84 with dissolve
    Lucy "好吧。"

    $ renpy.end_replay()


#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_taka1:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/taka_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0

    scene img_main21_388 with dissolve
    "到了站台上，她按指示朝出口走，你在洗手间旁边叫住了她。"
    scene img_main21_389 with dissolve
    "你们面前的那列火车驶出车站，等最后几个人也离开后，你低声开口。"
    scene img_main21_390 with dissolve
    MC "就站在这里别回头，我去看看情况。"
    Taka "好、好的……"
    scene img_main21_391 with dissolve
    pause

    play sound "audio/sounds/door.mp3"

    scene img_main21_392 with dissolve
    pause
    scene img_main21_393 with dissolve
    pause
    scene img_main21_394 with dissolve
    "你闪身进去，发现洗手间空无一人。"

    play sound "audio/sounds/door.mp3"

    scene img_main21_395 with dissolve
    MC "好了，最后一次改变主意的机会。"
    scene img_main21_396 with dissolve
    Taka "不、不……"
    scene img_main21_397 with dissolve
    pause
    scene img_main21_398 with dissolve
    "你环顾四周确认自己仍是独自一人——考虑到这座小站有多安静，这很容易做到……"


    scene img_main21_399 with dissolve
    pause

    play sound "audio/sounds/door.mp3"

    scene img_main21_400 with dissolve
    
    "然后你把手放在她的胯上，迅速把她推进男厕所。"
    
    play sound "audio/sounds/door_close.mp3" volume 2.0
    
    scene img_main21_401 with dissolve
    pause

    play sound "audio/sounds/door_lock.mp3" volume 2.0

    scene img_main21_402 with dissolve
    "在狭窄的小隔间里，你转身锁上门。"
    scene img_main21_403 with dissolve
    "你再次碰她时，她轻轻一颤。"
    MC "紧张了？"
    Taka "唔嗯，有一点……"
    MC "别担心，今天不会太过分。"
    MC "现在闭上眼睛。"
    scene img_main21_404 with dissolve
    Taka "好……"
    MC "不对。要说『是，老师』，记得吗？"
    scene img_main21_405 with dissolve
    Taka "是、是的，老师……"
    MC "乖女孩。现在……"
    scene img_main21_406 with dissolve
    "你把她转过来面对你，松了口气——她的眼睛确实闭着"
    scene img_main21_407 with dissolve
    "你轻轻把她抵在墙上。"
    scene img_main21_408 with dissolve
    MCi "（从正面看着她，突然之间，和自己的老师做这种事变得真实多了。）"
    MC "现在只剩我们两个，没有人会听见，也不用像在火车上那样克制……"
    scene img_main21_409 with dissolve
    Taka "啊……唔嗯……"
    scene img_main21_410 with dissolve
    "从她宽阔的胯部开始，你把双手向上滑动……"
    scene img_main21_411 with dissolve
    "你顺着她的身形曲线滑向紧致腰身的凹陷……"
    scene img_main21_412 with dissolve
    "然后再向外滑出，那是她胸部的隆起，勾勒出完整的沙漏曲线。"
    scene img_main21_413 with dissolve
    MC "靠，你性感得要命，姑娘。"
    scene img_main21_414 with dissolve
    Taka "唔嗯……从、从来没人这样对我说过……"
    MC "你的笑容也很好看。"
    scene img_main21_415 with dissolve
    Taka "啊……"
    MC "不过现在可不是害羞的时候。"
    scene img_main21_416 with dissolve
    "你把手移到她胸口中央，开始解开她的丝带。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main21_417 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main21_418 with dissolve
    pause
    scene img_main21_419 with dissolve
    "等她的扣子全部解开，你向下挪动，再次把她的裙子推上去，露出你在她连裤袜上撕出的洞的另一侧。"
    scene img_main21_420 with dissolve
    MC "你说过你从来没有过高潮，对吧？"
    scene img_main21_421 with dissolve
    Taka "是、是的……"
    "你听出她回答时声音里带着紧张的颤音。"
    MC "好，那我这就给你一个。"
    scene img_main21_422 with dissolve
    Taka "好、好的……"
    MC "不，这可不行，姑娘。"
    MC "我得先知道你想要。"
    scene img_main21_423 with dissolve
    Taka "你、你可以，呃，做……"
    MC "哈，我不是在征求同意。我是在问你有多想高潮。"
    scene img_main21_424 with dissolve
    Taka "我、我想……"
    MC "你想要被一个陌生男人带进洗手间，然后被弄到高潮？"
    scene img_main21_423 with dissolve
    Taka "是、是的……"
    MC "你说得一点也不让人信服。你听起来就像个害羞的小姑娘。"
    scene img_main21_425 with dissolve
    Taka "我、我……我真的想要！求你了，老师……"
    scene img_main21_426 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 2.0

    scene img_main21_427 with dissolve
    "你把她的内裤拨到一边……"
    scene img_main21_428 with dissolve
    Taka "等、等一下……呃……我能先摸摸你吗？"
    MC "当然，请便。"
    scene img_main21_429 with dissolve
    pause
    scene img_main21_430 with dissolve
    "她眼睛仍然闭着，伸出手摸了摸你的手臂。"
    scene img_main21_431 with dissolve
    "她的手开始在你身上游走，抚过你的胸膛，向上摸到你的肩膀。"
    scene img_main21_432 with dissolve
    Taka "你、你很大……"
    MC "是的，比你大得多。"
    scene img_main21_433 with dissolve
    MC "现在开始害怕了？"
    scene img_main21_434 with dissolve
    "她摇了摇头。"
    Taka "我、我……我的心跳得好快……但我不怕你。"
    MC "很好，因为接下来，在你高潮之前我都不会停。"
    scene img_main21_435 with dissolve
    pause
    "她的手还在你肩上，你稍微靠近一点，把自己的手伸进她的双腿之间。"
    Taka "啊……"
    scene img_main21_436 with dissolve
    "你的手指擦过她的阴蒂时，她轻轻绷紧了身体。"
    Taka "哦——哦天啊……"
    scene img_main21_437 with dissolve
    "她的呼吸卡在喉咙里，这反而诱使你更进一步，渴望看到她的更多反应。"
    scene img_main21_438 with dissolve
    pause
    "你的手指滑过她小丘上湿透的入口时，她浑身一阵战栗，甚至不由自主地小声呻吟了一下。"
    scene img_main21_439 with dissolve
    Taka "啊唔嗯……"
    scene img_main21_440 with dissolve
    MC "把内衣拉上来，我要看那对惊人的巨乳。"
    scene img_main21_441 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main21_442 with dissolve
    "她起初有些犹豫，但还是照做了。"
    scene img_main21_443 with dissolve
    "就在她照做的瞬间，你把一根手指滑进她体内，打了她一个措手不及。"
    Taka "唔唔嗯嗯……"
    scene img_main21_444 with dissolve
    MC "乖女孩。"
    #in and out repeated a few times
    scene img_main21_445 with dissolve
    "你一边把手指在她急切而毫无经验的小穴里进出，一边开始说话。"
    scene img_main21_446 with dissolve
    MC "那么，这就是你在幻想里做的事吗？"
    scene img_main21_445 with dissolve
    Taka "不、不是……"
    scene img_main21_446 with dissolve
    MC "告诉我。"
    scene img_main21_445 with dissolve
    Taka "你、你……唔嗯……呃……在我身后……"
    scene img_main21_446 with dissolve
    Taka "啊啊啊……"
    scene img_main21_445 with dissolve
    Taka "还、还有……"
    scene img_main21_447 with dissolve
    MC "还有什么？"
    scene img_main21_448 with dissolve
    Taka "唔嗯……把、把我按在墙上……"
    MC "好。"
    scene img_main21_449 with dissolve
    Taka "啊……"
    scene img_main21_450 with dissolve
    "你再一次把手放在她两侧，用力把她转了过来。"
    Taka "哦、哦……"
    scene img_main21_451 with dissolve
    "你把她按在墙上时，她的声音里既紧张又兴奋。"
    scene img_main21_452 with dissolve
    MC "像这样吗？"
    scene img_main21_453 with dissolve
    Taka "唔嗯……"
    MC "把背弓一点，把屁股撅起来。"
    scene img_main21_454 with dissolve
    MC "完美。乖女孩。"
    scene img_main21_455 with dissolve
    "你退后一步，把她的连裤袜和内裤拉到大腿处。"
    scene img_main21_456 with dissolve
    pause

    scene vid_main21_1 with dissolve
    "终于再无阻碍，你侧身一步，把手指滑进她体内。"
    Taka "唔嗯……"
    scene vid_main21_2 with dissolve
    MC "那么我当时做了什么？"
    Taka "啊唔嗯……你、你……"
    scene vid_main21_3 with dissolve
    Taka "你解开了裤子的拉链唔嗯……还、还有……"
    MC "我操了你？"
    Taka "是、是的……啊啊唔嗯！"
    scene vid_main21_4 with dissolve
    "她回答的同时，你把第二根手指滑进她体内，稍微加快了速度。"
    Taka "唔唔嗯……"
    scene vid_main21_5 with dissolve
    MC "所以你会幻想被陌生男人操？"
    Taka "不、不是！……啊唔嗯，只、只是你……"
    MC "我现在就能这么做。"
    Taka "唔唔嗯嗯……"
    scene vid_main21_6 with dissolve
    MC "想象一下……把我的鸡巴掏出来，插进你紧致的处女小穴……"
    Taka "唔嗯……"
    scene vid_main21_7 with dissolve
    MC "在你把头抵在墙上的时候，我把鸡巴狠狠干进你体内……"
    Taka "唔唔嗯啊嗯！"
    MC "我看得出你想当个乖骚货……"
    Taka "啊啊啊唔嗯唔嗯……"
    scene vid_main21_8 with dissolve
    MC "我敢肯定用不了多久，你就会随着每次挺送把那个圆屁股往我身上撞。"
    Taka "唔嗯嗯唔嗯……"
    MC "我说错了吗？"
    scene vid_main21_9 with dissolve
    Taka "不、不……唔嗯唔嗯啊……"
    MC "你确实想当个乖骚货？"
    Taka "唔嗯……是、是的……"
    scene vid_main21_10 with dissolve
    MC "你想让我把你变成我的乖骚货？"
    Taka "啊唔嗯——是的！"
    scene vid_main21_11 with dissolve   
    "你开始相当粗暴地用手指弄她，整条手臂都在动，而她已经神魂颠倒，开始在你的手指上磨蹭。"
    MC "我看得出。"
    Taka "哦——哦唔嗯我的天……别、别停……啊唔嗯……"
    scene vid_main21_12 with dissolve
    MC "相信我，我不会停。"
    Taka "是的是的……"
    scene vid_main21_13 with dissolve
    MC "所以，我把你按在墙上，操了你紧致的小洞。"
    Taka "哦唔嗯呃呃嗯嗯……"
    scene vid_main21_14 with dissolve
    MC "我射进你体内了吗？"
    Taka "啊啊啊唔嗯嗯嗯嗯！哦唔嗯嗯嗯嗯嗯……"
    scene vid_main21_15 with dissolve
    "她的动作变得抽搐而狂野，一场爆发式的高潮撕裂过她的身体时，她绷紧并剧烈痉挛。"
    Taka "哦啊啊啊！啊啊——"
    "你的手指继续在她痉挛的小穴里研磨，一波又一波的快感反复冲刷着她。"

    scene img_main21_457 with dissolve
    "终于平息下来，你停下动作，她也稍微松弛了。"
    Taka "哈啊啊啊……呼……呼……呼……"   
    "小洗手间里唯一的声音就是她沉重的呼吸，随着她逐渐从高峰退下，那呼吸又长又破碎。"
    MC "唔，这可真轻松。"
    Taka "哈啊……唔嗯。"
    MC "你告诉我你从来没自己弄到过高潮时，我还以为得费更多功夫呢。"
    scene img_main21_458 with dissolve
    Taka "我、我……那、这跟我自己弄完全不一样……"
    MC "因为你想变成我的骚货？"
    scene img_main21_459 with dissolve
    Taka "啊……"
    scene img_main21_460 with dissolve
    Taka "......"
    scene img_main21_461 with dissolve
    Taka "是、是的……我想改变。"
    scene img_main21_462 with dissolve
    "你把她从墙上拉进一个背后环抱的姿势。"

    $ renpy.end_replay()


#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_akatsuki3:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/akatsuki_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0

    scene img_main21_797 with dissolve
    "趁晓月脱掉剩下的衣服时，你从那个红盒子里拿出一瓶润滑剂，为那个小肛塞做准备。"
    scene img_main21_798 with dissolve
    "等她彻底赤裸，她又满怀期待地抬头看着你。"
    scene img_main21_799 with dissolve
    pause
    scene img_main21_800 with dissolve
    pause
    scene img_main21_801 with dissolve
    MC "过来，到沙发上。"
    scene img_main21_802 with dissolve
    pause
    scene img_main21_803 with dissolve
    pause
    scene img_main21_804 with dissolve
    "她跟着你走过去，你坐下后，她顺从地横躺在你的腿上。"
    scene img_main21_805 with dissolve
    MC "把屁股撅给我。"
    scene img_main21_806 with dissolve
    Akatsuki "唔嗯。"
    scene img_main21_807 with dissolve
    pause
    scene img_main21_808 with dissolve
    MC "这个很小，应该很容易进去，不过一开始可能还是会有点疼。"
    Akatsuki "唔嗯。"
    scene img_main21_809 with dissolve
    "她抵挡不住诱惑，把屁股翘在空中勾引着你……"

    play sound "audio/sounds/spank_mid2.mp3"

    scene img_main21_810 with vpunch
    "{i}啪！{/i}"
    Akatsuki "唔嗯。"
    scene img_main21_811 with dissolve
    "摸了一会儿之后，你决定回到正题。"
    scene img_main21_812 with dissolve
    "你拿起肛塞抵在她身上，感觉到压力时她发出一声轻轻的哼声。"
    scene img_main21_813 with dissolve
    Akatsuki "啊唔嗯……"
    MC "准备好了吗？"
    scene img_main21_814 with dissolve
    Akatsuki "唔嗯。"
    scene img_main21_815 with dissolve
    "你再加了点力，开始用前端缓缓撑开她紧致的小洞。"
    scene img_main21_816 with dissolve
    Akatsuki "喵嗯……"
    scene img_main21_817 with dissolve
    pause
    scene img_main21_818 with dissolve
    "等你觉得她热好身了，你把肛塞推进她的屁股，抵抗了一下之后，啵的一声就进去了。"
    Akatsuki "呀啊！"
    #a few wiggles before text
    scene img_main21_819 with dissolve
    pause
    scene img_main21_820 with dissolve
    pause
    scene img_main21_819 with dissolve
    pause
    scene img_main21_820 with dissolve
    "从最初的震惊中缓过来后，她左右扭动屁股，试探这全新的感觉。"
    scene img_main21_819 with dissolve
    Akatsuki "唔嗯……"
    scene img_main21_821 with dissolve
    MC "感觉还行吗？"
    Akatsuki "唔嗯。"
    MC "很好。"
    scene img_main21_822 with dissolve
    MC "现在我要打你的屁股，直到你觉得惩罚够了为止。在你叫停之前我不会停，好吗？"
    scene img_main21_823 with dissolve
    Akatsuki "唔嗯。"

    play sound "audio/sounds/spank_mid3.mp3"

    scene img_main21_824 with vpunch
    "{i}啪！{/i}"
    scene img_main21_825 with dissolve
    Akatsuki "啊唔嗯！"
    "她的声音里带着一丝惊讶，你猜是肛塞的感觉加上打屁股打了她一个措手不及。"
    scene img_main21_826 with dissolve
    MC "这是一下。"

    play sound "audio/sounds/spank_mid2.mp3"

    scene img_main21_827 with vpunch
    "{i}啪！！{/i}"
    Akatsuki "啊唔嗯……"
    scene img_main21_828 with dissolve
    MC "两下。"

    play sound "audio/sounds/spank_heavy1.mp3"

    scene img_main21_829 with vpunch
    "{i}啪！！{/i}"
    Akatsuki "唔嗯……"
    MC "三下……"

    play sound "audio/sounds/spank_heavy2.mp3"

    scene img_main21_830 with vpunch
    "你又打了一会儿晓月的屁股，但她没有阻止你……"

    play sound "audio/sounds/spank_mid3.mp3"

    scene img_main21_831 with vpunch
    "..."

    play sound "audio/sounds/spank_mid2.mp3"

    scene img_main21_832 with vpunch
    "......"

    play sound "audio/sounds/spank_heavy1.mp3"

    scene img_main21_833 with vpunch
    "........."
    scene img_main21_834 with fade
    pause

    play sound "audio/sounds/spank_heavy2.mp3"

    scene img_main21_835 with vpunch
    "{i}啪！！{/i}"
    Akatsuki "啊……"
    MC "十下了……"
    MC "小猫，你的屁股明天会青的。已经够了吗？"
    scene img_main21_836 with dissolve
    Akatsuki "唔嗯。还要。"

    play sound "audio/sounds/spank_heavy1.mp3"

    scene img_main21_837 with vpunch
    "..."

    play sound "audio/sounds/spank_heavy2.mp3"

    scene img_main21_838 with vpunch
    "......"
    scene img_main21_839 with fade
    Akatsuki "唔嗯嗯……"
    "打到第十五下时，她在你手落下的一瞬发出一声压抑的痛呼，你开始怀疑她永远不会阻止你，只为证明她有多抱歉。"
    scene img_main21_840 with dissolve
    MC "好了，我觉得差不多了。"
    scene img_main21_841 with dissolve
    "她摇摇头撑起身子，却因为体内带着肛塞活动的触感而再次惊讶地抽了口气。"
    scene img_main21_842 with dissolve
    Akatsuki "喵啊嗯……"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main21_843 with dissolve
    "她若无其事地从你腿上滑下，利落地把鸡巴从你的裤子里掏了出来。"
    "你以为她要给你口交——你本来知道她喜欢这么做……"
    scene img_main21_844 with dissolve
    "但当她起身坐到你膝盖上时，你有些困惑了。"
    scene img_main21_845 with dissolve
    "不过片刻之后她的意图就清楚了：她握住你的鸡巴，坐直身子，摆好要和你做爱的姿势。"
    scene img_main21_846 with dissolve
    MC "第一次只有一次，小猫。不是这样的，我们该……"
    scene img_main21_848 with dissolve
    pause
    scene img_main21_850 with dissolve
    pause
    scene img_main21_847 with dissolve
    pause
    scene img_main21_849 with vpunch
    "她完全无视了你，把湿淋淋的小穴一下子坐到你的鸡巴上，又太重又太快。"
    scene img_main21_851 with dissolve
    Akatsuki "咿啊啊！……"
    scene img_main21_852 with dissolve
    "因为进入得太过粗暴，她惊叫了一声，然后把自己紧紧贴在你的胸口上。"
    scene img_main21_853 with dissolve
    Akatsuki "对不起……"
    scene img_main21_854 with dissolve
    "你立刻张开双臂把她抱住，回敬这个拥抱。"
    MC "我原谅你了，晓月。真的，没那么糟。"
    scene img_main21_855 with dissolve
    "她把脸埋进你的脖子，似乎急切地想离你越近越好。"
    scene img_main21_856 with dissolve
    pause
    "不管别的一切如何发生，你的脑子还是忍不住记下她小穴裹住你鸡巴时的美妙手感。"
    "紧致、湿润、温暖，还有她完全坐在你硬邦邦的柱身上时，身体为了容纳你而挣扎的感觉。"
    scene img_main21_855 with dissolve
    MC "我该拿你怎么办才好，小猫？用这种方式失去处女之身可不太好。"
    scene img_main21_857 with dissolve
    pause
    scene img_main21_858 with dissolve
    Akatsuki "我需要你知道。"
    MC "我明白了。你现在是我的了，对吧？"
    scene img_main21_859 with dissolve
    Akatsuki "唔嗯。"
    MC "感觉怎么样？"
    scene img_main21_860 with dissolve
    Akatsuki "很疼……就像你把我劈成两半一样。"
    MC "好吧，那就先到这里。"
    scene img_main21_861 with dissolve
    "你感觉她要反驳，于是打断了她。"
    MC "我保证我们会再来一次，好好地来。但现在，我不想看到你这么痛苦，好吗？"
    scene img_main21_862 with dissolve
    "当她脸上浮现出如释重负的神色时，你就知道自己做了正确的决定。"
    Akatsuki "唔嗯……"
    scene img_main21_863 with dissolve
    "你又一次把她拉进怀里，用这个动作尽可能细致温柔地吻了她，然后她把手撑在你的肩上站了起来。"
    scene img_main21_864 with dissolve
    pause
    scene img_main21_865 with dissolve
    pause
    scene img_main21_866 with dissolve
    "在你的手从她屁股上稍微帮了一下力的情况下，晓月把身子从你的柱身上抬起来，在滑出的瞬间因那感觉和疼痛而抽气。"
    scene img_main21_867 with dissolve
    pause
    scene img_main21_868 with dissolve
    Akatsuki "唔唔嗯嗯嗯……"
    scene img_main21_869 with dissolve
    "尽管这是最好的结果，你还是忍不住有点失望。她那紧致的小穴真的感觉妙极了。"
    scene img_main21_870 with dissolve
    "她从你腿上滑下来，黏黏糊糊地依偎进你怀里。"
    scene img_main21_871 with dissolve
    "过了一会儿，你开始怀疑这个略显别扭的姿势是不是因为肛塞。"
    MC "要我帮你取出来吗？"
    scene img_main21_872 with dissolve
    Akatsuki "不要。"
    "她只是把你抱得更紧，于是你决定她想这样待多久就待多久。"
    "..."
    "......"
    scene img_main21_873 with dissolve
    "........."
    scene img_main21_874 with dissolve
    "毫无预兆地，她的手紧紧握住了你的鸡巴。"
    scene img_main21_875 with dissolve
    Akatsuki "你还硬着。"
    MC "嗯。"
    scene img_main21_876 with dissolve
    pause
    scene img_main21_877 with dissolve
    pause
    scene img_main21_876 with dissolve
    pause
    scene img_main21_877 with dissolve
    pause
    scene img_main21_876 with dissolve
    pause
    scene img_main21_877 with dissolve
    "她开始温柔地上下撸动，拉扯着你的皮肤，让手指描过你硬邦邦的柱身上的肌肉。"
    scene img_main21_878 with dissolve
    pause
    scene img_main21_879 with dissolve
    pause
    scene img_main21_878 with dissolve
    pause
    scene img_main21_879 with dissolve
    "感觉很好，但她手缓慢温柔的动作让这一切更像是爱的举动，而非欲望的发泄。"
    scene img_main21_880 with dissolve
    "过了一会儿你看向她的脸，发现她柔和地朝你笑着，似乎很享受在你脸上看到的那个表情。"
    scene img_main21_881 with dissolve
    pause
    scene img_main21_882 with dissolve
    "你开始感觉到鸡巴在她柔软的手掌里跳动，最后她重新低头看，不是出于害羞，而是带着目的。"
    scene img_main21_883 with dissolve
    "她调整了姿势，让嘴能够到你的鸡巴，开始舔前端，同时手仍在温柔地上下撸动柱身。"
    scene img_main21_884 with dissolve
    pause
    scene img_main21_885 with dissolve
    pause
    scene img_main21_884 with dissolve
    pause
    scene img_main21_885 with dissolve
    Akatsuki "唔嗯……"
    scene img_main21_884 with dissolve
    MC "乖女孩。"
    scene img_main21_886 with dissolve
    Akatsuki "啊唔嗯嗯……"
    scene img_main21_887 with dissolve
    Akatsuki "哦唔嗯嗯……"
    "她丝滑温暖的嘴、舌头和唾液，同时点燃了你每一个神经末梢。"
#more paired repeating images for player to click through
    scene img_main21_888 with dissolve
    pause
    scene img_main21_889 with dissolve
    pause
    scene img_main21_890 with dissolve
    pause
    scene img_main21_891 with dissolve
    Akatsuki "唔嗯嗯……"
    scene img_main21_892 with dissolve
    "她吸吮时偶尔发出的水声，和她满足你时柔和而闷闷的哼声混在一起。"
    scene img_main21_893 with dissolve
    Akatsuki "唔嗯……"
    scene img_main21_894 with dissolve
    "她没有含得很深，更愿意用嘴而不是喉咙，但看着她热情地吸吮，你对这个结果已经非常满意。"
    scene img_main21_895 with dissolve
    "再没有比这更清楚的了：此刻她满脑子只有你的快感，而她也一点一点加快了速度、加大了力度。"
    scene img_main21_892 with dissolve
    Akatsuki "唔嗯嗯……"
    scene img_main21_893 with dissolve
    MC "操……这样很好，小猫。"

    scene img_main21_896 with dissolve
    Akatsuki "唔嗯……"
    scene img_main21_897 with dissolve
    "角度不太好，但你还是伸手挤捏她一只结实的乳房，而她继续吸着。"
    scene img_main21_898 with dissolve
    Akatsuki "唔嗯嗯……"
    scene img_main21_899 with dissolve
    "你用力捏了一下她的乳头，她含着你的龟头发出惊讶又愉悦的呻吟。"
    scene img_main21_900 with dissolve
    Akatsuki "唔唔嗯嗯！！"
    scene img_main21_901 with dissolve
    "但她像是在报复一样进一步加强力度，你的注意力从她胸口被引开；她此刻似乎急切地想让你射进她辛勤工作的嘴。"
    scene img_main21_902 with dissolve
    MC "操，小猫，我要射了。"
    scene img_main21_903 with dissolve
    Akatsuki "唔嗯嗯……"
    scene img_main21_904 with dissolve
    pause
    scene img_main21_905 with dissolve
    pause
    scene img_main21_904 with dissolve
    pause
    scene img_main21_905 with dissolve
    pause
    scene img_main21_904 with dissolve
    pause
    scene img_main21_905 with dissolve
    pause
    scene img_main21_904 with dissolve
    pause
    scene img_main21_905 with dissolve
    pause



    scene img_main21_906 with vpunch
    pause 0.5
    scene img_main21_907 with vpunch
    pause 0.35
    scene img_main21_906 with vpunch
    pause 0.2
    scene img_main21_907 with vpunch
    pause 0.1
    scene img_main21_908 with vpunch
    pause 0.1
    scene img_main21_908 with flash
    "她把时机掐得分毫不差，在你爆发射进她那张急切的嘴时紧紧捏住你的柱身，拼命吸吮。"
    scene img_main21_908 with flash
    MC "操……！"
    scene img_main21_908 with flash
    Akatsuki "唔唔嗯嗯呃呼嗯……"
    scene img_main21_909 with dissolve
    "她一直含着，直到完全确信已经把你睾丸里的每一滴精液都吸了出来……"
    scene img_main21_910 with dissolve
    "才退开，仰头朝你笑了笑。"
    scene img_main21_911 with dissolve
    MC "乖女孩，刚才太棒了。"
    Akatsuki "唔嗯。"
    scene img_main21_912 with dissolve
    "她似乎很满足，蜷起身子把头枕在你的腿上。"

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_victoria5:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/victoria_theme.mp3" loop volume 1.0 fadeout 1.0 fadein 1.0

    scene img_main22_561 with fade
    "过了很久她才离开，坐直身子，脸上带着笑，动作里满是兴奋的弹跳。"
    Victoria "我们再做一次吧。"

    play sound "audio/sounds/bed.mp3" volume 4.0

    scene img_main22_562 with dissolve
    "你脸上浮起笑容，低吼一声站起来，把她重新推回床上。"
    scene img_main22_563 with dissolve
    Victoria "呃……你能帮我做件事吗？"
    MC "什么都行。"
    scene img_main22_564 with dissolve
    Victoria "不要留手。不管我有多痛，就算我尖叫、哭泣或者怎样。让我的身体永远属于你。"
    MC "你确定？我本来打算循序渐进地把你调教到那一步……"
    Victoria "对，完全不要。"
    scene img_main22_565 with dissolve
    pause
    scene img_main22_566 with dissolve
    Victoria "唔嗯……"
    scene img_main22_567 with dissolve
    pause
    scene img_main22_568 with dissolve
    pause
    scene img_main22_569 with dissolve
    "你从吻中分开，用力把她的手腕压进床垫，你们的目光对上一瞬，她朝你咧嘴笑。"
    MC "我觉得你还没资格再挨一次操。我想先只用你的嘴。"
    scene img_main22_570 with dissolve
    Victoria "主人……这不公平！"
    scene img_main22_571 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main22_572 with dissolve
    pause
    scene img_main22_573 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main22_574 with dissolve
    "尽管嘴上抗议，她还是顺从地把手举在头顶，任你把她的上衣拉上去。"
    scene img_main22_575 with dissolve
    "你往后靠上床头板，薇琪则在一旁看着你，依旧撅着嘴。"
    scene img_main22_576 with dissolve
    pause
    scene img_main22_577 with dissolve
    "不用吩咐，她就立刻爬过床来，把你的鸡巴掏了出来。"
    scene vid_main22_1 with dissolve
    "片刻之后，她把前端完全吞进温暖湿润的嘴。"
    scene vid_main22_2 with dissolve
    Victoria "唔唔嗯嗯嗯……"
    MC "乖女孩。"
    scene vid_main22_3 with dissolve
    Victoria "唔嗯嗯嗯……"
    "..."
    "......"
    scene vid_main22_4 with dissolve
    MC "操……你唱歌很好听，但这才是你嘴真正该干的事。"
    Victoria "唔嗯——唔嗯嗯……"
    MC "那么，如果我不留手，你真觉得自己承受得住吗？"
    scene vid_main22_5 with dissolve
    "你能感觉到她含着你的鸡巴突然笑了起来，因为她意识到你终究还是打算操她。"
    Victoria "唔嗯！"
    MC "我可不那么确定……毕竟你之前紧得要命……也许我们该用一些玩具先把你调教一下？"
    scene vid_main22_6 with dissolve
    Victoria "唔唔嗯嗯。"
    "她摇了摇头，你的鸡巴仍然埋在她吸吮的怀抱里。"
    scene vid_main22_7 with dissolve
    MC "我想亲自弄坏你会更令人满足……"
    Victoria "唔嗯！"
    MC "好了，坐起来。把牛仔裤脱掉。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main22_578 with dissolve
    "她抹掉嘴边的唾液，然后往后坐，迫不及待地脱下牛仔裤。"
    scene img_main22_579 with dissolve
    pause
    scene img_main22_580 with dissolve
    pause
    scene img_main22_579 with dissolve
    MC "过来。"
    scene img_main22_581 with dissolve
    Victoria "当然，主人！"
    scene img_main22_582 with dissolve
    "又一次不用吩咐，她就立刻回去为你口交。"
    scene img_main22_583 with dissolve
    MC "乖女孩，你学得很快。好了，现在我允许你用手指了。"
    scene img_main22_584 with dissolve
    pause
    scene img_main22_585 with dissolve
    "她空着的那只手立刻伸向自己的下面，一边继续给你口交，一边开始玩弄自己。"
    scene vid_main22_8 with dissolve
    MC "如果你嘴上的功夫继续保持这么好，我或许会考虑射进你那近乎处女的小穴里。"
    Victoria "唔哼嗯唔嗯嗯……"
    scene vid_main22_9 with dissolve
    "..."
    "......."
    "你让她吸吮并自慰了好长一段时间，直到你感觉到自己快要射进她嘴里……"
    scene img_main22_586 with dissolve
    "但在走到那一步之前，你伸手按住她的头，把她的嘴从你的鸡巴上带开。"
    scene img_main22_587 with dissolve
    Victoria "唔嗯……"
    scene img_main22_588 with dissolve
    pause
    scene img_main22_589 with dissolve
    MC "我想那还不算太糟。"
    scene img_main22_590 with dissolve
    "她撅起嘴，却笑了。"
    Victoria "哼……你真是个坏蛋，主人。"
    MC "把内裤脱掉。"
    scene img_main22_591 with dissolve
    "她按吩咐把内裤丢到一边，然后仰面躺下，手仍在双腿之间忙碌着。"
    scene img_main22_592 with dissolve
    pause
    scene img_main22_593 with dissolve
    MC "不，这次我要看着那个屁股在我的鸡巴上弹跳，同时让你尖叫。翻过身去。"
    scene img_main22_594 with dissolve
    Victoria "唔嗯……放马过来吧，主人。"

    play sound "audio/sounds/bed.mp3" volume 4.0

    scene img_main22_595 with dissolve
    "她翻身趴下，但姿势还不是你想要的，她回过头来挑衅地看着你。"
    scene img_main22_596 with dissolve
    pause

    play sound "audio/sounds/spank_heavy1.mp3"

    scene img_main22_597 with vpunch

    
    "{i}啪！{/i}"
    Victoria "唔嗯。"
    scene img_main22_598 with dissolve
    MC "脸朝下，屁股撅起来。"
    scene img_main22_599 with dissolve
    Victoria "像这样吗？"
    scene img_main22_600 with dissolve
    MC "差不多……"
    scene img_main22_601 with dissolve
    pause
    scene img_main22_602 with dissolve
    "你伸手下去把她的一个手臂往后拉，逼得她的背弓得更深。"
    scene img_main22_603 with dissolve
    Victoria "唔唔嗯嗯……"
    scene img_main22_604 with dissolve
    pause
    scene img_main22_605 with dissolve
    Victoria "你以前从没对我这么粗暴过……我绝对能习惯的……"
    scene img_main22_606 with dissolve
    MC "哦，你会的。"
    scene img_main22_607 with dissolve
    MC "现在……"
    scene img_main22_608 with dissolve
    "你把鸡巴握在手上，抵在她湿淋淋的小穴入口。"
    scene vid_main22_10 with dissolve
    MC "我希望你那些手指没白弄，因为我不会慢慢来。我现在兴奋得不行，只想射进你肚子里深处。"
    scene vid_main22_11 with dissolve
    Victoria "是的啊啊嗯唔嗯！！"
    "你把她的另一只手臂从床上拉起，一气呵成地把鸡巴送到底，她尖叫一声、略微弓起身子，随后脸和胸都撞在床垫上。"
    Victoria "啊啊啊！操……好大……"
    "尽管她要求你不要留手，你还是给了她一秒来适应被无助地钉在你鸡巴上的感觉。"
    scene vid_main22_12 with dissolve
    "不过，你也不想对她太温柔……"
    scene vid_main22_13 with dissolve
    pause
    Victoria "唔……唔嗯……唔嗯嗯……"
    "每次到底插进她体内时她都会发出一声轻哼，显然仍有些疼痛，但已经和第一次完全不一样了。"
    scene vid_main22_14 with dissolve
    MC "乖女孩，这次你承受得好多了。"
    Victoria "啊……唔嗯嗯……"
    scene vid_main22_15 with dissolve
    "她回过头用邪恶的笑容看着你，而你继续把她操进床垫里。"
    MC "完全任我摆布的感觉怎么样？"
    Victoria "真、真他妈……好、好棒……爽死了……"
    MC "很好，那我不客气加速了……"
    Victoria "唔嗯……唔嗯嗯……放马过来……"
    scene vid_main22_16 with dissolve
    "你加快速度，开始用又长又深的抽插动作……"
    "每一次你都把她的手臂往后拉，逼她的身体跟上你的节奏，同时在她紧夹、湿透的小穴里进进出出。"
    Victoria "哦——哦……操……"
    "你第一次觉得她的自信有了一丝动摇，她脸上的表情明显染上了痛苦……"
    scene vid_main22_17 with dissolve
    pause
    "但接着你注意到她每次挺送都用屁股撞向你的大腿，热情地把身子压回你的鸡巴上。"
    MC "你真是个乖受虐狂。"
    Victoria "啊……唔哼——唔嗯嗯……"
    scene vid_main22_18 with dissolve
    pause
    "你们保持这个节奏好一阵子，快感在两人相连的地方流淌。"
    "每一次抽送过去，你都开始感觉到薇琪变得更自信，也更能习惯被操了。"
    scene vid_main22_19 with dissolve
    Victoria "唔嗯嗯……主人！"
    "..."
    "......"
    scene vid_main22_20 with dissolve
    "确定她能承受之后，你让自己更原始的一面占据上风，速度又加快了些。"
    "这让她乱了一瞬，但很快又跟上你的节奏，再次摇着屁股迎上每一次挺送。"
    scene vid_main22_21 with dissolve
    pause
    Victoria "啊啊啊唔嗯……操……继、继续！"
    MC "唔嗯……你再指挥我，我就停下来了。"
    Victoria "不——操……求你了主人……我、我……"
    MC "你最好别比我先射，薇琪……"
    Victoria "唔嗯我、我……我唔嗯嗯……"
    scene vid_main22_22 with dissolve
    pause
    "你能感觉到她快要失控了，你鸡巴每一次粗暴的挺送都把她推得更接近临界点……"
    "但让她强忍着固然很有趣……她那紧致湿透的小穴也把你逼近了射精的边缘，无论你准没准备好。"
    scene vid_main22_23 with dissolve
    MC "操……在我射进你体内深处之前不行。"
    Victoria "唔嗯是的是的……我想要！"
    scene vid_main22_24 with dissolve
    pause
    "你进一步加快，以短促快速的动作用力地在她火热的小洞里进出。"
    scene vid_main22_25 with dissolve
    Victoria "啊唔嗯嗯嗯主人啊啊啊！！！"
    MC "唔嗯嗯……"
    "你咬紧牙关，不可避免的事情发生时，只来得及从喉咙里挤出一声闷哼……"
    Victoria "啊……我、我……我要……啊啊唔嗯嗯嗯嗯！"
    scene vid_main22_26 with flash
    "你把鸡巴狠狠撞进她因高潮而痉挛的小穴，把全部精液射进她体内深处。"
    Victoria "是的是的唔唔嗯嗯嗯唔嗯嗯嗯嗯！！！！"
    scene vid_main22_27 with flash
    "你射出最后一股精液，又抱了她好一会儿，她仍在痉挛的快感中扭动……"
    scene img_main22_609 with dissolve #may be removable for final frame pause of video
    pause

    play sound "audio/sounds/bed.mp3" volume 4.0

    scene img_main22_610 with vpunch
    "最后，当你们俩都被高潮弄得晕乎乎、喘不过气时，你松开她的手臂，让她跌回床上。"

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_akatsuki4:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0

    scene img_main22_17 with dissolve
    "你们俩脱完剩下的衣服，一起进了淋浴间。"

    play ambiance "audio/sounds/shower.mp3" volume 0.6 loop

    scene img_main22_18 with dissolve
    pause
    scene img_main22_19 with dissolve
    pause
    scene img_main22_20 with dissolve
    pause
    scene img_main22_21 with dissolve
    pause
    scene img_main22_22 with dissolve
    "你花了几分钟欣赏她挑逗般清洗身体的样子，然后在她注意到你的勃起时，逮到她朝你笑。"
    scene img_main22_23 with dissolve
    "她立刻放下手臂，抓住你的鸡巴。"
    scene img_main22_24 with dissolve
    Akatsuki "我的。"
    scene img_main22_25 with dissolve
    pause
    scene img_main22_26 with dissolve
    pause
    scene img_main22_27 with dissolve
    pause
    scene img_main22_28 with dissolve
    pause
    scene img_main22_29 with dissolve
    pause
    scene img_main22_30 with dissolve
    pause
    scene img_main22_31 with dissolve
    pause
    scene img_main22_32 with dissolve
    pause

    play ambiance "audio/sounds/shower_end.mp3" noloop volume 0.6

    scene img_main22_33 with dissolve
    pause

    scene img_main22_34 with dissolve
    "痛痛快快地冲了个澡后，你们穿好衣服下楼，晓月一刻也不想离开你身边。"

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_akatsuki5:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0

    scene img_main23_17 with dissolve
    "在洗手间里，你转身要关门，却发现身后多了个影子——晓月已经无声地从门缝里溜了进来。"
    scene img_main23_18 with dissolve
    pause

    play sound "audio/sounds/door.mp3"

    scene img_main23_19 with dissolve
    "薇琪饶有兴致地看着你们俩脱衣服。"
    scene img_main23_20 with dissolve
    "你脱衣服时注意到边桌上摆着几样位置很讲究的东西，心想是不是她故意放在那里的。"

    play ambiance "audio/sounds/shower.mp3" volume 0.6 fadein 1.0 loop

    scene img_main23_21 with fade
    pause
    scene img_main23_22 with dissolve
    MC "还好你个子小，小猫，这个淋浴间可不够三个人用。"
    Akatsuki "唔嗯。"
    scene img_main23_23 with dissolve
    pause
    scene img_main23_24 with dissolve
    pause
    scene img_main23_25 with dissolve
    "你的目光在你身旁两个湿透的美人之间来回撕扯，而你丝毫没有掩饰自己在打量她们。"
    scene img_main23_26 with dissolve
    pause
    scene img_main23_27 with dissolve
    "薇琪似乎很享受这种关注，摆出暧昧的姿势……"
    scene img_main23_28 with dissolve
    "而晓月一如既往地直奔你的鸡巴。"
    scene img_main23_29 with dissolve
    pause
    scene img_main23_30 with dissolve
    pause
    scene vid_main23_1 with dissolve
    pause
    "..."
    scene vid_main23_2 with dissolve
    pause
    "......"
    scene vid_main23_3 with dissolve
    pause
    "........."
    scene img_main23_31 with vpunch
    scene img_main23_31 with flash
    pause
    scene img_main23_32 with vpunch
    scene img_main23_32 with flash
    pause
    scene img_main23_33 with dissolve
    "淋浴在晓月热情的口交中结束，你则看着薇琪在倾泻的水流中用她曲线玲珑的身体为你表演。"
    MC "乖女孩。"
    scene img_main23_34 with dissolve
    Akatsuki "唔嗯嗯。"

    play ambiance "audio/sounds/shower_end.mp3" noloop volume 0.6

    scene img_main23_35 with fade
    pause
    scene img_main23_36 with dissolve
    Victoria "原来你们两个在淋浴间里干的是这种事……我可能得早点起床了。"
    MC "说得好像你做得到似的。"
    "她撅起嘴，但耸了耸肩，显然承认你说得可能没错。"
    scene img_main23_37 with dissolve
    MC "好了小猫，该继续罚你了。把那个可爱的小屁股带过来。"
    scene img_main23_38 with dissolve
    Akatsuki "唔嗯！"
    MC "弯腰。"
    scene img_main23_39 with dissolve
    pause
    scene img_main23_40 with dissolve
    pause
    scene img_main23_41 with dissolve
    "你从旁边拿起那个位置讲究的肛塞，在前端涂上一大团润滑剂……"
    scene img_main23_42 with dissolve
    pause
    scene img_main23_43 with dissolve
    Akatsuki "唔嗯嗯……"
    scene img_main23_44 with dissolve
    "你再一次把肛塞推进她紧致的小菊花，她被撑开时发出轻轻的呻吟。"
    Akatsuki "唔嗯……"
    scene img_main23_45
    Akatsuki "啊！"

    play sound "audio/sounds/spank_mid2.mp3"

    scene img_main23_46 with hpunch
    "{i}啪！{/i}"
    Akatsuki "唔嗯！"
    scene img_main23_47 with dissolve
    pause
    scene img_main23_48 with dissolve
    "你站起来，发现薇琪正着迷地看着。"
    scene img_main23_49 with dissolve
    Victoria "主人……你手上该不会还有另一个那种东西吧？"
    MC "没有，可惜我只有一个。现在看来真有点短视。"
    Victoria "唔嗯，真可惜……"
    MC "别担心，我肯定能想出办法。"
    scene img_main23_50 with dissolve
    "..."

    play sound "audio/sounds/spank_mid3.mp3"

    scene img_main23_51 with vpunch
    "{i}啪！{/i}"
    Akatsuki "喵！"
    scene img_main23_52 with dissolve
    MC "好了小猫，把校服套上去。我会允许你在开门营业前把它取出来。"
    scene img_main23_53 with dissolve
    "她别扭地站起来，显然屁股里的异物让她有些不适。但随后她还是抬头朝你露出一个意味深长的微笑。"
    scene img_main23_54 with dissolve
    Akatsuki "唔嗯。"
    scene img_main23_55 with dissolve
    Victoria "什么感觉，小猫？我可从没在屁股里塞过东西。"
    scene img_main23_56 with dissolve
    Akatsuki "唔嗯……紧。"

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_akatsuki6:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/swimming_trip.mp3" loop fadeout 1.0 fadein 1.0 volume 0.5

    "你转过身准备换衣服，却发现身边不知何时多了一位猫科追随者。"
    MC "我怎么会不惊讶呢？"
    scene img_main23_444 with dissolve
    "她只是耸耸肩，笑了笑。"
    Akatsuki "喵。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main23_445 with dissolve
    "你和晓月一起开始换衣服……"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main23_446 with dissolve
    pause
    "在你们俩都光着身子的瞬间，她扑了上来。"
    scene img_main23_447 with dissolve
    pause
    scene img_main23_448 with dissolve
    "她用那双急躁的小手很快就把你弄到硬如石头，一点时间都不浪费地把你滑进嘴里。"
    scene img_main23_449 with dissolve
    MC "操……你得快点结束，小猫。"
    scene img_main23_450 with dissolve
    Akatsuki "唔嗯……"
    scene img_main23_451 with dissolve
    pause
    scene img_main23_452 with dissolve
    pause
    scene img_main23_451 with dissolve
    pause
    scene img_main23_452 with dissolve
    pause
    scene img_main23_451 with dissolve
    pause

    play sound "audio/sounds/door_delay.mp3"

    scene img_main23_453 with fade
    "几分钟后，你听到门被推开，从那对快速晃动的猫耳上方望去，看见了一脸玩味的薇琪。"
    scene img_main23_454 with dissolve
    Victoria "我们一发现她不见了，就知道会在这种地方找到她。"
    Akatsuki "唔嗯……"
    scene img_main23_455 with dissolve
    Victoria "不过我们是来游泳的……所以我想我该帮忙加快点速度……"
    scene img_main23_456 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main23_457 with dissolve
    pause
    scene img_main23_458 with dissolve
    "她脸上浮现一个撩人的神色，把上衣拉起来，然后引导你的手去握住她的一只大奶子。"
    scene img_main23_459 with dissolve
    Victoria "啊……就是这样，主人……你想怎么揉都行……我完全是你的……"
    scene img_main23_460 with dissolve
    Victoria "揉吧，让她那张湿漉漉的小嘴在你又大又硬的鸡巴上上下滑动……"
    scene img_main23_461 with dissolve
    Victoria "为我们射出来吧，主人……全都放出来……射进她嘴里……"
    scene img_main23_462 with dissolve
    pause
    scene img_main23_463 with dissolve
    pause
    scene img_main23_464 with dissolve
    pause
    scene img_main23_465 with flash
    "晓月的嘴和薇琪的荤话两面夹击，你很快就射了一大堆。"
    scene img_main23_466 with flash
    Akatsuki "唔嗯嗯嗯……"
    scene img_main23_467 with flash
    Victoria "唔嗯，还挺刺激。"
    MC "操……"
    MC "你身上可能也有一点露西的成分，你好像和我一样享受那个？"
    scene img_main23_468 with dissolve
    Victoria "哈，我还没到露西那个程度。但我说过我理解她为什么会那样，记得吧？"

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_group2:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/swimming_pool.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0

    scene img_main23_610 with dissolve
    "你们一行人鱼贯进入更衣室，这一次除了晓月，你身边还多了两位同伴。"
    scene img_main23_611 with dissolve
    Lucy "你、你说要罚我们的，记得吧……"
    MC "我记得，乖女孩……"
    MC "唔嗯……"
    scene img_main23_612 with dissolve
    MC "你觉得你还能再来一次口交吗，小猫？"
    scene img_main23_613 with dissolve
    Akatsuki "唔嗯！"
    scene vid_main23_4 with dissolve
    pause
    "你这句话还没说完，她就已经把鸡巴掏出来干上了。"
    "猫娘丝滑的双唇开始沿你的柱身上下滑动，丝绒般湿润的舌头按摩着下侧，露西的眼睛立刻因兴奋而睁大……"
    scene vid_main23_5 with dissolve
    MC "操，乖女孩……"
    Akatsuki "唔嗯……"
    scene vid_main23_6 with dissolve
    MC "把上衣拉下来，露西。然后你们两个都跪到晓月旁边。"
    Lucy "好、好的。"
    Victoria "当然，主人！"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene vid_main23_7 with dissolve
    MC "完美……"
    scene vid_main23_8 with dissolve
    "..."
    scene vid_main23_9 with dissolve
    "......"
    scene vid_main23_10 with dissolve
    MC "看得开心吗，露西？"
    Lucy "啊……唔嗯嗯……"
    scene img_main23_614 with dissolve
    "晓月飞速进步的技术很快把你推向临界点，当你快要再次射进她那张饥渴的小嘴时，你叫停了她。"
    scene img_main23_615 with dissolve
    MC "操，我快射了……靠近一点……"
    scene img_main23_616 with dissolve
    pause
    scene img_main23_617 with dissolve
    "当你把鸡巴指向跪着的女孩们时，晓月立刻明白了你的意图，用手帮你弄了出来……"
    scene img_main23_618 with dissolve
    pause
    scene img_main23_617 with dissolve
    pause
    scene img_main23_618 with dissolve
    pause
    scene img_main23_617 with dissolve
    pause
    scene img_main23_618 with dissolve
    pause
    scene img_main23_617 with dissolve
    pause
    scene img_main23_619 with flash
    pause
    scene img_main23_620 with flash
    Lucy "啊……"
    scene img_main23_621 with flash
    pause
    scene img_main23_622 with flash
    Victoria "唔嗯嗯，主人……"
    scene img_main23_623 with dissolve
    pause
    scene img_main23_624 with dissolve
    pause
    scene img_main23_623 with dissolve
    pause
    scene img_main23_624 with dissolve
    "晓月帮你挤出了睾丸里最后几滴，你把它们涂满了她们的脸和胸……"
    MC "操……"
    scene img_main23_625 with dissolve
    MC "好了，快去。进淋浴间之前要让别的姑娘们都看见你。"
    scene img_main23_626 with dissolve
    Victoria "唔嗯，你真坏，主人。"
    scene img_main23_627 with dissolve
    Lucy "啊、啊……"
    scene img_main23_628 with dissolve
    Victoria "来吧，小露，你以前和我做过这种事，对吧？而且这次我们会一起……"
    Lucy "对、对……"
    scene img_main23_629 with dissolve
    "她脸上又浮现出害羞的笑容，薇琪兴奋地把她拉出了房间。"

    play sound "audio/sounds/door.mp3"

    scene img_main23_630 with dissolve
    MC "乖女孩。今天第三次了。"
    scene img_main23_631 with dissolve
    Akatsuki "唔嗯……我的下巴开始累了。"
    MC "那我们以后是不是该稍微节制一点？"
    scene img_main23_632 with dissolve
    Akatsuki "不要。我还想要更多。"
    Akatsuki "我还想再和你做一次爱……"
    scene img_main23_633 with dissolve
    "她有点害羞地低下头，然后继续说。"
    Akatsuki "再一次，再一次，再一次。"
    MC "这可以安排。"

    play music "audio/bgm/akatsuki_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
    play ambiance "audio/sounds/shower.mp3" volume 0.6 fadeout 1.0 fadein 1.0 loop

    scene img_main23_634 with dissolve
    pause
    scene vid_main23_11 with dissolve
    pause
    scene vid_main23_12 with dissolve
    "你们俩一起洗澡，然后一件事牵出另一件事，最后你在流水下用手指弄她。"
    scene vid_main23_13 with dissolve
    "..."
    scene vid_main23_14 with dissolve
    Akatsuki "唔嗯嗯嗯！"
    "几乎没过多久，她紧致的小穴就紧紧夹住你的手指，陷入一场让她脚趾蜷缩、脊背弓起的高潮。"
    scene img_main23_636 with dissolve
    pause
    scene img_main23_637 with dissolve
    MC "操，小猫……我从没见过哪个女孩这么快就高潮……"
    scene img_main23_638 with dissolve
    Akatsuki "实在太舒服了……我忍不住……"
    MC "你真是天生当性虐小猫的料。"
    scene img_main23_639 with dissolve
    Akatsuki "唔嗯。你的性虐小猫。"
    MCi "（我觉得差不多该把这事正式定下来了……）"

    $ renpy.end_replay()




#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_lucy7:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/lucy_theme.mp3" loop volume 1.2 fadeout 1.0 fadein 1.0

    scene img_main25_675 with dissolve
    "里面一片漆黑，你掏出手机，用屏幕的光照亮散落一地的店铺杂物。"
    scene img_main25_676 with dissolve
    MC "好了，宝贝，过来。"
    scene img_main25_677 with dissolve
    "你带她绕到堆叠的箱子后面，至少能多挡一点门口的方向，以防有人进来，然后把手机放下，光朝上照着。"
    scene img_main25_678 with dissolve
    MC "就像今天早上在淋浴间里那样。手扶在墙上，把那个屁股给我看。"
    scene img_main25_679 with dissolve
    Lucy "唔嗯嗯嗯——唔嗯……"
    scene img_main25_680 with dissolve
    MC "完美。"
    scene img_main25_681 with dissolve
    MC "现在让我看看这里都有什么……"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main25_682 with dissolve
    "你把她的裙子从下往上撩起，再把她的连裤袜拉下来，露出她湿透的一团内裤。"
    scene img_main25_683 with dissolve
    Lucy "唔嗯嗯……"
    scene img_main25_684 with dissolve
    MC "靠，你的大腿都湿透了，露西……"
    scene img_main25_685 with dissolve
    Lucy "唔嗯嗯……这、这个震动棒……我从没感受过这种东西。"

    play sound "audio/sounds/vibrator.mp3" loop fadein 1.0

    scene img_main25_686 with dissolve
    "你把手伸进口袋，又把档位调到最大，同时隔着内裤把它推进她的小穴。"
    scene img_main25_687 with dissolve
    Lucy "唔唔嗯唔嗯！！[PlayerName]！！"
    "她在快感中扭动，你再也等不及了。"
    scene img_main25_688 with dissolve
    "你把涨硬的鸡巴掏出来做准备……"
    scene img_main25_689 with dissolve
    "然后一把将她的内裤连同震动棒一起拉了下来……"

    stop sound

    scene img_main25_690 with dissolve
    "大功告成，你从她湿漉漉的衣物纠缠中抽出那个湿透的粉色装置，放到一边。"
    scene img_main25_691 with dissolve
    "然后你不再耽搁，把鸡巴对准她的穴口……"
  
    scene vid_main25_1 with dissolve
    "一口气送到底，她感觉自己的紧致小穴被劈开，不由自主地抽气尖叫。"
    Lucy "唔唔嗯唔嗯！是的是的！！！"
    scene vid_main25_2 with dissolve
    "知道你们俩都没心情玩花样，你开始在她温暖湿透的小洞里进出，每一次挺送都带出细小的水声。"
    Lucy "唔嗯……唔嗯……唔嗯……"
    MC "操，露西……这感觉真棒。"
    scene vid_main25_3 with dissolve
    Lucy "你、你也一样……唔嗯嗯嗯我、我……天啊……"
    scene vid_main25_4 with dissolve
    Lucy "我、我要……"
    MC "想都别想。在我允许之前你得忍住。"
    Lucy "唔嗯嗯不要，我、我忍不住了！"
    scene vid_main25_5 with dissolve
    MC "你可以。难道你不想同时高潮吗？"
    Lucy "唔嗯——是、是的……可、可是……我、我、我……"
    scene vid_main25_6 with dissolve
    "你继续挺送，开始感觉到她小穴里的肌肉在你柱身上抽搐，她正徘徊在爆发式高潮的边缘。"
    MC "操……再这样下去我很快就射了……"
    Lucy "唔嗯嗯快点啊！！！"
    scene vid_main25_7 with dissolve
    "露西自己加快了节奏，蹬开墙壁，摇着屁股往回靠，用她紧致痉挛的小穴按摩你的鸡巴。"
    MC "靠……乖女孩……"
    scene vid_main25_8 with dissolve
    Lucy "求求你了[PlayerName]！！！我、我……我要……"
    MC "操……再等一下下……"
    scene vid_main25_10 with dissolve
    "..."
    "......"
    "........."
    scene vid_main25_9 with dissolve
    Lucy "唔嗯我、我需要你，[PlayerName]……"
    scene vid_main25_11 with dissolve
    Lucy "我、唔嗯啊……我、我需要你的精液射在我体内……"
    scene vid_main25_12 with dissolve
    Lucy "求你了[PlayerName]，你可以的……求你填满我……"
    
    scene vid_main25_13 with flash
    Lucy "我——是的唔嗯嗯唔嗯嗯嗯啊啊啊……"
    "就在露西用荤话拼命想让你射出来时，你在她痉挛的小穴里爆发了，打断了她的话。"
    "这立刻让她陷入一场浑身战栗的高潮，你把精液泵进她子宫的深处。"
    "..."
    scene vid_main25_14 with dissolve
    "你们俩站了一会儿，喘息沉重，电流般的冲动在你们体内乱窜……"
    "..."
    "......"
    MC "操……"
    scene vid_main25_15 with dissolve
    "你把鸡巴从她湿淋淋的一团中抽出来，突然空荡荡的感觉让她不由自主地呻吟了一声。"
    Lucy "啊唔嗯嗯……"


    scene img_main25_692 with dissolve
    "你还看到她勉强想站起来，显然还没从爆发式的高潮中完全恢复，于是从背后抱住她，把她撑在墙上。"
    scene img_main25_693 with dissolve
    MC "{i}*低语{/i}操。真舒服，露西。"
    scene img_main25_694 with dissolve
    Lucy "{i}*低语{/i}唔嗯嗯……最棒的……"
    scene img_main25_695 with dissolve
    "这个亲密的拥抱又持续了一会儿，你们都从高峰退下，让心率恢复正常。"
    "..."
    "......"
    MC "{i}*低语{/i}该走了，这里还不算百分之百安全。"
    scene img_main25_696 with dissolve
    "你退后一步，低头看着她大腿间那滩正在往下淌的一团。"
    MC "我知道自己平时不喜欢紧身裤……但它们有一个好处……"
    Lucy "唔嗯？"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main25_697 with dissolve
    "你把她的内裤和连裤袜拉上去，把下面的一切都遮住。"
    MC "它们很擅长掩盖证据。"
    scene img_main25_698 with dissolve
    Lucy "啊……我、我……"
    MC "哈，别告诉我你到现在才意识到自己得这样走出去？"
    scene img_main25_699 with dissolve
    Lucy "我、我刚才根本没法思考……天啊……"
    MC "走吧，没事的。我会一直陪着你。"

    $ renpy.end_replay()




#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_taka2:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/taka_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0

    scene img_main24_522 with fade
    "和之前一样，你们一起下车，确认没有人之后把她拉进那间小洗手间。"

    play sound "audio/sounds/door_close.mp3" volume 2.0

    scene img_main24_523 with dissolve
    pause

    play sound "audio/sounds/door_lock.mp3" volume 1.0

    scene img_main24_524 with dissolve
    "你关上隔间门转过身，发现她正面对着你，微微吃了一惊，但看到她闭着眼睛时松了一口气。"
    scene img_main24_525 with dissolve
    MC "靠，你今天真主动啊，姑娘。"
    Taka "啊……"
    scene img_main24_526 with dissolve
    "你把她推回墙上。"
    scene img_main24_527 with dissolve
    MC "我倒想知道，你到底有多主动？"
    scene img_main24_528 with dissolve
    Taka "啊……我、我……"
    "她感到难堪，不知道该怎么回答。"
    MC "你想当我的小骚货吗？"
    scene img_main24_529 with dissolve
    Taka "是的……"
    scene img_main24_530 with dissolve
    MC "你想像乖小骚货那样用嘴侍奉我吗？"
    Taka "是、是的……"
    scene img_main24_532 with dissolve
    MC "乖女孩。"
    scene img_main24_533 with dissolve
    Taka "啊唔嗯……"
    scene img_main24_534 with dissolve
    pause
    scene img_main24_535 with dissolve
    "过了一会儿，你把拇指从她嘴里抽出来，用舌头在一个深吻中取代了它。"
    Taka "唔嗯……"
    scene img_main24_536 with dissolve
    "..."
    scene img_main24_537 with dissolve
    "......"
    scene img_main24_538 with dissolve
    "........."
    scene img_main24_539 with fade
    "在一番长时间的揉捏和热吻之后，你放开她，退后一步。"
    scene img_main24_540 with dissolve
    MC "好了姑娘。脱给我看。"
    scene img_main24_541 with dissolve
    Taka "脱、脱衣……？"
    MC "对。连裤袜和内裤可以留着，但其他的我不想看到。"
    scene img_main24_542 with dissolve
    MC "我要坐着欣赏。"
    scene img_main24_543 with dissolve
    "突然失去了你引导的双手，她似乎完全不知道该把自己放在哪里，开始显得有些慌乱。"
    scene img_main24_544 with dissolve
    Taka "这、这太羞人了……"
    MC "你觉得骚货会在自己的男人面前因为露出身体而害羞吗？"
    Taka "不、不会……"
    scene img_main24_545 with dissolve
    "你觉得对她可能有点太快了，于是站起身来重新掌控局面。"
    MC "没关系。我先帮你一把，等你习惯了再说。"
    Taka "好、好的……"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main24_546 with dissolve
    pause
    scene img_main24_547 with dissolve
    "你伸手解开她的丝带，脱下她衬衫的扣子，露出下面那件淡粉色的内衣。"
    scene img_main24_548 with dissolve
    MC "一步一步来。把衬衫脱掉。"
    scene img_main24_549 with dissolve
    Taka "好的……"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main24_550 with dissolve
    "她按吩咐脱掉已经松开的上衣，然后紧张地站着等待。"
    scene img_main24_551 with dissolve
    pause
    scene img_main24_552 with dissolve
    pause
    scene img_main24_550 with dissolve
    MC "接下来是裙子，递给我。"
    Taka "好、好的……"
    scene img_main24_553 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main24_554 with dissolve
    pause
    scene img_main24_555 with dissolve
    pause
    scene img_main24_556 with dissolve
    "按吩咐，她脱下裙子递给你，你随手把它叠在她丢在一边的上衣上，眼睛始终没有离开她。"
    scene img_main24_557 with dissolve
    MC "乖女孩。"
    scene img_main24_558 with dissolve
    pause
    scene img_main24_559 with dissolve
    "你把她拉近，她被这突如其来的接触弄得抽了口气，巨大的双乳挤压在你的胸口上。"
    scene img_main24_560 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 2.0

    scene img_main24_561 with dissolve
    "你伸手上去解开她的内衣扣，她顺从地张开双臂，让你把肩带从肩上褪下。"
    scene img_main24_562 with dissolve
    pause
    scene img_main24_563 with dissolve
    MC "站直，手放到背后。"
    scene img_main24_564 with dissolve
    Taka "好、好的……"
    scene img_main24_565 with dissolve
    pause
    scene img_main24_566 with dissolve
    MC "你的身材他妈的真性感，姑娘。"
    scene img_main24_567 with dissolve
    Taka "啊……"
    scene img_main24_568 with dissolve
    Taka "谢、谢谢您，老师……"
    scene img_main24_569 with dissolve
    pause
    scene img_main24_570 with dissolve
    "你把她拉进另一个揉捏式的吻，故意比原本打算的节奏慢一些，努力让她习惯这一切。"
    scene img_main24_571 with dissolve
    "..."
    scene img_main24_572 with dissolve
    "......"
    scene img_main24_573 with dissolve
    "........."
    scene img_main24_574 with dissolve
    MC "好了姑娘，觉得自己准备好应付人生第一根鸡巴了吗？"
    scene img_main24_575 with dissolve
    Taka "我、我……"
    "她的声音卡在喉咙里，但还是坚定地点了点头。"
    MC "乖女孩。"
    scene img_main24_576 with dissolve
    MC "过来。我们先用你的手，我会引导你。"
    scene img_main24_577 with dissolve
    Taka "好……"
    scene img_main24_578 with dissolve
    "你让她坐下，低头看着她害羞天真的表情，忍不住对接下来的事感到有点兴奋。"

    play sound "audio/sounds/zipper.mp3" volume 2.0

    scene img_main24_579 with dissolve
    "听到你拉开拉链的声音，她微微绷紧了身体……"
    scene img_main24_580 with dissolve
    "你抬眼发现她正屏息等待你的下一道命令。"
    MC "把手举起来。"
    scene img_main24_581 with dissolve
    "她照做后，你引导着她的双手摸到你的鸡巴上。"
    scene img_main24_582 with dissolve
    MC "先只是摸摸。熟悉一下手感。"
    "她一开始只是用最轻的力道、只用指尖试探性地四处摸索。"
    scene img_main24_583 with dissolve
    "等她摸清了感觉，她开始更主动地握一些，虽然仍然只是用手指。"
    scene img_main24_584 with dissolve
    Taka "哦！……好硬……"
    MC "你根本想象不到。真想好好感受的话，就用整只手试试。"
    scene img_main24_585 with dissolve
    "她按吩咐，温柔地用手掌包住你的柱身。"
    Taka "啊……"
    scene vid_main24_1 with dissolve
    "她另一只手也立刻跟上，开始缓慢地上下撸动——不用教，她显然已经明白了基本动作。"
    scene vid_main24_2 with dissolve
    MC "乖女孩，感觉太棒了。你是天生的。"
    Taka "嘿嘿，真、真的吗……我不觉得……这点程度应该很简单才对……"
    scene vid_main24_3 with dissolve
    MC "那就快一点，让我看看你有多想改变。证明你真的想当我的骚货。"
    Taka "啊……好、好的……"
    scene img_main24_586 with dissolve
    "你本想让她手撸得更快，但她却俯下身张开了嘴。"
    Taka "啊唔嗯嗯嗯……"
    scene img_main24_587 with dissolve
    "她用湿润的嘴裹住你的龟头，先给了你一点口交天赋的暗示——而你打算把这天赋彻底开发出来。"
    scene img_main24_588 with dissolve
    "但接着她又退开了一点。"
    Taka "啊……好、好大……"
    MC "对。"
    scene img_main24_587 with dissolve
    "她点点头，然后张开嘴，再试一次。"
    scene img_main24_589 with dissolve
    Taka "啊唔嗯……"
    scene img_main24_590 with dissolve
    MC "乖女孩。现在不需要含太深，用嘴和舌头就行。"
    Taka "啊唔嗯——唔嗯。"
    scene img_main24_591 with dissolve
    Taka "唔嗯……"
    scene img_main24_592 with dissolve
    "她用丝滑湿润、满是唾液的嘴舔弄吸吮你的龟头，放电般的冲动烟花穿过你每一个神经末梢。"
    scene img_main24_593 with dissolve
    Taka "唔唔嗯嗯……"
    scene img_main24_592 with dissolve
    pause
    scene img_main24_593 with dissolve
    pause
    scene img_main24_592 with dissolve
    pause
    scene img_main24_593 with dissolve
    pause
    scene img_main24_592 with dissolve
    pause
    scene img_main24_593 with dissolve
    MC "好了，把手放在腿上。现在我要你只用嘴，像个乖骚货一样侍奉我。"
    scene vid_main24_5 with dissolve
    Taka "唔嗯……"
    scene vid_main24_4 with dissolve
    Taka "唔嗯……唔嗯嗯嗯……唔嗯嗯嗯……"
    scene vid_main24_6 with dissolve
    pause
    scene vid_main24_7 with dissolve
    Taka "唔嗯嗯嗯……唔嗯嗯嗯……"
    MC "我他妈……感觉好极了，姑娘……"
    scene vid_main24_8 with dissolve
    Taka "唔嗯……"
    "她的嘴还在沿你的柱身上下滑动，你却能感觉到你的快感让她在微笑。"
    MC "你喜欢这样吗？喜欢用自己的身体让你的男人舒服吗？"
    Taka "唔嗯嗯嗯……"

    play sound "audio/sounds/door.mp3" volume 2.0

    scene img_main24_594 with hpunch
    "就在这时，身后开门的声音让你们俩同时一颤，幸福美满的一刻被打碎了。"
    scene img_main24_595 with dissolve
    "至少三个男人的喧闹谈话声充满这间小洗手间，她看起来完全慌了神。"
    scene img_main24_596 with dissolve
    "她立刻的反应当然是想要退开……但你比她快得多。"
    scene img_main24_597 with dissolve
    "你的手猛地伸上去按住她的头，让她保持在原位。"
    scene img_main24_598 with dissolve
    MC "{i}*低语{/i}继续吸，姑娘。"
    scene img_main24_599 with dissolve
    "她没有再试图退开，但那些男人的声音让她整个人僵住了。"

    "你几乎忍不住想用手鼓励她，但你真的不想把她逼得太紧。"
    scene img_main24_600 with dissolve
    "相反，你紧张地沉默着，那些男人大声说笑、忙着自己的事。"
    "..."
    "......"

    play sound "audio/sounds/tap_loop.mp3" volume 0.4 loop fadein 1.0

    "最后其中一个人打开了水龙头，给了你更多一些掩饰的声响。"
    scene img_main24_598 with dissolve
    MC "{i}*低语{/i}吸吧，姑娘。"
    scene vid_main24_9 with dissolve
    "她几乎察觉不到地点了点头，开始轻轻吮吸，极力不发声，同时你温柔地把鸡巴在她嘴里进进出出。"
    "害羞的女孩在旁人近在咫尺的情况下侍奉你，那感觉压倒性地强烈，你发现自己几乎要和她一样努力才能保持安静。"
    scene vid_main24_10 with dissolve
    "..."
    "......"
    Taka "唔呃。"
    scene img_main24_601 with dissolve
    "你把鸡巴推得稍微深了一点，她不小心发出一声闷住的呻吟，你们俩都僵住了，心跳仿佛停止了一瞬……"
    scene img_main24_602 with dissolve
    pause
    "..."
    "......"
    "但那些男人没有任何反应，因为他们根本没听见。"
    scene img_main24_603 with dissolve
    MC "{i}*低语{/i}继续。"
    scene vid_main24_11 with dissolve
    "她犹豫了一下，但重新开始，更多地靠使用舌头来尽量保持安静。"
    scene vid_main24_12 with dissolve
    "..."
    "那些男人不紧不慢地闲聊着，你发现自己努力忍住非常艰难……"
    scene vid_main24_13 with dissolve
    MCi "（我他妈，快要爆了……他们最好快点他妈地走人！）"
    "......"

    play sound "audio/sounds/tap_end.mp3" volume 0.4

    "水龙头的声音终于停了……"
    
    play sound "audio/sounds/door.mp3"

    "片刻之后关门的声音传来，你们俩陷入一阵突然的紧张沉默。"
    "..."
    "你们俩安静了很久，想到差点被发现，心跳如擂鼓……"
    MC "{i}*低语{/i}现在，姑娘……结束吧。"
    scene vid_main24_14 with dissolve
    "..."
    "在长时间的紧张浅尝之后，她的吸吮变得难以忍受，你只能再忍一小会儿……"
    MC "操，我要射了。"
    scene vid_main24_15 with dissolve
    Taka "唔嗯？！"
    scene vid_main24_16 with flash
    "你把她的头稍稍往前拉，开始把精液射进她喉咙深处。"
    MC "操！咽下去，姑娘！"
    "你闭上眼睛，在她湿润吸吮的嘴里高潮，脑海有一瞬间彻底空白。"
    Taka "唔唔嗯！"
    scene img_main24_604 with dissolve
    "你仍按着她的头，闭上眼睛稍稍前倾，花了一点时间从剧烈的释放中恢复。"
    scene img_main24_605 with dissolve
    Taka "唔唔嗯嗯……"
    scene img_main24_606 with dissolve
    "最后，你长长吐出一口憋着的气，浑身的紧张都随之流走，把鸡巴从她湿淋淋的嘴里抽出来，退后站起。"
    scene img_main24_607 with dissolve
    Taka "啊……"
    scene img_main24_608 with dissolve
    "你一松手，姑娘就深深吸气想缓过来，随即开始咳嗽，差点把一肺的精液吸进去。"
    scene img_main24_609 with dissolve
    MC "全咽下去。别吐出来。"
    scene img_main24_610 with dissolve
    "她的手猛地伸到嘴边，但她还是照你的指示做了，经过一番明显的吞咽努力后，她放松下来。"
    scene img_main24_611 with dissolve
    Taka "啊啊啊嗯……"
    scene img_main24_612 with dissolve
    MC "非常好，姑娘。你做得太棒了。"

    $ renpy.end_replay()

######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
label replay_akatsuki7:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/akatsuki_theme.mp3" loop fadeout 1.0 fadein 1.0

    "你还没睁开眼，就感觉脸上开始绽开笑容——晓月的小手正温柔地上下撸弄你清晨的勃起。"
    scene img_main26_1 with dissolve
    MC "早安，小猫。"
    scene img_main26_2 with dissolve
    Akatsuki "唔嗯，早。"
    scene img_main26_3 with dissolve
    "她继续柔软而不急不缓地撸动，让你彻底清醒过来……"
    scene img_main26_4 with dissolve
    "..."
    scene img_main26_5 with dissolve
    MC "该洗澡了？"
    scene img_main26_6 with dissolve
    Akatsuki "唔嗯。"

    play sound "audio/sounds/bed.mp3" volume 4.0

    scene img_main26_7 with dissolve
    "你爬下床，一把抱起晓月，不让她起身跟来。"

    scene img_main26_8 with dissolve
    pause

    scene img_main26_9 with dissolve
    Akatsuki "{i}*低语{/i}唔嗯嗯……"
    "她在你耳边发出柔软低沉的满足哼声，这是你听过的最接近真正呼噜声的声音，再次说明她有多喜欢被你抱起来。"
    
    play sound "audio/sounds/door.mp3"

    scene img_main26_10 with dissolve
    pause
    
    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main26_11 with dissolve
    pause
    
    scene img_main26_12 with dissolve
    "在洗手间里，你把她放下片刻好脱掉内裤，然后再次抱起她走进淋浴间。"
    scene img_main26_13 with dissolve
    "但你在迈进去之前停住了。"
    MC "抱歉你搬进来之后我们都没怎么单独相处。我对此有点愧疚。"
    scene img_main26_14 with dissolve
    "她的表情一如既往地难以解读，但你猜她有点惊讶，随后她笑着摇了摇头。"
    MC "这周末就我们两个出去约会，你觉得怎么样？"
    scene img_main26_15 with dissolve
    Akatsuki "唔嗯！好啊！"
    "她的回答立刻脱口而出，充满了你从这个面无表情的女孩身上听过的最大程度的兴奋。"
    MC "唔嗯，我很喜欢看你那个笑容。"
    scene img_main26_16 with dissolve
    Akatsuki "唔嗯……"
    MC "那就周六晚上。咖啡馆关门之后，我们出去逛逛。"
    scene img_main26_17 with dissolve
    Akatsuki "我也有个惊喜给你……和莎拉一起……到那时应该就准备好了。"
    "有那么一刻，你脑海中关于这短短一句话里可能包含的可能性疯狂驰骋。"
    MC "靠，小猫，你不能这样突然扔个炸弹过来。现在我等不到周六了……"
    scene img_main26_18 with dissolve
    Akatsuki "唔嗯。我也是……"

    play ambiance "audio/sounds/shower.mp3" fadein 1.0 volume 0.2 loop

    scene vid_main26_1 with dissolve
    "你抱着她走进淋浴间把她放下，她立刻热情地把你拉低，给了你一个深吻。"
    Akatsuki "唔嗯……"
    scene vid_main26_2 with dissolve
    "没等她把这个吻变成你们惯常的清晨口交，你把手往下滑，开始揉弄她的小穴。"
    Akatsuki "唔唔嗯嗯……"
    scene vid_main26_3 with dissolve
    "你没有中断这个吻，手再往下滑了一点，把手指推进她紧致而接纳的小洞。"
    Akatsuki "唔唔嗯嗯嗯！"
    "和往常一样，你看得出要让这只淫荡的小猫娘高潮并不需要多少……"
    scene img_main26_19 with dissolve
    "但出乎你意料的是，她中断了吻，退开了一点。"
    scene img_main26_20 with dissolve
    Akatsuki "我等不到周六了……"
    MC "对，你刚才不是说过了吗？"
    scene img_main26_21 with dissolve
    Akatsuki "不……我是说……我想再做一次。现在。"
    scene img_main26_22 with dissolve
    Akatsuki "求你了？"
    "她仰起头望着你，那双又大又天真的眼睛融化了你的心。但即使没有这个眼神，你也不可能拒绝她这样的请求。"

    scene img_main26_23 with dissolve
    "你又一次把她抱起，她本能地用手臂和腿缠住你，她那矫健的小身体完全能帮着分担自己的重量。"

    scene vid_main26_4 with dissolve
    "还没开始，你硬如石头的鸡巴就搁在她的两瓣屁股之间，她不耐烦地前后摇着胯磨蹭它。"
    scene vid_main26_5 with dissolve
    Akatsuki "唔嗯……"
    MC "准备好了吗，小猫？可能还是会疼。"
    Akatsuki "唔嗯。我能做到。"
    MC "乖女孩。"

    scene vid_main26_6 with dissolve    
    "二话不说，你把鸡巴前端抵在她温暖湿润的小洞上，她抬起胯、微微弓起背，好让它滑进去。"
    Akatsuki "啊唔嗯嗯嗯！！"
    scene vid_main26_7 with dissolve    
    "她叫出声来抱住你，紧贴着你的胸膛，而你的鸡巴缓缓滑入她那紧得惊人的小穴，把她完全劈开。"
    Akatsuki "唔嗯嗯……"
    scene vid_main26_8 with dissolve    
    "就在你想着要不要给她一点时间适应时……"
    scene vid_main26_9 with dissolve    
    "她往后靠进你的眼睛里，完全坐在你的柱身上，用细小的动作前后摇着。"
    scene vid_main26_10 with dissolve  
    Akatsuki "很疼……但我好喜欢！"
    MC "那就看你怎么处理这个了。"
    scene vid_main26_11 with dissolve
    "你稍稍后靠换个更好的角度，开始缓缓向上挺送进这只小小的猫娘体内。"
    Akatsuki "唔唔嗯嗯嗯……唔嗯嗯……唔唔嗯嗯嗯……"
    scene vid_main26_12 with dissolve
    pause
    "每次深深推进她体内，都会引出一小声愉悦的呻吟，这满足你的程度几乎不亚于她紧致的肉褶裹住你鸡巴时拉伸的感觉。"
    scene vid_main26_13 with dissolve
    "你完全沉浸在当下，彻底忘了自己保持这个缓慢节奏多久了……"
    scene vid_main26_14 with dissolve
    "..."
    "......"
    scene vid_main26_11 with dissolve
    "........."
    scene vid_main26_15 with dissolve
    "但最终你感觉到晓月变得有些急切，她开始扶着你的肩膀更用力地上下起伏……"
    Akatsuki "唔唔嗯！！……唔嗯嗯唔！"
    "过了一会儿，你意识到为什么……"
    scene vid_main26_16 with dissolve
    Akatsuki "我、唔唔嗯嗯嗯……我……"
    scene vid_main26_17 with dissolve
    "突然，她猛地把自己坐到底，尽可能深地把你的鸡巴吞进去，小穴在高潮的席卷中紧紧收缩。"
    Akatsuki "唔唔唔唔唔唔嗯嗯嗯！！！"
    "通过鸡巴，你能感觉到她高潮时每一丝细微的痉挛，她的肌肉在你身上痉挛性地收紧……"
    "她在你怀里体验到这样的快感，是能想象到的最有满足感的体验之一。"
    "..."
    scene vid_main26_18 with dissolve
    "最后，当余韵开始消退，她瘫软地伏在你身上，喘息沉重。"
    Akatsuki "唔嗯嗯……"
    MC "靠，你真的很容易高潮啊，小猫。"
    Akatsuki "唔嗯……"
    MC "{i}*低语{/i}但还没完。"
    scene vid_main26_19 with dissolve
    "你开始缓缓在她仍在恢复的身体里进出，又从这个疲惫的女孩嘴里引出一声愉悦的呻吟。"
    Akatsuki "唔唔嗯嗯嗯！"
    scene vid_main26_20 with dissolve
    MC "现在问这个可能有点晚了，但射在里面安全吗？"
    Akatsuki "啊，嗯嗯嗯嗯……"
    scene vid_main26_21 with dissolve
    Akatsuki "我唔嗯嗯……在吃避孕药嗯嗯……薇琪的爸爸唔嗯嗯……"
    MC "太好了……"
    scene vid_main26_22 with dissolve
    pause
    "你开始更快地向上挺送，双手借力扶着她的胯，而她也开始配合，循着你的节奏摆动。"
    MC "所以你想让我射进你紧致的小身体里？"
    Akatsuki "唔嗯嗯……"
    scene vid_main26_23 with dissolve
    MC "操……说话，小猫……说出来。"
    "你看得出，尽管其他事情都在发生，光是要开口说话就把她害羞的一面引了出来。"
    Akatsuki "唔嗯我、我……我想让你射进我体内啊啊啊……拜、拜托……"
    MC "操……"
    Akatsuki "唔嗯嗯嗯……我、我……"
    scene vid_main26_24 with dissolve
    "你怀疑她只是想让你的注意力从逼她说话上移开，但她突然加快了速度……"
    scene vid_main26_25 with dissolve
    pause
    "而这完全奏效了。她温暖饥渴的小穴夺走了你思考的能力，催促你快点填满她的子宫。"
    "..."
    "......"
    "........."
    Akatsuki "唔嗯……我、我……哦啊啊唔嗯……"
    scene vid_main26_26 with dissolve
    "你的脑海彻底空白，无力处理晓月想说的话，肌肉全都收紧，一股股精液射进她紧致痉挛的体内。"
    Akatsuki "唔唔唔唔唔唔唔唔唔！！！"
    scene vid_main26_27 with dissolve
    "过了好一会儿，这句话才穿透你迷雾般的脑海，你意识到晓月正在经历又一次高潮，而她的身体贪婪地吸收着你的种子……"
    "....."
    Akatsuki "唔唔唔唔嗯嗯！！"
    MC "操……"

    scene img_main26_24 with dissolve
    "举了她这么久，手臂和腿都想休息了，你瘫坐到淋浴间的地上，靠着墙，晓月仍坐在你身上。"

    $ renpy.end_replay()



######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
label replay_group3:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/night.mp3" loop fadeout 1.0 fadein 1.0

    scene img_main26_1346 with dissolve
    "你坐在床上，被两个急不可耐的女孩夹在中间，看着她们接下来要做什么。"
    scene img_main26_1347 with dissolve
    "她们俩都开始故意做作地脱起衣服……"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main26_1348 with dissolve
    pause
    scene img_main26_1349 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main26_1350 with dissolve
    pause
    scene img_main26_1351 with dissolve
    pause

    scene img_main26_1352 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main26_1353 with dissolve
    pause
    scene img_main26_1354 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main26_1355 with dissolve
    pause

    scene img_main26_1356 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main26_1357 with dissolve
    pause
    scene img_main26_1358 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main26_1359 with dissolve
    pause

    scene img_main26_1360 with dissolve
    "过了一会儿你才意识到这全是她们计划的一部分——就在你开始勃起的瞬间，薇琪爬到你两腿之间，把你的鸡巴掏了出来。"
    scene img_main26_1361 with dissolve
    Victoria "好了主人，我先来。你放松就好……"
    scene vid_main26_28 with dissolve
    "她用温暖柔软的手牢牢握住你的鸡巴，另一只手则开始温柔地揉弄前端……"
    "感觉是不错……但在一场让你射出来的比赛里，这并不是你原本期待的做法。"
    MC "你确定你想赢这场比赛吗，薇琪？"
    scene vid_main26_29 with dissolve
    Victoria "这叫策略，主人。"
    Victoria "你不会这么快就射，所以我没必要给你做太多前戏，好让别人来完成最后一击……"
    MC "有道理。"
    Victoria "没错，所以你就躺好享受吧。"
    scene vid_main26_30 with dissolve
    "你决定照做，往床头板上一靠，任由薇琪悠闲地撸动你神经密布的龟头……"
    scene vid_main26_31 with dissolve
    "..."
    scene vid_main26_32 with dissolve
    "......"
    scene vid_main26_33 with dissolve
    MC "你看起来还是有点不好意思啊，露西。"
    scene vid_main26_34 with dissolve
    Lucy "啊，唔嗯……我不知道自己能不能完全习惯这个……"
    Victoria "我以为你喜欢看呢？"
    scene vid_main26_35 with dissolve
    Lucy "啊……我、我……"
    "她整个人缩了起来，害羞至极地移开视线……"
    Lucy "{i}*轻声地{/i}我、我，呃……{i}*非常轻声地{/i}口、口交比较……"
    Victoria "哦真的吗？有意思。你真是充满惊喜。"
    scene vid_main26_36 with dissolve
    Akatsuki "轮到我了。"
    scene vid_main26_37 with dissolve
    "薇琪往后挪了挪，让小猫娘接替她的位置……"
    "晓月从薇琪停下的地方接着来，用稍小一点的手慢慢上下套弄你的鸡巴。"
    scene vid_main26_38 with dissolve
    MC "你也是？我还以为你肯定会先用嘴呢。"
    scene vid_main26_39 with dissolve
    Akatsuki "唔嗯。策略。"
    Victoria "噗。学猫的小猫。"
    scene vid_main26_40 with dissolve
    "..."
    scene vid_main26_41 with dissolve
    "......"
    scene vid_main26_42 with dissolve
    "终于轮到露西，她也照做一模一样，给你一场缓慢而温柔的手淫。"
    scene vid_main26_43 with dissolve
    "只是略有不同的是，她偶尔鼓起勇气时，会花上几秒带着爱意微笑着看进你的眼睛。"
    scene vid_main26_44 with dissolve
    "..."
    "......"
    "........."
    scene img_main26_1362 with dissolve
    Victoria "好了，又轮到我了！"
    scene img_main26_1363 with dissolve
    Victoria "该再提升一个档次了。"
    MC "哈，终于。"
    scene img_main26_1364 with dissolve
    Victoria "哎，你不喜欢我们的手活吗？"
    MC "我还挺喜欢的……但它主要只是让我更想要更多。你们要是再这么弄下去，我可能会扑到你们其中一个身上，管它什么比赛不比赛的……"
    Victoria "好了，现在我想试点新东西……"
    scene img_main26_1365 with dissolve
    Victoria "就照着这个来模仿吧，小猫。"

#Titjob - Vicky (add renders and dialogue at start with Vicky getting MC in position)
    scene img_main26_1366 with dissolve
    Victoria "好了，主人。请躺下，把腿搭在我腿上。"

    scene img_main26_1367 with dissolve
    pause

    scene img_main26_1367 with dissolve
    MC "像这样吗？"
    scene img_main26_1369 with dissolve
    Victoria "对！"
    scene img_main26_1370 with dissolve
    "等你摆好姿势，她俯身向前，把你的鸡巴夹在她硕大坚挺的双乳之间……"
    scene vid_main26_45 with dissolve
    "然后开始上下起伏……"
    scene vid_main26_46 with dissolve
    "..."
    scene vid_main26_47 with dissolve
    Lucy "啊……我、我压根没想过还能这样……"
    scene vid_main26_48 with dissolve
    Victoria "你的比我的还大呢，露西。你完全能轻松做到……"
    Lucy "我、我……这样不羞人吗？"
    Victoria "为什么？这里只有我们。"
    Lucy "我、我想也是……"
    scene vid_main26_49 with dissolve
    "薇琪回过头，用她挑衅的笑容低头看着你？"
    Victoria "怎么样，主人？"
    MC "唔嗯……"
    scene vid_main26_50 with dissolve
    "你把注意力集中在鸡巴被她丰满的乳房上下推弄的触感上，还有她柔软的皮肤摩擦着你皮肤的感受……"
    MC "挺舒服的……你这样大概就能让我射出来……"
    MC "不过我更想要你的嘴。"
    scene vid_main26_51 with dissolve
    Victoria "哈，这倒不意外……不过，我觉得你还没准备好到那一步……"
    scene vid_main26_52 with dissolve
    "..."
    "......"
    scene img_main26_1371 with dissolve
    "薇琪又用胸部按摩了你一会儿的柱身，最后晓月拍了拍她的肩。"
    scene img_main26_1372 with dissolve
    "你坐起身，看着这些美丽的裸体女孩在床上互相爬上对方的身体。"

    scene img_main26_1373 with dissolve
    pause

    scene img_main26_1374 with dissolve
    Akatsuki "轮到我了。"
    scene img_main26_1375 with dissolve
    Akatsuki "哦唔嗯……"
    scene vid_main26_53 with dissolve
    Akatsuki "唔嗯……"
    "晓月没有上薇琪的钩子去尝试乳交，而是直接使出她的看家本领……"
    scene vid_main26_54 with dissolve
    Akatsuki "唔嗯嗯嗯嗯……"
    "她的嘴上下侍弄时裹在你鸡巴上的温暖和唾液，与刚才的乳交形成了愉快的对比……"
    "你终于感觉是被满足了，而不只是被吊着……"
    scene vid_main26_55 with dissolve
    Akatsuki "唔嗯嗯嗯……唔嗯嗯嗯嗯……"
    "和往常一样，晓月的嘴表现极其出色，从她把你含进含出时柔软低沉的呻吟声中，就能听出她有多享受……"
    scene vid_main26_56 with dissolve
    Akatsuki "唔嗯嗯嗯……"

    scene img_black with fade
    "你闭上眼睛，把头向后仰，任由她的嘴把你送进一个充满幸福与快感的世界……"
    "..."
    "......"
    "她那有节奏的、丝滑湿润的吸吮夺走了你所有思绪，让你完全失去了对时间的感知，直到……"
    Lucy "呃……"
    scene vid_main26_57 with dissolve
    "你睁开眼，看见露西一半躲避着视线，一半注视着完全沉醉在为你口交中的猫娘……"
    Lucy "轮、轮到我了……"
    scene img_main26_1376 with dissolve
    Akatsuki "唔嗯。"
    MCi "（要是再让晓月继续下去，奖品就被她拿走了。）"
    scene img_main26_1377 with dissolve
    Lucy "呃、呃……"
    "出人意料的是，露西没有马上开始，而是转向另外两个女孩，艰难地想把她要说的话挤出来……"
    scene img_main26_1378 with dissolve
    Lucy "别、别太看……"
    scene img_main26_1379 with dissolve
    Victoria "抱歉了，露西。我可不敢保证。"
    scene img_main26_1380 with dissolve
    Akatsuki "唔嗯。"
    Lucy "啊……"
    scene img_main26_1381 with dissolve
    "她看起来羞愧难当，却同样坚定地挪近，拉了拉你的手臂。"
    scene img_main26_1382 with dissolve
    "你猜她是想让你躺下……"
    scene img_main26_1383 with dissolve
    "而当你照做时，她并没有像你预料的那样模仿晓月……"
    scene img_main26_1384 with dissolve
    "她一手握住你的鸡巴，跨坐在你身上。"
    scene img_main26_1385 with dissolve
    Victoria "靠，露西。你今晚真是大胆啊……"

    scene img_main26_1386 with dissolve
    pause

    scene img_main26_1387 with dissolve
    "露西无视了你，退回她自己那点小羞耻的泡泡里，用你涨硬的龟头在她湿漉漉的穴口上下蹭了几下……"
    scene img_main26_1388 with dissolve
    "然后缓缓地沿你的柱身坐下去，把它完全吞进她火热、湿润、紧夹的小穴里……"
    scene img_main26_1389 with dissolve
    Lucy "唔唔嗯嗯嗯嗯嗯！"
    Lucy "啊、啊……呃……"
    scene vid_main26_58 with dissolve
    "她闭上眼睛，不敢看你们任何一个，开始上下起伏……"
    Lucy "唔嗯嗯……唔嗯嗯嗯……"
    MC "操……"
    scene vid_main26_59 with dissolve
    Victoria "啊不……我都能从你声音里听出来了……等一下，主人！下一个是我！"
    scene vid_main26_60 with vpunch
    Lucy "不、不！"
    "露西突然睁开眼，一边继续骑着你，一边用炽热的目光低头看进你的眼睛……"
    Lucy "拜、拜托，[PlayerName]……求你了唔嗯……射进我体内……"
    scene vid_main26_61 with dissolve
    Lucy "唔嗯嗯嗯……我、我……"
    scene vid_main26_62 with dissolve
    "她似乎突然下定了决心，然后……"
    scene vid_main26_63 with dissolve
    "她把速度翻了一倍，在另外两个女孩面前毫不知耻地骑着你。"
    Lucy "唔嗯嗯……我、我需要……再把我填满……"
    "......"
    "........."

    scene img_black with fade

    "你闭上眼睛向后躺下，拼尽全力忍住不射，任凭露西用她那火辣的小身体试图把你榨干……"
    Lucy "唔嗯嗯嗯……"
    Lucy "{i}*低语{/i}请为我射出来，[PlayerName]。"
    "..."
    "......"
    "你完全搞不清这持续了多久……"
    "就在你以为已经到了极限、正要伸手把露西的胯拉下来射进她火热收紧的体内时……"
    "她突然退开，冰凉的空气打在你脉动、沾满液体的大鸡巴上……"
    Lucy "啊……"
    scene img_main26_1390 with dissolve
    pause
    scene img_main26_1391 with dissolve
    "你睁开眼，长长地吐出一口憋着的气……"
    scene img_main26_1392 with dissolve
    "只看见露西害羞地朝你笑着，她的回合已经过去了。"
    scene img_main26_1393 with dissolve
    MC "操，刚才太舒服了，露西。"
    Lucy "嘿嘿……"
    scene img_main26_1394 with dissolve
    Victoria "嗯……刚才热得要命……"
    scene img_main26_1395 with dissolve
    Akatsuki "唔嗯……"
    scene img_main26_1396 with dissolve
    Lucy "啊……"
    "露西突然想起自己一直在被人看着，又一次变得非常难为情……"
    scene img_main26_1397 with dissolve
    "但随着薇琪开始她的回合，她很快就不再是焦点了。"
    Victoria "这个是我的……"
    scene img_main26_1398 with dissolve
    "她学着露西的做法，只是反了过来——薇琪跨坐在你身上，让你对准她自己湿淋淋的小穴……"
    scene vid_main26_64 with dissolve
    "她没有露西那么小心，一下子坐下去，一气呵成地把你吞进她紧致的小洞里……"
    Victoria "唔唔嗯！操！……"
    scene img_main26_1399 with dissolve
    Victoria "啊唔嗯……啊啊啊……"
    scene img_main26_1400 with dissolve
    "她有些挣扎，你仰头朝她笑了笑，对她进入时依然感受到的痛苦与快感的混合略感满意。"
    Victoria "唔嗯嗯嗯……它在里面总感觉大那么多……"
    scene vid_main26_65 with dissolve
    "尽管还痛着，她没过多久就开始上下起伏，扭着腰把你推向高潮……"
    Victoria "唔嗯嗯……就是这样，唔嗯——主人……"
    scene vid_main26_66 with dissolve
    Victoria "唔嗯……操……就是这样……射进我体内……"
    Victoria "你、你知道我的身体完全是你的唔嗯嗯……"
    scene vid_main26_67 with dissolve
    Victoria "唔嗯我紧致的小穴……我的子宫唔嗯嗯嗯嗯……"
    scene img_black with fade
    "你把眼睛闭紧，试图尽量多撑一会儿……"
    Victoria "唔嗯……不错的尝试唔嗯……但我感觉它要来了……"
    scene vid_main26_68 with fade
    "你意识到她说得没错，于是放弃抵抗，放松身体，迎接那顺着脊背和鸡巴跳动、不断累积的感觉……"
    scene vid_main26_69 with flash
    "片刻之后，它累积成无法阻挡的压力，你最后一次狠狠向上顶进她体内……"
    Victoria "唔唔嗯唔唔嗯唔唔！！是的是的！！"
    "你射进她的子宫，一股股精液在她体内深处反复喷射，同时你全身的每一块肌肉都绷紧了……"
    "..."
    "......"
    scene img_main26_1401 with dissolve
    "最后，那压倒性的感觉消退，你瘫回床上，彻底精疲力尽。"
    scene img_main26_1402 with dissolve
    MC "哈啊啊……真舒服……"
    scene img_main26_1403 with dissolve
    "薇琪转过身趴在你胸口上抱住你，小心不让你的鸡巴从灌满精液的小穴里滑出来。"
    Victoria "唔嗯……唔嗯嗯……谢谢你，主人。"
    scene img_main26_1404 with dissolve
    MC "哈啊……对不起，露西……你差点就赢了……"
    scene img_main26_1405 with dissolve
    Lucy "唔嗯……你不用道歉！"
    scene img_main26_1406 with dissolve
    "过了一会儿，薇琪起身，从你渐渐软下的鸡巴上脱离，脸上挂着调皮的笑容。"
    scene img_main26_1407 with dissolve
    Victoria "下一个轮到你了，小猫。看来收拾残局的活儿归你了。"
    scene img_main26_1408 with dissolve
    Akatsuki "唔嗯……"
    "晓月歪着头，看着你那根沾满精液和爱液的大鸡巴，然后点了点头……"
    scene img_main26_1409 with dissolve
    Akatsuki "哦唔嗯嗯嗯……"
    "她开始吮吸你仍然极度敏感的鸡巴，温柔地清理这场比赛留下的痕迹……"
    scene img_main26_1410 with dissolve
    Lucy "晓、晓月！"
    Victoria "唔嗯，上面会有一些{i}你的{/i}味道哦，露西……"
    scene img_main26_1411 with dissolve
    Lucy "哦——天啊……"
    scene img_main26_1412 with dissolve
    "看来这连想看的欲望都让她受不了了，露西把脸埋进你旁边的枕头里……"
    scene img_black with fade
    "你闭上眼睛，在高潮后温暖的光晕中放松，任由晓月温柔地把你舔干净……"

    $ renpy.end_replay()


#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_akatsuki8:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/akatsuki_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
    
    scene img_main27_600 with dissolve
    MCi "（哟，这是怎么回事？）"
    scene img_main27_601 with dissolve
    MC "嘿。怎么了，小猫？"
    scene img_main27_602 with dissolve
    "她小跑到你身边，绕过桌子，然后摆出姿势展示她的装扮。"

    scene img_main27_603 with dissolve
    pause
    scene img_main27_604 with dissolve
    pause
    scene img_main27_605 with dissolve
    pause
    
    scene img_main27_602 with dissolve
    MC "真火辣，小猫。我很喜欢。"
    scene img_main27_606 with dissolve
    Akatsuki "唔嗯。"

    scene img_main27_607 with dissolve
    pause

    scene img_main27_608 with dissolve
    "她转过身撅起屁股，强调了她真正想给你看的东西……"

    scene img_main27_609 with dissolve
    pause
    scene img_main27_610 with dissolve
    pause

    scene img_main27_611 with dissolve
    "你伸手摸向那条黑色猫尾……"
    scene img_main27_612 with dissolve
    "然后轻轻拽了一下……"
    scene img_main27_613 with dissolve
    Akatsuki "喵啊啊……"
    "她用可爱又撩人的语调「喵」了一声，让你清楚那条尾巴是怎么连在她身上的。"
    MC "你配上这条尾巴太完美了，小猫。你知道我现在绝不会让你把它取下来，对吧？"
    scene img_main27_614 with dissolve
    Akatsuki "唔嗯。"
    scene img_main27_615 with dissolve
    MC "过来……"
    scene img_main27_616 with dissolve
    "你轻轻拽着尾巴把她拉过来，她不得不倒退着挪步，好防止肛塞被扯出来。"
    scene img_main27_617 with dissolve
    Akatsuki "喵啊啊啊嗯……"
    MC "可惜营业时间你大概不该在厨房里戴着这个。"
    scene img_main27_618 with dissolve
    Akatsuki "唔嗯。莎拉给我做了一个，可以套在我——"
    scene img_main27_619 with dissolve
    Akatsuki "喵啊嗯嗯……"
    "你又拽了一下尾巴，刺激到她紧致的小菊花，她的话被打断了。"
    scene img_main27_620 with dissolve
    Akatsuki "我的腰……她想要我批准她做你的女朋友。"
    MC "哦，她真的这么要求了？"
    "她今天一整天的表现忽然在你脑中说得通了……"
    MC "让我猜猜，薇琪就是她一整天都怪怪的的原因？"
    scene img_main27_621 with dissolve
    Akatsuki "唔嗯。你洗澡的时候她们在聊天。"
    MC "我早该想到的。"
    scene img_main27_622 with dissolve
    Akatsuki "你该回去干活了。"
    "小猫娘这完全不合她性格的要求让你歪了歪头……"
    
    play sound "audio/sounds/clothing.mp3" volume 4.0
    
    scene img_main27_623 with dissolve
    "然后你饶有兴致地看着她开始脱衣服……"

    play sound "audio/sounds/clothing.mp3" volume 4.0
    
    scene img_main27_624 with dissolve
    MC "你在我旁边这样，我要很难集中精神做账了，小猫。"
    scene img_main27_625 with dissolve
    Akatsuki "唔嗯……"
    "她看起来有点不满，而你决定顺着演下去。"
    MC "但好吧，看来我得回去干活了。"
    scene img_main27_626 with dissolve
    Akatsuki "唔嗯！"
    scene img_main27_627 with dissolve
    "你把目光从她紧致的小身体上移开，勉强把注意力集中到面前的屏幕上……"
    scene img_main27_628 with dissolve
    "然而她钻到桌子底下时擦过你的腿，你的注意力立刻就动摇了。"
    scene img_main27_629 with dissolve
    MCi "（看来我是别想跟上办公进度了。）"
    scene img_main27_630 with dissolve
    "..."
    scene img_main27_631 with dissolve
    MC "好吧，小猫。我看明白你想干什么了。"
    MC "我可以让你给我口交。但我真的得专心工作，所以乖乖地、安静点。"
    scene img_main27_632 with dissolve
    Akatsuki "唔嗯！"
    scene img_main27_633 with dissolve
    "你说到做到，无视她，继续往电脑里敲数字，而她拉开你的裤链，把鸡巴掏了出来。"
    
    scene img_main27_634 with dissolve

    play sound "audio/sounds/zipper.mp3" volume 3.0

    "..."
    scene img_main27_635 with dissolve
    "她的手很快就让你硬了起来……"
    scene vid_main27_1 with dissolve
    "而你一硬起来，她就立刻用温暖湿润的双唇裹住你的龟头。"
    scene vid_main27_2 with dissolve
    "尽管她的猫耳已经开始在你余光里上下晃动，你还是坚持敲着数字。"
    scene vid_main27_3 with dissolve
    "你知道这是一场毫无胜算的战斗——她满是唾液的嘴沿你的鸡巴上下滑动，快感如丝带般在你脑海中飞驰……"
    scene vid_main27_4 with dissolve
    "但你不让注意力从屏幕上移开，让她每让你分心一秒都得费一番力气。"
    scene vid_main27_5 with dissolve
    "..."
    scene vid_main27_6 with dissolve
    "......"
    scene vid_main27_7 with dissolve
    "........."

    scene vid_main27_8 with dissolve
    pause

    play sound "audio/sounds/doorbell1.mp3" volume 0.7

    scene img_main27_636 with vpunch
    "{i}叮咚！{/i}"
    "前门的门铃让你有点意外，但你现在实在懒得去管。"
    scene img_main27_637 with dissolve
    MC "是露西来了，对吧？"
    Akatsuki "唔嗯。"
    MC "很好，那就别停。她自己会开门。"
    scene img_main27_638 with dissolve
    Akatsuki "唔嗯……"
    scene img_main27_639 with dissolve
    "你立刻把这事抛到脑后，开始输入下一张采购发票的明细，而晓月继续侍奉着你……"
    
    play sound "audio/sounds/door.mp3"
    
    scene img_main27_640 with dissolve
    "但你还没敲完，办公室的门就开了，你听见露西的声音在外面……"

    play music "audio/bgm/akatsuki_searching.mp3" loop volume 1.0 fadeout 1.0 fadein 1.0

    scene img_main27_641 with dissolve
    "接着进来两位女士。"
    MCi "（我他妈……）"
    scene img_main27_642 with dissolve
    Akari "哟，输家？"
    scene img_main27_643 with dissolve
    "听到明里的声音，桌子底下的晓月僵住了，你涨硬的龟头还含在她嘴里……"
    scene img_main27_644 with dissolve
    "于是你飞快地把椅子往前拉，把她更深地推到桌子底下。"

    scene img_main27_645 with dissolve
    pause

    scene img_main27_646 with dissolve
    MC "呃，喂。"
    scene img_main27_647 with dissolve
    Akari "哼，你这是怎么了？你平时不是见到我就很开心吗！"
    MC "噗。只在{i}你{/i}的想象里。"
    MC "总之，抱歉。我现在有点走神。"
    scene img_main27_648 with dissolve
    Akari "那就别走神了。"
    scene img_main27_649 with dissolve
    "站在明里身后的那位年长女士对女儿跟你说话的语气有些吃惊，轻声却清晰地说道。"
    AkaneUnknown "你应该对人家更有礼貌，明里。"
    scene img_main27_650 with dissolve
    Akari "不用，反正我的厨艺比他好……"
    scene img_main27_651 with dissolve
    Akari "对吧，大男孩？"
    scene img_main27_652 with dissolve
    "她朝你投去调侃的一瞥，让那位女士露出几分无奈的神情。"
    AkaneUnknown "{i}*叹气{/i}明里……"
    scene img_main27_653 with dissolve
    AkaneUnknown "她这样我真的很抱歉。你一定是弗莱彻先生吧。"
    Akane "我是茜，晓月的母亲。"
    scene img_main27_654 with dissolve
    Akari "喂，我也是哦！"
    scene img_main27_655 with dissolve
    Akane "啧。安静，小丫头。"
    MC "很高兴认识你。真的很抱歉，我现在没法站起来跟你打招呼；我刚才弄伤了背……"
    scene img_main27_656 with dissolve
    Akari "娇气。"
    scene img_main27_657 with dissolve
    "茜看起来恨不得掐死明里，但还是忍住了。"
    scene img_main27_658 with dissolve
    Akane "不不，别在意。是我们不打招呼就闯进来了；完全没关系。"
    MC "那么，我能帮您什么？晓月她……"
    "你在快要说出「晓月正在镇上发传单」时及时刹住了车……"
    MCi "（她们很可能在镇上见过那些姑娘。毕竟王家餐馆就在那附近……）"
    MC "……目前不在。"
    scene img_main27_659 with dissolve
    Akane "没关系。其实，弗莱彻先生——"
    MC "请叫我[PlayerName]就行。"
    scene img_main27_660 with dissolve
    Akane "当然，[PlayerName]……"
    scene img_main27_661 with dissolve
    Akane "呃，我知道这有点奇怪，毕竟您并不怎么了解我，但我想请您帮个忙。是关于晓月的。"
    MC "什么样的忙？"
    scene img_main27_662 with dissolve
    Akane "是关于她离开我们家、搬去和您一起住这件事……"
    MC "如果您的意思是把她要回去，那可不行。只要她愿意，这里永远有她的家。"
    scene img_main27_663 with dissolve
    "嘴还含着你的鸡巴的晓月听到这话，稍稍精神了起来。"
    scene img_main27_664 with dissolve
    Akane "不不……"
    scene img_main27_665 with dissolve
    Akane "首先，我想先为我丈夫和女儿们的所作所为道歉。明里已经告诉我一些细节了。"
    scene img_main27_666 with dissolve
    "茜第一次带着一丝真切的怒气看向她的女儿。"
    Akane "你也道歉。"
    scene img_main27_667 with dissolve
    Akari "我们操纵了你，还有那些乱七八糟的事，我非常抱歉。"
    scene img_main27_668 with dissolve
    "明里瞥了一眼她那不为所动的母亲……"
    scene img_main27_669 with dissolve
    "然后带着一丝坏笑鞠了一躬。"
    scene img_main27_670 with dissolve
    "茜只是对女儿翻了翻白眼，然后转回来面对你。"
    MC "别在意。我已经原谅晓月了。"
    scene img_main27_671 with dissolve
    Akane "我知道。我们会通电话，她搬来之后我从没听过她这么开心。她平时总是那么安静。但自从遇见你，她身上有什么变了。"
    "你能感觉到桌子底下的晓月因为被这样谈论而有些害羞，但现在你没法低头看她。"
    scene img_main27_672 with dissolve
    Akane "但问题在于……她愿意跟我和明里说话，却一个字都不肯跟她父亲讲。"
    Akane "她说她「不能侍奉两个主人」，她「现在选择了你作为她的主人」……"
    MCi "（啊，是啊……那次我去接她的时候确实这么说过。看来她真的记在心里了。）"
    scene img_main27_673 with dissolve
    Akane "我知道您有充分的理由不喜欢我丈夫，但他真的不是坏人。只是有时候……有点被误导了。"
    scene img_main27_674 with dissolve
    Akane "我也了解晓月。我们聊天时，我能从她声音里听出她对您的依恋……我只是担心她可能再也不会跟她父亲说话了。"
    scene img_main27_675 with dissolve
    Akane "所以拜托了，[PlayerName]，您能跟她谈谈吗？我想在这件事上只有她肯听您的话。"
    MCi "（真麻烦……不过她大概说得对。是我告诉晓月要在我和她父亲之间做选择的。）"
    MC "就凭他做过的事，我确实不太喜欢他。"
    scene img_main27_676 with dissolve
    Akane "我再说一次，真的很抱歉。他那样骗你，完全不可接受。"
    MC "相信我，我对此也很气愤。但我对他对待晓月的方式同样气愤——"
    scene img_main27_677 with dissolve
    Akari "她也是。她知道之后扇了他一巴掌。"
    scene img_main27_678 with dissolve
    "茜锋利地看了明里一眼……"
    scene img_main27_679 with dissolve
    "然后又转回看你，眼神里只有悲伤，以及不想看到家庭破裂的纯粹愿望。"
    scene img_main27_680 with dissolve
    MC "您看，晓月对我意义重大。她是我的女朋友，我希望和她在一起很久很久……"
    scene img_main27_681 with dissolve
    "毫无预兆地，就在你说到这里时，晓月突然又开始吸你的鸡巴……"
    MCi "（我他妈，小猫，不是现在……）"
    "你轻轻咳了一声掩饰突然被打断的话，然后在晓月为你口交的同时继续说下去……"
    scene img_main27_682 with dissolve
    MC "呃、抱歉，我刚说到哪了。我打算永远和晓月在一起。也就是说，要和她的家人好好相处。"
    scene img_main27_683 with dissolve
    "晓月用舌头沿你柱身的下侧滑了一下来回应这句话……"
    scene img_main27_684 with dissolve
    "你握紧拳头，把手臂撑在桌上，锁死了自己对这只淘气猫娘可能产生的任何反应。"
    scene img_main27_685 with dissolve
    MC "您看起来是个好母亲，茜。希望以后我们能更好地互相了解。所以我会替您跟晓月谈谈的。"
    scene img_main27_686 with dissolve
    Akane "太感谢您了，[PlayerName]。晓月选了这么正派的男人，我很高兴。"
    scene img_main27_687 with dissolve
    Akari "唔嗯，我猜他也有靠谱的时候。在厨房外面。"
    scene img_main27_688 with dissolve
    Akane "抱歉，我不知道这条我该怎么说才合适。"
    MC "别担心。我完全打算让她好看。在厨房里。到时就看看谁才会被压下去。"
    scene img_main27_689 with dissolve
    "明里在母亲身后偷笑着朝你眨了眨眼……"
    scene img_main27_690 with dissolve
    "但桌子底下的晓月正悄悄把你逼疯，你真的只想让这场互动赶紧结束。"
    scene img_main27_691 with dissolve
    MC "真是抱歉要这么急着送您出门，但我今晚确实还有些工作要完成……"
    scene img_main27_692 with dissolve
    Akane "啊，当然。我们不能耽误您。"
    scene img_main27_693 with dissolve
    Akane "我丈夫和女儿们给您带来这么多麻烦，我再次道歉。"
    MC "别在意。很高兴认识您，茜。"
    scene img_main27_694 with dissolve
    Akari "妈，您先走吧。我想再和[PlayerName]聊一会儿……"
    MCi "（真是的……）"
    Akane "唔嗯，别留他太久。你也听到他很忙了。"
    scene img_main27_695 with dissolve
    "明里无视母亲，把她轰出了办公室。"

    play sound "audio/sounds/door_close.mp3" volume 2.0

    scene img_main27_696 with dissolve
    "她用力关上门，转回来朝你露出一个大大的笑容。"

    play music "audio/bgm/akari_tease.mp3" loop volume 1.0 fadeout 1.0 fadein 1.0

    Akari "那么，{i}弗莱彻先生{/i}……"
    MC "唔……什么事，明里？"
    scene img_main27_697 with dissolve
    "她朝桌子走回来……"
    scene img_main27_698 with dissolve
    "但转而绕到桌子另一边……"
    scene img_main27_699 with dissolve
    MCi "（靠……）"
    scene img_main27_700 with dissolve
    "就在你以为她会径直走到你面前、低头看晓月的时候……"

    scene img_main27_701 with dissolve
    pause

    scene img_main27_702 with dissolve
    "她停下脚步，滑到你面前坐到桌上，交叉着她裸露的双腿，撩人地展现在你面前。"
    scene img_main27_703 with dissolve
    Akari "我记得我给过你号码，还叫你不要发{i}太{/i}多色情照片……"
    scene img_main27_704 with dissolve
    Akari "但我一张都没收到。一张都没有。"
    "桌子底下晓月的服务彻底夺走了你组织俏皮回应的能力。"
    scene img_main27_705 with dissolve
    Akari "唔嗯……猫把舌头叼走了？"
    MCi "（她没低头看……但她肯定知道了，对吧……？）"
    scene vid_main27_9 with dissolve
    "你低头瞄了晓月一眼，判断明里从她坐着的位置绝对能看到晓月的头顶……"
    MC "哦，好吧……"

    scene img_main27_706 with dissolve
    pause

    scene img_main27_707 with dissolve
    "你从桌上拿起手机朝晓月指下去，回答你的只是一声紧绷、憋闷的低吼。"
    scene img_main27_708 with dissolve
    "她反应过来，停下抬头看你；你那沾满唾液、随时要爆的鸡巴还含在她嘴里。"
    
    scene img_main27_709 with dissolve

    play sound "audio/sounds/camera.wav"

    "晓月不情愿地完全退开，好让你迅速拍下一张鸡巴的照片发给明里。"
    scene img_main27_710 with dissolve
    Akari "天啊……"
    "她看着那张照片，有点着迷又突然脸红，露出了你之前没怎么见过的几分天真的样子。"
    Akari "那东西好大……会把我劈成两半……"
    Akatsuki "唔嗯。"
    scene img_main27_711 with dissolve
    "晓月一边继续口交一边应声，这声应答把明里从出神中拉了回来，她又一次用调侃的目光看着你。"
    Akari "背不舒服，是吗？"
    MC "好吧，你已经看穿我们了。那要么留下来看大结局，要么就走。"
    scene img_main27_712 with dissolve
    Akari "唔嗯，好难选啊……"
    scene img_main27_713 with dissolve
    "她突然放下手机，微微后仰，煞有介事地慢慢展开双腿准备从桌上起来……"
    scene img_main27_714 with dissolve
    "给了你一个非常刻意的走光视角……"
    scene img_main27_715 with dissolve
    Akari "唔嗯……我该留下，还是该走……？"
    scene img_main27_716 with dissolve
    "她把腿张得更开，你的目光又被吸引下去，在晓月的嘴和舌头沿你的鸡巴上下滑动时给你点事做。"
    scene img_main27_717 with dissolve
    "但接着她突然合上双腿，从桌上跳了下来。"
    scene img_main27_718 with dissolve
    Akari "真可惜。你要是个更好的厨师，我或许会留下。"
    MC "哈，别做梦了。你不过是想回家对着那张你明目张胆要来的照片自慰而已。是吧？"
    scene img_main27_719 with dissolve
    "她突然语塞，像是被抓住了一样移开视线。"
    Akari "不、不……"
    MC "哈，你开玩笑吧……我只是开玩笑……"
    scene img_main27_720 with dissolve
    "她飞快地转身冲向门口，但脸上的大红晕还是来不及藏住。"
    scene img_main27_721 with dissolve
    Akari "再见了，输家！"
    "她冲出去时，你连回应都懒得给。"


    # Advance Time
    $ CurrentTime += 1
    $ TimeOutput = Time[CurrentTime]

# Day 27 (Night) - //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# - /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    play sound "audio/sounds/door_close.mp3" volume 2.0

    scene vid_main27_10 with dissolve
    "你只是往椅背上一靠，终于能和晓月单独待着，感觉无比解脱……"
    "..."
    scene vid_main27_11 with dissolve
    "门一关，你一直绷着的紧张立刻开始从身上流走……"
    "......"
    scene vid_main27_12 with dissolve
    "而你一放松，就感觉到高潮正在迅速累积……"

    scene img_main27_722 with hpunch
    pause 0.5
    scene img_main27_722 with hpunch
    pause 0.35
    scene img_main27_722 with hpunch
    pause 0.2
    scene img_main27_722 with hpunch
    pause 0.1
    scene img_main27_722 with hpunch
    pause 0.1
    scene img_main27_722 with flash

    "紧接着精液几乎立刻爆发，射进小猫那张急切吸吮的嘴深处。"

    $ persistent.gallery_akatsuki8 = True

    scene img_main27_723 with dissolve
    Akatsuki "唔唔嗯嗯嗯……"
    scene img_main27_724 with dissolve
    MC "哈啊啊啊……操……"
    scene img_main27_725 with dissolve
    "..."
    scene img_black with fade
    "你又一次闭上眼睛往后靠，让晓月把你的存货吸干净，然后舔掉证据……"
    "..."
    "......"
    scene img_main27_726 with fade
    MC "操……要是那感觉不爽，小猫，我就为刚才那事打到你这辈子都忘不了。"
    scene img_main27_727 with dissolve
    Akatsuki "唔嗯……值得。"
    scene img_main27_728 with dissolve
    "她笑着爬到你身上，坐在你的腿上……"

    $ renpy.end_replay()


#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_taka3:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/misaki_theme.mp3" loop fadeout 0.5 fadein 2.0 volume 1.2

    scene img_main28_283 with dissolve
    Misaki "我、呃，是为了你才穿那件比基尼的……"
    MC "哦，你真穿了啊？"
    scene img_main28_284 with dissolve
    "你低头一看，发觉你们边聊边吃，午饭早就吃完了。"
    scene img_main28_285 with dissolve
    "和昨天一样，你起身绕过桌子。"
    MC "站起来。"
    scene img_main28_286 with dissolve
    "她照做之后，你又坐进了她的椅子里。"
    scene img_main28_287 with dissolve
    MC "想给我看看吗？"
    scene img_main28_288 with dissolve
    "她害羞地笑了笑，移开视线，随后点了点头。"
    Misaki "嗯。"
    MC "乖女孩。脱给我看。"
    scene img_main28_289 with dissolve
    Misaki "是、是的，老师。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main28_290 with dissolve
    "她的脸涨得通红，慢慢开始脱衣服……"
    scene img_main28_291 with dissolve
    MC "你越来越熟练了。"
    scene img_main28_292 with dissolve
    Misaki "啊……也许吧。"
    scene img_main28_293 with dissolve
    Misaki "我、我……还是觉得很不好意思……"
    MC "按你自己的节奏来。等你能自在地当着我的面脱衣服了，就可以开始更大胆一点。"
    
    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main28_294 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main28_295 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main28_296 with dissolve
    pause
    scene img_main28_297 with dissolve
    pause
    scene img_main28_298 with dissolve
    pause

    scene img_main28_299 with dissolve
    "花了一点时间，但最后她只剩下昨晚发给你那些照片里穿的那件轻薄比基尼。"
    Misaki "这、这样可以吗？"
    MC "你看起来美极了，姑娘。"
    scene img_main28_300 with dissolve
    Misaki "啊，嘿嘿……"

    scene img_main28_301 with dissolve
    pause

    scene img_main28_302 with dissolve
    "你站起身，轻轻把她搂进怀里……"
    scene img_main28_303 with dissolve
    "但你的目的并不是单纯为了逗弄她抱一抱，而是让她有些意外地把她抱了起来……"
    scene img_main28_304 with dissolve
    "然后把她圆润的屁股挪到桌沿上。"
    scene img_main28_305 with dissolve
    MC "你知道吗，我有个挺坏的主意……"
    scene img_main28_306 with dissolve
    MC "你还记得我以前给你布置过一次作业吗？那时我还是火车上那个神秘的家伙。"
    scene img_main28_307 with dissolve
    Misaki "啊……你、你是说，呃……你当时要我……那个……？"
    MC "哈，没错。那之后我一直让你练的那件事，你试过了吗？"
    scene img_main28_308 with dissolve
    Misaki "啊……"
    "这个问题太直接，她一时愣住了。"
    scene img_main28_309 with dissolve
    Misaki "没、没有……"
    scene img_main28_310 with dissolve
    "你转身把椅子拉过来，重新坐下，准备看着她。"
    scene img_main28_311 with dissolve
    MC "你能演示给我看看吗？"
    scene img_main28_312 with dissolve
    Misaki "真、真的吗？"
    MC "没错。我想看。"
    scene img_main28_313 with dissolve
    "..."
    scene img_main28_314 with dissolve
    Misaki "我、我……可、可以……如果你想的话……"
    scene img_main28_315 with dissolve
    "她紧张得几乎僵住，慢慢在桌上往后挪了挪……"
    
    scene img_main28_316 with dissolve
    pause

    scene vid_main28_1 with dissolve
    "然后别扭地把手伸到两腿之间……"
    scene vid_main28_2 with dissolve
    Misaki "这、这也太羞人了……"
    MC "要是太过头了，你可以停下。我不会生气的。"
    scene vid_main28_3 with dissolve
    "她抬眼看向你，像是在寻求安慰……"
    scene vid_main28_4 with dissolve
    "但随即又羞赧地移开视线。"
    Misaki "不、不……我、我至少能做到这种程度……"
    "你听出她声音里带着一丝不甘，猜想她是铁了心要弥补自己在课堂上说话毫无进展这一点……"
    MCi "（老实说，我不知道她在当众发言这件事上能不能走到那一步。不过即使只是在私下生活里多一分自信，也只会是好事。）"
    scene vid_main28_5 with dissolve
    MC "乖女孩。你做得很好。继续。"
    scene vid_main28_6 with dissolve
    "随着逐渐适应，她慢慢投入了一点。"
    scene vid_main28_7 with dissolve
    MC "快点。"
    scene vid_main28_8 with dissolve
    "听到你的命令，她的动作稍微加快了些。"
    MC "把腿张开一点。让我看。"
    scene vid_main28_9 with dissolve
    Misaki "啊……好、好的……"
    scene vid_main28_10 with dissolve
    "..."
    scene vid_main28_11 with dissolve
    MC "好了，我觉得该轮到我了。" 

    scene img_main28_317 with dissolve
    "你站起来，把硬得发疼的鸡巴掏出来，她的眼睛顿时睁大了……"
    scene img_main28_318 with dissolve
    "然后开始在她面前缓缓上下撸动，彻底吸引了她的目光。"
    MC "眼睛看着这里，姑娘。"
    scene img_main28_319 with dissolve
    "这是开始以来她第一次看你的脸，双颊烧着鲜红的羞意。"
    MC "这还是你第一次真正看到它，对吧？之前几次你都闭着眼睛。"
    scene img_main28_320 with dissolve
    "她点了点头……"
    Misaki "嗯……"
    scene img_main28_321 with dissolve
    "然后她的目光又落回你涨硬的鸡巴上……"
    MC "你停下来了，美咲。"
    scene vid_main28_12 with dissolve
    Misaki "啊，对、对不起……"
    MC "乖女孩。"
    MC "好，把腿再张开一点，就像是在等我操你一样。"
    scene vid_main28_13 with dissolve
    "一如既往，她照做了。"
    scene vid_main28_12 with dissolve
    MC "下次你在家的时候，我希望你想着的就是这个画面："
    MC "想着我，准备把你变成我的人。你做得到吗？"
    scene vid_main28_14 with dissolve
    "她又点了点头，看来由你全权主导时她最开心。"
    MC "再快一点。"
    scene vid_main28_15 with dissolve
    MC "想象我正准备把鸡巴塞进你那紧致的小穴里……"
    Misaki "啊……"
    scene vid_main28_16 with dissolve
    MC "站在你上方，准备像对待一个好骚货那样操你。"
    Misaki "嗯唔……是、是的……"
    scene vid_main28_17 with dissolve
    MC "哈，看你湿成什么样了。"
    Misaki "唔嗯……好、好难……好羞人……"
    MC "你现在是我的骚货了；习惯就好。"
    Misaki "唔嗯——唔哼……"
    scene vid_main28_18 with dissolve
    MC "说出来。"
    Misaki "我、我是……你的骚货……"
    MC "我的乖骚货。"
    scene vid_main28_19 with dissolve
    Misaki "是、是的……你的乖骚货……"
    MC "把内裤拨到一边，让我看看那个可爱的小穴。"
    Misaki "嗯唔……"
    scene vid_main28_20 with dissolve
    "她迟疑了一下，但还是照做了……"
    MC "乖女孩。"
    scene vid_main28_19 with dissolve
    MC "现在，看着我的鸡巴。涨得又硬又痛，全都是为你，美咲。"
    scene vid_main28_21 with dissolve
    Misaki "啊唔……"
    MC "这是你自找的。"
    Misaki "唔嗯嗯嗯……"
    scene vid_main28_22 with dissolve
    MC "不许把眼睛移开。明白吗？"
    Misaki "唔嗯，是……老师……"
    MC "那么，你觉得我想用这个对你做什么？"
    scene vid_main28_23 with dissolve
    Misaki "做、做爱……做、交欢……"
    MC "说清楚。"
    Misaki "你、你想……放、放进我的……"
    MC "再具体点。"
    Misaki "推、推进去……把、把那里撑开……唔嗯……"
    Misaki "到、到最里面……我、我……唔嗯……"
    MC "想象一下。被你的男人插进来，你觉得会是什么感觉？"
    scene vid_main28_24 with dissolve
    Misaki "唔嗯……我、我……我说不出口……"
    MC "睁开眼睛，姑娘。我不是让你一直看着它吗？"
    scene vid_main28_25 with dissolve
    Misaki "唔嗯……是、是的……"
    Misaki "我、我……会觉得又烫……又紧……像是被完全填满了一样……唔……"
    MC "把你的手指滑进去……"
    scene vid_main28_26 with dissolve
    Misaki "唔唔唔！！！"
    scene vid_main28_27 with dissolve
    MC "快点，姑娘。"
    Misaki "我、我唔唔……"
    scene vid_main28_28 with dissolve
    MC "快点。"
    scene vid_main28_29 with dissolve
    Misaki "是的是的唔唔唔！！！"
    scene vid_main28_30 with dissolve
    "她突然抽搐起来，高潮攫住了她，整个身体都绷得僵直……"
    "..."

    ##########BACK TO RENDERS:
    scene img_main28_322 with dissolve
    "终于，她长长地吐出一口气，松弛下来。"
    Misaki "哈啊啊啊啊呼……"
    "..."
    scene img_main28_323 with dissolve
    Misaki "啊……"
    "她抬头看向你，突然变得非常难为情。"
    MC "乖女孩。真他妈的性感。"

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_catherine1:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/catherine_theme.mp3" loop fadeout 1.0 fadein 1.0

    scene img_main29_319 with dissolve
    "你转过身把她拉进一个吻，这突如其来的举动又一次让她晕头转向……"
    Catherine "唔嗯！"
    scene img_main29_320 with dissolve
    "但过了一会儿，她的惊讶消退，整个人放松下来投入这个吻……"
    Catherine "唔嗯……"
    scene img_main29_321 with dissolve
    "..."
    scene img_main29_322 with dissolve
    Catherine "啊……"
    scene img_main29_323 with dissolve
    MC "那天晚上的问题你还没回答{i}我{/i}。对你来说，这仍然只是创立家族那套说辞吗？"
    scene img_main29_324 with dissolve
    Catherine "我、我……可你也没回答我的啊？"
    MC "你知道我的答案。"
    scene img_main29_325 with dissolve
    Catherine "哼。也许吧……"
    "她固执地撅起嘴，移开视线。"
    scene img_main29_326 with dissolve
    "于是你把手放在她脸颊上，把她转回来再亲一下……"
    Catherine "唔嗯！"
    scene img_main29_327 with dissolve
    "..."
    "这一次她也没有反抗，过了一会儿反而主动靠了过来……"
    scene img_main29_328 with dissolve
    "但这一次，发生了一件意外的事……"
    scene img_main29_329 with dissolve
    "她把手绕到你两腿之间，开始手忙脚乱地拉你的裤链……"
    scene img_main29_330 with dissolve
    Catherine "唔嗯……"
    scene img_main29_331 with dissolve
    "你也伸手帮了她一下……"

    play sound "audio/sounds/zipper.mp3" volume 3.0

    scene vid_main29_1 with dissolve

    "在吻还没分开的情况下，她用戴着手套的手握住你的柱身，开始缓缓上下撸动……"
    "..."
    Catherine "唔嗯嗯……"
    "......"

    scene vid_main29_2 with dissolve

    "最后你们俩都分开这个吻来喘口气……"
    Catherine "啊……"
    "然后她立刻害羞地移开了视线……"

    scene vid_main29_3 with dissolve

    "但她的手仍在继续为你撸动……"
    MC "那么，我能把这当成你的答案吗？"
    scene img_main29_332 with dissolve
    "她抬眼看了看你耸耸肩，你们俩{i}仍然{/i}都不肯先给出明确的答案。"

    scene vid_main29_4 with dissolve

    "但接着她加快了手活的速度……第一次做就做得不错，迅速把你推向临界点……"
    "又或者只是因为你憋得太狠了？"

    scene vid_main29_5 with dissolve

    MC "操……继续，公主殿下。"
    Catherine "哼……"

    scene vid_main29_6 with dissolve

    "在她把你推向高潮的同时，你把她拉进一个更长、更深的吻……"
    "..."

    scene vid_main29_7 with dissolve

    Catherine "唔嗯……"
    "她纤细的手指和柔软的手掌把你的鸡巴包裹得恰到好处……"
    "她那只天鹅绒手套的手为你撸动的感觉，简直精妙绝伦……"

    scene vid_main29_8 with dissolve

    "你们俩就这样保持在一起足够久，让你完全失去了对时间的感知……"
    "..."
    "......"

    scene vid_main29_9 with dissolve

    "最后，当你们再次分开时，凯瑟琳长长地、气息般地叹了一口气。"
    Catherine "呼啊啊啊……"
    MC "操我……"

    scene vid_main29_10 with dissolve

    "你能感觉到随着越来越接近射精，睾丸和鸡巴里的快感开始累积……"

    scene vid_main29_11 with dissolve

    "于是你对着凯瑟琳低吼着警告……"
    MC "就差一点了……快点，别停。"

    scene vid_main29_12 with dissolve

    "她还没来得及回答，你就粗暴地把她拉进另一个吻里……"
    Catherine "唔嗯嗯！"

    scene vid_main29_13 with dissolve

    "你看得出她对接下来的事有点手足无措……不过，正如你吩咐的那样，她继续有节奏地给你手活……"
    
    scene vid_main29_14 with dissolve

    "直到几秒之后，她的手把你推过了临界点，带你进入一次轻松而满足的高潮。"
    "..."
    "......"
    scene img_main29_333 with dissolve
    "最后，你绷紧的肌肉放松下来，一阵如释重负的感觉漫过你的全身。"
    scene img_main29_334 with dissolve
    Catherine "唔哼嗯！"
    scene img_main29_335 with dissolve
    "终于，等你彻底射完，你松开怀抱，让她第一次退开。"
    Catherine "啊……"
    scene img_main29_336 with dissolve
    "..."
    "......"
    "过了好一会儿，平复下来之后……"
    scene img_main29_337 with dissolve
    MC "乖女孩。真棒，公主。"
    scene img_main29_338 with dissolve
    Catherine "当、当然……"
    MC "初吻真是够劲爆的，对吧？"
    scene img_main29_339 with dissolve
    Catherine "噗……哼。"
    "她忍不住笑出声，随即又连忙收敛，撅起了嘴……"

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_group4:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/aurum_date.mp3" loop fadeout 1.0 fadein 1.0

    scene img_main29_1297 with dissolve
    "但晓月很快就被分散了注意力，她把一只手滑到你身下，隔着内裤开始揉弄你的鸡巴……"
    scene img_main29_1298 with dissolve
    Sarah "晓、晓月！"
    scene img_main29_1299 with dissolve
    "黑发猫娘无视了她，很快把另一只手也放下来，全部专注于你的鸡巴……"
    scene img_main29_1300 with dissolve
    "而你意识到，这很快就会进展到你怀疑莎拉还没准备好看到的程度——尤其是在她自己都还没什么经验之前。"
    MC "过来，莎拉。"
    scene img_main29_1301 with dissolve
    "她把略带慌乱的表情从晓月身上撕开，赶忙抓住机会去看别的东西。"
    MC "跨坐在我胸口上，面朝我。"
    scene img_main29_1302 with dissolve
    Sarah "为、为什么？"
    MC "我想和你谈谈。"
    scene img_main29_1303 with dissolve
    "她还是有些犹豫，但还是照做了……"

    scene vid_main29_15 with dissolve

    "而且时机刚刚好，晓月终于放开你的鸡巴，开始给你手活……"

    scene vid_main29_15 with dissolve
    pause

    scene img_main29_1304 with dissolve
    Sarah "我、我……我还是能感觉到她在做什么……天啊……我、我……"
    scene vid_main29_17 with dissolve
    "你把手放在她的屁股上捏了捏，把她的注意力拉回你身上。"
    scene img_main29_1304 with dissolve
    MC "放松。你不想做的事，不用勉强。如果你不舒服，我们现在就可以停。"
    scene img_main29_1305 with dissolve
    "她望进你的眼睛，恐惧渐渐平息，担忧也随你的温柔一起流走……"
    scene img_main29_1306 with dissolve
    Sarah "那、那个……我、我们其实还没谈过……但、但是……"
    MC "你想慢慢来？"
    scene img_main29_1307 with dissolve
    "她点点头，松了口气——她不必说出口，你就明白了她的心意。"
    MC "所以，你想让我们停下吗？"
    scene img_main29_1308 with dissolve
    "她鼓足勇气，摇了摇头。"
    Sarah "我、我只是……我、我可以先这样……"
    "那句话没说出口的后半段是：待在她看不见的地方。"
    MC "你确定？这还是相当变态的。"
    scene img_main29_1309 with dissolve
    "她低头瞪了你一眼，轻轻捶了下你的胸口。"
    Sarah "我、我说没关系了……笨蛋……"
    MC "乖女孩……"

    scene vid_main29_18 with dissolve

    "晓月把这当成了最后的绿灯，把你鸡巴的头部送进她急切而湿漉漉的嘴里……"
    
    scene vid_main29_19 with dissolve
    pause

    scene vid_main29_20 with dissolve

    "与此同时，你的视野完全被穿着单薄衣物的、满脸通红的莎拉占据。"
    MC "操我……"

    scene vid_main29_21 with dissolve
    
    "你无法抗拒，把这个羞赧的女孩拉进一个深吻——就像你昨晚花了好几个小时做的那样……"
    "只不过这次，当你的舌头伸进莎拉嘴里时，你的鸡巴正埋在晓月的嘴里……"
    Sarah "嗯嗯……"

    scene vid_main29_22 with dissolve

    Akatsuki "唔唔嗯嗯……"
    "..."
    "......"
    Akatsuki "嗯哼哼嗯……"

    scene vid_main29_23 with dissolve

    "晓月继续娴熟地为你口交，她滚烫、湿淋淋的嘴让你脊背一阵阵战栗，同时挑动着鸡巴顶端每一根神经末梢……"
    MC "嗯嗯……"
    Sarah "嗯嗯嗯……"

    scene vid_main29_24 with dissolve

    "而你感觉自己在无尽的深吻中把每一份感觉都传导给了莎拉，害得她在你嘴里呜咽低吟。"
    "这里最极致的收尾，本该是让晓月骑上你，直到你在她紧致的小穴深处射精……"
    "但你觉得，这对毫无经验的莎拉来说有点越线了……"

    scene vid_main29_25 with dissolve

    "而晓月显然也同意——她成功克制住自己，压下了那个此刻大概也在你脑海里翻涌的冲动……"
    "取而代之的，她卖力地为你服务……"

    scene vid_main29_26 with dissolve

    "只是偶尔退开，舔干净涂满你整根阴茎的大量唾液……"
    "她的舌头抚弄顶端，带来一阵阵窜过鸡巴、直冲脊背的快感战栗……"

    scene vid_main29_27 with dissolve

    "随后又重新投入她热情的吸吮……"
    "当然，在这一番铺垫再加上这一幕之后，她开始迅速把你推向一场极致的高潮……"
    "..."
    "......"

    scene vid_main29_28 with dissolve
    
    "你看得出晓月也感觉到它要来了，于是把速度和强度都拉满……"

    scene vid_main29_29 with dissolve
    
    "直接把你彻底推过临界点，逼你把睾丸里每一滴精液全都射进她喉咙深处……"
    scene img_main29_1310 with dissolve
    "当那一刻来临时，你的视野短暂地白了一瞬，全身的肌肉都绷紧，把莎拉压进你的胸口、压进这个吻的深处……"
    scene img_main29_1311 with dissolve
    "你在晓月嘴里射精，与此同时舌头还留在莎拉的嘴里。"
    scene img_main29_1312 with dissolve
    Sarah "唔唔嗯！！"
    "当然，莎拉准确地意识到了正在发生什么，在这过程中对着你的嘴尖叫出声……"

    scene img_main29_1313 with dissolve
    pause

    scene img_main29_1314 with dissolve
    "然后，终于，随着你的高潮消退、肌肉放松……"
    scene img_main29_1315 with dissolve
    "你松开抓着莎拉的手，让她退开喘气……"

    scene img_main29_1316 with dissolve
    pause

    scene img_main29_1317 with dissolve
    Sarah "啊、哈啊……"
    scene img_main29_1318 with dissolve
    Sarah "变、变态超级大笨蛋！"
    scene img_main29_1319 with dissolve
    MC "呼啊啊啊……那真是爽到爆炸……"
    "你完全看不见晓月，但此刻依然能感觉到她的侍弄，她正舔净你逐渐软下去的鸡巴。"
    scene img_main29_1320 with dissolve
    MC "不知道现在谁的心跳更快，是我的还是你的？"
    "莎拉依然没能好好看着你，用可爱又害羞的声音回答："
    scene img_main29_1321 with dissolve
    Sarah "我、我的……我相当确定。"
    scene img_main29_1322 with dissolve
    "晓月把最后一滴精液全都咽下，又舔干净证据，忽然出现在莎拉身边……"
    Akatsuki "猫喜欢喝奶。你本该尝尝的。"
    MC "嗯，我确实常看见她吃饭时喝很多牛奶，所以她肯定会喜欢。"
    scene img_main29_1323 with dissolve
    Sarah "我、我……"

    play sound "audio/sounds/bed.mp3" volume 4.0

    scene img_main29_1324 with dissolve
    "她迅速从你胸口滑下来，蜷缩在你身侧，把脸从你们两人面前藏起来。"
    scene img_main29_1325 with dissolve
    Sarah "{i}*闷闷的声音*{/i} 闭嘴。白痴。"

    scene img_main29_1326 with dissolve
    pause

    play sound "audio/sounds/bed.mp3" volume 4.0

    scene img_main29_1327 with dissolve
    "见状，晓月开心地占了靠墙的那一侧，心满意足地依偎进你的怀里。"
    scene img_main29_1328 with dissolve
    MC "这真是我收到过最棒的惊喜。谢谢你。我永远不会忘记。"
    scene img_main29_1329 with dissolve
    Akatsuki "嗯。"
    scene img_main29_1330 with dissolve
    "莎拉终于带着羞涩的笑容看向你，见你满意地点了点头……"

    scene img_main29_1331 with dissolve
    "之后，你们就这样躺在一起，平复了很久……"
    "..."
    "......"
    "........."

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_akatsuki9:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/akatsuki_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
    play ambiance "audio/sounds/shower.mp3" volume 1.0 loop fadein 1.0

    scene img_main30_33 with dissolve
    "一如既往，晓月很快又开始了抚弄你的鸡巴，而你知道如果由着她，几秒内它就会进到她的嘴里……"
    scene img_main30_34 with dissolve
    "但你觉得最近受到的宠爱已经远远足够了……"
    scene img_main30_35 with dissolve
    "于是，在她还没开始口交之前，你把手放在她背上，把她转向墙壁。"
    scene img_main30_36 with dissolve
    MC "手扶在墙上，小猫。"
    scene img_main30_37 with dissolve
    "她一言不发，照做了。"
    scene img_main30_38 with dissolve
    "你的一只手顺着她的后腰往下滑……"
    scene img_main30_39 with dissolve
    "然后向前压去，迫使她把腰抵在墙上拱起……"

    scene img_main30_40 with dissolve
    pause

    scene img_main30_41 with dissolve
    "接着又往下滑，掰开她的屁股……"
    scene img_main30_42 with dissolve
    "手指落在她的穴上。"
    
    scene vid_main30_2 with dissolve

    "毫不浪费时间，你开始沿着她的穴缓缓地上下抚摸……"
    "缓慢却有意地稍稍往深处探去，渐渐把她撑开……"
    Akatsuki "唔嗯嗯……"
    
    scene vid_main30_1 with dissolve

    "在你的侍弄下，她轻声呻吟哼叫……"
    Akatsuki "嗯嗯……"
    "每当你的指尖往前探得够深、擦过她的阴蒂时，她都会不由自主地轻轻颤抖。"
    Akatsuki "嗯嗯嗯……嗯嗯！！……唔嗯嗯嗯……"
    
    scene vid_main30_3 with dissolve
    pause
    
    scene vid_main30_4 with dissolve
    
    "你空着的右手伸到她身前，捏住她一边紧实的乳房……"
    Akatsuki "唔嗯嗯嗯……"

    scene vid_main30_5 with dissolve

    "又引发另一波柔软的呜咽与呻吟，你在揉捏和挤压她的乳头之间来回切换……"
    Akatsuki "嗯嗯嗯嗯～～～"

    scene vid_main30_6 with dissolve

    "与此同时你继续稍微加快揉弄她穴的速度……"

    scene vid_main30_7 with dissolve

    "..."
    
    scene vid_main30_1 with dissolve

    "......"
    
    scene vid_main30_8 with dissolve

    "终于，毫无预警——但你明知她早已准备充分——你把中指插进去，直到第二个指节……"
    Akatsuki "唔唔嗯嗯！"
    
    scene vid_main30_9 with dissolve

    "即便是她穴里最浅的部分，也感觉又紧又热，体内起伏的褶皱紧紧裹住你的手指……"
    Akatsuki "嗯嗯嗯……嗯嗯嗯嗯……唔嗯嗯嗯……"
    
    scene vid_main30_10 with dissolve

    "你逐渐加快速度，让手指在她体内更快地进出、蜷曲……"
    
    scene vid_main30_11 with dissolve

    "同时捏弄着她挺立的小乳头……"
    Akatsuki "嗯哼嗯……嗯嗯……唔嗯嗯嗯～！……"
    
    scene vid_main30_12 with dissolve
    pause
    
    scene vid_main30_13 with dissolve
    
    "最后，你把速度提得更快，手指一路推到第三个指节……"
    
    scene vid_main30_14 with dissolve

    Akatsuki "唔唔唔嗯嗯！"
    
    scene vid_main30_16 with dissolve

    "没过多久，你就感觉到她的穴在你指间收缩，大腿紧紧夹住，同时放声呻吟。"
    "她的背拱得更厉害，整个人越过临界点，陷入一次剧烈而颤抖的高潮。"
    
    scene vid_main30_15 with dissolve

    Akatsuki "嗯啊嘿嘿嗯嗯嗯！"
    "这持续了好一会儿……"
    "而那股窜过她身体的快感让你忍不住有点得意。"
    MCi "（哈，我真喜欢她这么容易就能被弄到高潮……）"

    scene img_main30_43 with dissolve
    "随着余韵渐渐消退，你看到她身体有些发软，双腿已经撑不住站立的意志……"
    scene img_main30_44 with dissolve
    MC "哦不，我还没完呢。"
    scene img_main30_45 with dissolve
    "你把手臂绕过她，把她整个人从墙边拉开……"
    scene img_main30_46 with dissolve
    "把她纤细的身体钉在你身上，用一只手强行扶住她……"
    
    scene vid_main30_17 with dissolve

    "另一只手则滑到她身前，开始揉弄她的阴蒂……"
    Akatsuki "啊嗯唔！"
    
    scene vid_main30_18 with dissolve

    "你送去的强烈快感让她颤抖呻吟，哪怕她还没从刚才那次高潮里完全缓过来……"
    
    scene vid_main30_19 with dissolve

    Akatsuki "唔唔唔嗯嗯嗯！……唔嗯嗯嗯嗯嗯……"
    
    scene vid_main30_20 with dissolve

    "但你不肯停下，不给她任何逃避的余地，这一次把全部注意力都集中在她的阴蒂上……"
    Akatsuki "唔唔嗯嗯……唔唔唔嗯……啊嗯嗯嗯嗯～！……"
    
    scene vid_main30_21 with dissolve
    
    "毫无预警地，你加快了速度……"
    "你看得出这简直把她逼疯了，她在你的掌握中扭动挣扎……"
    Akatsuki "唔嗯嗯～～～！"
    
    scene vid_main30_22 with dissolve

    "尽管如此，你依然毫不留情地刺激着她……"
    
    scene vid_main30_23 with dissolve

    "直到最后，她疯狂的叫喊逐渐变成顺从的愉悦啜泣，身体被你牢牢钉在胸口上，无处可逃……"
    "..."
    "......"
    
    scene vid_main30_24 with dissolve

    "最终，这实在太多了，她发出你从未听过的尖叫与哭喊……"
    Akatsuki "唔啊啊嗯～～～！唔唔唔唔嗯嗯唔唔唔！！"
    
    scene vid_main30_25 with dissolve
    
    "她再次爆发出一场更加剧烈、撼动全身的高潮……"
    "全身每一块肌肉都紧紧收缩，她发出一声呻吟，屁股在你胯间起伏，彻底失去控制……"
    "你知道要不是你还强行把她钉在怀里，她现在早就瘫成一堆在地板上，任由快感将她淹没。"
    "..."
    
    scene vid_main30_26 with dissolve
    
    "最终，那阵高潮终于平息，她只剩下粗重而紊乱的喘息，整个人软绵绵地挂在你的手臂上……"
    Akatsuki "啊呜呜呜呜……哈啊……"
    scene img_main30_47 with dissolve
    "你尽量轻柔地把她放到地上，她靠在你腿边支撑身体，一点力气都不剩了。"
    scene img_main30_48 with dissolve
    "她仰头摆到最舒服的位置，你伸手揉了揉她的头，惹得她满足地哼了一声……"
    scene img_main30_49 with dissolve
    Akatsuki "嗯嗯……"
    scene img_main30_50 with dissolve
    MC "嗯，玩得开心。"
    scene img_main30_51 with dissolve
    Akatsuki "嗯哼……"
    scene img_main30_52 with dissolve
    "..."
    scene img_main30_53 with dissolve
    "......"
    scene img_main30_54 with dissolve
    "最后，她双腿还有些发软地站起来，你们一起结束了这场淋浴。"

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_lucy8:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/lucy_theme.mp3" loop volume 1.2 fadeout 1.0 fadein 1.0

    scene img_main30_483 with dissolve
    "........."
    scene img_main30_484 with dissolve
    MC "嘿。"
    scene img_main30_485 with dissolve
    Lucy "嘿！"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main30_486 with dissolve
    "露西小跑到床边，你还没来得及说什么，她已经开始脱衣服了。"
    MC "哈哈，兴奋了？"
    scene img_main30_487 with dissolve
    "她突然意识到自己在干什么，脸颊一下子红了……"
    scene img_main30_488 with dissolve
    Lucy "嗯哼。"
    MC "内裤也要脱。我要你全裸。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main30_489 with dissolve
    "她点点头，把所有衣物都脱了下来。"
    scene img_main30_490 with dissolve
    MC "乖女孩。"
    scene img_main30_489 with dissolve
    MC "过来，趴在我腿上……"
    scene img_main30_491 with dissolve
    "..."
    scene img_main30_492 with dissolve
    MC "我还没这样搞过你吧？"
    Lucy "啊，嗯哼……"
    scene img_main30_493 with dissolve
    "她摆好姿势时，硕大的乳房在你的腿上蹭过……"
    scene img_main30_494 with dissolve
    "然后主动转过身，把屁股献给你的右手，不用你吩咐……"
    scene img_main30_495 with dissolve
    MC "你真有料啊，露西。热得要命。"
    scene img_main30_496 with dissolve
    Lucy "嘿嘿……全、全都是你的……"
    scene img_main30_497 with dissolve
    MC "那么，你今天是个不乖的女孩子？"
    scene img_main30_498 with dissolve
    Lucy "嗯哼……非、非常不乖……"
    "她调皮地回头看你，那副淘气的一面已经好一阵子没见过了。"
    MC "哦是吗？那你觉得自己该挨几下？"
    scene img_main30_499 with dissolve
    Lucy "呃嗯……至少十下。"
    MC "就为那么点小小的过错？"
    scene img_main30_500 with dissolve
    "她点了点头。"
    scene img_main30_501 with dissolve
    Lucy "别、别手下留情，主人……狠狠打。"
    MCi "（她这么说，是因为她真的想要，还是因为她以为我想要、又知道其他几个女孩最近都挨过这么多次？我在想什么呢。）"
    MCi "（几周前我会直接问她……但经历了我们一起做过的这些事之后，现在还小看她，会让我自己觉得恶心……简直像是背叛了她的信任。）"
    scene img_main30_502 with dissolve
    "你发现她正不安地抬头看你，鉴于她是那么敏锐的人，你怀疑她对你心里的纠结一清二楚。"
    MC "好吧。给这个不乖又有料的小女朋友十下狠的。你的屁股明天会又酸又疼，露西。"
    scene img_main30_503 with dissolve
    "她露出大大的笑容，点了点头。"
    Lucy "嗯哼。"
    scene img_main30_497 with dissolve
    MC "低头。给我数着……"

    scene img_main30_504 with dissolve
    pause

    play sound "audio/sounds/spank_mid2.mp3"

    scene img_main30_505 with hpunch
    "{i}*啪！*{/i}"
    Lucy "啊！"
    "你打得比以往任何一次都重……虽然比不上你对薇琪和凯瑟琳下手那么狠，但还是足够让她真切地感觉到。"
    scene img_main30_506 with dissolve
    Lucy "一、下……"
    scene img_main30_507 with dissolve
    MC "乖女孩。"

    play sound "audio/sounds/spank_mid3.mp3"

    scene img_main30_508 with hpunch
    "{i}*啪！*{/i}"
    Lucy "唔啊啊！"
    scene img_main30_509 with dissolve
    Lucy "二。"

    play sound "audio/sounds/spank_mid2.mp3"

    scene img_main30_510 with hpunch
    "..."

    play sound "audio/sounds/spank_mid3.mp3"

    scene img_main30_511 with hpunch
    "......"
    scene img_main30_512 with dissolve
    "打到第五下时，她的屁股已经红了起来，摸上去发烫，于是你停下来，先摸了她一会儿……"
    scene img_main30_513 with dissolve
    Lucy "嗯嗯……"
    scene img_main30_514 with dissolve
    "你的手指从她的屁股游走到她暴露在外的穴上……"
    scene img_main30_515 with dissolve
    "随性拨弄着，几乎漫不经心，完全凭当下兴致而行……"
    scene img_main30_516 with dissolve
    Lucy "啊……"
    scene img_main30_517 with dissolve
    "..."
    scene img_main30_518 with dissolve
    "......"
    scene img_main30_519 with dissolve
    "你看得出她才刚开始真正投入……当你把手抽开时……"

    play sound "audio/sounds/spank_mid2.mp3"

    scene img_main30_520 with hpunch
    "{i}*啪！*{/i}"
    Lucy "啊嗯嗯！"
    scene img_main30_521 with dissolve
    Lucy "六。"

    play sound "audio/sounds/spank_mid3.mp3"

    scene img_main30_522 with hpunch
    "..."

    play sound "audio/sounds/spank_heavy1.mp3"

    scene img_main30_523 with hpunch
    "......"

    play sound "audio/sounds/spank_heavy2.mp3"

    scene img_main30_524 with hpunch
    "{i}*啪！*{/i}"
    Lucy "嗯嗯嗯！"
    scene img_main30_525 with dissolve
    Lucy "十、十下……"
    scene img_main30_526 with dissolve
    "打完了；你又回去揉捏她那已经烧红了的屁股……"
    scene img_main30_527 with dissolve
    MC "全部结束。感觉怎么样？"
    scene img_main30_528 with dissolve
    "她长长地呼出一口气，像是所有紧张都被释放了出来……"
    scene img_main30_529 with dissolve
    "然后扭过身来冲你笑。"
    Lucy "嘿嘿……很轻松啊。"
    MCi "（管他的，和埃莉森的约会之前我还有点时间……）"
    scene img_main30_530 with dissolve
    "你把手放在她背上，让她看起来有点困惑……"
    scene img_main30_531 with dissolve
    "然后把她按下去，比刚才压得更深，把她的脸和胸口都压在床上。"
    scene img_main30_532 with dissolve
    MC "惩罚还没结束。"
    scene img_main30_533 with dissolve
    "她以坚定不移的决心与信任点了点头，做好了接受你任何处置的准备……"
    scene img_main30_534 with dissolve
    "不过你完全没打算再多打她一下。"
    scene img_main30_535 with dissolve
    "你只是把手从她的屁股滑下去，又回到她的穴上……"
    
    scene vid_main30_27 with dissolve

    "这一次，你比刚才更有意图地用手指插入她体内。"
    Lucy "唔嗯？"

    scene vid_main30_28 with dissolve

    MC "我判你一次高潮。现在乖乖地为我高潮吧。"
    Lucy "啊……嗯哼……"

    scene vid_main30_29 with dissolve

    "就像今天早上在淋浴间对晓月做的那样，你一开始慢得让人心痒，一点一点把她带入状态……"

    scene vid_main30_30 with dissolve

    "随后才逐渐加快，对她越来越粗暴……"

    scene vid_main30_31 with dissolve

    Lucy "嗯嗯嗯嗯……嗯嗯～～～"

    scene vid_main30_32 with dissolve

    Lucy "你、你的鸡巴，嗯嗯……可、可以，呃嗯……用、用你的鸡巴……"
    MC "嗯，这可不在计划之内……不过，如果你求我的话，我或许会考虑。"
    "她发出一声迷醉而淫荡的呻吟，急切地想让你进到她的体内。"
    Lucy "嗯哼求求你了……[PlayerName]……我需要它……"

    scene vid_main30_33 with dissolve

    "你的手指从一根加到两根……"
    "然后用这个舒服的节奏维持很久，用对更多的渴望把她逼疯……"
    Lucy "嗯嗯！！～～～求求你……我想要你进来……"

    scene vid_main30_34 with dissolve

    "她不停哀求、呻吟、乞怜，而你则继续无视她，在她紧致、湿透的小穴上卖力耕耘……"
    "..."
    "......"

    scene vid_main30_35 with dissolve

    "你维持了足够久，久到能感觉到她越来越接近高潮——尽管那更多的渴望，也或许正因为那渴望……"
    Lucy "嗯嗯嗯嗯……我、我嗯嗯……不唔……我不要～～～"
    Lucy "唔唔不要啊啊嗯嗯！"
    MC "忍住，露西。如果你能再撑十分钟，我就按你想要的把鸡巴给你。"
    "你带着几分残忍地低笑，因为你的指交正推向激烈而毫不留情的顶点，你完全清楚她根本撑不了那么久……"
    
    scene vid_main30_36 with dissolve
        
    Lucy "我、我忍不了！"
    Lucy "嗯嗯～～～啊啊嗯嗯……"

    scene vid_main30_37 with dissolve

    "你把速度提得更快，彻底压垮她最后一丝抵抗……"
    "但她仍旧抓紧床单、紧闭双眼，做最后的努力去抵抗窜过身体的快感……"
    Lucy "嗯啊嗯……唔唔嗯……嗯嗯嗯嗯嗯～～"

    scene vid_main30_38 with dissolve  
    
    "但这没有用，她的身体坠入一次凶猛的高潮……"
    Lucy "唔唔不要啊啊嗯嗯唔唔唔唔～～～～～～～～"
    "即便你感觉到她的穴在你指间愉悦地收缩痉挛，你仍继续用手指操弄她足足十五秒，任由一波接一波无法抗拒的快感将她淹没……"
    Lucy "哦呼～～～～啊啊啊啊嗯啊啊～～～～～～～～～～～～"

    scene img_main30_536 with dissolve
    "最终，她瘫软下来再也射不出来时，你放慢动作停了下来……"
    scene img_main30_537 with dissolve
    "抽出手指，重新把手放到她依然红得发亮的屁股上，而露西在那儿大口大口地呼吸。"
    "..."
    scene img_main30_538 with dissolve
    "过了好一阵子，才从那场压倒性的体验中恢复过来，她睁开眼睛坐起身……"
    scene img_main30_539 with dissolve
    "转过身来，搂着你的脖子躺进你的怀里。"
    scene img_main30_540 with dissolve
    Lucy "坏蛋……我、我想让你和我一起高潮……"
    MC "哈，明明你是那个想要受罚的不乖女孩。我要是把你想要的全都给你，那还算什么惩罚。"
    MC "你该庆幸自己是露西；换作薇琪，我会做一模一样的事，最后连让她高潮都不给。"
    scene img_main30_541 with dissolve
    Lucy "啊，嘿嘿……也许以后我该更小心一点，别乱许愿。"
    MC "真的吗？"
    scene img_main30_542 with dissolve
    "她咯咯笑着摇了摇头。"
    scene img_main30_543 with dissolve
    "..."
    "......"
    MC "你的晚饭大概要凉了……"
    scene img_main30_544 with dissolve
    "她忽然显得有些纠结。"
    MC "别担心，我敢肯定晓月不会介意帮忙热一下。"
    scene img_main30_545 with dissolve
    "你把她拉近些，她在你怀里放松地靠了一会儿……"
    scene img_main30_546 with dissolve
    "..."
    "......"

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_headmistress2:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/alison_date.mp3" loop fadeout 1.0 fadein 1.0
    
    scene img_main30_627 with dissolve
    "终于，天色开始晚了，你开始考虑该回家了……"
    MC "那么，晚安吻是允许的吗，还是连那个也得等？"
    scene img_main30_628 with dissolve
    Alison "噗。你每次见面都跟我吻别。要是那算问题，我早就会说了吧？"
    scene img_main30_629 with dissolve
    MC "嗯……看来道别的摸奶也不用等了……不知道还有什么是白等不用等的？"
    scene img_main30_630 with dissolve
    "她突然抢先出手，把你推倒在沙发的角落里，出其不意地让你措手不及……"
    scene img_main30_631 with dissolve
    "你发现自己被她笼罩在身下，她低头凝视你的眼睛，露出诱人的笑容。"
    Alison "我只说了要等做爱。你凭什么觉得{i}我{/i}还会等别的？"
    scene img_main30_632 with dissolve
    "你把双臂撑在身下借力……随后从沙发上撑起身体……"
    scene img_main30_633 with dissolve
    "一路反转局面，那个爱调侃的女人被你压住，反而仰头朝你咧嘴笑着。"
    scene img_main30_634 with dissolve
    MC "哦不。就算我乐意让你来操管我们家族的事务，你也很快就会发现，在这种事上我的做法是非常亲力亲为的。"
    Alison "嗯哼……别担心，我早就察觉到了……"
    scene img_main30_635 with dissolve
    Alison "上次差点被你的鸡巴噎死，可是个不小的破绽。"
    scene img_main30_636 with dissolve
    Alison "算你走运，我怎样都开心。"
    scene img_main30_637 with dissolve
    "她一边调侃一边俯身靠近，你则把她推回去，狠狠地吻了上去……"
    scene img_main30_638 with dissolve
    Alison "嗯嗯……"
    "正如她所说，由你主导、由你强势主导，她似乎完全自在得很……"
    scene img_main30_639 with dissolve
    "当你用力捏住她一边硕大的乳房时，你甚至能感觉到她在身下变得稍微温顺了些。"
    Alison "唔嗯嗯……"
    scene img_main30_640 with dissolve
    "最后，你结束这个吻退开，留下她仰面躺着，衣衫略显凌乱……"
    Alison "啊……"
    scene img_main30_641 with dissolve
    "你在沙发上往后挪了挪，准备站起来……"
    scene img_main30_642 with dissolve
    "但又一次，就在你试图起身时，她扑了上来，稳住身形后把你重新压倒……"
    scene img_main30_643 with dissolve
    "这一次她真正跨坐在你身上，同时磨蹭着你鼓起的部位……"
    scene img_main30_644 with dissolve
    Alison "我说怎样都开心，可不代表会让你轻松得手。"
    scene img_main30_645 with dissolve
    "她俯身吻上你……"
    Alison "嗯嗯……"
    scene img_main30_646 with dissolve
    MCi "（她真可惜，这局从一开始就注定了……）"
    scene img_main30_647 with dissolve
    "你先撑起双脚，然后在她磨蹭你的同时把手伸到她的裙子下面，落在她结实的屁股上……"
    scene img_main30_648 with dissolve
    "然后站起身，毫不费力把她整个人抱到空中。这一招她绝对做不到反过来的版本——当时被按倒的{i}你{/i}怀里装的是{i}她{/i}。"
    scene img_main30_649 with dissolve
    Alison "唔啊！这不算犯规吗！"
    scene img_main30_650 with dissolve
    MC "你哭去吧。"
    scene img_main30_651 with dissolve
    "她咧嘴一笑，又狠狠地吻上来，同时你抱着她朝卧室走去……"
    scene img_main30_652 with dissolve
    "你用她的屁股把门顶开……"
    scene img_main30_653 with dissolve
    Alison "唔嗯嗯……"

    scene img_main30_654 with dissolve
    pause

    play sound "audio/sounds/bed.mp3" volume 4.0

    scene img_main30_655 with dissolve
    "最终，当你把她放到床上时，她终于被迫中断了那个挑衅的吻……"

    play sound "audio/sounds/lightswitch.mp3" volume 2.0

    scene img_main30_656 with dissolve
    "你在黑暗中摸索了一会儿，才终于打开一盏台灯……"
    scene img_main30_657 with dissolve
    "等你转回头时，发现她已经半裸着，裙子被扔到不知哪儿去了。"
    scene img_main30_658 with dissolve
    MC "嗯嗯……又是丝袜。"
    scene img_main30_659 with dissolve
    Alison "我说过我清楚自己在做什么。"
    scene img_main30_660 with dissolve
    "你飞快地脱掉外套、踢掉鞋子，然后扑上前把她压在床上，又是一个吻……"
    scene img_main30_661 with dissolve
    "她愉快地融化在你的吻里，任由你主导一会儿……"
    scene img_main30_662 with dissolve
    Alison "唔嗯嗯……"
    scene img_main30_663 with dissolve
    "又一次，最终你感觉到她开始有些抗拒……但你片刻都不肯松开，始终把她压住。"
    Alison "哼……"
    scene img_main30_664 with dissolve
    "..."
    "......"
    scene img_main30_665 with dissolve
    "最后，你决定给她一个喘息的机会，松了手……"
    scene img_main30_666 with dissolve
    "而她立刻挑衅地一笑，翻身骑到了你身上……"

    scene vid_main30_39 with dissolve  
    
    "继续用身体磨蹭你鼓起的鸡巴……"

    scene vid_main30_41 with dissolve  
    
    MC "噗。你刚说自己能等。想得美！"
    Alison "嗯，是吗？照这个速度，我还没放弃，你的内裤里就要射了……"
    "你意识到她说得没错……她这样磨蹭下去可能真的会变得很危险……"

    scene vid_main30_40 with dissolve  
    
    "不过感觉他妈的确实很爽，于是你让她继续磨蹭了一会儿，满足地躺着享受……"

    scene vid_main30_42 with dissolve  
    
    "..."

    scene vid_main30_43 with dissolve  
    
    "......"
    "........."

    play sound "audio/sounds/bed.mp3" volume 4.0

    scene img_main30_667 with dissolve
    "但你完全没打算让她赢，最终你抓住她的手臂，把她翻回仰躺，重新夺回主导权。"
    scene img_main30_668 with dissolve
    Alison "胆小鬼。"
    scene img_main30_669 with dissolve
    "你把她的手腕按进床单里吻着她……"
    scene img_main30_670 with dissolve
    "而她立刻反击，用双腿缠住你，把自己的胯部抵上你的胯部磨蹭……"
    scene img_main30_671 with dissolve
    "这逼得你更进一步……"
    scene img_main30_672 with dissolve
    "你用力把她从床上抬起一点，越过她的背后去解她内衣的扣子……"   
    
    play sound "audio/sounds/bed.mp3" volume 6.0
    
    scene img_main30_673 with dissolve
    "然后毫不客气地把她重新摔回柔软的床垫上。"
    Alison "呃……"
    scene img_main30_674 with dissolve
    Alison "野蛮人。"
    scene img_main30_675 with dissolve
    "还没等你替她动手，她就自己伸手到胸前……"
    scene img_main30_676 with dissolve
    "把没扣的胸罩拉了下来，扔到床下。"
    scene img_main30_677 with dissolve
    "她抬头直视你的眼睛，毫不退缩地挑衅你，等着看你的下一步。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main30_678 with dissolve
    "作为回应，你往后一坐，开始脱自己的衣服，把它们扔成一堆压在她的上面……"
    scene img_main30_679 with dissolve
    "等你彻底赤裸，你转回头看她……"

    scene img_main30_680 with dissolve
    pause

    scene img_main30_681 with dissolve
    "捏住那条勉强吊着她小内裤的细带……"
    scene img_main30_682 with dissolve
    "然后迅速地把它拉下来……"
    scene img_main30_683 with dissolve
    "你不确定她原本期待的是什么，但显然不是这个，因为她听起来相当意外……"
    Alison "啊！"
    scene img_main30_684 with dissolve
    "不过她很快就恢复过来，挪动双腿，好让那最后一点障碍顺利脱离。"
    
    play sound "audio/sounds/bed.mp3" volume 4.0
    
    scene img_main30_685 with dissolve
    "就在它们还在朝卧室地板飞去的时候，你已经把埃莉森重新压回床上，又是一轮激烈的深吻……"
    scene img_main30_686 with dissolve
    "但这一次，当你把鸡巴抵在她暴露的穴上磨蹭时，她倒吸了一口气……"
    Alison "唔嗯嗯！！"
    scene img_main30_687 with dissolve
    "她持续地呻吟、喘息，你已经逼近那条不可逾越的界线。"
    Alison "嗯嗯……"
    scene img_main30_688 with dissolve
    "但她没有试图反抗，信任你会遵守承诺——哪怕事情已经到了这一步……"
    Alison "唔嗯嗯……"
    scene img_main30_689 with dissolve
    "..."
    "......"
    scene img_main30_690 with dissolve
    "最后，你退开一点，逗弄她。"
    MC "该死，我最好还是对你温柔点……你湿成这样，我可不希望它不小心滑进去。"
    scene img_main30_691 with dissolve
    "她的眼中闪过被挑战的光芒……"
    scene img_main30_692 with dissolve
    "而你笑了，看她拼尽全力挣扎了几下，却完全撼动不了你的力量和体重……"
    scene img_main30_693 with dissolve
    "最后你才放开力道，让她把你推翻，重新拿回上面的位置——身上只穿着丝袜和一个大胆的笑容。"

    scene vid_main30_44 with dissolve

    "她开始上下摆动腰胯，让湿透的穴沿着你硬如岩石的整根阴茎研磨摩擦……"

    scene vid_main30_45 with dissolve

    Alison "嗯哼嗯……"
    MC "哈哈，撞到你的阴蒂了？你是在逗我，还是在逗你自己？"

    scene vid_main30_46 with dissolve

    Alison "嗯嗯……都是。"
    "她咧嘴一笑，继续骑着你……"

    scene vid_main30_47 with dissolve

    "而你则相反，把双手枕在脑后，仰躺在床垫上，完全满足于让她来服侍你……"

    scene vid_main30_48 with dissolve

    Alison "得意忘形的混蛋。"
    MC "没错。看看你累趴之前能不能让我射出来……"
    "她又骑了几抽……"
    scene img_main30_694 with dissolve
    "然后顺着你的身体滑下来，跪坐在你的两腿之间……"

    scene vid_main30_49 with dissolve

    "立刻把你湿淋淋的鸡巴含进嘴里，帮你收尾……"
    Alison "嗯嗯……"

    scene vid_main30_50 with dissolve

    MC "操……"
    Alison "唔嗯嗯……"

    scene vid_main30_51 with dissolve

    MC "啊……看来我没说清楚你得用什么让我射出来……"
    Alison "嗯哼……"

    scene vid_main30_52 with dissolve

    "经过这一番铺垫和挑逗，她没花多久就把你逼到了高潮边缘……"

    scene vid_main30_53 with dissolve

    Alison "唔嗯嗯～～～"

    scene vid_main30_54 with dissolve

    "而她在你阴茎周围发出餍足的胜利呼噜声……"
    MC "真可惜……我刚想起来……你的咽反射并不怎么强……"

    scene vid_main30_55 with dissolve
    
    "你抬起一只手把她的头按了下去……"
    Alison "唔嗯！"
    "在这一刻，彻底攫取了对她完完全全的主导权……"
    "你把一股股精液射进她紧致而顺从的喉咙深处。"
    Alison "唔唔嗯唔！！"

    scene img_main30_695 with dissolve
    "你把她按在原位多停留了几秒，比必要的更久……"
    "..."
    scene img_main30_696 with dissolve
    Alison "嗯哼～～！"
    "她发出一声意外可爱的呜咽……"
    
    scene img_main30_697 with dissolve
    pause

    scene img_main30_698 with dissolve
    "当你终于松手、让她的喉咙从你的鸡巴上滑开时，她咳嗽着喘了几口气……"
    scene img_main30_699 with dissolve
    Alison "哈啊……"
    "..."
    scene img_main30_700 with dissolve
    "长长地呼出一口气后，她又一次露出调侃的笑容。"
    Alison "好吧好吧，这次算你赢。我早该料到的。"
    MC "最好习惯它，我打算每次都赢。"
    scene img_main30_701 with dissolve
    Alison "噗。像我会站在你那边一样……得意忘形……"
    scene img_main30_702 with dissolve
    "她从你两腿之间爬出来，挪回你身边的枕头上……"

    $ renpy.end_replay()



#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
#######################################################################################################################################################################################################################
label replay_group5:

    $ PlayerName = persistent.replay_PlayerName

    play music "audio/bgm/threesome.mp3" loop fadeout 1.5 fadein 1.5 volume 1.0

    scene img_main32_986 with fade
    "过了一会儿，两个女孩一起上楼来……"
    
    scene img_main32_987 with dissolve
    pause

    scene img_main32_988 with dissolve
    "薇琪一点也不浪费时间，直奔你身边，用一个兴奋而淫荡的吻主动出击……"
    scene img_main32_989 with dissolve
    Victoria "嗯嗯……"
    scene img_main32_990 with dissolve
    "..."
    "你把这个吻拖得很长……"
    scene img_main32_991 with dissolve
    "双手在她身上游走，几乎要演变成一场真正的深吻狂潮……"
    scene img_main32_992 with dissolve
    "直到，就在你开始感觉到她越来越兴奋的时候……"
    
    play sound "audio/sounds/spank_heavy1.mp3"
    
    scene img_main32_993 with vpunch
    "{i}*啪！*{/i}"
    scene img_main32_994 with dissolve
    Victoria "嗯！"
    scene img_main32_995 with dissolve
    Victoria "啊……"
    MC "好了，够了。"
    scene img_main32_996 with dissolve
    "你在床边坐下，两个女孩满怀期待地看着你。"
    scene img_main32_997 with dissolve
    MC "露西，过来。"

    play sound "audio/sounds/bed.mp3" volume 4.0

    scene img_main32_998 with dissolve
    "她立刻应声蹦过来，在你身旁坐下……"
    scene img_main32_999 with dissolve
    "你伸手揽住她，随手捏了捏她一边硕大的乳房。"
    scene img_main32_1000 with dissolve
    MC "乖女孩。一如既往地听话。"
    scene img_main32_1001 with dissolve
    "她害羞地红了脸，但依然仰头冲你笑。"
    Lucy "嗯哼……一直都很听话。"
    scene img_main32_1002 with dissolve
    MC "好了，我性感的小女奴，给我脱衣服。不过束腰留着，很性感。"
    scene img_main32_1003 with dissolve
    Victoria "嗯，好的，主人。"

    scene img_main32_1004 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main32_1005 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main32_1006 with dissolve
    pause

    scene img_main32_1007 with dissolve
    "你看着她挑逗地在你面前一件件脱下衣物，心率渐渐加快……"
    scene img_main32_1008 with dissolve
    "而且不用你吩咐，露西就自己把手滑下去，捏了捏你牛仔裤里越来越鼓的凸起……"

    scene img_main32_1009 with dissolve
    pause
    scene img_main32_1010 with dissolve
    pause

    scene img_main32_1011 with dissolve
    MC "那么，先对你做什么好呢……选择，选择……"
    scene img_main32_1012 with dissolve
    MC "嗯哼……"
    scene img_main32_1013 with dissolve
    MC "算了。露西，你先来。"
    Victoria "主～人！太过分了！"
    scene img_main32_1014 with dissolve
    MC "给我脱衣服。"
    scene img_main32_1015 with dissolve
    Lucy "嗯哼……"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main32_1016 with dissolve
    pause

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main32_1017 with dissolve
    pause
    scene img_main32_1018 with dissolve
    pause
    scene img_main32_1019 with dissolve
    MC "真火辣……"
    scene img_main32_1020 with dissolve
    "你慢慢地上下打量她，刻意而专注……"
    scene img_main32_1021 with dissolve
    "然后稍微靠近，低头看着她泛红的脸。"
    MC "让人无法抗拒。我今晚可能会把你操到神志不清。"
    scene img_main32_1022 with dissolve
    Lucy "啊，嘿嘿……"
    MC "你想要那样？"
    scene img_main32_1023 with dissolve
    "她低头看着地板，点了点头。"
    scene img_main32_1024 with dissolve
    MC "不过首先……"
    scene img_main32_1025 with dissolve
    MC "你确定你想试试看吗？"
    scene img_main32_1026 with dissolve
    "她向前一步，又点了点头，这一次更多是坚定而非羞怯。"
    MC "那么，跪到床上去。"
    scene img_main32_1027 with dissolve
    "她照做了……"
    scene img_main32_1028 with dissolve
    "不过你还是俯下身稍微调整她的姿势，你的动作让她的背形成了一道诱人的弧线。"
    scene img_main32_1029 with dissolve
    MC "乖女孩。给我保持这个姿势。"

    scene img_main32_1030 with dissolve
    pause

    scene img_main32_1031 with dissolve
    "你在塞子上涂了一点润滑剂，又在手指上抹了一团，涂在她最后一道防线之上。"
    scene img_main32_1032 with dissolve
    Lucy "哈啊啊……"
    scene img_main32_1033 with dissolve
    "她发出一声气若游丝的叹息，你已经看得出她窘迫到了极点。"
    scene img_main32_1034 with dissolve
    "于是你开心地抓住机会慢慢折磨、戏弄她，用手指越揉越深入。"
    scene img_main32_1035 with dissolve
    Lucy "嗯嗯……[PlayerName]……"
    MC "嘘。"

    scene img_main32_1036 with dissolve
    pause

    scene img_main32_1037 with dissolve
    Lucy "唔嗯……"

    scene img_main32_1036 with dissolve
    pause
    scene img_main32_1037 with dissolve
    pause

    scene img_main32_1035 with dissolve
    MC "好了，你准备好了吗？"
    scene img_main32_1038 with dissolve
    Lucy "嗯哼……"
    MC "准备好什么？"
    scene img_main32_1039 with dissolve
    Lucy "准、准备让你把它放进我的屁股里……"
    MC "乖女孩。"
    scene img_main32_1040 with dissolve
    "你把塞子换到右手，抵在她紧致的小穴口上……"
    scene img_main32_1041 with dissolve
    Lucy "嗯嗯……"
    scene img_main32_1042 with dissolve
    "慢慢地，一点一点地，你把它推得更深……"
    scene img_main32_1043 with dissolve
    "然后又拔出来，重新开始……"
    Lucy "唔嗯嗯……"
    scene img_main32_1044 with dissolve
    "当你在最宽的那部分停留片刻、把她撑开时，她发出一声呻吟……"
    Lucy "啊啊啊……"
    scene img_main32_1045 with dissolve
    "接着，当你把它整个推入时，她松了口气——惊讶中带着如释重负，因为被撑开的感觉换成了更柔和的压迫。"
    scene img_main32_1046 with dissolve
    "你从抽屉里抽出一张湿巾，擦掉手上的润滑剂……"
    scene img_main32_1047 with dissolve
    "然后转向已经等得不耐烦的维多利亚。"
    scene img_main32_1048 with dissolve
    Victoria "轮到我了？"
    MC "该你了。"
    scene img_main32_1049 with dissolve
    MC "露西，坐起来。"
    scene img_main32_1050 with dissolve
    Lucy "唔哼……"
    scene img_main32_1051 with dissolve
    "她带着塞子第一次挪动身子时，可怜地呜咽了一声。"
    MC "怎么样？"
    scene img_main32_1052 with dissolve
    "她听出你声音里那一丝担忧，安抚地笑了笑，然后点了点头。"
    Lucy "嗯哼！只是有点吓到我了……感觉好紧……"
    MC "哈。等我带着它操你的时候，会更紧。"
    scene img_main32_1053 with dissolve
    Lucy "啊……嗯哼……"
    scene img_main32_1054 with dissolve
    MC "那么，维多利亚……"
    scene img_main32_1055 with dissolve
    MC "转过去。"

    scene img_main32_1056 with dissolve
    pause

    scene img_main32_1057 with dissolve
    "你先用今天早些时候弄来的、颜色恰好是黑色的绳子，把她的手腕绑在身后……"    
    scene img_main32_1058 with dissolve
    Victoria "嗯嗯……可以再紧一点，主人……"
    scene img_main32_1059 with dissolve
    MC "不行。这是我们第一次做这个，所以要小心点。已经够紧了，就算你使出全力也挣不开。"
    scene img_main32_1060 with dissolve
    Victoria "对你来说也是第一次？"
    MC "是啊。以前从没试过这个。"
    scene img_main32_1061 with dissolve
    "她突然转身面向你，脸上绽开一个大大的笑容。"
    Victoria "真的？我是被你绑起来的第一个女孩？"
    MC "你是……不过，我不记得告诉过你可以转身。"
    scene img_main32_1062 with dissolve
    "她咯咯笑着，又把背转了回去。"

    play sound "audio/sounds/spank_heavy2.mp3"

    scene img_main32_1063 with vpunch
    "{i}*啪！*{/i}"
    scene img_main32_1064 with dissolve
    Victoria "嗯嗯……对不起，主人……"
    scene img_main32_1065 with dissolve
    MC "上床。"
    scene img_main32_1066 with dissolve
    "她开心地走到露西坐着的地方，可面对这个没有手臂支撑就得躺下的新体验时，却迟疑了……"
    scene img_main32_1067 with dissolve
    "不过她很快就解决了：先跪下，再翻身侧倒……"
    scene img_main32_1068 with dissolve
    "但她没躺多久，很快又跪回原位，把屁股献出来等着被塞入。"
    scene img_main32_1069 with dissolve
    "你涂上大量润滑剂， 比对露西时少了几分温柔，很快就以此开始撑开她……"
    scene img_main32_1070 with dissolve
    Victoria "唔嗯嗯……"
    scene img_main32_1071 with hpunch
    Victoria "嗯嗯……"
    "过了几秒，你把它一推到底，惹来一声满足的呻吟……"
    scene img_main32_1072 with dissolve
    Victoria "啊哈？！"
    "却又在下一秒立刻把它拔了出来，出其不意地吓她一跳。"
    scene img_main32_1073 with dissolve
    Victoria "唔唔嗯主～人……"
    scene img_main32_1074 with dissolve
    "你又戏弄她的肛门一会儿……"
    scene img_main32_1075 with dissolve
    "最后才终于把它彻底塞到位。"
    scene img_main32_1076 with dissolve
    MC "现在，躺到你的背上。"
    scene img_main32_1077 with dissolve
    "她翻过身去，你则抓起那根更长的绳子，让她被绑缚的手臂撑起上半身。"
    scene img_main32_1078 with dissolve
    MC "那么，我们来看看……"
    scene img_main32_1079 with dissolve
    Victoria "嗯，主人觉得你能自己想办法吗？你是新手，会挺难的吧……"
    scene img_main32_1080 with dissolve
    "她玩味地朝你坏笑，分明是在求罚。"
    scene img_main32_1081 with dissolve
    MC "你知道你这句话会让我讨上几个小时吗？"
    scene img_main32_1082 with dissolve
    "她又笑了，对这个回答满意得不能再满意。"
    scene img_main32_1083 with dissolve
    "你把绳子甩到她胸口，跪在床上她身旁……"
    scene img_main32_1084 with dissolve
    "然后用双手把她的腿和大腿摆成你想要的样子。"
    scene img_main32_1085 with dissolve
    "你用一只手继续按住不放，只是稍微用力捏了捏她的大腿取乐——薇琪便发出一声玩味的小呻吟……"
    scene img_main32_1086 with dissolve
    "你用另一只手取来绳子……"
    scene img_main32_1087 with dissolve
    "接着把绳子的一端紧紧缠在她的脚踝上。"
    scene img_main32_1088 with dissolve
    "粗绳结打好后，你把手指伸进绳子和她的腿之间，确认没有紧到弄疼她……"
    scene img_main32_1089 with dissolve
    MC "把腰从床上拱起来。"

    scene img_main32_1090 with dissolve
    pause

    scene img_main32_1091 with dissolve
    MC "乖女孩。保持这个姿势。"
    scene img_main32_1092 with dissolve
    "你把绳子从她身下穿过，从她的手臂之间穿过去，再从你已经绑在手腕上的那个结上方跨过……"
    scene img_main32_1093 with dissolve
    "然后整个绕到另一侧。"
    scene img_main32_1094 with dissolve
    "薇琪依旧保持着拱起腰的动作，你重复同样的过程，把绳子的另一端缠在她的另一只脚踝上。"
    scene img_main32_1095 with dissolve
    "大功告成，你往后坐了坐，给她留出空间。"
    MC "你还能动多少？"
    scene img_main32_1096 with dissolve
    "她放松地重新躺回床上，开始试探这副全新束缚的极限……"
    scene img_main32_1097 with dissolve
    "她的活动范围依然不小，想合拢双腿也完全做得到……"
    scene img_main32_1098 with dissolve
    "但这一切都无关紧要，绳子完美地实现了它们的首要目标——让她彻底无能为力。"
    scene img_main32_1099 with dissolve
    Victoria "哦不……我现在完全任人摆布了……主人，我能做的只有躺在背上，任由你处置……"
    scene img_main32_1100 with dissolve
    MC "很好。你就该待在那里。"
    scene img_main32_1101 with dissolve
    "作为回应，她只是把头往后一枕，无所畏惧地笑着。"
    scene img_main32_1102 with dissolve
    "你挪动过去跨坐在她身上，把她被束缚的无助身体进一步钉在床上。"
    scene img_main32_1103 with dissolve
    MC "露西，把她的口球递给我。" 

    scene img_main32_1104 with dissolve
    pause

    scene img_main32_1105 with dissolve
    "她从桌上拿起递给你，眼神里混杂着好奇与畏惧。"
    scene img_main32_1106 with dissolve
    "考虑到薇琪几小时前才亲自挑出这个东西，你二话不说也没去问许可。"
    MC "张嘴。"
    scene img_main32_1107 with dissolve
    "..."
    MC "该死，我现在就想把鸡巴塞进去……"
    scene img_main32_1108 with dissolve
    Victoria "嗯，那你就塞啊。我被绑得结结实实，你什么事都对我做不出来……"
    MC "哈。不行。你只配得上这个口球。露西可以在你面前乖乖给你口交。"
    scene img_main32_1109 with dissolve
    "她夸张地撅起嘴。"
    Victoria "哼。恶霸。"
    scene img_main32_1110 with dissolve
    "你直接把皮带上给她，把球体安置在她张开的、顺从的嘴里，然后在脑后扣紧固定。"
    scene img_main32_1111 with dissolve
    MC "太紧了吗？"
    scene img_main32_1112 with dissolve
    "她摇了摇头，在这副无助的姿态下说不出话来。"
    Victoria "嗯哼……"
    MC "一般来说，有哪里不对你只要告诉我停下就行。但像这样……"
    scene img_main32_1113 with dissolve
    MC "我要你想一个安全用的声音。好吗？"
    scene img_main32_1114 with dissolve
    "她点了点头，然后想了一会儿……"
    scene img_main32_1115 with dissolve
    "最后发出一声略显尖细的『呢——呢』，绝不会和普通的呻吟混淆。"
    MC "完美。我一听到那个声音就会停下，然后解开口球。"
    scene img_main32_1116 with dissolve
    "她又点了点头。"
    MC "那么……该给你下一个惊喜了。"
    scene img_main32_1117 with dissolve
    "她好奇地歪了歪头……"
    scene img_main32_1118 with dissolve
    "但你什么也没解释，只是撑起身体，滑回她的两腿之间。"
    scene img_main32_1119 with dissolve
    "她顺着被束缚的身体看向你，却有一会儿没能意识到你打算做什么。"
    scene img_main32_1120 with dissolve
    "随后，当你俯身靠近她的穴时，你最后看见的是她的眼睛猛然睁大，明白了过来……"
    
    ########################################################################################################
    #The keyboard code for the musical note is ♩ (Alt+9833) or ♪ (Eighth Note): Alt + 13 or Alt + 9834
    #Above may not work, try emoji_font property in renpy, also check if people still get the issue even with new versions

    ##########################################################################################################
    
    scene vid_main32_1 with dissolve
    "而你正好开始第一次用手指与舌头结合，慢慢探索她的穴。"
    Victoria "嗯嗯～～～～"
    scene vid_main32_2 with dissolve
    "初尝这意料之外的口交，她立刻开始轻轻挣扎着束缚；你已经看得出她很喜欢……"
    "但你并不满足，继续下去……"
    scene vid_main32_3 with dissolve
    "竭尽全力用她从未体验过的感觉把她逼疯……"
    Victoria "唔嗯嗯嗯嗯～～～～～～～"
    scene vid_main32_4 with dissolve
    "没过多久，这似乎就几乎让她承受不住了，她隔着口球呻吟起来……"
    Victoria "唔啊嘛哼嗯嗯嗯～～～～～～～"
    scene vid_main32_5 with dissolve
    "终于，你发现快速而不间断地集中刺激她的阴蒂，会让她疯狂地拉扯、挣扎绳索的极限……"
    scene vid_main32_6 with dissolve
    "而她似乎完全不知道该拿自己怎么办，除了承受那股将她感官淹没的强烈快感之外别无选择……"
    scene vid_main32_7 with dissolve
    "..."
    "......"
    scene vid_main32_8 with dissolve
    "你又持续了相当长一段时间，刻意想弄清楚她究竟对什么有反应、什么最能让她发疯……"
    Victoria "唔唔嗯嗯嗯～～～～～～～"
    "然后，毫无预警地……"

    scene img_main32_1121 with dissolve
    "你停下来，用手臂背面擦去脸上滴落的淫液。"
    scene img_main32_1122 with dissolve
    "抬眼看薇琪，只见她仍几乎不明白发生了什么……不明白你已经停了……"
    scene img_main32_1123 with dissolve
    "她看起来像是被雷劈中，因为不过几秒前，她还淹没在爆发式高潮边缘那种夺人心智的极乐之中……"
    MC "好了，轮到露西了。"
    scene img_main32_1124 with dissolve
    Victoria "唔唔唔唔唔唔唔！！"
    "她隔着口球绝望地呻吟，仅凭语气就传达出了难以想象的性渴望。"
    scene img_main32_1125 with dissolve
    "但你只是低头朝她咧嘴一笑。"
    scene img_main32_1126 with dissolve
    MC "我说过，你那句话会让我讨上几个小时。"
    scene img_main32_1127 with dissolve
    Victoria "嗯嗯……嗯嗯……"
    "她可怜地呜咽着，试图用眼神向你求情……"
    scene img_main32_1128 with dissolve
    "可被绑成这副样子，她什么都做不了。她的快感和高潮现在全都由你说了算。"
    scene img_main32_1129 with dissolve
    "你转向露西——你说轮到她是认真的。"
    scene img_main32_1130 with dissolve
    Lucy "我、我吗？真、真的吗？"
    MC "没错。"

    play sound "audio/sounds/clothing.mp3" volume 4.0

    scene img_main32_1131 with dissolve
    "你一边靠近她一边脱下衬衫……"
    scene img_main32_1132 with dissolve
    "然后随手一扔，目光自始至终没有离开她的脸……"
    "她看起来极其不安，不过你怀疑那可能只是紧张。"
    MC "你说过想和我每样都至少试一次，对吧？"
    scene img_main32_1133 with dissolve
    "她立刻点了点头，小小的笑容取代了几分畏惧……"
    scene img_main32_1134 with dissolve
    "随后一言不发地为你张开双腿。"
    MC "乖女孩。"
    scene img_main32_1135 with dissolve
    "你握住她的大腿，把她从床头板上拉开……"
    scene img_main32_1136 with dissolve
    "然后朝在一旁无助旁观的薇琪眨了眨眼——她全身都在为刚刚被你抢走的那次高潮而焦渴……"
    scene vid_main32_9 with dissolve
    "接着你搂住露西宽大的胯，把她的穴拉到自己嘴边。"
    Lucy "啊……嗯嗯～～～"
    scene vid_main32_10 with dissolve
    "就像对维多利亚那样，你一开始放得比较慢，让她习惯这种感觉……"
    scene vid_main32_11 with dissolve
    "接着更大胆一些，试着真正去撩拨她的底线……"
    scene vid_main32_12 with dissolve
    Lucy "嗯啊嗯！！嗯嗯嗯嗯～～～那、那个……"
    MCi "（靠，她真的很吃这一套……）"
    scene vid_main32_13 with dissolve
    "被这个反应鼓舞，你给她颤抖的穴越来越多的关照，急于从这个害羞女孩身上看到更加淫荡的回应……"
    scene vid_main32_14 with dissolve
    "直到，就像薇琪那样，只是这次没有绳子，她在你掌控中扭动挣扎，快感强烈到再也承受不住时失去自控……"
    scene vid_main32_15 with dissolve
    "..."
    "......"
    scene vid_main32_16 with dissolve
    "不过，与薇琪不同，你完全没打算停下……"
    scene vid_main32_17 with dissolve
    Lucy "嗯嗯嗯嗯～～～～～～～～～[PlayerName]！"
    scene vid_main32_18 with dissolve
    Lucy "[PlayerName]！嗯嗯我～～～～～～～[PlayerName]！我、我嗯～～～～～～～"
    scene vid_main32_19 with dissolve
    "她不再受束缚的双手猛地按上你的头顶，抓住你的头发，大腿紧紧夹住你，身体拱起，陷入一次肌肉紧绷、浑身战栗的高潮……"
    Lucy "唔唔唔唔唔唔啊唔唔嗯～～～～～～～～～～～～～～～"
    scene vid_main32_20 with dissolve
    "她甚至失去了对一贯轻柔呻吟的控制，一声纯粹出于野兽般欲望的尖叫喘息从唇间逸出，胯部在你紧握的双手下猛地起伏。"
    scene vid_main32_21 with dissolve
    "..."
    "......"
    scene img_main32_1137 with dissolve
    "终于，在一次漫长而剧烈的释放之后，她的肌肉开始慢慢放松……"
    scene img_main32_1138 with dissolve
    "但仍不时被一波波战栗的余韵袭来，每一次都让她小小地抽气……"
    Lucy "嗯嗯！"
    scene img_main32_1139 with dissolve
    Lucy "啊……嗯呜……嗯哼～～～啊………………"
    scene img_main32_1140 with dissolve
    "直到最后，她彻底瘫软，倒回床垫上，大口喘息。"
    scene img_main32_1141 with dissolve
    MC "乖女孩。"
    scene img_main32_1142 with dissolve
    Lucy "嗯嗯……"
    scene img_main32_1143 with dissolve
    "你又一次把手臂上的唾液在脸上擦干净，然后从边桌上抓过一只震动棒……"
    scene img_main32_1144 with dissolve
    "接着把注意力转回那个被绑住的金发女孩身上……"
    
    play sound "audio/sounds/clothing.mp3" volume 4.0
    
    scene img_main32_1145 with dissolve
    "这一次，在两个女孩之间轮换时，你顺手脱掉了裤子。"
    scene img_main32_1146 with dissolve
    Victoria "唔哼！唔嗯！"
    scene img_main32_1147 with dissolve
    MC "哈，好。轮到你了。"
    scene img_main32_1148 with dissolve
    Victoria "唔嗯！"
    "从她被口球堵住的鼻音里，你猜她想说的是『终于！』，却没能说出口。"

    $ renpy.music.set_volume(0.5, delay=1, channel='sound')
    play sound "audio/sounds/vibrator_low.mp3" volume 4.0 fadein 0.5 loop

    scene vid_main32_22 with dissolve
    "你坐在她两腿之间，随手把震动棒贴上她的穴……"

    $ renpy.music.set_volume(0.7, delay=1, channel='sound')
    scene vid_main32_23 with dissolve
    Victoria "唔嗯嗯～～嗯嗯嗯哼！～～"

    pause

    scene img_main32_1149 with dissolve
    "但你没有看向薇琪，而是把注意力放在还在恢复的露西身上。"
    MC "看来你喜欢刚才那样？"
    scene img_main32_1150 with dissolve
    Lucy "啊，嗯哼！"
    "她笑着点头，可你从她的语气里听出一丝迟疑，与她的表情完全不符。"
    MC "你不喜欢？"
    scene img_main32_1151 with dissolve
    Lucy "啊，我喜欢！非、非常棒……"
    scene img_main32_1152 with dissolve
    Lucy "我、我只是，呃……"
    scene img_main32_1153 with dissolve
    Lucy "该怎么说好呢……"
    scene img_main32_1154 with dissolve
    Lucy "太、太难为情了……我、我觉得你那样做让我太难为情了……"
    scene img_main32_1155 with dissolve
    "她笑着又把目光移开，显然正在肉体快感与内向矜持之间挣扎。"

    scene vid_main32_24 with dissolve
    "你和露西说话时，逐渐把震动棒从薇琪身上移开戏弄她；想获得舒服的接触、想好好感受的话，就得把腰抬得越来越高……"
    scene vid_main32_25 with dissolve
    "最终，当她把腰完全抬离床面时……"
    scene vid_main32_26 with vpunch
    "你又把震动棒往前一推，让它直接而毫不留情地压上她的穴……"
    "让她从刚才对快感的渴求骤然切换过来，惹出一声惊叫……"
    "那种切换后的感觉无处可逃、过于强烈，几乎要把她逼疯，可她又完全无力阻止……"
    scene vid_main32_27 with dissolve
    "但即便如此，你依然继续无视她，把全部主动的关注都给了露西。"

    scene img_main32_1156 with dissolve
    MC "嗯，不过我们可以多来几次，让你习惯……"
    scene img_main32_1157 with dissolve
    Lucy "嗯哼嗯……我还是更喜欢你成为全场的焦点，而不是我。"
    "你耸了耸肩，很高兴她愿意说出自己想要什么——哪怕在这个例子里，这多半是为了你自己。"

    $ renpy.music.set_volume(0.4, delay=1, channel='sound')

    scene vid_main32_28 with dissolve
    "你又戏弄了薇琪一会儿……"

    $ renpy.music.set_volume(0.6, delay=1, channel='sound')

    scene vid_main32_29 with dissolve
    "反复在猛烈的接触与戏弄的间隙之间循环，让她在被戏弄的间隙里拼命追逐那根震动棒……"
    
    $ renpy.music.set_volume(0.9, delay=1, channel='sound')

    scene vid_main32_30 with dissolve
    pause

    $ renpy.music.set_volume(0.8, delay=1, channel='sound')

    scene vid_main32_31 with dissolve
    Victoria "唔嗯嗯～～嗯嗯嗯哼！～～"
    
    $ renpy.music.set_volume(1.0, delay=1, channel='sound')
    play sound "audio/sounds/vibrator_high.mp3" volume 4.0 fadein 0.5 loop
    
    scene vid_main32_32 with dissolve
    "直到最后，你把她一步步推得更远，再次迫使她在接近高潮边缘时挣扎着绳索……"
    scene vid_main32_33 with dissolve
    Victoria "唔唔唔嗯嗯～～～～～～"
    "当你推过一直让她悬在那里的界线时，她因快感而呻吟；那夺人心智的震动每多持续一秒，兴奋就多淹没她一分……"
   
    scene img_main32_1158 with dissolve

    stop sound

    "然后就在她即将体验人生中最棒的高潮前最后一刻，你关掉震动棒并把它移开。"
    scene img_main32_1159 with dissolve
    Victoria "唔唔嗯唔唔唔唔！！！"
    scene img_main32_1160 with dissolve
    "她发出一声哀怨而不平的悲鸣，那被彻底拒绝的感觉再次让她绷紧的身体窜过一阵战栗。"
    scene img_main32_1161 with dissolve
    "露西从刚才的高潮里稍微恢复了一些，抬头看着你爬向她……"
    scene img_main32_1162 with dissolve
    "她脸上浮现出强烈的预感，因为她知道接下来要发生什么……"
    
    $ renpy.music.set_volume(0.6, delay=1, channel='sound')
    play sound "audio/sounds/vibrator_low.mp3" volume 4.0 fadein 0.5 loop

    scene vid_main32_34 with dissolve
    "你跨到她两腿之间，把震动棒抵在她依然敏感的穴上……"

    $ renpy.music.set_volume(0.8, delay=1, channel='sound')

    scene vid_main32_35 with dissolve
    Lucy "啊……嗯嗯～～～"

    $ renpy.music.set_volume(0.6, delay=1, channel='sound')

    scene vid_main32_36 with dissolve
    pause
    scene vid_main32_37 with dissolve
    pause

    $ renpy.music.set_volume(0.7, delay=1, channel='sound')
    play sound "audio/sounds/vibrator_high.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop

    scene vid_main32_38 with dissolve
    "她再次迷失自我，扭动着、呻吟着，你不停继续……"
    "直到最后……"
    scene vid_main32_39 with dissolve
    Lucy "唔唔唔唔唔唔唔啊唔唔嗯～～～～～～！！！"
    "就像上次一样，你把她推入又一次战栗的高潮……"
    "..."
    "......"
    scene img_main32_1163 with dissolve

    stop sound

    "等它终于平息，她已经眼神涣散、气息紊乱。"
    scene img_main32_1164 with dissolve
    Victoria "唔哼。"
    scene img_main32_1165 with dissolve
    "你低头看着那个饥渴而色情的金发女孩，把这当成了她在撅嘴。"

    scene img_main32_1166 with dissolve
    "只给了她最短暂的片刻去意识到正在发生什么，你就把震动棒塞进她的体内，出其不意惹来一声轻哼。"

    scene img_main32_1167 with dissolve
    pause

    scene img_main32_1168 with dissolve
    MC "这还是第一次你的穴和屁股里同时有东西。"
    
    $ renpy.music.set_volume(0.3, delay=1, channel='ambiance')
    play ambiance "audio/sounds/vibrator_low.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop
    
    scene img_main32_1169 with dissolve
    "她点了点头，但当你用遥控器打开震动棒时，眼神却闪躲了一下……"
    scene img_main32_1170 with dissolve
    "不过你只开到低档，刚好足够让她因为想要更多而发狂。"
    scene img_main32_1171 with dissolve
    Victoria "嗯嗯嗯～～～～～～"
    scene img_main32_1172 with dissolve
    "接着，你从桌上抓起第二根震动棒……"
    scene img_main32_1173 with dissolve
    "在露西还没完全消化发生了什么之前，对她做了同样的事。"

    $ renpy.music.set_volume(0.3, delay=1, channel='sound')
    play sound "audio/sounds/vibrator_low.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop

    scene img_main32_1174 with dissolve
    Lucy "唔嗯嗯……"
    scene img_main32_1175 with dissolve
    MC "换位置。我要口交。"
    scene img_main32_1176 with dissolve
    "她点点头，摇摇晃晃地绕到床的另一边，仍未从上次的高潮中完全恢复。"

    scene vid_main32_40 with dissolve
    "她开心地把你的鸡巴从内裤里拉出来，用温暖丝滑的嘴含住顶端。"

    $ renpy.music.set_volume(0.5, delay=1, channel='ambiance')
    play ambiance "audio/sounds/vibrator_high.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop

    scene vid_main32_41 with dissolve
    "与此同时，你坐在那里揉捏薇琪的胸部，偶尔把她的震动棒开到最大，同时捏着她硬如石头的乳头……"
    
    $ renpy.music.set_volume(0.3, delay=1, channel='ambiance')
    play ambiance "audio/sounds/vibrator_low.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop
    
    scene vid_main32_42 with dissolve
    "可等她开始真正感受到时，你又把它调低……"

    $ renpy.music.set_volume(0.6, delay=1, channel='sound')
    play sound "audio/sounds/vibrator_high.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop

    scene vid_main32_43 with dissolve
    "你让露西给你口交了一会儿，她自己那根震动棒此刻也毫不停歇地全功率运转着……"
    pause
    "..."
    "......"
    scene img_main32_1177 with dissolve
    "最后，当你冒险要射在她嘴里时，你让她停下……"
    scene img_main32_1178 with dissolve
    "然后起身去戏弄已经完全被折磨到崩溃的维多利亚。"
    
    scene img_main32_1179 with dissolve
    pause
    
    scene img_main32_1180 with dissolve
    "你低头冲她微笑，吊着她对接下来你要做什么的胃口……"
    scene img_main32_1181 with dissolve
    Victoria "唔哼……"
    scene img_main32_1182 with dissolve
    "等得够久之后，你把手指连同震动棒一起插进她的穴里，惹来一声尖叫。"
    scene img_main32_1183 with dissolve
    Victoria "嗯嗯嗯！"
    scene img_main32_1184 with dissolve
    "你缓缓移动手指，在她体内把震动棒推来推去……"
    scene img_main32_1185 with dissolve
    Victoria "唔唔嗯嗯嗯哼～～～～"
    MC "还记得我们的规则吗？除了射在我的鸡巴上，你不许高潮。"
    scene img_main32_1186 with dissolve
    Victoria "唔唔哼……"
    "这其实并不是一条永久规定，但以她被捆绑、被堵住嘴的状态，她自然也没法争辩。"
    
    $ renpy.music.set_volume(0.75, delay=1, channel='ambiance')
    play ambiance "audio/sounds/vibrator_high.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop
    
    scene img_main32_1187 with dissolve
    "你又用震动棒给了她一次猛烈的爆发……"
    "..."

    stop ambiance

    scene img_main32_1188 with dissolve
    "然后把它拔了出来，于是现在唯一的声响，是露西仍在背景里卖力弄出的动静……"
    scene img_main32_1189 with dissolve
    "接着你移动身体，把鸡巴对准她穴原本的位置。"
    scene img_main32_1190 with dissolve
    "当她意识到即将发生什么时，脸上浮现出期待的神情——至少隔着口球你是这么看出来的。"
    scene img_main32_1191 with dissolve
    MC "准备好了吗？"
    scene img_main32_1192 with dissolve
    "她急切地点头，急不可耐地想让你进去……"
    scene img_main32_1193 with dissolve
    "可你反而又戏弄了她一会儿，用鸡巴头在她穴上上下滑动，就是不给她想要的……"
    
    scene img_main32_1194 with dissolve
    pause
    scene img_main32_1193 with dissolve
    pause
    scene img_main32_1194 with dissolve
    pause
    scene img_main32_1193 with dissolve
    pause  
    
    scene img_main32_1195 with dissolve
    "就像对震动棒一样，她拼命抬起胯想让你进去……"
    scene img_main32_1196 with dissolve
    "但你不断抽离，让满足始终够不着……"
    scene img_main32_1197 with dissolve
    "直到……"
    scene img_main32_1198 with dissolve
    "你用整个身体一气呵成地压下，鸡巴一路滑进她那湿透、饥渴小穴的最深处。"
    scene img_main32_1199 with dissolve
    Victoria "嗯嗯嗯嗯嗯～～～～～～～"
    "你把她撑开、强迫她容纳你的尺寸时，她发出一声畅快的满足呻吟……"
    scene img_main32_1200 with dissolve
    "你等了一会儿，享受着整根没入她体内的感觉……"
    scene img_main32_1201 with dissolve
    "然后在她唇边的声音戛然而止——你放下她的腿，抽身退出……"
    scene img_main32_1202 with dissolve
    "让她感到的空虚，比你插进去之前还要厉害。"
    scene img_main32_1203 with dissolve
    Victoria "唔唔嗯！！！"
    scene img_main32_1204 with dissolve
    "你看见她的眼神变得哀求，用眼神乞求你放她逃出这座你让她深陷的、欲火焚烧的牢笼。"
    "但作为回应，你只是低头微笑，完全不为所动。"
    MC "你想让我给你一次高潮吗？"
    scene img_main32_1205 with dissolve
    "她用力点头。"
    MC "现在？"
    scene img_main32_1206 with dissolve
    Victoria "唔哼！"
    scene img_main32_1207 with dissolve
    MC "哈。我要把这样持续上好几个小时，薇琪。"
    scene img_main32_1208 with dissolve
    Victoria "唔唔嗯！"

    $ renpy.music.set_volume(0.3, delay=1, channel='ambiance')
    play ambiance "audio/sounds/vibrator_low.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop

    scene img_main32_1209 with dissolve
    "你把震动棒重新塞回去，调到低档……"
    scene img_main32_1210 with dissolve
    "然后又一次转向那个黑发女孩。"
    MC "翻过身去，露西。"
    scene img_main32_1211 with dissolve
    "她翻了过来……"

    stop sound

    scene img_main32_1212 with dissolve
    "让你得以把震动棒从她体内抽出——在你戏弄薇琪的这段时间里，它一直在她体内运转……"
    scene img_main32_1213 with dissolve
    "紧接着，你几乎没有任何前奏，就开始在它的位置上进入她的身体。"
    Lucy "唔嗯嗯嗯……"
    scene img_main32_1214 with dissolve
    "整根没入之后，你把她钉在床上，低头望进她的眼睛。"
    scene img_main32_1215 with dissolve
    MC "你要为我再高潮一次，好吗？"

    scene vid_main32_44 with dissolve
    "她仰头顺从地点点头，你开始缓缓把你的鸡巴送进她那个早已被开发、湿淋淋的小洞里。"
    Lucy "唔嗯嗯～～～～～"
    scene vid_main32_45 with dissolve
    "被自己的欲望以及你对两个女孩的把戏双重推着，你很快加大了强度——只要你一觉得露西能承受得住……"
    scene vid_main32_46 with dissolve
    "然后开始狠狠干她……"
    "在这一切铺垫之后，她紧致的小穴夹着你的每一寸鸡巴，来回吞咽窜动，很快你就彻底失去了自我……"
    "与此同时，露西早就忍受震动棒很久了，再加上肛塞还塞在另一个洞里、平添了一层强度……"
    scene vid_main32_47 with dissolve
    "她似乎很快就失去了自控，随着强度变得难以承受而紧紧闭上眼睛……"
    scene vid_main32_48 with dissolve
    Lucy "唔嗯嗯～～～～～[PlayerName]！"
    scene vid_main32_49 with dissolve  
    Lucy "唔唔嗯嗯～～～～～唔唔嗯嗯～～～～～唔唔嗯嗯～～～～～"
    "当你的鸡巴抵住她的子宫、而她的身体开始在你周围痉挛时，这份感觉就足以让你越过临界点……"
    scene vid_main32_50 with dissolve  
    "你们彼此的身体都在回应对方，当露西感觉到你开始在她体内爆射时，两人同时爆发出高潮。"
    Lucy "唔唔唔唔唔唔嗯嗯～～～～～！！！"
    "电流般的感觉窜上你的脊背，全身每一块肌肉同时收缩，你的视野有一瞬变得空白……"
    
    scene img_main32_1216 with flash
    "随后，你的大脑重新启动，却依旧整根埋在露西痉挛的身体里，在这场猛烈高潮的余韵中眨着眼睛。"
    
    scene img_main32_1216 with flash
    pause
    scene img_main32_1216 with flash
    pause
    scene img_main32_1216 with flash
    pause

    scene img_main32_1217 with dissolve
    "过了几秒，你终于恢复到足以思考计划下一步的程度……"
    scene img_main32_1218 with dissolve
    "你把你那根湿滑的鸡巴从露西被过度刺激、灌满精液的洞里抽了出来……"
    scene img_main32_1219 with dissolve
    "又一次在两个女孩之间切换。"

    scene img_main32_1220 with dissolve
    pause
    scene img_main32_1221 with dissolve
    pause

    scene img_main32_1222 with dissolve
    Victoria "嗯……？"
    scene img_main32_1223 with dissolve
    "当你伸手去解她的口球时，她看起来相当意外。"
    scene img_main32_1224 with dissolve
    Victoria "啊啊啊！主、主人，你、你——"
    scene img_main32_1225 with dissolve
    "你挪动身体把鸡巴摆到她嘴前时，她试图把一句话说出来……"
    scene img_main32_1226 with dissolve
    Victoria "唔嗯……"
    "可还没等她说上几个字，不用你吩咐，她就自然地开始吮吸送到嘴前的那团狼藉……"
    scene img_main32_1227 with dissolve
    "你本来只想让她帮你清理干净，可她对你刚刚射过的鸡巴突然而用力地吮吸，有点过了头……"
    scene img_main32_1228 with flash
    "你发现那股感觉冲击着你的感官，让你几乎撑不住身体。"
    scene img_main32_1229 with flash
    MC "喂，女人！是擦干净，不是吮。"
    scene img_main32_1230 with dissolve
    Victoria "嗯哼……"
    scene img_main32_1231 with dissolve
    "她顺从地照做，开始用舌头清理你逐渐软下去的鸡巴上残留的体液……"
    scene img_main32_1232 with fade
    MC "乖女孩。"
    scene img_main32_1233 with fade
    "等她弄完，你把口球重新扣好……"
    scene img_main32_1234 with dissolve
    "然后瘫坐在两人中间，短暂休息……"
    Victoria "唔嗯嗯……"
    scene img_main32_1235 with dissolve
    MC "过来，露西。"
    scene img_main32_1236 with dissolve
    "终于结束第三次高潮的她撑起身来到你身旁，依偎进你的怀里。"   
    scene img_main32_1237 with dissolve
    Lucy "唔哼嗯……刚、刚才那下……我脑子还在转……"
    scene img_main32_1238 with dissolve
    MC "哈，可我们还没完呢。"
    scene img_main32_1239 with dissolve
    Lucy "啊，真、真的吗？"
    MC "真的。"
    scene img_main32_1240 with fade
    "你说到做到，接下来一个小时都在戏弄两个女孩……"

    scene img_main32_1241 with fade
    pause

    scene img_main32_1242 with fade
    "反复把维多利亚逼到高潮边缘，却永远不让她完成……"
    
    $ renpy.music.set_volume(0.6, delay=1, channel='ambiance')
    play ambiance "audio/sounds/vibrator_high.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop
    
    scene img_main32_1243 with fade
    "让她越来越迷失在一片快感的红雾中，开始分不清你什么时候在戏弄她、什么时候没有……"
        
    scene img_main32_1244 with fade
    "最后发展到你最轻微的一点触碰，都足以让她过度紧绷的身体窜过一阵战栗——像一根被囚禁的弹簧，拼命想释放能量却完全做不到。"
    
    $ renpy.music.set_volume(0.3, delay=1, channel='ambiance')
    play ambiance "audio/sounds/vibrator_low.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop

    scene img_main32_1245 with fade
    pause

    scene img_main32_1246 with fade
    pause

    scene img_main32_1247 with fade
    "与此同时，露西被你逼着又高潮了两次……不过越来越难达到，也越来越不强烈，她那被压垮的身体疲惫不堪、一无所有……"
    
    scene img_main32_1248 with fade
    "她用最后的力气翻身四肢着地，好让你用一个她从未体验过的姿势操她……"
    
    scene img_main32_1249 with fade
    pause
    scene img_main32_1250 with fade
    pause
    
    scene img_main32_1251 with fade
    "然后把第二股精液射进她体内，麻木而欣喜。"

    scene img_main32_1252 with fade
    "你刚从那阵中缓过来，就立刻回头继续戏弄薇琪……"

    $ renpy.music.set_volume(0.6, delay=1, channel='ambiance')

    scene img_main32_1253 with fade
    "你在操露西时给她的短暂喘息，让她在你重新把她折磨到浑身颤抖时，不由自主地剧烈战栗起来……"
    
    $ renpy.music.set_volume(0.7, delay=1, channel='ambiance')
    play ambiance "audio/sounds/vibrator_high.mp3" volume 4.0 fadein 0.5 fadeout 0.5 loop
    
    scene img_main32_1254 with fade
    "等你戏弄得够久、自己也恢复得足以进行最终章时，你怀疑她就算没有口球恐怕也拼不出一句完整的话了。"

    stop ambiance
    $ renpy.music.set_volume(1.0, delay=1, channel='ambiance')
    $ renpy.music.set_volume(1.0, delay=1, channel='sound')

    scene vid_main32_51 with dissolve
    "准备好了，你干脆利落地把震动棒从她体内拔出，然后一言不发地再次俯身下去……"
    "她那被戏弄得湿淋淋、被剥夺了高潮的穴，第二次几乎承受不住这种强度，从一开始就扭动起来、呻吟起来。"
    scene vid_main32_52 with dissolve
    Victoria "嗯嗯嗯嗯嗯～～～～～～～"
    "..."
    "......"
    scene img_main32_1255 with fade
    "但这一次，当你停下并抽身后，你没给她片刻去体会那份落空……"
    scene vid_main32_53 with dissolve
    "你把鸡巴猛地插进她紧致的小穴，把所有戏弄的念头都抛到脑后，只剩一个念头：把她的脑子操出来。"
    scene vid_main32_54 with dissolve
    Victoria "嗯嗯嗯嗯嗯～～～～～～～"
    scene vid_main32_55 with dissolve
    "你什么也没说，很快就加大力度、略显粗暴地干她——正是她喜欢的方式……"
    scene vid_main32_56 with dissolve
    Victoria "唔唔嗯嗯唔唔嗯～～～～～"
    "在被无休止地戏弄了这么久之后，她其实花了很长时间才到达彻底高潮……比一小时前你就让她射出来的话，要久得多……"
    "取而代之的，她进入了一种持续的、翻涌的快感状态，持续得久得多、久得多……"
    "每一次挺进她的身体，都会伴随着她体内不由自主的收缩，那阵阵涟漪紧紧裹住你的鸡巴……"
    scene vid_main32_57 with dissolve
    "而你瞥一眼她的脸，就看到她正拼命维持神智清明，一波又一波无尽的肉体快感在她体内横冲直撞……"
    "直到，终于，在漫长的等待之后……"
    scene vid_main32_58 with flash
    Victoria "唔唔唔唔唔唔唔唔唔唔唔唔唔～～～～～～！！！！！"
    "当你推过以往每一次都会停下的界线时，她隔着口球尖叫起来……"
    "而积压了十二次焦渴高潮的全部力量，在这一刻一次性全部命中了她……"
    Victoria "唔唔唔唔唔唔唔啊哦哦哦哦唔唔唔唔～～～～～～～～！！！"
    "与此同时，这也完全足以把你推入今晚的第三次高潮……"
    "你在失去控制、给出与露西那份相配的内射时，不由自主地抓紧了床头板……"
    "..."
    "......"
    scene img_main32_1256 with dissolve
    "直到最后，你的肌肉终于放松到足以把鸡巴从维多利亚颤抖的身体里拔出来。"
    scene img_main32_1257 with dissolve
    "你让自己半跌回她的两腿之间，花了好长一会儿才喘匀气……"
    scene img_main32_1258 with dissolve
    "然后再一次回到两个女孩中间坐下，彻底精疲力竭。"

    $ renpy.end_replay()