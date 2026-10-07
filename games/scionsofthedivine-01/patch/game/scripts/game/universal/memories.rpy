label astarayngbg:
    scene black
    hide c1p4s2 with diss
    play bgm "bgm/Girl Time.ogg" fadein 1.5
    pause 1.0
    show c1p4b1s1 1
    rayn "他确实生疏了，而且有点不堪一击。" with diss
    rayn "不过我总觉得他是看在我是女人的份上手下留情了。"
    play sfx "sfx/Cloth3.ogg"
    show c1p4b1s1 2
    mc "（该死……）" with diss
    mc "（我是不是表现得太明显了？）"
    show c1p4b1s1 3
    rayn "说真的，他光着身子走出来的时候，我还挺惊艳的。" with diss
    rayn "我一直以为他就是那副瘦巴巴的窝囊样子。"
    show c1p4b1s1 4
    rayn "看来是我看走眼了。" with diss
    rayn "这倒让我好奇，那副无聊路人甲的外表下，他还藏着些什么。"
    show c1p4b1s1 5
    asta "他确实很奇怪。" with diss
    asta "我跟他也不算熟，但看起来他就是那种会转移话题、不会真正对谁敞开心扉的人。"
    show c1p4b1s1 6
    asta "不过我可以告诉你他在藏什么……" with diss
    asta "他腰带以下是雄伟的。"
    show c1p4b1s1 7
    rayn "嗯哼……" with diss
    rayn "才刚认识他，你就已经上手了！"
    rayn "我还以为你对人类更私密的生理需求没兴趣呢。"
    show c1p4b1s1 8
    asta "呃——不，不是！" with diss
    asta "完全不是那种事……"
    show c1p4b1s1 9
    asta "我们认识那天闯了点祸——好吧，是{i}我{/i}惹的祸——我让他躲到我那儿。" with diss
    asta "他需要换衣服，我借了他一些我父亲以前的旧衣服，他在浴室换的时候出了点{i}小意外{/i}。"
    play sfx "sfx/Locker - Open.ogg"
    show c1p4b1s1 10
    mc "（对……{i}小意外{/i}。）" with diss
    mc "（那可比{i}小意外{/i}大多了。）"
    show c1p4b1s1 11
    rayn "哦，我懂了。" with diss
    rayn "所以你趁机看了他的货色，嗯？"
    show c1p4b1s1 12
    asta "就一眼！" with diss
    asta "但已经足够{i}了解{/i}了。"
    show c1p4b1s1 11
    rayn "了解你想要它？" with diss
    show c1p4b1s1 13
    asta "才不是，坏蛋！" with diss
    show c1p4b1s1 14
    asta "是了解谁要是真的想要、并且最后得到它，那人会有多幸运。" with diss
    show c1p4b1s1 15
    rayn "嗯……" with diss
    rayn "所以，你不想要？"
    play sfx "sfx/Locker - Close.ogg"
    show c1p4b1s1 16
    asta "不想，就算想，我也不能让任何事分散我对{i}我的任务{/i}的专注。" with diss
    show c1p4b1s1 17
    rayn "啊，说得也是。" with diss
    rayn "他会成为{i}你的任务{/i}的一部分吗？"
    rayn "所以你才要训练他？"
    show c1p4b1s1 18
    asta "我还不知道。" with diss
    asta "我觉得他有潜力，但不确定他是否已经准备好完全接受自己成为神裔了。"
    show c1p4b1s1 19
    mc "（唉，是啊。）" with diss
    mc "（说实话我也不确定自己准备好了……）"
    mc "（偷听得够多了。）"
    mc "（我得快点洗完，然后……我想来一杯烈酒。）"
    hide c1p4b1s1 with diss
    pause 1.0
    return

