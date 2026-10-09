label splashscreen:
    scene black
    pause 0.3
    play music mystic_horror_full
    show sabirowgames
    $renpy.pause(1.5, hard=True)
    pause 8
    pause 1
    hide sabirowgames with dissolve
    show adult_warning with dissolve
    pause 7
    hide adult_warning with dissolve
    pause 0.3
    show gamename
    pause 5
    stop music fadeout 0.3
    return

# START:

label start:
    $ quick_menu = False
    # prolog
    
    scene menu_transitions with Dissolve(0.3)
    $ renpy.pause(2.8, hard=True)
    show menu_gg with Dissolve(0.1)
    
    '请输入名字，或直接使用默认名。' with Dissolve(0.3)

    if _preferences.language == 'schinese':
        $ ggname = renpy.input('你的名字是……', length=13, default='迪米安').strip()
        if ggname == '':
            $ ggname = '迪米安'
    elif _preferences.language == 'russian':
        $ ggname = renpy.input('Меня зовут...', length=13, default='Демиан', allow='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm-ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю').strip()
        if ggname == '':
            $ ggname = 'Демиан'
    else:
        $ ggname = renpy.input('你的名字是……', length=13, default='迪米安').strip()
        if ggname == '':
            $ ggname = '迪米安'
            
    scene black with dissolve
    pause 1
    
    play sound2 glitch_4
    show wear_headphones
    $ renpy.pause(0.5,hard=True)
    stop sound2 fadeout 0.3
    $ renpy.pause(0.2,hard=True)
    play sound3 glitch_1 volume 0.7
    $ renpy.pause(0.5,hard=True)
    stop sound3 fadeout 0.3
    pause 3.8
    
    scene black with dissolve
    '用括号括起来的内容，是角色内心的想法。{w}（感谢你玩到这款游戏！）' with Dissolve(0.3)
    '剧情会随着你的选择与行动而改变。'
    stop music fadeout 5

## New game
    show zasel_1 with dissolve
    $ renpy.pause(13,hard=True)
    pause 0.5
    play music w205
    scene zasel_2 with Dissolve(1.0)
    show screen girls with dissolve
    $ quick_menu = True
    ka 1 "到了。希望你们没坐得屁股发麻。" with Dissolve(0.3)
    scene zasel_3
    may 1 '这房子是什么情况？' with Dissolve(0.3)
    scene zasel_4
    ka 1 "好了，你们俩，这是你们父亲的公寓。说不上豪华，但住着挺舒服。两层楼，好几个房间，还有一间宽敞的浴室……" with Dissolve(0.3)
    scene zasel_5
    with Dissolve(0.2)
    ka 1 "算了，你们自己看吧。这是风间叔叔唯一能留给你们的东西。" with Dissolve(0.3)
    ka 1 "以后你们就住这儿了。新学校就在一箭之遥，市中心也不远。希望你们能喜欢这里。"
    scene zasel_6
    may 1 '哇……'
    play sound keys_drop
    scene zasel_10
    ka 1 '钥匙给你们。' with Dissolve(0.3)
    scene zasel_11
    ka 1 '公寓在十九楼。' with Dissolve(0.3)
    scene zasel_12
    gg 1 "[may]，你先进去吧。这边我来处理。" with Dissolve(0.3)
    scene zasel_13 with Dissolve(0.3)
    may 1 '好！' with Dissolve(0.3)
    scene zasel_14
    with Dissolve(0.2)
    may 1 "太谢谢你了，[ka]。我们真的很感激。" with Dissolve(0.3)
    ka 1 '[may]，要好好照顾自己！' with Dissolve(0.3)
    scene zasel_15
    pause 2.0
    
    scene zasel_17 with Dissolve(0.3)
    ka 1 "[gg]，替我照顾好[may]。我知道你这孩子有担当，但现在那姑娘比任何时候都需要有人撑着她。" with Dissolve(0.3)
    ka 1 "新的城市，新的面孔……还得跟老朋友一刀两断。我知道这一切都不容易，但你必须撑住。"
    scene zasel_16 with Dissolve(0.3)
    gg 1 "放心吧，叔叔。我会照顾好她的。她还能跟以前的朋友打电话，而且交新朋友这种事，从来都难不倒她。" with Dissolve(0.3)
    scene zasel_17 with Dissolve(0.3)
    ka 1 "是啊，那丫头挺坚强的。那你呢，[gg]？还撑得住吗？" with Dissolve(0.3)
    scene zasel_16 with Dissolve(0.3)
    gg 1 "我觉得我们能行。我一直是一个人过来的，在原来的学校也没留下什么朋友。" with Dissolve(0.3)
    scene zasel_17 with Dissolve(0.3)
    ka 1 "你觉得这是好事？人还是需要有人陪的，[gg]。" with Dissolve(0.3)
    scene zasel_16 with Dissolve(0.3)
    gg 1 "我有[may]就够了。再说，换个环境对我们也许是好事。正好可以重新开始。" with Dissolve(0.3)
    scene zasel_17 with Dissolve(0.3)
    ka 1 "这就对了，小子！" with Dissolve(0.3)
    scene zasel_9 with Dissolve(0.3)
    ka 1 "好了……该搬行李了。" with Dissolve(0.3)
    
    scene zasel_18 with dissolve
    gg 1 "行啊。不过说真的，我很意外。你之前说是一栋空房子，我以为会不一样。" with Dissolve(0.3)
    
    ka 1 "你们父亲可是为这地方拼了命的。" with Dissolve(0.3)
    ka 1 "他是个好人。可惜走得太早了。"
    ka 1 "他留给你们的，你们要好好珍惜。"
    
    gg 1 "当然，[ka]。" with Dissolve(0.3)
    
    scene zasel_20 with Dissolve(0.3)
    gg 1 "在我走之前……叔叔，关于我父亲到底是怎么死的，你确定已经全都告诉我们了？" with Dissolve(0.3)
    scene zasel_19 with Dissolve(0.3)
    ka 1 "哦，[gg]……他是死于车祸。很突然。" with Dissolve(0.3)
    ka 1 "认识他的人都受到了影响。至少我们的长辈都已经不在了——谢天谢地，他们不用经历这份悲痛。"
    ka 1 "但就算过了这么久，我老婆晚上有时还是会哭。她以为我没察觉。"
    scene zasel_20 with Dissolve(0.3)
    gg 1 "我明白……我一直没能真正接受，但希望以后能弄清楚。" with Dissolve(0.3)
    scene zasel_19 with Dissolve(0.3)
    ka 1 "别想太多，[gg]。你还小，该把心思放在学业上！" with Dissolve(0.3)
    scene zasel_20 with Dissolve(0.3)
    gg 1 "再次谢谢你，[ka]。你为我们做的一切，我们都记在心里。" with Dissolve(0.3)
    scene zasel_19 with Dissolve(0.3)
    ka 1 "说什么呢，[gg]。为风间叔叔做这点事，不算什么。" with Dissolve(0.3)
    ka 1 "那就这样吧，路上小心。我会去看你们的，你们随时给我打电话！"
    show black with dissolve
    stop music fadeout 2
    pause 2.0
    play sound door_close
    pause 1.0

## Go Home 
    show zahod_1 with dissolve
    $ renpy.pause(4, hard=True)
    pause 18.0

    show zahod_may_say_wait with Dissolve(0.2)
    pause 1.0

    $ athomewithmay = []
    menu athomewithmay:
        set athomewithmay
        '「你觉得这公寓怎么样？」':
            show zahod_may_say_yes with Dissolve(0.2)
            may 1 '太喜欢了！' with Dissolve(0.3)
            scene zahod_3 with Dissolve(0.3)
            may 1 '客厅又时髦又现代，厨房还超大！' with Dissolve(0.3)
            scene zahod_4 with Dissolve(0.3)
            may 1 "啊！这里的景色太棒了！不敢相信我们居然能住上这种公寓！" with Dissolve(0.3)
            show zahod_may_say_wait with Dissolve(0.2)
            gg 1 "你喜欢就好。" with Dissolve(0.3)
            gg 1 "（落地窗有点不寻常。要不要买几块窗帘，免得到时候被人看到？）"
            gg 1 "卧室看过了吗？"
            scene zahod_5 with Dissolve(0.3)
            may 1 "嗯，这公寓真的有两层呢！" with Dissolve(0.3)
            scene zahod_6 with Dissolve(0.3)
            may 1 "楼上有两间卧室，还有浴室和淋浴间。" with Dissolve(0.3)
            $ athomewithmay_point += 1
            show zahod_may_say_wait with Dissolve(0.2)
            jump athomewithmay

        '「有什么需要帮忙的吗？」':
            show zahod_may_say_wait with Dissolve(0.2)
            show zahod_may_say_no with Dissolve(0.2)
            may 1 "不不，[gg]，都没问题的！" with Dissolve(0.3)
            gg 1 "有什么需要就告诉我，好吗？" with Dissolve(0.3)
            may "谢了，[gg]。不过我现在最需要的，就是躺在真正的床上好好睡一觉。" with Dissolve(0.3)
            $ athomewithmay_point += 1
            show zahod_may_say_wait with Dissolve(0.2)
            jump athomewithmay
            
        '「刚才在外面的时候，叔叔有没有哪里不对劲？」' if athomewithmay_point == 2:
            scene zahod_7 with Dissolve(0.3)
            may 1 '什么意思？' with Dissolve(0.3)
            show zahod_may_say_wait2 with Dissolve(0.2)
            gg 1 "该怎么说呢……在车里和在房子门口时，他都有些……我都不知道该怎么形容。" with Dissolve(0.3)
            gg 1 "说到父亲的时候，他的反应特别奇怪。"
            gg 1 "尤其是在话题转到父亲的死讯时。"
            scene zahod_4 with Dissolve(0.3)
            may 1 "这个话题我也很难受。可叔叔到底说了什么？" with Dissolve(0.3)
            show zahod_may_say_wait2 with Dissolve(0.2)
            gg 1 "他说父亲是死于车祸。但我不确定。知道他那份工作一直很隐秘，可是……" with Dissolve(0.3)
            scene zahod_8 with Dissolve(0.3)
            may 1 "我懂。不过也许他只是不想谈这件事。" with Dissolve(0.3)
            show zahod_may_say_wait2 with Dissolve(0.2)
            gg 1 "嗯，也许你说得对。" with Dissolve(0.3)
            scene zahod_9 with Dissolve(0.3)
            may 1 "想和我谈谈吗？" with Dissolve(0.3)
            show zahod_may_say_wait2 with Dissolve(0.2)
            gg 1 "我也不知道有什么可谈的。只是有种直觉，事情不太对劲。" with Dissolve(0.3)
            gg 1 "先别想这些了。专心把这里当成我们人生的新篇章吧。"
            scene zahod_10 with Dissolve(0.3)
            may 1 "嗯。不会轻松，但两个人一起，什么都能撑过去！" with Dissolve(0.3)
            show zahod_may_say_wait with Dissolve(0.2)

        '「算了。」':
            pause 1.0
    
    scene zahod_11 with Dissolve(0.2)
    may 1 "明天得早点起来。" with Dissolve(0.3)
    $ may_unlock += 1
    show screen rel_open_may
    scene zahod_12 with dissolve
    may 1 "我直接去睡了。" with Dissolve(0.3)
    scene zahod_13 with Dissolve(0.1)
    pause 0.5
    scene zahod_13_1 with Dissolve(2.0)
    pause 2.0
    may 1 "对了，左手边第一间是我的房间。" with Dissolve(0.3)
    gg 1 "知道了。晚安。" with Dissolve(0.3)
    scene zahod_14 with dissolve
    may 1 "晚安！" with Dissolve(0.3)
    scene zahod_15 with Dissolve(0.1)
    pause 2.0
    gg 1 "（[may]真的很爱做饭，这个厨房正适合她）" with Dissolve(0.3)
    scene zahod_16 with Dissolve(0.1)
    pause 3.0
    gg 1 '（地板很宽敞。）' with Dissolve(0.3)
    gg "（有个视野很棒的阳台。）"
    show zahod_17 with Dissolve(0.1)
    $ renpy.pause(2, hard=True)
    pause 5.0
    scene zahod_17_1 with Dissolve(0.1)
    gg 1 "（这侧应该不会有卧室。）" with Dissolve(0.3)
    gg "（这房间不可能有窗户。）"
    gg '（嗯……这是浴室？）'
    menu:
        "查看\\n[blue](更多内容)":
            scene zahod_18 with Dissolve(0.1)
            pause 3.0
            gg 1 '（好一把气派的椅子。）' with Dissolve(0.3)
            pause 0.3

        "继续前进":
            pause 0.3
    show zahod_19 with Dissolve(0.1)
    $ renpy.pause(2, hard=True)
    pause 5.0
    scene zahod_19_1
    gg 1 "（看来这是[may]的房间。）" with Dissolve(0.3)
    gg "（门开着一条缝。她还是跟以前一样不让人省心。）"
    menu:
        "往里看\\n[blue](更多内容)":
            scene zahod_20 with dissolve
            ''
            scene zahod_21 with Dissolve(0.3)
            pause 1.6
            scene zahod_21_1 with Dissolve(0.3)
            gg 1 '（别待太久。）' with Dissolve(0.3)
            pause 0.3
            show zahod_22 with Dissolve(0.1)
            $ renpy.pause(2, hard=True)
            pause 5.0

        "继续前进":
            pause 0.3
            show zahod_23 with Dissolve(0.1)
            $ renpy.pause(2, hard=True)
            pause 5.0

    scene zahod_24 with Dissolve(0.3)
    pause 0.6
    gg 1 '（那这间应该就是我的房间。）' with Dissolve(0.3)
    scene black with dissolve
    play sound clothes_1
    pause 2.0
    scene zahod_25 with dissolve
    pause 1.0
    gg 0 '{cps=5}……{/cps}' with Dissolve(0.3)
    scene zahod_26 with dissolve
    pause 2.0
    gg 0 "（我始终摆脱不了这种感觉——父亲的死……不像[ka]说的只是一场普通车祸。）" with Dissolve(0.3)
    gg 0 "（叔叔是不是瞒着我和[may]什么？……也许只是我太累了，但这个念头一直在脑子里打转……）"
    gg 0 "（要不要去问问阿姨？还是我自己去查？）"
    gg 0 "（父亲……你到底遭遇了什么？……）"
    gg '{cps=5}……{/cps}'
    pause 1.0
    gg 0 "（算了。现在想这些也没用。该把心思放在接下来要做的事上。）" with Dissolve(0.3)
    gg 0 "（明天就要去新高中报到了……）"
    gg 0 "（不知道会是什么样？会和同学合不来吗？……）"
    gg 0 "（父亲的事先放一放。等时机到了再深挖……现在先睡一会儿，明天有硬仗要打。）"
    scene black with dissolve
    play music rain_street_01 fadein 13
    pause 3.0
    
## nighmires back/future
    play music2 call_start
    scene nightmare1_1 with dissolve
    ''
    scene nightmare1_2 with dissolve
    gg 6 '{cps=6}喂……{/cps}'
    scene nightmare1_3 with dissolve
    pause 2.0
    scene nightmare1_4 with dissolve
    pause 1.0
    gg 6 '{cps=7}[may]？{/cps}'
    stop music2
    scene nightmare1_5 with dissolve
    pause 1.0
    scene nightmare1_6 with Dissolve(0.3)
    gg 6 '{cps=7}喂？{/cps}' with dissolve
    scene nightmare1_5 with Dissolve(0.3)
    play music2 happy_memory_loopable_by_chilledmusic volume 0.6
    show nightmare1_21 with easeinright
    may 4 "早啊，[gg]。感觉怎么样？" with dissolve
    scene nightmare1_22 with Dissolve(0.3)
    gg 6 "没事，就是一直没睡着。你在哪儿，出什么事了？" with dissolve
    scene nightmare1_23 with Dissolve(0.3)
    may 4 "天都亮了，懒猪！你睡得跟死过去一样的时候，我去买了新鲜的鱼做早饭。" with dissolve
    may 4 "你最爱吃鱼了，我当然知道！我们做成饭团——好久没吃过了！"
    scene nightmare1_24 with Dissolve(0.3)
    gg 6 "谢啦，妹！不过你要是先说一声，我自己去买就行了。" with dissolve
    scene nightmare1_25 with Dissolve(0.3)
    may 4 "那样不就没惊喜了嘛？" with dissolve
    scene nightmare1_26 with Dissolve(0.3)
    gg 6 "嗯，你说得对。" with dissolve
    gg 6 "等等，可你已经把惊喜说掉了啊……" with dissolve
    scene nightmare1_27 with Dissolve(0.3)
    may 4 "{cps=6}我知道……{/cps} {w=0.6}不过没按计划来。" with dissolve
    may 4 "我本来是想说……好像出了点怪事……"
    stop music2 fadeout 13
    show nightmare1_7 with dissolve
    gg 6 "行吧，你该先说这个。到底怎么了？" with dissolve
    may 4 "我听到奇怪的声音……还看到远处好像有烟。烟好像是从市中心飘过来的。" with dissolve
    gg 6 "（烟？）" with dissolve
    gg "（奇怪的声音？）"
    gg 6 "（我什么也没看到。）" with dissolve
    gg 6 "我这边什么都看不到也听不到。可能是雨的关系吧。你听到的是什么声音？" with dissolve
    may 4 "像是远处在响的警报声。还有……一种低沉的轰隆声。" with dissolve
    scene nightmare1_8 with dissolve
    gg 6 "（地震？不可能吧——这座城市本来就在地震带上，真有的话我会有感觉的。）" with dissolve
    scene nightmare1_9 with dissolve
    gg 6 "你离家远吗？多久能回来？" with dissolve
    scene nightmare1_8 with Dissolve(0.3)
    may 4 "我很快就到。先去药店一趟，给你买点维生素。" with dissolve
    scene nightmare1_6 with Dissolve(0.3)
    gg 6 "维生素？干嘛？我可没让你买那个。" with dissolve
    scene nightmare1_5 with Dissolve(0.3)
    may 4 "我就是要买！吃了会更有精神！" with dissolve
    scene nightmare1_6 with Dissolve(0.3)
    gg 6 "[may]，我不知道外面发生了什么，但你快点回来。路上小心！我会一直听着。" with dissolve
    scene nightmare1_5 with Dissolve(0.3)
    may 4 "放心，我会小心的。" with dissolve
    play music2 ingestion_of_sorrows_by_tim_kulig
    $ renpy.pause(1.8,hard=True)
    scene nightmare1_10 with hpunch
    pause 0.1
    scene nightmare1_11 with dissolve
    pause 0.1
    scene black with Dissolve(0.2)
    pause 1.0
    show nightmare1_12 with dissolve
    pause 1.0
    gg 6 '我靠……那他妈是什么鬼？！' with Dissolve(0.3)
    scene nightmare1_13 with dissolve
    gg 6 '{cps=5}……{/cps}' with Dissolve(0.3)
    scene nightmare1_14 with dissolve
    gg 6 '[may]？' with Dissolve(0.3)
    scene nightmare1_15 with vpunch
    may 5 '啊啊啊！' with Dissolve(0.3)
    scene nightmare1_16 with dissolve
    may 5 '[gg]！{cps=5}……{/cps} {w=0.6}[gg]，救我！' with Dissolve(0.3)
    scene nightmare1_14 with dissolve
    gg 6 "[may]，怎么回事？！你在哪儿？" with Dissolve(0.3)
    scene nightmare1_16 with dissolve
    pause 1.6
    scene nightmare1_14 with vpunch
    gg 6 '[may]？！' with Dissolve(0.3)
    scene nightmare1_16 with dissolve
    play sound call_end volume 0.6
    gg 6 '{cps=5}……{/cps}'
    '通讯中断了。'
    scene nightmare1_15 with dissolve
    pause 2.0
    show nightmare1_12 with dissolve
    pause 1.0
    gg 6 "混账……" with Dissolve(0.3)
    gg "到底他妈发生了什么？"
    scene nightmare1_17 with dissolve
    gg 6 '([may]！)'
    stop music fadeout 10
    show nightmare1_18 with Dissolve(0.1)
    $ renpy.pause(24,hard=True)
    show nightmare1_19 with Dissolve(0.1)
    hide nightmare1_18
    pause 1.0
    gg 0 "（我有种很不好的预感。）" with Dissolve(0.3)
    pause 1.0
    gg 0 "（但我得赶紧过去。）" with Dissolve(0.3)
    pause 1.0
    menu:
        '环顾四周\\n[blue](更多内容)':
            pause 1.0
            gg 0 "只是太黑了，还是……" with Dissolve(0.3)
            pause 1.0
            gg 0 "黑暗里真他妈站着个什么东西？" with Dissolve(0.3)
            pause 1.0
            
            menu:
                '继续前进\\n[gr](推荐)':
                    pause 1.0
                    show nightmare1_20 with Dissolve(0.1)
                    hide nightmare1_19
                    $ renpy.pause(18.7,hard=True)
                    
                    stop music2 fadeout 1.6
                    scene nightmare_sbor_1 with hpunch
                    play music3 city_bird fadein 10 volume 0.7
                    pause 0.6
                    play sound clothes_2 volume 0.5
                    scene nightmare_sbor_2 with hpunch
                    gg 0 "噗！"
                    scene nightmare_sbor_3 with Dissolve(0.2)
                    gg 0 "哈……" with Dissolve(0.2)
                    scene nightmare_sbor_4
                    gg 0 "靠……" with Dissolve(0.3)
                    scene nightmare_sbor_5
                    with Dissolve(0.2)
                    gg 0 '{cps=5}……{/cps}' with Dissolve(0.3)
                    scene sbor_school_1
                    pause 1.6
                    gg 0 "（又是一场噩梦。）" with Dissolve(0.3)
                    gg 0 "（为什么这些噩梦一次又一次地重复？……）"
                    scene sbor_school_2 with Dissolve(0.3)
                    pause 1.0
                    
                "回家":
                    pause 1.0
                    gg 0 "靠，不管了。我要回家。"
                    scene black with dissolve
                    pause 3.0
                    
                    stop music2 fadeout 1.6
                    scene nightmare_sbor_1_1 with dissolve
                    play music3 city_bird fadein 10 volume 0.7
                    pause 1.6
                    gg 0 '{cps=5}……{/cps}'
                    play sound clothes_2 volume 0.5
                    scene nightmare_sbor_2 with dissolve
                    gg 0 "（他妈又是噩梦。）" with dissolve
                    gg 0 "（又是这种鬼东西。）"
                    scene nightmare_sbor_5
                    with Dissolve(0.2)
                    gg 0 '{cps=5}……{/cps}' with Dissolve(0.3)
                    scene sbor_school_1 with dissolve
                    gg 0 "（这次我及时醒过来了。）"
                    scene sbor_school_2 with Dissolve(0.3)
                    pause 1.0
            
        '继续前进':
            pause 1.0
            show nightmare1_20 with Dissolve(0.1)
            hide nightmare1_19
            $ renpy.pause(18.7,hard=True)
            
            stop music2 fadeout 1.6
            scene nightmare_sbor_1 with hpunch
            play music3 city_bird fadein 10 volume 0.7
            pause 0.6
            play sound clothes_2 volume 0.5
            scene nightmare_sbor_2 with hpunch
            gg 0 "噗！"
            scene nightmare_sbor_3 with Dissolve(0.2)
            gg 0 "哈……" with Dissolve(0.2)
            scene nightmare_sbor_4
            gg 0 "靠……" with Dissolve(0.3)
            scene nightmare_sbor_5
            with Dissolve(0.2)
            gg 0 '{cps=5}……{/cps}' with Dissolve(0.3)
            scene sbor_school_1
            pause 1.6
            gg 0 "（又是一场噩梦。）" with Dissolve(0.3)
            gg 0 "（为什么这些噩梦一次又一次地重复？……）"
            scene sbor_school_2 with Dissolve(0.3)
            pause 1.0
    
