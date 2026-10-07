label ch7_shelley_sex:
    $ persistent.ch7_shelley_sex = True
    if _in_replay:
        scene c007_s014_011 with Dissolve(0.5)
    j "我不会拒绝。"
    s "你是奶子派男人，对吧？还是屁股派？"
    stop music fadeout 2.0
    scene c007_s014_012 with Dissolve(0.25)
    j "我喜欢火辣的女人，不管尺寸是什么。"
    s "懂了。有些姑娘就是往某个方向有天赋。也许上帝对她们笑了一下，让她们两样都有。又或者她们懂得怎么甩、怎么用自己拥有的东西调情。"
    play sound zipper
    play music shelleytheme fadein 3.0
    scene c007_s014_013 with Dissolve(0.25)
    s "我是说，看看我拥有的。*咯咯笑*"
    scene c007_s014_014 with Dissolve(0.25)
    s "拜托，你今晚不想一个人睡吧？"
    j "我觉得这跟睡觉没关系，对吧？"
    scene c007_s014_015 with Dissolve(0.25)
    s "你说得对。春季学期一结束，我就又孤单又饥渴。值得睡的男生全都回家了。"
    j "而我是「值得睡的男生」？"
    scene c007_s014_016 with Dissolve(0.25)
    s "我在淋浴间看到你有什么了。我不介意试试看。而且你长得也不赖。怎么样？"
    j "我们脱光了看看会怎样。*轻笑*"
    scene c007_s014_017 with Dissolve(0.25)
    s "哦，那会弄出很大的动静。希望你别介意，因为这些宿舍床可不是为那种事设计的。两个人干起来的时候，它们叫得跟婊子似的。每次有女生带男人进来，我们都知道发生了什么。"
    j "听起来那会让她的邻居很尴尬。"
    scene c007_s014_018 with Dissolve(0.25)
    s "尴尬又饥渴。我承认，有不止几次，我都是一边听着别人被操，一边自己用手弄下面。我受够了这样。"
    j "你想当被操的那个，对吧？"
    play voice_loop shelley_slow
    scene c007_s014_019 with Dissolve(0.25)
    s "啊啊啊~~~ 对啊，你又不是不知道。你喜欢我的奶子吗？听起来挺喜欢的。"
    j "男人普遍都喜欢奶子，而你的特别漂亮。又圆又饱满。"
    s "很好。我还有别的地方可以让你摸。"
    scene c007_s014_020 with Dissolve(0.25)
    s "还有，也许你该别再去招惹那些生活里已经有别的内容的女孩，专挑那些自由单身的女人。也许你该别再把她们的事情搅得更乱，让她们更难回到自己的生活里。"
    j "所以，我该去招惹你？"
    s "我就是这个意思。"
    stop voice_loop
    play voice_loop kiss
    scene c007_s014_021 with flashpink
    s "啾噜噗~~~ 唔唔~~~"
    "知道刚才那些调情不是为了气我就好了。或者，也许就是为了气我，但既然这里就我一个带把的，她当然要好好利用。我他妈在乎吗？"
    scene c007_s014_022 with Dissolve(0.5)
    if k_sex >= 1 or l_sex >= 1:
        "我是说，她没说错，其他人确实都有生活要回去。雪莉在这儿，无牵无挂。"
    else:
        "如果我去招惹其他人，她说得对，他们确实都有生活要回去。雪莉在这儿，无牵无挂。"
    s "啾噜噗~~~ 唔唔~~~"
    stop voice_loop
    scene c007_s014_023 with vpunch
    j "哦？进展不够快？*轻笑* 我以为先亲热一下是应有之义。"
    s "是没错，但我真的很想把你的鸡巴掏出来。"
    scene c007_s014_024 with Dissolve(0.25)
    s "不瞒你说，我只是想近距离看看我要对付的是什么。好奇心这东西有时候很烦人。"
    j "怎么样？我够得上你的标准吗？"
    scene c007_s014_025 with Dissolve(0.25)
    s "*咯咯笑* 我打算在这根厚肉上好好放开手脚。所以，是的。"
    j "早知道。真该早点住宿舍，我上学那会儿肯定错过了不少东西。听你说话的架势，你们那时候是不是天天在做爱。"
    scene c007_s014_026 with Dissolve(0.5)
    s "没有父母干涉的青春期年轻人？你最好相信是的。"
    scene c007_s014_027 with Dissolve(0.25)
    s "虽然没电视和电影里演的那么疯那么野。并不是每天晚上都有喝醉的兄弟会派对变成群交，也不是有人光着身子在校园里狂奔。"
    j "真有那些事？我觉得我可能一直看错了片子。"
    scene c007_s014_028 with Dissolve(0.25)
    s "也许吧，但这真的重要吗？反正你来了之后已经搞到不少肉了。"
    if k_sex >= 1 or l_sex >= 1:
        j "我不是想弥补什么落下的时光。真的。"
    else:
        j "不算是，不过我也不打算争。"
    scene c007_s014_029 with Dissolve(0.5)
    s "反正也没差。来吧。我们挪到上铺去。如果你那根硬邦邦的东西在两腿之间晃荡着还爬得上去的话。"
    j "我又不是第一次硬着走三英尺路。"
    scene c007_s014_058 with Dissolve(0.25)
    s "跟着那个可爱的屁股就行。如果你跟得上。"
    j "对，我跟得上。"
    scene c007_s014_030 with Dissolve(0.25)
    s "哇，小心点。至少先让我上床再插进来。"
    j "*轻笑* 我看我就是被你这样吸引住了。"
    scene c007_s014_059 with Dissolve(0.25)
    s "很好。现在帮姑娘推一把，我们就能进行到那一步了。"
    j "唔唔唔~~~ 这里……"
    scene c007_s014_031 with Dissolve(0.25)
    s "谢谢 *咯咯笑*"
    j "这些床为什么他妈没有梯子？"
    s "每个人都问这个，然后等他们累够了——或者饥渴够了——自己就琢磨出怎么爬了。现在，他妈的上来。"
    scene c007_s014_032 with Dissolve(0.25)
    j "这不该费多大劲。大概是给更年轻的身体准备的。"
    s "你没那么老吧？"
    scene c007_s014_033 with Dissolve(0.5)
    j "老到身上有运动伤留下的酸痛，又年轻到还不在乎。"
    s "回答得好。"
    scene c007_s014_034 with Dissolve(0.25)
    s "既然有这种东西可以用，你真的一点都不在乎会不会弄疼自己，是吧？"
    j "你只要一直摆出那副很好操的样子，答案就永远是「是」。"
    s "我爱听这句。现在我要转过身撅起屁股。你就守着骚穴。不玩屁股。今晚。"
    j "今晚？"
    scene c007_s014_035 with Dissolve(0.25)
    s "你要是乖，也许哪天我让你走后门。"
    j "听起来值得努力争取。"
    scene c007_s014_036 with Dissolve(0.25)
    s "没错。我喜欢给人提供奖励。*咯咯笑*"
    j "你说这话好像你那性感的身体本身不是奖励似的。"
    scene c007_s014_037 with Dissolve(0.5)
    s "在我这儿，奉承是有用的。*咯咯笑*"
    j "我开始明白了。现在……"
    play voice_loop shelley_slow
    scene c007_s014_038 with hpunch
    s "唔唔~~~ 哦呜~~~ 操~~~"
    "才刚进前端，她就已经哼哼唧唧了。求你别叫。求你别叫。"
    scene c007_s014_039 with hpunch
    s "天哪操唔唔~~~ 好他妈满唔唔~~~"
    "开始动吧，但一开始慢一点。"
    scene c007_s014_040 with Dissolve(0.25)
    show shelley_ch7_sex with Dissolve(0.25)
    s "哦靠啊啊啊~~~ 天哪这感觉好爽唔唔~~~"
    s "太需要这个了啊啊啊~~~"
    j "我看出来了唔唔~~~"
    s "让那两个屁股瓣啪啪作响啊啊~~~"
    j "哦，我正努力让所有地方都晃起来。"
    s "感觉确实。"
    scene c007_s014_041 with Dissolve(0.5)
    hide shelley_ch7_sex
    "抽插了她几分钟之后，她开始挪动身子。我把这当成她想换姿势的信号。"
    stop voice_loop
    play voice_loop shelley_med
    scene c007_s014_042 with Dissolve(0.25)
    show shelley_ch7_sex2 with Dissolve(0.25)
    s "对，就这样啊啊啊~~~ 唔唔~~~"
    "我真不该惊讶雪莉在床上会那么吵。她看起来根本不可能不大叫。"
    s "操你，你真的啊啊啊~~~ 好用力"
    j "没我能使的劲大。"
    s "很好，因为我他妈需要你把我操烂唔唔~~~"
    j "想清楚你在要求什么。"
    stop voice_loop
    play voice_loop shelley_fast
    scene c007_s014_043 with Dissolve(0.5)
    show shelley_ch7_sex3 with Dissolve(0.25)
    hide shelley_ch7_sex2
    "大概是我自己被她激出来的。说实话，也许我本不该那么想听她大喊大叫，但我已经在她里面了，我只是想看那两个奶子晃动。"
    s "唔唔~~~ 唔唔~~~ 天哪要射了啊啊啊~~~~"
    s "靠好深啊啊啊~~~ 啊啊啊~~~"
    s "操，太他妈爽了啊啊~~~"
    j "很高兴能让你舒服。"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c007_s014_044 with Dissolve(0.5)
    show shelley_ch7_sex4 with Dissolve(0.25)
    hide shelley_ch7_sex3
    "最后一下。我说我累了的时候可不是开玩笑，但这个机会我无论如何都不会放过。雪莉那对奶子太棒了。"
    s "唔唔~~ 唔唔~~~ 哦啊啊啊~~~~"
    s "操我~~~ 快了快了啊啊啊~~~"
    "对，我看出来了。你的骚穴正紧紧地夹着我，一会儿像在挤奶，一会儿又像在把我推出去。你身体在传递矛盾的信息。真是个惊喜。"
    s "唔唔~~ 唔唔~~~ 哦啊啊啊天哪操啊啊啊！！" with hpunch
    s "唔嗯~~~ 靠咝咝~~"
    stop voice_loop
    play voice_loop shelley_cum
    scene c007_s014_045 with vpunch
    hide shelley_ch7_sex4
    pause 0.3
    scene c007_s014_047 with vpunch
    pause 0.3
    scene c007_s014_046 with vpunch
    pause 0.3
    scene c007_s014_047 with vpunch
    pause 0.3
    scene c007_s014_048 with vpunch
    pause 0.3
    scene c007_s014_049 with Dissolve(0.5)
    stop voice_loop
    j "啊啊啊~~~ 要射了啊啊啊~~~"
    s "啊啊啊~~~ 射吧。"
    scene c007_s014_050 with flash
    play sound male_cum
    pause 0.5
    scene c007_s014_050 with flash
    j "啊啊啊~~~ 操啊啊啊~~~ *喘气* 靠对"
    s "对 *喘气* 对 *喘气* 对。"
    scene c007_s014_051 with Dissolve(0.25)
    j "操，那感觉 *喘气* 真爽。*喘气* 不只是爽 *喘气*"
    s "是啊 *喘气*。这事儿我还能多来很多次。"
    $ renpy.end_replay()
    scene c007_s014_060 with Dissolve(0.5)
    j "今晚的话，可能 *喘气* 就到这儿了。我之前说自己累了不是开玩笑。"
    s "我挪一挪。给你腾个地方睡。"
    j "行，地方不大，但谢了。"
    scene c007_s014_061 with Dissolve(0.5)
    s "谢谢你的热牛肉注射，附带血清素、多巴胺和其他美妙脑内化学品。有时候姑娘得找个瓶子以外的东西。"
    j "很高兴能满足你。昨晚你想让我来你房间的时候，想的就是这个？"
    scene c007_s014_062 with Dissolve(0.25)
    s "算是吧。我想。我就是想找人待着。这里气氛太紧张了，我想做点不是焦虑的事。当然，被你这么干确实帮了我大忙。所以老实说，最后大概还是会变成做爱。"
    j "唉，我没去挺可惜的，但你理解的吧？"
    scene c007_s014_063 with Dissolve(0.25)
    s "对，昨天真是险。她现在没事了，对吧？"
    j "我想是。我想我跟她说了些道理。再加上一场差点死掉，总算让她知道厉害了。"
    scene c007_s014_064 with Dissolve(0.25)
    s "我懂。这样吧，我不会跟其他人提今天的事。以防你还想跟她们睡。"
    j "雪莉——"
    scene c007_s014_065 with Dissolve(0.25)
    s "不不不，事情已经够乱了。我不要任何类似于承诺的东西。你大概也不要。至少在这一切结束之前不要。不过，如果你还想再来一次，我可以考虑。"
    j "我会记住的。那么，你要留下来吗？"
    s "不了。我自己有床，而且我们不需要有人半夜来串门，推门就看见我在这儿一身汗、光着身子。"
    scene c007_s014_066 with Dissolve(0.25)
    s "事实上，趁余韵还没消我还是先走。"
    j "好吧。我……那个提议一直有效，如果——"
    scene c007_s014_067 with Dissolve(0.25)
    s "不了，我不是那么黏人的人。我也许疯，但我不爱抱抱。"
    scene c007_s014_068 with vpunch
    s "刚才挺开心的，不过炮友要知道什么时候该撤。*咯咯笑*"
    scene c007_s014_069 with Dissolve(0.25)
    s "晚安，[player_name]。回头见。"
    j "对，晚安，雪莉。"
    "真是善变。她做情人时也一样善变、难以预测。我猜我确实需要一个没有牵挂、只想做爱找点感觉的人。"
    scene c007_s014_070 with Dissolve(0.25)
    "不过，我本该问问她最后有没有决定跟我们一起来。不是说我会把她留下，但我希望雪莉能接受这件事。"
    "嘿，等一下。我记得她说过自己没有外套或大衣。那她他妈穿的是什么？"
    jump shelley_achievement_check
label ch8_shelley_sex:
    $ persistent.ch8_shelley_sex = True
    stop music fadeout 2.0
    scene c008_s005_026 with Dissolve(0.5)
    j "想找点乐子？"
    s "简直像读心术。啊啊啊~~~"
    play voice_loop kiss
    scene c008_s005_027 with flashpink
    play music shelleytheme fadein 2.0
    if ch7_shelley_sex == "no":
        "对。之前我拒绝过她一次，但不知为什么，现在感觉时机对了。也许只是因为我们身体上贴得太近，或者说这种高涨的、原始的情绪。"
    else:
        "我进来的时候{b}没{/b}想的是这个。我只是想确认她没事。也许只是因为我们身体上贴得太近，或者说这种高涨的、原始的情绪。"
    s "啾噜噗~~~~ 唔唔~~~"
    scene c008_s005_028 with Dissolve(0.5)
    if ch7_shelley_sex == "no":
        "我绝不会跟雪莉这种人扯上关系。太年轻、太飘忽，而且对我来说仍然是个谜。我们才刚认识。但看她说话和做事的方式，这感觉像是「无牵无挂」。"
    else:
        "可我们已经做过了。这是她为了让自己心情好一点而做的事吗？毕竟她已经停药一段时间了。我……我想我可以接受。"
    s "唔嗯~~~ 唔唔~~~"
    stop voice_loop
    scene c008_s005_029 with Dissolve(0.25)
    s "哈啊~~~ 好了，把奶子放出来，让你直接上手。*咯咯笑*"
    j "哼，总比隔着衣服找奶头强。"
    scene c008_s005_030 with Dissolve(0.25)
    s "哦，你刚才摸索得还行，但皮肤贴着皮肤总是更好。现在……"
    play sound kissfuck loop
    scene c008_s005_031 with flashpink
    if ch7_shelley_sex == "no":
        "她的奶子确实相当漂亮。那种让人想把玩着、吸吮好几小时的。"
    else:
        "雪莉肯定挺喜欢，因为她把舌头塞进我嘴里，像里面有东西吃似的。"
    s "唔嗯~~~ 啾噜噗~~~"
    scene c008_s005_032 with Dissolve(0.5)
    s "啾噜噗~~~ 唔唔~~~"
    "这是什么？在扯我短裤。某位姑娘可没什么耐心。"
    scene c008_s005_033 with hpunch
    "还有一只手伸到里面乱摸。真遗憾得告诉她，这可不是把我鸡巴掏出来的最佳姿势。"
    s "唔嗯~~~ 唔唔~~~"
    stop voice_loop
    scene c008_s005_034 with Dissolve(0.5)
    j "你想玩他的话，我们得先把我短裤脱了。只是提醒一下。"
    s "当然。我真不知道你是怎么把那条大蟒蛇塞进这么小的地方的。"
    scene c008_s005_035 with Dissolve(0.25)
    s "来，我来弄。"
    if ch7_shelley_sex == "no":
        j "后悔了？如果这事要往我以为的方向发展的话？"
    else:
        j "你刚才可没这个问题。*轻笑* 说到窄小的地方。"
    scene c008_s005_036 with Dissolve(0.5)
    if ch7_shelley_sex == "no":
        s "哦，去你的。我早就想把你拿出来试试深浅了。"
    else:
        s "也许这就是我为什么还想再来一次。你想过吗？*咯咯笑* 你真的能把一个姑娘塞得很满。"
    j "这个嘛，总能让人自我感觉良好。"
    scene c008_s005_037 with Dissolve(0.25)
    s "哦，得了吧。好像你还需要这种。你是那种长得帅、却不承认自己知道的男人。或者说没人足够常告诉你你很性感，好让你脑子里记住。"
    j "业余心理学家，是吗？"
    scene c008_s005_039 with Dissolve(0.5)
    s "这他妈真的重要吗？而且你刚才那个转移话题转移得很拙劣。"
    j "有可能。"
    scene c008_s005_040 with Dissolve(0.5)
    show shelley_ch8_hj with Dissolve(0.25)
    s "一个尺寸可观、却不像自以为了不起的男人？在正常世界里，你可能挺抢手的。"
    j "啊~~~ 这就是那个「抢手」的地方，对吧？"
    s "对，「正常」。不过现在这不重要。"
    j "只要你继续这样啊啊啊~~~ 我也许能暂时忘掉外面的世界。"
    s "今天早上我就是这种感觉。来点鸡巴和骚穴的互动，让我从那些疯狂的事上分点神，哪怕就一小时。"
    scene c008_s005_041 with Dissolve(0.5)
    hide shelley_ch8_hj
    s "也许如果我今晚表现得够好，我们能在我床上再来一场。让我带着笑入睡。*咯咯笑*"
    j "听起来挺美好，但你会厌倦我的。"
    scene c008_s005_042 with Dissolve(0.25)
    s "听着，老兄，我知道你离婚了，也知道那会给你带来痛苦和自尊上的打击，但我不是那种女孩。"
    scene c008_s005_043 with Dissolve(0.25)
    s "而且大多数女孩都不想被提醒你还没放下上一个，好吗？这是超级扫兴的事。"
    j "是吗？我这是往你头上泼冷水？"
    scene c008_s005_044 with Dissolve(0.25)
    s "我不是大多数女孩。而且我非常需要拥有你，好让我得到一次美妙的多巴胺冲击。*咯咯笑*"
    j "很高兴能派上点用场。那最好抓紧开始。"
    play voice_loop shelley_slow
    scene c008_s005_045 with Dissolve(0.5)
    s "啊啊啊~~~ 对就这样啊啊啊~~~ 操……好敏感……"
    "从她说话的方式看，这更多是为了获得那些让人愉悦的性爱脑内化学物质，而不是我们之间有什么浪漫的东西。我想我可以接受。没有情感依附的性爱。"
    stop voice_loop
    scene c008_s005_046 with Dissolve(0.25)
    j "这样对你来说有用吗？"
    s "再多也不够，不过我觉得我们最好快点到你插进来那一步，因为不知道我们能单独待多久。"
    scene c008_s005_047 with Dissolve(0.25)
    j "什么？你不想要观众？"
    s "我真不是个暴露狂，就算我说话做事像是在玩这套。"
    scene c008_s005_048 with Dissolve(0.25)
    s "但我觉得她们其中一个撞见我们，可能会闹出我不想待在那儿收拾的场面。"
    if k_sex >= 1 or l_sex >= 1:
        j "你说得可能没错。就算像你说的，她们都有旧生活要回去。"
    else:
        j "我向你保证，我们之间什么都没有。"
    scene c008_s005_049 with Dissolve(0.25)
    s "不管怎样，我不觉得一觉醒来去洗手间、撞见我们在做爱，不会变成几场尴尬的碰面和几次不客气的醒来。"
    j "而你不想那样？"
    scene c008_s005_050 with Dissolve(0.25)
    s "不，我不是那种会搅浑水的人。虽然我喜欢撩人，让他们有点不自在。"
    j "所以，你嘴上说得挺大？"
    scene c008_s005_051 with Dissolve(0.25)
    s "只是嘴上说说吗？*咯咯笑* 当然，我会跟一些我根本没打算发生点什么的人调情。但我也会撩那些我确实想操的人。"
    j "而对看不的人来说，这两样看起来是一样的，对吧？"
    #scene c008_s005_052
    scene c008_s005_053 with Dissolve(0.5)
    s "大概吧。但你能分辨，对吧？"
    j "当对象不是我的时？当然能。"
    scene c008_s005_054 with Dissolve(0.25)
    s "好吧，我把话说清楚。你是我想操的人之一。"
    j "*轻笑* 这一点我还是懂的。"
    scene c008_s005_055 with Dissolve(0.25)
    s "很好，因为我可不想让你待会儿自己打手枪，浪费掉这么棒的勃起的。"
    j "我这辈子不是第一次「蛋疼」。"
    scene c008_s005_056 with Dissolve(0.5)
    s "有我在你不会遇到那个问题。现在，让我……"
    play voice_loop shelley_slow
    scene c008_s005_057 with hpunch
    s "啊啊啊~~~ 靠你好粗啊啊啊~~~"
    "才进前端她就已经很吵了。而且回声在这屋里乱窜。我该开水龙头来盖住声音的。"
    scene c008_s005_058 with vpunch
    s "哦靠，啊啊啊~~~"
    j "唔唔唔~~~ 尽量让你里面塞进我越多越好。"
    scene c008_s005_059 with Dissolve(0.25)
    show shelley_ch8_sex with Dissolve(0.25)
    s "好他妈满唔唔~~~ 好他妈满"
    j "唔唔~~~ 操，好他妈紧"
    "这姿势对我屁股不太友好，但天哪，对做爱来说爽爆了。"
    s "哦呜~~~ 哦呜呜~ 哦天哪啊啊啊~~~"
    s "唔唔~~~ 唔唔~~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c008_s005_061 with Dissolve(0.5)
    show screen ch8_shelley_change with Dissolve(0.25)
    $ Show("ChangeCamera_s_ch8", transition=Dissolve(1.0))()
    s "哦操~~~ 操我~~~"
    j "对，就这样啊啊啊~~~"
    s "操，这正是我需要的啊啊啊~~~"
    "我敢肯定，她的身体正在分泌各种能抑制抑郁和悲伤的东西。这就解释了为什么那么多人会在葬礼之后做爱。"
    j "所以你手边正好有这东西，真是走运。"
    s "更走运的是，我们通常啊啊啊~~~ 没法让男人留宿在宿舍。"
    s "所以现在，我想要的时候，隔壁就有一台他妈的打桩机。"
    "接下来会有突然冒出来的人吗？"
    $ Hide("ChangeCamera_s_ch8", transition=Dissolve(1.0))()
    stop voice_loop
    hide screen ch8_shelley_change
    play voice_loop shelley_fast
    scene c008_s005_062 with Dissolve(0.5)
    hide shelley_ch8_sex2
    hide shelley_ch8_sex3
    s "啊啊啊~~~ 再用力点啊啊啊~~~"
    scene c008_s005_063 with Dissolve(0.5)
    show shelley_ch8_sex4 with Dissolve(0.25)
    s "哦天哪真的唔唔唔~~~"
    s "把我弄坏啊啊啊~~~ 我今天想走路姿势都怪"
    j "再这么骑下去，你可就啊啊啊~~~ 没得选了。"
    s "操我操到破皮啊啊~~~"
    "说起来……没用套套。但愿她没事。我本来想说「在吃避孕药」，不过她的用药问题让这不太可能。"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c008_s005_064 with Dissolve(0.5)
    show shelley_ch8_sex5 with Dissolve(0.25)
    hide shelley_ch8_sex4
    s "操，让我啊啊啊~~~ 啊啊啊~~~"
    "现在是她掌握主动权。这个坐姿没法大幅度挺腰。不过感觉她快要到了。"
    s "唔唔~~~ 唔唔~~~"
    s "靠，啊啊啊~~~ 靠，啊啊啊~~~"
    j "射吧，雪莉啊啊啊~~~"
    s "唔唔~~~ 操~~~！！" with hpunch
    s "唔唔~~~ 唔唔~~~"
    stop voice_loop
    play voice_loop shelley_cum
    scene c008_s005_065 with vpunch
    hide shelley_ch8_sex5
    pause 0.3
    scene c008_s005_066 with vpunch
    pause 0.3
    scene c008_s005_067 with vpunch
    pause 0.3
    scene c008_s005_066 with vpunch
    pause 0.3
    scene c008_s005_068 with Dissolve(0.5)
    stop voice_loop
    j "啊啊啊~~~ 哈啊啊~~~ 啊啊啊~~~"
    scene c008_s005_069 with flash
    play sound male_cum
    pause 0.5
    scene c008_s005_069 with flash
    scene c008_s005_070 with Dissolve(0.5)
    j "哈啊啊啊~~~ *喘气* 真爽 *喘气*"
    scene c008_s005_071 with Dissolve(0.25)
    s "对。我也是 *喘气*。你和我做爱挺搭的。"
    j "很高兴听你这么说。"
    $ renpy.end_replay()
    scene c008_s005_093 with Dissolve(1)
    "不想骗你。享受这波多巴胺冲击的可不只是雪莉。要不是我还留着点理智，我会说我开始喜欢她了——喜欢她的那一面。但等这阵劲过去，我就会明白，我们之间并不是那种关系。"
    s "这样我可以坐一会儿。只要你不介意。"
    scene c008_s005_094 with Dissolve(0.25)
    j "迟早我这些东西会从你体内流出来，然后你会想去洗一洗。"
    s "大概吧。答应我，等我们出去以后，找个周末好好做一场。庆祝一下。"
    scene c008_s005_080 with Dissolve(0.25)
    j "这听起来像是你开始喜欢我了。要是被救了之后你还想见我。"
    s "我说过了：庆祝。*咯咯笑*"
    scene c008_s005_081 with Dissolve(0.25)
    j "好吧，不想毁掉这一刻，不过我们该起来了。或者至少我该起来。我还有一堆事要办。"
    s "对，大人的破事。我想我该洗个澡。洗完也许会感觉好些。你要一起来吗？"
    scene c008_s005_082 with Dissolve(0.25)
    j "*轻笑* 谢谢你的好意，但我觉得那只会变成更多的做爱。而且我要出去，回来的时候肯定想把自己冲干净。"
    scene c008_s005_083 with Dissolve(0.25)
    s "哦，好吧，姑娘总得问一句。谢谢你……为我做了这些。"
    scene c008_s005_084 with Dissolve(0.5)
    j "当然。你要知道，需要的时候我们所有人都会帮你。所以别一个人扛。"
    s "我、我不会的。我不觉得现在独自行动是个好主意。"
    scene c008_s005_085 with Dissolve(0.25)
    j "好。我想卡莉今天想找你，等她起来了你去跟她打个招呼。"
    s "好。"
    scene c008_s005_086 with Dissolve(0.25)
    j "好吧，那我先走了。"
    "趁我还忍不住留下来跟她再来一轮的时候。"
    jump shelley_achievement_check
