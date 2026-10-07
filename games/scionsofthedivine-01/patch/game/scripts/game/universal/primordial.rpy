label primordial1:
    play bgm "bgm/Primordial.ogg" fadein 1.0
    $ effect_color = '#a000d1'
    show primordial1 1 with diss
    show smoke_effect
    show magic_effect at colored_ember
    pause 1.0
    show primordial1 2
    mc "（我在哪儿？）" with diss
    show primordial1 3
    mc "（我感觉……不太一样了。）" with diss
    mc "（等等……我的血管以前也这样发过光吗？）"
    mc "（一定是因为我血液里的魔力。）"
    show primordial1 4 with diss
    pause 1.0
    mc "（那是什么？！）" with diss
    play sfx2 "sfx/Whoosh.ogg"
    show primordial1 5 with diss
    pause 1.0
    show primordial1 6
    prim "战争就要来了……" with diss
    prim "你必须唤醒你真正的力量。"
    prim "如果你不肯……"
    prim "你会死。"
    stop bgm fadeout 1.5
    play sfx "sfx/Whoosh - Long.ogg"
    hide smoke_effect
    hide magic_effect
    hide primordial1 with dism
    stop bgm fadeout 1.0
    pause 1.0
    return

label primordial2:
    play bgm "bgm/Primordial.ogg" fadein 1.0
    $ effect_color = '#a000d1'
    show primordial2 1 with diss
    show smoke_effect
    show magic_effect at colored_ember
    pause 1.0
    show primordial2 2
    mc "（又是这个地方？）" with diss
    show primordial2 3
    mc "（哇！）" with diss
    mc "（那是什么东西？）"
    show primordial2 4
    prim "或许现在你明白了。" with diss
    prim "你需要这份力量。"
    prim "接受它！"
    prim "接受它，否则你会死。"
    mc "我不明白你在说什么。" with diss
    prim "他不理解？" with diss
    prim "我的语言是否已随时间失传？"
    prim "无所谓了。"
    prim "下次我们交谈时，我自会掌握你们的语言。"
    mc "（看来跟它沟通也没什么意义。）" with diss
    mc "（它还是听不懂我说话。）"
    show primordial2 5
    prim "但至少这一点，无需理解。" with diss
    prim "以创生之虚空为食！"
    prim "你的潜能必须实现！"
    play sfx "sfx/MC Magic - PowerUp.ogg"
    show primordial2 6 with hpunch
    pause 1.0
    show primordial2 7 with hpunchs
    stop sfx fadeout 1.0
    show primordial2 8
    mc "那感觉……太爽了！" with diss
    show primordial2 9
    mc "我{i}好{/i}爽！" with diss
    show primordial2 10
    mc "你对我做了什么？" with diss
    show primordial2 11
    prim "我强化了你。" with diss
    prim "再一次回到时间之内那片土地吧。"
    hide smoke_effect
    hide magic_effect
    hide primordial2 with dism
    stop bgm fadeout 1.0
    pause 1.0
    return