## school jinalyk
    scene black with dissolve
    stop music3 fadeout 3
    play music happy_memory_loopable_by_chilledmusic fadein 13 volume 0.6
    pause 1.6
    scene sbor_school_3 with dissolve
    pause 1.0
    scene sbor_school_4 with dissolve
    gg 2 "（还有[may]。）" with dissolve
    scene sbor_school_5 with dissolve
    pause 0.6
    gg 2 "（她正忙着做早饭。）" with dissolve
    pause 0.6
    menu:
        '「早上好。」':
            scene sbor_school_8 with dissolve
            gg 2 "早上好。" with dissolve
            scene sbor_school_9 with dissolve
            may 2 "哇，你已经醒了？" with dissolve
            scene sbor_school_10 with dissolve
            pause 1.6

        "往下看":
            scene sbor_school_6 with dissolve
            pause 2.6
            scene sbor_school_7 with dissolve
            pause 1.0
            scene sbor_school_8 with dissolve
            pause 1.6
            scene sbor_school_9 with dissolve
            may 2 "哇，你已经醒了？" with dissolve
            scene sbor_school_10 with dissolve
            gg 2 "早上好。" with dissolve
          
    scene sbor_school_9 with dissolve
    may 2 "早上好，[gg]！在新地方睡得怎么样？" with dissolve
    scene sbor_school_10 with dissolve
    gg 2 "……说不上来。做了些奇怪的梦，不过应该会过去的。" with dissolve
    scene sbor_school_9 with dissolve
    may 2 "别担心，换新环境都这样。不过我睡得特别好——床又大又软！想垫几个枕头都行，还能抱着枕头睡！" with dissolve
    scene sbor_school_10 with dissolve
    gg 2 "你喜欢就好。那我今晚是不是也该试试抱枕头睡？" with dissolve
    scene sbor_school_9 with dissolve
    may 2 "嘿嘿，强烈推荐！" with dissolve
    scene sbor_school_11 with dissolve
    may 2 "好，我也该去准备了。" with dissolve
    scene sbor_school_12 with Dissolve(0.3)
    may 2 "饭做好了。坐下吃吧——今天可有得忙！" with dissolve
    pause 1.0
    $ renpy.music.set_volume(1, delay=0, channel=u'music')
    scene sbor_school_13 with fade
    $ renpy.music.set_volume(0.5, delay=0, channel=u'music')
    play music2 city_bird fadein 0.6
    pause
    stop music2 fadeout 6
    $ renpy.music.set_volume(1, delay=0, channel=u'music')
    scene sbor_school_14
    ''
    scene sbor_school_15 with Dissolve(0.3)
    gg 3 "你换衣服还要多久？" with dissolve
    gg "要迟到了。"
    scene sbor_school_16 with Dissolve(0.3)
    may 3 "我早好了。" with dissolve
    pause 1.0
    may 3 "走吧。" with dissolve
    show sbor_school_17 with Dissolve(0.3)
    $ renpy.pause(7.7, hard=True)
    show sbor_school_18 with Dissolve(0.1)
    hide sbor_school_17
    ''
    scene sbor_school_20 with Dissolve(0.1)
    show sbor_school_19 with Dissolve(0.1)
    hide sbor_school_18
    $ renpy.pause(2, hard=True)
    may 3 '我好看吗？' with dissolve
    pause 0.6
    menu:
        '「你很好看。」\\n[gold](芽衣 +1)':
            show sbor_school_21 with Dissolve(0.1)
            hide sbor_school_19
            hide sbor_school_20
            $ love_may = love_may + 1
            show screen rel_up_may
            may 3 '真的？那太好了。' with Dissolve(0.3)
        '「还行。」':
            show sbor_school_22 with Dissolve(0.1)
            hide sbor_school_19
            hide sbor_school_20
            may 3 "你不喜欢？" with Dissolve(0.3)
            may 3 "你换衣服也太久了……" with Dissolve(0.3)
            gg 3 "不不！我喜欢，很漂亮。" with Dissolve(0.3)

    scene sbor_school_23 with Dissolve(0.3)
    gg 3 "随你怎么说吧，反正你穿校服一直挺好看的。不过这身尤其棒。我就是担心会有哪个混蛋来搭讪你。" with Dissolve(0.3)
    scene sbor_school_24
    may 3 "不会的。" with Dissolve(0.3)
    scene sbor_school_25 with Dissolve(0.3)
    may 3 "我都会说自己有男朋友。" with Dissolve(0.3)
    scene sbor_school_23 with Dissolve(0.3)
    gg 3 "要是不了解你，我还真就信了。" with Dissolve(0.3)
    scene sbor_school_25 with Dissolve(0.3)
    may 3 "嘿嘿……谢啦。" with Dissolve(0.3)
    scene sbor_school_26 with Dissolve(0.3)
    may 3 "该走了。" with Dissolve(0.3)
    stop music fadeout 3
    stop music2 fadeout 3
    scene black with dissolve
    pause 2.6
    
## School keldi
    play music city_bird volume 0.8 fadein 5
    scene school_start_1 with dissolve
    pause 2.0
    scene school_start_2 with dissolve
    pause 2.0
    scene school_start_3 with Dissolve(0.1)
    may 3 "哇，这学校真大。" with Dissolve(0.3)
    may "希望我们能很快记住各个地方怎么走。"
    scene school_start_4 with Dissolve(0.1)
    pause 1.0
    may 3 "话说……是我多心，还是有很多人在盯着我们看？" with Dissolve(0.3)
    gg 3 "我也注意到了。可能因为我们是新来的。学校是大了点，但毕竟是大家待的地方——新面孔总会引起好奇。" with Dissolve(0.3)
    may "有道理。不过还是有点让人不自在……" with Dissolve(0.3)
    scene school_start_5 with Dissolve(0.1)
    may 3 "全是些不认识的人……" with Dissolve(0.3)
    gg 3 "别担心，你很快就会交到很棒的新朋友。" with Dissolve(0.3)
    scene school_start_6 with Dissolve(0.1)
    pause 1.6
    may 3 "真够恶心的……" with Dissolve(0.3)
    scene school_start_7 with Dissolve(0.3)
    pause 1.6
    gg 3 '（本地的“艺术家”啊。）' with Dissolve(0.3)
    scene school_start_8
    gg 3 "离上课没多少时间了。办完入学手续就直接去教室吧。" with Dissolve(0.3)
    gg "放学后在校门口见？"
    scene school_start_9
    may 3 '好。' with Dissolve(0.3)
    stop music fadeout 2
    scene black with dissolve
    pause 1.6
    
# School Start
    play sound schooldoor
    scene school_class_start_door_1 with dissolve
    pause 0.6
    scene school_class_start_door_2 with dissolve
    pause 1.0
    play music school_fon fadein 5 volume 0.8
    scene school_class_start_1 with vpunch
    fcm1 "老师进教室了！" with Dissolve(0.3)
    scene school_class_start_2
    teacher 1 "咳咳……好了，同学们，回到座位上。" with Dissolve(0.3)
    scene school_class_start_3 with dissolve
    teacher 1 "今天有一位新同学加入我们。欢迎这位将要和大家一起学习的转学生。" with Dissolve(0.3)
    scene school_class_start_4 with dissolve
    teacher 1 "他长期生活在国外，今后打算在我们的城市生活和学习。" with Dissolve(0.3)
    teacher 1 "大家一起帮他适应这里的生活吧。"
    scene school_class_start_5 with dissolve
    gg 3 "我叫[gg]。很高兴认识大家，希望我们能相处愉快。" with Dissolve(0.3)
    show school_class_start_video with Dissolve(0.2)
    pause 6.3
    scene school_class_start_6 with Dissolve(0.2)
    teacher 1 "很高兴认识你，[gg]。进来找个位置坐下吧。" with Dissolve(0.3)
    play music jailbreak_whispers_by_john_bartmann
    scene school_class_start_7
    me0 1 "喂，[dai]，动手。" with Dissolve(0.3)
    scene school_class_start_8 with dissolve
    dai0 1 "嗯，就该这样。这新来的看着就很欠揍。" with Dissolve(0.3)
    scene school_class_start_9
    dai0 1 "看我的。" with Dissolve(0.3)
    scene school_class_start_10 with Dissolve(0.2)
    dai0 1 "（第一天就要挨揍，做好心理准备吧。）" with Dissolve(0.3)
    scene school_class_start_11
    menu:
        '踩上去\\n[blue](推荐)':
            scene school_class_start_11_1_1 with hpunch
            play sound kabluk
            play sound2 perelom volume 3
            ''
            scene school_class_start_11_1_2
            dai0 1 '唔……'
            scene school_class_start_11_1_3 with hpunch
            dai0 1 '混蛋！'
            $ nastupil_nogu = True
        '跨过去':
            play sound kabluk
            scene school_class_start_11_2_1
            ''
            scene school_class_start_11_2_2
            dai0 1 "（他发现了？！）"
            dai0 '（可恶，我明明算好了一切。）'
            scene school_class_start_11_2_3 with hpunch
            dai0 1 '喂，你！'

    scene school_class_start_12
    teacher 1 "干什么，[dai]？"
    play music2 school_fon fadein 5 volume 0.7
    stop music fadeout 5
    scene school_class_start_13
    play sound skrip_stula volume 0.6
    pause 0.3
    scene school_class_start_14 with dissolve
    dai0 1 "没什么，都挺好的。" with Dissolve(0.3)
    scene school_class_start_15
    teacher 1 "那么，[li]，[gg]坐在你旁边。请多关照他。" with Dissolve(0.3)
    scene school_class_start_16
    li 1 "当然。" with Dissolve(0.3)
    scene school_class_start_17
    li 1 "你好，我是[li]。" with Dissolve(0.3)
    scene school_class_start_18 with dissolve
    li 1 "[gg]——这名字也挺特别的。你是在国外出生的？" with Dissolve(0.3)
    scene school_class_start_19 with dissolve
    gg 3 "是的。很高兴认识你。" with Dissolve(0.3)
    scene school_class_start_20 with dissolve
    pause 1.6
    scene school_class_start_21 with dissolve
    li 1 "彼此彼此。第一天就遇上这种事，可别被吓到。" with Dissolve(0.3)
    li 1 "我看见他们把脚伸到你前面了。"
    scene school_class_start_22 with dissolve
    li 1 "那是[dai]。他对每个新生都来这套。" with Dissolve(0.3)
    scene school_class_start_dai_1
    pause 1.0
    scene school_class_start_dai_2 with dissolve
    pause 0.6
    scene school_class_start_dai_4 with vpunch
    pause 0.6
    scene school_class_start_dai_3 with Dissolve(0.3)
    pause 0.4
    scene school_class_start_dai_4 with Dissolve(0.3)
    pause 0.6
    if nastupil_nogu:
        scene school_class_start_18
        li 1 "看你把他怼回去真痛快。"  with Dissolve(0.3)
    else:
        scene school_class_start_18
        li 1 "你没理他，做得对。" with Dissolve(0.3)
    
    scene school_class_start_22 with dissolve
    li 1 "他右边那个是[me]。" with Dissolve(0.3)
    scene school_class_start_me_1
    pause 0.6
    scene school_class_start_me_2 with dissolve
    pause 1.6
    scene school_class_start_21
    li 1 "这种找茬的事一般都是他挑的头。" with Dissolve(0.3)
    scene school_class_start_18 with dissolve
    li 1 "那两个人你小心点……" with Dissolve(0.3)
    scene school_class_start_19 with dissolve
    gg 3 "谢谢你，[li]。跟那两位比起来，你的善意真是让人耳目一新。" with Dissolve(0.3)
    scene school_class_start_18 with dissolve
    li 1 "对待新同学本来就应该这样，不是吗？" with Dissolve(0.3)
    stop music2 fadeout 1
    play sound kinkonkankon_outin volume 0.7
    play sound3 city_bird fadein 1 volume 0.6
    scene school_zvonok_1
    $ renpy.pause(5.5, hard=True)
    scene school_class_start_23
    stop sound3 fadeout 2
    teacher 1 "好，现在开始上课。" with dissolve
    stop sound fadeout 1
    scene black with dissolve
    pause 1.0
    play sound schooldoor
    pause 2.0
    
## School canteen
    scene schoolcanteen_start_1 with dissolve
    play music fromage_by_steven_obrien fadein 13 volume 0.5
    pause 1.6
    scene schoolcanteen_start_2 with dissolve
    pause 0.8
    scene schoolcanteen_start_3 with dissolve
    li 1 "喂，[gg]，要不要一起去食堂吃点东西？" with dissolve
    scene schoolcanteen_start_4 with dissolve
    gg 3 "哦……好啊，我很乐意。谢谢你邀请我。" with dissolve
    gg 3 "（现在拒绝也没意义。我谁都不认识，对学校也完全不熟。）"
    scene schoolcanteen_start_5 with dissolve
    li 1 "刚来可能会不习惯，你不介意我带你转转吧？" with dissolve
    scene schoolcanteen_start_6 with dissolve
    gg 3 "（她简直是完美的班长。）" with dissolve
    gg 3 "那真是帮大忙了，又谢谢你。看来我现在确实需要人带一带。"
    scene schoolcanteen_start_7 with dissolve
    li 1 "那还等什么？走，吃东西去！" with dissolve
    scene black with dissolve
    pause 2.3
    play music2 schoolcanteen fadein 3 volume 0.5
    scene schoolcanteen_start_8 with dissolve
    pause 1.6
    scene schoolcanteen_start_9 with dissolve
    pause 2.0
    scene schoolcanteen_start_10 with dissolve
    ''
    scene schoolcanteen_start_11 with dissolve
    li 1 "跟平时一样，人真多。" with dissolve
    scene schoolcanteen_start_12 with dissolve
    li 1 '{cps=5}……{/cps}'
    li "看到那边那个拿着手机的女生了吗？"
    scene schoolcanteen_start_13 with Dissolve(0.3)
    pause 1.0
    gg 3 "红头发那个？" with dissolve
    li 1 "那是[leah]。" with dissolve
    scene schoolcanteen_start_14 with dissolve
    li 1 "她和我们同班，不过我猜你还没跟别人聊过吧。"
    scene schoolcanteen_start_15 with dissolve
    li 1 "要不要过去找她？你们俩认识新朋友都不吃亏，对吧？"
    scene schoolcanteen_start_16 with dissolve
    li 1 "多交个朋友总是好的嘛。"
    scene schoolcanteen_start_17 with dissolve
    gg 3 "也是。不过她看起来完全沉浸在手机里。你确定她想被打扰？" with dissolve
    scene schoolcanteen_start_14 with dissolve
    li 1 "哎呀，她没看上去那么不合群啦。" with dissolve
    scene schoolcanteen_start_16 with dissolve
    li 1 "再说了，我们是朋友嘛！"
    scene schoolcanteen_start_17 with dissolve
    gg 3 "好吧，你带路。" with dissolve
    scene black with dissolve
    pause 0.6
    scene schoolcanteen_start_18 with dissolve
    li 1 "喂，[leah]，介意我们坐过来吗？" with dissolve
    scene schoolcanteen_start_19 with Dissolve(0.3)
    leah 1 "当然，坐吧。" with dissolve
    scene schoolcanteen_start_20 with Dissolve(0.3)
    gg 3 '{cps=6}……{/cps}' with dissolve
    gg "很高兴认识你，[leah]。"
    leah 1 "嗯哼。" with dissolve
    scene schoolcanteen_start_21 with dissolve
    leah 1 "哦、哦，{cps=5}嗨、嗨。{/cps}"
    scene schoolcanteen_start_22 with dissolve
    pause 1.6
    scene schoolcanteen_start_23 with dissolve
    li 1 "别害羞，[leah]。这位是[gg]，新来的。" with dissolve
    scene schoolcanteen_start_24 with dissolve
    leah 1 "好、好的，我记得！" with dissolve
    $ leah_unlock = True
    scene schoolcanteen_start_25 with Dissolve(0.3)
    li 1 "那个，[gg]，你觉得我们学校怎么样？第一印象很重要吧？" with dissolve
    scene schoolcanteen_start_26 with dissolve
    gg 3 "还不错。就是还在慢慢适应。" with dissolve
    scene schoolcanteen_start_27 with dissolve
    leah 1 "我懂那种感觉……" with dissolve
    scene schoolcanteen_start_28 with dissolve
    leah 1 "一开始是有点难熬……希望你快点适应！" with dissolve
    scene schoolcanteen_start_26 with dissolve
    gg 3 "有你们两个在，我今天心情都好多了。暂时就让我跟着你们混吧。" with dissolve
    gg 3 "你们放学后一般做什么？"
    scene schoolcanteen_start_29 with dissolve
    li 1 "老实说，没什么特别的。" with dissolve
    scene schoolcanteen_start_30 with dissolve
    li 1 "一般就是在某个人家里待着，看看电影，或者去公园。"
    $ lillian_unlock += 1
    show screen rel_open_lillian
    scene schoolcanteen_start_26 with dissolve
    gg 3 "听起来不错。" with dissolve
    gg 3 "（或许该找时候叫上[li]一起玩。）"
    scene schoolcanteen_start_28 with dissolve
    leah 1 "我大部分时间都在家。玩玩电脑，或者看书。我真的很喜欢看书。" with dissolve
    scene schoolcanteen_start_27 with dissolve
    gg 3 "你现在在用手机看书？" with dissolve
    scene schoolcanteen_start_28 with dissolve
    leah 1 "哦，对！是一本关于龙的书。" with dissolve
    scene schoolcanteen_start_26 with dissolve
    $ leah_unlock = True
    leah 1 "龙之类的神话生物实在太有意思了。" with Dissolve(0.3)
    menu:
        '「我也喜欢这个。」\\n[blue](更多内容)':
            gg 3 "我也喜欢。我一直都对神话生物着迷。" with dissolve
            scene schoolcanteen_start_27 with dissolve
            leah 1 "嘿嘿，那太好了！" with dissolve
        '「原来如此。」':
            gg 3 '原来如此……'
    scene schoolcanteen_start_25 with dissolve
    li 1 "话说，[gg]，你为什么会来这里？" with dissolve
    li 1 "倒不是这里不好，恰恰相反。只是……太普通了？"
    scene schoolcanteen_start_26 with dissolve
    gg 3 "我和我妹妹一起来的。她也在这所学校读书，不过在别的班。" with dissolve
    scene schoolcanteen_start_25 with dissolve
    li 1"哦，那你们还能互相照应。总之，我觉得你会喜欢这里的。" with dissolve
    scene schoolcanteen_start_29 with dissolve
    li 1 "我们学校大部分学生都相处得不错，当然也有例外。"
    scene schoolcanteen_start_28 with dissolve
    leah 1 "确实。大部分学生都很友善，彼此也熟。" with dissolve
    scene schoolcanteen_start_26 with dissolve
    gg 3 "听你这么说我就放心了。不过我也没理由怀疑——我今天已经见识到了。" with dissolve
    scene schoolcanteen_start_31 with dissolve
    pause 2.0
    scene schoolcanteen_start_32 with dissolve
    li 1 "为新朋友干杯！" with dissolve
    show schoolcanteen_start_33 with Dissolve(0.1)
    $ renpy.pause(1,hard=True)
    scene schoolcanteen_start_34 with Dissolve(0.1)
    gg 3 "（该喝牛奶吗……）" with dissolve
    call screen schoolcanteen_start_screen

label schoolcanteen_start_choice_1:
    scene schoolcanteen_start_35 with Dissolve(0.1)
    ''
    show schoolcanteen_start_36 with Dissolve(0.1)
    $ renpy.pause(1.5,hard=True)
    jump after_schoolcanteen
    
label schoolcanteen_start_choice_2:
    play sound energy_vzal
    scene schoolcanteen_start_37 with Dissolve(0.1)
    pause 0.6
    leah 1 '{cps=5}……{/cps}' with dissolve
    scene schoolcanteen_start_38 with Dissolve(0.1)
    leah 1 '喂！' with dissolve
    scene schoolcanteen_start_39 with dissolve
    pause 1.6
    scene schoolcanteen_start_40 with Dissolve(0.1)
    ''
    show schoolcanteen_start_41 with Dissolve(0.1)
    $ renpy.pause(1.5,hard=True)
    jump after_schoolcanteen
    
label after_schoolcanteen:
    scene black with dissolve
    pause 2.0
    show schoolcanteen_start_42 with dissolve
    ''
    show schoolcanteen_start_43 with Dissolve(0.1)
    $ renpy.pause(6.5,hard=True)
    gg 3 "{cps=6}嗯？{/cps}" with dissolve
    gg 3 "（那个女生……刚才是在看我吗？）"
    gg 3 "（现在又装作没在看？）"
    gg 3 "{cps=5}……{/cps}"
    gg 3 "（她好像是我们班的。不知道在想什么。）"
    scene schoolcanteen_start_44 with dissolve
    gg 3 "（也许是我想多了。可以用手机相机确认一下……不过这样好像挺变态的……会被当成偷拍狂吧。）" with dissolve
    gg 3 "（干脆问问[li]她是谁。）"
    pause 1.0
    menu:
        "去问[li]":
            scene schoolcanteen_start_45 with dissolve
            gg 3 "[li]。"
            scene schoolcanteen_start_46 with dissolve
            gg 3 "看到那边那个端着咖啡的蓝发女生了吗？"
            scene schoolcanteen_start_47 with dissolve
            pause 1.0
            gg 3 "我总觉得她在往这边看。"
            scene schoolcanteen_start_48 with dissolve
            li 1 "[iz]在往这边看？看你？" with dissolve
            scene schoolcanteen_start_45 with dissolve
            gg 3 "至少在我看来是这样。"
            scene schoolcanteen_start_48 with dissolve
            li 1 "哈哈……也许吧。不过她不像是会留意新生的人。" with dissolve
        
        "用手机相机\\n[blue](更多内容)":
            show schoolcanteen_start_49 with Dissolve(0.1)
            $ renpy.pause(11,hard=True)
            show schoolcanteen_start_50 with Dissolve(0.1)
            hide schoolcanteen_start_49
            pause 1.0
            gg 3 "（哇，她其实超可爱的。）" with Dissolve(0.3)
            show schoolcanteen_start_51 with Dissolve(0.1)
            hide schoolcanteen_start_50
            pause 1.0
            gg 3 "（而且她真的在看我！）" with Dissolve(0.3)
            gg 3 "（她为什么要藏起来？）"
            li 1 "那个，[gg]，你在干什么？" with dissolve
            scene schoolcanteen_start_52 with Dissolve(0.1)
            li 1 "未经允许就拍别人可不礼貌。" with Dissolve(0.3)
            scene schoolcanteen_start_53 with dissolve
            gg 3 "嗯，我知道。只是那个女生好像先在看我。" with Dissolve(0.3)
            li 1 "说到底{cps=5}……{/cps}" with dissolve
            scene schoolcanteen_start_54 with dissolve
            li 1 "总之吧。那个女生叫[iz]。"
    
    scene schoolcanteen_start_53 with dissolve
    gg 3 "[iz]是吗？她在我们班？" with dissolve
    scene schoolcanteen_start_55 with dissolve
    li 1 "对，第三排第二个座位。" with dissolve
    li 1 "[iz]是皆崎集团董事长的孙女。那可是全国最大的企业之一。"
    li 1 "理所当然地很受欢迎。大概也是同样的原因，显得很疏离。"
    scene schoolcanteen_start_53 with dissolve
    gg 3 "没想到在这儿能遇到上流社会的人。" with dissolve
    scene schoolcanteen_start_54 with dissolve
    li 1 "她不是唯一一个。坐在她旁边的男生也和我们同班。" with dissolve
    li 1 "听说他是她爷爷身边某个亲信的儿子。"
    scene schoolcanteen_start_55 with dissolve
    li 1 "外人看可能像朋友，甚至是情侣。但我觉得他只是负责照看她、保证她安全。" with dissolve
    scene schoolcanteen_start_53 with dissolve
    gg 3 "就算是情侣我也不意外。[iz]确实很漂亮。" with dissolve
    scene schoolcanteen_start_56 with dissolve
    leah 1 "我同意，[gg]。[iz]真的美得没话说。" with dissolve
    scene schoolcanteen_start_57 with dissolve
    leah 1 "你不想去跟她说说话吗？也许她喜欢你呢？这可是你往上爬的好机会！" with dissolve
    scene schoolcanteen_start_58 with dissolve
    gg 3 "谢谢建议，但我觉得这不太合适。" with dissolve
    scene schoolcanteen_start_59 with dissolve
    li 1 "我也这么觉得。没必要惹上那种人，还是小心点好。" with dissolve
    scene schoolcanteen_start_60 with dissolve
    gg 3 "嗯，我可不想惹上什么麻烦。" with dissolve
    scene schoolcanteen_start_61 with dissolve
    leah 1 "你看起来挺圆滑的，[gg]。这正是我看重人的一点。" with dissolve
    scene schoolcanteen_start_62 with dissolve
    li 1 "总之，跟董事长孙女打交道要小心。她爷爷随便一句话，你轻则被开除。" with dissolve
    gg 3 "（不过我还是可以远远看着[iz]。）"
    scene schoolcanteen_start_56 with dissolve
    leah 1 "那你觉得[li]怎么样，[gg]？" with dissolve
    
    ### NEED SOME RENDERS
    li 1 "[leah]！我人就在这儿呢！" with dissolve
    leah 1 "嘿嘿……怎么样？" with dissolve
    
    menu:
        '「我觉得我们会成为朋友。\\n[gold](莉莲 +1)[gr](推荐)[blue](更多内容)」':
            scene schoolcanteen_start_63 with dissolve
            gg 3 "我觉得我们会成为朋友，[li]。" with dissolve
            show screen rel_up_lillian
            $ love_li += 1
            scene schoolcanteen_start_64 with dissolve
            li 1 "那当然！" with dissolve
            scene schoolcanteen_start_65 with dissolve
            pause 2.6
            scene schoolcanteen_start_66 with dissolve
            gg 3 '{cps=5}……{/cps}'
            scene schoolcanteen_start_67 with dissolve
            li 1 '{cps=5}……{/cps}'
            scene schoolcanteen_start_68 with dissolve
            li 1 "你刚才想说什么？" with dissolve
            menu:
                '「没。」':
                    scene schoolcanteen_start_69 with dissolve
                    gg 3 "没什么。" with dissolve
                    scene schoolcanteen_start_70 with dissolve
                    li 1 "也是……都上初中了再说“做朋友”总觉得有点别扭。" with dissolve
                    scene schoolcanteen_start_71 with dissolve
                    gg 3 "确实……" with dissolve
                    #scene schoolcanteen_start_72 with dissolve
                    li 1 '{cps=5}……{/cps}'
                    
                '「你很漂亮。」\\n[gold](莉莲 +2)':
                    scene schoolcanteen_start_73 with dissolve
                    gg 3 "说真的，我觉得你很漂亮，[li]。" with dissolve
                    scene schoolcanteen_start_74 with dissolve
                    li 1 "谢谢……这话真好听。" with dissolve
                    show screen rel_up_lillian
                    $ love_li += 2
                    scene schoolcanteen_start_75 with dissolve
                    li 1 '{cps=5}……{/cps}'
                    scene schoolcanteen_start_76 with dissolve
                    leah 1 "好可爱……" with dissolve
                    #scene schoolcanteen_start_77 with dissolve
                    #pause 2.0 
        '「她既可爱又漂亮。」\\n[gold](莉莲 +3)':
            scene schoolcanteen_start_73 with dissolve
            gg 3 "嗯，我觉得她既可爱又漂亮。" with dissolve
            gg 3 "而且我还想更了解你一点，[li]。"
            show screen rel_up_lillian
            $ love_li += 3
            scene schoolcanteen_start_74 with dissolve
            li 1 "哦，[gg]……你真会说话。" with dissolve
            scene schoolcanteen_start_75 with dissolve
            li 1 '{cps=5}……{/cps}'
            scene schoolcanteen_start_76 with dissolve
            leah 1 "好可爱……" with dissolve
            scene schoolcanteen_start_77 with dissolve
            pause 2.0
    
    scene schoolcanteen_start_78 with dissolve
    leah 1 "啊，快到午休结束时间了。大家都要出食堂了。" with dissolve
    scene schoolcanteen_start_79 with dissolve
    li 1 "那我们也不能磨蹭了！第一天就迟到可不好，对吧，[gg]？" with dissolve
    li 1 "下一节课八分钟后开始。"
    scene schoolcanteen_start_80 with dissolve
    gg 3 "谢谢你们叫上我一起坐。我很开心。" with dissolve
    scene schoolcanteen_start_81 with dissolve
    li 1 "嗯，教室里见。" with dissolve
    stop music fadeout 3
    stop music2 fadeout 3
    
