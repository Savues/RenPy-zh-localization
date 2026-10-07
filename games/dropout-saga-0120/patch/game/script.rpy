# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



default name = "琉克"
define l = Character("洛莉",color = "#B480DF", who_outlines=[ (2, "#000000") ], what_outlines=[ (2, "#000000") ])
define r1 = Character("[name]",color = "#007FFF")
define r2 = Character("[name]",color = "#CC0000")
define john = Character("约翰",color = "#CC0000")
define k = Character("凯恩",color = "#8DB600")
define ash = Character("阿什莉",color = "#8DB600")
define asu = Character("亚苏娜",color = "#e72bed")
define ja = Character("贾丝敏", color = "#E9D66B")
define ju = Character("朱莉", color = "#8dab29")
define ch = Character("巧琪",color = "#8DB600")
define lila = Character("莱拉",color = "#FF007F")
define sophia = Character("索菲娅",color = "#FF007F")
define ingrid = Character("英格丽",color = "#FF007F")
define isa = Character("伊莎贝拉",color = "#FF007F")
define hina = Character("希娜",color = "#FF007F")
define kayle = Character("凯尔",color = "#FF007F")
define tom = Character("汤姆", color = "#E9D66B")
define lara = Character("拉拉", color = "#FF007F")
define ava = Character("艾娃",color = "#FF007F")
define peter = Character("彼得",color = "#96FF33")
define grace = Character("格雷丝",color = "#FF007F")
define jen = Character("珍妮弗",color = "#FF007F")
define mika = Character("米卡",color = "#FF007F")
define nor = Character("诺曼", color = "#E9D66B")
define gui.dialogue_text_outlines = [ (2, "#000000", 0, 0) ]
define gui.name_text_outlines = [ (2, "#000000", 0, 0) ]


#Texting Characters

# NVL characters are used for the phone texting
define r1_nvl = Character("[r1]", kind=nvl, callback=Phone_SendSound, who_outlines=[ (0, "#000000") ], what_outlines=[ (0, "#000000")], what_font="Fonts/MiSans-Regular.ttf")
define l_nvl = Character("[l]", kind=nvl, callback=Phone_ReceiveSound, who_outlines=[ (0, "#000000") ], what_outlines=[ (0, "#000000") ], what_font="Fonts/MiSans-Regular.ttf")
define lila_nvl = Character("[lila]", kind=nvl, callback=Phone_ReceiveSound, who_outlines=[ (0, "#000000") ], what_outlines=[ (0, "#000000") ], what_font="Fonts/MiSans-Regular.ttf")
define ja_nvl = Character("[ja]", kind=nvl, callback=Phone_ReceiveSound, who_outlines=[ (0, "#000000") ], what_outlines=[ (0, "#000000") ], what_font="Fonts/MiSans-Regular.ttf")
define asu_nvl = Character("[asu]", kind=nvl, callback=Phone_ReceiveSound, who_outlines=[ (0, "#000000") ], what_outlines=[ (0, "#000000") ], what_font="Fonts/MiSans-Regular.ttf")
define sophia_nvl = Character("[sophia]", kind=nvl, callback=Phone_ReceiveSound, who_outlines=[ (0, "#000000") ], what_outlines=[ (0, "#000000") ], what_font="Fonts/MiSans-Regular.ttf")
define isa_nvl = Character("[isa]", kind=nvl, callback=Phone_ReceiveSound, who_outlines=[ (0, "#000000") ], what_outlines=[ (0, "#000000") ], what_font="Fonts/MiSans-Regular.ttf")

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

####

default patreoncode = "lbthx"
default patreoncheck = ""
default patreon = False

default gallery_normal_1 = False

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define redbulb = Fade(0.2, 0.0, 0.8, color='#ff0000')

default corruption = 0
default goodness = 0
default cash = 0

default screen_tooltip = ""


#School
default popularity = 0
default reputation = 0
default discipline = 0
default grades = 60
default fear = 0
default tempo = 8
default dayweek = 6
default daymonth = 1
default month = 1
default daytext = ""
default monthtext = ""
default chance = 0

default class_tutorial1 = False

default lila_text = False
default lila_office = False
default lila_coach_you = False
default lila_winning_chance = 0
default event_lila = 0
default love_lila = 0
default text_lila = 0
default corruption_lila = 0
default inhibition_lila = 100
default love_lila_blocked = False
default pregnancy_chance_lila = 0

default day = 0
default day_control_lila = 0
default day_control_ashley = 0

default ash_office = False
default ash_text = False
default event_ash = 0
default love_ash = 0
default text_ash = 0
default corruption_ash = 0
default pregnancy_chance_ash = 0

default asuna_office = False
default asuna_text = False
default event_asuna = 0
default love_asuna = 0
default corruption_asuna = 0
default text_asuna = 0
default pregnancy_chance_asu = 0

default jas_office = False
default jas_text = False
default event_jas = 0
default love_jas = 0
default corruption_jas = 0
default text_jas = 0
default infirmary_jas = True
default pregnancy_chance_jas = 0

default ju_office = False
default ju_text = False
default event_ju = 0
default love_ju = 0
default corruption_ju = 0
default text_ju = 0
default pregnancy_chance_ju = 0

##########STAFF

default isa_office = False
default isa_text = False
default event_isa = 0
default love_isa = 0
default corruption_isa = 0
default text_isa = 0
default loyalty_isa = 0
default pregnancy_chance_isa = 0

default lara_office = False
default lara_text = False
default event_lara = 0
default love_lara = 0
default corruption_lara = 0
default text_lara = 0
default loyalty_lara = 0