label soul_skinnydipping:
    if _in_replay:
        play bgs "bgs/Forest Pond - Night.ogg" fadein 1.0
    show c1p4s8 25 with diss
    mc "你在干什么？" with diss
    show c1p4b2s1 1
    hide c1p4s8
    soul "不然我在干什么？" with diss
    show c1p4b2s1 2
    mc "呃……" with diss
    mc "我转过去，等你进了水里再说。"
    show c1p4b2s1 3
    soul "那樣就毁掉这一切的意义了。" with diss
    soul "我们得建立信任。"
    soul "还有什么比分享彼此最私密的部分更好的办法呢？"
    show c1p4b2s1 4
    mc "我们才刚认识！" with diss
    mc "不能做{i}那种事{/i}！"
    show c1p4b2s1 5
    soul "哦，你这位正人君子。" with diss
    show c1p4b2s1 6
    soul "我不是那个意思。" with diss
    show c1p4b2s1 7
    mc "所以我们真的要一起裸泳？" with diss
    show c1p4b2s1 8
    soul "只是裸泳。" with diss
    soul "不发生关系。"
    soul "我以我的名誉担保。"
    show c1p4b2s1 9
    mc "好吧，随便。" with diss
    mc "我加入。"
    play bgm "bgm/Forget Me Not.ogg" fadein 1.5
    show c1p4b2s1 10
    soul "很好。" with diss
    show c1p4b2s1 11
    soul "现在仔细看……" with diss
    show c1p4b2s1 12
    soul "……每一处精细的……" with diss
    play sfx "sfx/Cloth3.ogg"
    show c1p4b2s1 13
    soul "……我身体的……" with diss
    show c1p4b2s1 14
    soul "……每一部分。" with diss
    show c1p4b2s1 15
    mc "（该死……！）" with diss
    mc "（她根本没有理由这么性感。）"
    play sfx "sfx/Water - Walk.ogg"
    show c1p4b2s1 16 with diss
    pause 1.0
    play sfx "sfx/Water - Wade.ogg"
    show c1p4b2s1 17
    soul "怎么样？" with diss
    soul "你要进来吗？"
    show c1p4b2s1 18
    mc "嗯——呃——再等一下。" with diss
    mc "我需要一秒钟——呃——做点……心理准备。"
    play sfx "sfx/Water - Move.ogg"
    show c1p4b2s1 19
    soul "我从这儿就看得见你的勃起了。" with diss
    soul "没必要害羞。"
    play sfx "sfx/Water - Move2.ogg"
    show c1p4b2s1 20
    soul "我知道自己很性感。" with diss
    show c1p4b2s1 21
    mc "那也没必要藏了。" with diss
    play sfx "sfx/Cloth3.ogg"
    show c1p4b2s1 22 with diss
    pause 1.0
    show c1p4b2s1 23
    soul "（真要命……）" with diss
    soul "（我{i}真的{/i}后悔说不做爱了。）"
    show c1p4b2s1 24 with diss
    pause 1.0
    play sfx "sfx/Water - Jump In.ogg"
    show c1p4b2s1 25 with hpunch
    pause 1.0
    show c1p4b2s1 26
    soul "这才像话！" with diss
    show c1p4b2s1 27
    mc "你的妆现在全花了。" with diss
    mc "对不起。"
    show c1p4b2s1 28
    soul "嗯，这也在预料之中。" with diss
    show c1p4b2s1 29
    soul "毕竟我们是在水里。" with diss
    show c1p4b2s1 30
    mc "也是。" with diss
    mc "我只是觉得你刚才好像很在意妆会不会花。"
    show c1p4b2s1 31
    soul "不，其实不是。" with diss
    show c1p4b2s1 32
    soul "现在看起来怎么样？" with diss
    show c1p4b2s1 33
    mc "你很美。" with diss
    mc "我是说——呃……"
    play sfx "sfx/Water - Move.ogg"
    show c1p4b2s1 34
    soul "谢谢，[mc_name]。" with diss
    show c1p4b2s1 35
    soul "你真贴心。" with diss
    show c1p4b2s1 36
    mc "呃……" with diss
    show c1p4b2s1 37
    soul "怎么了？" with diss
    show c1p4b2s1 38
    mc "你——呃——没穿衣服……" with diss
    mc "而且你还碰着我。"
    show c1p4b2s1 39
    soul "所以？" with diss
    show c1p4b2s1 38
    mc "感觉你像是想勾引我。" with diss
    show c1p4b2s1 37
    soul "别担心。" with diss
    soul "我本来会的……但我没有。"
    show c1p4b2s1 38
    mc "你会对一个完全陌生的人那样做？" with diss
    play sfx "sfx/Water - Move2.ogg"
    show c1p4b2s1 40
    soul "又不是第一次了。" with diss
    soul "虽然我以前只干过一次，而且结果不太如我的意。"
    show c1p4b2s1 41
    mc "哇，真的吗？" with diss
    mc "出了什么事？"
    show c1p4b2s1 42
    soul "他把我的热情当成了我很随便。" with diss
    show c1p4b2s1 43
    soul "不过他活该，毕竟我连做爱都没做过。" with diss
    show c1p4b2s1 44
    mc "这话题真是越来越私密了。" with diss
    show c1p4b2s1 45
    soul "就是这样。" with diss
    show c1p4b2s1 46
    soul "好了，我分享完了。" with diss
    soul "现在轮到你了。"
    soul "你和多少人上过床？"
    show c1p4b2s1 47
    mc "只有一个。" with diss
    show c1p4b2s1 48
    soul "哦，真的？" with diss
    soul "所以你才这么紧张？"
    soul "你没经验？"
    show c1p4b2s1 49
    mc "才不是，绝对不是。" with diss
    mc "我是只跟一个人做过，不是只做过一次。"
    show c1p4b2s1 48
    soul "所以……是女朋友？" with diss
    soul "还是，等等……"
    show c1p4b2s1 50
    soul "{i}*倒吸一口气*{/i}" with diss
    soul "你是同性恋？！"
    show c1p4b2s1 51
    mc "都不是。" with diss
    mc "我单身，也绝对不是同性恋。"
    show c1p4b2s1 52
    soul "那你真是个有底线的男人？" with diss
    show c1p4b2s1 53
    mc "差不多吧。" with diss
    mc "我只是有些理由没法说，所以做那种事会让我不舒服。"
    show c1p4b2s1 46
    soul "你知道，为了做而做也没什么不对。" with diss
    soul "反正你又不会跟睡过的人绑定一辈子。"
    show c1p4b2s1 48
    soul "毕竟我们都有需求。" with diss
    show c1p4b2s1 53
    mc "我是说，没错……" with diss
    mc "这点你说得对。"
    show c1p4b2s1 45
    soul "有时候让欲望赢一次也没什么。" with diss
    show c1p4b2s1 53
    mc "我可做不到那样。" with diss
    show c1p4b2s1 54
    soul "你认真的？" with diss
    show c1p4b2s1 55
    soul "不过是找点{i}乐子{/i}而已。" with diss
    soul "你总得偶尔活一下。"
    show c1p4b2s1 41
    mc "……" with diss
    show c1p4b2s1 56
    soul "对不起……" with diss
    show c1p4b2s1 57
    soul "我们换个话题吧？" with diss
    show c1p4b2s1 58
    mc "你不用道歉。" with diss
    mc "我只是不习惯这么直接的对话。"
    show c1p4b2s1 45
    soul "从俱乐部就该看出来了，我是个很直接的人。" with diss
    show c1p4b2s1 44
    mc "哦，这我确实看出来了。" with diss
    show c1p4b2s1 48
    soul "总之，我们开始练习吧？" with diss
    stop bgm fadeout 1.5
    hide c1p4b2s1 with diss
    pause 1.0
    return