## Minami nty
    scene black with dissolve
    pause 1.0
    play sound2 schooldoor volume 0.5
    pause 2.0
    scene school_class_teacher_0 with dissolve
    pause 2.0
    play sound woosh3 volume 0.3
    scene school_class_teacher_1 with PushMove(0.2, 'pushleft')
    pause 2.0
    play sound2 kinkonkankon_outin
    play sound3 city_bird fadein 1 volume 0.6
    scene school_zvonok_2
    $ renpy.pause(5.5, hard=True)
    stop sound3 fadeout 2
    play sound kabluk
    play music school_fon fadein 5
    scene school_class_teacher_2 with Dissolve(0.3)
    pause 2.0
    scene school_class_teacher_3 with Dissolve(0.3)
    mi0 1 "同学们下午好。请回到座位上，把作业本准备好。" with Dissolve(0.3)
    scene school_class_teacher_4 with Dissolve(0.3)
    pause 0.6
    gg 3 "（她挺漂亮的……）" with Dissolve(0.3)
    scene school_class_teacher_5 with Dissolve(0.3)
    pause 0.6
    scene school_class_teacher_6 with dissolve
    mi0 1 "既然班上来了一位新同学，我重新自我介绍一下。" with Dissolve(0.3)
    mi0 1 "我是栗原美波，你们的外语老师。"
    stop music fadeout 2
    scene black with dissolve
    pause 1.6
    scene school_class_teacher_7 with dissolve
    pause 1.6
    scene school_class_teacher_8 with Dissolve(0.3)
    pause 1.6
    play music school_fon fadein 5
    scene school_class_teacher_9 with Dissolve(0.3)
    cm1 1 "走廊里吵什么这么大声？" with Dissolve(0.3)
    scene school_class_teacher_10 with dissolve
    cm1 1 "把我午觉吵醒了。" with Dissolve(0.3)
    scene school_class_teacher_11 with dissolve
    pause 1.0
    scene school_class_teacher_12 with hpunch
    cm1 1 "他妈吵死了！"
    scene school_class_teacher_13 with Dissolve(0.3)
    pause 1.6
    scene school_class_teacher_14 with dissolve
    cm1 1 "栗原老师，我能去一下厕所吗？" with Dissolve(0.3)
    scene school_class_teacher_15 with Dissolve(0.3)
    pause 0.8
    scene school_class_teacher_16 with Dissolve(0.3)
    with Dissolve(0.3)
    pause 1.0
    scene school_class_teacher_17 with Dissolve(0.3)
    with Dissolve(0.3)
    mi 1 "不行。这节课还剩十五分钟。" with Dissolve(0.3)
    scene school_class_teacher_18 with Dissolve(0.3)
    cm2 1 "喂，你什么意思？" with Dissolve(0.3)
    cm2 1 "你怕什么？"
    scene school_class_teacher_19 with Dissolve(0.3)
    cm1 1 "是[da]！"
    scene school_class_teacher_20 with hpunch
    play music deadly_roulette_by_kevin_macleod
    da 1 "哟，你们这群杂种！[ken]在哪儿？！"
    scene school_class_teacher_4
    pause 0.5
    gg 3 "（本地的小混混来了。果然准时。）" with Dissolve(0.3)
    scene school_class_teacher_21
    ''
    scene school_class_teacher_22 with hpunch
    mi 1 "这是干什么？！给我滚出教室！"
    scene school_class_teacher_23 with Dissolve(0.3)
    da 1 "栗原老师，今天您格外迷人啊。" with Dissolve(0.3)
    scene school_class_teacher_24 with Dissolve(0.3)
    mi 1 "立刻离开教室，不然我就叫校长了！" with Dissolve(0.3)
    scene school_class_teacher_25 with Dissolve(0.3)
    da 1 "哎哟，栗原老师，您可真会说话。" with Dissolve(0.3)
    sh0 1 "是想勾引你男朋友吗？" with Dissolve(0.3)
    scene school_class_teacher_26 with Dissolve(0.3)
    mi 1 "你竟敢这样跟我说话？！" with Dissolve(0.3)
    scene school_class_teacher_27 with Dissolve(0.3)
    gg 3 "这里经常这样吗？学生真的这么不尊重老师？" with Dissolve(0.3)
    scene school_class_teacher_28 with dissolve
    li 1 "[da]那伙人是[ry]的狗腿子。" with Dissolve(0.3)
    scene school_class_teacher_29 with dissolve
    li 1 "没人管得了。" with Dissolve(0.3)
    scene school_class_teacher_28 with dissolve
    li 1 "在这所学校里，他们才是规矩。" with Dissolve(0.3)
    scene school_class_teacher_30 with dissolve
    li 1 "看到我前面那个被他们盯上的人了吗？" with Dissolve(0.3)
    li 1 "他叫[ken]。少数几个没向他们低过头的学生之一。"
    scene school_class_teacher_31 with PushMove(0.2, 'pushleft')
    da 1 "你这个王八蛋，已经忘了老子对你做过什么了吗？！" with Dissolve(0.3)
    scene school_class_teacher_32 with Dissolve(0.2)
    da 1 "缺了整整一周的课，现在又嚣张起来了？" with Dissolve(0.3)
    scene school_class_teacher_33 with Dissolve(0.2)
    da 1 "我他妈受够你了！要不要我再一次让你“睡着”回家？！"
    scene school_class_teacher_34
    ken 1 '{cps=5}……{/cps}'
    scene school_class_teacher_35 with Dissolve(0.2)
    da 1 "跟我走，你个混蛋。" with Dissolve(0.3)
    play sound skrip_stula volume 0.2
    scene school_class_teacher_36 with Dissolve(0.2)
    da 1 "不想在你全班同学面前丢脸的话。" with Dissolve(0.3)
    scene school_class_teacher_37 with dissolve
    pause 1.6
    scene school_class_teacher_38 with vpunch
    da 1 "你……" with Dissolve(0.3)
    if nastupil_nogu:
        scene school_class_teacher_38_1
        da 1 "听说有人踩了我们小猪猪的脚……希望没踩得太疼，宝贝？" with Dissolve(0.3)
        dai 1 '{cps=5}……{/cps}' with Dissolve(0.3)
        scene school_class_teacher_39 with dissolve
        da 1 "挺有种的新人……跟我来。我们带你参观一下，顺便教你点本地……规矩。" with Dissolve(0.3)
    else:
        scene school_class_teacher_38_2
        da 1 "哟，看，新来的。你知道的，我们偶尔也会给像你这样的人“参观讲解”——带你们看看学校和它的规矩，懂吧。" with Dissolve(0.3)
        scene school_class_teacher_39 with dissolve
        da 1 "你跟我们走。" with Dissolve(0.3)
    menu:
        '「没。」':
            scene school_class_teacher_40
            gg 3 "不。" with Dissolve(0.3)
            scene school_class_teacher_41
            pause 0.3
            play sound padenie_hlama volume 0.6
            pause 0.3
            scene school_class_teacher_42 with vpunch
            da 1 "起来……" with Dissolve(0.1)
            scene school_class_teacher_43
            pause 0.5
            play sound zahvat_1 volume 0.4
            scene school_class_teacher_44 with dissolve
            da 1 "……然后跟我走！" with Dissolve(0.1)
        '「带路吧。」':
            scene school_class_teacher_40
            gg 3 "带路吧。" with Dissolve(0.3)
            scene school_class_teacher_41
            pause 0.3
            play sound padenie_hlama volume 0.6
            pause 0.3
            scene school_class_teacher_42 with vpunch
            da 1 "我这就……" with Dissolve(0.1)
            scene school_class_teacher_43
            pause 0.5
            play sound zahvat_1 volume 0.4
            scene school_class_teacher_44 with dissolve
            da 1 "……帮你起来！" with Dissolve(0.1)
    play sound zahvat_2 volume 0.4
    scene school_class_teacher_45 with hpunch
    gg 3 "滚开。" with Dissolve(0.1)
    play sound zahvat_2 volume 0.3
    scene school_class_teacher_46 with hpunch
    gg 3 "野蛮的混蛋！" with Dissolve(0.1)
    scene school_class_teacher_47
    iz 1 "住手！他才刚来，什么都不懂！" with Dissolve(0.1)
    scene school_class_teacher_48
    li 1 "[da]，住手！他什么都没做！" with Dissolve(0.1)
    scene school_class_teacher_49
    pause 1
    scene school_class_teacher_50 with dissolve
    pause 1
    scene school_class_teacher_51 with dissolve
    da 1 "女士们……" with Dissolve(0.3)
    scene school_class_teacher_52
    li 1 "（真恶心。）" with Dissolve(0.3)
    scene school_class_teacher_53
    da 1 "别急，等我收拾完他们，再来找你。" with Dissolve(0.3)
    scene school_class_teacher_54
    iz 1 '{cps=5}……{/cps}'
    scene school_class_teacher_55
    li 1 "混蛋。" with Dissolve(0.3)
    scene school_class_teacher_56
    da 1 "哟，还挺会来事？已经跟女生混熟了？现在还护上你了。怂货。" with Dissolve(0.1)
    play sound zahvat_2 volume 0.2
    scene school_class_teacher_57 with Dissolve(0.2)
    gg 3 '{cps=5}……{/cps}' with Dissolve(0.3)
    scene school_class_teacher_58
    with Dissolve(0.2)
    gg 3 "少废话，带路。" with Dissolve(0.3)
    scene school_class_teacher_59 with dissolve
    da 1 '噗哈哈哈哈。'
    scene school_class_teacher_60 with dissolve
    da 1 "再见了，栗原老师。" with Dissolve(0.3)
    scene school_class_teacher_61
    mi 1 '{cps=5}……{/cps}' with Dissolve(0.3)
    mi "（再撑一会儿……）"
    stop music fadeout 10
    show black with dissolve
    pause 1.6
    
## Roof
    play music3 city_bird fadein 6
    scene school_roof_da_0 with dissolve
    pause 2.0
    scene school_roof_da_1
    pause 2.0
    scene school_roof_da_2
    da 1 "[sh]，守住楼梯，别让人上来。" with Dissolve(0.1)
    scene school_roof_da_3 with Dissolve(0.3)
    sh 1 "我们带那两个人先走。这边你自己应付。" with Dissolve(0.1)
    scene school_roof_da_4 with Dissolve(0.3)
    da 1 "明白。" with Dissolve(0.3)
    scene school_roof_da_5
    da 1 "去跟新人聊聊天吧。" with Dissolve(0.1)
    scene school_roof_da_6 with Dissolve(0.3)
    da 1 "[ken]，过来！" with Dissolve(0.1)
    scene school_roof_da_7
    ken 1 "抱歉，把你牵扯进来了。" with Dissolve(0.3)
    scene school_roof_da_8 with Dissolve(0.3)
    gg 3 "不是你的错。" with Dissolve(0.3)
    scene school_roof_da_9 with Dissolve(0.3)
    ken 1 "也许吧……不过万一你受伤了，治疗费我出，别担心。" with Dissolve(0.3)
    scene school_roof_da_10
    gg 3 "（我知道接下来会怎样……不过这小子已经彻底被打趴了。）" with Dissolve(0.3)
    gg 3 "（打架的时候，跑是最实用的本事。）"
    gg 3 "（初中时我短跑成绩很好。但把这小子一个人丢给两个人太不仗义。）"
    gg 3 "（而且他们随时都能回教室，跑了也没意义。）"
    $ renpy.music.set_volume(1, delay=3, channel=u'music3')
    scene school_roof_da_11 with hpunch
    bully1 1 "我在跟你说话！"
    $ renpy.music.set_volume(0.3, delay=6, channel=u'music3')
    play music march_on_utopia_loop_by_troyificus fadein 6 volume 0.7
    show school_roof_da_12
    bully1 1 "新人，吓尿裤子了？" with Dissolve(0.1)
    bully1 1 "哪儿来的？"
    gg 3 "（他想用说话拖住我……然后在最糟的时机动手。）" with Dissolve(0.3)
    gg 3 "（别再想了，先动手再说。）"
    bully1 1 "喂，哑巴了！？你他妈到底哪儿来的？"
    
    $ timer_range = 10
    $ timez = 10
    $ timer_jump = 'school_roof_ebanat_loose'
    show screen countdown
    $ timeout_label = 'school_roof_ebanat_loose'
    $ timeout = 10
    menu:
        bully1 1 '你他妈什么来头？' with Dissolve(0.3)
        '「不关你的事」':
            hide screen countdown
            bully1 1 "我客客气气跟你说话，你就这么回我？" with Dissolve(0.3)
            bully1 1 "算了，我速战速决。"
        '「我妈那边的。」':
            hide screen countdown
            bully1 1 "哈，不赖。我也是。" with Dissolve(0.3)
            bully1 1 "算了，我速战速决。"
            
        '[gr]出拳':
            hide screen countdown
            show school_roof_ebanat_win
            pause 4.7
            jump roof_boi

label school_roof_ebanat_loose:
    show school_roof_ebanat_loose
    pause 5.0
    jump roof_proebal
    
## Roof - draka
label roof_boi:

    scene school_roof_boi_1 with Dissolve(0.2)
    ''
    scene school_roof_boi_2 with hpunch
    gg 3 "放开他，刺猬头！"
    scene school_roof_boi_3
    pause 1.6
    scene school_roof_boi_4 with Dissolve(0.2)
    da 1 "你彻底疯了？活腻了？" with Dissolve(0.1)
    scene school_roof_boi_5
    gg 3 "（他体格和体重都占优……但这不算什么。）" with Dissolve(0.3)
    gg "（如果他从没练过运动，就不用担心。）"
    gg "（好了，别想了。不能再浪费时间，得动手。）"
    show fight_start
    stop music fadeout 1.5
    play music2 last_minute_failure_loop_by_troyificus fadein 2
    play sound 'audio/sound/woosh0.ogg' volume 0.7
    pause 1.2
    
## Roof - Draka Jabrayile 1
label school_roof_boi_start:
    $ timer_range = 3
    $ timez = 3
    $ timer_jump = 'roof_proebal'
    
    show screen countdown
    call screen school_roof_boi_1()
    jump roof_proebal

## Roof - Draka Jabrayile 2
label school_roof_boi_block:
    $ timer_range = 1.5
    $ timez = 1.5
    $ timer_jump = 'roof_proebal'
    
    show fight_block
    show screen countdown
    call screen school_roof_boi_2()
    
    jump roof_proebal
    
### Roof - Draka Jabrayile Punch
label school_roof_boi_punch:
    show fight_punch:
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 2.0 zoom 1.02
    pause 2.0
    stop music2 fadeout 6
    play music march_on_utopia_loop_by_troyificus fadein 13 volume 0.5
    scene school_roof_boi_7 with vpunch
    da 1 "呃！"
    scene school_roof_boi_8 with Dissolve(0.3)
    da 1 "好快……混蛋。" with Dissolve(0.1)
    scene school_roof_boi_9 with Dissolve(0.3)
    gg 3 "（他还想继续？）" with Dissolve(0.3)
    play sound snial_obuv
    scene school_roof_boi_10
    ''
    scene school_roof_boi_9
    gg 3 "（他在干什么？）" with Dissolve(0.1)
    scene school_roof_boi_11
    da 1 "我现在就废了你，臭屎蛋！" with Dissolve(0.1)
    scene school_roof_boi_12
    gg 3 "（他脱了鞋，光着脚站在那儿……）" with Dissolve(0.3)
    gg "（彻底的白痴？）"
    play sound2 whatsapp_roof
    scene school_roof_boi_13
    pause 1.6
    scene school_roof_boi_14 with Dissolve(0.3)
    pause 1.6
    scene school_roof_boi_15 with Dissolve(0.3)
    da 1 "算你走运，新人，保安马上就要来了。" with Dissolve(0.3)
    scene school_roof_boi_16
    da 1 "等我逮到你，就把你全身骨头一根根敲碎！" with Dissolve(0.3)
    scene school_roof_boi_12
    gg 3 '{cps=5}……{/cps}' with Dissolve(0.3)
    stop music fadeout 5
    
    jump roof_win

### Roof Loose
label roof_proebal:

    stop music fadeout 3
    stop music2 fadeout 3
    stop music3 fadeout 3
    play sound 'audio/sound/punch.ogg'
    scene black with dissolve
    pause 1.6
    $ draka_roof_loose = True
    pause 1.0
    show school_roof_loose_nm_1
    pause 5.0
    scene black with dissolve
    mi 1 '[ken]！' with Dissolve(0.3)
    pause 2.0
    show school_roof_loose_nm_2
    pause 5.0
    pause 2.0
    $ renpy.music.set_volume(0.3, delay=1, channel=u'music3')
    play music3 city_bird volume 0.7 fadein 1
    scene school_roof_loose_1 with dissolve
    mi 1 '[gg]？' with Dissolve(0.3)
    scene school_roof_loose_2 with dissolve
    mi 1 '[gg]，你怎么了？' with Dissolve(0.3)
    scene black with dissolve
    $ renpy.music.set_volume(0, delay=3, channel=u'music3')
    pause 1.6
    gg 3 '（又是这种梦……）' with Dissolve(0.3)
    pause 1.6
    gg 3 "（每次都一模一样。）" with Dissolve(0.3)
    $ renpy.music.set_volume(0.3, delay=1, channel=u'music3')
    scene school_roof_loose_3 with dissolve
    mi 1 "搞不明白，他这是怎么了？" with Dissolve(0.3)
    scene school_roof_loose_4 with dissolve
    mi 1 "[ken]，[da]对他做了什么？" with Dissolve(0.3)
    scene black with dissolve
    $ renpy.music.set_volume(0, delay=1, channel=u'music3')
    pause 1.6
    $ renpy.music.set_volume(0.3, delay=1, channel=u'music3')
    scene school_roof_loose_5 with vpunch
    mi 1 "[gg]，醒醒！" with Dissolve(0.3)
    $ renpy.music.set_volume(1, delay=3, channel=u'music3')
    scene school_roof_loose_6 with dissolve
    mi 1 "你们两个都得去医务室！我带你们过去！" with Dissolve(0.3)
    scene school_roof_loose_7 with dissolve
    gg 3 "我没事。" with Dissolve(0.3)
    scene school_roof_loose_8 with dissolve
    mi 1 "不行，这没得商量！" with Dissolve(0.3)
    scene school_roof_loose_7 with dissolve
    gg 3 "我完全没事。" with Dissolve(0.3)
    scene school_roof_loose_9
    pause 1.3
    scene school_roof_loose_10 with dissolve
    pause 0.3
    scene school_roof_loose_11 with dissolve
    pause 1.3
    scene school_roof_loose_12
    pause 0.6
    scene school_roof_loose_13 with dissolve
    pause 1.3
    scene school_roof_loose_14
    pause 1.6
    scene school_roof_loose_15 with dissolve
    mi 1 "（他身上一点伤都没有。）" with Dissolve(0.3)
    stop music3 fadeout 2
    scene black with dissolve
    pause 2.0
    play music japan_streets_2 volume 5.0 fadein 3
    pause 1.0
    scene outside_ken_0 with dissolve
    ''
    scene outside_ken_1
    play music japan_streets_1 volume 3.0
    play sound 'audio/sound/energy_vzal.ogg'
    ken 2 "给，同学。虽不能弥补什么，但眼下我只能做这些了。" with Dissolve(0.3)
    scene outside_ken_2 with dissolve
    gg 3 "谢了。别觉得还欠我什么。" with Dissolve(0.3)
    scene outside_ken_3 with dissolve
    ken 2 "算了……抱歉搞成这样。要不是他们先冲我来，也不会找你麻烦。" with Dissolve(0.3)
    play sound 'audio/sound/energy_open.ogg'
    pause 1.0
    scene outside_ken_4 with dissolve
    play sound 'audio/sound/energy_glot.ogg'
    pause 2.3
    scene outside_ken_5 with dissolve
    gg 3 "反正我这种新来的，迟早要经历这场“参观”。他们只是想立威而已。" with Dissolve(0.3)
    scene outside_ken_6_loose with dissolve
    gg 3 "不过，有件事你或许能帮我。" with Dissolve(0.3)

    jump sujet_1

