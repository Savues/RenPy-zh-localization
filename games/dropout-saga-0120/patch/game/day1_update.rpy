label day1_update:
    play music "audio/shower.ogg" fadein 4
    scene black
    with Dissolve (2)
    pause (1)
    scene day1_1
    with Dissolve (1)
    sophia "*咯咯笑着*"
    scene day1_2
    with dissolve
    sophia "要不要带[ava]出去吃点东西？市政厅附近有家很棒的餐厅，菜色特别棒。"
    sophia "或者带她去看看桥底下的那个地方。" 
    sophia "上次那场枪战之后，我们确实没怎么好好陪过她。"
    sophia "毕竟她还是个普通人，过不惯我们这种日子。"
    scene day1_3
    with dissolve
    sophia "你觉得呢，[nickname_sophia1]？"
    sophia "我们可以去吗？"
    r1 "当然可以，我完全没理由说不！"
    scene day1_4
    with dissolve
    sophia "太好了！谢谢！"
    scene day1_5
    with dissolve
    sophia "你最好了！"
    scene day1_6
    with dissolve
    r1 "嗯，我觉得确实是。"
    scene day1_7
    with dissolve
    sophia "你这个小丑！"
    play sound "audio/doorbell.ogg"
    scene day1_8
    with dissolve
    pause
    play music "audio/suspensesoundtrack1.ogg"
    scene day1_9
    with dissolve
    sophia "你在等客人吗？"
    r1 "没有。"
    scene day1_10
    with dissolve
    ava "哦不，走错门了。"
    ava "这里是……"
    play sound "audio/shortwhistle.ogg" volume 0.3
    scene day1_11
    pause
    scene day1_12
    with dissolve
    r1 "{size=-7}{i}没事吧？{/i}{/size}"
    scene day1_13
    with dissolve
    pause
    scene day1_14
    with dissolve
    pause
    "???" "是他吗？"
    scene day1_15
    with dissolve
    "???" "我能跟他说几句话吗？很快就好，我保证。"
    scene day1_10
    with dissolve
    ava "可是这里没有叫……的人……"
    scene day1_15
    with dissolve
    "???" "实在抱歉。我有时候会记错要找的人的名字。"
    "???" "这里是[r1]先生的家吗？"
    scene day1_16
    with dissolve
    r1 "你是哪位？"
    scene day1_17
    with dissolve
    pause
    scene day1_18
    with dissolve
    "???" "你身上的纹身挺有意思。"
    scene day1_19
    with dissolve
    "???" "我太失礼了，抱歉。"
    nor "我叫[nor]，刚才还在和你太太说话。"
    nor "抱歉，夫人，我没听清您的名字。"
    scene day1_16
    with dissolve
    ava "啊，我叫……"
    scene day1_20
    with dissolve
    r1 "她叫黛丝。"
    ava "她叫……"
    scene day1_21
    with dissolve
    "你轻轻拍了拍{color=#FF007F}[ava]{/color}的肩膀。"
    scene day1_23
    with dissolve
    pause
    scene day1_22
    with dissolve
    pause
    scene day1_24
    with dissolve
    ava "我马上回来。"
    scene day1_25
    with dissolve
    sophia "是谁啊，亲爱的？"
    scene day1_19
    with dissolve
    nor "久仰大名，[r1]先生。关于您的事我可是听过不少。"
    if police == 0:
        nor "尤其是听说我的部下在这座城市最负盛名的学府吃了闭门羹之后。" 
        nor "您可以想象我有多震惊。" 
    nor "我是警察局长。"
    nor "我儿子跟您提起过不少次。"
    nor "不过我不认为他那样说您是公允的。"
    nor "您也知道，如今的孩子嘴上没个把门的。"
    scene day1_26
    with dissolve
    r1 "你儿子已经不再是个孩子了。"
    scene day1_19
    with dissolve
    nor "在父亲眼里，儿子永远都是孩子。"
    nor "我能进来吗？我们可以聊聊。"
    scene day1_26
    with dissolve
    r2 "(冷静点，别剑拔弩张。)"
    r2 "(记住，我们只是校方的人。)"
    scene day1_27
    with dissolve
    r1 "当然，长官。久仰。"
    scene day1_28
    with dissolve
    r1 "我这副模样实在失礼了，没想到您会来。"
    r1 "我刚在洗澡。"
    scene day1_29
    with dissolve
    nor "哪里的话！我们都是男人，不是吗？"
    nor "只要您太太不吃醋。"
    nor "况且，我再怎么也不会去评判一个男人在自己家里怎么穿衣服。要怪就怪我没先打电话。"
    nor "不过您得体谅，我的日程排得很满。"
    r1 "我们进去谈吧。您能等我一分钟，让我把衣服穿上吗？"
    nor "当然！"
    scene black
    with Dissolve (2)
    pause (1)
    scene day1_30
    with Dissolve (1)
    nor "我又要为这突如其来的到访道歉了。"
    scene day1_31
    with dissolve
    r1 "没关系。"
    r1 "不过，您本来可以先给办公室打电话的。"
    scene day1_30
    with dissolve
    nor "您要说我老派，但有时候我们确实需要当面谈。"
    scene day1_32
    with dissolve
    pause
    r1 "我明白了。"
    r1 "那么，是什么风把您吹来了？"
    scene day1_33
    with dissolve
    nor "想必您已经从新闻里听说城那头万圣节派对上发生的事了吧。"
    scene day1_32
    with dissolve
    r1 "听说了。"
    scene day1_33
    with dissolve
    nor "太好了，那我就不必多费口舌。"
    nor "您看，我这局长的工作有不少规矩是不能马虎的。"
    nor "公共安全当然是我们第一要务！"
    nor "让未来的栋梁感受到警方的守护与庇护，这很重要。您说是不是？"
    nor "让大家安心相信这套体系运转正常、我们会竭尽全力终结那帮在我们安宁小城开枪的人——这很重要。"
    scene day1_32
    with dissolve
    r1 "『……「解决」……？』"
    scene day1_33
    with dissolve
    nor "当然是把他们抓起来！"
    nor "不管怎样，我相信您理解眼下派几名警员守护学校的必要性。"
    nor "我们可不想那边出什么事，对吧？"
    scene day1_32
    with dissolve
    r2 "(普通校方的人会怎么回答呢……？)"
    r1 "(我不喜欢这样。)"
    r2 "(我们没有退路，只能认下这个局面。)"
    r2 "(以后也许还有翻盘的机会。)"
    scene day1_34
    with dissolve
    r1 "我理解，而且没什么不能接受的。"
    r1 "不过您也得理解，我这份工作同样有些规矩不能忽视。"
    r1 "警员来太多会引起恐慌。学生可能会以为学院成了下一个目标。"
    scene day1_35
    with dissolve
    pause
    scene day1_33
    with dissolve
    nor "我可不想在这个节骨眼上给您添麻烦。"
    nor "那派两名警员呢？不能再多了。"
    nor "这样可以吗？"
    scene day1_32
    with dissolve
    r2 "(我们别无选择。拒绝只会引出太多疑问。)"
    scene day1_34
    with dissolve
    r1 "可以，没问题。"
    scene day1_30
    with dissolve
    nor "太好了！"
    nor "话说回来，我怎么以前从没听说过您？"
    nor "您是本地人吗？"
    scene day1_36
    with dissolve
    ava "不好意思，打扰一下，实在抱歉。"
    scene day1_37
    with dissolve
    ava "我刚在煮咖啡。两位要来一杯吗？"
    ava "我也可以泡茶。"
    scene day1_38
    with dissolve
    nor "谢谢您，夫人，您太客气了。"
    nor "不过您这一提醒，我才想起我约了市长喝咖啡。"
    scene day1_39
    with dissolve
    nor "改天我非常希望能和您好好聊聊，[r1]先生。"
    nor "希望是在更合适的场合。下次通个电话怎么样？"
    r1 "荣幸之至，局长。"
    r1 "我送您出去。"
    scene day1_40
    with dissolve
    pause
    scene day1_41
    with dissolve
    pause
    scene day1_42
    with dissolve
    pause
    scene day1_43
    with dissolve
    pause
    scene day1_44
    with dissolve
    pause
    scene day1_45
    with dissolve
    pause
    nor "哦对了，在我走之前。"
    scene day1_19
    with dissolve
    nor "不得不说，[r1]先生，您这个纹身很有意思。"
    nor "看着眼熟，但我想不起是在哪儿见过了。"
    nor "或许是现在孩子们玩的那种游戏里的？"
    nor "没想到这么年轻的人能当上校长。"
    nor "您身上肯定有过人之处，我很确定。"
    nor "那么……今天很愉快，祝您有美好的一天。"
    scene day1_46
    with dissolve
    r1 "该我说这句话。您也是。"
    scene day1_46
    play sound "audio/Open4.ogg"
    pause
    play sound "audio/hitwood1.ogg"
    scene day1_47
    with hpunch
    pause
    scene day1_48
    with dissolve
    r1 "去你的，[k]。"
    r1 "你到底把我拖进什么烂摊子里了？"
    scene black
    with Dissolve (2)
    pause (1)
    play sound "audio/Open5.ogg"
    pause (1)
    play sound "audio/Open4.ogg"
    stop music fadeout 2
    scene day1_49
    with Dissolve (1)
    pause
    scene day1_50
    with dissolve
    sophia "没事吧，[nickname_sophia1]？"
    scene day1_49
    with dissolve
    r1 "我没事。"
    r1 "只是饿了。"
    scene day1_51
    with dissolve
    ava "咖啡泡好啦——！！"
    scene day1_52
    with dissolve
    ava "你先在桌边坐一下，我给你端过去。"
    scene day1_53
    with dissolve
    pause
    scene day1_54
    with dissolve
    pause
    scene day1_55
    with dissolve
    pause
    scene day1_56
    with dissolve
    pause
    scene day1_57
    with dissolve
    r1 "什么？"
    scene day1_56
    with dissolve
    sophia "我觉得我应该得到比这更多的尊重。"
    scene day1_57
    with dissolve
    pause
    scene day1_58
    with dissolve
    r1 "不知道你在说什么。"
    scene day1_56
    with dissolve
    sophia "是吗？你就给我这种待遇？"
    scene day1_57
    with dissolve
    r1 "现在不行，[sophia]。"
    scene day1_59
    with dissolve
    ava "开——饭——啦——！"
    ava "我还做了培根！"
    scene day1_60
    with dissolve
    pause
    scene day1_61
    with dissolve
    pause
    scene day1_62
    with dissolve
    ava "怎么了？"
    scene day1_56
    with dissolve
    pause
    scene day1_57
    with dissolve
    r1 "什么都没发生。"
    scene day1_63
    with dissolve
    sophia "我不饿。"
    scene day1_64
    with dissolve
    r1 "[sophia]。"
    play sound "audio/Open5.ogg"
    scene day1_65
    with dissolve
    r1 "真是够了。"
    play sound "audio/Open4.ogg"
    scene day1_66
    with dissolve
    r1 "我马上回来。"
    scene black
    with Dissolve (2)
    pause (1)
    play sound "audio/Open5.ogg"
    pause (1)
    play sound "audio/Open4.ogg"
    scene day1_67
    with Dissolve (1)
    r1 "你到底有什么毛病？"
    scene day1_68
    with dissolve
    sophia "我的毛病？"
    scene day1_69
    with dissolve
    sophia "我的毛病是，今天还跟我同床睡，第二天就不肯告诉我到底发生了什么！"
    scene day1_70
    with dissolve
    sophia "又或者，像是让我照顾[ava]，好像你随时会消失一样，然后……"
    scene day1_71
    with dissolve
    sophia "我不知道……"
    scene day1_72
    with dissolve
    sophia "……差点让我们被一场枪战要了命。"
    scene day1_96
    with dissolve
    sophia "自打那场该死的破事之后，我们就一直低调行事，记得吗？"
    scene day1_73
    with dissolve
    sophia "现在有不三不四的人往家里跑。警察局长？！我们什么时候开始跟那种人打交道了？"
    scene day1_74
    with dissolve
    sophia "你还当着我的面说一切都好？好像我在这个圈子里待得还不够久，看不出有什么事正在发生似的？"
    scene day1_75
    with dissolve
    r1 "听着，我从来没说过我……"
    scene day1_76
    with hpunch
    sophia "我他妈很害怕，好吗？！"
    scene day1_77
    with dissolve
    pause
    scene day1_78
    with dissolve
    sophia "我已经失去过你一次了……{size=-7}你知道的{/size}？"
    scene day1_79
    with dissolve
    sophia "{size=-7}我、我再也承受不了第二次……{/size}"
    sophia "{size=-7}被丢下的那个人是我……上一次是……{/size}"
    scene day1_80
    with dissolve
    sophia "{size=-7}而现在，我又觉得你在一遍遍地把我推开。{/size}"
    sophia "我、我不能再失去你了。"
    sophia "我不能……我……"
    scene day1_81
    with dissolve
    pause
    scene day1_82
    with dissolve
    sophia "真是见鬼了。"
    sophia "我不要这样。"
    sophia "对不起，我……"
    scene day1_83
    with dissolve
    pause
    scene day1_84
    with dissolve
    pause
    scene day1_85
    with dissolve
    pause
    scene day1_86
    with dissolve
    sophia "都是眼睛里进了该死的东西。"
    sophia "我没事，我发誓。"
    scene day1_87
    with dissolve
    sophia "该死！"
    scene day1_88
    with dissolve
    sophia "*抽泣着* 对不起！"
    sophia "你不该看到我这副样子！"
    scene day1_89
    with dissolve
    sophia "给我一点时间！"
    scene day1_90
    with dissolve
    pause
    r1 "你从来没失去过我。"
    r1 "但你也知道我有时候只是个普通人。"
    scene day1_92
    with dissolve
    sophia "只是有时候。"
    scene day1_93
    with dissolve
    pause
    scene day1_91
    with dissolve
    sophia "抱歉，你继续。"
    scene day1_93
    with dissolve
    r1 "没关系。"
    scene day1_90
    with dissolve
    r1 "再说一次，你从来没失去过我。"
    r1 "我哪都不去。"
    r1 "我没有在推开你。"
    scene day1_91
    with dissolve
    sophia "但你以前做过一次。"
    scene day1_94
    with dissolve
    r1 "这不公平，[sophia]。"
    scene day1_95
    with dissolve
    sophia "对我来说也不公平。"
    sophia "我需要你。"
    scene day1_97
    with dissolve
    pause
    sophia "我想你了。"
    sophia "你们两个，我都想。"
    sophia "她死了……可离开的人是你。"
    scene day1_94
    with dissolve
    r1 "我现在在这儿。"
    scene day1_95
    with dissolve
    sophia "能待多久？"
    r1 "我不会走。"
    sophia "可要是你……{p=0.2}{nw}"
    r1 "我不。会。走。"
    scene day1_94
    with dissolve
    r1 "听着，很抱歉伤了你。"
    scene day1_95
    with dissolve
    sophia "不止一次。"
    scene day1_94
    with dissolve
    pause
    scene day1_95
    with dissolve
    pause 0.05
    scene day1_98
    with dissolve
    pause 0.05
    scene day1_95
    with dissolve
    pause 0.05
    scene day1_98
    with dissolve
    pause 0.05
    scene day1_95
    with dissolve
    pause
    scene day1_99
    with dissolve
    pause
    scene day1_100
    with dissolve
    sophia "对不起，我只是想缓一缓，别再哭了。"
    scene day1_101
    with dissolve
    r1 "我知道。"
    scene day1_102
    with dissolve
    pause
    scene day1_103
    with dissolve
    sophia "你得偶尔让我冲你发火。"
    r1 "那不可能。"
    scene day1_104
    with dissolve
    r1 "说真的。"
    r1 "我完全照顾得好自己。"
    r1 "你不再是个孩子了，但这不代表我就不该保护你、照顾你。"
    r1 "你可以说自己不需要保护，也不需要我照顾。但哪天要是你出了什么事，我绝不答应。"
    r1 "如果我有什么事没告诉你，要么是我自己还没想好该怎么办，要么是我觉得告诉你会让你陷入危险。"
    scene day1_105
    with dissolve
    pause
    scene day1_104
    with dissolve
    sophia "你是个笨蛋。"
    sophia "你以为我不知道？"
    sophia "[nickname_sophia1]，在意对方的可不止你一个。"
    sophia "失去过人的，也不只你一个。"
    sophia "我知道那是很久以前的事了，可感觉就像昨天才发生。"
    sophia "我也怕得要命会失去你，你这家伙。"
    scene day1_107
    with dissolve
    sophia "真是的！你又要把我弄哭了！"
    sophia "给我一分钟。"
    scene day1_105
    with dissolve
    pause
    scene day1_104
    with dissolve
    sophia "答应我，这件事我们一起扛。"
    sophia "还有，别再把我一个人丢下。"
    sophia "我只想知道，不管发生什么，我们都能一起找到办法。"
    scene day1_108
    with dissolve
    r1 "我答应你。"
    sophia "谢谢你，[nickname_sophia1]。"
    scene day1_109
    with dissolve
    r1 "过来吧。我们得去跟[ava]道歉。"
    r1 "她给我们做了早餐，然后我们就把她一个人晾在一边。"
    scene day1_110
    with dissolve
    sophia "唉，亲爱的。你说得对。"
    scene black
    with Dissolve (2)
    pause (1)
    play sound "audio/Open5.ogg"
    pause (1)
    play sound "audio/Open4.ogg"
    scene day1_111
    with Dissolve (1)
    pause
    scene day1_112
    with dissolve
    pause
    ava "你们没事吧？"
    scene day1_113
    with dissolve
    sophia "亲爱的，我……"
    sophia "我好对不……"
    scene day1_114
    with dissolve
    pause
    scene day1_115
    with dissolve
    ava "我只是想知道你还好不好。"
    scene day1_116
    with dissolve
    pause
    scene day1_117
    with dissolve
    sophia "我没事。"
    scene day1_118
    with dissolve
    sophia "其实……我不好。"
    scene day1_117
    with dissolve
    sophia "但我会好起来的。"
    scene day1_119
    with dissolve
    ava "那你不许喝咖啡。"
    scene day1_120
    with dissolve
    ava "我给你泡杯茶。"
    ava "喝了会舒服些。"
    scene day1_121
    with dissolve
    sophia "这次我们一起来弄，好不好？"
    scene day1_122
    with dissolve
    sophia "泡茶这种活就交给英国人吧，好吗？"
    stop music fadeout 2
    scene black
    with Dissolve (2)
    pause (1)
    scene day1_125
    with Dissolve(1)
    ava "那么……刚才那个男人是谁？"
    scene day1_126
    with dissolve
    pause
    scene day1_127
    with dissolve
    pause
    scene day1_128
    with dissolve
    pause
    scene day1_125
    with dissolve
    ava "所以……？"
    scene day1_127
    with dissolve
    r1 "警察局长。"
    play sound "audio/coughsophia.ogg"
    scene day1_129
    with hpunch
    pause
    stop sound
    scene day1_130
    with dissolve
    sophia "你是要……"
    scene day1_127
    with dissolve
    r1 "[ava]，你确定要卷进我们的生活吗？"
    scene day1_131
    with dissolve
    ava "怎么了？"
    scene day1_132
    with dissolve
    pause
    scene day1_133
    with dissolve
    r1 "*叹气* 呃……"
    r1 "我可真蠢。"
    scene day1_127
    with dissolve
    r1 "我犯了个错。"
    scene day1_134
    with dissolve
    sophia "[nickname_sophia1]……"
    scene day1_135
    with dissolve
    r1 "今天我们玩了一场危险的游戏。"
    r1 "这种事不能再有下次。"
    scene day1_136
    with dissolve
    r1 "所以我再问你一遍。"
    r1 "你真的确定要这样吗？"
    scene day1_137
    with dissolve
    ava "我不明白。"
    scene day1_136
    with dissolve
    r1 "我一直把你蒙在鼓里，以为这样是在保护你。"
    r1 "但其实不是。"
    r1 "事到如今继续瞒着你，比把真相告诉你更危险。"
    r1 "那天晚上是你自己告诉我的。"
    r1 "我只是没想到我们会这么快就走到这一步。"
    r1 "我以为慢慢让你接受，能让你没那么害怕。"
    r1 "但我错了。为此我道歉。"
    scene day1_137
    with dissolve
    ava "我还是跟不上。"
    scene day1_138
    with dissolve
    sophia "他的意思是，你……"
    scene day1_139
    r1 "我的意思是，你得学会在我不在的时候照顾好自己。"
    scene day1_140
    with dissolve
    r1 "这话对你也一样，[sophia]。"
    r1 "我不在、没法护着你们的时候，你们两个得互相照应。"
    scene day1_141
    with dissolve
    r1 "[ava]，我不太放心让你碰枪。"
    r1 "但你得知道该怎么做，才能让我和[sophia]保护你时更省力。"
    scene day1_136
    with dissolve
    r1 "我之所以住在林子附近，是有原因的。"
    r1 "我不喜欢有人来往。走这条路的人本来就很少。"
    r1 "如果我住在市中心，我的人生会完全不同。"
    r1 "所以有人按响我们家门铃，绝不会是走错。"
    r1 "不是什么上门卖曲奇的女童军。"
    r1 "知道我住在哪儿的人少之又少。"
    r1 "这次我毫无准备。而我不得不露面，是因为我以为你们可能有危险。"
    r1 "或者更糟，说出什么会把我们所有人都拖进危险的话。"
    r1 "他绝对不该看见我的纹身。我不能冒着浪费时间套件衬衫、而你趁机出事儿的风险。"
    r1 "我真的没那个时间。而那些让你先动手、后思考的局面，正是会要你命的。"
    r1 "我的纹身和狼群里其他人不一样。你可能没注意，我胸口烙的不是狼。"
    r1 "那是另有原因的。"
    scene day1_137
    with dissolve
    ava "那是……？"
    scene day1_136
    with dissolve
    r1 "这个改天再说。"
    scene day1_139
    with dissolve
    r1 "我的意思是……"
    scene day1_141
    with dissolve
    r1 "我一直小心把自己藏在暗处。"
    r1 "所以有人不请自来时，我们必须做最坏的打算。"
    r1 "也就是说，我们得有一套应急流程。"
    scene day1_140
    with dissolve
    r1 "我和[sophia]在一起时从不需要这套，因为要是开门的是她，她早就藏好一把手枪瞄着按门铃的人了。"
    scene day1_141
    with dissolve
    r1 "而且她肯定不会说什么危险的话。"
    scene day1_137
    with dissolve
    ava "那我该怎么办？"
    scene day1_141
    with dissolve
    r1 "第一，绝不要告诉任何人你的真名。"
    r1 "而且要前后一致。"
    r1 "在你不信任的人面前，你的名字现在是黛丝。因为我告诉那个男人的就是这个名字。"
    r1 "要是你碰到另一个用别的名字的警察，就会惹来一堆疑问。"
    scene day1_142
    with dissolve
    ava "明白了！"
    scene day1_143
    with dissolve
    ava "太刺激了！"
    scene day1_141
    r1 "这不是游戏！"
    scene day1_144
    with dissolve
    pause
    scene day1_145
    with dissolve
    pause
    scene day1_146
    with dissolve
    pause
    scene day1_147
    with dissolve
    r1 "天哪……好吧！"
    scene day1_139
    with dissolve
    r1 "我就当准你玩一会儿……"
    scene day1_141
    with dissolve
    r1 "但你必须明白，我告诉你的这些能救命。"
    r1 "必须当真。"
    scene day1_148
    with dissolve
    pause
    play music "audio/firstpastsoundtrack.ogg"
    scene day1_149
    with Dissolve(1)
    ava "对不起。"
    scene day1_141
    with Dissolve(1)
    pause
    scene day1_150
    with Dissolve(1)
    r1 "过来。"
    scene day1_151
    with Dissolve(1)
    r1 "我要告诉你一件事。"
    r1 "关于一个我和索菲娅曾经非常珍视的人。"
    scene day1_152
    with Dissolve(1)
    sophia "亲爱的？"
    scene day1_153
    with Dissolve(1)
    pause
    scene day1_154
    with Dissolve(1)
    r1 "[sophia]和我曾有一个对我们而言非常特别的人。"
    r1 "她叫[ingrid]。"
    scene day1_155
    with Dissolve(1)
    r1 "还记得你问起的那五大「家族」吗？"
    scene day1_156
    with Dissolve(1)
    ava "记得。"
    scene day1_157
    with Dissolve(1)
    r1 "她属于日耳曼那一族。"
    r1 "战后，是我保住了她的命。"
    r1 "那时候，我们还属于族群。"
    r1 "他们想杀她，说她是敌人。我让他们相信了相反的结论。"
    r1 "她因为战争而体弱带伤，丢下她一个人多半活不成。"
    r1 "我把她带到这里，叫来了[sophia]。我们俩一起照顾她，就像后来照顾你一样。"
    r1 "她和我住在这里，而[sophia]因为在英格兰还有些事，会偶尔来看我们。"
    r1 "日子久了，[sophia]来得越来越频繁。等我们意识到彼此的关系时，三个人已经住在一起了。"
    r1 "那是我第一次动了离开这种生活的念头。"
    scene day1_155
    with Dissolve(1)
    r1 "我很爱他们。有一天[ingrid]怀孕了。"
    r1 "我决定该退一步了。我把这个想法告诉了一个同伴，[k]。我们已经聊过他。"
    r1 "不过以防你不记得，他是我的队长。"
    r1 "我跟他说起[ingrid]怀孕的事时，当地政府截获了我们的对话。"
    r1 "我连「我想走」都没说，只说想退一步、想当个男人、想照顾我本该拥有的家庭。"
    r1 "他们还是决定把这条消息透露给族群的头领们。"
    r1 "族群绝不能冒失去对我的控制的风险。"
    scene day1_158
    with Dissolve(1)
    r1 "有一天晚上……"
    scene day1_153
    with Dissolve(1)
    r1 "[sophia]给我打电话，让我以最快速度回家。"
    r1 "[sophia]是医生，所以我以为孩子出事了。"
    r1 "结果发现是[ingrid]不见了。"
    r1 "于是我出去找她。"
    scene day1_156
    with Dissolve(1)
    ava "然后呢？"
    play sound "audio/heartbeat2.ogg"
    scene day1_159
    with redbulb
    r2 "他们埋伏了她。"
    r2 "然后杀了她。"
    scene day1_160
    sophia "对不起，我……"
    scene day1_161
    sophia "我、我听不下去了。"
    scene day1_162
    with Dissolve(1)
    sophia "我……我得走了。"
    scene day1_163
    with Dissolve(1)
    pause
    scene day1_164
    with Dissolve(1)
    r1 "你也得听。"
    scene day1_165
    with Dissolve(1)
    pause
    scene day1_166
    with Dissolve(1)
    sophia "*叹气*"
    scene day1_165
    with Dissolve(1)
    sophia "天哪，[r1]……"
    scene day1_167
    with Dissolve(1)
    r1 "对不起，这很重要。"
    r1 "我从没告诉过你。"
    scene day1_168
    with Dissolve(1)
    r2 "现在小心点。"
    r2 "我们可不想让他们知道这里还有某个人。"
    scene day1_169
    with Dissolve(1)
    pause
    scene day1_170
    with Dissolve(1)
    r1 "狼群和族群之所以分裂，责任在我。"
    r1 "那场战争的起因是[ingrid]的死。而我就是导火索。"
    r1 "他们多年前撒下的那颗小小种子——一场内战——起因竟是最大的理由。"
    scene day1_171
    with Dissolve(1)
    pause
    scene day1_172
    with Dissolve(1)
    pause
    scene day1_170
    with Dissolve(1)
    r1 "[ingrid]死的那晚，[k]他们不让我看她的遗体。"
    r1 "族群对外宣称是俄罗斯人干的。"
    r1 "希望我把注意力转到他们身上。"
    r1 "但现在狼群的掌权者找上了我。"
    r1 "他们告诉我真相，也承认并不知情、并不认同那次袭击。"
    r1 "我们所有人能活下去的唯一办法，就是永远先顾好自己人。"
    r1 "如果没有兄弟情谊，争权与贪婪迟早会把我们全都害死。"
    r1 "他们说[ingrid]是狼群的一员，你也是。"
    r1 "即便你身上没有我们的印记，你也受我们的庇护。"
    scene day1_171
    with Dissolve(1)
    r1 "从她死那天起，我就一直在怪自己。"
    play sound "audio/lightning.ogg"
    scene day1_173
    with flashbulb
    pause
    scene day1_174
    with Dissolve(1)
    k "兄弟，你最好别去看她。"
    scene day1_175
    with Dissolve(1)
    k "这不是你的错，[r1]。"
    scene day1_179
    with Dissolve(1)
    pause
    scene day1_175
    with Dissolve(1)
    k "我们会查出是谁下的手。"
    scene day1_176
    with Dissolve(1)
    r1 "她怀着孩子，[k]。"
    scene day1_177
    with Dissolve(1)
    pause
    k "我知道，兄弟。"
    scene day1_178
    with Dissolve(1)
    k "该死……"
    scene day1_179
    with Dissolve(1)
    pause
    scene day1_177
    with Dissolve(1)
    k "我送你回家。"
    scene day1_179
    with Dissolve(1)
    r1 "我不能回家。"
    scene day1_176
    with Dissolve(1)
    r1 "我怎么跟[sophia]说我们的孩子没了？"
    play sound "audio/lightning.ogg"
    scene day1_170
    with flashbulb
    r1 "我从来没原谅过自己。"
    scene day1_171
    with Dissolve(1)
    r1 "没有一天我不想过：如果她还活着，我们的生活会是什么样。"
    scene day1_180
    with Dissolve(1)
    pause
    scene day1_181
    with Dissolve(1)
    sophia "不是你的错。"
    scene day1_182
    with Dissolve(1)
    r1 "可还是……"
    scene day1_181
    with Dissolve(1)
    r1 "她是因为我才被杀的。"
    r1 "要是我当时闭嘴，她就不会死。"
    scene day1_170
    with Dissolve(1)
    r1 "她会平安无事。"
    r1 "我们也会有个孩子。"
    scene day1_171
    with Dissolve(1)
    r1 "[sophia]……战争那会儿……我做过一些无法想象的事。"
    r1 "哪怕按我们的标准来说。"
    scene day1_170
    with Dissolve(1)
    r1 "我走过一条满是仇恨的路，哪怕只见到当年那个我的一半，你也认不出我。"
    r1 "我不敢想，万一你们任何一个再出什么事会怎样。"
    scene day1_183
    with Dissolve(1)
    r1 "我只想让你们明白，我在拼尽全力保证你们的安全。"
    scene day1_184
    with Dissolve(1)
    r1 "但我的努力已经不够了。"
    scene day1_185
    with Dissolve(1)
    r1 "所以我不能再失去。"
    scene day1_186
    with Dissolve(1)
    r1 "我们得开始训练[ava]了。"
    r1 "我得为狼群办点事。"
    r1 "等我回来，我们教你们几招。"
    scene day1_187
    with Dissolve(1)
    r1 "[sophia]，把那支老步枪清理好准备好。"
    scene day1_188
    with Dissolve(1)
    r1 "我心意已决。"
    r1 "等我回来再详谈。"
    stop music fadeout 5
    scene black
    with Dissolve (2)
    pause (1)
    scene day1_123
    with Dissolve(1)
    pause
    scene day1_124
    with dissolve
    pause
    play sound "audio/beep.mp3"
    scene day1_189
    with dissolve
    pause
    scene day1_190
    with dissolve
    l_nvl "早——上——好，先生！"
    l_nvl "您今天来学院吗？日程排得很满。"
    menu:
        "看看她的头像。":
            scene lori_pfp
            with dissolve
            pause
        "继续聊天。":
            pause 0.001
    scene day1_190
    with dissolve
    r1_nvl "嗯，我几分钟就到。"
    l_nvl "好的！"
    l_nvl "谢谢您，先生！:)"
    nvl clear
    scene day1_191
    with dissolve
    pause
    scene day1_192
    with dissolve
    pause
    scene day1_193
    with dissolve
    pause
    scene day1_194
    with dissolve
    sophia "什——么？"
    scene day1_195
    with dissolve
    pause
    scene day1_196
    with dissolve
    pause
    scene day1_123
    with dissolve
    r1 "没什么。"
    scene day1_197
    with dissolve
    pause
    scene day1_198
    with dissolve
    sophia "我跟你说过我有多喜欢你刚才那样霸道吗？"
    scene day1_199
    with dissolve
    r1 "你就闭嘴吧。"
    scene day1_200
    with dissolve
    pause
    scene day1_201
    with dissolve
    r1 "你觉得她能做到吗？"
    scene day1_202
    with dissolve
    sophia "她比看起来坚强多了，[nickname_sophia1]。"
    scene day1_203
    with dissolve
    sophia "她有的是机会走。"
    sophia "那天万圣节派对上，她一直很镇定。"
    scene day1_202
    with dissolve
    sophia "她应付得来。"
    scene day1_201
    with dissolve
    pause
    scene day1_199
    with dissolve
    r1 "希望吧。"
    stop music fadeout 2
    scene black
    with Dissolve (2)
    pause (1)
    scene day1_sandboxhome1
    with Dissolve (1)
    
    