label ch9_shelley_sex:
    $ persistent.ch9_shelley_sex = True
    stop music fadeout 2.0
    scene c009_s009_019 with Dissolve(0.25)
    j "就算时机不对，我也可以。"
    s "这才是我爱听的话。*咯咯笑* 不合时宜可是我最喜欢的惊喜性爱类型。就是那种当场的刺激感让它这么好玩。"
    scene c009_s009_020 with Dissolve(0.5)
    j "我确实得问一句：你还好吗？我知道你压力很大，这个可以理解。但是……"
    s "不……不是那个原因。我就是普普通通地、正常地被吓到了。因为那些怪物，还有那层杀人雾。你在这儿会让我好受很多。"
    scene c009_s009_021 with Dissolve(0.5)
    s "但也许我只是想瞎搞，因为我们可以。而且我想做。就这么简单。你有鸡巴我有骚穴，我想把两者凑一起，好让我分点心。"
    j "我很高兴对你来说这么简单。"
    s "是啊。"
    play voice_loop kiss
    scene c009_s009_022 with flashpink
    play music shelleytheme fadein 2.0
    s "啾噜噗噗噗~~~ 唔唔~~~"
    "雪莉真是他妈太难捉摸了。我明白停药对她没帮助——这种处境给所有人施加的压力也没有——但我总觉得，就算一切都很顺利，她也会以每秒为单位地变来变去。不过我们还是在这儿。先把这两个奶子掏出来，好好享受吧。"
    stop voice_loop
    scene c009_s009_023 with Dissolve(0.25)
    s "哈啊~~~ 等不及想看了吧？"
    j "你都那么急着摆出来，我为什么不想看？*轻笑*"
    scene c009_s009_061 with Dissolve(0.25)
    s "我知道怎么能让男人有兴致。而你也不例外。"
    j "靠。我还以为自己比一个饥渴的大学生强。"
    s "饥渴的成年男人才对。"
    play voice_loop shelley_slow
    scene c009_s009_024 with Dissolve(0.5)
    j "别说得好像你没湿透一样。你刚才在里面是不是自己弄了？"
    s "也许啊啊啊~~~ 有一点。"
    scene c009_s009_025 with Dissolve(0.25)
    j "那要是我没决定留下来呢？"
    s "我就啊啊啊~~~ 得自己解决掉。我本来会很失落，但是啊啊啊~~~"
    scene c009_s009_026 with Dissolve(0.5)
    show shelley_ch9_finger with Dissolve(0.25)
    s "姑娘想要什么就做什么啊啊啊~~~"
    j "所以，我在这儿还真是好事，对吧？"
    s "啊啊啊~~~ 哦啊啊啊~~~ 唔唔~~~"
    s "唔唔~~~ 靠啊啊啊~~~"
    s "就这样啊啊啊~~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c009_s009_027 with Dissolve(0.5)
    show shelley_ch9_finger2 with Dissolve(0.25)
    hide shelley_ch9_finger
    "靠，她在这儿有点太吵了。"
    j "也许小声一点。"
    s "哈啊~~~ 你手指在我里面，很难做到。"
    j "我可以停——"
    s "不不不，别停。我只是啊啊啊~~~ 很难啊啊啊~~~"
    s "控制住自己啊啊啊~~~"
    stop voice_loop fadeout 2.0
    scene c009_s009_028 with Dissolve(0.25)
    hide shelley_ch9_finger2
    s "哈啊~~~ 我们停一下好吗？"
    j "我不是说要停，只是你一上头就会很吵。"
    scene c009_s009_029 with Dissolve(0.5)
    s "哦，我知道我啊啊啊~~~ 是个嚎叫型的。但我想做点能让我闭嘴的事，如果你懂我意思。*咯咯笑*"
    j "我懂。我也许是个迟钝的混蛋，但基本的性感姿势我还是会的。"
    scene c009_s009_030 with Dissolve(0.5)
    s "也许等我们出去以后，可以发明几个新的。"
    j "当然。我们整个周末都拿来搞这个。"
    scene c009_s009_031 with Dissolve(1)
    s "你觉得只有一个周末吗？*咯咯笑*"
    j "我可不想待得太久，让人赶。"
    s "听起来像个觉得女人不会想了解他的男人。你该对自己评价高点。"
    scene c009_s009_032 with Dissolve(0.25)
    j "现在是讨论自我价值之类问题的时候吗？"
    s "不，只要这根大肉棒还没登场就不是。"
    "在某种程度上，我很感激雪莉一到做爱环节就不分心去聊天。"
    play voice_loop blowjob1
    scene c009_s009_033 with Dissolve(0.25)
    s "唔~~~ 啾噜噗~~~"
    j "哦呜~~~ 哦靠，那啊啊啊~~~"
    scene c009_s009_034 with Dissolve(0.5)
    j "不错。啊啊啊~~~"
    "我大概该先把自己那玩意儿冲干净，但没想到这一趟会变成这种事。我大概该开始习惯：每次跟她单独待着，我们都可能会做爱。"
    scene c009_s009_035 with Dissolve(0.25)
    s "唔嗯~~~~ 啾噜噗噗~~~~"
    j "哦哦~~~ 哦呜~~~"
    scene c009_s009_036 with Dissolve(0.25)
    s "唔嗯~~~"
    scene c009_s009_037 with Dissolve(0.25)
    s "啾噜噗~~~ 唔唔~~~"
    j "哦，雪莉，啊~~~"
    scene c009_s009_038 with Dissolve(0.5)
    show shelley_ch9_bj with Dissolve(0.25)
    j "啊啊啊~~~ 哈啊~~~ 哦对"
    s "啾噜噗噗噗~~~ 唔唔~~~"
    "好吧，这至少让她安静下来了。这屋里唯一的声音就是她给我口交的声音。"
    s "啾噜噗噗噗~~~ 啾噜噗噗噗~~~"
    "而且她没在偷懒。雪莉要是想的话，我敢肯定她能让我射进她喉咙里。"
    j "哦，姑娘，这真舒服啊啊啊~~~"
    stop voice_loop
    scene c009_s009_039 with Dissolve(0.25)
    hide shelley_ch9_bj
    s "唔唔~~ 啾噜噗~~~"
    scene c009_s009_040 with Dissolve(0.25)
    s "好了，你又湿又硬。要不我们挪进隔间，我弯腰摆出要吐的姿势，你给我来一场世界级狠操？"
    j "你能保证小声点吗？"
    s "不做保证。*咯咯笑*"
    scene c009_s009_041 with Dissolve(1)
    s "来。我保证不乱扭屁股，好让你一次就命中。*咯咯笑*"
    j "是啊，虽然我很想看你摇你的摇钱树，不过我们还是快点开始吧。"
    scene c009_s009_042 with Dissolve(0.25)
    s "就跟男人一样。甜甜蜜蜜的性爱没时间了。"
    j "明明是你想在洗手间里来点野的。"
    play voice_loop shelley_slow
    scene c009_s009_043 with hpunch
    s "啊啊啊~~~ 我可没看见这附近有床啊啊啊~~~"
    j "说得好像那能拦住你似的。"
    scene c009_s009_044 with Dissolve(0.5)
    show shelley_ch9_fuck with Dissolve(0.25)
    if ch8_shelley_sex == "yes":
        s "啊啊啊~~~ 在淋浴隔间里做爱，不代表我在哪儿都愿意做。"
        j "这可帮不了你唔唔~~~说话。"
    else:
        s "啊啊啊~~~ 我承认这不是我第一次在能找到的地方就做啊啊啊~~"
        j "我没那么唔唔~~~震惊。"
    s "哦哦哦~~~ 哦呜呜~~~"
    j "话说公道，你也不是第一个把精液弄得到处都是的人了。"
    s "听这话就像你啊啊啊~~~ 是那种没计划地做过很多次的人嗯嗯~~~"
    s "唔唔唔~~~ 哈啊啊啊~~~ 啊啊啊~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c009_s009_045 with Dissolve(0.5)
    hide shelley_ch9_fuck
    show screen ch9_shelley_change with Dissolve(0.25)
    $ Show("ChangeCamera_s_ch9", transition=Dissolve(1.0))()
    s "对你来说啊啊啊~~~ 是在哪里啊啊啊~~~？"
    j "我干过的最狂野的地方是哪儿？"
    s "是啊啊啊啊~~~~ 除非现在改成公共厕所了啊啊啊~~~"
    menu:
        "办公室的隔间。" if ch3_laura_sex == "yes":
            j "办公室的隔间。"
            s "在上班的时候？啊啊啊~~~ 那肯定是下班以后啊啊啊~~~"
            "对，就这么说吧。"
        "会议桌。" if ch4_laura_sex == "yes":
            j "会议桌。唔唔~~~ 会议室。"
            s "哦哦~~~ 在老板的桌子上操？大会议之前还是之后？"
            j "当然是之后啊啊啊~~~"
        "学校课桌。" if ch7_kallie_sex == "yes":
            j "学校课桌。"
            s "啊啊啊~~~ 那个我也干过啊啊啊~~~ 得看是什么课桌，安全性不一样"
            j "讲台。"
        "汽车后座。":
            j "汽车后座。电影院的停车场。"
            s "有点啊啊啊~~~ 老套了。"
            "这跟我和南希的关系基本属于标准配置。"
    s "啊唔唔唔~~~ 哦啊啊啊~~~ 啊啊啊~~~"
    s "就啊啊啊~~ 干在那个上面"
    $ Hide("ChangeCamera_s_ch9", transition=Dissolve(1.0))()
    stop voice_loop
    play voice_loop shelley_fast
    scene c009_s009_047 with Dissolve(0.5)
    hide screen ch9_shelley_change
    show shelley_ch9_fuck4 with Dissolve(0.25)
    hide shelley_ch9_fuck2
    hide shelley_ch9_fuck3
    s "啊啊啊~~~ 哦啊啊啊~~~ 啊啊啊~~~"
    j "本来想问问你的，但我怕知道答案*轻笑*"
    s "没你想的那么大胆啊啊啊~~~"
    s "我曾经在啊啊啊~~~ 一个男生父母的床上干过啊啊啊~~~"
    s "他们去度假了，我们把那儿弄得一塌糊涂唔唔~~~"
    j "我连「弄得一塌糊涂」具体指什么都不想知道。"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c009_s009_048 with Dissolve(0.5)
    show shelley_ch9_fuck5 with Dissolve(0.25)
    hide shelley_ch9_fuck4
    s "啊啊啊~~~ 啊啊啊~~~ 靠靠靠"
    "听起来她快到了。很好，因为我不知道已经过了多久，再待下去别人会奇怪我们为什么在这儿待了二十多分钟了。"
    s "啊啊啊~~~ 哈啊啊啊~~~~ 操好深啊~~~"
    s "射吧，哦呜哦呜~~~ 哦靠老兄~~~"
    j "射在我鸡巴上，雪莉。"
    s "啊啊啊~~~！！" with hpunch
    s "啊啊啊~~~~"
    stop voice_loop
    play voice_loop shelley_cum
    scene c009_s009_049 with hpunch
    hide shelley_ch9_fuck5
    pause 0.3
    scene c009_s009_050 with hpunch
    pause 0.3
    scene c009_s009_049 with hpunch
    pause 0.3
    scene c009_s009_051 with hpunch
    pause 0.3
    scene c009_s009_051 with hpunch
    pause 0.3
    scene c009_s009_052 with Dissolve(0.5)
    stop voice_loop
    s "哦操我啊，老兄。你——"
    scene c009_s009_053 with Dissolve(0.25)
    j "快了。射哪儿？"
    s "射进我里面。现在"
    scene c009_s009_054 with flash
    play sound male_cum
    pause 0.5
    scene c009_s009_054 with flash
    j "啊啊啊~~~ 哦啊啊啊~~~"
    scene c009_s009_055 with Dissolve(0.25)
    j "希望刚才不是一时冲动。*喘气*"
    s "很快就会知道了。"
    j "别拿这个开玩笑。"
    $ renpy.end_replay()
    scene c009_s009_056 with Dissolve(1)
    j "好吧，既然我都出汗了，我该回外面去了。"
    s "没有做爱后的抱抱？真扫兴。"
    scene c009_s009_057 with Dissolve(0.5)
    j "你知道为什么，对吧？"
    s "我只是开玩笑。这里不合适，也不是时候。不过我挺享受刚才的。谢谢。"
    scene c009_s009_058 with Dissolve(0.5)
    j "我也是。你该去洗洗了。"
    s "对啊，你把身上不少东西都留在下面了……"
    scene c009_s009_059 with Dissolve(0.5)
    j "手、脸、脖子，雪莉。我不是要扫兴。凡是你可能露出皮肤的地方都洗一下。只是尽量减少长期损害。我认真的。"
    s "好吧。我会的。我……我知道你说得对。"
    scene c009_s009_060 with Dissolve(0.5)
    j "很好。我去看看我们的处境怎么样了。"
    s "好。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c009_s009_015 with Dissolve(2)
    play music school fadein 2.0
    "{color=#8bc7ff}靠，雪莉。你就是忍不住，对不对？你一进来就开始想「姑娘，要不我们干脆做爱」，好像你完全没有自控力似的。{/color}"
    "{color=#8bc7ff}我该在他走后就自己弄一下的。{/color}"
    scene c009_s009_016 with Dissolve(0.25)
    "{color=#8bc7ff}又不是说他很痛快地拒绝了。也许我就喜欢这一点。不，不是也许。我确实喜欢，因为这有点太像我自己了。{/color}"
    if s_sex >= 2:
        "{color=#8bc7ff}我是说，我们在很短的时间内做了不少。也就几天吧。如果我们俩不是都清楚这只是一场被凑到一起的疯狂时刻，我也许会以为我们之间有什么化学反应。{/color}"
    else:
        "{color=#8bc7ff}这也不是什么坏事。我可以习惯这样被他「顺路捎上」。但我得把时机挑得更好。{/color}"
    scene c009_s009_017 with Dissolve(0.25)
    "{color=#8bc7ff}我……我本可能落到更差的地方。和[player_name]、卡莉、劳拉一起困在这种烂处境里。不过，主要还是因为[player_name]。{/color}"
    if k_sex >= 1 or l_sex >=1:
        "{color=#8bc7ff}但如果他也在操她们中的一个，那这可不太能说明他有多想跟谁安定下来。我不怪他。感觉死亡就在每个转角。能爽的时候就爽一场，似乎是唯一能让自己不被这一切逼疯的办法。{/color}"
    else:
        "{color=#8bc7ff}我们之间有点年龄差，但我不在乎。他好像也不在乎。而且这也许只是当下热度罢了。感觉死亡就在每个转角。能爽的时候就爽一场，似乎是唯一能让自己不被这一切逼疯的办法。{/color}"
    scene c009_s009_018 with Dissolve(0.25)
    s "*叹气* 撑住。"
    "{color=#8bc7ff}我能感觉到那些让人愉悦的脑内汁液正在失效。现在别去糟糕的地方，雪莉。求你了。{/color}"
    jump shelley_achievement_check
label ch11_shelley_sex:
    $ persistent.ch11_shelley_sex = True
    scene c011_s008_026 with Dissolve(1)
    play music shelleytheme fadein 2.0
    s "嘿。你能……你愿不愿意……"
    j "愿意什么？"
    scene c011_s008_027 with Dissolve(0.25)
    s "你愿不愿意和我做爱？"
    if s_sex >= 2:
        j "你确定吗？我知道你之前是用它来获取血清素和内啡肽的提升，但我没想到你会有心情做任何事。"
    else:
        j "你确定吗？我知道你也许会用性爱来获取血清素和内啡肽的提升，但我没想到你会有心情做任何事。"
    scene c011_s008_028 with Dissolve(0.25)
    s "我不需要那个来获取。嗯，也许那样也不错。但是……"
    s "我从来没有真正……对我来说，性爱一直都是浅层的。我在派对上，想操人。或者我很无聊，跟一个我觉得性感的人在一起。它从来不会导向什么，也从来没有任何情感重量。我不会跟那些人产生联结。"
    scene c011_s008_029 with Dissolve(0.25)
    s "跟梅茜在一起时，做完之后我们还是原来那样。只是关系还算像朋友的人，哪怕我们一起做过一些事。"
    j "而你提起这个……为什么？"
    scene c011_s008_030 with Dissolve(0.25)
    s "我需要跟某个人感到亲近、有联结。如果感觉不到，我怕自己会飘走。在情感上，在精神上。我……你能就今晚一晚，像爱一个人那样爱我吗？好好疼我？"
    j "我确实在乎你。而且你到现在应该也知道了。但对你来说，如果你需要，我今晚可以温柔体贴。"
    scene c011_s008_031 with Dissolve(0.25)
    s "就是需要。我们之前做的那些事很开心，但我需要你今晚是想要我的。"
    j "嗯，有你压在这张床上，这当然就容易多了。而且你是个非常有魅力的女人。"
    scene c011_s008_032 with Dissolve(0.25)
    s "就只是「有魅力」？只有「有魅力」？"
    j "刚才那十分钟我一直在努力不去注意你的奶子几乎要从上衣里蹦出来。"
    scene c011_s008_033 with Dissolve(0.5)
    s "我就知道那个凸起是有原因的。不过，对你来说大概不需要太多就够了吧？"
    j "对你来说，确实不需要。"
    scene c011_s008_034 with Dissolve(0.5)
    s "你说话的方式像是你想要我。*咯咯笑* 好像我不用求你做这件事。"
    j "求你？不。而且，是的，我就是喜欢你那一面，雪莉。年轻，性感，还有……"
    "当你没被抑郁症折磨的时候，你相处起来还挺有意思的。"
    scene c011_s008_035 with Dissolve(0.25)
    s "你喜欢我的奶子？"
    j "你身上很多东西我都喜欢。这可能是今晚之前我们没聊过的。我们以前有个习惯，就是直接奔着做爱去。"
    scene c011_s008_036 with Dissolve(0.25)
    s "我也喜欢你身上很多东西。"
    j "很好。这让接下来要发生的事容易多了。"
    s "我也是这么想的。"
    play voice_loop kiss
    scene c011_s008_037 with flashpink
    s "啾噜噗~~~ 唔唔~~~ 唔唔~~~"
    if s_sex >= 2:
        "今晚之前，雪莉一直在跟我调情，我也不介意。我把这当成她的本性，而且也认为也就到此为止了。很简单，也挺愉快。我跟雪莉之间的任何问题，都跟身体上的亲近或感情无关。"
        scene c011_s008_038 with Dissolve(1)
        "比之前更多一些，雪莉和我啃咬了起来。我没数时间，她爬到我身上，舌头跟我的缠在一起，同时把乳房压进我的胸口。我一把抓住她两瓣屁股，惹出一声呻吟。"
    else:
        "今晚之前，雪莉和我基本是「好吧，我想做爱所以做吧」，我也不介意。很简单，也挺愉快。我跟雪莉之间的任何问题，都跟性爱或感情无关。"
        scene c011_s008_038 with Dissolve(1)
        "雪莉和我继续啃咬。我没数时间，她爬到我身上，舌头跟我的缠在一起，同时把乳房压进我的胸口。我一把抓住她两瓣屁股，惹出一声呻吟。"
    s "唔唔~~~ 啾噜噗噗~~~"
    stop voice_loop
    scene c011_s008_039 with Dissolve(0.25)
    s "我……哈啊~~~ 我……"
    j "雪莉？"
    "她脸上有种奇怪的表情，像是在考虑什么。"
    scene c011_s008_040 with Dissolve(0.25)
    s "对，是时候了。脱衣服。"
    j "通常这样会容易一点。而且能把你那两个展示出来。"
    scene c011_s008_041 with Dissolve(0.25)
    s "对，你喜欢它们。大多数人都喜欢。"
    j "它们确实讨人喜欢。而且……"
    play voice_loop shelley_slow
    scene c011_s008_042 with Dissolve(0.5)
    s "唔唔~~~ 操啊啊啊~~~ 好敏感。你怎么知道那个唔唔~~~"
    s "那对我就是个开关啊啊啊~~~ 老兄。我懂了。你啊~~~ 喜欢吸奶子。"
    stop voice_loop
    scene c011_s008_043 with Dissolve(0.25)
    j "你要是把别的东西塞到我嘴边，我也会去舔、去吸。*轻笑*"
    scene c011_s008_044 with Dissolve(0.25)
    s "那我可得让你兑现这句话了。"
    j "这张床上没多少空间，不过我很想看看你怎么试。"
    scene c011_s008_045 with Dissolve(0.5)
    s "你知道，我完全可以先下床再上去。你说得好像{a=https://en.wikipedia.org/wiki/The_floor_is_lava}地板是岩浆{/a}似的。"
    j "是啊，也许花了太多时间操心安全区域，养成了一些习惯。"
    scene c011_s008_046 with Dissolve(0.25)
    s "不过我{i}觉得{/i}我们在这儿至少是安全的。*咯咯笑* 或者，最好真是。因为我有期待。要是没能满足，我可会失望。"
    j "听起来我得像表演一样。"
    scene c011_s008_047 with Dissolve(0.25)
    s "那……那不是我想说的。我不是想给你压力。我……我知道……"
    j "你让我「好好疼你」，那里面有情感的成分。在把性感的身体部位互相挤压之外，还有满足和联结。"
    scene c011_s008_048 with Dissolve(0.25)
    s "我真的很喜欢那个互相挤压的部分。"
    j "好吧，今晚是你要的全套。"
    scene c011_s008_049 with Dissolve(0.25)
    s "你说话好像我点了单，还决定要上白金套餐似的。"
    j "我可以免费给你升个级。因为我在乎，也希望这对你来说够好。非常好。给你最好的。"
    scene c011_s008_050 with Dissolve(0.5)
    s "呃……[player_name]？你在想什么？你那个表情。"
    j "我确实说过，你要是把别的东西塞到我嘴边，我就会去舔、去吸。"
    s "哦？唔~~~"
    play voice_loop shelley_slow
    scene c011_s008_051 with Dissolve(0.25)
    s "哦靠老兄啊啊啊~~~ 哦呜~~~"
    show shelley_ch11_oral with Dissolve(0.25)
    s "啊啊啊~~~ 靠你居然没有啊啊啊~~~ 但现在别停啊啊啊~~~"
    "我猜你不会介意我帮你弄一阵子阴蒂和肉缝。你已经湿了。只要几分钟就能把你弄到湿透。"
    s "啊啊啊~~~ 哈啊~~~ 哦老兄"
    s "哦哦哦~~~ 哦呜~~~ 哦靠啊啊啊~~~"
    s "操~~ 哦好啊啊啊啊~~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c011_s008_052 with Dissolve(0.5)
    show shelley_ch11_oral2 with Dissolve(0.25)
    hide shelley_ch11_oral
    s "哦天哪~~~ 哦操老兄啊~~~"
    "你是习惯那些在你口交时不太会照顾女人感受的大学生了吧？"
    s "就是那里啊~~~ 哦操我啊啊啊~~~"
    s "你要是不小心唔唔~~~ 我可能啊啊啊~~~"
    "如果你想这样射出来，我没问题。让你高兴就好，姑娘。"
    stop voice_loop
    scene c011_s008_053 with Dissolve(0.25)
    hide shelley_ch11_oral2
    s "其实啊啊啊~~~ [player_name]，等一下。别啊啊啊~~~ 还不行啊啊啊~~~"
    "看来我被叫停了。"
    scene c011_s008_054 with Dissolve(0.25)
    j "我的表演还合你的胃口吗？*轻笑*"
    s "别犯蠢了。你知道你刚才干得不错。不过现在，过来。我要你用鸡巴好好表现。"
    scene c011_s008_055 with Dissolve(0.25)
    j "啊，对，我们俩都会享受的那部分。虽然刚才那边我也有点乐趣，但是——"
    s "吃骚穴跟操骚穴不一样。"
    j "对，大致是这么个意思。"
    scene c011_s008_073 with Dissolve(1)
    s "嘿，呃……"
    j "雪莉？"
    scene c011_s008_074 with Dissolve(0.25)
    s "我知道我以前说过这话，但我需要你知道我是认真的。谢谢你。谢谢你没有放弃我。换个人早就把我丢下了。但你没有。而我……"
    scene c011_s008_075 with Dissolve(0.25)
    s "我保证我会做得更好。会变得更好。"
    j "你不需要成为别的任何东西，只要做你自己就好。"
    scene c011_s008_056 with Dissolve(0.25)
    s "{b}我自己{/b}是个飘忽、情绪化、傻乎乎的家伙。但那是个会为你努力撑住自己的家伙。也会为其他人。不过今晚？再吻我一次。求你了。"
    play voice_loop kiss
    scene c011_s008_057 with flashpink
    s "啾噜噗噗~~~~ 唔唔~~~"
    "有意思。这就是她说的「好好疼爱」吗？更多的接吻。更慢一点。少一点直奔主题？我喜欢这个版本的雪莉，不过这可能只是一晚的事。"
    stop voice_loop
    scene c011_s008_058 with Dissolve(0.25)
    s "我哈啊~~~ 我们应该啊啊啊~~~"
    j "看来你准备好了。*轻笑*"
    scene c011_s008_059 with Dissolve(0.5)
    s "对。你感觉出来了。"
    j "也许可以放开他，让我滑进去。"
    scene c011_s008_060 with Dissolve(0.25)
    s "我现在啊啊啊~~~ 已经湿得够可以了。*咯咯笑*"
    j "下面那里面有多少是我的、多少是你的？"
    play voice_loop shelley_slow
    scene c011_s008_061 with vpunch
    s "唔~~~ 啊~~~ 一点点都有。滑唔唔~~~ 进来啊~~~"
    scene c011_s008_062 with hpunch
    s "哦靠啊唔~~~ 对哦太舒服了唔唔~~~"
    "就算给她舔了，她还是夹得我紧紧的。一开始得慢一点。"
    scene c011_s008_063 with Dissolve(0.5)
    show shelley_ch11_fuck with Dissolve(0.25)
    s "哦哦哦~~~ 哦呜呜~~~ 哦天哪啊啊啊~~~ 就这样"
    "我们对视着。她完全沉浸在当下。而且说实话，这感觉像是我们到达之前，我第一次不只是为了操她而看着她。"
    s "啊啊啊~~ 哈啊~~~ 哦对就这样"
    s "唔唔~~~ 哦[player_name]啊啊啊~~~ 好大啊啊啊~~~"
    "对，我知道大概是荷尔蒙的作用，但看到她这样，真的让我更觉得雪莉有多可爱。尤其是这是她这么久以来第一次看起来开心的样子。"
    stop voice_loop
    play voice_loop shelley_med
    scene c011_s008_064 with Dissolve(0.5)
    show shelley_ch11_fuck2 with Dissolve(0.25)
    hide shelley_ch11_fuck
    s "哦呜~~~ 哦对啊啊啊~~~"
    s "我让你感觉啊啊啊~~~ 舒服吗？"
    j "当然舒服唔唔~~~。像你这么性感的大学女生。"
    s "我后悔我们啊啊啊~~~ 没能在我的宿舍床上做啊啊啊~~~"
    s "我本来想唔唔~~~ 跟你一起过夜的唔唔~~~"
    j "那时候还早。唔唔~~~ 我们还不够了解彼此。"
    "而且我们大多数做爱都属于一时兴起。"
    scene c011_s008_076 with Dissolve(1)
    hide shelley_ch11_fuck2
    s "但我们现在算是了解了吧？"
    j "我想算。我们得花时间在一起唔唔~~~ 得互相了解。"
    scene c011_s008_077 with Dissolve(0.25)
    s "而你现在还想跟我混啊啊啊~~~？"
    j "当然想。我喜欢你。"
    scene c011_s008_078 with Dissolve(0.25)
    s "我也喜欢你。"
    stop voice_loop
    play voice_loop shelley_fast
    scene blank with Dissolve(1)
    scene c011_s008_065 with Dissolve(1)
    show shelley_ch11_fuck3 with Dissolve(0.25)
    "最后我们换了姿势，让雪莉能靠在枕头上。也让我能开始真正地狠狠干她。"
    s "唔唔~~ 唔唔~~~ 哦靠哦靠啊啊啊~~~"
    j "你喜欢把我整个吞进去，对吧？"
    s "只有一个啊啊啊~~~ 够高的能啊啊啊~~~"
    j "而且你身体还这么柔软唔唔~~~，也不赖。"
    s "你根本就没上什么体操课或者啊啊啊~~~ 瑜伽课。*咯咯笑*"
    j "大概就是天生有天赋吧。"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c011_s008_066 with Dissolve(0.5)
    show shelley_ch11_fuck4 with Dissolve(0.25)
    hide shelley_ch11_fuck3
    s "哈啊~~~ 哈啊~~~ 哦天哪啊啊啊~~~"
    "我感觉她音量提高的时候，已经很接近终点了。天知道我也一样。"
    s "哈啊~~~ 啊啊啊~~~ 操，操~~~"
    s "好深好深~~~ 哦哦哦~~~"
    j "射给我，雪莉唔唔~~~~"
    s "唔唔~~~！！" with vpunch
    s "哦天哪啊啊啊~~~"
    stop voice_loop
    play voice_loop shelley_cum
    scene c011_s008_067 with hpunch
    hide shelley_ch11_fuck4
    pause 0.3
    scene c011_s008_068 with hpunch
    pause 0.3
    scene c011_s008_069 with hpunch
    pause 0.3
    scene c011_s008_068 with hpunch
    pause 0.3
    scene c011_s008_069 with hpunch
    pause 0.3
    scene c011_s008_070 with Dissolve(0.5)
    stop voice_loop
    j "啊靠咝~~~ 要射了~~~"
    scene c011_s008_071 with flash
    play sound male_cum
    pause 0.5
    scene c011_s008_071 with flash
    j "靠对 *喘气* *喘气* 刚才真是 *喘气*"
    scene c011_s008_072 with Dissolve(0.5)
    s "感觉真好。*喘气* 对吧？"
    j "太爽了。你呢？"
    s "最棒的。正合我意。"
    $ renpy.end_replay()
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c011_s008_079 with Dissolve(2)
    play music nightmain fadein 2.0
    j "那么，你现在算是被好好疼爱过了吗？我猜今晚的作业就是这个，对吧？*轻笑*"
    scene c011_s008_080 with Dissolve(0.25)
    s "是的。过去这几天你对我这么好。你那么努力地让我撑下去，哪怕我只想放弃的时候。我……知道有人在希望我留下来，这感觉真好。"
    j "不只是我。卡莉和劳拉也一样。不过对，你不再是一个人了。而且不只是因为做爱。"
    scene c011_s008_081 with Dissolve(0.25)
    s "不过做爱也不差，对吧？"
    j "当然。尤其我还能看到你光着身子。不过这正变成一种习惯。我们要是一直这样下去，我可能就会开始想，我们之间是不是有点什么。"
    scene c011_s008_082 with Dissolve(0.25)
    s "不会。嗯……我觉得我们谁都还没到能做那种决定的处境。一切都太……就像每天光是挣扎着到达一个安全又活着的地方就已经很吃力。"
    s "我不会说我不喜欢这样。我甚至可能会期待它。跟我之前瞎搞过的有些人不一样，我想再见你一面。不只是因为我需要你让我活下去。"
    j "你一个人也完全撑得住。"
    scene c011_s008_083 with Dissolve(0.25)
    s "我领了这个谎的情，但你知道这不是真的。"
    scene c011_s008_084 with Dissolve(0.5)
    j "你的血清素和内啡肽补充够了吗？"
    s "你是在问我感觉好点了吗，对吧？"
    j "拐弯抹角地说：对。"
    scene c011_s008_085 with Dissolve(0.25)
    s "今晚不是为了这个。不过，也许有点用。我现在累了，所以……希望有用吧。"
    scene c011_s008_086 with Dissolve(0.25)
    s "你能不能……我知道你大概得回客厅去，但你能不能陪我到我重新睡着？"
    j "哦，我这是被赶出去了？"
    scene c011_s008_087 with Dissolve(0.25)
    s "不不不，你可以留下。我只是听见你刚才提到值班的事。跟劳拉说的。"
    j "对。很不幸，大窗户，加上是被一个我们不信任的人派来的，我应该待在外面。以防万一。不过我可以先陪你一会儿。"
    scene c011_s008_088 with Dissolve(0.25)
    s "谢谢。我……"
    "她还想说什么，但疲惫加上生活里种种不确定，也许让她把某件自己也没把握的事咽了回去。"
    scene blank with Dissolve(1)
    scene c011_s008_089 with Dissolve(1)
    "过了一会儿，雪莉又睡着了。光着身子，脸上还带着我们刚才那段时间留下的潮红，我很难撒得开她。当然，我们之间大概不会发展出什么长期的东西，但在那一刻，我觉得她格外迷人。"
    scene blank with Dissolve(1)
    scene c011_s008_090 with Dissolve(1)
    "我又磨蹭了几分钟，才终于溜下床，开始重新穿衣服。"
    scene c011_s008_091 with Dissolve(1)
    "别看她嘴上总说自己脆弱又破碎，雪莉能撑到这里已经很不容易了。我见过太多没撑到的。她只需要一些支持就能熬过去。我们每个人都一样。"
    jump shelley_achievement_check
