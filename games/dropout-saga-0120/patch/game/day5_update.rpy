label day5_update:
    label webringwar_day5:
        $ unlock_bust_char_image("lila", 1)
        $ unlock_bust_char_image("isa", 1)
        $ unlock_bust_char_image("sophia", 1)
        $ unlock_bust_char_image("ash", 1)
        $ unlock_bust_char_image("ava", 1)
        $ unlock_bust_char_image("ju", 1)
        $ unlock_bust_char_image("ingrid", 1)
        $ unlock_bust_char_image("ingrid", 1)
        "我们已经站在战争边缘。不管打不打仗，现在正是时候去掌握我们的资源，以及与其他家族和成员的关系。"
        #window hide
        #$quick_menu = False
        #show screen LIinfo with Dissolve(1)
        scene tutorial_0 with Dissolve(1)
        "我们可以查看「我们认为别人怎么看我们」以及「我们有多少资源」。"
        scene black with dissolve
        scene tutorial_1 with Dissolve(1)
        "现在我们只能看到跟我们最亲近的人。但之后我们可以切换到其他对象，记录我们在这座城市各派势力中的情报。"
        "我们可以查看「我们认为别人怎么看我们」以及「我们有多少资源」。"
        "第一页会列出每一位「LI」以及我们目前对他们的想法。"
        "随着和他们的接触，我们对他们的想法也会不时改变。"
        scene black with dissolve
        scene tutorial_3 with Dissolve(1)
        "嗯……[ingrid]已经灰掉了，原因很明显。{nw=2}"
        "在这里可以看到年龄、身高、体重、所属势力等等。"
        "你也可以点击她的半身像更换。随着剧情推进，你会解锁新的半身像。"
        "另外记住，他们的所属势力会随我们的行动而改变。"
        "最后，她们的爱意或堕落值，以及各势力的声望，都会在这些界面里以阈值的形式显示。"
        "累积到足够的点数后，就能解锁下一个阶段。"
        "大概就是这些！"
        scene black with Dissolve(1)
        pause 0.5
        stop music fadeout 5
        show screen LIinfo
        scene webringwar_day5_1
        with Dissolve(2)
        pause
        scene webringwar_day5_2
        pause
        play sound "audio/revolvercock.ogg"
        $ unlock_bust_char_image("lila", 1)
        #$ LI_bust_background["lila"] = "lila_bio00"
        #$ current_bust_LI["lila"] = 1
        scene webringwar_day5_3
        pause
        scene webringwar_day5_4
        pause
        r1 "这一件无可挑剔。"
        scene webringwar_day5_5
        with Dissolve(1)
        sophia "谢了。"
        scene webringwar_day5_6
        pause
        sophia "我自己修好的。"
        scene webringwar_day5_7
        with Dissolve(1)
        sophia "这一件还得再调一调。"
        scene webringwar_day5_8
        with Dissolve(1)
        r1 "暂时够用了。"
        scene webringwar_day5_9
        with Dissolve(1)
        sophia "嗯……是啊。"
        scene webringwar_day5_10
        with Dissolve(1)
        ava "提醒我一下，计划是什么来着？"
        scene webringwar_day5_11
        with Dissolve(1)
        sophia "我把我们的枪检查完。"
        sophia "然后我去查有没有可能预示战争的委托。"
        scene webringwar_day5_12
        with Dissolve(1)
        r1 "我去见俄罗斯人。"
        scene webringwar_day5_10
        with Dissolve(1)
        ava "而我……"
        scene webringwar_day5_13
        with Dissolve(1)
        sophia "……待在家里。"
        sophia "你还没准备好参与任何行动。"
        sophia "而且两件事都得我们单独去做。"
        scene webringwar_day5_14
        with Dissolve(1)
        ava "可是我……"
        scene webringwar_day5_12
        with Dissolve(1)
        r1 "没得商量。"
        r1 "你还没准备好。"
        scene webringwar_day5_15
        with Dissolve(1)
        pause
        scene webringwar_day5_16
        with Dissolve(1)
        ava "{size=-7}[ava]，你根本还没准备好参与任何行动……{/size}"
        scene webringwar_day5_17
        with Dissolve(1)
        ava "{size=-7}[ava]，没得商量……{/size}"
        ava "{size=-7}[ava]，你就是个废物……{/size}"
        scene webringwar_day5_18
        with Dissolve(1)
        ava "{size=-7}Right...{/size}"
        scene webringwar_day5_19
        with Dissolve(1)
        sophia "今天需要掩护吗？"
        scene webringwar_day5_8
        with Dissolve(1)
        r1 "不用。会上狼群会替我撑腰。"
        scene webringwar_day5_20
        with Dissolve(1)
        sophia "很好。"
        scene webringwar_day5_8
        with Dissolve(1)
        r1 "[sophia]，放轻松。"
        play sound "audio/hitwood1.ogg"
        scene webringwar_day5_21
        with hpunch
        sophia "我怎么可能放得下来？"
        scene webringwar_day5_22
        sophia "我们熬了一整夜。"
        sophia "现在收拾东西的样子，好像真要上战场似的！"
        scene webringwar_day5_23
        sophia "而我们还真有可能真的去打仗！！"
        scene webringwar_day5_24
        with Dissolve(1)
        pause
        scene webringwar_day5_25
        with Dissolve(2)
        pause
        scene webringwar_day5_26
        with Dissolve(1)
        sophia "亲爱的，对不起。我——"
        scene webringwar_day5_25
        r1 "这些够用了。"
        r1 "[k]让我从俄罗斯人那里弄一把枪——做做样子。"
        r1 "我会要求一把精密步枪。"
        scene webringwar_day5_27
        r1 "不知道行不行，但我会试试。"
        r1 "这些枪你整理得非常好。"
        r1 "谢谢你。"
        scene webringwar_day5_28
        with Dissolve(1)
        r1 "我得在[isa]来之前走。"
        r1 "你也该走了。"
        r1 "[ava]会去开门。"
        scene webringwar_day5_29
        with Dissolve(1)
        sophia "诶？"
        scene webringwar_day5_30
        with Dissolve(1)
        r1 "你可以把我们的枪藏进卧室的衣橱里，[ava]。"
        r1 "[sophia]一直在教你怎么处理它们。我相信你知道该怎么做。"
        r1 "子弹是空包弹。不过枪本来就不该上膛拿着。"
        r1 "安全措施。保持好习惯。"
        scene webringwar_day5_31
        with Dissolve(1)
        r1 "等我有机会再细谈。"
        scene webringwar_day5_32
        sophia "喂！"
        scene webringwar_day5_33
        sophia "别这样。"
        scene webringwar_day5_34
        r1 "如果你觉得自己没准备好，就告诉我。"
        r1 "如果你控制不住自己的情绪。"
        r1 "如果你现在扛不住压力。"
        r1 "那你就该待在家里，让我去做我的工作。"
        r1 "你现在这样很不专业，我不会容忍。"
        r1 "如果我不能相信搭档在子弹乱飞时还能保持冷静，我宁可一个人去。"
        scene webringwar_day5_35
        ava "喂！"
        ava "你们两个都给我住手！"
        scene webringwar_day5_36
        pause
        scene webringwar_day5_37
        with Dissolve(1)
        pause
        scene webringwar_day5_38
        with Dissolve(1)
        sophia "其实……"
        sophia "他说得对……"
        sophia "我刚才失控了。"
        scene webringwar_day5_39
        with Dissolve(1)
        pause
        scene webringwar_day5_40
        with Dissolve(1)
        r1 "*啧* 该死……"
        r1 "不……不，我没有。"
        scene webringwar_day5_41
        with Dissolve(1)
        r1 "这个情况压力太大了。"
        r1 "而且我们两个现在都在崩溃边缘。"
        r1 "我不是故意就这么无视你的。"
        r1 "我知道我们会互相伤害。"
        scene webringwar_day5_42
        with Dissolve(1)
        sophia "我们彼此需要……所以就这样吧……"
        sophia "你说呢？"
        scene webringwar_day5_43
        with Dissolve(1)
        pause
        scene webringwar_day5_44
        with Dissolve(2)
        pause
        scene webringwar_day5_45
        with Dissolve(2)
        r1 "嗯……"
        r1 "好。"
        scene webringwar_day5_46
        with Dissolve(1)
        ava "看吧？！也没那么难吧！"
        scene webringwar_day5_47
        with Dissolve(1)
        r1 "我们还不知道会不会开战。"
        r1 "就算气氛已经变了。"
        scene webringwar_day5_48
        with Dissolve(1)
        sophia "先调查，之后再担心。"
        scene webringwar_day5_47
        with Dissolve(1)
        r1 "没错。我们做好最坏的打算。"
        scene webringwar_day5_48
        with Dissolve(1)
        sophia "但也期待最好的结果。"
        scene webringwar_day5_44
        with Dissolve(2)
        play sound "audio/Lockpick_Success.ogg" volume 0.1
        show screen notifyEx( msg="[sophia]的{color=#00ff00}好感{/color}提升了{color=#00ff00}3{/color}点！" )
        $love_sophia+=3
        r1 "我的姑娘。"
        scene webringwar_day5_49
        with Dissolve(1)
        r1 "不过，你真有必要把工具都带上吗？"
        scene webringwar_day5_50
        with Dissolve(1)
        sophia "我得在林子里布一道警戒线。"
        sophia "那边安全吧？不会有野兽吗？"
        r1 "栅栏里面没有。"
        sophia "那我出发前先去那儿干活。"
        scene webringwar_day5_51
        with Dissolve(1)
        ava "呃……警戒线？"
        hide screen notifyEx
        scene webringwar_day5_52
        with Dissolve(1)
        r1 "炸药。"
        scene webringwar_day5_53
        with hpunch
        ava "什么？！"
        scene webringwar_day5_54
        with Dissolve(1)
        sophia "别吓着可怜的孩子。"
        sophia "只是摄像机而已，[ava]。"
        r1 "是吗？哎呀，那真抱歉！"
        scene webringwar_day5_53
        ava "所以不会有炸药了？！"
        ava "对吧？！对吧？！"
        scene webringwar_day5_54
        with Dissolve(1)
        sophia "看看你干的好事？"
        sophia "没有炸货。亲爱的，你可以放心了。"
        scene webringwar_day5_53
        ava "天啊！"
        scene webringwar_day5_55
        with Dissolve(2)
        sophia "你知道吗，在军队里我虽然还是外科医生，但待在军队就意味着你也是战斗人员。"
        sophia "我们的课程里有几堂是关于爆炸物的，但我们从来没有专门学过。"
        sophia "爆炸物这东西就算你懂操作，也他妈的很容易出事。"
        scene webringwar_day5_56
        with Dissolve(1)
        ava "好！我把话说清楚！我不要这屋子里有任何爆炸物！永远不要！"
        ava "明白了吗？！"
        ava "那边那些……那些……我已经让出很大一步了……"
        scene webringwar_day5_56_1
        ava "大规模杀伤性武器就在那边！"
        scene webringwar_day5_55
        with Dissolve(1)
        sophia "亲爱的，我是认真的。"
        sophia "我不碰那种东西。"
        scene webringwar_day5_58
        with Dissolve(1)
        r1 "再说了……我们三个人里，[ingrid]才是真正懂爆炸物的人。"
        scene webringwar_day5_57
        with Dissolve(1)
        ava "抱歉，我们要谈这个吗？"
        ava "我是说……你们还好吗？换个话题也行。"
        scene webringwar_day5_58
        with Dissolve(1)
        r1 "放轻松。这种时候没什么。"
        scene webringwar_day5_60
        ava "你确定？"
        scene webringwar_day5_59
        with Dissolve(1)
        sophia "哦，是啊。"
        sophia "那是一段珍贵的回忆。"
        sophia "现在回想起来，我们当时配合得相当好。"
        sophia "我们每个人都有各自的专长。"
        scene webringwar_day5_61
        with Dissolve(1)
        sophia "你还记得她用狙击步枪时有多狠吗？"
        scene webringwar_day5_58
        with Dissolve(1)
        r1 "{i}Jäger.{/i}"
        scene webringwar_day5_61
        with Dissolve(1)
        sophia "哦！对了！"
        scene webringwar_day5_59
        with Dissolve(1)
        sophia "当年她在德国家族的时候，他们有一个神枪手分队。"
        sophia "他们自称「耶格尔」。"
        sophia "哎呀妈呀。而且她是最厉害的那个！"
        scene webringwar_day5_63
        with Dissolve(1)
        sophia "啊，抱歉。我说的「分队」是指——"
        scene webringwar_day5_57
        ava "更下一级的分队。我知道。"
        ava "而「耶格尔」的意思是「猎人」。"
        scene webringwar_day5_64
        with Dissolve(1)
        pause
        scene webringwar_day5_62
        with Dissolve(1)
        pause
        scene webringwar_day5_58
        with Dissolve(1)
        r1 "别看我，我什么也没说。"
        r1 "前几天她还说什么「皮洛士式胜利」。"
        r1 "我只能承认她脑子够用。"
        scene webringwar_day5_62
        with Dissolve(1)
        sophia "对……"
        scene webringwar_day5_63
        with Dissolve(1)
        sophia "我刚说到……他们队伍里有几个「{i}Spezialkräfte{/i}」的人。"
        sophia "所以她那个分队可不是好惹的。"
        sophia "{i}Spezialkräfte{/i}的意思是——"
        scene webringwar_day5_57
        ava "特种作战部队。我知道。"
        scene webringwar_day5_65
        play sound "audio/dramaticstinger.ogg" volume 0.8
        pause
        scene webringwar_day5_66
        with Dissolve(1)
        sophia "你怎么知道这个？"
        scene webringwar_day5_57
        ava "我只是……就是知道……"
        scene webringwar_day5_67
        #play sound "audio/dramaticstinger.ogg" volume 0.8
        sophia "这已经不是聪明了。"
        sophia "这叫有学识。"
        sophia "你在说什么呢？你会说德语？"
        scene webringwar_day5_68
        ava "不会！我、我只是……就是知道。"
        ava "你一说我就想到这两个词了。"
        stop music fadeout 8
        scene webringwar_day5_67
        with Dissolve(1)
        pause
        scene webringwar_day5_66
        with Dissolve(1)
        sophia "胡说八道！"
        scene webringwar_day5_58
        with Dissolve(1)
        r1 "你多疑了，[sophia]。"
        scene webringwar_day5_68
        ava "我是认真的！"
        ava "而且这个词并不难……「{i}Spezial{/i}」听起来就像「special」……"
        ava "而「{i}kräfte{/i}」嘛……嗯……像是「craft」……"
        ava "我只是把线索连起来了，我发誓！"
        scene webringwar_day5_66
        with Dissolve(1)
        sophia "嗯……"
        scene webringwar_day5_58
        with Dissolve(1)
        r1 "看吧？"
        window hide
        play sound "audio/dial2.ogg"
        pause
        window auto
        stop sound fadeout 2
        scene webringwar_day5_69
        with Dissolve(1)
        r1 "我在听。"
        k "这条线路安全吗？"
        scene webringwar_day5_70
        with Dissolve(2)
        r1 "安全。"
        k "很好。计划有变。"
        k "今天别来这儿。"
        r1 "为什么？"
        k "警方在搞什么「便民」活动，隔三差五就来这儿。"
        k "你现在太受关注了，不能让人看见跟我们在一起。"
        k "我们会另约一次会面。"
        r1 "什么时候？"
        k "定下来我给你打电话。"
        k "我得通知俄罗斯人一声。"
        r1 "那我要从他们那儿弄的东西呢？"
        k "那可以等。"
        r1 "不，不能等。"
        r1 "我有个绝好的机会，我想抓住。"
        k "什么时候？"
        r1 "这个周末。"
        k "我去处理。"
        r1 "谢谢。"
        scene webringwar_day5_71
        with Dissolve(1)
        r1 "好吧……至少今天少了一件要操心的事。"
        sophia "说得好听。"
        r1 "我和俄罗斯人的会面只能先等等。"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "你刚才说的那把步枪，用来干什么？"
        scene webringwar_day5_71
        with Dissolve(1)
        sophia "如果你愿意，我可以弄一把来。"
        sophia "如果你需要的只是一把狙击步枪，那不一定要俄罗斯人的，对吧？"
        r1 "不……"
        scene webringwar_day5_72
        with Dissolve(1)
        r1 "不太是。必须是他们的。"
        sophia "为什么？"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "这有点……让人困惑。在这座城市里，只要不是本地俄罗斯人的俄罗斯枪，不就行了吗？"
        scene webringwar_day5_73
        with Dissolve(1)
        r1 "不……"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "所以呢？……你解释一下啊？"
        scene webringwar_day5_72
        with Dissolve(1)
        r1 "好吧，从头说起。"
        r1 "[k]让我从俄罗斯人那儿买一把枪。"
        r1 "一开始我以为这是为了维持他们和我们之间的商业往来。"
        r1 "后来[k]让我用那把枪去刺杀市长。" 
        scene webringwar_day5_68
        with hpunch
        ava "什么？！"
        scene webringwar_day5_73
        with Dissolve(1)
        r1 "放心，我不是要杀他。"
        scene webringwar_day5_72
        with Dissolve(1)
        r1 "只是「尝试」而已。我不知道为什么。"
        r1 "但我越想越觉得，这可能是个好机会。"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "什么好机会？"
        scene webringwar_day5_74
        with Dissolve(1)
        sophia "好让一切看起来像是俄罗斯人干的。"
        r1 "对。"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "可是……那只是一把枪……"
        ava "用俄罗斯的枪，不代表你就是俄罗斯人。"
        scene webringwar_day5_73
        with Dissolve(1)
        r1 "关键不只在枪。是时机让它变成千载难逢的机会。"
        r1 "前几天我见了市长，得知他打算约见几个俄罗斯商人。"
        r1 "我不知道他们和城里的俄罗斯家族有没有关系。但这不重要。"
        r1 "和俄罗斯人会面，结果就是用俄罗斯枪发动了一次刺杀。"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "你要嫁祸给他们？这样就够了吗……？"
        scene webringwar_day5_74
        with Dissolve(1)
        sophia "算是吧。"
        sophia "但就算他们不是主谋，从当时的情形来看，他们至少是「牵涉其中」。这足以让警方纠缠他们一阵子。"
        sophia "而且他们出了名的不专业。"
        sophia "枪上的指纹会有帮助。"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "等等……你就打算把枪丢在那儿让人发现？"
        scene webringwar_day5_73
        with Dissolve(1)
        r1 "对。"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "就是你从他们那儿买的那把枪？"
        scene webringwar_day5_73
        with Dissolve(1)
        r1 "对。"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "这样不会反噬吗？俄罗斯人会知道是你干的。"
        scene webringwar_day5_73
        with Dissolve(1)
        r1 "无所谓。"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "他们不能直接告诉警方吗？"
        ava "「不是我们干的！但枪是我们卖给这家伙的！去抓他，放过我们！」"
        scene webringwar_day5_73
        with Dissolve(1)
        r1 "跟警方做交易，是把他们全部送上绝路的最佳方式。"
        r1 "这一行里，能做和不能做的事之间只隔一条极细的线。"
        r1 "跟警方搭话，肯定就越线了。"
        sophia "最大的问题是报复。"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "我还是不明白……你为什么要挑衅他们？"
        scene webringwar_day5_73
        with Dissolve(1)
        r1 "这座城市靠的是一种非常微妙的平衡。"
        r1 "任何一方变得太强，都可能引发战争。"
        r1 "所以偶尔修剪一下枝头是必要的。"
        scene webringwar_day5_68
        with Dissolve(1)
        ava "那你们太强的时候，又是谁来修剪你们？"
        scene webringwar_day5_75
        with Dissolve(1)
        sophia "{i}No one zane, schurely!{/i}{p=0.0}(脑子正常的人，当然没有！)"
        r1 "哈！"
        scene webringwar_day5_76
        with Dissolve(1)
        ava "哈？"
        scene webringwar_day5_77
        with Dissolve(1)
        sophia "两年前，[r1]还在「族群」那边时，德国人和族群打了一场仗，[ingrid]至今还留着那时的伤。"
        play sound "audio/Flash.ogg" volume 0.5
        scene webringwar_day5_78
        with flashbulb
        ingrid "我到现在还是不知道 {i}vhy{/i} 你们 {i}tvo{/i} 要帮我。{p=0.0}(我到现在都不知道你们两个为什么要帮我。)"
        scene webringwar_day5_79
        with Dissolve(1)
        sophia "我也常常问自己同样的问题。"
        scene webringwar_day5_80
        with Dissolve(1)
        r1 "德国人已经败了。"
        r1 "我不能把你丢在那儿等死。"
        r1 "尤其是在我知道你本来有机会干掉我，却没有动手之后。"
        scene webringwar_day5_81
        with Dissolve(1)
        ingrid "他{i}vas tszoo{/i}太可爱了，让人下不了手。你说是不是？"
        scene webringwar_day5_85
        with Dissolve(1)
        pause
        scene webringwar_day5_86
        with Dissolve(1)
        pause
        play sound "audio/bone.mp3"
        scene webringwar_day5_82
        with hpunch
        pause
        scene webringwar_day5_83
        with hpunch
        ingrid "啊！"
        scene webringwar_day5_84
        with hpunch
        ingrid "Leck mich am Arsch, du englische Fotze! {p=0.0}(去你的，你这个英国婊子！)"
        scene webringwar_day5_87
        with Dissolve(1)
        sophia "这个婊子刚才是在骂我吗？"
        scene webringwar_day5_88
        sophia "我不懂德语，你这个混账！"
        sophia "我要是不把你的髋关节摆正，你的两条腿就都废了！给我忍着！"
        scene webringwar_day5_89
        with Dissolve(1)
        pause
        scene webringwar_day5_90
        with Dissolve(1)
        ingrid "哼。"
        scene webringwar_day5_86
        with Dissolve(1)
        sophia "想都别想。我可不是为了你才这么做的。"
        sophia "你现在死掉我都无所谓。"
        scene webringwar_day5_90
        with Dissolve(1)
        ingrid "{i}Zophia{/i}..."
        scene webringwar_day5_86
        with Dissolve(1)
        sophia "是 SO-PHIA！SO！是 S 开头的！"
        sophia "不是 Z！也不是「茨」！是 S！"
        scene webringwar_day5_90
        with Dissolve(1)
        ingrid "你弄完之后，能帮我剪一下头发吗？"
        scene webringwar_day5_92
        with Dissolve(1)
        sophia "什、什么……？为什么……？"
        scene webringwar_day5_91
        with Dissolve(1)
        ingrid "我已经受不了在镜子里看自己了。"
        ingrid "我认不出镜子里那个人。"
        ingrid "你能帮我吗？以一个女人的身份？"
        scene webringwar_day5_92
        with Dissolve(1)
        pause
        scene webringwar_day5_80
        with Dissolve(1)
        r1 "嗯。"
        scene webringwar_day5_90
        with Dissolve(1)
        ingrid "要是我自己一个人能搞定，{i}vouldn't{/i}就不会来问你了……"
        scene webringwar_day5_92
        with Dissolve(1)
        sophia "别说了！"
        sophia "我、我会帮你的，行了吧？别说了！"
        scene webringwar_day5_90
        with Dissolve(1)
        ingrid "Danke……{p=0.0}(谢谢……)"
        scene webringwar_day5_80
        with Dissolve(1)
        r1 "关于你的将来……"
        r1 "我会保护你，这是我欠你的。"
        r1 "没人能碰你。"
        r1 "但德国人已经没了，而你没有家。"
        r1 "在伤口愈合之前，你就住在这里。"
        r1 "之后你想走就走。"
        r1 "这期间我们会照顾你。"
        scene webringwar_day5_86
        with Dissolve(1)
        sophia "对！那谁照顾我们？！"
        scene webringwar_day5_93
        with Dissolve(1)
        ingrid "没有哪个 {i}zane{/i}，schurely……{p=0.0}(脑子正常的人，当然没有……)"
        scene webringwar_day5_94
        with hpunch
        ava "什么？！太可怕了！"
        ava "我还以为你要讲个好玩的故事！"
        scene webringwar_day5_95
        with Dissolve(1)
        ava "你真的……呃……"
        scene webringwar_day5_96
        with Dissolve(1)
        ava "……给她剪了头发？"
        scene webringwar_day5_97
        with Dissolve(1)
        sophia "你看，宝贝。"
        scene webringwar_day5_96
        with Dissolve(1)
        pause
        scene webringwar_day5_99
        with Dissolve(1)
        pause
        scene webringwar_day5_98
        with Dissolve(2)
        pause
        scene webringwar_day5_100
        with Dissolve(1)
        ava "你也剪了头发！"
        scene webringwar_day5_101
        with Dissolve(1)
        sophia "这个故事听起来可能有点怪，亲爱的。但那一刻，我第一次把她当成一个人来看。"
        sophia "一个女人。"
        sophia "在那之前，我眼里只有一个敌人。"
        scene webringwar_day5_102
        with Dissolve(1)
        sophia "她已经想杀我两次了。"
        sophia "我都准备拿刀捅她了。"
        sophia "可后来……「能帮我剪一下头发吗……」"
        sophia "我只想把她紧紧抱在怀里……"
        sophia "她还是个婊子……但话说回来……终归是个人。"
        scene webringwar_day5_75
        with Dissolve(1)
        r1 "你知道吗……我始终不理解剪头发这件事。"
        scene webringwar_day5_96
        with Dissolve(1)
        ava "你是男人……"
        scene webringwar_day5_95
        with Dissolve(1)
        ava "你不会懂的……"
        scene webringwar_day5_75
        with Dissolve(1)
        sophia "还记得我们初次见面时我已经是短发了吗？"
        r1 "记得。"
        sophia "那是我离开军队以后。"
        sophia "我失去的已经够多了，也再不敢照镜子。"
        sophia "我拿起剪刀，一点也没手下留情。"
        scene webringwar_day5_96
        with Dissolve(1)
        ava "女人的头发是她自身的延续……"
        scene webringwar_day5_75
        with Dissolve(1)
        sophia "对有些人来说，那只是换个发型。"
        sophia "对我而言，我无法忍受看到过去的自己。"
        sophia "我想[ingrid]也是一样。"
        r1 "啊……"
        scene webringwar_day5_103
        with Dissolve(1)
        r1 "那你为什么留短发？"
        scene webringwar_day5_104
        with Dissolve(1)
        ava "这是我的风格，行了吧？！"
        ava "别管了！"
        scene webringwar_day5_103
        with Dissolve(1)
        menu:
            "我觉得很好看。":
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[ava]的{color=#00ff00}好感{/color}提升了{color=#00ff00}5{/color}点！" )
                $love_ava+=5
                scene webringwar_day5_104
                with Dissolve(1)
                pause
                scene webringwar_day5_105_1
                with Dissolve(1)
                ava "谢、谢谢……"
            "你留长发一定很好看。":
                scene webringwar_day5_104
                with Dissolve(1)
                pause
                scene webringwar_day5_105_2
                with Dissolve(1)
                ava "谢谢……"
            
        scene webringwar_day5_106
        with Dissolve(1)
        sophia "看看气氛啊，[r1]。"
        r1 "什么？我确实是这么想的。"
        hide screen notifyEx
        scene webringwar_day5_107
        with Dissolve(1)
        ava "但等等……她不是因为觉得你可爱才要杀你的吧？"
        scene webringwar_day5_75
        with Dissolve(1)
        r1 "当然不是。她只是想羞辱[sophia]。"
        sophia "*咯咯笑*她有时候真是婊子！"
        sophia "就算伤好了她也一直在找茬！"
        r1 "不过看你们俩吵架还挺有意思的。"
        sophia "你运气好，我压根没拿刀捅她！"
        scene webringwar_day5_107
        with Dissolve(1)
        ava "那是什么原因？"
        scene webringwar_day5_103
        with Dissolve(1)
        r1 "那是另一场对话了。"
        r1 "改天再聊。"
        scene webringwar_day5_107
        with Dissolve(1)
        ava "好吧……"
        ava "她……好了吗？"
        scene webringwar_day5_75
        with Dissolve(1)
        pause
        play sound "audio/Flash.ogg" volume 0.5
        scene webringwar_day5_108
        with flashbulb
        r1 "金发小子，等你准备好了再说。"
        scene webringwar_day5_109
        with Dissolve(1)
        sophia "你们俩悠着点。别忘了这里还有个人在恢复期。"
        scene webringwar_day5_110
        with Dissolve(1)
        r1 "她自己决定。她随时可以回去做康复治疗。"
        scene webringwar_day5_111
        with Dissolve(1)
        ingrid "嗯……"
        scene webringwar_day5_112
        with Dissolve(2)
        pause
        scene webringwar_day5_113
        with Dissolve(2)
        pause
        play sound "audio/hit1l.ogg"
        scene webringwar_day5_114
        pause
        scene webringwar_day5_115
        with Dissolve(1)
        pause
        scene webringwar_day5_116
        with Dissolve(1)
        pause
        play sound "audio/fastmove1.ogg"
        scene webringwar_day5_117
        pause
        play sound "audio/throw1.ogg"
        scene webringwar_day5_118
        with hpunch
        pause
        scene webringwar_day5_119
        with hpunch
        sophia "放开她！"
        sophia "马上！"
        scene webringwar_day5_120
        with Dissolve(1)
        pause
        scene webringwar_day5_121
        with Dissolve(1)
        ingrid "妈妈说的。"
        scene webringwar_day5_122
        with Dissolve(1)
        r1 "她真没劲。"
        scene webringwar_day5_121
        with Dissolve(1)
        ingrid "你还指望一个英国医生能怎样？"
        scene webringwar_day5_123
        with Dissolve(1)
        sophia "我们居然能找到一个真在努力讲笑话的德国人，我真是太开心了！"
        sophia "你们俩现在悠着点！"
        scene webringwar_day5_121
        with Dissolve(1)
        ingrid "你知道我随时都能从这儿拧断你的胳膊吧？{p=0.0}（你知道我随时都能从这儿拧断你的胳膊吧？）"
        scene webringwar_day5_122
        with Dissolve(1)
        r1 "除非你先把我摔进草地里。"
        scene webringwar_day5_119
        with hpunch
        sophia "放手！现在！"
        scene webringwar_day5_124
        with Dissolve(1)
        r1 "好吧！好吧！"
        scene webringwar_day5_125
        with Dissolve(1)
        r1 "再来一次……这次不许抱摔。"
        scene webringwar_day5_127
        with Dissolve(1)
        ingrid "抓着我的是你啊，{i}Grossmann{/i}。"
        scene webringwar_day5_126
        with Dissolve(1)
        r1 "格罗斯什么？"
        scene webringwar_day5_127
        with Dissolve(1)
        ingrid "你……不懂。{p=0.0}（你……不会懂的。）"
        scene webringwar_day5_129
        with Dissolve(1)
        r1 "好。只用拳。"
        r1 "来吧。"
        scene webringwar_day5_130
        with Dissolve(1)
        pause
        play sound "audio/fastmove1.ogg"
        scene webringwar_day5_131
        pause
        play sound "audio/hit1l.ogg"
        scene webringwar_day5_132
        pause
        play sound "audio/hit1l.ogg"
        scene webringwar_day5_133
        pause
        play sound "audio/fastmove1.ogg"
        scene webringwar_day5_134
        pause
        play sound "audio/hit1l.ogg"
        scene webringwar_day5_135
        pause
        play sound "audio/fastmove1.ogg"
        scene webringwar_day5_136
        pause
        scene webringwar_day5_137
        sophia "慢点！你们会伤到自己的！"
        play sound "audio/fastmove1.ogg"
        scene webringwar_day5_138
        pause
        play sound "audio/hit1l.ogg"
        scene webringwar_day5_139
        pause
        play sound "audio/fastmove1.ogg"
        scene webringwar_day5_140
        pause
        play sound "audio/throw2.ogg"
        scene webringwar_day5_141
        with hpunch
        pause
        play sound "audio/throw2.ogg"
        scene webringwar_day5_142
        with hpunch
        pause
        scene webringwar_day5_143
        with hpunch
        pause
        scene webringwar_day5_144
        with Dissolve(1)
        sophia "你们受伤了吗？！"
        scene webringwar_day5_145
        with Dissolve(1)
        r1 "没事……"
        r1 "我很好。"
        scene webringwar_day5_144
        with Dissolve(1)
        sophia "你确定？"
        scene webringwar_day5_145
        with Dissolve(1)
        r1 "嗯……嗯……"
        scene webringwar_day5_147
        with Dissolve(1)
        pause
        scene webringwar_day5_146
        with Dissolve(1)
        ingrid "太过分了吗？"
        scene webringwar_day5_147
        with Dissolve(1)
        r1 "没有啊，那挺好。"
        r1 "你那套拳法哪儿学的？"
        scene webringwar_day5_146
        with Dissolve(1)
        ingrid "{i}Mein vater{/i}想要一个儿子。{p=0.0}（我父亲想要一个儿子。）"
        scene webringwar_day5_147
        with Dissolve(1)
        r1 "我相信他是。不过我想你其实是想说他想要个「儿子」吧。"
        scene webringwar_day5_146
        with Dissolve(1)
        ingrid "Ja！{p=0.0}（对！）"
        scene webringwar_day5_147
        with Dissolve(1)
        r1 "这就说得通了。"
        scene webringwar_day5_148
        with Dissolve(1)
        r1 "嗯，他得到了。"
        scene webringwar_day5_149
        with Dissolve(1)
        ingrid "Gut fight？{p=0.0}（打得好？）"
        scene webringwar_day5_150
        with Dissolve(1)
        r1 "打得漂亮。"
        ingrid "对！Vell fought！"
        r1 "嗯。"
        ingrid "Uell。"
        r1 "差不多吧。"
        scene webringwar_day5_151
        with Dissolve(1)
        pause
        scene webringwar_day5_152
        with Dissolve(1)
        r1 "怎么了？"
        scene webringwar_day5_153
        with Dissolve(1)
        ingrid "我知道你留手了。"
        scene webringwar_day5_154
        with Dissolve(1)
        r1 "什么？我没有！"
        scene webringwar_day5_153
        with Dissolve(1)
        ingrid "你根本没想过还手。"
        scene webringwar_day5_154
        with Dissolve(1)
        pause
        r1 "我没有吗？"
        r1 "我没注意到。"
        scene webringwar_day5_153
        with Dissolve(1)
        ingrid "但我注意到了。"
        scene webringwar_day5_154
        with Dissolve(1)
        r1 "哦，那大概是你没给我留够空间。"
        scene webringwar_day5_153
        with Dissolve(1)
        ingrid "我数了，你至少有五次机会能打中我。"
        scene webringwar_day5_163
        with Dissolve(1)
        r1 "那或许该由你来教我。"
        scene webringwar_day5_153
        with Dissolve(1)
        ingrid "那就跟我教你怎么说英语一样。"
        scene webringwar_day5_163
        with Dissolve(1)
        r1 "怎么「说」英语。"
        scene webringwar_day5_153
        with Dissolve(1)
        ingrid "我说的就是这个意思。"
        scene webringwar_day5_164
        with Dissolve(1)
        sophia "好吧。你去休息。"
        sophia "该我了。"
        scene webringwar_day5_165
        with Dissolve(1)
        r1 "那可有意思了。"
        r1 "一个德国人和一个英国人走进酒吧……"
        scene webringwar_day5_166
        with Dissolve(2)
        sophia "我还是比你块头大，你知道的。"
        scene webringwar_day5_167
        with Dissolve(1)
        ingrid "所以我永远不会让你忘记这一点。"
        play sound "audio/Flash.ogg" volume 0.5
        scene webringwar_day5_168
        with flashbulb
        ava "谁赢了？"
        scene webringwar_day5_169
        with Dissolve(1)
        sophia "就说她让我一直忘不了好了。"
        scene webringwar_day5_168
        with Dissolve(1)
        pause
        scene webringwar_day5_107
        with Dissolve(1)
        ava "那你呢……她真的打到你了吗？"
        scene webringwar_day5_155
        with Dissolve(1)
        r1 "当然。"
        scene webringwar_day5_107
        with Dissolve(1)
        ava "疼吗？"
        scene webringwar_day5_156
        with Dissolve(1)
        r1 "哦，还挺疼。她那一拳挺狠。"
        scene webringwar_day5_107
        with Dissolve(1)
        ava "那你为什么让她打你？！"
        scene webringwar_day5_157
        with Dissolve(1)
        r1 "我没有。她是堂堂正正赢我的。"
        scene webringwar_day5_158
        with Dissolve(1)
        r1 "跟她训练挺有意思的。"
        sophia "我记得你们俩打了一整晚。"
        r1 "她有那股劲。"
        scene webringwar_day5_159
        with Dissolve(1)
        ava "我可不想那样训练……"
        scene webringwar_day5_160
        with Dissolve(2)
        pause
        scene webringwar_day5_161
        with Dissolve(2)
        pause
        scene webringwar_day5_162
        with Dissolve(1)
        sophia "没那么疼的。"
        sophia "而且过一阵你就习惯了。"
        scene webringwar_day5_159
        with Dissolve(1)
        ava "我不确定……"
        scene webringwar_day5_157
        with Dissolve(1)
        r1 "一次打一仗就好。"
        r1 "传闻听多了，就显得比实际更残酷。"
        r1 "跟喜欢的人一起练有意思多了。你知道，几个人一起。"
        scene webringwar_day5_75
        with Dissolve(1)
        r1 "再说了，你们谁要是伤到我，我还有[sophia]或者[isa]可以——"
        scene webringwar_day5_71
        with Dissolve(2)
        r1 "啊……糟了。"
        sophia "怎么了？"
        r1 "我忘了。"
        r1 "我今天本该去接[isa]。"
        r1 "她把车停在附近，昨天我们去学院的时候，最后是把她送回了家。"
        sophia "学院？"
        scene webringwar_day5_159
        with Dissolve(1)
        ava "送到她家……？"
        scene webringwar_day5_70
        with Dissolve(1)
        r1 "天啊……当我没说。"
        r1 "我得去接她。"
        sophia "我不确定你回来的时候我还在不在。"
        scene webringwar_day5_170
        with Dissolve(1)
        r1 "没关系。有需要就给我发消息。"
        r1 "或者有什么变化。"
        scene black
        with Dissolve(2)
        pause(1)
        
        
        
    label day5_isabella_littlesecret:  
        play sound "audio/knockingdoor.ogg"
        scene day5_isabellalittlesecret_1
        with Dissolve(2)
        r1 "[isa]！开门！"
        r1 "对不起，好吗？我忘了。"
        r1 "我知道你在里面。"
        isa "呃……嘿！[r1]先生……"
        isa "没关系，真的。不用担心。"
        isa "我现在……身体不太方便。"
        r1 "你还好吗？需要帮忙吗？"
        isa "不用！"
        isa "我是说……我很好！"
        r1 "[isa]，你确定没事吗？"
        isa "确定！"
        r1 "好吧……你要我在车旁边等，还是……"
        isa "先生，我……我想我今天去不了公司。"
        r1 "[isa]，到底怎么了？"
        play sound "audio/beep.mp3"
        scene day5_isabellalittlesecret_2
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_3
        with Dissolve(1)
        nvl clear
        nvl_narrator "[isa]的聊天"
        isa_nvl "你一个人吗？"
        r1_nvl "当然。怎么了？"
        play sound "audio/fastmove1.ogg"
        scene day5_isabellalittlesecret_3_1
        pause
        play sound "audio/hitwood1.ogg"
        scene day5_isabellalittlesecret_4
        with hpunch
        pause
        scene day5_isabellalittlesecret_5
        with Dissolve(1)
        isa "请你千万别出声。"
        isa "点点头就行，好吗？"
        scene day5_isabellalittlesecret_6
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_7
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_6
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_8
        with Dissolve(1)
        isa "门口有警车吗？"
        isa "或者说，有任何车吗？"
        scene day5_isabellalittlesecret_9
        with Dissolve(1)
        pause
        r1 "没有？"
        scene day5_isabellalittlesecret_10
        isa "停！"
        isa "你在——"
        isa "我说了别出声！"
        scene day5_isabellalittlesecret_11
        isa "呃！"
        scene day5_isabellalittlesecret_12
        with Dissolve(1)
        isa "对不起……只是……"
        isa "算了……"
        scene day5_isabellalittlesecret_13
        with Dissolve(1)
        pause
        isa "对不起……"
        scene day5_isabellalittlesecret_14
        with Dissolve(2)
        r1 "没关系。"
        r1 "你没事就好。"
        scene day5_isabellalittlesecret_15
        with Dissolve(1)
        isa "你不该对一个女人撒谎。"
        isa "我们只是装作不知道，你们男人干的那些事。"
        scene day5_isabellalittlesecret_16
        with Dissolve(1)
        isa "可恶，[r1]……"
        isa "你不该来的。"
        scene day5_isabellalittlesecret_17
        with Dissolve(1)
        isa "我不想让任何人看到我这副样子。"
        scene day5_isabellalittlesecret_18
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_19
        with Dissolve(1)
        r1 "那你可真没藏好。"
        r1 "至少可以告诉我你病了。我就不会来了。"
        isa "我不喜欢撒谎。"
        scene day5_isabellalittlesecret_20
        with Dissolve(1)
        isa "说实话，我只希望今天你别想起我。"
        scene day5_isabellalittlesecret_21
        with Dissolve(1)
        pause
        #play music "audio/soundtrack/TheHowl.mp3" fadein 10 volume 1
        play music "audio/Castle in the sky.ogg" fadein 4 volume 0.2
        scene day5_isabellalittlesecret_22
        with Dissolve(1)
        r1 "不会的，[isa]。"
        r1 "现在告诉我到底怎么了。"
        scene day5_isabellalittlesecret_23
        with Dissolve(2)
        isa "记得我昨天跟我妈聊的那些吗？"
        r1 "记得。怎么了？"
        isa "是关于我前夫的。"
        isa "他是联邦探员。"
        scene day5_isabellalittlesecret_24
        with Dissolve(1)
        r1 "我不知道。"
        isa "我不喜欢谈自己的事，你会明白为什么的。"
        scene day5_isabellalittlesecret_25
        with Dissolve(1)
        isa "呃……我该怎么说……"
        r1 "慢慢来，没关系。"
        scene day5_isabellalittlesecret_27
        with Dissolve(1)
        pause 0.2
        scene day5_isabellalittlesecret_26
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_28
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_30
        with Dissolve(2)
        isa "*紧张地笑*"
        scene day5_isabellalittlesecret_31
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_32
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_33
        with Dissolve(2)
        isa "他伤害过我。"
        scene day5_isabellalittlesecret_34
        with Dissolve(2)
        isa "那是几年前的事……但感觉就像昨天。"
        scene day5_isabellalittlesecret_35
        with Dissolve(1)
        isa "我知道这听起来很蠢……"
        isa "一切始于我参加完医学大会后去参加派对的一次旅行，他先对我大吼大叫。"
        isa "几周后，只是一巴掌……"
        isa "并不疼……但我害怕了……"
        isa "也许是我的错……也许是我吵得太多……也许是我声音太大了……我不知道……"
        isa "又过了几周……他打了我。"
        isa "等我意识到发生了什么……我没法去上班，因为我眼眶淤青了。"
        scene day5_isabellalittlesecret_36
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_37
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_39
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_38
        with Dissolve(2)
        isa "你永远不会觉得这种事会发生在自己身上……"
        scene day5_isabellalittlesecret_39
        with Dissolve(1)
        isa "直到它真的发生……"
        scene day5_isabellalittlesecret_40
        with Dissolve(1)
        isa "我连离婚都没法申请……我不想在法庭上面对他……"
        isa "我觉得自己很没用……"
        scene day5_isabellalittlesecret_41
        with Dissolve(1)
        r1 "你在开玩笑吗？"
        r1 "别把责任往自己身上揽。"
        scene day5_isabellalittlesecret_42
        with Dissolve(1)
        isa "现在你知道我有多懦弱了……"
        scene day5_isabellalittlesecret_41
        with Dissolve(1)
        r1 "你是认真的吗？你做的事需要很大的勇气。"
        r1 "而你把它告诉我的勇气更大。"
        scene day5_isabellalittlesecret_42
        with Dissolve(1)
        isa "走投无路不等于勇敢。"
        isa "我本来该换个说法。"
        isa "如果我说那只是激素作祟，我想你会信。"
        scene day5_isabellalittlesecret_41
        with Dissolve(1)
        r1 "那你一定很看不起我。"
        scene day5_isabellalittlesecret_43
        with Dissolve(1)
        isa "我现在本来就挺看不起自己的……"
        isa "请别让我更难受。我不是想侮辱你……"
        scene day5_isabellalittlesecret_41
        with Dissolve(1)
        r1 "我的意思是……"
        r1 "我是想说，我绝不会把你一个人留在这儿。而且我也不会信那套「激素」的鬼话。"
        scene day5_isabellalittlesecret_44
        with Dissolve(1)
        isa "你不会吗？"
        scene day5_isabellalittlesecret_41
        with Dissolve(1)
        r1 "当然不会。"
        r1 "我说过，我从不轻看「忠诚」这个词。"
        r1 "当我说你随时需要我、我都在时，我是认真的。"
        r1 "你刚告诉我，你不喜欢撒谎。"
        r1 "所以你要是真想告诉我什么，就说实话。我想听真话。"
        scene day5_isabellalittlesecret_45
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_46
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_47
        with Dissolve(2)
        isa "呃……靠……"
        scene day5_isabellalittlesecret_41
        with Dissolve(1)
        r1 "不想说也没关系。"
        scene day5_isabellalittlesecret_47
        with Dissolve(1)
        isa "不是这个。给我一点时间。"
        scene day5_isabellalittlesecret_48
        with Dissolve(2)
        isa "嗯……我逃走了。就像个懦夫一样。"
        isa "一天晚上他在睡觉……我连行李都没收拾。"
        isa "等我给我妈打电话时，我已经开着车走到国土的一半了……"
        isa "我告诉她我要离开一阵子……"
        scene day5_isabellalittlesecret_49
        with Dissolve(1)
        r1 "一阵子？"
        scene day5_isabellalittlesecret_48
        with Dissolve(1)
        isa "我已经两年没见我妈了。"
        isa "我不能回那座城市……"
        isa "第一年我靠全部积蓄在这里活下去。我太害怕了，不敢去任何他可能找到我的医院上班。"
        isa "可现在我已经一无所有……"
        isa "连「我的车」都是用别人的名字租的……"
        scene day5_isabellalittlesecret_50
        with Dissolve(1)
        isa "我甚至不敢告诉她我在哪儿，因为我怕他会监听我的电话！"
        scene day5_isabellalittlesecret_49
        with Dissolve(1)
        r1 "[isa]……"
        scene day5_isabellalittlesecret_51
        with Dissolve(1)
        isa "[r1]……他想怎样就怎样吧。制度站在他那边。"
        isa "我换了号码……搬到了别的城市。我能做的都做了……"
        isa "可那种「他在监视我」的蠢恐惧一直缠着我……"
        r1 "好了，够了。"
        scene day5_isabellalittlesecret_52
        isa "求你别走！"
        isa "别把我一个人留在这儿。"
        scene day5_isabellalittlesecret_53
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_54
        with Dissolve(2)
        r1 "我没打算走。"
        isa "看起来像。"
        isa "对不起……"
        r1 "别再说这个了。"
        r1 "我哪儿都不去。"
        scene day5_isabellalittlesecret_53
        with Dissolve(1)
        r1 "我想说的是……"
        isa "什么？"
        r1 "虽然我不想让你害怕……"
        scene day5_isabellalittlesecret_54
        with Dissolve(2)
        r1 "虽然我不觉得你是懦夫……但我能理解你的理由。"
        r1 "不管怎样，我很高兴我在这儿。你不该一个人扛这些。"
        isa "[r1]……我又得搬家了……"
        scene day5_isabellalittlesecret_53
        r1 "什么？为什么？"
        isa "我妈说他一直在找我，她也不明白我为什么不告诉任何人我在哪儿。"
        isa "所以我打了他所在部门的电话，想找他上司谈谈。我想解释我没有失踪。"
        r1 "你不想立案调查。"
        isa "如果我说我没事，就不会有人来找我……"
        r1 "你为什么不告诉他上司他做过什么？"
        scene day5_isabellalittlesecret_55
        isa "因为我感到羞耻，[r1!u]！"
        isa "就是这样！"
        isa "而且我是个懦夫！"
        scene day5_isabellalittlesecret_56
        r1 "好了！可以别说了吗？我不想再听你说这种话。"
        r1 "那些不是事实，你知道。"
        scene day5_isabellalittlesecret_57
        with Dissolve(2)
        isa "你好好看看我，[r1]……"
        isa "我现在看起来勇敢吗？"
        scene day5_isabellalittlesecret_58
        with Dissolve(1)
        r1 "你看起来是个很出色的女人，只是遭遇了糟糕的事。"
        r1 "被打倒之后还想爬起来，这里面没有任何懦弱。"
        scene day5_isabellalittlesecret_57
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_59
        with Dissolve(1)
        isa "*紧张地笑*{p=0.0}出色？"
        scene day5_isabellalittlesecret_60
        with Dissolve(1)
        isa "我连自己的婚姻都维持不住……"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        r1 "你信任我吗，[isa]？"
        scene day5_isabellalittlesecret_60
        with Dissolve(1)
        isa "信任我做什么……？"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        r1 "是或不是的问题。"
        scene day5_isabellalittlesecret_60
        with Dissolve(1)
        isa "[r1]……"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "你说得对。"
        r1 "只是现在问这个不太合适。"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        r1 "不过我可以告诉你我是什么意思。"
        scene day5_isabellalittlesecret_61
        pause
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "不。我不说。"
        r1 "我用做的给你看。"
        scene day5_isabellalittlesecret_60
        with Dissolve(1)
        isa "我不明白……"
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "我让[sophia]开车送你回家。"
        r1 "我不会让你一个人留在这儿。"
        scene day5_isabellalittlesecret_63
        with Dissolve(1)
        isa "求你，别叫任何人！"
        isa "我不想让任何人看到我这副样子。"
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "如果你愿意，我可以留在这儿陪你直到你好些。"
        r1 "但不管怎样，我还是希望你跟[sophia]一起来我家。"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        r1 "就待在我们家吧。在那儿你会安全的。"
        scene day5_isabellalittlesecret_65
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_64
        with Dissolve(2)
        pause
        isa "我不配……你不用照顾我。"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        r1 "你值得拥有一切，而且远不止。"
        scene day5_isabellalittlesecret_66
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_67
        with Dissolve(2)
        pause
        isa "我该怎么办，[r1]……"
        isa "我不可能永远逃下去……"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        r1 "你不用。你可以想住多久就住多久。"
        r1 "我不介意。"
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "我知道等你感到安全了，就会想出办法。"
        r1 "他永远找不到那里。就算他找到了，我也会处理。"
        scene day5_isabellalittlesecret_63
        with Dissolve(1)
        isa "你疯了吗？！"
        isa "我绝不会把这种事推给你！那太危险了！"
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "你觉得一个人待着就不危险了吗？"
        scene day5_isabellalittlesecret_63
        with Dissolve(1)
        isa "[r1]，你没明白！"
        isa "是他！他很危险！"
        isa "万一他对你做什么呢？！"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        r1 "我看起来像是害怕了吗？"
        scene day5_isabellalittlesecret_68
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_69
        play sound "audio/clenching.ogg"
        with Dissolve(2)
        isa "你为什么就是不明白……"
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "我完全明白，[isa]。"
        r1 "我知道有多危险。但跟我们在一起你会安全得多。"
        r1 "再说了，有姑娘们陪着你会好得多。"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        r1 "你不想一个人待着的话，就不必。"
        r1 "我们靠得住。"
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "那个……你真想听的话……"
        scene day5_isabellalittlesecret_70
        with Dissolve(1)
        r1 "我喜欢布置的这个地方。很现代。"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "我在布置房间上一直很差劲。"
        r1 "我家没你家好……"
        r1 "……但那是个家。"
        scene day5_isabellalittlesecret_67
        with Dissolve(2)
        isa "我现在没心情，[r1]……"
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "你知道什么时候微笑最好吗，[isa]？"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        r1 "当你觉得笑不出来的时候。"
        r1 "因为那种时候你最需要笑容。"
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "毕竟……勇气的时刻，在绝望的映衬下才最耀眼。"
        scene day5_isabellalittlesecret_66
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_72
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_73
        with Dissolve(2)
        pause
        isa "你知道……我一直不喜欢那种脆弱的感觉……"
        isa "但这次我很高兴……你在这儿。"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "喂。别以为这不用还。"
        r1 "我也想轮到我哭一次。"
        scene day5_isabellalittlesecret_73
        with Dissolve(1)
        isa "你看起来不像是会在女人怀里哭的人。"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "搞什么？"
        r1 "我很敏感的，好吗？"
        scene day5_isabellalittlesecret_74
        with Dissolve(1)
        isa "*咯咯笑*"
        isa "住嘴！"
        scene day5_isabellalittlesecret_75
        with Dissolve(1)
        isa "我知道你想干什么……"
        scene day5_isabellalittlesecret_76
        with Dissolve(1)
        pause
        isa "..."
        isa "你知道……我第一次见到你的时候，想象中的你完全不一样。"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "真的吗？"
        scene day5_isabellalittlesecret_76
        with Dissolve(1)
        isa "对……你看起来像个粗人。"
        scene day5_isabellalittlesecret_77
        with Dissolve(1)
        isa "说实话……你有点吓到我了。"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "我？！粗人？！"
        r1 "我明明这么温柔。"
        scene day5_isabellalittlesecret_77
        with Dissolve(1)
        isa "而且我从来没这么高兴自己看走眼了。"
        scene day5_isabellalittlesecret_78
        with Dissolve(2)
        pause
        isa "嘿，头儿。"
        scene day5_isabellalittlesecret_71
        with Dissolve(2)
        r1 "嗯？"
        scene day5_isabellalittlesecret_78
        with Dissolve(2)
        isa "谢谢。"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "不客气。"
        scene day5_isabellalittlesecret_78
        with Dissolve(2)
        isa "我之前说过……但这件事能只在我们之间吗？"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "当然。"
        r1 "不过我还是会让[sophia]来接你。"
        r1 "但我不用说明原因。"
        r1 "不过我希望你自己告诉她。"
        r1 "她是个很好的女人。而且她支持你的方式，会比我强得多。"
        scene day5_isabellalittlesecret_62
        with Dissolve(1)
        r1 "算了……不，别告诉她。"
        scene day5_isabellalittlesecret_61
        with Dissolve(1)
        r1 "她可能会想把那个男人揪出来。"
        scene day5_isabellalittlesecret_74
        with Dissolve(1)
        isa "*咯咯笑*"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "那么……你接受吗？愿意和我们一起住吗？"
        r1 "我说的不只是因为你帮我处理伤口。"
        r1 "你想住多久都行。"
        r1 "把你的东西收拾起来，去透透气。"
        r1 "怎么样？"
        scene day5_isabellalittlesecret_78
        with Dissolve(1)
        isa "有一个条件……"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "嗯？"
        scene day5_isabellalittlesecret_78
        with Dissolve(1)
        isa "[ava]要教我做一两道菜。"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "这个你得去问她。"
        r1 "只是别……别问任何跟蛋有关的事。"
        scene day5_isabellalittlesecret_78
        with Dissolve(1)
        isa "为什么？"
        scene day5_isabellalittlesecret_71
        with Dissolve(1)
        r1 "就是别问。"
        r1 "尤其别在[sophia]面前问。"
        scene day5_isabellalittlesecret_79
        with Dissolve(1)
        r1 "听着，我还是得去学院。"
        r1 "那我给[sophia]打电话，可以吗？"
        r1 "她会来接你。"
        isa "让我先洗个澡。我现在难看死了。"
        isa "而且大概更臭。"
        scene day5_isabellalittlesecret_80
        with Dissolve(1)
        isa "不过我想你不会太失礼到不说实话。"
        scene day5_isabellalittlesecret_81
        with Dissolve(1)
        r1 "如果你真想知道……"
        scene day5_isabellalittlesecret_82
        with Dissolve(1)
        r1 "我觉得你闻起来很棒。"
        scene day5_isabellalittlesecret_83
        with Dissolve(1)
        r1 "不过这个地方嘛……"
        r1 "就差多了……"
        scene day5_isabellalittlesecret_84
        with Dissolve(1)
        r1 "我是说……得了吧……"
        r1 "我给你的钱，不够你租个好点的地方吗？"
        isa "既然你都说到那儿了，我们正好谈谈我的加薪。"
        scene day5_isabellalittlesecret_85
        with Dissolve(1)
        r1 "很高兴你感觉好些了。"
        scene day5_isabellalittlesecret_86
        r1 "我们可以改天再——"
        isa "先生……"
        scene day5_isabellalittlesecret_87
        with Dissolve(1)
        isa "如果我刚才做的事告诉了别人，他们肯定会把我送去警察局……"
        isa "我以为你也会这么做……那才是明智的做法，对吧？"
        isa "你为什么没有？"
        scene day5_isabellalittlesecret_90
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_88
        with Dissolve(1)
        r2 "「哦！那很简单啊，我的小姜姜！」"
        r2 "「我们这辈子一次都没求过警察！」"
        r2 "「我们压根儿就没那么想过！」"
        r2 "去啊，告诉她。"
        scene day5_isabellalittlesecret_89
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_90
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_91
        with Dissolve(1)
        r1 "那就是你一个人对上他的说法。"
        scene day5_isabellalittlesecret_87
        with Dissolve(1)
        isa "嗯？"
        scene day5_isabellalittlesecret_91
        with Dissolve(1)
        r1 "没有任何东西能佐证你的说法……我是说，能让警方相信的东西。"
        r1 "我见过太多，明白警察往往会包庇自己人。"
        r1 "没有实物、没有无可辩驳的证据……我不觉得报警对你有什么好处。"
        r1 "更何况那都是几年前的事了……"
        r1 "而且那还会把你的行踪告诉你前夫。"
        r1 "他就得来这座城市。"
        scene day5_isabellalittlesecret_88
        with Dissolve(1)
        r2 "反应够快，我喜欢。"
        scene day5_isabellalittlesecret_87
        with Dissolve(1)
        isa "我也想到这一点了……"
        scene day5_isabellalittlesecret_91
        with Dissolve(1)
        r1 "我们先专心让你恢复过来，好吗？"
        r1 "以后再想我们能做什么。"
        scene day5_isabellalittlesecret_87
        with Dissolve(1)
        isa "好……"
        scene day5_isabellalittlesecret_91
        with Dissolve(1)
        r1 "我去跟[sophia]说，她到了我告诉你，行吗？"
        scene day5_isabellalittlesecret_87
        with Dissolve(1)
        isa "好……"
        scene day5_isabellalittlesecret_91
        with Dissolve(1)
        r1 "我们家里见——"
        play sound "audio/hitwood1.ogg"
        scene day5_isabellalittlesecret_92
        with hpunch
        isa "谢谢，[r1]……"
        isa "真的……"
        isa "我知道你本没必要这么做。"
        isa "这太过私密了，而你在因为我冒险。"
        isa "我永远不会忘记你现在做的一切。"
        scene day5_isabellalittlesecret_93
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_94
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_95
        with Dissolve(1)
        r1 "别放在心上。"
        r1 "换作是我，我也会这么做。"
        scene day5_isabellalittlesecret_96
        with Dissolve(1)
        r1 "虽然听着老套，但我确实会照顾自己人。"
        r1 "我也许是你的上司，但你也可以把我当朋友。"
        scene day5_isabellalittlesecret_97
        with Dissolve(1)
        r1 "我是说……下班之后。"
        r1 "该开除的时候我照样会开除你。"
        play sound "audio/hit1.ogg"
        scene day5_isabellalittlesecret_98
        with hpunch
        isa "我说了别拿这个开玩笑！"
        #play sound "audio/coughmc.ogg"
        scene day5_isabellalittlesecret_99
        isa "啊糟糕！我忘了！"
        scene day5_isabellalittlesecret_100
        isa "我弄疼你了吗？！"
        scene day5_isabellalittlesecret_101
        r1 "没有！*咳嗽* 没事。"
        r1 "我很好。等我一下。"
        scene day5_isabellalittlesecret_102
        with Dissolve(1)
        isa "过来，让我看看。"
        r1 "没事，[isa]。刚才有点疼，但现在好了。"
        r1 "而且我真的得走了。"
        isa "「那不可能，先生！」"
        isa "你这话常说。"
        r1 "是吗？"
        isa "是啊。快过来。"
        scene day5_isabellalittlesecret_103
        with Dissolve(1)
        isa "我得解开你的衬衫，好吗？"
        scene day5_isabellalittlesecret_104
        with Dissolve(1)
        r1 "[isa]，相信我。我没事……真的。"
        isa "先生……这跟信不信任没关系。"
        isa "听着，你的伤口还没愈合。缝合线一崩，你就会大量出血！"
        isa "你想在工作的时候来这么一出吗？"
        isa "不想？很好，那就让我检查。"
        scene day5_isabellalittlesecret_105
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_106
        with Dissolve(1)
        r1 "好吧，请便。"
        scene day5_isabellalittlesecret_107
        with Dissolve(1)
        isa "我们得非常小心。缝合线没崩，但比看上去脆弱。"
        r1 "又不是我求着被打的。"
        scene day5_isabellalittlesecret_108
        with Dissolve(1)
        isa "你明明就是「求」被打。"
        r1 "我不记得了。"
        scene day5_isabellalittlesecret_109
        with Dissolve(1)
        isa "过一会儿你就想起来了。"
        scene day5_isabellalittlesecret_111
        with Dissolve(1)
        isa "先生……你真的得小心。"
        isa "我得重新给你缝合。这事可以等到晚上……"
        isa "……但有件事我必须告诉你："
        isa "如果你太乱来，就会发生伤口裂开，明白吗？"
        r1 "伤口什么？"
        scene day5_isabellalittlesecret_110
        with Dissolve(1)
        isa "抱歉……"
        scene day5_isabellalittlesecret_111
        with Dissolve(1)
        isa "伤口会裂开，而且得有人帮忙才能止血，明白吗？"
        isa "这是很严重的事。"
        isa "它还没好，所以请按还没好的来处理。"
        r1 "好吧，我会小心的。"
        r1 "谢谢。"
        scene day5_isabellalittlesecret_112
        with Dissolve(1)
        isa "做好本分是我的荣幸。"
        scene day5_isabellalittlesecret_113
        with Dissolve(1)
        r1 "那么……我现在走了……行吗？"
        scene day5_isabellalittlesecret_114
        isa "对！没错！"
        scene day5_isabellalittlesecret_115
        with Dissolve(2)
        pause
        isa "[r1]……"
        scene day5_isabellalittlesecret_116
        with Dissolve(1)
        r1 "嗯？"
        play sound "audio/Lockpick_Success.ogg" volume 0.1
        $ love_isa +=10
        show screen notifyEx( msg="[isa]的{color=#00ff00}好感{/color}提升了{color=#00ff00}10{/color}点！" )
        scene day5_isabellalittlesecret_117
        with Dissolve(1)
        isa "你是个好人。"
        isa "这个世界需要更多像你这样的人。"
        scene day5_isabellalittlesecret_116
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_118
        with Dissolve(1)
        r1 "*啧*"
        scene day5_isabellalittlesecret_119
        with Dissolve(1)
        isa "怎么了？"
        scene day5_isabellalittlesecret_118
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_116
        with Dissolve(1)
        r1 "没什么，抱歉。"
        scene day5_isabellalittlesecret_119
        with Dissolve(1)
        isa "确定吗？"
        isa "你看起来不太喜欢我刚才说的话。"
        scene day5_isabellalittlesecret_116
        with Dissolve(1)
        r1 "这个世界需要很多东西，[isa]。我不是其中之一。"
        scene day5_isabellalittlesecret_119
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_116
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_118
        with Dissolve(1)
        play sound "audio/Lockpick_Success.ogg" volume 0.1
        $ biopage["isa"] = 3
        show screen notifyEx( msg="[isa]的{color=#00ff00}人物档案{/color}已{color=#00ff00}更新{/color}！" )
        r1 "刚才的话当我没说。"
        r1 "我们晚上再见，好吗？"
        scene day5_isabellalittlesecret_119
        with Dissolve(1)
        isa "好。"
        scene day5_isabellalittlesecret_116
        with Dissolve(1)
        r1 "把你的号码给[sophia]，可以吗？"
        scene day5_isabellalittlesecret_119
        with Dissolve(1)
        isa "当然可以。但为什么？"
        scene day5_isabellalittlesecret_116
        with Dissolve(1)
        r1 "我想，也许知道门外等的是她会让你好受些。"
        r1 "那样你们沟通也更方便。"
        r1 "她会直接给你发消息。可以吗？"
        scene day5_isabellalittlesecret_117
        with Dissolve(1)
        isa "谢谢您，先生。"
        stop music fadeout 3
        scene day5_isabellalittlesecret_116
        with Dissolve(1)
        r1 "我们晚上见。有事就打电话给我。"
        
        hide notifyEx with dissolve
        play sound "audio/open4.ogg"
        play music2 "audio/soundtrack/suspenseheartbeat.ogg"
        scene day5_isabellalittlesecret_121
        pause
        scene day5_isabellalittlesecret_122
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_123
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_124
        with Dissolve(2)
        pause
        play sound "audio/clenching.ogg"
        scene day5_isabellalittlesecret_125
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_126
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_127
        r2 "呼吸。"
        r2 "试着冷静下来。"
        play sound "audio/dramaticstinger.ogg" volume 0.8
        scene day5_isabellalittlesecret_128
        pause
        scene day5_isabellalittlesecret_129
        r2 "不管你现在有多痛……"
        scene day5_isabellalittlesecret_130
        r2 "我感觉到的完全一样。"
        r2 "必须停下来。"
        play sound "audio/fastmove1.ogg"
        scene day5_isabellalittlesecret_131
        pause
        play sound "audio/throw2.ogg"
        scene day5_isabellalittlesecret_132
        with hpunch
        pause
        play sound "audio/dramaticstinger.ogg" volume 0.8
        scene day5_isabellalittlesecret_133
        pause
        scene day5_isabellalittlesecret_134
        with Dissolve(2)
        r2 "发火对我们没好处。"
        r2 "你得把心率降下来，不然伤口会裂开。"
        r2 "呼吸。"
        scene day5_isabellalittlesecret_135
        with Dissolve(2)
        r2 "来，手拿开。"
        r2 "没事。专心。"
        stop music2 fadeout 5
        scene day5_isabellalittlesecret_133
        with Dissolve(2)
        pause
        scene day5_isabellalittlesecret_136
        with Dissolve(2)
        r2 "那股怒气总有一天会有用。先留着。"
        r2 "但现在，你能……"
        scene day5_isabellalittlesecret_137
        with Dissolve(1)
        r2 "*咳咳* 先把我放下来？"
        scene day5_isabellalittlesecret_138
        with Dissolve(1)
        r2 "我不喜欢这种天气。"
        scene day5_isabellalittlesecret_139
        with Dissolve(1)
        r2 "所以？我在等……"
        scene day5_isabellalittlesecret_138
        with Dissolve(1)
        pause
        scene day5_isabellalittlesecret_140
        with Dissolve(1)
        r2 "谢谢。"
        scene day5_isabellalittlesecret_140
        with Dissolve(1)
        pause
        r2 "你到底要不要亲我？"
        r2 "你挺可爱的，但不是我喜欢的类型。"
        r2 "还有，我有点糊涂。如果那样发生了，算不算手淫？"
        scene day5_isabellalittlesecret_141
        with Dissolve(2)
        r1 "滚开。"
        scene black
        with Dissolve(3)
        pause
        
    label day5_dd_julie:  
        scene day5_dd_julie_1
        with Dissolve(2)
        r2 "（你得控制我们的心率。）"
        r1 "（现在可没那么容易。）"
        r2 "（我们在工作，好吗？先都放一放。以后再说。）"
        r2 "（我们不需要解决所有问题。）"
        r2 "（所以先呼吸。放轻松。冷静。）"
        scene day5_dd_julie_1
        with hpunch
        ja "你要把所有人都害死！"
        lila "我根本不在乎！"
        lila "你必须按我说的做！"
        scene day5_dd_julie_2
        with Dissolve(2)
        ju "呃……各位……"
        ju "不是这么演的……"
        scene day5_dd_julie_3
        with Dissolve(2)
        ju "记住……你们已经不是二十一世纪的女生了。"
        ju "不能那样说话、那样表现。你得进入角色。"
        scene day5_dd_julie_4
        with Dissolve(1)
        lila "可是……我们正在这么做啊……"
        scene day5_dd_julie_3
        with Dissolve(2)
        ju "[lila]，拜托……"
        ju "你是公主，施威没问题。"
        ju "但你同时也是圣骑士。你的角色是守序善良。"
        ju "「谁生谁死我不在乎」这话太脱离角色了。"
        scene day5_dd_julie_4
        with Dissolve(1)
        lila "可是我——"
        scene day5_dd_julie_5
        ju "不许「可是」！演好一点！"
        scene day5_dd_julie_6
        with Dissolve(1)
        ja "拜托，姐——"
        scene day5_dd_julie_5
        ju "还有你！"
        scene day5_dd_julie_6
        with Dissolve(1)
        ju "我知道你在塑造一个强势的角色，但你不能这样跟你未来的女王说话。"
        ju "那样会被杀掉的。"
        ju "那个时代的人都知道！"
        ju "只因为现实里[lila]是你朋友、不会杀你就那样演，那是元游戏！"
        ju "我昨晚已经跟你解释过了！"
        scene day5_dd_julie_3
        with Dissolve(1)
        ju "我们能拜托再试一次吗——？"
        scene day5_dd_julie_7
        with Dissolve(1)
        ash "没关系，[ju]。"
        ash "我们可以再来一次。"
        scene day5_dd_julie_8
        with Dissolve(1)
        ju "这才是我的好姑娘！"
        scene day5_dd_julie_9
        with Dissolve(1)
        ju "记住了，要演！"
        scene day5_dd_julie_4
        with Dissolve(1)
        ju "轮到你了，[lila]。"
        ju "整场重来。你把他们召集到了作战室。"
        lila "没错！"
        play sound "audio/Flash.ogg" volume 0.5
        play music "audio/soundtrack/haunted_castle.ogg" volume 0.5 fadein 5 
        scene day5_dd_julie_10
        with flashbulb
        lila "各公会的情况如何？"
        scene day5_dd_julie_11
        with Dissolve(1)
        ash "法师公会还没查到任何入侵相关的情报。"
        ash "如果我们获准进行（沟通）——"
        play sound "audio/hitwood1.ogg"
        scene day5_dd_julie_12
        with hpunch
        lila "我绝不会允许在我的王国里搞恶魔召唤。"
        lila "那是违法的！"
        scene day5_dd_julie_11
        with Dissolve(1)
        ash "现在是战时。至少可以请教——"
        play sound "audio/hitwood1.ogg"
        scene day5_dd_julie_12
        with hpunch
        lila "够了！"
        scene day5_dd_julie_13
        with Dissolve(1)
        lila "*叹气*"
        scene day5_dd_julie_14
        with Dissolve(1)
        lila "盗贼公会？"
        scene day5_dd_julie_15
        with Dissolve(1)
        pause
        scene day5_dd_julie_16
        with dissolve
        pause
        play sound "audio/meow1.ogg"
        asu "喵？"
        stop music
        play sound "audio/stopsound1.ogg" volume 0.5
        scene day5_dd_julie_17
        with hpunch
        play soundlow "audio/girlslaugh1.ogg" volume 0.5
        "女生们哄堂大笑。"
        scene day5_dd_julie_18
        with Dissolve(1)
        ju "天啊……"
        scene day5_dd_julie_19
        with hpunch
        pause
        scene day5_dd_julie_20
        with Dissolve(1)
        asu "拜托，Juju……那可是教科书级的角色扮演。"
        scene day5_dd_julie_19
        ju "才不是！"
        ju "那太尬了！"
        scene day5_dd_julie_21
        with Dissolve(1)
        ja "很好笑啊，姐。"
        scene day5_dd_julie_19
        ju "我当初就该选蒸汽朋克。或者《克苏鲁的呼唤》。"
        ju "选奇幻就是个错误。你们根本没法认真玩！"
        scene day5_dd_julie_22
        with Dissolve(1)
        r1 "这里都还好吗？"
        ju "不好！她们很臭！"
        r1 "是吗？"
        ju "很臭！臭死了！"
        scene day5_dd_julie_21
        with Dissolve(1)
        ja "[ju]，你知道你在跟谁说话吗？"
        scene day5_dd_julie_22
        with Dissolve(1)
        ju "不知道……为什么？"
        scene day5_dd_julie_24
        with Dissolve(1)
        ju "哦！是您啊，先生……"
        ju "刚才没太听清您的声音。抱歉。"
        scene day5_dd_julie_23
        with Dissolve(1)
        r1 "我听到有人在喊。出了什么事吗？"
        scene day5_dd_julie_24
        with Dissolve(1)
        ju "她们……呃……很臭！请恕我直言，先生。她们很臭。"
        scene day5_dd_julie_25
        with Dissolve(1)
        r1 "谁能解释一下？"
        scene day5_dd_julie_26
        with Dissolve(1)
        ju "我们在等体育课的时候玩龙与地下城。"
        scene day5_dd_julie_25
        with Dissolve(1)
        r1 "龙什么？"
        scene day5_dd_julie_24
        with Dissolve(1)
        ju "角色扮演游戏。"
        scene day5_dd_julie_23
        with Dissolve(1)
        r1 "[ju]，把书从脸上拿开。"
        scene day5_dd_julie_24
        with Dissolve(1)
        ju "哦……抱歉！"
        scene day5_dd_julie_27
        with Dissolve(1)
        ju "RPG！角色扮演游戏！"
        scene day5_dd_julie_23
        with Dissolve(1)
        r1 "角色扮演？！"
        scene day5_dd_julie_28
        with Dissolve(1)
        ash "这是个游戏。你多少得扮演虚构世界里的一个角色。"
        ash "是[ju]的主意。一开始是有点尬……"
        scene day5_dd_julie_29
        ju "才不尬！"
        scene day5_dd_julie_28
        with Dissolve(1)
        ash "但上手之后还挺酷的。"
        scene day5_dd_julie_29
        with Dissolve(1)
        ju "前提是你们真的上手了。"
        scene day5_dd_julie_30
        with Dissolve(1)
        asu "你得稍微用点想象力。"
        asu "我是个盗贼。"
        scene day5_dd_julie_25
        with Dissolve(1)
        r1 "盗贼？"
        scene day5_dd_julie_30
        with Dissolve(1)
        asu "不是那种「偷东西的贼」。"
        scene day5_dd_julie_31
        with Dissolve(1)
        asu "嗯……我就是个贼贼。"
        asu "但是……"
        scene day5_dd_julie_32
        with Dissolve(1)
        asu "创建角色时你可以选种族和职业。"
        asu "我是盗贼。或者说「游荡者」。这就是我的职业。"
        asu "我的职业偏向潜行，所以我选了一个相配的种族。"
        asu "所以我是「半塔巴西」。一种带猫科特征的人类，是人类和塔巴西族通婚的结果。"
        asu "一个半塔巴西盗贼。"
        scene day5_dd_julie_33
        with Dissolve(1)
        ju "我真为你骄傲。"
        scene day5_dd_julie_34
        with Dissolve(1)
        r1 "所以你爸妈跟猫配对过？"
        scene day5_dd_julie_35
        with Dissolve(1)
        asu "什么？！"
        asu "不，你——"
        asu "不是那样的，那——"
        scene day5_dd_julie_36
        with Dissolve(1)
        asu "啊，糟了。"
        scene day5_dd_julie_37
        with Dissolve(1)
        ju "嗯……我从没想过这个。"
        ju "嗯……倒也不是你的父母，但往上追溯几代……"
        ju "是啊……该死。"
        scene day5_dd_julie_38
        with Dissolve(1)
        ja "喂！不许歧视！"
        ja "爱有很多种形态！"
        scene day5_dd_julie_39
        with hpunch
        asu "不包括这种爱！不包括！"
        scene day5_dd_julie_40
        with Dissolve(1)
        asu "我留下永久心理阴影了。"
        play soundlow "audio/girlslaugh1.ogg" volume 0.5
        scene day5_dd_julie_17
        with hpunch
        "女生们咯咯笑起来。"
        scene day5_dd_julie_55
        with Dissolve(1)
        lila "你有尾巴吗？"
        scene day5_dd_julie_56
        with Dissolve(1)
        asu "姑娘，你要点脸！"
        scene day5_dd_julie_41
        with Dissolve(1)
        r1 "嗯。"
        scene day5_dd_julie_42
        with Dissolve(1)
        r1 "我上瘾了。"
        r1 "怎么不多跟我讲讲？"
        scene day5_dd_julie_44
        with Dissolve(1)
        r1 "你是什么？"
        ju "我是地下城主。"
        r1 "好吧，我们能别再讲黑话了？"
        r1 "连 RPG 是什么意思都不知道，我怎么会知道 DM 是什么？"
        scene day5_dd_julie_45
        with Dissolve(1)
        lila "你对缩写有点意见，对吧？"
        scene day5_dd_julie_46
        with Dissolve(1)
        asu "他有吗？"
        scene day5_dd_julie_78
        with Dissolve(1)
        pause
        scene day5_dd_julie_79
        with Dissolve(1)
        lila "我只是把心里话说出来了。"
        scene day5_dd_julie_47
        with Dissolve(1)
        ju "不过他说得对。"
        ju "我们对新玩家要有点耐心。"
        scene day5_dd_julie_44
        with Dissolve(1)
        r1 "新玩家？"
        ju "我已经决定让你加入了。"
        scene day5_dd_julie_44_1
        with Dissolve(1)
        ju "群星又一次排列正确了！而我们的桌面正处于宇宙动荡的最中心！"
        scene day5_dd_julie_21
        with Dissolve(1)
        ja "现在，请像个正常人一样说话。"
        scene day5_dd_julie_44
        with Dissolve(1)
        r1 "你听起来有点……执着过头了。"
        ju "我更愿意用「有热情」这个词。"
        ju "那么，你愿意跟我们一起玩吗？"
        r1 "要是我拒绝呢？"
        scene day5_dd_julie_48
        with Dissolve(1)
        pause
        scene day5_dd_julie_49
        with Dissolve(2)
        pause
        play sound "audio/slap.ogg"
        scene day5_dd_julie_50
        with hpunch
        pause
        scene day5_dd_julie_51
        with Dissolve(1)
        asu "哎哟！你干嘛打我？！"
        ash "你非教她这个不可。"
        asu "教什么？！"
        ash "假哭！"
        scene day5_dd_julie_52
        with Dissolve(1)
        asu "哦……"
        scene day5_dd_julie_53
        asu "对，那玩意儿挺好玩的。"
        scene day5_dd_julie_54
        ja "才不好玩！"
        ja "反正在家受罪的不是你。"
        scene day5_dd_julie_55
        with Dissolve(1)
        lila "我一直都想那么做。"
        scene day5_dd_julie_56
        with Dissolve(1)
        asu "哦，特别简单。你只要想着——"
        play sound "audio/slap.ogg"
        scene day5_dd_julie_50
        with hpunch
        pause
        scene day5_dd_julie_51
        asu "住手！"
        scene day5_dd_julie_57
        ash "别再教别人这个了！"
        scene day5_dd_julie_58
        asu "喂，要怪就怪游戏，别怪玩家！"
        asu "她脸挺漂亮的，应该多用用！"
        scene day5_dd_julie_59
        with Dissolve(1)
        pause
        scene day5_dd_julie_60
        with Dissolve(1)
        ju "先生，您觉得我够火辣吗？"
        scene day5_dd_julie_76
        with Dissolve(1)
        r1 "火辣？你这话什么意思——"
        scene day5_dd_julie_60
        with Dissolve(1)
        ju "哦，不对。抱歉。呃……泼辣！您觉得我是个泼辣的拉丁裔女孩吗？"
        scene day5_dd_julie_61
        with hpunch
        ja "[ju!u]！"
        scene day5_dd_julie_63
        ju "什么？"
        scene day5_dd_julie_62
        ja "先生，实在太抱歉了。"
        scene day5_dd_julie_64
        ju "什么？[asu]老这么说我。"
        scene day5_dd_julie_66
        asu "但不是对着他！"
        scene day5_dd_julie_65
        asu "天啊，姑娘！"
        scene day5_dd_julie_67
        asu "先生你看。我在教[ju]一些东西。"
        scene day5_dd_julie_65
        asu "而据「显然」所示，她不知道这种话能对谁说、不能对谁说！"
        scene day5_dd_julie_63
        with Dissolve(1)
        ju "可是……我问一句有什么害处……你们为什么都冲我喊？"
        scene day5_dd_julie_62
        with Dissolve(1)
        ja "天啊，[ju]。你有时候真把自己搞得很尴尬……"
        scene day5_dd_julie_63
        with Dissolve(1)
        ju "我不明白……"
        ju "有什么害处……"
        scene day5_dd_julie_65
        asu "这不合适，行了吧？！"
        asu "尤其是在公共场合！还对着一个男人！"
        scene day5_dd_julie_63
        with Dissolve(1)
        ju "可是……只是个问题而已……"
        scene day5_dd_julie_68
        with Dissolve(1)
        menu:
            "算了。不过你那个问题是什么意思？":
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[ju]的{color=#00ff00}好感{/color}上升了{color=#00ff00}5{/color}点！" )
                $love_ju+=5
                scene day5_dd_julie_69
                with Dissolve(1)
                ju "哦！呃……"
                ju "[asu]刚说了[lila]很漂亮。我就想起她说我的时候也是这么说的。"
                ju "而且我能相信你吧？所以我就问了。"
                hide notifyEx
                scene day5_dd_julie_70
                with Dissolve(1)
                asu "她脑子有时候就是这样。"
                scene day5_dd_julie_71
                ja "但你不能把想到的都随口说出来、都问出来！"
                scene day5_dd_julie_72
                with Dissolve(1)
                r1 "嗯。"
                scene day5_dd_julie_73
                with Dissolve(1)
                r1 "我大概明白她们的意思了。"
                r1 "你看。她们说得对。你要是一直这样，总有一天会惹上麻烦。"
                r1 "但这次不会。"
                r1 "现在这里只有我们。所以我可以说，你想什么时候对我坦诚都可以，而且应该坦诚。"
                scene day5_dd_julie_74
                with Dissolve(1)
                r1 "我对你们每一个人都是这话，明白吗？"
                scene day5_dd_julie_73
                with Dissolve(1)
                r1 "但别在别人面前这样。"
                ju "为什么不行？"
                scene day5_dd_julie_76
                with Dissolve(1)
                pause
                scene day5_dd_julie_72
                with Dissolve(1)
                pause
                scene day5_dd_julie_75
                with Dissolve(1)
                ju "欢迎。"
                scene day5_dd_julie_73
                with Dissolve(1)
                r1 "你看不出那会被怎么理解吗？"
                ju "看不出？有什么问题吗？"
            "她们说得对。你得明白我仍然是你的校长。":
                ju "但我不是那个意思……"
                ju "我只是想……"
                ju "唉，算了。"
        scene day5_dd_julie_77
        with Dissolve(1)
        ash "你真是太纯洁了。"
        scene day5_dd_julie_80
        with Dissolve(1)
        asu "我得挑更好的闺蜜了。"
        scene day5_dd_julie_81
        with Dissolve(1)
        lila "你的闺蜜们得挑更好的[asu]。"
        scene day5_dd_julie_82
        with Dissolve(1)
        asu "可惜她们只做出了一个原版。"
        scene day5_dd_julie_83
        with Dissolve(1)
        asu "我是正版。"
        scene day5_dd_julie_82
        with Dissolve(1)
        asu "拒绝仿制品。"
        scene day5_dd_julie_84
        with Dissolve(1)
        r1 "等等……你说你……在教她？"
        r1 "教什么？"
        scene day5_dd_julie_85
        with Dissolve(1)
        pause
        scene day5_dd_julie_86
        with Dissolve(1)
        pause
        scene day5_dd_julie_87
        with Dissolve(1)
        pause
        scene day5_dd_julie_88
        with Dissolve(1)
        r1 "嗯。"
        r2 "（你们听懂她想说什么了吗？）"
        r1 "（我他妈完全没听懂。）"
        r2 "（只是确认一下我们还对得上。）"
        scene day5_dd_julie_73
        with Dissolve(1)
        r1 "这事以后再说。"
        ju "你非走不可吗？"
        r1 "你们不是都有课吗？"
        scene day5_dd_julie_60
        with Dissolve(1)
        pause
        scene day5_dd_julie_59
        with Dissolve(1)
        ju "还剩多少分钟？"
        scene day5_dd_julie_77
        with Dissolve(1)
        ash "大概还有十五分钟。"
        scene day5_dd_julie_59
        with Dissolve(1)
        pause
        scene day5_dd_julie_89
        with Dissolve(1)
        ju "我真的很希望你能跟我们玩几分钟。"
        ju "前提是……你有时间的话……"
        scene day5_dd_julie_90
        with Dissolve(1)
        r1 "我从没玩过那种游戏。"
        r1 "大概就是不合我口味。"
        r1 "而且我不想扫你们的兴。"
        scene day5_dd_julie_89
        with Dissolve(1)
        ju "不试一下，你永远不会知道自己喜不喜欢！"
        scene day5_dd_julie_77
        with Dissolve(1)
        ash "说实话，我本来以为那会很难玩。"
        ash "结果我大错特错！"
        ash "这游戏挺好玩的。"
        scene day5_dd_julie_92
        with Dissolve(1)
        lila "你想当谁都行！"
        scene day5_dd_julie_93
        with Dissolve(1)
        asu "老实说，最好玩的就是逗[ju]。"
        scene day5_dd_julie_94
        with Dissolve(1)
        ja "就几分钟。你要是不喜欢，那就算了。"
        scene day5_dd_julie_95
        with Dissolve(1)
        pause
        scene day5_dd_julie_96
        with Dissolve(1)
        ju "不如你来帮我叙述？"
        scene day5_dd_julie_76
        with Dissolve(1)
        r1 "我要做什么？"
        scene day5_dd_julie_96
        with Dissolve(1)
        ju "过来。"
        scene day5_dd_julie_97
        with Dissolve(1)
        ju "{size=-7}你随时给我几个点子就行。"
        ju "{size=-7}先看我叙述，然后我们再往下走。"
        r1 "我试试。"
        scene day5_dd_julie_98
        with Dissolve(1)
        ju "好了，姑娘们。向他介绍一下自己。"
        scene day5_dd_julie_99
        with Dissolve(1)
        lila "我是圣骑士，也是公主。也就是说我纯洁而且——"
        scene day5_dd_julie_100
        asu "相似之处纯属巧合。"
        scene day5_dd_julie_101
        lila "而且这意味着我侍奉一位神明。"
        scene day5_dd_julie_102
        with Dissolve(1)
        asu "我刚说了，我是半塔巴西。我专精潜行与间谍活动。"
        asu "我在盗贼公会。而且我们「严格来说」并不存在。"
        asu "除非我们对王国有用。否则我们只是个传说。"
        scene day5_dd_julie_103
        with Dissolve(1)
        ash "我其实是个女巫。也就是说我和恶魔及邪恶神祇沟通。"
        ash "不过我属于法师公会。他们多少算学者。"
        ash "他们靠研究学习魔法。"
        ash "所以从恶魔那里汲取力量多少有点不受待见。而且是违法的。"
        ash "除非事先获得许可。"
        scene day5_dd_julie_104
        with Dissolve(1)
        ja "别笑，不过呃……"
        ja "我是个格斗家。"
        scene day5_dd_julie_105
        with Dissolve(1)
        r1 "哦？"
        scene day5_dd_julie_106
        with Dissolve(1)
        ja "别……别那样看我……"
        ja "徒手打架听起来很酷……就这样。"
        scene day5_dd_julie_104
        with Dissolve(1)
        ja "而且我是冒险者公会的一员……"
        ja "算是某种探路者或者佣兵。"
        scene day5_dd_julie_107
        with Dissolve(1)
        ju "而我是地下城主。DM。"
        ju "也就是说我是说故事的人。"
        scene day5_dd_julie_108
        with Dissolve(1)
        r1 "这一切听起来真够复杂的。"
        scene day5_dd_julie_109
        with hpunch
        ju "对吧？！"
        scene day5_dd_julie_110
        with Dissolve(1)
        ju "姑娘们在作战室。"
        ju "[lila]把她们召来，作为各自公会的代表。"
        ju "边境地区有遭遇战的报告。"
        ju "整支连队的士兵被发现全部死亡，却找不到任何敌人的尸体。"
        ju "只找到平民、士兵和牲畜的尸体——全都被开膛破肚。"
        scene day5_dd_julie_108
        with Dissolve(1)
        r1 "这……比我想象中你们几个会干的事要黑暗多了。"
        scene day5_dd_julie_109
        with hpunch
        ju "对吧？！"
        ju "我整周都在想这个！"
        scene day5_dd_julie_110
        with Dissolve(1)
        ju "总之，[lila]召她们来调查、寻找线索。"
        play music "audio/soundtrack/haunted_castle.ogg" volume 0.5 fadein 5 
        play sound "audio/Flash.ogg" volume 0.5
        scene day5_dd_julie_14
        with flashbulb
        lila "盗贼公会？"
        scene day5_dd_julie_15
        with Dissolve(1)
        pause
        scene day5_dd_julie_16
        with dissolve
        pause
        scene day5_dd_julie_15
        with Dissolve(1)
        asu "没什么。"
        scene day5_dd_julie_14
        with Dissolve(1)
        lila "嗯。"
        scene day5_dd_julie_111
        with Dissolve(1)
        lila "猫女，你在看什么？"
        scene day5_dd_julie_15
        with Dissolve(1)
        pause
        scene day5_dd_julie_16
        with dissolve
        pause
        scene day5_dd_julie_15
        with Dissolve(1)
        asu "是半塔巴西。"
        scene day5_dd_julie_112
        with Dissolve(1)
        asu "你已经调集了兵力，并在山边那条旧路上把巡逻翻倍。"
        scene day5_dd_julie_16
        with dissolve
        asu "为什么？"
        scene day5_dd_julie_14
        with Dissolve(1)
        lila "袭击就发生在那里。增援也是投在那里。"
        scene day5_dd_julie_16
        with dissolve
        pause
        scene day5_dd_julie_15
        with dissolve
        pause
        scene day5_dd_julie_16
        with dissolve
        asu "袭击的频率是多少？"
        scene day5_dd_julie_14
        with Dissolve(1)
        lila "至少每周一次。为什么？"
        scene day5_dd_julie_16
        with dissolve
        asu "那增援到位之后，王国又遭受了多少次袭击？"
        scene day5_dd_julie_14
        with Dissolve(1)
        lila "一次都没有。"
        lila "别玩心理战了。有话直说。"
        scene day5_dd_julie_16
        with dissolve
        pause
        scene day5_dd_julie_15
        with dissolve
        asu "增援没用。"
        scene day5_dd_julie_14
        with Dissolve(1)
        lila "这算哪门子议会？"
        lila "他们正在阻止袭击。"
        lila "这叫威慑。边境增派了守卫，所以袭击才没再发生。"
        scene day5_dd_julie_16
        with dissolve
        pause
        scene day5_dd_julie_15
        with dissolve
        asu "他们转移到了别处。"
        asu "你分散兵力去加强那个位置。"
        asu "完全没有遭遇战。"
        scene day5_dd_julie_16
        with dissolve
        asu "杀害你子民的那个不管是人还是什么，已经不在那儿了。他们去了更脆弱、更无防备的乡间。"
        asu "有幸存者吗？"
        scene day5_dd_julie_14
        with Dissolve(1)
        pause
        scene day5_dd_julie_13
        with Dissolve(1)
        lila "*叹气*"
        scene day5_dd_julie_14
        with Dissolve(1)
        lila "有一个男人。"
        $ renpy.music.set_volume(0.1,2,"music")
        scene day5_dd_julie_108
        r1 "她怎么知道这些的？"
        scene day5_dd_julie_107
        with Dissolve(1)
        ju "开会前我分别跟她们谈过。"
        ju "我给了她们各自不同的部分信息。"
        ju "现在这场戏就自然地推进了，因为每个角色都在试着从别人那儿套信息。"
        scene day5_dd_julie_108
        with Dissolve(1)
        r1 "真聪明。"
        scene day5_dd_julie_109
        with hpunch
        ju "对吧？！"
        scene day5_dd_julie_110
        with Dissolve(1)
        ju "我喜欢一切都严丝合缝的感觉。"
        ju "闭上眼睛，你就能想象出整个场景。"
        ju "角色们交谈着，烛火噼啪作响，风在独眼巨人的石墙上呼啸。"
        scene day5_dd_julie_108
        r1 "独眼巨人什么？"
        scene day5_dd_julie_107
        with Dissolve(1)
        ju "哦，算了。继续吧。"
        $ renpy.music.set_volume(1,2,"music")
        play sound "audio/Flash.ogg" volume 0.5
        scene day5_dd_julie_113
        with flashbulb
        ja "为什么没人告诉我们有这个幸存者？"
        scene day5_dd_julie_12
        with Dissolve(1)
        lila "因为不管你们希望老百姓相信什么，你们的公会效忠的是这个王国，而不是反过来。"
        scene day5_dd_julie_16
        with dissolve
        pause
        scene day5_dd_julie_15
        with dissolve
        asu "是你们要求我们提供建议的。"
        scene day5_dd_julie_16
        with dissolve
        asu "你对我们隐瞒这些，我们怎么给建议。"
        scene day5_dd_julie_114
        with Dissolve(1)
        ash "这个男人是怎么活下来的？"
        ash "我们能跟他谈谈吗？"
        scene day5_dd_julie_115
        with Dissolve(1)
        pause
        scene day5_dd_julie_116
        with Dissolve(1)
        asu "我们能吗？"
        scene day5_dd_julie_14
        with Dissolve(1)
        pause
        lila "我的副官正在审问他。"
        $ renpy.music.set_volume(0.1,2,"music")
        scene day5_dd_julie_97
        with Dissolve(1)
        ju "{size=-7}我有个主意。"
        ju "{size=-7}如果她们去跟那个人谈话，我要你担任翻译。"
        scene day5_dd_julie_90
        with Dissolve(1)
        r1 "什么？我完全不知道怎么做。"
        scene day5_dd_julie_96
        with Dissolve(1)
        ju "拜托！很好玩的！"
        scene day5_dd_julie_90
        with Dissolve(1)
        pause
        r1 "我可以试试……"
        r1 "我要做什么？"
        scene day5_dd_julie_96
        with Dissolve(1)
        ju "搞定！"
        scene day5_dd_julie_97
        with Dissolve(1)
        ju "{size=-7}听着……你要翻译的那个人是……"
        $ renpy.music.set_volume(1,2,"music")
        play sound "audio/Flash.ogg" volume 0.5
        scene day5_dd_julie_113
        with flashbulb
        ja "我们必须跟他谈。"
        scene day5_dd_julie_117
        with Dissolve(1)
        lila "不可能。"
        scene day5_dd_julie_113
        with Dissolve(1)
        ja "为什么？"
        scene day5_dd_julie_117
        with Dissolve(1)
        lila "国家机密。"
        lila "而且我也不确定让平民靠近他是否安全。"
        scene day5_dd_julie_116
        with Dissolve(1)
        asu "但我们不只是平民，对吧？"
        scene day5_dd_julie_113
        with Dissolve(1)
        ja "恕我直言，女士。要么让我们帮忙，要么送我们回家。"
        stop music fadeout 5
        play music2 "audio/soundtrack/whenever.ogg" volume 0.3 fadein 5
        scene day5_dd_julie_117
        with Dissolve(1)
        pause
        scene day5_dd_julie_118
        with Dissolve(1)
        lila "跟我来。"
        scene black
        with Dissolve(2)
        pause
        scene day5_dd_julie_119
        with Dissolve(3)
        ju "{i}先前那些俘虏的遗骸，散落在这古老地牢的厅堂各处。{/i}"
        ju "{i}要是仔细听，你能听见小型啮齿动物躲在拱廊黑暗阴影里的吱吱声。{/i}"
        scene day5_dd_julie_120
        with Dissolve(2)
        ju "{i}你看到一些绳子被牢牢绑在坚固的建筑结构上，仿佛是为了捆住各种身材的囚犯而准备的。{/i}"
        scene day5_dd_julie_121
        with Dissolve(2)
        ju "{i}而当然，这位囚犯并不是普通的强盗。{/i}"
        scene day5_dd_julie_122
        with Dissolve(2)
        ju "{i}你走近这条走廊里最后一间还完好的牢房。{/i}"
        scene day5_dd_julie_123
        with Dissolve(2)
        ju "{i}他听见了你靠近的脚步声……{/i}"
        scene day5_dd_julie_124
        with Dissolve(2)
        ju "{i}……在长廊里回荡。{/i}"
        scene day5_dd_julie_123
        with Dissolve(2)
        ju "{i}但他意识到一个令人安心的事实。{/i}"
        #scene day5_dd_julie_123
        #with Dissolve(2)
        #pause
        ### THIS SHIT DOESN'T WORK
        scene day5_dd_julie_125 with Dissolve(1)
        ju "{i}随着你铠甲的零件彼此碰撞发出回响……{/i}"
        play sound "audio/open3.ogg"
        scene day5_dd_julie_127
        with Dissolve(1)
        ju "{i}他认出，走近他的人穿的并非廉价盔甲。{/i}"
        ju "{i}他明白那些铸塑的金属出自最好的材料和最老练的工匠之手。{/i}"
        play sound "audio/open2.ogg"
        scene day5_dd_julie_128
        with Dissolve(1)
        ju "{i}只可能属于王族。{/i}"
        ju "{i}你们走近他。他被两根绳子从手腕处锁在天花板上。{/i}"
        scene day5_dd_julie_129
        with Dissolve(1)
        ash "为什么把他绑起来？"
        scene day5_dd_julie_130
        with Dissolve(1)
        pause
        scene day5_dd_julie_131
        with Dissolve(1)
        lila "他不是平民。"
        scene day5_dd_julie_132
        with Dissolve(1)
        asu "很有意思。"
        scene day5_dd_julie_133
        with Dissolve(1)
        ja "那他是谁？"
        scene day5_dd_julie_134
        with Dissolve(1)
        lila "只要他肯回答。"
        scene day5_dd_julie_135
        with Dissolve(1)
        r1 "我不是来回答士兵问题的。"
        r1 "我一直在等公主。"
        r1 "你还真来了。"
        $ renpy.music.set_volume(0.1,2,"music2")
        scene day5_dd_julie_96
        ju "不！不对！"
        ju "你得用那个时代的方式说话。"
        scene day5_dd_julie_90
        with Dissolve(1)
        r1 "我要吗？"
        ju "对！"
        r1 "那个时代的人到底是怎么说话的？"
        scene day5_dd_julie_96
        with Dissolve(1)
        ju "来，我教你！"
        scene day5_dd_julie_97
        with Dissolve(1)
        ju "{size=-7}你要这样说话……{/size}"
        scene day5_dd_julie_97
        with Dissolve(1)
        pause
        r1 "嗯……现在我明白阿什莉为什么说有点尬了……"
        scene day5_dd_julie_97_1
        ju "一点也不尬！"
        r1 "好吧……我说。就……刚才那句是什么？"
        scene day5_dd_julie_97
        with Dissolve(1)
        ju "{size=-7}你应该这样开始……{/size}"
        $ renpy.music.set_volume(1,2,"music2")
        play sound "audio/Flash.ogg" volume 0.5
        scene day5_dd_julie_136
        with flashbulb
        r1 "你的战士们糟糕透顶，他们身上的臭味令人作呕。"
        r1 "在他们面前张口说话，只会让我的胃里翻江倒海。"
        $ renpy.music.set_volume(0.1,2,"music2")
        scene day5_dd_julie_90
        pause
        scene day5_dd_julie_165
        pause
        scene day5_dd_julie_7
        with Dissolve(1)
        ash "我喜欢。"
        scene day5_dd_julie_102
        with Dissolve(1)
        asu "你很擅长这个。"
        $ renpy.music.set_volume(1,2,"music2")
        play sound "audio/Flash.ogg" volume 0.5
        scene day5_dd_julie_137
        with flashbulb
        lila "过去三天，你一句话都没说。"
        lila "结果你一开口就是侮辱人的话。"
        scene day5_dd_julie_136
        with Dissolve(1)
        r1 "甘愿被折磨上三天三夜。"
        r1 "那你倒是告诉我，跟折磨你的人合作时，你又是何等热情。" 
        scene day5_dd_julie_138
        with Dissolve(1)
        ja "他做了什么？"
        scene day5_dd_julie_134
        with Dissolve(1)
        lila "人们发现他时，他双手沾满血迹，站在尸山血海之中。"
        scene day5_dd_julie_123
        with Dissolve(1)
        r1 "那些探究的目光时不时会成为麻烦。"
        r1 "你知道那是什么感觉，对吧？"
        scene day5_dd_julie_134
        with Dissolve(1)
        lila "你在说什么鬼话？"
        scene day5_dd_julie_123
        with Dissolve(1)
        r1 "我不是在跟你说话。"
        scene day5_dd_julie_139
        with Dissolve(1)
        pause
        scene day5_dd_julie_134
        with Dissolve(1)
        pause
        scene day5_dd_julie_140
        with Dissolve(1)
        pause
        play sound "audio/movearmor1.ogg"
        scene day5_dd_julie_141
        with Dissolve(1)
        lila "你们解释一下。"
        scene day5_dd_julie_139
        with Dissolve(1)
        ash "我不知道。"
        scene day5_dd_julie_142
        with Dissolve(1)
        pause
        scene day5_dd_julie_141
        with Dissolve(1)
        pause
        scene day5_dd_julie_134
        with Dissolve(1)
        lila "你是站在我们这边，还是对面？"
        scene day5_dd_julie_136
        with Dissolve(1)
        r1 "你会为你拍死的苍蝇感到一丝愧疚吗？"
        r1 "会为你杀的老鼠、踩死的蚂蚁愧疚吗？"
        r1 "我既不支持你，也不反对你。"
        r1 "因为神明不会为低等生灵费心。"
        $ renpy.music.set_volume(0.1,2,"music2")
        scene day5_dd_julie_109
        with hpunch
        ju "就要这样！！！"
        ju "这才是我想要的！"
        scene day5_dd_julie_166
        with Dissolve(1)
        ju "角色扮演！"
        scene day5_dd_julie_96
        with Dissolve(1)
        ju "靠！这句太帅了！"
        ju "干得漂亮！"
        ju "下次跑团前我们得多练练。你一定会很棒的！"
        scene day5_dd_julie_21
        with Dissolve(1)
        ja "放轻松，姐。"
        scene day5_dd_julie_161
        with Dissolve(1)
        r1 "谢了。"
        scene day5_dd_julie_156
        with Dissolve(1)
        lila "我们能不能别再毁场子，回去继续演？"
        $ renpy.music.set_volume(1,2,"music2")
        play sound "audio/Flash.ogg" volume 0.5
        scene day5_dd_julie_134
        with flashbulb
        lila "换作是你，被囚禁在地牢里绑着，我可不敢自称神明。"
        lila "现在别再把事情搞得更糟。"
        lila "你到底有没有情报要给？"
        scene day5_dd_julie_136
        with Dissolve(1)
        r1 "那你就赦免我？"
        scene day5_dd_julie_134
        with Dissolve(1)
        lila "是的，这在我权力之内。"
        scene day5_dd_julie_136
        with Dissolve(1)
        r1 "我明白了。"
        scene day5_dd_julie_134
        with Dissolve(1)
        lila "所以呢？"
        scene day5_dd_julie_136
        with Dissolve(1)
        r1 "山边有个叫安特莱索恩的村子。"
        r1 "下一次袭击在两个月亮周期之内。"
        r1 "你最好抓紧。"
        play sound "audio/movearmor1.ogg"
        scene day5_dd_julie_141
        with Dissolve(1)
        pause
        scene day5_dd_julie_144
        with Dissolve(1)
        lila "出发。"
        lila "我得派出斥候、布置防御，以防他说的是真的。"
        scene day5_dd_julie_123
        with Dissolve(1)
        r1 "那我的赦免呢？"
        scene day5_dd_julie_130
        with Dissolve(1)
        lila "我会向我的女神祈祷，请她赦免你。"
        play sound "audio/open2.ogg"
        scene day5_dd_julie_129
        with Dissolve(1)
        pause
        play sound "audio/open3.ogg"
        scene day5_dd_julie_123
        with Dissolve(1)
        pause
        scene day5_dd_julie_97
        with Dissolve(1)
        ju "{size=-7}来，把这句告诉阿什莉……{/size}"
        scene day5_dd_julie_145
        with Dissolve(1)
        r1 "他们知道你从何处汲取魔力吗？"
        r1 "仙灵。古籍与年鉴。背诵远古的咒语。"
        r1 "很无聊，对吧？"
        r1 "别的什么东西讨你欢心了。"
        scene day5_dd_julie_146
        with Dissolve(1)
        ash "当心那些下流的流言。"
        scene day5_dd_julie_145
        with Dissolve(1)
        r1 "我闻得到你身上那股恶魔的腐臭。"
        r1 "虽然表面光鲜……那一群嬉皮笑脸的谄媚之徒……并不是你真正的朋友。"
        r1 "他们只是觊觎你自己幻想出来的东西。"
        stop music2 fadeout 5
        play music "audio/soundtrack/climax1.ogg" volume 0.5 fadein 5
        scene day5_dd_julie_146
        with Dissolve(1)
        pause
        stop music fadeout 3
        scene day5_dd_julie_147
        with Dissolve(1.5)
        pause
        play sound "audio/smokinginhale.ogg"
        scene day5_dd_julie_147_1
        with Dissolve(1.5)
        pause
        ash "仔细听我说，农民。"
        ash "如果我听见你到处说些与你无关的事。"
        ash "我就烧干你肺里的空气，看着你挣扎。"
        #play music "audio/soundtrack/climax2.ogg" volume 0.2
        scene day5_dd_julie_148
        with Dissolve(1.5)
        pause 0.3
        scene day5_dd_julie_149
        with Dissolve(1.5)
        pause 0.3
        scene day5_dd_julie_151
        with Dissolve(1.5)
        pause 0.3
        scene day5_dd_julie_150
        with Dissolve(1.5)
        ash "囚徒，你对我所沟通的那些存在一无所知。"
        ash "我建议你闭嘴。"
        scene day5_dd_julie_152
        with Dissolve(1)
        r1 "我对它们的了解，远超你的臆测。"
        r1 "它们诞生的时候，我就在场。"
        r1 "你可以在那无意义的守夜中自以为站得笔直，以为能智胜远古的存在……"
        r1 "你的一生不过是它们生命长河中的一粒微尘。"
        r1 "终有一天它们会露出真面目。到那时……"
        r1 "你会来找我。"
        stop music
        stop music2
        play sound "audio/stopsound1.ogg" volume 0.5
        scene day5_dd_julie_153
        with hpunch
        ju "我的天啊！！！！！"
        scene day5_dd_julie_154
        ash "[ju]，你能不能别再打断我们了？！"
        scene day5_dd_julie_155
        ja "坦白说，我现在有点跟不上了。"
        scene day5_dd_julie_65
        asu "表面光鲜？！"
        scene day5_dd_julie_156
        lila "你是把字典吞了吗？"
        scene day5_dd_julie_65
        asu "光鲜？！认真的吗？！"
        scene day5_dd_julie_76
        with Dissolve(1)
        r1 "有那么糟吗？"
        scene day5_dd_julie_157
        with Dissolve(1)
        pause
        scene day5_dd_julie_158
        with Dissolve(1)
        ja "姐，你快流口水了。"
        scene day5_dd_julie_159
        asu "你肯定是想说「垂涎三尺」！"
        scene day5_dd_julie_160
        with Dissolve(1)
        ash "「涎水横流。」"
        scene day5_dd_julie_17
        play soundlow "audio/girlslaugh1.ogg" volume 0.5
        "姑娘们哄堂大笑。"
        scene day5_dd_julie_157
        with Dissolve(1)
        ju "别理她们。"
        ju "你太棒了！"
        scene day5_dd_julie_161
        with Dissolve(1)
        r1 "嗯，对我来说算是新尝试。"
        r1 "但我很高兴你玩得开心。"
        scene day5_dd_julie_162
        ju "你疯了吗？！我「喜欢」？！"
        scene day5_dd_julie_163
        ju "听着！我在筹备一个克苏鲁的呼唤模组！"
        ju "而且你「必须」帮我！"
        scene day5_dd_julie_164
        ju "那些台词会超级帅！"
        ju "肯定严丝合缝！"
        scene day5_dd_julie_167
        ju "你读过 H.P. 洛夫克拉夫特吗？"
        scene day5_dd_julie_168
        ju "喵啊啊啊啊啊！！"
        scene day5_dd_julie_169
        with hpunch
        ju "哈哈哈哈！"
        scene day5_dd_julie_170
        ju "对！"
        scene day5_dd_julie_171
        ju "那也太酷了！！"
        scene day5_dd_julie_172
        ju "你知道「Discord」是什么吗？"
        scene day5_dd_julie_173
        lila "好了，够了。"
        lila "我们得走了。"
        scene day5_dd_julie_174
        ash "我觉得[ju]被你搞疯了。"
        scene day5_dd_julie_175
        ja "姑娘，别在校外烦他。"
        scene day5_dd_julie_167
        ju "为什么不？我看见你发消息——"
        scene day5_dd_julie_176
        ja "你他妈给我闭嘴！"
        scene day5_dd_julie_177
        pause
        scene day5_dd_julie_178
        ash "你还好吗，贾丝敏？"
        scene day5_dd_julie_179
        ash "这事有点不对劲。"
        scene day5_dd_julie_180
        ja "没什么。"
        scene day5_dd_julie_179
        ash "你就打算这么敷衍我？"
        scene day5_dd_julie_181
        ja "对。她只是想搞我。"
        scene day5_dd_julie_182
        r1 "有件事我该知道——"
        play music "audio/soundtrack/AFixBackEast.mp3" fadein 5 volume 0.3
        scene day5_dd_julie_183
        pause
        scene day5_dd_julie_184
        pause
        scene day5_dd_julie_185
        with Dissolve(1)
        ja "先生？"
        scene day5_dd_julie_183
        with Dissolve(1)
        pause
        r1 "我要你们全都回教室。"
        r1 "马上。"
        scene day5_dd_julie_186
        with Dissolve(1)
        pause
        scene day5_dd_julie_187
        with Dissolve(1)
        pause
        scene day5_dd_julie_188
        with Dissolve(1)
        asu "好了，快撤，不然要迟到了。"
        ash "嗯，你说得对。"
        scene day5_dd_julie_189
        with Dissolve(1)
        lila "谢谢您陪我们玩，先生。"
        scene day5_dd_julie_183
        with Dissolve(1)
        r1 "我的荣幸。"
        scene day5_dd_julie_191
        with Dissolve(1)
        pause
        scene day5_dd_julie_190
        with Dissolve(1)
        r1 "你也是，[ja]。"
        ja "先生，我……"
        r1 "现在。"
        scene day5_dd_julie_192
        with Dissolve(1)
        pause
        scene day5_dd_julie_193
        with Dissolve(1)
        pause
        ju "喂，姐。"
        scene day5_dd_julie_195
        with Dissolve(1)
        ju "Jaz？"
        scene day5_dd_julie_194
        with Dissolve(1)
        ja "嗯？"
        scene day5_dd_julie_196
        with Dissolve(1)
        ju "你在生我的气吗？"
        scene day5_dd_julie_194
        with Dissolve(1)
        pause
        scene day5_dd_julie_197
        pause
        scene day5_dd_julie_198
        ja "什么？为什么？"
        scene day5_dd_julie_196
        with Dissolve(1)
        ju "我说错什么了吗？"
        ju "如果说了我道歉。"
        scene day5_dd_julie_198
        with Dissolve(1)
        pause
        scene day5_dd_julie_199
        with Dissolve(1)
        pause
        scene day5_dd_julie_200
        with Dissolve(1)
        ja "没事的，小鸟。"
        ja "别放心上。"
        scene day5_dd_julie_201
        with Dissolve(1)
        ja "没什么。"
        ju "Jaz……"
        ja "嗯？"
        ju "看着我。"
        scene day5_dd_julie_202
        with Dissolve(1)
        ja "抱歉。什么事？"
        scene day5_dd_julie_203
        with Dissolve(1)
        ju "我们之间不保留秘密，记得吗？"
        ju "{i}Cuéntame.{/i}{p=0.0}(告诉我。)"
        scene day5_dd_julie_204
        with Dissolve(1)
        pause
        scene day5_dd_julie_205
        with Dissolve(1)
        ja "还记得小时候我叫你别跟我们街区那几个男生走太近吗？"
        ju "那些毒贩？"
        scene day5_dd_julie_206
        pause
        scene day5_dd_julie_208
        pause
        scene day5_dd_julie_207
        with Dissolve(1)
        pause
        scene day5_dd_julie_209
        with Dissolve(1)
        ju "什么？我又不傻。"
        ju "我是几年后才反应过来的。"
        scene day5_dd_julie_207
        ju "只是我们从没聊过这件事。"
        ju "他们怎么了？"
        scene day5_dd_julie_210
        with Dissolve(1)
        pause
        scene day5_dd_julie_211
        with Dissolve(1)
        pause
        scene day5_dd_julie_212
        with Dissolve(1)
        ja "我当时有种不好的预感。但没什么。"
        ju "你确定？"
        ja "确定，没什么需要说的。"
        ja "No pasa nada……{p=0.0}(没事了。)"
        scene day5_dd_julie_211
        with Dissolve(1)
        ja "走吧？"
        ju "好！"
        scene day5_dd_julie_213
        with Dissolve(1)
        ja "话说，姐……"
        ja "帮我个忙。"
        ja "你说。"
        scene day5_dd_julie_214
        with Dissolve(1)
        ja "我先去趟洗手间。马上就来。"
        ju "要我等你吗？"
        ja "不用！没事！"
        ja "你先去吧！"
        ju "好！"
        scene day5_dd_julie_215
        with Dissolve(1)
        pause
        scene day5_dd_julie_216
        with Dissolve(1)
        pause
        scene day5_dd_julie_217
        pause
        scene day5_dd_julie_218
        with Dissolve(1)
        r1 "你觉得你跑到这儿来干什么？"
        scene day5_dd_julie_219
        with Dissolve(1)
        k "我就是想亲眼来看看你在这儿都干了些什么。"
        scene day5_dd_julie_220
        with Dissolve(1)
        r1 "你开什么玩笑。"
        play sound "audio/hit1l.ogg"
        scene day5_dd_julie_221
        with hpunch
        r1 "我可是把脑袋别在裤腰带上！"
        scene day5_dd_julie_222
        r1 "校园里有警察。"
        r1 "你知道被人看见会怎么样吗？"
        r1 "要是被任何一个学生看见呢？！"
        scene day5_dd_julie_223
        r1 "你不能在下班时间打电话吗？"
        r1 "你他妈早上才告诉我不许靠近你。"
        r1 "现在你就这么跑来了？！"
        r1 "你他妈是不是疯了？！"
        play sound "audio/hit1l.ogg"
        scene day5_dd_julie_224
        k "那警察又是谁放进来的？！"
        play sound "audio/hit1l.ogg"
        scene day5_dd_julie_225
        with hpunch
        k "是谁到现在都没拿出一点有用的东西？"
        scene day5_dd_julie_226
        k "就你一个人有麻烦？"
        k "我这边呢？！"
        k "这份工作可是我给你的。"
        play sound "audio/hit1l.ogg"
        scene day5_dd_julie_227
        with hpunch
        k "别忘了，在这儿不是你一个人在向上面汇报。"
        scene day5_dd_julie_228
        r1 "啊！"
        r1 "靠！"
        k "来吧，我没那么用力。"
        scene day5_dd_julie_229
        with Dissolve(1)
        k "你没事吧？"
        r1 "嗯，给我一分钟。"
        scene day5_dd_julie_230
        with Dissolve(1)
        r1 "我没事。"
        k "怎么了？"
        r1 "没什么。"
        k "别扯了，好吗？"
        k "直接说。"
        scene day5_dd_julie_231
        with Dissolve(1)
        r1 "*叹气*"
        scene day5_dd_julie_232
        with Dissolve(1)
        r1 "枪伤。"
        k "旧伤？"
        r1 "不是。"
        k "什么时候？"
        r1 "上周。"
        k "那你还在这儿干什么？"
        r1 "因为枪伤就不来上班，正好会把我的身份彻底搞砸。"
        k "有人怀疑什么吗？"
        r1 "没有。"
        k "好。"
        scene day5_dd_julie_233
        with Dissolve(1)
        k "是谁？"
        r1 "还不知道。职业杀手。"
        r1 "我怀疑是俄罗斯人。"
        k "你去医院了？"
        scene day5_dd_julie_234
        with Dissolve(1)
        r1 "[sophia]帮我处理的。"
        k "嗯。"
        r1 "怎么？"
        scene day5_dd_julie_233
        with Dissolve(1)
        k "随便问问。"
        k "算了。"
        scene day5_dd_julie_235
        with Dissolve(1)
        k "听着，我来这里的原因很简单。"
        k "你的手机关机了。"
        k "我正好有机会来看看你把这地方搞成了什么样。"
        k "我不知道这里有警察。知道的话我就不来了。"
        k "我给你的这份工作，你什么也不跟我说。"
        k "所以这是你的问题。"
        scene day5_dd_julie_236
        with Dissolve(1)
        k "听着，我这是以朋友的身份说的。如果你觉得自己没准备好，就告诉我。"
        k "如果你控制不住情绪。"
        k "如果你扛不住这种压力。"
        k "没关系，你随时可以交给我们接手。"
        scene day5_dd_julie_234
        with Dissolve(1)
        pause
        r1 "我没事。"
        k "很好，这才是我想听的。"
        scene day5_dd_julie_237
        with Dissolve(1)
        k "现在告诉我。"
        k "那些学生。"
        k "有什么我该知道的吗？"
        r1 "没什么值得一提的，除了我现在在跟市长接触。"
        k "其中一个是他女儿？"
        r1 "对。"
        k "很好。"
        scene day5_dd_julie_238
        with Dissolve(1)
        k "我就知道你没把本事丢了。"
        k "至于那个「职业杀手」，交给我们。"
        k "还有，请把手机开着。"
        scene day5_dd_julie_239
        with Dissolve(1)
        k "回头见，[r1]。"
        scene day5_dd_julie_239_1
        with Dissolve(1)
        k "再说一次。记住，手机保持开机。"
        scene day5_dd_julie_240
        with Dissolve(1)
        pause
        r1 "待会儿见，[k]。"
        scene day5_dd_julie_241
        with Dissolve(1)
        pause
        scene day5_dd_julie_242
        with Dissolve(1)
        pause
        r1 "电池没电了。"
        r1 "真棒。"
        scene day5_dd_julie_243
        with Dissolve(1)
        r1 "真是太棒了。"
        scene day5_dd_julie_243_1
        with Dissolve(1)
        pause
        r1 "蠢透了。"
        scene day5_dd_julie_244
        with Dissolve(2)
        pause
        scene day5_dd_julie_246
        with Dissolve(2)
        pause
        scene black
        with Dissolve(2)
        pause
        scene day5_dd_julie_247
        with Dissolve(2)
        pause
        scene day5_dd_julie_248
        with Dissolve(2)
        pause
        scene day5_dd_julie_249
        with Dissolve(2)
        r2 "他说得还真有点对。"
        r2 "我们是来办事的。"
        r2 "结果却牵扯进去了。"
        scene day5_dd_julie_250
        with Dissolve(2)
        pause
        scene day5_dd_julie_251
        with Dissolve(1)
        r1 "我知道。"
        r1 "我只是讨厌被人指手画脚地管工作。"
        scene day5_dd_julie_250
        with Dissolve(1)
        r1 "我以前是个更专业的。"
        scene day5_dd_julie_252
        with Dissolve(1)
        r2 "一旦掺杂了感情，我们就无法专业行事。"
        scene day5_dd_julie_251
        with Dissolve(1)
        pause
        scene day5_dd_julie_253
        with Dissolve(1)
        r1 "*叹气* 女人一向是我的软肋。"
        scene day5_dd_julie_252
        with Dissolve(1)
        r2 "得了吧。要是你早听我的，这一切都可以避免。"
        r2 "别他妈牵扯进去。"
        r2 "干我们的活。做必要的事。"
        r2 "然后他妈的活着离开。"
        scene day5_dd_julie_254
        with Dissolve(1)
        r1 "要是事情真那么简单就好了。"
        r2 "本来很简单！这才是问题！是你把事情搞复杂的。"
        scene day5_dd_julie_253
        with Dissolve(1)
        r1 "不过我至少还有一件事做得不错。"
        scene day5_dd_julie_252
        with Dissolve(1)
        r2 "你能别再自怨自艾了吗？"
        r2 "那样子太可悲了。我们比那强。"
        scene day5_dd_julie_255
        r1 "我他妈只是在用玩笑发泄烦躁。"
        r1 "而你太不懂事，根本体会不到我的矛盾。"
        scene day5_dd_julie_256
        r1 "这可不是「扣扳机」那么简单的工作。"
        r1 "我得接近他们。"
        r1 "赢得他们的信任。"
        r1 "他们会把梦想告诉我。"
        r1 "还有他们的恐惧。"
        r1 "然后我像个疯子一样从他们身上汲取一切。"
        scene day5_dd_julie_254
        with Dissolve(1)
        r1 "要是事情真那么简单就好了。"
        r1 "要是我能说一句「管他的呢」就好了。"
        scene day5_dd_julie_250
        with Dissolve(1)
        r1 "但我不行。"
        r1 "必要的话，我会做完我的工作。"
        scene day5_dd_julie_255
        r1 "但这不代表我不痛苦。"
        r1 "也不代表我他妈乐在其中！"
        scene day5_dd_julie_252
        with Dissolve(1)
        pause
        r2 "*哼*"
        scene day5_dd_julie_257
        with Dissolve(1)
        r2 "听着，小子。"
        r2 "我并不是不体谅你的矛盾。"
        r2 "我知道你恨我。但那只是你恨自己的投射。"
        r2 "我不是你的敌人。我是你的盟友。"
        r2 "我就是你。"
        scene day5_dd_julie_258
        with Dissolve(1)
        r1 "这套「我就是你」的说辞我听腻了。"
        r1 "你就没有别的话可说了吗？"
        scene day5_dd_julie_259
        with Dissolve(1)
        r2 "听着，小——"
        r2 "嗯……"
        scene day5_dd_julie_260
        with Dissolve(1)
        r2 "听着，[r1]。"
        r2 "你的每一份恐惧。"
        r2 "每一次恐慌发作。每一回不安或焦虑。"
        r2 "我都有。"
        scene day5_dd_julie_261
        with Dissolve(1)
        r2 "所以我们现在这个处境才让我这么火大。"
        r2 "每过一天，我就觉得更「活着」一点。"
        r2 "而这会把我们的软肋全都暴露在表面。"
        r2 "我不喜欢焦虑的感觉。"
        r1 "你以为我就喜欢？"
        r2 "我不是这个意思。"
        r2 "我被困住了。我得透过你的眼睛来看这个世界。"
        r2 "你不听我的，非要去犯一个完全可以避免的错误，还因此焦虑——我就得跟你一起受着。"
        r2 "而我想感觉爽。我想要肾上腺素。那种快感。"
        r2 "就现在这样？太可悲了。"
        scene day5_dd_julie_258
        with Dissolve(1)
        r1 "人生不只是美好的部分。"
        scene day5_dd_julie_261
        with Dissolve(1)
        r2 "你是什么？心灵导师吗？"
        r2 "一切都本可以避免。但「我们」把自己搞到了这一步。"
        r2 "所以，我们根本没必要受这份罪，却还是站在这儿。"
        r2 "还在为自找的错误争论不休。"
        scene day5_dd_julie_258
        with Dissolve(1)
        r1 "我想退出。"
        r1 "所以我在承受后果。"
        r1 "不管我怎么否认都是我选了这种生活。"
        scene day5_dd_julie_261
        with Dissolve(1)
        r2 "现在你说得像个男人了。"
        r1 "而我也选择了退出。"
        r1 "这种生活已经从我身上拿走了太多。"
        scene day5_dd_julie_260
        with Dissolve(1)
        r2 "它会永远拿走更多。"
        r2 "这个污点会永远跟着我们。人不可能说放下就放下。"
        r2 "你要是觉得不是这样，那你就是个傻子。"
        r2 "我告诉你这些，只是因为你自己早就明白了。"
        r2 "我们到死都会被它纠缠。"
        scene day5_dd_julie_258
        with Dissolve(1)
        pause
        r1 "我常常这么想。"
        r1 "到最后……"
        r1 "迟早有一天……"
        scene day5_dd_julie_261
        with Dissolve(1)
        r2 "……会有人砍下我们的脑袋。[ingrid]早就知道。"
        r2 "我们也知道。"
        r1 "人喂恶魔……"
        r2 "恶魔吞噬人……"
        scene day5_dd_julie_258
        with Dissolve(1)
        pause
        r1 "镜子里的那番话，我很抱歉。我明白你想告诉我什么。"
        scene day5_dd_julie_260
        with Dissolve(1)
        r2 "你只是伤害了自己。"
        r2 "而且我们都知道，你之所以像在跟真的我说话，只是因为你迫切需要什么。"
        scene day5_dd_julie_258
        with Dissolve(1)
        r1 "那会是什么？"
        scene day5_dd_julie_262
        with Dissolve(1)
        r2 "你知道答案。"
        scene day5_dd_julie_265
        with Dissolve(1)
        r2 "不过得承认，难得有人把我当人看，感觉还挺舒服的。"
        r1 "别习惯。"
        stop music fadeout 3
        play music2 "audio/soundtrack/finalcombat.ogg" fadein 3 volume 0.3 
        play sound "audio/open3.ogg"
        scene day5_dd_julie_263
        pause
        scene day5_dd_julie_264
        with Dissolve(2)
        pause
        scene day5_dd_julie_266
        with Dissolve(2)
        pause
        scene day5_dd_julie_263
        with Dissolve(1)
        pause
        scene day5_dd_julie_266
        with Dissolve(2)
        pause
        scene day5_dd_julie_267
        with Dissolve(1)
        pause
        scene day5_dd_julie_268
        with Dissolve(1)
        pause
        scene day5_dd_julie_269
        with Dissolve(1)
        ja "进来。"
        scene day5_dd_julie_270
        with Dissolve(1)
        r1 "什么？"
        scene day5_dd_julie_269
        with Dissolve(1)
        ja "进、来。"
        scene day5_dd_julie_270
        with Dissolve(1)
        r1 "玩的时间结束了，[ja]。"
        r1 "我没兴致。"
        scene day5_dd_julie_271
        with Dissolve(1)
        ja "我不是在征求你的意见，[r1]。"
        scene day5_dd_julie_272
        with Dissolve(1)
        pause
        scene day5_dd_julie_273
        with Dissolve(1)
        r1 "换作是我，现在会非常小心。"
        r1 "这不怪你，但我心情差得。你的态度半点忙都帮不上。"
        scene day5_dd_julie_274
        with Dissolve(1)
        r1 "这是怎么回事？"
        r1 "到底怎么了？"
        scene day5_dd_julie_275
        with Dissolve(1)
        pause
        scene day5_dd_julie_274
        with Dissolve(1)
        r1 "所以呢？"
        scene day5_dd_julie_277
        with Dissolve(1)
        pause
        scene day5_dd_julie_276
        with Dissolve(1)
        r1 "你是认真的吗？"
        play sound "audio/fastmove1.ogg"
        scene day5_dd_julie_278
        pause
        play sound "audio/fastmove1.ogg"
        scene day5_dd_julie_279
        pause
        scene day5_dd_julie_280
        pause
        scene day5_dd_julie_281
        pause
        play sound "audio/fastmove1.ogg"
        scene day5_dd_julie_282
        pause
        play sound "audio/throw2.ogg"
        scene day5_dd_julie_284
        with hpunch
        pause
        scene day5_dd_julie_283
        with Dissolve(1)
        r1 "小心点，姑娘。我挺喜欢你的。但要小心。"
        scene day5_dd_julie_285
        with Dissolve(1)
        r1 "你至少告诉我发生了什么吧？"
        r1 "深呼吸。我们可以谈。"
        scene day5_dd_julie_286
        with Dissolve(1)
        ja "谈什么？你就是个骗子。"
        scene day5_dd_julie_287
        with Dissolve(1)
        r1 "我身上有很多标签，[ja]。"
        r1 "骗子不在其中。"
        scene day5_dd_julie_286
        with Dissolve(1)
        ja "你怎么敢当面这么说？"
        scene day5_dd_julie_287
        with Dissolve(1)
        r1 "我怎么就是骗子了？"
        r1 "你在说什么？"
        scene day5_dd_julie_288
        with Dissolve(1)
        pause
        play sound "audio/fastmove1.ogg"
        scene day5_dd_julie_289
        pause
        play sound "audio/throw1.ogg"
        scene day5_dd_julie_290
        pause
        play sound "audio/fastmove1.ogg"
        scene day5_dd_julie_291
        pause
        play sound "audio/throw2.ogg"
        scene day5_dd_julie_292
        with hpunch
        pause
        scene day5_dd_julie_293
        with Dissolve(1)
        r1 "听着，你是个好学生。我也很喜欢教你。看到你学了我几招，我很欣慰。"
        r1 "但你糊弄不了我。"
        r1 "我教了你很多，但你还是太嫩。"
        r1 "现在别再犯傻了。"
        r1 "跟我说话。到底怎么了？"
        scene day5_dd_julie_292
        pause
        scene day5_dd_julie_295
        with Dissolve(1)
        pause
        play sound "audio/fastmove1.ogg"
        scene day5_dd_julie_294
        pause
        scene day5_dd_julie_296
        pause
        scene day5_dd_julie_297
        with Dissolve(1)
        r1 "你就是不知道什么时候该放弃，对吧？"
        scene day5_dd_julie_298
        with Dissolve(1)
        r1 "*啧*"
        scene day5_dd_julie_299
        pause
        scene day5_dd_julie_300
        pause
        play sound "audio/fastmove1.ogg"
        scene day5_dd_julie_301
        pause
        play sound "audio/throw2.ogg"
        scene day5_dd_julie_302
        with hpunch
        pause
        scene day5_dd_julie_297
        with Dissolve(1)
        pause
        r1 "姑娘，我不会跟你动手。"
        r1 "我不想，也没有任何理由。"
        scene day5_dd_julie_303
        with Dissolve(1)
        r1 "听着……跟我说吧。"
        scene day5_dd_julie_304
        with Dissolve(1)
        ja "你到底是谁，[r1]？"
        r1 "我该说什么好呢？"
        r1 "你知道我是谁。"
        ja "我对你屁都不了解。"
        ja "你不知道从哪儿冒出来的。"
        scene day5_dd_julie_305
        r1 "注意用词。"
        r1 "我知道你在生气。但我在努力讲道理。"
        scene day5_dd_julie_304
        ja "你打架的样子像在拼命。你跟办公室职员一点都不像。"
        ja "你走进我们那片街区就跟没事人一样。"
        ja "大多数有钱人端着那种架子，连靠近都不敢。"
        ja "可你不一样。你连一点不适都没有。"
        scene day5_dd_julie_305
        r1 "我只是——"
        scene day5_dd_julie_304
        ja "让我说完！"
        ja "你让我离你那么近。"
        ja "你赢得了我的信任。"
        ja "然后呢？！"
        scene day5_dd_julie_305
        r1 "[ja]，我不——"
        play sound "audio/fastmove1.ogg"
        scene day5_dd_julie_306
        with hpunch
        pause
        play sound "audio/throw2.ogg"
        scene day5_dd_julie_307
        ja "你他妈为什么要靠近我？"
        ja "你到底想从我这儿得到什么？"
        ja "你为什么要去接近[lila]？！"
        scene day5_dd_julie_308
        with hpunch
        ja "你他妈到底想对我们做什么？！"
        scene day5_dd_julie_309
        r1 "好了，冷静点。"
        r1 "为什么要问这么多问题？"
        r1 "至少让我先弄清楚状况。"
        scene day5_dd_julie_310
        with Dissolve(1)
        ja "我听到你在跟那个人说话。"
        ja "他是什么人？毒贩？！"
        ja "他为什么要打听[lila]？！"
        ja "这跟[ch]有关系吗？"
        scene day5_dd_julie_311
        with Dissolve(1)
        pause
        r1 "毒贩？[ch]？"
        r1 "什么？！"
        scene day5_dd_julie_310
        with Dissolve(1)
        ja "你听到了。这里只有我们两个。你可以直接看着我的眼睛说。"
        ja "你到底想干什么？"
        scene day5_dd_julie_311
        with Dissolve(1)
        r1 "[ju]……我是说——[ja]。"
        r1 "听着，我完全不知道你那些印象是从哪来的。"
        r1 "你下了太多结论。我们谈谈吧。"
        scene day5_dd_julie_312
        with Dissolve(1)
        ja "你知道你有多虚伪吗？"
        ja "Mierda，我以前那么崇拜你！"
        scene day5_dd_julie_311
        with Dissolve(1)
        ja "你让我觉得安全！"
        ja "你对我的烟做的事。你用走路送我回家。"
        scene day5_dd_julie_310_1
        with Dissolve(1)
        ja "你教我用跟你锻炼的方式「健康地」发泄怒火和不满。"
        ja "你一直在我身边！照顾我！"
        scene day5_dd_julie_313
        with Dissolve(1)
        ja "可这一切都只是个漂亮的谎言，对吧？你在利用我们。"
        scene day5_dd_julie_314
        ja "你为什么要把他带到这里来？！"
        scene day5_dd_julie_315
        with Dissolve(1)
        r1 "好吧……我不是想无礼。但你说完了吗？"
        r1 "我能起来吗？"
        scene day5_dd_julie_313
        with Dissolve(1)
        ja "不要再有谎言。也不要再耍花样。"
        scene day5_dd_julie_316
        with Dissolve(1)
        r1 "[ja]。在你动手打我之前，为什么不直接用这个开始谈话？"
        ja "你只会用话把自己开脱掉。"
        ja "脑子忙着打架的时候，根本想不出借口。这还是你教我的。"
        ja "我要知道真相！"
        scene day5_dd_julie_322
        with Dissolve(1)
        pause
        scene day5_dd_julie_318
        with Dissolve(1)
        ja "所以？"
        scene day5_dd_julie_322
        with Dissolve(1)
        r1 "我在想。"
        scene day5_dd_julie_322_1
        r1 "*啧* 天啊……"
        scene day5_dd_julie_322
        with Dissolve(1)
        r1 "听着……我告诉你是谁，你就会放开我吗？"
        scene day5_dd_julie_318
        with Dissolve(1)
        ja "也许？试试看。"
        scene day5_dd_julie_322
        with Dissolve(1)
        r2 "（别说出来。）"
        scene day5_dd_julie_322_2
        with Dissolve(1)
        pause
        r1 "他不是毒贩。他是我老板。"
        r2 "（真是的，小子。）"
        scene day5_dd_julie_318
        with Dissolve(1)
        ja "你……老板？"
        scene day5_dd_julie_317
        with Dissolve(1)
        r1 "[ja]，这是个政治单位。上面总得有人要交代。"
        scene day5_dd_julie_324
        with Dissolve(1)
        ja "不不不！我、我看得出你有多紧张！你想赶紧把我们打发掉，样子太明显了。你在藏什么。"
        scene day5_dd_julie_318
        with Dissolve(1)
        ja "听着，别再骗了！我看得出来他有问题。"
        ja "你又没做错任何事！你根本没理由紧张！"
        scene day5_dd_julie_322
        r1 "我不是因为自己才紧张的……是因为……"
        r1 "嗯……是因为……"
        scene day5_dd_julie_318
        with Dissolve(1)
        ja "因为什么？"
        scene day5_dd_julie_322_2
        with Dissolve(1)
        r1 "因为你。"
        scene day5_dd_julie_318
        ja "我？！"
        scene day5_dd_julie_322_2
        with Dissolve(1)
        pause
        scene day5_dd_julie_322
        with Dissolve(1)
        r1 "我是在保护你。"
        scene day5_dd_julie_318
        ja "我他妈有什么——"
        scene day5_dd_julie_317
        r1 "我不放心他待在你们几个女孩身边，好吗？！"
        r1 "不是你。不是[ju]。不是阿什莉。尤其不能在[lila]身边。"
        scene day5_dd_julie_318
        pause
        ja "为什么？"
        scene day5_dd_julie_317
        r1 "我真希望能跟你解释清楚……但我做不到。"
        r1 "你到底听到了什么？"
        scene day5_dd_julie_318
        with Dissolve(1)
        pause
        scene day5_dd_julie_319
        with Dissolve(1)
        ja "我没听清多少。"
        ja "他说他不知道校园里有警察，不然他就不会来了。"
        ja "还说他对市长的女儿有兴趣。我知道他说的是[lila]。"
        scene day5_dd_julie_320
        with Dissolve(1)
        r1 "[ja]，我有话要跟你说。"
        r1 "我是真心希望你能听进去。"
        r1 "你再也别再偷听我说话。"
        r1 "说清楚了？"
        scene day5_dd_julie_318
        with Dissolve(1)
        ja "听起来更像命令，不像建议。"
        scene day5_dd_julie_320
        with Dissolve(1)
        r1 "要我加个「请」字吗？求你了，别再有下次。"
        r1 "听懂了吗？！"
        scene day5_dd_julie_318
        with Dissolve(1)
        ja "先让我说——"
        scene day5_dd_julie_320
        r1 "你不用！"
        r1 "到底听懂了没有？！"
        scene day5_dd_julie_318
        with Dissolve(1)
        pause
        scene day5_dd_julie_319
        with Dissolve(1)
        pause
        scene day5_dd_julie_320
        with Dissolve(1)
        r1 "答应我。"
        scene day5_dd_julie_319
        with Dissolve(1)
        ja "[r1]，我……"
        scene day5_dd_julie_320
        r1 "答应我！"
        scene day5_dd_julie_318
        ja "为什么？！"
        scene day5_dd_julie_320
        r1 "因为我他妈担心你啊！"
        scene day5_dd_julie_326
        with Dissolve(1)
        pause
        scene day5_dd_julie_320
        with Dissolve(1)
        r1 "对不起……听我说。"
        r1 "我的上司有他自己的利益和盘算。"
        r1 "政治这场游戏里，没有心软的余地。"
        r1 "有人能在这场游戏里活下来，有人不能。"
        r1 "我拿你们的命去赌，赌不起，明白吗？"
        r1 "他当然会对[lila]表示兴趣！接近市长对他有利。"
        r1 "要是他发现你是她的朋友，他也会来接近你。而我不会让这种事发生。"
        scene day5_dd_julie_319
        with Dissolve(1)
        pause
        scene day5_dd_julie_318
        with Dissolve(1)
        ja "我手上没有任何筹码。"
        ja "我既没有人脉也没有——"
        scene day5_dd_julie_320
        r1 "你信我吗？"
        scene day5_dd_julie_321
        with Dissolve(1)
        ja "我该信吗？我怎么信？"
        scene day5_dd_julie_322
        with Dissolve(1)
        r1 "我以为我至少也换来了那么一点吧。"
        r1 "我有什么理由骗你？"
        scene day5_dd_julie_323
        ja "你想让我相信，你为我做这一切是出于什么？善心？"
        ja "就因为我是你的学生？就因为你人那么好？"
        ja "就因为我是你的学生，你半夜三更跑到我家来，冒着生命危险……还……还……"
        scene day5_dd_julie_324
        ja "我是说！"
        scene day5_dd_julie_322
        with Dissolve(1)
        r1 "[ja]……"
        scene day5_dd_julie_325
        with Dissolve(1)
        ja "你到底是……谁……？"
        scene day5_dd_julie_322
        with Dissolve(1)
        r1 "为什么你就这么难以接受，我只是单纯在乎你、没有任何私心呢？"
        scene day5_dd_julie_324
        ja "因为根本没人会这样！"
        scene day5_dd_julie_322
        with Dissolve(1)
        r1 "[ja]，拜托……"
        scene day5_dd_julie_325
        with Dissolve(1)
        ja "没有人，[r1]……没有人……"
        scene day5_dd_julie_322
        with Dissolve(1)
        r1 "嗯。我会。"
        r1 "看着我的眼睛。我想告诉你一件事。"
        scene day5_dd_julie_318
        with Dissolve(1)
        pause
        scene day5_dd_julie_322
        with Dissolve(1)
        r1 "我在乎你。别再怀疑这一点。"
        r1 "你也许不信。但你看看我为你做的一切。"
        r1 "我半夜跑到你家，只是想看看你过得好不好。"
        r1 "我在乎的不是你在哪，我在乎的是你。"
        r1 "我花时间亲自教你，却什么都没想得到。"
        r1 "我照顾你，是因为我{b}想{/b}照顾你。"
        scene day5_dd_julie_326
        with Dissolve(1)
        pause
        scene day5_dd_julie_327
        with Dissolve(1)
        pause
        scene day5_dd_julie_328
        with Dissolve(1)
        pause
        ja "我倒宁愿他真是个毒贩。"
        scene day5_dd_julie_329
        with Dissolve(1)
        pause
        ja "操。我真蠢。"
        scene day5_dd_julie_322
        r1 "[ja]，你不能这么冲动。"
        r1 "你怎么会觉得对我动手是个好主意？"
        r1 "那又能怎样？"
        scene day5_dd_julie_329
        with Dissolve(1)
        pause
        scene day5_dd_julie_330
        with Dissolve(1)
        ja "呃啊！"
        ja "对不起。我不敢看你。"
        scene day5_dd_julie_331
        with Dissolve(1)
        ja "我……我只是……对不起……"
        scene day5_dd_julie_332
        r1 "我还没说完。坐下。"
        scene day5_dd_julie_333
        with Dissolve(1)
        pause
        ja "没必要教训我。"
        ja "我知道后果是什么。"
        scene day5_dd_julie_334
        with Dissolve(1)
        r1 "不会有后果的。"
        scene day5_dd_julie_335
        with Dissolve(1)
        pause
        scene day5_dd_julie_336
        pause
        scene day5_dd_julie_337
        ja "什么？为什么不会？！"
        scene day5_dd_julie_334
        r1 "你想有后果吗？"
        scene day5_dd_julie_338
        ja "不想！"
        ja "可是我——"
        scene day5_dd_julie_334
        r1 "我踏上那张垫子的瞬间，就知道你打算干什么了。"
        r1 "我又不是傻子。"
        scene day5_dd_julie_339
        with Dissolve(1)
        r1 "听着，这种事你不是第一次干。"
        scene day5_dd_julie_340
        with Dissolve(2)
        r1 "你得明白——"
        r1 "就是——"
        ja "……？"
        scene day5_dd_julie_341
        with Dissolve(2)
        pause
        scene day5_dd_julie_342
        with Dissolve(1)
        ja "你没事吧？"
        r1 "嗯……就是有点晕……"
        scene day5_dd_julie_340
        with Dissolve(2)
        ja "你确定吗？你脸色很苍白。"
        r1 "嗯。我没事。"
        r1 "只是……"
        stop music2 fadeout 3
        play music "audio/soundtrack/AFixBackEast.mp3" fadein 5 volume 0.3
        scene day5_dd_julie_343
        with Dissolve(2)
        r1 "只是……"
        ja "老师？！"
        play sound "audio/dropbody1.ogg"
        scene day5_dd_julie_344
        with hpunch
        ja "[r1!u]？！"
        scene black
        with Dissolve(2)
        ja "oh，操……操……MIERDA！"
        scene day5_dd_julie_345
        with Dissolve(2)
        ja "啊，靠……好……好吧……"
        ja "[ja]，你来干什么？你来干什么？！"
        scene black
        with Dissolve(2)
        pause
        scene day5_dd_julie_347
        with Dissolve(2)
        ja "听着，你欠我一次，我需要你帮忙。"
        ja "别跟任何人说话。手上的事全都放下，马上过来。"
        ja "我在旧体育馆。"
        ja "操，我哪知道！快过来！马上！"
        scene black
        with Dissolve(2)
        pause
        "{color=#FF007F}???{/color}" "到底出什么事了？！"
        ja "我完全不知道！"
        "{color=#FF007F}???{/color}" "搞什么，[ja]？！好多血！"
        "{color=#FF007F}???{/color}" "你怎么可能不知道？！"
        ja "他突然就晕过去了！我这边都慌死了！"
        "{color=#FF007F}???{/color}" "[isa]在哪儿？"
        ja "不知道，她今天没来。"
        "{color=#FF007F}???{/color}" "他这样多久了？"
        ja "操，我不知道！"
        ja "你到底帮不帮？！"
        "{color=#FF007F}???{/color}" "靠。好！"
        "{color=#FF007F}???{/color}" "扶住他！过来搭把手。我们得把他抬到浴室去。"
        scene black
        pause 0.2
        scene day5_dd_julie_349
        with Dissolve(2)
        ja "天哪！他好重！"
        "{color=#FF007F}???{/color}" "怎么？以前没抬过尸体？"
        ja "我现在没心情跟你闹！"
        "{color=#FF007F}???{/color}" "那你就冷静点！我不是已经在帮了吗！"
        scene black
        with Dissolve(2)
        pause
        scene day5_dd_julie_350
        with Dissolve(2)
        ja "这血也太多了……"
        "{color=#FF007F}???{/color}" "我觉得只是被我们抹开了。看着并没有比刚才更多血。"
        ja "这种情况下你怎么还能这么冷静？！"
        "{color=#FF007F}???{/color}" "[ja]，深呼吸。我们先看看情况再判断。"
        "{color=#FF007F}???{/color}" "慌也没用。放轻松。"
        scene black
        with Dissolve(2)
        pause
        "{color=#FF007F}???{/color}" "老师？"
        "{color=#FF007F}???{/color}" "你没事吧？"
        ja "他没反应了！"
        scene day5_dd_julie_348
        with Dissolve(2)
        ja "看！他睁眼了！"
        scene black
        with Dissolve(2)
        "{color=#FF007F}???{/color}" "于是我们又回到了原点。"
        scene day5_dd_julie_351
        asu "听着。你只有对我坦诚，我才能帮你。"
        asu "在这里，我是你的朋友，好吗？"
        ja "你在说什么鬼话？！"
        asu "你确定你真不知道发生了什么？"
        scene day5_dd_julie_352
        ja "你他妈在暗示什么，[asu]？！"
        scene day5_dd_julie_351
        asu "再说一遍，我是你的朋友。我什么也没暗示。"
        asu "我只是想知道事情的全貌。"
        asu "我得知道下一步该怎么办。"
        asu "现在告诉我。你到底确不确定？！"
        scene day5_dd_julie_352
        ja "事情是这样，我们刚才在打架。"
        ja "他一直在说话。"
        ja "然后突然就晕过去了。"
        ja "我慌了。"
        ja "我就给你打了电话。"
        ja "就这些。"
        scene day5_dd_julie_351
        asu "明白了。"
        scene day5_dd_julie_353
        asu "我要把他的衣服脱掉。"
        scene day5_dd_julie_354
        with hpunch
        pause
        scene day5_dd_julie_355
        ja "什么？！"
        asu "我得看看是什么情况。"
        asu "如果还在流血，我们得止血，然后叫救护车。"
        scene day5_dd_julie_356
        with Dissolve(2)
        asu "再拖下去也没有意义了。"
        scene day5_dd_julie_357
        with Dissolve(2)
        pause
        scene day5_dd_julie_358
        with Dissolve(1)
        ja "也许我们该叫救护车。"
        asu "你已经叫过我了。"
        asu "如果需要叫别人，我会叫的。"
        asu "这件事上，你得相信我的判断。"
        asu "现在放松点，你让我紧张了。"
        asu "我只是得真的——"
        play sound "audio/dramaticstinger.ogg" volume 0.8
        scene day5_dd_julie_359
        with hpunch
        pause
        scene day5_dd_julie_360
        with hpunch
        asu "啊啊啊啊啊啊啊——！"
        asu "耶稣！基督！的老娘！"
        asu "别这样！"
        scene day5_dd_julie_361
        ja "[r1]？！"
        ja "你没事吧？"
        scene day5_dd_julie_362
        asu "他已经失去意识了！那是条件反射！"
        asu "而且反射得相当准！"
        asu "啧！"
        scene day5_dd_julie_363
        with Dissolve(1)
        ja "你确定？"
        asu "算是吧。"
        scene day5_dd_julie_364
        with Dissolve(1)
        asu "老师？听得见就眨眨眼。"
        scene black
        with dissolve
        pause 0.2
        scene day5_dd_julie_364
        with dissolve
        pause
        scene day5_dd_julie_365
        asu "我有个办法。"
        scene black
        with Dissolve(2)
        pause
        scene day5_dd_julie_366
        with Dissolve(2)
        asu "不管你要做什么，别急着冲过去，好吗？"
        ja "为什么？"
        asu "信我一次。"
        ja "你凭什么觉得我会——"
        scene day5_dd_julie_367
        asu "[ja]，你只要告诉我有没有懂就行。"
        scene day5_dd_julie_368
        ja "懂了。"
        scene day5_dd_julie_367
        asu "很好。"
        scene black
        with Dissolve(2)
        pause 0.2
        scene day5_dd_julie_369
        with Dissolve(2)
        asu "现在我们等一会儿。"
        scene day5_dd_julie_370
        with Dissolve(2)
        pause
        scene day5_dd_julie_371
        with Dissolve(2)
        pause
        scene day5_dd_julie_372
        with Dissolve(2)
        pause
        scene day5_dd_julie_373
        with Dissolve(2)
        pause
        scene day5_dd_julie_374
        with Dissolve(2)
        ja "可能是关掉了吧？"
        asu "再等一下下。"
        scene day5_dd_julie_375
        with Dissolve(1)
        pause
        stop music2
        $ renpy.music.set_volume(1,2,"music2")
        play music3 "audio/shower2.ogg" volume 1.0
        scene day5_dd_julie_376
        pause
        stop music3 fadeout 8
        play music2 "audio/shower.ogg" volume 0.5
        scene day5_dd_julie_377
        pause
        scene day5_dd_julie_378
        with Dissolve(2)
        pause
        scene day5_dd_julie_379
        with Dissolve(2)
        pause
        scene day5_dd_julie_380
        with Dissolve(2)
        asu "嗯。"
        scene day5_dd_julie_381
        ja "你怎么知道那样会有用？！"
        scene day5_dd_julie_380
        with Dissolve(1)
        asu "因为我每次训练昏过去，我父亲就是这么对我的。"
        asu "冷水会让肾上腺素猛涨。"
        asu "能把人激醒。"
        asu "老师，你没事吧？"
        scene day5_dd_julie_382
        with Dissolve(1)
        r1 "这里到底怎么回事？"
        scene day5_dd_julie_380
        with Dissolve(1)
        asu "那我就当你说「是」了。"
        scene day5_dd_julie_383
        with hpunch
        pause
        scene day5_dd_julie_384
        with Dissolve(2)
        r1 "我昏了多久？"
        scene day5_dd_julie_380
        with Dissolve(2)
        asu "嗯。"
        asu "有意思。"
        scene day5_dd_julie_385
        with Dissolve(1)
        asu "我不确定。大概十到二十分钟。"
        asu "考虑到她跟我说的情况。"
        r1 "知道发生什么了吗？"
        asu "我会几个偏方，老师。但我不是医生。我建议你去看一个。"
        r1 "对。"
        asu "你看起来没失太多血。不过还是去检查一下比较好。"
        scene day5_dd_julie_386
        with hpunch
        ja "他居然没失很多血？！"
        ja "你看过隔壁那间屋子了吗？！"
        scene day5_dd_julie_387
        with Dissolve(1)
        asu "人体里的血量多到会让你吃惊。"
        asu "那边连零头都不算。"
        scene day5_dd_julie_388
        with Dissolve(1)
        asu "有人能帮你收拾那边吗？"
        scene day5_dd_julie_389
        with Dissolve(1)
        ja "我来收拾。"
        scene day5_dd_julie_388
        asu "不行。"
        asu "[ju]在等你。我们不想让她过来找你。"
        asu "老师？"
        scene day5_dd_julie_389
        with Dissolve(1)
        r1 "我原本可没打算这样，[asu]。"
        scene day5_dd_julie_388
        asu "那我找人帮你收拾。"
        asu "抱歉，我得打几个电话。"
        scene day5_dd_julie_390
        with Dissolve(1)
        ja "老师，我真的很……非常抱歉！"
        ja "我知道都是我的错。"
        scene day5_dd_julie_391
        with Dissolve(1)
        pause
        scene day5_dd_julie_392
        with Dissolve(1)
        r1 "[ja]，你的衣服。"
        ja "我的衣服？"
        scene day5_dd_julie_393
        with Dissolve(1)
        ja "什么意思？"
        scene day5_dd_julie_395
        with hpunch
        ja "天啊……"
        r1 "你要知道的话，我什么都没看见。"
        scene day5_dd_julie_394
        with Dissolve(1)
        ja "我们……"
        r1 "好吧。"
        scene day5_dd_julie_396
        with Dissolve(1)
        ja "我不是故意伤你的。我有多抱歉，怎么强调都不够。你必须相信我。"
        ja "我知道我当时很火大。我知道我们在打架……但我绝不会真的想伤你。绝不会！"
        r1 "我知道。"
        r1 "而且我也不怪你。"
        ja "你不怪我？"
        r1 "你不可能预知的。"
        r1 "既然都到这儿了，我需要你帮我做件事。"
        ja "什么事？"
        r1 "我得知道我背上的缝线有没有崩开。"
        r1 "你能帮我看看吗？"
        scene day5_dd_julie_397
        with Dissolve(2)
        r1 "有多严重？"
        ja "老师……"
        r1 "那么严重？"
        scene day5_dd_julie_398
        with Dissolve(2)
        ja "不……只是……"
        play sound "audio/dramaticstinger.ogg" volume 0.4
        ja "这是枪伤吗？"
        scene day5_dd_julie_400
        with Dissolve(1)
        r1 "拜托，专心点。在确定之前我不能动。"
        scene day5_dd_julie_398
        with Dissolve(1)
        ja "不，缝线没问题。"
        ja "但伤口裂开了一点。"
        scene day5_dd_julie_400
        with Dissolve(1)
        r1 "还在流血吗？"
        ja "没有。"
        r1 "很好。"
        scene day5_dd_julie_399
        with Dissolve(1)
        r1 "*叹气* 太好了。"
        scene day5_dd_julie_400
        with Dissolve(1)
        r1 "你有个有趣的朋友。"
        scene day5_dd_julie_401
        with Dissolve(1)
        ja "是啊……"
        ja "刚才在里面，你吓到我们了。"
        r1 "我不是故意的。"
        ja "我知道……"
        scene day5_dd_julie_402
        with Dissolve(1)
        r1 "我不想让你看到我这副样子。"
        scene day5_dd_julie_403
        with Dissolve(1)
        ja "那我们就算扯平了。"
        scene day5_dd_julie_401
        with Dissolve(1)
        r1 "嗯。好像是。"
        ja "所以……那真的是枪伤吗？"
        r1 "我要是说不是，你会信吗？"
        ja "我是说……你已经知道我的很多事了。"
        r1 "这跟我刚才问你的问题有什么关系？"
        ja "你现在该知道，我以前{b}见{/b}过枪伤。"
        r1 "是吗？"
        ja "你撞到脑子了吗？你不记得我住在哪了吗？"
        scene day5_dd_julie_402
        with Dissolve(1)
        r1 "那你的意思是，现在我就该知道关于伤口和子弹的一切了？"
        scene day5_dd_julie_403
        with Dissolve(1)
        pause
        scene day5_dd_julie_404
        with Dissolve(1)
        ja "算了。我不是故意要打探。"
        ja "我只是担心你。"
        scene day5_dd_julie_402
        with Dissolve(1)
        pause
        r1 "对不起。"
        scene day5_dd_julie_403
        with Dissolve(1)
        ja "那血真的很多。"
        ja "而我满脑子都是……"
        scene day5_dd_julie_404
        with Dissolve(1)
        ja "……我不想失去你。太吓人了。"
        ja "你晕倒了。到处都是血。我——"
        ja "我从没想过会亲眼看到那种事发生在这么近的地方。"
        ja "我是说……以前也发生过。但发生在你身上……那……"
        ja "操，我不知道……"
        scene day5_dd_julie_402
        with Dissolve(1)
        r1 "嗯。"
        r1 "能把水关掉吗？我想已经够冷了。"
        scene day5_dd_julie_403
        with Dissolve(1)
        ja "哦……对。"
        scene day5_dd_julie_405
        with Dissolve(2)
        pause
        stop music3 fadeout 2
        stop music2 fadeout 2
        scene day5_dd_julie_406
        with Dissolve(2)
        pause
        scene day5_dd_julie_407
        with Dissolve(2)
        ja "你知道吗……我五岁那年……[ju]刚满三岁……"
        ja "我母亲半夜进了我的房间，在我睡着时亲了亲我的额头。"
        scene day5_dd_julie_408
        with Dissolve(2)
        ja "我还记得她的话。「妈妈受不了了。她要走了……」"
        ja "「照顾好[ju]。」"
        ja "「等你长大了，来找我。」"
        ja "我听见了这些话，却不懂其中的意思。"
        scene day5_dd_julie_409
        with Dissolve(2)
        ja "但醒来的时候我就懂了。"
        ja "我一直比所有人都起得早，除了我母亲。"
        ja "我以前会帮她做早饭。"
        ja "每次我醒来，她都已经做了。所以我就帮她搭把手。"
        scene day5_dd_julie_410
        with Dissolve(2)
        ja "但即使只是个孩子，五点醒来、屋子里死一般寂静的那一刻，我也能明白她的意思。没有一点声音……除了那台蠢机器的哔哔声。"
        ja "桌上没有吃的……"
        ja "母亲不在。她没在给我们做早饭。"
        ja "[ju]马上就要醒了。我满脑子只有一个念头……"
        scene day5_dd_julie_411
        with Dissolve(1)
        ja "「妈妈不在，没人给我们做饭，妹妹要吃什么呢？」"
        scene day5_dd_julie_412
        with Dissolve(1)
        pause
        scene day5_dd_julie_413
        with Dissolve(1)
        ja "*叹气*"
        scene day5_dd_julie_414
        with Dissolve(1)
        ja "我摆好桌子。搬了把椅子爬上去。" 
        ja "我连椅子都扶不稳，只能使出全身力气把它推到灶台前。"
        ja "我做了[ju]最爱的早餐。把小刀插进面包卷里，就着炉火烤。"
        ja "她最喜欢烤得脆脆的。"
        scene day5_dd_julie_415
        with Dissolve(1)
        ja "找不到做果汁的材料。所以我只把牛奶放在桌上。" 
        ja "父亲醒了。"
        ja "他看见了那张桌子。"
        scene day5_dd_julie_416
        with Dissolve(1)
        ja "然后他把厨房里所有东西都摔到了地上。"
        ja "问我母亲在哪。我不知道。"
        ja "他发火了，开始砸厨房里的一切。"
        ja "我吓坏了，开始哭。"
        ja "哦天。他更火了……"
        ja "叫我别哭了，否则就让我有真正该哭的理由。"
        ja "我看见我做的一切……散落在满地的碎玻璃和洒出来的牛奶中间。"
        ja "我饿着，肚子也疼。我确实想过把它吃掉。"
        scene day5_dd_julie_417
        with Dissolve(1)
        ja "然后我看到，就在那儿，我烤的第一个面包卷。我本来以为已经烤坏了。不打算端给他们。"
        ja "不，我留着以后吃。留给我自己。"
        scene day5_dd_julie_418
        with Dissolve(1)
        ja "我一把抓起它，跑到[ju]床边。"
        ja "「姐，我给你做了这个。你说说味道怎么样？」我这么跟她说。"
        scene day5_dd_julie_419
        with Dissolve(1)
        ja "她睁开眼时，那是我见过最典型的「我还想再睡五分钟」的眼神。"
        scene day5_dd_julie_420
        with Dissolve(1)
        ja "她说的第一句话是，「你的呢？」"
        ja "「我没有。」我说。"
        ja "「那我们分着吃吧。」她说。"
        ja "在这样一个糟透了的早晨之后，我就在那一刻意识到，我拥有的只有我的妹妹。她对发生的一切都毫无察觉。"
        ja "那份纯真之下……她第一个想到的人是我。"
        ja "我只有我的妹妹。"
        ja "而她也只有我。"
        scene day5_dd_julie_421
        with Dissolve(1)
        ja "什么样的母亲会抛弃自己的孩子？"
        ja "什么样的父亲会这样对待自己的女儿？"
        scene day5_dd_julie_422
        with Dissolve(2)
        ja "真奇怪，都过去十多年了，感觉却还像昨天。"
        ja "那天的事我一件都没忘。"
        scene day5_dd_julie_424
        with Dissolve(1)
        pause
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "啊，该死……"
        r1 "你为什么要跟我说这些？"
        play sound "audio/clenching.ogg"
        scene day5_dd_julie_425
        ja "因为我想让你明白我当时为什么会那么生气。"
        scene day5_dd_julie_426
        with Dissolve(2)
        pause
        ja "我八岁那年打扫房子时，发现了妈妈的日记本。"
        scene day5_dd_julie_428
        with Dissolve(1)
        ja "Santo Dios，我那时候可喜欢读书了。"
        ja "我只是个想更了解自己母亲的孩子。"
        ja "我扔下扫帚，把能找到的关于她的一切都读了一遍。"
        scene day5_dd_julie_427
        with Dissolve(1)
        ja "爸爸在那里发现了我。他从我手里夺过日记本，甩到墙上。"
        ja "他用手背狠狠抽了我嘴巴一下，我差点昏过去。"
        ja "还告诉我永远不许再碰妈妈的东西。"
        scene day5_dd_julie_429
        with Dissolve(1)
        ja "这辈子除了必读的书，我再没读过第二本。"
        scene day5_dd_julie_430
        with Dissolve(1)
        ja "我过早地就不再是个孩子了。"
        scene day5_dd_julie_424
        with Dissolve(1)
        pause
        scene day5_dd_julie_423
        with Dissolve(1)
        pause
        r1 "人生对思考者而言是喜剧，对感受者而言是悲剧。"
        scene day5_dd_julie_430
        with Dissolve(1)
        ja "说它是噩梦都算轻描淡写了。"
        ja "你知道吗……我从没想过会有人在乎我们。一直是我们在对抗整个世界。"
        ja "而且一直都是这样。"
        ja "我学会了这样活着。"
        ja "不信任任何人。"
        ja "讨厌任何试图对我表示亲近的人。因为我明知道那全是假的。没人真的在乎我。"
        ja "人们只在对他们方便的时候才喜欢我。"
        scene day5_dd_julie_431
        with Dissolve(1)
        ja "然后你出现了。"
        ja "一个彻底的陌生人，因为一个支离破碎的女孩而让自己身陷险境。"
        ja "在我除了是个麻烦之外一无是处的时候，你却在我身边。"
        ja "是你让我开始相信，这世上除了姐姐之外，还有另一个人属于我。"
        ja "一个真的愿意在这个世界上做点好事的人。"
        ja "当我看到你和那个男人在一起，我感觉自己的希望又一次被碾得粉碎。"
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "我不是那种人。"
        r1 "我只是在做我的工作。"
        scene day5_dd_julie_431
        with Dissolve(1)
        pause
        scene day5_dd_julie_430
        with Dissolve(1)
        pause
        ja "混、蛋。"
        scene day5_dd_julie_424
        with Dissolve(1)
        r1 "你说什么？"
        scene day5_dd_julie_431
        ja "不！我才不会！"
        ja "你必须听我说。现在，我不再是你的学生了。"
        ja "别再拿「我只是在工作」这种鬼话糊弄我。你根本不是！"
        scene day5_dd_julie_430
        ja "¡Dios mío！你真是……"
        scene day5_dd_julie_432
        with Dissolve(1)
        ja "呃啊！"
        scene day5_dd_julie_430
        with Dissolve(2)
        pause
        ja "告诉我实话。我真的就那么不值一提吗？"
        ja "你……你一直在做的那些事……"
        ja "换成别人，你也会去做你做的那些事吗？对我来说，你是不是除了工作什么都不剩？"
        scene day5_dd_julie_424
        with Dissolve(1)
        pause
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "你真想听的话，我在你身上看见过无数次自己的影子。"
        r1 "你保护那些对你忠诚的人的样子。"
        r1 "你真心在乎自己人的样子。"
        r1 "让我想起我像你这么大时的样子。"
        scene day5_dd_julie_424
        with Dissolve(1)
        r1 "还有你有时控制不住自己怒火的样子。"
        scene day5_dd_julie_431
        with Dissolve(1)
        ja "你也会那样？"
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "要是你知道我做过的那些事的一半、感受过的情绪的一半就好了。"
        r1 "过得像坨屎一样的人生可不是只有你被诅咒，[ja]。"
        scene day5_dd_julie_430
        with Dissolve(1)
        ja "我知道别人的人生也遭受过痛苦。但这不会让我的痛苦减轻一分。"
        scene day5_dd_julie_424
        with Dissolve(1)
        r1 "确实不会。"
        r1 "但那也不是你冲别人发火的借口。"
        r1 "要么掌控你的情绪，要么被它们支配。"
        scene day5_dd_julie_430
        with Dissolve(1)
        ja "我觉得我什么都不在乎了。"
        scene day5_dd_julie_424
        with Dissolve(1)
        r1 "等到受伤的人变成你姐姐，你就不会这么想了。"
        scene day5_dd_julie_430
        with Dissolve(1)
        pause
        scene day5_dd_julie_433
        with Dissolve(1)
        ju "我绝不会——"
        scene day5_dd_julie_424
        r1 "你不会？！"
        r1 "你想想，要是因为这些事你被开除了会怎样？"
        r1 "你觉得她因此会更开心吗？"
        r1 "觉得一个人来这里会更好吗？"
        r1 "觉得她会更安全吗？"
        r1 "或者更糟。倘若我是另一种人呢？倘若我不只是让你退学，还对你提起诉讼呢。"
        r1 "要是你进了监狱，你姐姐会是什么感受？"
        r1 "通往地狱的路是由良好愿望铺成的。"
        r1 "你不能只是「打算」不去伤害你在乎的人，你必须真的「做到」。"
        r1 "否则你一定会出事。"
        scene day5_dd_julie_433
        with Dissolve(1)
        pause
        scene day5_dd_julie_424
        with Dissolve(1)
        pause
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "是。"
        scene day5_dd_julie_433
        with Dissolve(1)
        ja "是吗？"
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "是枪伤。"
        play sound "audio/open5.ogg"
        scene day5_dd_julie_434
        asu "好。接下来会这样处理。"
        scene day5_dd_julie_435
        with Dissolve(2)
        asu "今天发生的事，我们「永远」不会再对任何人提起。"
        asu "不告诉[ju]。不告诉[lila]。不告诉任何人。"
        scene day5_dd_julie_436
        with Dissolve(1)
        asu "会有人来把这里的垫子清理干净。"
        asu "那您呢，先生？需要接受治疗吗？"
        asu "要我带您去看医生吗？"
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "我没事。就是有点晕。"
        r1 "没什么我扛不住的。"
        scene day5_dd_julie_436
        with Dissolve(1)
        asu "您确定吗？我也可以安排人送您回家。"
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "我确定。"
        scene day5_dd_julie_436
        with Dissolve(1)
        pause
        scene day5_dd_julie_438
        asu "太好了！你们刚才在聊什么？"
        scene day5_dd_julie_439
        ja "这次没偷听？"
        scene day5_dd_julie_440
        asu "这话可是叛国啊！"
        asu "我——是你的朋友！"
        scene day5_dd_julie_424
        with Dissolve(1)
        r1 "你自己还不是一样。"
        scene day5_dd_julie_441
        with Dissolve(1)
        ja "我……知道……"
        scene day5_dd_julie_440
        asu "我感觉自己被接纳了呢！"
        asu "我最爱秘密了！"
        scene day5_dd_julie_442
        with Dissolve(1)
        ja "我搞砸了点事。"
        scene day5_dd_julie_438
        asu "一点点？"
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "坐下，[asu]。"
        r1 "我想和你们两个谈谈。"
        scene day5_dd_julie_443
        with Dissolve(1)
        asu "哦？"
        scene day5_dd_julie_444
        with Dissolve(1)
        asu "那肯定很有意思。"
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "是关于你昨天告诉我的事。"
        scene day5_dd_julie_445
        with Dissolve(1)
        asu "昨——？"
        scene day5_dd_julie_446
        with Dissolve(2)
        pause
        asu "你敢。"
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "我需要[ja]明白一件事。"
        scene day5_dd_julie_446
        with Dissolve(1)
        pause
        scene day5_dd_julie_447
        with Dissolve(1)
        pause
        scene day5_dd_julie_448
        with Dissolve(1)
        ja "怎么了？"
        scene day5_dd_julie_423
        with Dissolve(1)
        pause
        scene day5_dd_julie_424
        with Dissolve(1)
        r1 "[asu]告诉我，你姐姐是她最好的朋友之一。"
        r1 "还说你姐姐有多在乎她。"
        scene day5_dd_julie_449
        with Dissolve(1)
        ja "等等……真的假的？"
        scene day5_dd_julie_450
        with Dissolve(1)
        ja "太温馨了。"
        scene day5_dd_julie_446
        with Dissolve(1)
        pause
        scene day5_dd_julie_451
        with Dissolve(1)
        asu "我能说什么呢？我对书呆子没什么抵抗力。"
        scene day5_dd_julie_450
        with Dissolve(1)
        ja "是啊，她就是个彻头彻尾的书呆子。"
        scene day5_dd_julie_451
        with Dissolve(1)
        asu "但那是我们的书呆子。"
        scene day5_dd_julie_450
        with Dissolve(1)
        ja "顺带一提，她更是我的人。"
        scene day5_dd_julie_449
        with Dissolve(1)
        ja "我到底要明白什么？"
        scene day5_dd_julie_424
        with Dissolve(1)
        r1 "你和你姐姐不再孤单了。"
        r1 "其实早就不是了。"
        r1 "你有我。你有[asu]。"
        r1 "我不想让你从今以后再有别的想法。"
        scene day5_dd_julie_451
        with Dissolve(1)
        asu "你在开玩笑吗？"
        asu "你就这么想？"
        asu "姑娘，我和别的姑娘们都站在你这边，这点我敢保证。"
        scene day5_dd_julie_447
        with Dissolve(1)
        pause
        scene day5_dd_julie_448
        with Dissolve(1)
        pause
        scene day5_dd_julie_452
        with Dissolve(1)
        ja "谢谢大家……"
        scene day5_dd_julie_451
        with Dissolve(1)
        asu "听着，我得准备上班了。"
        asu "这事改天再聊，行吗？"
        scene day5_dd_julie_452
        with Dissolve(1)
        ja "我没事。谢谢。"
        scene day5_dd_julie_451
        with Dissolve(1)
        asu "太好了！"
        scene day5_dd_julie_443
        with Dissolve(1)
        asu "那么……走吧？"
        scene day5_dd_julie_423
        with Dissolve(1)
        r1 "好。给我几分钟。"
        stop music fadeout 3
        play sound "audio/Lockpick_Success.ogg" volume 0.1
        $ biopage["jas"] = 3
        show screen notifyEx( msg="[ja]的{color=#00ff00}人物档案{/color}已被{color=#00ff00}更新{/color}！" )
        scene black
        with Dissolve(2)
        pause
        hide notifyEx with dissolve
        scene day5_dd_julie_453
        with Dissolve(3)
        asu "别再这样了。"
        scene day5_dd_julie_454
        with Dissolve(1)
        r1 "嗯？做什么？"
        scene day5_dd_julie_453
        with Dissolve(1)
        asu "威胁我。"
        scene day5_dd_julie_454
        with Dissolve(1)
        r1 "威胁你？"
        scene day5_dd_julie_455
        with Dissolve(1)
        asu "我知道这套玩法。"
        asu "我在这里不是你的敌人。我不喜欢被人威胁。所以，请别再这样了。"
        scene day5_dd_julie_454
        with Dissolve(1)
        r1 "你什么意思？"
        scene day5_dd_julie_456
        with Dissolve(1)
        asu "别跟我装傻。"
        asu "你知道我们说的是什么。"
        scene day5_dd_julie_454
        with Dissolve(1)
        r1 "完全听不懂，[asu]。"
        scene day5_dd_julie_457
        with Dissolve(2)
        pause
        scene day5_dd_julie_458
        with Dissolve(2)
        pause
        scene day5_dd_julie_459
        with Dissolve(1)
        pause
        r1 "说真的，解释一下。"
        r1 "我没有威胁你。"
        scene day5_dd_julie_458
        with Dissolve(1)
        asu "那你可得换个更好的说法来表达你的意思。"
        asu "因为听起来像是在提醒我昨天那场对话。"
        asu "那场我说过「绝对不许离开你办公室」的对话。"
        scene day5_dd_julie_454
        with Dissolve(1)
        r1 "我是另有用意。"
        scene day5_dd_julie_458
        with Dissolve(2)
        asu "我洗耳恭听。"
        scene day5_dd_julie_454
        with Dissolve(1)
        r1 "先回答我一个问题。你觉得我的意思到底是什么？"
        scene day5_dd_julie_460
        with Dissolve(2)
        pause
        asu "先生，这里是个人们口是心非、言不达意的地方。"
        asu "如果您不是在威胁我，那我建议——"
        scene day5_dd_julie_461
        with Dissolve(1)
        asu "*叹气*"
        scene day5_dd_julie_462
        with Dissolve(1)
        asu "只是一场误会，对吧？"
        scene day5_dd_julie_454
        with Dissolve(1)
        r1 "是。"
        scene day5_dd_julie_462
        with Dissolve(1)
        asu "好。"
        scene day5_dd_julie_454
        with Dissolve(1)
        r1 "不是关于我们。是关于你的朋友。"
        scene day5_dd_julie_460
        with Dissolve(1)
        asu "[ju]？"
        scene day5_dd_julie_459
        with Dissolve(1)
        r1 "[ja]。"
        r1 "我想请你帮我做件事。"
        r1 "准确地说，是为了她。"
        scene day5_dd_julie_460
        with Dissolve(1)
        asu "嗯？"
        scene day5_dd_julie_459
        with Dissolve(1)
        r1 "帮我盯紧她。"
        r1 "她现在有点不稳定。"
        scene day5_dd_julie_460
        with Dissolve(1)
        pause
        asu "你不用这么——"
        scene day5_dd_julie_463
        with Dissolve(1)
        asu "哦？有意思。"
        scene day5_dd_julie_459
        with Dissolve(1)
        r1 "什么有意思？"
        scene day5_dd_julie_463
        with Dissolve(1)
        asu "你在乎她。"
        scene day5_dd_julie_459
        with Dissolve(1)
        r1 "你不是吗？她是你朋友。"
        scene day5_dd_julie_463
        with Dissolve(1)
        asu "当然。不过我很好奇，她对你来说算是「什么」。"
        asu "你的学生？你的朋友？"
        scene day5_dd_julie_459
        with Dissolve(1)
        r1 "两者不能兼是吗？"
        scene day5_dd_julie_463
        with Dissolve(1)
        asu "我可不知道你还会跟自己的学生交朋友。"
        scene day5_dd_julie_459
        with Dissolve(1)
        r1 "如果拉近关系能增强校长和学生之间的信任，那何乐而不为？"
        r1 "离学生近一些，才更容易真正了解学生的生活。"
        scene day5_dd_julie_463
        with Dissolve(1)
        pause
        scene day5_dd_julie_464
        with Dissolve(1)
        asu "确实。"
        asu "我在想，您在这方面的过往经历是否造就了这份洞察。"
        scene day5_dd_julie_459
        with Dissolve(1)
        r1 "也许我只是聪明。"
        scene day5_dd_julie_464
        with Dissolve(1)
        asu "希望如此。"
        scene day5_dd_julie_465
        with Dissolve(1)
        asu "聪明的头脑可比学来的把戏有意思多了，您说呢？"
        scene day5_dd_julie_466
        with Dissolve(1)
        pause
        scene day5_dd_julie_467
        r1 "你在耍我吗？"
        scene day5_dd_julie_465
        with Dissolve(1)
        asu "我可不会。您是男人，而男人不玩花样。"
        scene day5_dd_julie_467
        with Dissolve(1)
        r1 "那你也算男人？"
        scene day5_dd_julie_469
        with Dissolve(1)
        asu "那样事情就简单多了。"
        scene day5_dd_julie_470
        with Dissolve(1)
        asu "不过现实往往令人失望。"
        scene day5_dd_julie_468
        with Dissolve(1)
        r1 "你真有人来打扫这里吗？"
        scene day5_dd_julie_471
        with Dissolve(2)
        pause
        scene day5_dd_julie_472
        with Dissolve(1)
        asu "当然有。"
        asu "难的不是找到愿意打扫的人。"
        scene day5_dd_julie_471
        with Dissolve(1)
        asu "难的是找到能管住自己嘴的人。"
        asu "幸好我手头确实有这样的人。"
        scene day5_dd_julie_468
        with Dissolve(1)
        r1 "嗯。"
        scene day5_dd_julie_473
        with Dissolve(1)
        ja "看来我暂时得一直穿着这条短裤了。"
        scene day5_dd_julie_474
        with Dissolve(1)
        asu "我不知道。这样倒也有它的魅力。"
        scene day5_dd_julie_475
        with Dissolve(1)
        ja "是啊。真幽默。"
        scene day5_dd_julie_476
        with Dissolve(1)
        ja "真没想到你还在这儿存了换洗衣服。"
        scene day5_dd_julie_477
        with Dissolve(1)
        r1 "我想着既然我们要经常在这里训练，总得有几件换洗的衣服。"
        r1 "你懂的，以防万一。我是从仓库拿的。"
        r1 "幸好我猜对了。"
        scene day5_dd_julie_476
        with Dissolve(1)
        ja "真机灵。谢谢。"
        scene day5_dd_julie_477
        with Dissolve(1)
        r1 "我只是不确定有没有拿对你的尺码。"
        scene day5_dd_julie_478
        with Dissolve(1)
        ja "怎么说呢，短了那么几号。不过凑合穿吧。"
        ja "反正也比穿着湿衣服在校园里跑步强太多了。"
        scene day5_dd_julie_479
        with Dissolve(1)
        asu "等等。你们在用这个地方？"
        asu "用来训练？就你们两个？"
        scene day5_dd_julie_480
        with Dissolve(1)
        ja "我们刚才只是……我是说，我们——"
        scene day5_dd_julie_481
        asu "打住。下次你要是不「邀请」我，这事就没完。"
        scene day5_dd_julie_482
        with Dissolve(1)
        asu "你知道关于这个地方我听过多少故事吗？"
        scene day5_dd_julie_483
        with Dissolve(1)
        asu "我听说大学里的竞技体育有多激烈时，整个人都惊了。"
        asu "我兴奋得不行，迫不及待想来接受挑战。"
        asu "可轮到我来的时候，这地方居然荒得长满了苍蝇！你想想我有多意外！"
        asu "泳池脏得不行。这地方本身没问题，但基本被废弃了。有个篮球场和排球场，仅此而已。"
        asu "如果你们要在这儿训练，我也要加入。"
        scene day5_dd_julie_484
        with Dissolve(1)
        ja "我不知道……这原本是我和……就是我们两个人的事……我觉得我们不太——"
        scene day5_dd_julie_477
        r1 "我觉得这主意不错。"
        scene day5_dd_julie_485
        ja "什么？！"
        scene day5_dd_julie_477
        r1 "毕竟我不想再到处流血了。"
        r1 "我显然得停一段时间。"
        r1 "而我也不想让你停止训练。"
        scene day5_dd_julie_468
        with Dissolve(1)
        r1 "而且这对[asu]也有好处，对吧？"
        scene day5_dd_julie_469
        with Dissolve(1)
        asu "是是是，长官。这对[asu]有好处。"
        scene day5_dd_julie_467
        r1 "我说过别再这么叫了。"
        scene day5_dd_julie_486
        asu "是，长官！"
        scene day5_dd_julie_467
        pause
        scene day5_dd_julie_487
        with Dissolve(1)
        asu "抱歉……"
        scene day5_dd_julie_488
        with Dissolve(1)
        ja "那个……欢迎来到……搏击俱乐部？"
        scene day5_dd_julie_490
        asu "A—达—达—达！"
        asu "规则一：不许提起！"
        scene day5_dd_julie_478
        with Dissolve(1)
        ja "认真的？你居然真用了这个梗？"
        ja "你知道那个梗都老掉牙了吗？"
        scene day5_dd_julie_490
        asu "姑娘，对经典要有敬畏之心！"
        scene day5_dd_julie_491
        with Dissolve(1)
        r1 "好了，我们得走了。"
        r1 "这事改天再谈。"
        scene day5_dd_julie_492
        with Dissolve(1)
        asu "我得在这儿等到我的人到。不过你们先走吧。"
        scene day5_dd_julie_493
        with Dissolve(1)
        r1 "再次谢谢你。"
        scene day5_dd_julie_492
        with Dissolve(1)
        asu "不客气。有我在呢。"
        scene day5_dd_julie_494
        with Dissolve(1)
        r1 "好了，走吧。"
        ja "谢谢，[asu]。"
        scene day5_dd_julie_495
        with Dissolve(1)
        asu "小心脚下！"
        ja "哈！"
        scene day5_dd_julie_496
        with Dissolve(2)
        pause
        scene day5_dd_julie_497
        with Dissolve(2)
        pause
        scene day5_dd_julie_498
        with Dissolve(2)
        pause
        scene black
        with Dissolve(3)
        pause
        
        
        
        
    label day5_homesweethome:
        scene day5_homesweethome_1
        with Dissolve(2)
        isa "你能相信我上医学院之后就没做过一次美甲吗？"
        scene day5_homesweethome_2
        with Dissolve(1)
        sophia "你以为我就做了？"
        sophia "我们戴手套的时候指甲根本长不了。"
        sophia "天哪，我现在连指纹都快没了。"
        scene day5_homesweethome_3
        with Dissolve(1)
        isa "啊，别提了！我现在连手机都解不了锁！"
        isa "而且手上沾化学物品本来就不专业。"
        scene day5_homesweethome_4
        with Dissolve(1)
        isa "不过真的特别好看！"
        isa "全靠你，[ava]！"
        scene day5_homesweethome_5
        with Dissolve(1)
        ava "女人漂亮，心情就好。"
        ava "你今天看起来很低落。我说了做了会让你好受点的。"
        scene day5_homesweethome_4
        with Dissolve(1)
        isa "确实！不过其实不只是这个……"
        isa "我只是很高兴我们能这样闺蜜一下。"
        isa "我好怀念这样。"
        scene day5_homesweethome_6
        with Dissolve(1)
        ava "你那些朋友呢？"
        scene day5_homesweethome_7
        with Dissolve(1)
        isa "我……不想扫了大家的兴。"
        isa "我在这座城市从来没花多少时间认识人。"
        isa "除了我的同事[l]，也就没了。"
        isa "她忙得不可开交，根本没空出来玩。"
        scene day5_homesweethome_2
        with Dissolve(1)
        sophia "啊，糟了。我刚来这座城市时完全格格不入。"
        sophia "但我最后还是找到了办法。我相信你也能。"
        scene day5_homesweethome_9
        with Dissolve(1)
        isa "我想我已经找到了。"
        scene day5_homesweethome_10
        with Dissolve(1)
        pause 0.1
        scene day5_homesweethome_11
        with dissolve
        pause 0.1
        scene day5_homesweethome_10
        with Dissolve(1)
        pause
        play sound "audio/open4.ogg"
        scene day5_homesweethome_12
        pause
        scene day5_homesweethome_2
        with Dissolve(1)
        sophia "嘿，亲爱的！"
        scene day5_homesweethome_13
        with Dissolve(1)
        isa "嘿，先生！今天过得怎么样？"
        scene day5_homesweethome_14
        with Dissolve(1)
        r1 "我需要威士忌。"
        scene day5_homesweethome_15
        with Dissolve(1)
        pause
        scene day5_homesweethome_16
        with Dissolve(1)
        ava "我应该能弄到。"
        scene day5_homesweethome_17
        pause
        scene day5_homesweethome_18
        with Dissolve(1)
        pause
        scene day5_homesweethome_19
        with Dissolve(1)
        pause
        scene day5_homesweethome_20
        with Dissolve(1)
        sophia "亲爱的，怎么了？"
        scene day5_homesweethome_21
        with Dissolve(1)
        r1 "没什么。我只想喝一杯。"
        r1 "我想安静一会儿，再休息一下。"
        r1 "我就不能回到家喝上一杯威士忌然后睡觉吗？"
        scene day5_homesweethome_22
        with Dissolve(1)
        pause
        scene day5_homesweethome_23
        sophia "当然可以！大家今晚都喝个痛快！"
        sophia "我给你包扎差点没累死的好吗！"
        sophia "通宵做手术、差点把自己累死，谁在乎啊，对吧？！"
        scene day5_homesweethome_24
        with Dissolve(1)
        sophia "我们就痛痛快快地喝个够！"
        sophia "我去拿苏格兰威士忌！大家一起喝！"
        sophia "再说了光担心你的伤我就快疯了！"
        scene day5_homesweethome_25
        with Dissolve(1)
        pause
        scene day5_homesweethome_26
        with Dissolve(1)
        pause
        scene day5_homesweethome_27
        r1 "够了！停下！"
        scene day5_homesweethome_28
        with Dissolve(1)
        r1 "你有没有想过，有时候我只是工作累了？"
        r1 "我只想回到家，不想听任何事？"
        r1 "我只想安静待着，喝一杯，休息一下，恢复点精力？"
        scene day5_homesweethome_29
        with Dissolve(1)
        r1 "不是所有事都得说出来，你知道吧？"
        scene day5_homesweethome_30
        with Dissolve(1)
        sophia "哦？原来是这样啊？"
        scene day5_homesweethome_31
        with Dissolve(1)
        sophia "抱歉啦！我不过是一整天都在担心你嘛！"
        sophia "好吧我们都担心了！但那其实不重要！"
        sophia "真正重要的是喝你的酒，然后今晚剩下的时间都别理我们！"
        sophia "我们明明看得出你不对劲，问你一句，得到的却是「让我安静一下、放松一下好吗？」"
        scene day5_homesweethome_32
        with Dissolve(1)
        sophia "那当然没问题！让我来给你倒酒！"
        scene day5_homesweethome_33
        with Dissolve(1)
        pause
        scene day5_homesweethome_34
        with Dissolve(1)
        isa "也许我该走了……"
        scene day5_homesweethome_35
        r1 "留下。"
        scene day5_homesweethome_36
        with Dissolve(1)
        pause
        r1 "你真想听的话，是这样。"
        r1 "我一整天都在疼，光是这样就快让我崩溃了。"
        r1 "我有些并发症，到处都在流血，我想我是因为失血过多才昏过去的。"
        scene day5_homesweethome_37
        with hpunch
        "{color=#FF007F}[isa] 和 [sophia]{/color}" "什么？！"
        scene day5_homesweethome_38
        ava "所以你才没接电话？"
        scene day5_homesweethome_36
        r1 "手机没电了。"
        scene day5_homesweethome_39
        sophia "你是什么时候昏过去的？！"
        scene day5_homesweethome_40
        isa "昏了多久？！"
        sophia "这种事你得告诉我们！"
        scene day5_homesweethome_33
        with Dissolve(1)
        r1 "我手机没电了，刚说过了。"
        r1 "就算不是，我也没法联系你们任何人。"
        r1 "听着。我不是要把责任推给你们任何一位，好吗？让我先说完。"
        scene day5_homesweethome_36
        with Dissolve(1)
        r1 "发生了一场「斗殴」。"
        r1 "别问细节。本来不该变成那样的。"
        r1 "我撞到了后背，当时甚至都没察觉。"
        scene day5_homesweethome_41
        with Dissolve(1)
        sophia "大概是肾上腺素的关系。你的注意力全在别处，根本没注意到自己受伤了。"
        scene day5_homesweethome_36
        with Dissolve(1)
        r1 "也许吧。总之，我一路流血流到昏过去。"
        r1 "但我没事。"
        scene day5_homesweethome_43
        with Dissolve(1)
        isa "嗯，看来不是低血容量性休克。"
        sophia "要是那样，他就不会在这儿了。"
        scene day5_homesweethome_42
        with Dissolve(1)
        isa "那晕厥呢？"
        sophia "很有可能。"
        scene day5_homesweethome_44
        with Dissolve(1)
        isa "你是怎么恢复的？"
        scene day5_homesweethome_36
        with Dissolve(1)
        r1 "他们把我扔进浴室，打开了冷水。"
        scene day5_homesweethome_44
        with Dissolve(1)
        isa "聪明。"
        scene day5_homesweethome_42
        with Dissolve(1)
        sophia "体温骤变导致血管收缩。"
        isa "于是血压上升，肾上腺素飙升。"
        sophia "那么肯定是晕厥。"
        scene day5_homesweethome_45
        with Dissolve(1)
        ava "呃……在吗？"
        ava "你们能说人话吗？"
        scene day5_homesweethome_46
        with Dissolve(1)
        sophia "抱歉，亲爱的。我们是说，他的血压下降了。"
        isa "那可能就会让他晕过去。"
        scene day5_homesweethome_47
        with Dissolve(1)
        ava "他没事吧？"
        scene day5_homesweethome_46
        with Dissolve(1)
        isa "他应该没事。这种情况休息一下、多补充水分就够了。穿弹力袜也有帮助。"
        scene day5_homesweethome_47
        with Dissolve(1)
        ava "好……好……"
        ava "太好了……"
        scene day5_homesweethome_48
        ava "你们为什么打架？"
        ava "跟{b}谁{/b}打的？！"
        scene day5_homesweethome_36
        with Dissolve(1)
        r1 "不重要。是意外。"
        r1 "最后一根稻草是[k]来找我提要求。"
        scene day5_homesweethome_49
        with Dissolve(1)
        isa "谁？"
        scene day5_homesweethome_50
        with Dissolve(1)
        sophia "亲爱的，[k]他……"
        scene day5_homesweethome_36
        r1 "够了。我不会在[isa]面前谈这个。"
        r1 "她今天过得很辛苦。我{b}也是{/b}。"
        r1 "工作上有冲突。家里有压力。这两样我今天都受够了。"
        scene day5_homesweethome_51
        with Dissolve(1)
        r1 "如果现在我已经满足了你想知道消息的欲望——如果我不算个不懂体谅的混蛋——那我要去洗个澡。冷水澡。"
        play sound "audio/hitwood1.ogg"
        scene day5_homesweethome_52
        with hpunch
        pause
        scene day5_homesweethome_53
        with Dissolve(2)
        pause
        scene day5_homesweethome_54
        with Dissolve(2)
        pause
    label day5_ava_sex:
        scene day5_homesweethome_55
        with Dissolve(2)
        ava "我去跟他谈谈。"
        play sound "audio/open5.ogg"
        scene day5_homesweethome_56
        with Dissolve(2)
        pause
        play sound "audio/open4.ogg"
        scene day5_homesweethome_57
        with Dissolve(2)
        sophia "我需要你的帮助。"
        scene black
        with Dissolve(2)
        pause
        scene day5_homesweethome_58
        with Dissolve(2)
        pause
        play sound "audio/slidedoorclose1.ogg"
        scene day5_homesweethome_59
        with Dissolve(2)
        pause
        scene day5_homesweethome_60
        with Dissolve(2)
        pause
        scene day5_homesweethome_61
        with Dissolve(2)
        pause
        scene day5_homesweethome_59
        with Dissolve(2)
        pause
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "*咂* 别那样看我。"
        scene day5_homesweethome_61
        with Dissolve(1)
        ava "你们俩一吵架我就讨厌死了。"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "我也是。"
        scene day5_homesweethome_61
        with Dissolve(1)
        pause
        scene day5_homesweethome_62
        with Dissolve(1)
        ava "你知道她不是想让你们俩吵架的，对吧？"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "她就是。"
        r1 "但我也知道她不是。"
        r1 "我们最近压力都很大。这会让我们做出蠢事。"
        r1 "我们俩都不想吵。可还是吵了。"
        scene day5_homesweethome_62
        with Dissolve(1)
        ava "她一整天都在跟[isa]说有多担心你。"
        ava "[isa]好不容易才让她冷静下来。"
        ava "我觉得她觉得自己正在失去掌控。"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "我……正在失去掌控。"
        r1 "很久以来一直如此……"
        scene day5_homesweethome_62
        with Dissolve(1)
        ava "我是说……你差点死了……"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "我知道。"
        scene day5_homesweethome_62
        with Dissolve(1)
        ava "也许是时候告诉她实情了？"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "我不能。"
        scene day5_homesweethome_62
        with Dissolve(1)
        ava "为什么不能？"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "我就是不能，[ava]。求你别逼我重复。"
        scene day5_homesweethome_62
        with Dissolve(2)
        pause
        scene day5_homesweethome_63
        with Dissolve(2)
        pause
        scene day5_homesweethome_64
        with Dissolve(2)
        pause
        scene day5_homesweethome_65
        with Dissolve(2)
        pause
        scene day5_homesweethome_66
        with Dissolve(2)
        pause
        scene day5_homesweethome_67
        with Dissolve(2)
        pause
        scene day5_homesweethome_68
        with Dissolve(2)
        ava "天啊！怎么这么冷？！"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "我不知道你要来。"
        scene day5_homesweethome_68
        with Dissolve(1)
        ava "没关系！只是……呃！"
        scene day5_homesweethome_69
        with Dissolve(2)
        ava "听着……我知道我们最近经历了很多，但别生她的气。"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "我没有。"
        r1 "我们都是成年人了，[ava]。我们可以吵架而不往心里去。"
        scene day5_homesweethome_69
        with Dissolve(1)
        ava "我知道……可每次看到你们俩吵架……"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "我告诉你。就算我们在吵架，我对她有多珍视，心里毫无疑问半分。"
        r1 "而且我敢肯定她也一样。"
        scene day5_homesweethome_69
        with Dissolve(1)
        ava "那为什么还要吵呢……？"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "恋人偶尔也会吵架。这不代表我们不相爱。"
        scene day5_homesweethome_69
        with Dissolve(1)
        ava "我知道……但是……"
        ava "真的有必要吗？"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "有时候确实有。"
        r1 "有时候吵一架反而是健康的。"
        r1 "听着，两个人住在一起，不可能一点冲突都没有。"
        r1 "这就是我们本来的样子。我们有时会意见不合。"
        r1 "说到底，我们连自己都会跟自己作对。又怎么可能跟别人不吵？"
        scene day5_homesweethome_70
        with Dissolve(1)
        ava "亲爱的……我不是那个意思。"
        scene day5_homesweethome_58
        with Dissolve(1)
        r1 "那你倒是说说清楚。"
        scene day5_homesweethome_70
        with Dissolve(1)
        pause
        scene day5_homesweethome_71
        with Dissolve(1)
        ava "你知道你每次出门，我们有多害怕吗？"
        ava "每天早上你去上班……我们都不知道你还能不能回家……"
        ava "你什么都不跟我们说……"
        ava "我们不是想控制你……我们只是害怕！"
        ava "只要你……让我们参与进来，就不会有争吵了！"
        scene day5_homesweethome_72
        with Dissolve(1)
        r1 "啊，靠……"
        scene day5_homesweethome_73
        with Dissolve(1)
        r1 "我知道……听着……"
        r1 "我不觉得你想控制我。"
        r1 "有些事我实在没法告诉你。"
        r1 "你们担心我，我也是一样担心你们。"
        r1 "有些事我不说，我觉得你们反而更好。"
        r1 "还有些事我谁都不会说……因为我就是这样的人。"
        r1 "我这一辈子都是这么过来的。每次决定把想法或感受说出来，我都没得到什么好处。"
        r1 "我早就学会把情绪往肚子里咽。没人需要听我的难处。"
        r1 "我会自己解决，自己修好。"
        scene day5_homesweethome_71
        with Dissolve(1)
        ava "你害怕变得脆弱……"
        scene day5_homesweethome_73
        with Dissolve(1)
        r1 "我不是害怕，[ava]。我{b}不能允许{/b}自己脆弱。"
        scene day5_homesweethome_71
        with Dissolve(1)
        ava "亲爱的，那不叫生活……"
        scene day5_homesweethome_73
        r1 "但那是我的，好吗？"
        r1 "事情就是这样。"
        scene day5_homesweethome_74
        with Dissolve(1)
        ava "你又来了……"
        ava "我不是你的敌人……我不想吵……"
        scene day5_homesweethome_75
        with Dissolve(1)
        r1 "我知道，对不起。"
        scene day5_homesweethome_76
        with Dissolve(1)
        ava "亲爱的，我们真正需要你给的，是知道我们值得你信任。"
        ava "知道你需要我们……"
        ava "知道我们{b}能{/b}帮到你……"
        ava "就算工作上帮不上忙，至少也回来找我们，让我们能让你笑一笑……"
        ava "好让你一天稍微好过一点……"
        ava "我们想要的仅此而已……看到你开心。"
        scene day5_homesweethome_75
        with Dissolve(1)
        r1 "我的命是你们俩给的，[ava]。"
        r1 "你们{b}确实{/b}帮了我。"
        r1 "比你们想象的还要多。"
        scene day5_homesweethome_76
        with Dissolve(1)
        ava "我说的就是这个……那天半夜是你打电话给我们的。"
        ava "我们不知道你在哪。已经很晚了。而且一直联系不上你。"
        ava "而终于打通了，你却躺在人行道上流血……"
        ava "我们把你带回家，你差点死掉！"
        ava "[isa]不知道我们知道的事。那你今天连电话都不接的时候，[sophia]和我心里是什么感受？"
        ava "我们给[isa]做指甲不只是为了她。我以为这样也能让[sophia]分散一点注意力。"
        ava "就……至少让我们知道点情况，好吗？"
        scene day5_homesweethome_75
        with Dissolve(1)
        r1 "*叹气*……我尽量，好吗？"
        r1 "不做保证。但我会试。"
        scene day5_homesweethome_77
        with Dissolve(1)
        ava "我们要求的就只有这个。"
        scene day5_homesweethome_78
        with Dissolve(2)
        pause
        scene day5_homesweethome_75
        with Dissolve(1)
        r1 "你在干什么？"
        scene day5_homesweethome_77
        with Dissolve(1)
        ava "对不起……我做错了吗？"
        scene day5_homesweethome_75
        with Dissolve(1)
        r1 "没有，只是……你为什么要做这个？"
        play movie "images/Animations/day5/day5_avahand1.webm" loop 
        show movie with Dissolve(1)
        ava "[sophia]和[isa]在照顾你……可我在做什么？"
        ava "做饭？打扫房子？这些对我来说不够……"
        ava "我得对你有点用……"
        ava "我{b}想{/b}做个让你满意的女人……我以为这样能帮你缓解压力……"
        ava "为什么？你想让我停下吗？"
        r1 "不，不是那个意思。只是——"
        ava "我想让你压力大的时候就来用我……"
        ava "我想让你舒服……这有错吗？"
        r1 "没有。"
        play audio "audio/drums1.ogg" volume 0.5
        scene black
        play movie "images/Animations/day5/day5_avahand2.webm" loop 
        show movie with Dissolve(1)
        window hide
        pause
        window auto
        ava "我不想让你对我有不好的想法……但我一直在想……"
        ava "如果这能让你舒服……有什么害处呢？"
        ava "要是不和自己的另一半一起玩点刺激的，养个喜欢的人还有什么意义？"
        r1 "这对你来说叫冒险？"
        ava "也许吧……"
        ava "把你握在掌心……很刺激。看你享受其中……也很刺激。"
        ava "我觉得看你舒服更刺激。"
        ava "我做对了吗？"
        r1 "你做对了。"
        ava "这次由我先来，感觉也很好……以前总是你先……"
        ava "我想我偶尔也该主动一次。你觉得呢？"
        menu:
            "我觉得就算你没主动，我也不会因此不来找你。{p=0.0}{color=#00ff00}([ava] 好感 +3){/color}":
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[ava]的{color=#00ff00}好感{/color}增加了{color=#00ff00}3{/color}点！" )
                $love_ava+=3
                ava "*咯咯笑* 真的吗？"
                ava "我还以为你迟早会厌倦。"
                r1 "对象是你，我永远不会厌倦。"
                ava "你在给我灌迷魂汤吧？"
                r1 "也许吧。不过现在很难忍住。"
                
            "我觉得这是个好主意。我还想要更多。{p=0.0}{color=#ff0000}([ava] 堕落 +3){/color}":
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[ava]的{color=#ff0000}堕落{/color}增加了{color=#00ff00}3{/color}点！" )
                $corruption_ava+=3
                ava "*咯咯笑* 真的吗？"
                r1 "我不想再错过更多像这样的时刻。你想继续，我奉陪到底。"
                ava "我觉得我确实想要……"
        ava "我是说……看着你舒服，自己就舒服，这有点疯狂对吧？"
        r1 "一点也不。"
        ava "真的吗？"
        r1 "你知道看到你笑我有多开心吗？"
        r1 "我是不是也该说，看到你开心自己就开心，这种事也很疯狂？"
        window hide
        pause 0.1
        window auto
        scene day5_homesweethome_79
        with Dissolve(1)
        stop movie
        ava "你有时候说的话真的……"
        hide screen notifyEx with dissolve
        scene day5_homesweethome_80
        with Dissolve(1)
        pause
        scene day5_homesweethome_79
        with Dissolve(1)
        ava "我们现在该做什么？"
        
        menu:
            "继续打手枪。":
                play audio "audio/drums1.ogg" volume 0.5
                scene black
                play movie "images/Animations/day5/day5_avahand3.webm" loop 
                show movie with Dissolve(1)
                window hide
                pause
                window auto
                menu:
                    "转为口交。":
                        pause 0.01
                
            "转为口交。":
                pause 0.01
        play audio "audio/drums1.ogg" volume 0.5
        scene black
        play movie "images/Animations/day5/day5_blowjob1.webm" loop 
        show movie with Dissolve(1)
        window hide
        pause 0.1
        window auto
        ava "好，我能做到……"
        r1 "你以前做过这个。"
        ava "我知道……但一开始感觉很奇怪。"
        r1 "为什么？"
        ava "一开始舌头会有点刺刺麻麻的。"
        ava "然后吸的时候会不断有液体流出来，我得一直咽下去……接着就开始觉得身体发热……"
        ava "还有那个味道……当我把它凑得离鼻子那么近……"
        r1 "很难闻吗？"
        ava "什么？不……它……呃……很奇怪……"
        ava "甚至有点让人上瘾……"
        ava "让我觉得还想要更多。"
        window hide
        pause 0.1
        window auto
        scene day5_homesweethome_79
        with Dissolve(1)
        stop movie
        ava "我有个主意……"
        scene day5_homesweethome_80
        with Dissolve(1)
        ava "但别笑我，好吗？"
        ava "你要是愿意，我们可以试试……"
        r1 "什么主意？"
        scene day5_homesweethome_79
        with Dissolve(1)
        ava "如果我用我的胸部……？"
        ava "我想让你离我更近一些。"
        ava "离我的心这么近……离我的嘴这么近……"
        r1 "你知道该怎么做吗？"
        ava "我是说……我可以试试……"
        ava "可以吗？"
        r1 "可以。"
        scene day5_homesweethome_81
        with Dissolve(1)
        ava "感觉怎么样？"
        r1 "我能感觉到你的心跳得好快。"
        ava "我是说……我从没想过自己能做这种事。"
        play audio "audio/drums1.ogg" volume 0.5
        scene black
        play movie "images/Animations/day5/day5_boobjob1.webm" loop 
        show movie with Dissolve(1)
        window hide
        pause 0.1
        window auto
        ava "疼吗？"
        r1 "天啊，不疼！"
        r1 "你的胸部太棒了。"
        ava "我很高兴你喜欢。"
        ava "我不知道自己以前为什么没想到这个。"
        ava "你正在改变我。"
        play audio "audio/drums1.ogg" volume 0.5
        scene black
        play movie "images/Animations/day5/day5_boobjob2.webm" loop 
        show movie with Dissolve(1)
        window hide
        pause 0.1
        window auto
        r1 "那我做得还挺成功。"
        ava "你喜欢吗？"
        r1 "那你呢？"
        play sound "audio/Lockpick_Success.ogg" volume 0.1
        show screen notifyEx( msg="[ava]的{color=#ff0000}堕落{/color}增加了{color=#00ff00}3{/color}点！" )
        $corruption_ava+=3
        ava "*气喘吁吁* 喜欢……"
        hide screen notifyEx with dissolve
        ava "*气喘吁吁* 喜欢……"
        play audio "audio/drums1.ogg" volume 0.5
        scene black
        play movie "images/Animations/day5/day5_boobjob3.webm" loop 
        show movie with Dissolve(1)
        window hide
        pause 0.1
        window auto
        ava "你硬得厉害……"
        r1 "亲爱的，明明是你把我弄硬的。"
        play audio "audio/drums1.ogg" volume 0.5
        scene black
        play movie "images/Animations/day5/day5_boobjob4.webm" loop 
        show movie with Dissolve(1)
        window hide
        pause 0.1
        window auto
        ava "要是再这样下去，我就要你进到我身体里了。"
        r1 "我真想现在就把你按趴在这。"
        ava "别……别说这种话！"
        r1 "为什么不行？"
        ava "我……别——不要！"
        ava "我昨天那儿还有点酸……可你让我更想要你了。"
        r1 "能再快一点吗？我快到了。"
        play audio "audio/drums1.ogg" volume 0.5
        scene black
        play movie "images/Animations/day5/day5_boobjob5.webm" loop 
        show movie with Dissolve(1)
        window hide
        pause 0.1
        window auto
        ava "像……像这样吗？"
        r1 "你越来越熟练了……就是这样！"
        ava "我有个好老师。"
        window hide
        pause 0.1
        window auto
        menu:   
            "射在她脸上。":
                r1 "[ava]，我快了……"
                ava "射在我身上吧，没关系。"
        ava "求你射出来！"
        r1 "啊……操！"
        window hide
        pause 0.1
        window auto
        stop movie
        scene day5_homesweethome_82
        with hpunch
        r1 "*闷哼*"
        scene day5_homesweethome_83
        with flashbulb
        pause
        scene day5_homesweethome_84
        with flashbulb
        pause
        scene day5_homesweethome_85
        with Dissolve(2)
        ava "该死……"
        r1 "对不起。"
        ava "不……我……"
        play sound "audio/Lockpick_Success.ogg" volume 0.1
        show screen notifyEx( msg="[ava]的{color=#ff0000}堕落{/color}增加了{color=#00ff00}3{/color}点！" )
        $corruption_ava+=3
        ava "*咯咯笑*"
        scene day5_homesweethome_86
        with Dissolve(2)
        ava "我是说……射得越多，你就越享受。对吧？"
        r1 "嗯……也可以这么说。"
        hide screen notifyEx with dissolve
        ava "那我就高兴了！"
        r1 "我洗完澡了。你要留下来吗？"
        ava "我这样没法下楼……"
        menu:
            "真的吗？我觉得你这样美极了。{p=0.0}{color=#00ff00}([ava] 好感 +3){/color}":
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[ava]的{color=#00ff00}好感{/color}增加了{color=#00ff00}3{/color}点！" )
                $love_ava+=3
                ava "*咯咯笑* 真的吗？"
                r1 "现在仔细想想，可能不完全是因为我做了什么。"
                r1 "你本来就这么漂亮。"
                ava "你在给我灌迷魂汤吧？"
                
            "有意思的想法。也许哪天吧。{p=0.0}{color=#ff0000}([ava] 堕落 +3){/color}":
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[ava]的{color=#ff0000}堕落{/color}增加了{color=#00ff00}3{/color}点！" )
                $corruption_ava+=3
                ava "*咯咯笑* 你不是认真的吧。"
                r1 "只是随口一提。也许哪天吧。"
        hide screen notifyEx with dissolve
        ava "*咯咯笑* 天啊！你没救了！"
        r1 "我去换身衣服就下楼，好吗？"
        r1 "我觉得我大概得跟[sophia]道个歉。"
        ava "我也觉得！"
        r1 "得了吧。"
        $ renpy.end_replay()
        play music "audio/Castle in the sky.ogg" fadein 2 volume 0.1
        scene black
        with Dissolve(2)
        pause
        play sound "audio/open5.ogg"
        pause
        play sound "audio/open4.ogg"
        scene day5_homesweethome_87
        with Dissolve(2)
        r1 "[sophia]，你看……"
        r1 "关于刚才的事。"
        scene day5_homesweethome_88
        with Dissolve(1)
        r1 "我们能谈谈吗？"
        scene day5_homesweethome_89
        with Dissolve(1)
        pause
        scene day5_homesweethome_88
        with Dissolve(1)
        r1 "什……？"
        scene day5_homesweethome_90
        with Dissolve(1)
        sophia "哦，你已经下来了。"
        sophia "我以为你至少还要在上面十分钟。"
        scene day5_homesweethome_88
        with Dissolve(1)
        r1 "怎么了？"
        scene day5_homesweethome_91
        with Dissolve(1)
        sophia "你觉得我们在干什么？"
        scene day5_homesweethome_88
        with Dissolve(1)
        r1 "我明明看见你在摆桌子。我是说，你现在为什么要做这个？"
        scene day5_homesweethome_92
        with Dissolve(1)
        sophia "亲爱的……你看。"
        sophia "我……我们——"
        scene day5_homesweethome_93
        with Dissolve(1)
        sophia "好吧……这比我想象的难开口。"
        scene day5_homesweethome_94
        with Dissolve(1)
        isa "深呼吸一下。"
        scene day5_homesweethome_95
        with Dissolve(1)
        sophia "亲爱的……你看。"
        sophia "我知道我最近很让人烦。"
        sophia "我一直哭，一直尖叫大叫。"
        scene day5_homesweethome_96
        with Dissolve(1)
        sophia "我知道，好吗。我知道。"
        scene day5_homesweethome_97
        with Dissolve(1)
        sophia "我的时间不多……"
        scene day5_homesweethome_98
        with Dissolve(1)
        sophia "而且[isa]帮了我……"
        scene day5_homesweethome_99
        with Dissolve(1)
        sophia "所以我想，也许……"
        scene day5_homesweethome_100
        with Dissolve(1)
        sophia "真是的……你知道我最不擅长道歉。"
        scene day5_homesweethome_101
        with Dissolve(1)
        sophia "我做了点东西给你吃。不多，但我想你会喜欢。"
        scene day5_homesweethome_102
        with Dissolve(1)
        sophia "我们可以……一起吃晚饭。大概吧。"
        scene day5_homesweethome_103
        with Dissolve(1)
        sophia "然后晚点还可以一起看部电影。"
        scene day5_homesweethome_104
        with Dissolve(1)
        sophia "你觉得呢？"
        scene day5_homesweethome_105
        with Dissolve(2)
        pause
        scene day5_homesweethome_106
        with Dissolve(1)
        sophia "主意不好吗？"
        scene day5_homesweethome_105
        with Dissolve(1)
        pause
        scene day5_homesweethome_107
        with Dissolve(1)
        r1 "我觉得这主意棒极了。"
        scene day5_homesweethome_108
        with Dissolve(1)
        sophia "是吗？"
        scene day5_homesweethome_109
        with Dissolve(1)
        sophia "虽然你不能真的喝酒……"
        scene day5_homesweethome_110
        with Dissolve(1)
        sophia "但至少可以用果汁和气泡水装装样子，对吧？"
        scene day5_homesweethome_111
        with Dissolve(1)
        sophia "也许如果你不喜欢，我们可以——"
        scene day5_homesweethome_112
        with Dissolve(1)
        r1 "你完全没有什么需要道歉的。"
        scene day5_homesweethome_113
        with Dissolve(1)
        r1 "今天只是压力太大。"
        scene day5_homesweethome_114
        with hpunch
        sophia "我们别他妈再吵了，好吗？"
        r1 "真的吗？我超爱吵架的。"
        scene day5_homesweethome_115
        with Dissolve(1)
        sophia "滚！"
        play sound "audio/open4.ogg"
        scene day5_homesweethome_116
        with Dissolve(1)
        $ unlock_bust_char_image("ava", 2)
        show screen notifyEx( msg="[ava]的{color=#00ff00}胸部{/color}已{color=#00ff00}解锁{/color}！" )
        ava "是谁停战提议的？"
        scene day5_homesweethome_117
        with Dissolve(1)
        isa "都不是。我觉得更像是打成了平手。"
        hide notifyEx with dissolve
        scene day5_homesweethome_118
        with Dissolve(1)
        ava "爸爸妈妈能互相理解真是太好了！"
        isa "全靠你的功劳。"
        scene day5_homesweethome_119
        with Dissolve(1)
        ava "我只出了一点力。"
        scene day5_homesweethome_98
        with Dissolve(1)
        ava "可我看你也出了不少力。"
        scene day5_homesweethome_120
        with Dissolve(1)
        isa "我怎么能没出力？"
        ava "谢谢。"
        isa "不客气。"
        scene day5_homesweethome_122
        isa "你闻起来真好闻。你洗澡了？"
        scene day5_homesweethome_123
        ava "*咳嗽* 两位？开饭吗？我快饿死了！"
        scene day5_homesweethome_124
        with Dissolve(1)
        sophia "嗯，听起来是个好主意。"
        scene day5_homesweethome_125
        ava "太好了！那开始吧？"
        scene day5_homesweethome_126
        with Dissolve(2)
        pause
        scene day5_homesweethome_127
        with Dissolve(2)
        isa "那我就不打扰你们了。"
        scene day5_homesweethome_128
        with Dissolve(1)
        sophia "你疯了吗？"
        r1 "我们怎么可能让你走。"
        sophia "你帮忙准备了，当然要跟我们一起吃，亲爱的。"
        scene day5_homesweethome_129
        with Dissolve(1)
        isa "没关系的。我理解你们想有点私人空间。"
        scene day5_homesweethome_130
        with Dissolve(1)
        ava "[isa]，别这样。我们想让你待在这儿。"
        ava "来吧，坐我们旁边。"
        scene day5_homesweethome_131
        with Dissolve(1)
        ava "求求你了？"
        scene day5_homesweethome_132
        with Dissolve(1)
        pause
        scene day5_homesweethome_133
        with Dissolve(1)
        isa "谢谢你们。"
        isa "我很感激。"
        scene day5_homesweethome_134
        with Dissolve(1)
        r1 "你既然在这儿，就是一家人。"
        r1 "没有你我们就不摆桌子了。"
        r1 "我们要一起吃。"
        r1 "我想让你有在自己家的感觉。"
        scene day5_homesweethome_135
        with Dissolve(2)
        pause
        scene day5_homesweethome_136
        with Dissolve(2)
        pause
        scene day5_homesweethome_137
        with Dissolve(2)
        isa "谢谢你，[r1]……"
        scene day5_homesweethome_138
        with Dissolve(2)
        ava "第一个给你。"
        scene day5_homesweethome_139
        with Dissolve(2)
        pause
        scene day5_homesweethome_140
        with Dissolve(2)
        pause
        stop music fadeout 3
        stop music2 fadeout 3
        stop music3 fadeout 3
        scene black
        with Dissolve(3)
        pause
        jump day6_update
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        
        
        
        
 #       r1 "你是在哪儿学的这种拳法？"
 #       ingrid "Mein Vater wollte einen Sohn."
  #      r1 "他得到了。"
  #      ingrid "我跟你这样的男人打过。"
  #      ingrid "我知道你留手了。"
  #      r1 "什么？我没有！"
        
        #what's his profession?
        #threaten to break his hands, then
        #YES! FINALLY! SOMEONE WHO KNOWS HOW TO ROLEPLAY!
        #THAT'S WHAT I WANT!
        #asu "你只能选阻力最小的那条路。"
        #r2 "斩了蛇头，蛇身自会枯萎。"
        #r2 "兵卒既倒，王者自现。"
        #r2 "火焰招来飞蛾。"
        #r2 "杀了族群，公牛才会冲出来。"
        
        
            
        #stop music
        #play music "audio/birds.ogg" fadein 3 volume 0.2