label rayn_gettinwet:
    show c1p6b1s1 1
    hide c1p6s5
    mc "哦，好吧。" with diss
    show c1p6b1s1 2
    rayn "就这样？" with diss
    rayn "被人看光了也不觉得难为情？"
    show c1p6b1s1 3
    mc "不觉得。" with diss
    mc "我没什么好难为情的。"
    mc "嗯……也许只有对{i}下面那家伙{/i}的控制力……有点。"
    show c1p6b1s1 4
    rayn "嗯？" with diss
    play bgm "bgm/Passion of Champions.ogg" fadein 3.0
    show c1p6b1s1 5
    rayn "哦，天哪！" with hpunch
    rayn "阿斯塔拉还真没开玩笑！"
    rayn "你一直在下面藏了个怪物。"
    show c1p6b1s1 6
    rayn "这种东西不该一直关在笼子里，你知道吧？" with diss
    show c1p6b1s1 7
    rayn "关起来的野兽往往会变得温顺，忘了怎么在野外生存。" with diss
    show c1p6b1s1 8
    rayn "或者……" with diss
    show c1p6b1s1 9
    rayn "……或者变得如此狂暴，以至于{i}再也驯服不了{/i}。" with diss
    show c1p6b1s1 10
    mc "你在干什么？" with diss
    show c1p6b1s1 11
    mc "你知道吗？" with diss
    mc "管他的。"
    mc "你既然这么想要，那就拿去吧。"
    show c1p6b1s1 12 with diss
    pause 1.0
    show c1p6b1s1 13
    mc "嗯……" with diss
    show c1p6b1s1 14
    mc "你尽管拿去……" with diss
    show c1p6b1s1 16 with diss
    pause 1.0
    show c1p6b1s1 15
    rayn "你喜欢这样吗？" with diss
    show c1p6b1s1 17 with diss
    pause 1.0
    show c1p6b1s1 18
    mc "（真不敢相信我居然让这种事了。）" with diss
    mc "（不过我现在倒是不后悔。）"
    show c1p6b1s1 v1 with diss
    pause
    mc "你真擅长这个，雷恩。" with diss
    rayn "{i}嗯哼……{/i}" with diss
    mc "你再这样……我撑不了多久了。" with diss
    rayn "{i}嗯……{/i}" with diss
    show c1p6b1s1 19
    rayn "很好。" with diss
    rayn "我想感受它洒满我全身……"
    show c1p6b1s1 20
    rayn "尝一尝应该也不错……" with diss
    show c1p6b1s1 v2 with diss
    pause
    mc "（哦，操……）" with diss
    mc "（她现在又快又深……）"
    mc "我快到了……就快了……" with diss
    menu:
        "射在她嘴里。":
            show c1p6b1s1 21 with dism
            pause 1.0
            show c1p6b1s1 22 with hpunch
            pause 0.3
            show c1p6b1s1 23 with hpunch
            pause 0.3
            show c1p6b1s1 24
            rayn "{i}*噗{/i}" with hpunch
            rayn "（好多！）"
            show c1p6b1s1 25 with diss
            pause 1.0
            show c1p6b1s1 26 with dism
            pause 1.0
        "射在她胸上。":
            show c1p6b1s1 27 with dism
            pause 1.0
            show c1p6b1s1 28 with hpunch
            pause 0.3
            show c1p6b1s1 29 with hpunch
            pause 0.3
            show c1p6b1s1 30
            rayn "我的天，老兄！" with diss
    show c1p6b1s1 31
    rayn "那些东西到底是打哪儿来的？！" with diss
    rayn "你憋了挺久了吧？"
    show c1p6b1s1 32
    mc "算是吧，但又不完全是。" with diss
    mc "我一直都这样。"
    show c1p6b1s1 33
    rayn "嘶——！" with diss
    rayn "你之后的清理工作一定很痛苦。"
    show c1p6b1s1 34
    mc "有时候吧。" with diss
    play sfx "sfx/Shower - Off.ogg"
    stop sfx2 fadeout 1.0
    show c1p6b1s1 35 with diss
    pause 1.0
    show c1p6b1s1 36
    mc "你干嘛拔掉？" with diss
    show c1p6b1s1 37
    rayn "因为不用的话，水费就白交了。" with diss
    show c1p6b1s1 38
    mc "我还没完——" with diss
    show c1p6b1s1 39 with hpunch
    pause 1.0
    play sfx "sfx/Door - Shower - Quick.ogg"
    show c1p6b1s1 40 with hpunch
    pause 1.0
    show c1p6b1s1 41 with diss
    pause 1.0
    show c1p6b1s1 42 with diss
    pause 1.0
    show c1p6b1s1 43
    rayn "{i}*压低声音* 像刚才那样按住我……{/i}" with diss
    show c1p6b1s1 44 with diss
    pause 1.0
    play sfx "sfx/Table - Slam.ogg"
    show c1p6b1s1 45 with hpunch
    pause 1.0
    show c1p6b1s1 46
    rayn "嗯……{bt=2}{i}对哦{/i}{/bt}……！" with diss
    show c1p6b1s1 47
    rayn "现在就用你那怪物狠狠干我……" with diss
    show c1p6b1s1 48 with diss
    pause 1.0
    show c1p6b1s1 49 with diss
    pause 1.0
    stop bgm
    play sfx "sfx/Record Scratch.ogg"
    show c1p6b1s1 50
    sila "哇哦！" with hpunch
    sila "我可不想看到这种场面！"
    play sfx "sfx/Swipe.ogg"
    show c1p6b1s1 51
    toge "塞拉斯！" with hpunch
    show c1p6b1s1 52
    sila "没错！" with diss
    sila "我正准备去{i}男{/i}更衣室换衣服。"
    show c1p6b1s1 53
    rayn "对不起……" with diss
    show c1p6b1s1 54
    mc "我也是。" with diss
    mc "我们该换个地方……"
    show c1p6b1s1 55
    sila "别道歉。" with diss
    sila "我很高兴你认真听进了我的建议——"
    show c1p6b1s1 56
    sila "——但是，老兄，在更衣室里？" with diss
    sila "这下我坐哪儿都要提心吊胆了！"
    show c1p6b1s1 57
    rayn "我们可是在淋浴间开始的，这么想你好受点。" with diss
    show c1p6b1s1 58
    sila "嗯，那还好……" with diss
    sila "不过这也太尴尬了，我还是等你们两个弄完再进来吧。"
    play sfx "sfx/Footsteps - Tile.ogg"
    show c1p6b1s1 59 with diss
    pause 1.0
    show c1p6b1s1 60
    rayn "我不知道你怎么想，反正这感觉全没了。" with diss
    show c1p6b1s1 61 with diss
    pause 1.0
    mc "是啊……" with diss
    mc "我也是。"
    show c1p6b1s1 62
    rayn "别那么失落嘛……" with diss
    show c1p6b1s1 63
    rayn "……因为我{i}一定{/i}会——" with diss
    show c1p6b1s1 64
    rayn "——{i}迟早{/i}被你狠狠干一次的。" with diss
    rayn "不过看来不是今天。"
    show c1p6b1s1 65
    mc "哦，真的？" with diss
    mc "我还不能自己做主吗？"
    show c1p6b1s1 66
    rayn "你能。" with diss
    show c1p6b1s1 67
    rayn "不过我很确定，你已经把自己的意愿表达得{i}非常清楚{/i}了。" with diss
    show c1p6b1s1 68
    mc "是啊，你说得对。" with diss
    show c1p6b1s1 69
    rayn "穿好衣服，然后告诉塞拉斯现在可以进来了。" with diss
    stop bgm fadeout 1.0
    hide c1p6b1s1
    scrn "几分钟后……" with diss
    return