label ch12_shelley_sex:
    $ persistent.ch12_shelley_sex = True
    scene c012_s005_021
    #play music shelleytheme fadein 2.0
    s "这就是我爱听的话。还有，你没放过一个我一离开房间就作废的邀约。"
    scene c012_s005_023 with Dissolve(0.25)
    j "这个没有改期的机会吧？"
    s "没有。还有你干吗不——"
    stop music
    scene c012_s005_025 with hpunch
    s "——坐下。"
    scene c012_s005_026 with hpunch
    play music shelleytheme fadein 2.0
    j "哎哟。你本来可以好好说。"
    s "不了，我一直都说性爱得带点意外才够好玩。"
    j "只要是被按下去这种事，当然行。"
    scene c012_s005_027 with Dissolve(0.25)
    s "还有我的奶子也登场了？"
    j "穿那件上衣？我早赌它肯定会露。不过这个动机我确实很领情。"
    scene c012_s005_028 with Dissolve(0.25)
    s "什么？你是说刚才你还没硬？真丢人。"
    j "我刚从噩梦里醒来，但你的邀约加上公开展示的奶子，迅速把这个状况纠正了过来。"
    scene c012_s005_029 with Dissolve(0.5)
    s "你果然是奶子派男人，对吧？"
    j "说到女人，我对任何东西都来者不拒。"
    scene c012_s005_030 with Dissolve(0.25)
    s "这也太敷衍了，老兄。"
    scene c012_s005_031 with Dissolve(0.25)
    j "好吧，既然你要这么说：你喜欢男人什么？"
    s "哦，你他妈当然知道。当然，好屁股好胸膛是不错，但一旦看到一根又粗又肉的鸡巴，我可能很难再想别的。"
    scene c012_s005_032 with Dissolve(0.5)
    s "而且我告诉你，当我看到这根香肠时，你就已经引起了我的兴趣。*咯咯笑*"
    show shelley_ch12_hj with Dissolve(0.25)
    s "又粗又大，里面哦呜呜呜~~~ 也太爽了。"
    j "啊啊啊~~~ 对，你就一直这样挤着……"
    s "我握得挺紧的吧？我得把手指绕着他才行。"
    j "再这么卖力，我可能就唔唔~~~ 不用插进去了。"
    s "哦，你会想念我的骚穴的。你知道。"
    j "而且，我可能想把你射得满脸都是。"
    scene c012_s005_033 with Dissolve(0.5)
    hide shelley_ch12_hj
    s "哦？已经在挑要喷哪儿了？"
    j "再这么扯我，我可就没得选了。"
    scene c012_s005_034 with Dissolve(0.25)
    s "*咯咯笑* 很高兴我的手活还没生疏。"
    j "你想试的不止这一样吧？"
    scene c012_s005_035 with Dissolve(0.5)
    s "哈。你都等不及要把它塞进我嘴里了。"
    scene c012_s005_036 with Dissolve(0.25)
    j "是你把我弄成这样的，所以没错。"
    "那我把鸡巴塞进她嘴里，好让事情推进下去。"
    scene c012_s005_037 with Dissolve(0.5)
    s "啊啊啊~~~"
    j "靠，我能感觉到你的呼吸吹在我的唔唔~~~ 前端上。"
    play voice_loop blowjob1
    scene c012_s005_038 with Dissolve(0.25)
    j "啊啊啊~~~ 对，就这样。"
    show shelley_ch12_bj with Dissolve(0.25)
    s "啾噜噗~~~ 唔唔~~~"
    j "哦哦哦~~~ 哦呜呜呜~~~"
    "雪莉勤勤恳恳地在我给鸡巴口交时上下吞吐。看她舌头套弄柱身的方式，我猜她挺享受的。"
    s "啾噜噗噗噗~~~ 咝咝~~~~"
    j "呼~~~ 哦靠，对。现在先别回答，不过有没有人告诉过你，你这个挺厉害的？"
    s "唔唔~~~ 唔唔~~~"
    stop voice_loop
    play voice_loop blowjob2
    scene c012_s005_039-1 with Dissolve(0.5)
    show shelley_ch12_bj2 with Dissolve(0.25)
    hide shelley_ch12_bj
    s "嘘咝噗噗噗~~~"
    "当她开始一边扭动脑袋、一边用舌头套弄我的柱身时，我不得不集中注意力，免得提前射出来。"
    j "唔唔~~~ 哈啊~~~ 哦啊啊啊~~~"
    s "啾噜噗噗~~ 唔唔~~~"
    "我很欣赏她想在没有任何回报承诺的情况下让我射出来这份欲望。我之后得为她做点什么。"
    j "哦哦~~ 哦呜~~~"
    s "嘘咝噗噗噗~~~唔唔~~~"
    scene c012_s005_039 with Dissolve(0.5)
    show shelley_ch12_bj3 with Dissolve(0.25)
    hide shelley_ch12_bj2
    s "啾噜噗噗噗~~~~ 咝咝~~~"
    j "哦对啊啊啊~~~ 操~~~ 雪莉"
    "她这次是真用力了。把所有技巧都使出来了。"
    s "咝啾噜噗~~~~ 唔唔~~~"
    j "啊啊啊~~~ 操~~~ 你做到了"
    j "马上就要射了啊啊啊~~~ 只是提醒一下啊~~"
    s "啾噜噗噗噗~~~"
    stop voice_loop
    scene c012_s005_040 with flash
    hide shelley_ch12_bj2
    play sound male_cum
    pause 0.5
    scene c012_s005_040 with flash
    j "哦操我啊啊啊~~~"
    scene c012_s005_041 with Dissolve(0.25)
    j "靠，雪莉。我啊啊啊~~~ 警告过你了。"
    s "唔唔~~~"
    scene c012_s005_042 with Dissolve(0.25)
    j "抱歉，要我给你拿张纸巾吗？"
    scene c012_s005_043 with hpunch
    s "*咕咚*"
    j "或者不用。*轻笑*"
    scene c012_s005_044 with Dissolve(0.5)
    j "我得说，我很受用。天哪，太色情了。"
    s "很高兴听你这么说。现在能睡得像婴儿一样了吗？"
    scene c012_s005_045 with Dissolve(0.25)
    j "嘴里含着个奶子？也许不行。不过我现在放松多了。"
    s "*咯咯笑* 远家晚上再玩吧。不过既然已经开始了，我就想做完。"
    scene c012_s005_046 with Dissolve(0.25)
    j "我们商量个我回请你的方案。哪怕写张欠条也行。"
    scene c012_s005_047 with Dissolve(0.5)
    s "好好好。我这就上床去了。含着你那根鸡巴上下吞吐把我累坏了。"
    scene c012_s005_048 with Dissolve(0.25)
    s "我的上衣呢？"
    j "我想它一路飞到了洗手池那边。"
    scene c012_s005_049 with Dissolve(0.25)
    s "该死，就算我想也做不到第二次了。"
    $ renpy.end_replay()
    scene blank with Dissolve(2)
    scene c012_s005_050 with Dissolve(2)
    "雪莉先去了床上，我挪到沙发上。我在那边躺了一会儿，在脑子里回放着最近发生的事。睡着之前的某个时刻，我忽然想到：睡眠是人类唯一假装在做、实际目的是去做某件事的事。"
    jump shelley_achievement_check
label ch13_shelley_sex:
    $ persistent.ch13_shelley_sex = True
    scene c013_s012_012 with Dissolve(0.25)
    j "嘿。嘿，雪莉，没事的。"
    s "唔？我……"
    stop music fadeout 2.0
    scene c013_s012_013 with Dissolve(0.25)
    j "没事的。我在这儿。你跟在乎你的人在一起。留在我身边。我不知道告诉你你「快发作」有没有用，但我还是告诉你：没事的。我在这儿陪着你。"
    s "我…… *吸鼻子* 谢谢。我想我只是……越来越激动了。"
    scene c013_s012_014 with Dissolve(0.5)
    j "也许有一点，但没关系。"
    s "大多数时候，它发生的时候我自己都察觉不到。我就是——"
    scene c013_s012_067 with Dissolve(0.25)
    j "你没疯，雪莉。别再这么说。你只是在极端处境下做出相应的反应。"
    s "你对我太好了。这就是我这么喜欢你的原因。别人在我犯病的时候不会觉得我烦。"
    j "嗯，大学生嘛，未必总是把别人的利益放在第一位。你们都在摸索自己那堆烂摊子，也许意识不到别人需要有人抱一抱。"
    scene c013_s012_015 with Dissolve(0.25)
    s "也不只是这个，[player_name]。我想要的时候，确实很迟钝，也很自我中心。不过最近，我有时间坐着想想。比我应该想的还要多。"
    j "然后呢？"
    scene c013_s012_068 with Dissolve(0.25)
    s "我不知道该怎么说，因为我从来没真的有过那种欲望。"
    j "那就一口气说出来。电影里有编剧在那儿写最棒的演讲词，不代表现实里是那样运作的。"
    s "或者……"
    play voice_loop kiss
    scene c013_s012_016 with flashpink
    play music shelleytheme fadein 2.0
    "或者，雪莉干脆直接扑到我身上。"
    s "啾噜噗~~~ 唔嗯~~~"
    "事实上，我压根没料到她会这么做，而且雪莉可比其他人大了一圈。"
    stop voice_loop
    scene c013_s012_017 with hpunch
    j "啊啊啊~~~ 哇"
    "当我往后倒去时，我们的吻毫无仪式感地断开了。那一刻我唯一的希望就是床够大，我不会摔下去滚到地上。那样受伤也太蠢了。"
    scene c013_s012_018 with vpunch
    j "哎哟~~~"
    s "哦，天哪，[player_name]。对不起。我不是故意的。我只是……只是太想吻你了。"
    scene c013_s012_069 with Dissolve(0.25)
    j "没事。我只是没准备好让你扑过来。不过我可没抱怨。一个性感半裸的大学生想跟我啃咬？这种好事给我报一个。*轻笑*"
    s "很高兴听你这么说。因为我喜欢那个留着邋遢胡茬、还有一根好鸡巴的成熟男人。"
    scene c013_s012_019 with Dissolve(0.25)
    j "好吧，至少这一点是我的优势，而且我不是什么老金主。这么说胡子是加分项？"
    s "我其实不太在乎，不过我可不是在找一个像婊子一样被人包养的人。我是个婊女——意思是，我这个是免费的。"
    scene c013_s012_020 with Dissolve(0.25)
    j "*轻笑* 该死，我喜欢你拿这些事开玩笑的幽默感。"
    s "你看我眼睛盯着我奶子的样子，我敢肯定你可不只是迷这个。"
    scene c013_s012_021 with Dissolve(0.25)
    j "它们确实很棒。不过你身上别的很多地方也是。而且我得说，那件上衣本来是给谁穿的，那人可比你小得多。"
    s "大概吧。很多女孩都比我小。比如某位——"
    #scene c013_s012_022 with hpunch
    scene c013_s012_023 with hpunch
    j "不重要。过来。闲话少说。"
    scene c013_s012_024 with vpunch
    s "哦天哪，这张床~~~"
    j "我懂了。"
    scene c013_s012_070 with Dissolve(0.25)
    s "这张床没你说得那么大。"
    j "你刚才也没把我推开。我们不会有事的。"
    scene c013_s012_025 with Dissolve(0.5)
    s "你这么说只是因为你想做爱。"
    j "难道你不想？我还以为你的奶子露出来就是为了这个。除非……"
    scene c013_s012_026 with Dissolve(0.25)
    s "哦不，你不想。你可别假装说要从这张床上起来了。"
    j "回去继续啃咬？"
    s "啊啊啊~~~ 随你怎么叫它。"
    play voice_loop kiss
    scene c013_s012_027 with flashpink
    s "啾噜噗~~~ 唔唔~~~"
    "跟雪莉相处得越久，我就越难在我们之间保持一种不带感情的距离。一开始这只是「为了做爱而做爱」和「给我补充点脑内化学物质」。"
    scene c013_s012_028 with Dissolve(0.25)
    "现在，我觉得这稍微不只是那样了。她对感情这类事并不那么外露。或者说不总是如此。但我真的想现在跟她挑明吗？"
    s "唔唔~~~ 啾噜噗~~~"
    stop voice_loop
    scene c013_s012_029 with Dissolve(0.25)
    s "我们该啊啊啊~~~"
    j "进入今晚流程里的做爱环节？"
    s "对。我能感觉到它，它威胁着要冲破你的内裤。"
    scene c013_s012_030 with Dissolve(0.5)
    j "它一向如此。*轻笑* 在你面前。"
    s "不只是我。而且你不用为此撒谎。我可不是个笨姑娘。"
    if k_sex == 0 and l_sex == 0:
        scene c013_s012_031 with Dissolve(0.25)
        j "出人意料的是，我没在跟其他人瞎搞。离婚之后你是第一个跟我上床的女孩。"
        s "这有点甜，也有点让人难以置信。"
        scene c013_s012_032 with Dissolve(0.5)
        j "我那时候精神上实在没处在重新开始找对象的状态。"
        s "哦？*咯咯笑* 这可不算正式交往。我也许喜欢被操，但正常情况下，你不会这么快就上我的床。"
        scene c013_s012_033 with Dissolve(0.25)
        j "要不是那层雾，我们甚至都不会认识彼此。所以我非常怀疑，在正常生活里我们连调情都不会做。"
        s "说不好。我也许会在商店看见你，冲你眨个眼。不过说真的，我对每个我觉得性感的人都这么干。"
        scene c013_s012_034 with Dissolve(0.25)
        j "所以，想约我一顿正式的晚餐约会，还得先努力争取？因为追求者那么多？"
        s "嘿，我撒网撒得广，但这不代表回应多。所以也许你不用费太大力气就能上我的床。*咯咯笑*"

    else:
        scene c013_s012_031 with Dissolve(0.25)
        j "哦，我知道你挺有观察力。也庆幸你不是个长舌妇或者爱吃醋。"
        s "嗯，我不会再给别人制造狗屁事了。不会再让本来就够乱的局面更乱。而且我喜欢你，那样做只会毁掉一件好事。"
        scene c013_s012_032 with Dissolve(0.5)
        j "那你不想独占我咯？"
        s "*咯咯笑* 我不是那种在乎排他性的黏人姑娘。只要你还愿意把好鸡巴送过来就行。"
        scene c013_s012_033 with Dissolve(0.25)
        j "哦？一个「思想境界高」的女人在广撒网？"
        s "就你一个人，也算撒网吗？不过我愿意装得洒脱一点，承认我们没有在交往——虽然现在也不可能。"
        scene c013_s012_034 with Dissolve(0.25)
        j "要是我说我欠你一顿、两顿晚餐约会呢？"
        s "我觉得我们已经跳过那一段了。*咯咯笑*"

    scene c013_s012_035 with Dissolve(0.25)
    s "说起来，把屁股挪过来。我等不及了。"
    j "说得好像你等了很久似的。"
    scene c013_s012_036 with Dissolve(0.25)
    s "我有什么办法？我可不是个有耐心的姑娘。"
    j "我正在学习。对了，这张床是第一次派上用场的概率有多大？"
    s "如果真是，那我们就毁了它，给别人留下心理阴影。"
    play voice_loop shelley_slow
    scene c013_s012_037 with Dissolve(0.5)
    j "这正是计划。"
    s "啊啊啊~~~ 哦靠好烫啊啊啊~~~"
    scene c013_s012_038 with Dissolve(0.25)
    j "说这话的女人，下面正在唔唔~~~ 烧着一团欲火。"
    s "唔~~~ 闭嘴塞进来啊啊啊~~~"
    scene c013_s012_039 with Dissolve(0.25)
    s "哦呜~~~ 哦靠咝~~~"
    scene c013_s012_040 with Dissolve(0.25)
    show shelley_ch13_fuck with Dissolve(0.25)
    "我本该建议她小声点，但我知道没用。我要是想让她安静，早就把她拖到别的地方去了，比如另一栋房子。"
    s "唔唔~~~ 哦呜~~~ 哦啊啊啊~~~"
    s "唔唔~~~ 唔唔唔~~~ 天哪就这样"
    "至少床的弹簧没有尖叫。不过等我真的开始狠干她的时候，我就知道这肯定维持不了。"
    s "哦靠我太需要这个了。"
    scene c013_s012_041 with Dissolve(0.25)
    hide shelley_ch13_fuck
    j "来，把这两条长腿抬起来。"
    s "你喜欢我啊啊啊~~~ 比大多数女孩高，对吧？"
    scene c013_s012_042 with Dissolve(0.25)
    j "还有你身上有点肌肉。"
    s "所以没那么容易就唔唔~~~ 弄坏我。"
    stop voice_loop
    play voice_loop shelley_med
    scene c013_s012_043 with Dissolve(0.5)
    show shelley_ch13_fuck2 with Dissolve(0.25)
    j "这当然是加分项唔唔~~~"
    "跟一个身高跟我差不多、身上有点肌肉的人在一起，确实在我们想真正放开干的时候更方便。我不用担心一狠干就弄坏她。"
    s "唔唔~~~ 我能啊啊啊~~~ 我承受得住。*咯咯笑*"
    j "你明显承受得住唔唔~~~"
    "并不是说雪莉不柔软不脆弱，只是柔软脆弱的方式不同。"
    s "就这样一直操啊啊啊~~~"
    scene c013_s012_044 with Dissolve(0.5)
    hide shelley_ch13_fuck2
    j "说得好像我现在会停似的。"
    s "很好。再用力点啊啊啊~~~ 再用力。"
    stop voice_loop
    play voice_loop shelley_fast
    scene c013_s012_045 with Dissolve(1)
    "在她要求更用力之后，我托起她的胯，开始狠狠干她。"
    s "啊啊啊~~~ 哈啊~~~"
    scene c013_s012_046 with Dissolve(0.5)
    show shelley_ch13_fuck3 with Dissolve(0.25)
    s "哦操，啊啊啊~~~ 啊啊啊~~~"
    j "靠你啊啊啊~~~ 太好了"
    s "就这样唔唔~~~ 好深哦哦哦~~~"
    s "靠你啊啊啊~~~ 好他妈大啊啊啊~~~"
    s "啊啊啊~~~ 哈啊~~~ 唔唔~~~"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c013_s012_047 with Dissolve(0.5)
    show shelley_ch13_fuck4 with Dissolve(0.25)
    hide shelley_ch13_fuck3
    "雪莉湿透的骚穴发出咕叽咕叽的声响，我狠抽着，发誓要尽快射出来。从她的嚎叫里我知道，她大概也撑不了多久了。"
    s "唔唔~~~ 哦哦~~~ 哦呜~~~"
    j "操，啊啊啊~~~ 啊啊啊~~~"
    s "啊啊啊啊~~~ 哦哦~~~ 天哪，对啊啊啊~~~"
    s "就这样啊，快了哦哦哦~~~"
    s "操，唔唔唔~~~！！" with vpunch
    s "靠咝咝~~~" with vpunch
    stop voice_loop
    play voice_loop shelley_cum
    scene c013_s012_048 with hpunch
    hide shelley_ch13_fuck4
    pause 0.3
    scene c013_s012_049 with hpunch
    pause 0.3
    scene c013_s012_050 with hpunch
    pause 0.3
    scene c013_s012_051 with hpunch
    pause 0.3
    scene c013_s012_052 with Dissolve(0.5)
    stop voice_loop
    "再也忍不住了。"
    scene c013_s012_053 with flash
    play sound male_cum
    pause 0.5
    scene c013_s012_053 with flash
    j "哦靠啊啊啊~~~ 对哦哦哦~~~ *喘气*"
    s "靠，那真是啊啊啊~~~ *喘气* *喘气* 太爽了。"
    j "对，真的。"
    s "嘿，呃……来……"
    play voice_loop kiss
    scene c013_s012_054 with flashpink
    "我躺在那儿，剧烈活动后的余韵慢慢消退，体内的精液还在往外流，这时我意识到雪莉最近越来越亲昵了。或者说，是我以为她越来越亲昵。也许她只是沉浸在当下。"
    s "啾噜噗~~~ 唔嗯~~~"
    scene c013_s012_071 with Dissolve(0.5)
    "我承认我挺喜欢这种感觉的。喜欢「她和我」这个组合。但也许那只是因为我们刚做完。等这一刻过去，我还会一样吗？她还会吗？而后者大概是更重要的问题。"
    s "啾噜噗~~~ 唔唔~~~"
    stop music fadeout 2.0
    stop voice_loop
    jump shelley_achievement_check