## Roof Win

label roof_win:

    scene school_roof_pobedili_1 with fade
    pause 2.0
    $ renpy.music.set_volume(1, delay=3, channel=u'music3')
    scene school_roof_pobedili_2 with fade
    pause 2.0
    scene school_roof_pobedili_3
    mi 1 "什、什么？" with Dissolve(0.1)
    scene school_roof_pobedili_4 with dissolve
    mi 1 '这里以前发生过什么？' with Dissolve(0.3)
    stop music3 fadeout 2
    scene black with dissolve
    pause 3.0
    play music japan_streets_2 volume 5.0 fadein 3
    pause 1.0
    scene outside_ken_0 with dissolve
    ''
    scene outside_ken_1
    play music japan_streets_1 volume 3.0
    play sound 'audio/sound/energy_vzal.ogg'
    ken 2 "给你，哥们。" with Dissolve(0.3)
    scene outside_ken_2 with dissolve
    gg 3 '谢了。' with Dissolve(0.3)
    scene outside_ken_3 with dissolve
    ken 2 "不用。谢你今天出手。你把他们整惨了。你是练过空手道什么的吗？" with Dissolve(0.3)
    play sound 'audio/sound/energy_open.ogg'
    pause 1.0
    scene outside_ken_4 with dissolve
    play sound 'audio/sound/energy_glot.ogg'
    pause 2.3
    scene outside_ken_5 with dissolve
    gg 3 "算是吧。话说回来，我可不是白帮忙的。" with Dissolve(0.3)
    scene outside_ken_6_win with dissolve
    gg 3 "那就欠你一次。" with Dissolve(0.3)
    jump sujet_1

## Story con
label sujet_1:

    scene outside_ken_7 with dissolve
    ken 2 "行啊，说吧，要什么？" with Dissolve(0.3)
    scene outside_ken_8 with dissolve
    gg 3 '情报！' with Dissolve(0.3)
    scene outside_ken_9 with dissolve
    pause 1.6
    gg 3 "我刚转学过来。之前的学校从没发生过这种事。" with Dissolve(0.3)
    scene outside_ken_9_1 with dissolve
    gg 3 "我看得出来这儿的校霸称霸。还有什么新生该知道的吗？"
    scene outside_ken_10 with dissolve
    ken 2 "那就先从你已经知道的[da]说起吧。他和那几个刺头一般单独行动，但有时也会一起上。" with Dissolve(0.3)
    scene outside_ken_11 with dissolve
    ken 2 "大多数时候，他们听另一个人的指挥。他叫[ry]——是这个小团体的头目。" with Dissolve(0.3)
    scene outside_ken_12 with dissolve
    gg 3 "哦对，那家伙到底是谁？" with Dissolve(0.3)
    gg 3 "（[li]以前提过他，不过当时我没在意。）"
    scene outside_ken_13 with dissolve
    ken 2 "一个被宠坏的富二代和一个白痴。等一下。" with Dissolve(0.3)
    scene outside_ken_14 with dissolve
    ken 2 "给，看看这个。" with Dissolve(0.3)
    gg 3 "一个高中生哪来这么多现金？" with Dissolve(0.3)
    scene outside_ken_14_1
    ken 2 "投胎投得好。他是什么CEO的儿子，那家公司是这所学校的赞助商。" with Dissolve(0.3)
    scene outside_ken_14_2
    ken 2 "所以[ry]在这学校为所欲为。老师和校长通常都对他的胡闹睁一只眼闭一只眼。" with Dissolve(0.3)
    scene outside_ken_14_3
    ''
    gg 3 "这张照片是两年前拍的……" with Dissolve(0.3)
    scene outside_ken_15
    gg 3 "所以他现在和我们一样是高三？" with Dissolve(0.3)
    scene outside_ken_16 with dissolve
    ken 2 '没错。' with Dissolve(0.3)
    scene outside_ken_17 with dissolve
    gg 3 '明白。' with Dissolve(0.3)
    scene outside_ken_18 with dissolve
    ken 2 "还想知道什么？先说清楚，我也不是什么都知道。至于八卦，你最好去问女生。" with Dissolve(0.3)
    scene outside_ken_19 with dissolve
    $ kens_question_about_girls = []
    menu kens_question_about_girls:
        set kens_question_about_girls
        '「[li]和[iz]。」':
            gg 3 "你认识[li]和[iz]？" with Dissolve(0.3)
            scene outside_ken_20 with dissolve
            ken 2 "这两个人啊……" with Dissolve(0.3)
            scene outside_ken_21 with dissolve
            ken 2 "[li]没什么特别的。" with Dissolve(0.3)
            scene outside_ken_18 with dissolve
            ken 2 "校花之一，学习也好。看起来没有男朋友，不过没人知道确切情况。" with Dissolve(0.3)
            scene outside_ken_21 with dissolve
            ken 2 "平时只和女生一起玩，根本不搭理男生。在我看来就是个普通女孩。" with Dissolve(0.3)
            scene outside_ken_22 with dissolve
            ken 2 "但[iz]就不一样了——谁都知道她，是本校的风云人物。可即便如此，也没人真正了解她。她不让人靠近。" with Dissolve(0.3)
            scene outside_ken_20 with dissolve
            ken 2 "她要跟谁说话，也就是身边那个跟班。偶尔跟别人搭几句话，仅此而已。" with Dissolve(0.3)
            scene outside_ken_18 with dissolve
            ken 2 "今天她居然为你说话，倒是挺让人意外的。这还是头一回！" with Dissolve(0.3)
            scene outside_ken_19 with dissolve
            gg 3 "她有什么特别的？" with Dissolve(0.3)
            scene outside_ken_22 with dissolve
            ken 2 "她是皆崎集团董事长的孙女。而且美得像帝苑山巅的那朵幽兰。" with Dissolve(0.3)
            scene outside_ken_21 with dissolve
            ken 2 "其他的我就不知道了。" with Dissolve(0.3)
            scene outside_ken_18 with dissolve
            ken 2 "还想知道别的吗？" with Dissolve(0.3)
            $ kens_question_about_girls_point += 1
            scene outside_ken_19 with dissolve
            
            jump kens_question_about_girls
            
        '「[mi]。」':
            gg 3 "[mi]多大年纪？" with Dissolve(0.3)
            scene outside_ken_23 with dissolve
            ken 2 "栗原老师？" with Dissolve(0.3)
            scene outside_ken_24 with dissolve
            ken 2 "哈哈哈，不知道。她刚来我们学校的时候，老有人把她当成学生。" with Dissolve(0.3)
            scene outside_ken_22 with dissolve
            ken 2 "你真该看看那个想泡她的家伙，被她直接送去校长室时的表情。" with Dissolve(0.3)
            scene outside_ken_23 with dissolve
            gg 3 "换成我也怪不了他。" with Dissolve(0.3)
            scene outside_ken_25 with dissolve
            ken 2 "看来你偏好年长的女人啊？" with Dissolve(0.3)
            $ kens_question_about_girls_point += 1
            scene outside_ken_19 with dissolve
            
            jump kens_question_about_girls
        
        '「就这些。」' if kens_question_about_girls_point == 1:
            pause 1.0
    
    gg 3 "好。就这些。" with Dissolve(0.3)
    scene outside_ken_23 with dissolve
    ken 2 "你想知道的净是女生的事……你也是花花公子？" with Dissolve(0.3)
    ## new
    scene outside_ken_19 with dissolve
    gg 3 "今天早上之前我还真不是。" with Dissolve(0.3)
    scene outside_ken_21 with dissolve
    ken 2 "嗯，你确实长得好看，这点没得争。新来的第一天就动手打架……你不担心招来太多女生注意？" with Dissolve(0.3)
    scene outside_ken_23 with dissolve
    gg 3 "你说得像我是万人迷似的。" with Dissolve(0.3)
    scene outside_ken_22 with dissolve
    ken 2 "哼，要不要赌一下又会有美女主动贴上来？我押一罐咖啡。" with Dissolve(0.3)
    scene outside_ken_19 with dissolve
    gg 3 "行吧，好，我就跟你赌这个。" with Dissolve(0.3)
    
    scene outside_ken_26 with vpunch
    may 3 '[gg]！'
    scene outside_ken_27 with dissolve
    may 3 "太好了你还在！" with Dissolve(0.3)
    scene outside_ken_28 with dissolve
    pause 1
    ken 2"看来明天有免费饮料喝了。这大概是我赢过最轻松、也最心痛的一罐咖啡。" with Dissolve(0.3)
    scene outside_ken_29
    gg 3 "课上得怎么样？" with Dissolve(0.3)
    scene outside_ken_30 with dissolve
    may 3 "一切都超棒！我们班有很多很酷的女生——希望我们能成为朋友！" with Dissolve(0.3)
    show outside_ken_29 with dissolve
    gg 3 "替你高兴。" with Dissolve(0.3)
    scene outside_ken_31
    pause 1.3
    scene outside_ken_32 with dissolve
    ken 2 "你女朋友？" with Dissolve(0.3)
    scene outside_ken_31 with dissolve
    gg 3 "这是[may]，我的好姐妹。我们一起来的。" with Dissolve(0.3)
    scene outside_ken_33 with dissolve
    ken 2 "哦！我完全理解错了……抱歉！" with Dissolve(0.3)
    scene outside_ken_34 with dissolve
    ken 2 "你好，很高兴认识你。" with Dissolve(0.3)
    scene outside_ken_35 with Dissolve(0.3)
    ken 2 "你知道你这位朋友有多厉害吗？" with Dissolve(0.3)
    scene outside_ken_36 with dissolve
    may 3 "你好。当然知道啦！" with Dissolve(0.3)
    scene outside_ken_37 with Dissolve(0.3)
    ken 2 "我们今天有一点点……小冒险。不过[gg]毫发无伤，所以没事。" with Dissolve(0.3)
    scene outside_ken_30 with Dissolve(0.3)
    may 3 "……好吧，这事我们可得好好聊聊。对吧，[gg]？" with Dissolve(0.3)
    scene outside_ken_29 with Dissolve(0.3)
    gg 3 "当然。太谢了，[ken]。" with Dissolve(0.3)
    scene outside_ken_38 with Dissolve(0.3)
    ken 2 "咳咳！总之我也该回家了，不耽误你们了。" with Dissolve(0.3)
    scene outside_ken_39 with dissolve
    gg 3 "明天见。" with Dissolve(0.3)
    scene outside_ken_40 with Dissolve(0.3)
    may 3 "该回家了。路上你得把今天的事全讲给我听。" with Dissolve(0.3)
    stop music fadeout 5
    scene black with dissolve
    pause 2.0
    play sound door_close
    pause 1.0
    play sound divan_sit
    pause 1.0
    scene sweethome_1 with Dissolve(2.0):
        center
        yalign 0.1
        ease 5.0 yalign 0.8
    play music love_ballad_2_by_frank_schroeter fadein 8
    pause 2.0
    scene sweethome_2 with Dissolve(1.0)
    pause 1.0
    scene sweethome_3 with Dissolve(0.3)
    pause 1.0
    gg 3 "（今天真是充满了新鲜感。）" with dissolve
    gg 3 "（见面、介绍、一张张新面孔……谁能想到转学第一天会这么精彩？）"
    scene sweethome_4 with Dissolve(0.3)
    gg 3 "（第一天，我就打了一架、认识了一个可能成为朋友的人（有着火神之子般的眼眸），还见到了班里的美女。）"
    gg 3 "（在所有可能的展开里，这已经算相当不错了。）"
    scene sweethome_l_1 with Dissolve(0.3)
    gg 3 "（不管今天遇上什么麻烦，都盖不过[li]留下的那份明亮印象……）" with dissolve
    #scene sweethome_l_2 with Dissolve(0.5)
    gg 3 "（她就像一缕春日阳光，照暖了身边的一切。）"
    #scene sweethome_l_3 with Dissolve(0.5)
    gg 3 "（能坐在她旁边纯属运气好。我敢肯定，我们很快会更了解彼此。）"
    scene sweethome_m_1 with Dissolve(0.3)
    gg 3 "（还有[mi]……她简直就像从时尚杂志里走出来的——直接从「青年教师」那一页。）" with dissolve  
    #scene sweethome_m_2 with Dissolve(0.3)
    gg 3 "（而且她高雅得不得了！原来这种女人不只是电视剧里的设定。）"
    gg 3 "（她看起来很严厉，但那只是敬业而已。）"
    #scene sweethome_m_3 with Dissolve(0.3)
    gg 3 "（要是能看到她私下里的样子就好了。如果她性格真像看上去那么好，绝对是人间极品！）"
    gg 3 "（不过现在，还是在教室里欣赏就好。）"
    scene sweethome_5 with Dissolve(1.0):
        xalign 0.5
        yalign 0.3
        zoom 1.2
        ease 4.0 zoom 1
    gg 3 "（至于[may]……说真的，她总让我刮目相看。）" with dissolve
    scene sweethome_6 with Dissolve(0.3)
    gg 3 "（[may]面对最近接踵而来的麻烦，永远都是那么从容。）" with dissolve
    gg 3 "（她一直都很机灵能干，但能再次看到她眼里的那股光，还是让人很安心。）"
    scene sweethome_7 with Dissolve(0.3)
    gg 3 "（我觉得[may]会做得很好——学业上，交朋友上都是。）" with Dissolve(0.3)
    scene sweethome_8 with Dissolve(0.3)
    gg 3 "（不过我还是得多照看她。她得知道，不管什么时候她都能依靠我。）" with Dissolve(0.3)
    gg  3 "{cps=5}……{/cps}"

    gg 3 "（我记得小时候有件事。父亲经常出差，家里就留了个保姆照看我们。）"
    gg "（那天傍晚外面下着瓢泼大雨，家里的门被锁上了。）"
    
    gg 3 "（保姆忙了一整天，累得在沙发上睡着了，大概以为我们已经睡了。）"
    gg 3 "（可是那天晚上[may]……她想在水坑里踩着水跑一遍。）"
    
    gg 3 "（我记得她那个眼神……那双像小猫一样的眼睛，央着我陪她出去淋雨。）"
    gg 3 "（我怎么可能拒绝她？）"
    
    gg 3 "（好在房子只有一层，我只要打开窗户就行，不会吵醒保姆。）"
    gg 3 "（我先翻出去，再拉[may]上来。那一刻她脸上的幸福！任何言语都无法形容。）"
    scene sweethome_8 with Dissolve(1.0)
    pause 1.0
    gg 3 "（结果当然是我们俩都湿透了。回去的时候，只有一脸担忧又生气的保姆在等着。）" with Dissolve(0.3)
    scene sweethome_9 with Dissolve(0.3)
    gg 3 "（但就算她再凶，也盖不过那一天的快乐。）"
    scene sweethome_10 with Dissolve(0.3)
    gg 3 "（啊，偶尔回忆一下从前还挺不错。这种时刻的价值，都是等它彻底过去之后才明白的。）"
    scene sweethome_11 with Dissolve(0.3)
    may 3 "没事吧，[gg]？" with Dissolve(0.3)
    may 3 "你已经盯着窗外看了十分钟了。" with Dissolve(0.3)
    scene sweethome_12 with Dissolve(0.3)
    gg 3 "哦，没事。就是有点走神。" with Dissolve(0.3)
    scene sweethome_13 with Dissolve(0.3)
    may 3 "想什么呢？" with Dissolve(0.3)
    scene sweethome_12 with Dissolve(0.3)
    gg 3 "想我们上学第一天的事，还有今天过得怎么样。" with Dissolve(0.3)
    scene sweethome_14 with Dissolve(0.3)
    may 3 "天哪，今天真是漫长。不过现在终于可以放松了！" with Dissolve(0.3)
    scene sweethome_15 with Dissolve(0.3)
    may 3 "不过可惜我们被分到了不同的班。" with Dissolve(0.3)
    scene sweethome_16 with Dissolve(0.3)
    gg 3 "课间还能见面，所以也没关系。" with Dissolve(0.3)
    gg 3 "说不定是故意分开的，免得我们在上课聊天，或者觉得孤单。"
    scene sweethome_17 with Dissolve(0.3)
    may 3 "啊，就像那些电视剧里同班的双胞胎总是一起惹麻烦一样！" with Dissolve(0.3)
    may 3 "不过你说得对，也没那么糟。毕竟我们还是一起上学！"
    scene sweethome_18 with Dissolve(0.3)
    may 3 '{cps=5}……{/cps}' with Dissolve(0.3)
    scene sweethome_19 with Dissolve(0.3)
    may 3 "对，我刚说到哪了。哦对了，跟你说一声，我要去洗澡。未来半小时都会被占用。" with Dissolve(0.3)
    scene sweethome_20 with Dissolve(0.3)
    gg 3 "好，我不会偷看的。" with Dissolve(0.3)
    scene sweethome_21 with Dissolve(0.3)
    stop music
    play sound oblom volume 0.3
    may 3 "什么？"
    scene sweethome_22 with Dissolve(0.3)
    gg 3 "开玩笑的。" with Dissolve(0.1)
    scene sweethome_23 with Dissolve(0.3)
    may 3 '{cps=5}……{/cps}' with Dissolve(0.3)
    scene sweethome_24 with Dissolve(0.3)
    may 3 "哦……哈哈，说得好像你能似的。" with Dissolve(0.3)
    scene sweethome_25 with Dissolve(0.3)
    pause 1.6
    gg 3 "（天不早了但我并不困……接下来这段晚上该怎么打发？）" with Dissolve(0.3)
    gg 3 "（总是这样……新的环境有那么多可能性，可累了一天之后，脑子里什么都想不出来。）"
    scene sweethome_26 with Dissolve(0.3)
    play music may_shower_afterdoor
    gg 3 "{cps=5}……{/cps}"
    gg 3 "（这里的隔音不太好。她洗澡的声音我听得一清二楚。）"
    menu:
        "[gr]走到浴室门口":
            show sweethome_27 with Dissolve(0.1)
            $ renpy.pause(7,hard=True)
            play music2 may_shower_beforedoor fadein 3
            $ renpy.pause(3,hard=True)
            stop music fadeout 2
            gg 3 "（光是想着门后有个一丝不挂的女孩……）" with Dissolve(0.3)
            gg 3 "（我在想……要不要偷看一眼？）"
            menu:
                "偷看\\n[pink](成人场景)":
                    stop music
                    show sweethome_shower_1 with dissolve
                    $ renpy.pause(4.5, hard=True)
                    show sweethome_shower_2 with dissolve
                    gg 3 "（该死……看到她这副样子，我整个身体都绷紧了。）" with Dissolve(0.3)
                    gg 3 "（水流顺着[may]的身体淌下来，她美得惊人。）"
                    play music may_shower_close
                    scene sweethome_shower_3 with Dissolve(0.5)
                    gg 3 "（她的一切——身段、肌肤、动作——都让我兴奋不已。）" with Dissolve(0.3)
                    scene sweethome_shower_4 with Dissolve(0.5)
                    gg 3 "（我好想从背后抱住她……）" with Dissolve(0.3)
                    scene sweethome_shower_5 with Dissolve(0.5)
                    gg 3 "（……感受她撑着墙、贴在我身上的身体。）" with Dissolve(0.3)
                    scene sweethome_shower_6 with Dissolve(0.5)
                    gg 3 "（也许还可以轻轻抬起她的一条腿……）" with Dissolve(0.3)
                    scene sweethome_shower_7 with Dissolve(0.5)
                    gg 3 "（……在她急促喘息的时候，尽可能贴得更近。）" with Dissolve(0.3)
                    gg 3 "（真是……好一幅景象。我想摸遍她皮肤上的每一滴水珠。）"
                    stop music
                    show sweethome_shower_2 with dissolve
                    gg 3 "（但我还没疯到那个地步——不会做什么蠢事。）" with Dissolve(0.3)
                    gg 3 "（我可不是那种急色的人。我们还是朋友。）"
                    gg 3 "（等时机到了——肯定不只是洗个澡就结束的。）"
                '离开':
                    gg "（该死……我真的昏了头。这样是不对的吧？）" with Dissolve(0.3)
                    gg "（啧……够了。）"
                    gg '{cps=5}……{/cps}'
        '留在这里':
            pause 0.1
    gg 3 "（也许……我该冷静下来，找点事分散注意力？）" with Dissolve(0.3)
    gg 3 "（不过……这里差不多已经是市中心了。也许可以去找个性工作者？顺便还能熟悉一下这片地方。）"
    gg 3 "（不过我骗谁呢。我就是想去找个性工作者而已。）"
    gg 3 "（话说回来，我也可以等[may]洗完，然后冲个冷水澡直接睡下。明天大概会需要体力。）"
    menu:
        "去找个性工作者\\n[pink](奥莉维／由美子 成人场景)":
            pause 0.1
            jump home_go_alexxis
        "自慰\\n[pink](成人场景)":
            $ not_know_alexxis = True
            $ jerkoffer = True
            pause 0.1
            scene black with dissolve
            pause 2.0
            jump sweethome_jo
            
        "等[may]":
            $ not_know_alexxis = True
            gg 3 "（我还是等她吧。今天的刺激已经够多了。）" with Dissolve(0.3)
            pause 0.1
            scene black with dissolve
            pause 2.0
            jump home_gg_shower

#Jerkoffer
label sweethome_jo:
    stop music fadeout 2
    stop music2 fadeout 2
    scene sweethome_jo_1 with dissolve:
        center
        zoom 1.2
        ease 2 zoom 1
    gg 3 "（趁[may]洗澡还有一点时间……最重要的是别被发现。得保持警觉。）" with Dissolve(0.3)
    scene sweethome_jo_2 with dissolve
    gg 3 "（好吧，经典的黑与橙——给我点惊喜。今天有什么新花样？）" with Dissolve(0.3)
    play music3 erotic_by_frank_schroeter volume 0.4
    call screen sweethome_jo
    jump home_gg_shower
    
label sweethome_jo1:
    scene black with Dissolve(1.0)
    show sweethome_jo1_1 with Dissolve(1.0)
    play sound2 "audio/sound/sweethome_jo1_1.ogg" loop
    ''
    show sweethome_jo1_2 with Dissolve(0.3)
    hide sweethome_jo1_1
    stop sound2 fadeout 1
    play sound3 "audio/sound/sweethome_jo1_2.ogg" loop
    ''
    show sweethome_jo1_3 with Dissolve(0.3)
    hide sweethome_jo1_2
    ''
    show sweethome_jo1_4 with Dissolve(0.3)
    hide sweethome_jo1_3
    stop sound3 fadeout 1
    play sound2 "audio/sound/sweethome_jo1_4.ogg" loop
    ''
    show sweethome_jo1_5 with Dissolve(0.3)
    hide sweethome_jo1_4
    ''
    show sweethome_jo1_6 with Dissolve(0.3)
    hide sweethome_jo1_5
    ''
    scene black with Dissolve(0.2)
    show sweethome_jo1_6 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene black with Dissolve(0.3)
    show sweethome_jo1_6 with Dissolve(0.3)
    $ renpy.pause(0.2, hard=True)
    scene black with Dissolve(0.4)
    $ renpy.pause(0.5, hard=True)
    stop sound2 fadeout 1
    show sweethome_jo1_7 with Dissolve(1.5)
    $ renpy.pause(0.5, hard=True)
    
    $ sweethome_jo1_complete = True
    $ persistent.sweethome_jo = True
    $ persistent.sweethome_jo1 = True ## Unlock gallery
    call screen sweethome_jo

