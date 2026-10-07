image splash = "game_backdrop.webp"
image splash2 = "game_backdrop_logo_blur.webp"
image splash3 = "game_backdrop_logo.webp"
image splash4 = "game_backdrop_warning.webp"
image splash7 = "game_backdrop_warning2.webp"
image splash5 = "gray.webp"
image splash6 = "Toxicity_Splash_1.webp"

label splashscreen:
    scene black
    with Pause(1)

    show splash with Dissolve(2)
    show splash2 with Dissolve(2)
    show splash3 with Dissolve(2)
    with Pause(2)
    show splash2 with Dissolve(2)
    show splash4 with Dissolve(2)
    with Pause(3)
    show splash7 with Dissolve(2)
    with Pause(3)
    scene splash5 with Dissolve(1)
    with Pause(1)
    scene splash6 with Dissolve(1)
    with Pause(0.5)

    return

label start:
#Begin Prologue
    scene blank with Dissolve(2)
    scene gray with Dissolve(2)
    stop music fadeout 2.0
    scene mcnamechoice_background with Dissolve(1)
    label prompt_for_name:
    $ ui.text("{size=+10}{font=fonts/DCC - Ash.otf}请输入名字(默认：约翰){/font}{/size}", xalign=0.5, yalign=0.4)
    $ ui.input('', xalign=0.5, yalign=0.5)
    $ player_name = ui.interact()
    if player_name == '':
        $ player_name = 'John'
    $ ui.text("{size=+10}{font=fonts/DCC - Ash.otf}请输入姓氏(默认：休斯顿){/font}{/size}", xalign=0.5, yalign=0.4)
    $ ui.input('', xalign=0.5, yalign=0.5)
    $ player_lastname = ui.interact()
    if player_lastname == '':
        $ player_lastname = 'Houston'
    scene blank with Dissolve(1)
    $ ui.text("{size=+10}{font=fonts/DCC - Ash.otf}你就是[player_name][player_lastname]。{/font}{/size}", xalign=0.5, yalign=0.4)
    $ renpy.pause ()
    # Capture Player Name For Gallery
    $ persistent.player_name = player_name
    $ persistent.player_lastname = player_lastname
    #################
    scene blank with Dissolve(2)
    play music officemain fadein 2.0
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("Prologue_open", transition=Dissolve(1.0))()
    pause
    $ Hide("Prologue_open", transition=Dissolve(1.0))()
    $ Show("june_10_1015", transition=Dissolve(1.0))()
    pause
    $ Hide("june_10_1015", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c000_s001_001 with Dissolve(2)
    "办公室里平淡的一天。也不能说慢，只是没什么真正有意思的事发生。不过这就是日常。我们所有人到公司、坐下、磨完那些无聊的活儿，就为了拿到一份薪水。没有狗血的一天就是好日子。"
    "偶尔也会有电话或订单要费点心思处理，但大多数时候，只是有人按周租下我们的身体，一周五天。他们为我们的经验和知识付一部分钱给某些人，即便如此，那点钱也真的不够。"
    scene c000_s001_002 with Dissolve(0.25)
    "至于我，已经在这儿干了七年。是啊，我本可以另找一份工作，更好的那种。但薪水还行，而且我不是那种会从一个地方跳到另一个地方的人。"
    "这里有福利、有带薪假期，还没人对我指手画脚。我的活儿干得够好，以至于管理层想搞点人事变动的时候，我总是稳稳待在他们的视线之外。"
    scene c000_s001_003 with Dissolve(0.25)
    "考虑到最近刚裁过一轮人，我大概算是混得不错的了。这里曾经有二十六个人，现在顺利的话也就剩六个。经理还在休病假，所以多少算是由我负责——而这真是个糟糕的主意。"
    "我已经彻底消极了，勉强只做最基本的事。订单来了我们就处理，但速度说不上快。我们这里的数字正处在悬崖边上——要么继续开门，要么彻底关门。"
    scene c000_s001_004 with Dissolve(0.5)
    "奥蒂斯。我的同事。我不会说他是我的朋友。最多算是最浅薄意义上的“工作朋友”。你跟一个人并排坐了一年多，总得学会怎么跟他相处。像婚姻一样，只不过我在婚姻上也不怎么在行。"
    "他倒没多让人受不了，不过我承认他在社交上有点笨拙。也不是说我就好到哪儿去。我现在比以前随和多了——离婚会改变一个人。它会缩小你的社交圈，通常砍掉一半，有时候更多。到那时你才知道，在你们还是情侣的时候，究竟有谁是真的喜欢你。"
    scene c000_s001_005 with Dissolve(0.25)
    o "唉。我终于把那批货改送到正确的地址了。下单的时候，收货地址和账单地址不一样都不想想，蠢死了。"
    j "不一直都这样嘛。"
    "一堆无聊又没营养的套话，让他知道我听见了，却又不给出真正的反馈。我脑子里存了一大堆，需要的时候随时能拿出来应付。"
    scene c000_s001_006 with Dissolve(0.25)
    o "我该庆幸才对，至少有事可做。他们砍掉周边这片区域的业务，把我们的工作量搅得一团糟。"
    j "多少有点自我实现的预言。他们削减员工和支援，然后我们就没有人手去把业务做起来，接着又——"
    scene c000_s001_007 with Dissolve(0.25)
    o "恶性循环，老兄。"
    j "胡扯的衔尾蛇。"
    o "正是如此。"
    scene c000_s001_008 with Dissolve(0.5)
    o "所以，米奇那边有消息吗？"
    j "还在休病假。膝盖手术真是要命，基本上得靠物理治疗重新学怎么走路。"
    scene c000_s001_009 with Dissolve(0.25)
    o "唉。听着像下地狱。"
    j "是啊，他本来就不是那种身手利索的人。"
    scene c000_s001_010
    o "那罗杰呢？"
    j "我听说他办公室里还有些东西。看来他还没完全搬去新住处。同时要维持两个城市的两个据点，对他也够怪的。"
    scene c000_s001_011 with Dissolve(0.25)
    o "我猜离婚的时候把他弄丢了，只争取到了周末的探视权。"
    j "是啊，他可真走运。"
    scene c000_s001_012 with Dissolve(0.25)
    o "哦。哦，抱歉。我不是故意……"
    j "没事。反正这样也好。"
    "奥蒂斯可能有点笨拙，说话不过脑子，但我知道他没有恶意。而且这件事也不像别的那么难以启齿。"
    scene c000_s001_013 with Dissolve(0.5)
    j "哦，劳拉周五要来。"
    o "所以我们得表现得规规矩矩？"
    j "是你。她崇拜我。不知道为什么。"
    scene c000_s001_014 with Dissolve(0.25)
    o "小弟情结。"
    j "那我就受之有愧了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_10_520", transition=Dissolve(1.0))()
    pause
    $ Hide("june_10_520", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c000_s001_015 with Dissolve(2)
    play music nightmain fadein 2.0
    "工作日结束了。今天没发生什么重要的事。我是最晚离开大楼的，所以得锁门、关灯。"
    scene c000_s001_016 with Dissolve(0.25)
    "停车场难得没空到底。我们和周边几家店共用这个停车场，不过他们通常和我们上下班时间一样。也许有人在加夜班。"
    scene c000_s001_017 with Dissolve(0.25)
    "不过不是我。是时候回那个“家”了。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_10_610", transition=Dissolve(1.0))()
    pause
    $ Hide("june_10_610", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c000_s001_018 with Dissolve(2)
    "我那破公寓。嗯，也不算破。眼下还凑合。毕竟是匆忙找的。当你因为分居文件需要正式归档、必须另立住所而搬出那套两卧两卫的房子时，你可不一定有时间好好挑下一个住处。"
    "不过，把我住了快八年的房子留给分居的妻子，并不是我心甘情愿做的决定。即使那是为了启动离婚程序的牺牲，我到现在也没法释怀。"
    "因为她在感情上早已翻篇了，而我得赶在脾气失控之前，迅速把自己从这段关系里抽身出来。"
    "我们迟早会走到这一步，我早该有预感的。结婚第二年，我们就已经各自活在自己的小世界里了。不知为何，我们之间的火熄灭了，做什么都没用。"
    "那个收了高额费用、让我“认可”前妻每一项兴趣的婚姻咨询师，当然也帮不上什么忙。我不确定她是不是想让我给南希开一张空白支票，让她想做什么就做什么——在心情不好的时候，用我们的钱去填她灵魂里的某个洞。"
    scene c000_s001_019 with Dissolve(0.5)
    "而当我反对她这种毫无责任感的表现时，坏人就变成了我。于是我决定，与其被别人当成坏人，不如自己当。"
    "结果在经济上和感情上都被掏空，几乎失去所有拥有的东西，这就是我的“回报”。至于南希？我听说她已经有了新的男人。我本该说一句“恭喜她”，然后表现得像个爷们儿，但正如我们已经确立的那样……我是那个坏人。"
    "不幸的是，这场狗血我只能自己扛。爸妈是老派的人，不太明白为什么我们不能凑合着过下去。所以跟他们解释我为什么心情这么差，也行不通。"
    scene c000_s001_020 with Dissolve(0.5)
    "而且，当你身边没有一个不是“工作朋友”的人时，婚姻上的问题就很难找人倾诉。是啊，奥蒂斯能陪我抱怨办公室，但他对我家里的事压根儿不上心。说实话，我也不是多关心他的。"
    "大多数人只觉得我是那个整天板着脸、一副谁欠他钱似的混蛋。没人真的试着问过我一句“你还好吗”。"
    "就连每周会来露个面的人事专员都没有——这听起来简直离谱，因为难道他们不想知道，会不会哪个员工已经气到要拿枪把这地方扫一遍？"
    "我尽量不把私生活的那摊事带进办公室，但当你独自一人面对自己的思绪超过一段时间，你总会在脑子里把过去那段关系的所有片段重播一遍，仿佛只要重新来过，一切就能有不同的结果。"
    scene c000_s001_021 with Dissolve(0.5)
    "不过慢慢地，我觉得事情在变好。或者说，我在努力不再对它耿耿于怀。也许过阵子，我会重新出去约个会。也可能不会。我不着急，也许独处一段时间对我自己也有好处。"
    tv "{i}……未来一周的预报温度大约在 80 多华氏度（27～31℃）左右。最低温在 60 多（约 16℃），周日会掉到 50 多（约 10℃）。提醒一下，本周末空气质量指数预计会进入橙色区间，如果你安排了户外活动，最好做好准备。{/i}"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_13_905", transition=Dissolve(1.0))()
    pause
    $ Hide("june_13_905", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c000_s001_022 with Dissolve(2)
    play music officemain fadein 2.0
    "今天早上车不多，就算是在星期五也算少。我想是因为大家忙了一周已经彻底疲了，又赶上三天长假的缘故。学校放暑假了，我们这儿少了大约百分之三十的人口。对一个濒临干涸、被风吹散的镇子来说，这个变化很显眼。"
    scene c000_s001_023 with Dissolve(0.5)
    "办公室里和预料的一样忙。奥蒂斯来了，不过他今早好像不太想说话。我不怪他。我累了，只想混过去。"
    o "*咳嗽* *咳嗽* 唉……"
    scene c000_s001_024 with Dissolve(0.5)
    j "你那边还好吗？请个病假也行啊。"
    o "不用不用。就是……今天空气太差了。这咳嗽弄得很难受，还把哮喘给诱发出来了。我能撑过今天。"
    scene c000_s001_025 with Dissolve(0.25)
    j "行，但别觉得你就不能偷懒。"
    o "知道了。谢谢，老兄。"
    scene c000_s001_026 with Dissolve(0.5)
    "还有卡莉·科尔登。她来这儿一年了。大学刚毕业，就被招进来接替退休的露丝·巴格利。卡莉没有任何办公室经验，但适应得相当不错。她问了很多问题，等自在下来之后，就证明了自己是个可靠、能自己找事做的人。"
    "一起共事的时候，我不会假装我们不只是同事。我们不怎么聊天——说实话，她好像跟谁都话不多——不过相处得还行。大部分时候，她就算在跟人互动，也是在发消息。"
    scene c000_s001_027 with Dissolve(0.25)
    "从她偶尔透露的只言片语里，我知道她是四个孩子中最年长的。她也订婚了，未婚夫安德鲁来过办公室几次。看起来人不错，也挺帅的。两人看起来很相爱。"
    "我知道那是什么感觉。曾经。"
    scene c000_s001_028 with Dissolve(0.25)
    "*叮铃* *叮铃*"
    j "操。我今天真的一点都不想接电话。"
    scene c000_s001_029 with Dissolve(0.25)
    j "喂？环球办公用品，我是[player_name]。"
    ch "{i}[player_name]，我是查尔斯。{/i}"
    "查尔斯·豪斯是公司的区域销售主管。人不算坏，但我和他的全部交情都纯粹建立在佣金上。他住在镇子另一边，所以偶尔会过来一趟。他给我打电话可是稀罕事。"
    scene c000_s001_030 with Dissolve(0.25)
    j "哦，嗨，查尔斯。接到你电话真高兴。你要的采购报告我刚发过去了。"
    ch "{i}嗯，嗯，看到了，谢谢。不过我打电话不是为了这个，就是有点好奇想问两句。{/i}"
    j "好吧，什么事？"
    scene c000_s001_031
    ch "{i}是我多心，还是空气里有什么东西？花粉还是烟？我敢说外边的空气质量下降了不少。你那边怎么样？{/i}"
    j "我……我今早发现有雾。也可能是类似的东西。我更注意到的是路上没什么车。也许是今年的季节性过敏太厉害，或者来得太早。也可能两者都有。"
    ch "{i}那大概是原因吧。不过老兄，我跟你说，我咳得厉害。而且前臂在发痒，像是起疹子了。我正吃些苏德菲让自己好受点。{/i}"
    j "我，呃……"
    scene c000_s001_032 with Dissolve(0.25)
    ch "{i}抱歉，说得比你想听的多了。好吧，那边一切都还好吗？{/i}"
    j "还能再好到哪儿去。"
    ch "{i}很好。很好。我下周晚些时候尽量过去一趟。{/i}"
    j "我们一直在。"
    scene c000_s001_033 with Dissolve(0.5)
    o "查尔斯？"
    j "对。他下周晚些时候会过来。"
    o "那我把派对用品备上。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_13_135", transition=Dissolve(1.0))()
    pause
    $ Hide("june_13_135", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c000_s001_034 with Dissolve(2)
    "吃完午饭回来时，我在停车场看到一辆熟悉的车，这意味着下午可能没平时那么难熬。或者至少能有点事做。"
    scene c000_s001_035 with Dissolve(0.5)
    u "所以，你有对象了吗？"
    k "没有，还没有。"
    u "所以我猜，你还没计划过任何细节咯？"
    k "也许想了一点点。不过在确定时间和地点之前，很难做什么。"
    scene c000_s001_036 with Dissolve(0.5)
    "你和同事之间可以有不同类型的关系。大多数人属于那种你在办公室里见得到、但并不熟；或者说还不够熟到能多说两句客套话以外的话的人。也许你知道他们的名字。又或者，他们只是“早上总拿着贝果的那个金发女人”。"
    "再就是那种你没法忍受的人，或因为这或因为那。他们要么懒，要么就是不能信任——不能保证他们不把事情搞砸。遗憾的是，这类人往往身居管理层，或者正在拼命想爬公司那架梯子。"
    "然后是真正的工作朋友。你在办公室里和他们共度时间，但他们不会走进你的非工作生活。下班后也许会一起喝一杯，但很少有人能在两个圈子之间切换。就算做不到，有他们在也能帮那八个小时熬过去。"
    scene c000_s001_037 with Dissolve(0.25)
    "劳拉·米尔斯对我来说就属于那一类。她在办公室的时候，我们相处得不错。一起闲晃，一起扯淡。我想如果她一个月能在两三天以上，我可能就会跟她倾诉我的婚姻问题了。要是她不住在外地，我们或许会出去喝一杯、随便聊聊。"
    "劳拉是外勤代表。她在这一带跑来跑去，跟客户打交道，通常也要处理冒出来的各种客诉。每周没有哪一周不接到她打来的电话，调整订单或者报修设备。"
    o "他就是在吊着她，仅此而已。"
    scene c000_s001_038 with Dissolve(0.25)
    l "闭嘴吧，奥蒂斯。你自己过得惨，不代表别人也是。"
    menu:
        "保持沉默":
            "最好别掺和进去。劳拉和奥蒂斯从来就不对盘，我不想站队。"
            scene c000_s001_039 with Dissolve(0.25)
            j "嗨，劳拉。"
        "附和劳拉。\n[rgr](劳拉 好感 +1)":
            $ l_friend += 1
            scene c000_s001_039 with Dissolve(0.25)
            j "不地道，老兄。不地道。不是每个人都像我们这样，对爱情满腹怨气。*轻笑*"
    scene c000_s001_040 with Dissolve(0.25)
    l "[player_name]，你回来了。太好了。我得跟你聊两句。等一下，走之前。"
    j "好啊好啊。你忙完我还在。"
    "这时他们一起去了休息室。除了劳拉和奥蒂斯之间的紧张气氛之外，我也感觉卡莉不太爱在人前多说话。而且奥蒂斯或者我让她不自在，也完全不奇怪。"
    scene blank with Dissolve(2)
    scene c000_s001_041 with Dissolve(2)
    l "好啦，本周份的“跟另一个女人说话”配额也用完了。我跟你讲，这份工作绝对是个香肠盛宴。"
    j "作为香肠之一，{a=https://tvtropes.org/pmwiki/pmwiki.php/Main/IResembleThatRemark}我完全符合这句形容{/a}。今天剩下的时间你都在吗？"
    scene c000_s001_042 with Dissolve(0.25)
    l "在的。我有几封邮件要处理，可能会变成和拨款部的卡尔通电话。在办公室处理比在路上或者在客户那边方便。"
    j "唉。听起来真有意思。"
    scene c000_s001_043 with Dissolve(0.25)
    l "对。而且我周一要去南区跑一圈，接下来几天都会在那一带。回头再聊，好吗？"
    j "嗯嗯。下午咖啡加八卦。"
    scene c000_s001_044 with Dissolve(0.25)
    "我挺喜欢劳拉的。她是那种“不废话”的人，是自己人中的一个。已婚，三十多快四十，儿子刚上大学走掉。我见过她丈夫基思一次。高个子，很壮，像是打运动的。"
    scene blank with Dissolve(1)
    scene c000_s001_045 with Dissolve(1)
    "到下班时，奥蒂斯已经被咳嗽折磨得够呛。他脸色苍白（比平时更苍白）。我让他早点走，好好休息。"
    scene c000_s001_046 with Dissolve(0.5)
    k "嘿，我先走行吗？我活儿干完了，晚上还有饭局。"
    j "行啊。周末愉快。"
    k "你也是。"
    scene c000_s001_047 with Dissolve(0.5)
    "人挺好的姑娘。内向，不太合群。但她很努力工作。而且长得也不赖。"
    scene c000_s001_048 with Dissolve(0.5)
    l "你很快就走？"
    j "靠，你还在这儿？"
    scene c000_s001_049 with Dissolve(0.25)
    l "*笑* 这反应倒不在我意料之中。对，我正准备回家。"
    j "赶紧走。说真的。你通勤要一小时。别在这儿多待一分钟。"
    scene c000_s001_050 with Dissolve(0.25)
    l "这话从你嘴里说出来可真够讽刺的。"
    menu:
        "你有要回家的理由。\n[rrd](劳拉 焦虑 +1)":
            $ l_anxiety += 1
            j "你有要回家的理由。"
            scene c000_s001_051 with Dissolve(0.25)
            l "哎哟。那别待太久。晚安，周末愉快。"
            j "你也是。"
        "[gr]我很快就走。":
            j "我很快就走。我发誓。"
            scene c000_s001_051 with Dissolve(0.25)
            l "最好是。晚安，周末愉快。"
            j "你也是。"
    scene blank with Dissolve(2)
    stop music fadeout 2.0
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_13_615", transition=Dissolve(1.0))()
    pause
    $ Hide("june_13_615", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain fadein 2.0
    scene c000_s001_058 with Dissolve(2)
    "回家的路上车出奇地少，就算是在夏天的周五晚上也是如此。是不是很多人趁孩子放假都去度假了？我记得我上高中时好像确实有这么回事。"
    scene c000_s001_059 with Dissolve(0.5)
    "爸妈会计划去某个地方玩一周，比如佛罗里达或者科罗拉多。有那么一年，爸爸带我们去优胜美地公园露营。那可不是我想象中的乐趣，不过我确实看到了很棒的景色。"
    scene c000_s001_060 with Dissolve(0.5)
    "说到爸妈，我得赶紧给他打个电话。父亲节快到了。"
    scene blank with Dissolve(2)
    scene c000_s001_061 with Dissolve(2)
    "不知道为什么，能见度糟透了。哪儿着火了？我记得奥伦达州森林有一片失过火，火势吹进镇子的时候，连呼吸都成了受罪。"
    scene c000_s001_062 with Dissolve(0.5)
    "希望这次不是那种情况。只是傍晚来的怪雾。"
    scene c000_s001_063 with Dissolve(0.5)
    j "*咳嗽* *咳嗽*"
    "在它勾出什么毛病之前，最好赶紧进屋。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_14_815", transition=Dissolve(1.0))()
    pause
    $ Hide("june_14_815", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c000_s001_052 with Dissolve(2)
    "周六晚上，没有任何安排的周末夜晚。嗯，也不算完全没有安排。"
    scene c000_s001_053 with Dissolve(0.5)
    "我和几罐啤酒、一两袋薯片，还有电视上的篮球季后赛有个约。眼下，这是我休息夜最好的安排了。"
    scene c000_s001_054 with Dissolve(0.25)
    "是啊，以后我可能会重新去约会，但对我身心健康更正确的做法，是给自己留点时间。也就是给我自己，还有——希望是——一场不会在第三节就变成垃圾时间的比赛。"
    g1 "快点快点，再不走派对就要结束了。"
    scene c000_s001_055 with Dissolve(0.5)
    g2 "冷静点。反正这是校园里唯一的派对，其他人暑假基本都走了。要是再不抓紧，保安三点左右就得清场。"
    g1 "那我要在他们之前赶到。"
    scene c000_s001_056 with Dissolve(0.25)
    g2 "这可不能怪我，是你试了六条不同的裙子。"
    g1 "我想营造的是“来上我”的气氛。"
    scene c000_s001_057 with Dissolve(0.25)
    g2 "直接把胸露出来就行。或者去抓一两根鸡巴。现在，拎上啤酒，我们走。"
    "看来大学生也不是全都走了。"
    scene blank with Dissolve(2)
    stop music fadeout 2.0
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_16_812", transition=Dissolve(1.0))()
    pause
    $ Hide("june_16_812", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music officemain fadein 2.0
    scene c000_s001_064 with Dissolve(2)
    "又一个周一。又一个没有收获的周末，没能让一周五天变得比薪水更值钱。只能安下心来，尽我所能。"
    "奥蒂斯发消息说他不舒服，今天不来了。倒也不意外。新闻一直在反复播空气质量差、如何影响有健康问题的人。"
    scene c000_s001_065 with Dissolve(0.25)
    "而且公平地说，奥蒂斯本来大概就有健康问题。他每年从四月到十一月都在抱怨办公室太热。我从没见过他真的跑起来，也没见过他走快一点。"
    "所以，如果外面真的很糟（对我来说似乎也是），我能理解他需要一天恢复一下。也许去看个医生，拿到点什么能缓解的东西。要是我觉得他会听，我早就建议了。"
    scene c000_s001_066 with Dissolve(0.5)
    "自从这个办公点最近裁员之后，我已经习惯了有很多空桌子。当然，劳拉或查尔斯会定期过来，米奇迟早也会回来（罗杰偶尔），但现在只剩两个人了。"
    "卡莉刚刚上班。她正登录系统，处理那些还没转给账务的出货发票。她很在行。脑子快，眼又细。而且这还省得我干活。"
    scene c000_s001_067 with Dissolve(0.5)
    "只有我们两个人的好处是，我们俩都不是爱说话的人。在跟她一起工作之前，我一直以为自己只是内向。现在我明白了，我可能只是个不合群的老古板。"
    scene c000_s001_068 with Dissolve(0.25)
    "不过这倒不代表她没有朋友之类的。她一天到晚都在给好几个人发消息。或者更准确地说，她一直在给未婚夫发消息。"
    "我倒不介意。她很会多线程处理，活儿也能干完。说真的，她干这行比奥蒂斯强。时间久了，她会比我更强。"
    scene c000_s001_069 with Dissolve(0.25)
    "*叮铃*"
    scene c000_s001_070 with Dissolve(0.5)
    j "喂？环球办公用品，我是[player_name]。"
    l "{i}[player_name]，我是劳拉。{/i}"
    j "嗨劳拉，怎么了？需要什么吗？"
    l "{i}没什么大事，就是在外面跑一圈。你们那边还好吗？{/i}"
    scene c000_s001_071 with Dissolve(0.25)
    j "除了这里只有我和卡莉之外？我想是吧。奥蒂斯病假，其他人都不在这儿上班了。"
    l "{i}没别的了？{/i}"
    j "还能有什么？抱歉，我感觉我……就是，是不是该有什么情况？"
    l "{i}没，没有吧。也许只是……镇子这半边一直有浓烟，我有几个客户提到一到外面就呼吸困难。{/i}"
    scene c000_s001_070 with Dissolve(0.25)
    j "是啊，新闻里说过空气有问题。前几天奥蒂斯也在咳。所以确实有点情况。你出门戴口罩吗？"
    scene c000_s001_071 with Dissolve(0.25)
    l "{i}我车里有一个。办公室里还有吗？{/i}"
    j "我想还有。罗杰上次流感季的时候订过一批。我拿一个自己用，再看看卡莉是不是也需要。"
    scene c000_s001_072 with Dissolve(0.5)
    l "{i}好，挺好。我打算本周晚些时候过去一趟，希望到时候会好一些。{/i}"
    j "好啊。到时候见。"
    scene c000_s001_073 with Dissolve(0.25)
    k "刚才是劳拉？"
    "卡莉一般不会主动搭话，所以这有点让人意外。"
    menu:
        "[gr]她只是来问候一下。":
            j "呃，对。她来问候一下，说她本周晚些时候会过来。"
            scene c000_s001_074 with Dissolve(0.25)
        "她提到了一些关于烟的事。\n[rrd](卡莉 焦虑 +1)":
            $ k_anxiety += 1
            j "她提到了一些关于烟的事。"
            scene c000_s001_074 with Dissolve(0.25)
            k "哦，我还以为是今早的雾。难道是烟？"
            j "如果新闻报道可信的话，我想可能是。劳拉确实说过她本周晚些时候会过来。"
    k "哦？不错。"
    scene c000_s001_075 with Dissolve(0.25)
    "这段对话就这么结束了。"
    scene blank with Dissolve(2)
    stop music fadeout 2.0
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_16_525", transition=Dissolve(1.0))()
    pause
    $ Hide("june_16_525", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain2 fadein 2.0
    scene c000_s001_076 with Dissolve(2)
    "又是最后一个走。"
    j "*咳嗽* *咳嗽*"
    scene c000_s001_077 with Dissolve(0.5)
    "早该像我说的那样把口罩带上。"
    scene c000_s001_078 with Dissolve(0.25)
    "好了，走吧。"
    "*咔哒咔哒*" with hpunch
    "哦？车打不着火。今晚别跟我来这一套。我今晚实在没精力处理这种事。"
    scene c000_s001_079 with Dissolve(0.25)
    "来了。谢天谢地。但是……"
    j "*咳嗽* *咳嗽*"
    "闻起来像是有人在空调里抽烟了。算了。趁还没出什么事，赶紧回家。"
    scene blank with Dissolve(2)
    stop music fadeout 2.0
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_17_823", transition=Dissolve(1.0))()
    pause
    $ Hide("june_17_823", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music officemain fadein 2.0
    scene c000_s001_080 with Dissolve(2)
    "今天早上这儿安静得诡异。裁员之后，我向来是第一个到的。但外面也安静。路上几乎没什么车。像是在过某个全国性节日，却没人通知我。"
    "奥蒂斯没打电话，也没发消息。我就当他还病着，不算大事。"
    scene c000_s001_081 with Dissolve(0.5)
    "*叮铃*"
    "这么早就接到电话，还挺奇怪。"
    scene c000_s001_082 with Dissolve(0.25)
    j "喂？环球办公用品，我是[player_name]。"
    k "{i}嗨，我是卡莉……*嗞* {size=30}我可能会……*嗞* {/size}晚一点到。我的车打不着火……*嗞* {size=30}所以安德鲁送我过来。{/size}{/i}"
    "听起来我们这边信号很差。她的声音断断续续。"
    j "哦，好的，行。不急，我在这儿。"
    "简短直接，跟我们每一次交流一样。"
    scene c000_s001_083 with Dissolve(1)
    "趁着接打电话，我看看能不能联系上奥蒂斯，看看他需不需要什么。要是他病得厉害、需要见张熟脸，我回家路上可以顺道过去一趟。"
    "*嘟嘟嘟* *嘟嘟嘟* *嘟嘟嘟*"
    "没人接。那我留个语音。"
    j "嘿，老兄，我是[player_name]。希望你没事。要是不舒服就好好休息。需要什么的话——药啊、吃的啊——跟我说一声，我回家路上给你送过去。"
    scene c000_s001_084 with Dissolve(0.25)
    "我现在能做的也就这些。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_17_915", transition=Dissolve(1.0))()
    pause
    $ Hide("june_17_915", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    #Tuesday, June 17th, 9:15 am
    scene c000_s001_085 with Dissolve(2)
    k "抱歉抱歉。我在。"
    j "没事。车出问题了？"
    scene c000_s001_086 with Dissolve(0.25)
    k "就是打不着火。我对车了解不够，说不上是什么毛病。"
    j "是啊，我昨晚的车也很难打着。也许是烟雾闹的。"
    k "有可能。"
    scene c000_s001_087 with Dissolve(0.25)
    "唉，得开工了。今天的对话亮点，大概也就是这几通电话了。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_17_1142", transition=Dissolve(1.0))()
    pause
    $ Hide("june_17_1142", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    stop music fadeout 2.0
    scene c000_s001_088 with Dissolve(2)
    "我早上说这里安静是在开玩笑，但现在它成真了。外面死一般寂静，没有电话。天，连邮件都没有。"
    "我倒不是不能享受一天清闲，只是现在我宁愿忙一点。闲下来就会去想那些不该想的事，比如我前妻，以及那整件事是怎么走歪的。"
    "是啊，也许我结婚结得是有点早，但感觉她对这段婚姻也没那么上心。结婚第三年，我们就已经各自活在自己的小世界里。"
    scene c000_s001_089 with Dissolve(0.5)
    "卡莉站起来去打电话了。多半是想联系上安德鲁。也许我该早点吃午饭，看看能不能让人把她的车拖去修理厂检查一下。换作我就会这么做。"
    scene c000_s001_090 with Dissolve(0.25)
    "据我所知，安德鲁在镇子另一头的医院做信息化工作，所以顺路送她对他来说可不是一小段路。"
    k "哦。哦，天哪！"
    scene c000_s001_091 with Dissolve(0.25)
    play music menumain fadein 4.0
    "出事了。"
    j "没事吧？"
    scene c000_s001_092 with Dissolve(1)
    k "我……什么……怎么回事……"
    scene c000_s001_093 with Dissolve(0.5)
    j "呃。我……不知道。搞什么？"
label chapter01:
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("chapter01", transition=Dissolve(1.0))()
    pause
    $ Hide("chapter01", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    #########Chapter 01
    #1) Toxic fog. Kallie calls BF again. No response. EXTRA. Calls 911
    scene c000_s001_093 with Dissolve(2)
    $ k_anxiety += 1
    j "这他妈到底是什么？我想说这是雾，但雾不长这个像呕吐物的颜色。"
    scene c001_s001_001 with Dissolve(0.5)
    k "呃，那是烟，还是……"
    j "不知道。一般来说雾到上午就会散。所以烟这个说法挺合理。最近空气质量一直很差。"
    scene c001_s001_002 with Dissolve(0.25)
    k "我……我给安德鲁打个电话，看看他那边是不是也一样。"
    j "是啊，我也想知道是只有我们这边这样，还是到处都这样。"
    "这不正常，可我也解释不了。我倾向于认为这是某场没被本地新闻报道的火情产生的烟。我应该出去看看是什么情况。"
    scene c001_s001_003 with Dissolve(1)
    "卡莉看起来在担心。或者，表现出她能表现出的那么担心。"
    k "该死。"
    scene c001_s001_004 with Dissolve(0.5)
    j "都没事吧？"
    scene c001_s001_005 with Dissolve(0.25)
    k "我联系不上安德鲁。事实上，我连信号都没有。一格都没有。"
    j "真的？我看看我的手机。"
    scene c001_s001_006 with Dissolve(0.25)
    j "唔……"
    "没信号。没有拨号音。"
    k "怎么样？"
    menu:
        "我也没信号。\n[rrd](卡莉 焦虑 +1)":
            $ k_anxiety += 1
            j "我也没信号。真怪。"
            scene c001_s001_008 with Dissolve(0.25)
            k "……"
            j "我……对，我试试座机。就算信号塔有问题，办公室的座机应该还能打出去。"
        "[gr]试试座机。":
            j "我试试座机。就算信号塔有问题，办公室的座机应该还能打出去。"
            scene c001_s001_007 with Dissolve(0.25)
            k "好。"
    scene c001_s001_009 with Dissolve(1)
    "没有拨号音。不妙。我打给……奥蒂斯。这是我唯一能当场背出来的号码。"
    scene c001_s001_010 with Dissolve(0.25)
    "没人接。只有杂音。"
    k "怎么样？"
    menu:
        "没人接。":
            j "奥蒂斯不接。我试试别人吧。比如劳拉。"
        "试试劳拉。\n[rgr](卡莉 好感 +1)":
            $ k_friend += 1
            j "我试试劳拉。她一定会接电话。"
            scene c001_s001_011 with Dissolve(0.25)
            k "好。她应该会在。"
            "还是没人接。操，这到底是怎么了？"
    scene c001_s001_012 with Dissolve(0.25)
    j "好吧，她那边也没人接。我再死马当活马医一次。打 9-1-1。"
    k "哦？那倒是个办法。"
    "希望紧急服务没忙不过来。总不能只有我们为这事惊慌失措。"
    "又没有拨号音。操。"
    scene c001_s001_013 with Dissolve(0.25)
    k "没人接？"
    j "没有。这让我怀疑是不是服务断了。该不会是账单没交吧？"
    scene c001_s001_014 with Dissolve(0.25)
    k "那也解释不了手机信号也一起没了。"
    j "对，解释不了。你说得对。我应该……你知道吗？我去看看隔壁商家是不是也出问题了。街角那家家具店，也许。"
    scene c001_s001_015 with Dissolve(0.25)
    k "就这种东西，你还要出去？"
    j "我想知道是雾还是烟，出去一趟两个问题就都有答案了。"
    scene c001_s001_016 with Dissolve(0.25)
    k "好、好的。"
    j "我不会去太久。"
    scene blank with Dissolve(2)
    scene c001_s001_017 with Dissolve(2)
    "哦，哇，外面一样糟。而且天哪，真难呼吸。刺得……"
    scene c001_s001_018 with Dissolve(0.5)
    j "*咳嗽* *咳嗽*" with hpunch
    "操，真的是在烧。呼吸的时候在烧。露在外面的皮肤上也在烧。感觉像是有人往我手上和脸上喷了酸。"
    scene c001_s001_019 with Dissolve(0.25)
    j "嘶，嘶，嘶，操————~~~"
    "得回去了。完全没料到会这样。"
    scene blank with Dissolve(2)
    scene c001_s001_022 with Dissolve(2)
    j "靠，靠，靠。刚才那一下……操。"
    k "你已经回来了？"
    scene c001_s001_023 with Dissolve(0.25)
    j "哦，是啊。外面不太妙。"
    k "哇，你脸都红了。"
    scene c001_s001_024 with Dissolve(0.25)
    j "更像是烧伤了。外面那玩意儿烧得跟火一样。我走到停车场就不得不折返。感觉所有露在外面的东西都在着火。*咳嗽*"
    scene c001_s001_025 with Dissolve(0.25)
    j "听着，我得去洗手间试着把这些从……全身冲掉。要是我没把皮搓破，就马上回来。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c001_s001_020 with Dissolve(2)
    play music insideday fadein 2.0
    "好了，我觉得最严重的那些冲掉了。手、脸、脖子，头发上冲了点水，眼睛里溅了一点。真想洗个澡，但只能这样了。"
    "卡莉肯定没想到我会这么快就冲回来。希望我那样闯进来没吓到她。过去一个小时我一直搞不清发生了什么，而联系不上任何人更是雪上加霜。"
    scene c001_s001_021 with Dissolve(0.25)
    "说到这个，不知道她联系上她那位了没有？或者给他发了消息？我走的时候她应该还在打。"
    scene blank with Dissolve(2)
    scene c001_s001_026 with Dissolve(2)
    j "好多了。至少不再像是得了世界上最严重的晒伤。"
    "她在哪儿？我去找找看。这地方不大，她走不远。"
    "除非她试着出去了。"
    scene c001_s001_034 with Dissolve(1)
    j "哦，你在这儿啊。"
    "正盯着手机。看起来有点狼狈。考虑到刚才的情况，也情有可原。"
    k "我、我打不出去。电话打不通。短信也发不出去。"
    scene c001_s001_035 with Dissolve(0.25)
    j "我……嗯。"
    k "我、我、我……你试过吗……哦，哦，哦……"
    scene c001_s001_036 with Dissolve(0.25)
    k "喂？喂？911？有人吗？求你接电话。"
    menu:
        "告诉她你已经试过了。\n[rrd](卡莉 好感 -1)":
            $ k_friend -= 1
            j "嘿，我已经试过了。"
        "[gr]让她自己去试。":
            "她在这儿有点崩溃，不过告诉她“我已经试过了”并不会让情况变好。我想，她现在这个状态，只有亲自去做，这事才会真正落到她心里。"
    scene c001_s001_037 with Dissolve(0.5)
    k "快接、快接。谁都行。{i}求你了。{/i}"
    "我会说她应对得很糟，可我也说不准我们{b}应该{/b}怎么反应，因为我根本没搞懂这他妈到底是怎么回事。"
    scene c001_s001_038 with vpunch
    k "操————！"
    j "嘿，嘿，没事的。我们会想出——"
    scene c001_s001_039 with hpunch
    j "卡莉？等一下。你要去哪儿？"
    "她要走了？这可不行。"
    scene c001_s001_040 with Dissolve(0.25)
    j "卡莉，别出去！这件事听我的。"
    "靠。只希望她出去看到外面那副样子，能在被烧得太惨之前自己掉头回来。"
    scene c001_s001_041 with Dissolve(1)
    "说到这个，刚才那他妈到底是什么？一种像酸一样灼烧的浓雾。我想拿“罕见的天气现象”开个玩笑，但这事正变得严重起来。或者至少，是变得很麻烦。"
    scene c001_s001_042 with Dissolve(0.25)
    "你知道过去一个小时左右我什么都没听到吗？车流声。汽车声。天哪，你都会以为这下动静该让救援车辆满城乱窜了。"
    scene blank with Dissolve(1)
    scene c001_s001_043 with Dissolve(1)
    "她出去有一阵子了。多久了？很难说准。我尽量不让自己慌，但我的时间感已经不准了。感觉像是她已经走了十五、二十分钟，顶多大概也就五分钟。不过我还是该出去找找她。"
    scene c001_s001_044 with Dissolve(0.25)
    play sound doorclose
    "哦，谢天谢地她回来了。"
    k "嘶！嘶！疼疼疼~~~！好痛。痛死了。我、我、我……"
    scene c001_s001_045 with Dissolve(0.25)
    j "冲掉它！去洗手间拿点肥皂冲掉！这件事听我的。"
    k "好、好吧好吧好吧 *呻吟*"
    scene blank with Dissolve(1)
    scene c001_s001_046 with Dissolve(1)
    "看起来她和我经历了一样的事。走进那片……雾？烟？不管那是什么……一沾上就开始烧。"
    "我能听见水声。别的就没什么了。希望她没事。"
    menu:
        "别管她。":
            "就给她点时间吧。她不需要被催。"
        "问一下。\n[rgr](卡莉 好感 +1)":
            $ k_friend += 1
            scene c001_s001_047 with Dissolve(0.25)
            j "你在里面还好吗？需要帮忙吗？"
            k "嗯。我死不了。"
            "听起来她那边不太好。她的神经大概已经绷得很紧了。这也完全说得通。我自己也不是什么沉得住气的模范。"
    scene c001_s001_048 with Dissolve(0.5)
    play sound doorclose
    k "*叹气*"
    j "好些了吗？"
    scene c001_s001_049 with Dissolve(0.25)
    k "大概吧。好一点。真的，好一点了。至少不像皮肤要蜕掉一样。不过，这……我不知道。"
    scene c001_s001_050 with Dissolve(0.25)
    k "我只是想着，出去的话信号可能会好一点。*抽鼻子*"
    j "说实话，我出去的时候根本没考虑这个。我只是想着去敲一下邻居的门，看看他们是不是也电话有毛病。现在看来，那似乎也没那么重要了。"
    scene c001_s001_051 with Dissolve(0.25)
    k "……"
    j "看样子你在外面也联系不到人？"
    scene c001_s001_052 with Dissolve(0.25)
    k "没有。"
    j "*叹气* 好吧，不妙。我……我也不知道怎么办。"
    scene c001_s001_053 with Dissolve(0.25)
    k "要是我有车就好了，我就能钻进去直接开走。看看是不是只有{i}这里{/i}这样。"
    j "像是局部现象？这主意其实不赖。我去……"
    "上次我根本没走到车那儿。当然这次我可以跑过去。不过我可能得先戴个医用口罩。这里应该有那东西吧？"
    scene c001_s001_054 with Dissolve(0.25)
    j "就是疫情期间我们订的那种 N95 口罩？啊糟糕，那时候你还没来。"
    k "罗杰办公室那些？劳拉跟我说过，我刚来那周她提过。"
    j "哦，真的？那她记性真好，你也没忘。我去拿一个。"
    scene c001_s001_055 with Dissolve(0.25)
    k "你打算怎么办？"
    j "我要拼命冲向我那辆车。发动它，碾过前门，按响喇叭，然后我们他妈的离开这儿。行了吧？"
    scene c001_s001_056 with Dissolve(0.25)
    k "哦，好。我……好吧。你觉得口罩有用吗？"
    j "不会更糟。也许我看看他有没有外套可以穿。"
    scene blank with Dissolve(1)
    scene c001_s001_027 with Dissolve(1)
    "罗杰抽屉里有一盒口罩。大概是公司说必须订，他就订了，然后一直没用。我拿了一个，又拿了他挂在衣帽架上的一件外套，决定再赌一把。"
    scene c001_s001_028 with Dissolve(0.25)
    "跑得像有恶鬼在追我。那件外套已经让我热得像教堂里的婊子，但至少胳膊不会烧着了。还有这一口一口的玩意儿。"
    "可手和脸呢？已经开始感觉像在做化学换肤了。"
    scene c001_s001_029 with Dissolve(0.25)
    "快点，开了。没时间浪费。"
    scene c001_s001_030 with Dissolve(0.25)
    "好，进来。里面看着一切正常。给她发动一下试试。"
    scene c001_s001_031 with Dissolve(0.5)
    "*哒哒哒* *咔哒* *咔哒*"
    "这可不妙。"
    "*哒哒哒哒哒* *咔哒*" with vpunch
    scene c001_s001_032 with Dissolve(0.25)
    "操，不会吧。别告诉我这玩意儿还在搞我的车？"
    scene c001_s001_031 with vpunch
    "*哒哒哒哒哒哒哒哒*"
    scene c001_s001_032 with Dissolve(0.25)
    j "操——————！！！"
    scene c001_s001_033 with Dissolve(0.25)
    "我……我完全搞不懂这里到底他妈在搞什么，但我对耐心和理智的掌控真的快要崩了。没有座机。没有手机。车打不着火。手和脸都在痛。我只想……"
    "我只想喝一杯。很多杯。喝到麻木。再也不用去管这些狗屁倒灶的事。"
    scene c001_s001_057 with Dissolve(0.25)
    "但我不能。我得回去告诉卡莉这个坏消息。也许还得设法让她打起精神，因为她联系不上安德鲁，已经开始慌了。至于我？我还能打给谁？我前妻？"
    "好，在跑回去之前先深呼吸一下。"
    scene blank with Dissolve(1)
    scene c001_s002_001 with Dissolve(1)
    play sound doorclose
    j "靠，靠，靠。*气喘* *气喘*"
    k "我没听见你车开过来的声音。抱歉。"
    scene c001_s002_002 with Dissolve(0.25)
    j "*气喘* 车打不着火。"
    k "哦？"
    scene c001_s002_003 with Dissolve(0.25)
    j "对。前几天它就打火有点毛病，但我当时没当回事。可能是电瓶没电了。"
    k "我今天的车也打不着火。"
    j "唔，真的吗？"
    scene c001_s002_004 with Dissolve(0.25)
    j "好吧，那个……我得再洗把脸。马上回来。"
    k "好、好吧……"
    scene c001_s002_005 with Dissolve(0.5)
    k "*抽鼻子*"
    scene blank with Dissolve(2)
    scene c001_s002_006 with Dissolve(2)
    "好吧，至少知道洗手间里的肥皂能把这东西洗掉了。真不敢想如果我需要做个医疗级的冲洗才能搞定会怎么样。不过，那也等于假设了很多我现在根本不知道的事。"
    scene c001_s002_007 with Dissolve(0.25)
    "比如，这东西是从哪来的。它是什么。会不会自己消失。为什么电话打不通。为什么我的车启动不了。"
    "还有，卡莉在哪儿？"
    scene c001_s002_008 with Dissolve(0.5)
    j "你在这儿。还好吗？我是说，我知道答案肯定不是“好”，但是……"
    scene c001_s002_009 with Dissolve(0.25)
    k "我、我、我还是联系不上任何人。短信发不出去。没人接电话。上不了网。"
    j "手机信号可能受这……雾的影响。"
    scene c001_s002_010 with Dissolve(0.5)
    k "但办公室这边有无线网络。"
    j "嗯……我没想到这个。我想它跟座机一起断了吧。应该是同一家公司的服务。"
    scene c001_s002_011 with vpunch
    k "我们怎么办？总不能就这么待着吧？"
    j "我……我不太想留下。但看起来确实不太妙。"
    scene c001_s002_012 with Dissolve(0.25)
    "她开始慌了。就算她平时那么镇定，我也知道这种情况把她彻底打乱了。对我也一样。"
    menu:
        "说得直白点。":
            j "我在外面没看到其他人。连车声都没听到。所以我猜很多人跟我们一样被困住了。希望这很快过去，不然我们就得开始担心错过饭点了。"
        "[gr]试着让她打起精神。\n[rgr](卡莉 焦虑 -1)":
            $ k_anxiety -= 1
            j "但我敢肯定这就是那种常见的天空异象……"
            j "唉，我现在都在等一家 Waffle House 开门了。他们有专门派往灾区的团队，能就地开火做饭。"
    scene c001_s002_013 with Dissolve(0.25)
    k "天哪……吃饭。我从早上到现在竟然一次都没想过要吃东西。"
    j "我也没想过。外面那玩意儿进到嘴里，会留下特别恶心的味道。"
    scene c001_s002_014 with Dissolve(0.25)
    k "我知道你说的什么感觉。"
    j "我冰箱里有些剩菜。可以分你一点。"
    scene c001_s002_015 with Dissolve(0.25)
    k "呃……不了，我抽屉里有些蛋白棒。顶一顶应该够了。"
    j "好吧。我去拿，希望几个小时后情况能好转。"
    scene c001_s002_016 with Dissolve(0.25)
    "我说这话的时候自己都不信。不管外面在搞什么，都不像是短时间内能解决的样子。"
    k "*咳嗽*"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c001_s002_017 with Dissolve(2)
    play music insideday2 fadein 2.0
    "我们白等了。我不知道我们俩是不是都只是在指望情况能自己好转，或者指望有人开车路过、发现我们被困在这儿。我们不会那么走运的。我知道。"
    scene blank with Dissolve(1)
    scene c001_s002_018 with Dissolve(1)
    "越接近日落，就越难相信会有什么好转。现在不会。明天早上也不会。外面一片死寂，没有任何动静，这让人心里发毛。我知道平时的车流本来就少，何况大学生们都放假了。"
    "但眼下这种情形，就像飓风来临前沿海小镇的人仓皇出逃时的那种死城。"
    scene c001_s002_019 with Dissolve(1)
    "这时候卡莉已经明显有些撑不住了。她联系不上任何人，更别提安德鲁；继续待在这里也没什么盼头。她用手机、用办公室电话试了无数次，得到的都只有死一般的沉默。"
    scene c001_s002_020 with Dissolve(0.5)
    k "有没有好一点？"
    j "说不准。现在天黑了，看起来没那么清楚了。"
    scene c001_s002_021 with Dissolve(0.25)
    k "不过你闻得到吧，对吧？还是只有我闻得到？"
    j "你一说，还真是。像电池酸，或者变酸的牛奶。"
    scene c001_s002_022 with Dissolve(0.25)
    k "*呻吟* 唉，谢了。我刚才还有点饿，现在不会了。"
    j "蛋白棒对你没用吗？"
    scene c001_s002_023 with Dissolve(0.25)
    k "我吃了两根，但顶不上一顿正经饭。"
    j "你去看看休息室的自动贩卖机了吗？"
    scene c001_s002_024
    k "去了。它现在不接受信用卡。"
    j "没网？那如果很快还是不好，我就琢磨着把它撬开。"
    scene c001_s002_025 with Dissolve(0.25)
    k "那样你不会有麻烦吗？"
    j "让他们来抓我好了。"
    scene c001_s002_026 with Dissolve(0.25)
    k "有道理。"
    scene c001_s002_027 with Dissolve(0.5)
    j "我想……我想我们今晚得在这儿凑合了。你没车，我的车打不着火，而外面那副鬼样子，我他妈肯定不可能走回家。"
    k "唉。别说了。我……*叹气*"
    j "这话不得不说。整件事都很糟，但我们只能面对现实。"
    scene c001_s002_028 with Dissolve(0.25)
    k "然后呢？"
    j "希望这东西一夜之间就散了。或者这只是局部的气象异常。也许下点雨就没事了。散了就好了。"
    scene c001_s002_029 with Dissolve(0.25)
    k "你还觉得是天气的问题？"
    j "不知道。但也许太阳出来能烤掉一部分。或者风大起来把它吹散。哪怕只剩一点点，也够我们走到车那边把它打着。或者我们跑去最近还开着门的楼。也许是街那头的{i}汉堡店{/i}。"
    scene c001_s002_030 with Dissolve(0.25)
    k "现在别提吃的。"
    scene c001_s002_031 with Dissolve(0.5)
    "那不是什么好局面，也许这也不是什么好计划，但我当时脑子里确实不太正常。所有打给可能认识的人的电话都没人接。电话服务断了。"
    scene c001_s002_032 with Dissolve(0.5)
    "外面安静得诡异。当然，要是别人的车都跟我这台一样，这就说得通了。也许有几百上千辆（甚至更多）同样困在原地动不了。"
    "而卡莉……她对现状并不满意，但我感觉她跟我一样，当时也想不出更好的办法。可她的神经还能撑多久？联系不上她那位只会让情况更糟。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c001_s002_033 with Dissolve(2)
    play music nightmain2 fadein 2.0
    "天黑下来的时候，我们也没别的可做。于是挑了几个地方当临时床铺。"
    scene c001_s002_034 with Dissolve(1)
    "卡莉占了前厅的沙发。我在后面拿了一张带软垫的长凳。"
    scene blank with Dissolve(2)
    scene c001_s002_035 with Dissolve(2)
    "有一阵子我就那么躺着。对一个习惯熬夜的人来说，不先把自己精神上累垮就直接睡下，感觉很奇怪。当然，这里也没有电视或流媒体可以消磨。"
    "不过这也让我重新想了想我们的麻烦。明天早上，我得再试试我的车。"
    "到底是什么让它打不着火？是这层烟霾（烟？雾？我他妈根本不知道该叫什么）钻进了发动机？我对车没熟到能自己修的份上。"
    scene c001_s002_036 with Dissolve(0.25)
    "我快睡着时注意到，办公室里的空气有点闷了。太阳落山，气温降到六十多华氏度，空调也好一阵子没开，屋里就有点不太舒服。"
    "今晚我们正好赶上那个空调和暖气都不管的死角。这在夏天很奇怪。这也是雾带来的副作用吗？"
    scene blank with Dissolve(2)
    scene c001_s002_037 with Dissolve(2)
    "我不记得自己是什么时候醒的，但糟糕的睡铺加上心里有事，让人很难真正休息好。"
    scene c001_s002_038 with Dissolve(0.25)
    "出于好奇，我爬起来决定往外看看。"
    scene c001_s002_039 with Dissolve(1)
    "我溜到办公室前面，发现外面一片漆黑。漆黑，死寂。仿佛世界其他地方都不存在了。"
    "不止一次，我看到那些有毒的云团来回移动。"
    scene c001_s002_040 with Dissolve(1)
    "明天我得做点什么。躲在这里不是办法。要么把车修好，要么看看能不能进附近某栋楼。"
    scene c001_s002_041 with Dissolve(0.25)
    "我在潜意识里想，食物可能会变成一个问题。但我没打算待这么久。"
    scene blank with Dissolve(2)
    stop music fadeout 2.0
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_18_715", transition=Dissolve(1.0))()
    pause
    $ Hide("june_18_715", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday fadein 2.0
    scene c001_s003_001 with Dissolve(2)
    "那一觉绝对谈不上好。也不算最糟。在我和我前妻分开、她把我赶出去之前，我有过几个晚上是睡在沙发上的。几个睡不着的夜晚，气得要命，为着一场根本不会有结果的争吵。"
    scene c001_s003_002 with Dissolve(0.5)
    "如果我当时能看清在她心里我们早就离了，我大概就不会费那个力气去维系了。"
    "不过我现在浑身僵硬，真他妈需要点咖啡因。至少我们有咖啡机。我看看能不能煮点出来。多煮点。另外，早餐应该也不坏。我想我抽屉里藏了点东西。"
    scene c001_s003_003 with Dissolve(0.5)
    "我该去看看卡莉了。看看她睡得怎么样。"
    scene c001_s003_004 with Dissolve(0.5)
    $ k_anxiety += 1
    "好吧，她醒了。还盯着手机。该问的问题我还是得问，哪怕我已经知道答案。"
    j "早上好，卡莉。你睡得还好吗？"
    scene c001_s003_005 with Dissolve(0.25)
    k "……"
    j "没回音？"
    scene c001_s003_006 with Dissolve(0.5)
    $ k_desire += 1
    k "嗯？哦。抱歉。我只是……"
    j "你的电话和短信都没回音？"
    scene c001_s003_007 with Dissolve(0.25)
    k "没有。我……我从来没和安德鲁、朋友们断联这么久过。或者是……"
    scene c001_s003_008 with Dissolve(0.25)
    k "你那边有谁联系你了吗？"
    j "这边也是一片寂静。"
    "我本来就不是个爱打电话的人。也许一个月给我妈打一次。节假日或者有人过生日的时候会多一点。"
    scene c001_s003_009 with Dissolve(0.25)
    "卡莉被这事弄得心神不宁，这是理所当然的。换成我？我表面上还撑得住一些。我确实担心，但心里有一部分觉得这就是那团雾造成的通信中断。一个局部现象，很快就会过去。对吧？"
    "我是说，如果这是全国性的，我们之前不是早就该听到消息了吗？你看，我实在无法相信这种鬼东西会突然在所有地方同时冒出来。听起来根本不可信。"
    scene c001_s003_010 with Dissolve(0.25)
    k "我……我真的已经……很久没有这样了。"
    menu:
        "安慰她。\n[rgr](卡莉 焦虑 -1)":
            $ k_anxiety -= 1
            j "嘿，他没事。你家人也没事。就算他们也像我们一样被困住了，那他们大概也只是躲在家里或者公司，等这一切过去。"
            k "你觉得呢？"
            j "是啊。只有傻子才会在这鬼天气里出去，还意识不到皮肤被烧、呼吸困难是件坏事。而你不会跟傻子交往，对吧？"
            scene c001_s003_011 with Dissolve(0.25)
            k "没有。谢谢。为……"
            "让你笑了一下？应该的。我能做的最起码的事。"
        "保持沉默。":
            "她其实只是在自言自语。我没必要插嘴。"
    scene c001_s003_012 with Dissolve(0.5)
    k "外面还是……那样吗？那雾？"
    j "我看看。我都还没走到那一步，只是想当然而已。"
    scene c001_s003_013 with Dissolve(0.25)
    k "好。我马上过去。"
    "{color=#ffcccc}糟了。我昨晚就把裤子脱了，因为屋里实在太闷。他倒没太在意。不过，他在我印象里也不是会介意这种事的人。{/color}"
    scene c001_s003_014 with hpunch
    k "*咳嗽* *咳嗽*"
    scene c001_s003_015 with Dissolve(1)
    k "怎么样？唉。还在外面。"
    j "在。不过比之前好一些。淡了。"
    k "是吗？"
    scene c001_s003_016 with Dissolve(0.25)
    j "是淡了一点。要是这样，我不如冲出去试试看能不能把车打着。试一下总没坏处。"
    k "怎么都比再在这儿睡一晚强。"
    j "确实。"
    scene c001_s003_017 with Dissolve(0.5)
    k "屋里挺暖和的。还是只有我觉得暖和？"
    j "有一点。其实挺闷的。就像空调没开。大概是那种不太热也不太冷、所以它干脆什么都不做的区间。而且我们平时也不会这么早来。"
    scene c001_s003_018 with Dissolve(0.25)
    k "说得通。"
    scene c001_s003_019 with vpunch
    "*咔哒*"
    k "哦。啊……"
    j "饿了？我知道我是。"
    scene c001_s003_020 with Dissolve(0.25)
    k "是啊。一点也不丢人。我这儿没什么吃的。我平时都在外面吃。而自动贩卖机又……"
    j "我看看能不能把它弄开。或者敲下来点什么。等一下，我抽屉里有零钱。先试试这个。"
    scene c001_s003_021 with Dissolve(0.25)
    k "好吧。你真想把钱花在这上头吗？"
    j "现在还没到彻底“各顾各的”时候。"
    "因为我还在指望这事会过去。就算是最糟的飓风，最后幸存者也得在几天内回归正常生活，而不是直接转去做{a=https://en.wikipedia.org/wiki/Survivalism}生存主义{/a}。"
    scene blank with Dissolve(2)
    scene c001_s003_022 with Dissolve(2)
    "我们享用这顿“不健康不均衡的早餐”的时候，我一直在琢磨要不要再出去一趟到车那边。也许再翻找一下，能找到别的什么帮我撑过这雾。"
    scene c001_s003_023 with Dissolve(0.5)
    "也许能找到手套。或者帽子。能让冲向停车场那一路少受点罪的东西。"
    scene blank with Dissolve(2)
    scene c001_s003_024 with Dissolve(2)
    "还好，我七拼八凑弄到了点有用的东西。"
    k "这身打扮真够呛。"
    j "是啊，反正我不会靠这个拿什么奖。"
    if k_friend >= 2:
        scene c001_s003_025 with Dissolve(0.25)
        k "可不适合第一次约会穿。"
        j "实用至上，抱歉了。*轻笑*"
    scene c001_s003_026 with Dissolve(0.5)
    k "你要去很久吗？"
    j "不知道。要是能把车打着，那就不会。祝我好运吧。"
    scene c001_s003_027 with Dissolve(0.25)
    k "怎么打？前天都发动不了，现在怎么就能了？"
    j "我希望雾淡一点的话，也许它造成的影响会消退。或者我只是想找点事做，因为干等着、指望有人来救我们这种做法不属于我。我必须做点什么。被困在这儿已经一整天了。"
    scene c001_s003_028 with Dissolve(0.25)
    k "我*叹气*……好吧。有道理。"
    j "就像我说的，祝我好运。"
    scene c001_s003_029 with Dissolve(0.25)
    "{color=#ffcccc}他没说错。什么都不做只会让我们毫无进展。但我对他能不能成功没什么信心。这不代表我不欣赏他去尝试。{/color}"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c001_s003_030 with Dissolve(2)
    play music outsideday fadein 2.0
    "也许只是心理作用，不过这身装备好像比刚才那套管用。还是能沾到一些，但现在不算太难受。而且感觉也没那么笨重了。当然，这也可能全是我的心理作用。"
    scene c001_s003_031 with Dissolve(0.5)
    "好了，我进去试试能不能把你打着。"
    scene c001_s003_032 with Dissolve(1)
    "什么都没有。真的什么都没有。没有咔哒声。没有发动机的咳嗽声。什么都没有。死了。彻底死了。操。"
    "好吧，既然我的车算是死了，我还有别的选择吗？这些别的车怎么样？估计也好不到哪儿去，而且我也没钥匙。这是不是意味着外面所有车都废了？那停在里面的呢？停车场？我不确定附近有没有。"
    scene c001_s003_033 with Dissolve(0.25)
    "要理清的事情实在太多了。我的车到底为什么打不着火？没电了？我能不能换个电瓶？操，要只是这样我就该烧高香了。可电话都断了，这东西感觉在干扰什么。"
    "可电和水还都正常。但电线是埋在地下的。水管也是。"
    scene c001_s003_034 with Dissolve(0.25)
    "你知道，从这儿到附近一家店不算太远。距离和我直接往回走差不多。我好奇有没有别人也困在各自的工作地点。要是能有几个邻居一起行动倒不错。"
    scene blank with Dissolve(2)
    scene c001_s003_035 with Dissolve(2)
    j "有人吗？有人吗？前门开着，那个……我想你懂的。"
    scene c001_s003_036 with Dissolve(0.25)
    "没人。说实话，我怀疑我几个月来、甚至更久，都没见过这里超过一两个人。还开着，纯粹是因为有人想赚点钱。"
    "这下他们的生意肯定彻底完了。"
    scene c001_s003_037 with Dissolve(0.25)
    "这儿有张床。大概比公司的沙发强，不过我不觉得搬过来能算多大改善。除非他们的休息室里有个塞满东西的冰箱。"
    scene blank with Dissolve(2)
    scene c001_s003_038 with Dissolve(2)
    j "叩叩。有人在吗？我是[player_name]，环球办公用品的。"
    scene c001_s003_039 with Dissolve(0.25)
    "果然这家店死透了。手机信号一断，这里面所有东西基本都没用了。至少眼下是。可不能把这当成永久状态。只是临时不便。"
    scene c001_s003_040 with Dissolve(0.25)
    "我要是更有进取心一点，也许会顺走几个再网上转卖。算了，太麻烦，而且我不是那种爱顺东西的人。至少今天不是。也许情况更糟的话就不一定了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c001_s003_048 with Dissolve(2)
    play music insideday2 fadein 2.0
    play sound doorclose
    k "哦，谢天谢地你回来了。我都开始有点担心了。"
    j "我本来想发消息告诉你情况，可是……"
    scene c001_s003_049 with Dissolve(0.25)
    k "我知道。你的车……？"
    j "还是死着的。而且我对车不够熟，打不开引擎盖看看发动机到底哪儿出了问题。我爸脑子里大概正在冲我大喊，说他当年费尽心思教我的那些全白费了。"
    j "换个轮胎？换个电瓶？行。再往后呢？那都是我花钱让别人去弄的。"
    scene c001_s003_050 with Dissolve(0.25)
    k "*咳嗽* 那你怎么去了这么久？"
    j "我在车里待着恢复了一下，顺便去看看附近那些楼里有没有人。"
    scene c001_s003_051 with Dissolve(0.25)
    k "听你这意思是没有。"
    j "基本没有。不过我只来得及查两个地方就得回来了。或者说是两个不是空的、也没锁门的地方。我之前真没意识到这附近有这么多店面是关着门的。"
    k "这么多店都歇业了，简直让人以为这个镇子要完了。"
    scene c001_s003_052 with Dissolve(0.25)
    j "确实。那家家具店——菲尔丁斯家具——是开着的，但里面没人。我猜他们看到情况不对就撤了。大概店面那几扇大窗户，让人很容易注意到雾正在涌进来。"
    j "街角那家手机店呢？里面也没人。我确实想过顺一部新手机以防万一，但现实很快就否定了这个念头。"
    scene c001_s003_053 with Dissolve(0.25)
    k "得有个人帮你激活 SIM 卡才行吧？"
    j "对。而且我也不觉得是手机的问题，更像是网络断了。对了，我得洗洗。这身确实管用多了，不过我怀疑是心理作用，手腕和后脖颈都在发痒。"
    scene c001_s003_054 with Dissolve(0.25)
    k "好。我……我就在附近。"
    scene c001_s003_055 with Dissolve(0.25)
    k "*咳嗽* *咳嗽*"
    scene blank with Dissolve(2)
    scene c001_s003_056 with Dissolve(2)
    "好些了。就算洗澡这件事纯粹是心理作用。"
    "但现在我得想点事情了。得想出个办法解决我们眼下的处境，因为连着两晚睡在这儿不是我愿意干的事。我知道她也不是。她有家人，还有未婚夫要陪。"
    scene c001_s003_057 with Dissolve(0.5)
    "我大概该去看看她，问问她情绪上怎么样了。"
    "是我多心，还是屋里有点闷？"
    scene c001_s003_058 with Dissolve(0.25)
    k "*咳嗽* *咳嗽*"
    j "嘿，你还好吗？最近咳得挺厉害。"
    "就像奥蒂斯打电话请病假之前那样。老兄，希望他没事。"
    scene c001_s003_059
    k "我、我今天一直觉得呼吸困难。好像屋里的空气不太好。"
    j "我倒没注意，因为我刚才还在外面。我们这儿有能开的窗户吗？你觉得把门打开通向外头是不是个坏主意？"
    scene c001_s003_060 with Dissolve(0.25)
    k "没帮助。或者我觉得没有。"
    j "检查一下窗户吧，确保我们没漏了缝。"
    scene c001_s003_061 with Dissolve(0.25)
    "嗯？后颈上湿漉漉的皮肤吹到凉风。这感觉可真够特别的。挺好，说明在出了这么多事之后它还正常工作。你会想……"
    "等一下。通风口……"
    scene c001_s003_062 with Dissolve(0.25)
    j "操。操！"
    k "怎么了？"
    j "空调。它在从外面吸空气。"
    scene c001_s003_063 with Dissolve(0.25)
    k "哦，呃……"
    j "我关掉它。把通风口封上。我们只是在把那玩意儿放进来。难怪你咳得这么厉害。"
    scene c001_s003_064 with Dissolve(0.25)
    k "啊。好。呃，罗杰原来的办公室附近还有个温控器。我、我去关。"
    scene blank with Dissolve(1)
    scene c001_s003_065 with Dissolve(1)
    "接下来的十五分钟里，卡莉和我关掉了空调，四处检查把通风口都封上。我也复查了窗户。这时候大概已经晚了。我能感觉到一团团雾已经渗进了楼里。"
    scene blank with Dissolve(1)
    scene c001_s003_066 with Dissolve(1)
    "之前关着的那些房间，情况比一楼的空气质量还糟。为了不让已经钻进来的东西继续扩散，我提议能关就关着。"
    scene blank with Dissolve(1)
    scene c001_s003_067 with Dissolve(1)
    "没过多久我就开始出汗，有点喘不上气。"
    j "好，暂时先这样。不是个很好的选项，但我宁愿屋里别变成外面那样。"
    scene c001_s003_068
    k "这里面很快就会又热又闷。"
    j "至少太阳没穿透这玩意儿，把这里变成桑拿房。不过，阳光能透进来，或许是个好兆头，说明这东西在变薄。"
    scene c001_s003_070 with Dissolve(0.25)
    k "然后呢？"
    j "不知道。我大概一直在期待这会像那种自然灾害，最后消防或者救援队会进场。或者国民警卫队。总得有人。因为这肯定会引起那些有能力做点什么的人的注意。"
    j "你看过飓风袭击南方那些地方的影像吧？那些地方被切断联系，只能等着救援和恢复队伍赶过去。"
    scene c001_s003_071 with Dissolve(0.25)
    k "是啊，听起来合理。我以前从没经历过这种事。我们是从北边搬下来的，那边最糟也就是大暴雪或者结冰。要多久才会有援助？"
    j "通常的话？视情况而定，可能要一天左右才能有人员和车辆进来。但这种事？我不知道他们在做什么。不过，希望我们不用等太久。"
    "那大概不是我该得到的答案。我也没有更好的说法。"
    scene blank with Dissolve(1)
    scene c001_s003_072 with Dissolve(1)
    "接下来的一个小时，我在办公室里转来转去，翻着抽屉，看能找到多少吃的和别的杂物。除了奥蒂斯抽屉里的一堆零食和更多的口罩，我基本没什么收获。"
    scene c001_s003_073 with Dissolve(0.5)
    "我想到，如果救援指望不上，也许我得给卡莉也凑一套类似的“出行装备”。以防我们决定转移到有食物的地方。或者有床的地方。"
    scene c001_s003_074 with Dissolve(1)
    "说到卡莉，我找到她的时候她正趴着睡着了。她昨晚大概没怎么睡好。再加上没有像样的东西可吃，以及情绪压力对人的消耗，我能理解。"
    "最好让她多休息。"
    scene blank with Dissolve(2)
    scene c001_s003_075 with Dissolve(2)
    $ renpy.sound.set_volume(.20, 0.0, channel = "sound")
    "天啊，我真需要点事做。光是待在这儿，甚至比朝九晚五当牛做马还折磨人。操。"
    "眼下这个局面，很快就让我最近的生活动荡显得不值一提了。现在？现在我他妈宁可能回那破公寓，看一场橄榄球，或者一部电影。或者真的，什么都行。"
    play sound gunshot
    scene c001_s003_076 with hpunch
    "*咔嚓*"
    j "操？"
    "那是枪声吗？听着不像是很近。但是——"
    $ renpy.sound.set_volume(1.0, 0.0, channel = "sound")
    scene c001_s003_077 with Dissolve(0.5)
    $ k_anxiety += 1
    k "那是什么声音？"
    j "哦，你醒了。我想……对，是枪声。单发。那个方向。"
    scene c001_s003_078 with Dissolve(0.25)
    k "你怎么知道？"
    j "我以前听过。你住在镇上某些地方的时候，可能会听到什么，大概是街角便利店那边发生枪击，或者毒品交易谈崩了。"
    scene c001_s003_079 with Dissolve(0.25)
    j "不过，那……那说明外面还有别人。所以我们不是完全孤零零的。"
    "先不提他们居然觉得有必要朝谁或者什么东西开枪。"
    scene blank with Dissolve(1)
    scene c001_s003_080 with Dissolve(1)
    "接下来一个小时，我们就那么站着，等着听到或看到任何别的动静。等确认不会再有别的事发生，卡莉就回她的沙发上去了。"
    scene blank with Dissolve(2)
    stop music fadeout 2.0
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_18_645", transition=Dissolve(1.0))()
    pause
    $ Hide("june_18_645", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain fadein 2.0
    scene c001_s003_081 with Dissolve(2)
    "到了傍晚，我们又要在这儿睡一晚这件事就板上钉钉了。那声枪响虽然让人兴奋，也说明这里不止我们，但并没有带来任何实际结果。"
    "盯着窗户看，也只能看到那团浓密翻涌的雾。"
    "虽然我在个人层面并不了解卡莉多少（内向 + 已订婚 + 同事 + 我自己那堆破事，这些加起来让我们没机会熟络起来），但我必须设想这件事对她生活的冲击。"
    "人很容易陷入某种固定的日常，而这种扰乱，哪怕对适应力最好的人来说也足以把一切搞砸。"
    scene c001_s003_082 with Dissolve(0.5)
    "我觉得我得给我们俩找点事做，这样这种孤立感才不会很快变成问题。所以我决定了一个行动计划，不管它有多含糊。做点什么，哪怕徒劳，也总比什么都不做强。"
    scene c001_s003_083 with Dissolve(0.25)
    j "听着，明天我打算再往外走远一点，看看周边能找到什么。往路那头大概一个街区有家店。我可以想办法进去，看能不能给你找件能出门穿的衣服。"
    k "那件外套还在吧？还有手套和口罩？"
    j "在，但你需要能包住头的东西。再有副眼镜也不坏。虽然比不上那种酷酷的护目镜，但聊胜于无。"
    scene c001_s003_084 with Dissolve(0.25)
    k "你的意思是，我们可能得徒步走出去？"
    j "不是不可能。不过眼下，我倒想看看我们能到哪儿而不费太大劲。再说了，你也不想一辈子闷在这里吧？"
    scene c001_s003_085 with Dissolve(0.25)
    k "*叹气* 是啊。而且我的衣服开始有点……"
    j "我不能保证给你弄套新行头，但如果我能进那家服装店，我会看看能带点什么回来。"
    scene c001_s003_086
    k "好。吃的呢？我……从贩卖机里弄出来的那些东西撑不了多久，而且也谈不上顶饱。我以前以为自己能吃素，现在却特别想来个汉堡。"
    j "*轻笑* 是啊，我自己也特别想连吃几个超值套餐。想到我们可能会在这儿待得比预想的更久，我该去找点吃的。"
    scene c001_s003_087 with Dissolve(0.25)
    k "隔壁街区那家快餐店呢？我知道得走过去一段，但他们应该有些吃的。"
    j "{i}汉堡店{/i}？对。那……我可以试试看。从我车那边走到家具店，再从那儿试着过去。这样中间也有几个能让我缓一缓的安全点。"
    scene c001_s003_088 with Dissolve(0.25)
    k "听起来你可能会在外面待挺久。我……我真希望我们有个能互相联系的办法。万一出了什么事。"
    j "比如对讲机？不确定那玩意儿在这儿能不能用。不过，要是感觉有什么不对劲，我会回来。现在可不是逞英雄的时候。"
    scene c001_s003_089 with Dissolve(0.25)
    k "我不知道“对讲机”是什么，不过好吧。谢谢。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_18_1043", transition=Dissolve(1.0))()
    pause
    $ Hide("june_18_1043", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c001_s003_041 with Dissolve(2)
    "好吧，还是睡吧。我算不上困，但今天也没别的可做了。不过我们总算有了个看起来像计划的东西。或者说，让卡莉觉得我们不只是在干等的东西。"
    "天啊，这里开始变得又潮又闷。裤子都要黏在腿上了。只要我别穿着这样在办公室里乱晃，她应该不会介意。"
    scene blank with Dissolve(2)
    scene c001_s003_042 with Dissolve(2)
    $ renpy.pause ()
    scene c001_s003_043 with Dissolve(0.5)
    "{color=#ffcccc}唉，我以前从来不知道自己睡在自己的床上能被宠成什么样。那张沙发……我想这就是我能指望的极限了。实在没什么感觉。太焦虑了。{/color}"
    scene c001_s003_044 with Dissolve(0.25)
    "{color=#ffcccc}[player_name]醒着吗？听着不像。天哪，晚上一个人待在这地方，外面一点声音都没有，还挺瘆人的。{/color}"
    k "[player_name]？"
    scene c001_s003_045 with Dissolve(0.25)
    "{color=#ffcccc}对，他睡着了。所以我也不算完全是一个人。这样就好。而且他也在努力不把事情弄得更糟。为此感到庆幸。{/color}"
    if k_friend >= 2:
        scene c001_s003_046 with Dissolve(0.25)
        "{color=#ffcccc}他人挺好的。从没让我觉得不舒服，不像奥蒂斯，或者查尔斯。再说劳拉喜欢他，那他肯定不错。我们就是不太说话。从来没理由说。{/color}"
        "{color=#ffcccc}我觉得我们俩都不太爱说话，只是程度不同。而且出于工作原因，他得比我多跟人打交道。{/color}"
    scene c001_s003_047 with Dissolve(0.25)
    "{color=#ffcccc}我去下洗手间，然后接着睡。我不该在白天打盹。那会让晚上更难休息。可闲着没事做也是很难受。{/color}"
    k "*叹气*"
    scene blank with Dissolve(2)
    stop music fadeout 2.0
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_19_708", transition=Dissolve(1.0))()
    pause
    $ Hide("june_19_708", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c001_s003_090 with Dissolve(2)
    "哎呀。早上好。伸个懒腰，把僵的地方活动开。在那张长凳上睡到第二个晚上之后，睡到家具店那张床上开始显得是个好主意了。"
    "我得在卡莉起来看到我“晨勃”之前把裤子穿上。"
    scene blank with Dissolve(2)
    scene c001_s003_091 with Dissolve(2)
    "一小时后，我们俩都醒了，一边嚼着贩卖机里的零食，一边聊我昨天提的那些计划。我要穿上装备，看看能不能走到服装店和{i}汉堡店{/i}。"
    "给卡莉弄件能出门穿的衣服固然有用，但我觉得更重要的是让我们吃上真正的食物。"
    play music menumain fadein 4.0
    "*砰* *砰* *砰*" with vpunch
    scene c001_s003_092 with Dissolve(0.25)
    j "我他妈到底听到了什么？"
    "有人在砸那边的窗户？是救援吗？"
    scene c001_s003_093 with Dissolve(0.25)
    l "嘿！里面有人吗！让我进去！我把工牌落在车里了，进不去。"
    k "劳拉？是劳拉！"
    scene c001_s003_094 with Dissolve(0.5)
    j "劳拉？他妈的怎么回事？"
    l "{size=33}[player_name]！？谢天谢地。让我进去。外面越来越糟了。{/size}"
    if persistent.ch1_complete == False:
        $ persistent.ch1_complete = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_chapter1", transition=slideright)()
        pause
        $ Hide("achievement_chapter1", transition=dissolve)()
        $ quick_menu = True
    stop music fadeout 2.0
    scene blank with Dissolve(2)
label chapter02:
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("chapter02", transition=Dissolve(1.0))()
    pause
    $ Hide("chapter02", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c002_s001_001 with Dissolve(2)
    play music insideday fadein 2.0
    j "我的天，劳拉。真没想到你会——偏偏是你——就这样直接走到大楼来。你没事吧？无意冒犯，但你看起来像是被狠狠折腾过。"
    scene c002_s001_002 with Dissolve(0.25)
    l "*咳嗽* *咳嗽* 唔~~~我先……*咳嗽* *咳嗽*" with hpunch
    "她的声音很哑。脸色通红，光是喘口气都很费劲。看不出她已经在外面待了多久。"
    scene c002_s001_003 with Dissolve(0.25)
    j "嘿，嘿，我先送你去洗手间。洗一洗。相信我。洗脸能让这东西好一些。至少可能没那么疼，也能减轻刺激。"
    menu:
        "让卡莉扶她过去。\n[rgr](卡莉 信任 +1)":
            $ k_trust += 1
            scene c002_s001_004 with Dissolve(0.25)
            j "卡莉，你能带她去一下洗手间吗？"
            k "呃，哦，对。我能。劳拉在这儿。我这就……"
            l "*咳嗽* 谢、谢谢 *咳嗽* *咳嗽*" with hpunch
            "她要是糟成这样，在外面肯定待了很久。等她把咳嗽压下去之前，我们没法跟她好好说话。我不记得劳拉以前有呼吸方面的问题，但这次把她呛出哮喘来了。"
            scene blank with Dissolve(2)
            scene c002_s001_005 with Dissolve(2)
            "劳拉是怎么到这儿来的，她肯定有一肚子故事。她在外面已经两天了吧？那她一定是在附近某个地方。我知道她这周本来打算顺道来趟办公室。只希望她别太惨。她那咳嗽听着很吓人。"
            play sound doorclose
            scene c002_s001_006 with Dissolve(0.5)
            k "好吧，我觉得她好一些了。呼吸多少稳住了。"
            j "太好了。我刚才真有点担心。"
            scene c002_s001_007 with Dissolve(0.25)
            k "她让我给她拿点喝的。有吃的也给她一点。她说过去两天一直在车里，什么都没吃。"
            j "好。我抽屉里还有些零钱。奥蒂斯那边也有，需要的话可以拿更多。饿了就翻翻他藏的零食。"
            scene c002_s001_008 with Dissolve(0.25)
            k "好好好。哦，她现在想跟你说话了。既然能说了。不过小心点，听起来她吸了不少那东西进肺里。"
            j "我也这么觉得。"
            scene c002_s001_009 with Dissolve(0.25)
            j "劳拉？是我。你在里面还好吗？"
            l "{size=30}*喘气* 你可以进来了，[player_name]。求你了。因为我觉得隔着门喊对我一点用都没有。{/size}"
            scene blank with Dissolve(2)
            scene c002_s001_018 with Dissolve(2)
            j "嘿，劳拉。哦，呃……"
            l "我不得不把衬衫脱了。它钻进去之后快把我逼疯了。我只想把皮肤搓干净，让这种刺激感消失。"
            j "好好好。明白。"
            scene c002_s001_017 with Dissolve(0.5)
        "你亲自扶她进去。\n[rgr](劳拉 好感/欲望 +1)":
            $ l_friend += 1
            scene c002_s001_004 with Dissolve(0.25)
            j "来，我扶你。抓住我的手。"
            l "*咳嗽* 谢了 *咳嗽* *咳嗽*" with vpunch
            "她要是糟成这样，在外面肯定待了很久。等她把咳嗽压下去之前，我们没法跟她好好说话。我不记得劳拉以前有呼吸方面的问题，但这次把她呛出哮喘来了。"
            scene blank with Dissolve(2)
            scene c002_s001_010 with Dissolve(2)
            j "好，来。"
            l "恐怕得靠你帮忙 *咳嗽* 眼睛很难看清。" with vpunch
            scene c002_s001_011 with Dissolve(0.25)
            j "好。不过别嚷嚷我在洗手间里。卡莉，你能给她拿瓶水吗？希望这样能冲掉她嘴里和喉咙里的东西。我抽屉里还有些零钱。奥蒂斯那边也有，需要的话可以拿更多。"
            k "好、好吧。我马上回来。"
            "也许这能帮到劳拉。也许不能。不过至少给了卡莉一件能专注的事，在我把劳拉安顿好之前，她也有点事做。要是她能暂时别一直死盯手机就更好了。看起来那样不太健康。"
            scene blank with Dissolve(2)
            scene c002_s001_012 with Dissolve(2)
            j "好，给你。水槽就在这儿。我先放水。相信我，把这玩意儿从脸上和露出的皮肤上洗掉会有帮助。头发里也可以溅一点。不知道会沾进去多少，但总比不洗好。"
            l "*咳嗽* *咳嗽* *咳嗽*" with vpunch
            scene c002_s001_013 with Dissolve(0.25)
            "你就退后一步，让她做她需要做的事。她主要是呼吸困难。不过我想她的视力可能也受影响。我倒没想过这东西要是长时间进到眼睛里会怎么样。"
            scene c002_s001_014 with Dissolve(0.25)
            l "哦，操，这样好多了。"
            j "听你这么说真好。"
            scene c002_s001_015 with Dissolve(0.25)
            l "*呻吟* 天哪，到处都在痒。胳膊上。衬衫里面。肯定有一部分钻进去了。"
            j "对，所以我每次出去都得把自己裹严实。所以，什——"
            scene c002_s001_016 with Dissolve(0.25)
            $ l_desire += 1
            l "得把这东西洗掉。不洗我会被折磨疯。"
            j "哇。呃……"
            scene c002_s001_017 with Dissolve(0.25)
        "[gr]Mod: 在卡莉的帮忙下扶她过去。\n[rgr](劳拉 好感\欲望 +1)\n[rgr](卡莉 信任 +1)":
            $ l_friend += 1
            $ k_trust += 1
            scene c002_s001_004 with Dissolve(0.25)
            j "来,我扶你。把手给我。"
            j "卡莉,能帮我扶她去洗手间吗?"
            k "呃,哦,好。可以的。劳拉,来,把手给我……"
            l "*咳嗽* 谢了 *咳嗽* *咳嗽*" with vpunch
            "她要是病成这样,估计在外面已经待了一阵子。等她缓过来之前,我们没法跟她谈。我不记得劳拉以前有呼吸方面的问题,但这阵子把她呛得像哮喘了一样。"
            scene blank with Dissolve(2)
            scene c002_s001_010 with Dissolve(2)
            j "好了,给你。"
            l "我眼睛看不清,*咳嗽* 得靠你帮忙了 *咳嗽*。" with vpunch
            scene c002_s001_011 with Dissolve(0.25)
            j "行。但别因为我在洗手间里就大惊小怪。卡莉,能帮她拿瓶水吗?希望能把嘴和喉咙里那些东西冲掉。我办公桌里还有些零钱,奥蒂斯那儿也有,不够的话再去拿。"
            k "好、好的。没问题,我马上回来。"
            "也许对劳拉有点用,也许没用。但至少能让卡莉有个事做,等我把劳拉安顿好之前她也有个着落。她该别再一门心思盯着手机了,那样不健康。"
            scene blank with Dissolve(2)
            scene c002_s001_012 with Dissolve(2)
            j "好了,给你。水池就在这儿,我来放水。信我一次,把脸上和露出来的皮肤上这些脏东西洗掉会有用。头发上也可以冲一点。不知道会沾进去多少,但总归没坏处。"
            l "*咳嗽* *咳嗽* *咳嗽*" with vpunch
            scene c002_s001_013 with Dissolve(0.25)
            "往后退一点,让她自己处理。她主要就是呼吸困难。不过我想她的视力也可能受了影响。我倒没想过,那些脏东西要是长时间进了眼睛会怎么样。"
            scene c002_s001_014 with Dissolve(0.25)
            l "哦,操,好多了。"
            j "那就好。"
            scene c002_s001_015 with Dissolve(0.25)
            l "*呻吟* 天啊,浑身都痒。手臂上,衣服里面都有。我觉得钻进去了。"
            j "是啊,所以我每次出去都得尽快收工。话说回来——"
            scene c002_s001_016 with Dissolve(0.25)
            $ l_desire += 1
            l "得把这些洗掉,不然我非疯了不可。"
            j "哇。呃……"
            scene c002_s001_017 with Dissolve(0.25)
    "这跟我预想的不是一回事，不过那种刺激大概真能让人做出平时不会做的事。我应该……"
    menu:
        "转过身去。":
            $ ch2_l_lookaway = "yes"
            "假装在这儿给她一点隐私，老兄。转过身。又不是要盯着她的胸看个够，但还是有点绅士风度吧。"
        "别提这事。\n[rgr](劳拉 欲望 +1)":
            $ l_desire += 1
            "就当这不是什么大事。也许可以问问她遇到了什么，让她别一直想着疼痛。"
    if ch2_l_lookaway == "yes":
        scene c002_s001_019 with Dissolve(0.25)
    else:
        scene c002_s001_020 with Dissolve(0.25)
    j "那么，呃……发生什么了？我敢说你肯定有个精彩故事。我知道我们的是，但我觉得你的更好。"
    l "你先说。我先……*咳嗽* 试着把这东西洗掉，免得说太久。"
    if ch2_l_lookaway == "yes":
        scene c002_s001_022 with Dissolve(0.25)
    else:
        scene c002_s001_021 with Dissolve(0.25)
    j "好好好。两天前，卡莉和我就在办公室里——天哪，已经两天了吗？——当时她走到前面想给她未婚夫打电话，我听见她叫了一声。我冲过去看到那一片雾。我们的座机、网络和手机信号全没了，于是我出去到车那边，结果发现——"
    l "它死了？"
    j "你的也是？"
    l "对。"
    if ch2_l_lookaway == "yes":
        scene c002_s001_023 with Dissolve(0.25)
    else:
        scene c002_s001_024 with Dissolve(0.25)
    j "所以从那以后，我们就一直躲在这儿。昨天我试着把车打着，没成功。不过我倒是溜进了附近的店里，发现他们也……"
    l "*喘气* 我被困在里面了。我当时离开了哈伯路上的和谐酿酒厂，正要去高中那边下一个点。我打算今天下班前去趟办公室。上车的时候我注意到烟很重，还以为附近着火了。"
    if ch2_l_lookaway == "yes":
        scene c002_s001_026 with Dissolve(0.25)
    else:
        scene c002_s001_025 with Dissolve(0.25)
    l "我给基思打电话想问问情况，但打不通。我正开着车，那东西就猛地扑过来了。外面浓得像汤。简直像有人打开了开关一样涌进来。我把车停到路边，因为我什么都看不见。"
    l "然后我的车熄了。就那么不跑了。不知道是什么弄的。这种事我一向都交给我老公处理。"
    j "可以理解。换成我？我是花钱请人弄的。"
    scene c002_s001_027 with Dissolve(0.25)
    l "总之，我被困在这条路往前几个街区的地方，车停在路边，什么都看不见，只看得见烟。我下车待了一会儿，那东西开始烧得厉害，我就赶紧钻回车里。算我走运，扶手箱里还有几张湿巾。"
    j "你最后是在车里睡的吗？我猜这问题挺蠢的。反正附近也没有旅馆。"
    scene c002_s001_028 with Dissolve(0.25)
    l "对。一点都不好玩。第二晚过后，我知道自己在里面待不下去了。没暖气的话，晚上会变冷。何况我整整一整天都没看见另一个活人。"
    scene c002_s001_029 with Dissolve(0.25)
    l "好吧……我觉得我没事了。肺还是疼，也感觉像是有人拿砂纸在我脸上磨过，但我已经好到能正常感觉了。"
    j "我懂这种感觉。我第一次出去既没穿外套也没戴口罩。是个大错误。卡莉应该把你的水拿来了。零食我们也从贩卖机里狠狠补了一轮，所以算不上均衡的一餐，但眼下能凑合。"
    l "谢谢。我好久没吃东西了。幸好我车里至少还剩一瓶水。"
    scene blank with Dissolve(2)
    scene c002_s001_030 with Dissolve(2)
    k "劳拉，你……？"
    l "我死不了。谢谢。"
    j "劳拉刚才跟我说了，她一直困在车里，后来发现街上一个人都没有，就跑到这儿来了。"
    scene c002_s001_031 with Dissolve(0.25)
    k "哦？所以外面没人？"
    l "从和谐酿酒厂到这儿，一个人都没有。或者说，我没看到人。这一带往幽灵镇的方向恶化已经有一阵子了，但将近两天连一辆车、一个人影都看不到，还是很瘆人。"
    j "然后你就决定往公司来了？这……多远？两三个街区？半英里？"
    scene c002_s001_032 with Dissolve(0.25)
    l "那不是我的第一站，可南边那个仓库锁着门。我在外面待到十分钟的时候，已经难受得不行了，就朝我认识的第一个地方跑。我慌了。我承认。你在这儿我运气好，你要是不在，我可能得砸窗户了。"
    j "能理解。慌张这事。就算我装备齐全，有时候也挺有压力，你不会想在外面待太久。那玩意儿会从领口钻进去，很快就能把你逼疯。我尽量把外出时间压到很短的范围。听我在这说，跟我是什么专家似的。"
    scene c002_s001_033 with Dissolve(0.25)
    l "装备齐全？"
    j "对，我凑出了一件外套、一顶棒球帽、手套、口罩和护目镜，好歹能扛住。这不是什么高级时装，但够用了。我本来打算去停车场那边的服装店，看看能不能给卡莉弄点东西。"
    scene c002_s001_034 with Dissolve(0.25)
    k "还有{i}汉堡店{/i}。"
    j "那个也是。我想看看能不能进去。也许能给咱俩弄点吃的。你出现之前我正准备出发呢。"
    scene c002_s001_035 with Dissolve(0.25)
    l "等、等一下。你是想弄点东西好让卡莉能出去？她为什么不能直接用你的……哦~~~"
    j "是啊，劳拉。之后我们可能得一起去某些地方。到处找找。眼下看来不会有人来。或者不会很快来。除了昨天那声枪响和你走过来，从这事开始我们就没听到或看到过任何人。"
    scene c002_s001_036 with Dissolve(0.25)
    l "那个我也听到了。但是……现在还早。给他们一点机会吧。要是他们的车也像我一样出了毛病，可能得等几天。你也见过被飓风和龙卷风袭击的地方，和外界断联一两天。"
    k "已经“一天或者两天”了。"
    j "而且这可不是你平时会遇到的那种事。"
    scene c002_s001_037 with Dissolve(0.25)
    l "*叹气* 我知道。我知道。如果……如果你觉得那边有那个东西会帮上忙，我想……那行吧……"
    j "我可以试着给你弄一套比你现在这身更扛得住的。"
    l "如果你能弄到、而且反正也要出门的话，我会很感激。不过现在我只想好好伸个懒腰。也许能睡在不是汽车座椅的东西上。"
    scene c002_s001_038 with Dissolve(0.25)
    j "后面有几张沙发和长凳。先休息吧。让我来照顾你。卡莉？"
    k "你走的时候我照看着她。"
    j "好。我去换衣服，看看能走多远。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c002_s002_017 with Dissolve(2)
    play music outsideday fadein 2.0
    "劳拉居然就在附近还自己走了过来，这太离谱了。这让我觉得我们不是唯一被困在外面的人，也让我觉得外面的援助（我猜）如果救援正在进行，是能赶到我们这儿的。"
    "不过劳拉到的时候样子确实很惨。呼吸困难——就算戴着口罩也是——皮肤被刺激得又红又糙。我看得出那东西正在“钻进她皮肤里”，让她有点抓狂。我想如果我感觉所有神经都在着火，大概也会那样。"
    scene c002_s002_018 with Dissolve(0.5)
    "她的出现会改变我们的处境吗？我们原本是打算在这儿耗着，指望政府会采取某种应对措施。而且才第三天左右。现在我们最大的问题是没有生活舒适品，也没有更好的食物选择。"
    "我想我还是该按原计划去做，哪怕劳拉看起来不太赞成。谁知道情况会不会急转直下，我们到时候好有应对的准备。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c002_s002_005 with Dissolve(2)
    play music officemain fadein 2.0
    k "我得说，能看到另一个人我真的很高兴。我知道你也困在这儿很难受，但要说谁会这样直接走过来，我庆幸是你。"
    l "我理解。我一直希望有人能在这儿。如果我是个下注的人，我大概会押[player_name]会留下来。而且我确实想过，他要是看出什么不对，可能会让你提前回家。"
    scene c002_s002_006 with Dissolve(0.25)
    k "它打过来的时候，我们还没意识到已经太晚了，什么都做不了。而我现在没车。或者说，没一辆能开的车。"
    l "是啊。情况恶化得相当快。我当时以为只是风往这个方向转了。"
    scene c002_s002_007 with Dissolve(0.25)
    l "那么，和[player_name]一起困在这儿，你还好吗？听起来你好像挺高兴{i}还有别人{/i}在。"
    k "不不，不是那种意思。不是那个意思。[player_name]人很好。要说被困在办公室里一起的人，我可选比他更糟的多了。"
    l "比如奥蒂斯？"
    scene c002_s002_008 with Dissolve(0.25)
    k "呃。他还行吧。"
    l "大概吧。要是能跟他共事又不介意他，那就行了。我和他一直不太对路。"
    scene c002_s002_009 with Dissolve(1)
    l "*呻吟* 天哪，我真是弱爆了。好累。过去两天没怎么睡，在那种烟里走路也好不到哪儿去。或者说，我觉得没好。即便戴着口罩，我的肺感觉像是抽了一整包万宝路。接下来得悠着点。"
    k "你该这样。这里也没多少事可做。除了等。不过我们倒是有几张沙发可以躺。要是想休息的话。还想吃点别的吗？"
    l "我做梦都想来块牛排，不过早餐棒也行。还有，是我多心，还是屋里有点闷？"
    scene c002_s002_010 with Dissolve(0.25)
    k "我们不得不把空调关掉。它在把外面的东西吸进来。就算我自第一天以后就没出去过，它也还是让我咳。"
    l "哦哦哦~~~对、对，这样说得通。*叹气* 还好外面是阴天，不然我们可就真麻烦了。我知道这些办公室夏天会热得够呛。米奇以前老是抱怨这个。"
    scene c002_s002_011 with Dissolve(0.25)
    l "米奇真走运。他大概正在家里躲着这一切。罗杰也是。查尔斯也是。那奥蒂斯呢？"
    k "他请病假了。"
    l "嗯……那安德鲁呢？你大概也没他的消息吧？"
    scene c002_s002_012 with Dissolve(0.25)
    k "自从电话信号断了以后就没有了。而且他在医院那边，我总不能走过去看他。"
    l "对。我老公也是。最好的情况是他在家，那也是一个小时车程。"
    scene c002_s002_013 with Dissolve(0.25)
    k "最坏的情况呢？"
    l "也许在他办公室。如果我运气好的话。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c002_s002_001 with Dissolve(2)
    play music outsideday fadein 2.0
    j "有人吗？有人吗？这里是你们亲切的邻里……购物者。我没带武器，我带着诚意来的。"
    scene c002_s002_002 with Dissolve(0.5)
    "绝对不是那种从正门走进来的打劫者。没错，我知道自己就是来顺东西的，前提是这儿没人。我想我是这么预设的。这一带我其实没碰上过几个人，这也不怎么意外。"
    "在一个慢慢死去的镇子里，我们就是那条需要被截肢的坏死的肢体。给他六个月，这些店可能全都要关门。"
    scene c002_s002_003 with Dissolve(0.5)
    "至于带武器？我没想过这个，但如果情况不改善、我们被迫要撑更久，我可能会希望自己手上有点什么。也许我该留心看看有什么能用的。眼下？先看看这店里有什么吧。"
    "所以现在我要“买”的东西不止一份。也就是偷。老兄，机灵点，挑实用的。你现在这样子连衣服都穿不利索，别指望在这儿能翻到什么给劳拉和卡莉穿的衣服。两件长袖外套或大衣。帽子。墨镜要是能找到的话。"
    scene blank with Dissolve(2)
    scene c002_s002_004 with Dissolve(2)
    "好，这趟比我预想的顺利。运气不错，他们有背包。还有几样东西能让她们在外面待更久一些。"
    j "抱歉拿你们这些东西。要是你们的监控还在录的话。要是在录，我往公路那边跑了。让警察来抓我们吧。求你们了。"
    "事到如今，只要能离开这鬼地方，被抓住塞进警车后座我都没意见。现在，看看我能不能搞定{i}汉堡店{/i}。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c002_s002_014 with Dissolve(2)
    play music officemain fadein 2.0
    k "嗯嗯…… *呻吟*"
    l "你还好吗？"
    scene c002_s002_015 with Dissolve(0.25)
    k "脸很痒。我觉得我的化妆品跟……跟那玩意儿不太对付。前几天我往脸上抹了一点后来洗掉了，但重新涂上口红和腮红之后，就……就是很痒。"
    l "我有一阵子没化妆了。抱歉。不过我能理解。要是哪东西刺激了你的皮肤，再往上涂什么都可能让你变得很敏感。比如润肤霜。或者洁面乳。而且女人的护肤品里总是塞满了各种你意想不到的东西，除非你去看标签。"
    scene c002_s002_016 with Dissolve(0.25)
    k "嗯哼。我想我爱臭美的日子要到头了。至少眼下是。而且我还以为穿这一身好几天的日子已经是地狱了。"
    l "也许我们运气好，救援很快就来。我只知道我得洗个澡。很快。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c002_s002_019 with Dissolve(2)
    play music menumain fadein 2.0
    "后面的停车场有一辆车，这让我琢磨是不是有人在。说真的，要是这附近还有别人像我们一样被困着，这地方应该会排在他们要来的地方的前列。尤其是一旦吃的开始成问题。"
    play sound doorclose
    scene c002_s002_020 with Dissolve(0.5)
    "门是锁着的，但没关严。很奇怪。像是有人想打烊离开、结果太匆忙了。我只要用肩膀狠狠撞一下门框，它就松开了。"
    scene c002_s002_021 with Dissolve(0.25)
    "这地方看起来不差。我本来还担心已经被洗劫过了。"
    "闻起来……不太对。也可能只是我不习惯它不开门营业的样子。我溜到后面看看。"
    scene blank with Dissolve(2)
    scene c002_s002_022 with Dissolve(2)
    "好，冷藏库看起来是满的。他们有面包，饮料机也在运转。软冰淇淋机坏了，不过我记得它好像一直都用不了。我不是操作这些设备的专家，但真有必要的话我能琢磨明白。"
    "所以，也许可以做些汉堡和薯条带走。后厨那边有些东西放在保温灯下，但不知道放了多久。没必要吃坏东西吃出胃病。"
    scene c002_s002_023 with Dissolve(0.5)
    "不过，这地方还有别的地方让我觉得不对劲。像是，有什么东西烂了。"
    scene c002_s002_024 with Dissolve(0.25)
    "是从这边飘过来的。也许是下水道返上来的。要这只是最糟的，我们就还能活。就这地方现在的状况来看，就像有人看到外面那雾，觉得时薪不值得，于是赶在关门前把门锁上了。"
    scene c002_s002_025 with Dissolve(0.25)
    "我不怪他们。要是我知道发生了什么，我会跟卡莉说……好吧，我本来会主动提出送她回家。我都忘了她的车也废了。"
    scene blank with Dissolve(2)
    scene c002_s002_026 with Dissolve(2)
    "好，男厕所很恶心，不过也就那样。啧，我们在这厕所里真是一群脏兮兮的男人。现在……"
    play sound doorclose
    scene c002_s002_027 with Dissolve(0.5)
    "靠。窗户开着，一些雾已经飘进来了。而且，那是……"
    scene c002_s002_028 with Dissolve(0.25)
    "操。地上就躺着一具尸体。他怎么了？"
    "地上有血。看起来像是摔倒了。也许撞到了头？很难说。看不出是被枪打还是被捅的。不管怎样还是死了。他一个人在这儿，没能出去。这种死法挺凄凉的。"
    scene c002_s002_029 with Dissolve(0.25)
    "这里的空气相当糟糕。我得把门关着，别让雾渗进店里其他地方太多。最好出去，回姑娘们那边，给她们通报一下。"
    "我要告诉她们这里有具尸体吗？如果我们决定把这儿当餐厅用，我可能别无选择。我不能擅自做这个决定。得先跟劳拉和卡莉商量，看看她们怎么想。"
    scene c002_s002_031 with Dissolve(0.25)
    "我看看能不能把这扇窗户关上。这个洗手间已经没救了，但我不想连带着把整家店也搭进去。"
    scene c002_s002_030 with Dissolve(0.25)
    j "*呻吟* 操！" with vpunch
    "这玩意儿是直接画上去的吗？我听说过有人把窗框刷死，但没见过这么干的。"
    scene c002_s002_031 with Dissolve(0.25)
    "而且他妈的够不着。我可不想变成地上那位那样，逞英雄结果摔下去磕得脑袋开瓢死掉。"
    "靠。回去吧。我在外面已经开始有点扛不住了。这么跑来跑去他妈的真累。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c002_s003_001 with Dissolve(2)
    play music insideday fadein 2.0
    l "所以，他平时会出去这么久吗？我知道之前我对这个想法不太以为然，但我现在开始有点担心了。"
    k "没那么久。不过他确实说要先去那家服装店，然后试试{i}汉堡店{/i}。正常情况下这两家都不是走着能到的。"
    scene c002_s003_002 with Dissolve(0.25)
    l "唔……"
    j "我回来啦~~~"
    scene c002_s003_003 with Dissolve(0.25)
    l "谢天谢地。"
    scene c002_s003_004 with Dissolve(0.5)
    l "怎么样……你背了个包。"
    j "对，我拿了它，还有几样你们俩出去时能用的东西。"
    scene c002_s003_005 with Dissolve(0.25)
    l "你就这么拿走了？这才开始……大概三天吧。"
    j "现在开始一点点顺东西还不算早。而且我已经对着监控道歉了，他们可以派警察来抓我。所以，要是警察来了，你可得感谢我。"
    scene c002_s003_006 with Dissolve(0.25)
    k "你找到了什么？"
    j "外套。帽子。墨镜。几个口罩。我们这儿有手套，所以我觉得东西基本够了。我把这些拆开你们看看。没有一件是时髦的。我去那儿可不是为了换衣服，不过如果我们在这儿待得太久，也许可以再去一趟。"
    scene c002_s003_007 with Dissolve(0.25)
    k "还有汉堡店呢？"
    "我大概该小心处理这件事。要提那具尸体吗？要不要说实话？感觉这会让我们的处境显得更严重。如果有人死了，这就意味着这一切正变得越来越凶险。"
    menu:
        "[gr]说出来。\n[rrd](卡莉\劳拉 焦虑 +1)\n[rgr](卡莉\劳拉 信任 +1)":
            $ ch2_tell_deadbody = "yes"
            $ l_anxiety +=1
            $ k_anxiety +=1
            $ l_trust +=1
            $ k_trust +=1
            j "我确实到了。他们有吃的，有些放在保温灯下，但我还是按食品安全优先处理了。如果明天我们还在这儿，也许我可以回去试试弄清楚怎么用那些设备弄点吃的出来。"
            scene c002_s003_009 with Dissolve(0.25)
            k "哦，那太好了，因为我实在不知道早餐棒还能撑多久。"
            j "不过我先提醒你一件事。那儿……那儿的女洗手间里有个人。"
            scene c002_s003_010 with Dissolve(0.25)
            l "什么？你看见尸体了？"
            k "哦。哦，靠。"
            scene c002_s003_011 with Dissolve(0.25)
            j "据我判断，他们应该是想给店打烊。也许是个值班经理。我走进洗手间，发现有一扇窗户开着。整个房间里到处都是雾。也许他想关门的时候摔倒了。我不知道。我又不是医生。"
            scene c002_s003_012 with Dissolve(0.25)
            "卡莉被这件事吓到了一点，但我还是觉得对她坦白比较好。这确实让很多事情有了更清晰的重量。生死之类的。"
            l "死了。靠。那……好吧……"
            "连劳拉都被这件事弄得有点措手不及。反正我们在这儿也没什么别的娱乐可做，这事够她们俩想一阵子了。"
        "[rd]不要。\n[rrd](卡莉\劳拉 焦虑 +1)\n[rrd](卡莉\劳拉 信任 -1) 稍后":
            j "情况没那么糟。他们有吃的，有些放在保温灯下，但我还是按食品安全优先处理了。如果明天我们还在这儿，也许我可以回去试试弄清楚怎么用那些设备弄点吃的出来。"
            scene c002_s003_008 with Dissolve(0.25)
            k "哦，那太好了，因为我实在不知道早餐棒还能撑多久。"
            l "不过要是能来点快餐，我倒是能被说服，最近我一直在努力吃得健康些。"
            "而且我注意到，你似乎在纠结我这种搜刮行为合不合法。"
            j "好吧，那我们就看看明早我们对此有什么感觉，嗯？"
            scene c002_s003_009 with Dissolve(0.25)
            k "我大概会更饿。"
    scene c002_s003_013 with Dissolve(0.25)
    j "好吧，我得脱掉这身装备了。已经开始像教堂里的婊子一样出汗了。我把这个包放下——你们俩什么时候想看都行。"
    scene c002_s003_014 with Dissolve(0.25)
    l "*咳嗽* *咳嗽*" with hpunch
    k "劳拉？"
    l "没事。只是……他进来的时候那烟。我估计有一部分困在他的衣服里了。"
    scene c002_s003_015 with Dissolve(0.25)
    k "也许我们得换个办法。你觉得我们出去的时候，你能一起来吗？"
    l "我想可以。{i}如果{/i}需要的话。眼下先看看[player_name]给我们顺来了什么好东西吧。"
    scene blank with Dissolve(2)
    scene c002_s003_016 with Dissolve(2)
    "好了，我现在感觉好多了。对，我凑出来的这身确实让我出去方便些，但还不算完美。皮肤上还是沾了些那玩意儿，它会从布料底下钻进去。出去的时间越长越明显，所以我可走不了长途。而且我那件外套也沾了味儿，也许我们把它和帽子拿出去晾一会儿。"
    scene blank with Dissolve(2)
    scene c002_s003_017 with Dissolve(2)
    j "哦，嘿。没料到你会等我。我挑回来的东西都还好吗？"
    k "我还没仔细看。至少还没有。我只是想告诉你劳拉不太好。而且我觉得雾困在你的衣服里了。你刚才进来的时候她开始呼吸困难。"
    scene c002_s003_018 with Dissolve(0.25)
    j "对，我就猜可能是这个。我把它挂在洗手间里，想让它透透气。暂时我会照看她。也许她得在这儿待一阵子。如果我们再出去的话。"
    k "我真不想把她留在这儿。"
    scene c002_s003_019 with Dissolve(0.25)
    j "我知道。我也怀疑她不会乐意那样。劳拉要是认准了某件事，会有点倔。"
    k "“有点”？*咯咯笑*"
    scene c002_s003_020 with Dissolve(0.25)
    "我该不该问问卡莉最近怎么样？我们一直忙着摸索周边、应付劳拉的到来，都忘了去关心她了。她肯定对自己跟社交圈断了联系有点感受。"
    menu:
        "别提。":
            "还是别提为好。要是她有别的事分心，就不会一直盯着她那位好不好。还有她家人。朋友。她生活里有很多人。而我？我认识的大概五个人里来了两个（算上前妻是三个）。"
        "[gr]说点什么。\n[rrd](卡莉 焦虑 +1)[rgr](卡莉 好感 +1)":
            $ k_anxiety += 1
            $ k_friend += 1
            scene c002_s003_021 with Dissolve(0.5)
            j "嘿，你……还好吗？我知道这段时间一点都不愉快，你可能还在为联系不上安德鲁之类的感到焦虑。"
            k "我……我在努力不去太想这件事。"
            scene c002_s003_022 with Dissolve(0.25)
            j "啊，好吧。抱歉。只是……只是想关心你一下。"
            k "没事。谢谢你问。还有……"
    scene c002_s003_023 with Dissolve(0.25)
    l "[player_name]？我得声明，你被禁止再给女人买衣服了。"
    j "实用压倒美观，劳拉。"
    scene c002_s003_024 with Dissolve(1)
    j "你看，也没那么难看吧。"
    l "看起来像我要去滑雪。而且这帽子对我的发型可没好处。我好几天没洗澡了，帽印头可不是我想营造的风格。"
    scene c002_s003_025 with Dissolve(0.25)
    j "好吧，那我下次出去会找个有淋浴的地方。*轻笑*"
    k "我也不知道。这也没那么糟。就是有点热，不过应该能凑合。大概吧。"
    scene c002_s003_026 with Dissolve(0.25)
    j "试试看吧。"
    "劳拉情绪不太好。我现在最好先给她点空间。这一切大概把她压得很紧。也许先让她冷静一阵，我再找机会跟她好好谈。"
    scene c002_s003_027 with Dissolve(0.25)
    k "你看，没那么糟吧。我觉得这应该比原来那件外套管用。"
    j "听你这么说挺好。要是明天还没人来救我们，也许就去试试{i}汉堡店{/i}。"
    k "好啊。"
    scene blank with Dissolve(2)
    scene c002_s003_028 with Dissolve(2)
    "有一阵子，卡莉和劳拉就在旁边闲聊些有的没的。我猜卡莉是认真地在履行“看护劳拉”的职责。考虑到劳拉还在咳嗽、整体疲惫，这很合理。既要困在车里，又要长时间待在外面才走到这儿，她的状态确实不好。"
    "听她说，她在外面待了不到一小时，中途在几个雾没那么浓的地方停下缓过气。但她的经历让我大致知道了，一个人能在外面待多久，暴露才会变成更严重的问题。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c002_s003_029 with Dissolve(2)
    play music nightmain2 fadein 2.0
    "天黑下来的时候，卡莉已经超出了她的社交配额，跑去自己沙发上待着了。没有电视也没有网络可以分散注意力，我想她大概很快就会试着睡下。这总比坐在那儿焦虑地想着联系不上安德鲁和家人要好。"
    scene c002_s003_030 with Dissolve(1)
    "至于劳拉，她已经撑不住睡过去了。我希望好好睡一晚，哪怕不是在床上，也能让她好过一些。"
    scene blank with Dissolve(2)
    scene c002_s003_031 with Dissolve(2)
    "至于我？我回到窗边，盯着外面的黑暗。时不时能看到远处一片彩色的光雾。大概是附近路口的交通灯。"
    "我坐在那儿，盘算着带一队人去{i}汉堡店{/i}的可行性。当然，只有我一个人的时候，我可以直接下决定，可以硬撑着一口气走到那儿。但如果要带上卡莉（也许还有劳拉），我就得从一个点到下一个点，让每个人都有时间缓过来。"
    scene c002_s003_032 with Dissolve(0.25)
    "而且如果劳拉真的去，就得认真考虑她的疲惫程度。"
    if ch2_tell_deadbody == "yes":
        "然后还有那具尸体。至少我已经提前告诉过她们了。我不想让她们到了那儿才发现。我不会意外，知道这件事会让在那儿吃饭有点别扭。我想饥饿会占上风。"
    else:
        "然后还有那具尸体。我得含混带过，尽量不让她们意识到女洗手间里正有个人在腐烂。因为我能想象，知道这件事会让在那儿吃饭有点别扭。我只能希望饥饿能占上风。"
    "另外，希望我们能搞定怎么用烤架。还有炸锅。我做梦都想吃薯条。卡莉说过她搬来之前做过餐饮，这倒是个好消息。"
    scene c002_s003_033 with Dissolve(0.5)
    l "嘿。你在这儿啊。"
    j "哦，嗨。在找我吗？"
    scene c002_s003_034 with Dissolve(0.25)
    l "不算，不过有人陪着挺好的。现在我们赖在这儿，这地方也没多大。我就是好奇你去哪儿了。我以为你睡了。"
    j "还没。我还没完全适应太阳一下山就没事可做。你呢？"
    scene c002_s003_035
    l "我想差不多。我一直有点夜猫子，所以太阳一落山就上床不太合我口味。我看到卡莉倒是睡了。"
    j "也许是一种应对方式。我感觉她是在努力不去想太多。救援没还很远的希望支撑着她。"
    scene c002_s003_036 with Dissolve(0.25)
    l "你觉得会吗？"
    menu:
        "不知道。[yl]":
            j "不知道。如果我务实一点说，我从没见过这种鬼事。但总得有人来吧。他们不能就这么把我们扔在这儿。"
        "最终会的。[yl]":
            j "最终会的。是啊，我们从没见过这种鬼事。但总得有人来吧。他们不能就这么把我们扔在这儿。"
    l "但愿吧。"
    scene c002_s003_037 with Dissolve(0.25)
    l "[player_name]，我想为刚才道歉。我态度很烂，你不该受那份气。我……困在车里对我的精神状态没好处。在烟里拼了命走到这儿更帮不上忙。那些东西沾在皮肤上、钻进衬衫底下，足够把我逼疯。"
    scene c002_s003_038 with Dissolve(0.25)
    l "然后又呼吸困难。我开始恐慌。我以为我可能会死。"
    j "算你运气好，我们在这儿。"
    scene c002_s003_039 with Dissolve(0.25)
    l "*叹气* 相信我，我知道。我想象不出还能去哪儿。"
    j "隔壁那家家具店还开着。说实话，我挺惊讶居然有这么多地方就那么大敞着对公众开放。好像员工们一个个都觉得那份最低工资不值得，直接走人了。"
    if ch2_tell_deadbody == "yes":
        j "到现在为止，我只在{i}汉堡店{/i}看到过有人。"
        scene c002_s003_040 with Dissolve(0.25)
        l "而这可不算是好消息。毕竟是死了。它引出一大堆我不确定自己想不想知道的问题。"
        j "我知道。但如果我们要在这儿困上一阵子，也许就必须面对。或者等救援来了，我们得告诉他们附近还有别人。为了让他们的家人知道。"
        scene c002_s003_041 with Dissolve(0.25)
        l "是啊……"
    else:
        scene c002_s003_041 with Dissolve(0.25)
        l "我完全能理解。"
    scene c002_s003_042 with Dissolve(0.5)
    l "还有，谢谢你的外套和帽子。比只穿着衬衫出去强多了。我懂。我真的懂。我不会忘记那种感觉在皮肤上的触感。就像有人往上撒了碱。"
    j "是啊，我懂。那种程度足以把人逼疯到把衬衫脱掉、像洗命一样搓自己的皮。"
    scene c002_s003_043 with Dissolve(0.25)
    l "是啊，我想确实会。*咯咯笑* 大概不是你希望看到的，对吧？"
    if ch2_l_lookaway == "yes":
        j "我根本没看。说真的。我转过身去了，好歹给你留点隐私的错觉。"
        scene c002_s003_044 with Dissolve(0.25)
        l "我注意到了。"
    else:
        menu:
            "今天的高光时刻。\n[rgr](劳拉 好感 +1)":
                $ l_friend +=1
                j "我不介意。真的是今天的高光时刻。"
                scene c002_s003_044 with Dissolve(0.25)
                l "*咯咯笑* 谢谢。大概吧。"
            "我基本没在看。":
                j "我基本没在看。我当时更专注于从你那儿听点最新情况。"
                scene c002_s003_044 with Dissolve(0.25)
                l "嗯哼。"
    scene c002_s003_045 with Dissolve(0.5)
    j "你今晚能睡得了吗？"
    l "比汽车座椅强，所以能。"
    j "我是说，一个人睡。不是和你丈夫躺在同一张大床上。"
    scene c002_s003_046 with Dissolve(0.25)
    l "是啊……*叹气*"
    j "抱歉。我不该说那种话。你知道他没事的，对吧？你知道我想象不出他会蠢到冲进那种酸雾里，去一个可能根本没人的办公室。"
    scene c002_s003_047 with Dissolve(0.25)
    l "*咯咯笑* 你这个混蛋。不，基思没事的。我敢肯定。我敢说他已经和身边的人一起把自己关得严严实实了。"
    scene c002_s003_048 with Dissolve(0.25)
    l "不过我也不是不习惯一个人睡。我们这些年的作息很不一样，能同时睡在同一张床上的时候很少。有些晚上他直接在客厅倒下，有些晚上我在我楼上的办公室沙发上睡着。"
    j "听起来就是两个都很忙、生活几乎没有交集的人。没有评判的意思。"
    scene c002_s003_049 with Dissolve(0.25)
    l "你说得也没错。彼得上大学之后，我们就没必要一起吃晚饭或者办家庭活动了。就是两个很忙的大人各忙各的。"
    scene c002_s003_050 with Dissolve(1)
    "说完这些，我们就安静了下来。我好像从来没想过劳拉的家庭生活并不是那么千篇一律。对一个总在外面跑的人来说，这很合理。她的日程不允许她五点到家、六点上桌吃饭。"
    "没多久，劳拉就开始犯困。我推了推她，让她先去睡。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_20_701", transition=Dissolve(1.0))()
    pause
    $ Hide("june_20_701", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c002_s004_001 with Dissolve(2)
    play music insideday2 fadein 2.0
    j "嗯嗯~~~ *打哈欠*"
    scene c002_s004_002 with Dissolve(0.25)
    l "*咯咯笑* 看来某人没穿工作装。"
    j "哦，对。这里有点闷。抱歉。我去把裤子穿上，省得你看到我早上的小帐篷。"
    scene c002_s004_003 with Dissolve(0.25)
    l "又不是第一次一大早就看到男人的某些状况了。"
    j "状况，是吧。好像这有多糟似的。不过还是别告诉人事部。"
    play sound zipper
    scene c002_s004_004 with Dissolve(0.25)
    l "我觉得这属于情有可原的情况。只要别让卡莉看见。"
    j "她是个大姑娘了。她不会有事的。"
    "再说了，前几天她自己也是那样。"
    scene c002_s004_005 with Dissolve(0.5)
    k "早上好。你刚才说什么呢？"
    l "没什么。我就是在挤兑[player_name]。"
    scene c002_s004_006 with Dissolve(0.5)
    k "哦，好吧。"
    l "你今天决定不化妆了？"
    scene c002_s004_007 with Dissolve(0.25)
    k "*叹气* 我昨天说过，那东西开始刺激我的皮肤了。今天早上我实在做不到。"
    l "不，不，我理解。我的皮肤到现在还因为在外面待过而有点烧。我根本无法想象现在去涂粉底之类的东西。"
    menu:
        "反正你也不需要。\n[rgr](卡莉 好感 +1)":
            $ k_friend += 1
            j "反正你们俩都不需要。我是说化妆。"
            scene c002_s004_008 with Dissolve(0.25)
            l "这话我可要记进你的人事档案了。"
            j "随便。反正到头来他们要开除我也行。不过得当面来。"
        "保持沉默。":
            "现在大概别对外貌发表意见。就算在最好的时机也不会有人爱听，何况现在——我们好几个都没洗澡了。"
    scene c002_s004_009 with Dissolve(0.25)
    k "所以，我们今天还是出去吗？我知道现在还早，但我们已经聊了挺久了，而且我醒来就饿。说实话，我不知道那些格兰诺拉麦片棒还能吃多少根。"
    j "它们也没那么难吃，只是我吃过更差的。大学那会儿，我靠杯面和意大利面过活。还不放肉酱。就是面条加黄油加粉状帕玛森芝士。再加胡椒。那几年我是真穷。"
    scene c002_s004_010 with Dissolve(0.25)
    l "我觉得她说的是消化层面的。不是所有人都有铁打的胃。"
    j "哦？他们要把你刮干净？*轻笑*"
    k "……"
    scene c002_s004_011 with Dissolve(0.5)
    j "可以去，但我们得小心。裹严实。戴口罩。戴护目装备。我还带了些墨镜回来。路上大概得停一两个地方。我觉得从这儿一路硬撑过去，雾会成为问题。"
    k "我觉得不成问题。你觉得怎样最安全就怎样。劳拉？"
    l "我……好吧。"
    scene c002_s004_012 with Dissolve(0.25)
    j "你要是不想勉强，可以不去。"
    l "不不。我……我去。我不想一个人待在这儿。只是我觉得我走不了太远。我还没好利索。"
    scene c002_s004_013 with Dissolve(0.25)
    j "没关系。就像我说的，我们可以中途停。我已经想好了哪些点位最合适，能把我们在外面待的时间压到最短。给我们留点时间缓一缓。"
    l "好吧，那我去收拾一下，我们就出发。"
    scene c002_s004_014 with Dissolve(0.25)
    j "对，我也想去趟洗手间。再喝点东西。我们大概一小时后出发，行吗？"
    k "嗯哼。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c002_s004_015 with Dissolve(2)
    play music outsideday2 fadein 2.0
    "等大家都穿好装备——我得承认，那样子有点蠢，像我们要去爬雪山一样——我们就出发了。因为我之前已经踩过周边的点，她们让我走在前面。"
    scene c002_s004_016 with Dissolve(0.25)
    "和之前不一样，我这次注意不再乱走。考虑到劳拉最近暴露后的状况，也说不准卡莉能撑多久，我判断还是直接去第一个停靠点最好。"
    scene blank with Dissolve(2)
    scene c002_s004_017 with Dissolve(2)
    j "好了，到了。这应该是个不错的中途点。大家还好吗？"
    k "嗯哼。"
    l "我死不了。"
    scene c002_s004_018 with Dissolve(0.25)
    j "还喘不上气吗？"
    l "唉。可惜。虽然裹得严严实实，但我的皮肤好像已经开始又痒又烧了。"
    scene c002_s004_019 with Dissolve(0.25)
    j "我能理解你会有那种过于敏感的感觉。尤其你在外面待了那么久。你还能继续走吗？"
    l "让我缓一会儿就行，我撑得住。等到了最好有值得吃的东西。"
    scene c002_s004_020 with Dissolve(0.25)
    j "卡莉？"
    k "嗯？哦，抱歉。在看新出的平板。我本来打算买一台新的。只是不是现在。"
    j "等这一切结束，我一定犒劳自己。我知道我会。但不会买手机。要酒。还有能买到的最贵的牛排。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_20_823", transition=Dissolve(1.0))()
    pause
    $ Hide("june_20_823", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c002_s005_001 with Dissolve(2)
    l "*叹气* 谢天谢地到了。"
    j "是啊，我可不记得走这段路要这么久。"
    "大概因为一个人走更省事。当向导就意味着我不能把她们俩落在后面。"
    scene c002_s005_002 with Dissolve(0.25)
    k "我们现在能把这些全脱了吗？太沉了，我开始出汗了。"
    j "呃，可以。不过提醒一句，女洗手间有扇开着的窗户。"
    if ch2_tell_deadbody == "yes":
        l "以及其他一些事。"
        "对，现在别想那个了。"
    scene c002_s005_003 with Dissolve(0.25)
    j "所以，我对餐厅后厨这套不太熟。我想我们该回厨房里研究一下。"
    scene c002_s005_004 with Dissolve(0.25)
    k "我高中时干过。在一家小餐馆打工。主要是当服务员，但也看过厨师操作，知道该开什么关什么——如果他们设备差不多的话。我休息的时候可能还拿炸锅的油桶炸过一些不该炸的东西。"
    scene c002_s005_005 with Dissolve(0.25)
    j "好吧，那食物这块就归你负责了。我去冷库拿点东西，我们试着做点汉堡和薯条。劳拉？有什么偏好吗？"
    l "不用。随便吧。现在有吃的就不错了。谢谢。"
    scene c002_s005_006 with Dissolve(0.25)
    j "{size=32}我去拿些面包胚、肉饼，还有能找到的别的东西。{/size}"
    k "{size=32}好好好。我想我能搞定。另外，要是你在冷冻柜里看到一袋薯条……{/size}"
    scene c002_s005_007 with Dissolve(0.25)
    j "{size=32}哇。你看起来真像是知道自己在干什么。我提名你当今后的短单厨师。{/size}"
    l "{size=32}[player_name]！？[player_name]！？你能过来一下吗？{/size}"
    j "{size=32}哦，劳拉在叫你。这边你搞得定吗？听起来她需要人搭把手。{/size}"
    k "{size=32}能。现在能搞定了。谢谢。去看看她需要什么。{/size}"
    scene c002_s005_008 with Dissolve(0.5)
    j "需要帮忙就喊一声。劳拉？怎么了？没事吧？"
    if ch2_tell_deadbody == "yes":
        l "{size=32}我在女洗手间。你能过来一下吗？{/size}"
        scene c002_s005_009 with Dissolve(0.25)
        "操。看来她是好奇。我本来指望我们可以假装这里没有那只房间里的大象。"
        scene blank with Dissolve(1)
        scene c002_s005_010 with Dissolve(1)
        j "你是想确认我没在骗你？还是纯粹出于病态的好奇？"
        l "不不。我只是……想亲眼看看。味道这么大，很难不注意到。我不指望会好转。这东西在这儿待得越久，状况就越糟。"
        scene c002_s005_011 with Dissolve(0.25)
        j "我知道。如果救援来得太晚，我们也没什么办法。最多只能现在先把它关起来。幸好这里没有阳光照进来，把它变成火炉。"
        scene c002_s005_013 with Dissolve(0.25)
        k "{size=32}劳拉？各位？饭好了。大概好了。你们在哪儿？{/size}"
        j "在洗手间里。和尸体一起。就是去看看。你要是肠胃受不了就别进来。"
        scene c002_s005_014 with Dissolve(0.25)
        l "要进来也一定把口罩戴好。这里的空气很差。"
        j "我们真该走了。在这这儿没什么可做的。"
        play sound doorclose
        scene c002_s005_016 with Dissolve(0.25)
        k "那么，在哪儿……我……"
        l "你不必过来。"
        k "我……我想我还是宁愿知道。我……呃……我们知道是谁吗？又或者怎么死的？"
    else:
        l "{size=32}我在女洗手间。你能给我解释点什么吗？{/size}"
        scene c002_s005_009 with Dissolve(0.25)
        "操。看来劳拉想亲眼看看。我想这事躲不过去，尽管我本来指望我们可以假装这里没有那只房间里的大象。"
        scene blank with Dissolve(1)
        scene c002_s005_010 with Dissolve(1)
        $ l_anxiety +=1
        $ l_trust -=1
        j "我知道叫你别进来也不会管用。"
        l "我能闻到尸体的味道，[player_name]。你以为我们会闻不到？"
        scene c002_s005_011 with Dissolve(0.25)
        j "我本想把它说成是雾渗进了楼里。你也知道那味道有多难闻。说到这个，别太靠近窗户。"
        l "我知道。我是个成年人。但这事让我有点发毛，要是有个提前告知就好了。"
        j "而这正是我想避免的。不想让你和卡莉被吓到。我们所有人都在压力之下。我本来打算不让你们俩任何一个知道。"
        scene c002_s005_012 with Dissolve(0.25)
        l "结果搞砸了。"
        k "{size=32}劳拉？各位？饭好了。大概好了。你们在哪儿？{/size}"
        scene c002_s005_013 with Dissolve(0.25)
        j "等一下——"
        l "不，她应该看看这个。"
        j "你确定？"
        scene c002_s005_014 with Dissolve(0.25)
        l "确定。她得知道。我不是个天真小姑娘，你也别把她当瓷器。"
        j "我没有那个意思。"
        scene c002_s005_015 with Dissolve(0.25)
        l "不过瞒着她也没什么好处。卡莉？你能来一下女洗手间吗？记得戴上口罩。"
        k "{size=32}呃，好……{/size}"
        play sound doorclose
        scene c002_s005_016 with Dissolve(0.25)
        $ k_anxiety +=1
        $ k_trust -=1
        k "怎么了……哦……哦，靠。"
        l "对。这里有具尸体。就是我们发现的那具。"
        k "我……呃……我们知道是谁吗？又或者怎么死的？"
    scene c002_s005_017 with Dissolve(0.25)
    j "大概是值班经理或者持钥匙的人。最后走的一个，因为我猜他们当时正在打烊关门。看起来不像是有人对他们做了什么。也许是暴露过度要了他们的命。剧烈咳嗽，失去了平衡，摔下去，磕到了头。大概是这种。"
    scene c002_s005_018 with Dissolve(0.25)
    l "我也是这么想的。也许他们皮肤上沾了太多那玩意儿，起了不良反应。不管怎样，我们不该在这儿待太久了。开始影响到我了。"
    scene c002_s005_019 with Dissolve(0.25)
    k "好、好吧。有吃的。已经好了。在柜台上。你要是还饿的话。"
    j "谢谢。我们尽量让这顿饭吃得值一点。"
    play sound doorclose
    scene c002_s005_020 with Dissolve(0.25)
    "卡莉好像被这事弄得有点不安。可以理解。我现在也对这事没什么胃口。而且想着一具死人对提升食欲没多少帮助。它也让我们的处境比之前严重得多。起初我们只是在等救援。现在？有人死了，而且看不到任何人的影子。"
    scene blank with Dissolve(2)
    scene c002_s005_021 with Dissolve(2)
    "我一直觉得劳拉是用更结实的料造的。即便如此，她对这事也一言不发。等她消化完了，大概会有些话说。靠，我也会。"
    "我们坐着狼吞虎咽地吃掉了一大堆薯条和汉堡。必须得说卡莉备的份量足够，让每个人都能再来一份。虽然肉没什么可夸的，但卡莉用手头有的材料尽了力，考虑到当时的情况，我很感激她的努力。"
    scene blank with Dissolve(2)
    scene c002_s005_022 with Dissolve(2)
    "吃完之后，我们安静了一阵。又累，又还没从处境的严重性里缓过来，实在没什么轻松可言。"
    scene c002_s005_023 with Dissolve(0.5)
    k "我从没见过那样的尸体。以前见过一次。我爷爷的葬礼。但……不是那样。就那么躺在地上。"
    j "没多少人见过。除非他们的工作就是跟尸体打交道，比如警察或者殡葬业的人。"
    scene c002_s005_024 with Dissolve(0.25)
    l "我小时候撞见过我曾祖母。她在家里。在她的洗手间。她上厕所的时候心梗了。"
    scene c002_s005_025 with Dissolve(0.25)
    j "我自己也参加过几场葬礼。我前妻的母亲——我大概该叫前岳母——去世时，后事得我们操办。那阵子我被迫一下长大了很多。"
    scene c002_s005_026 with Dissolve(1)
    "虽然能吃上一顿饭挺好的，但对我们来说，那具尸体就在一道门外，这顿饭也就显得无关紧要了。"
    k "那么，那边是什么？看起来像一栋办公大楼。又一栋。我猜我们被这些楼包围了。"
    j "那边？普罗维登斯人寿。或者曾经是。"
    scene c002_s005_027 with Dissolve(0.5)
    l "*叹气* 他们大概六个月前关门了。那是一家处理保险咨询的呼叫中心。作为雇主，对这一带是巨大的损失。所以现在那边没人。听说是把所有岗位都转移到海外了。"
    j "这也解释了为什么停车场在过去一年里一直那么空。你能从空位数量看出他们一批一批地裁人。"
    k "好吧，比起我们，那栋楼离吃的更近。要是有人在的话。我不知道办公楼的另一侧有什么，但从这儿走过去也就一百英尺出头。"
    scene c002_s005_028 with Dissolve(0.25)
    l "你是说我们换个据点？至少往那边挪一挪？"
    k "我只是说说。而且我们办公室又不是什么旅店。"
    j "要是这一切来的时候我们能待在家就好了，对吧？"
    scene c002_s005_029 with Dissolve(0.25)
    l "有点。"
    j "而且等救援真的开进城，他们不会直接冲到环球办公用品来找我们。我想如果我们看到或者听到有人进来，得主动把他们拦下来。"
    l "你觉得他们会怎么出现？我不是想泼冷水。只是……"
    scene c002_s005_030 with Dissolve(0.25)
    j "如果是消防救援或者国民警卫队？全套装备，可能还有防毒面具。或者像电影里处理生物危害时穿的那种防护服。"
    l "他们的车呢？"
    scene c002_s005_031 with Dissolve(0.25)
    j "就算骑自行车进来我都认了。跳伞也行。滑翔机。事到如今我他妈什么都不在乎了。他们有号称能扛住攻击（包括毒气）的防弹车。我不明白我们政府怎么就没有一两辆。"
    l "好吧。也算。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_20_1135", transition=Dissolve(1.0))()
    pause
    $ Hide("june_20_1135", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c002_s006_001 with Dissolve(2)
    "没过多久，我们收拾干净，重新穿上“出行装备”，就出发了。那顿饭确实让人满足、也填了肚子，但那具死去的员工，我们谁也没法无视。"
    scene c002_s006_002 with Dissolve(0.25)
    "如果短时间内没人来把我们弄出去，我们就得再回来一次（或者在这附近另找个地方）。那具死者能怎么办？我总不能把他们搬走吧？在有人来处理遗体之前先破坏现场。"
    scene blank with Dissolve(1)
    scene c002_s006_003 with Dissolve(1)
    l "*呻吟*"
    k "我们离得不太远了。"
    scene c002_s006_004 with Dissolve(0.25)
    l "我知道。只是……我累了。感觉自己老了。"
    "不只是劳拉。我也被一种异常的疲惫折磨着。四肢像灌了铅一样，我们在外面待得越久，我的肌肉就越酸痛。"
    scene c002_s006_005 with Dissolve(0.5)
    j "唔……"
    "我以前没想过这个，但此刻我们往回走的时候，我开始怀疑这雾本身是不是就在消耗我们，好像我们正穿过某种比空气更稠的东西。又或者，这雾霾的毒性还有别的副作用。"
    scene c002_s006_006 with Dissolve(0.25)
    "嘿，等一下。刚才那是……"
    l "[player_name]？你没事吧？"
    scene c002_s006_007 with Dissolve(0.25)
    j "对，对。我只是想起……没什么。"
    "我们快到办公室了。最后加把劲进去吧。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c002_s007_001 with Dissolve(2)
    play music insideday2 fadein 2.0
    "回去之后，我们花了一些时间脱掉装备，把身上残留的雾洗掉。被这趟折腾得够呛，大家各自安顿下来歇了一阵。"
    scene blank with Dissolve(2)
    scene c002_s007_002 with Dissolve(2)
    "我想卡莉已经受够了社交，决定给她点空间。不过我知道在太晚之前我会想去看看她。哪怕只是看看她对洗手间那一眼适应得怎么样。"
    "不过劳拉可没收到这个通知。"
    scene c002_s007_003 with Dissolve(1)
    l "嘿，卡莉，你怎么样？"
    k "我、我没事。就是累。你呢？"
    scene c002_s007_004 with Dissolve(0.25)
    l "又累又垮。所幸咳嗽好些了。谢谢你今天做饭，真顶用。"
    k "是顶用。这么多天来第一顿正经饭。我以前以为自己能吃素，但一饿起来立刻就把它扔垃圾桶了。那个汉堡我吃得太过瘾了。足以说明我坚守原则的能力有多差。"
    scene c002_s007_005 with Dissolve(0.25)
    l "紧急时期就得做紧急的选择。希望这是你唯一要放弃的东西。"
    l "那么，你怎么样？关于……听着，我知道联系不上家人会让你很有压力。被困在这儿、什么都做不了，只会让情况更糟。我知道这对我来说也一样。我一直没收到彼得的消息，作为一个母亲，我努力不去想最坏的情况。"
    scene c002_s007_006 with Dissolve(0.25)
    k "他不会有事的。要是他像他妈妈的话。他大概……在哪儿来着？"
    scene c002_s007_007 with Dissolve(0.5)
    l "{a=https://www.uga.edu/}UGA{/a}。他在校园里有宿舍。"
    k "佐治亚？他应该没事吧。[player_name]好像觉得这可能只是我们这一带的事。是局部的。他说过这种事不可能全国同时发生，不然新闻早就会报道了。"
    scene c002_s007_008 with Dissolve(0.25)
    l "也许吧。不过我还是希望能收到他的消息。就为了确认一下。那安德鲁呢？"
    k "自从几天前他送我过来之后，就没有消息了。"
    scene c002_s007_009 with Dissolve(0.25)
    l "他在医院工作。他在那儿应该更安全，比这儿安全。而且他们有食堂。他大概吃得好。至少比我们好。"
    k "是啊。谢谢。我只能希望如此。还有你丈夫？"
    scene c002_s007_010 with Dissolve(0.25)
    l "基思是个大男孩。我相信不管他在哪儿都没事。说不定正在掌控局面。"
    k "你不知道他在哪儿？"
    scene c002_s007_011 with Dissolve(0.25)
    l "他跟我很像。他的工作让他到处跑，见很多人。所以我说不出他在哪儿。我只能相信他平安。靠，要是[player_name]是对的，他可能根本就在这一切之外。安安全全在家。或者在他在的某个地方。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_20_635", transition=Dissolve(1.0))()
    pause
    $ Hide("june_20_635", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c002_s008_001 with Dissolve(2)
    play music nightmain fadein 2.0
    "我勒个去。六小时？我比自己以为的累多了。我们回来没多久我就睡着了，等我醒来，太阳已经落山了。"
    "今天这趟——连带着发生的这一切——之后，我觉得该去看看其他人怎么样了。而且我得明白，待得越久，人的神经和情绪可能就越紧绷。她们俩都有拼命想联系上的家人。"
    "我该先去看谁？"
    menu:
        "卡莉\n[rgr](卡莉 好感 +1)\n[rgr](卡莉 焦虑 -1)":
            $ k_friend +=1
            $ k_anxiety -=1
            scene c002_s008_002 with Dissolve(1)
            j "嘿，你。正好赶在你睡下之前找到你。回来之后我睡了一小觉，所以你要是因为累了早睡我也理解。就好像光是待在外面就够累人了。或者，也许是我懒，该多走点路却没走。"
            k "我……我今晚大概会睡得很沉。好久没有觉得吃饱了。而且就像你说的，来回那段路比我习惯的要多。这要让我高中越野队教练知道了，非得气死不可。"
            scene c002_s008_003 with Dissolve(0.25)
            j "是啊……那你觉得怎么样？还好吗？我们在外面待了挺久，我知道你和劳拉之前都出现了呼吸困难。口罩管用吗？"
            k "管用，你弄来的这些确实有帮助。不过你不用这么操心我。操心你自己和劳拉就行。我挺好的。比劳拉之前好多了。"
            scene c002_s008_004 with Dissolve(0.5)
            j "也许我们这么做是因为在乎。而且劳拉有点母性情结。"
            j "再说了，我们都得互相看着点。你已经——亲身经历过——那玩意儿沾在皮肤上或者吸进肺里是什么滋味。我知道我们和外界断了联系，每个人都有点焦虑。"
            k "我、我知道。"
            scene c002_s008_005 with Dissolve(0.25)
            j "他们都很好。安德鲁。你的家人。只是联系不上，并不意味着他们出了什么事。我知道你需要听到这句话。而且这是真的。"
            scene c002_s008_006 with Dissolve(0.25)
            k "我知道。我只是……我{i}想{/i}知道。想跟安德鲁说说话。想跟我妈、我的兄弟姐妹说说话。"
            j "我理解。得到确认能让你脑子里那些最可怕的剧本安静下来。"
            k "是啊……"
            scene c002_s008_007 with Dissolve(0.25)
            k "我们明天还去吗？我只是问问，因为为了吃饭走那么远感觉有点夸张。而且我不确定劳拉从刚才的状态完全恢复了，能天天这么跑。"
            j "明天再说吧。到时候看状态。也许我自己回去一趟，给我们带点东西顶一顶。如果那样的话，可能得你先给我讲一遍那些设备怎么用。"
            scene c002_s008_008 with Dissolve(0.25)
            k "好好好。不是想冒犯，不过……"
            scene c002_s008_009 with Dissolve(0.25)
            j "该睡了呢，还是想一个人待会儿？"
            k "两个都要。谢谢。"
            scene c002_s008_010 with Dissolve(0.25)
            "说实话，卡莉能撑到现在已经很不错了。我尽量给她点空间。劳拉则相反，她需要更多的交流，而我也不知道卡莉能忍到什么程度不被磨掉。"
            "说到劳拉……"
            scene blank with Dissolve(1)
            scene c002_s008_011 with Dissolve(1)
            "好吧，她应该是睡过去了。最好让她睡。她可不像我睡了六个小时。明天早上我再跟她聊。"
        "劳拉\n[rgr](劳拉 好感 +1)\n[rgr](劳拉 焦虑 -1)":
            $ l_friend +=1
            $ l_anxiety -=1
            scene c002_s008_012 with Dissolve(1)
            j "嘿，你。有发生什么吗？"
            l "没有，一切平静。之前就稍微聊了点女人之间的话。你睡得怎么样？"
            scene c002_s008_013 with Dissolve(0.25)
            j "看来我比自己以为的更累。肚子饱了，又走了不少路。再加上那雾在外面对我们做的其他事。"
            scene c002_s008_014 with Dissolve(0.5)
            l "嗯？你什么意思？"
            j "我没法证明，但感觉在外面走路确实比平时吃力，好像我们在涉过某种比空气更稠的东西。"
            scene c002_s008_015 with Dissolve(0.25)
            l "唔……我倒没想过。有意思。"
            if ch2_tell_deadbody == "yes":
                j "我很讨厌你们俩看见那具尸体。这也是我当时提起它的原因。而且我真的不想让卡莉看到。"
            else:
                j "所以，我们真的有必要让她看尸体吗？"
            scene c002_s008_016 with Dissolve(0.25)
            l "她是个大姑娘。你不用把她护起来。"
            j "我们大家都在压力之下，劳拉。回不了家。没法联系家人朋友确认他们是否安全。她不需要更多。告诉她那里有具尸体，告诉她这些就够了。"
            scene c002_s008_017 with Dissolve(0.25)
            j "也许她正在想象安德鲁在别处也遇到类似情况。或者她的某个家人。"
            l "唔……你……我明白你的意思。现在你这么一说，我……是啊……"
            "有时候劳拉太专注于自己想做的事，就不会考虑到有些事需要小心处理。现在的局面已经够紧张了，我们没必要再让它更糟。"
            scene c002_s008_018 with Dissolve(0.5)
            j "那么，你现在怎么样？咳嗽和皮肤刺激呢。再出去一趟有没有加重？"
            l "没我担心的那么严重。尽管我之前对那外套和帽子抱怨了一堆，看起来确实起了作用，暴露少了不少。"
            j "那就好，那就好。你呢？看见那具尸体，感觉如何？"
            scene c002_s008_019 with Dissolve(0.25)
            l "不怎么样。这多少让我吃了这么久以来第一顿热乎饭的好心情打了折扣。而且这也没让情况变得更好，你懂吧？比如说，我们困在这儿，我们见到的唯一一个人是……死的。这让我对我们的前景没什么信心。"
            l "而且我很讨厌的是，如果我们需要回去拿吃的，那具尸体还会在那儿。"
            j "我们可以试着把他们挪走。"
            scene c002_s008_020 with Dissolve(0.25)
            l "然后破坏现场？我敢肯定这是违法的。"
            j "我再说一遍：让他们来抓我好了。"
            scene c002_s008_021 with Dissolve(0.25)
            l "话虽如此，做这种事还是让人发毛。"
            j "好吧。但如果这持续太久，我们可能得做一些平时不会做的选择。"
            scene c002_s008_022 with Dissolve(0.25)
            l "*叹气* 我知道。"
            scene c002_s008_023 with Dissolve(0.5)
            "过了一会儿，我看得出劳拉只是想休息。我跟她道了晚安，就去看卡莉了。"
            scene c002_s008_024 with Dissolve(1)
            "她已经睡着了。这很合理。我明天早上再跟她聊。"
        "[gr]Mod: 两个都来帮。\n[rgr](卡莉\劳拉 好感 +1)\n[rgr](卡莉\劳拉 焦虑 -1)":
            $ k_friend +=1
            $ l_friend +=1
            $ k_anxiety -=1
            $ l_anxiety -=1
            scene c002_s008_002 with Dissolve(1)
            j "嘿你。还好你还没打算睡。我回来的时候小睡了一会儿,所以能理解你为什么比平时更累。光是在外面待着就已经够累了。也可能是我偷懒,本该多走一会的却没走。"
            k "我……我今晚大概会睡得很沉。好久没有这么饱过了。而且就像你说的,来回那段路比我平时走的远多了。这要是让我高中越野跑的教练知道了,她非杀了我不可。"
            scene c002_s008_003 with Dissolve(0.25)
            j "是啊……那你现在怎么样?身体还好吗?我们在外面待了挺久,你和劳拉之前都有呼吸不畅的情况,口罩有用吗?"
            k "嗯,你弄来的那些好像确实有用。但你不用这么操心我,操心你和劳拉就行。我挺好的,比劳拉强多了。"
            scene c002_s008_004 with Dissolve(0.5)
            j "也许我们这么做是因为在意对方吧。再说,劳拉多少有点母性泛滥。"
            j "而且我们都得互相盯着点。你已经见过——亲身经历过——那些脏东西沾在皮肤上、吸进肺里是什么滋味了。我知道我们跟外面断了联系之后,每个人心里都有点慌。"
            k "我、我知道。"
            scene c002_s008_005 with Dissolve(0.25)
            j "他们都没事。安德鲁,你家人也是。我们跟他们断了联系,不等于他们那边就出了什么事。我知道你需要听到这句话,而且这是事实。"
            scene c002_s008_006 with Dissolve(0.25)
            k "我知道。我只是……我{i}想{/i}知道。想跟安德鲁说说话。想跟妈妈、跟我的兄弟姐妹说说话。"
            j "我明白。有个确切消息,能让你脑子里那些最坏的猜测少上几个。"
            k "嗯……"
            scene c002_s008_007 with Dissolve(0.25)
            k "我们明天还要回去吗?我只是问问,因为为了点吃的跑那么远感觉挺折腾的。而且我不确定劳拉已经从刚才的状态里缓过来,能天天这么跑。"
            j "明天的事明天再说,看我们状态怎么样。也许我自己回去拿点东西回来撑一阵子。要那样的话,我可能得让你跟我说一遍那些装备该怎么用。"
            scene c002_s008_008 with Dissolve(0.25)
            k "行,行。不是想冒犯你,但是……"
            scene c002_s008_009 with Dissolve(0.25)
            j "该睡了吗?还是想一个人待会儿?"
            k "都要。谢谢。"
            scene c002_s008_010 with Dissolve(0.25)
            "说实话,卡莉对现在的情况适应得挺好。我尽量给她留点空间。劳拉就不一样了,她需要多跟人待着。我不知道卡莉还能忍多久,忍到最后会不会受不了。"
            "说到劳拉……"
            scene blank with Dissolve(1)
            scene c002_s008_012 with Dissolve(1)
            j "嘿你。我错过什么了吗?"
            l "没有,没有。这边一切正常。刚才就两个女生聊了会儿。你睡得好吗?"
            scene c002_s008_013 with Dissolve(0.25)
            j "看来我比自己以为的更累。肚子里有东西,又走了不少路。再加上那雾在外面对我们做的别的什么。"
            scene c002_s008_014 with Dissolve(0.5)
            l "嗯?什么意思?"
            j "我没法证明,但就是感觉在外面走比平时费劲,像是在趟比空气更稠的东西。"
            scene c002_s008_015 with Dissolve(0.25)
            l "唔……没想过这点。有意思。"
            if ch2_tell_deadbody == "yes":
                j "我很讨厌你们俩看见那具尸体。我之所以说出来就是这个原因。而且我实在不想让卡莉看到。"
            else:
                j "所以,我们真的有必要让她看到尸体吗?"
            scene c002_s008_016 with Dissolve(0.25)
            l "她又不是小孩子。你不用什么都护着她。"
            j "我们大家现在压力都不小,劳拉。回不了家,也没法联系家人朋友确认他们是否平安。她不需要知道更多。只要告诉她那里有具尸体,就够了。"
            scene c002_s008_017 with Dissolve(0.25)
            j "也许她是在想安德鲁,或者她家里某个人,在别处也碰上了类似的事。"
            l "唔……你说得……我明白你的意思。现在你这么一说,我……也是……"
            "有时候劳拉一门心思只想着自己要做什么,没考虑到有些事得小心处理。现在这局面本来就够紧张了,我们没必要再给自己找麻烦。"
            scene c002_s008_018 with Dissolve(0.5)
            j "那你现在感觉怎么样?咳嗽和皮肤刺激都缓解了吗?再出去一趟有没有加重?"
            l "没我担心的那么严重。虽然我为了那件大衣和帽子抱怨了半天,但看起来确实挡住了不少。"
            j "那就好,那就好。你呢?看到那具尸体感觉怎么样?"
            scene c002_s008_019 with Dissolve(0.25)
            l "不太妙。让我这么久以来第一顿热乎饭都显得不是滋味。而且这也不会让情况变好,你懂吧?我们孤零零在这儿,唯一见到的活人……是死的。让我对我们的处境实在乐观不起来。"
            l "而且我很讨厌,万一我们得回去拿吃的,它们还就在那儿。"
            j "我们可以试着把它们挪开。"
            scene c002_s008_020 with Dissolve(0.25)
            l "还要破坏现场?那肯定是违法的吧。"
            j "我再说一遍:让他们来抓我啊。"
            scene c002_s008_021 with Dissolve(0.25)
            l "话虽如此,干这种事还是怪瘆人的。"
            j "好吧。但要是这样持续太久,我们可能得做些平时不会做的选择。"
            scene c002_s008_022 with Dissolve(0.25)
            l "*叹气* 我知道。"
            scene c002_s008_023 with Dissolve(0.5)
            "过了一会儿,我看得出来劳拉只是想休息。我跟她道了晚安,自己也去睡了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_21_737", transition=Dissolve(1.0))()
    pause
    $ Hide("june_21_737", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c002_s009_001 with Dissolve(2)
    play music insideday fadein 2.0
    j "嗯…… *呻吟*"
    "老兄，那张长凳第一两晚还行，现在开始真的硌死我了。我睡沙发的次数多到不愿承认，本以为自己早该习惯了。只希望我们不会在这儿待太久。"
    scene c002_s009_002 with Dissolve(0.25)
    "嗯？劳拉已经起来了。她确实一直给我的感觉是早起派。我好像闻到咖啡味了。她肯定在休息室。我去跟她聊聊。"
    "唉……今天早上我觉得有点被磨掉了。希望来点咖啡因就能解决。如果不行，也许昨天在外面待那么久真的有些副作用。现在下结论还太早，但这可能已经足够让我们重新考虑是不是该少跑几趟餐厅了。"
    scene c002_s009_003 with Dissolve(0.25)
    "我去看看卡莉和劳拉，看她们怎么样。听起来卡莉在走动。我猜我们都快成早起派了。"
    scene c002_s009_004 with Dissolve(0.5)
    "哦？哦，靠。我……我猜她在换衣服。也许她刚去洗手间洗漱完回来。或者她只是需要重新调整一下。又或者她睡觉时把胸罩脱了。无所谓。她还没看见我。我该走了。"
    menu:
        "悄悄走过去。":
            scene c002_s009_006 with Dissolve(0.25)
            "我们就悄悄过去，尽量别让这事儿让她尴尬。这附近没有隐私可言，可不是我们计划好的。"
        "早安。\n[rgr](卡莉 欲望 +1) [bl]信任点 ≥1 时,否则 [rrd](卡莉 焦虑 +1)":
            if k_trust >= 1:
                $ k_desire +=1
            else:
                $ k_anxiety +=1
            scene c002_s009_005 with Dissolve(0.25)
            j "早上好。"
            scene c002_s009_006 with Dissolve(0.25)
            k "嗯？哦。呃……早。"
    "是啊，除了一个洗手间和几间落地的玻璃办公室，我们也没多少换衣服的地方可选。现在已经有劳拉只穿胸罩，接下来又来这个。我怀疑我穿着内裤晃来晃去对她们来说没那么有意思。"
    scene c002_s009_007 with Dissolve(1)
    j "早啊，劳拉。咖啡已经煮上了？"
    l "嗯嗯~~~对。早上好。你睡得还行吗？"
    scene c002_s009_008 with Dissolve(0.25)
    j "大概吧。考虑到我现在困成这样，大概没睡好。你呢？"
    l "我累到一定睡得很沉。脖子还有点僵。"
    scene c002_s009_009 with Dissolve(0.5)
    l "所以我……我觉得我该问一句，不过你不想说也没关系。南希呢？我知道你一直没她的消息，可是……"
    j "她还在镇上。我不知道那男的名字，不过我最后听说是在文件办妥那阵子，她跟某个男人住在一起了。我有一部分有点担心，但我还是放不下，所以我想说，她现在是那个新男人的麻烦了。"
    scene c002_s009_010 with Dissolve(0.25)
    l "我能理解。人在感情上很难同时待在两个地方。你……我知道这事。米奇提过不止一次。可你从来没怎么说过，我也不想在上班的时候提起来。"
    j "我不想当那个在办公室抱怨自己婚姻、或者离婚的人。那种人相处起来可不愉快。也许要是我们在办公室之外多见几次，我可能会多说一些。"
    scene c002_s009_011 with Dissolve(0.25)
    l "等我们熬过去，我会找时间多跟你聊聊。"
    menu:
        "听起来不错。[yl]":
            j "听起来不错。我需要一点接近社交的生活了。"
        "你确定过了这事之后还想见我？[yl]":
            j "你确定过了这事之后还想见我？我们用这种方式共处，可算不上什么好消遣。"
    scene c002_s009_012 with Dissolve(0.5)
    l "我只是很遗憾你经历了那些。而且办公室里大概也没几个人真的在乎。"
    j "奥蒂斯对这事挺敏感，但他没有那种人生经验去理解是什么滋味。所以基本上就是尴尬地聊一小会儿，然后我们转去说别的。"
    scene c002_s009_013 with Dissolve(0.25)
    l "哦，[player_name]。"
    j "我不想多提，因为你总是很忙。而且很少待在楼里。"
    scene c002_s009_014
    l "你本来可以打个电话。或者把我拉到一边。"
    j "然后聊聊我的“感受”？*轻笑*"
    scene c002_s009_015 with Dissolve(0.25)
    l "对。或者你也可以说说你前妻的坏话。我不会因此看不起你。有时候人只是需要一个出口。"
    j "我不想当那种人。"
    scene c002_s009_016 with Dissolve(0.25)
    l "让人们做你的朋友吧，[player_name]。"
    scene c002_s009_017 with Dissolve(0.5)
    k "呃，早上好，劳拉。抱歉我……我只是……"
    j "咖啡？劳拉人真好，煮了一些。来，我让开点。"
    scene c002_s009_018 with Dissolve(0.25)
    "卡莉大概不是故意要打断那个时刻的。我怀疑她甚至根本不知道我离过婚。我确实一直瞒着。奥蒂斯和米奇知道。劳拉猜到了一点，但在那之前没说什么。"
    "而且我没说谎。我对南希的感情确实是矛盾的。我们已经结束了，我也永远不会跟她复合，但我确实想知道她过得好不好。只是想知道。不是叙旧。也不是要知道她现在的生活。"
    scene c002_s009_019 with Dissolve(1)
    "我们这么围坐着喝咖啡的片刻，怎么说呢，短短地有那么一点像正常日子。然后我望向窗外，一切又变得非常不正常。靠，连离我们不到十英尺的灌木都看不见，这本身就让人晕头转向。"
    scene c002_s009_020 with Dissolve(0.25)
    "这简直是斯蒂芬·金／约翰·卡朋克级别的鬼东西。浓得像要命的雾，而且联系上任何人都他妈像是在完成一项任务，哪怕我们并不在这个正在死去的镇子最落魄的角落。"
    "而且我们在这儿待得越久，我就越觉得外面可能根本一个人都没有。救援听上去像是白日梦。但我不能表露出来。得尽可能维持士气。"
    scene c002_s009_021 with Dissolve(0.25)
    j "那么，我想这话必须问了：我们还要试着回那家餐厅吗？"
    l "我觉得我做不到。不能连着两天去。说出来感觉挺疯狂的。你了解我的。我每天走六千到八千步。可过去这两天把我折腾惨了。"
    j "我可以自己去。卡莉可以教我怎么用那些设备。如果你愿意留在这儿的话。我想你也可以一起来，不过我一个人大概能走得更快。"
    scene c002_s009_022 with Dissolve(0.5)
    k "我……我觉得今天我们在这儿待着应该没问题。也许明天可以再试试。贩卖机里还有不少东西，只要有零钱。"
    j "最坏的情况，我可以把它撬开。或者砸碎玻璃。"
    scene c002_s009_023 with Dissolve(0.25)
    l "*叹气* 我知道这不该这么困扰我，但我就是不喜欢……{i}这样{/i}。"
    j "为了活下去而搜刮。{a=https://en.wikipedia.org/wiki/Hurricane_Katrina}卡特里娜飓风{/a}刚过时人们就这么干。情况也许不一样，但需求肯定一样。"
    l "我知道。只是……我从小连偷块口香糖都没干过。"
    scene c002_s009_024 with Dissolve(0.25)
    j "从没顺过当地五分店的唇彩？或者{a=https://www.claires.com/us/jewelry/earrings/}Claire's{/a}的耳环？我敢打赌卡莉年轻时也因为同侪压力顺过什么东西。"
    scene c002_s009_025 with Dissolve(0.25)
    k "*咯咯笑* 我不说。"
    j "这么说劳拉是这一群里唯一循规蹈矩的人了。"
    scene c002_s009_026
    l "哦？你也干过小偷小摸？除了过去几天弄来的衣服和吃的之外。"
    j "我可是一直在给贩卖机投钱的，这点要说清楚。虽然那钱有一部分是从奥蒂斯的备用金抽屉里挪的。不过改天我会还他。"
    "前提是我还能再见到他。想到他可能在这场雾之前就病着，我就担心他现在怎么样了。"
    l "你没回答我的问题。"
    scene c002_s009_027 with Dissolve(0.25)
    j "我读大学时在杂货店打工，可能偶尔顺手牵过羊。为了凑一晚上的晚饭钱，不小心弄坏过商品。"
    k "我也曾经把饮料弄错过。是故意的。把饼干掉在地上。也是故意的。"
    j "所以劳拉是这儿唯一一个规矩人。知道了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c002_s010_001 with Dissolve(2)
    play music insideday2 fadein 2.0
    "既然决定不再走一趟{i}汉堡店{/i}，我们就只能在办公室里消磨时间，很快就变得无聊透顶。与其说“变得”，不如说它本来就无聊，只不过那是在上班。"
    "但现在，那是在等一件可能发生也可能不会发生的事。而没有网络，也找不到什么可以消遣。"
    j "天哪，我现在愿意用一切换一台电视。就让我连着几个小时刷点什么。"
    l "就一台电视？"
    scene c002_s010_002 with Dissolve(0.25)
    j "如果是一支闪着红灯的车队开进来把我们救出去，我会更想要那个。但先从周一夜橄榄球开始也行。"
    l "今天是周一吗？我还以为是——"
    j "不是重点。我只想找点事杀时间。想到了橄榄球。"
    scene c002_s010_003 with Dissolve(0.25)
    l "我看家居园艺节目。卡莉？"
    k "Netflix 上有什么我看什么。找不到的时候就看《英国烘焙大赛》。"
    j "好主意。我超喜欢 Noel Fielding。"
    scene blank with Dissolve(2)
    scene c002_s010_004 with Dissolve(2)
    "没过多久，我们都散了，各自回到办公室里不同的角落。就连劳拉似乎也需要独处一会儿，消化最近发生的事。我想无论怎么聊，都改变不了她联系不上家人时的那种焦虑。"
    scene blank with Dissolve(2)
    scene c002_s010_005 with Dissolve(2)
    "我也想再问一次卡莉好不好，但她大概不会给出不同的回答。她把很多东西都憋在心里。我能感觉到她不想让我像个不受欢迎的监护人似的在她身边转悠。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_21_632", transition=Dissolve(1.0))()
    pause
    $ Hide("june_21_632", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c002_s010_006 with Dissolve(2)
    play music nightmain2 fadein 2.0
    "时间一点点过去，我意识到“起床／干等／睡觉”这样过一天对我没好处。对我们谁都没好处。不只有我一个人有这种感觉，这并不奇怪。"
    scene c002_s011_001 with Dissolve(1)
    j "嘿，我快睡了。"
    l "天已经黑了，说得通。来，坐一下。我想跟你说件事。一个想法。或者一个领悟。"
    scene c002_s011_002 with Dissolve(0.25)
    j "好啊，说吧。"
    l "[player_name]，我必须问你一个问题，而那个你明明知道是真的答案，你可能不会喜欢。"
    j "嗯，问吧。我有个想法。我最近也在琢磨一些事。"
    scene c002_s011_003
    l "要是救援不来会怎么办？我们怎么办？我们总不能永远待在这儿。我知道你对那个会来把我们弄出去的人抱有更多信心，但要是他们不来呢？"
    j "这件事我反反复复想了很久。一会儿觉得我们能不能留下、能留多久，一会儿又只想赶紧离开这儿。但说实话：你觉得政府会就这么把我们扔在这儿吗？"
    scene c002_s011_004 with Dissolve(0.25)
    l "我不确定是不是只有这儿，[player_name]。就算真的只是这儿，谁知道他们会不会干脆把受影响区域封锁起来，让我们自生自灭。也许再派几个科学家来查清这是什么。"
    j "*叹气* 我想过。我知道我们——人类——以前也不是没干过把整座城市扔掉任其腐烂的事。辐射区、不适合人类生存的地方，比如切尔诺贝利和福岛隔离区。我只是……不想去考虑我们已经是这样了。"
    scene c002_s011_005 with Dissolve(0.25)
    l "但如果真的只是这儿，我们可能不得不考虑下一步。靠，哪怕不是。"
    j "比如说想办法离开？我本来会说“离开这儿”，但我不知道{i}这儿{/i}到底指多大范围。三个街区的半径？整座城市？"
    l "至少，我们可以试着往餐厅那边靠近一点。眼下它看起来是我们能弄到食物的最近选择，所以我们最好别放着这么长一段路不去走。尤其外面还飘着那烟。"
    scene c002_s011_006 with Dissolve(0.25)
    j "我不反对这个主意。但去哪儿？紧挨着它的那栋办公楼大概是最好的选择。我们怎么进去？"
    l "不知道。我还没想到那么远。只是随口一提。"
    j "好吧，好吧。我出去看一眼。明天。不是现在。我不喜欢摸黑去任何地方。但我会去拿吃的，顺便在外面看一眼。"
    scene c002_s011_007 with Dissolve(0.5)
    l "这主意聪明。我……我想我们现在没必要冒险。"
    j "是啊，不过我最好还是休息一下。我们已经看到在外面待久了会把人磨成什么样。要是我的侦查之行有用，我得把每一分力气都用上。"
    l "我懂。"
    scene c002_s011_008 with Dissolve(0.25)
    l "嘿，[player_name]……我……抱歉我一直这么难搞。或者说，一直以来都很难搞。我很难受。我是个习惯的生物，被困在这儿对我一点好处都没有。我讨厌闲着。"
    j "我理解。你喜欢一天结束时能回家。或者更不喜欢被困在这种地方。"
    scene c002_s011_009 with Dissolve(0.5)
    l "是啊。家。"
    "是我听错了吗？听起来好像还有别的。或者，可能只是她不太能应付被困在这儿这件事。"
    menu:
        "别提。":
            "别管了。我们每个人情绪都不太好，对事情过度解读没有好处。我们在这儿都有些绷得太紧，去戳她只会让情况更糟。"
            scene c002_s011_014 with Dissolve(0.5)
            j "那么……"
            l "是啊。我……我知道我们今天没做多少事，但我真是累垮了。"
            scene c002_s011_015 with Dissolve(0.25)
            j "好好好。我昨天可是睡了六个小时。这局面对谁的睡眠和饮食习惯都没帮助。好了，我让你一个人待会儿，好好休息。"
            l "谢谢。明天再聊。"
            j "我一定。"
            scene c002_s011_010 with Dissolve(1)
            "看她没有聊天的兴致，我就离开了劳拉，回到我的长凳上。如果明天那趟路跟前几次一样，我就得把每一点有限的力气都用上。"
        "说点什么。\n[rgr](劳拉 好感\信任 +1)":
            $ l_friend += 1
            $ l_trust += 1
            j "劳拉？我……感觉好像还有别的事。你没事吧？而且我说的是“在这堆破事发生之前你就已经没事吧”。"
            scene c002_s011_016 with Dissolve(0.25)
            l "*叹气* 只是……大人的事。"
            j "我是个成年人。这点你是知道的，对吧？过来。"
            scene c002_s011_011 with Dissolve(0.25)
            l "是的，我清楚。只是……我现在不想谈这个。我很累，可能也有点情绪。"
            j "明白。"
            scene c002_s011_012 with Dissolve(0.25)
            l "只要……只要当我是个哥们儿。行吗？"
            j "所以，安静又让人安心。"
            l "拜托。"
            scene c002_s011_013 with Dissolve(0.5)
            "我们在那儿坐了一会儿，我的手臂搂着劳拉，她的手放在我的手上。她没说话，但似乎很珍惜这一刻。我没想过，她也许只是需要一个温暖的身体抱着，才能平静下来。"
            scene blank with Dissolve(2)
            scene c002_s011_010 with Dissolve(2)
            "过了一阵子，我离开劳拉，回到我的长凳上。如果明天那趟路跟前一次一样，我就得把每一点有限的力气都用上。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_21_1112", transition=Dissolve(1.0))()
    pause
    $ Hide("june_21_1112", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c002_s012_001 with Dissolve(2)
    "当然，我还是在某个时候醒了过来。凝滞的空气和缺少背景噪音显然没什么帮助。而且我睡姿变得很奇怪，髋部的一块肌肉开始发僵。"
    scene c002_s012_002 with Dissolve(0.5)
    "我决定起来走走，顺便看一眼外面。我没指望能看到什么。这已经有点像是用来平心静气的冥想了。"
    scene c002_s012_003 with Dissolve(1)
    "所以，劳拉已经在考虑搬了。离开这儿，到离食物更近的地方去。说得通，我也不能说自己没在琢磨这事。她提到想去看看附近那栋办公楼。"
    "据说那地方已经废弃了，所以我不确定我们会在那儿找到什么。也不知道能不能进去。要是关了一段时间，也许空调一直没开，我们就不用担心雾渗进去。至少眼下不用。"
    "没必要……"
    scene c002_s012_004 with Dissolve(0.5)
    "等等。那是什么？有动静？外面有人？"
    scene c002_s012_005
    j "我勒个去。嘿！嘿！！"
    scene c002_s012_006 with vpunch
    "*砰* *砰*"
    scene c002_s012_005 with Dissolve(0.25)
    j "嘿！这边！嘿！！到这边来！！！看这边！！"
    "靠，看样子他们没看见我。看来得狠狠敲玻璃才能引起注意。"
    scene c002_s012_007 with Dissolve(0.25)
    k "呃，嘿，怎、怎么了？"
    j "靠。抱歉把你吵醒了。我好像看见外面有人动了。"
    scene c002_s012_008
    k "真的？有人在夜里到处跑？"
    scene c002_s012_009 with Dissolve(0.25)
    j "我知道。我也很吃惊。来，看那边。"
    scene c002_s012_010
    k "我……我不……"
    j "应该是走了。该死。"
    scene c002_s012_011 with Dissolve(0.25)
    k "不不，那边！我看见了。他们正往这边来。"
    scene c002_s012_013
    j "嘿！嘿！！我觉得他们既看不见我们，也听不见我们。"
    k "如果、如果他们在外面，那他们看东西和呼吸可能都很费劲。"
    scene c002_s012_014 with Dissolve(0.25)
    j "靠，你说得对。我把衣服穿上，出去看看能不能把他们带进来。"
    k "好、好的。我留在这儿，看看能不能引起他们的注意。"
    scene c002_s012_015 with Dissolve(0.25)
    j "很好，很好。"
    scene blank with Dissolve(1)
    scene c002_s012_016 with Dissolve(1)
    l "外面那是什么鬼动静？"
    j "外面有人。我出去把他们带进来。卡莉在前头，正试着引起他们的注意。"
    scene c002_s012_017 with Dissolve(0.25)
    l "你……等等……你在外面？"
    j "对，对。我们俩都看到他了。"
    scene c002_s012_018 with Dissolve(0.25)
    l "好、好的。你在外面小心点。"
    scene blank with Dissolve(1)
    scene c002_s012_019 with Dissolve(1)
    l "嘿，卡莉。那个人在哪儿？你知道是男是女吗？"
    k "完全不知道。那边雾太大，我一下就跟丢了。他一直在来回移动，可就是不够近，我看不清细节。"
    scene c002_s012_020 with Dissolve(0.25)
    l "好，那我们就留意着。还有，[player_name]应该快绕过来了，我刚看见他出去。"
    k "所以他会从那边进来。"
    scene c002_s012_021 with Dissolve(0.25)
    l "对。靠，他有手电筒吗？"
    k "他有手机……应该是吧。"
    scene blank with Dissolve(2)
    scene c002_s012_022 with Dissolve(2)
    "好吧，也许是我想多了，但现在外面好像没那么浓了。不过还是黑得要命。我能看见远处路灯的光晕，别的就什么都看不见了。"
    scene c002_s012_023 with Dissolve(0.5)
    "我手机上的手电筒应用跟 Maglight 没法比，但也只能凑合用了。"
    "得抓紧点。我不想在外面待太久，不管这人是谁，在外面肯定已经有一阵子了——我是说，我猜的。搞不好就像劳拉那样，躲在几条街外的车里。"
    scene blank with Dissolve(2)
    scene c002_s012_024 with Dissolve(2)
    l "*叹气* 我什么也没看见。[player_name]，还有那个别的人。"
    k "我发誓我们看到有人了。"
    scene c002_s012_025 with Dissolve(0.25)
    l "哦，我相信你。只是现在根本看不清任何东西。太黑了，雾气也太重。"
    scene c002_s012_026 with Dissolve(0.25)
    l "等等，我看到了……"
    k "就是他。我觉得是。对。"
    scene c002_s012_027 with vpunch
    l "嘿，这边！"
    k "哦。哦，操。"
    play music horror fadein 2.0
    scene c002_s012_028 with Dissolve(0.5)
    $ l_anxiety +=1
    $ k_anxiety +=1
    l "什么玩意儿？"
    if persistent.ch2_complete == False:
        $ persistent.ch2_complete = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_chapter2", transition=slideright)()
        pause
        $ Hide("achievement_chapter2", transition=dissolve)()
        $ quick_menu = True
    scene blank with Dissolve(2)
    stop music fadeout 2.0
label chapter03:
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("chapter03", transition=Dissolve(1.0))()
    pause
    $ Hide("chapter03", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c003_s001_001 with Dissolve(2)
    play music horror fadein 2.0
    l "那是……那他妈到底是什么？"
    k "我、我我不是唯一看见那个东西的人吧？它不是……不……天啊。"
    scene c003_s001_002 with Dissolve(0.25)
    "{color=#66ff33}冷静点，劳拉。这是什么恐怖片里的鬼东西，可它好像正在走开。它没听见我们。应该没有吧……大概。{/color}"
    l "退后，退后。离窗户远一点。安静地，慢慢地。退、退到走廊里去。"
    k "……好。对。"
    scene c003_s001_068 with Dissolve(1)
    "{color=#66ff33}那是什么？看着像人，可是……烧焦了。畸形了。在外面待太久就会变成那样吗？我……{/color}"
    scene c003_s001_003 with Dissolve(0.5)
    l "靠，[player_name]还在外面。他出去「帮忙」了。他肯定没看见。"
    scene c003_s001_004 with Dissolve(0.25)
    k "我好像还能看见它。天啊，它那样抽搐真是瘆人。它是在走开，对吧？"
    scene c003_s001_005 with Dissolve(0.25)
    l "对，我觉得是。我们就待在这儿，别靠近窗户。天这么黑，希望它没看见我们。"
    l "你听，我必须出去——"
    scene c003_s001_006 with Dissolve(0.25)
    k "为什么？我们在里面是安全的，对吧？"
    l "也许吧。我觉的是。那玻璃挺厚的，隔音效果也不错。得拿车撞才能撞碎——可、可是[player_name]在外面。我得赶在他碰上{i}那个东西{/i}之前把他找回来。他完全不会想到。"
    scene c003_s001_007 with Dissolve(0.25)
    k "我……好。那、那我该做什么？"
    l "就待在这儿。如果你看见[player_name]，试着引起他的注意。让他赶紧回来。警告他。"
    scene c003_s001_008 with Dissolve(0.25)
    k "怎么做？我要是砸窗户，那东西不是会听见吗？然后折回来？你刚不是说玻璃很厚、隔音很好吗？"
    scene c003_s001_009 with Dissolve(0.25)
    l "我也不知道。冲他挥手。跳起来。{b}闪他{/b}。男人对「看到一对奶子」有种第二直觉。好像他们就是没法错过。"
    k "呃啊……"
    scene c003_s001_010 with Dissolve(0.25)
    l "我开玩笑的。大部分时间是。我穿上衣服，看看能不能找到他。"
    k "可、可是，你的……"
    scene c003_s001_011 with Dissolve(0.25)
    "{color=#ffcccc}你的呼吸怎么办？你现在这个状态可不适合干这种事。而且，我刚才只是站在这儿，吓得什么都不敢做。像个胆小鬼。{/color}"
    k "*叹气*"
    scene blank with Dissolve(2)
    scene c003_s001_012 with Dissolve(2)
    "靠。手机手电筒一点用都没有。雾太他妈浓了，反而让黑暗更难看穿。光一照过去，就像在我面前竖了一堵雾墙，什么都透不过去。"
    scene c003_s001_013 with Dissolve(0.25)
    j "嘿！你在外面吗？！我看见你在那边走动。我来救你了！"
    "好吧，我刚才那话听起来蠢透了。我显然不太擅长「告诉别人我在这里，要把你们带到安全的地方」这种事，是吧？"
    scene c003_s001_014 with Dissolve(0.25)
    j "喂！我看不见你。你要是能喊一声，我就过去找你。我不知道你在外面待了多久，但我能带你去个安全的地方！"
    "什么都没回应。而且我自己也没搞清现在的位置。办公室的后墙不是应该在这个方向吗？"
    scene c003_s001_015 with Dissolve(0.25)
    j "嘿！我在这儿——"
    scene c003_s001_016 with vpunch
    l "[player_name]。"
    scene c003_s001_017 with Dissolve(0.25)
    j "靠。劳拉。我不是……你怎么跑出来了？"
    scene c003_s001_018 with Dissolve(0.25)
    l "回来吧。跟你想的不一样。还有，小声点。"
    j "好……"
    scene blank with Dissolve(2)
    scene c003_s001_019 with Dissolve(2)
    "{color=#ffcccc}我什么也没看见。这是好事。但又不算好事，因为[player_name]和劳拉还在外面。希望他们没事。{/color}"
    "{color=#ffcccc}我刚才应该自己出去的，而不是让劳拉去。她的呼吸还是有问题，像是得了哮喘什么的。可我实在太胆小了。{/color}"
    scene c003_s001_020 with Dissolve(0.25)
    "{color=#ffcccc}糟糕。我现在只穿着内裤站在这儿。我过来的时候都没想起来这茬。不过话说回来，[player_name]也是。还有劳拉。看来这情况也不给我们留什么隐私。{/color}"
    scene c003_s001_021 with Dissolve(0.25)
    "{color=#ffcccc}我该跑回去把裤子拿过来。等着的时候先穿上。{/color}"
    scene blank with Dissolve(2)
    scene c003_s001_022 with Dissolve(2)
    j "劳拉，这他妈到底怎么回事？外面有人。我看见他了。"
    scene c003_s001_023 with vpunch
    l "*咳嗽* *咳嗽* 不 *咳嗽* 不是……"
    j "你不该出来的。我一个人没事的。"
    scene c003_s001_024 with Dissolve(0.25)
    l "有东西*咳嗽*不对劲。相信我。现在我们安静下来，回办公室去。拜托。"
    j "好好好。来，我扶你。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c003_s001_025 with Dissolve(2)
    play music nightmain fadein 2.0
    j "好了，我们回来了。到底怎么回事？"
    scene c003_s001_026 with vpunch
    l "*咳嗽* 等一下。"
    j "我们送你去洗手间吧。看看能不能给你冲一冲——"
    scene c003_s001_027 with Dissolve(0.5)
    k "你们在吗？"
    j "在。劳拉在我找到那个人之前把我拽回来了。"
    scene c003_s001_028 with Dissolve(0.25)
    k "那不是个人。它……我不知道。劳拉？"
    scene c003_s001_029 with Dissolve(0.25)
    l "我、我没事。让我先喘口气。"
    j "你说「不是个人」是什么意思？"
    scene c003_s001_030 with Dissolve(0.25)
    l "就像一个被严重烧伤、毁容的人。像是电影里的怪物。"
    k "我觉得它自己走开了。你出去之后我再看就没了。"
    scene c003_s001_031 with Dissolve(0.25)
    j "好、好的。呃……卡莉，你能送劳拉去洗手间洗一下吗？我回窗边看看能不能发现什么。"
    k "好、好的。你不用也去洗洗吗？"
    j "我会——等一下——但我想先看看他们是不是还在外面。"
    scene c003_s001_032 with Dissolve(0.25)
    l "眼下总得有人盯着。"
    j "我也是这么想的。"
    scene blank with Dissolve(2)
    scene c003_s001_033 with Dissolve(2)
    "好，所以我完全搞不懂这里到底他妈发生了什么。我出去想在黑暗里找到那个「人」，结果他们告诉我那根本不完全算个人。「像是电影里某种怪物」。所以，也许我运气好，没撞上他。"
    "一定严重到让劳拉觉得非追出来不可了，可这是个糟糕的主意，因为她呼吸还很困难。她之前在外面待那么久，肯定受了不轻的伤。要是有医生就好了，我一定带她去看。"
    scene c003_s001_034 with Dissolve(0.25)
    "真不知道该盯着什么看。天又黑，眼前全是雾。我倒想把灯打开，但暂时不暴露我们在这儿可能是更聪明的做法。"
    "不过我刚才确实喊了、也砸了窗户想引起他们注意。我那么做的时候，那东西确实朝我们这边走了一小会儿。"
    scene c003_s001_035 with Dissolve(0.5)
    k "嘿，你需要洗一下吗？"
    j "对。我确实该洗。我眼睛里进了一些。那种雾里根本没法戴墨镜。"
    scene c003_s001_036 with Dissolve(0.25)
    k "她需要缓一会儿，不过听起来咳嗽好些了。"
    j "好吧，那就好。你有没有——"
    scene c003_s001_037 with Dissolve(0.25)
    k "我没事。我就待后面。可要是我开始喊了……"
    j "我知道。我就冲过来。"
    scene blank with Dissolve(2)
    scene c003_s001_038 with Dissolve(2)
    j "劳拉，好点了吗？"
    l "好一点。感觉还是像有人往我脸上泼了清洁剂。"
    scene c003_s001_039 with Dissolve(0.25)
    j "我懂。那你从头给我讲一遍，刚才他妈到底发生了什么。"
    l "你出去之后，我和卡莉上到这边来看你说的东西。本以为外面只是有人需要被拦下来，这里待着是安全的。我们看见那个「人」在附近跌跌撞撞，但直到它走近才看清楚。"
    scene c003_s001_040 with Dissolve(0.5)
    l "它——我说{b}它{/b}，是因为我实在不知道还能怎么形容这东西——看起来像个类人的怪物。是啊，当时天还黑，所以我们没看得很仔细，但看到的部分很恐怖。像是被严重烧伤。头上没有头发。面目全非。"
    k "我甚至不知道它有没有穿衣服。"
    scene c003_s001_041 with Dissolve(0.25)
    l "这也看不清。天还是太黑。我只知道它不对劲。我想说它不像人，可它又确实是人样。有胳膊。有腿。只是近到让人感觉不对。好像我们本能地知道它不该长成那样。"
    j "好~~~ 所以这就是你跑出来抓我的原因。"
    scene c003_s001_042 with Dissolve(0.25)
    l "一时冲动吧。我想我只是不想让你撞见它。真不知道你要是撞上了会怎么样。"
    j "恐怖片看多了，看什么都往最坏处想。"
    scene c003_s001_043 with Dissolve(0.25)
    k "现在这情况只会更糟。跟外界断了联系，我们本来就绷得很紧。现在又来这个？你不能怪我们指望它能……我也不知道。反正点什么吧。"
    l "也许我只是觉得，在搞清楚它是什么、能做什么之前，最好别惊动它。"
    scene c003_s001_044 with Dissolve(0.25)
    j "或者，万不得已的时候，我们手上得有件能自保的东西。"
    l "没错。我想在我们回来的这段时间里，它已经走开了。"
    k "它走了。应该说是。我去……呃，把裤子穿上，回来就找不到它了。"
    scene c003_s001_045 with Dissolve(0.25)
    l "看来那些喊叫和挥手并没有真的引起它的注意。谢天谢地。"
    j "也许这侧的玻璃墙为了隔音是做了气密处理的。或者，如果它不算完全是人，也许它听力没那么好。我也说不准。不过现在，我……我不确定我们该怎么办。"
    scene c003_s001_046 with Dissolve(0.25)
    j "我可以待在这儿守着，看看它会不会过来。"
    k "我今晚别想睡着了。而且我不想一个人待着。就算知道你们两个就在附近也不行。"
    scene c003_s001_047 with Dissolve(0.25)
    l "我跟卡莉在一起。这事弄得我心神不宁。也许我们就待在一块儿吧。至少一阵子。"
    j "好，那我就待在这儿。你想来陪我当然可以。不过，也许你该找时间睡一会儿。"
    scene c003_s001_048 with Dissolve(1)
    "这说得通。我们都被刚才发生的事弄得不安起来。我自己没看见他们描述的东西，只能相信这不是什么由紧绷的神经加上压力催生的想象所产生的幻觉。"
    "但无论劳拉还是卡莉，都不像是会无缘无故发疯的人。外面确实有什么东西。有什么东西让她们害怕。"
    scene blank with Dissolve(1)
    scene c003_s001_049 with Dissolve(1)
    "于是我们背靠着墙坐得离窗户尽可能远。要是有东西过来，得靠得很近我们才能发现。某种程度上，我觉得只要天还黑，我们就都能相安无事地什么都不看见。"
    scene c003_s001_050 with Dissolve(0.5)
    l "这里有没有什么能当武器用的东西？"
    j "我没有枪也没有刀，什么都没有。"
    scene c003_s001_051 with Dissolve(0.25)
    k "我包里有辣椒喷雾。"
    j "*轻笑* 外面多的是辣椒喷雾。"
    scene c003_s001_052 with Dissolve(0.25)
    l "*咯咯笑* 这话比我想的还要真实，不过总比没有强。"
    j "明天我可以搜一遍。看看能不能找到什么结实或者够重的东西。也许米奇办公室藏着些什么。"
    l "我……我们可以。"
    scene c003_s001_053 with Dissolve(0.5)
    "我总是会忘记劳拉其实挺能干的，我不该表现得好像这里只有我一个人能干活的样。她们两个都是成年人（尽管我还是很难不把卡莉当成个刚毕业的女孩）。"
    scene blank with Dissolve(1)
    scene c003_s001_054 with Dissolve(1)
    "我不知道过了多久（我拿手机当地钟），我们就这么沉默地坐着，盯着在黑暗中流动的雾。"
    "时间一定够长，长到卡莉又睡着了。她居然能睡着，我有点意外——也有点松了口气。"
    scene c003_s001_055 with Dissolve(0.5)
    l "她一定是觉得安全了。"
    menu:
        "或者是累得顾不上了。":
            j "或者是累得顾不上了。总有个时候，肾上腺素会消退。"
            scene c003_s001_056 with Dissolve(0.25)
            l "她运气好。[player_name]，这就说到了我们真得做决定的一件事。我确实觉得我们必须考虑搬走。说真的。哪怕今晚的事没发生也该这么觉得。"
        "你不这么觉得？\n[rgr](劳拉 好感 +1)":
            $ l_friend += 1
            j "你不这么觉得？"
            l "不是这么回事。这里本来就不是个适合睡觉的地方，就算在最好的时候也是。但人多力量大，待在你认识、能依靠的人身边才安全。"
            scene c003_s001_056 with Dissolve(0.25)
            l "但我确实觉得我们必须考虑搬走。说真的。哪怕今晚的事没发生也该这么觉得。"
    j "搬到离食物更近的地方？对。现在更该搬了，因为外面有个可能危险的东西在游荡。不管它到底危不危险。"
    scene c003_s001_057 with Dissolve(0.5)
    l "在我看来它就是个危险。我不想再冒不必要的风险了。在{i}汉堡店{/i}看到那具尸体之后，我没法不觉得，这一切比我们愿意承认的要严重得多。"
    l "这不是什么「不方便」。这可能是生死攸关的事。"
    menu:
        "明早跟卡莉谈谈。[yl]":
            j "明早跟卡莉谈谈。"
            scene c003_s001_058 with Dissolve(0.25)
            l "我确定她会同意，不过我们还是该在做决定之前问问她。这关系到我们所有人。"
        "早上就出发，制定计划。[yl]":
            j "早上就出发，制定计划。等我们三个都醒着的时候。"
            scene c003_s001_058 with Dissolve(0.25)
            l "我确定卡莉会同意的。"
        "[rd]我再想想。\n[rrd](劳拉 焦虑 +1)":
            $ l_anxiety += 1
            j "我再想想。明天早上再聊。"
            scene c003_s001_058 with Dissolve(0.25)
            l "一定会的。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_22_728", transition=Dissolve(1.0))()
    pause
    $ Hide("june_22_728", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday fadein 2.0
    scene c003_s001_059 with Dissolve(2)
    "我醒来时已经是早上。我完全不记得自己什么时候睡着的，不过睡神显然还是来过了。我一动，就感觉到背和脖子因为姿势别扭而僵硬得厉害。"
    scene c003_s001_060 with Dissolve(0.5)
    "劳拉大概也一样，她正瘫在我身上。"
    scene c003_s001_061 with Dissolve(0.5)
    "那卡莉呢？她不知怎么滑了下去，半挂在我的腿上。我要是想站起来，就得把两个人都叫醒。"
    "我当然绝不会说出口，但那一刻我闻到了一股味道，确认我们仨都需要洗个澡、换身干净衣服。我有点替她们难过，因为就算在最好的情况下，我也会出点汗。"
    scene c003_s001_062 with Dissolve(0.25)
    k "唔嗯~~~"
    scene c003_s001_063 with Dissolve(0.5)
    k "*打哈欠*"
    j "早啊，小太阳。"
    scene c003_s001_064 with Dissolve(0.25)
    k "哦。呃……我……"
    "她对自己那样窝在我身上有点不好意思。我敢打赌不是故意的。"
    scene c003_s001_065 with Dissolve(0.25)
    j "你睡得好吗？"
    k "我浑身酸痛。还僵得很。"
    scene c003_s001_066 with Dissolve(0.5)
    l "唔嗯~~~ *呻吟*"
    l "可不是我预想中*打着哈欠*睡着的方式。"
    scene c003_s001_067 with Dissolve(0.25)
    j "我可不知道自己当枕头够不够格。"
    l "你够暖和的。"
    scene blank with Dissolve(2)
    scene c003_s002_001 with Dissolve(2)
    "我去给大家弄咖啡的时候，卡莉和劳拉踉踉跄跄地去了洗手间洗漱。从大家起来时那副吱呀作响、哼哼唧唧的样子来看，我猜没人睡得舒服，也没人睡够。"
    scene c003_s002_002 with Dissolve(0.25)
    "我趁这会儿没人在，又往外瞧了瞧依旧笼罩着办公室的雾。现在太阳升起来了，能见度基本等于零。昨晚在外面跌跌撞撞的东西已经走了。至少，我打算这么跟自己说。"
    "我虽然没亲眼看见两位姑娘看到的东西，但我信她们，所以还是担心。我昨晚最初的判断是「有人迷失在雾里」，依据只是看到一个人形的轮廓在跌跌撞撞。我当时只是以为对方是迷失了方向。"
    "我是说，劳拉当时来的时候状态就糟。现在也是。我有时能听出她声音里的沙哑。如果外面那个人比她多待一个小时，可能急需医疗救助。"
    scene c003_s002_003 with Dissolve(0.25)
    "但她们说看到的东西像个怪物。某个皮肤被烧伤、不太像人的——如果它曾经是人的话。"
    "这下我脑子里的某个开关被拨动了。上次从{i}汉堡店{/i}回来的时候，我看见停车场里有东西在动。是同一个吗？当时我只当是眼花。"
    "现在呢？谁知道呢？如果是，那就会冒出更多问题，而其中很多都暗示着情况比我们最初想的要糟得多。"
    scene c003_s002_004 with Dissolve(0.25)
    l "嘿，你睡得好吗？我刚才都没想起来问。现在我脑子也不太在状态。"
    menu:
        "我想你已经知道答案了。[yl]":
            scene c003_s002_005 with Dissolve(0.25)
            j "我想你已经知道答案了。"
            l "果然。我现在能有一张床睡就谢天谢地了。"
        "夹在两个女人中间？好啊。[yl]":
            scene c003_s002_005 with Dissolve(0.25)
            j "夹在两个女人中间？好啊。*轻笑*"
            l "我要跟人力资源部举报你这番不恰当的工作对话。"
            j "让他们来这儿开我啊。"
    scene c003_s002_006 with Dissolve(0.5)
    l "那你看到什么了吗？外面？"
    j "起来之后就没看到。可能是雾太浓。也可能是阳光让人看不清什么。靠，我现在连那边的灌木都看不见。"
    scene c003_s002_007 with Dissolve(0.25)
    l "我想这算好事。也算坏事。我分不清。大概是坏事吧，因为不管那是什么，它还在外面。我们不知道它在哪儿，也不知道它还会不会回来。"
    j "也不知道它有没有敌意。"
    scene c003_s002_008 with Dissolve(0.25)
    l "我们必须当它可能有敌意来对待，[player_name]。这一切对我们来说都非常危险，什么都不能想当然。"
    j "我知道，可也许只要躲着它就没事。除了亲眼看见它——好吧，是你们俩看见了——我们不知道它是什么，也不知道它想要什么。"
    scene c003_s002_009 with Dissolve(0.25)
    l "*叹气* 也是。虽然我们还是得考虑换个地方。我知道我昨晚提过，但我不喜欢我们在这儿这么暴露。而且我们要去目前最好的食物来源那儿得走很远，天知道那还能撑多久。"
    j "我考虑过了。我们得确保卡莉也同意。就是说，别做那种她被迫跟着走的独断决定。"
    scene c003_s002_010 with Dissolve(0.25)
    l "我觉得不成问题。她嘴上不说，但你看得出来她已经受够了。"
    if k_anxiety >= 2:
        scene c003_s002_011 with Dissolve(0.25)
        j "说起卡莉……她在哪儿？"
        l "我出来的时候，她还在洗手间里磨蹭。"
        menu:
            "去看看她。\n[rgr](卡莉 信任 +1)":
                $ k_trust += 1
                scene c003_s002_013 with Dissolve(0.5)
                j "唔嗯。我去看看她有没有事。昨晚那些事本来就够多了，可能把她吓到了。"
                l "好，那我去把咖啡弄完。顺便盯着点。"
                scene blank with Dissolve(1)
                scene c003_s002_014 with Dissolve(1)
                "好了，她来了。听上去她刚哭过，正在努力让自己镇定下来。几声压抑的抽鼻子，还有使劲让自己重新振作的动静。"
                j "卡莉？嘿，你还好吗？"
                if k_friend >= 3:
                    scene c003_s002_016 with Dissolve(0.25)
                    k "*吸鼻子* 说实话，没有。我只是……这糟透了。"
                    scene c003_s002_017
                    k "一切都糟透了。我只想回家。我想见安德鲁。想见我的家人。而且我害怕、又累、又浑身疼、还饿。"
                    j "我知道。抱歉这么糟。"
                    scene c003_s002_018 with Dissolve(0.25)
                    k "你道什么歉？又不是你的错。"
                    j "因为总得有人说出来。我又没法让上帝认罪，毕竟他是我心里头该为这一切负责的第一号人物。"
                    scene c003_s002_019 with Dissolve(0.25)
                    k "*咯咯笑* 哦，这话太可怕了。而且还亵渎神明。"
                    j "是啊，但逗你笑了，所以你也没那么介意。"
                    scene c003_s002_020 with Dissolve(0.25)
                    k "也许吧。别让劳拉等太久了。"
                    scene blank with Dissolve(1)
                    scene c003_s002_021 with Dissolve(1)
                    l "你来了。咖啡？"
                    k "好的，谢谢。我、我听见你们两个在说话。在说什么？"
                else:
                    scene c003_s002_015 with Dissolve(0.25)
                    k "唔嗯~~~ *吸鼻子* 嗯，嗯。就……给我一分钟，好吗？"
                    j "好。没事的。你要是想聊聊……"
                    k "不不，我没事。我没事。只是……走吧。我们回去。"
                    "努力装出一副勇敢的样子。看来我们还不够亲近，她不想跟我交心。"
                    scene blank with Dissolve(1)
                    scene c003_s002_021 with Dissolve(1)
                    l "你来了。咖啡？"
                    k "好的，谢谢。我、我听见你们两个在说话。在说什么？"
            "[rd]别烦她。\n[rrd](卡莉 焦虑 +1)":
                $ k_anxiety += 1
                scene c003_s002_013 with Dissolve(0.5)
                j "好，那她大概就是想一个人待会儿。也许是跟别人待太久了。或者，也许只是跟我。*轻笑*"
                l "对啊，我老忘了她不是那种多数人里的社交达人。"
                scene blank with Dissolve(1)
                scene c003_s002_012 with Dissolve(1)
                "几分钟后，卡莉慢慢晃了回来，脸有点红，使劲憋着不太成功的抽泣。"
                j "咖啡？糖、奶油，对吧？"
                k "好的，谢谢。我、我听见你们两个在说话。在说什么？"
    else:
        scene c003_s002_012 with Dissolve(0.5)
        k "同意什么？"
        scene c003_s002_021 with Dissolve(0.5)
    l "搬家。离开办公室。我知道我们一直在把这事挂在嘴边——算是暗示该做了——但我觉得它已经不能再拖了。"
    scene c003_s002_022 with Dissolve(0.25)
    k "我……我真的不想再待在这儿了。我不想再等一个不会来救我们的人，而且经过昨晚，我觉得这里已经不安全了。"
    k "我想回家，可既然看起来短期内没指望，那我接受任何看起来算是进展的东西。"
    scene c003_s002_023 with Dissolve(0.25)
    l "我们在这里有点太暴露了。这边和入口旁边都是大玻璃窗。万一有人想闯进来呢。再说了，我也不想每隔好几天才吃一顿。那段路我实在走得太吃力，我想尽量减少我们待在外面的时间。"
    "也能理解，毕竟她冲出去把我带回来，对她的身体状况毫无帮助。"
    l "[player_name]？你怎么想？"
    scene c003_s002_024 with Dissolve(0.25)
    j "对，对。我也不想再在这儿待下去了。反正我们又没有加班费。你走得了这段路吗？因为我们要是走了，就不回来了。"
    l "我、我们慢慢走的话我能撑住。"
    k "我们可以中途停好几次，对吧？要去哪儿来着？我记得我们其实没定下来。"
    scene c003_s002_025 with Dissolve(0.25)
    j "我们看的是「普罗维登斯人寿」那栋楼，对吧？就在{i}汉堡店{/i}隔壁。至少我们可以先过去看看，说不定我还能四处转转。"
    l "好，既然计划是这样，我们就该把想带走的东西都拿上。把那个背包塞满吧。"
    j "我去各处转转，看看有没有什么「能当武器」的东西。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_17_915", transition=Dissolve(1.0))()
    pause
    $ Hide("june_17_915", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday2 fadein 2.0
    scene c003_s002_026 with Dissolve(2)
    "先不说我们并没有更好的方案，我猜大家都受够这个地方也不算牵强。幽闭感、压力，再加上对前一晚那个访客的恐惧，三者叠加，压过了「也许有人正在这里找我们」那点正在熄灭的希望。"
    "现在讨论{b}怎么走{/b}可能还太早，但我越来越强烈地觉得，我们只能靠自己脱身了。不过，「徒步走出这个镇子」的前景看起来并不乐观。"
    scene blank with Dissolve(1)
    scene c003_s002_027 with Dissolve(1)
    "接下来一个小时左右，我们把办公室搜了一遍，看看有没有值得带走的东西。我还从贩卖机里拿了些零食，以防万一。"
    "可惜，除了订书机和拆信刀，没有任何能当武器的东西。我还盼着米奇也许在办公桌里藏了把枪。我倒是找到了一只手电筒，比我的手机强太多了。"
    scene blank with Dissolve(1)
    scene c003_s002_028 with Dissolve(1)
    "收拾妥当后，我们带上了出行装备。背包里塞满了所有可能用得上的东西，我们就出发了。离开时谁都没说话。也没有人道别。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c003_s003_001 with Dissolve(2)
    play music outsideday2 fadein 2.0
    "就这样，我们出了门，在雾里跋涉。感觉雾比之前更浓了。至少比昨晚更浓，不过我愿意把这归因于天黑、看不真切。"
    "这大概是迟早的事。头一两天，我还愿意相信这一切都是暂时的，或者会有人来帮忙。现在呢？我们只能靠自己了。我们会讨论怎么走出这个镇子最合适（前提是这场灾难只存在于{i}这里{/i}）。"
    scene c003_s003_002 with Dissolve(0.5)
    "虽然不是我提的，但我看得出卡莉一直在照看劳拉——她受雾气的影响还很严重。即便戴了口罩，她还是吸入了足够多的雾，呼吸听起来很粗重。"
    scene c003_s003_003 with Dissolve(0.5)
    "我只能假设，时间一长，再多的防护也挡不住这雾造成的伤害。"
    "劳拉会不会因此落下什么病根？我们会不会？我预期我们走出去得越多，遭受同样不良影响的概率就越高。"
    scene c003_s003_004 with Dissolve(0.5)
    "我？我会随时环顾四周，找我们的「怪物」。总得有人值班。而且说实话，谁也不知道它会在哪儿现身，会对我们造成什么危险。"
    "不过真要看见什么，我得有个应对方案。比如命令卡莉带劳拉去安全的地方，而我负责引开它？除此之外？我不知道。我甚至还不确定我们面对的到底是什么。"
    scene blank with Dissolve(2)
    scene c003_s003_005 with Dissolve(2)
    j "在这儿。门没锁。"
    scene c003_s003_006 with Dissolve(0.5)
    l "*咳嗽* *咳嗽* 操。" with vpunch
    k "好好好，给你。"
    l "我先坐一下 *咳嗽*。"
    j "背包里有点水。我去给你拿一瓶，你可以漱漱口。喝点。应该会好受些。"
    "希望吧。"
    scene blank with Dissolve(1)
    scene c003_s003_007 with Dissolve(1)
    k "好点了吗？"
    l "嗯。好一点了。谢谢。"
    "不是想催她，但我们不能在这儿待太久。就算那扇门是锁着的，前门也正把那玩意儿不停地漏进来，而后面那间只是储藏室。没有洗手间，也没有吃的喝的。"
    scene blank with Dissolve(1)
    scene c003_s003_008 with Dissolve(1)
    l "好，我觉得可以走了。还有多远？"
    j "大概走了一半。差不多吧。只要贴着店面走应该没事。"
    k "你在外面看到什么了吗？我可没在看。"
    j "没有。什么都没有。一路干净。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_22_1121", transition=Dissolve(1.0))()
    pause
    $ Hide("june_22_1121", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c003_s003_009 with Dissolve(2)
    j "到了。我要三份二号超值套餐，堂食，谢谢。"
    k "我看是自助的。*咯咯笑* 劳拉？"
    l "我没事。呃，也不能说没事。但还能撑。让我坐一下。"
    scene c003_s003_010 with Dissolve(0.25)
    j "好，既然到了……"
    k "我去厨房弄点吃的。喝的？劳拉？"
    scene c003_s003_011 with Dissolve(0.25)
    l "要是不介意的话。我保证我能派上点用场。给我一点时间恢复一下。"
    k "当然，当然。不急。"
    scene c003_s003_012 with Dissolve(0.5)
    j "对了，劳拉，你要愿意放个哨那就太好了。"
    l "顺便确认外面没有东西在晃？"
    scene c003_s003_013 with Dissolve(0.25)
    j "差不多是这个意思。我把包放在这儿。手电筒我带着。"
    l "你现在就走？"
    scene c003_s003_014 with Dissolve(0.25)
    j "我觉得该趁现在、趁我还有继续走的劲头时去做。趁热打铁嘛。要是能进去、摸清我们有哪些选择，我就回来，拿点东西吃，然后再做决定。我保证不会太久。"
    l "我很讨厌这样——万一出了事，你连联系我们的办法都没有。"
    scene c003_s003_015 with Dissolve(0.25)
    j "正因如此我才打算小心行事、确保安全。你们两个互相照应，好吗？"
    l "会的。小心。拜托了。"
    scene c003_s003_034 with Dissolve(0.5)
    "{color=#66ff33}我最讨厌自己这样无能为力。我应该做点什么帮上忙的。我只是……{/color}"
    "{color=#66ff33}这事快把我逼疯了。{/color}"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c003_s003_020 with Dissolve(2)
    play music insidedark fadein 2.0
    "好了，前门是那种旋转门式的设计。对挡雾来说可不太行，对挡人也一样。大堂算不上密闭，也不算防得住闯入者。我猜他们本来是可以把它锁起来的，但我越来越觉得这地方也被弃置了。开始有点「城市探险」的味道了。"
    scene c003_s003_021 with Dissolve(0.25)
    "大部分灯都关着。也许值夜班的保安没来上班。或者来了，然后说自己给的工资不够。我倒觉得电还没断。前台旁边还立着一块牌子，写着「健身中心仍在营业」，这挺让人安心的。"
    scene c003_s003_022 with Dissolve(0.25)
    "好，电梯在这儿。到底还有电。不错。这意味着这地方——虽然空着——可能对我们还有用。我上楼看看。如果上得去的话。"
    scene blank with Dissolve(2)
    scene c003_s003_016 with Dissolve(2)
    k "午饭好了。或者说早饭。现在太早了，应该还不到午饭的点。"
    l "不管叫什么，饭就是饭。谢谢你。"
    scene c003_s003_017 with Dissolve(0.25)
    k "你有没有……"
    l "好些了。还是累，还在喘。我以前从不抽烟，但我现在怀疑，如果我这辈子都是个老烟枪，会不会就是这种感觉。"
    scene c003_s003_018 with Dissolve(0.25)
    k "我猜他刚到这儿就出去了吧？我就觉得他可能会。"
    l "对。他说想四处看看，然后我们再商量。"
    scene c003_s003_019 with Dissolve(0.25)
    k "我把他的饭放到保温灯下面吧。这样就不会凉。"
    scene c003_s003_035 with Dissolve(0.5)
    "{color=#66ff33}[player_name]在外面到处走，我们却在这儿吃饭，这感觉糟透了。可我现在也不知道还能怎么办。我们只能等他回来吃上热饭，然后指望他带好消息回来。{/color}"
    "{color=#66ff33}我们现在太需要好消息了。{/color}"
    scene blank with Dissolve(2)
    scene c003_s003_023 with Dissolve(2)
    "办公室。就像劳拉说的。这里以前是一家保险公司的呼叫中心。"
    scene c003_s003_024 with Dissolve(0.25)
    "唔嗯。地方还留着一些固定设施，但看起来基本都被搬空了。"
    "空气似乎还不错。就是有点陈腐。他们关掉之后大概一直没开空调，也就是说雾不是从这条路进来的。这里眼下可能真是个不错的落脚点。不过不是长久之计。"
    scene c003_s003_025 with Dissolve(0.25)
    "我看到的只有几套沙发，和后面那边一个小茶水间。不是长久之计。"
    "不过说真的，我有种感觉，我们迟早得认真考虑怎么他妈离开这个镇子。现在嘛，我们只是需要搬到离食物更近、让他们觉得更安全的地方。"
    scene c003_s003_026 with Dissolve(0.25)
    "说到这个，我们可以把楼梯的门堵上。电梯也是？我想我能想出办法把它们停掉。要是我们在这儿躲几天，顺便考虑下一步怎么办。"
    scene blank with Dissolve(2)
    scene c003_s003_036 with Dissolve(2)
    "{color=#ffcccc}真不敢相信劳拉去上厕所了。我猜她是真的憋不住了。她开始发痒。至少她进的是男厕。{/color}"
    "{color=#ffcccc}可我还是不行。只是知道那具尸体就在里面，就已经让我毛骨悚然了。不止如此。我吃饭只是因为饿得没法不吃。{/color}"
    scene c003_s003_037 with Dissolve(0.25)
    if k_friend >= 3:
        "{color=#ffcccc}我很担心。为[player_name]担心。为我们担心。他就这么一个人出去了。希望他很快回来。希望他平安。到这个份上，要是出了事，没有他我们可怎么办？{/color}"
    else:
        "{color=#ffcccc}我……很害怕。非常害怕。而且理由充分。没有[player_name]在，我……我会怎么办？是他，还有劳拉。不过，有[player_name]在身边，确实让我觉得……好一点点。{/color}"
        "{color=#ffcccc}我最讨厌自己这么脆弱。如果只有我一个人，我肯定完蛋。{/color}"
    play sound doorclose
    scene c003_s003_038 with Dissolve(0.25)
    l "好，我得跟[player_name]好好谈谈为什么男厕所总是那么脏。"
    scene c003_s003_039 with Dissolve(0.25)
    k "你有没有……"
    l "好多了。谢谢你关心。外面怎么样？有什么动静吗？"
    scene c003_s003_040 with Dissolve(0.25)
    k "目前没有。"
    l "唔嗯……好吧，他肯定已经进去了，正在仔仔细细打量这个地方。"
    scene c003_s003_041 with Dissolve(0.25)
    k "对。是我多心，还是那具……尸体今天味道更重了？"
    l "不好说。按理说应该会。但我确实感觉它臭了不止一点。"
    scene c003_s003_042 with Dissolve(0.25)
    k "也可能是我心理作用。既然知道它在那儿，我就{i}没法{/i}不去想。这让我连饿都饿不起来。我们能做点什么吗？"
    l "[player_name]确实提过也许该把尸体挪走，但我觉得那是个坏主意。有很多理由。"
    k "哦？好吧。"
    scene c003_s003_043 with Dissolve(0.25)
    l "也许我能拿几条毛巾塞在门底下，把缝封得严一点。做不到密不透风，但应该能有点用吧。我想。我也不知道。我又不是处理尸体的专家。"
    k "也许我们不用再来这儿太多次了。"
    l "得看我们要待多久。"
    scene c003_s003_044 with Dissolve(0.25)
    k "你觉得我们得自己想办法离开吗？"
    l "有可能。不过，在花力气去试之前，我想先知道这事到底有多普遍。"
    k "我……我明白。"
    scene blank with Dissolve(2)
    scene c003_s003_030 with Dissolve(2)
    "好吧。五层长得都差不多的空办公室。全是空的。推开一扇扇门，尽是空荡荡的房间。那块写着「仍在营业」的健身中心招牌，据说就在这边。"
    scene blank with Dissolve(2)
    scene c003_s003_027 with Dissolve(2)
    "到了。要不是在这儿上过早班或者办过会员，估计不太好找。看看这健身中心给我们准备了什么。"
    scene c003_s003_028 with Dissolve(0.5)
    "哦，哇。这地方挺不错。如果我们想分散注意力，或者想练块头，这里正合适。"
    scene c003_s003_029 with Dissolve(0.25)
    "而且从这儿看巷子视野不错。我想我能看见{i}汉堡店{/i}。勉强能见。隔着雾的话。"
    "既然有地方能锻炼，我在想……"
    scene blank with Dissolve(2)
    scene c003_s003_032 with Dissolve(2)
    "如果标牌没骗人的话，更衣室就在里面。希望它能给我们带来点惊喜。"
    scene c003_s003_031 with Dissolve(0.5)
    "这里有储物柜。得看看能不能弄到总钥匙，看看里面有没有值得搜刮的东西——前提是这地方还对外开放。不过它大概不会像一年前那样有人来健身了。"
    scene c003_s003_033 with Dissolve(0.25)
    "没错。淋浴间。正合我意。{a=https://www.quora.com/What-is-the-etymology-of-the-term-fuckin-A-as-far-as-it-means-I-agree-or-Damn-right}我他妈可太需要了{/a}。这是我一直拼命想要的东西。我们所有人都需要。要是设施跟设计意图一样正常运作，那可真是好消息。只希望这水还没被用到让我们得担心军团病。"
    "我先打开水龙头，确认能出水再说。"
    play ambient shower
    scene c003_s003_032 with Dissolve(0.25)
    "哎，这就行。而且已经是热水了。太棒了。至少好运眷顾了一小会儿。"
    stop ambient
    "现在去找灯的开关。可能在经理办公室那边。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_22_203", transition=Dissolve(1.0))()
    pause
    $ Hide("june_22_203", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday fadein 2.0
    scene c003_s004_001 with Dissolve(2)
    l "天哪，我最讨厌这样干等着，什么都不知道。我们只能相信[player_name]没事。"
    k "对。你觉得……"
    scene c003_s004_002 with Dissolve(0.25)
    l "不。他够聪明，不会让自己陷进麻烦。要是觉得不对劲，他也能退出来。杀我的只是等待。"
    scene c003_s004_003 with Dissolve(0.25)
    l "我也讨厌自己对这一切这么悲观。感觉我们被迫承受的一切，件件都是为了磨掉人的耐心。我们太习惯想做什么就做什么了，所以困在这儿干等好消息，简直糟透了。"
    k "我算不上喜欢这样。不过我明白你的意思。"
    scene c003_s004_004 with Dissolve(0.5)
    "{color=#ffcccc}外面有东西在动。我看见了。看见什么东西在动。{/color}"
    k "劳拉。"
    scene c003_s004_005 with Dissolve(0.25)
    l "什么？哦。是不是……"
    k "不知道。"
    scene c003_s004_006 with Dissolve(0.25)
    "{color=#ffcccc}要是不是呢？我们躲起来？还是跑？{/color}"
    l "哦，谢天谢地，是[player_name]。"
    scene c003_s004_007 with Dissolve(0.25)
    k "我、我去开门。你待着别动。"
    "{color=#ffcccc}离他带进来的那股味儿远点。{/color}"
    scene c003_s004_008 with Dissolve(1)
    l "怎么样？你走了这么久，我只能假设你顺利进去了。"
    k "我带了些吃的喝的。你要来点吗？"
    j "哦，那太好了。我先脱下来透透气。"
    scene c003_s004_009 with Dissolve(0.25)
    k "马上回来。"
    scene c003_s004_010 with Dissolve(0.25)
    j "还有，劳拉，是的，我进去了。直接走进去的。"
    play sound zipper
    scene c003_s004_011 with Dissolve(0.5)
    l "里面怎么样？抱歉这么催你。只是想到我们大老远赶来，却得在这儿耗着，等洗手间里那具尸体烂掉，我就有点坐立不安。"
    scene c003_s004_012 with Dissolve(0.25)
    j "我懂。现在这情况不怎么样，我们所有人都压力很大。"
    scene c003_s004_013 with Dissolve(0.25)
    k "给。只能把汉堡放到保温灯下面了。"
    menu:
        "无所谓。我现在尝不出任何味道。\n[rrd](卡莉 焦虑 +1)\n[rrd](卡莉 好感 -1)":
            $ k_anxiety +=1
            $ k_friend -=1
            j "无所谓。我现在尝不出任何味道。我想雾里待久了，它会毁掉你的嗅觉吧。"
        "肯定很好吃。\n[rgr](卡莉 好感 +1)":
            $ k_friend +=1
            j "肯定很好吃。谢谢。"
    scene c003_s004_014 with Dissolve(0.5)
    l "那，说说这栋楼？"
    j "大堂不行。太暴露了。那些旋转玻璃门也完全挡不住雾。好消息是，只要我们上到二楼就没问题了。嗯，好到能期待的程度。那里还留着些家具，所以暂时可以在那边待着。"
    scene c003_s004_015 with Dissolve(0.25)
    j "我没来得及到处都看，有些房间还锁着，不过情况正在好转。我想只要找到电梯钥匙——也许留在保安室里——我们就能在二楼安顿一阵子。"
    l "怎么做？"
    j "我们坐电梯上去，把它停掉，然后把楼梯的门堵上，就能在那儿窝一阵子。这样一来，不管外面那个东西或那帮人是不是威胁，我们也该不会被看见。就算他们摸过来，也很难靠近我们。"
    scene c003_s004_016 with Dissolve(0.25)
    j "至少我们在那儿暴露的程度会低得多。还有一两个惊喜——是好的那种——我很想给你们看看。"
    l "哦？这么说，你觉得它还不错？"
    scene c003_s004_017 with Dissolve(0.25)
    j "好到值得我把你们俩叫回来。这必须是大家一起做的决定。我们都得认可才行。不如我带你们四处看看，你们再决定能不能接受。"
    k "那到那儿安全吗？"
    j "我觉得安全。我没看到什么。而且就像我说的，除了前面的大堂，我们不会接触到雾。让我收拾一下我们就出发。"
    scene blank with Dissolve(2)
    scene c003_s005_001 with Dissolve(2)
    "狼吞虎咽吃完饭（比我预想的更管用）后，我们带上装备出发。我把「能洗个澡」这件事先藏着，主要是想让它成为一个惊喜。另外，我内心有一部分不希望这件事影响他们的判断。"
    "洗个澡的诱惑可能会让他们对我可能忽略的危险更不上心。我讨厌这么想，但我需要所有人都能接受这个新地点。"
    scene blank with Dissolve(2)
    scene c003_s005_002 with Dissolve(2)
    l "这边好多了。我对刚才那边的情况实在没什么好感。虽然你提醒过我们，但那看着实在不像是个能待的地方。"
    j "对。我之前来过这边，上楼之后会好很多。待在一楼的话，恐怕我们得全副武装才能行动。电梯就在上面。"
    k "那灯呢？"
    scene c003_s005_003 with Dissolve(0.25)
    j "不知道。看起来这儿只留了最少的人手。保安。也许还有前台的人。不过对我们来说算走运——既然健身中心看起来还在使用，他们走的时候没把这里彻底断掉。"
    l "你的惊喜就是这个？健身中心？我看到牌子了。"
    j "耐心点，劳拉。耐心。*轻笑*"
    scene c003_s005_004 with Dissolve(0.5)
    "我先把背包放在电梯里，等我们决定是否留下再说。它比我早上出发时预计的重多了。"
    k "那这电梯能用吗？我的车抛锚了，你的车也抛锚了，然后……我心里就没底了。"
    j "我刚才刚用过。"
    scene c003_s005_005 with Dissolve(0.25)
    l "真要不行，还有楼梯。"
    k "对。我们能摘口罩了吗？"
    scene c003_s005_006 with Dissolve(0.25)
    j "哦，对，当然。我都忘了。"
    l "谢天谢地。我不是不领情，可我鼻梁上都要被勒出印子了。"
    k "说实话，光是闻不到自己的口气我就很高兴了。"
    scene blank with Dissolve(2)
    scene c003_s005_007 with Dissolve(2)
    j "到了。就像我说的：一片被遗弃的办公区。有几套沙发和长椅。想一个人待着的话，也有几间办公室。"
    "我敢肯定卡莉很领情。"
    scene c003_s005_008 with Dissolve(0.25)
    j "有几间办公室没锁。另一些锁着，尤其是楼上。还有，我看到楼上有个小休息区。有微波炉和迷你冰箱。"
    scene c003_s005_009
    l "你觉得我们能进那些房间吗？锁着的那些？以防万一吧。我只是想知道这地方到底有些什么。"
    j "要是能找到钥匙，当然可以。最坏的情况，也许我直接砸进去。这些门看起来都不算结实。"
    scene c003_s005_010 with Dissolve(0.25)
    l "好。虽然不是酒店，但眼下似乎能凑合。可我一点也不想在这儿待超过几天。"
    j "至少能给我们时间想想下一步。卡莉？"
    scene c003_s005_011 with Dissolve(0.25)
    k "眼下可以。就像你说的。"
    scene c003_s005_012 with Dissolve(0.25)
    l "那，这个健身中心？"
    j "跟我来。"
    scene blank with Dissolve(2)
    scene c003_s005_017 with Dissolve(2)
    j "看。而且看起来维护得相当好。"
    scene c003_s005_018 with Dissolve(0.25)
    l "哇，你真没骗我。考虑到那些办公室空成那样，我本以为这里会……更糟。"
    scene c003_s005_019 with Dissolve(0.25)
    k "我们能看到下面。看不太清。不过……"
    l "对。天气要是好点，我们也许就能看清下面的巷子。我希望我们能进五楼或六楼那些朝东的办公室。"
    j "把周边城区尽收眼底？"
    scene c003_s005_020
    l "正是。那你的惊喜呢？"
    j "靠，你真没耐心。跟我来。就在隔壁。卡莉？"
    k "来了。"
    scene blank with Dissolve(2)
    scene c003_s005_021 with Dissolve(2)
    j "{size=30}来，我先把灯打开。{/size}"
    scene c003_s005_022 with flash
    j "我们到了。"
    l "更衣室？我想这说得通。要是运气好，也许能在某个柜子里翻到换洗衣服。前提是这健身中心之前还常有人用。"
    scene c003_s005_023 with Dissolve(0.25)
    k "别人的衣服？*呻吟*"
    scene c003_s005_024 with Dissolve(0.25)
    j "乞讨的人没资格挑。再说……你知道的……{b}淋浴间{/b}。就在下面。"
    l "什么？哦，靠，我完全没……"
    scene c003_s005_025 with Dissolve(0.5)
    l "哦，谢天谢地。我从来没这么需要洗过澡。完全是脑子没转过弯来。睡眠不足，人都有点发懵。"
    j "我就知道。而且我们都该洗个澡，劳拉。我知道我该。"
    "今天在外面待太久了，好几处皮肤都在发烫。"
    scene c003_s005_026 with Dissolve(0.25)
    k "我们现在能放心做这个吗？我、我……我真的好想洗个澡，好像一周都没这么干净过了。"
    l "*叹气* 卡莉说得对。我们最好先确认这栋楼里没有意外，再做这个。"
    "谨慎一点大概最好。这里是陌生地盘，我们毕竟是大摇大摆进来的。"
    j "好，我们把搜索做完，也许我再把楼梯间的门堵上，然后就回来洗干净。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c003_s005_013 with Dissolve(2)
    play music nightmain fadein 2.0
    "接下来一个小时左右（差不多吧），我们把能去的区域彻底搜了一遍。好几层空的隔间工位，两旁是曾经坐着主管的办公室。还有几扇门锁着，包括六楼一间转角的办公室。"
    scene blank with Dissolve(2)
    scene c003_s005_015 with Dissolve(2)
    "我确实觉得，搬到二楼让卡莉（也许还有劳拉，虽然她藏得很好）觉得至少安全了一点。或者，也可能是因为我们在外面看来不像在老办公室时那么显眼。"
    scene blank with Dissolve(2)
    scene c003_s005_016 with Dissolve(2)
    "按计划，我搬了几件家具抵在楼梯出口上，只留下电梯作为从一楼进入的唯一通道。钥匙我迟早得找到。"
    "还得弄件武器，哪怕只是一条桌腿或者灭火器。"
    scene blank with Dissolve(2)
    scene c003_s005_014 with Dissolve(2)
    "当然，我们还得决定接下来怎么睡。卡莉看中了其中一间办公室。我和劳拉呢？"
    j "这比办公室那边可强多了。"
    l "我现在能有一张床睡就谢天谢地了。不过这样也行。"
    scene blank with Dissolve(2)
    scene c003_s006_001 with Dissolve(2)
    "尽我们所能把这里安顿好之后，我们回去享受了早就该来的一次淋浴。还有很多事我之后可以做、也会去做，但我觉得我们都迫切需要一点简单又久违的便利。"
    "我确实在想，痛痛快快洗一次能不能对大家都有帮助。劳拉在咳嗽。卡莉——她拼命想瞒着——一直在挠发痒的皮肤。我呢？我又累又浑身上下哪都难受。我在外面待得太久了。"
    scene c003_s006_002 with Dissolve(0.25)
    l "那么，不是想冒犯，但你们打算怎么办？我跟你们俩都还没熟到可以随便脱衣服的程度。"
    k "哦？呃，对。"
    scene c003_s006_003 with Dissolve(0.25)
    j "你们先去。我去办公室看看。找找储物柜的钥匙。"
    l "你觉得能有收获吗？"
    scene c003_s006_004 with Dissolve(0.25)
    j "试试总没坏处，而且我确实喜欢假装自己是个绅士。虽然是个臭烘烘的绅士。"
    l "*咯咯笑* 好，谢谢。我们尽量不用光热水。"
    scene c003_s006_005 with Dissolve(0.25)
    j "那我就承情了。"
    k "*咯咯笑*"
    scene c003_s006_006 with Dissolve(0.5)
    k "这儿放着几条毛巾。我想我们要是找得再仔细点，能找到更多。"
    l "我注意到了。不然我们就只能晾着干。要不你在那边脱，我在这边脱？成交？至少表面上还有个隐私的样子。"
    play sound zipper
    scene c003_s006_007 with Dissolve(0.25)
    k "行，这样就行。*咯咯笑*"
    l "我敢肯定，这不在你这周预想过会发生的事的清单上。反正它不在我的宾果卡上。"
    scene c003_s006_008 with Dissolve(0.25)
    k "我、我没事。我以前进过更衣室。高中参加校队的时候。"
    l "我已经很久没那么久了，但我记得那种场面。你再怎么想不看，都很难不去看——二三十个女生抢着冲进来，在赶去下一节课前的十分钟里挤着洗澡。"
    scene c003_s006_009 with Dissolve(0.25)
    k "我高中还跑过越野。所以运动员女孩的屁股和胸部，我见得多了。"
    scene c003_s006_010 with Dissolve(0.25)
    l "好，我保证尽量不看。"
    scene c003_s006_011 with Dissolve(0.25)
    k "我也是。*咯咯笑*"
    scene c003_s006_012 with Dissolve(1)
    l "我已经用浴巾裹好了，你现在可以看了。我来看看水压怎么样。"
    k "我、我马上过去。"
    scene c003_s006_013 with Dissolve(0.25)
    play ambient shower fadein 2.0
    "{color=#ffcccc}这一切真是……我很高兴[player_name]找到了这个地方，但这完全不是……我想也可能更糟。至少劳拉在这件事上表现得很坦然。她也明白现在不是时候。{/color}"
    scene c003_s006_014 with Dissolve(0.25)
    $ l_anxiety -= 1
    l "啊啊呜~~~ 好了。舒服。卡莉？"
    k "来了。水热吗？"
    scene c003_s006_015 with Dissolve(0.5)
    l "热。哦，靠，太舒服了。我太需要这个了。这说不定真能让最近这几天没那么难受。"
    k "好，我……"
    scene c003_s006_016 with Dissolve(0.25)
    $ k_anxiety -= 1
    k "*呻吟* 哦，天哪，你真没骗我。我……我可以就这么泡上一阵子。"
    l "别一整天。我们还得让[player_name]也轮一次。"
    scene c003_s006_017 with Dissolve(0.5)
    l "所以，你高中跑过越野？"
    k "呃，对。我也不算什么厉害角色。主要是团队项目，我爸妈希望我做点体育方面的事，好让我的大学申请看起来更全面一点。要不然就是练体操。你呢？"
    scene c003_s006_018 with Dissolve(0.25)
    l "真没有。高中没跑过。不过我那时候也不操心上什么大学，所以对我不算什么大事。我算是有健身卡，可我工作太忙了，纯属浪费钱。你知道，我们这些老女人得靠锻炼才不发福。"
    scene c003_s006_019 with Dissolve(0.25)
    k "你又不老。"
    l "有些日子我觉得自己就是老了。"
    scene blank with Dissolve(1)
    scene c003_s006_020 with Dissolve(1)
    "好，找到了一串钥匙。看起来能开储物柜。该看看有没有人留下什么东西了。比如那些以前用这健身中心、场所关闭时没把东西清走的前员工。"
    scene c003_s006_021 with Dissolve(0.5)
    l "{size=32}啊啊啊呜~~~这大概是有史以来最爽的感觉。{/size}"
    "听起来她们用得很享受。不错。我还担心会出什么岔子。比如水是冷的。或者更糟。"
    scene blank with Dissolve(1)
    scene c003_s006_022 with Dissolve(1)
    "忙活半天，就找到了两块除臭膏、几套健身服和三罐能量饮料。不过我还是凑齐了足够让我们换掉身上衣服的东西。汗臭加上困在布料里的雾味，我们都需要暂时摆脱它们。"
    "或者说，是我需要。"
    scene c003_s006_023 with Dissolve(0.5)
    "听起来她们还在洗。我该去告诉她们这个消息。"
    scene c003_s006_024 with Dissolve(0.5)
    "哦，这边左边还有几个淋浴间。我可以直接冲进去快速冲一下，不用等她们洗完。只要跟她们说一声，免得有什么误会。"
    menu:
        "你直接用淋浴间吧。\n[rrd](卡莉 焦虑 +1)\n[rgr](卡莉\劳拉 欲望 +1)":
            scene c003_s006_025 with Dissolve(0.5)
            $ ch3_takeshower = "yes"
            $ k_anxiety +=1
            j "嘿，是我。我正站在淋浴间外面。就是想告诉你们，我翻出了些衣服。基本上都是些运动服。不过比我们身上这套干净，而且没沾上外面那股味儿。"
            l "谢谢，[player_name]。我们很领情。"
            k "对，谢谢。"
            scene c003_s006_026 with Dissolve(0.25)
            j "我给你们放好了。另一边还有几个淋浴间。我冲一下，很快就好。我保证不久。也不许偷看。"
            k "好、好的。"
            l "当然。慢慢来。好好享受。我就很享受。"
            scene c003_s006_048 with Dissolve(1)
            "听起来她们俩都不太反感这个主意。当然，就算卡莉真的讨厌，她也不会让我知道。"
            scene c003_s006_049 with Dissolve(0.5)
            "而劳拉要是气炸了，一定会让我听见。不过只要我们互相看不见，就没问题。"
            scene c003_s006_027 with Dissolve(1)
            "哦，我操，太爽了。我比自己想象的更需要这个。我可能得慢慢来，好好享受一下。"
            scene c003_s006_028 with Dissolve(0.25)
            if l_desire >= 2 or k_desire >=2:
                "嗯，不是真的{b}享受{/b}这个。我不太可能一边冲澡一边来一发，对吧？我承认空气里确实有点微妙，而且我看到的皮肤比我想象的要多得多。不过，现在不是时候。"
            else:
                "嗯，不是真的{b}享受{/b}这个。我不太可能一边冲澡一边来一发，对吧？算了，现在不是时候。"
            "既然来了，就好好利用。每天都洗。也许再配合健身中心锻炼来打发时间。"
        "给她们留点隐私。":
            scene c003_s006_025 with Dissolve(0.5)
            "最好保持冷静。就目前这样我们已经够克制了。我敢肯定她们俩都不想跟我这样近距离待这么久。"
            j "嘿，是我。我正站在淋浴间外面。就是想告诉你们，我翻出了些衣服。基本上都是些运动服。不过比我们身上这套干净，而且没沾上外面那股味儿。"
            l "谢谢，[player_name]。我们很领情。"
            k "对，谢谢。"
            scene c003_s006_026 with Dissolve(0.25)
            j "我给你们放好了。我先出去，让你们俩在这儿随便用着，直到洗完。"
            l "我们保证不会太久。"
            j "我在健身中心等着。"
    scene blank with Dissolve(1)
    scene c003_s006_029 with Dissolve(1)
    k "我洗完了。我去看看我们有什么{i}美妙{/i}的衣服可以选。"
    l "给我一分钟。我想确保每个地方都洗到了。我再也不想有那种脏兮兮的感觉了。"
    scene c003_s006_030 with Dissolve(0.25)
    k "*咯咯笑* 我懂那种感觉。"
    if ch3_takeshower == "yes":
        scene c003_s006_032 with Dissolve(0.5)
        "{color=#ffcccc}哦？[player_name]就在外面。我想我们是用单间淋浴。他就在那儿毫不遮掩地站着。我敢说他今天在外面待了一整天，皮肤肯定火辣辣地疼。我大概不该看。{/color}"
        if k_desire >= 2:
            scene c003_s006_033 with Dissolve(0.25)
            $ k_desire += 1
            "{color=#ffcccc}啊，糟了。我……哦，哇。呃……那是他的鸡巴。我、我该……我该走了。{/color}"
    else:
        scene c003_s006_031 with Dissolve(0.5)
        "{color=#ffcccc}哦？那边还有几个淋浴间。我想[player_name]要是想去，本来可以去那边的。我敢说他今天在外面待了一整天，皮肤肯定火辣辣地疼。{/color}"
        "{color=#ffcccc}他给我们留出空间，我确实挺感激的。这样已经够让人不自在了。可他在外面待那么久，肯定也难受得很。{/color}"
    scene c003_s006_034 with Dissolve(1)
    k "唔嗯……"
    if ch3_takeshower == "no":
        stop ambient fadeout 2.0
    "{color=#ffcccc}看来[player_name]找到了别人的运动服。看起来也闻起来都挺干净。我不太乐意这样，可我现在没法再穿回自己的衣服。除非万不得已。我感觉那布料黏在皮肤上。就算想穿我都穿不上。{/color}"
    scene c003_s006_035 with Dissolve(0.25)
    l "好，我刚才在上面都开始打蔫了。不过那倒是让我的背舒服了些。"
    scene c003_s006_036 with Dissolve(0.25)
    l "嗯？这比我想象的好多了。"
    k "那套衣服？"
    scene c003_s006_037 with Dissolve(0.25)
    l "对。可能糟得多。再说，他还给我们留了些除臭剂。"
    k "可惜没有润肤乳。我需要花点时间修护一下皮肤。"
    scene c003_s006_038 with Dissolve(0.25)
    l "*咯咯笑* 有条件的时候，是该做点自我护理了。"
    k "我完全同意。你、你的咳嗽怎么样了？洗澡有用吗？"
    scene c003_s006_039 with Dissolve(0.25)
    l "我觉得有。它有点像个雾化器。而且我们这次在外面也没待很久。"
    "{color=#66ff33}伤害已经造成了，我怕。{/color}"
    scene c003_s006_040 with Dissolve(0.25)
    k "那，我们原来那些衣服怎么办？出门的时候还得穿，可我不想就这么……一直拎着。"
    scene c003_s006_041 with Dissolve(0.25)
    l "也许摊开晾着。让这里潮湿的空气吹一吹。要是能找到些空气清新剂或者喷雾除臭剂，我就直接喷一遍。我怀疑「洗衣服」现在还不在我们可行选项的清单上。"
    scene c003_s006_042 with Dissolve(0.25)
    k "我想现在再去那家服装店再拿点东西已经太晚了。"
    l "考虑到刚才那样，我觉得回头去不是个好主意。"
    if ch3_takeshower == "yes":
        stop ambient fadeout 2.0
        scene c003_s006_043 with Dissolve(0.5)
        "{color=#66ff33}嗯？淋浴的水声终于停了。[player_name]应该洗完了。我们就这么在同一间屋子里，各自光着程度不一，感觉有点怪。嗯，不算「怪」。是别的什么词吧。我想这就是那种会逼我们去面对平时可能让人不自在的东西的情况。{/color}"
        scene c003_s006_044 with Dissolve(0.25)
        j "嘿，你们都穿好了吗？我这边好了。你们要是还没好，我可以先在腰上裹条毛巾等着。"
        l "卡莉？"
        k "好、好了，我没问题。正在试着把它弄合身。"
        scene c003_s006_045 with Dissolve(0.25)
        $ l_desire += 1
        l "你可以进来了。我们先撤，把地方留给你。"
        "{color=#66ff33}哦，哇，[player_name]身材真好，那条浴巾几乎没留下多少想象空间。{/color}"
        scene c003_s006_046 with Dissolve(0.5)
        $ k_desire += 1
        j "好。那么，衣服怎么样？希望别太惨。选项有限，你们也知道我平时是怎么穿的。"
        l "凑合吧。考虑到楼里这么暖和，你完全可能倒霉得多。"
        k "有点松——大概是给体型更大的人穿的——不过眼下凑合了。"
        scene c003_s006_047 with Dissolve(0.25)
        l "好了，我们走吧。我们会在健身中心等你。"
        j "好，我不会太久。"
    else:
        scene blank with Dissolve(2)
        scene c003_s007_001 with Dissolve(2)
        "在这儿看画慢慢干真够无聊的。我想看看下面巷子里有没有什么，可这雾实在太浓了。就算真看到了又怎样？"
        "我是说，那至少能证实卡莉和劳拉昨晚跟我说的。我不是不信她们，只是想亲眼看看。现在我手上只有「看起来像个怪物」或者「严重烧伤的人」这种说法，帮不上什么忙。"
        scene c003_s007_002 with Dissolve(0.25)
        "我大概只是想知道我们面对的到底是什么。不过也许我们运气好，把那东西留在了旧办公室。"
        "等我们花一天左右适应这个地方，就得谈谈长期打算了。我不想把「救援不会来」这件事直接说出口，但我开始觉得这就是事实了。而且，至少劳拉好像也是这么想的。"
        scene c003_s007_003 with Dissolve(0.5)
        "跑步机上方有台电视。不知道我们能不能收到节目。或者会跟网络和手机信号一样？要是能找到遥控器，也许就能弄清楚。要是能看到紧急广播或者关于外面情况的新闻报道就好了。"
        scene c003_s007_004 with Dissolve(0.5)
        l "嘿，我们洗好了。淋浴间归你了。"
        j "啊，好。衣服怎么样？希望别太惨。"
        "在我看来还不错，不过这话我不会说出口。而且也许我该尽量少四处乱看。"
        scene c003_s007_005 with Dissolve(0.25)
        l "凑合吧。考虑到这里这么暖和，你完全可能倒霉得多。"
        k "有点松——大概是给体型更大的人穿的——不过这样也够了。"
        scene c003_s007_006 with Dissolve(0.25)
        l "我们把衣服留在更衣室了。也许我们运气好，淋浴的蒸汽能把它们「吹干」一点。反正再次出门之前用不着。"
        j "听起来不错。容我先去冲一下，我真的很需要。"
        scene c003_s007_007 with Dissolve(0.25)
        l "哦，那里面还有除臭剂。你需要的话可以用。"
        j "我大概需要。谢谢。"
        scene blank with Dissolve(2)
        scene c003_s007_008 with Dissolve(2)
        "至少她们没因为我给她们弄的衣服大惊小怪。我又没{b}故意{/b}去找紧身的。"
        scene c003_s007_009 with Dissolve(0.25)
        "不过，看她们穿非工作服，确实解答了我心里的几个疑问。我不否认，我确实想过。"
        scene c003_s007_010 with Dissolve(0.25)
        "眼下，且看我能不能好好享受这一周以来第一次淋浴吧？"
        scene c003_s006_027 with Dissolve(0.5)
        play ambient shower fadein 2.0
        "哦，我操，太爽了。我比自己想象的更需要这个。我可能得慢慢来，好好享受一下。"
        scene c003_s006_028 with Dissolve(0.25)
        if l_desire >= 2 or k_desire >2:
            "嗯，不是真的{b}享受{/b}这个。我不太可能一边冲澡一边来一发，对吧？我承认空气里确实有点微妙，而且我看到的皮肤比我想象的要多得多。不过，现在不是时候。"
        else:
            "嗯，不是真的{b}享受{/b}这个。我不太可能一边冲澡一边来一发，对吧？算了，现在不是时候。"
        "既然来了，就好好利用。每天都洗。也许再配合健身中心锻炼来打发时间。"
        stop ambient fadeout 2.0
    scene blank with Dissolve(2)
    scene c003_s007_011 with Dissolve(2)
    l "你在下面看到什么了吗？"
    k "没、没有。而且天开始黑了，我现在肯定也看不出什么。"
    scene c003_s007_012 with Dissolve(0.25)
    l "我有点希望我们把那位「朋友」留在了后面。我想我们是用「暴露在外面被人往里看」，换来了「完全看不见周围任何东西」。"
    k "真有必要的话，我们可以去大堂。不、不过不是现在。我……累了，还不太想重新穿上那身衣服。"
    scene c003_s007_013 with Dissolve(0.25)
    l "我懂。唔……上面有台电视。"
    k "是啊。你觉得……？"
    l "不知道。也许能看，也许不能。试试也不亏。"
    scene c003_s007_014 with Dissolve(0.5)
    j "好，我洗完了、擦干了、也穿好衣服了。可能耳朵里进了点水，不过现在大概能装得像个干净人。至少闻起来好多了。"
    scene c003_s007_015 with Dissolve(0.25)
    l "这个得由我们来评判。*咯咯笑* 而且这身打扮真不错。"
    j "对，我本想说背心加篮球裤可不是我的常见造型，不过T恤配短裤大概算是平移。我漏掉什么了吗？"
    l "没有，没有。说实话，我们在这儿也看不远。但我确实觉得这里更安全。卡莉？"
    scene c003_s007_016 with Dissolve(0.25)
    k "呃，对。把那扇门堵上是个好主意。"
    j "这倒提醒我了，我得去四处翻翻。看能不能找到那些钥匙。"
    scene c003_s007_017 with Dissolve(0.25)
    k "哦，我不是在说那个……"
    j "没关系。我得去。"
    scene c003_s007_018 with Dissolve(0.25)
    l "对了，换个话题，你注意到上面那台电视了吗？"
    if ch3_takeshower == "yes":
        j "想追你的肥皂剧吗？*轻笑* 我之前没注意，不过这确实是个让人愉快的惊喜。"
        scene c003_s007_019 with Dissolve(0.25)
        k "怎么说？"
        j "要是我能找到那台电视的遥控器，我们就能看看能不能收到任何节目。本地新闻、州新闻、全国新闻。到这一步我不在乎是哪个。任何新闻都好。"
    else:
        j "我也想。要是我能找到那台电视的遥控器，我们就能看看能不能收到任何节目。本地新闻、州新闻、全国新闻。到这一步我不在乎是哪个。任何新闻都好。"
    scene c003_s007_020 with Dissolve(0.25)
    l "只要是外面来的任何消息，对吧？"
    j "没错。那么，眼下你们俩先去把我们的「住处」安顿好吧？我去看看能不能进那间楼宇经理的办公室。"
    k "我该去把我们的衣服拿回来。我受不了就这么把它们留在更衣室。"
    scene c003_s007_021 with Dissolve(0.25)
    l "等到早上再说吧。不会有人闯进来偷走它们的。"
    k "我……也是。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_22_548", transition=Dissolve(1.0))()
    pause
    $ Hide("june_22_548", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c003_s008_001 with Dissolve(2)
    play music nightmain2 fadein 2.0
    "我压根没想过自己还得回一趟一楼，在去洗澡换衣服之前先检查那些办公室里有没有必需品——比如钥匙。我早该想到的，毕竟不管是经理办公室还是保安室，都该在一楼大厅附近才对。"
    scene c003_s008_002 with Dissolve(0.25)
    "我大概是光顾着怎么进来了。而且说实话，在洗上那个澡之前，我的皮肤痒得厉害，很难清醒地思考。我知道我们该做什么，但在那之前实在很难集中注意力。"
    "幸好这儿空气还不算太差。我可不想为了四处乱翻，又得穿回那身出门的行头。不过我还是不该待太久。"
    scene c003_s008_003 with Dissolve(0.5)
    j "哇——哈——~~~ 瞧这个。"
    "一把消防斧？我还以为「火灾时击碎」的那种箱子是过去时代的遗物了呢。比如很多楼在升级灭火系统之后都得把它们拆掉。又或者，是怕哪个员工一时发疯，抄起斧子砍了老板。"
    scene blank with Dissolve(2)
    scene c003_s008_004 with Dissolve(2)
    "我用斧子砸开那扇门的时候，尽量没搞成{a=https://www.youtube.com/watch?v=WDpipB4yehk}《闪灵》式模仿{/a}。这可比找钥匙或者密码强多了。希望这扇门值得，因为我不想老这么干。"
    scene c003_s008_005 with Dissolve(0.25)
    "我们在抽屉和杂物里翻一翻，看看有没有值钱的东西。而且那杯咖啡到现在肯定难喝死了。"
    scene blank with Dissolve(1)
    scene c003_s008_006 with Dissolve(1)
    "看来我可能找到电梯钥匙了，这样就能把它们停掉，真正把我们自己锁在二楼。往后我还得找到整栋楼的总钥匙，才能试着打开四楼、五楼和六楼的那些办公室。"
    "眼下先回楼上看看姑娘们怎么样了。希望她们已经安顿下来准备过夜了。今天真是漫长的一天，我开始觉得累了。"
    scene blank with Dissolve(2)
    scene c003_s008_007 with Dissolve(2)
    "好，看起来这招奏效了。因为这些东西全都没配使用说明，我摸索了好一阵子。电梯在二楼，已经停用了，等我们需要时再说。"
    scene c003_s008_008 with Dissolve(0.25)
    "我最好还是告诉其他人一声，以防有人想去别的楼层。她们还能用旁边的楼梯上健身中心，只是下不到大厅而已。"
    scene c003_s008_009 with Dissolve(0.5)
    "哦，靠，劳拉已经躺下睡得死沉了。这也合理，毕竟我们昨晚几乎没睡，从这儿走过来也够累的。而且她还没从之前那次暴露里完全恢复。"
    "希望她能踏踏实实睡一觉，对她有好处。我有种感觉，我们三个都会需要好好休息。我们接下来怎么办、能去哪儿，肯定得好好商量。先让这个地方养养人，过几天再想出下一步去哪儿。"
    scene c003_s008_010 with Dissolve(0.5)
    "我把这把斧子放回原处——我可不想在黑暗里像什么连环杀手一样到处晃——然后去找找卡莉。她多半也已经睡下了。"
    scene c003_s008_011 with Dissolve(1)
    "唔，不在这边的办公室里。我早料到她会找个僻静的地方待着。我不信她走得太远，比如去了楼上。我在这一层转一圈找找她。当然，她有隐私的权利，只是我想知道她人在哪儿。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_22_822", transition=Dissolve(1.0))()
    pause
    $ Hide("june_22_822", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c003_s008_012 with Dissolve(2)
    "我知道她小小一只，这儿也还挺暗的，但我没想到找卡莉会这么费劲。她是走丢了吗？自己四处逛去了？我知道她是个成年人，可不知道她在哪儿，我还是担心。"
    "我没觉得自己会是那种高度警觉的人。可这一整套破事把我的状态全打乱了。我已经没法相信任何「正常情况」，所以我拼命想让所有人都待在我视线里。"
    scene c003_s008_013 with Dissolve(0.25)
    k "嘿，呃……"
    j "哦，嘿，卡莉。你在这儿啊。我刚回来，一直在找你和劳拉。呃，就是刚才回到楼上的时候。"
    scene c003_s008_014 with Dissolve(0.5)
    k "劳拉累了，躺下了。"
    j "对，我出电梯的时候看见她了。先跟你说一声，免你吓一跳。我找到了电梯的钥匙，已经把它停用了。就是想告诉你一声，看你是不是想四处转转。"
    scene c003_s008_015 with Dissolve(0.25)
    k "没、没关系。我刚才在把我们的衣服摊在那边的隔间桌面上。"
    j "哦，你去把衣服拿回来了？"
    scene c003_s008_016 with Dissolve(0.25)
    k "对呀~~~ 我、我就是没法把它们留在更衣室。它……"
    menu:
        "就是让你不自在？\n[rgr](卡莉 信任 +1)":
            $ k_trust += 1
            j "就是让你不自在？像是后脑勺里有个小疙瘩在提醒你，应该把它们放在手边，万一我们急着要换衣服？"
            scene c003_s008_018 with Dissolve(0.25)
            k "*叹气* 对。我知道这很傻，可是……"
            j "不傻。我们每个人都有一些必须做的小怪癖，才能撑过一天。有时我们需要确认所有文件都整整齐齐地摞成一叠。或者书要按颜色或大小分类。或者复印的份数必须是偶数。"
            scene c003_s008_019 with Dissolve(0.25)
            k "你懂。"
            j "我懂。我真的懂。"
        "别提了。":
            scene c003_s008_017 with Dissolve(0.25)
            "我以前想过，但没细想。可卡莉也许就是那种需要把某些事情安排妥当才能放松的人。而眼下这一切对她来说简直是地狱。"
            "最好把我的想法留在心里。今天对她们来说已经够多了。我不该让她尴尬。"
    j "那，趁现在你在这儿，你还好吗？这一切都太疯狂了，我也知道现在的情况并没有变好。而且我们今天几乎是急急忙忙赶过来的，除了「别再回旧办公室」之外什么都没顾上。算是临时起意的搬家日吧。"
    scene c003_s008_020 with Dissolve(0.25)
    k "已经算改善了。我这几天第一次洗上澡。而且这些衣服……虽然不是我的，但能穿上一件我希望是干净的东西，感觉真好。"
    j "比我们有的干净多了。抱歉，比能穿的还要「运动」一点。"
    scene c003_s008_021 with Dissolve(0.5)
    k "没关系。还有，谢谢你。为……"
    j "没什么。我不过是撬了几个柜子门而已。说真的，健身中心以前的使用率这么高，还挺让我意外的。不过以后肯定就没什么客人了。"
    scene c003_s008_022 with Dissolve(0.25)
    k "不，不。那个也是。总之，谢谢你让这一切没那么难熬。本来可能糟得多，而你……我很感激你当时在。你现在也在。抱歉。就是……"
    j "没关系。这不是世界上最好的处境，但我想我们至少不用落得更糟的伴。这一点我同意。"
    scene c003_s008_023 with Dissolve(0.25)
    k "不只是因为这个。我……我不傻。我知道我不是个大女孩。而且很多东西我都会怕，大多数人不会。因为我没有像你或者劳拉那样自保的力量。"
    scene c003_s008_024 with Dissolve(0.25)
    j "劳拉想揍谁就能揍谁。"
    if k_trust >= 2:
        k "我知道。所以这件事发生时你在我身边，至少让我安心了一点。我能安心睡觉，知道你在。我能相信不会出事。谢谢。"
    else:
        k "我知道。所以这件事发生时你在我身边，至少让我安心了一点。我能安心睡觉，知道你在。谢谢。"
    menu:
        "[gr]不客气。":
            j "不客气。我们是一条船上的。"
            scene c003_s008_025 with Dissolve(0.25)
            k "……"
        "不过你更希望安德鲁在这儿。\n[rrd](卡莉 焦虑 +1)\n[rrd](卡莉 欲望 -1)":
            $ k_anxiety +=1
            $ k_desire -=1
            j "说实话，你更希望安德鲁在这儿。"
            scene c003_s008_025 with Dissolve(0.25)
            k "我倒希望我们根本不用做这些。"
    scene c003_s008_026 with Dissolve(0.5)
    k "不过还有件事，我想……我……我不知道你离过婚。抱歉。我前几天无意中听见你和劳拉说话。"
    j "哦，我，呃……我在公司其实没怎么提过。我不想当那个在办公室里抖家丑的人。不过我也知道，这可能没让我显得多好相处。"
    scene c003_s008_027 with Dissolve(0.25)
    k "我倒真没注意。"
    j "哎。那我在公司大概算个混蛋了吧。或者根据我上一段感情的结果来看，一直都是。"
    scene c003_s008_028 with Dissolve(0.25)
    k "不不，你不是。我不是那个意思。你一直都很稳、很专业。或者，也可能只是我不太会看人。我在这方面挺笨的。"
    k "但我以前见过。我姑姑几年前离了婚，那件事把她毁得不轻。她和我妈花了很多时间聊这个，说它伤害她的方式，是她从没想过的那些。"
    scene c003_s008_029 with Dissolve(0.25)
    k "它扭曲了她看待自己的方式，让她觉得自己可能再也不会相信任何人了。或者就算信任，也不足以愿意跟对方做出承诺。我记得当时很难过，因为我觉得她会因此永远一个人。"
    j "对我来说这事还新鲜，所以我现在不会做任何那类决定。可我脑子里有很多问题得理清楚。看看我是不是有些地方本可以做得更好。"
    scene c003_s008_030 with Dissolve(0.5)
    k "唉，我很遗憾你得经历这些。而且，你本来可以跟我说的。我会听的。"
    j "因为你不爱说话？*轻笑*"
    scene c003_s008_031 with Dissolve(0.25)
    k "我不想让你觉得我很自私、不在乎别人，可是……"
    j "你只是很难维持眼神接触或长时间对话，而且常常需要休息一下给自己充电？"
    scene c003_s008_032 with Dissolve(0.25)
    k "正是如此。但我不想让你觉得，在这件事上你只有一个人。"
    j "谢谢。而且说实话，我前妻现在还排不在我担心的事项清单上。"
    scene c003_s008_033 with Dissolve(0.25)
    k "我能想象。那么……"
    j "什么事？"
    scene c003_s008_034 with Dissolve(0.25)
    k "不不，我不该问。"
    j "问吧。你心里有一部分是好奇的。"
    k "是什么原因？如果你不介意我问的话。"
    scene c003_s008_035 with Dissolve(0.5)
    menu:
        "我们只是渐渐走远了。\n[rgr](卡莉 信任 +1)":
            $ k_trust +=1
            j "*叹气* 我们只是渐渐走远了。也许我们结婚时太年轻了。或者我们没意识到自己其实并不合适。很难说。"
            "{color=#ffcccc}听起来他是在替她说话。所以就算离婚了，他也不想说她的坏话。{/color}"
            scene c003_s008_036 with Dissolve(0.25)
            k "哦。谢谢你愿意回答。"
        "也许我只是不是个好丈夫。\n[rgr](卡莉 信任 +1)":
            $ k_trust +=1
            j "*叹气* 也许我只是不是个好丈夫。或者，我觉得我没能满足她的需要。在情感上。"
            "{color=#ffcccc}听起来他是在替她说话。所以就算离婚了，他也不想说她的坏话。{/color}"
            scene c003_s008_036 with Dissolve(0.25)
            k "哦。谢谢你愿意回答。"
        "她早就走出来了。":
            j "她早就走出来了。情感上——而且很可能身体上也一样——在我们分居的时候。我敢说她现在正跟新男友在一起。"
            scene c003_s008_036 with Dissolve(0.25)
            k "哦。谢谢你愿意回答。"
        "我不太想说。":
            j "我不想细讲。我觉得那样我会显得满腹怨气，而我们俩都不会有什么好形象。抱歉。你只要知道，有时候两个人在一起，就是走不下去。"
            scene c003_s008_036 with Dissolve(0.25)
            k "哦，这个嘛……"
    if k_friend >= 5 and k_desire >= 2:
        scene c003_s008_045 with Dissolve(0.25)
        k "唔嗯~~~"
        "嗯，这番闲聊挺不错，不过看起来卡莉已经聊够了，需要独处。最好道个晚安离开，把这件事留在正面的位置。"
        scene c003_s008_040 with Dissolve(0.25)
        "呃，这倒是出乎意料。不过挺好。自从离婚以后我就没怎么跟人联系过，现在大家都陷在这摊烂事里，卡莉和劳拉都比我想象的要亲近得多。"
        "我不会把这当成她们对我有什么感情。她们也需要一点温暖和安慰，而我是唯一能用的那块肉。"
        scene c003_s008_041 with Dissolve(0.25)
        "我不会说出口，但我不讨厌她柔软的身体贴着我。别硬了，伙计。"
        k "嗯，我很抱歉。也谢谢你在这时候陪着我——陪着我们。我真不知道要是没有你和劳拉在，我会怎么办。"
        scene c003_s008_042 with Dissolve(0.5)
        k "也许会被吓得魂不附体。"
        j "没什么。虽然我们更希望根本不用来这儿，但我不介意有人陪。有我可以依靠的人，感觉挺好。"
        "不瞒你说。我非常清楚她那两个奶子正压在我胸口上，而我正努力不对它有反应。"
        scene c003_s008_043 with Dissolve(0.25)
        j "再说了，你做的汉堡确实好吃。"
        k "*咯咯笑* 谢谢。"
        scene c003_s008_044 with Dissolve(0.25)
        k "那个……你要是之后想聊聊天，我不介意。不过眼下我想睡会儿了。累死了。"
    else:
        scene c003_s008_037 with Dissolve(0.25)
        k "那个……你要是之后想聊聊天，我不介意。不过眼下我想睡会儿了。累死了。"
    scene c003_s008_038 with Dissolve(0.5)
    j "当然。我想我们肯定有很多可以慢慢聊的。有任何事就告诉我。关于你的，或者周围发生的。好吗？"
    k "我会的。谢谢。"
    scene c003_s008_039 with Dissolve(0.5)
    "真有意思，卡莉和我在过去几天里说的话，比她整个在环球办公用品上班期间说的都多。共同经历过的创伤，真的能造出意想不到的友谊。"
    "操，我累趴了。该上床了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_23_822", transition=Dissolve(1.0))()
    pause
    $ Hide("june_23_822", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday2 fadein 2.0
    scene c003_s009_001 with Dissolve(2)
    "我比平时醒得晚。除了半夜有个瞬间醒来、搞不清身在何处之外，我这一觉其实睡得挺好。长椅算不上舒服，但我显然被这一天的折腾累坏了。"
    scene c003_s009_002 with Dissolve(0.25)
    "该起床去看看其他人都在干什么了。得确认每个人都没事。老办公室有个好处，我能四处张望找到卡莉和劳拉。这儿？得多费点腿脚了。"
    scene c003_s009_003 with Dissolve(0.5)
    "好，卡莉还在睡。很好，让她多休息会儿。反正她也没什么别的事非做不可。"
    scene c003_s009_004 with Dissolve(0.5)
    "劳拉的沙发空了。其实也不是她的沙发，只是她昨晚睡的地方。不过她已经起来了。我该去找找她。"
    scene blank with Dissolve(2)
    scene c003_s009_005 with Dissolve(2)
    "我以为能去的地方就那么几个。除非我们把楼上一些办公室打开。可这又提醒我得去找更多钥匙。或者，我可以直接拿斧子劈门把手。"
    scene c003_s009_006 with Dissolve(0.25)
    "劳拉在锻炼。跑步。我想就是找点事做。我很惊讶她呼吸都有问题，还愿意试着动起来。"
    scene c003_s009_007 with Dissolve(0.25)
    "我……我昨天就想到，我挑的那身运动服露出的皮肤有点多——说真的，是多得多——所以这差不多是我第一次真正注意到劳拉的……身段，找不到更好的词了。"
    scene c003_s009_008 with Dissolve(0.25)
    "你不想把人当成物件——尤其是在乎朋友——但这些终究是我自己的想法。我可以对自己承认，对一个三十多岁的女人来说，劳拉挺性感的。"
    l "[player_name]？是、是你吗？"
    j "对。抱歉，我不想打断你。锻炼得不错？"
    if l_friend >= 3 and l_trust >= 0:
        scene c003_s009_010
        l "总得找点事做。这儿能做的事就那么几样。而且你了解我，我喜欢忙起来。"
        j "我陪你一起行吗？还是你想一个人待着？"
        scene c003_s009_011 with Dissolve(0.25)
        l "有人陪挺好的。"
        "我有种感觉，这比你愿意承认的还要真实。"
        scene c003_s009_012 with Dissolve(0.25)
        j "那你的目标是跑多少？不会是马拉松吧？"
    else:
        scene c003_s009_009
        l "不许盯着看。你要待在这儿，就得一起锻炼。"
        j "健身房规矩？不许盯着别人看别人锻炼？"
        scene c003_s009_011 with Dissolve(0.25)
        l "差不多是这个意思。"
        scene c003_s009_012 with Dissolve(0.25)
        j "那我陪你跑一段。你的目标是多少？不会是马拉松吧？"
    scene c003_s009_013 with Dissolve(0.5)
    l "肺允许我跑多少就跑多少。每次出门我都觉得自己很弱，够受的了。"
    j "好吧，行。稍微活动一下可能有好处。"
    scene c003_s009_014 with Dissolve(0.25)
    "少暴露在外面、等能找到医院时再去接受治疗才更靠谱，不过就让她相信运动对她有好处吧。"
    "说真的，劳拉是那种必须做点什么的人。她得动起来。她的呼吸问题加上没完没了地干等着，这大概让她难受死了。"
    scene c003_s009_015 with Dissolve(0.25)
    "所以我决定跟劳拉一起上跑步机。对，我不会全速跑，但待在旁边也没什么坏处。万一她又开始咳。"
    "劳拉就不一样了，她完全是在拼命。我不得不觉得，这不只是想锻炼而已。她是在用跑步消磨焦虑或者情绪压力吗？"
    scene c003_s009_016 with Dissolve(0.25)
    "联系不上丈夫也联系不上儿子，对她一点好处都没有。靠，即便我这么个臭脾气，我也还是挂念我的家人。还有奥蒂斯。还有……也许还有南希。可我能做的只有专注当下，专注身边的人。那是我唯一能控制的事。"
    scene c003_s009_017 with Dissolve(0.25)
    l "卡莉？她还在*喘气* *喘气*……"
    j "我上次看见她的时候还在睡。"
    l "好。那就好。"
    scene c003_s009_018 with Dissolve(0.25)
    "劳拉的体力还不算差，但已经有点撑不住了。我建议她降一档，可她跑得像有恶魔在后面追。"
    j "你这么消耗热量，等下得吃一顿巨量午餐。"
    l "*喘气* 那我们大概得去那家餐馆。我没在这儿看到什么像样的吃的。"
    scene c003_s009_019 with Dissolve(0.25)
    j "我可以*喘气*过去拿点东西。趁现在还能进。"
    l "唔嗯~~~"
    "现在大概不是讨论接下来去哪儿的时候。"
    scene c003_s009_020 with Dissolve(0.25)
    l "*喘气* *喘气* 靠……"
    l "*咳嗽* 我不行了。" with vpunch
    scene c003_s009_021 with Dissolve(0.25)
    j "你做得很好 *喘气* 第一天不至于跑二十英里 *喘气*。"
    l "不是这个意思 *喘气* *喘气*"
    "好吧，我知道我不太会看女人——南希在我离开前不止一次让我深刻认识到这一点——但我觉得劳拉心里压着很多东西。哪怕在这一切发生之前就是。"
    menu:
        "给劳拉一点空间。":
            scene c003_s009_023 with Dissolve(0.25)
            "安静听着就行。她需要的只是有人愿意听她说话。"
            scene c003_s009_024
        "把手放在她背上。\n[rgr](劳拉 好感 +1)":
            $ l_friend +=1
            scene c003_s009_022 with Dissolve(0.25)
            j "嘿，我在这儿。"
            scene c003_s009_025
    l "*叹气* 撑住。撑住。"
    j "劳拉？"
    scene c003_s009_026 with Dissolve(0.25)
    l "我在这儿拼命想跑掉这把发福的老屁股。不管我多努力，都比不过那些年轻姑娘，这场仗我输定了。"
    j "你不是在跟任何人竞争。"
    scene c003_s009_027 with Dissolve(0.25)
    l "我们永远都在竞争，[player_name]。这就是为什么我们都要买化妆品、买贵的衣服、拼命跑步好像命悬一线。因为永远有个更年轻、更性感的人。"
    j "好吧~~~ 好吧~~~"
    scene c003_s009_028 with vpunch
    l "*叹气* 我就在这儿坐一会儿。"
    j "有什么需要我们谈的吗？"
    l "不不。*叹气* 只是……这一切实在太过了，我实在已经受够了。心累。抱歉。别管我。"
    menu:
        "好。我不管。\n[rrd](劳拉 好感 -1)":
            $ l_friend -=1
            j "好。我不管。"
        "[gr]或者，你可以跟我说说。":
            scene c003_s009_030 with Dissolve(0.25)
            j "或者，你可以跟我说说。"
            l "没什么好说的。我只是在发牢骚。我什么都担心，又累，胸口还因为咳嗽疼，就这样。"
            j "好吧，那我不提了。"
    "暂时不提，不过我感觉这事迟早得回头再说。"
    scene c003_s009_031 with Dissolve(0.25)
    j "你说什么？等一下。我刚想到一件事。"
    l "什么？怎么了？你要去哪儿？"
    j "后面有间办公室。我猜是给员工用的。健身中心的员工。我就是在那儿找到更衣室的储物柜钥匙的。"
    l "说到这个，你就找不到更不露一点的？"
    menu:
        "我喜欢把我的姑娘们打扮得漂漂亮亮。\n[rgr](劳拉 欲望 +1)":
            $ l_desire += 1
            j "什么？我喜欢把我的姑娘们打扮得漂漂亮亮。"
            scene c003_s009_033 with Dissolve(0.25)
            l "住口。你会让我以为你在调情。"
            j "也许我就是在调情。但那就别告诉人力资源部了。"
        "当时时间紧迫。":
            j "我那时候就觉得，时间确实紧迫。你们俩已经光着身子在淋浴间里了。"
            scene c003_s009_032 with Dissolve(0.25)
            l "好吧，也许我该换一件。"
    scene c003_s009_034 with Dissolve(0.25)
    j "不过眼下我更关心的是看看能不能找到电视遥控器。我四处看过，没找到。但你也知道，遥控器丢在自家客厅里？那你就完了。"
    l "你要是想去办公室，我在这儿帮你盯着。"
    j "当然，当然。我不会待太久。"
    scene c003_s009_035 with Dissolve(0.25)
    "{color=66ff33}操。我真该直接告诉他。这种事有人站在我这边就好了。{/color}"
    scene blank with Dissolve(2)
    scene c003_s009_036 with Dissolve(2)
    j "我回来了，还找到了遥控器。是{b}那个{/b}遥控器吗？希望是。要是的话，咱们放{a=https://jerryspringertv.com/}《杰瑞·斯普林格》{/a}吧。"
    l "要不我们先看看有没有任何节目？"
    scene c003_s009_037 with Dissolve(0.25)
    j "你把兴致全给弄没了。还有……"
    scene c003_s009_038 with Dissolve(0.25)
    j "有了。"
    l "雪花屏。当然了。"
    scene c003_s009_039 with Dissolve(0.25)
    j "我挨个台翻翻。也许他们本地台有信号。"
    "对，什么都没有。他妈的。"
    l "*叹气* 那答案就是这样了。"
    j "对，真白忙活。"
    scene c003_s009_040 with Dissolve(0.25)
    l "遥控器放这儿吧。我们待会儿再看看。以防万一。"
    j "也对。那么，接着跑？"
    l "不不。我得冲一下。我感觉自己脏死了。"
    scene c003_s009_041 with Dissolve(0.25)
    j "你说了算。我去看看卡莉醒了没。也许能找找钥匙。或者别的什么。待会儿见。"
    l "我们肯定会再见的。"
    scene blank with Dissolve(2)
    scene c003_s010_001 with Dissolve(2)
    j "哦，你在这儿啊。我还在想你起没起床。看样子你已经穿好衣服要出门了？"
    k "我、我是想来告诉你和劳拉一声的。然后拿电梯钥匙。我想着我可以过去做点吃的。毕竟我们就在隔壁。而且我们搬过来不就是为了这个吗。至少是其中一部分原因。"
    scene c003_s010_002 with Dissolve(0.25)
    j "对，我也在想同样的事。这件事开始以来，我们都没正经吃过几顿。要是能有点吃的就好了。我们可以等劳拉洗完再去。她刚才跑了一段。"
    k "我、我在想让她留在这儿。让她有机会恢复一点。再多恢复一点。我、我自己一个人去就行。你可以留在这儿。陪着她。"
    scene c003_s010_003
    j "或者，我去把东西穿上，拿上我们那把不算新的斧头，我陪你一起去。"
    k "你不用。我不是小孩子了。我能行。"
    "有人在给自己鼓劲。不过我不太喜欢让她一个人出去。"
    menu:
        "[gr]跟她说清楚。":
            j "我知道你能行。要是情况正常，我就下令让你去了，但最好是谁都不要单独外出。不能再这样了。尤其是我们已经知道外面有东西的时候。我不管我们离{i}汉堡店{/i}有多近。意外随时会发生。我们出门的时候得像个团队。"
            scene c003_s010_004 with Dissolve(0.25)
            k "那把劳拉留在这儿呢？"
            j "她在屋里是安全的。"
            scene c003_s010_005 with Dissolve(0.25)
            k "你、你说得对。"
        "这件事要严厉些。\n[rrd](劳拉 好感 -1)":
            $ k_friend -= 1
            j "对，那可不行。你不能一个人出去。没有陪同也不行。尤其是我们已经知道外面有东西的时候。我不管我们离{i}汉堡店{/i}有多近。"
            scene c003_s010_004 with Dissolve(0.25)
            k "你之前一直是一个人出去的。"
            j "那是在前天晚上之前。"
            scene c003_s010_005 with Dissolve(0.25)
            k "唔嗯……好吧。"
    "她对此并不高兴，但在这种情况下，我们需要的是每个人都安全、理智，而不是都对这一切满意。我并不想当这个生存小队的老大，可总得有人来当。而且我觉得劳拉会支持我。"
    scene blank with Dissolve(2)
    scene c003_s010_006 with Dissolve(2)
    $ l_anxiety +=1
    "准备的时间比预想的长得多，不过我还是换上了衣服，我们在出发前告诉了劳拉计划。她很安静，没有反对这个决定。看她之前的样子，我宁愿把这理解为她对自己的处境已经认命了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c003_s010_007 with Dissolve(2)
    play music outsideday fadein 2.0
    "除了趟过浓得化不开的雾——感觉比平时更糟——我们走回餐馆这一路没出什么事。"
    scene c003_s010_008 with Dissolve(1)
    k "*叹气* 到了。我真是受够了天天吃汉堡。"
    j "我们可以去冷库翻翻，看看还有别的什么。他们肯定有鸡肉。或者早餐香肠饼。培根。天啊，我做梦都想要培根。"
    scene c003_s010_009 with Dissolve(0.25)
    k "我们可以去看看。我不想在这儿待太久，但看看我们还有什么别的选择也不亏。看样子，他们可能正等着送货。"
    j "嗯？你什么意思？"
    scene c003_s010_010 with Dissolve(0.25)
    k "里面的量够我们吃一阵子，但不够他们招待几百个客人。他们可能本来快收到新一批肉、面包和生鲜了。这种店一周至少进两三趟货。可能还不止。"
    j "哦~~~ 对，那就说得通了。希望大部分东西都能放得住。"
    "因为一旦开始变质，再去翻找别的吃的可就够呛了。"
    scene blank with Dissolve(2)
    scene c003_s010_011 with Dissolve(2)
    "我尽力帮卡莉安顿好之后，她就把我赶走了。我把这理解成她铁了心要证明自己有点用。"
    scene c003_s010_012
    "于是我回到用餐区待着，尽力扮演一个哨兵。"
    scene c003_s010_013 with Dissolve(0.25)
    "不到十分钟，我就快撑不住打瞌睡了。我错过了早上那杯咖啡，而且这风景也实在算不上激动人心。这让我不禁想，那些靠这个拿工资的人，工作得有多枯燥麻木。"
    "没过多久，我就听见油脂在滋滋作响，香味慢慢飘了过来。这可比洗手间里偶尔飘过来的那点腐败气息强多了。"
    stop music fadeout 2.0
    scene c003_s010_014
    "我知道劳拉不喜欢「把尸体挪走」这个提议，但我越来越觉得，把它挪到外面对我们更好一些。如果我们还要在这儿待更久的话。而且说实话，这个决定到现在还没做。"
    "至少，让我去看看……"
    scene c003_s010_015 with Dissolve(0.25)
    "什……谁……那是……"
    extend "劳拉？靠，她要是自己跟出来我可要气疯了。"
    scene c003_s010_016 with Dissolve(0.25)
    "等等。是她吗？个子太高了，不像她。是别人？"
    play music horror fadein 2.0
    scene c003_s010_017 with Dissolve(0.25)
    "不。操。是……"
    scene c003_s010_018 with Dissolve(0.5)
    "我猜那就是劳拉和卡莉前两天想告诉我的。它跟到这儿来了？不可能。靠，我不知道。也许吧。这总比「不止一只」要好。"
    "长得真瘆人。看起来像个人，又不是。更像是某种「加密动物」。如果我们能活着出去，我倒要给它起个名字。"
    scene c003_s010_019 with Dissolve(0.25)
    "「行走脓包」？太像乐队名了。「烧伤男」？不，跟{a=https://burningman.org/}Burning Man{/a}太接近了。「灼烧者」？在我看来太游戏了点。"
    "现在看来，它好像没看见我。其实它只是在漫无目的地四处晃。"
    scene c003_s010_020 with Dissolve(0.5)
    k "好，我弄完了。而且我闻起来像个快餐厨子。你能帮我把这些打包吗？多出来的可以放进你昨天说的那个迷你冰箱里。"
    scene c003_s010_021 with Dissolve(0.25)
    j "嘘~~~ 安静。过来。趴低。"
    k "嗯？"
    j "在外面。我们的怪物。"
    scene c003_s010_022 with Dissolve(0.25)
    k "哦，操。操。"
    $ k_anxiety += 1
    scene c003_s010_023 with Dissolve(0.5)
    k "它在干什么？你觉得它跟着我们了吗？"
    j "我不知道。它看起来不像是会想太多的事。"
    "虽然细节很难看清，可我怎么也看不出任何像脸的地方。"
    scene c003_s010_024 with Dissolve(0.25)
    k "让我……"
    if k_trust >= 3 and k_anxiety >= 3:
        scene c003_s010_026 with hpunch
    else:
        scene c003_s010_025 with hpunch
    "操，它就在那儿。我好像能听见它隔着窗户喘气。咕噜咕噜的。像一种恶心的呼噜声。简直像肺癌的化身。"
    "它看得见我们吗？它在找我们吗？希望它没听见我们在这儿。既然它看起来不打算闯进来，那我只能认为我们暂时没事。"
    scene c003_s010_027
    "我把斧子放在那边了。真有需要我就冲过去拿。让卡莉跑，但不是往外面——她没穿外套。也许让她自己躲进冷库里。"
    if k_trust >= 3 and k_anxiety >= 3:
        scene c003_s010_031 with Dissolve(0.5)
    else:
        scene c003_s010_028 with Dissolve(0.5)
    "可以理解，卡莉吓坏了。"
    menu:
        "没事。我在这儿。\n[rgr](卡莉 好感 +1)":
            $ k_friend +=1
            j "嘿。嘿。没事的。我在这儿。我们只要等着，它应该就会走。上次不是也走了吗？"
            if k_trust >= 3 and k_anxiety >= 3:
                scene c003_s010_032 with Dissolve(0.25)
            else:
                scene c003_s010_029 with Dissolve(0.25)
            k "好、好吧。你说得对。可万一它不走呢？"
            j "我有一把斧子，还有毫无根据的自我保护意识。"
            if k_trust >= 3 and k_anxiety >= 3:
                scene c003_s010_033 with Dissolve(0.25)
            else:
                scene c003_s010_030 with Dissolve(0.25)
            k "*咯咯笑* 好吧~~~"
            "不合时宜的玩笑似乎还真有点用。"
        "让我看看能不能把它吓跑。":
            j "让我看看能不能把它吓跑。"
            if k_trust >= 3 and k_anxiety >= 3:
                scene c003_s010_032 with Dissolve(0.25)
            else:
                scene c003_s010_029 with Dissolve(0.25)
            k "不。别。别动。求你了。它……我们就等它自己走吧。"
    stop music fadeout 2.0
    scene blank with Dissolve(1)
    scene c003_s010_034 with Dissolve(1)
    play music outsideday fadein 2.0
    "我不知道我们贴着墙坐了多久。等我觉得时间应该足够让它走开之后，我偷偷瞄了一眼。"
    scene c003_s010_035 with Dissolve(0.25)
    k "它是不是……"
    j "只有雾。我觉得它走了。"
    scene c003_s010_036
    k "你确定？"
    j "雾这么厚，没法确定。不过我没看见它。东西准备好了吗？"
    scene c003_s010_037 with Dissolve(0.25)
    k "呃，好、好了。你能帮我把它打包吗？我、我特别想离开这儿。"
    j "当然。收拾完我们就回去。回到办公室里锁起门来会让我好受些。把楼梯堵上这主意真不错。"
    "这时候我们冲回厨房，把卡莉做好的所有食物都装盒装袋。她明显被刚才的事吓到了，但竭力不让它影响自己太多。"
    scene blank with Dissolve(1)
    scene c003_s010_038 with Dissolve(1)
    j "好，计划是这样：我打头阵。你跟着我回办公室。要是看见雾里有什么在动，你就拼命往大厅跑。别停，直到进屋。我去吸引它的注意力，把它引开。你去电梯那边，我尽快赶到。"
    k "我、我……好吧。"
    "她大概是想说点倔强的话，比如她自己没问题、不用我逞英雄。但我觉得现实已经甩了她一两个残酷的真相。我们俩都紧绷得不行，不管那东西是什么，都不是我们该去招惹的。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c003_s010_039 with Dissolve(2)
    "好，我出来了，四下没看见有什么东西潜伏在附近。到了这一步，我只能靠听，试着先听见它，因为我几乎什么都看不见。只有雾和影子。只能靠空间记忆来走了。"
    scene c003_s010_040 with Dissolve(0.25)
    "也许我们运气好，它已经走开了。不过我们还是得尽快移动。"
    play music monster
    scene c003_s010_041 with hpunch
    j "操！"
    k "什么？哦，操！"
    scene c003_s010_042 with Dissolve(0.25)
    j "快跑。走走走！"
    "我觉得它能听见我们。或者，它正拖着步子朝我们过来，像是听得见。倒不像是移动得有多快。事实上，我觉得真有必要的话，我们跑得过它。"
    j "快走。别等我。我会追上来。"
    scene c003_s010_043 with Dissolve(0.25)
    j "这边！这边！到这边来！"
    "我成功吸引了它的注意，卡莉就像我说的那样撒腿跑了。好姑娘。它并不算快，这对我有利。"
    scene c003_s010_044 with Dissolve(0.25)
    "看看我能不能在这儿演个伐木工。你倒是装出一副没躲开的意思啊。"
    play sound gas
    scene c003_s010_045 with flashyellow
    j "哦操呃~~~ *咳嗽* 操啊~~~ "
    "它刚才他妈对我做了什么？朝我喷了一口恶心的雾？靠，光是站在那儿空气都灼得慌。就算戴着眼镜我也很难看清。"
    scene c003_s010_046 with Dissolve(0.25)
    "打起精神来，兄弟！来。你能听见。就在附近。"
    j "*咳嗽* *咳嗽*"
    play sound axehit
    scene c003_s010_047 with flashred
    j "唔嗯~~~"
    "*啵*！"
    scene c003_s010_048 with Dissolve(0.25)
    "打中了。不知道造成多少伤害，但肯定把它打退了。得赶紧出去。几乎看不见。几乎喘不上气。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c003_s010_049 with Dissolve(2)
    play music insidedark fadein 2.0
    k "*喘气* *喘气* *咳嗽*" with hpunch
    "{color=#ffcccc}就算戴着口罩，我还是吸进去太多雾了。让我先喘口气。{/color}"
    scene c003_s010_050 with Dissolve(0.25)
    "{color=#ffcccc}[player_name]在哪儿？我以为他就在我后面。别告诉我他……没有他我不能上去。我该回大厅去。我记得他说过——{/color}"
    play sound doorclose
    scene c003_s010_051 with Dissolve(0.25)
    "{color=#ffcccc}走廊尽头那扇门开了。我该不该……万一那不是[player_name]呢？{/color}"
    scene c003_s010_052 with Dissolve(0.5)
    j "卡莉。是我。我在这儿。"
    k "谢天谢地。你有没有……"
    scene c003_s010_053 with Dissolve(0.25)
    k "怎么了？哦，你……*咳嗽* *咳嗽*" with hpunch
    j "对，它靠得最近，然后朝我喷了点什么。有一阵子我既看不清也喘不上气。现在还觉得自己像在外面泡了那玩意儿好几个小时。我得马上离开这儿，冲个澡。"
    scene c003_s010_054 with Dissolve(0.25)
    k "对，你得去。*咳嗽*" with vpunch
    j "你、你没事吧？"
    scene c003_s010_055 with Dissolve(0.5)
    k "吓得魂都没了，不过死不了。你跟它走散了？它还在外面吗？"
    j "我身后没看见它 *咳嗽* 我用斧子砍了它一下，但我没留下来补完。抱歉。按电梯，我们上去。劳拉肯定在担心我们去哪儿了。"
    "刚才真是险。也说明那东西没打算善罢甘休。它是个威胁。但只要我们能绕开它，就还能应付。"
    scene c003_s010_056
    k "谢谢。为……为了一直陪着我。还有……"
    j "我们是一条船上的，姑娘。"
    scene c003_s010_057 with Dissolve(0.25)
    k "是啊。"
    scene blank with Dissolve(2)
    scene c003_s011_001 with Dissolve(2)
    "尽管我拼命想忍住，短短一段电梯里我还是一直在咳。被那怪物喷了之后，我的外套还在渗出那毒雾。"
    l "哦，谢天谢地，我正担心你们呢。比我想的久多了。"
    scene c003_s011_002 with Dissolve(0.25)
    j "站 *咳嗽* 站远点。" with vpunch
    k "我们弄到食物了，可也碰上那晚的那个东西。"
    l "靠，你们俩没事吧？"
    scene c003_s011_003 with Dissolve(0.25)
    j "我得 *咳嗽* *咳嗽*……" with hpunch
    k "去吧。我去跟劳拉说发生了什么。"
    scene c003_s011_004 with Dissolve(0.25)
    "我有两个理由得去冲澡。一？我的肺和露在外面的皮肤，都感觉像被泡在辣椒油盆里。二？我不能让劳拉吸进这玩意儿。她才刚开始从这趟奔波里恢复。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c003_s011_005 with Dissolve(2)
    play music insideday2 fadein 2.0
    play ambient shower
    "好，开始觉得好点了。不过还是让我再多享受一会儿吧。等我回去食物肯定凉了，但眼下无所谓。有一部分那……喷雾？不管是什么，溅到了我的脖子和手腕上，烧得要命。"
    scene c003_s011_006 with Dissolve(0.25)
    "所以那就是劳拉和卡莉那晚近距离看到的东西。难怪劳拉会追出来。真是他妈恐怖。而且我一开始还觉得它可能没有敌意，但巷子里那一下足以说明我们必须避开它。"
    "不知道我那斧子有没有走运伤到它、伤得够不够让它以后都不再是麻烦？因为我可不想每次出去找吃的都要应付它。"
    scene c003_s011_007 with Dissolve(0.25)
    "然后还有一堆关于它从哪儿来的疑问。我原以为可能是被雾严重烧伤的人，但那样反而更糟。感觉像是变异了之类的。"
    "我想我是科幻恐怖小说看太多了。脑子里的想象停不下来。"
    scene c003_s011_008 with Dissolve(0.5)
    l "[player_name]？是我，劳拉。"
    j "对，我这边快弄完了。"
    scene c003_s011_009 with Dissolve(0.25)
    l "卡莉把刚才的事都跟我说了。你没事吧？"
    j "迎面挨了一下。像是普通雾的浓缩版。所以我才不想让你靠太近。不想让那些烟气沾到你身上——"
    stop ambient fadeout 2.0
    scene c003_s011_010 with Dissolve(0.25)
    l "我、我知道。我从你挂外套的地方就闻到了。我、另外给你找了件衣服。我觉得你可能用得上。"
    scene c003_s011_011 with Dissolve(0.5)
    j "啊，靠，对。我过来的时候没拿换洗的衣服。没想到会这样冲回来。你吃了吗？"
    l "吃了。还有谢谢你……总之，谢谢你的一切。谢谢你照看卡莉，确保你们俩都平安回来。"
    scene c003_s011_012 with Dissolve(0.25)
    j "她怎么样？我知道我不该把她当成那种脆弱的人，可它在餐馆附近徘徊的时候，她吓坏了。"
    l "她神经已经绷得很紧了，不过东西吃了。我有种感觉，等她缓过来，大概会一头栽倒着睡死过去。"
    scene c003_s011_013 with Dissolve(0.25)
    j "好。那个，我该……"
    l "让我……对，我给你留点空间。"
    "不太习惯看到劳拉这一面。她平时像个小火枪炮，谁的气都不受。现在呢？虚弱、疲惫、疲惫不堪。还有……难过。她心里有东西在啃着她。我该晚点找她谈谈。"
    scene blank with Dissolve(2)
    scene c003_s011_014 with Dissolve(2)
    "擦干身子、穿上劳拉给我找的衣服之后（可挑的真是少得可怜），我吃了自己那份饭——要我说，这顿可是我应得的。"
    scene blank with Dissolve(2)
    scene c003_s011_015 with Dissolve(2)
    "卡莉跑开一个人待着，我并不意外。今天的动静显然对她来说够多了。虽然我想去看看她，但我觉得还是给她一点空间好。我们明天早上再碰头。"
    scene blank with Dissolve(2)
    scene c003_s011_016 with Dissolve(2)
    "劳拉则是一副闷闷不乐、说实话有点疏远的样子。所以我也先让她自己冷静。我们之前聊过，我敢肯定得知我们在外面惹上了什么东西，并不会让她心情变好。"
    "于是我把时间花在盯着健身中心的窗户上，徒劳地想看看我们那位「朋友」是不是还在外面。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_23_713", transition=Dissolve(1.0))()
    pause
    $ Hide("june_23_713", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain2 fadein 2.0
    scene c003_s011_017 with Dissolve(2)
    "浓得密不透风的雾渐渐让位给黑暗。我决定回去了。"
    scene blank with Dissolve(2)
    scene c003_s011_018 with Dissolve(0.25)
    "好，很安静。我不想打扰任何人，但确实想确认大家都还好。看来卡莉已经睡下了。我能想象连续两天在雾里跋涉对她有多累，哪怕她高中跑过越野。"
    scene c003_s011_019 with Dissolve(0.25)
    "不知道劳拉去哪儿了。这地方够大，我得费点工夫才能找到每个人。"
    l "{size=32}*吸鼻子* *吸鼻子*{/size}"
    "是她……等等……我听见劳拉了，但听起来她好像在哭。"
    scene blank with Dissolve(2)
    scene c003_s012_001 with Dissolve(2)
    "真够呛。我理解原因。她害怕，又联系不上家人。而她最近一直把情绪写在脸上。生活里一堆问题一直在水面下闷着，这会儿全冒出来了。只是我从没见过她为什么事难过。她一直跟哥们儿一样。"
    scene c003_s012_002 with Dissolve(0.25)
    j "劳拉？本来想问你没事吗，可是……"
    l "*叹气* 靠。我不想……"
    scene c003_s012_003 with Dissolve(0.25)
    j "没事的，劳拉。我懂。你在难过这件事上也从来没怎么掩饰过。而且理由充分。你想让我走开吗？还是想找个人听你说说？至少这个我能做到。"
    l "唔嗯……坐下吧。求你了。反正你也早就见过我不堪的样子了。我想我也没法再假装自己没事了。"
    scene c003_s012_004 with Dissolve(0.5)
    j "我觉得这事让我们都比原本想的更看见、更了解了彼此。以前我们一起工作、可以避开很多私人的痛苦，那是一回事。可现在我们互相掺和得太深，想避都避不开。"
    l "这点我完全同意。不过我真希望你能多跟我说说你的离婚。我总觉得我本可以在你身边。"
    j "过去的事就过去了。现在才是现在。告诉我你怎么了。我知道你今天早上心情就不对。你现在是什么感觉？除了对未知那种惯常的恐惧和焦虑之外？"
    scene c003_s012_005 with Dissolve(0.25)
    l "很多都是，[player_name]。我恨自己不知道彼得在哪儿，也不知道他好不好。"
    j "他是个聪明的孩子。你可没养出个笨儿子。他大概跟学校那帮同学躲在宿舍里。开一场彻头彻尾的狂欢派对。男男女女都有。"
    scene c003_s012_006 with Dissolve(0.25)
    l "这可不能让事情变好。"
    j "劳拉，你儿子在上床。你就接受这一点吧。你再怎么当妈，也拦不住他在另一个州找姑娘。"
    scene c003_s012_007 with Dissolve(0.5)
    l "那在同一个他妈的县里呢？"
    j "嗯？什么？等等，我是说……这事……现在也不只是因为彼得了，对吧？"
    "靠，所有的暗示早就摆在那儿了。只是我没把它们串起来。而且我们俩谁也没比以前更坦承过自己的私生活。"
    scene c003_s012_008 with Dissolve(0.25)
    l "是我和基思的事。嗯，主要是基思。我很确定他在外面乱搞。可能还跟某个同事。那些迹象全都在。你也看过那些讲人们发现被出轨的电视剧和电影。"
    l "我们已经很久没同床了。上次同床还是儿子去上大学以后，我把这当成两个成年人各有各的生活忙。但不只是这样，我看得出来。"
    j "你知道是谁吗？"
    scene c003_s012_009 with Dissolve(0.25)
    l "不太确定，但我有几个猜测。或者说是猜到一个。他办公室里那个金发蠢货，老是跟他调情，连我偶尔去找他的时候都是。她这么干已经有一阵子了——去年就开始了——我之前根本没当回事。"
    l "我以为他会是个忠诚的丈夫，看来他是想把我换个新型号。"
    scene c003_s012_010 with Dissolve(0.25)
    j "你确定吗？是那种找到实证的程度？我真希望这只是一场误会，只是你们没谈过。毕竟他是男人，大概不会谈自己的感受。"
    l "有天晚上他很晚才回家，身上带着香水味。他跑过去洗澡的时候我闻到了。他说自己帮朋友搬了些东西，所以一身汗味。"
    scene c003_s012_011 with Dissolve(0.25)
    j "我的天，精彩。"
    l "我猜他就是等着彼得不在家，好去找个小姑娘让他感觉自己像个男人。我猜跟我过了二十年已经够他受的了。我对他不再够温柔了。我以为我们是朋友，以为他能接受真实的、我这样的自己。"
    scene c003_s012_012 with Dissolve(0.25)
    j "劳拉，如果这是真的，他就是个蠢货。可你得跟他谈。当面质问。"
    scene c003_s012_009 with Dissolve(0.25)
    l "好让他再来一次煤气灯操控？说服我什么都没发生？我敢说他现在正跟她在一起，把所有时间都花在她身上。现在没人看得见我的时候。对他来说可真方便。"
    l "天哪，我早该更努力一点的。可一旦有了孩子，就很难再又软又女性化了。你会忙到顾不上，只顾着工作、操心那些大人事，比如交账单、家里的大小工程。"
    if l_friend <= 2 or l_desire <= 0:
        scene c003_s012_064 with Dissolve(0.5)
        j "嘿，嘿，没事。不是你想的那样。你很棒，而且恕我直言，很性感。等这一切过去，你可以好好坐下来跟基思把话说开，然后——"
        scene c003_s012_065 with Dissolve(0.25)
        l "要是已经过了能谈的阶段了呢？"
        j "没有什么是过了谈不拢的阶段的，劳拉。你们有共同的家庭，共同的生活，还有一个儿子。电影要是教会了我什么，那就是——一场突如其来的灾难最能把人拉到一起。我敢说基思现在没法跟你说话了，反倒会明白他平时有多不拿你当回事。"
        scene c003_s012_066 with Dissolve(0.25)
        l "*叹气* 我……谢谢你愿意试一把。也许你是对的。看来我们只能指望了。"
        j "有点盼头总比什么都没有强。"
        scene c003_s012_067 with Dissolve(0.25)
        l "谢谢。为了……在这儿。当个朋友。我……"
        j "没事的，劳拉。我们已经够惨了。别让这些把你压垮。"
        "我抱了劳拉一会儿。我不知道我们这番话对她有没有用，但她看起来平静下来了。她自己的婚姻早就乱成一团，这是我本该看出来的。她说过的小抱怨已经够多了，我本可以把线索串起来。"
        scene blank with Dissolve(2)
        scene c003_s012_068 with Dissolve(2)
        "过了一阵，劳拉把自己收拾得差不多了，我觉得今晚大概就到此为止。这场谈话肯定不会就此结束——在她真正能跟丈夫谈之前都不会——不过至少她今晚也许能睡得踏实一点。"
        l "我、我要去睡了。我累坏了，而且……"
        scene c003_s012_069 with Dissolve(0.25)
        j "我懂。"
        l "你也该睡。下一步的事我们明天再谈。好吗？"
        scene c003_s012_070 with Dissolve(0.5)
        j "听起来不错。晚安。"
        l "你、你也晚安。"
        scene c003_s012_071 with Dissolve(0.25)
        "嗯，这至少让之前那些事说得通了。就算在这一切变成烂摊子之前，我也听到过一些小暗示。可现在我们一直待在一起，那些迹象就越来越明显了。就是……基思出轨？真的？很难相信他会蠢到这种地步。"
        "唉，晚了，我该找张沙发或者长椅凑合一晚。"
    else:
        $ ch3_laura_kiss = "yes"
        scene c003_s012_013 with Dissolve(0.5)
        j "嘿，嘿，没事。不是你想的那样。你很棒，而且恕我直言，很性感。等这一切过去，你可以好好坐下来跟基思把话说开，然后——"
        play voice_loop kiss
        scene c003_s012_015 with flashpink
        l "嘘呜~~~ 唔唔~~~"
        "哦？哇，呃……我猜我们最近确实亲近了不少。这一整件事确实让我们比我原本计划的亲近得多。我该……"
        "操，我不该……可是……万一呢？"
        menu:
            "收手。":
                "我们该做正确的事。我这鸡巴会恨死我，但我必须退开。踩刹车。"
                stop voice_loop
                scene c003_s012_014 with Dissolve(0.5)
                j "嘿，呃……"
                l "我……哈啊~~~[player_name]……"
                scene c003_s012_072 with Dissolve(0.25)
                j "劳拉，我们应该……"
                l "*叹气* 我……我知道。我……这是我的错。"
                scene c003_s012_073 with Dissolve(0.25)
                j "不算错。我懂。这段时间空气里一直很紧绷，我们也比平时亲近得多。你大概看见了我不想给别人看的部分。"
                l "我想就是这样了。"
                "她对我们停下来是不是有点失望？我自己心里也挺矛盾的，不过我只当那是一时情绪上头、外界压力加上机会凑在一起的结果。"
                scene c003_s012_064 with Dissolve(0.5)
                l "[player_name]，要是已经过了能谈的阶段了呢？我和基思之间？"
                scene c003_s012_065 with Dissolve(0.25)
                j "没有什么是过了谈不拢的阶段的，劳拉。你们有共同的家庭，共同的生活，还有一个儿子。电影要是教会了我什么，那就是——一场突如其来的灾难最能把人拉到一起。我敢说基思现在没法跟你说话了，反倒会明白他平时有多不拿你当回事。"
                l "*叹气* 我……谢谢你愿意试一把。也许你是对的。看来我们只能指望了。"
                scene c003_s012_066 with Dissolve(0.25)
                j "有点盼头总比什么都没有强。"
                l "谢谢。为了……在这儿。当个朋友。我……"
                scene c003_s012_067 with Dissolve(0.25)
                j "没事的，劳拉。我们已经够惨了。别让这些把你压垮。"
                "我抱了劳拉一会儿。我不知道我们这番话对她有没有用，但她看起来平静下来了。她自己的婚姻早就乱成一团，这是我本该看出来的。她说过的小抱怨已经够多了，我本可以把线索串起来。"
                scene blank with Dissolve(2)
                scene c003_s012_068 with Dissolve(2)
                "过了一阵，劳拉把自己收拾得差不多了，我觉得今晚大概就到此为止。这场谈话肯定不会就此结束——在她真正能跟丈夫谈之前都不会——不过至少她今晚也许能睡得踏实一点。"
                l "我、我要去睡了。我累坏了，而且……"
                scene c003_s012_069 with Dissolve(0.25)
                j "我懂。"
                l "你也该睡。下一步的事我们明天再谈。好吗？"
                scene c003_s012_070 with Dissolve(0.5)
                j "听起来不错。晚安。"
                l "你也是。"
                scene c003_s012_071 with Dissolve(0.25)
                "嗯，这至少让之前那些事说得通了。就算在这一切变成烂摊子之前，我也听到过一些小暗示。可现在我们一直待在一起，那些迹象就越来越明显了。就是……基思出轨？真的？很难相信他会蠢到这种地步。"
                "唉，晚了，我该找张沙发或者长椅凑合一晚。"
            "继续。\n[rgr](劳拉 爱意 +1)\n[rrd](劳拉 欲望 -1)\n[pks]":
                $ l_sex += 1
                $ l_love += 1
                $ l_desire -=1
                $ ch3_laura_sex = "yes"
                call ch3_laura_sex from _call_ch3_laura_sex
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_24_848", transition=Dissolve(1.0))()
    pause
    $ Hide("june_24_848", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday2 fadein 2.0
    scene c003_s013_001 with Dissolve(2)
    "{color=#ffcccc}不只是劳拉觉得被磨得精疲力尽。我的体力本来也该更好。可过了这几天，我实在感觉不太好。{/color}"
    scene c003_s013_002 with Dissolve(0.25)
    k "早上好。"
    l "早，卡莉。*打哈欠* 你起得真早。"
    scene c003_s013_003 with Dissolve(0.25)
    k "我昨晚很早就睡着了。我猜我一觉睡到了天亮。睡得跟婴儿一样。"
    if l_sex == 1:
        "{color=#66ff33}那就是说，她没听见我和[player_name]在干那事。谢天谢地。{/color}"
    else:
        "{color=#66ff33}那就是说，她没听见我和[player_name]在说话。谢天谢地。我想暂时把这件事只留在[player_name]和我之间。{/color}"
    l "要一起晨跑吗？"
    scene c003_s013_004 with Dissolve(0.5)
    k "好呀~~~ 我觉得自己体能退步了。"
    l "我可不这么觉得。你瘦得像根竹竿。"
    scene c003_s013_005 with Dissolve(0.25)
    k "我以前跑得好多了。现在姿势全毁了。可你拼命跑的时候，谁还顾得上姿势。再说我也想把体力练回来。"
    l "以防我们要在外面待更久？"
    k "我突然想到，我们可能得去比办公室到这儿更远的地方。在对我们的情况了解更多之前，很难说那到底是多远。"
    scene c003_s013_006 with Dissolve(0.25)
    l "*叹气* 对。我得跟[player_name]谈谈进楼上那些办公室的事。要能看见外面的那种。不过以后再说。我起来的时候他还在睡。"
    k "……好。"
    l "我开电视你不介意吧？"
    scene c003_s013_007 with Dissolve(0.25)
    k "你找到遥控器了？"
    l "是[player_name]找到的。不过昨天收到的全是雪花。我还指望能有信号呢。"
    scene c003_s013_008 with Dissolve(0.5)
    l "唔嗯~~~ 什么都没有。"
    k "开着吧。我们锻炼的时候有点白噪音也不坏。"
    scene c003_s013_009 with Dissolve(0.25)
    l "也是。没有大自然的声音好。也没有音乐好。"
    k "以前跑步的时候我戴耳机。训练的时候。"
    scene c003_s013_010 with Dissolve(0.25)
    l "我一直都没有什么固定流程——"
    tv "{i}*噼啪*……民防……{/i}"
    scene c003_s013_011 with Dissolve(0.25)
    l "嗯？你听到……"
    k "我也听到了。"
    scene c003_s013_012 with Dissolve(0.25)
    tv "{i}……警告不要……受影响区域……{/i}"
    l "受、受影响区域？"
    tv "{i}……仍无解释……隔离区……推测死亡人数……{/i}"
    if persistent.ch3_complete == False:
        $ persistent.ch3_complete = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_chapter3", transition=slideright)()
        pause
        $ Hide("achievement_chapter3", transition=dissolve)()
        $ quick_menu = True
    scene blank with Dissolve(2)
    stop music fadeout 2.0
label chapter04:
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("chapter04", transition=Dissolve(1.0))()
    pause
    $ Hide("chapter04", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c004_s001_001 with Dissolve(2)
    play music horror fadein 2.0
    if ch3_laura_sex == "yes":
        "好吧，我不能说自己已经在这儿安顿下来了，但连续两晚我都睡得还不错。当然，我可以把这归因于我们这两天都很忙、都在外面——还跟劳拉狠狠干了一场——但能一觉睡到天亮，总比另一种结果好。"
        "不过说真的，用做爱这种方式累到昏昏沉沉，也不算最坏，只是不指望再来一次。劳拉说得很清楚，那是一次性的事。她没说后悔，只说我们应该假装它没发生过。"
        scene c004_s001_002 with Dissolve(0.25)
        "这基本就等于说「靠，我们不该那么干」。"
    else:
        "好吧，我不能说自己已经在这儿安顿下来了，但连续两晚我都睡得还不错。当然，我可以把这归因于我们这两天都很忙、都在外面，但我能一觉睡到天亮，总比另一种结果好。"
        scene c004_s001_002 with Dissolve(0.25)
    "好了，该动起来看看今天有什么事要做了。我敢肯定我们在这儿待不了太久，但趁现在还是好好利用这个地方。"
    scene c004_s001_003 with Dissolve(0.25)
    l "{size=32}[player_name]！[player_name]！你在哪儿！？{/size}"
    "操。劳拉在喊，说明出事了。"
    j "劳拉？怎么了？"
    scene c004_s001_004 with Dissolve(0.5)
    l "你在这儿。跟我来。健身中心那台电视。我们收到了一部分信号。"
    j "信号？什么？哦，靠！真的？"
    scene c004_s001_006 with Dissolve(0.25)
    l "对。来。快来。趁还没丢。"
    j "播的是什么？"
    scene c004_s001_005 with Dissolve(0.25)
    l "看着像新闻广播。"
    scene blank with Dissolve(2)
    scene c004_s001_007 with Dissolve(2)
    j "卡莉，还在吗……"
    scene c004_s001_008 with Dissolve(0.25)
    k "没了。可能不到一分钟前就断了。"
    l "靠。这已经是第二次了。再这样下去，你们会以为我们是骗子。"
    menu:
        "[gr]我相信你们。\n[rgr](卡莉 焦虑 -1)":
            $ k_anxiety -= 1
            j "就算我昨天没跟那怪物正面碰上，我也相信你们。"
        "你逗我呢。":
            j "你是在逗我，对吧？*轻笑*"
            l "没有。*呻吟*"
    scene c004_s001_009 with Dissolve(0.5)
    j "那到底播了什么？能听出什么吗？"
    l "就像我说的，像是新闻广播。他们提到了隔离区，还提到国民警卫队。"
    k "我、我觉得可能是全国性的电视广播。我没认出台上那个女人的声音。就是说话的那个。"
    scene c004_s001_010 with Dissolve(0.25)
    l "所以不是本地新闻台。"
    k "不，我觉得不是。但他们提到某个区域被封锁。还让大家不要试图进入那个区域。"
    scene c004_s001_011 with Dissolve(0.25)
    j "所以不是全国性的。姑且算是一点安慰吧。"
    "对劳拉来说，这让彼得没有同样受波及有了一丝希望。"
    scene c004_s001_012 with Dissolve(0.25)
    l "还、还有别的吗？"
    k "没什么了。信号断得很碎，我没听清多少完整的句子。不过……"
    scene c004_s001_013 with Dissolve(0.25)
    l "嗯？是什么？"
    k "她把那段消息重复了一遍。"
    j "是重播的摘要？还是循环播放的广播，警告全国其他地方的人别靠近那个区域？"
    scene c004_s001_014 with Dissolve(0.25)
    k "我不知道。没听到足够多的内容，判断不出比刚才说的更多。"
    l "没关系。我们现在知道的比之前多了。我们应该……应该先让电视开着。以防万一。"
    scene c004_s001_015 with Dissolve(0.25)
    l "我们应该……"
    j "去四处看看，看能不能进楼上某些办公室？也许能看清周围几个街区？这样我们就能更好地判断现在的情况？"
    scene c004_s001_016 with Dissolve(0.25)
    l "对，就是这个。你找到钥匙了吗？"
    j "还没。不过必要的话，我还有「老砍柴」。"
    k "「老砍柴」？"
    scene c004_s001_017 with Dissolve(0.25)
    l "果然还是要靠一个男人才给武器起名字。"
    j "武器、车子、飞机、轮船。你得给它们起名字。通常是女孩子的名字。"
    "我们也喜欢给生殖器起名，不过这个现在不适合聊。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_24_1020", transition=Dissolve(1.0))()
    pause
    $ Hide("june_24_1020", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday2 fadein 2.0
    scene c004_s001_018 with Dissolve(2)
    "我们其实没什么作战计划。更像是「嘿，我们四处看看能做点什么」。我觉得她们听到的那点广播内容已经足够让她们不安了，哪怕那也为我们的处境提供了一些背景。"
    scene c004_s001_019 with Dissolve(1)
    "我不想根据二手听来的消息下什么结论，但那似乎确实印证了我的推测：这件事可能是局部的。"
    scene c004_s001_020 with Dissolve(1)
    l "嘿。有进展吗？"
    j "呃，还没有。这儿又不是我的办公室，我完全不知道有用的东西会放在哪儿。靠，我甚至不知道在{b}我自己的{/b}桌上乱七八糟的东西都在哪儿。给我点时间，我也许能翻出点什么。"
    scene c004_s001_021 with Dissolve(0.5)
    l "抱歉，我只是……我不是想催你。"
    j "没关系。我知道大家都绷得有点紧。那点消息大概也搅起了不少情绪。我的意思是，你怎么看待这件事？"
    scene c004_s001_022 with Dissolve(0.25)
    l "我不知道该怎么看待。它让我相信隔离区之外的地方一切「正常」。而我们不知怎么就被困在了里面。所以我的疑问更多了。"
    j "而且我觉得短时间内是不会有答案的。也许我们运气好，电视能再收到点什么。说到这个，卡莉留下来听了吗——"
    scene c004_s001_023 with Dissolve(0.25)
    l "没有。我让她去检查那些办公室的门了。看看哪些我们还没查过。我不想让她坐在那儿死盯着电视。就算可能我们该有一个人守着听。"
    j "就算看不清楚，区别也是有的。所以也许我们每个人都该轮流来，免得其他人钻牛角尖。这整件事可能会养成坏习惯甚至更糟，但我们得在获取消息和其他所有事之间找平衡。我们会有办法的。"
    l "对，我知道。"
    scene c004_s001_024 with Dissolve(0.25)
    j "靠。这儿我什么有用的都没找到。钥匙可能在谁那儿，那人说不定带回家了。"
    l "该死。我们就没个顺的时候，是吧？"
    scene c004_s001_025 with Dissolve(0.25)
    j "也没那么糟。我去拿斧子，要是有必要，就砍掉几个门把手。走，看看卡莉找到了什么。"
    l "好。"
    scene blank with Dissolve(2)
    scene c004_s001_026 with Dissolve(2)
    "我不能怪劳拉被这事影响。她本来就因为婚姻的问题压力不小。睡眠不足、吃不上正经饭、还担心儿子，这些大概已经让她绷到了极限。"
    scene c004_s001_027 with Dissolve(0.5)
    menu:
        "[gr]跟她谈谈这件事。\n[rgr](劳拉 焦虑 -1)":
            $ l_anxiety -= 1
            scene c004_s001_029 with Dissolve(0.5)
            j "嘿，我知道你绷得很紧，但外面还有人没受影响，这总归是好事。靠，这说明你儿子在这一切里是没事的。"
            l "是吗？"
            scene c004_s001_030 with Dissolve(0.25)
            j "他在佐治亚州。我们离得并不近，既然他们动用了国民警卫队封锁一片区域，那肯定不会蔓延到好几个州去。"
            if l_friend >= 5:
                scene c004_s001_031 with Dissolve(0.25)
                l "*叹气* 你说是就是吧。不过还是谢谢你愿意试。"
                "谁知道我说得对不对？到了这一步，我只能撒个小谎，让她好受一点。"
                scene c004_s001_032 with Dissolve(0.25)
                l "*叹气*"
                "我能感觉到她身体里的紧绷。她在试着放松，却没能做到。要是她不试着松下来，这会把她压垮。我担心压力和未知会让她崩溃，如果我不帮她想办法应对。"
                if ch3_laura_sex == "yes":
                    scene c004_s001_033 with Dissolve(0.5)
                    "而且，我不想再回到那个话题，但也许她需要一点身体上的释放。就当是转移注意力。算了，这不过是我用鸡巴思考罢了，因为天啊，我真想再要她一次。"
                    "我得提醒自己，那只是一瞬间的判断失误，绝不能再有下次。"
                    scene c004_s001_034 with Dissolve(0.25)
                    "*叮*"
                    "好了，我们到了。"
            else:
                l "*叹气* 你说是就是吧。"
        "也许不是。":
            "也许我就那么放过了。我们不可能老聊这些。她得被人劝出来。昨晚我们确实已经谈得挺动情了。"
            scene c004_s001_028 with Dissolve(0.25)
            "我们做点只属于此时此刻的事怎么样？进那些房间。看看能不能看清周围。我们得对接下来怎么办做出些决定。"
    scene blank with Dissolve(2)
    scene c004_s002_001 with Dissolve(2)
    "拿起那把消防斧之后，劳拉和我在三楼停了一下。发现卡莉不在，我们就继续往上走。"
    scene blank with Dissolve(2)
    scene c004_s002_002 with Dissolve(2)
    "我们发现她在这层楼背面的一扇办公室门附近徘徊。"
    scene c004_s002_003 with Dissolve(0.25)
    k "有收获吗？"
    l "钥匙方面一无所获。"
    scene c004_s002_004 with Dissolve(0.25)
    j "我可以再试一次，不过既然我手里有这件顺手的开门工具，我就不打算花太多时间。尤其那钥匙可能根本不在楼里。"
    k "唔……好吧，这扇门锁着，你要试试吗。"
    scene c004_s002_005 with Dissolve(0.25)
    j "当然。我在这儿献上我模仿{a=https://en.wikipedia.org/wiki/Paul_Bunyan_and_Babe_the_Blue_Ox}保罗·布尼恩{/a}的全力表演。"
    l "别伤着自己。"
    j "知道知道。话说回来，你最好退后一点。以防万一。"
    scene c004_s002_006 with Dissolve(0.25)
    j "然后……"
    play sound woodchop
    scene c004_s002_007 with vpunch
    "*咔——咚*" with vpunch
    scene c004_s002_008 with Dissolve(0.25)
    j "好，这比我预想的结实多了。再来一次。"
    scene blank with Dissolve(2)
    scene c004_s002_009 with Dissolve(2)
    j "*呻吟* 唔嗯~~~"
    l "你没事吧？"
    scene c004_s002_010 with Dissolve(0.25)
    j "没事。我猜我劈柴的那块肌肉还没活动开。我觉得没拉伤，但前臂肯定会有感觉。"
    k "所以，这就是……"
    scene c004_s002_011 with Dissolve(0.25)
    l "空的。看样子他们已经清空了。而且没有窗户。这地方就是一座坟墓。"
    j "有点失望，不过我也说不好自己原本期待找到什么。整栋楼就是某种血汗工厂恐怖故事。"
    scene c004_s002_012 with Dissolve(0.5)
    j "我大概可以翻翻抽屉。找什么？橡皮筋吗？"
    k "唔嗯~~~"
    l "你还好吗？"
    scene c004_s002_013 with Dissolve(0.25)
    k "就是这件傻衬衫。它当然挺可爱，可也太大了，我一半时间都在忙着不让它滑下去。"
    l "也许我们晚点可以再去翻一次储物柜？"
    scene c004_s002_014 with Dissolve(0.25)
    k "对，那倒不错。"
    j "好，这纯粹是浪费时间。"
    scene c004_s002_015 with Dissolve(0.25)
    l "那我们去下一扇锁着的门吧。看看你的胳膊还撑不撑得住。"
    j "我觉得我还能再来一下。*轻笑*"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_24_204", transition=Dissolve(1.0))()
    pause
    $ Hide("june_24_204", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c004_s002_016 with Dissolve(2)
    play music insideday fadein 2.0
    j "好，往下两间房，什么好东西都没有。我就不该抱太大希望。看起来他们真的把这里大部分东西都搬空了，只剩下空的隔间和几张桌子。让我怀疑他们是不是打算回来再搬剩下的。"
    l "据我所知，这地方关掉也没多久。他们可能把一些东西留在这儿，指望哪天能原样转卖给别的有意向的买家。不过考虑到这里都快成鬼城了，我不确定还能有什么人会感兴趣。"
    scene c004_s002_017 with Dissolve(0.25)
    j "只要价钱合适，嘛。"
    l "再说了，你到底期待找到什么？我只是想进这些房间，看看能不能看清周围几个街区。"
    scene c004_s002_018 with Dissolve(0.25)
    j "任何有用的东西。我们已经到了得四处搜刮的阶段了，劳拉。食物。武器。补给。你永远说不准。再来一个打火机或者手电筒也不坏。靠，我该回保安室看看能不能再找出一个手电筒。"
    l "以后吧，[player_name]。现在不行。"
    k "……"
    scene c004_s002_019 with Dissolve(0.25)
    j "知道，知道。"
    l "卡莉？"
    k "抱歉。来了。"
    scene blank with Dissolve(2)
    scene c004_s002_020 with Dissolve(2)
    play sound woodchop
    "*咔——咚*" with vpunch
    j "{size=30}成了。{/size}"
    scene c004_s002_021 with Dissolve(0.5)
    j "好，我现在对消防员和伐木工人多了几分敬意。还有那些选择住在林子里、砍柴，好让自己夜里暖和过冬的家伙。"
    k "哦哦！看。"
    scene c004_s002_022 with Dissolve(0.5)
    l "窗户。我这辈子从没有这么开心见到过窗户。要说多可怜，这话一点也不假。"
    j "连你自己盖房子的时候也没有？"
    l "盖房子那会儿，窗户连我最想做的决定前十都排不上。我更关心的是厨房台面和卧室的顶角线。那才是女士们更操心的事。对吧，卡莉？"
    scene c004_s002_023 with Dissolve(0.25)
    k "我、我……我是租的。其实那是安德鲁的公寓。我跟他一起搬进来的，所以房子的样子我没太多选择。"
    l "等你搬到下一个家就会变了。"
    k "你说是就是吧。"
    l "好吧，看看我们能看到什么。"
    scene c004_s002_024 with Dissolve(0.5)
    j "唔……雾的上方似乎有一层{a=https://en.wikipedia.org/wiki/Cloud_top}云顶{/a}。我们在几楼？六楼？"
    l "对。六楼。这有戏。"
    k "云顶？"
    scene c004_s002_025 with Dissolve(0.25)
    l "就是高度足够、能越过云层看到上面的地方。或者在这个情况下，是越过烟尘的顶部。或者雾。或者随便什么。通常你坐飞机的时候会看到。"
    k "知道这个对我们有什么用吗？"
    j "这意味着如果有可能救援，救援可能会以直升机从楼顶把人撤走的形式出现。"
    scene c004_s002_026 with Dissolve(0.25)
    l "前提是他们知道我们在这儿。"
    k "那医院的停机坪呢？安德鲁说过，那在校园里最高的那栋楼上。"
    l "医疗中心会是把撤离者送出城里的明智选择。如果我说了算，我就会这么办。"
    menu:
        "不过这儿确实看不了那么远。[yl]":
            j "不过这儿确实看不了那么远。"
            scene c004_s002_027 with Dissolve(0.25)
            l "在那个方向，几英里外，校园的另一头。对我们来说是一段苦路。"
            j "如果我们能确认当局确实派了救援车过来，我看不出有什么理由不值得一试。"
        "我们可以试试往那边走。[yl]":
            j "我们可以试试往那边走。这是我们目前最好的主意。"
            scene c004_s002_027 with Dissolve(0.25)
            l "我也这么想。在那个方向，几英里外，校园的另一头。对我们来说是一段苦路。"
    k "医院……唔嗯……"
    scene c004_s002_028 with Dissolve(0.5)
    j "好吧，现在我们有能看风景的窗户了，这不错。我得说，真没想到这儿有间会议室。这地方给我的感觉是「丢日结临时工」而不是「高管窝」的地方。我猜以前这里大概也坐过个副总裁或者总监。"
    scene c004_s002_029 with Dissolve(0.25)
    k "家具上都是灰。我觉得这儿没怎么被用过。"
    l "这种地方本来可能定位更高，后来公司要削减人力成本，就慢慢变成了呼叫中心。无论如何，其实也无所谓。"
    j "电视加上这个，我们大概能拼凑出自己处境的些许轮廓。"
    scene c004_s002_030 with Dissolve(0.25)
    l "我也这么觉得。我……"
    menu:
        "[rd]你们想坐着看吗？\n[rrd](劳拉 焦虑 +1)":
            $ l_anxiety += 1
            j "你们想坐着看吗？看看会不会有什么进展？"
            scene c004_s002_031 with Dissolve(0.25)
            l "眼下还能做什么？我需要知道外面有没有人。现在我没看到什么能告诉我外面世界还好，也没看到他们在拼命想办法帮我们。"
            scene c004_s002_032 with Dissolve(0.25)
            j "好吧，记得休息。"
            "因为老盯着这个不是好事。我们都绷得太紧了，心理健康现在是真问题。"
        "整天待在这儿可能不健康。\n[rgr](劳拉 信任 +1)":
            $ l_trust += 1
            j "好吧，先听我说完：我知道你可能想整天坐在这儿盯着外面，但一直放不下这件事可能并不健康。"
            scene c004_s002_031 with Dissolve(0.25)
            l "那我们眼下还能做什么？我需要知道外面有没有人。现在我没看到什么能告诉我外面世界还好，也没看到他们在拼命想办法帮我们。"
            scene c004_s002_032 with Dissolve(0.25)
            j "我只是说……"
    k "我们可以轮流来盯这个和电视。"
    scene c004_s002_033 with Dissolve(0.5)
    l "*叹气* 也行。"
    j "再说了，我们还得吃饭什么的。这样吧，我去把昨天带回来的东西热一下。我已经饿得前胸贴后背了。"
    k "我、我是能吃点的。"
    scene c004_s002_034 with Dissolve(0.25)
    "我们一天只吃一顿（还靠离开办公室前搜刮的剩货凑合），这撑不下去，但眼下我也不想把这事挑明。尤其不是对着劳拉那样的时候。"
    l "我……我……"
    scene c004_s002_035 with Dissolve(0.25)
    k "我给你拿点来。"
    l "那我就谢谢了。我不会整天待在这儿，不过趁还有天光，也许能发现点什么。"
    j "当然。记得休息，好吗？"
    scene c004_s002_036 with Dissolve(0.25)
    l "会的。我保证。"
    "劳拉够倔，我想就算我想硬把她拉开也做不到。她需要某种确认，确认她儿子平安无事，哪怕他在另一个州。至于她丈夫呢？"
    "尽管他们的婚姻一路坎坷（听起来他们可能正处在离婚前的阶段），她还是在乎基思。"
    scene c004_s002_037 with Dissolve(0.25)
    "而卡莉则一定会喜欢「我们去医院」这个提议。或者说，这个暗示：医院是个合理的撤离点。如果真是这样，她并没有把如释重负或喜悦表露出来。我想她把一切都憋着，独自消化。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_24_532", transition=Dissolve(1.0))()
    pause
    $ Hide("june_24_532", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain fadein 2.0
    scene c004_s003_001 with Dissolve(2)
    l "钥匙就在桌上，跟[player_name]说的一样。他也说了他没把储物柜全翻过，所以只能指望了。"
    scene c004_s003_002 with Dissolve(0.25)
    k "谢谢这个。我……这个睡觉挺舒服，而且除非我们得出门，我也不想再穿回原来那身衣服，可我需要点什么……{i}别的{/i}。"
    scene c004_s003_003 with Dissolve(0.5)
    k "要那种我每次弯腰都不会有奶子蹦出来的衣服。"
    l "*笑* 哦，这种恐惧我以前有过。几年前我买过一条参加活动的裙子，我的两个「女儿」不止一次威胁要从里面冒出来。"
    scene c004_s003_004 with Dissolve(0.25)
    l "来，看看我们能挖出什么。"
    k "好、好吧……"
    scene c004_s003_005 with Dissolve(0.25)
    "{color=#66ff33}我分不清卡莉是抑郁了还是只是安静。她身上压着很多焦虑——联系不上家人，也联系不上安德鲁——也许她需要有人陪她说说话。或者陪她聊点开心的事。{/color}"
    "{color=#66ff33}再说了，我其实也想听到有人说自己现在的感情关系还不错。这方面，我和[player_name]都算不上什么正面榜样。{/color}"
    scene c004_s003_006 with Dissolve(0.5)
    l "那，卡莉，跟我说说你和安德鲁是怎么认识的吧。我好像从来没听过这个故事。"
    k "哦？我……其实没什么好听的。"
    scene c004_s003_007 with Dissolve(0.25)
    l "别嘛。我很想听。现在我们有的是时间聊天，不用被工作打断。"
    k "好、好吧。那时候我住在北边，在一家咖啡店工作，他经常过来。我觉得他挺帅的。他每次来都穿一身看着就很体面的商务装，我记得他好像在附近的办公室上班。"
    scene c004_s003_008 with Dissolve(0.25)
    l "哦，那可真方便。"
    "{color=#66ff33}那时候他还在上大学吗？{/color}"
    scene c004_s003_009 with Dissolve(0.25)
    k "他来得特别勤。*咯咯笑* 我觉得他肯定知道我的排班。主要是夜班和周末。"
    l "那时候你在上学吗？"
    k "我们开始交往的时候，我刚上大学一年级。"
    scene c004_s003_010 with Dissolve(0.25)
    l "呃……好吧。我猜他挺会甜言蜜语，而且挺执着。"
    k "他确实很爱调情。夸奖个不停，还会在那儿留下一些小礼物。"
    scene c004_s003_011 with Dissolve(0.5)
    l "那你们怎么搬到南边来的？"
    k "他拿到了一个工作邀请。他原来那份工作干了五年，一直没什么起色。而且他公寓的房租越来越吃不消了。"
    scene c004_s003_012 with Dissolve(0.25)
    "{color=#66ff33}五年？卡莉看着也就二十三四岁，她说她是在大学认识他的，而他那时已经在工作了。这笔账我算不太过来。也许是我理解得不对，但我总觉得这里头有一两个危险信号。{/color}"
    scene c004_s003_013 with Dissolve(0.25)
    k "哦，找到了。这个看着不错。还行。你……要不……"
    l "对我来说太小了。我会被挤在里面，得拿鞋拔子把我撬出来那种。我的屁股会把布料撑到危险的程度。我再找找别的。"
    k "我、我去试穿一下。看看合不合身。"
    scene c004_s003_014 with Dissolve(1)
    l "那你的父母住哪儿？在这附近吗？还是……"
    k "没有，他们还在纽约州北部。所以要是[player_name]说得没错，他们应该没事。我真的很想让他们知道我平安。等这一切结束之后，我也想更常去看他们。也许别只在节日的时候去。"
    scene c004_s003_015 with Dissolve(0.25)
    k "*叹气* 真难受，到现在我们也就只负担得起去一两天，而且总是在很赶的情况下，没待多久就得回来。我觉得自己已经没什么时间跟任何人好好说话了。"
    scene c004_s003_016 with Dissolve(0.25)
    "{color=#66ff33}我……我该跟[player_name]提一下。确认自己不是疑神疑鬼、不是理解错了。可能只是我那过度保护的「母性」让我误读了这些。{/color}"
    k "你找到什么了吗？"
    l "找到了，不过感觉有点{a=https://www.imdb.com/title/tt0078607/}《危险蠢蠢欲动》{/a}。"
    scene c004_s003_017 with Dissolve(0.25)
    k "我……我不知道那是什么。"
    l "谢谢你让我觉得自己老了。"
    scene c004_s003_018 with Dissolve(0.25)
    k "也没比安德鲁老多少。"
    l "他、他多大？"
    k "34 岁。呃，七月就 35 了。"
    scene c004_s003_019 with Dissolve(0.5)
    k "你找到的那件能穿吗？"
    l "换个风格？行吧。"
    scene c004_s003_020 with Dissolve(0.5)
    k "哦，那不错。"
    l "谢谢你愿意试。*咯咯笑* 而且很适合你。"
    scene c004_s003_021 with Dissolve(0.25)
    k "对，我也觉得。屁股那儿有点紧，不过还能忍。"
    scene c004_s003_022 with Dissolve(0.25)
    l "你的屁股很翘，别太担心。"
    k "*咯咯笑* 好吧。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_24_748", transition=Dissolve(1.0))()
    pause
    $ Hide("june_24_748", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain2 fadein 2.0
    scene c004_s004_001 with Dissolve(2)
    k "*叹气*"
    "{color=#ffcccc}电视还是没信号。之前我们运气好，捞到了那点广播内容。但坐在这儿期待点什么也不亏。哪怕只有一丁点来自外面的信息，也比一片寂静强。{/color}"
    "{color=#ffcccc}还能做什么？睡觉？在楼里到处走看看剩下什么？连能读的东西都没了。哪怕是办公室里那种无聊的公司读物都没有。比如米奇以前放在办公桌后面的那些。也没有电脑可以玩。{/color}"
    scene c004_s004_002 with Dissolve(0.25)
    "{color=#ffcccc}所以我们是在谈去医院。我本该为我们考虑到了这个而高兴。这给了我们一个明确的方向。可那绝对不是一段近距离的路。我们怎么过去？哪怕只是走两个街区都够危险。我不确定我们要怎么走完好几英里。{/color}"
    scene c004_s004_003 with Dissolve(0.5)
    "{color=#ffcccc}那安德鲁呢？他应该在那儿。我本该为能再见到他而激动。或者至少该有点什么感觉。可劳拉……我们刚才聊起怎么认识的时候，我只是觉得……{/color}"
    "{color=#ffcccc}我不知道。我听见自己那么说的时候，感觉完全不一样。刚认识的时候，我觉得自己很特别、很重要。可跟她解释这件事，只让我觉得有什么地方不对劲。我不该对自己的未婚夫有这种感觉，对吧？{/color}"
    scene c004_s004_004 with Dissolve(0.25)
    "{color=#ffcccc}就好像我跟他失联越久，怀疑就越深。而且我已经有好几天没给任何人发消息、打电话了，这更没帮上忙。{/color}"
    scene c004_s004_005 with Dissolve(0.5)
    "{color=#ffcccc}还有我的手机？我……我太习惯随时能用了，失去它就……就像上瘾一样留下一个空缺，非得把它拿回来不可。但我意识到，过去这一年左右，我基本就是靠发消息跟朋友和家人联系的。{/color}"
    "{color=#ffcccc}而这……这不太好，对吧？{/color}"
    "{color=#ffcccc}真傻，我居然希望有网络能查一下，看看这种感觉叫什么名字。{/color}"
    scene blank with Dissolve(2)
    scene c004_s005_001 with Dissolve(2)
    "真不知道为什么我还在这儿巡楼。这又不是什么丧尸末日，用不着确认没有东西跑进楼里。一楼那扇门我们已经堵上了，电梯也停用了。所以要是有人或者什么东西找过来，它们很难靠近我们。"
    "真正要担心的是别让那些雾渗进来。我们到的时候空调是关着的，这很好。能碰到的通风口我们也全封上了。这里还不算完全密闭，但眼下够用了。"
    scene c004_s005_002 with Dissolve(0.25)
    "我想我只是在四处闲逛，因为无聊，也不想打扰别人。卡莉大概已经受够了人多的场面，而劳拉看起来在消化自己婚姻的状况，以及我们出去之后她该怎么办。前几天那番谈话希望有点用。"
    if ch3_laura_sex == "yes":
        "你知道……在我们上床、把事情搞得比本来复杂得多之前。我敢肯定她会把这当成高压之下的一种解压。"
    scene blank with Dissolve(1)
    scene c004_s005_003 with Dissolve(1)
    "有电视和会议室的窗户在，我们就有两种了解外面情况的途径。我唯一担心的是，这两样都可能变成卡莉和劳拉钻牛角尖的对象。"
    "她们两个都拼命想抓住任何一点外面世界的线索——任何能给她们希望的蛛丝马迹——结果可能就整天坐着等一个信号，无论那信号多小。"
    scene c004_s005_004 with Dissolve(0.25)
    "这本来也不该由我来管她们，所以我想我只能不时插一句，提醒她们休息，哪怕这意味着我替她们顶上。"
    scene blank with Dissolve(1)
    scene c004_s005_005 with Dissolve(1)
    "可悲的是，这可能只是因为她们有想见的人。而我呢？离婚之前我就已经跟很多人断了联系。除了家人，我工作之外的社交圈基本不存在。这不意味着我想死在这儿，但我对「跟外面的世界重逢」也没什么强烈的冲动。"
    scene c004_s005_006 with Dissolve(0.25)
    "*叹气* 我饿了。不知道还剩多少吃的，但我觉得我们很快得再去一趟。要是接下来我们决定做的事需要用到那儿，那可能就是最后一趟了。希望我们那位怪物朋友正躲在某个角落舔伤口。最好已经死了。如果还没有……我也不知道。看来我得准备好再跟它干一场。或者拼命逃命。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_25_814", transition=Dissolve(1.0))()
    pause
    $ Hide("june_25_814", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music officemain fadein 2.0
    scene c004_s006_001 with Dissolve(2)
    "整整六层楼，就一个茶水间，还是这个。而且它连「房间」都不算，是个塞了咖啡机和微波炉的壁橱。这地方简直是上班地狱。关掉它说不定反而是件好事。"
    scene c004_s006_002 with Dissolve(0.5)
    k "哦，嘿。早上好。"
    j "早上好，卡莉。"
    "换了身新衣服。我猜她昨天某个时候去「逛街」了。要是她不喜欢我挑的那些，我也不会往心里去。那件确实比她愿意露出来的露得多。"
    menu:
        "说点什么。\n[rgr](卡莉 好感 +1)":
            $ k_friend += 1
            scene c004_s006_003 with Dissolve(0.5)
            j "看来你的衣柜升级了。穿着挺舒服。"
            scene c004_s006_004 with Dissolve(0.25)
            k "呃，对。它……它更合身。不是说我有多不领情，之前那件挺适合睡觉的，可是……"
            j "没事，我不介意。嘿，来杯咖啡吗？我刚煮了一壶。"
        "什么都别说。":
            scene c004_s006_003 with Dissolve(0.5)
            "不用。什么都别说。这样本来就有点尴尬，别让它变得{b}真的{/b}尴尬。"
            j "嘿，来杯咖啡吗？我刚煮了一壶。"
    scene c004_s006_006 with Dissolve(0.25)
    k "我就说怎么闻到了。你找到什么了？我往冰箱里放东西的时候看到过这个，但没想到这儿还剩着咖啡。我还以为他们全拿走了。"
    j "对，我在那边柜子后面翻出了半袋。不知道放多久了，而且是 Folgers 的，所以肯定比不上我们在办公室喝的那些，但凑合能喝。我以前都没意识到我们那儿的有多好喝。"
    scene c004_s006_003 with Dissolve(0.25)
    j "说实话，这地方挺让人沮丧的。我知道以前我开玩笑说过我们——你、我和奥蒂斯——是给老板卖命的奴隶，但眼前这个可比那惨多了。算是开了个眼。"
    scene c004_s006_007 with Dissolve(0.25)
    k "环球办公用品是我第一份办公室工作，所以我大概以前不知道自己有多被惯着。"
    j "既然你这么说，我倒是一直隐约知道你以前在咖啡店干过，但我不知道你还有餐饮业的经验。还是说，北边的咖啡店也卖汉堡和薯条？"
    scene c004_s006_008 with Dissolve(0.25)
    k "哦。我们不卖。只有咖啡、玛芬蛋糕之类的东西。不过我有几个朋友是干这行的。凯利·奥曼在我妈家楼下不远处的汉堡王上班。不止一次，我都在后厨等她下班，然后我们一起出去玩。"
    j "所以你看着他们干活也学了点东西？不是说你不会做饭什么的。但知道怎么用那些设备，我挺佩服的。"
    scene c004_s006_009 with Dissolve(0.25)
    k "其实就是知道按钮和旋钮在哪儿。还有厨具。还有他们把东西放在哪儿。我又没在忙午餐高峰。"
    scene c004_s006_010 with Dissolve(0.5)
    k "我，呃……我在想……你觉得我们得多久去一次？去{i}汉堡店{/i}？我知道我们大概明天就得去，对吧？我们剩的东西不多了。"
    j "我想撑到今天没问题。所以对，明天。之后呢？谁知道。我希望我们能开始想想接下来去哪儿，以及到了之后吃的从哪儿来。"
    scene c004_s006_011 with Dissolve(0.25)
    k "……"
    menu:
        "你想留在这儿也行。\n[rrd](卡莉 好感 -1)":
            $ k_friend -= 1
            j "你想留在这儿也行。只要告诉我怎么用我需要的东西，剩下的我自己来。"
            scene c004_s006_012 with Dissolve(0.25)
            k "不，不。我……我做不了这个不。我想做点什么。我不能一直害怕下去。"
            "我想告诉她，她不需要「有用武之地」。但我觉得卡莉比我最初以为的更有主意。她和劳拉也许比自己意识到的更像。"
            j "好好好，我不会把你一个人撂下。我只是提一下。"
            scene c004_s006_013 with Dissolve(0.25)
            k "谢谢。我……就是，谢谢。"
        "我可以试着搬尸体。\n[rrd](卡莉 焦虑 +1)":
            $ k_anxiety += 1
            j "你要是愿意，我可以试着把尸体搬走。这不会让劳拉高兴，但她得放下「我们还得守规矩」这个念头。我们现在是在「无人区」了。有些事就是得做。"
            scene c004_s006_012 with Dissolve(0.25)
            k "不只是尸体的问题。是外面那个东西。我……我不想再撞见它。上次我们遇上它的时候，我怕得要死。"
            j "它要是有点自保意识，我敢肯定挨一斧子够它受的。靠，我甚至敢打赌我们能在哪个水沟里发现它躺着流血。你别说我，反正我自己是挡不住斧子的。"
            scene c004_s006_013 with Dissolve(0.25)
            k "你说是就是吧。"
    scene c004_s006_014 with Dissolve(1)
    j "说到出门，你觉得劳拉出去怎么样？我是说，我打算让她自己决定，不过我觉得她不会想留在这儿等我们。"
    k "我们可以建议她在这儿多休息一会儿。尤其是如果你觉得我们很快就要动身。让她把自己调整好，为我们计划好的那次撤离做准备。等我们决定了具体怎么办。"
    scene c004_s006_015 with Dissolve(0.25)
    j "对，说「我们去医院」跳过了「怎么去」。不过我们有几天时间理清。所以，谁去跟她说这事？"
    k "呃……"
    menu:
        "不是我。[yl]":
            j "不是我！" with hpunch
            scene c004_s006_016 with Dissolve(0.25)
            k "啊啊啊~~~ 好吧。*咯咯笑*"
        "让她先说。[yl]":
            k "我能搞定。她不太会反驳我。"
            scene c004_s006_016 with Dissolve(0.25)
            j "我也这么想。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_25_120", transition=Dissolve(1.0))()
    pause
    $ Hide("june_25_120", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday fadein 2.0
    scene c004_s007_001 with Dissolve(2)
    "这地方这么大，我有种感觉，要是我不主动找找，一天下来可能见不到劳拉和卡莉中的任何一个。尤其现在我们都各自有了自己那块能钻牛角尖的小天地：卡莉守着电视，劳拉待在有窗户的会议室，我呢，挨间搜刮办公室。"
    "反正也没别的事可做，我不如继续翻翻这地方剩下的东西。看这情形，这里好像并没有完全关掉。或者说，至少最近才关的。也许几周前这儿还有几个人在。"
    scene c004_s007_002 with Dissolve(0.25)
    "无论如何，其实也无所谓。我应该多想的是我们的下一步。我{b}应该{/b}。"
    "可是……我们现在掌握的信息还不足以做出明智的决定。事实上我们可能永远也不够。我们也许只能收拾东西就走人。找个近一点的地方，然后冲出去。"
    scene c004_s007_003 with Dissolve(0.5)
    "这是什么？一张门禁卡。唔……停车场通行？我百分之百确定这里所有员工都是停在跟我们之间那个大停车场里的。而那不需要门禁卡。"
    scene c004_s007_004 with Dissolve(0.25)
    "这就引出几个我很想知道的问题。比如这个车库里哪儿呢。这味道一看就是高管专用车位。在附近吗？也许是地下的？那电梯可到不了那儿。"
    "我可以去看看。反正我也有时间。也许我带上装备，在大堂那边翻翻，看看有没有我之前漏掉的东西。"
    scene blank with Dissolve(2)
    scene c004_s007_005 with Dissolve(2)
    "我知道自己一开始想把这件事往后拖，但我得克制那种「以后再说」的冲动。我们的处境不会随时间变好。而且在搞清楚之前，我不想先跟其他人提起。"
    "要是最后没结果，最好别先让她们的期待空欢喜一场。所以，来看看这附近有没有我之前没注意到的东西。"
    scene c004_s007_006 with Dissolve(0.25)
    "我得说，外面看不到我们那位变异朋友四处游荡，这还挺让人松了口气的。至少——要是他还活着的话——他没跟着我们回家。或者就算跟了，他也没本事进来。"
    scene blank with Dissolve(2)
    scene c004_s007_007 with Dissolve(2)
    "好吧，带手电筒果然是个好主意。这下面黑得他妈彻底。"
    "而且……没错。高管阶层的私人车库。大部分是空的。"
    scene c004_s007_008 with Dissolve(0.25)
    "除了那辆 SUV。不错。"
    "好，这是个积极进展。这儿空气还不算太糟，所以说不定这台家伙还能开。只要我能找到钥匙。因为我对撬车接线可不在行。"
    scene c004_s007_009 with Dissolve(0.25)
    "不过这给了我一个在搜办公室时留意的目标。盼着有人把车落下了。也许他们深夜之后被人接走了，打算回头再取。"
    "不管我编出什么故事，我现在大概都不该提这事。我不想给她们任何虚假的希望，让她们以为我们手上有这个。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_25_631", transition=Dissolve(1.0))()
    pause
    $ Hide("june_25_631", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain2 fadein 2.0
    scene c004_s008_001 with Dissolve(2)
    "我有多愿意给其他人留空间——如果她们想或者需要的话——可我必须确认每个人都还好。这种情况下，要是不小心，侵入式的念头和偏执的行为真的可能冒出来。"
    "我也不是免疫的。让自己忙起来是我唯一的办法，好把注意力放在「能做什么」上，而不是「这件事可能会怎么坑我们」上。"
    scene c004_s008_002 with Dissolve(0.5)
    "那边是卡莉。还盼着从电视或者她的手机里看到点什么。她还年轻，可能到现在都还离不开那种随时跟所有人保持连接的感觉。"
    scene c004_s008_003 with Dissolve(0.25)
    k "哦？是你。我听见有人走动，然后……"
    j "抱歉我不是更理想的对象。"
    scene c004_s008_004 with Dissolve(0.5)
    k "不是那么回事。我不介意。我只是……"
    j "你需要休息一下吗？"
    scene c004_s008_005 with Dissolve(0.25)
    k "也许不是那个，但坐在这儿干等着听动静没意义。而且我能忍的静电噪音也就那么多，再听下去就该头痛了。或者更糟。我怕自己都开始听见不存在的声音了。"
    j "所以你把声音关了。"
    scene c004_s008_006 with Dissolve(0.25)
    k "对。一个人在这儿跟那个待在一起，对我一点好处都没有。我太习惯人声、车流之类的东西了，它们一消失就让我有点不对劲。我听见楼体吱呀作响都会被吓一跳。"
    j "这是正常的反应。"
    scene c004_s008_007 with Dissolve(0.25)
    k "感觉我像个小受惊的女孩，我讨厌这样。我讨厌跟世界断开联系。我讨厌不能想出门就出门。我讨厌不能跟家里人说话。"
    j "我知道。这对局面一点帮助都没有。"
    scene c004_s008_005 with Dissolve(0.25)
    "我也没什么别的可说。我从来算不上多合群，但我能理解这对她有多重要。尤其是在关系到安德鲁或她家人的时候。也许我该换个话题，别让她在这件事上越陷越深。"
    j "嘿，我有个想法：你在这儿能收到信号吗？我手机放在外套里了，所以还没查。我问是因为如果我们在六楼、高于雾层，说不定能有信号。"
    scene c004_s008_008 with Dissolve(0.25)
    k "今天早上我也这么想。吃完早饭之后试了。没有。也许是信号塔倒了。或者，我们就是被切断了。"
    "「被切断」这个词暗示了一些我现在还不太愿意考虑的东西。"
    j "哦，那好吧，试试总没坏处。"
    scene c004_s008_009 with Dissolve(1)
    k "呃……我能问你件事吗？有点怪。也许吧。"
    j "当然。问吧。现在对我来说没什么是怪的。"
    scene c004_s008_010 with Dissolve(0.25)
    k "你、你觉得人们待在一起，是因为彼此在对方身边，还是因为住在同一个地方？"
    j "呃，怎么突然想到这个？"
    scene c004_s008_011 with Dissolve(0.25)
    k "就是……我一个人想事情的时候。会想人们当时为什么会那样做、那样想，然后我发现自己正照着从别人身上看到的路子走，就忍不住想「为什么」。"
    j "老实说，住得近不会坏事。我们往往会对经常相处的人更有好感。或者说，更有{i}感觉{/i}，因为我学到过反过来也成立。我猜「喜欢这个人」本身帮助很大。还有吸引力之类的。"
    j "我觉得很多关系之所以维持，纯粹是因为方便，以及人们一旦不满意，也不想经历大改大动带来的动荡。惯性，加上害怕孤独。有些婚姻没有早点结束，是因为相信两个人只要更努力就能把它撑下去。"
    scene c004_s008_012 with Dissolve(0.25)
    k "比如你们的？我不是那个意思。只是……我……抱歉……"
    j "我明白你想说什么，没错。我们大概在第一年就该分开。或者照现在这么想，干脆别在一起才对。不过南希和我不代表所有人。别的人就挺好。很多人都是。"
    scene c004_s008_013 with Dissolve(0.25)
    k "因为他们住在一起，然后对家庭投入了感情，觉得自己不能撒手不管。如果他们住在不同的城市，还会是现在这样吗？还是说人们正是为了不开始渐行渐远才搬到一起的？"
    j "如果你真的爱一个人，我不认为时间上的分离会毁掉一段感情。"
    k "可如果你不确定自己是不是真的爱他呢？要是你怀疑自己跟他在一起，只是因为社会希望人人成双成对、生儿育女，而你只是随大流呢。"
    scene c004_s008_014 with Dissolve(0.5)
    j "我觉得这件事得你自己想清楚。不过你在问问题，那已经是好的第一步了。"
    "她还是那么年轻，正试着理解人世。靠，我都比她大好几岁，还在做同样的事。劳拉大概也会这么说。"
    if k_friend >= 7:
        scene c004_s008_015 with Dissolve(0.25)
        "哦？我没想到会这样。我大概不该把它当回事。要是她觉得脆弱、孤独、陷在一些沉重的想法里，也许光是有人在旁边就够了。"
        scene c004_s008_016 with Dissolve(0.5)
        k "我……你不介意吧？"
        j "一点也不。这种时候有点人味交流挺好的。甚至算是一种安慰。"
        scene c004_s008_017 with Dissolve(0.25)
        k "我、我害怕。你知道的，对吧？我怕得很。"
        j "我知道，而且完全有理由。就算在我们遇上外面那个烧焦似的东西之前也是。日子很难，我们需要彼此。我们每个人都需要。"
        scene c004_s008_018 with Dissolve(0.25)
        k "我、我也有同感。要是没有你和劳拉，我不知道自己会怎么办。我发现我根本不知道在这种灾难里该怎么做。"
        j "这不是正常的灾难。没人应该知道该怎么办。"
        scene c004_s008_019 with Dissolve(0.25)
        k "我只想让你知道，我很感激你一直在做的事。有你在身边，我确实觉得更安全。"
        scene c004_s008_020 with Dissolve(0.25)
        k "有那么一小会儿，我不觉得这是世界末日。"
        j "知道就好。如果你需要有人安慰，或者想要个拥抱，尽管跟我说。我不排斥。"
        scene c004_s008_021 with Dissolve(0.5)
        k "*咯咯笑* 好。如果不太麻烦的话。"
        menu:
            "就当是饭钱的抵付。":
                j "就当是饭钱的抵付。你负责喂饱我，我负责当你的定心丸。"
                scene c004_s008_022 with Dissolve(0.25)
                k "成交。我喜欢这个说法。"
                scene c004_s008_023 with Dissolve(0.5)
                "这种感觉不错。虽然短暂，但有一份共享的温暖，同时又像是战友之间的情谊。而且她闻起来很香，哪怕是淋浴间里那种肥皂味。"
            "抱这么可爱的姑娘？\n[rgr](卡莉 欲望 +1)":
                $ k_desire += 1
                j "抱这么可爱的姑娘？一点也不麻烦。"
                scene c004_s008_022 with Dissolve(0.25)
                k "我……呃……*咯咯笑*"
                scene c004_s008_023 with Dissolve(0.5)
                "可能我有点太主动了。靠，她肯定知道自己可爱。这对她来说不可能是个谜。"
    scene c004_s008_024 with Dissolve(0.5)
    j "那么，你今天见过劳拉了吗？"
    k "我最后一次看见她的时候，她在楼上的会议室。"
    j "我就猜。我得去看看她没事吧。"
    scene c004_s008_025 with Dissolve(0.25)
    k "我、我提了明天要出门，还建议她暂时留在这儿。"
    j "哦？然后呢？"
    scene c004_s008_026 with Dissolve(0.25)
    k "她不太高兴，但我觉得她理解我为什么提这个。可能我还暗示了我们该谈谈这事。"
    j "还有这个主意有一部分是我出的？谢谢你把我推出去当挡箭牌。"
    k "抱歉。"
    scene c004_s008_027 with Dissolve(0.25)
    j "没关系，我开玩笑的。不过我去看看能不能跟她聊聊。你该休息一下了。别在这儿。出去走走。回你办公室待着，别在这儿耗着。"
    k "我、我知道。我会的。我保证。"
    scene c004_s008_028 with Dissolve(0.25)
    "我很想告诉她那辆 SUV 的事，让气氛有点变化，可我还不想先让她空欢喜。至少得等我找到钥匙。"
    scene blank with Dissolve(2)
    scene c004_s009_001 with Dissolve(2)
    "这局面把我们所有人都改变了，对我来说简直有点好笑。以前我和卡莉只是几乎不说话的同事。现在？我不敢说自己了解她最深的秘密，但感觉这件事把我们绑在了一起。"
    "她居然愿意对我交心，这对她来说是很大的一步。再加上我本来完全没料到她会有肢体接触，这足以说明我们现在的关系。我不假装等这一切结束我们还能是最铁的哥们儿，但我们会拥有一些只有彼此知道的东西。"
    scene blank with Dissolve(2)
    scene c004_s009_002 with Dissolve(2)
    "再说还有劳拉……我本来就觉得我们是朋友——工作上的朋友——但这件事真的让我们在不想让同事看到真面子的那些客套上，全都省了。"
    if ch3_laura_sex == "yes":
        "更别提我们还见过彼此没穿衣服的样子。以及更多。或者说，我不该「提」这件事，因为她肯定不想让我们表现得好像那发生过。我理解她还是想、也需要看看，等我们出去之后她的婚姻有没有可能挽救。"
    scene c004_s009_003 with Dissolve(0.25)
    "她在那儿。天都黑了，还在看。"
    j "嘿，劳拉，你还好吗？"
    l "[player_name]，我……对。有人陪着真好。"
    scene c004_s009_004 with Dissolve(0.25)
    j "什么？在这儿看太久了吗？看到什么值得看的东西了吗？"
    l "没我希望的那么多。也许看见远处有鸟。飞得很高，在城市上空。或者，我觉得那是鸟。"
    scene c004_s009_005 with Dissolve(0.5)
    j "这是好事，对吧？"
    l "感觉确实能证明雾并不是无处不在。或者差不多这个意思。水手看到海鸥时不是说类似的话吗？"
    j "我想是吧。我可没什么航海知识。所以，显然没有飞机之类的人造物？"
    scene c004_s009_006 with Dissolve(0.25)
    l "我没看见。而且说实话，连着坐上几个小时对我一点好处都没有。我集中注意力的能力正在下降。"
    j "我跟卡莉也聊过类似的话题。电视那件事已经变成了一个问题。"
    scene c004_s009_007 with Dissolve(0.25)
    l "对……其实我们今天早些时候聊过。说到回去拿更多食物，还有你们俩的担心。"
    j "你懂我们为什么要那么做，对吧？"
    scene c004_s009_008 with Dissolve(0.25)
    l "我懂，哪怕我不喜欢。我呼吸的问题还没解决。可你觉得我留在这儿真能好起来吗？"
    menu:
        "会的。":
            j "会的。听起来你比我们刚到的时候好多了。"
            scene c004_s009_009 with Dissolve(0.25)
            l "你说是就是吧。"
        "你不会再变差了。\n[rgr](劳拉 信任 +1)":
            $ l_trust += 1
            j "你不会再变差了。"
            scene c004_s009_009 with Dissolve(0.25)
            l "我想这话大概没错。至少，要是我们对此都坦率诚实的话。"
    j "嘿，走吧。别在这儿耗着了。现在天黑了，你不会再看到什么值得看的了。时间不早了，你也该换个地方待待。"
    "再说了，我敢肯定坐在这儿想她儿子或者她的婚姻，对她一点好处都没有。"
    if ch3_laura_sex == "no" and l_friend <= 3 or ch3_laura_sex == "no" and l_desire <= 1:
        scene c004_s009_010 with Dissolve(0.5)
        l "*叹气* 你说得对。我想我也需要有人提醒我，钻牛角尖不健康。"
        scene c004_s009_011 with Dissolve(0.25)
        j "我觉得我们每个人都该负责互相做理智和心理健康的检查。这是我们能完好走出这里唯一的办法。"
        l "大概吧。"
        scene c004_s009_012 with Dissolve(0.25)
        l "[player_name]，告诉我彼得没事。就算你并不真的相信。我只是需要有人把我从悬崖边拉回来。作为一个担心儿子的母亲。"
        j "他没事，我也真信着。他是你的孩子，所以聪明又机灵。而且他离这儿十万八千里，我敢说他好得很真要有什么，反倒该是他担心你。所以，也许我们该努努力，让你既安全又清醒。"
        scene c004_s009_013 with Dissolve(0.25)
        l "谢谢。这正是……我需要听到的话。"
    else:
        scene c004_s009_014 with Dissolve(0.5)
        l "[player_name]……我……你还记得那天晚上吗？"
        j "哪一天？你出现在办公室之后，我们经历了太多晚上了。"
        scene c004_s009_015 with Dissolve(0.25)
        if ch3_laura_kiss == "yes" or ch3_laura_sex == "yes":
            l "你知道是哪一天。我心情不好，你坐到我旁边，我们聊了我那快要完蛋的婚姻，然后我们……"
            if ch3_laura_sex == "yes":
                j "然后我们上床了？我以为你不想聊这个，也不想装作它发生过。我还以为那是个我们再也不会提起的秘密。这是那种「我让你别提某件事，结果后来我自己又提起来」的情况吗？男人都不喜欢这套，劳拉。*轻笑*"
            else:
                j "然后我们接吻了？我以为你不想聊这个，也不想装作它发生过。我还以为那是个我们再也不会提起的秘密。这是那种「我让你别提某件事，结果后来我自己又提起来」的情况吗？男人都不喜欢这套，劳拉。*轻笑*"
            scene c004_s009_016 with Dissolve(0.25)
            l "不不。我不是那个意思。我、我只是……我有很多时间可以想。困在这栋楼里，让我有大量时间去审视我的人生和我做过的每一个决定。我可不是整天只顾着盯窗外。"
        else:
            l "你知道是哪一天。我心情不好，你坐到我旁边，我们聊了我那快要完蛋的婚姻，然后我们……"
            j "我知道。你不用说第二遍。尤其要是把它挖出来只会让那道伤口重新裂开。"
            scene c004_s009_016 with Dissolve(0.25)
            l "不不，不是那样。我、我只是……我有很多时间可以想。困在这栋楼里，让我有大量时间去审视我的人生和我做过的每一个决定。我可不是整天只顾着盯窗外。"
        j "这些我也有过很多。南希搬走之后，每天晚上我都在回放我们在一起时说过的话、做过的选择。没有一次的结果是我们重归于好。"
        scene c004_s009_017 with Dissolve(0.25)
        l "所以，你懂的。然后我就开始想你这段时间……你说过一些话……"
        j "哦？我……要是我说了什么让你不舒服的话，那对不起。我最近基本不过滤了。睡眠不足加上吃不上饭，让我比平时更嘴碎。"
        scene c004_s009_018 with Dissolve(0.25)
        if ch3_laura_sex == "yes":
            l "不是那个意思。你……你让我很久以来第一次觉得自己有吸引力。我一直觉得自己的身体只是个功能性的存在。我早就不再相信会有人觉得我值得被要了。更别说我丈夫了。我第一个念头就往那儿去，这本身就很说明问题。"
        else:
            l "不是那个意思。你……你让我很久以来第一次对自己感觉不错。我一直觉得自己的身体只是个功能性的存在。我早就不再相信会有人觉得我值得被要了。更别说我丈夫了。我第一个念头就往那儿去，这本身就很说明问题。"
        menu:
            "[rd]听起来这话该你们俩去说。\n[rrd](劳拉 好感\欲望 -1)":
                $ l_friend -= 1
                $ l_desire -= 1
                j "听起来这话该你们俩等出去了再说。我不知道跟一个人处那么久是什么滋味，所以我没法说他是不是只是松懈了、该更上心的时候没上心。但有时候男人就是笨，丢掉了他们原本会做的事。"
                scene c004_s009_019 with Dissolve(0.25)
                l "*叹气* 我希望事情真有那么简单。"
                j "跟他坐下来谈谈不会有坏处。而且既然你觉得他可能在外面有人，你心里大概积了很多话要说。"
            "那他就是个白痴。\n[rgr](劳拉 好感 +1)":
                $ l_friend += 1
                j "那他就是个白痴。抱歉，但这是事实。这男人家里有个聪明漂亮的女人，却还在外面看别的。如果你说的是真的。真是个蠢货，我跟你说。"
        scene c004_s009_020 with Dissolve(0.25)
        l "……"
        j "我知道这大概帮不上你什么忙，但我想，让你听听一个局外人的看法应该不会有害。事后看来，我自己当年也本该有人这么跟我说。"
        scene c004_s009_021 with Dissolve(0.25)
        l "我希望你当初说了。我会听的。"
        j "我知道，可当你陷在自己的痛苦里时，很难看得见这一点。再说了，我觉得我们现在是比以前坦率多了。换成两周前，我们绝对不会这样。"
        l "这倒是真的。要不是被困在这儿什么都做不了，我不会提我和基思的那些问题。所以我才一直那么忙。这样我就不用想太久。就当是转移注意力。可现在我没有这个转移注意力的东西了，而且……"
        menu:
            "听着就好。[yl]":
                "我觉得劳拉不需要我在旁边附和她的抱怨。她显然很清楚问题在她自己眼里是什么样的。"
                scene c004_s009_022 with Dissolve(0.25)
                l "要是被人弄成这种感觉，我简直气疯了。这让我开始怀疑自己这些年。每一次他晚回家，或者周末要出去做事的时候。我讨厌这样。我讨厌它带给我的感觉。讨厌「我不够好」。讨厌「我不够」。"
            "你有权这么觉得。[yl]":
                j "你有权这么觉得。愤怒、难过。当然，你并不需要我的许可。"
                scene c004_s009_022 with Dissolve(0.25)
                l "我开始明白了。可我气就气在被弄成这种感觉。这让我开始怀疑自己这些年。每一次他晚回家，或者周末要出去做事的时候。我讨厌这样。我讨厌它带给我的感觉。讨厌「我不够好」。讨厌「我不够」。"
        scene c004_s009_023 with Dissolve(0.25)
        l "我只是……*吸鼻子*"
        if ch3_laura_sex == "yes":
            "我这时候该说点什么吗？我觉得说话得小心。我想支持她、给她打气，可要是不小心蹦出了一句不合适的话，效果可能会适得其反。而且想到她多少有点后悔我们上次的接触，我或许该谨慎用词。"
        else:
            "我这时候该说点什么吗？我觉得说话得小心。我想支持她、给她打气，可要是不小心蹦出了一句不合适的话，效果可能会适得其反。"
        menu:
            "别说话。":
                scene c004_s009_010 with Dissolve(0.5)
                "不了。让她自己发挥。光是在这儿应该就够了。她需要有人听她说话。有时候人们真的就只要这个——一个愿意倾听的耳朵，而不是一个把意见丢回来的人。"
                l "*叹气* 靠，我什么都不剩了。又累又烧干了。我只能气这么久，不然要给自己气出头痛。"
                j "要不我们离开这儿？在这个房间待着，对你没什么好处，对吧？"
                scene c004_s009_011 with Dissolve(0.25)
                l "不要~~~ 真的没有。"
                "我从没想过能看到劳拉快要撅嘴的样子。她一向那么强势、那么有主意。"
                scene c004_s009_012 with Dissolve(0.25)
                l "[player_name]，告诉我彼得没事。就算你并不真的相信。我只是需要有人把我从悬崖边拉回来。作为一个担心儿子的母亲。"
                j "他没事，我也真信着。他是你的孩子，所以聪明又机灵。而且他离这儿十万八千里，我敢说他好得很。真要有什么，反倒该是他担心你。所以，也许我们该努努力，让你既安全又清醒。"
                scene c004_s009_013 with Dissolve(0.25)
                l "谢谢。这正是……我需要听到的话。"
            "说点好听的。\n[rgr](劳拉 好感\欲望 +1)":
                $ l_friend += 1
                $ l_desire += 1
                scene c004_s009_024 with Dissolve(0.5)
                if ch3_laura_sex == "yes":
                    j "劳拉，你是个漂亮的女人。聪明，待在一起也舒服。就算我没看见你外面那层底下藏着的东西，我也会这么觉得。我一直都觉得你很有魅力。"
                else:
                    j "劳拉，你是个漂亮的女人。聪明，待在一起也舒服。而且很性感。我一直都觉得你非常有魅力，虽然这句坦白可能会让我惹上麻烦。"
                l "你只是——"
                j "不，我不是。我不是在「说好听的」。我说这些得不到任何好处。我只是说你该听到的话。也许不该从我嘴里说，但你无论如何都该知道。"
                scene c004_s009_025 with Dissolve(0.25)
                l "所以你不只是为了让我觉得好受才这么说？"
                if ch3_laura_sex == "yes":
                    j "我希望是。但就算不是，我也只是把它摆在这儿让你听见。来自一个你朋友、在乎你的人。也许我说得够多，它就能刻进你脑子里。再说了，我见过你没穿衣服的样子，我知道自己在说什么。"
                else:
                    j "我希望是。但就算不是，我也只是把它摆在这儿让你听见。来自一个你朋友、在乎你的人。也许我说得够多，它就能刻进你脑子里。"
                scene c004_s009_026 with Dissolve(0.25)
                l "你……你太好了。"
                j "是吗？你可比这了解我。*轻笑*"
                l "对，你不是那种会对人灌迷魂汤的人。"
                scene c004_s009_027 with Dissolve(0.25)
                l "唔嗯……*叹气*"
                if ch3_laura_sex == "yes":
                    "也许是我想多了，但我感觉劳拉看我的眼神开始有点黏黏的。她也许说过上次只是一次性的，可……当然，也可能是我完全看错了。"
                else:
                    "也许是我想多了，但我感觉劳拉看我的眼神开始有点黏黏的。我虽然迟钝，可我们之间好像有点温度……当然，也可能是我完全看错了。"
                menu:
                    "靠近。\n[rgr](劳拉 爱意 +1)\n[pks]":
                        stop music fadeout 2.0
                        $ l_sex += 1
                        $ l_love += 1
                        $ ch4_laura_sex = "yes"
                        call ch4_laura_sex from _call_ch4_laura_sex
                    "退开。":
                        scene c004_s009_028 with Dissolve(0.25)
                        "对，最好还是退开。情绪和神经都太脆弱了。她现在这个状态，我不该再逼她。"
                        scene c004_s009_010 with Dissolve(0.5)
                        l "[player_name]？"
                        j "要不我们离开这儿？在这个房间待着，对你没什么好处，对吧？"
                        scene c004_s009_011 with Dissolve(0.25)
                        l "对，确实没有。我想这一点很明白。"
                        "我从没想过能看到劳拉快要撅嘴的样子。她一向那么强势、那么有主意。"
                        scene c004_s009_012 with Dissolve(0.25)
                        l "[player_name]，告诉我彼得没事。就算你并不真的相信。我只是需要有人把我从悬崖边拉回来。作为一个担心儿子的母亲。"
                        j "他没事，我也真信着。他是你的孩子，所以聪明又机灵。而且他离这儿十万八千里，我敢说他好得很。真要有什么，反倒该是他担心你。所以，也许我们该努努力，让你既安全又清醒。"
                        scene c004_s009_013 with Dissolve(0.25)
                        l "谢谢。这正是……我需要听到的话。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c004_s010_001 with Dissolve(2)
    if ch4_laura_sex == "yes":
        "我们回到二楼，劳拉在她的沙发上躺下，我则回到自己的长椅。虽然我觉得自己比以往任何时候都更靠近她，但她睡的地方绝不可能跟我分享。她已经说得很清楚，我们那些风流事考虑欠妥，这种事该到此为止。"
        scene c004_s010_002 with Dissolve(0.5)
        "我不喜欢那样结束这一夜，但她说得对。她还有一个生活要回去过，哪怕那是一个如果婚姻真的完了就得重新拼起来的生活。"
        "像那样和她牵扯进去也许是个不错的消遣，而且（我希望）让她对自己感觉好了些，但那只让她本已浑水的局面更浑。"
        scene c004_s010_003 with Dissolve(0.5)
        "我不能再在感情上得寸进尺，而得在她需要的时候，重新做一个朋友。"
    elif ch4_laura_sex == "no" and ch3_laura_sex == "yes":
        "我们回到二楼，劳拉在她的沙发上躺下，我则回到自己的长椅。我感觉以她情绪被榨干的程度，劳拉撑不了多久就会睡着。"
        "除了四面八方的危险和必然要自己救自己这件事之外，她还在为家里的问题挣扎。"
        scene c004_s010_002 with Dissolve(0.5)
        "我不喜欢那样结束这一夜，但她说得对。她还有一个生活要回去过，哪怕那是一个如果婚姻真的完了就得重新拼起来的生活。以任何方式和她牵扯进去也许是个不错的消遣，但那只让我们本已浑水的局面更浑。"
        scene c004_s010_003 with Dissolve(0.5)
        "我不能再在感情上得寸进尺，而得在她需要的时候，重新做一个朋友。"
    else:
        "我们回到二楼，劳拉在她的沙发上躺下，我则回到自己的长椅。我感觉以她情绪被榨干的程度，劳拉撑不了多久就会睡着。"
        scene c004_s010_003 with Dissolve(0.5)
        "除了四面八方的危险和必然要自己救自己这件事之外，她还在为家里的问题挣扎。她需要的时候，我得尽力做个朋友。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_26_903", transition=Dissolve(1.0))()
    pause
    $ Hide("june_26_903", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music officemain fadein 2.0
    scene c004_s010_004 with Dissolve(2)
    $ l_anxiety += 1
    "第二天早上，等大家都起床活动开了（还有我灌下去的那几杯咖啡），我和卡莉换好衣服准备回餐馆。虽然我一直觉得卡莉能把自己的情绪收得挺好，可我开始能从她的肢体语言里读出一些细微的线索了。"
    "前一天我们已经谈过这事，所以我大致知道她在想什么，可我还是能从她躲开的眼神和拉拉链时紧张摆弄的手指里看出焦虑的痕迹。"
    play sound zipper
    scene c004_s010_005 with Dissolve(0.25)
    "劳拉则不是那种会藏起情绪的人。即便她说她理解其中的道理，她也不喜欢留下来。所幸的是，她并没有试图跟我们一起走。"
    "到了这一步，我们谁都不觉得这次跋涉有多值得考虑。有毒的雾、可能潜伏着的怪物，我们这么做只是因为吃饭是必需品。而我们每天只能吃一顿，这更让情况雪上加霜。"
    "我不知道她们怎样，反正我现在一直都很饿。还要多久我才会掉体重？或者因为没力气而开始应付不了平常那些体力活？"
    scene c004_s010_006 with Dissolve(0.25)
    "至少我们还有水喝，可就像卡莉之前说的，{i}汉堡店{/i}的食物也撑不了多久。就连现在，我也开始担心东西会不会变质。"
    l "你觉得我们能在外面待多久？"
    j "如果不碰上麻烦的话？跟上次差不多。也许更短。我们进去、把食物准备好、然后出来，对吧？"
    scene c004_s010_007 with Dissolve(0.25)
    k "对。我一点都不想在那儿多待。"
    l "*叹气* 所以我就在这儿干等着，什么都不做？"
    scene c004_s010_008 with Dissolve(0.5)
    k "你可以去看看电视。或者去会议室看看风景。"
    l "我……我更想做点真正有用的事。干坐着等待让我有点坐立不安，也许我宁愿做点{i}任何事{/i}，也不愿干等。"
    "我明白她的意思。我知道我一直想把 SUV 的事按住不说，直到有个值得说的结果，可既然这能让劳拉有事做，那我就该告诉她们。"
    scene c004_s010_009 with Dissolve(0.25)
    j "劳拉，我昨天找到了一张停车通行证。在那边，跟我的短裤放在一起。它能打开地下的私人停车场。我在那里发现了一辆没人动过的 SUV。"
    l "好吗？还有那个……"
    scene c004_s010_010 with Dissolve(0.25)
    j "那下面几乎没有雾。我不知道那辆 SUV 在那儿停了多久，不过看上去没人动过。"
    k "所以，如果它没被雾影响，也许还能开？"
    j "理论上可以。我之前没说，是因为还没找到钥匙，不过你要是想去办公室里翻翻找找，那就请便。"
    scene c004_s010_011 with Dissolve(0.25)
    l "当然。你在哪儿找到那张通行证的？"
    j "三楼，大楼东侧的一间办公室。"
    l "好，我先从那儿开始。"
    j "好。卡莉？"
    scene c004_s010_012 with Dissolve(0.25)
    k "我准备好了。尽可能地准备好了。"
    j "好，你知道规矩。要是在外面看见我们那位朋友，就拼命跑出来。往最近的地方跑。餐馆，或者回这边。"
    scene c004_s010_013 with Dissolve(0.25)
    l "那你呢？别在外面逞英雄。"
    j "我不敢保证。"
    scene blank with Dissolve(2)
    scene c004_s010_014 with Dissolve(2)
    l "可你之前为什么不提找到车的事？"
    menu:
        "别的事赶上了。\n[rrd](劳拉 信任 -1)":
            $ l_trust -= 1
            j "别的事赶上了。我知道这听起来好像这儿没发生什么大事，但我们的日子可不平淡。"
            scene c004_s010_015 with Dissolve(0.25)
            l "*叹气* 你说是就是吧。"
        "我分心了。" if ch4_laura_sex == "yes":
            j "你也可以说我就是分心了。"
            scene c004_s010_015 with Dissolve(0.25)
            l "好好好~~~好吧"
            "关于这个就到此为止吧。对，我把没提这事怪到我们做爱上了，不过既然不会再有第二次，我想也没什么。"
        "我不想先让你空欢喜。\n[rgr](劳拉 信任 +1)":
            $ l_trust += 1
            j "我不想先让你空欢喜。万一我们找不到钥匙呢？告诉你了，结果只是一条死路，那有什么意义？"
            scene c004_s010_015 with Dissolve(0.25)
            l "可你还是说了。还是告诉我们了。"
            j "因为多一双眼睛帮忙找车钥匙总归能提高成功率。而且要是我想，你可以趁我们回来之前找点事做。"
    scene c004_s010_016 with Dissolve(0.25)
    j "你想去看 SUV 的话，把手电筒带上。车库里面雾不浓，但大堂那边不太好，记得戴口罩，小心点。"
    scene c004_s010_017 with Dissolve(0.25)
    l "知道知道。你们也别在外面待太久。"
    scene blank with Dissolve(2)
    scene c004_s010_018 with Dissolve(2)
    "也许让劳拉去四处转转，比干等我们回来——或者更糟，盯着会议室的窗户看——能让她忙着有事做，不至于继续钻牛角尖。除了担心儿子，她还在苦苦挣扎于自己婚姻一天不如一天这件事。"
    k "*叹气*"
    scene c004_s010_019 with Dissolve(0.25)
    "而卡莉呢？她很紧张。可以理解。"
    menu:
        "会没事的。":
            j "会没事的。我们过去、把食物弄好、然后拼命跑回来。要是有麻烦，我们就撤。"
            k "可我们需要食物。不能就这么不去、拖到以后。我们必须去。"
            scene c004_s010_020 with Dissolve(0.25)
            j "我们还会有下一次机会。但今天我们不会让自己陷入危险。"
            k "我……好吧。"
        "你很勇敢。\n[rgr](卡莉 好感 +1)":
            $ k_friend += 1
            j "你很勇敢。做了这件事。我知道你在害怕。我自己也焦虑得很。"
            k "我不觉得自己勇敢。"
            scene c004_s010_020 with Dissolve(0.25)
            j "明明怕得要命还是去做，这就叫勇敢，卡莉。我很确定这个词在字典里。"
            k "*咯咯笑* 好吧。你说是就是吧。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c004_s011_001 with Dissolve(2)
    play music outsideday2 fadein 2.0
    "我突然想到，我们真的完全不知道怎么判断那怪物在不在附近。沉重的呼吸声？雾变浓？可上次它确实就是那么毫无预兆地走到我们跟前。"
    scene c004_s011_002 with Dissolve(0.5)
    "除了死死留意周围环境，我也不知道还能做什么。更麻烦的是，这团东西（雾？烟？）密度很奇怪，飘动的时候会发出一种怪响。几乎听不见，可在这周围毫无其他声音的时候，你就会注意到。"
    scene c004_s011_003 with Dissolve(0.25)
    "那是血吗？地上那儿。这就是我们前些天被袭击的地方吗？当所有东西看起来都像《开膛手杰克》的片场时，很难辨认地标。"
    k "怎么了吗？你停下了。"
    scene c004_s011_004 with Dissolve(0.25)
    "我该去看看吗？要不要告诉卡莉？"
    menu:
        "没事。我们走。\n[rrd](卡莉 信任 -1)":
            $ k_trust -= 1
            scene c004_s011_005 with Dissolve(0.5)
            j "没事。我以为看到了什么，其实是光线的错觉。我们走。"
            k "好、好吧。"
            "最好还是别在这儿招事。我确实砍到它了，所以它被我砍倒的时候是在流血的。这大概就是它倒下时留下的一条血迹。"
        "我觉得没什么。我马上追上来。":
            $ ch4_burnedone_1_seen = "yes"
            scene c004_s011_006 with Dissolve(0.5)
            j "我觉得没什么。我马上追上来。"
            k "你确定吗？"
            j "对。只是确认一件事。确认我们的退路是通的。走吧。我很快就到。"
            scene c004_s011_007 with Dissolve(0.25)
            "分开行动也许不是最好的计划，可卡莉现在脆弱得厉害，我想先把这一带查看清楚。"
            scene blank with Dissolve(2)
            scene c004_s011_011 with Dissolve(2)
            "还有那条血迹……"
            scene c004_s011_013 with Dissolve(0.25)
            "哦，原来在这儿。仰面躺在一摊自己的血里。那一下看来是致命的。"
            scene c004_s011_017 with Dissolve(0.5)
            "我的天，你这恶心的东西。浑身覆盖着烧焦的皮肉。面目全非。几乎不是人了。我还能闻到那股浓缩的氨和酸味。呕。"
            "好吧，那说明我们这位朋友不会再是麻烦了。我并不乐意再杀一个生物，可它对我们有敌意，所以这算自卫。"
            scene c004_s011_015 with Dissolve(0.5)
            "我该走了。别让卡莉等太久。还有，我得决定要不要告诉她。"
        "地上有一条血迹。\n[rgr](卡莉 信任 +1)\n[rrd](卡莉 焦虑 +1)":
            $ k_trust += 1
            $ k_anxiety += 1
            $ ch4_burnedone_1_seen = "yes"
            scene c004_s011_006 with Dissolve(0.5)
            j "地上有一条血迹。我想是我用斧子砍中那怪物脑袋时留下的。"
            k "哦？啊……"
            j "我去看看。就一下。你要是想先走一步……"
            if k_anxiety >= 6:
                scene c004_s011_007 with Dissolve(0.25)
                k "我、我去吧。别太久。小心。拜托。"
                j "我会的。我可不是什么英雄。你先走吧。"
                "分开行动也许不是最好的计划，可卡莉已经够脆弱了，我不怪她先走。而我也还是想把这一带查看一遍。只是为了保险。"
                scene blank with Dissolve(2)
                scene c004_s011_011 with Dissolve(2)
                "还有那条血迹……"
                scene c004_s011_013 with Dissolve(0.25)
                "哦，原来在这儿。仰面躺在一摊自己的血里。那一下看来是致命的。"
                scene c004_s011_017 with Dissolve(0.5)
                "我的天，你这恶心的东西。浑身覆盖着烧焦的皮肉。面目全非。几乎不是人了。我还能闻到那股浓缩的氨和酸味。呕。"
                scene c004_s011_015 with Dissolve(0.5)
                "好吧，那说明我们这位朋友不会再是麻烦了。我并不乐意再杀一个生物，可它对我们有敌意，所以这算自卫。"
                "我该走了。别让卡莉等太久。还有，我得决定要不要告诉她我发现了什么。她知道我去找了，但不知道我找到了东西。"
            else:
                $ ch4_burnedone_callie_seen = "yes"
                scene c004_s011_008 with Dissolve(0.25)
                k "不不。我、我跟你一起去。分开行动不是好主意。不过——"
                j "万一有什么不对，我们就撤出来。不管怎样，这是第一步。"
                scene c004_s011_009 with Dissolve(0.25)
                k "好。"
                scene blank with Dissolve(2)
                scene c004_s011_010 with Dissolve(2)
                "还有那条血迹……"
                scene c004_s011_012 with Dissolve(0.25)
                "哦，原来在这儿。仰面躺在一摊自己的血里。那一下看来是致命的。"
                j "我的天，你真恶心。"
                k "呃~~~"
                scene c004_s011_016 with Dissolve(0.5)
                "浑身覆盖着烧焦的皮肉。面目全非。几乎不是人了。我还能闻到那股浓缩的氨和酸味。呕。"
                j "在我看它是死了。那说明我们这位朋友不会再是麻烦了。"
                k "我……那当然挺好，但不代表我们就安全了。"
                scene c004_s011_014 with Dissolve(0.5)
                j "对。这个环境本身就有害。说到这个，我后脖子开始发烫了。我们该走了。"
                k "对。我们……我们该走了。"
    scene blank with Dissolve(2)
    if ch4_burnedone_callie_seen == "yes":
        scene c004_s011_019 with Dissolve(2)
        "好吧，这解答了几个疑问，又制造了多得多的疑问。我能伤到它（而且看样子那生物是失血而死），所以拿上斧子是个正确决定。可它{b}是{/b}什么、或者{b}曾经{/b}是什么，还留着太多需要弄清的。不是今天。而且得由那些更懂科学的人来弄。"
        scene c004_s011_026 with Dissolve(0.5)
        "或者由那些有任务在身、不能在外面待太久的人来弄。我们放轻脚步，比刚才更急促也更安静地往餐馆走去。"
        k "什……那是什么？"
        j "我真的不知道。它看着像人——两条胳膊、两条腿、一个头——可它究竟是什么，我一点头绪都没有。也许能瞎猜几种，其中几种可能会让人晚上睡不着。"
        scene c004_s011_027 with Dissolve(0.5)
        k "你觉得它以前{i}是{/i}人吗？"
        j "这是我的猜测之一。我不是搞科学的，脑子也不算好使。参考我看过的恐怖片和电子游戏，也许它是某个在外面待太久了的人。或者吸收了太多雾，皮肤被灼伤，然后变形了。"
        play sound zipper
        scene c004_s011_028 with Dissolve(0.25)
        k "它能把我们变成那样？我记得它看着真是又恶心又扭曲，皮肤上还有一个一个的脓包……*呕*"
        k "抱歉，光是想想就想吐。"
        scene c004_s011_024 with Dissolve(0.25)
        j "我们换个话题吧。它已经不是我们的问题了。专心做我们来的事。好消息是，回程路上它不会再骚扰我们。"
        k "对。确实。"
        scene c004_s011_025 with Dissolve(0.25)
        "坏消息也许是，如果我那些瞎猜里有哪怕一个沾点边，那可能就是我们被困在外面太久之后的下场。"
        j "好了，开始吧。我们俩都不想待太久。我帮你准备。"
        scene c004_s011_029 with Dissolve(0.25)
        k "那我就谢了。我、我真的一点都不想比必要的更久待在这儿。而且我们得确认食物没开始变质。有些东西我不知道还能放多久。"
        j "我懂。上次我们在这儿的时候，有些蔬菜已经开始有点可疑了。"
    elif ch4_burnedone_1_seen == "yes" and ch4_burnedone_callie_seen == "no":
        scene c004_s011_018 with Dissolve(2)
        "好吧，这解答了几个疑问，又制造了多得多的疑问。我能伤到它，所以拿上斧子是个正确决定。可它{b}是{/b}什么、或者{b}曾经{/b}是什么，还留着太多需要弄清的。不是今天。而且得由那些更懂科学的人来弄。"
        "或者由那些有任务在身、不能在外面待太久的人来弄。想到卡莉会担心我耽搁太久，我快步赶到了餐馆。"
        scene c004_s011_020 with Dissolve(0.5)
        j "好了，我到了。抱歉让你等。"
        k "你、你看到什么了？找到什么了吗？"
        "她已经从上次的袭击里知道那个生物的存在了，也看见我走开了。所以瞒着她没什么好处。再说我也不能瞒她太久。"
        scene c004_s011_021 with Dissolve(0.5)
        j "前几天跳出来袭击我们的那个生物……它现在仰面躺在巷子里。泡在自己的血泊中。看来我砍它那一下比我预想的更致命。"
        k "哦？哦……呃……它是什么？长什么样？毕竟你看它的时候它没在攻击我们。"
        j "我不知道它{b}曾经{/b}是什么。看着像人——两条胳膊、两条腿、一个头——可它现在究竟是什么，我一点头绪都没有，只知道它死了。也许能瞎猜几种，其中几种可能会让人晚上睡不着。"
        scene c004_s011_022 with Dissolve(0.25)
        k "你觉得它以前{i}是{/i}人吗？"
        j "这是我的猜测之一。我不是搞科学的，脑子也不算好使。参考我看过的恐怖片和电子游戏，也许它是某个在外面待太久了的人。或者吸收了太多雾，皮肤被灼伤，然后变形了。"
        scene c004_s011_023 with Dissolve(0.25)
        k "它能把我们变成那样？我记得它看着真是又恶心又扭曲，皮肤上还有一个一个的脓包……*呕*"
        scene c004_s011_024 with Dissolve(0.25)
        k "抱歉，光是想想就想吐。"
        j "我们换个话题吧。它已经不是我们的问题了。专心做我们来的事。好消息是，回程路上它不会再骚扰我们。"
        k "对。确实。"
        "坏消息也许是，如果我那些瞎猜里有哪怕一个沾点边，那可能就是我们被困在外面太久之后的下场。"
        scene c004_s011_025 with Dissolve(0.25)
        j "好了，开始吧。我们俩都不想待太久。我帮你准备。"
        scene c004_s011_029 with Dissolve(0.25)
        k "那我就谢了。我、我真的一点都不想比必要的更久待在这儿。而且我们得确认食物没开始变质。有些东西我不知道还能放多久。"
        j "我懂。上次我们在这儿的时候，有些蔬菜已经开始有点可疑了。"
    else:
        scene c004_s011_019 with Dissolve(2)
        "好吧，这解答了几个疑问，又制造了多得多的疑问。我能伤到它，所以拿上斧子是个正确决定。可它{b}是{/b}什么，还留着太多需要弄清的。不是今天。而且得由那些更懂科学的人来弄。"
        scene c004_s011_026 with Dissolve(0.5)
        j "好了，我们到了。来……呃……我们开始吧。越快进出越好。"
        k "对。"
        scene c004_s011_027 with Dissolve(0.5)
        j "我们俩都不想待太久。我帮你准备。"
        k "那我就谢了。我、我真的一点都不想比必要的更久待在这儿。尤其还躺在那么一具尸体旁边。"
        scene c004_s011_028 with Dissolve(0.25)
        j "估计我们不会再被它烦太久了。如果运气好，我们来的次数不会超过一次。"
        k "听到这个我有点高兴，可要是真去医院，我们就得找别的地方弄食物和水了。"
        scene c004_s011_024 with Dissolve(0.25)
        j "要是能把那辆 SUV 弄发动，我打算把我们能带的东西全装上去。从办公室顺来的水。冰箱里剩下的任何东西。这里能拿的都拿走。"
        k "对。前提是能找到钥匙。"
        scene c004_s011_025 with Dissolve(0.25)
        j "不过现在……"
        scene c004_s011_029 with Dissolve(0.25)
        k "当然，当然。一件一件来。而且我们得确认食物没开始变质。有些东西我不知道还能放多久。"
        j "我懂。上次我们在这儿的时候，有些蔬菜已经开始有点可疑了。"
    scene blank with Dissolve(2)
    scene c004_s012_001 with Dissolve(2)
    "{color=#66ff33}好吧，让我看看能不能弄明白[player_name]刚才说的是什么。换回自己的衣服花了点时间，但比起冒险，我宁愿稳妥又安全地处理。我知道他说下面空气没问题，可大堂不行，我甚至不想让自己陷入可能出事的境地。{/color}"
    "{color=#66ff33}更别说现在我是一个人。这曾经从来不是个问题。我很擅长独处。我必须擅长，哪怕是在自己家里。在彼得去上大学之后的那段婚姻里也是。{/color}"
    scene c004_s012_002 with Dissolve(0.25)
    "{color=#66ff33}找到了。在那边。{/color}"
    scene c004_s012_003 with Dissolve(0.25)
    "{color=#66ff33}靠，这车不错。Bronco。看着要么是新的，要么保养得很好。{/color}"
    scene c004_s012_004 with Dissolve(0.5)
    "{color=#66ff33}防盗灯在闪，这很好。说明电池还有电。只是我们没有钥匙。但这也意味着我可以去楼上找找遥控钥匙。要是我们运气够好的话。反正没有任何迹象表明有人走的时候把东西落下了。{/color}"
    "{color=#66ff33}我想看看也不费什么。也难怪[player_name]这么急着翻那些办公室。他知道这事多久了？我理解他想等到有个更好的结果再告诉我们，尤其是涉及到卡莉的时候。她是个好孩子，但我有种感觉，她需要回到从前那个样子。{/color}"
    scene c004_s012_005 with Dissolve(0.25)
    "{color=#66ff33}或者……也许我前几天那番对话让我觉得，她被「训练」成了必须向未婚夫报备的那种人，而这次分别把她弄得很迷茫。{/color}"
    if l_sex == 2:
        scene c004_s012_006 with Dissolve(0.25)
        "{color=#66ff33}说到迷茫……我不敢相信我们又做了一次。我告诉过自己那只是一次性的失误，可它又发生了，而我根本就是想要的。比我自己预想的还要想要。我们靠得很近，我能感觉到那股热度，我根本忍不住。{/color}"
        "{color=#66ff33}在这件事发生之前他一直是个可靠的人，之后更是我的支柱。一直在支持我。而且……也许我对他有吸引力；如果情况有一点点不同，我也不会这么做。我丈夫正在操别的女人。我们被困在这儿。孤单。{/color}"
        scene c004_s012_007 with Dissolve(0.25)
        "{color=#66ff33}我应该为此感到内疚，但那几乎是我现在唯一没有的感觉。我……我是不是在默许自己接受这件事？不，这只是我太需要人陪了。{/color}"
        "{color=#66ff33}可那其实并不重要，我不该让自己分心。{/color}"
    if l_sex == 1:
        scene c004_s012_006 with Dissolve(0.25)
        "{color=#66ff33}说到迷茫……我不敢相信我跟[player_name]做完了。事情就这么发生了，我甚至都没试着不去做。我想要。比我自己预想的还要想要。{/color}"
        "{color=#66ff33}在这件事发生之前他一直是个可靠的人，之后更是我的支柱。一直在支持我。而且……也许我对他有吸引力；如果情况有一点点不同，我也不会这么做。我丈夫正在操别的女人。我们被困在这儿。孤单。{/color}"
        scene c004_s012_007 with Dissolve(0.25)
        "{color=#66ff33}我应该为此感到内疚，但那几乎是我现在唯一没有的感觉。{/color}"
        "{color=#66ff33}可那其实并不重要，我不该让自己分心。{/color}"
    scene blank with Dissolve(2)
    scene c004_s011_030 with Dissolve(2)
    "费了一番功夫翻检食物、挑出还能吃的之后——比我第一次发现这个地方时希望的要少得多——卡莉告诉我她都搞定了。翻译过来就是「从我厨房里出去」。"
    scene c004_s011_031 with Dissolve(0.25)
    "我把这理解成：她需要觉得自己有用，而做饭这件事本身就足以让她分心。再说，也许她想找个人放哨。上次来的时候压力很大，留个心盯着潜在的麻烦也不坏。"
    if ch4_burnedone_1_seen == "yes":
        "不过既然那只怪物（我迟早得给它起个名字）已经死在排水沟里了，还有什么好担心的？假设它是跟着我们一路从办公室来的。"
        "不过，留意其他幸存者也不是坏主意。劳拉当初就是从雾里直接撞上我们的。外面肯定还有别人。"
    scene c004_s011_032 with Dissolve(0.5)
    k "好了，弄完了。我都快干成手了。可惜我们不会在这儿待太久了。"
    j "这技能可以迁移。*轻笑* 再说了，你要是愿意，也可以去当个快餐厨子。"
    scene c004_s011_033 with Dissolve(0.25)
    k "*咯咯笑* 也许吧。不过我还是不想在餐饮业干。我们手上有的东西我都尽力处理了。靠这些应该能撑几天。也许我们都不会待那么久。"
    j "确实。嘿，反正我还没脱装备，你穿衣服的时候我把东西都打包好。"
    scene c004_s011_034
    k "呃，好。谢谢。你看到什么了吗？"
    j "没有。什么都没有。这儿就我们俩。"
    stop music fadeout 2.0
    scene c004_s011_035 with Dissolve(0.25)
    k "好。"
    scene c004_s011_036 with Dissolve(0.5)
    "{color=#ffcccc}现在的「什么都没有」，我倒是能接受。只要有五分钟，不用觉得外面的世界在跟我们作对。只要外面什么都没有能伤害我们。{/color}"
    play music horror fadein 3.0
    scene c004_s011_037 with Dissolve(0.25)
    "{color=#ffcccc}可这要求也太高了。就连空气都想杀死我们。而离开这里感觉像件不可能的事。我的意思是，我们也许得徒步走出去，这计划就算在一切正常的时候都算疯狂透顶。{/color}"
    scene c004_s011_039 with Dissolve(0.25)
    "{color=#ffcccc}我从来没想过，跑越野这项技能日后还能派上用场。{/color}"
    scene c004_s011_040 with Dissolve(0.25)
    $ k_anxiety += 1
    k "哦。呃……"
    j "{size=30}好吧，我全塞进一个袋子里了。勉勉强塞下。等我们……的时候得小心点。{/size}"
    scene c004_s011_041 with Dissolve(0.5)
    j "卡莉？你没事吧，姑娘？"
    "她没反应。她是不是……"
    scene c004_s011_042 with Dissolve(0.5)
    if ch4_burnedone_1_seen == "yes":
        k "又、又来一个？"
        j "靠。又来一个？"
    else:
        k "它、它在那儿……"
        j "操。"
    scene c004_s011_043 with Dissolve(0.25)
    j "卡莉，快走。"
    "她彻底僵住了，像被车灯照住的鹿。一动不动。我得把她弄出它的视线。"
    scene c004_s011_044 with hpunch
    "在它看见我们之前先躲起来。"
    j "就在这儿。待在这儿。我不知道它有没有看见我们。"
    scene blank with Dissolve(1)
    scene c004_s011_045 with Dissolve(1)
    if ch4_burnedone_1_seen == "yes":
        "我不确定它能看清我们多少。有雾，又有晨光从玻璃上反射。不过我一点不想拿运气去试，尤其既然我们知道外面不止一个。有多少个？"
        "他妈的一点线索都没有，不过现在不是弄清楚这个的时候。先安全脱离这个状况，然后再说这些王八蛋到底有多少。"
        scene c004_s011_046 with Dissolve(0.25)
        "卡莉在发抖。我觉得她最近受的惊吓已经太多了。洗手间里的尸体、巷子里那只死掉的生物，现在又发现还有一只，我能理解她那点可怜的勇气大概已经用光了。"
    else:
        "我不确定它能看清我们多少。有雾，又有晨光从玻璃上反射。不过我一点不想拿运气去试，尤其是它能像巅峰时期的迈克·泰森那样把迎面砍来的斧子甩开。"
        scene c004_s011_046 with Dissolve(0.25)
        "卡莉在发抖。我觉得她最近受的惊吓已经太多了。洗手间里的尸体、之前我们被袭击、现在它又冒出来，我能理解她那点可怜的勇气大概已经用光了。"
    j "没事。我觉得它没看见我们。"
    scene c004_s011_047 with Dissolve(0.25)
    "我知道她最近一直很害怕。她自己跟我说的。而且理由充分。这简直是好莱坞恐怖片那套东西。她还是能克服恐惧跑出来帮忙，这一点说明了很多。大概一半是想证明自己有用，一半是倔。她不想成为累赘。"
    menu:
        "告诉她没事。":
            scene c004_s011_048 with Dissolve(0.5)
            j "嘿，没事的。没事。它没看见我们。我们在这儿很安全。我们像上次那样等它过去就好。"
            "不知道这有没有用。听起来她像是在憋着眼泪。也许就先抱着她吧。"
            if ch4_burnedone_1_seen == "yes":
                j "就算它真的看见我们，我手里还有那把斧子。我已经解决掉一只了。这只我也一样。"
            else:
                j "就算它真的看见我们，我手里还有那把斧子。也许这次我会留下来，看看多砍几下会怎样。"
            scene blank with Dissolve(1)
            scene c004_s011_049 with Dissolve(1)
            "努力当了几分钟温暖安心的抱枕之后，我决定偷偷往外瞄一眼。"
        "告诉她你为她骄傲。\n[rgr](卡莉 信任 +1)":
            $ k_trust += 1
            scene c004_s011_048 with Dissolve(0.5)
            j "嘿。我为你骄傲。我知道你在害怕。可你还是跑出来帮忙了。我很感激。劳拉也是。所以害怕也没关系。我们把这东西熬过去，我们会既安全又聪明，好吗？什么都不会发生。我不会让它得逞。"
            "不知道这有没有用。听起来她像是在憋着眼泪。也许就先抱着她吧。"
            scene blank with Dissolve(1)
            scene c004_s011_049 with Dissolve(1)
            "努力当了几分钟温暖安心的抱枕之后，我决定偷偷往外瞄一眼。"
        "看看那东西在哪儿。":
            scene c004_s011_049 with Dissolve(0.5)
            "让我探头看一眼，看看能不能找到我们那位朋友。"
    "什么都没有。或者说，我什么都没看见。这雾把能见度压得太差了，几码之外就什么都看不清。外面简直像一场{a=https://en.wikipedia.org/wiki/Fog_Bowl_(American_football)}雾战{/a}。"
    j "看起来我们这边是干净的。也许我们该收拾一下，离开这儿。卡莉？"
    scene c004_s011_050 with Dissolve(0.25)
    j "嘿，嘿，没事了。"
    "我知道现在不是时候，可她的眼睛有多漂亮，还是让我短暂地愣了一下。"
    if ch4_burnedone_1_seen == "yes":
        scene c004_s011_051 with Dissolve(0.25)
        k "我、我很抱歉。*吸鼻子* 我只是……我讨厌这样。我只想这一切赶紧结束。我让自己以为看见它死了我们就安全了，可还有一个。外面有多少只根本没谁知道。"
        scene c004_s011_052 with Dissolve(0.25)
        j "目前我们只见过一只死的和一只活的。这个我们应付得来。但我们得离开这儿。我们就努力做到不用再回来。努力到医院去。走出这个镇子。"
    else:
        scene c004_s011_051 with Dissolve(0.25)
        k "我、我很抱歉。*吸鼻子* 我只是……我讨厌这样。我只想这一切赶紧结束。"
        scene c004_s011_052 with Dissolve(0.25)
        j "我知道，我也是。可现在我们先离开这儿。我们就努力做到不用再回来。努力到医院去。走出这个镇子。"
    k "*叹气* 我……大概吧。"
    scene blank with Dissolve(1)
    scene c004_s011_053 with Dissolve(1)
    "卡莉穿好装备的时候，我回去拿了那个塞得满满当当、还温着的食物袋。"
    j "都拿到了。闻着不错。所以至少我们有一顿热饭可以期待。"
    scene c004_s011_054 with Dissolve(0.25)
    k "对……给。跟你换。"
    j "要是你想留着斧子——"
    k "不，你更强。我大概拿着它也做不了什么。或者做不了什么有用的事。"
    scene c004_s011_055 with Dissolve(0.25)
    j "好吧，如果你不介意强化一下性别角色的话。*轻笑*"
    k "*咯咯笑* 好吧……"
    "她眼里有了一点笑意。这比几分钟前好多了。"
    scene c004_s011_056 with Dissolve(0.25)
    "回程的路绷得很紧但没出什么事。受了惊的卡莉一路上都没说话。感觉我们怎么都躲不过这一劫，所以我不怪她沉默。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_26_1232", transition=Dissolve(1.0))()
    pause
    $ Hide("june_26_1232", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday fadein 2.0
    scene c004_s013_001 with Dissolve(2)
    "我们回来时劳拉居然在等着，我挺意外的。也许她听见我们上来了。"
    l "你们回来了。还顺利吗？"
    scene c004_s013_002 with Dissolve(0.25)
    j "不太顺利。"
    l "给，我帮你拿。"
    k "好。我、我要去冲一下。"
    scene c004_s013_003 with Dissolve(0.25)
    l "当然。我们去隔间那边摆东西。别太久。"
    k "……"
    scene c004_s013_004 with Dissolve(0.25)
    l "呃，她没事吧？看起来不太对。发生什么了？"
    j "给，让我一边脱这身脏衣服一边跟你说说。"
    scene c004_s013_005 with Dissolve(1)
    l "怎么了？她看起来像是哭过。"
    if ch4_burnedone_1_seen == "yes":
        j "长话短说：我在巷子里发现了之前袭击我们的那只生物，已经死了。我们去了餐馆，做了些吃的。我从厨房出来的时候，她正盯着外面另一只游荡的生物看。那把她吓得不轻，我们等它走开才赶紧离开。"
    else:
        j "长话短说：我们顺利到了餐馆，做了些吃的。我从厨房出来的时候，她正盯着之前袭击我们的那只生物，那家伙跟没事人一样四处乱走。那把她吓得不轻，我们等它走开才赶紧离开。"
    scene c004_s013_006 with Dissolve(0.25)
    j "她受了不小的惊吓，我觉得这一切——一件狗屁事接着一件、完全没有喘息的机会——终于把她压垮了。我能理解。她一直硬撑着装勇敢，可再加上跟世界断了联系，人就变成这样了。"
    l "我懂。相信我，我真懂。"
    scene c004_s013_007 with Dissolve(0.25)
    if ch4_burnedone_1_seen == "yes":
        l "所以，又来一个？不止一个？这是不是说明外面有很多只？"
        j "这个假设很合理。靠，我们留在办公室那边的那只说不定还在。"
        scene c004_s013_008 with Dissolve(0.25)
        l "三只？还是更多？"
        j "我没有答案，劳拉。就像我不知道它们从哪儿来一样。那只死的——我们只花了一点点时间查看——看起来以前可能曾经是人。也可能。可它们被烧得、变异得太厉害，已经很难在里面看出一个真正的人了。那完全是《毒液复仇者》和《食人猪》那种东西。"
    else:
        l "所以，一斧子砍脸上还不足以杀死它？"
        j "我那时候是在乱挥。我什么都看不见。可能只是擦到了。这里面有太多问题，而我在这儿一个答案都给不出来。说实话，我没那么聪明。"
        scene c004_s013_008 with Dissolve(0.25)
        j "我不知道它从哪儿来。就我看到的，它以前可能曾经是人。也可能。可它被烧得、变异得太厉害，已经很难在里面看出一个真正的人了。那完全是{a=https://www.imdb.com/title/tt0090190/}《毒液复仇者》{/a}和{a=https://www.imdb.com/title/tt0087015/}《食人猪》{/a}那种东西。"
    scene c004_s013_009 with Dissolve(0.25)
    j "我……我现在没什么胃口。而且我自己也得冲一下。后脖子被那玩意儿弄得火辣辣的。"
    l "我该去看看卡莉。确认她没事。"
    scene c004_s013_010 with Dissolve(0.25)
    j "要不要先把食物放这儿？"
    l "对，对。我试试让她吃点东西。我们都靠这点东西吊命，每天吃这么少。吃顿热的总会有点用。所以，别不吃。"
    j "我不会。就是需要……先从这一切里出来，冲一下。"
    scene c004_s013_011 with Dissolve(0.25)
    j "哦，我走之前问一下，你找到钥匙了吗？"
    l "没有。我倒是去车库看过那辆 SUV 了。是个好东西。可我还没看到遥控钥匙。五楼和六楼有几间办公室我进不去。"
    j "因为我把「老砍柴」带走了？"
    scene c004_s013_012 with Dissolve(0.25)
    l "正是。{size=32}天哪，这名字真蠢。{/size}"
    j "这个以后再说吧。"
    l "对。现在有更急的事。"
    scene blank with Dissolve(2)
    scene c004_s013_013 with Dissolve(2)
    l "{size=32}卡莉？你还好吗，亲爱的？我能进来吗？你穿好了吗？{/size}"
    k "*吸鼻子* 好了。"
    play sound doorclose
    scene c004_s013_014 with Dissolve(0.25)
    k "反正我们也不是没在同一间屋子里脱过衣服。剩下的隐私也没多少了，对吧？"
    if l_sex >= 1:
        l "也是，不过也许我还想保住最后那么一点。这样我还能说，你我没互相看过对方光着身子。"
        scene c004_s013_016 with Dissolve(0.25)
        k "嗯？"
        l "没什么。亲爱的，我听说这次挺吓人的。你会没事吗？"
    else:
        l "也是，不过也许我还想保住最后那么一点。这样我还能说，我没看过你们俩任何一个完全脱光的样子。"
        scene c004_s013_016 with Dissolve(0.25)
        k "谢谢。"
        l "亲爱的，我听说这次挺吓人的。你会没事吗？"
    scene c004_s013_017 with Dissolve(0.5)
    k "不会，但我也没什么选择，对吧？"
    l "*叹气* 我知道。对不起。你不是一个人扛。我感觉也差不多。我只能告诉你，你可以相信我和[player_name]会尽力让你安全，把我们所有人带出这里。"
    scene c004_s013_018 with Dissolve(0.25)
    k "可我受够了自己不够坚强。我不想只是被人照顾。我、我……我觉得自己像个孩子。我看见那怪物，整个人就缩成了个小女孩，怕着床底下的恶魔。"
    l "你做得挺好。我们每个人都需要彼此。你害怕是很正常的反应。所以，别去计较现在是谁扛得更多。我们每个人都在为这个集体尽自己那份力。再说了，你做的饭是我们俩谁都比不上的。"
    scene c004_s013_019 with Dissolve(0.25)
    l "说到这个……"
    k "我不饿。"
    scene c004_s013_020 with Dissolve(0.25)
    l "饿不饿都得吃。我们已经只剩一天一顿了。所以你必须吃。来。趁还没凉。"
    k "*叹气* 好吧。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_26_756", transition=Dissolve(1.0))()
    pause
    $ Hide("june_26_756", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain fadein 2.0
    scene c004_s014_001 with Dissolve(2)
    "花了好几小时试着撬开几扇门，结果发现又只是些空办公室之后，我的体力开始往下掉。上一顿那点有限的热量加上这趟外出，到下午我已经完全是靠意志在撑。"
    "站在那儿，目光几乎没法聚焦在我们看到的景象上，我一边努力理清我们的处境，脑子就飘走了。食物选择越来越少，又加上救援在好几英里外这种种假设，我们得比原计划更早动身。"
    scene c004_s014_002 with Dissolve(0.25)
    "我不想把全部希望都押在一辆打不着火的车上，可另一个选择——徒步走——不管在时间还是体力上都不是最优。劳拉能走多远，我们才不得不找地方躲一躲？"
    if ch4_burnedone_1_seen == "yes":
        "而且如果外面不止一只那种生物，我们就得尽力避开它们。上次我想硬碰硬的经历，我可不想再来第二次。没有什么比像被人踹了肺一脚更难受的了。"
    else:
        "还有外面那位朋友？我们得尽力避开它。只希望我们能跟它拉开距离，因为上次我想硬碰硬的经历，我可不想再来第二次。没有什么比像被人踹了肺一脚更难受的了。"
    scene c004_s014_015 with Dissolve(0.25)
    l "{size=30}[player_name]！你在哪儿？！{/size}"
    j "在这儿。会议室！"
    play sound doorclose
    scene c004_s014_003 with Dissolve(0.5)
    l "你在这儿。刚才还数落我在这儿一站就是好几个小时。"
    j "我不是在找借口，只是我实在没力气了，就在这儿停了一会儿。而且要是能看到点有用的东西，那就更好了。"
    scene c004_s014_004 with Dissolve(0.5)
    l "你看到了吗？"
    j "没有。也许有几只鸟，但它们太远了，什么都有可能。现在我只是在琢磨，要是去医院，我们该往哪个方向走。"
    scene c004_s014_005 with Dissolve(0.25)
    l "在大学校园的另一边。那个方向。你以前开车去过那儿，对吧？"
    j "不是从这儿出发。不过对。我猜一上路，我的方向感就回来了。钥匙有消息吗？"
    scene c004_s014_006 with Dissolve(0.25)
    l "有的话我肯定先说这个了。"
    j "大概吧。不过，也许你是想风趣一点，在一个更有戏剧性的时刻宣布。我们的生活好像就是这样。"
    scene c004_s014_007 with Dissolve(0.25)
    l "要是找不到钥匙呢？"
    j "那我们就得想好下一个落脚点。也许就这么一直走。用脚从一个地方挪到下一个。商店。仓库。什么都行。外面的情况看起来并没有好转。所以明天我出去侦察一下，看看东边那些楼是什么情况，我们能不能拿一栋当临时庇护所。"
    j "而且这里还有时间这一层因素。到某个时候——如果他们真在从医院撤离人员——那他们就会默认其他还活着的人都完了。"
    scene c004_s014_008 with Dissolve(0.25)
    l "*叹气* 他们真会把这一带当成没救了吗？"
    j "不是我想再提，可我们在切尔诺贝利和福岛隔离区都干过这种事。"
    l "对……"
    scene c004_s014_009 with Dissolve(0.5)
    j "卡莉怎么样？我们回来之后我就没见过她。"
    l "她没事。吃了东西之后好多了。她很累、压力很大，我觉得这一切对她来说压得太满了。还有，别暗示她不用做任何事。她想派上用场。跟我一样。"
    j "你不会被晾到边线上的，劳拉。"
    $ renpy.sound.set_volume(.20, 0.0, channel = "sound")
    scene c004_s014_010 with Dissolve(0.25)
    l "我知道。可我的意思是，我们现在都绷成这样了，就该互相照应。所以，如果我得戴上「妈妈」那顶帽子听她说话，那我戴就是了。而如果你发现我们当中谁在钻牛角尖——"
    j "比如电视或者这片风景？我保证会指出来。"
    l "好。那就——"
    play sound gunshot
    scene c004_s014_011 with vpunch
    "*咔嚓*"
    l "什么？靠！"
    j "靠。是枪声。那是从哪儿来的？"
    scene c004_s014_012 with Dissolve(0.5)
    l "很难判断。我觉得是从南边。"
    j "至少我们知道了外面还有别人。这个镇子上的枪可不少，我有点意外我们到现在还没听到更多。"
    l "我们要不要考虑给斧子找点升级？"
    scene c004_s014_013 with Dissolve(0.25)
    j "要是能找到枪械？没错。而且我们最好把遇到的每个人都当成潜在威胁。这种局面往往会侵蚀人的底线和善意。狗咬狗的局面，尤其是当他们觉得我们身上有什么值钱东西的时候。"
    l "我本以为自己已经不可能对这个局面感觉更糟了。"
    j "抱歉。"
    $ renpy.sound.set_volume(1.0, 0.0, channel = "sound")
    scene c004_s014_014 with Dissolve(0.25)
    "{color=#66ff33}现在大概不是提我前几天跟卡莉那次谈话的好时机。她和安德鲁的关系有些不对劲。不过，除了母亲的直觉，我真的有足够的依据吗？并没有。{/color}"
    "{color=#66ff33}最好别把这事塞到[player_name]脑子里。他已经一心扑在怎么把我们弄出去了。{/color}"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_26_1123", transition=Dissolve(1.0))()
    pause
    $ Hide("june_26_1123", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c004_s015_001 with Dissolve(2)
    "太阳落山之后，也没什么别的可做。电视还是只有静电，城市落入黑暗。有几扇窗还亮着灯，这意味着城市还有电。"
    "电……那能撑多久才会变成问题？又多一件要担心的事吧。"
    "累坏了，我倒在长椅上，几分钟就睡着了。"
    if k_friend >= 7:
        scene blank with Dissolve(2)
        scene c004_s015_002 with Dissolve(2)
        play music nightmain2 fadein 2.0
        k "{size=28}[player_name]？你、你醒着吗？我……{/size}"
        "那是……卡莉？肯定是在做梦。可要是我不是呢？"
        scene c004_s015_003 with Dissolve(1)
        j "唔嗯……卡莉？几点了？"
        k "很晚了。还在夜里。"
        scene c004_s015_004 with Dissolve(0.5)
        j "出什么事了吗？"
        k "没、没有。也不是那种事。我、我们没事。别担心。拜托。"
        scene c004_s015_005 with Dissolve(0.5)
        j "好吧~~~怎么了？"
        k "我……我很难睡着。我一直做噩梦，然后醒过来，四周一片黑……而且每次听见楼体吱呀作响，我就开始崩溃。"
        "雾第一次打过来之后，我们所有人都有点懵了圈。她保持高度警觉完全说得通。靠，光今天这一天就足够把任何正常人折腾垮。"
        scene c004_s015_007 with Dissolve(0.25)
        j "没事的。我们在这儿很安全。我知道这话大概对你的失眠没什么帮助。"
        k "你能不能……*咽口水*"
        scene c004_s015_008 with Dissolve(0.25)
        k "能不能……抱着我。就在沙发上。我……我想如果有个温暖的身体——如果因为有人在旁边而觉得安全——我也许就能睡着。"
        j "随便哪个温暖的身体，对吧？"
        scene c004_s015_009 with Dissolve(0.25)
        k "不，不是……我不是那个意思。我只是习惯了……"
        "跟人一起睡。"
        scene c004_s015_010 with Dissolve(0.5)
        j "没关系。要是地方够大，我想睡沙发对我来说算升级了。而且我懂。南希走了之后的头几个月，我也是很难面对那张冷冰冰的空床。"
        k "谢、谢谢。"
        scene blank with Dissolve(1)
        scene c004_s015_011 with Dissolve(1)
        k "我为……道歉。"
        j "别道歉。这段时间发生的事太吓人了，所以你能这样完全可以理解。看恐怖片是一回事，活在恐怖片里是另一回事。"
        scene c004_s015_012 with Dissolve(0.25)
        k "大概吧。我讨厌自己被缩成一个小女孩，因为夜里那些窸窸窣窣的东西就抖得像片叶子。"
        j "我不那么看你，卡莉。面对这种狗屁倒灶的事，你做得很好了。"
        scene c004_s015_013 with Dissolve(0.25)
        k "我、我大概吧。"
        scene c004_s015_034 with Dissolve(0.5)
        k "只是……我真的从来没有一个人待过这么久。我以前跟家人住在家里——跟妹妹莉丝贝特挤一个房间。"
        k "后来我跟安德鲁住到一起，再后来我们搬到南边，我就一直没有独处过。从来没有这么久。"
        j "你不是一个人，卡莉。劳拉和我都在。我们不会走。至少不会丢下你一个人走。"
        scene c004_s015_035 with Dissolve(0.25)
        k "我、我知道。可睡在沙发上，房间里没有别人。我……一个人在黑暗的房间里醒来就会慌。会迷失方向。有一瞬间不知道自己身在何处。而等我想起来的时候……"
        j "你想起来自己不在家？还有外面所有那些狗屁事？"
        scene c004_s015_036 with Dissolve(0.25)
        k "对。"
        j "我懂。下次再害怕地醒来，你一定要抓住我们当中一个。就像今晚这样。我们得互相照应。"
        "因为心理健康和身体一样重要。等我们出去了，我们每个人都会一塌糊涂，但也许到时候能少糊一点就好了。"
        scene c004_s015_014 with Dissolve(0.25)
        k "我……我知道我们以前不算亲近，像朋友那种，但我很感激你在这儿。"
        j "是因为我搜刮东西和挥斧头的本事吧。*轻笑*"
        scene c004_s015_015 with Dissolve(0.25)
        k "不不。你……我知道你是在开玩笑，可你和劳拉……"
        j "你不用说了。反正我们现在已经是朋友了。"
        scene c004_s015_016 with Dissolve(0.25)
        k "*咯咯笑* 好吧。"
        j "工作上的朋友，对吧？我已经升级到那一级了，对吧？*轻笑*"
        scene c004_s015_017 with Dissolve(0.25)
        k "打住。不止那级。*打哈欠*"
        "共同经历过的创伤，会让我们三个人比原先预想的亲近得多。"
        scene c004_s015_018 with Dissolve(0.5)
        "她好像平静下来了。希望她很快就能再睡着。"
        k "我……我……{size=28}喜欢你……{/size}"
        scene blank with Dissolve(2)
        scene c004_s015_019 with Dissolve(2)
        "我不知道过了多久，我迷迷糊糊打了个盹。外面还是黑的。"
        "卡莉睡着了，从声音判断是睡得很沉，大概也是她早就需要的睡眠。她做噩梦做了多久？也许一开始还没有，但我不会奇怪于我们被困得越久、那些梦就变得越糟。"
        scene c004_s015_033 with Dissolve(0.25)
        "我因为她今晚没事而松了口气，正考虑悄悄溜走。确实，跟一个可爱的年轻姑娘「同床」挺不错，可她已经跟别人订婚了。对，尽管是她主动要求的，但也许我该像个绅士一点。"
        if l_sex >= 1:
            "再说了，我已经在往劳拉身体里插了。我不需要再掺和进（或者制造）更多感情上的麻烦。"
        menu:
            "从那儿出来。":
                scene c004_s015_020 with Dissolve(0.5)
                "对，我们慢慢溜出去。真舍不得这份温暖——而且天啊她闻起来真香——但这样才对。"
                scene c004_s015_021 with Dissolve(0.25)
                "别醒过来，卡莉。拜托。"
                scene c004_s015_022 with Dissolve(0.25)
                "好了，我出来了。回到我的长椅。天哪，这感觉跟南希和我刚开始闹掰的第一个月一模一样。被赶回这楼里最差的地方睡觉。"
            "再多待一会儿。\n[rgr](卡莉 好感 +1)\n[rgr](卡莉 焦虑 -1)":
                $ k_anxiety -= 1
                $ k_friend += 1
                scene c004_s015_023 with Dissolve(0.5)
                "我不会把这变成习惯。不过，也许我自己也想睡上几个小时。因为这份共享的温暖我也需要。我会在她醒来之前溜走。早点。"
                "天哪，她闻起来真香。我都忘了有多好闻……"
                if k_desire >= 3:
                    scene blank with Dissolve(2)
                    scene c004_s015_024 with Dissolve(2)
                    "我醒了……好吧，也不算真的醒了……就是那种半睡半醒、眼睛再闭上一下就能重新睡着的状态。外面还是黑的，但借着附近走廊的光，我能看见卡莉脸的轮廓。"
                    scene c004_s015_025 with Dissolve(0.5)
                    k "唔嗯……"
                    "她是在做噩梦吗？听起来不像。那是别的什么声音。像是一声……的呻吟。"
                    "哦，等等。呃……"
                    $ k_desire += 1
                    scene c004_s015_026 with Dissolve(0.5)
                    "一只乱摸的手蹭到了我的鸡巴。我可不会自欺欺人地把这当成什么别的东西——不过是两个人挤在这么窄的地方，其中一个睡着了，手就落在了不该落的地方而已。靠，我居然还没把她其中一个奶子压塌，也算奇迹了。"
                    scene c004_s015_027 with Dissolve(0.25)
                    k "哈啊~~~"
                    "唔……那是……有人在摸。大概以为身边是安德鲁。我挪一下。"
                    scene c004_s015_028 with hpunch
                    "好，找到了。现在不是弄点温柔手活的时候，我们还没到那一步。"
                    scene c004_s015_029 with Dissolve(0.5)
                    "算了，我还是溜出去吧。真舍不得这份温暖，但这样才对。我知道她不是故意的，最好还是抵抗一下诱惑。"
                    scene c004_s015_021 with Dissolve(0.25)
                    "别醒过来，卡莉。拜托。"
                    scene c004_s015_022 with Dissolve(0.25)
                    "好了，我出来了。回到我的长椅。天哪，这感觉跟南希和我刚开始闹掰的第一个月一模一样。被赶回这楼里最差的地方睡觉。"
                else:
                    scene blank with Dissolve(2)
                    scene c004_s015_030 with Dissolve(2)
                    "我醒来的时候天还很早。卡莉还睡着。她看起来几乎像是松了口气，哪怕只是一瞬间。"
                    "不过我已经待得够久了，我怀疑卡莉不会再像昨晚那样希望我留下。"
                    scene c004_s015_031 with Dissolve(0.25)
                    "别醒过来，卡莉。拜托。尽可能多休息一会儿。"
                    scene c004_s015_032 with Dissolve(0.25)
                    "好了，我出来了。不如先冲一下，看看情况怎么样。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_27_1011", transition=Dissolve(1.0))()
    pause
    $ Hide("june_27_1011", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday fadein 2.0
    scene c004_s016_001 with Dissolve(2)
    "到了白天过了几个小时，我们喝完早上的咖啡，制定了继续搜这栋楼的计划。到现在，我们都在勉强维持精力。休息不足、三餐不济，正在慢慢拖垮我们。"
    scene c004_s016_002 with Dissolve(0.5)
    "想到这一点，我想继续推进，把最后几间办公室也打开。拼上几个小时，说不定能摸清这里还剩些什么。要是找不到 SUV 的钥匙，我们就得动身去下一个落脚点。"
    scene c004_s016_003 with Dissolve(0.25)
    "至于下一个落脚点在哪儿，得靠我们去发现。应劳拉的要求，我提议的侦察行程被推到了第二天。她的谨慎没错；我从前一天就累得够呛，我们的时间花在这儿更划算。"
    k "我要去看看最后那两扇门。我觉得前天我们漏掉了。"
    scene c004_s016_004 with Dissolve(0.25)
    l "呃，好。我再把这间办公室最后看一遍，然后就算它完了。"
    k "唔嗯~~~" with vpunch
    scene c004_s016_005 with Dissolve(0.25)
    "{color=#ffcccc}锁着。等[player_name]回来我告诉他。他还在楼上，对吧？{/color}"
    scene c004_s016_006 with Dissolve(0.25)
    "{color=#ffcccc}那这扇……{/color}"
    scene c004_s016_007 with hpunch
    u "{size=30}呃嗯~~~！！{/size}"
    "{color=#ffcccc}什么情况？里面有人。我听见动静了。{/color}"
    "{color=#ffcccc}还有，那是不是有雾从门缝底下漏出来？{/color}"
    scene c004_s016_008 with vpunch
    k "劳拉！！！劳拉！"
    if persistent.ch4_complete == False:
        $ persistent.ch4_complete = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_chapter4", transition=slideright)()
        pause
        $ Hide("achievement_chapter4", transition=dissolve)()
        $ quick_menu = True
label chapter05:
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("chapter05", transition=Dissolve(1.0))()
    pause
    $ Hide("chapter05", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c005_s001_001 with Dissolve(2)
    play music horror fadein 2.0
    u "{size=30}唔嗯~~~ 唔~~~{/size}"
    j "好吧，我确实听见了。"
    scene c005_s001_002 with Dissolve(0.25)
    l "嘿！你在里面还好吗？我们是来帮忙的。要是你能把门开一下——"
    j "等一下，劳拉。"
    scene c005_s001_003 with Dissolve(0.25)
    l "什么？我们不能等——"
    k "有雾漏出来。下面那边。"
    j "这个。我不知道这情况持续多久了，但它是个问题。而且我对这件事的感觉很不好。里面那个人肯定知道我们已经在这儿一阵子了。要是他躲在这儿，为什么我们到现在才听到动静？除非这是{i}新{/i}出的状况。"
    scene c005_s001_004 with Dissolve(0.25)
    l "我们不能就这么把他留在里面。他听起来情况很不好。我知道那是什么感觉。"
    k "可他把自己锁在里面了。"
    j "如果他被雾暴露着呢？那我信。那自然会有一些问题：怎么做到的？他开窗了？我以为在这样的楼里根本不可能。那他在多久了？"
    scene c005_s001_005 with Dissolve(0.25)
    k "要是 SUV 的钥匙就在他手上呢？"
    j "靠。对……"
    scene c005_s001_002 with vpunch
    u "{size=30}唔嗯呃~~~{/size}"
    l "[player_name]~~~？我们不能再等了。"
    j "靠。好吧。"
    "这让我后脖颈的汗毛都竖起来了。我有种不祥的预感，但也看不出多少更好的主意。我得赶紧进去把那个人拉出来。到走廊的安全地方再说。"
    scene c005_s001_006 with Dissolve(0.25)
    j "好了，女士们，退后。我要乱挥一轮。"
    l "[player_name]，小心。我对这事没什么好感。"
    scene c005_s001_007 with Dissolve(0.25)
    j "嘿，里面不管是哪位：你最好离门远点。最后给你一次机会把门开开，不然我就要硬闯了。"
    "没人应答？我不知道我进去的时候那个人会是什么状态。"
    play sound woodchop
    scene c005_s001_008 with hpunch
    j "唔嗯！！！"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene white with Dissolve(2)
    scene c005_s001_010 with Dissolve(2)
    j "我的天。*咳嗽* *咳嗽*"
    "那扇窗……肯定有人把它砸开了。什么样的白痴会干这种事？是想跳下去？还是指望喊救命？靠，也许有人一时崩溃，直接来了句「去他妈的吧，让雾把我带走」。"
    scene c005_s001_011 with Dissolve(0.25)
    "能见度糟透了。这儿已经积了一堆雾。这他妈的人到底在哪儿？照这个速度我肯定会绊到他。本来应该速战速决的。时间紧迫。也许在办公桌后面。"
    l "[player_name]！？"
    j "退后。这里面乱成一团。*咳嗽*"
    scene c005_s001_012 with hpunch
    play music monster
    u "唔嗯呃~~~！" with vpunch
    j "靠！"
    "靠，这儿有一只。靠！"
    l "[player_name]！？你——你没事吧——"
    play sound gas
    scene c005_s001_013 with flashyellow
    j "*咳嗽* 操操操~~~"
    "它靠得太他妈近了。得……不能让它出这个房间。不能让它跟着她们进走廊。几乎什么都看不见。什么都看不见。靠，这玩意儿烧得要命。得做点什么。"
    scene c005_s001_034 with Dissolve(0.25)
    if ch4_burnedone_1_seen == "yes":
        "必须反击。我知道它们能被杀死。这是唯一能阻止它跑出去的办法。"
    else:
        "必须反击。这是唯一能阻止它跑出去的办法。"
    scene c005_s001_014 with hpunch
    j "呃啊啊啊~~~！！！"
    play sound axehit
    scene c005_s001_015 with flashred
    "*咔——咚* *噗叽*" with hpunch
    play sound gas
    scene c005_s001_016 with flashyellow
    j "*咳嗽* *咳嗽*" with hpunch
    "操，我几乎什么都看不见。不能再跟这玩意儿玩打地鼠了。得试着把它打倒。也许能打死它。"
    play sound axehit
    scene c005_s001_017 with flashred
    "*咔叽*" with hpunch
    scene c005_s001_018 with vpunch
    j "*咳嗽* *咳嗽* 哈啊~~~"
    "打飞了。用力不小。我闻到血味了。靠，皮肤好疼。"
    scene c005_s001_035 with Dissolve(0.25)
    "我觉得我把它从窗户砸出去了。应该是。很难说清。有玻璃碎裂的声音。肉砸在金属上的声音。要是我猜对了，那真是走运。"
    scene c005_s001_019 with Dissolve(0.25)
    l "[player_name]！怎么回事？我们什么都看不见。你还……算了，我进去。"
    j "不不 *咳嗽*。等一下。" with hpunch
    scene c005_s001_020 with Dissolve(0.5)
    "我他妈什么都看不见。还有这窗为什么他妈开着？我只知道那个王八蛋已经不在里面了。"
    scene c005_s001_036 with Dissolve(0.25)
    "碎玻璃。有人把它砸开了。怎么砸的？为什么？靠，我不能……只是在里面瞎摸，情况一秒比一秒糟。得先出去，重新整理一下。回头再进来。"
    l "[player_name]！天哪，到底怎么了？"
    scene c005_s001_021 with Dissolve(0.25)
    j "现在没事了。别*咳嗽*进来。我这就出来。"
    scene c005_s001_022 with Dissolve(0.25)
    "我的天，我真不该只穿着短裤和背心就冲进来。我他妈的皮肤像烧着一样。急着去救「某个人」，压根没想到会是{b}那种{/b}东西。"
    scene c005_s001_023 with Dissolve(0.25)
    "得离开这儿。到走廊去，在那儿我也许能喘口气。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c005_s001_024 with Dissolve(2)
    play music insidedark fadein 2.0
    l "哦，[player_name]。靠，你有没有——有没有——"
    j "哈啊~~~ *咳嗽* 操。" with hpunch
    k "啊呜~~~ 哦天啊。"
    scene c005_s001_025 with Dissolve(0.25)
    j "*咳嗽* 里面有一只 *咳嗽* *咳嗽*。不只是个什么男人。"
    l "当然。我们能听见你。也能看见一部分。闻得到。你他妈真走运。疯了但走运。你本来该退出来的。来来来。让我看看。"
    "退不了。它会跑出房间，那我们两个都完蛋。"
    scene c005_s001_026 with Dissolve(0.25)
    l "靠，你的脸。我们得把你冲干净。"
    j "*咳嗽* {size=32}看不清。被近距离喷了两下。我们得{/size}*咳嗽*……"
    k "它、它还在里面吗？"
    scene c005_s001_027 with Dissolve(0.25)
    j "{size=32}两下{/size}*咳嗽* {size=32}应该够。不，{/size} *咳嗽* {size=32}现在不够了，我觉得它从开着的窗那儿掉出去了。{/size}"
    k "我们得处理一下那扇窗。"
    j "{size=32}砸开了{/size} *咳嗽*…… {size=32}别不戴{/size}*咳嗽* {size=32}口罩就进去。外套。{/size} *咳嗽* {size=32}真是一场灾难。得赶紧封上。{/size}" with vpunch
    l "靠，靠！卡莉，我得送他去洗手间。它……它溅了你一身。操，情况很糟。"
    scene c005_s001_028 with Dissolve(0.25)
    "我能闻到皮肤烧焦的味道。要吐了。"
    k "送他去淋浴间。"
    l "对。对。好主意。你撑得住吗？"
    scene c005_s001_030 with Dissolve(0.25)
    j "{size=32}需要你帮忙。我几乎什么都看不见。{/size}"
    l "卡莉？"
    k "我留在这儿。以防万一。"
    scene c005_s001_031 with Dissolve(0.25)
    "{color=ffcccc}真需要有人放哨吗？倒不如说我该收拾好东西，然后弄清楚到底发生了什么。{/color}"
    scene blank with Dissolve(1)
    scene c005_s001_032 with Dissolve(1)
    "操。我看不见了。而且呼吸起来疼得要命。他妈的皮肤像烧着一样。"
    j "*咳嗽* *咳嗽*" with vpunch
    scene c005_s001_033 with Dissolve(0.5)
    l "我扶着你。我来带路。*咳嗽*"
    "要不是我光顾着沉浸在自己的疼痛里，我大概会担心劳拉从我身上吸进去多少雾。"
    scene blank with Dissolve(2)
    scene c005_s001_037 with Dissolve(2)
    l "一步一步 *咳嗽* 来。"
    j "{size=32}抱歉，刚才我在里面搞砸了。应该先穿好装备再进去的。{/size}"
    scene c005_s001_038 with Dissolve(0.5)
    l "没关系，这不是你的错，要说谁的错也是我的。可我们怎么可能知道那是一只那种生物？我以为是个受重伤的人。一个把自己锁在充满那种雾的房间里的人。"
    scene blank with Dissolve(2)
    scene c005_s002_001 with Dissolve(2)
    "天哪，我们走到淋浴间花的时间感觉漫长得要命。劳拉这事上对我特别有耐心，我得记她一份好。我只希望她之前那样的时候，我对她的表现能有她一半好。"
    scene c005_s002_002 with Dissolve(0.5)
    l "来，我们到更衣室了。我带你去淋浴间。慢慢来，别急。"
    scene c005_s002_003 with Dissolve(1)
    l "好了，到了。终于到了。来，停这儿。"
    scene c005_s002_004 with Dissolve(0.25)
    l "你现在怎么样？我知道你很不好，但是——"
    j "*咳嗽* {size=32}很难{/size} *咳嗽* {size=32}看清{/size} *咳嗽* {size=32}喘气……{/size}"
    scene c005_s002_005 with Dissolve(0.25)
    l "好好好，到了。我把水放上。"
    play ambient shower
    scene c005_s002_006 with Dissolve(0.25)
    "我先把衣服脱了。不知道现在还有没有救。"
    scene c005_s002_007 with Dissolve(0.25)
    l "好，等一下就有热水了。嘿，嘿，我来帮你。"
    j "{size=32}我能自己{/size} *咳嗽*"
    scene c005_s002_008 with Dissolve(0.25)
    j "{size=32}我不想让你吸入比现在更多的{/size}*咳嗽* {size=32}这东西。{/size}"
    l "我没那么娇弱。"
    "我能听见她在憋着不咳。"
    scene c005_s002_009 with Dissolve(0.25)
    if l_sex >= 1:
        l "再说了，我已经看过你光着身子了，[player_name]。"
    else:
        l "我以前见过鸡巴，[player_name]。而且我觉得，我们已经到了该把绅士风度往后放一放的地步。"
    scene c005_s002_010 with Dissolve(0.5)
    $ l_desire +=1
    "脱完衣服，劳拉把我往正确的方向推了推。"
    scene c005_s002_011 with Dissolve(1)
    "站到淋浴下面之后，我在那儿待了一会儿，就让水冲在脸上和肩膀上。一开始是刺痛的，但几秒钟过去之后，痛感开始缓解。"
    scene c005_s002_012 with Dissolve(0.5)
    l "哦，你的衣服*咳嗽*完了，[player_name]。这上面有些烧痕。像是布料在融化。"
    j "扔了吧。"
    scene c005_s002_013 with Dissolve(0.25)
    l "我早就想到了。我去给你拿件衣服穿。马上回来。"
    j "还有看看卡莉 *咳嗽*。" with vpunch
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c005_s002_014 with Dissolve(2)
    play music insideday fadein 2.0
    "我在那儿站了一会儿，就让热水尽它所能地帮我。偶尔我会抹上皂，小心地把脸上和手臂上最严重的刺激物洗掉。那次袭击把我的皮肤弄得血肉模糊，我得费很大劲才不让自己把情况弄得更糟。"
    "我可能叫出来了一次。"
    if ch3_laura_sex == "yes" or ch4_laura_sex == "yes":
        scene c005_s002_015 with Dissolve(0.5)
        l "我回来了。我拿了你的工作服，不过也就这些了。再加上我们找到的那件背心。你还好吗？[player_name]？"
        j "死不了。我现在对{a=https://www.youtube.com/watch?v=zvtUrjfnSnA}《搏击俱乐部》{/a}里那场化学灼伤戏是什么感觉，有了更清楚的认识。"
        l "你的视力怎么样？"
        j "模糊，但好多了。我想再在淋浴下待一会儿，让水多冲一会儿。"
        scene c005_s002_016 with Dissolve(0.25)
        l "你咳嗽好多了。"
        j "那你呢？"
        l "等你那身东西被我扔掉之后就好了。烧伤有多严重？看你衣服那样，我有点担心。"
        scene c005_s002_017 with Dissolve(0.5)
        j "没镜子可照。有些地方我的皮肤火辣辣的。"
        menu:
            "让我出来吧。":
                "我大概在里面待够久了。再待下去我干脆就在这儿自己玩自己了。"
                stop ambient
                scene c005_s002_071 with Dissolve(0.5)
                j "让我出来，你可以好好给我检查一遍。"
                l "好，我这儿有条浴巾。"
                scene c005_s002_072 with Dissolve(0.25)
                j "那你先把眼睛转开一秒。"
                l "[player_name]，我以前见过你的鸡巴。"
                scene c005_s002_073 with Dissolve(1)
                j "所以，我们已经到了可以随便光着膀子的阶段？"
                l "这不叫随便。你受伤了，我得确认有没有留下什么持久或不可逆的伤害。"
                j "是哦~~~~你可以直接承认你想看我光着身子。"
                scene c005_s002_074 with Dissolve(0.25)
                l "好吧，看着还行。这儿那儿有几处发红，不过我觉得我们把你救得还算及时。"
                j "那我可以穿衣服了。除非你还想多享受一会儿。"
                scene c005_s002_075 with Dissolve(0.25)
                l "哈哈哈。我把你的衣服放在那边了。我得回去看看卡莉有没有事。我瞄见她穿上外套了，但没来得及问她。"
                j "你觉得她要去那边看看吗？"
                scene c005_s002_076 with Dissolve(0.25)
                l "我觉得是。"
                j "*叹气* 好吧，我穿衣服，一会儿就上去。"
                l "别赶着。我们能处理。而且说不定你今天的活儿已经干完了。"
                scene c005_s002_077 with Dissolve(0.25)
                j "等我上去想劝我别出去，那你可有得费劲了。"
                l "死脑筋的混蛋。*咯咯笑*"
            "再给我一会儿。\n[rgr](劳拉 爱意 +1)\n[rrd](劳拉 欲望 -1)\n[pks]":
                $ l_sex += 1
                $ l_love += 1
                $ ch5_laura_sex = "yes"
                $ l_desire -= 1
                call ch5_laura_sex from _call_ch5_laura_sex
    else:
        stop ambient fadeout 2.0
        scene blank with Dissolve(2)
        scene c005_s002_078 with Dissolve(2)
        "过了一阵，我觉得自己已经尽力了。当然，皮肤还是火辣辣的，但比之前好太多了。我抓了条浴巾围在腰上，正好在劳拉回来的时候走了出来。"
        scene c005_s002_079 with Dissolve(0.5)
        l "我回来了。我拿了你的工作服，不过也就这些了。再加上我们找到的那件背心。所幸你是男的，两身换洗衣服好像就够了。你还好吗？"
        j "死不了。我现在对{a=https://www.youtube.com/watch?v=zvtUrjfnSnA}《搏击俱乐部》{/a}里那场化学灼伤戏是什么感觉，有了更清楚的认识。"
        scene c005_s002_080 with Dissolve(0.5)
        l "你的视力怎么样？"
        j "模糊，但好多了。我想再在淋浴下待一会儿，让水多冲一会儿，可我实在快泡皱了。"
        scene c005_s002_081 with Dissolve(0.25)
        l "你咳嗽好多了。"
        j "那你呢？"
        scene c005_s002_082 with Dissolve(0.25)
        l "等你那身东西被我扔掉之后就好了。烧伤有多严重？看你衣服那样，我有点担心。"
        j "没镜子可照。有些地方我的皮肤火辣辣的。"
        scene c005_s002_083 with Dissolve(0.25)
        l "好吧，看着还行。这儿那儿有几处发红，不过我觉得我们把你救得还算及时。"
        j "那我可以穿衣服了。除非你还想多享受一会儿。"
        scene c005_s002_084 with Dissolve(0.25)
        l "哈哈哈。我把你的衣服放在那边了。我得回去看看卡莉有没有事。我瞄见她穿上外套了，但没来得及问她。"
        scene c005_s002_085 with Dissolve(0.25)
        j "她在想着要去那间办公室看看吗？"
        l "我觉得是。"
        scene c005_s002_086 with Dissolve(0.25)
        j "*叹气* 好吧，我穿衣服，一会儿就上去。"
        l "别赶着。我们能处理。而且说不定你今天的活儿已经干完了。"
        scene c005_s002_087 with Dissolve(0.25)
        j "等我上去想劝我别出去，那你可有得费劲了。"
        l "死脑筋的混蛋。*咯咯笑*"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c005_s003_001 with Dissolve(2)
    play music insideday2 fadein 2.0
    "{color=#ffcccc}该穿上我的大姑娘裤子了。我任由恐惧占了上风太久了。而且[player_name]受伤了，所以我必须去做这件事。我不想他和劳拉没必要的话再回到这儿来。{/color}"
    scene c005_s003_002 with Dissolve(0.5)
    "{color=#ffcccc}[player_name]说他把那只东西从开着的窗户打落了。我不明白那扇窗{b}为什么{/b}会开着。不过他说窗是碎的。{/color}"
    scene c005_s003_003 with Dissolve(0.25)
    "{color=#ffcccc}好吧，有人……看起来是真的很想把整扇窗都砸掉。为什么？是想喊救命？那说不通。他们要是想出去，直接下楼就行了。{/color}"
    "{color=#ffcccc}也许是因为在这么高的楼层，他们以为自己能朝救援直升机挥手。要是真有的话。我到现在还什么都没看见。{/color}"
    scene c005_s003_004 with Dissolve(0.25)
    "{color=#ffcccc}地上有玻璃。不多，但有一些。肯定有人从里面往外扔了什么东西。比如一台电脑显示器。{/color}"
    scene c005_s003_005 with Dissolve(0.25)
    "{color=#ffcccc}这儿有些衣服，看起来烧焦了也撕裂了。这以前是人吗？我知道我们之前谈过，它们有可能只是个吸了太多雾的普通人。这算是印证了。还是不算？{/color}"
    "{color=#ffcccc}不过，那到底是谁？{/color}"
    scene c005_s003_006 with Dissolve(0.5)
    "{color=#ffcccc}这是不是他的办公室？他们是被困在这儿了，还是躲进来的？我感觉有好多问题我都不会有答案，所以我能做的也就是在脑子里按合理的假设编故事。{/color}"
    "{color=#ffcccc}至少让我看看能不能找到点关于这人是谁的线索。{/color}"
    scene blank with Dissolve(1)
    scene c005_s003_007 with Dissolve(1)
    k "*呻吟* 什么都没有。"
    "{color=#ffcccc}我再去翻翻那些衣服。也许口袋里有什么东西。钱包之类的。{/color}"
    scene c005_s003_008 with Dissolve(0.5)
    "{color=#ffcccc}呃，这玩意儿真恶心。布料上有一些……黏糊糊的东西。像是他们的皮肉掉了……{/color}"
    scene c005_s003_009 with Dissolve(0.25)
    k "*干呕* *作呕*"
    "{color=#ffcccc}硬着头皮上，卡莉。没那么糟……{/color}"
    scene c005_s003_010 with Dissolve(0.25)
    k "哦，靠！找到了！"
    "{color=#ffcccc}钥匙。车钥匙！我天。而且是福特的车。那辆 Bronco！哦天哪，我们不可能这么走运。{/color}"
    scene c005_s003_011 with Dissolve(0.5)
    l "{size=32}卡莉？卡莉！你在哪儿？{/size}"
    k "等一下。"
    scene blank with Dissolve(2)
    scene c005_s003_012 with Dissolve(2)
    k "劳拉？哦，你们俩在这儿。嘿，我刚在那间办公室里。等一下，我过去找你们。抱歉，这边还一团糟。"
    scene c005_s003_013 with Dissolve(0.25)
    j "靠，我大概该把门堵上。或者窗。两个都堵。天哪，直接把那扇窗砸下来真蠢透了。"
    l "我们在里面听到声音。以为里面的人有麻烦。当时那是有计算的冒险。也许我当初该更坚决地反对进去，可事已至此。"
    scene c005_s003_014 with Dissolve(0.5)
    k "你还好吗？你刚才看起来……不太妙。"
    j "死不了。最严重的已经冲掉了。那件衬衫报废了。至少劳拉是这么说的。也可能她只是想让我把它扔掉、换件好看的。"
    scene c005_s003_018 with Dissolve(0.25)
    l "[player_name]……"
    scene c005_s003_015 with Dissolve(0.25)
    l "卡莉，你在里面找到什么了吗？"
    k "窗户被人砸开了。地上有些玻璃碎片。我不知道他们用什么砸的。电脑显示器？我没看见。"
    j "要是在街上找到一台，我们就知道答案了。还有我们那位朋友呢？"
    scene c005_s003_016 with Dissolve(0.25)
    k "没了。就像你说的，你肯定把它从窗户砸出去了。"
    l "你看到什么能解释它是怎么进去的、或者为什么进去的吗？"
    scene c005_s003_017 with Dissolve(0.25)
    k "只看到地上有些衣服。"
    j "唔……奇怪。这意味着……"
    scene c005_s003_018 with Dissolve(0.25)
    l "什么？意味着什么？"
    j "我一直在琢磨——可能之前也提过——餐馆外面那只怪物，是不是某个被雾暴露太久的人。或者被高浓度的雾直接命中。那只是我为了给自己解释这局面而喷出来的理论。"
    l "哦哦……呃……好吧。"
    "大概不该让她们想这件事想太久。尤其对劳拉来说，她在外面已经待得有点久了。"
    scene c005_s003_019 with Dissolve(0.5)
    k "哦，我本来该早点说的，不过我确实找到了一些钥匙。我想是那辆 SUV 的。在其中一个口袋里。我本来想等你回来之前再找找有没有什么证件。"
    j "太棒了。好发现，姑娘。至少这一趟还是有点好结果。"
    scene c005_s003_020 with Dissolve(0.25)
    l "我们该试试它们能不能用。别太早高兴。"
    j "我可以去看看。"
    scene c005_s003_021 with Dissolve(0.25)
    l "[player_name]。不行。你得待在这儿。你的视力和呼吸都还没恢复。你真觉得去那个漆黑的地下室是个好主意？"
    j "劳拉，只能二选一。我要么去检查那辆车，要么在办公室里再翻翻。至少我得试着把窗封上。"
    scene c005_s003_022 with Dissolve(0.25)
    l "*叹气* 天哪，你有时候真是倔。你才刚受过伤。"
    j "我现在已经好多了。"
    scene c005_s003_023 with Dissolve(0.25)
    l "不过也没好到百分之百。这样吧，我和卡莉下去看看那辆 SUV？我们带上手电筒和斧子。你留在这儿。聪明点。"
    j "听起来不错。再说你说得对，我也不知道自己的视力在车库那种黑暗里撑不撑得住。"
    scene c005_s003_024 with Dissolve(0.25)
    l "只是别在办公室里待太久。*叹气* 等等……你到底打算怎么把窗封上？"
    j "不知道。我在二楼杂物间看到一些垃圾袋和封装胶带。最坏的情况，我可以用那些把它糊上。然后尽量把门关严。"
    scene c005_s003_025 with Dissolve(0.25)
    l "好吧，别在里面待太久。还有要戴——"
    j "我知道，我知道。口罩。护目镜。之类的。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_27_142", transition=Dissolve(1.0))()
    pause
    $ Hide("june_27_142", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music outsideday fadein 2.0
    scene c005_s004_001 with Dissolve(2)
    k "他会没事吗？"
    l "要是他悠着点的话？没事。他脸上和皮肤有些烧伤。没有什么是不会愈合的。把他眼睛和脸上最严重的部分冲掉帮了大忙。"
    scene c005_s004_002 with Dissolve(0.25)
    k "……"
    l "顺便说一句，钥匙找得好，我们几乎把整栋楼都翻遍了都没找到。"
    scene c005_s004_003 with Dissolve(0.25)
    k "谢谢。我突然想到一件事：我们确定电池还有电吗？"
    l "我上次看的时候防盗灯还在闪。所以，就算它停了一阵子，我敢肯定也还能打着。可能要挣扎一两秒，但电应该够。不过，真要是发动了，我们得让车先怠速一会儿。"
    scene c005_s004_004 with Dissolve(0.25)
    "{color=#66ff33}{i}如果{/i}这就是对的钥匙的话。我把太多希望押在这上面了。{/color}"
    scene blank with Dissolve(2)
    scene c005_s004_005 with Dissolve(2)
    l "在那边。"
    k "哦？不错。"
    scene c005_s004_006 with Dissolve(0.25)
    l "不错归不错，我希望它能开。我试试解锁……"
    scene c005_s004_007 with flash
    "*哔* *哔*！"
    k "这是个好兆头。"
    l "是啊。"
    "{color=#66ff33}这下我放心了。难道终于有一件事顺着我们了？不过还是先把它打着，我再高兴。{/color}"
    scene blank with Dissolve(1)
    scene c005_s004_008 with Dissolve(1)
    l "好了，见证奇迹的时刻。"
    k "祝好运。"
    scene c005_s004_009 with Dissolve(0.25)
    "*咕噜噜噜噜嗯嗯*！" with vpunch
    l "*叹气* 哦他妈太好了。而且声音很健康。健康又结实。汽车要是能算健康的话。"
    k "我知道我的车打不着火的时候是什么声音。可当时我不知道那是因为雾。不过这声音听着不错。"
    scene c005_s004_010 with Dissolve(0.25)
    k "嘿，我看看收音机。"
    l "我们在地下。我估计收不到什么，不过试试吧。"
    scene c005_s004_011 with Dissolve(0.25)
    "收音机" "*crrrrsshhhhhhhh*"
    k "唔嗯~~~ 雪花噪。靠。*叹气*"
    l "等我们出去可以再试试。也许到了街上就能收到了。"
    k "也是。"
    scene blank with Dissolve(2)
    scene c005_s003_026 with Dissolve(2)
    "好吧，也只能这样了。不算完全密封，但眼下够了。而且要是那钥匙真管用，我们也不会在这儿待到需要在意这个。"
    "不过干完这些活儿，我出了身汗，头也有点不舒服。我想我还是没从被喷了那一下的影响里缓过来。"
    scene c005_s003_027 with Dissolve(0.5)
    "好了，赶紧把事儿办完。看看我能不能找到点证件。这哥们儿肯定有个钱包。"
    "呃，这玩意儿真恶心。摸上去还是湿的。"
    scene c005_s003_028 with Dissolve(0.25)
    "来了。一个钱包。你是谁？"
    scene c005_s003_029 with Dissolve(0.25)
    "克里夫·约翰逊。住在特伯里。通勤距离不短。而且那是镇上比较高档的地段。他大概是管理层。除了这个就只剩几张信用卡了。自从大家的照片都放到……说到曹操说到曹操……"
    scene c005_s003_030 with Dissolve(0.25)
    "手机。找到了。它……"
    scene c005_s003_031 with Dissolve(0.25)
    "他妈的开不了机。就算他设了密码我也打不开，不过无所谓了。"
    "好吧，趁我还有力气，我们出去把这儿封上。"
    scene blank with Dissolve(2)
    scene c005_s004_012 with Dissolve(2)
    $ k_anxiety -= 1
    $ l_anxiety -= 1
    l "哦天，我要是能一直这样就好了。空调和人体工学座椅？这是我几周以来最舒服的时刻。我们干脆今晚就住这儿吧。"
    k "要是我睡着了，就让我睡个十五分钟左右，好吗？*咯咯笑*"
    scene c005_s004_013 with Dissolve(0.25)
    "{color=#66ff33}这确实是我第一次感觉像回到了正常生活。我得盼着能从这儿开到医院。我们该坐下来把路线规划好。让在路上的时间尽可能短。{/color}"
    "{color=#66ff33}也许明天过完，我们就回到家人身边——或者回到旧生活的某种近似版本。希望吧。如果这一切真的顺利。当然，这也意味着我终于得跟基思做那场早就该做的谈话了。我们是该试着挽救婚姻？还是趁彼得已经不在家就此了断？{/color}"
    "{color=#66ff33}他到底和多少个女人上过床？我越回想我们的过去，就越开始琢磨他不在家的那些时候都跟谁在一起。{/color}"
    scene c005_s004_014 with Dissolve(0.25)
    if l_sex >= 2:
        "{color=#66ff33}跟[player_name]搞在一起，是不是意味着我已经接受了跟基思这段婚姻早就结束了？还是说，只是我自己也想轮到我一次？我……我喜欢[player_name]，但我不觉得继续下去是个好主意。至少等我们出去之后不行。{/color}"
    k "劳拉？你还好吗？你看起来像是有什么难过的事。"
    scene c005_s004_015 with Dissolve(0.25)
    l "哦，呃……"
    "{color=#66ff33}我该告诉她。我告诉了[player_name]。如果我想让她开口说出我和安德鲁之间可能存在的问题，我也该对她坦诚。{/color}"
    scene c005_s004_016 with Dissolve(0.25)
    l "我刚才只是在想，等我们出去以后会怎么样。得看情况有多糟，我们当中有些人可能得另找地方住。"
    k "*叹气* 我觉得他们不会让我回我们的公寓。反正你住在镇外。"
    scene c005_s004_017 with Dissolve(0.25)
    l "你看，问题就在这儿……我已经告诉[player_name]了，也该告诉你。我很确定我的婚姻正走向离婚。基思和我早就算不上夫妻了，而且我百分之百确定他跟某个同事睡在一起。可能还不止一个。"
    scene c005_s004_018 with Dissolve(0.25)
    k "哦，呃……对不起，劳拉。我……我不知道。"
    l "没人知道。或者，以前没人知道。到目前为止我只跟你和[player_name]说过。"
    k "那彼得呢？"
    scene c005_s004_019 with Dissolve(0.25)
    l "我觉得我们一直瞒着——在公开场合装作一切正常——直到他去上大学。可现在呢？基思连待在家里的时间都很少。也不遮掩自己在外面忙自己的事。下次他回家我得告诉他。如果他不是已经在那儿等着看他妈还活着没有的话。"
    k "我……我不知道该说什么。对不起。如、如果我能做什么，我一定做。"
    scene c005_s004_020 with Dissolve(0.25)
    l "我心领了。我只是觉得，既然我们都在这个地方，人人都得互相信任、互相依靠，而把那些影响我的事——那些我带进这场困境里的事——坦白出来，对大家是最好的。"
    k "我……我明白。"
    scene c005_s004_021 with Dissolve(0.25)
    "{color=#66ff33}我能看见她脑子在转，但也许现在不是逼她的时机。也许她压根不觉得有什么可担心的。也许是我太敏感了。{/color}"
    scene c005_s004_022 with Dissolve(0.25)
    l "好吧，我们已经开得够久了。没必要把油全烧掉。"
    k "看来我们得回去了。你觉得我们什么时候出发？"
    scene c005_s004_023 with Dissolve(0.25)
    l "我们跟[player_name]商量一下吧。越早越好。也许花一天左右搜集我们能搜集的物资，然后就出发。甚至可能明天就走，因为我觉得再等下去对我们不利。"
    k "对……"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_27_304", transition=Dissolve(1.0))()
    pause
    $ Hide("june_27_304", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday fadein 2.0
    scene c005_s004_024 with Dissolve(2)
    "把那扇办公室的门封好——又用胶带把原来门把手的位置贴上垃圾袋——之后，我觉得是时候休息一下了。之前那次袭击让我气喘吁吁，浑身难受。"
    scene c005_s004_025 with Dissolve(0.25)
    "姑娘们还没回来，我就在电梯旁边等她们。有那么几个瞬间，侵入式的念头让我担心她们的安危。但我说服自己不要采取任何行动。我必须相信她们没事。她们俩都挺聪明，大概也更有自我保护的本能。"
    scene c005_s004_026 with Dissolve(0.25)
    "可我还是足够在乎，焦虑还是悄悄爬了上来。这些人是朋友、是同事，如今已经变成了更近的关系。如果我们能活着出去，我们会一辈子连在一起。"
    if k_friend >= 8:
        "至于我和卡莉？我们从来没这么亲近过。当然，我也没指望自己会了解她的全部私生活，可我觉得我们之间建立了一种以前绝不可能有的联结。"
    if ch5_laura_sex == "yes":
        "而劳拉？我完全不知道我们之间在发生什么，也不知道这会走向哪里。也许等我们出去之后，这会变成一件我们再也不提的事。或者，它会成为某种更进一步的开始。"
    elif l_sex == 1:
        "至于劳拉？虽然我们上过了床，但那成了一个永远不该再提的话题，反而成了这一堆烂事里一段少有的美好回忆。这是一个我们必须守住的秘密。"
    scene c005_s004_027 with Dissolve(0.5)
    l "[player_name]？[player_name]！？"
    scene c005_s004_028 with Dissolve(0.25)
    l "哦，你在这儿啊。"
    j "嘿，你回来了。有好消息吧？"
    scene c005_s004_029 with Dissolve(0.5)
    l "我们有一辆能开的 SUV。油基本是满的。启动起来一点问题都没有。"
    k "它有空调。没有收音机，但有甜美甜美的空调。"
    scene c005_s004_030 with Dissolve(0.25)
    l "对，我们大概爽了一阵。你呢？你有没有……"
    j "没事。气喘得像抽了四十年烟的老头子。不过我把窗封好了，门也关上了大体遮住了。不是密封的，但我们不该再吸入太多雾了。"
    scene c005_s004_031 with Dissolve(0.25)
    j "我确实找到了那人的钱包和手机，但没什么能说明他是谁、或者他为什么会在这儿的东西。"
    k "也没说明他为什么要把窗砸开？"
    scene c005_s004_032 with Dissolve(0.25)
    j "人是挺疯的，压力之下会干些没道理的事。除此之外我就没什么了。"
    l "好了，我要下车了。去趟洗手间。我们出去的计划待会儿再谈。"
    scene c005_s004_033 with Dissolve(0.5)
    j "当然，我在这儿。"
    if k_friend >= 8:
        scene c005_s004_034 with Dissolve(0.25)
        k "你还好吗？真的还好吗？我……我刚才很担心你。"
        menu:
            "哦，我没事。别担心。\n[rrd](卡莉 信任 -1)":
                $ k_trust -= 1
                scene c005_s004_035 with Dissolve(0.5)
                j "哦，我没事。别担心。我只是太激动了。"
                scene c005_s004_036 with Dissolve(0.25)
                k "你说是就是吧。"
                "她好像并不太喜欢被这么敷衍过去。就算她的反应很微妙，我也开始能看出卡莉什么时候是真的不在意了。"
            "运气好才没更糟。\n[rgr](卡莉 信任 +1)":
                $ k_trust += 1
                scene c005_s004_035 with Dissolve(0.5)
                j "对，运气好才没更糟。我没看见，直到已经太晚，但把我弄到淋浴间冲掉确实有用。要不是我们动作快把我弄干净了，那伤害可真不好说。"
                scene c005_s004_037 with Dissolve(0.25)
                k "不过你脸颊上还是有一些烧伤。"
                j "有点刺痛。不过幸好我皮肤黑，看起来没那么严重。"
                scene c005_s004_038 with Dissolve(0.25)
                k "说得通。我……"
                j "去吧，去吧。我们待会儿再聊。我感觉我们有一场旅行计划的谈话要谈。"
                scene c005_s004_039 with Dissolve(0.25)
                k "对……"
    scene blank with Dissolve(2)
    scene c005_s014_001 with Dissolve(2)
    l "*叹气*"
    "{color=#66ff33}这辆 SUV 是我很久以来见到的第一个好消息。感觉几乎像好事了。可我们最近运气实在太背，我都不敢相信这事真会成。我只是怕明天下去打火的时候，这该死的东西发动不了。{/color}"
    scene c005_s014_002 with Dissolve(0.25)
    "{color=#66ff33}我……不该逼着[player_name]直接硬砸进去，可当时感觉时间很重要。确实重要。它{b}现在{/b}也依然重要。可我对自己在他受伤这件事里扮演的角色愧疚得要命。我当时太急了。一直都很急。{/color}"
    scene c005_s014_003 with Dissolve(0.25)
    "{color=#66ff33}可是……我们也不能慢悠悠地走去医院。他们不会永远撤离人员。到某个时候，他们会放弃，直接认定这里的人都死了。{/color}"
    "{color=#66ff33}「这里」？那到底是什么意思？我们还不知道范围有多大。我……我该停止胡思乱想了。这对谁都没好处。对缓解我的神经更没用。{/color}"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_27_719", transition=Dissolve(1.0))()
    pause
    $ Hide("june_27_719", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain fadein 2.0
    scene c005_s005_001 with Dissolve(2)
    "等我们重新聚在一起的时候已经是晚上了。想到我们居然在用会议室干它本来的用途，我私下里小小地笑了一下——虽然「讨论撤离这栋楼」这种事，普罗维登斯人寿里没有任何人预料得到。"
    "环顾四周，我能看出大家虽然因为 SUV 这件事走运而松了口气，却都被一直高度戒备的轮番折磨弄得疲惫不堪。"
    "一大早就在办公室里发现那只怪物，把所有人的神经都绷到了极限。就算我们尽了最大努力，这地方也不比别处更安全。"
    scene c005_s005_002 with Dissolve(0.25)
    l "我就直接问出来，把这个问题摆到台面上：你们觉得我们该多快出发？"
    k "明天。为什么要等？我们手上的食物撑不了多久，我也不想再回那家餐馆。尤其现在那儿还留着尸体、又有一堆怪物晃悠，而且我们已经确定不止一只。"
    scene c005_s005_003 with Dissolve(0.25)
    l "好。[player_name]？"
    "那就直说吧。大家都有一天时间考虑这件事的想法。我有种感觉，我可能是这里唯一的一个异类。卡莉和劳拉都有想回去的生活，而且都急着回去。"
    "我？我想准备得更充分一点。或者，也许我只是害怕我们出去之后到不了医院，被困在什么地方。"
    menu:
        "我想多弄点物资。\n[rrd](卡莉\劳拉 好感 -1)":
            $ l_friend -= 1
            $ k_friend -= 1
            scene c005_s005_004 with Dissolve(0.5)
            j "老实说，我想多弄点物资。水。食物。什么都行。以防万一路上出什么事，得在到之前先停一下。"
            k "我……我不想再回汉堡店了。"
            scene c005_s005_005 with Dissolve(0.25)
            l "我同意卡莉。我不想再在这儿待下去了。这不是五星级度假村，而那辆 SUV 今天就能开。我不想冒险出什么事，比如雾渗进车库。最近的意外已经够多了。"
            scene c005_s005_006 with Dissolve(0.25)
            l "另外，我觉得时间确实挺重要。我们一直没在天空看到直升机。我知道那地方有好几英里远，我们这边的视野也不好，可我担心外界的救援行动会有停下来的那一天。"
            j "好吧，我不再逼了。如果你们俩觉得明天走最好，那就这么办。不过我们今晚和明天早上应该把这栋楼再走一遍，看看走之前能拿走些什么。"
        "[gr]越早越好。":
            scene c005_s005_005 with Dissolve(0.5)
            j "越早越好。我承认，虽然我想补充水、食物和其他物资，但也许我们确实不该再磨蹭了。我们招来的麻烦已经够多了。"
            l "我同意。我不想再待在这儿了。这不是五星级度假村，而那辆 SUV 今天就能开。我不想冒险出什么事，比如雾渗进车库。最近的意外已经够多了。"
            scene c005_s005_006 with Dissolve(0.25)
            l "另外，我觉得时间确实挺重要。我们一直没在天空看到直升机。我知道那地方有好几英里远，我们这边的视野也不好，可我担心外界的救援行动会有停下来的那一天。"
            j "对，这话没错。不过我们该利用今晚和明天早上的时间把这栋楼走一遍，看看走之前能拿走些什么。"
    scene c005_s005_007 with Dissolve(0.25)
    k "如果还剩下什么的话。"
    scene c005_s005_008 with Dissolve(0.5)
    "就这样定下之后，我们的小会开完了。卡莉看起来已经准备睡了，却主动提出去看看休息室里还剩些什么。"
    if l_sex >= 1:
        scene c005_s005_009 with Dissolve(0.25)
        l "嘿，我……"
        j "对，怎么了？你没事吧？"
        scene c005_s005_010 with Dissolve(0.5)
        l "对，我想应该没事。我只是想谢谢你为……为我们之间那些事。"
        j "那不用谢我。我也挺享受的。"
        scene c005_s005_011 with Dissolve(0.25)
        l "有那么一小会儿，它让我感受到了恐惧和不安之外的东西。"
        j "我能为你做的，尽管说。*轻笑*"
        if ch5_laura_sex == "yes":
            scene c005_s005_013 with Dissolve(0.25)
            l "等我们出去之后我什么都不能保证……"
            j "我没要你保证。我知道你有些事得自己想清楚。有些决定得做。"
            scene c005_s005_014 with Dissolve(0.25)
            l "谢谢。我不会忘的。"
            j "我知道我不会。"
            scene c005_s005_015 with Dissolve(0.25)
            l "打住。我在这儿正努力甜一点呢。"
            j "我也是。"
        else:
            scene c005_s005_012 with Dissolve(0.25)
            l "我很领情。"
        scene c005_s005_016 with Dissolve(0.5)
        "我们往外走的时候，劳拉和我决定最后再把办公室走一遍，希望能找到点有用的东西。"
    else:
        scene c005_s005_016 with Dissolve(0.5)
        "劳拉和我决定最后再把办公室走一遍，希望能找到点有用的东西。"
    scene blank with Dissolve(2)
    scene c005_s005_017 with Dissolve(2)
    "一个小时后，劳拉和我分头行动。我回到保安室，只是想看看有没有漏掉什么。我们刚到这儿的时候，我压根没想过要旅行，一心只想着找钥匙。劳拉提议把健身中心再搜一遍，以防有人把饮料藏在经理办公室里。"
    "虽然我们没真正把 SUV 装满就离开让我有点不痛快，但劳拉关于时间宝贵的说法是有道理的。我心里有一部分在想，劳拉这种急切是不是在左右她的判断。也许接下来我得当那个主张稳重的声音。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_28_734", transition=Dissolve(1.0))()
    pause
    $ Hide("june_28_734", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music kallietheme fadein 2.0
    scene c005_s006_001 with Dissolve(2)
    "好了，出发前最后再冲一次澡。谁也不知道我们会落到哪儿。劳拉一门心思认定我们明天就能到医院。但我宁愿谨慎，也不想只靠乐观。"
    "所以，我得把自己收拾得干干净净。在办公室那段时间让我明白，好几天不洗澡简直是他妈的地狱。天哪，在这一切发生之前，我一定是被惯坏得厉害——随时都有自来水，每天三顿饭，还有一张床。"
    "说到这个……靠，我们出去之后我到底要住哪儿？搬去跟我爸妈住？呃。"
    scene c005_s006_002 with Dissolve(0.25)
    "唔，我的胡子开始长得不像话了。要是有剃刀或者修眉机，我就弄一下。也许是时候别看着这么邋遢了。"
    scene c005_s006_003 with Dissolve(0.25)
    "想这么做的恐怕不止我一个人。等我们获救之后，劳拉和卡莉的未来里大概会有一个「水疗日」。"
    "就我来说？我愿意用命换几杯啤酒，再换一次真正躺在床上睡个长周末。"
    scene c005_s006_004 with Dissolve(0.5)
    "哦？门开了？有人在这儿。我还以为早来一会儿就能独占这地方。看来不止我一个人起得早。"
    scene c005_s006_005 with Dissolve(0.25)
    k "*哼着歌*"
    "是卡莉。而且我觉得她没发现我在这儿。我该……"
    menu:
        "说「早上好」。\n[rgr](卡莉 欲望 +1)":
            if k_trust >=5:
                $ k_desire += 1
            else:
                $ k_friend -= 1
            scene c005_s006_009 with Dissolve(0.5)
            j "早上好，卡莉。"
            k "啊呜~~~"
            scene c005_s006_010 with Dissolve(0.25)
            k "哦，你在这儿。我、我没看见你。早上好。"
            j "正准备出发前冲一下。看来你想的跟我一样。"
            scene c005_s006_011 with Dissolve(0.25)
            k "对……我……"
            j "我去，就不打扰你了。"
            scene c005_s006_012 with Dissolve(0.25)
            k "谢、谢谢。对了，我煮了咖啡。你要来点吗。"
            j "谢谢。走之前喝一杯正好。待会儿见。"
            k "当然。"
        "等一下。":
            "在这儿停一下，看看她会不会直接去淋浴间，那样我就能不被她发现地溜出去。"
            scene c005_s006_008 with Dissolve(0.25)
            "哦，她……对……"
            scene c005_s006_039 with Dissolve(0.25)
            "我现在就出去。动静轻点，因为我不想让她以为我是什么偷看她换衣服的变态色狼。"
            scene c005_s006_038 with Dissolve(0.25)
            k "刚才是有人……"
        "现在就溜。":
            scene c005_s006_006 with Dissolve(0.5)
            "让我拿上东西，现在就溜出去。她是下楼来找点独处的时间的，我能理解。我知道自己当初也是这么做的。"
            scene c005_s006_007 with Dissolve(0.25)
            "再说了，我一直很顺利地让她愿意对我敞开心扉，我可不想给她理由缩回去。不想把到目前为止的进展全都抹掉。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_18_1042", transition=Dissolve(1.0))()
    pause
    $ Hide("june_18_1042", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music outsideday2 fadein 2.0
    scene c005_s006_013 with Dissolve(2)
    "花了几小时把收集来的东西全塞进背包，我们带上装备往车库去。虽然没人说出口，空气里却弥漫着如释重负的感觉。劳拉和卡莉的脚步都比平时更有劲。"
    scene c005_s006_014 with Dissolve(0.5)
    l "好吧，在你跟我争之前，我先宣布：我来开。"
    j "我本来也没打算跟你争。合理。你成天在镇里开车。我们三个人里，大概你对路线和该走哪几条街最熟。要是要绕路，你也知道怎么走最好。"
    k "我坐后面。你腿长。"
    j "谢谢。背包放后面跟你一起。斧子我拿着。"
    scene blank with Dissolve(1)
    scene c005_s006_015 with Dissolve(1)
    j "你不是开玩笑吧。这车真舒服。虽然我们已经很久没有过这么像样的车了。"
    l "趁还能享受就享受一下空调吧，因为出发前我们得关掉、封好通风口。"
    j "我们可以设成内循环，但最好还是别冒险把那玩意儿吸进车里。"
    scene c005_s006_016 with Dissolve(0.25)
    j "那么，你打算往哪边走？"
    l "我想我们从图尔平街出来。我右转，横穿枫树街，然后左转上橡木路。那样会穿过校园，平时那地方堵得要命，但这是最快的路线。"
    scene c005_s006_017 with Dissolve(0.25)
    l "过了另一边之后呢？转到第四街，一直开到艾弗里街，我们应该能直接开进医疗中心的停车场。这是最快、最直接的路线。"
    j "也是路上时间最短的。"
    scene c005_s006_018 with Dissolve(0.25)
    l "正是。我们准备好了吗？"
    k "好了。"
    j "尽可能地准备好了。走吧。"
    scene blank with Dissolve(2)
    scene white with Dissolve(2)
    scene c005_s006_019 with Dissolve(2)
    "我们驶出车库，直接撞进一片浓得化不开的雾里，前方几英尺以外什么都看不清。"
    j "好吧，这……"
    l "我他妈什么都看不见。我们只能慢慢来。"
    scene c005_s006_020 with Dissolve(0.5)
    l "好消息是这些路我熟得不能再熟。不过……"
    j "留意路牌之类的东西？"
    l "正是。"
    scene blank with Dissolve(2)
    scene c005_s006_021 with Dissolve(2)
    "我们大概以每小时十英里的速度爬行，照这个速度得走上好几个小时。幸好 SUV 听起来还撑得住。可因为我不知道那团雾对我自己的车做了什么才让它趴窝，我不能想当然地以为它对这辆车也会照做。"
    scene c005_s006_022 with Dissolve(0.5)
    $ l_anxiety += 1
    $ k_anxiety += 1
    "没过多久，我们就在人行道上撞见了一个我们的「朋友」在游荡。"
    j "这些王八蛋到处都是。"
    scene c005_s006_023 with Dissolve(0.25)
    k "它、它在跟着我们吗？"
    l "很难说。我觉得它没想做什么。它就像嘉年华上喝醉的人一样到处乱晃。"
    j "别怕一点点小剐蹭，劳拉。"
    scene c005_s006_024 with Dissolve(0.5)
    k "照这速度，基本上就是剐一下就跑。"
    "{color=#ffcccc}我感觉我们要是一停下来，它马上就会扑上来。而且还不止那一只。外面到底还有多少只？{/color}"
    scene blank with Dissolve(2)
    scene c010_s004_070 with Dissolve(2)
    k "哦，嘿，我差点忘了。能试试收音机吗？我们在车库里试过，收不到信号。"
    j "对，当然，当然。不来点路上音乐怎么行。"
    scene c010_s004_071 with Dissolve(0.5)
    "收音机" "*crrrrsshhhhhhhh*"
    l "当然了。"
    k "还是雪花噪。*呻吟*"
    j "我把波段从头到尾转一遍，看是不是全都废了。"
    scene c010_s004_072 with Dissolve(0.5)
    "收音机" "*shhhhhhhh*"
    j "好吧。106.5 以前一直不错，信号总是很强。别的就没什么了。"
    l "大部分都是吵人的杂音。"
    scene c010_s004_073 with Dissolve(0.5)
    j "对，我们把音量调低点。万一有什么东西能透进来。"
    l "我会留心听着。"
    scene blank with Dissolve(2)
    scene c005_s006_025 with Dissolve(2)
    "我们在外面待了多久？大概也就几分钟吧，哪怕感觉更久。为了随时留意周围而绷着的那种压力，把这趟车程搞得比穿过镇中心的赏景之旅糟糕太多了。"
    "不过车呢？劳拉在一个路口停下来的时候，发动机差点熄火。谁都没说话，但我觉得我们都明白让轮子一直转下去对我们最有利。"
    scene c005_s006_026 with Dissolve(0.5)
    "不出所料，没过多久我们就遇到了不少被丢在路边的车。不管是雾刚来时被困住的人留下的，还是那些没能在变成不可能之前逃走的人。"
    "当然，这惹得劳拉路怒症大发。"
    scene c005_s006_027 with Dissolve(0.5)
    l "靠！至少有点本事，把车靠边停好再跑啊。"
    j "他们听不见你的，劳拉。"
    scene c005_s006_028 with Dissolve(0.25)
    l "就算我理解他们为什么丢下车就跑，我还是可以生气一下。"
    j "随你高兴吧。"
    scene blank with Dissolve(2)
    scene c005_s006_029 with Dissolve(2)
    l "靠。他们就在街上跌跌撞撞。"
    j "直接开过去。非得撞就蹭开一下。我想他们不会找你要保险，也不会报警。再说了，车是红色的。沾点血也没人会注意。"
    scene c005_s006_030 with Dissolve(0.5)
    l "我在努力。我真的在努力。{w=1}我是说，努力不去撞到他们。"
    "{color=#ffcccc}他们为什么就在街上乱撞？感觉他们压根不知道我们在这儿。{/color}"
    scene c005_s006_030-1 with Dissolve(0.25)
    "{color=#ffcccc}天哪。求你了……就当没看见吧。{/color}"
    scene blank with Dissolve(2)
    scene c005_s006_031 with Dissolve(2)
    "开过那条支路之后，我开始对我们的运气有点信心了。虽然我们才走了几英里、前面还有平时十五分钟的路程，可这条路似乎已经清空了。"
    scene c005_s006_032 with Dissolve(0.25)
    "再加上好几分钟都没见到一只烧焦的怪物，我让自己放松了那么一小会儿。当然，这意味着我们注定要失望。"
    scene c005_s006_033 with hpunch
    l "王八蛋！搞什么？！"
    j "靠。我……"
    "得赶紧想办法。这辆车开始发出像是被雾呛到的声音了。"
    scene c005_s006_034 with Dissolve(0.5)
    l "等等。我挂倒挡试试。看看能不能绕别的路。"
    k "你后面是干净的。我觉得是。很难说清。至少没有车。"
    scene blank with Dissolve(2)
    scene c005_s006_035 with Dissolve(2)
    "劳拉拼命把 SUV 掉了个头冲了出去，但我看得出发动机已经很吃力了。它撑不了多久。"
    scene c005_s006_036 with Dissolve(0.5)
    "我能听见劳拉在低声跟车说话，好像在求它再撑一会儿。如果我们运气好，也许还能再开几个街区……"
    scene c005_s006_037 with Dissolve(0.5)
    $ l_anxiety += 1
    l "靠！" with hpunch
    "或者，我们的运气可以直接拉裤子。"
    scene c005_s007_001 with Dissolve(1)
    l "*叹气* 靠，我本来指望我们能走远一点的。连三分之一都还没到。"
    j "好吧，我们现在在哪儿？"
    scene c005_s007_002 with Dissolve(0.25)
    k "那边是不是有一片联排住宅？或者公寓。我每天都走这条路，附近不远的地方他们正在盖新房子。我不是说我们要住下，但至少能有个地方重新整理一下。"
    l "眼下也只能这样了。留在那辆破车里肯定不行。"
    "眼下我们周围没人也没有东西。卡莉说得对。我们不能就这么坐在这儿闷闷不乐。"
    scene c005_s007_003 with Dissolve(0.25)
    j "好吧，我们准备徒步吧。不能在这儿待一整天。劳拉？"
    l "我知道。只是……失望。我以为我们能走得更远。"
    j "卡莉？你还好吗？"
    scene c005_s007_004 with Dissolve(0.5)
    k "对。背包我来背。"
    menu:
        "你确定？很重。\n[rrd](卡莉 好感 -1)":
            $ k_friend -= 1
            j "你确定？很重。"
            scene c005_s007_005 with Dissolve(0.25)
            k "我能背得动。别走太快就行。"
        "[gr]当然。":
            j "当然。"
            "我不会逼她。卡莉想派上用场。"
            scene c005_s007_005 with Dissolve(0.25)
            k "只是别走太快。"
    scene c005_s007_006 with Dissolve(0.5)
    l "我们一起行动。谁都不落下。"
    j "劳拉说得对。斧子在我手上。要是外面看见什么，准备好往反方向跑。我不想在没必要的情况下跟它们打起来。"
    stop music fadeout 2.0
    scene blank with Dissolve(1)
    scene c005_s007_007 with Dissolve(1)
    play music horror fadein 2.0
    "花了几分钟做准备——包括再确认一遍方向、以及万一遭遇敌对情况该怎么办——我们爬出了 SUV。虽然我很清楚不该开口问她要不要帮忙，但我看得出卡莉背着那个包很吃力。"
    scene c005_s007_008 with Dissolve(0.25)
    "我们尽可能快地前进。雾那么浓，能见度成了难题。要辨认附近的建筑得费一番力气。"
    scene c005_s007_009 with Dissolve(0.25)
    "当我注意到卡莉开始落后时，我放慢了速度。虽然车抛锚之后我还没再见到任何一只那些生物，但它们随时可能从雾里冒出来，我很清楚这一点。"
    scene c005_s007_010 with Dissolve(1)
    "我确实想到过，我们开车从几只身边经过，却什么事都没发生，就好像那辆车对它们毫无吸引力。你会以为发动机的声音该把它们的注意力吸引过去。这是不是说明它们是被别的什么吸引的？"
    scene c005_s007_011 with Dissolve(0.25)
    "它们聋吗？那倒能解释我们第一天在办公室砸窗户时，第一只为什么没靠过来。不过我大概不该现在任由这些胡思乱想分心。"
    scene blank with Dissolve(2)
    scene c005_s007_033 with Dissolve(2)
    j "令人震惊的是，它锁着。"
    l "{size=30}这边这栋有个钥匙盒。看起来是准备出售或者出租的。{/size}"
    scene c005_s007_034 with Dissolve(0.25)
    j "你说这些是新的，对吧？我看看窗户里面。"
    k "对。他们过去六个月一直在盖。我想五月就完工了。"
    scene c005_s007_035 with Dissolve(0.25)
    j "我的天。我一件家具都没看见。"
    l "*呻吟* 全是新的，而且本来是抱着能租出去的期望盖的。"
    scene c005_s007_036 with Dissolve(0.25)
    j "在这种经济情况下？他们知道这儿的房地产市场已经崩了吧？好吧，抱歉各位，我得拿斧子跟这扇门好好谈谈了。"
    l "等等。就算我们闯进去，这儿也不是能久待的地方。你还记得办公室发生的事。"
    scene c005_s007_037 with Dissolve(0.25)
    j "我没打算搬进来住，劳拉——"
    k "各位。"
    scene c005_s007_038 with Dissolve(0.25)
    j "——我们只需要找个地方喘口气。"
    l "我知道，可是有——"
    k "各位！"
    scene c005_s007_039 with Dissolve(0.5)
    k "看。"
    j "嗯？靠。"
    "雾里有东西在动。看不太清，但从它移动的方式看，至少是那些怪物中的一只。"
    j "好吧，这片社区算是泡汤了。我们得走。"
    scene blank with Dissolve(2)
    scene c005_s007_040 with Dissolve(2)
    j "我觉得我们甩掉它们了。"
    l "最好还是离开街道吧。趁运气还没用完，这些还只是有惊无险。感觉它们是闻着我们的气味，慢慢追着我们。"
    scene c005_s007_041 with Dissolve(0.25)
    k "我记得前面一点有宿舍。如果我对位置的判断没错，也就再走几个街区。"
    j "那可能更好。通常那些楼至少是对公众开放的。或者说，至少大堂是。要是能进去，我们就能把入口堵上，再从里面想办法。"
    l "也只能这样了。我不喜欢在外面待这么久。"
    "因为这开始让我们所有人都不好受了吗？"
    scene blank with Dissolve(2)
    scene c005_s007_012 with Dissolve(2)
    "走了一阵子，我们误打误撞来到了伊斯特曼街学生公寓，那是大学地块的外沿。"
    l "这边。这边。我好像看见这个方向有东西。"
    j "悠着点，劳拉。"
    stop music fadeout 2.0
    scene c005_s007_013 with Dissolve(0.25)
    j "好吧，这看起来有戏。身后有太多扇锁着的门了。"
    "我们得赶紧进到室内。我呼吸已经有点吃力了。我知道劳拉也是。还有卡莉……"
    scene c005_s007_014 with Dissolve(0.25)
    j "你后面还好吗？卡莉？"
    k "有点出汗，不过还好。*喘气*"
    play music monster
    scene c005_s007_015 with hpunch
    u "唔嗯~~~ 唔呃~~~！！！"
    scene c005_s007_016 with hpunch
    $ k_anxiety += 1
    k "{size=55}啊啊呜~~~~！！{/size}"
    scene c005_s007_017 with vpunch
    k "呃嗯！！！"
    scene c005_s007_017-1 with vpunch
    j "卡莉？"
    u "呃~~~ 呃呃~~~！！！"
    play sound hit
    scene c005_s007_018 with vpunch
    "*砰*！！*咚*！！"
    scene c005_s007_019 with Dissolve(0.25)
    j "{size=55}卡莉？！卡莉！操操操~~~！！！{/size}"
    l "[player_name]？怎——怎么回事——"
    scene c005_s007_020 with Dissolve(0.5)
    "这玩意儿他妈从哪儿冒出来的？靠，它直接从雾里窜出来，像是一直躲在那儿。然后像热追踪导弹一样扑上她。得快点。把它从她身上弄开。"
    scene c005_s007_021 with Dissolve(0.25)
    j "哇哦，王八蛋！这边，这边！看这个又高又吵的家伙。我这块可好吃多了。她瘦得皮包骨。"
    "它好像压根不在乎我在这儿。"
    play sound gas
    scene c005_s007_022 with flashyellow
    "靠，它用那玩意儿喷了她。我得进去把它从她身上扒下来。她整个人都暴露在外面。"
    j "嘿，臭东西！抬起头，对着镜头笑一个！"
    play sound axehit
    scene c005_s007_023 with flashred
    "*啪*！*吱吱吱*" with vpunch
    "把它打倒。把它从她身边弄开。"
    play sound hit
    scene c005_s007_024 with flashred
    "*砰*"
    play sound axehit
    scene c005_s007_025 with flashred
    "*咚*"
    "给我趴下，贱货！"
    scene c005_s007_026 with Dissolve(0.25)
    "我觉得成了。"
    j "*咳嗽*" with vpunch
    l "[player_name]？！卡莉！"
    scene c005_s007_027 with Dissolve(0.5)
    "得去看看卡莉。看看伤得有多重。"
    j "卡莉？卡莉！"
    "靠，她昏过去了。希望只是「昏过去」。摔倒的时候帽子和口罩都掉了。"
    scene c005_s007_028 with Dissolve(0.25)
    "还有脉搏。谢天谢地。我得把她扶起来，然后我们得离开这儿。"
    l "哦天，她是不是——"
    scene c005_s007_029 with Dissolve(0.25)
    j "昏迷了，还受了伤。来，接着斧子。我放在那边了。"
    l "好好。要是我没看错，那边还有一只。"
    scene c005_s007_030 with Dissolve(0.25)
    j "要是它冲我们来，瞄准头，砍到它不能动为止。"
    scene c005_s007_031 with Dissolve(0.5)
    j "好了，我扶到她了。我们{b}必须{/b}进屋。现在。别再纠结怎么破门了。"
    l "跟、跟我。我好像看见宿舍入口离这儿不远。"
    scene c005_s007_032 with Dissolve(0.5)
    "卡莉像块死重的东西挂在我怀里。彻底昏迷了。可我还能听见她呼吸里的喘鸣。我们最好离得很近了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    play music horror fadein 2.0
    scene c005_s008_001 with Dissolve(2)
    l "这边。[player_name]，这边！这儿有扇门。我想这就是入口。"
    j "锁着吗？"
    scene c005_s008_002 with Dissolve(0.25)
    l "这重要吗？"
    scene c005_s008_003 with Dissolve(0.25)
    j "那要是需要，你就砸门吧。"
    scene c005_s008_007 with Dissolve(1)
    l "至少我们能进屋躲雾。看看我们能不能……"
    scene c005_s008_004 with Dissolve(0.25)
    l "靠。锁着。退后——"
    u "不要！！走开！别过来！" with vpunch
    scene c005_s008_005 with Dissolve(0.25)
    l "什……？"
    "里面有人。我不该太意外。我们迟早会撞上别人的，这是大概率。"
    scene c005_s008_006 with Dissolve(0.25)
    l "嘿，救命！让我们进去！我们的朋友受伤了，我们需要把她带进去！"
    u "不不不不不——！！走开！走开啊！！！！你们不能进来！{size=55}他不能进来！{/size}"
    scene c005_s008_007 with Dissolve(0.25)
    j "什么？这听着还挺针对。嘿，我甚至都不认识你。"
    u "{b}走开！{/b}我看见它们在外面！它们全都变成那种怪物了！"
    scene c005_s008_008 with Dissolve(0.25)
    l "去他的。我们得进去。你听着，贱货，要么你把门开锁，要么我拿这把斧子劈进去。"
    "那这可是个大赌注，劳拉。为了安全而牺牲这扇门可不明智，毕竟这个小小的门厅看起来还挺能挡雾的。不过光是威胁本身，也许就足够让这姑娘相信我们是认真的。"
    scene c005_s008_009 with Dissolve(0.25)
    l "我最后警告你一次：从一数到三。一……"
    l "二……"
    u "好好好，等等！"
    scene c005_s008_010 with Dissolve(0.25)
    u "我开，但你要让他离我远点。求你了~~~我求求你。"
    "*咔嗒*"
    l "谢天谢地。给。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c005_s008_011 with Dissolve(2)
    play music insideday fadein 2.0
    play sound doorclose
    j "*叹气* 靠，谢了。"
    "我们还没进门，里面那位就已经逃之夭夭了。"
    scene c005_s008_012 with Dissolve(0.25)
    l "卡莉她……"
    j "在呼吸。不过还是昏迷着。"
    scene c005_s008_013 with Dissolve(0.25)
    l "哦，她脸上有些烧伤。还有她的衬衫……哇。布料上半截都烧焦了。我觉得那东西正在烧穿聚酯纤维。这件没救了。呃……上面还在渗出那种玩意儿。"
    j "她是近距离被喷中的。真要没穿外套，我都不敢想会糟成什么样。不过我们得把她弄到洗手间，试着把这东西冲掉。那个、呃……刚才在里面那姑娘呢？"
    scene c005_s008_014 with Dissolve(0.25)
    l "我敢肯定她跑了。感觉她挺怕你的。"
    j "我真的什么都没对她做。我不认识她。不过，那不重要。"
    l "不止这些，但在我们跟她谈过之前，我们不会知道。眼下……"
    scene c005_s008_015 with vpunch
    l "嘿！洗手间在哪儿？"
    scene c005_s008_016 with Dissolve(0.25)
    j "算了，劳拉，她帮不上什么忙。我自己找。我们已经浪费够多时间了。"
    "再说了，我担心她撞到了头。我希望只是被打昏过去，而不是更糟的情况。"
    l "嘿！我们的朋友受伤了，我们得找洗手间！在哪儿？！"
    u "{size=32}呃……在走廊尽头，右转，然后左手边最后一扇门。{/size}"
    scene c005_s008_017 with Dissolve(0.25)
    j "真是意外啊。"
    l "[player_name]，你能照顾一下卡莉吗？我抱不动她，所以我去跟那姑娘谈谈。试着把事情说开。或者，至少确保她不会趁我们转身时突然发难。"
    j "尽量别再冲她吼或者威胁她了，好吗。*轻笑*"
    scene c005_s008_018 with Dissolve(0.25)
    l "哈哈哈。那是一时激动，而且——"
    j "你的「母熊模式」上线了？"
    l "对。我猜是看到卡莉受伤触发了什么。我忍不住把她当成自己的孩子。"
    "我懂。那对我也是一种触发。"
    scene blank with Dissolve(2)
    scene c005_s009_001 with Dissolve(2)
    "好吧，看起来这就是宿舍的洗手间兼淋浴间。比我预想的要好。我找个水池。"
    k "唔嗯~~~ *咳嗽* *咳嗽*" with vpunch
    scene c005_s009_002 with Dissolve(0.5)
    j "卡莉？你有没有……"
    k "*咳嗽* 怎么……我的头……"
    scene c005_s009_003 with Dissolve(0.25)
    k "看东西看不清楚……"
    j "我们把你弄到水池边。试着把这东西冲掉。"
    "靠，这玩意儿真的在烧穿她的外套。"
    scene c005_s009_004 with Dissolve(1)
    k "{size=32}什……发生了什么……{/size}"
    j "你被一只怪物袭击了。它从背后抓住你，把你摔在地上。你昏迷了一小会儿。来，我扶你坐下。慢慢的。"
    scene c005_s009_005 with Dissolve(0.25)
    k "我、我们在哪啊啊啊~~~还没出去吗？"
    j "不。我们在一栋学生宿舍里面。试着洗洗你的脸。水池在你右手边。"
    scene c005_s009_006 with hpunch
    k "啊啊呜~~~"
    "平衡感乱了。她连站直都很费劲。"
    scene c005_s009_007 with Dissolve(0.25)
    j "没事。我扶着你，你慢慢来。"
    k "我、我看不见。什么都模模糊糊的。全是白的。我……哈啊~~~"
    scene c005_s009_008 with Dissolve(0.25)
    j "我知道。我之前也一样。你仰面躺着的时候被那玩意儿正面喷了一下。把它冲掉，过一会儿你就没事了。现在，我们把你的外套脱下来。"
    "趁上面残留的东西还没把合成纤维熔到你的皮肤上。"
    k "好、好吧……"
    scene c005_s009_009 with Dissolve(0.25)
    j "水池在你右手边。你要不要——"
    k "我、我想我摸索着能找到。只是别……"
    play sound zipper
    scene c005_s009_010 with Dissolve(0.25)
    j "我在这儿。不会走。"
    scene c005_s009_011 with Dissolve(0.25)
    "她受的冲击相当大，而且理由充分。我自己之前——在办公室——也挨了一下，我觉得都没这么严重。我只是有点轻微的刺激和烧伤，正在愈合。而且都被我的胡子挡住了。"
    play sound zipper
    scene c005_s009_012 with Dissolve(0.25)
    "可对卡莉来说严重得多，连外套都毁成那样了。我们得给她找点别的穿。还有她的帽子和眼镜也丢了。落在外面某处了。"
    scene c005_s009_013 with Dissolve(0.5)
    k "*喘气* *喘气* 我……我好疼。我的头……"
    j "怎么样？你在外面摔了一跤，撞到了地面。你{i}可能{/i}有脑震荡。"
    scene c005_s009_014 with Dissolve(0.25)
    k "头晕得厉害。皮肤疼。后背和胸口都疼。"
    j "你当时离得很近，它真的烧到了你的一部分衣服。"
    "而且我从这儿能看见你胸口起了水泡。"
    scene c005_s009_015 with Dissolve(0.25)
    k "感觉确实。我需要把它冲掉。不只是脸。胸口和后背，唔嗯~~~"
    j "好吧，那……看起来房间另一边有几个淋浴间。你想不想试一个？我知道这对我之前有点用。"
    scene c005_s009_016 with Dissolve(0.25)
    k "想，可是……啊啊啊~~~"
    j "要我帮你吗？"
    k "求你了。我、我看不见，而且站不稳。"
    scene c005_s009_017 with Dissolve(0.25)
    j "我知道。我不会离开你身边的，好吗？我就在这儿。我一只手扶着你。"
    k "谢、谢谢。"
    scene c005_s009_018 with Dissolve(1)
    "这过程很艰难，我们走得很慢。她视力受损，我得一步步带着她做完。"
    scene c005_s009_019 with Dissolve(0.5)
    "不止一次，我们不得不停下来等她咳完。跟劳拉最初出现时相比，卡莉在呼吸方面似乎没那么糟。另一方面，她的皮肤是灼伤的，好几处明显起了烫伤。"
    scene blank with Dissolve(2)
    scene c005_s014_004 with Dissolve(2)
    l "嘿，我……我为刚才的吼叫道歉……也为威胁人身安全的事道歉。我们的朋友受伤了，我们需要让她进来。我知道你们害怕。我们都害怕。但我们真的没有恶意。"
    l "我们真的没有恶意。我向你保证。"
    scene c005_s014_005 with Dissolve(0.5)
    "{color=#66ff33}我那份急躁和往前冲又一次让别人替我买单了。如果我当时做了不同的选择——哪怕一点点不同——也许卡莉就不会有事。我只是一直往前推、拼命跑，我知道[player_name]和卡莉都在努力跟上我。{/color}"
    scene c005_s014_006 with Dissolve(0.5)
    l "听着，我们没必要做朋友什么的，但别以为我们是来害你的。我不知道你之前遇到过什么，可我们处境相同。我们不得不躲开那些怪物。卡莉被其中一只袭击了。"
    "{color=#66ff33}在这儿纯属浪费时间。也许我该等局面平静下来之后再来试一次。{/color}"
    scene blank with Dissolve(2)
    scene c005_s009_020 with Dissolve(2)
    j "好了，到这儿了。你就站在这儿，我把水放上。"
    k "我……啊啊啊~~~"
    scene c005_s009_021 with Dissolve(0.25)
    j "其实，也许我们把你弄进淋浴间、拉上帘子、让你私下换衣服更好。把衣服扔出来，然后你自己开水。"
    if k_friend <= 6 or k_trust <= 5:
        k "我……好、好吧。但你要待在附近。我感觉不太好。"
        scene c005_s009_022 with Dissolve(0.25)
        j "当然，不走。来，跨过那个边沿。别绊着。"
        scene c005_s009_023 with Dissolve(0.25)
        j "然后把帘子拉上。你还好吗？"
        k "好、好吧。只是……就待在那儿。"
        scene c005_s009_024 with Dissolve(0.25)
        k "劳、拉在哪儿？"
        j "她去跟那个放我们进来的姑娘谈了。大概是刚才把她吓得不轻，正在安抚她。不过你要是不想一个人待着，我可以去叫她。"
        k "不、不，别。我、我现在不想一个人待着。我不信……我不……"
        scene c005_s009_025 with Dissolve(0.25)
        j "没关系。"
        "那是她的衬衫。我直接当垃圾扔了。她的外套已经烂成这样了，我也不知道这件衬衫还能不能救。"
        scene c005_s009_026 with Dissolve(0.25)
        k "你、你说劳拉在跟一个姑娘说话？"
        j "对，我们到的时候你已经昏过去了。"
        scene c005_s009_027 with Dissolve(0.25)
        "还有内衣。"
        j "我们到的时候，碰上了这个姑娘——你可以想象——她吓坏了，我们得说服她让我们进去。其实更准确地说，多亏劳拉那句位置恰到好处的威胁，我们才进去的。"
        scene c005_s009_028 with Dissolve(0.25)
        k "她、她不肯让我们进去？"
        j "我觉得她是被那些怪物吓到了。考虑到我们在路上看见的那么多，我能理解。而且不知为什么，她好像也很怕我在这儿。"
        j "我知道自己现在这副样子挺吓人的，不过要是她觉得我丑到那个份上，我还是会往心里去的。"
        k "她、她大概只是吓坏了。"
        j "对，我也这么想。我的自我形象已经经不起更多打击了。*轻笑*"
        scene c005_s009_029 with Dissolve(0.25)
        k "我、我好了。裸着。在……哪儿……"
        j "往这边来。开关在墙上。"
        k "我、我拿到了。谢谢。"
        play ambient shower
        "这比必要的难度大多了。自己都看不清，还得牵着一个盲人走。"
    else:
        scene c005_s009_030 with Dissolve(0.25)
        k "不，我……我站不太稳。你能不能就待在这儿？我不想摔倒。"
        j "好吧，呃……我至少先把淋浴的水开着。然后我去叫劳拉。她去跟那个终于放我们进来的姑娘谈了。刚才因为对方不配合冲她吼了，现在正安抚她。对，我越说出口，这事听起来越蠢。"
        scene c005_s009_031 with Dissolve(0.25)
        j "现在不重要。她应该能帮你换衣服。"
        k "不、不，别。我、我现在不想一个人待着。我不信……我不……"
        scene c005_s009_032 with Dissolve(0.25)
        j "你确定？真的、真的确定？因为——"
        k "求你了。没、没关系的。"
        scene c005_s009_033 with Dissolve(0.25)
        j "好吧，既然你这么说。我去把水放上。这样你就能洗热水澡了。"
        play ambient shower
        scene c005_s009_034 with Dissolve(0.25)
        j "好了，水热起来了。我该……你需要……"
        k "……"
        scene c005_s009_035 with Dissolve(0.25)
        j "呃，好，呃……那我先转过去。你要是想让我去叫劳拉，我也可以去。这个选择还在。"
        k "没、没事。你就待在附近。以防万一。"
        scene c005_s009_036 with Dissolve(0.25)
        j "我就在这儿。只是不看。我面朝另一边。所以你要是需要我扶稳，就伸手。或者出声。"
        k "我……谢谢你。*吸鼻子*"
        scene c005_s009_037 with Dissolve(0.25)
        k "你、你说劳拉在跟一个姑娘说话？"
        j "对，我们到的时候你已经昏过去了。我们到的时候碰上了一个姑娘——你可以想象——她吓坏了，我们得说服她让我们进去。更准确地说，是劳拉威胁了她。"
        scene c005_s009_038 with Dissolve(0.25)
        k "她、她不肯让我们进去？"
        j "我觉得她是被那些怪物吓到了。考虑到我们在路上看见的那么多，我理解。而且她好像也很怕我在这儿。"
        scene c005_s009_039 with Dissolve(0.25)
        j "我知道自己现在这副样子挺吓人的，不过要是她觉得我丑到那个份上，我还是会往心里去的。"
        k "她、她大概只是吓坏了。"
        scene c005_s009_040 with Dissolve(0.25)
        j "对，我也这么觉得。我的自我形象已经经不起更多打击了。*轻笑*"
        k "……"
        extend "*吸鼻子* *吸鼻子*"
        if k_friend >=9:
            $ ch5_kshowerhug = "yes"
            scene c005_s009_041 with Dissolve(0.25)
            k "*叹气* 哈啊~~~"
            j "你没事吧？需要帮忙吗？"
            scene c005_s009_042 with Dissolve(0.25)
            k "没事。只是……*叹气* 等一下。*吸鼻子*"
            "{color=#ffcccc}我好困惑。现在只有你紧挨着我身边，我才有安全感。我不明白为什么，但这是真的。别走。求你了。{/color}"
        scene c005_s009_043 with Dissolve(0.25)
        k "淋浴间……是往这边走吗？我……"
        j "对。在我右手边。你能听见水声。小心，有帘子。我留着了，你可以拉上。还有，注意第一步，那里有个边沿。别绊着。"
        scene c005_s009_044 with Dissolve(0.25)
        k "我……我好像看见了。不算真的{i}看见{/i}。模模糊糊的，可是……"
        j "视力在恢复？"
        k "慢慢地。嗯。"
        scene c005_s009_028 with Dissolve(0.25)
        "卡莉摇摇晃晃、跌跌撞撞，在陌生的环境里摸索了好一会儿才拉上帘子、挪进淋浴间。我很讨厌自己帮不上更多忙，可我们还没熟到那份上。也没熟到让我做这种事会心安理得。"
        scene c005_s009_029 with Dissolve(0.25)
        "不过我大概还是想说：我没看见她裸着身子，这样等我们出去之后，我就能直视安德鲁的双眼，而不必撒谎说卡莉和我之间的亲密有多出乎意料。那亲密程度也远超她会希望的。"
        "再说了，她都无法说「不」的情况下，我不会白占这个便宜。她还能站着洗漱，这让我松了口气。"
    scene c005_s009_045 with Dissolve(1)
    j "你头怎么样？抱歉，我老是问。"
    k "疼。但只有按到头皮才疼。我觉得没流血。"
    j "那就好。你刚才摔得可不轻。我敢说你除了撞了一下，没什么更严重的了。"
    scene c005_s009_080 with Dissolve(0.25)
    k "我的背……我觉得是淤青了。一碰就疼。"
    j "不意外。你像袋土豆似的被摔在地上。我看它是从背后抓住你的。等我反应过来发生了什么，你已经倒在地上了。"
    scene c005_s009_081 with Dissolve(0.25)
    k "那、那背包呢？"
    j "我们待会儿再说。"
    "等事情安顿下来，我去看看能不能找回来。"
    scene c005_s009_046 with Dissolve(0.25)
    "有一阵子我就站在那儿听着。卡莉在里面窸窸窣窣，听起来不像是会摔倒。事实上我得说，她状态在好转。或者至少是稳住了。"
    "我的心思转到劳拉身上，她还没出现。她还在跟那姑娘谈吗？我该担心吗？的确，她吓得想躲着我们，可她会袭击劳拉吗？"
    stop ambient
    scene c005_s009_047 with Dissolve(0.25)
    "我短暂地想过要不要去看看。等水声停下时，我觉得还是先看看卡莉怎么样、再做决定为好。"
    scene c005_s009_048 with vpunch
    k "呃嗯~~~"
    "她一屁股坐在地上的时候，我就知道自己不能离开她。"
    scene c005_s009_049 with Dissolve(0.5)
    j "卡莉？！嘿，嘿，你没——你——"
    k "没、没事。我的*喘气*腿没撑住。头还有点晕，热水澡让我*喘气* *喘气*……"
    scene c005_s009_050 with Dissolve(0.25)
    j "头晕？"
    k "对。*喘气* 让我在这儿坐一会儿。"
    j "要我给你拿点什么吗？毛巾？我去给你拿条毛巾。"
    scene c005_s009_051 with Dissolve(0.25)
    k "不用，不用。你能不能就……坐在这儿陪我？*吸鼻子*"
    j "当然，当然。"
    scene c005_s009_052 with Dissolve(0.25)
    k "我……谢谢。为……"
    j "没事。你现在看得清楚点了吗？我当时花了一会儿才恢复视力。"
    scene c005_s009_053 with Dissolve(0.25)
    k "*叹气* 还是模糊的。不过我能看见瓷砖。看见帘子。也能看见你坐在那儿。只是……细节不太清。软绵绵的色块，我得知道那是什么东西。"
    j "那就不错了。比我们刚进来的时候强。会恢复的。要是能找到点眼药水就好了。你头上那个包呢？抱歉老是问。"
    "也许我比自己以为的更焦虑，那种过度保护的本能被激活了。"
    scene c005_s009_054 with Dissolve(0.25)
    k "一跳一跳地疼。"
    j "我看看能不能找点止痛药。这附近肯定有急救包。"
    if ch5_kshowerhug == "yes":
        scene c005_s009_055 with Dissolve(0.25)
        j "还有，我该去给你拿那条毛巾了。以及你的衣服。可别折腾完了反倒着凉。"
        k "[player_name]……"
        k "我能……牵你的手吗？"
        scene c005_s009_056 with Dissolve(0.5)
        j "哦，当然。来。"
        k "*叹气*"
        scene c005_s009_057 with Dissolve(0.5)
        "她的手在我掌心里那么小、那么单薄。可她还是抓得很紧。我该让她安心，告诉她没事。虽然她赤身裸体、湿漉漉的，我们之间只隔着一道帘子，但她已经脱离危险了。"
        j "没事了。你现在安全了。什么都不会、也没有谁能再打扰你。有劳拉拿着斧子呢。*轻笑* 你要觉得我可怕，真该看看她拿着斧子的样子。她是只有油门没有刹车。"
        scene c005_s009_058 with Dissolve(0.25)
        k "我、我的脸怎么样？摸着很粗糙。"
        menu:
            "我把你带进来的时候，还没这么糟。":
                j "我把你带进来的时候，还没这么糟。"
            "我敢肯定现在也很可爱。\n[rgr](卡莉 好感 +1)":
                $ k_friend += 1
                j "我敢肯定现在也很可爱。"
        scene c005_s009_059 with Dissolve(0.25)
        k "听着。求你了。"
        j "好吧。"
        "别看她的奶子。别看她的奶子。"
        scene c005_s009_060 with Dissolve(0.5)
        k "怎么样？"
        j "对，有一些轻微的烧伤。还有眼睛受了刺激。没有什么是时间不能治愈的。"
        scene c005_s009_061 with Dissolve(0.25)
        k "那就好。你……没关系。要是你不小心……我知道你在努力不看。"
        j "对，我在努力。在这一切之外，你不用比现在更脆弱。而且我也没有那个权利……你懂的。"
        scene c005_s009_062 with Dissolve(0.25)
        k "谢谢……谢谢你为……"
        j "那条毛巾怎么样？我也该看看劳拉那边怎么样了。"
        scene c005_s009_063 with Dissolve(0.25)
        k "别……别走。求你了。"
        j "我不会丢下你的，姑娘。只是……劳拉在的话会方便些。总得有人在旁边确保你没事。"
        scene c005_s009_064 with Dissolve(0.25)
        k "会没事的。我……*叹气*"
        scene c005_s009_065 with Dissolve(0.5)
        j "我看见那边有几条毛巾。最多两秒。"
        k "谢谢。"
        scene c005_s009_066 with Dissolve(0.25)
        j "给。算不上最软的，但能擦干。想也别想更好。谁知道这是谁的。"
        scene c005_s009_069 with Dissolve(0.25)
        j "毛巾给你。你在……哦？你站起来了。"
        k "我要出来了。慢慢地。"
        scene c005_s009_070 with Dissolve(0.25)
        j "好吧。我先把目光挪开。"
        "你这样让我很不好办。对，我是想看你的奶子，但不是这种方式。"
        scene c005_s009_071 with Dissolve(0.25)
        j "来，我帮你把浴巾撑开。你现在看得清了吧？"
        k "看得清。*吸鼻子* 我自己来。"
        scene blank with Dissolve(1)
        scene c005_s009_072 with Dissolve(1)
        k "好了。你可以……你现在可以看了。"
        scene c005_s009_073 with Dissolve(0.5)
        j "好吧。你……你"
        k "有多严重？"
        scene c005_s009_074 with Dissolve(0.25)
        j "会愈合的，你会跟来这儿之前一样好。跟你一直一样好。"
        scene c005_s009_075 with Dissolve(0.25)
        k "*吸鼻子*"
        "她在这儿很挣扎。我能感觉到她身体里的虚弱。她撑着纯粹是因为我在。离她彻底没力气，大概也剩不了多少时间了。"
        scene c005_s009_076 with Dissolve(0.5)
        "这一整件事把我们推进了多少从来、从来不会发生的处境。本不该发生的事。这段故事我敢肯定我们永远不会告诉安德鲁——他的女朋友裹着浴巾、拼命抓着我。而我正努力不去想她不裹浴巾会是什么样子。"
        scene c005_s009_077 with Dissolve(0.25)
        l "[player_name]？卡莉？"
        j "劳拉？靠。你能在这儿等一下吗？我去叫劳拉。"
        scene c005_s009_078 with Dissolve(0.25)
        k "……"
        if ch5_kshowerhug == "yes":
            scene c005_s009_079 with Dissolve(0.25)
            "{color=#ffcccc}我只是想让你们再多抱我一会儿，这有那么错吗？就像……这是很久很久以来我第一次觉得被人保护着。{/color}"
        scene c005_s010_001 with Dissolve(1)
        j "劳拉！我们在这儿。卡莉在淋浴间这边。她刚洗完。没事吧？"
        scene c005_s010_002 with Dissolve(0.5)
        l "*叹气* 现在不行。她把自己锁在一个房间里不出来。我花了十分钟给卡莉找衣服。这里大部分房间都被搬空了。"
        j "暑假。或者……夏季学期？快开学了对吧？"
        scene c005_s010_003 with Dissolve(0.25)
        l "对。这周就该开始。我找到了一些东西。既然她的外套看起来很糟。她怎么样？"
        j "她挺能扛的。头上挨了一下。说后背有淤青。而且我看她脸上和肩膀有烧伤。所幸没有什么是不能愈合的。不过眼下她看不清东西，平衡感也完蛋了。我们得守着她一阵子。虽然我很确定她讨厌这个主意。"
        scene c005_s010_004 with Dissolve(0.25)
        j "现在她需要你。我给她裹了条浴巾，但我觉得不该让她一个人待着。"
    else:
        scene c005_s009_065 with Dissolve(0.5)
        j "我该给你拿条毛巾。还有你的衣服。我看看还能不能救。"
        k "我……谢谢你。"
        scene c005_s009_066 with Dissolve(0.5)
        j "给。算不上最软的，但能擦干。想也别想更好。谁知道这是谁的。"
        scene c005_s009_067 with Dissolve(0.5)
        j "毛巾给你。我去看看劳拉那边怎么样。等她出现了，好吗？你穿衣服的时候得有人在旁边。我保证不会久。我们俩一个就会回来。"
        k "好。"
        scene c005_s009_068 with Dissolve(0.25)
        "虽然不忍心把她一个人留着，可我得确认劳拉没出事。"
        scene c005_s010_001 with Dissolve(1)
        l "[player_name]？卡莉？"
        j "我们在这儿。卡莉在淋浴间这边。我正想去找你。没事吧？"
        scene c005_s010_002 with Dissolve(0.5)
        l "*叹气* 现在不行。她把自己锁在一个房间里不出来。我花了十分钟给卡莉找衣服。这里大部分房间都被搬空了。"
        j "暑假。或者……夏季学期？快开学了对吧？"
        scene c005_s010_003 with Dissolve(0.25)
        l "对。这周就该开始。我找到了一些东西。既然她的外套看起来很糟。她怎么样？"
        j "她挺能扛的。头上挨了一下。说后背有淤青。而且我看她脸上和肩膀有烧伤。所幸没有什么是不能愈合的。不过眼下她看不清东西，平衡感也完蛋了。我们得守着她一阵子。虽然我很确定她讨厌这个主意。"
        scene c005_s010_004 with Dissolve(0.25)
        j "现在她需要你。我给了她一条毛巾擦身，但我觉得不该让她一个人待着。"
    scene c005_s010_005 with Dissolve(0.25)
    l "而且你没有……"
    j "我在努力当个绅士。我没看见某些东西——某些部位——我敢肯定她也希望维持这样。"
    scene c005_s010_006 with Dissolve(0.25)
    l "我懂。我那样看见她是一回事，一个男人那样看见又是另一回事。"
    j "对。"
    l "那就别走远。以防我们需要你。也因为我不想再让那个姑娘更不安了。她看起来相当笃定地认为你会变成那种怪物。"
    scene c005_s010_007 with Dissolve(0.5)
    j "当然。我就出去一分钟，看看情况。有需要就喊我。"
    l "我会的。"
    scene c005_s010_008 with Dissolve(1)
    l "卡莉。哦，姑娘，你……"
    k "很糟，对吧？"
    scene c005_s010_009 with Dissolve(0.25)
    l "没有什么是不能愈合的。"
    k "这不算回答。"
    scene c005_s010_010 with Dissolve(0.25)
    l "可能比这糟得多。[player_name]之前挨得同样重。区别是他没有你这种瓷器般的皮肤。"
    scene c005_s010_011 with Dissolve(0.25)
    l "来，我给你找了一套干净衣服。哪怕往好了想，我觉得你也不会想再穿回那身「出门的衣服」。"
    k "不。我……你能站近一点吗？我不知道自己的腿现在还行不行。"
    scene c005_s010_012 with Dissolve(0.25)
    l "不会丢下你。让我去拿衣服。我放在长椅上了。"
    scene c005_s010_013 with Dissolve(1)
    k "你、你打听到那姑娘的事了吗？[player_name]说这儿已经有人了。"
    l "她勉强给了点配合。我试着跟她谈谈，但她对我一言不发，把自己锁进了宿舍的一间房里。我不意外。这第一印象可不太好。"
    play sound zipper
    scene c005_s010_014 with Dissolve(0.25)
    k "她是学生，对吧？"
    l "我敢这么押。也可能她跟我们一样自己找到这儿来的。不过更可能的是，夏季学期她住在宿舍里。也许开学前就住下了，然后雾就来了。"
    scene c005_s010_015 with Dissolve(0.25)
    l "彼得本来也该这么做。他有一门化学课和实验要修。他说夏天先修比跟其他课一起修省事。我想我该庆幸他决定留在佐治亚州。"
    k "那衣服……呢？"
    scene c005_s010_017 with Dissolve(0.25)
    l "我又找到一间没被搬空的房间。所以也许她不是唯一还留在校园里的人。我没仔细查她是不是一个人。[player_name]——"
    scene c005_s010_018 with hpunch
    k "啊！！"
    l "你没事吧？"
    scene c005_s010_019 with Dissolve(0.25)
    k "只是……只是有点站不稳。"
    l "是头上那个包搞的。你在外面待了一阵子。可能有点脑震荡。来，我扶着你，别摔了。"
    scene c005_s010_020 with Dissolve(0.25)
    k "谢谢。你刚才说到[player_name]？"
    l "哦对，他说他要出去一下，看看我们周围的情况。宿舍里面（他最好是说他不出宿舍）。我们一路赶到这儿，根本没仔细确认这个地方安全不安全。我想在室内、没沾到雾，就够好了。"
    scene blank with Dissolve(2)
    scene c005_s010_021 with Dissolve(2)
    "快速扫了一圈周围之后，我回到洗手间看看卡莉和劳拉怎么样。我们慌慌张张弃了 SUV、接着遭到伏击、然后拼命想找个「安全」的地方，这一连串下来，我们把我们所在位置目前是什么状况完全忽略了。"
    "从我能推断的来看，证据虽然有限，那个姑娘（还锁在自己房间里）就是这儿唯一的人。"
    scene c005_s010_022 with Dissolve(0.25)
    "另外有几个房间看起来还没被收拾。也许还有别的学生来过，但后来走了。"
    "正门和通往楼梯的门都被锁上了（其实正门是我们自己又锁的）。另一头还有一个出口，用家具堵住了。"
    scene c005_s010_023 with Dissolve(0.25)
    "我之后得做一次更彻底的搜索，不过先……"
    scene c005_s010_024 with Dissolve(0.25)
    l "你在这儿还好吗？"
    k "浑身都疼，不过眼下这样就不错了。"
    scene c005_s010_025 with Dissolve(0.5)
    j "女士们。"
    l "[player_name]。你没事吧？我知道出事的时候你离卡莉很近。"
    scene c005_s010_026 with Dissolve(0.25)
    j "哦？对。我出去之前洗过了。卡莉伤得最重。你呢？"
    l "我得洗。"
    scene c005_s010_027 with Dissolve(0.25)
    j "水池在那边。你洗的时候我陪卡莉待着。"
    k "我本想说我不用人看着，不过……"
    scene c005_s010_028 with Dissolve(0.5)
    j "没事的，姑娘。现在让我们先照顾你。我们很快就会让你找个地方休息。你好点了吗？"
    k "头还疼。皮肤也是火辣辣的。视力嘛……"
    scene c005_s010_029 with Dissolve(0.25)
    j "会好的。信我。"
    k "我……我信。"
    scene c005_s010_030 with Dissolve(0.25)
    k "那么，这边情况怎么样？"
    j "正门锁着。通往楼上的门也锁着。所以上面我还没查，不过除了我们那位新朋友，我没听见这儿还有别人。另一个出口被堵住了。我还没试过那通向哪儿。"
    scene c005_s010_031 with Dissolve(0.25)
    j "有些房间里还有东西。床单。私人物品。这里头有个故事，但可能得从那位姑娘嘴里才能问出来。"
    l "看来我得再对她说几句好话，才能让她出来。"
    scene c005_s010_032 with Dissolve(0.25)
    menu:
        "用你的妈妈嗓音。\n[rrd](劳拉 好感 -1)":
            $ l_friend -= 1
            j "用你的妈妈嗓音。我敢肯定那比我去说好使。卡莉？需要搭把手吗？"
        "[gr]你会比我强。":
            j "你会比我强。卡莉？需要搭把手吗？"
    scene c005_s010_033 with Dissolve(0.25)
    l "她对你好像异常抵触。"
    j "我不认识她。我发誓不认识。"
    scene c005_s010_034 with Dissolve(0.5)
    k "也许她以为你是那种怪物之一。"
    j "这话我可往心里去了。*轻笑*"
    l "不重要。眼下不重要。我们得能休息。我知道大家都累垮了。也就是说我们得确保她不会成为麻烦。"
    scene c005_s010_035 with Dissolve(0.25)
    j "你可以再威胁她一次。"
    l "这没用。现在……卡莉，我们尽量把你弄到一间屋子里去休息吧。躺在真正的床上。"
    k "好、好吧。"
    scene c005_s010_036 with Dissolve(0.5)
    l "你能走吗？"
    j "需要的话我可以背她。"
    scene c005_s010_037 with Dissolve(0.25)
    k "不用不用，我自己能走。"
    "卡莉看起来那么胆小，可她要是执拗起来，跟劳拉一样倔。"
    scene c005_s010_038 with Dissolve(0.25)
    k "那我们的背包呢？里面还有我们的衣服之类的东西。"
    l "还在外面。当时我没想到要拿。"
    j "我去——"
    scene c005_s010_039 with Dissolve(0.25)
    l "[player_name]~~~。"
    j "以后再说吧。不过我们确实得找时间把它拿回来。"
    "因为我们现在拥有的只有身上这套衣服。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c005_s011_001 with Dissolve(2)
    play music nightmain2 fadein 2.0
    "于是我们分头行动。我留下劳拉照看卡莉，自己对所在位置做一次更全面的评估。我不想再来一次「锁着的门后面藏着怪物」。"
    scene blank with Dissolve(2)
    scene c005_s011_002 with Dissolve(2)
    "幸好，我找到三层长得一样的走廊和一样的房间，大部分都是空的。事实上，除了那扇锁着的门——门后那个姑娘还在躲着我——只有另外三间房看起来有人用过。"
    scene blank with Dissolve(2)
    scene c005_s011_003 with Dissolve(2)
    "一楼一头有一个休息区兼小厨房，这让人挺期待，只要我们能搜刮到足够的食物撑一阵子。"
    scene blank with Dissolve(2)
    scene c005_s011_004 with Dissolve(2)
    "能撑多久？不知道。我们冲向医院的计划暂时搁置了。至少得等卡莉恢复到能再出去。而且我们还得给她弄件新外套。"
    scene blank with Dissolve(2)
    scene c005_s011_005 with Dissolve(2)
    "据我所见，后门通过一条走廊连着附近的一栋教学楼。如果我没记错——我好多年前来过这儿——那是哈灵顿楼，文学院所在地。如果我们有时间，也许可以过去看看能翻出什么有意思的东西。"
    scene blank with Dissolve(2)
    scene c005_s011_006 with Dissolve(2)
    "但现在？我他妈累坏了，而且我得去跟大家报个平安。凭我们最近这运气，谁知道我会查出什么来。"
    play sound doorclose
    scene c005_s011_007 with Dissolve(0.25)
    l "你在这儿。我都开始担心了。"
    j "就是在各层转转。她……怎么样了？"
    scene c005_s011_008 with Dissolve(0.5)
    l "睡着了。没用多久。我只是出来找你的。今晚我陪着她，保险一点。烧伤不算太糟，会愈合的。可她的眼睛……我不知道，也许我们能找点眼药水帮上忙？至于头上，我觉得可能只是轻微脑震荡。所幸也没出血。"
    l "那这个地方呢？拜托你告诉我有好消息。"
    scene c005_s011_009 with Dissolve(0.25)
    j "空的，除了我们和……她。后门被封死了。我想它通向哈灵顿楼，所以需要的话我们可以去那边探探。正门锁着，我还拖了些东西挡在前面，以防万一。"
    j "窗户看起来全都是那种夹层玻璃，里面嵌着固定铁丝网。牢固成这样，你会以为这是监狱，不过我猜他们只是不想让人闯进去。或者闯出来。"
    scene c005_s011_010 with Dissolve(0.25)
    l "这让我稍微放心了些。"
    j "那你呢？你怎么样？"
    scene c005_s011_011 with Dissolve(0.25)
    l "累瘫了。不过呼吸好多了。还有那个喘不掉的咳喘。而且我很失望。我是真的让自己相信那辆车能带我们走更远。我希望它成真。我需要它成真。"
    j "我大概正好相反。一路上我都在等它抛锚。我们能开这么远已经算走运了。"
    scene c005_s011_012 with Dissolve(0.25)
    l "我们不会再遇到第二辆那样的车了吧？"
    menu:
        "我们走运过一次。\n[rgr](劳拉 好感 +1)":
            $ l_friend += 1
            j "不知道。我们走运过一次。而且校园里肯定还有能开的东西。"
            scene c005_s011_013 with Dissolve(0.25)
            l "那就指望一下吧。"
        "我可不敢指望。":
            j "我可不敢指望。我们得想别的办法。也许徒步穿过校园。"
            scene c005_s011_013 with Dissolve(0.25)
            l "*叹气* 大概吧。"
    if l_sex >= 1:
        scene c005_s011_014 with Dissolve(0.5)
        l "我……靠，[player_name]。我不想承认，但要是没有你，我大概早就崩了。"
        j "你本来也能撑住的。你是个坚强、有目标的女人。"
        scene c005_s011_015 with Dissolve(0.25)
        l "不是那么回事。而且，也许我只是厌倦了坚强。厌倦我们受伤。饿了。不睡好觉。"
        j "床倒是随你挑。"
        scene c005_s011_016 with Dissolve(0.25)
        l "那算升级了。行吧。但我睡不好也不全是因为床。"
        j "我知道。可你得接受这一刻本来的样子。我们在这儿是安全的。大家都活着。而且明天可以重新开始。"
        l "那也只能这样了。"
    scene c005_s011_017 with Dissolve(0.5)
    j "嘿，我想为刚才在外面对你说话太冲道个歉。"
    l "没关系。当时气氛紧张，时间又紧。我敢肯定我在外面也没表现得多好。说实话，卡莉好像是唯一一个没失去冷静的人。"
    j "或者说，她挤不进我们俩中间插一句话。*轻笑*"
    scene c005_s011_018 with Dissolve(0.25)
    l "她不够强势也没关系。不是每个人都能强势。"
    j "我平时也不是，但没办法……魔鬼逼得人不得不强。"
    scene c005_s011_019 with Dissolve(0.25)
    j "那，那个姑娘……"
    l "我能想到的只有把门锁上。我不知道她是不是危险，但我们必须假设她是。明天我再试着跟她谈。"
    scene c005_s011_020 with Dissolve(0.25)
    j "或者，等卡莉好点让她去。"
    l "因为她跟她年纪更接近？"
    scene c005_s011_021 with Dissolve(0.25)
    j "对，也因为她现在不会把她视为威胁。"
    l "这也是原因之一。"
    j "不过今晚还是把门锁好。"
    scene c005_s011_022 with Dissolve(1)
    "没过多久，劳拉跟我道了晚安就回去了。有那么一瞬间，我想到自己也许可以跟她们同住一间房，但这个念头过去了。我们有足够的床，我觉得也需要找回一点隐私。"
    scene c005_s011_023 with Dissolve(0.5)
    "尽管我们相处得越久，就越难不陷入那种「事后绝不会跟外面的人提起」的处境。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_29_824", transition=Dissolve(1.0))()
    pause
    $ Hide("june_29_824", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music kallietheme fadein 2.0
    scene c005_s012_001 with Dissolve(2)
    k "唔嗯~~~ 唔嗯~~~"
    scene c005_s012_002 with Dissolve(0.25)
    k "*打哈欠*"
    l "早上好，卡莉。"
    scene c005_s012_003 with Dissolve(0.25)
    k "哦，劳拉。早上好。我猜我昨晚睡得很死。"
    l "你大概是的。我也知道终于有张床睡感觉不坏。你怎么样？"
    scene c005_s012_004 with Dissolve(0.25)
    k "僵硬。我下背是淤青，又酸又疼。脖子也是。"
    l "皮肤呢？"
    scene c005_s012_005 with Dissolve(0.25)
    k "痒。而且毛衣有些地方磨到伤口了。不过我不介意你找来的衣服。我……我总得有件能穿的。我不知道我的衣服还能不能救。"
    l "外套肯定不行了。有几处都烧穿了。等晾干了我们再看看其他的。"
    scene c005_s012_006 with Dissolve(0.25)
    k "……好。昨天发生了什么？我只记得跟在你们后面，然后有什么东西抓住了我的背包，接着我就被拽倒了。"
    l "我没看到全部。我甚至不知道出事了，直到听见你尖叫，然后[player_name]大喊。我跑回去的时候，他已经把那东西打倒在地，正把斧子往它背上砍。"
    scene c005_s012_007 with Dissolve(1)
    l "*叹气* 我……我从第一次你遇上那种东西开始，就一直在想这件事的现实——它们是活生生的生物。我不知道它们是什么、怎么来的，但它们会流血、会死。我只是……从来没想过自己会是一个能接受杀生的人。"
    l "我也从没想过[player_name]你会这样。当然，我不是在评判他。"
    k "它们一直都先攻击我们。[player_name]从没攻击过没先想伤害我们的那只。"
    scene c005_s012_008 with Dissolve(0.25)
    l "我知道，所以我才没那么难受。但这么短时间就落到这一步，还是挺可悲的。不是你死就是我亡。如果它们做的那些事真算是杀人。"
    k "……那感觉并不好受。我跟你说。"
    scene c005_s012_009 with Dissolve(0.25)
    l "我……对不起。我不是想贬低你经历的事。"
    k "没关系。"
    scene c005_s012_010 with Dissolve(1)
    k "我暂且认为这个地方还行。暂时还行。"
    l "[player_name]确认了我们暂时没事。两个出口都封好了。所有房间都查过。除了那个姑娘——她还躲着——这里只有我们。没有别的意外。我昨晚把门锁上了，以防万一。"
    scene c005_s012_011 with Dissolve(0.25)
    k "那就好。难得。她还是不肯出来也不肯说话？"
    l "还是太早。不过昨天她一进去就把门锁上了。我能理解。我们确实有点强行闯入了。"
    k "要是我一个人在这儿待上几周，我肯定也怕死了。"
    scene c005_s012_012 with Dissolve(0.25)
    l "好吧，我该去洗漱一下，看看这儿有没有什么能吃的。"
    k "劳拉……"
    scene c005_s012_013 with Dissolve(0.25)
    l "嗯？要帮忙？来，我扶你一把。"
    k "也许吧，不过……我得问你件事。前几天你问起安德鲁和我的时候……"
    l "我只是随口找点话说，因为我们一直没机会聊。"
    scene c005_s012_014 with Dissolve(0.25)
    k "可你问的都是些有针对性的问题。我知道是。而这让我开始想——我一个人时经常这样——也许我意识到了一些让我不太好受的事。或者我没意识到，只是在自欺欺人。"
    l "哦，卡莉，我不是想——"
    scene c005_s012_015 with Dissolve(0.25)
    k "你已经有猜测了，对吧？有什么地方不对劲。我跟你讲我和他是怎么认识的时候，就开始对其中一些事实感到不舒服。比如，他比我大那么多。"
    l "你看，我并不想评判他。如果他让你幸福，那才是最重要的。可我听到了一些话——一些具体的词句——让我觉得很不妙。你要是说我错了，我也能理解。"
    l "而且年龄差距确实可能是个问题。但如果这对你们来说行得通，那不过是我自己那些先入为主的偏见，不是你的问题。"
    scene c005_s012_016 with Dissolve(0.5)
    k "还不止这个。第一次失去手机信号的时候，我慌了。不只是因为我想听到他或者家人的消息，而是因为我总觉得必须跟他报个到。怎么说呢，我怕他因为我第一晚不在家会生气。"
    k "但是，我离他越久，那种焦虑着要向他汇报的冲动就越淡。手机打不通这件事，好像解开了我身上某种束缚。事实上，我开始觉得，是他一直在把我和我的家人隔开。和我以前那些朋友。"
    scene c005_s012_017 with Dissolve(0.25)
    k "我觉得自己挺蠢的。因为我想，他在我还小、还不太合群的时候对我那么温柔、给我那么多关注，才让我把心思全放在了他身上。我不想失去那一切，因为感觉他好像是唯一一个想要我的男人。至少我以前是这么想的。又或者，是他让我这么想的。他跟我说，不会有人像他那样爱我。"
    l "天哪。我……*叹气* 我本希望不是真的，但我想，我之前的担心也许是对的。大概我只是没怎么在他身边，每次聊天都只听他说好听的。对不起。"
    scene c005_s012_018 with Dissolve(0.25)
    k "这不是……不是你的错。"
    l "不，卡莉。我之前就该多问问你。也许我早一点听到这个故事，就会开口了。你需要的是一个朋友。一个能挺身而出的人。而且，我想，在一群男人堆里上班也没什么帮助。"
    scene c005_s012_019 with Dissolve(0.25)
    l "如果[player_name]不是正忙着离婚那摊子事，他可能早就发现有什么不对劲了。"
    k "他——他也是我会有这种想法的原因之一。他把我们俩都当成平等的人对待，还说什么大家是一条心，这种感觉太陌生了。它让我反复怀疑自己。「安德鲁会怎么做？」而答案往往不怎么样。当「控制欲强」这个词冒进我脑子，我就知道事情不妙。"
    scene c005_s012_020 with Dissolve(0.5)
    l "是啊，不是什么好事。听着，等我们出去以后，我觉得你得跟安德鲁好好谈一次。你甚至可以考虑搬出去，给自己一点时间想清楚自己需要什么、想要什么。要是真得搬，你可以先住我那儿一阵子，等你站稳了脚跟再说。"
    k "谢谢。我……如果这件事能带来什么好的结果，那就是我知道，往后我有两个可以信任的人了。"
    l "是啊，我觉得我也一样。好了，起来吧，去洗漱一下，再看看有没有什么能当早餐的。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_29_936", transition=Dissolve(1.0))()
    pause
    $ Hide("june_29_936", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday2 fadein 2.0
    scene c005_s013_001 with Dissolve(2)
    "得承认，我昨晚睡得比很长一段时间以来都好。是的，躺到床上时我累得要死，但我没有像往常那样醒好几次，动不动就浑身僵硬酸痛，因为睡得实在难受。事实上，我相当确定自己比平时晚了很多才醒。"
    scene c005_s013_002 with Dissolve(0.5)
    "我在小厨房里转了转，看有没有什么东西能勉强算作早餐。或者说，来杯咖啡。我已经穿上外套，打算再出去一趟。有件事我本来想见到劳拉时跟她说。刚才听见洗手间里有水声，我猜她已经起床忙活了。"
    scene c005_s013_003 with Dissolve(0.25)
    l "你在干什么？"
    j "早上好啊。刚才在找咖啡喝。要来点吗？*轻笑*"
    scene c005_s013_004 with Dissolve(0.5)
    l "别装傻，[player_name]。"
    j "对，我是要出去。那次袭击之后我们跑得太急，东西都落下了，我打算去取回来。话说回来，卡莉怎么样了？我听见你们俩在洗手间里说话，所以我想「好多了」吧。"
    scene c005_s013_005 with Dissolve(0.25)
    l "她会没事的。烧伤会慢慢好起来。要不是你及时赶到，情况只会更糟。但脑震荡和她背上的淤青才是拖慢她的地方。她现在平衡感还是有问题。站久了腿就发软。"
    j "那就好。我是说，不是那件事本身好，而是她能恢复过来。我们暂时住这儿，这地方看起来还行。至少眼下如此。她只能好好休养。然后我们得想清楚下一步怎么办。"
    scene c005_s013_006 with Dissolve(0.25)
    l "但是[player_name]，别以为我忘了。我不高兴你这么做。昨天我们才刚在外面。卡莉还受着伤。我知道你累了，在外面待了这么久，现在大概浑身都还在发疼，而你自己也才刚遭过袭击。"
    j "劳拉，我明白，但我没打算在外面待很久。更不是要去把这片地方逛个遍。我就是出去一下，把背包——还有别的东西——拿回来，也许顺便看一眼附近的楼。"
    l "背包可以等。"
    j "能等吗？我们都见识过那雾把车弄成什么样了。里面还有衣服和一些吃的，我们用得上。"
    scene c005_s013_007 with Dissolve(0.25)
    l "宿舍里还留了一些东西，卡莉和我可以穿。看起来雾来之前这儿住了几个女生。"
    j "对，女生。这是女生宿舍。你可能不记得了，但我是男的。我可不想在逃出去之前一直穿着那件臭烘烘的工作衬衫。所以，也许我去把背包拿回来，顺便看看那边那栋楼是不是男生该住的地方。我不会进去，但我得先摸个路，以后再来的时候好认。"
    scene c005_s013_008 with Dissolve(0.25)
    l "*嘟囔着*"
    scene c005_s013_009 with Dissolve(1)
    j "你从那位……有没有听到什么消息？我们还没互通过名字，而且我厌倦了说「那个女的」，就像我厌倦了把外面那些东西称作「怪物」，或者讽刺地叫它们「我们的朋友」一样。"
    l "还没有。安静得像教堂里的老鼠。"
    menu:
        "[rd]我们该担心吗？\n[rrd](劳拉 焦虑 +1)":
            $ l_anxiety += 1
            j "我们该担心吗？担心她……你懂的？死在里面了？"
            scene c005_s013_010 with Dissolve(0.25)
            l "呃，希望不是。这念头也太丧气了。"
            j "是吗？想想我们到目前为止经历过的这一切？"
            scene c005_s013_011 with Dissolve(0.25)
            l "说得也是。"
        "[gr]我们晚点再去试试。":
            j "我们晚点再去试试。总得有个时候让她知道我们没有恶意。或者你们俩里总有一个能做到。不知怎么的，我之前对不起过她。"
            scene c005_s013_010 with Dissolve(0.25)
            l "我还是觉得卡莉最合适，因为{b}你{/b}不是她，那个威胁要硬闯进来的疯女人也不是。"
            j "也不碍事。"
    if l_sex >= 2:
        scene c005_s013_013 with Dissolve(0.25)
    else:
        scene c005_s013_012 with Dissolve(0.25)
    l "喂，小心点，好吗？出去别干蠢事。别逞英雄。"
    j "跟平时一样不蠢。我去拿斧头，然后就走。"
    l "在我和卡莉昨晚睡的那个房间里。我去给你拿来，顺便送你出去。在这儿等着，用不了一分钟。"
    scene c005_s013_014 with Dissolve(1)
    "我明白劳拉平时反应和说话的方式往往有点尖刻，但我知道她不是故意要刻薄。她只是很直接，不绕弯子地表达自己想说的话。我挺欣赏她这种坦率、不加修饰的做事方式。"
    scene c005_s013_015 with Dissolve(0.25)
    "而且没错，紧张归紧张，我们每个人多少都在某个时候受过伤。可事情还是得做。我们不能干耗着舔伤口。"
    if k_friend >= 10:
        scene c005_s013_019 with Dissolve(0.25)
        $ ch5_kallieseenoff = "yes"
        k "喂……你、你要出去？"
        j "喂，你。你还好吗？"
        scene c005_s013_020 with Dissolve(0.25)
        k "只能说好过一点。不过我还活着，这就是个好的开始。你打算去拿背包吗？"
        menu:
            "里面有几套挺漂亮的衣服。\n[rgr](卡莉 好感 +1)":
                $ k_friend +=1
                j "我知道里面有几套挺漂亮的衣服。*轻笑* 我寻思着换几身衣服也好。"
            "我们现有的任何补给都用得上。":
                j "我们打包带出来的东西都用得上。几瓶瓶装水，办公室拿的零食，还有手电筒。"
        scene c005_s013_021 with Dissolve(0.5)
        k "对不起，我……"
        j "不是你的错。这些混蛋明显是伏击型的捕食者，所以我在外面开路的时候得更聪明一点。要是我那么做了，你就不会被扑倒。"
        scene c005_s013_022 with Dissolve(0.25)
        k "没关系。你……在外面小心点。"
        j "我打算那么做。赶紧去把背包拿来，然后回来。"
        if k_desire >= 4:
            scene c005_s013_024 with Dissolve(0.25)
            k "好。"
            "卡莉这样抱来抱去的，我倒是能习惯了。不过其中一部分原因可能是她需要点东西让自己安定下来。我能感觉到她的腿在发抖。"
        else:
            scene c005_s013_023 with Dissolve(0.25)
            k "很好。"
        scene c005_s013_025 with Dissolve(0.25)
    else:
        scene c005_s013_016 with Dissolve(0.5)
    l "明白了。你现在打算走吗？"
    j "对。最多给我三十分钟。"
    if ch5_kallieseenoff == "yes":
        scene c005_s013_026 with Dissolve(0.5)
        l "我送你到门口。你走以后我把门锁上。卡莉，我会在前门等。我们最好别耽搁太久。"
        k  "好。"
        scene c005_s013_027 with Dissolve(0.25)
        "{color=#ffcccc}*叹气* 我能撑的时间也就这么多了。我想得过几天才能缓过来。{/color}"
    else:
        scene c005_s013_017 with Dissolve(0.25)
        l "我送你到门口。你走以后我把门锁上。"
        j "好。"
    play sound doorclose
    scene c005_s013_018 with Dissolve(1)
    $ renpy.pause ()
    scene blank with Dissolve(2)
    scene c005_s013_028 with Dissolve(2)
    if ch5_kallieseenoff == "yes":
        "{color=#ffcccc}我不喜欢[player_name]出去，尤其还是因为我。我告诉过自己不会成为累赘，结果还是这样。我受了伤，总得有人替我收拾烂摊子。{/color}"
    else:
        "{color=#ffcccc}听起来[player_name]要出去。大概是去拿背包。我不喜欢这样，尤其是他这么做是因为我。我告诉过自己不会成为累赘，结果还是这样。我受了伤，总得有人替我收拾烂摊子。{/color}"
    scene c005_s013_028-1 with Dissolve(0.25)
    "{color=#ffcccc}他们一直告诉我不是那样，但我厌倦了那种感觉——好像我做的事没他们多。或者，根本做不到。{/color}"
    play sound doorclose
    scene c005_s013_029 with Dissolve(0.5)
    u "呃，你好？"
    k "哦，呃……嗨。"
    if persistent.ch5_complete == False:
        $ persistent.ch5_complete = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_chapter5", transition=slideright)()
        pause
        $ Hide("achievement_chapter5", transition=dissolve)()
        $ quick_menu = True
label chapter06:
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("chapter06", transition=Dissolve(1.0))()
    pause
    $ Hide("chapter06", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c006_s002_001 with Dissolve(2)
    play music outsideday fadein 2.0
    "好了，开始吧。而且要快。过去几天我出去太多次，暴露在这种雾里太频繁了。走到这儿，再有一两天恢复，对我们所有人来说大概都是必要的。"
    "昨天走了那一小段之后，我对横穿整座城没什么信心。也许我们可以穿过校园，从一栋楼挪到另一栋楼，但横穿草坪绝对不行了。我没那个力气了，而且我知道卡莉短时间内也撑不住。"
    scene c006_s002_002 with Dissolve(0.5)
    "同时，劳拉现在神经绷得太紧了，我怕她随时会崩。她真的把所有希望都押在坐SUV去医院上吗？考虑到我们的车一碰到雾就那么快完蛋，这一直都不现实。"
    "我想我一直都知道她有点「{a=https://en.wikipedia.org/wiki/Type_A_and_Type_B_personality_theory}A型性格{/a}」，而这件事真的在压迫她。"
    scene c006_s002_003 with Dissolve(0.5)
    "这就意味着我不能再由着她的性子来。不能那么一味顺从，免得我们又给自己招麻烦。我知道我这辈子大半时间都随波逐流——南希没少数落我，说我没法掌控局面——但我知道我不能再这样了。"
    scene c006_s002_004 with Dissolve(1)
    "好了，我们是在……我们是从哪儿出来的？浓雾里四周都是长得一模一样的楼，很难辨认方位。"
    scene c006_s002_005 with Dissolve(0.25)
    "哦，找到了。应该是。"
    "对，一堆死掉的玩意儿。呃，好吧，你正在……腐烂？很难说。看起来脏兮兮的，而且你身上的雾味浓得不得了。最好别在这儿多待。说实话，我本以为你会臭得多。"
    scene c006_s002_006 with Dissolve(0.25)
    "背包在哪儿？卡莉的帽子呢？"
    scene c006_s002_007 with Dissolve(0.25)
    "这是什么？"
    scene c006_s002_008 with Dissolve(0.25)
    "哦，嘿，一部手机。卡莉的手机。她一定是摔倒的时候掉了。我拿回去给她。就算联系不上任何人，她肯定也会因为拿回来而松一口气。"
    scene blank with Dissolve(1)
    scene c006_s002_009 with Dissolve(1)
    "在周围翻找了几分钟后，我把东西都找回来了，只剩她的面罩。我们得再弄一个，或者随便做个替代品才能再次出发。现在既然已经出来了，要不要顺便侦查一下？"
    menu:
        "[gr]最好现在就回去。":
            $ ch6_backearly = "yes"
            "我最好现在就回去。劳拉已经够焦虑了，我要是再磨蹭个三十分钟左右，可能真会把她逼到极限。"
        "[rd]也许可以稍微看一会儿。\n[rrd](卡莉 焦虑 +1)":
            $ l_anxiety += 1
            "就稍微一会儿吧。看看周围这些楼。"
            scene blank with Dissolve(2)
            scene c006_s002_010 with Dissolve(2)
            "好了，这看起来是个进楼的好办法。要是跟另外那栋一样，我稍花点力气就能进去。看情况——我们打算住多久、有没有吃的——也许我会回来再翻找一番。"
            scene c006_s002_011 with Dissolve(0.5)
            "我不该在外面待太久。虽然我很想趁这段时间干点入室盗窃之类的事，但我不想再赌运气了。就好像我能感觉到外面还有别的东西。正在四处游荡。"
            scene blank with Dissolve(2)
            scene c006_s002_012 with Dissolve(2)
            "好了，这就确认了这也是一栋宿舍楼。我几乎看不清里面，这没什么帮助，但我很确定那是和我昨晚睡的那种一样的床。"
            scene c006_s002_013 with Dissolve(0.5)
            "嗯？靠，外面有什么东西{b}在{/b}动。趁它还没转向我，我们赶紧他妈离开这儿。"
    scene blank with Dissolve(2)
    scene c006_s002_014 with Dissolve(2)
    l "*叹气*"
    "{color=#66ff33}真是一团糟。而且这里面很大一部分都是我的错。我就是……我等不了。一天都等不了。连一分钟都不肯等，好让卡莉不用那么拼命跟上我们。我赶得要死，结果把[player_name]和卡莉都推进了会让他们受伤的境地。{/color}"
    "{color=#66ff33}但这就是我这个人。老是「走、走、走」。这在工作时也许是优点，可一旦超出自己的领域就没那么妙了。又或者，我是在拿这个当借口，好像是我星座才让我这么做的。{/color}"
    scene c006_s002_015 with Dissolve(0.25)
    "{color=#66ff33}可我停不下来。我还在琢磨怎么让队伍重新动起来。我一直在纠结附近会有什么车。因为我需要知道。彼得是安全的。基思……{/color}"
    "{color=#66ff33}我必须知道他没事。我还爱着他，哪怕我恨他。该死，他对我们这段失败的婚姻也负有责任。这样多少年了？有多少个深夜，是因为他在跟别人上床？{/color}"
    scene c006_s002_016 with Dissolve(0.25)
    "{color=#66ff33}我必须知道。到了这一步，我只想把一切都弄清楚。因为我们得把他的出轨摊到明面上。{/color}"
    if l_sex >= 1:
        "{color=#66ff33}也许我可以告诉他，在别人的怀抱里寻找慰藉的并不只有他一个。只是要让他明白，能让别人动心的并不只有他。{/color}"
    scene c006_s002_017 with Dissolve(0.25)
    "{color=#66ff33}操，劳拉，这事真是一团乱麻。{/color}"
    play sound doorclose
    scene c006_s002_018 with Dissolve(0.5)
    j "我回——来——啦~~~ 想我了？"
    if ch6_backearly == "no":
        l "我他妈刚才还正担心呢。你没事吧？"
        j "没事。就是去隔壁那栋宿舍楼瞄了一眼。还没进去，不过查查看有没有补给、或者我们这儿缺的东西，是个不错的主意。"
        l "只是别……{size=30}别逼我……{/size}"
        scene c006_s002_019 with Dissolve(0.25)
        l "好好好。看来你把背包拿回来了。而且看起来还算完好。在外面一切都还好吗？"
        j "还好吧。我在外面没看到什么。嗯，倒是看到了一个{i}那种东西{/i}，但它表现得像是没看见我。我们出去的时候一定得留意周围。"
    else:
        l "可算来了。你出去的时候悠闲地散了个步？"
        j "很高兴你心情好到还能拿这个开玩笑。"
        scene c006_s002_019 with Dissolve(0.25)
        l "也没什么大不了的……*呻吟* 好好好。看来你把背包拿回来了。而且看起来还算完好。在外面一切都还好吗？"
        j "还好吧。我在外面没看到什么。我觉得听见外面有什么动静，但没看见东西。我们出去的时候一定得留意周围。"
    scene c006_s002_020 with Dissolve(0.25)
    j "不过{a=https://www.merriam-webster.com/dictionary/TL;DR}一句话总结{/a}就是：我到了，把能找到的卡莉的东西拿走，现在人在这儿了。她的面罩不见了，不过我找到了她的眼镜和帽子，晾一晾的话，她等会儿应该就能用。"
    l "*叹气* 好。我们进去吧，等我把这两扇门锁上。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c006_s003_001 with Dissolve(2)
    play music insideday fadein 2.0
    l "好了，把东西拿出来看看还有哪些能用的。至少我们能把食物和饮料……"
    scene c006_s003_002 with Dissolve(0.25)
    $ s_anxiety +=1
    l "哦，你好。"
    u "啊啊啊……"
    scene c006_s003_003 with Dissolve(0.25)
    k "没事的。就像我之前说的，它们没有恶意。只是特别护主，而且当时情况太紧张了。"
    u "好、好吧……"
    "我大概该退后一点，让卡莉和劳拉来处理这个。尤其她之前对我的反应那么激烈。"
    scene c006_s003_004 with Dissolve(0.5)
    k "所以，这位是雪莉——"
    $ s_met = "yes"
    s "雪莉·华莱士。"
    l "我是劳拉·米尔斯，这位是[player_name] [player_lastname]。很抱歉之前那样跟你见面，但现在你知道情况了，我相信你能理解。我不是想冲你尖叫、威胁你，但我们必须进屋。是有正当理由的，希望你能明白。"
    scene c006_s003_005 with Dissolve(0.25)
    k "我把发生的事告诉她了。"
    s "我、我明白了。卡莉说你们正开车往这边来，只好找地方躲起来。还说她被一个灼烧者袭击了。"
    scene c006_s003_006 with Dissolve(0.5)
    j "灼烧者？"
    s "那是我给它们起的名字。他们出去之后被雾灼伤，然后就变成了那些东西。"
    scene c006_s003_007 with Dissolve(0.25)
    j "说实话，我挺喜欢这个叫法。总比一直喊「怪物」「生物」强。"
    l "那不重要。告诉我，你说的「他们出去了」是什么意思？"
    scene c006_s003_008 with Dissolve(0.5)
    s "我……我当时就在这儿。我和另外几个女生——梅茜、特里安娜、布丽——暑期学期就住在这儿。我们有——现在还有——房间。雾一来，我们就困在这儿了。我们，还有那边男生宿舍的家伙们。过了几天，他们有些人就过来了，开始商量我们该怎么办。"
    s "当然了，话题就转到些蠢事上，比如重新繁衍地球之类的。但一旦发现我们大多数人根本不担心这个，大家就都在吵着要离开这儿。可他们既定不下要去哪儿，也想不出该怎么走。"
    scene c006_s003_009 with Dissolve(0.25)
    s "一天早上，特里安娜和两个男的就这么{b}从正门走了{/b}。他们走了，再也没回来。那天晚些时候，来了几个灼烧者，在院子里游荡。"
    s "我们从二楼的窗户勉强能看见他们。其中一个男的——我记得他叫卡尔——说他们宿舍有个人大概是把窗户开着忘了关，同样的事就发生在他身上了。"
    "雾把他们变成灼烧者，这跟我一直在推测的还算吻合，但不知道她说的时间线准不准。"
    scene c006_s003_010 with Dissolve(0.25)
    s "没过多久，布丽、梅茜和其余几个男的就决定从后门走。说是打算尽量穿过一栋栋楼横穿校园。他们走了以后，我就再没听到他们的消息。我把门堵上了，因为我怕他们出了什么事。"
    l "为什么？你为什么会那么想？"
    scene c006_s003_011 with Dissolve(0.25)
    s "那天晚些时候，我听见那边传来喊叫声。或者说我以为那是。也可能是别的。我不知道是什么，但他们再也没回来。"
    menu:
        "[rd]那之后呢？\n[rrd](雪莉 焦虑 +1)":
            $ s_anxiety +=1
            j "那之后呢？你再没见过他们，也没听过他们的消息？"
            scene c006_s003_012 with Dissolve(0.25)
            s "没有。就……就这么没了。我不知道发生了什么，而且我觉得我也不想知道。"
        "[gr]什么都别说。":
            "让她按自己的记忆讲吧。她受的刺激可能太深，追问只会适得其反。"
    scene c006_s003_013 with Dissolve(0.5)
    l "嗯……那你为什么留下来？我猜他们说要走的时候，你考虑过跟他们一起走。"
    s "我心里过不去。而且他们也不知道要去哪儿。就一句「不在这儿」而已。我不确定这样够不够。要是他们到了一个没有床、没有食物、没有水的地方呢？然后就只是从一个地方流浪到另一个地方。"
    s "再加上，卡尔和另一个男的就是那种货色。他们老想说服我们跟他们一起喝酒。我当时就有种感觉：要是他们把我们中的任何一个单独弄到手，坏事就要发生了。"
    scene c006_s003_014 with Dissolve(0.25)
    "我想追问一下她之前说的、最先离开的那批人变成了灼烧者的事，但我不确定能从她嘴里问出多少。她给我的感觉像是受了惊吓。也可能有点呆。或者两者都有。"
    menu:
        "[gr]暂时别追了。":
            "现在最好是别逼得太紧。让她到外面来是好的第一步，幸好她看起来对我们不构成威胁。"
        "[rd]还是问吧。\n[rrd](雪莉 焦虑 +1)":
            $ s_anxiety +=1
            j "那么，关于你刚才说的……关于灼烧者。你怎么知道那些离开的人变成了那样？你亲眼看到了吗？那听起来太可怕了。"
            "前提是真的。"
            scene c006_s003_015 with Dissolve(0.25)
            s "我、我没亲眼看到。但……几天前我看到一个在附近游荡，它身上……怎么说呢……有个男的那天穿着件浅蓝色的翻领短袖。Izod的。是Izod的。所以那个蹒跚着走的东西，脖子那儿有一块同样颜色的布料，像是衣领。"
            l "这可有点麻烦了。"
            scene c006_s003_007 with Dissolve(0.25)
            s "对。我……如果你看看外面那些——我见过几个——全都是个头很大、块头像男人的。我不知道特里安娜怎么了。我只知道她当时穿着件红色的羽绒服，后来就再也没见过那件衣服。"
            j "得留个心眼。"
    scene c006_s003_016 with Dissolve(1)
    "到现在我觉得，我在这儿可能反而让她焦虑。看来卡莉做得不错，把她带出来跟我们说话了。我该溜开一下，把她交给劳拉，看看她们能不能问出更多。"
    j "我要去洗漱一下。也许再看看有没有什么能穿的，不至于还是那套穿了好几周的工作服。"
    l "行行行。我一会儿就来找你。"
    scene c006_s003_017 with Dissolve(0.25)
    j "嗯。很高兴认识你，雪莉。"
    s "呃，嗯……"
    scene blank with Dissolve(2)
    scene c006_s003_018 with Dissolve(2)
    "所以，雪莉……女大学生，雾来的时候还留在校园里。按她自己的说法，她当时不是一个人，但其他人都决定离开这儿。有一批人想从外面硬闯出去，另一批人则打算穿过一栋栋楼横穿校园，这计划也不算最差。"
    "但她留下了。当然，她解释说是不喜欢带头的那几个男的，可我觉得不止如此。又或者，她只是那种觉得熬下去情况就会变好的人。"
    scene c006_s003_019 with Dissolve(0.25)
    "她说那批人变成了灼烧者？我不知道该怎么看待。我自己也有一套类似的推测，但听她这么一说，我心里反而没那么笃定了。这个说法仍然站得住脚，但我想，不亲眼见到证据，听起来实在太离谱。"
    "哦，还有把这东西叫成「灼烧者」？这个我能接受。还是专有名词好使。"
    scene c006_s003_020 with Dissolve(0.25)
    "难怪我们出现的时候她怕我。在那种能见度下，我又把卡莉抱在怀里，我的轮廓看起来可能就像她说的那种灼烧者。尤其是如果看起来像我在追着劳拉跑。再说，如果她认为人在外面待久了就会变成那东西——行，我现在明白了。"
    "这就意味着我们三个人现在变成四个了，不管她愿不愿意。我们不能就这么把她留在这儿。就算她恨这个主意。希望我们能说服她这是最好的选择。"
    scene c006_s003_021 with Dissolve(0.25)
    "走之前我们有几天时间。卡莉得恢复，而我还得给她弄一件新外套。顺便看看雪莉那边有什么东西。"
    scene blank with Dissolve(2)
    scene c006_s003_023 with Dissolve(2)
    "好了，我们回去看看……"
    s "来吧。我有些东西你应该能穿。其他人跑的时候，我顺手拿了一堆自己喜欢的。其实我们早就在互相换衣服穿了——至少我和布丽是这样。"
    k "好、好吧。"
    if ch5_kshowerhug == "yes":
        scene c006_s003_025 with Dissolve(0.25)
    else:
        scene c006_s003_024 with Dissolve(0.25)
    "我想是雪莉更适合？也可能只是因为卡莉的年纪更接近她，也是我们几个里最不吓人的一个，所以她俩更容易处得来。"
    s "还有几件可爱的，肯定正合你的身。我穿就有点小了，就算硬往里塞也塞不下。*咯咯笑*"
    play sound doorclose
    scene c006_s003_026 with Dissolve(0.5)
    j "所以，我猜我们对新来的这位没意见了？"
    l "我不敢说完全没意见，不过她和卡莉聊起衣服来了。你知道……我们没什么选择，只能到处搜刮着找东西穿。我猜这让她也想把自己有的拿出来显摆一下。"
    j "她还真是一片好心。"
    scene c006_s003_027 with Dissolve(0.25)
    l "换个话题似乎真的让她一下子活过来了。她之前总是心不在焉，细节也说得很含糊，然后她们俩就聊起了卡莉的毛衣，接着东一句西一句，她的情绪就好了起来。一旦聊到跟外面和那些人无关的事，她就来劲了。"
    j "还从她那儿问出别的有用东西了吗？她说的倒也不是完全没信息量。"
    scene c006_s003_028 with Dissolve(0.25)
    l "我不知道她对事实有多准。感觉她不太留心，而且就算留心了，也是被动的。关于那些人的说法，感觉缺了不少细节。"
    menu:
        "她可能有所隐瞒。":
            j "那我们得小心点。她可能有所隐瞒。"
        "创伤会搞乱你的记忆。":
            j "创伤会搞乱你的记忆，劳拉。她还年轻，可能只是进入了生存模式。"
    scene c006_s003_029 with Dissolve(0.25)
    l "*叹气* 是啊。那我们该检查一下背包，看看里面有没有什么不对劲。"
    j "它封得很严实，所以希望不会有东西需要多处理，晾一晾就行。"
    scene c006_s003_030 with Dissolve(0.25)
    l "你觉得我们会在这儿待多久？"
    menu:
        "几天。\n[rrd](劳拉 焦虑 +1)":
            $ l_anxiety +=1
            j "最多几天。我们得给卡莉弄一件新外套，也得看看雪莉那边有什么。我接下来一两天就专门用来想清楚最好的行动方案。"
        "够卡莉恢复就行。":
            j "够卡莉恢复就行。而且我们得给她弄一件新外套，也得看看雪莉那边有什么。我接下来一两天就专门用来想清楚最好的行动方案。"
    scene c006_s003_031 with Dissolve(1)
    l "你觉得雪莉会跟我们走吗？我印象里她想在这儿长期窝下去。"
    j "我们不能心安理得地把她丢下，对吧？"
    scene c006_s003_032 with Dissolve(0.25)
    l "不，我不是那个意思。不过，如果她反对，也别太意外。我们可能得说服她离开才是最好的选择。除非卡莉提过，我们其实还没跟她说过我们为什么要上路。"
    j "我们其实还没正式问过她，对吧？也许她已经准备好走了。谁知道她一个人在这儿待了多久。老实说，我自己都记不清过了几天。"
    scene c006_s003_033 with Dissolve(0.25)
    l "我还没问。"
    "因为你一直惦记着这事儿，对不对？"
    scene blank with Dissolve(2)
    scene c006_s004_001 with Dissolve(2)
    s "好好好，我看看有没有你会喜欢的。不过，乞丐也没资格挑，对吧？*咯咯笑*"
    k "你有什么我能穿的，我都很感激。"
    scene c006_s004_002 with Dissolve(0.25)
    s "没问题，姑娘。所以你是说你们所有人这几周基本都穿着同一套衣服？我天，那也太惨了。我有不少换洗的，但不能送去洗衣店洗，这点也够让人难受的。"
    k "我们在普罗维登斯生活楼的健身中心找到了几件，但都不太是我平时会穿的。"
    scene c006_s004_003 with Dissolve(0.25)
    s "好吧，看看我到这儿之后搜罗的东西会不会好些。算我走运，得以保留去年的宿舍房间，主要是为了不用收拾东西搬到校园另一边去。"
    s "哦哟~~~ 也许这件。所以……你和[player_name]。你们俩是不是有一腿？"
    scene c006_s004_004 with Dissolve(0.25)
    k "我、我订婚了。"
    s "嗯哼。那看来是没戏了。不过不管我自己的情况怎么样，要是有一个男的像他那样把我救出来、从雾里抱着我走，我肯定永远不会拒绝让那个男人上我的床。他随时都可以上，懂的都懂。*咯咯笑*"
    scene c006_s004_005 with Dissolve(0.25)
    k "啊呼~~~"
    s "他在勾搭劳拉？她虽然年纪大点，但我敢打赌床上功夫肯定好。看起来那么紧绷的女人，肯定有狂野的一面。"
    scene c006_s004_006 with Dissolve(0.25)
    k "她、她结婚了。"
    s "啥？所以他是自由的？没结婚什么的，也没有女朋友？"
    k "不，他、他离过婚。"
    scene c006_s004_007 with Dissolve(0.25)
    s "嗯，好。来，试试这件合不合适。你比特里安娜矮了大概半英尺，可能会有点大，但总比你那件毛衣睡得舒服。"
    k "哦？呃……我觉得这件遮不了多少。"
    scene c006_s004_008 with Dissolve(0.25)
    s "呃。小心点的话没人会看到你的奶子。再说，你大概也就穿着睡觉。不过要是你在宿舍里这么穿，说不定能放出一个「随时可以上」的信号。"
    k "……"
    scene c006_s004_009 with Dissolve(0.25)
    s "那你毕业多久了？或者说你还在念？我压根没想过你可能是一边上班一边把学位读完的。要是你真的在上班的话。我一直没在这附近见过你——"
    k "呃，啊~~~"
    scene c006_s004_010 with Dissolve(0.25)
    s "——不过这也不难相信。我确实在美术楼那边待得太久了。他们从来不告诉你，上那种课每天在工作室要待三个小时，所以你最多只能挤出三门课。这就是我为什么不得不去上暑假的课。"
    s "或者是曾经。我不觉得我这样能拿到学分。也许我爸妈能把学费退一部分，因为老爸绝不可能付了钱还让我不去上课。他要是付了钱结果我人被困在这儿，肯定气炸了。天啊，我真希望能跟他们说上话。我一直没能用手机打通任何人的电话。你呢？"
    scene c006_s004_011 with Dissolve(0.25)
    k "没、没有。从一开始就没有。"
    s "我就知道。彻底断联太惨了。网上那么多东西我都错过了。要是我再不快点回去，我所有朋友都会以为我在放他们鸽子。"
    scene c006_s004_012 with Dissolve(0.25)
    s "这么干也太混账了吧？因为电话断了就认定我生活里没别的事，还反倒怪我。你会以为人们能理解，但很多人根本不会替别人想。"
    s "哦哟~~~ 你试试这件呗？"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_29_348", transition=Dissolve(1.0))()
    pause
    $ Hide("june_29_348", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday2 fadein 2.0
    scene c006_s005_001 with Dissolve(2)
    "我打开电视的时候就没抱什么期望。但要是不试着看看能不能收到点什么，那就太说不过去了。哪怕只能听到外面世界一两句含混不清的话，也比最近强多了。结果我等来的是一片雪花和失望。"
    scene c006_s005_002 with Dissolve(0.5)
    k "有动静吗？"
    j "哦，嗨，卡莉。都没听见你说话。没有，还是那些。不过还是值得一看，因为哪怕只能听到一丁点消息，理论上也是有帮助的。看你换了新衣服。"
    scene c006_s005_003 with Dissolve(0.5)
    k "雪莉给了我几件。穿不出去见人，但舒服多了。别告诉劳拉，那件毛衣穿在我背和肩膀上真的一点都不舒服。"
    j "我猜那些伤处应该还很嫩。放心，我不会说。说到劳拉，我最后看到她把背包里的东西拿出来摆开晾了一会儿。看起来都还挺好的。"
    scene c006_s005_004 with Dissolve(0.25)
    k "那就好。"
    j "我看雪莉跟你熟络起来了。她怎么样？"
    scene c006_s005_005 with Dissolve(0.25)
    k "她挺好的。大概吧。我还不太了解她。看得出她一旦觉得自在点了，就因为身边有人而兴奋起来。可能兴奋得有点过头。她会有点……闹。我不是贬义，但……"
    j "她很咋呼？要是她一个人在这儿待了很久，可能正需要跟人接触。多半是个外向的人。"
    scene c006_s005_006 with Dissolve(0.25)
    k "对，我觉得就是。她、她没有你能穿的衣服。我问过了，她全是女生的东西。"
    j "我也没指望有。不过还是谢谢你问，我记着这份心。但男生宿舍就在对面。我明天过去看看能找到点什么。"
    scene c006_s005_007 with Dissolve(0.25)
    k "你确定那样安全吗？"
    menu:
        "我不知道。\n[rrd](卡莉 焦虑 +1)":
            $ k_anxiety += 1
            j "说实话，我不知道。但这事必须做。我得看看那边有没有值得拿的东西。"
        "我会速去速回。":
            j "我会速去速回。要是情况不对，我可没打算多待。"
    scene c006_s005_008 with Dissolve(0.25)
    k "……"
    scene c006_s005_009 with Dissolve(0.5)
    j "你怎么样？今天看起来稳当多了。"
    k "累，头也开始疼了。我想我醒着的时间太长了。"
    j "我去给你拿点药。"
    scene c006_s005_010 with Dissolve(0.25)
    k "不不，我没事。我只要休息一下。我正准备回自己那个房间。也就是我们现在那个房间。你……你知道我的意思。"
    j "好。如果你需要什么——"
    scene c006_s005_011 with Dissolve(0.25)
    k "我会告诉你的。"
    scene c006_s005_012 with Dissolve(0.5)
    "哦，等等，我刚才出去的时候顺手捡了她的手机。我该还给她。或者，该吗？最近这部手机一直是她焦虑的来源。当然，最终我还是得还给她，不过今天她或许该专心休养。"
    menu:
        "还给她吧。\n[rgr](卡莉 好感 +1)\n[rrd](卡莉 焦虑 +1)\n[grr]":
            $ ch6_givecellphone = "yes"
            $ k_anxiety += 1
            $ k_friend += 1
            scene c006_s005_013 with Dissolve(0.5)
            j "哦，嗨，我在外面捡到了你的手机。想必是你摔倒的时候从口袋里掉了出来。"
            k "真的吗？我……我到这儿以后都没想过这事。"
            scene c006_s005_014 with Dissolve(0.25)
            j "我去帮你拿过来，好让你拿着。"
            k "呃……好。"
            scene c006_s005_015 with Dissolve(0.25)
            j "给你。希望没摔得太坏。"
            k "谢、谢谢。我看看还能不能用。"
        "不客气。":
            "还是先留着吧。至少等她恢复几天、身体好点了再说。现在把手机给她，只会重新引爆她和安德鲁、和家人失去联系的创伤。我理解这个道理，但现在她该做的只是休息。"
    scene c006_s005_016 with Dissolve(0.5)
    k "我……我去休息一会儿。"
    j "行行行。既然有时间，就好好歇着吧。"
    scene c006_s005_017 with Dissolve(0.25)
    k "我、我会的。回头见。"
    j "回头见。电视上要是我听到什么，一定告诉你。"
    if ch5_kshowerhug == "yes":
        scene c006_s005_018 with Dissolve(0.25)
        "我也不是指望真能收到什么，但总得试试，对吧？"
    scene blank with Dissolve(2)
    if ch6_givecellphone == "yes":
        scene c006_s005_019 with Dissolve(2)
        "{color=#ffcccc}我很感激他做的事，但我其实有点希望[player_name]没找到我的手机。我本该松一口气，可一看到它，心里涌上来的只有一阵恐惧，好像它不见了我才真的自由。我甚至都没意识到自己失去了它。当然了，从那之后不到一天就发生了太多事。{/color}"
        scene c006_s005_020 with Dissolve(0.25)
        "{color=#ffcccc}我本该感激：万一以后手机又有信号了，我就能联系上父母。可我感受不到。我只看到安德鲁送我的这部手机——那是他为了能……为了能什么？{/color}"
        "{color=#ffcccc}越想越觉得，他做的一切都是为了盯着我。把我和其他所有人隔开。不知怎么的，我的套餐成了「长途通话分钟有限」，意思是给妈妈打的每通电话都短而直接。没有一句废话。{/color}"
        scene c006_s005_021 with Dissolve(0.25)
        "{color=#ffcccc}妈妈到底在不在乎发生了什么？或者，她压根就没想过这件事？她是不是只顾着高兴——大孩子终于搬出家门，跟一个迟早会娶她的男人住在一起，因为这就是她和那一代人好像唯一在乎的事？{/color}"
        scene c006_s005_023 with Dissolve(0.25)
        "{color=#ffcccc}操，越想越气。也越意识到我原来一直被囚禁着。我还小、还容易拿捏的时候，他把我收在了羽翼下——我是个书呆子、内向的人，而他把这一点用足了。然后他带着我们搬家，让我变得离不开他。{/color}"
        scene c006_s005_024 with vpunch
        k "操他妈的！！！"
        scene c006_s005_025 with Dissolve(0.5)
        "{color=#ffcccc}等我们出去以后，我要走，回北边老家。就算身上只剩这身衣服也无所谓。我只希望我爸妈和兄弟姐妹都平安。[player_name]好像觉得不在这一带的人都该没事。我只希望他是对的。{/color}"
        scene c006_s005_026 with Dissolve(0.25)
        "{color=#ffcccc}我也觉得他说得对。广播里听得清的部分我都听见了。而他们用的是「隔离区」「受影响区域」这种词，听起来好像并不是到处都这样。{/color}"
        scene c006_s005_027 with Dissolve(0.25)
        "{color=#ffcccc}我真不想离开劳拉和[player_name]——过去几周我们变得这么亲近——但等我们出去以后，我不能留在这附近。如果我想救自己，就不能。我甚至不知道自己还能不能再见安德鲁。{/color}"
        "{color=#ffcccc}要是真见了，他肯定会想办法说服我留下。我不……我不觉得自己有力气把他推开，就算我知道那才是对的。{/color}"
        scene c006_s005_028 with Dissolve(0.25)
        "{color=#ffcccc}这枚戒指？我真舍不得交出去。这是别人给过我最漂亮的东西。但我不能留着。它……它会标出我是个所有物。我……我回到北边以后会把它寄给他。我必须跟他保持距离。{/color}"
    else:
        scene c006_s005_025 with Dissolve(2)
        k "*叹气*"
        "{color=#ffcccc}天哪，好疼，而且我实在太累了。我只想一直睡到我们离开这儿的那一刻。到时候叫醒我就行。我们去哪儿？不知道。医院？我不……我希望安德鲁不在那儿等我。他……他大概已经离开这座城了吧。万一他们是用停机坪把人撤出去的。{/color}"
        scene c006_s005_026 with Dissolve(0.25)
        "{color=#ffcccc}等我们出去以后，我要走，回北边老家。就算身上只剩这身衣服也无所谓。我只希望我爸妈和兄弟姐妹都平安。[player_name]好像觉得不在这一带的人都该没事。我只希望他是对的。{/color}"
        scene c006_s005_027 with Dissolve(0.25)
        "{color=#ffcccc}不过，广播里听得清的部分我都听见了。而他们用的是「隔离区」「受影响区域」这种词，听起来好像并不是到处都这样。{/color}"
        "{color=#ffcccc}我真不想离开劳拉和[player_name]——过去几周我们变得这么亲近——但等我们出去以后，我不能留在这附近。如果我想救自己，就不能。我甚至不知道自己还能不能再见安德鲁。要是真见了，他肯定会想办法说服我留下。我不……我不觉得自己有力气把他推开，就算我知道那才是对的。{/color}"
        scene c006_s005_028 with Dissolve(0.25)
        "{color=#ffcccc}这枚戒指？我真舍不得交出去。这是别人给过我最漂亮的东西。但我不能留着。它……它会标出我是个所有物。我……我回到北边以后会把它寄给他。我必须跟他保持距离。{/color}"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_29_812", transition=Dissolve(1.0))()
    pause
    $ Hide("june_29_812", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain2 fadein 2.0
    scene c006_s006_001 with Dissolve(2)
    "当电视和外面的车流声断断续续地消失一阵子之后，那点雪花声就像海妖的召唤一样，哪怕隔着另一个房间。我听见那嗡嗡声，就决定去看看。"
    scene c006_s006_002 with Dissolve(0.5)
    j "人家说这么近看电视伤眼睛。"
    l "哦，呃……是啊。"
    scene c006_s006_003 with Dissolve(0.25)
    j "听见或看见什么了吗？"
    l "没有。就是……白噪音。"
    j "你在这儿盯着它多久了？"
    scene c006_s006_004 with Dissolve(0.5)
    l "*叹气* 很难说。我现在分不太清现在到底是几点了。挺怪的，感觉我们到这儿已经过了好几个月。我知道不是……我知道它没有感觉中那么久。"
    menu:
        "其实也就几周。[yl]":
            j "对，其实也就几周。我知道它没有感觉中那么久。"
        "时间的感知是件挺奇怪的事。[yl]":
            j "我们对时间的感知是件挺奇怪的事。它感觉起来比实际要长。我们太习惯一天之内想做什么就做什么、想去哪儿就去哪儿，所以跟那比起来，我们到目前为止这点进展显得小得可笑。"
    scene c006_s006_005 with Dissolve(0.25)
    l "是啊……"
    j "你男朋友没事的，劳拉。就跟卡莉的家人一样，他在这场混乱之外，很安全。多半是在担心他妈，但他的处境比我们好。"
    scene c006_s006_006 with Dissolve(0.25)
    l "你怎么知道？你有什么证据？"
    "说实话，很大程度上只是毫无根据地相信这事不是到处都在。因为如果真是到处都那样，我们跑也就没意义了。"
    scene c006_s006_007 with Dissolve(0.25)
    j "再说了，新闻广播你跟我一样都听到了。确实很残破，也不太说得通，但如果整个国家都烂成这样，他们不可能在搞什么隔离。说不通的。某个地方一定有人在局外看着这一切。不然我们听到的会是完全不同的消息。"
    j "比如「我的天，我们全完蛋了」。或者同样有用的什么东西。"
    "劳拉今晚格外焦躁。我认识她这么久，从没见她这么……毛躁过。我想是接连不断的压力，加上她对自己做过的某些决定心里不太踏实，正在把她磨垮。"
    menu:
        "正面硬扛吧。":
            j "听着，我知道很多事没按我们的想法走，也许我们有些选择帮了倒忙，但我们还活着，这已经比外面有些人强了。"
        "试着把事情往好处想。\n[rrd](劳拉 信任 -1)":
            $ l_trust -=1
            "最好别把这事想得比实际更严重。总得有人把她从那个悬崖边拉回来。"
            j "不过我们没完蛋。事实上，考虑到我们经历过的东西，我们进展得还算不错。"
    scene c006_s006_008 with Dissolve(0.25)
    l "真的吗，[player_name]？卡莉伤得这么重，我们可能得在这儿再等上几天才能走。而且我们还能找到另一辆车的概率有多大？只能一路走到医院了。"
    l "你知道那有多疯狂吗？我们才走了不到两个街区，你我都开始感觉到暴露在外面的影响了。你也清楚我们经不起长时间暴露。"
    scene c006_s006_009 with Dissolve(0.25)
    l "我们没法就这么徒步穿过整座城。除非是嫌命长。或者一不留神，外面那些该死的东西就扑上来。"
    l "照这个速度——如果我们能活下来的话——我们几个月后才能到医院。到时候早就没人来救我们了。"
    j "那我们就继续走。往城外去。要是不够远的话——"
    scene c006_s006_010 with Dissolve(0.25)
    l "如果？我他妈，[player_name]，我不知道自己还能撑多久。"
    j "劳拉，你比自己以为的坚强。你不会放弃的。你还有想再见到的人。所以我懂，你累了，也受伤了，但别让那些破事钻进你心里。"
    scene c006_s006_011 with Dissolve(0.25)
    l "你他妈说得倒轻巧，你又不是一辈子都在外面跑、想同时兼顾家庭和事业、还觉得自己两头都做不好。而且就因为你是个臭婊子，你朋友也没几个。"
    l "我他妈到底在试着回去干什么？一个不爱我的丈夫？一个已经成人、还嫌他妈妈絮絮叨叨的儿子？"
    j "喂，喂，喂，劳拉。还有——"
    scene c006_s006_012 with hpunch
    l "住口！给我住口！别再试着把你自己都不信的东西说成道理！我不想再从你嘴里听到这种话了！"
    menu:
        "退开。":
            "是啊，她现在火气正旺，听不进道理。最好还是退开。"
        "等等……\n[rrd](劳拉 好感 -1)":
            $ l_friend -= 1
            j "喂，等等——"
    scene c006_s006_013 with hpunch
    l "他妈——！！操、操、{b}操{/b}！！！"
    "是啊……她……我该先让她一个人待会儿。说话解决不了问题。至少今晚不行。从这一切开始到现在我们已经聊了不少，但那不过是在给一条被砍断的肢体贴创可贴。"
    scene c006_s006_014 with Dissolve(0.25)
    "我能做的，就是把让我们能往前走的事情一件件做好。去给卡莉搜一件新外套和面罩，顺便弄点吃的喝的撑一阵子。看看能不能穿过一栋栋楼横穿校园。再看看有没有哪辆车留在外面还能开。"
    "我想，我给劳拉的那点分散注意力的东西根本不够。我不能怪她。她确实有一个要回去的生活，哪怕那生活烂成一团。"
    "天哪，真想喝一杯。或者来点什么。"
    scene c006_s006_015 with Dissolve(0.5)
    s "外面都还好吗？"
    "劳拉那一嗓子把雪莉引过来，一点也不奇怪。她对这群人的相处方式还不熟。"
    scene c006_s006_016 with Dissolve(0.25)
    j "对，它……"
    menu:
        "只是在发泄而已。":
            j "劳拉只是在发泄。明天早上就没事了。"
        "这几天够难熬的。\n[rgr](雪莉 信任 +1)":
            $ s_trust += 1
            j "这几天确实很难熬。你大概已经从卡莉那儿听说发生了什么。所以现在我们到了一个能喘口气的地方，她就把几句脏话撒出来了。如果她用这种方式来应对，那就随她吧。"
    scene c006_s006_017 with Dissolve(0.25)
    s "听起来她是想揍谁一顿。女人那样尖叫的时候，多半是要杀人了。"
    j "这话也可能没错，但眼下不是。她有家人还在外面，而她又拼命想知道他们是否安好，这更让人受不了。"
    scene c006_s006_018 with Dissolve(0.25)
    s "卡莉说她有个在UGA读书的哥哥，对吧？她说暑期他应该在学校里。那他运气真好，离这儿远远的。要是我聪明一点，可能就该待在家，秋季再想办法把这门课塞进去。要是这附近还会开课的话。"
    s "看来我得想办法把学分转过去。天哪，那我妈肯定高兴坏了。她会想把我弄去蒙茅斯或者蒙特克莱尔。呃……"
    j "蒙茅斯还是蒙特克莱尔？那是……"
    scene c006_s006_019 with Dissolve(0.25)
    s "新泽西。「花园之州」。其实更该叫「混凝土之园」。"
    scene c006_s006_020 with Dissolve(0.25)
    s "好了，我要回去了。刚才那场小型尖叫狂欢之前，我都快睡着了。"
    j "行行行。我保证尽量安静。"
    scene c006_s006_021 with Dissolve(0.25)
    s "谢了。"
    scene c006_s006_022 with Dissolve(0.25)
    "考虑到今天的开头，这样收尾也算不错了。至于劳拉……我只能让她睡一觉，希望她明天早上能在情绪上缓过来。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_30_818", transition=Dissolve(1.0))()
    pause
    $ Hide("june_30_818", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music morning fadein 2.0
    scene c006_s007_001 with Dissolve(2)
    "好吧。虽然我一点都不想这么做，但我确实得出去。连着三天往外跑，真是……唉。这活儿该拿危险津贴，不过回报是我们能多活一会儿。而且我真的得看看外面还有什么。"
    "我已经有足够时间弄清目前的食物情况了。还好水还能供应，但存粮不多，除了几个房间里藏着的些零食，这里几乎没什么能果腹的东西。"
    scene c006_s007_002 with Dissolve(0.25)
    "所以，但愿雪莉说的那些男生宿舍里还有能吃的东西。那得是我的第一站。也许也是唯一一站。这一切让我有点疲惫了。问题是我根本耗不起休息日。当吃饭和安全都成问题的时候，没有周末可言。"
    scene c006_s007_003 with Dissolve(0.25)
    if k_friend >= 10:
        k "喂、喂？是……{w=2}劳拉？[player_name]？"
    else:
        k "喂、喂？是……{w=2}劳拉？"
    j "我在这儿。这边。"
    scene c006_s007_004 with Dissolve(0.5)
    k "哦。你在这儿。我、我还想着……看起来……你又要出去？"
    j "对，我要去看看对面那栋男生宿舍。看看那边情况怎么样。也许能找点吃的、穿的。或者别的什么。"
    scene c006_s007_005 with Dissolve(0.25)
    if k_friend >= 10:
        k "*叹气* 你……你不该这么频繁地出去。你看起来……看起来很累。我不喜欢这样。"
        j "我很感激你的关心，我不会待太久，但这件事必须做。趁我们还在这儿，就得去搜刮东西。谁知道呢，说不定我还能再找到几把落在外面的车钥匙。"
    else:
        k "好。"
        j "我不会待太久，但这件事必须做。趁我们还在这儿，就得去搜刮东西。谁知道呢，说不定我还能再找到几把落在外面的车钥匙。"
    scene c006_s007_006 with Dissolve(0.25)
    k "我们没那么好命。*咯咯笑*"
    j "不过试试总没坏处。"
    scene c006_s007_007 with Dissolve(0.25)
    k "你介意吗？我得……"
    j "上厕所？当然，那我先出去。"
    scene c006_s007_008 with Dissolve(0.25)
    k "别……别走太远。我还有点虚。不过……当我没说。拜托。"
    menu:
        "你要是放屁，我可是会笑出来的。":
            scene c006_s007_009 with Dissolve(0.5)
            j "我可不敢保证你放屁的时候我不笑。"
            k "*呻吟* 天哪，太丢人了。"
        "我保证。\n[rgr](卡莉 好感\信任 +1)":
            $ k_friend +=1
            $ k_trust +=1
            scene c006_s007_009 with Dissolve(0.5)
            j "我保证——才怪，你离得远着呢。再说了，我真不知道你跑到那边干什么。女人从来不尿尿。"
            k "正是。"
    "也许我们该让她找回一点该有的谦逊。她最近已经够受的了。"
    scene c006_s007_010 with Dissolve(1)
    "我不愿去想这一切有多让她下不来台。受了伤，还得靠我们保证她不会再摔倒。洗澡的时候还得有人站在旁边。而她又那么迫切地想证明自己有用、想被人需要。"
    scene c006_s007_011 with Dissolve(0.5)
    k "我……我……"
    j "那么，你今天早上见过劳拉了吗？"
    k "还没有。你又想让她去看门？"
    menu:
        "对。[yl]":
            scene c006_s007_012 with Dissolve(0.5)
            j "对。我出去的时候，正好让她盯着门。"
            "就算卡莉听见了，最好也别跟她提昨晚的事。"
        "不止这个。[yl]":
            scene c006_s007_012 with Dissolve(0.5)
            j "不止这个。昨晚我们说话的时候，她情绪很激动。我觉得这一切真的开始把她磨得够呛，所以我就随她发了一通火、跺着脚走了。"
            k "那我应该就……"
            scene c006_s007_013 with Dissolve(0.25)
            j "你就留意着她点。我觉得她是真的铁了心要去医院、离开这儿。她一路都在硬撑，而接二连三的挫折实在把她压垮了。"
            k "好。我、我会看好她的。"
    scene c006_s007_014 with Dissolve(0.5)
    j "你的眼睛看起来在恢复了，没那么充血了。皮肤怎么样？"
    k "好多了吧。那个……呃……"
    scene c006_s007_015 with hpunch
    j "卡莉？"
    scene c006_s007_016 with Dissolve(0.25)
    k "对、对不起。仍、仍有眩晕。比之前好些了，但一……就发作的时候……"
    j "你站得太久了就会发作？"
    k "大概吧。"
    scene c006_s007_017 with Dissolve(0.25)
    s "哇，我是不是撞见什么不该看的了？抱歉。"
    scene c006_s007_018 with Dissolve(0.5)
    j "没有没有。我只是想扶卡莉站好。来，我扶你过来一点。长椅在……我右手边。你右手边。来。"
    k "我、我自己来。"
    scene c006_s007_019 with Dissolve(0.25)
    k "*叹气* 好，等我一下。我讨厌自己这么虚弱。"
    j "这是暂时的。好吧。养上几天，你就会恢复得跟没事人一样。"
    scene c006_s007_020 with Dissolve(0.5)
    k "但我感觉——"
    j "休息。认真的。你应得的。没有人会来衡量你出了几分力。这又不是上班。就算真是，操，那也无所谓。行了吧？"
    scene c006_s007_021 with Dissolve(0.25)
    k "好。谢谢。为了……"
    scene c006_s007_022 with Dissolve(0.25)
    s "你看起来又要出去？要我留下来陪她吗？卡莉？我可以啊。完全没问题。"
    j "最终还是要的。我得去找劳拉，让她也来门口轮班放哨。"
    scene c006_s007_023 with Dissolve(0.5)
    s "我可以留下来陪卡莉。我们现在算是好朋友了吧？就像新年第一天搬进新宿舍的室友那样。"
    k "差不多吧。*咯咯笑*"
    scene c006_s007_024 with Dissolve(0.25)
    "雪莉确实在往卡莉那边靠。这很合理：她俩年纪更近，而且在我们三个里卡莉更好说话。劳拉状态好的时候都是「冲劲十足」，而我自从到了这儿就进进出出的。再加上还有那档子事——她以为我可能是灼烧者。"
    "趁她在这儿，我该跟她打听打听男生宿舍的事。看看能不能对那边有点预期。"
    menu:
        "问吧。\n[rrd](雪莉 焦虑 +1)\n[grr]":
            $ s_anxiety +=1
            $ ch6_s_dormtalk = "yes"
            j "嘿，雪莉。我过去那边会遇到什么情况？是说男生宿舍。"
            scene c006_s007_025 with Dissolve(0.25)
            s "你、你是指什么？"
            j "布局跟这里一样吗？那边可能住了多少学生？诸如此类。"
            scene c006_s007_026 with Dissolve(0.25)
            s "呃，大多数宿舍都长得一样。至少校园这一片是这样。我想都是同一时期建的。"
            j "那楼层布局也一样了。"
            scene c006_s007_027 with Dissolve(0.25)
            s "对。那边还剩多少男的？我不知道。也许一个都没有。卡尔跟他那帮人跑过来了。雾来的第一天，有几个男的冲进雾里，尖叫得像在玩一样开心。怪胎。我猜他们最后跑掉了。或者……变成了灼烧者。"
            s "还剩多少？不知道。我倒记得他们提过，有个家伙把窗户开着。"
            j "所以那栋宿舍可能暴露在雾里？"
            scene c006_s007_028 with Dissolve(0.25)
            s "也许吧。"
            j "知道了很有用。我进去的时候会一直戴着面罩。谢谢。"
        "别。":
            "也许不会。雪莉大概不会告诉我什么是我自己搜十分钟就能查到的。再加上下午她那反应还历历在目。她现在可能没事，但我感觉这种状态既脆弱又暂时。"
    scene c006_s007_029 with Dissolve(0.5)
    k "我现在好多了。"
    j "好好，那就好。我得去找劳拉，趁早出发。你会没事的，对吧？"
    k "会的。"
    s "她交给我照顾。我帮人看过一次狗——我不是说你就是条狗——但照顾活物我在行。"
    scene c006_s007_030 with Dissolve(0.25)
    j "我觉得她不需要别的，只需要有人看着她别摔倒就行。"
    s "我、我能做到。"
    if k_friend >= 10:
        scene c006_s007_031 with Dissolve(0.25)
        k "小心点。拜托了。"
        j "我会的。回见。"
        scene c006_s007_032 with Dissolve(0.25)
        s "我们在这儿。"
        scene c006_s007_033 with Dissolve(1)
        s "你喜欢他，对吧？"
        k "我……呃……"
        scene c006_s007_034 with Dissolve(0.25)
        s "我可不是在评判。他……也算是个英雄吧？"
        k "…"
        scene c006_s007_035 with Dissolve(0.25)
        s "要是没人骑那匹马，我可就自己上鞍了。*咯咯笑*"
    else:
        scene c006_s007_032 with Dissolve(0.25)
        j "该走了。回见。"
        s "我们在这儿。"
        scene c006_s007_034 with Dissolve(1)
        s "靠。他还真算是个英雄，是吧？给他套身消防服，直接印到挂历上去得了。"
        k "…"
        scene c006_s007_035 with Dissolve(0.25)
        s "要是没人骑那匹马，我可就自己上鞍了。*咯咯笑*"
    scene blank with Dissolve(2)
    scene c006_s007_036 with Dissolve(2)
    "运气不错，我没花多久就找到了劳拉，她正在休息室等我。看她的脸色——那双布满血丝的眼睛和没睡好的人特有的苍白——我怀疑她心情并没有好转。会不会再来一次昨晚那样？我希望不会。"
    j "喂，你。"
    scene c006_s007_037 with Dissolve(0.25)
    l "我……昨天的事我们就忘了吧，行吗？我一直……*叹气*"
    j "你不用解释，我也不会再翻这笔旧账。雪莉在洗手间陪卡莉。我让她暂时照看一下卡莉。"
    scene c006_s007_038 with Dissolve(0.25)
    l "那就好。我不想把她一个人留着，既然要跟她共用一个空间，也只能信她了。你出去的时候要我顶门吗？"
    j "对。我要去另一栋宿舍翻翻。等我回来，我们可以聊聊我一直在琢磨的其他计划。不过，先弄到更多食物——以及其他能捡到的东西——才是第一优先。"
    scene c006_s007_039 with Dissolve(0.25)
    l "行，明白。"
    "我讨厌她声音里那股认输的调子，但我没心思再深究下去。尤其因为我并没有能让情况变好的办法。"
    scene blank with Dissolve(2)
    scene c006_s007_040 with Dissolve(2)
    l "你觉得要多久？我得知道什么时候该从「担心」升级成「非常担心」。"
    j "我不知道。一小时？我不想在里面待太久。走到入口并不远。不过要是我找到了什么东西，一小时可能就不够。"
    l "或者是碰上麻烦？"
    scene c006_s007_041 with Dissolve(0.25)
    j "更像是躲开麻烦。"
    l "你最好是。别搞什么英雄主义。这次是认真的。我不会在那边把你捞出来。还有，要是你在里面碰到人呢？我们是不是得做好有人跟着来的准备？"
    scene c006_s007_042 with Dissolve(0.25)
    j "*叹气* 这问题很难答，因为要看情况。要是只有一个呢？我也许能摸摸对方的底，但不告诉他我来自哪儿。"
    l "只要他们没从窗户看到你——因为我们可以做到——只要你离得够近。"
    j "*呻吟* 靠。"
    scene c006_s007_043 with Dissolve(0.25)
    l "听着，相信你的直觉。但也要明白，不是每个人都会把我们的利益放在心上。听雪莉说话的意思，那边有几个男的好像很快就有了一副「后启示录」的样子。抓住机会使劲捞，懂的都懂。"
    j "我知道。我本来希望灼烧者已经是我们最大的麻烦了。"
    scene c006_s007_044 with Dissolve(0.25)
    l "还不一定。要是你再找到一件武器——任何能改成武器的东西——都带上。拜托了。你在外面的时候，我手里没家伙，心里就没底。"
    j "会的。"
    l "还有，小心点。拜托。"
    j "知道了。会的。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c006_s007_045 with Dissolve(2)
    play music outsideday2 fadein 2.0
    "就算知道要去哪儿，也不是想走就走。雾让辨认地标几乎不可能。不过应该是这个方向。我只要小心点就行。"
    scene c006_s007_046 with Dissolve(0.5)
    "而且我发誓我听见了外面的动静。拖沓的脚步声在周围的混凝土间回荡。倒也不意外。我知道外面至少有一个。"
    scene blank with Dissolve(2)
    scene c006_s007_047 with Dissolve(2)
    "那段路走起来感觉比实际更长。对我是好事，我避开了所有遭遇。就这样保持下去。"
    scene c006_s007_048 with Dissolve(0.5)
    "希望这玩意儿没上锁。不然就得让我这把斧头跟你打个照面了。"
    scene blank with Dissolve(2)
    scene c006_s008_001 with Dissolve(2)
    "幸好没锁。这里又黑又安静。还好我想起来带了手电筒。"
    "这里必须格外小心。雪莉的叙述暗示男生们都离开了这栋楼，但这不代表我该把这里当成空屋。听动静。"
    "这里……好像有一层薄雾。要不是有光我可能都注意不到。雪莉确实说过有扇窗户一直开着。听这低低的嗡嗡声，我想空调可能还在运转，正把那玩意儿一点一点吸进屋里。"
    scene c006_s008_002 with Dissolve(0.25)
    if ch6_s_dormtalk == "yes":
        "再往里走走吧。雪莉说得没错。这儿基本上就是她那间宿舍的翻版。这样也好。至少楼层布局我心里有数了。"
    else:
        "再往里走走吧。这儿基本上就是那栋宿舍的翻版。这样也好。至少楼层布局我心里有数了。"
    scene c006_s008_003 with Dissolve(0.25)
    "好了，一间一间来，先从第一间开始。"
    scene blank with Dissolve(2)
    scene c006_s008_005 with Dissolve(2)
    "三间里有两间是空的。不意外。这间看起来主人还没完全收拾完。我翻翻看有没有带零食。"
    scene blank with Dissolve(2)
    scene c006_s008_006 with Dissolve(2)
    "好消息，坏消息。好消息呢？一盒烤芝士饼干和一瓶萘普生。坏消息呢？这家伙肯定不到五英尺高，因为他那些衣服我一件都穿不下。他的鞋是七号。"
    "继续往前走吧。我不该待太久，不然劳拉又要急躁起来，我不想再去刺激她了。"
    scene blank with Dissolve(2)
    scene c006_s008_004 with Dissolve(2)
    "剩下的房间里，除了有一间以外全空着。不过那间倒是提供了几件尺寸跟我更接近的衣服。我挑了几件塞进背包，继续往前走。"
    "有那么一会儿，我考虑要不要进洗手间看看，但决定还是算了。我想先去二楼，再多搜几间房，然后就得走了。"
    scene blank with Dissolve(2)
    scene c006_s008_007 with Dissolve(2)
    "我天，这上面的空气糟透了。肯定哪儿有扇开着的窗户。要不是我本来就在赶时间，这一下更是把我催死了。"
    "走廊尽头那扇门半开着。我敢打赌雾到处飘就是那间屋子造成的。这层楼一间一间搜吧，看看我能走到哪。"
    scene blank with Dissolve(2)
    scene c006_s008_008 with Dissolve(2)
    "又是些衣服。一盒麦片。没什么有用的。嗯……麦片还是有用处的，就算没有牛奶。"
    scene c006_s008_009 with Dissolve(0.25)
    "等等，还有一瓶詹姆森威士忌。有人以前不是个乖孩子。去他的，我拿走了。也许喝上一两口能让气氛好点。"
    scene c006_s008_010 with hpunch
    stop music
    "*咚* *哒-咚*"
    scene c006_s008_011
    "那是什么声音？像是有什么在动。在走廊里？还是在附近的房间里？"
    scene c006_s008_012 with Dissolve(0.5)
    "是谁？又一个学生？看看走廊这副样子，我心里不太妙。太像普罗维登斯生活楼的那个办公室了。但我也不能一直待在这儿。"
    scene blank with Dissolve(2)
    scene c006_s008_013 with Dissolve(2)
    play music horror fadein 2.0
    "好吧，这边什么都没有。暂时没有。除了满满的雾。那声音是从哪儿来的？我想是那边那头。"
    scene c006_s008_014 with Dissolve(0.25)
    "*咚*"
    "对，浑身上下都写满了「不」。你们这种家伙四处游荡的场面我见多了，你就是个灼烧者。我他妈这就走。"
    scene c006_s008_015 with Dissolve(0.25)
    "你他妈到底怎么进来的？跟普罗维登斯生活楼那个一样？我开始觉得我的推测有点道理了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c006_s009_001 with Dissolve(2)
    play music insidedark fadein 2.0
    k "我在这儿什么都看不见。"
    s "我也是这么想的。一楼的窗户确实不适合往外看。我知道，这很让人意外。要是上到三楼，也许会好些。你知道最好的地方该去哪儿吗？哈灵顿楼。我有一门工作室课的教室窗户正对着院子。我们能看见一切。"
    scene c006_s009_002 with Dissolve(0.25)
    s "嗯，「一切」得看雾有多糟。看不清东西确实一点帮助都没有。以前天气好的时候，我会在课上做作业，然后脑子就开始飘，接着就不自觉地开始观察别人。"
    s "而且你并不会真的意识到自己在干这个。只是看着别的学生从一个地方跑到另一个地方。看着男生一边套上连帽衫一边跑去上课。或者看着某个女生一边快走一边想办法同时应付她那杯早晨的拿铁和书本，好赶到校园另一边的课。"
    scene c006_s009_003 with Dissolve(0.25)
    s "然后莫林教授就走到我旁边，清了清嗓子，提醒我本来该在做点事。"
    scene c006_s009_004 with Dissolve(0.25)
    k "唔~~~~我讨厌这样。被困在这儿。一点用都没有。"
    s "哎呀，你又不是没用。不像我这个没用。*咯咯笑* 你只是需要休息一下，姑娘。把身体养好。我保证你很快就能跟以前一样生龙活虎。"
    scene c006_s009_005 with Dissolve(0.25)
    k "我要是真「生龙活虎」起来，你是知道那意味着什么的，对吧？"
    s "我……我知道。"
    scene blank with Dissolve(2)
    scene c006_s009_006 with Dissolve(2)
    l "谢天谢地。我……本来想说我开始有点担心了，但你走了以后我就一直紧张得不行。"
    j "我一直有留意自己待了多久。但没有手表很难算。我已经很久没戴表了，因为我拿手机当时钟。也曾经是。我进去，捡了些东西，没待太久。而且楼里有个灼烧者，所以我决定不逞英雄。"
    scene c006_s009_007 with Dissolve(0.25)
    l "在楼里？怎么回事？它找到办法进去了？我记得办公室那边也有过一个。是类似的情况吗？"
    j "我想是。雪莉顺口提过，说男生宿舍里有个家伙把窗户开着。结果二楼全是雾。靠，一楼更是一片鬼样。你绝对不会想摘下面罩。"
    j "所以我正在二楼翻找，听见了动静。走到走廊一看，就看到其中一个在尽头那间屋子里跌跌撞撞。我可没留下来重演早上那种靠把东西砸出窗户才勉强赢下来的战斗。"
    scene c006_s009_008 with Dissolve(0.25)
    l "那就好。就当那儿没别人了。"
    j "至少没有我们想带回来的人。我没看见尸体，不过空气那么差，那个灼烧者大概就是唯一活着的东西。我想三楼还可以再搜一搜，但我没什么信心。"
    scene c006_s009_009 with Dissolve(0.25)
    l "靠。有找到什么值得带的东西吗？"
    j "我没把每间房都搜遍。你可以想象，我得把时间砍掉一些。我确实拿了些零食和衣服。还有一点提神的东西。有人偷偷藏在自己房间的一瓶威士忌。"
    scene c006_s009_007 with Dissolve(0.25)
    l "哦？那不奇怪。我们要是在这儿多待一阵子，我完全预计还能找到更多东西。也许还有大麻。"
    j "抽一口、递一口，对吧？好了，我去冲个澡。我没被什么太严重的东西碰到，但老毛病的地方已经开始发痒了。"
    scene c006_s009_010 with Dissolve(0.25)
    l "走之前把背包放台面上。我想检查一下。"
    j "行行行。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_30_143", transition=Dissolve(1.0))()
    pause
    $ Hide("june_30_143", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain fadein 2.0
    scene c006_s009_011 with Dissolve(2)
    l "哎呀哎呀哎呀。看来你终于搞到了念叨已久的那身换洗衣服。有人焕然一新了啊。"
    j "我可不是为了好看。*轻笑* 我只是挑了几件希望穿得上、看着合适的。再加上它们是干净的。我记得以前上大学的时候——我们有时候确实不常洗衣服。"
    scene c006_s009_012 with Dissolve(0.25)
    l "那可不光是上大学才这样。"
    j "好吧，雪莉人呢？"
    scene c006_s009_013 with Dissolve(0.5)
    k "她……她回自己房间了。之前我们聊天的时候，我提到等我好到能自己走路了我们就得走，她好像不太高兴。"
    l "她难道没想过我们不会一直住在这儿吗？我们可是走进这栋宿舍楼的。"
    scene c006_s009_014 with Dissolve(0.25)
    j "她可能还停留在「会有人来救她」这个念头上。她可能根本没想那么远。有些人在灾难面前就是反应不过来。"
    scene c006_s009_015 with Dissolve(0.5)
    l "卡莉，她到了这儿以后，有没有说过自己原本打算怎么办？我还没机会单独跟她说上几句话。毕竟我们刚出现的时候冲她吼过。"
    k "没、没有吧。我、我承认自己有点分心。我记得在到这儿之前我跟她说过我们要去医院。她总该知道计划是这样的。"
    j "也许我们该把话说清楚：我们要离开这座城，而医院大概是我们逃出去的最佳机会。"
    scene c006_s009_016 with Dissolve(0.25)
    "理论上是这样。不过这个计划里掺了太多「奢望」。尤其是到现在为止，我们连一点迹象都没看到，说明这座城还有人关注。"
    k "那要是她不想走呢？她虽然没明说，但我感觉她躲在这儿躲得挺自在。"
    menu:
        "我们得说服她不是这样。":
            j "我们得说服她不是这样。坐下来好好谈一次，把情况明明白白告诉她。我们不能就这么把她留下。到现在这个地步，那基本等于判她死刑。"
            scene c006_s009_017 with Dissolve(0.25)
            l "食物来源就那么点，我们走了之后她也撑不了多久。我明白她害怕——老天爷，理由多着呢——但我们不能就这么把她留下。"
        "那是她自己的选择。\n[rrd](劳拉 信任 -1)":
            $ l_trust -= 1
            j "可惜，这还是得她自己决定。"
            scene c006_s009_018 with Dissolve(0.25)
            l "[player_name]！真是的。我不喜欢强迫她这个做法，但你比我更清楚。食物来源就那么点，我们走了之后她也撑不了多久。我明白她害怕——老天爷，理由多着呢——但我们不能就这么把她留下。"
    scene c006_s009_019 with Dissolve(0.5)
    k "我……我会跟她谈谈的。这事大概该由我来做。我先看看她是怎么想的。也许能劝她跟我们一起走。"
    l "她得明白，这里不会越变越……"
    scene c006_s009_020 with Dissolve(0.25)
    j "劳拉。卡莉知道。"
    scene c006_s009_021 with Dissolve(0.25)
    l "抱歉。我就是……算了。"
    scene c006_s009_022 with Dissolve(1)
    k "你在男生宿舍有没有看到什么有意思的？我出来的时候劳拉在翻背包。我看到一些零食。看起来你还找到了些衣服。"
    j "看来你提过二楼那个灼烧者了？"
    l "提了。也说了你决定在它发现你之前撤出来。"
    scene c006_s009_023 with Dissolve(0.25)
    k "那是不是意味着你不会再回去了。"
    j "不会马上回去。我没来得及把那地方搜完，不过既然我们不打算在这儿待很久……"
    scene c006_s009_024 with Dissolve(0.25)
    l "「在这儿待很久」？"
    j "外套。出去穿的衣服。*叹气* 我还得找件东西替代你丢的那件。还得看看雪莉有没有她自己能穿的。还有手套、帽子、面罩。"
    scene c006_s009_025 with Dissolve(0.25)
    j "操。看来我确实得回去一趟。或者看看步行范围内还有别的什么选择。"
    l "现在不行。不过我们该商量一下打算怎么做。至少得知道我们在朝什么目标努力。"
    scene c006_s009_026 with Dissolve(0.25)
    j "我不指望附近能找到车。就算找到，能用的也难说。我在想之前雪莉说的那件事——有群人决定走进教学楼群，试着从一栋楼挪到另一栋楼地穿过校园。"
    j "我不知道这条路可不可行，但它能把我们待在外面的时间压到最少。我本来打算明天去查看一下附近那栋楼，看看那边情况怎么样。"
    l "你觉得这事有多容易？你提的那个办法。我不是在这儿念的书，所以校园我不太熟。"
    scene c006_s009_027 with Dissolve(0.25)
    j "我是跟南希搬来这儿之前就毕业了。我念的是北卡州立。卡莉？"
    k "网课。抱歉。安德鲁调过来的时候，我除了报网课别无选择。我只填过表格、只通过邮件跟教授联系过。"
    scene c006_s009_028 with Dissolve(0.25)
    l "所以我们要在这儿认路，可能得靠雪莉帮忙。"
    j "听上去是这样。不过首先我得先侦查一下。至少要确认这个计划到底有没有一丁点可行性。我可不想过去以后发现窗户都碎了，或者有扇门大敞着。"
    scene c006_s009_029 with Dissolve(0.25)
    l "那可真是我们的运气了，对吧？"
    "我们这场小小的会议给了每个人各自要盯的事：踩点附近那栋教学楼。给卡莉和雪莉弄装备。说服雪莉她必须跟我们一起走。我敢肯定还有不少我当场根本没考虑到的。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_30_836", transition=Dissolve(1.0))()
    pause
    $ Hide("june_30_836", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c006_s010_001 with Dissolve(2)
    play music lauratheme fadein 2.0
    "我承认我当时就想先去隔壁那栋楼瞄一眼，但太阳一落山，我那点理智的谨慎就冒出来了，提醒我在黑暗里于陌生地盘乱走纯粹是在自找麻烦。所以我决定先忍到早上。"
    scene blank with Dissolve(2)
    scene c006_s010_002 with Dissolve(2)
    "我在宿舍楼里转悠了一会儿，挨个往其他房间里瞄，想看看第一遍搜寻有没有漏掉什么。"
    scene c006_s010_003 with Dissolve(0.25)
    "虽然我有一部分念头想去找雪莉谈谈，但我压住了这个冲动。看她们俩相处的样子，让卡莉继续经营这段关系才是对的。"
    "我确实觉得她最初对我的恐惧已经消了，但我不想去挑战运气，尤其在我们还得说服她跟我们走的情况下。"
    scene c006_s010_004 with Dissolve(0.25)
    "我敲了卡莉的门，想看看她想不想聊聊。她没应门，我便把这归为她睡着了，或者只是想一个人待会儿。我敢肯定，操持跟雪莉的关系耗光了她那点可怜的社交电量。"
    scene c006_s010_005 with Dissolve(1)
    "至于劳拉，我在休息室找到她，看起来情绪糟透了。过去几天发生的事摆在那儿，我敢肯定她在脑子里钻得太深了。我该看看她是不是只是需要一个朋友。"
    scene c006_s010_006 with Dissolve(0.25)
    j "嘿，那边那位。你还好吗？我知道答案大概是否定的，但我还是得问一句。"
    scene c006_s010_007 with Dissolve(0.25)
    l "啊，[player_name]……*叹气* 是啊。我想我一直都……"
    menu:
        "想得太多了点？[yl]":
            j "想得太多了点？大概吧。"
        "对自己太严苛了点？[yl]":
            j "对自己太严苛了点？大概吧。"
    scene c006_s010_008 with Dissolve(0.5)
    l "想不这样都难。我……我太习惯于一直「去做」「去干」了，现在什么都做不了，简直要命。几十年的习惯不可能一下子改掉。老实说，我们连走两条街都免不了受伤。"
    scene c006_s010_009 with Dissolve(0.25)
    l "而且连听一听我爱的人是否平安都做不到？这是折磨。我真需要点东西让神经松一松。所以……"
    j "你盯着那瓶詹姆森看呢？我过来的时候，它就被你摆在了旁边。"
    scene c006_s010_010 with Dissolve(0.25)
    l "我不该喝的。但，没错，我在看。"
    j "今晚你要是想喝点麻的，我陪你。我自己也正好想放松一下。"
    scene c006_s010_011 with Dissolve(0.25)
    l "这话我同意。咱俩最近身心上都挨了不少打。"
    j "这么安排，合你意吧？"
    scene c006_s010_012 with Dissolve(0.25)
    l "我倒不是排斥烈酒，不过我自己更偏啤酒。"
    scene c006_s010_013 with vpunch
    l "嘶溜噗~~~ 唔~~~"
    "靠，姑娘。一口闷。我该找几个小酒杯才对。"
    scene c006_s010_014 with Dissolve(0.25)
    l "唔~~~不是我平常爱喝的，不过也还行。有点辣。"
    j "反正能让我缓一缓就够了，对吧？"
    scene c006_s010_015 with Dissolve(0.25)
    l "也不一定。我喝过能把家具清漆都泡下来的土酒。那种东西一进嘴你就后悔。这瓶好歹是有人花钱、让大人从酒铺买回来的。"
    j "当然得给你最好的。拿来。"
    scene c006_s010_016 with vpunch
    j "*咕咚*"
    "烧得还挺舒坦。不是我喝过最烈的酒，但今晚够用了。"
    scene c006_s010_017 with Dissolve(0.25)
    j "啊~~~那，你觉得雪莉怎么样？"
    l "她确实是个大学生。*咯咯笑* 我都忘了那个年纪有多{i}轻浮毛躁{/i}。又或者，我从来就不是那样。她人不坏，但感觉在「疯癫小精灵」和「受惊的小奶狗」之间来回横跳。"
    j "那算是大学生的样子，还是因为别的？我们所有人都压力很大。"
    scene c006_s010_018 with Dissolve(0.25)
    l "不管怎样，她不坏。而且她和卡莉好像处得来。我猜年纪更接近这一点帮了忙。你觉得她呢？"
    menu:
        "她不再觉得我是怪物了……[yl]":
            j "她不再觉得我是怪物了，那我就知足了。"
        "我有点受不了她。[yl]":
            j "她对我来说有点太过了。我受不了那么高的能量。"
        "她和卡莉好像挺合得来。[yl]":
            j "她和卡莉好像挺合得来，那我就放心了。她现在主动站出来帮卡莉，这说明她人不错。"
    scene c006_s010_019 with Dissolve(0.25)
    l "嗯哼。"
    scene c006_s010_061 with hpunch
    l "嘶溜噗~~~~ *咕咚*"
    "这是第几杯了？我们喝得比我预想的猛多了。"
    scene c006_s010_062 with vpunch
    j "*咕咚* 嘶~~~"
    scene c006_s010_063 with Dissolve(0.25)
    j "看来你也弄到了新衣服。"
    l "是啊，不过还行。暂时能穿。年轻姑娘身材又好，为夏天准备的衣服实在太多了。"
    menu:
        "啊，你穿这个挺好看的。\n[rgr](劳拉 好感 +1)":
            $ l_friend +=1
            j "啊，你穿这个挺好看的。这个颜色很衬你。"
            scene c006_s010_064 with Dissolve(0.25)
            l "谢了。"
        "你身材够辣的。\n[rgr](劳拉 欲望 +1)\n[grr]":
            $ l_desire +=1
            j "得了吧。你也有。"
            scene c006_s010_064 with Dissolve(0.25)
            l "这话可不合适啊，[player_name]。"
            if l_sex >= 1:
                j "底下什么样我都见过了。我心里有数。*轻笑*"
    scene c006_s010_020 with hpunch
    l "*咕咚* 嘶溜噗~~~ 唔~~~"
    scene c006_s010_021 with Dissolve(0.25)
    l "*叹气* 我们到底有多惨，[player_name]？那辆Bronco本来是我们唯一的希望，开着它就能直接奔向自由。结果我们连校园都没到，医院就更别提了。我们还能找到别的出路吗？"
    scene c006_s010_022 with Dissolve(0.25)
    j "劳拉，人类既有机变又有疯劲。我们总能想到办法熬过去。你看那些{a=https://www.nasa.gov/missions/apollo/apollo-13-mission-details/}阿波罗13号{/a}的宇航员。他们本来要去月球，结果装备出了故障，只好把一些根本不该那么拼的东西硬拼起来，才回家。"
    j "所以，只要得用非常规手段回家，我们就会用。"
    scene c006_s010_023 with Dissolve(0.25)
    l "要是我们到了医院，他们已经不再撤离人了呢？"
    j "那我们就继续往外走。开——或者走——出城。要是蔓延得比那更广，我们就接着走。只要我们还活着、还在一起，就不停止前进。"
    scene blank with Dissolve(2)
    if ch5_laura_sex == "no":
        scene c006_s010_065 with Dissolve(2)
        "灌了几轮之后——那瓶酒被我们喝掉了不少——我和劳拉都感觉飘飘忽忽、麻麻的。她大概比我醉得还厉害一点。"
        scene c006_s010_066 with Dissolve(0.5)
        "我觉得差不多该到此为止了，就站起来，打算把酒挪个地方。为了不再受诱惑。"
        scene c006_s010_067 with Dissolve(0.5)
        "当然，我的平衡力早就输给了血液里的酒精浓度。我觉得自己应该能踉踉跄跄走回床上，不至于出太大问题。"
        scene c006_s010_068 with Dissolve(0.5)
        "可劳拉呢？她一个字都没说就睡着了。我才刚转过身，她就已经没影了。"
        j "靠，姑娘。"
        scene c006_s010_069 with Dissolve(0.5)
        "尽管我自己也摇摇晃晃，还是决定试着把她挪到比瘫在沙发上更舒服的地方。"
        scene blank with Dissolve(2)
        scene c006_s010_070 with Dissolve(2)
        "不用多说，那是一段小小的冒险，但我确实把她安顿睡了。现在得给我自己找个平躺的地方，因为我天，我开始迅速断片了。"
    else:
        scene c006_s010_024 with Dissolve(2)
        "灌了几轮之后——那瓶酒被我们喝掉了不少——我和劳拉都感觉飘飘忽忽、麻麻的。也许还有点傻乎乎的。酒加大学宿舍，简直能把两个成年人打回最幼稚的原形。"
        menu:
            "再来一轮，玩得开心点。\n[rgr](劳拉 爱意\欲望 +1)\n[pks]":
                $ l_love += 1
                $ ch6_laura_sex = "yes"
                $ l_desire += 1
                call ch6_laura_sex from _call_ch6_laura_sex
            "该收场睡觉了。":
                scene blank with Dissolve(2)
                scene c006_s010_065 with Dissolve(2)
                "最好到此打住，免得我们俩明天早上都抱着马桶吐、然后顶着宿醉醒来。"
                scene c006_s010_066 with Dissolve(0.5)
                "在半醉的迷糊劲儿里，我觉得差不多该到此为止了，就站起来，打算把酒挪个地方。为了不再受诱惑。"
                scene c006_s010_067 with Dissolve(0.5)
                "当然，我的平衡力早就输给了血液里的酒精浓度。我觉得自己应该能踉踉跄跄走回床上，不至于出太大问题。"
                scene c006_s010_068 with Dissolve(0.5)
                "可劳拉呢？她一个字都没说就睡着了。我才刚转过身，她就已经没影了。"
                j "靠，姑娘。"
                scene c006_s010_069 with Dissolve(0.5)
                "尽管我自己也摇摇晃晃，还是决定试着把她挪到比瘫在沙发上更舒服的地方。"
                scene blank with Dissolve(2)
                scene c006_s010_070 with Dissolve(2)
                "不用多说，那是一段小小的冒险，但我确实把她安顿睡了。虽然我很想顺着那股冲动行事，但还是决定不要爬到她旁边去。"
                "现在得给我自己找个平躺的地方，因为我天，我开始迅速断片了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c006_s011_001 with Dissolve(2)
    play music nightmain2 fadein 2.0
    $ renpy.pause ()
    scene c006_s011_002 with Dissolve(0.5)
    k "唔嗯~~~ 啊呃~~~"
    scene c006_s011_003 with Dissolve(0.5)
    k "我、我在……呃~~~"
    scene c006_s011_004 with Dissolve(0.5)
    k "好、好吧……宿舍……"
    "{color=#ffcccc}噩梦。糟糕的噩梦。然后我醒了，有一瞬间不知道自己在哪儿。但我是在宿舍里。我们两天前到的这儿。{/color}"
    "{color=#ffcccc}就我一个人。劳拉呢？我……我想她睡在别的地方了吧。[player_name]也是。我……{/color}"
    scene c006_s011_005 with Dissolve(0.25)
    k "*抽鼻子* *抽鼻子*"
    "{color=#ffcccc}我好累。累得疼。累得怕。累得做噩梦。可这些噩梦里没有那些怪物。也没有死亡。{/color}"
    scene c006_s011_006 with Dissolve(0.25)
    "{color=#ffcccc}梦的是回去。回到……从前的样子。被困在一个不属于我的人生里。它曾经属于过我吗？{/color}"
    k "*叹气*"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_1_904", transition=Dissolve(1.0))()
    pause
    $ Hide("july_1_904", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music morning fadein 2.0
    scene c006_s011_024 with Dissolve(2)
    j "呃呕……"
    scene c006_s011_025 with Dissolve(0.5)
    "我想我还能更糟。可能是多喝了一两杯。一杯够劲的咖啡就能解决。在食物这么有限、我们又没吃够的情况下跑去喝酒，大概不是什么好主意。"
    "还好我们还有自来水，虽然不知道能撑多久。"
    scene c006_s011_026 with Dissolve(0.25)
    "劳拉多喝了点，真可惜。她今天大概会难受得要命。这很扫兴，因为昨晚是我这么久以来第一次看到她接近快乐。"
    "我觉得这种喝法不能太频繁。至少在弄到更多酒之前不行。"
    scene c006_s011_027 with Dissolve(0.5)
    "该去弄杯急需的咖啡了。也许再探头看一眼，确认劳拉还活着。"
    scene blank with Dissolve(2)
    scene c006_s011_007 with Dissolve(2)
    "{color=#ffcccc}这一晚很难熬。我不知道自己有没有连续睡上二十分钟。不过我不该抱怨。这张床仍然是这一切开始以来我睡过最好的地方。{/color}"
    scene c006_s011_008 with Dissolve(0.25)
    "{color=#ffcccc}来，让我看看。视力差不多恢复正常了。边缘还有一点模糊，但看起来最严重的刺激已经消了。{/color}"
    scene c006_s011_009 with Dissolve(0.25)
    "{color=#ffcccc}脸也好多了。之前那些担心自己毁了容的焦虑，也许是我反应过度了。虽然那份担心并非没道理，但我还是为自己当时的表现感到有点傻。{/color}"
    "{color=#ffcccc}不过，[player_name]对我很温柔。他没有因为我受伤又害怕，就把我当成一个愚蠢又娇气的小孩。{/color}"
    scene c006_s011_010 with Dissolve(0.25)
    l "呃……靠……"
    k "劳拉？"
    l "唔嗯~~~ 抱歉，得……"
    scene c006_s011_011 with Dissolve(0.5)
    l "哦天哪，昨晚喝太多了。"
    k "劳拉？你没事吧？"
    scene c006_s011_012 with Dissolve(0.25)
    l "我想不是。得……"
    scene c006_s011_013 with Dissolve(0.25)
    k "咦？噢！呃……"
    l "*呕* 呃~~~ 呼~~~ 哈~~~"
    scene c006_s011_014 with Dissolve(0.25)
    "{color=#ffcccc}别听别听别听。她没在吐。没在吐。没在吐。{/color}"
    scene c006_s011_015 with Dissolve(0.5)
    l "哦操我~~~ *喘气* *喘气*"
    k "你……你还活着吗？"
    scene c006_s011_016 with Dissolve(0.25)
    l "只要我肚子里的东西没跑到外面来，*喘气* 还活着。"
    k "你生病了吗？"
    l "昨晚我和[player_name]喝了酒，*喘气* 喝太多了。我不是喝烈酒的人。至少不该喝那么多。"
    scene c006_s011_017 with Dissolve(0.25)
    l "肚子里没东西垫着，扛不住。"
    k "你喝了多少？"
    scene c006_s011_018 with Dissolve(0.25)
    l "哈啊~~~~ 太多了。我不知道。我在沙发上昏过去了，多到直接断片。宿醉要命得要死。我觉得我想死。"
    scene c006_s011_019 with Dissolve(0.25)
    k "需要我给你拿点什么吗？"
    scene c006_s011_020 with Dissolve(0.25)
    l "*喘气* 水、咖啡、止痛药，再加一根早餐棒，任何组合都太棒了。另外，我觉得我该回床上了。我……"
    scene c006_s011_021 with Dissolve(0.5)
    l "靠，我不行。如果[player_name]要去查看那个——"
    scene c006_s011_022 with Dissolve(0.25)
    k "我可以帮他。我有这个能力。我头已经好多了。你不用把我当成玻璃做的。"
    l "卡莉，我们不让你去，不是因为觉得你干不了这活儿。是因为我们想保护自己的人。你也听见过我怎么数落[player_name]。我就是不想让他再受伤。他犟得跟头猪一样，根本不肯听我的。"
    scene c006_s011_023 with Dissolve(0.25)
    k "那……让我来帮你。行吗？来，我先把你扶回床上，再去给你拿那些东西。"
    l "*叹气* 好好好。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c006_s012_001 with Dissolve(2)
    play music insideday fadein 2.0
    "靠，这大概不是我喝过最好的一杯咖啡，但也够了。它帮我把最后一点宿醉的余韵甩掉了。我本来打算洗漱一下，但听见里面有人在说话，就觉得最好把空间留给他们；而且我也不想为了讲点体面，就在厨房水槽边上凑合洗。"
    scene c006_s012_002 with Dissolve(0.25)
    "过去几天我们都过分地闯进了彼此的私人空间。我敢肯定卡莉对「必须让我站在旁边才能洗澡」这件事尴尬得要死。所以也许，我可以把这个早晨的浴室让给她们。"
    "另外，我本来打算去哈灵顿楼探探路。不知道那边空气怎么样，所以我不知道自己回来以后需不需要先洗漱一下。"
    scene c006_s012_003 with Dissolve(0.25)
    "走之前，我得先去看看劳拉，确认她熬过了昨晚那顿酒。再看看卡莉。她摔伤已经两天了。我希望她头好点了。"
    "也许还得找个人在宿舍和连廊之间那扇后门放哨。"
    scene c006_s012_004 with Dissolve(0.5)
    s "呃，早上好。"
    j "哦，嗨，雪莉。早上好。我在冲咖啡。你要来一杯吗？"
    scene c006_s012_005 with Dissolve(0.25)
    s "不了不了，我不爱喝。除非你打算往里加足够多的糖和牛奶，让它彻底变成别的东西。"
    j "*轻笑* 好。我很确定我们没有牛奶，所以那就不成了。"
    s "我就知道。雾来之前我没想着去趟超市，现在真是后悔。"
    scene c006_s012_006 with Dissolve(0.5)
    s "嘿，我……我想为我前几天的反应道个歉。我……我不该锁上门不让你们进来。那时候我不知道你们当中有人受了伤。"
    menu:
        "你那样做是对的。\n[rgr](雪莉 焦虑 -1)":
            $ s_anxiety -=1
            j "从务实的角度看，你那样做是对的。你孤身一人，也不认识我们。我们完全可能是麻烦。或者更糟。当然，我们是在逃命，卡莉也需要进屋，但我能理解你为什么那么做。"
        "我看起来是挺吓人的。\n[rgr](雪莉 好感 +1)":
            $ s_friend += 1
            j "我看起来是挺吓人的，哪怕没穿那些装备也是。而且说得委婉点，劳拉当时心情可不太好，所以没开门也许是个合理的本能反应。"
    scene c006_s012_007 with Dissolve(0.25)
    s "谢谢，但我还是为自己当时的反应感到愧疚。"
    j "我们都在慢慢摸索自己在危机里会怎么做。现在最重要的是我们都在这儿，都在恢复，同时为下一步做准备。"
    scene c006_s012_008 with Dissolve(0.25)
    s "只是……我看见男生们在外面到处跑，接着那些灼烧者就出现了，然后另一栋宿舍的男生也跑过来，跟布丽她们一起走了……感觉这世界本该有的样子……坏掉了。"
    s "我知道大学就是这种「自己搞定自己」的疯狂阶段，但雾一来，事情真的变得又怪又失控。就好像规则凭空消失了一样。我没跟他们走，是因为我总觉得可能会发生什么坏事，而那坏事不会是雾造成的，也不会是灼烧者造成的。"
    j "我讨厌这种想法可能是对的，但有时候你只能相信自己的直觉。希望真的什么都没发生。"
    scene c006_s012_009 with Dissolve(0.25)
    s "我……卡莉说你去了男生宿舍？你看到什么了吗？还有人在吗？"
    menu:
        "没什么。只有雾。":
            "也许我得斟酌一下怎么回雪莉。她给我的感觉是还承受不了某些残酷的真相。至少现在还不行。"
            j "没什么。只有雾。我记得有扇窗户开着。我找到了几样东西，不过因为我答应过不会待太久，就早点回来了。"
            scene c006_s012_010 with Dissolve(0.25)
            s "哦，呃……那看来大家都已经走了。"
            j "那我就当是吧，虽然我还没上到三楼。"
        "除了一个灼烧者，没别人。\n[rrd](雪莉 焦虑 +1)":
            $ s_anxiety +=1
            j "一堆雾，除了一个灼烧者没别人。看到它以后我没多待。"
            scene c006_s012_011 with Dissolve(0.25)
            s "它、它是怎么进去的？哦靠。"
            j "这不是我第一次在楼里遇到灼烧者。"
            scene c006_s012_012 with Dissolve(0.25)
            s "你觉得会是我说的那样，有人待在雾里太久了吗？"
            j "我没有足够的证据支撑，但这不算最糟的推测。"
            "考虑到她从我们到这儿开始就一直心神不宁，这大概不是个适合深聊的话题。老实说，可能在我们出现之前她就已经这样了。我确实得记住，我们遇到的每个人心里都有一套自己熬到今天的故事。"
    scene c006_s012_013 with Dissolve(0.5)
    s "你要回去吗？"
    j "今天不。东西迟早得去找，但今天我打算去隔壁那栋楼瞄一眼——"
    scene c006_s012_014 with Dissolve(0.25)
    s "哈灵顿楼。"
    j "对，就是它。既然我不指望外面还能再停着一辆能用的车，就得想个办法，让我们用最小的危险穿过校园。所以我想先进隔壁那栋楼看看情况。你能告诉我该有个什么心理准备吗？比如楼层图或者路线？"
    scene c006_s012_015 with Dissolve(0.25)
    s "我不知道。我不太擅长记路之类的。我就是凭感觉{b}走{/b}，走着走着就到了。我知道自己工作室教室在哪儿，但那只是因为过去两年我去得很多。多数时候我就是跟熟人一起上课，事先跟他们约好。"
    j "好吧……如果我去隔壁，我这一路不撞上锁死的门、也不用被迫走到外面去的概率有多大？"
    scene c006_s012_016 with Dissolve(0.25)
    s "你……你不该去。谁知道那边什么样。布丽她们就是往那边走的，之后我一直没听到她们的消息。也不能说完全没有。第一天我听到过一些喊叫，但之后就再没有了。"
    j "你那些朋友很可能已经走了。我想看看我们能不能跟上她们。"
    scene c006_s012_017 with Dissolve(0.25)
    s "跟上她们？我知道卡莉提过要去医院。你觉得从这儿能走到那儿吗？"
    j "值得一试。反正我们也不打算在这儿干等着谁来。"
    "雪莉看起来对此不太高兴。现在正是展开这个话题的好时机。"
    scene c006_s012_018 with Dissolve(0.5)
    k "早啊。"
    s "哦，嗨，姑娘。"
    "算了。雪莉的注意力只有仓鼠那么长，卡莉一走过来，这个时机多半已经没了。"
    scene c006_s012_019 with Dissolve(0.25)
    j "早，卡莉。"
    s "刚才我听见有人在厕所里难受得不行。你没事吧？"
    k "不是我。劳拉不太舒服。我扶她回床上，让她睡一觉醒酒。我们有治头疼的东西吗？"
    scene c006_s012_020 with Dissolve(0.25)
    j "我前几天好像找到了一些萘普生。还有水。我们昨晚可能确实多喝了几杯。所以她宿醉也说得通。"
    k "不止这样。她当时在厕所里，往马桶里吐。"
    s "哦~~~那从来都不好受。"
    scene c006_s012_021 with Dissolve(0.25)
    k "而且……我向来不擅长读人、不擅长看情绪，但我觉得她状态并不好。她看起来很低落。很消沉。也许只是累了、身体不舒服，但感觉又不止是这样。"
    j "我觉得她只是压力太大，被这一切磨得精疲力尽。她有家人，她拼命想知道他们的消息。"
    "我不确定卡莉知道多少，但雪莉在的时候，我不想把劳拉和基思之间的私事拿出来说。"
    scene c006_s012_022 with Dissolve(0.5)
    k "你今天还打算出去吗？"
    j "不算吧。我打算去隔壁那栋楼踩点，看看情况。也许能从那儿看清我们周围的地形，看看能不能跟校园里其他几栋楼连通。顺便看看有没有什么对我们有用的东西被落下了。"
    scene c006_s012_023 with Dissolve(0.25)
    k "好、好吧，你要我看着门吗？劳拉还病着……"
    s "我可以照看她。你要是担心她的话。我、我比起守在门口更愿意干这个。尤其是通往哈灵顿楼的那扇门。谁知道那边在搞什么。"
    menu:
        "你不用。\n[rgr](雪莉 好感 +1)":
            $ s_friend += 1
            j "你不用。我不会待太久，也不觉得会出事。"
            "有点是善意的谎言，但这种白色谎言是为了让人安心。"
            scene c006_s012_024 with Dissolve(0.25)
            k "至少得有人在后面给你锁门。我觉得这样我们都会觉得安全一点。"
            j "那就这么办。"
        "那样最好。\n[rrd](雪莉 焦虑 +1)":
            $ s_anxiety += 1
            j "要是有个人在我身后锁上门，那最好不过。以防万一。"
            scene c006_s012_024 with Dissolve(0.25)
            k "你觉得会有麻烦吗？"
            j "到了这个地步，我什么都不想当然。"
            scene c006_s012_025 with Dissolve(0.25)
            k "*叹气* 说得也是。"
    scene c006_s012_027 with Dissolve(0.5)
    k "你打算多久走？"
    j "还没。慢慢来。听起来你一大早就起来处理一堆事了。想喝咖啡、想洗澡就去吧。尽量慢慢进入今天的状态。我去装备一下，走之前先去看一眼劳拉。"
    scene c006_s012_028 with Dissolve(0.25)
    k "好、好吧。大概给我三十来分钟。"
    j "行，那我到后门等你。"
    scene blank with Dissolve(2)
    scene c006_s012_029 with Dissolve(2)
    "穿好大部分装备后，我去看了一眼劳拉，她已经又睡着了。我不想吵醒她——因为我知道不管舒不舒服她都会硬撑——所以我放轻了动作。"
    "要是早知道她酒量不行，我可能早就把瓶子收走了。但看起来我们那晚只是聊得挺开心。而且我自己大概也喝多了一点。"
    scene c006_s012_030 with Dissolve(0.25)
    if ch6_laura_sex == "yes":
        "当然，后来我们俩闹到一块儿去的时候，我脑子已经不是清醒的了，不管我喝了多少。要不是我们本来就暧昧，那事就不会发生。我只能希望她对发生过的事毫无印象，因为我知道这只会让她处理自己那段失败的婚姻更难。"
        "而且，不管我有多喜欢她，我不是想把事情弄得更糟。眼下我得真的退一步。我们那样亲密下去肯定对她没好处。就算我愿意往好的方向想。"
    "她现在动不了，我今天就得格外小心。要是有任何看着不对劲的地方，我就得立刻撤退。我讨厌自己这么想，但心底里我还是把劳拉看得跟我更对等。"
    "是啊，卡莉想帮忙，用她自己的方式也确实帮上了，但她纤细的身板加上刚受的伤，让我不太想在事情演变成动手的时候依赖她。"
    scene c006_s012_031 with Dissolve(0.25)
    "之前在餐馆外面看到那个灼烧者时，她也是当场僵住了。我不想在我正需要有人把门在身后摔上的当口，再来一次那种情况。"
    "至于雪莉？我还就是信不过她。我不知道真到了乱成一锅粥的时候，我能不能指望她。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c006_s012_032 with Dissolve(2)
    play music school fadein 2.0
    "等卡莉来的时候，我把门口堆的家具挪开了。她没过多久就到了。她走动的样子让我相信她的脑震荡已经消退了。"
    scene c006_s012_033 with Dissolve(0.25)
    k "劳拉怎么样？你去看过她了，对吧？"
    j "那会儿她睡着了，我不想叫醒她。她确实该休息，哪怕这不是休息的好方式。昨晚喝醉听起来像个不错的计划。今天？不太行，不过这也正常。"
    scene c006_s012_034 with Dissolve(0.25)
    k "我怕她撑不了多久。她压力真的很大，而困在这儿对她一点好处都没有。她说，她和她丈夫之间……情况很糟。"
    j "她也跟你说了？那就说得通了。她大概是需要一个能理解她的人倾诉。也就是从一个女人的角度听听说法。又不是你那小子在外面乱搞。"
    scene c006_s012_035 with Dissolve(0.25)
    k "…"
    j "好，我这就进去看看。"
    scene c006_s012_036 with Dissolve(0.25)
    k "你知道该往哪儿走吗？"
    j "不太知道，而且雪莉给的细节也没什么用。所以我就走一步看一步，能走多远算多远，回头再说。"
    if k_friend >= 10:
        scene c006_s012_037 with Dissolve(0.5)
        k "喂。小……小心点。拜托。"
        j "我会的。我们这个队伍里可不能再有人受伤了。*轻笑*"
        scene c006_s012_038 with Dissolve(0.25)
        k "不，我是认真的。"
        j "我知道。我这是拿讽刺当防御机制。这次我会小心的。"
    scene c006_s012_039 with Dissolve(0.5)
    k "我在这儿。你回来的时候敲敲门。"
    j "你想要个特殊暗号吗？"
    scene c006_s012_040 with Dissolve(0.25)
    k "不不。就……敲一下，告诉我是你、而且一切平安。"
    j "好。"
    scene blank with Dissolve(2)
    scene c006_s012_048 with Dissolve(2)
    "那条连廊挺不错。或者说，挺方便。肯定是哪个爱抱怨的阔太太妈妈抱怨自家孩子下雨天还得走着去上课什么的，学校就修了这个。它没有保温层，也没有暖通空调，但就隔绝雾这件事而言，目前它干得不错。"
    "如果哈灵顿楼那边还是封闭的，也许能让我们至少走完一段横穿校园的路。它应该能让我们弄清楚还有哪些别的路线可选。"
    scene blank with Dissolve(2)
    scene c006_s012_049 with Dissolve(2)
    "好，这段路直接通到楼背面。而且门没锁。我在想，要是校园保安到最后还在，他们会不会把门锁上？以我在学校时的经验，大多数教学楼都是二十四小时开放的，因为很多人想把活儿挤在一天里的各个时间段做完。"
    scene c006_s012_050 with Dissolve(0.25)
    "我想喊一声「有人吗？」，但引起别人注意不是个好主意。我应该小心点，万一还有人待在这一带。谁知道他们现在是什么状态。"
    scene c006_s012_051 with Dissolve(0.25)
    "望出去只有满满的雾，还有其他楼的楼顶。"
    scene blank with Dissolve(2)
    scene c006_s012_052 with Dissolve(2)
    "我唯一听见的动静就是自己脚步的回声。这就意味着这个地方早就人走空了。我去几间教室看看有没有什么值得注意的东西。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c006_s012_041 with Dissolve(2)
    play music insideday2 fadein 20
    l "呕呃……呃嗯……"
    s "我懂那种感觉。至少你还活着，哪怕你并不觉得自己想活。"
    scene c006_s012_042 with Dissolve(0.25)
    l "唔……雪莉？"
    s "对。我跟卡莉和[player_name]说了会照看你。确保你不会再吐一地。"
    scene c006_s012_043 with Dissolve(0.25)
    s "给，我给你拿了水和一根早餐棒。你得往肚子里垫点东西。相信我，我懂。我以前有些东西能让宿醉好过一点，但我的老配方用完了。"
    l "*叹气* 谢了。我……严重高估了自己的酒量。"
    scene c006_s012_044
    s "大家都一样。算你运气好，没在可能会出事的地方喝成那样。所以他们老告诫我们女生：参加聚会绝不能落单。"
    s "连出去玩玩都得担心某个素不相识的男人趁你多喝几杯占你便宜，这事挺让人丧的。"
    scene c006_s012_045 with Dissolve(0.25)
    s "你运气好，[player_name]在身边。或者，我猜是他把你弄上床的。我可没干这事，卡莉那身板更不可能拖着谁走。不过，也许是你自己喝高了，踉踉跄跄摸进来的？"
    scene c006_s012_046 with Dissolve(0.5)
    l "不，不是。昨晚我跟[player_name]在一起。"
    s "他今早一直在灌咖啡，那就对得上。"
    scene c006_s012_047 with Dissolve(0.25)
    l "*叹气* 我不知道我还撑不撑得住。这一切实在太多了。我一天天就这么混过去。我……我不行了……"
    s "喝过头就是这个下场。抱歉。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c006_s012_053 with Dissolve(2)
    play music school fadein 2.0
    "空着。现在是暑期学期，不是每间房都会用到。这间呢？闻着像清洁剂和地板蜡。"
    "外面呢？雾很浓，什么都看不清。"
    scene c006_s012_054 with Dissolve(0.5)
    "我好像能看到附近两三栋楼的轮廓。我知道雪莉说过她真的很不认路，但这方面她总能帮上点忙的。我们越清楚这些楼跟哈灵顿楼是怎么连起来的，就越好。"
    scene blank with Dissolve(2)
    scene c006_s012_055 with Dissolve(2)
    "好了。我没有把每间房都仔细搜一遍，但如果有人藏在这儿，那他们藏得相当到位。这儿没有一般人长期占据会留下的痕迹。"
    "好消息是这地方是封闭的。我觉得我们可以不用全副武装就来查看，这很重要——至少在给卡莉和雪莉找到装备之前是这样。这样也许能让大伙一起过来，把这地方彻底搜一遍，看有没有能用的东西。"
    scene c006_s012_056 with Dissolve(0.25)
    "正门通向街面，那边我没看到什么有希望的东西。我们看看这扇侧门通往哪儿。"
    "*咔哒* *咔哒-咔哒*" with hpunch
    scene c006_s012_057 with Dissolve(0.25)
    "锁着。当然了。看来我今天的运气没那么好。我可以试着把它砸开，但今天还是算了。我不知道另一边有什么，现在还不该再赌运气。说不定下一栋楼门户大开，里面全是灼烧者呢。"
    scene blank with Dissolve(2)
    scene c006_s013_001 with Dissolve(2)
    "{color=#ffcccc}原来守着门等人是这种感觉？我没想到会这么紧张，但每次听到点什么动静，就会把神经全勾起来。可我不能就这么躲开。劳拉现在根本不行，就算她行，我也应该至少能做成这一次。{/color}"
    "{color=#ffcccc}算我运气好，头好多了。视线还有点不稳，远处的东西仍然模糊。但我没有之前那种眩晕的毛病了。而且谢天谢地，头也不疼了。{/color}"
    scene c006_s013_002 with Dissolve(0.25)
    "{color=#ffcccc}听起来雪莉和劳拉在走动。我能听见雪莉一直在说话。她真的很爱聊，是吧？我想这就是她的性格，或者是她应付焦虑的方式。不是每个人都会像我这样，能安安静静坐上好几个小时。{/color}"
    "{color=#ffcccc}我知道劳拉说她昨晚喝醉了，但我担心她没能很好地应对这一切。证据就在她小声嘟囔的那些话里。我想如果我有个儿子，我大概也会这样。我还会加一句「还有个丈夫」——但按她说的，她那段婚姻好像已经完了。至少在她心里完了。{/color}"
    scene c006_s013_003 with Dissolve(0.25)
    "{color=#ffcccc}不过，她对基思一定还是有感情的，哪怕那些感情被悲伤和愤怒染了色。她需要知道他没事。我……我懂。我甚至比自己以为的更懂。因为当我开始意识到，我自己的经历里也有一个我本该在乎的人，可我感受到的却只有恐惧。{/color}"
    "{color=#ffcccc}但说到底，我还是想知道他有没有事。哪怕只是等我们离开这个地方以后，一个电话或者一条短信。{/color}"
    "*敲* *敲*" with hpunch
    j "喂，是我。我回来了。"
    scene c006_s013_004 with Dissolve(0.25)
    k "等等，等等。"
    scene c006_s013_005 with Dissolve(0.5)
    k "怎么样？"
    j "不错。挺有希望。我没把每一寸都走遍，但我看到的都是空的、封闭的。没有开着的窗户。等我们想好怎么继续往前走的这段期间，完全可以去那边探索探索。"
    scene c006_s013_006 with Dissolve(0.25)
    j "周围校园的景色可能不怎么样，但它能帮我们发现附近有哪些值得去的地方。停车楼。快餐店。或者别的什么。"
    k "听起来确实挺有盼头。"
    scene c006_s013_007 with Dissolve(0.5)
    menu:
        "问问她。\n[rgr](卡莉 好感 +1)":
            $ k_friend += 1
            j "你怎么样？平衡感还是有问题吗？"
            scene c006_s013_008 with Dissolve(0.25)
            k "我、我挺好的。好多了。视野边缘还有点模糊，不过我能走。只要需要再出发，我随时可以。"
            j "现在先放轻松。在我们想好怎么继续之前，不用急。"
        "问问劳拉。":
            j "劳拉那边有消息吗？我去看她的时候她昏迷着。"
            scene c006_s013_008 with Dissolve(0.25)
            k "雪莉去看过她。我听见她们在走动，还有雪莉说话的声音，所以我想她醒了。"
            j "那就好。我不觉得劳拉是那种很能喝的人，所以昨晚对她来说可能过量了。"
    scene c006_s013_009 with Dissolve(0.25)
    j "来，帮我把这些东西放回原位，然后我们去找其他人。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c006_s013_010 with Dissolve(2)
    play music insideday fadein 2.0
    s "你回来了。太好了。我不喜欢那扇门那么久都敞着。因为……"
    j "没事。空的。那边没人。走廊尽头有一扇门，我猜是通向另一栋楼的，但锁着。所以如果你那些朋友是从那儿走的，他们肯定把门都关好了。或者，也许他们走了别的路，因为碰到了跟我一样的情况。"
    scene c006_s013_011 with Dissolve(0.25)
    s "所以那边真的什么都没有？"
    j "有几间基本空掉的教室。我没仔细搜一遍看能不能给我们找到些东西，不过有几间房是被人搬空的。"
    scene c006_s013_012
    s "嗯。不知道那间画室还开不开。哈灵顿楼里有间绘画工作室，我本来打算暑假泡在那儿。你只上一门课的时候，总有些空闲时间要打发，我想提前开始下学期的项目。"
    j "嗯，如果你有兴致去探探，我可以告诉你怎么走。不过也许别一个人去。我们两个人搭伙会更稳妥。"
    scene c006_s013_013 with Dissolve(0.25)
    s "就像结伴制度一样。"
    j "就像结伴制度一样。所以，劳拉……"
    scene c006_s013_014 with Dissolve(0.25)
    s "她去洗澡了。她觉得自己脏兮兮的，想好好泡一泡。把她身上那股呕吐物和酒味洗掉。这宿舍里又不是第一个早上醒来、只想把前一夜所有记忆从身上洗掉的女人了。"
    s "算她走运，不用操心要不要吃事后避孕药。真希望我能多帮点忙。我以前有些东西能压住真宿醉，但现在用完了。"
    scene c006_s013_015 with Dissolve(0.25)
    j "好了，我打算换身舒服点的衣服。这件外套能挡住雾里的东西，可它是给凉天穿的。我有点出汗。"
    s "去洗你自己个澡吧。也许能给劳拉表演一下，让她好受点。不管怎样，我们都在。"
    if ch6_laura_sex == "yes":
        "好……她刚才只是一个不设防的大学生，还是说她知道我们昨晚在一块儿了？"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_27_719", transition=Dissolve(1.0))()
    pause
    $ Hide("june_27_719", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music nightmain2 fadein 2.0
    scene c006_s013_016 with Dissolve(2)
    "我终于找到劳拉的时候，她瘫在沙发上，电视开着。休息室里弥漫着空洞静电的低嗡声。卡莉和雪莉不知在哪儿，要么在一起待着，要么各自在房间里。"
    scene c006_s013_017 with Dissolve(0.5)
    "尽管一点细节都没有，劳拉的目光死死锁在电视上。我决定先过去陪她一会儿，哪怕只是待着。"
    "虽然我并不喜欢干坐着等——心底里我需要找点事做，而这段空闲实在无聊——但现在也确实没什么可做的。"
    "能进哈灵顿楼和附近的宿舍，就能搜刮补给和装备，但最终我们得考虑怎么继续走向医院。"
    scene c006_s013_018 with Dissolve(0.5)
    "而劳拉看起来根本没法考虑任何事。看她的情绪，还有说话时那种空洞的语气，我知道这不只是宿醉的余韵。"
    scene c006_s013_019 with Dissolve(0.5)
    l "你进了隔壁那栋教学楼？"
    j "对。我看过了。里面没人，但可以放心进去探索。没有开着的窗户。没有意外。只有尽头一扇锁着的门，大概通向校园更深处。"
    scene c006_s013_020 with Dissolve(0.25)
    l "好吧。随便吧。"
    j "你要喝点什么吗？或者吃点？我去给你拿。"
    scene c006_s013_021 with Dissolve(0.25)
    l "不饿。不渴。"
    j "好吧。你最近跟其他人说过话吗？"
    l "…"
    scene c006_s013_022 with Dissolve(0.25)
    j "劳拉，你是——"
    l "算了。我……我不想再说话了。我说话说够了。"
    menu:
        "算了。":
            "现在最好不要逼劳拉。我们都有点残破、疲惫，而这一切看起来终于一次性全追上她了。"
        "说点什么。\n[rrd](劳拉 好感 -1)":
            $ l_friend -=1
            j "听着，我知道一切都烂透了，但我可以当一个好听众——"
            scene c006_s013_023 with Dissolve(0.25)
            l "你他妈什么都做不了，所以别说了！"
            j "好。知道了。"
            "别往心里去。她已经受够了。我该退一步，让她睡一觉缓过来。也许她过会儿就缓过来，变回原来的样子。"
    scene c006_s013_024 with Dissolve(0.5)
    "我们沉默地坐了一会儿。我不确定自己待在旁边对她有没有好处，就决定悄悄溜开，把空间留给她。又不是要走人。她要是需要我，我就在这栋楼里。"
    scene c006_s013_025 with Dissolve(0.5)
    "我走的时候突然想到，前面几周发生的事对她来说可能实在太多了。劳拉从来没给我一种容易陷入抑郁的感觉，但在极端压力之下，什么都有可能。"
    "眼下我只能给她一点空间。"
    scene blank with Dissolve(2)
    scene c006_s013_026 with Dissolve(2)
    "我在三楼的房间里翻找了一阵，除了更多女装和一些女性卫生用品，什么也没发现，然后走回休息室经过。这会儿她又瘫在沙发上了，电视还开着。"
    scene c006_s013_027 with Dissolve(0.5)
    "我在那儿站了一会儿，侧耳去听有没有任何广播的迹象能穿透这堵刺耳的噪音墙。"
    "什么也没有。或者至少现在没有。我敢肯定劳拉打开它，就是抱着能听到点什么的希望。任何东西。她需要知道彼得没事。基思也是。就算他们正要离婚。"
    scene c006_s013_028 with Dissolve(0.5)
    "我悄悄查看了她的情况。劳拉睡得很沉。"
    scene c006_s013_029 with Dissolve(0.25)
    "尽管我很不情愿就这么把她留在这儿，但如果这点静电正好能给她提供入睡所需的白噪音，那我就把这一切都留给她、不去打扰了。沙发够软够舒服，她也确实该休息。"
    scene c006_s013_030 with Dissolve(0.5)
    "我知道她又在过度专注这件事了。她拼命想看到任何一点「外面还好」的迹象——任何一点关于我们处境的有用信息——但我知道这正在腐蚀她内心的什么东西。理智？意志力？还是介于两者之间？"
    scene c006_s013_031 with Dissolve(0.25)
    "我大概也该去睡了。不过在那之前，先去看看卡莉，问问她怎么样。我回来以后还没怎么跟她说话。"
    scene c006_s013_033 with Dissolve(0.5)
    "其实，雪莉一加入，她就有点沉默了。不过我也不该太意外。通常在别人更抢话的时候，她就会在谈话里「退居其次」。"
    scene c006_s013_034 with Dissolve(0.25)
    "我该去找雪莉试试吗？她对我还是有点疏远。不过她和卡莉倒是渐渐熟络起来。也许我先问卡莉更好。别再搅乱我们之间本来就不稳定的关系。"
    scene c006_s013_035 with Dissolve(0.25)
    j "卡莉？你醒着吗？"
    k "呃，醒着。你、你可以进来。"
    scene blank with Dissolve(1)
    scene c006_s001_003 with Dissolve(1)
    j "嗨，我正要去睡之前先来看看你。也想确认你还撑得住。我知道今天挺忙的。"
    "她换的什么？我猜她找到了舒服的衣服。大概是雪莉给她的。"
    k "我没事。好多了。感觉基本恢复正常了。有张床真不错。能睡个整晚。"
    scene c006_s001_004 with Dissolve(0.25)
    j "天啊，这话我完全同意。比起蜷在沙发上强多了，哪怕那也是宿舍床。你的皮肤怎么样？烧伤那边？"
    k "一碰就疼，但在好转吧。我想。很难说。最近我不太想照镜子看太久。我眼睛里的红血丝大概也基本消了。你能不能……坐……"
    scene c006_s001_005 with Dissolve(0.25)
    j "据我看起来，恢复得相当不错。最严重的部分在消退了。"
    scene c006_s001_006 with Dissolve(0.5)
    k "请再凑近点看看。我好确认不是自己眼睛出了问题、根本看不出来。"
    j "好。"
    scene c006_s001_007 with Dissolve(0.25)
    "操，这件衬衫几乎兜不住她的奶子。我不该盯着这个。"
    j "对，你确实在恢复。而且眼睛也没那么红了。也许我能找点眼药水帮帮忙。"
    scene c006_s001_008 with Dissolve(0.25)
    k "太好了。我……我只是担心它不会好起来。我不想最后留下一道疤。很丑的那种。我知道这有点虚荣，但……"
    menu:
        "我觉得你不用担心。\n[rgr](卡莉 信任 +1)":
            $ k_trust += 1
            j "我觉得你不用担心。你恢复得好好的。很快就会变回原样。"
        "你怎么都好看。\n[rgr](卡莉 好感 +1)":
            $ k_friend +=1
            j "拜托啦~~~ 你怎么都好看。就算真会留疤，那也只是给相貌添点特色。"
    scene c006_s001_009 with Dissolve(0.25)
    k "谢啦。"
    scene c006_s001_104 with Dissolve(0.25)
    j "嘿，那个，我……你怎么看雪莉？你跟她接触得比别人多得多，我自己不太敢去找她。不是说我怕她，而是我不想惹毛她。"
    j "感觉她还是提防我，因为她以为自己看到了什么。或者说，因为那些男的出去以后她不得不面对的事。"
    scene c006_s001_105 with Dissolve(0.25)
    k "她在我面前特别能说，但这也许就是她本来的样子。有时候她能自顾自说上好几分钟，都不等我回应。"
    j "我敢肯定你听得津津有味。"
    scene c006_s001_106 with Dissolve(0.25)
    if k_trust >= 6:
        k "我能应付。我不觉得她真的怕你，但你让她按自己的节奏来接近你也未必错。我要是处在她的位置，也会希望这样。她还不知道你是可以信任、不会伤害她的人。"
    else:
        k "我能应付。我不觉得她真的怕你，但你让她按自己的节奏来接近你也未必错。我要是处在她的位置，也会希望这样。"
    j "好吧。我也是这么想的。我本来打算在睡觉前去看她一眼，但还是先按下不表，等她自己主动。"
    scene c006_s001_107 with Dissolve(0.5)
    k "那劳拉呢？她……她看起来可不太妙。"
    j "确实。这不只是昨晚喝醉的问题。我当时就该意识到，但我以为我们喝几杯能让她放松一点。她的情绪状态很不好。我之前想跟她聊聊，她不愿意，所以我就给她留点独处时间。"
    j "眼下她瘫在沙发上。电视开着。"
    scene c006_s001_108 with Dissolve(0.25)
    k "她抑郁了，对吧？她之前是真的铁了心要开车去医院、被救出来。现在这条路眼看走不通，她就快撑不住了。"
    j "我不是心理医生，但我也看得出这是怎么回事。创伤后应激。抑郁。对这一切彻底受够了。我离婚那阵子，离婚前后，也很不好过，所以我能理解。明天我会再试着跟她谈谈，因为我不会就这么放弃她。尤其是在她最需要朋友的时候。"
    scene c006_s001_109 with Dissolve(0.25)
    k "我也会试试。她……她对我来说一直像个没有血缘的妈。这一切开始以后更是。"
    j "好，我们一起。我不认为能把她从这个状态里硬拽出来，但在她需要的时候给她支持，也只能做到这一步了。"
    k "嗯。"
    scene c006_s001_010 with Dissolve(0.5)
    "我们靠得也太近了，这感觉怪得有点过头。纯粹因为需要，我们之间的私人距离早就被抛到脑后了。可我们之间就是有股热乎劲。而我又拼命忍着不去偷看，这更不管用。操，我开始硬了。"
    menu:
        "该起来了。":
            "我该起来走人了。趁现在还没太尴尬。"
            scene c006_s001_011 with Dissolve(0.25)
            j "那我该走了。已经晚了，我不想耽误你睡觉。我想你也想一个人待会儿。"
            k "我……嗯，好。"
            scene c006_s001_102 with Dissolve(0.5)
            j "晚安。"
            k "你也是。"
            scene c006_s001_103 with Dissolve(0.5)
            "我很想再多陪卡莉一会儿——我们困在这儿越久，真的越像是在慢慢靠近——但我……我得诚实：我溜走是为了躲开一股很严重的情欲张力。"
            "我知道这不是她的错，但那件衬衫让我很难不去偷看。而且我本来就觉得她很可爱。很性感，哪怕她自己不这么表现。我不需要这个。也不需要冒险一不小心做出什么，毁掉我们已经取得的进展。"
            jump ch6_endofnight
        "[gr]我有话直说。":
            scene c006_s001_011 with Dissolve(0.25)
            j "好，卡莉，我有话直说。那件衬衫几乎什么都没藏住。不是我介意。只是……"
            scene c006_s001_012 with Dissolve(0.25)
            k "*咯咯笑* 我……它穿着舒服。而且劳拉找的那件毛衣一直在磨我本就发嫩的皮肤。"
            j "哦，我这边没什么可抱怨的。不过，也许觉得你该知道一下。"
            scene c006_s001_013 with Dissolve(0.25)
            k "再说了，你早上大概看得比这更多。"
            j "没你想的那么多。也许露了一点侧乳，或者一点屁股，但我确实努力把视线移开了。我知道有一种「熟人之间的裸露」程度，我觉得我们俩都能说没有越过那条线。"
            scene c006_s001_014 with Dissolve(0.25)
            k "也许吧……"
            j "好吧，那我该走了。也许真能找到我老说要找的那种眼药水。也让你好好休息。而且我想你也想一个人待会儿。"
            if k_friend >= 13 or k_friend >= 10 and k_desire >= 6:
                $ ch6_staywithkallie = "yes"
                scene c006_s001_015 with Dissolve(0.25)
                k "你能……[player_name]，你能留下来吗？我很不想麻烦你，但就一会儿。我……我不想一个人。现在不想。就到我睡着为止。拜托。"
                scene c006_s001_016 with Dissolve(0.5)
                k "我今晚就是特别焦虑，知道有人在附近会好受很多。"
                j "懂你。陌生的地方。外面一堆疯狂事。全是未知。我不介意。床不大，但如果你不介意我，我就陪你到你睡着。"
                scene c006_s001_017 with Dissolve(0.5)
                k "谢谢。我、我很感激。"
                "就跟之前在办公室沙发上那次一样。她只是需要有人在身边，让她觉得安全。我该庆幸她把我当成可以信任的人。"
                stop music fadeout 2.0
                scene blank with Dissolve(2)
                scene c006_s001_018 with Dissolve(2)
                play music kallietheme fadein 2.0
                "过了大约一分钟，我们安顿下来。正如我说过的，床不大，她的屁股几乎立刻就贴上了我的胯。我一直在等那个时刻——她不再矜持，让我挪一挪、让我们之间留点空隙。或者不会——考虑到之前那些身体接触。"
                "我不知道过了多久，才听到伴随卡莉入睡的轻柔呼噜声。我把这理解成我这个「安全毯」的职责完成了。如果我想，我可以溜出去，顺便处理一下短裤里那根{a=https://www.urbandictionary.com/define.php?term=Semi-Hard}半硬{/a}。"
                menu:
                    "留下过夜吧。\n[rgr](卡莉 爱意 +1)\n[rrd](卡莉 欲望 -1)\n[pks]":
                        $ ch6_kallie_sex = "yes"
                        $ k_love += 1
                        $ k_sex += 1
                        $ k_desire -=1
                        "也许我可以再多待一会儿。太早起来会吵醒她，我不太想那样。而且我得承认，身旁有个暖烘烘的身体挺享受的。闻着香。而且很软。"
                        call ch6_kallie_sex from _call_ch6_kallie_sex
                    "现在就走。[rx]真的?\n[rgr](卡莉 欲望 +1)":
                        $ k_desire += 1
                        "对，趁她睡着走。"
                        scene c006_s001_093 with Dissolve(1)
                        "我很想再多陪卡莉一会儿——我们困在这儿越久，真的越像是在慢慢靠近——但我……我得诚实：我溜走是为了躲开一股很严重的情欲张力。也许还能趁一个人的时候打一发。"
                        scene c006_s001_094 with Dissolve(1)
                        "我知道这不是她的错，但那件衬衫让我很难不去偷看。而且我本来就觉得她很可爱。很性感，哪怕她自己不这么表现。我不需要这个。也不需要冒险一不小心做出什么，毁掉我们已经取得的进展。"
                        jump ch6_endofnight
            else:
                scene c006_s001_015 with Dissolve(0.25)
                k "我……嗯，好。"
                scene c006_s001_102 with Dissolve(0.5)
                j "晚安。"
                k "你也是。"
                scene c006_s001_103 with Dissolve(0.5)
                "我很想再多陪卡莉一会儿——我们困在这儿越久，真的越像是在慢慢靠近——但我……我得诚实：我溜走是为了躲开一股很严重的情欲张力。"
                "我知道这不是她的错，但那件衬衫让我很难不去偷看。而且我本来就觉得她很可爱。很性感，哪怕她自己不这么表现。我不需要这个。也不需要冒险一不小心做出什么，毁掉我们已经取得的进展。"
                jump ch6_endofnight
label ch6_endofnight:
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c006_s013_031 with Dissolve(2)
    l "嗯唔~~~ 唔嗯~~~"
    l "{size=30}不……不不、嗯~~~{/size}"
    scene c006_s013_032 with Dissolve(0.25)
    tv "{i}……生命迹象……救援工作持续进行……{/i}"
    tv "{i}……勉强可视为不宜居住……{/i}"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_2_738", transition=Dissolve(1.0))()
    pause
    $ Hide("july_2_738", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday fadein 2.0
    if ch6_kallie_sex == "yes":
        scene white with Dissolve(2)
        scene c006_s014_019 with Dissolve(2)
        j "唔嗯~~~ *打哈欠*"
        scene c006_s014_020 with Dissolve(1)
        "哦？有那么一瞬间，我忘了自己在哪儿、又是怎么到这儿的。至于卡莉？她真的一整晚都贴着我睡。这一点我不介意。我完全可以习惯一睁眼旁边就躺着一个一丝不挂的性感小女人。"
        scene c006_s014_021 with Dissolve(0.5)
        "我做梦都想不到昨晚会是那样的。之前她几乎不跟我说话。"
        "按她说的，我想这有一半是因为她本身内向，另一半是因为安德鲁在用各种方式压着她，让她少跟那些可能指出她婚姻有问题的人来往。"
        scene c006_s014_022 with Dissolve(0.25)
        "等劳拉心情好一些，我得跟她好好谈谈出去以后该怎么办。我们总不能直接把她送回他身边，对吧？最坏的情况，也不过是我把她送上飞回她家的飞机，然后再也见不到她。"
        scene c006_s014_021 with Dissolve(0.25)
        "又或者，就像昨晚那样，我们让她自己做一个完全属于自己的决定。我们逼她去做她不想做的事，那就跟安德鲁没什么区别。"
        scene c006_s014_022 with Dissolve(0.25)
        "最好还是别表现得好像我们之间真的变了什么。昨晚我们确实聊了她和她的生活，比以往任何时候都多，但我不会假装我们刚刚开始了一段什么关系。"
        scene c006_s014_023 with Dissolve(0.5)
        "昨晚的事，我就该装作什么都没变。那不是两个人坠入爱河。那是一个年轻女人想从自己的人生里拿回一点主导权。"
        if ch6_kallie_sex_cum == "yes":
            "而我很乐意在场，因为我一直觉得她很可爱。疏远，但可爱。不过看到她一丝不挂的样子？天哪天哪。真是个性感的小妖精。我可以习惯射在她里面。说到这个……去找避孕套吧。"
        else:
            "而我很乐意在场，因为我一直觉得她很可爱。疏远，但可爱。不过看到她一丝不挂的样子？天哪天哪。真是个性感的小妖精。"
        scene c006_s014_024 with Dissolve(0.25)
        "最好别让自己去期待、去奢望那些不会成真的事。那只是一次性的，我不能指望她还会那样想要我。天知道，南希很快就厌倦我了。"
        scene c006_s014_025 with Dissolve(0.25)
        "我知道男人都爱说「真舍不得离开你」，但这一次这句话确实成立。自从离婚前南希把我赶到沙发上以后，这是我第一次跟女人同床。"
        if l_sex == 1:
            "说真的，就连我跟劳拉那次做完了以后，我们最后还是各走各的。再说劳拉，出于多个原因，我大概该把{b}这件事{/b}烂在肚子里。嗯，我们搞过一次然后就过去了，但我不指望跟她说出去以后不会闹出什么事。"
        elif ch5_laura_sex == "yes":
            "说真的，就连我跟劳拉那次做完了以后，我们最后还是各走各的。再说劳拉，出于多个原因，我大概该把{b}这件事{/b}烂在肚子里。我不知道她对我们之间这事是什么想法，但我不指望跟她说出去以后不会闹出什么事。"
        scene c006_s014_026 with Dissolve(0.25)
        "好了，别再慢吞吞地吊着我，好让我多看两眼卡莉的身体。该套上衣服、趿拉着去洗澡了。"
    scene blank with Dissolve(2)
    scene c006_s014_001 with Dissolve(2)
    if ch6_kallie_sex == "yes":
        "我很确定没吵醒卡莉。听起来也没别人醒着。正好可以洗一洗。当然，我们没就时间表达成什么口头约定，但我押的是天蒙蒙亮这个点更好。或者至少赶在两个最小的醒来之前。"
    else:
        "早起就是为了赶在其他人起床前洗个澡。当然，我们没就时间表达成什么口头约定，但我押的是天蒙蒙亮这个点更好。或者至少赶在两个最小的醒来之前。"
    scene c006_s014_002 with Dissolve(0.5)
    if ch6_kallie_sex == "yes":
        "我确定卡莉睡着了。我很不想离开她——她看起来太可爱了——但考虑到昨晚发生的事，我觉得两个人在彼此怀里温存着醒来并不是什么好主意。"
        scene c006_s014_003 with Dissolve(0.5)
        "尽管她向我保证那正是她想要的，我不得不认为，在清晨冷冽的光线下，我大概不会那么好看。"
    else:
        "考虑到我们到了这儿以后，卡莉几乎没什么隐私可言，我想让她至少有一天能自己安安静静洗个澡。"
        scene c006_s014_003 with Dissolve(0.5)
        "我们把「体面」和「一点小小的享受」的标准降到这种地步，是他妈的多可悲啊。"
    scene c006_s014_004 with Dissolve(0.5)
    "劳拉可能是唯一一个这么早还醒着的人。尤其是她昨天大半时间都花在从宿醉里恢复。今天我得去看看她。把我看到的给她汇报一下，这样我们也许能做些计划。"
    play ambient shower
    scene c006_s014_005 with Dissolve(0.5)
    "而且迟早我们得试着打开雪莉这块缺口。卡莉跟她处得好像还行。比我强。她对我真是……太疏远了。"
    scene c006_s014_006 with Dissolve(0.25)
    "因为迟早我们得继续上路，而我们谁都不想就这么把她留在这儿。除非她自己想留下。感觉我们到现在都还没真正让她谈过这一整件事。好像我们在绕着这个话题打转，因为怕她的反应。"
    scene c006_s014_007 with Dissolve(0.5)
    $ s_desire += 1
    s "早上好~~~"
    j "哦，靠。呃，早上好。"
    scene c006_s014_008 with Dissolve(0.25)
    j "我还希望我来得早一点，能赶上「男生专属时段」。"
    s "这是女生宿舍，老兄。这里从来就没有「男生专属」。"
    scene c006_s014_010 with Dissolve(0.5)
    s "不过，你要是能一直这么性感，我倒是愿意给你开个通行证，让你随时都能来。事实上，我们可以试着多找找两个人都在的时间。"
    j "*轻笑* 好吧~~~"
    "这一版的雪莉到底藏在哪里？我想这说明她没那么怕我了。"
    scene c006_s014_011 with Dissolve(0.25)
    s "在我看来，这不算拒绝。"
    "好了，这已经不只是打情骂俏了。而且她就在那儿脱衣服。我该……"
    menu:
        "让她看个够。\n[rgr](雪莉 好感\欲望 +1)":
            $ s_friend += 1
            $ s_desire += 1
            scene c006_s014_013 with Dissolve(0.5)
            j "那这说明什么？"
            s "说明你下面硬得……*咯咯笑*"
        "转过去。":
            "眼睛盯着地砖看。就当这里是监狱。"
            scene c006_s014_012 with Dissolve(0.25)
            s "嗯，那屁股就是女生被操的时候会想抓住的那种。"
            scene c006_s001_073 with flash
            pause 0.3
            scene c006_s014_012 with Dissolve(0.5)
            "昨晚有人试过了。"
            j "那我谢谢你啊。"
    scene c006_s014_014 with Dissolve(0.25)
    s "这种小打小闹的调情倒是挺有意思，可我来这儿是为了洗澡。"
    j "我很快就洗完，不打扰你了。"
    scene c006_s014_015 with Dissolve(0.5)
    s "哎，别这么快就走。我自己弄的时候，想到你会哼哼唧唧，到时候谁来听？这样才公平嘛。"
    j "哼……好吧~~~"
    scene c006_s014_016 with Dissolve(0.25)
    s "你要是在洗澡时想着操我、打个手枪，我也无所谓。我不介意。"
    "靠，这发展太快了。一开始只是猝不及防碰面后的一段尴尬调情，现在却成了……这是什么？"
    scene c006_s014_017 with Dissolve(0.25)
    "我想我该高兴她对我态度好些了，虽然这并不是我想要的方式。不过我得说，那屁股是真紧。"
    scene c006_s014_018 with Dissolve(0.25)
    s "哦，对，大男孩。就这样、啊啊啊~~~"
    "靠，一大早搞这些也太早了。"
    stop ambient
    if persistent.ch6_complete == False:
        $ persistent.ch6_complete = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_chapter6", transition=slideright)()
        pause
        $ Hide("achievement_chapter6", transition=dissolve)()
        $ quick_menu = True
label chapter07:
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("chapter07", transition=Dissolve(1.0))()
    pause
    $ Hide("chapter07", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s001_001 with Dissolve(2)
    play music insidedark fadein 2.0
    "好了，趁雪莉还没闹得更过分，穿好衣服赶紧出去。或者趁别人还没走进来、开始琢磨这里头到底在搞什么。"
    if ch6_kallie_sex == "yes":
        "尤其是在昨晚之后。我不打算假装我们现在就是恋人了——事实上，我敢打赌卡莉会装作昨晚什么都没发生——但我们的生活里已经够多狗屁事了，我没必要再添新的。"
    else:
        "卡莉可能会有点担心，想听我们俩给个说法。自从这一切开始，我一直很努力弥合我们之间的裂痕，但你永远不知道什么会让她退开。"
    scene c007_s001_002 with Dissolve(0.25)
    "那劳拉呢？我要是不小心说了什么，她会信。就算她现在状态不好，她也足够信任我，知道我那边没干什么。她提过，她把雪莉想成那种「疯癫小精灵」。"
    scene c007_s001_003 with Dissolve(0.25)
    "说到劳拉，她在哪儿？她昨晚在这儿昏睡过去。老天，电视还开着。"
    "我想再跟她试试。看看她心情有没有好一点。我完全有理由担心她被我们现在的处境压得喘不过气。我这个业余心理咨询师并不高明，但我不能就这么把她一个人丢着。"
    "我该看看她夜里有没有挪到床上去。"
    scene blank with Dissolve(2)
    scene c007_s001_004 with Dissolve(2)
    "好——不在那儿。卡莉还在自己房间。而我刚把雪莉留在淋浴间里。她他妈跑哪儿去了？这地方又不大。虽然有整整三层。"
    scene blank with Dissolve(2)
    scene c007_s001_005 with Dissolve(2)
    "二楼三楼都没有。她的可能去向越来越窄，而且每况愈下。她不在后门那儿。幸好那儿还堵着，所以她没溜进哈灵顿楼。那就意味着……什么？"
    "剩下的唯一地方就是……"
    scene c007_s001_006 with hpunch
    "靠！大门。她该不会是出去了吧？"
    scene blank with Dissolve(2)
    scene c007_s001_007 with Dissolve(2)
    j "{size=58}靠靠靠靠靠！！！{/size}" with vpunch
    s "喂。你在哪儿——"
    scene c007_s001_008 with Dissolve(0.25)
    j "靠！"
    s "好吧~~~我可以，但不是……现在……"
    scene blank with Dissolve(2)
    scene c007_s001_009 with Dissolve(2)
    l "{size=28}我应该……也许……{/size}"
    play sound doorclose
    scene c007_s001_010 with Dissolve(0.5)
    j "劳拉？我他妈，总算找到你了。你可真是把我吓死了。我知道你想让我体会你的感受，但也不用这样来证明。"
    j "劳拉？"
    scene c007_s001_011 with Dissolve(0.25)
    l "{size=28}我可以试试……就这么走……{/size}"
    j "劳拉？劳拉！喂，你在干什么？"
    scene c007_s001_012 with Dissolve(0.25)
    l "{size=28}我不行……我不能再待下去了……不、不会好起来的……{/size}"
    j "你装备都没穿。我们先回屋。"
    scene c007_s001_013 with Dissolve(0.25)
    l "{size=28}不，我、我没事。我只是……只是……{/size}"
    l "{size=28}我要是试试，是能撑到的。我、我能……{/size}"
    scene c007_s001_014 with Dissolve(0.5)
    "她状态很不对。像是魂都不在了。"
    menu:
        "温柔点。\n[rgr](劳拉 信任 +1)":
            $ l_trust += 1
            "我试着把她劝回来。我认识的那个劳拉还在里面。"
            j "劳拉，嘿。听我说。你得回屋来。绝对不能这样出去。外面的天气对你没好处。你看，我知道一切都烂透了，你也担心你儿子和基思，但你今天就这么走出去，走不了多远的。"
            j "嘿，是我，[player_name]。我保证我们很快就能重新上路。我们正在想办法。但我们必须做得稳妥，这样才能让所有人都平安到达要去的地方。"
            scene c007_s001_015 with Dissolve(0.25)
            l "[player_name]，你……别……别……"
            j "我知道，我知道。被困在另一栋楼里不是你想要的。我们谁都不想。但求你了，我求你相信我，我们能活着到医院。就算那边没人，我们也会想办法出城。"
            scene c007_s001_016 with Dissolve(0.25)
            j "但要那样，我们就得聪明一点。安全第一。所以我需要你耐心一点，相信我是真心为你好。"
            l "我、我……*抽鼻子*"
            scene c007_s001_017 with Dissolve(0.25)
            "我把能说的都说了。不知道有没有用。我不愿意相信她在这儿失去了理智，但我怪不了她。这一切简直他妈就是恐怖片烂桥段，再坚强的人也可能会崩。而所有这些压力和痛苦，对她来说可能真的太多了。"
        "严厉点。\n[rrd](劳拉 焦虑 +1)":
            $ l_anxiety += 1
            "去他的，我得把她震回当下，哪怕只是暂时的。"
            j "劳拉！嘿！住手！你哪儿也不去。不能这样。我需要你清醒过来。我知道一切都烂透了，你也担心你儿子和基思，但你今天就这么走出去，是不可能活着到任何地方的。"
            j "靠，我懂。你气车开不成，还得等卡莉好起来，但这不是你能这么做的方式。你是个成年人，我今天需要你拿出成年人的样子！"
            scene c007_s001_015 with Dissolve(0.25)
            l "[player_name]，你……别……别……"
            j "听着，我知道自己干过些蠢事。男人出名地爱干些会要命的事。所以我最清楚什么不该做。因为困在这儿而烦躁就冲出去，不是路。我们会到医院。要是那也不行，我们就他妈离开这座城。"
            scene c007_s001_016 with Dissolve(0.25)
            j "但要那样，我们就得聪明点。外面已经有人死了。或者更糟。你要是也死了，就再也见不到彼得了！"
            l "我、我……*抽鼻子*"
            scene c007_s001_017 with Dissolve(0.25)
            "我本可以说得温和得多，但该点的还是得点到。我不愿意相信她在这儿失去了理智，但我怪不了她。这一切简直他妈就是恐怖片烂桥段，再坚强的人也可能会崩。而所有这些压力和痛苦，对她来说可能真的太多了。"
    scene c007_s001_018 with Dissolve(0.5)
    l "我……天哪，我他妈在干什么？"
    j "不知道。我正希望你能告诉我。*轻笑*"
    scene c007_s001_019 with Dissolve(0.25)
    l "我只是……我……我得知道彼得没事。我得见到他。我得……"
    scene c007_s001_020 with Dissolve(0.25)
    l "你不懂有个孩子是什么滋味。拼了命生下一个你爱的东西，然后……却……却不知道他好不好。不知道他是否还活着。"
    l "还有基思……有多少……多少个晚上他跟别的女人在一起？每个周末他都说是去跟朋友「出去逛逛」……我的邻居盖尔……"
    scene c007_s001_021 with Dissolve(0.25)
    l "一个人怎么能把这么多年就这么扔掉？"
    j "嘿、嘿、嘿。以后见到基思，你再冲他大吼大叫。但为着他可能做过的事焦虑，一点用都没有。而且彼得是个聪明、能干的孩子。他身上有太多你的影子了，对吧？所以就算他跟我们一样身陷麻烦，他也能照顾好自己。现在，我们……我们回屋去吧。拜托。"
    scene c007_s001_022 with Dissolve(0.25)
    l "好……我……我今天就不出去了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    play music morning fadein 2.0
    if ch6_kallie_sex == "yes":
        scene c007_s001_023 with Dissolve(2)
        $ renpy.pause ()
        scene c007_s001_024 with Dissolve(0.25)
        k "唔嗯嗯~~~ *打哈欠* 啊~~~"
        scene c007_s001_025 with Dissolve(0.25)
        "{color=#ffcccc}我已经很久没睡得这么沉了。真舒服。不过{i}确实{/i}有点冷。{/color}"
        scene c007_s001_026 with Dissolve(0.25)
        k "哦？呃……"
        "{color=#ffcccc}没穿衣服。我……哦，对。就是因为这个。{/color}"
        scene c007_s001_027 with Dissolve(0.5)
        k "*咯咯笑*"
        "{color=#ffcccc}昨晚出了一身汗。靠着他睡太暖和了，我好像压根没想起来要把衣服穿回去。他已经走了。他肯定是自己起了床，好让我多睡一会儿。他人真好。{/color}"
        scene c007_s001_028 with Dissolve(0.25)
        "{color=#ffcccc}我……我不敢相信我真壮着胆子做了那件事。我躺在那儿装睡，骗了自己多久才终于下手？{/color}"
        scene c007_s001_029 with Dissolve(0.5)
        "{color=#ffcccc}而且我不敢相信，他停下来了两次，只因为要确认我没事。确认我们接下来要做的事没问题。我……我没想到……不知道被人关心「我好不好」是什么感觉……不知道原来会有人把决定权交给我，问我想要什么。{/color}"
        scene c007_s001_030 with Dissolve(1)
        "{color=#ffcccc}我……他……别这样，卡莉。现在想这些太早了。去琢磨如果……{/color}"
    else:
        scene c007_s001_030 with Dissolve(2)
        "{color=#ffcccc}现在几点了？还是说……算了。我肯定比平时睡得久。{/color}"
        scene c007_s001_031 with Dissolve(0.25)
        "{color=#ffcccc}得去看看劳拉，看她怎么样了。还有[player_name]。我敢肯定他又想出去。{/color}"
    scene c007_s001_032 with hpunch
    "*敲* *敲* *敲*"
    s "{size=32}嗨，你起了吗，姑娘？{/size}"
    k "起了。我只是……只是在穿衣服。马上。"
    scene c007_s001_033 with Dissolve(0.25)
    s "{size=32}呃，你得到外面来一趟。快点。{/size}"
    k "好。我尽快。"
    scene c007_s001_034 with Dissolve(0.25)
    "{color=#ffcccc}这听着可不太妙。出什么事了？{/color}"
    scene blank with Dissolve(2)
    scene c007_s002_001 with Dissolve(2)
    k "怎么了？你听着像是出事了。"
    s "是劳拉。[player_name]刚把她带回来。"
    k "带她……什么？什——"
    scene c007_s002_002 with Dissolve(0.25)
    s "哦、哦，她没事。身体上没事。[player_name]之前在找她，听他说，她当时在前门外面。我不知道发生了什么，但她看起来不太对劲。"
    k "靠。"
    scene c007_s002_003 with Dissolve(1)
    j "来。给你。我们先在这儿坐一会儿，休息一下。你脸色很白。或者更白了。"
    j "嘿，我知道你给自己很大压力，但没事的。我们会好起来的。我们会离开这儿，只是得聪明一点、安全一点。而且你很聪明，劳拉。我知道。所以，别再干冲动的事，好吗？"
    scene c007_s002_004 with Dissolve(0.25)
    l "{size=30}我……我只是……我真的以为我们……我们会……{/size}"
    j "我、我、我知道。我们运气不太好。但我们也每次都撑了过来。我们都活着。四肢健全。你是个战士，所以我们先缓一缓，然后接着干。我已经在收拾东西，好让我们重新上路。"
    scene c007_s002_005 with Dissolve(0.25)
    l "{size=32}可是彼得……{/size}"
    j "你儿子没事，很安全，劳拉。基思也是。他会没事的，等你下次见到他，想冲他吼叫就吼叫。或者随你当时的心情。但他们都好好的。我向你保证，他们比我们过得好。所以我们得把注意力放回自己身上，保住自己的命。明白吗？"
    scene c007_s002_006 with Dissolve(0.25)
    l "唔嗯……我……"
    scene c007_s002_007 with Dissolve(0.25)
    s "{size=30}我觉得她崩了。这一切对她来说太重了。{/size}"
    k "嘘~~~"
    "{color=#ffcccc}雪莉说话是不太懂分寸，但我怕她说对了。劳拉好像确实没能好好应对这一切。她之前真的把希望全押在那辆SUV上了，不是吗？{/color}"
    scene c007_s002_008 with Dissolve(0.25)
    j "你要喝点什么吗？吃点东西？到了这儿以后，你看着这两样都没怎么碰。我去给你拿瓶水和一根早餐棒之类的。"
    s "冰箱里有几瓶水。"
    j "谢了。我马上回来。就一下。"
    scene c007_s002_009 with Dissolve(0.25)
    s "慢慢来。我去陪陪劳拉。我们得聊聊。现在就劳拉是我唯一不算合得来的人，而所有人都说我是个交际花，哪怕我们一开始就不是一路人。当然，这也不能怪谁。"
    scene c007_s002_010 with Dissolve(0.25)
    "{color=#ffcccc}趁雪莉陪着劳拉，我该问问[player_name]到底出了什么事。她昨天睡得很多，但我当时只当是宿醉。这事没那么简单。{/color}"
    scene c007_s002_011 with Dissolve(1)
    k "怎么了？"
    j "回头再说。咱们晚点再聊，好吗？我现在不想谈这个。"
    k "呃，好吧。"
    scene c007_s002_012 with Dissolve(0.5)
    j "给。求你了，尽量吃点喝点。你需要这个。等我们重新上路的时候，你得保持体力。我正在努力让我们再动起来。卡莉已经完全好了，我只要给她换件外套和面罩就行。"
    "{color=#ffcccc}他不想提雪莉，因为我们真的还没机会跟她正经说过要继续上路的事。我一提，她就换话题。我敢说[player_name]那边也没从她嘴里听到什么实质内容。{/color}"
    scene c007_s002_013 with Dissolve(0.25)
    j "好。今天早上我们放松一点。最近压力有点太大了。"
    s "姑娘，你该洗个澡了。信我，热水澡提神效果一流。我早上刚洗过，人一下就精神了。洗完这一天就有个全新的开始。"
    scene c007_s002_014 with Dissolve(0.25)
    l "好、好吧。我……我是该洗一个。"
    j "很好。你把早饭吃完，然后我们就去——"
    scene c007_s002_015 with Dissolve(0.25)
    s "我带她去吧。我想你在这栋楼才几天，就在浴室里跟别的女生一起洗漱，花的时间够久了。*咯咯笑* 再说了，也许劳拉想要一点隐私，我保证不偷看。"
    s "我在这儿住得够久，早就知道怎么屏蔽那些半裸着在淋浴间里晃来晃去的女生了。我甚至说不上布丽或特里安娜的奶子长什么样。梅茜的话？那就完全是另一回事了。"
    j "今天这个话题我们大概得跳过。"
    scene c007_s002_016 with Dissolve(0.25)
    s "今天？是啊。但我看得出你很感兴趣。*咯咯笑*"
    scene c007_s002_017 with Dissolve(0.25)
    s "好。劳拉？你准备好了吗？需要我帮忙吗？"
    l "我、我自己能搞定。*叹气*"
    scene c007_s002_018 with Dissolve(0.5)
    s "那我就先待着吧，毕竟你需要一个浴室伙伴。而且我还得补个妆。"
    "雪莉主动顶上，我挺感激。这给了我几分钟时间，让我能停下来试着稳住自己。我想我只是一直太依赖劳拉了，却没意识到她已经悬在边缘了——比喻意义上的。"
    scene c007_s002_019 with Dissolve(1)
    "而且我也该跟卡莉谈谈。"
    j "刚才的事，抱歉。"
    k "不不，能理解。她人就在旁边，当着人家的面议论很不礼貌。不过……出什么事了？"
    scene c007_s002_020 with Dissolve(0.25)
    j "我之前出来的时候，她根本不见踪影。昨晚我把她留在这儿的沙发上。我知道她昨天情绪很不好，这么说还算客气了。老实说，接下来好几天都是这样。所以我不想去打扰她。我想给她点空间。"
    j "所以发现她不见了，我有点慌了。我在楼里到处跑，最后在前门找到她——她盯着外面，念叨着也许干脆就走出去算了。所以我好不容易劝住她，把她拖回屋里。但她那时状态很不好。"
    scene c007_s002_021 with Dissolve(0.25)
    j "确实不好。我……*叹气* 听着，我不是心理医生。我可以跟她谈，试着告诉她事情会好起来，但被困在这儿加上担心家人，她已经严重地恶性循环了。SUV坏掉之前，我们在普罗维登斯生活楼的时候她就已经开始钻牛角尖了，之后更是一发不可收拾。"
    j "她甚至开始认真琢磨基思还跟谁出轨过，我甚至不知道这种想法有没有超出偏执臆想的范畴。"
    scene c007_s002_022 with Dissolve(0.25)
    k "信任一崩塌，她就忍不住要去猜，不是吗？"
    j "我倒不觉得。我能理解。我以前对我前妻也有过类似的念头，但没到她这样。"
    scene c007_s002_023 with Dissolve(0.25)
    k "你觉得她可能会伤害自己吗？"
    menu:
        "她可能会再试着走出去。\n[rrd](卡莉 焦虑 +1)":
            $ k_anxiety += 1
            j "她可能会再试着走出去。这是我最怕的。怕她在某个恍惚的瞬间……发疯的时候……我都不知道该用哪个词……连外套都不穿就冲出去。"
            scene c007_s002_024 with Dissolve(0.25)
            k "那我们得看着她吗？"
            j "眼下应该有人陪着她。我讨厌让所有人都轮到当保姆，但她恢复过来之前我们可能只能这么做。"
        "[gr]我觉得不会。\n[rgr](卡莉 焦虑 -1)":
            $ k_anxiety -= 1
            j "我觉得不会。某种程度上说，劳拉的求生本能挺强的，尤其是我们把话说明白之后——她要是继续这样，就再也见不到儿子了。"
            scene c007_s002_024 with Dissolve(0.25)
            k "我、我不知道。我从没见过她那样。我怕她会做什么冲动的事。"
            j "好，我懂了。这事得小心处理。眼下应该有人陪着她。我讨厌让所有人都轮到当保姆，但她恢复过来之前我们可能只能这么做。"
        "什么都有可能。\n[rrd](卡莉 焦虑 +1)":
            $ k_anxiety += 1
            j "尽管我不想承认，但什么都有可能。我们现在是在一片完全未知的领域里。"
            scene c007_s002_024 with Dissolve(0.25)
            k "那我们得看着她吗？"
            j "眼下应该有人陪着她。我讨厌让所有人都轮到当保姆，但她恢复过来之前我们可能只能这么做。"
    scene c007_s002_025 with Dissolve(0.25)
    if k_anxiety >= 5:
        k "只要她能。"
    else:
        k "她会的。我知道。"
    j "要是非得这样，我就把劳拉打晕，自己把她扛出去。我不会让她做出伤害自己的事。我向她保证过，她会再见到彼得。而我已经……"
    "在我人生里辜负过一个女人。老实说，连我自己都辜负过。"
    scene c007_s002_026 with Dissolve(0.25)
    k "没、没事的。我知道。我们一起扛。"
    j "我们只能一起。我已经拖得太久了，但我觉得是时候坐下来跟雪莉好好谈谈，怎么把所有人都带出去了。因为我也不能把她丢下。"
    scene c007_s002_027 with Dissolve(0.25)
    k "回头再说。现在，先让自己喘口气。我去看看雪莉需不需要我帮她照看劳拉。"
    j "好。这……这样就行了。我倒是想说需要呼吸点新鲜空气，但那暂时是不在菜单上的选项。"
    k "可惜啊。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_2_1020", transition=Dissolve(1.0))()
    pause
    $ Hide("july_2_1020", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s002_028 with Dissolve(2)
    play ambient shower
    play music insideday2 fadein 2.0
    k "雪莉？劳拉？都没事吧？"
    s "嗨，姑娘。我在。"
    scene c007_s002_029 with Dissolve(0.25)
    s "劳拉没事。她正在享受热水澡。我们花了挺久才把她弄进去，不过等她被拉回当下之后，看起来就还好。你想想今天早上、过去这几天，还有……你懂的。"
    k "她会没事吗？"
    scene c007_s002_030 with Dissolve(0.5)
    s "很难说。我不是精神科医生，虽然我也看过不少。说实话，据我所知我觉得她是解离发作了。这一切对她来说实在太多，她直接「啪一下断片」了。[player_name]确实说过她最近绷得太紧了。"
    s "我是说，我不怪她。如果我想回家见家人，而各种破事一直挡着路，我可能也会崩溃。"
    scene c007_s002_031 with Dissolve(0.25)
    s "我叔叔在他妻子去世后，也差不多经历过同样的事。她很年轻——太年轻了，不该就这么突然死掉——那件事把他击垮了。他就那么站着，嘴里念念有词，站了好久好久。"
    s "有时候他会突然清醒过来，但谁也不知道他花了多久才缓过来。葬礼之后，甚至过了好几个星期，他还会走神。我觉得他再也没完全正常过。"
    scene c007_s002_032 with Dissolve(0.5)
    k "那……那可不乐观。"
    s "是不怎么样，但劳拉和泰迪——我叔叔——不是同一种人。泰迪没有露西姨妈，什么都做不了。没有她他就废了。我跟劳拉也不算很熟，但我感觉她相当能自立。她大概只是需要时间去消化这一切。"
    s "嗯，再加上一点让人心情好的药。可惜这楼里没有更多那种药了。"
    scene c007_s002_033 with Dissolve(0.25)
    k "…"
    scene c007_s002_034 with Dissolve(0.25)
    k "我去看看她需不需要帮忙。"
    s "行行行。我就在附近。"
    stop ambient
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_2_1118", transition=Dissolve(1.0))()
    pause
    $ Hide("july_2_1118", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music insideday fadein 2.0
    scene c007_s003_001 with Dissolve(2)
    "卡莉和雪莉在照看劳拉，我也帮不上什么。所以我决定上三楼看看，能不能把周围看得更清楚些。虽然眼下这事儿不算紧迫——考虑到正在发生的一切——但我还是得收集情报，好把下一步规划得更好。"
    "因为有雾，我看不到下面多少东西。指望附近还停着一辆车，纯属白日做梦。不过周围建筑的轮廓倒是给了我一点思路。要是我在外面多待一会儿，也许能走到其中一栋。"
    scene c007_s003_002 with Dissolve(0.25)
    s "{size=30}喂？！[player_name]？！你在哪儿？求求求你在上面。{/size}"
    j "我在里面，雪莉。"
    play sound doorclose
    scene c007_s003_003 with Dissolve(0.25)
    s "嘿，你果然在。我还希望你没出去。"
    scene c007_s003_004 with Dissolve(0.25)
    j "没有。今天不出。我只做力所能及的事。劳拉她——"
    scene c007_s003_005 with Dissolve(0.5)
    s "卡莉现在在里面陪劳拉，情况还行。还算行吧。大致上过得去。我不打算假装现在的局面有多好，但我想本来可能更糟。不过这么说并不会让过去这几天变好哪怕一点。"
    j "不过还是谢谢你帮忙。多一个人在旁边挺好，万一再发生今天这种事。"
    scene c007_s003_006 with Dissolve(0.25)
    s "听我这段时间观察，「今天这种事」自打雾来了以后发生得可不少。"
    menu:
        "[gr]我们运气一直不太好。":
            j "我们运气一直不太好。不过大家都还在，所以也不算最糟。"
            scene c007_s003_009 with Dissolve(0.25)
            s "也许往后我可以当你的幸运符。"
            menu:
                "那是说我得摸摸你？\n[rgr](雪莉 好感\欲望 +1)":
                    $ s_friend += 1
                    $ s_desire += 1
                    j "那是说我得摸摸你？求好运？"
                    scene c007_s003_010 with Dissolve(0.25)
                    s "只要你出牌够漂亮？当然。*咯咯笑*"
                "希望你是。\n[rgr](雪莉 好感 +1)":
                    $ s_friend += 1
                    j "希望我是。"
        "我们比别人强点。":
            j "我们比别人强点。"
            scene c007_s003_007 with Dissolve(0.25)
            s "哦？怎么说？"
            j "有个人在{i}汉堡店{/i}。我们在洗手间发现他死了。不知道怎么死的，也不知道为什么，只知道他死了。"
            scene c007_s003_008 with Dissolve(0.25)
            s "唔。那可真糟。"
    scene c007_s003_011 with Dissolve(0.5)
    j "所以，趁你在这儿，我得先把有些事挑明，免得以后让你措手不及。你也知道，我们原本是横穿整座城，结果到了这儿。我们一直想赶到医院去，想着救援可能会是直升机降落在楼顶停机坪上。"
    j "这也是劳拉一直这么紧绷的原因之一。她一门心思想把那辆SUV一路开过去。我没那么乐观。事实上，我们走过的距离比我原本估计的还多。"
    scene c007_s003_012 with Dissolve(0.25)
    j "但重点是，我们不会永远待在这儿。食物来源有限，我也没指望有人开着车进来救我们。我不会逼你现在就做决定，但我希望你能跟我们一起走。"
    s "那要是我不想走呢？"
    menu:
        "我没法强迫你。":
            j "我没法强迫你走。我觉得你留下不明智，但你有你自己的理由。而这些理由，迟早你得跟劳拉和卡莉解释。"
            scene c007_s003_013 with Dissolve(0.25)
            s "嗯……"
        "[rd]我会试着劝你别这样。\n[rrd](雪莉 焦虑 +1)":
            $ s_anxiety += 1
            j "我会试着劝你别这样。在那之前，我会想办法解释为什么我觉得待在这儿不是个好主意。我会问你：既然这个地方的一切都撑不下去，你为什么还想留下。但不是现在。今天大概不是我来劝你的好时机。"
            scene c007_s003_013 with Dissolve(0.25)
            s "今天大概压力有点太大。"
        "要是得我把你打晕带走的话……\n[rgr](雪莉 好感 +1)":
            $ s_friend += 1
            j "不知道。真要是得把你打晕带走，我就那么干。我知道卡莉和劳拉不会让我把你留在这儿。所以，要是我不得不把你扛上肩，那就只能这么办。"
            scene c007_s003_014 with Dissolve(0.25)
            s "哦哟~~~ 我承认，这说法我还挺爱听的。"
    scene c007_s003_015 with Dissolve(0.25)
    j "嗯……不管怎样，看来我们还有时间，因为就算我们全都百分之百恢复了，也还有一大堆事要做、要想清楚。比如我们怎么穿过校园。还有，我得给卡莉找件替换外套，再弄个能呼吸的面罩之类的东西。"
    j "还有，给你的东西。我不知道你自己带没带能用的，但手套、帽子、眼镜加呼吸面罩这一套配齐了，出门会好过得多。"
    s "我是按春天和夏天打包的。嗯，本来是只按春天来的，后来我决定上一门暑假的课。反正我没带外套之类的。事实上，我也不知道留在这儿的人里谁带了。"
    scene c007_s003_016 with Dissolve(0.25)
    j "*叹气* 那我可能得想点创意了。"
    j "那，你知道附近这些楼的情况吗？我知道正对面有个男生宿舍。还有别的吗？我就是想着也许能搜刮到点有用的东西。"
    s "当然还有别的宿舍。比如草坪另一边。我知道几条街外有整个宿舍区，但那对你没什么用。不过附近的话……有。你上哈灵顿楼的高层就能看见。"
    scene c007_s003_017 with Dissolve(0.25)
    j "哦，真的吗？太好了，那我可以溜进去看一眼。"
    s "你觉得过去那边安全吗？"
    scene c007_s003_018 with Dissolve(0.25)
    j "那栋楼是空的，所以安全。"
    s "好。不错。"
    scene c007_s003_019 with Dissolve(0.25)
    "我确实没花多少时间在个人层面去了解雪莉。我们刚到这儿的时候，她不太像是想跟我说话。甚至不太想待在我旁边。现在？好多了。我该……"
    menu:
        "问问她。\n[rgr](雪莉 好感 +1)":
            $ s_friend += 1
            scene c007_s003_020 with Dissolve(0.5)
            j "嘿，我们确实还没怎么聊过。如果这不是结识新朋友的最佳方式，我先道个歉。不过我问你几个私人问题，你介意吗？好让我对你的了解不至于只有「你叫雪莉」。"
            s "不介意。只要你不介意我也问你点什么。"
            call c007_shelley_choices from _call_c007_shelley_choices
            call c007_shelley_choices from _call_c007_shelley_choices2
            call c007_shelley_choices from _call_c007_shelley_choices3
            call c007_shelley_choices from _call_c007_shelley_choices4
            call c007_shelley_choices from _call_c007_shelley_choices5
            jump c007_shelley_end
        "以后再说。":
            "现在不是深挖私事的好时机。而且她可能压根不想让我了解她的任何事，这么问只是浪费我们两个人的时间。我感觉她已经在往门口挪了。"
            scene c007_s003_030 with Dissolve(0.5)
            s "这……呃……挺有意思的，不过我该回去了。得去看看卡莉需不需要人搭把手照顾劳拉。"
            j "行行行。谢谢你来帮忙，我们晚点再聊。"
            scene c007_s003_031 with Dissolve(0.25)
            s "我可记着呢。"
            jump c007_shelley_end
label c007_shelley_choices:
    menu:
        "你有兄弟姐妹吗？" if ch7qs_1 == False:
            $ ch7qs_1 = True
            j "你有兄弟姐妹吗？你提过你家人住在新泽西。"
            scene c007_s003_021 with Dissolve(0.5)
            s "没有。我是独生女。爸妈在商量再要一个，不过这时候才生第二个，可能有点晚了。"
            j "你担心他们吗？你家里人？"
            scene c007_s003_022 with Dissolve(0.25)
            s "嗯。有一点吧。不过跟你一样，我觉得这边的事仅限于这边，所以他们在家里大概没事。我妈可能已经急疯了，但那我也无能为力。已经是两个问题了，所以你欠我一个。"
            j "好吧，问吧。"
            scene c007_s003_023 with Dissolve(0.25)
            s "那你家人呢？"
            j "我也是独生女。我父母住在卡罗来纳东边，靠近边境。我们不怎么来往。所以我确实担心，但跟家里有点疏远的时候，这种「担心有多少」实在很难量化。"
            s "我能理解。我当初跑去外州上大学是有原因的，老兄。"
            return
        "感情上有没有什么重要的人？" if ch7qs_2 == False:
            $ ch7qs_2 = True
            scene c007_s003_024 with Dissolve(0.5)
            j "不想问得太私密，但……你感情上有没有什么重要的人？比如男朋友。或者女朋友。"
            s "现在没有。我不太想在自己人生最黄金的年纪就把自己拴住。*咯咯笑* 你呢？"
            j "最近刚离婚。"
            scene c007_s003_025 with Dissolve(0.25)
            s "这可不算回答。更像是在描述一种状态。哪怕你正在走完离婚这套流程，也可以同时惦记着别的姑娘。人们老这么干。"
            j "那就是离异、目前单身。*轻笑*"
            return
        "你是学美术的？" if ch7qs_3 == False:
            $ ch7qs_3 = True
            scene c007_s003_026 with Dissolve(0.5)
            j "我听说你是学美术的。是这样吗？"
            s "对，我小时候画油画、素描都挺好的。大概是我们那一届最强的，所以就想过去专门学这个。我爸不太高兴。他老说画画早就不再是正经工作了，不过也许他们是想让我自己撞明白。"
            scene c007_s003_027 with Dissolve(0.25)
            j "我相信你会找到适合自己的路。"
            s "总比去拿个教师资格证强。你是哪个学校？念的学位？我姑且这么假设。"
            scene c007_s003_028 with Dissolve(0.25)
            j "北卡州立。不过工商管理的学位眼下好像没什么用。"
            return
        "你在校内有朋友吗？" if ch7qs_4 == False:
            $ ch7qs_4 = True
            scene c007_s003_029 with Dissolve(0.5)
            j "雾来的时候，你在校内有没有朋友？我知道现在是暑期学期，也许你认识的人都走了。"
            s "我跟留在宿舍的那几个女生算是认识，但我朋友基本都回家过节了。有两个住在城里，所以我有点担心他们没事吧。除了劳拉和卡莉，你还有别的朋友或者同事吗？"
            scene c007_s003_030 with Dissolve(0.25)
            j "大多已经不在城里了。奥蒂斯因为生病缺了最后几天班，所以我不知道他怎么样了。我想我们也没那么熟，不然我也不会现在才想起他。"
            return
        "我觉得今天就到这里吧。[lbl](选择最后一个)":
            scene c007_s003_031 with Dissolve(0.5)
            j "我觉得今天问得够多了。"
            if ch7qs_1 == True and ch7qs_2 == True and ch7qs_3 == True and ch7qs_4 == True:
                scene c007_s003_034 with Dissolve(0.25)
                $ s_friend += 1
                $ s_trust += 1
                s "好，我还有一个想问的，但你一直没给我个合适的口子。"
                j "好吧。问吧。"
                scene c007_s003_035 with Dissolve(0.25)
                s "你有没有对她们其中哪个下手？做点床上那档子事缓解压力？靠，哪怕只是摸摸捏捏也行。又不用真的到「藏起黄瓜」那一步。"
                #j "No. Nothing like that's happening with us. Laura's married, and Kallie is engaged."
                j "劳拉已婚，卡莉订婚了。"
                scene c007_s003_036 with Dissolve(0.25)
                s "真的？因为我听说，劳拉那老公有点混账，她挺需要人疼的。还有，让我这么说吧：要是你像对卡莉那样救了我，我大概已经开始练怎么用花体字写「雪莉·[player_lastname]夫人」了，顺便琢磨我们的孩子该叫什么名字。*咯咯笑*"
                j "好吧，嗯，也许他们生活里还有别的事，跟我这样的人纠缠并不是个好主意。"
                scene c007_s003_037 with Dissolve(0.25)
                s "你说的是就是。嗯，能聊一次正常话题真好。这还挺有意思的，不过我该回去了。得看看卡莉要不要人搭把手照顾劳拉。"
                scene c007_s003_032 with Dissolve(0.25)
                j "行行行。谢谢你来帮忙，我们晚点再聊。"
                s "我可记着呢。"
            else:
                s "不错。是啊，能聊一次正常话题真好。这还挺有意思的，不过我该回去了。得看看卡莉要不要人搭把手照顾劳拉。"
                scene c007_s003_032 with Dissolve(0.25)
                j "行行行。谢谢你来帮忙，我们晚点再聊。"
                s "我可记着呢。"
            jump c007_shelley_end
label c007_shelley_end:
    play sound doorclose
    scene c007_s003_033 with Dissolve(0.5)
    "嗯，至少我跟她摊开谈了。她看起来不像坏人。只是不成熟，也许还有点心不在焉。我希望她能回心转意跟我们一起走，因为不然的话，那是一场我不知道自己有没有力气打完的仗。"
    scene blank with Dissolve(2)
    scene c007_s004_001 with Dissolve(2)
    k "*叹气*"
    "{color=#ffcccc}至少劳拉看起来「好些了」，但我不喜欢她那样发作了。这不是说她不能发作、或者不被允许发作。天知道，我觉得我们每个人都压力很大。我们居然都还没崩，算是个奇迹。{/color}"
    scene c007_s004_002 with Dissolve(0.25)
    "{color=#ffcccc}可是劳拉一直是个那么坚强稳当的人。我仰望的人。我……我想我现在依然如此。我不该把她捧得那么高。这一切变得太难以承受，也是没问题的。只要不再恶化就行。{/color}"
    "{color=#ffcccc}希望休息几天能有用。我知道我自己也很需要。{/color}"
    scene c007_s004_003 with Dissolve(0.5)
    "{color=#ffcccc}还有[player_name]？他那么拼，就为了把这一切勉强撑住。我希望他不必觉得非撑不可，但考虑到我受了伤、劳拉状态又不好，他还能指望谁呢？雪莉？我喜欢她，可她还是怕得除了躲在这儿什么都不肯做。{/color}"
    scene c007_s004_004 with Dissolve(0.25)
    "{color=#ffcccc}可是，[player_name]把劳拉带回来时照顾她的那个样子……我……原来有人纯粹关心你的安危，是这种感觉吗？就是单纯地为另一个人担心？他把我带回来的时候也是那样的吗？我那段时候昏得太厉害，想不太起来了。{/color}"
    scene c007_s004_005 with Dissolve(0.25)
    if ch6_kallie_sex == "yes":
        "{color=#ffcccc}如果是的话……那我们前天晚上做的事……感觉是对的。我好久好久以来第一次这么开心。就算我本来不该那么做。但我想要，他也想要我，然后……{/color}"
        "{color=#ffcccc}我大概不该再来一次。就算……{/color}"
        k "*叹气*"
    else:
        "{color=#ffcccc}如果真是那样……我……我不知道。{/color}"
    scene c007_s004_006 with Dissolve(0.25)
    "{color=#ffcccc}好吧，我的皮肤看起来好多了。只有几块地方还有点红，像长了青春痘。呃，我可不想又变回一副青少年的样子。那时候我可尴尬了。{/color}"
    "{color=#ffcccc}不过，我之前那些担心会留疤的焦虑，好像也没什么道理。即便它确实让我更清楚那些灼烧者有多危险。{/color}"
    scene c007_s004_007 with Dissolve(0.25)
    "{color=#ffcccc}我该回去了，好歹确保有人在劳拉身边。她说自己好些了，但我对这种情况还是有点不安。我不擅长处理别人的情绪，可我也不想当个烂朋友。{/color}"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_24_748", transition=Dissolve(1.0))()
    pause
    $ Hide("june_24_748", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s004_008 with Dissolve(2)
    play music nightmain fadein 2.0
    "嗯，今天完全不是我预想的走向。我本来就不擅长做计划。更像是「到了再说、见招拆招」那种人。卡莉还在恢复，我想我正好能对这一带做一次更长时间的搜索。哪怕只是对接下来能怎么往前走有个更清楚的想法。"
    "甚至跟劳拉一起把哈灵顿楼彻底搜一遍，因为我有种感觉这条路是对的。"
    scene c007_s004_009 with Dissolve(0.25)
    "可是劳拉……她这么一发作——这么形容吧——真的把那些计划全打乱了。这我完全没料到，尽管我本该更意识到这种可能性。她这几天确实很挣扎，而且最后失控了。"
    scene c007_s004_010 with Dissolve(0.25)
    "劳拉就像一根橡皮筋，被拉得太紧了。每一件新发生的事（我被喷雾喷到、卡莉受伤、SUV抛锚，等等）都让她绷得更紧。我只能希望她刚才那短暂的解离就是极限，给她时间她会好起来。"
    "因为除了给足耐心和休息，我不知道还能做什么。我讨厌这样像保姆一样盯着她，可我不想把她一个人丢着。万一她再发作怎么办？总得有人拦着她别伤害自己。"
    scene c007_s004_011 with Dissolve(0.5)
    l "[player_name]……"
    j "嘿，劳拉。对，我在这儿。"
    scene c007_s004_012 with Dissolve(0.25)
    l "我……我是不是很糟糕？"
    menu:
        "[rd]你刚才不在一会儿。\n[rrd](劳拉 焦虑 +1)":
            $ l_anxiety +=1
            j "你刚才走开了一会儿。但我们现在都在这儿，这才是最重要的。"
        "[gr]没关系。":
            j "没关系。我们都压力大得很，所以你那样一下也没什么。你应得的。"
    scene c007_s004_013 with Dissolve(0.25)
    l "我……*抽鼻子*"
    j "你不是一个人，劳拉。我们都在这儿陪你。我，卡莉。就连雪莉也是。所以你要知道，你身边有人在乎你。"
    scene c007_s004_014 with Dissolve(0.25)
    l "我们会死在这儿，对吧？"
    j "我可没打算死。也没打算让你们任何一个人出事。所以，不会。眼下我们只是在重整，想清楚怎么继续往前走。就这些。"
    scene c007_s004_015 with Dissolve(0.25)
    l "我、我需要……需要……"
    j "你需要放轻松，好吗？我不是心理医生也不是大夫，但我要说：现在这个状态下，你除了让别人做主以外什么都做不了。我知道你讨厌这话，但这是事实。"
    scene c007_s004_016 with Dissolve(0.5)
    j "而且不只是我。卡莉也是。她聪明又能干，你现在得让她当这个主。我不是要把你当小孩，但真有必要，我会这么做。"
    l "不想……想一直待在这儿……永远……"
    scene c007_s004_017 with Dissolve(0.25)
    j "不会的。但你得让我——让我们所有人——一起把事情理清楚。好吗？"
    l "……好……好累……"
    scene c007_s004_018 with Dissolve(0.25)
    j "那你尽管休息。你要是需要什么，我们会有一个人在旁边。"
    scene c007_s004_019 with Dissolve(1)
    j "哦，卡莉。多久了——"
    k "我不想打断。她是……"
    scene c007_s004_020 with Dissolve(0.25)
    j "我想她睡着了。我本来打算等你来了再走。我现在该走了。把你们两个留在这儿。"
    k "她会没事吗？"
    scene c007_s004_021 with Dissolve(0.25)
    j "走着瞧吧。她好像多少知道自己发生了什么，这是个好兆头。"
    k "你说就是。"
    scene c007_s004_022 with Dissolve(0.25)
    j "那我先出去，让你至少有点独处的时间。我知道你大概也需要一点「自己的时间」。"
    if k_friend >= 12:
        scene c007_s004_024 with Dissolve(0.5)
        k "嘿。我……"
        j "嗯？怎么了？"
        scene c007_s004_025 with Dissolve(0.25)
        k "没什么……我只是……"
        scene c007_s004_026 with Dissolve(0.25)
        k "今天有点疯狂……太闹腾了。就这些。谢了，晚安。"
        scene c007_s004_027 with Dissolve(0.25)
        j "晚安，我就在隔壁，你需要什么就跟我说。"
        k "好。"
        scene blank with Dissolve(2)
        scene c007_s004_028 with Dissolve(2)
        if ch6_kallie_sex == "yes":
            "我会觉得有点奇怪，但也许她是想多聊点昨晚的事，结果因为劳拉在房间里又作罢了。没关系。以后还会有单独相处的时间。"
        else:
            "我会觉得有点奇怪，但也许她只是被劳拉那场崩溃吓到了。她要是以后想聊，我就随时奉陪。"
    else:
        k "今天有点疯狂……太闹腾了。谢了，晚安。"
        scene c007_s004_023 with Dissolve(0.25)
        j "晚安，我就在隔壁，你需要什么就跟我说。"
        k "好。"
    scene blank with Dissolve(2)
    scene c007_s004_029 with Dissolve(2)
    "现在大家都安顿下来准备睡了，我也开始迅速撑不住。背和肩膀疼成这样，我想我这一整天都绷得死紧。"
    "而且对我们逃出去真正有用的事一件也没做成，所以这算是白过的一天。但我不能怪劳拉。自从第一天出现在办公室，她就勉强撑着没垮。"
    scene c007_s004_030 with Dissolve(0.25)
    "往后我们得一直留意着她。她不会喜欢被当成易碎的人，但让她回到儿子身边，比她怎么看我重要多了。"
    if l_sex >= 2:
        "至于跟她的那些胡搞？到头了。那也没让这一切变好，对吧？"
    scene c007_s004_031 with Dissolve(0.25)
    "至少卡莉看起来已经恢复原样了。眩晕已经过去，皮肤也差不多正常了。"
    if ch6_kallie_sex == "yes":
        "昨晚那一场？我们还没机会谈。事实上，感觉我们都在装作它根本没发生过。但听她说了那些，我不会忘记她和安德鲁的事，哪怕我能做的只是别让她回到那种生活里去。"
    scene c007_s004_032 with Dissolve(0.25)
    "至少我提了让雪莉一起走这个话题，哪怕没谈出结果。现在别的事太多了。而且她对我忽冷忽热。前一分钟还在抓狂，下一分钟又跟我调情。"
    "一天之内要处理的事太多了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_3_815", transition=Dissolve(1.0))()
    pause
    $ Hide("july_3_815", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s005_001 with Dissolve(2)
    play music morning fadein 2.0
    "天刚亮就醒了，其实我并不需要这么早。说起来挺惨的，明明可以赖床，我就是做不到。而且没有空调，一醒来就一身汗、黏糊糊的，更不好受。谢天谢地还有自来水。"
    scene c007_s005_002 with Dissolve(0.25)
    "我该觉得自己幸运。通常到了夏天这个时候，这儿已经热得受不了了。也许是雾削弱了最毒的那部分暑气。"
    scene c007_s005_003 with Dissolve(0.25)
    "那今天打算怎么安排？先去看看劳拉恢复得怎么样。之后呢？我该再回哈灵顿楼做一次更全面的搜索。再查一下附近的楼，因为给卡莉和雪莉弄装备很重要。"
    scene c007_s005_004 with Dissolve(0.5)
    "迟早我得认真努力，让雪莉接受「她必须跟我们一起走」这个想法。就算这对她是个强人所难，我也得把卡莉拉进来一起说服她。"
    j "哦，劳拉。早上好。"
    scene c007_s005_005 with Dissolve(0.25)
    l "[player_name]……"
    j "你今天早上感觉怎么样？"
    scene c007_s005_006 with Dissolve(0.5)
    l "还活着。这大概已经比我应得的多了。"
    j "你昨天只是有点失控。可以理解。"
    scene c007_s005_007 with Dissolve(0.25)
    l "不只是失控。我已经跟那些入侵性的念头打了一阵子，而且正在输。我……我只是……我控制不住。我一直在想基思每一次离开的时间稍微久一点的时候。每次我纳闷「他怎么这么久才回来？」的时候——那会不会就是他跑去偷情了？"
    scene c007_s005_008 with Dissolve(0.25)
    l "几年前有一次家族聚会，他和我的表姐露伊丝有一阵子不见人影，当时我什么也没多想。可要是他们是去上床了呢？我忍不住在脑子里把整段婚姻重播一遍又一遍，找出越来越多他可能不忠的时刻。"
    scene c007_s005_009 with Dissolve(0.25)
    l "而我只想冲到他面前对着他大吼大叫。在这等着简直从内部把我折磨死。失去的每一秒，都是他跟那个跟他一起上班的婊子上床的又一个机会。"
    "靠，劳拉在这条路上真的越走越黑了。比我跟南希那会儿崩得还厉害。这里面有多少是她自己想象出来的、其实根本没这么糟？在查不出真相的情况下，她正用一种恶性的方式把这些东西往心里堆。"
    j "听着，我不会替基思说话，但我觉得你在这件事上烂掉了。你得把心思放在平平安安回到彼得身边。"
    scene c007_s005_010 with Dissolve(0.25)
    l "彼得？我……我该怎么跟他解释？"
    j "他已经是大孩子了，劳拉。我敢肯定他能理解。他大概也有过不止一两个经历父母离婚的朋友。"
    l "他不该被迫承受！基思本该……"
    scene c007_s005_011 with Dissolve(0.25)
    j "我知道。我知道。他本该做很多事。你有理由生气。但现在，我要你专心做好你能做的，完好无损地回到你儿子身边。别的都先放下。"
    l "我、我……我做不到……我会试试。试着去对抗那个冲动……"
    scene c007_s005_012 with Dissolve(0.5)
    k "劳拉？哦，你在这儿。我起来的时候发现你不在。"
    scene c007_s005_013 with Dissolve(0.25)
    j "没事。我们就是在说话。"
    "我故意把话带过去，好让劳拉保住一点体面，也让卡莉别太担心劳拉正处在一种非常脆弱的状态——一个一两个坏冲动就可能把她推去做有害的事的状态。基思运气好，他人不在这儿，看不到她可能会对他做什么。"
    scene c007_s005_014 with Dissolve(0.25)
    l "我、我要去上个厕所。没事。至少这个我还能做到。"
    j "行行行。我该出去了，让你们俩至少有点隐私。我可不觉得把这里变成男女混用浴室是楼里任何人想要的。"
    scene c007_s005_015 with Dissolve(0.25)
    "我不知道卡莉出现是好是坏。它缓和了紧张气氛，但也让我没能跟劳拉谈出任何进展，而我真的觉得跟她好好做些工作很有必要，哪怕我根本算不上什么心理医生。也不太擅长处理情绪。"
    scene blank with Dissolve(2)
    scene c007_s005_016 with Dissolve(2)
    "如果她一边解离，一边过度执着于基思和逃出去这件事，她有可能直接崩掉。真的，不是说着玩的，彻底崩掉。那会是什么样？"
    s "唔嗯嗯~~~ *打哈欠* 早。"
    scene c007_s005_017 with Dissolve(0.25)
    j "早啊。今天挺忙的，大家都已经起来了。"
    s "看来大家个个都精神抖擞。我知道我是，但那只是因为你这条内裤几乎没往身上裹多少。"
    menu:
        "你这打扮真是一点都不给人留想象空间。\n[rgr](雪莉 好感\欲望 +1)":
            $ s_friend += 1
            $ s_desire += 1
            j "你这打扮真是一点都不给人留想象空间。"
            scene c007_s005_018 with Dissolve(0.25)
            s "确实没给人留。但你不想想的话，也不用费什么脑子。*咯咯笑*"
            scene c007_s005_019 with Dissolve(0.25)
            s "回见！"
            "天哪，她真该学会挑时机。她心情变好是好事，可我今天已经没有那个情绪余量了。"
        "我该走了。":
            scene c007_s005_020 with Dissolve(0.25)
            j "我该走了。"
            s "哎哟~~~ 别这么快就走嘛。*咯咯笑*"
            "她心情变好是好事，可我今天已经没有那个情绪余量了。"
    scene blank with Dissolve(2)
    scene c007_s005_021 with Dissolve(2)
    "大伙儿晃晃悠悠地适应新的一天，过了一个多小时（为什么不呢？我们又不急着去哪儿），我觉得自己状态还行，就又进了哈灵顿楼。劳拉吃了点东西、抿了几口咖啡，坐在沙发上默默望着远处发呆。"
    scene c007_s005_022 with Dissolve(0.5)
    "我跟她说话时她没说什么，但能问出来的那点东西，比昨天有条理多了。"
    scene c007_s005_023 with Dissolve(1)
    "尽管我对她现在的精神状态很不安，但我耗不起再浪费一天。我们的食物来源正迅速减少。很快我们就会不管愿不愿意，都被迫上路。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_24_1020", transition=Dissolve(1.0))()
    pause
    $ Hide("june_24_1020", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s005_024 with Dissolve(2)
    play music school fadein 2.0
    "反正我不打算出去，也不打算往更深处走，我就没穿装备。不过面罩和手套还是塞在口袋里以防万一。我带上了斧头，万一得硬闯进哪个教授的办公室。"
    scene c007_s005_025 with Dissolve(0.5)
    if k_friend >= 12 or k_sex >= 1:
        k "[player_name]。你在这儿啊。我正想找你说两句。"
    else:
        k "嘿，你在这儿。我正想找你说两句。"
    j "在我去哪儿之前？嗯，我打算进去待一会儿。你来了正好。我正想找个人在我过去的时候帮忙盯着。"
    scene c007_s005_026 with Dissolve(0.5)
    k "可是，我们真需要吗？我是说，得有人在这儿放哨吗？楼里又没有雾，不用把门堵上。而且你说过那边没人，对吧？"
    j "我猜是。我还真没想过。我一直把每个入口都当成「必须挡住危险」来对待，纯粹是警觉过度。不过晚上我还是想把它堵上。"
    scene c007_s005_027 with Dissolve(0.25)
    k "我、我能理解你为什么想这么做。至少睡觉的时候能安心点。"
    j "行，好，那我在那边待几个小时。所以——"
    scene c007_s005_028 with Dissolve(0.25)
    k "我要跟你一起去。你只是去找我们能用的东西，对吧？我觉得多一个人去会更有帮助。两个人四只眼睛，总比一个人能注意到些东西。而且你说过那边没人、没危险。"
    j "从务实角度看，是的。"
    scene c007_s005_029 with Dissolve(0.25)
    k "好。我马上回来。我会告诉劳拉和雪莉我们去哪儿。"
    j "让雪莉……"
    scene c007_s005_030 with Dissolve(0.25)
    k "陪劳拉。我知道。就……等我回来，好吗。"
    j "好。"
    scene c007_s005_031 with Dissolve(0.5)
    "我早该料到的。卡莉一直拼命想帮上忙，近乎执拗地想帮。现在她看起来已经恢复原样了，我还真没法把她劝退。我更不可能叫上劳拉一起去。"
    if ch6_kallie_sex == "yes":
        "这会是自那晚以来我们第一次单独相处。我该主动提点什么，还是让她想说的时候自己说？我讨厌把她当成娇贵易碎的人，可也许她压根不想承认我们做过什么。就把它留成一段她不必承认真的发生过的记忆吧。"
    scene blank with Dissolve(2)
    scene c007_s006_001 with Dissolve(2)
    "我们穿过连廊的那段路走得很安静、很慢。尽管我已经保证过了，我敢肯定卡莉还是有点紧张……"
    scene c007_s006_002 with Dissolve(0.5)
    k "你确定这里面安全吗？"
    j "足够安全，但我们确实得留意周围。"
    scene c007_s006_003 with Dissolve(0.5)
    k "哇。我……天哪，我感觉像个游客。"
    scene c007_s006_004 with Dissolve(0.5)
    k "全是雾。*呻吟* 那边还有更多楼。"
    j "是别的教学楼。我上次进来时，走廊尽头通向下一栋楼的那扇门是锁着的。"
    scene c007_s006_005 with Dissolve(0.25)
    k "那也就是说，我们可以穿过去到下一栋？然后再下一栋？"
    j "我也是这个打算。我不知道那些楼是不是跟这栋一样安全，所以我正努力给你和雪莉弄外套。还要面罩，还有雪莉需要的其他东西。"
    scene c007_s006_006 with Dissolve(0.25)
    k "她会来吗？"
    j "我已经跟她提过了。她好像还没拿定主意，所以我得加大力度说服她。只是不是现在。"
    scene c007_s006_007 with Dissolve(0.25)
    k "……好吧。"
    if k_friend >= 13 or k_friend >= 10 and k_desire >= 6:
        scene c007_s006_008 with Dissolve(0.25)
        $ renpy.pause ()
    scene blank with Dissolve(2)
    scene c007_s006_009 with Dissolve(2)
    k "这是我第一次进大学校园。"
    j "你上的是……你是远程上课。抱歉，我一时脑子没转过来。"
    scene c007_s006_010 with Dissolve(0.25)
    if k_sex >= 1:
        k "对，安德鲁说上网课更方便。我想他是不想让我真的跑去学校。我连一次校园参观都没参加过，所以这一切对我来说都是全新的。"
        "又是另一种控制手段。到这一步，这家伙简直就是个阴险的混蛋。"
    else:
        k "对，我连一次校园参观都没参加过，所以这一切对我来说都是全新的。"
        j "嗯，不过这样大概不是体验它的最佳方式。暑假期间空着。现在没人在这儿学任何东西。也没有任何能让你拿到学位的东西。"
    scene blank with Dissolve(2)
    scene c007_s008_001 with Dissolve(2)
    s "好吧，这简直是有史以来最烂的电视节目。而且所有台都在播。*咯咯笑*"
    scene c007_s008_002 with Dissolve(0.25)
    s "不过我猜你喜欢，对吧？"
    l "还……还行……"
    scene blank with Dissolve(2)
    scene c007_s006_011 with Dissolve(2)
    j "我在这儿看不清什么。雪莉说这边还有更多宿舍。可能要多走一会儿才能到。"
    k "她跟我说，她那门美术课的教室视野不错。她在这栋楼里有一间工作室教室。"
    scene c007_s006_012 with Dissolve(0.5)
    j "哦，真的吗？我前几天好像看到过类似的东西。我们去找找看吧。"
    scene blank with Dissolve(2)
    scene c007_s008_003 with Dissolve(2)
    s "好，你需要什么吗？我有点饿，但不是饿这里有的东西。一直都这样，不是吗？你买一堆吃的，等你真想吃点什么的时候，偏偏是想吃没买的那些。*咯咯笑*"
    scene c007_s008_004 with Dissolve(0.25)
    s "劳拉？"
    l "我……我什么都不要。"
    scene c007_s008_005 with Dissolve(0.25)
    s "嗯，等你想吃了跟我说。"
    l "呃，基思去哪儿了……基思在哪儿？"
    scene c007_s008_006 with Dissolve(0.25)
    s "基思？我猜你是说[player_name]。他和卡莉进哈灵顿楼四处看看去了。"
    l "我……好、好吧……"
    scene blank with Dissolve(2)
    scene c007_s006_013 with Dissolve(2)
    k "嗯？这是雪莉的画室？"
    j "对，你闻得到颜料味。再多的清洁剂也盖不住颜料和溶剂的气味。"
    scene c007_s006_014 with Dissolve(0.5)
    k "我们该告诉雪莉，我们可以不费事就走到这儿。她也许会想来这儿。就为了看看让人安心、熟悉的东西。"
    "主意不坏，但我们不能骗自己以为这里完全安全。这种愚蠢我已经上当太多次了。"
    scene c007_s006_015 with Dissolve(0.5)
    k "嗯……"
    "侧间里什么都没有。或者说，没什么有用的。基本都是美术用品。"
    scene c007_s006_016 with Dissolve(0.25)
    j "好，又是雾。住英格兰就是这样吗？如果是……那也有点名不副实。"
    scene c007_s006_017 with Dissolve(0.5)
    "她穿的那身。或者说那件上衣。她穿着真他妈可爱。我想对她来说，难得能穿一次既不实用也不功能性的东西，应该挺舒服的。"
    scene c007_s006_018 with Dissolve(0.25)
    k "下面。我能看到院子。虽然不太清楚，但能看到。"
    j "好，那不错。我觉得男生宿舍在那边，所以我再往前走一段就能到。大概四五十码。我不太会估算距离，但看起来做得到。"
    scene c007_s006_019 with Dissolve(0.25)
    k "比我们从SUV开到这儿那段路还短。"
    j "确实。虽然我会在外面待得更久，但还算撑得住。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c007_s008_007 with Dissolve(2)
    s "呼。好吧，我憋得够久了。"
    scene c007_s008_008 with Dissolve(0.25)
    s "我马上回来。得去趟洗手间。"
    l "{size=30}好。{/size}"
    play sound doorclose
    scene c007_s008_009 with Dissolve(0.5)
    $ renpy.pause ()
    scene c007_s008_010 with Dissolve(0.5)
    $ renpy.pause ()
    play music insidedark fadein 2.0
    scene c007_s008_011 with Dissolve(0.5)
    $ renpy.pause ()
    scene blank with Dissolve(2)
    scene c007_s008_012 with Dissolve(2)
    $ renpy.pause ()
    play sound doorclose
    scene c007_s008_011 with Dissolve(0.5)
    s "劳拉？你没事吧，姑娘？"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c007_s006_020 with Dissolve(2)
    play music school fadein 2.0
    "我本来打算把这片地方彻底搜一遍，但一旦开始四处乱逛，感觉更像是在随便参观。想到这意味着卡莉得到了她以前被剥夺的东西，我不想打击她那份好奇探索的热情。"
    scene c007_s006_021 with Dissolve(0.5)
    "也不全是白费；我记下了几个办公室，之后可以再回来看看。这趟完全没白来。事实上，能有这么一小段只有我们两个人的时间挺好的。我看到了卡莉最本真的样子：年轻、好奇、安静。"
    scene c007_s006_022 with Dissolve(0.5)
    "有一阵子，我一直在权衡要不要回去的利弊。再多待几分钟也没坏处吧？哪怕我被那种「必须负责」的焦虑折磨着。"
    scene c007_s006_023 with Dissolve(0.5)
    j "*叹气* 好吧，我们大概该回去了。"
    "我讨厌自己这么想，但她在旁边的时候，我确实没做成多少事。她忙着像游客一样体验一件以前没机会体验的事，而我既是导游又是保镖。"
    scene c007_s006_024 with Dissolve(0.5)
    k "呃……[player_name]，跟我来一下。拜托。我想跟你谈谈。"
    j "我们在这儿说就行。"
    scene c007_s006_025 with Dissolve(0.25)
    k "私下说。"
    j "就我们俩。这儿没别人。我真想不出还能有多私密——"
    scene c007_s006_026 with Dissolve(0.25)
    k "就这么……在外面，感觉好奇怪。拜托啦~~~"
    j "好吧。去哪儿？"
    scene c007_s006_027 with Dissolve(0.25)
    k "这间教室就行。"
    j "随你。"
    scene blank with Dissolve(2)
    scene c007_s007_001 with Dissolve(2)
    j "好。看起来他们还没把这间搬空完。怪了。"
    k "对吧。我想是吧。"
    scene c007_s007_002 with Dissolve(0.25)
    j "来，我先把这个放下。我真不知道消防员是怎么扛着这玩意儿走那么久的。"
    if ch6_kallie_sex == "yes":
        scene c007_s007_003 with Dissolve(0.25)
        k "那么，呃……"
        j "嗯？你还好吗？头啊、皮肤啊，都还好吧。你的皮肤看起来不错。"
        scene c007_s007_005 with Dissolve(0.5)
        k "我好多了，但我想说的是……"
        scene c007_s007_025 with Dissolve(0.25)
        k "那天晚上我们做的事。"
        j "哦？呃，对。我想我们确实该谈谈这个。昨天劳拉崩溃那一场，加上我不想让别人知道，我就一直忍着没说。而且我也不确定你是不是想干脆装作没发生过。"
        scene c007_s007_026 with Dissolve(0.25)
        k "我、我不……*叹气* 还是别提比较好。看看我们现在的处境，那件事好像也没那么重要。但别以为我不领情。"
        scene c007_s007_027 with Dissolve(0.25)
        k "说实话，我有一部分还希望早上醒来时你在我旁边。但我们不能装作这很正常。哪一点都不正常。等我们离开{i}这儿{/i}以后，有太多事等着我们去做。也有太多要面对。"
        j "比如把你从安德鲁身边带走？"
        scene c007_s007_008 with Dissolve(0.25)
        k "对。"
        j "这就是会发生的事。你明白的，对吧？我还没来得及跟劳拉谈这件事——这是有原因的——但我敢肯定她会同意我。真要是得把你送上回家的飞机，我们就送。"
        scene c007_s007_007 with Dissolve(0.25)
        k "谢谢。我……我会需要你们俩帮我撑住的，因为我觉得自己使不出力气去反抗，哪怕我心里再清楚应该反抗。他知道怎么让我觉得自己有多渺小。"
        scene c007_s007_009 with Dissolve(0.25)
        k "我只是……我简直太没用了……我觉得自己蠢透了、还……*抽鼻子*"
        scene c007_s007_010 with Dissolve(0.25)
        j "没事的，卡莉。你不蠢，也不弱。那些话是一个施虐者用来把你钉在原地的说法。你现在跟一群在乎你、希望你平安的人在一起。"
        "她在我怀里哭，我们就这么站了好一会儿。别看她自己觉得那么虚弱渺小，她却紧紧地抱住了我。"
        scene c007_s007_028 with Dissolve(1)
        k "[player_name]，我不知道我们会怎样。不知道要是能活下来，我们的生活会变成什么样。但是……"
        scene c007_s007_029 with Dissolve(0.25)
        k "我只是想让你知道，我越来越喜欢你了。抱歉，这话听起来不太对。我……自从我们被困在办公室以后，我越来越了解你，我觉得我们更亲近了。"
        j "既然我们确实睡过了，我希望是这样。但你不是第一个「上完就忘」的人。跟陌生人来一发这种关系本来就有。"
        scene c007_s007_030 with Dissolve(0.25)
        k "我不是……我不觉得自己是那种人。我可能很难弄清楚自己对一件事、对一个人是什么感觉。很难给我脑子和心里说的话找准位置。"
        scene c007_s007_031 with Dissolve(0.25)
        k "我知道自己可能是因为跟某人待得多了，就更容易跟他亲近，可所有人不是都这样吗？我以前怕自己就是有这方面的毛病，因为当初我觉得自己应该留在安德鲁身边，就是出于这个原因。但是……"
        j "但现在你意识到，是他在让你依赖他？从而逼你对某些事产生某种感觉？"
        scene c007_s007_032 with Dissolve(0.25)
        k "我想是吧。而你……你并没有做这种事。我知道你是在试着保护我。还有劳拉。所以不一样。"
        j "我也会这么说。在最近之前，我只把你当成同事。现在？我会说我们是朋友，甚至更进一步。时间久了，我们可以更亲近。一起挺过这一切，会给我们之间一种我认为什么都摧不毁的联结。"
        scene c007_s007_033 with Dissolve(0.25)
        k "我……我希望如此。希望更亲近。我只是想试着跟一个不把我当所有物的人在一起。"
        j "我无法想象会有这种事，但是……"
    else:
        scene c007_s007_003 with Dissolve(0.25)
        k "嘿，呃……[player_name]，我得跟你说件事。我跟劳拉聊的那些，她有跟你提起什么吗？"
        j "没有。不过你也知道，劳拉最近有点绷得太紧，我们没太多时间随便聊天。出什么事了？"
        scene c007_s007_004 with Dissolve(0.5)
        k "*叹气* 我之前——在办公室的时候——跟劳拉聊过我的感情状况，然后我突然意识到有什么不对。非常不对。我觉得劳拉问的那些问题真的让我开始怀疑一切。让我意识到一些我可能一直没察觉到的事。"
        k "我觉得……我觉得我和安德鲁之间有问题。他比我大那么多，这本来不该是问题，但当我开始回想我们相识的经过，它听起来越来越不像一段浪漫故事，越来越像是他是个捕食者。"
        scene c007_s007_005 with Dissolve(0.25)
        k "我以前没什么恋爱经验。我……不是个爱社交的女孩。所以我以为我们之间发生的一切都是正常的。但我现在明白，他在让我依赖他——甚至早在我们搬到另一个州之前就是——还基本上把我跟家人切断了。"
        k "跟他分开的每一天，我都更清楚那对我没有好处。我想能跟父母——跟兄弟姐妹——说话时他不在旁边盯着。我想见他们的时候，他不用在我背后盯着看。"
        scene c007_s007_006 with Dissolve(0.25)
        k "我试过把他的行为一笔带过。我想替他找借口，因为如果留下来，就等于承认我没本事找到别人。"
        j "所以你才会问那个「因为对方在身边就觉得跟对方在一起」的问题？还有那么沉迷于手机？"
        scene c007_s007_007 with Dissolve(0.25)
        k "也许吧。我……一开始只是害怕联系不上。我也想听到家人的消息，但后来我意识到，那其实是因为「我应该报个到」这种期待在驱使我。"
        scene c007_s007_008 with Dissolve(0.25)
        k "他把我跟所有人都隔开了。把我搬到这里。告诉我不可能找到更好的。他一开始不是这么说的。大部分是暗示：能有他是我走运。我不够好，找不到更好的。不够聪明。不够漂亮。"
        j "他{b}放{/b}什么屁。你聪明又漂亮。你只是安静内敛，但这不改变任何事。任何一个男人能跟你一起出现在公开场合都会觉得是荣幸，更别说约会了。如果他跟你说的是那种话，那他就是个他妈的白痴。或者一块你根本不需要留在生活里的烂泥。"
        scene c007_s007_009 with Dissolve(0.25)
        k "谢……我……*抽鼻子*"
        scene c007_s007_010 with Dissolve(0.25)
        j "没事。你现在跟一群在乎你、希望你平安的人在一起。"
        "她在我怀里哭，我们就这么站了好一会儿。别看她自己觉得那么虚弱渺小，她却紧紧地抱住了我。"
        scene c007_s007_011 with Dissolve(0.5)
        k "我、我……我不确定自己曾经真的爱过他。现在我长时间认真想想。我觉得我只是「想要」被爱。我想要的是被爱，不是被占有，不是被买走。爱应该是温暖、快乐的，而不是冰冷、令人害怕的。"
        k "那时候我年轻又天真，只知道有人来追求我就很开心。我是个中学里的书呆子女孩，没有社交生活。女孩都想要那种童话式的爱情，可没人会告诉你那些童话有多毒、多糟糕。"
        scene c007_s007_012 with Dissolve(0.25)
        k "你读过那些故事吗？女孩被关在高塔里、躺在昏迷中，等着某个男人来救她们。而她们因为被找到、被救下就高兴得不得了，于是「爱上」了她们看到的第一个男人。故事从不会说，她们可能只是把一种囚禁换成了另一种。"
        k "我很久很久都没看出原来是这么回事。直到我不再被精神操控。也许更早我就知道哪里不对，只是我没有独立到能真正冷静想一遍……不被他「说服」。"
        scene c007_s007_013 with Dissolve(0.25)
        k "他控制我跟谁说话、说多久。控制我电视上看什么。电影。比如，他不想让我看到那些可能让我质疑「我们的关系为什么是这样、而不是另一种」的东西。"
        j "那……那他妈太糟了，我很抱歉你经历过这些。你能意识到有问题是好事，等我们出去以后，你一定得正面处理它。要是你需要人帮你脱身，我和劳拉都很乐意帮忙。"
        scene c007_s007_014 with Dissolve(0.5)
        j "前提是你想要。我猜既然我们聊到了这个，多半是。"
        k "我想要能够自己做选择。做我自己的选择。你不知道失去那种能力会把一个人变成什么样。那……那种生活毫无希望。只有孤独。"
        j "对不起。除了这句，我不知道还能说什么。"
        scene c007_s007_015 with Dissolve(0.25)
        k "我没想要别的。但是，[player_name]，我……跟你在一起我觉得安全。已经有段时间了。这是我第一次在谁身边觉得安全。你救了我。把我从……本来可能发生在我身上的事里救了出来。我不记得了。"
        k "劳拉说它把我摔在地上，还想喷我那玩意儿。像是想把我烧伤。把我变成它那样。全是恶心又扭曲的东西。"
        j "你永远不会变成那种东西。"
        scene c007_s007_016 with Dissolve(0.25)
        k "谢了。我喜欢你这样说这种话。听起来傻乎乎的、很孩子气，但……感觉很真诚。也不像你等着我回报你什么。事实上，你……你不会逼我去做我不想做的事。你不会对我指手画脚。我觉得你认真对待我，也听得见我。你在听我说话。"
        if k_friend <= 10:
            j "我尽力了。这是我能做的全部，因为我们所有人都得靠彼此活下来。你最近两边都经历过，所以你懂我的意思。"
            scene c007_s007_017 with Dissolve(0.25)
            k "我懂。真的懂。谢谢你。谢谢你是我能信任的人。是我的朋友。"
            j "没什么。*叹气* 我们该回去了。看看劳拉。"
            scene c007_s007_018 with Dissolve(0.25)
            k "不过，我们还真没怎么找补给。"
            j "我记下了几个想搜的房间。回头再说。"
            scene c007_s007_019 with Dissolve(0.25)
            k "回去的路上顺便？"
            j "行。我想雪莉没有我们也能再撑几分钟。"
            jump ch7_returntodorm
        else:
            scene c007_s007_020 with Dissolve(0.25)
            k "我……我不知道。我有感觉。我觉得自己不像别的女孩。我们说过，因为待得近，我更容易在乎一个人、或者对一个人产生好感，也许正因为你在身边，我才……才有了这种感觉。"
            j "卡莉……你想说什么？"
            scene c007_s007_021 with Dissolve(0.25)
            k "那天晚上你坐下来的时候……我叫你留下是有原因的。我只是需要攒够……勇气吧。我想让你那晚……跟我睡。睡觉。你懂的。"
            j "不算「睡觉」吧。"
            scene c007_s007_022 with Dissolve(0.25)
            k "对。我想知道那种感觉——觉得事情由我掌控，而不是被人逼着……做某些事。"
            j "哦，哇。呃……靠。我想我要是更会读暗示，刚才可能就留下来了。"
            scene c007_s007_023 with Dissolve(0.25)
            k "也就是我当时穿的那件衬衫。"
            j "我不想擅自认定什么。我不太会读话外之意，也不擅长调情。而且你知道……你还订着婚。"
            scene c007_s007_024 with Dissolve(0.25)
            k "……也许不再是了。但我必须知道……你会吗？如果你当时留下来的话？我不是在要什么承诺或者更进一步，我只是想……"
    scene c007_s007_034 with Dissolve(1)
    "哦？这……我在这儿得小心点。虽然我觉得她和这件事都很有吸引力，但这不是没有坑的。她还订着婚，我们以后得面对这个问题。"
    "另外，她不止一次说过，她担心自己之所以能跟人亲近只是因为「不得不」。如果这件事真的发展下去，我不知道对她和我意味着什么。等这段共同的狗血剧情结束，这份吸引会消退吗？"
    if ch5_laura_sex == "yes":
        "而且我跟劳拉还有那档子事，我也许不该再往这个方向走。可话说回来，看劳拉最近的样子，我猜我们那点小艳遇已经结束了。"
    menu:
        "我不知道。\n[rrd](卡莉 欲望 -1)":
            $ k_desire -=1
            scene c007_s007_035 with Dissolve(0.5)
            j "我不知道。我喜欢你，也喜欢我们能更了解彼此。这是这一整件事唯一的好处。我想我们现在算是不错的朋友了。"
            k "我……我也这么觉得。"
            j "但是，我不想让你的处境比以前更乱。你和安德鲁的事。我不知道等我们出去以后哪条路才是对的——但我真的不想让你觉得自己是在「把一种囚禁换成另一种」。"
            scene c007_s007_036 with Dissolve(0.25)
            k "我不觉得……"
            j "你有太多事要想清楚。这方面你得信我，因为我经历过。不是完全一样，但我知道重大的感情决定从来都不容易。"
            scene c007_s007_037 with Dissolve(0.25)
            k "好、好吧……谢谢你。谢谢你愿意对我坦诚，也谢谢你是那种我可以信任、能对我说实话的人。是我的朋友。"
            if ch6_kallie_sex == "yes":
                scene c007_s007_015 with Dissolve(0.5)
                j "而且，如果前天晚上我们做的事没能帮到你，反而让你更难想清楚，我会很抱歉。"
                k "那……我喜欢。那是我想要、也需要的东西。说不定反而让某些事对我来说更清楚了。再说，嗯……"
                scene c007_s007_016 with Dissolve(0.25)
                j "我也挺享受的。*轻笑*"
                j "*叹气* 我们该回去了。看看劳拉。"
            else:
                scene c007_s007_016 with Dissolve(0.5)
                j "没问题。*叹气* 我们该回去了。看看劳拉。"
            scene c007_s007_018 with Dissolve(0.25)
            k "不过，我们还真没怎么找补给。"
            j "我记下了几个想搜的房间。回头再说。"
            scene c007_s007_019 with Dissolve(0.25)
            k "回去的路上顺便？"
            j "行。我想雪莉没有我们也能再撑几分钟。"
            jump ch7_returntodorm
        "我会的。\n[rgr](卡莉 爱意 +1)\n[pks]" if ch6_kallie_sex == "no":
            j "我想我要是没那么迟钝，刚才就会了。我是说，你就是你。"
            scene c007_s007_038 with Dissolve(0.25)
            k "我不是……"
            j "你可爱得要命。还有……嗯……"
            $ ch7_kallie_sex = "yes"
            $ k_love += 1
            $ k_sex += 1
            call ch7_kallie_sex from _call_ch7_kallie_sex1
        "所以你跟着我来，就是因为这个？\n[rgr](卡莉 爱意 +1)\n[pks]" if ch6_kallie_sex == "yes":
            j "呃，所以呢，你跟着我来就是因为这个？"
            scene c007_s007_038 with Dissolve(0.25)
            k "我……不太会调情。我也不是总能把握时机，但我猜我或许能在回去之前把自己说服着说出点什么。主要是因为我知道不会有人打断我们。"
            j "是啊，就我们四个人，想凑出十分钟都难——"
            $ ch7_kallie_sex = "yes"
            $ k_love += 1
            $ k_sex += 1
            call ch7_kallie_sex from _call_ch7_kallie_sex2
label ch7_returntodorm:
    stop music fadeout 2.0
    if ch7_kallie_sex == "yes":
        scene blank with Dissolve(1)
        scene c007_s008_053 with Dissolve(1)
        "接下来的几分钟里，我们手忙脚乱地穿回衣服。"
        scene c007_s008_054 with Dissolve(0.5)
        "四周很安静，空气里还残留着性爱的气味。我忍不住短暂地幻想了一下：只要能溜出来，我们随时都可以再来一次。"
        scene c007_s008_054-1 with Dissolve(0.5)
    else:
        scene c007_s008_054-1 with Dissolve(0.5)
    s "[player_name]！卡莉！[player_name]！卡莉！"
    j "嗯，看来有人等不及我们回去了。"
    "等等。我们不是把她留给劳拉了吗？"
    scene blank with Dissolve(2)
    scene c007_s008_056 with Dissolve(2)
    play sound doorclose
    s "哦，谢天谢地。你在这儿。"
    scene c007_s008_057 with Dissolve(0.25)
    j "雪莉？出什么事了？"
    scene c007_s008_058 with Dissolve(0.5)
    s "是劳拉。我刚去撒了趟尿，回来她就不见了。我跑到正门，好像看见她走远了。"
    play music horror
    scene c007_s008_059 with hpunch
    j "靠！靠靠靠！！！"
    s "对不起。我没想到她会这么做。真的。"
    scene blank with Dissolve(2)
    scene c007_s008_013 with Dissolve(2)
    "我拼命往宿舍跑，越快越好。等我赶到的时候，每一口气都带出明显的喘鸣。"
    scene c007_s008_014 with Dissolve(0.5)
    "我冲进房间套装备，一边喊劳拉的名字，心里还抱着一点可笑的希望：兴许是雪莉没注意到她。"
    scene blank with Dissolve(1)
    scene c007_s008_015 with Dissolve(1)
    "穿好以后，我冲向大门。"
    scene blank with Dissolve(2)
    scene c007_s008_016 with Dissolve(2)
    "当然了，我完全不知道她在哪儿。取决于雪莉过了多久才发现她不见，劳拉可能已经比我领先十五分钟甚至更久。"
    scene c007_s008_017 with Dissolve(0.5)
    "她会去哪儿？她当时还一门心思盯着去医院，会不会干脆决定徒步走过去？或者，她陷在一种解离的狂热里，就那么走到了外面？她的外套不见了，说明她至少还残留着点理智，装备过。"
    "最后我决定赌她是冲着医院去的。那是我唯一的线索。"
    scene blank with Dissolve(2)
    scene c007_s008_018 with Dissolve(2)
    "我冲过院子（去医院最好的走法是回到主路上），一路喊着她的名字。这是场不得不赌的博弈。"
    "我知道外面有灼烧者，但我不清楚声音会不会把它们引过来。事实上，我根本不知道是什么会吸引它们。它们总是在最不方便的时候冒出来。气味？体温？动静？谁知道呢？"
    scene blank with Dissolve(2)
    scene c007_s008_019 with Dissolve(2)
    j "劳拉！劳拉你在哪儿？！"
    "操，什么都没有。可我已经开始觉得自己像在跑马拉松了。侧腹开始疼，汗出得像教堂里偷情的婊子。"
    scene c007_s008_020 with Dissolve(0.5)
    "然后我看见「朋友」里有一个出来了。管他妈，我没时间耗在这破事上。我绕大路跑，并且记住别再从这条路回来。"
    scene blank with Dissolve(2)
    scene c007_s008_021 with Dissolve(2)
    "我开始搞不清自己他妈在哪儿了。要说这一带哪儿看着眼熟，没有一处像的，可在这雾里，一切都开始像失焦的背景板。而且我压根没来过这儿，就算没雾也不认识路。我本该留点{a=https://en.wikipedia.org/wiki/Hansel_and_Gretel}面包屑{/a}，这样就知道怎么回去。"
    scene c007_s008_022 with Dissolve(0.5)
    j "劳拉！劳——拉——啊！！！" with vpunch
    u "{size=28}*咳* *咳* *咳*{/size}"
    "外面有人。肯定是劳拉。求老天保佑是她。"
    j "劳拉！劳拉！！"
    scene c007_s008_023 with Dissolve(1)
    "在那儿！她在那儿。弓着背，看起来不太好。至少还活着。或者说，我觉得那是她。不过我得留意周围。已经太多次了，我们被埋伏着的灼烧者打劫，我他妈受够了。"
    menu:
        "现在就过去找劳拉。[yl]":
            scene c007_s008_024 with Dissolve(0.5)
            "现在就得赶到她那儿。"
        "看看四周。[yl]":
            "就一秒。劳拉可以再等一秒。"
            scene c007_s008_025 with Dissolve(0.5)
            "什么也没有。或者附近什么也没有。我能看见远处的轮廓。那后面是个女人吗？是{b}那个{/b}劳拉吗？不可能。她明明就在那边。别想太多了，哥们儿。"
            scene c007_s008_024 with Dissolve(0.5)
    j "嘿，劳拉，是我，[player_name]！我在这儿。你他妈到底在想什么？就那样直接走出来？！"
    scene c007_s008_026 with Dissolve(0.25)
    l "*咳* *咳* {size=32}我得回家……得去看看……{/size} *咳*"
    scene c007_s008_027 with Dissolve(0.5)
    j "不，劳拉！不对！很抱歉事情没按计划发展，但这不是办法！你不能就这么走去医院！"
    if l_trust <= 2:
        scene c007_s008_062 with hpunch
        l "不！别碰我！别…… *咳* {size=32}别拦我……{/size}"
        "靠。看来我之前让劳拉信任我这件事做得不怎么样。现在只能当这个混蛋，硬把她拉回来。"
    scene c007_s008_028 with hpunch
    j "你是想死吗？因为我需要你别他妈想不开！"
    l "可是我、我、我 *咳*"
    scene c007_s008_029
    j "如果这之后你恨我，那我道歉，但总得有人把你摇醒。彼得没事，很安全，而你唯一能再见到他的办法，就是聪明一点、从这儿出去。"
    l "可是 *咳* 基思呢？那怎么办——"
    scene c007_s008_030 with Dissolve(0.25)
    j "基思滚蛋！那个出轨的混蛋现在可以滚了。我知道你需要搞清楚你婚姻里到底出了什么岔子，但那些破事可以等！你要让他难堪，就他妈活着去让他难堪！穿过一座充满死亡烟雾的城市去搞这个，不是办法。"
    menu:
        "[rd]看看我们周围。\n[rrd](劳拉 焦虑 +1)":
            $ l_anxiety +=1
            scene c007_s008_032 with Dissolve(0.5)
            "我什么也没看到。也许那边有什么在动，但可能只是雾在飘。"
            l "我、我不…… *咳*"
            scene c007_s008_031 with Dissolve(0.25)
        "[gr]专注在劳拉身上。":
            pass
            l "我、我不…… *咳*"
            scene c007_s008_031 with Dissolve(0.25)
    j "劳拉，很抱歉事情没按你希望的方式发展，而且现在也不是讨论这件事的时间和地点。你在这件事上不理性。但我和卡莉需要你。好吗？我们要是不齐心协力，就谁也出不去。"
    j "所以我需要你把注意力放在我们身上。如果你需要点什么撑住自己，就想想再见到儿子。想想让基思滚蛋。但像这样跑掉是疯的，我不许你这么做。"
    if l_trust <= 2:
        scene c007_s008_063 with vpunch
        l "放开我 *咳*……放开我，我需要…… *咳*"
        "她虚弱地捶打着我的胸口。要是她还有点力气，这事可能还更难。天哪，我讨厌这样，但我还是得把她强行带回去，是吧？"
    else:
        scene c007_s008_033 with Dissolve(0.25)
        l "{size=32}我需要……{/size}*咳* *咳* {size=32}需要……{/size}"
    scene c007_s008_034 with vpunch
    "我没料到劳拉会一下子彻底脱力——她倒进我怀里，开始抽泣。"
    l "{size=32}我、我不知道{/size} *咳* *咳* {size=32}我哪里出了问题。我……我要疯了{/size} *咳*"
    scene c007_s008_035 with Dissolve(0.25)
    l "我就是啊啊啊~~~"
    "我抱着她，任她靠在我身上哭。与此同时我扫视四周。有些明显的动静，说明我们得赶紧结束这一切。"
    scene c007_s008_036 with Dissolve(1)
    j "劳拉？劳拉，我得把你带回宿舍。你不能再跟我拧着。有麻烦正在慢慢朝我们这边挪过来，我们没时间再耗在这儿讲道理了。"
    l "*咳* {size=32}我……我不知道我能不能{/size} *咳*"
    scene c007_s008_037 with Dissolve(0.25)
    j "这个问题这里没得谈。要是非得帮你不可，我就会帮。把胳膊给我。我扶你。"
    l "{size=32}好、好吧……我只是{/size} *咳* {size=32}我在努力，可是{/size} *咳* *咳*"
    scene c007_s008_038 with Dissolve(0.25)
    j "我知道。站稳了，让我来带路。"
    "我只能做到这一步。她没有在这件事上跟我拧，让我一瞬间松了口气。我本来做好了她死命反抗的准备，宁可把她扛在肩上、连踢带叫地拖回去。可她已经碎了，压根无力反抗。"
    scene blank with Dissolve(1)
    scene c007_s008_039 with Dissolve(1)
    "好了，我能看到一些眼熟的建筑结构。这就对了。劳拉走得很吃力，我几乎是在拖着她走。她想说什么，但咳得太厉害，我一个字也听不清。"
    play music monster
    scene c007_s008_040 with hpunch
    "操，一个灼烧者刚好踉跄着走出来。我得尽力绕开它。我抓着劳拉，根本没法给它来一记结实的，除非先松手。也许我们从大边绕。"
    play sound gas
    scene c007_s008_041 with flashyellow
    j "靠！！"
    "绕开。躲开最浓的那片。"
    scene c007_s008_042 with vpunch
    l "*咳* *咳* 哦，天哪。"
    play sound axehit
    scene c007_s008_043 with flashred
    j "靠！滚开！"
    scene c007_s008_044 with Dissolve(0.25)
    "没时间收拾它了。抓住劳拉，走。"
    scene c007_s008_045 with Dissolve(0.5)
    j "劳拉，给。手。"
    l "不，不。我……*咳* *咳* 咳得停不下来。哈啊~~~ 腿……喘不上气……"
    "去他的，没时间在这儿耗。我能听见周围的灌木丛里有动静。"
    scene c007_s008_046 with vpunch
    l "哦！哦靠！" with hpunch
    j "抓紧了。我要加倍步频冲回宿舍。"
    "至少先冲出这一带。"
    stop music fadeout 2.0
    scene blank with Dissolve(1)
    scene c007_s008_047 with Dissolve(1)
    play music horror fadein 2.0
    "这话我不会说出口，但劳拉比卡莉重。再加上一路冲刺追她，我已经喘得不行了。"
    scene c007_s008_048 with Dissolve(0.5)
    "说到劳拉，她抓得死紧，可咳嗽很厉害。厉害到什么程度呢——以至于都盖不住她正在放声大哭、嘴里含混不清地嘟囔这件事。"
    scene blank with Dissolve(1)
    scene c007_s008_049 with Dissolve(1)
    "操，又来一个。它们像闻着味儿一样从各处冒出来。我们加快速度。我只能祈祷这个混蛋动作慢，好让我把它远远甩掉。"
    scene blank with Dissolve(1)
    scene c007_s008_050 with Dissolve(1)
    "等我看见宿舍楼熟悉的轮廓时，劳拉已经真的呼吸困难了。我也好不到哪儿去。胳膊和腿都在疼，肺像在烧。每一寸露在外面的皮肤都在尖叫着喊疼。"
    j "再撑一会儿。快到了。"
    scene c007_s008_051 with Dissolve(0.5)
    "劳拉只是费力地吐了一口气，听起来像一只垂死风琴发出的最后一声呜咽。"
    scene blank with Dissolve(1)
    scene c007_s008_052 with Dissolve(1)
    "靠，总算回来了。先进去，看看伤得怎么样。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c007_s008_060 with Dissolve(2)
    play music insidedark fadein 4.0
    k "哦天哪，她没事吧？劳拉？！我们在隔壁房间的窗户看到你了。"
    s "哦，靠，我不该——"
    scene c007_s008_061 with Dissolve(0.25)
    j "现在别说这个。我直接带她去淋浴间，想办法把身上这玩意儿尽量冲掉。把门堵上。我回来的时候后面缀着几个灼烧者。"
    scene blank with Dissolve(2)
    scene c007_s009_001 with Dissolve(2)
    "我讨厌这样对他们说话，但时间他妈太要紧了，而且劳拉咳得喘得那么厉害，我怕她气胸。"
    "我连在水槽那儿给她洗把脸的时间都不想浪费。想想看，我和卡莉当时都得正经冲个澡才能把这东西冲干净，所以我直接带她去后面。"
    scene c007_s009_002 with Dissolve(0.5)
    "到这一步，我得问问自己：这种事我还得做几次？要是哪天我还得把雪莉拖进淋浴间，我就得跟所有人来一次非常不客气的公开训话。事实上，也许是时候让我当这个混蛋，立几条规矩了。"
    scene c007_s009_003 with Dissolve(0.25)
    j "到了，劳拉。好，我得帮你把外套、手套什么的脱掉。"
    scene c007_s009_004 with Dissolve(0.25)
    "路上把帽子丢了。她这身装备看起来不算太糟。只要晾一晾就行。不像卡莉那件外套，那已经是彻底报废了。"
    scene c007_s009_005 with Dissolve(0.25)
    l "*咳* 喘不上气…… *咳*"
    scene c007_s009_006 with Dissolve(0.5)
    j "我知道，我知道。我在。不走。我这就把你弄进淋浴间，把这玩意儿冲掉。"
    scene c007_s009_007 with Dissolve(0.25)
    "她露在外面的脸又红、甚至有点起泡。她在外面也撑不了多久了。老实说，我自己也不好受，只是因为必须撑住，我才撑住了。"
    scene c007_s009_008 with vpunch
    j "慢点。"
    scene c007_s009_009 with Dissolve(0.25)
    l "*咳* 腿……啊~~~好软 *咳*"
    "我连离开她去开水的时间都没有。"
    j "好吧，我跟你一起进去。衣服湿了又怎样，操。会干的。"
    scene blank with Dissolve(1)
    scene c007_s009_010 with Dissolve(1)
    "费了些劲才把她弄进去、没让她绊倒摔一跤。弄好之后我把手伸进去——另一只手还牢牢扶着她——把水打开了。"
    play ambient shower
    scene c007_s009_011 with Dissolve(0.25)
    "是啊，刚开始水还是凉的那几秒并不好受。"
    scene c007_s009_012 with Dissolve(0.25)
    l "得、得啊~~~把衬衫脱掉。里面烧得慌 *咳*"
    scene c007_s009_013 with Dissolve(0.25)
    "行行行。反正我们的衣服本来就会湿得透透的。你别摔倒就行。"
    scene c007_s009_014 with Dissolve(0.25)
    l "啊啊啊~~~"
    j "让你自己站着这事我已经受够了。"
    scene c007_s009_015 with Dissolve(1)
    k "[player_name]？劳拉？"
    j "在里面！"
    scene c007_s009_016 with Dissolve(0.5)
    k "哦。啊啊啊~~~"
    j "她呼吸很困难，也撑不住身子。我能想到的办法只有这个。"
    scene c007_s009_017 with Dissolve(0.25)
    k "有没有什么我能帮忙的？"
    j "我们的外套。还有她的衬衫。你能挂起来吗？晾一晾，让她的衬衫干。"
    k "好、好吧，行。"
    scene c007_s009_018 with Dissolve(0.5)
    j "劳拉？劳拉，你还……"
    l "*喘气* 我能坐下吗？腿……我再也站不住了。"
    stop music fadeout 2.0
    j "好，那我们就慢一点。"
    scene blank with Dissolve(2)
    scene c007_s009_019 with Dissolve(2)
    play music insideday fadein 2.0
    "我想尽量让她慢慢坐下去，可劳拉的身体压根不打算做任何事，只想彻底失去全部力气。幸好我在，接住了她。"
    scene c007_s009_020 with Dissolve(0.5)
    "接下来的几分钟，我就抱着她，听她把哭和咳混在一起发出来。听见她的呼吸似乎好转了些，我多少松了口气。"
    scene c007_s009_021 with Dissolve(0.5)
    j "劳拉？好点了吗？刚才有一阵子真把我吓坏了。我以为我要失去你了。"
    l "我……*咳* 刚才……很不好过 *咳* 现在好点了。还是……不太行。"
    scene c007_s009_022 with Dissolve(0.25)
    j "你现在好到能让我接着骂你了吗？"
    l "别…… *咳* *咳* 我……"
    menu:
        "有什么就都说出来。\n[rrd](劳拉 好感 -1)":
            $ l_friend -= 1
            scene c007_s009_023 with Dissolve(0.5)
            j "不不。我是担心。是害怕。而且，对，是生气。我知道你担心彼得、气炸了基思，但像这样横穿整座城市跑出去就是找死。要是非得这样才能拦住你，我真会把你铐在我身上。"
            j "我不是不心疼你承受了这么大的情绪压力，我也不知道有个孩子是什么滋味，但你这么冲出去，就再也见不到彼得了。你恨死我也行，但这话他妈的属实。所以如果这次必须由我来当恶人，我就当。"
        "饶了她吧。\n[rgr](劳拉 好感 +1)":
            $ l_friend += 1
            scene c007_s009_023 with Dissolve(0.5)
            j "好吧，我不再为难你，但这种事不能再发生第二次了。我知道你害怕、担心家人、气基思，但你不能这样对我们。我们也在乎你。"
            j "我们需要你，劳拉。我们所有人一起活着离开这里的唯一办法，就是抱成团。人越多，我们的胜算越大。"
    scene c007_s009_024 with Dissolve(0.25)
    l "对不起 *抽泣* 我真的很对不起。我只是…… *咳* 让一切都压垮了我。太多了 *咳* *咳*"
    scene c007_s009_025 with Dissolve(0.25)
    l "我觉得我快疯了 *咳* 然后我就说服自己非走不可。我再也待不下去了。"
    j "我向你保证，我们会找到出去的办法，但我们得比这聪明。我知道自己最近蠢得可以，一直随波逐流，对每件事都当成短暂的小麻烦来处理，但这种事不能再有了。"
    j "这是永久的现实，我们必须做该做的事，让我们所有人都活着。"
    scene c007_s009_026 with Dissolve(0.25)
    j "而且，每次出这种破事都得把我们中的一个人拖进淋浴间，我也有点受够了。"
    l "*咳* 对不起。我……我刚才失去理智了。我……我不会再这样了。"
    scene c007_s009_027 with Dissolve(0.25)
    j "真的吗？因为我需要能信任你，劳拉。我们不能每次都派个人看着你，以防你又跑掉。"
    l "我知道。*抽鼻子* 我知道。"
    "刚才那些话比我本该说的狠多了，但事情本来不该走到这一步。劳拉刚才有一阵子失去了理智，我只希望过去这半个小时的刺激足够把她拉回来。"
    scene c007_s009_028 with Dissolve(1)
    "水继续当头浇下来，我们在那儿坐了一会儿。我只是听着她呼吸里的沙哑慢慢——几乎察觉不到地——改善。虽然我不会骗自己说劳拉已经脱险了，但至少现在她活着；如果不是我及时找到她，她可能已经不在了。"
    stop ambient
    scene c007_s009_029 with Dissolve(0.5)
    "卡莉回来时，伸手关掉了淋浴。手里拿着一对毛巾，我很清楚现在用还太早。我们俩看起来都像被暴风雨淋透的狗。我得先脱掉衣服，才谈得上擦干自己。"
    scene c007_s009_030 with Dissolve(0.5)
    "卡莉伸手扶劳拉出淋浴间，我帮着她站起来。"
    k "你没事吧？脸有点红，但我觉得没烧伤得太厉害。"
    scene c007_s009_031 with Dissolve(0.25)
    l "对不起 *咳* 我不是……不是故意的 *咳*"
    j "你还能站着吗，还是我们……算了，我们把你挪到长椅上吧。"
    scene c007_s009_032 with Dissolve(0.25)
    l "我、我觉得可以……"
    j "不行。先让你坐下。你在那儿脱衣服，就不用担心再摔一跤。"
    scene c007_s009_033 with Dissolve(0.5)
    "安置好她以后，我让卡莉帮忙，自己开始脱衣服。脱的时候，我听见卡莉尽力照顾劳拉，而劳拉在一阵阵咳得撕心裂肺的间隙里，拼命地道歉。"
    scene c007_s009_034 with Dissolve(0.25)
    l "我很蠢，我不该——"
    k "劳拉，没关系。我理解。你很久以来都得当那个大人，再加上一堆别的压力，就超出极限了。我没有儿子，但我还是担心我的家人，哪怕我知道他们在好几个州之外。我也想再听到他们的声音。"
    scene c007_s009_035 with Dissolve(0.25)
    k "我真的很害怕，但我会努力变好。我相信你和[player_name]会在，所以你也得一样。你得让我们陪在你身边。"
    l "*叹气* 我知道。我只是……刚才失去了理智。疯了。蠢透了。这种事足以把人压垮。"
    scene c007_s009_036 with Dissolve(1)
    j "好了，我把衣服甩到浴帘杆上滴水晾干。它们会皱得要死，但也没别的办法了。我得回房间拿件干的。劳拉？"
    scene c007_s009_037 with Dissolve(0.5)
    l "[player_name]，我……对不起。我真的很抱歉。"
    j "没事。你怎么样？"
    scene c007_s009_038 with Dissolve(0.5)
    l "肺像被塞了屎，脸就像有人拿钢丝球在上面狠狠搓过。"
    j "好消息是它会好。"
    "受伤总比死掉强。"
    scene c007_s009_039 with Dissolve(0.25)
    k "相信我，一定会的。"
    j "那，雪莉呢？我还以为她会来看好戏。"
    "或者至少看我裹着条毛巾站在那儿。"
    scene c007_s009_040 with Dissolve(0.25)
    k "我觉得她受够了。她对……你知道的……那件事真的很受伤。"
    j "好吧，那个我以后再处理。卡莉，你能——"
    scene c007_s009_041 with Dissolve(0.25)
    k "我送她回房间，再找身换洗衣服。跟我来，劳拉。"
    l "好。谢谢。还有[player_name]……我不会忘记这件事。忘记你……跑来救我。"
    if ch7_kallie_sex == "yes":
        scene c007_s009_043 with Dissolve(0.25)
    else:
        scene c007_s009_042 with Dissolve(0.25)
    j "没事。我一会儿就过去。等我先找件干衣服。"
    scene c007_s009_044 with Dissolve(0.25)
    "我需要去把雪莉找出来吗？我本来非常确定她会跟卡莉在这儿，不过看来她自己选择不出现。也许那些吼叫、还有我冲出去追劳拉，对她来说太过头了。我没有足够证据下结论，但我得到的感觉是雪莉的情绪可能比较容易大起大落。"
    "又或者，我可以在这儿暂停十分钟不去追狗血剧情。她在自己房间，等会儿想聊自然会找我。老实说，我累瘫了。全身酸痛得像刚跑完一场马拉松。或者更糟。我他妈需要休息一下。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_22_203", transition=Dissolve(1.0))()
    pause
    $ Hide("june_22_203", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s010_001 with Dissolve(2)
    play music insideday3 fadein 2.0
    "一换上干净衣服，所有先前被肾上腺素神奇压住的酸痛，就一起露出了它们丑陋的脑袋。"
    "尽管如此，我决定不坐下休息，因为我怕自己会直接睡过去，或者更糟——起不来。"
    if ch7_kallie_sex == "yes":
        "要不是跟卡莉单独待了那会儿，今天可能会彻底变成一场灾难。而劳拉当时脆弱成那样，我也没料到什么近在眼前的时机，能让我们再单独相处。"
    scene c007_s010_002 with Dissolve(0.5)
    "我在卡莉的房门外停下（是啊，明明天花板下所有私人物品都属于别人，把这儿当成她的房间还是怪怪的），侧耳听了一下。"
    scene blank with Dissolve(2)
    scene c007_s010_003 with Dissolve(2)
    l "我当初刚到办公室的时候以为已经够糟了 *咳* 结果这次居然更糟。[player_name]找到我的时候，我 *咳* 认定自己的肺已经完蛋了。就算戴着面罩也是。我那面罩的防雾效果没我想的那么好。"
    k "你走了多远？你知道自己当时在哪儿吗？"
    scene c007_s010_004 with Dissolve(0.25)
    l "不知道。我……这些楼看起来都开始一模一样了，尤其是在雾里。"
    k "你……我实在不想问，但……"
    scene c007_s010_005 with Dissolve(0.25)
    l "没关系。我、我保证再也不干那么疯狂的事了。我只是……*咳* 当时失去了理智。疼痛特别能让人清醒。再加上怕自己会死。还有，[player_name]真是把我骂惨了，我从没见过他那么生气。"
    k "他那么做只是因为担心。"
    scene c007_s010_006 with Dissolve(0.25)
    l "我知道那是出于关心。我只是……*咳* 觉得自己那样失去理智很蠢。"
    k "没关系。这件事给我们很大压力，也许我们都在做一些以前不会做的选择。"
    scene c007_s010_007 with Dissolve(0.25)
    l "嗯……"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_26_756", transition=Dissolve(1.0))()
    pause
    $ Hide("june_26_756", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s010_008 with Dissolve(2)
    play music nightmain2 fadein 2.0
    "混乱过去以后，宿舍里安静下来。夜幕降临时，我在走廊里来回走，好像巡逻一圈就能让我对我们的处境更安心。想到哈灵顿楼那扇门可能还开着（我是急忙跑回来的），我就去查看了一下。"
    scene c007_s010_009 with Dissolve(0.5)
    "看到路障已经重新架好，我松了口气。肯定是卡莉跟雪莉回来以后自己弄的。知道她还能有这种分寸，感觉真好。"
    scene c007_s010_010 with Dissolve(0.5)
    s "呃，嘿……[player_name]？"
    j "哦，雪莉。嘿。"
    scene c007_s010_011 with Dissolve(0.25)
    s "嘿。劳拉……劳拉还好吗？我看见你带她回来，然后不久前我听见她跟卡莉在另一个房间里，然后……"
    j "她没事。至少还活着，虽然以后可能会落下个肺气肿之类的毛病。"
    scene c007_s010_012 with Dissolve(0.5)
    s "我、我很抱歉。我、我应该守着她的。我只是去上了个厕所，然后就有点走神了。我老这样。我当时在洗脸，心想「他们回来以后我真该去冲个澡」，然后才想起我该回去看劳拉。"
    s "我的意思是，我没想过她会直接走出去。我只以为她很难过。或者很抑郁。不是那种疯了想自杀的样子。"
    menu:
        "她不是想自杀。":
            j "她不是想自杀。她只是太想见到家人，情急之下做了一个当时的状态不足以让她完全意识到有多危险的决定。"
        "她好多了。":
            j "她好多了。这就够了。出去这主意并不明智，但我看她真的体会到了那个决定的份量。"
        "[gr]不是你的错。\n[rgr](雪莉 焦虑 -1)":
            $ s_anxiety -= 1
            j "不是你的错。劳拉是个成年人，她要是铁了心要出去，你说什么也劝不住她。再说，如果她特意等你走开了一小会儿？那也只是因为她不想被你拦住。"
    scene c007_s010_013 with Dissolve(0.25)
    s "我……好吧。我想我确实不太理解她为什么那样出去。我怕死，不敢出门。外面有想杀我们的东西。但要是我有孩子或者丈夫，我可能就不会那么在乎自己的安全了。"
    j "嗯，大概就是那种感觉。劳拉有时会钻进牛角尖，我觉得这一切把她彻底打懵了。她属于那种必须让世界按她习惯的方式运转才安心的人。"
    scene c007_s010_014 with Dissolve(0.25)
    s "*哼* 我懂她。手机打不通简直要了我的命，因为我只想能跟所有人说话。跟家人联系，哪怕我觉得他们应该没事。也只是想让他们知道我还好。"
    scene c007_s010_015 with Dissolve(0.25)
    s "你有没有……你在外面看到什么人了吗？我只是……有我认识的人就这么冲进了那雾里，而如果劳拉连走到某个地方都很费劲，那他们肯定也一样。也许他们只走到一半，就在另一栋楼里躲了起来。或者……更糟。"
    j "没有。我确实看到几个灼烧者，但没有别人。说实话，我那会儿没怎么留意周围的楼。"
    scene c007_s010_016 with Dissolve(0.25)
    s "你没事吗？你在外面也待了一阵子。你身上看起来没沾太多东西。你的脖子和脸颊有点红。反正没听上去像劳拉那么严重。"
    j "我想是我运气好。也许是狂奔救了我一命，我动得太快，那东西来不及沾上我。我现在还浑身酸痛，胸口感觉像被人来了一记左勾拳，但我死不了。"
    s "……好吧……"
    scene c007_s010_017 with Dissolve(0.25)
    s "那，你今晚有空吗？也许晚点可以一起待会儿。"
    j "呃……我得趁还不太晚去看看劳拉。不是怕她又干出什么，而是她需要一个朋友。如果早点结束——我有种感觉她会想睡——我就过去露个面。"
    scene c007_s010_018 with Dissolve(0.25)
    s "行行行。那就晚点再说。"
    scene blank with Dissolve(2)
    scene c007_s010_019 with Dissolve(2)
    "天渐渐晚了，我决定去看看劳拉。卡莉趁机先去冲个澡，睡前把自己收拾干净。我有种感觉她也想自己独处一会儿。"
    j "嘿，你。"
    l "[player_name]，我……"
    scene c007_s010_020 with Dissolve(0.25)
    j "你好点了吗？咳得怎么样？皮肤呢？你的眼睛红得要命，所以戴墨镜也不太顶用。"
    l "我本来没打算在外面待那么久。而且我开始咳得厉害的时候，眼镜滑松了。感觉有人在里面烤炭火似的。"
    scene c007_s010_021 with Dissolve(0.5)
    j "皮肤呢？这儿那儿有点红，但没卡莉那次严重。"
    l "我死不了。"
    scene c007_s010_022 with Dissolve(0.25)
    j "好了，往那边挪挪。我陪你坐会儿。"
    l "你不用。我不觉得自己配有任何人——"
    scene c007_s010_023 with Dissolve(1)
    j "闭嘴。你这套「我好可怜」的戏该停了。我们在乎你，希望你平安活着。所以，接下来一段时间我们会围着你转，这是有正当理由的，你得接受，别再想着自己一个人扛。"
    l "你是这么想的？你觉得我是因为需要一个人待着才要走的？"
    scene c007_s010_024 with Dissolve(0.25)
    j "我不知道，劳拉。你那会儿不太像你自己。跟我说说当时是怎么回事。"
    l "我也说不太清。我就是失去了理智。我……一切都像滚雪球一样失控了，我开始分不清现实。我甚至记不清卡莉说我前天做的有些事。什么都……像是断了片。"
    scene c007_s010_025 with Dissolve(0.25)
    l "我没疯吧？……我希望我没疯。"
    menu:
        "你没有。":
            j "你只是被自己累积的负面压力给反噬了。而且我可能太常让步了，本来该更果断。我一向这样，但以后不会了。"
        "人都会有迷失自我的时候。":
            j "人都会有迷失自我的时候。我离婚那阵子就是这样，所以我能理解。还有……本该更果断一些的时候，我却总是对你让步。我一直都是这样，但以后不会了。"
        "[rd]希望不会。\n[rrd](劳拉 焦虑 +1)":
            $ l_anxiety += 1
            j "希望不会。我希望只是因为烂事一次性堆得太多了。还有……本该更果断一些的时候，我却总是对你让步。我一直都是这样，但以后不会了。"
    scene c007_s010_026 with Dissolve(0.25)
    if l_sex >=1:
        j "所以我没能帮上忙。你过度专注于那辆SUV、那台电视，或者城市夜景的时候，我本该把你拉回来。我不该那样撩拨你的心思，像刚才那样跟你打情骂俏。"
    else:
        j "所以我没能帮上忙。你过度专注于那辆SUV、那台电视，或者城市夜景的时候，我本该把你拉回来。"
    scene c007_s010_027 with Dissolve(0.5)
    l "你大概说得对。我那份痴迷确实让事情变得更糟了。但不是你的错。你始终冷静、始终如一，而且……"
    scene c007_s010_028 with Dissolve(0.25)
    l "而且你还救了我一命。我当时真以为自己会死在外面。那感觉就像有人朝我的膈肌上打了一拳，我根本喘不上气。"
    j "总之你还活着，还能看到下一个日出。"
    scene c007_s010_029 with Dissolve(0.25)
    l "[player_name]，如果我又变成那样，拦住我。用什么方式都行。"
    j "你怕那种事再发生一次吗？"
    scene c007_s010_030 with Dissolve(0.25)
    l "我以前压根没觉得这有可能。等我们离开这儿，我可能得找个人看看。得吃点什么药。"
    j "或者，你也可以理解为：眼下这种高压时期，事情一旦崩了，人就会做出意想不到的反应。"
    scene c007_s010_031 with Dissolve(0.25)
    l "也许吧。不过，这事肯定得让我们落下PTSD。"
    j "确实。"
    scene c007_s010_032 with Dissolve(0.25)
    l "你能留下来一会儿吗？我已经很久没有贴着温热的身体睡觉了。"
    j "当然。你安心睡，我在这儿。"
    scene blank with Dissolve(2)
    scene c007_s010_033 with Dissolve(2)
    "我照约定坐在那儿，看着劳拉闭上眼睛。她的呼吸里带着一点轻微的喘鸣。"
    "毫不意外，几分钟之内她就睡熟了。她的身体软绵绵的，我一动，她也只是含糊地嘟囔一声，然后继续睡。"
    "那会儿我考虑过，是留下来，还是去见见雪莉——她之前让我去看看她。鉴于今天发生的一切，或许还是该再告诉她一次：今天的事不怪她。"
    menu:
        "留在劳拉身边。\n[rgr](劳拉 信任 +1)":
            $ l_trust += 1
            "我权衡了一下利弊，决定留在劳拉身边才是最好的选择。如果跟我挤一张床能让她这一晚睡得安稳些，我无所谓。现在最需要支持的人是她，不是别人。"
            scene blank with Dissolve(2)
            scene c007_s010_034 with Dissolve(2)
            "我想我也跟着打了个盹。等我醒来时，卡莉已经回来了。"
            j "{size=32}嘿，别管我。{/size}"
            scene c007_s010_035 with Dissolve(0.25)
            k "{size=32}她……{/size}"
            j "{size=32}睡着了。{/size}"
            scene c007_s010_036 with Dissolve(0.25)
            k "{size=32}好吧。酷。{/size}"
            j "{size=32}你要是想让我走，我可以走。给你们留点私人空间。{/size}"
            scene c007_s010_037 with Dissolve(0.25)
            k "{size=32}不不，留下吧。我想今晚有你在，我们俩都会好受些。{/size}"
            scene blank with Dissolve(1)
            if ch7_kallie_sex == "yes":
                scene c007_s010_039 with Dissolve(1)
            else:
                scene c007_s010_038 with Dissolve(1)
            "卡莉没再多说什么，爬上自己的床，花了接下来几分钟在找一个舒服的姿势。"
            "不知道我们俩是谁先睡着的。我只知道，直到第二天早上阳光透过窗帘洒进房间，我才再次醒来。"
        "离开。":
            scene blank with Dissolve(2)
            scene c007_s010_050 with Dissolve(2)
            $ ch7_sh_look = "yes"
            "好吧，我溜出去的时候劳拉没醒。她大概是累得死死的。卡莉还没回来，不过我选择相信她没事，只是想独处一会儿吧。老天知道，她值得。"
            "再多陪雪莉一会儿也无妨。嗯，我们确实聊过，但不像其他人那样，我和她之间几乎没什么相处的经验。就连卡莉那么安静，我们之间也有一份基础的熟悉感作底。她知道我会作何反应，也能相信我不是个危险的人。"
            scene c007_s010_051 with Dissolve(0.25)
            "*敲门* *敲门*" with vpunch
            scene c007_s010_052 with Dissolve(0.25)
            j "雪莉？我是[player_name]。"
            "没动静。一片寂静。也许她等我等着等着就睡着了。今天真是压力山大，又忙得脚不沾地。"
            scene c007_s010_051 with Dissolve(0.25)
            "*敲门* *敲门*" with vpunch
            scene c007_s010_053 with Dissolve(0.25)
            j "雪莉？"
            "通常我只会给她留点空间，但我现在神经绷得紧紧的，也许我就是想亲眼确认她没事。"
            scene blank with Dissolve(2)
            scene c007_s010_054 with Dissolve(2)
            j "雪莉？我是[player_name]。"
            "好吧，她躺在床上。"
            scene c007_s010_055 with Dissolve(0.25)
            "在呼吸。还活着。刚才有那么一瞬间，我以为是最坏的结果。看来「最坏的事」吃多了，我也被训练出来了。"
            scene c007_s010_056 with Dissolve(0.5)
            "我想，我在劳拉那儿待得稍微久了点，不过我是在做「情感支持」的分诊，劳拉优先。我应该多花点时间陪陪雪莉。我感觉这次约她出来，本来就是想单独待一会儿。而且卡莉和劳拉跟我说的那些话，让我不知不觉成了个还算安全的情绪出口。"
            scene c007_s010_057 with Dissolve(0.25)
            "我还是悄悄溜出去，别吵醒她。"
            scene c007_s010_058 with Dissolve(0.25)
            "嗯……处方药瓶。空掉的处方药瓶。我大概不该去翻——多半是治过敏或者偏头痛的——但要是她已经喝了不少，那这事可就有点麻烦了。"
            scene c007_s010_059 with Dissolve(0.25)
            "利培酮？拉莫三嗪？我完全不知道那是干什么用的。我可以去问别人，但这种信息我不该知道。所以，也许下次聊天时，让她自己主动告诉我吧。"
            scene c007_s010_060 with Dissolve(0.25)
            "现在先溜出去，找张床躺平吧。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_4_828", transition=Dissolve(1.0))()
    pause
    $ Hide("july_4_828", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s011_001 with Dissolve(2)
    play music morning fadein 2.0
    "第二天早上宿舍里很安静，看来姑娘们都睡了个大懒觉。没了平日那熙熙攘攘的动静做背景，我注意到隔壁房间有人活动也不算奇怪。所以我洗完澡回来、正准备再次出门时，肯定也被她们察觉到了。"
    "因为劳拉又一次想{a=https://www.merriam-webster.com/dictionary/go it alone}单独行动{/a}，我们又白白损失了一天，我得重新回到寻找装备和食物这件事上。到现在，我基本已经认命了：我们不会再徒步穿越整个校园了。劳拉那次的尝试——哪怕她自己都没想清楚就做了——已经证明这条路根本走不通。"
    scene c007_s011_002 with Dissolve(0.5)
    if k_friend >= 12:
        k "[player_name]？我好像听见你起床了。"
    else:
        k "嘿。我好像听见你起床了。"
    j "嘿，卡莉。你睡得好吗？"
    scene c007_s011_003 with Dissolve(0.25)
    k "还不错。劳拉还在休息。我想就剩你和我了。"
    j "抱歉把你吵醒了。"
    scene c007_s011_004 with Dissolve(0.5)
    k "没关系。我没必要整天闲躺着。事情该做的时候就得做。想来想去，你今天打算干什么？还有，别说你又要出门。你每次出门才穿外套。"
    j "那我们还是得给你弄件新外套和口罩。雪莉的也是。"
    scene c007_s011_005 with Dissolve(0.25)
    k "别出门。求你了。你昨天才刚出去过，我听得出你的呼吸状态不太好。虽然没劳拉那么严重，但你也不是百分之百没问题了。我们承受不起你生病或者受伤。"
    j "我们的时间正在一点点流失。存粮有限，说真的，根本不够撑。"
    scene c007_s011_006 with Dissolve(0.25)
    k "我们会想出办法的，但我求你今天为了自己的身体留下。倘若你非得做点什么才觉得自己有在做事，那就去哈灵顿楼吧。我敢肯定那边还有些我们没找到的东西。毕竟上次被打回来的时候，我们还有很多事没做完。"
    j "好吧好吧，我待在屋里，不过我打算花点时间待在那边。真的，我会好好把那地方翻一遍，看看能不能弄清楚怎么进到相连的那些楼里去。我实在不能再白白浪费一天了。"
    scene c007_s011_007 with Dissolve(0.25)
    k "就是别变成劳拉那样。行吗？我知道我们不能一直待在这儿，但我不想看到你也像她一样崩溃。"
    j "行。我……我需要有人提醒我，不能就这样接着她没做完的事干下去。谢谢。"
    scene c007_s011_008 with Dissolve(0.25)
    k "行吧。我想我得留在这儿？我不太确定自己要怎么同时看着门和看着劳拉。"
    j "我记得我们已经得出结论，宿舍到哈灵顿楼这段路不需要派人守着。而且我看劳拉已经缓过来了，也许你只要保证她在屋里来去没问题就行。"
    scene c007_s011_009 with Dissolve(0.5)
    k "这点事我还是能做的。前面她也替我做过。但这是不是就意味着，我们没法完全信任雪莉？"
    if ch7_sh_look == "yes":
        "我能说什么呢？她之前放了我鸽子，我对她是有顾虑的？而且翻看她的处方药已经侵犯了隐私——哪怕我可以把它说成是「必须知道」——我也没法把这件事告诉其他人。"
    else:
        "我能说什么呢？她之前放了我鸽子，我对她是有顾虑的。她年纪轻，而且总是不在，因为她老是跑去忙自己的事？"
    menu:
        "[gr]我只是习惯了就我们三个。":
            scene c007_s011_010 with Dissolve(0.25)
            j "我只是习惯了就我们三个。而且她年纪轻，可能还有点不靠谱。"
            k "我能理解。我小时候也不总在家，所以挺能体谅的。"
            scene c007_s011_011 with Dissolve(0.25)
            j "我实在想象不出你会走神。或者像她那样叽叽喳喳说个不停。"
            k "也不完全像她那样。*窃笑*"
        "[rd]她现在就是个难以预料的人。\n[rrd](卡莉 焦虑 +1)":
            $ k_anxiety += 1
            scene c007_s011_010 with Dissolve(0.25)
            j "说实话，她现在就是个难以预料的人。我没法让她确认会跟我们一起走，她也不止一次溜得不知去向。偏偏是我们最经不起意外的时候，她还这么不可预测。"
            j "我明白她年纪轻，这对她来说是个残酷的当头一棒，但四个人里，只有她我还没熟到能看透。是，劳拉当时出现了解离性崩溃，可我能预判她可能会做什么。要是事情崩了，我不知道雪莉会做什么。"
            scene c007_s011_011 with Dissolve(0.25)
            k "好、好吧，我明白你的意思了。我想，可能得花些时间才能慢慢信任她。"
            j "两个方向都是。是啊。"
    scene c007_s011_012 with Dissolve(0.25)
    j "好吧，那我该出发了。还是带上那把斧子，以防我得撬开什么门。不过走之前，我该去看看劳拉。"
    k "她刚才还在睡，所以如果她……你别惊讶。"
    j "昨天把她折腾得够呛，所以如果她还没醒，我就别叫醒她了。"
    if ch7_kallie_sex == "yes":
        scene c007_s011_014 with Dissolve(0.25)
        k "嘿。我……"
        j "小心点。我知道。"
        scene c007_s011_015 with Dissolve(0.5)
        "她是真的开始喜欢我吗？那些主动的肢体接触。还有做爱——但这感觉比「两个人随便找个地方打一炮」要多一点。而且，我自己确实也发现她非常可爱、非常让人想要。"
        scene c007_s011_016 with Dissolve(0.25)
        k "我……嗯，小心点。拜托了。"
        j "我会的。你也是。"
    else:
        scene c007_s011_013 with Dissolve(0.25)
        k "嗯。还有……"
        j "小心点。我知道。你也是。"
    k "我们都会小心的。"
    scene blank with Dissolve(2)
    scene c007_s011_017 with Dissolve(2)
    "卡莉提醒我果然没错。我探头看了一眼，劳拉还睡得死沉。不想吵醒她，我把门带上，打算回来再跟她聊。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c007_s012_001 with Dissolve(2)
    play music school fadein 2.0
    "好吧，我之前来过两次，所以大致知道会是什么样，也记得几处本来打算再去看看的地方。我担心一个暑假都没什么人的地方，不会剩下太多装备和补给可选，但我还是得尽到这份责任。"
    "我带上背包，把其余装备全塞了进去。不用再当导游，我说不定真能干点正事，推进我们的进度了。"
    scene c007_s012_002 with Dissolve(0.5)
    "我不想说得太难听，但昨天（天哪，感觉像过了一个星期）基本上就是在到处走，让卡莉自己随便逛，而我负责保驾护航。我想让她觉得自己更像是这件事的一员，而不是被人捧在手心里，哪怕我的第一反应还是想保护她，让她不受任何可能的伤害。"
    if ch7_kallie_sex == "yes":
        scene c007_s012_003 with Dissolve(0.5)
        "还有另一件事。从那之后，我就发现自己会用一些也许不该有的眼光去看她。她毕竟还是别人的未婚妻，即便等她回到家这一点就不再成立了。"
        "我不想让自己分心太重，但卡莉最近确实「主动」了很多（找不到更好的词），所以我忍不住想用浪漫的方式碰她。"
        scene c007_s012_004 with Dissolve(0.5)
        "可我的那些担忧和疑问都是真实的、经过考虑的：如果她真的只是因为我离得近才被我吸引呢？我就在她身边，而且一直稳定、一路支持着她。"
        "如果她回到北边父母那儿，从此再跟我也不联系了呢？如果那能让她摆脱安德鲁，我得学会接受才行。"
    scene blank with Dissolve(1)
    scene c007_s012_005 with Dissolve(1)
    "还有劳拉那档子事？操，我从没想过偏偏是她会那样突然绷断、迷失自己。她一直绷得太紧了，现在回头看，一切仿佛早有定论。不过昨晚多少让我松了口气。她看起来已经恢复了几分原来的样子。而且有人陪着，她就很满足了。"
    scene c007_s012_006 with Dissolve(0.5)
    "这就引出了一个问题：劳拉有多久没有单纯地和一个人同床而卧了？不是做爱，只是有个人能让她抱着。听他们说起来，她和基思在自己家里都几乎形同陌路。昨晚抱着她，大概是她很久以来第一次这样。"
    scene blank with Dissolve(2)
    scene c007_s012_022 with Dissolve(2)
    $ renpy.pause ()
    "*敲门* *敲门*" with vpunch
    s "{size=30}[player_name]？是我啦~~~{/size}"
    play sound doorclose
    scene c007_s012_023 with Dissolve(0.5)
    s "靠。你人根本不在。我白打扮了。"
    scene c007_s012_024 with Dissolve(0.25)
    s "可恶。"
    scene blank with Dissolve(2)
    scene c007_s012_007 with Dissolve(2)
    "我明明昨天就告诉过自己，这地方不值得一看，但我忽然想到，绘画课——那种会用油画颜料和溶剂的课——说不定会存放清洁用品。所以还是值得花十分钟去确认一下。"
    scene c007_s012_008 with Dissolve(0.5)
    "这儿也许没有跟食物或衣物相关的东西，但那绝不是我在找的唯一目标。说到我们需要的、能用的那些玩意儿，我得开始考虑的不再只是几个狭窄的类别了。"
    "哦，谢天谢地，门没锁。"
    scene c007_s012_009 with Dissolve(1)
    "啊，氨水和清洁剂那股冲鼻的味道。这儿的储藏室里东西还不少。要全部翻一遍得花些时间。"
    scene c007_s012_010 with Dissolve(0.25)
    j "那么，我们这儿有些什么？"
    scene c007_s012_011 with Dissolve(0.25)
    j "他妈的，中大奖了。"
    "一盒手套，还有看起来是一次性口罩。我把这些塞进包里，这样今天我也能说自己有点收获了。"
    scene c007_s012_012 with Dissolve(1)
    "下面那儿是什么？是宿舍楼和这栋楼之间的院子。从这儿我居然能看到东西。话说回来，雾还是那个讨厌的鬼样子，不过总比待在那下面强。"
    scene c007_s012_013 with Dissolve(0.5)
    "有动静。至少有一个灼烧者。不止一个。按照我们之前的讨论，他们是以前的学生吗？是住在这几栋宿舍楼里的男生吗？雪莉说得对吗——她以前就认识他们，在他们变成那样之前？如果是的话，得接触多少才会变成那样？我和劳拉在外面待了一阵子，但那点时间远远不够让我们落到这种地步。"
    scene c007_s012_014 with Dissolve(0.25)
    "那些一开始就在外面的人呢？是什么驱使他们能在那种地方待那么久，久到把自己搞成这副德行？是痛苦把他们压垮了吗？把他们逼疯了吗？然后他们连自保的本能都失去了？"
    scene blank with Dissolve(2)
    scene c007_s012_025 with Dissolve(2)
    play sound doorclose
    l "卡莉？[player_name]？{w=2}雪莉？"
    scene c007_s012_026 with Dissolve(0.25)
    l "有人吗？"
    play sound doorclose
    k "在这儿呢，这儿。来啦。"
    scene c007_s012_027 with Dissolve(0.25)
    k "我刚才在浴室里。"
    l "没事。我就是……*咳嗽*……刚醒，想弄清楚大家都在哪儿。[player_name]呢？"
    scene c007_s012_028 with Dissolve(0.25)
    k "他在哈灵顿楼那边，找补给和装备。已经过去两个小时了。"
    l "他不该一个人去的。"
    k "我知道，可他答应我会小心的。"
    scene blank with Dissolve(2)
    scene c007_s012_016 with Dissolve(2)
    "手里没有这地方的地图，我就只能靠眼睛判断这些楼到底有没有像我希望的那样连在一起。运气不错，透过最浓的雾我至少还能看到那些屋顶。"
    scene c007_s012_015 with Dissolve(0.5)
    "就我所能看清的，那个方向有个差不多大小的建筑。大概可以从我前几天看到的那扇门过去。可再往后呢？我想那边是学生中心。"
    "再往后？谁知道呢。这个只能走一步看一步了，因为我们必须尽量减少出门。我不知道我们还剩几个人能再受得住那种折腾。"
    scene blank with Dissolve(2)
    scene c007_s012_017 with Dissolve(2)
    "好吧，回去之前再确认最后一个猜想。我在这儿感觉已经待了好几个小时了，我敢肯定至少有一个人在担心。或者——我希望她们在担心。"
    scene c007_s012_018 with Dissolve(0.5)
    "到了。底层有几扇门通向另一栋楼。看看这扇有没有像另一扇那样被堵死。"
    scene c007_s012_019 with Dissolve(0.25)
    "看起来没人拖些家具来挡在门口。"
    scene c007_s012_020 with hpunch
    "*哐当* *哐当*"
    "果然。真是《寂静岭》那一套。"
    scene c007_s012_021 with Dissolve(0.25)
    "我倒想砸它试试，但也许不是今天。也不能一个人来。我已经觉得自己离其他人太远了，万一出了什么意外，我就完蛋了。不过，等我们重新动起来，这倒是个不错的起点。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_4_623", transition=Dissolve(1.0))()
    pause
    $ Hide("july_4_623", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s013_001 with Dissolve(2)
    play music nightmain fadein 2.0
    "我回来的时候，门口一个人都没有。我知道我出门时已经说服自己这事没那么重要，可还是有那么几秒钟，我担心出了什么岔子。我想，最近没完没了的意外已经让我神经太紧绷了。"
    j "我回来了。而且我带了礼物。"
    scene c007_s013_002 with Dissolve(0.25)
    "看来得我自个儿把所有东西搬回来了。"
    scene blank with Dissolve(2)
    scene c007_s013_003 with Dissolve(2)
    "是不是比我想的晚，大家都去睡了？应该没有吧。至少卡莉听说我回来会松一口气。劳拉要是还醒着，也会。"
    scene c007_s013_004 with Dissolve(0.25)
    "好的一面是，电视关着呢，所以没人会一直纠结「万一从新闻里听到什么动静」这种可能。"
    scene c007_s013_005 with Dissolve(0.25)
    l "[player_name]，我听见你回来了。我醒过来发现你已经出门的时候，卡莉跟我提过你在外面。"
    scene c007_s013_006 with Dissolve(0.5)
    j "嗯，我去了哈灵顿楼找东西。确实找到了一些手套和口罩，算是有收获。"
    j "而且我想，如果我能把通往后一栋楼的某扇门弄开——或者干脆砸开——我们大概就能从楼里穿过校园，不用再跑到外面去了。接下来得边走边摸索下一步该怎么走，但我感觉这条路是可行的。"
    l "雪莉能给你什么启发吗？"
    scene c007_s013_007 with Dissolve(0.25)
    j "不太行。她说过自己空间记忆不好，或者说不太认路。所以也许我们去的时候带上她会更好。也许她看到熟悉的地方，就能想起些什么。"
    l "她答应了吗？"
    scene c007_s013_008 with Dissolve(0.25)
    j "还没有，不过我跟她很明确地谈过她不能一直待在这儿这件事。我答应等我们更接近脱出去的时候再回头处理这个。对了，你现在怎么样？"
    scene c007_s013_009 with Dissolve(0.25)
    l "我……来，让我先坐下。"
    scene c007_s013_010 with Dissolve(0.5)
    l "我好多了。只是还是很累，呼吸还是很费劲。而且我今天脑子是清醒的，这个你就别担心了。我脑子里偶尔还是会冒出几句实况转播，但我的自制力现在强了些，所以这个理由足以压住那些「现在就走」的念头。"
    scene c007_s013_011 with Dissolve(0.25)
    k "劳拉？哦，你在这儿。我照你说的打了水。还有你一定是刚回来吧。我去看过后门，发现关着。"
    j "刚回来。我弄到了些手套和口罩，算是个开始。再弄到两件外套、帽子和护目装备，我们就能重新出发了。唔，前提是让这个家伙休养一段时间。"
    scene c007_s013_012 with Dissolve(0.25)
    j "还有，你们两个今天有谁听到雪莉的消息了吗？"
    k "没有，她一整天都待在自己房间里。"
    scene c007_s013_013 with Dissolve(0.25)
    j "好吧，呃……每个人都有权独处一会儿，而且我想她也有不少事要考虑。"
    l "我们该担心吗？"
    scene c007_s013_014 with Dissolve(0.25)
    j "我觉得不像。我发现她想说话的劲儿总是时有时无，所以现在她可能没什么聊天的兴致。不过我待会儿还是去跟她谈谈，确认一下。"
    l "好吧。听起来不错。"
    scene c007_s013_015 with Dissolve(0.25)
    j "不过，先让我从这儿出去。我觉得昨天那雾还残留在里面，所以——"
    l "嗯，嗯，我明白。"
    "看见劳拉能下床走动，气色也像是「回来了」，真好。我们还是得留意她有没有反复的迹象，但至少她还活着，我觉得自己已经很走运了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_4_842", transition=Dissolve(1.0))()
    pause
    $ Hide("july_4_842", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s013_016 with Dissolve(2)
    play music nightmain2 fadein 2.0
    j "呼……是啊。"
    "操，现在一放松下来，我才发现自己比预想的要累得多。昨天在哈灵顿楼里到处走，加上一大早的奔跑，全都在这时候找上门来了。这些年到处开车、活动量少得可怜，如今总算是切身体会到它的代价了。"
    scene c007_s013_017 with Dissolve(0.5)
    "不过至少劳拉的状态好多了。卡莉说她今晚会照看她。我……我本该预料到劳拉会崩溃的。我确实有点担心她绷得太紧会出问题，但我没想到她会那样直接断掉。"
    scene c007_s013_018 with Dissolve(0.5)
    "这一切开始以来，她一直承受着巨大的压力。担心儿子，为丈夫抓狂，还有那种一心想离开这里的渴望。她一直在硬撑，而事情不顺的时候，她的反应也很糟。我理解，我确实理解。可她没有随波逐流，而是把一切都往自己心里咽。"
    "是啊，我们得赶在情况变得更糟之前离开这座城，但怎么走必须讲究策略。而我觉得，我顺着她那股「赶紧走」的劲儿，已经迁就得太久了。"
    scene c007_s014_001 with Dissolve(0.5)
    "我觉得我们当中有些人应付这种烂事，就是比别人强。有些人需要固定的作息，需要起床、上班。而像我这样的人——独来独往，纯粹因为账单得付才去工作的——反倒更能扛住这种接二连三的冲击。"
    "我不是说我更喜欢现在这样，但总比我以前的日子强。"
    if s_friend >= 6 or s_desire >= 3:
        $ ch7_shelleyvisits = "yes"
        "*敲门* *敲门*" with hpunch
        j "什么事？"
        play sound doorclose
        scene c007_s014_002 with Dissolve(0.5)
        s "嘿，就我。我知道你失望了，但我尽量让你觉得值。"
        if ch7_sh_look == "yes":
            j "倒不是失望。就是这两天太累人，我有点撑不住了。啊，抱歉，我昨晚来得太晚了。我过去的时候，你已经睡着了。"
            scene c007_s014_003 with Dissolve(0.25)
            s "没关系。等一切平息下来，我才发现自己比原先以为的更累。就算我来了，估计也没什么兴致陪你。"
        else:
            j "倒不是失望。就是这两天太累人，我有点撑不住了。啊，抱歉，我昨晚没过去。我不是故意睡着的，只是大概比预想的更累。"
            scene c007_s014_003 with Dissolve(0.25)
            s "没关系。反正我去了估计也没什么兴致陪你。我很快就睡着了。"
        scene c007_s014_004 with Dissolve(0.25)
        s "那她怎么样？劳拉？今天我没能跟她说上话。我想给她留点空间，因为她对事情的反应不太好。倒不是说我不同情她。我……我最近有点不靠谱，而且你来了之后，还没见过我最好的一面。"
        j "她是被压力压垮了，只是需要休息一下。而且我们开的那辆车抛锚，也把她「能被救出去」的那点希望砸了个粉碎。"
        scene c007_s014_005 with Dissolve(0.25)
        s "看起来不只是这些，不过那大概属于私事，如果你不想跟我说，我也能理解。"
        j "谢谢。我想劳拉不会愿意把自己的某些事告诉陌生人。现在卡莉在照看她，以防她需要人陪或者需要什么东西。"
        scene c007_s014_006 with Dissolve(0.5)
        s "而你被撵出来了，所以今晚是一个人睡？真可惜，连个能跟你挤一张床的人都没有。"
        j "嗯？什么？"
        scene c007_s014_007 with Dissolve(0.25)
        s "兄弟，我不傻。自打你来了之后，这地方就一直他妈一股那个味儿。也许你一直在打手枪。那两个又那么火辣，我能理解。"
        s "不过我不知道是只有一个——还是两个都有——但既然她们俩手上都还戴着戒指，那说不定这算是种「通行牌」式的玩法：让她们自己爽够了，然后各回各家，各过各的生活。"
        j "我猜你已经把一切都算明白了，是吧？"
        scene c007_s014_008 with Dissolve(0.25)
        s "也许吧。也许没有。而且你大概也不是那种会往外抖家丑的人。女孩子挺欣赏这一点的。反正不欠谁什么。你给自己攒了个局面，稍微释放一下正好当个消遣，对吧？"
        j "听起来你挺懂这种感觉的。"
        scene c007_s014_009 with Dissolve(0.25)
        s "我可是上大学的人。没有哪个周末躲得过校园派对——那种场合里，酒劲和荷尔蒙一撞，出来的就全是些不靠谱的决定。"
        j "好吧，我今天累了一天。如果你想——"
        scene c007_s014_010 with Dissolve(0.25)
        s "也许我现在就想当个「不靠谱的决定」。"
        scene c007_s014_011 with Dissolve(0.25)
        s "喜欢吗？"
        if ch7_kallie_sex == "yes":
            "哦？雪莉又主动出击了。我该把这当成她单纯在撩人，还是……又或者，我是不是该{b}现在{/b}就叫停，因为我还想看看我和卡莉之间会走到哪一步？"
        else:
            "哦？雪莉又主动出击了。我该把这当成她单纯在撩人，还是就这样？"
        menu:
            "我不这么觉得。":
                j "我不这么觉得。我是说，摸着挺舒服的，但我累得半死，也没什么心情瞎搞。"
                scene c007_s014_052 with Dissolve(0.25)
                s "比你已经做过的还多？还是就今晚？"
                j "就今晚这么说吧。你又辣又年轻，换作别的情形，我肯定二话不说就答应了，但现在我实在一点力气都没有。"
                "我得斟酌一下措辞，别让她往心里去。因为说实话，如果一切恢复正常，她连正眼都不会看我一下。"
                scene c007_s014_053 with Dissolve(0.25)
                s "哦，你喜欢又辣又年轻的？还是只要是可能对你有意思的就行？"
                "感觉到一点火药味。不过至少她没再变本加厉地往上贴。还暂时没有。"
                j "嗯，要说我最近的人生记录嘛，就是没人看上我，外加一个看上别的男人的前任。"
                scene c007_s014_054 with Dissolve(0.25)
                s "那你或许该别再去招惹那些生活里还挂着别的牵挂的姑娘，转而守着那些清白自由、随时可用的女人。也许你就别再把人家的水搅浑，让她们更难回到自己原本的生活里。"
                if l_sex == 0 and k_sex == 0:
                    j "我不知道你以为是怎么回事，但它真的不是「那样」。"
                else:
                    j "也许事情没那么干净利落。我知道没那么简单，雪莉。相信我，我很清楚。而如果我真在做什么，我会尽可能小心地处理。"
                scene c007_s014_055 with Dissolve(0.25)
                s "管他的。随便你想怎么骗自己就怎么骗吧。滚开，伙计。"
                scene c007_s014_056 with Dissolve(0.25)
                if l_sex == 0 and k_sex == 0:
                    "得，来了。操，雪莉的心情糟透了。而且她说得没错，只是她不知道全部的事实，不知道我在这件事上的挣扎和她以为的一样多。不过在我们最终离开这地方之前，我得先跟她把这一页揭过去。"
                else:
                    "得，来了。操，雪莉的心情糟透了。也许刚才我算是躲过一劫吧，反正等我们最终离开这地方之前，我得先跟她把这一页揭过去。"
                play sound doorclose
                scene c007_s014_057 with Dissolve(0.25)
                "不过今晚不行。我太累了，没力气好好地、热血沸腾地为现状辩护。"
                "嘿，等一下。我记得她说过她没有外套也没有大衣？那她他妈穿的到底是啥？"
            "我不拒绝。\n[rgr](Shelly 爱意 +1)\n[rrd](雪莉 欲望 -1)\n[pks]":
                $ s_sex += 1
                $ s_love += 1
                $ s_desire -= 1
                $ ch7_shelley_sex = "yes"
                call ch7_shelley_sex from _call_ch7_shelley_sex
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_5_729", transition=Dissolve(1.0))()
    pause
    $ Hide("july_5_729", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c007_s015_001 with Dissolve(2)
    play music insideday fadein 2.0
    "第二天早上，我起床的时间可能比平时稍微晚了一点。身上好几处都在酸痛，那种酸不是因为睡姿不好，而是因为最近我走了太多路、站了太久。"
    "即便如此，我还是在盘算今天的行程，大概会去周边某栋宿舍楼。在离开这间宿舍之前，我至少还得找到一件外套和另外几样东西，才能心里踏实。"
    scene c007_s015_002 with Dissolve(0.5)
    "我走进起居室时，略微有些惊讶地发现劳拉已经在那儿等着我了。她的气色，是这一切开始以来最好的一次。"
    scene c007_s015_003 with Dissolve(0.5)
    j "早啊。今天穿得这么齐整？打算出门散步？"
    l "我……我好多了，[player_name]。我知道你担心，但我向你保证我没事。呃，说的是心理上。"
    scene c007_s015_004 with Dissolve(0.25)
    j "话虽如此。"
    l "你和别人提过哈灵顿楼。我想着，也许我能跟着去看看。跟你一起。我不会一个人去。至少在……之前不会。"
    "别的什么都不用说了。肺部的实打实的损伤，加上她随时可能旧病复发的隐忧，劳拉都还没到可以放心的时候。"
    scene c007_s015_005 with Dissolve(0.5)
    j "我今天本来打算去另一栋宿舍楼，不过要是我们动作快一点，我可以带你四处看看，让你大致了解我们到目前为止都发现了什么、摸清了什么。"
    j "目前看起来，最好的选择是穿过哈灵顿楼，再穿过下一栋楼，然后看看我们能不能一口气冲到学生中心。"
    scene c007_s015_006 with Dissolve(0.25)
    l "那样我们就能到……？"
    j "这个得等到了才知道，但至少能让我们横穿校园走完一部分。比我们现在待的地方要远。谁知道呢？也许多一双眼睛会有帮助。"
    scene c007_s015_007 with Dissolve(0.25)
    l "你带卡莉去看过了吧？"
    j "主要是走了个过场。她发现了几间办公室，我昨天都进去看过了。不过雪莉那天死活不肯离开宿舍楼，直到你出门那天才作罢。"
    scene c007_s015_008 with Dissolve(0.25)
    l "好吧。我……*叹气* 你就带我转几分钟吧。拜托。我想重新变得有点用处。"
    menu:
        "行，我们走一小会儿。[yl]":
            j "行，我们走一小会儿。不过，我今天真的必须去其中一栋宿舍楼一趟。"
        "真的吗？这么快？[yl]":
            j "真的？前天才出去过，这么快？劳拉——"
            scene c007_s015_009 with Dissolve(0.25)
            l "我知道你需要能重新信任我。但我保证我会明智行事，也会听指挥。我唯一能开始向你证明自己正在康复的方式，就是用行动。"
            j "*叹气* 好吧，不过{i}一切{/i}我都会盯着。而且我们只过去一小会儿。我今天真的必须去其中一栋宿舍楼一趟。"
        "你悠着点。[yl]":
            j "你悠着点。你说话的声音还像个老烟枪。"
            scene c007_s015_009 with Dissolve(0.25)
            l "我没时间彻底康复。至少让我觉得自己不再是个累赘。"
            j "好吧，既然你在这件事上这么固执，那我们就过去一小会儿。我今天真的必须去其中一栋宿舍楼一趟。"
    scene c007_s015_010 with Dissolve(0.25)
    l "我们不会待太久。回头我也会帮你盯着前门。"
    j "好吧，那我得跟卡莉说一声我们在哪儿，免得她担心。"
    "既然劳拉铁了心要这么做，我也不能说不。我们没有多余人手，能永远把她晾在一边。不过，也许我不在的时候，该让雪莉或者卡莉去照看一下她。"
    scene blank with Dissolve(2)
    scene c007_s015_011 with Dissolve(2)
    j "好了，情况就是这样。这栋楼我已经检查过了，很安全。没有破损，没有意料之外的住户。这里边里外外的东西我都翻得差不多了，除了书、家具和少量美术用品，我什么都没找到，除了我昨天弄到的那副手套和口罩。"
    scene c007_s015_012
    l "从这儿看附近的建筑，景色还不错。"
    j "如果进到教室那边，就能看见另一侧的院子。其实二楼那间美术教室最适合看这个。"
    scene c007_s015_013 with Dissolve(0.25)
    l "那隔壁那栋楼呢？"
    j "有两个入口。那边往下的一个锁着，我觉得从另一头还被堵死了。另一处在一楼，只是上了锁，用斧子狠狠干一下就能砸开。等我们准备好的时候。"
    scene c007_s015_014 with Dissolve(0.5)
    l "你已经没试过吗？"
    j "大家本来就都神经紧绷，我不想在没人体知道我行踪的情况下，走那么远。"
    scene c007_s015_015 with Dissolve(0.25)
    l "嗯，这主意不错。以后不该再让任何人处于可能有危险的境地而没有后援。"
    scene c007_s015_016 with Dissolve(0.5)
    j "好吧，你是想再往深处走走，还是回去？你的好奇心——"
    scene c007_s015_017 with hpunch
    "*哐啷* *哐当* *哗啦————*"
    l "刚才那他妈是什么动静？"
    j "听上去是从隔壁传来的。看来我们在这儿未必是独处。"
    if persistent.ch7_complete == False:
        $ persistent.ch7_complete = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_chapter7", transition=slideright)()
        pause
        $ Hide("achievement_chapter7", transition=dissolve)()
        $ quick_menu = True
label chapter08:
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("chapter08", transition=Dissolve(1.0))()
    pause
    $ Hide("chapter08", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c008_s001_001 with Dissolve(2)
    play music insidedark fadein 2.0
    l "操，那是什么声音？"
    j "听起来是某个又大又重的东西倒了。这种事不会自己发生，我该去看看。"
    scene c008_s001_002 with Dissolve(0.25)
    l "{b}我们{/b}该去看看。"
    j "如果你跟我去，那就照我说的做。我怎么说就怎么做，我什么时候说就什么时候动。我不是故意要摆臭脸，但是——"
    scene c008_s001_003 with Dissolve(0.25)
    l "我知道。我……我最近做的决定都不太好。我已经不是我自己了。"
    scene c008_s001_004 with Dissolve(0.5)
    j "我也不敢说自己有多聪明，劳拉，但万一出了什么岔子，你现在的状态根本应付不来。所以让我来打头阵，照我的命令来。如果我说「跑」，你就跑。明白吗？"
    l "明白。"
    scene blank with Dissolve(2)
    scene c008_s001_005 with Dissolve(2)
    j "看起来这是最好的入口。另一个在楼上，锁着，而且据我判断还被堵死了。这个呢？至少我们能看穿。除了给那把锁来一下，问题不大。"
    scene c008_s001_006 with Dissolve(0.5)
    j "那么，口罩带在身上了吗？该装备起来了。"
    l "我……带了。我把口罩和眼镜都放回大衣口袋里了。你说里面会有雾吗？"
    scene c008_s001_007 with Dissolve(0.25)
    j "不知道。在找到反证之前，我就当有。就算没有，如果真看到雾，你就立刻退回这儿来，明白吗？你最近暴露在外面的时间已经够久了。"
    l "我……我会的。"
    "她前阵子那场小休，估计把她折腾得不轻。把她吓得够呛，因为我从没见过劳拉这么顺从。这对我反而有利，我没工夫去应付她耍脾气。"
    scene c008_s001_008 with Dissolve(0.25)
    j "好，退后。我发起疯来可是不收着的。"
    scene blank with Dissolve(2)
    scene c008_s001_009 with Dissolve(2)
    j "好，等我一下。我四处看看。"
    "这边也是一样。看着还行，不过我还是得花上一两分钟确认一下。"
    scene blank with Dissolve(2)
    scene c008_s001_010 with Dissolve(2)
    j "行吧，这里面看来没有雾。考虑到这儿这么暖和，他们可能已经很久没开空调了。或者，有人足够聪明，把空调关掉了。"
    l "你觉得雾来了之后，还有人待在这儿吗？"
    scene c008_s001_011 with Dissolve(0.25)
    j "雪莉确实提过，她有几个室友往这个方向来了。谁知道他们走到哪儿了？所以我们得留意有没有人在附近。"
    l "比如刚才那声巨响的来源？"
    j "对，就是它。不过，我们别太引人注目。在确认这里的人是善意的之前，或者说，在确认这里是灼烧者之前。"
    scene c008_s001_012 with Dissolve(0.5)
    "说完这些，我和劳拉开始缓缓穿过这栋楼。"
    "我们从窗户往里看，检查没上锁的门，一楼找到的只有空荡荡的房间。有些房间的家具被搬空了，这让我怀疑，雾来袭前不久，清洁人员应该刚刚来过。"
    scene blank with Dissolve(2)
    scene c008_s001_013 with Dissolve(2)
    j "去二楼碰碰运气吧。"
    l "我不想说丧气话，但如果我们找不到那个声音的来源怎么办？"
    scene c008_s001_014 with Dissolve(0.5)
    j "如果那声音不是从这里传出来的，我们就探索的时候顺便留意着。而且，反正我们的计划就是穿过这栋楼横穿校园，顺便看看周边还有什么也不错。"
    l "你觉得那会是什么时候的事？"
    scene c008_s001_015 with Dissolve(1)
    j "等卡莉丢的装备补齐了，再给雪莉弄到一份，我们就出发。所以我才需要去查看一下别的宿舍楼。"
    l "好。"
    scene c008_s001_016 with Dissolve(0.25)
    j "哦？等一下。等等。"
    l "怎么了？"
    scene c008_s001_017 with Dissolve(0.25)
    j "呃……看看下面那扇门。拜托。"
    l "有什么问题？"
    scene c008_s001_018 with Dissolve(0.25)
    j "通路那边干净吗？那个门口？"
    l "不干净。门口堆着些东西。是谁把自己关在里面了？难道那是——"
    scene c008_s001_019 with Dissolve(0.25)
    j "对。我这边也看到东西了。"
    scene c008_s001_020 with Dissolve(0.25)
    "这看起来不太妙。看不太清是什么，但我觉得那是血。而且里面以前住着人吗？我得想办法进去。"
    menu:
        "[gr]让她留在走廊上。":
            $ ch8_laura_stay = "yes"
            j "劳拉，你在外面等着。我进去看看发生了什么。"
        "[rd]别。\n[rrd](劳拉 焦虑 +1)":
            "我可能需要她帮忙，我不能把她当成一碰就碎的人。但要是她在我面前开始焦虑，我就把她打发回宿舍楼去。"
            j "让我把这个弄开，看看里面是什么情况。"
    play sound hit
    scene c008_s001_021 with hpunch
    j "嗯唔~~！！操！！"
    j "有东西卡住门了。等我一下。"
    play sound hit
    scene c008_s001_022 with hpunch
    j "唔呃~~ 找到了，就在这儿。"
    "门开出一条缝，够我侧身挤进去。"
    if ch8_laura_stay == "no" and l_anxiety >= 5:
        scene c008_s001_023 with Dissolve(0.25)
        l "我……我想我还是待在外面吧。如果可以的话。"
        j "行，我先进去看看情况，你再进来。"
    if ch8_laura_stay == "yes" or l_anxiety >= 5:
        scene c008_s001_024 with Dissolve(0.5)
        "操，这也太挤了。让我……"
        j "哦，操。"
        scene c008_s001_025 with Dissolve(0.5)
        l "怎么了？"
        j "待在走廊里，等我一下。"
        l "[player_name]？"
        scene c008_s001_026 with Dissolve(0.5)
        "我的天哪。这里发生了什么？看样子是个学生。雪莉的室友之一吧。也许吧。这个东西掉在她身上了。看起来是被压死的。到处都是血。是你把自己关在这儿的吗？你他妈怎么会被落在这儿？还是你自己选择留下来的？"
        l "[player_name]？出什么事了？"
        scene c008_s001_027 with Dissolve(0.25)
        j "这里面有个死掉的女孩。我觉得她死了。我过去看看。"
        scene c008_s001_028 with Dissolve(0.25)
        j "没有脉搏。没有呼吸。是啊，她走了。"
        l "[player_name]？"
        j "没事的，劳拉。等我一下，我马上出来。"
        scene c008_s001_047 with Dissolve(0.5)
        "有根棒球棍。肯定是她的。我走的时候带上。交给劳拉吧。可怜这姑娘再也用不上它了。"
        scene c008_s001_048 with Dissolve(0.5)
        "而且看这情形，她在这儿已经待了一阵子了。"
        scene c008_s001_049 with Dissolve(0.5)
        "那么，呃，这是什么？《我看见了女巫？》我完全不明白。"
        scene c008_s001_050 with Dissolve(0.25)
        "那这个呢？她在这儿待了多少天？二十天？我们才过去三个星期吧？这不对啊。我自己都快记不清今天是哪天了。"
        scene c008_s001_049 with Dissolve(0.25)
        "不过这个「女巫」是怎么回事？是她以为自己看到的，还是真有其事？她从窗户望出去的视野，说不定让她看见了什么，然后她把它想象成了某种怪物。"
        "见鬼，也许这就是她对灼烧者的叫法。又或者它完全指别的东西，只是我硬要把它和我们现在的处境联系起来。"
        scene c008_s001_042 with Dissolve(0.5)
        l "[player_name]？我不是要黏着你，但是……"
        j "再等一下。我马上就出来。"
        "我想这里也没什么可做的了。不过至少让我先把这个东西从她身上挪开。就这样把她留在那儿，我觉得不对劲。"
        scene c008_s001_044 with Dissolve(0.5)
        "试了好几次，我终于把那个铁皮柜从她身上抬开了。"
        scene blank with Dissolve(1)
        scene c008_s001_046 with Dissolve(1)
        "我替她摆好一个像样的葬礼姿势，然后觉得是时候走了。"
        scene c008_s001_051 with Dissolve(1)
        l "里面怎么回事？"
        j "里面有个死掉的女孩。看着像个大学生，应该是躲在这个房间里躲了很久。大概是宿舍楼里的某个姑娘。"
        scene c008_s001_052 with Dissolve(0.25)
        l "靠，糟了。我们得告诉雪莉这件事。"
        menu:
            "是的。\n[rgr](劳拉 信任 +1)":
                $ l_trust += 1
                j "是的。把一切都说清楚，我们才能为可能发生的事做好准备。因为这局面他妈一天比一天糟。我已经见过太多尸体了。"
            "我们真要告诉她吗？\n[rrd](劳拉 信任 -1)":
                $ l_trust -= 1
                j "要告诉吗？如果她没看见这个，她就真的需要知道这种事吗？她本来就有点闷闷不乐，我们何必再雪上加霜。"
        scene c008_s001_053 with Dissolve(0.25)
        l "嗯，我不知道。我现在这个精神状态，没法做决定。还是太麻木了。"
        j "那你没进来反而是好事。看样子她在这儿待了很久。她瘦得皮包骨。而且那股尿骚味，可不是什么好兆头。"
        scene c008_s001_054 with Dissolve(0.25)
        j "她一定是掉队了，把自己锁在了这儿。因为灼烧者？因为其他人？因为她实在受不了这种狗屁倒灶的事？谁知道呢。长时间独自一人，足以把人逼疯。"
        j "也许她以为安全了就试着逃出去，却因为缺乏食物虚弱得连挪动这个铁皮柜的力气都没有，结果柜子倒下来砸在她身上。"
        l "*叹气* [player_name]，别让我变成她那样。疯疯癫癫，孤零零地死在一个房间里。求你了。我知道刚才我失控了，但你答应我，你不会落到这种地步。"
        scene c008_s001_055 with Dissolve(0.25)
        j "不会发生的。你，我，卡莉，雪莉，我们四个要一起出去，就算得我把你们一个个背出去。"
        l "谢谢。"
        scene c008_s001_056 with Dissolve(0.25)
        j "我倒是找到了一根棒球棍，也算是个收获。"
        l "应该算是好消息吧。不过感觉还是有点瘆人。"
        j "我想，我们开始穿别人的衣服那会儿，早就越过这条线了。"
    else:
        scene c008_s001_024 with Dissolve(0.5)
        "操，这也太挤了。让我……"
        j "哦，操。"
        scene c008_s001_025 with Dissolve(0.5)
        l "怎么了？"
        j "先退开一下。"
        l "[player_name]？"
        scene c008_s001_026 with Dissolve(0.5)
        "我的天哪。这里发生了什么？看样子是个学生。雪莉的室友之一吧。也许吧。这个东西掉在她身上了。看起来是被压死的。到处都是血。是你把自己关在这儿的吗？你他妈怎么会被落在这儿？还是你自己选择留下来的？"
        $ l_anxiety += 1
        l "[player_name]？她……？"
        scene c008_s001_029 with Dissolve(0.25)
        j "我觉得她死了。我过去看看。"
        scene c008_s001_030 with Dissolve(0.25)
        j "没有脉搏。没有呼吸。"
        l "靠，糟了。我们得告诉雪莉这件事。"
        menu:
            "是的。\n[rgr](劳拉 信任 +1)":
                $ l_trust += 1
                j "是的。把一切都说清楚，我们才能为可能发生的事做好准备。因为这局面他妈一天比一天糟。我已经见过太多尸体了。"
            "我们真要告诉她吗？\n[rrd](劳拉 信任 -1)":
                $ l_trust -= 1
                j "要告诉吗？如果她没看见这个，她就真的需要知道这种事吗？她本来就有点闷闷不乐，我们何必再雪上加霜。"
        scene c008_s001_031 with Dissolve(0.5)
        l "嗯，我不知道。我现在这个精神状态，没法做决定。还是太麻木了。"
        j "你要不要先出去透透气？"
        scene c008_s001_032 with Dissolve(0.25)
        l "不，不。我没事。你觉得她是怎么落到这步的？看样子她在这儿待了很久。"
        j "她掉队了，把自己锁在了这儿。因为灼烧者？因为其他人？因为她实在受不了这种狗屁倒灶的事？谁知道呢。长时间独自一人，足以把人逼疯。"
        scene c008_s001_033 with Dissolve(0.25)
        j "也许她以为安全了就试着逃出去，却因为缺乏食物虚弱得连挪动这个铁皮柜的力气都没有，结果柜子倒下来砸在她身上。"
        j "她瘦得皮包骨。而且那股尿骚味，可不是什么好兆头。"
        scene c008_s001_034 with Dissolve(0.25)
        l "这儿就有一根棒球棍。"
        scene c008_s001_035 with Dissolve(0.25)
        j "真的？拿去吧。她再也用不上了。"
        l "*叹气* [player_name]，别让我变成这样。疯疯癫癫，孤零零地死在一个房间里。求你了。我知道刚才我失控了，但你答应我，你不会落到这种地步。"
        scene c008_s001_036 with Dissolve(0.25)
        j "不会发生的。你，我，卡莉，雪莉，我们四个要一起出去，就算得我把你们一个个背出去。"
        scene c008_s001_037 with Dissolve(0.25)
        l "谢谢。"
        scene c008_s001_038 with Dissolve(0.5)
        $ ch8_laura_witch = "yes"
        j "那么，呃，这是什么？"
        l "《我看见了女巫》？我完全不明白。"
        scene c008_s001_039 with Dissolve(0.25)
        l "那这个呢？她在这儿待了多少天？二十天？不对啊。只过了十八天而已。"
        j "就按你说的算吧。也许她自己数乱了日子。有点……我觉得不用再往下说了。"
        scene c008_s001_040 with Dissolve(0.25)
        "不过这个「女巫」到底是怎么回事？是她以为自己看到的，还是真有其事？她从窗户望出去的视野，说不定让她看见了什么，然后她把它想象成了某种怪物。见鬼，也许这就是她对灼烧者的叫法。"
        scene c008_s001_041 with Dissolve(0.5)
        l "我想这里也没什么可做的了。"
        j "*叹气* 至少让我先把这个东西从她身上挪开。就这样把她留在那儿，我觉得不对劲。"
        l "好。来，把斧子给我。"
        scene c008_s001_043 with Dissolve(0.5)
        "试了好几次，我终于把那个铁皮柜从她身上抬开了。"
        scene blank with Dissolve(1)
        scene c008_s001_045 with Dissolve(1)
        "我替她摆好一个像样的葬礼姿势，然后觉得是时候走了。"
        scene blank with Dissolve(1)
    scene c008_s001_057 with Dissolve(1)
    l "我们回去吧？还是你想再多看看？说实话，这已经超出我能承受的范围了，而且这一切让我有点心神不宁。"
    "她崩溃也才没过多久。带她出来，可能是我太急了。"
    j "嗯，我们得回去了。这次出门本来不在计划内，我敢肯定卡莉正担心我们俩都出事了。我今天晚些时候再来，把这地方好好搜一遍。往外探索的事，今天可以先放一放。"
    scene c008_s001_058 with Dissolve(0.25)
    j "再说，就算还没发现那个姑娘之前，你看起来和听起来都已经有点疲惫了。"
    l "确实。操，我讨厌这种感觉。不过这都是我自己的问题。所以整个人垮下来了，跟一个月前完全不是一个人。"
    scene c008_s001_059 with Dissolve(0.25)
    j "其实我们谁都不是。不管怎样，我们回去吧，把消息告诉她们。然后等我把这轮搜索做完，你可以去后门守着，如果你愿意。因为我不能保证只有她一个人还在附近徘徊，我必须确认清楚。"
    scene c008_s001_060 with Dissolve(0.25)
    if ch8_laura_witch == "yes":
        l "那「女巫」的事呢？"
        j "我们自己知道就行。那可能只是一个疲惫饥饿的大脑编出来的东西。"
        l "好。我能理解。"
    else:
        "至于「女巫」的事，我会自己烂在肚子里。那可能只是一个疲惫饥饿的大脑编出来的东西。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c008_s002_001 with Dissolve(2)
    play music school fadein 2.0
    "我们默默地往回走。我想劳拉正用她自己的方式消化刚才那一幕。希望这不会让她想起彼得——他大概也是差不多的年纪。"
    scene c008_s002_002 with Dissolve(0.5)
    l "这是真的，对吧？"
    j "劳拉？"
    scene c008_s002_003 with Dissolve(0.5)
    l "不，不，我没有再次解离。倒有点希望自己是在解离。这太疯狂了。一切都随着时间推移变得越来越他妈离谱。怪物。他妈的怪物。尸体。操，那些死人。"
    j "一辈子都看不够。"
    scene c008_s002_004 with Dissolve(0.25)
    l "是啊。第一个？那个在{i}汉堡店{/i}的男人？我当时大概没真正反应过来。感觉一切都那么不真实，像在做噩梦。他不过是个涂满了红漆的人偶——我就是这么给自己解释的。可那个女孩呢？我……操，[player_name]。"
    j "我知道。她身上还是热的。她才刚……是啊。我……要是我能早一点找到她……"
    scene c008_s002_005 with Dissolve(0.25)
    l "你可能会眼睁睁看着她死掉，仅此而已。我们不是医生，这里也不是医院。那个铁皮柜一旦砸到她身上，我们什么都做不了。"
    j "唉。这话真够冷血的。"
    "她说得没错。我当时能做什么？守着她，让她别一个人死？"
    scene c008_s002_006 with Dissolve(0.25)
    l "你救不了所有人。我知道这话从我嘴里说出来有多怪，但你真的救不了。我们甚至不知道她在那儿。"
    j "那么问题就变成了：外面还剩下多少这样的人？像我们一样被困在某个地方？"
    "也没变成那些灼烧者——如果那真是正在发生的事的话。"
    scene c008_s002_007 with Dissolve(0.25)
    l "我都不知道。也许我宁愿不知道。我们回去吧。我撑不了多久了。看来我还是那么容易就气喘。"
    scene blank with Dissolve(2)
    scene c008_s002_008 with Dissolve(2)
    j "来，我扶你坐下。"
    scene c008_s002_009 with Dissolve(0.5)
    l "抱歉。看来我们这趟小散步比我预想的更久。"
    scene c008_s002_010 with Dissolve(0.5)
    j "没关系。至少我们找到了之前一直在说的那件额外武器。我去拿我的帽子和手套，以防万一。我知道我们没看到什么……"
    j "我本来想说「糟糕」，但现在这词已经不适用了。"
    scene c008_s002_011 with Dissolve(0.5)
    s "你们两个他妈跑哪儿去了。我们正担心你们去哪儿了呢。你们没回应的时候，我们急坏了。"
    scene c008_s002_012 with Dissolve(0.25)
    s "{size=50}卡莉！我们在楼下起居室！{/size}"
    j "我们没料到会这么久。"
    scene c008_s002_013 with Dissolve(0.25)
    s "我们一起床发现你俩都不见了的时候，都快疯了。"
    scene c008_s002_014 with Dissolve(0.5)
    s "我不想撒谎说我以为最坏的情况发生了，以为你们又出去了。不过在这地方被憋疯，我也不会怪你们。"
    scene c008_s002_015 with Dissolve(0.25)
    k "我的天哪，你们两个跑哪儿去了？"
    l "抱歉。是我让[player_name]带我去哈灵顿楼待一会儿，然后……"
    scene c008_s002_016 with Dissolve(0.5)
    menu:
        "我们没注意时间。\n[rrd](卡莉\雪莉 信任 -1)":
            $ s_trust -= 1
            $ k_trust -= 1
            j "我们没注意时间。"
            scene c008_s002_017 with Dissolve(0.25)
            l "不，别在这件事上撒谎。别瞒着她们，[player_name]。她们需要知道，尤其是我们之后还得从那边过去。"
            s "出什么事了？"
            j "隔壁那栋楼传来一声巨响，我们就去查看了一下。"
        "[gr]我们听见隔壁那栋楼传来一声巨响。":
            j "我们听见隔壁那栋楼传来一声巨响，就去查看了一下。"
            scene c008_s002_017 with Dissolve(0.25)
            k "什么？什么声音？"
            l "你就告诉她们吧。她们需要知道。"
    scene c008_s002_018 with Dissolve(0.25)
    j "我们费了点劲才摸过去，又花了一会儿才找到声音的来源。在二楼，我们发现一间被封住的教室，里面住着人。"
    scene c008_s002_019 with Dissolve(0.25)
    s "靠，操……操……"
    k "住在那儿？那是谁？既然她没跟你们一起回来……她跑出去了？"
    j "不。我不知道发生了什么，但我们到的时候，发现有一个{i}人{/i}被压在铁皮柜下面。柜子倒了。那就是我们听见的声音。我猜她是想出去。从现场的样子看，她在那儿待了有几个星期。"
    scene c008_s002_020 with Dissolve(0.25)
    k "她——"
    j "死了。在我们赶到之前。被那个柜子砸死了。如果我们知道她在那儿……"
    scene c008_s002_021 with Dissolve(0.25)
    s "她？是谁？她长什么样？"
    "是的，雪莉认识这个女孩。这大概会让她彻底崩溃，但既然已经走到这一步了，我总不能聊到一半就停下。"
    j "个子不高。浅棕色头发，扎着两条辫子。她穿着裙子和一件紫色上衣。"
    scene c008_s002_022 with Dissolve(0.25)
    $ s_anxiety += 1
    s "靠，梅茜。靠，靠靠靠。"
    k "对不起，雪莉。我……"
    scene c008_s002_023 with hpunch
    j "操，我……我不是希望她用这种方式知道的。我当时就有种不好的预感，觉得那可能是她的朋友。"
    scene c008_s002_024 with Dissolve(0.25)
    l "我们总得去一个人。她这时候需要有个人陪着。她刚刚得知认识的人死了。"
    k "我去吧。我可能不知道该说什么，但我很擅长听。"
    j "嗯，那大概是最好的安排。既然坏消息是我带回来的，不过如果你需要帮手，或者她开始说些奇怪的话、做些奇怪的举动，就来找我们。"
    k "我……我会的。"
    scene c008_s002_025 with Dissolve(0.5)
    l "[player_name]……？"
    j "我得回去把这栋楼彻底搜一遍，看看我们能从哪儿接上。既然封印已经破开了，我们也没法再装作不知道。"
    scene c008_s002_026 with Dissolve(0.25)
    l "好。"
    j "我去把剩下的装备拿上。"
    scene c008_s002_027 with Dissolve(0.25)
    "{color=#66ff33}[player_name]这次真的受到了很大打击。他在硬撑，但我看得出他被搅乱了。{/color}"
    scene blank with Dissolve(2)
    scene c008_s003_001 with Dissolve(2)
    "卡莉能去陪雪莉真是太好了。我做不到。我现在勉强才撑得住。一件破事接一件破事。我们连喘口气的机会都没有，而我也远没有像自己应该做的那样去消化这一切。"
    "我他妈为雪莉感到无比愧疚。为梅茜。操我要是我动作再快一点，或者早点知道她在那儿，她可能还活着。见鬼，也许她是因为听见我们的声音才想逃出来的。太多问题，太多的愧疚。"
    scene c008_s003_002 with Dissolve(0.5)
    "但我必须做那个坚毅的人。那个去干实事的人。因为卡莉受了伤（而我很清楚自己在做什么，所以心里特别想照顾她），劳拉还相当脆弱，而我还不信任雪莉能办成什么事。"
    scene c008_s003_003 with Dissolve(0.5)
    "天哪，我他妈被困在一个{a=https://en.wikipedia.org/wiki/Catch-22_(logic)}第22号军规{/a}里了。人们抱怨男人没有复杂的情感、不懂得处理情绪，却不明白我们往往就是靠动手做事来应对的。或者，干脆在这栋楼的某个角落里一个人待着，因为去过度分析我们心理版图里的细微差别，纯粹是浪费时间和精力。"
    "但要是我真的崩溃了、好好哭上一场呢？那我就是个软弱、有缺陷的人。我心肠软，撑不起所有人期待的那个支柱。那个永远可靠、没有感情、只是一步一步往前挪的机器。一次又一次地把自己扔进危险里。"
    scene blank with Dissolve(2)
    scene c008_s003_004 with Dissolve(2)
    "好了，自怜就先到此为止。我只是紧绷、疲惫，而且他妈浑身疼。我的肺感觉还是糟透了。而且最近我漏掉的饭太多了。见鬼，我有一个多星期没拉过一场像样的屎了。我这身体现在大概是把吃下去的喝下去的每一点东西都攒着。"
    "我们确认一下别再有别的「惊喜」了。"
    scene blank with Dissolve(2)
    scene c008_s003_010 with Dissolve(2)
    s "我、我只是*抽噎*，不敢相信梅茜没了。她……她跟其他人一起走了，我、我当时就觉得不对劲。我就是……感觉不对，b、可是她和布丽想走。"
    s "我留下来，是因为我实在不想跟那几个男生一起走。我、我本来该拦住他们。说点什么把他们留下来。"
    scene c008_s003_011 with Dissolve(0.25)
    k "对不起。我不知道还能说什么。这一切感觉都太……不真实了。就这么得知你认识的人没了。你们是朋友吗？关系好吗？"
    s "我和布丽*抽噎*关系还不错。还有特里安娜。天哪，她怎么了？我……我都不想知道。可是，梅茜她……"
    scene c008_s003_012 with Dissolve(0.25)
    s "我们……*抽噎*我不能算很好的朋友。不过我们算是……比较亲近吧。毕竟我们俩暑假都留在宿舍楼里。我知道一些关于她的事。"
    k "我……我很抱歉。"
    scene c008_s003_013 with Dissolve(0.25)
    s "靠，我……我们要死在这儿了，对吧？"
    k "不，不，我们不会的。我们很快就会离开，然后去那家医院，接着我们就会被疏散出去。"
    scene c008_s003_014 with Dissolve(0.25)
    s "你、你真这么觉得？就这么*抽噎*简单？"
    if k_trust >= 6:
        k "不会容易，但我相信这个计划。我相信[player_name]。"
    else:
        k "不会容易，但我相信这个计划。"
    s "我只是……*抽噎* *抽泣*"
    scene blank with Dissolve(2)
    scene c008_s003_005 with Dissolve(2)
    "整栋楼彻底搜完之后，这儿基本什么都没有。一个房间里有几个空食品包装袋，还有几扇破碎的窗户和翻倒的课桌，像是曾经住过一帮闹腾的租客。我敢打赌是跟梅茜一起离开宿舍楼的那帮人。接下来路上我得留神找找他们。"
    scene blank with Dissolve(2)
    scene c008_s003_006 with Dissolve(2)
    "从这儿看，我们想再往前走就必须出门了。不过我们可以穿过这片草坪到学生中心，再从那儿计划下一步。"
    scene blank with Dissolve(2)
    scene c008_s003_007 with Dissolve(2)
    "我实在放不下梅茜。她的宿舍房间是哪一间？就是我现在用的这间吗？她是一瞬间就死了，还是在我们蹑手蹑脚绕过去的时候慢慢失血而死？她看起来没我最初担心的那么惨，但她还是死了。"
    "你看起来像是刚高中毕业。不管你父母在哪儿，总得有人去通知他们。还有雪莉？最好别带她过来。我们出发的时候绕开这一整条走廊。"
    scene c008_s003_008 with Dissolve(0.5)
    "既然都到这儿了，我干脆翻翻她的包。感觉像是盗墓，但为了活命，这又是另一件我得强行压下去的事。万一里面除了化妆品和卫生棉条还有别的什么呢。"
    scene blank with Dissolve(1)
    scene c008_s003_009 with Dissolve(1)
    "好，一副墨镜。就这样慢慢凑吧，我已经攒够让我们离开这儿的东西了。明天我必须去那些宿舍楼。不许再磨蹭，不许再被打断。"
    "时间不早了，我该回去了。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_5_640", transition=Dissolve(1.0))()
    pause
    $ Hide("july_5_640", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c008_s003_015 with Dissolve(2)
    play music nightmain fadein 2.0
    "感觉比平时脆弱一些，我特意花时间把哈灵顿楼和另一栋楼之间连通的那道门堵上了（要不是雪莉现在这个状态，我本来会问问那栋楼叫什么）。"
    "回到宿舍后，我重新把后门堵了起来。就算没有证据支持，我也不想让任何人或者什么东西在夜里摸回我们这儿。"
    scene c008_s003_016 with Dissolve(1)
    "我又累又窝火，拖着沉重的步子回到我的房间（或者那是梅茜的？），然后动手脱掉装备。"
    scene c008_s003_017 with Dissolve(1)
    "没有空调，厚外套和棒球帽把我捂出了一身细汗，我不得不把那些布料从身上剥下来。"
    play sound doorclose
    scene c008_s003_018 with Dissolve(0.5)
    l "[player_name]？我好像听见你回来了。"
    scene c008_s003_019 with Dissolve(0.5)
    j "嗯。刚忙完。我尽力把那地方搜了一遍。封得挺严实的。或者说，够我们用了——我们只需要用它去到别的地方。"
    l "怎么样？"
    j "最远那头一楼的出口正对着学生中心。路不短，所以我们得装备齐全，不过应该能走过去。但考虑到我在外面见过那么多灼烧者，我们动作得快。我不知道他们是怎么追踪我们的，我不想再来一次伏击。"
    scene c008_s003_020 with Dissolve(0.25)
    l "再往前呢？"
    j "我对这个校园还不够熟，说不上来。到了那儿我才能更有把握。运气好的话，我们能停一会儿，看看附近有没有别的、更合适的选择，最多停留到上完厕所，也许再看看有没有吃的。"
    j "我又找到了一副墨镜，这样就还差一副，再加几顶帽子，还有给卡莉找的另一件外套。也许雪莉自己有墨镜，我还没问过。她……？"
    scene c008_s003_021 with Dissolve(0.25)
    l "卡莉一直陪着她。得知那个女孩的事，她整个人都垮了。听上去她们关系很近。或者说，她足够了解那个女孩。"
    j "她们住同一间宿舍，用名字直接称呼彼此。可能就这么简单。"
    scene c008_s003_022 with Dissolve(0.25)
    l "再加上这对她来说也许是个警钟。这就是真的了。而且有人在死。有些死因，我以前以为自己不会碰上，直到我失去理智、想自己一个人走出这儿。"
    j "是啊，压力和绝望会让人变得孤注一掷。"
    "这话从她嘴里说出来，可算是很私人的坦白了。大概是因为今天的事，她觉得有点难为情。"
    menu:
        "你还好吗？\n[rgr](劳拉 好感 +1)":
            $ l_friend += 1
            j "那么，你还好吗？我知道今天本来只是简单转一圈就回来的。我们原定的计划算是泡汤了。"
            scene c008_s003_023 with Dissolve(0.25)
            l "累。我大概很快就要睡了。我只是想确认你平安回来了。"
        "随它去吧。":
            "最好什么都别说。她这么要强的女人，肯定早就烦透了依赖别人。尤其是我还一遍又一遍地提起这件事。"
    scene c008_s003_024 with Dissolve(0.5)
    l "你……你明天会去其他宿舍楼吧？"
    j "一早就去。我们离逃出去已经很近了，我不想再浪费任何时间。"
    scene c008_s003_025 with Dissolve(0.25)
    l "你走之前叫醒我。我能做的最起码就是在门口放个哨。而且我保证乖乖的。我之前那些……胡闹，已经足够让我自己清醒了。"
    j "周围死的人已经够多了，所以要是能再避开点创伤，我会很感激。"
    scene c008_s003_026 with Dissolve(0.25)
    l "我知道，我也很抱歉。"
    j "没事。真的没事。"
    if l_sex >= 2:
        scene c008_s003_027 with Dissolve(0.25)
        "劳拉抱我的时候，一句话也没说。我知道我们之间有些话该说，但谁都没能鼓起力气或者勇气。"
        scene c008_s003_028 with Dissolve(1)
        "我们沉默了几分钟，然后劳拉道了晚安，回床上睡了。"
        scene c008_s003_029 with Dissolve(1)
        "我不骗自己：那一刻我确实想过，也许会有什么后续。但看来我「我们之间的打闹真的已经结束了」这个假设是对的。我不打算在这件事上逼她，尤其是以她最近的状态。我不想把事情弄得更乱。"
        if ch7_kallie_sex == "yes":
            "然后就是我和卡莉之间那档子事。等我们离开这儿，她也有自己的顾虑要面对。我是不是也让她的处境变得更难了？还是说，有个人对她好这一点，反而让她从安德鲁那套精神操控里得到了某种清醒？"
    else:
        scene c008_s003_029 with Dissolve(1)
        "我们之间又沉默了几分钟，气氛有些不安，然后劳拉道了晚安，回床上睡了。"
    scene c008_s003_030 with Dissolve(0.5)
    "我在那儿站了太久，拿不定主意是该直接睡，还是先找点东西吃再睡。明天早上反正很快就到了。"
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_5_919", transition=Dissolve(1.0))()
    pause
    $ Hide("july_5_919", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c008_s004_001 with Dissolve(2)
    "尽管今天的事已经把我榨干了，我还是很难入睡。在宿舍床上摊了好像好几个小时之后，我放弃了这种令人沮丧的努力，起身下床。"
    scene c008_s004_002 with Dissolve(0.5)
    "有那么一瞬间，我想看看我带回来的那瓶威士忌里还剩下点没有。灌上几杯说不定就管用了，尤其是空着肚子的时候。我不会说出口，但这些天我一直在压缩自己的进食量，好确保存粮能多撑几天。"
    scene c008_s004_003 with Dissolve(0.5)
    "当我看见卡莉坐在沙发上、手里拿着书、似乎完全沉浸在自己的世界里时，你可以想象我有多惊讶。我怀疑我足足站了五到十秒她都没发现我。对她来说，这大概是个不错的逃遁之所。我考虑过悄悄退开，把这一刻留给她。"
    scene c008_s004_004 with Dissolve(0.25)
    if k_friend >= 10:
        k "啊，[player_name]。你还没睡？"
    else:
        k "啊。你还没睡？"
    scene c008_s004_005 with Dissolve(0.25)
    j "我正想对你说同样的话。*轻笑*"
    k "嗯，我想着其他人应该都睡了，自己又有点坐不住，就决定拿本书看看，看到困了为止。"
    j "这主意不坏。没有电视也没有网络，我们说不定得回到二十世纪初的生活方式了。反正你和我都不会记得那是什么样子。"
    scene c008_s004_006 with Dissolve(0.5)
    j "那雪莉怎么样了？我回来得晚，她已经睡了，我就不想打扰她。她这人忽冷忽热的，我从她那儿得不到什么准话。"
    k "她情绪上确实不太稳定。这并不说明她是个坏人，但我感觉她难以预测。"
    if ch7_sh_look == "yes":
        "也许那就是她的处方药治的。我改天该问问她。我不会跟其他人提起，因为那样对她不公平。"
    scene c008_s004_007 with Dissolve(0.25)
    k "她……你能想象她为此有多崩溃。我尽量陪在她身边、给她支持，但除了「对不起」，我不知道还能说什么。每当这种时候，我就真切地觉得自己身上有什么地方是坏的。"
    j "你没有坏。我们每个人都有在那种当口不知道该说什么的时候。所以才有了「为你祈祷」这种说法。因为太多人想表达关心，却没有言语或文字的工具去表达。"
    scene c008_s004_008 with Dissolve(0.25)
    j "在当下说不出合适的话，这只是因为你是人。我们身边没有电影编剧随手递来一段最完美的台词。大多数时候，一个人需要的只是有你在旁边。如果你不知道她为什么难过，那才真有问题。"
    k "我知道。其实在她跑开之前，我就有预感她会用那种方式来接受这个消息。我自己没经历过这种事——我想我是运气好——但我年轻时参加过不止一场葬礼。家族人丁兴旺，所以只要哪位伯公或者三表亲过世，我们就得去。"
    scene c008_s004_009 with Dissolve(0.25)
    k "不过说回雪莉……她……我觉得她和梅茜在某种意义上挺亲近的。也许算不上朋友。但是……她说的那些话，听起来像是失去了一个关系很近的人，哪怕那种亲近并没有持续多久。"
    j "她们之间会不会是恋人关系？"
    scene c008_s004_010 with Dissolve(0.25)
    k "我不知道。也许吧。我不想擅自假设什么。"
    k "不过我离开的时候，她的情绪已经被掏空了。我把她弄上了床。希望她睡一觉就能缓过来，但我觉得接下来一段时间我们还是得对她小心些。"
    j "可以理解。"
    scene c008_s004_011 with Dissolve(0.25)
    k "你……你还好吗？"
    menu:
        "还好。就是又累又亢奋。[yl]":
            j "我没事。就是又累又亢奋。你知道那种想睡却睡不着的劲儿吧。我现在就是那样。"
            k "……"
        "我已经受够了死亡。[yl]":
            j "说真的，我已经受够了死亡。受不了每探索一栋新楼都提心吊胆。受不了外面那些烂事，包括灼烧者。我真的……累了。抱歉，这话没能让你好受点。"
            k "没事。我宁愿你跟我说实话。"
    scene c008_s004_012 with Dissolve(1)
    k "我……进那栋楼安全吗？就像前天那样？只是四处看看？"
    j "呃，是安全的。哈灵顿楼没问题，而且我暂时把通往另一栋楼的那道门堵上了。我想那栋楼大概也可以进去，不过也许等到我们动身出发之前再说吧。等我给你找到外套和帽子之后，我们要从那儿路过才能到学生中心。"
    scene c008_s004_013 with Dissolve(0.25)
    k "我没打算走到那么远。主要是我想带上雪莉一起，把她带出宿舍楼。带她去她的画室。那对她来说是个熟悉、能让人安心的地方。所以我不想冒险让雪莉看到梅茜，或者看到别的什么。"
    j "这主意不错。我明天会出去，劳拉替我看门，所以如果你想带她出去散散心、顺便转移一下注意力，那就去做吧。再说了，就像你说的，她确实得离开这儿。整天躲起来对她形象不好。"
    if k_friend >= 12 or k_sex >= 1:
        scene c008_s004_016 with Dissolve(1)
        "哦？她牵住了我的手。考虑到我们最近已经这么亲近，这本来不该让我意外，但它还是让我吃了一惊。雾灾之前她几乎不跟我说话，而现在我们处在这么一种奇怪的位置，我不知道「我们」会走向哪里。"
        scene c008_s004_017 with Dissolve(0.5)
        j "卡莉？你还好吗？有没有——"
        k "没事。就是……"
        "我觉得她想说点什么，但她要么找不到词，要么还在犹豫那些感觉是不是真的存在。我不该让这件事对她变得更难。也许就这样接受它本来的样子就好了。"
        scene c008_s004_018 with Dissolve(0.25)
        j "没关系。你不用说什么。如果你只是需要一双温暖的手握着撑一下，我不在意。"
        k "谢谢。"
        scene c008_s004_019 with Dissolve(1)
        "我们在黑暗与安静中坐了很久。我想问她很多问题，其中几个都围绕着她这一刻在想什么。但我没有追问。我敢肯定，光是最近意识到安德鲁一直在对她做什么，她就已经有太多要消化的了。"
        "如果她现在需要的只是有个人陪在身边，不要求她做任何事、说任何话，那我做得到。"
        scene c008_s004_020 with Dissolve(1)
        "过了一会儿，她松开了我的手。她脸红得厉害，勉强才能对视的目光，始终没有说话。我很想知道她在想什么，但我忍住了。我告诉自己，如果她想说，她会开口的。她已经证明过她能做到，只是通常需要时间把所有事情想透。"
        scene c008_s004_014 with Dissolve(0.5)
        j "好了，我该让你回去看书了。本想嘱咐你别熬太晚，但你自己也是大人了。"
        k "晚安。"
        j "你也是。"
        scene c008_s004_015 with Dissolve(0.5)
        "我说不上来我们之间到底在发生什么。这里面确实有点什么，但卡莉从来不会直说自己心里想什么。而且这事可能永远都不会有什么结果，尤其是如果我们能出去的话，而且说不定很快就能出去。"
    else:
        scene c008_s004_014 with Dissolve(0.25)
        j "好了，我该让你回去看书了。本想嘱咐你别熬太晚，但你自己也是大人了。"
        k "晚安。"
        j "你也是。"
        scene c008_s004_015 with Dissolve(0.5)
        "知道可以指望卡莉，这感觉真好。虽然劳拉在康复，但我总得盯着她，而雪莉崩溃成这样也是情理之中。所以卡莉在这儿，稳稳地是件好事。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_6_832", transition=Dissolve(1.0))()
    pause
    $ Hide("july_6_832", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c008_s005_001 with Dissolve(2)
    play music insideday3 fadein 2.0
    "某个时候——对着天花板盯了大约一小时之后——我终于迷迷糊糊睡着了。出乎意料地，我后来醒得比计划的晚。我们谁都没设闹钟，但当我发现宿舍里安静得出奇、而且只有我一个人醒着的时候，还是吃了一惊。"
    "虽然四个人怎么也比不上一整栋楼的大学生那么吵，但在这种死寂的包围之下，相邻房间里的动静和说话声，对留心的人来说还是很显眼的。"
    scene c008_s005_002 with Dissolve(0.5)
    "我没急着叫醒别人，心想不如慢慢开启这一天。喝杯咖啡什么的。直到我的膀胱发现我已经醒了，冲我发来消息，表示该去趟洗手间了。"
    scene c008_s005_003 with Dissolve(0.25)
    j "啊————"
    "顺便把早上的屁也一起放了。身边一直围着三个女人，我根本没机会按需要的频率排气。不过这也要求我胃里得有点存货，而我最近吃的实在太少了。"
    s "{size=32}唔呃~~~~ *抽泣*{/size}"
    scene c008_s005_004 with Dissolve(0.25)
    "靠，我不是一个人。雪莉？她什么时候进来的？还是我走进来的时候她就已经在了？"
    scene c008_s005_005 with Dissolve(1)
    "她在哪儿？在一楼？我没听见水声，所以……"
    scene c008_s005_006 with Dissolve(0.25)
    "在那儿呢。"
    j "雪莉？嘿，是我。"
    s "*抽噎* 哦，[player_name]，我……*抽噎*"
    scene c008_s005_007 with Dissolve(0.25)
    s "我只是……*抽噎* 醒得太早，然后……*抽噎*……我只是……"
    j "我知道，雪莉。我知道。这两天真是糟透了。不过我倒是好奇，你怎么跑到这儿来了。"
    scene c008_s005_008 with Dissolve(0.25)
    s "*抽噎* 我起来上洗手间，然后好像就晃悠到这儿来了。我现在有点明白劳拉刚才在那边突然断片是什么感觉了。*抽噎* 我都不知道自己为什么进这儿。也许只是想找个黑漆漆的洞躲起来哭一场。或者洗个澡。"
    j "是啊，悲伤能把人折腾得够呛。让你说出、做出一些平时不会说的话和事。打破你平常的反应模式。我本想问你还好吗，但我也知道那是句蠢话。你需要什么吗，还是——"
    scene c008_s005_009 with Dissolve(0.25)
    s "就在这儿陪我待一会儿。好吗？我现在不想一个人。我……我受够了一个人。"
    j "这我能做到。"
    scene c008_s005_010 with Dissolve(0.5)
    j "那么，我不想踩太敏感的话题……你可以说你不想聊这个，但你和梅茜熟吗？这是你第一次失去这样一个你足够了解的人吗？"
    scene c008_s005_011 with Dissolve(0.25)
    s "嗯，我们……说句私心的话，我们算是朋{i}友{/i}。不是什么闺密之类的。就是我认识的人。不过我们曾经胡搞过一两次。不是那种交往关系。也不是什么我们打算认真对待的事。"
    j "所以，她算是你的情人？那只是大学女生在摸索，还是说你俩属于「不认真但可能会认真起来」那种？"
    scene c008_s005_012 with Dissolve(0.5)
    s "嗯。没人说过这是要认真对待的关系，我们俩也都只是四处玩。还算不上交往。我估计就是两个大学生，因为又饥渴又无聊而搞出来的事。我连她姓什么都不知道。"
    s "我们各有各的生活，除了在宿舍楼里几乎不一起玩。不过我们确实一起度过了几个晚上，所以这就意味着，世上又少了一个了解我的人。"
    scene c008_s005_013 with Dissolve(0.25)
    s "但这还是疼得要命，而且真的让这一切比我预想的要真实得多。我想我以前就是个愚蠢、天真的姑娘，自欺欺人地以为一切都还算过得去。"
    j "这种事带来的冲击，大概真像一盆冷水当头浇下——打个比方而已。我没多久之前也经历过一次。"
    scene c008_s005_014 with Dissolve(0.25)
    s "不过，为这个哭得稀里哗啦，我还是觉得自己很蠢。她甚至都不是我的家人。这又不算什么真爱，也谈不上我失去了女朋友。主要就是，一个同样喜欢女孩子的潜在好友。而且这也不是什么只有我们才有的事。所以我这就是「大学女生金曲集」呗？"
    j "别因为这个太苛责自己。我们每个人脱离父母的掌控之后，都试过一些新东西。你们俩都不是第一个在大学里探索这些的人。这不过是很多人用来试探自己边界的方式罢了。"
    scene c008_s005_015 with Dissolve(0.25)
    s "大概吧。你不介意，对吧？"
    menu:
        "我敢肯定那肯定很火辣。{image=gui/emoji_female.webp}{image=gui/emoji_female.webp}":
            $ bicontent = "yes"
            j "有你在场的话，我敢肯定很火辣。*轻笑*"
            scene c008_s005_016 with Dissolve(0.25)
            s "谢谢。而且可能还真是。*窃笑*"
        "又不是我的恋爱关系，轮不到我做主。":
            j "说实话，也不是我的恋爱关系，轮不到我做主。我没干过那种事，不过我也觉得男人大多就是一堆功能健全的肉块，纳闷女人怎么会觉得我们有吸引力。"
            s "哦？好吧。"
    "我想问她，既然她们亲近到能发生那种关系，为什么梅茜她们走的时候她没有跟着走。但我怕我们得把她的思绪从那些话题上引开，免得她一头扎进情绪的漩涡里。"
    scene c008_s005_017 with Dissolve(0.5)
    s "[player_name]……我不想再待下去了。我……我躲在这儿是因为我觉得跟其他人一起走不安全，可是……可是这里……我再也待不下去了。"
    j "没关系，我能理解。反正我们也没打算把你一个人留下。"
    "我讨厌她要经历这些才肯开口，不过这次结果对我们有利。"
    scene c008_s005_018 with Dissolve(0.25)
    s "这一切开始之后，我就一直没出去过。外面……很糟吗？那些灼烧者和雾？"
    j "我们会尽量压缩待在外面的时间。不过我们得给你配齐装备。你有那件外套，我这边有一些手套和口罩。我们得给你弄顶帽子和一副墨镜。遮得越多越好。"
    scene c008_s005_019 with Dissolve(0.25)
    s "我有一副。墨镜。"
    j "好。好。"
    scene c008_s005_020 with Dissolve(0.5)
    s "我确实得……我该告诉你一件事。一件我不想让任何人知道的事。我并不以此为荣，但它已经开始变成一个麻烦了。"
    scene c008_s005_021 with Dissolve(0.25)
    s "我在吃几种情绪稳定剂。我……他们说我是躁郁症——或者类似什么鬼东西——所以我得吃些处方药才能把情绪调平。我已经停药一周了。本来该去补药的，但雾灾来了之后我就开始省着吃，现在已经彻底断供了。"
    j "这件事我们得做点什么吗？最近的药店有多远？"
    scene c008_s005_022 with Dissolve(0.25)
    s "没有车，我们没法从这儿过去。而且虽然不致命，但是……"
    menu:
        "你只能自己学着应付。":
            j "那你就得自己学着应付，而且一旦有什么不对劲，得告诉我们。我们可以支持你，但你必须对我们坦诚。"
            scene c008_s005_023 with Dissolve(0.25)
            s "如果我能的话。有时候事情发生的时候，我自己都没意识到。"
        "我们得替你盯着。\n[rgr](雪莉 好感\信任 +1)":
            $ s_friend += 1
            $ s_trust += 1
            j "我们只能盯着——你和我——尽量在它发作的时候照应你。"
            scene c008_s005_023 with Dissolve(0.25)
            s "如果能做到的话。有时候事情发生的时候，我自己都没意识到。"
    j "你想让其他人知道吗？"
    scene c008_s005_024 with Dissolve(0.25)
    s "如果可以的话，暂时别。"
    "这也不是我藏的第一个秘密了。"
    j "好，没问题。但如果出了什么事，而我需要她们明白原因，我可能还是得告诉她们。"
    scene c008_s005_021 with Dissolve(0.25)
    s "我……我知道。我会尽力把自己撑住的。如果我撑得住的话。"
    j "别一个人扛，好吗？我们也在这儿。"
    if s_trust >= 2 or s_love >= 1 or s_friend >= 5:
        scene c008_s005_072 with Dissolve(0.5)
        s "……"
        play voice_loop kiss
        scene c008_s005_073 with flashpink
        s "呼噜~~~ 唔唔唔~~~"
        "现在情绪正激动。我早该料到的，尤其是雪莉这种爱调情的姑娘。"
        stop voice_loop
        scene c008_s005_074 with Dissolve(0.5)
        s "谢谢。我……"
        menu:
            "我们该起来了，走了。":
                j "我们该起来了，走了。或者，至少我该起来了。我还有一堆事要做。你需要……"
                scene c008_s005_075 with Dissolve(0.5)
                s "我没事。我……我该洗个澡。洗一洗也许会好受点。要一起吗？"
                j "*轻笑* 心意我领了，不过我要出门，回来以后正想冲个澡。"
                scene c008_s005_076 with Dissolve(0.25)
                s "哦，好吧，试试总没坏处。谢谢你……就这么陪着我。"
                scene c008_s005_077 with Dissolve(0.25)
                j "当然。你要知道，需要的话，我们所有人都会帮你。所以别一个人扛。"
                s "我……我不会的。我觉得现在一个人待着不是什么好主意。"
                scene c008_s005_078 with Dissolve(0.25)
                j "行。我记得卡莉今天想跟你待着，等她起来了就去找她聊聊。"
                s "好。"
                scene c008_s005_079 with Dissolve(0.25)
                j "好吧，那我至少先给你留点隐私。"
                jump ch8_mainmorning
            "想不想打打闹闹？\n[rgr](雪莉 爱意\欲望 +1)\n[pks]":
                $ s_sex += 1
                $ s_love += 1
                $ s_desire += 1
                $ ch8_shelley_sex = "yes"
                call ch8_shelley_sex from _call_ch8_shelley_sex
                jump ch8_mainmorning
    else:
        scene c008_s005_075 with Dissolve(0.5)
        j "我们该起来了，走了。或者，至少我该起来了。我还有一堆事要做。你需要……"
        s "我没事。我……我该洗个澡。洗一洗也许会好受点。要一起吗？"
        scene c008_s005_076 with Dissolve(0.25)
        j "*轻笑* 心意我领了，不过我要出门，回来以后正想冲个澡。"
        s "哦，好吧，试试总没坏处。谢谢你……就这么陪着我。"
        scene c008_s005_077 with Dissolve(0.25)
        j "当然。你要知道，需要的话，我们所有人都会帮你。所以别一个人扛。"
        s "我……我不会的。我觉得现在一个人待着不是什么好主意。"
        scene c008_s005_078 with Dissolve(0.25)
        j "行。我记得卡莉今天想跟你待着，等她起来了就去找她聊聊。"
        s "好。"
        scene c008_s005_079 with Dissolve(0.25)
        j "好吧，那我至少先给你留点隐私。"
        jump ch8_mainmorning
label ch8_mainmorning:
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c008_s006_001 with Dissolve(2)
    play music insideday2 fadein 2.0
    "好吧，刚才那番小谈之后，我对雪莉的状况多少安心了一些。我想她脆弱还会持续一阵子，不过也许她一直都是这样，只不过没了药，这一点就更明显了。"
    scene c008_s006_002 with Dissolve(0.5)
    if ch8_shelley_sex == "yes":
        "这个情报暂时得由我一个人揣着，除非她自己想说出来。还有就是——我们一直为了找乐子在交换体液这件事。"
        "我敢肯定，她让我每晚上门只是个一时冲动的提议。我不能让自己误以为{i}这件事{/i}超出了等价交换的范畴。"
    else:
        "这个事实暂时得由我一个人揣着，除非她自己想说出来。"
    scene c008_s006_003 with Dissolve(0.5)
    l "早。要来点咖啡吗？"
    j "早。我太想要一杯了，谢谢。你睡得还好吗？"
    scene c008_s006_004 with Dissolve(0.5)
    l "最近我干这种事干得太多了，不过还好。知道你接下来要问什么，我就省得你开口了……我确实好多了，但像昨天那样的日子——跟那个女孩有关——让一切都很难熬。"
    l "而且感觉每天我们都在等下一次打击到来。我们接下来会怎么样？轮到谁受伤？或者更糟。"
    menu:
        "轮到我了。\n[rrd](劳拉 好感 -1)":
            $ l_friend -= 1
            j "我觉得今天轮到我了。"
            scene c008_s006_006 with Dissolve(0.25)
            l "这一点都不好笑。"
        "只要我们待在一起，就不好笑了。":
            j "只要我们待在一起，就不好笑了。我知道你现在可能没这个感觉，但要想活下去，我们真的必须互相照应。"
            scene c008_s006_006 with Dissolve(0.25)
            l "你说是就是吧。"
    scene c008_s006_005 with Dissolve(0.25)
    l "给你。我们没有牛奶也没有咖啡伴侣，将就喝黑咖啡吧。"
    j "像我的灵魂一样纯黑。谢谢。"
    scene c008_s006_007 with Dissolve(0.25)
    l "你闻起来该洗个澡了。"
    j "雪莉现在正在里面。我要是出门，就等回来再说吧。"
    scene c008_s006_008 with Dissolve(0.25)
    l "我想实际一点考虑更靠谱。你什么时候决定走？能给我个十五到二十分钟吗？"
    j "嗯，嗯。我想先好好享用这杯咖啡，然后再正经换好衣服。不急。"
    l "你打算去哪儿？"
    j "院子对面那些宿舍楼。我们只需要再弄几样东西，就能让所有人都装备齐全。还要再弄点吃的。"
    scene c008_s006_009 with Dissolve(0.25)
    l "所有人？你说动雪莉一起去了？还是我们仍然在执行「想办法把她拉上」的计划？"
    j "除非她改变主意，雪莉今天早上已经说得很清楚，她不想再待下去了。梅茜的死大概就是那个把她叫醒的警钟。"
    scene c008_s006_010 with Dissolve(0.25)
    l "很好。我说的「好」不是那个意思，而是庆幸她改了主意。这样我们能少操一份心。"
    j "我同意。谢谢你的咖啡。我去换装备了。你准备好了就来找我。"
    l "好。我……好啊。"
    if ch8_shelley_sex == "yes":
        scene blank with Dissolve(2)
        scene c008_s005_087 with Dissolve(2)
        play ambient shower
        "{color=#8bc7ff}我的天哪，我他妈太需要这个了。已经很久没有出现过一个我愿意让他进我房间的男人了，更别提让他进我裤子里。而且我的老天，那男人的鸡巴真他妈值得骑。{/color}"
        scene c008_s005_088 with Dissolve(0.25)
        "{color=#8bc7ff}趁他还在身边，我得好好利用一番。我并不想要什么认真或者长期的关系，不过如果[player_name]不介意偶尔来一发「随传随到」，我就能拿他当个提升血清素的补剂。{/color}"
        scene c008_s005_089 with Dissolve(0.25)
        "{color=#8bc7ff}不过要是还有下次，我可能得考虑避孕的事了。{/color}"
        scene c008_s005_090 with Dissolve(0.5)
        "{color=#8bc7ff}因为[player_name]留在里面那玩意儿可不少。他要是射精的时候不像是使足了劲要把人搞怀孕，我都不信。{/color}"
        scene c008_s005_091 with Dissolve(0.5)
        "{color=#8bc7ff}而且我也不知道怀孕的激素会不会让我更疯。我得把这件事捂得严严实实，因为我可输不起，一崩就彻底完了。{/color}"
        scene c008_s005_092 with Dissolve(0.25)
        "{color=#8bc7ff}一旦离开这儿，我真的得努力不让自己成为累赘。至少别比平时更糟。{/color}"
        stop ambient
    scene blank with Dissolve(2)
    scene c008_s006_011 with Dissolve(2)
    if ch8_shelley_sex == "yes":
        "考虑到刚才在浴室里跟雪莉发生的那些事，我在这儿可能得小心点。我知道我很容易被人劝说着去做一些事后并不明智的事。把东西塞给她挺开心的，她自己也不当回事，但最终这可能会变成一件大事。"
    elif ch8_shelley_sex == "no" and s_sex == 1:
        "好吧，考虑到我和雪莉之间这股性张力，我在这儿可能得小心点。我知道我很容易被人劝说着去做一些事后并不明智的事。前天晚上那次挺开心的，她自己也不当回事，但最终这可能会变成一件大事。"
    else:
        "好吧，考虑到我和雪莉之间这股性张力，我在这儿可能得小心点。我知道我很容易被人劝说着去做一些事后并不明智的事——而且我可不想让她以为我们是在谈恋爱。"
    scene c008_s006_012 with Dissolve(1)
    if l_sex >= 2:
        "劳拉和我不再胡搞，坦白说是件好事。事实上，我知道她之前崩溃的时候我没帮上忙。事到如今，我们只能做朋友，仅此而已。我绝对不想把她已经一塌糊涂的处境搅得更乱。"
        if s_sex >= 1:
            "如果她发现雪莉和我在上床？大概不会有什么好结果。那肯定会让我们之间这点短暂的游戏戛然而止。"
    else:
        "劳拉和我当初没有放纵那股性张力，坦白说是件好事。我觉得那对她之前的崩溃没有任何帮助。她需要我是个朋友，任何相反的冲动都必须压下去。我绝对不想把她已经一塌糊涂的处境搅得更乱。"
    if k_sex >= 1:
        scene c008_s006_013 with Dissolve(1)
        "还有卡莉……我真的应该对她谨慎一点。我一跟她单独待在一起，就会发现自己被她吸引，可考虑到她被安德鲁折腾成那样，我还是会怀疑自己是不是在占她的便宜，哪怕我并没有这个意思。这件事我真的该处理得小心些。"
        if l_sex >= 2:
            "如果劳拉发现我们在一起上床，我敢肯定她会闹翻天。哪怕劳拉知道安德鲁虐待她到什么程度。见鬼，那大概都不够，尤其是我和她前不久也干过同样的事。"
        else:
            "如果劳拉发现我们在一起上床，我敢肯定她会闹翻天。哪怕劳拉知道安德鲁虐待她到什么程度。见鬼，那大概都不够。"
    if k_sex >= 1 and s_sex >= 1 and l_sex >= 1:
        scene c008_s006_014 with Dissolve(1)
        "那要是她们三个开始对起话来呢？嗯，那肯定会掀起一场风波。雪莉算是知道点什么，她说自己不介意，但另外两个不会。"
        "可要是对自己诚实一点，我是在想跟她们中的某一个确立关系吗？还是说，这只是为了让自己好受一点、而和我们所有人共同身处的这糟糕局面有关的纯粹肉体交易？"
        scene c008_s006_015 with Dissolve(0.25)
    else:
        scene c008_s006_015 with Dissolve(1)
    l "嘿，你准备好了吗？"
    j "呃，好了，正收尾。其他人知道了吗？"
    scene c008_s006_016 with Dissolve(0.25)
    l "我刚跟卡莉说了。她提了一嘴要带雪莉去哈灵顿楼。就是想让她出去待一小会儿。"
    j "她说到时候带雪莉去画室。那里对她来说是个熟悉、能让人安心的地方。再说，我觉得让她提前适应一下「外面是什么样子」也有好处。她可以在窗户后面安全地看到外面的景象。"
    scene c008_s006_017 with Dissolve(0.25)
    l "好吧。我想这说得通。雪莉闷在屋里太久了。"
    j "卡莉办事我还是放心的。"
    l "我尽量。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c008_s007_001 with Dissolve(2)
    play music outsideday fadein 2.0
    "好吧，动作要快，但也要小心，这看起来像是自相矛盾。不过既然我要去院子对面那些宿舍楼，我不想在这儿多待哪怕一秒。"
    "我知道自己走得了这段路。这不是问题。尽管在这儿待着确实会慢慢磨损人。我去救劳拉的时候已经领教过这一点了。她那次没动脑子就跑出去，到现在身子还虚着。"
    scene c008_s007_002 with Dissolve(0.5)
    "我让她守门，这决定明智吗？是不是该让卡莉去守？反正不是雪莉——我还不信任她。归根结底这事就一个字：信任。我得相信那通警钟足以让劳拉安分守己。"
    "不过这不是我现在该想的事。别陷进胡思乱想里。专注点，伙计。我知道事情很多，但在外面分心可没什么好处。"
    scene c008_s007_003 with Dissolve(0.5)
    "说到外面：这空气有点怪。大气。我要找的词是这个。闷闷的。我知道雾灾以来天气就一直不正常。这还是那回事吗？希望不是什么坏东西。我可不想让这局面再往坏里走。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c008_s007_009 with Dissolve(2)
    play music school fadein 2.0
    k "是这个方向。哦，等等，我干嘛要告诉你这个？*窃笑*"
    scene c008_s007_010 with Dissolve(0.5)
    s "不不不。没事没事。我一直都不太擅长记路。我就是跟着别人走，然后一路晃悠，直到晃到该去的地方。不过从宿舍楼走到画室这条路，我倒是能靠肌肉记忆走个大概。"
    scene c008_s007_011 with Dissolve(0.5)
    s "我确实得问一句：我们待在这儿安全吗？这……外面雾那么重，而我们之间只隔着一层窗户。"
    k "[player_name]已经把整栋楼都走遍了，确认没有破损之类的问题。里面没有任何会威胁到我们的东西。而且他说他还把通往隔壁那栋楼的门封住了，以防万一。"
    scene c008_s007_012 with Dissolve(0.25)
    s "卡森楼？"
    k "如果那栋楼叫这个名字的话，对。"
    scene c008_s007_013 with Dissolve(0.25)
    s "那里面就是……"
    k "是，不过我们不该过去。如果你指的是那儿的话。"
    scene c008_s007_014 with Dissolve(0.25)
    s "不不不。我……我不想看。我不想看到她那个样子。这个我还分得清。"
    k "我们该走了。"
    scene c008_s007_015 with Dissolve(0.25)
    s "呃……对，对。走楼梯上去。"
    scene blank with Dissolve(2)
    scene c008_s007_004 with Dissolve(2)
    "好吧，这地方跟其他几栋一模一样。这么说来还真有效率。这些楼大概都是同一时期建的。"
    "和另外那栋宿舍楼不同，这里没有雾，算是加分项。但同样地，也听不到任何动静。我的第一反应是喊一声，但求生的本能告诉我别喊。"
    scene c008_s007_005 with Dissolve(0.5)
    "好，我到底是来干什么的？心里默念一下清单。帽子、一件外套，还有——如果需要的话——另一副墨镜。我忘了问雪莉有没有。刚才有点分心。也许我可以翻翻柜子和冰箱，看看有没有能顺走的吃的。"
    scene blank with Dissolve(2)
    scene c008_s007_016 with Dissolve(2)
    s "到了。天哪，那股颜料和溶剂的味道，正好挠得我那点舒适区痒痒的。"
    k "好。你这儿有你的画吗？我想看看。"
    scene c008_s007_017 with Dissolve(0.25)
    s "呃……应该没有。除非我落下了什么。学期结束之后，我妈让我把东西寄回家了。我想，我暑假又没排画室课，所以当时觉得留着也没什么大不了的。"
    k "你这儿有画画或者素描用的材料吗？"
    scene c008_s007_018 with Dissolve(0.25)
    s "呃，储藏室或者柜子里可能有一些。我平时有个化妆箱，笔和颜料都放在里面。我爸老开玩笑说，那就像一个粉色的假鱼饵盒——既装不了钓具，也装不了化妆品。"
    scene c008_s007_019 with Dissolve(0.25)
    s "我……我想我爸。我……"
    k "等你出去之后，还能再见到他。"
    scene c008_s007_020 with Dissolve(0.25)
    s "我知道。我……当事情开始变得压得我喘不过气的时候，我需要靠想这个来撑住。有你们在身边真好。要不然，我可能会让那些坏念头钻进来太久。"
    k "我们都在努力做彼此的情感支撑。这比我以往任何时候预期的都要多，也比我以为我需要的要多。"
    scene c008_s007_021 with Dissolve(0.25)
    s "是啊。我看得出来每个人都在努力撑过这一天。就像劳拉。她那样崩溃，我挺难受的。我无法想象为人父母之后会那样担心孩子，或者担心丈夫。我对爸妈也有点担心，不过我想他们在泽西那边应该没事。"
    scene c008_s007_022 with Dissolve(0.5)
    s "那你呢？"
    k "也差不多。我家在纽约州北部，所以我想他们离得够远，应该没事。等我们出去以后，我要北上去看他们。也许在他们那儿住一阵子。"
    scene c008_s007_023 with Dissolve(0.25)
    s "哦？那……"
    k "嗯……"
    scene c008_s007_024 with Dissolve(0.25)
    s "怎么了？"
    k "就是往下看看能看到什么。"
    scene c008_s007_025 with Dissolve(0.5)
    s "你看得出来？看着就一片白茫茫的。哦，等等，大概是盯着看久了，就能分辨出东西来了。我们在找什么？"
    k "我只是想问问，会不会在下面看到[player_name]。或者别的灼烧者。"
    scene c008_s007_026 with Dissolve(0.25)
    s "你担心他？他可是个大男孩。我觉得他能照顾好自己。"
    k "就算他真有麻烦，我们好像也做不了什么。"
    scene c008_s007_027 with Dissolve(0.25)
    s "不过要是下面有灼烧者，我们至少能提醒他。挥挥手，指给他看。"
    k "前提是他能从这儿看见我们。"
    scene c008_s007_028 with Dissolve(0.25)
    s "他能看见。这不难。我以前还从这扇窗户跟人喊过话呢。鲁迪——他是我画室课的同学——有一天晚上我跟他狠狠吵了一架。他在楼下，我在这儿。"
    k "吵什么？"
    s "操，我真不记得了。我不喜欢他，大概就只是这个原因吧。我承认，那次我状态很糟。其实我也说不清自己为什么讨厌他。可能因为我是个阴晴不定的臭婊子吧。"
    if k_friend >= 12 or k_sex >= 1:
        scene c008_s007_029 with Dissolve(0.25)
        k "哦，下面有东西在动。我觉得是[player_name]。"
        s "嗯？还真是。一开始没看出来。他背着那个包，看起来又臃肿又笨拙。我现在明白自己为什么会把他当成灼烧者了。"
    else:
        scene c008_s007_030 with Dissolve(0.25)
        s "靠，下面有东西在动。我觉得是[player_name]。一开始没看出来。他背着那个包，看起来又臃肿又笨拙。我现在明白自己为什么会把他当成灼烧者了。"
    scene c008_s007_031 with Dissolve(0.5)
    k "那边有……我觉得他是一个人。或者附近没有别的东西。"
    s "好。我们应该设法引起他的注意，让他知道有人在这儿给他打气。也免得他做出什么不雅的举动，比如抠鼻子或者抠屁股。*窃笑*"
    scene c008_s007_032 with Dissolve(0.25)
    s "我们又不能开窗冲他喊。只能喊叫加拍窗户了。"
    scene c008_s007_033 with hpunch
    s "嘿！哥们！这儿！*吹口哨*"
    k "呃，能别这么大声吗。"
    scene c008_s007_034 with Dissolve(0.25)
    s "嗯？随便吧。"
    if k_friend >= 12 or k_sex >= 1:
        $ ch8_kallie_flash = "yes"
        scene c008_s007_041 with Dissolve(0.25)
        k "*窃笑* 不，我……"
        s "嗯？怎么了？有什么好笑的？"
        scene c008_s007_042 with Dissolve(0.25)
        k "劳拉以前说过，如果你真想引起一个男人的注意，就对他闪光胸。据说男人都抵挡不住胸部。"
        s "这哪儿是「据说」，明摆着。*大笑*"
        scene c008_s007_043 with Dissolve(0.25)
        s "事实上——"
        scene c008_s007_044 with Dissolve(0.25)
        s "砰！看看这样能不能引起他的注意。瞧那颤巍巍的胸，哥们。你明明就喜欢这个。"
        scene c008_s007_045 with Dissolve(0.25)
        s "来吧，卡莉，跟我一起。两对奶子总比一对强。"
        k "好、好吧。我……"
        scene c008_s007_046 with Dissolve(0.25)
        s "*大笑* 这才像话。嘿，[player_name]，往上看。来嘛，你不想错过两对超棒的胸部吧。"
        scene c008_s007_047 with Dissolve(0.25)
        s "哈！看见了吧。他往这儿看了。我想是。我就知道他忍不住。来，给他表演一个。"
        scene c008_s007_048 with Dissolve(0.5)
        k "我有种预感，这事以后肯定要被念叨。"
        s "只会有好事。他心里有数。"
        scene c008_s007_049 with Dissolve(0.25)
        s "好，他继续往前走了。我敢说刚才那一下他肯定挺开心的，不过他真不该在外面待太久。"
        if bicontent == "yes":
            scene c008_s007_055 with Dissolve(0.25)
            s "哦~~~那对是不是最可爱的？"
            k "我，呃……"
            scene c008_s007_056 with Dissolve(0.25)
            s "没关系，姑娘。这不是我第一回看胸了。住在宿舍楼里，这种东西看多了。而且这也不算多秘密。我已经告诉[player_name]了。我多少有点双性向。"
            k "哦？那倒也……"
            scene c008_s007_057 with Dissolve(0.25)
            s "大概是大学时的那种事吧，在摸索自己在性方面是什么取向。我懂的。他们说这是个阶段，但我觉得男人和女人我都觉得性感。有些男人。"
            scene c008_s007_058 with Dissolve(0.25)
            s "比如你？你可爱得要命，但我敢打赌你是只认男人的那种姑娘。你和劳拉。"
            k "我……"
            scene c008_s007_059 with Dissolve(0.25)
            k "你和梅茜……也是那种关系吗？"
            s "我们有过一些……我们没在交往，但没错。我……我们能别……"
            scene c008_s007_060 with Dissolve(0.25)
            k "好。抱歉。"
            s "没关系。"
            scene c008_s007_050 with Dissolve(0.25)
            k "嗯唔~~~"
            scene c008_s007_051 with Dissolve(0.25)
            s "所以你是{i}喜欢{/i}他的，对吧？反正我感受下来是这个意思。"
            k "呃，不是那种喜欢。我只是……我们从第一天起就一直在一起，我想我们慢慢就变得亲近了。所以我会担心。就像前天劳拉出去的时候，我担心她那样。"
            scene c008_s007_052 with Dissolve(0.25)
            s "嗯哼。好吧。你不用说。"
            scene c008_s007_053 with Dissolve(0.25)
            s "我能理解为什么每个姑娘都会这样。嗯，离婚那档子事大概让他有点郁郁寡欢，不过他很性感，放开的时候还挺有意思。而且他是那种你会觉得「如果真有事，他会为你拼一把」的男人。"
            scene c008_s007_054 with Dissolve(0.25)
            k "……"
            s "不过你已经有男人了，我也不打算因为你多看两眼就评判你。"
        else:
            scene c008_s007_050 with Dissolve(0.5)
            k "嗯唔~~~"
            scene c008_s007_051 with Dissolve(0.25)
            s "你是{i}喜欢{/i}他的，对吧？"
            k "呃，不是那种喜欢。我只是……我们从第一天起就一直在一起，我想我们慢慢就变得亲近了。所以我会担心。就像前天劳拉出去的时候，我担心她那样。"
            scene c008_s007_052 with Dissolve(0.25)
            s "嗯哼。好吧。你不用说。"
            scene c008_s007_053 with Dissolve(0.25)
            s "我能理解为什么每个姑娘都会这样。嗯，离婚那档子事大概让他有点郁郁寡欢，不过他很性感，放开的时候还挺有意思。而且他是那种你会觉得「如果真有事，他会为你拼一把」的男人。"
            scene c008_s007_054 with Dissolve(0.25)
            k "……"
            s "不过你已经有男人了，我也不打算因为你多看两眼就评判你。"
    else:
        scene c008_s007_035 with vpunch
        s "嘿！！！上面！！！"
        scene c008_s007_036 with Dissolve(0.25)
        s "靠，他没听见我们。"
        k "反正我们大概也不该分散他的注意力。外面太危险了，他可不能停下来往这儿看。"
        scene c008_s007_037 with Dissolve(0.25)
        s "嗯唔……大概吧，这一切开始之后我就没出去过了。"
        k "我们出去过，而且并不好玩。"
        scene c008_s007_038 with Dissolve(0.25)
        s "你这话可让我对我们离开这儿没什么美好期待了。"
        k "这不是我们能做选择的事。想获救，我们就非做不可。"
        scene c008_s007_039 with Dissolve(0.25)
        s "*叹气* 他妈的，可不是嘛。"
        scene c008_s007_040 with Dissolve(0.25)
        $ renpy.pause ()
    scene blank with Dissolve(2)
    scene c008_s007_006 with Dissolve(2)
    if ch8_kallie_flash == "yes":
        "好吧，这可真是我没料到的事。我就把它记成是雪莉说服卡莉干了一件疯狂的事吧。我没料到她对卡莉的影响力能到这种程度。"
        "不过我并不介意。再说，那个内向的姑娘，那个以前做什么都得看安德鲁脸色、连多活一点都不被允许的姑娘，也许正好需要活一活，哪怕是在她人生最糟糕的时刻。"
        scene c008_s007_007 with Dissolve(0.5)
        "好吧，今天总算也有了点好结果。在我出发之前，我该问问雪莉暑假期间他们是不是把几栋宿舍楼封起来了。整栋楼空荡荡的。我想也说得通，既然不指望有学生住，他们自然会把人都集中到一块儿。"
        scene c008_s007_008 with Dissolve(0.5)
        "除了柜子里留下的几箱旧麦片和饼干，什么值得拿的东西都没有。而且那些说不定都过期了，不过有旧食物总比没食物强。"
    else:
        "我想我该问问雪莉暑假期间他们是不是把几栋宿舍楼封起来了。整栋楼空荡荡的。我想也说得通，既然不指望有学生住，他们自然会把人都集中到一块儿。"
        scene c008_s007_007 with Dissolve(0.5)
        "除了柜子里留下的几箱旧麦片和饼干，什么值得拿的东西都没有。而且那些说不定都过期了，不过有旧食物总比没食物强。"
        scene c008_s007_008 with Dissolve(0.5)
        "我好像听见了什么动静，不过大概只是我脑子里的错觉。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("june_27_304", transition=Dissolve(1.0))()
    pause
    $ Hide("june_27_304", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c008_s008_000 with Dissolve(2)
    play music insideday3 fadein 2.0
    j "那栋楼是空的，只剩下一些看起来是上学期遗留的破烂。我猜在雾灾来临之前，他们还在清理——或者本来就在计划清理——这地方。我在那个小厨房里找到几箱剩下的麦片和饼干，所以也不算白跑一趟。"
    l "外面怎么样？没遇到什么麻烦吧？"
    scene c008_s008_001 with Dissolve(0.25)
    j "没有。灼烧者是在外面，不过因为我是一个人，动作能很快。我到现在还是搞不懂他们是怎么追踪我们的，但以他们那种慢吞吞的速度，只要我们不是正好撞上他们，就构不成威胁。只要留心周围就行。"
    if ch8_kallie_flash == "yes":
        scene c008_s008_004 with Dissolve(0.5)
        s "嘿嘿~~~我们回来啦！"
        j "不过我顶着两对胸贴着二楼的窗户喊话，回来可没那么容易。*轻笑* 不过我可没抱怨。谢谢你们的表演。"
        l "什么？"
        scene c008_s008_005 with Dissolve(0.25)
        s "*窃笑* 有人说，这样能引起你的注意。"
        k "劳拉跟我说——"
        scene c008_s008_006 with Dissolve(0.25)
        l "*大笑* 哦，天哪，{i}那个{/i}？你当真了？我当时是想开个玩笑缓和一下气氛。"
        s "什么？这主意棒极了，我很享受。"
        j "我也一样。"
        scene c008_s008_004 with Dissolve(0.25)
        j "说起来，我好像还没弄清楚你手头有哪些能穿的衣服，等我们需要出门的时候用。我们得穿过院子才能到学生中心，而且谁也不知道对面还有什么。我知道你还有前几天晚上穿的那件外套。"
    else:
        scene c008_s008_002 with Dissolve(0.5)
        s "我们回来啦！看见你们往前走了，想着我们也该跟上。"
        j "在熟悉的环境里待着，感觉怎么样？"
        scene c008_s008_003 with Dissolve(0.25)
        s "挺好的。我觉得出去一趟对我有点帮助。而且那股颜料的味道，出奇地让人安心。"
        j "听你这么说真好。"
        scene c008_s008_004 with Dissolve(0.25)
        j "趁现在大家都在，我想起我还没弄清楚你手头有哪些能穿的衣服，等我们需要出门的时候用。我们得穿过院子才能到学生中心，而且谁也不知道对面还有什么。我知道你还有前几天晚上穿的那件外套。"
    scene c008_s008_007 with Dissolve(0.25)
    s "哦？那件？那玩意儿够在外面穿吗？有点薄。"
    l "它能挡一层。你要的就是别让雾碰到皮肤。一旦走进去，你会发现雾比想象中密得多。这布料真的很薄吗？还是说里面至少衬了别的什么？"
    scene c008_s008_008 with Dissolve(0.25)
    s "我……我不知道。就一件拉链外套。"
    j "我们可以看看。既然说到这儿：你有裤子吗？牛仔裤？通常遮得越多越好。我还差好几样东西，只想知道要不要把裤子也加进清单。我突然想到，现在是夏天，你手边可能只有短裤或者裙子。"
    j "我弄到了几个呼吸面罩和医用手套，这方面没问题。帽子和一件外套排在清单最前面。"
    scene c008_s008_009 with Dissolve(0.25)
    s "我可以去看看。你要是愿意，我给你配一身，你再告诉我行不行。"
    j "不用搞成时装秀，不过这大概也是一次有用的练习。卡莉，我还在找一件外套或者夹克之类的。还有帽子。也许去看看雪莉有没有你能用的别的东西。"
    k "好。我跟她去。"
    scene c008_s008_010 with Dissolve(0.5)
    l "那么，既然她已经加入了……"
    j "嗯，我一直在盯着这事，不过既然我们已经说服雪莉非去不可，我就可以更直接地催她准备装备了。我讨厌事情变成这样，但如果梅茜的死能让雪莉动起来，那我认。"
    scene c008_s008_011 with Dissolve(0.25)
    j "路上我们还是得对她小心，尤其是真正出发之后。别带她经过那间教室。她现在还很脆弱，我不想再刺激到她。"
    l "我们大家都挺脆弱的。"
    menu:
        "是啊，我们都是。":
            j "是啊，我们都是。"
        "说到这个……\n[rgr](劳拉 好感 +1)":
            $ l_friend += 1
            j "说到这个，你现在怎么样？"
            scene c008_s008_012 with Dissolve(0.25)
            l "我……我没打算在你出去的时候又自己跑掉。"
            j "我问的不是这个。"
            scene c008_s008_013 with Dissolve(0.25)
            l "我……我只是为自己那样失控感到羞耻。"
            j "没关系，我们都能理解。我觉得我们每个人都在做些平时不会做的选择。"
            scene c008_s008_014 with Dissolve(0.25)
            l "确实。"
    scene c008_s008_015 with hpunch
    j "*咳嗽* *咳嗽*"
    l "你没事吧？听起来有点难受。"
    scene c008_s008_016 with Dissolve(0.25)
    j "只是有点透支了。"
    l "在外面待太久了？你脸色发白。最近在掉体重吗？"
    scene c008_s008_017 with Dissolve(0.25)
    j "我在流行那种新式减肥法。找到什么能吃的就大量吃，然后大量走路。*轻笑*"
    l "[player_name]……"
    scene c008_s008_018 with Dissolve(0.25)
    j "让我冲个澡就没事了。"
    s "{size=30}[player_name]？劳拉？你们能进来一下吗？{/size}"
    scene c008_s008_019 with Dissolve(0.25)
    j "这话听起来要么是好事，要么是坏事。"
    l "去吧。我想她房间里会有点挤。而且我未必扛得住大学生玩「换装游戏」。我把这些东西先收起来。"
    j "好。谢谢。"
    scene blank with Dissolve(2)
    scene c008_s008_020 with Dissolve(2)
    s "所以，这就是我手头的东西。卡莉给我指点了一下，说什么最合适。"
    j "不错。你差不多能出门了。"
    scene c008_s008_021 with Dissolve(0.25)
    s "你也看到了，我确实有一副墨镜，但没有帽子。我不喜欢弄出「帽子头」。"
    j "实用比什么都重要。你就一件外套？"
    scene c008_s008_022 with Dissolve(0.25)
    s "现在确实是{i}夏天{/i}。我又不是料得到会有毒雾像恐怖片一样滚滚而来。"
    j "没关系。这只意味着我得再弄两顶帽子和一件外套。在我不得不开始就地取材之前，还有一两个地方可以再找找。"
    scene c008_s008_023 with Dissolve(0.25)
    s "这够厚吗？"
    j "什么料子？棉的？"
    scene c008_s008_024 with Dissolve(0.25)
    s "应该是吧。不过里面是{b}毡{/b}的。你要是喜欢可以摸摸看。*窃笑*"
    j "好吧好吧。我敢肯定够用了。"
    if ch8_kallie_flash == "yes":
        scene c008_s008_025 with Dissolve(0.5)
        s "刚才那场小表演好看吗？*窃笑*"
        j "好看。不过我震惊的是，这主意居然是卡莉想出来的，不是你。"
        scene c008_s008_026 with Dissolve(0.25)
        k "我……我只是重复了劳拉之前说的话。最先撩衣服的是雪莉。"
        if bicontent == "yes":
            s "我几乎没怎么劝她，她就加入了。我跟你说，那对胸可挺可爱的。"
            scene c008_s008_027 with Dissolve(0.25)
            k "……"
            j "你们两个在这项上谁都不含糊。"
        else:
            s "我几乎没怎么劝她，她就加入了。"
        scene c008_s008_028 with Dissolve(0.25)
        s "不过……你刚才那个语气，听着像我爸对我失望时的语气。"
        menu:
            "不，不。没事的。\n[rgr](Kallei\雪莉 好感 +1)":
                $ ch8_kallie_flash2 = "yes"
                $ s_friend += 1
                $ k_friend += 1
                j "不，不。没事的。看胸这种事我永远不会拒绝。尤其是一对这么棒的。再说了，你们所在的地方，我们确认过是安全的。"
                scene c008_s008_030 with Dissolve(0.25)
                s "好。要是你表现得好，说不定还能再看一次。*窃笑*"
                "我明明很想提醒她们注意周围环境，但又舍不得掐掉这点不负责任的乐趣。我开始觉得我可能正在把每一件可能发生的事都往最坏处想。"
                j "既然有这好事，我一定好好表现。*轻笑*"
                scene c008_s008_031 with Dissolve(0.25)
                s "我敢打赌你会的。"
            "别误会……":
                j "别误会：我可喜欢两对胸部从二楼窗户俯视我了，而且你们两个当时心情好到愿意这么做，我挺高兴的，但是……"
                scene c008_s008_026 with Dissolve(0.25)
                k "我们需要更留意周围环境？我还以为哈灵顿楼已经确认清空、安全了？"
                scene c008_s008_029 with Dissolve(0.25)
                j "*叹气* 是啊，我可能想得太多了。我不想因为你有几分钟没被这一切的危险性压着，就惩罚你。或者，我们身上发生的烂事实在太多了，以至于我对这些事警惕过头了。"
                s "明白了。"
                "我很不想掐掉她们这点不负责任的乐趣，可万一她们干那事的时候出了岔子呢？不过，也许我确实正在把每一件可能发生的事都往最坏处想。"
    scene c008_s008_032 with Dissolve(0.5)
    j "好吧，这至少让我知道还剩多少事没做。*咳嗽*"
    k "……"
    scene c008_s008_033 with Dissolve(0.25)
    s "你要是想看更多姑娘换衣服，就留下吧。*窃笑*"
    j "不用了，没事的。虽然那看着挺有意思，但我确实得去洗那个拖了太久的澡了。"
    s "好吧~~~"
    scene blank with Dissolve(2)
    scene c008_s008_034 with Dissolve(2)
    "呼。我以为洗个澡会让我好受点，结果还是疲惫，咳嗽也一直不停。我想是因为短时间内出去太多次了，但我也实在没什么选择。"
    scene c008_s008_035 with Dissolve(0.25)
    "我不会跟其他人说太多，但我的免疫力可能已经因为吃饭不规律而受损了。而且暴露在雾里也是，不管我裹得多严实。就算算上今天找到的东西，我们的食物也没多少，而且剩下的那些也谈不上营养均衡。我们的营养金字塔大概只剩一块正在朽掉的积木。"
    scene c008_s008_036 with Dissolve(0.25)
    "说到其他人，看见雪莉和卡莉相处得好，我挺高兴。卡莉本来就是随和的人，不过至少她在的时候，我能放心有人照看着雪莉。要是雪莉没在吃药，她情绪上一出岔子，就得有人在旁边。"
    if ch8_kallie_flash == "yes":
        "另外，雪莉好像正在影响卡莉，让她变得有点「无忧无虑」起来。我以前绝对想不到她会朝谁脱衣服，更别说从二楼窗户往下脱了。她错过了大学生活里那些不负责任和可疑的选择，稍微野一点也许对她有好处。"
    scene c008_s008_037 with Dissolve(0.25)
    j "*咳嗽* *咳嗽*"
    "虽然不太好这么说，但这也算是早睡了，毕竟电视上也没什么我非看不可的。希望睡长一点能让我舒服些。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_6_812", transition=Dissolve(1.0))()
    pause
    $ Hide("july_6_812", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene c008_s009_001 with Dissolve(2)
    play music nightmain2 fadein 2.0
    l "[player_name]？"
    scene c008_s009_002 with Dissolve(0.5)
    l "哦？好吧……"
    "{color=#66ff33}他{i}确实{/i}早早就睡了。很好，他该好好休息。这两天[player_name]看起来又苍白又疲惫。是出去太多次加上压力太大的双重结果。{/color}"
    "{color=#66ff33}而且我也没帮上忙。我要怎么向他解释，那是一种「干脆……让一切都大到压垮自己」的感觉？直接崩掉？我……{/color}"
    scene c008_s009_003 with Dissolve(0.25)
    "{color=#66ff33}我想我做不到，因为连我自己都不明白是怎么走到那一步的。不过这不重要。是他……他冲出来找我的。要不然我早就死在外面了。我会蠢到一个人跑出去送死。{/color}"
    l "……"
    scene blank with Dissolve(2)
    scene c008_s009_004 with Dissolve(2)
    l "在看书？"
    k "嗯？哦，劳拉……对。我……我昨晚跟[player_name]说过，没有电视，看书是打发时间的唯一办法。而且我不讨厌。我其实挺喜欢读书的。"
    scene c008_s009_005 with Dissolve(0.25)
    l "我可不行。上学和工作的时候我已经读够了。不过要是你能把阅读当享受，那真挺好的。希望这儿有些值得你花时间的东西，当然，别是教材就行。"
    k "我找到几本别人留下的书。不算多有深度，但能打发时间。"
    scene c008_s009_006 with Dissolve(0.5)
    l "[player_name]已经睡着了。我刚去看过他。他好像不太舒服。刚才在咳嗽，脸色也有点瘦削。"
    k "他老往外跑。而且他不肯让任何其他人去。"
    scene c008_s009_007 with Dissolve(0.25)
    l "说句公道话，我不觉得他是排斥这个想法。太过了。只是他属于那种凡事都要一个人扛的男人。而且我们刚到的时候你受了伤，我还失控了一阵子。他确实没法开口让我们把担子分过来。"
    k "……"
    scene c008_s009_008 with Dissolve(0.25)
    l "我觉得他再也不会让我一个人出门了。我也不知道他会不会让雪莉在没人看着的情况下做什么。不是说她有什么不好。她年纪轻，有时候有点毛躁。你懂的。你俩好像已经成了好朋友。"
    k "她是个好人。要不是被困在这儿，我敢肯定我们根本不会说话。不过我还挺喜欢她的，我们相处得也挺好。我只是觉得她需要有人在旁边。我不知道她之前一个人是怎么撑过来的，不管那是多久。"
    scene c008_s009_009 with Dissolve(0.25)
    l "所以她对你来说不算太难搞？我不瞒你说，她有时候确实会让我有点受不了。"
    k "我想我只是习惯周围有人一直聊天。大多数人甚至不在乎我有没有回应。他们只想一直说下去，中间不要有人插嘴。又或者，也许我只是习惯了被人弄得觉得自己应该闭嘴。至少雪莉在我身边的时候，还会试着把对话接下去。"
    if ch8_kallie_flash == "yes":
        scene c008_s009_010 with Dissolve(0.5)
        l "听起来她也正在影响你嘛。*窃笑*"
        k "我发誓，我提到你之前说的那件事的时候，没想过她会那样做。"
        scene c008_s009_011 with Dissolve(0.25)
        l "这么年轻又没心没肺，真好啊。等责任把这些夺走，再因为草率的决定惩罚你之前。"
        k "我连当个不负责任的大学生都没赶上。"
        scene c008_s009_012 with Dissolve(0.25)
        l "我也没有。"
        "{color=#66ff33}虽然理由不同。我不想细说——也不想重新撕开一道刚结的伤口——但听起来安德鲁确实偷走了她好几年的时光。等我们出去，我要狠狠揍他一顿。{/color}"
    scene blank with Dissolve(2)
    scene c008_s009_013 with Dissolve(2)
    "{color=#8bc7ff}操，梅茜就这么……没了。死了。我……{/color}"
    scene c008_s009_014 with Dissolve(0.5)
    "{color=#8bc7ff}我想亲眼去看，但我知道那不是个好主意。可我他妈这颗疯脑袋一直说「万一不是她呢？」，我一直觉得非去不可不可。但我知道，要是我真去了，我他妈就会彻底崩掉。{/color}"
    "{color=#8bc7ff}靠，真他妈糟，我需要点什么让情绪平下来，让这些该死的冲动停下来。我需要睡觉，可一闭上眼就看见梅茜她们死去，「她们全都死了」这个念头像死循环一样卡在我脑子里。{/color}"
    scene c008_s009_015 with Dissolve(0.25)
    "{color=#8bc7ff}天哪，我为什么在按时吃药这件事上不能更聪明一点？妈唠叨这事唠叨了那么久，搞得我都开始对此心生怨气。或者，我只是想当然地以为自己没事、不需要吃。现在我才知道，那是屁话。{/color}"
    scene c008_s009_016 with Dissolve(0.25)
    "{color=#8bc7ff}按理说，在几次把酒和药混着吃之后我早该吸取教训了，可我就只擅长当一个傻乎乎的大学生。{/color}"
    "{color=#8bc7ff}我……我在这儿待不下去了。{/color}"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_7_845", transition=Dissolve(1.0))()
    pause
    $ Hide("july_7_845", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music morning fadein 2.0
    scene c008_s010_001 with Dissolve(2)
    "{color=#66ff33}今天早上很安静。通常我起床的时候，[player_name]早就已经起了。不知道这是不是意味着他还在床上。如果是，我该让他多睡会儿。{/color}"
    "{color=#66ff33}我这是怎么了？我以前属于那种天一亮就起床的人。现在我想什么时候起就什么时候起。也算不上「想什么时候起就什么时候起」。我还在从那次不明智的外出中恢复。{/color}"
    scene c008_s010_002 with Dissolve(0.25)
    "{color=#66ff33}见鬼，我到现在都还在努力从第一次踏进雾里——那还只是到办公室之前——的后果中恢复过来。现在，只要我在外面待上任何一段时间，情况就会变得更糟。这到底给我造成了多少不可逆的伤害？{/color}"
    "{color=#66ff33}不知道医院里还有没有医务人员。要是没有，等我们出去以后，我得去一趟诊所。如果能出去的话。我现在也没那么确定了。希望这东西太稀罕了。{/color}"
    scene c008_s010_003 with Dissolve(0.5)
    k "劳拉？早啊。"
    l "早。要来点咖啡吗？"
    scene c008_s010_004 with Dissolve(0.25)
    k "呃，你看见雪莉了吗？"
    l "没有。你是我今天第一个说话的人。她不在自己房间吗？"
    scene c008_s010_005 with Dissolve(0.25)
    k "不在。洗手间里我也既没看见她，也没听见她。"
    l "她可不算安静的人。操。她能去哪儿……"
    scene c008_s010_006 with Dissolve(0.25)
    k "你觉得她会不会是去看她朋友的尸体了？"
    l "*叹气* 靠。去楼上看看。看看她是不是在上面。我去前门。后门汇合。"
    scene c008_s010_007 with Dissolve(0.25)
    k "那[player_name]呢？"
    l "我去叫他起来。"
    scene blank with Dissolve(2)
    scene c008_s010_008 with Dissolve(2)
    l "[player_name]？[player_name]？我需要你醒醒。拜托。"
    j "嗯唔~~~ 唔嗯~~~"
    scene c008_s010_009 with Dissolve(0.25)
    l "起来吧，[player_name]。我很想让你多睡一会儿，但大家都需要你。"
    j "{size=32}嗯……本来就不该睡这么晚。{/size}"
    scene c008_s010_010 with Dissolve(0.25)
    l "你脸色还是很苍白，不过问题不在这儿。卡莉觉得雪莉不见了。或者，她可能是去看她朋友的尸体了。"
    scene c008_s010_011 with Dissolve(0.5)
    j "什么？我甚至还没……{w=2}我得先喝杯咖啡才能处理这件事。什么？"
    l "卡莉觉得雪莉不见了。她在楼上找。我该去后门跟她汇合。"
    scene c008_s010_012 with Dissolve(0.25)
    j "我们连她走没走都不知道？"
    l "[player_name]，她不是那种一声不吭就消失的人。"
    scene c008_s010_013 with Dissolve(0.25)
    "是吗？我们并不怎么了解她，而且劳拉不知道她已经停药了。"
    j "操，我得套上衣服。她要是真去了那边，我得有准备。"
    scene c008_s010_014 with Dissolve(0.25)
    j "{b}操————{/b}！让大家他妈的别到处乱跑，这个要求很过分吗？我们是不是该给小组定几条基本规矩？！搞个他妈的结伴制度？"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c008_s010_015 with Dissolve(2)
    play music insidedark fadein 2.0
    k "楼上的家具被挪开了，我没看见她。"
    j "好，接下来这样。我进去，直接去隔壁那栋楼——"
    scene c008_s010_016 with Dissolve(0.25)
    k "卡森楼。雪莉说那栋楼叫这个名字。"
    scene c008_s010_017 with Dissolve(0.25)
    j "好。卡森楼。我直接过去。直奔梅茜那个房间。你们两个{b}待在原地。{/b}我不需要好几个人在外面乱晃。"
    l "明白。"
    scene c008_s010_018 with Dissolve(0.25)
    l "别往心里去。他只是因为又一次被人一声不吭地丢下、而且还是这么早被叫醒，火气大，这可以理解。"
    k "我……"
    scene c008_s010_019 with Dissolve(0.25)
    l "你没事的，卡莉。你是好孩子。他需要重新学着信任的，是我，是雪莉。"
    scene blank with Dissolve(2)
    scene c008_s011_001 with Dissolve(2)
    "我一路咒骂着冲到卡森楼的出口。我对雪莉很恼火——这可以理解——但心底里，我不得不承认，她大概也在应付着她自己的烂摊子。"
    scene c008_s011_002 with Dissolve(0.25)
    "她那么年轻，人生还在摸索阶段，偏偏还停着药，得在这噩梦般的处境里活下来，而现在甚至还没来得及消化「认识的人就死在两栋楼之外」这件事。"
    "等找到她，我得把火气收一收。"
    scene blank with Dissolve(1)
    scene c008_s011_003 with Dissolve(1)
    "门还是被堵着的。所以她不是从这边过来的。二楼还有另一组门，但从另一头被堵死了。"
    "二楼……操，我怎么一开始没想到这个？"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c008_s011_004 with Dissolve(2)
    play music school fadein 2.0
    "然后她就在那儿。就坐在那儿。谢天谢地。现在知道她人在哪儿，我就能把高度紧绷的焦虑松下来了。她现在知道自己能毫无阻碍地到这个房间，我早该想到她可能会过来。"
    "我心里攒着一大堆火气，得先搁到一边，因为我得小心地接近这件事。谁知道她现在是什么精神状态。要是她只是心血来潮跑过来的，我可要好好骂她一顿。"
    scene c008_s011_005 with Dissolve(0.5)
    j "雪莉？是我。"
    s "嗯？哦，[player_name]。我……"
    scene c008_s011_006 with Dissolve(0.25)
    menu:
        "[rd]狠狠说她。\n[rrd](雪莉 焦虑 +1)":
            $ s_anxiety += 1
            j "雪莉，你他妈搞什么？你知道找不到你的时候我们有多慌吧？就那么一声不吭地消失了。你总知道你不能他妈的这样吧！"
            scene c008_s011_007 with Dissolve(0.5)
            s "靠，对不起，我、我只是……我……"
            j "怎么回事？你不能再想干什么就干什么了！我知道你还是个大学生，但在这儿，你要是想活下去，就得赶紧学会长大。"
            scene c008_s011_008 with Dissolve(0.25)
            "得狠一点，才能让她明白这么做不合适。"
        "温和一点。\n[rgr](雪莉 好感 +1)":
            $ s_friend += 1
            j "所以你就这么跑过来了？打算在这儿搞点新作品？"
            scene c008_s011_007 with Dissolve(0.5)
            s "哦，不，我……我只是……"
            j "你知道之前找不到你，我们有多担心。"
            scene c008_s011_008 with Dissolve(0.25)
            s "对不起。我……我不是故意让你担心的，可是我……*叹气*"
            j "跟我说说吧。拜托。"
    scene c008_s011_009 with Dissolve(0.25)
    s "对不起。我就是快疯了。我昨晚一夜没睡。我的睡眠已经糟了一段时间了，一直都是。脑子里那些念头没完没了地闯进来，把我这颗疯脑袋转个不停。停药对我没好处。这点我知道，可现在真的特别糟。"
    j "是有什么特别的事吗？是梅茜的事？还是就……这一切？跟我说说。"
    scene c008_s011_010 with Dissolve(0.5)
    s "说「这一切」也没用，是我自己没处理好药的事。每次我以为不吃也能撑过去，我就会发作一次，然后迷失好几天，直到重新吃药、让药效回到身体里。可现在根本没办法补药。"
    scene c008_s011_011 with Dissolve(0.25)
    s "所以昨晚就是这样，整夜醒着，翻来覆去地纠结每一件小事。脑子里全是我自己各种惨死的方式，其中有些……"
    j "你不会死的。在我眼皮底下不会。"
    scene c008_s011_012 with Dissolve(0.25)
    s "问题不在这里。遇上侵入性思维的时候，事实根本不重要。它们享有优先权，因为它们全是我脑子里那堆疯狂的烂东西，而我的脑子很清楚我哪里最脆弱。它会告诉我，没人会爱我，我是个让人失望的人，我被抛下是因为没人在乎，而且……"
    s "所以我做了一件我知道可能有用的事。我来了这儿。这里算是我的快乐之地，是我觉得舒服的地方。我本来考虑过去找些美术用品——我确实翻找了几分钟，直到那股念头消退——但我发现自己根本想不出有什么想画的东西。"
    j "画画有用吗？"
    scene c008_s011_013 with Dissolve(0.25)
    s "有点用。它能让我分心不去想那些疯狂的东西。就像一条温暖的毯子裹住了我的脑子。但这没法替代重新吃药。我不可能二十四小时站在画布前面把它赶走。"
    j "我们也许得绕道去一趟最近的药店。"
    scene c008_s011_014 with Dissolve(0.25)
    s "我觉得不会那么容易。"
    j "那最近的美术用品店呢？"
    scene c008_s011_015 with Dissolve(0.5)
    s "大概一样难，不过还是谢谢你愿意提。"
    "雪莉长长地叹了一口气，那口气里压满了压力。如果有个温热的身体能让她靠着会有帮助，那我倒是可以做到。"
    j "我直说吧：我以为你可能会跑去卡森楼。"
    scene c008_s011_016 with Dissolve(0.5)
    s "去看梅茜？不。我做不到。我、我现在还不够坚强，做不到那件事。这我知道。我这颗装着猫的脑子里，好歹还剩下那么一点常识，告诉我那是个坏主意。因为要是我看见她，我就会开始想伤害自己，而我不想那样。"
    j "有自我保护意识是好事。比我们有些人强。至少你没像我一样被灼烧者喷了一脸。"
    scene c008_s011_017 with Dissolve(0.25)
    s "我……我们是不是得……"
    j "不用。路过的时候我们不用靠近那个房间。我特意确认过了。"
    s "那就好。"
    scene c008_s011_018 with Dissolve(0.25)
    j "听着，你出门一定要告诉别人你要去哪儿。就算是想来这儿也一样。等我们出去以后，我不想你哪天又在没跟任何人一起的情况下跑出去。这条规矩不只是针对你，是针对所有人。我们都得结伴，互相照应。"
    s "我……我尽量。我会的。"
    scene c008_s011_019 with Dissolve(0.25)
    j "你可能没意识到，但你已经是这个小组的一员了。是我们中的一员。这意味着你有一些责任，也有一些好处。但这也意味着你得让我们知道你在哪儿。好的一面是，如果你需要有人只是陪在身边，我们会在。"
    s "你们会在吗？"
    menu:
        "我们所有人都会。":
            scene c008_s011_020 with Dissolve(0.25)
            j "我们所有人都会。"
        "会的。我会。\n[rgr](雪莉 信任 +1)":
            $ s_trust += 1
            scene c008_s011_020 with Dissolve(0.25)
            j "会的。我会。"
    "我突然意识到，雪莉这辈子可能都没怎么有过一群死心塌地的伙伴。但眼下这个局面，正在锻造出几段我们谁都没料到的关系。"
    if s_friend >= 4 or s_desire >= 3:
        scene c008_s011_026 with Dissolve(0.5)
        s "你知道什么会有帮助吗？"
        j "来点内啡肽或者多巴胺的刺激？我不觉得那是个长远的办法。"
        scene c008_s011_027 with Dissolve(0.25)
        s "也不需要是长远的。我们不用真做爱。也许就稍微打闹一下，让我释放一下就行。"
        menu:
            "好，稍微一下。\n[rgr](雪莉 好感\欲望 +1)\n[pks]":
                $ s_friend += 1
                $ s_desire += 1
                scene c008_s011_030 with Dissolve(0.5)
                j "好，稍微一下。不过，我可不想因为自己心里堆了太多层东西，就靠这个来脱身。"
                s "你不用，除非你真想给我点高兴的理由。*窃笑*"
                scene c008_s011_031 with Dissolve(0.5)
                j "今天我们就用手指简单弄一下怎么样？"
                s "我没问题。来，我把它拉下来。让你免费通行，因为我可不想让你把手伸到下面去把我的内裤撑变形。"
                scene c008_s011_032 with Dissolve(0.25)
                j "只是把别的东西撑开，对吧？"
                scene c008_s011_033 with Dissolve(0.25)
                s "别说了，你这么一说我就湿了。"
                "我真喜欢打闹这一招居然这么容易就让她心情好转。"
                scene c008_s011_034 with Dissolve(0.5)
                j "等等，你身后那件是什么？你穿着它来的？"
                s "哦，那个？我找到的。柜子里有一件连帽衫。我当时在找美术用品——我确实有那么一阵发疯，觉得自己能做点什么——然后就看到它了。我想卡莉也许用得上。"
                j "哦，对，看着挺合适的。我们带回去给她看看。"
                scene c008_s011_035 with Dissolve(0.25)
                s "不过先……"
                play voice_loop shelley_slow
                scene c008_s011_036 with Dissolve(0.5)
                j "好好好，反正你的小穴就在那儿。"
                s "哦操，啊啊啊~~~~"
                j "我们伸几根进去吧。"
                s "好的~~~~"
                scene c008_s011_037 with Dissolve(0.5)
                show shelley_ch8_finger with Dissolve(0.25)
                s "哈啊~~~~ 就这样，啊啊啊~~~~"
                "不是要催她，不过我们今天可能没一整天可以这么耗着。"
                s "嗯唔~~~ 你要我脱掉上衣吗？给你点东西看？"
                j "你要是真脱，我可能会忍不住把你翻过来扒下裤子掏鸡巴。就现在这样，我下面已经有点硬了。"
                s "嗯唔~~~ 他要是觉得挤，就放他出来吧。"
                l "{size=30}[player_name]！雪莉！{/size}"
                scene c008_s011_038 with Dissolve(0.5)
                hide shelley_ch8_finger
                j "*叹气* 没人听我说话。"
                s "操~~~~ 我都快好了。"
                stop voice_loop
                scene c008_s011_039 with Dissolve(0.25)
                j "我大概没法叫她滚蛋。"
                s "呃呃~~~ 就先这样吧。我确实好多了，不过这可能只是因为有你。*窃笑*"
                scene c008_s011_040 with Dissolve(1)
                "我抓起那件连帽衫，在门口等着，雪莉花了十几秒把短裤和内裤重新穿好。"
                scene c008_s011_041 with Dissolve(0.5)
                s "劳拉会生我的气吧？"
                j "你在担心劳拉生气？"
                scene c008_s011_042 with Dissolve(0.25)
                s "她就像我妈一样，伙计。我心里有种根深蒂固的需求，就是不想让她失望。"
                j "但你就不介意我生气？"
                scene c008_s011_043 with Dissolve(0.25)
                if k_sex >= 1:
                    s "我都见过你的鸡巴了，伙计。而且我知道怎么让你原谅我。*窃笑*"
                else:
                    s "你是个男人。我朝你亮一下胸，你就会把这事全忘了。*窃笑*"
                jump ch8backinhall
            "那可不行。":
                j "那可不行。虽然这诱惑挺大，但我只能改天再说了。"
                scene c008_s011_028 with Dissolve(0.25)
                s "失望，不过我理解。有些男人需要场地浪漫一下之类的。不过你最好值这个价，因为这事可不会很快过去。"
                s "[player_name]，我确实很感激你来找我。也很抱歉这么难搞。不过我们不用把这件事告诉其他人吧？"
                scene c008_s011_029 with Dissolve(0.25)
                j "我们不用，不过你以后可以考虑一下。"
                s "……"
                scene c008_s011_023 with Dissolve(0.5)
    else:
        scene c008_s011_021 with Dissolve(0.5)
        s "*打哈欠* 操，我好累。"
        j "你上一次睡觉是什么时候？"
        scene c008_s011_022 with Dissolve(0.25)
        s "前天晚上。"
        j "听起来我们该送你回去了。别在路上猝死。"
        scene c008_s011_023 with Dissolve(0.25)
    s "好吧，我只想让你知道，我很抱歉……哦？！我还真找到东西了。"
    j "真的？"
    scene c008_s011_024 with Dissolve(0.5)
    s "对，有个柜子里有一件连帽衫。我当时在找美术用品——我确实有那么一阵发疯，觉得自己能做点什么——然后就找到了它。我想卡莉也许用得上。"
    j "哦，对，看着挺合适的。我们带回去给她看看。"
    l "{size=30}[player_name]！雪莉！{/size}"
    scene c008_s011_025 with Dissolve(0.5)
    j "*叹气* 没人听我说话。"
    s "我们快走吧，别等你朝别人发火。"
label ch8backinhall:
    scene blank with Dissolve(2)
    scene c008_s012_001 with Dissolve(2)
    l "你们两个在这儿啊。哦，谢天谢地，你们找到她了。"
    j "对，我在她的画室里碰到了雪莉。就在这儿。我们聊了些事，正准备回去。"
    scene c008_s012_002 with Dissolve(0.25)
    s "抱歉，我只是……需要去我的快乐之地。我最近一直没睡好，而且……"
    l "没关系，雪莉。你不用解释。我们每个人都在跟某种东西较劲。你能睡得着吗？我们还剩一点威士忌，你要是需要点什么助眠的话。"
    scene c008_s012_003 with Dissolve(0.25)
    s "我觉得我现在已经够累了，不需要什么。而且喝酒可能不是个好主意。"
    l "好吧，说得过去。我们送你回房间。"
    "也许劳拉会看出自己和雪莉有些共同之处，哪怕她不知道具体细节。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c008_s012_004 with Dissolve(2)
    play music insideday fadein 2.0
    "回宿舍的一路都很安静。我从来没把雪莉当成身手敏捷的人，但她走起路来那种笨拙，反倒衬出她衰弱得多快。"
    "一回到她房间，她就谢过我们，为添麻烦深深道了歉，然后踉跄着进去睡了个长觉。"
    play sound doorclose
    scene c008_s012_005 with Dissolve(0.5)
    l "所以……"
    j "别待在外面。"
    scene blank with Dissolve(2)
    scene c008_s012_006 with Dissolve(2)
    l "听着，很抱歉我没留下来，但你们两个消失得越久，我越担心。你们一直说要结伴、说要一起干，可转头就自己跑了。还自己一个人出门。万一你出事了怎么办？"
    menu:
        "这里不是民主投票。\n[rrd](劳拉 好感 -1)":
            $ l_friend -= 1
            j "劳拉，眼下这里不是民主投票。我在做艰难的决定，因为最近我们已经太多次死里逃生了。就算我受伤了，也没什么大不了。我会扛起来。这不就是这个世界的规则吗？男人他妈得更扛得住，因为所有人就是这么期望我们的。所以我会的。"
            scene c008_s012_007 with Dissolve(0.25)
            j "所以，当我说「留下」，那就是认真的。当我说「我们谁都不单独行动」，我是对你们所有人说的，因为每次去查看下一个房间有没有危险的那个人，都会是我。每。一。次。而且我这么干不是想当混蛋，也不是想当英雄。"
            j "我这么干是因为我他妈在乎你们所有人，不想看到你们中的任何一个受到更多伤害。如果这意味着最后你们都恨我，那就恨吧。至少你们能活着出去。"
            scene c008_s012_008 with Dissolve(0.25)
            l "……这个……我明白你的意思，虽然听着有点难受。"
        "这很合理。":
            j "这个立场是合理的，但你得明白，我觉得自己必须开始为整个小组的安全做那些严肃的、一瞬间就得做出的决定，因为最近我们已经太多次死里逃生了。哪怕这意味着我要让自己冒险，好把你们其他人挡在伤害之外。"
            scene c008_s012_007 with Dissolve(0.25)
            j "因为说到底，每次去查看下一个房间、下一个地点有没有危险的，都会是我。我得先出去，这样你才不会变得更糟。这样卡莉才不会再被灼烧者扑倒。我们甚至不知道她再次出门会是什么反应，可能会引发恐慌发作。"
            j "所以我这么干，是因为我他妈在乎你们所有人，不想看到你们任何一个陷入更深的危险。我在做每个选择时都会考虑潜在的危险，尽量挑出我能做的最好决定，哪怕这会让我自己身陷险境。"
            scene c008_s012_008 with Dissolve(0.25)
            l "好吧，我之前没从这个角度想过。"
    "劳拉早就习惯了一个人做主，让她听别人的命令她本来就不乐意，更别说对方还是个以前的同事了。"
    scene c008_s012_009 with Dissolve(0.25)
    l "那雪莉呢？那边发生了什么？这是我们需要知道的事吗？我知道她有点没心没肺，但——"
    scene c008_s012_010 with Dissolve(0.25)
    j "事情就是这样，劳拉。她应对得不算好，而且刚刚得知认识的人死了。我告诉她不能那样乱跑，但考虑到我们眼下这场该死的风暴，我也实在气不起来。"
    scene c008_s012_011 with Dissolve(0.25)
    l "嗯。我想我该多体谅一点。光是为我儿子担心，我就已经失控了。她可是真的失去了一个人。而且那个人就在步行可到的范围内。"
    j "我知道在「尽力」和「同情」之间找平衡很难，但我会尽力。"
    "别提药的事。如果雪莉自己想说，告诉她其他人，那是她的事。眼下我只能留心看着她。"
    play sound doorclose
    scene c008_s012_012 with Dissolve(0.5)
    k "你回来啦。我看雪莉已经回去了。我探头看她房间的时候她已经睡着了。她还好吗？"
    j "嗯，只是休息得很不好，就去了个能让她开心的地方。看来你已经试穿我们的小发现品了。挺合身的，很好。"
    scene c008_s012_013 with Dissolve(0.25)
    k "对。我在台子上看到它，还以为是要给我出门穿的。"
    scene c008_s012_014 with Dissolve(0.25)
    l "这料子够厚。虽然可能比不上皮夹克，但短距离应该没问题。"
    k "不错。你在哪儿找到的？"
    j "雪莉。她翻柜子找美术用品的时候看到了。所以我们得谢她。现在就只差帽子，我们就能出发了。"
    scene c008_s012_015 with Dissolve(0.25)
    l "我先把我们这儿的东西过一遍，想想该带什么。前几天我找到了一个急救包。不过还得看价值和背包空间来取舍。"
    j "嗯……你会以为学生宿舍里应该有更多包或者背包。当时我心理清单上没这一项，不过下次出去的时候可以考虑。"
    scene c008_s012_016 with Dissolve(0.25)
    k "我可以问问雪莉有没有。等她醒了再说。如果她一直睡不好，我们暂时别打扰她。"
    j "那挺好。毕竟我还有些东西要搜刮——"
    scene c008_s012_017 with Dissolve(0.25)
    l "不行。你看起来又累又苍白，你今天吃东西了吗？你不能这副样子出门。"
    "我想这是劳拉在用她的方式重新找回一些对生活的掌控感。既然我自封了领队，她至少要确保还有另一个人在盯着我。而且她也不算没道理，毕竟我今天连一杯咖啡都还没喝。"
    j "好吧。我吃点东西，看看之后什么感觉。"
    scene blank with Dissolve(2)
    scene c008_s012_018 with Dissolve(2)
    "尽管我很不情愿再浪费更多时间，我还是答应了劳拉的要求。我把它当成一根橄榄枝——一个妥协——算是对「我把话说得那么明白，以后在小组的事情上会越来越强势」的一点补偿。"
    "雪莉翻出一件连帽衫给卡莉，多少缓解了我的焦虑。只要再找到个头饰，我那份「重新上路」的清单就差不多齐了。"
    scene blank with Dissolve(1)
    scene c008_s012_019 with Dissolve(1)
    "要是对自己诚实点，今天已经太晚了，任何返程的尝试都可能出问题。就算是在灰蒙蒙的日光下，出门也有危险。"
    "等太阳落下去、天更黑了？那谁知道那会给灼烧者带来什么优势呢。更长、更深的阴影会削弱我的视野，也削弱我避开它们的能力。"
    scene blank with Dissolve(1)
    scene c008_s012_020 with Dissolve(1)
    "在宿舍里，我尽量让自己忙起来，主要就是再检查一遍其他房间，看有没有之前漏掉的有用东西。劳拉则在梳理我们剩下物资的优先级。食物、药品和水是必需品。换洗的衣服最多只能留下一两套，前提是装得下。"
    scene blank with Dissolve(2)
    scene c008_s012_021 with Dissolve(2)
    "太阳落下之后，劳拉和卡莉都回了各自的房间，最终是要休息一下。我没指望她们会更晚才起。没有电子设备分散注意力，我们的生物钟已经变成了农民作息。"
    scene c008_s012_022 with Dissolve(1)
    "我顺便 看了一眼雪莉，她睡得很沉。不知道跟她聊那些话有没有用，还是她终于把力气耗完了。配给有限，可能让连续几天不休息变得更难熬。"
    "没什么事可做之后，我回了自己的房间。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_7_1004", transition=Dissolve(1.0))()
    pause
    $ Hide("july_7_1004", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    $ renpy.music.set_volume(.20, 0.0, channel = "music")
    scene c008_s013_001 with Dissolve(2)
    play music rain fadein 2.0
    "时间不早了。我睡不着，正到处晃悠，这时听见了一阵既出乎意料又熟悉的声音。我想我不该太惊讶；气压整整一天都在积累，空气里有种明显的变化。所以当我听到玻璃上传来轻柔的噼啪声时，我就走过去看。"
    "果然太黑了，什么都看不见。于是我决定上楼，试试三楼的某个房间。"
    scene c008_s013_002 with Dissolve(0.5)
    "对，情况好不到哪儿去，不过我在雾层大部分之上，能看见外面正下着绵密的雨，只能看到模糊的轮廓。远处传来低沉的轰鸣声，说明这是一场不小的风暴。是雾灾以来我们遇到的第一场。"
    "我承认我很意外。我想我只是一直以为我们不会有正常的天气变化，好像我们在不止一个方面都跟世界其余部分断开了联系。"
    scene c008_s013_003 with Dissolve(0.5)
    "我很想打开窗户，就为了闻闻那熟悉的夏日阵雨的味道。不过光是看看也就够了。有那么一会儿，我想知道这会对雾产生什么影响。会不会变淡？会不会被冲散？我们哪有那么好的运气。不过万一真有，明天倒可能是最好的突围时机。"
    scene c008_s013_004 with Dissolve(0.25)
    k "在下雨吗？我好像听见楼下窗户被敲得嗒嗒响，可我几乎什么都看不见。"
    j "哦，卡莉，呃，对。我听到的也是这个。我上来是想看看能不能看得清楚些。还是黑的，不过借着灯光能看出来。"
    scene c008_s013_005 with Dissolve(0.5)
    k "对。因为还有电，所以我们多少有点光污染。"
    "这能维持多久？几个星期？大概更短。"
    scene c008_s013_006 with Dissolve(0.25)
    j "你怎么找到我的？"
    k "门还开着。"
    j "啊，对哦。"
    scene c008_s013_007 with Dissolve(0.5)
    k "哦，看。那是不是有一盏红灯在闪？"
    j "嗯？让我……"
    scene c008_s013_008 with Dissolve(0.25)
    j "靠，还真是。"
    k "那是……那是什么？"
    j "那是飞机或者直升机上那种{a=https://en.wikipedia.org/wiki/Navigation_light}航行灯{/a}，用来告诉别人它们正在黑暗或者恶劣天气中飞行。也就是说，外面有人。"
    scene c008_s013_009 with Dissolve(0.25)
    k "这是好消息吧？说明这片地方之外还有别人。说不定甚至还在从医院里救人。"
    j "对。这……证实了我们一直以来的猜测。"
    "这是这一切开始以来我们第一个好消息。可以带回给其他人了。"
    scene c008_s013_010 with Dissolve(0.25)
    k "嗯……我已经看不见它了。"
    j "大概钻进云里去了。"
    scene c008_s013_104 with Dissolve(0.25)
    k "我本该因为现在看不见而失望的，但知道它刚才还在，我就已经松了口气了。"
    j "因为这证实了我们一直希望是真的东西？"
    scene c008_s013_105 with Dissolve(0.25)
    k "对。我们该告诉劳拉。明天吧。现在让她睡。"
    j "明天。不过总算能带回去一个好消息，也不错。"
    scene c008_s013_011 with Dissolve(0.5)
    "我们沉默地站了好一会儿，只是着迷于这场天气。它是一小块出乎意料的{b}从前{/b}，几乎让人怀旧又充满希望。我确实觉得我们俩都在盼着能再看见一架飞机。"
    "我偷偷侧眼看了卡莉一下，觉得她比平时还要美。也许只是气氛的关系。外面透进来的微弱光线照亮了她柔和的轮廓，触动了我心里的某根弦。"
    scene c008_s013_012 with flash
    scene c008_s013_013 with Dissolve(0.5)
    "闪电亮起的时候，我惊讶于她居然没有退缩。"
    j "你 不怕雷暴？"
    scene c008_s013_014 with Dissolve(0.25)
    k "不怕。我喜欢。雨声，隆隆的雷声。很让人安心。不知道为什么，就是这样。"
    j "不错。"
    scene c008_s013_015 with Dissolve(1)
    "我不知道我们在窗边徘徊了多久。她每次挪动一下，我都以为这场守望就要结束了。"
    scene c008_s013_016 with Dissolve(1)
    "过了一会儿，卡莉明显开始发抖。下了雨之后气温降了，而她那身打扮可不是为了保暖。我能理解，在没有空调的夏天，她为什么这么穿。"
    if k_sex == 0:
        scene c008_s013_017 with Dissolve(0.25)
        k "我玩够了。开始冷了。我想回去再睡一会儿。雨应该有点用。我喜欢这种白噪音。"
        scene c008_s013_018 with Dissolve(0.25)
        j "对。我也得一样。要是明天还要出去，我得尽量多休息。"
        k "……"
        jump ch8k_nextmorning
    else:
        menu:
            "抱住她给她取暖。\n[rgr](卡莉 爱意 +1)\n[rrd](卡莉 欲望 -1)\n[pks]":
                scene c008_s013_020 with Dissolve(0.5)
                "最后，我决定从卡莉身后靠上去，双臂环住她。我说服自己这只是为了给她取暖。如果她不愿意，她只要说一声就行了。"
                scene c008_s013_021 with Dissolve(0.5)
                "但说实话，我觉得自己是在试探。想知道我们之前那些亲密时刻是不是只是一时冲动下的短暂放纵，看看在相对正常的情况下，卡莉会不会不习惯这样跟我亲密。"
                scene c008_s013_022 with Dissolve(0.25)
                k "唔嗯~~~"
                "她发出了一点几乎听不见的声音，听起来介于开心和如释重负之间。过了一会儿，她整个人靠回了我的怀里。我不确定这是不是有意的，但我能感觉到她的屁股压在我的胯上。只希望我那半硬的玩意儿没太明显。"
                scene c008_s013_023 with Dissolve(0.25)
                k "这样真好。"
                j "我也这么觉得。"
                "我们又一次安静下来，就那么站着看雨。我猜她在盼着再看见一架飞机。而我这边，注意力有点太集中在她身上了。柔软、娇小，闻起来那么香，我一直在想她脱光的样子，然后……"
                scene c008_s013_024 with Dissolve(0.25)
                k "[player_name]……"
                j "哦？我是不是……离得太近了？抱得太紧了？还是……"
                "下面硬得厉害，大概正戳着她屁股呢。"
                scene c008_s013_025 with Dissolve(0.5)
                k "没有。我……我……这样让我很开心。这是我很久以来最放松、最安心、最快乐的一次。甚至比雾灾之前还要好。我第一次觉得安全。"
                j "很高兴我能派上点用场。"
                scene c008_s013_026 with Dissolve(0.25)
                k "不是……只是我不习惯……这是我第一次觉得自由。可以做我想做的事，说我想说的话，穿我想穿的衣服。"
                j "我很抱歉是这样。"
                scene c008_s013_027 with Dissolve(0.25)
                k "别道歉。知道有你和劳拉支持我，知道等我们出去以后，你们两个会试着帮我回家，帮我离开安德鲁，这感觉真好。"
                j "我们会的。"
                if k_friend >= 13 or k_trust >= 6 and k_friend >= 10:
                    $ ch8_kallie_sex = "yes"
                    $ k_love += 1
                    $ k_sex += 1
                    $ k_desire -=1
                    call ch8_kallie_sex from _call_ch8_kallie_sex
                    jump ch8k_nextmorning
                else:
                    scene c008_s013_028 with Dissolve(1)
                    j "时间不早了。或者差不多吧。*轻笑* 也许我们该回去了。"
                    scene c008_s013_017 with Dissolve(0.25)
                    k "*叹气* 对，我这边也够了。开始冷了。我得多睡一会儿。雨应该有点用。我喜欢这种白噪音。"
                    j "我确实也该一样。要是明天还要出去，我得尽量多睡。"
                    if ch8_kallie_flash == "yes":
                        scene c008_s013_019 with Dissolve(0.25)
                        j "不过要是运气好，说不定还能在窗户上多看几眼胸。"
                        k "……"
                    else:
                        scene c008_s013_018 with Dissolve(0.25)
                        k "……"
                    jump ch8k_nextmorning
            "提议该回去了。":
                j "时间不早了。或者差不多吧。*轻笑* 也许我们该回去了。"
                scene c008_s013_017 with Dissolve(0.25)
                k "*叹气* 对，我这边也够了。开始冷了。我得多睡一会儿。雨应该有点用。我喜欢这种白噪音。"
                j "我确实也该一样。要是明天还要出去，我得尽量多睡。"
                if ch8_kallie_flash == "yes":
                    scene c008_s013_019 with Dissolve(0.25)
                    j "不过要是运气好，说不定还能在窗户上多看几眼胸。"
                    k "……"
                else:
                    scene c008_s013_018 with Dissolve(0.25)
                    k "……"
                jump ch8k_nextmorning
label ch8k_nextmorning:
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("nightmare1", transition=Dissolve(1.0))()
    pause
    $ Hide("nightmare1", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    scene white with Dissolve(2)
    play music horror fadein 2.0
    scene c008_s014_001 with Dissolve(2)
    "{color=#ffcccc}现在几点了？我早该出门上班了。不能迟到。我得保住这份工作，我们才付得起婚礼的钱。也许我还能请到不只是我家人的人。{/color}"
    scene c008_s014_002 with Dissolve(0.25)
    "{color=#ffcccc}不不不，不对。今天一定是周末。是吗？我没穿上班的衣服。我……安德鲁绝不会让我穿成这样出门。露出这么多皮肤。{/color}"
    scene c008_s014_002-1 with Dissolve(0.25)
    scene c008_s014_002 with Dissolve(0.25)
    "{color=#ffcccc}这不对劲。什么东西看着都不对劲，全都是……{/color}"
    scene c008_s014_003 with Dissolve(0.25)
    "{color=#ffcccc}我……我真的不想待在这里。这一点我很确定。就算我不是在这个时间回家会感到不自在……{/color}"
    an "卡莉。"
    show ch8dream
    an "{size=65}{b}没有我你什么都不是！{/b}{/size}" with hpunch
    k "不不不~~~~"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("july_8_736", transition=Dissolve(1.0))()
    pause
    $ Hide("july_8_736", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    play music morning fadein 2.0
    hide ch8dream
    if ch8_kallie_sex == "yes":
        scene c008_s013_099 with Dissolve(2)
        k "唔嗯~~~ 唔呃~~~！！"
        scene c008_s013_100 with Dissolve(0.25)
        k "哦……哦，靠……靠……"
        "{color=#ffcccc}这里是……哦，对，宿舍房间。和[player_name]。我们……昨晚。{/color}"
        scene c008_s013_101 with Dissolve(0.25)
        "{color=#ffcccc}天哪，这些噩梦……是不是越来越严重了？感觉是。而且就算睡着了我也躲不开安德鲁。就像他在追我，被他抓到的时候，他嘴里说出的全是最伤人的话。{/color}"
        scene c008_s013_102 with Dissolve(0.25)
        "{color=#ffcccc}是不是因为我……跟[player_name]的事？我只是感觉……就是……我说不清。{/color}"
        scene c008_s013_103 with Dissolve(0.25)
        "{color=#ffcccc}我得走了。我不想吵醒他。我……我不想让他……看见我这个样子。他会问，而我……现在不行。今天不行。{/color}"
    else:
        scene c008_s014_006 with Dissolve(2)
        k "嗯唔！！！啊啊啊~~！！"
        scene c008_s014_007 with Dissolve(0.25)
        k "哦……哦，靠……靠……"
        "{color=#ffcccc}这里是……哦，对，宿舍房间。{/color}"
        scene c008_s014_008 with Dissolve(0.25)
        "{color=#ffcccc}天哪，这些噩梦……是不是越来越严重了？感觉是。而且就算睡着了我也躲不开安德鲁。就像他在追我，被他抓到的时候，他嘴里说出的全是最伤人的话。{/color}"
        "{color=#ffcccc}就算现在睡在床上，我还是觉得没休息够。好累。{/color}"
        scene c008_s014_009 with Dissolve(0.25)
        "{color=#ffcccc}我该起来了。我绝对不想再回到床上。现在躺下去，只会被最糟糕的东西弄醒。{/color}"
    scene blank with Dissolve(2)
    scene c008_s014_010 with Dissolve(2)
    if ch8_kallie_sex == "yes":
        "看来卡莉中途还是起来了。真可惜，我本来想跟她一起醒的，但这也说得通。她和劳拉同住一间房，我不觉得她会想编一套昨晚在哪儿的说辞。"
        "就算我们俩都同意她该离开安德鲁，我也不敢保证劳拉知道我们俩「办事」之后会高兴。不过，就只是那样吗？原始的、动物性的交媾？我倒愿意相信不只是那样。"
    else:
        "今天早上这儿确实好像凉快了一点。出门之前我说不准，但也许那场雨帮了我们。"
    scene c008_s014_011 with Dissolve(0.5)
    j "早啊，劳拉。你昨晚一觉睡到雨停吗？"
    l "看样子是。那声音太熟悉了，待着还挺舒服的。我睡得特别沉。直到在浴室撞见卡莉，我才知道下过雨。"
    scene c008_s014_012 with Dissolve(0.25)
    j "她告诉你了？她有没有也提到看见一架飞机？或者直升机？我不确定是什么，但昨晚我们看见了航行灯。"
    l "对，她说了。让我告诉你，蹲马桶的时候收到这种消息，感觉还真他妈不错。所以你到底看见什么了？"
    scene c008_s014_013 with Dissolve(0.25)
    j "就是飞机或直升机底部那种常见的灯。它在远处，不过我觉得这场雨其实改善了能见度。我只知道，这证实了我们一直希望是真的东西。"
    l "你觉得那是从医院那边来的概率有多大？"
    scene c008_s014_014 with Dissolve(0.5)
    j "跟别处一样大。比我们昨天掌握的情况要好。"
    l "对。我就把它当成给大家的一点及时提振吧。这也确实意味着我们得重新动起来。"
    scene c008_s014_015 with Dissolve(0.25)
    j "只要给姑娘们找到几顶帽子就行，这就是我今天的目标。到了这个地步，要是我得抓几条毛巾或者床单裹她们脑袋，像戴头巾一样，我们也照干不误。"
    j "说到「姑娘们」……"
    l "我最后听见的时候卡莉在洗澡，雪莉还在自己房间里睡着。"
    scene c008_s014_016 with Dissolve(0.25)
    j "很好。所以人齐了。我去弄点咖啡，然后换好装备出门。"
    l "你觉得这场雨对雾有影响吗？"
    j "我觉得有这个可能。很快就能知道。"
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    scene c008_s014_017 with Dissolve(2)
    play music outsideday2 fadein 2.0
    "哇，我可真是又惊又喜。雨{b}确实{/b}让情况好转了。雾还在外面，但薄了很多。我的视野相当不错。我不打算冒这个险，不过我确实在想，不穿外套我能撑多久。"
    scene c008_s014_018 with Dissolve(0.5)
    "但我现在能看见我们的「朋友」在外面游荡了。既然它们最擅长的攻击方式是从灌木丛后面或者厚雾墙里伏击我们，那它们的威胁就小多了。不过还是恐怖得很，而且我——等离开这个地狱之后——很想知道它们到底是什么。"
    scene blank with Dissolve(1)
    scene c008_s014_019 with Dissolve(1)
    "我甚至完全不知道它们是怎么追踪附近的人。比如说，它们对声音基本没反应，我也看不出它们能不能看见东西。热量？气味？它们真是个能让科学家们挖到宝的大问号。"
    scene blank with Dissolve(1)
    scene c008_s014_020 with Dissolve(1)
    "真可悲，我发现自己在许愿，希望面对的只是僵尸而不是这些东西。要是电视和电影能作参考的话，僵尸的行动倒是可以预测。"
    scene c008_s014_021 with Dissolve(0.5)
    "它们只想要脑子，或者想吞吃活人（为什么从来没想过要吃别的僵尸的肉？），而且通常根据声音和视线行动（这两样东西按理说应该随着腐烂而退化）。灼烧者却完全没给我们任何关于其目的或者吸引它们的因素的线索。"
    scene c008_s014_022 with Dissolve(0.5)
    "好了，白日梦够了。该动身去最后一栋宿舍楼了。雾是这副样子，说不定我能创纪录地赶到那儿。而且，求老天保佑，那边也许还有些值钱的东西可以顺走。"
    scene blank with Dissolve(2)
    scene c008_s014_023 with Dissolve(2)
    "进展顺利。如果雾的浓度维持不变，我也许还能再跑一个地方。也许回前几天我去看过的那间男生宿舍，就是有灼烧者的那栋。我意识到三楼我还没好好查过，我可不想留下任何没翻过的石头。"
    stop music fadeout 2.0
    scene c008_s014_024 with Dissolve(0.25)
    u "嘿！！！！嘿，这边！！！我的天哪，我不敢相信这儿还有别人！"
    "这正是我想说的。"
    scene c008_s014_025 with Dissolve(0.5)
    b1 "我的天哪！我还以为只剩我一个了。天哪，我在里面待了好几周了。"
    "这家伙没戴口罩也没戴手套。他疯了吗？我得在他把自己弄伤之前把他弄进屋里去。"
    j "站住！别动！我过来找你！"
    play music monster fadein 2.0
    scene c008_s014_026 with hpunch
    b1 "*咳嗽* *咳嗽*"
    "靠，一个灼烧者刚刚——"
    j "嘿！！！嘿！！！你后面！！"
    scene c008_s014_027 with hpunch
    b1 "什么？！操操操！！"
    scene c008_s014_028 with vpunch
    "那一刻，一切都感觉不真实了。断裂了。声音渐渐远去。感觉就像我在电视或者显示器上看这一幕。很快我就会恢复知觉，而到那时我才会意识到，那一刹那的震惊把我钉在原地动弹不得。"
    scene c008_s014_029 with hpunch
    "但那已经足够让灼烧者把他扑倒在地了。他在尖叫，哀求我去救他。可在我耳朵里，那只是静电噪音。"
    play sound gas
    scene c008_s014_030 with flashyellow
    "然后事情变得更糟了。糟得多得多。尖叫变成了咕噜咕噜的呛咳声。"
    play sound gas
    scene c008_s014_031 with flashyellow
    "与其说对我，不如说对他。不过，有些东西一个人不该亲眼、亲耳看到。"
    play sound gas
    scene c008_s014_032 with flashyellow
    "操。哦，操。我……操……"
    if persistent.ch8_complete == False:
        $ persistent.ch8_complete = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_chapter8", transition=slideright)()
        pause
        $ Hide("achievement_chapter8", transition=dissolve)()
        $ quick_menu = True
#jump to script 2
    jump chapter09
#endout
    stop music fadeout 2.0
    scene blank with Dissolve(2)
    play music menumain fadein 2.0
    window hide
    show datetime_1 at truecenter with dissolve
    show datetime_2 at truecenter with dissolve
    $ Show("tobecontinued", transition=Dissolve(1.0))()
    pause
    $ Hide("tobecontinued", transition=Dissolve(1.0))()
    hide datetime_2 with dissolve
    hide datetime_1 with dissolve
    # Leads into game end panel.
    scene gameend with Dissolve(2)
    #play music menumain fadein 2.0
    "你已经到达当前版本的结尾了。感谢游玩。如果你想把存档留着等下次更新，请回滚。"
    "感谢所有赞助者一直以来的支持！"
    "请在{a=https://www.patreon.com/ilsproductions}Patreon{/a}、{a=https://subscribestar.adult/ilsproductions}Subscribestar{/a}，或者{a=https://x.com/IlsProductions}X/Twitter{/a}、{a=https://bsky.app/profile/ilsproductions.bsky.social}Bluesky{/a}上关注{b}TOXICity{/b}。"
    # This ends the game.
    scene blank with Dissolve(4)
    $ renpy.pause ()
    $ renpy.full_restart()
    return