label ch14_shelley_sex:
    $ persistent.ch14_shelley_sex = True
    scene c014_s005_023 with Dissolve(1)
    "即使我朝她走去，她也没有任何意识到我在旁边的迹象。她肯定陷在思绪深处了。"
    j "雪莉？"
    scene c014_s005_074 with Dissolve(0.25)
    j "嘿，你。你没事吧？"
    s "唔？哦，啊……对。我想是吧。我刚才只是看着外面，没什么特别的原因，就是……"
    j "在想事情？"
    "她的眼睛有点红，像是哭过。"
    scene c014_s005_075 with Dissolve(0.25)
    s "比以前还红。我以前从来不站着不动到足以让任何事留在心上。这招对我管用了太久。"
    j "抱歉……？"
    scene c014_s005_076 with Dissolve(0.25)
    s "没事。我只是意识到我以前有多空虚。"
    j "你对自己有点太狠了。"
    scene c014_s005_077 with Dissolve(0.25)
    s "我这是……在自省。是个新养成的习惯。我想是从你和卡莉那儿学的。"
    j "别让它困住你。有时候想太多对一个人没好处。"
    scene c014_s005_078 with Dissolve(0.25)
    s "什么？你更喜欢我这个傻乎乎的花瓶？"
    j "你不是花瓶。不过你确实很有趣，我喜欢你这一点。我知道我随时都能被你逗笑。"
    scene c014_s005_024 with Dissolve(0.25)
    s "就只是这样~~~？"
    stop music fadeout 2.0
    scene c014_s005_025 with Dissolve(0.25)
    j "这个问题问得很有陷阱。而且你知道我还喜欢你什么。"
    scene c014_s005_026 with Dissolve(0.25)
    s "你是说这些？*咯咯笑*"
    j "虽然很难让人相信，但我确实不只把你当成性感大学女生的身体。"
    scene c014_s005_027 with Dissolve(0.5)
    s "但那是我性格的核心。*咯咯笑*"
    j "我希望你在这一点上是在跟我开玩笑。"
    s "这重要吗？操，吻我。"
    play voice_loop kiss
    scene c014_s005_028 with flashpink
    play music shelleytheme fadein 2.0
    s "啾噜噗~~~ 唔唔~~~"
    "雪莉花太多时间贬低自己了，好像那个爱调情的骚货底下藏着一个需要人照顾的温柔女孩。不过现在大概不是坐下来谈这件事的时候。尤其当我感觉到她在扯自己的胸罩。"
    stop voice_loop
    scene c014_s005_029 with Dissolve(0.25)
    s "哈啊~~~ 这就是你叫我来的原因？"
    j "这样我们就能不被打扰地瞎搞？其实不是。但现在我也非常不想错过这个机会。"
    play voice_loop shelley_slow
    scene c014_s005_030 with Dissolve(0.25)
    s "你最好啊啊啊~~~ 不要。"
    j "只要你的奶子一露出来就不行。不过你已经知道了吧？我可不是第一个被你那性感屁股吸引过来的人。"
    s "第一个。最后一个。谁在乎？啊啊啊~~~"
    stop voice_loop
    play voice_loop kiss
    scene c014_s005_031 with flashpink
    "雪莉猛地转过头来抢我的嘴唇。她的舌头滑进我嘴里的同时，我感觉到她柔软的屁股压在我的胯上。"
    s "啾噜噗~~~ 唔唔~~~"
    stop voice_loop
    scene c014_s005_032 with Dissolve(0.25)
    s "好吧好吧，虽然我很喜欢你玩弄我那两个奶子，但你至少得把那件夹克脱了。它很臭，而且我知道底下有好得多的东西。"
    j "比如我的蓝色高尔夫衫。*轻笑*"
    scene c014_s005_033 with Dissolve(0.5)
    s "那也一点都不好，你知道我什么意思。我可不能是这儿唯一露皮肤的人。"
    j "对，但你的皮肤比我的有意思多了。"
    scene c014_s005_035 with Dissolve(0.25)
    s "这也许有那么一点点对。*咯咯笑* 我不再往下说了，因为你们不太经得起夸奖。好像你们都缺关注缺得厉害，我随口说一句「你屁股真性感」，你就飘起来了。"
    j "这话太私密了。而且我从没那样看过自己。"
    scene c014_s005_036 with Dissolve(0.25)
    s "不是你。我是说男人这种生物。你们总是把夸奖变成玩笑，所以我知道有人把你伤得不轻。"
    j "你再这么往我心理深处钻，性爱可就要从我的选项里划掉了。"
    scene c014_s005_037 with Dissolve(0.25)
    s "你一边说一边让我扯下你的衬衫。*咯咯笑*"
    scene c014_s005_038 with Dissolve(0.25)
    s "听着，我那么说不是想伤你。我喜欢你。非常喜欢。但你身上确实有伤。我知道南希伤过你，但我不是她。"
    j "我没想把你当成她对待，雪莉。"
    scene c014_s005_079 with Dissolve(0.25)
    s "我……我不是这个意思。你控制不住自己。我们某种程度上都让过去的关系定义了自己。也许这就是我从来不去抓紧任何东西的原因。你不会指望一个新来的人像对待前任那样对你，因为你连花十分钟在乎他们都没有过。"
    j "而我在那之前是新恋人——"
    scene c014_s005_080 with Dissolve(0.25)
    s "我不是那个意思。求你别多想。我知道你想，因为你就是这样。我只是……我们能继续吗？我想要。我希望你也是。"
    j "对，让我这次别再想太多。"
    scene c014_s005_039 with Dissolve(0.5)
    s "好，我们可以等做完再想。等射完的迷雾散去。"
    j "这事肯定会发生的。*轻笑*"
    scene c014_s005_040 with Dissolve(0.25)
    s "通常那就是后悔和「靠，我有个女朋友或者男朋友」开始登场的时候。"
    j "听这口气像是听过不少。"
    scene c014_s005_041 with Dissolve(0.25)
    if k_sex >= 1 or l_sex >= 1:
        s "我挺意外你没更常提这件事。"
        j "也许等我不在了。"
    else:
        s "也许不止一次。不过我以前从没追过我认为已经有对象的人。先说清楚。我不是破坏别人家庭的人。"
        j "知道了。"
    scene c014_s005_081 with Dissolve(0.25)
    s "好了，闲话少说。把鸡巴掏出来，坐到床上。"
    j "是，长官。"
    scene c014_s005_042 with Dissolve(1)
    s "*咯咯笑* 「长官」？以前从没人这么叫过我。太年轻了。"
    j "那是一种尊称。"
    scene c014_s005_043 with Dissolve(0.25)
    s "也许我一直没做过什么值得被尊敬的事。更像是那种「你这骚货」型的姑娘。"
    j "我对你的人生了解不够，没法判断这是不是你在为了戏剧效果而夸大其词。我觉得这一点我得纠正一下。"
    scene c014_s005_044 with Dissolve(0.25)
    s "既然我们已经在做了？我们是不是顺序弄反了？"
    j "要不这样，等我们出去了，我请你吃一顿晚餐约会？"
    s "那么，我大概该在一家很棒的餐厅里挣一个。"
    scene c014_s005_045 with Dissolve(0.25)
    j "我是说……哦……对，那个。"
    play voice_loop blowjob1
    scene c014_s005_046 with Dissolve(0.25)
    s "嘘咝噗噗噗~~~ 唔嗯~~~~"
    show shelley_ch14_bj with Dissolve(0.25)
    j "哦哦哦~~~ 哦对，虽不是我进来的目的，但我收下了。"
    s "唔唔~~~ 咝啾噜~~~"
    "她摇晃的样子让我觉得雪莉在笑我那句话。"
    s "啾噜噗~~~ 唔唔~~~"
    j "哦哦哦~~~ 哦呜呜呜~~~~"
    stop voice_loop
    play voice_loop blowjob2
    scene c014_s005_047 with Dissolve(0.5)
    show shelley_ch14_bj2 with Dissolve(0.25)
    hide shelley_ch14_bj
    j "啊啊啊~~~ 哈啊~~~ 靠，姑娘。"
    "希望这地方以后有人住的话，等这一切结束回来，不会纳闷是谁把他们的床弄得一团糟，因为很快就会有液体流出来。"
    s "啾噜噗噗噗~~~ 咝咝~~~~"
    j "哦呜~~~ 哦哦~~~"
    "我可能得叫她慢一点，不然我就要射了。虽然我不认为短时间内它不会再硬起来进行第二轮。"
    s "啾噜噗~~"
    scene c014_s005_048 with Dissolve(0.25)
    hide shelley_ch14_bj
    stop voice_loop
    "我不知道她有没有察觉我快到了，但雪莉停了下来。她退开脑袋时，顽皮地舔了舔我的前端。"
    j "天哪，你吸鸡巴真够狠。"
    scene c014_s005_049 with Dissolve(0.25)
    s "我别的性感招数也做得很好。"
    j "那你得展示给我看。"
    scene c014_s005_082 with Dissolve(0.25)
    s "如果你在邀请的话……"
    j "对你？永远都愿意。"
    scene c014_s005_050 with Dissolve(0.5)
    s "[player_name]？"
    "她脸上有种奇怪的表情，好像我那句话触动了她某根弦。"
    scene c014_s005_051 with hpunch
    j "哦哦~~~ 哦哎哟！！"
    "雪莉扑上来压在我身上，用某种笨拙的动作想压倒我。这让我吃了一惊。"
    play voice_loop kiss
    scene c014_s005_053 with flashpink
    "她整个人覆在我身上，吻我时带着比平时更多的东西。通常接吻只是她在调情，或是把气氛往正确方向推的手段。但这一次，感觉像是失散多年的恋人重逢。"
    s "啾噜噗~~~ 唔嗯~~~~"
    stop voice_loop
    scene c014_s005_054 with Dissolve(0.5)
    j "唔嗯~~~ 我喜欢这个。"
    s "[player_name]……"
    j "雪莉？"
    scene c014_s005_083 with Dissolve(0.25)
    s "我……我喜欢你。"
    j "你说过这话了。"
    s "说了很多次。"
    scene c014_s005_052 with Dissolve(0.25)
    j "我记得我也听你说过。"
    s "那是真的。"
    j "雪莉？"
    scene c014_s005_055 with Dissolve(0.25)
    s "好了好了，够了，肉麻的情绪。我有你非常需要放在我体内的东西。"
    j "够了？我们几乎什么都没聊。"
    "而且我感觉这本来是要通向某个地方的。"
    scene c014_s005_056 with Dissolve(0.25)
    s "来。就是他。扶住我。别让我——"
    j "摔倒？知道了。"
    play voice_loop shelley_slow
    scene c014_s005_057 with Dissolve(0.25)
    s "哦哦哦~~~ 操我啊啊啊~~~"
    j "马上就好，再唔唔~~ 一秒。"
    scene c014_s005_058 with vpunch
    s "靠，你啊啊啊~~~"
    j "舒服吗？"
    scene c014_s005_059 with vpunch
    s "好他妈大。"
    j "你又来了，用夸奖，想把我整个人都撩起来。"
    scene c014_s005_060 with Dissolve(0.5)
    show shelley_ch14_fuck with Dissolve(0.25)
    s "如果这是真的，就不算夸奖啊啊啊~~~"
    j "那我就信你的话了啊啊啊~~"
    s "毕竟我是个姑娘，我懂这个，对吧？*咯咯笑*"
    j "那可不是我说的唔唔~~~话。"
    s "我知道。只是啊啊啊~~~ 在开玩笑。"
    stop voice_loop
    play voice_loop shelley_med
    scene c014_s005_061 with Dissolve(0.5)
    show shelley_ch14_fuck2 with Dissolve(0.25)
    hide shelley_ch14_fuck
    s "啊啊啊~~~ 哈啊~~~ 哦靠啊啊啊~~~"
    "得小心点。我们这种打情骂俏有时候会滑向像在评判对方。我对她和她的生活了解不够，没法真的下那种判断。说真的，据我所知她身上背的账可能没她说的那么多。"
    j "唔唔~~~ 靠，对"
    s "哈啊啊啊~~~ 操我，天哪我太需要这个了。"
    j "你我都一样。"
    "而且，也许这一次，我该别再钻自己脑子里的牛角尖，好好享受这一刻。不过，我有种感觉是我们有些事得谈谈。"
    stop voice_loop
    scene blank with Dissolve(1)
    scene c014_s005_062 with Dissolve(1)
    play voice_loop shelley_fast
    show shelley_ch14_fuck3 with Dissolve(0.25)
    hide shelley_ch14_fuck2
    "某个时刻，我们换了姿势，我开始像拼了命一样狠干雪莉。"
    s "哦靠咝~~~ 啊啊啊~~~"
    j "对，就是让那两个屁股瓣啪啪响。"
    s "唔唔~~~ 别逗我笑，我会……"
    j "说会破坏气氛。"
    s "至少唔唔~~~ 我们还能享受再接再厉的乐趣。"
    "周围没人的话，我们确实可以。想的话，我们可以整整做一天。我也知道那不会发生。我们再不回去，其他人该担心了。"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c014_s005_063 with Dissolve(0.5)
    show screen ch14_shelley_change with Dissolve(0.25)
    $ Show("ChangeCamera_s_ch14", transition=Dissolve(1.0))()
    hide shelley_ch14_fuck3
    "当我们终于意识到只有我们两个人时，我才明白我们不必小声。于是我好好地、狠狠地把雪莉操了一遍。"
    s "哦靠咝咝~~~ 啊啊啊~~~"
    "汗津津的，我狠命地抽插着她，气喘吁吁。我只想射进她体内。留下我们玩得痛快的证据，哪怕只是短短一会儿。"
    s "靠靠~~~ 咝咝咝~~~ 啊啊~~~"
    "雪莉开始以一种感觉快要到了的方式抽搐。"
    j "唔唔~~~ 哦啊啊啊~~~"
    s "靠啊啊啊~~~" with vpunch_soft
    s "唔唔~~~ 哦啊啊啊~~~~"
    $ Hide("ChangeCamera_s_ch14", transition=Dissolve(1.0))()
    hide screen ch14_shelley_change
    stop voice_loop
    play voice_loop shelley_cum
    scene c014_s005_065 with hpunch
    hide shelley_ch14_fuck4
    hide shelley_ch14_fuck5
    pause 0.3
    scene c014_s005_066 with hpunch
    pause 0.3
    scene c014_s005_067 with hpunch
    pause 0.3
    scene c014_s005_066 with hpunch
    pause 0.3
    scene c014_s005_067 with hpunch
    pause 0.3
    scene c014_s005_068 with Dissolve(0.5)
    stop voice_loop
    s "哦呜~~~"
    "我几乎没注意到她嘴里溢出的那声呜咽。我当时有点专注于别的地方。"
    scene c014_s005_069 with flash
    play sound male_cum
    pause 0.5
    scene c014_s005_070 with flash
    pause 0.5
    scene c014_s005_071 with Dissolve(0.5)
    s "{size=30}天哪……那感觉哈啊~~~ {/size}"
    j "对。*喘气* 对。"
    scene c014_s005_072 with Dissolve(0.5)
    j "来，让我……"
    s "小心。你*喘气* 把我里面灌满了。会到处流出来。"
    scene c014_s005_073 with Dissolve(0.5)
    j "不是我的床。那就不是我的问题。"
    s "只是你留在我体内的那点「婴儿汁」而已。*咯咯笑*"
    $ renpy.end_replay()
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c014_s005_084 with Dissolve(2)
    play music insideday3 fadein 2.0
    "接下来的十到十五分钟，我们只是躺在那儿，光着身子，汗津津的，大口喘气，为这场没计划的运动哼哼唧唧。我脑子里记着一些之前做的笔记，考虑过要不要提出来。"
    scene c014_s005_085 with Dissolve(0.5)
    $ shelley_admitlike = "yes"
    "雪莉决定抢先开口。"
    s "嘿。我知道有些话是一时冲动之下说的之类的……"
    j "枕边话？我懂。"
    scene c014_s005_086 with Dissolve(0.5)
    s "不是。我……其实真的喜欢你。是那种真的喜欢。当然，做爱挺棒的，但你不止是一个现成的鸡巴。你一直……我以前从不让别人靠近我，因为我怕他们看到我状态不好的样子，然后跑掉。"
    s "你……你在我最糟的时候在场，而且一直陪着我撑过来。而这……我以前从来没有过。"
    j "我在乎你，雪莉。你很善良。很有趣。有点傻乎乎的。但你本质上是个好人。漂亮得要命。性感。就算我们不做爱，我还是会喜欢你。"
    scene c014_s005_087 with Dissolve(0.25)
    s "但我这么——"
    j "不，雪莉。每个人都在用自己的方式处理这些。我理解。"
    scene c014_s005_088 with Dissolve(0.25)
    s "嗯，我……我真的喜欢你。你不用说什么。知道就行。"
    scene c014_s005_089 with Dissolve(0.5)
    if ch13_kallie_sex == "yes" or ch12_kallie_sex == "yes" or ch12_laura_sex == "yes":
        if ch13_kallie_sex == "yes" or ch12_kallie_sex == "yes" and ch12_laura_sex == "no":
            s "而且，我这么说不是在宣示什么排他性。因为我以前在这方面一点也不好。我知道你和卡莉的事。"
        elif ch13_kallie_sex == "no" or ch12_kallie_sex == "no" and ch12_laura_sex == "yes":
            s "而且，我这么说不是在宣示什么排他性。因为我以前在这方面一点也不好。我知道你和劳拉的事。"
        else:
            s "而且，我这么说不是在宣示什么排他性。因为我以前在这方面一点也不好。我知道你和其他人的事。"
        j "你对此可一点都不含糊。"
        scene c014_s005_090 with Dissolve(0.25)
        s "只是……"
        j "雪莉？"
        s "没什么。只要知道，遇见你是我很久以来遇到的最棒的事。谢谢。"
    else:
        j "那很好，因为那会让做爱变得有点尴尬。至少对我来说会。"
        s "我听说「恨意性爱」这种东西存在。不过我不行。我确实得喜欢一个人。或者说，{b}真的很喜欢{/b}一个人。"
        scene c014_s005_091 with Dissolve(0.25)
        j "我就当自己已经进入「真的很喜欢」这一档了。"
        s "你确实进入了。"
    scene c014_s005_092 with Dissolve(1)
    "雪莉沉默下来时，我知道不该逼她。我见过她为梅茜流泪，也见过她对自己的神志感到恐惧。我渐渐明白，让这一刻自然呼吸是很重要的。"
    scene c014_s005_093 with Dissolve(0.5)
    "过了一会儿，我起身说我得去把巡查走完。"
    scene c014_s005_094 with Dissolve(0.5)
    "雪莉停留了片刻，然后说她要去洗手间收拾一下。"
    scene blank with Dissolve(2)
    scene c014_s005_095 with Dissolve(2)
    "{color=#8bc7ff}天哪，他真的在我里面灌了好多。我觉得应该没事。如果不是……算了，管他的。{/color}"
    scene c014_s005_096 with Dissolve(0.25)
    "{color=#8bc7ff}那会不会是最糟的？我是说，在雾里怀孕。操，那对胎儿会有什么影响？我连想都不想。{/color}"
    "{color=#8bc7ff}但我和他？我不想用这种方式困住他，不过他会对我好的。我知道会。而且我真的喜欢他。也许还更多一些。{/color}"
    scene c014_s005_097 with Dissolve(0.25)
    "{color=#8bc7ff}擢，现在不是想「关系」和这些屁事的时候。{/color}"
    jump shelley_achievement_check
label ch15_shelley_sex:
    $ persistent.ch15_shelley_sex = True
    play voice_loop kiss
    scene c015_s005_001 with flashpink
    play music shelleytheme fadein 2.0
    s "啾噜噗~~~ 唔唔~~~"
    "我坐下来跟她聊天时本没打算这样，但我们之间有种化学反应，让从聊天转到啃咬变得很容易。而且雪莉本来就不需要多少铺垫就能从零跳到「来操吧」。"
    stop voice_loop
    scene c015_s005_044 with Dissolve(0.25)
    s "*咯咯笑* 你知道我在想什么吗？"
    j "真的？我还以为自己是下来替你值夜班的。"
    s "这也算是在「慰劳」我。"
    scene c015_s005_002 with Dissolve(0.25)
    j "我很欣赏你这么一按开关就能操。不过我还是没搞明白，那个开关到底是被什么打开的。"
    scene c015_s005_003 with Dissolve(0.25)
    s "性感的人。还有我喜欢的人。你两样都占了。不过我知道什么能让你兴奋起来。"
    scene c015_s005_045 with Dissolve(0.25)
    j "嗯，反正就是奶子。特别是你的。"
    s "考虑到我接下来想做什么，你最好这么说。"
    scene c015_s005_004 with Dissolve(0.25)
    j "你确定不要先试试弄点——"
    s "都这样了还想别的。你应该更清楚。"
    scene c015_s005_005 with Dissolve(1)
    if ch14_shelley_sex == "yes":
        "雪莉花了几秒钟的尴尬才爬到我腿上。她一坐稳就盯着我的眼睛，像是在考虑下一步该干什么。或者说有话想说。考虑到她之前的坦白，我可以猜个大概。"
    else:
        "雪莉花了几秒钟的尴尬才爬到我腿上。她一坐稳就盯着我的眼睛，像是在考虑下一步该干什么。或者说有话想说。"
    "我没有等着听她要说什么，而是决定主动推进。"
    play voice_loop shelley_slow
    scene c015_s005_006 with Dissolve(0.25)
    s "哈啊啊啊~~~~ 对啊啊啊~~~ 我就知道你啊~~~ 会的"
    s "记得唔唔~~~ 两个都要唔唔~~~"
    scene c015_s005_007 with Dissolve(0.25)
    "我还没脱内裤——更别说进到她里面了——雪莉就已经叫得很响了。"
    s "哦哦~~~ 操我，我啊啊啊~~~"
    stop voice_loop
    scene c015_s005_008 with Dissolve(0.25)
    if ch14_shelley_sex == "yes":
        s "哦天哪，我要是早知道跟成熟男人做爱这么他妈好玩，我早就该多来几次了。"
        j "我还以为只有我这么想。"
    else:
        s "[player_name]……"
        j "雪莉？"
        scene c015_s005_046 with Dissolve(0.5)
        s "我……我喜欢你。"
        j "你之前说过了。"
        scene c015_s005_047 with Dissolve(0.25)
        s "说了很多次。"
        j "我记得我也听你说过。"
        scene c015_s005_048 with Dissolve(0.25)
        s "那是真的。"
        j "雪莉？"
    play voice_loop kiss
    scene c015_s005_009 with flashpink
    s "啾噜噗噗噗~~~ 嘘咝噗噗~~~"
    "她把私处在我的私处上磨蹭。隔在我们之间的，只有薄薄两层布。"
    stop voice_loop
    scene c015_s005_010 with Dissolve(0.25)
    s "哈啊啊啊~~~ 我觉得我刚才好像漏了一点在里面。*咯咯笑*"
    j "我们可以确保不止「一点」。"
    scene c015_s005_011 with Dissolve(0.25)
    s "很快，不过我还有别的事想做。为了你。"
    j "这已经像是我们为彼此一起做的事了。"
    scene c015_s005_012 with Dissolve(0.25)
    s "让我也回礼一次。"
    j "回礼就是把我的短裤扯掉？*轻笑* 因为这对我来说不算什么大不方便。"
    scene c015_s005_013 with Dissolve(0.25)
    s "你就是那种想知道圣诞礼物是什么、还要提前两周拆开看的人，对吧？"
    j "这可不是「两周」那种情况。这是正在发生的事，我想知道我现在该不该坐着。"
    scene c015_s005_014 with Dissolve(0.5)
    s "待在你别动，让那根硬邦邦的肉棒完全立着。"
    j "有你那两个奶子在外面晃，我可硬不起来。"
    scene c015_s005_015 with Dissolve(0.25)
    s "我很高兴你这么说。*咯咯笑*"
    j "哦呜~~~ 啊~~ 好吧，对，就这样。"
    show shelley_ch15_tj with Dissolve(0.25)
    s "你看起来这招对你很有效唔唔~~~"
    j "柔软、滚烫，还裹着我的命根子啊啊啊~~~ 对。"
    j "不过我不确定这对你有没有多大用。"
    s "你会很意外唔唔~~~的"
    s "其中很大一部分快乐，来自看见你喜欢的人正在享受啊啊啊~~~ 享受「你」。"
    scene c015_s005_016 with Dissolve(0.5)
    show shelley_ch15_tj2 with Dissolve(0.25)
    hide shelley_ch15_tj
    j "我是啊。"
    s "而且，摩挲这么粗这么烫的东西，确实让我啊啊啊~~~ 的汁液都流出来了。"
    j "啊啊啊~~~ 可不止一种汁液在动。"
    s "我在想象他在别的地方稍微夹紧一点唔唔~~~"
    j "我们可以进行到那一步了唔唔~~~"
    scene c015_s005_017 with Dissolve(0.25)
    hide shelley_ch15_tj2
    s "我本来就打算那样。我只是想看看你能离射出来多近。"
    scene c015_s005_018 with Dissolve(0.5)
    j "够近了。把那条内裤脱掉。"
    s "更像是剥下来。*咯咯笑*"
    #reshoot scene c015_s005_019 with Dissolve(0.25)
    j "这个区别我爱听。"
    scene c015_s005_020 with Dissolve(0.25)
    s "我知道，这能给我自信。"
    j "尽管说实话，并不完全是因为我——"
    scene c015_s005_021 with Dissolve(0.25)
    s "不。别用这种语气说话。我不吃这一套。"
    j "好吧。有些习惯很难改。"
    s "那我们就养成一些新习惯吧。"
    play voice_loop kiss
    scene c015_s005_022 with flashpink
    s "啾噜噗~~~ 唔唔~~~"
    "最近雪莉对我贬低自己的话反应奇怪地强烈。是很微妙的，但这已经不是她第一次驳回我的自我批评了。"
    scene c015_s005_023 with Dissolve(0.5)
    "尽管这很难做到，我可能不得不承认雪莉被我吸引了。当然，她把自己扮演成一个性感的生物，但我不能想当然地认为她对自己的情人毫无差别。"
    stop voice_loop
    scene c015_s005_024 with Dissolve(0.25)
    s "你前任是个愚蠢的婊子，不知道自己错过了什么。你在我眼里性感得要命。"
    j "嗯，只要你自己这么觉得，那才重要。"
    scene c015_s005_025 with Dissolve(0.25)
    s "确实重要。你该坐到沙发上去了。"
    j "我刚从那儿回来。"
    s "那你的屁股印应该还在。"
    scene c015_s005_026 with Dissolve(1)
    j "好吧，既然我们说性感女神……"
    scene c015_s005_027 with Dissolve(0.25)
    s "今晚我不是想让你亲我屁股。*咯咯笑* 也许下次。"
    j "时间线拉得够长的话，我感觉你想对我做的事可多了。"
    scene c015_s005_028 with Dissolve(0.5)
    s "你是在说这要变成固定项目吗？对。我想让你对我做的事太多了。"
    s "不过，首先……"
    play voice_loop shelley_slow
    scene c015_s005_029 with vpunch
    s "哦呜~~~ 天哪，你的鸡巴啊啊啊~~~"
    "她那么湿，却又那么紧、那么烫。"
    scene c015_s005_030 with vpunch
    s "操我啊啊啊~~~ 天哪你他妈把我灌满了。"
    j "我尽力了。*轻笑*"
    scene c015_s005_033 with Dissolve(0.25)
    show shelley_ch15_fuck with Dissolve(0.25)
    s "哈啊~~~ 唔唔~~~"
    "我知道我们该注意外面，但也许一点带点爱的干扰对我们俩都有好处。"
    s "唔唔~~~ 哦靠，啊啊啊~~~"
    "对雪莉来说，我把这当成让她保持好心情。也许还不止如此。那些「我喜欢你」的话里暗示着更多。"
    s "哈啊啊啊~~~~ 哦天哪啊啊啊~~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c015_s005_034 with Dissolve(0.5)
    show shelley_ch15_fuck2 with Dissolve(0.25)
    hide shelley_ch15_fuck
    s "哦靠，啊啊啊~~~ 唔唔~~~"
    "至于我？我喜欢她。不然我不会这么老是以光着身子的状态和她待在一起。"
    j "靠，姑娘，你感觉真好。"
    s "哦哦~~~ 好他妈粗啊啊啊~~~"
    s "这个我可以啊啊啊~~~ 整晚都做下去。"
    "离天亮只剩几个小时了，但我觉得我能撑够久。"
    stop voice_loop
    scene blank with Dissolve(1)
    scene c015_s005_035 with Dissolve(1)
    show screen ch15_shelley_change with Dissolve(0.25)
    $ Show("ChangeCamera_s_ch15", transition=Dissolve(1.0))()
    play voice_loop shelley_fast
    hide shelley_ch15_fuck2
    "过了一阵子，我们换了姿势。这让我得以缓一口气，忍住不射。尽管我多想连着好几个小时地操雪莉，但我怀疑自己没那个体力。"
    s "哦哦哦~~~ 再用力点啊啊啊~~~"
    "她身上的一切都在加倍努力把我推过临界点。她柔软的屁股撞着我的腰。她的呻吟。她摇曳的奶子，每次挺进都会晃动。"
    s "哦呜~~~ 哦靠咝~~~"
    j "小声点。"
    s "你啊啊啊~~~ 干得我这么狠，很难做到啊 *咯咯笑*"
    $ Hide("ChangeCamera_s_ch15", transition=Dissolve(1.0))()
    hide screen ch15_shelley_change
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c015_s005_037 with Dissolve(0.5)
    show shelley_ch15_fuck5 with Dissolve(0.25)
    hide shelley_ch15_fuck3
    hide shelley_ch15_fuck4
    j "哦，那我应该更用力才对啊啊啊~~~"
    s "你最爱的就是我用力的时候啊啊啊~~~ 我知道"
    "管他的。到了这一步，我只想把一肚子东西全灌进她体内。"
    s "哈啊~~~ 哈啊~~~"
    "离她这么近，浑身是汗地干着，这让我想起我对她的感觉。我知道那只是一波会消退的内啡肽，但就算我们不是这样的时候，也确实有些什么存在吧？"
    s "哦靠老兄啊啊啊~~~"
    s "天哪，就这样！！！" with vpunch_soft
    s "啊啊啊~~~"
    stop voice_loop
    play voice_loop shelley_cum
    scene c015_s005_038 with vpunch
    hide shelley_ch15_fuck5
    pause 0.3
    scene c015_s005_038 with vpunch
    pause 0.3
    scene c015_s005_039 with vpunch
    pause 0.3
    scene c015_s005_039 with vpunch
    pause 0.3
    scene c015_s005_040 with vpunch
    pause 0.3
    scene c015_s005_041 with Dissolve(0.5)
    stop voice_loop
    s "哦呜~~~ 操~~~"
    j "唔唔唔~~~" with hpunch_soft
    scene c015_s005_042 with flash
    play sound male_cum
    pause 0.5
    scene c015_s005_042 with flash
    pause 0.5
    scene c015_s005_043 with Dissolve(0.5)
    s "哦呜~~~ *喘气* 刚才那…… *喘气*"
    j "对。*喘气*"
    scene c015_s005_049 with Dissolve(0.5)
    s "操，*喘气* 真是把我累惨了。"
    j "嗯，谁让你一勾引我就停不下来。"
    s "我看得出来。*咯咯笑*"
    $ renpy.end_replay()
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c015_s005_050 with Dissolve(2)
    play music nightmain2 fadein 2.0
    "有一小会儿，我们只是坐在那儿，雪莉在我怀里。时不时地，她会发出一声听起来很满足的呻吟。"
    scene c015_s005_051 with Dissolve(1)
    if ch14_shelley_sex == "no":
        $ shelley_admitlike = "yes"
        s "嘿。之前……我说了句话……"
        j "说了类似喜欢我的话。我以为那是一时冲动说的。欲念上头之类。"
        scene c015_s005_052 with Dissolve(0.25)
        s "不。我……其实真的喜欢你。是那种真的喜欢。当然，做爱挺棒的，但你不止是一个现成的鸡巴。你一直……我以前从不让别人靠近我，因为我怕他们看到我状态不好的样子，然后跑掉。"
        scene c015_s005_053 with Dissolve(0.25)
        s "你……你在我最糟的时候在场，而且一直陪着我撑过来。而这……我以前从来没有过。"
        j "我在乎你，雪莉。你很善良。很有趣。有点傻乎乎的。但你本质上是个好人。漂亮得要命。性感。就算我们不做爱，我还是会喜欢你。"
        scene c015_s005_054 with Dissolve(0.25)
        s "但我这么——"
        j "不，雪莉。每个人都在用自己的方式处理这些。我理解。"
        scene c015_s005_055 with Dissolve(0.25)
        s "嗯，我……我真的喜欢你。你不用说什么。知道就行。而且你该别再说自己坏话了。别再说自己不够性感。我觉得你帅得要命。"
    else:
        s "[player_name]？"
        j "嗯？"
        scene c015_s005_055 with Dissolve(0.25)
        s "我知道这可能不该由我来说，也许又该由我来说，因为我们现在经常做爱，但你该别再说自己坏话了。别再说自己不够性感。我觉得你帅得要命。"
    j "还是说只是帅到{b}够{/b}被操的程度？"
    scene c015_s005_056 with Dissolve(0.25)
    s "比那强多了，你这个书呆子。我以前从没离过婚——也没经历过任何长期承诺的关系——所以我不知道自信被那样打击是什么滋味。但我相当确定，她对你做的事，问题不在你身上。"
    j "你怎么能这么确定？也许她找到了更好的人。"
    scene c015_s005_057 with Dissolve(0.25)
    s "我他妈才不信。"
    "{color=#8bc7ff}因为如果我以为自己能爱上一个人，我就绝不会放你走。{/color}"
    scene blank with Dissolve(2)
    scene c015_s005_058 with Dissolve(2)
    "过了一阵子，我知道欢乐时光结束了，我得回去值班。而雪莉该去床上睡那仅剩的几小时，等屋子里重新热闹起来。"
    j "该把衣服穿回去了。你也该睡一会儿。"
    s "刚才那运动量，我想这不难。"
    scene c015_s005_059 with Dissolve(0.25)
    s "我……我能留在这儿吗？睡沙发上？我只是……想靠近你一点，这样有安全感。我知道很傻，但是……"
    scene c015_s005_060 with Dissolve(0.25)
    j "没关系的，雪莉。如果你在有我在旁边的情况下能睡着。我会尽量安静。"
    s "谢谢。我……就是，谢谢。"
    jump shelley_achievement_check