label sweethome_jo2:
    scene black with Dissolve(1.0)
    show sweethome_jo2_1 with Dissolve(1.0)
    play sound2 "audio/sound/pussy_1.ogg" loop
    ''
    show sweethome_jo2_2 with Dissolve(0.3)
    hide sweethome_jo2_1
    ''
    show sweethome_jo2_3 with Dissolve(0.3)
    hide sweethome_jo2_2
    ''
    show sweethome_jo2_4 with Dissolve(0.3)
    hide sweethome_jo2_3
    ''
    show sweethome_jo2_5 with Dissolve(0.3)
    hide sweethome_jo2_4
    ''
    show sweethome_jo2_6 with Dissolve(0.3)
    hide sweethome_jo2_5
    stop sound2 fadeout 1
    play sound3 "audio/sound/pussy_2.ogg" loop
    ''
    show sweethome_jo2_7 with Dissolve(0.3)
    hide sweethome_jo2_6
    ''
    stop sound3 fadeout 1
    scene black with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    
    show sweethome_jo2_8 with Dissolve(1.5)
    $ renpy.pause(0.5, hard=True)
    
    $ sweethome_jo2_complete = True
    $ persistent.sweethome_jo = True
    $ persistent.sweethome_jo2 = True ## Unlock gallery
    call screen sweethome_jo

label sweethome_jo3:

    scene black with Dissolve(1.0)
    play music2 japan_streets_1 volume 0.4
    play sound3 "audio/sound/pussy_1.ogg" loop
    show sweethome_jo3_1 with Dissolve(1.0)
    ''
    show sweethome_jo3_2 with Dissolve(0.3)
    hide sweethome_jo3_1
    ''
    show sweethome_jo3_3 with Dissolve(0.3)
    hide sweethome_jo3_2
    ''
    show sweethome_jo3_4 with Dissolve(0.3)
    hide sweethome_jo3_3
    stop sound2 fadeout 1
    play sound3 "audio/sound/pussy_2.ogg" loop
    ''
    show sweethome_jo3_5 with Dissolve(0.1)
    hide sweethome_jo3_4
    $ renpy.pause(5.0, hard=True)
    scene black with Dissolve(0.2)
    stop sound3 fadeout 1
    $ renpy.pause(1.0, hard=True)
    show sweethome_jo3_6 with Dissolve(1.5)
    $ renpy.pause(0.5, hard=True)

    $ sweethome_jo3_complete = True
    $ persistent.sweethome_jo = True
    $ persistent.sweethome_jo3 = True ## Unlock gallery
    stop music2 fadeout 5
    call screen sweethome_jo

label sweethome_jo4:
    play music2 japan_streets_1 volume 0.4
    scene black with Dissolve(1.0)
    play sound2 sweethome_jo4 loop
    show sweethome_jo4_1 with Dissolve(1.0)
    ''
    show sweethome_jo4_2 with Dissolve(0.3)
    hide sweethome_jo4_1
    ''
    show sweethome_jo4_3 with Dissolve(0.3)
    hide sweethome_jo4_2
    ''
    show sweethome_jo4_4 with Dissolve(0.3)
    hide sweethome_jo4_3
    ''
    scene black with Dissolve(0.5)
    stop sound2 fadeout 1
    $ renpy.pause(1.0, hard=True)
    show sweethome_jo4_5 with Dissolve(1.5)
    $ renpy.pause(0.5, hard=True)

    $ sweethome_jo4_complete = True
    $ persistent.sweethome_jo = True
    $ persistent.sweethome_jo4 = True ## Unlock gallery
    stop music2 fadeout 5
    call screen sweethome_jo
    
#GoToAlexxis
label home_go_alexxis:
    gg 3 "（现在就走的话——也许能在她发现之前赶回来。）" with Dissolve(0.3)
    gg 3 "（就说自己一直在房间里睡觉……应该能糊弄过去。）"
    gg 3 "（好，就这么办。是时候满足一下我最原始的冲动了。）"
    stop music fadeout 4
    stop music2 fadeout 4
    scene black with dissolve
    pause 2.0
    play music japan_streets_1 volume 3.0 fadein 3
    pause 1.0
   
    scene home_go_alexxis_1 with dissolve
    gg 4 "（这座城市哪里能找到性工作者或者夜店？）" with Dissolve(0.3)
    gg 4 "（我完全不了解这附近有什么。）"
    scene home_go_alexxis_2 with dissolve
    gg 4 "（可以四处逛逛找找粉色霓虹灯，但不想把整晚都耗在这上面。）" with Dissolve(0.3)
    gg 4 "（我得找个能帮忙的人。）"
    play sound car_signal_1
    scene home_go_alexxis_3 with hpunch
    taxidriver 1 "要打车吗？"
    gg 4 "要！" with vpunch
    scene home_go_alexxis_4 with dissolve
    gg 4 "这附近有能让男人在辛苦一天后放松一下的地方吗？" with Dissolve(0.3)
    scene home_go_alexxis_5 with dissolve
    taxidriver 1 "嗯……我倒是知道一两个地方。" with Dissolve(0.3)
    taxidriver 1 "市中心有家现场演出的酒廊，可以喝酒放松，价格也不贵。"
    taxidriver 1 "要是想找点更刺激的，城那头有家夜店——我可以送你去。"
    scene home_go_alexxis_4 with dissolve
    gg 4 "这些听起来都不错，但我想找的是有女人的地方。" with Dissolve(0.3)
    scene home_go_alexxis_6 with vpunch
    taxidriver 1 "听着，如果你就只有这些问题，别浪费我时间！"
    scene home_go_alexxis_4 with dissolve
    gg 4 "大叔，我真的需要个女人！随便报个地方带我去，钱我付。" with Dissolve(0.3)
    scene home_go_alexxis_7 with dissolve
    taxidriver 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene home_go_alexxis_8 with dissolve
    taxidriver 1 "有一家店，叫「Alexxis」。" with Dissolve(0.3)
    scene home_go_alexxis_9 with dissolve
    taxidriver 1 "你在那里能找到你想要的一切。" with Dissolve(0.3)
    scene home_go_alexxis_4 with dissolve
    gg 4 "太好了，走吧。" with Dissolve(0.3)
    scene home_go_alexxis_6 with vpunch
    taxidriver 1 "不，我可不送你去那儿！"
    play sound cardoor_closed
    scene home_go_alexxis_10 with hpunch
    play sound car_taxi_starter
    pause 1.0
    scene home_go_alexxis_11 with dissolve
    pause 1.0
    scene home_go_alexxis_12 with dissolve
    pause 1.0
    scene home_go_alexxis_13 with dissolve
    gg 4 "（什么意思？……）" with Dissolve(0.3)
    scene home_go_alexxis_14 with dissolve
    gg 4 "（这老头脑子有毛病。）" with Dissolve(0.3)
    scene home_go_alexxis_15 with dissolve
    play sound2 camaro_1969 volume 0.2
    pause 1.0
    scene home_go_alexxis_16 with dissolve
    stop sound
    play sound2 camaro_1969 volume 0.4
    pause 1.0
    play sound3 car_signal_2
    scene home_go_alexxis_17 with vpunch
    pause 2.0
    scene home_go_alexxis_18
    play music2 camaro_1969
    pause 1.0
    scene home_go_alexxis_19 with dissolve
    pause 1.3
    scene home_go_alexxis_20 with Dissolve(0.3)
    pause 0.3
    scene home_go_alexxis_21 with Dissolve(0.3)
    pause 0.2
    scene home_go_alexxis_22 with Dissolve(0.3)
    pause 0.3
    scene home_go_alexxis_21 with Dissolve(0.3)
    pause 0.2
    scene home_go_alexxis_22 with Dissolve(0.3)
    pause 1.3
    stop music
    show home_go_alexxis_23 with Dissolve(0.1)
    $ renpy.pause(10,hard=True)
    play music2 camaro_1969
    ja0 1 '{cps=5}……{/cps}' with Dissolve(0.3)
    scene home_go_alexxis_23_1
    gg 4 "你知道「Alexxis」在哪儿吗？" with Dissolve(0.3)
    ja0 1 '{cps=5}……{/cps}' with Dissolve(0.3)
    gg "我想去那儿。能指个路吗？" with Dissolve(0.3)
    scene home_go_alexxis_24 with dissolve
    ja0 1 "上车吧。" with Dissolve(0.3)
    stop music2 fadeout 3.2
    play sound car_sit
    scene black with dissolve
    pause 1.6
    play music camaro_1969 volume 0.5
    scene home_go_alexxis_25 with dissolve
    pause 2.0
    scene home_go_alexxis_26 with dissolve
    ja0 1 "所以说，兄弟，你想要个女人？" with Dissolve(0.3)
    scene home_go_alexxis_27 with dissolve
    ja0 1 "「Alexxis」离这儿就几个街区。" with Dissolve(0.3)
    scene home_go_alexxis_28 with dissolve
    ja0 1 "那是富二代们常去的地方——服务和女人都是一流。你是他们中的一个？" with Dissolve(0.3)
    
    scene home_go_alexxis_26 with dissolve
    gg 4 "如果你是问这个，我不是富二代。" with Dissolve(0.3)
    ja0 1 "好好好，兄弟，你说什么都对。" with Dissolve(0.3)
    scene home_go_alexxis_29 with dissolve
    pause 1.0
    scene home_go_alexxis_30 with dissolve
    pause 1.0
    scene home_go_alexxis_31 with dissolve
    ja0 1 "我叫[ja]。" with Dissolve(0.3)
    menu:
        '[gr]握手':
            $ salam_jarabja = True
            scene home_go_alexxis_32 with dissolve
            gg 4 "[gg]。"
            scene home_go_alexxis_33 with dissolve
            pause 0.3
            play sound demon_moment
            scene home_go_alexxis_34_1 with Dissolve(0.2)
            pause 0.2
            scene home_go_alexxis_34_2 with Dissolve(0.1)
            pause 0.03
            scene home_go_alexxis_34 with Dissolve(0.1)
            pause 0.1
            stop sound fadeout 6
            scene home_go_alexxis_33 with dissolve
            pause 0.3
            scene home_go_alexxis_35 with Dissolve(0.2)
            pause 1.0
            gg 4 "（这到底是什么情况？）" with Dissolve(0.1)
            play sound heart_bass
            scene home_go_alexxis_36 with dissolve
            ja 1 "很高兴认识你，兄弟。" with Dissolve(0.3)
            scene home_go_alexxis_37 with dissolve
            gg 4 "（他刚才眼睛是不是……还是我看错了？）" with Dissolve(0.3)
            stop sound fadeout 6
            gg "嗯，嗯。你能送我去吗？" with Dissolve(0.3)
        '什么都不做':
            gg 4 '[gg]。'
            scene home_go_alexxis_38 with dissolve
            ja 1 '{cps=5}……{/cps}' with Dissolve(0.3)
            gg 4 "你能送我去吗？" with Dissolve(0.3)
    scene home_go_alexxis_39 with dissolve
    gg 4 "我时间不多。" with Dissolve(0.3)
    scene home_go_alexxis_40 with dissolve
    ja 1 '没问题！' with Dissolve(0.3)
    scene home_go_alexxis_41 with dissolve
    ja 1 "从这儿开过去也就几分钟。" with Dissolve(0.3)
    stop music fadeout 5
    scene black with dissolve
    pause 2.6
    
    # Inside Alexxis
    play music camaro_1969
    scene alexxis_1 with dissolve
    pause 1.0
    gg 4 "那我该付你多少钱？" with Dissolve(0.3)
    ja 1 "不用。" with Dissolve(0.3)
    gg "免费？" with Dissolve(0.3)
    ja "你又不是什么「富二代」。好人之间就该互相帮忙。" with Dissolve(0.3)
    gg "……懂了，谢谢。祝你生意兴隆！" with Dissolve(0.3)
    stop music fadeout 5
    play sound car_sit
    scene black with dissolve
    pause 5.0
    play music cocktails_and_lobsters_by_alexander_nakarada
    scene alexxis_2 with dissolve
    pause 1.0
    gg 4 "（这地方确实不一般。）" with dissolve
    gg 4 "（我敢肯定这里只接待有钱客人。）"
    show alexxis_3 with Dissolve(0.1)
    $ renpy.pause(8,hard=True)
    scene alexxis_4 with dissolve
    gg 4 "（不知道她们的价位是多少？）" with dissolve
    gg "（大概超出我的预算了。）" with dissolve
    gg "（不过要是真能带来非同一般的体验，也许值得一试。）" with dissolve
    show alexxis_5 with Dissolve(0.1)
    $ renpy.pause(1,hard=True)
    scene alexxis_7 with Dissolve(0.6)
    so 1 "欢迎光临，我是[so]。" with dissolve
    scene alexxis_8 with dissolve
    so 1 "欢迎来到「Alexxis」。希望您在这里度过愉快的时间。" with dissolve
    show alexxis_9 with Dissolve(0.3)
    gg 4 "谢谢你，[so]。" with dissolve
    gg 4 "不得不说，这里的气氛真是太棒了。感觉像是走进了另一个世界。"
    scene alexxis_10 with dissolve
    so 1 "您能这么说我很高兴。我们的装潢，以及为客人提供一切他们所渴望之事的本事，都是我们的骄傲。" with dissolve
    scene alexxis_11 with dissolve
    so 1 "不过，有一点我得先说清楚。" with dissolve
    scene alexxis_12 with dissolve
    so 1 "「Alexxis」不提供任何色情服务——我们可是正经店家。" with dissolve
    gg 4 "（那我跑来这里干什么？）" with dissolve
    gg "（这国家大概不允许卖淫吧。）"
    gg "（这该不会是她提前准备好的说辞，用来应付警察或有关部门吧？）"
    scene alexxis_13 with dissolve
    so 1 "顶多只是手动服务……" with dissolve
    scene alexxis_14 with dissolve
    pause 0.6
    scene alexxis_14_1 with Dissolve(0.3)
    so 1 "你懂的。" with dissolve
    show alexxis_9 with dissolve
    gg 4 "当然我懂。" with dissolve
    gg 4 "还能指望什么。反正你我都知道我来这儿是干什么的。" with dissolve
    scene alexxis_15 with dissolve
    so 1 "您能理解就太好了。" with dissolve
    scene alexxis_16 with dissolve
    so 1 "客人尊重我们的规定和底线，对我们来说很重要。" with dissolve
    scene alexxis_10 with dissolve
    so 1 "不过还请您不要因此放不开，好好享受在这里的时光。" with dissolve
    scene alexxis_17 with dissolve
    so 1 "请稍等。我去叫姑娘们。" with dissolve
    $ sophia_unlock = True
    scene black with dissolve
    pause 1.0
    so 1 "姑娘们，有客人来了！" with dissolve
    scene alexxis_18 with dissolve
    show alexxis_19 with Dissolve(0.1)
    $ renpy.pause(8,hard=True)
    scene alexxis_20 with dissolve
    scene alexxis_20 with dissolve
    so 1 '这位是[olivia]。' with dissolve
    scene alexxis_21 with dissolve
    so 1 '这位是[yumiko]。' with dissolve
    scene alexxis_22 with dissolve
    so 1 "两位都是这方面的行家。" with dissolve
    $ persistent.gallery_alexxis = True ## Opening Alexxis in the gallery
    scene alexxis_23
    so 1 "所以只是看个人喜好而已。" with dissolve
    scene alexxis_24
    olivia 1 "我们两人都经验丰富，也接受过各种手法的训练。" with dissolve
    scene alexxis_25 with dissolve
    olivia 1 "如果您有特别的偏好，或者身体哪里有不适，我们可以按您的需求来调整。" with dissolve
    scene alexxis_26 with dissolve
    olivia 1 "我擅长深层按摩。" with dissolve
    scene alexxis_27 with dissolve
    olivia 1 "我最喜欢针对让人不适的部位重点处理。" with dissolve
    scene alexxis_24 with dissolve
    olivia 1 "您若有兴趣，我很乐意陪您。" with dissolve
    $ olivia_unlock = True
    scene alexxis_28 with dissolve
    yumiko 1 "我们两人的风格很不一样，所以要看您想要什么样的体验。" with dissolve
    scene alexxis_29 with dissolve
    olivia 1 "[yumiko]的手法非常轻柔。" with dissolve
    scene alexxis_30 with dissolve
    olivia 1 "而我则负责让客人一滴不剩地释放。" with dissolve
    scene alexxis_31 with dissolve
    yumiko 1 "我更注重整体的放松与平衡。" with dissolve
    scene alexxis_32 with dissolve
    yumiko 1 "但这不代表我不能强硬一点。" with dissolve
    scene alexxis_33 with dissolve
    yumiko 1 "我的意思是……我想说的是……" with dissolve
    scene alexxis_34 with dissolve
    olivia 1 "她的意思是，不管我们的专长是什么，她都会满足客人的任何要求。" with dissolve
    scene alexxis_35 with dissolve
    yumiko 1 "对，我就是这个意思。抱歉。" with dissolve
    $ yumiko_unlock = True
    gg 4 "（真是个艰难的选择……）" with dissolve
    call screen olivia_or_yumiko with dissolve

label alexxis_olivia:

    scene alexxis_o_1
    gg 4 '[olivia]，我选你。' with dissolve
    scene alexxis_o_2 with dissolve
    gg 4 '我腹股沟这块有些疼痛和不适，我觉得深层按摩应该能帮上忙。' with dissolve
    scene alexxis_o_3 with dissolve
    olivia 1 '好眼光，帅哥。' with dissolve
    scene alexxis_o_4 with dissolve
    olivia 1 '我一定会重点照顾您疼痛的部位，以及身上其他僵硬的地方。' with dissolve
    scene alexxis_o_5
    so 1 '选[olivia]非常合适。' with dissolve
    scene alexxis_o_6 with dissolve
    so 1 '她经验非常丰富，一定能让您感觉好上不少。' with dissolve
    scene alexxis_o_7
    olivia 1 '跟我来。' with dissolve
    stop music fadeout 3
    scene black with dissolve
    pause 3.3
    jump alexxis_olivia_1

label alexxis_olivia_1:

    scene alexxis_o_8 with dissolve
    play music erotic_by_frank_schroeter volume 0.5
    olivia 1 "请进。" with dissolve
    scene alexxis_o_9 with dissolve
    olivia 1 "坐吧。第一次来这种地方？" with dissolve
    play sound divan_sit
    scene alexxis_o_10 with dissolve
    gg 4 "嗯，从没来过这种地方。" with dissolve
    scene alexxis_o_11 with dissolve
    olivia 1 '你多大了？' with dissolve
    scene alexxis_o_12 with dissolve
    gg 4 '十八。' with dissolve
    scene alexxis_o_13 with dissolve
    olivia 1 "哦，那你比我还小啊。" with dissolve
    scene alexxis_o_14 with dissolve
    olivia 1 "但你看起来二十五岁。" with dissolve
    scene alexxis_o_12 with dissolve
    gg 4 "这话我就当夸奖收下了。" with dissolve
    scene alexxis_o_15 with dissolve
    olivia 1 "既然是第一次来……我一定会让你一次又一次地想再回来找我。" with dissolve
    scene alexxis_o_16 with dissolve
    gg 4 "您不用太卖力——不管怎样我都喜欢。" with dissolve
    scene alexxis_o_17 with dissolve
    olivia 1 '不。' with dissolve
    scene alexxis_o_18 with dissolve
    olivia 1 "能成为您在Alexxis的第一位客人，是我的荣幸。" with dissolve
    scene alexxis_o_19 with dissolve
    olivia 1 "放心交给我吧，帅哥。" with dissolve
    scene alexxis_o_20 with dissolve
    pause 1.0
    gg 4 "靠……好大！" with dissolve
    scene alexxis_o_21 with dissolve
    gg 4 "这话你大概听腻了，但你的身材真的很好。" with dissolve
    show alexxis_o_22 with Dissolve(0.1)
    ''
    scene alexxis_o_23 with Dissolve(0.1)
    olivia 1 "打算就这么看着？" with dissolve
    scene alexxis_o_24 with dissolve
    olivia 1 "来啊，摸摸看。" with dissolve
    scene alexxis_o_25 with dissolve
    pause 1.0
    gg 4 "我一点都不会让你等——我乐意之至。" with dissolve
    scene alexxis_o_26 with dissolve
    pause 1.0
    scene alexxis_o_27 with dissolve
    pause 1.0
    gg 4 "好软……" with dissolve
    show alexxis_o_28 with Dissolve(0.3)
    pause 1.0
    gg 4 "哦，该死……" with dissolve
    scene alexxis_o_27 with dissolve
    pause 1.0
    gg 4 "会上瘾的。" with dissolve
    show alexxis_o_28 with Dissolve(0.3)
    pause 0.6
    gg 4 "我喜欢这样。"  with dissolve
    scene alexxis_o_29 with dissolve
    pause 0.6
    gg 4 "忘不了那对奶头。" with dissolve
    show alexxis_o_30 with Dissolve(0.3)
    pause 0.6
    olivia 1 '啊！' with dissolve
    scene alexxis_o_24 with dissolve
    olivia 1 '喂，轻点。' with dissolve
    scene alexxis_o_31 with dissolve
    olivia 1 '放松，我们有的是时间。' with dissolve
    scene alexxis_o_32 with dissolve
    olivia 1 "你已经让我硬起来了。" with dissolve
    scene alexxis_o_33 with dissolve
    pause 1.0
    gg 4 "（哇，这是什么内裤——开裆款？）" with dissolve
    scene alexxis_o_34 with dissolve
    olivia 1 "把衣服脱了，让你那位朋友出来透透气。" with dissolve
    play sound clothes_1
    scene black with dissolve
    pause 2.0
    play sound clothes_2
    show alexxis_o_35 with dissolve
    olivia 0 "哇……" with dissolve
    show alexxis_o_36 with Dissolve(0.1)
    $ renpy.pause(2.9,hard=True)
    scene alexxis_o_37 with Dissolve(0.6)
    olivia 0 "这……好大。"
    scene alexxis_o_38 with dissolve
    gg 0 "对你来说都算大？" with dissolve
    scene alexxis_o_39 with dissolve
    olivia 0 "等你见过平时来这里的那些家伙，你就不会这么问了。你有在健身吗？" with dissolve
    scene alexxis_o_40 with dissolve
    gg 0 "类固醇打太多了。" with dissolve
    scene alexxis_o_41 with dissolve
    olivia 0 "看那玩意儿，我一秒都不信。" with dissolve
    scene alexxis_o_42 with dissolve
    olivia 0 "是时候让你舒服一下了……" with dissolve
    scene alexxis_o_43 with dissolve
    gg 0 "嗯唔！" with dissolve
    scene alexxis_o_44 with dissolve
    olivia 0 "真不敢相信看起来这么好看。" with dissolve
    scene alexxis_o_45 with dissolve
    olivia 0 "握在手里手感真好……" with dissolve
    scene alexxis_o_46 with dissolve
    olivia 0 "我自己也很享受！" with dissolve
    scene alexxis_o_47 with dissolve
    olivia 0 "好了，开始让你好好爽一把……" with dissolve
    show alexxis_o_48 with Dissolve(0.1)
    ''
    show alexxis_o_48_1 with Dissolve(0.1)
    hide alexxis_o_48
    ''
    show alexxis_o_48_2 with Dissolve(0.1)
    hide alexxis_o_48_1
    ''
    show alexxis_o_49 with Dissolve(0.1)
    hide alexxis_o_48_2
    ''
    gg 0 "（天啊，太爽了。）" with dissolve
    ''
    gg 0 "快一点。" with dissolve
    pause 1.0
    scene black with dissolve
    pause 0.3
    show alexxis_o_50 with dissolve
    ''
    gg 0 "靠，我要射了……" with dissolve
    ''
    gg 0 "要来了！" with dissolve
    scene black with dissolve
    pause 0.3
    show alexxis_o_50 with dissolve
    pause 0.3
    scene black with dissolve
    pause 0.6
    play sound cumming
    scene alexxis_o_51 with dissolve
    olivia 0 "啊！" with dissolve
    scene alexxis_o_52 with dissolve
    olivia 0 "好烫……" with dissolve
    scene alexxis_o_53 with dissolve
    pause 1.6
    scene alexxis_o_54 with dissolve
    olivia 0 "按规矩是不行的，不过只要你别告诉别人……" with dissolve
    scene alexxis_o_55 with dissolve
    olivia 0 "我可以为你做点更棒的事。" with dissolve
    scene alexxis_o_56 with dissolve
    pause 1.0
    gg 0 "别停。" with dissolve
    scene alexxis_o_52 with dissolve
    olivia 0 "完美……" with dissolve
    scene alexxis_o_57 with dissolve
    olivia 0 "我想尝尝你的味道……" with dissolve
    scene alexxis_o_58 with dissolve
    olivia 0 '啊……' with dissolve
    scene alexxis_o_59 with dissolve
    pause 1.0
    scene alexxis_o_60 with dissolve
    gg 0 "哦哦！" with dissolve
    scene alexxis_o_61 with dissolve
    pause 1.0
    scene alexxis_o_62 with dissolve
    gg 0 "太爽了。"
    scene alexxis_o_63 with dissolve
    pause 1.0
    scene alexxis_o_64 with dissolve
    olivia 0 '唔……' with dissolve
    scene alexxis_o_65 with dissolve
    gg 0 '哈！' with dissolve
    scene alexxis_o_66 with dissolve
    pause 2.0
    scene alexxis_o_67 with dissolve
    pause 1.0
    scene alexxis_o_68 with dissolve
    pause 1.0
    olivia 0 "我开始了。" with dissolve
    scene alexxis_o_69 with dissolve
    gg 0 "来吧。" with dissolve
    scene alexxis_o_70 with dissolve
    pause 1.0
    scene alexxis_o_71 with dissolve
    pause 1.6
    scene alexxis_o_72 with dissolve
    pause 1.0
    show alexxis_o_73 with Dissolve(0.1)
    ''
    gg 0 "（这比打手枪爽多了。）" with dissolve
    ''
    show alexxis_o_74 with Dissolve(0.1)
    hide alexxis_o_73
    gg 0 "啊，靠，太爽了！" with dissolve
    pause 1.0
    olivia 0 '嗯……' with dissolve
    pause 1.0
    show alexxis_o_75 with Dissolve(0.1)
    hide alexxis_o_74
    ''
    gg 0 "拜托，别停！" with dissolve
    ''
    gg 0 "（她要是再这么吸下去，我肯定撑不住！）" with dissolve
    ''
    scene black with dissolve
    pause 0.6
    play sound divan_vstal volume 0.7
    pause 1.6
    
    scene alexxis_o_76 with Dissolve(0.1)
    gg 0 "再深一点！" with Dissolve(0.1)
    olivia 0 '{cps=5}……{/cps}' with dissolve
    scene alexxis_o_77 with dissolve
    olivia 0 "怎么突然这么粗暴？" with dissolve
    scene alexxis_o_78 with dissolve
    gg 0 "继续，[olivia]。" with dissolve
    pause 1.0
    olivia 0 '{cps=5}……{/cps}' with dissolve
    scene alexxis_o_79 with dissolve
    pause 1.6
    scene alexxis_o_80 with dissolve
    pause 0.6
    show alexxis_o_81 with Dissolve(0.1)
    ''
    olivia 0 '唔嗯……'
    ''
    show alexxis_o_82 with Dissolve(0.1)
    hide alexxis_o_81
    pause 1.0
    gg 0 "爽死了，[olivia]。" with dissolve
    ''
    gg 0 '快点！' with dissolve
    pause 0.6
    show alexxis_o_83 with Dissolve(0.1)
    hide alexxis_o_82
    ''
    show alexxis_o_84 with Dissolve(0.1)
    hide alexxis_o_83
    ''
    gg 0 "我快忍不住了！" with dissolve
    ''
    show alexxis_o_83 with Dissolve(0.1)
    hide alexxis_o_84
    pause 2.0
    gg 0 "现在！" with dissolve
    scene black with dissolve
    pause 0.3
    show alexxis_o_83 with dissolve
    pause 0.6
    scene black with dissolve
    pause 1.0
    show alexxis_o_85 with Dissolve(0.1)
    play sound cumming
    pause 5.0
    show alexxis_o_86 with Dissolve(0.1)
    play sound cumming
    pause 5.0
    scene black with dissolve
    pause 0.3
    scene alexxis_o_87 with dissolve
    olivia 0 "啊……" with dissolve
    pause 1.0
    scene alexxis_o_88 with dissolve
    olivia 0 "好多……" with dissolve
    pause 1.0
    scene alexxis_o_89 with dissolve
    olivia 0 '{cps=5}……{/cps}' with dissolve
    gg 0 "（她这是怎么了？）" with dissolve
    scene alexxis_o_90 with dissolve
    olivia 0 "还硬着呢？" with dissolve
    scene alexxis_o_91 with dissolve
    olivia 0 "不能就这样结束——你得进来！" with dissolve
    scene alexxis_o_92 with dissolve
    olivia 0 "还是说，你不想吃主菜？" with dissolve
    scene black with dissolve
    play sound divan_sit
    pause 1.0
    scene alexxis_o_93 with dissolve
    gg 0 "那不是违规吗？" with dissolve
    scene alexxis_o_94 with dissolve
    olivia 0 "本来我打算就到此为止的……" with dissolve
    scene alexxis_o_95 with dissolve
    olivia 0 "但现在……我想要更多。" with dissolve
    $ persistent.gallery_olivia_unlock_1 = True ## Gallery with Olivia 1 - open
    show alexxis_o_93
    call screen olivia_sex_choice
    