label laylconfess:
    play bgm "bgm/Late Night Cravings.ogg" fadein 1.0
    show c1p7b1s1 1 with diss
    hide c1p7s2
    pause 1.0
    play sfx "sfx/Cloth.ogg"
    show c1p7b1s1 2 with diss
    pause 1.0
    play sfx "sfx/Cloth2.ogg"
    show c1p7b1s1 3 with hpunch
    pause 1.0
    mc "你确定这真的是你想要的吗？" with diss
    show c1p7b1s1 4
    layl "嗯。" with diss
    layl "我确定。"
    play sfx "sfx/Cloth3.ogg"
    show c1p7b1s1 5 with diss
    pause 1.0
    show c1p7b1s1 6 with diss
    pause 1.0
    show c1p7b1s1 7
    layl "啊，好。" with diss
    layl "终于！"
    show c1p7b1s1 v1 with diss
    pause 1.0
    mc "要是想换个节奏，告诉我。" with diss
    layl "这——呃——这样就挺好的……暂时。" with diss
    mc "好。" with diss
    pause
    show c1p7b1s1 8
    layl "好……" with diss
    layl "再快一点。"
    show c1p7b1s1 9
    mc "没问题。" with diss
    show c1p7b1s1 v2 with diss
    pause 1.0
    layl "嗯嗯……对……" with diss
    layl "就是这样。"
    mc "（她真的很享受。）" with diss
    mc "（她微微扭动的样子还挺可爱的。）"
    layl "就这样保持下去……保持这个速度……" with diss
    mc "你喜欢这样吗？" with diss
    layl "哦哦，好喜欢。" with diss
    layl "喜欢死了……"
    pause
    mc "（她现在变得更湿了。）" with diss
    mc "（我敢说她很快就要到了。）"
    mc "（也许我该再加一点点。）"
    show c1p7b1s1 v3 with diss
    pause 1.0
    layl "{bt=2}我、操……{/bt}" with diss
    layl "{bt=2}就是……这样……{/bt}"
    layl "{bt=2}啊啊……{/bt}"
    pause
    layl "{bt=2}我要——哦——要去了……好、好厉害……{/bt}" with diss
    layl "{bt=2}别、别……{/bt}"
    layl "{bt=2}不要——啊——停……{/bt}"
    mc "（她现在激烈地在我手指上磨蹭。）" with diss
    mc "（我知道她有点小淫荡，但没想到会是这样。）"
    play sfx "sfx/Magic - Zap.ogg"
    show c1p7b1s1 10 with hpunch
    pause 0.5
    show c1p7b1s1 11
    layl "{shader=jitter}呃嗯！{/shader}" with diss
    show c1p7b1s1 12
    layl "刚、刚才是……怎么回事？" with diss
    show c1p7b1s1 13
    mc "我不知道。" with diss
    mc "我想我的魔力可能从指尖涌出来了一点。"
    show c1p7b1s1 14
    layl "是你让它那样的吗？" with diss
    show c1p7b1s1 15
    mc "不是。" with diss
    show c1p7b1s1 16
    layl "你能做到吗？" with diss
    show c1p7b1s1 17
    mc "哦，你喜欢吗？" with diss
    show c1p7b1s1 18
    layl "嗯。" with diss
    layl "其实……非常喜欢。"
    show c1p7b1s1 19
    mc "是吗。" with diss
    mc "我看看这次能不能故意做到。"
    show c1p7b1s1 20
    mc "（天哪，她真没开玩笑。）" with diss
    mc "（刚才那一下就让她湿得滴到椅子上了。）"
    show c1p7b1s1 21
    mc "我来了。" with diss
    play sfx "sfx/Magic - Zap.ogg"
    show c1p7b1s1 22 with diss
    pause 0.3
    show c1p7b1s1 23
    layl "{bt=2}操——对！{/bt}" with diss
    show c1p7b1s1 24
    layl "{bt=2}呃啊啊！{/bt}" with diss
    show c1p7b1s1 25 with hpunch
    pause 0.5
    show c1p7b1s1 26 with diss
    pause 0.5
    stop bgm fadeout 3.0
    show c1p7b1s1 27
    layl "刚才……那、那个……" with diss
    layl "……太棒了……"
    show c1p7b1s1 28
    layl "我现在……要睡得……像块石头一样。" with diss
    show c1p7b1s1 29
    mc "就在这儿？" with diss
    mc "你不先清理一下吗？"
    show c1p7b1s1 28
    layl "太累了……" with diss
    layl "睡醒再弄。"
    show c1p7b1s1 29
    mc "打算睡在自己的汁液里？" with diss
    mc "还挺性感。"
    show c1p7b1s1 30
    layl "嗯……" with diss
    layl "谢谢你让我这么舒服。"
    show c1p7b1s1 31
    mc "不客气。" with diss
    mc "好好睡，莱拉。"
    show c1p7b1s1 30
    layl "你也是。" with diss
    hide c1p7b1s1 with diss
    return