label ch16_shelley_sex:
    $ persistent.ch16_shelley_sex = True
    scene c016_s005_021 with Dissolve(0.5)
    "我们站了一会儿，雪莉的双臂环着我的胸口。我能感觉到她的乳房贴在我背上，但努力压下那些不断试图让我专注于「正抱着我的那个大学女生」的性念头。"
    "我提醒自己，她之所以在这儿，是因为害怕，需要一个具体的东西来安抚自己。"
    scene c016_s005_022 with Dissolve(0.25)
    s "[player_name]？"
    j "你好点了吗？"
    s "嗯。我……"
    scene c016_s005_023 with Dissolve(0.25)
    "雪莉靠过来，在我脸颊上亲了一下。感觉是件纯粹简单的事。几乎有点天真又贴心。我得承认，我的心跳快了一点。"
    scene c016_s005_024 with Dissolve(0.25)
    s "我能说服你做件事吗？"
    j "哦，这就是你叫我来的目的？*轻笑*"
    stop music fadeout 2.0
    scene c016_s005_025 with Dissolve(0.5)
    s "也许这样贴着你对我确实有影响。我看得出来你那边也不反感。*咯咯笑*"
    j "你在我胯上蹭来蹭去也不赖。"
    s "很好。转这边。求你了。"
    play voice_loop kiss
    scene c016_s005_026 with flashpink
    play music shelleytheme fadein 2.0
    s "啾噜噗~~~ 唔嗯~~~"
    "雪莉切换频道的速度有点好笑。前一分钟她还害怕、只想要被安抚，下一分钟我们就在接吻、互相磨蹭。不过我不该指望这会超出接吻的范围。又或者，也许我们不该这样。"
    scene c016_s005_027 with Dissolve(0.5)
    s "啾噜噗噗噗~~~~ 唔唔~~~"
    "但她越是往我身上贴，「负责任」的念头就越输给了想跟她亲近的欲望。我喜欢雪莉。她也喜欢我。为什么我们不能找点乐子呢？"
    stop voice_loop
    scene c016_s005_028 with Dissolve(0.25)
    s "你知道我想要什么，对吧？"
    j "我有个主意。也许我们不该。"
    scene c016_s005_029 with Dissolve(0.5)
    s "不该？得了吧。他好像巴不得在我里面。那会让我很开心。哦~~~开心死了。"
    j "而那才是重要的，对吧？*轻笑*"
    scene c016_s005_030 with Dissolve(0.25)
    s "你喜欢让我开心。我喜欢让你开心。所以这对两个人都是最好的结果。"
    "她在拉我的裤链。如果我要叫停，现在就是时候。"
    scene c016_s005_031 with Dissolve(0.25)
    "当她的手伸进我牛仔裤里的时候。我没有叫停，而是说——"
    j "小心。里面没多少空间。"
    scene c016_s005_032 with Dissolve(0.25)
    s "我看得出来。*咯咯笑* 真不知道你天天怎么把他塞进去。"
    j "他又不是一直那么大。而且我又不像往塑料袋里塞杂货那样把他塞进去。"
    "到这时，我一只手已经罩住了她的奶子，而她正慢慢撸着我。"
    scene c016_s005_033 with Dissolve(0.5)
    s "所以，这是啊啊啊~~~ 只给我的？"
    j "我想是吧。你——"
    play voice_loop kiss
    scene c016_s005_034 with flashpink
    "没等我问这是不是她真的想继续下去的事，她又一次吻了我。她抓紧我，抱得更紧了。"
    s "啾噜噗噗~~~ 咝咝~~~~"
    scene c016_s005_035 with Dissolve(0.5)
    if ch16_laura_sex == "yes":
        "就在那时，我快速算了一下。我们有几个小时。之前跟劳拉搞过一轮，我比平时持久。所以多一个小时左右会有帮助。"
        "而且，我彻底清醒了，如果雪莉想用从现在到天亮这段时间找点乐子，我也乐意。因为说实话，我越来越难抵抗她了。"
    else:
        "就在那时，我快速算了一下。我们有几个小时。我彻底清醒了，如果雪莉想用接下来这几个小时找点乐子，我也乐意。因为说实话，我越来越难抵抗她了。"
    s "唔嗯~~~ 唔唔~~~"
    stop voice_loop
    scene c016_s005_036 with Dissolve(0.25)
    s "早该如此了。*咯咯笑* 不知道为什么，你在抗拒这件事。"
    j "我在想大家很快就要起来了，不知道我们能不能挤得出这个时间。及时地。"
    s "那就快点吧。"
    play voice_loop kiss
    scene c016_s005_037 with flashpink
    "在她再次吻我之前，她用力拽了一下我牛仔裤的腰头，裤子从我胯上滑了下来。但没掉到地上，而是堆在了我膝盖周围。我得把它们迈出来，但鸡巴正压在她肚子上，所以这暂时不在我关心的优先事项里。"
    s "唔唔~~~ 啾噜噗~~~"
    stop voice_loop
    scene c016_s005_038 with Dissolve(0.25)
    s "*咯咯笑* 好了，从里面挣出来。我帮你把衬衫脱了。因为我要在外面光着，你就最好也是。"
    j "对啊，可你性感又好看。"
    scene c016_s005_039 with Dissolve(0.25)
    s "哦，别来这套。不然我就把这件衬衫缠到你头上。"
    scene c016_s005_040 with Dissolve(0.25)
    j "这算是威胁？"
    s "我现在只有这个。因为我不想伤到你。我喜欢你。"
    scene c016_s005_067 with Dissolve(0.5)
    s "我也是。我真的很喜欢你。而且我不想伤到你，哪怕只是玩闹。也不想因为你什么事上犯犟就伤到你。"
    scene c016_s005_068 with Dissolve(0.25)
    s "听着，现在不是谈这个的时候。天哪，我不想破坏气氛，但不久之后我们得谈谈你试图去说服所有人别像她那样想这件事。明白吗？"
    j "好。"
    scene c016_s005_069 with Dissolve(0.25)
    s "而且我真的很想要你。因为我觉得你性感，而且我对你怀有愧意。所以，我们能……？"
    j "对。我还有兴致。"
    scene c016_s005_041 with Dissolve(0.5)
    s "很好。现在，挪到这边来，开始吧。"
    scene c016_s005_042 with Dissolve(0.25)
    j "要给这张沙发开光吗？"
    s "我们在这儿待不了那么久，不成问题的。*咯咯笑*"
    scene c016_s005_043 with Dissolve(0.25)
    j "这么一想，那我是不是该先弄湿弄透。*轻笑*"
    scene c016_s005_044 with Dissolve(0.25)
    s "听起来我有福了。"
    j "你会的。"
    scene c016_s005_045 with Dissolve(0.5)
    s "你知道你不必这么做，对吧？我可没有在计较我们有没有前戏。主要是因为你太会操了，我不需要任何赛前准备。"
    j "知道就好，但我这么做是因为我愿意。而且也许我想让你知道，我喜欢你。"
    scene c016_s005_046 with Dissolve(0.25)
    s "好吧，但如果我开始叫得很大声——"
    j "你一直都很大声，姑娘。我觉得现在所有人都知道了。"
    play voice_loop shelley_slow
    scene c016_s005_047 with Dissolve(0.25)
    s "唔唔~~~ 哦哦~~~ 哦对"
    scene c016_s005_048 with Dissolve(0.5)
    show shelley_ch16_oral with Dissolve(0.25)
    s "唔嗯~~~ 哦操啊啊啊~~~"
    "这段关系——如果我们真能这么叫的话——有些东西我好像还在慢慢消化。"
    s "啊嗯~~~ 哦靠啊啊啊~~~"
    "雪莉不是那种会故作矜持的人。她想要什么就要什么，喜欢什么就喜欢什么。这种坦率的存在方式让人耳目一新，哪怕它感觉非常「只顾当下」。"
    s "唔唔~~~ 哦呜呜~~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c016_s005_049 with Dissolve(0.5)
    show shelley_ch16_oral2 with Dissolve(0.25)
    hide shelley_ch16_oral
    s "唔唔~~~ 哦天哪你啊啊啊~~~"
    "一段完全活在当下的关系能行得通吗？又或者，等我变得无聊又令她厌倦之后，她会不会被新的闪亮东西吸引走？我以前已经经历过一次类似的事了。"
    s "唔唔~~~ 唔唔~~~ 就那里啊啊啊~~~~"
    s "那里哦哦~~~ 哦等等啊啊啊~~~"
    "这个念头让我有点刺痛。并不是说雪莉和南希是同一个人，而是我害怕如果我们走得太远，我最后又会落到同样的地方。"
    s "等等等等啊啊啊~~~"
    stop voice_loop
    scene c016_s005_050 with Dissolve(0.25)
    hide shelley_ch16_oral2
    s "嘿、嘿啊啊啊~~~"
    j "有问题吗？"
    s "上来操我。在我把你满脸都射满之前。"
    #scene c016_s005_051
    scene c016_s005_052 with Dissolve(0.25)
    j "那是坏事吗？"
    s "一般情况下不是，但今晚不是。我需要那根大肉棒在我体内。"
    scene c016_s005_053 with Dissolve(0.5)
    j "也许等我们有更多时间好好享受的时候？"
    s "你他妈最好相信会有。"
    play voice_loop shelley_slow
    scene c016_s005_054 with Dissolve(0.25)
    s "哈啊~~~ 哦哦~~~ 推进去。"
    j "在推了。对一个湿得一塌糊涂的人来说，你有点紧。"
    scene c016_s005_055 with vpunch_soft
    s "哦呜~~~ 哦哦~~~ 啊啊啊~~~"
    "大概是角度的问题。她背靠着沙发、胯部抬起，这跟男上位、女上位或者后入都不一样。"
    scene c016_s005_056 with hpunch
    s "哦呜~~~ 唔唔~~~"
    "最后，我深深地滑了进去。"
    scene c016_s005_057 with Dissolve(0.25)
    show shelley_ch16_fuck with Dissolve(0.25)
    s "哈啊~~~ 哈啊~~~ 啊啊啊~~~"
    "我们开始动起来，我能听见沙发在吱呀作响。声音不大，但考虑到这栋房子——以及这片社区——安静得死寂，那就很显眼了。"
    s "哦靠，我啊啊啊~~~~ 操，我太需要你了唔唔~~~"
    s "我太需要你给我这个了啊啊啊~~~"
    j "很高兴能让你满意唔唔~~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c016_s005_058 with Dissolve(0.5)
    show shelley_ch16_fuck2 with Dissolve(0.25)
    hide shelley_ch16_fuck
    s "哦对，就这样啊啊啊~~~"
    "雪莉把手肘撑在沙发靠背上方，把胯抬起来，这样我更容易狠干她。"
    s "啊啊啊~~~ 哈啊啊~~~~ 哦呜啊啊啊~~~"
    j "哦对啊啊啊~~~ 就这样。"
    s "唔唔~~~ 唔唔~~~ 天哪，再狠点操我"
    j "来，让我唔唔~~~"
    stop voice_loop
    play voice_loop shelley_fast
    scene c016_s005_059 with Dissolve(0.5)
    show shelley_ch16_fuck3 with Dissolve(0.25)
    hide shelley_ch16_fuck2
    "我把她的腿抬了起来，就在她手臂下滑落的瞬间，这个动作让她重重地坐到了我的鸡巴上，惹出一声尖锐的惊叫。"
    s "哦哦哦~~~ 哦靠，啊啊啊~~~"
    "出于本能，我把这理解成「狠狠干她」，于是照做了。"
    s "哦呜~~~ 哦呜呜~~~ 唔唔~~~~"
    s "哦靠哦靠啊啊啊~~~"
    s "唔唔~~~"
    "最后那声听起来像低吼。这也更激励了我。"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c016_s005_060 with Dissolve(0.5)
    show shelley_ch16_fuck4 with Dissolve(0.25)
    hide shelley_ch16_fuck3
    "我双手撑在沙发上，就这么干了起来。我们俩都在奔着一个一塌糊涂的高潮去。"
    s "啊啊啊~~~ 哈啊啊~~~~"
    j "对，要射了啊啊啊~~~ 马上要射了"
    s "操啊啊啊~~~~ 射吧啊啊啊~~~"
    stop voice_loop
    play voice_loop shelley_cum
    scene c016_s005_061 with vpunch
    hide shelley_ch16_fuck4
    pause 0.3
    scene c016_s005_061 with vpunch
    pause 0.3
    scene c016_s005_062 with vpunch
    pause 0.3
    scene c016_s005_062 with vpunch
    pause 0.3
    scene c016_s005_063 with vpunch
    stop voice_loop
    "没等我说什么，她也跟着去了。"
    scene c016_s005_064 with flash
    play sound male_cum
    pause 0.5
    scene c016_s005_064 with flash
    j "啊嗯~~~ 咝咝咝~~~~ *喘气*"
    scene c016_s005_065 with Dissolve(0.5)
    s "哦操…… *喘气* *喘气*"
    j "对。完事后我得来点咖啡，再洗个澡。*轻笑*"
    scene c016_s005_066 with Dissolve(0.5)
    s "什么？你是说你后悔了？"
    j "一点也不。*喘气* 不过，也许今晚等我累瘫的时候就不一定了。"
    $ renpy.end_replay()
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c016_s005_070 with Dissolve(2)
    play music nightmain2 fadein 2.0
    "我们在沙发上沉默地坐了一会儿。我努力不让自己打瞌睡。我还在值班，而且我很清楚，第一个醒来的人要是发现我光着身子跟雪莉在一起，那场面肯定「顺利」得不得了。"
    scene c016_s005_071 with Dissolve(0.5)
    "想到这一点，我起身去收拾衣服。当然，这既不浪漫，也不是你想给这一夜收尾的方式，但保持活动能让我不去幻想「我可以跟她依偎在一起，假装几小时后我们不用上路」。"
    scene c016_s005_072 with Dissolve(0.5)
    s "[player_name]？我们会没事吗？"
    j "会啊。怎么会没事？"
    scene c016_s005_073 with Dissolve(0.5)
    s "不知道。我想我只是情绪上有点多余。看见梅茜之类的。而且……"
    scene c016_s005_074 with Dissolve(0.5)
    s "我有一种不祥的预感，好像要发生什么事，而我不喜欢这种感觉。也许是因为已经发生了这么多破事。我猜我一直在等下一件糟糕的事冒出来。到头来，它会伤害我们其中一个。或者更糟。"
    "我不能怪雪莉有这种感觉。这件事我自己已经挣扎了天知道多久。但我不能让她一直纠结在上面。要是让她心里腐烂发酵，她会走进糟糕的地方去。"
    scene c016_s005_075 with Dissolve(0.5)
    j "那你怎么不信我和伊芙、还有劳拉能处理好这些事，好吗？我们会竭尽全力，确保我们所有人都能活着出去。"
    s "「我们所有人」？"
    scene c016_s005_076 with Dissolve(0.5)
    j "对。这非常明确地包括你。"
    "我不知道这有没有让她安心。她的表情有一瞬间读不出来。我决定不再继续这个话题，是时候把她送回卧室，让她趁屋子喧闹起来之前睡那么一小会儿。"
    scene c016_s005_077 with Dissolve(0.25)
    j "你该回床上去了。离我们得起床出发还有几个小时。今天会很长。"
    s "*叹气* 大概吧。我能留在这儿跟你一起吗？"
    if ch15_shelley_stay == "yes":
        j "快成习惯了，但好吧。只要你不介意我在这儿，而且我不会吵到你。"
    else:
        j "只要你不介意我在这儿，而且我不会吵到你，当然行。"
    scene c016_s005_078 with Dissolve(0.25)
    s "重点就是这个，[player_name]。知道你在附近让我好受些。像个安全毯。"
    j "对。我懂。"
    scene blank with Dissolve(2)
    scene c016_s005_019 with Dissolve(2)
    "雪莉找了个借口，装作我们什么都没做过，重新穿上睡衣，爬回沙发上，花了几分钟才找到一个勉强舒服的姿势。有那么一会儿，我怀疑她是把睡衣打包带过来了，还是只是从卧室的抽屉里翻出来穿上。"
    scene c016_s005_020 with Dissolve(1)
    "其实无所谓。几分钟后，我听见她的呼吸声，知道她又睡着了。"
    jump shelley_achievement_check