label alexxis_olivia_sex_1:

    $ alexxis_olivia_choice_sex_1 += 1

    if alexxis_olivia_choice_sex_2 == 0: 
        gg 0 "好吧" with dissolve
        scene black with dissolve
        pause 2.0
        show alexxis_o_sex1_1 with Dissolve(0.1)
        olivia 0 '哈啊！' with dissolve
        show alexxis_o_sex1_2 with Dissolve(0.1)
        hide alexxis_o_sex1_1
        gg 0 "（来了！我进去了！）" with dissolve
        olivia '呵……' with dissolve
        show alexxis_o_sex1_3 with Dissolve(0.1)
        hide alexxis_o_sex1_2
        gg 0 "（该死，她里面在把我吞进去。）" with dissolve
        show alexxis_o_sex1_4 with Dissolve(0.1)
        hide alexxis_o_sex1_3
        olivia 0 "好胀！" with dissolve
        gg 0 "（又暖又软。）" with dissolve
        gg 0 "（她里面在夹我。）" with dissolve
        show alexxis_o_sex1_5 with Dissolve(0.1)
        hide alexxis_o_sex1_4
        ''
        show alexxis_o_sex1_1 with Dissolve(0.1)
        hide alexxis_o_sex1_5
        ''
        gg 0 "（再深一点！）" with dissolve
        show alexxis_o_sex1_6 with Dissolve(0.1)
        hide alexxis_o_sex1_1
        olivia 0 '哈啊！' with dissolve
        ''
        olivia 0 '啊……' with dissolve
        gg 0 "我快忍不住了！" with dissolve
        show alexxis_o_sex1_7 with Dissolve(0.1)
        hide alexxis_o_sex1_6
        pause 0.4
        play sound cumming
        scene black with Dissolve(0.1)
        pause 0.6
        show alexxis_o_sex1_8 with Dissolve(0.3)
        ''
        $ persistent.gallery_olivia_unlock_2 = True ## Gallery with Olivia 2 - open
        call screen olivia_sex_choice
    
    if alexxis_olivia_choice_sex_2 == 1:

        scene black with dissolve
        pause 2.0
        
        show alexxis_o_sex1_1
        olivia 0 "对！" with dissolve
        show alexxis_o_sex1_2 with Dissolve(0.1)
        hide alexxis_o_sex1_1
        gg 0 "这个姿势又让我硬起来了！" with dissolve
        olivia 0 "拜托，别停！" with dissolve
        show alexxis_o_sex1_3 with Dissolve(0.1)
        hide alexxis_o_sex1_2
        ''
        show alexxis_o_sex1_4 with Dissolve(0.1)
        hide alexxis_o_sex1_3
        olivia 0 '你怎么都不会累……' with dissolve
        gg 0 '闭嘴。最后一次了！' with dissolve
        ''
        show alexxis_o_sex1_5 with Dissolve(0.1)
        hide alexxis_o_sex1_4
        ''
        show alexxis_o_sex1_1 with Dissolve(0.1)
        hide alexxis_o_sex1_5
        ''
        gg 0 "（要来了……）" with dissolve
        show alexxis_o_sex1_6 with Dissolve(0.1)
        hide alexxis_o_sex1_1
        olivia 0 "我受不了了！" with dissolve
        ''
        olivia 0 "天啊……" with dissolve
        gg 0 '要来了！' with dissolve
        show alexxis_o_sex1_7 with Dissolve(0.1)
        hide alexxis_o_sex1_6
        pause 0.5
        play sound cumming
        scene black with Dissolve(0.1)
        pause 0.6
        show alexxis_o_sex1_8 with Dissolve(0.3)
        ''
        $ persistent.gallery_olivia_unlock_2 = True ## Gallery with Olivia 2 - open
        jump alexxis_olivia_exit
        
    
label alexxis_olivia_sex_2:

    $ alexxis_olivia_choice_sex_2 += 1
    
    if alexxis_olivia_choice_sex_1 == 0:
        gg 0 '好吧。' with dissolve
        scene black with dissolve
        pause 2.0
        show alexxis_o_sex2_1 with Dissolve(0.1)
        olivia 0 "啊啊……好！" with dissolve
        ''
        show alexxis_o_sex2_2 with Dissolve(0.1)
        hide alexxis_o_sex2_1
        gg 0 "哦，靠！" with dissolve
        ''
        show alexxis_o_sex2_3 with Dissolve(0.1)
        hide alexxis_o_sex2_2
        gg 0 "（来了！我进去了！）" with dissolve
        ''
        olivia 0 "哈啊……" with dissolve
        show alexxis_o_sex2_4 with Dissolve(0.1)
        hide alexxis_o_sex2_3
        gg 0 "（她刚刚把我整个吞进体内了。）" with dissolve
        ''
        show alexxis_o_sex2_5 with Dissolve(0.1)
        hide alexxis_o_sex2_4
        olivia 0 '好胀！' with dissolve
        ''
        show alexxis_o_sex2_1 with Dissolve(0.1)
        hide alexxis_o_sex2_5
        gg 0 "（里面又暖又软。）" with dissolve
        ''
        show alexxis_o_sex2_6 with Dissolve(0.1)
        hide alexxis_o_sex2_1
        pause 2.0
        gg 0 "（她动起来把我顶得更深了。）" with dissolve
        ''
        show alexxis_o_sex2_7 with Dissolve(0.1)
        hide alexxis_o_sex2_6
        gg 0 "（她从里面夹紧我。）" with dissolve
        ''
        show alexxis_o_sex2_8 with Dissolve(0.1)
        hide alexxis_o_sex2_7
        olivia 0 "哈啊啊" with dissolve
        ''
        show alexxis_o_sex2_9 with Dissolve(0.1)
        hide alexxis_o_sex2_8
        ''
        show alexxis_o_sex2_10 with Dissolve(0.1)
        hide alexxis_o_sex2_9
        ''
        show alexxis_o_sex2_6 with Dissolve(0.1)
        hide alexxis_o_sex2_10
        pause 2.0
        olivia 0 "帅哥……喜欢我体内的感觉吗？" with dissolve
        gg 0 "我要射了。" with dissolve
        ''
        olivia 0 "射进来。"
        gg 0 "你确定？"
        olivia 0 "哦……好……"
        ''
        gg 0 "我快忍不住了！" with dissolve
        show alexxis_o_sex2_11 with Dissolve(0.1)
        hide alexxis_o_sex2_6
        pause 3.0
        show alexxis_o_sex2_12 with Dissolve(0.1)
        hide alexxis_o_sex2_11
        ''
        $ persistent.gallery_olivia_unlock_3 = True ## Gallery with Olivia 2 - open
        call screen olivia_sex_choice
        
    if alexxis_olivia_choice_sex_1 == 1:
        scene black with dissolve
        pause 2.0
        show alexxis_o_sex2_1_1 with Dissolve(0.1)
        olivia 0 "你好有力……" with dissolve
        ''
        show alexxis_o_sex2_2 with Dissolve(0.1)
        hide alexxis_o_sex2_1_1
        gg 0 "天啊，太舒服了……" with dissolve
        ''
        show alexxis_o_sex2_3 with Dissolve(0.1)
        hide alexxis_o_sex2_2
        gg 0 "靠……爽死了！" with dissolve
        ''
        olivia 0 '好的……' with dissolve
        show alexxis_o_sex2_4 with Dissolve(0.1)
        hide alexxis_o_sex2_3
        ''
        show alexxis_o_sex2_5 with Dissolve(0.1)
        hide alexxis_o_sex2_4
        olivia 0 "天啊，我头都快转起来了。" with dissolve
        ''
        show alexxis_o_sex2_1_1 with Dissolve(0.1)
        hide alexxis_o_sex2_5
        ''
        gg 0 '快点！' with dissolve
        show alexxis_o_sex2_6_1 with Dissolve(0.1)
        hide alexxis_o_sex2_1_1
        pause 2.0
        gg 0 "这样才对。" with dissolve
        ''
        show alexxis_o_sex2_7 with Dissolve(0.1)
        hide alexxis_o_sex2_6_1
        ''
        show alexxis_o_sex2_8 with Dissolve(0.1)
        hide alexxis_o_sex2_7
        olivia 0 "快射吧……" with dissolve
        pause 1.0
        olivia 0 "我快受不了了！" with dissolve
        ''
        show alexxis_o_sex2_9_1 with Dissolve(0.1)
        hide alexxis_o_sex2_8
        ''
        show alexxis_o_sex2_10 with Dissolve(0.1)
        hide alexxis_o_sex2_9_1
        ''
        show alexxis_o_sex2_6_1 with Dissolve(0.1)
        hide alexxis_o_sex2_10
        pause 2.0
        ''
        gg 0 "要来了！"
        show alexxis_o_sex2_11_1 with Dissolve(0.1)
        hide alexxis_o_sex2_6_1
        pause 3.0
        show alexxis_o_sex2_12_1 with Dissolve(0.1)
        hide alexxis_o_sex2_11_1
        ''
        $ persistent.gallery_olivia_unlock_3 = True ## Gallery with Olivia 2 - open
        jump alexxis_olivia_exit
    
label alexxis_olivia_exit:

    scene black with dissolve
    stop music fadeout 6.0
    pause 3.6
    scene alexxis_olivia_exit_1 with dissolve
    pause 0.6
    scene alexxis_olivia_exit_2 with dissolve
    olivia 0 "再来一次吧，帅哥，你最棒了！" with Dissolve(0.3)
    scene alexxis_olivia_exit_3 with dissolve
    olivia 0 "以后要常来哦！" with Dissolve(0.3)
    scene black with dissolve
    pause 1.0
    
            
    jump sujet_2

label alexxis_yumiko:

    scene alexxis_y_1
    gg 4 "今天，我选[yumiko]。"
    scene alexxis_y_2 with dissolve
    gg 4 "我也需要点时间放松一下、恢复点体力。"
    scene alexxis_y_3
    so 1 "选[yumiko]非常合适。"
    scene alexxis_y_4 with dissolve
    so 1 "她的手法很轻柔，但效果非常好。"
    scene alexxis_y_5
    so 1 "[yumiko]，去准备房间吧。"
    scene alexxis_y_6
    yumiko 1 "好吧。"
    scene alexxis_y_7 with dissolve
    yumiko 1 "请十五分钟后来我房间。"
    scene alexxis_y_8
    so 1 "这是您第一次来，可能还不太熟悉我们的服务。"
    scene alexxis_y_9 with dissolve
    so 1 "我保证，这会让你永生难忘……"
    scene alexxis_y_10 with dissolve
    gg 4 "那肯定。"
    scene black with dissolve
    pause 1.0
    scene alexxis_y_11 with dissolve
    pause 2.6
    scene alexxis_y_12
    so 1 "时候到了。"
    scene alexxis_y_13
    so 1 "请进，尽情享受吧。"
    stop music fadeout 3
    scene black with dissolve
    pause 3.0
    scene alexxis_y_14 with dissolve
    play music erotic_by_frank_schroeter volume 0.4
    yumiko 2 "欢迎光临，先生。" with dissolve
    show alexxis_y_15 with Dissolve(0.1)
    $ renpy.pause(2.7,hard=True)
    scene alexxis_y_16 with dissolve
    yumiko 2 "房间我已经为您准备好了。" with dissolve
    play sound oblom volume 0.2
    stop music
    scene alexxis_y_17 with hpunch
    ry0 0 "滚出去。"
    scene alexxis_y_18 with Dissolve(0.1)
    play music marty_gots_a_plan_by_kevin_macleod volume 0.7
    ry0 1 "现在我要跟她在一起。" with Dissolve(0.3)
    scene black with dissolve
    pause .3
    show alexxis_y_19 with Dissolve(0.3)
    gg 4 "（这家伙……）" with Dissolve(0.3)
    gg 4 "([ry]？！)"
    show alexxis_y_20 with dissolve
    gg 4 "现在轮到我跟[yumiko]了。" with Dissolve(0.3)
    hide alexxis_y_20 with dissolve
    gg 4 "[so]可以作证。" with Dissolve(0.3)
    show alexxis_y_21 with dissolve
    gg 4 "去排队等你的号吧。" with Dissolve(0.3)
    scene alexxis_y_22 with dissolve
    ry 1 "什么排队不排队的，关我什么事。" with Dissolve(0.3)
    scene alexxis_y_23 with dissolve
    ry 1 "我是这里的常客！" with Dissolve(0.3)
    scene alexxis_y_24 with dissolve
    ry 1 "现在给我滚出去，把她让给我！" with Dissolve(0.3)
    show alexxis_y_25 with Dissolve(0.1)
    $ renpy.pause(1,hard=True)
    scene alexxis_y_26 with dissolve
    yumiko 2 '{cps=5}……{/cps}' with dissolve
    gg 4 "（被宠坏的小少爷。）" with dissolve
    show alexxis_y_27 with Dissolve(0.1)
    $ renpy.pause(0.5,hard=True)
    ry 1 "先生，请听我说……" with Dissolve(0.1)
    scene alexxis_y_28 with dissolve
    ry 1 "没必要动手。请收下这个，换个人吧。" with Dissolve(0.3)
    show alexxis_y_29 with dissolve
    menu:
        '收下这笔钱：+$1000\\n[gr](金钱 +1000)[pink](奥莉维 成人场景)':
            $ renpy.notify('你获得了 +$1000。')
            scene alexxis_y_30_1 with dissolve
            ry 1 "明智的选择，小子。" with Dissolve(0.3)
            $ aksha += 1000
            scene alexxis_y_31_1 with dissolve
            ry 1 "现在请离开吧。" with Dissolve(0.3)
            scene black with dissolve
            stop music fadeout 5
            pause 2.0
            scene alexxis_y_32_1 with dissolve
            ry 1 "好了，宝贝，我们开始吧。" with Dissolve(0.3)
            scene alexxis_y_33_1 with dissolve
            gg 4 "（他为什么要给这么多？）" with Dissolve(0.3)
            gg 4 "（这里的服务真有那么贵吗？）"
            gg 4 "{cps=5}……{/cps}"
            pause 1.0
            scene alexxis_y_34_1 with dissolve
            gg 4 "（算了，我来这儿是为了找乐子的。换个人吧。）" with Dissolve(0.3)
            scene black with dissolve
            pause 2.0
            scene alexxis_yo_1 with dissolve
            pause 0.6
            gg 4 "[olivia]，我改主意了——今晚我想陪你。" with Dissolve(0.3)
            jump alexxis_olivia_1
            
        '坚持选[yumiko]\\n[pink](由美子 成人场景)':
            $ yumiko_ry = True
            scene alexxis_y_30 with vpunch
            gg 4 "我他妈打死你个混蛋……" with dissolve
            show alexxis_y_19 with dissolve
            gg 4 "把钱塞回你自己屁眼里，别来毁老子今晚的心情！她现在是我的。" with Dissolve(0.3)
            show alexxis_y_21 with dissolve
            gg 4 "现在给老子滚出去排队！" with Dissolve(0.3)
            hide alexxis_y_21 with dissolve
            ry 1 '{cps=5}……{/cps}' with dissolve
            scene alexxis_y_31 with dissolve
            ry 1 "好吧，了不起的小平民。" with Dissolve(0.3)
            scene alexxis_y_32 with dissolve
            ry 1 "今晚就让你玩个够。" with Dissolve(0.3)
            scene black with dissolve
            pause 1.0
            scene alexxis_y_33 with dissolve
            ry 1 "但别以为这事就这么算了！" with Dissolve(0.3)
            play sound door_close_power
            scene alexxis_y_34 with vpunch
            stop music fadeout 5
            gg 4 "赶紧滚！"
    scene black with dissolve
    pause 1.0
    scene alexxis_y_35 with dissolve
    play music erotic_by_frank_schroeter fadein 5 volume 0.4
    yumiko 2 "非常抱歉先生，我完全没想到会这样！" with dissolve
    scene alexxis_y_36 with dissolve
    yumiko 2 "我都不知道该怎么办……" with dissolve
    scene alexxis_y_37 with dissolve
    yumiko 2 '{cps=5}……{/cps}' with dissolve
    scene alexxis_y_38 with dissolve
    gg 4 "没关系，[yumiko]。我们继续吧？" with dissolve
    scene alexxis_y_39 with dissolve
    yumiko 2 "请跟我来。" with dissolve
    scene alexxis_y_40 with dissolve
    pause 1.0
    scene alexxis_y_41 with dissolve
    pause 2.0
    scene alexxis_y_42 with dissolve
    pause 2.0
    scene black with dissolve
    pause 1.0
    scene alexxis_y_43 with dissolve
    pause 1.0
    yumiko 2 "您以前来过这种地方吗？" with dissolve
    gg 0 "不。" with dissolve
    scene alexxis_y_44 with Dissolve(0.1)
    yumiko 2 "明白了。那就请相信我，好吗？" with dissolve
    scene alexxis_y_45 with Dissolve(0.1)
    yumiko 2 "请随意放松。" with dissolve
    scene alexxis_y_46 with dissolve
    yumiko 2 "什么都不用担心。" with dissolve
    scene alexxis_y_47 with Dissolve(0.1)
    yumiko 2 "一切交给我吧。" with dissolve
    scene alexxis_y_48 with dissolve
    gg 0 "（我等不及了。）" with dissolve
    scene alexxis_y_49 with dissolve
    pause 1.6
    scene alexxis_y_50 with dissolve
    pause 1.6
    scene alexxis_y_51 with dissolve
    pause 1.6
    scene alexxis_y_52 with dissolve
    pause 1.6
    scene alexxis_y_53 with dissolve
    yumiko 2 "感觉怎么样，先生？" with dissolve
    scene alexxis_y_54 with dissolve
    gg 0 "还用问？继续。" with dissolve
    scene alexxis_y_55 with dissolve
    yumiko 2 "要不……您脱下来吧……" with dissolve
    scene black with dissolve
    pause 1.0
    scene alexxis_y_56 with dissolve
    yumiko 2 '{cps=5}……{/cps}' with dissolve
    scene alexxis_y_57 with dissolve
    yumiko 2 '真是的……' with dissolve
    scene alexxis_y_58 with dissolve
    yumiko 2 '好大……' with dissolve
    scene alexxis_y_59 with dissolve
    yumiko 2 '您好！' with dissolve
    scene alexxis_y_60 with dissolve
    pause 1.0
    scene alexxis_y_59 with dissolve
    pause 1.0
    scene alexxis_y_61 with dissolve
    yumiko 2 "舒服吗？" with dissolve
    scene alexxis_y_62 with dissolve
    gg 0 "现在可以开始了。" with dissolve
    scene alexxis_y_63 with dissolve
    yumiko 2 '好。' with dissolve
    scene alexxis_y_64 with dissolve
    pause 1.0
    show alexxis_y_65 with dissolve
    gg 0 '（哦，靠……）' with dissolve
    ''
    show alexxis_y_66 with dissolve
    hide alexxis_y_65
    ''
    gg 0 '（天啊，这声音……）' with dissolve
    ''
    show alexxis_y_67 with dissolve
    hide alexxis_y_66
    pause 1.0
    ''
    gg 0 '（她越来越快了。我快射了。）' with dissolve
    ''
    gg 0 "你好厉害，[yumiko]。" with dissolve
    show alexxis_y_68 with dissolve
    hide alexxis_y_67
    yumiko 2 "好好享受。" with dissolve
    ''
    gg 0 '我要射了！' with dissolve
    scene black with dissolve
    pause 0.1
    show alexxis_y_68 with dissolve
    pause 0.5
    scene black with dissolve
    pause 0.3
    show alexxis_y_68 with dissolve
    pause 0.2
    scene black with dissolve
    play sound cumming
    scene alexxis_y_69 with dissolve
    yumiko 2 '啊！' with dissolve
    scene alexxis_y_70 with dissolve
    ''
    scene alexxis_y_71 with dissolve
    yumiko 2 '{cps=5}……{/cps}' with dissolve
    scene alexxis_y_72 with dissolve
    yumiko 2 '好多……' with dissolve
    scene alexxis_y_73 with dissolve
    pause 0.6
    scene alexxis_y_74 with dissolve
    pause 0.6
    scene alexxis_y_75 with dissolve
    pause 0.6
    scene alexxis_y_76 with dissolve
    pause 0.6
    gg 0 '（该死，我好像要漏出来了。）' with dissolve
    scene alexxis_y_77 with dissolve
    pause 0.6
    gg 0 '（她救了我。）' with dissolve
    scene alexxis_y_78 with dissolve
    yumiko 2 '嗯……' with dissolve
    scene alexxis_y_79 with dissolve
    gg 0 '[yumiko]，我喜欢这样。' with dissolve
    scene alexxis_y_80 with dissolve
    pause 0.3
    scene alexxis_y_79 with dissolve
    pause 0.2
    scene alexxis_y_80 with dissolve
    pause 0.1
    scene alexxis_y_79 with dissolve
    pause 0.2
    scene alexxis_y_81 with dissolve
    pause 1.0
    gg 0 '（刚才那是什么？）' with dissolve
    scene alexxis_y_82 with dissolve
    pause 1.0
    scene alexxis_y_83 with dissolve
    pause 1.0
    scene alexxis_y_84 with dissolve
    pause 0.3
    scene alexxis_y_85 with dissolve
    pause 1.0
    scene alexxis_y_86 with dissolve
    pause 0.6
    scene alexxis_y_87 with dissolve
    pause 1.0
    scene alexxis_y_88 with dissolve
    gg 0 '（她像只猫。）' with dissolve
    scene alexxis_y_89 with dissolve
    pause 1.0
    scene alexxis_y_90 with dissolve
    pause 1.0
    scene alexxis_y_91 with dissolve
    pause 0.6
    scene alexxis_y_92 with dissolve
    pause 0.3
    gg 0 '（她的眼睛为什么在那样发亮？）' with dissolve
    scene alexxis_y_93 with dissolve
    pause 0.6
    yumiko 2 '嗯……' with dissolve
    gg 0 '就是这样！对……' with dissolve
    scene alexxis_y_94 with dissolve
    yumiko 2 '*吮吸*' with dissolve
    pause 1.0
    scene alexxis_y_95 with dissolve
    pause 1.0
    scene alexxis_y_96 with dissolve
    ''
    scene black with dissolve
    pause 1.0
    scene alexxis_y_97 with dissolve
    ''
    scene alexxis_y_98 with dissolve
    pause 1.6
    scene alexxis_y_99 with dissolve
    pause 1.0
    scene alexxis_y_100 with dissolve
    pause 0.7
    scene alexxis_y_101 with dissolve
    pause 1.0
    gg 0 "您好像在想很色色的事情呢。" with dissolve
    scene alexxis_y_102 with dissolve
    pause 1.0
    scene alexxis_y_103 with dissolve
    pause 0.3
    show alexxis_y_104 with dissolve
    ''
    show alexxis_y_105 with dissolve
    hide alexxis_y_104
    gg 0 '（天啊，那个眼神……）'
    show alexxis_y_106 with dissolve
    hide alexxis_y_105
    gg 0 '（靠……）' with dissolve
    pause 0.3
    gg 0 '太色情了……'
    show alexxis_y_104 with dissolve
    hide alexxis_y_106
    ''
    show alexxis_y_107 with dissolve
    hide alexxis_y_104
    pause 0.6
    gg 0 '（她看我的眼神，像是被附身了一样。）'
    show alexxis_y_106 with dissolve
    hide alexxis_y_107
    gg 0 '靠，太好了……'
    gg '再深一点！'
    show alexxis_y_108 with dissolve
    hide alexxis_y_106
    gg 0 '（该死……太爽了！）'
    ''
    gg 0 '[yumiko]，再快一点，我要射了。'
    show alexxis_y_109 with dissolve
    hide alexxis_y_108
    pause 0.3
    gg 0 '保持速度，别停！'
    ''
    gg 0 '（快了……）' with dissolve
    show alexxis_y_110 with dissolve
    hide alexxis_y_109
    ''
    gg 0 '我要射了！' with dissolve
    scene black with dissolve
    pause 0.3
    show alexxis_y_110
    pause 0.2
    scene black with dissolve
    play sound cumming
    pause 0.6
    show alexxis_y_111 with dissolve
    $ renpy.pause(3.5,hard=True)
    scene alexxis_y_112 with dissolve
    pause 1.0
    gg 0 '这纹身真可爱。' with dissolve
    pause 1.0
    show alexxis_y_113 with Dissolve(0.6)
    $ renpy.pause(2.4,hard=True)
    show alexxis_y_114 with Dissolve(0.1)
    hide alexxis_y_113
    pause 1.0
    gg 0 "我本来没打算这么使力的。" with dissolve
    gg 0 "我想尽量遵守规定。"
    gg 0 "但如果一直这样，我怕自己会忍不住。"
    scene alexxis_y_115 with dissolve
    yumiko 2 "我这么做是希望您能放松。" with dissolve
    scene alexxis_y_116 with dissolve
    yumiko 2 "您明白我为什么这么做，对吧？" with dissolve
    show alexxis_y_114 with Dissolve(0.6)
    pause 0.3
    gg 0 "您也许会后悔的。" with dissolve
    $ persistent.gallery_yumiko_unlock_1 = True ## Gallery with Yumiko 1 - open
    pause 0.6
    call screen yumiko_sex_choice

