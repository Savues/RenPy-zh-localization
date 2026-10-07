label pls1:
    scene black
    with fadeb
    $ mc_name = renpy.input("请输入名字，直接回车则使用默认名。（弗林）")
    $ mc_name = mc_name.strip()
    if mc_name == "":
        $ mc_name = "Flynn"
    if mc_name in takenfirstnames:
        "（这个名字故事里别的角色也在用。不介意的话就继续，想换可以回退。）"
    scene black
    show magic_effect at theme_ember
    with fadeb
    play sfx "sfx/Chapter - In.ogg"
    show prologue as prologue_blur at text_glow
    show prologue
    with staticflow
    $ save_name = "序章"
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide prologue
    hide prologue_blur
    hide magic_effect
    with grunge
    pause 0.5
    scrn "十三年前……" with diss
    show pls1 1
    mc "爸爸，你能再给我讲一遍那个关于诸神与女神的故事吗？" with diss
    show pls1 2
    mcdad "又来？" with diss
    show pls1 3
    mcdad "你{i}每晚{/i}都想听那个故事。" with diss
    show pls1 4
    mc "因为它太精彩了啊！" with diss
    show pls1 5
    mcdad "那也是我最喜欢的故事之一。" with diss
    show pls1 3
    mcdad "好吧。" with diss
    mcdad "我再讲一遍给你听。"
    hide pls1 with diss
    pause 1.0
    mcdad "很久很久以前，这个世界和现在很不一样。" with diss
    mcdad "那是一个充满魔法与奇迹的世界，神明行走于凡人间。"
    play sfx "sfx/Whoosh.ogg"
    play bgm "bgm/Ancient Times.ogg" fadein 1.5
    pause 0.1
    show pls1 6
    mcdad "这些神明是强大的存在，统治着世界，赐予世人祝福与指引，陪伴他们一生。" with fadew
    mcdad "人们珍爱着自己的神明与女神，有些人甚至将毕生都献于侍奉祂们。"
    show pls1 7
    mcdad "然而，和大多数生灵一样，祂们并不完美，彼此之间也难以和睦相处。" with diss
    mcdad "祂们为了争夺对世界的掌控，不断相互征战。"
    play sfx "sfx/Slash.ogg"
    hide pls1
    pause 1.0
    show pls1 8
    mcdad "每一场这样的战争结束时，通常都只剩下一个胜者。" with dism
    play sfx "sfx/Divine Power Release.ogg"
    show pls1 9
    mcdad "然而，世界的天平永远无法真正被倾覆。" with diss
    mcdad "陨落者的疆土与信众皆可被人夺走，唯独祂的神力无法被另一位神明占有。"
    show pls1 10
    mcdad "命运绝不会允许这种事发生，而是将这份力量重新分给一种特殊的凡人——神裔。" with diss
    show pls1 11
    mcdad "神裔与其他凡人不同；他们天生与强大的魔法亲和，灵魂也远胜于普通凡人。" with diss
    mcdad "凭借这些特质，他们得以驾驭陨落者的神力，并最终借此飞升，跻身神明之列。"
    play sfx "sfx/Whoosh.ogg"
    show pls1 12
    mcdad "然而某一天，神裔们发现自己再也无法驾驭这份力量。" with diss
    mcdad "他们只眼睁睁看着它从指间消散。"
    show pls1 13
    mcdad "他们向最通晓魔法能量的贤者求助，希望这份力量仍能被驾驭。" with diss
    mcdad "然而他们所了解到的，比任何人所能预料的都更加糟糕。"
    show pls1 14
    mcdad "神力正在从这世上消退。" with diss
    mcdad "从那一天起，再也不会有新的神裔，因而也不会再诞生新的神明。"
    show pls1 15
    mcdad "这一真相，加上神明之间永无止境的战争，让世上的神明急剧减少，直到只剩下最后一位。" with diss
    show pls1 16
    play sfx "sfx/Footsteps - Cave.ogg"
    mcdad "在无力挽回这一切之后，最后一位神明决定以永世隐居作为惩罚，把祂的子民留在原地自寻活路。" with dism
    show pls1 17
    mcdad "由于极少有凡人能以魔法完成神明所为之事，他们只能被迫想出新的法子，去做那些昔日由神明代劳的事情。" with dism
    show pls1 18
    mcdad "他们发明了让作物丰收的肥料、建造巨型建筑的吊车与升降机、治愈疾病的药物，等等。" with disl
    mcdad "渐渐地，困苦消退了；随着时间流逝，神明只剩下一个遥远的传说。"
    stop bgm fadeout 3.0
    show pls1 19
    mc "嘿，爸爸？" with diss
    show pls1 20
    mc "你觉得神力还会回来吗？" with diss
    show pls1 21
    mcdad "我{i}确实{/i}这么认为，儿子。" with diss
    mcdad "大多数人不这么认为……"
    mcdad "他们说我傻，因为我相信；但我倒觉得他们才是傻子。"
    show pls1 22
    mcdad "神裔终将再次驾驭神力，你们给我记住。" with diss
    show pls1 23
    mcdad "到那时所有人都会明白我的研究是对的，我所发掘的预言都是{i}真的{/i}！" with diss
    mcdad "他们会看出从头到尾都对的是我，而{i}他们{/i}才是蠢货！"
    show pls1 24
    mcdad "然后……" with diss
    show pls1 25
    mcdad "对不起，儿子……" with diss
    mcdad "我太激动了。"
    show pls1 26
    mcdad "我只是受够了所有人拿我开玩笑、嘲笑我的种种理论。" with diss
    mcdad "哪怕是那些我能拿出证据支撑的理论。"
    show pls1 27
    mc "没关系的，爸爸。" with diss
    mc "我知道你一定能找到你想找的东西。"
    mc "到时候{i}你{/i}就可以笑{i}他们{/i}了。"
    show pls1 28
    mcdad "谢谢你，儿子。" with diss
    mcdad "至少还有你站在我这边。"
    play sfx "sfx/Cloth2.ogg"
    show pls1 29
    mcdad "我爱你。" with diss
    show pls1 30
    mc "我也爱你，爸爸！" with diss
    hide pls1 with diss
    pause 1.0
    jump pls2

label pls2:
    scene black
    scrn "十二年前……" with diss
    show pls2 1
    mcmom "什么？！" with hpunch
    mcmom "你不是认真的吧！"
    show pls2 2
    mcdad "最多也就一两年！" with diss
    mcdad "我还能经常回来探望你们。"
    show pls2 3
    mcmom "你知道我一直都支持你的事业，但这也太过分了！" with diss
    mcmom "我们还有一个儿子！"
    mcmom "一个爱死你的儿子！"
    show pls2 4
    mcmom "你让我怎么——" with diss
    show pls2 5 with diss
    pause 1.0
    show pls2 6
    mcdad "哦，[mc_name]。" with diss
    mcdad "这么晚了，你怎么还醒着？"
    show pls2 7
    mc "我睡不着……" with diss
    mc "我在想，你能不能再讲一遍我们最喜欢的那个故事……"
    show pls2 8
    mcdad "当然，儿子。" with diss
    mcdad "先上床睡觉，那个故事我就讲给你听。"
    hide pls2 with diss
    pause 1.0
    jump pls3

label pls3:
    scene black
    scrn "六年前……" with diss
    show pls3 1
    mc "妈妈！我回来了。" with diss
    mc "我放学回来了。"
    show pls3 2
    mcmom "今天过得怎么样？" with diss
    show pls3 3
    mc "老样子……" with diss
    show pls3 4
    mcmom "那几个孩子还在欺负你吗？" with diss
    show pls3 3
    mc "嗯，不过没事了。" with diss
    mc "莱拉和莎拉让我别理他们，说那样他们就会放过我。"
    mc "好像还真有点用。"
    pause 1.0
    mc "有爸爸的消息吗？" with diss
    show pls3 5
    mcmom "宝贝，你最好先坐下。" with diss
    play sfx "sfx/Chair Scoot2.ogg"
    show pls3 6
    mcmom "今天考古协会打电话来了……" with diss
    mcmom "你父亲的挖掘现场出了事故。"
    show pls3 7
    mc "他没事吧？！" with diss
    show pls3 8
    mcmom "他们还不清楚……" with diss
    show pls3 9
    mcmom "他、他们找到了你父亲队伍里几个人的遗体，但、但有、有几个——" with diss
    mcmom "{i}*抽泣*{/i}"
    show pls3 10
    mcmom "对不起……" with diss
    show pls3 11
    mcmom "有几个人始终没有找到……其中就包括你父亲。" with diss
    show pls3 12
    mc "也就是说，他可能还活着，对吧？" with diss
    show pls3 13
    mcmom "没、没有人听到过他的消息，而这、这一切也才发生几、几天。" with diss
    mcmom "最、最好的办法就是——{i}*抽泣*{/i}——按最、糟糕的情况来打算……"
    play sfx "sfx/Chair Scoot3.ogg"
    show pls3 14
    mc "不！" with hpunch
    mc "爸爸还在外面的某个地方！"
    mc "一定是的！"
    show pls3 15 with diss
    pause 1.0
    play sfx "sfx/Cloth2.ogg"
    show pls3 16
    mcmom "哦，孩子……" with diss
    mcmom "我也希望是这样……"
    hide pls3 with diss
    pause 1.0
    jump pls4

label pls4:
    scene black
    scrn "四年前……" with diss
    show pls4 1
    mc "妈妈，我要搬出去了。" with diss
    show pls4 2
    mcmom "什么？" with diss
    mcmom "为什么？"
    show pls4 3
    mc "我再也待不下去了。" with diss
    mc "我现在十九了，也找到了一份薪水不错的工作。"
    mc "所以我要用自己赚的钱租个住处。"
    show pls4 4
    mc "这里塞满了关于失去的一切的记忆……" with diss
    show pls4 5
    mcmom "我们可以一起找个新地方。" with diss
    show pls4 6
    mc "不……我想试着一个人生活。" with diss
    mc "谢谢你想着帮我，妈妈。"
    mc "真的。"
    mc "但这件事我已经决定了。"
    mc "我今天已经给那套公寓付了定金，随时可以搬进去。"
    show pls4 7
    mcmom "哦……我明白了。" with diss
    show pls4 5
    mcmom "有时候我都忘了你已经长大了。" with diss
    show pls4 6
    mc "我{i}早{/i}就长大了……" with diss
    show pls4 8
    mcmom "我知道……" with diss
    mcmom "只是你经历的事太多了。"
    show pls4 9
    mcmom "我想我也要搬到别处去。" with diss
    mcmom "也许搬到城市外围吧。"
    mcmom "这样我们离得不算太远，还能互相走动，你也不用再来这个老地方了。"
    show pls4 10
    mc "你不用这样。" with diss
    mc "我不介意回这房子看看。"
    mc "我只是再也{i}住{/i}不下去了。"
    show pls4 11
    mcmom "我知道我{i}不{/i}必这么做，但我想。" with diss
    mcmom "一年多前我就考虑过搬了，但你那时快毕业了，我就想着再等等。"
    show pls4 12
    mcmom "不过，我原本打算的是我们俩一起搬。" with diss
    mcmom "但这样也好！"
    mcmom "我为你骄傲得不能再骄傲。"
    show pls4 13
    mc "谢谢，妈妈。" with diss
    mc "我先去收拾一些东西。"
    mc "我爱你！"
    show pls4 5
    mcmom "我也爱你，儿子。" with diss
    stop bgm fadeout 3.0
    hide pls4 with diss
    pause 1.0
    jump c1p1s1

label c1p1s1:
    scene black
    show magic_effect at theme_ember
    with fadeb
    play sfx "sfx/Chapter - In.ogg"
    show c1p1 as c1p1_blur at text_glow
    show c1p1
    with staticflow
    $ save_name = "第1-1章：事故"
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide c1p1
    hide c1p1_blur
    hide magic_effect
    with grunge
    pause 0.5
    scrn "现在……" with diss
    play bgm "bgm/Office Music.ogg" fadein 1.5
    play bgs "bgs/Office Sounds.ogg" fadein 1.0
    show c1p1s1 1
    mc "（今天真是慢得要命。）" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    mc "（真等不及要离开这里了。）"
    layl "[mc_name]，又在发呆啊。"
    show c1p1s1 2
    layl "你不是还有活没干完吗？" with diss
    show c1p1s1 3
    $ CharacterProfile.unlock_profile([chara["layl"]])
    mc "该做的我都做完了，还多做了一些，但不到下班时间我不能走。" with diss
    show c1p1s1 4
    layl "你其实可以让我提前放你走啊。" with diss
    layl "我自己也差不多要提前打卡了。"
    show c1p1s1 3
    mc "我知道可以，可我真的需要这最后几分钟。" with diss
    mc "最近我手头很紧，不把最后整整一个小时干完，那段就不给钱。"
    show c1p1s1 5
    layl "好吧，明白了。" with diss
    layl "不过你干活是真的好，我可以帮你申请加薪。"
    show c1p1s1 6
    mc "你不用这样。" with diss
    mc "大家都知道你是我朋友，这样别人会议论你的。"
    show c1p1s1 7
    layl "你不是认真的吧。" with diss
    layl "你干活的量和质量摆在那里。"
    layl "我觉得你早就该加薪了。"
    show c1p1s1 3
    mc "既然你真要提，那我就不推辞了。" with diss
    mc "谢了，莱拉。"
    show c1p1s1 4
    layl "先别谢我！" with diss
    layl "我可不保证什么。"
    show c1p1s1 5
    layl "总之，你快下班了。" with diss
    layl "我在楼下等你，然后我们去吃晚饭怎么样？"
    layl "我全包。"
    show c1p1s1 6
    mc "好啊，我没意见。" with diss
    show c1p1s1 8
    layl "太好了！我等你。" with diss
    stop bgs fadeout 1.0
    hide c1p1s1 with diss
    pause 1.0
    jump c1p1s2

label c1p1s2:
    scene black
    show c1p1s2 1
    mc "（终于从那张该死的办公桌前解脱了。）" with diss
    show c1p1s2 2
    mc "莱拉，不好意思让你久等了。" with diss
    mc "准备好走了吗？"
    show c1p1s2 3
    layl "没事，我在大厅里翻了会儿杂志。" with diss
    layl "你要是走了我就走。"
    show c1p1s2 2
    mc "嗯，我已经打好卡了。" with diss
    show c1p1s2 3
    layl "太好了！" with diss
    layl "想到哪儿吃了吗？"
    show c1p1s2 2
    mc "没。" with diss
    mc "你请客，我又不挑食，随你定。"
    show c1p1s2 3
    layl "好吧，那我就不说了。" with diss
    layl "等到了你就知道啦！"
    show c1p1s2 4
    mc "天哪，我等下肯定会后悔吧？" with diss
    layl "希望不会！"
    hide c1p1s2 with diss
    stop bgm fadeout 3.0
    pause 1.0
    jump c1p1s3

label c1p1s3:
    scene black
    play bgs "bgs/Parking Garage.ogg" fadein 1.0
    show c1p1s3 1
    layl "所以你还没买车？" with diss
    show c1p1s3 2
    mc "还没。" with diss
    show c1p1s3 3
    play sfx "sfx/Car - Beep.ogg"
    layl "行，那你就坐我的车。" with diss
    show c1p1s3 4
    mc "哇哦！" with diss
    mc "不用开公司的车了？"
    mc "这辆美人儿你从哪弄来的？"
    show c1p1s3 5
    layl "那是我爸十几岁时的车。" with diss
    layl "刚拿到手没多久他就撞得很惨，但怎么都不肯放手。"
    layl "上个月他发现我开公司的车，气得不行，把它送去翻新，然后——瞧！"
    layl "它现在跑起来像只小猫一样顺！"
    show c1p1s3 6
    play sfx "sfx/Car - Door Open.ogg"
    layl "那么，吃什么去？" with diss
    layl "真等不及让你感受一下它在街上飞驰的样子！"
    stop bgs fadeout 1.0
    show c1p1s3 7
    play sfx "sfx/Car - Door Close.ogg"
    mc "天，连内饰都这么棒。" with diss
    show c1p1s3 8
    layl "是吧！" with diss
    layl "自从拿到车，我就一直近乎强迫症地把它里里外外擦得一尘不染。"
    show c1p1s3 9
    mc "换我也会这样。" with diss
    show c1p1s3 10
    play sfx "sfx/Car - Start.ogg"
    layl "我知道你会的。好了，出发吧！" with diss
    hide c1p1s3
    scrn "吃完饭回家的路上……" with diss
    jump c1p1s4

label c1p1s4:
    scene black
    show c1p1s4 1
    play bgs "bgs/Car - Drive.ogg" volume 0.75 fadein 1.0
    mc "又让你破费了，莱拉，这比我本来打算吃的微波卷饼好太多了。" with diss
    show c1p1s4 2
    layl "没什么。" with diss
    layl "我今天挺开心的。"
    show c1p1s4 1
    mc "我也是。" with diss
    show c1p1s4 3
    layl "话说，现在我有自己的车了，要是我们的班次能对上，我可以顺路送你上下班。" with diss
    show c1p1s4 4
    mc "不用这么麻烦，不过你愿意的话，我也没意见。" with diss
    show c1p1s4 5
    layl "当然！" with diss
    layl "反正我去上班也要经过你家门口。"
    show c1p1s4 6
    mc "莱拉，小心！" with diss
    play sfx "sfx/Divine Power Whoosh.ogg"
    show c1p1s4 7 with diss
    pause 1.0
    play sfx "sfx/Astral - Blow.ogg"
    play sfx2 "sfx/Car - Screech.ogg"
    hide c1p1s4
    stop bgs fadeout 1.0 fadeout 1.0
    pause 3.0
    show c1p1s4 8
    layl "[mc_name]。" with diss
    hide c1p1s4 with diss
    pause 1.0
    show c1p1s4 9
    layl "[mc_name]！" with diss
    hide c1p1s4 with diss
    pause 1.0
    show c1p1s4 10
    layl "快起来……" with diss
    layl "起来！"
    hide c1p1s4 with diss
    pause 1.0
    jump c1p2s1

label c1p2s1:
    scene black
    show magic_effect at theme_ember
    with fadeb
    play sfx "sfx/Chapter - In.ogg"
    show c1p2 as c1p2_blur at text_glow
    show c1p2
    with staticflow
    $ save_name = "第1-2章：觉醒"
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide c1p2
    hide c1p2_blur
    hide magic_effect
    with grunge
    pause 0.5
    play bgm "bgm/Light Tragedy.ogg" fadein 1.5
    show c1p2s1 1 with diss
    play bgs "bgs/Hospital.ogg"  fadein 1.0
    $ CharacterProfile.unlock_outfit([(chara["mc"], 1)])
    pause 0.2
    show c1p2s1 2
    mc "（呃，头好疼。）" with diss
    show c1p2s1 3
    mc "（医院？！）" with diss
    mc "（发生了什么？）"
    show c1p2s1 4
    $ CharacterProfile.unlock_outfit([(chara["layl"], 1)])
    mc "（嗯？）" with diss
    mc "（莱拉没有单独病房，也穿着便装。）"
    mc "（她没事就好。）"
    mc "嘘，莱拉。"
    pause 1.0
    mc "莱拉，醒醒。" with diss
    show c1p2s1 5 with diss
    pause 1.0
    show c1p2s1 6
    layl "嘿，你醒了……" with diss
    show c1p2s1 7 with diss
    pause 1.0
    show c1p2s1 8
    layl "你醒了！" with diss
    play sfx "sfx/Hug Excited.ogg"
    show c1p2s1 9
    layl "我一直担心死了！" with diss
    play sfx "sfx/Hug Excited Back.ogg"
    show c1p2s1 10 with diss
    pause 1.0
    play sfx "sfx/Hug Excited Release.ogg"
    show c1p2s1 11
    layl "感觉怎么样？" with diss
    show c1p2s1 12
    mc "我脑袋感觉像被卡车撞了一样。" with diss
    play sfx "sfx/Footsteps - Tile.ogg"
    show c1p2s1 13
    layl "我去给你叫医生。" with diss
    show c1p2s1 14
    layl "我马上回来。" with diss
    show c1p2s1 15
    play sfx "sfx/Door - Sliding.ogg"
    mc "（我完全搞不清状况。）" with diss
    mc "（我们明明没出车祸，可我却躺在医院病床上。）"
    mc "（莱拉毫发无损，说明出事的只有我。）"
    show c1p2s1 16
    mc "（我身上看不出有伤。）" with diss
    mc "（就只有这个要命的头疼。）"
    play sfx "sfx/Door - Sliding.ogg"
    pause 1.0
    show c1p2s1 17
    chri "你好，[mc_name]，我是克里斯汀。" with dism
    $ CharacterProfile.unlock_profile([chara["chri"]])
    play sfx "sfx/Door - Sliding.ogg"
    show c1p2s1 17c with diss
    pause 1.0
    play sfx "sfx/Footsteps - Tile.ogg"
    show c1p2s1 17d
    chri "我是这两个月一直照看你的医生。" with diss
    show c1p2s1 18
    stop bgm
    play sfx "sfx/Stinger - Gloom.ogg"
    mc "（不可能吧……）" with diss
    mc "（我肯定听错了。）"
    show c1p2s1 19
    mc "不好意思，我好像听错了。" with diss
    mc "你刚才说的是两个月？"
    show c1p2s1 20
    chri "对，你没听错，你昏迷了两个月。" with diss
    show c1p2s1 19
    mc "谁能跟我解释一下到底发生了什么？" with diss
    show c1p2s1 20
    chri "我的猜测是，你遭遇了某种浓缩魔法能量的骤增。" with diss
    chri "迄今为止，这件事的影响还不清楚。"
    chri "没人能解释你为什么会昏迷，更奇怪的是，你体内现在有巨量的魔法能量。"
    show c1p2s1 19
    mc "那是什么意思？" with diss
    mc "等等……我成法师了？"
    play sfx "sfx/Slap.ogg" volume 0.25
    show c1p2s1 21
    stop bgm
    chri "呃，不是。" with diss
    chri "不是这么运作的。"
    show c1p2s1 22
    play bgm "bgm/Light Tragedy.ogg" fadein 1.5
    mc "该死。" with diss
    show c1p2s1 23
    layl "你从两个月的昏迷中醒来，发现自己体内塞满了魔力……" with diss
    layl "……而你在担心的居然{i}是这个{/i}？！"
    show c1p2s1 24
    layl "我怎么会指望别的呢？" with diss
    show c1p2s1 25
    mc "我现在实在想不出别的了；再说了，我还想让你别摆出那副伤心的表情。" with diss
    show c1p2s1 26
    chri "你该想的是自己的身体，想怎么好起来。" with diss
    show c1p2s1 27
    layl "同意。" with diss
    show c1p2s1 28
    chri "话说，之前也有过几例魔法能量滞留在人体内的情况，不过通常只出现在长期接触高浓度魔能的人身上。" with diss
    chri "那种情况下你只会像感冒一样病一场，身体把它扛过去就没事了。"
    chri "但你的情况是，体内的魔力水平似乎还在上升，而你的身体看起来并没有在抵抗。"
    chri "我要再留你观察几天，监测你的身体状况。"
    chri "不过现在，我就让你们单独待一会儿吧。"
    play sfx "sfx/Footsteps - Tile.ogg" volume 0.75
    show c1p2s1 29
    mc "谢谢你，克里斯汀。" with diss
    play sfx "sfx/Door - Sliding.ogg"
    show c1p2s1 30
    layl "对不起没告诉你昏迷的事，我怕你刚醒就受刺激。" with diss
    show c1p2s1 31
    mc "你不用为这个道歉，莱拉，我完全理解。" with diss
    mc "我倒觉得挺巧的，我醒来的那天你正好在。"
    play sfx "sfx/Cloth2.ogg"
    show c1p2s1 32
    layl "其实从出事那天起，我每天都来。" with diss
    layl "一下班我就直奔这里，希望你已经醒了。"
    show c1p2s1 32b
    layl "说到上班，还有件事我一直没告诉你……" with diss
    show c1p2s1 32c
    layl "卢米奈特已经找到人顶替你了。" with diss
    show c1p2s1 33
    mc "那他们可倒霉了。" with diss
    mc "他们不知道自己失去了什么。"
    mc "再说了，那种地方本来也不适合我。"
    show c1p2s1 34
    layl "嗯，我知道，不过我会想念和你一起上班的。" with diss
    show c1p2s1 35
    mc "不过我们还是可以一起玩。你在这儿干等着我醒来，浪费了那么多时间，我可欠你不少！" with diss
    show c1p2s1 34
    layl "我倒不是有什么意见，只是你不必补偿我。" with diss
    layl "那是我自己的选择。"
    show c1p2s1 35
    mc "我很庆幸有人这么在乎我。" with diss
    mc "每次我最需要的时候，你都在。"
    show c1p2s1 36
    layl "当然！" with diss
    layl "这一点也永远不会变。"
    layl "你也是我{i}最{/i}好的朋友啊。"
    layl "又不是我一个人在付出。"
    show c1p2s1 37
    mc "嗯，我知道。" with diss
    mc "谢谢你这么常来看我！"
    mc "真不敢想，要是我醒来时你不在，我会糊涂成什么样。"
    show c1p2s1 38
    layl "不用谢我。" with diss
    layl "我做这种事不是为了被人记住或感谢，是因为我在乎。"
    show c1p2s1 39
    layl "不过探视时间快结束了，我大概该走了。" with diss
    layl "我明天再来看你。"
    layl "再见，[mc_name]！"
    show c1p2s1 40
    mc "回见，莱拉！" with diss
    stop bgs fadeout 1.0
    stop bgm fadeout 3.0
    hide c1p2s1
    jump c1p2s2

label c1p2s2:
    scene black
    scrn "几天后……" with diss
    show c1p2s2 1
    play bgm "bgm/New Day.ogg" fadein 1.5
    play sfx "sfx/Treadmill Loop.ogg" loop
    mc "（目前为止，应该还算顺利。）" with diss
    mc "（我体内的魔力还在不断增长，但我感觉很好，所有健康检查也都通过了。）"
    stop sfx fadeout 1.0
    show c1p2s2 2
    mc "（呼——！）" with diss
    mc "（明明我平时不怎么爱动，现在却好像能一直走下去，不过今天就先这样吧。）"
    show c1p2s2 3 with diss
    pause 1.0
    show c1p2s2 4 with diss
    pause 1.0
    show c1p2s2 5 with diss
    pause 1.0
    show c1p2s2 6
    mc "哦，早上好，克里斯汀！" with diss
    mc "我没注意到有人进来。"
    show c1p2s2 7
    chri "咦——什——呃……" with diss
    show c1p2s2 8
    chri "呃——早、早上好！" with diss
    chri "抱歉，被你吓了一跳。"
    chri "我知道你会趁这里没别人的清早活动，所以过来看看你。"
    show c1p2s2 9
    chri "今天感觉怎么样？" with diss
    show c1p2s2 10
    mc "说实话，好得不能再好！" with diss
    mc "从第二天起我就再没偏过头，身体也感觉更有力气了。"
    show c1p2s2 11
    chri "（小声）你看起来确实结实多了。" with diss
    show c1p2s2 12
    mc "抱歉，你刚说什么？" with diss
    mc "平板把你刚才的话盖过去了。"
    show c1p2s2 9
    chri "哦，呃，你感觉好些了真是太好了！" with diss
    show c1p2s2 10
    mc "嗯。" with diss
    mc "我敢肯定不是那个，不过还是谢了。"
    mc "我觉得我现在可以回家了，不过还是让专业的人来判断吧。"
    show c1p2s2 13
    chri "嗯，你大部分指标都在平均以上。" with diss
    show c1p2s2 9
    chri "只要你答应按时来做常规检查，我今天就能给你办出院手续。" with diss
    show c1p2s2 10
    mc "我当然会。" with diss
    mc "我保证。"
    show c1p2s2 9
    chri "我们还要做最后一项检查，然后就可以开始办出院手续了。" with diss
    chri "我们去检验室把这项检查做完，如何？"
    show c1p2s2 10
    stop bgm fadeout 3.0
    mc "等一下……" with diss
    mc "你感觉到了吗？"
    show c1p2s2 9
    chri "感觉到什么？" with diss
    show c1p2s2 10
    mc "我也说不清，空气里像是有什么电流一样。" with diss
    show c1p2s2 15
    chri "我什么都没感觉到。" with diss
    chri "也许这是种新症状——"
    show c1p2s2 16 with diss
    pause 1.0
    show c1p2s2 17
    play sfx "sfx/Magic Power Surge.ogg"
    mc "呃啊！" with hpunch
    show c1p2s2 18
    chri "搞什么鬼？！" with diss
    show c1p2s2 19
    mc "（大口喘气）那……真要命……" with diss
    show c1p2s2 20
    mc "感觉身体同时被火烧和电击一样。" with diss
    show c1p2s2 21
    chri "呃，刚才发生了什么？！" with diss
    show c1p2s2 22
    chri "必须马上把你送去检验室！" with diss
    hide c1p2s2 with diss
    pause 1.0
    jump c1p2s3

label c1p2s3:
    scene black
    play bgs "bgs/Hospital.ogg" fadein 1.0
    play bgm "bgm/Light Tragedy.ogg" fadein 1.5
    pause 1.0
    show c1p2s3 1 with diss
    pause 1.0
    show c1p2s3 2
    chri "搞什么？！" with diss
    chri "我从没见过这种情况！"
    show c1p2s3 3
    chri "我要分析一下这份样本，看看能查到什么。" with diss
    show c1p2s3 4
    chri "哪儿也别去！" with diss
    show c1p2s3 5
    mc "放心，不得到答案我是不会走的。" with diss
    show c1p2s3 6
    chri "很好。" with diss
    chri "我一会儿就回来。"
    show c1p2s3 7
    mc "（我到底是怎么了？）" with diss
    show c1p2s3 8
    mc "（我该给莱拉打个电话，告诉她发生了什么。）" with diss
    hide c1p2s3
    scrn "你刚跟莱拉通完电话不久，克里斯汀就回来了。" with diss
    show c1p2s3 17
    chri "嘿，[mc_name]，我回来了。" with diss
    show c1p2s3 18
    chri "我有个相当有意思的发现。" with diss
    chri "你体内的魔法似乎在细胞层面和你的血液结合了。"
    chri "从字面意义上说，魔法正在你的血管里流淌。"
    show c1p2s3 19
    mc "这是好事还是坏事？" with diss
    show c1p2s3 18
    chri "嗯，考虑到你之前那场魔力爆发，我只能说这是坏事。" with diss
    chri "不过不知怎么的，它似乎并没有伤害你。"
    chri "现在要判断这会给你带来什么后果还太早。"
    chri "所以只能走着看了。"
    chri "另外还有一个问题，和你的状况无关。"
    show c1p2s3 19
    mc "什么问题？" with diss
    show c1p2s3 18
    chri "显然，今天有人看到了你那点小{i}爆发{/i}，所以有位守望者过来问话。" with diss
    show c1p2s3 19
    mc "守望者在找我？！" with diss
    show c1p2s3 20
    chri "{i}*叹气*{/i}……对。" with diss
    show c1p2s3 21
    chri "其中一位就在病房外面。" with diss
    chri "她说问话时不许我在场。"
    chri "所以我走之后，你尽量保持冷静，老实回答她的问题。"
    hide c1p2s3 with diss
    pause 1.0
    play sfx "sfx/Footsteps - Tile.ogg"
    show c1p2s3 22a with diss
    pause 1.0
    show c1p2s3 22d
    stop bgm fadeout 3.0
    $ CharacterProfile.unlock_profile([chara["vero"]])
    vero "你好，[mc_name]，我是维罗妮卡。" with diss
    vero "我隶属守望者团。"
    vero "我们接到报告，说你身上有某种魔法装置发生了爆炸。"
    vero "我来跟进这件事。"
    show c1p2s3 23
    mc "没有什么魔法装置，是我。" with diss
    show c1p2s3 24
    vero "你？" with diss
    show c1p2s3 23
    mc "对，是我。" with diss
    show c1p2s3 22d
    vero "好吧……既然你不愿意坦白配合，我就只能把你拘留了。" with diss
    show c1p2s3 23
    mc "这就是坦白。" with diss
    mc "几个月前我被某种魔法能量击中，现在它正在淹没我的身体。"
    mc "我不知道它为什么会像你说的那样{i}「爆炸」{/i}，但这就是事实。"
    mc "问我的医生吧，她会给你作证。"
    show c1p2s3 25
    vero "问题就在这儿，我已经跟她谈过了。" with diss
    vero "我觉得她是在替你撒谎。"
    show c1p2s3 26
    vero "你得明白，你说的这些听起来根本——" with diss
    play sfx "sfx/Pen Drops.ogg"
    pause 1.0
    show c1p2s3 27
    unkn "哎呀！" with dism
    unkn "抱歉，我不是有意打断的。"
    play bgm "bgm/Astara Battle Theme.ogg" fadein 1.5
    play sfx "sfx/Footsteps - Tile.ogg"
    show c1p2s3 28
    vero "这是守望者的事务，女士！" with diss
    vero "你现在必须报上身份！"
    show c1p2s3 29
    unkn "你再这么跟我说话，我就让你{i}见识{/i}一下什么叫后悔。" with diss
    show c1p2s3 30
    vero "是吗？" with diss
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p2s3 31 with hpunch
    pause 0.5
    show c1p2s3 32
    unkn "原来你想这么玩，嗯？" with diss
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p2s3 33 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Kick - Miss.ogg"
    show c1p2s3 34 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Punch - Hit.ogg"
    show c1p2s3 35 with hpunch
    pause 0.5
    show c1p2s3 36
    unkn "冲脸去的。" with diss
    unkn "真的？"
    unkn "祝你第二次也能这么好运。"
    play sfx2 "sfx/Astral - Warp.ogg"
    show c1p2s3 37 with hpunch
    pause 0.5
    show c1p2s3 38
    unkn "过来吧，小甜心。" with diss
    play sfx2 "sfx/Astral - Warp.ogg"
    show c1p2s3 39 with hpunch
    pause 0.5
    show c1p2s3 40
    vero "你是怎么做到的？！" with diss
    show c1p2s3 41
    unkn "我可以解释，但你不会懂的。" with diss
    unkn "你们这些心胸狭窄的守望者从来都听不懂。"
    stop bgm fadeout 1.0
    play sfx "sfx/Astral - Charge.ogg"
    show c1p2s3 42
    unkn "那我就直接让你看好了！" with hpunch
    play sfx2 "sfx/Astral - Blow.ogg"
    hide c1p2s3
    pause 3.0
    show c1p2s3 43
    mc "刚才发生了什么？" with diss
    show c1p2s3 44
    unkn "你就是这样道谢的？" with diss
    unkn "算了，我们得离开这里。"
    show c1p2s3 45 with diss
    pause 0.5
    play sfx "sfx/Asta Finger Snap.ogg"
    play sfx2 "sfx/Astral - Portal.ogg"
    show c1p2s3 46 with diss
    pause 0.5
    show c1p2s3 47
    mc "你是谁？" with diss
    show c1p2s3 48
    unkn "现在没时间说这个。" with diss
    unkn "走，快走。"
    play sfx "sfx/Astral - Warp.ogg"
    show c1p2s3 49 with diss
    pause 1.0
    show c1p2s3 50
    mc "（嗯，这事看起来挺可疑……）" with diss
    mc "（……不过那个守望者不会一直躺着。）"
    mc "（管他的，就用传送门！）"
    play sfx "sfx/Astral - Warp.ogg"
    show c1p2s3 51 with diss
    pause 1.0
    show c1p2s3 52 with diss
    pause 1.0
    show c1p2s3 53
    chri "[mc_name]！" with diss
    chri "附近的护士说这里面发生了巨大的爆炸声。"
    chri "你不会又爆发了一次吧？"
    show c1p2s3 54
    chri "[mc_name]？" with diss
    show c1p2s3 55
    chri "{i}*倒吸一口气*{/i}！" with diss
    play sfx "sfx/Footsteps - Tile - Fast.ogg"
    show c1p2s3 56 with dism
    chri "你没事吧？！" with diss
    chri "发生了什么？！"
    show c1p2s3 57
    vero "我没事。" with diss
    show c1p2s3 58
    vero "但你的朋友和他的同伙可就不会没事了！" with diss
    play sfx2 "sfx/Footsteps - Tile.ogg"
    show c1p2s3 59
    chri "同伙？" with diss
    chri "可没有别人进来过——"
    play sfx "sfx/Door Slam.ogg"
    show c1p2s3 60 with diss
    pause 1.0
    show c1p2s3 61
    chri "（她说的{i}同伙{/i}是指谁？）" with diss
    stop bgs fadeout 1.0
    hide c1p2s3 with diss
    jump c1p3s1
    
label c1p3s1:
    scene black
    show magic_effect at theme_ember
    with fadeb
    play sfx "sfx/Chapter - In.ogg"
    show c1p3 as c1p3_blur at text_glow
    show c1p3
    with staticflow
    $ save_name = "第1-3章：真相"
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide c1p3
    hide c1p3_blur
    hide magic_effect
    with grunge
    pause 0.5
    play bgm "bgm/Legends of Old.ogg" fadein 1.5
    play bgs "bgs/Skyscraper.ogg" fadein 1.0
    play sfx2 "sfx/Astral - Warp.ogg"
    show c1p3s1 1 with diss
    pause 1.0
    play sfx2 "sfx/Astral - Portal.ogg"
    show c1p3s1 2 with diss
    pause 1.0
    show c1p3s1 3
    mc "现在，你能告诉我你是怎么做到的吗？" with diss
    show c1p3s1 4
    unkn "守望者是很好下手的对象。" with diss
    unkn "只要把他们激怒，就能很轻松地放倒。"
    unkn "那是因为你被训练成在战斗中发泄怒火，而不是保持冷静。"
    show c1p3s1 5
    mc "我不是这个意思。" with diss
    show c1p3s1 6
    unkn "哦，你是说我的魔法……" with diss
    show c1p3s1 5
    mc "没错，我就是说魔法！" with diss
    mc "我见过法师施展法术，那远远超出普通魔法的范畴！"
    play sfx "sfx/Astral - Simple.ogg"
    show c1p3s1 7
    unkn "可不是嘛。" with diss
    unkn "感觉也很了不得。"
    play sfx "sfx/Astral - Fade.ogg"
    show c1p3s1 8
    unkn "等你学会控制自己的力量就知道了。" with diss
    show c1p3s1 5
    mc "学会控制{i}我的{/i}力量？" with diss
    mc "你在说什么，而且你到底是谁？"
    show c1p3s1 8
    $ CharacterProfile.unlock_profile([chara["asta"]])
    asta "我叫阿斯塔拉，这几天一直在追踪你的能量源。" with diss
    show c1p3s1 5
    mc "你一直在跟踪我？！" with diss
    show c1p3s1 8
    asta "我只是循着你的气息而已，说跟踪太夸张了。" with diss
    show c1p3s1 9
    asta "你体内有着{i}巨量{/i}的魔法能量。" with diss
    asta "比我见过的任何人都多，甚至比我自己的还多。"
    show c1p3s1 5
    mc "你说的{i}其他人{/i}是什么意思？" with diss
    show c1p3s1 10
    asta "唉。" with diss
    asta "看来我得给你解释清楚。"
    play sfx "sfx/Footsteps - Concrete.ogg"
    show c1p3s1 11
    asta "我们坐下来说吧，我试着把一切都讲明白。" with diss
    show c1p3s1 12
    asta "你熟悉古代那些关于神明与神力的传说吗？" with diss
    show c1p3s1 13
    mc "当然，我小时候特别迷这些故事。" with diss
    mc "我爸爸坚信神力总有一天会回来。"
    mc "他当时其实正在研究这方面的预言，后来他……去世了。"
    show c1p3s1 12
    asta "嗯，你爸爸是对的……" with diss
    asta "{i}我们是神裔{/i}，我和世界各地许多其他神裔一样，神力在我们体内奔流。"
    $ profile_filters.append(("Scions", "Scions"))
    show c1p3s1 13
    mc "得了吧。" with diss
    mc "你把我想得有多蠢？"
    mc "我们也许有{i}某种{/i}魔力，但你说那是神力，未免太疯了。"
    show c1p3s1 14
    asta "你这家伙真是混蛋！" with diss
    show c1p3s1 15
    mc "你不能就这样闯进我的生活，宣称我是神裔，然后告诉我我有神力。" with diss
    mc "你真以为我会毫无证据就相信这种事？"
    show c1p3s1 16
    asta "行，你要证据？" with diss
    show c1p3s1 17
    mc "你要干什——" with diss
    stop bgm fadeout 1.0
    show c1p3s1 18 with diss
    pause 0.2
    play sfx2 "sfx/Whoosh.ogg"
    show c1p3s1 19 with diss
    pause 0.5
    play sfx "sfx/Falling Wind.ogg" loop
    show c1p3s1 20
    mc "{shader=jitter}糟了！{/shader}" with diss
    show c1p3s1 21 with diss
    pause 0.2
    hide c1p3s1 with diss
    stop sfx fadeout 1.5
    play sfx2 "sfx/Body - Drop.ogg"
    pause 2.0
    show c1p3s1 22
    mc "（什么？！）" with diss
    show c1p3s1 23
    mc "（我怎么没死？！）" with diss
    play sfx "sfx/Whoosh.ogg"
    show c1p3s1 24 with diss
    pause 0.01
    play sfx2 "sfx/Jump - Landing.ogg"
    show c1p3s1 25 with diss
    pause 0.5
    show c1p3s1 26
    asta "这样的证据够吗？" with diss
    show c1p3s1 27
    mc "你疯了吗？！" with diss
    mc "你差点把我杀了！"
    show c1p3s1 28
    asta "相信我，要杀死神裔可比这难多了。" with diss
    show c1p3s1 27
    mc "你{i}就是{/i}疯了。" with diss
    show c1p3s1 28
    asta "你还没回答我的问题。" with diss
    asta "现在你信了吗？"
    show c1p3s1 27
    mc "我不知道该信什么。" with diss
    mc "我的确跟别人不一样，而且一直都不一样，但这不代表是因为我有神力。"
    show c1p3s1 29
    asta "唉，随便吧。" with diss
    show c1p3s1 30
    asta "我们不该在外面抛头露面。" with diss
    asta "守望者会来找我们的。"
    show c1p3s1 31
    mc "顺便说一句，谢了。" with diss
    mc "要是没有你突然冒出来把事情弄得更复杂，我肯定好好的。"
    show c1p3s1 32
    asta "随你怎么说。" with diss
    asta "我有个地方可以躲一阵子，我们待多久都行。"
    asta "你愿意跟我走吗？"
    show c1p3s1 31
    mc "我好像也没什么选择。" with diss
    mc "我要是回家，肯定会被逮捕。"
    stop bgs fadeout 1.0
    hide c1p3s1
    scrn "阿斯塔拉又开出一个传送门，你不情不愿地穿了过去。" with diss
    pause 1.0
    jump c1p3s2

label c1p3s2:
    scene black
    play bgm "bgm/Astara's Home.ogg" fadein 1.5
    show c1p3s2 1
    asta "这里是我家！" with diss
    asta "随便坐，别客气。"
    show c1p3s2 2
    mc "我没想到你会把我带到你自己家。" with diss
    show c1p3s2 3
    asta "嗯，这里很隐蔽，守望者找不到我们。" with diss
    show c1p3s2 2
    mc "那就好，我可一点也不想再跟她们打交道了。" with diss
    show c1p3s2 3
    asta "嗯，我也一样。" with diss
    asta "想吃点什么、想喝点什么，自己随便拿。"
    asta "别因为你人在我家，我就要端茶倒水、事事伺候。"
    show c1p3s2 2
    mc "好吧……" with diss
    mc "那我看来是求不到足部按摩了。"
    show c1p3s2 4
    asta "噫，我可不想碰你那双臭脚！" with diss
    asta "你连鞋袜都不穿就在外面乱跑！"
    show c1p3s2 5
    mc "你也知道医院对病人无菌着装有多严格。" with diss
    mc "我哪有时间跑回储物柜拿鞋。"
    mc "再说了，只是开玩笑而已。"
    show c1p3s2 6
    asta "说到衣服，我给你拿几件我爸的，你好换掉这身难看的医院服。" with diss
    asta "我敢肯定他的衣服你能穿。"
    show c1p3s2 7
    mc "你爸的衣服？" with diss
    mc "你爸爸也住这儿吗？"
    show c1p3s2 8
    asta "不……他不……" with diss
    asta "我马上回来。"
    show c1p3s2 9
    mc "（刚才有点尴尬。）" with diss
    mc "（我提到她父亲时，她看起来很难过。）"
    show c1p3s2 10
    asta "给，去试试。" with diss
    asta "洗手间在你右手边。"
    play sfx "sfx/Door - Sliding2.ogg"
    show c1p3s2 11
    mc "（真希望合身。）" with diss
    mc "（医院的衣服太难受了。）"
    play sfx "sfx/Cloth.ogg"
    show c1p3s2 12 with diss
    pause 1.0
    play sfx "sfx/Door - Sliding2.ogg"
    show c1p3s2 13
    stop bgm fadeout 3.0
    asta "嘿，我忘了说，你——" with diss
    show c1p3s2 14 with diss
    pause 1.0
    play sfx "sfx/Door - Sliding - Slam.ogg" volume 1.5
    show c1p3s2 16
    asta "{b}{shader=jitter}我的天啊！{/shader}{/b}" with hpunch
    asta "我没想到你已经开始换衣服了！"
    show c1p3s2 15
    mc "{i}*隔着门说*{/i} 没事，我真希望医院别对衣着管得那么严。" with diss
    mc "{i}*隔着门说*{/i} 要真是那样，我就穿内裤出来了。"
    show c1p3s2 16
    asta "是啊，内裤挺好。" with diss
    play sfx "sfx/Slap.ogg" volume 0.25
    show c1p3s2 17
    asta "（内裤挺好？）" with diss
    asta "（真的？！）"
    asta "（阿斯塔拉，你就不能接句更俏皮的话吗？）"
    asta "（说得好像你没看过阴茎似的。）"
    show c1p3s2 18
    asta "（不过你{i}那种{/i}可没见过。）" with diss
    play sfx2 "sfx/Door - Sliding2.ogg"
    show c1p3s2 19
    $ CharacterProfile.unlock_outfit([(chara["mc"], 2)])
    mc "我觉得挺合身的。" with diss
    hide c1p3s2 with diss
    pause 1.0
    play bgm "bgm/Astara's Home.ogg" fadein 1.5
    show c1p3s2 20
    mc "再多跟我说说这股力量吧。" with diss
    show c1p3s2 21
    asta "哦？" with diss
    asta "你开始相信我了？"
    show c1p3s2 22
    mc "我还不完全确定，但你说的这些显然有些是真的。" with diss
    mc "希望你还知道些没告诉我的事，能帮我把一切串起来。"
    show c1p3s2 21a
    asta "知道了。" with diss
    asta "你特别想知道哪方面的事？"
    show c1p3s2 22
    mc "你怎么知道我们的力量是神力？" with diss
    mc "我的意思是，我们也可能只是某种超强法师。"
    show c1p3s2 23
    asta "超强法师？" with diss
    asta "真的？"
    show c1p3s2 21a
    asta "回答你的问题：我知道，因为我曾经和我这份力量原本所属的神明说过话。" with diss
    show c1p3s2 22
    mc "开玩笑吧？" with diss
    mc "你是说你的力量是神直接赐给你的？"
    show c1p3s2 21a
    asta "{i}女神{/i}，而且不是那样的。" with diss
    asta "如果传说是真的，那旧日诸神里只剩一位还活着，而且早已把自己藏了起来。"
    asta "她既然已经死了，我自然没当面跟她说过话，但她偶尔会在梦里和我交谈。"
    asta "我相信原本拥有你这份力量的神明，很快就会来找你。"
    show c1p3s2 22
    mc "所以你梦见了一位已死的女神，就足以让你相信自己是继承神力的神裔了？" with diss
    show c1p3s2 21a
    asta "对，差不多吧。" with diss
    asta "你得留意自己的梦，老兄。"
    asta "向潜意识敞开内心，能揭示很多你原本永远不会知道或理解的事。"
    show c1p3s2 22
    mc "你这么说吧，不过我好像从来没做过梦。" with diss
    mc "我睡觉从来不做梦。"
    show c1p3s2 21a
    asta "人人都会做梦，只是大多数人醒来记不住。" with diss
    asta "你大概也是这样。"
    show c1p3s2 22
    mc "这话说得可能有道理。" with diss
    show c1p3s2 23
    asta "嘿，你看！" with diss
    asta "你居然没有直接反对我说的话。"
    asta "有进步了！"
    show c1p3s2 22
    mc "我得为自己辩解一句：你不打招呼就冒出来，为了点破事把一个守望者打了一顿，然后告诉我我是神裔，还把我从楼上推了下去。" with diss
    mc "所以我很难信任你，还请见谅。"
    show c1p3s2 24
    asta "是是是，你说得对。" with diss
    asta "事情变成这样，我真的很抱歉。"
    asta "我本来完全没打算这样跟你打招呼的。"
    show c1p3s2 25
    mc "你本可以等那个守望者走了再动手。" with diss
    show c1p3s2 25a 1
    asta "我知道……" with diss
    asta "我只是不想在我还没机会跟你谈这些之前，就让她把你关起来。"
    show c1p3s2 22
    mc "你觉得她没有任何实证也能把我扣下吗？" with diss
    show c1p3s2 21a
    asta "我觉得她肯定会试。" with diss
    asta "守望者总在背地里干些见不得光的事。"
    show c1p3s2 22
    mc "真的？" with diss
    mc "我可从没听说她们做过什么天怒人怨的事。"
    show c1p3s2 21a
    asta "你也永远别想再见到。" with diss
    asta "她们表面功夫做得很足，但越往上面走，腐败就越严重。"
    show c1p3s2 22
    mc "这不奇怪。" with diss
    mc "说到底，她们也不过是另一家企业。"
    mc "不管打着什么维和的旗号，里面估计也全是贪腐的人。"
    show c1p3s2 21a
    asta "没错，一个不落。" with diss
    show c1p3s2 26
    asta "总之，我还有点事要处理。" with diss
    asta "你要是愿意可以在这儿过夜，这沙发睡起来还不赖。"
    asta "我大概天亮才能回来。"
    show c1p3s2 27
    mc "你要出去？" with diss
    mc "你不怕被抓到？"
    show c1p3s2 28
    asta "不，不太担心。" with diss
    show c1p3s2 29
    asta "回见！" with diss
    play sfx "sfx/Door.ogg"
    show c1p3s2 30
    mc "（在陌生人家里睡觉，感觉怪怪的。）" with diss
    mc "（我有一大堆事要想，也许会整夜不睡去理清这一切。）"
    stop bgm fadeout 3.0
    hide c1p3s2 with diss
    pause 1.0
    show c1p3s2 31
    mc "{i}*打哈欠*{/i}" with diss
    show c1p3s2 32
    mc "（天，好累。）" with diss
    mc "（睡一小会儿应该没关系。）"
    show c1p3s2 33 with dism
    pause 1.0
    hide c1p3s2 with disl
    pause 1.0
    call primordial1 from _call_primordial1
    show c1p3s2 34
    mc "{i}*猛地惊醒*{/i}" with hpunch
    show c1p3s2 35
    $ CharacterProfile.unlock_outfit([(chara["asta"], 1)])
    asta "哇哦！" with diss
    asta "你没事吧？"
    show c1p3s2 36
    mc "没事，我只是做了个特别奇怪的梦。" with diss
    show c1p3s2 37
    asta "先生，{i}「我不做梦」{/i}的人，做梦了？" with diss
    asta "早饭快好了，边吃边跟我说说吧。"
    hide c1p3s2 with diss
    pause 1.0
    play bgm "bgm/Astara's Home.ogg" fadein 1.5
    show c1p3s2 38
    asta "所以你身处某个诡异的地方，魔力被强化了，然后有{i}某个异域的东西{/i}用你听不懂的语言对你说话？" with diss
    show c1p3s2 39
    asta "我解梦一向很在行，但这个我一点头绪都没有。" with diss
    show c1p3s2 40
    mc "可你昨天不是说，在你之前拥有这份力量的神明会在梦里造访你吗？" with diss
    show c1p3s2 39
    asta "嗯，是这样，但神明曾经也都是凡人，所以看起来跟普通人一样。" with diss
    show c1p3s2 40
    mc "你不觉得那是神明在接触我吗？" with diss
    show c1p3s2 41
    asta "我的意思是，确实有可能，但听起来实在太离谱了。" with diss
    asta "尤其是它用某种陌生语言说话那部分——你本来应该听得懂的。"
    show c1p3s2 40
    mc "偏偏就发生在你昨天说完那些话之后，实在太巧了。" with diss
    show c1p3s2 39
    asta "这点我同意。" with diss
    asta "要是你再梦到一次，就能知道是不是神明了，不过现在先别太担心。"
    asta "我是不是可以认为你现在信我了？"
    show c1p3s2 40
    mc "这个还不好说。" with diss
    mc "不过我确实慢慢被你说服了。"
    play sfx2 "sfx/Cloth.ogg" volume 0.25
    show c1p3s2 42
    asta "那我就却之不恭了。" with diss
    play sfx "sfx/Dishes.ogg"
    show c1p3s2 43 with diss
    pause 1.0
    play sfx2 "sfx/Door - Knock.ogg"
    pause 1.0
    show c1p3s2 44 with diss
    pause 1.0
    play sfx "sfx/Door - Open.ogg"
    show c1p3s2 45
    unkn "都办妥了。" with diss
    unkn "守望者撤销了对你们、还有那个[mc_name]的全部指控。"
    asta "谢谢你告诉我。" with diss
    asta "祝你今天愉快。"
    unkn "你也是，阿斯塔拉。" with diss
    play sfx "sfx/Door.ogg"
    show c1p3s2 46
    mc "我没听错吧？" with diss
    mc "守望者撤销了对我们的全部指控？"
    show c1p3s2 47
    asta "没错！" with diss
    asta "也就是说，你现在可以回家了。"
    show c1p3s2 46
    mc "所以你昨晚就是在做这些？" with diss
    show c1p3s2 48
    asta "也许吧。" with diss
    asta "就算真是，我也不会告诉你。"
    show c1p3s2 46
    mc "如果真是那样，那就谢谢你了。" with diss
    show c1p3s2 47
    asta "不客气。" with diss
    show c1p3s2 46
    mc "既然这样，我就换回病号服，把衣服还回医院，然后去取我的东西。" with diss
    mc "抱歉这么突然就走，我手机落在那儿了。"
    mc "还有一样对我很重要的东西。"
    show c1p3s2 49
    asta "完全理解。" with diss
    asta "不用道歉，昨天把事情搞砸的是我。"
    hide c1p3s2 with diss
    pause 1.0
    play sfx2 "sfx/Door - Sliding2.ogg"
    show c1p3s2 50
    mc "你爸的衣服我放在洗手台上了。" with diss
    mc "我这就走。"
    mc "谢谢你的早饭！"
    show c1p3s2 51
    asta "不客气！" with diss
    asta "我很快再来找你。"
    show c1p3s2 52
    mc "{i}*开玩笑地说*{/i} 好吧，跟踪狂。" with diss
    mc "再见！"
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    hide c1p3s2 with diss
    pause 1.0
    jump c1p3s3

label c1p3s3:
    scene black
    play bgm "bgm/New Day.ogg" fadein 1.5
    play bgs "bgs/Hospital.ogg" fadein 1.0
    show c1p3s3 1 with diss
    pause 0.5
    mc "（终于不用被守望者追着跑，也能把东西取回来了。）" with diss
    show c1p3s3 2
    mc "打扰一下，请问克里斯汀今天在吗？" with diss
    mc "我住院期间她是我的主治医生。"
    show c1p3s3 3
    nurs "我不确定，不过我可以帮你查一下。" with diss
    play sfx "sfx/Keyboard - Type.ogg"
    show c1p3s3 4 with diss
    pause 1.0
    nurs "那不奇怪。" with diss
    show c1p3s3 3
    nurs "她在，先生。" with diss
    nurs "要我帮您呼叫她吗？"
    show c1p3s3 2
    mc "好的，麻烦你。" with diss
    play sfx "sfx/Keyboard - Type.ogg"
    show c1p3s3 4
    nurs "好的。" with diss
    show c1p3s3 3
    nurs "她一会儿就过来。" with diss
    nurs "您可以先坐下等她。"
    show c1p3s3 2
    mc "谢谢。" with diss
    hide c1p3s3 with diss
    pause 1.0
    show c1p3s3 5
    chri "[mc_name]！" with diss
    show c1p3s3 6
    chri "见到你真是太高兴了！" with diss
    show c1p3s3 7
    chri "到底发生了什么？！" with diss
    chri "你跑哪儿去了？"
    show c1p3s3 8
    mc "说来话长。" with diss
    mc "有没有安静点的地方可以谈？"
    show c1p3s3 7
    chri "当然，跟我来。" with diss
    hide c1p3s3
    scrn "你跟着克里斯汀来到她的办公室，把发生的经过说了一遍。" with diss
    show c1p3s3 9
    chri "这信息量真够大的。" with diss
    show c1p3s3 10
    mc "是啊，尤其是她说我们两个都是神裔。" with diss
    mc "说实话，我开始相信她了。"
    show c1p3s3 9
    chri "嗯，那倒是能解释我血检的结果。" with diss
    show c1p3s3 10
    mc "什么意思？" with diss
    show c1p3s3 11
    chri "你消失之后，我重新核对了结果，发现有些地方对不上……" with diss
    chri "你血液里的标记物和我第一次取样（你昏迷时）的不一样。"
    chri "这说明你的细胞正在快速演变。"
    show c1p3s3 12
    chri "如果这种血液变化遍布你的所有器官，那你几乎已经不能算人了。" with diss
    show c1p3s3 13
    mc "不是吧？" with diss
    mc "有办法逆转吗？"
    show c1p3s3 14
    chri "逆转？！" with diss
    chri "你疯了吗？！"
    show c1p3s3 13
    mc "怎么了？" with diss
    mc "我才不想当什么神裔，管我现在是什么。"
    mc "在所有可能得到神力的人里，我偏偏是最不配的那个。"
    show c1p3s3 15
    chri "就算我想逆转，我也不知道怎么做。" with diss
    chri "那就好比让我想办法关掉重力或者让时间静止。"
    show c1p3s3 13
    mc "所以我就只能这样了？" with diss
    show c1p3s3 16
    chri "是啊，命运决定送你一份礼物。" with diss
    chri "你该好好接纳它！"
    chri "换我有过那种力量，绝不会抱怨。"
    chri "想想你能用它做多少好事。"
    show c1p3s3 13
    mc "是啊，但那不是我。" with diss
    mc "我不是童话里那种英雄，这种事我连从哪儿开始都不知道。"
    show c1p3s3 15
    chri "你可以从学会控制现在的力量开始。" with diss
    chri "也许你可以再找到阿斯塔拉，请她教你怎么使用。"
    show c1p3s3 13
    mc "大概吧，我也不知道……" with diss
    mc "我真希望被选中的换成随便哪个别人都好。"
    mc "我连正常的生活都还没摸索明白。"
    mc "我怎么可能摸得清神的生活？"
    show c1p3s3 15
    chri "我的建议是，一步一步来。" with diss
    chri "你不必一次就想清楚。"
    play sfx "sfx/Bag - Rustle.ogg"
    show c1p3s3 17
    chri "哦，我差点忘了！" with diss
    chri "你落在这儿的东西我全都收好了，替你保管着。"
    chri "莱拉也给你带了新衣服。"
    play sfx "sfx/Bag - Place.ogg"
    show c1p3s3 18
    chri "给你。" with diss
    chri "你的东西都在里面。"
    show c1p3s3 19
    mc "谢谢你，克里斯汀。" with diss
    show c1p3s3 20
    chri "不客气！" with diss
    chri "你去换衣服，我在这儿等你。"
    hide c1p3s3 with diss
    pause 0.5
    show c1p3s3 20a1
    mc "求你了，一定要告诉我莱拉发现了我口袋里的东西，特意给我留在这儿……" with diss
    show c1p3s3 20a2
    mc "呼……果然……" with diss
    show c1p3s3 20a3
    mc "要是不在这儿我肯定会难过。" with diss
    hide c1p3s3 with diss
    pause 0.5
    show c1p3s3 21
    $ CharacterProfile.unlock_outfit([(chara["mc"], 3)])
    mc "这样舒服多了！" with diss
    mc "恕我直言，那身病号服烂透了。"
    show c1p3s3 22
    chri "那已经是兼顾舒适度和无菌标准了。" with diss
    show c1p3s3 23
    chri "但确实很烂。" with diss
    show c1p3s3 24
    chri "东西拿到了，你想赶紧走了吧。" with diss
    show c1p3s3 25
    mc "嗯，我大概该走了，莱拉肯定急坏了。" with diss
    show c1p3s3 26
    chri "哦对了！" with diss
    chri "你突然消失的时候，她{i}真的{/i}慌得不行。"
    chri "她让我告诉你，要是来取东西就给她打电话。"
    show c1p3s3 25
    mc "我想我还是直接去看她吧。" with diss
    mc "发生的事太多了，电话里说不清楚。"
    show c1p3s3 24
    chri "那大概是个好主意。" with diss
    chri "那我们先到这儿吧。"
    show c1p3s3 25
    mc "再见，克里斯汀。" with diss
    show c1p3s3 27
    chri "哦等等！" with diss
    chri "我忘了把电话号码给你。"
    chri "有什么事就打给我。"
    show c1p3s3 28
    mc "谢谢，克里斯汀，我会的！" with diss
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    hide c1p3s3 with diss
    pause 1.0
    jump c1p3s4

label c1p3s4:
    scene black
    show c1p3s4 1
    mc "（到了。）" with diss
    mc "（希望莱拉今天没在上班。）"
    play sfx "sfx/Door - Knock.ogg"
    show c1p3s4 2 with diss
    pause 1.0
    play sfx2 "sfx/Door - Open.ogg"
    play bgm "bgm/The Calm.ogg" fadein 1.5
    show c1p3s4 3
    $ CharacterProfile.unlock_outfit([(chara["layl"], 3)])
    layl "[mc_name]？！" with diss
    play sfx2 "sfx/Cloth2.ogg"
    show c1p3s4 4
    layl "谢天谢地你没事！" with hpunch
    layl "我一直担心死了。"
    show c1p3s4 5
    mc "我没事，莱拉，抱歉让你担心了。" with diss
    show c1p3s4 6
    layl "进来吧，你可得好好解释一下。" with diss
    play sfx2 "sfx/Door.ogg"
    show c1p3s4 7
    $ CharacterProfile.unlock_profile([chara["layldad"]])
    layldad "嘿，[mc_name]，好久不见！" with diss
    show c1p3s4 8
    mc "嘿，韦克斯特罗斯先生！" with diss
    mc "抱歉好久没来串门了。"
    mc "最近我生活里发生了很多事。"
    show c1p3s4 9
    layldad "我听说了！" with diss
    layldad "好像是魔力中毒外加昏迷两个月，对吧？"
    show c1p3s4 10
    mc "要真是那样就好了。" with diss
    show c1p3s4 9
    layldad "我很想留下来听完全部经过，但我开会要迟到了。" with diss
    show c1p3s4 11
    layldad "也许之后莱拉会把这事从头给老头子讲一遍。" with diss
    show c1p3s4 12
    layl "当然，爸爸！" with diss
    layl "祝你会顺利。"
    show c1p3s4 13
    layldad "谢谢，宝贝！" with diss
    show c1p3s4 14
    $ CharacterProfile.unlock_profile([chara["laylmom"]])
    laylmom "回家路上别忘了去趟商店！" with diss
    laylmom "今晚做菜真的需要那些番茄。"
    show c1p3s4 15
    layldad "不会忘的，亲爱的，我保证。" with diss
    show c1p3s4 16 with diss
    pause 1.0
    show c1p3s4 17
    layldad "大家下午愉快！" with diss
    show c1p3s4 18
    layl "你也是，爸爸！" with diss
    mc "谢谢，你也是。"
    laylmom "再见啦，我爱你！"
    show c1p3s4 19
    layldad "我也爱你，宝贝！" with diss
    play sfx "sfx/Door.ogg"
    show c1p3s4 20 with diss
    pause 0.5
    show c1p3s4 21
    laylmom "[mc_name]，你要待一会儿吗？" with diss
    laylmom "我做饭的时候可以给你多盛一份。"
    show c1p3s4 22
    mc "我可能待不了那么久，但还是谢谢你。" with diss
    show c1p3s4 23
    layl "什么？！" with diss
    layl "你就这样突然消失，现在连饭都不肯留下来吃了？"
    show c1p3s4 24
    mc "那件事真的很抱歉。" with diss
    mc "等我把一切解释清楚，你就明白了。"
    show c1p3s4 23
    layl "不行，你不接受我妈妈的晚饭邀请，我就不肯体谅你。" with diss
    show c1p3s4 25
    laylmom "哦，宝贝，别这样嘛。" with diss
    laylmom "他留不下，那就留不下吧。"
    laylmom "你不该逼他。"
    show c1p3s4 26
    layl "可是妈妈！" with diss
    layl "我跟您说过他遭遇的事了吧？"
    show c1p3s4 25
    laylmom "是啊，宝贝，你说过。" with diss
    show c1p3s4 26
    layl "那您就该明白，我只是担心他，想让他多待一会儿。" with diss
    $ choice1 = ChoiceOption(
            "留下来吃晚饭。",
            stats={"layl": {"affection": 5}},
            path_info=("layl", "Story Scene")
        )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            $ layldinner = True
            show c1p3s4 27
            mc "好吧，你赢了，我留下来吃晚饭。" with diss
            show c1p3s4 28
            layl "太好啦！" with diss
            layl "谢谢！"
        "不留下来。":
            show c1p3s4 27
            mc "对不起，莱拉，我真的不能留下。" with diss
            show c1p3s4 29
            layl "行，但你最好有个足够好的理由。" with diss
    show c1p3s4 30
    laylmom "我去院子里干会儿活。" with diss
    laylmom "需要我就喊我。"
    show c1p3s4 31
    layl "好的，妈妈。" with diss
    show c1p3s4 32
    layl "走，去我房间，你好好解释一下。" with diss
    hide c1p3s4 with diss
    pause 0.5
    jump c1p3s5

label c1p3s5:
    scene black
    show c1p3s5 1
    layl "现在给我说清楚医院里发生了什么。" with diss
    layl "克里斯汀说你直接消失了，还把一个守望者打晕在地。"
    show c1p3s5 2
    mc "嗯，这么说也不算错。" with diss
    mc "我当时在医院的活动区，发生了某种魔力爆发。"
    show c1p3s5 3
    mc "于是克里斯汀带我去抽血，接着一个守望者冲进来盘问我，以为那是炸弹……" with diss
    stop bgm fadeout 3.0
    show c1p3s5 4
    mc "然后不知从哪儿冒出来一个女人，直接跟那守望者打了起来！" with diss
    play bgm "bgm/UhOh.ogg" fadein 1.5
    show c1p3s5 5
    layl "（糟了！）" with diss
    layl "（我漏掉了？！）"
    mc "她用我从没见过的魔法打赢了，然后开出一个传送门，说我必须跟她走。"
    mc "所以我就穿了过去。"
    show c1p3s5 6
    layl "嗯哼，继续，我在听。" with diss
    show c1p3s5 7
    layl "（希望他还没发现。）" with diss
    layl "（要是我动作够快够小心，也许能趁他滔滔不绝的时候溜过去藏好。）"
    show c1p3s5 8
    layl "（他还背对着我吗？）" with diss
    layl "（好，他确实是。）"
    show c1p3s5 9
    layl "（太好了！）" with diss
    layl "（成功了。）"
    play sfx "sfx/Swipe.ogg"
    show c1p3s5 10
    mc "到目前为止你还跟得上吗？" with hpunch
    show c1p3s5 11
    layl "跟得上！" with diss
    layl "当然！"
    show c1p3s5 12
    mc "然后她告诉我我是神裔——" with diss
    show c1p3s5 13
    layl "（操，操，操！）" with diss
    layl "（我他妈到底要把它藏哪儿？！）"
    show c1p3s5 14
    mc "那个疯女人居然直接把我从楼上踢了下去，跟没事人一样！" with diss
    show c1p3s5 15
    layl "她做了什么？！" with hpunch
    show c1p3s5 16
    mc "她把我踢——" with diss
    stop bgm fadeout 3.0
    show c1p3s5 17 with diss
    pause 1.0
    show c1p3s5 18 with diss
    pause 1.0
    show c1p3s5 19
    layl "（可恶！）" with diss
    show c1p3s5 20
    layl "（任务失败……）" with diss
    show c1p3s5 21
    mc "呃，你在拿{i}那个{/i}……做什么？" with diss
    show c1p3s5 22
    layl "我把它放在书桌上了……" with diss
    layl "我没指望会有人来，压根没想过要收起来。"
    show c1p3s5 23
    mc "嗯哼……" with diss
    mc "我这就——呃——转过去把话说完。"
    mc "对，我正在这么做。"
    mc "我刚说到哪儿了？"
    hide c1p3s5 with diss
    play bgm "bgm/The Calm.ogg" fadein 1.5
    pause 0.5
    show c1p3s5 24
    layl "哇，所以那个阿斯塔拉和克里斯汀都觉得你可能是神裔？" with diss
    layl "听起来完全像胡说八道，老兄。"
    show c1p3s5 25
    mc "一开始我也这么想，但现在我基本确定她们是对的。" with diss
    show c1p3s5 24
    layl "为什么这么说？" with diss
    show c1p3s5 25
    mc "发生了这么多事，想否认也越来越难了。" with diss
    show c1p3s5 24
    layl "嗯，好像还真是。" with diss
    show c1p3s5 25
    mc "那你觉得呢？" with diss
    mc "相信她们的是不是显得我很蠢？"
    show c1p3s5 26
    layl "我可没这么说。" with diss
    layl "你现在真的拥有神力了吗？你试过用吗？"
    show c1p3s5 27
    mc "说来奇怪，我还真没试过。" with diss
    mc "要不要试一下？"
    show c1p3s5 28
    layl "对，这个我必须看！" with diss
    show c1p3s5 29
    mc "好啊，不过要是什么都做不到，你可别笑我。" with diss
    show c1p3s5 30
    layl "我尽量！" with diss
    show c1p3s5 31
    mc "那就开始了……" with diss
    show c1p3s5 32 with diss
    pause 1.0
    show c1p3s5 33
    mc "好像什么也没发生。" with diss
    show c1p3s5 34
    layl "放轻松，清空杂念，把注意力放在你自己的能量上。" with diss
    layl "你可以的。"
    show c1p3s5 35
    mc "放松……" with diss
    mc "清空杂念……"
    mc "专注于自己的能量。"
    pause 1.0
    play bgs "bgs/Primordial - Glow.ogg"
    show c1p3s5 36
    mc "还是没——" with diss
    show c1p3s5 37 with diss
    pause 1.0
    stop bgs fadeout 1.0
    show c1p3s5 38 with diss
    pause 1.0
    show c1p3s5 39
    layl "这绝对不是普通的魔法。" with diss
    layl "你{i}真的{/i}可能是神裔。"
    show c1p3s5 40
    mc "我不知道，可如果我真有神力，我刚才试的应该会成功才对。" with diss
    show c1p3s5 41
    layl "什么意思？" with diss
    layl "它成功了啊！"
    show c1p3s5 40
    mc "不，没有成功。" with diss
    mc "我刚才想的是变出一百万颗水晶，让我们发财。"
    show c1p3s5 42
    layl "天哪，真的吗？" with diss
    layl "你脑子里冒出来的东西，永远都会让我吃惊。"
    layl "你会先想着发财，倒也说得通。"
    show c1p3s5 43
    layl "还好你没试着让我衣服消失什么的。" with diss
    show c1p3s5 40
    mc "喂，我不是变态好吗！" with diss
    mc "别忘了，用震动棒用得那么勤、以至于就那么扔在桌上凉着的人是你。"
    show c1p3s5 44
    layl "你非要在这种时候提醒我吗？" with diss
    layl "我差点就忘了这茬。"
    show c1p3s5 45
    mc "{i}*笑出声*{/i} 抱歉，你这辈子都别想摆脱这件事了。" with diss
    show c1p3s5 44
    layl "太好了。" with diss
    show c1p3s5 46
    layl "我好像听见爸爸回来了，就先下楼了。" with diss
    show c1p3s5 47
    layl "你敢在我爸妈面前提震动棒的事试试。" with diss
    show c1p3s5 48
    mc "不会的，放心。" with diss
    hide c1p3s5 with diss
    pause 1.0
    jump c1p3s6

label c1p3s6:
    scene black
    show c1p3s6 1
    layl "嘿爸爸，我好像听见你回来了！" with diss
    layl "会议怎么样？"
    show c1p3s6 2
    $ CharacterProfile.unlock_outfit([(chara["layldad"], 1)])
    layldad "很顺利，亲爱的！" with diss
    show c1p3s6 3
    layldad "我看见[mc_name]也还在。" with diss
    layldad "你留下来吃晚饭吗？"
    layldad "我想差不多快好了。"
    if layldinner:
        show c1p3s6 4
        mc "嗯，莱拉说服我留下了。" with diss
        show c1p3s6 5
        layldad "太好了！" with diss
        layldad "就像你们小时候那样，每个周五晚上都过来跟我们一起吃饭。"
        stop bgm fadeout 3.0
        hide c1p3s6 with diss
        pause 1.0
        call laylfamdinner from _call_laylfamdinner
    else:
        show c1p3s6 4
        mc "不了先生，我还有点事要处理。" with diss
        show c1p3s6 3
        layldad "哦没关系，那就下次吧。" with diss
        show c1p3s6 6
        mc "既然说到这个，我得走了，莱拉。" with diss
        show c1p3s6 7
        layl "好吧。" with diss
        layl "路上小心。"
        show c1p3s6 6
        mc "我会的。" with diss
        mc "替我跟你妈妈说再见。"
        show c1p3s6 7
        layl "我会的。" with diss
        layl "再见，[mc_name]。"
        show c1p3s6 6
        mc "再见。" with diss
        show c1p3s6 8
        mc "再见，韦克斯特罗斯先生！" with diss
        show c1p3s6 9
        layldad "[mc_name]，晚上愉快！" with diss
        hide c1p3s6 with diss
        pause 1.0
    jump c1p3s7

label c1p3s7:
    scene black
    show c1p3s7 1
    $ CharacterProfile.unlock_outfit([(chara["mc"], 4)])
    mc "（真是漫长的一天。）" with diss
    mc "（一方面我想直接倒下就睡，可另一方面我又想多了解一些我现在拥有的力量。）"
    mc "（我想试着冥想看看有没有用。）"
    show c1p3s7 2 with diss
    pause 1.0
    hide c1p3s7 with diss
    pause 1.0
    play bgs "bgs/Primordial - Glow.ogg"
    show c1p3s7 2a
    mc "（我都坐了多久了？）" with diss
    mc "（一个小时吧……还是两个小时？）"
    mc "（不过我好像开始和血液里的能量建立联系了。）"
    show c1p3s7 3
    mc "（糟了！）" with diss
    play sfx "sfx/MC Magic - SemiControlled Surge.ogg"
    pause 3.0
    stop bgs fadeout 1.0
    show c1p3s7 4 with diss
    pause 0.5
    show c1p3s7 5
    mc "（呃……糟。）" with diss
    mc "（好吧，没电了确实也没别的事可做。）"
    mc "（我还是直接睡吧。）"
    hide c1p3s7 with diss
    pause 1.0
    play bgm "bgm/New Day.ogg" fadein 1.5
    play sfx "sfx/Door - Knock.ogg"
    show c1p3s7 6 with diss
    pause 1.0
    show c1p3s7 7
    mc "（这大晚上的，谁会来敲我的门？）" with diss
    play sfx "sfx/Door - Knock.ogg"
    pause 1.0
    show c1p3s7 8
    mc "等一下！" with diss
    play sfx "sfx/Door - Open.ogg"
    show c1p3s7 9
    asta "天哪，你看起来像是刚睡醒！" with diss
    show c1p3s7 10
    asta "我没吵醒你吧？" with diss
    show c1p3s7 11
    mc "嗯，不过没关系。" with diss
    mc "反正我也该起来了。"
    mc "我猜{i}跟踪狂{/i}知道我住哪儿，我不该惊讶？"
    show c1p3s7 12
    asta "我说过会再来找你的。" with diss
    asta "而且你昨晚释放的那股巨大能量，也让我很容易就找到你了。"
    asta "真不敢相信你把整个电网都弄停了。"
    show c1p3s7 13
    mc "{i}整个{/i}电网？" with diss
    show c1p3s7 14
    asta "对。" with diss
    asta "整张网都废了，老兄。"
    asta "现在一整片街区都没电！"
    show c1p3s7 13
    mc "哦，哇。" with diss
    mc "嗯，那是意外。"
    mc "我在试着学会更好地控制力量。"
    show c1p3s7 15
    asta "那你运气不错！" with diss
    asta "我就是为了这个来的。"
    asta "有个人我想让你见见。"
    show c1p3s7 13
    mc "谁？" with diss
    show c1p3s7 15
    asta "他是我朋友，也是教我魔法在人体内如何运作的人。" with diss
    show c1p3s7 16
    asta "那就走吧！" with diss
    asta "你随便收拾一下，我们就走！"
    hide c1p3s7 with diss
    pause 1.0
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    jump c1p4s1
    
label c1p4s1:
    scene black
    show magic_effect at theme_ember
    with fadeb
    play sfx "sfx/Chapter - In.ogg"
    show c1p4 as c1p4_blur at text_glow
    show c1p4
    with staticflow
    $ save_name = "第1-4章：试炼"
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide c1p4
    hide c1p4_blur
    hide magic_effect
    with grunge
    pause 0.5
    play bgm "bgm/Fitness.ogg" fadein 1.5
    play bgs "bgs/Gym.ogg" fadein 1.0
    show c1p4s1 1
    asta "就在这儿等着。" with diss
    asta "我去把这家店的老板叫来。"
    show c1p4s1 2
    mc "（这个地方真不错。）" with diss
    mc "（不知道在这儿训练要多少钱。）"
    show c1p4s1 3 with diss
    pause 1.0
    show c1p4s1 4
    $ CharacterProfile.unlock_profile([chara["sila"]])
    sila "不会吧！" with diss
    sila "[mc_name]？！"
    sila "快过来，兄弟！"
    show c1p4s1 5
    mc "塞拉斯？！" with diss
    mc "这也太巧了吧？"
    show c1p4s1 6
    asta "你们认识？" with diss
    show c1p4s1 7
    mc "认识。" with diss
    mc "塞拉斯以前是我的防身术教练。"
    mc "虽然那都是很久以前的事了。"
    show c1p4s1 8
    sila "这位[mc_name]，曾是我最出色的学员之一。" with diss
    sila "当然，那是在他取消我的课之前。"
    show c1p4s1 9
    mc "那件事我很抱歉。" with diss
    mc "我成年了，得去工作，就再也挤不出时间了。"
    show c1p4s1 10
    sila "没事，兄弟。" with diss
    sila "「生命不息」，我总这么说。"
    sila "我还真想过把它当健身房的标语，后来还是算了。"
    show c1p4s1 11
    asta "这下介绍环节可以省掉了。" with diss
    asta "塞拉斯，[mc_name]就是我跟你说过的那个新神裔。"
    asta "那个体内有着超乎寻常的魔法能量的人。"
    show c1p4s1 12
    sila "你是认真的？" with diss
    sila "小[mc_name]是神裔？"
    sila "而且不光是神裔，还是{i}那种{/i}神裔？"
    show c1p4s1 13
    asta "对，千真万确。" with diss
    asta "我们得把他调教出来。"
    asta "以他现在的状态，就算有那些力量，任何一个三流神裔都能把他当早餐吃掉。"
    show c1p4s1 14
    mc "喂！" with diss
    show c1p4s1 15
    sila "嗯，既然这样，我觉得暂时还不该让他跟我练。" with diss
    show c1p4s1 16
    sila "嘿，雷恩！" with diss
    sila "我给你带了个新猎物！"
    show c1p4s1 18
    $ CharacterProfile.unlock_profile([chara["rayn"]])
    rayn "他看起来没什么了不起。" with diss
    rayn "我们不是说好，你只把{i}有天分{/i}的学员送到我这儿吗？"
    show c1p4s1 19
    sila "别被他小小的身板骗了！" with diss
    sila "他十几岁、我还是他教练的时候，我就犯过这个错。"
    sila "第一节课我吃足了苦头，因为我低估了他。"
    show c1p4s1 20
    rayn "你是说这个小不点是你以前的学生？" with diss
    show c1p4s1 21
    sila "那当然！" with diss
    sila "准确地说，是我教过最优秀的学生之一。"
    sila "你还记得你刚拜我为师时，我提过[mc_name]吗？"
    show c1p4s1 22
    rayn "[mc_name]？！" with diss
    rayn "这{i}就是{/i}他？！"
    show c1p4s1 23
    sila "没错！" with diss
    sila "本来该由我亲自带他，但后来变了很多。"
    sila "我学会了魔法，而他已经生疏了。"
    sila "他值得最好中最好的，而除了你，没人能给得起。"
    show c1p4s1 24
    asta "他真的需要学会，或者重新学会，怎么打架。" with diss
    show c1p4s1 25
    rayn "好吧，行。" with diss
    rayn "我来带他。"
    show c1p4s1 26
    rayn "那么，[mc_name]，来一场热热身切磋，看看你还记得多少、真正能做到多少？" with diss
    show c1p4s1 27
    mc "听着不错。" with diss
    mc "就算是切磋，你也不用让着我，我还应付得来。"
    show c1p4s1 28
    rayn "哦，小甜心，我可从来没打算让。" with diss
    rayn "等你准备好挨揍了再来找我。"
    show c1p4s1 29
    sila "更衣室里我有各种尺寸的装备。" with diss
    sila "我一般只让健身房会员用馆里的装备，不过从现在起你可以当自己是终身会员了。"
    sila "我带你去更衣室。"
    show c1p4s1 30
    asta "塞拉斯，你走之前，自己要不要也活动一下？" with diss
    asta "今天我拳头痒了。"
    show c1p4s1 31
    sila "哦，那可太好了！" with diss
    hide c1p4s1 with diss
    pause 1.0
    show c1p4s1 32
    $ CharacterProfile.unlock_outfit([(chara["mc"], 5)])
    mc "嘿雷恩，你准备好开始了吗？" with diss
    show c1p4s1 33
    rayn "随时。" with diss
    show c1p4s1 34 with diss
    pause 1.0
    show c1p4s1 35
    rayn "就等你。" with diss
    show c1p4s1 36
    mc "（好，我能行。）" with diss
    mc "（不过我想稍微留一点手。）"
    mc "（这样等我突然「变强」的时候，她就会以为我进步了。）"
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p4s1 37 with hpunch
    pause 0.5
    show c1p4s1 38
    rayn "至少架势还算像样。" with diss
    play sfx "sfx/Fight - Kick - Miss.ogg"
    show c1p4s1 39
    rayn "但你太慢了！" with hpunch
    play sfx "sfx/Table - Slam.ogg"
    show c1p4s1 40
    rayn "这就是塞拉斯昔日明星弟子的水平？" with hpunch
    rayn "真是让人失望。"
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p4s1 41 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p4s1 42 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p4s1 43
    rayn "说实话，对你的期待高多了。" with hpunch
    show c1p4s1 44
    rayn "起来！" with diss
    show c1p4s1 45
    rayn "让你见识一下{i}真正{/i}的格斗高手。" with diss
    stop bgm fadeout 3.0
    show c1p4s1 46
    $ CharacterProfile.unlock_outfit([
        (chara["asta"], 2),
        (chara["sila"], 1)
    ])
    sila "{i}*大口喘气*{/i}" with diss
    show c1p4s1 47
    sila "呃啊！" with diss
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p4s1 48 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Kick - Miss.ogg"
    show c1p4s1 49 with hpunch
    pause 0.5
    show c1p4s1 50 with diss
    pause 1.0
    play sfx "sfx/Throw.ogg"
    pause 0.5
    show c1p4s1 51 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p4s1 52
    asta "呃！" with hpunch
    show c1p4s1 53
    asta "打得不错。" with diss
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p4s1 54 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p4s1 55 with hpunch
    pause 0.5
    play sfx "sfx/Power - Buff.ogg"
    show c1p4s1 56
    sila "吼——！" with hpunch
    play sfx "sfx/Power - Impact.ogg"
    show c1p4s1 57 with hpunch
    pause 0.5
    show c1p4s1 58
    asta "还行。" with diss
    show c1p4s1 59
    asta "不过你永远比不上我的力量。" with diss
    play sfx "sfx/Astral - Charge2.ogg"
    show c1p4s1 60 with diss
    pause 1.0
    show c1p4s1 61 with diss
    pause 1.0
    show c1p4s1 62
    sila "等等，停手！" with diss
    sila "我认输。"
    show c1p4s1 63
    sila "你赢了！" with diss
    sila "这种切磋真该换个地方，别在我这么贵的健身房里。"
    show c1p4s1 64
    rayn "{i}那{/i}才叫打架。" with diss
    rayn "看穿对方的动作，在一瞬间做出反应。"
    rayn "以及那种不管不顾的狠劲。"
    show c1p4s1 65
    rayn "哪怕不是为了自保、也不是单纯的生死关头，{i}正是{/i}这些才让格斗成为一种艺术。" with diss
    show c1p4s1 66
    mc "哇，你对这些真的很热衷啊。" with diss
    show c1p4s1 67
    rayn "是啊。" with diss
    show c1p4s1 68
    rayn "那么准备好第二回合了吗？" with diss
    show c1p4s1 69
    mc "嗯，大概吧。" with diss
    hide c1p4s1 with diss
    pause 1.0
    play sfx "sfx/Table - Slam.ogg"
    show c1p4s1 70 with hpunch
    pause 1.0
    show c1p4s1 71
    rayn "你还是没能赢我，不过这次你有点样子了。" with diss
    show c1p4s1 72
    rayn "我真没想到你以前的训练底子会显出来，两场都是。" with diss
    rayn "光这一点就足以让我觉得，我的時間花在你身上值得。"
    show c1p4s1 73
    mc "谢谢你，雷恩，我很感激这一切。" with diss
    mc "不过我还以为我是来学怎么使用力量的。"
    show c1p4s1 74
    rayn "你是说魔法力量？" with diss
    show c1p4s1 75
    mc "对，阿斯塔拉说她带我来就是为了这个。" with diss
    show c1p4s1 76
    rayn "哦……" with diss
    show c1p4s1 77
    rayn "抱歉，这个我帮不了你。" with diss
    rayn "总之，我们俩都该去冲个澡了。"
    show c1p4s1 78
    mc "（她教不了我用魔法，那跟她训练还有什么意义？）" with diss
    mc "（唉……感觉我今天一整天都在被人耍着走。）"
    mc "（我就该待在家里。）"
    mc "（至少那样我还有点进展。）"
    stop bgs fadeout 1.0
    hide c1p4s1 with diss
    pause 1.0
    jump c1p4s2

label c1p4s2:
    scene black
    show c1p4s2 1
    mc "（真是蠢透了……）" with diss
    mc "（至少我又见到塞拉斯了。）"
    play sfx "sfx/Door - Distant.ogg" volume 0.5
    show c1p4s2 2
    rayn "{i}*远远地*{/i} 嘿阿斯塔拉，洗得舒服吗？" with diss
    show c1p4s2 3
    asta "{i}*远远地*{/i} 嗯，挺舒服的。" with diss
    asta "{i}*远远地*{/i} 我很喜欢这里的水压。"
    asta "{i}*远远地*{/i} 还有这晶体供暖，简直绝了！"
    show c1p4s2 4
    mc "咦，通风口应该是把更衣室连起来了。" with diss
    mc "不过我不该偷听，那样很失礼。"
    show c1p4s2 2
    asta "{i}*远远地*{/i} 那[mc_name]怎么样？" with diss
    show c1p4s2 3
    mc "不过话说回来，当着不在场的人的面聊他们，同样很失礼。" with diss
    $ choice1 = ChoiceOption(
                "偷听。",
                stats={"asta": {"affection": -3}, "mc": {"karma": -3}},
                path_info=(("asta", "rayn"), "Lewd Scene"),
            )
    $ choice2 = ChoiceOption(
                "不偷听。",
                stats={"mc": {"karma": 3}}
            )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            $ asta_rayn_eavesdrop = True
            show c1p4s2 5 with diss
            pause 1.0
            hide c1p4s2 with diss
            call astarayngbg from _call_astarayngbg
            $ CharacterProfile.unlock_memory([(chara["asta"], "astarayngbg"),(chara["rayn"], "astarayngbg")])
        "[choice2.get_display_text()]":
            $ choice2.apply_stats()
            show c1p4s2 2
            mc "（算了，还是算了。）" with diss
            hide c1p4s2 with diss
            pause 1.0
    jump c1p4s3

label c1p4s3:
    scene black
    play bgm "bgm/Fitness.ogg" fadein 1.5
    play bgs "bgs/Gym.ogg" fadein 1.0
    show c1p4s3 1
    asta "嘿，[mc_name]。" with diss
    asta "你是来找雷恩的吧，她已经走了。"
    show c1p4s3 2
    mc "糟糕，我还想谢谢她呢。" with diss
    show c1p4s3 3
    asta "那么，洗得舒服吗？" with diss
    show c1p4s3 2
    mc "嗯，挺舒服的。" with diss
    mc "这里水压挺足的。"
    show c1p4s3 4
    asta "我刚才还在跟雷恩说一模一样的话呢！" with diss
    show c1p4s3 5
    mc "嗯，我知道了。" with diss
    show c1p4s3 6 with diss
    pause 1.0
    show c1p4s3 7
    asta "我忘了通风管这么容易传声……" with diss
    show c1p4s3 8
    asta "所以你全听见了？" with diss
    show c1p4s3 9
    if asta_rayn_eavesdrop:
        mc "嗯……抱歉。" with diss
        mc "不过知道有人对我感兴趣，感觉还挺不错的。"
        show c1p4s3 10
        asta "没关系。" with diss
        asta "不过现在回想起来，我说的有些话挺让人难为情的。"
    else:
        mc "也还好。" with diss
        mc "我很快就开了花洒，什么都没听见。"
        show c1p4s3 10
        asta "那就好。" with diss
    asta "明天同一时间，你要不要再来这儿见我？"
    show c1p4s3 11
    mc "反正我工作也没了，没别的事。" with diss
    mc "那去呗。"
    show c1p4s3 12
    asta "太好了！" with diss
    asta "那明天见！"
    show c1p4s3 13 with diss
    pause 1.0
    show c1p4s3 14
    sila "雷恩是个狠角色啊。" with diss
    show c1p4s3 15
    mc "是啊，她对这些充满热情。" with diss
    mc "这让我有点希望自己也有那种劲头。"
    show c1p4s3 14
    sila "是啊！" with diss
    sila "我是有动力，但她完全不在一个层次！"
    show c1p4s3 16
    sila "我这么说你得信，你{i}不会{/i}想知道支撑她那种动力的是什么。" with diss
    sila "那是压得人一生都喘不过气的重担。"
    show c1p4s3 17
    mc "她出过什么事吗？" with diss
    show c1p4s3 16
    sila "这不是我该讲的故事。" with diss
    sila "也许有一天她会对你敞开心扉。"
    sila "我只是希望你明白，那种动力通常来自最黑暗的地方。"
    show c1p4s3 17
    mc "这倒说得通。" with diss
    mc "我正想去一趟「最后一滴」，就是二十二街那家。"
    mc "你要一起来吗？"
    show c1p4s3 18
    sila "今天不行，兄弟，不过改天一定补上。" with diss
    sila "这么多年没见，我们有的是话要聊。"
    show c1p4s3 19
    mc "是啊。" with diss
    mc "不过好吧，那我还是明天再见你了。"
    show c1p4s3 20
    sila "回见，[mc_name]。" with diss
    hide c1p4s3 with diss
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    pause 1.0
    jump c1p4s4

label c1p4s4:
    scene black
    play bgm lastdropmusic fadein 1.5
    play bgs "bgs/Club.ogg" fadein 1.0
    $ renpy.random.shuffle(lastdropmusic)
    show c1p4s4 1 with diss
    pause 1.0
    show c1p4s4 2
    mc "（哇，这地方现在可不只是间酒吧了。）" with diss
    show c1p4s4 3
    mc "嘿，能给我来杯酒吗？" with diss
    mc "来点烈的。"
    show c1p4s4 4
    bart "没问题，一杯「急速脉动」马上来！" with diss
    show c1p4s4 5
    mc "急速脉动？" with diss
    mc "我从没听说过。"
    show c1p4s4 6
    bart "这是我自己调的。" with diss
    bart "烈酒加柠檬味的法师汽水，再撒一小撮盐。"
    show c1p4s4 7
    bart "给你！" with diss
    show c1p4s4 8
    mc "谢了！" with diss
    mc "这地方怎么变成这样了？"
    mc "我上次来的时候这还是间酒吧，而那才一年前。"
    show c1p4s4 9
    bart "赶上了升级改造。" with diss
    bart "生意开始不行，老板就决定把这地方改头换面。"
    bart "他雇了个新经理，现在这里是间夜店。"
    show c1p4s4 10
    bart "他们甚至还请了本地DJ来放超酷的曲子。" with diss
    show c1p4s4 8
    mc "不吹，这里还真不错。" with diss
    mc "听不见那些念头，就更容易把它们淹掉。"
    show c1p4s4 11
    bart "嗯，我懂。" with diss
    bart "今天有什么让你不高兴？"
    show c1p4s4 8
    mc "我知道你想干什么。" with diss
    mc "我不需要一个酒保心理医生，不过谢谢你的关心。"
    show c1p4s4 11
    bart "为什么不需要？" with diss
    bart "有时候，一个与此事没有利害关系的人给出的旁观视角，{i}恰恰{/i}正是你需要的。"
    show c1p4s4 8
    mc "我不知道……" with diss
    mc "但把满肚子的烂事倒给一个连名字都不知道的人，我总觉得不对。"
    show c1p4s4 12
    $ CharacterProfile.unlock_profile([chara["soul"]])
    soul "大家都叫我索尔，我该怎么称呼你？" with diss
    show c1p4s4 13
    mc "我叫[mc_name]。" with diss
    show c1p4s4 14
    soul "好，[mc_name]，我们不再是彻底的陌生人了。" with diss
    soul "这样你是不是就能更自在地跟我聊你的麻烦了？"
    show c1p4s4 15
    mc "哇，女士，你可真是不依不饶啊。" with diss
    show c1p4s4 16
    soul "我只是觉得你手里那杯酒只是治标不治本，而我也许能给你个更持久的办法。" with diss
    soul "再说了，像你这么特别的人，不该一个人扛着所有麻烦。"
    show c1p4s4 13
    mc "{i}特别{/i}？" with diss
    mc "什么意思？"
    show c1p4s4 17
    soul "我想你明白我的意思。" with diss
    soul "拥有那么强的力量，你还是找得到借酒浇愁的理由。"
    show c1p4s4 18
    mc "（她不可能知道我是神裔，对吧？）" with diss
    mc "（除非……她也是。）"
    show c1p4s4 13
    mc "等等，你跟我一样？！" with diss
    show c1p4s4 19
    soul "哦，不。" with diss
    soul "我只是对感知魔力很有经验罢了。"
    soul "你的气息和我见过的任何人都不同，这只能说明一件事。"
    show c1p4s4 20
    mc "所以你只是个法师？" with diss
    show c1p4s4 21
    soul "不只是法师，我是其中最强的之一。" with diss
    show c1p4s4 22
    mc "那你怎么会在这儿？" with diss
    mc "法师可是全世界薪水最高的人群之一。"
    show c1p4s4 23
    soul "我喜欢这里。" with diss
    soul "但我也不是那种到处在人前炫耀实力的人。"
    show c1p4s4 22
    mc "这我能理解。" with diss
    mc "如果你真有你说的那么强，那你可能会变成大名人。"
    mc "要是你讨厌被人注意，那确实不是件好事。"
    show c1p4s4 24
    soul "正是。" with diss
    soul "我喜欢把自己的生活过得简单轻松。"
    show c1p4s4 25
    soul "现在你多了解了我一点，而我对你几乎一无所知。" with diss
    soul "那就说吧。"
    show c1p4s4 26
    soul "什么事让你需要喝那么烈的酒？" with diss
    show c1p4s4 27
    mc "好吧，你赢了。" with diss
    mc "我最近发现自己是神裔，整个人生都被搅乱了。"
    hide c1p4s4
    scrn "接下来的一个小时，你把发生的一切都向索尔抱怨了一遍。" with diss
    show c1p4s4 28
    mc "——而且没人真正在帮我学会使用这些力量。" with diss
    mc "我甚至不想当什么神裔，可既然别人都希望我当，我就试着学着应对。"
    mc "为了一个我根本不在乎的东西，承受这么大压力。"
    show c1p4s4 29
    soul "哇，这确实够呛。" with diss
    soul "那么，如果有办法摆脱这些力量，你会吗？"
    show c1p4s4 28
    mc "毫不犹豫！" with diss
    show c1p4s4 30
    soul "我明白了。" with diss
    soul "可惜，这个我帮不了。"
    soul "但我{i}可以{/i}帮你学会使用你的力量。"
    show c1p4s4 28
    mc "真的？" with diss
    mc "至少这样承受起来会容易些。"
    show c1p4s4 31
    soul "就是这个意思。" with diss
    soul "我午夜下班，你要是愿意在这儿等，或者那时候再来，我可以帮你。"
    show c1p4s4 28
    mc "那太好了！" with diss
    mc "谢谢你，索尔。"
    show c1p4s4 31
    soul "不客气。" with diss
    stop bgs fadeout 1.0
    hide c1p4s4 with diss
    stop bgm fadeout 3.0
    pause 1.0
    jump c1p4s5

label c1p4s5:
    scene black
    play bgs "bgs/City - Night.ogg"
    show c1p4s5 1
    mc "（里面越来越吵了。）" with diss
    mc "（我就在这儿待到午夜吧。）"
    show c1p4s5 2
    mc "（不知道索尔是不是真像她说的那么强。）" with diss
    play sfx "sfx/Footsteps - Concrete - Slow.ogg"
    pause 1.5
    show c1p4s5 3
    unkn "哎呀，哎呀，哎呀。" with diss
    unkn "瞧瞧这是谁。"
    unkn "我终于追上你了。"
    show c1p4s5 4
    mc "呃，我们认识吗？" with diss
    show c1p4s5 5
    unkn "大概不认识！" with diss
    play bgm "bgm/Scion of Fire.ogg"
    play sfx "sfx/Fire - Start.ogg"
    show c1p4s5 6
    unkn "不过等我收拾完你，你就难忘喽！" with diss
    play sfx "sfx/Fire - Blast.ogg"
    show c1p4s5 7 with hpunch
    pause 1.0
    show c1p4s5 8
    mc "嘿！" with diss
    mc "你干什么，老兄？！"
    show c1p4s5 9
    unkn "躲得不错！" with diss
    unkn "不过有点可惜，你没用你的力量。"
    show c1p4s5 10
    mc "你在说什么？" with diss
    show c1p4s5 11
    unkn "别跟我装傻，小子！" with diss
    unkn "我知道你是什么，因为我也是！"
    show c1p4s5 12
    $ CharacterProfile.unlock_profile([chara["leon"]])
    scif "我是里昂，火之神裔！" with diss
    show c1p4s5 13
    scif "到目前为止，我遇到的每一个神裔都被我的火焰烧成了灰，只有一个例外！" with diss
    scif "就连她，也不得不从我焚尽一切的烈焰中逃走！"
    show c1p4s5 14
    mc "（又一个神裔？）" with diss
    mc "（而且听起来，他一直在猎杀其他神裔。）"
    show c1p4s5 15
    mc "你为什么要追杀其他神裔？" with diss
    show c1p4s5 16
    scif "这还不明显吗？" with diss
    show c1p4s5 17
    scif "旧日诸神明白其中的道理，而我从得到力量那天起就懂了！" with diss
    scif "如果别人质疑你的威势，你就统治不了世界！"
    scif "所以我要把每一个竞争者都找出来，让他们见识我的力量！"
    play sfx "sfx/Fire - Continual.ogg"
    queue sfx "sfx/Fire - C Loop.ogg" loop
    pause 0.5
    show c1p4s5 18
    scif "等我全部解决，再没人能挑战里昂的威势！" with hpunch
    play sfx "sfx/Fire - Start.ogg"
    show c1p4s5 19 with hpunch
    pause 1.0
    play sfx "sfx/Fire - Explosion.ogg"
    show c1p4s5 20
    mc "呃啊！" with hpunch
    play sfx "sfx/Body - Drop - Light.ogg"
    show c1p4s5 21
    scif "什么？" with diss
    scif "你连还手都不打算？！"
    scif "无所谓，我直接送你解脱！"
    play sfx "sfx/Fire - Explosion.ogg"
    play sfx2 "sfx/Light - Shield.ogg"
    show c1p4s5 22 with hpunch
    scif "搞什么？" with diss
    show c1p4s5 22a
    scif "这护盾是从哪冒出来的？！" with diss
    show c1p4s5 23 with diss
    pause 1.0
    show c1p4s5 24
    soul "天，没人告诉我真正的好戏是在外面上演。" with diss
    show c1p4s5 25
    scif "听着女士，这件事你最好别掺和！" with diss
    scif "你知道自己在招惹谁吗？！"
    show c1p4s5 26
    soul "嗯，让我想想……" with diss
    soul "是个神裔，对吧？"
    soul "而且看起来，是个使用火系魔法的。"
    show c1p4s5 25
    scif "什么？！" with diss
    scif "你怎么可能知道？！"
    scif "你不是我同类！"
    show c1p4s5 24
    soul "那不重要。" with diss
    soul "重要的是，你想杀的这个人是我的朋友。"
    show c1p4s5 27
    scif "那你打算怎么阻止我？" with diss
    play sfx "sfx/Light - Cast.ogg"
    show c1p4s5 28
    soul "这样！" with diss
    play sfx "sfx/Light - Spear Strike.ogg"
    show c1p4s5 29 with hpunch
    pause 0.2
    play sfx "sfx/Light - Spear Strike.ogg"
    show c1p4s5 30 with hpunch
    pause 0.2
    play sfx "sfx/Light - Spear Miss.ogg"
    show c1p4s5 31 with hpunch
    pause 0.2
    show c1p4s5 32
    scif "你他妈怎么会有这么强的力量？！" with diss
    play sfx "sfx/Fire - Continual.ogg"
    show c1p4s5 33 with hpunch
    pause 1.0
    play sfx "sfx/Fire - Flames.ogg"
    show c1p4s5 34 with hpunchr
    stop sfx fadeout 0.5
    show c1p4s5 35 with diss
    pause 1.0
    play sfx "sfx/Light - Cast.ogg"
    show c1p4s5 36 with diss
    pause 1.0
    play sfx "sfx/Light - Cast2.ogg"
    show c1p4s5 37 with hpunch
    pause 0.2
    play sfx "sfx/Light - Cast2.ogg" volume 1.2
    play sfx2 "sfx/Light - Cast2 - Layer.ogg"
    show c1p4s5 38 with hpunch
    pause 0.2
    play sfx "sfx/Light - Cast2.ogg" volume 1.4
    show c1p4s5 39 with hpunch
    pause 0.2
    show c1p4s5 40
    scif "什么？！" with diss
    play sfx "sfx/Light - Continual.ogg"
    queue sfx "sfx/Light - C Loop.ogg" loop
    show c1p4s5 41 with hpunchr
    stop bgm fadeout 5.0
    stop sfx fadeout 1.0
    play sfx "sfx/Light - C End.ogg"
    show c1p4s5 42
    scif "操！" with diss
    scif "我要跑了！"
    play sfx "sfx/Footsteps - Concrete - Fast.ogg"
    show c1p4s5 43 with diss
    pause 1.0
    show c1p4s5 44
    soul "[mc_name]！" with diss
    show c1p4s5 45
    soul "（谢天谢地，他还有呼吸。）" with diss
    soul "（但我得马上把他送去医院！）"
    hide c1p4s5 with diss
    pause 1.0
    jump c1p4s6

label c1p4s6:
    scene black
    play sfx "sfx/Car - Door Close.ogg"
    show c1p4s6 1
    soul "别担心，[mc_name]，你会没事的。" with diss
    stop bgs fadeout 1.0
    hide c1p4s6 with diss
    pause 1.0
    play sfx2 "sfx/Car - Screech.ogg"
    play bgs "bgs/Car - Idle.ogg" fadein 1.0
    show c1p4s6 2
    $ CharacterProfile.unlock_outfit([(chara["asta"], 3)])
    soul "认真的吗？！" with diss
    soul "又来一个？"
    play sfx2 "sfx/Car - Door Open.ogg"
    show c1p4s6 3
    asta "你对他做了什么？！" with diss
    show c1p4s6 4
    soul "{i}我{/i}对他做了什么？！" with diss
    soul "我现在是在救他的命！"
    show c1p4s6 5
    soul "阻止我的人是你！" with diss
    show c1p4s6 7
    soul "他没时间耗了。" with diss
    show c1p4s6 8
    soul "如果你是朋友，就上车。" with diss
    show c1p4s6 9
    soul "不是的话，就请{i}{b}滚开{/b}{/i}！" with diss
    play sfx3 "sfx/Car - Pass.ogg"
    show c1p4s6 10
    asta "我是朋友。" with diss
    play sfx2 "sfx/Car - Door Open.ogg"
    show c1p4s6 11
    soul "太好了，走吧！" with diss
    play sfx "sfx/Car - Door Close.ogg"
    stop bgs fadeout 1.0
    show c1p4s6 12
    asta "所以发生了什么？" with diss
    play bgs "bgs/Car - Drive2.ogg" fadein 1.0
    queue bgs "bgs/Car - Drive2b.ogg"
    show c1p4s6 13
    soul "他被人袭击了。" with diss
    show c1p4s6 14
    asta "谁干的？" with diss
    asta "你能描述一下对方的样子吗？"
    show c1p4s6 15
    soul "我敢肯定是另一个神裔。" with diss
    soul "橙色头发，古铜色皮肤，大概六英尺高，眼睛发出橙色的光。"
    show c1p4s6 16
    asta "听起来像里昂。" with diss
    asta "下一个问题听起来会很奇怪，不过他的血管有没有发光？"
    show c1p4s6 17
    soul "没有。" with diss
    soul "这跟那有什么关系？"
    show c1p4s6 18
    asta "这说明他已经不算神裔了。" with diss
    asta "他已经是货真价实的神了。"
    show c1p4s6 19
    soul "什么？！" with diss
    soul "神的话，肯定比那强得多。"
    soul "虽然我把他打穿了一个洞，他还是走了一段路。"
    show c1p4s6 20
    asta "嗯，那他也算比较弱了，毕竟神裔五个月前才开始回归。" with diss
    asta "不过能在这么短时间里完全觉醒力量，还是很了不起的。"
    show c1p4s6 21
    soul "对我来说，他一点都不了不起。" with diss
    stop bgs fadeout 3.0
    play sfx "sfx/Car - Turn Off.ogg"
    show c1p4s6 22
    soul "到了。" with diss
    soul "帮我把他送进医院，拜托。"
    soul "他比看起来重。"
    hide c1p4s6 with diss
    stop bgs fadeout 1.0
    pause 1.0
    call primordial2 from _call_primordial2
    jump c1p4s7

label c1p4s7:
    scene black
    show c1p4s7 1
    soul "能叫个医生过来吗？！" with diss
    show c1p4s7 2
    nurs "天哪！" with diss
    nurs "他伤得很重！"
    show c1p4s7 3
    asta "还用说？！" with diss
    asta "快救他啊！"
    show c1p4s7 4
    nurs "把他带到这边来！" with diss
    nurs "后面有副担架。"
    hide c1p4s7 with diss
    play bgs "bgs/Hospital.ogg" fadein 1.0
    play bgm "bgm/Light Tragedy.ogg" fadein 1.5
    pause 1.0
    show c1p4s7 5
    soul "医生人呢？" with diss
    soul "都快半小时了！"
    show c1p4s7 6
    asta "不知道，但我几乎感知不到他的能量了。" with diss
    show c1p4s7 7
    asta "如果他再得不到救治……恐怕撑不住了……" with diss
    play sfx "sfx/Door - Sliding.ogg"
    show c1p4s7 8
    chri "[mc_name]？！" with diss
    show c1p4s7 9
    soul "终于来了！" with diss
    soul "我还以为永远等不到医生了。"
    show c1p4s7 10
    chri "嗯，虽然他并不归我负责，但我是医生，他是朋友。" with diss
    chri "我自己接手。"
    show c1p4s7 11
    asta "等等，你能这么做？" with diss
    show c1p4s7 12
    chri "嗯，不能……但我不在乎。" with diss
    show c1p4s7 13
    chri "这伤得太重了。" with diss
    chri "他怎么会有这种烧伤？！"
    show c1p4s7 14
    soul "就算我说了你也不会信。" with diss
    show c1p4s7 13
    chri "是他的神裔力量又失控了吗？" with diss
    show c1p4s7 15
    soul "好吧，也许你还真会信。" with diss
    soul "不过不是，是另一个神裔袭击了他。"
    show c1p4s7 16
    asta "他怎么受的伤很重要吗？！" with diss
    asta "快给他上药啊！"
    show c1p4s7 17
    chri "你说得对，不重要。" with diss
    chri "但这种伤光靠药是不够的。"
    show c1p4s7 18
    chri "我通常不让人看到我这么做，但这次一分钟都不能浪费。" with diss
    stop bgm fadeout 3.0
    play sfx "sfx/Heal.ogg"
    show c1p4s7 19 with diss
    pause 1.0
    show c1p4s7 20 with diss
    pause 1.0
    show c1p4s7 21
    chri "{i}*气喘吁吁*{/i}" with diss
    show c1p4s7 22
    asta "不可能吧！" with diss
    asta "你是治愈法师？！"
    show c1p4s7 23
    soul "这能力相当罕见。" with diss
    show c1p4s7 24
    chri "请别告诉任何人。" with diss
    chri "我宁愿自己留着。"
    show c1p4s7 25
    soul "放心。" with diss
    soul "你的秘密在我这儿很安全。"
    show c1p4s7 26
    asta "我也是。" with diss
    show c1p4s7 27
    mc "唔……" with diss
    show c1p4s7 28
    mc "天啊……" with diss
    show c1p4s7 29
    chri "别急。" with diss
    chri "完全恢复需要一点时间。"
    chri "你的大脑得先接受「你已经没伤」这个事实。"
    show c1p4s7 30
    mc "克里斯汀，你会魔法？" with diss
    show c1p4s7 31
    mc "谢谢大家……" with diss
    mc "我还以为自己必死无疑了。"
    show c1p4s7 32
    mc "不过还是你们救了我。" with diss
    stop bgm fadeout 3.0
    play sfx "sfx/Door - Sliding.ogg"
    play bgm "bgm/Tensions.ogg" fadein 3.0
    show c1p4s7 33
    vero "抱歉打断一下……" with diss
    show c1p4s7 34
    mc "嗯？" with diss
    show c1p4s7 35
    asta "怎么又是你！" with diss
    show c1p4s7 36
    vero "又要出什么问题？" with diss
    stop bgm
    play sfx "sfx/Swipe.ogg" volume 1.0
    show c1p4s7 37
    unkn "哇哦！" with hpunch
    unkn "各位女士，保持冷静！"
    show c1p4s7 38
    asta "哦，太好了，这次是{i}两个{/i}！" with diss
    show c1p4s7 39
    unkn "别担心！" with diss
    unkn "我们是来谈和的。"
    $ CharacterProfile.unlock_profile([chara["kate"]])
    kate "我叫凯特琳，不过你可以叫我凯特。"
    show c1p4s7 40
    soul "守望者来这儿到底做什么？" with diss
    show c1p4s7 41
    kate "嗯，[mc_name]曾是之前一项调查的对象。" with diss
    kate "护士们不知道那项调查已经撤销，看到他在这儿就把我们叫来了。"
    show c1p4s7 42
    vero "我们是来通知她们这个变更的，免得他一出现她们就进入高度戒备——这似乎相当频繁。" with diss
    show c1p4s7 43
    asta "好吧。" with diss
    asta "但为什么要来{i}这儿{/i}？"
    stop bgm fadeout 3.0
    show c1p4s7 44
    kate "有你们在，她肯定不会承认，毕竟她一向端着凶巴巴的人设，不过维罗妮卡想为她调查时对[mc_name]的态度道歉。" with diss
    show c1p4s7 45
    chri "我觉得该道的歉不止一个。" with diss
    play bgm "bgm/Shenanigans.ogg"
    show c1p4s7 46
    asta "她要是挨个道歉，我也要一个！" with diss
    show c1p4s7 47
    vero "想得美！" with hpunch
    show c1p4s7 48
    vero "要道歉也该是你向我道歉！" with diss
    vero "{i}你{/i}打断了{i}{b}我的{/b}{/i}调查，然后还动手打我！"
    show c1p4s7 49
    asta "哇，哇，哇。" with hpunch
    asta "你等一下！"
    show c1p4s7 50
    asta "{i}我{/i}打了{i}你{/i}？！" with diss
    asta "明明是你先动手的！"
    show c1p4s7 51
    vero "是，但你先顶撞我，然——" with diss
    stop bgm fadeout 1.0
    play sfx "sfx/Swipe.ogg"
    show c1p4s7 52
    kate "女士们，女士们！" with hpunch
    kate "够了！"
    show c1p4s7 53
    kate "大家能不能好好相处？" with diss
    show c1p4s7 54
    vero "{i}*哼{/i}" with diss
    show c1p4s7 55
    asta "{i}*唔{/i}" with diss
    show c1p4s7 56
    mc "{i}*咳咳*{/i} 我感觉好多了。" with diss
    show c1p4s7 57
    soul "那么，你还打算去做我们说的那件事吗？" with diss
    soul "我不知道你还有没有别的事，也不知道你几点睡，不过对我来说现在还不算晚，你要是还想来就来吧。"
    show c1p4s7 58
    mc "嗯？" with diss
    mc "哦！"
    mc "你是说教我怎么用神裔的力量？"
    show c1p4s7 59
    asta "[mc_name]！" with diss
    asta "守望者还在这儿！"
    show c1p4s7 60
    mc "那又怎样？" with diss
    show c1p4s7 61
    kate "你是神裔？！" with diss
    show c1p4s7 62
    vero "别信这些鬼话，凯特。" with diss
    vero "神裔根本不存在。"
    show c1p4s7 63
    kate "呃，他们当然存在！" with diss
    kate "你昨天是不是错过了跟队长的整个简报？"
    show c1p4s7 62
    vero "我昨天休假，记得吗？" with diss
    show c1p4s7 64
    kate "哦对……" with diss
    show c1p4s7 65
    kate "总之，他给我们看了第48区那场「恐怖袭击」的录像。" with diss
    kate "结果根本不是什么恐怖分子。"
    kate "只是一个人，他在召唤某种影子生物袭击——"
    show c1p4s7 66
    vero "凯特！" with hpunch
    vero "我很想多了解一些，不过我们得出去谈。"
    vero "不能在平民面前讨论守望者的事务。"
    show c1p4s7 67
    kate "哦，对……" with diss
    kate "哎呀！"
    play sfx "sfx/Door - Sliding.ogg"
    show c1p4s7 68
    asta "好……她们走了。" with diss
    show c1p4s7 69
    asta "要是再多看一秒那身该死的守望者制服……" with diss
    show c1p4s7 70
    soul "为什么你这么反感守望者？" with diss
    show c1p4s7 71
    asta "私事。" with diss
    show c1p4s7 70
    soul "她们对你做过什么？" with diss
    show c1p4s7 71
    asta "这个我不回答。" with diss
    show c1p4s7 70
    soul "那就是有咯。" with diss
    show c1p4s7 72
    asta "别再问了，好吗？！" with hpunch
    show c1p4s7 73
    soul "喂。" with diss
    soul "没必要对我这么凶。"
    show c1p4s7 74
    asta "抱歉……" with diss
    show c1p4s7 75
    asta "我只是不想跟任何人谈这件事，{i}永远{/i}都不想。" with diss
    play sfx "sfx/Astral - Portal.ogg"
    show c1p4s7 76
    asta "我先溜了，[mc_name]。" with diss
    asta "明天见。"
    play sfx "sfx/Astral - Warp.ogg"
    show c1p4s7 77
    soul "次元魔法？" with diss
    soul "真没想到我这辈子还能见到这种事。"
    show c1p4s7 78
    chri "你对魔法还真是挺了解。" with diss
    show c1p4s7 79
    soul "嗯，我经验很多。" with diss
    show c1p4s7 78
    chri "是吗……" with diss
    show c1p4s7 80
    chri "那么，[mc_name]，刚才那位就是大名鼎鼎的阿斯塔拉？" with diss
    show c1p4s7 81
    soul "大名鼎鼎？" with diss
    soul "除了对守望者的纯粹憎恨，她看起来并不坏。"
    show c1p4s7 82
    chri "[mc_name]第一次见到她时，她把那个棕发的家伙狠狠揍了一顿。" with diss
    chri "然后把他带走，最后还从摩天楼上把他推了下去。"
    chri "她就是这样让他开始怀疑自己，最后接受了自己是神裔的事实。"
    show c1p4s7 83
    soul "哦，那好吧。" with diss
    show c1p4s7 84
    mc "就是她。" with diss
    mc "她真的没看起来那么糟糕。"
    mc "虽然她确实很难相处。"
    show c1p4s7 85
    chri "很高兴见过她。" with diss
    chri "不过没能采到她的血样本，有点可惜。"
    chri "那对我研究神裔回归会很有帮助。"
    show c1p4s7 86
    mc "你想弄清他们是怎么、或者为什么会回来？" with diss
    show c1p4s7 85
    chri "对。" with diss
    chri "我想这也许能帮我找到逆转这个过程的办法。"
    chri "而且这方面没有任何文献记录。"
    chri "如果我发表研究成果，能为需要医疗救助的人争取到大量资金。"
    show c1p4s7 87
    chri "而且，虽然我认为要放弃力量蠢透了，但作为你的主治医生，我尊重你的意愿。" with diss
    show c1p4s7 88
    soul "哦？" with diss
    soul "也许你根本不需要我教。"
    soul "既然有办法摆脱它们，也许你该把精力放在那上面。"
    show c1p4s7 89
    mc "今晚我们已经看到，不管{i}可能{/i}发生什么，我都必须学会。" with diss
    mc "只要我还有这些力量，其他任何神裔都能找到我。"
    mc "下一次我不要再无能为力。"
    show c1p4s7 88
    soul "好吧，随你。" with diss
    soul "我可不是想改变你的想法。"
    soul "那你准备好了吗？"
    show c1p4s7 89
    mc "嗯，我准备好了。" with diss
    mc "但只要能找个地方停一下，让我买件新衬衫。"
    mc "回头见，克里斯汀。"
    mc "希望下次是在更好的情形下。"
    show c1p4s7 90
    chri "我可记着了。" with diss
    chri "再见，[mc_name]！"
    hide c1p4s7 with diss
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    pause 1.0
    jump c1p4s8

label c1p4s8:
    scene black
    play bgs "bgs/Forest Pond - Night.ogg" fadein 1.0
    show c1p4s8 1
    mc "我们要去哪儿？" with diss
    play sfx "sfx/Leaves Rustle.ogg"
    show c1p4s8 2
    soul "就从这儿穿过去。" with diss
    play bgm "bgm/Magical Time.ogg" fadein 5.0
    show c1p4s8 3
    soul "铛——！" with diss
    show c1p4s8 4
    soul "当我需要逃离城市的喧嚣时，就喜欢来这里。" with diss
    soul "在这里可以尽情放松，不怕弄坏任何东西。"
    show c1p4s8 5
    mc "真漂亮！" with diss
    mc "而且没有电，这很好。"
    mc "上次我想弄清自己的能力时，好像把整个区域的电网都弄停了。"
    show c1p4s8 6
    soul "那我还真是选了个没电的地方。" with diss
    show c1p4s8 7
    soul "现在，第一课是感知你自己的魔法。" with diss
    soul "你能做到吗？"
    show c1p4s8 5
    mc "那要看你说的{i}感知{/i}是什么意思了……" with diss
    show c1p4s8 8
    soul "我的意思是——" with diss
    show c1p4s8 9
    soul "——{i}感受{/i}它。" with diss
    show c1p4s8 10
    soul "就像你现在感受到我一样。" with diss
    show c1p4s8 11
    mc "（糟糕，她靠得可真近。）" with diss
    mc "（以前没注意过，不过她整夜在夜店工作，闻起来居然还挺舒服。）"
    mc "（像薰衣草。）"
    show c1p4s8 12
    soul "那么，你能感受到自己的魔法吗？" with diss
    show c1p4s8 13
    mc "嗯，其实这是我朋友莱拉教我的。" with diss
    show c1p4s8 14
    soul "哦？" with diss
    soul "你认识不少法师啊。"
    show c1p4s8 15
    mc "哦，不是。" with diss
    mc "莱拉不是法师。"
    mc "她只是特别热衷于与更高层次的自我连结。"
    mc "她说这样有助于达成目标。"
    show c1p4s8 16
    soul "哦，听起来她人挺不错。" with diss
    show c1p4s8 17
    soul "既然你已经能感知自己的魔法，下一步就是控制它。" with diss
    soul "听起来，你还没摸索出来。"
    show c1p4s8 18
    mc "绝对没有。" with diss
    show c1p4s8 17
    soul "如果你愿意，我可以帮你。" with diss
    show c1p4s8 18
    mc "怎么帮？" with diss
    show c1p4s8 19
    soul "你听说过{i}编织{/i}吗？" with diss
    show c1p4s8 18
    mc "我还真没听说过。" with diss
    show c1p4s8 17
    soul "简单说，{i}编织{/i}是两个法师——或者在这个情况下，一个法师和一个神裔——共同控制同一股魔法能量的过程。" with diss
    soul "不过这需要相当程度的默契和对彼此的理解才能做到。"
    show c1p4s8 18
    mc "嗯，这可能有点困难。" with diss
    mc "我们几乎不熟。"
    show c1p4s8 20
    soul "这倒是。" with diss
    soul "不过我知道一件能帮助我们建立默契的事。"
    show c1p4s8 18
    mc "什么事？" with diss
    show c1p4s8 21
    soul "跟我来。" with diss
    show c1p4s8 22
    soul "所以这里不仅适合逃离城市，还是个私密又不错的游泳地点。" with diss
    show c1p4s8 23
    mc "哦，不错！" with diss
    mc "不过我没有泳衣。"
    stop bgm fadeout 3.0
    show c1p4s8 24
    soul "我也没有。" with diss
    play sfx "sfx/Cloth3.ogg"
    show c1p4s8 25 with diss
    pause 1.0
    $ choice1 = ChoiceOption(
            "让她继续。", 
            path_info=("soul", "Lewd Scene"),
            stats={"soul": {"affection": 5}}
        )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            $ soul_sd = True
            call soul_skinnydipping from _call_soul_skinnydipping
            $ CharacterProfile.unlock_memory([(chara["soul"], "soulskinnydip")])
            play bgm "bgm/Magical Time.ogg"
        "阻止她。":
            mc "我觉得这不是个好主意。" with diss
            show c1p4s8 26
            soul "为什么？" with diss
            show c1p4s8 27
            mc "我也说不上来……" with diss
            mc "只是让我不太舒服。"
            show c1p4s8 28
            soul "哦……对不起。" with diss
            soul "要不我们就在不建立连接的情况下试试编织吧。"
            soul "我先下水把妆卸了。"
            hide c1p4s8 with diss
            pause 1.0
    jump c1p4s9

label c1p4s9:
    scene black
    show c1p4s9 1
    soul "现在舒服多了。" with diss
    soul "准备好试试编织了吗？"
    show c1p4s9 2
    mc "当然！" with diss
    mc "具体要怎么做？"
    show c1p4s9 3
    soul "好，我会用一点魔法，你要试着{i}感受{/i}它。" with diss
    soul "就像你感受自己的魔法或其他任何东西那样。"
    play sfx "sfx/Light - Cast.ogg"
    show c1p4s9 4 with diss
    pause 1.0
    play sfx "sfx/Light - Cast2.ogg"
    show c1p4s9 5 with diss
    pause 1.0
    show c1p4s9 6
    mc "说真的，这挺酷的。" with diss
    mc "你是召唤系的？"
    mc "我隐约记得在我时醒时昏的时候，看你召出过长枪。"
    show c1p4s9 7
    soul "不是。" with diss
    soul "我操纵的是光。"
    show c1p4s9 8
    mc "所以这个其实只是光？" with diss
    show c1p4s9 9
    soul "嗯。" with diss
    soul "具有实体形状的光。"
    soul "嗯……大部分是实体。"
    show c1p4s9 8
    mc "天，这也太酷了。" with diss
    show c1p4s9 10
    soul "好了，专心点。" with diss
    soul "我们不是来讨论{i}我的{/i}魔法，而是来帮你学会{i}你的{/i}。"
    show c1p4s9 11
    soul "去把剑拿起来吧。" with diss
    show c1p4s9 12 with diss
    pause 1.0
    show c1p4s9 13 with diss
    pause 1.0
    if soul_sd:
        pass
    else:
        play sfx "sfx/Whoosh.ogg"
        show c1p4s9 14 with diss
        pause 1.0
        show c1p4s9 15
        soul "好吧……这在意料之中。" with diss
        soul "再来一次。"
        show c1p4s9 12 with diss
        pause 1.0
        show c1p4s9 13 with diss
        pause 1.0
    play sfx "sfx/Footstep - Leaves.ogg"
    show c1p4s9 16
    mc "哈哈！" with hpunch
    mc "我做到了！"
    if soul_sd:
        show c1p4s9 17
        soul "你确实做到了！" with diss
        soul "看来我们之间至少建立了足够的信任。"
    else:
        show c1p4s9 17
        soul "好了！" with diss
    show c1p4s9 18
    mc "它的能量温暖又舒缓。" with diss
    mc "这和我想象中一件武器该有的样子完全不一样。"
    show c1p4s9 19
    soul "为什么不？" with diss
    show c1p4s9 18
    mc "因为，武器是用来杀人的。" with diss
    show c1p4s9 20
    soul "也不一定。" with diss
    soul "我做的武器是用来保护自己和别人的。"
    show c1p4s9 21
    soul "好了，我要从剑里释放大部分能量。" with diss
    soul "剩下的形态要靠你自己的魔力维持。"
    soul "如果你不这么做，剑的形态就会崩解，魔法也会散掉。"
    show c1p4s9 22
    mc "所以，虽然这剑是用我的魔力做的，我也能用自己的魔力维持它？" with diss
    show c1p4s9 23
    soul "正是如此。" with diss
    soul "这是编织最基础的形式。"
    soul "法师们通常把这门技法称为「传递」，因为你可以把魔力在法师之间不断传递，同时稳步强化它原本的形态。"
    soul "一个法师单独永远造不出一座山，但用这门技法，我见过法师们合力做到这一点。"
    show c1p4s9 24
    mc "这有可能？！" with diss
    show c1p4s9 23
    soul "有可能。" with diss
    soul "而这还只是编织能做到的事情之一。"
    soul "等你精通更高级的形式后，能做的还多着呢。"
    show c1p4s9 21
    soul "准备好维持这把剑了吗？" with diss
    show c1p4s9 25
    mc "我试试。" with diss
    show c1p4s9 26
    soul "好，我数三下释放大部分能量……" with diss
    soul "二……"
    soul "一……"
    if soul_sd:
        pass
    else:
        play sfx "sfx/Light - Fade.ogg"
        show c1p4s9 27 with diss
        pause 1.0
        soul "别让它散掉！"
    play sfx "sfx/Light - Unfade.ogg"
    show c1p4s9 28 with diss
    pause 1.0
    show c1p4s9 29
    soul "干得好！" with diss
    play sfx "sfx/MC Magic - Unstable.ogg"
    show c1p4s9 30 with diss
    pause 0.5
    show c1p4s9 31
    mc "又来了。" with diss
    play sfx "sfx/Light - Shield.ogg"
    show c1p4s9 32 with diss
    pause 1.0
    show c1p4s9 33
    soul "这就是我们从编织开始练的原因。" with diss
    soul "我可以帮你稳定能量。"
    show c1p4s9 34
    mc "这还真方便。" with diss
    mc "我还以为它肯定要炸了。"
    mc "我的魔法好像总是这样。"
    show c1p4s9 35
    soul "把能量和注意力都集中在剑上。" with diss
    soul "你能感觉到自己魔力的不稳定吗？"
    show c1p4s9 36
    mc "我想是的……" with diss
    mc "感觉就像有人拿砂纸在我脑子里磨。"
    show c1p4s9 37
    soul "{i}*笑出声*{/i} 我从没听过这种形容，不过还挺贴切的。" with diss
    show c1p4s9 38
    soul "话说回来，你知道那股不稳定是从哪儿来的吗？" with diss
    show c1p4s9 39
    mc "完全不知道。" with diss
    show c1p4s9 38
    soul "嗯，那肯定是你内心的某个地方出了问题。" with diss
    soul "也许你对自己能做到什么有所怀疑？"
    show c1p4s9 39
    mc "我不怀疑自己现在能做到事了。" with diss
    mc "我只是还不清楚自己究竟{i}能{/i}做什么。"
    show c1p4s9 40
    soul "哦。" with diss
    soul "把能量从剑里释放出来。"
    show c1p4s9 36 with diss
    pause 1.0
    play sfx "sfx/Magic - Dispel.ogg"
    show c1p4s9 41 with diss
    pause 1.0
    show c1p4s9 42
    soul "呼……" with diss
    soul "你确实很有潜力。"
    soul "帮你稳定魔力，是我当法师以来做过最难的事。"
    soul "而我的经历可不算少。"
    show c1p4s9 43
    mc "抱歉，我的能量这么不稳定。" with diss
    show c1p4s9 44
    soul "不用道歉。" with diss
    soul "没人一开始就完美。"
    show c1p4s9 43
    mc "你觉得阿斯塔拉刚获得力量时，也有这么多麻烦吗？" with diss
    show c1p4s9 44
    soul "老实说，我怀疑没有。" with diss
    soul "那个女人冲动又自信。"
    soul "这两点造就了一个强大的法师。"
    soul "所以我想，她应该也是强大的神裔。"
    show c1p4s9 43
    mc "这两点我都不具备，至少在这件事上是这样。" with diss
    show c1p4s9 45
    soul "没关系。" with diss
    soul "我们会把你教出来的。"
    show c1p4s9 44
    soul "告诉我，到现在为止你都用力量做到过些什么。" with diss
    soul "至少能帮我们把你的类型大致缩小范围，希望这能帮你稳定魔力。"
    show c1p4s9 43
    mc "到目前为止，我爆炸过……" with diss
    mc "……发过光、冒过火花……"
    mc "……还有别的……"
    mc "哦对了。"
    mc "我又爆炸了一次。"
    show c1p4s9 46
    soul "{i}*笑出声*{/i} 这可没什么帮助。" with diss
    soul "这些「爆炸」是什么样的？"
    show c1p4s9 43
    mc "呃……有点像电。" with diss
    mc "看起来总是紫色的闪电，我第二次爆炸的时候还把电网弄停了。"
    show c1p4s9 47
    soul "所以，两次是以电为主的爆炸……" with diss
    soul "再加上一次发光……"
    soul "也可能还是电……"
    show c1p4s9 48
    soul "要不要试试用你的魔力驱动某样东西？" with diss
    show c1p4s9 43
    mc "我不确定这是不是个好主意。" with diss
    mc "我可能会把它过载，然后炸掉。"
    show c1p4s9  49
    soul "嗯，你大概说得对。" with diss
    soul "嗯……"
    show c1p4s9 50
    soul "我知道了！" with hpunch
    show c1p4s9 51
    soul "直接把你的能量以原本的形态释放出来！" with diss
    soul "别急着拿它做什么，先看看你能不能只控制它流向哪里。"
    show c1p4s9 52
    mc "这说不定行得通。" with diss
    mc "要是我失败了，做好自保的准备。"
    show c1p4s9 53
    soul "当然。" with diss
    play sfx "sfx/Electric - Continual.ogg"
    queue sfx "sfx/Electric - C Loop.ogg" loop
    show c1p4s9 54 with diss
    pause 0.5
    show c1p4s9 55 with hpunch
    pause 1.0
    mc "（嗯。）" with diss
    mc "（不知怎么的，光是把力量释放出来，竟然比以前容易多了。）"
    mc "（这是因为那个奇怪的紫发男对我做的事吗？）"
    show c1p4s9 56
    soul "很好！" with diss
    soul "现在保持住。"
    show c1p4s9 55 with diss
    play sfx2 "sfx/Fire - Continual.ogg"
    pause 0.5
    stop sfx fadeout 2.0
    queue sfx2 "sfx/Fire - C Loop.ogg" loop
    show c1p4s9 57 with hpunch
    pause 1.0
    show c1p4s9 58
    soul "（火？现在就放火？）" with diss
    soul "（而且是紫色的，就和那道闪电一样……）"
    soul "（这绝对{i}不{/i}正常！）"
    soul "（他的魔法连自己想变成什么都不知道。）"
    show c1p4s9 59
    soul "继续撑住！" with diss
    show c1p4s9 58
    soul "（等等……我认得那道火里的气息。）" with diss
    show c1p4s9 60
    soul "（不会吧！）" with hpunch
    soul "（那是里昂的火！）"
    soul "（这怎么可能？！）"
    show c1p4s9 61
    soul "好了，停！" with diss
    show c1p4s9 62 with diss
    pause 1.0
    play sfx2 "sfx/Fire - C End.ogg"
    show c1p4s9 63 with diss
    pause 1.0
    show c1p4s9 64
    soul "在此之前，你用过火系魔法吗？" with diss
    show c1p4s9 65
    mc "没有。" with diss
    mc "为什么这么问？"
    show c1p4s9 66
    soul "我在里面发现了一些有趣的东西。" with diss
    soul "那道{i}属于你的{/i}火，和{i}里昂的{/i}气息一模一样。"
    show c1p4s9 67
    mc "什么？！" with hpunch
    mc "你是说那个想杀我的火系法师？！"
    show c1p4s9 68
    soul "对，就是他。" with diss
    soul "我不知道这怎么可能。"
    soul "没有法师能用别人的魔法，而且每个法师的魔力都是独一无二的。"
    soul "对神裔来说一定有所不同……或者也许只是{i}你{/i}与众不同。"
    show c1p4s9 67
    mc "你是说我{i}偷{/i}了他的魔法？" with diss
    show c1p4s9 69
    soul "我不知道。" with diss
    soul "这对我来说完全是全新的领域。"
    show c1p4s9 70
    soul "不过这个我们改天再继续。" with diss
    soul "我今天要是再睡不够，今晚的班就要变成噩梦了。"
    show c1p4s9 71
    mc "你都没告诉我你今天还要上班！" with diss
    show c1p4s9 72
    soul "没关系。" with diss
    soul "我能应付。"
    soul "我们回车里吧，我送你回家。"
    hide c1p4s9 with diss
    stop bgs fadeout 1.0
    stop bgm fadeout 3.0
    pause 1.0
    jump c1p5s1

label c1p5s1:
    scene black
    show magic_effect at theme_ember
    with fadeb
    play sfx "sfx/Chapter - In.ogg"
    show c1p5 as c1p5_blur at text_glow
    show c1p5
    with staticflow
    $ save_name = "第1-5章：风波"
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide c1p5
    hide c1p5_blur
    hide magic_effect
    with grunge
    pause 0.5
    play sfx "sfx/Door.ogg"
    show c1p5s1 1 with diss
    pause 1.0
    mc "（哎，电来了！）" with diss
    show c1p5s1 2
    soul "[mc_name]……" with diss
    show c1p5s1 3
    soul "{i}*打哈欠*{/i}" with diss
    show c1p5s1 2
    soul "你说我能不能在这儿先睡一小会儿？" with diss
    show c1p5s1 4
    soul "我累得开不了车了，怕开着开着撞上去……" with diss
    show c1p5s1 5
    mc "当然可以！" with diss
    mc "我可不想你出事故。"
    mc "再说了，你累成这样也有我的份。"
    show c1p5s1 6
    soul "太好了，谢谢。" with diss
    soul "放心，我不记得自己打不打呼。"
    show c1p5s1 5
    mc "就算打也没关系。" with diss
    show c1p5s1 4
    soul "你应该——" with diss
    show c1p5s1 3
    soul "{i}*打哈欠*{/i}" with diss
    show c1p5s1 7
    soul "抱歉……" with diss
    show c1p5s1 4
    soul "你也该睡一会儿。" with diss
    soul "阿斯塔拉说今天要见你，估计你下午有事吧。"
    show c1p5s1 5
    mc "对，不过不是现在。" with diss
    mc "我现在肯定要先睡一觉。"
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p5s1 8 with diss
    pause 1.0
    show c1p5s1 9
    soul "我也是。" with diss
    soul "晚安……"
    show c1p5s1 10
    soul "……早安？" with diss
    show c1p5s1 11
    soul "呃……随便吧。" with diss
    soul "睡个好觉。"
    show c1p5s1 12
    mc "你也是。" with diss
    hide c1p5s1 with diss
    play bgm "bgm/New Day.ogg" fadein 1.5
    pause 1.0
    show c1p5s1 13
    mc "（这一觉睡得真香。）" with diss
    show c1p5s1 14
    mc "（不知道索尔醒了没有，人还在不在。）" with diss
    show c1p5s1 15
    mc "（她还在睡。）" with diss
    show c1p5s1 16
    mc "（要不我去叫醒她……）" with diss
    show c1p5s1 17
    mc "（算了，让她睡吧。）" with diss
    play sfx "sfx/Door - Knock.ogg"
    show c1p5s1 18
    pause 1.0
    mc "（糟了！）" with diss
    mc "（还是在她再敲一次之前看看是谁。）"
    play sfx "sfx/Door - Open.ogg"
    show c1p5s1 19
    layl "嗨，[mc_name]！" with diss
    show c1p5s1 20
    mc "嘘！" with hpunch
    show c1p5s1 21
    mc "{i}*压低声音*{/i} 她在睡觉。" with diss
    show c1p5s1 22
    layl "{i}*压低声音*{/i} 那是谁？" with diss
    show c1p5s1 23
    mc "{i}*压低声音*{/i} 索尔……她是我朋友。" with diss
    show c1p5s1 24
    layl "{i}*压低声音*{/i} 可我怎么还没见过她？" with diss
    show c1p5s1 25
    mc "{i}*压低声音*{/i} 因为我昨天才刚认识她。" with diss
    mc "{i}*压低声音*{/i} 她救过我的命。"
    mc "{i}*压低声音*{/i} 说来话长。"
    show c1p5s1 26
    layl "{i}*压低声音*{/i} 改天一定要讲给我听。" with diss
    layl "{i}*压低声音*{/i} 我下班开车路过，就想过来看看你。"
    layl "{i}*压低声音*{/i} 要是我打扰了，我可以走。"
    show c1p5s1 25
    mc "{i}*压低声音*{/i} 没事。" with diss
    mc "{i}*压低声音*{/i} 只要小声点就行。"
    mc "{i}*压低声音*{/i} 去我房间的话就不用小声了。"
    mc "{i}*压低声音*{/i} 走吧。"
    hide c1p5s1 with diss
    pause 1.0
    show c1p5s1 27
    mc "所以你今天被排到早班了？" with diss
    show c1p5s1 28
    layl "对，彻底完蛋。" with diss
    layl "糟透了。"
    layl "我讨厌早晨。"
    show c1p5s1 29
    mc "我知道。" with diss
    mc "卢米奈特那边怎么样？"
    show c1p5s1 30
    layl "说实话不太好。" with diss
    layl "没了你帮我保持理智，我开始越来越讨厌那儿了。"
    show c1p5s1 31
    mc "我跟你说了两年了，那个地方对里面任何一个员工都不好。" with diss
    show c1p5s1 32
    layl "嗯，我知道。" with diss
    layl "直到你不在了，我才终于自己意识到这一点。"
    show c1p5s1 33
    layl "好的一面是，我很快就能辞职了。" with diss
    show c1p5s1 29
    mc "真的？" with diss
    mc "怎么回事？"
    show c1p5s1 33
    layl "我爸刚谈成一笔大单，报酬很高。" with diss
    layl "他说要把这笔钱全用来帮我把技术实验室办起来。"
    show c1p5s1 34
    mc "太棒了，莱拉。" with diss
    mc "你终于有个地方可以造那些你一直想造的巨型机器人了。"
    show c1p5s1 35
    layl "对吧！" with diss
    layl "他说连合适的厂房都找好了！"
    layl "只要等款项到账，他就立刻买下来！"
    show c1p5s1 36
    mc "那说不定就是这几天的事了？" with diss
    show c1p5s1 37
    layl "对，随时都可能！" with diss
    layl "等一切按我想要的样子弄好，我就带你去看。"
    show c1p5s1 36
    mc "我很期待。" with diss
    play sfx "sfx/Door - Open.ogg"
    show c1p5s1 38
    soul "我好像听见后面有说话声。" with diss
    show c1p5s1 39
    mc "我们没吵到那边去吧？" with diss
    show c1p5s1 40
    soul "没有。" with diss
    soul "你们俩都没把我吵醒。"
    show c1p5s1 41
    mc "那就好。" with diss
    mc "索尔，这位是莱拉。"
    mc "就是我跟你说的那个朋友，她教我怎么感知自己的能量。"
    show c1p5s1 42
    mc "莱拉，这位是索尔。" with diss
    mc "她昨天救了我的命。"
    show c1p5s1 43
    layl "很高兴认识你，索尔！" with diss
    layl "也谢谢你救了这么个笨蛋。"
    layl "没他我早就完了。"
    show c1p5s1 44
    soul "我也很高兴认识你，莱拉。" with diss
    soul "你不用谢我。"
    soul "没有正当理由，我不会眼睁睁看着人被谋杀。"
    play sfx "sfx/Cloth2.ogg"
    show c1p5s1 45
    layl "{i}{b}谋杀？！{/b}{/i}" with hpunch
    layl "你没说那救命是因为有人想{i}{b}杀{/b}{/i}你啊！"
    show c1p5s1 46
    mc "嗯，事实就是这样。" with diss
    mc "另一个神裔想杀我。"
    mc "他说自己是火之神裔。"
    show c1p5s1 47
    mc "这就让我好奇，一共有哪些类型的神裔。" with diss
    mc "我猜故事里每种神明都该对应一种。"
    mc "说不定还有些没被写下来的。"
    show c1p5s1 48
    soul "所以就是元素、情感，还有像生死这类普遍概念。" with diss
    show c1p5s1 49
    soul "对吧？" with diss
    show c1p5s1 50
    layl "哇，有人对这些故事很了解啊！" with diss
    show c1p5s1 51
    layl "看来不只是[mc_name]一个人迷上了它们。" with diss
    show c1p5s1 44
    soul "我可不至于说痴迷。" with diss
    show c1p5s1 52
    soul "那么，莱拉……" with diss
    soul "[mc_name]跟我说，是你教会他感知自己的能量……可你不是法师啊。"
    soul "你是在哪儿学的？"
    show c1p5s1 53
    layl "网上的一些玄学社群，还有我的瑜伽老师。" with diss
    show c1p5s1 44
    soul "哦，有意思。" with diss
    show c1p5s1 53
    layl "我从小就一心想当法师。" with diss
    show c1p5s1 54
    layl "直到十几岁出头我才明白，使用魔法必须是与生俱来的能力，学不来。" with diss
    show c1p5s1 55
    soul "那一定很让人失望。" with diss
    show c1p5s1 56
    mc "哦，确实非常失望。" with diss
    mc "她断断续续哭了好几天。"
    show c1p5s1 57
    layl "但后来我意识到，我拥有比魔法更厉害的东西……" with diss
    show c1p5s1 58
    layl "……那就是我的头脑。" with diss
    show c1p5s1 57
    layl "凭我一直在研究的那些概念，我能与法师匹敌，甚至超越他们。" with diss
    show c1p5s1 49
    soul "那可就有意思了。" with diss
    soul "我对法师没什么恶意，不过要是能把大部分人从那副高高在上的样子上拉下来就好了。"
    soul "他们太傲慢了，就因为掌握的力量比多数人都强。"
    show c1p5s1 59
    soul "我希望你成为真正的神明之后，[mc_name]，还能记得身为凡人是什么感觉，善待我们。" with diss
    show c1p5s1 47
    mc "前提是我能活到成神那天。" with diss
    mc "外面好像有很多坏的神裔。"
    mc "先是里昂袭击我，还说他一直在猎杀像我们这样的人。"
    mc "后来凯特又说什么有个带着暗影军队的神裔袭击了「48区块」，那到底是什么地方？"
    show c1p5s1 60
    layl "48区块？" with diss
    layl "那可是超级机密的守望者设施！"
    show c1p5s1 61
    soul "既然是{i}超级机密{/i}，你{i}怎么会{/i}知道？" with diss
    show c1p5s1 46
    mc "你是不是又去暗网了？" with diss
    show c1p5s1 62
    layl "对……" with diss
    show c1p5s1 63
    mc "我们不是说好你别去网络那些地方吗？" with diss
    mc "各种黑客和怪人都在那儿蹲着，就等着扑倒下一个毫无防备的用户！"
    show c1p5s1 64
    layl "可这就是重点啊。" with diss
    layl "我很清楚这一点，而且我的电脑水平无人能及！"
    layl "他们得在黑客技术上赢过我才行，那是不可能的。"
    show c1p5s1 65
    soul "黑客行为不是被国王禁止了吗？" with diss
    show c1p5s1 66
    layl "是啊，但没人能追踪到我，所以我没事。" with diss
    show c1p5s1 67
    layl "除非你要去告发我？" with diss
    show c1p5s1 68
    soul "不会，我自己也不是什么圣人，我也不想给谁惹麻烦。" with diss
    soul "所以你不用担心我会说什么。"
    show c1p5s1 69
    soul "不过[mc_name]可就不好说了……" with diss
    show c1p5s1 70
    mc "喂，虽然我不喜欢她在暗网乱逛，但我也不是告密者。" with diss
    show c1p5s1 71
    mc "总之，女士们，我今天还得去健身房继续上格斗课。" with diss
    mc "先快速处理几件事，然后我就出门。"
    show c1p5s1 72
    layl "你又去上课了？" with diss
    layl "什么时候开始的？"
    show c1p5s1 73
    mc "昨天。" with diss
    show c1p5s1 74
    layl "啧……脱离了公司的束缚，看来一天里真能发生不少事。" with diss
    show c1p5s1 73
    mc "阿斯塔拉带我去学怎么掌握自己的力量。" with diss
    mc "你可能不信，她带我去的那个人是塞拉斯。"
    mc "他好像发现自己是个法师了。"
    show c1p5s1 75
    layl "他不是已经三十多岁了吗？" with diss
    show c1p5s1 73
    mc "我记得是三十二岁。" with diss
    show c1p5s1 74
    layl "嗯……" with diss
    layl "那我成为法师是不是还有点希望？"
    show c1p5s1 76
    soul "这种事有时候就是很怪，所以谁也说不准。" with diss
    show c1p5s1 77
    soul "总之，我也得回家好好泡个澡。" with diss
    soul "谢谢你让我借宿，[mc_name]。"
    soul "我可不希望把自己的车弄坏。"
    show c1p5s1 78
    mc "没关系。" with diss
    mc "再见，索尔。"
    show c1p5s1 79
    layl "很高兴认识你！" with diss
    show c1p5s1 80
    soul "彼此彼此，莱拉。" with diss
    soul "再见了！"
    show c1p5s1 75
    layl "我去客厅等你。" with diss
    hide c1p5s1 with diss
    pause 1.0
    show c1p5s1 82
    mc "我差不多该出门了。" with diss
    show c1p5s1 83
    layl "我能来看你训练吗？" with diss
    show c1p5s1 84
    layl "我想再见塞拉斯一次，也许还能顺便学点东西。" with diss
    show c1p5s1 85
    mc "有什么不行的。" with diss
    mc "塞拉斯应该也很高兴见到你。"
    mc "哦对了，你还能认识阿斯塔拉和雷恩！"
    show c1p5s1 86
    layl "好吧，阿斯塔拉我认识，你提过她。" with diss
    layl "可雷恩是谁？"
    show c1p5s1 87
    mc "真正在训练我的人是她。" with diss
    mc "塞拉斯觉得我还不够格跟他正面对练。"
    mc "他说得大概没错。"
    mc "不过他们开始用魔法之后，阿斯塔拉很轻松就赢过他。"
    show c1p5s1 88
    layl "那我更得去了！" with diss
    layl "要是能看法师和神裔交手，我能学到一大堆东西，正好帮我实现最新的设计概念。"
    show c1p5s1 89
    mc "哦？" with diss
    mc "你要设计新机器人了？"
    show c1p5s1 90
    layl "不，比那更好。" with diss
    layl "不过我不说。"
    layl "你就等着我把技术实验室弄到手、把概念变成现实吧。"
    show c1p5s1 89
    mc "好吧，随便你。" with diss
    mc "不过最好值得我等下去，你现在把我的好奇心全勾起来了，在知道之前它会一直在后台折磨我。"
    show c1p5s1 90
    layl "相信我，绝对值得等。" with diss
    show c1p5s1 89
    mc "那你准备好去找灵感了吗？" with diss
    show c1p5s1 91
    layl "好了！" with diss
    layl "你带路的话我来开车。"
    layl "不过我想先停一下买运动服。"
    layl "我早就该添置一身新行头了，顺路买一套吧。"
    show c1p5s1 92
    layl "你愿意的话可以帮我挑。" with diss
    show c1p5s1 89
    mc "嗯，好吧。" with diss
    mc "不过我对时尚风格不太在行，可能会挑得很糟。"
    show c1p5s1 93
    layl "别担心。" with diss
    layl "要是很糟我会告诉你的。"
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    hide c1p5s1
    scrn "你和莱拉在去塞拉斯健身房的路上，先去了一家服装店。" with diss
    jump c1p5s2

label c1p5s2:
    play bgm "bgm/Shopping.ogg" fadein 1.5
    show c1p5s2 1
    layl "好了，我挑了几套来试。" with diss
    layl "得帮我选出最好的一套。"
    show c1p5s2 2
    mc "听起来很简单。" with diss
    show c1p5s2 3
    layl "更衣室在后面。" with diss
    hide c1p5s2 with diss
    pause 1.0
    show c1p5s2 4
    layl "你就在这儿等着，我每换一套就出来给你看。" with diss
    layl "你只要告诉我穿在我身上好不好看就行。"
    show c1p5s2 5
    mc "收到。" with diss
    play sfx "sfx/Door - Light - Open.ogg" volume 1.5
    show c1p5s2 6
    layl "太好了！" with diss
    layl "马上回来。"
    play sfx "sfx/Door - Light - Close.ogg" volume 1.5
    show c1p5s2 7
    mc "（这倒是新鲜体验。）" with diss
    mc "（她以前从没拉着我去给她{i}自己{/i}买衣服。）"
    hide c1p5s2 with diss
    pause 1.0
    play sfx "sfx/Door - Light - Open.ogg" volume 1.5
    show c1p5s2 8
    layl "第一套来啦！" with diss
    layl "怎么样？"
    menu:
        "好":
            $ layl_shoppingoutfits += 1
            show c1p5s2 9
            mc "太棒了！" with diss
            show c1p5s2 10
            layl "真的吗？" with diss
            layl "我不太喜欢这套。"
        "坏":
            show c1p5s2 9
            mc "肯定有更好的。" with diss
            show c1p5s2 11
            layl "对，这套我也不满意。" with diss
    show c1p5s2 12
    layl "我去换另一套。" with diss
    play sfx "sfx/Door - Light - Close.ogg" volume 1.5
    show c1p5s2 7 with diss
    pause 1.0
    hide c1p5s2 with diss
    pause 1.0
    play sfx "sfx/Door - Light - Open.ogg" volume 1.5
    show c1p5s2 13
    layl "第二套来啦！" with diss
    layl "你觉得怎么样？"
    menu:
        "好":
            $ layl_shoppingoutfits += 1
            show c1p5s2 14
            mc "这套穿在你身上真是火辣！" with diss
            if layl_shoppingoutfits >= 1:
                mc "或者，也可能只是你本人很火辣。"
            show c1p5s2 15
            layl "这正是我想要的。" with diss
            if layl_shoppingoutfits >= 1:
                show c1p5s2
                layl "而且完全就是我{i}自己{/i}的风格。" with diss
        "坏":
            show c1p5s2 14
            mc "嗯……还是算了。" with diss
            mc "这套太风尘了。"
            show c1p5s2 16
            layl "我会用的词是{i}性感{/i}……不过好吧。" with diss
    show c1p5s2 17
    layl "只剩最后一套了。" with diss
    if layl_shoppingoutfits == 0:
        layl "希望至少最后这套你会喜欢。"
    play sfx "sfx/Door - Light - Close.ogg" volume 1.5
    show c1p5s2 7 with diss
    pause 1.0
    hide c1p5s2 with diss
    pause 1.0
    play sfx "sfx/Door - Light - Open.ogg" volume 1.5
    show c1p5s2 18
    layl "锵！" with diss
    layl "你肯定会喜欢这套。"
    menu:
        "好":
            $ layl_shoppingoutfits += 1
            show c1p5s2 19
            mc "绝对！" with diss
            mc "这是目前最好的一套！"
            show c1p5s2 20
            layl "对，我也这么觉得。" with diss
            layl "就买这套了。"
        "坏":
            show c1p5s2 19
            mc "可是，我不太喜欢这套。" with diss
            
            show c1p5s2 21
            layl "真可惜，本来要买的就是这套。" with diss
    $ CharacterProfile.unlock_outfit([(chara["layl"], 4)])
    show c1p5s2 22
    layl "我喜欢这套，因为它不限制我的动作。" with diss
    if layl_shoppingoutfits == 0:
        show c1p5s2 23
        layl "你真的一套都不喜欢吗？" with diss
        show c1p5s2 24
        mc "抱歉，真的不行。" with diss
        mc "不太喜欢。"
        mc "我想我只是在运动服方面比较奇怪。"
        show c1p5s2 25
        layl "哦。" with diss
    show c1p5s2 26
    mc "所以我得问了。" with diss
    mc "既然你反正要买自己{i}喜欢{/i}的那套，那让我「帮忙挑」的意义是什么？"
    show c1p5s2 22
    layl "不知道。" with diss
    layl "我想我大概是想听听你的意见，帮{i}我{/i}做决定。"
    show c1p5s2 27
    layl "抱歉……这是个坏毛病……" with diss
    show c1p5s2 22
    layl "不过要是能让你好受点，我认识很多女人也这样。" with diss
    layl "我们甚至会互相这么干。"
    show c1p5s2 26
    mc "女人有时候真是奇怪。" with diss
    show c1p5s2 28
    layl "我去换回自己的衣服，然后我们就出发。" with diss
    play sfx "sfx/Door - Light - Close.ogg" volume 1.5
    show c1p5s2 7 with diss
    pause 1.0
    stop bgm fadeout 3.0
    show c1p5s2 29
    play sfx "sfx/Zipper.ogg"
    layl "（让他来挑{i}我的{/i}衣服，感觉怪怪的。）" with diss
    layl "（一般都是{i}我{/i}在给{i}他{/i}挑东西。）"
    play sfx "sfx/Thud - Light.ogg" volume 0.75
    show c1p5s2 30
    layl "（呃！）" with hpunch
    layl "（我在想什么啊？！）"
    layl "（我得清醒一点。）"
    show c1p5s2 31
    layl "（我真的在因为他有性感的朋友而吃醋吗？！）" with diss
    layl "（我不能老用那种眼光看他……）"
    show c1p5s2 32
    layl "（这让我想起莎拉……）" with diss
    layl "（而且，那种机会我早就错过了。）"
    show c1p5s2 33
    layl "（我得控制住自己的情绪。）" with diss
    hide c1p5s2 with diss
    pause 1.0
    play bgm "bgm/Shopping.ogg" fadein 1.5
    show c1p5s2 34
    layl "好了，今天挺开心的。" with diss
    layl "总算是从给你和你那个磨叽鬼挑东西里换换口味。"
    show c1p5s2 35
    mc "我只觉得衣服就是衣服。" with diss
    mc "对我来说，只要该遮的都遮住了就行。"
    show c1p5s2 36
    clerk "一共两百晶体。" with diss
    play sfx "sfx/Crystal C - Counter.ogg"
    show c1p5s2 37
    layl "谢谢，给你。" with diss
    show c1p5s2 38
    clerk "谢谢您，{i}小姐{/i}。" with diss
    clerk "祝您购物愉快。"
    show c1p5s2 39
    layl "一定会的！" with diss
    layl "祝您今天愉快！"
    stop bgm fadeout 3.0
    hide c1p5s2 with diss
    pause 1.0
    play bgm "bgm/Fitness.ogg" fadein 1.5
    play bgs "bgs/Gym.ogg" fadein 1.0
    jump c1p5s3
    
label c1p5s3:
    scene black
    show c1p5s3 1
    layl "这家店是塞拉斯开的？！" with diss
    show c1p5s3 2
    mc "对，我们认识他到现在，他一路走了这么远。" with diss
    mc "我在电视上看过他参加BFC。"
    show c1p5s3 3
    layl "BFC？" with diss
    show c1p5s3 4
    mc "对，残暴格斗锦标赛。" with diss
    mc "你真的从来没听说过？"
    show c1p5s3 6
    layl "真没有，出乎意料吧。" with diss
    layl "按理说我该在网上哪儿都刷到过，但没有。"
    layl "完全没听说过。"
    show c1p5s3 5
    mc "那是全世界最受欢迎的武术锦标赛。" with diss
    mc "他们甚至不允许使用魔法，所以是纯靠武艺。"
    show c1p5s3 3
    layl "塞拉斯拿过冠军吗？" with diss
    show c1p5s3 4
    mc "拿过，而且三连冠。" with diss
    mc "他现在是卫冕冠军。"
    show c1p5s3 7
    layl "什么？！" with hpunch
    layl "不可能吧！"
    layl "考虑到是全球赛事，这也太厉害了。"
    show c1p5s3 8
    mc "对，真的很厉害。" with diss
    mc "所以他说我还不够格跟他训练时，我才没抱怨。"
    mc "以我现在的生疏程度，他说得肯定没错。"
    show c1p5s3 9
    sila "你们在聊我吗？" with diss
    show c1p5s3 10
    layl "塞拉斯！" with diss
    layl "见到你真好。"
    show c1p5s3 11
    sila "呃……" with diss
    sila "等等……让我想想……"
    show c1p5s3 12
    sila "莱拉，对吧？" with diss
    show c1p5s3 13
    layl "呃，这个……" with diss
    layl "没错！"
    layl "就是我。"
    show c1p5s3 14
    sila "我逗你玩的。" with diss
    sila "我记得你清清楚楚。"
    sila "其实我刚才在健身房另一头就认出你和[mc_name]了，专门过来打招呼。"
    show c1p5s3 15
    mc "见到你真好，塞拉斯。" with diss
    show c1p5s3 16
    sila "你也是，老兄。" with diss
    show c1p5s3 15
    mc "阿斯塔拉来了吗？" with diss
    show c1p5s3 16
    sila "来了，她在楼上的瑜伽室。" with diss
    show c1p5s3 17
    layl "你这儿还有瑜伽课？！" with diss
    show c1p5s3 18
    sila "当然有！" with diss
    sila "我们有瑜伽室、健身器材、格斗台和游泳池。"
    sila "哦，还有休息区，可以吃点东西或者补充水分。"
    show c1p5s3 19
    sila "不过大部分设施只有付费会员才能用。" with diss
    sila "免费会员只能用健身器材。"
    show c1p5s3 17
    layl "所以我想来上瑜伽课的话得付费？" with diss
    show c1p5s3 18
    sila "一般来说，是的。" with diss
    sila "一个月二十五晶体。"
    show c1p5s3 20
    sila "但你是老朋友，我给你和[mc_name]一样的待遇。" with diss
    show c1p5s3 18
    sila "终身会员，完全免费。" with diss
    sila "只要开门，这里的所有设施你都能用。"
    show c1p5s3 21
    layl "你不用这样！" with diss
    layl "我不介意付钱，而且也不贵。"
    show c1p5s3 22
    sila "好吧，既然你{i}想{/i}付，我不跟你争。" with diss
    sila "但要是哪天忘交，别发现你的会员卡还能用时太惊讶。"
    show c1p5s3 23
    sila "说到卡片……" with diss
    show c1p5s3 24
    sila "给你，[mc_name]。" with diss
    sila "你昨天走之后我就让人做了这张。"
    sila "在闸口扫一下就能进。"
    show c1p5s3 16
    sila "我本可以说像上次那样直接翻进去……" with diss
    sila "但我不在的时候，别人看见你这么干可能会想歪。"
    show c1p5s3 15
    mc "谢谢，塞拉斯。" with diss
    mc "你和莱拉先聊吧。"
    mc "我去找阿斯塔拉。"
    show c1p5s3 25 with diss
    play bgs "bgs/Gym.ogg" volume 0.5
    pause 1.0
    show c1p5s3 26 with diss
    pause 1.0
    mc "（她看起来很专注。）" with diss
    mc "（我不该打扰她。）"
    show c1p5s3 27 with diss
    pause 1.0
    show c1p5s3 28 with diss
    pause 1.0
    show c1p5s3 29
    asta "你就打算一直站在那儿默默看我吗？" with diss
    show c1p5s3 30
    mc "呃——不好意思……" with diss
    mc "只是看着实在太有意思了。"
    show c1p5s3 31
    asta "是吗……" with diss
    show c1p5s3 32
    asta "那么，感觉怎么样？" with diss
    show c1p5s3 33
    mc "挺好的，怎么？" with diss
    show c1p5s3 32
    asta "因为你昨晚的烧伤挺吓人的，所以问问。" with diss
    asta "我只是好奇治疗魔法对神裔是不是和对别人一样有效。"
    asta "看来确实有效。"
    show c1p5s3 33
    mc "目前没有副作用，也没出现反复。" with diss
    show c1p5s3 32
    asta "那就好。" with diss
    asta "以后可能用得上。"
    asta "我们神裔比凡人更能扛、恢复也快得多，但对抗神力造成的伤害就不行了。"
    show c1p5s3 34
    asta "所以有个治疗者会非常方便。" with diss
    asta "当然，前提是克里斯汀愿意在需要时帮我们。"
    show c1p5s3 33
    mc "她看起来很喜欢帮助别人，我敢肯定她会的。" with diss
    show c1p5s3 32
    asta "希望如此。" with diss
    asta "你已经亲眼见过我们接下来要面对什么了。"
    show c1p5s3 33
    mc "是啊……" with diss
    mc "外面有些神裔相当有敌意。"
    show c1p5s3 35
    asta "不过这也能理解。" with diss
    asta "我们很多人以前都觉得自己完全无能为力。"
    show c1p5s3 36
    asta "现在有了力量，就能去够那些以前永远够不到的星辰。" with diss
    show c1p5s3 37
    asta "你难道不想用{i}你{/i}新获得的力量去达成{i}你的{/i}愿望吗？" with diss
    asta "就算是那些黑暗的愿望？"
    show c1p5s3 33
    mc "这个念头我有过几次。" with diss
    mc "问题是我没什么欲望。"
    mc "不过要是能变得很有钱倒是不错。"
    show c1p5s3 38
    asta "对别人来说是很宏大的目标，但对神裔而言呢？" with diss
    show c1p5s3 39
    asta "不值一提。" with diss
    show c1p5s3  34
    asta "我有一些从前绝不可能实现的野心。" with diss
    asta "但现在，我的力量让这一切都成了可能。"
    show c1p5s3 33
    mc "你的野心到底是什么？" with diss
    if asta_rayn_eavesdrop:
        mc "和你的{i}任务{/i}有关吗？"
        show c1p5s3 32
        asta "我都忘了你昨天是个爱打听的小老鼠了。" with diss
        asta "所以这句是从雷恩那儿听来的，嗯？"
        show c1p5s3 33
        mc "我控制不住。" with diss
        mc "一听到自己的名字，后面就全乱了套。"
        mc "好奇心赢了。"
        mc "但对，我确实听说了，而且从那之后就一直很好奇。"
        show c1p5s3 35
        asta "我明白了。" with diss
    else:
        show c1p5s3 32
        asta "我算是有一个{i}任务{/i}。" with diss
    show c1p5s3 36
    asta "也许很快我会告诉你。" with diss
    asta "不过现在，你离能帮上忙还差得远。"
    show c1p5s3 33
    mc "为什么？" with diss
    show c1p5s3 41
    asta "因为那对你来说会比昨晚的里昂危险得多。" with diss
    asta "而且，抱歉，我不会为了{i}我{/i}的问题搭上别人的命。"
    show c1p5s3 33
    mc "说得也是。" with diss
    mc "如果我哪天准备好了，你会告诉我吗？"
    show c1p5s3 34
    asta "也许。" with diss
    show c1p5s3 36
    asta "不过是你{i}准备好{/i}的时候，不是「如果」。" with diss
    asta "到那时我会确保你足够强，能在需要时站住脚。"
    show c1p5s3 42
    asta "不过我都不确定自己是否{i}想要{/i}别人的帮助。" with diss
    show c1p5s3 33
    mc "好吧，如果你需要，别客气，尽管开口。" with diss
    show c1p5s3 32
    asta "说定了。" with diss
    show c1p5s3 43
    layl "哇！" with diss
    layl "这瑜伽室不错啊！"
    show c1p5s3 44
    mc "嘿，莱拉。" with diss
    mc "你跟塞拉斯聊完了？"
    show c1p5s3 45
    layl "嗯，不过他那边有人要接待。" with diss
    layl "所以我就想上来看看。"
    show c1p5s3 46
    layl "等我从卢米奈特辞职后，肯定会在这儿花很多时间。" with diss
    show c1p5s3 47
    asta "你要把你的朋友介绍给我吗，[mc_name]？" with diss
    show c1p5s3 48
    mc "哦，对！" with diss
    mc "这位是莱拉，我们一起长大的。"
    show c1p5s3 49
    mc "莱拉，这位是阿斯塔拉。" with diss
    show c1p5s3 50
    layl "很高兴认识你！" with diss
    show c1p5s3 51
    asta "谢谢，也是！" with diss
    show c1p5s3 52
    asta "你喜欢瑜伽啊？" with diss
    show c1p5s3 53
    layl "当然！" with diss
    layl "我从十五岁起几乎每天都练。"
    show c1p5s3 54
    asta "不错！" with diss
    asta "我几个月前才开始。"
    asta "你能给我一些建议吗？"
    show c1p5s3 55
    layl "现在？" with diss
    show c1p5s3 51
    asta "呃，对啊。" with diss
    asta "有什么不行呢？"
    asta "会很好玩的！"
    show c1p5s3  53
    layl "好！" with diss
    layl "我得换衣服。"
    layl "可惜我没有瑜伽裤，不过我{i}确实{/i}有的应该能凑合。"
    show c1p5s3 52
    asta "你知道储物柜在哪儿吗？" with diss
    show c1p5s3 56
    layl "不知道，一点头绪都没有。" with diss
    show c1p5s3 57
    asta "走，我带你去。" with diss
    asta "哦对了，里面的淋浴间一流。"
    show c1p5s3 58
    mc "（她们就这么走了。）" with diss
    mc "（阿斯塔拉明明今天又要见我，结果只是来做瑜伽，连教都不教，这到底是为什么。）"
    show c1p5s3 59
    mc "（现在仔细想想，她真的没教过我任何实用的东西。）" with diss
    mc "（算了。）"
    mc "（我还是去看看塞拉斯在做什么吧。）"
    show c1p5s3 60 with diss
    play bgs "bgs/Gym.ogg" volume 1.0
    pause 1.0
    show c1p5s3 61
    mc "嘿塞拉斯，你忙吗？" with diss
    show c1p5s3 62
    sila "不忙，不怎么忙。" with diss
    sila "我就随便待着。"
    show c1p5s3 63
    sila "坐吧，老兄！" with diss
    play sfx "sfx/Cloth2.ogg" volume 2.0
    show c1p5s3 64
    sila "我看见阿斯塔拉带着莱拉走了。" with diss
    sila "她们就这么把你撂下了对吧？"
    show c1p5s3 65
    mc "对，真是。" with diss
    show c1p5s3 66
    sila "我老远就看出来会这样。" with diss
    show c1p5s3 67
    sila "不是说你被撂下！" with diss
    show c1p5s3 68
    sila "我是说我早知道她们会成为好朋友。" with diss
    sila "她们很合得来。"
    show c1p5s3 65
    mc "真的吗？！" with diss
    mc "她们俩？！"
    mc "我完全想不到。"
    show c1p5s3 66
    sila "对，阿斯塔拉和莱拉一样，也喜欢那些养生和身心修习的东西。" with diss
    show c1p5s3 65
    mc "我大概知道她是这样，但跟她不算很熟。" with diss
    show c1p5s3 66
    sila "你以后会知道的。" with diss
    sila "她跟莱拉一样，绝大部分事都很坦率。"
    show c1p5s3 69
    sila "阿斯塔拉的不同之处在于，一旦某件事她不肯说，就是{i}完全{/i}不说。" with diss
    show c1p5s3 65
    mc "我开始发现了。" with diss
    show c1p5s3 70
    sila "对了……" with diss
    show c1p5s3 71
    sila "抱歉昨晚喝多没去。" with diss
    sila "我听说你出了事，总觉得自己也有责任。"
    show c1p5s3 72
    sila "我要是在场，一定让那个混蛋好看。" with diss
    show c1p5s3 73
    mc "没事的，塞拉斯。" with diss
    mc "我没大碍。"
    show c1p5s3 68
    sila "是啊，阿斯塔拉说你伤得不轻，不过看你现在已经恢复了。" with diss
    sila "肯定是神裔那种特殊的恢复力。"
    show c1p5s3 65
    mc "对，肯定。" with diss
    show c1p5s3 74
    mc "（我隐约记得阿斯塔拉和索尔答应过要替克里斯汀的魔法保密。）" with diss
    mc "（看来阿斯塔拉守约了。）"
    show c1p5s3 75
    sila "你觉得这健身房怎么样？" with diss
    show c1p5s3 76
    mc "非常棒！" with diss
    mc "我就知道，你拿那么多冠军奖金，肯定会大有作为。"
    show c1p5s3 77
    sila "你还在追BFC？！" with diss
    show c1p5s3 78
    mc "当然！" with diss
    mc "自从你介绍给我之后，我每年一场都没落下。"
    show c1p5s3 79
    sila "这话让我很自豪。" with diss
    sila "很高兴你生活再忙，也没有放松自己的训练。"
    show c1p5s3 80
    sila "嗯，至少多少练了一点。" with diss
    sila "昨天雷恩可是把你按在地上摩擦。"
    show c1p5s3 65
    mc "说实话，我有点在留手。" with diss
    show c1p5s3 66
    sila "我看出来了，老兄。" with diss
    sila "我敢说她也看出来了，等她完全意识到之后肯定不会高兴。"
    show c1p5s3  68
    sila "下次跟她切磋你可得做好准备。" with diss
    sila "她生气起来打起架来，挨揍的那一方可不好受。"
    show c1p5s3 65
    mc "哦呀……" with diss
    show c1p5s3 64
    sila "是啊，兄弟，你完蛋了！" with diss
    show c1p5s3 65
    mc "抱歉，塞拉斯，我得把这张会员卡还给你了。" with diss
    mc "我还没活够，看来是没法再来这儿了。"
    show c1p5s3 77
    sila "哈哈！" with diss
    sila "没那么夸张，老兄！"
    sila "不过你大概会流不少血。"
    sila "一定戴好护齿，别把牙打掉了。"
    show c1p5s3 76
    mc "嗯，这完全帮不上忙。" with diss
    show c1p5s3 79
    sila "我这是为你好！" with diss
    show c1p5s3 81
    sila "总之，我快饿死了。" with diss
    sila "你也要来点吃的吗？"
    show c1p5s3 82
    mc "好啊，你有什么？" with diss
    show c1p5s3 83
    sila "我可以做几个汉堡。" with diss
    show c1p5s3 82
    mc "听着不错。" with diss
    hide c1p5s3 with diss
    play bgs2 "bgs/Meat Cooking.ogg" fadein 1.0
    pause 1.0
    show c1p5s3 84
    layl "嗯……" with diss
    layl "这边闻起来好香。"
    show c1p5s3 85
    asta "同意。" with diss
    asta "闻起来是塞拉斯又在做汉堡了。"
    show c1p5s3 86
    sila "你还不了解我吗。" with diss
    sila "一天至少得吃一个汉堡！"
    show c1p5s3 87
    asta "希望你多做点。" with diss
    asta "做完瑜伽我正好想吃点东西。"
    show c1p5s3 88
    layl "我也想要一个，谢谢！" with diss
    show c1p5s3 89
    sila "既然你们要{i}做完{/i}瑜伽再吃，那就结束后来找，我给你们现做。" with diss
    show c1p5s3 90
    asta "成交。" with diss
    show c1p5s3 91
    asta "回头见，哥们儿！" with diss
    show c1p5s3 92
    sila "你听见了吗？" with diss
    show c1p5s3 93
    sila "哥们儿……" with diss
    sila "切！"
    show c1p5s3 94
    sila "也就是我疼她。" with diss
    sila "不然我才不再给她做呢！"
    show c1p5s3 95
    mc "哦，你和阿斯塔拉是不是……" with diss
    show c1p5s3 96
    sila "我们是什么？" with diss
    show c1p5s3 97
    sila "哦，你是说在交往！" with diss
    sila "不，不是那种关系。"
    sila "她就像我从来没有过的妹妹。"
    show c1p5s3 98
    mc "哦，我明白了。" with diss
    show c1p5s3 99
    sila "你喜欢她吗？" with diss
    sila "我有点以为你和莱拉是一对。"
    show c1p5s3 100
    mc "我们只是朋友。" with diss
    mc "我没打算认真投入什么关系。"
    show c1p5s3 101
    sila "为什么？" with diss
    show c1p5s3 100
    mc "有原因。" with diss
    show c1p5s3 101
    sila "哦哦，我大概知道了。" with diss
    show c1p5s3 100
    mc "是啊……" with diss
    show c1p5s3 101
    sila "不过你亏了。" with diss
    sila "要是不想承诺，那就不承诺也行啊。"
    sila "随便玩一玩，找点乐子。"
    if soul_sd:
        show c1p5s3 100
        mc "最近也有人跟我说过类似的话。" with diss
        mc "她说屈从本能、只是为了做而做，也没什么不对。"
        show c1p5s3 101
        sila "这话说得可真够直白的。" with diss
        sila "但也说得真对。"
        sila "总得想办法满足需求。"
    show c1p5s3 100
    mc "你说得可能有道理。" with diss
    mc "我会试着对这类事更开放一些。"
    show c1p5s3 97
    sila "我强烈建议你这么做。" with diss
    sila "会让生活有趣得多。"
    stop bgs2 fadeout 2.0
    show c1p5s3 103
    sila "汉堡好了！" with diss
    sila "现在就剩把它们组装起来。"
    show c1p5s3 104
    sila "给你，老兄。" with diss
    sila "慢用！"
    show c1p5s3 105
    mc "看起来真好吃！" with diss
    hide c1p5s3 with diss
    pause 1.0
    show c1p5s3 106
    asta "嘿，[mc_name]。" with diss
    asta "我们瑜伽和饭都吃完了。"
    show c1p5s3 107
    asta "所以我得问问……" with diss
    asta "你是不是走到哪儿都在告诉别人你是神裔了？"
    show c1p5s3 108
    mc "不是对{i}所有人{/i}。" with diss
    show c1p5s3 109
    asta "克里斯汀知道……" with diss
    show c1p5s3 110
    asta "索尔知道……" with diss
    show c1p5s3 111
    asta "我亲眼看见你在那两名守望者面前脱口而出的……" with diss
    show c1p5s3 112
    asta "而我刚刚又发现莱拉也知道了！" with diss
    show c1p5s3 113
    mc "嗯……" with diss
    mc "那确实已经是不少人了。"
    show c1p5s3 114
    asta "嗯哼。" with diss
    show c1p5s3 115
    asta "算了……" with diss
    asta "只要你别到处说我也是，我就无所谓。"
    show c1p5s3 116
    mc "关于你也是神裔这件事，我{i}只{/i}告诉了莱拉和克里斯汀。" with diss
    mc "而且当时我还没完全相信你。"
    mc "但我不会把你的事告诉别人。"
    mc "我保证。"
    show c1p5s3 117
    asta "行吧。" with diss
    asta "还有，谢谢。"
    show c1p5s3 118
    asta "现在跟我来。" with diss
    show c1p5s3 119
    asta "莱拉，你也来。" with diss
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    hide c1p5s3 with diss
    pause 1.0
    jump c1p5s4

label c1p5s4:
    scene black
    play bgm "bgm/Ambitions.ogg" fadein 3.0
    show c1p5s4 1
    mc "嗯，我们到后面来到底是干什么？" with diss
    show c1p5s4 2
    asta "找个不显眼的地方谈话。" with diss
    show c1p5s4 3
    mc "谈什么？" with diss
    show c1p5s4 4
    asta "我制定了一个计划，需要一些帮助。" with diss
    show c1p5s4 3
    mc "这个{i}计划{/i}是什么？" with diss
    show c1p5s4 2
    asta "去寻找并训练新的神裔。" with diss
    show c1p5s4 3
    mc "你要干什么？！" with diss
    mc "我见过的最后一个神裔可是想杀我！"
    show c1p5s4 5
    asta "然后呢？" with diss
    show c1p5s4 6
    mc "然后{i}你{/i}还想去找{i}他们{/i}？！" with diss
    show c1p5s4 7
    asta "对。" with diss
    show c1p5s4 8
    layl "他们不可能{i}全都{/i}是坏人吧？" with diss
    show c1p5s4 9
    asta "确实。" with diss
    asta "我目前只找到两个。"
    show c1p5s4 10
    asta "里昂可不友好……" with diss
    show c1p5s4 11
    asta "不过你还不错，[mc_name]。" with diss
    asta "所以找到好人的概率是一半一半。"
    asta "那个人可能和你当初被我找到时一样迷茫、一样害怕。"
    show c1p5s4 12
    mc "我没害怕。" with diss
    show c1p5s4 13
    asta "也许吧，但你确实很迷茫。" with diss
    asta "想想我们能帮到他们多少。"
    show c1p5s4 14
    mc "（真的吗？）" with diss
    mc "（她几乎没怎么帮{i}我{/i}，还想去帮{i}别人{/i}？）"
    $ choice1 = ChoiceOption(
            "除非你真的教我。", 
            stats={"mc": {"karma": 5}, "asta": {"affection": 5}, "layl": {"affection": 3}}
        )
    $ choice2 = ChoiceOption(
            "你都还没教过我呢！", 
            stats={"mc": {"karma": -5}, "asta": {"affection": 3}, "layl": {"affection": -3}}
        )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            show c1p5s4 3
            mc "前提是你真的教我。" with diss
            mc "我觉得自己到现在还几乎不懂神裔是怎么回事。"
            show c1p5s4 4
            asta "别担心，我打算教。" with diss
            asta "我知道我自己几乎没教你什么，但我会的。"
            show c1p5s4 3
            mc "希望如此。" with diss
            mc "你刚才还说，不想为了你的任务搭上别人的命。"
            mc "外面有敌对的神裔，这事可能一样危险。"
            show c1p5s4 4
            asta "这点你说得对。" with diss
        "[choice2.get_display_text()]":
            $ choice2.apply_stats()
            stop bgm fadeout 5.0
            show c1p5s4 3a
            mc "你到现在根本还没教过我！" with hpunch
            show c1p5s4 15
            mc "是莱拉教会我怎么调用自己的力量。" with diss
            mc "雷恩在教我打架，我觉得对神裔没什么帮助。"
            mc "而索尔才是教我如何使用、发现力量所在的人。"
            show c1p5s4 16
            mc "你都干了些什么？！" with hpunch
            mc "哦，说得也是。"
            show c1p5s4 17
            mc "你害我在守望者那边惹了麻烦。" with diss
            mc "你把我从一栋楼上踢了下去！"
            show c1p5s4 18
            mc "就算没摔死，也疼得要命！" with diss
            show c1p5s4 19
            mc "然后，你把{i}真正{/i}教我的责任全推给了别人。" with diss
            mc "而且要我说，他们根本不是神裔！"
            show c1p5s4 20
            layl "喂！" with hpunch
            layl "太过分了，[mc_name]！"
            show c1p5s4 21
            asta "不……没关系……" with diss
            asta "他说得对。"
            show c1p5s4 22
            asta "抱歉，我其实没怎么认真教你东西。" with diss
            asta "也谢谢你刚才对我这么坦诚。"
            asta "我保证以后会为你做得更多。"
            show c1p5s4 23
            asta "说实话，我也不太清楚自己到底能为你做什么。" with diss
            asta "我不知道你的力量是什么，也不知道怎么运作。"
            asta "每个神裔都不一样。"
            show c1p5s4 24
            asta "我可能只是害怕，一旦你发现我和你一样无知，就会觉得我是骗子……" with diss
            asta "看来正是我的不作为才让你这么想。"
            show c1p5s4 25
            mc "我不觉得你是骗子。" with diss
            mc "但即便你还在学，你也是最适合教我的人。"
            mc "可我从你这儿几乎什么都没学到。"
            show c1p5s4 26
            asta "我知道……" with diss
            asta "对不起。"
            asta "我会做得更好。"
            show c1p5s4 27
            mc "那我就太感谢了。" with diss
            mc "如果你{i}真的{/i}开始帮我，我就支持这个计划。"
            play bgm "bgm/Ambitions.ogg" fadein 3.0
            show c1p5s4 26
            asta "谢谢。" with diss
        "我们能帮什么忙？":
            show c1p5s4 3
            mc "我们该怎么帮？" with diss
    show c1p5s4 4
    asta "首先要做的是开始寻找其他人。" with diss
    asta "有经验的法师似乎能察觉我们气息的不同，但不知道为什么不同。"
    asta "作为神裔，{i}我们{/i}天生就能分辨谁是不是神裔。"
    asta "只要对方足够强，隔得再远也行，就像我当初找到你一样，[mc_name]。"
    show c1p5s4 28
    layl "可我不是法师，也不是神裔。" with diss
    layl "我跟这事有什么关系？"
    show c1p5s4 9
    asta "神力也只是另一种形式的魔法，而所有魔法本质上都是能量。" with diss
    asta "你说过自己是技术工程师，所以我希望你能设计出某种东西，追踪神裔的能量特征。"
    asta "这样我们就能到处找到他们，而不是只碰巧找到附近的。"
    show c1p5s4 29
    layl "这主意真不错。" with diss
    show c1p5s4 30
    layl "我知道魔法就是能量，但从没把它和能量的各种性质联系起来过。" with diss
    show c1p5s4 29
    layl "总之，对，我觉得我能想出办法。" with diss
    show c1p5s4 31
    mc "那我呢？" with diss
    mc "我看不见气息。"
    show c1p5s4 2
    asta "我来教你。" with diss
    asta "很简单。"
    show c1p5s4 4
    asta "你知道怎么感知能量，对吧？" with diss
    asta "也包括别人的能量？"
    show c1p5s4 3
    mc "对。" with diss
    show c1p5s4 4
    asta "好，这基本是一样的。" with diss
    asta "你现在能感觉到{i}我的{/i}能量吗？"
    show c1p5s4 3
    mc "能。" with diss
    show c1p5s4 4
    asta "很好。" with diss
    asta "现在别去「感觉」，改用眼睛。"
    asta "集中在我能量的{i}感觉{/i}上试着把它想象出来。"
    show c1p5s4 3
    mc "好……" with diss
    play sfx "sfx/Whoosh.ogg"
    show c1p5s4 32 with diss
    pause 1.0
    mc "成功了！" with diss
    mc "这还挺简单！"
    show c1p5s4 33
    asta "对吧？" with diss
    asta "但这只是第一步。"
    asta "现在你得试着去看那些你感觉不强烈、也不知道该往哪儿找的能量。"
    show c1p5s4 34
    asta "你的身体一直在感知每一个其他神裔的能量，因为我们都被同一种东西连接着……" with diss
    asta "……神力。"
    asta "你要做的是捕捉这些感觉，无论多微弱，然后用它在视觉上定位能量来自哪里。"
    show c1p5s4 35
    asta "能量特征离得越远或越弱，这就越难做到。" with diss
    asta "我想这个限制会因你与力量和身体的契合程度而不同。"
    show c1p5s4 32
    mc "说得通。" with diss
    show c1p5s4 34
    asta "去试试看能不能看见别的神裔的气息。" with diss
    show c1p5s4 32
    mc "好。" with diss
    show c1p5s4 36
    mc "（不行，这儿什么都没有……）" with diss
    show c1p5s4 37
    mc "（嗯……还是什么都没有。）" with diss
    show c1p5s4 38
    mc "（等等……那是什么？）" with diss
    show c1p5s4 39
    mc "那边有一股红色的，非常巨大！" with diss
    show c1p5s4 40
    asta "干得好。" with diss
    asta "我盯上那个已经有几天了。"
    show c1p5s4 41
    asta "他的气息和{i}你{/i}的完全不一样，但这是我见过第二大的。" with diss
    show c1p5s4 42
    mc "也就是说他们非常强？" with diss
    show c1p5s4 41
    asta "有可能。" with diss
    asta "单凭气息你能确定的只有一件事：他们拥有{i}大量{/i}魔力。"
    asta "这完全说明不了他们运用的熟练程度。"
    asta "不过话说回来。"
    show c1p5s4 43
    asta "如果他们{i}真的{/i}擅长运用，而且心怀敌意，那你可能就到此为止了。" with diss
    asta "所以我建议暂时别去招惹那个。"
    show c1p5s4 41
    asta "还好，他们似乎从没离开过那片区域。" with diss
    show c1p5s4 42
    mc "嗯，这倒是奇怪。" with diss
    show c1p5s4 44
    asta "说不定他们被关在什么监狱里呢。" with diss
    asta "我从没侦察过那个的具体位置。"
    show c1p5s4 28
    layl "看他们是因为什么被关的，这可能会很糟。" with diss
    show c1p5s4 45
    layl "一个拥有神力的杀人犯，对谁都没好处。" with diss
    show c1p5s4 46
    mc "我们已经有一个里昂了。" with diss
    show c1p5s4 45
    layl "正是。" with diss
    layl "一个神力疯子就够受的了。"
    show c1p5s4  4
    asta "这就引出了第二个目标……" with diss
    asta "我们找神裔不只是为了教导或训练他们。"
    asta "我们还要阻止那些坏人。"
    show c1p5s4 3
    mc "我们到底要怎么做到？" with diss
    show c1p5s4 4
    asta "我还没想出来。" with diss
    asta "但一定会有办法。"
    show c1p5s4 47
    layl "也许我能想出办法。" with diss
    layl "如果神力的运作方式{i}完全{/i}和能量一样，那就应该可行。"
    layl "因为{i}所有{/i}能量都可以被中和。"
    show c1p5s4 9
    asta "那可太有用了。" with diss
    asta "不过我不想一下子把太多任务都丢给你们。"
    show c1p5s4 47
    layl "没关系！" with diss
    layl "我就喜欢攻克复杂的东西！"
    show c1p5s4 9
    asta "既然你这么说。" with diss
    asta "祝你想出办法。"
    asta "我可不想亲手杀掉自己的同族，再引发一个无神纪元。"
    show c1p5s4 48
    layl "我会尽力让那没必要发生。" with diss
    show c1p5s4 49
    asta "那么，还有问题吗？" with diss
    layl "没有。" with diss
    mc "我也没有。" with diss
    show c1p5s4 50
    asta "好，那今天就到这里。" with diss
    asta "我先回家了。"
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p5s4 51
    layl "我也回家。" with diss
    layl "累死我了。"
    show c1p5s4 52
    layl "要送你回家吗？" with diss
    show c1p5s4 53
    mc "我本来想去医院看看克里斯汀。" with diss
    mc "离这儿不算远，我走过去就行。"
    show c1p5s4 51
    layl "哦，好吧。" with diss
    layl "替我向她问好！"
    show c1p5s4 54
    mc "一定。" with diss
    show c1p5s4 51
    layl "回头见，[mc_name]！" with diss
    hide c1p5s4 with diss
    stop bgs fadeout 1.0
    stop bgm fadeout 3.0
    jump c1p6s1

label c1p6s1:
    scene black
    show magic_effect at theme_ember
    with fadeb
    play sfx "sfx/Chapter - In.ogg"
    show c1p6 as c1p6_blur at text_glow
    show c1p6
    with staticflow
    $ save_name = "第1-6章：悲剧"
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide c1p6
    hide c1p6_blur
    hide magic_effect
    with grunge
    pause 0.5
    play bgm "bgm/Tyranny.ogg" fadein 3.0
    play bgs "bgs/City - Evening.ogg" fadein 1.0
    show c1p6s1 1 with diss
    pause 1.0
    mc "（回到医院。）" with diss
    mc "（这次好歹是自己来的。）"
    show c1p6s1 2
    mc "（那是克里斯汀吗？）" with diss
    mc "（她看起来很难过……）"
    show c1p6s1 3
    mc "嗨，克里斯汀。" with diss
    mc "你还好吗？"
    $ CharacterProfile.unlock_outfit([(chara["chri"], 1)])
    show c1p6s1 4
    chri "哦，[mc_name]……嗨。" with diss
    show c1p6s1 5
    mc "你看起来心事重重。" with diss
    mc "想聊聊吗？"
    show c1p6s1 6
    chri "这个……也许吧。" with diss
    show c1p6s1 7
    chri "你还记得我说过在研究神裔吗？" with diss
    show c1p6s1 8
    mc "嗯。" with diss
    mc "怎么了？"
    show c1p6s1 9
    chri "医院收到命令，要交出我的全部研究资料……" with diss
    show c1p6s1 8
    mc "什么？！" with hpunch
    mc "不可能！"
    mc "谁下的，守望者吗？"
    show c1p6s1 9
    chri "不。" with diss
    chri "是王庭。"
    show c1p6s1 8
    mc "国王亲自下的命令？！" with diss
    show c1p6s1 6
    chri "对……" with diss
    show c1p6s1 9
    chri "不过这还不是最糟的……" with diss
    show c1p6s1 7
    chri "{i}所有{/i}医院都被禁止为神裔提供治疗。" with diss
    show c1p6s1 10
    chri "这也都怪我……" with diss
    play sfx "sfx/Cloth2.ogg"
    show c1p6s1 11
    mc "喂，别这么说。" with diss
    mc "守望者是靠自己发现神裔真实存在的。"
    mc "他们本来可以把神裔的事告诉国王。"
    show c1p6s1 12
    chri "你不明白。" with diss
    chri "他们用{i}我的{/i}研究开发出了一种检测方法。"
    chri "现在所有人来看病，都必须先接受检测才能接受治疗。"
    show c1p6s1 13
    chri "如果查出是神裔，他们连治都不会{i}给治{/i}。" with diss
    show c1p6s1 14
    mc "这不是你的错。" with diss
    show c1p6s1 15
    chri "我当初就不该去研究的。" with diss
    chri "我至少可以把所有发现留在脑子里，然后毁掉所有检测手段。"
    show c1p6s1 16
    mc "好吧，是这样。" with diss
    mc "但你做不到的，你没法预知未来。"
    mc "又不是你早就知道或计划了会发生这种事。"
    show c1p6s1 17
    chri "你说得也有道理。" with diss
    show c1p6s1 18
    chri "但我还是觉得这一切糟透了……" with diss
    chri "我本该是帮助人的。"
    chri "帮助{i}所有{/i}人。"
    show c1p6s1 19
    mc "你可能没法公开地帮助神裔，但阿斯塔拉说要是我们再需要，她欢迎你帮忙。" with diss
    mc "说实话，我们几乎肯定还会再需要。"
    show c1p6s1 20
    chri "我愿意，但我可能会因此丢工作。" with diss
    chri "按规定，我不能在监管区域或机构之外行医。"
    show c1p6s1 19
    mc "那就别用医学帮我们……" with diss
    mc "用你的魔法。"
    show c1p6s1 21
    chri "认真的？！" with diss
    chri "我明白了啊！"
    play sfx "sfx/Cloth2.ogg"
    show c1p6s1 22
    chri "你不要我的帮助，因为我是好医生。" with diss
    chri "你要它，因为我是法师。"
    chri "你去吧！"
    play sfx "sfx/Footsteps - Concrete.ogg"
    show c1p6s1 23
    chri "所以我才不想让任何人知道！" with diss
    chri "人们总是想按自己的私心去{i}利用{/i}法师。"
    show c1p6s1 24
    mc "克里斯汀，等等！" with diss
    mc "不是这样的！"
    play sfx "sfx/Footsteps - Concrete.ogg"
    show c1p6s1 25
    chri "哦，是吗？！" with hpunch
    chri "那到底是怎样，[mc_name]？！"
    show c1p6s1 26
    mc "我们要尽可能多地召集神裔，帮他们掌握自己的力量。" with diss
    mc "你也看到了他们中的一个对我做了什么！"
    show c1p6s1 27
    mc "不是所有人都会友善，但我们想帮助那些友善的人！" with diss
    mc "我们会承担很大的风险，但你可以帮我们降低这些风险……"
    show c1p6s1 28
    chri "这是个高尚的目标……" with diss
    show c1p6s1 29
    chri "但我做不到。" with diss
    show c1p6s1 30
    chri "我费了很大力气才让自己的魔法一直保密。" with diss
    chri "也是费了更大的力气才得到这份工作。"
    $ choice1 = ChoiceOption(
            "还记得你前几天跟我说的话吗？", 
            stats={"mc": {"karma": 5}, "chri": {"affection": 5}},
        )
    $ choice2 = ChoiceOption(
            "好啊，那你就让人去死吧！", 
            stats={"mc": {"karma": -5}, "chri": {"affection": -5}},
        )
    $ choice3 = ChoiceOption(
            "算了，至少我试过了。", 
            stats={"chri": {"affection": 3}},
        )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            show c1p6s1 31
            mc "还记得你那天对我说的话吗？" with diss
            mc "想想你用{i}自己的{/i}力量能做成多少{i}好事{/i}。"
        "[choice2.get_display_text()]":
            $ choice2.apply_stats()
            show c1p6s1 31
            mc "行，那就让人去死吧！" with diss
            mc "等他们真的死了，想想今天这场对话！"
            play sfx "sfx/Footsteps - Concrete.ogg"
            show c1p6s1 32
            chri "等等你这个混蛋！" with diss
            chri "你说得对，好吗？！"
        "[choice3.get_display_text()]":
            $ choice3.apply_stats()
            show c1p6s1 31
            mc "好吧，至少我努力过了。" with diss
            mc "再见，克里斯汀。"
            show c1p6s1 33
            chri "等等！" with diss
            chri "别走。"
    show c1p6s1 34
    chri "你说得对……" with diss
    show c1p6s1 30
    chri "我不知道自己刚才为什么那样。" with diss
    chri "对不起。"
    chri "我想是这件事比我以为的更让我难以承受。"
    show c1p6s1 34
    chri "我之所以这么难受，不就是因为他们不让我帮助神裔吗。" with diss
    chri "而看看我，站在这里拒绝唯一可行的解决办法？"
    chri "太蠢了……"
    show c1p6s1 35
    chri "需要我帮忙的时候就打电话给我。" with diss
    chri "好吗？"
    play sfx "sfx/Footsteps - Concrete.ogg"
    show c1p6s1 36
    chri "我现在得回去工作了。" with diss
    show c1p6s1 37
    mc "（刚才本来可以更顺利的……）" with diss
    mc "（不过我不能否认，她是真的很在乎别人。）"
    play sfx "sfx/Whoosh.ogg"
    show c1p6s1 38
    mc "（那股气息又出现了。）" with diss
    mc "（而且离这儿似乎也不算太远。）"
    show c1p6s1 39
    mc "（我知道阿斯塔拉说过这可能很危险，但这也意味着我们更该尽早处理。）" with diss
    mc "（我至少可以先侦察一下这个神裔，看看对手是什么来头。）"
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    hide c1p6s1 with diss
    pause 1.0
    jump c1p6s2

label c1p6s2:
    scene black
    play bgs "bgs/Estate - Night.ogg" fadein 3.0
    play sfx "sfx/Footstep - Leaves.ogg"
    show c1p6s2 1
    mc "（呼……）" with diss
    mc "（这地方比我想象的{i}远{/i}多了……）"
    mc "（不过应该快到了。）"
    show c1p6s2 2
    mc "（嗯？！）" with diss
    mc "（这地方真豪华！）"
    mc "（肯定是哪个有钱的混账住这儿。）"
    play sfx "sfx/Whoosh.ogg"
    show c1p6s2 3
    mc "（凑近了看，这气息大得多！）" with diss
    mc "（看起来在上面某一层。）"
    show c1p6s2 4
    mc "（看来得爬楼了。）" with diss
    show c1p6s2 5
    mc "（我可以敲门，但感觉那样可能会很糟。）" with diss
    mc "（毕竟这次只是来侦察。）"
    hide c1p6s2 with diss
    pause 1.0
    play sfx "sfx/Leaves Rustle.ogg"
    show c1p6s2 6 with diss
    pause 1.0
    show c1p6s2 7
    mc "（到了。）" with diss
    mc "（现在看看……）"
    show c1p6s2 8
    mc "（该死……这地方真不错！）" with diss
    show c1p6s2 9
    mc "（是个女人。）" with diss
    mc "（看看是不是我们要找的那个神裔……）"
    stop bgs fadeout 1.0
    play sfx "sfx/Whoosh.ogg"
    show c1p6s2 10a with diss
    play sfx2 "sfx/Heartbeat - Scared.ogg" volume 2.0
    pause 0.1
    play bgm "bgm/Despair.ogg" fadein 1.0 volume 1.2
    show c1p6s2 10
    mc "（不会吧……）" with diss
    mc "（我得赶紧离开。）"
    show c1p6s2 11 with dism
    pause 0.5
    show c1p6s2 12 with diss
    pause 0.5
    play sfx "sfx/Dark - Summon.ogg"
    show c1p6s2 13
    mc "（嗯？！）" with diss
    play sfx "sfx/Dark - Pull.ogg"
    show c1p6s2 14
    mc "不妙！" with hpunch
    hide c1p6s2 with diss
    pause 1.0
    play sfx "sfx/Dark - Push.ogg"
    show c1p6s2 15 with hpunch
    play sfx2 "sfx/Table - Slam.ogg"
    pause 1.0
    show c1p6s2 16
    mc "哦，糟了……" with diss
    show c1p6s2 17
    mc "这下不好办了。" with diss
    show c1p6s2 18
    unkn "你为什么监视我？！" with diss
    show c1p6s2 19
    mc "（该死！）" with diss
    show c1p6s2 20
    unkn "怎么样？！" with diss
    unkn "回答我！"
    play sfx "sfx/Cloth2.ogg"
    show c1p6s2 21
    mc "我没有监视你！" with diss
    show c1p6s2 22
    mc "好吧，我确实有点在监视……" with diss
    mc "但不是你想的那种原因！"
    show c1p6s2 23
    unkn "我看我父亲又派了他手下的一个走狗来！" with hpunch
    unkn "还是说，你就是个变态色狼！"
    show c1p6s2 22
    mc "我不是谁派来的！" with diss
    mc "来这里是我自己的选择！"
    mc "我也不是什么变态！"
    show c1p6s2 24
    unkn "是啊，才怪……" with diss
    play sfx "sfx/Dark - Summon.ogg"
    play sfx2 "sfx/Blood - Sheath.ogg"
    show c1p6s2 25
    unkn "说实话！" with hpunch
    unkn "现在！"
    unkn "我父亲为什么又派人监视我？！"
    show c1p6s2 26
    mc "这、这才是真相！" with diss
    mc "我连你父亲是谁都不知道！"
    play sfx "sfx/Blood - Sheath.ogg"
    stop bgm fadeout 3.0
    show c1p6s2 27
    mc "（谢天谢地！）" with diss
    show c1p6s2 28
    unkn "我看得出你是诚实的。" with diss
    show c1p6s2 29
    unkn "那你为什么在我窗外往里看？" with diss
    show c1p6s2 30
    unkn "话说回来，你是怎么找到这个地方的？" with diss
    unkn "这里在任何地图上都没有……而且藏得很严实。"
    show c1p6s2 28
    unkn "那是父亲确保的。" with diss
    show c1p6s2 31
    mc "我是跟着你的气息来的。" with diss
    mc "它把我带到了这里。"
    show c1p6s2 28
    unkn "我的气息？" with diss
    show c1p6s2 31
    mc "对。" with diss
    mc "我也是神裔。"
    show c1p6s2 32
    unkn "荒谬。" with diss
    unkn "几百年前神裔就随着诸神一起灭绝了。"
    show c1p6s2 33
    unkn "等等……" with diss
    unkn "你说「也」是什么意思？"
    show c1p6s2 34
    mc "和你一样，我也是神裔。" with diss
    show c1p6s2 35
    mc "（天哪，我比阿斯塔拉当时还不如……）" with diss
    mc "（我真该对她宽容一点。）"
    show c1p6s2 28
    unkn "我{i}不是{/i}神裔，我是法师。" with diss
    show c1p6s2 31
    mc "神裔没有灭绝，你也不是法师。" with diss
    mc "光看你的气息我就能分辨。"
    play sfx "sfx/Door - Heavy - Open.ogg"
    show c1p6s2 36
    unkn "小姐！" with hpunch
    unkn "您没事吧？！"
    play bgm "bgm/UhOh.ogg"
    show c1p6s2 37 with diss
    pause 1.0
    show c1p6s2 38
    unkn "{i}*倒吸一口气*{/i}" with hpunch
    show c1p6s2 39
    unkn "他不可能在这里！" with diss
    play sfx "sfx/Footsteps - Wood - Fast.ogg"
    show c1p6s2 40
    unkn "我这就把他请出去，然后叫骑士！" with diss
    show c1p6s2 41
    mc "（骑士？！）" with diss
    play sfx "sfx/Cloth2.ogg" volume 1.5
    show c1p6s2 42 with hpunch
    pause 1.0
    play sfx "sfx/Throw.ogg"
    show c1p6s2 43 with hpunch
    pause 1.0
    play sfx "sfx/Body - Drag.ogg"
    show c1p6s2 44
    mc "（这老家伙强得离谱！）" with diss
    show c1p6s2 45
    unkn "巴思，等等！" with hpunch
    show c1p6s2 46
    unkn "先别把他扔出去。" with diss
    unkn "也别叫骑士！"
    stop bgm fadeout 3.0
    show c1p6s2 47
    barth "我必须这么做，小姐！" with diss
    barth "您知道一旦被人发现会怎样！"
    show c1p6s2 48
    unkn "可这里只有我们！" with diss
    show c1p6s2 49
    barth "您父亲的眼线到处都是！" with diss
    barth "我们不能冒险！"
    show c1p6s2 50 with diss
    pause 0.5
    show c1p6s2 51 with diss
    pause 0.5
    play sfx "sfx/Dark - Closing In.ogg"
    play sfx2 "sfx/Earth - Rumbling.ogg" loop
    show c1p6s2 52 at hpunchr
    with diss
    pause 0.1
    show c1p6s2 53 at hpunchs
    with diss
    pause 0.1
    play sfx "sfx/Dark - Summon.ogg"
    show c1p6s2 54 at hpunchs
    with diss
    pause 0.1
    show c1p6s2 55 at hpunchs
    with diss
    pause 0.1
    play sfx "sfx/Dark - Summon.ogg"
    show c1p6s2 56 at hpunchs
    with diss
    stop sfx2 fadeout 2.0
    pause 1.0
    show c1p6s2 57
    barth "小姐，您必须立刻阻止他！" with diss
    show c1p6s2 58 with diss
    pause 0.5
    show c1p6s2 59
    unkn "现在我父亲的眼线就看不到任何东西了……" with diss
    show c1p6s2 60
    unkn "放开他。" with diss
    unkn "这是命令。"
    show c1p6s2 61
    barth "呃……" with diss
    play sfx "sfx/Cloth2.ogg" volume 1.2
    show c1p6s2 62 with diss
    pause 0.5
    play sfx2 "sfx/Table - Slam.ogg"
    show c1p6s2 63
    barth "是，小姐……" with hpunch
    show c1p6s2 64
    barth "等令尊得知此事时……" with diss
    show c1p6s2 65
    barth "……别说我没有尽力阻止。" with diss
    show c1p6s2 66
    unkn "我不会有事的，巴思。" with diss
    unkn "不会有人发现的。"
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s2 67
    barth "既然您这么说……" with diss
    play sfx "sfx/Door - Heavy - Open.ogg"
    show c1p6s2 68 with diss
    pause 1.0
    show c1p6s2 69
    $ CharacterProfile.unlock_profile([chara["barth"]])
    unkn "我为巴塞洛缪道歉……" with diss
    unkn "他只是太护着我了。"
    unkn "现在，把你刚才的话说完。"
    show c1p6s2 70
    mc "嗯……好吧。" with diss
    show c1p6s2 71
    mc "你的气息是神裔的，不是法师的。" with diss
    mc "如果不是这样，我根本找不到这个地方，也找不到你。"
    show c1p6s2 72
    unkn "我凭什么相信这些？" with diss
    show c1p6s2 71
    mc "我觉得你其实已经相信了。" with diss
    mc "只是你不愿意接受。"
    mc "相信我，我也经历过。"
    mc "我得被从大概五十层楼高的地方扔下去，才终于相信。"
    show c1p6s2 73
    unkn "而你居然活下来了？！" with diss
    show c1p6s2 74
    mc "对，神裔好像挺能扛的。" with diss
    show c1p6s2 75
    unkn "哦……" with diss
    show c1p6s2 76
    mc "那你相信我了吗？" with diss
    show c1p6s2 77
    unkn "我相信你{i}不是{/i}变态。" with diss
    unkn "但我只觉得你疯了。"
    show c1p6s2 78
    mc "有可能。" with diss
    show c1p6s2 79
    unkn "我也相信，如果我父亲发现有不被允许的人来过这里，他会往这儿降下各种天罚。" with diss
    show c1p6s2 80
    unkn "你最好走了。" with diss
    unkn "不过就从窗户出去。"
    show c1p6s2 78
    mc "但我认识一个人，能帮你更好地了解自己是什么！" with diss
    show c1p6s2 81
    unkn "……" with diss
    show c1p6s2 80
    unkn "明天晚上这个时间再来。" with diss
    unkn "我需要想一整天。"
    show c1p6s2 78
    mc "好吧，合理。" with diss
    mc "那我就先走了。"
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s2 82 with diss
    pause 1.0
    show c1p6s2 83
    $ CharacterProfile.unlock_profile([chara["mela"]])
    mela "对了，我叫梅拉妮。" with diss
    show c1p6s2 84
    mc "我是[mc_name]。" with diss
    show c1p6s2 85
    mela "很高兴认识你，[mc_name]。" with diss
    mela "回去的路上小心别被人看见。"
    show c1p6s2 84
    mc "我会的。" with diss
    hide c1p6s2
    scrn "回到家、上床睡觉之后……" with diss
    call primordial3 from _call_primordial3
    jump c1p6s3

label c1p6s3:
    scene black
    play bgm "bgm/Astara's Home.ogg" fadein 1.0
    show c1p6s3 1 with diss
    pause 1.0
    show c1p6s3 2
    asta "所以你之前看到的那个怪东西，叫作原初者？" with diss
    show c1p6s3 3
    mc "对，它是这么说的。" with diss
    show c1p6s3 4
    asta "我本想帮上更多忙，但我完全不知道原初者是什么。" with diss
    asta "这是我第一次听说它们。"
    show c1p6s3 5
    asta "下次见到和我说话的那位女神时，我可以问问她。" with diss
    show c1p6s3 3
    mc "希望她知道点什么。" with diss
    mc "这一切让我越来越糊涂了。"
    mc "我只想要答案。"
    show c1p6s3 6
    asta "我相信答案会来的。" with diss
    asta "耐心一点。"
    show c1p6s3 3
    mc "我在努力了。" with diss
    mc "不过这对我来说很难。"
    show c1p6s3 7
    asta "我当然知道。" with diss
    show c1p6s3 8
    mc "你这话什么意思？" with diss
    show c1p6s3 9
    asta "别以为我没注意到昨晚你的气息出现在那个红色气息旁边。" with diss
    show c1p6s3 3
    mc "哦……" with diss
    show c1p6s3 2
    asta "你显然还活着，所以我想你没有被发现。" with diss
    asta "又或者你被发现了，只是运气好，碰上了一个不具敌意的神裔。"
    show c1p6s3 3
    mc "我被发现了，不过对，她没有敌意。" with diss
    mc "嗯……也不能说完全没有。"
    mc "不过她真的很会控制自己的力量。"
    show c1p6s3 10
    asta "她的是什么力量？" with diss
    show c1p6s3 11
    mc "不太好说。" with diss
    mc "她能操控影子，还有一度从手里射出一把刀，看起来像是由凝固的血液构成的。"
    show c1p6s3 4
    asta "两种不同的魔法……" with diss
    asta "有意思。"
    show c1p6s3 3
    mc "和她的力量无关，她似乎是某种贵族。" with diss
    show c1p6s3 12
    asta "贵族？" with diss
    asta "你为什么会这么觉得？"
    show c1p6s3 13
    mc "她住的那座宅邸相当气派，穿着昂贵的衣服，还有一名管家。" with diss
    show c1p6s3 14
    asta "嗯，听起来确实像贵族。" with diss
    show c1p6s3 2
    asta "还有别的吗？" with diss
    asta "你有没有和她谈过加入我们、以及加入我们找到的其他神裔的事？"
    show c1p6s3 3
    mc "算是吧。" with diss
    mc "我很难说服她自己不是法师。"
    pause 1.0
    mc "说起来……" with diss
    mc "你当初劝我的时候，我态度很糟，真的很抱歉。"
    show c1p6s3 5
    asta "道歉我收下了。" with diss
    asta "但那现在不重要。"
    show c1p6s3 12
    asta "最后你说服她了吗？" with diss
    show c1p6s3 13
    mc "我想可能说服了。" with diss
    mc "她要我今晚再去一趟，大概是想再谈谈。"
    show c1p6s3 5
    asta "那我和你一起去。" with diss
    show c1p6s3 3
    mc "我觉得那不是个好主意。" with diss
    mc "她和她的管家似乎都很不希望有别人在场。"
    mc "带你去可能会让事情更麻烦。"
    show c1p6s3 5
    asta "好吧。" with diss
    asta "那就祝你自己成功。"
    show c1p6s3 3
    mc "我会尽力的。" with diss
    show c1p6s3 9
    asta "哦！" with diss
    asta "我也有事要告诉你！"
    show c1p6s3 5
    asta "雷恩让你今天去健身房继续上课。" with diss
    show c1p6s3 3
    mc "哦，好。" with diss
    mc "那我现在就过去。"
    show c1p6s3 5
    asta "好。" with diss
    asta "谢谢你把那个神裔的事告诉我。"
    show c1p6s3 3
    mc "不客气。" with diss
    stop bgm fadeout 3.0
    hide c1p6s3
    scrn "你离开阿斯塔拉的公寓，前往健身房。" with diss
    jump c1p6s4

label c1p6s4:
    scene black
    play bgm "bgm/Fitness.ogg" fadein 2.0
    show c1p6s4 1
    rayn "终于来了！" with diss
    rayn "我等了一上午了！"
    show c1p6s4 2
    mc "抱歉。" with diss
    mc "一听说你在找我，我就赶过来了。"
    show c1p6s4 3
    rayn "没关系。" with diss
    rayn "我只是想重新评估一下你的格斗能力。"
    rayn "这次我要你认真对待。"
    show c1p6s4 2
    mc "我上次很认真了好吗！" with diss
    show c1p6s4 4
    rayn "放屁！" with diss
    rayn "你当我傻吗？！"
    rayn "你的技术几乎无懈可击！"
    show c1p6s4 5
    rayn "我在脑子里把我们的交手过了越多遍，就越意识到你的输是故意的！" with diss
    show c1p6s4 4
    rayn "你在强迫自己打得很差！" with diss
    show c1p6s4 6
    mc "好吧，被你发现了！" with diss
    mc "我确实留手了。"
    show c1p6s4 7
    rayn "什么？！" with diss
    rayn "你该不会觉得我应付不了你，只因为我个子小而且没有小鸡鸡吧？！"
    rayn "是这样吗？！"
    show c1p6s4 6
    mc "才不是！完全不是！" with diss
    mc "我是想让你觉得，是你帮我提高了，所以我就一点点把这一切更认真地对待。"
    show c1p6s4 8
    rayn "这番好意不错，但我不需要那种傻乎乎的信心加成。" with diss
    rayn "我可不想浪费时间去教一个水平已经和我持平甚至更高的人。"
    show c1p6s4 9
    rayn "再来一场切磋，这次认真点。" with diss
    rayn "我必须知道你到底有多强。"
    show c1p6s4 2
    mc "好。" with diss
    mc "这次我不留手。"
    show c1p6s4 10
    rayn "很好。" with diss
    rayn "去换衣服，我们开始。"
    hide c1p6s4 with diss
    pause 1.0
    show c1p6s4 11
    rayn "准备好了？" with diss
    stop bgm fadeout 1.0
    stop bgs fadeout 1.0
    show c1p6s4 12
    mc "好了。" with diss
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p6s4 13
    rayn "（糟了！）" with hpunch
    rayn "（他这次快了好多！）"
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p6s4 14 with hpunch
    pause 0.1
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p6s4 15
    rayn "（我几乎完全反应不过来！）" with hpunch
    show c1p6s4 16
    rayn "没想到你这么{i}强{/i}。" with diss
    rayn "我得加把劲了。"
    show c1p6s4 17
    mc "喂！" with diss
    mc "我要是不能留手，你也不能！"
    show c1p6s4 18
    rayn "我不会再留手了！" with diss
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p6s4 19 with hpunch
    pause 0.1
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p6s4 20 with hpunch
    pause 0.1
    show c1p6s4 21 with diss
    pause 0.1
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p6s4 22 with hpunch
    pause 0.1
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p6s4 23 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p6s4 24 with hpunch
    pause 0.05
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p6s4 25 with hpunch
    pause 0.05
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p6s4 26 with hpunch
    pause 0.05
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p6s4 27 with diss
    pause 0.1
    play sfx "sfx/Fight - Punch - Hit.ogg"
    show c1p6s4 28 with hpunch
    pause 0.05
    show c1p6s4 29
    rayn "（该死……）" with diss
    rayn "（好疼！）"
    rayn "（他怎么越来越快？！）"
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p6s4 30
    rayn "（不只是快，整体都更强了！）" with hpunch
    rayn "（就好像他在从我的动作里学习……）"
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p6s4 31
    rayn "（……并且实时地适应它们！）" with hpunch
    show c1p6s4 32
    rayn "（他太厉害了！）" with diss
    hide c1p6s4 with diss
    pause 1.0
    play sfx "sfx/Table - Slam.ogg"
    show c1p6s4 33 with hpunch
    pause 1.0
    show c1p6s4 34
    mc "你认输吗？" with diss
    show c1p6s4 35
    rayn "（哇，他居然真的赢了我。）" with diss
    rayn "（通常这样毫无还手之力会让我生气……）"
    show c1p6s4 36
    rayn "（可对他，却……）" with diss
    show c1p6s4 37
    rayn "（我该不会因为这个兴奋起来了吧？！）" with hpunch
    show c1p6s4 38
    rayn "对……" with diss
    rayn "我、我认输。"
    show c1p6s4 39
    rayn "现在能从我身上起来了吗？" with diss
    play sfx "sfx/Cloth2.ogg" volume 2.0
    show c1p6s4 40
    mc "哦，对……抱歉。" with diss
    show c1p6s4 41
    mc "你打得很好。" with diss
    show c1p6s4 42
    rayn "谢谢。" with diss
    show c1p6s4 43
    rayn "这下定了……" with diss
    rayn "我不打算训练你了。"
    show c1p6s4 41
    mc "哎，别啊！" with diss
    mc "别因为赢了一场就耍赖不教我！"
    show c1p6s4 42
    rayn "我不是耍赖。" with diss
    rayn "我只是觉得我教不了你什么。"
    show c1p6s4 41
    mc "我们至少还能偶尔切磋吗？" with diss
    show c1p6s4 44
    rayn "好啊，听起来不错。" with diss
    show c1p6s4 45
    rayn "你怎么能那么强？" with diss
    rayn "连塞拉斯都没这么打。"
    show c1p6s4 41
    mc "塞拉斯教了我足够的基础，让我能发展出自己的风格。" with diss
    mc "这些年当他的学生时，我一直在慢慢磨炼它。"
    show c1p6s4 45
    rayn "你发展出了自己的风格？" with diss
    show c1p6s4 42
    rayn "而我前几天还在跟你讲格斗是什么鬼。" with diss
    show c1p6s4 43
    rayn "我真是个白痴。" with diss
    show c1p6s4 41
    mc "你不蠢。" with diss
    mc "要怪就怪我藏着自己真实的实力。"
    mc "我本该坦白一点的。"
    show c1p6s4 44
    rayn "别放心上。" with diss
    rayn "我去冲个澡然后回家。"
    rayn "谢谢你认真对待这场切磋。"
    rayn "你让我知道自己还有太多要学。"
    show c1p6s4 46
    mc "不客气。" with diss
    mc "我也去冲个澡。"
    hide c1p6s4 with diss
    pause 1.0
    jump c1p6s5

label c1p6s5:
    scene black
    play sfx "sfx/Shower - On.ogg"
    show c1p6s5 1 with diss
    pause 1.0
    play sfx2 "sfx/Shower - Loop.ogg" loop
    show c1p6s5 2
    mc "（雷恩好像很坦然地接受了这败。）" with diss
    show c1p6s5 3
    mc "（她不想再教我，这真让人难受……）" with diss
    mc "（不过她认为教不了我什么，多半是对的。）"
    mc "（至少她还愿意跟我切磋。）"
    show c1p6s5 4
    mc "（好的一面是，塞拉斯也许会开始教我了。）" with diss
    play sfx "sfx/Footsteps - Tile - Bare.ogg" volume 2.0
    pause 1.0
    show c1p6s5 5
    mc "（我以为这里只有我一个男的。）" with diss
    mc "（肯定是别人也来了。）"
    show c1p6s5 6
    mc "（算了，反正我也没打算在淋浴间唱歌。）" with diss
    show c1p6s5 7
    mc "（我快点洗完出去吧。）" with diss
    rayn "嘿[mc_name]，我跟你一起洗行吗？" with diss
    $ choice1 = ChoiceOption(
            "那还是算了。",
            stats={"rayn": {"affection": 5}},
            path_info=("rayn", "Lewd Scene")
        )
    $ choice2 = ChoiceOption(
            "你疯了吗？才没有！",
            stats={"rayn": {"affection": -5}},
        )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            $ rayngw = True
            show c1p6s5 8
            mc "应该可以吧。" with diss
            play sfx "sfx/Door - Shower.ogg"
            show c1p6s5 10
            mc "所以？" with diss
            mc "你想干什么？"
            show c1p6s5 11
            rayn "洗澡啊，废话。" with diss
            show c1p6s5 12
            mc "哦，真的吗？" with diss
            mc "别的淋浴间多的是。"
            mc "尤其是{i}女{/i}更衣室里那个。"
            show c1p6s5 13
            rayn "抱歉，我说明白一点。" with diss
            show c1p6s5 14
            rayn "我是想{i}和{/i}你{i}一起{/i}洗。" with diss
            call rayn_gettinwet from _call_rayn_gettinwet
            $ CharacterProfile.unlock_memory([(chara["rayn"], "rayngw")])
        "[choice2.get_display_text()]":
            $ choice2.apply_stats()
            show c1p6s5 8
            mc "你疯了吗？！" with hpunch
            mc "没有！"
            show c1p6s5 15
            rayn "啧！" with diss
            rayn "随便你，老兄！"
            rayn "你是我见过最奇怪的男人！"
            rayn "好多{i}真男人{/i}求之不得呢！"
            stop bgm fadeout 1.0
            stop sfx2 fadeout 1.0
            hide c1p6s5 with diss
            pause 1.0
    jump c1p6s6

label c1p6s6:
    scene black
    play bgm "bgm/Fitness.ogg" fadein 2.0
    if rayngw:
        show c1p6s6 1 with diss
        pause 1.0
        show c1p6s6 2
        rayn "我得去换上我的衣服。" with diss
        show c1p6s6 3
        rayn "等我一下？" with diss
        show c1p6s6 4
        mc "好啊。" with diss
        play sfx "sfx/Footsteps - Wood.ogg"
        show c1p6s6 5
        rayn "酷。" with diss
        rayn "马上就回来。"
        show c1p6s6 6 with diss
        pause 1.0
        show c1p6s6 7
        sila "我什么都不打算说了。" with diss
        show c1p6s6 8
        mc "真的很抱歉。" with diss
        mc "那是一时冲动的事。"
        mc "还有——"
        show c1p6s6 9
        sila "老兄，放松！" with hpunch
        sila "我一点都没生气。"
        show c1p6s6 10
        sila "我甚至有点自豪。" with diss
        sila "能证明你把我的建议当回事真的很好……"
        show c1p6s6 11
        sila "……虽然这份证明把我烫得够呛。" with diss
        show c1p6s6 12
        sila "总之，我要去洗洗眼睛。" with diss
        play sfx "sfx/Footsteps - Wood.ogg"
        show c1p6s6 13 with diss
        pause 1.0
        play sfx "sfx/Footsteps - Wood.ogg"
        show c1p6s6 14 with diss
        $ CharacterProfile.unlock_outfit([(chara["rayn"], 1)])
        pause 1.0
        show c1p6s6 15
        rayn "哦，太好了，塞拉斯已经走了。" with diss
        show c1p6s6 16
        rayn "我现在太丢脸了，没法直视他……" with diss
        rayn "我从来不想让他看到我那样。"
        show c1p6s6 17
        mc "我也是。" with diss
        show c1p6s6 18
        rayn "而且塞拉斯对我来说就像亲哥哥一样，所以更难受。" with diss
        rayn "在我……之后，他收留了我。"
    else:
        play sfx "sfx/Footsteps - Wood.ogg"
        show c1p6s6 14 with diss
        $ CharacterProfile.unlock_outfit([(chara["rayn"], 1)])
        pause 1.0
        show c1p6s6 15
        rayn "嘿，[mc_name]……" with diss
        rayn "我只是想过来为刚才的态度道歉。"
        show c1p6s6 16
        rayn "我不知道自己怎么了……" with diss
        show c1p6s6 17
        mc "别放在心上。" with diss
        mc "我没生气什么的，只是不巧在不合适的时间、合适的地点。"
        show c1p6s6 16
        rayn "是啊……" with diss
        rayn "我该想到你可能会因为那是在公共场所而不自在。"
        show c1p6s6 15
        rayn "要是被塞拉斯发现，我自己也会很丢脸，毕竟他对我像哥哥一样。" with diss
        show c1p6s6 19
        mc "话说你们两个到底什么关系？" with diss
        mc "他好像很了解你。"
        show c1p6s6 18
        rayn "说来话长，不过我想我信你信到能讲给你听。" with diss
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    show c1p6s6 20
    rayn "你知道吗？" with diss
    rayn "算了。"
    rayn "我不该拿这些细节来烦你。"
    rayn "那些不重要。"
    show c1p6s6 21
    mc "我觉得挺重要的。" with diss
    mc "不然你为什么要提起？"
    show c1p6s6 15
    rayn "{i}*叹气*{/i} 好吧……" with diss
    rayn "你说得对。"
    rayn "能跟塞拉斯以外的人聊聊这件事，感觉很不错。"
    show c1p6s6 22
    rayn "还记得我们第一次切磋之后你问我魔法的事吗？" with diss
    show c1p6s6 23
    mc "当然记得。" with diss
    mc "那正是我被带来这里的全部原因，也是我们相遇的缘由。"
    show c1p6s6 24
    rayn "那个我帮不了你、现在也{i}依然{/i}帮不了你的原因——" with diss
    play bgm "bgm/Troubled Past.ogg" fadein 1.0
    show c1p6s6 25
    rayn "——是我{i}曾经{/i}是个法师……但现在不是了。" with diss
    rayn "我从来没机会学到魔法究竟是什么，也不知道怎么用。"
    show c1p6s6 26
    mc "我原以为一旦觉醒了魔法力量，就永远是法师了。" with diss
    show c1p6s6 27
    rayn "那{i}曾经{/i}确实是这样。" with diss
    rayn "直到某家大公司发现了剥离人类魔力的方法。"
    show c1p6s6 28
    mc "这有可能？！" with hpunch
    mc "怎么可能？！"
    show c1p6s6 29
    rayn "那个手术还在实验阶段，侵入性极强，对接受手术的人来说绝对不好受。" with diss
    show c1p6s6 28
    mc "那为什么会有人自愿去做？" with diss
    show c1p6s6 30
    rayn "{i}我{/i}没有选择……" with diss
    hide c1p6s6
    call raynbstory from _call_raynbstory
    show c1p6s6 27
    rayn "就那样。" with diss
    rayn "我是那么小的年纪里第一个拥有魔力的人……"
    show c1p6s6 29
    rayn "……也是第一个失去魔力的人……" with diss
    stop bgm fadeout 5.0
    show c1p6s6 28
    mc "唉，雷恩，我真的很抱歉。" with diss
    show c1p6s6 15
    rayn "谢谢你，[mc_name]……" with diss
    show c1p6s6 18
    rayn "总之，我十六岁能自己生活之后就走了。" with diss
    rayn "我不在乎那意味着流落街头、为了吃顿饭沿街乞讨。"
    show c1p6s6 22
    rayn "然后，流落街头几天后，塞拉斯看到我正在对付几个心怀不轨的恶徒，就觉得我的潜力值得投资。" with diss
    rayn "他把家让给了我住，后来我够格了，就让我在这儿当教练。"
    show c1p6s6 21 
    mc "哇……" with diss
    mc "我真不知道该说什么。"
    mc "但我想我{i}能{/i}说什么其实也帮不上忙。"
    show c1p6s6 24
    rayn "没关系。" with diss
    rayn "你说得对，我说什么都没用，但能有人聊聊这件事，比你想象的要有帮助。"
    rayn "而且是塞拉斯以外的人。"
    show c1p6s6 22
    rayn "所以，谢谢你听我这个悲惨的故事。" with diss
    show c1p6s6 24
    rayn "我想我该走了。" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s6 31
    rayn "回见，[mc_name]。" with diss
    show c1p6s6 32
    mc "（看来那就是塞拉斯说的她那种「干劲」……）" with diss
    mc "（我越了解这些公司，以及国王纵容和默许的那些事，就越意识到这个世界有多烂。）"
    mc "（我开始明白原初者所说的「公司势力膨胀」是什么意思了。）"
    show c1p6s6 33
    mc "（天，我整个心情都被拉下去了。）" with diss
    mc "（真希望我能把力量给她，因为我本来就不想要。）"
    play sfx "sfx/Footsteps - Wood.ogg"
    play bgs "bgs/Gym.ogg"
    play bgm "bgm/Fitness.ogg" fadein 5.0
    show c1p6s6 34
    sila "嘿，[mc_name]！" with diss
    sila "我还以为你已经走了。"
    show c1p6s6 35
    mc "本来是准备走的，但雷恩想先跟我聊聊。" with diss
    mc "知道她第一次上课后没教我魔法，我还抱怨她，现在觉得自己真渣。"
    show c1p6s6 36
    sila "哦！" with diss
    sila "她告诉你了！"
    show c1p6s6 37
    sila "我从没见她这么快就信任一个人。" with diss
    sila "她一定真的很喜欢你。"
    show c1p6s6 38
    sila "不过这事确实要慢慢消化。" with diss
    show c1p6s6 39
    sila "我说过的，如果你背负着驱动她的一切，就不会再想要她那种干劲。" with diss
    show c1p6s6 40
    mc "是啊……绝对不想要。" with diss
    mc "真不敢相信有人会把自己的孩子送去那种地方。"
    show c1p6s6 41
    sila "我也一样，兄弟。" with diss
    show c1p6s6 42
    sila "更糟的是，我知道全部真相后试着让守望者介入。" with diss
    sila "他们说无能为力，因为父母对孩子任何「医疗」事务都有完全支配权。"
    sila "所以我举报了他们的罪行，他们却立刻、连调查都没做，就说是毫无根据的指控。"
    show c1p6s6 43
    sila "他们根本没查！" with hpunch
    show c1p6s6 44
    sila "阿斯塔拉做了些调查，发现雷恩家有好几个守望者在拿他们的薪水。" with diss
    show c1p6s6 45
    mc "等等，阿斯塔拉知道雷恩的过去？" with diss
    show c1p6s6 41
    sila "据我所知不知道，只有你和我。" with diss
    show c1p6s6 35
    mc "有意思……" with diss
    play sfx "sfx/Phone - MC - Ringtone.ogg" loop
    show c1p6s6 46 with diss
    pause 1.0
    show c1p6s6 47 with diss
    pause 1.0
    stop sfx
    show c1p6s6 48
    mc "喂？" with diss
    show c1p6s6 49
    soul "嘿，[mc_name]，我是索尔。" with pushl
    soul "你在哪儿？"
    show c1p6s6 50
    mc "我在弹性健身，怎么了？" with pushr
    mc "有什么事？"
    show c1p6s6 49
    soul "有件重要的事我们得谈谈。" with pushl
    soul "是关于那晚我们发现的、关于你力量的事。"
    show c1p6s6 51
    mc "是坏事吗？" with pushr
    mc "我今天可不想再被拉低心情了。"
    show c1p6s6 52
    soul "不，不是坏事。" with pushl
    show c1p6s6 53
    soul "要说的话，反而是好事。" with diss
    show c1p6s6 50
    mc "哦，那好。" with pushr
    mc "你想在哪儿见？"
    show c1p6s6 49
    soul "你不用来。" with pushl
    soul "我过去找你。"
    show c1p6s6 50
    mc "哦，那好吧。" with pushr
    mc "你现在在路上了吗？"
    show c1p6s6 49
    soul "没有，不过一两分钟后我就到。" with pushl
    soul "我正要下班。"
    show c1p6s6 54
    soul "一会儿见！" with diss
    play sfx "sfx/Phone Hangup.ogg"
    show c1p6s6 37
    sila "没事吧？" with pushr
    show c1p6s6 35
    mc "嗯。" with diss
    if soul_sd:
        mc "那是索尔，就是我跟你提过、给过我和你类似建议的那个人。"
    else:
        mc "那是索尔，她是一直在帮我处理神裔这些事的朋友。"
    show c1p6s6 37
    sila "哦，明白了。" with diss
    show c1p6s6 38
    sila "所以你就要走了，对吧？" with diss
    show c1p6s6 35
    mc "不，她要来这里。" with diss
    show c1p6s6 37
    sila "哦，太好了！" with diss
    sila "能认识她很有意思！"
    hide c1p6s6
    jump c1p6s7

label c1p6s7:
    scene black
    scrn "索尔来到健身房……" with diss
    show c1p6s7 1
    $ CharacterProfile.unlock_outfit([(chara["soul"], 1)])
    soul "嘿，[mc_name]！" with diss
    soul "抱歉来晚了一会儿。"
    soul "我得先换掉工作服。"
    show c1p6s7 2
    mc "没关系。" with diss
    mc "塞拉斯一直陪着我呢。"
    if soul_sd:
        show c1p6s7 3
        sila "你就是那位有名的索尔。" with diss
        sila "听说你的目标和我很相似。"
        show c1p6s7 4
        soul "我的目标？" with diss
        show c1p6s7 5
        sila "对！" with diss
        sila "把这个笨蛋开导开来，让他愿意跟不同的人尝试新东西！"
        show c1p6s7 6
        soul "哦……" with diss
        soul "好吧，这么说确实也算我的一个目标。"
        soul "不过不是主要目标。"
    else:
        show c1p6s7 3
        sila "很高兴认识你。" with diss
        show c1p6s7 4
        soul "我也是！" with diss
    show c1p6s7 7
    sila "好了，你们俩先聊你们要聊的。" with diss
    sila "到吃汉堡的时间了！"
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s7 8 with diss
    pause 1.0
    show c1p6s7 9
    soul "他人不错。" with diss
    soul "你们认识很久了？"
    show c1p6s7 10
    mc "算是吧……" with diss
    mc "我们几年前是朋友，后来因为我太忙就渐渐疏远了。"
    mc "最近才重新开始一起玩，但好像什么都没变。"
    mc "他是个好朋友。"
    show c1p6s7 11
    soul "我明白了。" with diss
    show c1p6s7 12
    soul "有没有更私密一点的地方可以聊？" with diss
    show c1p6s7 13
    mc "有。" with diss
    mc "瑜伽室应该没人。"
    show c1p6s7 14
    mc "跟我来。" with diss
    stop bgm fadeout 3.0
    play bgs "bgs/Gym.ogg" volume 0.05
    hide c1p6s7 with diss
    pause 1.0
    play bgm "bgm/Inner Tranquility.ogg" fadein 3.0
    show c1p6s7 15
    mc "对，一个人都没有。" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s7 16
    soul "很好。" with diss
    show c1p6s7 17
    soul "我联系了一个在智者们身边学习魔法的朋友。" with diss
    soul "他觉得那——"
    show c1p6s7 18
    mc "智者？！" with diss
    show c1p6s7 19
    mc "你是说{i}那些{/i}智者？！" with diss
    mc "就是{i}魔法{/i}的智者？！"
    show c1p6s7 20
    soul "对……" with diss
    soul "怎么了？"
    show c1p6s7 21
    mc "我只是好奇。" with diss
    mc "我不知道他们还收学生。"
    show c1p6s7 22
    soul "一般来说他们不收，不过其中一位病重垂危。" with diss
    soul "他们在教我朋友成为他的接班人。"
    show c1p6s7 23
    mc "他们不都是几百岁了吗？" with diss
    mc "我以为他们是不死的。"
    show c1p6s7 24
    soul "[mc_name]……你跑题了。" with diss
    show c1p6s7 25
    soul "我是来谈你的，不是谈智者的。" with diss
    show c1p6s7 26
    mc "你说得对，抱歉。" with diss
    mc "接下来我只听，除非你问我问题。"
    show c1p6s7 27
    soul "谢谢。" with diss
    show c1p6s7 28
    soul "总之，我那个朋友进了智者的图书馆，找到了一些非常古老的、关于神裔的日记。" with diss
    show c1p6s7 29
    soul "据说，{i}最初的诸神{/i}并不像后世诸神那样一开始就是神裔。" with diss
    show c1p6s7 30
    soul "他们只是凭空一下子就有了神力。" with diss
    show c1p6s7 31
    soul "这一点很重要，因为最开始他们非常少。" with diss
    soul "那些具体的类型，是祂们死后力量被分割、散逸到神裔身上才形成的。"
    show c1p6s7 29
    soul "基本上，一开始并没有单独的火神、战神、愤怒之神之类的神明。" with diss
    show c1p6s7 31
    soul "只有一位神，祂涵盖了这一切。" with diss
    show c1p6s7 28
    soul "现在说有意思的部分……" with diss
    show c1p6s7 32
    soul "我朋友认为，你获得力量的方式和其他神裔不一样。" with diss
    soul "他认为你是像最初的诸神那样获得力量的，这就是为什么你的魔法能承载他人的本源。"
    show c1p6s7 33
    mc "所以，这就是我现在能用里昂的火的原因？" with diss
    show c1p6s7 34
    soul "嗯。" with diss
    soul "本质上，你的魔力是原始而未成形的。"
    soul "别人继承的是已经被赋予形态的能量，而你的魔力处于最基本的状态，可以塑造成任何东西。"
    show c1p6s7 35
    soul "这也解释了它为什么这么不稳定。" with diss
    soul "如此原初的东西，会攀附上任何能攀附的事物，只为在这个世界上获得形态。"
    show c1p6s7 33
    mc "事情开始说得通了。" with diss
    show c1p6s7 34
    soul "对，它一开始表现为电，是因为在这么大的城市里你被电包围着。" with diss
    show c1p6s7 33
    mc "那火呢？" with diss
    mc "那天晚上池塘边并没有火。"
    show c1p6s7 32
    soul "没有，但那天晚上你刚碰上了里昂的火。" with diss
    show c1p6s7 33
    mc "嗯，我一整晚都在想这件事……" with diss
    mc "也许这就是它化成火焰的原因。"
    show c1p6s7 36
    soul "不过你知道这意味着什么吗？" with diss
    show c1p6s7 37
    mc "不太知道。" with diss
    show c1p6s7 38
    soul "这意味着你不会像大多数法师、神裔、甚至神明那样，被限制在单一类型的魔法上！" with diss
    soul "以你气息的体量和魔法的性质来看，你有可能成为有史以来最强的存在！"
    show c1p6s7 39
    mc "我觉得原初者还是在我之上。" with diss
    show c1p6s7 40
    soul "原初者？" with diss
    show c1p6s7 39
    mc "对……宇宙级实体，比宇宙和宇宙中的一切都更古老。" with diss
    show c1p6s7 41
    soul "我塞给你的信息是不是太多了？" with diss
    soul "你在说什么？"
    hide c1p6s7
    scrn "你把原初者以及你与它打交道的经历告诉了索尔……" with diss
    show c1p6s7  40
    soul "所以那就是它对那个大球形东西的称呼？" with diss
    soul "{i}源头{/i}？"
    show c1p6s7 39
    mc "对，就是。" with diss
    mc "更准确地说，是{i}一切{/i}的源头。"
    show c1p6s7 42
    soul "我的天哪！" with hpunch
    show c1p6s7 43
    soul "如果你的力量直接来自存在的源头……" with diss
    show c1p6s7 42
    soul "那你等于握着创世之力！" with diss
    show c1p6s7 44
    soul "唯一的麻烦是你的身体还在限制你。" with diss
    show c1p6s7 45
    soul "我们得想办法让你飞升。" with diss
    show c1p6s7 46
    mc "你是说飞升成{i}神{/i}？" with diss
    show c1p6s7 47
    soul "对，完全正确！" with diss
    soul "里昂都做到了，所以应该不会太难。"
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s7 48 with diss
    pause 1.0
    show c1p6s7 49
    asta "楼上这么热闹……" with diss
    show c1p6s7 50
    asta "我错过什么大场面了吗？" with diss
    show c1p6s7 51
    soul "是啊！" with diss
    soul "你错过了！"
    show c1p6s7 52
    soul "我们发现他的力量是什么了！" with diss
    show c1p6s7 53
    asta "哦？" with diss
    asta "说来听听。"
    show c1p6s7 54
    soul "创世。" with diss
    show c1p6s7 55
    asta "创世？" with diss
    asta "具体是什么意思？"
    show c1p6s7 56
    mc "我觉得意思是，我的力量可以是我想要的任何东西。" with diss
    show c1p6s7 57
    asta "真的？" with diss
    asta "你凭什么这么说？"
    show c1p6s7 58
    soul "不用凭什么，我们能证明。" with diss
    show c1p6s7 59
    soul "开个传送门。" with diss
    show c1p6s7 60
    asta "传到哪儿？" with diss
    show c1p6s7 61
    soul "我不管！" with diss
    soul "哪儿都行！"
    soul "快弄一个出来！"
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s7 62
    asta "好吧好吧……" with diss
    asta "这么指手画脚。"
    show c1p6s7 63 with diss
    pause 1.0
    play sfx "sfx/Astral - Portal.ogg"
    show c1p6s7 64 with diss
    pause 1.0
    show c1p6s7 65
    asta "你的传送门好了。" with diss
    asta "然后呢？"
    show c1p6s7 66
    soul "你以前穿过过她的传送门吗，[mc_name]？" with diss
    show c1p6s7 67
    mc "穿过啊，怎么了？" with diss
    show c1p6s7 68
    soul "我希望你记住穿过它时的感觉。" with diss
    soul "记住你被阿斯塔拉的能量包围时那种感觉。"
    show c1p6s7 69
    mc "好，我记得很清楚。" with diss
    show c1p6s7 70
    soul "很好。" with diss
    soul "现在像之前对闪电和火焰那样释放你的能量，但这次要把阿斯塔拉能量的记忆放在脑海最前面。"
    show c1p6s7 71
    mc "好……" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s7 72 with diss
    pause 1.0
    show c1p6s7 73 with diss
    pause 1.0
    play sfx "sfx/Astral - Portal.ogg"
    stop bgm fadeout 5.0
    show c1p6s7 74 with diss
    pause 1.0
    show c1p6s7 75
    asta "搞什么？！" with hpunch
    show c1p6s7 76
    soul "锵！" with diss
    soul "这就是创世之力！"
    show c1p6s7 77
    asta "太疯狂了！" with diss
    asta "你能模仿别人的力量？！"
    show c1p6s7 78
    soul "看来这个传送门里的能量也极其稳定。" with diss
    show c1p6s7 79
    soul "你不再怀疑自己了！" with diss
    show c1p6s7 80
    asta "也可能是原初者对他做了什么的结果。" with diss
    show c1p6s7 81
    soul "哦？" with diss
    soul "你也知道原初者？"
    show c1p6s7 82
    asta "只知道[mc_name]告诉我的。" with diss
    asta "我打算问问赋予我力量的那位女神的神灵。"
    show c1p6s7 83
    soul "你能和死去的神明交谈？！" with diss
    show c1p6s7 84
    asta "对……" with diss
    asta "我早期就是这样学会控制自己的能力的。"
    show c1p6s7 85
    soul "我开始意识到自己其实对神裔和神力的运作了解得有多少。" with diss
    show c1p6s7 86
    soul "所以，这个原初者就是你力量的来源，对吧？" with diss
    show c1p6s7 87
    mc "老实说，我不确定。" with diss
    show c1p6s7 88
    asta "抱歉打断大家的学习时间，但你得赶紧去见另一个神裔了。" with diss
    asta "你本来天黑后还要再去一趟，对吧？"
    show c1p6s7 89
    mc "嗯。" with diss
    show c1p6s7 90
    asta "天快黑了。" with diss
    show c1p6s7 91
    mc "好了，现在我需要的时候可以传送过去了。" with diss
    show c1p6s7 92
    asta "你对那里的样子记得清楚吗？" with diss
    asta "只有这样传送门才能连到对面。"
    show c1p6s7 93
    mc "放心，我记得。" with diss
    show c1p6s7 94
    asta "别这样，总算有{i}一{/i}件我能教你的事了，别不当回事。" with diss
    show c1p6s7 95
    mc "抱歉……" with diss
    mc "还有别的能告诉我的吗？"
    show c1p6s7 96
    asta "永远——我是说{i}永远{/i}别——尝试制造能把你送到多个地方的传送门。" with diss
    asta "我曾用一块砖头试过一次。"
    show c1p6s7 97
    asta "结果另一头只出来一把灰……" with diss
    show c1p6s7 98
    mc "知道了。" with diss
    mc "我可不想变成[mc_name]糊。"
    show c1p6s7 99 with diss
    pause 1.0
    play sfx "sfx/Astral - Portal.ogg"
    show c1p6s7 100
    asta "还有，传送门一定要随手关上。" with diss
    asta "每多开一个，都会持续抽走你的能量储备。"
    show c1p6s7 101
    mc "明白。" with diss
    play sfx "sfx/Astral - Portal.ogg"
    show c1p6s7 102 with diss
    pause 1.0
    show c1p6s7 103
    mc "还有别的吗？" with diss
    show c1p6s7 104
    asta "没了，目前我知道的就这么多了。" with diss
    show c1p6s7 105
    soul "等等，另一个神裔是怎么回事？" with diss
    show c1p6s7 106
    mc "昨晚我跟着一个气息，找到了另一个像我们这样的人。" with diss
    mc "她以为自己是法师，不过我觉得至少稍微说服了她一点。"
    mc "她让我今晚再来，她需要时间考虑我说的话。"
    show c1p6s7 107
    soul "哦……" with diss
    show c1p6s7 108
    soul "你为什么要找其他神裔？" with diss
    soul "那不会很危险吗？"
    show c1p6s7 109
    asta "这些我会解释给她听的，[mc_name]。" with diss
    asta "你先去吧。"
    show c1p6s7 110
    mc "哦，好。" with diss
    play sfx "sfx/Astral - Portal.ogg"
    show c1p6s7 111 with diss
    pause 1.0
    mc "（希望直接传送到她房间不会吓到她。）" with diss
    mc "（他们那么怕被人看见我出现在那里，直接传送过去应该是最安全的。）"
    play sfx "sfx/Astral - Warp.ogg"
    show c1p6s7 112 with diss
    pause 1.0
    stop bgs fadeout 1.0
    stop bgm fadeout 1.0
    hide c1p6s7 with diss
    pause 1.0
    jump c1p6s8

label c1p6s8:
    scene black
    show c1p6s8 1 with diss
    $ CharacterProfile.unlock_outfit([(chara["mela"], 1)])
    pause 1.0
    play sfx "sfx/Astral - Warp.ogg"
    show c1p6s8 2 with diss
    pause 0.2
    play sfx2 "sfx/Throw.ogg"
    show c1p6s8 3 with hpunch
    pause 0.2
    show c1p6s8 4 with hpunch
    pause 0.05
    show c1p6s8 5 with diss
    pause 0.05
    play sfx "sfx/Cloth2.ogg"
    play bgm "bgm/Upper Society.ogg" fadein 3.0
    show c1p6s8 6 with hpunch
    pause 1.0
    show c1p6s8 7
    mc "抱歉……" with diss
    mc "我不是想吓你。"
    show c1p6s8 8
    mela "你刚才是从一个传送门里出来的吗？" with diss
    show c1p6s8 7
    mc "对。" with diss
    mc "我今天刚发现自己能制造传送门。"
    mc "我觉得直接传送进来比再冒着被人看见爬树安全。"
    show c1p6s8 9
    mela "我很感谢你这么体贴。" with diss
    show c1p6s8 10
    mela "（他真的很强。）" with diss
    mela "（而且反应也很快。）"
    show c1p6s8 11
    mela "（等等……）" with diss
    mela "（他还抱着我！）"
    play sfx "sfx/Swipe.ogg"
    show c1p6s8 12
    mela "抱、抱歉！" with hpunch
    show c1p6s8 13
    mela "你、你不用一直抱着我……" with diss
    mela "我现在自己能站稳了……"
    show c1p6s8 14
    mc "不麻烦。" with diss
    show c1p6s8 15
    mela "不过……" with diss
    show c1p6s8 16
    mc "那么，嗯，昨晚我说的那些，你想清楚了吗？" with diss
    show c1p6s8 17
    mela "想好了。" with diss
    show c1p6s8 18
    mela "我相信你。" with diss
    show c1p6s8 19
    mc "我倒是不该惊讶。" with diss
    mc "我自己也不过花了一天就信了。"
    show c1p6s8 20
    mela "你是{i}怎么{/i}发现自己是神裔的？" with diss
    mela "你提到过被人从楼上扔下去？"
    show c1p6s8 21
    mc "对。" with diss
    mc "一个叫阿斯塔拉的女人告诉我的……"
    mc "……而她是从赋予她力量的那位神明那里得知的。"
    show c1p6s8 20
    mela "不过那些神明除了一个之外全都死了。" with diss
    show c1p6s8 21
    mc "对，你说得对，抱歉。" with diss
    mc "我的意思是，她是从那位神明的神灵那里得知的。"
    show c1p6s8 22
    mela "我不确定这样会不会好懂一点。" with diss
    show c1p6s8 23
    mc "你是说，赋予你力量的那位神明从没给你托过梦或显过灵？" with diss
    show c1p6s8 24
    mela "没有，完全没有过。" with diss
    mela "我的梦总是一模一样……"
    show c1p6s8 19
    mc "你获得力量有多久了？" with diss
    show c1p6s8  25
    mela "差不多四个月吧。" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s8 26
    mela "来，我们坐下说吧。" with diss
    mela "在这边会更舒服些。"
    show c1p6s8 27 with diss
    pause 1.0
    show c1p6s8 28
    mc "既然你相信我了，有兴趣和我们这些同类见见面，一起开发自己的力量吗？" with diss
    show c1p6s8 29
    mela "我很想……但我不能。" with diss
    show c1p6s8 28
    mc "为什么？" with diss
    show c1p6s8 30
    mela "说来话长……" with diss
    mela "我就直接说是因为我父亲吧。"
    show c1p6s8 28
    mc "哦……又是他。" with diss
    mc "话说他到底有什么问题？"
    mc "你和巴塞洛缪为什么这么怕他？"
    show c1p6s8 31
    mela "这个我不想谈……" with diss
    $ choice1 = ChoiceOption(
            "那就不用说了。", 
            stats={"mela": {"affection": 5}, "mc": {"karma": 3}}
        )
    $ choice2 = ChoiceOption(
            "为什么不？到目前为止我对你可是坦诚相待的。", 
            stats={"mela": {"affection": -3}}
        )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            show c1p6s8 28
            mc "那就不谈。" with diss
            mc "我只是想知道，如果他发现我不止一次、而是两次来过这里，我该不该担心。"
            show c1p6s8 30
            mela "不，你不用担心。" with diss
            mela "他不会发现的。"
            show c1p6s8 28
            mc "希望如此。" with diss
            mc "听起来他要是真发现了，可不会有好事。"
            mc "那既然知道自己是神裔，你打算怎么办？"
        "[choice2.get_display_text()]":
            $ choice2.apply_stats()
            show c1p6s8 28
            mc "为什么这么问？" with diss
            mc "到目前为止我对你都很坦诚。"
            show c1p6s8 32
            mela "只是我没有。" with diss
            show c1p6s8 33
            mc "好吧，随便。" with diss
            mc "我只是好奇。"
            show c1p6s8 28
            mc "那既然知道自己是神裔，你打算怎么办？" with diss
    show c1p6s8 30
    mela "什么都不做。" with diss
    mela "这不会改变我的处境。"
    show c1p6s8 28
    mc "你真的一点都不想去探索它能走多远？" with diss
    show c1p6s8 30
    mela "真的不想。" with diss
    show c1p6s8 28
    mc "为什么？" with diss
    mc "你知道成为神裔意味着可以飞升成神，对吧？"
    show c1p6s8 30
    mela "我当然知道。" with diss
    mela "但那不是我想要的东西。"
    show c1p6s8 31
    mela "说实话，现在知道自己是什么之后，我反而希望这份礼物落在别人身上……" with diss
    show c1p6s8 34
    mc "我完全理解。" with diss
    show c1p6s8 35
    mela "你理解？" with diss
    show c1p6s8 36
    mc "对。" with diss
    mc "我几乎每天都在想同样的事。"
    show c1p6s8 35
    mela "你对自身的感受一定和我一样。" with diss
    show c1p6s8 36
    mc "也许吧。" with diss
    mc "我觉得自己配不上这份力量，或者这力量在我身上是浪费了。"
    show c1p6s8 31
    mela "是啊……我也是这么觉得。" with diss
    show c1p6s8 34
    mc "不过我的朋友们正推着我向前，把我推出那种想法。" with diss
    mc "我还是不想要这些力量，但我开始觉得它也许能带来一些好事。"
    show c1p6s8 35
    mela "听起来都是很好的人。" with diss
    show c1p6s8 34
    mc "确实是。" with diss
    mc "不过我相信，如果你告诉你的朋友们你是什么，他们也会这么做。"
    show c1p6s8 31
    mela "我不确定巴思会不会真的相信我。" with diss
    show c1p6s8 34
    mc "那你其他朋友呢？" with diss
    show c1p6s8 35
    mela "没有别的。" with diss
    show c1p6s8 36
    mc "什么？！" with diss
    mc "你在开玩笑吧？"
    show c1p6s8 31
    mela "不……" with diss
    show c1p6s8 34
    mc "哦……" with diss
    mc "好吧，那现在我是你朋友了，而且我觉得你应该像我一样，学会接纳自己新的能力。"
    mc "至少弄清楚它能把你带向什么样的未来。"
    show c1p6s8 29
    mela "你真的是这个意思吗？" with diss
    show c1p6s8 28
    mc "对，不去探索就永远不知道自己能做什么。" with diss
    mc "依我看，你可是个狠角色！"
    show c1p6s8 29
    mela "不，我说的不是力量。" with diss
    mela "我们……真的现在是朋友了吗？"
    show c1p6s8 28
    mc "我希望是！" with diss
    mc "我可不跟陌生人聊这么多。"
    show c1p6s8 37
    mela "那么……我能请你帮个忙吗？" with diss
    mela "我是说，既然我们是朋友了……"
    show c1p6s8 38
    mc "当然。" with diss
    show c1p6s8 39
    mela "我想接受你的建议，但我不能想走就走……" with diss
    show c1p6s8 37
    mela "你愿意隔三差五过来一趟，把你和其他人学到的东西告诉我吗？" with diss
    show c1p6s8 38
    mc "完全没问题。" with diss
    mc "既然我现在能传送了，这事特别方便。"
    show c1p6s8 40
    mela "太好了！" with diss
    mela "这一定会超级有意思！"
    hide c1p6s8
    scrn "隔壁房间里……" with diss
    show c1p6s8 41
    barth "（不敢相信……！）" with diss
    barth "（小姐听起来很开心！）"
    show c1p6s8 42
    barth "（我已经十多年没听到她笑了！）" with diss
    show c1p6s8 43
    barth "（也许我不该对那个男孩那么严厉……）" with diss
    barth "（只要他不被抓住，我觉得这对她是好事。）"
    hide c1p6s8 with diss
    pause 1.0
    show c1p6s8 44
    mela "很高兴再见到你，[mc_name]。" with diss
    mela "但我得休息一下了。"
    show c1p6s8 45
    mc "哦，好。" with diss
    mc "那我就先走了。"
    show c1p6s8 46
    mela "抱歉……" with diss
    show c1p6s8 47
    mc "你道歉太多了。" with diss
    mc "你又没做错什么。"
    show c1p6s8 48
    mela "我知道……" with diss
    show c1p6s8 49
    mc "我什么时候再来？" with diss
    show c1p6s8 50
    mela "你想来的时候都行。" with diss
    show c1p6s8 51
    mc "现在我能直接传送进来了，能在没那么晚的时候来吗？" with diss
    show c1p6s8 52
    mela "也许吧。" with diss
    mela "怎么都有风险。"
    show c1p6s8 51
    mc "我明白了……" with diss
    mc "你有电话吗？我可以先发消息给你。"
    show c1p6s8 53
    mela "没有。" with diss
    show c1p6s8 50
    mela "就算有，信号也传不进来。" with diss
    show c1p6s8 51
    mc "该死，我开始觉得这个地方就是个高级监狱了。" with diss
    show c1p6s8 54
    mela "……" with diss
    stop bgm fadeout 3.0
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s8 55
    mc "梅拉妮……" with diss
    mc "……你是被逼无奈才待在这里的吗？"
    show c1p6s8 56
    mela "不、不是的……" with diss
    show c1p6s8 57
    mc "跟我说实话。" with diss
    show c1p6s8 58
    mela "这就是实话。" with diss
    mela "我发誓！"
    show c1p6s8 59
    mela "我父亲只是管得特别严，仅此而已。" with diss
    show c1p6s8 60
    mc "你不能自己做决定吗？" with diss
    mc "等等……你多大？"
    show c1p6s8 61
    mela "十八岁。" with diss
    show c1p6s8 62
    mc "那去你父亲的吧。" with diss
    mc "你已经是成年人了，不该被他控制。"
    show c1p6s8 63
    mela "要真是那么简单就好了……" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p6s8 64
    mela "你该走了。" with diss
    mela "我想睡了。"
    show c1p6s8 65
    mc "好吧。" with diss
    mc "但这个话题没完。"
    play sfx "sfx/Astral - Portal.ogg"
    show c1p6s8 66 with diss
    pause 1.0
    show c1p6s8 67
    mc "我会很快再来。" with diss
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    hide c1p6s8
    scrn "第二天……" with diss
    jump c1p6s9

label c1p6s9:
    show c1p6s9 1
    mc "（又到一年中的这个日子了。）" with diss
    mc "（这一天我真的又爱又恨。）"
    show c1p6s9 2
    mc "（我得找件像样的衣服穿。）" with diss
    hide c1p6s9 with diss
    pause 1.0
    show c1p6s9 3
    $ CharacterProfile.unlock_outfit([(chara["mc"], 6)])
    mc "（这件应该行。）" with diss
    play sfx "sfx/Door - Knock.ogg"
    pause 1.0
    show c1p6s9 4
    mc "（我敢打赌那是莱拉。）" with diss
    play sfx "sfx/Door - Open.ogg"
    show c1p6s9 5
    $ CharacterProfile.unlock_outfit([(chara["layl"], 5)])
    layl "嘿，[mc_name]……" with diss
    layl "你看起来不错。"
    show c1p6s9 6
    mc "谢谢，莱拉。" with diss
    mc "你也一样。"
    show c1p6s9 5
    layl "那你都准备好出发了吗？" with diss
    show c1p6s9 6
    mc "嗯……" with diss
    hide c1p6s9 with diss
    pause 1.0
    play bgs "bgs/Car - Drive.ogg" volume 1 fadein 1.0
    show c1p6s9 7 with diss
    pause 1.0
    show c1p6s9 8
    layl "你今天还是那么安静。" with diss
    show c1p6s9 9
    mc "嗯……" with diss
    show c1p6s9 10
    layl "别担心，我理解。" with diss
    layl "我们不用说话。"
    show c1p6s9 11
    mc "抱歉，我只是在回忆。" with diss
    show c1p6s9 12
    layl "别道歉。" with diss
    show c1p6s9 13
    layl "我也想她……" with diss
    stop bgm fadeout 3.0
    stop bgs fadeout 1.0
    hide c1p6s9
    scrn "七年前……" with diss
    call sarapast from _call_sarapast
    play bgs "bgs/Car - Drive.ogg" volume 0.75 fadein 1.0
    show c1p6s9 14
    layl "这么多年你还留着它。" with diss
    layl "那天我去医院，发现你把它落下了，我震惊极了。"
    mc "我当时没什么选择……" with diss
    mc "要么留下，要么被逮捕。"
    layl "我知道……" with diss
    layl "我知道要是它也丢了你会疯掉，所以我把它和我带去的新衣服放在一起。"
    mc "谢谢你这么做。" with diss
    layl "不客气。" with diss
    layl "我知道它对你有多重要。"
    show c1p6s9 15
    mc "你会不会想过，她为什么那么做？" with diss
    show c1p6s9 16
    layl "一直在想……" with diss
    show c1p6s9 17
    layl "我知道她有自己的问题，但你们在一起之后，她的世界好像终于开始见阳光了。" with diss
    show c1p6s9 18
    mc "我也这么以为……" with diss
    show c1p6s9 19
    layl "我猜是她的脑子没法和这个世界同步。" with diss
    layl "也许她意识到永远不可能，于是觉得自己做的事是唯一的选择。"
    show c1p6s9 20
    mc "对，你大概说得对。" with diss
    mc "我只希望当时能看出她到底有多糟。"
    mc "那样的话，也许我就能帮帮她。"
    show c1p6s9 21
    layl "她很擅长把这一切藏起来。" with diss
    show c1p6s9 22
    mc "是啊……" with diss
    stop bgs fadeout 1.0
    hide c1p6s9
    scrn "你和莱拉来到了墓地……" with diss
    play bgm "bgm/Let You Go.ogg"
    play bgs "bgs/Day - Birds.ogg"
    play sfx "sfx/Car - Door Close.ogg"
    show c1p6s9 23 with diss
    pause 1.0
    play sfx "sfx/Footsteps - Concrete.ogg"
    show c1p6s9 24 with diss
    pause 1.0
    show c1p6s9 25 with diss
    pause 1.0
    show c1p6s9 26
    layl "嘿，莎拉，我们又来了……" with diss
    layl "是莱拉和[mc_name]。"
    show c1p6s9 27
    layl "生日快乐！" with diss
    show c1p6s9 28
    mc "生日快乐，莎拉……" with diss
    mc "今天你就二十二岁了。"
    show c1p6s9 29
    layl "真难以想象，你已经走了五年。" with diss
    show c1p6s9 30
    layl "我想念我们聊天……" with diss
    show c1p6s9 31
    mc "我也想念你的笑容……" with diss
    show c1p6s9 32
    layl "对着墓碑说话，总感觉怪怪的……" with diss
    show c1p6s9 33
    mc "是啊……" with diss
    mc "就是不一样了……"
    show c1p6s9 34
    mc "我们真的很想你，莎拉……" with diss
    mc "……我们也爱你……"
    show c1p6s9 35 with diss
    pause 0.5
    play sfx "sfx/Grass - Rustle.ogg"
    show c1p6s9 36
    layl "……" with diss
    show c1p6s9 37 with diss
    pause 0.5
    show c1p6s9 38 with diss
    pause 1.0
    show c1p6s9 39
    layl "可恶！" with diss
    layl "我明明表现得那么好！"
    layl "我跟自己说了今年不哭的！"
    play sfx "sfx/Cloth2.ogg"
    show c1p6s9 40
    mc "没关系，莱拉。" with diss
    mc "你不该压抑自己的情绪。"
    show c1p6s9 41
    layl "我知道……" with diss
    hide c1p6s9
    scrn "过了一会儿……" with diss
    show c1p6s9 42
    mc "既然你好像好了一点，我能单独待一会儿吗？" with diss
    show c1p6s9 43
    layl "没关系，你去吧。" with diss
    layl "反正我也得去趟洗手间。"
    show c1p6s9 44
    mc "谢了，莱拉。" with diss
    play sfx "sfx/Footsteps - Grass.ogg"
    show c1p6s9 45 with diss
    pause 1.0
    show c1p6s9 46
    mc "嘿，莎拉，是我……" with diss
    mc "今年发生在我身上的那些疯狂事，你肯定想不到。"
    show c1p6s9 47
    mc "时代真的开始变了……" with diss
    mc "我真希望你在场能看到。"
    show c1p6s9 48
    mc "不过在这么多变化之下……" with diss
    mc "……我觉得还有一件事也得改变。"
    show c1p6s9 49
    mc "我最近在这里交了些新朋友……我觉得她们中有些人喜欢我。" with diss
    mc "就是{i}真的{/i}那种喜欢……{i}那种意思。{/i}"
    show c1p6s9 50
    mc "但每当我想对某个人做出那种回应时，我就会僵住，我想我明白原因了。" with diss
    show c1p6s9 51
    mc "是因为你。" with diss
    show c1p6s9 50
    mc "我怕自己那样对别人，会毁掉我们曾经拥有的一切……" with diss
    mc "又或者，如果我向前走，就会不知怎么地侮辱你的记忆……"
    show c1p6s9 52
    mc "但我觉得现在我必须这么做。" with diss
    mc "是时候让我放下过去，真正重新开始生活了。"
    if rayngw:
        mc "其实我已经有点开始了，感觉很好。"
        mc "我不想再束缚自己了。"
    show c1p6s9 53
    mc "但你要知道，即使我要放下你，放下我们曾拥有的一切——" with diss
    mc "——我永远不会忘记。"
    mc "你会永远是我历史上最明亮……也是最黑暗的一部分。"
    stop bgm fadeout 5.0
    show c1p6s9 52
    mc "希望有一天我们在死后重逢时，你能原谅我……" with diss
    play sfx "sfx/Footsteps - Grass.ogg"
    show c1p6s9 54
    layl "我回来了。" with diss
    show c1p6s9 55
    mc "时机正好！" with diss
    mc "我刚把要说的话说完。"
    show c1p6s9 56
    layl "现在像平常一样去喝个痛快吗？" with diss
    show c1p6s9 57
    mc "好。" with diss
    show c1p6s9 58
    toge "再见，莎拉。" with diss
    $ CharacterProfile.unlock_profile([chara["sara"]])
    stop bgs fadeout 1.0
    hide c1p6s9
    scrn "你和莱拉去「最后一滴」喝酒……" with diss
    jump c1p7s1

label c1p7s1:
    scene black
    show magic_effect at theme_ember
    with fadeb
    play sfx "sfx/Chapter - In.ogg"
    show c1p7 as c1p7_blur at text_glow
    show c1p7
    with staticflow
    $ save_name = "第1-7章：前进"
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide c1p7
    hide c1p7_blur
    hide magic_effect
    with grunge
    pause 0.5
    play bgm lastdropmusic fadein 1.5
    play bgs "bgs/Club.ogg" fadein 1.0
    $ renpy.random.shuffle(lastdropmusic)
    show c1p7s1 1
    layl "哇！" with diss
    layl "我好久没来这儿了……"
    layl "一切和以前都不一样了！"
    show c1p7s1 2
    soul "喂，你们俩！" with diss
    show c1p7s1 3
    soul "你们是来看我的，还是出来玩的？" with diss
    show c1p7s1 4
    layl "我们是来喝个烂醉的。" with diss
    show c1p7s1 5
    soul "好嘞！" with diss
    soul "想喝点什么特别的东西不？"
    show c1p7s1 6
    mc "还真有。" with diss
    mc "我们每人一杯「迅捷脉冲」，谢谢。"
    show c1p7s1 7
    soul "哦？" with diss
    soul "你挺爱喝这个的啊？"
    show c1p7s1 6
    mc "我觉得它成了我的新最爱。" with diss
    mc "味道不错，一杯就能让我微醺。"
    show c1p7s1 8
    layl "「迅捷脉冲」是什么？" with diss
    show c1p7s1 9
    mc "索尔的招牌酒，你会喜欢的。" with diss
    play sfx "sfx/Glass - Slide.ogg"
    show c1p7s1 10
    soul "来了！" with diss
    show c1p7s1 11
    mc "谢谢，索尔。" with diss
    play sfx "sfx/Glass - Ice - Slam.ogg"
    show c1p7s1 12 with hpunch
    pause 0.3
    show c1p7s1 13
    layl "{i}哇{/i}，这酒真烈！" with diss
    show c1p7s1 14
    mc "就是这个意思！" with diss
    show c1p7s1 15
    soul "你们俩今天怎么都闷闷不乐？" with diss
    show c1p7s1 16
    layl "今天是我们的朋友的生日……" with diss
    layl "她几年前去世了。"
    show c1p7s1 17
    mc "嗯。" with diss
    mc "每年我们去扫过墓，都会出来喝一杯。"
    mc "一半是因为她生前从没机会喝过，至少不能合法地喝；另一半是为了把这一天的悲伤淹掉。"
    show c1p7s1 18
    soul "太不容易了。" with diss
    soul "我为你们的失去感到遗憾。"
    show c1p7s1 19
    layl "不，没关系！" with diss
    layl "现在说出来容易多了。"
    show c1p7s1 20
    layl "至少对我来说。" with diss
    layl "不过我想对[mc_name]来说，还是难一些。"
    show c1p7s1 21
    mc "我正在好转。" with diss
    mc "我今天甚至对自己许下了承诺……是时候重新为自己而活了。"
    show c1p7s1 22
    layl "真的？" with diss
    layl "我跟你说了好久要这么做。"
    layl "很高兴你终于听进去了。"
    show c1p7s1 23
    layl "这也是她会希望的。" with diss
    show c1p7s1 24
    mc "希望吧。" with diss
    show c1p7s1 25
    layl "总之，再给我一杯「迅捷脉冲」，谢谢！" with diss
    show c1p7s1 26
    soul "没问题！" with diss
    show c1p7s1 27
    soul "不过下一杯你可得慢点喝，小姑娘！" with diss
    show c1p7s1 28
    layl "想都别想！" with diss
    hide c1p7s1
    scrn "几杯之后……" with diss
    show c1p7s1 29
    soul "好了，你们俩，我要把你们都停酒了。" with diss
    show c1p7s1 30
    layl "哎……" with diss
    layl "为什么？"
    show c1p7s1 31
    soul "因为……" with diss
    soul "不让客人喝太醉本来就是工作职责之一。"
    show c1p7s1 32
    layl "可、可是我们是朋友啊？" with diss
    show c1p7s1 33
    soul "是啊，我们是朋友。" with diss
    soul "所以我才现在停你的酒。"
    show c1p7s1 34
    mc "非停不可吗？" with diss
    mc "我们能再喝一杯吧？"
    show c1p7s1 35
    soul "不行。" with diss
    soul "你们俩今晚已经喝够了。"
    show c1p7s1 36
    soul "还有，你们最好坐公交回去！" with diss
    soul "不许开车，莱拉！"
    show c1p7s1 37
    layl "她说得有道理，[mc_name]……" with diss
    layl "我觉得我可能都{i}开不了{/i}车了。"
    show c1p7s1 38
    mc "没事没事。" with diss
    mc "我搞定。"
    show c1p7s1 39
    soul "嗯哼。" with diss
    soul "你打算怎么办？"
    soul "你几乎跟她一样醉。"
    show c1p7s1 40
    mc "我会魔法！" with diss
    show c1p7s1 41
    soul "你该不会真要——" with diss
    play sfx "sfx/Astral - Portal.ogg"
    show c1p7s1 42
    soul "好吧……那就直接在这儿开个传送门吧。" with diss
    show c1p7s1 43
    mc "看吧？" with diss
    mc "我搞定了。"
    show c1p7s1 44
    layl "你能开「歪洞」了？" with diss
    show c1p7s1 45
    mc "对！" with diss
    mc "我不是说过了吗？！"
    show c1p7s1 46
    layl "呃……" with diss
    show c1p7s1 47
    soul "你就打算把它留在那儿？" with diss
    soul "你到底把它开到哪儿去了？"
    show c1p7s1 48
    mc "我家。" with diss
    show c1p7s1 49
    soul "你确定？" with diss
    show c1p7s1 50
    mc "我想是的……" with diss
    show c1p7s1 51
    mc "只有一个办法能知道！" with diss
    play sfx "sfx/Astral - Warp.ogg"
    show c1p7s1 52 with diss
    pause 1.0
    show c1p7s1 53
    layl "我的天哪！" with diss
    layl "他「啵」地一下就没了！"
    show c1p7s1 54
    layl "我也要「啵」！" with diss
    show c1p7s1 55
    soul "不——等等——莱拉，我们不知道会到——" with diss
    play sfx "sfx/Astral - Warp.ogg"
    show c1p7s1 55a with diss
    pause 1.0
    show c1p7s1 56
    soul "（呃！）" with diss
    soul "（他们一起喝酒时就像小孩一样！）"
    show c1p7s1 57
    soul "（不过我不能太苛责他们……）"
    soul "（今天似乎确实很难熬。）"
    stop bgm fadeout 3.0
    stop bgs fadeout 3.0
    hide c1p7s1 with diss
    pause 1.0
    jump c1p7s2

label c1p7s2:
    scene black
    play sfx "sfx/Astral - Portal.ogg"
    show c1p7s2 1 with diss
    pause 1.0
    play sfx "sfx/Astral - Warp.ogg"
    show c1p7s2 2 with diss
    pause 0.3
    play sfx "sfx/Table - Slam.ogg"
    show c1p7s2 3 with hpunch
    pause 1.0
    show c1p7s2 4
    mc "哦哟！" with diss
    play sfx "sfx/Astral - Warp.ogg"
    show c1p7s2 5 with diss
    pause 0.3
    play sfx "sfx/Body - Drop2.ogg"
    show c1p7s2 6 with hpunch
    pause 1.0
    show c1p7s2 7
    layl "嘿，[mc_name]。" with diss
    show c1p7s2 8
    mc "嘿，莱拉。" with diss
    show c1p7s2 9
    layl "{i}*咯咯笑*{/i} 我们落到的这个姿势，还挺亲密的……" with diss
    show c1p7s2 10
    mc "是啊，看起来是。" with diss
    show c1p7s2 11
    layl "而且喝了酒之后我总是会有那方面的冲动，这更糟糕了。" with diss
    show c1p7s2 12
    mc "{i}那方面？{/i}" with diss
    show c1p7s2 13
    layl "对。" with diss
    layl "你知道我什么意思……"
    show c1p7s2 14
    layl "就是{i}那种{/i}冲动！" with diss
    show c1p7s2 15
    mc "哦……" with diss
    show c1p7s2 16
    layl "{i}*轻声地*{/i} 你能帮我解决一下吗？" with diss
    show c1p7s2 17
    mc "什么？" with diss
    show c1p7s2 18
    layl "{i}我想要你……{/i}" with diss
    layl "{i}……让我去。{/i}"
    show c1p7s2 19
    mc "我？！" with diss
    show c1p7s2 20
    layl "为什么不行？" with diss
    show c1p7s2 21
    mc "我们都还有点醉……我觉得这不是个好决定。" with diss
    show c1p7s2 20
    layl "我可不这么觉得。"  with diss
    layl "穿过那个传送门、再加上那一摔，好像已经让我清醒得差不多了。"
    show c1p7s2 21
    mc "你也一样？" with diss
    show c1p7s2 22
    layl "对。" with diss
    show c1p7s2 23
    layl "总之，我一直太害怕，不敢对你说什么、也不敢主动。" with diss
    layl "后来你跟莎拉在一起了，其他事也就那么发生了……"
    show c1p7s2 22
    layl "但你说过要开始放下过去、为自己而活，我就觉得也许我也该这么做。" with diss
    show c1p7s2 24
    layl "你要是还不想的话，我们甚至可以不做到最后。" with diss
    show c1p7s2 25
    layl "我只需要{i}某种{/i}释放。" with diss
    $ choice1 = ChoiceOption(
            "管他的，为什么不行？", 
            stats={"layl": {"affection": 3}},
            path_info=("layl", "Lewd Scene")
        )
    $ choice2 = ChoiceOption(
            "等你明天还有同样想法再来问我吧。", 
            stats={"layl": {"affection": 5}},
        )
    $ choice3 = ChoiceOption(
            "我累了，去睡了。", 
            stats={"layl": {"affection": -3}},
        )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            $ laylconfess = True
            show c1p7s2 26
            mc "管他的，为什么不呢？" with diss
            show c1p7s2 27
            layl "真的？" with diss
            show c1p7s2 26
            mc "对。" with diss
            call laylconfess from _call_laylconfess
            $ CharacterProfile.unlock_memory([(chara["layl"], "laylconfess")])
        "[choice2.get_display_text()]":
            $ choice2.apply_stats()
            $ layl_postponesex = True
            show c1p7s2 28
            mc "明天如果你还有同样的感觉，再来问我一次。" with diss
            hide c1p7s2 with diss
        "[choice3.get_display_text()]":
            $ choice3.apply_stats()
            show c1p7s2 29
            mc "我累了。" with diss
            mc "我去睡了。"
            hide c1p7s2 with diss
    scrn "你离开莱拉，回房睡觉。" with diss
    jump c1p7s3

label c1p7s3:
    play bgm "bgm/New Day.ogg" fadein 3.0
    show c1p7s3 1 with diss
    pause 1.0
    show c1p7s3 2 with diss
    pause 1.0
    show c1p7s3 3
    mc "莱拉，你在吗？" with diss
    pause 1.0
    show c1p7s3 4
    mc "（看来她已经走了。）" with diss
    mc "（也许她去取车了。）"
    show c1p7s3 5
    mc "（我看看消息。）" with diss
    show c1p7s3 6 with diss
    pause 1.0
    mc "（嗯……什么都没有。）" with diss
    show c1p7s3 7
    mc "（这完全不像她。）" with diss
    mc "（希望我没惹她生气。）"
    mc "（我们到家时都挺清醒的，但……）"
    mc "（……也许她是在为昨晚的事害羞或后悔。）"
    play sfx "sfx/Astral - Portal.ogg"
    show c1p7s3 8 with diss
    pause 1.0
    play sfx "sfx/Astral - Warp.ogg"
    show c1p7s3 9 with diss
    pause 1.0
    play sfx "sfx/Astral - Portal.ogg"
    show c1p7s3 10
    mc "阿斯塔拉？" with diss
    mc "你怎么在这儿？"
    show c1p7s3 11
    asta "我又找到一个神裔了。" with diss
    asta "我们一起去见对方吧。"
    show c1p7s3 10
    mc "嗯……好。" with diss
    mc "现在吗？"
    show c1p7s3 11
    asta "如果你不介意的话。" with diss
    show c1p7s3 10
    mc "完全不介意。" with diss
    mc "走吧。"
    stop bgm fadeout 3.0
    hide c1p7s3
    scrn "阿斯塔拉把你传送到那个神裔气息附近。" with diss
    play bgm "bgm/Mornings in the City.ogg" fadein 3.0
    play bgs "bgs/City - Alley - Morning.ogg" fadein 1.0
    play sfx "sfx/Astral - Portal.ogg"
    show c1p7s3 12
    asta "好，那个神裔应该就在这一带。" with diss
    show c1p7s3 13
    asta "我刚从这里去找你，他们要是离开了应该也没走远。" with diss
    asta "我们用感知去找他们吧。"
    show c1p7s3 14
    mc "好。" with diss
    play sfx "sfx/Whoosh.ogg"
    show c1p7s3 15
    mc "哦，有意思。" with diss
    show c1p7s3 16
    asta "嗯。" with diss
    show c1p7s3 17
    asta "你找到了吗？" with diss
    show c1p7s3 18
    mc "嗯，在那边。" with diss
    mc "不过那气息和我之前见过的都不一样。"
    show c1p7s3 19
    asta "那个老流浪汉？" with diss
    show c1p7s3 20
    mc "不是。" with diss
    mc "用气息视觉看他后面。"
    show c1p7s3 21
    asta "气息视觉，嗯？" with diss
    show c1p7s3 22
    asta "这个说法我喜欢。" with diss
    show c1p7s3 23 with diss
    pause 1.0
    asta "我明白你说的那个气息是什么了。" with diss
    asta "不过我以前见过类似的……里昂的。"
    show c1p7s3 24
    mc "很好。" with diss
    mc "我正好有账要跟那个混蛋算。"
    show c1p7s3 25
    asta "先别激动。" with diss
    asta "颜色不对，不会是他。"
    show c1p7s3 26
    asta "不过他们的力量大概类似，小心点。" with diss
    show c1p7s3 27
    mc "明白。" with diss
    play sfx "sfx/Footsteps - Concrete.ogg"
    show c1p7s3 28
    asta "那就走吧！" with diss
    hide c1p7s3 with diss
    pause 1.0
    show c1p7s3 29 with diss
    pause 1.0
    show c1p7s3 30
    asta "那不可能是神裔吧？" with diss
    show c1p7s3 31
    asta "他看起来太小了。" with diss
    show c1p7s3 32
    mc "我想继承神力应该没有年龄限制。" with diss
    show c1p7s3 33
    asta "大概吧。" with diss
    play sfx "sfx/Footsteps - Concrete.ogg"
    show c1p7s3 34
    asta "喂，小子！" with diss
    asta "你在这种后巷里鬼鬼祟祟干什么？"
    show c1p7s3 35
    asta "你不是该在上学之类的吗？" with diss
    show c1p7s3 36
    unkn "谁——呃——我？" with diss
    show c1p7s3 37
    mc "我这儿没看到别人。" with diss
    show c1p7s3 38 with diss
    pause 0.5
    show c1p7s3 39 with diss
    pause 0.5
    show c1p7s3 40
    unkn "您说得对，先生。" with diss
    show c1p7s3 41
    asta "哦，他被叫了一声{i}先生{/i}。" with diss
    asta "我喜欢这小子。"
    show c1p7s3 42
    unkn "我、我不上学……" with diss
    show c1p7s3 37
    mc "什么？" with diss
    mc "为什么不上？"
    show c1p7s3 40
    unkn "那是——" with diss
    show c1p7s3 43
    unkn "我不想谈这个。" with diss
    $ choice1 = ChoiceOption(
        "回答问题，小鬼。", 
        stats={"asta": {"affection": -3}, "mc": {"karma": -3}},
    )
    $ choice2 = ChoiceOption(
        "至少告诉我们你叫什么名字？", 
    )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            show c1p7s3 44a 1
            mc "回答问题，小子。" with diss
            show c1p7s3 44a 2
            unkn "为什么？" with diss
            show c1p7s3 44a 3
            asta "他没欠我们什么。" with diss
            show c1p7s3 44a 4
            asta "人家对你表示了尊敬，你真有必要这么凶吗？" with diss
            show c1p7s3 44a 5
            mc "抱歉。" with diss
            mc "你说得对。"
            play sfx "sfx/Cloth2.ogg"
            show c1p7s3 44a 6
            asta "别在意他。" with diss
            asta "他今天好像起床气很重。"
            show c1p7s3 44a 7
            asta "你叫什么名字，小子？" with diss
        "[choice2.get_display_text()]":
            show c1p7s3 37
            mc "至少能告诉我们你的名字吗？" with diss
            play sfx "sfx/Cloth2.ogg"
            show c1p7s3 44a 7
            asta "放心，我们没有恶意。" with diss
    show c1p7s3 45
    $ CharacterProfile.unlock_profile([chara["eddi"]])
    eddi "我叫埃德温。" with diss
    eddi "不过朋友们都叫我埃迪。"
    show c1p7s3 46
    eddi "嗯，以前是……在我还有朋友的时候。" with diss
    show c1p7s3 47
    mc "你朋友们怎么了？" with diss
    show c1p7s3 48
    eddi "不，也不算怎么了。" with diss
    show c1p7s3 49
    eddi "他们只是不再是我的朋友了。" with diss
    show c1p7s3 50
    asta "人来人往，埃迪。" with diss
    asta "这就是生活。"
    show c1p7s3 51
    mc "是啊，真可惜。" with diss
    mc "不过也有例外。"
    show c1p7s3 52
    asta "其实没有。" with diss
    asta "所有人都会离开你，或早或晚，永远如此"
    show c1p7s3 53
    mc "莱拉做了我十九年的朋友，我不认为这会改变。" with diss
    show c1p7s3 54
    asta "会的。" with diss
    asta "没有什么能永恒。"
    show c1p7s3 55
    eddi "这没让事情好转。" with diss
    play sfx "sfx/Footsteps - Concrete - Slow.ogg"
    show c1p7s3 56
    eddi "我走了。" with diss
    show c1p7s3 57
    mc "等一下！" with diss
    mc "我们有些重要的事必须跟你谈谈。"
    stop bgm fadeout 3.0
    show c1p7s3 58
    eddi "把手拿开……" with diss
    show c1p7s3 59
    mc "先坐下一会儿。" with diss
    show c1p7s3 60
    eddi "我说……" with diss
    show c1p7s3 61
    eddi "把手——" with diss
    play sfx "sfx/Water - C End.ogg"
    show c1p7s3 62 with diss
    pause 0.5
    play bgm "bgm/Scion of Water.ogg"
    play sfx "sfx/Water - Jet.ogg"
    show c1p7s3 63
    eddi "——从我身上拿开！" with hpunch
    play sfx2 "sfx/Water - Impact.ogg"
    show c1p7s3 64 with hpunch
    pause 0.5
    show c1p7s3 65
    asta "好险。" with diss
    show c1p7s3 66
    asta "你没事吧，[mc_name]？" with diss
    show c1p7s3 67
    mc "呃，没事。" with diss
    show c1p7s3 68
    mc "我没料到他会那样突然发作。" with diss
    show c1p7s3 69
    asta "不过说句公道话，他提醒过你了。" with diss
    play sfx "sfx/Footsteps - Asphalt - Run.ogg"
    show c1p7s3 70
    mc "对，而且现在让他跑了。" with diss
    show c1p7s3 71
    asta "交给我。" with diss
    show c1p7s3 72 with diss
    pause 0.5
    play sfx "sfx/Astral - Portal.ogg"
    show c1p7s3 73 with diss
    pause 0.5
    play sfx "sfx/Astral - Warp.ogg"
    show c1p7s3 74 with diss
    pause 0.5
    play sfx "sfx/Astral - Warp.ogg"
    show c1p7s3 75 with diss
    pause 0.5
    play sfx "sfx/Astral - Portal.ogg"
    show c1p7s3 76 with diss
    pause 0.5
    show c1p7s3 77
    eddi "什么？！" with diss
    show c1p7s3 78
    eddi "刚才那是传送门？！" with diss
    show c1p7s3 79
    asta "对！" with diss
    show c1p7s3 80
    eddi "那是你做的？" with diss
    show c1p7s3 81
    mc "确实是。" with diss
    show c1p7s3 82
    eddi "好。" with diss
    play sfx "sfx/Water - C End.ogg"
    show c1p7s3 83
    eddi "现在我知道该先对付谁了！" with diss
    play sfx2 "sfx/Water - Blade.ogg"
    show c1p7s3 84 with hpunch
    pause 0.5
    play sfx "sfx/Whoosh - Air.ogg"
    play sfx3 "sfx/Water - Air.ogg"
    show c1p7s3 85 with diss
    pause 0.5
    play sfx "sfx/Fight - Slice.ogg"
    show c1p7s3 86 with hpunch
    pause 0.5
    play sfx "sfx/Water - Impact.ogg"
    show c1p7s3 87 with diss
    pause 0.5
    show c1p7s3 88
    asta "{i}*皱眉*{/i}" with diss
    show c1p7s3 89
    asta "请你冷静点！" with diss
    asta "我们已经说过，我们对你没有恶意！"
    show c1p7s3 90
    eddi "哦，是吗？" with diss
    eddi "那为什么要问这么多问题？"
    show c1p7s3 91
    eddi "我敢说你们就是那个到处从街上抓法师的组织！" with diss
    eddi "我在课上小小的魔力失控了一次，现在整座该死城市都在找我！"
    show c1p7s3 92
    eddi "他们把我开除已经够糟了，我朋友们还全都背叛了我……" with diss
    show c1p7s3 93
    eddi "我拒绝被你们这群怪胎「消失」！" with diss
    play sfx "sfx/Water - Wave.ogg" volume 0.5
    play sfxl "sfx/Water - WaveL.ogg" fadein 1.0
    show c1p7s3 94
    eddi "呜啊啊！" with hpunchs
    play sfx "sfx/Water - Wave.ogg"
    show c1p7s3 95 with hpunch
    pause 1.0
    show c1p7s3 96
    mc "（这波好大！）" with diss
    mc "（他召唤了这么多水？！）"
    show c1p7s3 97
    mc "（我躲不开……）" with diss
    show c1p7s3 98
    mc "（阿斯塔拉看起来也很慌。）" with diss
    show c1p7s3 99
    mc "（我有了！）" with diss
    play sfx "sfx/Footsteps - Asphalt - Run.ogg"
    show c1p7s3 100
    asta "你到底在干什么？！" with diss
    show c1p7s3 101
    mc "就是这个！" with diss
    play sfx "sfx/Fire - Start.ogg"
    show c1p7s3 102 with hpunch
    pause 0.5
    play sfx "sfx/Fire - Wall.ogg"
    show c1p7s3 103 with hpunch
    pause 0.5
    stop bgm fadeout 3.0
    stop sfxl fadeout 3.0
    play sfx2 "sfx/Steam.ogg"
    show c1p7s3 104 with diss
    pause 1.0
    show c1p7s3 105
    asta "呃！" with diss
    asta "我什么都看不见！"
    asta "这么多该死的蒸汽！"
    mc "至少我们没和鱼一起游泳！" with diss
    asta "认真的？！" with diss
    asta "水做的笑话？！"
    asta "而且一点都不好笑！"
    show c1p7s3 106
    mc "你不喜欢我的笑话，阿斯塔拉？" with diss
    show c1p7s3 107 with disl
    pause 1.0
    mc "哦，我的错！" with diss
    mc "你不是阿斯塔拉！"
    show c1p7s3 108
    eddi "才不是！" with diss
    play sfx "sfx/Fight - Punch - Hit.ogg"
    show c1p7s3 109 with hpunch
    pause 0.5
    show c1p7s3 110
    mc "（我的天哪！）" with diss
    mc "（他这一拳跟卡车一样重。）"
    show c1p7s3 111
    eddi "我敢说你以为我会直接逃跑！" with diss
    eddi "毕竟这些蒸汽本来正好能当掩护。"
    show c1p7s3 112
    eddi "不过……我受够你们这些人追着我跑了！" with diss
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p7s3 113 with hpunch
    pause 0.5
    show c1p7s3 114
    mc "我完全不知道你在说什么。" with diss
    mc "但如果你想打……"
    show c1p7s3 115
    mc "……我奉陪。" with diss
    show c1p7s3 116
    eddi "（什么？！）" with diss
    eddi "（他的眼睛在发光，和我的一样！）"
    eddi "（他也是和我一样的特殊法师！）"
    show c1p7s3 117
    eddi "（糟了！）" with diss
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p7s3 118 with hpunch
    pause 0.5
    show c1p7s3 119
    eddi "等等！" with diss
    eddi "我觉得我可能搞错了！"
    $ choice1 = ChoiceOption(
            "住手。", 
            stats={"mc": {"karma": 3}},
        )
    $ choice2 = ChoiceOption(
            "继续进攻。", 
            stats={"mc": {"karma": -3}},
        )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
        "[choice2.get_display_text()]":
            $ choice2.apply_stats()
    play sfx "sfx/Astral - Barrier.ogg"
    show c1p7s3 120 with hpunch
    pause 1.0
    show c1p7s3 121
    mc "什么？" with diss
    mc "阿斯塔拉的魔法……"
    play sfx "sfx/Astral - Barrier - Push.ogg"
    show c1p7s3 122 with hpunch
    pause 0.5
    play sfx "sfx/Body - Drop.ogg"
    show c1p7s3 123 with hpunch
    pause 1.0
    show c1p7s3 124
    asta "够了！" with diss
    show c1p7s3 125
    asta "我们要么好好谈，要么各走各的！" with diss
    show c1p7s3 126
    eddi "我们可以谈。" with diss
    eddi "你们看起来不像是我一直以为的那种人。"
    show c1p7s3 127
    mc "你要是早点肯听我们说，早就明白了！" with diss
    show c1p7s3 128
    eddi "是，先生，您当然说得对。" with diss
    show c1p7s3 129
    asta "嗯……真够麻烦的。" with diss
    show c1p7s3 130
    asta "而且我敢肯定我们也引来了不少注意。" with diss
    asta "我们去个人少的地方吧。"
    play sfx "sfx/Astral - Portal.ogg"
    stop bgs fadeout 1.0
    stop bgm fadeout 1.0
    hide c1p7s3
    scrn "阿斯塔拉把你和埃迪传送到塞拉斯的健身房「弹性健身」。" with diss
    jump c1p7s4

label c1p7s4:
    play bgm "bgm/Fitness2.ogg" fadein 3.0
    play sfx "sfx/Astral - Warp.ogg"
    show c1p7s4 1 with diss
    pause 1.0
    play sfx "sfx/Astral - Portal.ogg"
    show c1p7s4 2
    eddi "公共健身房就是你说的「私密」场所？" with diss
    show c1p7s4 3
    asta "老板今天把它包下来了，说要做维护。" with diss
    asta "别担心，不会有人找到我们。"
    show c1p7s4 4
    eddi "除非有人正好走进来，比如那样。" with diss
    show c1p7s4 5
    mc "没事，他是老板，也是朋友。" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p7s4 6
    sila "嘿，这小子是谁？" with diss
    show c1p7s4 7
    eddi "大家能不能别再叫我{i}小子{/i}了？" with diss
    eddi "我都快十七了。"
    show c1p7s4 8
    sila "抱歉。" with diss
    sila "我当然没有冒犯的意思。"
    show c1p7s4 9
    asta "他叫埃德温。" with diss
    show c1p7s4 10
    eddi "不过我还是喜欢叫埃迪。" with diss
    show c1p7s4 8
    sila "很高兴认识你，埃迪！" with diss
    show c1p7s4 11
    sila "所以他就是你们在找的那个新神裔？" with diss
    show c1p7s4 12
    asta "对。" with diss
    asta "他是元素系的。"
    show c1p7s4 13
    sila "哦，那就是很强的那种了！" with diss
    show c1p7s4 14
    eddi "神裔？" with diss
    show c1p7s4 15
    eddi "你的意思是我是神？！" with diss
    show c1p7s4 16
    asta "还不是。" with diss
    asta "你还没飞升。"
    show c1p7s4 17
    mc "等等……" with diss
    mc "你真信了？"
    mc "就这样？"
    show c1p7s4 18
    eddi "这倒能解释很多事。" with diss
    show c1p7s4 19
    eddi "为什么那些猎法师的人要追我……" with diss
    eddi "为什么他们看到我的能力时那么震惊……"
    eddi "还有为什么我使用魔法时会发光。"
    show c1p7s4 20
    eddi "我从没见过哪个法师那样发光。" with diss
    show c1p7s4 21
    mc "这次倒是轻松。" with diss
    show c1p7s4 22
    asta "再说说这些「猎法师者」的事吧。" with diss
    asta "你知道他们为什么追你吗？"
    show c1p7s4 23
    eddi "不太清楚。" with diss
    eddi "除了我会用魔法之外。"
    show c1p7s4 24
    asta "所以你知道的也不比我多……" with diss
    show c1p7s4 25
    mc "我对这些「猎法师者」一无所知。" with diss
    mc "有人能给我讲讲吗？"
    show c1p7s4 26
    sila "你平时都不看新闻吗？" with diss
    show c1p7s4 27
    mc "你好！" with diss
    mc "昏迷两个月！"
    mc "有点印象了吗？"
    show c1p7s4 28
    sila "哦！" with diss
    sila "对对对。"
    show c1p7s4 29
    sila "那个……猎法师者是个来路不明的组织，专门追踪法师、从街上把他们抓走。" with diss
    sila "没人知道他们是谁，也不知道他们真正想干什么。"
    show c1p7s4 30
    vero "我想我能补充一些你们缺的信息。" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p7s4 31 with diss
    $ CharacterProfile.unlock_outfit([(chara["vero"], 1)])
    pause 1.0
    play sfx "sfx/Footsteps - Wood - Fast.ogg"
    show c1p7s4 32
    asta "呃！" with dism
    asta "这里不欢迎你！"
    show c1p7s4 33
    asta "你怎么找到我们的？！" with diss
    show c1p7s4 34
    vero "那不重要。" with diss
    vero "而且你看……"
    vero "……我知道你不喜欢我。"
    vero "我其实也不喜欢你。"
    vero "话虽如此……"
    show c1p7s4 35
    vero "我认识的人里，只有你和[mc_name]可能帮得了我。" with diss
    show c1p7s4 36
    asta "你为什么会这么想？" with diss
    asta "这么说吧。"
    asta "{i}我们为什么要帮你？{/i}"
    show c1p7s4 35
    vero "你们两个都是神裔。" with diss
    vero "你们强大到我根本无法想象。"
    show c1p7s4 37
    vero "而如果这件事真像我想的那么深，那么无可比拟的力量正是我需要的。" with diss
    show c1p7s4 38
    asta "好吧。" with diss
    asta "告诉我你知道的猎法师者的情报，我就考虑帮你。"
    show c1p7s4 39
    vero "好。" with diss
    vero "说定了。"
    show c1p7s4 40
    vero "那么，猎法师者大约是一个半月前开始活动的，对吧？" with diss
    show c1p7s4 41
    asta "嗯。" with diss
    show c1p7s4 40
    vero "差不多同一时间，守望者军团的成员也开始失踪。" with diss
    vero "我发现这两件事的时间总是对得上。"
    show c1p7s4 42
    vero "先是又一名法师失踪。" with diss
    vero "然后一两天后，又一名守望者失踪。"
    show c1p7s4 43
    mc "守望者也失踪了？" with diss
    mc "公司为什么不调查？"
    show c1p7s4 44
    vero "他们在查。" with diss
    vero "至少据说是这样。"
    show c1p7s4 45
    vero "我向指挥官提出证据时，他说这件事正在「处理中」。" with diss
    show c1p7s4 44
    vero "所以我暂时没再追查。" with diss
    show c1p7s4 46
    vero "但现在，我开始怀疑高层也牵涉其中。" with diss
    show c1p7s4 47
    asta "哦，哇！" with diss
    asta "守望者不过就是个腐败、贪钱的公司，跟外面那些有钱的混蛋一样！"
    show c1p7s4 48
    asta "谁能想到呢？" with diss
    show c1p7s4 49
    eddi "我还以为守望者负责维持和平，防止公司权力膨胀呢？" with diss
    show c1p7s4 50
    asta "所以我还是会叫你小子。" with diss
    show c1p7s4 51
    vero "你们俩能不能安静听我说话？" with diss
    vero "下一部分很重要。"
    show c1p7s4 52
    asta "是，长官！" with diss
    show c1p7s4 53
    vero "呃。" with diss
    show c1p7s4 54
    vero "总之……" with diss
    vero "我怀疑高层牵涉其中的理由是，凯特失踪了。"
    show c1p7s4 55
    mc "就是那个和你一起在医院出现的活泼金发姑娘？" with diss
    show c1p7s4 56
    vero "对，就是她。" with diss
    show c1p7s4 57
    asta "这为什么让你怀疑你的上级？" with diss
    show c1p7s4 58
    vero "她没告诉我她要去哪儿，而且她昨天是排班的。" with diss
    vero "我去接班时，她不在。"
    vero "我又去找指挥官问了一次。"
    vero "他说她去度假了。"
    show c1p7s4 59
    mc "也许她真去了。" with diss
    show c1p7s4 56
    vero "不，她没有。" with diss
    vero "凯特要真想走，肯定会先故意气我一番，或者至少跟我道别。"
    show c1p7s4 60
    vero "昨晚我加班待到很晚，等指挥官走了好去翻他的桌子。" with diss
    show c1p7s4 61
    asta "哇。" with diss
    asta "原来你不是个乖宝宝嘛。"
    show c1p7s4 62
    vero "看来你也不知道怎么在别人说话时{i}不{/i}插嘴。" with diss
    show c1p7s4 63
    mc "别吵了，姑娘们。" with diss
    mc "这事听起来越来越严重了。"
    show c1p7s4 56
    vero "你说得对，确实严重。" with diss
    vero "还记得凯特怎么突然开始念叨48区块吗？"
    show c1p7s4 55
    mc "对，是某种秘密设施对吧？" with diss
    show c1p7s4 56
    vero "说是秘密都算客气的了。" with diss
    vero "即便在守望者内部，也几乎没人知道那里在做什么。"
    show c1p7s4 64
    vero "总之，回到正题。" with diss
    show c1p7s4 56
    vero "我在指挥官的桌子里发现一份清单，上面提到有货物从我们分部发往48区块。" with diss
    vero "可清单上没有货物，只有一个编号……"
    show c1p7s4 65
    vero "……凯特的编号。" with diss
    show c1p7s4 57
    asta "所以你觉得他们把凯特送到48区块去了？" with diss
    asta "也许她只是被调岗，有特权知道那里的事。"
    show c1p7s4 54
    vero "如果我真这么信，那倒是没问题。" with diss
    vero "可太多地方对不上了。"
    show c1p7s4 53
    vero "她没告诉我她要走。" with diss
    vero "她的排班还在{i}我们{/i}这边。"
    vero "而且他们用的是他妈的货运清单来记录，而不是正规的调令。"
    show c1p7s4 58
    vero "再加上，指挥官说她去度假了！" with diss
    show c1p7s4 66
    asta "你说得对……" with diss
    asta "矛盾太多了。"
    show c1p7s4 67
    mc "我们能怎么帮？" with diss
    show c1p7s4 68
    asta "我可没说想帮忙！" with diss
    show c1p7s4 56
    vero "一个神裔总比没有强。" with diss
    vero "有多少我就要多少。"
    vero "我要试着找出48区块的确切位置。"
    vero "找到了之后，我要你们冲进去把凯特带出来。"
    show c1p7s4 69
    toge "什么？！" with hpunch
    show c1p7s4 70
    mc "你要我独自闯进一个超级机密、重兵把守、进行着不可告人之事、还属于这个星球上最强大战斗力量的设施？！" with diss
    mc "就我一个人？！"
    show c1p7s4 71
    vero "好吧，骑士团严格来说是这个世界最强的战斗力量……" with diss
    vero "……但单个神裔攻进去过。"
    show c1p7s4 70
    mc "对，可你不是抓住那个人了吗？" with diss
    show c1p7s4 56
    vero "没有。" with diss
    vero "他大肆破坏，屠了几百名士兵，然后就走了。"
    show c1p7s4 72
    asta "我真想见见这个神裔……" with diss
    show c1p7s4 73
    mc "认真的吗，阿斯塔拉？" with diss
    mc "他听起来很危险。"
    show c1p7s4 74
    asta "只要他打的是对的人、对的地方，我没问题。" with diss
    show c1p7s4 75
    eddi "哇。" with diss
    eddi "你真的很恨守望者。"
    show c1p7s4 56
    vero "那么，你愿意吗？" with diss
    vero "你愿意帮我把凯特带回来吗？"
    show c1p7s4 67
    mc "我肯定会后悔的……但好，我答应。" with diss
    show c1p7s4 66
    asta "我也算一个。" with diss
    asta "但不是为了你，也不是为了凯特。"
    asta "我有自己的理由想去那里。"
    show c1p7s4 64
    vero "随便吧。" with diss
    vero "只要你们把我朋友带回来，你们做什么我都不在乎。"
    show c1p7s4 60
    vero "现在我只需要想办法找到这个地方……" with diss
    show c1p7s4 68
    asta "莱拉能查到吗？" with diss
    asta "她在技术方面简直是巫师，而且现在一切都上网了。"
    show c1p7s4 76
    mc "这倒是。" with diss
    mc "她以前也确实查到过一些关于48区块的东西。"
    show c1p7s4 77
    mc "我去联系她，看看能挖出什么。" with diss
    show c1p7s4 71
    vero "万一她查不到，我自己也去试试。" with diss
    show c1p7s4 78
    vero "对我来说又是一个漫长的夜晚。" with diss
    show c1p7s4 79
    vero "谢谢你们俩答应。" with diss
    vero "如果你们把凯特带回来，我欠你们的，这辈子都还不清。"
    $ choice1 = ChoiceOption(
        "你不会欠我任何东西。",
        stats={"vero": {"affection": 5}, "asta": {"affection": -3},"mc": {"karma": 5}},
    )
    $ choice2 = ChoiceOption(
        "那当然没错。",
        stats={"asta": {"affection": 3}, "mc": {"karma": -5}},
    )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            show c1p7s4 80
            mc "你不欠我什么。" with diss
            mc "我这么做是为了所有被带走的人，不只是凯特。"
            show c1p7s4 81
            vero "也许我之前看错你了。" with diss
            vero "你看起来其实是个好人。"
            show c1p7s4 82
            mc "我在努力做好人，但没人是完美的。" with diss
            show c1p7s4 81
            vero "你愿意为素不相识的人做到这种程度，这本身就说明你是什么样的人。" with diss
        "[choice2.get_display_text()]":
            $ choice2.apply_stats()
            show c1p7s4 80
            mc "那当然。" with diss
            mc "既然我要花时间、赌性命，你们就欠我大人情。"
            show c1p7s4 83
            vero "我会想办法报答你们的，别担心。" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p7s4 84
    vero "我还有很多事要做。" with diss
    vero "我明天差不多一点在这儿碰面。"
    show c1p7s4 86
    eddi "那个人是谁？" with diss
    show c1p7s4 87
    asta "不重要。" with diss
    show c1p7s4 88
    asta "我不信任她，你也不该信，[mc_name]。" with diss
    show c1p7s4 89
    mc "如果她说的是真的，那48区块里可能有很多答案。" with diss
    show c1p7s4 90
    asta "什么答案？" with diss
    show c1p7s4 89
    mc "原初者说战争要来了。" with diss
    mc "不只是神裔之间，还包括那些权力膨胀的公司。"
    mc "按他的说法，这才是神裔能再次使用神力的原因。"
    show c1p7s4 91
    asta "我开始越来越不喜欢这个计划了。" with diss
    show c1p7s4 92
    eddi "可我也是神裔！" with diss
    eddi "需要额外支援的话可以带上我。"
    show c1p7s4 93
    asta "带上那个刚因为「想错了」就攻击我们的小子？" with diss
    asta "免了。"
    asta "你在当神裔这回事上还有很多要学，情绪也太不稳定，不适合这种任务。"
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p7s4 94
    asta "埃迪，你在这儿等一下，我得跟[mc_name]单独谈谈。" with diss
    show c1p7s4 95
    eddi "是，长官……" with diss
    show c1p7s4 96
    mc "怎么了，阿斯塔拉？" with diss
    show c1p7s4 97
    asta "还记得我提过我的{i}任务{/i}吗？" with diss
    show c1p7s4 96
    mc "当然记得。" with diss
    show c1p7s4 98
    asta "那是我答应的原因。" with diss
    asta "我已经对守望者打了很久的单人战争了。"
    asta "不过直到我获得力量，才开始尝到胜利的滋味。"
    show c1p7s4 96
    mc "对守望者宣战……" with diss
    mc "为什么？"
    show c1p7s4 99
    asta "因为……" with diss
    asta "……我现在不想谈这个。"
    show c1p7s4 100
    mc "（还是那么神秘。）" with diss
    show c1p7s4 101
    mc "我明白了……" with diss
    show c1p7s4 102
    asta "我一直在考虑像之前说的那样找些帮手，但我不确定自己是否想这么做。" with diss
    show c1p7s4 103
    asta "看了你对付埃迪的表现，你的头脑和近身格斗的技巧……" with diss
    show c1p7s4 104
    asta "我觉得我身边真的很需要一个你这样的人……如果你愿意帮我。" with diss
    show c1p7s4 105
    mc "这要看你打算让我做什么。" with diss
    mc "没有正当理由，我不想杀人。"
    show c1p7s4 106
    asta "有时候你可能别无选择。" with diss
    show c1p7s4 107
    asta "不管怎样，我只是把这个提议摆出来，现在别做决定。" with diss
    asta "我们还有更大的事要操心。"
    if chara["asta"].get_stat("affection") >= 15:
        show c1p7s4 108
        asta "我想说的只是……我信任你。" with diss
        asta "你向我证明了自己相当有能力，这对我意义重大。"
        show c1p7s4 109
        mc "谢谢你的信任。" with diss
    else:
        show c1p7s4 110
        asta "别以为这意味着你是特别的人，或是唯一能帮我的人。" with diss
        asta "我只是觉得你很强，而这可能有用。"
        show c1p7s4 111
        mc "哎呀，谢谢。" with diss
    mc "我会好好考虑，等48区块这摊事结束后给你答复。"
    show c1p7s4 112
    asta "谢谢你，[mc_name]。" with diss
    show c1p7s4 113
    asta "我现在得回去看着埃迪，免得他无聊跑了。" with diss
    show c1p7s4 114
    mc "好，我试着联系莱拉。" with diss
    mc "然后回家。"
    show c1p7s4 115
    asta "好。" with diss
    asta "回头见，[mc_name]。"
    stop bgs fadeout 1.0
    stop bgm fadeout 1.0
    hide c1p7s4
    scrn "给莱拉发完消息后，你一整天都在家度过。" with diss
    jump c1p8s1

label c1p8s1:
    scene black
    show magic_effect at theme_ember
    with fadeb
    play sfx "sfx/Chapter - In.ogg"
    show c1p8 as c1p8_blur at text_glow
    show c1p8
    with staticflow
    $ save_name = "第1-8章：风暴"
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide c1p8
    hide c1p8_blur
    hide magic_effect
    with grunge
    pause 0.5
    play bgm "bgm/New Day.ogg"
    show c1p8s1 1
    mc "{i}*打哈欠*{/i}" with diss
    show c1p8s1 2
    mc "（嗯……莱拉还是没回我……）" with diss
    show c1p8s1 3
    mc "（我开始有点担心了。）" with diss
    show c1p8s1 4
    mc "（希望维罗妮卡找到了48区块的位置。）" with diss
    show c1p8s1 5
    mc "（好的一面是，这个早晨总算归我一个人了。）" with diss
    show c1p8s1 6
    mc "（没有传送门打开……）" with diss
    show c1p8s1 7
    mc "（没有敲门声……）" with diss
    show c1p8s1 8
    mc "（这会是美好的一天。）" with diss
    stop bgm fadeout 3.0
    hide c1p8s1
    scrn "你享用了这个早晨，然后出发去和维罗妮卡、阿斯塔拉会合。" with diss
    play bgm "bgm/Fitness.ogg"
    play sfx "sfx/Astral - Portal.ogg"
    show c1p8s1 9 with diss
    pause 1.0
    show c1p8s1 10
    mc "（看来她们俩都到了。）" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p8s1 11
    asta "嘿，[mc_name]！" with diss
    asta "我们来早了一点。"
    show c1p8s1 12
    mc "我看到了。" with diss
    mc "你们找到位置了吗？"
    play sfx "sfx/Bag - Leather - Open.ogg"
    show c1p8s1 13
    vero "这是我找到的所有关于48区块的资料。" with diss
    show c1p8s1 14
    vero "里面还有一张地图，帮你找到那里。" with diss
    play sfx "sfx/Footsteps - Wood.ogg"
    show c1p8s1 15
    asta "我先快速过一遍。" with diss
    asta "准备好出发我就来找你。"
    show c1p8s1 16
    vero "再次感谢你们答应去救凯特。" with diss
    show c1p8s1 17
    mc "我只希望她真的在那儿。" with diss
    show c1p8s1 18
    vero "嗯，我也希望。" with diss
    vero "不过我想他们不会把她转移到别处。"
    show c1p8s1 17
    mc "希望不会。" with diss
    mc "话说你和凯特之间是怎么回事？"
    show c1p8s1 16
    vero "我们在成为守望者之前，是同一所训练学校的。" with diss
    vero "那段日子让我们走到一起，成了好朋友。"
    show c1p8s1 17
    mc "那里的训练是什么样的？" with diss
    mc "我听说要真正毕业成为正式守望者非常难。"
    show c1p8s1 19
    vero "那个地方的恐怖故事我能讲上一大堆。" with diss
    vero "前提是我别讲得太烂。"
    show c1p8s1 17
    mc "就算讲得烂我也想听。" with diss
    show c1p8s1 16
    vero "也许改天吧。" with diss
    vero "希望到时候我们已经把凯特带回来，让她把这些故事讲得绘声绘色。"
    show c1p8s1 17
    mc "她确实像是会讲好故事的人。" with diss
    mc "那我就等把她带回来之后再说吧。"
    show c1p8s1 20
    asta "好了，[mc_name]，我们走吧。" with diss
    show c1p8s1 21
    mc "那我该动身了。" with diss
    mc "回头见。"
    show c1p8s1 22
    vero "你们两个都要小心！" with diss
    vero "都是！"
    show c1p8s1 23
    asta "我一直都很小心！" with diss
    stop bgm fadeout 3.0
    play bgs "bgs/City - Day.ogg"
    hide c1p8s1 with diss
    pause 1.0
    show c1p8s1 24 with diss
    pause 1.0
    show c1p8s1 25
    mc "摩托车？" with diss
    mc "为什么不直接传送？"
    show c1p8s1 26
    asta "你把之前学的都忘了吗？" with diss
    show c1p8s1 27
    asta "不能传送到我从没去过的地方。" with diss
    asta "那简直是自找残废。"
    show c1p8s1 28
    mc "对，我忘了。" with diss
    mc "所以……坐得下两个人吗？"
    show c1p8s1 29
    asta "你自己没有车吗？" with diss
    show c1p8s1 28
    mc "呃，没有。" with diss
    show c1p8s1 30
    asta "那你就跟我一起吧。" with diss
    asta "不过这车可不是为两个人设计的。"
    play sfx "sfx/Motorcycle - Get On.ogg"
    show c1p8s1 31 with diss
    pause 1.0
    if chara["asta"].get_stat("affection") >= 15:
        show c1p8s1 32
        asta "抓稳我。" with diss
        play sfx "sfx/Cloth2.ogg"
        show c1p8s1 33 with diss
        pause 1.0
        show c1p8s1 34
        asta "好吧，也许别抓得{i}这么{/i}紧。" with diss
        show c1p8s1 36
        mc "哦！" with diss
        mc "抱歉！"
        show c1p8s1 35
        asta "没事。" with diss
        show c1p8s1 36
        asta "出发！" with diss
    else:
        show c1p8s1 32
        asta "最好别掉下去！" with diss
        show c1p8s1 35
        mc "我不会的。" with diss
        asta "随你怎么说。" with diss
        asta "不过我警告你，我开车像疯女人一样。"
        show c1p8s1 36
        asta "出发！" with diss
    play sfx "sfx/Motorcycle - Start.ogg"
    stop bgs fadeout 3.0
    hide c1p8s1
    scrn "你和阿斯塔拉在路上开了几个小时后，到达了48区块。" with diss
    jump c1p8s2

label c1p8s2:
    play bgm "bgm/Before the Storm.ogg" fadein 3.0
    play bgs "bgs/Desert - Day.ogg" fadein 3.0
    show c1p8s2 1 with diss
    mc "{i}这{/i}就是48区块？！" with diss
    mc "我就知道不会轻松，但天啊。"
    mc "我都不知道还有这种技术存在！"
    show c1p8s2 2
    asta "我也一样。" with diss
    asta "我开始理解这个地方为什么如此保密了。"
    show c1p8s2 3
    asta "我敢说里面还有更多这种技术。" with diss
    show c1p8s2 4
    mc "你看到那些炮了吗？！" with diss
    show c1p8s2 5
    mc "我们根本不可能靠近！" with diss
    mc "更别说进去了！"
    show c1p8s2 6
    asta "好了好了，别慌。" with diss
    asta "这肯定比我习惯的更难，不过这不是我第一次潜入。"
    show c1p8s2 7
    mc "所以你有计划了。" with diss
    show c1p8s2 8
    asta "还没有，但给我点时间，我会想出来的。" with diss
    asta "不过我们冲进去前应该先休息一下。"
    play sfx "sfx/Footsteps - Sand.ogg"
    show c1p8s2 9
    asta "我们不能又渴又累地去打那种堡垒。" with diss
    asta "我们需要每一分力气。"
    mc "完全同意。" with diss
    hide c1p8s2
    scrn "阿斯塔拉传送了几次，带回一些补给，让你俩休息恢复。" with diss
    show c1p8s2 10
    mc "除了炽烈的阳光和漫天沙尘，这儿其实挺宁静的。" with diss
    show c1p8s2 11
    asta "因为这里太偏僻，唯一能听见的只有风卷着沙子掠过的声音。" with diss
    show c1p8s2 12
    mc "比起城市里的各种气味和噪音，这里真是种享受。" with diss
    show c1p8s2 13
    asta "是啊……" with diss
    show c1p8s2 14
    mc "你没事吧，阿斯塔拉？" with diss
    show c1p8s2 15
    asta "嗯？" with diss
    show c1p8s2 16
    asta "哦——呃——没事，我很好。" with diss
    asta "只是我不习惯执行这种任务时身边有人。"
    show c1p8s2 17
    asta "其实……我根本不习惯身边有人。" with diss
    show c1p8s2 18
    asta "我一直都是独狼。" with diss
    asta "无论是我的任务……还是生活里其他一切。"
    show c1p8s2 19
    asta "说实话，我常常觉得自己很孤独。" with diss
    show c1p8s2 18
    asta "但我不能让任何东西分散我的注意力。" with diss
    asta "我的任务永远排在第一位。"
    show c1p8s2 20
    mc "我能理解。" with diss
    mc "但你终究是人。"
    mc "好吧，也许不完全是人，但你的心智运转还是同样的道理，同样的需求。"
    show c1p8s2 21
    mc "每个人都需要陪伴。" with diss
    show c1p8s2 22
    asta "我不需要。" with diss
    asta "我不会让自己和任何人靠得那么近，也不会让任何人靠我那么近。"
    show c1p8s2 23
    mc "因为你觉得他们会离开你？" with diss
    show c1p8s2 24
    mc "「不管怎样，他们总会离开」，对吧？" with diss
    show c1p8s2 25
    asta "是啊……" with diss
    $ choice1 = ChoiceOption(
        "你也许是对的。", 
        stats={"asta": {"affection": 3}},
    )
    $ choice2 = ChoiceOption(
        "那我就不去了。", 
        stats={"asta": {"affection": 5}},
    )
    $ choice3 = ChoiceOption(
        "你就那么死心眼吗？", 
        stats={"asta": {"affection": -3}},
    )
    $ choice4 = ChoiceOption(
        "你为什么会这么想？", 
    )
    menu asta_loneliness:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            $ asta_lonely = 1
            show c1p8s2 26
            mc "你可能说对了。" with diss
            mc "但你也可能错了。"
            mc "有些人能做好朋友、好家人、甚至恋人很多年。"
            show c1p8s2 27
            asta "我生命里没有这种人。" with diss
            show c1p8s2 28
            mc "那只是说明你还没遇到对的人。" with diss
        "[choice2.get_display_text()]":
            $ choice2.apply_stats()
            $ asta_lonely = 2
            show c1p8s2 26
            mc "好吧，我不会的。" with diss
            show c1p8s2 27
            asta "所以你已经悟出了真正永生的秘诀，嗯？" with diss
            show c1p8s2 28
            mc "什么？" with diss
            mc "才不是。"
            show c1p8s2 30
            asta "那你怎么可能知道？" with diss
            show c1p8s2 31
            mc "因为我想把我们现在是朋友这件事当真，而且不想让它改变。" with diss
            show c1p8s2 25
            asta "你并不总能选择……" with diss
            show c1p8s2 26
            mc "好吧，反正我暂时不打算死，既然你说的是这个。" with diss
        "[choice3.get_display_text()]":
            $ choice3.apply_stats()
            $ asta_lonely = 3
            show c1p8s2 32
            mc "你真那么固执？" with diss
            play sfx "sfx/Sand - Shift.ogg"
            show c1p8s2 33
            asta "那不是固执，是现实。" with diss
            asta "你该找个时候在现实里生活一下。"
            show c1p8s2 37
            mc "我就是生活在现实里，而且我的现实里有守在我身边的朋友。" with diss
            show c1p8s2 38
            asta "真的吗？" with diss
            asta "那莱拉怎么没找到48区块？"
            show c1p8s2 39
            asta "按她的性子，她也会跟你一起去见维罗妮卡的。" with diss
            asta "那她为什么没来？"
            show c1p8s2 37
            mc "我不知道。" with diss
            mc "她又不是黏在我身上。"
            show c1p8s2  40
            asta "也许不是，但她不会错过这种事。" with diss
            asta "我不会让她跟我们来这儿，但就我对她的了解，她至少会来给你送行。"
            show c1p8s2 37
            mc "够了！" with diss
            mc "不关你的事！"
            show c1p8s2 38
            asta "我的感情也不关你的事！" with diss
            asta "给我专心，不然我们都得死！"
            play sfx "sfx/Footsteps - Sand.ogg"
            show c1p8s2 35 with diss
            pause 1.0
            show c1p8s2 36
            mc "（我真不懂这个女人。）" with diss
            show c1p8s2 41
            mc "（不过她说到莱拉那点倒是对的。）" with diss
            mc "（也许我根本不懂{i}任何{/i}女人……）"
        "[choice4.get_display_text()]" if not asta_lonely_c4:
            $ choice4.apply_stats()
            show c1p8s2 26
            mc "你为什么这么想？" with diss
            $ asta_lonely_c4 = True
            show c1p8s2 27
            asta "因为永远都是这样。" with diss
            show c1p8s2 29
            asta "要么人们厌倦你，要么开始恨你，要么他们死了……" with diss
            show c1p8s2 27
            asta "最后结果都一样。" with diss
            jump asta_loneliness
    if asta_lonely in [1, 2]:
        play sfx "sfx/Sand - Shift.ogg"
        show c1p8s2 33
        asta "呃，你看！" with diss
        asta "我知道你想做什么，我也很感激，真的……"
        show c1p8s2 34
        asta "……但现在我们有比我的感情重要得多的事情要担心！" with diss
        asta "把注意力放在目标上，不然我们都得死！"
        play sfx "sfx/Footsteps - Sand.ogg"
        show c1p8s2 35 with diss
        pause 1.0
        show c1p8s2 36
        mc "（这就是我想和她交朋友的下场……）" with diss
    hide c1p8s2
    scrn "过了一会儿……" with diss
    play sfx "sfx/Footsteps - Sand.ogg"
    show c1p8s2 42 with diss
    pause 1.0
    show c1p8s2 43
    asta "集中精神了吗？" with diss
    show c1p8s2 44
    mc "嗯。" with diss
    show c1p8s2 45
    asta "很好，因为我有计划了。" with diss
    show c1p8s2 46
    asta "那些炮其实不算问题，我们可以直接传送到他们视野后面。" with diss
    show c1p8s2 47
    mc "好，就是传送到他们身后，明白了。" with diss
    show c1p8s2 48
    asta "不对。" with diss
    asta "不是传送门……是瞬移。"
    show c1p8s2 49
    mc "有区别吗？" with diss
    show c1p8s2 50
    asta "算是吧。" with diss
    asta "你记得我和维罗妮卡的那场战斗吗？"
    show c1p8s2 49
    mc "哦，对！" with diss
    mc "那场战斗中我完全没见过传送门！"
    show c1p8s2 50
    asta "对，因为我用的不是传送门。" with diss
    show c1p8s2 49
    mc "我做不到。" with diss
    show c1p8s2 51
    asta "暂时做不到，但你的力量可以模仿别人。" with diss
    asta "你不能像之前那样，在我瞬移时感知我的能量，再学着自己塑形吗？"
    show c1p8s2 49
    mc "也许可以。" with diss
    mc "之前很容易，但这对我来说还是很新的概念。"
    show c1p8s2 52
    asta "试试就知道了。" with diss
    play sfx "sfx/Footsteps - Sand.ogg"
    show c1p8s2 53
    asta "来吧。" with diss
    show c1p8s2 54
    asta "好，我瞬移到几英尺外。" with diss
    asta "在我瞬移前后，都仔细注意我周围的能量。"
    show c1p8s2 55 with diss
    pause 1.0
    play sfx "sfx/Astral - Warp.ogg"
    show c1p8s2 56 with diss
    pause 1.0
    show c1p8s2 57 with diss
    pause 1.0
    play sfx "sfx/Footsteps - Sand.ogg"
    show c1p8s2 58
    asta "现在你试试。" with diss
    asta "这和制造传送门几乎一样，只是能量的用法不同。"
    show c1p8s2 59
    asta "在脑中清楚地想象你要去的位置，然后不是开一道门，而是把自己放到那里。" with diss
    show c1p8s2 60
    mc "好，试试看。" with diss
    play sfx "sfx/Astral - Warp.ogg"
    show c1p8s2 61 with diss
    pause 1.0
    show c1p8s2 62 with diss
    pause 1.0
    show c1p8s2 63
    asta "我真惊讶！" with diss
    asta "你学得好快！"
    play sfx "sfx/Footsteps - Sand.ogg"
    show c1p8s2 64
    asta "现在回到计划。" with diss
    show c1p8s2 48
    asta "越过那些炮之后，我们得真正进入基地。" with diss
    asta "顶上有个通风口，很可能是用来把新鲜空气送到地下各层的。"
    asta "我们就从那儿进去。"
    asta "然后，我们只要找到基地的地图或图纸，看看能不能定位他们存放文件的地方，并希望里面有些能让这一切值得的东西。"
    show c1p8s2 47
    mc "对。" with diss
    mc "听起来够简单。"
    show c1p8s2 50
    asta "我们还得找到安保中枢，把摄像头画面清掉。" with diss
    show c1p8s2 49
    mc "我们可不想像第一个攻进这里的神裔那样，被全网通缉。" with diss
    show c1p8s2 50
    asta "完全正确。" with diss
    asta "希望你擅长潜行。"
    asta "我可不想对付整个基地，就算有支援。"
    show c1p8s2 49
    mc "我会像忍者一样。" with diss
    show c1p8s2 50
    asta "希望如此。" with diss
    show c1p8s2 49
    asta "里面见！" with diss
    play sfx "sfx/Astral - Warp.ogg"
    show c1p8s2 66 with diss
    pause 1.0
    show c1p8s2 67
    mc "（我能做到。）" with diss
    play sfx "sfx/Astral - Warp.ogg"
    show c1p8s2 68 with diss
    pause 1.0
    show c1p8s2 69
    asta "你做到了！" with diss
    asta "很好。"
    show c1p8s2 70
    asta "现在去那个通风口。" with diss
    stop bgm fadeout 3.0
    stop bgs fadeout 3.0
    hide c1p8s2
    scrn "你和阿斯塔拉进入通风系统，潜入了基地。" with diss
    jump c1p8s3

label c1p8s3:
    play bgm "bgm/Stealth Operation.ogg" fadein 1.0
    play bgs "bgs/Sector 48 - Server.ogg" fadein 3.0
    show c1p8s3 1 with diss
    pause 1.0
    asta "{i}*压低声音*{/i} 快点了。" with diss
    asta "{i}*压低声音*{/i} 我讨厌这么狭窄的地方。"
    mc "{i}*压低声音*{/i} 我已经尽力了。" with diss
    mc "{i}*压低声音*{/i} 这里看起来就是主监控室。"
    asta "{i}*压低声音*{/i} 那就从这儿出去吧。" with diss
    asta "{i}*压低声音*{/i} 没有守卫？"
    mc "{i}*压低声音*{/i} 没有。" with diss
    asta "{i}*压低声音*{/i} 好，那走吧。" with diss
    play sfx "sfx/Vent - Open.ogg"
    show c1p8s3 2 with diss
    pause 1.0
    play sfx "sfx/Jump - Landing.ogg"
    show c1p8s3 3 with diss
    pause 1.0
    play sfx "sfx/Jump - Landing.ogg"
    show c1p8s3 4 with diss
    pause 1.0
    show c1p8s3 5
    asta "干得漂亮。" with diss
    asta "这肯定就是我们要找的地方。"
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 6
    asta "开始翻查这里所有的文件。" with diss
    asta "我去把摄像头画面清掉，再让它们停机几个小时。"
    mc "明白。" with diss
    play sfx "sfx/Drawer - Metal - Open.ogg"
    show c1p8s3 7 with diss
    pause 1.0
    show c1p8s3 8
    mc "不可能！" with diss
    show c1p8s3 9
    mc "阿斯塔拉，来看这个！" with diss
    show c1p8s3 10
    asta "什么？" with diss
    asta "你发现什么重要的东西了吗？"
    show c1p8s3 11
    mc "「考古学家发现了能引领我们找到最后一位在世神明下落的{i}钥匙{/i}。」" with diss
    show c1p8s3 12
    asta "他们找到最后的神了？！" with diss
    show c1p8s3 13
    mc "对……" with diss
    show c1p8s3 14
    mc "……而且是借助了{i}我父亲{/i}的协助。" with diss
    show c1p8s3 15
    asta "你父亲？" with diss
    asta "就是那位已经去世的？"
    show c1p8s3 16
    mc "对。" with diss
    mc "这是他多年前失踪的那次考古之旅的资料。"
    show c1p8s3 17
    mc "他的队伍当时正在发掘一座供奉最后的真神的神庙，随后遭到袭击。" with diss
    mc "协会说他们从未找到他的遗体……但他也再没回家。"
    show c1p8s3 18
    asta "你说的是失踪，不是死亡。" with diss
    show c1p8s3 15
    asta "这意味着他可能还活着。" with diss
    asta "甚至可能被关在这里。"
    show c1p8s3 16
    mc "太久了……" with diss
    mc "我不敢让自己抱希望。"
    show c1p8s3 19
    asta "那最后的真神呢？" with diss
    asta "资料上怎么写的？"
    show c1p8s3 16
    mc "不多。" with diss
    mc "这份甚至都没确认他们有没有找到他。"
    show c1p8s3 18
    asta "该死。" with diss
    show c1p8s3 15
    asta "继续翻那些文件。" with diss
    asta "我们在找任何能用来关押囚犯的东西。"
    asta "也留意其他关于最后的真神的情报。"
    asta "我想知道守望者为什么对他这么感兴趣。"
    show c1p8s3 16
    mc "好。" with diss
    hide c1p8s3 with diss
    pause 1.0
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 20
    mc "在这里！" with diss
    mc "我找到东西了！"
    play sfx "sfx/Paper - Unfold.ogg"
    show c1p8s3 21
    mc "看来他们把人关在最底层。" with diss
    show c1p8s3 22
    asta "那我们就去那儿。" with diss
    show c1p8s3 23
    asta "走吧。" with diss
    hide c1p8s3 with diss
    pause 1.0
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 24 with diss
    pause 1.0
    show c1p8s3 25 with diss
    pause 1.0
    play sfx "sfx/Footsteps - Metal - Take Cover.ogg"
    show c1p8s3 26
    asta "{i}*压低声音*{/i} 等等，退后！" with diss
    asta "{i}*压低声音*{/i} 这个交给我。"
    play sfx "sfx/Footsteps - Metal - Run.ogg"
    show c1p8s3 27 with diss
    pause 1.0
    play sfx "sfx/Whoosh - Air.ogg"
    show c1p8s3 28 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Punch - Hit.ogg"
    show c1p8s3 29 with hpunch
    pause 0.5
    show c1p8s3 30
    asta "安全。" with diss
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 31
    mc "该死，一拳就解决了？" with diss
    show c1p8s3 32
    asta "我也有练过好吧。" with diss
    asta "继续走。"
    hide c1p8s3 with diss
    pause 1.0
    show c1p8s3 33 with diss
    pause 1.0
    show c1p8s3 34
    asta "{i}*压低声音*{/i} 这次有两个。" with diss
    asta "{i}*压低声音*{/i} 你解决左边那个。"
    show c1p8s3 35
    mc "明白。" with diss
    show c1p8s3 36 with diss
    pause 1.0
    play sfx "sfx/Fight - Kick - Miss.ogg"
    show c1p8s3 37 with hpunch
    pause 0.5
    play sfx "sfx/Cloth2.ogg"
    show c1p8s3 38 with diss
    pause 1.0
    play sfx "sfx/Body - Drop - Light.ogg"
    show c1p8s3 39 with diss
    pause 1.0
    show c1p8s3 40
    mc "这扇门应该通往电梯，能一路下到我们要找的地下层。" with diss
    stop bgm fadeout 5.0
    hide c1p8s3 with diss
    pause 1.0
    play sfx "sfx/Elevator - Open.ogg"
    show c1p8s3 41 with diss
    pause 1.0
    show c1p8s3 42
    ssent "什——？" with diss
    play sfx "sfx/Gun - Rifle - Sent - Handle.ogg"
    show c1p8s3 43
    ssent "不许动！" with hpunch
    show c1p8s3 44
    mc "该死！" with diss
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 45 with diss
    pause 1.0
    play bgm "bgm/Astara Battle Theme.ogg" fadein 5.0
    show c1p8s3 46
    mc "阿斯塔拉！" with diss
    mc "你在干什——？"
    show c1p8s3 47
    ssent "现在转过身来！" with diss
    show c1p8s3 48 with diss
    pause 0.5
    play sfx "sfx/Fight - Punch - Block.ogg"
    show c1p8s3 49 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Punch - Hit.ogg"
    show c1p8s3 50 with hpunch
    pause 0.5
    show c1p8s3 51
    ssent "这就是你们的本事？" with diss
    play sfx "sfx/Cloth2.ogg"
    show c1p8s3 52 with hpunch
    pause 0.5
    play sfx "sfx/Whoosh - Air.ogg"
    show c1p8s3 53 with diss
    pause 0.3
    play sfx "sfx/Crash - Metal.ogg"
    show c1p8s3 54 with hpunch
    show c1p8s3 55 with diss
    pause 1.0
    show c1p8s3 56
    mc "阿斯塔拉！" with diss
    show c1p8s3 57
    asta "呃啊，我……我没事。" with diss
    show c1p8s3 58
    asta "他会后悔的！" with diss
    show c1p8s3 59
    ssent "她是神裔！" with diss
    ssent "开火！"
    play sfx "sfx/Gun - Rifle - Sent - Handle.ogg"
    show c1p8s3 60
    ssent "只准用非致命弹药！" with diss
    show c1p8s3 61 with mhpunch
    play sfx "sfx/Gun - Rifle - Sent - Shoot.ogg"
    pause 0.2
    show c1p8s3 61 with mhpunch
    play sfx2 "sfx/Gun - Rifle - Sent - Shoot.ogg"
    pause 0.2
    show c1p8s3 61 with mhpunch
    play sfx3 "sfx/Gun - Rifle - Sent - Shoot.ogg"
    pause 0.2
    show c1p8s3 61 with mhpunch
    play sfx "sfx/Gun - Rifle - Sent - Shoot.ogg"
    pause 0.3
    show c1p8s3 61 with mhpunch
    play sfx2 "sfx/Gun - Rifle - Sent - Shoot.ogg"
    pause 0.3
    show c1p8s3 61 with mhpunch
    play sfx3 "sfx/Gun - Rifle - Sent - Shoot.ogg"
    pause 0.3
    show c1p8s3 62 with diss
    pause 1.0
    show c1p8s3 63
    ssent "她人呢？！" with diss
    play sfx "sfx/Astral - Warp.ogg"
    show c1p8s3 64 with diss
    pause 1.0
    play sfx "sfx/Astral - Simple.ogg"
    show c1p8s3 65 with diss
    pause 1.0
    play sfx "sfx/Fight - Punch - Hit.ogg"
    play sfx2 "sfx/Astral - Blow2.ogg"
    show c1p8s3 66 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Punch - Hit.ogg"
    play sfx2 "sfx/Astral - Blow2.ogg"
    show c1p8s3 67 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Kick - Miss.ogg"
    play sfx2 "sfx/Whoosh - Air.ogg"
    show c1p8s3 68 with hpunch
    pause 0.5
    play sfx "sfx/Crash - Metal.ogg"
    show c1p8s3 69 with hpunch
    pause 1.0
    show c1p8s3 70 with diss
    pause 1.0
    show c1p8s3 71 with diss
    pause 1.0
    show c1p8s3 72
    asta "[mc_name]！" with diss
    asta "你就打算站着不动？！"
    show c1p8s3 73
    mc "哦呃——不！" with diss
    mc "抱歉！"
    play sfx "sfx/Footsteps - Metal - Run.ogg"
    show c1p8s3 74 with diss
    pause 1.0
    play sfx "sfx/Whoosh.ogg"
    show c1p8s3 75 with diss
    pause 1.0
    show c1p8s3 76
    ssent "他也是神裔？！" with diss
    play sfx "sfx/Fight - Punch - Hit.ogg"
    show c1p8s3 77 with hpunch
    pause 0.5
    play sfx "sfx/Fight - Punch - Hit.ogg"
    show c1p8s3 78 with hpunch
    pause 0.5
    play sfx "sfx/Footsteps - Metal - Take Cover.ogg"
    show c1p8s3 79 with diss
    pause 1.0
    show c1p8s3 80
    asta "这铠甲太硬了。" with diss
    asta "再打下去我的手要废了。"
    show c1p8s3 81
    asta "管他的！" with diss
    asta "我现在就解决掉！"
    play sfx "sfx/Astral - Portal.ogg"
    show c1p8s3 82 with diss
    pause 0.2
    play sfx2 "sfx/Astral - Portal.ogg"
    show c1p8s3 83 with diss
    pause 0.01
    play sfx3 "sfx/Astral - Portal.ogg"
    show c1p8s3 84 with diss
    pause 0.01
    play sfx2 "sfx/Astral - Portal.ogg"
    show c1p8s3 85 with diss
    pause 0.01
    play sfx "sfx/Cloth2.ogg"
    show c1p8s3 86 with hpunch
    pause 0.5
    play sfx "sfx/Cloth3.ogg"
    show c1p8s3 86a with hpunch
    pause 0.5
    play sfx "sfx/Fight - Kick - Miss.ogg"
    play sfx2 "sfx/Whoosh - Air.ogg"
    show c1p8s3 87 with hpunch
    pause 0.5
    play sfx "sfx/Body - Drop - Light.ogg"
    show c1p8s3 88 with hpunch
    pause 0.5
    play sfx "sfx/Astral - Warp.ogg"
    show c1p8s3 89 with diss
    pause 1.0
    stop bgm fadeout 3.0
    play sfx "sfx/Fight - Eviscerate.ogg"
    play sfx2 "sfx/Astral - Warp.ogg"
    show c1p8s3 90 with hpunchs
    pause 1.0
    show c1p8s3 91
    mc "我的天，阿斯塔拉！" with diss
    $ choice1 = ChoiceOption(
            "你非杀了他们不可吗？！", 
            stats={"mc": {"karma": 5}},
        )
    $ choice2 = ChoiceOption(
            "那帮混蛋活该！", 
            stats={"mc": {"karma": -5}},
        )
    menu:
        "[choice1.get_display_text()]":
            $ choice1.apply_stats()
            show c1p8s3 92
            mc "你非得杀了他们不可吗？！" with diss
            show c1p8s3 93
            asta "你希望他们杀了我们？" with diss
            show c1p8s3 94
            mc "我倒是希望谁都别死！" with diss
            show c1p8s3 95
            asta "好——那——真是抱歉！" with diss
            asta "这是我唯一想得出对付他们的办法。"
            show c1p8s3 96
            mc "算了。" with diss
            mc "继续走。"
        "[choice2.get_display_text()]":
            $ choice2.apply_stats()
            show c1p8s3 97
            mc "那些混蛋死了活该！" with diss
            show c1p8s3 96
            mc "现在快走。" with diss
    show c1p8s3 98
    asta "等等！" with diss
    show c1p8s3 99
    asta "你不好奇这些东西为什么还完好无损吗？" with diss
    show c1p8s3 100
    mc "不太好奇。" with diss
    play sfx "sfx/Whoosh.ogg"
    show c1p8s3 101
    asta "你应该好奇！" with diss
    asta "它们在散发神力！"
    show c1p8s3 102
    asta "我猜他们把神力当成那身装甲的某种能源。" with diss
    show c1p8s3 103
    mc "这就解释了他们的装甲为何能抵抗我们的力量。" with diss
    mc "不过这是件好事。"
    show c1p8s3 104
    asta "怎么说？" with diss
    show c1p8s3 105
    mc "这意味着我们可以用气息视觉发现其他士兵，避免更多冲突。" with diss
    mc "至少在他们发现这摊烂摊子之前。"
    show c1p8s3 106
    asta "我都没想到这一点，但你说得对。" with diss
    show c1p8s3 107
    mc "试试吧。" with diss
    play sfx "sfx/Whoosh.ogg"
    show c1p8s3 108 with diss
    pause 1.0
    show c1p8s3 109
    mc "那边有两个……" with diss
    show c1p8s3 110
    mc "那边好像有四个。" with diss
    show c1p8s3 111
    mc "还有……" with diss
    show c1p8s3 112
    mc "{i}那他妈是什么？！{/i}" with diss
    show c1p8s3 113
    asta "我不能确定，但有几个猜测。" with diss
    show c1p8s3 114
    asta "先找到凯特，然后回头再深入调查。" with diss
    show c1p8s3 115
    mc "听起来不错。" with diss
    hide c1p8s3 with diss
    pause 1.0
    play bgm "bgm/Stealth Operation.ogg" fadein 1.0
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 116
    mc "呼！" with diss
    mc "能追踪那些人确实方便多了。" with diss
    show c1p8s3 117
    asta "是啊……" with diss
    show c1p8s3 118
    mc "你在想什么？" with diss
    show c1p8s3 119
    asta "没什么，我没事。" with diss
    show c1p8s3 120
    asta "继续走吧。" with diss
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 121 with diss
    pause 1.0
    show c1p8s3 122
    $ CharacterProfile.unlock_outfit([(chara["kate"], 1)])
    kate "[mc_name]？！" with diss
    kate "我就说那声音听着耳熟！"
    show c1p8s3 123
    mc "凯特！" with diss
    mc "我们到处都在找你！"
    mc "是维罗妮卡让我们来救你出去的。"
    show c1p8s3 124
    kate "好，但快点！" with diss
    kate "守卫每隔十五分钟左右就会经过这里。"
    show c1p8s3 125
    mc "知道了。" with diss
    play sfx "sfx/Metal - Creaking.ogg"
    show c1p8s3 126 with diss
    pause 1.0
    show c1p8s3 127
    mc "看来我没自己以为的那么强。" with diss
    show c1p8s3 128
    asta "这些栏杆注入了土系晶体。" with diss
    asta "那种魔力强化让它们成为这星球上最坚固的东西。"
    show c1p8s3 129
    asta "我有个更好的办法。" with diss
    play sfx "sfx/Astral - Portal.ogg"
    show c1p8s3 130 with diss
    pause 1.0
    show c1p8s3 131
    asta "那个传送门会把你送到维罗妮卡那边。" with diss
    show c1p8s3 132
    kate "真的假的？！" with diss
    show c1p8s3 133
    kate "在从管事的人那儿拿到答案之前，我哪儿也不去。" with diss
    show c1p8s3 134
    asta "那你可以回总部去问你的上级。" with diss
    show c1p8s3 135
    kate "什么？" with diss
    kate "我为什么要那么做？"
    show c1p8s3 134
    asta "因为{i}这个地方{/i}就是48区块。" with diss
    show c1p8s3 136
    kate "是守望者绑架了我？！" with diss
    kate "为什么？"
    show c1p8s3 134
    asta "不知道，但我们打算查清楚。" with diss
    show c1p8s3 135
    kate "放我出去我就帮你们！" with diss
    show c1p8s3 137
    asta "那才是你的出路。" with diss
    show c1p8s3 138
    asta "带着你只会拖慢我们。" with diss
    show c1p8s3 139
    mc "再说了，维罗妮卡在等你。" with diss
    mc "她担心得快疯了。"
    show c1p8s3 140
    kate "呃，好吧！" with diss
    kate "至少查到什么来告诉我一声！"
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 141
    asta "行行行，随便。" with diss
    asta "快走吧，求你了。"
    play sfx "sfx/Astral - Warp.ogg"
    show c1p8s3 142 with diss
    pause 1.0
    show c1p8s3 143
    asta "真是的，她真能抱怨。" with diss
    show c1p8s3 144
    mc "不过也能理解，你说呢？" with diss
    show c1p8s3 145
    asta "大概是吧。" with diss
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 146
    asta "去调查那股能量的来源吧。" with diss
    hide c1p8s3 with diss
    stop bgm fadeout 3.0
    play sfx "sfx/Door - Large - Auto.ogg"
    pause 1.0
    show c1p8s3 147 with diss
    pause 1.0
    show c1p8s3 148
    asta "我就知道！" with diss
    show c1p8s3 149
    mc "那就是最后的真神吗？" with diss
    show c1p8s3 150
    mc "那些管子是干什么的？" with diss
    show c1p8s3 151
    asta "是他，而且看起来他们正用那些管子抽取他的能量。" with diss
    show c1p8s3 152
    asta "这就解释了能量核心是怎么来的。" with diss
    show c1p8s3 153
    mc "我要把他救出来。" with diss
    show c1p8s3 154
    mc "他的生命体征看起来很平稳。" with diss
    mc "我要放他出来。"
    play sfx "sfx/Keyboard - Type.ogg"
    show c1p8s3 155 with diss
    pause 1.0
    play sfx "sfx/Pod - Open - Water.ogg"
    show c1p8s3 156 with diss
    pause 1.0
    show c1p8s3 157 with diss
    pause 1.0
    show c1p8s3 158 with diss
    pause 1.0
    show c1p8s3 159
    tlg "{i}*倒吸一口气*{/i}" with diss
    show c1p8s3 160
    tlg "我……我在哪儿？" with diss
    tlg "你、你们是谁？！"
    show c1p8s3 161
    mc "放松，是我们把你从那个舱里救出来的。" with diss
    show c1p8s3 162 with diss
    pause 1.0
    show c1p8s3 163
    tlg "那我还真是该谢谢你们。" with diss
    show c1p8s3 164
    resh "我是雷什蒙……" with diss
    play sfx "sfx/Spirit - Aura.ogg"
    show c1p8s3 165
    resh "……灵魂之神。" with diss
    show c1p8s3 166
    mc "[mc_name]，呃，创世之神裔……大概？" with diss
    show c1p8s3 167
    asta "阿斯塔拉。" with diss
    show c1p8s3 168
    resh "你们两个都是神裔？" with diss
    show c1p8s3 169
    resh "而且还有气息！" with diss
    show c1p8s3 170
    resh "这意味着预言要成真了……" with diss
    show c1p8s3 171
    mc "预言？" with diss
    show c1p8s3 172
    resh "那是一则远古预言，早在我说这个时代之前就被记载下来。" with diss
    resh "包括我在内，大多数神明有一段时间都把它当作虚妄之词。"
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 173
    resh "我以后再详细解释。" with diss
    resh "我已经准备好离开这牢笼了。"
    show c1p8s3 174 with diss
    pause 1.0
    play sfx "sfx/Door - Large - Auto.ogg"
    show c1p8s3 175 with diss
    pause 1.0
    play bgm "bgm/Threats Revealed.ogg" fadein 5.0
    show c1p8s3 176
    unkn "这么快就要走？" with diss
    show c1p8s3 177
    asta "是你！" with diss
    play sfx "sfx/Footsteps - Metal - Run.ogg"
    show c1p8s3 178 with diss
    pause 1.0
    show c1p8s3 179 with diss
    pause 1.0
    play sfx "sfx/Gun - Rifle - Sent - Handle.ogg"
    show c1p8s3 180 with diss
    pause 1.0
    play sfx "sfx/Gun - Rifle - Sent - Shoot.ogg"
    show c1p8s3 181 with hpunch
    pause 0.3
    play sfx "sfx/Bullet - Impact - Body.ogg"
    show c1p8s3 182 with hpunch
    pause 0.3
    play sfx "sfx/Body - Drop - Light.ogg"
    show c1p8s3 183 with hpunch
    pause 1.0
    show c1p8s3 184
    unkn "认清你的位置，街头老鼠。" with diss
    play sfx "sfx/Footsteps - Metal - Run.ogg"
    show c1p8s3 185
    mc "阿斯塔拉！" with diss
    play sfx "sfx/Cloth2.ogg"
    show c1p8s3 186 with diss
    pause 1.0
    show c1p8s3 187
    unkn "年轻人，你知道这是什么地方吗？" with diss
    show c1p8s3 188
    mc "我看起来像在乎吗？！" with diss
    show c1p8s3 189
    unkn "我们把人带到这里，让他们变成更高等的存在。" with diss
    show c1p8s3 190
    unkn "当然，我们采取的手段不太道德……" with diss
    show c1p8s3 191
    unkn "……但我向你保证，这是为了全人类的更大利益。" with diss
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 192
    resh "别听他的毒舌之词！" with diss
    show c1p8s3 193
    unkn "有毒？" with diss
    unkn "hardly 才怪。"
    unkn "至少我还在为人类做事。"
    show c1p8s3 194
    unkn "你最近到底为人类做了什么？" with diss
    show c1p8s3 195
    unkn "等等，算了。" with diss
    unkn "别回答。"
    show c1p8s3 196
    unkn "谁都知道你抛弃了我们。" with diss
    show c1p8s3 197
    resh "那是必须做的事。" with diss
    resh "你们太依赖我们的力量了。"
    show c1p8s3 198
    resh "既然我是我这一族仅存的一个，我根本没法满足这么多人的需求！" with diss
    show c1p8s3 199
    resh "所以我把自己封印起来，希望你们能学会自立……" with diss
    show c1p8s3 193
    unkn "而我们做到了。" with diss
    show c1p8s3 200
    mc "能说回正题吗？" with diss
    mc "这和{i}帮助人类{/i}有什么关系？"
    show c1p8s3 201
    unkn "这是我们的下一步。" with diss
    unkn "人类、机器与魔法，全部凝聚为一个存在。"
    unkn "人类的顶点。"
    show c1p8s3 197
    resh "你是说凝聚成了怪物！" with diss
    show c1p8s3 194
    unkn "比起你们这些所谓的神明，也算不上更怪物。" with diss
    show c1p8s3 200
    mc "好吧……但目的是什么？" with diss
    show c1p8s3 202
    unkn "我喜欢这个人。" with diss
    unkn "总是在问对的问题。"
    show c1p8s3 203
    unkn "我们所有守望者都宣过誓，誓言是保护人类及其在这个世界的未来。" with diss
    unkn "而这一切正是为了确保我们能履行那个誓言。"
    show c1p8s3 204
    unkn "我们对抗人类的恐怖分子尚且吃力，而在与精灵族的战争中我们付出的损失，用不着我提醒你吧。" with diss
    unkn "还有不死族这个日益增长的威胁。"
    unkn "我们怎么可能指望对抗神裔和真正的神明？"
    show c1p8s3 203
    unkn "这就是我们在这里进行的研究的意义。" with diss
    unkn "就算神裔正在崛起，我们也已有自保的手段。"
    show c1p8s3 205
    asta "你真的指望——" with diss
    show c1p8s3 206
    asta "——呃——" with diss
    show c1p8s3 205
    asta "——指望我们相信这套鬼话？" with diss
    show c1p8s3 207
    asta "你、你根本不在乎人类……" with diss
    show c1p8s3 208
    unkn "我们当然在乎。" with diss
    unkn "不然我们谁也不会来当守望者。"
    show c1p8s3 209
    asta "那我、我母亲呢？" with diss
    show c1p8s3 210
    asta "你们只是为了她的钱利用她……而当她倾尽所有去、去给予时，你们就把她丢在那儿等死！" with diss
    show c1p8s3 211
    asta "后来，我父亲想把你们绳之以法……" with diss
    show c1p8s3 210
    asta "……结果你们把他谋杀了！" with diss
    show c1p8s3 212
    asta "{i}*痛苦地皱起眉{/i}" with diss
    show c1p8s3 213
    asta "这对人类有什么好处？！" with diss
    show c1p8s3 214
    unkn "真可怜……" with diss
    show c1p8s3 215
    unkn "如果你天真到以为人人都该享有同等待遇，那你对这个世界如何运转真是一无所知。" with diss
    unkn "每个人都有自己该扮演的角色，而你父母把他们那份扮演得相当不错。"
    show c1p8s3 216
    unkn "我唯一后悔的，是当初没连亲爱的老爸一起做掉。" with diss
    show c1p8s3 213
    asta "去你的！" with diss
    show c1p8s3 217
    mc "我听够了。" with diss
    show c1p8s3 218
    unkn "好吧，迈克尔，我本来尽量想避免这个结果……" with diss
    show c1p8s3 219
    mc "迈克尔……" with diss
    show c1p8s3 220
    mc "爸爸？！" with diss
    show c1p8s3 221
    unkn "消灭神裔。" with diss
    unkn "我们不需要他们。"
    show c1p8s3 222
    unkn "再把那位「神」关回收容区。" with diss
    show c1p8s3 223
    ssent "长官！" with diss
    play sfx "sfx/Gun - Rifle - Sent - Handle.ogg"
    show c1p8s3 224 with diss
    pause 1.0
    show c1p8s3 225
    resh "你和那姑娘退后。" with diss
    show c1p8s3 226
    resh "我还没恢复全部力量，但对付这些家伙还是够的。" with diss
    show c1p8s3 227 with diss
    pause 1.0
    play sfx "sfx/Body - Drop - Light.ogg"
    show c1p8s3 228 with hpunch
    pause 1.0
    show c1p8s3 229
    mc "阿斯塔拉！" with diss
    mc "情况不妙。"
    show c1p8s3 230
    asta "阿、阿斯塔拉……这、这颗……子、子弹……" with diss
    show c1p8s3 231
    asta "不应该……对我们影、影响这么……" with diss
    show c1p8s3 232
    asta "……大……" with diss
    play sfx "sfx/Cloth2.ogg"
    show c1p8s3 233 with diss
    pause 1.0
    mc "阿斯塔拉。" with diss
    pause 0.5
    mc "阿斯塔拉！" with diss
    show c1p8s3 234
    mc "（还有脉搏，但很微弱。）" with diss
    show c1p8s3 235
    resh "看看你们在我不再留手之后能撑多久。" with diss
    play sfx "sfx/Spirit - Charge.ogg"
    show c1p8s3 236 with diss
    pause 1.0
    play sfx "sfx/Magic - Toss.ogg"
    show c1p8s3 237 with hpunch
    pause 0.5
    play sfx "sfx/Spirit - Impact.ogg"
    show c1p8s3 238 with hpunch
    pause 0.5
    show c1p8s3 239 with diss
    pause 0.5
    show c1p8s3 240 with diss
    pause 1.0
    play sfx "sfx/Spirit - Form.ogg"
    show c1p8s3 241 with diss
    pause 1.0
    show c1p8s3 242 with mhpunch
    play sfx "sfx/Gun - Rifle - Sent - Shoot.ogg"
    pause 0.2
    show c1p8s3 242 with mhpunch
    play sfx "sfx/Gun - Rifle - Sent - Shoot.ogg"
    pause 0.5
    show c1p8s3 242 with mhpunch
    play sfx "sfx/Gun - Rifle - Sent - Shoot.ogg"
    pause 0.2
    play sfx2 "sfx/Spirit - Phase.ogg"
    show c1p8s3 242a with diss
    pause 1.0
    show c1p8s3 243
    resh "尝试得不错。" with diss
    play sfx "sfx/Fight - Punch - Miss.ogg"
    show c1p8s3 244 with hpunch
    pause 0.3
    play sfx2 "sfx/Spirit - Phase.ogg"
    show c1p8s3 245 with diss
    pause 0.5
    play sfx3 "sfx/Spirit - Impact.ogg"
    show c1p8s3 246 with hpunch
    pause 1.0
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 247
    mc "我们必须把她带出去。" with diss
    show c1p8s3 248
    resh "那就去吧。" with diss
    show c1p8s3 249
    resh "我要把这个地方拆了。" with diss
    show c1p8s3 250
    mc "他们人太多了。" with diss
    mc "我们可不是为了救你才来的，然后把你丢在这儿等死。"
    mc "跟我们走。"
    show c1p8s3 251
    resh "{i}*叹气*{/i}" with diss
    show c1p8s3 252
    resh "你说得对。" with diss
    resh "走吧。"
    play sfx "sfx/Footsteps - Metal.ogg"
    show c1p8s3 253 with diss
    pause 1.0
    show c1p8s3 254 with diss
    pause 1.0
    show c1p8s3 255
    mc "不管用了！" with diss
    mc "我开不出传送门！"
    show c1p8s3 256
    resh "那还是打出去吧。" with diss
    show c1p8s3 257
    mc "我们没时间打架！" with diss
    mc "她快不行了！"
    show c1p8s3 258
    resh "不管我们做什么都改变不了这一点。" with diss
    resh "至少我们打出去，她还有一线机会。"
    show c1p8s3 259
    resh "就算在我虚弱的状态下，我也比你们强。" with diss
    resh "你背着她。"
    show c1p8s3 260
    resh "我负责战斗。" with diss
    show c1p8s3 261
    mc "好。" with diss
    play sfx "sfx/Cloth.ogg"
    show c1p8s3 262 with diss
    pause 1.0
    show c1p8s3 263
    resh "准备好了吗？" with diss
    hide c1p8s3 with diss
    pause 1.0
    play bgm "bgm/Get Out Alive.ogg"
    play sfx "sfx/Spirit - Punch.ogg"
    show c1p8s3 264 with hpunch
    pause 1.0
    play sfx "sfx/Spirit - Punch.ogg"
    show c1p8s3 265 with hpunch
    pause 1.0
    play sfx "sfx/Footsteps - Metal - Run.ogg"
    show c1p8s3 266
    resh "别掉队！" with diss
    show c1p8s3 267
    mc "我才没有！" with diss
    mc "上面往右拐！"
    play sfx "sfx/Gun - Rifle - Sent - Handle.ogg"
    show c1p8s3 268 with diss
    pause 1.0
    show c1p8s3 269
    resh "退后！" with diss
    resh "这个交给我！"
    show c1p8s3 270
    ssent "投降！" with diss
    ssent "立刻！"
    play sfx "sfx/Spirit - Charge.ogg"
    show c1p8s3 271 with diss
    pause 1.0
    show c1p8s3 272
    resh "想都别想！" with diss
    play sfx "sfx/Spirit - Aura.ogg"
    show c1p8s3 273 with diss
    pause 0.5
    play sfx "sfx/Spirit - Impact.ogg"
    show c1p8s3 274 with hpunch
    pause 0.5
    play sfx "sfx/Astral - Barrier - Push.ogg"
    show c1p8s3 275 with hpunch
    pause 0.5
    play sfx "sfx/Body - Drop.ogg"
    show c1p8s3 276
    mc "我的天！" with diss
    show c1p8s3 277
    mc "我们继续走。" with diss
    hide c1p8s3 with diss
    pause 1.0
    show c1p8s3 278
    mc "那里！" with diss
    mc "那应该就是正门！"
    play sfx "sfx/Mech - Drop.ogg"
    show c1p8s3 279 with hpunch
    pause 1.0
    play sfx2 "sfx/Mech - Move.ogg"
    show c1p8s3 280
    mc "该死！" with diss
    mc "怎么后面总还有一个！"
    show c1p8s3 281
    resh "别担心。" with diss
    play sfx "sfx/Footsteps - Metal - Run.ogg"
    show c1p8s3 282
    resh "它们越大……" with diss
    play sfx "sfx/Whoosh - Air.ogg"
    show c1p8s3 282a with hpunch
    pause 0.5
    play sfx "sfx/Spirit - Aura.ogg"
    show c1p8s3 283
    resh "……就倒得越——" with diss
    play sfx "sfx/Fight - Stab - Mech.ogg"
    show c1p8s3 284
    resh "——狠！" with hpunch
    play sfx "sfx/Mech - Drop.ogg"
    show c1p8s3 285 with diss
    pause 1.0
    play sfx "sfx/Mech - Spark.ogg"
    show c1p8s3 286
    resh "我们能……" with diss
    show c1p8s3 287
    resh "她没事吧？" with diss
    show c1p8s3 288
    mc "她……" with diss
    play sfx "sfx/Stinger - Serious.ogg"
    stop bgs fadeout 1.0
    hide c1p8s3
    mc "她已经没呼吸了……"
    hide c1p8s3 with diss
    pause 1.0
    jump c1toc2

label c1toc2:
    scene black
    show magic_effect at theme_ember
    with fadeb
    play sfx "sfx/Chapter - In.ogg"
    show eoc1 as eoc1_blur at text_glow
    show eoc1
    with staticflow
    $ save_name = "第一章 完"
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide eoc1
    hide eoc1_blur
    with grunge
    pause 1.0
    play sfx "sfx/Chapter - In.ogg"
    show supportscreen as supportscreen_blur at text_glow
    show supportscreen
    with staticflow
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide supportscreen
    hide supportscreen_blur
    with grunge
    pause 1.0
    play sfx "sfx/Chapter - In.ogg"
    show thanks as thanks_blur at text_glow
    show thanks
    with staticflow
    pause
    play sfx2 "sfx/Chapter - Out.ogg"
    hide thanks
    hide thanks_blur
    with grunge
    return