default lori_office = False
default lori_text = False
default event_lori = 0
default love_lori = 0
default corruption_lori = 0
default text_lori = 0
default loyalty_lori = 0

default hina_office = False
default hina_text = False
default event_hina = 0
default love_hina = 0
default corruption_hina = 0
default text_hina = 0
default loyalty_hina = 0

###OUTSIDE COLLEGE

default ava_trigger = False
default ava_office = False
default ava_text = True
default event_ava = 0
default talk_ava = 0
default love_ava = 0
default corruption_ava = 0
default inibition_ava = 100
default pregnancy_chance_ava = 0
default nickname_ava1 = "亲爱的"

default sophia_office = False
default sophia_text = True
default event_sophia = 0
default talk_sophia = 0
default love_sophia = 50
default corruption_sophia = 0
default inibition_sophia = 100
default pregnancy_chance_sophia = 0
default nickname_sophia1 = "亲爱的"

default ingrid_alive = False
default ingrid_office = False
default ingrid_text = True
default event_ingrid = 0
default talk_ingrid = 0
default love_ingrid = -30
default corruption_ingrid = 0
default inibition_ingrid = 100
default nickname_ingrid1 = "亲爱的"

default grace_office = False
default grace_text = True
default event_grace = 0
default talk_grace = 0
default love_grace = -30
default corruption_grace = 0
default inibition_grace = 100
default nickname_grace1 = ""



###FACTIONS REP
default newcomers = 0
default newcomers_power = 0

default wolfpack = 30
default wolfpack_power = 35

default russians = -30
default russians_power = 40


default germans = -15
default germans_power = 0

default police = 0
default police_power = 75

default herd = -30
default herd_power = 45

default civilians = 0

default minorfactions = 0


#### PROGRAM SETUP
define persistent.dialogueBoxOpacity = 1.0
image logo = "logo.webp"

#####

#### ANIM SETUP
image intro1 = Movie(play = "intro1.webm", image = "intro1_1.png", loop = False)
 

# The game starts here.

label splashscreen:
    scene black with dissolve
    pause (3)
    show logo with dissolve
    pause
    scene black with dissolve
    pause (3)
    return
# The game starts here.