label ch17_shelley_sex:
    $ persistent.ch17_shelley_sex = True
    scene c017_s006_001 with Dissolve(1)
    "某个时候，我的体力开始下滑，于是决定靠在泳池边上喘口气。游泳很好玩，能让我们暂时不去想外面发生的事，但我身体还不舒服，需要保存体力。"
    "我都忘了，就算泳池这么大，游上几圈也能消耗多少体力。雪莉抓住了这个机会朝我蹚水过来，眼里闪着调皮的光，宣告她又要搞事了。"
    s "嘿，那边~~~ *咯咯笑*"
    scene c017_s006_002 with Dissolve(0.25)
    j "雪莉。看来这是你的主意。"
    s "得让这姑娘走出壳来，哪怕我得拿锤子帮她敲。我试探性提了句「裸泳」，但最后我们只是穿着内衣游泳，省得花几个小时找泳装。"
    scene c017_s006_002-1 with Dissolve(0.25)
    j "不过我还是挺享受的。"
    s "是吗？要不你展示给我看？*咯咯笑*"
    stop music fadeout 2.0
    play voice_loop kiss
    scene c017_s006_003 with flashpink
    play music shelleytheme fadein 2.0
    "我已经学会了，雪莉说这种话时，多半是在预警——她准备扑过来跟我亲热。这一次，是她的手搭在我头和肩上，舌头滑进我的嘴里，乳房压着我。"
    s "啾噜噗~~~ 唔唔~~~"
    scene c017_s006_004 with Dissolve(0.25)
    k "哦？*咯咯笑* 好吧~~~"
    s "啾噜噗噗~~~ 啾噜噗噗~~~"
    "雪莉把她湿热的身体在我身上磨蹭，让我很难想别的事情。"
    scene c017_s006_005 with Dissolve(0.5)
    "我好像听见了水花声，很轻很远，但我当时太专注于那个像是好几周没见似地跟我啃咬的大学生女生了。而且我硬得厉害，紧贴身的内裤被顶出了一个明显的帐篷。"
    s "啾噜噗噗噗~~~~ 唔嗯~~~"
    stop voice_loop
    scene c017_s006_006 with Dissolve(0.25)
    s "*咯咯笑* 所以，你是不是在想我在想的事？"
    j "也许吧。要不你给我说清楚点？"
    s "你。我。你的房间。光着身子，还有很多很多做爱。在我们需要吃饭之前，我不想出房间。"
    j "懂了。"
    scene c017_s006_007 with Dissolve(0.25)
    k "我得回房间了。我觉得我已经游够了。"
    if ch14_shelleytellskallie == "yes" and kallie_lover == "no":
        "卡莉的话里没有一丝恶意。她是在试着体谅人。在听了我前任多年被动攻击式的屁话之后，这种感觉耳目一新。而且考虑到我们刚才的谈话，我猜这里面也带着一点情感上的自我保护。"
    else:
        "卡莉的话里没有一丝恶意。她是在试着体谅人。在听了我前任多年被动攻击式的屁话之后，这种感觉耳目一新。"
    s "靠。嘿。等等。我们刚才在——"
    scene c017_s006_008 with Dissolve(0.25)
    k "没关系的。我打算给你们俩一点独处的时间、一点空间。我们谁都很久没有过了。"
    s "不，姑娘。对不起，我们不是想让你不舒服。我保证。"
    scene c017_s006_009 with Dissolve(0.25)
    "这时雪莉蹚水走向台阶，一边向卡莉解释自己。"
    k "你们俩没事的，雪莉。真的。"
    scene c017_s006_010 with Dissolve(0.25)
    if ch14_shelleytellskallie == "yes" and kallie_lover == "no":
        ###if kallie no longer
        "要不是我自己正顶着一根吓人的鸡巴、还在碰碰是不是得自己处理掉，我本来会对雪莉对她这段新友谊的用心而感到敭敭。"
        "卡莉已经很多年没有过支持网络了，而现在她身边有个女人，不希望她因为我们刚结束自己那场短暂风流没多久就又亲热起来而不高兴。"
    else:
        "要不是我自己正顶着一根吓人的鸡巴、还在琢磨是不是得自己处理掉，我本来会为雪莉对她这段新友谊的用心而感到佩服。"
        "卡莉已经很多年没有过支持网络了，而现在她身边有个女人，不希望她因为一场突如其来的亲热而心里不痛快。"
    scene c017_s006_011 with Dissolve(0.5)
    s "嘿，我不是想让你难堪。我真的只是……我猜我让自己有点上头了。你知道我的德行，而他浑身湿淋淋的、性感得要命，我根本控制不住自己。我该更好地不让那些最坏的冲动接管我，我真的很努力在改了，但是——"
    k "雪莉——"
    scene c017_s006_012 with Dissolve(0.25)
    k "我是认真的。我对此完全没意见。我本来就打算出来了。所以，请别为这个心里过不去。别因为我。"
    scene c017_s006_013 with Dissolve(0.5)
    s "但我在努力变得更好。当个更好的朋友，不再干那种让别人尴尬的蠢事。而刚才我任由自己又退回了坏习惯。"
    k "如果你真的喜欢他，这就不算坏习惯，姑娘。你喜欢他，对吧？"
    scene c017_s006_014 with Dissolve(0.25)
    if ch14_shelleytellskallie == "yes":
        s "你知道我喜欢。我已经跟你说过了。"
    else:
        s "喜欢。我也已经跟他说过了。"

    k "就算你没说，这也很明显。去玩吧。你们俩都值得。我没事。正好我可以安静待一会儿。我没事，我发誓。"
    scene c017_s006_015 with Dissolve(0.25)
    s "好——吧。如果你觉得没问题的话。"
    k "我没问题。别那么担心。"
    j "雪莉？我们在这儿的事完了吗？"
    scene c017_s006_016 with Dissolve(0.5)
    s "抱歉，[player_name]，我只是觉得她需要有人照应，而且我不想让我们就在那儿亲热，让她觉得尴尬。"
    j "我懂，真的懂。如果你想今天就到这儿回去，我也理解。反正我们又不是半裸着准备做爱什么的。"
    scene c017_s006_017 with Dissolve(0.25)
    s "哦不不不。我们要做。既然她都给我们腾地方、给许可了，我想被操。被你操。"
    j "这节奏转得可真快。"
    scene c017_s006_018 with Dissolve(0.25)
    s "哦，我可没停止想要你。*咯咯笑* 我完全可以一边照顾我朋友，一边兴奋着。"
    j "你就是这么复杂。*轻笑*"
    scene c017_s006_019 with Dissolve(0.25)
    s "哦，你还不知道呢。一个女人脑子里可以同时装着大概十六个不同的念头，而那就是一场「看哪个先到嘴边」的战争。"
    j "不过我很高兴，那些有趣和色情的念头在你那儿享有优先排队权。"
    scene c017_s006_020 with Dissolve(0.25)
    s "我就知道。*咯咯笑*"
    "她是在故意撅屁股吗？我觉得是。感觉像是在求我从后面要她。我不该浪费这个机会。"
    scene c017_s006_021 with Dissolve(0.25)
    s "哇~~~ 嘿~~~ *咯咯笑*"
    j "我猜这就是你想要的。男人不总是擅长读懂暗示，所以——"
    scene c017_s006_022 with Dissolve(0.5)
    s "老兄，我说了我想做爱。所以你「可能」做的事里，我没想要的真的非常少。别想太多了。我喜欢你，而且从你现在这根硬东西来看，我看得出来我们俩都想来点野的。"
    j "抱歉，有时候我实在忍不住。"
    scene c017_s006_023 with Dissolve(0.5)
    s "我懂。不是每个人都能对每个冲上来就照做的。但趁现在只有我们俩，把这事办了吧。天哪，希望劳拉别这时候上来。"
    j "那可就倒霉了。你想挪到躺椅上去吗？"
    s "直接来啊，老兄。"
    scene c017_s006_024 with Dissolve(0.25)
    j "哦，不要浪漫？不要慢慢累积激情的铺垫？不要前戏？"
    s "就这一次？对。我们下次用你那套蠢浪漫的方式。我只想被狠狠干，被你干。"
    play voice_loop shelley_slow
    scene c017_s006_025 with hpunch
    j "你说了算。"
    s "啊啊啊~~~ 操~~~ 唔唔~~~"
    "我滑进去的时候她抖了一下。尽管她刚才那么主动，我觉得她其实没准备好接住我。"
    scene c017_s006_026 with Dissolve(0.25)
    s "哦哦~~~ 靠咝~~~ 啊啊啊~~~"
    "抽插了几下之后，我就深深埋在她体内，她的屁股瓣压着我的腰。"
    scene c017_s006_027 with Dissolve(0.5)
    show shelley_ch17_fuck with Dissolve(0.25)
    s "啊啊啊~~~ 哈啊~~~ 操我啊啊啊~~~~"
    "我抓住她的手臂，把它们往后拉，同时她在我身上弹跳起伏，带着我的长度，发出像是等太久了似的哼哼唧唧。"
    s "唔唔~~ 哦呜呜~"
    s "操~~~ 唔唔~~~"
    "卡莉走了真是件好事。我敢肯定她不想看这场注定又吵又汗的结合。"
    j "嘿，嘿，转过来。"
    stop voice_loop
    play voice_loop shelley_med
    scene c017_s006_028 with Dissolve(0.5)
    hide shelley_ch17_fuck
    s "好吧，什么啊啊啊~~~ 哦靠对。"
    scene c017_s006_029 with Dissolve(0.5)
    show shelley_ch17_fuck2 with Dissolve(0.25)
    "我抓住她的奶子，开始真的狠干她。享受着这种关注，雪莉开始大声嚎叫起来。"
    s "哈啊啊啊~~~~ 哦天哪啊啊啊~~~"
    "她想抓住我的手，但挣扎着够不到。我对此很满意。这才是我真正给她想要的。"
    j "唔唔~~~ 哈啊~~~ 对"
    s "操啊啊啊~~~~ 靠对啊啊啊~~~"
    "有一瞬间，一个问题冒进我脑子：我们是第一批在这儿做爱的人吗？这看起来是个跟某人独处的绝佳地点。但我怀疑人们不会在这么公开的地方干这事（就算你是会员也一样）。"
    s "哈啊啊啊~~~ 啊啊啊~~~~"
    stop voice_loop
    scene blank with Dissolve(2)
    scene c017_s006_030 with Dissolve(2)
    play voice_loop shelley_fast
    show shelley_ch17_fuck3 with Dissolve(0.25)
    hide shelley_ch17_fuck2
    "我们只慢下来跪到地上。瓷砖地板并不舒服，但我们俩似乎都不在乎。雪莉想要我，我也想要她。"
    s "哈啊~~~ 天哪，你操得真好"
    j "对这么性感的女人来说很容易唔唔~~~"
    s "哦哦哦~~~ [player_name]，啊啊啊~~~"
    if ch16_shelley_sex == "yes" or ch15_shelley_sex  == "yes":
        "至少这次我们不是在做沙发上。"
    s "哦哦哦~~~ 哦呜呜呜~~~"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c017_s006_031 with Dissolve(0.5)
    show shelley_ch17_fuck4 with Dissolve(0.25)
    hide shelley_ch17_fuck3
    "我们快到的时候，她的一条手臂滑了一下，手掌啪地拍在地上。我抓住另一只的手，锁住了她的手腕。我们干得这么狠，谁都不想结束。"
    s "啊啊啊~~~ 啊啊啊~~~"
    j "操，快了啊啊啊~~~"
    s "我也是~~~ 哦天哪我好想要"
    s "加油加油啊啊啊~~~~"
    j "哦靠，姑娘~~~"
    s "啊啊啊~~~" with vpunch_soft
    s "唔唔~~~ 哦啊啊啊~~~~"
    stop voice_loop
    play voice_loop shelley_cum
    scene c017_s006_032 with vpunch
    hide shelley_ch17_fuck4
    pause 0.3
    scene c017_s006_033 with vpunch
    pause 0.3
    scene c017_s006_034 with vpunch
    pause 0.3
    scene c017_s006_033 with vpunch
    pause 0.3
    scene c017_s006_035 with vpunch
    stop voice_loop
    s "哦靠，刚才那是 *喘气*"
    j "要射了~~~"
    scene c017_s006_036 with flash
    play sound male_cum
    pause 0.5
    scene c017_s006_036 with flash
    pause 0.5
    scene c017_s006_037 with Dissolve(0.5)
    j "啊嗯~~~ 靠，啊啊啊~~~ 啊啊啊……"
    s "靠，好多。刚才一直憋着不给？*咯咯笑*"
    scene c017_s006_038 with Dissolve(0.5)
    j "也许我从你这儿就只能榨出这么多。*喘气*"
    s "*咯咯笑* 好吧，我可是你的性感小玩物，对吧？"
    $ renpy.end_replay()
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c017_s006_039 with Dissolve(2)
    play music insideday fadein 2.0
    "喘着粗气、拿刚才的性爱表现互相打趣了几分钟之后，雪莉和我坐在池边，双腿垂在水里。她出奇地安静，依偎在我身边，仿佛这次终于心满意足了。"
    scene c017_s006_040 with Dissolve(0.5)
    "我太习惯她话多、脑子里一个念头都不停的样子了，所以我好奇她是真的一下子平静放松了，还是仍在消化过去一周发生的所有事。"
    j "你还好吗？"
    scene c017_s006_041 with Dissolve(0.25)
    s "头一回？对。我做梦都想不到自己会在这种处境里。"
    j "一家跟以前的陌生人乱搞在一起的酒店套房，大家一起躲着毒雾和怪物别死掉？我觉得这进不了前十。"
    scene c017_s006_042 with Dissolve(0.25)
    s "那当然不用说了。但还有另一件事。或者，另外几件事。跟一个成熟男人牵扯上。还有在我生命里有一个我真心当作朋友的人。"
    "我本可以把话题往她对我们关系的感受上引，但觉得那大概可以留到以后。等它从两个人玩乐变成某种更恒久的东西时，如果那有可能的话。相反，我把注意力放在她那句话的后半截。"
    scene c017_s006_043 with Dissolve(0.25)
    j "这真的是你第一次吗？拥有一个你视为朋友的人？我本来会押大钱说你身边总是有人围着转。"
    s "在中学的时候，女孩儿们像走马灯一样换了个遍，最后她们都会厌倦我一天到晚兴奋过头、精力过剩。而且直到高三上学期我才把药吃稳，所以并不是一直那么好相处。而且说实话，十几岁的少年彼此都很混蛋，哪怕在最好的时候。"
    scene c017_s006_044 with Dissolve(0.25)
    j "这个我没法反驳。"
    s "上了大学之后，我信了那套「探索阶段」的屁话，而那也不太容易让人留在身边。当你在品尝人生自助餐时，你不会把盘子堆满同一样东西。"
    scene c017_s006_045 with Dissolve(0.25)
    j "这比喻真够狠的。*轻笑* 而且，吃东西跟维持关系可不是一回事。"
    s "随便吧。"
    if ch12_kallie_sex == "yes" or ch13_kallie_sex == "yes" or ch14_kallie_sex == "yes":
        scene c017_s006_046 with Dissolve(0.25)
        ###if Kallie ended it
        s "听着，我在尽量不让事情对她变难。我很在乎她，觉得自己在她身边必须小心。今天我可能稍微放松了警惕。因为你们俩之前……"
        j "因为我们之前有过亲密接触？而我对她太蠢了。"
        scene c017_s006_047 with Dissolve(0.25)
        s "差不多。她说她不介意我们，我只能相信她。不过我尽量不拿这事去戳她。"
        j "我懂，真的懂。她和我现在的状态还不错，我们也互相关心，但肉体那部分已经结束了。"
        scene c017_s006_048 with Dissolve(0.25)
        s "所以我赚到了？*咯咯笑*"
        j "当然。"
    else:
        scene c017_s006_047 with Dissolve(0.25)
        s "我尽量了。至于卡莉……她是个非常好的人，也一直在努力对我。她见过我被抑郁症折腾的样子，而我……我看得出她也在打自己的仗。我不喜欢让她一个人待着，哪怕我知道安静独处是她需要的东西之一。那是她的应对方式。"
        j "她是个爱思考的人。"
    scene c017_s006_049 with Dissolve(0.5)
    s "答应我，等我们出去之后，别让她回到安德鲁身边。"
    j "这就是计划。劳拉或者我，会把她送上飞回家的飞机。"
    scene c017_s006_050 with Dissolve(0.25)
    s "好。她比我们以为的更坚强，但我觉得安德是唯一她可能挡不住的东西。"
    j "他知道怎么把她击垮。我以前也经历过，知道那种感觉。"
    scene c017_s006_051 with Dissolve(0.25)
    s "……"
    "过了一阵子，我们决定该穿好衣服回去了。"
    scene blank with Dissolve(2)
    scene c017_s006_052 with Dissolve(2)
    "下楼的电梯里，雪莉一直靠着我。不止一次，我听见她满足地哼着歌。我看向她时，她微笑着，脸上洋溢着幸福的光。"
    "虽然我不会说我们是在认真交往，但我看得出来我们有可能。我不介意。我很喜欢雪莉。非常喜欢。但就像卡莉一样，我必须考虑到，一旦安全了，我就要把她送回家。"
    jump shelley_achievement_check
label ch18_shelley_sex:
    $ persistent.ch18_shelley_sex = True
    play voice_loop kiss
    scene c018_s002_022 with flashpink
    play music shelleytheme fadein 2.0
    "我不会拒绝她。至少不会在这个阶段。也许我们不会走得更远。就只是摸摸亲亲，然后安定下来。毕竟我们明早很早就得出发。"
    s "啾噜噗~~~ 唔唔~~~"
    scene c018_s002_023 with Dissolve(0.5)
    "我在骗谁呢？当雪莉开始把我的内裤往下拉时，我就知道这不会只是一次深夜的亲热。"
    s "啾噜噗~~~ 唔唔~~~"
    scene c018_s002_024 with Dissolve(0.25)
    stop voice_loop
    j "雪莉？*轻笑*"
    s "那个……哈啊~~~"
    scene c018_s002_025 with Dissolve(0.5)
    j "这就是你那个「爱」字不说出口的变体吗？"
    s "不。至少对别人不会。但对你？也许吧。又或者，我只是想要你，因为你想要我的时候会让我开心。让我心里暖暖的。"
    scene c018_s002_026 with Dissolve(0.5)
    j "嗯，我整个人生目标就是让你开心。"
    s "很好，因为我想要的就是这个。对我们俩都是。"
    "她一只手握着我的鸡巴来回撸动，让我很难想别的事，除了把她扒光、好好疼爱她之外。不过……"
    scene c018_s002_027 with Dissolve(0.5)
    j "嘿，你确定吗？在我们做得太过之前？你当时进来的时候——"
    s "确定。我没骗你。你让我开心，而我就想要你这样。现在一直如此。但今晚，我只是……"
    scene c018_s002_028 with Dissolve(0.25)
    s "我需要感觉到你。也让你感觉到我。"
    j "哦，我们已经在做不少了。"
    scene c018_s002_029 with Dissolve(0.25)
    s "我想要更多。而且我看得出你也一样。"
    j "罪名成立。"
    scene c018_s002_030 with Dissolve(0.25)
    s "你很难藏住。*咯咯笑*"
    j "你把它掏出来的时候可藏不住。来，让我看看你是不是也一样。"
    scene c018_s002_031 with Dissolve(0.25)
    play voice_loop shelley_slow
    j "哦？你下面又湿又热。"
    s "啊啊啊~~~ 哦你他妈对我做了这种事啊啊啊~~~"
    scene c018_s002_032 with Dissolve(0.5)
    show shelley_ch18_finger with Dissolve(0.25)
    j "做了什么？"
    s "哦，操啊啊啊~~~ 你知道的"
    j "我不觉得我知道。"
    s "天哪啊啊啊~~~~ 唔唔~~~ 哦爽死了~~~"
    s "唔唔~~~ 哦呜，就这样啊啊啊~~~"
    j "雪莉？刚才那声是什么？*轻笑*"
    hide shelley_ch18_finger
    scene c018_s002_033 with Dissolve(0.25)
    s "哦靠，你知道那是什么啊啊啊~~~ 过来，你这个猛男。"
    "她扭过身来，伸手扶住我的肩膀。"
    stop voice_loop
    scene c018_s002_034 with vpunch
    j "哇！"
    s "来，现在。"
    scene c018_s002_035 with Dissolve(0.5)
    j "有点凶了啊，不是吗？"
    s "别再扭捏了。请把他放进我里面。"
    j "不用问第二次。"
    play voice_loop shelley_slow
    scene c018_s002_036 with hpunch
    s "哦哦~~~ 天哪啊啊啊~~"
    scene c018_s002_037 with hpunch
    "虽然我有一部分想深入探索这段我们一直跳着回避的、接近「我爱你」的关系，但我核心想做爱的需求占了上风。"
    s "啊嗯~~~ 哦呜呜~~~"
    scene c018_s002_038 with Dissolve(0.25)
    j "到了啊啊啊~~~"
    s "靠，我需要你。"
    j "我在这儿。"
    scene c018_s002_039 with Dissolve(0.5)
    show shelley_ch18_fuck with Dissolve(0.25)
    "我们的手交扣在一起，我开始抽插。雪莉快乐地呻吟回应。"
    s "哦哦哦~~~ 哦呜~~~ 天哪啊啊啊~~~"
    s "哈啊~~~ 就这样"
    s "操我啊啊啊~~~"
    "继续下去时，我注视着她的面容，随着我深深挺入，她的脸因情欲而扭曲。在那底下，是一个我正逐渐对她生出感情的人的柔软脆弱。是爱吗？"
    s "啊啊啊~~~ 哈啊~~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c018_s002_040 with Dissolve(0.5)
    show shelley_ch18_fuck2 with Dissolve(0.25)
    hide shelley_ch18_fuck
    s "啊啊啊~~~ 天哪啊啊啊~~~"
    "到这时，我对她、对我们之间已经有了复杂的感情。诚然一开始这一切只是图方便，但感觉上我们正在朝某种更……实在的东西发展。长期的吗？我不知道。"
    s "啊啊啊~~~ 哈啊啊~~~~"
    "连她自己都承认，雪莉不是一个会依恋别人的。但这一条似乎正一天天不那么坚定了。"
    s "唔唔~~~ 哦靠，啊啊啊~~~"
    scene c018_s002_054 with Dissolve(0.5)
    hide shelley_ch18_fuck2
    s "嘿、嘿啊~~~"
    j "雪莉？"
    scene c018_s002_055 with Dissolve(0.25)
    s "往后靠。我想啊啊啊~~~ 试个东西。"
    j "你永远都愿意干点疯狂的性爱花样，不是吗？"
    scene c018_s002_056 with Dissolve(0.25)
    s "他们出了一本讲姿势的书唔唔~~~ 我想把它们全试一遍*咯咯笑*"
    s "跟你一起试。"
    "这足以说服我答应她的要求。"
    stop voice_loop
    scene blank with Dissolve(2)
    play voice_loop shelley_fast
    scene c018_s002_041 with Dissolve(2)
    show shelley_ch18_fuck3 with Dissolve(0.25)
    "几秒钟后，我们摆成了一个奇怪的、像椒盐卷饼一样的姿势，然后继续。在我脑子里，「雪莉想跟我试一堆东西」这件事，许诺了某种比我之前预期更认真的东西。"
    s "哈啊~~~ 哦天哪啊啊啊~~~"
    s "靠，那啊啊啊~~~"
    s "正正好好命中唔唔~~~"
    "看她身体弹跳的样子，我就知道我正正好顶在她想要的地方。"
    s "啊啊啊~~~ 哈啊~~~"
    stop voice_loop
    scene c018_s002_042 with Dissolve(0.5)
    show shelley_ch18_fuck4 with Dissolve(0.25)
    hide shelley_ch18_fuck3
    play voice_loop shelley_preorgasm
    "对，那个姿势确实古怪，但它让雪莉比只是仰面躺着任我抽插能掌握更多主动权。"
    s "啊啊啊~~~ 哈啊啊~~~"
    j "天哪，姑娘，我要啊啊啊~~~"
    s "射吧。灌进来啊啊啊~~~"
    "我知道我们在无保护性爱上一直玩得很松，但此刻我根本不在想我要不要让她怀孕。"
    s "哦靠咝~~~ 啊啊啊~~~"
    s "唔唔~~~！！" with vpunch_soft
    stop voice_loop
    play voice_loop shelley_cum
    scene c018_s002_043 with hpunch
    hide shelley_ch18_fuck4
    pause 0.25
    scene c018_s002_043 with hpunch
    pause 0.25
    scene c018_s002_044 with hpunch
    pause 0.25
    scene c018_s002_045 with hpunch
    pause 0.25
    scene c018_s002_046 with Dissolve(0.5)
    stop voice_loop
    j "啊啊啊~~~ 对啊啊啊~~~"
    scene c018_s002_047 with flash
    play sound male_cum
    pause 0.5
    scene c018_s002_047 with flash
    pause 0.5
    scene c018_s002_048 with Dissolve(0.5)
    j "靠，刚才那…… *喘气* *喘气* 真火辣。"
    s "哦，你知道啊。*喘气*"
    scene c018_s002_049 with Dissolve(0.5)
    j "这就是你想要的全部吗？"
    s "*咯咯笑* 一直都是。"
    $ renpy.end_replay()
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c018_s002_062 with Dissolve(2)
    play music nightmain fadein 2.0
    "做完之后，我们依偎着。或者更准确地说，是雪莉整个人摊在我身上，我抱着她。她很安静，有那么一会儿，我怀疑她是不是已经睡着了。"
    scene c018_s002_063 with Dissolve(0.25)
    s "[player_name]……"
    j "怎么了，雪莉？"
    s "我想让你知道…… *叹气*"
    scene c018_s002_064 with Dissolve(0.25)
    s "你对我来说很安全——但不是那种蠢女孩一边盯着要跟别的男人上钩的男人一边说的那种「安全」。我很感激我知道你对我永远都会是这样。而且你从不评判我。不管我状态多差。从来不。"
    scene c018_s002_065 with Dissolve(0.25)
    s "抱歉这么晚才来你房间。我知道我们得很早起来出发，但是——"
    j "雪莉，我是认真的：你任何时候需要我，都可以来找我。这一点没有任何改变。"
    s "我知道，但我还是……那场做爱不是因为「忍受我」的某种奖励。我……我真的……"
    scene c018_s002_066 with Dissolve(0.25)
    s "对不起。我只是不想在做爱的时候，或者在我脆弱的时候说出来。好吗？"
    menu:
        "没关系。":
            j "没关系。你没有任何压力非做非说不可。留着它，等你觉得时机合适的时候。"
            scene c018_s002_067 with Dissolve(0.25)
            s "谢谢。"
        "嗯，我爱你。":
            $ s_love += 1
            $ ch18_tellshelleylove = "yes"
            j "嗯，不管怎么说……我爱你。我知道。但我不指望你回应这句话。我只是想把它说出来，这样你就不必害怕当那个先说出口的人、然后被吊在半空。"
            scene c018_s002_068 with Dissolve(0.25)
            s "……"
            j "我爱你，雪莉。"
            scene c018_s002_069 with Dissolve(0.25)
            s "谢谢。我…… *吸鼻子*"
            j "没关系的。"
    scene c018_s002_070 with Dissolve(0.5)
    if kallie_lover == "yes":
        s "那……那你和卡莉呢？我是说，我明白现在有点奇怪的事在发生，但我没那么蠢，会以为你、我和她将来会变成一个三人组合。"
        j "我知道。总有一天我们得做出选择。现在没人会对「谁跟谁在一起」做长期决定。至少今晚不会。"
        scene c018_s002_071 with Dissolve(0.25)
        s "那等我们出去之后呢？如果我们能出去的话。"
        j "等那一天到来的时候。如果我还想把她送到一个我知道她安全的地方。送到她家人那儿。大概我对你也会做同样的事。把你送回那个因为不知道你是否安全而恐怕已经吓坏的家庭。"

    else:
        s "我知道现在想这些太早了，但我们出去之后会怎样？如果能出去的话。你和我呢？"
        j "等那一天到来时，我第一个念头是把你送回家，回到那个因为不知道你死活而害怕的家人身边。"
    scene c018_s002_072 with Dissolve(0.25)
    s "我……对，我……我得见我的家人。但那之后……"
    j "你觉得你家人会让你回来吗？我想你妈妈再也不会让你离开她的视线了。"
    scene c018_s002_073 with Dissolve(0.25)
    s "也许吧。我是个大姑娘了。大体上是。不过我可以让她唠叨一阵子。"
    scene c018_s002_074 with Dissolve(0.25)
    s "但总有一天……"
    j "到时候我们再处理。好吗？我保证。到时候会有时间的，我保证。"
    s "好吧……"
    scene c018_s002_075 with Dissolve(0.5)
    s "[player_name]，我害怕明天，但我保证我会努力撑住自己。"
    j "我知道你会的。待在卡莉或者劳拉身边。等我们找到能休息的地方，我会让你做任何你需要的事来让自己好受点。相信我们其他人就好。"
    s "我……我会的。"
    jump shelley_achievement_check