label alexxis_yumiko_sex_1:

    $ alexxis_yumiko_choice_sex_1 += 1
    scene black with dissolve
    
    if alexxis_yumiko_choice_sex_2 == 0:
        show alexxis_y_sex1_1 with dissolve
        pause 2.0
        gg 0 '天啊，这身材……' with dissolve
        ''
        scene alexxis_y_sex1_2 with dissolve
        pause 1.0
        scene alexxis_y_sex1_3 with dissolve
        pause 0.6
        gg 0 "[yumiko]，现在把你的手拿开。" with dissolve
        scene alexxis_y_sex1_4 with dissolve
        pause 0.6
        gg 0 "（现在这个洞我有用。）"with dissolve
        scene black with dissolve
        pause 1.0
        scene alexxis_y_sex1_5 with dissolve
        pause 2.0
        scene alexxis_y_sex1_5_1 with dissolve
        gg 0 '啧，该死！' with dissolve
        scene alexxis_y_sex1_6 with dissolve
        pause 1.6
        scene alexxis_y_sex1_6_1 with dissolve
        yumiko 3 '...!' with dissolve
        scene alexxis_y_sex1_7 with dissolve
        gg 0 '你知道我现在要对你做什么吗？' with dissolve
        gg '[yumiko]……' with dissolve
        yumiko 3 '{cps=5}……{/cps}' with dissolve
        scene alexxis_y_sex1_8 with dissolve
        yumiko 3 '你要干什么？' with dissolve
        scene alexxis_y_sex1_9 with dissolve
        yumiko 3 '我……' with dissolve
        scene alexxis_y_sex1_10 with dissolve
        gg 0 "我现在要用你的小穴了。" with dissolve
        yumiko 3 "诶？" with dissolve
        gg 0 "不行吗？" with dissolve
        scene alexxis_y_sex1_11 with dissolve
        pause 1.0
        scene alexxis_y_sex1_12 with dissolve
        pause 0.3
        scene alexxis_y_sex1_11 with dissolve
        pause 0.1
        scene alexxis_y_sex1_12 with dissolve
        yumiko 3 '{cps=5}……{/cps}' with dissolve
        gg 0 "（她的眼睛怎么了，那是隐形眼镜吗？）" with dissolve
        scene alexxis_y_sex1_13 with dissolve
        yumiko 3 "请便。" with dissolve
        scene alexxis_y_sex1_14 with dissolve
        yumiko 3 "放进来。" with dissolve
        scene alexxis_y_sex1_13 with dissolve
        gg 0 '好好说话。' with dissolve
        scene alexxis_y_sex1_15 with dissolve
        yumiko 3 '请、请把它放进来！' with dissolve
        play sound cumming
        scene alexxis_y_sex1_16 with dissolve
        yumiko 3 '呃！' with dissolve
        scene alexxis_y_sex1_17 with dissolve
        pause 1.0
        scene alexxis_y_sex1_18 with dissolve
        pause 1.0
        scene alexxis_y_sex1_19 with dissolve
        pause 1.0
        gg 0 "我要开始了。" with dissolve
        show alexxis_y_sex1_20 with Dissolve(0.6)
        gg 0 '（她体内这些温热的感觉……）' with dissolve
        show alexxis_y_sex1_21 with Dissolve(0.1)
        hide alexxis_y_sex1_20
        gg 0 '（爽死了。）' with dissolve
        show alexxis_y_sex1_22 with Dissolve(0.1)
        hide alexxis_y_sex1_21
        $ renpy.pause(3.96,hard=True)
        show alexxis_y_sex1_23 with Dissolve(0.1)
        hide alexxis_y_sex1_22
        ''
        show alexxis_y_sex1_24 with Dissolve(0.1)
        hide alexxis_y_sex1_23
        pause 1.0
        yumiko 3 '我……' with dissolve
        pause 1.0
        yumiko 3 '{cps=5}……{/cps}我爱死了这一切。' with dissolve
        ''
        show alexxis_y_sex1_25 with Dissolve(0.6)
        hide alexxis_y_sex1_24
        ''
        show alexxis_y_sex1_26 with Dissolve(0.1)
        hide alexxis_y_sex1_25
        ''
        show alexxis_y_sex1_27 with Dissolve(0.1)
        hide alexxis_y_sex1_26
        ''
        show alexxis_y_sex1_28 with dissolve
        hide alexxis_y_sex1_27
        ''
        show alexxis_y_sex1_29 with Dissolve(0.6)
        hide alexxis_y_sex1_28
        ''
        show alexxis_y_sex1_30 with Dissolve(0.1)
        hide alexxis_y_sex1_29
        ''
        show alexxis_y_sex1_31 with Dissolve(0.6)
        hide alexxis_y_sex1_30
        yumiko 3 '啊！' with dissolve
        ''
        show alexxis_y_sex1_32 with Dissolve(0.1)
        hide alexxis_y_sex1_31
        pause 1.0
        yumiko 3 "{cps=5}主、主{/cps}人……" with dissolve
        gg 0 "（我要射了！）" with dissolve
        show alexxis_y_sex1_33 with Dissolve(0.1)
        hide alexxis_y_sex1_32
        yumiko 3 "我很喜欢这种感觉。" with dissolve
        gg 0 '再深一点点……' with dissolve
        show alexxis_y_sex1_34 with Dissolve(0.1)
        hide alexxis_y_sex1_33
        ''
        gg 0 "（我现在就要射了！）" with dissolve
        $ persistent.gallery_yumiko_unlock_2 = True ## Gallery with Yumiko 2 - open
        menu:
            "射在里面":
                show alexxis_y_sex1_35 with dissolve
                hide alexxis_y_sex1_34
                $ renpy.pause(3.5,hard=True)
                show alexxis_y_sex1_36 with Dissolve(0.6)
                hide alexxis_y_sex1_35
                
                pause 2.0
                call screen yumiko_sex_choice
            
            "射在小腹上":
                show alexxis_y_sex1_37 with dissolve
                hide alexxis_y_sex1_34
                $ renpy.pause(0.4,hard=True)
                scene black with Dissolve(0.2)
                $ alexxis_yumiko_outcumming = True
                play sound cumming
                pause 0.6
                show alexxis_y_sex1_38 with dissolve
                
                pause 2.0
                call screen yumiko_sex_choice
        
    if alexxis_yumiko_choice_sex_2 == 1:
        
        scene black with dissolve
        pause 1.0
        scene alexxis_y_sex1_5 with dissolve
        pause 2.0
        scene alexxis_y_sex1_5_1 with dissolve
        gg 0 '啧，该死！' with dissolve
        scene alexxis_y_sex1_6 with dissolve
        pause 1.6
        scene alexxis_y_sex1_6_1 with dissolve
        yumiko 3 '...!' with dissolve
        scene alexxis_y_sex1_7 with dissolve
        gg 0 "这次换我来主导。" with dissolve
        gg 0 '放松点。' with dissolve
        yumiko 3 '{cps=5}……{/cps}' with dissolve
        scene alexxis_y_sex1_8 with dissolve
        yumiko 3 '你要干什么？' with dissolve
        scene alexxis_y_sex1_9 with dissolve
        yumiko 3 '我……' with dissolve
        scene alexxis_y_sex1_10 with dissolve
        gg 0 "我要再上一次你的小穴。" with dissolve
        yumiko 3 '诶？' with dissolve
        gg 0 "你不介意吧？" with dissolve
        scene alexxis_y_sex1_11 with dissolve
        pause 1.0
        scene alexxis_y_sex1_12 with dissolve
        pause 0.3
        scene alexxis_y_sex1_11 with dissolve
        pause 0.1
        scene alexxis_y_sex1_12 with dissolve
        yumiko 3 '{cps=5}……{/cps}' with dissolve
        gg 0 "（她的眼睛怎么了，是那副隐形眼镜吗？）" with dissolve
        scene alexxis_y_sex1_13 with dissolve
        yumiko 3 "我不介意，随您高兴。" with dissolve
        scene alexxis_y_sex1_14 with dissolve
        yumiko 3 '把它放进来。' with dissolve
        scene alexxis_y_sex1_13 with dissolve
        gg 0 '好好说话。' with dissolve
        scene alexxis_y_sex1_15 with dissolve
        yumiko 3 '请、请把它放进来！' with dissolve
        play sound cumming
        scene alexxis_y_sex1_16 with dissolve
        yumiko 3 '呃！' with dissolve
        scene alexxis_y_sex1_17 with dissolve
        pause 1.0
        scene alexxis_y_sex1_18 with dissolve
        pause 1.0
        scene alexxis_y_sex1_19 with dissolve
        pause 1.0
        gg 0 '我开始动了。' with dissolve
        show alexxis_y_sex1_20 with Dissolve(0.6)
        gg 0 "（里面又暖又软……）" with dissolve
        show alexxis_y_sex1_21 with Dissolve(0.1)
        hide alexxis_y_sex1_20
        gg 0 "（爽到不行。）" with dissolve
        show alexxis_y_sex1_22 with Dissolve(0.1)
        hide alexxis_y_sex1_21
        $ renpy.pause(3.96,hard=True)
        show alexxis_y_sex1_23 with Dissolve(0.1)
        hide alexxis_y_sex1_22
        ''
        show alexxis_y_sex1_24 with Dissolve(0.1)
        hide alexxis_y_sex1_23
        pause 1.0
        yumiko 3 '是您在动……' with dissolve
        pause 1.0
        yumiko 3 '{cps=5}……{/cps}要把我弄疯了' with dissolve
        ''
        show alexxis_y_sex1_25 with Dissolve(0.6)
        hide alexxis_y_sex1_24
        ''
        show alexxis_y_sex1_26 with Dissolve(0.1)
        hide alexxis_y_sex1_25
        ''
        show alexxis_y_sex1_27 with Dissolve(0.1)
        hide alexxis_y_sex1_26
        ''
        show alexxis_y_sex1_28 with dissolve
        hide alexxis_y_sex1_27
        ''
        show alexxis_y_sex1_29 with Dissolve(0.6)
        hide alexxis_y_sex1_28
        ''
        show alexxis_y_sex1_30 with Dissolve(0.1)
        hide alexxis_y_sex1_29
        ''
        show alexxis_y_sex1_31 with Dissolve(0.6)
        hide alexxis_y_sex1_30
        yumiko 3 '啊！' with dissolve
        ''
        show alexxis_y_sex1_32 with Dissolve(0.1)
        hide alexxis_y_sex1_31
        pause 1.0
        yumiko 3 "{cps=5}主、主{/cps}人……" with dissolve
        gg 0 "（她快到了。）" with dissolve
        show alexxis_y_sex1_33 with Dissolve(0.1)
        hide alexxis_y_sex1_32
        yumiko 3 '感觉真好。' with dissolve
        gg 0 '再一点点……' with dissolve
        show alexxis_y_sex1_34 with Dissolve(0.1)
        hide alexxis_y_sex1_33
        ''
        gg 0 "（我要射了！）" with dissolve
        $ persistent.gallery_yumiko_unlock_2 = True ## Gallery with Yumiko 2 - open
        menu:
            "射在里面":
                show alexxis_y_sex1_35 with dissolve
                hide alexxis_y_sex1_34
                $ renpy.pause(3.5,hard=True)
                show alexxis_y_sex1_36 with Dissolve(0.6)
                hide alexxis_y_sex1_35
                ''
                pause 0.6
            
            "射在小腹上":
                show alexxis_y_sex1_37 with dissolve
                hide alexxis_y_sex1_34
                $ renpy.pause(0.4,hard=True)
                scene black with Dissolve(0.2)
                play sound cumming
                pause 0.6
                show alexxis_y_sex1_38 with dissolve
                ''
                pause 0.6
        
        jump alexxis_yumiko_exit

label alexxis_yumiko_sex_2:

    $ alexxis_yumiko_choice_sex_2 += 1
    scene black with dissolve
    
    if alexxis_yumiko_choice_sex_1 == 0:
    
        show alexxis_y_sex1_1 with dissolve
        pause 2.0
        gg 0 '我的天，这身材……' with dissolve
        ''
        scene alexxis_y_sex1_2 with dissolve
        pause 1.0
        scene alexxis_y_sex1_3 with dissolve
        pause 0.6
        yumiko 3 '主人，请仰躺下。' with dissolve
        scene alexxis_y_sex1_4 with dissolve
        pause 0.6
        yumiko 3 "一切交给我。" with dissolve
        scene black with dissolve
        pause 1.0
        
        scene alexxis_y_sex2_1 with dissolve
        pause 2.0
        scene alexxis_y_sex2_2 with dissolve
        pause 1.6
        scene alexxis_y_sex2_3 with dissolve
        yumiko 3 "就这样躺好，放松。" with dissolve
        scene alexxis_y_sex2_4 with dissolve
        pause 2.0
        scene alexxis_y_sex2_5 with dissolve
        pause 2.0
        gg 0 "（她太骚了，快把我逼疯了。）" with dissolve
        scene alexxis_y_sex2_6 with Dissolve(0.3)
        play sound cumming
        yumiko 3 '啊……' with dissolve
        gg 0 "（进来了！）" with dissolve
        scene alexxis_y_sex2_7 with Dissolve(0.3)
        yumiko 3 "我快撑不住了……" with dissolve
        scene alexxis_y_sex2_8 with Dissolve(0.3)
        gg 0 "明明是主人自己坐上来的。" with dissolve
        scene alexxis_y_sex2_9 with Dissolve(0.3)
        yumiko 3 "好大……" with dissolve
        scene alexxis_y_sex2_10 with dissolve
        yumiko 3 '啊！' with dissolve
        gg 0 '请开始动吧。' with dissolve
        show alexxis_y_sex2_11 with dissolve
        ''
        show alexxis_y_sex2_12 with dissolve
        hide alexxis_y_sex2_11
        ''
        show alexxis_y_sex2_13 with dissolve
        hide alexxis_y_sex2_12
        yumiko 3 '主人……' with dissolve
        yumiko 3 '感觉舒服吗？' with dissolve
        show alexxis_y_sex2_14 with Dissolve(0.3)
        hide alexxis_y_sex2_13
        gg 0 '嗯，[yumiko]，非常舒服……' with dissolve
        gg 0 '我快射了。' with dissolve
        show alexxis_y_sex2_15 with Dissolve(0.3)
        hide alexxis_y_sex2_14
        yumiko 3 '你滑动的动作……我能感觉到你的形状……' with dissolve
        yumiko 3 '感觉它变得更大更胀了。' with dissolve
        show alexxis_y_sex2_16 with Dissolve(0.3)
        hide alexxis_y_sex2_15
        ''
        gg 0 '我真的撑不住了……' with dissolve
        show alexxis_y_sex2_17 with Dissolve(0.3)
        hide alexxis_y_sex2_16
        gg 0 '（再一点点！）' with dissolve
        ''
        gg 0 "我要射了！" with dissolve
        scene black with dissolve
        pause 1.0
        show alexxis_y_sex2_18 with Dissolve(0.3)
        hide alexxis_y_sex2_17
        $ renpy.pause(5.9,hard=True)
        show alexxis_y_sex2_19 with Dissolve(0.3)
        hide alexxis_y_sex2_18
        pause 1.0
        yumiko 3 "我也去了。" with Dissolve(0.3)
        $ persistent.gallery_yumiko_unlock_3 = True ## Gallery with Yumiko 3 - open
        pause 1.6
        
        call screen yumiko_sex_choice
    
    if alexxis_yumiko_choice_sex_1 == 1:

        if alexxis_yumiko_outcumming == False:
        
            scene alexxis_y_sex2_1 with dissolve
            pause 2.0
            scene alexxis_y_sex2_2 with dissolve
            pause 1.6
            scene alexxis_y_sex2_3 with dissolve
            yumiko 3 '现在躺下休息吧，主人。' with dissolve
            yumiko 3 "一切交给我" with dissolve
            scene alexxis_y_sex2_4 with dissolve
            pause 2.0
            scene alexxis_y_sex2_5 with dissolve
            pause 2.0
            gg 0 "（她简直性感得要命……）" with dissolve
            scene alexxis_y_sex2_6 with Dissolve(0.3)
            play sound cumming
            yumiko 3 '唔嗯……' with dissolve
            gg 0 "（我又进到她里面了！）" with dissolve
            scene alexxis_y_sex2_7 with Dissolve(0.3)
            yumiko 3 "我受不了了……" with dissolve
            scene alexxis_y_sex2_8 with Dissolve(0.3)
            gg 0 "明明是主人坐上来的。" with dissolve
            scene alexxis_y_sex2_9 with Dissolve(0.3)
            yumiko 3 "好大……" with dissolve
            scene alexxis_y_sex2_10 with dissolve
            yumiko 3 '啊！' with dissolve
            gg 0 '请开始动吧。' with dissolve
            show alexxis_y_sex2_11 with dissolve
            ''
            show alexxis_y_sex2_12 with dissolve
            hide alexxis_y_sex2_11
            ''
            show alexxis_y_sex2_13 with dissolve
            hide alexxis_y_sex2_12
            yumiko 3 "主人……感觉舒服吗？" with dissolve
            show alexxis_y_sex2_14 with Dissolve(0.3)
            hide alexxis_y_sex2_13
            gg 0 "嗯，[yumiko]……不只是舒服。我又快到了。" with dissolve
            show alexxis_y_sex2_15 with Dissolve(0.3)
            hide alexxis_y_sex2_14
            yumiko 3 "你滑动的动作……每一寸都能感觉到……" with dissolve
            yumiko 3 "在我里面变得越来越大……" with dissolve
            show alexxis_y_sex2_16 with Dissolve(0.3)
            hide alexxis_y_sex2_15
            ''
            gg 0 "我再也撑不住了……" with dissolve
            show alexxis_y_sex2_17 with Dissolve(0.3)
            hide alexxis_y_sex2_16
            gg 0 '（再一点点！）' with dissolve
            ''
            gg 0 "我要射了！" with dissolve
            scene black with dissolve
            pause 1.0
            show alexxis_y_sex2_18 with Dissolve(0.3)
            hide alexxis_y_sex2_17
            $ renpy.pause(5.9,hard=True)
            show alexxis_y_sex2_19 with Dissolve(0.3)
            hide alexxis_y_sex2_18
            ''
            pause 0.6
            
        if alexxis_yumiko_outcumming == True:
        
            scene alexxis_y_sex2_1 with dissolve
            pause 2.0
            scene alexxis_y_sex2_2_outcum with dissolve
            pause 1.6
            scene alexxis_y_sex2_3_outcum with dissolve
            yumiko 3 '现在就这样躺下休息吧，主人。' with dissolve
            yumiko 3 "一切交给我。"
            scene alexxis_y_sex2_4_outcum with dissolve
            pause 2.0
            scene alexxis_y_sex2_5_outcum with dissolve
            pause 2.0
            gg 0 "（她太骚了，快把我逼疯了。）" with dissolve
            scene alexxis_y_sex2_6_outcum with Dissolve(0.3)
            play sound cumming
            yumiko 3 '唔……' with dissolve
            gg 0 "（我又进到她里面了！）" with dissolve
            scene alexxis_y_sex2_7_outcum with Dissolve(0.3)
            yumiko 3 "我受不了了……" with dissolve
            scene alexxis_y_sex2_8_outcum with Dissolve(0.3)
            gg 0 "明明是主人自己坐下的。" with dissolve
            scene alexxis_y_sex2_9_outcum with Dissolve(0.3)
            yumiko 3 "好大好胀……" with dissolve
            scene alexxis_y_sex2_10_outcum with dissolve
            yumiko 3 '啊！' with dissolve
            gg 0 '请开始动吧。' with dissolve
            show alexxis_y_sex2_11_outcum with dissolve
            ''
            show alexxis_y_sex2_12_outcum with dissolve
            hide alexxis_y_sex2_11_outcum
            ''
            show alexxis_y_sex2_13_outcum with dissolve
            hide alexxis_y_sex2_12_outcum
            yumiko 3 "主人……感觉舒服吗？" with dissolve
            show alexxis_y_sex2_14_outcum with Dissolve(0.3)
            hide alexxis_y_sex2_13_outcum
            gg 0 "嗯，[yumiko]，太爽了……我爱死了。又要射了。" with dissolve
            show alexxis_y_sex2_15_outcum with Dissolve(0.3)
            hide alexxis_y_sex2_14_outcum
            yumiko 3 "你滑动的动作让我把你的形状感觉得这么清楚……感觉它变得越来越大。" with dissolve
            show alexxis_y_sex2_16_outcum with Dissolve(0.3)
            hide alexxis_y_sex2_15_outcum
            ''
            gg 0 "我真的撑不住了……" with dissolve
            show alexxis_y_sex2_17_outcum with Dissolve(0.3)
            hide alexxis_y_sex2_16_outcum
            gg 0 '（再坚持一下！）' with dissolve
            yumiko '太爽了……' 
            gg 0 '当然。' 
            ''
            gg 0 "我要射了！" with dissolve
            scene black with dissolve
            pause 1.0
            show alexxis_y_sex2_18 with Dissolve(0.3)
            hide alexxis_y_sex2_17_outcum
            $ renpy.pause(5.9,hard=True)
            show alexxis_y_sex2_19 with Dissolve(0.3)
            hide alexxis_y_sex2_18
            ''
            pause 0.6
        
        $ persistent.gallery_yumiko_unlock_3 = True ## Gallery with Yumiko 3 - open
        jump alexxis_yumiko_exit