label start:
    $ renpy.music.set_volume(0.3, channel='soundlow')
    scene black with Dissolve (3)
    $name = renpy.input("你叫什么名字？")
    $name = name.strip()
    if name == "":
        $name = "琉克"
    "你玩过序章了吗？"
    menu:
        "是。":
            "要回顾一下你之前的选择吗？"
            menu:
                "是。":
                    jump recapitulate
                "否。":
                    jump recapitulate_random
        "否。":
            "想看看你在序章中本可以做出的其他选择吗？"
            menu:
                "是。":
                    jump recapitulate
                "否。":
                    jump recapitulate_random
        

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    label recapitulate:
        scene intro1_1
        with Dissolve (1)
        "第一次见到{color=#FF007F}[lila]{/color}时，你是吓了她，还是安慰了她？"
        menu:
            "我吓了她。{p=0.0}{color=#ff0000}([lila] 堕落 +1){/color}":
                $corruption_lila +=1
            "我安慰了她。{p=0.0}{color=#00ff00}([lila] 好感 +1){/color}":
                $love_lila +=1
        scene black
        with Dissolve (1)
        scene intro2_1
        with Dissolve (1)
        "你保守了{color=#FF007F}[ash]{/color}的秘密，还是以此向她索取了什么？"
        menu:
            "我拿这个秘密向她索取了东西。{p=0.0}{color=#ff0000}([ash] 堕落 +1){/color}":
                $corruption_ash +=1
            "我保护了她。{p=0.0}{color=#00ff00}([ash] 好感 +1){/color}":
                $love_ash +=1
        scene black
        with Dissolve (1)
        scene intro3_1
        with Dissolve (1)
        "你收集到了{color=#FF007F}[lila]{/color}的男友吸毒的证据吗？"
        menu:
            "收集到了。{p=0.0}{color=#ff0000}([lila] 堕落 +1){/color}":
                $corruption_lila +=1
            "没有。{p=0.0}{color=#00ff00}([lila] 好感 +1){/color}":
                $love_lila +=1
        scene black
        with Dissolve (1)
        scene intro4_1
        with Dissolve (1)
        "游泳比赛时，你赢了{color=#FF007F}[lila]{/color}吗？"
        menu:
            "赢了。{p=0.0}{color=#00ff00}(纪律 +5){/color}":
                $discipline +=5
            "没有。{p=0.0}{color=#00ff00}([lila] 好感 +1){/color}":
                $love_lila +=1
        scene black
        with Dissolve (1)
        scene intro5_1
        with Dissolve (1)
        "在{color=#FF007F}[ava]{/color}撞到头之后，你悉心照料她，把她安全带回了自己家。她当时神志还很混乱，却邀请你和她同床而眠。你是上了床，还是尊重了她的状况？"
        menu:
            "我上了她的床。{p=0.0}{color=#ff0000}([ava] 堕落 +1){/color}":
                $corruption_ava +=1
            "我尊重了她的意愿。{p=0.0}{color=#00ff00}(善良 +1){/color}":
                $goodness +=1
        scene black
        with Dissolve (1)
        scene intro6_1
        with Dissolve (1)
        "眼看酒吧里的事态就要失控，{color=#FF007F}[sophia]{/color}一把拉住{color=#FF007F}[ava]{/color}的手臂，想赶在她卷进来帮你之前先把她带走。就在这时，{color=#FF007F}[ava]{/color}撞上了一个喝醉的混混。"
        "{color=#FF007F}[sophia]{/color}想要道歉，以免引人注意，却被那人一巴掌扇在嘴上，打得嘴角渗血。看到这一幕，你胸中怒火与肾上腺素猛然上涌，体内的另一个自己短暂地接管了身体。"
        "你挥拳打在他脸上。然后又是一拳，再一拳，直到他被打晕过去。{color=#FF007F}[sophia]{/color}死死抱住你，不让你再当着{color=#FF007F}[ava]{/color}的面殴打那个昏倒的男人。你夺回了身体的控制权，还是任由残暴支配了自己？" 
        menu:
            "我继续殴打那个男人。{p=0.0}{color=#ff0000}(善良 -1){/color}":
                $goodness -=1
            "我夺回了身体的控制权。{p=0.0}{color=#00ff00}(善良 +1){/color}":
                $goodness +=1
        scene black
        with Dissolve (1)
        scene intro7_1
        with Dissolve (1)
        "你有叫醒{color=#FF007F}[ava]{/color}，为酒吧里那场暴力向她道歉吗？"
        menu:
            "有。":
                $love_ava +=1
            "我决定让她继续睡。":
                pause 0.01
        scene black
        with Dissolve (1)
        scene intro8_1
        with Dissolve (1)
        "趁她们还在睡，你决定给{color=#FF007F}[ava]{/color}和{color=#FF007F}[sophia]{/color}做早餐吗？"
        menu:
            "做了。":
                $love_ava +=1
                $love_sophia +=1
            "我还有更重要的事要做。":
                pause 0.01
        scene black
        with Dissolve (1)
        scene intro9_1
        with Dissolve (1)
        "你上班前，{color=#FF007F}[ava]{/color}有没有跑下楼来吻你？"
        menu:
            "有。":
                $love_ava +=1
            "没有。":
                pause 0.01
        scene black
        with Dissolve (1)
        scene intro10_1
        with Dissolve (1)
        "你在医务室里说服{color=#FF007F}[ja]{/color}和你说话了吗？"
        menu:
            "说服了。":
                $love_jas +=1
                $infirmary_jas = True
            "我给了她独处的空间。":
                pause 0.01
                $infirmary_jas = False
        scene black
        with Dissolve (1)
        scene intro11_1
        with Dissolve (1)
        "你们第一次单独出去时，你吓到{color=#FF007F}[lila]{/color}了吗？"
        menu:
            "吓到了。{p=0.0}{color=#ff0000}([lila] 堕落 +1){/color}":
                $corruption_lila +=1
            "我告诉她，跟我在一起很安全。{p=0.0}{color=#00ff00}([lila] 好感 +1){/color}":
                $love_lila +=1
        scene black
        with Dissolve (1)
        scene intro12_1
        with Dissolve (1)
        "你打听过{color=#FF007F}[ash]{/color}、{color=#FF007F}[asu]{/color}或{color=#FF007F}[ja]{/color}的情况吗？"
        menu:
            "阿什莉。{p=0.0}{color=#00ff00}([ash] 好感 +1){/color}":
                $love_ash +=1
            "亚苏娜。{p=0.0}{color=#00ff00}([asu] 好感 +1){/color}":
                $love_asuna +=1
            "贾丝敏。{p=0.0}{color=#00ff00}([ja] 好感 +1){/color}":
                $love_jas +=1
        scene black
        with Dissolve (1)
        scene intro13_1
        with Dissolve (1)
        $nickname_sophia1 = renpy.input("[sophia]是怎么称呼你的？")
        $nickname_sophia1 = nickname_sophia1.strip()
        if nickname_sophia1 == "":
            $nickname_sophia1 = "darling"
        scene black
        with Dissolve (1)
        scene intro14_1
        with Dissolve (1)
        $nickname_ava1 = renpy.input("[ava]是怎么称呼你的？")
        $nickname_ava1 = nickname_ava1.strip()
        if nickname_ava1 == "":
            $nickname_ava1 = str(r1)
        scene black
        with Dissolve (1)
        scene intro15_1
        with Dissolve (1)
        "面对{color=#FF007F}[ja]{/color}时，你是强势相逼，还是温和相待？"
        menu:
            "强势。{p=0.0}{color=#ff0000}([ja] 堕落 +1){/color}":
                $corruption_jas +=1
            "温和。{p=0.0}{color=#00ff00}([ja] 好感 +1){/color}":
                $love_jas +=1
        scene black
        with Dissolve (1)
        scene intro16_1
        with Dissolve (1)
        "到最后，她是因为待在你身边而开心，还是被你束缚得喘不过气？"
        menu:
            "被束缚。{p=0.0}{color=#ff0000}([ja] 堕落 +1){/color}":
                $corruption_jas +=1
            "很开心。{p=0.0}{color=#00ff00}([ja] 好感 +1){/color}":
                $love_jas +=1
        scene black
        with Dissolve (1)
        scene intro17_1
        with Dissolve (1)
        "在[ava]就睡在你身边的时候，你有没有上{color=#FF007F}[sophia]{/color}？"
        menu:
            "上了。{p=0.0}{color=#ff0000}([sophia] 堕落 +1){/color}":
                $corruption_sophia +=1
            "没有。":
                pause 0.01
        scene black
        with Dissolve (1)
        scene intro18_1
        with Dissolve (1)
        "警察要进入校区时，你是坚持阻拦，还是放他们进来？"
        menu:
            "我拒绝让他们进来。{p=0.0}{color=#00ff00}(学院声望与人气 +1){/color}":
                $reputation+=1
                $popularity+=1
            "我把他们带去了我的办公室。{p=0.0}{color=#00ff00}(警方关系 +1){/color}":
                $police+=1
        scene black
        with Dissolve (1)
        scene intro19_1
        with Dissolve (1)
        "撞见{color=#FF007F}[ja]{/color}抽烟时，你把烟从她手里拿走了吗？"
        menu:
            "最后还是还给了她。{p=0.0}{color=#ff0000}([ja] 堕落 +1){/color}":
                $corruption_jas +=1
            "我把烟从她手里拿走了。{p=0.0}{color=#00ff00}([ja] 好感 +1){/color}":
                $love_jas +=1
        scene black
        with Dissolve (1)
        scene intro20_1
        with Dissolve (1)
        "你是允许{color=#FF007F}[ash]{/color}随时给你发短信，还是告诉她只有得到你的许可才可以？"
        menu:
            "我给了她许可。{p=0.0}{color=#00ff00}([ash] 好感 +1){/color}":
                $love_ash +=1
            "我拿「让她乖乖听我的」开了个玩笑。{p=0.0}{color=#ff0000}([ash] 堕落 +1){/color}":
                $corruption_ash +=1
        
    label intro_sta:    
        scene black
        with Dissolve (3)
        pause (3)
        scene disclaimer
        with Dissolve (2)
        pause
        scene black
        with Dissolve (3)
        pause 0.5
        play music "audio/youshook2.ogg" volume 0.65
        #play music "audio/miles.ogg"
        pause (2)
        scene prologue1
        with dissolve
        r1 "[sophia]？"
        scene prologue2
        with dissolve
        sophia "回镇上了，亲爱的？"
        sophia "连个电话都不打给我？"
        scene prologue3
        with dissolve
        sophia "怎么，不打算请我进去？"
        play sound "audio/Flash.ogg"
        scene prologue4
        with flashbulb
        sophia "我们能聊聊这地方从我们离开那天起就没变过吗？"
        scene prologue5
        with dissolve
        sophia "我是说，简直就是……"
        scene prologue6
        with dissolve
        sophia "什……？"
        r1 "什么……？"
        scene prologue7
        with dissolve
        pause
        scene prologue8
        with dissolve
        pause
        scene prologue9
        with dissolve
        sophia "搞什么鬼……"
        sophia "我可太想这张床了。"
        play sound "audio/Flash.ogg"
        scene prologue10
        with flashbulb
        k "{i}不过这次会有个自由职业者跟着你……{/i}"
        scene prologue11
        with dissolve
        r1 "{i}自由职业者可可靠不了，[k]。他们只忠于出价最高的人。{/i}"
        scene prologue10
        with dissolve
        k "{i}可惜这正是俄罗斯人无法接受的条件。他们要一个……「中立」的人物参与这次交易，所以你得留心看着她。{/i}"
        scene prologue11
        with dissolve
        r1 "{i}'Her'?.{/i}"
        scene prologue12
        with hpunch
        sophia "{i}好了，[k]，我回来了。我们刚说到哪儿？哦对，我待会儿要合作的那个家伙。{/i}"
        scene prologue13
        with dissolve
        sophia "{i}就是他吗？{/i}"
        scene prologue14
        with dissolve
        sophia "{i}哇，靠！这是咖啡？你给我弄的？{/i}"
        scene prologue15
        with dissolve
        sophia "{i}我快渴死了！{/i}"
        scene prologue16
        with dissolve
        r1 "{i}...{/i}"
        scene prologue17
        with dissolve
        r1 "{i}你逗我呢，[k]？{/i}"
        scene prologue18
        with dissolve
        k "{i}[name]……来，见过[sophia]！{/i}"
        scene prologue19
        with dissolve
        pause
        scene prologue20
        with dissolve
        pause
        scene prologue21
        with dissolve
        sophia "{i}很高兴认识你！{/i}"
        scene prologue22
        with dissolve
        sophia "{i}这咖啡真不错，[k]！{/i}"
        scene prologue23
        with Dissolve (1)
        r1 "{i}...{/i}"
        scene prologue24
        with Dissolve (1)
        r1 "{i}我的老天……{/i}"
        scene prologue25
        play sound "audio/Flash.ogg"
        with flashbulb
        sophia "{i}我还以为你们都是那种「嘿，这是我的地盘，我说了算，我想要什么就拿什么」的派头呢。{/i}"
        scene prologue26
        with Dissolve (1)
        sophia "{i}就是这种派头！{/i}"
        sophia "{i}没想到你们还真会租车啊！{/i}"
        r1 "{i}...{/i}"
        r1 "{i}我们不是黑帮。而且我们绝不会说「哟」。{/i}"
        r1 "{i}租车比较不引人注目。{/i}"
        sophia "{i}这是你的主意还是[k]的？{/i}"
        r1 "{i}Mine.{/i}"
        scene prologue27
        with Dissolve (1)
        sophia "{i}看来你比我以为的机灵。{/i}"
        scene prologue28
        with Dissolve (1)
        pause
        scene prologue29
        with Dissolve (1)
        pause
        scene prologue30
        with Dissolve (1)
        pause
        play sound "audio/Flash.ogg"
        scene prologue31
        with flashbulb
        pause
        scene prologue32
        with Dissolve (1)
        "俄罗斯人" "{i}我猜一切都按计划进行，对吧？{/i}"
        scene prologue33
        with Dissolve (1)
        sophia "{i}嗯。那家伙是行家。没有目击者，干得很干净。{/i}"
        "俄罗斯人" "{i}要我数一下钱吗？{/i}"
        sophia "{i}你数也行。不过我向你保证，一分不少。{/i}"
        "俄罗斯人" "{i}很好。很好。{/i}"
        scene prologue34
        with Dissolve (1)
        "俄罗斯人" "{i}但还是照之前说好的。这活儿要「无人目击」。{/i}"
        scene prologue35
        with Dissolve (1)
        sophia "{i}你是在逗我？我刚说了，根本没有目——{/i}"
        scene prologue36
        with hpunch
        sophia "{i}你到底想干……{/i}"
        scene prologue37
        with hpunch
        pause
        scene black
        play sound "audio/gunshot1.ogg"
        pause
        scene prologue38
        with Dissolve (3)
        sophia "{i}你看，那棵树上有鸟！{/i}"
        scene prologue39
        with Dissolve (1)
        sophia "{i}这一带我可太野了！{/i}"
        sophia "{i}这里的一切都太美了！{/i}"
        scene prologue40
        with Dissolve (1)
        sophia "{i}你以前怎么从来不带我来这种地方？！{/i}"
        r1 "{i}嗯……我们都需要点清静。我小时候心情不好就会来这里冷静一下。{/i}"
        r1 "{i}我想对你应该也一样管用。{/i}"
        scene prologue41
        with Dissolve (1)
        sophia "{i}谢谢你，亲爱的。我们真的需要——{/i}"
        scene prologue42
        with hpunch
        sophia "{i}PEEEEEEEACE{/i}"
        play sound "audio/watersplash.ogg"
        scene prologue43
        with hpunch
        pause
        scene prologue44
        with Dissolve (1)
        ingrid "{i}ICH BIN DER KÖNIG DES HÜGELS！{p=0.0}(我是山头之王！){/i}"
        scene prologue45
        with Dissolve (1)
        pause
        scene prologue46
        with Dissolve (1)
        ingrid "{i}亲爱的，你没事吧？{/i}"
        play sound "audio/sophiagasp.ogg"
        scene prologue47
        pause
        scene prologue48
        with hpunch
        sophia "{i}我的老天爷啊！{/i}"
        scene prologue49
        with Dissolve (1)
        sophia "{i}搞什么鬼，[ingrid]！别再把我往这该死的水里推了！{/i}"
        scene prologue50
        with Dissolve (1)
        pause
        scene prologue51
        with Dissolve (1)
        pause
        scene prologue52
        with Dissolve (1)
        pause
        scene prologue53
        with Dissolve (1)
        ingrid "{i}Vhy 你俩为什么那样互相看着对方？{/i}"
        r1 "我觉得是有人把啤酒瓶掉进水里了。"
        scene prologue54
        with Dissolve (1)
        ingrid "{i}Barbarians!{/i}"
        scene prologue55
        with Dissolve (1)
        ingrid "{i}Vhere 在哪儿？我要把那东西砸到他们脸上！{/i}"
        scene prologue56
        with Dissolve (1)
        ingrid "{i}我什么都看不见。{/i}"
        scene prologue57
        with hpunch
        pause
        play sound "audio/watersplash.ogg"
        scene prologue58
        with hpunch
        pause
        play sound "audio/Flash.ogg"
        scene prologue59
        with flashbulb
        sophia "{i}*抽泣着* 他们把她杀了！{/i}"
        scene prologue60
        with Dissolve (1)
        sophia "{i}他们把她杀了！{/i}"
        scene prologue61
        with Dissolve (1)
        pause
        scene prologue62
        with Dissolve (1)
        pause
        scene prologue63
        with Dissolve (1)
        pause
        play sound "audio/Flash.ogg"
        scene prologue64
        with flashbulb
        pause
        scene prologue65
        with Dissolve (1)
        pause
        scene prologue66
        with Dissolve (1)
        pause
        play sound "audio/Flash.ogg"
        scene prologue67
        with flashbulb
        pause
        scene prologue68
        with Dissolve (1)
        k "{i}*开着免提* 你最好离开一阵子，[r1]。{/i}"
        k "{i}*开着免提* 剩下的交给我们。{/i}"
        scene prologue69
        with Dissolve (1)
        r1 "{i}把他们开的头做完，我再去休息。{/i}"
        scene prologue68
        with Dissolve (1)
        k "{i}*开着免提* 兄弟，有件事我得告诉你。{/i}"
        k "{i}*开着免提* 狼群里有些头领开始担心你了。{/i}"
        scene prologue70
        with Dissolve (1)
        k "{i}*开着免提* 你做什么都没用。他们设下埋伏动了她。{/i}"
        k "{i}*开着免提* 你又不可能预知会发生什么。{/i}"
        k "{i}*开着免提* 你得放下。{/i}"
        scene prologue71
        with Dissolve (1)
        k "{i}*开着免提* 你上一次睡觉是什么时候？{/i}"
        play sound "audio/Flash.ogg"
        scene prologue72
        with flashbulb
        k "{i}搞什么，[r1]？{/i}"
        k "{i}你为什么不叫支援？{/i}"
        scene prologue73
        with Dissolve (1)
        r2 "{i}不需要。{/i}"
        scene prologue74
        with Dissolve (1)
        k "{i}那三个都是你一个人解决的？{/i}"
        scene prologue73
        with Dissolve (1)
        r2 "{i}楼上还有五个。{/i}"
        k "{i}天哪，儿子……{/i}"
        scene prologue75
        with Dissolve (1)
        k "{i}好吧……这一仗我们赢了。{/i}"
        k "{i}你该回家了，[r1]。好好休息。{/i}"
        k "{i}这里我们来收拾。{/i}"
        play sound "audio/Flash.ogg"
        scene prologue76
        with flashbulb
        pause
        scene prologue77
        with Dissolve (1)
        pause
        scene prologue78
        with hpunch
        pause
        play sound "audio/Flash.ogg"
        scene prologue79
        with flashbulb
        pause
        play sound "audio/sophiagasp.ogg"
        scene prologue80
        with dissolve
        "{color=#FF007F}索菲娅{/color}猛然惊醒，喘着粗气。"
        scene prologue81
        with dissolve
        sophia "{i}我的天……[name]？[name]？{/i}"
        sophia "{i}你还活着吗？！{/i}"
        r1 "{i}Hmpf...{/i}"
        sophia "{i}谢天谢地！{/i}"
        scene prologue82
        with dissolve
        sophia "{i}撑住，我这就带你去看医生，你会没事的。{/i}"
        r1 "{i}不……{size=-2}医生……{size=-4}不……{size=-3}医院……{/size}{/size}{/size}{/i}"
        sophia "{i}[name]...?!{/i}"
        scene black
        with Dissolve (2)
        sophia "{i}[name!u]!!{/i}"
        play sound "audio/Flash.ogg"
        scene prologue83
        with flashbulb
        sophia "{i}你他妈为什么要那么做？！{/i}"
        sophia "{i}你为什么要救我？！你疯了吗？！{/i}"
        sophia "{i}你根本不认识我！{/i}"
        scene prologue84
        with dissolve
        r1 "{i}{size=-6}在我们这行……活下去的唯一办法……{/size}{/i}"
        r1 "{i}{size=-6}就是……照顾好那些……站在我们这边的人……{/size}{/i}"
        r1 "{i}{size=-6}我们在这份……{/size}{/i}"
        r1 "{i}{size=-6}契约里……是绑在一起的……{/size}{/i}"
        r1 "{i}{size=-6}我看着你的背后……{/size}{/i}"
        r1 "{i}{size=-6}你看着我的……{/size}{/i}"
        r1 "{i}{size=-6}Loyalty...{/size}{/i}"
        r1 "{i}{size=-6}这一切……{/size}{/i}"
        scene prologue85
        with dissolve
        sophia "{i}你没有权利这么对我。{/i}"
        scene prologue86
        with dissolve
        sophia "{i}{size=-7}你更没有……{/size}{/i}"
        scene prologue85
        with dissolve
        sophia "{i}你他妈敢死试试。{/i}"
        scene prologue84
        with dissolve
        r1 "{i}{size=-6}只是……{/size}{/i}"
        r1 "{i}{size=-6}只是皮外伤……{/size}{/i}"
        scene prologue85
        with dissolve
        pause
        scene prologue86
        with dissolve
        pause
        scene prologue87
        with dissolve
        sophia "{i}去你的……{/i}"
        play sound "audio/Flash.ogg"
        scene prologue88
        with flashbulb
        r1 "{i}我得离开一阵子。你也应该回英格兰。{/i}"
        sophia "{i}*声音发颤* 什、什么？{/i}"
        scene prologue89
        with dissolve
        r1 "{i}我现在不能待在你身边。{/i}"
        scene prologue90
        with dissolve
        sophia "{i}你要跟我分手吗？{/i}"
        sophia "{i}我做错什么了吗？{/i}"
        scene prologue89
        with dissolve
        pause
        scene prologue91
        with dissolve
        r1 "{i}我向你保证，不是那个。{/i}"
        r1 "{i}你了解我。我从不找借口。{/i}"
        r1 "{i}如果我想这样，你会知道的。{/i}"
        r1 "{i}我需要离开所有人一段时间。{/i}"
        r1 "{i}而且没有我护着你，我觉得你在这里并不安全。{/i}"
        r1 "{i}就算我把一切都教给了你……要是你出了什么事，我永远都不会原谅自己。{/i}"
        sophia "{i}那我就不明白，我为什么不能跟你一起走。{/i}"
        scene prologue89
        with dissolve
        pause
        scene prologue92
        with dissolve
        pause
        scene prologue93
        with dissolve
        pause
        scene prologue94
        with dissolve
        r1 "{i}求你了，照我说的做。{/i}"
        scene prologue95
        with dissolve
        r1 "{i}这种事不能再发生。{/i}"
        r1 "{i}不能再有下次。绝对不行。{/i}"
        sophia "{i}{size=-6}我看着你的背后……{/size}{/i}"
        sophia "{i}{size=-6}你看着我的……{/size}{/i}"
        sophia "{i}{size=-6}忠诚高于一切……还记得吗？{/size}{/i}"
        scene prologue96
        with dissolve
        r1 "{i}我们会再见的。{/i}"
        r1 "{i}我向你保证，这不是结局。{/i}"
        r1 "{i}把手机给我。我教你万一遇到紧急情况该怎么联系我。{/i}"
        play sound "audio/Flash.ogg"
        scene prologue97
        with flashbulb
        pause
        scene prologue98
        with dissolve
        r2 "{i}(我再说一遍啊。){/i}"
        r2 "{i}(你把每一个你爱的人，都推开了。){/i}"
        r2 "{i}(那又把你带到了什么地步？){/i}"
        scene prologue99
        with dissolve
        r1 "{i}闭嘴，我在专心。{/i}"
        scene prologue100
        with dissolve
        r2 "{i}我也就是说说。{/i}"
        r2 "{i}你为我们的处境挣扎，对我们谁都没好处。{/i}"
        r2 "{i}我不会走的。{/i}"
        r2 "{i}你应该……你知道吧……给[sophia]打个电话。{/i}"
        r2 "{i}告诉她我们没事，请她过来。{/i}"
        scene prologue99
        with dissolve
        r1 "{i}拜托了，闭嘴吧你。{/i}"
        scene prologue100
        with dissolve
        pause
        scene prologue101
        with dissolve
        r2 "{i}再往左一点，风向变了。{/i}"
        scene prologue102
        with Dissolve (2)
        pause
        play sound "audio/snipershot.ogg"
        scene black
        pause
        scene prologue103
        with Dissolve (2)
        r1 "{i}我已经决定好了。{/i}"
        scene prologue104
        with dissolve
        r2 "{i}决定什么？{/i}"
        scene prologue103
        with dissolve
        r1 "{i}决定离开狼群。{/i}"
        scene prologue106
        with dissolve
        r2 "{i}你会把我们俩都害死。{/i}"
        scene prologue105
        with dissolve
        r1 "{i}我心意已决。你得走。{/i}"
        play sound "audio/Flash.ogg"
        scene prologue107
        with flashbulb
        pause
        scene prologue108
        with dissolve
        k "{i}[r1]，我的兄弟！{/i}"
        k "{i}你上一票干得太漂亮了！我跟老板说：「要是有人能办成那事，那就得是[name]！」你果然没让我失望，儿子！{/i}"
        k "{i}所以，你为什么想见我？需要我做什么？{/i}"
        scene prologue109
        with dissolve
        r1 "{i}我想退下来。{/i}"
        scene prologue110
        with dissolve
        pause
        scene prologue111
        with dissolve
        k "{i}这个嘛……我可从没听说谁能金盆洗手。不过只要投票，什么都有可能。{/i}"
        scene prologue110
        with dissolve
        k "{i}我手上有个活儿给你。办成了，我能帮你说服狼群的头领投你一票。{/i}"
        play sound "audio/Flash.ogg"
        scene prologue112
        with flashbulb
        pause
        scene prologue113
        with dissolve
        pause
        scene prologue114
        with dissolve
        pause
        scene prologue115
        with dissolve
        pause
        scene prologue116
        with dissolve
        pause
        play sound "audio/Flash.ogg"
        scene prologue117
        with flashbulb
        l "{i}您一定是[name]先生吧？我是洛莉！很高兴认识您！{/i}"
        l "{i}不知道您什么时候能到呢。您来得正好！我可以带您在校园里转转。{/i}"
        scene prologue118
        with dissolve
        lila "{i}所以……谢谢您……好心的先生？您对我真好！{/i}"
        lila "{i}希望以后能多与您来往！{/i}"
        r1 "{i}我又不是政客。不用这么客气。{/i}"
        r1 "{i}你叫什么来着？莉、莉拉？{/i}"
        scene prologue119
        with dissolve
        lila "{i}我都听腻了！{/i}"
        scene prologue120
        with dissolve
        lila "{i}也不能怪你呀！{/i}"
        lila "{i}我叫[lila]。莉——拉。{/i}"
        play sound "audio/Flash.ogg"
        scene prologue121
        with flashbulb
        r1 "{i}我还不知道你有个妹妹，[lila]。{/i}"
        scene prologue122
        with dissolve
        asu "{i}Sister?{/i}"
        scene prologue123
        with dissolve
        lila "{i}她只是我朋友啦，笨蛋！{/i}"
        asu "{i}而且我还比她大。她才是妹妹。{/i}"
        play sound "audio/Flash.ogg"
        scene prologue124
        with flashbulb
        ja "那你的强项是什么？"
        scene prologue125
        with dissolve
        r1 "嗯……解剖、化学、物理、体育。"
        scene prologue126
        with dissolve
        ju "解剖听起来很有意思。"
        scene prologue127
        with dissolve
        asu "对啊！拿莱拉当教材！"
        scene prologue128
        with dissolve
        lila "亚苏娜！"
        scene prologue127
        with dissolve
        asu "对，直接把她拿去！"
        scene prologue129
        with dissolve
        lila "我要杀了你！"
        scene prologue130
        with dissolve
        ash "她不愿意的话，我可以。"
        scene prologue127
        with dissolve
        asu "阿什莉也主动请缨了！"
        scene prologue130
        with dissolve
        ash "我是说，如果莱拉太害怕的话……"
        play sound "audio/throw2.ogg"
        scene prologue131
        pause
        scene prologue127
        with dissolve
        asu "那她现在死了！"
        play sound "audio/Flash.ogg"
        scene prologue132
        with flashbulb
        ava "我、我是艾、艾娃。"
        scene prologue133
        with dissolve
        r1 "嗯……很高兴认识你，艾、艾娃。"
        play sound "audio/hit1.ogg"
        scene prologue134
        pause
        scene prologue136
        with dissolve
        pause
        scene prologue137
        with dissolve
        pause
        scene prologue135
        with dissolve
        pause
        play sound "audio/Flash.ogg"
        scene prologue138
        with flashbulb
        ava "小家伙学会说话了吗？"
        scene prologue139
        with dissolve
        ava "我、我是艾娃。"
        scene prologue140
        with dissolve
        sophia "她会说话了！"
        scene prologue141
        with dissolve
        r1 "我得去跟俄罗斯人谈。能帮我照看一下她吗？"
        scene prologue142
        with dissolve
        sophia "交给我吧，亲爱的！"
        scene prologue143
        with dissolve
        r1 "谢了。别吓着她。"
        sophia "我才不会！"
        scene prologue144
        with dissolve
        sophia "过来坐我旁边吧，亲爱的。咱们女人之间好好聊聊。"
        play sound "audio/Flash.ogg"
        scene prologue145
        with flashbulb
        sophia "天哪！还有谁饿了？！"
        play sound "audio/Flash.ogg"
        scene prologue146
        with flashbulb
        sophia "别动！"
        sophia "而我——"
        sophia "好了！"
        scene prologue147
        with dissolve
        sophia "你确定不把头发染成金色？"
        sophia "我觉得你染得出来。"
        scene prologue148
        with dissolve
        r1 "你们俩在干什么？"
        scene prologue149
        with dissolve
        sophia "你回来得真早！我们刚弄好装扮。"
        scene prologue148
        with dissolve
        r1 "万圣节装扮不是应该走恐怖路线吗？"
        scene prologue150
        with dissolve
        sophia "你说什么呢？我可是机车党。机车党就是吓人。"
        scene prologue151
        with dissolve
        ava "而我——是哈莉·奎茵。"
        scene prologue148
        with dissolve
        pause
        play sound "audio/Flash.ogg"
        scene prologue152
        with flashbulb
        pause
        scene prologue153
        with dissolve
        pause
        scene prologue153-2
        with dissolve
        ava "我能在这儿待一辈子。"
        play sound "audio/Flash.ogg"
        scene prologue154
        with flashbulb
        ava "我要你相信我！"
        play sound "audio/Flash.ogg"
        scene prologue155
        with flashbulb
        r1 "你我这样的，已经快要绝种了。"
        scene prologue156
        with dissolve
        r1 "如今愿意为了家人越线的人不多了。"
        r1 "一旦越了那条线，人通常就回不来了。"
        r1 "我看得出来你有多在乎你妹妹。"
        r1 "你为她吃过什么苦，我只能想象。"
        scene prologue157
        with dissolve
        r1 "但还有人在指望我们。"
        r1 "所以我们只能撑着。"
        r1 "直到能安心闭眼的那一天。"
        stop music fadeout 4
        scene black
        with Dissolve (3)
        pause (1)
        scene tutorial1
        with Dissolve (1)
        "《堕落学园》里有一些你可能还不熟悉的特殊机制。如果你还没玩过序章，要不要先看看这些机制的提示与说明？"
        "简单来说，就是想看看教程吗？很快的。:)"
        menu:
            "直接带我去游戏吧。":
                pause 0.01
            "嗯，我想再多了解一些。":
                pause 0.01
                play sound "audio/Lockpick_success.ogg"
                scene tutorial2
                with dissolve
                pause
                play sound "audio/Lockpick_success.ogg"
                scene tutorial3
                with dissolve
                pause
                play sound "audio/Lockpick_success.ogg"
                scene tutorial4
                with dissolve
                pause
                play sound "audio/Lockpick_success.ogg"
                scene tutorial5
                with Dissolve(1)
                pause (0.5)
                scene tutorial6
                with Dissolve(1)
                pause
                scene tutorial5
                with Dissolve(1)
                pause (0.5)
                scene tutorial7
                with Dissolve(1)
                pause (0.5)
                scene tutorial8
                with Dissolve(1)
                pause
                play sound "audio/Lockpick_success.ogg"
                scene tutorial7
                with Dissolve(1)
                pause (0.5)
                scene tutorial5
                with Dissolve(1)
                pause (0.5)
                scene tutorial9
                with Dissolve(1)
                pause (0.5)
                scene tutorial10
                with Dissolve(1)
                pause
                scene black
                with Dissolve(2)
                "暂时就这些！随着游戏加入更多功能，这份教程也会继续扩充 :)"
        jump day1_update
                
        
        
    label recapitulate_random:
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_lila +=1
        else:
            $love_lila +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_ash +=1
        else:
            $love_ash +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_lila +=1
        else:
            $love_lila +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $discipline +=5
        else:
            $love_lila +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_ava +=1
        else:
            $goodness +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $goodness -=1
        else:
            $goodness +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $love_ava +=1
        else:
            pause 0.01
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $love_ava +=1
            $love_sophia +=1
        else:
            pause 0.01
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $love_ava +=1
        else:
            pause 0.01
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $love_jas +=1
        else:
            pause 0.01
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_lila +=1
        else:
            $love_lila +=1
        $chance = renpy.random.randint(1, 3)
        if chance == 1:
            $love_ash +=1
        elif chance == 2:
            $love_jas +=1
        else:
            $love_asuna +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_lila +=1
        else:
            $love_lila +=1
        scene intro13_1
        with Dissolve (1)
        $nickname_sophia1 = renpy.input("[sophia]是怎么称呼你的？")
        $nickname_sophia1 = nickname_sophia1.strip()
        if nickname_sophia1 == "":
            $nickname_sophia1 = "darling"
        scene black
        with Dissolve (1)
        scene intro14_1
        with Dissolve (1)
        $nickname_ava1 = renpy.input("[ava]是怎么称呼你的？")
        $nickname_ava1 = nickname_ava1.strip()
        if nickname_ava1 == "":
            $nickname_ava1 = str(r1)
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_jas +=1
        else:
            $love_jas +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_jas +=1
        else:
            $love_jas +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_sophia +=1
        else:
            pause 0.01
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_jas +=1
        else:
            $love_jas +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $corruption_ash +=1
        else:
            $love_ash +=1
        $chance = renpy.random.randint(1, 2)
        if chance == 1:
            $reputation+=1
            $popularity+=1
        else:
            $police+=1
        jump intro_sta
        
            
        
        
        
        
        
        
        
        
        #"「我想我的姑娘了。」":
         #   "teste"    #Phone conversation start
         
         
    #show nighten e1m2_b:
    #    ease 0.5 xalign 0.7 


    return
