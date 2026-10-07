label day6_update:
    label day6_areyouwashed:
        $ lock_bust_char_image("ava", 3)
        $ unlock_bust_char_image("ava", 2)
        stop music fadeout 3
        stop music2 fadeout 3
        stop music3 fadeout 3
        $_game_menu_screen = "save_screen"
        $quick_menu = True
        
        play music "audio/soundtrack/original2-slow.ogg" volume 0.5 fadein 7
        
        scene day6_areyouwashed_1
        with Dissolve(2)
        pause
        scene day6_areyouwashed_2
        with Dissolve(2)
        pause
        scene day6_areyouwashed_3
        with Dissolve(2)
        pause
        play sound "audio/handgunslide1.ogg" volume 0.5
        scene day6_areyouwashed_4
        with Dissolve(2)
        pause
        scene day6_areyouwashed_5
        with Dissolve(2)
        pause
        play sound "audio/handgunclip1.ogg" volume 0.5
        scene day6_areyouwashed_6
        with Dissolve(2)
        pause
        scene day6_areyouwashed_7
        with Dissolve(2)
        pause
        play sound "audio/handgunslide2.ogg" volume 0.5
        scene day6_areyouwashed_8
        pause
        scene day6_areyouwashed_9
        with Dissolve(2)
        r1 "你就打算站在那儿看我吗？"
        scene day6_areyouwashed_10
        with Dissolve(0.5)
        sophia "嗯……或许吧？"
        scene day6_areyouwashed_11
        with Dissolve(2)
        sophia "我得说，你整理那些子弹的时候看起来挺健美的。"
        sophia "是空包弹，对吧？"
        scene day6_areyouwashed_12
        with Dissolve(2)
        pause
        scene day6_areyouwashed_15
        with Dissolve(0.5)
        r1 "你怎么知道这些是空包弹？"
        scene day6_areyouwashed_13
        with Dissolve(2)
        sophia "谁知道呢……"
        scene day6_areyouwashed_14
        with Dissolve(2)
        sophia "也许我是——"
        sophia "等等……那把我知道。"
        sophia "那看起来是[ingrid]的配枪。是吧？"
        scene day6_areyouwashed_16
        with Dissolve(0.5)
        r1 "不。现在它是你的了。"
        sophia "什么？不，我不能收下。"
        r1 "为什么不能？"
        r1 "收下吧。我还有别的。"
        sophia "可是——"
        r1 "[sophia]。收下。我是认真的。"
        scene day6_areyouwashed_17
        with Dissolve(2)
        pause
        scene day6_areyouwashed_18
        with Dissolve(2)
        r1 "*轻笑* 我猜你知道怎么用。"
        scene day6_areyouwashed_20
        with Dissolve(1)
        pause
        scene day6_areyouwashed_19
        with Dissolve(0.5)
        sophia "别犯傻。"
        scene day6_areyouwashed_20
        with Dissolve(1)
        sophia "我想老习惯很难改。"
        scene day6_areyouwashed_21
        with Dissolve(1)
        sophia "你还是在把实弹换成空包弹。"
        sophia "就像我们刚把[ingrid]带来的时候一样。"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "那时候那样更安全。"
        scene day6_areyouwashed_12
        with Dissolve(1)
        r1 "这房子已经不适合放实弹了。"
        r1 "现在那样又更安全了。"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "我想让你用那把枪教[ava]如何自卫。"
        scene day6_areyouwashed_19
        with Dissolve(1)
        sophia "她最终总得用实弹练习。你知道的，对吧？"
        play sound "audio/handgunclip1.ogg" volume 0.5
        scene day6_areyouwashed_12
        with Dissolve(1)
        r1 "会的。等她明白扣动扳机意味着什么之后。"
        r1 "更重要的是，明白这些东西既强大又危险。"
        r1 "先用空包弹，然后是哑弹。只有这样才能进入实弹训练。"
        r1 "所以，是的。最终会有的。但现在还不行。"
        scene day6_areyouwashed_20
        with Dissolve(1)
        pause
        play sound "audio/Flash.ogg" volume 0.5
        play music2 "audio/soundtrack/Ambiance/nature1.ogg" volume 0.5
        scene day6_areyouwashed_65
        with flashbulb
        sophia "我会用枪，[ingrid]。"
        ingrid "我可从没说不会。但狙击步枪完全是另一种东西。"
        scene day6_areyouwashed_66
        with Dissolve(1)
        ingrid "它不只是工具。它要求完美。"
        scene day6_areyouwashed_68
        with Dissolve(1)
        sophia "你能别再说了吗？"
        sophia "好吧，你是专家。但你不是神。"
        sophia "我看得出来这比握手枪难多了。"
        sophia "我向你保证！你每次一开口都是——"
        scene day6_areyouwashed_69
        ingrid "{i}我要你听我说，verdammt！{/i}"
        ingrid "{i}今晚我们会处在无法直接跟在他身后的局面。{/i}"
        ingrid "{i}我们需要在高处做他的眼睛。清楚了吗？{/i}"
        ingrid "{i}这是我的主场。按我的规矩。{/i}"
        scene day6_areyouwashed_67
        with Dissolve(1)
        ingrid "{i}如果你不理解我在做什么。如果你跟我不同步。如果你引发任何冲突……{/i}"
        ingrid "{i}如果我做出判断时多花了一秒钟……{/i}"
        scene day6_areyouwashed_69
        with Dissolve(1)
        ingrid "{i}我需要你认真对待这件事。{/i}"
        ingrid "{i}如果我失手，如果我犹豫，如果我不确定……这里没有任何犯错的余地。{/i}"
        ingrid "{i}这份责任无法改变。它是强制的。你明白吗？！{/i}"
        scene day6_areyouwashed_68
        with Dissolve(1)
        sophia "我很认真。"
        scene day6_areyouwashed_69
        with Dissolve(1)
        ingrid "{i}你并不认真。天哪，外科医生怎么这么难搞？{/i}"
        scene day6_areyouwashed_68
        sophia "我难搞？！我？！"
        scene day6_areyouwashed_69
        ingrid "{i}你就是！你太傲慢了。但拿着步枪时？那态度会害死人。{/i}"
        scene day6_areyouwashed_68
        sophia "我还以为那个才是——"
        scene day6_areyouwashed_69
        ingrid "认真对待这件事。"
        ingrid "这就是我为什么必须反复强调。"
        ingrid "{i}听着。今晚我们要协同行动，你必须服从我的每一条指令。{/i}" 
        ingrid "{i}你能做到吗？{/i}"
        scene day6_areyouwashed_68
        with Dissolve(1)
        sophia "我试试看。"
        scene day6_areyouwashed_70
        with Dissolve(1)
        play sound "audio/handgunslide2.ogg" volume 0.5
        ingrid "{i}Gut.{/i}"
        scene day6_areyouwashed_70_1
        with Dissolve(1)
        sophia "{size=-7}现在难搞的人变成我了……真是荒谬。{/size}"
        scene day6_areyouwashed_70
        with Dissolve(1)
        ingrid "{i}今晚你会用这样的瞄准镜，这样就能熟悉它。{/i}"
        ingrid "{i}你来当我的观察手。{/i}"
        ingrid "{i}忘掉你那些关于精准的知识。{/i}"
        scene day6_areyouwashed_68
        with Dissolve(1)
        sophia "你什么意思？"
        scene day6_areyouwashed_70
        with Dissolve(1)
        ingrid "{i}这跟你平常的做法不一样。{/i}"
        ingrid "{i}你的手枪。快拔、瞄准、开枪。子弹打到你瞄准的地方。{/i}"
        ingrid "{i}你讲究快和机动。你边移动边射击，有时两者同时进行。{/i}"
        ingrid "{i}步枪？我们一动不动。{/i}"
        ingrid "{i}我们还得担心不暴露位置。重新转移的机会很少。{/i}"
        ingrid "{i}风、距离、障碍物。子弹落在哪里，什么都会变。{/i}"
        ingrid "{i}跟你做手术不同，有些事我们控制不了。{/i}"
        scene day6_areyouwashed_68
        with Dissolve(1)
        sophia "你是在耍我吗？！"
        sophia "手术同样需要大量计算。你到底在说什么鬼话？"
        sophia "就算真是那样，那种生活也早就跟我无关了。"
        scene day6_areyouwashed_70
        with Dissolve(1)
        ingrid "{i}你永远都是外科医生。就像我永远都是个 Jäger。"
        ingrid "{i}我不是这个意思，Zophia。{/i}" 
        ingrid "{i}一切都是你选的。房间、光线、器械。{/i}"
        ingrid "{i}在外面？风、雨、光，还有移动目标。{/i}"
        ingrid "{i}无菌、可控的环境。{/i}"
        ingrid "{i}但在这里，我们只能适应我们拿到的。{/i}"
        ingrid "{i}在压力下你还能保持同样的精准度吗？{/i}"
        scene day6_areyouwashed_68
        with Dissolve(1)
        sophia "我可是战区的创伤外科医生。那环境一点都谈不上可控。"
        sophia "我能在炮火下照顾好自己。"
        scene day6_areyouwashed_69
        with Dissolve(1)
        ingrid "{i}炮火下？当然。我知道你是谁。我见过你上战场。{/i}"
        ingrid "{i}你大概能给自己做手术，不用麻醉什么的——这一点我丝毫不怀疑。"
        ingrid "{i}但我指的是更……真实的东西。{/i}"
        ingrid "{i}在炮火下，你能给他做手术吗？明知道手术刀只要错动一下，他就会永远离开你的双臂？{/i}"
        ingrid "{i}在炮火下，你能做那个吗？{/i}"
        scene day6_areyouwashed_68
        with Dissolve(1)
        pause
        scene day6_areyouwashed_71
        with dissolve
        pause
        scene day6_areyouwashed_72
        with Dissolve(1)
        play sound "audio/handgunslide2.ogg" volume 0.5
        ingrid "{i}Gut。既然你明白了，你就该知道，当我透过这个瞄准镜守着他时，我必须在他出事之前就看清一切。{/i}"
        ingrid "{i}因为这里就是我的手术室。我不能……失败。{/i}"
        ingrid "{i}你可能永远不需要做那种判断。但我必须做。每次我趴在瞄准镜后面……{/i}"
        scene day6_areyouwashed_69
        with Dissolve(1)
        ingrid "{i}今晚……我是主刀，你来辅助我。{/i}"
        ingrid "{i}不许质疑……不许冲突。{/i}"
        ingrid "{i}我指挥，你辅助。我们就这么配合。作为一个团队。{/i}"
        ingrid "{i}因为伤，我太久没碰步枪了。我需要校准这把。{/i}"
        ingrid "{i}所以拿上我给你的瞄准镜。盯着我瞄准的方向。{/i}"
        ingrid "{i}我们如同一人。明白了吗？{/i}"
        play sound "audio/Flash.ogg" volume 0.5
        scene day6_areyouwashed_20
        with flashbulb
        pause
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "你没事吧？"
        scene day6_areyouwashed_20
        with Dissolve(1)
        sophia "嗯……我没事。"
        sophia "现在是我在训练[ava]了。"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "你一直在做这个，对吧？"
        scene day6_areyouwashed_19
        with Dissolve(1)
        sophia "嗯……算是吧。"
        sophia "房子里还有[isa]，这样会有点麻烦。"
        scene day6_areyouwashed_22
        r1 "像你本来在做的那样，带她去林子里就行。"
        r1 "不一定非得在房子里。"
        r1 "其实……我本来就不希望你在房子里做。"
        scene day6_areyouwashed_20
        with Dissolve(1)
        sophia "我能想办法安排。"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "你已经教过她基础的东西了，但她现在可以学点更进阶的东西。"
        r1 "我改装了那把，让它手感更……真实。它会模拟实弹的后坐力。"
        r1 "但小心别打出实弹，明白吗？那东西会在她手里炸开。"
        r1 "我要你让她看清实弹、空包弹和哑弹的区别。"
        r1 "等确认她能保持冷静，我们就上实弹。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "其实这倒提醒我了……"
        sophia "关于她……"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "打住。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "不，我是认真的。让我说完一句。"
        sophia "你不觉得有点可疑吗？"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "好。她会一点德语……那又怎样？"
        r1 "我还会一点意大利语呢，那也不代表我是做披萨的。"
        r1 "再说了，她把「Kraft」那部分搞错了。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "而我正因为如此才点到为止。"
        sophia "但耍小聪明和有真学问是两回事。"
        sophia "她可能只是聪明……但是……"
        sophia "你懂的？"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "我明白。但我们没有任何真正的理由怀疑她。"
        r1 "或者觉得她不只是表面那样。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "除了她的纹身。"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "也许我们太沉浸在自己的小世界里了。"
        r1 "在我们的世界里，纹身是有含义的。对平民来说就没那么回事。"
        r1 "她可能只是喜欢那个图案。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "我知道……但听我说……"
        sophia "在沙漠的时候，我们遇到过就那样露过马脚的渗透者。"
        sophia "她说错那个德语词的方式……她说那意思是「craft」……"
        sophia "这正是我们的翻译警告过我们的那种错误。"
        sophia "我不是说她是什么联邦探员、间谍或者该死的克格勃。我还没疯。"
        sophia "我只是说，在遇到我们之前她有自己的人生。"
        sophia "她是个很好的女孩。她是我朋友。但我们不知道她到底是谁，对吧？"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "也许你想太多了。你已经不在沙漠里了。"
        r1 "德国人已经走了。"
        r1 "她没有口音，也没有任何习惯性的小动作。"
        r1 "[ava]只是犯了个简单的错，仅此而已。这不能说明她有威胁。"
        r1 "你也看到过她是什么样的人，她怎么对待每个人。"
        r1 "我们现在知道她是谁了。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "是的。"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "那你想怎么办？"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "暂时……什么都不做。"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "那你为什么还要提？"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "说不定哪天会有人来敲我们的门。"
        sophia "也许她有家人，或者有工作。有认识她、担心她的人。"
        scene day6_areyouwashed_22
        r1 "你为什么现在才说这个？"
        scene day6_areyouwashed_23
        sophia "因为我扯远了。我只是遇到了一个有点意思的小东西。"
        sophia "一个我忍不住想逗逗的人……"
        sophia "..."
        scene day6_areyouwashed_20
        with Dissolve(1)
        sophia "然后我意识到，我遇到的是一个朋友。"
        scene day6_areyouwashed_23
        with dissolve
        sophia "而我不想失去她……"
        sophia "现在我在这儿，教我的朋友怎么在我们的世界里活下去……"
        sophia "昨天那事之后……我很担心它会反过来咬我们一口。"
        scene day6_areyouwashed_22
        r1 "真到那一步我们再担心，好吗？"
        r1 "但我觉得不会。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "这点我不太确定……万一哪天她醒来，记起了一切呢？"
        sophia "别忘了，我们认识的[ava]并不是一直这样。"
        sophia "也许她会意识到这种生活不适合她……"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "我知道……我自己已经撞见过好几次自己在想这个了。"
        r1 "但就像我说的，如果随着时间推移她想起更多，我们再担心。"
        r1 "没必要去逼她。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "我也想尊重她的隐私，亲爱的。真的。"
        sophia "但在我们的世界里，知道得太少和知道得太多一样危险。"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "我知道。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "还有一件事……"
        sophia "[ava]发生了那样的事之后……"
        sophia "[isa]……我实在忍不住去查了她。"
        sophia "我挺喜欢她的，但还是觉得小心为上，免得后悔……"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "[sophia]……"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "你看……我想先从你这里听到解释。这不是关于你和狼群的工作，好吗？"
        sophia "我还不至于蠢到那地步。"
        sophia "实际上我是在找任何东西。"
        sophia "轻罪记录、欠缴罚单、交通违规。任何将来可能给我们添麻烦的东西。"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "继续……"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "但我发现她在……校园医务室工作？"
        scene day6_areyouwashed_24
        with Dissolve(1)
        r1 "天哪，[sophia]……"
        scene day6_areyouwashed_25
        with Dissolve(1)
        r1 "你光靠「查」轻罪记录，怎么可能查到这种事？"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "亲爱的，她是平民。她又不是在藏什么东西。"
        scene day6_areyouwashed_25
        with Dissolve(1)
        r1 "「又不是在藏什么东西。」"
        scene day6_areyouwashed_24
        with Dissolve(1)
        r1 "看在老天的份上，[isa]……"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "什么？真的，亲爱的。我连挖都不用挖——是她自己告诉我的。"
        scene day6_areyouwashed_26
        with Dissolve(1)
        r1 "真会毁掉自己的掩护。"
        scene day6_areyouwashed_27
        with Dissolve(0.5)
        r1 "她还说了什么？"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "我的掩护？"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "不是你的。是[isa]的。"
        r1 "你看，[isa]遇到过一些麻烦。"
        r1 "这事很私密，我实在没法多说。我答应过她会保密。"
        r1 "求你别逼我到不得不背叛她信任的地步。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "为什么？"
        menu:
            "因为为了你，我愿意。{p=0.0}{color=#00ff00}([sophia] 好感 +4){/color}":
                scene day6_areyouwashed_25
                with Dissolve(1)
                r1 "因为你知道，为了你我会的。"
                r1 "我欠你这份。"
                r1 "不过……还是希望你别逼我到不得不出尔反尔的地步。"
                scene day6_areyouwashed_23
                with Dissolve(1)
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[sophia]的{color=#00ff00}好感{/color}提升了{color=#00ff00}4{/color}点！" )
                $love_sophia+=4
                pause
                scene day6_areyouwashed_28
                with Dissolve(2)
                sophia "最近秘密越来越多了……"
            "因为我说出的话就是我的承诺。{p=0.0}{color=#00ff00}([isa] 好感 +4){/color}":
                scene day6_areyouwashed_25
                with Dissolve(1)
                r1 "因为我向她保证过。就像我向你保证的那样。"
                r1 "我对你从没出尔反尔过，对吧？"
                r1 "如果我去说别人的秘密，你怎么能相信我的话？"
                scene day6_areyouwashed_23
                with Dissolve(1)
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[isa]的{color=#00ff00}好感{/color}提升了{color=#00ff00}4{/color}点！" )
                $love_isa+=4
                pause
                scene day6_areyouwashed_28
                with Dissolve(2)
                sophia "最近秘密越来越多了……"
            "因为我不在乎。{p=0.0}{color=#ff0000}(善良 -2){/color}":
                scene day6_areyouwashed_25
                with Dissolve(1)
                r1 "因为我不在乎，而且现在也不打算为此操心。"
                r1 "这会提高我工作的成功率。"
                r1 "所以希望你以后别再质疑我。"
                scene day6_areyouwashed_23
                with Dissolve(1)
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="你的{color=#00ff00}善良{/color}下降了{color=#ff0000}2{/color}点！" )
                $goodness-=2
                pause
                scene day6_areyouwashed_28
                with Dissolve(2)
                sophia "最近秘密越来越多了……"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "我做的是必须做的事。不是我想做的事。"
        hide screen notifyEx with dissolve
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "但你也看得出来，秘密会让我们陷入多大危险？……我们还能撑多久才露馅？"
        sophia "或者我们还能撑多久才遇上不该遇上的人？[ava]和我都会措手不及。"
        sophia "然后呢？我们祈祷然后指望好运？"
        sophia "我理解你暂时不想告诉[ava]。她现在还太嫩。"
        sophia "但你至少该告诉我。"
        scene day6_areyouwashed_26
        with Dissolve(1)
        sophia "事情越来越危险了。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "你还记得在部队受训的内容吗？"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "你得说具体点。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "RTI。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "抗审讯？那又怎么样？"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "还记得侦察是怎么运作的吗？为什么只有指挥官知道命令？"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "这样就算有人被抓，也无法泄露任务或整个小队。"
        sophia "你怕的就是这个？"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "你知道得越多，危险就越大。"
        r1 "你没法交出自己不知道的东西。"
        r1 "只要有人觉得你知道的比该知道的多，你就变得有价值了。"
        r1 "你就值得他们费力气来挖了。"
        r1 "只要我们透露出你牵涉其中，你就一定会成为目标。"
        r1 "你明白吗？"
        scene day6_areyouwashed_23
        with Dissolve(1)
        sophia "给谁当目标？！"
        sophia "亲爱的，我不需要你在我背上画个靶子。我早就有了一个！"
        sophia "你觉得我要是进了俄罗斯地界会怎样？"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "不是……那种情况。"
        r1 "任务中被俘是一回事，被人设局抓住完全是另一回事。"
        r1 "我因为[ingrid]对族群做的事，已经在这座城市的各个势力间传开了。"
        r1 "我出征时把你推开，是有原因的。"
        scene day6_areyouwashed_29
        with Dissolve(2)
        sophia "亲爱的……你想死在那场战争里，不想把我一起拖进去。"
        sophia "我花了比该花的更长的时间才明白过来，但最后还是明白了。"
        sophia "而你应该知道，我本来会跟你一起去的。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "那不是你的战争。"
        r1 "那样更安全。"
        scene day6_areyouwashed_29
        with Dissolve(1)
        sophia "对谁更安全？！"
        sophia "别对我说这种话。你明明知道我也失去了[ingrid]。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "我的意思是你不属于任何势力。你只会成为所有人的目标。"
        r1 "尤其是在他们想伤害我的时候。族群会先拿你开刀。"
        r1 "我在乎你。但狼群不欠你任何东西。"
        r1 "你要是受伤，不会有人为你报复。"
        r1 "也不会有人为你改变计划来保证安全。"
        r1 "只有我一个人会为你的死难过。"
        r1 "而那会成为压垮我的最后一根稻草。"
        r1 "我还活着，是因为那场战争里你不在我身边。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        pause
        scene day6_areyouwashed_26
        with Dissolve(1)
        r1 "我给他们传去了非常明确的信息。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "他们知道我会对任何伤害你的人做什么。"
        r1 "我会把那个胆敢碰你一根手指的混账揪出来。"
        r1 "但那有行动风险，也会招来针对你的猎杀。"
        r1 "而这差别就取决于你知道多少。"
        scene day6_areyouwashed_23
        with Dissolve(1)
        r1 "我瞒着你……是因为我担心你。"
        r1 "你和艾娃知道得越少，你们就越安全。"
        scene day6_areyouwashed_23
        pause
        scene day6_areyouwashed_28
        with Dissolve(2)
        sophia "*叹气*"
        scene day6_areyouwashed_29
        with Dissolve(2)
        sophia "你和我一起趟过地狱，又一起爬了回来。"
        sophia "我足够了解你，看得出来你什么时候没跟我说全。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "[sophia]……"
        scene day6_areyouwashed_29
        with Dissolve(1)
        sophia "我不知道那是什么……但还有别的事你没告诉我。"
        sophia "这没关系……但是……"
        scene day6_areyouwashed_28
        with Dissolve(2)
        sophia "别像丢剩饭给野狗那样丢点零碎给我。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "你不是小孩子。我就当面告诉你，有些事我不能谈。"
        r1 "我不是在找借口。"
        scene day6_areyouwashed_22
        with Dissolve(1)
        r1 "你为什么想知道更多？"
        r1 "老实告诉我。你是想被接纳，还是想确认我们安全？"
        scene day6_areyouwashed_28
        with Dissolve(2)
        sophia "我们从来都不安全。在我们这行更不可能。"
        scene day6_areyouwashed_29
        with Dissolve(1)
        sophia "我想知道的是我们有所准备。"
        sophia "想知道我们还有彼此。"
        sophia "想知道万一出事，我们能互相支撑。"
        sophia "我守你的背，你守我的背。还记得吗？"
        scene day6_areyouwashed_27
        with Dissolve(2)
        r1 "这点没变。"
        scene day6_areyouwashed_29
        with Dissolve(1)
        sophia "那我不知道自己在防什么，怎么守你？"
        scene day6_areyouwashed_27
        with Dissolve(1)
        pause
        scene day6_areyouwashed_26
        with Dissolve(1)
        pause
        scene day6_areyouwashed_27
        with Dissolve(0.5)
        r1 "好吧。我可以告诉你一点。"
        r1 "但你得答应我不再深挖。在我需要告诉你更多之前，你要对我说的满意。"
        r1 "如果……真有那一天。"
        r1 "成交？"
        scene day6_areyouwashed_29
        with Dissolve(1)
        sophia "成交。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "我是卧底。"
        scene day6_areyouwashed_26
        with Dissolve(1)
        r1 "狼群要我潜入一个机构。就是你查的那所学院。"
        r1 "那是个很特别的地方……给政客、商人、警察高层之类的人……"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "高端的。那种人。"
        r1 "狼群要我尽可能多地搜集他们的情报。"
        scene day6_areyouwashed_30
        with Dissolve(1)
        pause
        scene day6_areyouwashed_31
        with Dissolve(1)
        sophia "你和市长那顿晚餐……"
        sophia "嗯……现在全都说得通了。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "那次……比我预想的要容易……"
        scene day6_areyouwashed_32
        with Dissolve(1)
        sophia "好了好了，亲爱的。我们都是专业的，不是吗？有我的话在——不会再有人多嘴。"
        sophia "这是个渗透任务。在平民场所。"
        sophia "我不需要知道更多。"
        sophia "我只是希望你早点告诉我你是卧底。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "这不让你介意吗？"
        scene day6_areyouwashed_32
        with Dissolve(1)
        sophia "介意什么？"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "介意我要渗透一个民用设施？"
        scene day6_areyouwashed_33
        with Dissolve(1)
        sophia "现在才来讨论道德，不觉得太晚了吗？"
        scene day6_areyouwashed_27
        with Dissolve(1)
        pause
        scene day6_areyouwashed_26
        with Dissolve(1)
        r1 "也许吧。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "你还记得你为什么踏上这条路吗？"
        scene day6_areyouwashed_34
        with Dissolve(1)
        pause
        scene day6_areyouwashed_35
        with dissolve
        pause 0.2
        sophia "嗯……记得。"
        scene day6_areyouwashed_36
        with Dissolve(1)
        sophia "被军事法庭判刑之后……我对这一切烦透了……"
        sophia "我只想要一块地、几头牲口，在远离所有人的地方。"
        scene day6_areyouwashed_37
        with dissolve
        sophia "和动物一起生活显得更……人道一点。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "我就是在这片街巷长大的。见过最不堪的那一面。"
        r1 "我一无所有的时候——当我真的{b}什么都不是{/b}的时候——是畜群收留了我。"
        r1 "人{b}想{/b}有个归属。而当你一无所有时，那真的能把人的脑子搞乱。"
        r1 "尤其当你还只是个孩子。"
        r1 "我的价值观和大多数人不一样。"
        r1 "但我的原则始终没变。我{b}想{/b}让这座城市变得更好。"
        scene day6_areyouwashed_37
        with Dissolve(1)
        sophia "真希望我还有那种信念……"
        sophia "我把我的那份埋在了沙漠里……连同我以为自己懂的一切。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "我们每个人都有那样一天。我的那天，是[ingrid]死去的那天。"
        scene day6_areyouwashed_38
        with Dissolve(1)
        sophia "我知道，亲爱的。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "但那依然困扰着我。"
        scene day6_areyouwashed_38
        with Dissolve(1)
        sophia "因为你的原则没变。"
        scene day6_areyouwashed_26
        with Dissolve(1)
        r1 "因为我的原则没变……"
        scene day6_areyouwashed_27
        with dissolve
        r1 "我试着想明白，那场战争里我做的那些事{b}为什么{/b}。"
        r1 "「我这么做，是为了再也没人敢伤害我爱的人。」"
        r1 "「我这么做，是为了把这座城市身上无端滋生的贪婪洗干净。」"
        r1 "「我这么做，是为了让那些贪权妄想的混蛋知道，咬了太多会是什么下场。」"
        r1 "这些理由都说得通。"
        r1 "可真相呢？"
        scene day6_areyouwashed_26
        with dissolve
        pause 0.2
        scene prologue44
        pause 0.05
        scene prologue54
        pause 0.05
        scene prologue64
        pause 0.05
        scene prologue72
        pause 0.05
        scene prologue77
        pause 0.05
        scene prologue60
        pause 0.05
        scene prologue96
        pause 0.05
        scene day6_areyouwashed_26
        pause
        r1 "我本来会把他们全杀了，纯粹只为杀人而杀。"
        scene day6_areyouwashed_73
        with Dissolve(1)
        pause
        scene day6_areyouwashed_74
        with dissolve
        pause
        scene day6_areyouwashed_26
        with Dissolve(1)
        r1 "就算毫无好处我也会去打仗。不……毫无价值。"
        r1 "我不在乎能不能赢，也不在乎谁对。"
        r1 "我想要血。"
        r1 "我{b}需要{/b}看到他们受苦。"
        scene day6_areyouwashed_74
        with Dissolve(1)
        sophia "我……明白了。"
        scene day6_areyouwashed_27
        with dissolve
        r1 "那改变了我。"
        scene day6_areyouwashed_74
        with Dissolve(1)
        pause
        scene day6_areyouwashed_75
        with dissolve
        sophia "我们每个人都有心魔……我想。"
        sophia "它改变了我们所有人。"
        scene day6_areyouwashed_76
        with dissolve
        sophia "*咂*"
        scene day6_areyouwashed_77
        with dissolve
        sophia "你本来不必一个人扛。"
        scene day6_areyouwashed_78
        with dissolve
        sophia "我……本可以帮你。"
        scene day6_areyouwashed_26
        with Dissolve(1)
        r1 "现在说这个有点晚了。"
        r1 "但也许你现在能帮我。"
        scene day6_areyouwashed_39
        with Dissolve(1)
        pause
        scene day6_areyouwashed_26
        with Dissolve(1)
        pause
        scene day6_areyouwashed_39
        with Dissolve(1)
        pause
        scene day6_areyouwashed_40
        with dissolve
        sophia "[sophia]能帮你解决什么？"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "既然我们都在敞开心扉……"
        scene day6_areyouwashed_26
        with dissolve
        r1 "有件事一直让我很纠结。"
        scene day6_areyouwashed_39
        with Dissolve(1)
        sophia "是关于离开狼群的事？"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "是关于我必须做的事。"
        scene day6_areyouwashed_27_2
        with Dissolve(1)
        sophia "*轻笑* 你在干什么？掰断他们的手指逼供？"
        sophia "我是说……这份工作能{b}糟{/b}到什么地步？"
        scene day6_areyouwashed_27_3
        with dissolve
        sophia "他们只是平民。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        r1 "困扰我的不是暴力，[sophia]。"
        r1 "在我看来，他们是无辜的人。"
        r1 "这些人……他们只是想过好自己的日子。"
        r1 "我不想让他们被卷进交火。"
        scene day6_areyouwashed_39
        with Dissolve(1)
        pause
        scene day6_areyouwashed_41
        with dissolve
        sophia "好吧，亲爱的，我有点听不懂了。"
        sophia "我不知道你在那边干什么，可我们都已经做了这么多……"
        sophia "我是说……他们会怎样又有什么关系——"
        scene day6_areyouwashed_42
        with dissolve
        sophia "哦……"
        scene day6_areyouwashed_40
        with dissolve
        sophia "你把自己牵扯进来了。"
        sophia "你把这事当成自己的了。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        scene day6_areyouwashed_26
        with dissolve
        r1 "我是……"
        r1 "而我不喜欢这样。"
        scene day6_areyouwashed_27
        with dissolve
        r1 "我对几个学生有了感情。"
        menu:
            "我觉得自己像是在背叛他们。{p=0.0}{color=#00ff00}(善良 +2){/color}":
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="{color=#00ff00}善良{/color}增加了{color=#00ff00}2{/color}点！" )
                $goodness+=2
                r1 "还有和他们越走越近……成为他们的朋友。"
                r1 "把他们的秘密托付给我。"
                r1 "最后却背叛他们……"
                scene day6_areyouwashed_26
                with dissolve
                r1 "这种事我不会轻易去做。"
                scene day6_areyouwashed_27
                with dissolve
                r1 "这种事我根本不会做。"
            "但我知道自己不该在意。他们只是达成目的的手段。{p=0.0}{color=#ff0000}(善良 -2){/color}":
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="你的{color=#00ff00}善良{/color}减少了{color=#ff0000}2{/color}点！" )
                $goodness-=2
                r1 "可即便如此……这一切还是困扰着我。"
                r1 "我不喜欢这样。我不要这样。"
                r1 "这会让我变得软弱。而我现在承受不起。"
            
        
        
        hide screen notifyEx with dissolve
        scene day6_areyouwashed_41
        with Dissolve(1)
        pause
        scene day6_areyouwashed_40
        with Dissolve(1)
        pause
        scene day6_areyouwashed_43
        with dissolve
        sophia "你知道吗……这挺有意思的。"
        sophia "我都忘了这份工作能把人变得多麻木。"
        scene day6_areyouwashed_40
        with dissolve
        sophia "不过，也许我们还没彻底迷失。"
        scene day6_areyouwashed_43
        with dissolve
        sophia "我记得我成为外科医生时有多年轻……"
        sophia "我想救活那些所有人都已经放弃的生命。"
        sophia "想要拥有{b}改变{/b}命运的力量。"
        sophia "我那时充满干劲。"
        scene day6_areyouwashed_45
        with dissolve
        sophia "我参军，是因为我{b}相信{/b}自己能带来改变。"
        scene day6_areyouwashed_44
        with dissolve
        sophia "而现在我是个杀手……"
        sophia "命运都已经把我们耍成这样了，它还让我们以为自己掌控得了什么？"
        scene day6_areyouwashed_27
        with Dissolve(1)
        scene day6_areyouwashed_26
        with dissolve
        r1 "我们选择自己创造命运……"
        scene day6_areyouwashed_27
        with dissolve
        r1 "直到命运决定替我们选。"
        scene day6_areyouwashed_44
        with Dissolve(1)
        pause
        scene day6_areyouwashed_45
        with dissolve
        sophia "不管境况如何……"
        scene day6_areyouwashed_46
        with dissolve
        sophia "我很高兴命运让我们相遇。"
        scene day6_areyouwashed_27
        with Dissolve(1)
        scene day6_areyouwashed_26
        with dissolve
        pause
        scene day6_areyouwashed_47
        with Dissolve(1)
        r1 "我也是。"
        scene day6_areyouwashed_48
        with dissolve
        sophia "很高兴我们聊了这些。"
        sophia "别担心，我会好好照顾[ava]。"
        r1 "谢谢你，[sophia]。"
        r1 "今天有什么计划？"
        sophia "晚点我要带[ava]去林子里。"
        sophia "你今天要做什么？"
        r1 "今晚晚些时候我有个商务会面。"
        r1 "不过我得先去学院。"
        r1 "所以我会在这儿准备能准备的，然后就出发。"
        sophia "商务会面？"
        scene day6_areyouwashed_49
        with Dissolve(1)
        r1 "跟学院有关。"
        scene day6_areyouwashed_50
        with Dissolve(1)
        sophia "只是个平民？"
        scene day6_areyouwashed_49
        with Dissolve(1)
        r1 "对。"
        scene day6_areyouwashed_50
        with Dissolve(1)
        sophia "好。"
        scene day6_areyouwashed_51
        with dissolve
        sophia "只要记住，万一事情不顺利……"
        sophia "或者你哪天需要人手……"
        scene day6_areyouwashed_52
        with dissolve
        sophia "就打给[sophia]。"
        sophia "她待人可能不如以前那么周到了。"
        sophia "但她还是他妈的很棒。"
        scene day6_areyouwashed_53
        with dissolve
        scene day6_areyouwashed_52
        with dissolve
        pause
        play sound "audio/Flash.ogg" volume 0.5
        scene day6_areyouwashed_54
        with flashbulb
        sophia "哪儿都看不到他。"
        scene day6_areyouwashed_55
        with Dissolve(1)
        ingrid "没关系。"
        scene day6_areyouwashed_56
        sophia "你他妈到底在说什么？"
        sophia "我们得掩护他。"
        scene day6_areyouwashed_57
        with Dissolve(1)
        ingrid "他能照顾好自己。"
        ingrid "我们盯着他，就不是在掩护他。" 
        scene day6_areyouwashed_58
        sophia "那我们在这儿干嘛？"
        scene day6_areyouwashed_59
        with Dissolve(1)
        r1 "我也不知道是什么情况，但别出声。"
        r1 "只说必要的话。我们的通讯器关不掉。"
        scene day6_areyouwashed_60
        with Dissolve(1)
        ingrid "{i}Zophia{/i}，这是城区。"
        ingrid "街面上的敌对目标他能应付。"
        ingrid "你是观察手。还记得{i}我说的{/i}吗。"
        ingrid "{i}窗户{/i}。屋顶。楼房。那些才是{i}应该{/i}盯的地方。"
        ingrid "如果他需要直接火力支援，{i}我{/i}会提供。"
        ingrid "{i}否则，{/i}我们是在保护他不受{i}他看不见的东西{/i}伤害。"
        scene day6_areyouwashed_61
        with Dissolve(1)
        pause
        scene day6_areyouwashed_62
        with Dissolve(1)
        pause
        scene day6_areyouwashed_60
        with Dissolve(1)
        ingrid "{i}Zophia{/i}，{i}风向？{/i}"
        scene day6_areyouwashed_62
        with Dissolve(1)
        sophia "每秒两米，东南风。"
        scene day6_areyouwashed_60
        with Dissolve(1)
        ingrid "对。但只有东南不够。"
        scene day6_areyouwashed_61
        with Dissolve(1)
        sophia "每秒两米，来自十一点钟方向。"
        scene day6_areyouwashed_63
        with Dissolve(1)
        ingrid "Gut."
        ingrid "现在到你十点钟方向。三楼。"
        ingrid "看到那道反光了吗？"
        scene day6_areyouwashed_62
        with Dissolve(1)
        sophia "看到了。"
        scene day6_areyouwashed_60
        with Dissolve(1)
        ingrid "那是瞄准镜。"
        ingrid "这就是为什么你的位置要尽可能高的原因之一。"
        ingrid "路灯会在你的瞄准镜上反光，暴露你的位置。"
        ingrid "联系他，确认目标。"
        scene day6_areyouwashed_64
        with Dissolve(1)
        sophia "亲爱的。可能是个带瞄准镜的俄国人。"
        sophia "我们合同目标那栋楼的四楼。"
        r1 "{i}我抬不了那么高看。{/i}"
        r1 "{i}你们俩确定？{/i}"
        scene day6_areyouwashed_61
        with Dissolve(1)
        sophia "确定吗？"
        scene day6_areyouwashed_60
        with Dissolve(1)
        ingrid "我确定。"
        scene day6_areyouwashed_64
        with Dissolve(1)
        sophia "确定。"
        sophia "[ingrid]在请求你的许可，要动手了。"
        r1 "{i}动手。{/i}"
        scene day6_areyouwashed_79
        play sound "audio/snipershot.ogg"
        pause
        scene day6_areyouwashed_80
        with dissolve
        sophia "你回来以后，一起喝一杯？"
        scene day6_areyouwashed_18
        with Dissolve(1)
        r1 "哦？我现在能喝酒了？"
        scene day6_areyouwashed_80
        with dissolve
        sophia "不过只能给你一杯无酒精啤酒。"
        scene day6_areyouwashed_18
        with Dissolve(1)
        r1 "求你了……干脆直接杀了我算了？"
        scene day6_areyouwashed_81
        with dissolve
        sophia "你在耍我吗？"
        scene day6_areyouwashed_18
        with dissolve
        r1 "很好笑是吧？"
        scene day6_areyouwashed_81
        with Dissolve(1)
        pause
        scene day6_areyouwashed_82
        with dissolve
        sophia "我当初何必给你缝针。"
        scene day6_areyouwashed_18
        with dissolve
        r1 "要是我不缝，你就没笑话可听了。"
        scene day6_areyouwashed_83
        with dissolve
        sophia "性事我会怀念……笑话？"
        sophia "那倒不会。"
        scene day6_areyouwashed_18
        with Dissolve(1)
        pause
        scene day6_areyouwashed_84
        with dissolve
        r1 "你在笑我吗？"
        scene day6_areyouwashed_83
        with Dissolve(1)
        pause
        scene day6_areyouwashed_85
        with dissolve
        pause
        scene day6_areyouwashed_86
        with Dissolve(1)
        sophia "*咯咯笑* 我走了！"
        sophia "趁我还没真给你一巴掌。"
        scene day6_areyouwashed_87
        with Dissolve(1)
        sophia "再见啦，亲爱的！"
        r1 "什么？连个吻都没有？"
        sophia "再见啦，爱你哦！"
        r1 "*轻笑* 再见，亲爱的。"
        scene day6_areyouwashed_87_1
        with Dissolve(1)
        sophia "哦！对了，我走之前。关于那个 RTI 的事。"
        sophia "你还记得你教过我我们这行的哪一条吗？"
        scene day6_areyouwashed_87_2
        with Dissolve(1)
        sophia "永远把最后一颗子弹留给自己。"
        sophia "谁都别想活捉我。"
        scene day6_areyouwashed_91
        with Dissolve(1)
        play sound "audio/open4.ogg"
        pause
        scene day6_areyouwashed_90
        with Dissolve(2)
        pause
        scene day6_areyouwashed_92
        with Dissolve(2)
        pause
        scene day6_areyouwashed_93
        with Dissolve(2)
        pause
        play sound "audio/handgunslide2.ogg" volume 0.5
        scene day6_areyouwashed_94
        pause
        stop music fadeout 3
        stop music2 fadeout 3
        scene black
        with Dissolve(2)
        pause
        
        
        
    label day6_lilainthepool:
        play music2 "audio/soundtrack/Ambiance/pool1.ogg" volume 0.9
        scene day6_lilainthepool_1
        with Dissolve(2)
        pause
        lila "*沉重的喘息*"
        scene day6_lilainthepool_2
        with Dissolve(2)
        lila "*沉重的喘息*"
        scene day6_lilainthepool_3
        with dissolve
        lila "你还差十秒……"
        scene day6_lilainthepool_4
        with Dissolve(1)
        r1 "是吗？"
        scene day6_lilainthepool_5
        with hpunch
        pause
        scene day6_lilainthepool_6
        with hpunch
        lila "你怎么老这么安静？！"
        lila "你在那儿站了多久了？！"
        scene day6_lilainthepool_4
        with Dissolve(1)
        pause
        scene day6_lilainthepool_7
        with dissolve
        r1 "安静……？"
        r1 "我不觉得……"
        scene day6_lilainthepool_8
        with dissolve
        r1 "你大概是太专注了，没听见我过来。"
        r1 "我知道你会在这儿。我要单独跟你谈谈。"
        scene day6_lilainthepool_9
        with Dissolve(2)
        lila "跟……我单独谈？"
        lila "出什么事了吗？"
        scene day6_lilainthepool_10
        with Dissolve(1)
        r1 "什么事？"
        scene day6_lilainthepool_11
        with dissolve
        r1 "哦……"
        r1 "没有。没什么事。"
        scene day6_lilainthepool_12
        with Dissolve(2)
        r1 "我想也许可以请你帮我点……更私人的忙。"
        scene day6_lilainthepool_13
        with Dissolve(1)
        pause
        scene day6_lilainthepool_14
        with dissolve
        pause
        scene day6_lilainthepool_15
        with dissolve
        lila "当然，老师。随时都行！"
        lila "我能帮你什么？"
        scene day6_lilainthepool_16
        with Dissolve(1)
        r1 "别叫「老师」。我……"
        r1 "这次不是那种谈话。"
        r1 "我今天不是以校长的身份来的。"
        r1 "我说了……这是私事……"
        scene day6_lilainthepool_17
        with Dissolve(1)
        pause
        scene day6_lilainthepool_18
        with Dissolve(1)
        pause
        scene day6_lilainthepool_17
        with Dissolve(1)
        pause
        scene day6_lilainthepool_19
        with Dissolve(1)
        pause
        scene day6_lilainthepool_20
        with Dissolve(1)
        lila "我在这里……"
        scene day6_lilainthepool_21
        with Dissolve(1)
        lila "你确定没事吗？你好像有什么在困扰你。"
        scene day6_lilainthepool_22
        with Dissolve(1)
        r1 "确实有一点。"
        r1 "是关于你朋友的事。我希望这场谈话能只有我们两个人知道，好吗？"
        scene day6_lilainthepool_23
        with Dissolve(1)
        pause
        scene day6_lilainthepool_24
        with Dissolve(1)
        pause
        scene day6_lilainthepool_23
        with Dissolve(1)
        pause
        scene day6_lilainthepool_25
        with hpunch
        lila "*咳嗽* 当、当然！"
        scene day6_lilainthepool_26
        lila "等等……我的{b}朋友{/b}？"
        lila "什么朋友？"
        scene day6_lilainthepool_22
        with Dissolve(1)
        r1 "[asu]。"
        scene day6_lilainthepool_27
        with Dissolve(1)
        lila "她怎么了？"
        scene day6_lilainthepool_22
        with Dissolve(1)
        r1 "我今晚要跟她吃饭。跟我们之前那次差不多。"
        scene day6_lilainthepool_28
        with hpunch
        lila "差、差不多？！"
        scene day6_lilainthepool_22
        with Dissolve(1)
        r1 "嗯……也不完全是。她会在一家公开的餐厅见我，而不是在她家。"
        r1 "她说她知道一家餐厅，但到现在都没告诉我。"
        scene day6_lilainthepool_29
        with Dissolve(1)
        r1 "得看那家餐厅在城市的哪个位置，我得做一些准备。"
        r1 "太多事情不在我掌控之中，而我不喜欢这样。"
        r1 "我在想能不能请你帮我处理一下。"
        scene day6_lilainthepool_30
        with Dissolve(1)
        pause
        lila "哦……"
        scene day6_lilainthepool_29
        with Dissolve(1)
        pause
        scene day6_lilainthepool_31
        with Dissolve(1)
        lila "哦——"
        scene day6_lilainthepool_32
        with dissolve
        lila "*咯咯笑* 你是怕被人看见跟学生在一起吗？"
        scene day6_lilainthepool_33
        with Dissolve(1)
        pause
        scene day6_lilainthepool_34
        with Dissolve(1)
        r1 "是担心。"
        scene day6_lilainthepool_33
        with Dissolve(1)
        r1 "这是两码事。"
        scene day6_lilainthepool_36
        with Dissolve(1)
        lila "当、当然。"
        lila "至少这次是在外面见……"
        scene day6_lilainthepool_37
        with Dissolve(1)
        lila "那样……大概比较安全……"
        scene day6_lilainthepool_33
        with Dissolve(1)
        r1 "对谁安全？"
        scene day6_lilainthepool_36
        with Dissolve(1)
        lila "什么意思？"
        scene day6_lilainthepool_22
        with Dissolve(1)
        r1 "没什么。只是随口说说。对不起。"
        r1 "最近脑子里事太多，理不清楚。"
        scene day6_lilainthepool_38
        with Dissolve(1)
        pause
        scene day6_lilainthepool_39
        with Dissolve(1)
        lila "别担心，好吗？"
        lila "我会帮你的。"
        scene day6_lilainthepool_40
        with Dissolve(1)
        lila "不过我得说……你好像有跟学生搞「非正式约会」的毛病。"
        scene day6_lilainthepool_41
        with Dissolve(1)
        r1 "*轻笑* 嗯？是吗？"
        r1 "也许我该改改了。"
        scene day6_lilainthepool_44
        with Dissolve(1)
        lila "只要你……偶尔为我破个例……"
        scene day6_lilainthepool_41
        with Dissolve(1)
        r1 "*轻笑* 如果你给我有用的建议……"
        scene day6_lilainthepool_43
        with dissolve
        r1 "那我也许会。"
        scene day6_lilainthepool_42
        with dissolve
        lila "那么……我能帮你什么？"
        lila "你到底在「担心」什么？"
        scene day6_lilainthepool_22
        with Dissolve(1)
        r1 "她有跟你说过我们在哪儿见面吗？"
        scene day6_lilainthepool_36
        with Dissolve(1)
        lila "没有，我……甚至不知道你们俩要见面。"
        lila "不过我可以帮你打听一下。"
        scene day6_lilainthepool_22
        with Dissolve(1)
        r1 "不用。她既然没说，那就别打听了。"
        r1 "听着，我是认识[asu]，可……"
        r1 "但我在这个学院之外，并不了解她是个什么样的女孩。"
        scene day6_lilainthepool_33
        with Dissolve(1)
        r1 "有什么我该知道的吗？有什么我该留意的？"
        scene day6_lilainthepool_42
        with Dissolve(1)
        pause
        scene day6_lilainthepool_45
        with Dissolve(1)
        lila "拜托，我们说的是[asu]啊。"
        scene day6_lilainthepool_43
        with dissolve
        r1 "我知道。只是想弄清楚该有个什么心理准备。"
        scene day6_lilainthepool_42
        with Dissolve(1)
        lila "我的意思是……"
        lila "听着，[asu]是我的朋友。我爱她。"
        lila "*轻笑* 她有时候有点争强好胜，触及这点时挺烦的，但我还是爱她。"
        lila "她父亲大概是在推她去商界积累些经验。仅此而已。"
        scene day6_lilainthepool_22
        with Dissolve(1)
        r1 "她父亲？"
        lila "对！我是说……"
        lila "对他来说你是认真的吧？" 
        scene day6_lilainthepool_49
        with Dissolve(1)
        r1 "没错。"
        scene day6_lilainthepool_46
        with Dissolve(1)
        pause
        scene day6_lilainthepool_47
        with Dissolve(1)
        lila "听着，如果是那样，她只是第一步，对吧？"
        lila "你只要留下好印象就行。"
        scene day6_lilainthepool_48
        with Dissolve(1)
        lila "而且我得说，你在她那儿开局已经很不错了。"
        scene day6_lilainthepool_49
        with Dissolve(1)
        r1 "是吗？"
        scene day6_lilainthepool_50
        with Dissolve(1)
        lila "你疯了吗？你们打架那天，她一个字都没说。"
        scene day6_lilainthepool_49
        with Dissolve(1)
        r1 "我不觉得那对她来说是什么大事。"
        scene day6_lilainthepool_48
        with Dissolve(1)
        lila "*轻笑* 就像我说的。她{b}确实{/b}有点争强好胜。"
        lila "不过放轻松，你已经做得很好了。"
        lila "再说了……你们又不是敌人，对吧？这不是打架。"
        scene day6_lilainthepool_50
        with dissolve
        lila "这更像是……像是……"
        scene day6_lilainthepool_48
        with dissolve
        lila "拜托，帮我说下去。"
        scene day6_lilainthepool_49
        with Dissolve(1)
        r1 "像跳舞？"
        scene day6_lilainthepool_50
        with dissolve
        lila "像跳舞……？"
        scene day6_lilainthepool_48
        lila "等等！像{b}跳舞{/b}！对，太完美了！"
        lila "所以，呃……你们俩更像是……在跳舞！"
        lila "你们偶尔会踩到对方的脚。"
        lila "但最后你们还是搭档，对吧？"
        lila "你们还是在{b}一起跳舞{/b}。"
        scene day6_lilainthepool_49
        with Dissolve(1)
        pause
        scene day6_lilainthepool_43
        with dissolve
        r1 "这个说法不错。"
        r1 "谢谢。"
        scene day6_lilainthepool_48
        with Dissolve(1)
        lila "嗯……你确实来求我帮忙了！"
        scene day6_lilainthepool_50
        with dissolve
        lila "看来在我父母身边长大还是学到了一些东西。"
        scene day6_lilainthepool_49
        with Dissolve(1)
        pause
        scene day6_lilainthepool_51
        with dissolve
        r1 "*轻笑*"
        scene day6_lilainthepool_52
        with dissolve
        r1 "很难想象你穿着泳装时的样子。"
        scene day6_lilainthepool_53
        with Dissolve(1)
        lila "那你干脆{b}自己{/b}穿泳装好了！我帮你看办公室！"
        scene day6_lilainthepool_51
        with dissolve
        r1 "哈！也许你真该！"
        scene day6_lilainthepool_54
        with Dissolve(1)
        lila "太好了！那样我们就能改成吃晚饭了！"
        lila "话说回来……既然说到这个……"
        lila "你可是答应过要把这里重新好好经营起来的。"
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "我现在不就在做吗。"
        scene day6_lilainthepool_56
        with Dissolve(1)
        pause
        scene day6_lilainthepool_57
        with Dissolve(1)
        lila "哦……"
        lila "原来如此，那我就懂了。好主意。"
        r1 "什么好主意？"
        scene day6_lilainthepool_45
        with Dissolve(1)
        lila "哦，没什么！没事！"
        scene day6_lilainthepool_58
        with Dissolve(1)
        r1 "嗯。"
        scene day6_lilainthepool_59
        with dissolve
        r1 "你提到她父亲。你觉得他可能会来吃饭吗？"
        scene day6_lilainthepool_60
        with Dissolve(1)
        lila "嗯……对[asu]来说，很难讲。"
        lila "老实说，我觉得她不会愿意。"
        lila "她有说你们怎么去那家餐厅吗？她开车送你？"
        scene day6_lilainthepool_59
        with Dissolve(1)
        r1 "嗯，没有。她还没说什么。"
        r1 "我们提过的具体细节，大概只有牛排什么的。别的就真没说了。"
        scene day6_lilainthepool_49
        with Dissolve(1)
        r1 "总之，这跟她父亲有什么关系？"
        scene day6_lilainthepool_60
        with Dissolve(1)
        lila "嗯……我们出去逛街时，她父亲送过她很多次。"
        lila "说不定他也可以……照样送她？当作见见你的借口？"
        scene day6_lilainthepool_50
        with dissolve
        lila "等等，这说不通……他见你根本不需要借口。"
        lila "呃……我不知道。"
        scene day6_lilainthepool_60
        with Dissolve(1)
        lila "也许我们想太多了？"
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "*轻笑* 我觉得你们确实想多了。"
        scene day6_lilainthepool_60
        with Dissolve(1)
        lila "好吧，我们退一步说。"
        lila "她有跟你说过她父亲的事吗？"
        scene day6_lilainthepool_49
        with Dissolve(1)
        r1 "没有。"
        scene day6_lilainthepool_61
        with Dissolve(1)
        lila "*叹气*"
        scene day6_lilainthepool_62
        with dissolve
        lila "这就是[asu]。"
        scene day6_lilainthepool_59
        with Dissolve(1)
        r1 "她应该告诉我吗？"
        scene day6_lilainthepool_61
        with Dissolve(1)
        lila "那事……有点复杂。"
        scene day6_lilainthepool_63
        with dissolve
        lila "总之，别想太多了。"
        lila "我相信你和他会相处融洽。"
        lila "不过听着，如果你真想留下好印象，一定要准时到。"
        lila "守时在她那儿很重要。"
        scene day6_lilainthepool_34
        with Dissolve(1)
        r1 "守时？"
        scene day6_lilainthepool_63
        with Dissolve(1)
        lila "我知道，我知道。但她确实非常看重这个。"
        lila "她父亲也是。"
        lila "大概是家族作风吧。" 
        scene day6_lilainthepool_34
        with Dissolve(1)
        r1 "嗯……日本人的作风？"
        scene day6_lilainthepool_50
        with Dissolve(1)
        lila "算是吧，但也不全是。你看，亚苏娜有……一半日本血统。她是在这儿长大的。"
        scene day6_lilainthepool_63
        with Dissolve(1)
        lila "我是说……看看我。我家有德国血统。可我完全不懂他们的文化。"
        lila "听着，她可不是传统的日本女人。有她父亲在，情况就完全不一样了。"
        lila "要那样谈论亚苏娜……还挺难开口的。"
        scene day6_lilainthepool_45
        with Dissolve(1)
        lila "*咯咯笑* 我真没想到我居然会给出怎么应付她的建议。"
        scene day6_lilainthepool_46
        with Dissolve(1)
        pause
        scene day6_lilainthepool_64
        with Dissolve(1)
        pause
        scene day6_lilainthepool_65
        with Dissolve(1)
        pause
        scene day6_lilainthepool_66
        with Dissolve(1)
        lila "*咯咯笑* 有一条很重要！千万别鞠躬，明白吗？"
        lila "我知道前两天那场切磋你们互相鞠过躬，但那就留在垫子上吧。"
        lila "你要是那样做，她不会认真对待你。除非你想让她每隔一分钟就拿这事开玩笑，否则别做。"
        r1 "日本人之间不互相鞠躬吗？"
        lila "是啊，会！但你不是日本人！所以别太刻意。"
        r1 "那不是表示尊敬的方式吗？"
        lila "我……大概吧？我想确实可以这么理解。"
        lila "但在有些人看来，那也可能像是嘲弄，对吧？"
        lila "还是别过头为好。"
        scene day6_lilainthepool_67
        with Dissolve(1)
        lila "唔唔……"
        lila "呃……"
        scene day6_lilainthepool_68
        with dissolve
        lila "哦！我在电影里见过这一幕。"
        lila "假设你正在见一位俄罗斯企业家。"
        lila "见面之前他可能会给你们俩各倒一杯伏特加，对吧？" 
        lila "而拒绝的话就很失礼。"
        scene day6_lilainthepool_67
        with Dissolve(1)
        lila "我觉得挺像的，不是吗？"
        lila "你就让这些事自然发生就好。"
        scene day6_lilainthepool_68
        with Dissolve(1)
        lila "比如……我第一次去她家时，她说进屋前得把鞋脱在外面。"
        lila "如果这对她真的那么重要，她会比你先说。"
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "*轻笑* 我觉得俄罗斯那个比方挺贴切的。"
        scene day6_lilainthepool_68
        with Dissolve(1)
        lila "对吧？！"
        lila "我的意思是，我也不知道这是真的还是我们从电影里看来的。"
        lila "说不定鞠躬也是这一类！"
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "*轻笑* 不过有些事电影里确实处理得比较温和。"
        r1 "但我懂你的意思。"
        r1 "有没有什么可以算作不尊重或失礼的事？说不定哪天用得上。"
        
        scene day6_lilainthepool_68
        with dissolve
        lila "嗯……也许我学到过一些。"
        lila "进屋之前要脱鞋。"
        lila "给客人倒饮料要先于给自己倒……"
        lila "哦！要是你们去日本餐厅，别用筷子指人！"
        lila "还有不管怎样，别把筷子插进米饭里！"
        scene day6_lilainthepool_69
        with dissolve
        lila "*咯咯笑* 我在她们家干过一次。她父亲把我训了一整通，而[asu]就坐在那儿憋着不笑。"
        scene day6_lilainthepool_70
        with dissolve
        lila "所以，是的。那事你别做。"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "嗯。训了你一通？"
        scene day6_lilainthepool_70
        with dissolve
        lila "那个……我可能稍微……有那么一点点夸张。"
        lila "他只是……很平静地生气。"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "平静地？"
        scene day6_lilainthepool_67
        with dissolve
        lila "平静地？平静地？谁在乎啊！"
        lila "也许用「克制」更合适？"
        scene day6_lilainthepool_68
        with dissolve
        lila "呃……我不知道。我想说的是，他确实是个非常佛系的人。"
        lila "他佛得我后背都发凉。你懂我的意思吧？"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "也许我懂。"
        scene day6_lilainthepool_70
        with Dissolve(1)
        lila "我敢肯定，跟在我家吃的那顿完全不一样。"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "你什么意思？"
        scene day6_lilainthepool_68
        with Dissolve(1)
        lila "首先……我母亲不会在。"
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "*轻笑* 你母亲没那么糟。"
        scene day6_lilainthepool_68
        with Dissolve(1)
        lila "哦，对。那不是你整晚都在听她盘问。"
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "*轻笑* 真的？"
        scene day6_lilainthepool_67
        with Dissolve(1)
        lila "好——吧……我们现在别聊这个了，行吗？"
        scene day6_lilainthepool_68
        with dissolve
        lila "回到[asu]吧。你现在是不是自在多了？"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "嗯。"
        r1 "听着，我不是在说跟她见面让我不自在。"
        r1 "那本身没什么问题。说到她父亲也一样。"
        r1 "但我不喜欢不知道自己会面对什么。"
        r1 "就是一顿晚饭吗？她想聊什么特别的事吗？我需要留意什么吗？"
        r1 "就是这类顾虑。"
        scene day6_lilainthepool_68
        with Dissolve(1)
        lila "哦，不会。[asu]有时候可能确实那样。但她更像是……"
        lila "像是……嗯，我也不知道。她没跟我说过什么。不过也许以后会。"
        lila "她就那样。什么事都憋着，直到最后一刻。"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "真的吗？"
        scene day6_lilainthepool_68
        with Dissolve(1)
        lila "真的！我的意思是，我们之间一般不瞒着对方。"
        scene day6_lilainthepool_28
        with hpunch
        lila "我是说……"
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "*轻笑* 是啊。希望至少有一个秘密你不会告诉我。"
        scene day6_lilainthepool_25
        with hpunch
        lila "当、当然会。"
        scene day6_lilainthepool_72
        with dissolve
        lila "嗯……"
        scene day6_lilainthepool_73
        with dissolve
        lila "[asu]这个人吧……通常都是自己做决定。"
        lila "然后再去问信任的人，看看这个主意好不好。你懂我的意思吧？"
        scene day6_lilainthepool_72
        with dissolve
        lila "我该怎么说呢……呃……"
        scene day6_lilainthepool_68
        with dissolve
        lila "我觉得她不知道前天晚上你来了我家。"
        lila "除非她跟我母亲聊过。有时候她们会聊。"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "她们会聊天？"
        scene day6_lilainthepool_68
        with dissolve
        lila "哦，会啊。自从[asu]开始给她父亲做事之后聊得更多了。"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "聊什么？"
        scene day6_lilainthepool_68
        with dissolve
        lila "*咯咯笑* 你不好奇吗？"
        lila "比如给点建议之类的？我也不知道。"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "类似某种指导关系？"
        scene day6_lilainthepool_68
        with dissolve
        lila "*咯咯笑* 指导？不是的，才不是那种！"
        scene day6_lilainthepool_69
        with dissolve
        lila "抱歉，你说得好像她是正在培训的绝地武士。"
        scene day6_lilainthepool_68
        with dissolve
        lila "不，更像是呃……"
        lila "我不知道。你从来没向朋友请教过吗？"
        lila "朋友之间有时候会聊聊想法。她们两个都关心政治和商业。"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "我明白了。"
        r1 "所以她确实有可能知道我们一起吃了饭？"
        scene day6_lilainthepool_68
        with dissolve
        lila "我……大概吧？不好说。"
        lila "反正也无所谓。就算她只是有点直觉，那又有什么区别？"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "我只是想确认她可能会掌握什么样的信息。"
        scene day6_lilainthepool_73
        with dissolve
        lila "那她知道和我们一起吃过饭，有什么问题吗？"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "你说过她很好胜。"
        scene day6_lilainthepool_69
        with dissolve
        lila "*轻笑* 我觉得她在这事上不会较劲！"
        scene day6_lilainthepool_68
        with dissolve
        lila "哦！不过她可能对我母亲先请了你有点不高兴。"
        lila "我是说……不是真的不高兴……" 
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "*轻笑* 更像是友好竞争。懂了。"
        scene day6_lilainthepool_68
        with dissolve
        lila "对！我母亲确实会催[asu]一把。"
        scene day6_lilainthepool_73
        with dissolve
        lila "我想这样能让她们保持……警觉？"
        scene day6_lilainthepool_68
        with dissolve
        lila "其实真的能！确实能让她们保持警觉！"
        lila "就像你跟我比赛那次。它让我想更努力训练！"
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "这个待会儿再说。"
        scene day6_lilainthepool_68
        with dissolve
        lila "对！我也要来求你帮忙了！"
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "*轻笑* 真的？"
        scene day6_lilainthepool_68
        with dissolve
        lila "当然！你以为我的建议是白给的吗？我可不随便给人！"
        scene day6_lilainthepool_55
        with Dissolve(1)
        r1 "*轻笑* 那么，还有另一条很棒的建议吗？"
        scene day6_lilainthepool_68
        with Dissolve(1)
        lila "*咯咯笑* 我想没有了！"
        lila "我的意思是，放轻松！只要你能有跟我们在一起时一半的优雅表现，你就没问题！"
        scene day6_lilainthepool_71
        with Dissolve(1)
        r1 "谢谢你，[lila]。"
        scene day6_lilainthepool_74
        with Dissolve(1)
        lila "不客气！"
        if lila_coach_you == True:
            scene day6_lilainthepool_75
            with dissolve
            lila "既然我帮了你……我也想要你帮个忙！"
            scene day6_lilainthepool_76
            with Dissolve(1)
            pause
            scene day6_lilainthepool_77
            with dissolve
            r1 "*轻笑* 好吧……什么事？"
            scene day6_lilainthepool_75
            with Dissolve(1)
            pause
            scene day6_lilainthepool_78
            with dissolve
            lila "我的圈速还差十秒才达标。" 
            lila "我一百米的配速还是一分半。"
            lila "按我的竞技标准，这还是太慢了。"
            scene day6_lilainthepool_76
            with Dissolve(1)
            r1 "你为什么这么想？"
            scene day6_lilainthepool_78
            with Dissolve(1)
            lila "因为就是太慢了！"
            scene day6_lilainthepool_78
            pause
            lila "你自己说要指导我的。你应该知道那个配速不够快。"
            scene day6_lilainthepool_79
            with Dissolve(1)
            r1 "听着……你可能给自己压力太大了。"
            r1 "我理解你很沮丧。"
            r1 "但现在先别盯着数字不放，好吗？"
            r1 "我们还有更重要的事要操心。"
            scene day6_lilainthepool_78
            with Dissolve(1)
            lila "但这个很重要！"
            scene day6_lilainthepool_79
            with Dissolve(1)
            r1 "好吧，我们退一步。跟你说件事。"
            r1 "你知道有些消防员为了通过 CPAT，得在百米内跑进两分钟吗？"
            scene day6_lilainthepool_80
            with Dissolve(1)
            lila "CPAT 是什么？"
            scene day6_lilainthepool_81
            with Dissolve(1)
            r1 "别太担心这个。"
            r1 "那是职业消防员的一项体能测试。"
            scene day6_lilainthepool_82
            with Dissolve(1)
            lila "真的？只要两分钟？"
            lila "这……跟我想象的不一样。"
            scene day6_lilainthepool_83
            with Dissolve(1)
            r1 "他们只是按不同的标准来衡量。"
            r1 "可他们照样靠这个救人。速度不是一切。"
            scene day6_lilainthepool_84
            with Dissolve(1)
            lila "等等……这是打算说教吗？"
            scene day6_lilainthepool_85
            with Dissolve(1)
            r1 "*轻笑* 取决于有没有用。"
            scene day6_lilainthepool_84
            with Dissolve(1)
            lila "*憋着笑* 我是认真的。"
            scene day6_lilainthepool_85
            with Dissolve(1)
            r1 "我想说的是……还有更大的图景。"
            scene day6_lilainthepool_84
            with Dissolve(1)
            lila "我知道有！但我又不是在救人……"
            lila "我是想赢过对手的配速。"
            scene day6_lilainthepool_83
            with Dissolve(1)
            r1 "如果你不学会放松，两样都做不到。"
            r1 "听着，你刚才还说让我放轻松。你自己也该这么做。"
            scene day6_lilainthepool_81
            with dissolve
            r1 "你追这个成绩追了多久了？"
            scene day6_lilainthepool_86
            with Dissolve(1)
            lila "六个月……我一开始是两分钟的配速。"
            lila "我进步了，但是……现在感觉像是停滞了……"
            lila "有些日子我甚至觉得自己在倒退。"
            scene day6_lilainthepool_87
            with Dissolve(1)
            r1 "我看出是怎么回事了。"
            r1 "你没给身体适应的时间。"
            scene day6_lilainthepool_86
            with Dissolve(1)
            lila "你什么意思？我当然得努力训练！"
            scene day6_lilainthepool_87
            with Dissolve(1)
            r1 "你当然得。但练得太狠，最终还是会把自己练垮。你必须让身体休息。"
            scene day6_lilainthepool_86
            with Dissolve(1)
            lila "什么？"
            scene day6_lilainthepool_87
            with Dissolve(1)
            r1 "对。就是这样。"
            r1 "努力并不总是等于进步。"
            scene day6_lilainthepool_88
            with Dissolve(1)
            lila "这说不通。如果我不逼自己达到那个配速，就永远到不了！"
            scene day6_lilainthepool_87
            with Dissolve(1)
            r1 "听着……进步不是线性的——"
            scene day6_lilainthepool_89
            with Dissolve(1)
            r1 "*叹气* 算了。你在这儿等我一下。"
            lila "你要去哪儿？"
            r1 "在这儿等一秒。我马上回来。"
            scene black
            with Dissolve(2)
            pause
            scene day6_lilainthepool_90
            with Dissolve(2)
            pause
            scene day6_lilainthepool_91
            with Dissolve(1)
            pause
            scene day6_lilainthepool_90
            with Dissolve(1)
            pause
            scene day6_lilainthepool_92
            with Dissolve(1)
            pause
            scene day6_lilainthepool_93
            with hpunch
            lila "你要干什么？！"
            scene day6_lilainthepool_94
            with Dissolve(1)
            r1 "好教练要以身作则，对吧？"
            r1 "想着我们可以一起验证一下那个「别太拼命」的理论。"
            play audio "audio/movingthroughwater1.ogg" volume 0.5
            scene day6_lilainthepool_95
            with Dissolve(1)
            r1 "再说了……有时候最好的指导是亲手示范。"
            scene day6_lilainthepool_96
            with Dissolve(1)
            lila "亲、亲手？"
            scene day6_lilainthepool_97
            with Dissolve(1)
            r1 "你来不来？"
            scene day6_lilainthepool_98
            with Dissolve(1)
            lila "好吧……"
            play audio "audio/movingthroughwater1.ogg" volume 0.5
            scene day6_lilainthepool_99
            with Dissolve(1)
            lila "……什么事？"
            r1 "听着。我不是最好的游泳者。但我还懂一点运动。"
            r1 "而人们想把某项运动练好时，问题在于他们练得太狠，忘了最重要的一部分。"
            scene day6_lilainthepool_100
            with dissolve
            lila "也就是……？"
            r1 "让你的身体和大脑都休息。"
            r1 "恢复来自休息。身体就是在那个时候变强的。"
            r1 "你的成绩本来变好过，后来才变差的，对吧？"
            lila "对……？"
            scene day6_lilainthepool_101
            with dissolve
            r1 "你进步了，但身体一直在垮掉，而你不让它恢复。现在反而退步了。"
            r1 "这跟你刚才说亚苏娜的是一回事。别太拼命。"
            lila "那我该怎么办？"
            r1 "你需要不时调整训练内容。"
            r1 "训练里我们管这叫周期化。讲究的是更聪明地练，而不是更拼命地练。"
            r1 "既然配速已经提升了，接下来练耐力。"
            scene day6_lilainthepool_102
            with dissolve
            lila "我的耐力？"
            r1 "对，我过来的时候你已经气喘了。"
            lila "因为我在用力啊！"
            r1 "我知道。放松。"
            r1 "过来。为我漂在水上。"
            lila "漂着？"
            r1 "相信我。我想看看一样东西。"
            scene day6_lilainthepool_103
            with Dissolve(1)
            lila "你是要我……就这么躺在水里？而你就站在旁边？"
            lila "那、那怎么提升速度？"
            scene day6_lilainthepool_104
            with Dissolve(1)
            r1 "好了，别跟你的教练顶嘴。"
            r1 "试一次，好吗？我有骗过你吗？"
            r1 "就想想你当初学游泳和漂在水上的过程，仅此而已。"
            scene day6_lilainthepool_103
            with Dissolve(1)
            pause
            scene day6_lilainthepool_105
            with Dissolve(1)
            lila "天哪……"
            play audio "audio/movingthroughwater1.ogg" volume 0.5
            scene day6_lilainthepool_106
            with Dissolve(1)
            lila "这感觉好尴尬……"
            scene day6_lilainthepool_107
            with Dissolve(1)
            r1 "尽量放松一点。"
            r1 "我要碰你了，好吗？"
            scene day6_lilainthepool_108
            with Dissolve(1)
            lila "碰、碰我？！"
            scene day6_lilainthepool_107
            with Dissolve(1)
            r1 "这有助于建立身心联结。"
            r1 "闭上眼睛，感受一下我要告诉你的东西。"
            scene day6_lilainthepool_108
            with Dissolve(1)
            lila "好……"
            scene day6_lilainthepool_109
            with Dissolve(1)
            menu:
                "触碰她的背。":
                    pass
            scene day6_lilainthepool_110
            with Dissolve(1)
            pause
            scene day6_lilainthepool_111
            with Dissolve(1)
            pause
            r1 "你的背很强壮，但肩膀要放松。"
            lila "我的肩膀？"
            r1 "你太紧绷了。吸满气，然后放松。"
            menu:
                "触碰她的腹部。":
                    pass
            scene day6_lilainthepool_112
            with Dissolve(1)
            r1 "你的核心也很稳。这有助于保持身体姿态，减少阻力。"
            menu:
                "冒险摸一下她的臀部。":
                    scene day6_lilainthepool_113
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_114
                    with hpunch
                    lila "你、你在干什么？！"
                    scene day6_lilainthepool_115
                    with Dissolve(1)
                    r1 "在摸肌肉的不平衡。"
                    r1 "如果你游泳时用的某块主要肌肉明显比其他的弱，其他肌肉就会试图过度代偿。"
                    r1 "这会让你比该有的更早疲劳，动作也会不够流畅。而这还只是最乐观的情况。"
                    lila "那最糟的呢……？"
                    r1 "最糟就是你受伤。"
                    r1 "你要是觉得不自在，我可以停。"
                    scene day6_lilainthepool_116
                    with Dissolve(1)
                    pause
                    play sound "audio/Lockpick_Success.ogg" volume 0.1
                    show screen notifyEx( msg="[lila]的{color=#00ff00}堕落{/color}上升了{color=#00ff00}4{/color}点！" )
                    $corruption_lila+=4
                    lila "呃……不。"
                    lila "我觉得没问题。"
                    
                "让她转过身":
                    pass
            r1 "很好，能请你转个身吗？"
            scene day6_lilainthepool_117
            with Dissolve(1)
            lila "这样？"
            r1 "完美。我扶着你——感觉怎么样？"
            scene day6_lilainthepool_118
            with Dissolve(1)
            lila "有点……紧绷……"
            scene day6_lilainthepool_119
            with Dissolve(1)
            r1 "我在扶着你。试着放松。我不会让你沉下去。"
            lila "那……不完全是我紧绷的原因……"
            r1 "我明白。但听我说。水里的阻力很大，对吧？"
            r1 "你越紧张，浪费的能量就越多。"
            r1 "游泳不只是快不快——还在于省不省力气，对吧？"
            lila "我……觉得有道理。"
            lila "我觉得体力多了就能划更多下。"
            r1 "没错。那就是我们的目标。"
            r1 "当然，这是一项速度很重要的运动。"
            r1 "但没有耐力，你就练不了那么久，也练不出效果。最后是你在限制自己。"
            r1 "这样说能理解吗？"
            lila "我觉得能。"
            r1 "那么……跟我一起想。你太拼了。"
            r1 "你很紧绷——光是为了维持漂浮，肌肉就已经在浪费力气了……"
            r1 "而漂浮本该是你最放松的状态，对吧？"
            r1 "连你的呼吸都在消耗你。看出它们是怎么连在一起的吗？"
            lila "嗯，我想我明白了。"
            r1 "很好。记住——我是你教练，对吧？"
            lila "你、你是。"
            r1 "那我们来练习怎么让你更放松。这也是我存在的意义之一。"
            scene day6_lilainthepool_120
            with Dissolve(1)
            r1 "你是个出色的游泳者。我不是来教你怎么游泳的。"
            r1 "我是来教你怎么在压力下管理自己的。这才是我擅长的。"
            r1 "在比赛里，光会游泳是不够的。"
            lila "嗯，我听人这么说过。"
            r1 "而且确实如此，对吧？"
            r1 "有太多人在自己擅长的事上天赋异禀。"
            r1 "但一到压力下——比赛时，或者被人盯着时——他们就崩了。"
            lila "等等……确实是这样。以前就发生过。"
            r1 "看吧？"
            r1 "你有那个心。我只要指个方向就行。"
            r1 "我可以帮你建立实力，但动力得来自你自己。"
            r1 "你明白我的意思吗？"
            scene day6_lilainthepool_121
            with Dissolve(1)
            pause
            scene day6_lilainthepool_122
            with dissolve
            lila "我在听。"
            scene day6_lilainthepool_120
            with Dissolve(1)
            r1 "很好。现在放松。"
            r1 "感受水流在你周围跳动。"
            r1 "我在这儿扶着你。我不会让你沉下去。"
            scene day6_lilainthepool_123
            with Dissolve(1)
            pause
            scene black with Dissolve(2)
            pause
            scene day6_lilainthepool_124
            with Dissolve(2)
            lila "我不知道你这么会教人。"
            r1 "这么说我更像个实干家而不是老师，不过我觉得自己做得还行。"
            lila "说真的，刚才真挺好玩。"
            scene day6_lilainthepool_125
            with dissolve
            r1 "嗯……你不是我的第一个学生。"
            lila "真的？你以前当过教练？"
            r1 "*轻笑* 当然没有。我是说，不是你想的那种。"
            r1 "我猜，我经常去教那些我在乎的人。"
            scene day6_lilainthepool_126
            with Dissolve(1)
            lila "所以我是个你在乎的人？"
            scene day6_lilainthepool_127
            with Dissolve(1)
            r1 "当然。" 
            scene day6_lilainthepool_128
            with dissolve
            r1 "我在乎我所有的学生。"
            scene day6_lilainthepool_126
            with Dissolve(1)
            lila "所以我只是个学生？那你是在这儿才认识我的？"
            scene day6_lilainthepool_127
            with Dissolve(1)
            r1 "我好像有跟学生「非正式见面」的习惯，记得吗？"
            scene day6_lilainthepool_128
            with dissolve
            r1 "*轻笑* 不过我得说……你确实有点与众不同。"
            scene day6_lilainthepool_126
            with Dissolve(1)
            lila "哦……非常感谢您，善良的先生！"
            lila "我正希望您能注意到我有点不一样呢！"
            scene day6_lilainthepool_129
            with Dissolve(1)
            "你和[lila]相视而笑。"
            scene day6_lilainthepool_130
            with Dissolve(1)
            lila "那么……伤势怎么样了？"
            scene day6_lilainthepool_127
            with Dissolve(1)
            r1 "在好转。这儿疼那儿疼的，但我没事。"
            r1 "有靠谱的人照顾我。"
            scene day6_lilainthepool_131
            with Dissolve(1)
            lila "我……不介意多照顾你一点。"
            lila "就是……如果由我来好好照顾你的话。"
            scene day6_lilainthepool_127
            with Dissolve(1)
            pause
            scene day6_lilainthepool_128
            with dissolve
            r1 "*轻笑* 你太厉害了。"
            scene day6_lilainthepool_132
            with Dissolve(1)
            pause
            scene day6_lilainthepool_133
            with dissolve
            pause
            scene day6_lilainthepool_134
            with dissolve
            lila "谢谢……"
            lila "那天我真的很担心你。"
            scene day6_lilainthepool_135
            with Dissolve(1)
            r1 "我知道。那不是我想要的……对不起。"
            scene day6_lilainthepool_136
            with Dissolve(1)
            lila "别傻了。要是我知道你受伤了，我绝对不会扑上去。"
            scene day6_lilainthepool_135
            with Dissolve(1)
            r1 "我知道。我只是不想让你承担这个。"
            scene day6_lilainthepool_137
            with Dissolve(1)
            pause
            scene day6_lilainthepool_138
            with Dissolve(1)
            lila "我……其实不介意你多让我承担一点。"
            scene day6_lilainthepool_139
            with Dissolve(1)
            pause
            scene day6_lilainthepool_140
            with hpunch
            pause
            scene day6_lilainthepool_141            
            lila "我、我的意思是！我不介意照顾你！"
            scene day6_lilainthepool_142
            lila "不！我是说……我是说……"
            scene day6_lilainthepool_128
            with Dissolve(1)
            r1 "*轻笑* 放松，莱拉……我懂你的意思。"
            menu:
                "把手覆在莱拉的手上。":
                    scene day6_lilainthepool_143
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_144
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_145
                    with dissolve
                    pause
                    scene day6_lilainthepool_128
                    with Dissolve(1)
                    r1 "我们不该在这里谈这些。"
                    play sound "audio/Lockpick_Success.ogg" volume 0.1
                    show screen notifyEx( msg="[lila]的{color=#00ff00}好感{/color}提升了{color=#00ff00}4{/color}点！" )
                    $love_lila+=4
                    scene day6_lilainthepool_146 
                    with Dissolve(1)
                    lila "我……知道。"
                    scene day6_lilainthepool_147
                    with dissolve
                    pause
                    scene day6_lilainthepool_146
                    with dissolve
                    lila "你什么时候再来我家？"
                    scene day6_lilainthepool_148
                    with Dissolve(1)
                    r1 "那要看你父母会不会请我了。"
                    scene day6_lilainthepool_146
                    with Dissolve(1)
                    lila "嗯……是吗？"
                    scene day6_lilainthepool_148
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_149
                    with dissolve
                    r1 "你在想什么？"
                    scene day6_lilainthepool_150
                    with Dissolve(1)
                    lila "哦！没什么！"
                    scene day6_lilainthepool_149
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_148
                    with dissolve
                    r1 "*轻笑* 是啊……"
                    scene day6_lilainthepool_150
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_151
                    with dissolve
                    pause
                    scene day6_lilainthepool_152
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_151
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_153
                    with Dissolve(1)
                    lila "你能在这儿真好。"
                    scene day6_lilainthepool_148
                    with dissolve
                    r1 "我也是。"
                    scene day6_lilainthepool_154
                    with Dissolve(1)
                    "[lila]亲了亲你的脸颊。"
                    scene day6_lilainthepool_155
                    with Dissolve(2)
                    pause
                "搂住莱拉。":
                    scene day6_lilainthepool_156
                    with hpunch
                    pause
                    scene day6_lilainthepool_157
                    with Dissolve(2)
                    pause
                    scene day6_lilainthepool_160
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_161
                    with dissolve
                    r1 "我们不该在这里谈这些。"
                    scene day6_lilainthepool_157
                    with Dissolve(1)
                    play sound "audio/Lockpick_Success.ogg" volume 0.1
                    show screen notifyEx( msg="[lila]的{color=#00ff00}堕落{/color}上升了{color=#00ff00}4{/color}点！" )
                    $corruption_lila+=4
                    lila "我……知道。"
                    scene day6_lilainthepool_162
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_158
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_159
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_163
                    with Dissolve(1)
                    lila "你什么时候再来我家？"
                    scene day6_lilainthepool_161
                    with Dissolve(1)
                    r1 "那得看你父母欢不欢迎我。"
                    scene day6_lilainthepool_163
                    with Dissolve(1)
                    lila "是吗……？"
                    scene day6_lilainthepool_161
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_160
                    with dissolve
                    r1 "你在想什么？"
                    scene day6_lilainthepool_159
                    with Dissolve(1)
                    lila "哦！没什么！"
                    scene day6_lilainthepool_160
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_161
                    with dissolve
                    r1 "*轻笑* 对哦……"
                    scene day6_lilainthepool_163
                    with Dissolve(1)
                    lila "你来了真好。"
                    scene day6_lilainthepool_161
                    with Dissolve(1)
                    r1 "我也是。"
                    scene day6_lilainthepool_164
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_152
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_164
                    with Dissolve(1)
                    pause
                    scene day6_lilainthepool_154
                    with Dissolve(1)
                    "[lila]亲了亲你的脸颊。"
                    scene day6_lilainthepool_155
                    with Dissolve(2)
                    pause
        hide screen notifyEx with dissolve
        stop music2 fadeout 2    
        scene black with Dissolve(2)
        pause
        
        
        
    label day6_thedinner:
        scene day6_thedinner_1
        with Dissolve(2)
        pause
        scene day6_thedinner_2
        with Dissolve(2)
        r2 "我们还有一堆文件要处理。"
        r1 "嗯？"
        r2 "文件啊。它不会自己走流程的。"
        r1 "那可以等。"
        r2 "今晚那顿饭——你想太多了。"
        r1 "也许吧。"
        r1 "总得有人想。"
        play sound "audio/beep.mp3"
        scene day6_thedinner_3
        with Dissolve(1)
        pause
        scene day6_thedinner_4
        with Dissolve(1)
        r2 "你最好收下这个。"
        scene day6_thedinner_5
        with Dissolve(1)
        pause
        scene day6_thedinner_6
        with Dissolve(1)
        pause
        nvl clear
        nvl_narrator "[asu]的聊天"
        asu_nvl "嗨——老师！" 
        asu_nvl "在忙吗？"
        menu:
            "看看她的头像。":
                scene asu_pfp
                with dissolve
                pause
            "继续聊天。":
                pass
        scene day6_thedinner_6
        r1_nvl "你不是该在上课吗？"
        asu_nvl "呜！就这样？:("
        r1_nvl "什么意思？"
        asu_nvl "哦，没什么！"
        asu_nvl "对啊，我在上商务课 :D"
        asu_nvl "我很确定我们已经讲过，我还有更要紧的事要操心 ;]"
        asu_nvl "而且"
        asu_nvl "我是在这儿谈生意！✨"
        scene day6_thedinner_8
        with Dissolve(1)
        pause
        scene day6_thedinner_9
        with Dissolve(1)
        pause
        scene day6_thedinner_10
        with Dissolve(1)
        r2 "别看我。顺着说就行。"
        scene day6_thedinner_6
        with Dissolve(1)
        r1_nvl "你还想说什么？"
        asu_nvl "当然！"
        asu_nvl "我们今晚有约，记得吗？;D"
        r1_nvl "没什么细节当然容易忘。"
        asu_nvl "诶！我们说好了吃牛排的！"
        asu_nvl "还是什么吧……我也不太确定 D:"
        asu_nvl "抱歉让你一直焦虑"
        r1_nvl "焦虑？"
        asu_nvl "你不焦虑吗？"
        r1_nvl "我该焦虑吗？"
        asu_nvl "那当然，因为我焦虑啊！"
        r1_nvl "？"
        asu_nvl "我已经饿了！;]"
        scene day6_thedinner_8
        with Dissolve(1)
        pause
        scene day6_thedinner_10
        with Dissolve(1)
        r2 "她在耍我们呢。" 
        scene day6_thedinner_9
        with Dissolve(1)
        r1 "那还用你说。"
        scene day6_thedinner_10
        with Dissolve(1)
        r2 "诶，别怪传话的。" 
        scene day6_thedinner_6
        with Dissolve(1)
        r1_nvl "那牛排听着不错"
        r1_nvl "只要你别像上次那样把肉怼我脸上。"
        asu_nvl "lol"
        asu_nvl "你还记得那事？"
        r1_nvl "也许。"
        r1_nvl "所以，你有想去的店吗？"
        asu_nvl "哦对了！说到这个 :D" 
        asu_nvl "我给咱们找到了一家超棒的店" 
        asu_nvl "你会爱上的！" 
        asu_nvl "其实是我父亲推荐的！" 
        scene day6_thedinner_11
        with Dissolve(1)
        pause
        scene day6_thedinner_12
        with Dissolve(0.5)
        pause
        scene black
        with Dissolve(1)
        scene day6_thedinner_13
        with Dissolve(1)
        r1_nvl "我不知道你父亲也掺和进来了。"
        scene day6_thedinner_14
        with dissolve
        "{color=#FF007F}[asu]{/color}咯咯笑了。"
        scene day6_thedinner_13
        with dissolve
        "商务教授" "谈判者有哪几种类型？"
        "商务教授" "有人吗？"
        "商务教授" "[asu]？"
        scene day6_thedinner_15
        with Dissolve(1)
        asu "什么事？哦。"
        "商务教授" "抱歉，我的课打扰到你了。"
        asu "完全没有，老师。我只是用手机记笔记快一点。"
        "商务教授" "那我想你大概知道我问题的答案了。"
        asu "哦……我算是比较安静的学生。"
        "商务教授" "我知道你是谁，[asu]。你要是再翘我的课，这门课就挂了。"
        "商务教授" "我的学生在这儿时，我要他们回答我的问题。"
        "商务教授" "既然你不听讲，那你也许该回家待着。"
        asu "可我在听啊。"
        "商务教授" "那我在等。谈判者有哪几种类型？"
        asu "这得看你参照哪本文献。早期的是说谈判者分四类：催化型、控制型、支持型和分析型。"
        asu "较新的则说有五类：竞争型、合作型、战略型、创新型和问题解决型。"
        asu "你还能找到别的说法，有的说只有三类，有的说超过二十类。不过如今学界的共识是五种。"
        scene day6_thedinner_15
        pause
        "商务教授" "..."
        "商务教授" "这个……正确。"
        asu "所以……我能继续用手机记笔记吗？对我而言这样效率更高。"
        "商务教授" "嗯。当然可以。"
        scene day6_thedinner_16
        with dissolve
        asu "谢谢。"
        scene day6_thedinner_13
        with Dissolve(1)
        asu_nvl "别担心，他不会来的。" 
        asu_nvl "看来你只能跟他的女儿相处了。"
        scene day6_thedinner_17
        with Dissolve(1)
        pause
        scene day6_thedinner_18
        with Dissolve(1)
        pause
        scene day6_thedinner_17
        with Dissolve(1)
        pause
        scene day6_thedinner_13
        with Dissolve(1)
        asu_nvl "最后这段我们就别传出去了，好吗？" 
        scene day6_thedinner_6
        with Dissolve(1)
        r1_nvl "我以为本来就没有别人知道。"
        asu_nvl "本来就没人知道！"
        asu_nvl "我是说，除了我父亲，没人知道这件事。"
        asu_nvl "除非你已经告诉了别人。"
        r1_nvl "你父亲不介意？"
        asu_nvl "一开始就是他帮我安排好的。"
        asu_nvl "别再说我父亲了，求你了。"
        asu_nvl "总之，你一般几点吃晚饭？" 
        r1_nvl "我时间灵活，你方便就行。"
        asu_nvl "太好了！有想去的店吗？"
        r1_nvl "我以为你已经有你父亲推荐的店了。"
        asu_nvl "哈哈哈"
        asu_nvl "有的！"
        asu_nvl "不过我以为你会有自己的想法"
        asu_nvl "是我们在吃晚饭，不是我父亲。"
        asu_nvl "我找到一个超棒的地方！"
        r1_nvl "那到底是哪儿呢？"
        asu_nvl "啊，对！我差点忘了！"
        asu_nvl "要的话我可以送你去！"
        r1_nvl "[asu]，我只需要餐厅的地址。"
        r1_nvl "我没事的。"
        asu_nvl "其实我……现在还不知道地址"
        asu_nvl "不过在城东那边。"
        scene day6_thedinner_9
        with Dissolve(1)
        pause
        scene day6_thedinner_10
        with Dissolve(1)
        r2 "城东是三不管地带。"
        r2 "我们应该没事。不用叫人。"
        scene day6_thedinner_9
        with Dissolve(1)
        r1 "嗯。"
        scene day6_thedinner_6
        with Dissolve(1)
        r1_nvl "我觉得挺好。"
        r1_nvl "只要记得准时把地址发给我。"
        asu_nvl "绝对不会！"
        asu_nvl "好！回头聊！"
        r1_nvl "什么？"
        asu_nvl "回头聊！"
        scene day6_thedinner_8
        with Dissolve(1)
        pause
        r1 "*叹气* 也许我干这行太老了。"
        scene day6_thedinner_10
        with Dissolve(1)
        r2 "不，我们只是压力太大。"
        r2 "你既然不打算做完文件，我们干脆回家准备今晚的事吧。"
        scene day6_thedinner_8
        with Dissolve(1)
        r1 "*叹气* 嗯，我想我就这么办吧。"
        scene day6_thedinner_9
        with Dissolve(1)
        r1 "你觉得呢？"
        scene day6_thedinner_10
        with Dissolve(1)
        r2 "我觉得我们会没事的。"
        r2 "我们经历过更糟的。"
        r2 "不过有几个点挺有意思。"
        scene day6_thedinner_9
        with Dissolve(1)
        r1 "比如？"
        scene day6_thedinner_10
        with Dissolve(1)
        r2 "她为什么要主动提到她父亲也参与其中？"
        r2 "好等下再找借口推掉？图什么？"
        scene day6_thedinner_9
        with Dissolve(1)
        r1 "有些人就是嘴太松……"
        scene day6_thedinner_10
        with Dissolve(1)
        r2 "[asu]像是会犯这种口误的人吗？"
        scene day6_thedinner_9
        with Dissolve(1)
        r1 "她确实嘴挺不严的。不过我明白你的意思。"
        r1 "你觉得他掺和得有多深？"
        scene day6_thedinner_10
        with Dissolve(1)
        r2 "这不重要。不管他有没有参与，我们都没准备好迎接又一个玩家登场。"
        r2 "我们得假定他参与了。"
        r2 "一个小姑娘在这一切里能有多大权力？"
        r2 "毕竟那是她父亲的公司。"
        scene day6_thedinner_9
        with Dissolve(1)
        pause
        scene day6_thedinner_2
        with Dissolve(2)
        pause
        scene day6_thedinner_1
        with Dissolve(2)
        pause
        scene black
        with Dissolve(2)
        pause
        scene day6_thedinner_19
        with Dissolve(2)
        isa "你恢复得{b}非常{/b}快。"
        isa "看你这么活蹦乱跳，我很惊讶我的缝线居然还撑得住。"
        scene day6_thedinner_20
        with Dissolve(1)
        sophia "亲爱的，你压根儿就不知道。"
        scene day6_thedinner_21
        with dissolve
        sophia "而且那可是{b}我的{/b}缝线，非常感谢。"
        scene day6_thedinner_22
        with Dissolve(1)
        pause
        scene day6_thedinner_23
        with dissolve
        isa "*咯咯笑* 对！我也很惊讶{b}你的{/b}缝线居然没掉。"
        scene day6_thedinner_24
        with Dissolve(1)
        pause
        scene day6_thedinner_25
        with dissolve
        sophia "嗯……乖一点，也许我就让你见识见识我的技术！"
        scene day6_thedinner_27_2
        with Dissolve(1)
        pause
        scene day6_thedinner_27
        with Dissolve(0.5)
        isa "创伤外科医生……"
        scene day6_thedinner_26
        with Dissolve(1)
        r1 "今天那些缝线{b}绝不能{/b}裂开。"
        scene day6_thedinner_27_3
        with Dissolve(1)
        isa "嗯……你的伤口愈合得不错。"
        scene day6_thedinner_27_4
        with Dissolve(1)
        isa "我{b}可以{/b}把线拆了……但那样伤口重新裂开的概率会变大。"
        scene day6_thedinner_27_5
        with Dissolve(0.5)
        pause
        scene day6_thedinner_19
        with Dissolve(1)
        sophia "最好还是别拆，亲爱的。"
        scene day6_thedinner_24
        with Dissolve(1)
        sophia "你今天要去哪儿？"
        scene day6_thedinner_26
        with Dissolve(1)
        r1 "城东。"
        scene day6_thedinner_21
        with Dissolve(1)
        sophia "那就好。缝线没问题。"
        scene day6_thedinner_28
        with Dissolve(1)
        isa "……这完全说不通。"
        scene day6_thedinner_25
        with Dissolve(1)
        sophia "那是我的一点迷信。"
        scene day6_thedinner_29
        with Dissolve(1)
        pause
        scene day6_thedinner_30
        with dissolve
        pause
        scene day6_thedinner_31
        with dissolve
        isa "什么……？这是英国或者欧洲那边的讲究吗？" 
        isa "我完全听不懂。" 
        scene day6_thedinner_26
        with Dissolve(1)
        r1 "*咂* 城东很清净。我就不用堵在路上好几个小时了。"
        scene day6_thedinner_32
        with Dissolve(1)
        isa "哦！对。我还在熟悉这边的路。"
        scene day6_thedinner_25
        with Dissolve(1)
        sophia "别太在意我说的话，亲爱的。"
        sophia "我是在逗你。"
        scene day6_thedinner_27_2
        with Dissolve(1)
        isa "*咯咯笑* 好吧……我完全不知道那是什么意思。"
        scene day6_thedinner_32
        with Dissolve(1)
        isa "不过现在懂了。座椅的摩擦可能会让伤口重新裂开。"
        isa "所以尽量避免。你大概应该——"
        scene day6_thedinner_33
        ava "你什么时候回来？"
        scene day6_thedinner_26
        with Dissolve(1)
        pause
        r1 "不知道。"
        scene day6_thedinner_33
        with Dissolve(1)
        ava "我会等你。"
        scene day6_thedinner_34
        with Dissolve(1)
        pause
        scene day6_thedinner_35
        with dissolve
        sophia "亲爱的，不就是一顿饭吗。"
        scene day6_thedinner_33
        with Dissolve(1)
        pause
        scene day6_thedinner_36
        with dissolve
        pause
        scene day6_thedinner_26
        with Dissolve(1)
        pause
        r1 "[ava]，看着我。"
        scene day6_thedinner_37
        with Dissolve(1)
        pause
        scene day6_thedinner_38
        with dissolve
        pause
        scene day6_thedinner_26
        with Dissolve(1)
        r1 "我会没事的。"
        r1 "我不在的时候，你照顾好[sophia]。"
        scene day6_thedinner_40
        sophia "嘿！我是什么，小孩子吗？"
        scene day6_thedinner_41
        r1 "你也要照顾好[isa]。"
        scene day6_thedinner_42
        isa "嘿，哇！我是什么，软柿子吗？"
        scene day6_thedinner_39
        with Dissolve(1)
        "{color=#FF007F}[sophia]{/color}和{color=#FF007F}[isa]{/color}轻轻笑了一下。"
        scene day6_thedinner_43
        with dissolve
        pause
        scene day6_thedinner_37
        with Dissolve(1)
        ava "我……"
        scene day6_thedinner_44
        with Dissolve(1)
        ava "既然要有东西吃，我最好去做饭了。"
        scene day6_thedinner_45
        with Dissolve(1)
        isa "[ava]……"
        scene day6_thedinner_26
        with Dissolve(1)
        play sound "audio/open4.ogg"
        r1 "伊莎贝拉，你能先陪艾娃一会儿吗？"
        scene day6_thedinner_46
        with Dissolve(1)
        isa "好、好的……当然。"
        scene day6_thedinner_47
        with Dissolve(1)
        pause
        scene day6_thedinner_48
        with dissolve
        sophia "嘿，你能顺手把门带上吗，亲爱的？"
        isa "当然！"
        sophia "谢谢！"
        scene day6_thedinner_26
        with Dissolve(1)
        play sound "audio/open4.ogg"
        pause
        scene day6_thedinner_49
        with Dissolve(1)
        pause
        scene day6_thedinner_50
        with dissolve
        sophia "那么。"
        scene day6_thedinner_53
        with Dissolve(1)
        pause
        scene day6_thedinner_52
        with Dissolve(1)
        pause
        scene day6_thedinner_51
        with Dissolve(1)
        sophia "情况怎么样？"
        scene day6_thedinner_52
        with Dissolve(1)
        r1 "我还在等地址。不过她选了城东跟我见面。"
        sophia "她？"
        r1 "一个学生。"
        sophia "明白。你猜为什么吗？"
        r1 "变量太多了，没法给出有根据的推测。"
        r1 "简单说是因为那是城里的高档区。但我不能确定那是{b}唯一{/b}的原因。"
        sophia "嗯……至少城东是中立地界，不是吗？"
        r1 "是的。不用叫人。"
        sophia "这样也安全一点。"
        sophia "这姑娘有多重要？你为什么要见她？"
        scene day6_thedinner_54
        with Dissolve(1)
        r1 "这……说起来太长了。"
        r1 "我可能需要她帮个忙。"
        r1 "但那所该死的学院有个问题，[sophia]：我要应付的可不只是学生。"
        r1 "每一步都有人在盯着。"
        scene day6_thedinner_51
        with Dissolve(1)
        sophia "好吧……"
        sophia "听起来有点——"
        scene day6_thedinner_54
        r1 "我知道这听起来像什么。"
        r1 "警察局长的儿子就在那所学院。"
        r1 "你明白我一直在跟什么样的人打交道吗？"
        scene day6_thedinner_51
        with Dissolve(1)
        sophia "明白……"
        sophia "所以……是他们的父母，不是孩子。"
        scene day6_thedinner_54
        r1 "他们的父母，不是孩子。"
        r1 "她家在警方和市政厅都有关系。我不知道有多深。"
        r1 "她父亲有人脉和财力。是我见过最多的。"
        scene day6_thedinner_51
        with Dissolve(1)
        sophia "你说的资源是指什么？"
        scene day6_thedinner_52
        with Dissolve(1)
        r1 "她父亲出钱养着警方。"
        scene day6_thedinner_51
        with Dissolve(1)
        sophia "多少钱？"
        scene day6_thedinner_52
        with Dissolve(1)
        r1 "几百万。"
        scene day6_thedinner_51
        with Dissolve(1)
        pause
        scene day6_thedinner_55
        with Dissolve(0.5)
        sophia "我靠。"
        scene day6_thedinner_56
        with Dissolve(0.5)
        sophia "你要是愿意，我可以趁你吃饭的时候查查她。"
        sophia "我能给你查出她扎实的底细，让你用得上。"
        scene day6_thedinner_52
        with Dissolve(1)
        r1 "不用。"
        r1 "现在不是跟她结怨的时候。"
        r1 "我更想先多个盟友。"
        scene day6_thedinner_51
        with Dissolve(1)
        sophia "所以你就这么不带武器去？"
        scene day6_thedinner_52
        with Dissolve(1)
        r1 "我理解这为什么让你担心。"
        r1 "但我这是从长远考虑。"
        r1 "要是真查到什么，我多半会拿来用。"
        r1 "那会改变我对她的看法。甚至连说话方式都会变。"
        r1 "我宁可装成去吃顿饭的无辜家伙，也不想冒险把她推到对立面。"
        r1 "现在就走勒索这条路，我觉得我就再也没有这个选项了。"
        scene day6_thedinner_51
        with Dissolve(1)
        sophia "那要是这姑娘不想结盟呢？"
        scene day6_thedinner_57
        with Dissolve(1)
        r1 "那我就相应地对付她。"
        r1 "在别人眼里，我只是个在学校打工的人。"
        r1 "我要是每次都表现得不寻常，人们就会开始起疑。"
        r1 "比起他们已经在问的那些问题，更多。"
        r1 "所以，是的。我冒着「不带武器」的风险去。但我觉得长期来看这样更好。"
        scene day6_thedinner_51
        with Dissolve(1)
        sophia "不管怎样我都站你这边。"
        sophia "有需要就给我们打电话。"
        scene day6_thedinner_56
        with Dissolve(0.5)
        sophia "那么……关于她和警方的关系……"
        scene day6_thedinner_57
        with Dissolve(1)
        r1 "我可以再推测一步：这大概是她选那个地方的最大原因。"
        r1 "她可能知道也可能不知道这座城市的分区。但警方知道。"
        scene day6_thedinner_56
        with Dissolve(1)
        sophia "其实不只如此。城里最高档的地方也在那儿。"
        sophia "她要是那么有钱，那大概也是她最熟悉的区域。"
        sophia "要资金吗？我可以——"
        scene day6_thedinner_57
        r1 "不用。"
        scene day6_thedinner_56
        with Dissolve(1)
        sophia "好、好吧……"
        scene day6_thedinner_58
        with Dissolve(0.5)
        sophia "嗯……"
        scene day6_thedinner_59
        with Dissolve(0.5)
        sophia "等等。你说她还没把地址告诉你？"
        scene day6_thedinner_57
        with Dissolve(1)
        r1 "对。"
        scene day6_thedinner_59
        with Dissolve(1)
        sophia "有原因吗？"
        scene day6_thedinner_57
        with Dissolve(1)
        r1 "她父亲是这座城市权力圈子里的大人物。"
        r1 "我不清楚他具体是什么人，也不清楚他具体做什么。"
        r1 "但瞥见他女儿一眼，我就能大致判断出这个人。"
        r1 "我得利用这顿饭更好地弄清整件事。"
        scene day6_thedinner_58
        with Dissolve(1)
        sophia "那就是又一个需要盯着的权力人物。"
        scene day6_thedinner_57
        with Dissolve(1)
        r1 "又是一张可能直接连到我们这个世界的势力网。"
        r1 "老实说，现在这不在我的顾虑范围内。稍微被算计一下我还应付得来。"
        r1 "我更担心的是地点。现在没那么担心了。"
        scene day6_thedinner_58
        with Dissolve(1)
        sophia "听着就不对劲。我不喜欢。"
        sophia "见面之前我们该先摸清底细。"
        scene day6_thedinner_57
        with Dissolve(1)
        r1 "你还记得[l]吗？"
        r1 "关于他们父母的情报，我需要的就是她帮忙。"
        r1 "我会跟她再深入聊聊。这里面有文章。"
        r1 "而且就我对这姑娘的这点了解，我干这行时见过更糟的人。"
        scene day6_thedinner_59
        with Dissolve(1)
        sophia "你觉得今晚你自己应付得来吗？"
        scene day6_thedinner_57
        with Dissolve(1)
        r1 "我只能打好手里这副牌……"
        r1 "可我现在这牌烂得很。"
        r1 "将就着用现有的吧。"
        scene day6_thedinner_59
        with Dissolve(1)
        sophia "今天我有什么能{b}主动{/b}帮上忙的吗？"
        scene day6_thedinner_57
        with Dissolve(1)
        r1 "谢谢。不用了。"
        r1 "我得维持我的身份。既然不会有安全问题，我想一个人去没问题。"
        scene day6_thedinner_60
        with Dissolve(1)
        sophia "好吧……"
        scene day6_thedinner_61
        with Dissolve(0.5)
        sophia "万一出岔子……就打给[sophia]，好吗？"
        scene day6_thedinner_52
        with Dissolve(1)
        play sound "audio/beep.mp3"
        r1 "我——"
        scene day6_thedinner_27_6
        with Dissolve(1)
        r1 "稍等。"
        scene day6_thedinner_62
        with Dissolve(1)
        nvl_narrator "现在时间：下午5点18分"
        asu_nvl "嗨——！"
        asu_nvl "我拿到地址了。七点怎么样？"
        r1_nvl "晚上好。发过来吧。我会到。"
        asu_nvl "太好了！回见！"
        asu_nvl "哦，抱歉"
        asu_nvl "我忘了"
        asu_nvl "一会儿见！"
        scene day6_thedinner_27_6
        with Dissolve(1)
        r1 "我拿到地址了。"
        r1 "我得换身衣服。"
        scene day6_thedinner_61
        with Dissolve(1)
        sophia "我在楼下等你。"
        scene day6_thedinner_57
        with Dissolve(1)
        r1 "能帮我个忙吗？"
        scene day6_thedinner_61
        with Dissolve(1)
        sophia "随时都行，亲爱的。"
        scene day6_thedinner_57
        with Dissolve(1)
        r1 "帮我看着点艾娃。我知道这对大家压力都很大。"
        r1 "但她还没那么坚强。"
        scene day6_thedinner_61
        with Dissolve(1)
        pause
        scene day6_thedinner_63
        with Dissolve(0.5)
        sophia "我会的。"
        scene day6_thedinner_64
        with Dissolve(1)
        pause
        scene day6_thedinner_65
        with Dissolve(1)
        sophia "你{b}不是{/b}一个人。"
        scene day6_thedinner_66
        with Dissolve(1)
        pause
        scene day6_thedinner_67
        with Dissolve(1)
        pause
        scene day6_thedinner_68
        with Dissolve(1)
        sophia "别又让我把你扛回家。"
        sophia "必要的话我会……但别让我……"
        scene day6_thedinner_64
        with Dissolve(1)
        sophia "我们会没事的。别迟到。"
        sophia "我们等你。"
        scene day6_thedinner_69
        with Dissolve(1)
        sophia "我在楼下。别忘了穿暖和点，亲爱的。"
        sophia "他们说今晚会下雪。"
        scene day6_thedinner_70
        with Dissolve(1)
        pause
        scene day6_thedinner_71
        with Dissolve(1)
        pause
        scene black
        with Dissolve(2)
        pause
        scene day6_thedinner_72
        with Dissolve(2)
        pause
        scene day6_thedinner_73
        with Dissolve(2)
        pause
        scene day6_thedinner_74
        with Dissolve(1)
        r1 "我想就是这里了。"
        scene day6_thedinner_75
        with Dissolve(1)
        r1 "真有意思。我想象中的不太一样。"
        scene day6_thedinner_76
        with Dissolve(2)
        pause
        r1 "挺安静的地方……"
        scene day6_thedinner_77
        with Dissolve(2)
        "???" "先生？"
        scene day6_thedinner_78
        with Dissolve(2)
        r1 "嗯？"
        scene day6_thedinner_79
        with Dissolve(2)
        "女服务员" "抱歉打扰您，先生。我不是有意打扰的。"
        "女服务员" "您是在等人吗？"
        scene day6_thedinner_80
        with Dissolve(1)
        r1 "是的。"
        r1 "请问现在几点了？"
        r1 "我约了七点在这儿见一个人。"
        r1 "预订大概是用我的名字。或者她的。我叫[r1]。"
        scene day6_thedinner_79
        with Dissolve(1)
        "女服务员" "哦！当然。您是阿川小姐的客人。"
        "女服务员" "抱歉。您要不要进来喝点什么，边等边？"
        "女服务员" "今晚外面很冷。"
        scene day6_thedinner_81
        with Dissolve(1)
        r1 "其实我还是在外面等她吧。"
        r1 "能告诉我现在几点吗？"
        scene day6_thedinner_79
        with Dissolve(1)
        "女服务员" "差五分七点，先生。"
        scene day6_thedinner_81
        with Dissolve(1)
        r1 "谢谢。"
        scene day6_thedinner_79
        with Dissolve(1)
        "女服务员" "需要什么的话，叫我就好。"
        scene day6_thedinner_81
        with Dissolve(1)
        r1 "好的，谢谢。"
        scene day6_thedinner_82
        with Dissolve(2)
        pause
        scene day6_thedinner_83
        r1 "等等。"
        scene day6_thedinner_84
        with Dissolve(2)
        "女服务员" "什么事？"
        scene day6_thedinner_85
        with Dissolve(2)
        r1 "这地方一直都这么空吗？"
        scene day6_thedinner_84
        with Dissolve(2)
        "女服务员" "天气原因，先生……今晚我们所有的桌子都被预订了。"
        "女服务员" "我想没人愿意冒着雪在外面等。"
        scene day6_thedinner_85
        with Dissolve(1)
        r1 "我明白了……"
        r1 "好的，谢谢。"
        scene day6_thedinner_84
        with Dissolve(2)
        "女服务员" "不客气，先生。"
        play music "audio/soundtrack/smokeandashes.ogg" volume 0.5 fadein 2
        scene day6_thedinner_86
        with Dissolve(2)
        pause
        scene day6_thedinner_87
        with Dissolve(2)
        pause
        scene day6_thedinner_88
        with Dissolve(2)
        pause
        scene day6_thedinner_89
        r1 "谢谢——"
        r1 "……你？"
        scene day6_thedinner_90
        with Dissolve(2)
        r1 "嗯。"
        r1 "好吧。"
        scene day6_thedinner_91
        with Dissolve(2)
        pause
        play music2 "audio/footsteps1.ogg"
        scene day6_thedinner_92
        with Dissolve(2)
        pause
        stop music2 fadeout 4
        scene day6_thedinner_93
        with Dissolve(2)
        pause
        scene day6_thedinner_94
        with Dissolve(1)
        asu "晚上好，先生。"
        scene day6_thedinner_95
        with Dissolve(1)
        asu "希望没让您等太久。"
        scene day6_thedinner_96
        with Dissolve(1)
        r1 "我刚到。"
        scene day6_thedinner_95
        with Dissolve(1)
        asu "是吗？"
        scene day6_thedinner_97
        with Dissolve(1)
        r1 "是。"
        scene day6_thedinner_98
        with Dissolve(2)
        pause
        scene day6_thedinner_99
        with Dissolve(2)
        pause
        scene day6_thedinner_100
        with Dissolve(1)
        pause
        play sound "audio/Lockpick_Success.ogg" volume 0.1
        show screen notifyEx( msg="[asu]的{color=#00ff00}好感{/color}提升了{color=#00ff00}4{/color}点！" )
        $love_asuna+=4
        
        scene day6_thedinner_101
        with Dissolve(1)
        asu "如今守时可是稀有品质。"
        scene day6_thedinner_102
        with Dissolve(1)
        r1 "我是个大忙人。能做的最少也得是高效利用时间。"
        hide screen notifyEx with dissolve
        scene day6_thedinner_103
        with Dissolve(1)
        asu "*轻笑* 那我很高兴你为我留出了时间。"
        scene day6_thedinner_104
        with Dissolve(1)
        asu "继续在附近转圈吧，弗兰克。"
        asu "我准备回家时给你打电话。"
        play sound "audio/carshut.ogg" volume 0.5
        scene day6_thedinner_105
        with Dissolve(1)
        pause
        scene day6_thedinner_106
        with Dissolve(1)
        asu "说真的。我不想让你干等。"
        r1 "真的没关系。"
        asu "那……好吧。"
        asu "嗯，希望你饿了。这里的菜……简直太棒了！"
        scene day6_thedinner_107
        with Dissolve(1)
        r1 "*轻笑* 饿坏了。"
        scene day6_thedinner_108
        with Dissolve(1)
        r1 "顺便说，你这条裙子很好看。"
        asu "*咯咯笑* 你的也很好看。"
        asu "我是说你的西装。"
        asu "意大利的，对吧？"
        r1 "对。你的呢？"
        asu "不知道。大概是德国的。"
        scene day6_thedinner_109
        with Dissolve(1)
        asu "*轻笑* 但我开始后悔了。今晚太冷了。"
        scene day6_thedinner_110
        with Dissolve(1)
        r1 "*轻笑* 坐在豪车里很容易忘记。"
        scene day6_thedinner_111
        with Dissolve(1)
        asu "哎呀。你还真会让人家女孩子觉得自己很特别呢。"
        asu "不过请别对我妄下断论。"
        scene day6_thedinner_110
        with Dissolve(1)
        r1 "*轻笑* 哦……抱歉。我不是那个意思。"
        r1 "我只是想说看起来挺舒服的。以前没见过。"
        scene day6_thedinner_111
        with Dissolve(1)
        asu "真的吗？"
        asu "需要的话我可以送你回家。"
        scene day6_thedinner_110
        with Dissolve(1)
        r1 "*轻笑* 那就不必了。"
        scene day6_thedinner_112
        with Dissolve(1)
        pause
        scene day6_thedinner_113
        with Dissolve(1)
        asu "真有意思。"
        r1 "怎么了？"
        scene day6_thedinner_114
        with Dissolve(1)
        asu "我还以为你比较习惯坐豪车。"
        scene day6_thedinner_113
        with Dissolve(1)
        r1 "*轻笑* 有人会习惯吗？"
        asu "我会！"
        asu "没什么了不起的。"
        r1 "*轻笑* 也是……"
        r1 "既然标准这么高，下次我开直升机来。"
        asu "哎呀，得了吧。我还以为你见惯了各种人……你毕竟是做那份工作的。"
        scene day6_thedinner_115
        with Dissolve(1)
        r1 "各种人？"
        scene day6_thedinner_116
        with Dissolve(1)
        asu "*咯咯笑* 让你困惑了？"
        asu "你没见过[lila]的母亲吗？"
        asu "政客、艺术家、音乐家。只要出得起我们学院学费的人。"
        asu "我想那里每个人都已经坐过豪车了。"
        asu "也许只有[ch]的父亲没有。因为他开的是坦克。"
        asu "哦，算了。他以前坐过我父亲的豪车。"
        scene day6_thedinner_117
        with Dissolve(1)
        r1 "你父亲的豪车？"
        scene day6_thedinner_116
        with Dissolve(1)
        asu "对！他也有！"
        asu "我母亲也有。"
        asu "不过她从来不用。"
        asu "总之，你见过[ch]的父亲，对吧？"
        scene day6_thedinner_117
        with Dissolve(1)
        r1 "见过。"
        scene day6_thedinner_116
        with Dissolve(1)
        asu "是吗？感觉怎么样？"
        scene day6_thedinner_117
        with Dissolve(1)
        r1 "他直接出现在我家门口。"
        scene day6_thedinner_119
        with Dissolve(1)
        asu "*咯咯笑* 这可真是没礼貌。"
        scene day6_thedinner_117
        with Dissolve(1)
        r1 "是有点。"
        scene day6_thedinner_119
        with Dissolve(1)
        asu "他一向如此。老实说，我最讨厌这种仗势压人。"
        asu "他能查出你住哪儿。那又怎样？"
        asu "你又不是在藏什么。"
        scene day6_thedinner_117
        with Dissolve(1)
        r1 "也是……"
        r1 "你对你那些朋友的事真知道得不少。"
        scene day6_thedinner_120
        with Dissolve(2)
        pause
        scene day6_thedinner_122
        with Dissolve(2)
        pause
        scene day6_thedinner_121
        with Dissolve(2)
        pause
        asu "首先，他们不是我的朋友。"
        asu "*轻笑* 他们没品味。"
        asu "他们就是一群猩猩。"
        asu "看看[ch]就知道了——你应该能猜到我怎么看他父亲。"
        asu "说真的，我一直不明白[lila]看上了他什么。"
        scene day6_thedinner_123
        with Dissolve(1)
        r1 "也许你不该那样议论警察局长。"
        scene day6_thedinner_121
        with Dissolve(1)
        asu "*咯咯笑* 那他能怎么样？"
        scene day6_thedinner_124
        with Dissolve(1)
        asu "得了吧。你仔细看看我。"
        scene day6_thedinner_123
        with Dissolve(1)
        pause
        r1 "我看着呢。"
        scene day6_thedinner_125
        with Dissolve(1)
        asu "我不是不尊重权威。只是我不尊重他的权威。"
        asu "*轻笑* 你和我之间不会有问题的。"
        scene day6_thedinner_126
        with Dissolve(2)
        pause
        scene day6_thedinner_127
        with Dissolve(2)
        pause
        play sound "audio/Flash.ogg" volume 0.5
        scene day6_thedinner_129
        with flashbulb
        grace "[r1]先生，您觉得我的裙子怎么样？"
        play sound "audio/Flash.ogg" volume 0.5
        scene day6_thedinner_127
        with flashbulb
        r1 "嗯。"
        scene day6_thedinner_125
        with Dissolve(1)
        asu "怎么？"
        scene day6_thedinner_130
        with Dissolve(1)
        r1 "即便如此，你在公开场合也不该那样议论他。"
        asu "*轻笑* 你看看这里有人吗？"
        asu "这又不是公开场合。只有你和我。"
        r1 "谁知道呢。"
        r1 "我能问你一件事吗？"
        asu "当然！"
        r1 "是关于你的裙子。"
        asu "哦，又回到这个话题？怎么了？"
        r1 "你说可能是德国的。为什么？"
        asu "是[grace]太太送给我的。她说要紧。"
        r1 "你知道为什么吗？"
        asu "是问她为什么送我，还是问它为什么特别？"
        r1 "都问。"
        asu "*咯咯笑* 她把同一条裙子送给了[lila]和我。"
        asu "[lila]长高了。我没有。所以我一直穿着。"
        asu "至于它为什么特别……我不知道。"
        asu "那你的呢？真的是意大利的？"
        r1 "是。"
        asu "你怎么知道？"
        r1 "卖给我的人当时在做披萨。"
        scene day6_thedinner_132
        with Dissolve(1)
        asu "太好笑了！"
        r1 "*轻笑* 我又不是侦探。"
        r1 "既然你都提到他们了，也许该去问[ch]或者他父亲。"
        scene day6_thedinner_131
        with Dissolve(1)
        asu "呃！不要！"
        scene day6_thedinner_132
        with Dissolve(1)
        asu "光是想到要靠近[ch]我就想吐。"
        asu "上课时我已经够受的了。"
        scene day6_thedinner_133
        with Dissolve(1)
        asu "先生，我一直在想……"
        asu "我能说得直接一点吗？"
        r1 "当然。"
        scene day6_thedinner_134
        with Dissolve(1)
        asu "你怎么看他们？"
        scene day6_thedinner_135
        with Dissolve(1)
        r1 "局长和他儿子？"
        scene day6_thedinner_134
        with Dissolve(1)
        asu "对。"
        scene day6_thedinner_135
        with Dissolve(1)
        r1 "*轻笑* 我不该对他们有看法，[asu]。"
        scene day6_thedinner_134
        with Dissolve(1)
        asu "对身边的人有看法，是我们理所当然的权利。"
        asu "但这不意味着要让它影响工作。"
        asu "你觉得我没法和[ch]一起完成我们的课题吗？"
        asu "*轻笑* 我问的是个人问题。不用写完整评估报告。" 
        scene day6_thedinner_135
        with Dissolve(1)
        r1 "好吧……我跟他们不够熟，无法形成看法。"
        scene day6_thedinner_134
        with Dissolve(1)
        asu "嗯。我还以为你跟他们接触更多。"
        asu "所以，校园里那些警察……"
        scene day6_thedinner_135
        with Dissolve(1)
        r1 "他们惹麻烦了吗？"
        scene day6_thedinner_134
        with Dissolve(1)
        asu "没有……"
        scene day6_thedinner_136
        with Dissolve(1)
        asu "算了。当我没说。"
        scene day6_thedinner_137
        with Dissolve(1)
        r1 "嗯……是你先提起的。我很好奇。"
        r1 "说吧。把话说完。"
        scene day6_thedinner_136
        with Dissolve(1)
        pause
        scene day6_thedinner_139
        with Dissolve(2)
        pause
        scene day6_thedinner_138
        with Dissolve(1)
        asu "真的没什么。"
        r1 "我还是想知道。"
        asu "好吧……那就说。"
        asu "你为什么让他们进校园？"
        r1 "去跟局长作对不是什么明智之举。"
        asu "我想也是……"
        scene day6_thedinner_140
        with Dissolve(1)
        asu "不过你确实完全有权那么做。"
        scene day6_thedinner_142
        with Dissolve(1)
        r1 "我知道。"
        r1 "但我为什么要那么做？就像你说的，我没什么好藏的。"
        asu "*轻笑* 不只是这个原因。"
        r1 "当然不是。"
        r1 "我知道其中的含义。"        
        r1 "但稍微让一步没什么损失，对吧？"
        asu "我想也是。"
        asu "但你担任的是选任职务。"
        asu "人们会说闲话。"
        
        scene day6_thedinner_141
        with Dissolve(1)
        r1 "让他们说去。"
        asu "这……是个有意思的立场。"
        r1 "怎么说？"
        asu "你不该担心一下能不能保住职位吗？"
        r1 "*轻笑* 我担心。但我更担心把工作做好。"
        asu "那不够。"
        scene day6_thedinner_141
        pause
        asu "抱歉……我越界了。"
        
        scene day6_thedinner_138
        with Dissolve(1)
        r1 "不，没关系。我想听。"
        asu "父亲说过，不只是把工作做好。还要让别人相信你最适合。"
        r1 "你觉得这说法对吗？"
        asu "我怎么想不重要。这是事实。"
        asu "你可以做得很好。但如果没人认同你，你就当不上选任职务。"
        
        scene day6_thedinner_141
        with Dissolve(1)
        r1 "*轻笑* 确实。"
        r1 "而毫无理由地跟局长作对、说他没法在安保上临时帮个忙……"
        r1 "……能帮我让他相信我就是合适的人选吗？"
        r1 "有时候，这是在搭桥。"
        r1 "如果为这种小事跟他对着干，他只会更想换掉我，而不是跟我合作。"
        
        scene day6_thedinner_138
        with Dissolve(1)
        asu "这也会让人觉得你好拿捏。"
        r1 "*轻笑* 你不觉得这反而可能是好事？"
        r1 "你不该总想着争夺主导权。适当的退让也很重要。"
        
        scene day6_thedinner_140
        with Dissolve(1)
        asu "嗯。也许吧。"
        asu "但有时候那也是危险的位置。"
        
        
        scene day6_thedinner_142
        with Dissolve(1)
        r1 "*轻笑* 你为什么这么想？"
        asu "因为其中的含义。"
        asu "那里每个人都在争更大的那块。"
        asu "不只是为了自己拿更多。有时是为了确保别人拿得更少。"
        
        scene day6_thedinner_143
        with Dissolve(1)
        asu "我希望你能明白我的意思。"
        scene day6_thedinner_144
        with Dissolve(1)
        asu "今晚我们有很多要谈。但我饿了。开始吧？"
        scene day6_thedinner_145
        with Dissolve(2)
        pause
        scene black
        with Dissolve(2)
        pause
        scene day6_thedinner_147
        with Dissolve(2)
        asu "你觉得呢？"
        r1 "这……跟我预想的有点不一样。"
        scene day6_thedinner_148
        with Dissolve(1)
        asu "真的？你原本以为是什么样？"
        r1 "说实话？日本菜。"
        scene day6_thedinner_149
        with Dissolve(1)
        asu "哇……我没意识到今晚要靠出身来定义我了。"
        scene day6_thedinner_150
        with Dissolve(1)
        r1 "我不是那个意思。"
        asu "我知道。逗你玩的。"
        asu "老实说，这家餐厅是个特别的地方。只是原因可能和你想的不一样。"
        scene day6_thedinner_151
        with Dissolve(1)
        r1 "作为一家特别的餐厅，这儿可真安静。"
        scene day6_thedinner_149
        with Dissolve(1)
        asu "*轻笑* 那可能是我安排的。"
        scene day6_thedinner_152
        with Dissolve(1)
        "女服务员" "打扰了，阿川女士。您的座位准备好了。"
        asu "拜托了，海瑟尔。阿川女士是我母亲。"
        asu "你知道你可以叫我[asu]。"
        "海瑟尔" "好的，小姐……[asu]。"
        scene day6_thedinner_153
        with Dissolve(1)
        asu "总有一天你会习惯的。"
        asu "我们走吧？"
        scene day6_thedinner_152
        with Dissolve(1)
        "海瑟尔" "请跟我来。"
        scene day6_thedinner_154
        with Dissolve(1)
        r1 "你说可能是你安排的，是什么意思？"
        r1 "*轻笑* 你该不会把整家餐厅都包下来了吧？"
        scene day6_thedinner_155
        with Dissolve(1)
        asu "嗯。是的。"
        scene day6_thedinner_156
        with Dissolve(1)
        pause
        r1 "真的？"
        scene day6_thedinner_158
        with Dissolve(1)
        asu "哦，就今晚。就我们两个。"
        scene day6_thedinner_157
        with Dissolve(1)
        pause
        r1 "为什么？"
        scene day6_thedinner_159
        with Dissolve(1)
        asu "因为我想要隐私，不然还能为什么？"
        asu "钱是一种资产。而我们偶尔有奢侈的余地去用。"
        scene day6_thedinner_157
        with Dissolve(1)
        pause
        r1 "嗯。"
        scene day6_thedinner_160
        with Dissolve(2)
        pause
        scene day6_thedinner_161
        with Dissolve(2)
        pause
        scene day6_thedinner_162
        with Dissolve(2)
        "海瑟尔" "这张桌子合您的意吗，[asu]小姐？"
        asu "很好，海瑟尔。谢谢。"
        play sound "audio/gettinupchair.ogg"
        scene day6_thedinner_163
        with Dissolve(1)
        asu "哦？谢谢你！"
        asu "你真有绅士风度。"
        r1 "*轻笑* 有时候。心情好的时候。"
        scene day6_thedinner_164
        with Dissolve(1)
        "海瑟尔" "需要为您点杯饮品吗，阿川……亚苏娜小姐？"
        scene day6_thedinner_165
        with Dissolve(1)
        asu "*轻笑* 你该问问那位绅士，海瑟尔。"
        scene day6_thedinner_166
        with Dissolve(1)
        "海瑟尔" "好的。抱歉。"
        scene day6_thedinner_167
        with Dissolve(1)
        "海瑟尔" "先生，您想喝点什么吗？"
        r1 "你们有什么？"
        "海瑟尔" "您想喝什么都可以，先生。葡萄酒、气泡水、软饮……"
        r1 "给我们一点时间想想。准备好了我会叫你。"
        "海瑟尔" "好的，先生。"
        scene day6_thedinner_168
        with Dissolve(2)
        pause
        scene day6_thedinner_169
        with Dissolve(2)
        asu "我很喜欢你帮我拉开椅子安排座位的样子。"
        asu "我父亲也这样。他不喜欢背对入口。"
        scene day6_thedinner_170
        with Dissolve(1)
        r1 "我敢说，他是个有意思的人。"
        scene day6_thedinner_169
        with Dissolve(1)
        pause
        asu "是。"
        scene day6_thedinner_171
        with Dissolve(1)
        r1 "你说这家餐厅很特别。"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "我说过。"
        scene day6_thedinner_171
        with Dissolve(1)
        r1 "为什么？"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "哦，是个有意思的故事。"
        scene day6_thedinner_172
        with Dissolve(0.5)
        asu "你知道这里以前是黑帮谈判的地方吗？"
        asu "差不多就像黑手党那样。"
        scene day6_thedinner_169
        with Dissolve(0.5)
        asu "*轻笑* 这座城市见过的东西真多，挺有意思的。"
        asu "有时感觉离我们的现实非常遥远。"
        asu "我无法想象这个地方、这片街区会有那种人。"
        scene day6_thedinner_171
        with Dissolve(1)
        pause
        scene day6_thedinner_173
        with Dissolve(1)
        r1 "真有意思。"
        scene day6_thedinner_169
        with Dissolve(0.5)
        asu "是吧？"
        
        scene day6_thedinner_174
        with Dissolve(0.5)
        r1 "这么空的餐厅，换了别人肯定要说这是场谋杀陷阱。"
        scene day6_thedinner_172
        with Dissolve(1)
        asu "*咯咯笑* 你对黑手党又了解多少？"
        scene day6_thedinner_173
        with Dissolve(1)
        pause
        scene day6_thedinner_174
        with Dissolve(0.5)
        r1 "*轻笑* 嗯。我看过一次《教父》。"
        scene day6_thedinner_169
        with Dissolve(0.5)
        asu "好片子。"
        asu "那今天这里没有警察队长真是谢天谢地。"
        scene day6_thedinner_172
        with Dissolve(0.5)
        asu "不过我得说，你要是去上厕所，我可就开跑了。"
        scene day6_thedinner_174
        r1 "哈！"
        scene day6_thedinner_176
        with Dissolve(0.5)
        r1 "你搞反了。"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "*轻笑* 我想象不出你跑步的样子。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "怎么？你没看过我的腿有多长吗？"
        r1 "我跑步很在行。"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "你肯定有两百磅重。你是很多种人。我可不觉得跑步厉害是其中之一。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "哦？还想再赌一次？"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "*轻笑* 免了。上次之后可不行。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "*轻笑* 说得好。"
        r1 "嗯……看来那场比赛我太投入了。"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "那引出不少问题呢。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "是吗？什么问题？"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "*轻笑* 你可能不知道，我不是在炫耀。"
        asu "但我是四届世界冠军。"
        asu "青年组两个团体冠军，女子组一个团体冠军，外加一个个人冠军。"
        asu "我从没见过有人像你这样打架。也许只有我父亲例外。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "你真这么觉得？我只是碰巧以前看过你的招式——"
        scene day6_thedinner_278
        asu "打住。"
        asu "别说了。但你这种虚假的谦虚让我很烦。"
        asu "而且这不适合你。"
        asu "格斗的人一眼就能认出彼此。"
        asu "我从没见过你参加任何赛事。但我知道你打过。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "*轻笑* 好吧，你赢了。"
        r1 "不过你为什么会这么说？"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "听着，有的格斗士靠力量，有的靠速度，有的就是学得快。"
        asu "可老师您三招就把我放倒了。"
        asu "三……招……"
        asu "所以请您别再这样了。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "*轻笑* 好吧。好吧。对不起。"
        r1 "我不是故意要冒犯你，也不是要说你们没那么强。"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "谢谢。"
        asu "也抱歉，我不该说得那么冲。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "你有你的骄傲，我理解。没事了。"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "不过我告诉你个秘密。"
        asu "女生们那天聊了很多。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "但你不提？"
        scene day6_thedinner_169
        with Dissolve(1)
        pause
        scene day6_thedinner_193
        with Dissolve(1)
        asu "我那时候有更……要紧的事。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "是吗？"
        scene day6_thedinner_193
        with Dissolve(1)
        asu "嗯……"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "得帮[ju]搭她的 D&D 战役。"
        
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "*轻笑* 是啊。我敢说她从没想过会有你这样的朋友。"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "哦……"
        asu "*轻笑* 我觉得是你搞反了。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "怎么说？"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "我从没想过会有[ju]这样的朋友。"
        scene day6_thedinner_176
        with Dissolve(1)
        pause
        scene day6_thedinner_193
        with Dissolve(1)
        asu "这种双重生活有时候……挺累的。"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "双重生活？"
        scene day6_thedinner_193
        with Dissolve(1)
        asu "对。我能在她面前更像是……我想成为的那个自己。"
        asu "这跟其余时候不一样……那时候我才是我{b}必须{/b}成为的那个人。"
        scene day6_thedinner_187
        with Dissolve(1)
        asu "不过你懂这种感觉，对吧？"
        scene day6_thedinner_176
        with Dissolve(1)
        r1 "我完全不知道那是什么感觉。"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "我是说……你那儿可是有很重的伤。我可不信那些针是[isa]给你缝的。"
        asu "而且……你让[ja]担心得不行，记得吗？"
        scene day6_thedinner_177
        with Dissolve(1)
        r1 "那事……很不幸。"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "你知道她喜欢你吗？"
        asu "比她表现出来的要多。"
        scene day6_thedinner_177
        with Dissolve(1)
        r1 "我也喜欢我所有的学生。"
        scene day6_thedinner_169
        with Dissolve(1)
        asu "我相信你是。"
        asu "不过有些人可能会对你的做法有意见。"
        asu "很多人会问，为什么你们俩在自习时间单独待在一栋废弃建筑里。"
        scene day6_thedinner_177
        with Dissolve(1)
        r1 "同样也会有人问，我现在为什么跟一个学生单独吃饭。"
        scene day6_thedinner_178
        with Dissolve(1)
        pause
        scene day6_thedinner_179
        with Dissolve(0.5)
        asu "说起来，我们还没点喝的。"
        scene day6_thedinner_180
        with Dissolve(1)
        pause
        scene day6_thedinner_181
        with Dissolve(1)
        pause
        scene day6_thedinner_177
        with Dissolve(1)
        pause
        scene day6_thedinner_181
        with Dissolve(1)
        asu "对不起……我说错什么了吗？"
        scene day6_thedinner_182
        with Dissolve(1)
        pause
        scene day6_thedinner_183
        with Dissolve(0.5)
        r1 "*咂*"
        scene day6_thedinner_184
        with Dissolve(1)
        r1 "没有。我只是一饿就脾气有点差。"
        scene day6_thedinner_185
        with Dissolve(1)
        asu "天啊！我也是！"
        asu "而且我永远都很饿！"
        scene day6_thedinner_186
        with Dissolve(1)
        r1 "嗯。你想喝点什么？"
        scene day6_thedinner_185
        with Dissolve(1)
        pause
        scene day6_thedinner_187
        with Dissolve(1)
        asu "有什么推荐吗？"
        scene day6_thedinner_186
        with Dissolve(1)
        menu:
            "也许喝葡萄酒。":
                scene day6_thedinner_187
                with Dissolve(1)
                asu "喝葡萄酒挺有意思。只是别让我醉醺醺地回去见父亲。那可不太好看。"
            "气泡水。":
                scene day6_thedinner_187
                with Dissolve(1)
                asu "专业。有格调。我喜欢。"
            "咖啡。":
                scene day6_thedinner_187
                with Dissolve(1)
                asu "第一杯就喝咖啡？我有那么无趣吗？"
            "汽水。":
                $love_asuna+=4
                scene day6_thedinner_187
                with Dissolve(1)
                asu "也对。出去的路上我们还可以顺手买两个热狗。"
            "我不知道……清酒？":
                scene day6_thedinner_187
                with Dissolve(1)
                asu "嗯……这个我有点纠结。我是不是又在被血统定义？"
            "我不是来玩游戏的，亚苏娜。":
                scene day6_thedinner_187
                with Dissolve(1)
                asu "无聊……"
        scene day6_thedinner_186
        with Dissolve(1)
        r1 "那么……正确答案是什么？"
        scene day6_thedinner_187
        with Dissolve(1)
        asu "哦，没有正确答案。我只是想看看你怎么看我。"
        scene day6_thedinner_188
        with Dissolve(1)
        pause
        scene day6_thedinner_189
        with Dissolve(0.5)
        pause
        scene day6_thedinner_187
        with Dissolve(1)
        pause
        if love_asuna > 4:
            play sound "audio/Lockpick_Success.ogg" volume 0.1
            show screen notifyEx( msg="[asu]的{color=#00ff00}好感{/color}增加了{color=#00ff00}4{/color}点！" )
        asu "汽水。"
        scene day6_thedinner_186
        with Dissolve(1)
        r1 "汽水？"
        scene day6_thedinner_187
        with Dissolve(1)
        asu "*轻笑* 我挺喜欢樱桃汽水的。很清爽。"
        asu "但我现在想喝葡萄酒。你觉得呢？"
        scene day6_thedinner_190
        with Dissolve(1)
        pause
        scene day6_thedinner_191
        with Dissolve(1)
        r1 "听起来不错。"
        scene day6_thedinner_190
        with Dissolve(1)
        r1 "不过我不能喝太多。"
        scene day6_thedinner_187
        with Dissolve(1)
        hide screen notifyEx with dissolve
        pause
        asu "我也不能。"
        asu "是因为你的伤口吗？"
        scene day6_thedinner_190
        with Dissolve(1)
        r1 "所以我们才来这儿？就为了聊我的伤口？"
        scene day6_thedinner_187
        with Dissolve(1)
        asu "不是啦，傻瓜。我们是来吃饭的。"
        asu "我正想和我的校长一起喝几杯呢。"
        asu "也许还能聊聊公事。"
        asu "笑一笑……"
        asu "不过如果有失礼的地方，我先道歉。"
        scene day6_thedinner_193
        with Dissolve(1)
        asu "我不是故意的。只是好奇。"
        scene day6_thedinner_192
        with Dissolve(1)
        "黑兹尔" "请问您要点酒水了吗，[asu]小姐？"
        asu "好的。我想尝尝葡萄酒。"
        scene day6_thedinner_193
        with Dissolve(1)
        asu "如果我的……朋友也想一起的话。"
        scene day6_thedinner_194
        with Dissolve(1)
        pause
        scene day6_thedinner_195
        with Dissolve(0.5)
        r1 "有什么推荐吗？"
        scene day6_thedinner_196
        with Dissolve(1)
        "黑兹尔" "我们有一款很棒的波尔多，跟今晚的菜色搭配极好。不过如果您更喜欢白葡萄酒，我们的夏布利也很出色。"
        "黑兹尔" "需要看一下酒单吗？"
        scene day6_thedinner_195
        with Dissolve(1)
        pause
        scene day6_thedinner_197
        with Dissolve(0.5)
        pause
        scene day6_thedinner_187
        with Dissolve(1)
        asu "牛排？"
        scene day6_thedinner_197
        with Dissolve(1)
        r1  "我喜欢。"
        scene day6_thedinner_187
        with Dissolve(1)
        asu "那就红酒。"
        scene day6_thedinner_192
        with Dissolve(1)
        asu "波尔多很好，黑兹尔，麻烦了。"
        "黑兹尔" "马上就来，[asu]小姐。"
        scene day6_thedinner_198
        with Dissolve(1)
        asu "天啊……那天在你办公室真好玩。"
        asu "我一直想对[ch]这么做很久了。"
        scene day6_thedinner_199
        with Dissolve(0.5)
        asu "而且[ju]护着我的时候太可爱了。"
        scene day6_thedinner_197
        with Dissolve(1)
        r1  "你有个好朋友。"
        scene day6_thedinner_199
        with Dissolve(1)
        asu "是啊……"
        scene day6_thedinner_200
        with Dissolve(0.5)
        asu "我希望自己对她来说也是好朋友。"
        scene day6_thedinner_197
        with Dissolve(1)
        r1 "就我所见，我觉得是的。"
        scene day6_thedinner_200
        with Dissolve(1)
        pause
        scene day6_thedinner_201
        with Dissolve(0.5)
        "{color=#FF007F}[asu]{/color}咯咯笑了。"
        scene day6_thedinner_203
        with Dissolve(0.5)
        pause
        scene day6_thedinner_202
        with Dissolve(0.5)
        asu "她跟那个地方……太不一样了。"
        asu "跟所有事……所有人都……"
        scene day6_thedinner_204
        with Dissolve(0.5)
        asu "她值得拥有全世界，你知道吗？"
        scene day6_thedinner_205
        with Dissolve(1)
        r1 "我还以为你会这样说[lila]。"
        scene day6_thedinner_206
        with Dissolve(1)
        asu "我是说，我爱[lila]！"
        asu "但她会{b}继承{/b}它……如果她想要的话。"
        scene day6_thedinner_207
        with Dissolve(0.5)
        asu "可[ju]……没有那个条件。"
        scene day6_thedinner_208
        with Dissolve(1)
        asu "而这是件好事，你知道吗？"
        asu "我们{b}需要{/b}更多像她这样的人。"
        asu "没有私心、没有盘算的人。"
        scene day6_thedinner_209
        with Dissolve(1)
        asu "这种人……让人耳目一新。"
        scene day6_thedinner_210
        with Dissolve(0.5)
        asu "你遇到过这样的人吗？"
        scene day6_thedinner_205
        with Dissolve(1)
        r1 "怎么？想跟我换朋友？"
        scene day6_thedinner_211
        with Dissolve(1)
        asu "*轻笑* 小心点。她已经是我的小跟班了。去找你自己的吧。"
        scene day6_thedinner_205
        with Dissolve(1)
        r1 "*轻笑* 小跟班？"
        scene day6_thedinner_212
        with Dissolve(1)
        asu "你看过她的眼睛吗？那么……"
        scene day6_thedinner_213
        with Dissolve(0.5)
        pause
        scene day6_thedinner_214
        with Dissolve(0.5)
        asu "很纯吧？"
        scene day6_thedinner_205
        with Dissolve(1)
        r1 "*轻笑* 是啊……我知道。"
        r1 "那就是她的魅力。"
        scene day6_thedinner_215
        with Dissolve(1)
        asu "确实是。"
        scene day6_thedinner_205
        with Dissolve(1)
        r1 "你刚说的[lila]……说她会继承它，听起来很任人唯亲吧？"
        scene day6_thedinner_216
        with Dissolve(1)
        asu "哦，不是。我不是那个意思。"
        asu "莱拉完全有能力靠自己挣到它。"
        asu "她是完美的校园女王。人气旺，人人都喜欢她。"
        scene day6_thedinner_217
        with Dissolve(1)
        asu "她是运动健将。成绩好。长得漂亮。"
        scene day6_thedinner_218
        with Dissolve(1)
        asu "而且当然，我们不能否认，我们天生就比大多数人拥有更多……资源。"
        asu "没有我父亲的公司，我做成的事连一半都不到。"
        asu "身为市长的女儿，[lila]打开了许多原本不存在的门。"
        scene day6_thedinner_219
        with Dissolve(0.5)
        asu "说到底，我们都懂这个游戏。朱莉连边都沾不上。" 
        asu "而且她也活不下来。"
        asu "至少……我认识的那个[ju]活不下来。"
        asu "而我不会允许这种事发生。"
        scene day6_thedinner_217
        with Dissolve(1)
        r1 "你知道这可能由不得你，对吧？"
        scene day6_thedinner_219
        with Dissolve(1)
        pause
        scene day6_thedinner_220
        with Dissolve(0.5)
        asu "也许吧。"
        scene day6_thedinner_221
        with Dissolve(0.5)
        asu "谁知道呢……"
        scene day6_thedinner_222
        with Dissolve(1)
        r1 "但我明白你的意思。"
        r1 "不是每个人都适合。"
        scene day6_thedinner_221
        with Dissolve(1)
        asu "我猜你喜欢这个，对吧？这个游戏。否则你也不会当上校长。"
        scene day6_thedinner_222
        with Dissolve(1)
        pause
        scene day6_thedinner_223
        with Dissolve(1)
        menu:
            "我喜欢。":
                r1 "我很擅长。而且我已经学会享受它了。"
                scene day6_thedinner_221
                with Dissolve(1)
                asu "*轻笑* 赢的时候挺有意思。不赢的时候就不太有。"
            "不太有。":
                r1 "对，不太有。"
                r1 "我已经因为它失去太多了。"
                $love_asuna+=4
                scene day6_thedinner_221
                with Dissolve(1)
                pause 1
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[asu]的{color=#00ff00}好感{/color}增加了{color=#00ff00}4{/color}点！" )
                asu "谁不是呢？"
            "我玩的是另一个游戏。":
                r1 "我玩的和你不是同一个游戏。不然我也没法说我喜欢你的。"
                scene day6_thedinner_221
                with Dissolve(1)
                asu "你玩的是不同的棋盘，但棋子是一样的。"
        scene day6_thedinner_224
        with Dissolve(1)
        "黑兹尔" "请问现在给您斟酒吗，[asu]小姐？"
        scene day6_thedinner_225
        with Dissolve(1)
        asu "请先给这位先生斟。"
        "黑兹尔" "马上。"
        hide screen notifyEx with dissolve
        scene day6_thedinner_226
        with Dissolve(1)
        pause
        r1 "谢谢。"
        scene day6_thedinner_227
        with Dissolve(1)
        pause
        scene day6_thedinner_228
        with Dissolve(1)
        pause
        scene day6_thedinner_229
        with Dissolve(1)
        pause
        scene day6_thedinner_228
        with Dissolve(1)
        pause
        scene day6_thedinner_227
        with Dissolve(1)
        pause
        scene day6_thedinner_229
        with Dissolve(1)
        pause
        scene day6_thedinner_230
        with Dissolve(0.5)
        r1 "什么？"
        scene day6_thedinner_231
        with Dissolve(1)
        asu "*咯咯笑* 她在等你尝呢。"
        scene day6_thedinner_229
        with Dissolve(1)
        r1 "哦……"
        scene day6_thedinner_232
        with Dissolve(1)
        pause
        scene day6_thedinner_233
        with Dissolve(1)
        r1 "嗯，不错。"
        scene day6_thedinner_234
        "{i}女服务员憋住了笑。{/i}"
        scene day6_thedinner_235
        with Dissolve(1)
        "{color=#FF007F}[asu]{/color}咯咯笑了。"
        play sound "audio/coughsophia.ogg"
        scene day6_thedinner_236
        pause
        scene day6_thedinner_237
        with Dissolve(1)
        stop sound fadeout 1
        "黑兹尔" "非常抱歉。"
        scene day6_thedinner_235
        with Dissolve(1)
        asu "没关系，黑兹尔。酒瓶留下就行，不用给我斟。"
        scene day6_thedinner_238
        with Dissolve(0.5)
        asu "谢谢。"
        scene day6_thedinner_239
        with Dissolve(1)
        "黑兹尔" "打扰了。"
        scene day6_thedinner_240
        with Dissolve(1)
        r1 "我做错什么了吗？"
        scene day6_thedinner_241
        with Dissolve(1)
        asu "不，是我错了。"
        scene day6_thedinner_240
        with Dissolve(1)
        r1 "怎么说？"
        scene day6_thedinner_241
        with Dissolve(1)
        asu "我把你带到了错误的餐厅。"
        asu "你身上有些部分拼不太起来。"
        asu "*轻笑* 我说不上来。有时候感觉你完全是另一个人。"
        scene day6_thedinner_240
        with Dissolve(1)
        r1 "愿意解释一下吗？"
        scene day6_thedinner_241
        with Dissolve(1)
        asu "好吧，你听着。"
        asu "很明显你从没来过这种地方。"
        asu "我困惑的是，你要是习惯不了跟高——"
        scene day6_thedinner_240
        with Dissolve(1)
        r1 "嗯？"
        scene day6_thedinner_241
        with Dissolve(1)
        asu "抱歉。"
        asu "我是说……在你这个圈子里，没人靠不多走动关系就能爬上去。"
        asu "我只是好奇，你得靠什么样的关系才能拿到这份工作。"
        scene day6_thedinner_240
        with Dissolve(1)
        r1 "看来是对的那种。"
        scene day6_thedinner_241
        with Dissolve(1)
        asu "*轻笑* 嗯，算是吧。"
        asu "但我父亲不认识你。这很说明问题。"
        asu "[ch]的父亲也不认识你。这挺奇怪，不过我准了。"
        scene day6_thedinner_240
        with Dissolve(1)
        r1 "*轻笑* 你还{i}准{/i}了？"
        scene day6_thedinner_241
        with Dissolve(1)
        asu "*轻笑* 对！他不重要！忘了他吧！"
        asu "我是说，我原以为应聘这份工作的人至少会被查一查。看来是我想错了。"
        asu "可连{b}市长{/b}都不认识你。全州最负盛名的学院，市长居然连它的校长都不认识。"
        asu "那可是他亲女儿就读的学院。"
        asu "这有点奇怪，不是吗？"
        scene day6_thedinner_249
        with Dissolve(1)
        asu "我不是想冒犯你或者指控你什么，好吗？"
        asu "弄明白你是怎么做到的对我很重要。我想学。"
        scene day6_thedinner_243
        with Dissolve(1)
        r1 "嗯。所以这才是你的目的。"
        scene day6_thedinner_249
        with Dissolve(1)
        asu "嗯……对……"
        asu "我无法想象没有正确的关系也能拿到这种职位。这就是我理解不了的地方。"
        scene day6_thedinner_243
        with Dissolve(1)
        r1 "嗯……既然这样，那你就学吧。"
        r1 "有时候只需要认识对的那一个人，不需要整个圈子。"
        r1 "我的前任卡尔也是我的朋友。"
        r1 "所以他不得不暂时离任时，就让我来顶上。"
        r1 "别忘了这一切都是临时的。"
        r1 "我还得正式被选上，记得吗？"
        scene day6_thedinner_241
        with Dissolve(1)
        asu "我想你说得对。"
        scene day6_thedinner_242
        with Dissolve(1)
        asu "话说回来，你和局长见面怎么样？"
        asu "你知道……因为你的纹身。"
        scene day6_thedinner_243
        with Dissolve(1)
        r1 "我的纹身？"
        scene day6_thedinner_245
        with Dissolve(1)
        asu "对。你穿了像这件一样的西装吗？"
        asu "不，等等。你说他去了你那儿，对吧？"
        asu "他看见了吗？"
        scene day6_thedinner_246
        with Dissolve(1)
        r2 "别缩回去。别装出被冒犯的样子。"
        r2 "她会以为我们在藏什么东西。"
        scene day6_thedinner_247
        with Dissolve(1)
        pause
        scene day6_thedinner_248
        with Dissolve(0.5)
        r2 "在她那个世界里，那图案可能意味着任何事。"
        r2 "顺着演就行。"
        scene day6_thedinner_243
        with Dissolve(1)
        pause
        r1 "他会有什么意见吗？"
        scene day6_thedinner_249
        with Dissolve(1)
        asu "哦，我不知道。警察通常不喜欢纹身。"
        asu "我也想过要去纹一个。"
        asu "*咯咯笑* 但我父亲会把我杀了。"
        scene day6_thedinner_243
        with Dissolve(1)
        r1 "都二十一世纪了，[asu]。"
        r1 "现在人们对纹身的偏见不像以前那么大了。"
        scene day6_thedinner_249
        with Dissolve(1)
        asu "*轻笑* 你显然还不了解我父亲。"
        asu "而你那位……挺有意思。"
        asu "我能问问是什么图案吗？"
        scene day6_thedinner_250
        with Dissolve(1)
        pause
        scene day6_thedinner_251
        with Dissolve(0.5)
        pause
        scene day6_thedinner_252
        with Dissolve(1)
        pause
        scene day6_thedinner_253
        with Dissolve(1)
        pause
        scene day6_thedinner_251
        with Dissolve(1)
        pause
        scene day6_thedinner_250
        with Dissolve(0.5)
        pause
        play sound "audio/gettinupchair.ogg"
        scene day6_thedinner_254
        with Dissolve(1)
        pause
        scene day6_thedinner_249
        with Dissolve(1)
        asu "怎么了吗？"
        scene day6_thedinner_255
        with Dissolve(1)
        r1 "是的。我需要道歉。"
        play sound "audio/fillingglass.ogg"
        scene day6_thedinner_256
        with Dissolve(1)
        pause
        stop sound fadeout 2    
        scene day6_thedinner_257
        with Dissolve(1)
        pause
        scene day6_thedinner_258
        with Dissolve(1)
        r1 "我失礼了。"
        r1 "我本该先给您斟酒。"
        scene day6_thedinner_259
        with Dissolve(1)
        pause
        play sound "audio/gettinupchair.ogg"
        scene day6_thedinner_260
        with Dissolve(1)
        pause
        scene day6_thedinner_261
        with Dissolve(1)
        pause
        scene day6_thedinner_262
        with Dissolve(1)
        asu "不用道歉。"
        scene day6_thedinner_263
        with Dissolve(1)
        asu "我不是在找人给我斟酒。"
        scene day6_thedinner_264
        with Dissolve(1)
        r1 "那你在找什么？"
        scene day6_thedinner_263
        with Dissolve(1)
        asu "别的东西……"
        asu "我还在摸索。"
        scene day6_thedinner_265
        with Dissolve(1)
        r1 "嗯。"
        scene day6_thedinner_263
        with Dissolve(1)
        asu "*轻笑* 别担心。"
        asu "我觉得这对我们俩都有好处。"
        asu "我们聊得越多，我越觉得我们可以互相帮上忙。"
        scene day6_thedinner_264
        with Dissolve(1)
        r1 "我不明白。"
        r1 "帮我什么？"
        scene day6_thedinner_263
        with Dissolve(1)
        asu "你知道背后有多少人在议论你吗？"
        asu "[grace]太太问过我们多少关于你的事。"
        asu "或者局长来访时，你的名字被提起过多少次。"
        asu "或者我父亲有多想见你。"
        scene day6_thedinner_264
        with Dissolve(1)
        r1 "那我什么时候能见到他？"
        scene day6_thedinner_263
        with Dissolve(1)
        asu "要是我说了算……"
        asu "永远不。"
        scene day6_thedinner_264
        with Dissolve(1)
        pause
        scene day6_thedinner_263
        with Dissolve(1)
        asu "我觉得你漏看了我们聊天里的几个要点。"
        asu "你知道，[ja]曾经跟我说过，「Estás entrando a la boca del lobo.」"
        asu "如果我没记错，那大概可以译成「你正走进狼的嘴里」之类的意思。"
        asu "我觉得这比说你闯进了马蜂窝要有诗意多了。"
        scene day6_thedinner_264
        with Dissolve(1)
        r1 "我不觉得这两句话是一个意思。"
        scene day6_thedinner_263
        with Dissolve(1)
        "{color=#FF007F}[asu]{/color}轻笑了一声。"
        play sound "audio/gettinupchair.ogg"
        scene day6_thedinner_266
        with Dissolve(1)
        asu "说你是钻进蛇窝里是不是更好？"
        scene day6_thedinner_267
        with Dissolve(1)
        pause
        scene day6_thedinner_266
        with Dissolve(1)
        asu "感觉你希望我说话再直接一点。我没意见。"
        asu "请坐。我有个东西你会感兴趣。"
        scene day6_thedinner_267
        with Dissolve(1)
        pause
        play sound "audio/gettinupchair.ogg"
        scene day6_thedinner_250
        with Dissolve(1)
        r1 "我听着。"
        scene day6_thedinner_249
        with Dissolve(1)
        asu "你是卡尔的朋友，对吧？"
        scene day6_thedinner_250
        with Dissolve(1)
        r1 "对。"
        scene day6_thedinner_249
        with Dissolve(1)
        asu "但光凭这一点，你还算不上这个圈子的人，对吧？"
        scene day6_thedinner_250
        with Dissolve(1)
        pause
        scene day6_thedinner_249
        with Dissolve(1)
        asu "听着。我想说的是……"
        asu "你没在那儿念过书。你不认识这些人。"
        scene day6_thedinner_250
        with Dissolve(1)
        r1 "我很清楚他们是什么人，[asu]。"
        scene day6_thedinner_249
        with Dissolve(1)
        asu "那你就该知道，你跟我一样，都是棋子。"
        asu "就像[lila]。或者[ch]。汤姆。每一个人都是。"
        asu "很不想这么说，但这是事实。"
        asu "我想要什么不重要。[lila]想要什么也不重要。"
        asu "就算[ch]摆出一副那地方归他所有的样子，他想要什么其实也无所谓。"
        asu "做决定的是我们的父母，不是我们。"
        scene day6_thedinner_250
        with Dissolve(1)
        r1 "你在笑。但听起来并不怎么高兴。"
        scene day6_thedinner_277
        with Dissolve(1)
        pause
        scene day6_thedinner_278
        with Dissolve(1)
        asu "当你知道了我知道的东西，就会这样。"
        asu "真相不会让我难受。但现实会。"
        asu "我赌上的东西太多了。我不能让事情就这样下去。"
        asu "改变是必要的。我不信那边发生的事会延续到下一代。"
        transform callback:
        #    matrixcolor (TintMatrix("#e7ca70") * SaturationMatrix(0.6))
            matrixcolor (SepiaMatrix(tint='#ffeec2'))
        #Something to test out later. I need to try different combinations to get the proper effect I want.
        scene day6_thedinner_250
        with Dissolve(1)
        pause
        play sound "audio/Flash.ogg" volume 0.5
        scene dinnerwiththedevil_117_14 at callback
        with flashbulb
        lila "哦，他们是我的朋友。"
        scene dinnerwiththedevil_117_17 at callback
        with dissolve
        "市长" "你和奖学金学生做朋友？"
        scene dinnerwiththedevil_117_18 at callback
        with dissolve
        lila "对啊！他们特别好！"
        lila "怎么了？"
        scene dinnerwiththedevil_117_16 at callback
        with dissolve
        grace "你其他朋友怎么看他们？"
        scene dinnerwiththedevil_117_19 at callback
        with dissolve
        lila "什么意思？"
        scene dinnerwiththedevil_117_16 at callback
        with dissolve
        grace "哦，你知道的……"
        grace "他们跟你那个圈子合得来吗？"
        scene dinnerwiththedevil_117_19 at callback
        with dissolve
        lila "合得来啊！他们超棒的！"
        lila "[ju]是班上最聪明的女生。物理就是她在帮我。"
        lila "我前几天跟你说过的。"
        scene dinnerwiththedevil_117_16 at callback
        with dissolve
        grace "我不知道她是奖学金学生。"
        grace "这倒有意思。"
        scene dinnerwiththedevil_117_19 at callback
        with dissolve
        lila "怎么了？"
        scene dinnerwiththedevil_117_20 at callback
        with dissolve
        grace "没什么要紧的。只是好奇。"
        scene dinnerwiththedevil_109 at callback
        with dissolve
        "市长" "时代会变。"
        grace "事情会演变。"
        play sound "audio/Flash.ogg" volume 0.5
        scene day6_thedinner_250
        with flashbulb
        pause
        
        
        scene day6_thedinner_278
        with Dissolve(1)
        asu "你明白我的意思了吗？"
        scene day6_thedinner_250
        with Dissolve(1)
        r1 "这一点上你也许是对的。"
        scene day6_thedinner_247
        with Dissolve(1)
        r2 "她可能有点低估了自己的位置。"
        r2 "我们不只是棋子，她也不只是。"
        r2 "他们父母在这一切里确实更有权力，这没错。"
        r2 "但他们只能拿到二手消息。"
        scene day6_thedinner_248
        with Dissolve(0.5)
        r2 "像[ch]那样的人，可能会跟她父亲说我们是一群白痴。"
        r2 "而[lila]可能会说我们很棒。"
        r2 "让学生站在我们这边很重要。"
        r2 "学生能影响父母。"
        scene day6_thedinner_250
        with Dissolve(1)
        r1 "我们已经同意得对此做点什么了。"
        r1 "还有必要再提吗？你有新情报？"
        
        
        scene day6_thedinner_277
        with Dissolve(1)
        pause
        scene day6_thedinner_278
        with Dissolve(0.5)
        pause
        scene day6_thedinner_279
        with Dissolve(1)
        pause
        scene day6_thedinner_280
        with Dissolve(1)
        pause
        scene day6_thedinner_281
        with Dissolve(1)
        asu "拿着。自己看。"
        scene day6_thedinner_282
        with Dissolve(2)
        pause
        scene day6_thedinner_283
        with Dissolve(2)
        pause
        scene day6_thedinner_284
        with Dissolve(2)
        pause
        scene day6_thedinner_316
        with Dissolve(2)
        pause
        scene day6_thedinner_276
        r1 "那是什么？"
        scene day6_thedinner_285
        with Dissolve(1)
        asu "你觉得呢？"
        scene day6_thedinner_276
        with Dissolve(1)
        r1 "这是谁的椅子？"
        scene day6_thedinner_285
        with Dissolve(1)
        pause
        asu "不重要。"
        asu "而这就是我从椅子上擦不干净的东西。"
        asu "我只能把它搬到教室最后面。今天我坐在上面，这样别人就不会坐。"
        asu "上面写的东西比这难听多了。"
        scene day6_thedinner_276
        with Dissolve(1)
        r1 "等等。这是今天发生的？"
        scene day6_thedinner_285
        with Dissolve(1)
        asu "每天都发生，只是换不同的人、不同的班、不同的年级。"
        asu "你知道，这么有组织的事不可能凭空冒出来。"
        asu "这件事我不能问任何人，也不能告诉任何人。我唯一能信任的人就是你。"
        asu "一个局外人。"
        scene day6_thedinner_276
        with Dissolve(1)
        r1 "有人有危险吗？"
        scene day6_thedinner_285
        with Dissolve(1)
        asu "先生，我接下来会把话说得非常清楚。"
        asu "去年，有人把一位高三生的车座浸满了汽油"
        asu "你知道泳池为什么停用吗？"
        asu "传闻是有个学生差点淹死在里面。"
        asu "她也是奖学金学生。"
        asu "奇怪的地方是——谁会跳进一个盖着盖子的泳池？"
        asu "所以，如果我觉得您的问题是——"
        scene day6_thedinner_276
        r1 "我先打断一下。"
        r1 "我理解你的不满，但因为我提问就指责我，对解决问题没有任何帮助。"
        scene day6_thedinner_285
        with Dissolve(1)
        asu "我知道……对不起。"
        scene day6_thedinner_276
        with Dissolve(1)
        r1 "我知道这是个敏感话题。"
        r1 "我能理解这为什么会让你这么难受。"
        r1 "听着。我也一样喜欢[ju]和[ja]。"
        r1 "我不会让任何事发生在他们身上。"
        scene day6_thedinner_285
        with Dissolve(1)
        asu "如果你不知道我刚才告诉你的那些事……你怎么保护他们？"
        asu "你自己说的。你没法对不知道的事采取行动。"
        scene day6_thedinner_276
        with Dissolve(1)
        r1 "我们务实地来看这件事吧。"
        r1 "撇开我的个人感情。撇开我有多在乎他们。"
        r1 "这样吧，姑且假设这纯粹只是为了工作。完全是职业考量。"
        r1 "如果我想保住职位，你认为我会让这种事发生吗？"
        r1 "如果学生在我的任期内因为那种事受伤，你觉得会怎样？"
        r1 "警察会把这里翻个底朝天。全城新闻都会报。"
        scene day6_thedinner_285
        asu "我明白。"
        scene day6_thedinner_276
        r1 "所以你也明白，我不是完美的人。"
        r1 "但我确实在拼命努力。"
        r1 "而且既然我在这儿，就绝不会让他们出事。"
        
        scene day6_thedinner_285
        with Dissolve(1)
        pause
        scene day6_thedinner_286
        with Dissolve(0.5)
        asu "你知道……那天你和我们一起玩 D&D 的时候……"
        scene day6_thedinner_285
        with Dissolve(0.5)
        asu "我无法想象任何一个管理者会那样做。"
        asu "这说明了很多。"
        scene day6_thedinner_276
        with Dissolve(1)
        r1 "这同样说明了很多关于你的事。"
        r1 "你敢那样跟我说话。我能想象你有多在乎他们。"
        scene day6_thedinner_285
        with Dissolve(0.5)
        asu "有勇气意味着我应该害怕。"
        asu "我没什么好怕的。"
        scene day6_thedinner_276
        with Dissolve(1)
        pause
        r1 "我们退一步说。"
        r1 "我们是来互相帮忙的，记得吧？"
        scene day6_thedinner_285
        with Dissolve(1)
        pause
        scene day6_thedinner_271
        with Dissolve(1)
        asu "对不起。对，我们是。"
        scene day6_thedinner_276
        with Dissolve(1)
        r1 "我们放松点，好吗？我们在同一队。"
        scene day6_thedinner_199
        with Dissolve(0.5)
        asu "嗯……你说得对。"
        scene day6_thedinner_200
        with Dissolve(0.5)
        asu "我们……"
        scene day6_thedinner_199
        with Dissolve(0.5)
        asu "把酒喝完吧。"
        asu "好好吃饭。"
        asu "剩下的可以以后再聊。怎么样？"
        scene day6_thedinner_276
        with Dissolve(1)
        pause
        scene day6_thedinner_288
        with Dissolve(0.5)
        r1 "那太好了……"
        scene day6_thedinner_289
        with Dissolve(2)
        pause
        scene day6_thedinner_290
        with Dissolve(2)
        pause
        scene day6_thedinner_291
        with Dissolve(2)
        pause
        scene black
        with Dissolve(2)
        pause
        scene day6_thedinner_292
        with Dissolve(2)
        asu "好，你五分钟后可以进来。"
        asu "我会在门口那边。"
        asu "谢谢你，弗兰克。"
        scene day6_thedinner_293
        with Dissolve(1)
        asu "今晚很愉快，是吧？"
        r1 "是的。"
        asu "我的意思是……菜很棒。"
        scene day6_thedinner_294
        with Dissolve(1)
        r1 "*轻笑* 陪酒的人更棒。"
        asu "哦？"
        scene day6_thedinner_295
        with Dissolve(1)
        r1 "我是说，那位女服务员太棒了。"
        asu "*轻笑* 海瑟尔人很好。"
        scene day6_thedinner_296
        with Dissolve(1)
        asu "你给的小费很大方。"
        scene day6_thedinner_297
        with Dissolve(1)
        r1 "既然是你付的账，这是我该做的最低限度了。"
        scene day6_thedinner_298
        with Dissolve(1)
        asu "好吧……要是我伤了你的自尊心，下次你可以请我吃饭。"
        r1 "*轻笑* 我只是希望你能早点告诉我你那个小计划。"
        scene day6_thedinner_299
        with Dissolve(0.5)
        asu "不然你就会让我付钱了吗？"
        r1 "嗯……如果你求得够诚恳的话。"
        asu "哈！"
        asu "下次我们再想办法。"
        scene day6_thedinner_300
        with Dissolve(1)
        asu "还有，先说清楚，那不是我的什么「小计划」。"
        r1 "所以不是你的主意？"
        asu "我是说那不是个计谋。那是基本的礼貌。"
        asu "是我发出的邀请，那就该由我来付钱。父亲一直都是这么说的。"
        scene day6_thedinner_307
        with Dissolve(1)
        asu "先生……你看。刚才那事我真的很抱歉——"
        scene day6_thedinner_303
        with Dissolve(1)
        r1 "你还年轻。但你该学会控制自己的情绪。这种机会不多。"
        r1 "我说你有勇气，不是暗示你该怕我。"
        r1 "就像我今晚早些时候说的，你不该那样议论局长。"
        r1 "那不是尊敬那个人，而是尊敬那个职位。"
        r1 "换个校长，可能就会理解成另一个意思了。"
        scene day6_thedinner_301
        with Dissolve(1)
        asu "换个校长，我们就不会有这场对话了。" 
        asu "我也许选错了餐厅，但我很高兴选对了人。"
        asu "也许我们能互相帮上更多忙，不只是奖学金那件事。我们能做很多。"
        scene day6_thedinner_303
        with Dissolve(1)
        r1 "确实。"
        r1 "但记住。"
        scene day6_thedinner_304
        with Dissolve(1)
        r1 "一句好话加一把枪，永远比只有一把枪走得更远。"
        scene day6_thedinner_302
        with Dissolve(0.5)
        asu "*轻笑* 我觉得这不是正确的那句——"
        scene day6_thedinner_307
        asu "等等，所以原来你其实懂一点黑手党的事。"
        scene day6_thedinner_303
        with Dissolve(1)
        pause
        scene day6_thedinner_304
        with Dissolve(0.5)
        pause
        scene day6_thedinner_305
        with Dissolve(2)
        pause
        scene day6_thedinner_307
        with Dissolve(1)
        asu "我想这是我的告辞信号了。"
        asu "那番话我们改天再聊。"
        scene day6_thedinner_308
        with Dissolve(1)
        asu "你真不要我送你一程吗？"
        r1 "真的不用。我住得有点远。"
        asu "真的不麻烦。你确定吗？"
        r1 "我确定。"
        asu "好吧。"
        scene day6_thedinner_309
        with Dissolve(2)
        pause
        asu "哦，差点忘了。"
        scene day6_thedinner_310
        with Dissolve(2)
        asu "这个给你……以防我们刚才聊天时你漏掉了什么。"
        asu "那些驻扎在校的警察……"
        asu "跟枪击案没关系。"
        scene day6_thedinner_311
        with Dissolve(1)
        r1 "你为什么这么说？"
        scene day6_thedinner_312
        with Dissolve(1)
        asu "你说卡尔是你的朋友。"
        asu "抱歉，你的掩护借口该换一个更好的。"
        asu "我知道你有个有权势的朋友。" 
        asu "而那个朋友让你当上校长，可能得罪了不少人。"
        asu "你迟早得面对[ch]的父亲。"
        scene day6_thedinner_313
        with Dissolve(0.5)
        asu "还有我的父亲。"
        scene day6_thedinner_314
        with Dissolve(1)
        asu "今晚很愉快，先生。"
        asu "我很期待下次。"
        asu "有些东西我想给您看。"
        scene day6_thedinner_309
        with Dissolve(2)
        asu "祝您晚安，先生。"
        scene day6_thedinner_315
        with Dissolve(2)
        pause
        r1 "你也是。"
        stop music fadeout 4
        scene black with Dissolve(2)
        play sound "audio/Lockpick_Success.ogg" volume 0.1
        $ biopage["asuna"] = 2
        show screen notifyEx( msg="[asu]的{color=#00ff00}人物档案{/color}已被{color=#00ff00}更新{/color}！" )
        $ unlock_bust_char_image("asuna", 1)
        pause
        hide screen notifyEx with dissolve
        
        
        play music2 "audio/soundtrack/Ambiance/nature1.ogg" volume 0.5
        play sound "audio/carshut.ogg"
        scene day6_thedinner_317
        with Dissolve(2)
        pause
        scene day6_thedinner_318
        with Dissolve(2)
        pause
        scene day6_thedinner_319
        with Dissolve(2)
        pause
        scene day6_thedinner_320
        with Dissolve(2)
        pause
        scene day6_thedinner_321
        with Dissolve(2)
        pause
        scene day6_thedinner_322
        with Dissolve(2)
        pause
        scene day6_thedinner_323
        with Dissolve(2)
        pause
        scene day6_thedinner_324
        with Dissolve(2)
        pause
        scene day6_thedinner_325
        with Dissolve(2)
        sophia "而我当时正拼命忍住不笑——"
        scene day6_thedinner_326
        with Dissolve(0.5)
        pause
        scene day6_thedinner_327
        with Dissolve(0.5)
        sophia "哟！看谁回来了！"
        scene day6_thedinner_328
        with Dissolve(2)
        pause
        scene day6_thedinner_329
        with Dissolve(0.5)
        pause
        scene day6_thedinner_330
        with Dissolve(0.5)
        pause
        scene day6_thedinner_331
        with Dissolve(1)
        isa "我们正准备担心呢。"
        scene day6_thedinner_332
        with Dissolve(1)
        r1 "*轻笑* 抱歉了。"
        scene day6_thedinner_327
        with Dissolve(1)
        sophia "你在笑什么？"
        scene day6_thedinner_333
        with Dissolve(1)
        r1 "*轻笑*"
        scene day6_thedinner_334
        with Dissolve(1)
        r1 "回家的感觉真好，我想。"
        scene day6_thedinner_335
        with Dissolve(1)
        pause
        scene day6_thedinner_336
        with Dissolve(1)
        ava "你们没有电话吗……？"
        scene day6_thedinner_337
        with Dissolve(1)
        r1 "我试着打给你们了，但我手机没电。"
        r1 "对不起。比我预想的久。"
        scene day6_thedinner_338
        with Dissolve(1)
        pause
        scene day6_thedinner_339
        with Dissolve(0.5)
        ava "我困得没力气吵架了。"
        scene day6_thedinner_340
        with Dissolve(1)
        sophia "*哼唱* 我就说他会没事的嘛——"
        scene day6_thedinner_341
        with Dissolve(1)
        r1 "好了。你们几个去睡吧？"
        r1 "我去锁门。"
        scene day6_thedinner_342
        with Dissolve(2)
        isa "好了[ava]。你的值班结束了。我们去睡吧？"
        ava "别……别取笑我。做饭的人……是我……"
        scene day6_thedinner_343
        with Dissolve(1)
        isa "*咯咯笑* 已经不是了！明天早饭我来做。"
        isa "你需要睡觉。"
        scene day6_thedinner_341
        with Dissolve(1)
        r1 "[ava]。[isa]。"
        scene day6_thedinner_344
        with Dissolve(1)
        pause
        scene day6_thedinner_341
        with Dissolve(1)
        r1 "谢谢你们。真的。"
        scene day6_thedinner_344
        with Dissolve(1)
        pause
        scene day6_thedinner_345
        with Dissolve(2)
        pause
        scene day6_thedinner_341
        with Dissolve(1)
        play sound "audio/open4.ogg"
        pause
        scene day6_thedinner_346
        with Dissolve(2)
        pause
        scene day6_thedinner_347
        sophia "按摩！"
        scene day6_thedinner_348
        with Dissolve(2)
        pause
        scene day6_thedinner_349
        with Dissolve(1)
        sophia "什么？很疼！"
        scene day6_thedinner_350
        with Dissolve(1)
        pause
        scene day6_thedinner_351
        with Dissolve(2)
        sophia "天哪……太舒服了……"
        scene day6_thedinner_352
        with Dissolve(1)
        pause
        scene day6_thedinner_353
        with Dissolve(1)
        r1 "嘿。"
        scene day6_thedinner_354
        with Dissolve(1)
        pause
        scene day6_thedinner_355
        with Dissolve(1)
        pause 0.2
        sophia "嗯？"
        scene day6_thedinner_353
        with Dissolve(1)
        r1 "谢谢你……谢谢你们撑住了。"
        scene day6_thedinner_355
        with Dissolve(1)
        pause 0.2
        sophia "这次……我觉得我们是在一起的。"
        sophia "我百分之百确信你会没事。"
        scene day6_thedinner_353
        with Dissolve(1)
        pause 0.2
        r1 "我知道。"
        scene day6_thedinner_355
        with Dissolve(1)
        pause 0.2
        sophia "我只是需要你给我这个。"
        scene day6_thedinner_353
        with Dissolve(1)
        pause
        scene day6_thedinner_355
        with Dissolve(1)
        pause 0.2
        sophia "只要知道你安全，我就放心了。"
        sophia "当你叫我别担心时，我就知道该担心。"
        sophia "真正让我害怕的，是你瞒着我。"
        scene day6_thedinner_353
        with Dissolve(1)
        pause
        scene day6_thedinner_352
        with Dissolve(0.5)
        r1 "嗯……"
        scene day6_thedinner_353
        with Dissolve(0.5)
        r1 "我知道。"
        r1 "对不起。"
        scene day6_thedinner_355
        with Dissolve(1)
        pause 0.2
        sophia "别道歉。我知道你是为什么。"
        sophia "而且我为此爱你。"
        sophia "我们的关系是建立在忠诚之上的。建立在信任之上。"
        sophia "我完全信任你。所以你叫我留下，我就留下。"
        sophia "你叫我跳，我就跳。"
        sophia "我只是需要知道，你同样信任我。"
        scene day6_thedinner_352
        with Dissolve(1)
        pause
        scene day6_thedinner_353
        with Dissolve(1)
        r1 "你知道我是的。"
        scene day6_thedinner_355
        with Dissolve(1)
        sophia "我知道。但你独自待了太久，已经忘了这一点。"
        sophia "[ava]和我就在这儿提醒你。"
        sophia "你不是一个人。"
        scene day6_thedinner_353
        with Dissolve(1)
        r1 "现在好像还有[isa]了。"
        scene day6_thedinner_356
        with Dissolve(1)
        sophia "哦，她太棒了！"
        scene day6_thedinner_357
        with Dissolve(1)
        sophia "我们身边需要多点平民，你知道吗？"
        sophia "这感觉就像一阵清风。"
        scene day6_thedinner_355
        with Dissolve(0.5)
        sophia "哦，就是你之前不想告诉我的那件事。"
        sophia "她告诉我了。所以你不用担心了。"
        scene day6_thedinner_353
        with Dissolve(1)
        r1 "等等，真的吗？"
        scene day6_thedinner_355
        with Dissolve(1)
        sophia "真的啊！前男友？"
        scene day6_thedinner_356
        with Dissolve(0.5)
        sophia "男人！你到底什么时候才能学会？"
        scene day6_thedinner_352
        with Dissolve(1)
        r1 "哇……"
        r1 "我没想到她会说出来。"
        scene day6_thedinner_355
        with Dissolve(1)
        sophia "*咯咯笑* 我的意思是，换我是他我也会这么做。"
        sophia "她太漂亮了！"
        scene day6_thedinner_352
        with Dissolve(1)
        pause
        scene day6_thedinner_353
        with Dissolve(1)
        r1 "等等。她到底跟你说了什么？"
        scene day6_thedinner_355
        with Dissolve(1)
        sophia "说她前男友没能很好地接受分手。"
        sophia "说他一直跑去她家或者她工作的地方，求她复合。"
        sophia "*咯咯笑* 我有点理解他。可怜的家伙。"
        scene day6_thedinner_353
        with Dissolve(1)
        pause
        scene day6_thedinner_352
        with Dissolve(1)
        r1 "[isa]……"
        scene day6_thedinner_355
        with Dissolve(1)
        sophia "真是把自己的掩护全毁了，对吧？"
        scene day6_thedinner_358
        with Dissolve(1)
        sophia "天哪……你这按摩要了我的命。"
        scene day6_thedinner_353
        with Dissolve(1)
        pause
        scene day6_thedinner_359
        with Dissolve(1)
        pause
        scene day6_thedinner_360
        with Dissolve(1)
        sophia "什么？……很舒服啊……"
        scene day6_thedinner_353
        with Dissolve(1)
        pause
        scene day6_thedinner_361
        with Dissolve(1)
        sophia "不要——别停！"
        sophia "给我回来下面！"
        scene day6_thedinner_362
        with Dissolve(1)
        pause
        scene day6_thedinner_363
        with Dissolve(1)
        pause
        scene day6_thedinner_364
        with Dissolve(1)
        pause
        scene day6_thedinner_365
        with Dissolve(2)
        pause
        scene day6_thedinner_366
        with Dissolve(2)
        pause
        sophia "你为什么……那样看着我？"
        scene day6_thedinner_367
        with Dissolve(1)
        pause
        scene day6_thedinner_368
        with Dissolve(1)
        pause
        menu:
            "因为你是我的。{p=0.0}{color=#00ff00}([sophia] 堕落 +4){/color}":
                scene day6_thedinner_369
                with Dissolve(1)
                r1 "而现在……和你在一起……"
                r1 "我真是……"
                scene day6_thedinner_370
                pause
                scene day6_thedinner_371
                with Dissolve(1)
                pause
                scene day6_thedinner_380
                with Dissolve(2)
                pause
                scene day6_thedinner_372
                with Dissolve(2)
                pause
                scene day6_thedinner_373
                with Dissolve(2)
                sophia "照这个速度我们会把孩子们吵醒的。"
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[sophia]的{color=#00ff00}堕落{/color}上升了{color=#00ff00}4{/color}点！" )
                $corruption_sophia+=4
                scene day6_thedinner_374
                with Dissolve(1)
                pause
        
            "谢谢你。为这一切。{p=0.0}{color=#00ff00}([sophia] 好感 +4){/color}":
                play sound "audio/Lockpick_Success.ogg" volume 0.1
                show screen notifyEx( msg="[sophia]的{color=#00ff00}好感{/color}提升了{color=#00ff00}4{/color}点！" )
                $love_sophia+=4
                scene day6_thedinner_376
                with Dissolve(1)
                sophia "*咯咯笑* 不客气！"
                sophia "但如果你想好好谢我……可以先从我的嘴唇开始。"
                scene day6_thedinner_375
                with Dissolve(2)
                pause
                scene day6_thedinner_377
                with Dissolve(2)
                pause
                scene day6_thedinner_372
                with Dissolve(2)
                pause
                scene day6_thedinner_378
                with Dissolve(2)
                sophia "照这个速度我们会把孩子们吵醒的。"
        hide screen notifyEx with dissolve
        menu:
            "我不在乎。 {p=0.0}(开始一段成人场景。)":
                label day6_sophiasex:
                    scene day6_thedinner_379
                    with Dissolve(1)
                    r1 "那你最好一声都别出。"
                    scene day6_thedinner_381
                    with Dissolve(2)
                    pause
                    scene day6_thedinner_382
                    with Dissolve(2)
                    pause
                    scene day6_thedinner_383
                    with Dissolve(2)
                    pause
                    scene day6_thedinner_384
                    with Dissolve(2)
                    pause
                    scene day6_thedinner_385
                    with Dissolve(2)
                    pause
                    scene day6_thedinner_386
                    with Dissolve(2)
                    pause
                    play audio "audio/drums1.ogg" volume 0.5
                    scene black
                    play movie "images/Animations/day6/day6_sophia_idle1.webm" loop 
                    show movie with Dissolve(1)
                    window hide
                    pause
                    window auto
                    play audio "audio/drums1.ogg" volume 0.5
                    scene black
                    play movie "images/Animations/day6/day6_sophia_idle2.webm" loop 
                    show movie with Dissolve(1)
                    window hide
                    pause
                    window auto
                    play audio "audio/drums1.ogg" volume 0.5
                    scene black
                    play movie "images/Animations/day6/day6_sophia_idle3.webm" loop 
                    show movie with Dissolve(1)
                    window hide
                    pause
                    window auto
                    menu:
                        "去她的。":
                            pass
                    play audio "audio/cumsound.mp3" volume 0.1
                    scene black
                    play movie "images/Animations/day6/day6_sophia_insert1.webm" loop 
                    show movie with Dissolve(1)
                    window hide
                    pause 3
                    window auto
                    play audio "audio/drums1.ogg" volume 0.5
                    scene black
                    play movie "images/Animations/day6/day6_sophia_againstwall1.webm" loop 
                    show movie with Dissolve(1)
                    window hide
                    pause
                    window auto
                    play audio "audio/drums1.ogg" volume 0.5
                    scene black
                    play movie "images/Animations/day6/day6_sophia_againstwall2.webm" loop 
                    show movie with Dissolve(1)
                    window hide
                    pause
                    window auto
                    play sound "audio/Lockpick_Success.ogg" volume 0.1
                    show screen notifyEx( msg="[sophia]的{color=#00ff00}堕落{/color}上升了{color=#00ff00}4{/color}点！" )
                    $corruption_sophia+=4
                    sophia "真不敢相信……我们……在这里……"
                    hide screen notifyEx with dissolve
                    sophia "她们会……听到我们的……"
                    r1 "*轻笑* 所以我才叫你别出声。"
                    sophia "但我忍不住……忍不住不回应……"
                    play audio "audio/drums1.ogg" volume 0.5
                    scene black
                    play movie "images/Animations/day6/day6_sophia_againstwall3.webm" loop 
                    show movie with Dissolve(1)
                    window hide
                    pause
                    window auto
                    sophia "天哪……"
                    sophia "我们得快点……结束……"
                    sophia "求你了……"
                    play audio "audio/drums1.ogg" volume 0.5
                    scene black
                    play movie "images/Animations/day6/day6_sophia_againstwall4.webm" loop 
                    show movie with Dissolve(1)
                    window hide
                    pause
                    window auto
                    menu:
                        "射在她体内。":
                            pass
                    play audio "audio/cumsound.mp3" volume 0.1
                    play movie "images/Animations/day6/day6_sophia_creampie.webm" loop 
                    show movie with flashbulb
                    window hide
                    pause 4
                    window auto
                    stop movie
                    scene black
                    scene day6_thedinner_387
                    with Dissolve(2)
                    r1 "*低吼*"
                    play sound "audio/Lockpick_Success.ogg" volume 0.1
                    show screen notifyEx( msg="[sophia]的{color=#00ff00}堕落{/color}与{color=#00ff00}好感{/color}都上升了{color=#00ff00}3{/color}点！" )
                    $corruption_sophia+=3
                    $love_sophia+=3
                    sophia "有时候你真的……"
                    hide screen notifyEx with dissolve
                    sophia "……让我疯掉。"
                    r1 "*轻笑* 我也一样。"
                    r1 "我们该睡了吧。"
                    sophia "我可以就在这儿睡着……那样我就是世界上最幸福的女人……"
                    r1 "*轻笑* 我还得冲个澡。不过你先睡吧。"
                    r1 "帮我把被窝暖好。"
                    $ renpy.end_replay()
                
            
            "你说得对。我们睡吧。":
                scene day6_thedinner_379
                with Dissolve(1)
                sophia "什、什么？"
                scene day6_thedinner_388
                with Dissolve(1)
                sophia "你就这样……走掉？！"
                r1 "*轻笑* 怎么，等不到明天了？"
                sophia "你该庆幸自己长了张漂亮脸蛋。别以为可以这样吊着我。"
                r1 "那……看来你明天得报复回来了。"
                sophia "哦……那当然！"
                r1 "*轻笑* 我还得冲个澡。不过你可以先去我们房间。"
                r1 "帮我把被窝暖好。"
                
                
        
        scene black with Dissolve(2)
        pause
        scene day6_thedinner_389 with Dissolve(2)
        pause
        r1 "[isa]……"
        r1 "嘿……[isa]。"
        isa "嗯……？"
        scene day6_thedinner_390 with Dissolve(2)
        isa "嗯……先生……？"
        isa "出什么事了吗？"
        r1 "没什么。"
        r1 "你确定不要毯子吗？今晚挺冷的。"
        scene day6_thedinner_391 with Dissolve(1)
        pause
        scene day6_thedinner_392 with Dissolve(0.5)
        isa "真的不用，先生。"
        isa "我真的很喜欢冷，先生。"
        scene day6_thedinner_393 with Dissolve(1)
        r1 "需要什么就随时找我，好吗？"
        r1 "把我叫醒也行。我不介意。"
        r1 "我不想让你不舒服。"
        scene day6_thedinner_392 with Dissolve(1)
        isa "谢谢您，先生。我真的没事。"
        scene day6_thedinner_394 with Dissolve(1)
        r1 "很好。听着。"
        scene day6_thedinner_395 with Dissolve(1)
        r1 "我真的很感谢你今晚照顾[ava]。"
        r1 "你不知道那对我有多重要。"
        scene day6_thedinner_397 with Dissolve(1)
        pause
        scene day6_thedinner_396 with Dissolve(0.5)
        isa "那没什么……"
        scene day6_thedinner_394 with Dissolve(1)
        r1 "那比什么都重要。"
        r1 "我欠你一个人情。"
        scene day6_thedinner_398 with Dissolve(1)
        r1 "*吻了吻她的头* 谢谢。"
        scene day6_thedinner_399 with Dissolve(1)
        r1 "晚安，好吗？"
        play sound "audio/open4.ogg"
        scene day6_thedinner_399
        pause
        scene day6_thedinner_400 with Dissolve(1)
        pause
        play sound "audio/Lockpick_Success.ogg" volume 0.1
        show screen notifyEx( msg="[isa]的{color=#00ff00}好感{/color}提升了{color=#00ff00}4{/color}点！" )
        isa "你也是……"
        scene black with Dissolve(2)
        pause
        hide screen notifyEx with dissolve
        play sound "audio/open4.ogg" volume 0.1
        scene day6_thedinner_401 with Dissolve(2)
        pause
        scene day6_thedinner_402 with Dissolve(2)
        pause
        scene day6_thedinner_403 with Dissolve(2)
        pause
        scene day6_thedinner_404 with Dissolve(2)
        pause
        scene day6_thedinner_405 with Dissolve(2)
        pause
        scene day6_thedinner_406 with Dissolve(2)
        pause
        play sound "audio/beep.mp3"
        pause
        scene day6_thedinner_407 with Dissolve(0.5)
        play sound "audio/beep.mp3"
        pause
        play sound "audio/beep.mp3"
        pause
        scene day6_thedinner_408 with Dissolve(1)
        stop music2 fadeout 3
        play music "audio/soundtrack/smokeandashes.ogg" volume 0.5
        
        r1 "{size=-7}我在听。{/size}"
        ja "{i}Sir...{/i}"
        r1 "{size=-7}[ja]?{/size}"
        ja "{i}*抽泣* 对不起把你吵醒了。{/i}"
        r1 "{size=-7}不，你没有……吵醒我。{/size}"
        r1 "{size=-7}我还没睡。{/size}"
        r1 "{size=-7}出什么事了？已经凌晨两点了。{/size}"
        r1 "{size=-7}你在哭吗？{/size}"
        ja "{i}你能不能……求你了……{/i}"
        r1 "{size=-7}深呼吸。告诉我发生了什么。{/size}"
        ja "{i}*抽泣* 你能……来接我吗？{/i}"
        r1 "{size=-7}你在哪儿？{/size}"
        ja "{i}*抽泣* 我……已经不知道了。{/i}"
        r1 "{size=-7}[ja]，集中精神。你在哪儿？{/size}"
        ja "{i}*哭泣* 我在家……求你了，你能过来吗？{/i}"
        r1 "{size=-7}我这就出发。别挂断，好吗？{/size}"
        r1 "{size=-7}我赶过去的时候一直跟我说话。{/size}"
        ja "{i}*抽泣* 好的……{/i}"
        
        scene black with Dissolve(2)
        pause
        scene day6_thedinner_409 with Dissolve(2)
        r1 "我看到你了。就待在原地，好吗？"
        r1 "我在停车。"
        ja "我好像看到你了。"
        r1 "我要挂断了，好吗？我马上就到。"
        ja "好……"
        play sound "audio/carshut.ogg"
        scene day6_thedinner_410 with Dissolve(2)
        pause
        scene day6_thedinner_411 with Dissolve(2)
        r1 "[ja]？"
        scene day6_thedinner_412 with Dissolve(2)
        pause
        scene day6_thedinner_413 with Dissolve(2)
        pause
        scene day6_thedinner_415 with Dissolve(2)
        pause
        scene day6_thedinner_414 with Dissolve(2)
        pause
        ja "晚上好，先生。"
        jump day7_update
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        
        
        
     #   asu "通往权力的路上铺满了虚伪与尸体。"
        #HOW DO YOU FIND THE POTATOES?
        #I just looked at y plate
 #       r1 "你是在哪儿学会这样出拳的？"
 #       ingrid "Mein vater想要个儿子。"
  #      r1 "那他还真有了一个。"
  #      ingrid "我打过像你这样的人。"
  #      ingrid "我知道你留了手。"
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