label ch19_shelley_sex:
    $ persistent.ch19_shelley_sex = True
    play voice_loop kiss
    scene c019_s006_011 with flashpink
    if _in_replay:
        play music shelleytheme fadein 2.0
    $ shelley_lover = "yes"
    "跟雪莉相处的这些日子里，我已经开始习惯她那些突然的冲动。她有些笨拙、有时还有点毛手毛脚，脑子里冒出什么就做什么。但在一段坦白说到一半时，她突然伸手环住我、印下一个热情的吻，还是把我打了个措手不及。"
    s "啾噜噗~~~ 嘘咝噗噗~~~"
    stop voice_loop
    scene c019_s006_059 with Dissolve(0.25)
    j "我大概明白你的意思了。*轻笑*"
    s "是吗？还是说，你感觉到我下面湿得一塌糊涂？"
    j "我现在是有点意识到了，毕竟我的内裤都被你蹭湿了。"
    scene c019_s006_060 with Dissolve(0.25)
    s "我控制不住自己。你没穿内裤、而你现在又硬得要命，这让我啊啊啊~~~"
    j "你不用解释。"
    scene c019_s006_061 with Dissolve(0.25)
    s "我知道，但我就喜欢告诉你，你让我硬了。"
    j "所以，那就是为什么——"
    s "这是原因之一，但不是主要的。不过……"
    scene c019_s006_062 with Dissolve(0.25)
    s "我们能……你懂的？"
    j "好像我能拒绝你似的。"
    scene c019_s006_012 with Dissolve(0.25)
    s "很好。我就知道。*咯咯笑*"
    scene c019_s006_013 with Dissolve(0.25)
    j "我是说，当你把奶子掏出来的时候，我没法拒绝你。"
    s "你现在就已经硬了好吗。"
    scene c019_s006_063 with Dissolve(0.25)
    j "因为你把骚穴亮出来，还坐在我腿上，一副很敏感的样子。"
    s "哦？我柔软又脆弱的样子会让你兴奋？"
    j "主要是那句话里的「你」。不过既然你现在在我这儿……"
    play voice_loop shelley_slow
    scene c019_s006_014 with Dissolve(0.25)
    s "啊啊啊~~~ 靠，好敏感啊啊啊~~~"
    "我舔吸着她乳头时，她发出了一声呻吟。"
    scene c019_s006_015 with Dissolve(0.25)
    s "哦哦哦~~~ 哦呜~~~ 哦啊啊啊~~~"
    "她的呻吟在空荡的走廊里回响，我希望我们离得够远，雪莉一贯的大嗓门不会被人注意到。"
    stop voice_loop
    scene c019_s006_016 with Dissolve(0.25)
    s "我喜欢你这样对我。"
    j "在你想让我做的其他所有事情里？"
    s "对。每一样都喜欢。"
    play voice_loop kiss
    scene c019_s006_017 with flashpink
    "这一次，我的手还抓着她的奶子，感觉到雪莉换了个姿势，凑过来再次吻我。"
    s "啾噜噗~~~ 啾噜噗噗~~~ 唔唔~~~"
    stop voice_loop
    scene c019_s006_018 with Dissolve(0.25)
    s "天哪，我好喜欢吻你。"
    "既然这个词已经说出口了，雪莉就尽情利用它，像是给自己词库里找到了一个新鲜又管用的词。"
    j "我们可以多做点你爱做的事。"
    scene c019_s006_019 with Dissolve(0.25)
    s "这正是计划。来，让我起来，好让你把内裤脱掉。隔着一层棉布把他推进去有点难。"
    j "我很愿意试试。*轻笑*"
    scene c019_s006_020 with Dissolve(0.5)
    s "不了。我可没为了「不跟你肌肤相贴」才把自己塞进这身衣服里的。而且，对，我找到它的时候第一个念头就是你会喜欢，而且我会用它让你操我。"
    j "我开始觉得你越来越能预判我脑子里在想什么了。"
    scene c019_s006_021 with Dissolve(0.25)
    s "所以我才没穿内裤。*咯咯笑*"
    j "真的？那是为了我，而不是部分为了你自己？你身上有暴露狂的潜质。"
    scene c019_s006_022 with Dissolve(0.25)
    s "如果你懂我的意思，那我现在真正在意的是「在我体内」这件事。"
    j "这真的一点都不低调。爱你，但低调不是你的强项。"
    s "不过扭着我光着的屁股，直到你整根埋进来，这倒是低调得很。现在——"
    scene c019_s006_023 with Dissolve(0.25)
    j "第一，做一点赛前准备。把屁股撅出来，双腿分开。"
    s "好、好吧。行。"
    "{color=#8bc7ff}靠，他这样命令我，触发了我自己都不知道我喜欢的东西。{/color}"
    play voice_loop shelley_slow
    scene c019_s006_024 with Dissolve(0.5)
    show shelley_ch19_oral with Dissolve(0.25)
    "我把脸埋进她两瓣屁股之间，舌头插进她的骚穴。当我碰到某个敏感的地方时，雪莉发出一声喜悦的尖叫。"
    s "哦操~~~ 对啊啊啊~~~~"
    s "唔唔~~~ 哈啊~~~"
    "她因我攻击她的阴蒂而抽搐。双手用力按在储物柜上，我听见其中一扇门的响声，是她手指伸展开时带动的。"
    s "唔唔~~~ 唔唔~~~ 哦靠老兄"
    s "啊啊啊~~~ 哈啊~~~"
    stop voice_loop
    play voice_loop shelley_fast
    scene c019_s006_025 with Dissolve(0.5)
    show shelley_ch19_oral2 with Dissolve(0.25)
    hide shelley_ch19_oral
    "我把脸尽量往里推，确保舌头能深深滑进她的肉缝里。就在这时，她的双腿开始发软。"
    s "哦靠咝~~~"
    "我在两种冲动之间摇摆：一是想狠狠干到她允许的极限，二是想直接把内裤扯下来就在这儿干她。最后，我觉得自己应该比她平时遇到的那类男朋友强一点。"
    s "唔唔~~~ 哦天哪，[player_name]。"
    s "我……啊啊啊~~~ 我……"
    stop voice_loop
    scene c019_s006_026 with Dissolve(0.5)
    hide shelley_ch19_oral2
    s "[player_name]？[player_name]，求你了~~~ 我好喜欢……而且……而且……"
    scene c019_s006_027 with Dissolve(0.25)
    s "听着，我可以让你那样做上几个小时，但我现在真的需要你操我。"
    j "这差不多就是我一直想听的话。"
    scene c019_s006_028 with Dissolve(0.5)
    s "怎么样？"
    j "我本来想看看你能撑到什么时候才会求我继续。"
    scene c019_s006_029 with Dissolve(0.25)
    s "要是我射了呢？在我满足自己的时候，我可以很自私。"
    j "继续，直到你变成一滩躺在地板上的自己汁液里哭哭嗒嗒地哀叹。*轻笑*"
    scene c019_s006_030 with Dissolve(0.25)
    s "这画面我喜欢，但今晚不行。"
    j "留到以后约会的计划里吧。"
    scene c019_s006_031 with Dissolve(0.25)
    s "我还是喜欢这个说法。连约会一起。"
    j "我猜我们现在是该像正常人一样真的去吃个饭、看个电影了。"
    play voice_loop shelley_slow
    scene c019_s006_032 with vpunch
    s "啊啊啊~~~ 正常人啊啊啊~~~ 那是什么样子？"
    j "我们得去弄清楚唔唔~~~"
    scene c019_s006_033 with vpunch
    s "唔唔~~~ 哦靠太爽了~~~"
    scene c019_s006_034 with Dissolve(0.25)
    "{color=#8bc7ff}天哪，听他把约会说得像件稀松平常的事，而我只想说「好」。{/color}"
    scene c019_s006_035 with Dissolve(0.5)
    show shelley_ch19_fuck with Dissolve(0.25)
    s "唔唔~~~ 唔唔~~~ 哦靠，啊啊啊~~~"
    j "天哪，你感觉他妈的太爽了。"
    s "操我，你的鸡巴啊啊啊~~~"
    s "操，我需要这个，需要你啊啊啊~~~"
    "不知为什么，储物柜门的响声很分散注意力，那烦人的敲打让我难以专注。"
    scene c019_s006_036 with Dissolve(0.25)
    hide shelley_ch19_fuck
    j "好了，姑娘，我们退回去。"
    s "什么啊~~~~~ 随你怎样"
    scene c019_s006_037 with Dissolve(0.25)
    "从那声音来判断，我开始觉得只要是「我们之间」的事，雪莉大概都会任我去做。当然我也不会把她推得太远。"
    s "哦靠，再多~~~点~~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c019_s006_038 with Dissolve(0.5)
    show shelley_ch19_fuck2 with Dissolve(0.25)
    "当我深深插进她体内时，我努力扶住雪莉不让她倒下。"
    s "操~~~ 哦天哪啊啊啊~~~"
    s "唔唔~~~ 唔唔~~~"
    s "天哪，再多~~~ 再多~~~"
    "尽我所能给你更多。"
    stop voice_loop
    play voice_loop shelley_fast
    scene c019_s006_039 with Dissolve(0.5)
    show shelley_ch19_fuck3 with Dissolve(0.25)
    hide shelley_ch19_fuck2
    "我不愿承认，但今天发生的事和在外面待太久，已经把我累得比我希望的更厉害。也许我该让雪莉来骑我，但我们已经在这个位置了，而我也不会提议停下来喘口气。"
    s "唔唔~~~ 操，就这样啊啊啊~~~"
    s "唔唔~~~ 唔唔~~~ 靠~~~"
    s "哦哦哦~~~ 天哪我爱死了啊啊啊~~~"
    j "我也是唔唔~~~"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c019_s006_040 with Dissolve(0.5)
    show shelley_ch19_fuck4 with Dissolve(0.25)
    hide shelley_ch19_fuck3
    s "天哪，快了啊啊啊~~~ 快了~~~"
    s "太爽了，要射了啊啊啊~~~"
    "很好，因为我正开始没力气，而且一直在忍着不射。"
    s "唔唔~~ 哦靠，啊啊啊~~~"
    s "啊啊啊~~~ 哈啊~~~"
    s "哦操我~~~！！" with vpunch_soft
    stop voice_loop
    play voice_loop shelley_cum
    scene c019_s006_041 with vpunch
    hide shelley_ch19_fuck4
    pause 0.3
    scene c019_s006_042 with vpunch
    pause 0.3
    scene c019_s006_043 with vpunch
    pause 0.3
    scene c019_s006_042 with vpunch
    pause 0.3
    scene c019_s006_044 with Dissolve(0.5)
    stop voice_loop
    "随着力气从她身体里流走，我勉强多抱了一会儿，好让自己也射出来。"
    scene c019_s006_045 with flash
    play sound male_cum
    pause 0.5
    scene c019_s006_045 with flash
    pause 0.5
    scene c019_s006_046 with Dissolve(0.5)
    s "哦靠，那是*喘气*好多。"
    j "说这话的姑娘正滴得一地板都是*喘气*"
    scene c019_s006_047 with Dissolve(0.25)
    s "也有点是你的错。*咯咯笑*"
    j "我把这当成夸奖。*轻笑*"
    $ renpy.end_replay()
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c019_s006_064 with Dissolve(2)
    play music nightmain2 fadein 2.0
    #scene c019_s006_048
    "做爱的余韵消退后，我精疲力竭地瘫回椅子里，塑料椅面冰凉地贴着我光着的屁股。希望这意味着我今晚能睡得又沉又死。雪莉还沉浸在我们刚才的欢爱里，兴奋不已，依偎在我身旁。"
    "虽然她之前说了「我爱你」，但我不想再特意把话题挑回来。我是在给她一个台阶，让她可以假装那一刻其实没发生过。这也没什么好惊讶的。我们朝那个方向已经走了好几周了。"
    scene c019_s006_065 with Dissolve(0.25)
    s "唔嗯~~~ *咯咯笑*"
    j "好吧，那我现在可以说，我操过一个啦啦队员了。"
    scene c019_s006_066 with Dissolve(0.25)
    s "那在你的清单上吗？我知道男人都有一份「这辈子一定要做过」的事。"
    j "在大部分高中男生的清单上。也许还有些女生。"
    scene c019_s006_067 with Dissolve(0.25)
    s "确实。我自己也在上面。不过站在另一边，也确实是个体验。"
    j "听起来你以前并不是——"
    scene c019_s006_068 with Dissolve(0.25)
    s "啦啦队一员？去他的。那需要太多的专注力和执行力，对一个还在摸索该把哪些药组合起来、才能撑过一个月的人来说，太不现实了。"
    scene c019_s006_069 with Dissolve(1)
    "我猜她十几岁的时候有更重要的事要专注。这很合理。激素水平加上化学失衡，已经够折磨人了。"
    "有一阵子我们都没说话。我只能想象雪莉正在回想做爱前的那段对话。"
    scene c019_s006_070 with Dissolve(0.5)
    s "[player_name]，我……"
    j "如果你想说你刚才只是一时冲动才说了「我爱你」，我能理解。"
    scene c019_s006_071 with Dissolve(0.25)
    s "不，不是。我真的是。或者说，我感觉自己是真的。对不起。这件事对我来说很难真正抓住。也或许不是很难，只是我…… *叹气*"
    scene c019_s006_072 with Dissolve(0.25)
    s "我只是害怕。不是怕你。我知道我可以信任你。知道我们在一起时我可以只是我自己，而你不评判。天哪，在我关于这件事的所有想法里，我知道你是其中最好的部分，尤其是对我而言。就这样坐在这儿，一起聊些蠢事？你根本不知道这让我有多开心。"
    j "那是什么？"
    scene c019_s006_073 with Dissolve(0.25)
    s "我、我怕我最后会变成她那样。变成南希。"
    j "怎么会？"
    scene c019_s006_074 with Dissolve(0.25)
    s "我花了很多年活在当下。从不把一段关系维持下去，因为我一旦无聊就放弃，或者因为新的闪亮东西出现就转移视线。又或者，我只是不想让任何人发现我正在吃一大把药、根本没法在关系里成为对等的伙伴。"
    j "我早就知道你在吃药，而这对我来说没有任何改变。"
    scene c019_s006_075 with Dissolve(0.25)
    s "这不是重点。我……我只是想不要成为你眼中那种人。对你而言。我很害怕自己最后又会变回「我自己」。然后我会临阵脱逃，而你不该承受这个。不该再一次。你太好了。"
    s "所以我想，等这一切结束、等我们出去之后，我就拉开距离。但我又不想，因为……此刻这一切对我来说就像天堂。我……我想要更多。多得多。"
    scene c019_s006_076 with Dissolve(0.25)
    s "我现在只是很困惑。很害怕。而且我觉得你值得比这更好的东西。某种更实在的东西。来自一个不会因为看见新的闪亮东西就转身走开的人。"
    j "那是……那是个很合理的担心，但也许你对自己太苛刻了。今晚——以及接下来最近的一段时间——我们先别为那种决定操心，好吗？"
    scene c019_s006_077 with Dissolve(0.25)
    s "但是——"
    j "雪莉，我爱你，而且今晚不必是一个要把什么钉死的时刻。没人会一次性就做出终身的决定。这件事我们可以以后再谈。"
    scene c019_s006_078 with Dissolve(0.25)
    s "好、好吧。如果你觉得那样好的话。"
    j "我确实这么觉得。"
    scene c019_s006_079 with Dissolve(0.5)
    "当然，我现在是在放她一马，但事实是我也不可能从她嘴里套出什么关于未来感情的承诺。不确定性太大了，根本没法那么做。"
    j "*叹气* 我们该回去了。趁还没人来找我们。别让劳拉比现在更担心。"
    scene c019_s006_080 with Dissolve(0.25)
    s "大概吧。"
    scene c019_s006_081 with Dissolve(0.5)
    s "我很喜欢这套——作为一套衣服——但当成日常穿着大概不现实。"
    j "我敢肯定会让人多看几眼，也会招来几个问题。"
    scene c019_s006_082 with Dissolve(0.25)
    s "我唯一想让其转头的人是你。*咯咯笑*"
    j "任务完成。你换下这身之前穿的衣服在哪儿？"
    scene c019_s006_083 with Dissolve(0.25)
    s "更衣室。"
    j "你想让我陪你去吗？"
    scene c019_s006_084 with Dissolve(0.5)
    s "不用，我没事。从那儿到大堂都很安全。我保证不会太久。"
    j "好吧。我给你十分钟，超时我就来找你。"
    scene c019_s006_085 with Dissolve(0.25)
    s "行行行。我现在可是在计时呢。一会儿见。"
    jump shelley_achievement_check
label ch20_shelley_sex:
    $ persistent.ch20_shelley_sex = True
    "那并不意味着我们不能像真正的情侣那样依偎在一起。而且，鉴于我们单独相处的次数那么多，雪莉也愿意把这些心情分享出来，把我们想成那种关系很牵强吗？好吧，事情没那么非黑即白，但至少今晚，我们可以是。"
    "我不知道她是不是已经睡着了，但她背脊窜过一阵战栗时发出的咯咯笑声告诉我，我的肢体接触并没有让她反感。我心里有点使坏，又有几分发情，于是决定再进一步。"
    scene c020_s006_010 with Dissolve(0.25)
    "我的手伸向她的乳房，捏了一把。如果她真的睡着了，我大概得不到多少反应——而那就是适可而止的信号。"
    s "唔嗯……"
    scene c020_s006_011 with Dissolve(0.25)
    s "玩得开心吗？*咯咯笑*"
    j "只是想看看现在是什么情况。你要是想让我停，我随时能停。"
    stop music fadeout 2.0
    scene c020_s006_013 with Dissolve(0.25)
    s "别停。其实……"
    scene c020_s006_014 with Dissolve(0.25)
    s "给你。直接接触。"
    j "*轻笑* 我就猜是这样。"
    scene c020_s006_015 with Dissolve(0.25)
    s "就知道嘛……唔唔嗯~~~……就知道什么？"
    j "你钻到沙发上是有目的的。"
    scene c020_s006_016 with Dissolve(0.25)
    s "是啊。但不只是为了跟我亲热。"
    j "抱歉，我不是想把你的动机简化成生理需求。我应该——"
    play music shelleytheme fadein 2.0
    play voice_loop kiss
    scene c020_s006_017 with flashpink
    "她翻过身把我拉近，嘴唇直直贴上我的。我那句为自己辩解的道歉，随着她的舌头滑进我嘴里而彻底死了。"
    s "啾噜噗~~~ 咻噜噗~~~"
    scene c020_s006_018 with Dissolve(0.5)
    "也许我并没有完全想错，她脑子里确实装着那件事。又或者，只要我们单独待着，这就总是一种可能。"
    s "嘘咝~~~~~ 唔唔嗯~~~~"
    stop voice_loop
    scene c020_s006_041 with Dissolve(0.25)
    s "我爬进你的「床」上来，可不只是为了跟你亲热。先跟你说清楚。"
    j "我不该擅自揣测。抱歉。"
    scene c020_s006_019 with Dissolve(0.25)
    s "哦，我不是说我不喜欢我们一起合奏出的这种性感声响，而是我来找你，是因为你让我安心。而且你很暖和。\n    而且我喜欢和你单独待着。还有……还有，我爱你。"
    j "我也爱你，雪莉。"
    scene c020_s006_020 with Dissolve(0.25)
    s "不过既然我们已经到这一步了……"
    j "你也爱我的鸡巴吗？"
    s "你他妈当然最好信了。"
    play voice_loop kiss
    scene c020_s006_021 with flashpink
    s "咻噜噗噗~~~ 嘘咝~~~~~"
    "好吧，如果她之前还没那个意思，现在肯定有了。真得喜欢这样的女人——几分钟之内，就能从打瞌睡变成抚弄我的鸡巴。"
    stop voice_loop
    scene c020_s006_022 with Dissolve(0.25)
    s "你也喜欢我的身体，对吧？*咯咯笑*"
    j "这还用问吗？"
    s "我只是想亲耳听你说出来。"
    play voice_loop kiss
    scene c020_s006_023 with flashpink
    "我用一个吻回答了她，同时手指在她的小穴上撩拨。"
    s "唔唔嗯~~~ 咻噜噗噗~~~~"
    stop voice_loop
    scene c020_s006_022 with Dissolve(0.25)
    j "对。我喜欢。"
    s "我啊啊~~~ 能感觉到。"
    j "你怎么不翻过来侧躺？"
    s "嗯啊啊~~~ 嗯。"
    scene c020_s006_024 with Dissolve(1)
    j "好了。大概不是最舒服的姿势——"
    s "不在乎。我要你进来。"
    scene c020_s006_025 with Dissolve(0.5)
    s "啊嗯~~~ 嗯，我能感觉到他抵着我。天啊，他好烫。"
    j "你也是。"
    play voice_loop shelley_slow
    scene c020_s006_026 with hpunch
    s "啊啊啊啊~~~ 哦咿嗯~~~"
    scene c020_s006_027 with hpunch
    s "哦操~~~ 哦嗯嗯~~~"
    "她里面湿得一塌糊涂，烫得像在发烧。"
    scene c020_s006_028 with Dissolve(0.25)
    s "啊嗯嗯~~~ 嗯啊啊啊~~~"
    "我一口咬住她的乳房，在深处抽送着捏紧。雪莉在快感中尖叫起来。"
    scene c020_s006_029 with Dissolve(0.25)
    show shelley_ch20_fuck with Dissolve(0.25)
    s "哈啊啊~~~ 哦操嗯啊啊啊~~~"
    "沙发很结实，我一边在雪莉体内进出，一边庆幸它没有弹簧。"
    s "唔嗯~~~ 唔唔嗯~~~"
    "我知道她本来就会叫得够大声了，沙发完全没必要再替我们通报。"
    s "唔唔嗯~~~ 唔嗯~~~~~"
    j "是的宝贝啊啊~~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c020_s006_030 with Dissolve(0.5)
    show shelley_ch20_fuck2 with Dissolve(0.25)
    hide shelley_ch20_fuck
    "麻烦在于，我得先换个更好的姿势才能真正进到她最里面去。于是我把她的腿抬起来，希望能把髋部压得更深一些。"
    s "哦哦哦~~~ 天啊嗯啊啊啊~~~"
    "就在我离完全退出还差几厘米的时候，这个角度显然对她起了作用。"
    s "唔嗯~~~ 唔哦~~~"
    "我那点「能保持安静」的指望彻底泡汤了。"
    stop voice_loop
    play voice_loop shelley_fast
    scene c020_s006_031 with Dissolve(0.5)
    show shelley_ch20_fuck3 with Dissolve(0.25)
    hide shelley_ch20_fuck2
    "不想再在临界点上磨蹭，我换了个姿势接着干。"
    s "哦操~~~ 嗯啊啊啊~~~"
    s "唔嗯~~~ 就那样"
    s "天啊嗯啊啊啊~~~"
    j "嗯，你感觉好爽"
    s "你也是啊啊啊~~~"
    scene blank with Dissolve(1)
    scene c020_s006_032 with Dissolve(1)
    show shelley_ch20_fuck4 with Dissolve(0.25)
    hide shelley_ch20_fuck3
    "雪莉最后让我仰躺下去，好让她骑在我身上。"
    s "哈啊~~~ 哦操你的鸡巴"
    j "你真是唔唔~~~"
    s "舒服死了啊啊啊~~~~"
    s "你怎么总是这么爽啊啊啊~~~"
    j "我努力着呢。*轻笑*"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c020_s006_033 with Dissolve(0.5)
    show shelley_ch20_fuck5 with Dissolve(0.25)
    hide shelley_ch20_fuck4
    "我盼着她就快到了，因为我知道我自己也快了。"
    s "啊嗯嗯哈哈~~~ 啊嗯嗯~~~~"
    s "哦操操~~~"
    j "嗯，快射了"
    s "射吧啊啊~~~ 操我啊啊啊~~~"
    s "唔嗯~~~" with hpunch_soft
    stop voice_loop
    play voice_loop shelley_cum
    scene c020_s006_034 with hpunch
    hide shelley_ch20_fuck5
    pause 0.3
    scene c020_s006_035 with hpunch
    pause 0.3
    scene c020_s006_036 with hpunch
    pause 0.3
    scene c020_s006_035 with hpunch
    pause 0.3
    scene c020_s006_036 with hpunch
    pause 0.3
    scene c020_s006_037 with Dissolve(0.5)
    stop voice_loop
    "来了。"
    scene c020_s006_038 with flash
    play sound male_cum
    pause 0.5
    scene c020_s006_038 with flash
    scene c020_s006_039 with Dissolve(0.5)
    j "唔哦~~~ 操 *喘息*"
    s "嗯 *喘息* 现在可爽死了。*咯咯笑*"
    scene c020_s006_040 with Dissolve(0.25)
    s "*喘息* 天啊，我爱你。"
    j "我敢肯定上帝很感激这句话，但——"
    s "我也爱你。*咯咯笑*"
    $ renpy.end_replay()
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c020_s006_042 with Dissolve(2)
    play music nightmain fadein 2.0
    "{color=#EEF527}天哪，那姑娘真是半点都藏不住。希望她别把其他人吵醒。{/color}"
    scene c020_s006_043 with Dissolve(0.25)
    "{color=#EEF527}又或者，其实也无所谓了，因为大家基本都清楚他俩在搞什么。那家伙的性生活简直是最藏不住的秘密。{/color}"
    if e_sex >= 3 and bicontent == "no":
        "{color=#EEF527}也许还不至于完全不知道，因为我不确定有没有人知道我们的事。暂时还没有。{/color}"
    elif e_sex >= 3 and bicontent == "yes":
        "{color=#EEF527}也许还不至于完全不知道，因为我不确定除了雪莉之外还有没有人知道我们的事。暂时还没有。{/color}"
    scene blank with Dissolve(2)
    scene c020_s006_044 with Dissolve(2)
    s "你知道，我来找你真的只是想离你近一点。我刚下完夜班，心里有点不安。"
    j "是啊，当「我们能不能一起睡」真的就只是睡觉的时候，我就不该再预设你另有目的。"
    scene c020_s006_045 with Dissolve(0.25)
    s "以前你这么说倒也没错。那时的我还是个大学女生，这点我承认。但现在简单多了。我来找你，是因为你让我快乐、让我安心。而且我爱你。"
    "她像是在试验这些词，仿佛还不太习惯把它们说出口，而说出口本身让她感到安慰。"
    scene c020_s006_046 with Dissolve(0.25)
    s "当然，这最后滚到床上也不坏，但就算只是抱着一起躺也好啊。老实说，光是这样躺着、你的髋和肩膀贴着我的背——就只是碰着我——都已经足够了。"
    j "你本来可以——"
    scene c020_s006_047 with Dissolve(0.25)
    s "不，不行。你一对我的动手动脚、戳来戳去，我就他妈完全失控。"
    j "那看来我以后得注意点。"
    scene c020_s006_048 with Dissolve(0.25)
    s "或者，你不用改。我是说，你可以更好。"
    j "这里头信号真够乱的。"
    scene c020_s006_049 with Dissolve(0.25)
    s "你只要知道我爱你，还有——显然——我对你说不出不就行了。重要的就是这个。"
    j "你这么说越来越顺口了啊，是不是？"
    s "感觉确实不错。我承认。我大概是在等对的人。"
    "我就是对的人。知道这一点，感觉真好。"
    jump shelley_achievement_check
