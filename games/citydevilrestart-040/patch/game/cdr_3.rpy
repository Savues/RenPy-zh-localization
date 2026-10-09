label cdr_3:

    scene black with Dissolve(1.0)
    pause 2
    pause 1

###### SWEETHOME, STREETS - MAY, RY

label maybar:

    play music2 pick_your_self_up fadein 2 volume 0.8
    
    show maybar_1 with Dissolve(0.5)
    $ renpy.pause(4.3, hard=True)
    
    play sound may_shower_close
    
    scene maybar_2 with Dissolve(0.3)
    pause 2
    
    stop sound fadeout 0.3
    
    show maybar_3 with Dissolve(0.2)
    hide maybar_1
    $ renpy.pause(3.9, hard=True)
    pause 1
    show maybar_4 with Dissolve(0.2)
    hide maybar_3
    $ renpy.pause(1, hard=True)
    pause 14.5
    scene black with Dissolve(0.2)
    pause 0.3
    scene maybar_5 with Dissolve(0.6)
    ''
    scene maybar_6 with Dissolve(0.5)
    ''
    scene maybar_7 with Dissolve(0.4)
    ''
    scene maybar_8 with Dissolve(0.4)
    ''
    scene maybar_9 with Dissolve(0.4)
    ''
    scene maybar_10 with Dissolve(0.4)
    ''
    stop music2 fadeout 3
    
    scene black with Dissolve(0.5)
    pause 2
    
    play music2 free_flowing_loop_1 fadein 3 volume 1
    play sound4 city_traffic_1 fadein 5 volume 0.05 loop
    
    show maybar_11 with Dissolve(0.5)
    $ renpy.pause(18.9, hard=True)
    
    scene maybar_11_1 with Dissolve(0.4)
    "街上几乎空无一人，只有几盏路灯在抵挡黑暗。"
    scene maybar_12 with Dissolve(0.3)
    "远处传来引擎的嗡鸣，偶尔夹杂着路人的说话声。"
    scene maybar_13 with Dissolve(0.3)
    may 10 "（真够典型的……）" with Dissolve(0.3)
    scene maybar_14 with Dissolve(0.3)
    may 10 "（出租车怎么不动了？）" with Dissolve(0.3)
    scene maybar_15 with Dissolve(0.3)
    may 10 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene maybar_16 with Dissolve(0.3)
    may 10 "（他是不是走错街了？）" with Dissolve(0.3)
    scene maybar_17 with Dissolve(0.3)
    may 10 "（这个点一个人走路还真让人不舒服……）" with Dissolve(0.3)
    scene maybar_18 with Dissolve(0.3)
    may 10 "（不过房子很近。走到车那儿应该没事。）" with Dissolve(0.3)
    scene maybar_19 with Dissolve(0.3)
    may 10 "（奇怪，他在软件上没回消息。）" with Dissolve(0.3)
    scene maybar_20 with Dissolve(0.3)
    may 10 "（是没看到？还是他属于那种讨厌打字的司机？）" with Dissolve(0.3)
    may 10 "（一般来说，出租车司机看不到乘客都会回头确认。）"
    scene maybar_21 with Dissolve(0.3)
    may 10 "（嗯……车还停在隔壁那条街。离我家有点远，不过算了，也不是什么大事。）" with Dissolve(0.3)
    scene maybar_22 with Dissolve(0.3)
    may 10 "（我走过去上车，然后这事就算过去了。）" with Dissolve(0.3)
    play sound2 ry_car_loop loop fadein 6 volume 0.5
    play sound ry_car_start
    
    stop music2 fadeout 1
    $ renpy.music.set_volume(0.6, delay=0, channel=u'music3')
    play music3 phonk_cdr_1_lowpass fadein 3
    $ renpy.music.set_volume(0, delay=0, channel=u'music4')
    play music4 phonk_cdr_1 fadein 3 volume 0.8
    
    scene maybar_23 with Dissolve(0.3)
    pause 1
    scene maybar_24 with Dissolve(0.3)
    pause 0.8
    scene maybar_25 with Dissolve(0.3)
    pause 0.6
    scene maybar_26 with Dissolve(0.3)
    pause 1.3
    
    $ renpy.music.set_volume(1, delay=0.5, channel=u'music3')
    
    scene maybar_27 with Dissolve(0.3)
    ry 3 "哟，[may]，是你吗？！" with Dissolve(0.3)
    scene maybar_28 with Dissolve(0.3)
    ry 3 "最近怎么样？" with Dissolve(0.3)
    may 10 "（他怎么会在这儿？巧合？）" with Dissolve(0.3)
    scene maybar_29 with Dissolve(0.3)
    may 10 "[ry]……嗨。你来这儿干什么？" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0, delay=0.3, channel=u'music3')
    $ renpy.music.set_volume(1, delay=0.3, channel=u'music4')
    
    scene maybar_30 with Dissolve(0.3)
    ry 3 "“这个啊，我看到你了，然后你……全身都是黑色！”" with Dissolve(0.3)
    ry 3 "“真的好靓，你不冷吗？”"
    
    $ renpy.music.set_volume(1, delay=0.3, channel=u'music3')
    $ renpy.music.set_volume(0, delay=0.3, channel=u'music4')
    
    scene maybar_31 with Dissolve(0.3)
    may 10 "“我……不会冻着。我的出租车在等。”" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0, delay=0.3, channel=u'music3')
    $ renpy.music.set_volume(1, delay=0.3, channel=u'music4')
    
    scene maybar_32 with Dissolve(0.3)
    ry 3 "出租车？" with Dissolve(0.3)
    scene maybar_33 with Dissolve(0.3)
    ry 3 "要搭车吗？" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=0.3, channel=u'music3')
    $ renpy.music.set_volume(0, delay=0.3, channel=u'music4')
    
    scene maybar_34 with Dissolve(0.3)
    may 10 "不不，谢谢，我有车，很快就到了。" with Dissolve(0.3)
    scene maybar_35 with Dissolve(0.3)
    ry 3 "好吧，随你。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.7, delay=0.3, channel=u'music3')
    
    show maybar_36 with Dissolve(0.2)
    $ renpy.pause(5.3, hard=True)
    
    scene maybar_37 with Dissolve(0.3)
    may 10 "（他没走。）" with Dissolve(0.3)
    may 10 "（他为什么这么执着？）"
    scene maybar_38 with Dissolve(0.3)
    may 10 "（如果他继续纠缠，我就只能直说了。）" with Dissolve(0.3)
    scene maybar_39 with Dissolve(0.3)
    may 10 "[ry]，真的……我只是想走一段路。别跟着我。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1.5, delay=0.3, channel=u'music3')
    
    scene maybar_40 with Dissolve(0.3)
    ry 3 "“万一你找不到自己的出租车呢？”" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.8, delay=0.3, channel=u'music3')
    
    scene maybar_41 with Dissolve(0.3)
    may 10 "不会的。" with Dissolve(0.3)
    scene maybar_42 with Dissolve(0.3)
    may 10 "我就住这附近。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.3, delay=0.3, channel=u'music3')
    play sound3 city_traffic_1 fadein 2 volume 0.4 loop
    
    stop sound2 fadeout 4
    scene maybar_43 with Dissolve(0.3)
    pause 2
    
    scene maybar_44 with Dissolve(0.3)
    pause 1.5
    scene maybar_45 with Dissolve(0.3)
    pause 1.5
    scene maybar_46 with Dissolve(0.3)
    pause 1.5
    scene maybar_47 with Dissolve(0.3)
    may 10 "“哎呀，糟了……”" with Dissolve(0.3)
    scene maybar_48 with Dissolve(0.3)
    taxidriver3 1 "“这里没什么好看的，小姐。”" with Dissolve(0.3)
    scene maybar_49 with Dissolve(0.3)
    may 10 "“我想那是我叫的车。”" with Dissolve(0.3)
    scene maybar_50 with Dissolve(0.3)
    taxidriver3 1 "“啊，你是下单的那位？”" with Dissolve(0.3)
    scene maybar_51 with Dissolve(0.3)
    taxidriver3 1 "“抱歉抱歉！”" with Dissolve(0.3)
    scene maybar_52 with Dissolve(0.3)
    taxidriver3 1 "“但你看，我没法载你！”" with Dissolve(0.3)
    scene maybar_53 with Dissolve(0.3)
    may 10 "“哎呀没事没事……没什么大不了的。”" with Dissolve(0.3)
    scene maybar_54 with Dissolve(0.3)
    may 10 "“我就……等一等。或者再叫一辆。”" with Dissolve(0.3)
    play sound2 ry_car_loop loop fadein 1 volume 0.5
    scene maybar_55 with Dissolve(0.3)
    taxidriver3 1 "“千万别给差评啊！”" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0, delay=0.3, channel=u'music3')
    $ renpy.music.set_volume(1, delay=0.3, channel=u'music4')
    
    scene maybar_56 with Dissolve(0.3)
    may 10 "“不会不会，放心！”" with Dissolve(0.3)
    taxidriver3 1 "“你可以取消这单，再叫一辆车。”" with Dissolve(0.3)
    scene maybar_57 with Dissolve(0.3)
    ry 3 "“确定不要我这一程？”" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.5, delay=0.3, channel=u'music3')
    $ renpy.music.set_volume(0, delay=0.3, channel=u'music4')
    
    scene maybar_58 with Dissolve(0.3)
    ry 3 "“副驾都给你坐。”" with Dissolve(0.3)
    scene maybar_59 with Dissolve(0.3)
    may 10 "“这……挺诱人的，不过……我还是再叫一辆吧。”" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0, delay=0.3, channel=u'music3')
    $ renpy.music.set_volume(1, delay=0.3, channel=u'music4')
    $ renpy.music.set_volume(1, delay=0.5, channel=u'sound2')
    play sound3 car_door_2_open
    
    scene maybar_60 with Dissolve(0.3)
    ry 3 "“别害羞嘛。我还给你开门呢！”" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.5, delay=0.3, channel=u'music3')
    $ renpy.music.set_volume(0, delay=0.3, channel=u'music4')
    $ renpy.music.set_volume(0.3, delay=0.5, channel=u'sound2')
    
    scene maybar_61 with Dissolve(0.3)
    may 10 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene maybar_62 with Dissolve(0.3)
    ry 3 "“上车吧，走咯！”" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0, delay=0.3, channel=u'music3')
    $ renpy.music.set_volume(1, delay=0.3, channel=u'music4')
    $ renpy.music.set_volume(1, delay=0.5, channel=u'sound2')
    
    scene maybar_63 with Dissolve(0.3)
    ry 3 "“我保证不撩你！嘿嘿……”" with Dissolve(0.3)
    
    show maybar_64 with Dissolve(0.3)
    $ renpy.pause(4, hard=True)
    
    $ renpy.music.set_volume(0.5, delay=0.3, channel=u'music4')
    play sound dm1
    
    scene maybar_65_1 with hpunch
    
    $ renpy.music.set_volume(1, delay=1, channel=u'music4')
    
    pause 0.5
    scene maybar_65 with Dissolve(0.3)
    pause 1
    scene maybar_66 with Dissolve(0.3)
    play sound3 car_door_2_close
    ry 3 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene maybar_67 with Dissolve(0.3)
    ry 3 "{cps=5}……{/cps}" with Dissolve(0.3)

    scene maybar_68 with Dissolve(0.3)
    pause 1.5
    scene maybar_69 with Dissolve(0.3)
    pause 1
    scene maybar_70 with Dissolve(0.3)
    pause 1.5
    
    $ renpy.music.set_volume(0, delay=2, channel=u'music4')
    $ renpy.music.set_volume(1, delay=2, channel=u'music3')
    
    stop sound2 fadeout 4
    scene black with Dissolve(1.0)
    
    $ renpy.music.set_volume(1, delay=0.3, channel=u'music4')
    
    $ renpy.pause (2,hard=True)
    
    pause 2
    
### SIRENEYES, OUTSIDE
    play sound3 ry_car_loop loop fadein 1 volume 0.5
    
    show maybar_71 with Dissolve(1.0)
    pause 1
    may 10 "谢谢你载我。虽然没必要，但……还是谢谢。" with Dissolve(0.3)
    ry 3 "“行了行了，不用谢我！”" with Dissolve(0.3)
    
    stop music4 fadeout 10
    stop music3 fadeout 10
    stop sound4 fadeout 1
    stop music2 fadeout 10
    play sound2 maybar_elevator_1
    
    show maybar_72 with Dissolve(0.3)
    hide maybar_71
    $ renpy.pause(1, hard=True)
    stop sound3 fadeout 1
    $ renpy.pause(8, hard=True)
    
    play sound4 maybar_elevator_2
    
    $ renpy.pause(2.5, hard=True)
    
    $ renpy.music.set_volume(1, delay=0, channel=u'music4')
    $ renpy.music.set_volume(1, delay=0, channel=u'music3')
    play music3 elevator_music_speaker_loop
    
    $ renpy.pause(1.5, hard=True)
    
    scene maybar_73 with Dissolve(0.3)
    may 10 "“等等……你为什么跟我一起走？”" with Dissolve(0.3)
    scene maybar_74 with Dissolve(0.3)
    may 10 "“我自己走到门口就行。”" with Dissolve(0.3)
    scene maybar_75 with Dissolve(0.3)
    ry 3 "“这可不像你平时的样子，[may]。你是要去夜店吧。”" with Dissolve(0.3)
    scene maybar_76 with Dissolve(0.3)
    may 10 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene maybar_77 with Dissolve(0.3)
    may 10 "（那你在这儿又怎么解释？）" with Dissolve(0.3)
    scene maybar_78 with Dissolve(0.3)
    ry 3 "“真没想到你是会去蹦迪的类型。”" with Dissolve(0.3)
    scene maybar_79 with Dissolve(0.3)
    may 10 "“我不是去蹦迪的。”" with Dissolve(0.3)
    scene maybar_80 with Dissolve(0.3)
    ry 3 "“那你来这儿干什么？”" with Dissolve(0.3)
    ry 3 "“第一次来这种地方？”"
    ry 3 "“别担心，我来得也不多。一个月大概一次……”"
    scene maybar_81 with Dissolve(0.3)
    may 10 "“只是见个人。”" with Dissolve(0.3)
    scene maybar_82 with Dissolve(0.3)
    ry 3 "“这可有意思了！你还真是不爱亮底牌啊？”" with Dissolve(0.3)
    scene maybar_83 with Dissolve(0.3)
    may 10 "“你在说什么？”" with Dissolve(0.3)
    scene maybar_84 with Dissolve(0.3)
    ry 3 "“不是个老头子吧？”" with Dissolve(0.3)
    scene maybar_85 with Dissolve(0.3)
    may 10 "“我——天啊，[ry]！我是去见朋友！”" with Dissolve(0.3)
    scene maybar_86 with Dissolve(0.3)
    ry 3 "“哟，朋友……我猜是那位男的？”" with Dissolve(0.3)
    scene maybar_87 with Dissolve(0.3)
    ry 3 "“他对你来说是什么人？”" with Dissolve(0.3)
    scene maybar_88 with Dissolve(0.3)
    ry 3 "“别说什么「只是朋友」，我可不信。”" with Dissolve(0.3)
    scene maybar_89 with Dissolve(0.3)
    may 10 "“他……是我的全部。”" with Dissolve(0.3)
    scene maybar_90 with Dissolve(0.3)
    may 10 "“我是说——”" with Dissolve(0.3)
    scene maybar_91 with Dissolve(0.3)
    may 10 "“他是跟我非常亲近的人！”" with Dissolve(0.3)
    scene maybar_92 with Dissolve(0.3)
    ry 3 "“全部？哇，这么说在你心里这人就跟神一样。”" with Dissolve(0.3)
    scene maybar_93 with Dissolve(0.3)
    may 10 "“你非得对每件事都要评论吗？”" with Dissolve(0.3)
    scene maybar_94 with Dissolve(0.3)
    ry 3 "“放轻松，只是好奇你怎么看。”" with Dissolve(0.3)
    scene maybar_95 with Dissolve(0.3)
    may 10 "“你干嘛还要送我过去啊？！”" with Dissolve(0.3)
    scene maybar_96 with Dissolve(0.3)
    ry 3 "“护送一个穿漂亮裙子的美女——这有什么问题？”" with Dissolve(0.3)
    scene maybar_97 with Dissolve(0.3)
    may 10 "“这位小姐可没要求护送。”" with Dissolve(0.3)
    scene maybar_92 with Dissolve(0.3)
    ry 3 "“那要是那位男的想靠近一点呢？比如说，现在？”" with Dissolve(0.3)
    scene maybar_93 with Dissolve(0.3)
    may 10 "“这位小姐说不要。我们甚至都不是朋友！”" with Dissolve(0.3)
    scene maybar_98 with Dissolve(0.3)
    ry 3 "“而且我不许你只把我当「朋友」。”" with Dissolve(0.3)
    scene maybar_99 with Dissolve(0.3)
    ry 3 "“我猜你觉得我不懂什么「女性逻辑」吧？”" with Dissolve(0.3)
    scene maybar_100 with Dissolve(0.3)
    ry 3 "“你对别人来说太好了。你值得更好的！”" with Dissolve(0.3)
    scene maybar_101 with Dissolve(0.3)
    may 10 "“你话真多……”"
    scene maybar_102 with Dissolve(0.3)
    ry 3 "“我只是想说，你就像糖果，[may]。连蝴蝶结都配齐了。”" with Dissolve(0.3)
    scene maybar_103 with Dissolve(0.3)
    ry 3 "“你只露出一面，但我知道包装纸下面藏着很棒的东西。”" with Dissolve(0.3)
    scene maybar_104 with Dissolve(0.3)
    ry 3 "“别人觉得你冷淡，其实你只是不肯对任何人展示温柔的那一面。”" with Dissolve(0.3)
    scene maybar_105 with Dissolve(0.3)
    may 10 "（温柔的一面？）" with Dissolve(0.3)
    scene maybar_106 with Dissolve(0.3)
    may 10 "（你以为我是什么人？）" with Dissolve(0.3)
    scene maybar_107 with Dissolve(0.3)
    may 10 "“我才不是那样！”" with Dissolve(0.3)
    scene maybar_108 with Dissolve(0.3)
    ry 3 "“喝完一杯鸡尾酒再说这话，我可能就娶你了。”" with Dissolve(0.3)
    scene maybar_109 with Dissolve(0.3)
    ry 3 "“但只要有人够耐心，你就会敞开心扉。”" with Dissolve(0.3)
    scene maybar_110 with Dissolve(0.3)
    may 10 "“耐心？”" with Dissolve(0.3)
    scene maybar_111 with Dissolve(0.3)
    ry 3 "“鲜花、糖果、浪漫——全套。”" with Dissolve(0.3)
    scene maybar_112 with Dissolve(0.3)
    ry 3 "“你知道我对你是认真的吧？”" with Dissolve(0.3)
    scene maybar_113 with Dissolve(0.3)
    ry 3 "“我觉得你该给自己一个机会，换个角度看事情。”" with Dissolve(0.3)
    scene maybar_114 with Dissolve(0.3)
    ry 3 "“你太放不开自己了。”" with Dissolve(0.3)
    scene maybar_115 with Dissolve(0.3)
    ry 3 "“如果你愿意，我可以教你再自由一点。”" with Dissolve(0.3)
    ry 3 "“你还没厌倦躲在墙后面吗？”"
    
    play sound slap_in_the_face
    
    scene maybar_116 with hpunch
    pause 1.5
    
    scene maybar_117 with Dissolve(0.3)
    may 10 "“管好你的手，不然我的高跟鞋就招呼你脸上了。”" with Dissolve(0.3)
    scene maybar_118 with Dissolve(0.3)
    ry 3 "“好好好，别激动。”" with Dissolve(0.3)
    scene maybar_119 with Dissolve(0.3)
    ry 3 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene maybar_120 with Dissolve(0.3)
    ry 3 "“但老实说，[may]——你就一次都不想放纵一下吗？”" with Dissolve(0.3)
    scene maybar_121 with Dissolve(0.3)
    may 10 "“我现在这样就挺好，[ry]。”" with Dissolve(0.3)
    scene maybar_122 with Dissolve(0.3)
    ry 3 "“自制力是个陷阱，[may]。”" with Dissolve(0.3)
    
    play sound2 maybar_elevator_3
    pause 0.3
    
    scene maybar_123 with Dissolve(0.3)
    
    play sound3 elevator_bell
    
    ry 3 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    stop music3 fadeout 1
    $ renpy.music.set_volume(0, delay=0, channel=u'music2')
    $ renpy.music.set_volume(0.3, delay=0, channel=u'music3')
    play music2 syreneyes_2 fadein 3
    play music4 syreneyes_2_lowpass fadein 3
    
    scene maybar_124 with Dissolve(0.5)
    ry 3 "“好吧，随你。看来你还没完全懂我的意思。”" with Dissolve(0.3)
    scene maybar_125 with Dissolve(0.3)
    ry 3 "“你早晚会明白的。”" with Dissolve(0.3)
    
### SIRENEYES CLUB

    $ renpy.music.set_volume(1, delay=0.5, channel=u'music2')
    $ renpy.music.set_volume(0, delay=0.5, channel=u'music3')
    
    scene maybar_126 with Dissolve(0.3)
    pause 2.5
    scene maybar_127 with Dissolve(0.3)
    saguard1 1 "晚上好。你们在名单上吗？" with Dissolve(0.3)
    
    stop music4
    play sound clothes_2
    $ renpy.music.set_volume(1, delay=0, channel=u'music3')
    
    scene maybar_128 with Dissolve(0.3)
    ry 3 "这是我的人。让我们进去，她跟我一起。" with Dissolve(0.3)
    
    play sound2 clothes_4
    
    scene maybar_129 with Dissolve(0.3)
    may 10 "[ry]！放手！" with Dissolve(0.3)
    
    play sound3 clothes_5
    
    scene maybar_130 with Dissolve(0.3)
    ry 3 "“女生喝酒前不都要先吊着一下吗？”" with Dissolve(0.3)
    scene maybar_131 with Dissolve(0.3)
    saguard1 1 "请便。" with Dissolve(0.3)
    scene maybar_132 with Dissolve(0.3)
    pause 2
    scene maybar_133 with Dissolve(0.3)
    ry 3 "“看看多好玩！”" with Dissolve(0.3)
    scene maybar_134 with Dissolve(0.3)
    ry 3 "“走吧，我请你喝一杯。”" with Dissolve(0.3)
    scene maybar_135 with Dissolve(0.3)
    may 10 "“我什么都不要。而且你为什么还跟着我？”" with Dissolve(0.3)
    scene maybar_136 with Dissolve(0.3)
    may 10 "“你可是只答应了载我一程！”" with Dissolve(0.3)
    scene maybar_137 with Dissolve(0.3)
    ry 3 "“像你这样的美女，你觉得我会丢下你一个人？”" with Dissolve(0.3)
    scene maybar_138 with Dissolve(0.3)
    ry 3 "“看看大家都在盯着你看。”" with Dissolve(0.3)
    scene maybar_139 with Dissolve(0.3)
    may 10 "“我不想让人看见我跟你在一起。”" with Dissolve(0.3)
    scene maybar_140 with Dissolve(0.3)
    ry 3 "“哎呀，[may]，放松点嘛！”" with Dissolve(0.3)
    scene maybar_141 with Dissolve(0.3)
    ry 3 "“让我请你——随便挑一杯鸡尾酒。”" with Dissolve(0.3)
    scene maybar_142 with Dissolve(0.3)
    pause 1.5
    scene maybar_143 with Dissolve(0.3)
    ry 3 "“你人都来了就来放松一下，别浪费时间了！”" with Dissolve(0.3)
    scene maybar_144 with Dissolve(0.3)
    may 10 "（他旁边那个女孩是谁？）" with Dissolve(0.3)
    scene maybar_145 with Dissolve(0.3)
    ry 3 "“嘿，怎么了？生我气了？”" with Dissolve(0.3)
    may 10 "（是女服务员的制服，但她明显空闲得过分了。）" with Dissolve(0.3)
    scene maybar_146 with Dissolve(0.3)
    may 10 "（她花那么多时间跟他毫无意义地闲聊，把他从工作上分心……）" with Dissolve(0.3)
    scene maybar_147 with Dissolve(0.3)
    ry 3 "[may]，别这样阴沉着脸嘛。少了这副表情，这家店里的每个男人很快就都会被你迷得团团转！" with Dissolve(0.3)
    scene maybar_148 with Dissolve(0.3)
    may 10 "（呃，看看他们！）" with Dissolve(0.3)
    scene maybar_149 with Dissolve(0.3)
    ry 3 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene maybar_150 with Dissolve(0.3)
    pause 2
    scene maybar_151 with Dissolve(0.3)
    may 10 "（不管怎么说，看起来他们在一起玩得挺开心。）" with Dissolve(0.3)
    scene maybar_152 with Dissolve(0.3)
    ry 3 "“真好奇——他哪一点吸引了你？”" with Dissolve(0.3)
    scene maybar_153 with Dissolve(0.3)
    may 10 "一切。" with Dissolve(0.3)
    scene maybar_154 with Dissolve(0.3)
    ry 3 "“全部？”" with Dissolve(0.3)
    scene maybar_155 with Dissolve(0.3)
    ry 3 "“挺猛啊。”" with Dissolve(0.3)
    scene maybar_156 with Dissolve(0.3)
    ry 3 "“你就这么随口说说？”" with Dissolve(0.3)
    scene maybar_157 with Dissolve(0.3)
    ry 3 "“那你告诉我，他到底是哪一点让你这么着迷？”" with Dissolve(0.3)
    scene maybar_158 with Dissolve(0.3)
    may 10 "“要说清楚太花时间了。”" with Dissolve(0.3)
    scene maybar_159 with Dissolve(0.3)
    ry 3 "“而且你看，他现在正忙着呢。”" with Dissolve(0.3)
    scene maybar_160 with Dissolve(0.3)
    ry 3 "“我们喝一杯等等吧。说不定等会儿你就不想要他了。”" with Dissolve(0.3)
    scene maybar_161 with Dissolve(0.3)
    may 10 "（他们只是同事，只是同事……）" with Dissolve(0.3)
    ry 3 "“这里肯定有你会喜欢的东西。你来就是为了这个，对吧？”" with Dissolve(0.3)
    scene maybar_162 with Dissolve(0.3)
    may 10 "（可恶，他一直在给我洗脑。）" with Dissolve(0.3)
    scene maybar_163 with Dissolve(0.3)
    may 10 "“你刚才说什么？”" with Dissolve(0.3)
    
    show maybar_164 with Dissolve(0.2)
    ry 3 "“我在说鸡尾酒，[may]。”" with Dissolve(0.3)
    ry 3 "“你知道人们来这里不会没有原因的。”"
    show maybar_167 with Dissolve(0.2)
    hide maybar_164
    ry 3 "“这里有能像魔法一样击中你的东西。不只是好喝——会让你惊爆眼球。”" with Dissolve(0.3)
    show maybar_168 with Dissolve(0.2)
    hide maybar_167
    may 10 "“我不要那种东西。”" with Dissolve(0.3)
    show maybar_164 with Dissolve(0.2)
    hide maybar_168
    ry 3 "“你不要，是因为你不懂它的原理。你该试试——不会后悔的。”" with Dissolve(0.3)
    show maybar_165 with Dissolve(0.2)
    hide maybar_164
    ry 3 "“它不只是饮料。它是一次做真实的自己的机会。”" with Dissolve(0.3)
    ry 3 "“你的内心藏着什么，[may]，你不知道吗？”"
    show maybar_167 with Dissolve(0.2)
    hide maybar_165
    may 10 "（我打扮得这么漂亮，他还没看我……）" with Dissolve(0.3)
    ry 3 "[may]？" with Dissolve(0.3)
    show maybar_168 with Dissolve(0.2)
    hide maybar_167
    may 10 "我不需要那个。" with Dissolve(0.3)
    show maybar_166 with Dissolve(0.2)
    hide maybar_168
    ry 3 "“好吧，好吧……”" with Dissolve(0.3)
    
    scene maybar_171 with Dissolve(0.3)
    waitressbar2 1 "晚上好！您要点些什么吗？" with Dissolve(0.3)
    scene maybar_172 with Dissolve(0.3)
    ry 3 "我要一杯蓝湖。" with Dissolve(0.3)
    scene maybar_173 with Dissolve(0.3)
    ry 3 "那您呢？" with Dissolve(0.3)
    scene maybar_174 with Dissolve(0.3)
    may 10 "不用了，谢谢。我不喝了。" with Dissolve(0.3)
    scene maybar_175 with Dissolve(0.3)
    waitressbar2 1 "只要一杯蓝湖？" with Dissolve(0.3)
    scene maybar_176 with Dissolve(0.3)
    ry 3 "对。把单子交给那位调酒师。" with Dissolve(0.3)
    scene maybar_177 with Dissolve(0.3)
    "他指了指[hayato]。"
    scene maybar_178 with Dissolve(0.3)
    waitressbar2 1 "明白了！我一定把您的单子交给他！" with Dissolve(0.3)
    scene maybar_179 with Dissolve(0.3)
    pause 2
    scene maybar_180 with Dissolve(0.3)
    ry 3 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene maybar_181 with Dissolve(0.3)
    pause 1.5
    scene maybar_182 with Dissolve(0.3)
    "[ry]注意到了他的纹身。"
    
    show maybar_164 with Dissolve(0.2)
    ry 3 "你怎么看纹身？" with Dissolve(0.3)
    show maybar_170 with Dissolve(0.2)
    hide maybar_164
    may 10 "什么都不要。" with Dissolve(0.3)
    show maybar_166 with Dissolve(0.2)
    hide maybar_170
    ry 3 "“拜托，那玩意儿酷毙了！有没有想过弄一个？”" with Dissolve(0.3)
    show maybar_170 with Dissolve(0.2)
    hide maybar_166
    may 10 "不知道。大概不会。" with Dissolve(0.3)
    show maybar_165 with Dissolve(0.2)
    hide maybar_170
    ry 3 "“想听点疯狂的吗？”" with Dissolve(0.3)
    ry 3 "“你会吓一跳的。”"
    show maybar_170 with Dissolve(0.2)
    hide maybar_165
    may 10 "请便。" with dissolve
    show maybar_169 with Dissolve(0.2)
    hide maybar_170
    ry 3 "“你觉得纹身最终留在身体的哪一层？”" with Dissolve(0.3)
    show maybar_170 with Dissolve(0.2)
    hide maybar_169
    may 10 "“皮肤的某一层。”" with Dissolve(0.3)
    show maybar_169 with Dissolve(0.2)
    hide maybar_170
    ry 3 "“更下面那层？”" with dissolve
    show maybar_170 with Dissolve(0.2)
    hide maybar_169
    may 10 "“对，就在皮肤深层的下面。”" with Dissolve(0.3)
    show maybar_166 with Dissolve(0.2)
    hide maybar_170
    ry 3 "“那为什么它们不会扩散开？”" with Dissolve(0.3)
    show maybar_170 with Dissolve(0.2)
    hide maybar_166
    may 10 "“我看过动画——一根细针腾出空间，然后把墨填进去。”" with Dissolve(0.3)
    show maybar_169 with Dissolve(0.2)
    hide maybar_170
    ry 3 "“是皮肤组织把它固定在那里的，对吧？”" with Dissolve(0.3)
    show maybar_170 with Dissolve(0.2)
    hide maybar_169
    may 10 "“差不多。”" with dissolve
    show maybar_164 with Dissolve(0.2)
    hide maybar_170
    ry 3 "“不过这理解相当表面。”" with Dissolve(0.3)
    ry 3 "“墨进入皮肤时，颗粒是巨大的。”"
    ry 3 "“墨分子非常庞大。”"
    show maybar_169 with Dissolve(0.2)
    hide maybar_164
    ry 3 "“我们的免疫系统会做出反应，派上百万……呃……巨噬细胞前往纹身部位。”" with Dissolve(0.3)
    ry 3 "“巨噬细胞是能吞噬细菌、死亡细胞和其他外来有毒微粒的细胞。”"
    ry 3 "“这些巨噬细胞聚集过来吞噬墨汁，但无法完全分解它。”"
    ry 3 "“因为墨分子太大了。”"
    show maybar_166 with Dissolve(0.2)
    hide maybar_169
    ry 3 "“于是它们形成一道墙，然后死掉。”" with Dissolve(0.3)
    ry 3 "“这样就防止纹身在体内扩散。”"
    show maybar_164 with Dissolve(0.2)
    hide maybar_166
    ry 3 "“这件事会持续你的一生。”" with dissolve
    ry 3 "“此时此刻，你的免疫系统正在生产的数百万巨噬细胞存在的唯一目的，就是维持你的纹身不散。”"
    show maybar_170 with Dissolve(0.2)
    hide maybar_164
    may 10 "“你说我的知识表面，自己给的却是歪曲的事实。”" with Dissolve(0.3)
    may 10 "“巨噬细胞确实会对抗墨汁，但不完全是那样。”"
    may 10 "“在愈合过程中，巨噬细胞会把墨汁包裹进自己的细胞质里。”"
    may 10 "“愈合之后，它们仍然抓着那些色素颗粒。”"
    may 10 "“由于墨汁始终惰性且不溶，老化过程会一直继续。”"
    may 10 "“抓着墨汁的巨噬细胞最终会衰老死亡。”"
    may 10 "“当新细胞取代它们时，可能吸收残留的色素，纹身就逐渐褪色。”"
    show maybar_169 with Dissolve(0.2)
    hide maybar_170
    ry 3 "{cps=5}……{/cps}" with Dissolve(0.3)
    ry 3 "咳咳……"
    show maybar_164 with Dissolve(0.2)
    hide maybar_169
    ry 3 "“那你告诉我——激光祛除的时候会发生什么？”" with Dissolve(0.3)
    show maybar_169 with Dissolve(0.2)
    hide maybar_164
    may 10 "{cps=5}……{/cps}" with dissolve
    show maybar_166 with Dissolve(0.2)
    hide maybar_169
    ry 3 "“这方面我知道得不多。他们基本就是用激光把它烧掉——我猜新细胞会重新长出来？”" with Dissolve(0.3)
    show maybar_170 with Dissolve(0.2)
    hide maybar_166
    may 10 "“就像我们说的，色素颗粒太大，靠淋巴系统排不出去。”" with Dissolve(0.3)
    may 10 "“激光只是把它们打碎成淋巴系统能处理的小块。”"
    show maybar_166 with Dissolve(0.2)
    hide maybar_170
    ry 3 "“我去……”" with Dissolve(0.3)
    ry 3 "“这些你都是哪儿学的？”"
    ry 3 "“我是说，你自己又没有纹身吧？”"
    show maybar_165 with Dissolve(0.2)
    hide maybar_166
    ry 3 "“除非……你藏在什么特别的地方藏了一个，嘿嘿。”" with Dissolve(0.3)
    show maybar_164 with Dissolve(0.2)
    hide maybar_165
    ry 3 "“说真的，你怎么会知道这些？”" with Dissolve(0.3)
    show maybar_168 with Dissolve(0.2)
    hide maybar_164
    may 10 "“他告诉我的。我们一起研究过。”" with Dissolve(0.3)
    show maybar_166 with Dissolve(0.2)
    hide maybar_168
    ry 3 "“他有纹身？”" with Dissolve(0.3)
    show maybar_170 with Dissolve(0.2)
    hide maybar_166
    may 10 "“没有。他有一次找到一篇文章，跟我分享了。”" with Dissolve(0.3)
    may 10 "“我们交叉核对了资料，得出了这些结论。”"
    show maybar_164 with Dissolve(0.2)
    hide maybar_170
    ry 3 "“所以这些知识……呃……为什么要研究这个啊……”" with Dissolve(0.3)
    ry 3 "“算了。既然你给我上了一课，我待会儿再给你一次机会尝尝鸡尾酒——我请客！”"
    show maybar_167 with Dissolve(0.2)
    hide maybar_164
    may 10 "（她好像要走了……）" with Dissolve(0.3)
    
    scene maybar_183 with Dissolve(0.3)
    may 10 "“我……我去他那儿。再谢谢你载我一程。”" with Dissolve(0.3)
    scene maybar_184 with Dissolve(0.3)
    
    ry 3 "“需要我的时候随时发消息！”" with Dissolve(0.3)
    
    stop music2 fadeout 2
    
    scene black with Dissolve(1.0)
    
    play music3 syreneyes_1 fadein 2
    
    pause 2
    scene bar_night2_again_27 with Dissolve(1.0)
    may 10 "（我走向他的时候，心脏疯狂跳动，快要从胸口蹦出来。）" with Dissolve(0.3)
    scene bar_night2_again_74 with Dissolve(0.5)
    may 10 "（空气仿佛凝滞了，但简短交谈之后，焦虑开始消退……）" with Dissolve(0.3)
    may 10 "（取而代之的是一股暖意在体内蔓延。）"
    scene bar_night2_again_107 with Dissolve(0.5)
    may 10 "（我接过他特意为我调的那杯酒，毫不犹豫地喝了下去。）" with Dissolve(0.3)
    scene bar_night2_again_108 with Dissolve(0.5)
    may 10 "（冰凉的液体顺着喉咙滑下，留下一丝余韵……）" with Dissolve(0.3)
    scene bar_night2_again_124 with Dissolve(0.5)
    may 10 "（我抬起头看他，忽然觉得整个世界都倾斜了。）" with Dissolve(0.3)
    may 10 "（思绪变得迟缓、纠缠——像是沉进柔软的雾里。）"
    scene bar_night2_again_142 with Dissolve(0.5)
    may 10 "（他……美得惊人。五官更锋利，笑容更迷人。）" with Dissolve(0.3)
    may 10 "（一股奇异的热流涌遍全身，在太阳穴突突直跳。）"
    
    scene black with Dissolve(1.0)
    pause 0.5
    
    scene outside_night2_gohome_4 with Dissolve(0.3)
    may 10 "（我这是怎么了？）" with Dissolve(0.3)
    scene outside_night2_gohome_37 with Dissolve(0.3)
    may 10 "（为什么移不开视线？）" with Dissolve(0.3)
    scene outside_night2_gohome_44 with Dissolve(0.5)
    may 10 "（有那么一瞬间，我感到一股无法抗拒的冲动，想触碰他。）" with Dissolve(0.3)
    scene outside_night2_gohome_45 with Dissolve(0.5)
    may 10 "（想把他拉得更近……）" with Dissolve(0.3)
    scene outside_night2_gohome_46 with Dissolve(0.5)
    may 10 "（想做点不该做的事。）" with Dissolve(0.3)
    scene black with Dissolve (0.3)
    
    stop music3 fadeout 4
    
    pause 0.5
    may 10 "（真蠢。）" with Dissolve(0.3)
    may 10 "（太鲁莽了。）"
    scene black with Dissolve(1.0)
    pause 2
    pause 2

###### HOME, NIGHT - MAY

label nighthome:

    play music relaxing_lofi_ena__sascha_ende fadein 8

    scene nighthome_1 with Dissolve(1.0)
    ''
    scene nighthome_2 with Dissolve(0.5)
    pause 1.5
    scene nighthome_3 with Dissolve(0.3)
    pause 1
    scene nighthome_4 with hpunch
    may 10 "（那么……昨天到底发生了什么……？）" with Dissolve(0.3)
    scene nighthome_5 with Dissolve(0.3)
    may 10 "（为、为什么……）" with Dissolve(0.3)
    scene nighthome_6 with Dissolve(0.3)
    may 10 "（他为什么睡在我旁边？！）" with Dissolve(0.3)
    scene nighthome_7 with Dissolve(0.3)
    may 10 "（完了……我昨晚做了什么？）" with Dissolve(0.3)
    
    scene black with Dissolve(1.0)
    pause 0.5
    
    scene outside_night2_gohome_51 with Dissolve(1.0)
    pause 0.5
    scene outside_night2_gohome_54 with Dissolve(0.3)
    pause 0.3
    scene outside_night2_gohome_55 with Dissolve(0.3)
    pause 0.3
    scene outside_night2_gohome_56 with Dissolve(0.3)
    pause 0.3
    scene outside_night2_gohome_73 with Dissolve(0.3)
    pause 0.3
    scene outside_night2_gohome_80 with Dissolve(0.3)
    pause 0.5
    
    scene black with Dissolve(1.0)
    pause 1
    
    scene nighthome_8 with Dissolve(0.3)
    may 10 "（我简直像个彻底的傻瓜……）" with Dissolve(0.3)
    scene nighthome_9 with Dissolve(0.3)
    may 10 "（太丢脸了！怎么会变成这样？）" with Dissolve(0.3)
    scene nighthome_10 with Dissolve(0.3)
    may 10 "（我想现在就消失……）" with Dissolve(0.3)
    scene nighthome_11 with Dissolve(0.3)
    pause 1
    scene nighthome_12 with Dissolve(0.5)
    pause 1.3
    scene nighthome_13 with Dissolve(0.5)
    pause 1.6
    scene nighthome_14 with Dissolve(0.5)
    pause 2
    scene nighthome_15 with Dissolve(0.5)
    pause 1.5
    scene black with Dissolve(1.0)
    pause 2
    
    scene nighthome_16 with Dissolve(0.7)
    pause 0.5
    may 13 "（难道接下来一辈子都得躲着他？）" with Dissolve(0.3)
    scene nighthome_17 with Dissolve(0.5)
    may 13 "（还是干脆假装什么都没发生？）" with Dissolve(0.3)
    scene nighthome_18 with Dissolve(0.5)
    may 13 "（我昨天那么努力想给他留下好印象……）" with Dissolve(0.3)
    may 13 "（而现在……感觉一切都毁了。）"
    scene nighthome_19 with Dissolve(0.6)
    ''
    scene nighthome_20 with Dissolve(0.5)
    ''
    show nighthome_21 with Dissolve(0.4)
    $ renpy.pause (9, hard=True)
    show nighthome_22 with Dissolve(0.3)
    may 13 "（他去哪儿了？）" with Dissolve(0.3)
    scene nighthome_23 with Dissolve(0.3)
    may 13 "（我怎么会没注意到他已经走了？）" with Dissolve(0.3)
    scene nighthome_24 with Dissolve(0.3)
    may 13 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene nighthome_25 with Dissolve(0.3)
    may 13 "（门开着。）" with Dissolve(0.3)
    scene nighthome_26 with Dissolve(0.3)
    may 13 "（他会去哪儿？）" with Dissolve(0.3)
    scene nighthome_27 with Dissolve(0.3)
    may 13 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene nighthome_28 with Dissolve(0.3)
    may 13 "（他大概也觉得尴尬吧……）" with Dissolve(0.3)
    may 13 "（我们以后还能对视吗？）"
    
    play sound2 door_creaking_1 volume 0.5
    
    scene nighthome_29 with Dissolve(0.3)
    pause 1.5
    scene nighthome_30 with Dissolve(0.3)
    may 13 "[gg]？" with Dissolve(0.3)
    scene nighthome_31 with Dissolve(0.3)
    gg 15 "你没事吧？" with Dissolve(0.3)
    scene nighthome_32 with Dissolve(0.3)
    may 13 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene nighthome_33 with Dissolve(0.3)
    may 13 "你能……先出去一下吗？" with Dissolve(0.3)
    scene nighthome_34 with Dissolve(0.3)
    gg 15 "现在不行。" with Dissolve(0.3)
    scene nighthome_35 with Dissolve(0.3)
    may 13 "我……感觉糟透了。而且我以为……我以为你现在会怎么看我。" with Dissolve(0.3)
    scene nighthome_36 with Dissolve(0.3)
    gg 15 "别想太多。过来坐下。我们得谈谈。" with Dissolve(0.3)
    
    scene black with Dissolve(0.5)
    pause 0.3
    
    scene nighthome_37 with Dissolve(0.5)
    gg 15 "你对刚才发生的事心里过不去，对吧？" with Dissolve(0.3)
    scene nighthome_38 with Dissolve(0.3)
    may 13 "嗯。" with Dissolve(0.3)
    scene nighthome_39 with Dissolve(0.3)
    gg 15 "你还记得全部经过吗？" with Dissolve(0.3)
    scene nighthome_40 with Dissolve(0.3)
    may 13 "差不多都记得。" with Dissolve(0.3)
    scene nighthome_41 with Dissolve(0.3)
    gg 15 "好。你还记得我在车上跟你说的吗？" with Dissolve(0.3)
    
    scene black with Dissolve(0.5)
    pause 0.5
    scene outside_night2_gohome_20 with Dissolve(0.3)
    gg 12 "我那个混蛋师父以为我忘加了一种重要配料。" with Dissolve(0.3)
    scene outside_night2_gohome_21 with Dissolve(0.3)
    gg 12 "你刚才那杯酒里本来有我倒进杯子之前就已经去掉的某种东西。" with Dissolve(0.3)
    gg 12 "所以你现在说的任何话，我都不会当真，[may]。"
    scene outside_night2_gohome_22 with Dissolve(0.3)
    gg 12 "我觉得等你清醒过来……应该不会真的记得。" with Dissolve(0.3)
    gg 12 "但你不必为刚才发生的事感到羞耻。我会理解的。"
    
    scene nighthome_42 with Dissolve(0.5)
    pause 1
    may 13 "我记得。虽然还是很难相信。" with Dissolve(0.3)
    scene nighthome_43 with Dissolve(0.3)
    gg 15 "只是想确认你的记忆没问题。" with Dissolve(0.3)
    scene nighthome_44 with Dissolve(0.3)
    may 13 "“我为自己昨晚的样子感到恶心。”" with Dissolve(0.3)
    scene nighthome_45 with Dissolve(0.3)
    gg 15 "“那是药物的作用。别怪自己。”" with Dissolve(0.3)
    scene nighthome_46 with Dissolve(0.3)
    may 13 "“都是你那份该死的工作害的！”" with Dissolve(0.3)
    scene nighthome_47 with Dissolve(0.3)
    may 13 "“你怎么能任由这种事发生？”" with Dissolve(0.3)
    scene nighthome_48 with Dissolve(0.3)
    may 13 "“你说只是喝杯鸡尾酒。我完全没想到你会给我下那种药……”" with Dissolve(0.3)
    scene nighthome_49 with Dissolve(0.3)
    may 13 "“我会不会上瘾啊？”" with Dissolve(0.3)
    scene nighthome_50 with Dissolve(0.3)
    gg 15 "“冷静点！”" with Dissolve(0.3)
    scene nighthome_51 with Dissolve(0.3)
    gg 15 "“我保证你会没事的。”" with Dissolve(0.3)
    scene nighthome_52 with Dissolve(0.3)
    may 13 "“拉钩！”" with Dissolve(0.3)
    scene nighthome_53 with Dissolve(0.3)
    gg 15 "“这么认真……”" with Dissolve(0.3)
    scene nighthome_54 with Dissolve(0.3)
    may 13 "“我等着呢！”" with Dissolve(0.3)
    scene nighthome_55 with Dissolve(0.3)
    ''
    scene nighthome_56 with Dissolve(0.3)
    gg 15 "（至少她满意了。）" with Dissolve(0.3)
    scene nighthome_57 with Dissolve(0.3)
    ''
    
    stop music fadeout 3
    
    scene black with Dissolve(1.0)
    pause 1
    
    play music2 mystery_revealed_loop fadein 5
    
    pause 1
    
    show nighthome_58 with Dissolve(0.2)
    $ renpy.pause (7, hard=True)
    
    scene nighthome_59 with Dissolve(0.3)
    "电视上正在播报一则突发新闻。"
    "主播出现在画面中，神情严峻而紧绷。"
    "背景播放着惨案的画面：破碎的店铺、闪烁的警灯、玻璃碎片，还有不知所措的围观者。"
    
    show nighthome_60 with Dissolve(0.2)
    newsanchor 1 "影滨市正经历一段艰难时期。" with Dissolve(0.3)
    newsanchor 1 "昨天的恐怖袭击造成多人死亡，再次威胁到市民的安全。"
    newsanchor 1 "当局报告有数十人受伤，但具体死亡人数尚未公布。"
    newsanchor 1 "初步调查显示，此次袭击的幕后是一个身份不明的犯罪团伙。"
    newsanchor 1 "调查人员正在排查其与不断升级的帮派冲突是否有关联。"
    show nighthome_61 with Dissolve(0.2)
    hide nighthome_60
    newsanchor 1 "提醒市民保持警惕，避免不必要的外出。" with Dissolve(0.3)
    "画面切到市长的声明。他站在市政厅外的讲台后，看似镇定，眼底却藏着明显的不安。"
    mayor 1 "近几个月来，犯罪率已攀升至危险水平。" with Dissolve(0.3)
    mayor 1 "“我们正在目睹暴力的升级，保护人民是我们的职责。”"
    mayor 1 "“从即刻起，我已下令加强警力部署并追加安全措施。”"
    "画面转向皆崎集团社长皆崎龙巳对记者讲话。"
    show nighthome_62 with Dissolve(0.2)
    hide nighthome_61
    tatsumi 1 "“我谨代表皆崎集团，向遇难者家属致以最深的慰问。”" with Dissolve(0.3)
    tatsumi 1 "“我们深知事态严重，承诺调动一切企业资源，协助恢复秩序。”"
    show nighthome_61 with Dissolve(0.2)
    hide nighthome_62
    "主播的语气变得低沉，几乎带着不祥。"
    show nighthome_60 with Dissolve(0.2)
    hide nighthome_61
    newsanchor 1 "有目击者称，在犯罪现场看到了拥有他们所称的「超人能力」的人。" with Dissolve(0.3)
    newsanchor 1 "目前还没有官方证实。"
    newsanchor 1 "但真相，或许只有那些再也无法开口的人知道。"
    show nighthome_61 with Dissolve(0.2)
    hide nighthome_60
    "画面回到演播室。沉重的沉默持续片刻后，切到了下一则新闻。"
    
    scene nighthome_63 with Dissolve(0.5)
    pause 0.5
    gg 15 "（信徒……恶魔……这不是随机的暴力事件。）" with Dissolve(0.3)
    scene nighthome_64 with Dissolve(0.3)
    gg 15 "（这一切一直在酝酿，很快就会失控。）" with Dissolve(0.3)
    scene nighthome_65 with Dissolve(0.3)
    gg 15 "（在我把事情拼凑完整之前，还会死多少人？）" with Dissolve(0.3)
    gg 15 "（我不该带她来的。但如果不是[may]，还能是谁呢……）"
    scene nighthome_66 with Dissolve(0.3)
    gg 15 "（可恶，我太急了……）" with Dissolve(0.3)
    gg 15 "（不过……也不算全无收获。我拿到这个了。）"
    scene nighthome_67 with Dissolve(0.3)
    gg 15 "（他们大概已经发现少了东西，尤其是在[hayato]用在[may]酒里的那次之后。）" with Dissolve(0.3)
    gg 15 "（我要跟卡门有一场愉快的对话了……而且不会愉快。）"
    
    stop music2 fadeout 0.5
    $ renpy.music.set_volume(1, delay=1, channel=u'music3')
    play music3 living_the_good_life_main_full fadein 2
    play sound woosh2
    
    scene nighthome_68 with PushMove(0.1, 'pushleft')
    may 13 "嘿，你没睡吗？" with Dissolve(0.3)
    
    play sound woosh1
    
    scene nighthome_69 with PushMove(0.1, 'pushright')
    gg 15 "没能。" with Dissolve(0.3)
    scene nighthome_70 with Dissolve(0.3)
    may 13 "你干嘛坐这儿？" with Dissolve(0.3)
    scene nighthome_71 with Dissolve(0.3)
    may 13 "我们该准备了。" with Dissolve(0.3)
    scene nighthome_72 with Dissolve(0.3)
    gg 15 "我自己能应付，慢性子。还是你磨蹭了。" with Dissolve(0.3)
    
    play sound clothes_2
    
    pause 0.1
    scene nighthome_73 with Dissolve(0.3)
    pause 2
    scene nighthome_74 with Dissolve(0.3)
    gg 15 "你撑得住吗？" with Dissolve(0.3)
    scene nighthome_75 with Dissolve(0.3)
    may 13 "我……还好。" with Dissolve(0.3)
    scene nighthome_76 with Dissolve(0.3)
    may 13 "我只是想躲起来……躲开一切。也躲开你。" with Dissolve(0.3)
    scene nighthome_77 with Dissolve(0.3)
    gg 15 "我们什么时候开始不互相救场了？" with Dissolve(0.3)
    scene nighthome_78 with Dissolve(0.3)
    may 13 "尴尬的原因就是你。" with Dissolve(0.3)
    scene nighthome_79 with Dissolve(0.3)
    may 13 "还有，我刚想起来我们还得上学。" with Dissolve(0.3)
    scene nighthome_80 with Dissolve(0.3)
    gg 15 "睡了吗？" with Dissolve(0.3)
    scene nighthome_81 with Dissolve(0.3)
    may 13 "翻来覆去一整夜，脑子里全是……所有的事。" with Dissolve(0.3)
    scene nighthome_82 with Dissolve(0.3)
    gg 15 "饿吗？" with Dissolve(0.3)
    scene nighthome_83 with Dissolve(0.3)
    may 13 "还好。要我给你做点什么吗？" with Dissolve(0.3)
    scene nighthome_84 with Dissolve(0.3)
    gg 15 "不用。专心考试吧。" with Dissolve(0.3)
    
    stop music3 fadeout 4
    
    scene black with Dissolve(1.0)
    pause 2
    
    $ renpy.music.set_volume(1, delay=2, channel=u'music3')
    play sound4 traffic_asian_metropolis_of_manila_loop loop fadein 2 volume 0.4
    
    pause 1
    
    scene nighthome_85 with Dissolve(0.5)
    pause 0.3
    gg 3 "（她今天安静得反常。）" with Dissolve(0.3)
    gg 3 "（平时她一定会唠叨要买什么可爱的家居装饰……）"
    gg 3 "（或者因为没陪她看而落下的动画……）"
    gg 3 "（或者她喜欢的那些女孩子气的东西……）"
    gg 3 "（但今天——一言不发。）"
    gg 3 "快到学校了。"
    
    stop sound4 fadeout 5
    play music2 the_old_carpenter_main_full fadein 2
    
    scene nighthome_87 with Dissolve(0.3)
    may 14 "嗯。" with Dissolve(0.3)
    scene nighthome_86 with Dissolve(0.3)
    gg 3 "你今天很可爱。比如那个马尾。" with Dissolve(0.3)
    scene nighthome_88 with Dissolve(0.3)
    may 14 "才不可爱……昨晚的口红都没擦掉。" with Dissolve(0.3)
    scene nighthome_89 with Dissolve(0.3)
    gg 3 "喂，[may]，怎么了？一副没精神的样子。" with Dissolve(0.3)
    
    show nighthome_91 with Dissolve(0.5)
    may 14 "没什么……希望考试别太难。" with Dissolve(0.3)
    may 14 "你又不会吃力。"
    show nighthome_90 with Dissolve(0.5)
    hide nighthome_91
    gg 3 "你是说[iz]的答案吧，我可没用。" with Dissolve(0.3)
    show nighthome_92 with Dissolve(0.3)
    hide nighthome_90
    may 14 "那你还发？你知道我也不会作弊的。" with Dissolve(0.3)
    show nighthome_90 with Dissolve(0.3)
    hide nighthome_92
    gg 3 "你可能会紧张到脑子一片空白。" with Dissolve(0.3)
    show nighthome_92 with Dissolve(0.3)
    hide nighthome_90
    may 14 "就算那样。" with Dissolve(0.3)
    show nighthome_90 with Dissolve(0.3)
    hide nighthome_92
    gg 3 "宁可挂科也不用卑鄙手段？" with Dissolve(0.3)
    show nighthome_92 with Dissolve(0.3)
    hide nighthome_90
    may 14 "显然。" with Dissolve(0.3)
    show nighthome_90 with Dissolve(0.3)
    hide nighthome_92
    gg 3 "要是这是生死考试呢？" with Dissolve(0.3)
    gg 3 "就像我们看的那部电影。你会赌吗？"
    show nighthome_92 with Dissolve(0.3)
    hide nighthome_90
    may 14 "就是那个考不及格就处决的那部？" with Dissolve(0.3)
    show nighthome_90 with Dissolve(0.3)
    hide nighthome_92
    gg 3 "对，就是那部《罗根》。" with Dissolve(0.3)
    show nighthome_92 with Dissolve(0.3)
    hide nighthome_90
    may 14 "我不知道……万一被抓到怎么办？" with Dissolve(0.3)
    show nighthome_90 with Dissolve(0.3)
    hide nighthome_92
    gg 3 "假设你把答案藏在没人会看的地方。你会这么做吗？" with Dissolve(0.3)
    show nighthome_92 with Dissolve(0.3)
    hide nighthome_90
    may 14 "要是命悬一线？绝对会。" with Dissolve(0.3)
    may 14 "可你能藏在哪儿呢？"
    show nighthome_90 with Dissolve(0.3)
    hide nighthome_92
    gg 3 "嗯……" with Dissolve(0.3)
    gg 3 "袖子不行。"
    gg 3 "被怀疑的话口袋会被搜。"
    gg 3 "我会把一张小抄塞进鞋里。"
    gg 3 "但你……"
    gg 3 "你有没有见过女生把纸条藏在衣服里的？完全不会引人怀疑。"
    show nighthome_92 with Dissolve(0.3)
    hide nighthome_90
    may 14 "不是。" with Dissolve(0.3)
    may 14 "给我看看？"
    
    scene nighthome_93 with Dissolve(0.3)
    pause 1.5
    scene nighthome_94 with Dissolve(0.3)
    pause 1
    scene nighthome_95 with Dissolve(0.3)
    gg 3 "简单。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.5, delay=0.5, channel=u'music2')
    play sound clothes_3 volume 2.0
    
    scene nighthome_96 with hpunch
    may 14 "啊！" with Dissolve(0.3)
    
    play sound2 grab_1 volume 2
    
    scene nighthome_97 with hpunch
    may 14 "喂，你干什——？！" with Dissolve(0.3)
    scene nighthome_98 with Dissolve(0.3)
    gg 3 "等一下，我做给你看。" with Dissolve(0.3)
    scene nighthome_99 with Dissolve(0.3)
    may 14 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene nighthome_100 with Dissolve(0.3)
    may 14 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene nighthome_101 with Dissolve(0.3)
    gg 3 "看好学了。" with Dissolve(0.3)
    scene nighthome_102 with Dissolve(0.3)
    gg 3 "方案一：把答案写在纸条上，用胶带贴在裙子内侧。" with Dissolve(0.3)
    gg 3 "经典做法。没人注意的时候瞄一眼裙摆。"
    scene nighthome_103 with Dissolve(0.3)
    gg 3 "给，帮我拿着。" with Dissolve(0.3)
    scene nighthome_104 with Dissolve(0.3)
    gg 3 "放松，[may]，没人会看到。" with Dissolve(0.3)
    scene nighthome_105 with Dissolve(0.3)
    gg 3 "方案二更好：把答案写在大腿上，撩起裙子看。" with Dissolve(0.3)
    gg 3 "隐蔽多了。"
    gg 3 "但纸会响，有风险。"
    scene nighthome_106 with Dissolve(0.3)
    gg 3 "有人会用胶带包起来，或者揉成团来消音。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=5, channel=u'music2')
    
    scene nighthome_107 with Dissolve(0.3)
    gg 3 "这样就没有声音，也不会在裙子下面闪出白纸。只有皮肤。" with Dissolve(0.3)
    scene nighthome_108 with Dissolve(0.3)
    gg 3 "没有哪个老师有胆量往那儿看。" with Dissolve(0.3)
    scene nighthome_109 with Dissolve(0.3)
    may 14 "但要是女老师怀疑作弊，那就另说了。" with Dissolve(0.3)
    scene nighthome_110 with Dissolve(0.3)
    gg 3 "我们学校有几个女老师来着？" with Dissolve(0.3)
    scene nighthome_111 with Dissolve(0.3)
    may 14 "呃……也对……不过我们的裙子太短，写不下多少。" with Dissolve(0.3)
    scene nighthome_112 with Dissolve(0.3)
    gg 3 "去找校长抗议吧。" with Dissolve(0.3)
    scene nighthome_113 with Dissolve(0.3)
    may 14 "所以……要是没准备，我们就死定了？" with Dissolve(0.3)
    scene nighthome_114 with Dissolve(0.3)
    gg 3 "跟那个老变态计划的一模一样。" with Dissolve(0.3)
    scene nighthome_115 with Dissolve(0.3)
    may 14 "哈？" with Dissolve(0.3)
    scene nighthome_116 with Dissolve(0.3)
    gg 3 "校长。" with Dissolve(0.3)
    scene nighthome_117 with Dissolve(0.3)
    may 14 "就因为裙子短？！" with Dissolve(0.3)
    scene nighthome_118 with Dissolve(0.3)
    gg 3 "没错。在一场你没法把答案藏在裙子底下的考试上赌命，唯一的出路是……" with Dissolve(0.3)
    scene nighthome_119 with Dissolve(0.3)
    may 14 "是……？" with Dissolve(0.3)
    scene nighthome_120 with Dissolve(0.3)
    gg 3 "成人片里女孩考不及格会怎么样？" with Dissolve(0.3)
    scene nighthome_121 with Dissolve(0.3)
    may 14 "你敢把那句话说完试试！" with Dissolve(0.3)
    scene nighthome_122 with Dissolve(0.3)
    gg 3 "校长赢。" with Dissolve(0.3)
    scene nighthome_123 with Dissolve(0.3)
    may 14 "你那种片子看太多了。" with Dissolve(0.3)
    scene nighthome_124 with Dissolve(0.3)
    gg 3 "还不是你害的？" with Dissolve(0.3)
    scene nighthome_125 with Dissolve(0.3)
    may 14 "别说了！我知道你要说什么！" with Dissolve(0.3)
    scene nighthome_126 with Dissolve(0.3)
    gg 3 "被我说中了吧。" with Dissolve(0.3)
    scene nighthome_127 with Dissolve(0.3)
    may 14 "我不知道是那种类型的动画！" with Dissolve(0.3)
    scene nighthome_128 with Dissolve(0.3)
    gg 3 "是啊，是啊。谁会请朋友来看里番片啊？" with Dissolve(0.3)
    scene nighthome_129 with Dissolve(0.3)
    may 14 "我们怎么就聊到这个了？！" with Dissolve(0.3)
    scene nighthome_130 with Dissolve(0.3)
    may 14 "从考试聊到电影，再聊到里番，再聊到作弊方法！" with Dissolve(0.3)
    scene nighthome_131 with Dissolve(0.3)
    may 14 "我们不聊这个！" with Dissolve(0.3)
    scene nighthome_132 with Dissolve(0.3)
    gg 3 "不过你已经不再为昨晚发愁了，对吧？" with Dissolve(0.3)
    scene nighthome_133 with Dissolve(0.3)
    may 14 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene nighthome_134 with Dissolve(0.3)
    may 14 "谢啦～" with Dissolve(0.3)
    
    stop music2 fadeout 4
    stop sound4 fadeout 2
    
    scene black with Dissolve(1.0)
    pause 2
    
    play sound4 schoolclassroombsy loop fadein 2
    
    pause 2

###### SCHOOL - LIS & Classmates

label schooltest:

    if chloe_saved == True:
        scene schooltest_1_chloe_saved with Dissolve(1.0)
        
    else:
        scene schooltest_1 with Dissolve(1.0)
        
    "教室里充满了紧绷的沉默，只有蓝色圆珠笔划过纸面的沙沙声打破寂静。"
    "学生们专注地填着答题卡，努力不被分心。"
    scene schooltest_2 with Dissolve(0.6)
    "不过这场考试看起来不算太难，紧张感却依然弥漫在空气里。"
    "有些人明显很紧张，浪费宝贵的时间拼命回想背过的内容。"
    scene schooltest_3 with Dissolve(0.5)
    "但另一些人看上去就自信得多。"
    "很明显，有些人正在对照前一天出现在班级群里的那份文件核对答案。"
    scene schooltest_4 with Dissolve(0.4)
    "答案填得飞快，好像几乎没人停下来想过这些答案是从哪来的。"
    scene schooltest_5 with Dissolve(0.3)
    "[mi]环视教室，但看她平静的表情，显然没有抓作弊者的打算。"
    
    if chloe_saved == True and chloe_date_bar == True:
        scene schooltest_6 with Dissolve(0.3)
        "克洛伊那晚去酒吧赴约了……虽然最后根本没见成面，却似乎救了她一命。"
        "也许还不算全完。还有机会解释清楚，再约她一次吗？"
        
    elif chloe_saved == True and chloe_date_fake == True:
        scene schooltest_6 with Dissolve(0.3)
        "克洛伊来到了约定的地点……但我们谁也没见到，最后她回了家。"
        "这救了她的命，但之后她大概再也不会答应约会了。"
        
    elif chloe_saved == True and chloe_date_bar == False and chloe_date_fake == False:
        scene schooltest_6 with Dissolve(0.3)
        "克洛伊活了下来。那晚她本来该跟朋友出去，但她显然没有去。"
        "我救了她的命——虽然她永远不会知道。"
    else:
        pause 0.1
        
    if chloe_saved == True:
        scene schooltest_7_chloe_saved with Dissolve(0.3)
        
    else:
        scene schooltest_7 with Dissolve(0.3)
        
    "时间过去。已经答完题的人如释重负地靠在椅背上。"
    "但大多数人还伏在卷子上，赶在老师宣布考试结束前拼命补救最后写错的地方。"
    
    stop sound4 fadeout 4
    play music3 funny_20 fadein 2
    
    scene schooltest_8 with Dissolve(0.3)
    me 1 "嘘，[dai]，你写完了吗？" with Dissolve(0.3)
    scene schooltest_9 with Dissolve(0.3)
    dai 1 "写完了一会儿了。" with Dissolve(0.3)
    scene schooltest_10 with Dissolve(0.3)
    me 1 "我手机没电了……没法对答案。" with Dissolve(0.3)
    scene schooltest_11 with Dissolve(0.3)
    me 1 "冷战到底是打什么？" with Dissolve(0.3)
    dai 1 "经济竞争。" with Dissolve(0.3)
    scene schooltest_12 with Dissolve(0.3)
    me 1 "经济竞争……" with Dissolve(0.3)
    scene schooltest_13 with Dissolve(0.3)
    me 1 "你确定？" with Dissolve(0.3)
    scene schooltest_14 with Dissolve(0.3)
    me 1 "我记的是政治和意识形态的对抗。" with Dissolve(0.3)
    scene schooltest_15 with Dissolve(0.3)
    dai 1 "我填的「D」。" with Dissolve(0.3)
    scene schooltest_16 with Dissolve(0.3)
    me 1 "好吧，随便……" with Dissolve(0.3)
    play sound penwrite_bw
    scene schooltest_17 with Dissolve(0.3)
    me 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene schooltest_18 with Dissolve(0.3)
    me 1 "最后三道历史题你填了什么？" with Dissolve(0.3)
    dai 1 "全是「D」。" with Dissolve(0.3)
    me 1 "等等，三道都是「D」？" with Dissolve(0.3)
    dai 1 "嗯。" with Dissolve(0.3)
    scene schooltest_19 with Dissolve(0.3)
    me 1 "开什么玩笑！" with Dissolve(0.3)
    scene schooltest_20 with Dissolve(0.3)
    me 1 "第20题：哪个国家第一个把人送上月球？" with Dissolve(0.3)
    scene schooltest_21 with Dissolve(0.3)
    me 1 "你真填了英国？" with Dissolve(0.3)
    scene schooltest_15 with Dissolve(0.3)
    dai 1 "是。" with Dissolve(0.3)
    scene schooltest_18 with Dissolve(0.3)
    me 1 "尼尔·阿姆斯特朗和巴兹·奥尔德林都是美国人，白痴。" with Dissolve(0.3)
    me 1 "还有第18题——你真填了尼基塔·赫鲁晓夫？"
    dai 1 "是。" with Dissolve(0.3)
    scene schooltest_16 with Dissolve(0.3)
    me 1 "这完全胡扯……你到底从哪儿看来的？" with Dissolve(0.3)
    scene schooltest_21 with Dissolve(0.3)
    me 1 "让我看看你的答题卡。" with Dissolve(0.3)
    scene schooltest_22 with Dissolve(0.3)
    dai 1 "给！" with Dissolve(0.3)
    
    play sound as1 volume 0.6
    
    scene schooltest_23 with Dissolve(0.3)
    ''
    scene schooltest_24 with Dissolve(0.3)
    me 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene schooltest_25 with Dissolve(0.3)
    me 1 "[dai]，你没救了。" with Dissolve(0.3)
    scene schooltest_26 with Dissolve(0.3)
    mi 5 "时间到。把答题卡传到前面。" with Dissolve(0.3)
    
    stop music3 fadeout 1
    
    scene black with Dissolve(0.5)
    pause 1
    
    play music2 sneaky_dramedy_loop fadein 2
    
    scene schooltest_27 with Dissolve(0.3)
    sotaro 1 "你觉得大家都考满分了吗？" with Dissolve(0.3)
    scene schooltest_28 with Dissolve(0.3)
    takeo 1 "别人不好说，但我故意错了几道，免得看起来太可疑。" with Dissolve(0.3)
    scene schooltest_29 with Dissolve(0.3)
    sotaro 1 "我全部原封不动抄的。想看看她对答案时我的表情吗？" with Dissolve(0.3)
    scene schooltest_30 with Dissolve(0.3)
    takeo 1 "你真觉得她会相信是你自己做出来的？" with Dissolve(0.3)
    scene schooltest_31 with Dissolve(0.3)
    sotaro 1 "男人就不能偶尔拿一次满分，换换花样？" with Dissolve(0.3)
    scene schooltest_32 with Dissolve(0.3)
    takeo 1 "喂，这里面根本不看分数！" with Dissolve(0.3)
    scene schooltest_33 with Dissolve(0.3)
    takeo 1 "这考的是你真正的知识，白痴。这些成绩不计入期末。" with Dissolve(0.3)
    scene schooltest_34 with Dissolve(0.3)
    sotaro 1 "但可能会影响我们的学期评定！" with Dissolve(0.3)
    scene schooltest_35 with Dissolve(0.3)
    takeo 1 "那上了大学你靠 假分数怎么办？继续作弊？" with Dissolve(0.3)
    scene schooltest_36 with Dissolve(0.3)
    sotaro 1 "管我屁事。" with Dissolve(0.3)
    scene schooltest_37 with Dissolve(0.3)
    mi 5 "有意思……" with Dissolve(0.3)
    scene schooltest_38 with Dissolve(0.3)
    mi 5 "非常有意思……" with Dissolve(0.3)
    scene schooltest_39 with Dissolve(0.3)
    sotaro 1 "看，开始了。" with Dissolve(0.3)
    
    stop music2 fadeout 1
    $ renpy.music.set_volume(1, delay=0, channel=u'music3')
    play music3 mystery_revealed_loop fadein 5
    
    show schooltest_40 with Dissolve(0.3)
    $ renpy.pause (4.3, hard=True)
    show schooltest_41 with Dissolve(0.3)
    hide schooltest_40
    mi 5 "那么。我们可就相当棘手了。" with Dissolve(0.3)
    mi 5 "几乎每个学生都在这场考试里拿了九十分以上。"
    mi 5 "这可能意味着一件事——或者另一种可能。第一，全班同学突然都变成了模范学生，把内容掌握得滴水不漏。"
    mi 5 "那对你们来说是好事，也会让我作为老师感到骄傲……"
    mi 5 "但遗憾的是，现实并不总给最理想的情况留位置。"
    mi 5 "那就只剩下另一种可能：每个学生不知怎么都提前拿到了答案。"
    
    scene schooltest_42 with Dissolve(0.3)
    "教室凝固了，紧张感在空气中变得黏稠。"
    scene schooltest_43 with Dissolve(0.3)
    "[mi]的目光毫不动摇地扫过每一个学生。"
    scene schooltest_44 with Dissolve(0.3)
    mi 5 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene schooltest_45 with Dissolve(0.3)
    mi 5 "有没有人愿意证实一下我的第二个猜测？" with Dissolve(0.3)
    scene schooltest_46 with Dissolve(0.1)
    pause 0.2
    scene schooltest_45 with Dissolve(0.1)
    pause 0.2
    scene schooltest_46 with Dissolve(0.1)
    pause 0.2
    scene schooltest_45 with Dissolve(0.3)
    pause 1
    scene schooltest_47 with Dissolve(0.3)
    daniella 1 "是……全是[iz]干的，栗原老师！" with Dissolve(0.3)
    scene schooltest_48 with Dissolve(0.3)
    reina 1 "对！她昨天在班级群里把答案发给我们了！" with Dissolve(0.3)
    scene schooltest_49 with Dissolve(0.3)
    mi 5 "皆崎泉……这是很严重的指控，我很难相信……" with Dissolve(0.3)
    scene schooltest_50 with Dissolve(0.3)
    mi 5 "我们学校最优秀的学生之一？" with Dissolve(0.3)
    mi 5 "不可能。"
    scene schooltest_52 with Dissolve(0.3)
    kyoko 1 "栗原老师，是真的！" with Dissolve(0.3)
    scene schooltest_53 with Dissolve(0.3)
    kyoko 1 "我可以给您看聊天记录。您想看吗？" with Dissolve(0.3)
    scene schooltest_51 with Dissolve(0.3)
    "[mi]几乎掩饰不住失望，神情凝重地点了点头。" with Dissolve(0.3)
    scene schooltest_54 with Dissolve(0.3)
    "[kyoko]把手机屏幕亮给众人看，上面是[iz]发答案文件的班级群聊。" with Dissolve(0.3)
    scene schooltest_55 with Dissolve(0.3)
    "[mi]深吸一口气，闭了闭眼让自己镇定下来。" with Dissolve(0.3)
    scene schooltest_56 with Dissolve(0.3)
    mi 5 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene schooltest_57 with Dissolve(0.3)
    mi 5 "考试结束。所有人离开教室。" with Dissolve(0.3)
    scene schooltest_58 with Dissolve(0.3)
    mi 5 "除了[iz]和[kyoko]。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.4, delay=0.5, channel=u'music3')
    scene black with Dissolve(0.5)
    
    $ renpy.music.set_volume(1, delay=1, channel=u'music3')
    
    pause 1
    
    scene schooltest_59 with Dissolve(0.3)
    "几分钟后教室空了——交完卷的学生匆匆离开。"
    scene schooltest_60 with Dissolve(0.3)
    "只剩下[iz]、[li]、[leah]、[ken]和[kyoko]，后者满怀期待地看着美波。"
    scene schooltest_61 with Dissolve(0.3)
    "气氛越来越紧张。"
    scene schooltest_62 with Dissolve(0.3)
    mi 5 "那条消息确实是从[iz]的账号发出的。" with Dissolve(0.3)
    scene schooltest_63 with Dissolve(0.3)
    mi 5 "[iz]，你能解释一下吗？" with Dissolve(0.3)
    scene schooltest_64 with Dissolve(0.3)
    iz 3 "不是我。" with Dissolve(0.3)
    scene schooltest_65 with Dissolve(0.3)
    kyoko 1 "栗原老师，您自己也看到了。" with Dissolve(0.3)
    scene schooltest_66 with Dissolve(0.3)
    mi 5 "谢谢你，[kyoko]。你可以走了。" with Dissolve(0.3)
    
    play sound schooldoor
    stop music3 fadeout 2
    
    scene schooltest_67 with Dissolve(1.0)
    pause 0.7
    scene schooltest_68 with Dissolve(0.2)
    pause 0.6
    
    play music2 tutorial_looped fadein 5
    
    scene schooltest_69 with Dissolve(0.3)
    mi 5 "那么……现在可以说说你要告诉我什么了吗？" with Dissolve(0.3)
    scene schooltest_70 with Dissolve(0.3)
    mi 5 "而我应该说过，只有[iz]可以留在教室里。你怎么还在？" with Dissolve(0.3)
    scene schooltest_71 with Dissolve(0.3)
    li 1 "问题是……真的不是[iz]。" with Dissolve(0.3)
    scene schooltest_72 with Dissolve(0.3)
    li 1 "你说吧，[leah]。" with Dissolve(0.3)
    scene schooltest_73 with Dissolve(0.3)
    leah 1 "是真的。" with Dissolve(0.3)
    scene schooltest_74 with Dissolve(0.3)
    "[iz]一言不发，紧紧抿着嘴唇。"
    "[mi]眯起眼睛，把视线转向男生们。"
    scene schooltest_75 with Dissolve(0.3)
    mi 5 "男生们，有什么要补充的吗？" with Dissolve(0.3)
    scene schooltest_76 with Dissolve(0.3)
    gg 3 "情况就跟她说的完全一样。" with Dissolve(0.3)
    scene schooltest_77 with Dissolve(0.3)
    gg 3 "消息是从[iz]的账号发出的。" with Dissolve(0.3)
    gg 3 "情况看起来很明白，但问题在于——她昨天手机不见了。"
    scene schooltest_78 with Dissolve(0.3)
    iz 3 "是被偷了！" with Dissolve(0.3)
    scene schooltest_79 with Dissolve(0.3)
    gg 3 "我们不知道那条消息到底是谁发的。" with Dissolve(0.3)
    scene schooltest_80 with Dissolve(0.3)
    mi 5 "你的意思是，有人发消息来陷害[iz]？" with Dissolve(0.3)
    scene schooltest_81 with Dissolve(0.3)
    gg 3 "很有可能。" with Dissolve(0.3)
    scene schooltest_82 with Dissolve(0.3)
    iz 3 "你怎么不去问问你朋友？" with Dissolve(0.3)
    scene schooltest_83 with Dissolve(0.3)
    iz 3 "也许他知道点什么？" with Dissolve(0.3)
    scene schooltest_84 with Dissolve(0.3)
    ken 1 "{cps=5}……{/cps}"
    scene schooltest_85 with Dissolve(0.3)
    ken 1 "我不方便跟她谈。能不能请她联系手机运营商？" with Dissolve(0.3)
    scene schooltest_86 with Dissolve(0.3)
    ken 1 "如果手机还开着，他们或许能定位。" with Dissolve(0.3)
    scene schooltest_87 with Dissolve(0.3)
    gg 3 "前提是SIM卡还没被丢掉。" with Dissolve(0.3)
    scene schooltest_88 with Dissolve(0.3)
    gg 3 "（不过，谁会费这么大劲去陷害一个女学生？）" with Dissolve(0.3)
    scene schooltest_89 with Dissolve(0.3)
    gg 3 "[iz]，你得联系运营商，报备手机丢失。" with Dissolve(0.3)
    scene schooltest_90 with Dissolve(0.3)
    gg 3 "他们能帮你停掉那个号码，也可能查到手机位置。" with Dissolve(0.3)
    scene schooltest_91 with Dissolve(0.3)
    iz 3 "我一看到那条消息就联系了。" with Dissolve(0.3)
    scene schooltest_92 with Dissolve(0.3)
    li 1 "运营商真的会提供这种信息吗？" with Dissolve(0.3)
    scene schooltest_93 with Dissolve(0.3)
    leah 1 "我想只有通过官方申请才行。" with Dissolve(0.3)
    scene schooltest_94 with Dissolve(0.3)
    mi 6 "没错。不过那种信息只提供给警方。" with Dissolve(0.3)
    scene schooltest_95 with Dissolve(0.3)
    mi 6 "没有正式申请，运营商不会交出数据。" with Dissolve(0.3)
    scene schooltest_96 with Dissolve(0.3)
    ken 1 "那我们只能去找警察了。这是唯一的办法，[iz]。" with Dissolve(0.3)
    scene schooltest_97 with Dissolve(0.3)
    li 1 "你不觉得现在最不该由你来说教的人就是我吗？" with Dissolve(0.3)
    scene schooltest_98 with Dissolve(0.3)
    ken 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene schooltest_99 with Dissolve(0.3)
    pause 2
    scene schooltest_100 with Dissolve(0.3)
    pause 1.5
    scene schooltest_101 with Dissolve(0.3)
    mi 6 "这是什么意思？" with Dissolve(0.3)
    scene schooltest_102 with Dissolve(0.3)
    li 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene schooltest_103 with Dissolve(0.3)
    gg 3 "没必要把他牵扯进来。" with Dissolve(0.3)
    scene schooltest_104 with Dissolve(0.3)
    gg 3 "[ken]跟这事无关。" with Dissolve(0.3)
    scene schooltest_105 with Dissolve(0.3)
    mi 6 "你在瞒着我什么吗？" with Dissolve(0.3)
    scene schooltest_106 with Dissolve(0.3)
    gg 3 "[iz]手机不见，只是问题的一部分。" with Dissolve(0.3)
    scene schooltest_107 with Dissolve(0.3)
    gg 3 "昨天有人想陷害[ken]，让所有人都以为是他干的。" with Dissolve(0.3)
    scene schooltest_108 with Dissolve(0.3)
    gg 3 "不管这个人是谁，他已经同时毁了[ken]泉的名誉。" with Dissolve(0.3)
    scene schooltest_109 with Dissolve(0.3)
    iz 3 "所以你的建议是？" with Dissolve(0.3)
    scene schooltest_110 with Dissolve(0.3)
    gg 3 "用你的家族。" with Dissolve(0.3)
    scene schooltest_111 with Dissolve(0.3)
    iz 3 "什么？" with Dissolve(0.3)
    scene schooltest_112 with Dissolve(0.3)
    gg 3 "动用你家族的影响力。" with Dissolve(0.3)
    scene schooltest_113 with Dissolve(0.3)
    iz 3 "你在开玩笑吧。" with Dissolve(0.3)
    scene schooltest_114 with Dissolve(0.3)
    iz 3 "难道我家族是什么魔法咒语，念一下就能解决一切？" with Dissolve(0.3)
    scene schooltest_115 with Dissolve(0.3)
    gg 3 "如果你不愿意为正义动用家族的名声，那你祖父当年的辛劳是为了什么？" with Dissolve(0.3)
    scene schooltest_116 with Dissolve(0.3)
    iz 3 "那不是我的成就。" with Dissolve(0.3)
    scene schooltest_117 with Dissolve(0.3)
    gg 3 "但手机是你的。" with Dissolve(0.3)
    scene schooltest_118 with Dissolve(0.3)
    li 1 "在这种情况下，那是有正当理由的。" with Dissolve(0.3)
    scene schooltest_119 with Dissolve(0.3)
    iz 3 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene schooltest_120 with Dissolve(0.3)
    iz 3 "我不想为这种小事去麻烦祖父。" with Dissolve(0.3)
    scene schooltest_121 with Dissolve(0.3)
    gg 3 "其实你未必需要麻烦他。" with Dissolve(0.3)
    scene schooltest_122 with Dissolve(0.3)
    li 1 "等等，真的吗？" with Dissolve(0.3)
    scene schooltest_123 with Dissolve(0.3)
    li 1 "那我们怎么解决？" with Dissolve(0.3)
    scene schooltest_124 with Dissolve(0.3)
    gg 3 "我想你能猜到吧，[iz]？" with Dissolve(0.3)
    scene schooltest_125 with Dissolve(0.3)
    gg 3 "尤其要是放任不管，名誉受损的也会波及你祖父。" with Dissolve(0.3)
    scene schooltest_126 with Dissolve(0.3)
    iz 3 "呃，我就知道迟早会这样。对，我想我知道你什么意思了。" with Dissolve(0.3)
    scene schooltest_127 with Dissolve(0.3)
    li 1 "那么，是什么？" with Dissolve(0.3)
    scene schooltest_128 with Dissolve(0.3)
    ken 1 "我还是不明白。" with Dissolve(0.3)
    
    stop music2 fadeout 4
    
    scene black with Dissolve(1.0)
    pause 2
    
    play sound3 heavy_dirty_traffic fadein 5
    
    pause 2
    
###### PAWNSHOP, STREET - MC, IZ
    
label izumipawnshop:

    show izpawnshop_1 with Dissolve(0.5)
    $ renpy.pause (4, hard=True)
    
    scene izpawnshop_2 with Dissolve(0.3)
    "周围的街道看起来灰暗——墙面剥落，人行道上堆着垃圾，稀疏的路灯投下昏黄的光。"
    "每走一步，回声都在震耳欲聋的寂静中荡开。这地方谈不上友善，但我们别无选择。"
    scene izpawnshop_3 with Dissolve(0.3)
    "[iz]走在我身边，视线不时落在我手机屏幕上——那个定位标记一动不动。"
    "越靠近，紧张感就越重。未知总是沉甸甸的。"
    scene izpawnshop_4 with Dissolve(0.3)
    "手机没动——这可能意味着任何事。也许它只是被丢在某个黑暗的角落。也许等着我们的是更大的东西。"
    scene izpawnshop_5 with Dissolve(0.3)
    iz 4 "不过运营商就这么把信息交出来，还是让我有点意外。" with Dissolve(0.3)
    scene izpawnshop_6 with Dissolve(0.3)
    iz 4 "我以为这通常得费一番周折。" with Dissolve(0.3)
    scene izpawnshop_7 with Dissolve(0.3)
    gg 16 "魔法在于提对那个人的姓。" with Dissolve(0.3)
    gg 16 "你家族享有的特权。用吧，但别拿它去伤害别人。"
    
    stop sound3 fadeout 10
    play music3 jazz_sneaker_loop fadein 2
    
    scene black with Dissolve(0.3)
    pause 0.3
    
    $ izumi_unlock = True
    show screen rel_open_izumi
    show izpawnshop_10 with Dissolve(0.3)
    iz 4 "相信我，我知道皆崎这个姓氏有多大能耐。别以为能靠它吓到我。" with Dissolve(0.3)
    show izpawnshop_8 with Dissolve(0.2)
    hide izpawnshop_10
    gg 16 "我根本没打算那么做。只是觉得这做法让人恶心。" with Dissolve(0.3)
    show izpawnshop_9 with Dissolve(0.2)
    hide izpawnshop_8
    iz 4 "太轻松了，而且不公平。" with Dissolve(0.3)
    iz 4 "换成别人的重要东西被偷，多半会一直拖着，被排在后面。"
    iz 4 "只是一部手机——警察局里谁会费心管这个？"
    iz 4 "为什么什么事都要靠关系？"
    show izpawnshop_8 with Dissolve(0.2)
    hide izpawnshop_9
    gg 16 "关系……或者有本事的朋友。" with Dissolve(0.3)
    show izpawnshop_13 with Dissolve(0.2)
    hide izpawnshop_8
    iz 4 "哦？现在你有本事了？" with Dissolve(0.3)
    show izpawnshop_11 with Dissolve(0.2)
    hide izpawnshop_13
    gg 16 "至少我够聪明，能看出[ken]在这里没责任。" with Dissolve(0.3)
    show izpawnshop_10 with Dissolve(0.2)
    hide izpawnshop_11
    iz 4 "哎呀，拜托！" with Dissolve(0.3)
    iz 4 "我的东西在他储物柜里。这不是铁证是什么？"
    show izpawnshop_8 with Dissolve(0.2)
    hide izpawnshop_10
    gg 16 "就像那条从你账号发到班级群里的消息一样。" with Dissolve(0.3)
    gg 16 "[iz]，显然有人想让你以为是[ken]干的。"
    show izpawnshop_12 with Dissolve(0.2)
    hide izpawnshop_8
    iz 4 "我也考虑过这种可能——看起来确实像陷害。" with Dissolve(0.3)
    iz 4 "但万一不是呢？你凭什么这么确定？"
    show izpawnshop_11 with Dissolve(0.2)
    hide izpawnshop_12
    gg 16 "直觉。" with Dissolve(0.3)
    show izpawnshop_13 with Dissolve(0.2)
    hide izpawnshop_11
    iz 4 "他是你朋友，我明白。但那他为什么连一句辩解都不说？" with Dissolve(0.3)
    show izpawnshop_9 with Dissolve(0.2)
    hide izpawnshop_13
    iz 4 "哪怕一句也好，我很乐意听。" with Dissolve(0.3)
    show izpawnshop_8 with Dissolve(0.2)
    hide izpawnshop_9
    gg 16 "有时候说了也没用。" with Dissolve(0.3)
    gg 16 "你知道吗，也许他觉得反正也没人会信他。"
    show izpawnshop_10 with Dissolve(0.2)
    hide izpawnshop_8
    iz 4 "别觉得你朋友完全无辜。" with Dissolve(0.3)
    iz 4 "他当男生简直是无可救药。总是毫无理由找茬，主动去招惹那帮人，却又打不回来。"
    show izpawnshop_9 with Dissolve(0.2)
    hide izpawnshop_10
    iz 4 "而且被打完之后，下次还要回来装这副「不屈不挠」的样子——然后再被打一次。" with Dissolve(0.3)
    iz 4 "有时候他会毫无预兆地先动手，一个人冲进一整群人里。"
    iz 4 "还有他那个眼神……"
    show izpawnshop_12 with Dissolve(0.2)
    hide izpawnshop_9
    iz 4 "可恶，我真的想相信不是他，也希望不是。" with Dissolve(0.3)
    iz 4 "但想到他那些古怪的行径，我没法确定。"
    iz 4 "真不敢相信你居然答应了这个。"
    iz 4 "你不会真以为我会特别感激你吧？"
    show izpawnshop_11 with Dissolve(0.2)
    hide izpawnshop_12
    gg 16 "我来是因为美波拜托我，可不是出于对你的私人同情。" with Dissolve(0.3)
    show izpawnshop_13 with Dissolve(0.2)
    hide izpawnshop_11
    iz 4 "噗。哇，好有骑士精神啊！" with Dissolve(0.3)
    iz 4 "所以你帮我纯粹是为了她？"
    show izpawnshop_14 with Dissolve(0.2)
    hide izpawnshop_13
    gg 16 "很高兴我们达成共识。" with Dissolve(0.3)
    gg 16 "少点火气，我们就能更快找到你的手机。"
    show izpawnshop_10 with Dissolve(0.2)
    hide izpawnshop_14
    iz 4 "注意你的语气。" with Dissolve(0.3)
    iz 4 "她也跟我说了，说你会护送我去。"
    show izpawnshop_8 with Dissolve(0.2)
    hide izpawnshop_10
    gg 16 "我还以为是你自愿选的我。" with Dissolve(0.3)
    show izpawnshop_13 with Dissolve(0.2)
    hide izpawnshop_8
    iz 4 "你对现实的理解明显膨胀得离谱。" with Dissolve(0.3)
    show izpawnshop_11 with Dissolve(0.2)
    hide izpawnshop_13
    gg 16 "或者说你对朋友的标准高得不切实际。" with Dissolve(0.3)
    show izpawnshop_10 with Dissolve(0.2)
    hide izpawnshop_11
    iz 4 "在你一个所谓「朋友」偷了我东西之后，这要求完全合理。" with Dissolve(0.3)
    show izpawnshop_8 with Dissolve(0.2)
    hide izpawnshop_10
    gg 16 "即使我现在正在帮你找它？" with Dissolve(0.3)
    show izpawnshop_10 with Dissolve(0.2)
    hide izpawnshop_8
    iz 4 "因为老师拜托你了。而且是为了帮你朋友。" with Dissolve(0.3)
    iz 4 "要是换成你自己，我怀疑你对他不会这么宽容。"
    show izpawnshop_8 with Dissolve(0.2)
    hide izpawnshop_10
    gg 16 "那我还真是走运，不在你那个位置上。" with Dissolve(0.3)
    gg 16 "我只是想说——如果被怀疑的是我，我会希望有个冷静的人来处理。"
    show izpawnshop_13 with Dissolve(0.2)
    hide izpawnshop_8
    iz 4 "你在明着暗示我该冷静点？" with Dissolve(0.3)
    show izpawnshop_11 with Dissolve(0.2)
    hide izpawnshop_13
    gg 16 "哪敢想！那是夸奖。" with Dissolve(0.3)
    gg 16 "而且我当然是在讨好一位人脉很广的人。"
    show izpawnshop_8 with Dissolve(0.2)
    hide izpawnshop_11
    gg 16 "我把话说得这么坦白，就是让你知道我百分之百认真诚实。" with Dissolve(0.3)
    gg 16 "顺便说一句，这也是一种操控。"
    show izpawnshop_10 with Dissolve(0.2)
    hide izpawnshop_8
    iz 4 "显然……" with Dissolve(0.3)
    iz 4 "随便吧。到了吗？"
    iz 4 "赶紧办完算了。"
    
    scene izpawnshop_15 with Dissolve(0.3)
    gg 16 "快到了。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.5, delay=2, channel=u'music3')
    play sound3 heavy_dirty_traffic fadein 3 volume 0.5
    
    scene izpawnshop_16 with Dissolve(0.3)
    pause 2
    scene izpawnshop_17 with Dissolve(0.3)
    gg 16 "你在这儿走路不害怕吗？" with Dissolve(0.3)
    scene izpawnshop_18 with Dissolve(0.3)
    iz 4 "我有什么好怕的？" with Dissolve(0.3)
    scene izpawnshop_19 with Dissolve(0.3)
    gg 16 "破败的街区，昏暗的灯光，恶心难闻的气味——还能有更糟的？" with Dissolve(0.3)
    scene izpawnshop_20 with Dissolve(0.3)
    iz 4 "被人背叛信任吗？" with Dissolve(0.3)
    iz 4 "不过现在我还得信任你这样的人，走过这些闷臭的小巷。"
    scene izpawnshop_21 with Dissolve(0.3)
    pause 1
    gg 16 "到了。就是这扇门，就在我们面前。" with Dissolve(0.3)
    pause 1.5
    
    stop music3 fadeout 3
    stop sound3 fadeout 3
    
    scene black with Dissolve(1.0)
    pause 2
    
### PAWNSHOP

    play sound2 broken_ventilation_system_loop_1 loop fadein 2 volume 0.3
    
    scene izpawnshop_22 with Dissolve(1.0)
    "我们沿着狭窄的楼梯往下走，地下室里空气沉甸甸的，充满潮湿和陈旧金属的刺鼻气味。"
    scene izpawnshop_23 with Dissolve(0.3)
    "裸露的砖墙没有任何粉饰，只有吊灯投下昏暗的光。"
    scene izpawnshop_24 with Dissolve(0.3)
    "那点光几乎穿不透乱七八糟堆着的杂物。"
    
    $ renpy.music.set_volume(0, delay=0, channel=u'sound4')
    $ renpy.music.set_volume(1, delay=1, channel=u'sound5')
    play sound4 male_snoring_lp loop
    play sound5 male_snoring_lp_lowpass loop
    
    scene izpawnshop_25 with Dissolve(0.3)
    "楼梯边的椅子上，一个胖守卫在睡梦中摇晃。"
    
    $ renpy.music.set_volume(1, delay=0.5, channel=u'sound4')
    $ renpy.music.set_volume(0, delay=0.5, channel=u'sound5')
    
    scene izpawnshop_26 with Dissolve(0.3)
    "他的呼吸沉重而均匀，仿佛根本不在乎周围的一切。"
    
    $ renpy.music.set_volume(0, delay=0.5, channel=u'sound4')
    $ renpy.music.set_volume(1, delay=0.5, channel=u'sound5')
    
    scene izpawnshop_27 with Dissolve(0.3)
    "积满灰尘的柜台后面，女店员心不在焉地刷着手机。显然没料到会有客人。"
    
    stop sound2 fadeout 10
    stop sound4 fadeout 5
    stop sound5 fadeout 5
    play music2 mysterious_tango_loop fadein 2
    
    scene izpawnshop_28 with Dissolve(0.3)
    gg 16 "晚上好。我看你们在展示手机——能买一台吗？" with Dissolve(0.3)
    scene izpawnshop_29 with Dissolve(0.3)
    psclerk 1 "当然，我们款式很齐全。您对哪个型号感兴趣？" with Dissolve(0.3)
    scene izpawnshop_30 with Dissolve(0.3)
    "[iz]的视线锁在了玻璃柜台后面的某样东西上。"
    scene izpawnshop_31 with Dissolve(0.3)
    "她僵住了，手指攥成拳头。"
    scene izpawnshop_32 with Dissolve(0.3)
    "顺着她的视线，我立刻明白了原因——那些胡乱摆放的手机中间躺着一台蓝色智能手机。"
    scene izpawnshop_33 with Dissolve(0.3)
    gg 16 "（跟她的一模一样。巧合？不太可能。看来我们的猜测没错。）" with Dissolve(0.3)
    scene izpawnshop_34 with Dissolve(0.3)
    gg 16 "这台多少钱？" with Dissolve(0.3)
    scene izpawnshop_35 with Dissolve(0.3)
    psclerk 1 "蓝色的这台？" with Dissolve(0.3)
    scene izpawnshop_36 with Dissolve(0.3)
    psclerk 1 "一千四百美元。" with Dissolve(0.3)
    scene izpawnshop_37 with Dissolve(0.3)
    gg 16 "这基本算是新机的价格了。" with Dissolve(0.3)
    scene izpawnshop_38 with Dissolve(0.3)
    psclerk 1 "可它基本就是新的。" with Dissolve(0.3)
    scene izpawnshop_39 with Dissolve(0.3)
    psclerk 1 "独家型号，蓝色，1TB 存储。现在这种要卖两倍价钱。" with Dissolve(0.3)
    scene izpawnshop_40 with Dissolve(0.3)
    psclerk 1 "连一道划痕都没有。" with Dissolve(0.3)
    scene izpawnshop_41 with Dissolve(0.3)
    psclerk 1 "没有原盒，不过我们可以送你一根全新的原装充电线。" with Dissolve(0.3)
    scene izpawnshop_42 with Dissolve(0.3)
    "我看了[iz]一眼——她正仔细端详着展示柜里的手机。"
    scene izpawnshop_43 with Dissolve(0.3)
    "她犹豫了一瞬，我们目光相遇。"
    scene izpawnshop_44 with Dissolve(0.3)
    "她不悦地眯起眼睛——不用一句话意思就很清楚。这局面让她恼火，但已经没有回头路了。"
    scene izpawnshop_45 with Dissolve(0.3)
    "我默默点头，示意她用智能手表应用发个信号。"
    scene izpawnshop_46 with Dissolve(0.3)
    "只要轻轻一点——也许附近就会响起一阵熟悉的声音。"
    scene izpawnshop_47 with Dissolve(0.3)
    gg 16 "（拜托，[iz]，动手吧。）" with Dissolve(0.3)
    
    play sound2 vibration_01 loop
    
    scene izpawnshop_48 with Dissolve(0.3)
    
    play sound3 scifi_pulse_vibrating loop volume 0.5
    
    "她眼睛没离开展示中的手机，抬手在表上点了一下，一秒后那台蓝色手机开始震动。"
    
    stop sound2 fadeout 0.3
    stop sound3 fadeout 1
    
    scene izpawnshop_49 with Dissolve(0.3)
    iz 4 "那绝对是我的手机。" with Dissolve(0.3)
    scene izpawnshop_50 with Dissolve(0.3)
    "店员察觉到震动，愣了一瞬，随即皱起眉，用手把手机盖住。"
    scene izpawnshop_51 with Dissolve(0.3)
    gg 16 "看来你把一台偷来的手机摆出来卖。" with Dissolve(0.3)
    scene izpawnshop_52 with Dissolve(0.3)
    psclerk 1 "这台手机是按规定收来并检验过的。" with Dissolve(0.3)
    scene izpawnshop_53 with Dissolve(0.3)
    psclerk 1 "客人从哪儿弄到东西拿来卖，我们不负责。" with Dissolve(0.3)
    scene izpawnshop_54 with Dissolve(0.3)
    gg 16 "那就告诉我们是谁典当的。我们需要送来者的联系方式。" with Dissolve(0.3)
    scene izpawnshop_55 with Dissolve(0.3)
    psclerk 1 "抱歉，客户信息严格保密。" with Dissolve(0.3)
    scene izpawnshop_56 with Dissolve(0.3)
    psclerk 1 "不买东西的话，请离开。" with Dissolve(0.3)
    scene izpawnshop_57 with Dissolve(0.3)
    iz 4 "充电线我不要。真正的机主来了，能便宜点吗？" with Dissolve(0.3)
    scene izpawnshop_58 with Dissolve(0.3)
    psclerk 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene izpawnshop_59 with Dissolve(0.3)
    psclerk 1 "呃……我不清楚……" with Dissolve(0.3)
    scene izpawnshop_60 with Dissolve(0.3)
    psclerk 1 "这种情况从来没发生过，真是意外。" with Dissolve(0.3)
    scene izpawnshop_61 with Dissolve(0.3)
    iz 4 "我本来想着要花赏金赎回自己的手机，所以带了现金。" with Dissolve(0.3)
    scene izpawnshop_62 with Dissolve(0.3)
    iz 4 "我带了……" with Dissolve(0.3)
    scene izpawnshop_63 with Dissolve(0.3)
    iz 4 "一千二百七十块。" with Dissolve(0.3)
    iz 4 "能给我吗？"
    scene izpawnshop_64 with Dissolve(0.3)
    psclerk 1 "稍等，我去问一下……" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=0, channel=u'sound4')
    play sound4 male_snoring_lp
    
    scene izpawnshop_65 with Dissolve(0.3)
    pause 2
    
    stop sound4 fadeout 0.5
    
    scene izpawnshop_66 with Dissolve(0.3)
    pause 1
    scene izpawnshop_67 with Dissolve(0.3)
    psguard 1 "嗯？" with Dissolve(0.3)
    
    play sound5 creature_snore_right
    
    scene izpawnshop_68 with Dissolve(0.3)
    "她朝旁边那间屋子看了一眼，什么也没说。"
    
    stop sound5 fadeout 0.3
    
    scene izpawnshop_69 with Dissolve(0.3)
    psclerk 1 "好。这个价钱可以给你。" with Dissolve(0.3)
    scene izpawnshop_70 with Dissolve(0.3)
    psclerk 1 "给你。" with Dissolve(0.3)
    scene izpawnshop_71 with Dissolve(0.3)
    iz 4 "呃……谢谢……？" with Dissolve(0.3)
    scene izpawnshop_72 with Dissolve(0.5)
    pause 0.3
    gg 16 "（第一次见她对我笑……）" with Dissolve(0.3)
    scene izpawnshop_73 with Dissolve(0.3)
    gg 16 "（挺可爱的，但这种情况下我心情很复杂。）" with Dissolve(0.3)
    scene izpawnshop_74 with Dissolve(0.3)
    gg 16 "（整件事真是让人火大，但事实摆在这里：只有两条路——谈，或者硬来。）" with Dissolve(0.3)
    scene izpawnshop_75 with Dissolve(0.3)
    gg 16 "现在，讲点道理吧——把摄像头的录像给我们看。" with Dissolve(0.3)
    scene izpawnshop_76 with Dissolve(0.3)
    gg 16 "我想知道是谁把它送来的。" with Dissolve(0.3)
    scene izpawnshop_77 with Dissolve(0.3)
    psclerk 1 "我刚说了，客户信息严格保密。" with Dissolve(0.3)
    scene izpawnshop_78 with Dissolve(0.3)
    gg 16 "加钱也不行？" with Dissolve(0.3)
    scene izpawnshop_79 with Dissolve(0.3)
    psclerk 1 "这种出价……你最好去跟他说。" with Dissolve(0.3)
    
    stop music2 fadeout 10
    play sound3 broken_ventilation_system_loop_1 loop volume 0.3 fadein 3
    $ renpy.music.set_volume(1, delay=0, channel=u'sound4')
    $ renpy.music.set_volume(0, delay=0, channel=u'sound5')
    play sound4 male_snoring_lp loop
    play sound5 male_snoring_lp_lowpass loop
    
    scene izpawnshop_80 with Dissolve(0.3)
    psclerk 1 "我保证他能给你个解释。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0, delay=0.5, channel=u'sound4')
    $ renpy.music.set_volume(1, delay=0.5, channel=u'sound5')
    
    scene izpawnshop_81 with Dissolve(0.3)
    gg 16 "（我讨厌他们这套下作做派……）" with Dissolve(0.3)
    scene izpawnshop_82 with Dissolve(0.3)
    pause 0.5
    
    call screen izumi_pawnshop_choice_dom_sub

###### PAWNSHOP, IN - NEGOTITATION
    
label pawnshop_deal:
    
    stop sound3 fadeout 5
    stop sound4 fadeout 2
    stop sound5 fadeout 2
    play music3 dinner_party_main_full
    
    pause 0.3
    scene izpawnshop_83 with Dissolve(0.3)
    "那个守卫体格魁梧，显然习惯用暴力解决问题，懒洋洋地抬起眼。"
    scene izpawnshop_84 with Dissolve(0.3)
    "他脸上带着不悦——他已经意识到我们不是来买东西的。"
    
    play sound2 chairwood
    
    scene izpawnshop_85 with Dissolve(0.3)
    psguard 1 "不买东西的话，门在那边。" with Dissolve(0.3)
    scene izpawnshop_86 with Dissolve(0.3)
    gg 16 "我能看摄像头的录像吗？比如说，给点小费用让我们看一眼。" with Dissolve(0.3)
    scene izpawnshop_87 with Dissolve(0.3)
    "守卫嗤笑着，慢慢把我从头到脚打量了一遍。"
    scene izpawnshop_88 with Dissolve(0.3)
    psguard 1 "录像？你说「小」费用？" with Dissolve(0.3)
    scene izpawnshop_89 with Dissolve(0.3)
    iz 4 "他不会答应的。这里的人……都不是什么老实人。" with Dissolve(0.3)
    scene izpawnshop_90 with Dissolve(0.3)
    gg 16 "先从这部手机开始，怎么样？" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=0.5, channel=u'sound4')
    $ renpy.music.set_volume(1, delay=0.5, channel=u'sound5')
    play sound old_man_laughing
    
    scene izpawnshop_91 with Dissolve(0.3)
    psguard 1 "噗哈！就为这点风险，一百块？" with Dissolve(0.3)
    
    stop sound fadeout 0.5
    
    scene izpawnshop_92 with Dissolve(0.3)
    psguard 1 "小子，你傻吗？" with Dissolve(0.3)
    scene izpawnshop_93 with Dissolve(0.3)
    psguard 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene izpawnshop_94 with Dissolve(0.3)
    "他的视线停在泉身上，嘴角扯出一个得意的笑。"
    scene izpawnshop_95 with Dissolve(0.3)
    psguard 1 "哦，那可就不一样了……" with Dissolve(0.3)
    psguard 1 "真是个美人……"
    scene izpawnshop_96 with Dissolve(0.3)
    psguard 1 "要是你这位女朋友把耳环给我，我也许可以让你看录像。" with Dissolve(0.3)
    scene izpawnshop_97 with Dissolve(0.3)
    iz 4 "你认真的吗？拿我的耳环换一段录像文件？" with Dissolve(0.3)
    scene izpawnshop_98 with Dissolve(0.3)
    psguard 1 "要么耳环，要么五百现金。不然就滚。我这儿不是做慈善的。" with Dissolve(0.3)
    scene izpawnshop_99 with Dissolve(0.3)
    iz 4 "我没有更多现金了。" with Dissolve(0.3)
    scene izpawnshop_100 with Dissolve(0.3)
    pause 0.1
    menu:
        "付钱给他\\n[red](金钱 -400)[gold](泉 +1)":
                scene izpawnshop_101 with Dissolve(0.3)
                gg 16 "听着，五百太贵了。四百怎么样。" with Dissolve(0.3)
                scene izpawnshop_102 with Dissolve(0.3)
                
                play sound money_1
                
                gg 16 "现金，现在。" with Dissolve(0.3)
                scene izpawnshop_103 with Dissolve(0.3)
                psguard 1 "四百？" with Dissolve(0.3)
                scene izpawnshop_104 with Dissolve(0.3)
                psguard 1 "嗯……" with Dissolve(0.3)
                scene izpawnshop_105 with Dissolve(0.3)
                psguard 1 "{cps=5}……{/cps}" with Dissolve(0.3)
                scene izpawnshop_106 with Dissolve(0.3)
                psguard 1 "行，便宜你了，臭小子。" with Dissolve(0.3)
                
                $ renpy.notify("你给出去了四百块。")
                $ aksha -= 400
                $ pawnshop_paid = True
                
                scene izpawnshop_107 with Dissolve(0.3)
                iz 4 "他就是在敲诈我们。让他放段录像又不难！" with Dissolve(0.3)
                
                $ love_iz += 1
                show screen rel_up_izumi
                
                scene izpawnshop_108 with Dissolve(0.3)
                gg 16 "我知道。但吵架更费时间。看到录像更重要。" with Dissolve(0.3)
                
        "把耳环给他":
                pause 0.3
                show izpawnshop_109 with Dissolve(0.1)
                $ renpy.pause (1.5, hard=True)
                
                scene izpawnshop_110 with Dissolve(0.3)
                gg 16 "交给我吧，[iz]。" with Dissolve(0.3)
                scene izpawnshop_111 with Dissolve(0.3)
                "我小心地伸手到她耳边，帮她摘下耳环。"
                
                play sound slap_in_the_face
                
                scene izpawnshop_112 with hpunch
                pause 1.5
                scene izpawnshop_113 with Dissolve(0.3)
                pause 1.5
                scene izpawnshop_114 with Dissolve(0.3)
                iz 4 "你真要给出去？" with Dissolve(0.3)
                scene izpawnshop_115 with Dissolve(0.3)
                gg 16 "我们需要那段录像。那只是东西而已，[iz]。" with Dissolve(0.3)
                gg 16 "等真相查清，我们会拿回来的。"
                scene izpawnshop_116 with Dissolve(0.3)
                iz 4 "只是东西而已？" with Dissolve(0.3)
                scene izpawnshop_117 with Dissolve(0.3)
                iz 4 "对你来说只是东西……你说得真轻松……" with Dissolve(0.3)
                scene izpawnshop_118 with Dissolve(0.3)
                "我默默地摘下另一只耳环，把两只一起交给守卫。"
                scene izpawnshop_119 with Dissolve(0.3)
                "他咧嘴一笑接过，显然很满意这份轻易到手的战利品。"
                scene izpawnshop_120 with Dissolve(0.3)
                psguard 1 "可悲……" with Dissolve(0.3)
                scene izpawnshop_121 with Dissolve(0.3)
                iz 4 "我从没想过你会这么……这么干脆地交出去……真的没有别的办法了吗？" with Dissolve(0.3)
                scene izpawnshop_122 with Dissolve(0.3)
                gg 16 "这种时候，时间最要紧。想想我们要抓的是谁。" with Dissolve(0.3)
                scene izpawnshop_123 with Dissolve(0.3)
                iz 4 "{cps=5}……{/cps}"
                
                $ izumi_earrings_lost = True
                
    scene izpawnshop_124 with Dissolve(0.3)
    psguard 1 "跟我来。趁我还没改主意。" with Dissolve(0.3)
    
    stop music3 fadeout 3
    
    scene black with Dissolve(0.6)
    pause 1
    
### PAWNSHOP - Carl's office - DEAL
    
    play music2 stylish_thief_loop_1 fadein 8
    play sound5 creature_snore
    
    scene izpawnshop_125 with Dissolve(1.0)
    ''
    if izumi_earrings_lost == True:
        scene izpawnshop_126_1 with Dissolve(0.3)
    else:
        scene izpawnshop_126 with Dissolve(0.3)
        
    psguard 1 "行，我不想惹麻烦，动作快点，然后滚。" with Dissolve(0.3)
    
    if izumi_earrings_lost == True:
        scene izpawnshop_127_1 with Dissolve(0.3)
    else:
        scene izpawnshop_127 with Dissolve(0.3)
        
    psguard 1 "你看到的都烂在肚子里。" with Dissolve(0.3)
    
    if izumi_earrings_lost == True:
        scene izpawnshop_128_1 with Dissolve(0.3)
    else:
        scene izpawnshop_128 with Dissolve(0.3)
        
    gg 16 "当然。我们只需要某些细节……" with Dissolve(0.3)
    scene izpawnshop_129 with Dissolve(0.3)
    gg 16 "能把有人留下那台蓝色手机时的近期录像给我们看看吗？" with Dissolve(0.3)
    scene izpawnshop_130 with Dissolve(0.3)
    "守卫按了几个按钮，屏幕上闪过一段监控录像。"
    
    stop sound5 fadeout 10
    play sound hud_screen_is_on volume 0.3
    
    scene izpawnshop_131 with Dissolve(0.3)
    "画面里出现一个个子娇小的女孩——红发塞在帽子里，脸被医用口罩遮住。"
    scene izpawnshop_132 with Dissolve(0.3)
    gg 16 "（红发女孩……跟我们年纪差不多。）" with Dissolve(0.3)
    scene izpawnshop_133 with Dissolve(0.3)
    gg 16 "（身形有点像[may]。）" with Dissolve(0.3)
    scene izpawnshop_134 with Dissolve(0.3)
    iz 4 "我猜她大概刚满十八。" with Dissolve(0.3)
    scene izpawnshop_135 with Dissolve(0.3)
    iz 4 "她为什么要拿着我的手机？" with Dissolve(0.3)
    scene izpawnshop_136 with Dissolve(0.3)
    psguard 1 "不关我的事。她来了，留下手机，我的活就干完了。" with Dissolve(0.3)
    scene izpawnshop_137 with Dissolve(0.3)
    gg 16 "她一个人来的？" with Dissolve(0.3)
    
    if izumi_earrings_lost == True:
        scene izpawnshop_138_1 with Dissolve(0.3)
    else:
        scene izpawnshop_138 with Dissolve(0.3)
    
    psguard 1 "审问呢？" with Dissolve(0.3)
    
    if izumi_earrings_lost == True:
        scene izpawnshop_139_1 with Dissolve(0.3)
    else:
        scene izpawnshop_139 with Dissolve(0.3)
    
    psguard 1 "我们这儿客流量大。" with Dissolve(0.3)
    
    if izumi_earrings_lost == True:
        scene izpawnshop_140_1 with Dissolve(0.3)
    else:
        scene izpawnshop_140 with Dissolve(0.3)
    
    iz 4 "哦当然了，赃物流量大。" with Dissolve(0.3)
    
    if izumi_earrings_lost == True:
        scene izpawnshop_141_1 with Dissolve(0.3)
    else:
        scene izpawnshop_141 with Dissolve(0.3)
    
    psguard 1 "管好你的嘴，小姑娘。我们这儿什么都按规矩来。" with Dissolve(0.3)
    
    scene izpawnshop_142 with Dissolve(0.3)
    "我们把注意力重新放回录像上。"
    scene izpawnshop_143 with Dissolve(0.3)
    "那个拿着手机的女孩瞥了眼摄像头，但脸基本被口罩挡住。"
    scene izpawnshop_144 with Dissolve(0.3)
    gg 16 "（有意思……她好像知道自己可能会被拍到。）" with Dissolve(0.3)
    scene izpawnshop_145 with Dissolve(0.3)
    gg 16 "（这是事先计划好的？）" with Dissolve(0.3)
    
    if izumi_earrings_lost == True:
        scene izpawnshop_146_1 with Dissolve(0.3)
    else:
        scene izpawnshop_146 with Dissolve(0.3)
    
    iz 4 "现在我们怎么找她？连名字都没有。" with Dissolve(0.3)
    scene izpawnshop_147 with Dissolve(0.3)
    psguard 1 "到这儿。你看够了，滚吧——我没时间陪你们。" with Dissolve(0.3)
    scene izpawnshop_148 with Dissolve(0.3)
    pause 2
    
    stop music2 fadeout 3
    play sound2 heavy_dirty_traffic loop fadein 4 volume 0.5
    
    scene black with Dissolve(1.0)
    pause 2
    
### PAWNSHOP - OUTSIDE, END1
    
    scene izpawnshop_149 with Dissolve(0.3)
    "我们默默走出当铺，身后只留下灰尘的气味和老旧灯光的暖黄。"
    scene izpawnshop_150 with Dissolve(0.3)
    "脑子里只留下一件事：我们线索太少，下一步也不清楚。"
    
    if izumi_earrings_lost == True:
        scene izpawnshop_151_1 with Dissolve(0.3)
    else:
        scene izpawnshop_151 with Dissolve(0.3)
    
    iz 4 "真是个恶心的地方。" with Dissolve(0.3)
    
    if izumi_earrings_lost == True:
        scene izpawnshop_152_1 with Dissolve(0.3)
    else:
        scene izpawnshop_152 with Dissolve(0.3)
    
    iz 4 "我不知道哪更糟——是他们几乎不遮掩那些见不得人的生意，还是他们对「客人」毫不在意。" with Dissolve(0.3)
    scene izpawnshop_153 with Dissolve(0.3)
    gg 16 "走捷径比漫长调查省事。有时候这样反而更简单。" with Dissolve(0.3)
    
    if izumi_earrings_lost == True:
        scene izpawnshop_154_1 with Dissolve(0.3)
    else:
        scene izpawnshop_154 with Dissolve(0.3)
    
    iz 4 "而你确定没有别的办法？" with Dissolve(0.3)
    scene izpawnshop_155 with Dissolve(0.3)
    gg 16 "下次你想用假搜查令的话我们可以试试。" with Dissolve(0.3)
    
    if izumi_earrings_lost == True:
        scene izpawnshop_156_1 with Dissolve(0.3)
    else:
        scene izpawnshop_156 with Dissolve(0.3)
    
    iz 4 "好好好，算你说得有理。" with Dissolve(0.3)
    
    jump pawnshop_ending
    
###### PAWNSHOP, IN - DOMINATE
    
label pawnshop_resolve:
    
    stop sound3 fadeout 5
    stop sound4 fadeout 2
    stop sound5 fadeout 2
    
    pause 0.3
    
    play music3 assault_main_orig
    
    scene izpawnshop_157 with Dissolve(0.3)
    gg 16 "这破地方是谁的？" with Dissolve(0.3)
    scene izpawnshop_158 with Dissolve(0.3)
    psclerk 1 "你、你说什么？" with Dissolve(0.3)
    scene izpawnshop_159 with Dissolve(0.3)
    gg 16 "我问了。这破地方是谁的？" with Dissolve(0.3)
    scene izpawnshop_160 with Dissolve(0.3)
    psclerk 1 "呃……[carl]。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=0.5, channel=u'sound4')
    $ renpy.music.set_volume(1, delay=0.5, channel=u'sound5')
    play sound table_hit_hand_impact
    
    scene izpawnshop_161 with vpunch
    gg 16 "[carl]在哪儿？" with Dissolve(0.3)
    scene izpawnshop_162 with Dissolve(0.3)
    psclerk 1 "在他办公室……？" with Dissolve(0.3)
    scene izpawnshop_163 with Dissolve(0.3)
    gg 16 "你这是在陈述还是在问？" with Dissolve(0.3)
    scene izpawnshop_164 with Dissolve(0.3)
    psclerk 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    play sound chairwood
    
    scene izpawnshop_165 with Dissolve(0.3)
    "那个一直懒洋洋瘫在门边的守卫察觉到气氛不对，开始朝我们走过来。"
    scene izpawnshop_166 with Dissolve(0.3)
    gg 16 "喂，把[carl]叫出来。" with Dissolve(0.3)
    scene izpawnshop_167 with Dissolve(0.3)
    psguard 1 "什么玩意儿？！" with Dissolve(0.3)
    scene izpawnshop_168 with Dissolve(0.3)
    gg 16 "你听见了。把[carl]带来。" with Dissolve(0.3)
    
    play sound clothes_3
    
    scene izpawnshop_169 with Dissolve(0.3)
    psguard 1 "听着，眯眯眼，趁还能走赶紧滚！" with Dissolve(0.3)
    
    play sound2 police_opening_baton
    
    scene izpawnshop_170 with hpunch
    "守卫干脆利落地把伸缩警棍完全甩开。" with Dissolve(0.3)
    scene izpawnshop_171 with Dissolve(0.3)
    "他往前迈了一步，很明显这段对话到此为止。" with Dissolve(0.3)
    scene izpawnshop_172 with Dissolve(0.3)
    "我的手指握紧成拳，但[iz]就在我身边——我不能只想着自己。" with Dissolve(0.3)
    scene izpawnshop_173 with Dissolve(0.3)
    gg 16 "（可恶。现在只能先退。）" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.5, delay=1.5, channel=u'music3')
    
    scene black with Dissolve(1.0)
    pause 1
    
### PAWNSHOP - OUTSIDE, THE BRICK
    
    play sound3 heavy_dirty_traffic fadein 1 volume 0.5
    
    scene izpawnshop_174 with Dissolve(1.0)
    "我泉转身走到了外面。"
    scene izpawnshop_175 with Dissolve(0.5)
    "就在我思考下一步时，有东西吸引了我的目光……"
    scene izpawnshop_176 with Dissolve(0.3)
    pause 2
    
    play sound pick_up_stone
    
    scene izpawnshop_177 with Dissolve(0.5)
    pause 1.5
    scene izpawnshop_178 with Dissolve(0.3)
    iz 4 "你疯了吗？你打算干什么？！" with Dissolve(0.3)
    
    stop sound3 fadeout 2
    
    scene black with Dissolve(0.5)
    
    $ renpy.music.set_volume(1, delay=1.5, channel=u'music3')
    
    pause 0.5
    
    scene izpawnshop_179 with Dissolve(0.3)
    "我右手攥着那块砖，重新走进当铺。" with Dissolve(0.3)
    scene izpawnshop_180 with Dissolve(0.3)
    gg 16 "[carl]在哪儿？" with Dissolve(0.3)
    scene izpawnshop_181 with Dissolve(0.3)
    psguard 1 "我说了，贱人，滚出去！" with Dissolve(0.3)
    
    play sound2 police_opening_baton
    
    scene izpawnshop_182 with Dissolve(0.3)
    pause 1.5
    
    play sound rocks_impact_dropping_brick_on_stone_floor
    play sound3 blood_gore_impact_3
    
    scene izpawnshop_183 with hpunch
    pause 1.5
    
    play sound4 fist_chest_punch_6
    play sound kick_2 volume 0.5
    
    scene izpawnshop_184 with hpunch
    "他砰地一声倒在地上。"
    
    play sound5 human_vocal_female_lunatic_scream_fear_short_01
    
    scene izpawnshop_185 with hpunch
    "女店员尖叫着缩在柜台后面。"
    
    play sound door_doors_wing
    
    scene izpawnshop_186 with hpunch
    "那声响引得一个陌生男人从后屋冲了出来。"
    scene izpawnshop_187 with hpunch
    carl 1 "搞什么……[psmonica]，怎么回事？！" with Dissolve(0.3)
    scene izpawnshop_188 with Dissolve(0.3)
    gg 16 "啊，原来你就是[carl]。" with Dissolve(0.3)
    scene izpawnshop_189 with Dissolve(0.3)
    carl 1 "你他妈是谁？" with Dissolve(0.3)
    scene izpawnshop_190 with Dissolve(0.3)
    gg 16 "再说一遍你的名字。" with Dissolve(0.3)
    scene izpawnshop_191 with Dissolve(0.3)
    psmonica 1 "[psmonica]……" with Dissolve(0.3)
    scene izpawnshop_192 with Dissolve(0.3)
    gg 16 "你……" with Dissolve(0.3)
    scene izpawnshop_193 with Dissolve(0.3)
    gg 16 "站到[psmonica]旁边。" with Dissolve(0.3)
    scene izpawnshop_194 with Dissolve(0.3)
    carl 1 "所以是抢劫啊，操。" with Dissolve(0.3)
    scene izpawnshop_195 with Dissolve(0.3)
    pause 1.5
    scene izpawnshop_196 with Dissolve(0.3)
    carl 1 "哦，操，Thadius？" with Dissolve(0.3)
    carl 1 "他死了？"
    scene izpawnshop_197 with Dissolve(0.3)
    gg 16 "没有，突然说要睡觉去了。" with Dissolve(0.3)
    scene izpawnshop_198 with Dissolve(0.3)
    pause 1
    scene izpawnshop_199 with Dissolve(0.3)
    gg 16 "你手里拿的是什么？" with Dissolve(0.3)
    scene izpawnshop_200 with Dissolve(0.3)
    psmonica 1 "我、我的……我的手……手机……" with Dissolve(0.3)
    scene izpawnshop_201 with Dissolve(0.3)
    gg 16 "放进兜里。双手放在柜台上，让我看得见。" with Dissolve(0.3)
    scene izpawnshop_202 with Dissolve(0.3)
    psmonica 1 "请不要……" with Dissolve(0.3)
    scene izpawnshop_203 with Dissolve(0.3)
    gg 16 "现在你说——听着回答。摄像头的录像我去哪儿能弄到？" with Dissolve(0.3)
    scene izpawnshop_204 with Dissolve(0.3)
    carl 1 "录像？" with Dissolve(0.3)
    scene izpawnshop_205 with Dissolve(0.3)
    gg 16 "监控录像。天花板上那个摄像头的。" with Dissolve(0.3)
    scene izpawnshop_206 with Dissolve(0.3)
    carl 1 "你跟黑帮是一伙的？" with Dissolve(0.3)
    scene izpawnshop_207 with hpunch
    gg 16 "[iz]！" with Dissolve(0.3)
    scene izpawnshop_208 with Dissolve(0.3)
    iz 4 "我来了！" with Dissolve(0.3)
    scene izpawnshop_209 with Dissolve(0.3)
    gg 16 "现在给我下来！" with Dissolve(0.3)
    scene izpawnshop_210 with Dissolve(0.3)
    carl 1 "行行行，我知道了。我办公室。我……我给你们看。" with Dissolve(0.3)
    
    stop music3 fadeout 3
    
    scene black with Dissolve(0.3)
    pause 0.5
    
### PAWNSHOP - Carl's office - RESOLVE
    
    play music2 stylish_thief_loop_1 fadein 8
    
    scene izpawnshop_211 with Dissolve(0.3)
    ''
    scene izpawnshop_212 with Dissolve(0.3)
    "他一句话没说，把我们带到旁边那间摆着电脑的房间——他们的录像存储中心。"
    scene izpawnshop_213 with Dissolve(0.3)
    gg 16 "我需要有人留下那台蓝色手机时的录像。" with Dissolve(0.3)
    scene izpawnshop_214 with Dissolve(0.3)
    "他打开监控软件，飞快翻着文件，直到找到那段记录。"
    
    play sound hud_screen_is_on volume 0.3
    
    scene izpawnshop_131 with Dissolve(0.3)
    "录像里是个大约十八岁的女孩。红发塞在帽子里，脸被口罩遮住。"
    scene izpawnshop_132 with Dissolve(0.3)
    carl 1 "就是她。那台手机是她带来的。" with Dissolve(0.3)
    scene izpawnshop_133 with Dissolve(0.3)
    gg 16 "（红发女孩……跟我们年纪差不多。）" with Dissolve(0.3)
    scene izpawnshop_134 with Dissolve(0.3)
    gg 16 "（她的身形有点像[may]。）" with Dissolve(0.3)
    scene izpawnshop_135 with Dissolve(0.3)
    iz 4 "她是谁……又为什么会有我的手机？" with Dissolve(0.3)
    scene izpawnshop_136 with Dissolve(0.3)
    carl 1 "不知道。她进来放下手机就走了。" with Dissolve(0.3)
    
    scene izpawnshop_215 with Dissolve(0.3)
    gg 16 "她一个人来的？" with Dissolve(0.3)
    scene izpawnshop_216 with Dissolve(0.3)
    carl 1 "昨天这儿人很多，不过那个时间点……对，看起来只有她一个人。" with Dissolve(0.3)
    scene izpawnshop_217 with Dissolve(0.3)
    carl 1 "我们这儿客人多——电子产品卖得快。" with Dissolve(0.3)
    scene izpawnshop_218 with Dissolve(0.3)
    iz 4 "客人？还是从赃物里牟利的人？" with Dissolve(0.3)
    scene izpawnshop_142 with Dissolve(0.3)
    "我把注意力重新放回录像上。"
    scene izpawnshop_143 with Dissolve(0.3)
    "那个拿手机的女孩转向摄像头，但脸几乎完全被口罩挡住。"
    
    scene izpawnshop_219 with Dissolve(0.3)
    gg 16 "（有意思……看来她自己猜到可能会被拍到。）" with Dissolve(0.3)
    scene izpawnshop_220 with Dissolve(0.3)
    gg 16 "（是摆拍的吗？）" with Dissolve(0.3)
    
    scene izpawnshop_221 with Dissolve(0.3)
    gg 16 "我要的就这些。" with Dissolve(0.3)
    scene izpawnshop_222 with Dissolve(0.3)
    iz 4 "可我们连她名字都不知道！要怎么找她？" with Dissolve(0.3)
    scene izpawnshop_223 with Dissolve(0.3)
    carl 1 "就这些了吗？" with Dissolve(0.3)
    scene izpawnshop_224 with Dissolve(0.3)
    gg 16 "是的，谢谢配合。" with Dissolve(0.3)
    scene izpawnshop_225 with Dissolve(0.3)
    pause 2
    
    stop music2 fadeout 3
    play sound2 heavy_dirty_traffic loop fadein 4 volume 0.5
    
    scene black with Dissolve(1.0)
    pause 2
    
### PAWNSHOP - OUTSIDE, END2
    
    scene izpawnshop_226 with Dissolve(1.0)
    "我走出当铺，身后只留下碎砖、被吓傻的店员和一动不动的守卫。"
    scene izpawnshop_227 with Dissolve(0.3)
    "外面的空气比之前凉了些——不过也可能只是肾上腺素退去后留下的空虚。"
    scene izpawnshop_228 with Dissolve(0.3)
    "[iz]沉默地走在我身边。她瞥了我一眼，什么也没说。"
    
    $ love_iz += 1
    show screen rel_up_izumi
    $ pawnshop_resolve = True
    jump pawnshop_ending
    
###### PAWNSHOP - END
    
label pawnshop_ending:
    
    scene izpawnshop_229 with Dissolve(1.0)
    "路灯闪着冷光一盏盏亮起，天色暗了下来，把我们的影子拉长在人行道上。"
    
    if izumi_earrings_lost == True:
        scene izpawnshop_230_1 with Dissolve(0.6)
    else:
        scene izpawnshop_230 with Dissolve(0.3)
    
    "我掏出手机，屏幕上亮起好几通未接来电和[mi]的消息。"
    play sound4 call_dial_tone loop volume 0.3
    
    if izumi_earrings_lost == True:
        scene izpawnshop_231_1 with Dissolve(0.3)
    else:
        scene izpawnshop_231 with Dissolve(0.3)
        
    pause 2
    
    show izpawnshop_232:
        xpos 0
        ease 0.5 xpos -240
        
    stop sound4
    play sound3 button_accept_ping volume 0.3
    play sound woosh1 volume 0.5
    play music2 twinkled_night_loop_03 fadein 1
    $ renpy.music.set_volume(0.3, delay=2, channel=u'sound2')
    
    show izpawnshop_233 with Dissolve(0.3):
        xpos 1930
        ease 0.5 xpos 0
        
    mi 7 "[gg]！终于——你们两个没事吧？" with Dissolve(0.3)
    scene izpawnshop_234 with Dissolve(0.3)
    mi 7 "我正开始往最坏的方向想……" with Dissolve(0.3)
    scene izpawnshop_235 with Dissolve(0.3)
    gg 16 "放心吧。[iz]跟我在一起——我们没事。" with Dissolve(0.3)
    scene izpawnshop_236 with Dissolve(0.3)
    gg 16 "中间有些……麻烦，但没什么大碍。你找我有事？" with Dissolve(0.3)
    scene izpawnshop_237 with Dissolve(0.3)
    mi 7 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene izpawnshop_238 with Dissolve(0.3)
    mi 7 "有。我不知道该怎么解释，但挖得越深，这团乱麻就越难理清。" with Dissolve(0.3)
    scene izpawnshop_239 with Dissolve(0.3)
    mi 7 "尤其是你给我的那张纸条。" with Dissolve(0.3)
    scene izpawnshop_240 with Dissolve(0.3)
    gg 16 "你发现了什么？" with Dissolve(0.3)
    scene izpawnshop_241 with Dissolve(0.3)
    mi 7 "这么说吧……那天在咖啡馆我用紫外线灯的时候，我注意到了一些东西。" with Dissolve(0.3)
    scene izpawnshop_242 with Dissolve(0.3)
    mi 7 "那张纸条里藏着代码，我应该已经破解了……但细节等见面再说。" with Dissolve(0.3)
    scene izpawnshop_243 with Dissolve(0.3)
    mi 7 "我还从前同事那里拿到了一些数据。" with Dissolve(0.3)
    scene izpawnshop_244 with Dissolve(0.3)
    mi 7 "不想在电话里说太多。你现在回家吗？" with Dissolve(0.3)
    scene izpawnshop_245 with Dissolve(0.3)
    gg 16 "快了。" with Dissolve(0.3)
    scene izpawnshop_246 with Dissolve(0.3)
    gg 16 "三十分钟后能到我家吗？" with Dissolve(0.3)
    scene izpawnshop_247 with Dissolve(0.3)
    mi 7 "我正想提议见面呢。不过你家安全吗？" with Dissolve(0.3)
    scene izpawnshop_248 with Dissolve(0.3)
    mi 7 "我们也可以换个地方见面，但我觉得真的不能再拖了。" with Dissolve(0.3)
    scene izpawnshop_249 with Dissolve(0.3)
    gg 16 "过来吧。我们把一切都谈清楚。" with Dissolve(0.3)
    scene izpawnshop_250 with Dissolve(0.3)
    mi 7 "三十分钟后见。" with Dissolve(0.3)

    stop sound2 fadeout 2
    stop music2 fadeout 4

    scene black with Dissolve(1.0)
    pause 2
    pause 2
    
    $ renpy.music.set_volume(1, delay=0, channel=u'sound2')

###### HOME - MC, MINAMI, MAY

label vishome_minami:

    play music3 relaxing_lofi_ena__sascha_ende fadein 2

    show vishome_minami_1 with Dissolve(0.3)
    $ renpy.pause (4.5, hard=True)

    scene vishome_minami_2 with Dissolve(0.3)
    "见到[mi]，我关上门，公寓里的寂静立刻把我们吞没，隔绝了街上的噪音。"
    
    play sound clothes_1
    
    scene vishome_minami_3 with Dissolve(0.3)
    "屋里很暖，我毫不犹豫上前帮她脱外套。她没有反对，任由布料从肩头滑落。"
    scene vishome_minami_4 with Dissolve(0.3)
    gg 16 "进来吧，别客气。那件外套放桌上就行。" with Dissolve(0.3)
    scene vishome_minami_5 with Dissolve(0.3)
    mi 7 "谢谢。" with Dissolve(0.3)
    scene vishome_minami_6 with Dissolve(0.3)
    "她的香水留下一缕淡香——若有若无，恰好衬她。"
    scene vishome_minami_7 with Dissolve(0.3)
    "[mi]已经在桌边坐好，等着我。"
    scene vishome_minami_8 with Dissolve(0.3)
    "她神情专注而沉着——这种时候，她像是要把周围的一切都关在外面。"
    
    play sound creakswoodenstairs
    
    scene vishome_minami_9 with Dissolve(0.3)
    "忽然，楼上传来一阵急促的脚步声。"
    scene vishome_minami_10 with Dissolve(0.3)
    "我还没来得及转头，芽衣就从楼梯上下来了。"
    scene vishome_minami_11 with Dissolve(0.3)
    "她眼里闪过一丝不安，但一看到我就立刻被喜悦取代。"
    
    show vishome_minami_12 with Dissolve(0.2)
    $ renpy.pause(5.4,hard=True)
    
    scene vishome_minami_13 with Dissolve(0.3)
    may 15 "你终于回来啦！" with Dissolve(0.3)
    scene vishome_minami_14 with Dissolve(0.3)
    may 15 "一个人在家总觉得不踏实。" with Dissolve(0.3)
    scene vishome_minami_15 with Dissolve(0.3)
    may 15 "你帮上她了吗？" with Dissolve(0.3)
    scene vishome_minami_16 with Dissolve(0.3)
    gg 16 "咳……[may]，我们有客人。" with Dissolve(0.3)
    scene vishome_minami_17 with Dissolve(0.3)
    ''
    scene vishome_minami_18 with Dissolve(0.3)
    may 15 "栗原老师……怎么……" with Dissolve(0.3)
    scene vishome_minami_19 with Dissolve(0.3)
    may 15 "为什么……你会……在我们家？" with Dissolve(0.3)
    scene vishome_minami_20 with Dissolve(0.3)
    mi 7 "[may]？"
    
    stop music3 fadeout 10
    
    scene black with Dissolve(0.5)
    pause 0.5
    
    play music cozy_lo_fi_background_hip_hop fadein 10
    
    scene vishome_minami_21 with Dissolve(0.5)
    mi 7 "真没想到……说真的，看见你在这儿挺意外的。" with Dissolve(0.3)
    scene vishome_minami_22 with Dissolve(0.3)
    gg 16 "我跟[may]住在一起。" with Dissolve(0.3)
    scene vishome_minami_23 with Dissolve(0.3)
    may 15 "[gg]，你从没提过要请人来家里……" with Dissolve(0.3)
    scene vishome_minami_24 with Dissolve(0.3)
    gg 16 "这次见面看起来很突然，但有个重要的原因。抱歉，我该先跟你说的。" with Dissolve(0.3)
    scene vishome_minami_25 with Dissolve(0.3)
    mi 7 "[may]，我完全没想到会变成这样。" with Dissolve(0.3)
    scene vishome_minami_26 with Dissolve(0.3)
    mi 7 "谁能想到我和学生会在教室以外这样见面。" with Dissolve(0.3)
    scene vishome_minami_27 with Dissolve(0.3)
    mi 7 "我得问一下——你们两位是情侣还是亲戚？" with Dissolve(0.3)
    scene vishome_minami_28 with Dissolve(0.3)
    may 15 "啊……不、不是。既不是亲戚也不是情侣说来话长……" with Dissolve(0.3)
    scene vishome_minami_29 with Dissolve(0.3)
    may 15 "是某些契机让我们走到一起的。" with Dissolve(0.3)
    scene vishome_minami_30 with Dissolve(0.3)
    may 15 "你要是回想细节，可能会觉得这一切都有点奇怪……怎么说呢……" with Dissolve(0.3)
    scene vishome_minami_31 with Dissolve(0.3)
    gg 16 "（她给我带了东西。我们单独谈会更好。）" with Dissolve(0.3)
    scene vishome_minami_32 with Dissolve(0.3)
    gg 16 "[may]，能泡点茶吗？" with Dissolve(0.3)
    scene vishome_minami_33 with Dissolve(0.3)
    may 15 "我其实很想听听你们在聊什么，不过……好吧，我去烧水。" with Dissolve(0.3)
    
    show vishome_minami_34 with Dissolve(0.5)
    gg 16 "现在可以放开说了。你查到什么了？" with Dissolve(0.3)
    show vishome_minami_36 with Dissolve(0.2)
    hide vishome_minami_34
    mi 7 "就像我刚才说的，你给我的那张纸上写着加密信息。" with Dissolve(0.3)
    show vishome_minami_38 with Dissolve(0.2)
    hide vishome_minami_36
    mi 7 "内容指定了一个时间和坐标。指向的地点就在这座城里，所以我认为应该是在那里见面。" with Dissolve(0.3)
    show vishome_minami_34 with Dissolve(0.2)
    hide vishome_minami_38
    gg 16 "可我近期没约任何人见面。这次会面是什么时候？" with Dissolve(0.3)
    show vishome_minami_36 with Dissolve(0.2)
    hide vishome_minami_34
    mi 7 "今天，一个半小时后。我把坐标发到你手机上。" with Dissolve(0.3)
    mi 7 "地点和时间我都确认过。"
    show vishome_minami_34 with Dissolve(0.2)
    hide vishome_minami_36
    gg 16 "那这次会面是谁安排的？" with Dissolve(0.3)
    show vishome_minami_36 with Dissolve(0.2)
    hide vishome_minami_34
    mi 7 "你现在应该猜到了。" with Dissolve(0.3)
    show vishome_minami_34 with Dissolve(0.2)
    hide vishome_minami_36
    gg 16 "[asami]……"
    show vishome_minami_36 with Dissolve(0.2)
    hide vishome_minami_34
    mi 7 "不然我只会以为是随机的地理数据。" with Dissolve(0.3)
    mi 7 "从加密的细节来看，她打算在那里等你。"
    mi 7 "但是……总觉得哪里不对劲。"
    show vishome_minami_34 with Dissolve(0.2)
    hide vishome_minami_36
    gg 16 "你什么意思？" with Dissolve(0.3)
    show vishome_minami_38 with Dissolve(0.2)
    hide vishome_minami_34
    mi 7 "我有种不好的预感……" with Dissolve(0.3)
    mi 7 "她为什么要给你那张纸，却隐瞒会面地点？"
    show vishome_minami_34 with Dissolve(0.2)
    hide vishome_minami_38
    gg 16 "我直接问她。" with Dissolve(0.3)
    show vishome_minami_37 with Dissolve(0.2)
    hide vishome_minami_34
    mi 7 "我还是没完全想通。她到底是怎么联系上你的？为什么不像上次那样直接找你？" with Dissolve(0.3)
    show vishome_minami_38 with Dissolve(0.2)
    hide vishome_minami_37
    mi 7 "她到底想从你这儿得到什么……" with Dissolve(0.3)
    mi 7 "小心点。"
    show vishome_minami_34 with Dissolve(0.2)
    hide vishome_minami_38
    gg 16 "不用担心。我觉得她不会伤害我。" with Dissolve(0.3)
    show vishome_minami_36 with Dissolve(0.2)
    hide vishome_minami_34
    mi 7 "别忘了这仍可能是陷阱。等你的未必是[asami]，甚至可能是信徒。" with Dissolve(0.3)
    show vishome_minami_34 with Dissolve(0.2)
    hide vishome_minami_36
    gg 16 "我会留意的。这是我们唯一的线索，别无选择。" with Dissolve(0.3)
    gg 16 "谁知道我们还能不能有下一次机会揭开真相？"
    show vishome_minami_39 with Dissolve(0.2)
    hide vishome_minami_34
    mi 7 "请务必小心。" with Dissolve(0.3)
    show vishome_minami_35 with Dissolve(0.2)
    hide vishome_minami_39
    gg 16 "明白。" with Dissolve(0.3)
    show vishome_minami_40 with Dissolve(0.2)
    hide vishome_minami_35
    mi 7 "这是我从前同事那里弄来的。" with Dissolve(0.3)
    mi 7 "这些文件……绝不能落到不该落的人手里。"
    show vishome_minami_34 with Dissolve(0.2)
    hide vishome_minami_40
    gg 16 "里面是什么？" with Dissolve(0.3)
    show vishome_minami_36 with Dissolve(0.2)
    hide vishome_minami_34
    mi 7 "恶魔阶层存在的证据，它们的分类和各自独特的性质。" with Dissolve(0.3)
    show vishome_minami_37 with Dissolve(0.2)
    hide vishome_minami_36
    mi 7 "我觉得你应该自己读一遍，但……小心别让别人看到这些纸。" with Dissolve(0.3)
    show vishome_minami_38 with Dissolve(0.2)
    hide vishome_minami_37
    mi 7 "说实话，我都不确定该不该让她知道。" with Dissolve(0.3)
    show vishome_minami_35 with Dissolve(0.2)
    hide vishome_minami_38
    gg 16 "还是让[may]别牵扯进来比较好。她的安全是第一位的。" with Dissolve(0.3)

    scene vishome_minami_41 with Dissolve(0.3)
    gg 16 "我过几分钟就出来。" with Dissolve(0.3)
    scene vishome_minami_42 with Dissolve(0.3)
    "我拿起那叠文件，从桌边起身，不慌不忙地走向楼梯。"
    scene vishome_minami_43 with Dissolve(0.3)
    "踏上台阶时，我感觉[may]灼热的目光烧在背上。她什么也没说，但她的沉默比言语更响。"
    
    stop music fadeout 5
    play sound2 evening_city_looping_ambience_loop_full loop fadein 5
    
    scene vishome_minami_44 with Dissolve(1)
    "走进房间，我把那些纸放在床上。"
    "这只是个借口——把自己隔开，好买几秒钟消化这一切。"
    
    scene black with Dissolve(0.5)
    pause 0.3
    
    stop sound2 fadeout 2
    play sound3 mysterious_muted_dimension_loop fadein 2 loop
    
    scene vishome_minami_45 with Dissolve(1.0)
    gg 16 "（我知道今晚要见[asami]。而现在，我完全不知道那里等着我的是什么。）" with Dissolve(0.3)
    gg 16 "（那个认识我的[asami]来自未来，但活在此时这条时间线上的她，实质上是另一个人。）"
    scene vishome_minami_46 with Dissolve(0.6)
    gg 16 "（这两年她都经历了什么？而现在的她又会怎么看我？）" with Dissolve(0.3)
    gg 16 "（在这条时间线上，我们甚至还没见过面。她大概不会有关于我的重要信息。）"
    
    stop sound3 fadeout 1
    play sound2 evening_city_looping_ambience_loop_full loop fadein 5
    
    scene black with Dissolve(0.5)
    pause 0.3
    
    scene vishome_minami_47 with Dissolve(0.6)
    gg 16 "（那她昨晚为什么不开枪？难道她认识那帮人？）" with Dissolve(0.3)
    gg 16 "（不知道我已经经历过的那条时间线里，后来是怎么发展的。）"
    scene vishome_minami_48 with Dissolve(0.5)
    gg 16 "（我们是在战场上相遇，站到同一边、肩并肩对抗共同的敌人吗？）" with Dissolve(0.3)
    gg 16 "（还是以另一种方式——在沉默中，在话语与秘密之间，因共同的目标而缓慢又不可避免地被绑在一起？）"
    
    play sound pistol_1
    
    scene vishome_minami_49 with Dissolve(0.5)
    gg 16 "（我不打算朝她开枪。但盲目信任也不行。我必须保持警惕。）" with Dissolve(0.3)
    
    play sound pistol_2
    
    scene vishome_minami_50 with Dissolve(0.6)
    gg 16 "（讽刺的是，我随身带的那把枪……原本是她的。）" with Dissolve(0.3)
    
    play sound3 mountain_audio_tea_kettle_whistling_loop fadein 0.3
    stop sound2 fadeout 0.3
    
    scene vishome_minami_51 with Dissolve(0.3)
    pause 1.5
    
    stop sound3 fadeout 0.5
    play music relaxing_lofi_ena__sascha_ende
    
    scene vishome_minami_52 with Dissolve(0.5)
    pause 2
    scene vishome_minami_53 with Dissolve(0.3)
    gg 16 "我得走了。" with Dissolve(0.3)
    scene vishome_minami_54 with Dissolve(0.3)
    mi 7 "你去会面的时候，[may]一个人没事吗？" with Dissolve(0.3)
    scene vishome_minami_55 with Dissolve(0.3)
    gg 16 "其实我想拜托你一件事。今天能不能陪着她，帮我看着她直到我回来？" with Dissolve(0.3)
    scene vishome_minami_56 with Dissolve(0.3)
    mi 7 "要能让你安心，我乐意之至。" with Dissolve(0.3)
    scene vishome_minami_57 with Dissolve(0.3)
    mi 7 "看来你不在的时候她需要人陪。" with Dissolve(0.3)
    scene vishome_minami_58 with Dissolve(0.3)
    gg 16 "谢谢你，[mi]。别让[may]起疑。" with Dissolve(0.3)
    scene vishome_minami_59 with Dissolve(0.3)
    gg 16 "只是……尽量别让她觉得出了什么事。" with Dissolve(0.3)
    scene vishome_minami_60 with Dissolve(0.3)
    mi 7 "当然。我就跟她聊聊天，让她分心。" with Dissolve(0.3)
    scene vishome_minami_61 with Dissolve(0.3)
    mi 7 "快去做你该做的事吧！" with Dissolve(0.3)
    scene vishome_minami_62 with Dissolve(0.3)
    "我又检查了一遍东西是否带齐，然后走向门口。" with Dissolve(0.3)
    scene vishome_minami_63 with Dissolve(0.3)
    "就在这时，[may]端着托盘从厨房出来，一看到我愣住了。" with Dissolve(0.3)
    scene vishome_minami_64 with Dissolve(0.3)
    may 15 "你要走？可我刚泡好茶……" with Dissolve(0.3)
    may 15 "等等！出什么事了吗？"
    scene vishome_minami_65 with Dissolve(0.3)
    gg 16 "我很快就回来。[mi]会陪着你，好吗？" with Dissolve(0.3)
    scene vishome_minami_66 with Dissolve(0.3)
    mi 7 "没事的，[may]。[gg]忙的时候我们好好聊聊。" with Dissolve(0.3)
    scene vishome_minami_67 with Dissolve(0.3)
    mi 7 "你不介意聊些女孩子的话题吧？" with Dissolve(0.3)
    scene vishome_minami_68 with Dissolve(0.3)
    may 15 "哦、哦！当、当然不介意！" with Dissolve(0.3)
    scene vishome_minami_69 with Dissolve(0.3)
    may 15 "[gg]，怎么了？她要留下来？" with Dissolve(0.3)
    scene vishome_minami_70 with Dissolve(0.3)
    gg 16 "我不在的时候她陪你。" with Dissolve(0.3)
    scene vishome_minami_71 with Dissolve(0.3)
    may 15 "真的有必要吗？" with Dissolve(0.3)
    scene vishome_minami_72 with Dissolve(0.3)
    mi 7 "这么说，你们只是青梅竹马？" with Dissolve(0.3)
    scene vishome_minami_73 with Dissolve(0.3)
    mi 7 "[may]，他没对你做过什么……奇怪的事吧？" with Dissolve(0.3)
    scene vishome_minami_74 with Dissolve(0.3)
    may 15 "没、没有，没有那种事！" with Dissolve(0.3)
    scene vishome_minami_75 with Dissolve(0.3)
    mi 7 "看来你这种小个子不是他的菜。" with Dissolve(0.3)
    scene vishome_minami_76 with Dissolve(0.3)
    mi 7 "你运气好。" with Dissolve(0.3)
    scene vishome_minami_77 with Dissolve(0.3)
    gg 16 "就算是，我脑子也还清醒着呢。" with Dissolve(0.3)
    scene vishome_minami_78 with Dissolve(0.3)
    mi 7 "哈哈，逗你的！" with Dissolve(0.3)
    scene vishome_minami_79 with Dissolve(0.3)
    mi 7 "喂，你那是什么表情？" with Dissolve(0.3)
    scene vishome_minami_80 with Dissolve(0.3)
    may 15 "呃，没有……没什么！" with Dissolve(0.3)
    scene vishome_minami_81 with Dissolve(0.3)
    mi 7 "光看你脸我还真差点信了。" with Dissolve(0.3)
    scene vishome_minami_82 with Dissolve(0.3)
    may 15 "真的没什么，别担心。" with Dissolve(0.3)
    scene vishome_minami_83 with Dissolve(0.3)
    mi 7 "是吗……" with Dissolve(0.3)
    scene vishome_minami_84 with Dissolve(0.3)
    mi 7 "[gg]，你出门前没落下什么吧？" with Dissolve(0.3)
    scene vishome_minami_85 with Dissolve(0.3)
    gg 16 "没有。要带的都带了。" with Dissolve(0.3)
    scene vishome_minami_86 with Dissolve(0.3)
    gg 16 "那我走了。别太想我！" with Dissolve(0.3)
    
    play sound dish_plate_put_away
    
    scene vishome_minami_87 with Dissolve(0.3)
    pause 1
    scene vishome_minami_88 with Dissolve(0.3)
    pause 1.5
    
    play sound2 pouring_boiling_water_into_instant_coffee
    
    scene vishome_minami_89 with Dissolve(0.3)
    pause 0.5
    may 15 "他走了。" with Dissolve(0.3)
    
    stop sound2 fadeout 0.3
    play sound foodtware_stirring_tea_drink_in_cup_mug_with_spoon_01 volume 0.5
    
    show vishome_minami_93 with Dissolve(0.5)
    mi 7 "谢谢你的茶。" with Dissolve(0.3)
    show vishome_minami_90 with Dissolve(0.3)
    hide vishome_minami_93
    may 15 "不客气。" with Dissolve(0.3)
    show vishome_minami_91 with Dissolve(0.3)
    hide vishome_minami_90
    mi 7 "我能问你几个问题吗？" with Dissolve(0.3)
    mi 7 "要是哪个问题太私人，你不用回答。"
    show vishome_minami_96 with Dissolve(0.3)
    hide vishome_minami_91
    may 15 "好啊，我不介意。" with Dissolve(0.3)
    show vishome_minami_92 with Dissolve(0.3)
    hide vishome_minami_96
    mi 7 "你真不是他妹妹？" with Dissolve(0.3)
    show vishome_minami_96 with Dissolve(0.3)
    hide vishome_minami_92
    may 15 "真的不是。" with Dissolve(0.3)
    show vishome_minami_91 with Dissolve(0.3)
    hide vishome_minami_96
    mi 7 "除了你们两个，还有别人住这儿吗？" with Dissolve(0.3)
    show vishome_minami_90 with Dissolve(0.3)
    hide vishome_minami_91
    may 15 "没有，就我们俩。" with Dissolve(0.3)
    show vishome_minami_91 with Dissolve(0.3)
    hide vishome_minami_90
    mi 7 "还有别的亲戚吗？" with Dissolve(0.3)
    show vishome_minami_99 with Dissolve(0.3)
    hide vishome_minami_91
    may 15 "有个叔叔最近帮我们搬进了这套公寓。不过……没有别人了。" with Dissolve(0.3)
    show vishome_minami_91 with Dissolve(0.3)
    hide vishome_minami_99
    mi 7 "我明白了。那我问一下——你父母是什么时候不在的？" with Dissolve(0.3)
    show vishome_minami_90 with Dissolve(0.3)
    hide vishome_minami_91
    may 15 "妈妈……很久以前了。爸爸两个月前去世。" with Dissolve(0.3)
    show vishome_minami_91 with Dissolve(0.3)
    hide vishome_minami_90
    mi 7 "你知道原因吗？" with Dissolve(0.3)
    show vishome_minami_99 with Dissolve(0.3)
    hide vishome_minami_91
    may 15 "意外。车祸。" with Dissolve(0.3)
    show vishome_minami_92 with Dissolve(0.3)
    hide vishome_minami_99
    mi 7 "唉，可怜的孩子……我很难过。" with Dissolve(0.3)
    mi 7 "不过，作为你的老师，我想问问你的未来。"
    show vishome_minami_93 with Dissolve(0.3)
    hide vishome_minami_92
    mi 7 "记住，要是感到不舒服，随时可以打断我。" with Dissolve(0.3)
    show vishome_minami_94 with Dissolve(0.3)
    hide vishome_minami_93
    may 15 "没关系，我理解你的关心。你想问什么？" with Dissolve(0.3)
    show vishome_minami_97 with Dissolve(0.3)
    hide vishome_minami_94
    mi 7 "首先……你打算跟他一起住多久？" with Dissolve(0.3)
    show vishome_minami_98 with Dissolve(0.3)
    hide vishome_minami_97
    may 15 "{cps=5}……{/cps}" with Dissolve(0.3)
    may 15 "{cps=5}……{/cps}"
    show vishome_minami_92 with Dissolve(0.3)
    hide vishome_minami_98
    mi 7 "好吧。那你只要明白这一点：现在你毕竟还只是个女高中生。也许[gg]接受的就是现在这样。" with Dissolve(0.3)
    show vishome_minami_95 with Dissolve(0.3)
    hide vishome_minami_92
    mi 7 "但总有一天，他——或者你——也许会遇到某个特别的人。而你……可能会处境尴尬。" with Dissolve(0.3)
    show vishome_minami_96 with Dissolve(0.3)
    hide vishome_minami_95
    may 15 "住在一起有什么问题？合租的人不一定是情侣，也可以各自跟别人交往……" with Dissolve(0.3)
    may 15 "跟一个不是家人的人住在一起，不代表你就属于他。"
    show vishome_minami_91 with Dissolve(0.3)
    hide vishome_minami_96
    mi 7 "有道理。" with Dissolve(0.3)
    mi 7 "而且我真的很高兴，你从小就认识他，跟他在一起很有安全感。"
    mi 7 "[gg]看起来是个可靠的人。我看得出你信任他——从你们的相处方式就很明显。"
    show vishome_minami_92 with Dissolve(0.3)
    hide vishome_minami_91
    mi 7 "但我还注意到另一件事……" with Dissolve(0.3)
    mi 7 "你自己也有该做的决定。你明白的，对吧？"
    show vishome_minami_99 with Dissolve(0.3)
    hide vishome_minami_92
    may 15 "是的……我明白。" with Dissolve(0.3)
    show vishome_minami_91 with Dissolve(0.3)
    hide vishome_minami_99
    mi 7 "你作为无忧无虑的学生的时间会过得很快。" with Dissolve(0.3)
    mi 7 "所以趁现在好好珍惜他的温柔，但要想清楚你想站在谁身边。"
    show vishome_minami_90 with Dissolve(0.3)
    hide vishome_minami_91
    may 15 "栗原老师……" with Dissolve(0.3)
    show vishome_minami_92 with Dissolve(0.3)
    hide vishome_minami_90
    mi 7 "光有[mi]就够了。" with Dissolve(0.3)
    show vishome_minami_96 with Dissolve(0.3)
    hide vishome_minami_92
    may 15 "啊……好吧……" with Dissolve(0.3)
    may 15 "[mi]，你说。"
    show vishome_minami_93 with Dissolve(0.3)
    hide vishome_minami_96
    mi 7 "嗯？" with Dissolve(0.3)
    show vishome_minami_94 with Dissolve(0.3)
    hide vishome_minami_93
    may 15 "你喜欢[gg]吗？" with Dissolve(0.3)

    stop music fadeout 4

    scene black with Dissolve(0.5)
    pause 2
    pause 2

###### ROOFTOP - MC, ASAMI

label meeting_asami:
    
    show meeting_asami_1 with Dissolve(0.1)
    $ renpy.pause (26, hard=True) #66
    show meeting_asami_1_sub_1
    $ renpy.pause (2, hard=True)
    hide meeting_asami_1_sub_1
    $ renpy.pause (0.1, hard=True)
    show meeting_asami_1_sub_2
    $ renpy.pause (2, hard=True)
    hide meeting_asami_1_sub_2
    $ renpy.pause (9.4, hard=True)
    show meeting_asami_1_sub_3
    $ renpy.pause (1.1, hard=True)
    hide meeting_asami_1_sub_3
    $ renpy.pause (0.3, hard=True)
    show meeting_asami_1_sub_4
    $ renpy.pause (3, hard=True)
    hide meeting_asami_1_sub_4
    $ renpy.pause (6.7, hard=True)
    show meeting_asami_1_sub_5
    $ renpy.pause (2.2, hard=True)
    hide meeting_asami_1_sub_5
    $ renpy.pause (0.3, hard=True)
    show meeting_asami_1_sub_6
    $ renpy.pause (1.2, hard=True)
    hide meeting_asami_1_sub_6
    $ renpy.pause (1.4, hard=True)
    show meeting_asami_1_sub_7
    $ renpy.pause (1.2, hard=True)
    hide meeting_asami_1_sub_7
    $ renpy.pause (2.4, hard=True)
    show meeting_asami_1_sub_8
    $ renpy.pause (2.2, hard=True)
    hide meeting_asami_1_sub_8
    $ renpy.pause (3.6, hard=True)

    play sound2 amb_citytrafficdronehorns loop fadein 2

    scene meeting_asami_2 with Dissolve(0.3)
    gg 16 "（能走到这里真不容易。）" with Dissolve(0.3)
    scene meeting_asami_3 with Dissolve(0.3)
    gg 16 "（现在，得弄清楚我为什么会在这里……）" with Dissolve(0.3)
    scene meeting_asami_4 with Dissolve(0.3)
    gg 16 "（那是什么声音？）" with Dissolve(0.3)
    scene meeting_asami_5 with Dissolve(0.3)
    pause 1.5
    scene meeting_asami_6 with Dissolve(0.3)
    asami 4 "你他妈是谁？" with Dissolve(0.3)
    
    show meeting_asami_7 with Dissolve(0.2)
    $ renpy.pause (1.8, hard=True)
    
    stop sound2 fadeout 5
    play music2 dark_cyberpunk_future_loop
    
    $ renpy.pause (20.7, hard=True)
    
    scene meeting_asami_8 with hpunch
    gg 17 "住手！" with Dissolve(0.3)
    
    show meeting_asami_9 with Dissolve(0.2)
    $ renpy.pause (28.2, hard=True)
    
    scene meeting_asami_10 with hpunch
    asami 5 "抓到你了！" with Dissolve(0.3)
    scene meeting_asami_11 with Dissolve(0.3)
    asami 5 "刚才还算热身。现在说吧……" with Dissolve(0.3)
    scene meeting_asami_12 with Dissolve(0.3)
    gg 17 "[asami]，等等……" with Dissolve(0.3)
    scene meeting_asami_13 with Dissolve(0.3)
    pause 0.3
    scene meeting_asami_14 with Dissolve(0.3)
    pause 1
    
    play sound heavy_body_fall_01
    
    scene meeting_asami_15 with vpunch
    pause 1.5
    scene meeting_asami_16 with Dissolve(0.3)
    asami 5 "一个知道我名字的男人？那你回答我……" with Dissolve(0.3)
    asami 5 "你他妈到底是谁？！"
    scene meeting_asami_17 with Dissolve(0.3)
    gg 17 "我叫[gg]！" with Dissolve(0.3)
    scene meeting_asami_18 with Dissolve(0.3)
    asami 5 "告诉我是谁派你来的，我就让你痛快上路。" with Dissolve(0.3)
    scene meeting_asami_19 with Dissolve(0.3)
    gg 17 "我是[gg]——我是在见过你之后才来的……" with Dissolve(0.3)
    scene meeting_asami_20 with Dissolve(0.3)
    gg 17 "从未来来的！" with Dissolve(0.3)
    scene meeting_asami_21 with Dissolve(0.3)
    asami 5 "你以为这是玩笑？" with Dissolve(0.3)
    scene meeting_asami_22 with Dissolve(0.3)
    gg 17 "靠，我不是在开玩笑！这他妈是传送门和恶魔！" with Dissolve(0.3)
    gg 17 "是你告诉我一年后会有一场灾难！"
    scene meeting_asami_23 with Dissolve(0.3)
    gg 17 "是那个你说要我去找的未来！" with Dissolve(0.3)
    gg 17 "听我说啊，混蛋！"
    
    stop music2 fadeout 4
    scene black with Dissolve(1.0)
    play music3 in_tension_asami_loop fadein 8
    pause 2
    pause 2
    
    $ asami_unlock = True
    show screen rel_open_asami
    
    show meeting_asami_24 with Dissolve(0.5)
    asami 4 "所以……是这么回事。真他妈是个笑话。" with Dissolve(0.3)
    asami 4 "我讨厌这样。"
    gg 16 "你的意思是什么都改变不了？" with Dissolve(0.3)
    show meeting_asami_27 with Dissolve(0.2)
    hide meeting_asami_24
    asami 4 "问题不在这里。" with Dissolve(0.3)
    asami 4 "在那条时间线里，灾难已经发生了。"
    asami 4 "只不过那时我在帮你，而我们还是失败了。"
    asami 4 "你知道知道这件事我有多火大吗？"
    show meeting_asami_28 with Dissolve(0.2)
    hide meeting_asami_27
    gg 16 "这时间旅行到底是怎么回事？" with Dissolve(0.3)
    show meeting_asami_29 with Dissolve(0.2)
    hide meeting_asami_28
    asami 4 "说来话长。而且据我所见，方法不止一种。" with Dissolve(0.3)
    asami 4 "但先算了。你那个时代遇见我的时候——这座城还立着吗？还是一片废墟？"
    show meeting_asami_28 with Dissolve(0.2)
    hide meeting_asami_29
    gg 16 "废弃了，但大体完好。" with Dissolve(0.3)
    gg 16 "人们还在——警察、军队，拼命守着防线。看起来不太妙。"
    show meeting_asami_26 with Dissolve(0.2)
    hide meeting_asami_28
    asami 4 "当然了。人类在公平较量中从来就没有胜算。" with Dissolve(0.3)
    asami 4 "不过有个好消息：你到的时候，入侵已经持续一年了。"
    asami 4 "也就是说……如果我们现在还剩将近一年，这次我们真的可以做点什么。"
    show meeting_asami_29 with Dissolve(0.2)
    hide meeting_asami_26
    asami 4 "就算阻止不了，至少能扭转一些天平。" with Dissolve(0.3)
    asami 4 "说真的？我很惊讶你们居然撑了那么久。"
    show meeting_asami_28 with Dissolve(0.2)
    hide meeting_asami_29
    gg 16 "好吧，这也算……有点意义。那我们现在就行动。" with Dissolve(0.3)
    gg 16 "如果我们能弄清楚这些传送门为什么会开启，也许能找到一条出路。"
    show meeting_asami_25 with Dissolve(0.2)
    hide meeting_asami_28
    asami 4 "为什么？你问这个？" with Dissolve(0.3)
    asami 4 "我有一些推测……"
    asami 4 "但在那条时间线里，未来早已注定。"
    show meeting_asami_27 with Dissolve(0.2)
    hide meeting_asami_25
    asami 4 "你们第一次失败只有一个原因：你们没有准备好。" with Dissolve(0.3)
    asami 4 "你们不知道要来的东西是什么。对吧？"
    show meeting_asami_28 with Dissolve(0.2)
    hide meeting_asami_27
    gg 16 "假设你说得对。那我现在该做什么？" with Dissolve(0.3)
    show meeting_asami_29 with Dissolve(0.2)
    hide meeting_asami_28
    asami 4 "你能自由进行时间旅行吗？" with Dissolve(0.3)
    show meeting_asami_24 with Dissolve(0.2)
    hide meeting_asami_29
    gg 16 "不能。连我自己都没完全搞明白是怎么发生的。" with Dissolve(0.3)
    show meeting_asami_31 with Dissolve(0.2)
    hide meeting_asami_24
    asami 4 "那就……跳下去。" with Dissolve(0.3)
    show meeting_asami_30 with Dissolve(0.2)
    hide meeting_asami_31
    gg 16 "什么？" with Dissolve(0.3)
    show meeting_asami_31 with Dissolve(0.2)
    hide meeting_asami_30
    asami 4 "我们在楼顶。够高。跳下去。" with Dissolve(0.3)
    show meeting_asami_30 with Dissolve(0.2)
    hide meeting_asami_31
    gg 16 "我还不想疯到去自杀。" with Dissolve(0.3)
    show meeting_asami_31 with Dissolve(0.2)
    hide meeting_asami_30
    asami 4 "你活不活跟我无关。问题在于：死亡逼近的时候，人会变得更强。" with Dissolve(0.3)
    asami 4 "除非你接受死亡，否则你活不下来。"
    show meeting_asami_30 with Dissolve(0.2)
    hide meeting_asami_31
    gg 16 "你疯了？" with Dissolve(0.3)
    gg 16 "我会摔成肉饼。什么都不会「发生」。"
    show meeting_asami_32 with Dissolve(0.2)
    hide meeting_asami_30
    asami 4 "那新闻就会说是一名学生自杀。" with Dissolve(0.3)
    asami 4 "不过话说回来——末日来的时候，你也不会在乎了。双赢。"

    scene meeting_asami_33 with Dissolve(0.3)
    gg 16 "（我非常怀疑这一点。）" with Dissolve(0.3)
    asami 4 "我要是想杀你，你已经死了。" with Dissolve(0.3)
    asami 4 "跳。不然你就把你刚跟我说的一切再经历一遍。"
    
    scene black with Dissolve(0.3)
    pause 0.3
    
    scene meeting_asami_34 with Dissolve(0.3)
    gg 16 "（可恶。我他妈到底是怎么了？）" with Dissolve(0.3)
    scene meeting_asami_34_1 with Dissolve(0.3)
    gg 16 "行。我跳。" with Dissolve(0.3)
    
    show meeting_asami_35 with Dissolve(0.2)
    $ renpy.pause (4.4, hard=True)
    
    scene meeting_asami_36 with Dissolve(0.2)
    gg 16 "那是什么？" with Dissolve(0.3)
    scene meeting_asami_37 with Dissolve(0.3)
    asami 4 "准备好了？" with Dissolve(0.3)
    scene meeting_asami_38 with Dissolve(0.3)
    gg 16 "不。" with Dissolve(0.3)
    scene meeting_asami_39 with Dissolve(0.3)
    asami 4 "等你睁开眼……别相信任何人。" with Dissolve(0.3)
    scene meeting_asami_40 with Dissolve(0.3)
    asami 4 "回头见。" with Dissolve(0.3)
    
    stop music3 fadeout 2
    play sound2 demian_falls_stereo_color_panic_main volume 0.8
    
    show meeting_asami_41 with Dissolve(0.3)
    $ renpy.pause (11.3, hard=True)
    stop music3 fadeout 4
    scene black with Dissolve(0.1)
    pause 3
    pause 3
    
    jump darkside1

###### DARKSIDE - 1

label darkside1:
    
    show darkside1_1 with Dissolve(0.1)
    $ renpy.pause(2.2, hard=True)
    
    play music3 empty_scary_place_ambience_looping volume 0.8 fadein 8
    
    $ renpy.pause(2, hard=True)
    
    scene darkside1_2 with hpunch
    gg 16 "啊啊！" with Dissolve(0.1)
    scene darkside1_3 with Dissolve(0.3)
    gg 16 "我他妈，这到底怎么回事？！" with Dissolve(0.1)
    scene darkside1_4 with Dissolve(0.3)
    gg 16 "{cps=5}……{/cps}"
    scene darkside1_5 with Dissolve(0.3)
    pause 2
    play sound ds1_rat
    show darkside1_6 with Dissolve(0.2)
    $ renpy.pause (11.3, hard=True)
    
    scene darkside1_7 with Dissolve(0.3)
    gg 16 "（我在哪儿……？）" with Dissolve(0.3)
    scene darkside1_8 with Dissolve(0.3)
    gg 16 "（恶魔……？）" with Dissolve(0.3)
    
    play sound2 fs_ext_up_concrete_steps volume 0.4
    
    scene darkside1_9 with Dissolve(0.3)
    pause 2
    scene darkside1_10 with Dissolve(0.3)
    pause 1.5
    
    stop sound2 fadeout 0.3
    
    scene darkside1_12 with Dissolve(0.3)
    pause 1
    gg 16 "这到底是什么鬼地方？！" with Dissolve(0.3)
    
    play sound clothes_2
    
    scene darkside1_13 with Dissolve(0.3)
    pause 1
    
    play sound3 grab_4
    
    scene darkside1_14 with Dissolve(0.3)
    gg 16 "（我该确认一下……）" with Dissolve(0.3)
    
    play sound2 button_declined_2 volume 0.5
    
    scene darkside1_15 with Dissolve(0.3)
    gg 16 "（这里没有信号。）" with Dissolve(0.3)
    
    play sound clothes_1
    
    scene darkside1_16 with Dissolve(0.3)
    pause 1
    scene darkside1_17 with Dissolve(0.3)
    gg 16 "...!" with Dissolve(0.1)
    scene darkside1_18 with Dissolve(0.3)
    gg 16 "（搞什么……？）" with Dissolve(0.3)
    gg 16 "（这个原本在我口袋里。）"
    scene darkside1_19 with Dissolve(0.3)
    gg 16 "（是某种装置。一个小金属球——很轻，几乎像个玩具。漆面斑驳，到处是刮痕。）" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.5, delay=2, channel=u'music3')
    
    scene darkside1_20 with Dissolve(0.3)
    gg 16 "（一侧有一枚很小的镜头……摄像头？）" with Dissolve(0.3)
    
    play sound3 cinematic_hologram_indicator
    
    scene darkside1_21 with Dissolve(0.3)
    pause 0.5
    scene darkside1_20 with Dissolve(0.3)
    pause 0.4
    gg 16 "（有个指示灯在闪……糟了，要启动了吗？）" with Dissolve(0.3)
    scene darkside1_21 with Dissolve(0.3)
    pause 0.4
    scene darkside1_20 with Dissolve(0.2)
    pause 0.3
    scene darkside1_21 with Dissolve(0.2)
    pause 0.2
    scene darkside1_20 with Dissolve(0.2)
    
    play sound2 cinematic_hologram_1 volume 0.5
    
    pause 0.1
    scene darkside1_22 with Dissolve(0.2)
    pause 0.5
    scene darkside1_23 with Dissolve(0.3)
    pause 0.2
    asami 4 "欢迎来到地狱，[gg]。你在暗界，而它已经注意到你了！" with Dissolve(0.3)
    asami 4 "我在楼顶把这个装置塞给了你。现在你是一站式消息的接收者。"
    scene darkside1_24 with Dissolve(0.3)
    asami 4 "它就像来自上帝的短信——只不过你祈祷，而祂保持沉默。只管读，别浪费脑子去想着回复。" with Dissolve(0.3)
    scene darkside1_25 with Dissolve(0.3)
    asami 4 "这个维度是个活生生的噩梦。它隔几里外就能闻到新来的气味，最爱击碎那些还没意识到自己在面对什么的人。" with Dissolve(0.3)
    asami 4 "第一次永远特别。这个世界会把你深埋在心底的所有烂事都拖出来。"
    scene darkside1_26 with Dissolve(0.3)
    asami 4 "它会逼你选择。逼你做出在正常生活里绝不敢做的事。活下来的不是最强的，而是最懂得适应的。" with Dissolve(0.3)
    asami 4 "如果它没击碎你的精神，就会吞噬你的身体。所以如果你能撑过第一轮，就当你走了狗屎运。"
    scene darkside1_27 with Dissolve(0.3)
    gg 16 "（可恶……你就这么爱把我丢在这种鬼地方，是吧？）" with Dissolve(0.3)
    scene darkside1_28 with Dissolve(0.3)
    asami 4 "现在仔细听好。" with Dissolve(0.3)
    asami 4 "暗界是一张腐烂的空间网络，每一处都有自己的规则——有时蠢得离谱。"
    scene darkside1_29 with Dissolve(0.3)
    asami 4 "有些区域正在崩塌，有些则刚刚诞生。" with Dissolve(0.3)
    asami 4 "一切都在流动，一切都在变化。它们之间的通道只对拥有灵魂石的人开放。"
    asami 4 "你掉进来的那个传送门，通往我去过的一个区域。如果路线没有偏移，你就被困住了。字面意义上的。"
    asami 4 "这一带布满压力板、绊线和感应机关。踩错一步你就完了。"
    scene darkside1_30 with Dissolve(0.3)
    asami 4 "这里的一切都想碾碎你。" with Dissolve(0.3)
    asami 4 "所以打起精神吧，机器人。你要是能出去——我们还会再见。"
    scene darkside1_31 with Dissolve(0.3)
    gg 16 "（机器人……？）" with Dissolve(0.3)
    gg 16 "（对[may]来说我是一张石面脸，对这位来说我是机器人。）"
    scene darkside1_32 with Dissolve(0.3)
    gg 16 "（懂了，红眼睛。你早说这些我就不用在楼顶被你推下去了。）" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=5, channel=u'music3')
    
    scene darkside1_33 with Dissolve(0.3)
    gg 16 "（不过……你要是不说，我可能也不会在这儿。）" with Dissolve(0.3)
    
    play sound2 fs_ext_up_concrete_steps volume 0.4 loop
    play sound3 floor_board_creaks_ody loop
    
    scene darkside1_34 with Dissolve(0.3)
    pause 1.5
    
    stop sound2 fadeout 0.3
    stop sound3 fadeout 0.3
    
    scene darkside1_35 with Dissolve(0.3)
    gg 16 "（那边……是一条走廊。看起来是唯一的出路……如果那真是出口的话。）" with Dissolve(0.3)
    scene darkside1_36 with Dissolve(0.3)
    gg 16 "（可我要怎么过去……？）" with Dissolve(0.3)
    scene darkside1_37 with Dissolve(0.3)
    gg 16 "（认真的吗……我得一直踩在这些木板上走？）" with Dissolve(0.3)
    
    play sound2 fs_ext_up_concrete_steps volume 0.4 loop
    play sound3 floor_board_creaks_ody loop
    
    scene darkside1_38 with Dissolve(0.3)
    pause 1.5
    scene darkside1_39 with Dissolve(0.3)
    
    stop sound2 fadeout 0.3
    stop sound3 fadeout 0.3
    
    gg 16 "（这里的一切一百年前就烂掉了。踩错一步我就会成为这些废墟的一部分。）" with Dissolve(0.3)
    scene darkside1_40 with Dissolve(0.3)
    gg 16 "（操……我离地有多高？）" with Dissolve(0.3)
    scene darkside1_41 with Dissolve(0.3)
    gg 16 "（这座塔简直像个无底洞。）" with Dissolve(0.3)
    scene darkside1_42 with Dissolve(0.3)
    gg 16 "（看不见天空，窗户被厚厚的浓雾封住。）" with Dissolve(0.3)
    
    play sound2 fs_ext_up_concrete_steps volume 0.4
    
    scene darkside1_43 with Dissolve(0.3)
    pause 1.5
    
    stop sound2 fadeout 0.3
    
    scene darkside1_44 with Dissolve(0.3)
    gg 16 "（这条走廊会把我带到哪里？）" with Dissolve(0.3)
    
    play music2 sci_fi_creepy_cave_background_ambience_loop_1 fadein 5
    $ renpy.music.set_volume(0.3, delay=3, channel=u'music3')
    
    scene darkside1_45 with Dissolve(0.3)
    gg 16 "（这个世界不解释规则……算了，我配合就是。看来得自己读出言外之意。）" with Dissolve(0.3)
    scene darkside1_46 with Dissolve(0.3)
    gg 16 "（陷阱肯定就在附近。我一个都还没看见，这反而让我紧张。）" with Dissolve(0.3)
    gg 16 "（但撞上信徒或恶魔更糟。他们看见我大概会当成菜鸟。不过也许这样反而好？）"
    scene darkside1_47 with Dissolve(0.3)
    gg 16 "（他们会轻视我，我也许能打个措手不及。但说真的，我现在能做什么？）" with Dissolve(0.3)
    gg 16 "（一双拳头和一把枪。够用吗？）"
    scene darkside1_48 with Dissolve(0.3)
    gg 16 "（不用能力的话，我在这儿就是块肉。）" with Dissolve(0.3)
    gg 16 "（希望别碰上人。可我为什么会来这儿？）"
    scene darkside1_49 with Dissolve(0.3)
    gg 16 "（总之，只有他们先动手我才会先动手。）" with Dissolve(0.3)
    gg 16 "（碰上演员更糟。先装友好，然后从背后捅刀。）"
    gg 16 "（希望只有这一个空间是这副德行。闻着就像个乱葬岗。）"
    show darkside1_50 with Dissolve(0.3)
    $ renpy.pause(7, hard=True)
    
    $ renpy.music.set_volume(0.3, delay=3, channel=u'music3')
    play sound horror_shock_appearance_2
    
    $ renpy.pause(0.8, hard=True)
    
    
    scene darkside1_51 with Dissolve(0.1)
    gg 16 "（搞什么……？）" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.6, delay=5, channel=u'music3')
    
    scene darkside1_52 with Dissolve(0.3)
    gg 16 "（我绕回原地了吗？跟我进走廊时看到的一模一样。）" with Dissolve(0.3)
    gg 16 "（要是有出路，我一定能找到。就算得砸穿一堵墙。）"
    
    stop music2 fadeout 5
    
    show darkside1_53 with Dissolve(0.3)
    $ renpy.pause(6.4, hard=True)
    
    scene darkside1_54 with Dissolve(0.1)
    gg 16 "（那大概不是出口……不过看起来也没有别的路。）" with Dissolve(0.3)
    
    show darkside1_55 with Dissolve(0.1)
    $ renpy.pause(2.6, hard=True)
    
    play sound sharp_horror_hit_1
    
    $ renpy.pause(1, hard=True)
    
    scene darkside1_56 with Dissolve(0.1)
    gg 16 "（我操！又一具尸体？到底有多少具？）" with Dissolve(0.3)
    gg 16 "（这地方好像专收尸体。）"
    scene darkside1_57 with Dissolve(0.3)
    gg 16 "（如果他还活着，一定虚弱得厉害。）" with Dissolve(0.3)
    scene darkside1_58 with Dissolve(0.3)
    gg 16 "（他所有装备都散在旁边，而且没拿武器。大概吧。）" with Dissolve(0.3)
    scene darkside1_59 with Dissolve(0.3)
    gg 16 "（步枪肯定没上弹，弹匣不见了。）" with Dissolve(0.3)
    scene darkside1_60 with Dissolve(0.3)
    gg 16 "（我不是第一次见这种东西。这就是[asami]提过的灵魂石吗？）" with Dissolve(0.3)
    gg 16 "（他旁边有一把砍刀。我靠近的话，他应该没时间用。）"
    scene darkside1_61 with Dissolve(0.3)
    pause 0.3
    
    menu:
        "跟他说话\\n[gr](推荐)":
            gg 16 "你还活着吗？" with Dissolve(0.3)
            gg 16 "{cps=5}……{/cps}"
            gg 16 "你不介意的话我靠近一点。"
            scene darkside1_62 with Dissolve(0.3)
            gg 16 "（他好像已经死了。）" with Dissolve(0.3)
            
            $ darkside1_stranger_talk = True
            
            scene darkside1_63 with hpunch
            ds_stranger1 1 "咳咳哈……" with Dissolve(0.3)
            
        "靠近":
            scene darkside1_67 with Dissolve(0.3)
            gg 16 "（空枪没什么用。）" with Dissolve(0.3)
            scene darkside1_68 with Dissolve(0.3)
            gg 16 "（但那把砍刀说不定还派得上用场。）" with Dissolve(0.3)
            scene darkside1_69 with Dissolve(0.3)
            gg 16 "（还有这个会发光的东西……你到底是什么？）" with Dissolve(0.3)
            scene darkside1_70 with Dissolve(0.3)
            gg 16 "（为什么我觉得你不只是个小摆件？）" with Dissolve(0.3)
            gg 16 "（值得仔细看看。）"
            scene darkside1_71 with Dissolve(0.3)
            gg 16 "（我记得[asami]曾经当着我的面用过两次类似的发光石块。）" with Dissolve(0.3)
            
            play sound3 sub_woosh
            $ renpy.music.set_volume(0.2, delay=1, channel=u'music3')
            
            scene black with Dissolve(0.6)
            pause 0.5
            scene darkside1_90_1 with Dissolve(1.0)
            gg 16 "（第一次是那天晚上，在街上。她把石块扔到一边，闪了一下，升起烟雾，传送门就在她面前打开。）" with Dissolve(0.3)
            gg 16 "（跟我十分钟前从楼顶掉进去的那个一模一样。）"
            
            $ renpy.music.set_volume(0.6, delay=3, channel=u'music3')
            
            scene black with Dissolve(0.3)
            pause 0.3
            scene darkside1_71 with Dissolve(0.5)
            gg 16 "（等等……而在那之前……她也扔过一块这样的石块。这不可能是巧合吧？）" with Dissolve(0.3)
            show darkside1_72
            $ renpy.pause(0.8, hard=True)
            
            $ renpy.music.set_volume(0.2, delay=0.2, channel=u'music3')
            play sound cinematic_hit_bell_hits_horror_1 volume 2
            
            $ renpy.pause(0.2, hard=True)
            
            scene darkside1_73_1 with Dissolve(0.1)
            pause 0.3
            
            $ renpy.music.set_volume(0.6, delay=5, channel=u'music3')
            
            scene darkside1_73 with Dissolve(1.0)
            pause 0.5

    if darkside1_stranger_talk == True:
        scene darkside1_64 with Dissolve(0.3)
    else:
        scene darkside1_74 with Dissolve(0.3)
    ds_stranger1 1 "{cps=5}……{/cps}"
    
    if darkside1_stranger_talk == True:
        scene darkside1_65 with Dissolve(0.3)
        pause 0.7
    else:
        pause 0.1
    
    if darkside1_stranger_talk == True:
        scene darkside1_66 with Dissolve(0.3)
    else:
        scene darkside1_75 with Dissolve(0.3)
    ds_stranger1 1 "现、现在……它归你了……" with Dissolve(0.3)
    
    scene darkside1_76 with Dissolve(0.3)
    gg 16 "你为什么把这个给我？" with Dissolve(0.3)
    scene darkside1_77 with Dissolve(0.3)
    ds_stranger1 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene darkside1_78 with Dissolve(0.3)
    pause 0.8
    scene darkside1_79 with Dissolve(0.3)
    pause 1.3
    scene darkside1_80 with Dissolve(0.3)
    pause 0.8
    scene darkside1_81 with Dissolve(0.3)
    pause 1
    scene darkside1_82 with Dissolve(0.3)
    "那个陌生人把砍刀扔进了深渊，它消失在雾里，仿佛从未存在过。没有回声，没有落地的声响——只有一片死寂。"
    scene darkside1_83 with Dissolve(0.3)
    pause 1
    scene darkside1_84 with Dissolve(0.3)
    gg 16 "喂，你打算干什么？" with Dissolve(0.3)
    scene darkside1_85 with Dissolve(0.3)
    pause 1
    scene darkside1_86 with Dissolve(0.3)
    pause 0.5
    
    show darkside1_87 with Dissolve(0.3)
    $ renpy.pause(9.5, hard=True)
    
    scene darkside1_88 with Dissolve(0.3)
    gg 16 "可恶……" with Dissolve(0.3)
    scene darkside1_89 with Dissolve(0.3)
    gg 16 "（这石头是有什么诅咒吗？）" with Dissolve(0.3)
    
    if darkside1_stranger_talk == True:
        scene darkside1_90 with Dissolve(0.3)
        gg 16 "（我记得[asami]曾经当着我的面用过两次类似的发光石块。）" with Dissolve(0.3)
        
        play sound3 sub_woosh
        $ renpy.music.set_volume(0.2, delay=1, channel=u'music3')
        
        scene black with Dissolve(0.6)
        pause 0.3
        scene darkside1_90_1 with Dissolve(1.0)
        gg 16 "（第一次是那天晚上，在街上。她把石块扔到一边，闪了一下，升起烟雾，传送门就在她面前打开。）" with Dissolve(0.3)
        gg 16 "（跟我十分钟前从楼顶掉进去的那个一模一样。）"
        
        $ renpy.music.set_volume(0.6, delay=3, channel=u'music3')
        
        scene black with Dissolve(0.3)
        pause 0.3
        scene darkside1_90 with Dissolve(0.5)
        gg 16 "（等等……而在那之前……她也扔过一块这样的石块。这不可能是巧合吧？）" with Dissolve(0.3)
        pause 0.3
    else:
        pause 0.1
        
    scene darkside1_91 with Dissolve(0.3)
    gg 16 "（你为什么要把它给我……？）" with Dissolve(0.3)
    
    play music2 horror_background_noise_loop fadein 5
    stop music3 fadeout 10
    
    scene darkside1_92 with Dissolve(1.0)
    pause 2
    scene darkside1_93 with Dissolve(0.3)
    "我沿着黑暗的走廊缓缓前行，在昏暗的空间里努力辨认。"
    scene darkside1_94 with Dissolve(0.3)
    gg 16 "（这里好像只有我一个人。）" with Dissolve(0.3)
    
    play sound2 plate_push_away_1
    
    scene darkside1_95 with vpunch
    pause 0.6
    
    play sound6 horror_shock_appearance_2
    
    show darkside1_96 with Dissolve(0.05)
    $ renpy.pause(0.25, hard=True)
    
    play sound3 metal_stone_ancient_trap_full
    
    $ renpy.pause(0.25, hard=True)
    
    play sound sword_whoosh volume 2
    
    $ renpy.pause(0.5, hard=True)

    play sound4 fire_trap_1 volume 2
    
    $ renpy.pause(1, hard=True)
    
    play sound5 fire_loop_burning_spark_flame_3 loop fadein 2 volume 0.5
    
    show darkside1_97 with Dissolve(0.1)
    hide darkside1_96
    gg 16 "（可恶！）" with Dissolve(0.3)
    gg 16 "（[asami]警告过我这里布满陷阱……但没告诉我陷阱在哪儿。真棒。真他妈有用的信息！）"
    
    play sound plate_push_away_2
    play music3 action_thriller_suspense_horror_loop_2
    stop music2 fadeout 2
    
    scene darkside1_98 with vpunch
    pause 0.6
    scene darkside1_99 with Dissolve(0.3)
    gg 16 "（现在每一步都有陷阱？！）" with Dissolve(0.3)
    scene darkside1_100 with Dissolve(0.3)
    gg 16 "（我要怎么走过去？）" with Dissolve(0.3)
    scene darkside1_101 with Dissolve(0.3)
    gg 16 "...!" with Dissolve(0.1)
    scene darkside1_102 with Dissolve(0.3)
    gg 16 "（什么玩意儿？！）" with Dissolve(0.1)
    
    play music2 action_thriller_suspense_horror_loop_1
    stop music3 fadeout 2
    stop sound5 fadeout 1
    play sound2 soundjay_fire_main_1
    play sound3 building_fire fadein 3 loop
    
    $ renpy.music.set_volume(1, delay=0, channel=u'music3')
    
    show darkside1_103 with Dissolve(0.05)
    $ renpy.pause(1.3, hard=True)
    
    play sound fire_trap_2
    
    scene darkside1_104 with hpunch
    pause 1
    scene darkside1_105 with Dissolve(0.1)
    pause 0.3
    
    play sound4 fire_trap_3
    play sound7 dsgnbass_clock_wind_down_slomo
    
    show darkside1_106 with Dissolve(0.05)
    $ renpy.pause(2.5, hard=True)
    
    play sound cinematic_woosh_1
    
    $ renpy.pause(4, hard=True)
    
    play sound6 weapon_trap_flamethrower_burst_fire_mid_flame_blast_long_1
    
    $ renpy.pause(3, hard=True)
    
    play sound heavy_body_fall_02
    
    scene darkside1_107 with vpunch
    pause 1.5
    
    play sound fire_trap_2
    
    scene darkside1_108 with Dissolve(0.3)
    pause 1.2
    
    play sound fire_trap_3
    
    scene darkside1_109 with Dissolve(0.3)
    pause 0.9
    scene darkside1_110 with Dissolve(0.3)
    pause 0.7
    
    stop sound3 fadeout 10
    
    play sound3 horror_shock_appearance_3
    
    show darkside1_111 with Dissolve(0.05)
    $ renpy.pause(1, hard=True)
    
    play sound4 mobile_game_action_arrow_trap_1 volume 2
    
    $ renpy.pause(2, hard=True)
    
    scene darkside1_112 with hpunch
    gg 18 "（金属箭？！）" with Dissolve(0.1)
    scene darkside1_113 with Dissolve(0.3)
    gg 18 "（我得贴着墙……小心移动。）" with Dissolve(0.3)
    scene darkside1_114 with Dissolve(0.3)
    gg 18 "（最重要的是别再触发更多……）" with Dissolve(0.3)
    scene darkside1_115 with Dissolve(0.3)
    pause 1
    
    play sound5 mobile_game_action_arrow_trap_1 volume 1
    
    scene darkside1_116 with hpunch
    pause 1
    
    play sound blood_gore_impact_3
    
    scene darkside1_117 with hpunch
    pause 1
    
    play music3 action_thriller_suspense_horror_loop_3 fadein 0.3
    stop music2 fadeout 5
    
    scene darkside1_118 with hpunch
    gg 18 "啊啊啊啊！" with Dissolve(0.1)
    scene darkside1_119 with hpunch
    gg 18 "可恶……该死！" with Dissolve(0.1)
    scene darkside1_120 with Dissolve(0.3)
    gg 18 "（疼痛贯穿全身……）" with Dissolve(0.3)
    scene darkside1_121 with Dissolve(0.3)
    gg 18 "（呼吸很困难，但我不能倒下。）" with Dissolve(0.3)
    
    stop music3 fadeout 15
    play music2 horror_background_noise_loop fadein 5
    play sound2 wooden_stick_crack_break
    
    scene darkside1_122 with Dissolve(0.3)
    pause 1
    scene darkside1_123 with Dissolve(0.3)
    pause 0.8
    scene darkside1_124 with Dissolve(0.3)
    pause 1
    
    play sound blood_gore_impact_6 volume 0.3
    
    scene darkside1_125 with Dissolve(0.3)
    gg 18 "哈啊……哈啊……" with Dissolve(0.1)
    scene darkside1_126 with Dissolve(0.3)
    gg 18 "（我知道暗界凶险万分，但这……这也太过分了。）" with Dissolve(0.3)
    scene darkside1_127 with Dissolve(0.3)
    gg 18 "（要是这样下去……其他信徒到底是怎么过来的？）" with Dissolve(0.3)
    scene darkside1_128 with Dissolve(0.3)
    gg 18 "（这到底是什么鬼东西？！）" with Dissolve(0.3)
    scene darkside1_129 with Dissolve(0.3)
    gg 18 "{cps=5}……{/cps}"
    scene darkside1_130 with Dissolve(0.3)
    gg 18 "（前面又一个出口。拜托别是另一个陷阱……）" with Dissolve(0.3)
    
    show darkside1_132 with Dissolve(0.3)
    $ renpy.pause(5.5, hard=True)
    
    scene darkside1_131 with Dissolve(0.3)
    gg 18 "（刚才那是什么声音？！）" with Dissolve(0.3)
    
    scene darkside1_133 with Dissolve(0.3)
    gg 18 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    play sound clothes_5
    
    scene darkside1_134 with Dissolve(0.3)
    
    play sound clothes_2
    
    pause 0.7
    
    scene darkside1_135 with Dissolve(0.3)
    gg 18 "（好像在响应什么……）" with Dissolve(0.3)
    scene darkside1_136 with Dissolve(0.3)
    gg 18 "（看起来很眼熟。）" with Dissolve(0.3)
    scene darkside1_137 with Dissolve(0.3)
    gg 18 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene darkside1_138 with Dissolve(0.3)
    gg 18 "（原来她当时就是这么用的，对吧？）" with Dissolve(0.3)
    
    show darkside1_139 with Dissolve(0.3)
    $ renpy.pause(0.7, hard=True)
    
    play sound3 lost_in_space_transition_full
    
    $ renpy.pause(4.7, hard=True)
    
    play sound4 walking_1 volume 0.2 loop
    
    $ renpy.pause(3, hard=True)
    
    stop music2 fadeout 10
    play music3 mystery_ethereal_background_loop_full fadein 5
    
    $ renpy.pause(3, hard=True)
    
    stop sound4
    
    scene darkside1_140 with Dissolve(0.1)
    "我面前是一片辽阔的、被浓雾笼罩的空间。"
    "乍一看空无一物，但圆圈中央立着一个可疑的身影。"
    scene darkside1_141 with Dissolve(1.0)
    "人形。一动不动，像座雕像。"
    gg 0 "（信徒？还是……别的什么？可他在这里干什么？）" with Dissolve(0.3)
    gg 0 "（他在盯着什么？……四周都是废墟，但他的目光固定在唯一还完整的那道拱门上。）"
    scene darkside1_142 with Dissolve(0.3)
    gg 0 "（要是我把发光的石块扔到那儿，应该就能打开通往别处的传送门。）" with Dissolve(0.3)
    gg 0 "（考虑到我是怎么来到这儿的，这完全有可能……）"
    scene darkside1_143 with Dissolve(0.3)
    gg 0 "（可他妈的怎么回事？他身后有扇门？！）" with Dissolve(0.3)
    gg 0 "（说真的，那扇门也通向另一个世界吗？）"
    gg 0 "（这里不对劲……不。这里的一切都他妈彻底乱套了！）"
    scene darkside1_144 with Dissolve(0.3)
    gg 0 "（他甚至对我的存在毫无反应。）" with Dissolve(0.3)
    scene darkside1_145 with Dissolve(0.3)
    gg 0 "（而且我好像回不去了。我踏过门槛的那一刻，回去的路就真的消失了。）" with Dissolve(0.3)
    
    play sound pistol_1
    
    scene darkside1_146 with Dissolve(0.3)
    pause 1
    
    play sound pistol_2
    
    scene darkside1_147 with Dissolve(0.3)
    pause 0.8
    scene darkside1_148 with Dissolve(0.3)
    pause 0.2
    
    menu:
        "靠近他\\n[gr](推荐)":
            gg 0 "（我得弄清他是谁，在这里干什么。）" with Dissolve(0.3)
            scene darkside1_149 with hpunch
            gg 0 "喂！" with Dissolve(0.1)
            scene darkside1_150 with Dissolve(0.3)
            gg 0 "你是谁？" with Dissolve(0.3)
            scene darkside1_150_1 with Dissolve(0.3)
            pause 0.1
            $ darkside1_approach_wanchan = True
            
            play sound5 walking_1 loop volume 0.3
            
            show darkside1_151 with Dissolve(0.05)
            $ renpy.pause(7, hard=True)
            
            stop sound5
            play sound4 horror_hit_sharp_stab_distorted_ring_bullet_harsh_bright_impact_1
            play sound2 horror_shock_appearance_4
            
            $ renpy.pause(1, hard=True)
            
            
        "从他身边走过":
            scene darkside1_149 with Dissolve(0.3)
            gg 0 "（谁知道这家伙是谁、在干什么。最好别惹上他，悄悄走过去就是。）" with Dissolve(0.3)
            scene darkside1_150_1 with Dissolve(0.3)
            pause 0.1
            
            play sound5 walking_2 loop volume 0.3
            
            show darkside1_221 with Dissolve(0.05)
            $ renpy.pause(6.5, hard=True)
            
            play sound6 walking_1 loop volume 0.3
            stop sound5
            
            $ renpy.pause(5, hard=True)
            
            play sound5 walking_2 loop volume 0.3
            stop sound6
            
            $ renpy.pause(1, hard=True)
            
            stop sound5
            
            scene darkside1_222 with Dissolve(0.1)
            gg 0 "（他去哪儿了？）" with Dissolve(0.3)
            
            show darkside1_223 with Dissolve(0.05)
            $ renpy.pause(1, hard=True)
            
            scene darkside1_224 with Dissolve(0.1)
            gg 0 "{cps=5}……{/cps}"
            
            show darkside1_225 with Dissolve(0.05)
            $ renpy.pause(0.6, hard=True)
            
            play sound4 horror_hit_sharp_stab_distorted_ring_bullet_harsh_bright_impact_1
            play sound2 horror_shock_appearance_4
            
            $ renpy.pause(0.4, hard=True)
            
    play sound3 scary_male_evil_laugh
    stop music3 fadeout 10
    play music4 mysterygame_loop fadein 10
    
    if darkside1_approach_wanchan == True:
        scene darkside1_152 with hpunch
    else:
        scene darkside1_226 with hpunch
        
    wanchan 1 "哈哈哈哈哈哈！" with Dissolve(0.1)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_153 with Dissolve(0.3)
    else:
        scene darkside1_227 with Dissolve(0.3)
        
    wanchan 1 "这么晚还有客人。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_154 with Dissolve(0.3)
    else:
        scene darkside1_228 with Dissolve(0.3)
    
    wanchan 1 "没想到还能见到活人。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_155 with Dissolve(0.3)
    else:
        scene darkside1_229 with Dissolve(0.3)
    
    wanchan 1 "我几乎以为再也见不到活人穿过这些墙了。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_156 with Dissolve(0.3)
    else:
        scene darkside1_230 with Dissolve(0.3)
    
    wanchan 1 "能在这种地方遇见迷途者，可不常见。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_157 with Dissolve(0.3)
    else:
        scene darkside1_231 with Dissolve(0.3)
    
    wanchan 1 "不过，不过！不过我们别做突然的动作，好吗？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_158 with Dissolve(0.3)
    else:
        scene darkside1_232 with Dissolve(0.3)
    
    wanchan 1 "不管我看起来多么和善，只要你还用那把格洛克指着我……" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_159 with Dissolve(0.3)
    else:
        scene darkside1_233 with Dissolve(0.3)
    
    wanchan 1 "哦，我可怜的心都要碎了。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_160 with Dissolve(0.3)
    else:
        scene darkside1_234 with Dissolve(0.3)
    
    wanchan 2 "能不能麻烦你把那坨垃圾从我眼前拿走？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_161 with Dissolve(0.3)
    else:
        scene darkside1_235 with Dissolve(0.3)
    
    pause 0.3
    menu:
        "放下枪\\n[gr](推荐)":
            pause 0.1
        "离开":
            $ darkside1_wanchan_leave = True
            jump darkside1_wanchan_leave
    
    if darkside1_approach_wanchan == True:
        scene darkside1_162 with Dissolve(0.3)
    else:
        scene darkside1_236 with Dissolve(0.3)
    
    pause 1
    
    if darkside1_approach_wanchan == True:
        scene darkside1_163 with Dissolve(0.3)
    else:
        scene darkside1_237 with Dissolve(0.3)
        
    wanchan 1 "啊，我的礼貌呢！" with Dissolve(0.3)
        
    if darkside1_approach_wanchan == True:
        scene darkside1_164 with Dissolve(0.3)
    else:
        scene darkside1_238 with Dissolve(0.3)
    
    wanchan 1 "容我自我介绍一下：我是一名游商。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_165 with Dissolve(0.3)
    else:
        scene darkside1_239 with Dissolve(0.3)
        
    wanchan 1 "为迷途灵魂引路，为绝望之人指路，也是这条走廊的守护者。" with Dissolve(0.3)
        
    if darkside1_approach_wanchan == True:
        scene darkside1_166 with Dissolve(0.3)
    else:
        scene darkside1_240 with Dissolve(0.3)
    
    wanchan 1 "或许我们的相遇是命运本身的安排。不过你看起来……很紧绷。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_167 with Dissolve(0.3)
    else:
        scene darkside1_241 with Dissolve(0.3)
    
    wanchan 1 "我该提高警惕吗？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_168 with Dissolve(0.3)
    else:
        scene darkside1_242 with Dissolve(0.3)
        
    gg 0 "你有事就直说，别绕弯子。" with Dissolve(0.3)
        
    if darkside1_approach_wanchan == True:
        scene darkside1_169 with Dissolve(0.3)
    else:
        scene darkside1_243 with Dissolve(0.3)
    
    wanchan 1 "哦！原来是位绅士，我看得出来！" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_170 with Dissolve(0.3)
    else:
        scene darkside1_244 with Dissolve(0.3)
        
    wanchan 1 "刚才我还以为你只是又一个觊觎着自己控制不了的力量的混小子。" with Dissolve(0.3)
        
    if darkside1_approach_wanchan == True:
        scene darkside1_171 with Dissolve(0.3)
    else:
        scene darkside1_245 with Dissolve(0.3)
    
    wanchan 1 "我不记得你的脸，但从你的姿态看……你不是新手。这很好。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_172 with Dissolve(0.3)
    else:
        scene darkside1_246 with Dissolve(0.3)
        
    wanchan 1 "这条走廊……是起始区域与其他人通常栖身之处之间的通道……" with Dissolve(0.3)
        
    if darkside1_approach_wanchan == True:
        scene darkside1_173 with Dissolve(0.3)
    else:
        scene darkside1_247 with Dissolve(0.3)
    
    wanchan 1 "不过，也许你早就知道了？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_174 with vpunch
    else:
        scene darkside1_248 with vpunch
        
    wanchan 1 "哈哈哈哈！你当然知道！" with Dissolve(0.3)
        
    if darkside1_approach_wanchan == True:
        scene darkside1_175 with Dissolve(0.3)
    else:
        scene darkside1_249 with Dissolve(0.3)
    
    wanchan 1 "抱歉……太久没有客人，我一时忍不住想说点深刻的话。" with Dissolve(0.3)
    wanchan 1 "我完全不知道你是怎么来到这儿的。这条路对大多数人都是关闭的……"
    
    if darkside1_approach_wanchan == True:
        scene darkside1_176 with Dissolve(0.3)
    else:
        scene darkside1_250 with Dissolve(0.3)
    
    wanchan 1 "但既然它为你打开，就说明你有钥匙。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_177 with Dissolve(0.3)
    else:
        scene darkside1_251 with Dissolve(0.3)
        
    wanchan 1 "要是你需要什么，我随时效劳！" with Dissolve(0.3)
        
    if darkside1_approach_wanchan == True:
        scene darkside1_178 with Dissolve(0.3)
    else:
        scene darkside1_252 with Dissolve(0.3)
    
    gg 0 "我明白了……我有个问题想问你。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_179 with Dissolve(0.3)
    else:
        scene darkside1_253 with Dissolve(0.3)
        
    wanchan 1 "要是对我好奇，我建议你别浪费时间。" with Dissolve(0.3)
        
    if darkside1_approach_wanchan == True:
        scene darkside1_180 with Dissolve(0.3)
    else:
        scene darkside1_254 with Dissolve(0.3)
    
    gg 0 "你替谁做事？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_181 with Dissolve(0.3)
    else:
        scene darkside1_255 with Dissolve(0.3)
    
    wanchan 1 "啊，是我疏忽了……准确地说，我并不为谁做事……" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_182 with Dissolve(0.3)
    else:
        scene darkside1_256 with Dissolve(0.3)
    
    wanchan 1 "我只是存在。存在是为了侍奉那宏大的暗之维度——世界之间无尽的虚空。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_183 with Dissolve(0.3)
    else:
        scene darkside1_257 with Dissolve(0.3)
    
    wanchan 1 "还有，请不要把我和那些设局玩游戏的人混为一谈。我们毫无共同之处。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_184 with Dissolve(0.3)
    else:
        scene darkside1_258 with Dissolve(0.3)
    
    gg 0 "（我完全不知道他在说谁。）" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_185 with Dissolve(0.3)
    else:
        scene darkside1_259 with Dissolve(0.3)
    
    gg 0 "给我看看你卖什么。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_186 with Dissolve(0.3)
    else:
        scene darkside1_260 with Dissolve(0.3)
    
    wanchan 1 "我有各种场合用的各式道具，还有许多像这条一样的隐秘路线情报。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_187 with Dissolve(0.3)
    else:
        scene darkside1_261 with Dissolve(0.3)
    
    wanchan 1 "全看你有多少灵魂石……最字面意义上的。你有多少？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_188 with Dissolve(0.3)
    else:
        scene darkside1_262 with Dissolve(0.3)
    
    wanchan 1 "给我看看，我会按你的财力量身搭配。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_189 with Dissolve(0.3)
    else:
        scene darkside1_263 with Dissolve(0.3)
    
    wanchan 1 "任何秘密都能用你的灵魂来换！" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_190 with Dissolve(0.3)
    else:
        scene darkside1_264 with Dissolve(0.3)
    
    gg 0 "做买卖的方式真怪。你就不能直接报个价？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_191 with Dissolve(0.3)
    else:
        scene darkside1_265 with Dissolve(0.3)
    
    "商人缓缓微笑，眼底却闪过一丝阴影。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_192 with Dissolve(0.3)
    else:
        scene darkside1_266 with Dissolve(0.3)
    
    wanchan 1 "你太急躁了，迷途者。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_193 with Dissolve(0.3)
    else:
        scene darkside1_267 with Dissolve(0.3)
    
    wanchan 1 "我可不是普通的商人。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_194 with Dissolve(0.3)
    else:
        scene darkside1_268 with Dissolve(0.3)
    
    wanchan 1 "我提供的不是商品，而是机会！" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_195 with Dissolve(0.3)
    else:
        scene darkside1_269 with Dissolve(0.3)
    
    wanchan 1 "我们毕竟还只是初识，就让我确认一下你并非一个空壳。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_196 with Dissolve(0.3)
    else:
        scene darkside1_270 with Dissolve(0.3)
    
    gg 0 "随便。说点别的区域吧。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_197 with Dissolve(0.3)
    else:
        scene darkside1_271 with Dissolve(0.3)
    
    wanchan 1 "嗯？你对世界之间的门感兴趣？" with Dissolve(0.3)
    "商人微微歪头，像是在权衡要不要继续。"
    
    if darkside1_approach_wanchan == True:
        scene darkside1_198 with Dissolve(0.3)
    else:
        scene darkside1_272 with Dissolve(0.3)
    
    wanchan 1 "这么说吧……" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_199 with Dissolve(0.3)
    else:
        scene darkside1_273 with Dissolve(0.3)
    
    wanchan 1 "每一个维度都是活的，有自己的性质、自己的法则。它们索取代价——任务、试炼、鲜血……" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_200 with Dissolve(0.3)
    else:
        scene darkside1_274 with Dissolve(0.3)
    
    wanchan 1 "每一个选择都会打开一条新路，同时关上一条旧路。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_201 with Dissolve(0.3)
    else:
        scene darkside1_275 with Dissolve(0.3)
    
    wanchan 2 "逗留太久——黑暗空间就会重置你所有的进度，重新制造障碍……" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_202 with Dissolve(0.3)
    else:
        scene darkside1_276 with Dissolve(0.3)
    
    wanchan 1 "这条规则并非处处适用，但我们的走廊包括在内。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_203 with Dissolve(0.3)
    else:
        scene darkside1_277 with Dissolve(0.3)
    
    wanchan 1 "不过，如果你有灵魂石的话……咳咳咳咳……" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_204 with Dissolve(0.3)
    else:
        scene darkside1_278 with Dissolve(0.3)
    
    wanchan 1 "你拥有的灵魂石越多，最后落到正确地方的机会就越大。它们能打开封印的门。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_205 with Dissolve(0.3)
    else:
        scene darkside1_279 with Dissolve(0.3)
    
    wanchan 1 "现在明白了吗？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_206 with Dissolve(0.3)
    else:
        scene darkside1_280 with Dissolve(0.3)
    
    gg 0 "（基本上都是[asami]写过的那些东西。）" with Dissolve(0.3)
    gg 0 "如果时间有限……我还有多少时间？"
    
    if darkside1_approach_wanchan == True:
        scene darkside1_207 with Dissolve(0.3)
    else:
        scene darkside1_281 with Dissolve(0.3)
    
    wanchan 1 "这么说吧……这条走廊已经四天没变过了。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_208 with Dissolve(0.3)
    else:
        scene darkside1_282 with Dissolve(0.3)
    
    wanchan 1 "我有个问题要问自己。迷途的你……是一个人来的吗？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_209 with Dissolve(0.3)
    else:
        scene darkside1_283 with Dissolve(0.3)
    
    gg 0 "你什么意思？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_210 with Dissolve(0.3)
    else:
        scene darkside1_284 with Dissolve(0.3)
    
    wanchan 1 "你的同伴在哪儿？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_211 with Dissolve(0.3)
    else:
        scene darkside1_285 with Dissolve(0.3)
    
    wanchan 1 "还是说他们已经不在人世了？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_212 with Dissolve(0.3)
    else:
        scene darkside1_286 with Dissolve(0.3)
    
    wanchan 1 "有时候独自旅行要安全得多。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_213 with Dissolve(0.3)
    else:
        scene darkside1_287 with Dissolve(0.3)
    
    gg 0 "（我觉得还是别再说下去。他是个疯子！我不敢想他会对更多问题作何反应。）" with Dissolve(0.3)
    
    jump darkside1_wanchan_leave
    
###### DARKSIDE - WANCHAN LEAVE

label darkside1_wanchan_leave:
    
    if darkside1_approach_wanchan == True:
        scene darkside1_214 with Dissolve(0.3)
    else:
        scene darkside1_288 with Dissolve(0.3)
    
    gg 0 "我得走了。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_215 with Dissolve(0.3)
    else:
        scene darkside1_289 with Dissolve(0.3)
    
    wanchan 1 "很好……我猜我们还会再见，迷途者。" with Dissolve(0.3)
    
    scene darkside1_216 with Dissolve(0.3)
    pause 1.5
    
    if darkside1_approach_wanchan == True:
        scene darkside1_217 with Dissolve(0.3)
    else:
        scene darkside1_290 with Dissolve(0.3)
    
    gg 0 "那扇门通向哪里？" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_218 with Dissolve(0.3)
    else:
        scene darkside1_291 with Dissolve(0.3)
    
    wanchan 1 "通往出口。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_219 with Dissolve(0.3)
    else:
        scene darkside1_292 with Dissolve(0.3)
    
    gg 0 "好的，谢谢。" with Dissolve(0.3)
    
    if darkside1_approach_wanchan == True:
        scene darkside1_220 with Dissolve(0.3)
    else:
        scene darkside1_293 with Dissolve(0.3)
    
    wanchan 1 "祝您狩猎愉快！" with Dissolve(0.3)
    
    scene darkside1_294 with Dissolve(0.3)
    pause 1
    play sound scary_male_i_wouldnt_do_that_with_evil_laugh
    wanchan 2 "我可不会那么做。哈哈哈！" with Dissolve(0.3)
    
    stop music4 fadeout 8
    
    show darkside1_295 with Dissolve(0.1)
    $ renpy.pause (4, hard=True)
    play music2 horror_screeches_loop_roomtone_layer fadein 8
    $ renpy.pause (3.5, hard=True)
    jump darkside1_corridor
    
###### DARKSIDE - 1 - CORRIDOR
    
label darkside1_corridor:

    play sound2 big_stadium_door_closing
    
    scene darkside1_corridor_1 with hpunch
    pause 0.3
    gg 0 "（门砰地关上了。我敢说回去的路已经对我关闭了。）" with Dissolve(0.3)
    scene darkside1_corridor_2 with Dissolve(0.3)
    gg 0 "（不过，总得继续往前走……）" with Dissolve(0.3)
    
    jump darkside1_corridor_w1_1
    
##############################################

label darkside1_corridor_w1_1:

    scene darkside1_corridor_lab_w1
    show darkside1_corridor_w1_1 with Dissolve(0.1)
    hide darkside1_corridor_w1_l_3
    
    call screen ds_corridor_w1

label darkside1_corridor_w1_l:

    scene darkside1_corridor_lab_w1
    show darkside1_corridor_w1_l_1 with Dissolve(0.1)
    hide darkside1_corridor_w1_1
    $ renpy.pause (0.7, hard=True)
    

    scene darkside1_corridor_lab_w1_l
    show darkside1_corridor_w1_l_2 with Dissolve(0.1)
    hide darkside1_corridor_w1_l_1 with Dissolve(0.1)
    
    ''
    $ ds_corridor_w1_l = True
    
    show darkside1_corridor_w1_l_3 with Dissolve(0.1)
    hide darkside1_corridor_w1_l_2
    $ renpy.pause (1.2, hard=True)
    
    jump darkside1_corridor_w1_1
    
label darkside1_corridor_w1_2:

    scene darkside1_corridor_lab_w1
    show darkside1_corridor_w1_2 with Dissolve(0.1)
    hide darkside1_corridor_w1_1
    $ renpy.pause (0.5, hard=True)
    play sound6 walking_2
    $ renpy.pause (3.5, hard=True)
    stop sound6
    $ renpy.pause (0.5, hard=True)

##############################################

label darkside1_corridor_w2_1:
    
    scene darkside1_corridor_lab_w2
    show darkside1_corridor_w2_1 with Dissolve(0.1)
    call screen ds_corridor_w2
    
label darkside1_corridor_w2_l:

    scene darkside1_corridor_lab_w2
    show darkside1_corridor_w2_l_1 with Dissolve(0.1)
    $ renpy.pause (1.2, hard=True)
    
    scene darkside1_corridor_lab_w2_l
    show darkside1_corridor_w2_l_2 with Dissolve(0.1)
    
    ''
    $ ds_corridor_w2_l = True
    
    show darkside1_corridor_w2_l_3 with Dissolve(0.1)
    hide darkside1_corridor_w2_l_2
    $ renpy.pause (1.2, hard=True)
    
    jump darkside1_corridor_w2_1

label darkside1_corridor_w2_r:
    
    scene darkside1_corridor_lab_w2
    show darkside1_corridor_w2_r_1 with Dissolve(0.1)
    $ renpy.pause (1.2, hard=True)
    
    scene darkside1_corridor_lab_w2_r
    show darkside1_corridor_w2_r_2 with Dissolve(0.1)
    
    ''
    $ ds_corridor_w2_r = True
    
    show darkside1_corridor_w2_r_3 with Dissolve(0.1)
    hide darkside1_corridor_w2_r_2
    $ renpy.pause (1.2, hard=True)
    
    jump darkside1_corridor_w2_1

label darkside1_corridor_w2_2:

    scene darkside1_corridor_lab_w2
    show darkside1_corridor_w2_2 with Dissolve(0.1)
    play sound2 paranormal_location
    $ renpy.pause (0.5, hard=True)
    play sound6 walking_2
    $ renpy.pause (4, hard=True)
    stop sound6
    $ renpy.pause (0.5, hard=True)
    
    jump darkside1_corridor_w3_1

##############################################

label darkside1_corridor_w3_1:

    scene darkside1_corridor_lab_w3
    show darkside1_corridor_w3_1 with Dissolve(0.1)
    
    call screen ds_corridor_w3

label darkside1_corridor_w3_l:

    scene darkside1_corridor_lab_w3
    show darkside1_corridor_w3_l_1 with Dissolve(0.1)
    $ renpy.pause (1.2, hard=True)
    
    scene darkside1_corridor_lab_w3_l
    show darkside1_corridor_w3_l_2 with Dissolve(0.1)
    
    ''
    $ ds_corridor_w3_l = True
    
    show darkside1_corridor_w3_l_3 with Dissolve(0.1)
    hide darkside1_corridor_w3_l_2
    $ renpy.pause (1.2, hard=True)
    
    jump darkside1_corridor_w3_1

label darkside1_corridor_w3_2:

    scene darkside1_corridor_lab_w3
    show darkside1_corridor_w3_2 with Dissolve(0.1)
    $ renpy.pause (0.5, hard=True)
    play sound6 walking_3
    $ renpy.pause (2, hard=True)
    stop sound6
    $ renpy.pause (0.5, hard=True)
    
    jump darkside1_corridor_w4_1

##############################################

label darkside1_corridor_w4_1:

    scene darkside1_corridor_lab_w4
    show darkside1_corridor_w4_1 with Dissolve(0.1)
    
    play sound3 horror_female_voice_cry_fearful
    ''
    
    scene darkside1_corridor_lab_w4
    show darkside1_corridor_w4_r_1 with Dissolve(0.1)
    $ renpy.pause (1.1, hard=True)
    
    scene darkside1_corridor_lab_w4_r
    show darkside1_corridor_w4_r_2 with Dissolve(0.1)
    
    ''
    
    scene darkside1_corridor_lab_w4_r
    show darkside1_corridor_w4_r_3 with Dissolve(0.1)
    $ renpy.music.set_volume(0.2, delay=0.5, channel=u'music2')
    $ renpy.pause (0.5, hard=True)
    play sound2 scary_double_hit volume 2
    $ renpy.pause (2, hard=True)
    $ renpy.music.set_volume(1, delay=2, channel=u'music2')
    
    scene darkside1_corridor_lab_w4
    show darkside1_corridor_w4_1 with Dissolve(0.1)
    
    pause 1.5
    gg 0 "（什么？！）" with Dissolve(0.1)
    pause 0.5
    
    scene darkside1_corridor_lab_w4
    show darkside1_corridor_w4_2 with Dissolve(0.1)
    $ renpy.pause (2.5, hard=True)

    scene darkside1_corridor_lab_w4_3
    show darkside1_corridor_w4_3 with Dissolve(0.1)
    
    pause 0.5
    gg 0 "...!" with Dissolve(0.1)
    pause 0.5
    
    show darkside1_corridor_w4_4 with Dissolve(0.1)
    hide darkside1_corridor_w4_3
    $ renpy.pause (0.5, hard=True)
    play sound6 walking_4
    $ renpy.pause (1.8, hard=True)
    stop sound6
    $ renpy.pause (0.5, hard=True)
    
    jump darkside1_corridor_w5_1
    
##############################################

label darkside1_corridor_w5_1:

    scene darkside1_corridor_lab_w5
    show darkside1_corridor_w5_1 with Dissolve(0.1)
    
    call screen ds_corridor_w5

label darkside1_corridor_w5_l:

    scene darkside1_corridor_lab_w5
    show darkside1_corridor_w5_l_1 with Dissolve(0.1)
    $ renpy.pause (1.2, hard=True)
    
    scene darkside1_corridor_lab_w5_l
    show darkside1_corridor_w5_l_2 with Dissolve(0.1)
    
    call screen ds_corridor_w5_l
    
label darkside1_corridor_w5_3:
    
    scene darkside1_corridor_lab_w5_l
    show darkside1_corridor_w5_l_3 with Dissolve(0.1)
    $ renpy.pause (1.2, hard=True)
    
    jump darkside1_corridor_w5_1

label darkside1_corridor_w5_2:

    scene darkside1_corridor_lab_w5
    show darkside1_corridor_w5_2 with Dissolve(0.1)
    $ renpy.pause (0.5, hard=True)
    play sound6 walking_4
    $ renpy.pause (3, hard=True)
    stop sound6
    $ renpy.pause (0.5, hard=True)
    
    jump darkside1_corridor_w6_1

label darkside1_corridor_w5_l2:
    
    scene darkside1_corridor_lab_w5_l
    show darkside1_corridor_w5_l2_1 with Dissolve(0.1)
    $ renpy.music.set_volume(0.2, delay=6, channel=u'music2')
    $ renpy.pause (0.5, hard=True)
    play sound6 walking_1
    $ renpy.pause (2, hard=True)
    stop sound6
    $ renpy.pause (0.5, hard=True)
    play sound4 mountain_audio_scary_scratch volume 1.5
    $ renpy.pause (3.2, hard=True)
    play sound5 cinematic_impact_horror_hit_01 volume 3
    $ renpy.music.set_volume(1, delay=3, channel=u'music2')
    $ renpy.pause (2, hard=True)
    
    scene darkside1_corridor_lab_w5_l_2
    show darkside1_corridor_w5_l2_2 with Dissolve(0.1)
    
    gg 0 "（可恶，那是什么？！）" with Dissolve(0.1)
    pause 0.5
    
    scene darkside1_corridor_lab_w5_l_2
    show darkside1_corridor_w5_l2_3 with Dissolve(0.1)
    $ renpy.pause (0.5, hard=True)
    play sound6 walking_2
    $ renpy.pause (5.3, hard=True)
    stop sound6
    $ renpy.pause (0.5, hard=True)
    
    jump darkside1_corridor_w6_1

##############################################

label darkside1_corridor_w6_1:
    
    scene darkside1_corridor_lab_w6
    show darkside1_corridor_w6_1 with Dissolve(0.1)
    play sound3 ghostly_paranormal_breath
    call screen ds_corridor_w6
    
label darkside1_corridor_w6_l:

    scene darkside1_corridor_lab_w6
    show darkside1_corridor_w6_l_1 with Dissolve(0.1)
    hide darkside1_corridor_w6_1
    $ renpy.pause (1.2, hard=True)
    
    scene darkside1_corridor_lab_w6_l
    show darkside1_corridor_w6_l_2 with Dissolve(0.1)
    hide darkside1_corridor_w6_l_1
    
    ''
    $ ds_corridor_w6_l = True
    
    show darkside1_corridor_w6_l_3 with Dissolve(0.1)
    hide darkside1_corridor_w6_l_2
    $ renpy.pause (1.2, hard=True)
    
    jump darkside1_corridor_w6_1

label darkside1_corridor_w6_r:
    
    scene darkside1_corridor_lab_w6
    show darkside1_corridor_w6_r_1 with Dissolve(0.1)
    hide darkside1_corridor_w6_1
    $ renpy.pause (1.2, hard=True)
    
    scene darkside1_corridor_lab_w6_r
    show darkside1_corridor_w6_r_2 with Dissolve(0.1)
    hide darkside1_corridor_w6_r_1
    
    ''
    $ ds_corridor_w6_r = True
    
    show darkside1_corridor_w6_r_3 with Dissolve(0.1)
    hide darkside1_corridor_w6_r_2
    $ renpy.pause (1.2, hard=True)
    
    jump darkside1_corridor_w6_1

label darkside1_corridor_w6_2:

    scene darkside1_corridor_lab_w6
    show darkside1_corridor_w6_2 with Dissolve(0.1)
    $ renpy.pause (0.5, hard=True)
    play sound6 walking_1
    $ renpy.pause (2, hard=True)
    stop sound6
    $ renpy.pause (0.5, hard=True)
    
    jump darkside1_corridor_w7_1

label darkside1_corridor_w7_1:

    scene darkside1_corridor_lab_w7
    show darkside1_corridor_w7_1 with Dissolve(0.1)
    pause 0.5
    gg 0 "（唯一没有门扇的门洞。看来这就是离开这鬼地方的出口。）" with Dissolve(0.3)
    pause 0.5
    stop music2 fadeout 7
    play sound2 paranormal_disturbance_2
    scene darkside1_corridor_lab_w7
    show darkside1_corridor_w7_2 with Dissolve(0.1)
    $ renpy.pause (23, hard=True)
    
    scene black
    pause 2
    pause 2
    jump evan_story

###### TOWN - EVAN

label evan_story:
    
    play sound clockalarm_digib01 fadein 0.6 loop
    
    scene evan_story_1 with Dissolve(1.0)
    pause 1.5
    scene evan_story_2 with Dissolve(0.3)
    pause 1
    scene evan_story_3 with Dissolve(0.3)
    pause 1
    scene evan_story_4 with Dissolve(0.3)
    pause 0.5
    evan 0 "（又是一天，又是一块钱。）" with Dissolve(0.3)
    scene evan_story_5 with Dissolve(0.3)
    evan 0 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    stop sound fadeout 0.3
    play music2 relax_deodo
    
    scene evan_story_6 with Dissolve(0.3)
    evan 1 "（我怎么会落到这种地步？）" with Dissolve(0.3)
    scene evan_story_7 with Dissolve(0.3)
    pause 1
    scene evan_story_8 with Dissolve(0.3)
    evan 1 "喂，醒醒，已经七点了。" with Dissolve(0.3)
    scene evan_story_9 with Dissolve(0.3)
    evan 1 "一小时后就要上课了。" with Dissolve(0.3)
    scene evan_story_10 with Dissolve(0.3)
    grace 3 "再睡五分钟……" with Dissolve(0.3)
    scene evan_story_11 with Dissolve(0.3)
    evan 1 "五分钟？" with Dissolve(0.3)
    scene evan_story_12 with Dissolve(0.3)
    evan 1 "你要上课了！" with Dissolve(0.3)
    scene evan_story_13 with Dissolve(0.3)
    evan 1 "我打工供你读大学，起来。" with Dissolve(0.3)
    scene evan_story_14 with Dissolve(0.3)
    evan 1 "以前你拿奖学金的时候，想怎么混都行。但现在，起来。" with Dissolve(0.3)
    scene evan_story_15 with Dissolve(0.3)
    grace 3 "真烦……" with Dissolve(0.3)
    scene evan_story_16 with Dissolve(0.3)
    evan 1 "你在那边嘟囔什么？" with Dissolve(0.3)
    scene evan_story_17 with Dissolve(0.3)
    grace 3 "没、没什么，我什么都没说。" with Dissolve(0.3)
    
    stop music2 fadeout 1.5
    play music busy_city_street_traffic_loop_full fadein 1.5
    
    scene evan_story_18 with Dissolve(1.0)
    pause 2
    
    stop music fadeout 1.5
    play music2 office_busy_ambience_loop fadein 3
    
    scene evan_story_19 with Dissolve(0.6)
    pause 1
    scene evan_story_20 with Dissolve(0.4)
    pause 1.2
    scene evan_story_21 with Dissolve(0.3)
    pause 0.5
    scene evan_story_22 with Dissolve(0.3)
    pause 0.7
    scene evan_story_23 with Dissolve(0.3)
    kaito 1 "你看新闻了吗？" with Dissolve(0.3)
    scene evan_story_24 with Dissolve(0.3)
    kaito 1 "太惨了。" with Dissolve(0.3)
    scene evan_story_25 with Dissolve(0.3)
    kaito 1 "新闻说是意外，但有传言说当时发生了一些怪事。" with Dissolve(0.3)
    scene evan_story_26 with Dissolve(0.3)
    souta 1 "怪事？什么意思？" with Dissolve(0.3)
    scene evan_story_27 with Dissolve(0.3)
    kaito 1 "他们说看到奇怪的闪光，像闪电，但没有下雨。" with Dissolve(0.3)
    scene evan_story_28 with Dissolve(0.3)
    kaito 1 "还有声音，一阵异常的轰鸣……总之都很怪。希望别再出事。" with Dissolve(0.3)
    scene evan_story_29 with Dissolve(0.3)
    pause 1
    scene evan_story_30 with Dissolve(0.3)
    evan 2 "（再撑几个小时我就自由了。）" with Dissolve(0.3)
    scene evan_story_31 with Dissolve(0.3)
    evan 2 "（回家路上还得买点吃的。）" with Dissolve(0.3)
    scene evan_story_32 with Dissolve(0.3)
    itsuki 1 "喂，[evan]，这个给你。刚有快递送来的。" with Dissolve(0.3)
    scene evan_story_33 with Dissolve(0.3)
    evan 2 "给我的？" with Dissolve(0.3)
    scene evan_story_34 with Dissolve(0.3)
    evan 2 "我没订东西啊。" with Dissolve(0.3)
    scene evan_story_35 with Dissolve(0.3)
    itsuki 1 "上面写着你的名字。" with Dissolve(0.3)
    scene evan_story_36 with Dissolve(0.3)
    itsuki 1 "你收着吧。" with Dissolve(0.3)
    scene evan_story_37 with Dissolve(0.3)
    pause 1
    
    stop music2 fadeout 1
    play music harbor_dock_evening_loop fadein 2 volume 0.6
    play music3 calm_city_night volume 0.4 fadein 2
    
    scene evan_story_38 with Dissolve(1.0)
    pause 1.5
    
    play sound2 cigarette_burning_1 volume 0.4
    
    scene evan_story_39 with Dissolve(0.3)
    pause 1
    scene evan_story_40 with Dissolve(0.3)
    pause 1.5
    scene evan_story_41 with Dissolve(0.3)
    pause 1.2
    scene evan_story_42 with Dissolve(0.3)
    pause 1
    scene evan_story_43 with Dissolve(0.3)
    pause 1.2
    
    play sound box1 volume 0.6
    
    scene evan_story_44 with Dissolve(0.3)
    evan 2 "（这么轻的盒子。是空的吗？）" with Dissolve(0.3)
    scene evan_story_45 with Dissolve(0.3)
    evan 2 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    play sound box2
    
    scene evan_story_46 with Dissolve(0.3)
    pause 0.5
    evan 2 "（这什么鬼东西？谁会寄这个给我？）" with Dissolve(0.3)
    scene evan_story_47 with Dissolve(0.3)
    evan 2 "{cps=5}……{/cps}"
    
    play sound dm4
    stop music fadeout 1
    stop music3 fadeout 1
    play music2 evil_wobbling_background_loop fadein 1
    
    scene evan_story_48 with Dissolve(0.1)
    pause 0.1
    scene evan_story_49 with Dissolve(0.1)
    pause 0.1
    scene evan_story_50 with Dissolve(0.1)
    pause 0.5
    evan 2 "（刚才那只眼睛是不是睁开了？！）" with Dissolve(0.3)
    
    play sound3 dm5
    
    scene evan_story_51 with Dissolve(0.3)
    evan 2 "（什么……？！）" with Dissolve(0.3)
    scene evan_story_52 with Dissolve(0.3)
    evan 2 "发、发生……怎么了？！" with Dissolve(0.3)
    
    play sound2 dark_portal_trailer_hit
    stop music2 fadeout 10
    
    scene evan_story_53 with Dissolve(0.3)
    pause 0.3
    scene black with Dissolve(0.5)
    evan 2 "啊啊啊啊！" with Dissolve(0.1)
    
    jump evan_story_ds

###### DARKSIDE - 1 - EVAN

label evan_story_ds:

    play sound3 demon_portal_open volume 2
    play music3 lurking_evil fadein 3

    scene evan_story_ds_1 with vpunch
    pause 0.1
    scene evan_story_ds_2 with Dissolve(1.0)
    evan 2 "（我、我在哪儿……？）" with Dissolve(0.3)
    scene evan_story_ds_3 with Dissolve(0.3)
    evan 2 "（这是什么地方？）" with Dissolve(0.3)
    scene evan_story_ds_4 with Dissolve(0.3)
    player_prisoner 1 "嘿，这也是你第一次来吗？" with Dissolve(0.3)
    scene evan_story_ds_5 with Dissolve(0.3)
    evan 2 "（第一次？）" with Dissolve(0.3)
    scene evan_story_ds_6 with Dissolve(0.3)
    evan 2 "这里到底怎么回事？" with Dissolve(0.3)
    scene evan_story_ds_7 with Dissolve(0.3)
    player_prisoner 1 "我刚才还在做社区服务，然后……砰！" with Dissolve(0.3)
    scene evan_story_ds_8 with Dissolve(0.3)
    player_prisoner 1 "现在我就到这儿了……" with Dissolve(0.3)
    scene evan_story_ds_9 with Dissolve(0.3)
    player_prisoner 1 "你也收到包裹了吗？" with Dissolve(0.3)
    scene evan_story_ds_10 with Dissolve(0.3)
    evan 2 "（包裹？）" with Dissolve(0.3)
    scene evan_story_ds_11 with Dissolve(0.3)
    pause 1.5
    scene evan_story_ds_12 with Dissolve(0.3)
    player_woman1 1 "这是什么魔法吗？我在做梦吗……？" with Dissolve(0.3)

    play sound2 cinematic_impact_1
    
    scene evan_story_ds_13 with Dissolve(0.3)
    pause 1.5

    play music2 wildkittytunes_dark_soundscapes
    stop music3 fadeout 3
    
    scene evan_story_ds_14 with Dissolve(0.3)
    figure 1 "嗯，看来大家都来了。" with Dissolve(0.3)
    scene evan_story_ds_15 with Dissolve(0.3)
    player_prisoner 1 "嘿，你是谁？！" with Dissolve(0.3)
    scene evan_story_ds_16 with Dissolve(0.3)
    player_prisoner 1 "还有我们他妈到底在哪儿？" with Dissolve(0.3)
    scene evan_story_ds_17 with Dissolve(0.3)
    player_prisoner 1 "如果这是恶作剧，你会后悔的！" with Dissolve(0.3)
    scene evan_story_ds_18 with Dissolve(0.3)
    player_woman1 1 "这是哪门子真人秀……？" with Dissolve(0.3)
    scene evan_story_ds_19 with Dissolve(0.3)
    figure 1 "请别大喊大叫。大家冷静一点。" with Dissolve(0.3)
    scene evan_story_ds_20 with Dissolve(0.3)
    figure 1 "你们该高兴才对！你们运气好得出奇，因为今天，你们的人生将永远改变！" with Dissolve(0.3)
    scene evan_story_ds_21 with Dissolve(0.3)
    figure 1 "你们所有人都收到了包裹，这意味着作为人类的生活已经成过去式！" with Dissolve(0.3)
    scene evan_story_ds_22 with Dissolve(0.3)
    evan 2 "你在说什么？" with Dissolve(0.3)
    player_woman1 1 "这都是什么鬼话？" with Dissolve(0.3)
    player_woman1 1 "如果我们不再是人类，那我们是什么？"
    figure 1 "信徒。" with Dissolve(0.3)
    evan 2 "那又是什么意思？" with Dissolve(0.3)
    scene evan_story_ds_23 with Dissolve(0.3)
    figure 1 "而且，作为刚刚新鲜出炉的信徒，你们将时不时地被丢进暗之维度无尽的空间里。" with Dissolve(0.3)
    scene evan_story_ds_24 with Dissolve(0.3)
    figure 1 "而如果你们能在这些空间里以及别处完成任务……" with Dissolve(0.3)
    
    play sound drumstomsddeepacce volume 3
    
    scene evan_story_ds_25 with Dissolve(0.3)
    figure 2 "就会变强，并获得各种奖励！" with Dissolve(0.3)
    scene evan_story_ds_26 with Dissolve(0.3)
    player_prisoner 1 "等一下！什么奖励？" with Dissolve(0.3)
    scene evan_story_ds_27 with Dissolve(0.3)
    player_prisoner 1 "比如钱？" with Dissolve(0.3)
    
    play sound2 figure_evil_laugh
    
    scene evan_story_ds_28 with Dissolve(0.3)
    figure 1 "哈哈哈！" with Dissolve(0.3)
    scene evan_story_ds_29 with Dissolve(0.3)
    figure 1 "不哦，是有用得多的东西。" with Dissolve(0.3)
    
    play sound3 evilwhoosh1
    
    scene evan_story_ds_30 with Dissolve(0.3)
    figure 2 "作为奖励，你们会得到灵魂石。而灵魂石能换到你们需要的一切。" with Dissolve(0.3)
    scene evan_story_ds_31 with Dissolve(0.3)
    player_prisoner 1 "连钱也能？" with Dissolve(0.3)
    
    play sound4 hell_on_earth_1
    
    scene evan_story_ds_32 with Dissolve(0.3)
    figure 1 "想要的话，你可以把石子换成现金。" with Dissolve(0.3)
    scene evan_story_ds_33 with Dissolve(0.3)
    figure 1 "不知道为什么，很多人一开始都这么做。" with Dissolve(0.3)
    
    stop sound4 fadeout 2
    
    scene evan_story_ds_34 with Dissolve(0.3)
    player_prisoner 1 "多、多少钱？一颗灵魂石能换多少？" with Dissolve(0.3)
    scene evan_story_ds_35 with Dissolve(0.3)
    figure 1 "这么说吧……" with Dissolve(0.3)
    scene evan_story_ds_36 with Dissolve(0.3)
    figure 1 "一万美元。" with Dissolve(0.3)
    scene evan_story_ds_37 with Dissolve(0.3)
    evan 2 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene evan_story_ds_38 with Dissolve(0.3)
    player_woman1 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene evan_story_ds_39 with Dissolve(0.3)
    player_prisoner 1 "哈哈哈！我要发财了！" with Dissolve(0.3)
    scene evan_story_ds_40 with Dissolve(0.3)
    evan 2 "那要是我们没完成你的任务呢？" with Dissolve(0.3)
    scene evan_story_ds_41 with Dissolve(0.3)
    figure 1 "我正要说到这个！" with Dissolve(0.3)
    scene evan_story_ds_42 with Dissolve(0.3)
    player_woman1 1 "什么？会怎样？" with Dissolve(0.3)
    figure 1 "很简单……" with Dissolve(0.3)
    
    play sound drumstomsddeepacce volume 3
    
    scene evan_story_ds_43 with Dissolve(0.3)
    figure 1 "你们就死定了！" with Dissolve(0.3)
    
    play sound evil_boom_1
    
    show evan_story_ds_44 with Dissolve(0.1)
    pause 1
    
    play sound2 evil_boom_2
    
    show evan_story_ds_45 with Dissolve(0.1)
    pause 2
    
    play sound3 evil_boom_3
    
    scene evan_story_ds_46 with Dissolve(0.1)
    pause 3.5
    
    play sound apocalyptic_impact_sinister_hit_tone_03
    
    scene evan_story_ds_47 with vpunch
    figure 1 "欢迎来到暗界！" with Dissolve(0.3)
    scene evan_story_ds_48 with Dissolve(0.3)
    evan 2 "等等，我还有问题！" with Dissolve(0.3)
    
    show evan_story_ds_49 with Dissolve(0.1)
    $ renpy.pause (4.3, hard=True)
    
    scene evan_story_ds_50 with Dissolve(0.3)
    evan 2 "你到底是谁……" with Dissolve(0.3)
    
    play music3 music_loop_ashes_and_rubble_ominous_swelling_dark_full_1 fadein 7
    stop music2 fadeout 10
    
    scene evan_story_ds_51 with Dissolve(0.3)
    player_woman1 1 "雾散开一些了。是不是意味着任务现在开始？" with Dissolve(0.3)
    scene evan_story_ds_52 with Dissolve(0.3)
    player_woman1 1 "我们到了哪里……我、我们在哪儿？" with Dissolve(0.3)
    scene evan_story_ds_53 with Dissolve(0.3)
    player_nerd 1 "这、这里到底在干什么……我们要死在这儿吗……？" with Dissolve(0.3)
    scene evan_story_ds_54 with Dissolve(0.3)
    player_prisoner 1 "大家冷静！我觉得这可能是某种电视节目，周围的一切都是假的！" with Dissolve(0.3)
    scene evan_story_ds_55 with Dissolve(0.3)
    player_prisoner 1 "反正我现在自由了，无所谓。" with Dissolve(0.3)
    scene evan_story_ds_56 with Dissolve(0.3)
    player_woman1 1 "喂、喂……" with Dissolve(0.3)
    scene evan_story_ds_57 with Dissolve(0.3)
    player_woman1 1 "那、那是什么……那边那个是什么？" with Dissolve(0.3)
    scene evan_story_ds_58 with Dissolve(0.3)
    player_nerd 1 "嗯？" with Dissolve(0.3)
    scene evan_story_ds_59 with Dissolve(0.3)
    player_prisoner 1 "快转身！" with Dissolve(0.3)
    
    play sound monster_5 volume 0.6
    
    scene evan_story_ds_60 with Dissolve(0.3)
    player_nerd 1 "!!!" with Dissolve(0.3)
    
    play sound2 monster_1
    
    scene evan_story_ds_61 with Dissolve(0.3)
    player_nerd 1 "?!" with Dissolve(0.3)
    
    play sound5 evil_boom_4
    
    scene evan_story_ds_62 with Dissolve(0.3)
    pause 0.5
    
    play sound evilwhoosh1
    
    scene evan_story_ds_63 with Dissolve(0.3)
    pause 0.3
    
    play sound3 scream_huge_monster_1
    play sound4 blood_gore_impact_4
    play music2 adventure_game_loop
    stop music3 fadeout 10
    
    scene evan_story_ds_64 with hpunch:
        xalign 0.5
        yalign 0.5
        zoom 1.1
        ease 4 zoom 1
    pause 3
    
    play sound5 evil_boom_2
    
    scene evan_story_ds_65 with Dissolve(0.1)
    evan 2 "它……它把他的头拧下来了？！" with Dissolve(0.3)
    
    play sound7 runners_group_on_road_loop_full loop volume 0.6
    
    scene evan_story_ds_66 with Dissolve(0.3)
    player_prisoner 1 "我、我们快离开这儿！" with Dissolve(0.3)
    scene evan_story_ds_67 with Dissolve(0.3)
    pause 1.2
    scene evan_story_ds_68 with Dissolve(0.3)
    pause 1
    
    play sound3 stone_hit_on_ground_2_full
    
    scene evan_story_ds_69 with Dissolve(0.3)
    pause 1
    
    play sound heavy_body_fall_03
    
    scene evan_story_ds_70 with vpunch
    pause 0.5
    
    play sound2 monster_2
    stop sound7 fadeout 10
    
    scene evan_story_ds_71 with Dissolve(0.3)
    player_silentguy 1 "救命！别、别丢下我！" with Dissolve(0.3)
    scene evan_story_ds_72 with Dissolve(0.3)
    player_silentguy 1 "不要！别靠近我！" with Dissolve(0.3)
    
    play sound3 monster_3
    
    scene evan_story_ds_73 with Dissolve(0.3)
    player_silentguy 1 "求、求求你……" with Dissolve(0.3)
    
    play sound5 scream_huge_monster_3
    play sound6 cinematic_impact_horror_hit_01
    play sound4 blood_gore_impact_5
    stop music2 fadeout 10
    
    scene black with Dissolve(0.1)
    pause 2
    pause 2
    
    play music3 dark_loop_nightmare_void_ghostly_full_ominous_movement fadein 7 volume 0.6
    play sound7 ghostly_whisper_background_loop_1 loop fadein 7
    
    pause 2
    
##### MC - 1
    
    play sound evilwhoosh1
    
    scene evan_story_ds_gg_1 with Dissolve(1.0)
    pause 2
    stop sound7 fadeout 10
    
    scene evan_story_ds_gg_2 with Dissolve(0.3)
    gg 0 "（这里有十几个。）" with Dissolve(0.3)
    scene evan_story_ds_gg_3 with Dissolve(0.3)
    gg 0 "（他们没有攻击……只是站在那里。好像在等什么。或者……某个人？）" with Dissolve(0.3)
    
    play sound evil_boom_4
    
    scene evan_story_ds_gg_4 with Dissolve(0.3)
    pause 1.2
    
    play sound2 vageleaf_leaves_heavy_impact
    
    scene evan_story_ds_gg_5 with Dissolve(0.3)
    pause 0.7
    
    play sound3 evilwhoosh1
    play sound4 minotaur_breath
    
    scene evan_story_ds_gg_6 with Dissolve(0.3)
    pause 1.5
    scene evan_story_ds_gg_7 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_gg_8 with Dissolve(0.3)
    gg 0 "（他们不动……是因为怕它？）" with Dissolve(0.3)
    
    play sound5 evil_boom_4
    play sound6 minotaur_in_the_labyrinth
    
    scene evan_story_ds_gg_9 with Dissolve(0.3)
    gg 0 "（你他妈到底是什么……）" with Dissolve(0.3)
    
    
    scene black with Dissolve(0.3)
    
    stop music3 fadeout 5
    
    pause 2
    
    play music2 lurking_evil fadein 5
    
    pause 2
    
##### EVAN - 1
    
    scene evan_story_ds_74 with Dissolve(1.0)
    evan 2 "谢天谢地……我们总算甩掉了……" with Dissolve(0.3)
    evan 2 "（如果这不是梦，我必须找到回去的路。）"
    evan 2 "（[grace]……我得回去找她。）"
    scene evan_story_ds_75 with Dissolve(0.3)
    evan 2 "这他妈什么鬼东西！" with Dissolve(0.3)
    scene evan_story_ds_76 with Dissolve(0.3)
    player_prisoner 1 "你他妈挡我路干什么？！" with Dissolve(0.3)
    scene evan_story_ds_77 with Dissolve(0.3)
    player_liam 1 "我怎么挡你路了？" with Dissolve(0.3)
    scene evan_story_ds_78 with Dissolve(0.3)
    player_prisoner 1 "明明是我先跑的，你追上来差点把我撞倒！" with Dissolve(0.3)
    scene evan_story_ds_79 with Dissolve(0.3)
    player_prisoner 1 "你以为这条路是你家的？" with Dissolve(0.3)
    scene evan_story_ds_80 with Dissolve(0.3)
    player_liam 1 "那我下次是不是还得看路？" with Dissolve(0.3)
    scene evan_story_ds_81 with Dissolve(0.3)
    player_prisoner 1 "你这硬汉要是再挡我，我就亲手宰了你。" with Dissolve(0.3)
    scene evan_story_ds_82 with Dissolve(0.3)
    player_liam 1 "想现在就试试？看看最后站着的是谁。" with Dissolve(0.3)
    scene evan_story_ds_83 with Dissolve(0.3)
    player_woman2 1 "喂，哥们，现在不是打架的时候！" with Dissolve(0.3)
    scene evan_story_ds_84 with Dissolve(0.3)
    player_woman2 1 "我看见不远处有光，好像有人家。" with Dissolve(0.3)
    scene evan_story_ds_85 with Dissolve(0.3)
    player_woman1 1 "还等什么？快过去！" with Dissolve(0.3)
    scene evan_story_ds_86 with Dissolve(0.3)
    player_prisoner 1 "{cps=5}……{/cps}"
    
    stop music2 fadeout 10
    play music3 dark_ambient_loop fadein 8
    
    scene black with Dissolve (0.3)
    pause 0.5
    
    scene evan_story_ds_87 with Dissolve(1.0)
    pause 1.5
    scene evan_story_ds_88 with Dissolve(0.3)
    player_woman1 1 "走走走，哥们们，快到了，就快了！" with Dissolve(0.3)
    
    play sound grab_4
    
    scene evan_story_ds_89 with Dissolve(0.3)
    pause 1
    
    play sound2 dm3
    
    scene evan_story_ds_90 with hpunch
    player_liam 1 "啊！？啊啊！" with Dissolve(0.1)
    scene evan_story_ds_91 with Dissolve(0.3)
    player_woman2 1 "...?!" with Dissolve(0.1)
    
    play sound bodx_fall_final12
    
    scene evan_story_ds_92 with Dissolve(0.3)
    player_woman2 1 "啊啊啊！" with Dissolve(0.1)
    scene evan_story_ds_93 with Dissolve(0.3)
    player_woman1 1 "你他妈在干什么？！" with Dissolve(0.3)
    scene evan_story_ds_94 with Dissolve(0.3)
    player_prisoner 1 "你冲我吼什么？" with Dissolve(0.3)
    player_prisoner 1 "他自己站不稳又不能怪我。"
    scene evan_story_ds_95 with Dissolve(0.3)
    evan 2 "（操，要独自活着出去更难了。）" with Dissolve(0.3)
    evan 2 "（我必须救他们！）"
    
    play sound2 dirt_hit
    
    scene evan_story_ds_96 with Dissolve(0.3)
    evan 2 "继续走，我来扶他们起来！" with Dissolve(0.3)
    scene evan_story_ds_97 with Dissolve(0.3)
    player_woman1 1 "别把我当傻子！我亲眼看见是你把他推倒的！" with Dissolve(0.3)
    scene evan_story_ds_98 with Dissolve(0.3)
    player_prisoner 1 "女人，你最好照他说的做，我们自己能出去。" with Dissolve(0.3)
    scene evan_story_ds_99 with Dissolve(0.3)
    player_prisoner 1 "别管他们了，他们在这儿活不下来。" with Dissolve(0.3)
    scene evan_story_ds_100 with Dissolve(0.3)
    player_prisoner 1 "那怪物会在他们追上我们之前就吃掉他们。" with Dissolve(0.3)
    scene evan_story_ds_101 with Dissolve(0.3)
    player_woman1 1 "那就帮他们啊！" with Dissolve(0.3)
    
    play sound3 kick_1
    
    scene evan_story_ds_102 with hpunch
    pause 1
    
    play sound3 kick_6 volume 0.2
    play sound4 dirt_hit volume 0.2
    
    scene evan_story_ds_103 with Dissolve(0.3)
    pause 1.3
    scene evan_story_ds_104 with Dissolve(0.3)
    player_woman1 1 "我宁愿跟那些不会在我最意想不到的时候把我推下去的人一起走！" with Dissolve(0.3)
    
    play sound heavy_body_fall_03 volume 2
    
    scene evan_story_ds_105 with Dissolve(0.3)
    pause 0.6
    scene evan_story_ds_106 with Dissolve(0.3)
    player_prisoner 1 "是我带你们离开那东西的，你这贱人！" with Dissolve(0.3)
    scene evan_story_ds_107 with Dissolve(0.3)
    player_woman1 1 "离我远点！" with Dissolve(0.3)
    scene evan_story_ds_108 with Dissolve(0.3)
    player_liam 1 "你能走吗？" with Dissolve(0.3)
    scene evan_story_ds_109 with Dissolve(0.3)
    player_woman2 1 "能……我没得选。" with Dissolve(0.3)
    scene evan_story_ds_110 with Dissolve(0.3)
    evan 2 "快点，我们时间不多！" with Dissolve(0.3)
    scene evan_story_ds_111 with Dissolve(0.3)
    player_liam 1 "再坚持一下，我扶着你。" with Dissolve(0.3)
    scene evan_story_ds_112 with Dissolve(0.3)
    player_woman2 1 "啊，没那么容易……" with Dissolve(0.3)
    scene evan_story_ds_113 with Dissolve(0.3)
    player_liam 1 "你也是，别掉队！" with Dissolve(0.3)
    scene evan_story_ds_114 with Dissolve(0.3)
    evan 2 "我已经爬到最快了！" with Dissolve(0.3)
    scene evan_story_ds_115 with Dissolve(0.3)
    player_woman2 1 "就差一点了！" with Dissolve(0.3)
    scene evan_story_ds_116 with Dissolve(0.3)
    player_woman2 1 "啊……" with Dissolve(0.3)
    scene evan_story_ds_117 with Dissolve(0.3)
    player_woman2 1 "抓住我的手！" with Dissolve(0.3)
    scene evan_story_ds_118 with Dissolve(0.3)
    player_liam 1 "我抓到了，谢谢。你最好去帮他。" with Dissolve(0.3)
    scene evan_story_ds_119 with Dissolve(0.3)
    player_liam 1 "抓紧！" with Dissolve(0.3)
    evan 2 "好、好的……谢谢……" with Dissolve(0.3)
    scene evan_story_ds_120 with Dissolve(1.0)
    player_liam 1 "我没看见那个混蛋。" with Dissolve(0.3)
    scene evan_story_ds_121 with Dissolve(0.3)
    evan 2 "走吧，别在这儿久留，可能不止一个。" with Dissolve(0.3)
    scene evan_story_ds_122 with Dissolve(1.0)
    pause 1
    scene evan_story_ds_123 with Dissolve(0.3)
    player_woman2 1 "那家伙怎么办？" with Dissolve(0.3)
    scene evan_story_ds_124 with Dissolve(0.3)
    player_liam 1 "他能自己应付，别管他了。" with Dissolve(0.3)
    scene evan_story_ds_125 with Dissolve(0.3)
    player_prisoner 1 "站住！" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.3, delay=0, channel=u'music2')
    play sound monster_4 volume 0.4
    play music2 adventure_game_loop fadein 5
    stop music3 fadeout 10
    
    scene evan_story_ds_126 with Dissolve(0.3)
    player_prisoner 1 "等等我！" with Dissolve(0.3)
    scene evan_story_ds_127 with Dissolve(0.3)
    player_prisoner 1 "?!" with Dissolve(0.1)
    
    $ renpy.music.set_volume(0.5, delay=2, channel=u'music2')
    
    scene evan_story_ds_128 with Dissolve(0.3)
    player_prisoner 1 "那边……树上有东西动了？" with Dissolve(0.3)
    scene evan_story_ds_129 with Dissolve(0.3)
    player_prisoner 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    play sound2 monster_1 volume 0.3
    
    scene evan_story_ds_130 with Dissolve(0.3)
    player_prisoner 1 "喂！谁在那儿？！" with Dissolve(0.3)
    scene evan_story_ds_131 with Dissolve(0.3)
    player_prisoner 1 "可恶、可恶，贱人，不要！" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=1, channel=u'music2')
    
    scene evan_story_ds_132 with Dissolve(1.0)
    player_prisoner 1 "啊啊啊啊！" with Dissolve(0.1)
    
    stop music2 fadeout 4
    play music3 main_track_with_screamer fadein 4 volume 0.7
    
    pause 2
    scene evan_story_ds_133 with Dissolve(1.0)
    player_woman1 1 "你们没事吧？" with Dissolve(0.3)
    player_liam 1 "我没事，你呢？" with Dissolve(0.3)
    player_woman2 1 "我、我会……我们先休息一会儿……" with Dissolve(0.3)
    scene evan_story_ds_134 with Dissolve(0.3)
    player_woman1 1 "还不行。我们不知道离那怪物有多远，也不知道它会不会追上来。安全起见，趁还能走就先走。" with Dissolve(0.3)
    scene evan_story_ds_135 with Dissolve(0.3)
    player_woman1 1 "至少走到找到看起来安全的地方为止。" with Dissolve(0.3)
    scene evan_story_ds_136 with Dissolve(0.3)
    player_woman2 1 "你觉得那家伙还能追上来吗？" with Dissolve(0.3)
    scene evan_story_ds_137 with Dissolve(0.3)
    player_liam 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene evan_story_ds_138 with Dissolve(0.3)
    player_woman1 1 "别管他了。他太危险，不能信任。我们继续走。" with Dissolve(0.3)
    scene evan_story_ds_139 with Dissolve(0.3)
    player_woman2 1 "已经？……好、好吧。" with Dissolve(0.3)
    
    play sound cinematic_woosh_1 volume 0.3
    
    scene evan_story_ds_140 with Dissolve(1.0)
    pause 2
    scene evan_story_ds_141 with Dissolve(1.0)
    pause 2
    
    play sound cinematic_impact_1
    
    scene evan_story_ds_142 with Dissolve(0.3)
    evan 2 "终于，我们到了！" with Dissolve(0.3)
    evan 2 "好，别急。走在一起，里面可能也很危险。"
    player_liam 1 "希望有吃的。我一整天没吃东西就被弄到这儿来了。" with Dissolve(0.3)
    player_woman2 1 "要是能出去，我建议庆祝一下。我请客！" with Dissolve(0.3)
    scene evan_story_ds_143 with Dissolve(0.3)
    player_woman1 1 "那我要一瓶干红，一个人喝。" with Dissolve(0.3)
    player_woman2 1 "你们也一人一瓶，不过先出去再说。" with Dissolve(0.3)
    player_liam 1 "为了这个我们得先活着出去，哈哈。" with Dissolve(0.3)
    scene evan_story_ds_144 with Dissolve(0.3)
    evan 2 "（这味道好奇怪……）" with Dissolve(0.3)
    evan 2 "（我从没闻过这种味道。难道是……）"
    
    play sound2 door_knocking1 volume 0.4
    
    scene evan_story_ds_145 with Dissolve(0.3)
    player_liam 1 "喂！里面有人吗？" with Dissolve(0.3)
    player_woman2 1 "我们在林子里迷路了，能让我们进去吗？" with Dissolve(0.3)
    scene evan_story_ds_146 with Dissolve(0.3)
    evan 2 "（嗯？那是什么……）" with Dissolve(0.3)
    scene evan_story_ds_147 with Dissolve(0.3)
    evan 2 "（血？！）" with Dissolve(0.3)
    scene evan_story_ds_148 with Dissolve(0.3)
    evan 2 "等等！" with Dissolve(0.3)
    scene evan_story_ds_149 with Dissolve(0.3)
    player_liam 1 "喂，屋主！我们想进去，我们没带武器！" with Dissolve(0.3)
    scene evan_story_ds_150 with Dissolve(0.3)
    evan 2 "各位……" with Dissolve(0.3)
    
    show evan_story_ds_151 with Dissolve(0.3)
    $ renpy.pause (1, hard=True)
    
    scene evan_story_ds_152 with Dissolve(0.3)
    beardedman 1 "谁在外面？你们是谁？" with Dissolve(0.3)
    scene evan_story_ds_153 with Dissolve(0.3)
    player_liam 1 "我们迷路了，能帮帮我们吗？" with Dissolve(0.3)
    scene evan_story_ds_154 with Dissolve(0.3)
    beardedman 1 "迷路了？" with Dissolve(0.3)
    
    play music2 mysterious_and_spooky_loop fadein 10
    stop music3 fadeout 10
    
    scene evan_story_ds_155 with Dissolve(0.3)
    beardedman 1 "哎呀，我太没礼貌了，当然请进！我刚做完晚饭。" with Dissolve(0.3)
    scene evan_story_ds_156 with Dissolve(0.3)
    player_woman2 1 "您一个人住这儿吗？" with Dissolve(0.3)
    scene evan_story_ds_157 with Dissolve(0.3)
    beardedman 1 "当然不是！" with Dissolve(0.3)
    scene evan_story_ds_158 with Dissolve(0.3)
    beardedman 1 "我儿子早就该回来了，大概只是晚了点。" with Dissolve(0.3)
    scene evan_story_ds_159 with Dissolve(0.3)
    player_woman2 1 "可、可外面很危险！您确定他没事吗？" with Dissolve(0.3)
    scene evan_story_ds_160 with Dissolve(0.3)
    beardedman 1 "危险？" with Dissolve(0.3)
    
    play sound beardedman_demon_laugh
    
    scene evan_story_ds_161 with Dissolve(0.3)
    beardedman 1 "哈哈哈哈！" with Dissolve(0.1)
    
    play sound2 evil_boom_2
    
    scene evan_story_ds_162 with Dissolve(0.3)
    beardedman 2 "你们不了解我儿子。他肯定没事，别担心。" with Dissolve(0.3)
    scene evan_story_ds_163 with Dissolve(0.3)
    player_liam 1 "希望我们突然来访没有太打扰您。" with Dissolve(0.3)
    scene evan_story_ds_164 with Dissolve(0.3)
    beardedman 1 "哪儿的话，一点也不麻烦。有人作伴我们很高兴，这附近很少有路人经过。" with Dissolve(0.3)
    scene evan_story_ds_165 with Dissolve(0.3)
    beardedman 1 "今晚我在地上给你们铺几张床，明早送你们到山脚。" with Dissolve(0.3)
    scene evan_story_ds_166 with Dissolve(0.3)
    beardedman 1 "郊外离那儿只有一步之遥。" with Dissolve(0.3)
    player_woman2 1 "太好了！" with Dissolve(0.3)
    scene evan_story_ds_167 with Dissolve(0.3)
    evan 2 "我们在来路上被袭击了。能告诉我们这里具体是哪里吗？" with Dissolve(0.3)
    scene evan_story_ds_168 with Dissolve(0.3)
    beardedman 1 "野生动物很危险，晚上最好别在我们的林子里闲逛。" with Dissolve(0.3)
    scene evan_story_ds_169 with Dissolve(0.3)
    evan 2 "可我们具体在哪儿？" with Dissolve(0.3)
    scene evan_story_ds_170 with Dissolve(0.3)
    beardedman 1 "嗯？" with Dissolve(0.3)
    scene evan_story_ds_171 with Dissolve(0.3)
    beardedman 1 "我不确定你问的是什么意思。" with Dissolve(0.3)
    scene evan_story_ds_172 with Dissolve(0.3)
    player_woman1 1 "嘘！我觉得他不想回答这个。" with Dissolve(0.3)
    scene evan_story_ds_173 with Dissolve(0.3)
    evan 2 "已经注意到了？" with Dissolve(0.3)
    scene evan_story_ds_174 with Dissolve(0.3)
    pause 0.1
    scene evan_story_ds_175 with Dissolve(0.1)
    pause 0.2
    scene evan_story_ds_174 with Dissolve(0.1)
    pause 0.1
    scene evan_story_ds_175 with Dissolve(0.1)
    pause 0.5
    scene evan_story_ds_176 with Dissolve(0.3)
    evan 2 "你们有电话吗？我们想联系家人。" with Dissolve(0.3)
    scene evan_story_ds_177 with Dissolve(0.3)
    beardedman 1 "没有，这儿没信号。" with Dissolve(0.3)
    scene evan_story_ds_178 with Dissolve(0.3)
    evan 2 "最近的镇子叫什么名字？" with Dissolve(0.3)
    beardedman 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    beardedman 1 "……哦，我真是老了，头都开始转了。"
    scene evan_story_ds_179 with Dissolve(0.3)
    beardedman 1 "孩子们，你们问题真多。明早我送你们到山脚，剩下的你们自己就能打听到了。" with Dissolve(0.3)
    scene evan_story_ds_180 with Dissolve(0.3)
    player_liam 1 "喂，你们怎么这么多问题啊？" with Dissolve(0.3)
    scene evan_story_ds_181 with Dissolve(0.3)
    player_liam 1 "明天一切都会清楚。现在先安静下来，等着吃饭吧！" with Dissolve(0.3)
    scene evan_story_ds_182 with Dissolve(0.3)
    beardedman 1 "你们先安顿好，我去拿点晚饭来。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.5, delay=2, channel=u'music2')
    $ renpy.music.set_volume(0.5, delay=0, channel=u'sound3')
    play sound3 bonfire_loop fadein 2
    
    scene evan_story_ds_183 with Dissolve(1.0)
    pause 3
    
    $ renpy.music.set_volume(1, delay=1, channel=u'sound3')
    
    scene evan_story_ds_184 with Dissolve(0.5)
    pause 3
    
    $ renpy.music.set_volume(1, delay=2, channel=u'music2')
    stop sound3 fadeout 10
    
    scene evan_story_ds_185 with Dissolve(0.3)
    evan 2 "{cps=5}……{/cps}"
    scene evan_story_ds_186 with Dissolve(0.3)
    player_liam 1 "这个真好吃，靠，我还能再吃！" with Dissolve(0.3)
    scene evan_story_ds_187 with Dissolve(0.3)
    player_woman2 1 "很好吃，谢谢。" with Dissolve(0.3)
    scene evan_story_ds_188 with Dissolve(0.3)
    beardedman 1 "我再给你们拿一些。" with Dissolve(0.3)
    scene evan_story_ds_189 with Dissolve(0.3)
    beardedman 1 "你怎么不吃？" with Dissolve(0.3)
    scene evan_story_ds_190 with Dissolve(0.3)
    beardedman 1 "你也吃点吧，需要体力。" with Dissolve(0.3)
    scene evan_story_ds_191 with Dissolve(0.3)
    evan 2 "不用了，谢谢，我不饿。" with Dissolve(0.3)
    scene evan_story_ds_192 with Dissolve(0.3)
    player_woman1 1 "是、是啊……把我们的份给他们吧。" with Dissolve(0.3)
    scene evan_story_ds_193 with Dissolve(0.3)
    player_liam 1 "哈，你们疯了吧！" with Dissolve(0.3)
    scene evan_story_ds_194 with Dissolve(0.3)
    player_liam 1 "那我们就能多吃！" with Dissolve(0.3)
    scene evan_story_ds_195 with Dissolve(0.3)
    beardedman 1 "那至少喝点水。嗓子肯定干得难受。来，喝点水。" with Dissolve(0.3)
    scene evan_story_ds_196 with Dissolve(0.3)
    evan 2 "（他为什么这么执着？！）" with Dissolve(0.3)
    scene evan_story_ds_197 with Dissolve(0.3)
    evan 2 "（这水和这食物肯定下了毒！）" with Dissolve(0.3)
    scene evan_story_ds_198 with Dissolve(0.3)
    beardedman 1 "喝吧。健康的身体需要充足的水分。" with Dissolve(0.3)
    
    play sound grab_plastic_1
    
    scene evan_story_ds_199 with Dissolve(0.1)
    pause 0.7
    
    play sound2 knife_slash_4
    play music3 fear_anxiety_mystery_conspiracy_theory_loop 
    stop music2 fadeout 3
    
    scene evan_story_ds_200 with hpunch
    evan 2 "你到底想干什么？！" with Dissolve(0.3)
    scene evan_story_ds_201 with Dissolve(0.3)
    player_woman2 1 "喂！你在干什么？！" with Dissolve(0.3)
    scene evan_story_ds_202 with Dissolve(0.3)
    player_woman2 1 "他喂过我们了，放他走！" with Dissolve(0.3)
    scene evan_story_ds_203 with Dissolve(0.3)
    evan 2 "我一看到门口的血就知道不对劲。你刚才是想毒死我们吧？" with Dissolve(0.3)
    scene evan_story_ds_204 with Dissolve(0.3)
    player_liam 1 "你这混蛋疯了！" with Dissolve(0.3)
    scene evan_story_ds_205 with Dissolve(0.3)
    player_liam 1 "放他走，不然我砸烂你的脸！" with Dissolve(0.3)
    
    play sound humans_kicks_kick_wood_table_hollow_rattle
    play sound2 knock_over_table_setting
    
    scene evan_story_ds_206 with vpunch
    player_woman1 1 "别、别靠近他！" with Dissolve(0.3)
    scene evan_story_ds_207 with Dissolve(0.3)
    player_woman1 1 "你瞎了吗？！" with Dissolve(0.3)
    scene evan_story_ds_208 with Dissolve(0.3)
    player_woman1 1 "你没注意到他行为有什么可疑的吗？" with Dissolve(0.3)
    scene evan_story_ds_209 with Dissolve(0.3)
    player_woman2 1 "热情待客有什么不好？" with Dissolve(0.3)
    scene evan_story_ds_210 with Dissolve(0.3)
    pause 0.5
    
    $ renpy.music.set_volume(0.3, delay=2, channel=u'music3')
    
    show evan_story_ds_211 with Dissolve(0.1)
    $ renpy.pause (2.8, hard=True)
    
    play sound3 bone_crusher_monster_footstep volume 2
    
    scene evan_story_ds_212 with Dissolve(0.1)
    pause 0.3
    scene evan_story_ds_213 with Dissolve(0.5)
    pause 1
    scene evan_story_ds_214 with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=2, channel=u'music3')
    
    beardedman 1 "你来了，儿子！" with Dissolve(0.3)
    
    play sound evil_boom_1
    
    scene evan_story_ds_215 with Dissolve(0.1)
    pause 0.7
    
    play sound2 evil_boom_2
    
    show evan_story_ds_216 with Dissolve(0.1)
    pause 0.7
    
    play sound3 evil_boom_4
    
    show evan_story_ds_217 with Dissolve(0.1)
    pause 0.7
    
    play sound4 evil_boom_3
    
    show evan_story_ds_218 with Dissolve(0.1)
    pause 0.7
    player_liam 1 "搞什么……" with Dissolve(0.3)
    
    play sound scream_huge_monster_1
    stop music3 fadeout 2
    play music2 horror_loop fadein 2
    
    scene evan_story_ds_219 with hpunch
    pause 1
    scene evan_story_ds_220 with hpunch
    player_woman1 1 "能抓什么就抓什么，准备战斗！" with Dissolve(0.3)
    scene evan_story_ds_221 with Dissolve(0.3)
    player_woman2 1 "你……你为什么要这样对我们？！" with Dissolve(0.3)
    scene evan_story_ds_222 with Dissolve(0.3)
    pause 1
    
    play sound blood_gore_impact_2 volume 0.4
    
    scene evan_story_ds_223 with hpunch
    pause 0.8
    
    play sound2 dm4
    
    scene evan_story_ds_224 with Dissolve(0.1)
    pause 1.5
    
    play sound3 zahvat_1
    
    scene evan_story_ds_225 with Dissolve(0.1)
    pause 1
    
    play sound beardedman_house_wood_break volume 1.5
    
    scene evan_story_ds_226 with vpunch
    pause 1.5
    scene evan_story_ds_227 with Dissolve(0.1)
    pause 1
    
    play sound2 axe_swing_2
    
    scene evan_story_ds_228 with hpunch
    pause 0.8
    
    play sound3 monster_2
    
    scene evan_story_ds_229 with Dissolve(0.1)
    pause 0.8
    
    play sound axe_swing_1
    
    scene evan_story_ds_230 with hpunch
    pause 0.8
    scene evan_story_ds_231 with Dissolve(0.1)
    player_liam 1 "快跑、快跑快点！" with Dissolve(0.1)
    scene evan_story_ds_232 with Dissolve(0.3)
    player_liam 1 "我会尽量拖住他！" with Dissolve(0.3)
    scene evan_story_ds_233 with hpunch
    player_woman1 1 "快点！" with Dissolve(0.3)
    
    play sound2 evil_boom_1
    
    scene evan_story_ds_234 with Dissolve(0.1)
    pause 1.5
    scene evan_story_ds_235 with Dissolve(0.3)
    pause 1
    
    play sound3 grab_3 volume 2
    
    scene evan_story_ds_236 with vpunch
    pause 1.5
    scene evan_story_ds_237 with Dissolve(0.1)
    pause 0.8
    
    play sound4 blood_gore_impact_1
    
    scene evan_story_ds_238 with hpunch
    pause 1
    
    play sound5 kick_2
    
    scene evan_story_ds_239 with hpunch
    pause 0.8
    
    play sound6 heavy_body_fall_01 volume 1.5
    
    scene evan_story_ds_240 with vpunch
    pause 1.5
    scene evan_story_ds_241 with Dissolve(0.3)
    pause 1.3
    
    play sound7 monster_3
    
    scene evan_story_ds_242 with Dissolve(0.1)
    pause 1
    scene evan_story_ds_243 with Dissolve(0.3)
    player_woman1 1 "各位……" with Dissolve(0.3)
    
    play sound scream_huge_monster_3
    
    scene evan_story_ds_244 with hpunch
    pause 1
    
    play sound2 kick_3
    
    scene evan_story_ds_245 with hpunch
    pause 1

    play sound3 monster_4
    
    scene evan_story_ds_246 with Dissolve(0.1)
    player_woman2 1 "救、救、救命！" with Dissolve(0.1)
    scene evan_story_ds_247 with vpunch
    
    play sound4 zahvat_2
    
    evan 2 "快跑啊！" with Dissolve(0.1)
    scene evan_story_ds_248 with Dissolve(0.3)
    pause 1.2
    scene evan_story_ds_249 with Dissolve(0.3)
    pause 1.5
    scene evan_story_ds_250 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_251 with Dissolve(0.3)
    evan 2 "快点，现在不能停！" with Dissolve(0.1)
    scene evan_story_ds_252 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_253 with Dissolve(0.3)
    player_woman1 1 "跑、跑不动……" with Dissolve(0.1)
    scene evan_story_ds_254 with Dissolve(0.3)
    pause 0.6
    scene evan_story_ds_255 with Dissolve(0.3)
    evan 2 "怎么了？" with Dissolve(0.3)
    scene evan_story_ds_256 with Dissolve(0.3)
    player_woman1 1 "我跑不动……" with Dissolve(0.3)
    player_woman1 1 "我以为我能撑过惊吓，但看来持续不了多久。"
    scene evan_story_ds_257 with Dissolve(0.3)
    player_woman1 1 "你现在跑，还能摆脱他。" with Dissolve(0.3)
    scene evan_story_ds_258 with Dissolve(0.3)
    evan 2 "可恶！" with Dissolve(0.3)
    evan 2 "我不会把你丢在这儿！"
    scene evan_story_ds_259 with Dissolve(0.3)
    player_woman1 1 "喂，你疯了吗？" with Dissolve(0.3)
    scene evan_story_ds_260 with Dissolve(0.3)
    player_woman1 1 "你想让我们两个都死在这儿？！" with Dissolve(0.3)
    scene evan_story_ds_261 with Dissolve(0.3)
    evan 2 "别吵了，我扶着你！" with Dissolve(0.3)
    
    play sound2 cinematic_boom_1
    stop music2 fadeout 2
    play music3 lurking_evil fadein 10
    play sound3 ghostly_whisper_background_loop_5 fadein 1 volume 0.3 loop
    play sound4 tinnitus fadein 3 loop volume 0.3
    
    scene evan_story_ds_262 with vpunch
    pause 0.3
    evan 2 "啊……这、这是什么？" with Dissolve(0.3)
    scene evan_story_ds_263 with Dissolve(0.5)
    pause 0.7
    scene evan_story_ds_264 with Dissolve(0.5)
    pause 1
    
    stop sound3 fadeout 10
    
    scene evan_story_ds_265 with Dissolve(0.5)
    pause 0.8
    scene evan_story_ds_266 with Dissolve(1.0)
    pause 0.5
    evan 2 "（这种感觉……好像有什么温暖的东西在全身蔓延……）" with Dissolve(0.3)
    evan 2 "（我感觉……轻飘飘的？）"
    evan 2 "（脑子也清醒了……饥饿、压力，全都消失了！）"
    
    stop sound4 fadeout 1
    play sound mountain_audio_cinematic_hit
    
    scene evan_story_ds_267 with Dissolve(0.1)
    pause 2
    scene evan_story_ds_268 with Dissolve(0.3)
    player_woman1 1 "真奇怪……" with Dissolve(0.3)
    scene evan_story_ds_269 with Dissolve(0.3)
    player_woman1 2 "什么都没变，可疲惫和疼痛……就这么没了。" with Dissolve(0.3)
    scene evan_story_ds_270 with Dissolve(0.3)
    evan 3 "你的眼睛……是红的！" with Dissolve(0.3)
    scene evan_story_ds_271 with Dissolve(0.3)
    player_woman1 2 "诶？！你的也是！这到底意味着什么？！" with Dissolve(0.3)
    scene evan_story_ds_272 with Dissolve(0.3)
    evan 3 "我闻到一股刺鼻的味道……" with Dissolve(0.3)
    scene evan_story_ds_273 with Dissolve(0.3)
    evan 3 "铁锈味？！" with Dissolve(0.3)
    
    play sound scream_huge_monster_1
    play music2 action_thriller_suspense_horror_loop_6 fadein 2
    stop music3 fadeout 4
    
    scene evan_story_ds_274 with hpunch
    pause 2
    
    play sound fight_blocks_3
    
    scene evan_story_ds_275 with Dissolve(0.1)
    player_woman1 2 "喂、喂，起来！快！" with Dissolve(0.3)
    scene evan_story_ds_276 with Dissolve(0.1)
    player_woman1 2 "那东西已经很近了！快点！" with Dissolve(0.3)
    scene evan_story_ds_277 with Dissolve(0.3)
    pause 1.2
    scene evan_story_ds_278 with Dissolve(0.1)
    pause 1
    scene evan_story_ds_279 with Dissolve(0.1)
    evan 3 "哈啊……准、准备……" with Dissolve(0.3)
    scene evan_story_ds_280 with Dissolve(0.3)
    evan 3 "准备战斗！" with Dissolve(0.3)
    scene evan_story_ds_281 with Dissolve(0.3)
    player_woman1 2 "什么？" with Dissolve(0.3)
    evan 3 "我们跑不过它。" with Dissolve(0.3)
    scene evan_story_ds_282 with Dissolve(0.3)
    evan 3 "你也感觉到了吧？" with Dissolve(0.3)
    scene evan_story_ds_283 with Dissolve(0.3)
    player_woman1 2 "我……我觉得是……" with Dissolve(0.3)
    scene evan_story_ds_284 with Dissolve(0.3)
    player_woman1 2 "你觉得我们能赢吗？" with Dissolve(0.3)
    scene evan_story_ds_285 with Dissolve(0.3)
    evan 3 "没得选。不打就是死。" with Dissolve(0.3)
    
    stop music2 fadeout 4
    
    scene black with Dissolve(1.0)
    pause 1
    pause 1
    
    ##### MC - 2
    
    play sound gunrif_gun_rifle_ruger
    play music3 dark_ambient_loop
    
    scene evan_story_ds_gg_10 with Dissolve(0.1)
    pause 1
    scene evan_story_ds_gg_11 with Dissolve(0.3)
    gg 19 "（那是最后一个……）" with Dissolve(0.3)
    
    play sound fight_swing_1 volume 1.3
    
    scene evan_story_ds_gg_12 with Dissolve(0.3)
    gg 19 "（这他妈是什么东西？怎么这么快？！）" with Dissolve(0.3)
    
    play sound fight_swing_2 volume 1
    
    scene evan_story_ds_gg_13 with Dissolve(0.3)
    pause 0.5
    
    play sound fight_swing_4 volume 1.5
    
    scene evan_story_ds_gg_14 with Dissolve(0.3)
    gg 19 "（它是在戏弄我吗……？）" with Dissolve(0.3)
    
    play sound boom_01
    play sound2 kick_4
    play sound3 tinnitus loop
    $ renpy.music.set_volume(0.3, delay=1, channel=u'music3')
    
    scene evan_story_ds_gg_15 with hpunch
    pause 0.3
    
    play sound4 boom_02
    
    scene evan_story_ds_gg_16 with hpunch:
        xalign 0.5
        yalign 0.5
        zoom 1
        ease 10 zoom 1.1
    gg 20 "（……还是我真的累到连反应都做不出来？）" with Dissolve(0.3)
    
    stop sound3 fadeout 10
    play sound5 heavy_body_fall_03 volume 2
    play sound kick_3
    
    scene evan_story_ds_gg_17 with hpunch
    pause 1.5
    
    play sound6 boom_04

    scene evan_story_ds_gg_18 with Dissolve(0.5):
        xalign 0.5
        yalign 0.5
        zoom 1
        linear 10 zoom 1.1
    pause 3
    
    $ renpy.music.set_volume(1, delay=2, channel=u'music3')
    
    scene evan_story_ds_gg_19 with Dissolve(0.3)
    gg 20 "（可它……比我面对过的任何敌人都强。）" with Dissolve(0.3)
    scene evan_story_ds_gg_20 with Dissolve(0.3)
    gg 20 "子弹他妈对我没用！" with Dissolve(0.3)
    scene evan_story_ds_gg_21 with Dissolve(0.3)
    gg 20 "但你，你这个怪物，居然真让我后退了？！" with Dissolve(0.3)
    scene evan_story_ds_gg_22 with Dissolve(0.1)
    pause 0.8
    
    play sound boom_03 volume 2
    
    scene evan_story_ds_gg_23 with vpunch
    pause 1
    scene evan_story_ds_gg_24 with Dissolve(0.5):
        xalign 0.5
        yalign 0.5
        zoom 1
        ease 3 zoom 1.03
    pause 2
    scene evan_story_ds_gg_25 with Dissolve(0.1)
    gg 20 "（不……我不会让自己倒下。不能在这里，不能是现在！）" with Dissolve(0.3)
    scene evan_story_ds_gg_26 with Dissolve(0.3)
    gg 20 "（我的力量……还在我身体里的某个地方。我能感觉到它从内部抓挠着，渴望着冲出来。）" with Dissolve(0.3)
    
    play sound cinematic_boom_1
    
    scene evan_story_ds_gg_27 with Dissolve(0.3)
    gg 19 "（要是我输了——就全完了。）" with Dissolve(0.3)
    
    play sound7 boom_05
    
    scene evan_story_ds_gg_28 with Dissolve(0.3)
    gg 19 "（周围这些生物会把我撕成碎片。）" with Dissolve(0.3)
    scene evan_story_ds_gg_29 with Dissolve(0.3)
    gg 19 "我……会拼尽全力……" with Dissolve(0.3)
    scene evan_story_ds_gg_30 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_gg_31 with Dissolve(0.3)
    pause 1.3
    
    play sound cinematic_bass_neuron_rip_f fadein 5
    play sound2 scifi_pulse_vibrating fadein 2
    
    scene evan_story_ds_gg_32 with Dissolve(0.3)
    gg 19 "我……会拼尽全力……" with Dissolve(0.3)
    
    stop sound2 fadeout 1
    stop music3 fadeout 4
    play music2 robert_slump_cinematic_modern_metal_doom
    play sound thunder_2
    play sound4 demian_large_realistic_explosion_2
    play sound5 demian_designed_electric_impact_5
    play sound6 cinematic_whoosh_2
    
    scene evan_story_ds_gg_33 with vpunch:
        xalign 0.5
        yalign 0.5
        zoom 1.05
        ease 5 zoom 1
    gg 21 "我会使出我的全部！！" with Dissolve(0.3)
    
    play sound6 demian_realistic_distant_explosion_2
    play sound7 demian_designed_electric_impact_6
    play sound8 thunder_1
    play sound2 cinematic_whoosh_3
    
    play sound cinematic_whoosh_1
    
    scene evan_story_ds_gg_34 with vpunch:
        xalign 0.5
        yalign 0.5
        zoom 1.05
        ease 2 zoom 1
    pause 1.5
    scene evan_story_ds_gg_35 with vpunch
    pause 1
    scene evan_story_ds_gg_36 with Dissolve(0.5)
    gg 21 "看清楚了，混蛋……" with Dissolve(0.3)
    scene evan_story_ds_gg_37 with Dissolve(0.3)
    gg 21 "现在让你见识一下，谁才是真正的怪物……" with Dissolve(0.3)
    
    play sound zip_whoosh
    stop music2 fadeout 4
    
    scene black with Dissolve(0.3)
    pause 1
    pause 2
    
    ##### EVAN - 2
    
    play music3 music_loop_ashes_and_rubble_ominous_swelling_dark_full_1 fadein 3
    
    scene evan_story_ds_286 with Dissolve(1.0)
    pause 1.2
    scene evan_story_ds_287 with Dissolve(0.3)
    evan 3 "看起来我们成功了……" with Dissolve(0.3)
    scene evan_story_ds_288 with Dissolve(0.3)
    player_woman1 2 "它死了吗？" with Dissolve(0.3)
    
    play sound cinematic_impact_1
    
    pause 0.3
    scene evan_story_ds_289 with hpunch
    figure 1 "它肯定死了，玩家们！" with Dissolve(0.3)
    scene evan_story_ds_290 with Dissolve(0.3)
    figure 1 "我第一次不得不说，你们完成了一次相当高质量的击杀。" with Dissolve(0.3)
    scene evan_story_ds_291 with Dissolve(0.3)
    evan 3 "什么！？你一直在看着我们！？" with Dissolve(0.3)
    scene evan_story_ds_292 with Dissolve(0.3)
    figure 1 "不是全程，但最有意思的部分当然在看！这才是重点！" with Dissolve(0.3)
    scene evan_story_ds_293 with Dissolve(0.3)
    evan 3 "因为你们，除了我们全都死了！" with Dissolve(0.3)
    
    show evan_story_ds_294 with Dissolve(0.3)
    figure 1 "这几乎总是如此。能在关键时刻解锁潜力的人极少。" with Dissolve(0.3)
    figure 1 "但这次，你们两个都做到了！这已经够棒了！"
    show evan_story_ds_295 with Dissolve(0.3)
    hide evan_story_ds_294
    player_woman1 2 "为、为什么要逼我们经历这一切……" with Dissolve(0.3)
    player_woman1 2 "那个在房子里的家伙……他为我们牺牲了！"
    figure 1 "也就是说你们也必须为了他继续战斗下去。否则他的牺牲就白费了。对吧亲爱的玩家？" with Dissolve(0.3)
    show evan_story_ds_296 with Dissolve(0.3)
    hide evan_story_ds_295
    evan 3 "这些力量……是你让它们在恰好的时刻觉醒的吗？" with Dissolve(0.3)
    figure 1 "完全不是！你们是自己觉醒力量的。而且你们心里清楚得很。那是一种无可错认的感觉。" with Dissolve(0.3)
    figure 1 "我们每个人体内都蕴藏着非凡的潜力，但正如你们亲眼所见的，能正确解锁它的人寥寥无几。"
    evan 3 "那个人为我们丢了命。为什么他的力量没有觉醒？" with Dissolve(0.3)
    show evan_story_ds_294 with Dissolve(0.3)
    hide evan_story_ds_296
    figure 1 "谁知道呢。也许他血脉里的潜质比你们少了一滴。" with Dissolve(0.3)
    figure 1 "或者，为他人牺牲的觉悟与不惜代价求生的觉悟，本就是两回事。"
    player_woman1 2 "他……他叫什么名字？" with Dissolve(0.3)
    show evan_story_ds_295 with Dissolve(0.3)
    hide evan_story_ds_294
    figure 1 "他叫利亚姆。是城里一家健身房的教练。他有老婆和两个孩子，一男一女。" with Dissolve(0.3)
    player_woman1 2 "你们这些怪物……" with Dissolve(0.3)
    figure 1 "我们跟你一样。现在跟你完全一样。在我第一场游戏里，我也曾为一起行动的人哀悼。" with Dissolve(0.3)
    figure 1 "我是唯一的幸存者，但我把对他的悲痛转化成了力量。也希望你能做到。"
    show evan_story_ds_296 with Dissolve(0.3)
    hide evan_story_ds_295
    figure 1 "顺便说一句，我不建议你拿怒气来撒在我身上。我可不是那种能随便威胁、还不用付代价的人。" with Dissolve(0.3)
    evan 3 "{cps=5}……{/cps}" with Dissolve(0.3)
    show evan_story_ds_294 with Dissolve(0.3)
    hide evan_story_ds_296
    figure 1 "好了，感伤的话说够了。进入正题！" with Dissolve(0.3)
    figure 1 "你们赢了，任务完成！恭喜！"
    figure 1 "现在可以从尸体中取出灵魂石，回去领取奖励了。"
    show evan_story_ds_296 with Dissolve(0.3)
    hide evan_story_ds_294
    evan 3 "灵魂石……在尸体里面？" with Dissolve(0.3)
    figure 1 "这些尸体曾经活生生，意味着里面装着灵魂。很合理，对吧？那么，让我说得更清楚些。" with Dissolve(0.3)
    show evan_story_ds_297 with Dissolve(0.3)
    hide evan_story_ds_296
    figure 1 "你们需要找到空间裂隙——最近的一个就在那道拱门里。" with Dissolve(0.3)
    figure 1 "你们可以借此打开通往人类世界的传送门。方法很简单，把灵魂石扔进裂隙。"
    
    scene evan_story_ds_298 with Dissolve(0.3)
    figure 1 "门只会开几秒，一个人通过后就会立刻关闭。" with Dissolve(0.3)
    scene evan_story_ds_299 with Dissolve(0.3)
    figure 1 "你们可以造出更稳定的门。这需要三颗灵魂石。" with Dissolve(0.3)
    scene evan_story_ds_300 with Dissolve(0.3)
    figure 1 "这样就能让好几个人通过，持续时间也更长。" with Dissolve(0.3)
    scene evan_story_ds_301 with Dissolve(0.3)
    figure 1 "看来我没漏讲什么。" with Dissolve(0.3)
    scene evan_story_ds_302 with Dissolve(0.3)
    pause 0.7
    
    play sound knife_blade_1 volume 0.5
    
    scene evan_story_ds_303 with Dissolve(0.3)
    figure 1 "不过我想你们今天可能用得上这个！" with Dissolve(0.3)
    
    play sound2 knife_into_dirt
    
    scene evan_story_ds_304 with Dissolve(0.3)
    pause 1
    
    play sound3 evil_boom_3
    
    scene evan_story_ds_305 with Dissolve(0.3)
    figure 1 "祝你们好运！也欢迎加入信徒的行列——不管你们命中注定要在其中待多久！" with Dissolve(0.3)
    
    play sound4 up_in_smoke volume 2
    
    scene evan_story_ds_306 with vpunch
    pause 0.6
    
    play sound5 woosh0
    
    scene evan_story_ds_307 with Dissolve(0.3)
    pause 1.6
    scene evan_story_ds_308 with Dissolve(0.3)
    evan 3 "等等！可是我们该怎么……" with Dissolve(0.3)
    scene evan_story_ds_309 with Dissolve(0.3)
    evan 2 "可恶！" with Dissolve(0.3)
    scene evan_story_ds_310 with Dissolve(0.3)
    player_woman1 2 "我明白了。也就是说，要回去我们至少还需要一颗石头。最好两颗。" with Dissolve(0.3)
    scene evan_story_ds_311 with Dissolve(0.3)
    player_woman1 2 "这具身体里有几颗？" with Dissolve(0.3)
    scene evan_story_ds_312 with Dissolve(0.3)
    evan 2 "我猜只有一颗。" with Dissolve(0.3)
    scene evan_story_ds_313 with Dissolve(0.3)
    evan 2 "（如果我没理解错——这场游戏从设计上就没打算让所有幸存者都赢。）" with Dissolve(0.3)
    scene evan_story_ds_314 with Dissolve(0.3)
    player_woman1 2 "喂，这颗石头具体在哪儿？" with Dissolve(0.3)
    scene evan_story_ds_315 with Dissolve(0.3)
    evan 2 "不知道。也许在头里？" with Dissolve(0.3)
    scene evan_story_ds_316 with Dissolve(0.3)
    player_woman1 2 "灵魂石，对吧？我觉得应该在心脏。" with Dissolve(0.3)
    evan 2 "随你便。反正我们也得在这堆污秽里翻找。" with Dissolve(0.3)
    scene evan_story_ds_317 with Dissolve(0.3)
    player_woman1 2 "我来试试剖开胸腔。" with Dissolve(0.3)
    scene evan_story_ds_318 with Dissolve(0.3)
    pause 0.8
    
    play sound blood_gore_impact_1
    play sound2 knife_slash_4 volume 2
    
    scene evan_story_ds_319 with Dissolve(0.2)
    pause 0.6
    
    play sound3 knife_blade_2 volume 0.5
    play sound4 blood_gore_impact_2 volume 0.4
    
    scene evan_story_ds_320 with Dissolve(0.3)
    pause 0.8
    scene evan_story_ds_321 with Dissolve(0.3)
    player_woman1 2 "结果没那么难找——它在发光！" with Dissolve(0.3)
    scene evan_story_ds_322 with Dissolve(0.3)
    player_woman1 2 "但这里只有一颗……" with Dissolve(0.3)
    scene evan_story_ds_323 with Dissolve(0.3)
    evan 2 "（我们真得回去再找一颗吗？）" with Dissolve(0.3)
    scene evan_story_ds_324 with Dissolve(0.3)
    evan 2 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    play sound evilwhoosh1
    
    scene evan_story_ds_325 with Dissolve(0.3)
    evan 3 "（又是那股血腥味……）" with Dissolve(0.3)
    scene evan_story_ds_326 with Dissolve(0.3)
    evan 3 "（味道不太一样，不是从尸体那边来的。）" with Dissolve(0.3)
    
    play sound3 boom_03
    
    scene evan_story_ds_327 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_328 with Dissolve(0.3)
    evan 3 "你看到了吗？" with Dissolve(0.3)
    scene evan_story_ds_329 with Dissolve(0.3)
    player_woman1 2 "那边有人！我能感觉到他的存在。" with Dissolve(0.3)
    scene evan_story_ds_330 with Dissolve(0.3)
    evan 3 "（他们？她感觉到了好几个人？）" with Dissolve(0.3)
    scene evan_story_ds_331 with Dissolve(0.3)
    evan 3 "（不是靠气味？）" with Dissolve(0.3)
    scene evan_story_ds_332 with Dissolve(0.3)
    player_woman1 2 "喂，你！出来！" with Dissolve(0.3)
    
    play music2 the_horror_loop
    stop music3 fadeout 5
    
    scene evan_story_ds_333 with Dissolve(0.3)
    pause 0.8
    scene evan_story_ds_334 with Dissolve(0.3)
    player_woman1 2 "不可能……" with Dissolve(0.3)
    scene evan_story_ds_335 with Dissolve(0.3)
    evan 3 "（他还活着？！）" with Dissolve(0.3)
    evan 3 "（是我们丢下的那个罪犯吗？！）"
    
    play sound cinematic_boom_1
    
    scene evan_story_ds_336 with Dissolve(0.3)
    evan 3 "（他的眼睛……）" with Dissolve(0.3)
    scene evan_story_ds_337 with Dissolve(0.3)
    player_prisoner 2 "你们抛弃了我……" with Dissolve(0.3)
    scene evan_story_ds_338 with Dissolve(0.3)
    player_prisoner 2 "你怎么能把同伴丢下等死？！" with Dissolve(0.3)
    scene evan_story_ds_339 with Dissolve(0.3)
    player_woman1 2 "你们当时举止古怪！我们怕他会伤害我们！" with Dissolve(0.3)
    scene evan_story_ds_340 with Dissolve(0.3)
    evan 3 "（既然那怪物已经死了，他也能回来了吗？）" with Dissolve(0.3)
    scene evan_story_ds_341 with Dissolve(0.3)
    evan 3 "（可他怎么知道任务内容的？……难道那个斗篷男也告诉他跟我们一样的话了？）" with Dissolve(0.3)
    scene evan_story_ds_342 with Dissolve(0.3)
    evan 3 "嘿，都过去了！你一定也感觉到了跟我们一样。身体上的变化，你注意到了吗？" with Dissolve(0.3)
    scene evan_story_ds_343 with Dissolve(0.3)
    player_prisoner 2 "之所以过去了，只因为我一个人活了下来。一个人，你懂吗？！" with Dissolve(0.3)
    scene evan_story_ds_344 with Dissolve(0.3)
    player_prisoner 2 "那其他人都在哪儿，嗯？" with Dissolve(0.3)
    scene evan_story_ds_345 with Dissolve(0.3)
    player_prisoner 2 "早就死了吧？可悲的杂种。" with Dissolve(0.3)
    scene evan_story_ds_346 with Dissolve(0.3)
    player_woman1 2 "我们被袭击了……只剩下我们。" with Dissolve(0.3)
    
    play sound man_giggling_gleefully
    
    scene evan_story_ds_347 with Dissolve(0.3)
    player_prisoner 2 "哈哈哈！正义……何等命运的讽刺！" with Dissolve(0.3)
    scene evan_story_ds_348 with Dissolve(0.3)
    player_prisoner 2 "他们都是因为你抛下我才死的！" with Dissolve(0.3)
    scene evan_story_ds_349 with Dissolve(0.3)
    player_prisoner 2 "现在……现在你们要变成我的奖励！" with Dissolve(0.3)
    scene evan_story_ds_350 with Dissolve(0.3)
    evan 3 "别做蠢事！我们有两个人！" with Dissolve(0.3)
    scene evan_story_ds_351 with Dissolve(0.3)
    player_prisoner 2 "那正好！" with Dissolve(0.3)
    scene evan_story_ds_352 with Dissolve(0.3)
    player_prisoner 2 "这意味着我能从你们身上再拿两颗石头！" with Dissolve(0.3)
    scene evan_story_ds_353 with Dissolve(0.3)
    player_woman1 2 "两颗？你在说什么？" with Dissolve(0.3)
    scene evan_story_ds_354 with Dissolve(0.3)
    player_woman1 2 "我们只有一颗！" with Dissolve(0.3)
    scene evan_story_ds_355 with Dissolve(0.3)
    player_prisoner 2 "哈……所以你们还没搞明白？白痴……" with Dissolve(0.3)
    scene evan_story_ds_356 with Dissolve(0.3)
    player_prisoner 2 "看！" with Dissolve(0.3)
    scene evan_story_ds_357 with Dissolve(0.3)
    player_woman1 2 "怎么可能？！那东西你从哪儿弄来的？你也杀了那种东西吗？" with Dissolve(0.3)
    player_prisoner 2 "{cps=5}……{/cps}"
    scene evan_story_ds_358 with Dissolve(0.3)
    player_prisoner 2 "你们丢下我之后，那个混蛋袭击了我。砍掉了我一条胳膊。但我活下来了。" with Dissolve(0.3)
    scene evan_story_ds_359 with Dissolve(0.3)
    player_prisoner 2 "我回去把那个书呆子的身体当诱饵，甩掉了怪物。" with Dissolve(0.3)
    scene evan_story_ds_360 with Dissolve(0.3)
    player_prisoner 2 "在那片混乱中，我感到某种新的东西。身体发生了变化。" with Dissolve(0.3)
    scene evan_story_ds_361 with Dissolve(0.3)
    pause 0.5
    scene evan_story_ds_362 with Dissolve(0.3)
    player_prisoner 2 "然后……我感到疼痛退去，力量重新充满身体！跟你一样吧？" with Dissolve(0.3)
    scene evan_story_ds_363 with Dissolve(0.3)
    evan 3 "你对他做了什么？" with Dissolve(0.3)
    scene evan_story_ds_362 with Dissolve(0.3)
    player_prisoner 2 "我走近那个书呆子时，他的身体看起来只是一块肉。但当我撕开他的外衣，我看到了……" with Dissolve(0.3)
    player_prisoner 2 "我看到他胸口的那团光。"
    player_prisoner 2 "我好奇那他妈是什么，想都没想就把他剖开，取了出来……"
    scene evan_story_ds_364 with Dissolve(0.3)
    player_woman1 2 "你……你为了石头把他剖开了？！" with Dissolve(0.3)
    scene evan_story_ds_365 with Dissolve(0.3)
    player_prisoner 2 "正是如此。" with Dissolve(0.3)
    scene evan_story_ds_366 with Dissolve(0.3)
    player_prisoner 2 "我拿到手的那一刻，感觉到更强大的力量涌来。然后……我的胳膊长回来了。看？" with Dissolve(0.3)
    scene evan_story_ds_367 with Dissolve(0.3)
    player_prisoner 2 "我他妈是不死之身！" with Dissolve(0.3)
    scene evan_story_ds_368 with Dissolve(0.3)
    evan 3 "（他的胳膊像壁虎尾巴一样长回来了？！）" with Dissolve(0.3)
    scene evan_story_ds_369 with Dissolve(0.3)
    player_woman1 2 "你这白痴跟我们一样！" with Dissolve(0.3)
    scene evan_story_ds_370 with Dissolve(0.3)
    player_prisoner 2 "不不不。你完全搞错了！" with Dissolve(0.3)
    scene evan_story_ds_371 with Dissolve(0.3)
    player_prisoner 2 "难道你那女性逻辑理解不了我看得到你们未愈合的伤口吗？" with Dissolve(0.3)
    scene evan_story_ds_372 with Dissolve(0.3)
    evan 3 "（确实，他身上一点伤都没有……除了胳膊上的血迹。这说明我们每个人得到的能力不同。）" with Dissolve(0.3)
    scene evan_story_ds_373 with Dissolve(0.3)
    evan 3 "（我获得了敏锐的嗅觉。她似乎用别的方式感知他人。但那个家伙……）" with Dissolve(0.3)
    scene evan_story_ds_374 with Dissolve(0.3)
    evan 3 "（他获得了再生能力？）" with Dissolve(0.3)
    scene evan_story_ds_375 with Dissolve(0.3)
    evan 3 "你根本不知道我们的能力是什么，那为什么要独自对上我们两个人冒险？" with Dissolve(0.3)
    scene evan_story_ds_376 with Dissolve(0.3)
    player_prisoner 2 "哈……你根本不明白自己在跟谁作对。你以为你那点可怜本事能拦住我？" with Dissolve(0.3)
    scene evan_story_ds_377 with Dissolve(0.3)
    player_prisoner 2 "你就像我已经读过的书。" with Dissolve(0.3)
    scene evan_story_ds_378 with Dissolve(0.3)
    player_prisoner 2 "你……你不过是一条狗。闻味道的野兽，像沙漠里嗅腐肉的胡狼。" with Dissolve(0.3)
    scene evan_story_ds_379 with Dissolve(0.3)
    evan 3 "什……你刚才说什么……" with Dissolve(0.3)
    
    play sound boom_01
    
    scene evan_story_ds_380 with Dissolve(0.3)
    player_prisoner 2 "你很弱，嗅探者。" with Dissolve(0.3)
    scene evan_story_ds_381 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_382 with Dissolve(0.3)
    player_prisoner 2 "还有你……你的能力更有意思，但一样可悲。" with Dissolve(0.3)
    player_prisoner 2 "你能感知周围的人，能感知他们对你的意图是善是恶。"
    player_prisoner 2 "就像雷达，把人标记成友方或敌方。"
    scene evan_story_ds_383 with Dissolve(0.3)
    player_woman1 2 "你怎么知道？！怎么可能？！" with Dissolve(0.3)
    
    play sound2 man_giggling_gleefully
    
    scene evan_story_ds_384 with Dissolve(0.1)
    player_prisoner 2 "哈哈哈！" with Dissolve(0.1)
    
    play sound3 evil_boom_1
    
    scene evan_story_ds_385 with Dissolve(0.3)
    player_prisoner 2 "我一眼就把你们看穿了。把同伴丢下的可悲杂种。" with Dissolve(0.3)
    scene evan_story_ds_386 with Dissolve(0.3)
    player_prisoner 2 "我比你们老练得多。在获得这些力量之前我就在杀人。而现在……" with Dissolve(0.3)
    scene evan_story_ds_387 with Dissolve(0.3)
    player_prisoner 2 "现在我的人生终于有意义了。所以为什么要浪费在你们这些可悲的废话上？" with Dissolve(0.3)
    scene evan_story_ds_388 with Dissolve(0.3)
    player_prisoner 2 "你最好祈祷。或者主动投降，我让你死得痛快些。" with Dissolve(0.3)
    scene evan_story_ds_389 with Dissolve(0.3)
    evan 3 "（他彻底疯了！）" with Dissolve(0.3)
    evan 3 "（让他变强的不只是再生能力。）"
    evan 3 "（他……他能读懂我们。看见我们看不见的东西。）"
    scene evan_story_ds_390 with Dissolve(0.3)
    evan 3 "他已经不是人了，他是怪物……" with Dissolve(0.3)
    scene evan_story_ds_391 with Dissolve(0.3)
    player_woman1 2 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene evan_story_ds_392 with Dissolve(0.3)
    player_prisoner 2 "死亡是从恐惧中解脱，生命则是与恐惧同处。" with Dissolve(0.3)
    scene evan_story_ds_393 with Dissolve(0.3)
    player_prisoner 2 "但恐惧的只有你们。你的恐惧就是我的奖励！" with Dissolve(0.3)
    scene evan_story_ds_394 with Dissolve(0.3)
    pause 0.3
    
    play sound demian_distant_boom_1 volume 2
    stop music2 fadeout 5
    $ renpy.music.set_volume(0.2, delay=0, channel=u'music3')
    play music3 horror_loop fadein 10
    
    scene evan_story_ds_395 with vpunch
    pause 0.3
    scene evan_story_ds_396 with Dissolve(0.3)
    pause 0.8
    scene evan_story_ds_397 with Dissolve(0.1)
    pause 0.3
    scene evan_story_ds_398 with Dissolve(0.5)
    pause 1
    
    play sound2 demian_distant_boom_2 volume 2
    
    scene evan_story_ds_399 with vpunch
    pause 0.3
    scene evan_story_ds_400 with Dissolve(0.5)
    pause 0.8
    
    play sound3 demian_distant_boom_3 volume 2
    $ renpy.music.set_volume(0.4, delay=2, channel=u'music3')
    
    scene evan_story_ds_401 with vpunch
    pause 0.3
    scene evan_story_ds_402 with Dissolve(0.3)
    evan 3 "这、这他妈到底怎么回事？！" with Dissolve(0.1)
    scene evan_story_ds_403 with Dissolve(0.3)
    player_woman1 2 "我感觉到某种极其危险的东西正在逼近！" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=2, channel=u'music3')
    play sound cinematic_whoosh_3
    
    scene evan_story_ds_404 with Dissolve(0.3)
    player_prisoner 2 "那就是你的死期逼近了，女人！" with Dissolve(0.3)
    scene evan_story_ds_405 with Dissolve(0.2)
    pause 0.7
    
    play sound2 fight_swing_1
    
    scene evan_story_ds_406 with Dissolve(0.2)
    pause 1
    
    play sound3 fight_swing_2
    
    scene evan_story_ds_407 with Dissolve(0.3)
    pause 0.7
    
    play sound4 fight_swing_3
    
    scene evan_story_ds_408 with Dissolve(0.3)
    pause 0.8
    
    play sound4 demian_distant_boom_2 volume 2.4
    play sound6 demian_designed_electric_impact_6 volume 0.2
    play sound7 evil_boom_4
    play sound8 heavy_body_fall_01
    play sound2 heavy_body_fall_02
    play sound3 heavy_body_fall_03
    
    scene evan_story_ds_409 with vpunch
    pause 0.5
    scene evan_story_ds_410 with Dissolve(0.5)
    pause 0.7
    scene evan_story_ds_411 with Dissolve(0.3)
    pause 0.7
    
    play sound fight_swing_4
    
    scene evan_story_ds_412 with Dissolve(0.2)
    pause 1
    
    play sound blood_gore_impact_4 volume 0.4
    play sound2 kick_3
    play sound3 tinnitus fadein 3 volume 0.5
    $ renpy.music.set_volume(0.1, delay=2, channel=u'music3')
    
    scene evan_story_ds_413 with hpunch
    pause 1
    
    scene black with Dissolve(0.5)
    pause 0.5
    
    scene evan_story_ds_414 with Dissolve(1.3)
    pause 0.5
    
    stop sound3 fadeout 3
    $ renpy.music.set_volume(1, delay=3, channel=u'music3')
    
    scene evan_story_ds_415 with Dissolve(0.2)
    evan 3 "（你这混蛋！）" with Dissolve(0.1)
    scene evan_story_ds_416 with Dissolve(0.3)
    pause 1
    
    play sound4 fight_swing_3
    
    scene evan_story_ds_417 with Dissolve(0.2)
    pause 0.8
    
    play sound4 fight_blocks_1
    
    scene evan_story_ds_418 with Dissolve(0.2)
    pause 0.6
    
    play sound5 knife_blade_1 volume 0.3
    play sound6 cinematic_whoosh_2
    
    scene evan_story_ds_419 with Dissolve(0.3)
    evan 3 "已经忘了我？！" with Dissolve(0.3)
    scene evan_story_ds_420 with Dissolve(0.3)
    pause 0.5
    scene evan_story_ds_421 with Dissolve(0.3)
    pause 0.6
    
    play sound2 fight_punch_backofhead_1
    
    scene evan_story_ds_422 with vpunch
    pause 0.5
    
    play sound3 fight_blocks_2
    
    scene evan_story_ds_423 with Dissolve(0.3)
    player_woman1 2 "我、我拖住他！快解决他！" with Dissolve(0.3)
    
    play sound5 knife_blade_2 volume 0.3
    
    scene evan_story_ds_424 with Dissolve(0.3)
    evan 3 "啊啊啊！" with Dissolve(0.1)
    
    play sound2 blood_gore_impact_5 volume 0.5
    play sound3 fight_blocks_3
    
    scene evan_story_ds_425 with hpunch
    pause 0.7
    
    play sound5 kick_4 volume 0.5
    
    scene evan_story_ds_426 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_427 with Dissolve(0.3)
    evan 3 "诶？……" with Dissolve(0.3)
    scene evan_story_ds_428 with Dissolve(0.3)
    pause 0.8
    scene evan_story_ds_429 with Dissolve(0.3)
    evan 3 "我、我刚才做了什么……？" with Dissolve(0.3)
    scene evan_story_ds_430 with Dissolve(0.3)
    player_woman1 2 "你这该死的滑头……" with Dissolve(0.3)
    scene evan_story_ds_431 with Dissolve(1.0)
    pause 0.5
    evan 3 "不……不！" with Dissolve(0.1)
    scene evan_story_ds_432 with Dissolve(0.3)
    evan 3 "{cps=5}……{/cps}"
    scene evan_story_ds_433 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_434 with Dissolve(0.3)
    pause 0.7
    
    play sound demian_distant_boom_1 volume 3
    
    scene evan_story_ds_435 with vpunch
    pause 0.3
    
    play sound2 demian_distant_boom_2 volume 3
    play sound3 minotaur_mythical_beast_the_minotaur
    
    scene evan_story_ds_436 with vpunch
    pause 0.3
    scene evan_story_ds_437 with Dissolve(0.3)
    pause 0.2
    scene evan_story_ds_438 with Dissolve(0.3)
    pause 1
    
    play sound3 minotaur_pain_moan_1
    play sound4 kick_1
    stop music3 fadeout 5
    
    scene evan_story_ds_439 with vpunch
    pause 0.6
    scene evan_story_ds_440 with Dissolve(0.3)
    pause 1
    
    play sound minotaur_mythical_beast_the_minotaur
    play music2 robert_slump_cinematic_modern_metal_doom_p1 noloop
    
    scene evan_story_ds_441 with Dissolve(0.3)
    pause 0.7
    scene evan_story_ds_442 with Dissolve(0.6)
    pause 1
    scene evan_story_ds_443 with Dissolve(0.5)
    pause 0.8
    scene evan_story_ds_444 with Dissolve(0.5)
    pause 1.5
    scene evan_story_ds_445 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_446 with Dissolve(0.3)
    pause 0.8
    scene evan_story_ds_447 with Dissolve(0.3)
    pause 0.7
    
    play sound demian_designed_electric_impact_5 volume 1.2
    play sound2 demian_designed_electric_impact_6 volume 2
    play sound3 evil_boom_1
    
    scene evan_story_ds_448 with Dissolve(0.1)
    pause 0.5
    
    play sound4 demian_designed_electric_impact_5 volume 1.5
    play sound5 demian_large_realistic_explosion_2
    play sound6 cinematic_impact_1
    
    scene evan_story_ds_449 with hpunch
    pause 0.4
    scene evan_story_ds_450 with Dissolve(0.1)
    pause 0.6
    
    play sound demian_designed_electric_impact_5 volume 1.2
    play sound2 demian_designed_electric_impact_6 volume 2
    play sound3 zip_whoosh
    play sound4 dsgnbass_clock_wind_down_slomo
    play sound5 demian_downer_1
    
    scene evan_story_ds_451 with hpunch:
        xalign 0.5
        yalign 0.5
        zoom 1.05
        ease 5 zoom 1
    pause 4
    
    play sound demian_whoosh_hit_1
    
    scene evan_story_ds_452 with Dissolve(0.2)
    pause 0.8
    
    play sound2 demian_trailer_hit
    play sound3 minotaur_pain_moan_2
    play sound4 kick_2
    play sound5 blood_gore_impact_3
    
    scene evan_story_ds_453 with hpunch
    pause 0.5
    scene evan_story_ds_454 with Dissolve(0.2)
    pause 0.8
    
    play sound blood_gore_impact_4
    
    scene evan_story_ds_455 with Dissolve(0.3)
    pause 1
    
    play sound heavy_body_fall_03 volume 2
    play sound2 kick_3 
    
    scene evan_story_ds_456 with vpunch
    pause 1
    scene evan_story_ds_457 with Dissolve(0.5):
        xalign 0.5
        yalign 0.5
        zoom 1.05
        ease 5 zoom 1
    pause 4
    
    $ renpy.music.set_volume(0.3, delay=0, channel=u'music5')
    play music5 thriller_drone_looped fadein 4
    stop music2 fadeout 5
    
    scene evan_story_ds_458 with Dissolve(0.1)
    player_prisoner 2 "还有你他妈是谁？！" with Dissolve(0.3)
    scene evan_story_ds_459 with Dissolve(0.3)
    evan 3 "（又一个恶魔？！）" with Dissolve(0.3)
    evan 3 "（一个外表跟人类无异，但我从他身上感觉到巨大的力量。）"
    
    play sound cinematic_boom_1
    $ renpy.music.set_volume(1, delay=4, channel=u'music5')
    
    show evan_story_ds_460 with Dissolve(0.1)
    $ renpy.pause (3.8, hard=True)
    
    scene evan_story_ds_461 with Dissolve(0.3)
    player_prisoner 2 "什……？" with Dissolve(0.3)
    scene evan_story_ds_462 with Dissolve(0.3)
    player_prisoner 2 "这……不可能。我看到的是什么？！" with Dissolve(0.3)
    scene evan_story_ds_463 with Dissolve(0.3)
    player_prisoner 2 "我……读不懂他。你的力量……是错的！" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.2, delay=1, channel=u'music5')
    play music3 robert_slump_cinematic_modern_metal_doom_p4 noloop
    
    scene evan_story_ds_464 with Dissolve(0.3)
    pause 1
    
    play sound fight_swing_1
    
    scene evan_story_ds_465 with Dissolve(0.2)
    pause 0.7
    
    play sound fight_swing_3
    
    scene evan_story_ds_466 with Dissolve(0.2)
    pause 0.5
    
    play sound fight_blocks_4
    $ renpy.music.set_volume(0.5, delay=20, channel=u'music5')
    
    scene evan_story_ds_467 with hpunch
    player_prisoner 2 "咕啊……" with Dissolve(0.3)
    scene evan_story_ds_468 with Dissolve(0.3)
    player_prisoner 2 "你、你到底是什么怪物？" with Dissolve(0.3)
    scene evan_story_ds_469 with Dissolve(0.3)
    pause 0.8
    scene evan_story_ds_470 with Dissolve(0.2)
    pause 0.7
    
    play sound2 blood_gore_impact_4
    
    scene evan_story_ds_471 with hpunch
    pause 0.5
    
    play sound3 blood_gore_impact_5
    $ renpy.music.set_volume(1, delay=5, channel=u'music5')
    
    scene evan_story_ds_472 with hpunch
    pause 1
    
    scene evan_story_ds_473 with Dissolve(0.1)
    evan 3 "哦……操……" with Dissolve(0.3)
    show evan_story_ds_474:
        xpos 0
        ease 0.5 xpos -400
    play sound woosh1 volume 0.5
    show evan_story_ds_475:
        xpos 900
        ease 0.5 xpos 0
    pause 2
    scene evan_story_ds_476 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_477 with Dissolve(0.3)
    pause 1
    
    play sound knife_into_dirt volume 2
    
    scene evan_story_ds_478 with Dissolve(0.3)
    pause 1
    
    play sound2 kick_4 volume 0.5
    stop music3 fadeout 1
    
    scene evan_story_ds_479 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_480 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_481 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_482 with Dissolve(0.3)
    gg 21 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene evan_story_ds_483 with Dissolve(0.3)
    gg 21 "灵魂石。" with Dissolve(0.3)
    scene evan_story_ds_484 with Dissolve(0.3)
    evan 2 "嗯？" with Dissolve(0.3)
    
    play sound fight_blocks_3 volume 0.4
    
    scene evan_story_ds_485 with vpunch
    evan 2 "哎哟哎哟！" with Dissolve(0.3)
    scene evan_story_ds_486 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_487 with Dissolve(0.3)
    evan 2 "是、是是，在这儿，在这儿，求你别杀我！" with Dissolve(0.3)
    scene evan_story_ds_488 with Dissolve(0.3)
    evan 2 "我只有这些！" with Dissolve(0.3)
    scene evan_story_ds_489 with Dissolve(0.3)
    gg 21 "这是实话吗？" with Dissolve(0.3)
    scene evan_story_ds_490 with Dissolve(0.3)
    evan 2 "我没有取过别的！怪物尸体旁边那个女孩拿走了一颗，我发誓！" with Dissolve(0.3)
    scene evan_story_ds_489 with Dissolve(0.3)
    gg 21 "出口在哪儿？" with Dissolve(0.3)
    scene evan_story_ds_491 with Dissolve(0.3)
    evan 2 "出、出口？" with Dissolve(0.3)
    scene evan_story_ds_492 with Dissolve(0.3)
    evan 2 "啊，那个裂、裂隙……在那边！" with Dissolve(0.3)
    scene evan_story_ds_493 with Dissolve(0.3)
    evan 2 "往那边走一点你就能看见那道拱门。" with Dissolve(0.3)
    scene evan_story_ds_494 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_495 with Dissolve(0.1)
    pause 1.5
    scene evan_story_ds_496 with Dissolve(0.5)
    pause 1
    
    $ renpy.music.set_volume(0.3, delay=1, channel=u'music5')
    play sound2 tinnitus fadein 3 loop
    play sound4 blood_gush_2 volume 0.6
    $ renpy.music.set_volume(0.5, delay=0, channel=u'sound7')
    play sound7 male_choking_panting_full fadein 2
    
    scene evan_story_ds_497 with hpunch
    pause 0.7
    
    $ renpy.music.set_volume(0.5, delay=0, channel=u'sound7')
    play sound7 male_choking_panting_full loop volume 0.4
    
    scene evan_story_ds_498 with Dissolve(0.3)
    pause 1
    
    $ renpy.music.set_volume(1, delay=0.3, channel=u'sound7')
    
    scene evan_story_ds_499 with Dissolve(0.3)
    pause 1
    
    $ renpy.music.set_volume(0, delay=0.3, channel=u'sound7')
    play sound6 blood_gush_1
    
    scene evan_story_ds_500 with hpunch
    pause 0.8
    scene evan_story_ds_501 with Dissolve(0.3)
    pause 1
    
    $ renpy.music.set_volume(1, delay=0.3, channel=u'sound7')
    $ renpy.music.set_volume(1, delay=2, channel=u'music5')
    stop sound2 fadeout 4
    stop sound7 fadeout 1
    
    gg 20 "靠……" with Dissolve(0.3)
    
    stop music5 fadeout 4
    play music2 mysterious_and_spooky_loop fadein 0.3
    
    scene evan_story_ds_502 with Dissolve(0.3)
    wanchan 1 "就打算这样回去？……就这副样子？" with Dissolve(0.3)
    
    play sound scary_male_evil_laugh_2
    
    scene evan_story_ds_503 with Dissolve(0.3)
    wanchan 1 "哈哈哈！" with Dissolve(0.3)
    scene evan_story_ds_504 with Dissolve(0.3)
    wanchan 1 "呼！闻起来像……英雄味。还是烤肉味？" with Dissolve(0.3)
    scene evan_story_ds_505 with Dissolve(0.3)
    wanchan 1 "老大，这些恶魔是你烤的，还是它们把你烤了？" with Dissolve(0.3)
    scene evan_story_ds_506 with Dissolve(0.3)
    gg 20 "你想要什么？" with Dissolve(0.3)
    scene evan_story_ds_507 with Dissolve(0.3)
    wanchan 1 "你看起来就像流动的美学犯罪现场。" with Dissolve(0.3)
    scene evan_story_ds_508 with Dissolve(0.3)
    wanchan 1 "就这副样子回现实？浑身是血、满身泥、还半裸着？" with Dissolve(0.3)
    scene evan_story_ds_509 with Dissolve(0.3)
    wanchan 2 "你妈在地铁里会晕倒，警察会开枪。" with Dissolve(0.3)
    scene evan_story_ds_510 with Dissolve(0.3)
    gg 20 "说重点。我要回去。" with Dissolve(0.3)
    scene evan_story_ds_511 with Dissolve(0.3)
    wanchan 1 "是是是，英雄总是这么急。不过听我说一句。" with Dissolve(0.3)
    scene evan_story_ds_512 with Dissolve(0.3)
    wanchan 1 "我把这件小杰作给你。能盖住血迹、气味和罪孽，还增添些格调。" with Dissolve(0.3)
    scene evan_story_ds_513 with Dissolve(0.3)
    wanchan 1 "但是……" with Dissolve(0.3)
    scene evan_story_ds_514 with Dissolve(0.3)
    wanchan 1 "作为交换，你给我一颗灵魂石。" with Dissolve(0.3)
    scene evan_story_ds_515 with Dissolve(0.3)
    wanchan 1 "就一颗。小意思吧？" with Dissolve(0.3)
    scene evan_story_ds_516 with Dissolve(0.3)
    gg 20 "这交易不公平。"
    scene evan_story_ds_517 with Dissolve(0.3)
    wanchan 1 "暗界没有公平的交易，只有必要的交易。" with Dissolve(0.3)
    scene evan_story_ds_518 with Dissolve(0.3)
    wanchan 1 "你不想一走出去就被当成恶魔吧？不想吓到等着你的人吧？" with Dissolve(0.3)
    scene evan_story_ds_519 with Dissolve(0.3)
    gg 20 "我宁愿浑身沾满屎走出去，也不为一件外套交出石头。何况这儿的尸体随随便便都能扒到衣服。" with Dissolve(0.3)
    scene evan_story_ds_520 with Dissolve(0.3)
    wanchan 1 "就你这身板，只有我的能穿。试试。" with Dissolve(0.3)
    
    play sound cinematic_swish_hit_1
    
    scene evan_story_ds_521 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_522 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_523 with Dissolve(0.3)
    gg 22 "行，算你狠。现在归我了。" with Dissolve(0.3)
    scene evan_story_ds_524 with Dissolve(0.3)
    wanchan 3 "到了地狱也要有style。" with Dissolve(0.3)
    scene evan_story_ds_525 with Dissolve(0.3)
    wanchan 3 "哦呵呵……真是美人，你身上有四颗呢……" with Dissolve(0.3)
    
    show evan_story_ds_527 with Dissolve(0.3)
    wanchan 3 "我可以给你别的东西。不过我担心你会独自离开，把那位可怜的家伙扔在这儿再找一颗石头。" with Dissolve(0.3)
    show evan_story_ds_526 with Dissolve(0.3)
    hide evan_story_ds_527
    gg 22 "我不管他。他有刀，可以从那个女孩身上割一颗出来。" with Dissolve(0.3)
    show evan_story_ds_527 with Dissolve(0.3)
    hide evan_story_ds_526
    wanchan 3 "你真是冷酷……而这太棒了！" with Dissolve(0.3)
    wanchan 3 "那么，我恳请你看看我的其他货品……"
    show evan_story_ds_526 with Dissolve(0.3)
    hide evan_story_ds_527
    gg 22 "钱。" with Dissolve(0.3)
    show evan_story_ds_527 with Dissolve(0.3)
    hide evan_story_ds_526
    wanchan 3 "钱？" with Dissolve(0.3)
    show evan_story_ds_526 with Dissolve(0.3)
    hide evan_story_ds_527
    gg 22 "我对现金感兴趣。两颗灵魂石换。" with Dissolve(0.3)
    show evan_story_ds_527 with Dissolve(0.3)
    hide evan_story_ds_526
    wanchan 3 "嗯……老板，你也知道，大概……十五万我都能出。" with Dissolve(0.3)
    show evan_story_ds_526 with Dissolve(0.3)
    hide evan_story_ds_527
    gg 22 "十五万？！两颗石头？！" with Dissolve(0.3)
    show evan_story_ds_527 with Dissolve(0.3)
    hide evan_story_ds_526
    wanchan 3 "没错！" with Dissolve(0.3)
    show evan_story_ds_526 with Dissolve(0.3)
    hide evan_story_ds_527
    gg 22 "两条命？！" with Dissolve(0.3)
    gg 22 "你们在暗界待久了，脑子烧坏了吧？"
    show evan_story_ds_527 with Dissolve(0.3)
    hide evan_story_ds_526
    wanchan 3 "嘿嘿，你还能指望什么？" with Dissolve(0.3)
    wanchan 3 "在这里，这样一颗石头最多给一万。"
    show evan_story_ds_526 with Dissolve(0.3)
    hide evan_story_ds_527
    gg 22 "一条命才一万……" with Dissolve(0.3)
    show evan_story_ds_527 with Dissolve(0.3)
    hide evan_story_ds_526
    wanchan 3 "没办法啊。要是给得更多——这儿一半的杂碎为了点白菜都能互相砍。" with Dissolve(0.3)
    wanchan 3 "这就是经济学。"
    wanchan 3 "或者说是疯狂……哈哈哈……或者两者本来就是一回事。"
    show evan_story_ds_526 with Dissolve(0.3)
    hide evan_story_ds_527
    gg 22 "这场杂耍是你挑起的。把牌摊开吧。你出多少？" with Dissolve(0.3)
    show evan_story_ds_527 with Dissolve(0.3)
    hide evan_story_ds_526
    wanchan 3 "好吧，看你这张苦脸，还有我未来几个不眠之夜……" with Dissolve(0.3)
    wanchan 3 "就……十八吧。"
    show evan_story_ds_526 with Dissolve(0.3)
    hide evan_story_ds_527
    gg 22 "它们颜色不一样。" with Dissolve(0.3)
    show evan_story_ds_527 with Dissolve(0.3)
    hide evan_story_ds_526
    wanchan 3 "哦呵呵，那就更有意思了。蓝色的比绿色的贵一点……确实。" with Dissolve(0.3)
    
    scene evan_story_ds_528 with Dissolve(0.3)
    gg 22 "二十一。快点，别让我想到把你也变成商品。" with Dissolve(0.3)
    scene evan_story_ds_529 with Dissolve(0.3)
    wanchan 3 "哈哈哈哈！就这股劲头，你肯定饿不死。" with Dissolve(0.3)
    scene evan_story_ds_530 with Dissolve(0.3)
    wanchan 3 "二十一——成交。" with Dissolve(0.3)
    scene evan_story_ds_531 with Dissolve(0.3)
    wanchan 3 "你知道吗……我几乎不敢想下一家会被你榨成什么样。" with Dissolve(0.3)
    scene evan_story_ds_532 with Dissolve(0.3)
    pause 1
    $ renpy.notify ("你得到 21000 美元")
    $ aksha += 21000
    
    play sound money_1 volume 0.5
    
    scene evan_story_ds_533 with Dissolve(0.3)
    gg 22 "按这个汇率——我得在这儿搞一场屠杀了。" with Dissolve(0.3)
    
    play sound2 cinematic_whoosh_1
    
    scene evan_story_ds_534 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_535 with Dissolve(0.3)
    gg 22 "它们归你了。拿走吧。" with Dissolve(0.3)
    scene evan_story_ds_536 with Dissolve(0.3)
    wanchan 3 "真没礼貌……" with Dissolve(0.3)
    scene evan_story_ds_537 with Dissolve(0.3)
    wanchan 3 "不过，一手交钱一手交货！" with Dissolve(0.3)
    scene evan_story_ds_538 with Dissolve(0.5)
    pause 1
    scene evan_story_ds_539 with Dissolve(0.3)
    wanchan 3 "别忘了再来找我！也许到那时你已经学会微笑了……" with Dissolve(0.3)
    scene evan_story_ds_540 with Dissolve(0.3)
    pause 1
    scene evan_story_ds_541 with Dissolve(0.3)
    pause 0.8
    scene evan_story_ds_542 with Dissolve(0.3)
    
    play sound3 entering_portal_1 volume 1.5
    
    pause 1
    
    stop music2 fadeout 3
    
    scene black with Dissolve(0.5)
    pause 2
    pause 2
    
    jump homecoming_gangdebt

###### TOWN - GANG DEBT

label homecoming_gangdebt:
    
    play music3 busy_city_street_traffic_loop_full volume 0.5 fadein 1
    
    scene homecoming_gangdebt_0 with Dissolve(2.0):
        xalign 0.5
        yalign 0.5
        zoom 1.05
        linear 3.5 zoom 1
    pause 3
    
    stop music3 fadeout 3
    
    scene homecoming_gangdebt_1 with Dissolve(0.5)
    pause 2
    
    play sound2 mc_house_elevator
    
    scene homecoming_gangdebt_2 with Dissolve(0.3)
    pause 1
    
    show homecoming_gangdebt_2_9 with Dissolve(0.1)
    pause 0.9
    show homecoming_gangdebt_2_10 with Dissolve(0.1)
    hide homecoming_gangdebt_2_9
    pause 0.8
    show homecoming_gangdebt_2_11 with Dissolve(0.1)
    hide homecoming_gangdebt_2_10
    pause 0.7
    show homecoming_gangdebt_2_12 with Dissolve(0.1)
    hide homecoming_gangdebt_2_11
    pause 0.6
    show homecoming_gangdebt_2_13 with Dissolve(0.1)
    hide homecoming_gangdebt_2_12
    pause 0.5
    show homecoming_gangdebt_2_14 with Dissolve(0.1)
    hide homecoming_gangdebt_2_13
    pause 0.4
    show homecoming_gangdebt_2_15 with Dissolve(0.1)
    hide homecoming_gangdebt_2_14
    pause 0.4
    show homecoming_gangdebt_2_16 with Dissolve(0.1)
    hide homecoming_gangdebt_2_15
    pause 0.5
    show homecoming_gangdebt_2_17 with Dissolve(0.1)
    hide homecoming_gangdebt_2_16
    pause 0.6
    show homecoming_gangdebt_2_18 with Dissolve(0.1)
    hide homecoming_gangdebt_2_17
    pause 0.8
    show homecoming_gangdebt_2_19 with Dissolve(0.1)
    hide homecoming_gangdebt_2_18
    pause 1
    
    scene homecoming_gangdebt_3 with Dissolve(0.3)
    pause 1.5
    scene homecoming_gangdebt_4 with Dissolve(0.3)
    pause 0.6
    
    stop sound2 fadeout 1
    play music2 the_suspense_mystery fadein 5
    play sound3 knock_on_door_7 volume 0.5
    
    mi 7 "你想要什么？" with Dissolve(0.3)
    scene homecoming_gangdebt_5 with Dissolve(0.3)
    mi 7 "这么晚了，你找她做什么？" with Dissolve(0.3)
    scene homecoming_gangdebt_6 with Dissolve(0.3)
    jae_wook0 1 "你只要把栗原[may]叫出来就行……" with Dissolve(0.3)
    scene homecoming_gangdebt_7 with Dissolve(0.3)
    mi 7 "这么晚？！" with Dissolve(0.3)
    scene homecoming_gangdebt_8 with Dissolve(0.3)
    mi 7 "我现在就报警！" with Dissolve(0.3)
    scene homecoming_gangdebt_9 with Dissolve(0.3)
    do_hyun0 1 "你再不快点，我们就只能……" with Dissolve(0.3)
    scene homecoming_gangdebt_10 with Dissolve(0.3)
    gg 22 "有什么问题吗？" with Dissolve(0.3)
    scene homecoming_gangdebt_11 with Dissolve(0.3)
    mi 7 "[gg]？！" with Dissolve(0.3)
    scene homecoming_gangdebt_12 with Dissolve(0.3)
    may 16 "[gg]？" with Dissolve(0.3)
    scene homecoming_gangdebt_13 with Dissolve(0.3)
    gg 22 "他们是我的熟人……" with Dissolve(0.3)
    scene homecoming_gangdebt_14 with Dissolve(0.3)
    gg 22 "别担心，姑娘们，我们只是聊几句。很快就回来。" with Dissolve(0.3)
    
    scene black with Dissolve(0.5)
    pause 0.5
    
    play music4 busy_city_street_traffic_loop_full volume 0.2 fadein 1
    
    scene homecoming_gangdebt_15 with Dissolve(0.5)
    pause 1
    jae_wook0 1 "他的脸怎么了？" with Dissolve(0.3)
    scene homecoming_gangdebt_16 with Dissolve(0.5)
    do_hyun0 1 "谁知道呢。看起来这小子除了我们之外还摊上了别的麻烦。" with Dissolve(0.3)
    scene homecoming_gangdebt_17 with Dissolve(0.3)
    gg 22 "（他们是谁？）" with Dissolve(0.3)
    scene homecoming_gangdebt_18 with Dissolve(0.3)
    gg 22 "（为什么在找[may]，又怎么会知道她的名字？）" with Dissolve(0.3)
    
    stop music4 fadeout 10
    
    scene homecoming_gangdebt_19 with Dissolve(0.3)
    do_hyun0 1 "Kang-hyung，人我们带来了……看来这小子在替她操心。" with Dissolve(0.3)
    scene homecoming_gangdebt_20 with Dissolve(0.3)
    do_hyun0 1 "他很平静地跟着我们，没惹麻烦。" with Dissolve(0.3)
    scene homecoming_gangdebt_21 with Dissolve(0.3)
    do_hyun0 1 "然后前门后面有个女孩哭着喊了他的名字。会不会就是栗原[may]本人？" with Dissolve(0.3)
    scene homecoming_gangdebt_22 with Dissolve(0.5)
    pause 1.5
    scene homecoming_gangdebt_23 with Dissolve(0.3)
    kang_seok0 1 "道贤，我说过一万遍了——别想、别猜，只管照我的命令做。思考是我的工作。" with Dissolve(0.3)
    scene homecoming_gangdebt_24 with Dissolve(0.3)
    kang_seok0 1 "把人送到、必要时把他们的脸打烂——这是你的活。" with Dissolve(0.3)
    scene homecoming_gangdebt_25 with Dissolve(0.3)
    kang_seok0 1 "不过现在先尽量别声张。我们谁都不想多惹麻烦。" with Dissolve(0.3)
    scene homecoming_gangdebt_26 with Dissolve(0.3)
    kang_seok0 1 "对吧，小子？" with Dissolve(0.3)
    gg 22 "{cps=5}……{/cps}" with Dissolve(0.3)
    kang_seok0 1 "那他的脸怎么说，道贤？你说他没惹麻烦。" with Dissolve(0.3)
    scene homecoming_gangdebt_27 with Dissolve(0.3)
    do_hyun 1 "不知道，我们碰上他的时候就是这样。" with Dissolve(0.3)
    scene homecoming_gangdebt_28 with Dissolve(0.3)
    kang_seok0 1 "那么，你跟栗原健是什么关系？我不记得他有个儿子。" with Dissolve(0.3)
    scene homecoming_gangdebt_29 with Dissolve(0.3)
    gg 22 "（他在说她父亲？这些就是他欠钱的那帮人。）" with Dissolve(0.3)
    gg 22 "你来早了。我记得你说还剩十三天。"
    scene homecoming_gangdebt_28 with Dissolve(0.3)
    kang_seok0 1 "时间在走啊，小子。债在涨，你看起来一点也不急着还。" with Dissolve(0.3)
    scene homecoming_gangdebt_29 with Dissolve(0.3)
    gg 22 "时候还没到。我会还上他的债。现在别来烦我们。" with Dissolve(0.3)
    kang_seok0 1 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene homecoming_gangdebt_30 with Dissolve(0.3)
    kang_seok0 1 "跟长辈说话这么没礼貌。兄弟们，教教他我们怎么处理不敬。" with Dissolve(0.3)
    scene homecoming_gangdebt_31 with Dissolve(0.3)
    do_hyun 1 "是，大哥！" with Dissolve(0.3)
    scene homecoming_gangdebt_32 with Dissolve(0.3)
    kang_seok0 1 "就是别……打得太狠。" with Dissolve(0.3)
    scene homecoming_gangdebt_33 with Dissolve(0.3)
    jae_wook0 1 "按住他的胳膊。" with Dissolve(0.3)
    scene homecoming_gangdebt_34 with Dissolve(0.3)
    jae_wook0 1 "既然你老老实实跟着来了，我们就速战速决。" with Dissolve(0.3)
    scene homecoming_gangdebt_35 with Dissolve(0.3)
    jae_wook0 1 "你得忍一下，会有点疼。" with Dissolve(0.3)
    jae_wook0 1 "喂，按紧了！"
    do_hyun 1 "可怜的小子，替别人扛债。" with Dissolve(0.3)
    
    play sound cigarette_burning_1 volume 0.6
    
    scene homecoming_gangdebt_36 with Dissolve(0.3)
    do_hyun 1 "你为什么自己出来，而不是栗原[may]？" with Dissolve(0.3)
    jae_wook0 1 "老大才不会下令让我们打她。" with Dissolve(0.3)
    scene homecoming_gangdebt_37 with Dissolve(0.3)
    do_hyun 1 "他会自己先玩个尽兴，就像昨天对那些女孩一样，记得吧？" with Dissolve(0.3)
    scene homecoming_gangdebt_38 with Dissolve(0.3)
    kang_seok0 1 "喂！都他妈把嘴给我闭上！大哥在城里的时候，一个字都不许提！" with Dissolve(0.3)
    scene homecoming_gangdebt_39 with Dissolve(0.3)
    kang_seok0 1 "你们他妈知不知道他知道了会有多惨？！" with Dissolve(0.3)
    scene homecoming_gangdebt_40 with Dissolve(0.3)
    do_hyun 1 "当然，大哥。只是……他就是个普通小子……" with Dissolve(0.3)
    scene homecoming_gangdebt_41 with Dissolve(0.3)
    kang_seok0 1 "我说了，闭上你们他妈愚蠢的嘴！现在就给我揍他！" with Dissolve(0.1)
    scene homecoming_gangdebt_42 with Dissolve(0.3)
    pause 0.6
    kang_seok0 1 "怎么，小子，不害怕？" with Dissolve(0.3)
    kang_seok0 1 "你看起来要么彻底疯了，要么就是从没被人一拳打在牙上。"
    scene homecoming_gangdebt_43 with Dissolve(0.3)
    pause 1
    
    play sound fight_swing_1
    
    scene homecoming_gangdebt_44 with Dissolve(0.2)
    pause 0.8
    
    play sound2 fight_punches_hollywood_1
    stop music2 fadeout 3
    play music3 trigubovich_cinematic_tension_background_loop
    
    scene homecoming_gangdebt_45 with hpunch
    pause 0.6
    scene homecoming_gangdebt_46 with Dissolve(0.2)
    kang_seok0 1 "...!" with Dissolve(0.1)
    scene homecoming_gangdebt_47 with Dissolve(0.2)
    jae_wook0 1 "你个小婊子！" with Dissolve(0.3)
    
    play sound fight_swing_2 volume 2
    
    scene homecoming_gangdebt_48 with hpunch
    pause 0.6
    scene homecoming_gangdebt_49 with Dissolve(0.3)
    jae_wook0 1 "你他妈死定了！" with Dissolve(0.1)
    scene homecoming_gangdebt_50 with Dissolve(0.3)
    kang_seok0 1 "哥们……你们认真的吗……" with Dissolve(0.3)
    
    play sound fight_blocks_1
    
    scene homecoming_gangdebt_51 with hpunch
    pause 0.8
    
    play sound2 fight_punches_hollywood_2
    
    scene homecoming_gangdebt_52 with hpunch
    pause 1
    
    play sound3 kick_3
    play sound4 fight_blocks_2
    
    scene homecoming_gangdebt_53 with vpunch
    pause 1
    
    play sound5 fight_blocks_3
    
    scene homecoming_gangdebt_54 with hpunch
    pause 0.7
    
    play sound6 metal_hit volume 2
    
    scene homecoming_gangdebt_55 with vpunch
    pause 2
    scene homecoming_gangdebt_56 with Dissolve(0.3)
    kang_seok0 1 "他还是个孩子，就算还手也……" with Dissolve(0.3)
    scene homecoming_gangdebt_57 with Dissolve(0.3)
    kang_seok0 1 "怎么，对付女人和老人之后，连怎么正确讨债都忘了！？" with Dissolve(0.3)
    
    play sound fight_blocks_4 volume 2
    
    scene homecoming_gangdebt_58 with Dissolve(0.1)
    do_hyun 1 "你干脆去死吧，混蛋！" with Dissolve(0.3)
    scene homecoming_gangdebt_59 with Dissolve(0.2)
    do_hyun 1 "在雅，我抓住他了！" with Dissolve(0.3)
    scene homecoming_gangdebt_60 with Dissolve(0.3)
    pause 0.8
    
    play sound2 fight_punches_gutbonebreakes_1
    
    scene homecoming_gangdebt_61 with hpunch
    pause 0.6
    
    play sound3 fight_punch_backofhead_1
    
    scene homecoming_gangdebt_62 with hpunch
    pause 0.8
    
    play sound4 kick_3 volume 0.4
    
    scene homecoming_gangdebt_63 with Dissolve(0.3)
    kang_seok0 1 "嗯……现在连空手道课都教这个了吗？" with Dissolve(0.3)
    scene homecoming_gangdebt_64 with Dissolve(0.3)
    gg 22 "你今天不该出来。" with Dissolve(0.3)
    scene homecoming_gangdebt_65 with Dissolve(0.3)
    kang_seok0 1 "你看起来可不像普通高中生啊。" with Dissolve(0.3)
    scene homecoming_gangdebt_66 with Dissolve(0.3)
    kang_seok0 1 "哈哈哈……真没想到，谁能想到，我居然在跟一个学生小子打架……" with Dissolve(0.3)
    scene homecoming_gangdebt_67 with Dissolve(0.3)
    kang_seok0 1 "以我的身份，为了一个孩子弄脏自己的手……" with Dissolve(0.3)
    
    play sound2 cinematic_boom_1
    
    scene homecoming_gangdebt_68 with Dissolve(0.1)
    pause 0.8
    
    play sound fight_swing_3 volume 3
    
    scene homecoming_gangdebt_69 with hpunch
    gg 22 "（好快！）" with Dissolve(0.1)
    scene homecoming_gangdebt_70 with Dissolve(0.3)
    kang_seok0 1 "哈，你也不简单……" with Dissolve(0.3)
    
    play sound3 fight_blocks_2
    
    scene homecoming_gangdebt_71 with hpunch
    pause 0.6
    
    play sound4 fight_blocks_3
    
    scene homecoming_gangdebt_72 with hpunch
    pause 0.4
    scene homecoming_gangdebt_73 with Dissolve(0.3)
    pause 0.8
    
    play sound5 fight_swing_4 volume 2
    
    scene homecoming_gangdebt_74 with hpunch
    pause 0.8
    
    play sound6 fight_swing_1 volume 3
    
    scene homecoming_gangdebt_75 with hpunch
    pause 1
    scene homecoming_gangdebt_76 with Dissolve(0.3)
    kang_seok0 1 "抓到你了！" with Dissolve(0.3)
    
    play sound7 fight_punches_gutbonebreakes_4
    
    scene homecoming_gangdebt_77 with hpunch
    pause 1
    
    play sound8 dirt_hit volume 0.4
    
    scene homecoming_gangdebt_78 with hpunch
    pause 1
    scene homecoming_gangdebt_79 with Dissolve(0.3)
    kang_seok0 1 "你知道吗，你让我想起一个人。" with Dissolve(0.3)
    scene homecoming_gangdebt_80 with Dissolve(0.3)
    pause 1
    scene homecoming_gangdebt_81 with Dissolve(0.3)
    gg 22 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene homecoming_gangdebt_82 with Dissolve(0.3)
    kang_seok0 1 "你到底是谁啊？" with Dissolve(0.3)
    scene homecoming_gangdebt_83 with Dissolve(0.3)
    gg 22 "你告诉我名字，我就回答。" with Dissolve(0.3)
    scene homecoming_gangdebt_84 with Dissolve(0.3)
    kang_seok0 1 "真是个嘴硬的混蛋……行吧，那我就打到你自己说出来……" with Dissolve(0.3)
    scene homecoming_gangdebt_85 with Dissolve(0.3)
    kang_seok0 1 "是谁派你来的？你跟栗原健是什么关系？还有，你这身本事是跟谁学的？" with Dissolve(0.3)
    scene homecoming_gangdebt_86 with Dissolve(0.3)
    gg 22 "等我把债还上，你就知道了。" with Dissolve(0.3)
    scene homecoming_gangdebt_87 with Dissolve(0.3)
    kang_seok0 1 "觉得自己很能打是吧？！" with Dissolve(0.3)
    scene homecoming_gangdebt_88 with Dissolve(0.3)
    kang_seok0 1 "那从现在起，我可要动真格的了！" with Dissolve(0.3)
    
    play sound2 fight_punches_gutbonebreakes_3
    
    scene homecoming_gangdebt_89 with hpunch
    pause 0.8
    
    play sound4 fight_swing_2 volume 3
    
    scene homecoming_gangdebt_90 with hpunch
    kang_seok0 1 "来吧，小子，让我看看……" with Dissolve(0.3)
    scene homecoming_gangdebt_91 with Dissolve(0.2):
        xalign 0.5
        yalign 0.5
        zoom 1.05
        ease 1 zoom 1
    kang_seok0 1 "让我看看你到底有多少斤两！" with Dissolve(0.1)
    
    play sound2 fight_blocks_4
    
    scene homecoming_gangdebt_92 with hpunch
    pause 0.8
    
    play sound3 fight_punches_gutbonebreakes_2
    
    scene homecoming_gangdebt_93 with hpunch
    pause 0.6
    scene homecoming_gangdebt_94 with Dissolve(0.3)
    pause 0.8
    scene homecoming_gangdebt_95 with Dissolve(0.3)
    pause 1
    scene homecoming_gangdebt_96 with Dissolve(0.5):
        xalign 0.5
        yalign 0.5
        zoom 1.05
        ease 1 zoom 1
    kang_seok0 1 "...!" with Dissolve(0.1)
    
    play sound fight_punches_hollywood_3
    play sound2 blood_gore_impact_1 volume 0.5
    
    scene homecoming_gangdebt_97 with hpunch
    pause 0.8
    scene homecoming_gangdebt_98 with Dissolve(0.2)
    pause 0.6
    
    play sound3 fight_punches_gutbonebreakes_4
    
    scene homecoming_gangdebt_99 with hpunch
    pause 0.8
    
    play sound fight_punches_hollywood_4
    play sound2 blood_gore_impact_2 volume 0.5
    
    scene homecoming_gangdebt_100 with hpunch
    pause 1
    scene homecoming_gangdebt_101 with Dissolve(0.3):
        xalign 0.5
        yalign 0.5
        zoom 1.05
        ease 2 zoom 1
    kang_seok0 1 "什么？！……" with Dissolve(0.1)
    
    play sound kick_1 volume 0.5
    stop music3 fadeout 4
    play music2 the_suspense_mystery fadein 4
    
    scene homecoming_gangdebt_102 with vpunch
    pause 0.5
    kang_seok0 1 "咳……哈……我没想到还能再遇到这样的人……" with Dissolve(0.3)
    scene homecoming_gangdebt_103 with Dissolve(0.3)
    gg 22 "什么样？" with Dissolve(0.3)
    scene homecoming_gangdebt_104 with Dissolve(0.3)
    kang_seok0 1 "那个眼神……" with Dissolve(0.3)
    scene homecoming_gangdebt_105 with Dissolve(0.5)
    kang_seok0 1 "你的眼睛……你的招式……靠，跟他一模一样……" with Dissolve(0.3)
    pause 1
    
    stop music2 fadeout 4
    
    scene black with Dissolve(1.0)
    pause 2
    pause 2
    
    jump date_event_1_intro

###### DATE EVENT - START

label date_event_1_intro:

    play music4 science_documentary_loop fadein 5
    
    scene date_event_1_intro_1 with Dissolve(1.5)
    gg 2 "（可恶，最近这几天简直疯了一样。）" with Dissolve(0.3)
    gg 2 "（感觉过去一周发生的事，比我之前整个人生都多。）"
    scene date_event_1_intro_2 with Dissolve(0.5)
    gg 2 "（昨天跟那帮混混的冲突……我只跟[mi]和[may]说是我自己解决的。）" with Dissolve(0.3)
    gg 2 "（[mi]好像很平静，到家还给我发了消息。）"
    gg 2 "（但[may]看起来完全懵了……她的眼神暴露了她有多害怕。）"
    
    scene black with Dissolve(0.5)
    pause 0.5
    scene date_event_1_intro_3 with Dissolve(0.5)
    gg 2 "（好吧，难得休几天，也许我该带[may]出去散散心、看场电影？）" with Dissolve(0.3)
    gg 2 "（尤其那晚鸡尾酒的事之后，我们之间好像还隔着一堵墙。）"
    gg 2 "（而且一起看电影一直是我放松、忘掉外界烦恼的好方式。）"
    gg 2 "（至少有那么几个小时，我们可以做回从前的样子，窝在电视前。）"
    
    scene black with Dissolve(0.5)
    pause 1
    scene date_event_1_intro_4 with Dissolve(1.0)
    gg 2 "（我记得连爸爸以前有时也跟我们一起看电影。）" with Dissolve(0.3)
    scene date_event_1_intro_5 with Dissolve(0.5)
    gg 2 "（他喜欢老动作片——周末会放出来，像某种家庭仪式。）" with Dissolve(0.3)
    scene date_event_1_intro_6 with Dissolve(0.5)
    gg 2 "（[may]以前总惊叹女主角怎么翻过汽车的。）" with Dissolve(0.3)
    gg 2 "（而我坐在那儿数主角换弹匣前开了多少枪。）"
    scene date_event_1_intro_7 with Dissolve(0.5)
    gg 2 "（要是有暴力或者床戏……）" with Dissolve(0.3)
    scene date_event_1_intro_8 with Dissolve(0.5)
    gg 2 "（……他会捂住[may]的耳朵，我就遮住她的眼睛。）" with Dissolve(0.3)
    
    scene black with Dissolve(0.5)
    pause 0.5
    
    scene date_event_1_intro_9 with Dissolve(0.5)
    gg 2 "（幸好那次[may]从节庆上带回来的碟片我们没一起看。）" with Dissolve(0.3)
    scene date_event_1_intro_10 with Dissolve(0.5)
    gg 2 "（她很喜欢封面，结果那却是重口里番。）" with Dissolve(0.3)
    scene date_event_1_intro_11 with Dissolve(0.5)
    gg 2 "（是啊，幻想世界什么事都可能发生，但要是把哥布林暴力这个主题挖掘得这么细致……）" with Dissolve(0.3)
    
    scene black with Dissolve(0.5)
    pause 0.5
    
    scene date_event_1_intro_12 with Dissolve(0.5)
    gg 2 "（好了，我在想什么呢。今天没有里番。）" with Dissolve(0.3)
    scene date_event_1_intro_13 with Dissolve(0.5)
    gg 2 "{cps=5}……{/cps}"
    gg 2 "（昨天还被箭刺穿的那只手，现在看起来像什么都没发生过。不痛，也没疤。就……跟新的一样。）" with Dissolve(0.3)
    scene date_event_1_intro_14 with Dissolve(0.5)
    gg 2 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    scene black with Dissolve(0.5)
    pause 0.5
    
    scene date_event_1_intro_15 with Dissolve(0.5)
    gg 2 "（我可以给[li]发条消息。不知道她怎么样了？）" with Dissolve(0.3)
    gg 2 "（她对那个一直纠缠她的前任只字不提，这让我很在意。）"
    gg 2 "（我不清楚她具体需要什么，但看起来她不想说。）"
    gg 2 "（也许我该去见见她，聊聊。甚至帮她把那个混蛋解决掉。）"
    gg 2 "（不过大部分情况下，我说不准自己该不该插手。）"
    gg 2 "（但……她见到那个人时的反应，明显没有让她高兴。）"
    gg 2 "（而且她对我从不会那样。也许她在等我主动？）"
    gg 2 "（不管怎样，见到她我会很高兴。这段时间我们处得挺好。）"
    
    if lillian_hotel_choice_leave == False:
        scene date_event_1_intro_16 with Dissolve(1.0)
        gg 2 "（甚至可以说，我们已经不止是朋友了。）" with Dissolve(0.3)
        
    scene black with Dissolve(0.5)
    pause 0.5
    gg 2 "{cps=5}……{/cps}"
    
    scene date_event_1_intro_17 with Dissolve(1.0)
    gg 2 "（如果她不介意的话，今天也许也能见见[mi]。）" with Dissolve(0.3)
    gg 2 "（我想跟她分享发生在我身上的事……但算了，现在不谈这个。）"
    gg 2 "（为什么什么事都要跟恶魔还有那些破事扯上关系？）"
    gg 2 "（我们可以像普通人那样共度时光，不带任何神秘色彩。）"
    gg 2 "（见面、喝咖啡、散散步……甚至可以就去上次认识的那家咖啡馆。）"
    gg 2 "（不过我现在手头有点钱，可以带她去个更好的地方。毕竟她是个成年女性，值得。）"
    gg 2 "（她很有趣，而且只要她对我有一点点好感，我想她不会拒绝。）"
    
    scene black with Dissolve(0.5)
    pause 0.5
    
    show date_event_1_intro_18 with Dissolve(1.0)
    gg 2 "（但如果今天去见她或者[li]，大概就没时间看完[may]准备的全部电影了。）" with Dissolve(0.3)
    gg 2 "（我只有两天。）"
    gg 2 "（第一天只陪[may]。第二天可以在[li]和[mi]之间分。）"
    gg 2 "（反正也用不了那么久……）"
    gg 2 "（如果白天约[mi]，她大概能腾出时间。）"
    gg 2 "（我觉得她晚上可能在批作业或者准备课程。）"
    gg 2 "（嗯……那就先见[mi]，晚上再见[li]。）"
    
    jump date_event_1_choice
    
label date_event_1_choice_newday:
    scene black with Dissolve(0.5)
    pause 0.5
    $ date_event_1_day += 1
    $ date_event_1_after_minami = False
    pause 0.5
    
    if date_event_1_day >= 3:
        jump end_tatsumi
    else:
        show date_event_1_intro_18 with Dissolve(1.0)
        jump date_event_1_choice
        
    
label date_event_1_choice:
    if date_event_1_day >= 3:
        jump end_tatsumi
    else:
        call screen date_event_1_choice_day
    
###### DATE EVENT - MAY
    
label date_event_1_may:
    
    scene black with Dissolve(0.5)
    pause 0.5
    
    scene date_event_1_may_1 with Dissolve(0.5)
    gg 2 "（[may]说她找到了几部不错的恐怖片。）" with Dissolve(0.3)
    scene date_event_1_may_2 with Dissolve(0.5)
    gg 2 "（我敢打赌看一两部之后，她就会想换成自己爱的狗血剧。）" with Dissolve(0.3)
    scene date_event_1_may_3 with Dissolve(0.5)
    pause 0.3
    play sound knock_on_door_3
    pause 0.3
    
    gg 2 "（但这是我很愿意做的牺牲。）" with Dissolve(0.3)
    scene date_event_1_may_4 with Dissolve(0.3)
    gg 2 "（她现在应该在房间里。）" with Dissolve(0.3)
    
    play music cute_delights_loop fadein 5
    stop music4 fadeout 5
    
    scene date_event_1_may_5 with Dissolve(0.3)
    may 17 "[gg]！要敲门的话，至少先等一下回应啊！" with Dissolve(0.3)
    scene date_event_1_may_6 with Dissolve(0.3)
    may 17 "万一我还没穿好衣服呢？" with Dissolve(0.3)
    scene date_event_1_may_7 with Dissolve(0.3)
    gg 2 "那也没什么不寻常的。我们互相看光过好几次了。" with Dissolve(0.3)
    scene date_event_1_may_8 with Dissolve(0.3)
    may 17 "那都是好久以前的事了！" with Dissolve(0.3)
    scene date_event_1_may_9 with Dissolve(0.3)
    may 17 "笨蛋。" with Dissolve(0.3)
    scene date_event_1_may_10 with Dissolve(0.3)
    gg 2 "我想问一下：接下来几个小时你有空吗？" with Dissolve(0.3)
    scene date_event_1_may_11 with Dissolve(0.3)
    
    if date_event_1_day == 1:
        may 17 "大概一小时后我本来想出门，逛逛商店，买点衣服。" with Dissolve(0.3)
    if date_event_1_day == 2:
        may 17 "昨天我想去购物来着，挑点东西……但没成。我打算半小时后出门。" with Dissolve(0.3)
    
    scene date_event_1_may_12 with Dissolve(0.3)
    may 17 "现在我连看那条黑裙子都想哭……" with Dissolve(0.3)
    scene date_event_1_may_13 with Dissolve(0.3)
    gg 2 "我有个提议。" with Dissolve(0.3)
    scene date_event_1_may_14 with Dissolve(0.3)
    gg 2 "要不要看那些你为我们电影马拉松准备的片子？" with Dissolve(0.3)
    scene date_event_1_may_15 with Dissolve(0.3)
    may 17 "哇真的吗！？" with Dissolve(0.3)
    scene date_event_1_may_16 with Dissolve(0.3)
    may 17 "我还以为你永远不会提呢！" with Dissolve(0.3)
    scene date_event_1_may_17 with Dissolve(0.3)
    "[may]从床上跳起来，跑到床头柜边。"
    scene date_event_1_may_18 with Dissolve(0.3)
    "她从里面拿出好几包光盘。"
    scene date_event_1_may_19 with Dissolve(0.3)
    gg 2 "（这比我想的顺利多了。）" with Dissolve(0.3)
    
    show date_event_1_may_20 with Dissolve(0.3)
    may 17 "看，这不是爱情片，是真正的恐怖片！" with Dissolve(0.3)
    may 17 "我朋友们去影院看过，说非常吓人而且很特别！"
    gg 2 "只要不无聊就行。上次你找的那部怪文艺片，我看得都快睡着了。" with Dissolve(0.3)
    
    scene date_event_1_may_21 with Dissolve(0.3)
    may 17 "“哟，你不理解Elian Wrayne的作者意图，这说明的可比他本人多多了！”" with Dissolve(0.3)
    scene date_event_1_may_22 with Dissolve(0.3)
    gg 2 "我不跟你争，我又不是潜在影迷。" with Dissolve(0.3)
    scene date_event_1_may_23 with Dissolve(0.3)
    may 17 "那算什么奇怪的说法？" with Dissolve(0.3)
    scene date_event_1_may_24 with Dissolve(0.3)
    may 17 "总之，算了……" with Dissolve(0.3)
    scene date_event_1_may_25 with Dissolve(0.3)
    may 17 "因为我信我朋友，所以顺便把第二部也买了。" with Dissolve(0.3)
    scene date_event_1_may_26 with Dissolve(0.3)
    gg 2 "好吧。不过里面好像还有别的东西。" with Dissolve(0.3)
    scene date_event_1_may_27 with Dissolve(0.3)
    may 17 "还有……那个可是个惊喜！" with Dissolve(0.3)
    scene date_event_1_may_28 with Dissolve(0.3)
    gg 2 "随你怎么说。所以我们就是买薯片，然后被那些诡异笑容吓到？" with Dissolve(0.3)
    scene date_event_1_may_29 with Dissolve(0.3)
    may 17 "没错！" with Dissolve(0.3)
    
    stop music fadeout 2
    
    scene black with Dissolve(1.0)
    pause 0.5
    
    $ renpy.music.set_volume(1, delay=0, channel=u'music2')
    play music2 creepy_fantasy fadein 3
    
    scene date_event_1_may_30 with Dissolve(1.0)
    pause 1
    scene date_event_1_may_31 with Dissolve(1.0)
    pause 1.5
    
    $ renpy.music.set_volume(0.8, delay=2, channel=u'music2')
    
    scene date_event_1_may_32 with Dissolve(0.3)
    gg 2 "所以这个诅咒是随着携带者死亡而传给下一个人的？" with Dissolve(0.3)
    scene date_event_1_may_33 with Dissolve(0.3)
    may 17 "看起来是这样。" with Dissolve(0.3)
    scene date_event_1_may_34 with Dissolve(0.3)
    may 17 "而且能制造幻觉迷惑携带者，在恰好的时机杀死他们。" with Dissolve(0.3)
    scene date_event_1_may_35 with Dissolve(0.3)
    gg 2 "我奇怪，为什么携带者不干脆自我隔离几天，看看诅咒会不会消失？" with Dissolve(0.3)
    scene date_event_1_may_36 with Dissolve(0.3)
    may 17 "可那也可能是幻觉啊，[gg]！" with Dissolve(0.3)
    scene date_event_1_may_37 with Dissolve(0.3)
    may 17 "时间久了，当事人自己都分不清自己做的、看到的是幻觉还是现实！" with Dissolve(0.3)
    scene date_event_1_may_38 with Dissolve(0.3)
    gg 2 "所以这诅咒完全无解？" with Dissolve(0.3)
    scene date_event_1_may_39 with Dissolve(0.3)
    gg 2 "随时你的所有努力都可能被证明是假的，任何行动都可能毫无意义？这也太不公平了。" with Dissolve(0.3)
    scene date_event_1_may_40 with Dissolve(0.3)
    may 17 "哈哈，好像还真是……" with Dissolve(0.3)
    
    scene black with Dissolve(1.0)
    pause 0.5
    
    scene date_event_1_may_41 with Dissolve(1.0)
    "电影走向高潮。主角正在探索一间废弃的房子，准备直面自己的恐惧。"
    "现在一片死寂，而在恐怖片里这只能意味着一件事……"
    
    $ renpy.music.set_volume(0.3, delay=1, channel=u'music2')
    play sound may_movie_screamer_1
    
    scene date_event_1_may_42 with hpunch
    pause 1.5
    
    $ renpy.music.set_volume(0.7, delay=5, channel=u'music2')
    
    scene date_event_1_may_43 with Dissolve(0.3)
    gg 2 "你真有那么害怕？" with Dissolve(0.3)
    scene date_event_1_may_44 with Dissolve(0.3)
    may 17 "这部片本来就是要吓人的啊！所以我被吓到了……" with Dissolve(0.3)
    scene date_event_1_may_45 with Dissolve(0.3)
    may 17 "而且你刚才说那怪物无法逃脱的时候，真的让我毛骨悚然。" with Dissolve(0.3)
    scene date_event_1_may_46 with Dissolve(0.3)
    may 17 "其实那比任何怪物都吓人。" with Dissolve(0.3)
    scene date_event_1_may_47 with Dissolve(0.3)
    may 17 "无法掌控自己的行为。不知道发生在自己身上的是真实还是把戏。" with Dissolve(0.3)
    scene date_event_1_may_48 with Dissolve(0.3)
    gg 2 "（可恶。看起来她又想起那晚鸡尾酒的事了。）" with Dissolve(0.3)
    scene date_event_1_may_49 with Dissolve(0.3)
    gg 2 "[may]，别担心。这只是电影，现实中遇到这种事的概率极低。" with Dissolve(0.3)
    gg 2 "尤其是在发生过那件事之后。"
    scene date_event_1_may_50 with Dissolve(0.3)
    gg 2 "我们对吃的东西、喝的东西、还有做的所有事都会更小心的。好吗？" with Dissolve(0.3)
    gg 2 "（我自己在犯错之前，也得多用脑子想想。）"
    scene date_event_1_may_51 with Dissolve(0.3)
    may 17 "好吧……可我还是不安。万一已经有人在操控我……而我自己都没察觉呢？" with Dissolve(0.3)
    scene date_event_1_may_52 with Dissolve(0.3)
    gg 2 "这已经属于该找心理咨询师的范畴了。" with Dissolve(0.3)
    scene date_event_1_may_53 with Dissolve(0.3)
    may 17 "你什么意思？" with Dissolve(0.3)
    scene date_event_1_may_54 with Dissolve(0.3)
    gg 2 "不过你不是一个人——人类争论自己有没有自由意志，已经争了几个世纪。" with Dissolve(0.3)
    scene date_event_1_may_55 with Dissolve(0.3)
    gg 2 "我们真的能选择自己的行为吗……还是只是在遵循被经验、事件和成长刻进我们体内的东西？" with Dissolve(0.3)
    scene date_event_1_may_56 with Dissolve(0.3)
    gg 2 "谁知道呢……" with Dissolve(0.3)
    scene date_event_1_may_57 with Dissolve(0.3)
    may 17 "当电影里的角色大概很幸福吧。" with Dissolve(0.3)
    scene date_event_1_may_58 with Dissolve(0.3)
    may 17 "编剧已经写好了你和你的每一个举动，你没办法偏离剧本。" with Dissolve(0.3)
    scene date_event_1_may_59 with Dissolve(0.3)
    gg 2 "但这也意味着电影一结束，你也就结束了。那真的算好事吗？" with Dissolve(0.3)
    scene date_event_1_may_60 with Dissolve(0.3)
    may 17 "但你根本不会想到这一层。" with Dissolve(0.3)
    scene date_event_1_may_61 with Dissolve(0.3)
    may 17 "反正最后只有幸福结局或者悲伤结局，仅此而已。" with Dissolve(0.3)
    scene date_event_1_may_62 with Dissolve(0.3)
    gg 2 "[may]，别误会，但我们不会有幸福结局。" with Dissolve(0.3)
    scene date_event_1_may_63 with Dissolve(0.3)
    may 17 "什么？" with Dissolve(0.3)
    scene date_event_1_may_64 with Dissolve(0.3)
    gg 2 "也不会有悲伤结局。我们只是活着——一天又一天，一年又一年。没有开始，也没有结束。" with Dissolve(0.3)
    scene date_event_1_may_65 with Dissolve(0.3)
    gg 2 "只有当下。而把当下变成幸福的，符合我们的最大利益。" with Dissolve(0.3)
    scene date_event_1_may_66 with Dissolve(0.3)
    may 17 "哇……这话说得真好！" with Dissolve(0.3)
    scene date_event_1_may_67 with Dissolve(1.0)
    pause 1
    gg 2 "（与此同时，电影已经走到了为续集铺垫的悲伤结局，而续集的碟片就摆在我们面前。）" with Dissolve(0.3)
    scene date_event_1_may_68 with Dissolve(0.5)
    gg 2 "（[may]似乎已经把那些消极念头挤出脑袋。于是我们顺势开始看第二部。）" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=2, channel=u'music2')
    
    scene date_event_1_may_69 with Dissolve(0.3)
    ''
    
    stop music2 fadeout 2

    scene black with Dissolve(1.0)
    pause 2
    
    play music3 horror_alexunderthesky fadein 10
    
    scene date_event_1_may_70 with Dissolve(0.5)
    pause 2
    
    show date_event_1_may_71 with Dissolve(0.2)
    may 17 "真的很奇怪。这次是换了个新女主角来摆脱诅咒。" with Dissolve(0.3)
    may 17 "但我们为什么要追下去？说不定任何时候一切都可能只是幻觉。"
    show date_event_1_may_72 with Dissolve(0.2)
    hide date_event_1_may_71
    gg 2 "可观众喜欢女主角，就会替她担心、盼她成功，不管发生什么。" with Dissolve(0.3)
    gg 2 "但电影这么赚钱，诅咒肯定不会被随便消除。"
    show date_event_1_may_71 with Dissolve(0.2)
    hide date_event_1_may_72
    may 17 "于是角色受苦，我们看个爽，还因为这样他们能拍更多角色受苦的电影？" with Dissolve(0.3)
    show date_event_1_may_72 with Dissolve(0.2)
    hide date_event_1_may_71
    gg 2 "差不多。" with Dissolve(0.3)
    gg 2 "这在砍杀片里尤其明显，观众只等着看下一个角色会用哪种新鲜方式死去。"
    show date_event_1_may_73 with Dissolve(0.2)
    hide date_event_1_may_72
    may 17 "不过任何类型都可以这么说。" with Dissolve(0.3)
    may 17 "如果人们喜欢伟大英雄建功立业的故事，那就会出更多功绩更大的英雄故事。"
    may 17 "人们喜欢灰姑娘遇到有钱人的电影。"
    may 17 "然后历经无数阴谋和丑闻终于在一起。所以他们会看更多这类女孩的故事！"
    show date_event_1_may_74 with Dissolve(0.2)
    hide date_event_1_may_73
    gg 2 "又或者反过来，主角建立了一个由各类型性感美女组成的后宫的故事也非常受欢迎。" with Dissolve(0.3)
    gg 2 "然后跟她们做些不知羞耻的事。"
    
    scene date_event_1_may_75 with Dissolve(0.3)
    may 17 "[gg]，够了！" with Dissolve(0.3)
    scene date_event_1_may_76 with Dissolve(0.3)
    gg 2 "也就是说会有更多英雄，还有更多性感美女的后宫！" with Dissolve(0.3)
    scene date_event_1_may_77 with Dissolve(0.3)
    may 17 "我们都被带偏了，电影吓人的部分要开始了！" with Dissolve(0.3)
    
    stop music3 fadeout 7
    
    scene black with Dissolve(0.5)
    pause 1.5
    
    play music2 relaxing_lofi_ena__sascha_ende fadein 10
    
    scene date_event_1_may_78 with Dissolve(1.0)
    gg 2 "所以结果整部电影的后半段都是幻觉。不知道下一部会怎么样。" with Dissolve(0.3)
    scene date_event_1_may_79 with Dissolve(0.3)
    may 17 "总有一天编剧大概得摆脱这个诅咒，免得同一套剧情没完没了地重复。" with Dissolve(0.3)
    scene date_event_1_may_80 with Dissolve(0.3)
    gg 2 "我倒不介意有些系列能像《猛鬼街》那样拍到十五部。" with Dissolve(0.3)
    scene date_event_1_may_81 with Dissolve(0.3)
    may 17 "但那多无聊！那些片子就是这么消失的。" with Dissolve(0.3)
    scene date_event_1_may_82 with Dissolve(0.3)
    gg 2 "只不过是那些电影的创作者想象力贫乏。" with Dissolve(0.3)
    scene date_event_1_may_83 with Dissolve(0.3)
    gg 2 "如果有人真的热爱自己的工作，稳稳写出二十部而不掉质量并不难。" with Dissolve(0.3)
    
    show date_event_1_may_84 with Dissolve(0.3)
    may 17 "哦，我想起我有个同学，真正的书虫。" with Dissolve(0.3)
    may 17 "别的女生和我在课间一起玩、去食堂的时候，她整天坐在一个位置看书！"
    may 17 "她连吃饭都在看。"
    may 17 "我曾经瞄过她手上那本书的封面——叫《战斗之矛20000》。"
    may 17 "背面列着这个系列的全部书目，超过五十本！"
    may 17 "我后来跟她聊了一会儿——那上面的书她已经读完三十二本了！"
    show date_event_1_may_85 with Dissolve(0.3)
    hide date_event_1_may_84
    gg 2 "哦，那个世界我听说过。我记得最初是从桌上游戏改编的。" with Dissolve(0.3)
    gg 2 "他们说内容多到有海量的人能完全投身其中，除了这些什么都不聊。"
    show date_event_1_may_84 with Dissolve(0.3)
    hide date_event_1_may_85
    may 17 "呃。那种东西我肯定很快就看腻。" with Dissolve(0.3)
    show date_event_1_may_85 with Dissolve(0.3)
    hide date_event_1_may_84
    gg 2 "我不知道这是好事还是坏事。" with Dissolve(0.3)
    gg 2 "一方面，研究多种事物、不卡在一件事上，确实很有意思。"
    gg 2 "另一方面，那样你可能对任何话题都只有浅层认识。"
    
    scene date_event_1_may_86 with Dissolve(0.3)
    may 17 "[gg]，你又让我消极了！接着看吧！" with Dissolve(0.3)
    
    stop music3 fadeout 10
    play music2 ottoman_palace_version_1 fadein 8 volume 0.7
    
    scene date_event_1_may_87 with Dissolve(0.3)
    "她按下播放，屏幕上出现「壮丽世纪」几个字，字体是华丽的金色。" with Dissolve(0.3)
    scene date_event_1_may_88 with Dissolve(0.3)
    gg 2 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_may_89 with Dissolve(0.3)
    gg 2 "这不是恐怖片吧？" with Dissolve(0.3)
    scene date_event_1_may_90 with Dissolve(0.3)
    may 17 "我可没说今天所有片子都是恐怖片……" with Dissolve(0.3)
    scene date_event_1_may_91 with Dissolve(0.3)
    gg 2 "又是那种穷学生遇上有钱帅哥的狗血剧？" with Dissolve(0.3)
    scene date_event_1_may_92 with Dissolve(0.3)
    may 17 "其实不是，这是系列剧！而且里面没有那样的学生或有钱人。" with Dissolve(0.3)
    scene date_event_1_may_98 with Dissolve(0.3)
    may 17 "好吧，是有钱人，但跟我们之前看的那些不是一个路数。" with Dissolve(0.3)
    scene date_event_1_may_95 with Dissolve(0.3)
    gg 2 "唔……一共有多少集？" with Dissolve(0.3)
    scene date_event_1_may_93 with Dissolve(0.3)
    may 17 "二十六集。这是第一季。" with Dissolve(0.3)
    scene date_event_1_may_94 with Dissolve(0.3)
    gg 2 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_may_95 with Dissolve(0.3)
    gg 2 "我看。那也不算多。" with Dissolve(0.3)
    scene date_event_1_may_96 with Dissolve(0.3)
    may 17 "每集平均两个小时。" with Dissolve(0.3)
    scene date_event_1_may_97 with Dissolve(0.3)
    gg 2 "什么！？" with Dissolve(0.3)
    scene date_event_1_may_98 with Dissolve(0.3)
    may 17 "整部系列一共一百四十集。" with Dissolve(0.3)
    scene date_event_1_may_99 with Dissolve(0.3)
    gg 2 "而你刚才还说看同一个东西看几遍会腻。" with Dissolve(0.3)
    scene date_event_1_may_100 with Dissolve(0.3)
    may 17 "这不一样！" with Dissolve(0.3)
    scene date_event_1_may_101 with Dissolve(0.3)
    gg 2 "怎么就不一样了？" with Dissolve(0.3)
    scene date_event_1_may_102 with Dissolve(0.3)
    gg 2 "谁能拍两百八十个小时的东西啊！？" with Dissolve(0.3)
    scene date_event_1_may_103 with Dissolve(0.3)
    may 17 "[gg]，我又没让你看完整个系列。就看几集嘛。" with Dissolve(0.3)
    scene date_event_1_may_104 with Dissolve(0.3)
    gg 2 "那也太长了……" with Dissolve(0.3)
    scene date_event_1_may_105 with Dissolve(0.3)
    may 17 "你想看恐怖片的时候，我会找片来陪你看。" with Dissolve(0.3)
    scene date_event_1_may_106 with Dissolve(0.3)
    may 17 "可我想看自己喜欢的东西，你立刻就耍赖了！" with Dissolve(0.3)
    scene date_event_1_may_107 with Dissolve(0.3)
    gg 2 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_may_108 with Dissolve(0.3)
    gg 2 "（好吧，她说得对。）" with Dissolve(0.3)
    scene date_event_1_may_109 with Dissolve(0.3)
    gg 2 "（你为这点小事抱怨太多。 说到底，你搞这个马拉松本来就是为了让她开心。）" with Dissolve(0.3)
    scene date_event_1_may_110 with Dissolve(0.3)
    gg 2 "好吧，[may]，你说得对。看几集吧。" with Dissolve(0.3)
    
    stop music2 fadeout 5
    
    scene black with Dissolve(1.0)
    pause 1
    
    play music3 turkish_waltz fadein 5 volume 0.5
    
    scene date_event_1_may_111 with Dissolve(1.0)
    pause 1
    scene date_event_1_may_112 with Dissolve(0.3)
    gg 2 "（好吧，这比我想象的糟糕多了。）" with Dissolve(0.3)
    scene date_event_1_may_113 with Dissolve(0.3)
    gg 2 "（经典狗血剧以前在我看来纯粹是脑残。但现在看来，真正的威胁一直是土耳其电视剧。）" with Dissolve(0.3)
    scene date_event_1_may_114 with Dissolve(0.3)
    gg 2 "（我能感觉到每看一分钟，脑子里的褶皱都在被抹平。）" with Dissolve(0.3)
    scene date_event_1_may_115 with Dissolve(0.3)
    may 17 "别摆出这么痛苦的表情。" with Dissolve(0.3)
    scene date_event_1_may_116 with Dissolve(0.3)
    gg 2 "这部剧是精神控制武器。" with Dissolve(0.3)
    scene date_event_1_may_117 with Dissolve(0.3)
    may 17 "你看点有人味的东西也好！" with Dissolve(0.3)
    scene date_event_1_may_118 with Dissolve(0.3)
    gg 2 "要是这就是有人味的东西，那我不想做人。" with Dissolve(0.3)
    scene date_event_1_may_119 with Dissolve(0.3)
    may 17 "你又抱怨了。" with Dissolve(0.3)
    scene date_event_1_may_120 with Dissolve(0.3)
    gg 2 "这是我的临终挣扎。" with Dissolve(0.3)
    scene date_event_1_may_121 with Dissolve(1.0)
    gg 2 "（好吧。男人说了要看好几集，就得说话算话。）" with Dissolve(0.3)
    gg 2 "（哪怕比再去一趟异世界还可怕。）"
    scene date_event_1_may_122 with Dissolve(0.3)
    "[may]努力跟着剧情走，可她的目光越来越往他这边飘。" with Dissolve(0.3)
    scene date_event_1_may_123 with Dissolve(0.3)
    gg 2 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_may_124 with Dissolve(0.3)
    may 17 "你真的一点都不感兴趣？" with Dissolve(0.3)
    scene date_event_1_may_125 with Dissolve(0.3)
    gg 2 "不知道为什么，苏丹和无数妃嫔的两百八十小时韵事一点也激不起我。" with Dissolve(0.3)
    scene date_event_1_may_126 with Dissolve(0.3)
    gg 2 "不过也许我看上几集之后，会变成这部剧的忠实粉丝。" with Dissolve(0.3)
    scene date_event_1_may_127 with Dissolve(0.3)
    gg 2 "到那时我就会彻底变成另一个人，你会永远失去你这位老朋友。但现在，不好意思，我没什么兴趣。" with Dissolve(0.3)
    
    play music2 relaxing_lofi_ena__sascha_ende fadein 5
    $ renpy.music.set_volume(0.1, delay=5, channel=u'music3')
    
    scene date_event_1_may_128 with Dissolve(0.3)
    may 17 "也许你只是不懂谈恋爱是什么感觉？" with Dissolve(0.3)
    
    show date_event_1_may_130 with Dissolve(0.2)
    gg 2 "你以为我什么都不知道？" with Dissolve(0.3)
    show date_event_1_may_129 with Dissolve(0.2)
    hide date_event_1_may_130
    may 17 "那你说说你知道什么。" with Dissolve(0.3)
    show date_event_1_may_130 with Dissolve(0.2)
    hide date_event_1_may_129
    gg 2 "我觉得没什么好说的。" with Dissolve(0.3)
    show date_event_1_may_129 with Dissolve(0.2)
    hide date_event_1_may_130
    may 17 "拜托，我想知道！" with Dissolve(0.3)
    show date_event_1_may_130 with Dissolve(0.2)
    hide date_event_1_may_129
    gg 2 "{cps=5}……{/cps}"
    gg 2 "反正跟苏丹宫廷里最有影响力的人坠入爱河完全不是一回事。" with Dissolve(0.3)
    show date_event_1_may_129 with Dissolve(0.2)
    hide date_event_1_may_130
    may 17 "[gg]，我是认真的！" with Dissolve(0.3)
    show date_event_1_may_130 with Dissolve(0.2)
    hide date_event_1_may_129
    gg 2 "好吧好吧……" with Dissolve(0.3)
    gg 2 "这个嘛，我可以说，恋爱就是看着一个人，然后忘了其他所有事。"
    gg 2 "她的每一个动作、每一个微笑，对你来说都变得不一样。"
    gg 2 "大概就像成瘾。"
    show date_event_1_may_129 with Dissolve(0.2)
    hide date_event_1_may_130
    may 17 "是那种不好的瘾吗？" with Dissolve(0.3)
    show date_event_1_may_130 with Dissolve(0.2)
    hide date_event_1_may_129
    gg 2 "看对象是谁，你懂的。" with Dissolve(0.3)
    gg 2 "如果是真爱——你能看见并接纳对方的缺点与怪癖，承受不了失去对方——那就是好的。"
    gg 2 "如果只是对某个人的执念，那就是坏的。"
    gg 2 "（当然还有些没分寸、毒害精子的白痴。但我不想提他们扫了兴。）"
    show date_event_1_may_129 with Dissolve(0.2)
    hide date_event_1_may_130
    may 17 "那你……有过那种感觉吗？" with Dissolve(0.3)
    show date_event_1_may_130 with Dissolve(0.2)
    hide date_event_1_may_129
    gg 2 "哈。也许吧。" with Dissolve(0.3)
    show date_event_1_may_129 with Dissolve(0.2)
    hide date_event_1_may_130
    may 17 "「也许」是什么意思？" with Dissolve(0.3)
    show date_event_1_may_130 with Dissolve(0.2)
    hide date_event_1_may_129
    gg 2 "那你呢，[may]？你有过吗？" with Dissolve(0.3)
    scene date_event_1_may_131 with Dissolve(0.3)
    "她脸颊泛红，却鼓起了勇气没有移开视线。" with Dissolve(0.3)
    scene date_event_1_may_132 with Dissolve(0.3)
    may 17 "我……想……有。" with Dissolve(0.3)
    scene date_event_1_may_133 with Dissolve(0.3)
    "房间里弥漫着紧绷的沉默。" with Dissolve(0.3)
    scene date_event_1_may_134 with Dissolve(0.3)
    may 17 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_may_135 with Dissolve(0.3)
    gg 2 "你这段时间很奇怪。为什么？" with Dissolve(0.3)
    scene date_event_1_may_136 with Dissolve(0.3)
    may 17 "我没有……" with Dissolve(0.3)
    scene date_event_1_may_137 with Dissolve(0.3)
    "她的声音在颤抖。" with Dissolve(0.3)
    scene date_event_1_may_138 with Dissolve(0.3)
    "我的目光落在她的嘴唇上。那上面有犹豫……同时还有别的什么……"
    "一个让我移不开视线的呼唤。它们看起来那么柔软、脆弱，仿佛此刻说出的任何一句话都会改变一切。"
    gg 2 "你想告诉我什么吗？" with Dissolve(0.3)
    scene date_event_1_may_139 with Dissolve(0.3)
    "她的呼吸急促起来，承受不住这份张力，闭上了眼睛。"
    gg 2 "[may]……" with Dissolve(0.3)
    scene date_event_1_may_140 with Dissolve(0.3)
    may 17 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_may_141 with Dissolve(0.3)
    "我的手轻轻碰了碰她的脸颊，用手指拂开她的一缕头发。"
    scene date_event_1_may_142 with Dissolve(0.3)
    gg 2 "好吧，你那部剧没那么差。" with Dissolve(0.3)
    scene date_event_1_may_143 with Dissolve(0.3)
    may 17 "[gg]。" with Dissolve(0.3)
    scene date_event_1_may_144 with Dissolve(0.3)
    gg 2 "嗯？" with Dissolve(0.3)
    scene date_event_1_may_145 with Dissolve(0.3)
    may 17 "你……真的从来没有那样看过我吗？" with Dissolve(0.3)
    scene date_event_1_may_146 with Dissolve(0.3)
    may 17 "那个……以那种方式？" with Dissolve(0.3)
    scene date_event_1_may_147 with Dissolve(0.3)
    gg 2 "（呼……我们终于谈到这个话题了。）" with Dissolve(0.3)
    gg 2 "我先确认一件事。是因为那晚，对吧？"
    scene date_event_1_may_148 with Dissolve(0.3)
    "她紧张地点了点头。"
    scene date_event_1_may_149 with Dissolve(0.3)
    gg 2 "听着，[may]……你对我来说比任何人都重要。" with Dissolve(0.3)
    scene date_event_1_may_150 with Dissolve(0.3)
    may 17 "但你不把我当女孩子看？" with Dissolve(0.3)
    scene date_event_1_may_151 with Dissolve(0.3)
    gg 2 "你希望我把你当女孩子看？" with Dissolve(0.3)
    scene date_event_1_may_152 with Dissolve(0.3)
    may 17 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_may_153 with Dissolve(0.3)
    pause 1
    
    $ renpy.music.set_volume(1, delay=0, channel=u'music3')
    stop music3 fadeout 0.3
    
    scene date_event_1_may_154 with Dissolve(0.3)
    gg 2 "你干嘛关掉电视？" with Dissolve(0.3)
    scene date_event_1_may_155 with Dissolve(0.3)
    may 17 "反正你也没在看。" with Dissolve(0.3)
    scene date_event_1_may_156 with Dissolve(0.3)
    gg 2 "所以？" with Dissolve(0.3)
    scene date_event_1_may_157 with Dissolve(0.3)
    may 17 "那你为什么还在这儿？" with Dissolve(0.3)
    scene date_event_1_may_158 with Dissolve(0.3)
    gg 2 "因为我们约好了要一起度过这段时间。" with Dissolve(0.3)
    scene date_event_1_may_159 with Dissolve(0.3)
    may 17 "……但我感受不到。" with Dissolve(0.3)
    scene date_event_1_may_160 with Dissolve(0.3)
    gg 2 "那你觉得这是什么？" with Dissolve(0.3)
    scene date_event_1_may_161 with Dissolve(0.3)
    may 17 "也许……因为你也想待得更近一点？！" with Dissolve(0.3)
    scene date_event_1_may_162 with Dissolve(0.3)
    gg 2 "[may]……" with Dissolve(0.3)
    scene date_event_1_may_163 with Dissolve(0.3)
    may 17 "我受够了你总是跟我保持距离！" with Dissolve(0.3)
    scene date_event_1_may_164 with Dissolve(0.3)
    gg 2 "你知道自己在说什么吗？" with Dissolve(0.3)
    scene date_event_1_may_165 with Dissolve(0.3)
    may 17 "那你呢？" with Dissolve(0.3)
    
    play music3 sexy_downtempo_erotic_hip_hop_instrumental fadein 10 volume 0.5
    stop music2 fadeout 10
    
    scene date_event_1_may_166 with Dissolve(0.3)
    pause 2
    scene date_event_1_may_167 with Dissolve(0.3)
    may 17 "你这么努力想对我好……却不是你真正想对我好的方式。" with Dissolve(0.3)
    may 17 "我们甚至住在一起……"
    scene date_event_1_may_168 with Dissolve(0.3)
    may 17 "{cps=5}……{/cps}"
    scene date_event_1_may_169 with Dissolve(0.3)
    may 17 "对不起，可为什么别的女生就能允许自己比我做更多？" with Dissolve(0.3)
    scene date_event_1_may_170 with Dissolve(0.3)
    may 17 "这么多年了，你为什么总是只把我当妹妹？" with Dissolve(0.3)
    scene date_event_1_may_171 with Dissolve(0.3)
    may 17 "为什么我不能对你来说是更重要的人？" with Dissolve(0.3)
    scene date_event_1_may_172 with Dissolve(0.3)
    gg 2 "你真的想要这样吗？" with Dissolve(0.3)
    scene date_event_1_may_173 with Dissolve(0.3)
    "我慢慢按压她的大腿，力道暧昧，几乎带着挑逗。"
    scene date_event_1_may_174 with Dissolve(0.3)
    "那不只是一个触碰，而是一个无声的提问：可以吗？你愿意吗？……你打算走到哪一步？"
    scene date_event_1_may_175 with Dissolve(0.3)
    "她的目光从下方抬起——柔软、炽热，仿佛连她自己都不敢相信这是真的。"
    scene date_event_1_may_176 with Dissolve(0.3)
    "嘴唇微微张开。没有声音。只有呼吸——紊乱得仿佛每一秒都有一个世纪那么长。"
    
    play sound kiss_1
    
    scene date_event_1_may_177 with Dissolve(0.3)
    pause 1.5
    scene date_event_1_may_178 with Dissolve(0.3)
    "她靠得更近，仿佛这个吻是她躲避整个世界的港湾。"
    scene date_event_1_may_179 with Dissolve(0.3)
    "我的手指沿她的大腿缓缓上移，抚过每一寸皮肤。"
    "稍稍收紧，我感到她的身体在回应，掌心下泛起鸡皮疙瘩。"
    scene date_event_1_may_180 with Dissolve(0.3)
    "我顺着一个流畅的动作描过她的大腿，停在她柔软温热的臀部。"
    scene date_event_1_may_178 with Dissolve(0.3)
    may 17 "嗯……" with Dissolve(0.3)
    scene date_event_1_may_181 with Dissolve(0.3)
    "她猛地倒吸一口气，仿佛有火花迸射。而我体内某处收紧。紧张，甜蜜而煎熬。我几乎无法呼吸。"
    scene date_event_1_may_182 with Dissolve(0.3)
    may 17 "等等……" with Dissolve(0.3)
    scene date_event_1_may_183 with Dissolve(0.3)
    may 17 "我看得出现在你是什么眼神……你已经想要了。" with Dissolve(0.3)
    scene date_event_1_may_184 with Dissolve(0.3)
    gg 2 "你也一样。别装了。" with Dissolve(0.3)
    scene date_event_1_may_185 with Dissolve(0.3)
    may 17 "我、我……我没装。只是……" with Dissolve(0.3)
    scene date_event_1_may_186 with Dissolve(0.3)
    gg 2 "嘘……如果觉得不舒服，告诉我。好吗？" with Dissolve(0.3)
    scene date_event_1_may_187 with Dissolve(0.3)
    may 17 "{cps=5}………{/cps}" with Dissolve(0.3)
    scene date_event_1_may_188 with Dissolve(0.3)
    "她一句话也没说。只是靠得更近，双臂环住我的脖子，头靠在我肩上。"
    scene date_event_1_may_189 with Dissolve(0.3)
    "无声。只有与我同步的呼吸。"
    scene date_event_1_may_190 with Dissolve(0.3)
    "我的手指缓缓描过她的背，像是在解读她、记住她，每一寸、每一道曲线。"
    scene date_event_1_may_191 with Dissolve(0.3)
    ''
    scene date_event_1_may_192 with Dissolve(0.3)
    "我往后靠，把她一起带了下去……"
    scene date_event_1_may_193 with Dissolve(0.3)
    pause 1
    scene date_event_1_may_194 with Dissolve(0.3)
    "让她躺在身侧，我俯身压上去，用一只手臂支撑着身体……"
    scene date_event_1_may_195 with Dissolve(0.3)
    "另一只手描过她的脸颊，在嘴角边停住。"
    "她没有移开视线，也没有试图后退。她眼里有同意，有信任，还有某种极深的亲密。"
    scene date_event_1_may_196 with Dissolve(0.3)
    "我再次吻她。更深，更贪婪，带着再也藏不住的爱。"
    scene date_event_1_may_197 with Dissolve(0.3)
    may 17 "你一直在等这一刻吗？" with Dissolve(0.3)
    scene date_event_1_may_198 with Dissolve(0.3)
    gg 2 "或许吧。" with Dissolve(0.3)
    scene date_event_1_may_199 with Dissolve(0.3)
    "我掀起她的连帽衫，露出她的皮肤——温热、柔软，如此真实。"
    scene date_event_1_may_200 with Dissolve(0.3)
    "我的手指隔着单薄的胸罩描过她胸部的轮廓。"
    scene date_event_1_may_201 with Dissolve(0.3)
    "她紧紧闭上眼，咬住嘴唇。"
    scene date_event_1_may_202 with Dissolve(0.3)
    "我慢慢掀起那层布料……"
    scene date_event_1_may_203 with Dissolve(0.3)
    "而就在同一瞬间，她用手挡住了自己的胸口。"
    scene date_event_1_may_204 with Dissolve(0.3)
    may 17 "[gg]……" with Dissolve(0.3)
    scene date_event_1_may_205 with Dissolve(0.3)
    gg 2 "怎么了，[may]？" with Dissolve(0.3)
    scene date_event_1_may_206 with Dissolve(0.3)
    "没听到回答，我把手掌放低到她小腹。"
    scene date_event_1_may_207 with Dissolve(0.3)
    "绕着她的肚脐画圈，然后滑向她的短裤。"
    scene date_event_1_may_208 with Dissolve(0.3)
    "我缓慢而小心地触碰她最脆弱的地方。但就在我试着再往下一寸时——"
    scene date_event_1_may_209 with Dissolve(0.3)
    may 17 "等、等一下！……等等……不要那里……" with Dissolve(0.3)
    scene date_event_1_may_210 with Dissolve(0.3)
    may 17 "今天能到此为止吗？" with Dissolve(0.3)
    scene date_event_1_may_211 with Dissolve(0.3)
    "我立刻退开。点了点头，就这样抱着她，没有再进一步。"
    scene date_event_1_may_212 with Dissolve(0.3)
    gg 2 "你真会挑在最有意思的时候叫停。" with Dissolve(0.3)
    scene date_event_1_may_213 with Dissolve(0.3)
    may 17 "我、我只是……现在心脏受不了……" with Dissolve(0.3)
    scene date_event_1_may_214 with Dissolve(0.3)
    may 17 "对不起……" with Dissolve(0.3)
    scene date_event_1_may_215 with Dissolve(0.3)
    gg 2 "没关系，别在意。" with Dissolve(0.3)
    
    show screen rel_up_may
    $ love_may += 6
    
    scene date_event_1_may_216 with Dissolve(0.5)
    pause 2.5
    
    $ date_event_1_may = True
    $ date_event_1_day += 1
    
    stop music3 fadeout 5
    
    scene black with Dissolve(1.0)
    pause 2
    pause 2
    
    if date_event_1_day >= 3:
        jump end_tatsumi
        
    else:
        play music4 science_documentary_loop fadein 5
        show date_event_1_intro_18 with Dissolve(1.0)
        jump date_event_1_choice

###### DATE EVENT - MINAMI

label date_event_1_minami:

    scene date_event_1_minami_1 with Dissolve(0.3)
    gg 2 "{cps=5}……{/cps}" with Dissolve(0.3)
    show date_event_1_minami_2:
        xpos 0
        ease 0.5 xpos -400
        
    stop music4 fadeout 3
    play music2 business_education_main_loop_with_piano fadein 1
        
    show date_event_1_minami_3:
        xpos 1900
        ease 0.5 xpos 0
    mi 5 "喂？[gg]？" with Dissolve(0.3)
    scene date_event_1_minami_4 with Dissolve(0.3)
    gg 2 "下午好，[mi]！最近怎么样？" with Dissolve(0.3)
    scene date_event_1_minami_5 with Dissolve(0.3)
    mi 5 "请记住，在正式场合你应该称呼我为栗原老师。" with Dissolve(0.3)
    mi 5 "出什么事了？"
    scene date_event_1_minami_6 with Dissolve(0.3)
    gg 2 "其实也没什么。今天平静得出奇。" with Dissolve(0.3)
    gg 2 "我在想，栗原老师，也许我们可以在更随意的场合见面？"
    scene date_event_1_minami_7 with Dissolve(0.3)
    mi 5 "哇。真没想到。一切还好吗？" with Dissolve(0.3)
    scene date_event_1_minami_8 with Dissolve(0.3)
    gg 2 "完全没问题。我绝对没有被绑架，也没有被引诱进陷阱，如果你想问的是这个。" with Dissolve(0.3)
    scene date_event_1_minami_9 with Dissolve(0.3)
    mi 5 "好吧。那你为什么想见面？" with Dissolve(0.3)
    scene date_event_1_minami_10 with Dissolve(0.3)
    gg 2 "一个男人请美女一起玩乐，真的需要理由吗？" with Dissolve(0.3)
    scene date_event_1_minami_11 with Dissolve(0.3)
    "电话里传来轻轻的笑声。"
    scene date_event_1_minami_12 with Dissolve(0.3)
    mi 5 "哎呀，[gg]，你真会说话！听起来很诱人，不过我今晚恐怕得在学校待到很晚。" with Dissolve(0.3)
    scene date_event_1_minami_13 with Dissolve(0.3)
    gg 2 "什么？周末也要工作吗？" with Dissolve(0.3)
    mi 5 "不是一直这样，不过有时候会。我想我能挤出几个小时，但那就不算正式见面了。" with Dissolve(0.3)
    scene date_event_1_minami_14 with Dissolve(0.3)
    mi 5 "不过，如果你想证明自己是个负责任的学生，可以来学校帮我个忙。" with Dissolve(0.3)
    gg 2 "这么快就想让我干活了，栗原老师？" with Dissolve(0.3)
    scene date_event_1_minami_15 with Dissolve(0.3)
    mi 5 "哎呀，[gg]，我可不敢让你靠近那个。" with Dissolve(0.3)
    scene date_event_1_minami_16 with Dissolve(0.3)
    mi 5 "我听说你体育挺不错。所以你可以帮我做点……有运动量的事情。" with Dissolve(0.3)
    scene date_event_1_minami_17 with Dissolve(0.3)
    gg 2 "（哇。她刚才是故意停顿的吧？）" with Dissolve(0.3)
    scene date_event_1_minami_18 with Dissolve(0.3)
    gg 2 "好啊，我很乐意帮忙！" with Dissolve(0.3)
    scene date_event_1_minami_19 with Dissolve(0.3)
    mi 5 "太好了。带上运动服！体育馆见……一小时后？" with Dissolve(0.3)
    scene date_event_1_minami_20 with Dissolve(0.3)
    gg 2 "我大概四十分钟后到。" with Dissolve(0.3)
    scene date_event_1_minami_21 with Dissolve(0.3)
    gg 2 "（可恶，她大概是在挑逗我，但用那种语气，没哪个男人扛得住。）" with Dissolve(0.3)
    
    stop music2 fadeout 3
    play music city_bird fadein 3
    
    scene black with Dissolve(1.0)
    pause 1
    
    scene date_event_1_minami_22 with Dissolve(1.3)
    "收拾好东西、沿着熟悉的路出发，没花多少时间。"
    gg 23 "（哇。学校这么空真是奇怪。虽然不是异世界，但还是……很怪。）" with Dissolve(0.3)
    gg 23 "（总之这儿没什么威胁我。没有学生，剩下的老师也在离开。）"
    
    stop music fadeout 2
    play music2 discovering_daily_loop_1 fadein 3
    
    scene date_event_1_minami_23 with Dissolve(1.0)
    pause 1
    scene date_event_1_minami_24 with Dissolve(0.3)
    gg 23 "哟，[ken]，没想到在这儿碰见你。" with Dissolve(0.3)
    scene date_event_1_minami_25 with Dissolve(0.3)
    ken 5 "嗨，[gg]。周末也在训练？" with Dissolve(0.3)
    scene date_event_1_minami_26 with Dissolve(0.3)
    pause 1
    scene date_event_1_minami_27 with Dissolve(0.3)
    gg 23 "不完全是。你在这儿也能练？" with Dissolve(0.3)
    
    show date_event_1_minami_29 with Dissolve(0.3)
    ken 5 "结果发现还真可以。只要跟体育老师安排一下，他可能会让你周末进体育馆。" with Dissolve(0.3)
    ken 5 "这儿有些器械，而且免费！比随便报个健身房强多了。"
    show date_event_1_minami_28 with Dissolve(0.3)
    hide date_event_1_minami_29
    gg 23 "哈，没想到你是健身房的类型。" with Dissolve(0.3)
    gg 23 "我猜大部分同学周末不是泡在电脑前就是在酒吧晃荡。"
    show date_event_1_minami_29 with Dissolve(0.3)
    hide date_event_1_minami_28
    ken 5 "其实这是我第一次来。这几天发生的事让我想了很多。" with Dissolve(0.3)
    ken 5 "还有你揍[da]那一下——真的超爽！"
    ken 5 "而且你把那混蛋放倒得那么轻松！"
    show date_event_1_minami_30 with Dissolve(0.3)
    hide date_event_1_minami_29
    ken 5 "不过……就像我说的，现在他可能在哪里埋伏我，我就没那么走运了。" with Dissolve(0.3)
    show date_event_1_minami_28 with Dissolve(0.3)
    hide date_event_1_minami_30
    gg 23 "所以你才决定变强？" with Dissolve(0.3)
    show date_event_1_minami_29 with Dissolve(0.3)
    hide date_event_1_minami_28
    ken 5 "对，今天我做了俯卧撑、深蹲，还打了沙袋！" with Dissolve(0.3)
    show date_event_1_minami_28 with Dissolve(0.3)
    hide date_event_1_minami_29
    gg 23 "更厉害了啊，干得好。" with Dissolve(0.3)
    show date_event_1_minami_31 with Dissolve(0.3)
    hide date_event_1_minami_28
    ken 5 "已经开始有效果了？" with Dissolve(0.3)
    gg 23 "……嗯，好像开始有点肌肉了。" with Dissolve(0.3)
    gg 23 "（拜托把衣服穿上。）"
    show date_event_1_minami_29 with Dissolve(0.3)
    hide date_event_1_minami_31
    ken 5 "你也这么觉得？再多一点我就能跟[da]平分秋色了！" with Dissolve(0.3)
    show date_event_1_minami_28 with Dissolve(0.3)
    hide date_event_1_minami_29
    gg 23 "其实我得提醒你一点。" with Dissolve(0.3)
    gg 23 "第一，别到处找架打。自卫是一回事，找事是另一回事。"
    gg 23 "最糟的结果，你可能变成[da]那样。我更喜欢现在你面前的这个[ken]。"
    show date_event_1_minami_30 with Dissolve(0.3)
    hide date_event_1_minami_28
    ken 5 "哦。你说得对。抱歉。" with Dissolve(0.3)
    
    scene date_event_1_minami_35 with Dissolve(0.3)
    pause 1
    
    show date_event_1_minami_32 with Dissolve(0.3)
    gg 23 "不用道歉。另外还有第二点。" with Dissolve(0.3)
    gg 23 "一旦开始就别放弃。第一次练完你会觉得很爽，但关键在于坚持。"
    gg 23 "别指望立刻见效。练几次之后你可能会想放弃，那是在锻炼你的意志力，不是身体。"
    gg 23 "而且你必须硬撑过去，如果你真的想变强。"
    show date_event_1_minami_33 with Dissolve(0.3)
    hide date_event_1_minami_32
    ken 6 "……哇，这番激励真够受的！太感谢了！现在我更想变得像你了。" with Dissolve(0.3)
    show date_event_1_minami_32 with Dissolve(0.3)
    hide date_event_1_minami_33
    gg 23 "不客气。你真想像我？" with Dissolve(0.3)
    show date_event_1_minami_34 with Dissolve(0.3)
    hide date_event_1_minami_32
    ken 6 "那个……当然。你照过镜子吗？你在女生里很受欢迎，能打，而且身材好。" with Dissolve(0.3)
    show date_event_1_minami_32 with Dissolve(0.3)
    hide date_event_1_minami_34
    gg 23 "（嗯。听到这话有点尴尬，尤其是我并不觉得自己有多拼。）" with Dissolve(0.3)
    gg 23 "（但我得支持他，可恶。）"
    gg 23 "该怎么说呢……我不是天生的，花了好些年才走到今天。"
    gg 23 "但不是不可能。继续练吧——不过记住，那不是为了女孩，也不是为了打恶霸。"
    gg 23 "是为了你自己。"
    
    scene date_event_1_minami_36 with Dissolve(0.3)
    ken 6 "明白了。谢谢老师。" with Dissolve(0.3)
    scene date_event_1_minami_37 with Dissolve(0.3)
    gg 23 "别这样。训练加油。" with Dissolve(0.3)
    scene date_event_1_minami_38 with Dissolve(0.3)
    ken 6 "谢谢，我要走了。你也加油！" with Dissolve(0.3)

    stop music2 fadeout 5
    
    scene black with Dissolve(1.0)
    pause 1
    
    play music3 business_education_main_loop fadein 3
    
    pause 1
    
    scene date_event_1_minami_39 with Dissolve(1.0)
    pause 1
    scene date_event_1_minami_40 with Dissolve(0.3)
    gg 24 "（嗯。这个时间居然没有社团在用体育馆，挺奇怪的。）" with Dissolve(0.3)
    gg 24 "（我们学校明明有篮球、足球，看那个球网——还有排球。）"
    gg 24 "（大概是学校资源充足到每人都有自己的场地吧。）"
    scene date_event_1_minami_41 with Dissolve(0.3)
    gg 24 "[mi]！你也在这儿！？" with Dissolve(0.3)
    
    scene date_event_1_minami_42 with Dissolve(0.3)
    mi 8 "我就在这儿，年轻人，不用喊。" with Dissolve(0.3)
    scene date_event_1_minami_43 with Dissolve(0.3)
    mi 8 "而且在学校里我还是栗原老师！" with Dissolve(0.3)
    
    show date_event_1_minami_44 with Dissolve(0.3)
    $ renpy.pause (17.3, hard=True)
    
    show date_event_1_minami_45 with Dissolve(0.3)
    gg 24 "（哇。为了这一幕专程来都值了。）" with Dissolve(0.3)
    scene date_event_1_minami_46 with Dissolve(0.3)
    gg 24 "拜托，这儿就我们两个！我至少可以叫你美波老师吧？" with Dissolve(0.3)
    scene date_event_1_minami_47 with Dissolve(0.3)
    mi 8 "我想我早就没能跟你保持proper的师生界限了。" with Dissolve(0.3)
    scene date_event_1_minami_48 with Dissolve(0.3)
    mi 8 "行吧，那就美波老师。但只有我们两个的时候。" with Dissolve(0.3)
    scene date_event_1_minami_49 with Dissolve(0.3)
    gg 24 "不proper的界限万岁！" with Dissolve(0.3)
    
    show date_event_1_minami_50 with Dissolve(0.3)
    gg 24 "那么，你叫我来到底是为了什么？" with Dissolve(0.3)
    show date_event_1_minami_51 with Dissolve(0.3)
    hide date_event_1_minami_50
    mi 8 "当然是运动啊。你还能指望什么？" with Dissolve(0.3)
    show date_event_1_minami_50 with Dissolve(0.3)
    hide date_event_1_minami_51
    gg 24 "（我本来还……想了一些更不现实的事情。）" with Dissolve(0.3)
    show date_event_1_minami_51 with Dissolve(0.3)
    hide date_event_1_minami_50
    mi 8 "我不会让你搬器械之类的事。那样就成了童工。" with Dissolve(0.3)
    mi 8 "所以我的提议是，我们做点运动。你陪我。"
    show date_event_1_minami_50 with Dissolve(0.3)
    hide date_event_1_minami_51
    gg 24 "哦，那这样就不算童工了？" with Dissolve(0.3)
    show date_event_1_minami_51 with Dissolve(0.3)
    hide date_event_1_minami_50
    mi 8 "你随时可以走开。这不会影响你的成绩——这不是正式课程。" with Dissolve(0.3)
    mi 8 "其实严格来说，我现在根本不该跟学生待在一起……"
    show date_event_1_minami_50 with Dissolve(0.3)
    hide date_event_1_minami_51
    gg 24 "你的秘密我会保密。那么，我们做什么运动？" with Dissolve(0.3)
    show date_event_1_minami_51 with Dissolve(0.3)
    hide date_event_1_minami_50
    mi 8 "排球。" with Dissolve(0.3)
    show date_event_1_minami_50 with Dissolve(0.3)
    hide date_event_1_minami_51
    gg 24 "这个我能应付。你只是需要个伴一起玩？" with Dissolve(0.3)
    show date_event_1_minami_51 with Dissolve(0.3)
    hide date_event_1_minami_50
    mi 8 "我以前还挺擅长的，但现在……唉，显然没时间了。" with Dissolve(0.3)
    mi 8 "我当然可以自己练球，但那太无聊。"
    show date_event_1_minami_50 with Dissolve(0.3)
    hide date_event_1_minami_51
    gg 24 "有道理。看来你一直在保持体能，美波老师。" with Dissolve(0.3)
    show date_event_1_minami_51 with Dissolve(0.3)
    hide date_event_1_minami_50
    mi 8 "……谢谢你，[gg]。" with Dissolve(0.3)
    mi 8 "说实话，只是习惯而已。锻炼的时间够长，身体自己就会渴求它。"
    show date_event_1_minami_50 with Dissolve(0.3)
    hide date_event_1_minami_51
    gg 24 "像戒断反应一样啊……是啊，我懂那种感觉。" with Dissolve(0.3)
    gg 24 "（不过最近，我倒是从另一种「运动」里得到了不少……）"
    
    scene date_event_1_minami_52 with Dissolve(1.0)
    pause 1
    scene date_event_1_minami_53 with Dissolve(0.5)
    "[mi]从器械筐里拿出一个排球，在地上拍了两下。它在木地板上几乎不弹起来。" with Dissolve(0.3)
    scene date_event_1_minami_54 with Dissolve(0.5)
    "她又翻找了一阵，直到找到一个手感合适的。" with Dissolve(0.3)
    scene date_event_1_minami_55 with Dissolve(0.3)
    mi 8 "这些球他们会充气吗……？" with Dissolve(0.3)
    scene date_event_1_minami_56 with Dissolve(0.3)
    mi 8 "啊，这个应该可以。" with Dissolve(0.3)
    scene date_event_1_minami_57 with Dissolve(0.3)
    "确认球的硬度够用后，她眼里闪着光看向我。"
    scene date_event_1_minami_58 with Dissolve(0.3)
    mi 8 "要热身吗，还是直接开始？" with Dissolve(0.3)
    scene date_event_1_minami_59 with Dissolve(0.3)
    gg 24 "我们边打边热身吧。" with Dissolve(0.3)
    scene date_event_1_minami_60 with Dissolve(0.3)
    mi 8 "随你……" with Dissolve(0.3)
    scene date_event_1_minami_61 with Dissolve(0.3)
    pause 1
    show date_event_1_minami_61_1:
        xpos 0
        ease 0.5 xpos -870
        
    play sound woosh1 volume 0.5
        
    show date_event_1_minami_62:
        xpos 1500
        ease 0.5 xpos 0
    pause 1
    
    play sound2 woosh2 volume 0.5
    
    show date_event_1_minami_63:
        xpos 1000
        ease 0.5 xpos 0
    pause 0.5
    "[mi]把球抛起，轻巧地跳了起来。"
    gg 24 "（跳发？认真的吗？）" with Dissolve(0.3)
    
    show date_event_1_minami_64 with Dissolve(0.3)
    $ renpy.pause (5.5, hard=True)
    
    play sound volleyball_hit_echo_2
    
    $ renpy.pause (1.5, hard=True)
    
    scene date_event_1_minami_64_1 with Dissolve(0.3)
    mi 8 "小心！" with Dissolve(0.3)
    
    play sound2 volleyball_hit_1 volume 1.5
    
    scene date_event_1_minami_65 with hpunch
    pause 1
    scene date_event_1_minami_66 with Dissolve(0.3)
    mi 8 "我的天，[gg]，太对不起！可能我打得有点重。" with Dissolve(0.3)
    scene date_event_1_minami_67 with Dissolve(0.3)
    gg 24 "哇……好准。我完全没跟上球。" with Dissolve(0.3)
    scene date_event_1_minami_68 with Dissolve(0.3)
    gg 24 "（因为我的注意力粘在另外两样东西上了。）" with Dissolve(0.3)
    scene date_event_1_minami_69 with Dissolve(0.3)
    mi 8 "请更小心一点。就算这不是正式课程，我也得对你的安全负责。" with Dissolve(0.3)
    scene date_event_1_minami_70 with Dissolve(0.3)
    gg 24 "果然。你比起学生更怕被起诉。" with Dissolve(0.3)
    scene date_event_1_minami_71 with Dissolve(0.3)
    mi 8 "你知道不是这样。" with Dissolve(0.3)
    scene date_event_1_minami_72 with Dissolve(0.3)
    mi 8 "不过嘛，学生这么多、性格又各异，要真心关心每一个确实不容易。" with Dissolve(0.3)
    
    play sound volleyball_catch_1
    
    scene date_event_1_minami_73 with Dissolve(0.3)
    gg 24 "好吧。比分一比零，你发球。" with Dissolve(0.3)
    
    scene date_event_1_minami_74 with Dissolve(1.0)
    gg 24 "我懂你对学生的态度。有几个真的欠收拾。当然，纯粹出于教育目的。" with Dissolve(0.3)
    mi 8 "体罚不是答案。至少在高中不是。" with Dissolve(0.3)
    
    play sound2 volleyball_hit_echo_1
    
    scene date_event_1_minami_75 with Dissolve(0.3)
    pause 1
    
    play sound3 woosh1
    
    show date_event_1_minami_75_1:
        xpos 0
        ease 0.5 xpos -620
    show date_event_1_minami_76:
        xpos 1400
        ease 0.5 xpos 0
    mi 8 "现代教育工作者认为，如果非要用体罚来惩罚学生，那只能说明老师本人有问题。" with Dissolve(0.3)
    
    play sound volleyball_hit_echo_2
    
    scene date_event_1_minami_77 with Dissolve(0.3)
    pause 1
    show date_event_1_minami_77_1:
        xpos 0
        ease 0.5 xpos -800
        
    play sound2 woosh2
        
    show date_event_1_minami_78:
        xpos 1400
        ease 0.5 xpos 0
    gg 24 "但几百年来，体罚一直是常规手段。而且很多成年人都回想起它觉得挺管用。" with Dissolve(0.3)
    
    play sound3 volleyball_hit_echo_1
    
    scene date_event_1_minami_79 with hpunch
    pause 1
    
    play sound4 volleyball_hit_echo_2 volume 2
    
    scene date_event_1_minami_80 with vpunch
    gg 24 "（好吧，好歹这次没打到我脑袋。）" with Dissolve(0.3)
    scene date_event_1_minami_81 with Dissolve(0.3)
    mi 8 "凡事都要有度。有些不称职的老师太容易越线，直接开始霸凌学生。" with Dissolve(0.3)
    scene date_event_1_minami_82 with Dissolve(0.3)
    gg 24 "看来我得再集中注意力一点。" with Dissolve(0.3)
    scene date_event_1_minami_83 with Dissolve(0.3)
    mi 8 "我们已经打得挺好了。别想太多。" with Dissolve(0.3)
    
    play sound5 volleyball_catch_2
    
    scene date_event_1_minami_84 with Dissolve(0.3)
    gg 24 "哈！对我来说这还只是热身。" with Dissolve(0.3)
    scene date_event_1_minami_85 with Dissolve(0.3)
    gg 24 "我觉得不称职的老师永远会找到霸凌学生的方法。就算不是身体上的，也是精神上的。而依我看，后者更糟。" with Dissolve(0.3)
    scene date_event_1_minami_86 with Dissolve(0.3)
    pause 1
    
    play sound woosh1
    
    show date_event_1_minami_86_1:
        xpos 0
        ease 0.5 xpos -650
        
    play sound2 volleyball_hit_echo_2
        
    show date_event_1_minami_87:
        xpos 1400
        ease 0.5 xpos 0
    mi 8 "这才是真正的问题。不管规则怎么定，都没法除掉坏人。" with Dissolve(0.3)
    
    play sound3 volleyball_hit_1 volume 3
    
    scene date_event_1_minami_88 with vpunch
    mi 8 "我们能做的最好的事，就是把我们够得着的人培养好——别让他们自己也变成坏人。" with Dissolve(0.3)
    
    play sound4 woosh1
    
    show date_event_1_minami_88_1:
        xpos 0
        ease 0.5 xpos -600
    show date_event_1_minami_89:
        xpos 1400
        ease 0.5 xpos 0
    gg 24 "你不觉得有些人已经无可救药了吗？比如[da]。"
    
    play sound volleyball_hit_echo_2
    
    scene date_event_1_minami_90 with Dissolve(0.3)
    mi 8 "你错了，[gg]。人任何年纪都能改变。" with Dissolve(0.3)

    play sound2 woosh2
    
    show date_event_1_minami_90_1:
        xpos 0
        ease 0.5 xpos -540
    show date_event_1_minami_91:
        xpos 1400
        ease 0.5 xpos 0
    mi 8 "但年纪越大越难，这一点确实是真的。所以社会有充分理由尽可能把年轻人教好。"
    
    play sound volleyball_hit_echo_1
    
    scene date_event_1_minami_92 with Dissolve(0.3)
    pause 1.5

    play sound2 woosh1
    
    show date_event_1_minami_92_1:
        xpos 0
        ease 0.5 xpos -940
    show date_event_1_minami_93:
        xpos 1400
        ease 0.5 xpos 0
    gg 24 "「尽可能好」是谁说了算？按别人的标准？归根结底教育是国家定义的，不是吗？所以——按国家标准？" with Dissolve(0.3)
    
    play sound volleyball_hit_echo_2
    
    scene date_event_1_minami_94 with Dissolve(0.3)
    mi 8 "谈政治很少会有好结果。" with Dissolve(0.3)
    
    play sound2 woosh1
    
    show date_event_1_minami_94_1:
        xpos 0
        ease 0.5 xpos -400
    show date_event_1_minami_95:
        xpos 1400
        ease 0.5 xpos 0
    mi 8 "当然有官方课程。但老师仍有机会往里面加一点自己的东西。"
    
    play sound volleyball_catch_2
    
    scene date_event_1_minami_96 with Dissolve(0.3)
    gg 24 "是吗？" with Dissolve(0.3)
    scene date_event_1_minami_97 with Dissolve(0.3)
    gg 24 "你不觉得这有点傲慢吗——超出自己的科目，去推销那些可能只有你自己认为「正确」的东西？" with Dissolve(0.3)
    
    play sound2 volleyball_hit_echo_2 volume 2
    play sound3 volleyball_hit_echo_1
    
    scene date_event_1_minami_98 with vpunch
    pause 1.3
    
    stop music3 fadeout 8
    
    scene date_event_1_minami_99 with Dissolve(0.3)
    mi 9 "这球打得不错。网球单打会更有意思，但这样也够有挑战了。" with Dissolve(0.3)
    
    play music2 main_file_reforme_sound fadein 10
    
    scene date_event_1_minami_100 with Dissolve(0.3)
    mi 9 "至于你说的……每个老师都会经历这些。" with Dissolve(0.3)
    scene date_event_1_minami_101 with Dissolve(0.3)
    mi 9 "有些人最后放弃，只是照本宣科地讲课。有些人跟学生斗到底——然后变成被讨厌的老师。" with Dissolve(0.3)
    scene date_event_1_minami_102 with Dissolve(0.3)
    mi 9 "还有些人……放下自己的骄傲，单纯地，跟学生像人一样说话。" with Dissolve(0.3)
    scene date_event_1_minami_103 with Dissolve(0.3)
    mi 9 "在我看来，最后一种是最好的方式。但也是最难走的。" with Dissolve(0.3)
    scene date_event_1_minami_104 with Dissolve(0.3)
    gg 25 "看来你做得挺不错。" with Dissolve(0.3)
    
    show date_event_1_minami_105 with Dissolve(0.3)
    mi 9 "谢谢你的好话。不过只凭我跟你说话的方式来评价我并不太公平。毕竟你是……特殊个案。" with Dissolve(0.3)
    show date_event_1_minami_106 with Dissolve(0.3)
    hide date_event_1_minami_105
    gg 25 "很高兴知道我在你心里不只是个学生。" with Dissolve(0.3)
    show date_event_1_minami_105 with Dissolve(0.3)
    hide date_event_1_minami_106
    mi 9 "咳……是的，我确实觉得我们能建立联系很幸运。都不敢想如果信徒的力量落到某个不良少年手里会怎样。" with Dissolve(0.3)
    show date_event_1_minami_106 with Dissolve(0.3)
    hide date_event_1_minami_105
    gg 25 "对，我记得你的忠告。除非万不得已，我不会使用能力。" with Dissolve(0.3)
    gg 25 "不过……测试一下我能不能一个人对抗整支队伍，好像还挺有意思。"
    show date_event_1_minami_105 with Dissolve(0.3)
    hide date_event_1_minami_106
    mi 9 "我怀疑不行。如果你的能力真像你描述的那样，你没法长时间维持「时间减速」，也做不到快速进出。" with Dissolve(0.3)
    mi 9 "不经过长时间训练绝对做不到。这不是什么电子游戏里的技能。"
    show date_event_1_minami_106 with Dissolve(0.3)
    hide date_event_1_minami_105
    gg 25 "你这话倒让我好奇了——要是我开始练会怎样？" with Dissolve(0.3)
    show date_event_1_minami_105 with Dissolve(0.3)
    hide date_event_1_minami_106
    mi 9 "我承认，作为科学家我也很感兴趣。但现在，多用一次那种能力都是巨大的风险。" with Dissolve(0.3)
    show date_event_1_minami_106 with Dissolve(0.3)
    hide date_event_1_minami_105
    gg 25 "你说话的方式就好像真有人能追踪到它们。" with Dissolve(0.3)
    show date_event_1_minami_105 with Dissolve(0.3)
    hide date_event_1_minami_106
    mi 9 "问题就在这儿——我不敢肯定。而那种不确定……才是最可怕的。" with Dissolve(0.3)
    show date_event_1_minami_106 with Dissolve(0.3)
    hide date_event_1_minami_105
    gg 25 "好吧，乱七八糟的事我也经历过不少了。" with Dissolve(0.3)
    show date_event_1_minami_105 with Dissolve(0.3)
    hide date_event_1_minami_106
    mi 9 "[gg]……请别让自己陷入危险。我是真的担心你。" with Dissolve(0.3)
    show date_event_1_minami_106 with Dissolve(0.3)
    hide date_event_1_minami_105
    gg 25 "好的，[mi]。" with Dissolve(0.3)
    gg 25 "对了……球呢？"
    
    scene date_event_1_minami_107 with Dissolve(0.3)
    mi 9 "好像滚到哪儿去了。你没看见吗？" with Dissolve(0.3)
    scene date_event_1_minami_108 with Dissolve(0.3)
    gg 25 "（球不见踪影。但左边有一扇储物间的门开着——肯定滚进去了。）" with Dissolve(0.3)
    gg 25 "（这儿看不清里面，灯是关的。）"
    scene date_event_1_minami_109 with Dissolve(0.3)
    gg 25 "嗯。看来我得去储物间看看。" with Dissolve(0.3)
    
    stop music2 fadeout 10
    play music3 interesting_undercurrent_loop_1 fadein 10 volume 0.8
    
    scene date_event_1_minami_110 with Dissolve(0.5)
    "里面安静又半暗，天花板附近的小窗透进一丝微光。" with Dissolve(0.3)
    scene date_event_1_minami_111 with Dissolve(0.3)
    "球不见踪影——肯定跟其他的混在一起，或者滚到架子后面了。" with Dissolve(0.3)
    scene date_event_1_minami_112 with Dissolve(0.3)
    "我开始翻[mi]刚才也检查过的那堆球。一切都指向我们那个倔强的逃犯藏在更里面。" with Dissolve(0.3)
    scene date_event_1_minami_113 with Dissolve(0.3)
    gg 25 "（早知道把手机带来了……）" with Dissolve(0.3)
    mi 9 "[gg]？没事吧？" with Dissolve(0.3)
    scene date_event_1_minami_114 with Dissolve(0.3)
    "[mi]出现在门口。体育馆的光从她身后照过来，我这才注意到她的衣服被汗水浸得有点透了。" with Dissolve(0.3)
    scene date_event_1_minami_115 with Dissolve(0.3)
    gg 25 "呃……没事，就是找不到我们那个球。" with Dissolve(0.3)
    scene date_event_1_minami_116 with Dissolve(0.3)
    mi 9 "我帮你找。其他的看起来不太一样，应该不难找。" with Dissolve(0.3)
    scene date_event_1_minami_117 with Dissolve(0.3)
    gg 25 "要不直接从这辆推车上拿一个？" with Dissolve(0.3)
    scene date_event_1_minami_118 with Dissolve(0.3)
    mi 9 "器械是体育老师负责的。我不想给他惹麻烦。" with Dissolve(0.3)
    scene date_event_1_minami_119 with Dissolve(0.3)
    gg 25 "球没充气明明是他的责任！这怎么会怪到他头上？" with Dissolve(0.3)
    scene date_event_1_minami_120 with Dissolve(0.3)
    mi 9 "[gg]，我们弄丢的球，我们就得找回来！" with Dissolve(0.3)
    scene date_event_1_minami_121 with Dissolve(0.3)
    mi 9 "而且别对体育老师这么凶——我敢肯定他只是太忙了。关键时候他还是很负责、很细心的，而且……" with Dissolve(0.3)
    
    play sound sliding_door_close
    stop music3 fadeout 10
    
    scene date_event_1_minami_122 with Dissolve(0.3)
    pause 2
    
    play sound2 locking_unlocking_door_1
    
    scene date_event_1_minami_123 with Dissolve(0.3)
    gg 25 "什……" with Dissolve(0.3)
    gg 25 "（那肯定是体育老师……）"
    
    play music2 funny_quirky_loop fadein 3
    
    scene date_event_1_minami_124 with Dissolve(0.3)
    kengo 1 "可恶，那个女人迟早要把我害死……" with Dissolve(0.3)
    scene date_event_1_minami_125 with Dissolve(0.3)
    mi 9 "打扰一下！我们还在里面呢！" with Dissolve(0.3)
    scene date_event_1_minami_126 with Dissolve(0.3)
    kengo 1 "是是是，亲爱的，我保证今晚早点回家！" with Dissolve(0.3)
    kengo 1 "不，我不是你妈生日忘了——是学校有急事！"
    scene date_event_1_minami_127 with Dissolve(0.3)
    kengo 1 "宝贝，那些学生没你想的那么可爱，你根本用不着担心！" with Dissolve(0.3)
    scene date_event_1_minami_128 with Dissolve(0.3)
    kengo 1 "你知道在我眼里你是世界上最美的女人！" with Dissolve(0.3)
    
    play sound door_hand_impact_3 volume 3
    
    scene date_event_1_minami_129 with hpunch
    pause 1
    scene date_event_1_minami_128 with Dissolve(0.2)
    pause 0.8
    
    play sound2 door_hand_impact_4 volume 3
    
    scene date_event_1_minami_129 with hpunch
    pause 0.6
    scene date_event_1_minami_128 with Dissolve(0.3)
    pause 0.7
    
    play sound3 door_hand_impact_5 volume 4
    
    scene date_event_1_minami_129 with hpunch
    pause 0.5
    gg 25 "哦，了不起。他耳朵聋了吗？" with Dissolve(0.3)
    scene date_event_1_minami_130 with Dissolve(0.3)
    gg 25 "现在怎么办？" with Dissolve(0.3)
    scene date_event_1_minami_131 with Dissolve(0.3)
    mi 9 "我猜你没带手机吧？" with Dissolve(0.3)
    scene date_event_1_minami_132 with Dissolve(0.3)
    gg 25 "没有，没想到会用到。" with Dissolve(0.3)
    scene date_event_1_minami_133 with Dissolve(0.3)
    mi 9 "而且我已经跟同事说过我到星期一才回来……" with Dissolve(0.3)
    scene date_event_1_minami_134 with Dissolve(0.3)
    mi 9 "也许他发现我们在更衣室的东西会回来找我们？" with Dissolve(0.3)
    scene date_event_1_minami_135 with Dissolve(0.3)
    mi 9 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    stop music2 fadeout 8
    
    scene date_event_1_minami_136 with Dissolve(1.3)
    pause 1.3
    scene date_event_1_minami_137 with Dissolve(0.5)
    "我们等了一阵，可没人来。虽然窗户很小，房间还是越来越热越来越闷。" with Dissolve(0.3)
    scene date_event_1_minami_138 with Dissolve(0.3)
    pause 1
    
    play music3 the_right_spot_main_full fadein 10
    
    scene date_event_1_minami_139 with Dissolve(0.3)
    mi 9 "[gg]，真的很抱歉……但我可以把衬衫脱了吗？" with Dissolve(0.3)
    scene date_event_1_minami_140 with Dissolve(0.3)
    gg 25 "抱歉，什么？" with Dissolve(0.3)
    scene date_event_1_minami_141 with Dissolve(0.3)
    mi 9 "这里面实在太热了，而且我刚打完球还在出汗。我保证凉快一点就马上穿上。" with Dissolve(0.3)
    scene date_event_1_minami_142 with Dissolve(0.3)
    gg 25 "……好吧。" with Dissolve(0.3)
    scene date_event_1_minami_143 with Dissolve(0.3)
    gg 25 "（反正我也不可能拒绝。）" with Dissolve(0.3)
    
    play sound clothes_1
    
    scene date_event_1_minami_144 with Dissolve(0.5)
    pause 1
    scene date_event_1_minami_145 with Dissolve(0.5)
    pause 1
    scene date_event_1_minami_146 with Dissolve(0.3)
    mi 9 "这……实在尴尬。但我相信你足够成熟，能理解这……不合适。" with Dissolve(0.3)
    scene date_event_1_minami_147 with Dissolve(0.3)
    gg 25 "哦，当然。不过我觉得大多数学生现在巴不得处在我这个位置。" with Dissolve(0.3)
    scene date_event_1_minami_148 with Dissolve(0.3)
    mi 10 "那看来我运气不错，摊上的是你。" with Dissolve(0.3)
    scene date_event_1_minami_149 with Dissolve(0.3)
    pause 1
    scene date_event_1_minami_150 with Dissolve(0.3)
    mi 10 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_minami_151 with Dissolve(0.3)
    gg 25 "既然都到这一步了，我其实也越来越热。可以让我也把衬衫脱了吗？" with Dissolve(0.3)
    scene date_event_1_minami_152 with Dissolve(0.3)
    mi 10 "哈哈……要是被人发现我们这样，我可要闯大祸了。" with Dissolve(0.3)
    scene date_event_1_minami_153 with Dissolve(0.3)
    gg 26 "（确实挺热的。）" with Dissolve(0.3)
    scene date_event_1_minami_154 with Dissolve(0.3)
    gg 26 "所以在师生关系上，真的那么严格吗？" with Dissolve(0.3)
    scene date_event_1_minami_155 with Dissolve(0.3)
    mi 10 "当然严格。" with Dissolve(0.3)
    
    $ renpy.music.set_volume(0.5, delay=4, channel=u'music3')
    
    scene date_event_1_minami_156 with Dissolve(0.3)
    mi 10 "基本道德并没有消失——尽管讽刺的是，有些学生在这方面的经验似乎比某些老师丰富得多。" with Dissolve(0.3)
    scene date_event_1_minami_157 with Dissolve(0.3)
    gg 26 "不过，如果反过来——男老师，女学生——社会对老师的谴责会严厉得多。" with Dissolve(0.3)
    scene date_event_1_minami_158 with Dissolve(0.3)
    mi 10 "这并不能让它变得不那么错误。尤其是在这所学校——几年前发生了某起……事件之后，这里管得更严了。" with Dissolve(0.3)
    scene date_event_1_minami_159 with Dissolve(0.3)
    gg 26 "事件？" with Dissolve(0.3)
    scene date_event_1_minami_160 with Dissolve(0.3)
    mi 10 "对。我那时还不在，但老师们偶尔还是会提起。" with Dissolve(0.3)
    scene date_event_1_minami_161 with Dissolve(0.3)
    mi 10 "以前还有一位体育老师——一个相当惹眼的女人。而事实证明，她很懂得利用这一点。" with Dissolve(0.3)
    scene date_event_1_minami_162 with Dissolve(0.3)
    gg 26 "你真会吊胃口，美波老师。" with Dissolve(0.3)
    scene date_event_1_minami_163 with Dissolve(0.3)
    mi 10 "哈哈……总之，有一天他们在这间储物间里当场抓住了她。跟三个高三学生。" with Dissolve(0.3)
    scene date_event_1_minami_164 with Dissolve(0.3)
    gg 26 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_minami_165 with Dissolve(0.3)
    gg 26 "我去。这体育老师可真够呛。" with Dissolve(0.3)
    scene date_event_1_minami_166 with Dissolve(0.3)
    mi 10 "可不是嘛——当时全校都炸了锅。" with Dissolve(0.3)
    mi 10 "那位老师当天就被解雇了，之后学校甚至讨论要成立一个专门的纪律委员会。"
    scene date_event_1_minami_167 with Dissolve(0.3)
    mi 10 "当然最后并没有真的成立。但现在校长动不动就提醒我们，严禁与学生发生任何关系。" with Dissolve(0.3)
    scene date_event_1_minami_168 with Dissolve(0.3)
    gg 26 "我敢肯定，跟她一起被抓的那几个男生事后受到的心理创伤不轻。" with Dissolve(0.3)
    scene date_event_1_minami_169 with Dissolve(0.3)
    mi 10 "我没告诉你，不过听说有几个学生还留着她的电话号码。据说甚至有人到处转发。" with Dissolve(0.3)
    scene date_event_1_minami_170 with Dissolve(0.3)
    mi 10 "但你不会真打算去找吧？" with Dissolve(0.3)
    scene date_event_1_minami_171 with Dissolve(0.3)
    gg 26 "我找那个干嘛？我眼前就站着一个非常惹眼的老师。" with Dissolve(0.3)
    scene date_event_1_minami_172 with Dissolve(0.3)
    mi 10 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=4, channel=u'music3')
    
    scene date_event_1_minami_173 with Dissolve(0.5)
    pause 1
    scene date_event_1_minami_174 with Dissolve(0.5)
    pause 1.5
    scene date_event_1_minami_175 with Dissolve(0.3)
    mi 10 "说起来，这让我想起另一个故事。我还在念师范的时候，有人在一次深夜派对上跟我讲的。" with Dissolve(0.3)
    scene date_event_1_minami_176 with Dissolve(0.3)
    mi 10 "我一个同学上大学前在夏令营打工。她说她当时对某个十五岁男孩……特别感兴趣。" with Dissolve(0.3)
    scene date_event_1_minami_177 with Dissolve(0.3)
    gg 26 "他们是恋人吗？" with Dissolve(0.3)
    scene date_event_1_minami_178 with Dissolve(0.3)
    mi 10 "哦，不是。" with Dissolve(0.3)
    scene date_event_1_minami_179 with Dissolve(0.3)
    mi 10 "她说她觉得他是个甜美天真的男孩，她很想……教他一些有用的东西。" with Dissolve(0.3)
    scene date_event_1_minami_180 with Dissolve(0.3)
    gg 26 "那对她来说不是挺危险的吗？" with Dissolve(0.3)
    scene date_event_1_minami_181 with Dissolve(0.3)
    mi 10 "危险总带着某种刺激感。何况她也不是对谁都那样。" with Dissolve(0.3)
    scene date_event_1_minami_182 with Dissolve(0.3)
    mi 10 "那个男孩是……特殊的一个。" with Dissolve(0.3)
    
    stop music3 fadeout 0.3
    play sound oblom volume 0.4
    
    scene date_event_1_minami_183 with Dissolve(0.1)
    ken 6 "[gg]！你在里面吗？" with Dissolve(0.3)
    
    play music3 the_right_spot_main_full fadein 1
    
    scene date_event_1_minami_184 with Dissolve(0.3)
    gg 26 "[ken]？！在，我在！" with Dissolve(0.3)
    scene date_event_1_minami_185 with Dissolve(0.3)
    ken 6 "呼！谢天谢地找到你了！" with Dissolve(0.3)
    scene date_event_1_minami_186 with Dissolve(0.3)
    mi 10 "他要看见我们了！" with Dissolve(0.3)
    scene date_event_1_minami_187 with Dissolve(0.3)
    gg 26 "嘘！" with Dissolve(0.3)
    scene date_event_1_minami_188 with Dissolve(0.3)
    gg 26 "跟着我就行。" with Dissolve(0.3)
    scene date_event_1_minami_189 with Dissolve(0.3)
    ken 6 "我在校门口碰到体育老师离开，就问了他你在哪儿。" with Dissolve(0.3)
    scene date_event_1_minami_190 with Dissolve(0.3)
    ken 6 "他塞给我一大串钥匙——看起来急得要命！" with Dissolve(0.3)
    show date_event_1_minami_191:
        xpos 0
        ease 0.5 xpos 600
    show date_event_1_minami_192:
        xpos -1000
        ease 0.5 xpos 0
    ken 6 "我试试爬到窗户那儿。"
    scene date_event_1_minami_193 with Dissolve(0.3)
    mi 10 "...?" with Dissolve(0.3)
    scene date_event_1_minami_194 with Dissolve(0.3)
    gg 26 "...!" with Dissolve(0.3)
    scene date_event_1_minami_195 with Dissolve(0.3)
    ken 6 "里面没有别人吧？" with Dissolve(0.3)
    scene date_event_1_minami_196 with Dissolve(0.3)
    gg 26 "没有，就我一个。" with Dissolve(0.3)
    scene date_event_1_minami_197 with Dissolve(0.3)
    gg 25 "我是进来从储物间拿球的，老师不小心把我锁在里面了。" with Dissolve(0.3)
    scene date_event_1_minami_198 with Dissolve(0.3)
    ken 6 "真是场噩梦！幸好我留下来了！" with Dissolve(0.3)
    scene date_event_1_minami_199 with Dissolve(0.3)
    gg 25 "多亏你刚好在附近。不然我得被困到明天早上。" with Dissolve(0.3)
    scene date_event_1_minami_200 with Dissolve(0.3)
    ken 6 "你能把窗户打开吗？我把钥匙扔下去。" with Dissolve(0.3)
    scene date_event_1_minami_201 with Dissolve(0.3)
    ken 6 "给。这几把里应该有一把能开储物间。" with Dissolve(0.3)
    
    play sound keys_drop
    
    scene date_event_1_minami_202 with Dissolve(0.3)
    gg 25 "谢了，[ken]。我出去了。" with Dissolve(0.3)
    scene date_event_1_minami_203 with Dissolve(0.3)
    ken 6 "好。行，我得跑了——回见！" with Dissolve(0.3)
    scene date_event_1_minami_204 with Dissolve(0.3)
    gg 25 "他走了。" with Dissolve(0.3)
    "与此同时，[mi]在检查靠墙的一个箱子。"
    scene date_event_1_minami_205 with Dissolve(0.3)
    mi 10 "啊——球在这儿。" with Dissolve(0.3)
    
    play sound locking_unlocking_door_2
    
    scene date_event_1_minami_206 with Dissolve(0.5)
    pause 1
    
    play sound2 sliding_door_open
    
    scene date_event_1_minami_207 with Dissolve(0.2)
    pause 1
    scene date_event_1_minami_208 with Dissolve(0.3)
    mi 10 "好吧，今天就到这儿。我觉得我们都足够成熟，不会去谈刚才发生的事……" with Dissolve(0.3)
    scene date_event_1_minami_209 with Dissolve(0.3)
    gg 25 "嗯，没问题。" with Dissolve(0.3)
    scene date_event_1_minami_210 with Dissolve(0.3)
    mi 10 "最好就当什么都没发生。" with Dissolve(0.3)
    scene date_event_1_minami_211 with Dissolve(0.3)
    mi 10 "把钥匙给我——我去换衣服，然后锁门。" with Dissolve(0.3)
    
    play sound keys_drop
    
    scene date_event_1_minami_212 with Dissolve(0.2)
    pause 1.5
    scene date_event_1_minami_213 with Dissolve(0.5)
    mi 10 "[gg]。" with Dissolve(0.3)
    scene date_event_1_minami_214 with Dissolve(0.3)
    gg 25 "嗯？" with Dissolve(0.3)
    
    show screen rel_up_minami
    $ love_mi +=6
    
    scene date_event_1_minami_215 with Dissolve(0.3)
    mi 10 "谢谢你陪我。" with Dissolve(0.3)
    
    stop music3 fadeout 4
    
    $ date_event_1_minami = True
    
    scene black with Dissolve(1.5)
    pause 2
    
    if date_event_1_lillian == True:
        pause 2
        jump end_tatsumi
        
    else:
        pause 1
        jump date_event_1_lillian_after_minami
        
label date_event_1_lillian_after_minami:

    play music4 science_documentary_loop fadein 5

    show date_event_1_lillian_after_minami_1 with Dissolve(0.5)
    $ renpy.pause (4.5, hard=True)
    scene date_event_1_lillian_after_minami_1_1 with Dissolve(0.3)
    hide date_event_1_lillian_after_minami_1
    
    $ date_event_1_after_minami = True
    
    if date_event_1_day == 1:
        jump date_event_1_choice
    elif date_event_1_day == 2:
        jump date_event_1_choice

###### DATE EVENT - LILLIAN

label date_event_1_lillian_start:

    scene date_event_1_lillian_1 with Dissolve(0.3)
    pause 1.3
        
    jump date_event_1_lillian
    
label date_event_1_lillian:
    
    if date_event_1_after_minami == True:
        scene date_event_1_lillian_after_minami_2 with Dissolve(0.3)
    else:
        scene date_event_1_lillian_2 with Dissolve(0.3)
    pause 1.3
    
    if date_event_1_after_minami == True:
        scene date_event_1_lillian_after_minami_3 with Dissolve(0.3)
        gg 23 "嘿，[li]。怎么了？" with Dissolve(0.3)
    else:
        scene date_event_1_lillian_3 with Dissolve(0.3)
        gg 2 "嘿，[li]。怎么了？" with Dissolve(0.3)
    
    if date_event_1_after_minami == True:
        show date_event_1_lillian_after_minami_4:
            xpos 0
            ease 0.5 xpos -400
    else:
        show date_event_1_lillian_4:
            xpos 0
            ease 0.5 xpos -400

    stop music4 fadeout 8
    play music3 marimba_is_loop_02 fadein 4
    play sound woosh1
    
    show date_event_1_lillian_5 with Dissolve(0.3):
        xpos 1930
        ease 0.5 xpos 0
    
    li 6 "嘿！都好啊，你呢？" with Dissolve(0.3)
    
    if date_event_1_after_minami == True:
        scene date_event_1_lillian_after_minami_6 with Dissolve(0.3)
        gg 23 "我也还行。那么，听着，今天也许能见个面吗？出去走走之类的。" with Dissolve(0.3)
    else:
        scene date_event_1_lillian_6 with Dissolve(0.3)
        gg 2 "我也还行。那么，听着，今天也许能见个面吗？出去走走之类的。" with Dissolve(0.3)
    
    if date_event_1_after_minami == True:
        scene date_event_1_lillian_after_minami_7 with Dissolve(0.3)
    else:
        scene date_event_1_lillian_7 with Dissolve(0.3)
    
    li 6 "呃，今天？有点突然，不过可以。" with Dissolve(0.3)
    
    if date_event_1_after_minami == True:
        scene date_event_1_lillian_after_minami_8 with Dissolve(0.3)
        li 6 "我刚做完家里的活。四十分钟后见可以吗？" with Dissolve(0.3)
    else:
        scene date_event_1_lillian_8 with Dissolve(0.3)
        li 6 "还是接近傍晚的时候吧，如果你不介意。" with Dissolve(0.3)
    
    if date_event_1_after_minami == True:
        scene date_event_1_lillian_after_minami_9 with Dissolve(0.3)
        gg 23 "当然不介意。那么……在哪儿见？" with Dissolve(0.3)
        gg 23 "我建议找个具体的地方，安静又舒适的那种。不过我对这座城还不太熟，你懂的。"
    else:
        scene date_event_1_lillian_9 with Dissolve(0.3)
        gg 2 "当然不介意。那么……在哪儿见？" with Dissolve(0.3)
        gg 2 "我建议找个具体的地方，安静又舒适的那种。不过我对这座城还不太熟，你懂的。"
    
    if date_event_1_after_minami == True:
        scene date_event_1_lillian_after_minami_10 with Dissolve(0.3)
    else:
        scene date_event_1_lillian_10 with Dissolve(0.3)
    
    li 6 "在公园见吧，离我家不远。那儿安静又舒服。我开始收拾的时候把定位发给你。" with Dissolve(0.3)
    
    if date_event_1_after_minami == True:
        scene date_event_1_lillian_after_minami_11 with Dissolve(0.3)
        gg 23 "说定了。到时候见！" with Dissolve(0.3)
    else:
        scene date_event_1_lillian_11 with Dissolve(0.3)
        gg 2 "说定了。到时候见！" with Dissolve(0.3)
    
    $ date_event_1_after_minami = False

    stop music3 fadeout 4
    
    scene black with Dissolve(1.0)
    pause 2
    
    $ renpy.music.set_volume(1, delay=0, channel=u'music2')
    play music2 morning_in_a_city_park fadein 5
    
    pause 1

    show date_event_1_lillian_12 with Dissolve(1.0)
    $ renpy.pause (4, hard=True)
    show date_event_1_lillian_12_1 with Dissolve(0.3)
    hide scene date_event_1_lillian_12
    pause 0.5
    "正如[li]所说，公园确实是个见面的好地方。"
    scene date_event_1_lillian_13 with Dissolve(0.5)
    "微风拂过树梢，空气中飘着青草和花朵的清新气息。"
    scene date_event_1_lillian_14 with Dissolve(0.5)
    "附近某处鸟儿在相互鸣叫，偶尔才传来路人压低的笑声。"
    scene date_event_1_lillian_15 with Dissolve(0.5)
    "她已经在那儿等我了——坐在喷泉边的旧木椅上，若有所思地看着水珠上的光点。"
    
    $ renpy.music.set_volume(0.2, delay=5, channel=u'music2')
    play music3 back_on_your_feet_main_full
    
    scene date_event_1_lillian_16 with Dissolve(0.3)
    gg 23 "嘿。等很久了吗？" with Dissolve(0.3)
    scene date_event_1_lillian_17 with Dissolve(0.3)
    li 7 "没有，我也刚到。" with Dissolve(0.3)
    scene date_event_1_lillian_18 with Dissolve(0.3)
    "她笑了笑，但眼里能看出一丝不安。"
    scene date_event_1_lillian_19 with Dissolve(0.3)
    gg 23 "你看起来有心事。出什么事了？" with Dissolve(0.3)
    scene date_event_1_lillian_20 with Dissolve(0.3)
    li 7 "没什么，就是……今天有点奇怪。" with Dissolve(0.3)
    scene date_event_1_lillian_21 with Dissolve(0.3)
    gg 23 "那就起来，我们走走吧。" with Dissolve(0.3)
    scene date_event_1_lillian_22 with Dissolve(1.0)
    pause 1
    scene date_event_1_lillian_23 with Dissolve(0.5)
    "[li]没说话，可她的目光一次次回到我身上。像是想说点什么又不敢。"
    scene date_event_1_lillian_24 with Dissolve(0.3)
    gg 23 "说吧，告诉我，出什么事了？" with Dissolve(0.3)
    scene date_event_1_lillian_25 with Dissolve(0.3)
    li 7 "不是什么大事，但……嗯……我跟你提过我的前任吧，就是那个，怎么说……" with Dissolve(0.3)
    scene date_event_1_lillian_26 with Dissolve(0.3)
    gg 23 "那个混蛋。记得。" with Dissolve(0.3)
    scene date_event_1_lillian_27 with Dissolve(0.3)
    
    if date_event_1_day == 1:
        li 7 "对。昨天他在我的窗外站了一整天，想跟我谈谈……复合。" with Dissolve(0.3)
    else:
        li 7 "对。前天他也在我的窗外站了一整天，想跟我谈谈……复合。" with Dissolve(0.3)
        
    scene date_event_1_lillian_28 with Dissolve(0.3)
    gg 23 "所以是因为他？你才决定不出去的，怕碰上他？" with Dissolve(0.3)
    scene date_event_1_lillian_29 with Dissolve(0.3)
    li 7 "算是吧……我知道这听起来不怎么样。但当时那样子真的很瘆人。" with Dissolve(0.3)
    li 7 "他……好像困在过去出不来。说了些奇怪的话……而且……他现在多半又在窗外等着我。"
    scene date_event_1_lillian_30 with Dissolve(0.3)
    gg 23 "你确定？" with Dissolve(0.3)
    scene date_event_1_lillian_31 with Dissolve(0.3)
    li 7 "我在见你之前给他发了消息。说想见我。" with Dissolve(0.3)
    scene date_event_1_lillian_32 with Dissolve(0.3)
    li 7 "而且我在所有能屏蔽的地方都把他拉黑了。他还是有办法让我知道他在。" with Dissolve(0.3)
    li 7 "……我只是不想一个人碰上他。"
    scene date_event_1_lillian_33 with Dissolve(0.3)
    gg 23 "听起来他算是跟踪狂了。" with Dissolve(0.3)
    scene date_event_1_lillian_34 with Dissolve(0.3)
    li 7 "我真的希望还没到那一步。唉……" with Dissolve(0.3)
    scene date_event_1_lillian_35 with Dissolve(0.3)
    li 7 "今天你能送我回家就好了……回程的车费我出。" with Dissolve(0.3)
    scene date_event_1_lillian_36 with Dissolve(0.3)
    gg 23 "说什么呢！别担心，不麻烦。" with Dissolve(0.3)
    scene date_event_1_lillian_37 with Dissolve(0.3)
    li 7 "那么，你答应了？" with Dissolve(0.3)
    scene date_event_1_lillian_38 with Dissolve(0.3)
    gg 23 "当然。听你说了这么多，我怎么可能让你一个人。" with Dissolve(0.3)
    scene date_event_1_lillian_39 with Dissolve(0.3)
    pause 1
    scene date_event_1_lillian_40 with Dissolve(0.5)
    li 7 "嘿嘿……谢谢。真的。" with Dissolve(0.3)
    
    stop music2 fadeout 6
    
    scene date_event_1_lillian_41 with Dissolve(0.3)
    "我们在树叶的沙沙声里穿过公园。路灯的光穿过枝叶洒落，在小路上投下斑驳的金色。"
    "每走一步，她的步伐都更笃定些，脸上那抹淡淡的阴翳也逐渐被笑容取代。"
    scene date_event_1_lillian_42 with Dissolve(0.3)
    "有那么一会儿，一切都变得很简单：聊学校、开玩笑、说些有的没的。"
    "在她明亮而有些心不在焉的笑声里，我听见了那个我早已习惯的声音。"

    play music4 streetambience_ldj_audio_v2 fadein 2 volume 0.5
    stop music3 fadeout 10
    
    scene date_event_1_lillian_43 with Dissolve(0.3)
    "但当我们转上她熟悉的那条街、走近她家时，那刚刚还在温暖我的笑容消失了，她方才还灵动明亮的眼神也忽然黯淡下去。"
    gg 23 "不好的念头涌上来了？" with Dissolve(0.3)
    li 7 "诶？……嗯……" with Dissolve(0.3)
    scene date_event_1_lillian_44 with Dissolve(0.3)
    gg 23 "想再走一会儿吗？不用急着回家。" with Dissolve(0.3)
    scene date_event_1_lillian_45 with Dissolve(0.3)
    li 7 "我很想……可一方面我不想，另一方面又觉得应该面对他。" with Dissolve(0.3)
    scene date_event_1_lillian_46 with Dissolve(0.3)
    li 7 "抱歉，那个……有点利用你来让他退开。" with Dissolve(0.3)
    
    play music3 background_piano_loop_by_newzhilla fadein 8
    stop music4 fadeout 20
    
    scene date_event_1_lillian_47 with Dissolve(0.3)
    gg 23 "嘿，不用道歉！我很乐意帮忙。如果需要的话……" with Dissolve(0.3)
    scene date_event_1_lillian_48 with Dissolve(0.3)
    gg 23 "我可以帮你砸点东西，要我干吗？" with Dissolve(0.3)
    scene date_event_1_lillian_49 with Dissolve(0.3)
    li 7 "什么？！不用！" with Dissolve(0.3)
    scene date_event_1_lillian_50 with Dissolve(0.3)
    li 7 "他会报案的！" with Dissolve(0.3)
    scene date_event_1_lillian_51 with Dissolve(0.3)
    gg 23 "刚才那一瞬间，我还以为你担心的是他的身体。" with Dissolve(0.3)
    
    show date_event_1_lillian_53 with Dissolve(0.3)
    li 7 "我不在乎他的身体。让我火大的是他还想拿回点什么。" with Dissolve(0.3)
    show date_event_1_lillian_52 with Dissolve(0.3)
    hide date_event_1_lillian_53
    gg 23 "你们是怎么认识的？" with Dissolve(0.3)
    show date_event_1_lillian_55 with Dissolve(0.3)
    hide date_event_1_lillian_52
    li 7 "我们有共同的朋友……好像甚至不是在学校认识的。" with Dissolve(0.3)
    li 7 "我们是在一个家庭派对上认识的。音乐很响，所有人都在跳舞、喝酒、聊天……"
    li 7 "而我就是融入不进去。我只是坐在角落里，端着一杯汽水，看别人玩得开心。"
    show date_event_1_lillian_52 with Dissolve(0.3)
    hide date_event_1_lillian_55
    gg 23 "真的？我不信会没人搭讪你这样的美女。" with Dissolve(0.3)
    show date_event_1_lillian_54 with Dissolve(0.3)
    hide date_event_1_lillian_52
    li 7 "哈哈……其实还真有。他就是其中之一。" with Dissolve(0.3)
    li 7 "在所有人里，他算是……最正派的那个。然后不知怎么就变成了朋友。"
    li 7 "说真的，那之后他看着仍像个好人。他很细心。送我花、糖果，经常发消息。"
    show date_event_1_lillian_52 with Dissolve(0.3)
    hide date_event_1_lillian_54
    gg 23 "听起来他当时很认真。不过话说回来，看你这样也不奇怪。" with Dissolve(0.3)
    show date_event_1_lillian_55 with Dissolve(0.3)
    hide date_event_1_lillian_52
    li 7 "那时候我对这一切都很满意。但现在我觉得，也许当时我身边根本没有更好的人。" with Dissolve(0.3)
    li 7 "现在回头看就很清楚了，因为过了一阵子，他突然变得很强势。"
    
    show date_event_1_lillian_58 with Dissolve(0.3)
    hide date_event_1_lillian_55
    li 7 "我不想太快推进，而他对此非常生气。好像我欠他什么似的。" with Dissolve(0.3)
    li 7 "我能理解他是出于关心，但……"
    show date_event_1_lillian_56 with Dissolve(0.3)
    hide date_event_1_lillian_58
    gg 23 "又或者他觉得，送过花和别的礼物就该得到什么。" with Dissolve(0.3)
    
    show date_event_1_lillian_54 with Dissolve(0.3)
    hide date_event_1_lillian_56
    li 7 "呃……说实话我真不想这么想。" with Dissolve(0.3)
    li 7 "不过当时，我觉得我们之间一切都还好。至少一开始是这样。"
    show date_event_1_lillian_52 with Dissolve(0.3)
    hide date_event_1_lillian_54
    gg 23 "我明白了。重要的是你自己走出来了，没有忍受那种对待。" with Dissolve(0.3)
    show date_event_1_lillian_55 with Dissolve(0.3)
    hide date_event_1_lillian_52
    li 7 "嗯……不过其实有段时间，我几乎完全不理他了。" with Dissolve(0.3)
    li 7 "这让我显得很懦弱吗？"
    show date_event_1_lillian_52 with Dissolve(0.3)
    hide date_event_1_lillian_55
    gg 23 "一点也不。你不欠他什么，如果他还不懂，那混蛋是他自己。" with Dissolve(0.3)
    li 7 "{cps=5}……{/cps}" with Dissolve(0.3)
    show date_event_1_lillian_57 with Dissolve(0.3)
    hide date_event_1_lillian_52
    li 7 "希望跟我在一起时……" with Dissolve(0.3)
    show date_event_1_lillian_56 with Dissolve(0.3)
    hide date_event_1_lillian_57
    gg 23 "我保证你绝不会从我这儿受到任何恶心待遇！" with Dissolve(0.3)
    show date_event_1_lillian_58 with Dissolve(0.3)
    hide date_event_1_lillian_56
    li 7 "……谢谢。听你这么说我很高兴。" with Dissolve(0.3)
    
    play music4 streetambience_ldj_audio_v2 fadein 2 volume 0.5
    $ renpy.music.set_volume(0.3, delay=1, channel=u'music3')
    
    scene date_event_1_lillian_59 with Dissolve(0.3)
    li 7 "天啊……" with Dissolve(0.3)
    scene date_event_1_lillian_60 with Dissolve(0.3)
    gg 23 "你前任？" with Dissolve(0.3)
    
    stop music3 fadeout 3
    play music2 jazzy_suspense_seamless_loop
    
    scene date_event_1_lillian_61 with Dissolve(0.3)
    yuto 2 "嘿，[li]！好久不见！" with Dissolve(0.3)
    scene date_event_1_lillian_62 with Dissolve(0.3)
    li 7 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_lillian_63 with Dissolve(0.3)
    gg 23 "{cps=5}……{/cps}" with Dissolve(0.3)
    scene date_event_1_lillian_64 with Dissolve(0.3)
    yuto 2 "哈哈！这就是你说的那个「新男人」？" with Dissolve(0.3)
    scene date_event_1_lillian_65 with Dissolve(0.3)
    yuto 2 "我知道他为什么来。你觉得他是要伤害我？" with Dissolve(0.3)
    scene date_event_1_lillian_66 with Dissolve(0.3)
    gg 23 "你要是看不出她有多讨厌你陪在身边，那就是瞎了。你到底在她家门口干什么？" with Dissolve(0.3)
    scene date_event_1_lillian_67 with Dissolve(0.3)
    yuto 2 "首先，我是你女朋友的男人……" with Dissolve(0.3)
    
    $ renpy.music.set_volume(1, delay=0, channel=u'music3')
    play sound slap_in_the_face
    
    scene date_event_1_lillian_68 with hpunch
    pause 1
    
    play sound2 heavy_body_fall_01
    
    scene date_event_1_lillian_69 with Dissolve(0.3)
    gg 23 "我再说一遍。你他妈是谁，来这儿干什么？" with Dissolve(0.3)
    scene date_event_1_lillian_70 with Dissolve(0.3)
    yuto 2 "咳……" with Dissolve(0.3)
    scene date_event_1_lillian_71 with Dissolve(0.3)
    yuto 2 "我叫[yuto]。[li]没跟你提过我？" with Dissolve(0.3)
    
    play sound3 walking_4
    
    scene date_event_1_lillian_72 with Dissolve(0.3)
    pause 1
    stop sound3 fadeout 0.3
    
    scene date_event_1_lillian_73 with Dissolve(0.3)
    yuto 2 "对了，还有刚才那一拳？几乎没感觉！" with Dissolve(0.3)
    scene date_event_1_lillian_74 with Dissolve(0.3)
    gg 23 "我建议你走。下次会更疼。" with Dissolve(0.3)
    scene date_event_1_lillian_75 with Dissolve(0.3)
    yuto 2 "哇，冷静点，何必这么凶？" with Dissolve(0.3)
    scene date_event_1_lillian_76 with Dissolve(0.3)
    yuto 2 "看来[li]挑了个……相当普通的男人。" with Dissolve(0.3)
    scene date_event_1_lillian_77 with Dissolve(0.3)
    gg 23 "普通？你在说什么鬼话？" with Dissolve(0.3)
    scene date_event_1_lillian_78 with Dissolve(0.3)
    yuto 2 "我们其实约好了。约在她家。" with Dissolve(0.3)
    scene date_event_1_lillian_79 with Dissolve(0.3)
    yuto 2 "我们之间还有点东西，对吧，[li]？" with Dissolve(0.3)
    scene date_event_1_lillian_80 with Dissolve(0.3)
    gg 23 "一点都不好笑。混蛋，你在打什么主意？" with Dissolve(0.3)
    scene date_event_1_lillian_81 with Dissolve(0.3)
    yuto 2 "这有什么难的？我们一起出去、喝杯咖啡、打打游戏、聊聊天……" with Dissolve(0.3)
    scene date_event_1_lillian_82 with Dissolve(0.3)
    yuto 2 "然后我们会把邻居都嫉妒死地狠狠干到她叫出声来。" with Dissolve(0.3)
    scene date_event_1_lillian_83 with Dissolve(0.3)
    yuto 2 "她以前是我的女人。而且看样子她连提都没跟你提过我。" with Dissolve(0.3)
    scene date_event_1_lillian_84 with Dissolve(0.3)
    yuto 2 "哦对了，告诉你一件事——她可不是你以为的那种人！" with Dissolve(0.3)
    scene date_event_1_lillian_85 with Dissolve(0.3)
    yuto 2 "想看真相吗？我手机里有些照片。" with Dissolve(0.3)
    scene date_event_1_lillian_86 with Dissolve(0.3)
    li 7 "你这混蛋……" with Dissolve(0.3)
    scene date_event_1_lillian_87 with Dissolve(0.3)
    yuto 2 "哦，刺痛了吗？" with Dissolve(0.3)
    scene date_event_1_lillian_88 with Dissolve(0.3)
    yuto 2 "等你看完要是肯求我，说不定我还让你看我们玩得有多开心。" with Dissolve(0.3)
    scene date_event_1_lillian_89 with Dissolve(0.3)
    li 7 "你在说什么鬼话？！" with Dissolve(0.3)
    scene date_event_1_lillian_90 with Dissolve(0.3)
    yuto 2 "看！" with Dissolve(0.3)
    scene date_event_1_lillian_91 with Dissolve(0.3)
    gg 23 "……这他妈是什么玩意儿？" with Dissolve(0.3)
    scene date_event_1_lillian_92 with Dissolve(0.3)
    yuto 2 "想看近一点吗？" with Dissolve(0.3)
    
    play sound3 grab_plastic_2
    
    scene date_event_1_lillian_93 with Dissolve(0.3)
    gg 23 "看啊。给我……让我看看。" with Dissolve(0.3)
    
    play sound2 kick_6
    
    scene date_event_1_lillian_94 with vpunch
    pause 1.5
    
    play sound dm1
    
    scene date_event_1_lillian_95 with Dissolve(0.3)
    yuto 2 "嘿！那可是MyPhone 19！你知道那玩意儿多少钱吗？！" with Dissolve(0.3)
    scene date_event_1_lillian_96 with Dissolve(0.3)
    gg 23 "比假牙还贵？" with Dissolve(0.3)
    scene date_event_1_lillian_97 with Dissolve(0.3)
    yuto 2 "什、什么？呃……嗯，也、也可能是吧，不过得看是哪种……" with Dissolve(0.3)
    
    play sound4 blood_gore_impact_1 volume 0.5
    play sound5 fight_punches_hollywood_4
    
    scene date_event_1_lillian_98 with hpunch
    pause 1.5
    
    play sound6 fight_punches_gutbonebreakes_1
    
    scene date_event_1_lillian_99 with vpunch
    pause 1
    scene date_event_1_lillian_100 with Dissolve(0.3)
    yuto 3 "正、正正赶时髦呢……" with Dissolve(0.3)
    scene date_event_1_lillian_101 with Dissolve(0.3)
    gg 23 "看来你是那种连话都听不懂的人。" with Dissolve(0.3)
    scene date_event_1_lillian_102 with Dissolve(0.3)
    yuto 3 "呃啊……操！" with Dissolve(0.3)
    scene date_event_1_lillian_103 with Dissolve(0.3)
    gg 23 "我警告过你了，蠢货。" with Dissolve(0.3)
    scene date_event_1_lillian_104 with hpunch
    gg 23 "现在给我滚出去！"
    scene date_event_1_lillian_105 with Dissolve(0.3)
    yuto 3 "你、你根本不了解她！第一次碰、碰到比她强的男人，她、她就会直接跟他上床！" with Dissolve(0.3)
    
    play sound fight_punches_light_b_1
    
    scene date_event_1_lillian_106 with hpunch
    gg 23 "你敢再靠近她一步试试。听到没有？！" with Dissolve(0.3)
    scene date_event_1_lillian_107 with Dissolve(0.3)
    yuto 3 "哈……听说还得对付她家的看门狗，连它都懒得起来！" with Dissolve(0.3)
    scene date_event_1_lillian_108 with Dissolve(0.3)
    yuto 3 "操、操……这、这也太他妈疼了……" with Dissolve(0.3)
    
    stop music2 fadeout 5
    
    scene date_event_1_lillian_109 with Dissolve(0.3)
    gg 23 "{cps=5}……{/cps}" with Dissolve(0.3)
    
    play music3 background_piano_loop_by_newzhilla fadein 8
    
    scene date_event_1_lillian_110 with Dissolve(0.3)
    li 7 "谢谢……" with Dissolve(0.3)
    scene date_event_1_lillian_111 with Dissolve(0.3)
    li 7 "也抱歉你因为我特意跑过来。" with Dissolve(0.3)
    scene date_event_1_lillian_112 with Dissolve(0.3)
    gg 23 "没事。随时都可以。" with Dissolve(0.3)
    
    if love_li >= 13:
    
        scene date_event_1_lillian_113 with Dissolve(0.3)
        li 7 "要不要进来坐坐？" with Dissolve(0.3)
        scene date_event_1_lillian_114 with Dissolve(0.3)
        gg 23 "什么？" with Dissolve(0.3)
        scene date_event_1_lillian_115 with Dissolve(0.3)
        li 7 "你刚才那么勇敢地替我出头，不谢谢你才是傻瓜。" with Dissolve(0.3)
        scene date_event_1_lillian_113 with Dissolve(0.3)
        li 7 "进来吧，我给你煮杯咖啡。我爸妈很晚才回来，别害羞。" with Dissolve(0.3)
        scene date_event_1_lillian_114 with Dissolve(0.3)
        
        menu:
            "「当然，我很愿意。」\\n[gold](莉莲 +5)[pink](性爱场景)":
                gg 23 "当然，我很愿意。" with Dissolve(0.3)
                
                stop music4 fadeout 3
                stop music3 fadeout 3
                
                scene black with Dissolve(1.0)
                pause 2
                pause 1
                
                jump date_event_1_lillian_home
                
            "「我有别的事要做。」\\n[gold](莉莲 +3)":
                gg 23 "我也很想去，不过还有点事要处理……下次吧。" with Dissolve(0.3)

                jump date_event_1_lillian_leave
            
    else:
        
        scene date_event_1_lillian_115 with Dissolve(0.3)
        li 7 "那个……我该走了。今晚真的很开心。" with Dissolve(0.3)
        scene date_event_1_lillian_114 with Dissolve(0.3)
        gg 23 "嗯，早点休息。" with Dissolve(0.3)
        jump date_event_1_lillian_leave

label date_event_1_lillian_leave:

    scene date_event_1_lillian_116 with Dissolve(0.3)
    li 7 "好吧……那我就不留你了。回头见！" with Dissolve(0.3)
    scene date_event_1_lillian_117 with Dissolve(0.3)
    gg 23 "回见！" with Dissolve(0.3)
    
    play sound2 walking_1
    
    scene date_event_1_lillian_118 with Dissolve(0.5)
    pause 1
    
    stop sound2 fadeout 3
    
    scene date_event_1_lillian_119 with Dissolve(0.5)
    pause 1.5
    
    $ date_event_1_day += 1
    $ date_event_1_lillian = True
    $ love_li += 3
    show screen rel_up_lillian
    
    stop music3 fadeout 4
    stop music4 fadeout 4

    scene black with Dissolve(1.0)
    pause 2
    pause 2

    if date_event_1_may == True:
        jump end_tatsumi
        
    else:
        show date_event_1_intro_18 with Dissolve(1.0)
        jump date_event_1_choice
    
    
label date_event_1_lillian_home:
    
    play music2 faiths_reward_main_full fadein 5 
    
    show date_event_1_lillian_120 with Dissolve(0.05)
    $ renpy.pause (10.5, hard=True)
    
    scene date_event_1_lillian_121 with Dissolve(0.5)
    gg 23 "哇，这咖啡真的很好喝。" with Dissolve(0.3)
    scene date_event_1_lillian_122 with Dissolve(0.3)
    gg 23 "我以为是速溶的，没想到你还是家里有专属机的手冲咖啡师。" with Dissolve(0.3)
    scene date_event_1_lillian_123 with Dissolve(0.3)
    li 7 "要再来一杯吗？" with Dissolve(0.3)
    scene date_event_1_lillian_124 with Dissolve(0.3)
    gg 23 "现在不用了，谢谢。" with Dissolve(0.3)
    
    play sound sipping_hot_tea_from_mug volume 0.6
    
    scene date_event_1_lillian_125 with Dissolve(0.3)
    pause 1.5
    scene date_event_1_lillian_126 with Dissolve(0.3)
    gg 23 "{cps=5}……{/cps}"
    scene date_event_1_lillian_127 with Dissolve(0.3)
    gg 23 "看来你把他气得够呛。" with Dissolve(0.3)
    
    show date_event_1_lillian_131 with Dissolve(0.3)
    li 7 "真搞不懂他当时在想什么。为什么要那样丢自己的人……" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_131
    gg 23 "至少他现在不敢再来了。" with Dissolve(0.3)
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "希望吧。不过还是难以相信。他以前看起来那么……正常。甚至还挺体贴。" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "人初次见面的时候，往往会把自己伪装成跟真实性格完全相反的样子。" with Dissolve(0.3)
    gg 23 "尤其是当他们以为对方安静、好摆布的时候。"
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "喂，你刚才是在说我是那种人吗？" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "我又没说你真是。不过……那天的派对上，你看起来确实像。" with Dissolve(0.3)
    show date_event_1_lillian_131 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "我只是不太喜欢吵闹的人群。我同学很喜欢那种场合，但我去了只会格格不入。" with Dissolve(0.3)
    show date_event_1_lillian_133 with Dissolve(0.3)
    hide date_event_1_lillian_131
    li 7 "不过说实话……上次跟你一起玩，我确实很开心。" with Dissolve(0.3)
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_133
    gg 23 "听你这么说我很高兴。我懂你的意思。" with Dissolve(0.3)
    gg 23 "有些人就是更适合待在家里、上上网、跟亲近的人待在一起。"
    gg 23 "不过我倒是找到了一份在酒吧打工的活。那家店看着还停在六十年代，那里基本上就是一场永不落幕的派对，只不过比较……有格调。"
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "在那里工作不会让你难受吗？" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "不好说。现在我也没什么选择余地，做不做都得做。" with Dissolve(0.3)
    gg 23 "不过我觉得，调调酒、站在旁边看着，比真的参与进去要好太多了。"
    gg 23 "有时候得听醉鬼胡说八道，不过那都不算什么。"
    show date_event_1_lillian_132 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "哈哈！这才是睿智沉稳的调酒师形象啊——随时准备好聊天，顺便指点人生！" with Dissolve(0.3)
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_132
    gg 23 "对我来说只是一份工作而已。只要给钱，又不烦我，为什么不干？" with Dissolve(0.3)
    show date_event_1_lillian_133 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "我觉得你站在吧台后肯定特别好看。真想看看你穿上调酒师制服的样子……" with Dissolve(0.3)
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_133
    gg 23 "那改天过来坐坐，我给你调几杯。" with Dissolve(0.3)
    show date_event_1_lillian_132 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "那就这么说定了！" with Dissolve(0.3)
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_132
    gg 23 "（嗯……以她的身材，来我们这里肯定很合适。客人都会专程为了看她而来。）" with Dissolve(0.3)
    gg 23 "（但还是算了。谁知道那些客人会怎么对待女招待？我在吧台后面也不可能面面俱到。）"
    gg 23 "（幸好现在她是我的，只属于我一个人。）"
    show date_event_1_lillian_133 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "我以前房间里有一整排书架，塞满了书和漫画。现在应该还放在哪里，只是最近我都在网上看。" with Dissolve(0.3)
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_133
    gg 23 "你就是这样跟[leah]交上朋友的，对吧？" with Dissolve(0.3)
    show date_event_1_lillian_133 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "嗯……跟她说话带来的快乐，几乎胜过这座城市里任何一段关系。" with Dissolve(0.3)
    li 7 "当然……除了遇见你之外。"
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_133
    gg 23 "听你这么说真好。那你原本是哪里人？" with Dissolve(0.3)
    show date_event_1_lillian_133 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "我是在这里出生的。不过我小时候，跟你一样，我和父母搬走了。" with Dissolve(0.3)
    li 7 "我外公是纯德国人。他经营一家电池制造公司。"
    show date_event_1_lillian_131 with Dissolve(0.3)
    hide date_event_1_lillian_133
    li 7 "他身体变差之后，爸爸决定让我们搬去跟他住一阵。所以我们在德国住了一段时间。" with Dissolve(0.3)
    li 7 "那会儿我还很小。妈妈不是纯日本人，跟当地人沟通很困难。而且不是所有人都会说英语。"
    li 7 "两年半之后我们回来了，爸爸也恢复了原来的职位，然后……就这样了。"
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_131
    gg 23 "你外公现在怎么样？" with Dissolve(0.3)
    show date_event_1_lillian_133 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "挺好的。身体也没问题，现在退休了。老是给我们发他去打猎、钓到鱼的视频。" with Dissolve(0.3)
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_133
    gg 23 "他多大年纪了？" with Dissolve(0.3)
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "今年六十七岁。" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "所以你爸那边是德国人，你妈是日本人。" with Dissolve(0.3)
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "一半吧。她妈妈是摩尔多瓦人。" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "挺酷的，血管里流着这么多国家的血。" with Dissolve(0.3)
    show date_event_1_lillian_133 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "嗯，一想到这个我就很喜欢。" with Dissolve(0.3)
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_133
    gg 23 "你刚说你爸爸恢复了原来的职位——是什么职位？" with Dissolve(0.3)
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "高级督察。" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "警察？" with Dissolve(0.3)
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "对，他管一个部门，自己带一队人。" with Dissolve(0.3)
    li 7 "他说再过一年左右，可能升任副署长。"
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "他多大年纪了？" with Dissolve(0.3)
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "四十七岁。" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "这么年轻就快当上副署长了。看来他业绩很出色啊？" with Dissolve(0.3)
    show date_event_1_lillian_133 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "好像是吧。我为他骄傲！" with Dissolve(0.3)
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_133
    gg 23 "那惹你可危险了——他能把我送进监狱！" with Dissolve(0.3)
    show date_event_1_lillian_132 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "就是说！哈哈。" with Dissolve(0.3)
    
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_132
    pause 1.5
    
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "话说，你看到我的照片时为什么反应那么大？" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "你的照片？" with Dissolve(0.3)
    show date_event_1_lillian_131 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "[yuto]给你看的那张……" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_131
    gg 23 "什么？那根本就不是照片！" with Dissolve(0.3)
    gg 23 "他只是把你的脑袋剪成方块，贴到某个裸女的身体上而已。"
    gg 23 "这种垃圾东西，自从大家开始拿画图程序当图像编辑器之后我就没见过。"
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "真的？我都没看清他到底给我看了什么……" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "简直离谱。我完全不知道他图什么——那种东西连初中生都骗不过！" with Dissolve(0.3)
    show date_event_1_lillian_131 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "嗯，那他应该已经把那些删了……" with Dissolve(0.3)
    li 7 "如果他只是想激怒你，就会拿别的东西给你看了。"
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_131
    gg 23 "（所以她真的给他发了照片？）" with Dissolve(0.3)
    gg 23 "（也许其中一张，就是我们出去喝酒时我看到的那张。）"
    gg 23 "不管怎样都无所谓了。那部手机已经没了。"
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "嗯。" with Dissolve(0.3)
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_130
    pause 1.5
    show date_event_1_lillian_133 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "你知道吗，要是我能早点遇见你就好了。" with Dissolve(0.3)
    li 7 "在我遇到他之前……我真希望自己能回到过去，痛快地甩了他一次，而不是像现在这样收场。"
    show date_event_1_lillian_129 with Dissolve(0.3)
    hide date_event_1_lillian_133
    gg 23 "他肯定接受不了。你要是直接跟他翻脸，他很可能会伤害你。" with Dissolve(0.3)
    show date_event_1_lillian_131 with Dissolve(0.3)
    hide date_event_1_lillian_129
    li 7 "也许我怕的正是这个……不过，你听了那么多关于我的混账话，还替我收拾烂摊子，真的很对不起。" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_131
    gg 23 "[li]，你经历了很多。谁都会犯错，我也会。至于照片的事，别放在心上。" with Dissolve(0.3)
    gg 23 "很多男生女生都这么干。只要不外传，就没什么好羞耻的。"
    show date_event_1_lillian_131 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "嗯，我明白。我只是担心会让你不舒服。" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_131
    gg 23 "那时候你跟他很亲近，信任他。但现在你更成熟、更清醒了。而且人在我手里，很安全。" with Dissolve(0.3)
    gg 23 "所以别再自己吓自己了。"
    pause 1.5
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "……等等，我好像搞错了。你说的照片，是指……那种私密照？" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "……嗯，是啊。" with Dissolve(0.3)
    show date_event_1_lillian_136 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "天哪，[gg]！我从来没给他发过那种照片！" with Dissolve(0.3)
    show date_event_1_lillian_134 with Dissolve(0.3)
    hide date_event_1_lillian_136
    gg 23 "是吗？" with Dissolve(0.3)
    show date_event_1_lillian_133 with Dissolve(0.3)
    hide date_event_1_lillian_134
    li 7 "我还以为我们说的是那种蠢照片……" with Dissolve(0.3)
    li 7 "就是那种鬼脸、奇怪姿势……之类以后回想起来会让自己尴尬的东西。"
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_133
    gg 23 "啊……靠，看来是我完全搞错了。" with Dissolve(0.3)
    show date_event_1_lillian_130 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "都怪那个白痴！肯定是他让你误会了。" with Dissolve(0.3)
    show date_event_1_lillian_128 with Dissolve(0.3)
    hide date_event_1_lillian_130
    gg 23 "也许吧……说真的，我还记得那天晚上在酒吧，你不小心给我看的那张照片。" with Dissolve(0.3)
    show date_event_1_lillian_136 with Dissolve(0.3)
    hide date_event_1_lillian_128
    li 7 "那张不是发给他的……" with Dissolve(0.3)
    show date_event_1_lillian_134 with Dissolve(0.3)
    hide date_event_1_lillian_136
    gg 23 "{cps=5}……{/cps}" with Dissolve(0.3)
    gg 23 "（给别人看的？）"
    gg 23 "懂了。那就跟我没关系了。"
    show date_event_1_lillian_136 with Dissolve(0.3)
    hide date_event_1_lillian_134
    li 7 "你又想多了。是发给我的。我只是喜欢……" with Dissolve(0.3)
    li 7 "有时候喜欢看看自己，看看自己的身材，仅此而已。"
    show date_event_1_lillian_135 with Dissolve(0.3)
    hide date_event_1_lillian_136
    gg 23 "我也喜欢看你……你很美。而且你真的有很多值得骄傲的地方。" with Dissolve(0.3)
    show date_event_1_lillian_137 with Dissolve(0.3)
    hide date_event_1_lillian_135
    li 7 "……可恶！都怪你，我现在脸都红了！" with Dissolve(0.3)
    show date_event_1_lillian_135 with Dissolve(0.3)
    hide date_event_1_lillian_137
    gg 23 "放轻松，我不是想让你难堪。" with Dissolve(0.3)
    li 7 "{cps=5}……{/cps}" with Dissolve(0.3)
    show date_event_1_lillian_138 with Dissolve(0.3)
    hide date_event_1_lillian_135
    li 7 "你知道吗……有时候我觉得，跟你在一起的一切都太顺利了。" with Dissolve(0.3)
    li 7 "你总是这么体谅人，像是刻意在讨好我一样……还是说你本来就是这样，一直都是？"
    show date_event_1_lillian_134 with Dissolve(0.3)
    hide date_event_1_lillian_138
    gg 23 "这样让你不安吗？" with Dissolve(0.3)
    show date_event_1_lillian_136 with Dissolve(0.3)
    hide date_event_1_lillian_134
    li 7 "不……恰恰相反。这正是我渴望了很久的——身边能有你这样的人。一个真的就像你这样的人。" with Dissolve(0.3)
    show date_event_1_lillian_135 with Dissolve(0.3)
    hide date_event_1_lillian_136
    gg 23 "那你就当自己找到了灵魂伴侣吧。我不是在演，对你我就是这样。" with Dissolve(0.3)
    li 7 "{cps=5}……{/cps}" with Dissolve(0.3)
    show date_event_1_lillian_138 with Dissolve(0.3)
    hide date_event_1_lillian_135
    li 7 "要不……再多待一会儿？" with Dissolve(0.3)
    show date_event_1_lillian_135 with Dissolve(0.3)
    hide date_event_1_lillian_138
    gg 23 "我本来也没打算这么快走。" with Dissolve(0.3)
    
    stop music2 fadeout 3
    
    scene black with Dissolve(0.5)
    pause 1
    
    play music3 lillian_chill_beat fadein 5
    
    scene date_event_1_lillian_139 with Dissolve(0.3)
    li 7 "你知道吗……现在我更不想让你走了。" with Dissolve(0.3)
    scene date_event_1_lillian_140 with Dissolve(0.3)
    gg 23 "那看来我得去见见你父母了。" with Dissolve(0.3)
    scene date_event_1_lillian_141 with Dissolve(0.3)
    li 7 "哈，我不介意。我觉得我妈肯定会喜欢你。" with Dissolve(0.3)
    scene date_event_1_lillian_142 with Dissolve(0.3)
    gg 23 "那当然。不过你爸会是什么反应？" with Dissolve(0.3)
    scene date_event_1_lillian_143 with Dissolve(0.3)
    li 7 "哦，我都不敢想。……要是他不喜欢你，我可就只能去拘留所看你了。毕竟他是警察。" with Dissolve(0.3)
    scene date_event_1_lillian_144 with Dissolve(0.3)
    gg 23 "就算那样？万一我决定反抗呢？" with Dissolve(0.3)
    scene date_event_1_lillian_145 with Dissolve(0.3)
    li 7 "你是打算为了我跟我爸打架？" with Dissolve(0.3)
    scene date_event_1_lillian_146 with Dissolve(0.3)
    gg 23 "如果他反对，我可能只能把你劫持走了。" with Dissolve(0.3)
    
    play sound clothes_2
    
    scene date_event_1_lillian_147 with Dissolve(0.3)
    li 8 "坏蛋……" with Dissolve(0.3)
    scene date_event_1_lillian_148 with Dissolve(0.3)
    gg 23 "乖乖投降。" with Dissolve(0.3)
    scene date_event_1_lillian_149 with Dissolve(0.3)
    li 8 "要是我不愿意呢？" with Dissolve(0.3)
    scene date_event_1_lillian_150 with Dissolve(0.3)
    gg 23 "那我就只好说服你了。" with Dissolve(0.3)
    scene date_event_1_lillian_151 with Dissolve(0.3)
    li 9 "你知道吗……你挺擅长的……" with Dissolve(0.3)
    
    play sound clothes_3
    
    scene date_event_1_lillian_152 with Dissolve(0.3)
    gg 0 "看来我抓到的人质运气不错。" with Dissolve(0.3)
    
    $ de1_lillian_sex_kiss = False
    $ de1_lillian_sex_lick = False
    $ de1_lillian_sex_1 = False
    $ de1_lillian_sex_2 = False
    
    $ persistent.gallery_de1_lillian = True

    scene black with Dissolve(0.3)
    pause 0.3
    
    ############################################################## SEX_POS_SELECTION_MENU
    show date_event_1_lillian_153 with Dissolve(0.3)
    $ renpy.pause (15.4, hard=True)
    
    show date_event_1_lillian_154 with Dissolve(0.3)
    hide date_event_1_lillian_153
    pause 0.5
    call screen de1_lillian_sex
    
    #show date_event_1_lillian_153 with Dissolve(0.3)
    #$ renpy.pause (13, hard=True)
    
    jump date_event_1_lillian_sex_kiss

label date_event_1_lillian_sex_kiss:

    show date_event_1_lillian_155 with Dissolve(0.3)
    hide date_event_1_lillian_154
    hide date_event_1_lillian_153
    $ renpy.pause (9, hard=True)
    
    play sound kiss_1
    
    $ renpy.pause (0.5, hard=True)
    
    show date_event_1_lillian_156 with Dissolve(0.3)
    pause 0.3
    li 9 "唔……" with Dissolve(0.3)
    scene date_event_1_lillian_157 with Dissolve(0.5)
    li 9 "你好……好辣。我从没想到推开你会这么难……" with Dissolve(0.3)
    scene date_event_1_lillian_158 with Dissolve(0.5)
    gg 0 "你推不开的，别费劲了。" with Dissolve(0.3)
    
    $ de1_lillian_sex_kiss = True
    $ persistent.gallery_date_event_1_lillian_sex_kiss = True
    
    call screen de1_lillian_sex
    
label date_event_1_lillian_sex_lick:
    
    $ de1_lillian_sex_kiss_lock = True
    
    show date_event_1_lillian_159 with Dissolve(0.3)
    hide date_event_1_lillian_154
    $ renpy.pause (8.3, hard=True)
    show date_event_1_lillian_160 with Dissolve(0.3)
    hide date_event_1_lillian_159
    li 9 "我在发抖……都是因为你。" with Dissolve(0.3)
    gg 0 "这是我见过最美的画面。" with Dissolve(0.3)
    
    scene black with Dissolve(0.3)
    pause 0.3
    
    play voice1 voice_lillian_hotel_moan1 volume 0.5
    
    show date_event_1_lillian_161 with Dissolve(0.3)
    hide date_event_1_lillian_160
    ''
    show date_event_1_lillian_162 with Dissolve(0.3)
    hide date_event_1_lillian_161
    ''
    show date_event_1_lillian_163 with Dissolve(0.3)
    hide date_event_1_lillian_162
    
    stop voice1 fadeout 1
    play voice1 voice_lillian_hotel_moan2 volume 0.4
    
    ''
    show date_event_1_lillian_164 with Dissolve(0.3)
    hide date_event_1_lillian_163
    ''
    show date_event_1_lillian_165 with Dissolve(0.3)
    hide date_event_1_lillian_164
    ''
    
    stop voice1 fadeout 1
    
    show date_event_1_lillian_166 with Dissolve(0.3)
    hide date_event_1_lillian_165
    
    $ renpy.pause (2, hard=True)
    
    play voice1 voice_lillian_hotel_orgasm noloop
    
    $ renpy.pause (2.5, hard=True)
    
    scene black with Dissolve(0.3)
    pause 0.6
    
    show date_event_1_lillian_167 with Dissolve(1)
    $ love_li += 1
    show screen rel_up_lillian
    ''
    
    $ de1_lillian_sex_lick = True
    $ persistent.gallery_date_event_1_lillian_sex_lick = True
    
    call screen de1_lillian_sex
    jump date_event_1_lillian_sex_1
    
label date_event_1_lillian_sex_1:

    scene black with Dissolve(0.5)
    pause 0.5
    
    $ de1_lillian_sex_kiss_lock = True
    $ de1_lillian_sex_lick_lock = True

    show date_event_1_lillian_168 with Dissolve(0.5)
    $renpy.pause(8, hard=True)
    
    play sound2 lillian_hotel_109_sound loop
    
    show date_event_1_lillian_169 with Dissolve(0.3)
    hide date_event_1_lillian_168
    ''
    show date_event_1_lillian_170 with Dissolve(0.3)
    hide date_event_1_lillian_169
    li 9 "别停……就这样……啊……好舒服！" with Dissolve(0.3)
    show date_event_1_lillian_171 with Dissolve(0.3)
    hide date_event_1_lillian_170
    ''
    show date_event_1_lillian_172 with Dissolve(0.3)
    hide date_event_1_lillian_171
    li 9 "天啊……[gg]我不行了……还要更多……" with Dissolve(0.3)
    ''
    show date_event_1_lillian_173 with Dissolve(0.3)
    hide date_event_1_lillian_172
    gg 0 "你快把我逼疯了。" with Dissolve(0.3)
    ''
    show date_event_1_lillian_174 with Dissolve(0.3)
    hide date_event_1_lillian_173
    ''
    
    play sound2 lillian_hotel_110_sound loop
    
    show date_event_1_lillian_175 with Dissolve(0.3)
    hide date_event_1_lillian_174
    li 9 "对……就是这样……再用力……" with Dissolve(0.3)
    ''
    li 9 "啊……千万别停……" with Dissolve(0.3)
    show date_event_1_lillian_176 with Dissolve(0.3)
    hide date_event_1_lillian_175
    li 9 "再多点……求你了……你敢停试试……" with Dissolve(0.3)
    gg 0 "我不会放手的，[li]……" with Dissolve(0.3)
    show date_event_1_lillian_177 with Dissolve(0.3)
    hide date_event_1_lillian_176
    li 9 "别……你最好别……" with Dissolve(0.3)
    ''
    gg 0 "要去了！" with Dissolve(0.3)
    
    stop sound2 fadeout 1
    
    show date_event_1_lillian_178 with Dissolve(0.3)
    hide date_event_1_lillian_177
    
    play sound cumming
    
    $ renpy.pause (3.5, hard=True)
    
    scene black with Dissolve(0.3)
    
    show date_event_1_lillian_179 with Dissolve(1)
    ''
    
    $ de1_lillian_sex_1 = True
    $ persistent.gallery_date_event_1_lillian_sex_1 = True
    
    call screen de1_lillian_sex
    jump date_event_1_lillian_sex_2

label date_event_1_lillian_sex_2:

    scene black with Dissolve(0.5)
    pause 0.5
    
    $ de1_lillian_sex_kiss_lock = True
    $ de1_lillian_sex_lick_lock = True
    
    play sound2 lillian_hotel_109_sound loop
    
    show date_event_1_lillian_180 with Dissolve(0.3)
    ''
    
    play sound2 lillian_hotel_110_sound loop
    
    show date_event_1_lillian_181 with Dissolve(0.3)
    hide date_event_1_lillian_180
    li 9 "对……再多点……再用力……！" with Dissolve(0.3)
    show date_event_1_lillian_182 with Dissolve(0.3)
    hide date_event_1_lillian_181
    gg 0 "这是你自找的……忍住……" with Dissolve(0.3)
    show date_event_1_lillian_183 with Dissolve(0.3)
    hide date_event_1_lillian_182
    li 9 "好！好！" with Dissolve(0.3)
    show date_event_1_lillian_184 with Dissolve(0.3)
    hide date_event_1_lillian_183
    li 9 "唔……啊！求你了……把我撕碎吧！" with Dissolve(0.3)
    show date_event_1_lillian_185 with Dissolve(0.3)
    hide date_event_1_lillian_184
    gg 0 "你快把我逼疯了……再快一点……" with Dissolve(0.3)
    show date_event_1_lillian_186 with Dissolve(0.3)
    hide date_event_1_lillian_185
    ''
    show date_event_1_lillian_187 with Dissolve(0.3)
    hide date_event_1_lillian_186
    li 9 "啊啊……我……我不行了！" with Dissolve(0.3)
    show date_event_1_lillian_188 with Dissolve(0.3)
    hide date_event_1_lillian_187
    ''
    gg 0 "要去了！" with Dissolve(0.3)
    
    stop sound2 fadeout 1
    
    show date_event_1_lillian_189 with Dissolve(0.3)
    hide date_event_1_lillian_188
    
    play sound cumming
    
    $ renpy.pause (3.4, hard=True)
    
    scene black with Dissolve(0.3)
    pause 1
    
    show date_event_1_lillian_190 with Dissolve(0.3)
    $ renpy.pause (7.2, hard=True)
    
    scene black with Dissolve(0.3)
    pause 0.5
    
    show date_event_1_lillian_191 with Dissolve(0.5)
    
    ''
    
    $ de1_lillian_sex_2 = True
    $ persistent.gallery_date_event_1_lillian_sex_2 = True
    
    jump date_event_1_lillian_sex_end

label date_event_1_lillian_sex_end:

    stop music3 fadeout 4
    pause 1
    $ date_event_1_lillian = True
    $ love_li += 5
    show screen rel_up_lillian

    scene black with Dissolve(1.0)
    pause 2
    pause 2

    if date_event_1_may == True:
        jump end_tatsumi
        
    else:
        show date_event_1_intro_18 with Dissolve(1.0)
        jump date_event_1_choice

###### 04 END - TATSUMI

label end_tatsumi:
    
    stop music4 fadeout 1
    stop music fadeout 1
    stop music3 fadeout 1
    
    play music2 post_noir_piano_loop fadein 10
    
    scene end_tatsumi_0 with Dissolve(1.0)
    pause 0.3
    show end_tatsumi_1 with Dissolve(0.1)
    $ renpy.pause (13, hard=True)
    
    show end_tatsumi_2 with Dissolve(0.3)
    hide end_tatsumi_1
    tatsumi 1 "你查到了什么？" with Dissolve(0.3)
    sebas0 0 "他来时无声，去时也无踪。" with Dissolve(0.3)
    tatsumi 1 "一般来说，第一次进入暗界都要经过我们。但这个孩子……" with Dissolve(0.3)
    tatsumi 1 "他好像本来就知道怎么进去。"
    sebas0 0 "那不是偶然。他的每一个行动都是算计好的。" with Dissolve(0.3)
    sebas0 0 "而且，他的力量和其他新人不一样。"
    scene end_tatsumi_3 with Dissolve(0.3)
    tatsumi 1 "有什么特别之处？" with Dissolve(0.3)
    scene end_tatsumi_4 with Dissolve(0.3)
    sebas0 0 "他引发了一场混乱。很有用，但不在计划之内。" with Dissolve(0.3)
    scene end_tatsumi_5 with Dissolve(0.3)
    tatsumi 1 "嗯……你怎么看？" with Dissolve(0.3)
    scene end_tatsumi_6 with Dissolve(0.3)
    sebas0 0 "眼下他还不成气候。但要是我们放任他不管，总有一天他会成为威胁。" with Dissolve(0.3)
    scene end_tatsumi_7 with Dissolve(0.3)
    tatsumi 1 "他要是胆敢挡我们的路……" with Dissolve(0.3)
    scene end_tatsumi_8 with Dissolve(0.3)
    sebas0 0 "我会像碾碎其他人一样碾碎他。" with Dissolve(0.3)
    scene end_tatsumi_9 with Dissolve(0.5)
    pause 0.5
    
    stop music2 fadeout 6
    
    scene end_tatsumi_10 with Dissolve(0.3)
    pause 1.5
    scene black with Dissolve(1.0)
    pause 2
    pause 2
    jump cdr_4