label alexxis_yumiko_exit:

    scene black with dissolve
    stop music fadeout 5
    pause 5.0
    
    jump sujet_2

#Alexxis Exit
label sujet_2:

    scene black with dissolve
    pause 1.0
    play music3 cocktails_and_lobsters_by_alexander_nakarada volume 0.6
    show alexxis_exit_1 with Dissolve(0.6)
    $ renpy.pause(5.9,hard=True)
    scene alexxis_exit_2 with dissolve
    so 1 "刚才很棒吧？" with Dissolve(0.3)
    show alexxis_exit_3 with Dissolve(0.6)
    gg 4 "嗯，爽到不行。就像站了好几年终于坐下了。" with Dissolve(0.3)
    scene alexxis_exit_4 with dissolve
    so 1 "您能喜欢就好。" with dissolve
    scene alexxis_exit_5 with dissolve
    so 1 "现在是结账时间。" with Dissolve(0.3)
    scene alexxis_exit_6 with dissolve
    so 1 "一共 $800。" with Dissolve(0.3)
    show alexxis_exit_3 with Dissolve(0.6)
    gg 4 "（我靠！整整 $800！）" with Dissolve(0.3)
    
    if aksha >= 800:
        gg 4 "（现在我明白[ry]为什么给那么多了。）"
        pause 0.1
        
        menu:
            "支付：-$800\\n[gr](推荐)" if aksha >= 800:
                gg 4 "（现在我明白[ry]为什么给那么多了。）" with Dissolve(0.3)
                gg "（我身上有 $[aksha]。）"
                show alexxis_exit_pay_1 with Dissolve(0.6)
                gg 4 "给你。" with Dissolve(0.3)
                hide alexxis_exit_pay_1 with Dissolve(0.6)
                show alexxis_exit_pay_2 with Dissolve(0.6)
                hide alexxis_exit_3
                $ renpy.notify('你支付了 $800。')
                $ aksha -= 800
                gg 4 "（幸好有[ry]给的那笔额外的钱。）" with Dissolve(0.3)
                gg 4 "（不然可就难堪了。）"
                scene alexxis_exit_pay_3 with dissolve
                so 1 "一切都办妥了。" with Dissolve(0.3)
                scene alexxis_exit_pay_4 with dissolve
                so 1 "感谢您选择「Alexxis」。" with Dissolve(0.3)
                scene alexxis_exit_pay_5 with dissolve
                gg 4 "不客气，[so]。这里的服务物超所值。" with Dissolve(0.3)
                scene alexxis_exit_pay_6 with dissolve
                so 1 "您能这么说我很高兴。期待您再来。" with Dissolve(0.3)
                
                jump home_gg_shower
                
            "撒谎：「我没那么多钱。」":
                gg 4 "（好吧，我有 $[aksha]。）" with Dissolve(0.3)
                gg 4 "（钱是够。但我不想把钱全给她。）"
                scene alexxis_exit_7 with dissolve
                gg 4 "我没那么多钱。身上只有 $250。" with Dissolve(0.3)
                $ dolg_alexxis = True
                scene alexxis_exit_8 with dissolve
                so 1 "原来如此……" with Dissolve(0.3)
                scene alexxis_exit_9 with dissolve
                so 1 '{cps=5}……{/cps}' with Dissolve(0.3)
                scene alexxis_exit_10 with dissolve
                so 1 "您明白「Alexxis」不是城里其他地方那种地方吧？" with Dissolve(0.3)
                scene alexxis_exit_11 with dissolve
                so 1 "我们接待的是高端客人，价格也对应我们的服务品质。" with Dissolve(0.3)
                scene alexxis_exit_12 with dissolve
                gg 4 "这就很尴尬了。我还以为跟别处一样，一次 $100 到 $150。" with Dissolve(0.3)
                scene alexxis_exit_13 with dissolve
                so 1 "差距可不小，先生……" with Dissolve(0.3)
                scene alexxis_exit_14 with dissolve
                so 1 "不过，已经享受过的服务，您还是得付钱。" with Dissolve(0.3)
                show alexxis_exit_15 with Dissolve(0.6)
                gg 4 "（怎么才能不付钱就脱身？）" with Dissolve(0.3)
                gg 4 "（钱是够，但太贵了。）"
                gg 4 "我明白得付钱，可我只有 $250。能通融一下吗？"
                
    else:
        gg 4 "（我只有 $[aksha]。）"
        gg 4 "（搞什么！）"
        scene alexxis_exit_7 with dissolve
        gg 4 "我没那么多钱，身上只有 $[aksha]。" with dissolve
        $ dolg_alexxis = True
        scene alexxis_exit_8 with dissolve
        so 1 "原来如此……" with Dissolve(0.3)
        scene alexxis_exit_9 with dissolve
        so 1 '{cps=5}……{/cps}' with Dissolve(0.3)
        scene alexxis_exit_10 with dissolve
        so 1 "您明白「Alexxis」不是城里其他地方那种地方吧？" with Dissolve(0.3)
        scene alexxis_exit_11 with dissolve
        so 1 "我们接待的是高端客人，价格也对应我们的服务品质。" with Dissolve(0.3)
        scene alexxis_exit_12 with dissolve
        gg 4 "这就很尴尬了。我还以为跟别处一样，一次 $100 到 $150。" with Dissolve(0.3)
        scene alexxis_exit_13 with dissolve
        so 1 "差距可不小，先生……" with Dissolve(0.3)
        scene alexxis_exit_14 with dissolve
        so 1 "不过，已经享受过的服务，您还是得付钱。" with Dissolve(0.3)
        show alexxis_exit_15 with Dissolve(0.6)
        gg 4 "（怎么才能不付钱就脱身？）" with Dissolve(0.3)
        gg 4 "我明白得付钱，可我只有 $[aksha]。能通融一下吗？"
        
    gg 4 "新客能有折扣吗？"
    scene alexxis_exit_9 with dissolve
    so 1 '{cps=5}……{/cps}' with Dissolve(0.3)
    scene alexxis_exit_10 with dissolve
    so 1 "我们不打折。离开之前，您得把剩下的钱付清。" with Dissolve(0.3)
    show alexxis_exit_15 with Dissolve(0.6)
    gg 4 "（要是保安来了翻我的口袋，那只会更糟。）" with Dissolve(0.3)
    gg 4 '{cps=5}……{/cps}'
    $ renpy.music.set_volume(1, delay=3, channel=u'music3')
    gg "[so]，我没想到这么贵。能通融一次吗？" with Dissolve(0.3)
    $ renpy.music.set_volume(0.3, delay=3, channel=u'music3')
    scene alexxis_exit_16 with dissolve
    pause 0.6
    play sound2 dm2
    play sound heart_bass volume 1.6
    scene alexxis_exit_16_1 with dissolve
    pause 0.6
    scene alexxis_exit_17 with dissolve
    pause 0.6
    scene alexxis_exit_18_1 with dissolve
    pause 0.3
    scene alexxis_exit_18 with dissolve
    pause 0.3
    scene alexxis_exit_18_1 with dissolve
    pause 0.3
    scene alexxis_exit_18 with dissolve
    pause 1.0
    gg 4 "（又来这套？）" with Dissolve(0.3)
    scene alexxis_exit_19 with dissolve
    $ renpy.music.set_volume(1, delay=3, channel=u'music3')
    so 1 "您说得对，我应该事先告诉您价格。" with Dissolve(0.3)
    scene alexxis_exit_13 with dissolve
    so 1 "铁公鸡……" with Dissolve(0.3)
    scene alexxis_exit_20 with dissolve
    gg 4 "诶？" with Dissolve(0.3)
    scene alexxis_exit_21 with dissolve
    so 1 "哦，我把这话说出来了？" with Dissolve(0.3)
    gg 4 "（你这个婊子。）"
    scene alexxis_exit_22 with dissolve
    so 1 "为此我道歉。您可以走了。" with Dissolve(0.3)
    scene alexxis_exit_23 with dissolve
    gg 4 "感谢您的理解。" with Dissolve(0.3)
    scene alexxis_exit_24 with dissolve
    so 1 "不客气。" with Dissolve(0.3)
    scene alexxis_exit_25 with hpunch
    so 1 "不过，您还是得把剩下的钱付清。" with Dissolve(0.3)
    gg 4 "（想都别想。我不会再来了。）" with Dissolve(0.3)
    scene alexxis_exit_26 with dissolve
    so 1 "这次我先放您走，但请尽快回来把剩下的钱补上。" with Dissolve(0.3)
    scene alexxis_exit_27 with dissolve
    gg 4 "当然，我一定会回来付钱的。谢谢理解。" with Dissolve(0.3)
    scene alexxis_exit_28 with dissolve
    so 1 "不客气。我们恭候。" with Dissolve(0.3)
    
    jump home_gg_shower

#Home gg shower
label home_gg_shower:
    stop music fadeout 4
    stop music2 fadeout 4
    stop music3 fadeout 5
    scene black with dissolve
    pause 5.0
    play music may_shower_close
    show sweethome_end_1 with dissolve
    pause 1.6
    if not_know_alexxis == True:
        pause 0.1
    if not_know_alexxis == False:
        gg 0 "（我在「Alexxis」过得很开心。是个难忘的夜晚。）" with dissolve
        if dolg_alexxis:
            gg 0 "（不过现在得把欠的钱还上。而且不能拖。）"
            gg 0 "（我有种不好的预感。）"
        else:
            gg 0 "（可惜我当时只想着钱。）" with Dissolve(0.3)
            gg 0 "（不过话说回来，那些钱正好救了我——服务费高得离谱。而且我也得到了想要的。）"
        if yumiko_ry:
            gg 0 "（再说了，我还顶撞了那个金发富二代。他肯定记得。）"
            gg 0 "（但跟[yumiko]真的爽到不行，我一点不后悔。）"
    gg 0 "{cps=5}……{/cps}" with Dissolve(0.3)
    gg 0 "（今天的行程算是结束了。总体还不错。）"
    gg 0 "（学校比想象中乱多了，不过只要我表现得好，他们应该会放过我。）"
    gg 0 "{cps=5}……{/cps}"
    show sweethome_end_2 with dissolve
    hide sweethome_end_1
    gg 0 "（糟了。我好像把包忘在学校了。）"
    gg 0 "（全拜[ry]带头的那群垃圾所赐。）"
    gg 0 "（我记得他们那边有两个人在我班上。）"
    gg 0 "（一个叫[dai]的胖子，还有他的跟班[me]。）"
    gg 0 "（不过跟那个金发混蛋比起来，他们看着还挺无害。要是他们最拿手的就是绊人……）"
    gg 0 "（也许他们是想用这种方式立威。）"
    gg 0 "（但要是他们再来找事，我就得教训他们一顿。）"

    if draka_roof_loose == False:
        gg 0 "（[da]这是他应得的。得保持警惕。下次再碰面，结果可能就不一样了。）"
    if draka_roof_loose == True:
        gg 0 "（这次我输给了[da]。下次就不会了……）"
    gg 0 "（这家伙绝对有病。）"
    gg 0 "（鬼知道他在想什么。总之还是保持距离为好。）"
    gg 0 "（或者反过来靠近他。不是因为害怕，而是出于策略。有时离得近反而更容易观察。）"
    gg 0 "（如果非要跟这种人打交道——我会让他们明白欺负人不是个好主意。）"
    gg 0 "{cps=5}……{/cps}"
    play sound demon_moment volume 0.5
    show sweethome_end_3 with vpunch
    hide sweethome_end_2
    pause 2.0
    asami0 0 "终于找到你了，[gg]……" with Dissolve(0.3)
    show sweethome_end_4 with Dissolve(0.6)
    hide sweethome_end_3
    $ renpy.pause(3.9,hard=True)
    play sound woosh0
    stop music fadeout 5
    
label sujet_3:
    play sound2 heart_bass volume 2.0
    play music2 ancient_basement_by_tim_kulig fadein 6 volume 0.5
    scene black with Dissolve(0.3)
    stop sound2 fadeout 13
    pause 3.0
    scene sweethome_end_5 with Dissolve(2.0)
    ''
    scene sweethome_end_6 with dissolve
    pause 1.6
    scene sweethome_end_7 with dissolve
    ''
    scene sweethome_end_8 with dissolve
    pause 1.0
    scene sweethome_end_9 with dissolve
    gg 0 '诶？' with dissolve
    scene sweethome_end_10 with dissolve
    pause 1.6
    gg 0 '我在哪儿？'
    scene sweethome_end_11 with dissolve
    asami0 1 "哪儿都不是。字面意义上的。但重要的是，你和我在一起。" with Dissolve(0.3)
    show sweethome_end_12 with Dissolve(0.3)
    $ renpy.pause(3.9,hard=True)
    show sweethome_end_12_1 with Dissolve(0.3)
    asami0 1 "你可真让我好找。我差点没赶上你离开学校，否则还得找上好一阵子。" with Dissolve(0.3)
    pause 1.6
    gg 0 '（什么情况？）' with dissolve
    scene sweethome_end_13 with dissolve
    gg 0 "你到底是谁？我不认识你。"
    #scene sweethome_end_13 with dissolve
    scene sweethome_end_15 with vpunch
    asami0 1 "现在还不认识。但我已经认识你了。"
    scene sweethome_end_16 with dissolve
    gg 0 "什……你到底是谁？"
    scene sweethome_end_17 with dissolve
    asami0 1 "我叫[asami]。很高兴……再次见到你。"
    gg 0 "（「再次」？这是什么意思？）"
    show sweethome_end_18 with Dissolve(0.1)
    $ renpy.pause(3.5,hard=True)
    scene sweethome_end_19 with dissolve
    asami 1 "你刚搬来这里，对吧？我一直在等你。第一天就找到你，简直是走运。" with dissolve
    scene sweethome_end_20 with dissolve
    gg 0 "（这到底是在搞什么鬼？）"
    gg 0 "玩笑先放一边。我这是在哪儿？"
    scene sweethome_end_23 with dissolve
    asami 1 "哪儿都不是，我刚说了。不开玩笑。"
    
    scene sweethome_end_24 with dissolve
    gg 0 "……那好吧。又是个蠢梦。"
    scene sweethome_end_21 with dissolve
    asami 1 "很遗憾不是，虽然感觉起来确实很像。"

    
    scene sweethome_end_22 with dissolve
    asami 1 "说到这个——告诉我，[gg]，你最近有没有做一些奇怪又可怕的梦？"
    asami 1 "细节各不相同，但每次都以悲剧收场？"
    scene sweethome_end_23 with dissolve
    asami 1 "每次都像是在同一个地方。一遍又一遍。"
    scene sweethome_end_24 with dissolve
    gg 0 "你怎么知道这些？"
    stop music2 fadeout 3
    scene sweethome_end_25 with dissolve
    asami 1 "你现在还什么都不知道。该死的时间错位，快把人逼疯了。你得亲眼看看。"
    scene sweethome_end_26 with dissolve
    pause 1.6
    play sound dm3
    scene sweethome_end_27 with Dissolve(0.1)
    play music rain_street_01
    play music2 leaving_home_by_kevin_macleod fadein 8 volume 0.8
    pause 0.06
    show sweethome_end_28 with Dissolve(0.2)
    $ renpy.pause(13,hard=True)
    show sweethome_end_29 with Dissolve(0.6)
    gg 5 "（这怎么可能？……）" with Dissolve(0.3)
    gg 5 "我们这是在哪儿？"
    asami 2 "这里是你我初次相遇的地方。" with Dissolve(0.6)
    asami 2 "至少对我来说是这样。但你……我不知道你已经来过多少次了。"
    asami 2 "从那之后过了一年。大灾变之后一年。但我还记得每一件事，就像昨天一样。"
    asami 2 "对其他人来说，那个早晨很普通。对我来说，却莫名地不祥。但我当时还是希望一切照常进行。"
    asami 2 "先是下起瓢泼大雨，仿佛天空在警告我们。"
    asami 2 "接着整座城市被浓稠黏腻的雾吞没。到了傍晚，连呼吸都变得困难。空气仿佛在凝结，闷热得让人作呕。"
    show sweethome_end_30 with Dissolve(0.6)
    hide sweethome_end_29
    pause 0.6
    asami 2 "然后是一声可怕的响动。像是尖叫，也像是哀嚎——遥远，却又像是什么东西正从内部被撕开。" with Dissolve(0.6)
    asami 2 "有那么一瞬间，世界消失了。万物坠入黑暗。等光回来时——它展现的是真正的人间地狱。"
    asami 2 "整座城市被火焰吞没。大多数正过着日常的人毫无防备，瞬间丧生。"
    show sweethome_end_31 with Dissolve(0.6)
    hide sweethome_end_30
    pause 0.6
    asami 2 "但那还只是个开始。" with Dissolve(0.6)
    asami 2 "它们突然出现了。怪物。成百上千。"
    asami 2 "像烧焦的野狗，长着猩红的眼睛。它们像瘟疫一样涌上街头。"
    asami 2 "地铁、房屋、屋顶——到处都是。它们只做一件事：吞噬。不加区别，永不停歇。"
    show sweethome_end_32 with Dissolve(0.6)
    hide sweethome_end_31
    pause 0.6
    asami 2 "那一天永远烙在幸存者的记忆里。那一天，人类看清了自己究竟有多么无能为力。" with Dissolve(0.6)
    pause 1.0
    pause 0.6
    gg 5 "（这感觉很熟悉。）" with Dissolve(0.6)
    gg 5 "黑暗降临了……然后吞噬了所有人……"
    show sweethome_end_33 with Dissolve(0.6)
    hide sweethome_end_32
    gg 5 "没错……我以前每次醒来都会忘掉细节，但现在我全都想起来了！这就是我梦见的情景！" with Dissolve(0.6)
    gg 5 "所以这一切都是真的？！而且我还经历过这些？……"
    asami "其实不止一次。"
    show sweethome_end_29 with Dissolve(0.6)
    hide sweethome_end_33
    asami "而且在那之前，是我帮你挺过来的——我们一起战斗过。" with Dissolve(0.3)
    asami "所以我才在找你。"
    gg 5 "所以……既然我们现在是在未来……" with Dissolve(0.3)
    asami 2 "相对你而言，是的。" with Dissolve(0.3)
    asami 2 "准确地说，是比你现在往后两年。也就是你搬来这里的两年之后。"
    gg 5 "你是说我也会经历这场地狱？" with Dissolve(0.3)
    asami 2 "是的。大灾变还在一年之后，但导致它的一切，可能早就开始了。" with Dissolve(0.3)
    show sweethome_end_34 with Dissolve(0.6)
    hide sweethome_end_29
    gg 5 "{cps=5}……{/cps}"  with Dissolve(0.3)
    gg 5 "（我梦见过这座毁灭的城市。我在梦里见过[may]。）"
    gg 5 "等等！[may]怎么了？"
    show sweethome_end_29 with Dissolve(0.6)
    hide sweethome_end_34
    gg 5 "我必须知道！" with Dissolve(0.3)
    asami 2 "她死了。" with Dissolve(0.3)
    pause 1.0
    gg 5 "……我明白了。所以这一切都白费了。" with Dissolve(0.3)
    asami 2 "也不尽然。每一种结果都是我们今后可以利用的新经验。只是我们以前从没走到这一步。" with Dissolve(0.3)
    gg 5 "要阻止大灾变，我们该怎么做？" with Dissolve(0.3)
    asami 2 "恐怕那是不可能的。你自己也说过，这是无法阻止的转折点。" with Dissolve(0.3)
    asami 2 "但我们可以改变{cps=6}你的时间线。{/cps}"
    gg 5 "什么意思？" with Dissolve(0.3)
    asami 2 "你必须回去。" with Dissolve(0.3)
    gg 5 "这是不是说，我能救下[may]？" with Dissolve(0.3)
    asami 2 "你有一种特别的力量，[gg]。" with Dissolve(0.3)
    asami 2 "连我都不知道我们已经重温这一刻多少次了。但你有时间救下你身边的人。"
    show sweethome_end_34 with Dissolve(0.6)
    hide sweethome_end_29
    gg 5 "我要怎么做？" with Dissolve(0.3)
    gg 5 "我已经准备好付出一切了。"
    show sweethome_end_35 with Dissolve(0.1)
    hide sweethome_end_34
    $ renpy.pause(1,hard=True)
    show sweethome_end_36 with Dissolve(0.1)
    hide sweethome_end_35
    $ renpy.pause(5,hard=True)
    show sweethome_end_37 with Dissolve(0.1)
    hide sweethome_end_35
    asami 2 "我从不怀疑这一点。" with Dissolve(0.3)
    $ renpy.force_autosave()
    asami 2 "我们得立刻开始行动。" with Dissolve(0.3)
    gg 5 "那么，具体该怎么做？" with Dissolve(0.3)
    asami '{cps=6}找到我。{/cps}' with Dissolve(0.3)
    $ renpy.music.set_volume(1, delay=0, channel=u'music2')
    gg '什么？' with Dissolve(0.3)
    stop music fadeout 5
    show sweethome_end_38 with Dissolve(0.1)
    hide sweethome_end_37
    $ renpy.music.set_volume(0, delay=5, channel=u'music2')
    $ renpy.pause(5.1,hard=True)
    jump cdr_1