label sandbox_home_1:    
    $ renpy.end_replay()
    scene day1_sandboxhome1
    menu:
        "索菲娅":
            jump sandbox_home1_sophia1
        "去楼下。":
            jump downstairs_1
            
label sandbox_home1_sophia1:
    scene day1_sandboxhome1_sophia1
    menu:
        "聊聊。":
            if talk_sophia == 0:
                r1 "你有没有想过回到从前？"
                scene day1_sandboxhome1_sophia2
                with dissolve
                sophia "开始怀旧了？"
                r1 "我是认真的。"
                sophia "你好，认真先生。我是[sophia]。"
                scene day1_sandboxhome1_sophia4
                with dissolve
                sophia "[nickname_sophia1]，我们回不去从前了。"
                scene day1_sandboxhome1_sophia3
                with dissolve
                sophia "只要现在能待在你身边，我就很满足。"
                r1 "那就好。"
                r1 "那我去干活了。"
                sophia "你一走我就把那支步枪拿出来。"
                r1 "好。"
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[sophia]的{color=#00ff00}好感{/color}提升了{color=#00ff00}1{/color}点！" )
                $talk_sophia +=1
                $love_sophia +=1
            elif (ava_trigger == True):
                r1 "你在教[ava]什么？"
                scene day1_sandboxhome1_sophia3
                with dissolve
                sophia "什么意思？"
                r1 "你是在教她怎么给我口交吗？"
                scene day1_sandboxhome1_sophia46
                with hpunch
                sophia "什么？"
                scene day1_sandboxhome1_sophia3
                with dissolve
                sophia "哦！她一直在问，在床上该怎么做才能让你舒服。"
                sophia "刚才玩过之后，她就一直在问你是不是没满足。"
                sophia "所以我给了她一个关于怎——"
                scene day1_sandboxhome1_sophia2
                with hpunch
                sophia "等等！"
                sophia "她给你口了？"
                r1 "这个……她……"
                scene day1_sandboxhome1_sophia45
                with hpunch
                sophia "哦——……我的……天——！"
                sophia "那个小淫娃！"
                sophia "没想到她还有这一手。"
                scene day1_sandboxhome1_sophia2
                with dissolve
                sophia "下次你最好邀请我！"
                sophia "我要看！"
                r1 "我……考虑看看。"
                r1 "我真的该去干活了。"
                scene day1_sandboxhome1_sophia3
                with dissolve
                sophia "我会想你的。"
            else:
                r1 "(还是让她干活吧。)"
                
        "摸一把。" if ((love_sophia > 50) or (_in_replay)):
            scene day1_sandboxhome1_sophia5
            with dissolve
            pause
            scene day1_sandboxhome1_sophia6
            with dissolve
            sophia "手感不错？"
            r1 "过来就行。"
            scene day1_sandboxhome1_sophia7
            with dissolve
            pause
            scene day1_sandboxhome1_sophia8
            with dissolve
            pause
            scene day1_sandboxhome1_sophia9
            with dissolve
            pause
            scene day1_sandboxhome1_sophia10
            with dissolve
            sophia "你在干什么？"
            r1 "跟我女朋友寻欢呢。"
            scene day1_sandboxhome1_sophia11
            with dissolve
            pause
            scene day1_sandboxhome1_sophia10
            with dissolve
            sophia "这个嘛……"
            scene day1_sandboxhome1_sophia12
            with dissolve
            sophia "那我也能和我的男人玩吗？"
            scene day1_sandboxhome1_sophia13
            with dissolve
            sophia "要我在你上班前帮你撸一发吗？"
            scene day1_sandboxhome1_sophia14
            with dissolve
            sophia "或者你更想让我……"
            scene day1_sandboxhome1_sophia15
            with dissolve
            pause
            scene day1_sandboxhome1_sophia16
            with dissolve
            pause
            scene day1_sandboxhome1_sophia17
            with dissolve
            pause
            sophia "你知道，我可是个纯洁的小女生。"
            sophia "难道你不想用我吗，[nickname_sophia1]？"
            scene day1_sandboxhome1_sophia17
            pause
            scene day1_sandboxhome1_sophia18
            with dissolve
            r1 "再这么撩我，你很快就会发现自己一丝不挂。"
            scene day1_sandboxhome1_sophia19
            with dissolve
            sophia "嘻嘻嘻。"
            scene day1_sandboxhome1_sophia20
            with dissolve
            pause
            scene day1_sandboxhome1_sophia10
            with dissolve
            sophia "好了，回去干活吧。"
            if love_sophia < 52:
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[sophia]的{color=#00ff00}好感{/color}提升了{color=#00ff00}1{/color}点！" )
                $love_sophia +=1 
        "磨蹭。" if ((love_sophia > 51) and (corruption_sophia > 0)) or (_in_replay):
            scene day1_sandboxhome1_sophia5
            with dissolve
            pause
            scene day1_sandboxhome1_sophia6
            with dissolve
            scene day1_sandboxhome1_sophia7
            with dissolve
            pause
            scene day1_sandboxhome1_sophia8
            with dissolve
            pause
            scene day1_sandboxhome1_sophia9
            with dissolve
            pause
            scene day1_sandboxhome1_sophia21
            with dissolve
            pause
            scene day1_sandboxhome1_sophia22
            with dissolve
            pause
            scene day1_sandboxhome1_sophia23
            with dissolve
            sophia "什么事？"
            scene day1_sandboxhome1_sophia24
            with dissolve
            sophia "出什么问题了吗？"
            scene day1_sandboxhome1_sophia25
            with dissolve
            r1 "没有，完全没有。"
            scene day1_sandboxhome1_sophia26
            with dissolve
            r1 "大概只是在欣赏风景。"
            scene day1_sandboxhome1_sophia27
            with dissolve
            sophia "你想让我来劲？"
            r1 "我不知道……你呢？"
            scene day1_sandboxhome1_sophia28
            with dissolve
            sophia "也许吧……"
            scene day1_sandboxhome1_sophia29
            with dissolve
            r1 "也许？"
            scene day1_sandboxhome1_sophia30
            with dissolve
            sophia "就、就那么……"
            scene day1_sandboxhome1_sophia31
            with dissolve
            sophia "一点点！"
            scene day1_sandboxhome1_sophia32
            with dissolve
            sophia "一点点而已！"
            scene day1_sandboxhome1_sophia28
            with dissolve
            sophia "真可惜你有这么多事要做……"
            scene day1_sandboxhome1_sophia33
            with dissolve
            sophia "而我只能待在这里……"
            scene day1_sandboxhome1_sophia34
            with dissolve
            sophia "孤零零的……"
            scene day1_sandboxhome1_sophia35
            with dissolve
            pause
            r1 "真逗。"
            scene day1_sandboxhome1_sophia36
            with dissolve
            sophia "那个，我……"
            scene day1_sandboxhome1_sophia37
            with dissolve
            sophia "好……"
            scene day1_sandboxhome1_sophia38
            with dissolve
            sophia "很好笑的女孩……"
            sophia "我能坐到你腿上吗，[nickname_sophia1]？"
            r1 "你打算把你开的头做完吗？"
            scene day1_sandboxhome1_sophia39
            with dissolve
            sophia "啊啊——……"
            scene day1_sandboxhome1_sophia40
            with dissolve
            sophia "你真没意思！"
            scene day1_sandboxhome1_sophia40_1
            with dissolve
            pause
            scene day1_sandboxhome1_sophia41
            with dissolve
            pause
            r1 "其实我挺有意思的。"
            scene day1_sandboxhome1_sophia42
            with dissolve
            pause
            scene day1_sandboxhome1_sophia43
            with dissolve
            r1 "我可是很有趣的。"
            r1 "不过说真的……我得去上班了。"
            r1 "在我改变主意操你之前，赶快起来。"
            scene day1_sandboxhome1_sophia44
            with dissolve
            sophia "别磨蹭太久，不然我可就自己先开始了。"
            stop music fadeout 2
            scene black
            with Dissolve (2)
            pause (1)
            scene day1_sandboxhome1
            with Dissolve (1)
            if love_sophia < 52:
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[sophia]的{color=#00ff00}好感{/color}上升了{color=#00ff00}1{/color}点！" )
                $love_sophia +=1 
            if corruption_sophia < 2:
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[sophia]的{color=#ff0000}堕落{/color}上升了{color=#00ff00}1{/color}点！" )
                $corruption_sophia +=1 
            jump sandbox_home_1
        "回去":
            #$ renpy.end_replay()
            jump sandbox_home_1
    jump sandbox_home1_sophia1
    
    
label downstairs_1:
    scene day1_downstairs_1
    menu:
        "去看看艾娃":
            jump sandbox_home1_ava1
        "回卧室。":
            jump sandbox_home_1
        "去学院。":
            jump jas_day1_bathroom
    
label sandbox_home1_ava1:
    if (ava_trigger == True):
        scene day1_sandboxhome1_ava68
        r1 "她在洗澡。而且我要迟到了。"
        jump downstairs_1
    else:
        scene day1_sandboxhome1_ava1
        menu:
            "跟她说说话。":
                ava "哦，早上好！"
                ava "我以为你已经去上班了。"
                scene day1_sandboxhome1_ava2
                with dissolve
                r1 "其实没有。"
                scene day1_sandboxhome1_ava3
                with dissolve
                r1 "走之前想先看看你。"
                r1 "也许顺便看看你想我没。"
                scene day1_sandboxhome1_ava4
                with dissolve
                ava "才没有。我很好，真的。"
                scene day1_sandboxhome1_ava6
                with hpunch
                ava "我是说！我当然爱你！"
                scene day1_sandboxhome1_ava7
                with hpunch
                ava "我是说！想你！"
                scene day1_sandboxhome1_ava8
                with hpunch
                pause
                scene day1_sandboxhome1_ava9
                pause
                scene day1_sandboxhome1_ava10
                with dissolve
                r1 "你还知道我能看见吧？"
                scene day1_sandboxhome1_ava11
                with dissolve
                ava "你才看不见！我藏起来了！"
                scene day1_sandboxhome1_ava10
                with dissolve
                r1 "行了，起来吧。"
                scene day1_sandboxhome1_ava12
                with dissolve
                pause
                scene day1_sandboxhome1_ava13
                with dissolve
                ava "天啊！我真想找个地缝钻进去！"
                scene day1_sandboxhome1_ava14
                with dissolve
                pause
                scene day1_sandboxhome1_ava15
                with dissolve
                r1 "听着，你对自己太苛刻了。"
                scene day1_sandboxhome1_ava16
                with dissolve
                r1 "放松点。我不是来评判你的。"
                scene day1_sandboxhome1_ava17
                with dissolve
                ava "要是真有那么容易就好了。"
                scene day1_sandboxhome1_ava18
                with dissolve
                r1 "可以有那么容易。"
                scene day1_sandboxhome1_ava19
                with dissolve
                ava "拜托，你一直都这么自信吗？"
                scene day1_sandboxhome1_ava20
                with dissolve
                r1 "倒也不是。不过这是我应得的。"
                ava "哦？这么说以前你也是个人类咯？！"
                r1 "少来！"
                scene day1_sandboxhome1_ava21
                with hpunch
                pause
                scene day1_sandboxhome1_ava22
                with dissolve
                pause
                scene day1_sandboxhome1_ava21
                ava "你……？"
                scene day1_sandboxhome1_ava23
                ava "嗯……你……？"
                scene day1_sandboxhome1_ava24
                ava "你刚刚是不是掀了我的裙子？"
                r1 "荒谬！我怎么可能！"
                scene day1_sandboxhome1_ava23
                ava "我很确定你掀了。"
                r1 "是吗？那你转过来给我看看证据？"
                scene day1_sandboxhome1_ava25
                with dissolve
                ava "别闹！你让我很尴尬！"
                r1 "要我停下吗？"
                scene day1_sandboxhome1_ava26
                with dissolve
                pause
                scene day1_sandboxhome1_ava27
                with dissolve
                pause
                scene day1_sandboxhome1_ava28
                with dissolve
                pause
                scene day1_sandboxhome1_ava29
                with dissolve
                r1 "好吧，我得去上班了。"
                scene day1_sandboxhome1_ava24
                with hpunch
                ava "不要！"
                scene day1_sandboxhome1_ava25
                with dissolve
                ava "我是说……"
                scene day1_sandboxhome1_ava30
                with dissolve
                ava "我们能不能……就这样多待一会儿？"
                menu:
                    "继续。":
                        r1 "我有个主意。"
                        scene day1_sandboxhome1_ava31
                        with dissolve
                        pause
                        scene day1_sandboxhome1_ava32
                        with dissolve
                        ava "你、你要做什么？"
                        r1 "你紧张了？"
                        ava "有、有一点。"
                        scene day1_sandboxhome1_ava33
                        with dissolve
                        pause
                        r1 "在我看来，你至少也一样兴奋。"
                        scene day1_sandboxhome1_ava34
                        with dissolve
                        ava "我、我的心跳得好快。"
                        scene day1_sandboxhome1_ava35
                        with dissolve
                        pause
                        scene day1_sandboxhome1_ava36
                        with dissolve
                        pause
                        scene day1_sandboxhome1_ava69
                        with dissolve
                        pause
                        scene day1_sandboxhome1_ava70
                        with hpunch
                        pause
                        scene day1_sandboxhome1_ava71
                        with hpunch
                        ava "你在干什么？！"
                        r1 "你信任我吗？"
                        scene day1_sandboxhome1_ava72
                        with dissolve
                        ava "我……但是……"
                        r1 "再说一次。你信任我吗？"
                        scene day1_sandboxhome1_ava73
                        with dissolve
                        ava "信任。"
                        r1 "那就相信我。"
                        r1 "深呼吸。闭上眼睛。"
                        scene day1_sandboxhome1_ava74
                        with dissolve
                        pause
                        r1 "现在松开我的手。"
                        r1 "想象我们就躺在自己的床上。"
                        scene day1_sandboxhome1_ava70
                        with dissolve
                        r1 "而我正在吻你……"
                        scene day1_sandboxhome1_ava69
                        with Dissolve (1)
                        r1 "先吻你的嘴唇，然后是脖子。"
                        scene day1_sandboxhome1_ava40
                        with dissolve
                        r1 "指尖慢慢地滑过你全身。"
                        r1 "偶尔还会轻咬你的下唇。"
                        scene day1_sandboxhome1_ava37
                        with dissolve
                        pause
                        scene day1_sandboxhome1_ava38
                        with dissolve
                        pause
                        scene day1_sandboxhome1_ava39
                        with dissolve
                        pause
                        r1 "你开始享受了，对吧？"
                        scene day1_sandboxhome1_ava40
                        with dissolve
                        ava "你……在对我做这种事。"
                        ava "都怪……"
                        scene day1_sandboxhome1_ava41
                        with dissolve
                        ava "……你。"
                        scene day1_sandboxhome1_ava42
                        with dissolve
                        pause
                        scene day1_sandboxhome1_ava43
                        with dissolve
                        pause
                        scene day1_sandboxhome1_ava44
                        with dissolve
                        pause
                        scene day1_sandboxhome1_ava45
                        with hpunch
                        pause
                        scene day1_sandboxhome1_ava46
                        with hpunch
                        pause
                        scene day1_sandboxhome1_ava47
                        with hpunch
                        pause
                        scene day1_sandboxhome1_ava48
                        with dissolve
                        menu:
                            "口交。":
                                $ava_trigger = True
                                scene day1_sandboxhome1_ava49
                                with hpunch
                                pause
                                scene day1_sandboxhome1_ava50
                                with dissolve
                                pause
                                ava "你、你要我……"
                                scene day1_sandboxhome1_ava49
                                with dissolve
                                ava "要、要含……唔……"
                                scene day1_sandboxhome1_ava50
                                with dissolve
                                ava "来满足你？"
                                menu:
                                    "怂恿她再放开一点。{p=0.0}{color=#ff0000}(艾娃 堕落 +2){/color}":
                                        play sound "audio/Lockpick_Success.ogg" volume 0.1
                                        show screen notifyEx( msg="[ava]的{color=#ff0000}堕落{/color}上升了{color=#00ff00}2{/color}点！" )
                                        $corruption_ava +=2
                                        r1 "跟我说「我可以含你的鸡巴吗？」"
                                        scene day1_sandboxhome1_ava51
                                        with hpunch
                                        ava "什么？！"
                                        ava "我、我不行！"
                                        r1 "当然你可以。"
                                        r1 "先轻轻亲一下，再问我能不能含。"
                                        scene day1_sandboxhome1_ava52
                                        with dissolve
                                        pause
                                        scene day1_sandboxhome1_ava53
                                        with dissolve
                                        ava "好、好的，[ava]。你可以的。"
                                        scene day1_sandboxhome1_ava54
                                        with dissolve
                                        pause
                                        scene day1_sandboxhome1_ava55
                                        with dissolve
                                        ava "我可以含你的鸡巴吗，[nickname_ava1]？"
                                    "安慰她。{p=0.0}{color=#00ff00}(艾娃 好感 +2){/color}":
                                        play sound "audio/Lockpick_Success.ogg" volume 0.1
                                        show screen notifyEx( msg="[ava]的{color=#00ff00}好感{/color}上升了{color=#00ff00}2{/color}点！" )
                                        $love_ava +=2
                                        r1 "慢慢来。没关系。"
                                        r1 "只有你真的想做的时候才做。"
                                        scene day1_sandboxhome1_ava56
                                        with dissolve
                                        ava "谢谢。我有点怕自己做不好。"
                                        scene day1_sandboxhome1_ava52
                                        with dissolve
                                        ava "那个……[sophia]现在不在……"
                                        scene day1_sandboxhome1_ava53
                                        with dissolve
                                        ava "好、好的，[ava]。你可以的。"
                                scene day1_sandboxhome1_ava59
                                with dissolve
                                pause
                                r1 "看着我。"
                                scene day1_sandboxhome1_ava60
                                with dissolve
                                pause
                                scene day1_sandboxhome1_ava61
                                with dissolve
                                ava "我做对了吗？"
                                r1 "做得很好。现在多用一点舌头，然后把它放进嘴里。"
                                ava "好、好的。"
                                scene day1_sandboxhome1_ava62
                                with dissolve
                                pause
                                scene day1_sandboxhome1_ava75
                                with hpunch
                                ava "我不行！"
                                scene day1_sandboxhome1_ava76
                                with dissolve
                                ava "对不起！只是这一切发展得太快了！"
                                ava "我能不能……先帮你手交？"
                                r1 "[ava]……你不想做也没关系。"
                                scene day1_sandboxhome1_ava77
                                with hpunch
                                ava "我想做！"
                                scene day1_sandboxhome1_ava78
                                with dissolve
                                ava "只是……"
                                scene day1_sandboxhome1_ava79
                                with dissolve
                                ava "你能握着我的手引导我吗？"
                                r1 "那我就牵着你的手，好吗？"
                                ava "好、好的。"
                                scene day1_sandboxhome1_ava80
                                with dissolve
                                pause
                                image movie = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)
                                play movie "images/Animations/avahandjobsandbox1.webm" loop 
                                show movie with dissolve
                                pause
                                play movie "images/Animations/avahandjobsandbox2.webm" loop 
                                show movie with dissolve
                                ava "我做对了吗？"
                                r1 "做得好些了。感觉好一点了吗？"
                                ava "嗯。你引导我的话就容易多了。"
                                scene day1_sandboxhome1_ava78
                                with dissolve
                                stop movie
                                ava "我……我觉得我准备好把它放进嘴里了。"
                                scene day1_sandboxhome1_ava81
                                with dissolve
                                ava "不难，对吧？"
                                r1 "我……不清楚。"
                                scene day1_sandboxhome1_ava82
                                with dissolve
                                ava "*咯咯笑*"
                                scene day1_sandboxhome1_ava83
                                with dissolve
                                ava "谢谢……谢谢你帮我破冰。"
                                scene day1_sandboxhome1_ava84
                                with dissolve
                                ava "好，我能做到。"
                                ava "跟手交一样，只是用嘴。"
                                ava "对吧？"
                                ava "只要再靠近一点……"
                                ava "然后把你的鸡巴放进我嘴里……"
                                scene day1_sandboxhome1_ava85
                                with dissolve
                                pause
                                play movie "images/Animations/avablowjobsandbox4.webm" loop 
                                show movie with dissolve
                                pause
                                play movie "images/Animations/avablowjobsandbox5.webm" loop 
                                show movie with dissolve
                                pause
                                play movie "images/Animations/avablowjobsandbox6.webm" loop 
                                show movie with dissolve
                                pause
                                scene day1_sandboxhome1_ava86
                                with dissolve
                                stop movie
                                ava "你喜欢吗？会不会弄疼你？"
                                r1 "做得很好，宝贝。"
                                r1 "你这样子也很可爱。"
                                r1 "那你自己呢？喜欢吗？"
                                scene day1_sandboxhome1_ava87
                                with dissolve
                                ava "喜欢！"
                                ava "我觉得我有点熟练了！"
                                ava "我可以快一点吗？"
                                r1 "当然！"
                                scene day1_sandboxhome1_ava88
                                with dissolve
                                pause
                                #play music "audio/slurp.ogg"
                                play movie "images/Animations/avablowjobsandbox1.webm" loop 
                                show movie with dissolve
                                pause
                                play movie "images/Animations/avablowjobsandbox2.webm" loop 
                                show movie with dissolve
                                pause
                                play movie "images/Animations/avablowjobsandbox3.webm" loop 
                                show movie with dissolve
                                pause
                                r1 "[ava]……我快……"
                                stop music
                                scene day1_sandboxhome1_ava63
                                hide movie
                                stop movie
                                scene day1_sandboxhome1_ava63
                                with flashbulb
                                pause
                                scene day1_sandboxhome1_ava64
                                with flashbulb
                                pause
                                scene day1_sandboxhome1_ava65
                                with flashbulb
                                pause
                                ava "我……好像射到你鼻子上了……味道好奇怪。"
                                ava "还有……我想洗澡了。"
                                scene day1_sandboxhome1_ava66
                                with dissolve
                                ava "不过我做得好吗？"
                                ava "[sophia]教过我几招怎么取悦你……但我不确定自己做对了没有。"
                                r1 "哦，做得很好。"
                                ava "太好了！"
                                r1 "等等，什么？[sophia]一直在教你？怎么教的？"
                                scene day1_sandboxhome1_ava67
                                with dissolve
                                ava "哦，她只是让我用手，还有小心牙齿。"
                                ava "挺好玩的。我当时好怕咬到你。"
                                r1 "那我得谢谢[sophia]了。"
                                ava "我得在她看到我这副样子之前洗个澡……"
                                $ renpy.end_replay()
                                jump downstairs_1
                            "去上班。":
                                pause 0.001
                    "去上班。":
                        pause 0.001
                
    
            "回去。":
                $ renpy.end_replay()
                jump downstairs_1
     
    $ renpy.end_replay()
    jump sandbox_home1_ava1
            
    
label jas_day1_bathroom: 
    stop music fadeout 2
    scene black
    with Dissolve (2)
    pause (1)
    scene jas_day1_bathroom_49
    with dissolve
    play music "audio/stressless.ogg" fadein 3 volume 0.1
    l "早上好，先生！"
    l "我要调整一年级的今天的课程安排。"
    l "大概一小时后我把新课表送到您那儿。"
    r1 "谢谢，[l]。"
    scene jas_day1_bathroom_51
    with dissolve
    l "哦！不客气，先生！"
    scene jas_day1_bathroom_49
    with dissolve
    l "另外，[lila]的母亲打电话来了！"
    l "她问他们家那家餐馆还开不开了。"
    r1 "那……很奇怪。"
    l "怎么奇怪了？"
    r1 "让您去接这种社交性质的电话，不合适吧？"
    scene jas_day1_bathroom_50
    with dissolve
    l "哦！是那种奇怪！"
    l "完全不会，先生！"
    l "您是以学校的名义出面，这是一次公务约见。"
    l "哪怕它带点社交性质。"
    scene jas_day1_bathroom_49
    with dissolve
    l "再说了，我是您的私人助理！"
    l "这种事我非常乐意替您效劳。"
    r1 "好的。谢谢你，[l]。"
    scene jas_day1_bathroom_51
    with dissolve
    l "随时为您效劳，先生！"
    scene jas_day1_bathroom_3
    with Dissolve(1)
    pause
    play sound "audio/beep.mp3"
    scene jas_day1_bathroom_4
    with dissolve
    pause
    scene jas_day1_bathroom_5
    with dissolve
    pause
    scene jas_day1_bathroom_52
    nvl_narrator "[sophia]的聊天"
    sophia_nvl "[nickname_sophia1]，你会超爱这个的！"
    menu:
        "看看她的头像。":
            scene sophia_pfp
            with dissolve
            pause
        "继续聊天。":
            pause 0.001
    scene jas_day1_bathroom_52
    r1_nvl "出什么事了？"
    sophia_nvl "放轻松，小家伙！我给你发了张照片！"
    sophia_nvl "话说，你什么时候加个头像啊？"
    r1_nvl "头像？"
    sophia_nvl "就是那个你应该加上的东西啊，这样我跟你说话时就能看到你的脸！"
    sophia_nvl "哦，等等！这也太棒了！"
    sophia_nvl "{image=phone/sophia_selfie1.png}"
    menu:
        "查看图片。":
            scene jas_day1_bathroom_53
            with dissolve
            pause
        "继续聊天。":
            pause 0.001
    scene jas_day1_bathroom_52
    sophia_nvl "好主意！她会把我们都杀了！{image=emoji/sweat.png}"
    r1_nvl "拜托，对她温柔点。"
    r1_nvl "我记得你也教了她不少。"
    sophia_nvl "不公平！"
    r1_nvl "教她基础的就够了。别乱来。"
    r1_nvl "等我回家再说。"
    sophia_nvl "没问题！"
    nvl clear
    scene jas_day1_bathroom_3
    with Dissolve(1)
    pause
    play sound "audio/beep.mp3"
    scene jas_day1_bathroom_4
    with dissolve
    r1 "我在上班，[sophia]……"
    r1 "呃……算是吧……"
    scene jas_day1_bathroom_5
    with dissolve
    pause
    scene jas_day1_bathroom_6
    nvl_narrator "[ja]的聊天"
    ja_nvl "嘿。"
    r1_nvl "[ja]？"
    menu:
        "看看她的头像。":
            scene jasmin_pfp
            with dissolve
            pause
        "继续聊天。":
            pause 0.001
    scene jas_day1_bathroom_6
    ja_nvl "能聊聊吗？"
    r1_nvl "当然，来我办公室吧。"
    ja_nvl "不……呃……得私下说。"
    r1_nvl "出什么事了吗？"
    ja_nvl "不知道。"
    r1_nvl "你在哪？"
    ja_nvl "{image=phone/jasmin_selfie1.png}"
    ja_nvl "教室。"
    ja_nvl "你能来吗？"
    r1_nvl "行，没问题。"
    ja_nvl "好，谢了。"
    scene jas_day1_bathroom_1
    with Dissolve(1)
    pause
    scene jas_day1_bathroom_2
    with dissolve
    r1_nvl "要我带你出去吗？"
    scene jas_day1_bathroom_7
    with dissolve
    pause
    play sound "audio/Open5.ogg"
    scene jas_day1_bathroom_8
    with dissolve
    pause
    scene jas_day1_bathroom_9
    with hpunch
    pause
    stop music
    play sound "audio/hitwood1.ogg"
    scene jas_day1_bathroom_10
    with hpunch
    pause
    scene jas_day1_bathroom_11
    ja "你到底做了什么？"
    scene jas_day1_bathroom_12
    pause
    scene jas_day1_bathroom_11
    pause
    scene jas_day1_bathroom_13
    r1 "你说得具体一点。"
    play sound "audio/hitwood1.ogg"
    scene jas_day1_bathroom_14
    with hpunch
    pause
    scene jas_day1_bathroom_11
    ja "我家那片街区。大家都躲着我走。"
    ja "你。到底。做了什么。"
    scene jas_day1_bathroom_12
    pause
    scene jas_day1_bathroom_11
    pause
    scene jas_day1_bathroom_13
    r1 "我不知道你——"
    play sound "audio/hit1.ogg"
    scene jas_day1_bathroom_15
    with hpunch
    pause
    play sound "audio/hit1.ogg"
    scene jas_day1_bathroom_16
    with hpunch
    ja "你做了什么！"
    scene jas_day1_bathroom_17
    r1 "拜托，别再这样了。"
    play sound "audio/hit1.ogg"
    scene jas_day1_bathroom_18
    with hpunch
    r1 "[ja]，冷静点！"
    play sound "audio/hit1.ogg"
    scene jas_day1_bathroom_19
    with hpunch
    ja "你到底。"
    play sound "audio/hit1.ogg"
    scene jas_day1_bathroom_18
    with hpunch
    ja "做了什么？！"
    play sound "audio/hit1.ogg"
    scene jas_day1_bathroom_19
    with hpunch
    r1 "[ja]。"
    play sound "audio/hit1.ogg"
    scene jas_day1_bathroom_18
    with hpunch
    ja "什么？！"
    play sound "audio/hitwood1.ogg"
    scene jas_day1_bathroom_20
    with hpunch
    r1 "你能不能冷静一点？！"
    scene jas_day1_bathroom_21
    r1 "你们这些女人到底是怎么回事？"
    r1 "你们是约好了同一天发疯吗？"
    scene jas_day1_bathroom_22
    with dissolve
    pause
    scene jas_day1_bathroom_21
    with dissolve
    pause
    scene jas_day1_bathroom_23
    with dissolve
    r1 "天啊……"
    scene jas_day1_bathroom_24
    with dissolve
    r1 "如果我松手……你能冷静下来吗？"
    r1 "像个文明人一样说话？"
    scene jas_day1_bathroom_25
    with dissolve
    ja "好、好的。"
    scene jas_day1_bathroom_26
    with dissolve
    r1 "对不起，好吗？"
    r1 "我只是需要你冷静下来。"
    r1 "你没事吧？"
    scene jas_day1_bathroom_27
    with dissolve
    pause
    scene jas_day1_bathroom_26
    with dissolve
    r1 "要我退开一点吗？"
    r1 "给你点空间？"
    scene jas_day1_bathroom_27
    with dissolve
    pause
    scene jas_day1_bathroom_28
    with dissolve
    ja "不、不用。"
    scene jas_day1_bathroom_29
    with dissolve
    ja "对不起。我不该打你的。"
    scene jas_day1_bathroom_28
    with dissolve
    ja "我越界了。"
    scene jas_day1_bathroom_26
    with dissolve
    r1 "没关系。"
    r1 "我弄疼你了吗？"
    scene jas_day1_bathroom_29
    with dissolve
    ja "没有。"
    ja "刚才只是吓了我一跳。"
    scene jas_day1_bathroom_26
    with dissolve
    r1 "我退开几步，好吗？"
    r1 "你不是想去我办公室吗？我们可以去那边私下谈。"
    scene jas_day1_bathroom_30
    with dissolve
    ja "不。我不想让[l]听到我们的谈话。"
    ja "这里比较安全。"
    scene jas_day1_bathroom_31
    with dissolve
    pause
    scene jas_day1_bathroom_32
    with dissolve
    pause
    scene jas_day1_bathroom_33
    with dissolve
    r1 "在杂物间里？"
    scene jas_day1_bathroom_34
    with dissolve
    r1 "总之。你刚才说什么？"
    r1 "谁怕你了？"
    scene jas_day1_bathroom_35
    with dissolve
    ja "*叹气*"
    scene jas_day1_bathroom_36
    with dissolve
    ja "我都不知道他们到底怕不怕我。"
    ja "但他们确实在躲着我。"
    scene jas_day1_bathroom_37
    with dissolve
    ja "我比家里所有人都起得早。"
    scene jas_day1_bathroom_38
    with dissolve
    ja "所以一大早就去面包店，给[ju]买点面包卷。"
    scene jas_day1_bathroom_36
    with dissolve
    ja "他们说不能卖给我，也不给理由。"
    scene jas_day1_bathroom_35
    with dissolve
    ja "我跑了三家面包店才买到一点面包，他们还不让我付钱。"
    scene jas_day1_bathroom_39
    with dissolve
    ja "我去找莱罗伊，问大家到底怎么了。"
    ja "他和其他人说我不再受欢迎了，不准我再靠近他们。"
    scene jas_day1_bathroom_40
    with dissolve
    ja "你送我回家之后发生了什么？"
    ja "你跟他们谈过了吗？"
    scene jas_day1_bathroom_41
    with dissolve
    r1 "我不知道那家伙是你朋友。"
    scene jas_day1_bathroom_35
    with dissolve
    ja "他不是。我是说。不重要。"
    scene jas_day1_bathroom_38
    with dissolve
    ja "我们那片街区的人不能知道我在这里读书。"
    scene jas_day1_bathroom_41
    with dissolve
    r1 "为什么？"
    scene jas_day1_bathroom_38
    with dissolve
    ja "因为……"
    scene jas_day1_bathroom_35
    with dissolve
    ja "听着，就算我们没钱也没关系。一点都不重要。"
    scene jas_day1_bathroom_40
    with dissolve
    ja "你不能告诉那边的人，你在往上走。"
    ja "那不安全。对我，对[ju]，对谁都不安全。"
    ja "人家会觉得我是个势利眼，或者觉得我在炫耀。"
    scene jas_day1_bathroom_35
    with dissolve
    ja "更别说还会发生一堆别的事了。"
    scene jas_day1_bathroom_41
    with dissolve
    r1 "你昨天还告诉我，因为你是本地人所以很安全。"
    r1 "现在又说要是被人知道你在读这所学院，就会成为靶子。"
    r1 "那你凭什么觉得我会把自己暴露给一群我根本不认识的人？"
    r1 "把这所学校和我的身份告诉他们，我岂不是比你会更招人恨？"
    scene jas_day1_bathroom_40
    with dissolve
    pause
    scene jas_day1_bathroom_42
    with dissolve
    ja "你不是吗？"
    r1 "我为什么要？"
    scene jas_day1_bathroom_42
    pause
    scene jas_day1_bathroom_43
    with dissolve
    pause
    scene jas_day1_bathroom_44
    with dissolve
    ja "对不起。"
    scene jas_day1_bathroom_41
    with dissolve
    r1 "他们威胁你或者你妹妹了吗？"
    scene jas_day1_bathroom_44
    with dissolve
    ja "倒也没有。"
    ja "但我确实察觉到有什么不对劲。"
    ja "莱罗伊和他那伙人掌管着那片地方。跟他们关系不好可不是闹着玩的。"
    scene jas_day1_bathroom_41
    with dissolve
    r1 "（看来我得去拜访他一趟了。）"
    r1 "他们对你说了什么？"
    scene jas_day1_bathroom_35
    with dissolve
    ja "听着，对不起。可能是别的事。我以为你也是他们一伙的。"
    ja "既然知道你不是，我就不想把你牵扯进来。"
    play sound "audio/hitwood1.ogg"
    scene jas_day1_bathroom_45
    r1 "[ja]，他们到底对你说了什么？"
    scene jas_day1_bathroom_46
    with dissolve
    ja "让我别靠近他们，也别去他们的地盘。"
    ja "想买杂货还是什么的话，就去街区另一头。"
    ja "还有，他们那边的东西店里我什么也买不到。"
    scene jas_day1_bathroom_45
    with dissolve
    r1 "我明白了。"
    r1 "[ju]知道吗？"
    scene jas_day1_bathroom_46
    with dissolve
    ja "应该不知道。今天早上他们才找过我。"
    scene jas_day1_bathroom_45
    with dissolve
    r1 "我很认真地跟你说几句。"
    r1 "只要你觉得自己不安全，就给我打电话。"
    r1 "千万别想自己一个人去解决这种事。"
    r1 "我知道你人生中有很多难事都是一个人扛过来的。"
    r1 "但这一次不算，明白吗？"
    r1 "你已经不再是一个人了。"
    scene jas_day1_bathroom_46
    with dissolve
    ja "你、你为什么这么说？"
    scene jas_day1_bathroom_45
    with dissolve
    pause
    scene jas_day1_bathroom_47
    with dissolve
    r1 "因为你已经打了我一下。"
    r1 "所以我就有权多管闲事了。你只能忍着我了。"
    scene jas_day1_bathroom_46
    with dissolve
    pause
    scene jas_day1_bathroom_48
    with dissolve
    ja "你个混蛋。"
    scene jas_day1_bathroom_47
    with dissolve
    r1 "现在回教室去，不然我就要给你停课了。"
    stop music fadeout 2
    scene black
    with Dissolve (2)
    play music "audio/stressless.ogg" fadein 5 volume 0.1
    pause (1)
    scene jas_day1_bathroom_3
    with Dissolve(1)
    pause
    play sound "audio/beep.mp3"
    scene jas_day1_bathroom_4
    with dissolve
    pause
    scene jas_day1_bathroom_5
    with dissolve
    pause
    scene jas_day1_bathroom_6
    ja_nvl "刚才那事真的很抱歉。"
    menu:
        "安慰她。{p=0.0}{color=#00ff00}([ja] 好感 +2){/color}":
            play sound "audio/Lockpick_Success.ogg" volume 0.1
            show screen notifyEx( msg="[ja]的{color=#00ff00}好感{/color}上升了{color=#00ff00}2{/color}点！" )
            $love_jas += 2
            r1_nvl "没关系。我理解你当时在气头上。"
            ja_nvl "谢啦！"
        "训斥她。{p=0.0}{color=#ff0000}([ja] 堕落 +1){p=0.0}{color=#00ff00}([ja] 好感 -1){/color}":
            play sound "audio/Lockpick_Success.ogg" volume 0.1
            show screen notifyEx( msg="[ja]的{color=#ff0000}堕落{/color}上升了{color=#00ff00}1{/color}点！" )
            show screen notifyEx( msg="[ja]的{color=#00ff00}好感{/color}下降了{color=#ff0000}1{/color}点！" )
            $love_jas -= 1
            $corruption_jas += 1
            r1_nvl "别再有下次了。"
            ja_nvl "不会的！"
    ja_nvl "我真的不该打你。真的很抱歉。"
    ja_nvl "话说，今天你要带我们参观吗？"
    r1_nvl "参观？"
    ja_nvl "我们的体育课取消了。说是要带我们参观什么地方。"
    ja_nvl "我还以为你知道点什么。"
    r1_nvl "我马上回来。"
    
label sandbox_office1:
    scene jas_day1_bathroom_4
    menu:
        "进入 Patreon 限定内容":           
            $patreoncheck = renpy.input("你是真正的 Patreon 会员吧，[name]？")
            $patreoncheck = patreoncheck.strip()
            
            if patreoncheck == patreoncode:
                play sound "audio/Lockpick_Success.ogg"
                "谢谢！兑换码已激活！"
                $patreon = True
            else:
                "抱歉。你确定自己是 Patreon 会员吗？"
                "如果不是的话，去看看我们的 Patreon 页面吧！"
                "Patreon限定内容里有作弊码、可重复观赏场景的图鉴等等一大堆东西哦！:)"
                $patreon = False
            jump sandbox_office1
        "进入成人图鉴" if patreon == True:
            jump nsfw_gallery_patreon
        "给[sophia]发消息":
            if (sophia_text == True):
                $sophia_text = False
                nvl clear
                r1_nvl "那边还好吗？"
                sophia_nvl "{image=phone/sophia_selfie2.png}"
                menu:
                    "查看图片。":
                        scene sophia_texting1
                        with dissolve
                        pause
                    "继续聊天。":
                        pause 0.001
                scene jas_day1_bathroom_4
                r1_nvl "[ava]怎么样了？"
                sophia_nvl "{image=phone/sophia_selfie3.png}"
                menu:
                    "查看图片。":
                        scene sophia_texting2
                        with dissolve
                        pause
                    "继续聊天。":
                        pause 0.001
                scene jas_day1_bathroom_4
                sophia_nvl "她还没开枪打我！"
                sophia_nvl "我觉得这已经算我赢了！"
                r1_nvl "枪上了膛吗？"
                sophia_nvl "当然没有！"
                sophia_nvl "我可是有点被冒犯到了！"
                r1_nvl "谁知道呢！说不定你手艺退步了！"
                sophia_nvl "是啊，昨晚你可没这么说！"
                r1_nvl "哈！哈！这种话别当着孩子们的面说！"
                sophia_nvl "喂！跟她玩得开心的是你诶！"
                sophia_nvl "把你的人生伴侣晾在一边！:("
                r1_nvl "我的人生伴侣？"
                sophia_nvl "小心哦！"
                r1_nvl "好吧，我得回去工作了。"
                sophia_nvl "真可惜……我本来在想一件事。"
                r1_nvl "什么事？"
                sophia_nvl "我在想你应该收个礼物……"
                sophia_nvl "不过也可能是我想多了……"
                r1_nvl "别吊我胃口嘛。"
                sophia_nvl "好吧……既然你都这么说了！"
                sophia_nvl "你现在一个人吗？"
                r1_nvl "是的。"
                sophia_nvl "稍等一下。"
                sophia_nvl "我在等她把头转开。"
                r1_nvl "？"
                sophia_nvl "{image=phone/sophia_selfie4.png}"
                menu:
                    "查看图片。":
                        scene sophia_texting3
                        with dissolve
                        pause
                    "继续聊天。":
                        pause 0.001
                scene jas_day1_bathroom_4
                sophia_nvl "尽快回来哦！:)"
                sophia_nvl "不然我就要在你上班的时候开远程了！>:)"
                nvl clear
                jump sandbox_office1
            else:
                r1 "不能再拖了。我得打给[l]。"
                jump sandbox_office1
            
        "打给[l]。":
            pause 0.001
    
label club_intro_1:
    stop music fadeout 2
    scene black
    with Dissolve (2)
    pause (1)
    play sound "audio/knockingdoor.ogg"
    scene club_intro1
    with Dissolve(1)
    l "先生？我可以进来吗？"
    scene jas_day1_bathroom_6
    with dissolve
    r1 "可以，[l]。请进。"
    scene club_intro2
    with dissolve
    pause
    l "今天是我们向一年级学生介绍设施的日子。"
    scene club_intro3
    with dissolve
    l "前任校长卡尔把今天定为参观体育设施的日子。也就是说学院的泳池和格斗馆。"
    l "下周我们有一……"
    scene club_intro4
    with dissolve
    l "其实有好几个约见。"
    l "如果您愿意，我可以把它们发到您的邮箱。"
    l "或者下周我提醒您。"
    scene club_intro5
    with dissolve
    r1 "下周提醒我就行。"
    r1 "我记得那些设施已经停用了。为什么还要带学生参观？"
    scene club_intro6
    with dissolve
    l "现在学生们正在上体育课。所以我们带他们参观体育设施。"
    scene club_intro7
    with dissolve
    l "这也是鼓励那些想参加课外体育活动的学生为学校改革捐款的一种方式。"
    l "同时也让他们看看学校今后能提供什么。"
    l "有些学生的父母是职业运动员。如果他们能来参加这里的专项运动，对学校会很有好处。"
    r1 "好吧……行。"
    r1 "先去泳池吧。"
    scene black
    with Dissolve (2)
    pause (1)
    scene club_intro8
    with Dissolve(1)
    ju "你说真的吗？！"
    scene club_intro9
    with dissolve
    lila "对啊！我家就有一个一模一样的泳池。"
    lila "我妈从我还在襁褓里的时候就教我游泳了。"
    ju "太夸张了！我们家不可能有泳池。"
    lila "为什么？"
    ju "根本放不下啊。而且我这辈子就没游过泳！"
    lila "哦！等你学会之后就挺爽的！"
    scene club_intro10
    with dissolve
    asu "小心点，你可能会把妹妹弄丢，交给[lila]了。"
    scene club_intro11
    with dissolve
    pause
    scene club_intro12
    with dissolve
    ash "谁把他们推进泳池里，我给二十块。"
    scene club_intro13
    with dissolve
    "{color=#FF007F}[lila]{/color} {color=#FFF}和{/color} {color=#FF007F}[ju]{/color}" "我们都听到了！"
    scene club_intro14
    with dissolve
    pause
    scene club_intro15
    with hpunch
    r1 "看来你们都认识这里啊。"
    scene club_intro16
    with dissolve
    ja "你到底是从哪儿冒出来的？！"
    r1 "当然是走楼梯。"
    ja "你刚才是瞬移过来的吗？搞什么！"
    ja "完全没人听见你来！"
    scene club_intro18
    with dissolve
    asu "简直像个刺客！"
    scene club_intro17
    with dissolve
    r1 "别胡说。"
    r1 "[ju]好像对泳池很感兴趣。"
    ja "对，我们以前从没游过。"
    ja "这是她第一次看到泳池。"
    scene club_intro19
    with dissolve
    pause
    scene club_intro17
    with dissolve
    r1 "你们都想试试？"
    scene club_intro20
    with dissolve
    ju "可以吗？！"
    r1 "有什么不可以的。离下一个设施还有时间。"
    r1 "你们只需要泳衣。"
    scene club_intro21
    with dissolve
    ju "我没有。"
    lila "没关系。我们帮你弄一套。"
    scene club_intro22
    with dissolve
    lila "等一下。"
    scene club_intro23
    with dissolve
    lila "先生，我记得更衣室里有一些泳衣。要不要去试试？"
    scene club_intro24
    with dissolve
    r1 "你们想的话当然可以。"
    scene black
    with Dissolve (2)
    pause (1)
    scene club_intro25
    with Dissolve(1)
    pause
    scene club_intro26
    with dissolve
    pause
    scene club_intro27
    with dissolve
    pause
    play sound "audio/watersplash.ogg"
    scene club_intro28
    with dissolve
    pause
    scene club_intro29
    with dissolve
    ja "不——还是不用了。非常感谢。"
    #play sound "audio/imitchicken.ogg"
    scene club_intro30
    with dissolve
    lila "*发出鸡叫的声音*"
    scene club_intro31
    with dissolve
    pause
    scene club_intro32
    with dissolve
    ja "喂，你这个小……"
    #play sound "audio/imitchicken.ogg"
    scene club_intro33
    with dissolve
    lila "*发出更多鸡叫的声音*"
    scene club_intro33_1
    with dissolve
    pause
    scene club_intro34
    with dissolve
    pause
    scene club_intro35
    with dissolve
    pause
    scene club_intro36
    pause
    play sound "audio/watersplash.ogg"
    scene club_intro37
    pause
    scene club_intro38
    with dissolve
    r1 "你确定你不去吗？"
    asu "不……真的不用。"
    lila "{i}你到底为什么那样做！{/i}"
    ja "{i}还不是你自找的！{/i}"
    lila "{i}你差点把我害死了！{/i}"
    r1 "那你就留在这里，看你的同学们在泳池里玩吗？"
    ja "{i}别这么玻璃心！{/i}"
    scene club_intro39
    with dissolve
    asu "也许我只是想跟你待在一起。"
    ju "{i}你们两个别打了！{/i}"
    ash "{i}就是说！你们两个像小孩子一样！{/i}"
    ja "{i}是她先动手的！{/i}"
    lila "{i}我才没有！{/i}"
    scene club_intro38
    with dissolve
    r1 "真的？没别的原因？"
    asu "那个……我妈总说不要吃饱了游泳。"
    scene club_intro40
    with dissolve
    lila "我们以前在这儿游过。"
    scene club_intro41
    with dissolve
    ja "等一下……"
    scene club_intro42
    with dissolve
    ja "姑娘，你该不会是在说我想的那样吧？"
    scene club_intro43
    with dissolve
    ash "[lila]，你们两个单独在泳池里干什么呢？"
    scene club_intro44
    with dissolve
    lila "哎，你们两个别闹了！"
    lila "我们只是友好切磋了一下。"
    scene club_intro45
    with dissolve
    ju "在泳池里还能干什么？"
    scene club_intro46
    with dissolve
    pause
    scene club_intro47
    with dissolve
    pause
    scene club_intro48
    with dissolve
    pause
    scene club_intro49
    with dissolve
    ju "什么……？"
    scene club_intro46
    with dissolve
    ja "姐姐，你啊……千万别变。"
    scene club_intro50
    with dissolve
    r1 "我看到了。"
    scene club_intro51
    with dissolve
    asu "太好了！对你来说，装瞎可太糟糕了！"
    scene club_intro50
    with dissolve
    r1 "臭小子。"
    scene club_intro51
    with dissolve
    asu "我能问你件事吗？"
    scene club_intro50
    with dissolve
    r1 "问吧。"
    scene club_intro51
    with dissolve
    asu "我们为什么要来这儿？"
    scene club_intro50
    with dissolve
    r1 "从哲学角度？"
    scene club_intro52
    with dissolve
    pause
    scene club_intro53
    with dissolve
    pause
    scene club_intro54
    with dissolve
    pause
    asu "抱歉，什么？"
    scene club_intro50
    with dissolve
    r1 "逗你玩的。"
    r1 "你想玩花样，我也可以。"
    scene club_intro55
    with dissolve
    asu "好吧好吧。"
    asu "不过既然你决定跟我玩，你就该知道。"
    scene club_intro56
    with dissolve
    asu "我很擅长这个。"
    scene club_intro51
    with dissolve
    r1 "那你也该知道一件事。"
    scene club_intro55
    with dissolve
    asu "是吗？什么事？"
    scene club_intro57
    with dissolve
    r1 "我不习惯输。"
    scene club_intro51
    with dissolve
    pause
    scene club_intro58
    with dissolve
    asu "我们的晚餐你想好了吗？"
    scene club_intro60
    with dissolve
    r1 "我得看看我的资金。"
    scene club_intro59
    with dissolve
    asu "我绝不会让你付钱。是我约的你，记得吗？"
    scene club_intro57
    with dissolve
    r1 "我在这圈子里够久了，知道你不付钱的话，最后就得用别的东西付。"
    scene club_intro59
    with dissolve
    pause
    scene club_intro60
    with dissolve
    asu "你真有意思。"
    r1 "怎么说？"
    scene club_intro61
    with dissolve
    asu "我知道你在瞒着什么。我不知道是什么，但它太有意思了！"
    r1 "我没什么好瞒的。"
    scene club_intro60
    with dissolve
    asu "这么说的那些人，瞒得最多。"
    scene club_intro51
    with dissolve
    asu "反正每个人都会有点瞒着的事。"
    scene club_intro63
    with dissolve
    "{color=#FF007F}[asu]{/color}深深吸了口气。"
    scene club_intro64
    with dissolve
    asu "不过看到带领我们的不是个彻底的笨蛋，还是挺不错的。"
    play sound "audio/watersplash.ogg"
    scene club_intro61
    with dissolve
    r1 "你第一次见到我的时候还以为我是笨蛋吧？"
    scene club_intro60
    with dissolve
    asu "我没那么自大。"
    r1 "所以你确实很自大。"
    scene club_intro60
    with dissolve
    asu "我倒觉得刚刚好。"
    scene club_intro59
    with dissolve
    asu "你也差不了多少。"
    asu "「我不习惯输？」"
    asu "听起来很自大。"
    scene club_intro60
    with dissolve
    asu "不过我相信这是你应得的。"
    asu "傲慢是挣来的。"
    asu "傲慢无礼可不是。"
    asu "你肯定懂这个道理。"
    scene club_intro61
    with dissolve
    asu "我能再问一个问题吗？"
    r1 "问。"
    scene club_intro59
    with dissolve
    asu "你以前是干什么的？特种部队？"
    scene club_intro57
    with dissolve
    r1 "我可以告诉你。但那样我就得杀了你。"
    scene club_intro59
    with dissolve
    pause
    scene club_intro66
    with dissolve
    asu "有意思，太有意思了。"
    scene club_intro61
    with dissolve
    r1 "你要真是那种人，肯定不会回答我的问题。"
    asu "不管你怎么答，我都不会信。我想知道的不是你的答案。"
    asu "而是你会怎么答。"
    play sound "audio/watersplash.ogg"
    scene club_intro60
    with dissolve
    r1 "那我是怎么答的？"
    asu "直接。"
    asu "我以为你会很惊讶。"
    asu "或者是不屑一顾。"
    asu "至少也该在回答前停顿一下。"
    asu "但面对奇怪的问题立刻就答？"
    asu "这种反应速度可是很稀有的。"
    r1 "因为我是从动画里学的。"
    scene club_intro67
    with dissolve
    pause
    scene club_intro68
    with hpunch
    lila "喂——！"
    scene club_intro69
    with hpunch
    asu "天哪，[lila!u]！"
    scene club_intro70
    with dissolve
    lila "所以，你们俩在聊什么呢？"
    scene club_intro73
    with dissolve
    asu "哦！我们刚才在聊你们婚——"
    scene club_intro71
    with hpunch
    lila "{size=-7}喂，闭嘴！{/size}"
    scene club_intro72
    with dissolve
    lila "嘿嘿！我看[asu]是忘了吃药！"
    lila "可怜虫。别理她了！"
    r1 "我们得快点。我还有一个地方要带你们看。"
    
    
    scene black
    pause
    play sound "audio/lightswitch.ogg"
    scene club_intro74
    pause
    play sound "audio/spotlight.ogg"
    scene club_intro75
    pause
    scene club_intro76
    with dissolve
    ash "我都不知道校园里还有这么大个地方。"
    lila "是啊，我爸跟我说过这几年停用了不少设施，不过他在这儿读书的时候有个很大的格斗馆。"
    lila "我记得还有拳击台。"
    scene club_intro77
    with dissolve
    r1 "拳击台在别的地方。"
    scene club_intro78
    with dissolve
    lila "对！"
    scene club_intro79
    with dissolve
    lila "有时候我们会忘了这个地方有多大！"
    scene club_intro80
    with dissolve
    ash "我们能进去吗？"
    r1 "当然。够干净了。"
    scene club_intro80_1
    ash "干净……够？"
    scene club_intro81
    with dissolve
    pause
    scene club_intro82
    with dissolve
    asu "谁教你们进去之前要先鞠个躬的？"
    scene club_intro83
    with dissolve
    ja "谁不知道啊，笨蛋！"
    scene club_intro84
    with dissolve
    ja "还有上垫子之前要先脱鞋。"
    scene club_intro85
    with dissolve
    pause
    scene club_intro86
    with dissolve
    pause
    scene club_intro87
    with dissolve
    pause
    scene club_intro88
    with dissolve
    pause
    scene club_intro89
    with dissolve
    pause
    scene club_intro90
    with dissolve
    pause
    asu "闭嘴！"
    scene club_intro91
    with dissolve
    pause
    scene club_intro90
    with dissolve
    asu "你开玩笑吧！"
    scene club_intro92
    with hpunch
    pause
    scene club_intro92_1
    with hpunch
    pause
    scene club_intro93
    with dissolve
    pause
    scene club_intro94
    with dissolve
    asu "我们什么时候有这些东西了？"
    scene club_intro85
    with dissolve
    r1 "你会用吗？"
    scene club_intro95
    with dissolve
    asu "你开玩笑吧？"
    play music "audio/drumswar.ogg" fadein 15 volume 0.5
    asu "我爸想要个儿子。"
    scene club_intro96
    with dissolve
    tom "我想看看。"
    scene club_intro97
    with dissolve
    ash "[tom]……"
    scene club_intro98
    with dissolve
    tom "放轻松！我又不是要伤害她。"
    scene club_intro95
    with dissolve
    asu "我觉得她更担心你。"
    scene club_intro100
    with dissolve
    tom "再说了，这只是运动而已！"
    scene club_intro99
    with dissolve
    ja "拜托，老兄。"
    ja "你块头是她两倍大。"
    scene club_intro95
    with dissolve
    asu "没事的，Jaz。让他来。"
    scene club_intro99
    with dissolve
    tom "看吧？"
    scene club_intro101
    with dissolve
    pause
    scene club_intro102
    with dissolve
    lila "你确定这是个好主意？"
    scene club_intro103
    with dissolve
    ash "是啊，来吧。他可能会伤到她。"
    scene club_intro102
    with dissolve
    lila "我说的不是她。"
    scene club_intro104
    with dissolve
    r1 "至少对其中一个人来说会是一堂好课。"
    r1 "不过要是我觉得可能危险，我会叫停。"
    scene club_intro105
    with dissolve
    pause
    scene club_intro106
    with dissolve
    pause
    scene club_intro107
    with dissolve
    pause
    scene club_intro108
    with dissolve
    ash "你至少定几条规则吧？"
    scene club_intro109
    with dissolve
    r1 "[asu]！你能把规则告诉他吗？"
    scene club_intro110
    with dissolve
    asu "哦！很简单！"
    scene club_intro111
    with dissolve
    asu "这是{i}木刀{/i}。也叫{i}竹刀{/i}。随便啦。"
    asu "跟{i}竹剑{/i}不一样，这东西打起来很疼。"
    asu "所以既然我们没穿护具，就不能真的打到对方。"
    scene club_intro112
    with dissolve
    asu "必须在击中之前停下。"
    asu "而割到一次就算一次击倒。"
    asu "摔投和压制可以，但不算结束比赛。"
    scene club_intro113
    tom "听着，我可不是第一次混这行。"
    scene club_intro111
    with dissolve
    asu "哦！那好吧。"
    scene club_intro114
    with dissolve
    pause
    scene club_intro121
    with dissolve
    pause
    scene club_intro122
    with dissolve
    pause
    scene club_intro115
    asu "你确定以前干过这个？"
    tom "什么时候开始？"
    asu "你准备好就行。"
    scene club_intro116
    with dissolve
    ju "太酷了！"
    scene club_intro114
    with dissolve
    pause
    scene club_intro117
    with dissolve
    pause
    play sound "audio/bokkenhit.ogg"
    scene club_intro118
    pause
    play sound "audio/swordswing.ogg"
    scene club_intro119
    pause
    scene club_intro120
    asu "看来这局算我赢。"
    scene club_intro123
    with dissolve
    asu "再来一次？"
    scene club_intro124
    with dissolve
    pause
    scene club_intro125
    with dissolve
    tom "你他妈怎么做到的？"
    scene club_intro123
    with dissolve
    asu "来啊！别现在才怕！"
    scene club_intro126
    with dissolve
    tom "好，再来一次。"
    tom "既然你那么厉害，我也不留手了。"
    scene club_intro115
    with dissolve
    asu "你确定自己知道在干什么？"
    asu "这可不是棒球。"
    scene club_intro127
    with dissolve
    tom "走着瞧。"
    play music "audio/drumswar.ogg" fadein 15 volume 0.5
    scene club_intro128
    with dissolve
    pause
    scene club_intro129
    with dissolve
    pause
    play sound "audio/clenching.ogg"
    scene club_intro130
    with dissolve
    pause
    scene club_intro131
    with dissolve
    pause
    scene club_intro132
    with dissolve
    pause
    scene club_intro133
    with dissolve
    pause
    scene club_intro134
    with dissolve
    pause
    scene club_intro135
    with dissolve
    pause
    scene club_intro136
    with dissolve
    pause
    scene club_intro137
    with dissolve
    ash "要阻止他们吗？"
    scene club_intro138
    with dissolve
    ash "还是……做点什么？"
    scene club_intro139
    with dissolve
    lila "不用。"
    lila "[asu]从出生起就在训练了。"
    lila "我可不觉得她应付他会吃力。"
    scene club_intro138
    with dissolve
    ash "等等，什么？"
    scene club_intro139
    with dissolve
    lila "对啊。她爸是七段剑道。"
    lila "她应付他绰绰有余。"
    scene club_intro140
    with dissolve
    ash "段是什么鬼？"
    scene club_intro139
    with dissolve
    lila "那是……"
    lila "我也不知道。"
    lila "某种阶段或者毕业？八段是最高段位。"
    scene club_intro140
    with dissolve
    ash "什……"
    scene club_intro141
    with dissolve
    ash "我们说的是同一个[asu]吗？"
    scene club_intro139
    with dissolve
    lila "别被她的外表骗了。"
    scene club_intro143
    with dissolve
    lila "[asu]可是条鲨鱼。"
    scene club_intro142
    with dissolve
    lila "她只是在逗他玩。"
    lila "我更担心[tom]不知道该怎么接受输给她。"
    lila "毕竟她可是世界冠军。"
    scene club_intro140
    with dissolve
    ash "什么？我怎么从来不知道？"
    scene club_intro139
    with dissolve
    lila "那你说得出几个世界冠军的名字？"
    lila "你知道上一届世界马术锦标赛是谁拿的冠军吗？"
    scene club_intro138
    with dissolve
    pause
    scene club_intro141
    with dissolve
    ash "……你说得对。"
    scene club_intro142
    with dissolve
    lila "剑道是很小众的运动。"
    lila "我每次比赛都去现场，所以才知道。"
    lila "你今年才认识她。"
    lila "而我从小就认识她。"
    scene club_intro144
    with dissolve
    lila "而且她的眼睛有种特别的东西。"
    lila "我也说不清具体是什么。"
    lila "但如果你真的仔细看她的眼睛。"
    scene club_intro145
    with dissolve
    lila "你就会发现她身上有些不一样。"
    scene club_intro143
    with dissolve
    asu "别让女士久等，[tom]。"
    scene club_intro127
    with dissolve
    pause
    play sound "audio/swordswing.ogg"
    scene club_intro146
    pause
    play sound "audio/fastmove1.ogg"
    scene club_intro147
    pause
    scene club_intro148
    with dissolve
    pause
    play sound "audio/throw1.ogg"
    scene club_intro149
    with dissolve
    pause
    play sound "audio/fastmove1.ogg"
    scene club_intro150
    pause
    play sound "audio/throw2.ogg"
    scene club_intro151
    with hpunch
    pause
    scene club_intro152
    with dissolve
    pause
    asu "这局又算我的。"
    scene club_intro153
    with dissolve
    pause
    scene club_intro154
    with dissolve
    asu "再来一次？我看你已经有点上手了。"
    scene club_intro155
    with dissolve
    tom "搞什么？你刚才明明能伤到我！"
    scene club_intro154
    with dissolve
    asu "别撒娇了。我只有你一半大，伤不了你的。"
    scene club_intro145
    with dissolve
    pause
    scene club_intro156
    with dissolve
    pause
    scene club_intro157
    with dissolve
    pause
    scene club_intro158
    with dissolve
    pause
    scene club_intro107
    with dissolve
    pause
    scene club_intro159
    with dissolve
    pause
    scene club_intro155
    with dissolve
    tom "喂，你这个小……"
    scene club_intro160
    r1 "够了。"
    r1 "把剑给我，[tom]。你输得明明白白。"
    scene club_intro161
    with dissolve
    tom "行！拿去！"
    scene club_intro162
    with dissolve
    tom "谁会用剑啊。无用的运动。"
    asu "大概只有那个揍了你一顿的女孩吧。"
    tom "对！谁在乎！"
    scene club_intro163
    with dissolve
    asu "要来试试吗，先生？"
    scene club_intro164
    with dissolve
    r1 "没人教过你别挑战段位比你高的人吗？"
    scene club_intro165
    with dissolve
    asu "段位更高？"
    scene club_intro166
    with dissolve
    r1 "不管怎样，我可不是来揍自己学生的。"
    scene club_intro167
    asu "我给学校捐两万。"
    scene club_intro168
    with hpunch
    "{color=#FF007F}[ja]{/color} {color=#FFF}和{/color} {color=#FF007F}[ash]{/color}" "什么情况？"
    scene club_intro169
    ash "她是在虚张声势吧？"
    scene club_intro170
    with dissolve
    lila "不是。"
    scene club_intro169
    with dissolve
    ash "她真有那么多钱？"
    scene club_intro174
    with dissolve
    pause
    scene club_intro175
    with dissolve
    pause
    scene club_intro176
    with dissolve
    ash "……该死。"
    scene club_intro171
    with dissolve
    pause
    scene club_intro172
    with dissolve
    r1 "我有个更好的主意。"
    scene club_intro209
    with dissolve
    r1 "{size=-7}不要钱，换一个人情怎么样？{/size}"
    r1 "{size=-7}我随时都可以来收，而且绝不追问。{/size}"
    asu "{size=-7}呜……我喜欢。{/size}"
    asu "{size=-7}我欣赏那种认为人情比金钱更值钱的人。{/size}"
    scene club_intro173
    with dissolve
    r1 "成交？"
    scene club_intro167
    asu "那我赢了怎么办？"
    scene club_intro173
    r1 "一样。"
    scene club_intro167
    asu "成交。"
    scene club_intro173
    with dissolve
    r1 "那就各就各位吧。"
    scene club_intro177
    with dissolve
    lila "有意思起来了。"
    scene club_intro178
    with dissolve
    pause
    scene club_intro179
    with dissolve
    asu "就一只手？"
    scene club_intro180
    with dissolve
    r1 "别担心，我不会伤到你。"
    scene club_intro210
    with dissolve
    tom "$200 [asu]把他揍飞了。"
    scene club_intro181
    with dissolve
    pause
    asu "那双眼睛……"
    scene club_intro182
    with dissolve
    pause
    scene club_intro181
    with dissolve
    pause
    scene club_intro182
    r1 "[asu]，我在等。"
    scene club_intro181
    asu "哦，抱歉！"
    scene club_intro183
    with dissolve
    pause
    play sound "audio/bokkenhit.ogg"
    scene club_intro184
    pause
    play sound "audio/fastmove1.ogg"
    scene club_intro185
    pause
    play sound "audio/bokkenhit.ogg"
    scene club_intro186
    pause
    play sound "audio/fastmove1.ogg"
    scene club_intro187
    pause
    scene club_intro188
    with dissolve
    pause
    play sound "audio/fastmove1.ogg"
    scene club_intro189
    pause
    play sound "audio/fastmove1.ogg"
    scene club_intro190
    pause
    play sound "audio/bokkenhit.ogg"
    scene club_intro191
    with hpunch
    pause
    play sound "audio/fastmove1.ogg"
    scene club_intro192
    pause
    play sound "audio/throw2.ogg"
    scene club_intro193
    with hpunch
    pause
    play sound "audio/fastmove1.ogg"
    scene club_intro194
    pause
    scene club_intro195
    pause
    scene club_intro196
    lila "什……？"
    scene club_intro197
    pause
    scene club_intro199
    r1 "这回合算我的。"
    r1 "还想再来一次吗？"
    scene club_intro195
    asu "你是在哪……"
    scene club_intro198
    asu "你到底是在哪学的这种打法？"
    scene club_intro200
    with dissolve
    ash "你说世界冠军来着？"
    scene club_intro201
    with dissolve
    lila "这……完全说不通。"
    scene club_intro199
    with dissolve
    r1 "大概是新手运气好吧。"
    scene club_intro202
    with dissolve
    r1 "你的应对相当不错。我很欣赏。"
    r1 "打得漂亮吗？"
    scene club_intro203
    with dissolve
    asu "打？！"
    asu "你三招就把我解决了。那根本不叫打。"
    asu "那是……完全另一个层级的东西。"
    scene club_intro202
    with dissolve
    r1 "胡说。"
    r1 "来，把手给我。"
    scene club_intro204
    with dissolve
    r1 "打得很漂亮。谢谢。"
    scene club_intro205
    with dissolve
    pause
    scene club_intro206
    with dissolve
    pause
    scene club_intro207
    with dissolve
    pause
    scene club_intro208
    with dissolve
    asu "谢谢您，先生。"
    scene club_intro210
    with dissolve
    tom "这家伙到底是谁啊？"
    ch "完全不知道。但我会查清楚的。"
    stop music fadeout 5
    scene club_intro211
    with dissolve
    ash "喂，[lila]。"
    scene club_intro212
    with dissolve
    lila "嗯？"
    ash "你前任来了。"
    scene club_intro213
    with dissolve
    pause
    scene club_intro214
    with dissolve
    lila "呃啊……操……"
    ash "要我拦住他吗？"
    lila "没事……我自己处理。"
    scene club_intro215
    with dissolve
    ch "喂，[lila]。"
    ch "这家伙是怎么回事？"
    scene club_intro216
    with dissolve
    lila "你想干嘛，[ch]？"
    ch "我想知道你跟那家伙是什么关系。"
    lila "你脑子坏了吗？这种话也问得出口？"
    ch "我看见你跟他在一起。"
    lila "那又怎样？！"
    ch "我看到你们靠得很近。"
    lila "老兄，那根本说明不了什么。你什么都没看见。"
    lila "而且你知道吗？关你什么事？"
    lila "管好你自己。我现在最不需要的就是你在背后嚼舌根。"
    ch "[lila]，拜托了。"
    lila "别跟我来这套，[lila]。"
    lila "还有你他妈冷静点。我们之间什么都没有。"
    lila "我也没欠你一个解释。"
    ch "你这话到底什么意思？"
    lila "意思是你该过好你自己的日子，少管闲事。"
    lila "我的人生已经没你说话的份了。"
    ch "我看见你主动去勾搭他！"
    lila "老兄，你他妈给我闭嘴！会被人听到的！"
    scene club_intro217
    with dissolve
    asu "你知道这事没完，对吧？"
    asu "我一定要知道你到底在哪学的这种打法。"
    r1 "我们晚餐的时候有的是时间聊。"
    scene club_intro218
    with hpunch
    ch "你必须告诉我到底怎么回事！"
    lila "我才不告诉你！"
    scene club_intro219
    ash "喂！退开！"
    scene club_intro220
    with hpunch
    ch "把你的脏手从我身上拿开！"
    scene club_intro221
    with hpunch
    lila "喂！别碰她！"
    ch "你他妈搞清楚自己的位置！"
    scene club_intro223
    ch "你家根本没资格待在这所学院！"
    ch "要不是[tom]他爸替你把贷款摆平，你连门都进不来！"
    play sound "audio/throw2.ogg"
    scene club_intro222
    with hpunch
    pause
    scene club_intro224
    ash "{size=-7}操！我的手！{/size}"
    scene club_intro225
    ash "{size=-7}操！我好像断了！{/size}"
    ash "{size=-7}操！操！操！操！操！{/size}"
    scene club_intro226
    ash "你以为你比我强？猜猜看！"
    ash "你能在这儿还不是靠你那该死的老爸！"
    ash "你那可悲的小人生里没有一样东西是你自己挣来的！"
    ash "你身上没有半点特别！你跟这所破学院里其他人一样，活在父母的阴影下！"
    ash "你绝对没有任何特别之处！"
    scene club_intro227
    ash "还有你知道吗，你这个该死的小混蛋？！"
    ash "我他妈是靠自己挣来这个位置的！"
    ash "所以你他妈去死吧！"
    scene club_intro228
    with dissolve
    pause
    scene club_intro229
    with dissolve
    ch "{size=-7}该死的婊子……{/size}"
    scene club_intro230
    lila "大家冷静点！"
    play sound "audio/clenching.ogg"
    scene club_intro231
    pause
    scene club_intro232
    with dissolve
    pause
    play sound "audio/fastmove1.ogg"
    scene club_intro233
    with hpunch
    pause
    play sound "audio/throw2.ogg"
    scene club_intro234
    pause
    r2 "小伙子，你最好仔细想想你下一步要做什么。"
    play sound "audio/clenching.ogg"
    scene club_intro236
    pause
    scene club_intro235
    r2 "你会发现我没看上去那么好耐心。"
    scene club_intro234
    r2 "明白了吗？"
    ch "明白了！"
    scene club_intro236
    r2 "很好。"
    r2 "那么……"
    scene club_intro237
    r1 "你受伤了吗？"
    ch "没有。"
    r1 "那就好。"
    r1 "这事我以后再处理。"
    scene club_intro238
    r1 "我希望你们都能像个成年人的样子。"
    r1 "如果你们不想被卷进来，我希望你们守口如瓶。"
    r1 "关于改进我们学校的事，改天再谈。"
    r1 "暂时就这些。"
    r1 "都散了。"
    scene club_intro237
    r1 "想去医务室就去医务室，想写报告就写。"
    ch "好的。"
    scene club_intro239
    r1 "你除外，[ash]。"
    r1 "留下。"
    scene club_intro240
    with dissolve
    pause
    scene club_intro241
    with dissolve
    ash "真的没事。"
    ash "我待会儿再去找你们。"
    scene club_intro242
    with dissolve
    pause
    scene club_intro243
    with dissolve
    pause
    scene club_intro244
    with dissolve
    pause
    scene club_intro245
    with dissolve
    pause
    ash "..."
    ash "他活该。"
    r1 "看着我。"
    ash "..."
    scene club_intro246
    with dissolve
    pause
    scene club_intro245
    with dissolve
    pause
    scene club_intro247
    with dissolve
    ash "他活该。"
    r1 "来，让我看看你的手。"
    scene club_intro248
    with dissolve
    pause
    scene club_intro249
    with dissolve
    pause
    scene club_intro250
    with dissolve
    pause
    scene club_intro251
    with dissolve
    pause
    scene club_intro252
    with hpunch
    ash "你他妈在干……"
    scene club_intro253
    with dissolve
    pause
    scene club_intro254
    with dissolve
    pause
    scene club_intro255
    with dissolve
    ash "{size=-7}……什么？{/size}"
    scene club_intro256
    with dissolve
    r1 "让我好好看看你的手。"
    scene club_intro257
    with dissolve
    pause
    scene club_intro258
    with dissolve
    pause
    scene club_intro259
    with dissolve
    pause
    scene club_intro256
    with dissolve
    r1 "看起来没断。手指能动吗？"
    scene club_intro260
    with dissolve
    ash "有点疼。"
    r1 "有点疼没关系。"
    r1 "但我觉得你可能有点脱臼。"
    scene club_intro261
    with dissolve
    r1 "会有点疼，忍着点好吗？"
    r1 "一直看着我。我数到五。"
    r1 "一。"
    scene club_intro260
    r1 "二。"
    play sound "audio/bone.mp3"
    scene club_intro262
    with hpunch
    pause
    scene club_intro263
    pause
    scene club_intro264
    with dissolve
    pause
    scene club_intro265
    with dissolve
    ash "你不是说要数到五吗？"
    scene club_intro266
    with dissolve
    r1 "我从来没说过我数学好。"
    ash "我讨厌你……"
    r1 "好了……可以放开我了吗？"
    scene club_intro267
    with dissolve
    r1 "我得检查一下你的手被我弄成什么样了。"
    ash "不行。"
    ash "很疼。"
    r1 "[ash]……"
    ash "好吧！只是……别再那样了。"
    r1 "我不会再。"
    scene club_intro269
    with dissolve
    pause
    scene club_intro270
    with dissolve
    pause
    scene club_intro271
    with dissolve
    pause
    scene club_intro270
    with dissolve
    pause
    scene club_intro272
    with dissolve
    ash "所以……我是不是……？"
    ash "我会被退学吗？"
    scene club_intro273
    with dissolve
    pause
    ash "……？"
    scene club_intro274
    with dissolve
    ash "[r1]？"
    scene club_intro275
    r1 "你手上应该敷点冰。"
    scene club_intro274
    with dissolve
    ash "[r1]，我会被退学吗？"
    scene club_intro275
    r1 "我好像有绷带。不过最好还是让[isa]在医务室处理。"
    scene club_intro274
    with dissolve
    ash "我不想被退学。"
    scene club_intro275
    with dissolve
    pause
    scene club_intro276
    with dissolve
    pause
    scene club_intro275
    with dissolve
    r1 "从我来这儿的第一天起，我就想揍那小子一顿。"
    r1 "装腔作势、自以为是的臭小鬼。"
    r1 "我实在没耐心对付一个靠出身和经济地位就觉得自己高人一等的巨婴。"
    scene club_intro276
    with dissolve
    r1 "但你也不该动手打他。"
    scene club_intro274
    with dissolve
    ash "我知道。"
    scene club_intro276
    with dissolve
    r1 "知道是不够的。"
    scene club_intro275
    with dissolve
    r1 "我刚来这里的时候，以为这个地方会完全不一样。"
    r1 "我以为你们都是一帮自命不凡的富家子弟。"
    r1 "我完全没想到，也没想过会在这里遇到你、[ja]或者她姐姐这样的人。"
    r1 "我更没想过会遇到[lila]或[asu]那样的人。"
    r1 "[asu]看起来确实很自大。但如果她真是[lila]说的那种世界冠军，那她的人品就比我原本以为的厚重得多。"
    scene club_intro274
    with dissolve
    ash "为什么？"
    scene club_intro275
    with dissolve
    r1 "想象一下你在她那个年纪就拿了世界冠军。光这一点就足以让人自满。"
    r1 "再想象一下，你在比赛之外、在所有人面前，输给了一个陌生人。"
    r1 "她本可以恼羞成怒，可以发火，可以否认，什么都行。"
    scene club_intro276
    with dissolve
    r1 "但她却出于尊重向我低头致意。"
    r1 "鞠躬在西方文化里并不常见。但她有一半日本血统，这就说得通了。"
    scene club_intro275
    with dissolve
    r1 "而[lila]是个特别温柔的姑娘。"
    r1 "换成别人，本城最有影响力的政治家的女儿，很容易觉得全世界都该围着她转。"
    scene club_intro276
    with dissolve
    r1 "但她非常脚踏实地。"
    scene club_intro275
    with dissolve
    r1 "还有像你和[ja]这样的人。"
    r1 "你们不是在这样的生活里长大的，而是在成年初期才开始体验它。"
    scene club_intro277
    with dissolve
    r1 "阿什莉，你得做得比这更好。"
    r1 "你必须更聪明一点。"
    scene club_intro274
    with dissolve
    r1 "不然你在这个地方活不下去。"
    r1 "这里是蛇窝。一旦被激怒，它们会反咬一口。"
    r1 "你会站在原地虚弱下去，直到被它们的毒液活活蚀死。"
    scene club_intro278
    with dissolve
    ash "所以，我是不是就该忍气吞声地接受他说的那些屁话？"
    scene club_intro274
    with dissolve
    r1 "不是。但你要明白，当着所有人的面一拳打在他脸上时，他说了什么就不重要了。"
    r1 "别人只会看见你做了什么。"
    r1 "虽然他确实活该，但在所有人面前动手，反倒显得你是错的那个。"
    r1 "而且我敢说他不会就这么咽下这口气。"
    scene club_intro276
    with dissolve
    r1 "你本该让我来处理。"
    play music "audio/Castle in the sky.ogg" fadein 4 volume 0.1
    scene club_intro274
    with dissolve
    pause
    scene club_intro279
    with dissolve
    pause
    scene club_intro280
    with dissolve
    pause
    menu:
        "安慰她。 {p=0.0}{color=#00ff00}([ash] 好感 +2){/color}":
            play sound "audio/Lockpick_Success.ogg" volume 0.1
            show screen notifyEx( msg="[ash]的{color=#00ff00}好感{/color}上升了{color=#00ff00}2{/color}点！" )
            $love_ash +=2
            scene club_intro281
            with dissolve
            r1 "嘿，没事的。不用哭。"
            r1 "我会保护你。不会有事的。"
        "自己解决。 {p=0.0}{color=#ff0000}([ash] 堕落 +2){/color}":
            play sound "audio/Lockpick_Success.ogg" volume 0.1
            show screen notifyEx( msg="[ash]的{color=#ff0000}堕落{/color}上升了{color=#00ff00}2{/color}点！" )
            $corruption_ash +=2
            scene club_intro281
            with dissolve
            r1 "你不用担心。我会替你摆平。"
            r1 "他不敢碰你。我保证。"
    scene club_intro282
    with dissolve
    ash "不是那个……"
    ash "我只是……"
    scene club_intro283
    with dissolve
    pause
    ash "他怎么能对我说那种话？"
    ash "他让我觉得自己像是[tom]的财产！"
    ash "而且他没说错！我觉得自己真的就是！"
    ash "要不是他，我永远不会来这种地方！"
    ash "而我因为我爸的关系，不得不忍受跟他待在一起！"
    ash "我被困在这里了！"
    ash "我……我喘不上气。"
    scene club_intro284
    with dissolve
    pause
    scene club_intro285
    with dissolve
    pause
    scene club_intro286
    with dissolve
    pause
    scene club_intro287
    with dissolve
    pause
    scene club_intro288
    with dissolve
    pause
    scene club_intro289
    with dissolve
    pause
    scene club_intro290
    with dissolve
    pause
    scene club_intro291
    with dissolve
    pause
    scene club_intro292
    with dissolve
    pause
    scene club_intro290
    with dissolve
    r1 "人生不可能一帆风顺到不发生任何事。"
    r1 "[tom]也许是你今天会在这里的原因。"
    r1 "但他决定不了你的命运。"
    scene club_intro293
    with dissolve
    r1 "所以别再让他支配你的人生了。"
    r1 "你已经在这里了。就用你已经经历的一切，做你认为最好的选择。"
    scene club_intro292
    with dissolve
    pause
    scene club_intro301
    with Dissolve(1)
    pause
    scene club_intro302
    with Dissolve(1)
    pause
    scene club_intro268
    with dissolve
    ash "为什么……"
    ash "你为什么要做这些？"
    ash "你到底是怎么做到的？"
    r1 "[ash]……"
    ash "你看起来就像是直接从书里走出来的。"
    ash "你凭空就出现了。"
    ash "你会打架。"
    ash "你非常聪明。"
    ash "我们对你一无所知……一切都太神秘了。"
    scene club_intro294
    with dissolve
    ash "而你对我……"
    ash "你让我觉得……"
    scene club_intro295
    with dissolve
    ash "你为什么要这样？"
    menu:
        "「我会一直在你身边。」 {p=0.0}{color=#00ff00}([ash] 好感 +2){/color}":
            play sound "audio/Lockpick_Success.ogg" volume 0.1
            show screen notifyEx( msg="[ash]的{color=#00ff00}好感{/color}上升了{color=#00ff00}2{/color}点！" )
            #$ renpy.notify (str(ash) + "的好感上升了2点！")
            $love_ash +=2
            scene club_intro296
            with dissolve
            r1 "听着，现在你可能感觉不到。"
            r1 "但你已经走到这一步了。"
            r1 "我相信前方有很好的东西在等着你。"
            r1 "等你走到那一刻，我会在你身边。"
            r1 "你值得更好的。"
            r1 "而我会让你看到。"
        "「我会保护你。」 {p=0.0}{color=#ff0000}([ash] 堕落 +2){/color}":
            play sound "audio/Lockpick_Success.ogg" volume 0.1
            show screen notifyEx( msg="[ash]的{color=#ff0000}堕落{/color}上升了{color=#00ff00}2{/color}点！" )
            $corruption_ash +=2
            scene club_intro296
            with dissolve
            r1 "听着，我知道我们认识的时间还很短。"
            r1 "你还不够了解我，不知道我的理由。"
            r1 "但只要待在我身边，信任我。"
            r1 "我就会保护你。"
            r1 "眼下这件事，你只信任我一个人。"
            r1 "所以也只有我能帮你扛过去。"
            r1 "你值得更好的。"
            r1 "而我会让你看到更好的。"
    scene club_intro297
    with dissolve
    pause
    ash "你能……抱抱我吗？"
    scene club_intro298
    with dissolve
    pause
    scene club_intro299
    with dissolve
    ash "让我就这样待一会儿，求你了……"
    r1 "当然。"
    ash "谢谢，[r1]……"
    scene club_intro300
    with Dissolve (2)
    pause
    scene black
    with Dissolve (3)
    pause
    
    jump day2_update
    
    
    #ja_nvl "{image=phone/Selfie1.png}"
    
    
    
    
    
    
    
    