label ch21_shelley_sex:
    $ persistent.ch21_shelley_sex = True
    play voice_loop kiss
    scene c021_s008_007 with flashpink
    play music shelleytheme fadein 2.0
    s "咻噜噗~~~ 唔唔嗯~~~"
    "哎呀，看来这场角色扮演马上就要往更肉体化的方向走了。又或者，以雪莉的性子，我觉得大概就是这样。感觉这一整场本来就为了这个。"
    stop voice_loop
    scene c021_s008_008 with Dissolve(0.5)
    s "幸好办公室没人，因为要是同事看见我们，我可不知道会惹出什么麻烦。"
    j "好吧，反正我是老板，惹麻烦的也是我，所以也许我们还是低调点。"
    scene c021_s008_009 with Dissolve(0.25)
    s "哦，如果你肯好好伺候我，这点我当然能做到。"
    j "我能做到。不过这就带出一个问题了。"
    s "什——么问题~~~"
    scene c021_s008_010 with Dissolve(0.25)
    j "那件外套？你就是在办公室里随便捡到件衣服，直接套在胸罩外面就来了？你是故意的吗？我是说，我知道你喜欢在我面前显摆。"
    s "也许吧。不过我也找不到合适的衬衫。或者说，我不想找「一件合适的衬衫」。再加上这里有点闷。或者嘛~~~ 我是在所有人都下班之后才这么穿的，好让你注意到、想让你看我。*咯咯笑*"
    j "哦，我正在看你呢。没法不看你——你一整天就在这张桌子后面热辣又性感地坐着。"
    scene c021_s008_011 with Dissolve(0.5)
    s "很好。也许我能做点什么来挣个加薪。"
    j "嗯，那就先让我看看货色，之后再说。"
    s "我知道你又想看，[player_lastname]先生。你逮着机会就往我衬衫里瞄。"
    play voice_loop shelley_slow
    scene c021_s008_012 with Dissolve(0.25)
    j "你这么火，我要是不看才奇怪。"
    s "啊啊~~~ 我就知道你想要我。每次和我开完会，你那鼓包都会变大，我看得出来。"
    stop voice_loop
    scene c021_s008_013 with Dissolve(0.25)
    s "来，让我看看你一直瞒着我的是什么。"
    j "我觉得你早该知道，我下面那儿的动静。"
    s "也许吧，但我还是想看。不然我怎么挣这份钱？"
    scene c021_s008_014 with Dissolve(0.25)
    s "哎呀，他要进来还真有点难度，是不是？"
    j "我觉得我们应付得来。"
    s "嗯，不过先……"
    play voice_loop kiss
    scene c021_s008_015 with flashpink
    s "咻噜噗噗~~~ 唔嗯~~~~"
    "我们就那样站着接吻，雪莉的手缓缓抚上我。我卡在两种念头之间——一边想看这场角色扮演会走到哪一步，一边只想把她按下去狠狠干。"
    scene c021_s008_016 with Dissolve(0.25)
    stop voice_loop
    s "哈啊~~~ 现在我要让你高兴了。"
    j "你已经让我高兴了，雪莉。"
    scene c021_s008_017 with Dissolve(0.25)
    s "但那种高兴换不来更大的薪水。*咯咯笑*"
    j "哦？哦，说得对。抱歉，我刚才一时忘了自己的身份。"
    "老实说，我从没当过经理，也没碰上过这种事，很难一直不出戏。所以我只是照搬电视和电影里看来的套路。而那些家伙总是被描绘成糟糕透顶的人渣。"
    scene c021_s008_018 with Dissolve(0.5)
    s "那么，给我口交……那值再加五百块薪水，对吧？"
    j "不清楚。得看你保证的有没有那么好吃。*轻笑* 我只付得起顶级的活。"
    s "哦，真的吗？"
    play voice_loop blowjob1
    scene c021_s008_019 with Dissolve(0.25)
    "雪莉把这句话当真了，立刻凑了上来。还没进她嘴里的前几秒，我就能感觉到她的热气喷在鸡巴上。她的舌头沿着顶端滑过，我整个人不由自主地一颤。"
    scene c021_s008_020 with Dissolve(0.25)
    s "咻噜噗噗~~~ 唔唔嗯~~~"
    j "唔哦嗯~~~ 嗯。"
    scene c021_s008_021 with Dissolve(0.25)
    show shelley_ch21_bj with Dissolve(0.25)
    j "唔嗯~~~ 操这姑娘啊啊~~~"
    "好吧，她当真了。或者说，比我预想的当真得多。"
    s "嘘咝噜噗噗~~~~ 唔唔嗯~~~~"
    j "操~~~ 哦嗯嗯~~~ 不想让别人看见你这么厉害"
    j "别的主管估计会想分着玩你唔唔嗯~~~"
    stop voice_loop
    play voice_loop blowjob2
    scene c021_s008_022 with Dissolve(0.5)
    show shelley_ch21_bj2 with Dissolve(0.25)
    hide shelley_ch21_bj
    "我想，「被人传来传去」这个前景对雪莉来说像是按下了某个开关。话虽如此，她还是尽力把我含到最深。"
    s "嘘咝~~~~ 唔嗯~~~"
    j "哦，我可不会让你这么轻易脱身唔唔嗯~~~"
    j "我可不想让你越过我，直接去勾搭我老板啊啊~~~"
    j "尤其是没有我这么厉害的嘴哦嗯嗯~~~"
    s "咻噜噜~~~"
    scene c021_s008_023 with Dissolve(0.5)
    show shelley_ch21_bj3 with Dissolve(0.25)
    hide shelley_ch21_bj2
    "这句夸奖把她推向了最后冲刺，而我当然不会拦住她。"
    s "嘘咝咝~~~~ 咻噜噜~~~"
    j "哦操，这一下给你加薪可加得爽了啊啊~~~"
    j "吞下去还有奖金啊啊~~~"
    s "咻噜噗噗~~~ 唔唔嗯~~~~"
    j "哦操，华莱士小姐啊啊~~~"
    j "你的本事在这儿都要浪费掉了啊啊~~~"
    j "操，哦操，要去了~~~"
    stop voice_loop
    scene c021_s008_024 with flash
    play sound male_cum
    hide shelley_ch21_bj3
    pause 0.5
    scene c021_s008_024 with flash
    "我射出来的时候，她死死含住，一滴不落地全接了下去。我看到她在第一波射进喉咙后干呕着抽动了一下——我敢肯定那一波是溅在她喉咙后壁上的。"
    scene c021_s008_025 with Dissolve(0.25)
    j "哦操，那感觉太爽了。"
    "雪莉慢慢退开，让沾着我口水的鸡巴从她嘴里滑出来。"
    scene c021_s008_026 with Dissolve(0.25)
    j "操，华莱士小姐，这值得多给几天带薪假。"
    s "*含糊不清* 唔唔嗯~~~ 唔唔嗯~~~"
    scene c021_s008_027 with Dissolve(0.25)
    s "*吞咽*"
    j "哦，对，全部吞下去。"
    scene c021_s008_028 with Dissolve(0.25)
    s "我做得很好吗？*咯咯笑*"
    j "好极了，一如既往。"
    s "很好。那要怎样才能换来升职？"
    scene c021_s008_029 with Dissolve(0.5)
    j "我想你知道。*轻笑*"
    s "哦，不行，[player_lastname]先生。在办公室里做爱？那听起来可是老板和下属绝不该做的坏事呢。"
    scene c021_s008_030 with Dissolve(0.25)
    j "我会让你物超所值的。你已经拿到加薪了。"
    s "还有带薪假。别忘了。"
    scene c021_s008_031 with Dissolve(0.25)
    j "我怎么会忘呢。毕竟你火成这样。"
    "天啊，她真的火。雪莉和我在一块儿胡闹——比其他人都多得多——但在这种只有我们两个人的时刻，我看到的是她本来的样子，那么美，我就只想抱着她，和她共度一生。"
    s "[player_name]？[player_lastname]先生？你没事吧？"
    scene c021_s008_032 with Dissolve(0.25)
    j "嗯，没事，就是刚才走神了一下。把这屁股撅起来。"
    s "除非你说喜欢。"
    j "喜欢。我爱你的屁股，爱你火辣的小穴，爱你的一切。"
    scene c021_s008_033 with Dissolve(0.5)
    s "哦，天啊，现在就把他放进我里面。求你了，[player_lastname]先生。就在这里。我湿得要死了。"
    j "很好。你就该一直水灵灵地随时准备好给我用。用他们的话说，随叫随到。"
    scene c021_s008_034 with Dissolve(0.25)
    s "操，那把我存进快速拨号吧。长官，你想怎么用我都行。"
    j "哦，我本来就打算这么做。"
    play voice_loop shelley_slow
    scene c021_s008_035 with vpunch
    s "哦哦哦~~~ 操~~~"
    scene c021_s008_036 with vpunch
    s "唔嗯~~~ 我的天嗯啊啊啊~~~"
    j "听起来你挺喜欢的，华莱士小姐。"
    scene c021_s008_037 with Dissolve(0.5)
    show shelley_ch21_fuck with Dissolve(0.25)
    s "哦操，你里面真爽唔唔嗯~~~"
    j "也许你享受这个，本身就是报酬的一部分。*轻笑*"
    s "唔嗯~~~ 便宜的混蛋 *咯咯笑*"
    j "放心吧，我会在别的方面补偿你，把这段办公室恋情宠得更好。"
    s "哼，光这样可不够唔唔嗯~~~"
    stop voice_loop
    play voice_loop shelley_med
    scene c021_s008_038 with Dissolve(0.5)
    show shelley_ch21_fuck2 with Dissolve(0.25)
    hide shelley_ch21_fuck
    j "*轻笑* 哦，所以这就是纯粹各取所需的关系？"
    s "唔嗯~~~ 不管那词什么意思"
    s "要是「你插进来，我拿钱」这样，那没错。"
    j "你还真是唔唔嗯~~~ 现实得很啊"
    s "姑娘家得、得啊啊~~~~ 挣工资。我那份房租可不便宜，你知道的啊啊~~~"
    j "要不我替你付房租？给我留把钥匙，我想什么时候过去就什么时候过去。"
    s "那样会把你啊啊~~~ 弄坏的"
    stop voice_loop
    play voice_loop shelley_fast
    scene c021_s008_039 with Dissolve(0.5)
    show shelley_ch21_fuck3 with Dissolve(0.25)
    hide shelley_ch21_fuck2
    j "想当我的性感女秘书，就得挣够这个价唔唔嗯~~~"
    s "听起来像啊啊~~~ 在谈判"
    j "而且我这边还站在权力那一头啊啊~~~"
    s "但要是我告诉管理层呢？"
    j "你不敢的，嗯唔唔~~~"
    s "听起来你那个「权力位置」也没那么神气嘛啊啊~~~"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c021_s008_040 with Dissolve(0.5)
    show shelley_ch21_fuck4 with Dissolve(0.25)
    hide shelley_ch21_fuck3
    "好吧，至少知道了雪莉够聪明，知道拿自己的位置做筹码——哪怕那个位置现在正被压在办公椅上，而我在她身下狠干。"
    s "唔嗯~~~ 哦嗯啊啊~~~~ 操我"
    j "姑娘，把那奖金挣回来啊啊~~~"
    s "是的，长官啊啊~~~"
    s "操~~~ 该死啊啊~~~"
    s "哦操操操啊啊~~~"
    "高潮的浪潮一波波冲刷过她，她紧紧地抱住了我。"
    stop voice_loop
    play voice_loop shelley_cum
    scene c021_s008_041 with vpunch
    hide shelley_ch21_fuck4
    pause 0.3
    scene c021_s008_042 with vpunch
    pause 0.3
    scene c021_s008_041 with vpunch
    pause 0.3
    scene c021_s008_043 with vpunch
    pause 0.3
    scene c021_s008_042 with vpunch
    pause 0.3
    scene c021_s008_043 with vpunch
    stop voice_loop
    s "哦操，刚才那下啊啊~~~"
    j "嗯，要去了啊啊~~~"
    scene c021_s008_044 with flash
    play sound male_cum
    pause 0.5
    scene c021_s008_044 with flash
    s "操，那可真是 *喘息* 太多了。"
    j "嗯，华莱士小姐，你确实能把我撩硬。"
    scene c021_s008_045 with Dissolve(0.25)
    s "「撩硬」？你是想说「涨工资」吧？"
    j "我要是让你怀上，那可比这多得多。"
    scene c021_s008_046 with Dissolve(0.5)
    s "哦？没人告诉过你，别跟自己的情妇结婚吗？*咯咯笑*"
    j "至少得做个负责任的父亲。"
    $ renpy.end_replay()
    scene blank with Dissolve(2)
    scene c021_s008_051 with Dissolve(2)
    j "嗯，刚才挺好玩。我是不是该期待更多这种角色扮演，好给生活加点料？"
    s "我确实得让你一直对我有兴趣。我不想我们之间变得无聊。"
    scene c021_s008_052 with Dissolve(0.25)
    j "你真担心我会厌倦你？因为我们到目前为止做的事，没有一件够得上「无聊」。"
    s "别人都会担心。还有……你是第一个让我认真觉得想留在身边的人。"
    scene c021_s008_053 with Dissolve(0.5)
    s "我不想失去你。如果那意味着我得——"
    j "停。你不用做任何事，也不用成为不是自己的人，雪莉。我们之间的性爱很棒，但那不是我来的原因。我在乎的是你这个人。"
    scene c021_s008_054 with Dissolve(0.25)
    s "那么，如果我们以后再也不会做爱了呢？"
    j "我还是会在。我刚才说那些，可不是为了脱你的裤子才编的。我真的爱你。"
    scene c021_s008_055 with Dissolve(0.25)
    s "我、我只是……我不习惯有人留下来。多数时候我倒也无所谓。但对你，我……我不想你走。我需要你。你让我快乐。你让我安心。你……你在我状态很差的时候不会用那种眼神看我。"
    j "这就叫爱啊，姑娘。"
    scene c021_s008_056 with Dissolve(0.25)
    s "我……我在学吧。我想。"
    scene c021_s008_057 with Dissolve(0.5)
    "雪莉靠进我怀里，把刚才角色扮演的那套架势全都卸下了。我感觉到她在发抖，像是在拼命让自己保持镇定。"
    scene c021_s008_058 with Dissolve(0.25)
    j "没事的。我在这儿。"
    s "你……你永远都在。*抽鼻子*"
    "有一阵子，我们就这么沉默地坐着。刚运动完，半裸着、汗津津的，这画面想必很怪，但没人路过来打断。我敢肯定他们听见了。被操的时候，雪莉可不是能憋住不出声的人。"
    if ch19_eve_shelley_bi_sex == "yes":
        scene c021_s008_059 with Dissolve(1)
        s "呃，我……我大概还是得坦白。在高中那边的浴室里，伊芙和我做过了。"
        if ch19_eve_sex == "yes":
            j "哦，是啊。伊芙跟我提过。我猜你们俩都是想让我知道，别人也在床上爽着。*轻笑* 你俩干起来的画面，做睡前幻想素材还真不错。"
        else:
            j "哦？那感觉怎么样？"
        scene c021_s008_060 with Dissolve(0.25)
        s "就……就那么发生了。我的意思是，我们之前确实一直在调情，但我看见她在洗澡，然后一环扣一环，两个人就光着身子干了起来。你……你不会……你生气了吗？因为我跟别人做了？"
        if l_sex >= 3 or e_sex >= 3 or k_sex >= 3:
            j "没有，我没生气。我有什么资格说你不能跟别人鬼混？你知道我把鸡巴插进过别人身体里，也没为这发过一场疯。我怎么可能发？"
        elif ch19_eve_sex == "yes" or ch20_eve_sex == "yes":
            j "没有，我没生气。我们现在又没在谈什么独占的关系。你大概也知道我跟她睡过，我也没为这大吵大闹。我怎么可能？"
        else:
            j "没有，我没生气。如果这是在外面、如果我们正式在谈恋爱，情况可能就不一样了，但现在，光是活下去、保持清醒更重要。如果泄点火就能做到，那很好。再说了，伊芙也确实需要个出口。"
        scene c021_s008_061 with Dissolve(0.25)
        s "大概吧。我……"
        s "我知道我们现在并不是真的在交往，但我爱你，也不希望你觉得等我们出去之后我就会变成另一个人。我知道这很难让你相信，因为「一个刚跟别人上完床的花心大萝卜」传达的信息完全不是那么回事。"
        scene c021_s008_062 with Dissolve(0.25)
        s "但是……如果将来有一天你决定选我，那就只会是我们两个人。我向你发誓。"
        j "好。等到了那一天——等生活恢复成某种正常的样子——我们再一起做这个决定。"
        scene c021_s008_063 with Dissolve(0.25)
        s "嗯。"
        "我能从雪莉脸上看到一丝柔软，说明她这回是认真的。总有一天——希望不会太久——我们得认真谈谈以后有没有一起生活的可能。而我要不要把她送回家人那边，这也是我必须考虑的事。"
        if ch19_eve_sex == "yes" or ch20_eve_sex == "yes":
            scene c021_s008_064 with Dissolve(0.5)
            j "所以，你觉得自己能说服她来一场「你—我—她」的小三人行？*轻笑*"
            s "真的吗？因为那可他妈的性感死了。三个人挤进一张床？嗯。"
            scene c021_s008_065 with Dissolve(0.25)
            s "我大概有办法。我觉得说服她不会太费力。"
            j "这话我爱听。"
            s "*咯咯笑* 我就知道我爱你是有些理由的。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c021_s008_066 with Dissolve(2)
    play music insideday3 fadein 2.0
    "还没等有人来偷窥，我们就起身穿衣服了。"
    scene c021_s008_067 with Dissolve(0.25)
    "雪莉在刚才那番谈话之后情绪格外激动，她停下来，直直看进我的眼睛。"
    s "我真的爱你。我本来以为自己做不到这种事，但现在……嗯。"
    j "你一直都做得到。你只是需要对的人。我是「现在」的那个人，但是——"
    scene c021_s008_068 with Dissolve(0.25)
    s "这话你可别说了。别让我变成卡莉，戳着你的肋骨。"
    j "嗯，那种事我有点受够了。"
    s "不过那招确实管用。"
    j "可惜啊，真的管用。"
    jump shelley_achievement_check
label ch22_shelley_sex:
    $ persistent.ch22_shelley_sex = True
    scene blank with Dissolve(2)
    scene c022_s006_013 with Dissolve(2)
    "调整花了几分钟——全程伴时不爽地拿手肘顶我的肋骨——最后雪莉总算坐进了我怀里，我们也把注意力放回了电影。到目前为止我对剧情都没怎么上心，但有雪莉贴着我，我发现自己根本不在乎。"
    scene c022_s006_014 with Dissolve(0.25)
    "不只是这样。我还一直在偷看她，欣赏这个甜美、美丽、信任我到愿意这样亲近的年轻女人。而且这不只是身体空虚、想找个人发泄——雪莉不止一次说过这一点。她对我有感情，我也对她有。"
    "当然，年龄差摆在那里。她是个大学女生，而我是个无聊的办公室离婚男人。她能从我这种人身上得到什么？除了拥有同样的人生创伤之外？那能撑得起一段承诺关系吗？"
    scene c022_s006_015 with Dissolve(0.5)
    s "嘿，那个……你……你……"
    j "嗯？怎么了？"
    scene c022_s006_044 with Dissolve(0.25)
    s "你知道我为什么要做这些吧？*咯咯笑*"
    j "你想要亲近？你是想要一次感觉像正常人的体验？"
    scene c022_s006_045 with Dissolve(0.25)
    s "你是不是不开窍？"
    j "不，我只是谨慎，不擅自假设任何事。"
    scene c022_s006_046 with Dissolve(0.25)
    s "真的吗？现在？"
    j "有些习惯是改不掉的。你一次又一次地被推开、被告知没人要你，这会让人很难主动迈出第一步，因为我只会预期再一次被拒绝。"
    stop music fadeout 3.0
    scene c022_s006_016 with Dissolve(0.25)
    s "哦，[player_name]，你得明白不是每个人都像你前任那样是个蠢货。你可以对我主动。我不介意。事实上，我正想要。所以我才坐在这边，而不是沙发的另一头。"
    j "嗯，这个嘛……"
    s "哦，别说了。*咯咯笑*"
    play voice_loop kiss
    scene c022_s006_017 with flashpink
    s "咻噜噗~~~ 唔唔嗯~~~"
    play music shelleytheme fadein 2.0
    "尽管雪莉平时把自己的意图表达得很直白，她却没能真正体会被一次次推开、一次次拒绝是什么滋味。那会在你脑子里留下一个声音——不管证据如何都说——每一次身体接触都有极大可能会被拒绝。"
    stop voice_loop
    scene c022_s006_018 with Dissolve(0.25)
    s "我得让你明白，不是每个人都会那样对你。老实说，谁都不该那样对你。你火辣、有趣，而且……嗯，还有很多优点。再说，成熟男人这一套对我也挺受用。我们最大的问题是没能有多少独处时间。"
    j "可我们现在有。暂时。"
    scene c022_s006_019 with Dissolve(0.5)
    s "那就该好好珍惜。"
    j "你只是想把你的女伴们都弄到手。*轻笑*"
    scene c022_s006_020 with Dissolve(0.25)
    s "你也想要这个。"
    j "想要。我真的想要。"
    scene c022_s006_021 with Dissolve(0.25)
    s "这个信号够明显了吧？你该明白我想要什么。"
    j "我想我还没那么不开窍。"
    scene c022_s006_022 with hpunch
    "我们还在沙发上，我扑过去想吻雪莉，结果两个人七手八脚缠成一团，一起向后倒。不知道为什么——大概只是她四肢乱舞的样子太滑稽——雪莉一路笑着一屁股跌坐下去。"
    s "你总算肯主动了。"
    j "你想让我来主导？好啊~~~"
    play voice_loop kiss
    scene c022_s006_023 with flashpink
    "我压在她身上，咬住雪莉的嘴唇。我们啃在一起的时候，我感觉她在扯我的衬衫。"
    s "咻噜噗噗~~ 唔唔嗯~~~~"
    stop voice_loop
    scene c022_s006_024 with Dissolve(0.25)
    j "*轻笑* 好，我懂了——我该脱光，好把火热的部位贴在一起。"
    s "很高兴这提示够明显。"
    scene c022_s006_025 with Dissolve(0.5)
    j "要不是我这些年听惯了自相矛盾的暗示，还有社会教育我说「不经同意就动手动脚就是怪人」，我大概会表现得更明显一些。"
    s "去他妈的社会怎么想。我告诉你，只要我把上衣脱了，我就只剩内裤了。"
    scene c022_s006_026 with Dissolve(0.25)
    j "只剩内裤？接下来要发生的就是这个？我要不要去拿个一捏就响的油彩小丑鼻子和红气球？"
    s "如果那是你的癖好，我愿意试试角色扮演。不过今晚你能不能让我用正常的方式叫出来——用那根八英寸的东西顶进我身体里。"
    scene c022_s006_027 with Dissolve(0.25)
    j "所以今晚是正常做爱，角色扮演以后再说。我记下了。"
    s "行，反正别来星球大战那套。不知为什么，扮成莱娅公主这件事让我有点抗拒。"
    scene c022_s006_028 with Dissolve(0.25)
    j "明白。不演太空公主，可以干小丑。"
    scene c022_s006_029 with Dissolve(0.5)
    s "也不完全是那么回事，但你懂我意思。"
    j "我大概不懂，不过我相信等我们到了你不喜欢的部分，你会告诉我。"
    scene c022_s006_030 with Dissolve(0.25)
    s "你可想不到那条线画在哪儿。*咯咯笑* 现在，给我拿来。我为这一刻等得太他妈久了。"
    j "从我们到这儿开始？还是从我们单独待在沙发上开始？"
    play voice_loop shelley_slow
    scene c022_s006_031 with Dissolve(0.25)
    s "哦哦哦~~~ 嗯啊啊啊~~~"
    j "怎么了？"
    scene c022_s006_032 with vpunch
    s "不想说有多久了啊啊啊~~~ 你会觉得我是个坏女孩。"
    j "恐怕说这些已经太晚了。"
    scene c022_s006_033 with Dissolve(0.25)
    s "那就……唔唔嗯~~~ 让我好好享受这一次吧。"
    j "哦不，你现在勾起我好奇心了。"
    show shelley_ch22_fuck with Dissolve(0.25)
    j "你一天里有多长时间是处在性兴奋状态的？"
    s "比你以为的啊啊~~~ 得多"
    s "尤其是你在唔唔嗯~~~ 身边的时候。"
    j "能听人唔唔~~~ 这么说真好。"
    s "你也许不信，但看见这一点的可不只是那个发疯似的淫荡女孩。"
    stop voice_loop
    play voice_loop shelley_med
    scene c022_s006_034 with Dissolve(0.5)
    show shelley_ch22_fuck2 with Dissolve(0.25)
    hide shelley_ch22_fuck
    j "嗯，只要你看见了啊啊~~~ 就够了。"
    s "好。这正是我唔唔~~~ 现在想听的。"
    "嗯，当我正把鸡巴整根埋在雪莉体内时，还去钓夸赞、说别的女人因为我下面湿了，听起来很没品——哪怕她对关系这件事开放一些。"
    s "哦哦哦~~~ 哦天啊我太需要这个了。"
    j "我们俩都需要。能这样结束这么糟的一天真好。"
    stop voice_loop
    play voice_loop shelley_fast
    scene c022_s006_035 with Dissolve(0.5)
    show shelley_ch22_fuck3 with Dissolve(0.25)
    hide shelley_ch22_fuck2
    "一旦我们真的干起来，再想把这个话题往下推就没意义了。"
    s "唔嗯~~~ 哦嗯嗯~~ 哦操嗯啊啊啊~~~"
    j "天啊，嗯，真的好爽。"
    s "哦哦哦~~~ 就在那儿唔嗯~~~"
    s "嗯，嗯啊啊啊~~~"
    scene c022_s006_036 with Dissolve(0.5)
    show shelley_ch22_fuck4 with Dissolve(0.25)
    hide shelley_ch22_fuck3
    s "哦操唔嗯~~~"
    "沙发虽然结实，但从背后狠干雪莉的时候，它还是开始嘎吱作响。"
    s "唔嗯~~~ 哦嗯~~~ 唔嗯~~~"
    j "操嗯啊啊啊~~~"
    s "唔嗯~~~ 唔唔嗯~~~"
    stop voice_loop
    play voice_loop shelley_preorgasm
    scene c022_s006_037 with Dissolve(0.5)
    show shelley_ch22_fuck5 with Dissolve(0.25)
    hide shelley_ch22_fuck4
    "我们冲向一个又湿又脏的终点时，我意识到我们和卧室之间根本没有门。我敢肯定楼上每个人都听得一清二楚。"
    s "哈啊~~~ 啊啊~~~"
    j "给我射，姑娘唔唔嗯~~~"
    s "嗯啊啊啊，我射了~~~"
    s "唔嗯~~~ 唔唔嗯~~~"
    s "哦操唔嗯~~~" with vpunch_soft
    stop voice_loop
    play voice_loop shelley_cum
    scene c022_s006_038 with vpunch
    hide shelley_ch22_fuck5
    pause 0.2
    scene c022_s006_039 with vpunch
    pause 0.2
    scene c022_s006_040 with vpunch
    pause 0.2
    scene c022_s006_039 with vpunch
    pause 0.2
    scene c022_s006_040 with vpunch
    pause 0.2
    scene c022_s006_041 with Dissolve(0.5)
    stop voice_loop
    s "唔哦~~~ 哦嗯~~~"
    j "啊操~~~"
    scene c022_s006_042 with flash
    play sound male_cum
    pause 0.5
    scene c022_s006_042 with flash
    pause 0.5
    scene c022_s006_043 with Dissolve(0.25)
    j "哦操，那真是…… *喘息* 哦，嗯。"
    scene c022_s006_047 with Dissolve(0.5)
    s "嗯，操。我…… *呼气* 我今天大概到这儿了。比我想的还累。"
    j "要不试着把电影看完？"
    s "你真的在乎吗？*咯咯笑*"
    $ renpy.end_replay()
    scene blank with Dissolve(2)
    scene c022_s006_048 with Dissolve(2)
    "我们最后还是试着把电影看完，但那时早就跟丢了剧情。于是我们就那么沉默地坐着，珍惜着在一起、又独处的每一刻，哪怕只有短短一会儿。"
    scene c022_s006_049 with Dissolve(0.5)
    s "[player_name]？"
    j "嗯，雪莉？"
    scene c022_s006_050 with Dissolve(0.25)
    s "我爱你。这点我要说清楚。我爱你。我也喜欢和你在一起。"
    j "我也是。虽然有时候我挺难搞的。"
    scene c022_s006_051 with Dissolve(0.25)
    s "嗯，我明白我们各自都有些得靠自己解决的破事。但我不想让这些让我们的关系变得比现在更难。"
    scene c022_s006_052 with Dissolve(0.25)
    s "你看，我理解你在之前那段关系里有过什么心结、什么问题，也明白你是怎么走到今天这一步的。我以前连任何东西都留不过几周。但我在努力撑过去。你绝对值得我冒这个险。你该跟我一起走这段路。"
    j "我在努力，雪莉。可有些肌肉记忆真不是那么容易改掉的。她毁掉的不只是我们的婚姻；她还毁掉了我在此后任何一段关系里感到安心、自信的能力。我的自我认知……不太好。"
    scene c022_s006_053 with Dissolve(0.25)
    s "这我理解。但也许你可以明白我不是她。好吗？我不知道她到底有什么毛病，但换作是我，我就不会放你走，更不会在外面乱搞。我会像这样每晚都把你抱紧。我知道你是个多棒的男人。"
    j "*叹气* 谢了。"
    scene c022_s006_054 with Dissolve(0.5)
    "雪莉往我身上蹭了蹭，注意力重新回到电视上。"
    scene c022_s006_055 with Dissolve(1)
    "十分钟后，我提到在她下班前也许该先放点片子，她已经昏昏欲睡。"
    scene c022_s006_056 with Dissolve(1)
    "她开玩笑说要免费演练一场，然后收拾好衣服走向浴室。等她走远，我也重新穿好衣服，把注意力转向窗外。"
    scene blank with Dissolve(2)
    scene c022_s006_009 with Dissolve(2)
    "字幕开始滚动的时候，雪莉已经摊在沙发上，睡得很沉。"
    jump shelley_achievement_check
label shelley_achievement_check:
    #stop music fadeout 2.0
    if s_sex >= 1 and persistent.shelley_firstime == False:
        scene blank with Dissolve(2)
        $ persistent.shelley_firstime = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_shelley_firstime", transition=slideright)()
        pause
        $ Hide("achievement_shelley_firstime", transition=dissolve)()
        $ quick_menu = True
    jump misc_achievement_check
    return