label primordial3:
    play bgm "bgm/Primordial.ogg" fadein 1.0
    $ effect_color = '#a000d1'
    show primordial3 1 with diss
    show smoke_effect
    show magic_effect at colored_ember
    pause 1.0
    mc "（我就该想到，一睡下去又会来到这个地方。）" with diss
    mc "（现在能做梦、记住梦里的事，感觉真奇怪。）"
    prim2 "这不是梦。" with diss
    show primordial3 2
    mc "你读了我的想法？" with hpunch
    show primordial3 3
    mc "而且你还说出了真正的话！" with hpunch
    show primordial3 5
    prim2 "是的。" with diss
    prim2 "我花了些时间，学会你们一族现代的语言。"
    prim2 "现在我们可以有效沟通了。"
    show primordial3 4
    mc "太好了，因为我有一大堆问题想问。" with diss
    prim2 "一切都会按部就班的。" with diss
    prim2 "首先，我想告诉你一件事。"
    prim2 "我已经尝试警告你好几次了。"
    prim2 "每一次我都失败了……"
    show primordial3 6
    prim2 "战争就要来了，[mc_name]。" with diss
    prim2 "而你将在其中扮演关键的角色。"
    show primordial3 4
    mc "战争？" with diss
    mc "你是指和神裔之间的战争？"
    mc "别告诉我历史又要重演了……"
    prim2 "不只是神裔，也未必是重演。" with diss
    prim2 "这将是一场前所未见的战争。"
    prim2 "凡人已经发展出足以与神力匹敌、甚至凌驾其上的技术与进化。"
    prim2 "你们称为\"公司\"的许多组织，已研发出机器与变异手段，让凡人得以触及曾经不可能企及的高度。"
    prim2 "这便是神力重回神裔之上的原因。"
    mc "你怎么知道这一切的？" with diss
    prim2 "请原谅我。" with diss
    prim2 "我还没有正式介绍自己。"
    prim3 "我便是某些人所说的「原初者」。"
    prim3 "我的存在，早于你们整个宇宙。"
    mc "什么？！" with hpunch
    mc "这些信息一下子太多了……"
    prim3 "你此刻不必相信，也不必理解。" with diss
    prim3 "重要的是，你要变得更强。"
    mc "我要怎么做？" with diss
    play sfx "sfx/Whoosh.ogg"
    show primordial3 7
    prim3 "就用这个。" with diss
    show primordial3 8
    mc "我记得这东西，上次也出现过。" with diss
    show primordial3 9
    prim3 "这就是{i}源头{/i}。" with diss
    mc "什么的源头？" with diss
    show primordial3 10
    prim3 "一切的源头。" with diss
    show primordial3 11
    mc "好吧……" with diss
    mc "我要像上次那样站在这儿，等这东西劈我吗？"
    show primordial3 12
    prim3 "不。" with diss
    prim3 "这一次，你必须进入其中。"
    prim3 "如此，你将与一切相连——所有地方，所有时刻。"
    show primordial3 13
    mc "听起来像是准要犯偏头痛。" with diss
    show primordial3 12
    prim3 "若超出你的承受，我会强行将你拉出。" with diss
    show primordial3 13
    mc "我必须这么做吗？" with diss
    show primordial3 12
    prim3 "这是你变强的唯一途径。" with diss
    show primordial3 14
    mc "好吧，随便吧。" with diss
    play sfx "sfx/Astral - Warp.ogg"
    hide smoke_effect
    hide magic_effect
    stop bgm fadeout 1.0
    hide primordial3 with diss
    pause 1.0
    mc "哇！" with diss
    mc "里面只有一片虚空……"
    mc "就像我身处虚无之中一样。"
    show source 1 with diss
    pause 1.0
    mc "那道光是什么？" with diss
    play sfx "sfx/Whoosh - Long.ogg"
    show source 2
    mc "我又到哪儿了？" with diss
    play sfx "sfx/Source - Stinger.ogg"
    show source 3 with hpunch
    pause 0.2
    show source 4
    mc "呃啊！" with diss
    mc "我就知道！"
    mc "真、真·要命的偏头痛……"
    play sfx "sfx/Light - Ring.ogg"
    show source 5
    mc "呃啊！" with hpunch
    play sfx "sfx/Everything.ogg" loop
    show pls1 1 with fadew
    pause 0.3
    show pls1 5
    pause 0.3
    show pls1 8
    pause 0.3
    show pls1 29
    pause 0.3
    show pls2 1
    hide pls1
    pause 0.2
    show pls2 8
    pause 0.2
    show laylmem1 4
    hide pls2
    pause 0.2
    show laylmem1 12
    pause 0.2
    show sarapast 46
    hide laylmem1
    pause 0.2
    show sarapast 68
    pause 0.2
    show sarapast 69
    pause 0.2
    show sarapast 77
    pause 0.1
    show everything 5
    hide sarapast
    pause 0.1
    show laylmem2 6
    hide everything
    pause 0.1
    show laylmem2 10
    pause 0.1
    show c1p1s1 1
    hide laylmem2
    pause 0.1
    show c1p1s3 3
    hide c1p1s1
    pause 0.1
    show c1p1s4 7
    hide c1p1s3
    pause 0.05
    show c1p2s1 1
    hide c1p1s4
    pause 0.05
    show c1p2s1 10
    pause 0.05
    show c1p2s1 17
    pause 0.05
    show c1p2s2 17
    hide c1p2s1
    pause 0.05
    show c1p2s2 22
    pause 0.05
    show c1p2s3 2
    hide c1p2s2
    pause 0.05
    show c1p2s3 26
    pause 0.05
    show c1p2s3 34
    pause 0.05
    show c1p2s3 46
    pause 0.05
    show c1p3s1 18
    hide c1p2s3
    pause 0.05
    show c1p3s1 22
    pause 0.05
    show c1p3s2 19
    hide c1p3s1
    pause 0.01
    show c1p3s3 20a2
    hide c1p3s2
    pause 0.01
    show c1p3s4 5
    hide c1p3s3
    pause 0.01
    show c1p3s5 19
    hide c1p3s4
    pause 0.01
    show c1p3s5 37
    pause 0.01
    show c1p3s7 4
    hide c1p3s5
    pause 0.01
    show c1p4s1 26
    hide c1p3s7
    pause 0.01
    show c1p4s1 43
    pause 0.01
    show c1p4s1 57
    pause 0.01
    show c1p4s4 29
    hide c1p4s1
    pause 0.01
    show c1p4s5 6
    hide c1p4s4
    pause 0.01
    show c1p4s5 22a
    pause 0.01
    show c1p4s5 36
    pause 0.01
    show c1p4s6 3
    hide c1p4s5
    pause 0.01
    show c1p4s7 3
    hide c1p4s6
    pause 0.01
    show c1p4s7 20
    pause 0.01
    show c1p4s7 58
    pause 0.01
    show c1p4s8 3
    hide c1p4s7
    pause 0.01
    show c1p4s9 8
    hide c1p4s8
    pause 0.01
    show c1p4s9 57
    pause 0.01
    show c1p5s2 18
    hide c1p4s9
    pause 0.01
    show c1p5s3 28
    hide c1p5s2
    pause 0.01
    show c1p5s3 102
    pause 0.01
    show c1p5s4 50
    hide c1p5s3
    pause 0.01
    show c1p6s1 2
    hide c1p5s4
    pause 0.01
    show c1p6s2 10
    hide c1p6s1
    pause 0.01
    show c1p6s2 62
    pause 0.01
    show everything 6
    hide c1p6s2
    pause 0.01
    show everything 7
    pause 0.01
    show everything 8
    pause 0.01
    show everything 9
    pause 0.01
    show everything 10
    pause 0.01
    show c1p8s3 62
    hide everything
    pause 0.01
    show everything 12
    hide c1p8s3
    pause 0.01
    show everything 13
    pause 0.01
    show everything 14
    pause 0.01
    play sfx "sfx/Stinger - Serious.ogg"
    show everything 15 with hpunch
    pause 0.5
    stop sfx
    hide source
    hide everything with disl
    pause 3.0
    play bgm "bgm/Primordial.ogg" fadein 1.0
    show primordial3 15 with disl
    show smoke_effect
    show magic_effect at colored_ember
    pause 3.0
    show primordial3 16
    prim3 "你活下来了。" with diss
    show primordial3 17
    mc "是啊……" with diss
    show primordial3 18
    mc "刚才那一堆到底是什么鬼！？" with hpunch
    show primordial3 19
    prim3 "一切。" with diss
    show primordial3 20
    prim3 "你的存活让我看到了莫大的希望。" with diss
    prim3 "你是第一个。"
    show primordial3 18
    mc "第一个什么？" with diss
    show primordial3 19
    prim3 "第一个活下来的人。" with diss
    prim3 "现在我送你回你的世界。"
    show primordial3 18
    mc "等等！" with diss
    mc "我还有更多问——"
    hide smoke_effect
    hide magic_effect
    stop bgm fadeout 1.0
    play sfx "sfx/Whoosh - Long.ogg"
    show primordial3 21
    mc "——题……" with diss
    show primordial3 22
    mc "搞什么啊，老兄！？" with diss
    show primordial3 23
    mc "（我得去找阿斯塔拉，问问她这一切是怎么回事。）" with diss
    mc "（也许她能给我一些答案。）"
    hide primordial3 with diss
    pause 1.0
    return
