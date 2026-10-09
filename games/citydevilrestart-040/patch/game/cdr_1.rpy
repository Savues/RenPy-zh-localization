label cdr_1:
    stop music2
    $ renpy.music.set_volume(1, delay=0, channel=u'music2')
    scene black
    hide screen girls with dissolve
    $ quick_menu = False
    pause 3.0
    show timetravel_1
    $ renpy.pause(5,hard=True)
    pause 1.0
    scene black
    pause 1.0
    show screen girls with dissolve
    $ quick_menu = True
    gg t0 "（{cps=6}好重……{/cps}）" with dissolve
    gg t0 "（{cps=8}我感觉……有什么在压着我……{/cps}）"
    gg t0 "（{cps=10}我这是怎么了？{/cps}）"
    show awoke_1
    $ renpy.pause(4,hard=True)
    scene awoke_2 with dissolve
    play music2 clouds_above_the_oceanloopable_by_chilledmusic fadein 20 volume 0.6
    gg 0 "[may]，你在干什么？"  with dissolve
    scene awoke_3 with dissolve
    may 6 "[gg]……" with dissolve
    scene awoke_4 with dissolve
    may 6 "你终于醒了！" with dissolve
    scene awoke_5 with dissolve
    may 6 "你昏倒在浴室里……我……我吓死了！" with dissolve
    may 6 "我把你拖到这儿，你就像睡着了一样……有一瞬间我甚至想……你该不会再也醒不过来了吧？"
    scene awoke_6 with fade
    may 6 "躺着好好休息，敢乱动我就生气！我去给你拿衣服。" with dissolve
    gg 0 "姐姐。" with dissolve
    scene awoke_7 with dissolve
    may 6 "嗯？" with dissolve
    gg 0 "我昏迷了多久？" with dissolve
    scene awoke_8 with dissolve
    may 6 "从傍晚开始吧。你在浴室里待太久了。" with dissolve
    may 6 "所以我就过去看看你没事吧……"
    scene awoke_9 with dissolve
    may 6 "我敲了门！" with dissolve
    scene awoke_10 with dissolve
    may 6 "但你没应……我以为可能是水声太大你听不见……" with dissolve
    scene awoke_11 with dissolve
    may 6 "我一直敲，一直都没人应。" with dissolve
    scene awoke_12 with dissolve
    may 6 "然后我就把门推开一条缝，想让你听见我……可是……" with dissolve
    scene awoke_13 with dissolve
    may 6 "你躺在浴室的地板上，我当时就慌了。" with dissolve
    scene awoke_14 with dissolve
    may 6 "事情就是这样……" with dissolve
    may 6 "{cps=5}……{/cps}"
    gg 0 "你没叫救护车？" with dissolve

    scene awoke_8 with dissolve
    may 6 "我……没有……看到你的那一瞬间，我整个人都糊了……我都不记得自己是怎么把你拖到这里的……" with dissolve
    may 6 "我真是个笨蛋……应该叫救护车的……"
    scene awoke_14 with dissolve
    gg 0 "[may]，没事。我现在感觉挺好，可能是用力过猛了。" with dissolve
    may 6 "……好吧。但还是不许起来！" with dissolve

    scene awoke_15 with dissolve
    may 6 "我去给你拿衣服。" with dissolve
    scene awoke_16 with dissolve
    gg 0 "（我为什么会突然昏过去？）" with dissolve
    gg 0 "{cps=5}……{/cps}"
    scene awoke_17 with fade
    $ renpy.music.set_volume(0.3, delay=3, channel=u'music2')
    pause 0.3
    scene awoke_17_1 with dissolve
    gg 0 "（我记得被黑暗包围……还有一个女孩……[asami]？）" with dissolve
    gg 0 "（这次的梦实在太逼真了。）"
    gg 0 "（一切都太真实了，我发誓那真的发生过。）"
    gg 0 "（我现在甚至还能感觉到……头部中枪的疼痛。）"
    gg 0 "（而且我从没见过那样的女孩。）"
    gg 0 "（我记得那女孩长什么样。她对我说的话、给我看的东西、她的举止……）"
    gg 0 "（连名字都记得。[asami]。这种梦根本不可能是自己编出来的。）"
    $ renpy.music.set_volume(1, delay=5, channel=u'music2')
    scene awoke_16 with fade
    gg 0 "（梦是在她开枪打中我的时候结束的。）" with dissolve
    gg 0 "（不过，这些奇怪的梦里，总有某些东西是一致的。）"
    scene awoke_18 with dissolve
    ''
    play sound pat_cloth_1
    scene awoke_19 with dissolve
    ''
    scene awoke_20 with dissolve
    may 6 "请穿好衣服。" with dissolve
    may 6 "我先出去一下。"
    play sound pat_cloth_2
    scene awoke_21 with dissolve
    gg 0 "诶？" with dissolve
    gg t0 "（内裤？）"
    scene awoke_22 with dissolve
    gg 0 "（靠，对哦。我在洗澡来着。）" with dissolve
    
##Uncle Kazama, call, debt

    stop music2 fadeout 3
    play music3 call_start
    scene awoke_23 with Dissolve(0.1)
    "来电。" with dissolve
    scene awoke_24 with Dissolve(0.1)
    gg 0 "（叔叔？）" with dissolve
    stop music3
    scene awoke_25 with Dissolve(0.3)
    gg 0 "喂，[ka]。" with dissolve
    scene awoke_26 with Dissolve(0.3)
    ka 2 "您还好吗？[may]怎么样？" with dissolve
    scene awoke_25 with Dissolve(0.3)
    gg 0 "还不错。就是有点累，不过事情应该会慢慢好起来的。你们和你阿姨呢？" with dissolve
    scene awoke_26 with Dissolve(0.3)
    play music2 dark_secrets_decision_by_sascha_ende fadein 5 volume 0.3
    ka 2 "啊，我倒想跟你聊聊，不过那些以后再说吧。" with dissolve
    ka 2 "[gg]，孩子，有个坏消息要告诉你。"
    ka 2 "我不想一上来就给你添堵，但我和燕商量了一下，觉得你该知道。"
    scene awoke_25 with Dissolve(0.3)
    gg 0 "出什么事了？" with dissolve
    scene awoke_26 with Dissolve(0.3)
    ka 2 "你父亲……他欠了别人一笔债。我本想自己处理，却遇到了麻烦。" with dissolve
    scene awoke_27 with Dissolve(0.3)
    gg 0 "什么？！什么债？！" with dissolve
    scene awoke_28 with Dissolve(0.3)
    ka 2 "抱歉现在才告诉你。但事情似乎一天比一天复杂。" with dissolve
    scene awoke_27 with Dissolve(0.3)
    gg 0 "那……他欠的是谁？欠多少？" with dissolve
    scene awoke_28 with Dissolve(0.3)
    ka 2 "那是个非常危险的人，[gg]。" with dissolve
    ka 2 "目前这笔债是六万美元。"
    scene awoke_29 with Dissolve(0.3)
    gg 0 "六万美元？！这他妈太扯了！" with dissolve
    gg 0 "我父亲怎么会落到这种地步？"
    scene awoke_30 with Dissolve(0.3)
    ka 2 "具体细节我也不清楚。现在只能告诉你这些。" with dissolve
    scene awoke_29 with Dissolve(0.3)
    gg 0 "那我该怎么办？" with dissolve
    scene awoke_30 with Dissolve(0.3)
    ka 2 "你得想办法把这笔债还上。我知道这非常难。" with dissolve
    ka 2 "我和燕会尽一切努力，但恐怕能帮的有限。"
    scene awoke_29 with Dissolve(0.3)
    gg 0 "这个人……他知道我们住哪儿吗？" with dissolve
    scene awoke_30 with Dissolve(0.3)
    ka 2 "恐怕知道。而且[may]是他的亲女儿，他们肯定会先冲她下手。" with dissolve
    gg 0 "（真他妈倒霉。）" with dissolve
    scene awoke_29 with dissolve
    gg 0 "我不会让那种事发生。"
    scene awoke_30 with dissolve
    ka 2 "当然不会。但孩子，无论如何请一定要小心。你们的命最重要。" with dissolve
    ka 2 "必要的话，也许你们该考虑把公寓卖掉。"
    gg 0 "{cps=5}……{/cps}" with dissolve
    ka 2 "抱歉用这种消息给你打电话，但总比……从那个人嘴里听到要好。" with dissolve
    ka 2 "过几天我再联系你。"
    scene awoke_31 with dissolve
    gg 0 "好。到时候再聊。"
    
    scene awoke_32 with dissolve
    gg 0 "{cps=5}……{/cps}" with dissolve
    stop music2 fadeout 5
    gg 0 "（真是他妈绝了。）"
    scene black with Dissolve(1.5)
    pause 2.0
    
##School day 2
label school_corrior_dolg:
    play music3 city_bird volume 0.6
    show school_corrior_dolg_1 with dissolve
    $ renpy.pause(3, hard=True)
    pause 1.0
    gg 3 "于是我们的第二天校园生活开始了。" with dissolve
    play music2 sweet_benjamin_tissot fadein 5 volume 0.5
    stop music3 fadeout 5
    scene school_corrior_dolg_2 with Dissolve(0.3)
    gg 3 "感觉怎么样，[may]？" with dissolve
    scene school_corrior_dolg_3 with Dissolve(0.3)
    may 7 "比昨天好多了。第一天虽然挺吓人的，但我跟几个女生聊过天！希望我们能成为朋友！" with dissolve

    scene school_corrior_dolg_33 with Dissolve(0.3)
    gg 3 "我从来没怀疑过。你总是能给人惊喜。" with dissolve
    scene school_corrior_dolg_23 with Dissolve(0.3)
    may 7 "哈哈。干嘛这么说？" with dissolve
    scene school_corrior_dolg_9 with Dissolve(0.3)
    gg 3 "你刚才一把把我从浴室拖到卧室，力气从哪儿来的？" with dissolve
    scene school_corrior_dolg_10 with Dissolve(0.3)
    may 7 "哦那个。说实话我也不知道怎么回事。看到你躺在那儿，我就抓着你的胳膊一使劲，直接把你拽起来了。" with dissolve
    
    scene school_corrior_dolg_4 with Dissolve(0.3)
    may 7 "今天有什么安排吗？" with dissolve
    may 7 "我还想问你打算去找书包呢。"
    show school_corrior_dolg_5 with Dissolve(0.3)
    gg 3 "嗯，昨天落在教室了。大概还在那儿。" with dissolve
    scene school_corrior_dolg_6 with Dissolve(0.3)
    may 7 "对了，昨天我和几个女生在聊这所学校的历史。" with dissolve
    scene school_corrior_dolg_7 with Dissolve(0.3)
    may 7 "结果发现这学校挺老的，而且曾经荒废过一段时间。" with dissolve
    may 7 "大约两年前，有个商人买下来重新翻修了。"
    scene school_corrior_dolg_8 with Dissolve(0.3)
    may 7 "挺有意思的吧？"

    menu:
        '[gr]「挺有意思的。」':
            scene school_corrior_dolg_5 with Dissolve(0.3)
            gg 3 "还真挺有意思。" with dissolve
            gg 3 "还好有人接手了这所学校。能让它重新开起来真是太好了。"
            gg 3 "（[ken]之前提过[ry]的父亲。她说的应该就是那个人。）"
            
            scene school_corrior_dolg_9 with Dissolve(0.3)
            may 7 "*窃笑*" with dissolve
            scene school_corrior_dolg_10 with Dissolve(0.3)
            may 7 "对了。" with dissolve
            
        '「我不太在意。」':
        
            show school_corrior_dolg_5 with Dissolve(0.3)
            gg 3 "说真的，这些我不太关心。" with dissolve

            scene school_corrior_dolg_11 with Dissolve(0.3)
            may 7 "哎呀，知道自己学校的历史不是挺有意思的吗！" with dissolve
            scene school_corrior_dolg_12 with Dissolve(0.3)
            may 7 "{cps=5}……{/cps}" with dissolve

    scene school_corrior_dolg_3 with Dissolve(0.3)
    may 7 "我想我们可以参加个学校社团。你觉得呢？" with dissolve

    menu:
        '[gr]「什么社团？」':
            show school_corrior_dolg_5 with Dissolve(0.3)
            gg 3 "你想参加什么社团？" with dissolve
            scene school_corrior_dolg_6 with Dissolve(0.3)
            may 7 "老实说我还没想好。需要再想想。" with dissolve
            
            menu:
                "建议她参加烹饪社\\n[gold](芽衣 +3)[gr](推荐)":
                    show school_corrior_dolg_5 with Dissolve(0.3)
                    gg 3 "我觉得你很适合烹饪社。" with dissolve
                    gg 3 "你做饭那么好吃，去了肯定是最耀眼的那个。我还想多吃你做的菜呢。"

                    scene school_corrior_dolg_13 with Dissolve(0.3)
                    show screen rel_up_may
                    $ love_may += 3
                    may 7 "谢谢你夸奖，[gg]！我好开心。" with dissolve
                    scene school_corrior_dolg_14 with Dissolve(0.3)
                    may 7 "我一直都喜欢做菜，也喜欢研究新菜谱。" with dissolve
                    scene school_corrior_dolg_15 with Dissolve(0.3)
                    may 7 "那我还真可以考虑一下烹饪社。" with dissolve
                    scene school_corrior_dolg_16 with Dissolve(0.3)
                    may 7 "既能展示我的手艺，也能跟别人学习！" with dissolve
                    
                    menu:
                        "支持她\\n[gold](芽衣 +3)[gr](推荐)":
                            scene school_corrior_dolg_17 with Dissolve(0.3)
                            gg 3 "你一聊到做菜，眼睛就发光。" with dissolve
                            scene school_corrior_dolg_18 with Dissolve(0.3)
                            gg 3 "你肯定是最棒的！你的天赋会让所有人都刮目相看。" with dissolve
                            show screen rel_up_may
                            $ love_may += 3
                            scene school_corrior_dolg_19 with Dissolve(0.3)
                            may 7 "我觉得你可以参加运动社团，或者试试有创意的活动。" with dissolve
                            may 7 "你很强，什么都做得到。"
                            
                            menu:
                                "「也可以考虑舞蹈社。」\\n[gold](芽衣 +1)[gr](推荐)":
                                    show school_corrior_dolg_34 with Dissolve(0.3)
                                    gg 3 "也可以考虑舞蹈社。" with dissolve
                                    gg 3 "我经常看你看舞蹈视频。"
                                    
                                    scene school_corrior_dolg_35 with Dissolve(0.3)
                                    show screen rel_up_may
                                    may 7 "啊啊啊不行，我跳不了那种。被看着我会害羞。" with dissolve
                                    $ love_may += 1
                                    
                                    menu:
                                        "支持她\\n[gold](芽衣 +5)[gr](推荐)":
                                            scene school_corrior_dolg_25 with Dissolve(0.3)
                                            gg 3 "别害羞，[may]。" with dissolve
                                            scene school_corrior_dolg_26 with Dissolve(0.3)
                                            gg 3 "我仿佛能看到你随着音乐起舞的样子——一定很迷人。" with dissolve
                                            scene school_corrior_dolg_27 with Dissolve(0.3)
                                            gg 3 "想想你跳出那些优雅的动作。身材这么好！" with dissolve
                                            
                                            scene school_corrior_dolg_28 with Dissolve(0.3)
                                            show screen rel_up_may
                                            may 7 "你真会说话，[gg]。那我……再想想吧。" with dissolve
                                            $ love_may += 5
                                            scene school_corrior_dolg_30 with Dissolve(0.3)
                                            may 7 "你的胳膊好有力……" with dissolve
                                            scene school_corrior_dolg_31 with Dissolve(0.3)
                                            gg 3 "我也会摸摸你，不过是在家里。" with dissolve
                                            scene school_corrior_dolg_32 with Dissolve(0.3)
                                            may 7 "嘿嘿。那就不必了。" with dissolve
                                            scene black with Dissolve(0.6)
                                            pause 0.1
                                            
                                        "什么都不做":
                                            pause 0.3
                                            scene black with Dissolve(0.6)
                                            pause 0.1
                                            
                                "什么都不做":
                                    pause 0.3
                                    scene black with Dissolve(0.6)
                                    pause 0.1
                        
                        "「也可以考虑舞蹈社。」\\n[gold](芽衣 +1)[gr](推荐)":
                            show school_corrior_dolg_5 with Dissolve(0.3)
                            gg 3 "也可以考虑舞蹈社。" with dissolve
                            gg 3 "我经常看你看舞蹈视频。"
                            
                            scene school_corrior_dolg_24 with Dissolve(0.3)
                            show screen rel_up_may
                            may 7 "啊啊啊不行，我跳不了那种。被看着我会害羞。" with dissolve
                            $ love_may += 1
                            
                            menu:
                                "支持她\\n[gold](芽衣 +3)[gr](推荐)":
                                    scene school_corrior_dolg_25 with Dissolve(0.3)
                                    gg 3 "别害羞，[may]。" with dissolve
                                    scene school_corrior_dolg_26 with Dissolve(0.3)
                                    gg 3 "我仿佛能看到你随着音乐起舞的样子——一定很迷人。" with dissolve
                                    scene school_corrior_dolg_27 with Dissolve(0.3)
                                    gg 3 "想想你跳出那些优雅的动作。身材这么好！" with dissolve
                                    
                                    scene school_corrior_dolg_28 with Dissolve(0.3)
                                    show screen rel_up_may
                                    may 7 "你真会说话，[gg]。那我……再想想吧。" with dissolve
                                    $ love_may += 5
                                    scene school_corrior_dolg_29 with Dissolve(0.3)
                                    may 7 "我觉得你可以参加运动社团，或者试试有创意的活动。" with dissolve
                                    may 7 "你很强，什么都做得到。"
                                    scene black with Dissolve(0.6)
                                    pause 0.1
                                    
                                "什么都不做":
                                    pause 0.5
                                    scene school_corrior_dolg_23 with Dissolve(0.3)
                                    may 7 "我觉得你可以参加运动社团，或者试试有创意的活动。" with dissolve
                                    may 7 "你很强，什么都做得到。"
                        
                        "什么都不做":
                            pause 0.3
                            scene school_corrior_dolg_23 with Dissolve(0.3)
                            may 7 "我觉得你可以参加运动社团，或者试试有创意的活动。" with dissolve
                            may 7 "你很强，什么都做得到。"
                
                "建议她参加舞蹈社\\n[gold](芽衣 +1)[gr](推荐)":
                    show school_corrior_dolg_5 with Dissolve(0.3)
                    gg 3 "认真考虑一下参加舞蹈社吧。" with dissolve
                    gg 3 "我经常看你看舞蹈视频。"
                    
                    scene school_corrior_dolg_24 with Dissolve(0.3)
                    show screen rel_up_may
                    may 7 "啊啊啊不行，我跳不了那种。被看着我会害羞。" with dissolve
                    $ love_may += 1
                    
                    menu:
                        "支持她\\n[gold](芽衣 +5)[gr](推荐)":
                            scene school_corrior_dolg_25 with Dissolve(0.3)
                            gg 3 "别害羞，[may]。" with dissolve
                            scene school_corrior_dolg_26 with Dissolve(0.3)
                            gg 3 "我仿佛能看到你随着音乐起舞的样子——一定很迷人。" with dissolve
                            scene school_corrior_dolg_27 with Dissolve(0.3)
                            gg 3 "想想你跳出那些优雅的动作。身材这么好！" with dissolve
                            
                            scene school_corrior_dolg_28 with Dissolve(0.3)
                            show screen rel_up_may
                            may 7 "你真会说话，[gg]。那我……再想想吧。" with dissolve
                            $ love_may += 5
                            scene school_corrior_dolg_29 with Dissolve(0.3)
                            may 7 "我觉得你可以参加运动社团，或者试试有创意的活动。" with dissolve
                            may 7 "你很强，什么都做得到。"
                            
                            menu:
                                '「你也可以参加烹饪社。」\\n[gold](芽衣 +3)[gr](推荐)':
                                    show school_corrior_dolg_37 with Dissolve(0.3)
                                    gg 3 "我觉得你很适合烹饪社。" with dissolve
                                    gg 3 "你做饭那么好吃，去了肯定是最耀眼的那个。我还想多吃你做的菜呢。"

                                    scene school_corrior_dolg_38 with Dissolve(0.3)
                                    show screen rel_up_may
                                    $ love_may += 3
                                    may 7 "谢谢你夸奖，[gg]！我好开心。" with dissolve
                                    scene school_corrior_dolg_39 with Dissolve(0.3)
                                    may 7 "我一直都喜欢做菜，也喜欢研究新菜谱。" with dissolve
                                    scene school_corrior_dolg_40 with Dissolve(0.3)
                                    may 7 "那我还真可以考虑一下烹饪社。" with dissolve
                                    scene school_corrior_dolg_41 with Dissolve(0.3)
                                    may 7 "既能展示我的手艺，也能跟别人学习！" with dissolve
                                    
                                    menu:
                                        "支持她\\n[gold](芽衣 +3)[gr](推荐)":
                                            scene school_corrior_dolg_17 with Dissolve(0.3)
                                            gg 3 "你一聊到做菜，眼睛就发光。" with dissolve
                                            scene school_corrior_dolg_18 with Dissolve(0.3)
                                            gg 3 "你肯定是最棒的！你的天赋会让所有人都刮目相看。" with dissolve
                                            $ love_may += 3
                                            show screen rel_up_may
                                            scene school_corrior_dolg_20 with Dissolve(0.3)
                                            may 7 "你的胳膊好有力……" with dissolve
                                            scene school_corrior_dolg_21 with Dissolve(0.3)
                                            gg 3 "我也会摸摸你，不过是在家里。" with dissolve
                                            scene school_corrior_dolg_22 with Dissolve(0.3)
                                            may 7 "嘿嘿。那就不必了。" with dissolve
                                            scene black with Dissolve(0.6)
                                            pause 0.1
                                        
                                        "什么都不做":
                                            pause 0.3
                                            scene black with Dissolve(0.6)
                                            pause 0.1
                                            
                                "什么都不做":
                                    pause 0.3
                                    scene black with Dissolve(0.6)
                                    pause 0.1
                            
                        "建议她参加烹饪社\\n[gold](芽衣 +3)[gr](推荐)":
                            show school_corrior_dolg_5 with Dissolve(0.3)
                            gg 3 "我觉得你很适合烹饪社。" with dissolve
                            gg 3 "你做饭那么好吃，去了肯定是最耀眼的那个。我还想多吃你做的菜呢。"

                            scene school_corrior_dolg_13 with Dissolve(0.3)
                            may 7 "谢谢你夸奖，[gg]！我好开心。" with dissolve
                            scene school_corrior_dolg_14 with Dissolve(0.3)
                            may 7 "我一直都喜欢做菜，也喜欢研究新菜谱。" with dissolve
                            scene school_corrior_dolg_15 with Dissolve(0.3)
                            may 7 "那我还真可以考虑一下烹饪社。" with dissolve
                            scene school_corrior_dolg_16 with Dissolve(0.3)
                            may 7 "既能展示我的手艺，也能跟别人学习！" with dissolve
                            $ love_may += 3
                            
                            menu:
                                "支持她\\n[gold](芽衣 +3)[gr](推荐)":
                                    scene school_corrior_dolg_17 with Dissolve(0.3)
                                    gg 3 "你一聊到做菜，眼睛就发光。" with dissolve
                                    scene school_corrior_dolg_18 with Dissolve(0.3)
                                    gg 3 "你肯定是最棒的！你的天赋会让所有人都刮目相看。" with dissolve
                                    $ love_may += 3
                                    scene school_corrior_dolg_19 with Dissolve(0.3)
                                    may 7 "我觉得你可以参加运动社团，或者试试有创意的活动。" with dissolve
                                    may 7 "你很强，什么都做得到。"
                                    scene black with Dissolve(0.6)
                                    pause 0.1
                                    
                                "什么都不做":
                                    pause 0.3
                                    scene school_corrior_dolg_23 with Dissolve(0.3)
                                    may 7 "我觉得你可以参加运动社团，或者试试有创意的活动。" with dissolve
                                    may 7 "你很强，什么都做得到。"
                        
                        "什么都不做":
                            pause 0.5
                            scene school_corrior_dolg_23 with Dissolve(0.3)
                            may 7 "我觉得你可以参加运动社团，或者试试有创意的活动。" with dissolve
                            may 7 "你很强，什么都做得到。"
                    
                "「再多想想」":
                    show school_corrior_dolg_5 with Dissolve(0.3)
                    gg 3 "再多想想吧。等你决定参加哪个社团再说。" with dissolve
                    scene school_corrior_dolg_33 with Dissolve(0.3)
                    may 7 "好吧。" with dissolve
                        
        '「我不感兴趣。」':
            gg 3 "老实说，我不感兴趣。" with dissolve
            
    show school_corrior_dolg_5 with Dissolve(0.3)
    stop music2 fadeout 15
    play music3 city_bird fadein 8 volume 0.3
    gg 3 "[may]，有件事我得告诉你。" with dissolve
    scene school_corrior_dolg_42 with Dissolve(0.3)
    may 7 "怎么了，[gg]？你看起来很严肃。" with dissolve
    show school_corrior_dolg_44 with Dissolve(0.3)
    gg 3 "[ka]最近给我打了电话。" with dissolve
    gg 3 "他说我们父亲欠了别人的钱，现在这笔债落到我们头上了。"
    scene school_corrior_dolg_43 with Dissolve(0.3)
    may 7 "欠债？爸爸跟别人借了钱？" with dissolve
    may 7 "怎么会这样？太奇怪了，我们家以前好像什么都不缺……"
    show school_corrior_dolg_44 with Dissolve(0.3)
    gg 3 "嗯，我自己都难以相信。" with dissolve
    gg 3 "总之叔叔提醒我们了，说那是个非常危险的人。"
    gg 3 "事情肯定很严重——他甚至建议把父亲的公寓卖掉。"
    scene school_corrior_dolg_45 with Dissolve(0.3)
    may 7 "难以置信……爸爸怎么会欠下这种债？" with dissolve
    may 7 "那他又是怎么认识这个「危险人物」的？"
    show school_corrior_dolg_46 with Dissolve(0.3)
    gg 3 "叔叔没细说，但我觉得这跟父亲的死有关。" with dissolve
    gg 3 "（虽然我很不想承认，但[ka]可能也牵涉其中。）"
    gg 3 "（也许父亲成了他们的棋子，现在得由我来收拾这个烂摊子了。）"
    scene school_corrior_dolg_47 with Dissolve(0.3)
    may 7 "听起来好惨……我们到底欠多少？" with dissolve
    show school_corrior_dolg_44 with Dissolve(0.3)
    gg 3 "六万美元。" with dissolve
    may 7 "{cps=5}……{/cps}" with dissolve
    scene school_corrior_dolg_48 with Dissolve(0.3)
    may 7 "怎么会这么多……" with dissolve
    show school_corrior_dolg_46 with Dissolve(0.3)
    may 7 "{cps=5}……{/cps}" with dissolve
    scene school_corrior_dolg_50 with Dissolve(0.3)
    may 7 "要不要把公寓卖掉？" with dissolve
    show school_corrior_dolg_44 with Dissolve(0.3)
    gg 3 "绝对不行，公寓不能卖。还有，谁来都别开门。" with dissolve
    gg 3 "如果不是我们，也不认识的人——立刻报警，明白吗？"
    scene school_corrior_dolg_45 with Dissolve(0.3)
    may 7 "明白了……" with dissolve
    scene school_corrior_dolg_23 with Dissolve(0.3)
    may 7 "我们会一起撑过去的，[gg]。去找工作吧。记住，我永远会帮你！" with dissolve
    show school_corrior_dolg_5 with Dissolve(0.3)
    gg 3 "谢了，妹。" with dissolve
    gg 3 "好了[may]，快上课了。"
    gg 3 "开学头几天可不能迟到。"
    scene school_corrior_dolg_51 with Dissolve(0.3)
    may 7 "嗯，你说得对。加油！" with dissolve
    scene school_corrior_dolg_52 with Dissolve(0.3)
    gg 3 "放学见。" with dissolve
    scene school_corrior_dolg_53 with Dissolve(0.3)
    may 7 "路上小心！" with dissolve
    
    scene school_corrior_dolg_49 with dissolve
    gg 3 "{cps=5}……{/cps}" with dissolve
    ken 3 "嘿，[gg]！怎么样？" with dissolve
    show school_corrior_dolg_54
    $ renpy.pause(1, hard=True)
    pause
    scene school_corrior_dolg_55 with dissolve
    gg 3 "还不错。你昨天之后呢？" with dissolve
    scene school_corrior_dolg_56 with Dissolve(0.3)
    ken 3 "我很好啊，恢复得跟狗一样快。" with dissolve
    scene school_corrior_dolg_57 with Dissolve(0.3)
    ken 3 "我刚才看到你跟[may]在一起。" with dissolve
    scene school_corrior_dolg_58 with Dissolve(0.3)
    ken 3 "你们俩看起来都有点累。" with dissolve
    ken 3 "没事吧？"
    scene school_corrior_dolg_55 with Dissolve(0.3)
    gg 3 "只是在处理搬家的事。没什么特别的。" with dissolve
    scene school_corrior_dolg_59 with Dissolve(0.3)
    ken 3 "有什么需要帮忙的尽管说。" with dissolve
    scene school_corrior_dolg_60 with Dissolve(0.3)
    gg 3 "你的眼睛怎么样？不疼吗？" with dissolve
    scene school_corrior_dolg_61 with Dissolve(0.3)
    ken 3 "啊，那个……完全没……" with dissolve
    scene school_corrior_dolg_62 with Dissolve(0.3)
    ken 3 "{cps=5}……{/cps}" with dissolve
    play sound as1 volume 0.8
    scene school_corrior_dolg_63 with Dissolve(0.1)
    ''
    play sound zahvat_2 volume 0.6
    scene school_corrior_dolg_64 with vpunch
    ''
    scene school_corrior_dolg_65 with Dissolve(0.1)
    pause 0.1
    show school_corrior_dolg_66
    $ renpy.pause(1.96, hard=True)
    stop music3 fadeout 1
    scene black
    pause 2.0
    show school_corrior_dolg_67 with Dissolve(0.8)
    play music2 missing_loopable_by_dave_deville fadein 6 volume 0.6
    pause 0.5
    play sound2 heart_bass fadein 2 volume 3
    gg 3 "（什么情况？）" with dissolve
    da 1 "哎哟，肿脸哥，感觉怎么样？" with dissolve
    scene black with Dissolve(0.5)
    pause 0.5
    gg 3 "（他妈河豚。）" with dissolve
    stop sound2 fadeout 6
    show school_corrior_dolg_68 with Dissolve(0.5)
    $ renpy.pause(4.6, hard=True)
    show school_corrior_dolg_69 with Dissolve(0.1)
    hide school_corrior_dolg_68
    gg 3 "（我觉得自己撞到头了。）" with dissolve
    gg 3 "（可奇怪，一点都不疼。）"
    gg 3 "（有种奇怪的感觉……）"
    gg 3 "（我浑身都是劲。）"
    gg 3 "（为什么所有人都像被定住了？）"
    scene black with dissolve
    pause 0.4
    show school_corrior_dolg_70 with Dissolve(0.3)
    $ renpy.pause(28, hard=True)
    stop music2 fadeout 10
    play music3 city_bird fadein 8 volume 0.3
    $ renpy.pause(4, hard=True)
    gg 3 "（这点程度应该死不了。）" with dissolve
    gg 3 "（但这股力量在手，好像一切都变得很简单。）"
    scene school_corrior_dolg_71 with Dissolve(0.3)
    pause 1.0
    gg 3 "（周围的一切都重新活了过来。）" with dissolve
    scene school_corrior_dolg_72 with Dissolve(0.3)
    gg 3 "（看来刚才让时间静止的是我。）" with dissolve
    scene school_corrior_dolg_73 with Dissolve(0.3)
    da 1 "...!" with vpunch
    scene school_corrior_dolg_74 with Dissolve(0.3)
    da 1 "{cps=5}……{/cps}" with dissolve
    scene school_corrior_dolg_75 with Dissolve(0.1)
    bully1 1 "[da]？！"
    mob 1 "他怎么起来这么快？！"
    play sound zahvat_1 volume 0.6
    stop music3 fadeout 3
    play music2 the_show_must_be_go_by_kevin_macleod fadein 0 volume 0.6
    scene school_corrior_dolg_76 with hpunch
    gg 3 "{cps=66}现在被我逮到了，再说一遍刚才的话？！{/cps}"
    scene school_corrior_dolg_77 with Dissolve(0.1)
    da 2 "...!"
    scene school_corrior_dolg_78 with vpunch
    gg 3 "[ken]！"
    play sound woosh1 volume 0.6
    scene school_corrior_dolg_79 with Dissolve(0.1)
    gg 3 "{cps=66}过来揍他。{/cps}" with dissolve
    play sound woosh2 volume 0.6
    scene school_corrior_dolg_80 with PushMove(0.1, 'pushright')
    ken 3 "诶？"
    play sound woosh3 volume 0.6
    scene school_corrior_dolg_81 with PushMove(0.1, 'pushleft')
    da 2 "{cps=66}[ken]，你他妈敢动手试试！我打爆你的屁股！{/cps}"
    play sound woosh2 volume 0.6
    scene school_corrior_dolg_79 with vpunch
    gg 3 "{cps=66}别理他吠。动手啊，使劲打！{/cps}"
    play sound woosh3 volume 0.6
    scene school_corrior_dolg_80 with PushMove(0.1, 'pushright')
    ken 3 "{cps=66}这样我们会惹上大麻烦的，老兄。{/cps}"
    play sound woosh2 volume 0.6
    scene school_corrior_dolg_79 with PushMove(0.1, 'pushleft')
    gg 3 "{cps=66}他们欺负所有人也不是一天两天了！是时候反击了！{/cps}"
    play sound woosh3 volume 0.6
    scene school_corrior_dolg_80 with PushMove(0.1, 'pushright')
    ken 3 "可是……"
    play sound woosh2 volume 0.6
    scene school_corrior_dolg_78 with hpunch
    gg 3 "{cps=66}你还在等什么？！别浪费这个机会。{/cps}"
    play sound woosh3 volume 0.6
    scene school_corrior_dolg_82 with PushMove(0.1, 'pushright')
    ken 3 "{cps=66}明白。{/cps}"
    scene school_corrior_dolg_83 with vpunch
    ken 3 "{cps=66}你说得对。这种机会哪还有第二次？{/cps}"
    play sound woosh2 volume 0.6
    scene school_corrior_dolg_81 with vpunch
    da 2 "{cps=66}住手！{/cps}"
    scene school_corrior_dolg_84:
        xalign 0.5 yalign 0.5
        zoom 0.8
        ease 4.0 zoom 1.0
    pause 1.0
    play sound punch
    scene school_corrior_dolg_85 with hpunch:
        xalign 0.5 yalign 0.5
        zoom 1.0
        linear 4.0 zoom 0.8
    pause 1.5
    play sound as1 volume 0.8
    scene school_corrior_dolg_86 with Dissolve(0.1):
        xalign 0.5 yalign 0.5
        zoom 1.1
        linear 2.8 zoom 1.0
    pause 2.0
    play sound body_fell volume 1
    scene school_corrior_dolg_87 with vpunch
    pause 1.0
    ken 3 "哈哈……[gg]，我们完蛋了，但靠，从没这么爽过！" with dissolve
    scene school_corrior_dolg_88 with Dissolve(0.1)
    ''
    scene school_corrior_dolg_89 with Dissolve(0.1)
    gg 3 "「我们」？" with dissolve
    gg 3 "我没打他。"
    gg 3 "你下一个任务，就是没有我的帮助再做到一次。做好准备吧！"
    play sound as2 volume 0.8
    scene school_corrior_dolg_90 with vpunch:
        xalign 0.5 yalign 0.5
        zoom 1.1
        linear 4.0 zoom 1.0
    ken 3 "...!"
    scene school_corrior_dolg_91 with Dissolve(0.1)
    gg 3 "希望你记住了这次的教训。" with dissolve
    stop music2 fadeout 6
    play music3 city_bird fadein 8 volume 0.3
    scene school_corrior_dolg_92 with Dissolve(0.3)
    gg 3 "（也许我做得有点过，但这清醒感，还有这力量……）" with dissolve
    gg 3 "（我得弄清楚我的身体到底怎么了。）"
    gg 3 "（不过折腾完这一通，我彻底累垮了。）"
    mob 1 "老师来了！"
    scene school_corrior_dolg_93 with dissolve
    pause 1.0
    scene school_corrior_dolg_94 with dissolve
    mi 1 "[gg]！" with dissolve
    scene school_corrior_dolg_95 with Dissolve(0.1)
    mi 1 "跟我来。" with dissolve
    scene black with Dissolve(1.3)
    play sound schooldoor
    pause 2.0
    stop music3 fadeout 6
    
## Minami, debt, school fight
label school_dolg_minami:
    
    play music2 timeslip_by_phat_sounds volume 0.6 fadein 3
    scene school_dolg_minami_1 with dissolve
    pause 0.3
    mi 1 "[gg]，你居然在走廊里闹事，想什么呢！？" with dissolve
    mi 1 "你知道学校禁止打架吧！"
    scene school_dolg_minami_2 with Dissolve(0.1)
    mi 1 "这种行为绝对不能容忍。" with dissolve
    scene school_dolg_minami_3 with Dissolve(0.3)
    gg 3 "我明白。但你也知道[da]。" with dissolve
    scene school_dolg_minami_4 with Dissolve(0.1)
    gg 3 "他根本不尊重你，还在学校里欺负学生。" with dissolve
    scene school_dolg_minami_5 with Dissolve(0.3)
    gg 3 "我不得不给他点颜色看看。" with dissolve
    scene school_dolg_minami_6 with Dissolve(0.1)
    mi 1 "这很严重，[gg]。" with dissolve
    mi 1 "你刚转来，显然也不是那种惹事的人。"
    scene school_dolg_minami_7 with Dissolve(0.3)
    mi 1 "我们不该以暴制暴。不然就等于承认那些施暴者是对的！" with dissolve
    show school_dolg_minami_8 with Dissolve(0.3)
    pause 0.3
    play sound woosh2 volume 0.3
    show school_dolg_minami_8 with Dissolve(0.1):
        top
        zoom 1
        ease 0.3 zoom 1.1
    mi 1 "而且……别人可能已经注意到你的异常了。" with dissolve
    scene school_dolg_minami_9 with Dissolve(0.1)
    gg 3 "什么意思？" with dissolve
    scene school_dolg_minami_2 with Dissolve(0.1)
    mi 1 "[gg]，我不知道你是怎么卷进这些事的，但在这种小打小闹里炫耀你的能力，极其不智。" with dissolve
    scene school_dolg_minami_3 with Dissolve(0.3)
    gg 3 "{cps=5}……{/cps}"
    play sound woosh3 volume 0.3
    show school_dolg_minami_13 with Dissolve(0.2):
        zoom 0.8 xalign 0.5 yalign 0.5
        easein 0.2 zoom 1.0
    mi 1 "你拥有的力量，其危险之处你自己都还没明白。" with dissolve
    scene school_dolg_minami_14 with Dissolve(0.3)
    mi 1 "怎么不说话？装作听不懂发生了什么？现在已经晚了吧。" with dissolve
    scene school_dolg_minami_12 with Dissolve(0.1)
    gg 3 "{cps=5}……{/cps}"
    gg 3 "（我意识到自己身上正在发生超自然的事。）"
    gg 3 "（或者……我疯了。）"
    gg 3 "（但她的话说明，这可能就是真的。）"
    scene school_dolg_minami_6 with Dissolve(0.1)
    mi 1 "[gg]，我很在意刚才在走廊看到的事。" with dissolve
    if draka_roof_loose == True:
        scene school_dolg_minami_8 with Dissolve(0.3)
        mi 1 "昨天你在天台上被打，却连一处擦伤都没有。" with dissolve
    if draka_roof_loose == False:
        scene school_dolg_minami_8 with Dissolve(0.3)
        mi 1 "我觉得昨天在天台上动手的人就是你。" with dissolve
        scene school_dolg_minami_7 with Dissolve(0.3)
        mi 1 "可惜我没亲眼看见，所以不能确定。" with dissolve
        
    scene school_dolg_minami_1 with Dissolve(0.1)
    mi 1 "今天，我亲眼看到了你移动的速度。" with dissolve
    mi 1 "跟我说实话！"
    mi 1 "你知道这是为什么吗？"
    show school_dolg_minami_15 with Dissolve(0.1)
    gg 3 "（她好像知道些什么。）" with dissolve
    gg 3 "（不确定该不该告诉她……）"
    gg 3 "（但现在她似乎是唯一可能理解我的人。）"
    gg 3 "我自己也不明白。"
    gg 3 "我一直在做一些奇怪的梦……感觉像是别人的记忆……极其真实的记忆。"
    gg 3 "现在又出了这种事……本以为搬家之后能过安生日子，可现在我觉得非弄清楚不可。"
    scene school_dolg_minami_2 with Dissolve(0.1)
    mi 1 "再多说一点。" with dissolve
    mi 1 "也许我能帮上点忙。"
    show school_dolg_minami_15 with Dissolve(0.1)
    gg 3 "在这些梦里，我去了未来。" with dissolve
    gg 3 "我看到的一切都太真实了，就像我真的在现场一样。"
    gg 3 "最近我梦到了一个女孩……一个陌生人，但很危险。"
    gg 3 "先说清楚，不是春梦。她朝我开了枪。"
    scene school_dolg_minami_8 with Dissolve(0.1)
    mi 1 "这听起来可不妙。" with dissolve
    mi 1 "梦往往有意义，指向某种重要的东西。"
    scene school_dolg_minami_7 with Dissolve(0.3)
    mi 1 "跟我说说这个女孩。你还记得什么？" with dissolve
    scene school_dolg_minami_6 with Dissolve(0.3)
    mi 1 "她也许在某种程度上跟你有某种联系。" with dissolve
    show school_dolg_minami_16 with Dissolve(0.1)
    gg 3 "我记得她的脸，尽管现实中从没见过她。" with dissolve
    gg 3 "深色头发，身材纤细。"
    gg 3 "她说话的口吻，好像我们认识了很多年……而且她知道我的名字。"
    gg 3 "她开枪之后我就醒了，现在额头中弹的地方还隐隐作痛。"
    scene school_dolg_minami_17 with Dissolve(0.1)
    mi 1 "我的天。" with dissolve
    scene school_dolg_minami_18 with Dissolve(0.1)
    gg 3 "也许是幻痛之类的。医生应该能解释清楚。" with dissolve
    scene school_dolg_minami_4 with Dissolve(0.1)
    gg 3 "但不管怎么说，那感觉不愉快。" with dissolve
    scene school_dolg_minami_10 with Dissolve(0.1)
    mi 1 "老实说，我暂时也说不准这意味着什么。" with dissolve
    mi 1 "这些梦或记忆，也许跟你潜藏的能力有关。"      
    scene school_dolg_minami_11 with Dissolve(0.3)
    gg 3 "我完全找不到解释。" with dissolve
    show school_dolg_minami_16 with Dissolve(0.1)
    gg 3 "为什么会看清她的脸，还记得她的名字？" with dissolve
    gg 3 "这不正常。"
    scene school_dolg_minami_19 with Dissolve(0.2)
    mi 1 "我明白这一定既吓人又让人困惑。" with dissolve
    scene school_dolg_minami_20 with Dissolve(0.3)
    mi 1 "但我们得继续查下去。" with dissolve
    scene school_dolg_minami_3 with Dissolve(0.3)
    gg 3 "我必须弄清楚。" with dissolve
    gg 3 "我不想一直蒙在鼓里。"
    scene school_dolg_minami_2 with Dissolve(0.1)
    mi 1 "我可以帮你查更多。" with dissolve
    scene school_dolg_minami_1 with Dissolve(0.1)
    mi 1 "我有些人脉或许能帮上忙。" with dissolve
    mi 1 "交给我吧。"
    stop music2 fadeout 6
    play music3 breathe_easy_and_relax_by_musiclfiles volume 0.6 fadein 6
    scene school_dolg_minami_21 with Dissolve(0.1)
    gg 3 "嗯……我不知道你怎么会知道这些事。不过谢谢你，[mi]。" with dissolve
    scene school_dolg_minami_22 with Dissolve(0.1)
    pause 0.3
    show school_dolg_minami_23
    $ renpy.pause(4, hard=True)
    pause 0.5
    mi 1 "我得想想，不过我知道的都会告诉你。不过我们得改天见面谈。" with dissolve
    scene school_dolg_minami_24 with Dissolve(0.3)
    mi 1 "找个私密的地方。"
    scene school_dolg_minami_25 with Dissolve(0.1)
    gg 3 "什么时候？" with dissolve
    scene school_dolg_minami_26 with Dissolve(0.1)
    mi 1 "明天放学后。" with dissolve
    scene school_dolg_minami_27 with Dissolve(0.3)
    mi 1 "这毕竟不是学校的事，多做些防备也不为过。" with dissolve
    scene school_dolg_minami_28 with Dissolve(0.3)
    mi 1 "相信我，这对你会有用的。" with dissolve
    gg 3 "（靠，这学校里的人是不是每个人都有黑道关系、亿万富翁父母或者什么神秘背景？）" with dissolve
    scene school_dolg_minami_29 with Dissolve(0.3)
    mi 1 "也许能找到你部分问题的答案。" with dissolve
    play sound skrip_stula volume 0.6
    scene school_dolg_minami_30 with Dissolve(0.1)
    gg 3 "明白，那就明天放学后见。" with dissolve
    scene school_dolg_minami_31 with Dissolve(0.3)
    $ minami_know_superpower = True
    mi 1 "[gg]，小心点。" with dissolve
    stop music3 fadeout 3
    
    scene black with dissolve
    pause 3.0
## Dai and Mezehiro, Debt, School
label school_dolg_dm:

    play music3 city_bird fadein 1 volume 0.5
    
    scene school_dolg_dm_1 with Dissolve(1.0)
    gg t3 "（好了，下课了。）" with dissolve
    scene school_dolg_dm_2 with Dissolve(0.3)
    gg 3 "（[may]应该快出来了。我等着。）" with dissolve
    scene school_dolg_dm_3 with Dissolve(0.1)
    me 1 "喂，新人！" with dissolve
    scene school_dolg_dm_4 with Dissolve(0.3)
    dai 1 "有事找你。过来！" with dissolve
    scene school_dolg_dm_5 with Dissolve(0.1)
    gg 3 "（这两个白痴又来了。）" with dissolve
    
    $ renpy.music.set_volume(0.3, delay=3, channel=u'music3')
    play music2 marty_gots_a_plan_by_kevin_macleod volume 0.6 fadein 3
    
    scene school_dolg_dm_6 with dissolve
    me 1 "[gg]，还是说你叫什么来着？" with dissolve
    scene school_dolg_dm_7 with Dissolve(0.3)
    me 1 "给他！" with dissolve
    scene school_dolg_dm_8 with Dissolve(0.3)
    pause 1.0
    play sound swing6
    scene school_dolg_dm_9 with Dissolve(0.3)
    dai 1 "要来一根吗？" with dissolve
    
    menu:
        "接过烟\\n[red](吸烟)":
            scene school_dolg_dm_13 with Dissolve(0.3)
            pause 1.0
            scene school_dolg_dm_14 with Dissolve(0.3)
            pause 1.0
            play sound zajigalka
            scene school_dolg_dm_15 with Dissolve(0.3)
            $ smoking = True
            pause 1.5
        
        '「我不抽烟。」':
            scene school_dolg_dm_10 with Dissolve(0.3)
            gg 3 "我不抽烟。" with dissolve
            scene school_dolg_dm_11 with Dissolve(0.3)
            dai 1 "我早说了他不抽！" with dissolve
            scene school_dolg_dm_12 with Dissolve(0.3)
            dai 1 "...!"
            
    scene school_dolg_dm_16 with Dissolve(0.3)
    me 1 "你到底是哪儿冒出来的？" with dissolve
    scene school_dolg_dm_17 with Dissolve(0.3)
    me 1 "你可真是惹了不少事。" with dissolve
    scene school_dolg_dm_18 with Dissolve(0.3)
    dai 1 "你有在健身吗？靠什么补剂才练成那样的？" with dissolve
    scene school_dolg_dm_19 with Dissolve(0.3)
    me 1 "说不定他不像你这个死肥猪，一口气吃到撑死！" with dissolve
    play sound2 swing4 volume 0.5
    scene school_dolg_dm_20 with Dissolve(0.3)
    dai 1 "去你的！"
    scene school_dolg_dm_16 with Dissolve(0.3)
    me 1 "喂……别记恨我们，行吗？我们不是坏人。" with dissolve
    scene school_dolg_dm_17 with Dissolve(0.3)
    me 1 "毕竟我们是同班的！" with dissolve
    scene school_dolg_dm_21 with Dissolve(0.3)
    me 1 "以后要是有麻烦，尽管来找我们——自己人，我们照管。" with dissolve
    scene school_dolg_dm_22 with Dissolve(0.3)
    dai 1 "话说……" with dissolve
    scene school_dolg_dm_23 with Dissolve(0.3)
    li 1 "喂，你们两个！"
    
    stop music2 fadeout 1
    $ renpy.music.set_volume(1, delay=1, channel=u'music3')
    
    show school_dolg_dm_24 with Dissolve(0.1)
    $ renpy.pause(2.5, hard=True)
    play sound woosh2
    scene school_dolg_dm_25 with hpunch
    li 1 "干嘛缠着他？！"
    play sound2 swing3 volume 0.5
    scene school_dolg_dm_26 with Dissolve(0.3)
    li 1 "你们想跟那只刺猬一样被收拾吗？！" with dissolve
    scene school_dolg_dm_27 with Dissolve(0.1)
    $ renpy.music.set_volume(0.3, delay=1, channel=u'music3')
    play music2 marty_gots_a_plan_by_kevin_macleod volume 0.6 fadein 1
    dai 1 "冷静点，[li]。什么事让你这么激动？" with dissolve
    
    if love_li >= 3:
        scene school_dolg_dm_28 with Dissolve(0.3)
        gg 3 "别担心，[li]，我们只是聊聊。" with dissolve
    if love_li < 3:
        scene school_dolg_dm_29 with Dissolve(0.3)
        gg 3 "你刚才那话，到底是想护着谁？" with dissolve
    
    scene school_dolg_dm_30 with Dissolve(0.3)
    dai 1 "就是说！别搞得好像我们是坏人一样。" with dissolve
    scene school_dolg_dm_31 with Dissolve(0.3)
    me 1 "你给我闭嘴。" with dissolve
    play sound zahvat_2 volume 0.3
    scene school_dolg_dm_32 with hpunch
    dai 1 "去你的！"
    
    if love_li >= 3:
        scene school_dolg_dm_33 with Dissolve(0.3)
    if love_li < 3:
        scene school_dolg_dm_34 with Dissolve(0.3)
    gg 3 "你们刚才在聊什么？" with dissolve
    
    scene school_dolg_dm_35 with Dissolve(0.3)
    dai 1 "哦对，我们正想着要去……" with dissolve
    scene school_dolg_dm_36 with Dissolve(0.3)
    me 1 "我们决定出去聚一聚，想叫上你。"with dissolve 
    me 1 "跟朋友保持联系很重要！"
    scene school_dolg_dm_37 with Dissolve(0.3)
    dai 1 "喂，别老抢我话，白痴！" with dissolve

    if love_li >= 3:
        scene school_dolg_dm_33 with Dissolve(0.3)
    else:
        scene school_dolg_dm_34 with Dissolve(0.3)
        
    gg 3 "他们真是朋友吗？" with dissolve
    
    if love_li >= 3:
        scene school_dolg_dm_38 with Dissolve(0.3)
    else:
        scene school_dolg_dm_39 with Dissolve(0.3)
        
    li 1 "大概吧……"
    
    scene school_dolg_dm_40 with Dissolve(0.3)
    me 1 "钱别操心，[dai]全包了。" with dissolve
    play sound swing4 volume 0.5
    scene school_dolg_dm_41 with hpunch
    dai 1 "我什么时候说过这话了？这明明是你的主意！"
    play sound2 swing1 volume 0.5
    scene school_dolg_dm_42 with hpunch
    me 1 "上次就是我付的钱！"
    play sound3 swing2 volume 0.5
    scene school_dolg_dm_43 with hpunch
    dai 1 "那次明明只有两个人。现在是三个！"
    play sound zahvat_2 volume 0.5
    scene school_dolg_dm_44 with hpunch
    me 1 "别这么小气！"
    scene school_dolg_dm_45 with Dissolve(0.3)
    dai 1 "去你的！" with dissolve
    scene school_dolg_dm_46 with Dissolve(0.3)
    gg 3 "你请客的话我就去。" with dissolve
    scene school_dolg_dm_47 with Dissolve(0.3)
    gg 3 "（要是他们从此不再烦我，就完美了。而且这说不定能成为我找工作的起点。）" with dissolve
    scene school_dolg_dm_48 with Dissolve(0.3)
    li 1 "你们要去我也去。" with dissolve
    scene school_dolg_dm_49 with Dissolve(0.3)
    dai 1 "喂，我可请不起你们这种人！你们这种人叫什么来着？！" with dissolve
    scene school_dolg_dm_50 with Dissolve(0.3)
    li 1 "我自己那份我会付，放心吧。" with dissolve
    scene school_dolg_dm_51 with Dissolve(0.3)
    dai 1 "那就太棒了！" with dissolve
    play sound zahvat_1 volume 0.5
    scene school_dolg_dm_52 with vpunch
    da 2 "你们这些家伙在聊什么？"
    scene school_dolg_dm_53 with Dissolve(0.3)
    da 2 "{cps=5}……{/cps}"
    play sound woosh1 volume 0.5
    scene school_dolg_dm_54 with PushMove(0.1, 'pushleft')
    li 1 "在说你是怎么上了一堂宝贵的一课。"
    play sound2 woosh2 volume 0.5
    scene school_dolg_dm_55 with PushMove(0.1, 'pushright')
    da 2 "屁。他只是走运罢了。"
    menu:
        '「你确定？」\\n[gr](推荐)':
            scene school_dolg_dm_56 with Dissolve(0.3)
            gg 3 "你确定？"
            play sound2 swing2 volume 0.5
            scene school_dolg_dm_58 with hpunch
            da 2 "不确定！"
            play sound slap1
            scene school_dolg_dm_59 with hpunch
            da 2 "该死，我是说……"
            play sound2 swing1 volume 0.5
            scene school_dolg_dm_60 with Dissolve(0.3)
            da 2 "算了。" with dissolve
            
        '什么都不说':
            scene school_dolg_dm_56 with Dissolve(0.3)
            gg 3 "{cps=5}……{/cps}"
            scene school_dolg_dm_57 with Dissolve(0.3)
            da 2 "随便吧。" with dissolve
     
    scene school_dolg_dm_61 with Dissolve(0.3)
    me 1 "我们今晚聚一下吧。" with dissolve
    scene school_dolg_dm_62 with Dissolve(0.3)
    da 2 "不打算叫上我？" with dissolve
    scene school_dolg_dm_63 with Dissolve(0.3)
    dai 1 "好、好吧，带上我。" with dissolve
    scene school_dolg_dm_64 with Dissolve(0.3)
    da 2 "这还差不多。" with dissolve
    scene school_dolg_dm_65 with Dissolve(0.3)
    me 1 "好，我们交换一下号码吧。" with dissolve
    scene school_dolg_dm_66 with Dissolve(0.3)
    me 1  "今晚给你打电话！" with dissolve
    stop music2 fadeout 3
    scene black with Dissolve(1.0)
    pause 3.0
    
## Home, Debt

label home_dolg_may:
    
    $ renpy.music.set_volume(1, delay=0, channel=u'music3')
    play music3 scott_buckley_the_long_dark volume 0.5 fadein 6
    show home_dolg_may_0 with Dissolve(0.5)
    $ renpy.pause(3, hard=True)
    gg t8 "（我已经想不出怎么赚钱了。）" with dissolve
    scene home_dolg_may_1 with dissolve
    gg t8 "（就算找份普通的兼职，也远远凑不够我要的数。）"
    gg t8 "（靠，六万块得省吃俭用存好几年！）" with dissolve
    gg t8 "（也许该跟他们谈谈。那个金发头目肯定有的是钱……）"
    gg t8 "{cps=5}……{/cps}"
    scene home_dolg_may_2 with Dissolve(0.3)
    gg t8 "（但说了有什么用？我跟他几乎不熟。）" with dissolve
    gg t8 "（也许他们有些我还没想到的门路。）"
    gg t8 "{cps=5}……{/cps}"
    gg t8 "（不过看他们的样子，能想出来的多半是卖违禁品之类的歪门邪道……）"
    gg t8 "（话说回来，想快速赚到那种钱也没有别的办法。）"
    gg t8 "（看来只能咽下疑虑，赌一把了。为了平静的生活……）"
    stop music3 fadeout 1
    play sound woosh3
    scene home_dolg_may_3 with hpunch
    may 8 "[gg]！"
    scene home_dolg_may_4 with Dissolve(0.3)
    may 8 "{cps=5}……{/cps}" with dissolve
    scene home_dolg_may_5 with Dissolve(0.3)
    gg 8 "怎么了？" with dissolve
    play sound box1
    show home_dolg_may_6  with Dissolve(0.3):
        zoom 1.2 xalign 0.5 yalign 0.5
        easein 1.0 zoom 1.0
    pause 1.0
    menu:
        "打开":
            pause 0.6
    show home_dolg_may_7 with Dissolve(0.1)
    hide home_dolg_may_6
    $ renpy.pause(1.0, hard=True)
    play sound box2 volume 0.2
    $ renpy.pause(0.5, hard=True)
    play sound2 dm2
    $ renpy.pause(2.5, hard=True)
    play music3 unseen_by_phat_sounds volume 0.6 fadein 1
    gg 8 "（一把枪？）" with dissolve
    scene home_dolg_may_8 with Dissolve(0.3)
    gg 8 "……你从哪儿找到这个的？" with dissolve
    scene home_dolg_may_9 with Dissolve(0.3)
    may 8 "在你房间里啊！" with dissolve
    scene home_dolg_may_10 with Dissolve(0.3)
    may 8 "我在打扫时发现床底下有个箱子。" with dissolve
    scene home_dolg_may_11 with Dissolve(0.3)
    may 8 "以前没见过，就想看看是什么，然后该放哪儿。" with dissolve
    scene home_dolg_may_12 with Dissolve(0.3)
    may 8 "然后……" with dissolve
    scene home_dolg_may_13 with Dissolve(0.3)
    gg 8 "我知道了。" with dissolve
    scene home_dolg_may_14 with Dissolve(0.3)
    gg 8 "（这他妈怎么会有把枪出现在我房间里？）" with dissolve
    scene home_dolg_may_10 with Dissolve(0.3)
    may 8 "你老实说……" with dissolve
    play sound woosh2
    show home_dolg_may_15:
        zoom 0.8 xalign 0.5 yalign 0.1
        easein 0.1 zoom 1
    may 8 "{cps=66}你是不是在做什么违法的事？{/cps}" with Dissolve(0.1)
    scene home_dolg_may_16 with Dissolve(0.3)
    gg 8 "[may]，别傻了，我们才搬来两天。" with dissolve
    gg 8 "你怎么会这么想？"
    scene home_dolg_may_17 with Dissolve(0.3)
    may 8 "那要是我们住得再久一点，你就会了？" with dissolve
    scene home_dolg_may_8 with Dissolve(0.3)
    gg 8 "妹，我虽然是坏小子，但我不会朝人开枪。" with dissolve
    scene home_dolg_may_9 with Dissolve(0.3)
    may 8 "那这把枪是怎么到你房间里的？" with dissolve
    scene home_dolg_may_18 with Dissolve(0.3)
    gg 8 "我也想知道。" with dissolve
    play sound woosh2
    scene home_dolg_may_19:
        zoom 1.2 xalign 0.5 yalign 0.5
        easein 0.2 zoom 1
    may 8 "报警吗？" with Dissolve(0.3)
    scene home_dolg_may_20 with Dissolve(0.3)
    gg 8 "不。" with dissolve
    scene home_dolg_may_21 with Dissolve(0.3)
    may 8 "为什么？" with dissolve
    scene home_dolg_may_22 with Dissolve(0.3)
    gg 8 "（完全不知道这玩意儿哪来的……但我怀疑有人动了手脚。）" with dissolve
    gg 8 "（让我想起一件事……）"
    $ renpy.music.set_volume(0.3, delay=1, channel=u'music3')
    scene black with Dissolve(1.0)
    pause 0.5
    scene home_dolg_may_23 with Dissolve(1.6):
        center
        zoom 1.2
        ease 2 zoom 1
    scene home_dolg_may_24 with Dissolve(1.8)
    ''
    $ renpy.music.set_volume(1, delay=3, channel=u'music3')
    scene home_dolg_may_22 with Dissolve(2.0)
    gg 8 "（真的是她吗？）" with dissolve
    gg 8 "（不可能是真的。）"
    gg 8 "（搬进来之后我一次都没看过床底下。会不会是爸爸的枪？）"
    gg 8 "（不可能。他是科学家，不是黑道。）"
    gg 8 "（不过摊上这笔债之后，什么事我都不觉得稀奇了。）"
    scene home_dolg_may_25 with Dissolve(0.3)
    may 8 "[gg]……？" with dissolve
    scene home_dolg_may_26 with Dissolve(0.3)
    gg 8 "不能。要是警方怀疑我们犯了案，或者告我们非法持有武器怎么办？" with dissolve
    play sound3 box1 volume 0.3
    scene home_dolg_may_27 with Dissolve(0.3)
    gg 8 "我能把它处理掉。" with dissolve
    scene home_dolg_may_28 with Dissolve(0.3)
    gg 8 "给我拿副手套来。" with dissolve
    scene home_dolg_may_29 with Dissolve(0.3)
    gg 8 "（我得小心，不能留下指纹。）" with dissolve
    gg 8 "（这可能是个圈套。）"
    scene home_dolg_may_30 with Dissolve(0.3)
    gg 8 "（那个梦跟其他的不一样，我感觉自己真的经历过。）" with dissolve
    gg 8 "（也许就是那次。）"
    scene home_dolg_may_31 with Dissolve(0.3)
    may 8 "给。"
    scene home_dolg_may_32 with Dissolve(0.3)
    pause 1.0
    play sound gloves
    scene home_dolg_may_33 with Dissolve(0.3):
        pause 1.8
        zoom 1.0 xalign 0.5 yalign 0.1
        easein 0.3 zoom 1.5
    pause 1.5
    play sound2 woosh2 volume 0.5
    show home_dolg_may_34 with fade
    $ renpy.pause(13,hard=True)
    scene home_dolg_may_35 with Dissolve(0.3)
    may 8 "一封信？" with dissolve
    scene home_dolg_may_36 with Dissolve(0.3)
    may 8 "在里面。" with dissolve
    play sound gloves volume 0.5
    scene home_dolg_may_37 with Dissolve(0.3)
    pause 1.0
    play sound box1 volume 0.5
    scene home_dolg_may_38 with Dissolve(0.3)
    pause 1.8
    play sound paper1 volume 0.5
    scene home_dolg_may_39 with Dissolve(0.3)
    pause 1.5
    play sound swing6 volume 0.5
    show home_dolg_may_40 with Dissolve(0.2):
        zoom 0.8 xalign 0.5 yalign 0.5
        easein 0.2 zoom 1
    gg 8 "（该死……）" with dissolve
    play sound woosh1 volume 0.5
    show home_dolg_may_41 with Dissolve(0.2):
        zoom 1.3 xalign 0.5 yalign 0.5
        easein 0.2 zoom 1
    gg 8 "坐下！" with dissolve
    scene home_dolg_may_42 with fade
    "亲爱的，希望你一切都好。" with dissolve
    scene home_dolg_may_43 with Dissolve(0.3)
    "实在没有别的办法。" with dissolve
    "就当这是我送你的礼物吧。"
    "P.S. 不用担心，追溯不到源头。用的时候小心点！"
    scene home_dolg_may_44 with Dissolve(0.3)
    "永远属于你的，[asami]。" with dissolve
    pause 0.5
    may 8 "上面写了什么？" with dissolve
    scene home_dolg_may_45 with Dissolve(0.3)
    gg 8 "没什么重要的，全是胡言乱语。" with dissolve
    scene home_dolg_may_46 with Dissolve(0.3)
    may 8 "我能看看吗？" with dissolve
    scene home_dolg_may_47 with Dissolve(0.3)
    
    $ choice_var = 1
    menu:
        "把信交给她\\n[gr](推荐)":
            play sound paper1 volume 0.5
            scene home_dolg_may_48 with fade
            may 8 "{cps=5}……{/cps}" with dissolve
            scene home_dolg_may_49 with Dissolve(0.3)
            may 8 "真是份奇怪的礼物。" with dissolve
            scene home_dolg_may_50 with Dissolve(0.3)
            may 8 "{cps=5}……{/cps}" with dissolve
            scene home_dolg_may_51 with Dissolve(0.3)
            may 8 "「永远属于你的……」" with dissolve
            scene home_dolg_may_52 with Dissolve(0.3)
            may 8 "[asami]是谁？" with dissolve
            $ may_know_asami = True
            show home_dolg_may_53 with Dissolve(0.3)
            pause 0.5
            gg 8 "{cps=5}……{/cps}" with dissolve
            gg 8 "老实说……我觉得现实中我们从没见过她。"
            gg 8 "而且我完全不知道这一切是从哪儿来的。"
            
        '「不。」':
            show home_dolg_may_54 with fade
            gg 8 "不。" with dissolve
            scene home_dolg_may_55 with Dissolve(0.3)
            may 8 "为什么？" with dissolve
            show home_dolg_may_54 with Dissolve(0.3)
            
            $ choice_var = 0
            menu:
                "「是说明书。」":
                    show home_dolg_may_54 with Dissolve(0.3)
                    gg 8 "这是本使用说明书。你真的想知道？" with dissolve
                    scene home_dolg_may_56 with Dissolve(0.3)
                    may 8 "用口红写的？" with dissolve
                    show home_dolg_may_54 with Dissolve(0.3)
                    gg 8 "是个标志。" with dissolve
                    
                '「是情书。」':
                    show home_dolg_may_54 with Dissolve(0.3)
                    gg 8 "是情书。" with dissolve
                    scene home_dolg_may_57 with Dissolve(0.3)
                    may 8 "你开玩笑吧？" with dissolve
                    show home_dolg_may_54 with Dissolve(0.3)
                    
                "「完全是胡话。」":
                    gg 8 "我说了，全是鬼话。" with dissolve
                    
            may 8 "{cps=5}……{/cps}" with dissolve
    $ choice_var = 0
    scene home_dolg_may_58 with Dissolve(0.3)
    gg 8 "我会处理掉的。你可以继续打扫了。" with dissolve
    scene home_dolg_may_59 with Dissolve(1.3)
    may 8 "好吧……" with dissolve
    stop music3 fadeout 8
    pause 1.5
    play music2 a_nice_dream_by_frank_schroeter fadein 8 volume 0.8
    gg 8 "我要去跟几个同学聚一下。" with dissolve
    scene home_dolg_may_60 with Dissolve(1.3)
    gg 8 "可能会回来得晚。" with dissolve
    may 8 "尽量别过了午夜才回来。" with dissolve
    may 8 "我会等你。" with dissolve
    show home_dolg_may_61 with Dissolve(0.3)
    $ renpy.pause(5.9,hard=True)
    show home_dolg_may_62 with Dissolve(0.1)
    hide home_dolg_may_61
    $ choice_var = 1
    $ home_dolg_may_choices = []
    menu home_dolg_may_choices:
        set home_dolg_may_choices
        "「要跟我一起去吗？」":
            gg 8 "要跟我一起去吗？" with dissolve
            scene home_dolg_may_63 with Dissolve(0.3)
            may 8 "哦，不了。我还是想待在家。" with dissolve
            scene home_dolg_may_64 with Dissolve(0.3)
            gg 8 "为什么？" with dissolve
            scene home_dolg_may_65 with Dissolve(0.3)
            may 8 "那个……下次吧。" with dissolve
            scene home_dolg_may_66 with Dissolve(0.3)
            may 8 "那边会有男生……我不习惯那种场合。" with dissolve
            scene home_dolg_may_67 with Dissolve(0.3)
            may 8 "我宁愿待在家看动画。" with dissolve
            scene home_dolg_may_68 with Dissolve(0.3)
            may 8 "玩得开心。" with dissolve
            scene home_dolg_may_69 with Dissolve(0.3)
            gg 8 "谢了。" with dissolve
            pause .5
            scene home_dolg_may_70 with Dissolve(0.3)
            may 8 "会有女生吗？" with dissolve
            show home_dolg_may_71 with Dissolve(0.3)
            menu:
                "「有，[li]会去。」\\n[blue](更多内容)":
                    gg 8 "有，[li]会去——我同学。" with dissolve
                    $ may_know_lillian = True
                    scene home_dolg_may_72 with Dissolve(0.3)
                    may 8 "这样啊……" with dissolve
                    scene home_dolg_may_73 with Dissolve(0.3)
                    may 8 "那就替我向[li]问好。" with dissolve
                    scene home_dolg_may_74 with Dissolve(0.3)
                    gg 8 "我觉得你们俩应该能合得来。" with dissolve
                    scene home_dolg_may_75 with Dissolve(0.3)
                    may 8 "也、也许吧。" with dissolve
                    may 8 "也许……"
                    scene home_dolg_may_76 with Dissolve(0.3)
                    may 8 "不过会有多少男生？" with dissolve
                    scene home_dolg_may_77 with Dissolve(0.3)
                    gg 8 "除了我，还有另外三个同学。" with dissolve
                    scene home_dolg_may_78 with Dissolve(0.3)
                    may 8 "{cps=5}……{/cps}"
                    scene home_dolg_may_79 with Dissolve(0.3)
                    may 8 "一个女生……" with dissolve
                    scene home_dolg_may_80 with Dissolve(0.3)
                    may 8 "被四个男的围着……" with dissolve
                    scene home_dolg_may_81 with Dissolve(0.3)
                    may 8 "他们跟她很熟吗？" with dissolve
                    scene home_dolg_may_82 with Dissolve(0.3)
                    gg 8 "倒也谈不上。真要说的话，可能我跟她最熟。" with dissolve
                    scene home_dolg_may_83 with Dissolve(0.3)
                    may 8 "那她怎么会跟你们混在一起？" with dissolve
                    scene home_dolg_may_84 with Dissolve(0.3)
                    may 8 "肯定是因为你吧？" with dissolve
                    scene home_dolg_may_85 with Dissolve(0.3)
                    gg 8 "[may]，你想太多了！我们只是朋友，没什么特别的。" with dissolve
                    scene home_dolg_may_86 with Dissolve(0.3)
                    may 8 "我只是好奇嘛。" with dissolve
                    show home_dolg_may_87 with Dissolve(0.01)
                    $ renpy.pause(1.499,hard=True)
                    show home_dolg_may_88 with Dissolve(0.01)
                    menu:
                        '「你吃醋了？」':
                            gg 8 "[may]，你该不会是吃醋了吧？" with dissolve
                            scene home_dolg_may_89 with Dissolve(0.3)
                            may 8 "才、才不是，我连她是谁都不认识！" with dissolve
                            scene home_dolg_may_90 with Dissolve(0.3)
                            gg 8 "别把这事当回事。你不用担心。" with dissolve
                            scene home_dolg_may_91 with Dissolve(0.3)
                            may 8 "好。"
                                        
                        "「别放在心上。」":
                            gg 8 "别放在心上。" with dissolve
                            scene home_dolg_may_91 with Dissolve(0.3)
                            may 8 "小心点就行。" with dissolve
                            
                        '不用。':
                            pause 0.3
                            
                    show home_dolg_may_88 with Dissolve(0.3)
                    
                '「不。」':
                    gg 8 "不。"
                    scene home_dolg_may_92 with Dissolve(0.3)
                    may 8 "好。有事联系！" with dissolve
                    show home_dolg_may_71 with Dissolve(0.3)
                    gg 8 "知道了。想打电话随时打。" with dissolve
                    
            jump home_dolg_may_choices

        '「谢谢你照顾我。」':
            gg 8 "话说，那天晚上多亏你照顾我了。" with dissolve
            scene home_dolg_may_93 with Dissolve(0.3)
            may 8 "啊，没什么。你当时都昏迷了……" with dissolve
            scene home_dolg_may_94 with Dissolve(0.3)
            gg 8 "昏迷着，还光着身子，对吧？" with dissolve
            gg 8 "我又没抱怨，只是好奇。" with dissolve
            scene home_dolg_may_95 with Dissolve(0.3)
            gg 8 "那场面肯定挺壮观的。" with dissolve
            gg 8 "那我可得更厉害一点才能扳平……" with dissolve
            gg 8 "对吧？" with dissolve
            scene home_dolg_may_96 with Dissolve(0.3)
            may 8 "别闹了，[gg]！一点都不好笑！" with dissolve
            scene home_dolg_may_97 with Dissolve(0.3)
            gg 8 "哎呀，[may]。你慌张的样子很可爱啊。" with dissolve
            scene home_dolg_may_98 with Dissolve(0.3)
            gg 8 "但你得承认，还挺有意思的。" with dissolve
            scene home_dolg_may_99 with Dissolve(0.3)
            may 8 "是哦。我最好的朋友，昏迷着躺在浴室里，差点被自己的口水或者流出来的水淹死。" with dissolve
            may 8 "笑死我了。我快笑死了。"
            may 8 "我只是想尽我所能帮点忙。有那么糟糕吗？"
            show home_dolg_may_62 with Dissolve(0.3)
            $ may_thanks_night = True
            gg 8 "当然没有！" with dissolve
            jump home_dolg_may_choices

        "离开\\n[gr](最后选择)":
            pause 0.1
    $ choice_var = 0
    gg 8 "好了，我出门了。" with dissolve
    scene home_dolg_may_100 with Dissolve(0.3)
    may 8 "一路顺风！" with dissolve
    stop music2 fadeout 3
    play music3 japan_streets_2 fadein 6
    jump classmates_party_1

## Cafe, Debt, Lillian, Dai, Mezehiro and Jabrayil
label classmates_party_1:
    scene black with Dissolve(0.5)
    pause 2.0
    show cm_party_0 with Dissolve(0.5)
    play sound cm_party_0_sound
    $ aksha -= 19
    $ renpy.pause(5.5,hard=True)
    scene cm_party_1 with Dissolve(0.3)
    gg 8 "([li]？)" with dissolve
    gg 8 "（她怎么会一个人在这儿？）"
    scene cm_party_2 with Dissolve(0.3)
    gg 8 "你在等我吗？" with dissolve
    scene cm_party_3 with Dissolve(0.3)
    li 2 "{cps=5}……{/cps}"
    scene cm_party_4 with Dissolve(0.3)
    li 2 "哦，嗨！对啊。" with dissolve
    scene cm_party_5 with Dissolve(0.3)
    li 2 "天太黑，没一下子认出你。" with dissolve
    scene cm_party_6 with Dissolve(0.3)
    li 2 "谢天谢地你来了。我都担心你会不会压根不跟这群混蛋见面。" with dissolve
    scene cm_party_7 with Dissolve(0.3)
    li 2 "你不介意我也来吧？" with dissolve
    show cm_party_8 with Dissolve(0.3)
    gg 8 "当然不介意。不过有点不好意思——一般都是男生等女生，不是反过来。" with dissolve
    scene cm_party_15 with Dissolve(0.3)
    li 2 "哈哈哈！那就当你欠我一次等人情吧。" with dissolve
    show cm_party_8 with Dissolve(0.3)
    
    menu:
        "「你美极了！」\\n[gold](莉莲 +1)":
            gg 8 "你美极了！" with dissolve
            $ love_li += 1
            show screen rel_up_lillian
            $ lillian_compliment_appearance = True
            scene cm_party_9 with Dissolve(0.3)
            li 2 "谢谢！" with dissolve
            scene cm_party_10 with Dissolve(0.3)
            li 2 "出门前我试了新的化妆。" with dissolve
            scene cm_party_11 with Dissolve(0.3)            
            li 2 "后来又换了发型。" with dissolve
            scene cm_party_12 with Dissolve(0.3)
            li 2 "想给你看看我的新样子。" with dissolve
            show cm_party_13 with Dissolve(0.3)
            gg 8 "你很美，比平时更美。" with dissolve
            gg 8 "那个发型真的很适合你。真好看。"
            scene cm_party_14 with Dissolve(0.3)
            li 2 "你就知道说好听的，是吧？" with dissolve
            scene cm_party_15 with Dissolve(0.3)
            li 2 "不过你喜欢就好。我可是很用心准备的！" with dissolve
            show cm_party_13 with Dissolve(0.3)
            gg 8 "你那么多优点，我怎么可能注意不到。" with dissolve
            scene cm_party_16 with Dissolve(0.3)
            li 2 "你真会讨女孩子欢心！" with dissolve
            show cm_party_13 with Dissolve(0.3)
            gg 8 "我们进去吧？他们大概在等我们了。" with dissolve
            gg 8 "他们肯定也会喜欢你的新造型。"
            scene cm_party_17 with Dissolve(0.3)
            li 2 "好，走吧。" with dissolve
        "「进去吧。」":
            gg 8 "那两个在里面吗？" with dissolve
            scene cm_party_17 with Dissolve(0.3)
            li 2 "在，等着我们呢。" with dissolve
            show cm_party_13 with Dissolve(0.3)
            gg 8 "知道了。进去吧。" with dissolve

    scene black with dissolve
    stop music3 fadeout 6
    pause 0.5
    play music2 fsm_team_escp_midnight_room volume 0.5 fadein 8
    play sound swing3
    scene cm_party_18 with hpunch
    me 2 "你干嘛把他也叫来？"
    scene cm_party_19 with Dissolve(0.3)
    dai 2 "那不然我能怎么办？" with dissolve
    scene cm_party_20 with Dissolve(0.3)
    me 2 "混蛋，你得明白……" with dissolve
    scene cm_party_21 with Dissolve(0.3)
    me 2 "{cps=5}……{/cps}"
    scene cm_party_22 with Dissolve(0.3)
    me 2 "哦……[gg]！" with dissolve
    dai 2 "怎么了？" with dissolve
    scene cm_party_23 with Dissolve(0.3)
    gg 8 "跟早上比没什么变化。" with dissolve
    scene cm_party_24 with Dissolve(0.3)
    me 2 "坐，坐下！" with dissolve
    play sound swing1 volume 0.4
    scene cm_party_25 with Dissolve(0.3)
    me 2 "喂，服务员！" with dissolve
    scene cm_party_26 with Dissolve(0.3)
    cm_barmen "我不是服务员，我……" with dissolve
    scene cm_party_27 with Dissolve(0.3)
    dai 2 "哥们，今晚喝不喝？" with dissolve
    play sound2 swing3 volume 0.5
    scene cm_party_28 with Dissolve(0.3)
    play sound2 swing5 volume 0.5
    
    menu:
        '「喝。」':
            gg 8 "是。"
            $ ishti = True
            scene cm_party_29 with Dissolve(0.3)
            me 2 "服务员！我们要酒！" with dissolve
            cm_barmen "我不是服务员，我是……" with dissolve
            scene cm_party_30 with Dissolve(0.3)
            gg 8 "你也喝？" with dissolve
            scene cm_party_31 with Dissolve(0.3)
            li 2 "为什么不喝？" with dissolve
            play sound woosh2 volume 0.8
            scene cm_party_32 with vpunch
            da 3 "给我也倒一杯。" with dissolve
            
        '[gr]「不。」':
            gg 8 "不。"
            $ ishti = False
            scene cm_party_31 with Dissolve(0.3)
            li 2 "我也不喝了。" with dissolve
            play sound woosh2 volume 0.8
            scene cm_party_32 with vpunch
            da 3 "菜鸟……" with dissolve
    
    gg t8 "（这白痴真来了啊……）" with dissolve
    scene cm_party_33 with Dissolve(0.3)
    da 3 "赶紧给我滚出去！" with dissolve
    da 3 "啊，等下肯定喝到飞起……"
    scene cm_party_34 with Dissolve(0.3)
    pause 1.5
    scene cm_party_35 with Dissolve(0.3)
    pause 1
    scene cm_party_36 with Dissolve(0.3)
    pause 1.0
    scene cm_party_37 with Dissolve(0.3)
    pause 2.6
    scene cm_party_38 with Dissolve(0.3)
    li 2 "别理他们。" with dissolve
    play sound glass_bottles_1 volume 0.5
    scene cm_party_39 with Dissolve(0.3)
    me 2 "快吃！" with dissolve
    if ishti == True:
        scene cm_party_40 with Dissolve(0.3)
        li 2 "给。" with dissolve
        gg 8 "谢了。" with dissolve
    else:
        scene cm_party_41 with Dissolve(0.3)
        dai 2 "你真不喝？" with dissolve
        scene cm_party_42 with Dissolve(0.3)
        da 3 "肯定是酒精不耐受，哈哈！" with dissolve
        scene cm_party_43 with Dissolve(0.3)
        pause 1.0
        scene cm_party_44 with Dissolve(0.3)
        gg 8 "只是现在没心情喝。" with dissolve
        scene cm_party_45 with Dissolve(0.3)
        me 2 "服务员！" with dissolve
        cm_barmen "我不是服务员，我……" with dissolve
        me 2 "我们要果汁！" with dissolve
        cm_barmen "{cps=5}……{/cps}" with dissolve
        cm_barmen "什么口味？"
        me 2 "你们有什么？" with dissolve
        cm_barmen "苹果、橙子、菠萝和樱桃。" with dissolve
        scene cm_party_46 with Dissolve(0.3)
        me 2 "要哪种？" with dissolve
        scene cm_party_47 with Dissolve(0.3)
        menu:
            '「苹果。」':
                gg 8 "苹果。" with dissolve
                $ juice_apple = True
                scene cm_party_45 with Dissolve(0.3)
                me 2 "给我们上苹果汁！" with dissolve
                
            '「橙子。」':
                gg 8 "橙子。" with dissolve
                $ juice_orange = True
                scene cm_party_45 with Dissolve(0.3)
                me 2 "给我们上橙汁！" with dissolve
                
            '[gr]「菠萝。」':
                gg 8 "菠萝。" with dissolve
                $ juice_pineapple = True
                scene cm_party_45 with Dissolve(0.3)
                me 2 "给我们上菠萝汁！" with dissolve
                
            '「樱桃。」':
                gg 8 "樱桃。" with dissolve
                $ juice_cherry = True
                scene cm_party_45 with Dissolve(0.3)
                me 2 "给我们上樱桃汁！" with dissolve
    
    scene cm_party_41 with Dissolve(0.3)
    dai 2 "所以……你是新来的。第一印象怎么样？" with dissolve
    scene cm_party_48 with Dissolve(0.3)
    gg 8 "还在适应。目前还不错。" with dissolve
    gg 8 "（不过除了[may]父亲的离奇死亡、那笔巨额债务、奇怪的梦，还有时间变慢——不过这些你不用知道。）"
    scene cm_party_49 with Dissolve(0.3)
    dai 2 "你会喜欢这儿的。这镇上永远都在发生些疯狂的事。" with dissolve
    if ishti == False:
        play sound glass_bottles_2 volume 0.5
        if juice_apple == True:
            scene cm_party_50 with Dissolve(0.3)
        elif juice_orange == True:
            scene cm_party_51 with Dissolve(0.3)
        elif juice_pineapple == True:
            scene cm_party_52 with Dissolve(0.3)
        else:
            scene cm_party_53 with Dissolve(0.3)
        pause 1.5
        li 2 "我也喝果汁。我给你倒点。" with dissolve
        play sound poured
        scene cm_party_54 with Dissolve(0.3)
        pause 2.0
        if juice_apple == True:
            scene cm_party_55 with Dissolve(0.3)
        elif juice_orange == True:
            scene cm_party_56 with Dissolve(0.3)
        elif juice_pineapple == True:
            scene cm_party_57 with Dissolve(0.3)
        else:
            scene cm_party_58 with Dissolve(0.3)
            
        li 2 "给！" with dissolve
        gg 8 "谢了。" with dissolve
        scene cm_party_59 with Dissolve(0.3)
        da 3 "[li]，也帮我倒一点。" with dissolve
        if juice_apple == True:
            scene cm_party_60 with Dissolve(0.3)
        elif juice_orange == True:
            scene cm_party_61 with Dissolve(0.3)
        elif juice_pineapple == True:
            scene cm_party_62 with Dissolve(0.3)
        else:
            scene cm_party_63 with Dissolve(0.3)
        li 2 "你就当没喝过吧。" with dissolve
        scene cm_party_64 with Dissolve(0.3)
        dai 2 "哈哈哈！" with dissolve
        scene cm_party_65 with Dissolve(0.3)
        da 3 "{cps=5}……{/cps}" with dissolve
        play sound as3 volume 0.4
        scene cm_party_66 with Dissolve(0.3)
        ""
        scene cm_party_67 with Dissolve(0.3)
        pause 1.5
    
    if juice_pineapple == True:
        scene cm_party_68 with Dissolve(0.3)
        da 3 "要是在准备用嘴给女孩口交的时候，菠萝汁最合适了。" with dissolve
        play sound2 energy_glot volume 0.5
        scene cm_party_69 with Dissolve(0.3)
        pause 2.0
        stop sound2 fadeout 1
        play sound woosh1 volume 0.8
        scene cm_party_70 with Dissolve(0.1):
            zoom 1.2 xalign 0.5 yalign 0.5
            easein 0.3 zoom 1
        da 3 "你知道吗？" with dissolve
        scene cm_party_65 with Dissolve(0.3)
        dai 2 "你是说能改变味道？" with dissolve
        scene cm_party_71 with Dissolve(0.3)
        da 3 "对。喝了菠萝汁之后，你的精液会变甜。" with dissolve
        scene cm_party_72 with Dissolve(0.3)
        gg 8 "你自己试过？" with dissolve
        scene cm_party_73 with Dissolve(0.3)
        da 3 "书上看的。" with dissolve
        play sound2 energy_glot volume 0.5
        scene cm_party_69 with Dissolve(0.3)
        pause 2.0
        stop sound2 fadeout 1
        play sound dm1 volume 0.8
        scene cm_party_74 with vpunch
        da 3 "喂？！什么叫「试过」？！" with dissolve
        scene cm_party_75 with Dissolve(0.3)
        gg 8 "我记下了……" with dissolve
        scene cm_party_76 with Dissolve(0.3)
        li 2 "你刚才为什么看我？" with dissolve
        scene cm_party_77 with Dissolve(0.3)
        gg 8 "没什么。" with dissolve
        
    scene cm_party_78 with Dissolve(0.3)
    me 2 "话说，[gg]，你跟父母住吗？" with dissolve
    scene cm_party_79 with Dissolve(0.3)
    gg 8 "才不要。" with dissolve
    scene cm_party_80 with Dissolve(0.3)
    dai 2 "我靠，那我们可以去你家聚！" with dissolve
    scene cm_party_81 with Dissolve(0.3)
    me 2 "好主意，都有谁？" with dissolve
    scene cm_party_82 with Dissolve(0.3)
    gg 8 "我不是一个人住。" with dissolve
    scene cm_party_83 with Dissolve(0.3)
    dai 2 "哦是吗？还有谁跟你一起住？" with dissolve
    scene cm_party_84 with Dissolve(0.3)
    me 2 "该不会是个女生吧。" with dissolve
    if ishti == True:
        scene cm_party_85 with Dissolve(0.3)
    if ishti == False:
        scene cm_party_86 with Dissolve(0.3)
    gg 8 "{cps=5}……{/cps}"
    dai 2 "才不是！" with dissolve
    scene cm_party_78 with Dissolve(0.3)
    me 2 "放学以后一般做什么？" with dissolve
    me 2 "你有打工吗？"
    scene cm_party_79 with Dissolve(0.3)
    gg 8 "那个有点问题。老实说，我现在真的很需要钱。" with dissolve
    scene cm_party_80 with Dissolve(0.3)
    dai 2 "唉，哥们，我懂。钱永远排在第一位。" with dissolve
    scene cm_party_84 with Dissolve(0.3)
    dai 2 "我听说有些人光用手就能赚大钱。" with dissolve
    scene cm_party_79 with Dissolve(0.3)
    gg 8 "用手？" with dissolve
    scene cm_party_88 with Dissolve(0.3)
    pause 1.5
    li 2 "呃！" with dissolve
    scene cm_party_79 with Dissolve(0.3)
    gg 8 "那样能赚多少？" with dissolve
    scene cm_party_87 with Dissolve(0.3)
    dai 2 "大概一天一千美元左右。" with dissolve
    scene cm_party_79 with Dissolve(0.3)
    gg 8 "你认真的？" with dissolve
    scene cm_party_87 with Dissolve(0.3)
    dai 2 "「Alexxis」只接待有钱人。他们的服务简直离谱！" with dissolve
    scene cm_party_79 with Dissolve(0.3)
    if not not_know_alexxis:
        gg 8 "（又是那个「Alexxis」……）" with dissolve
    gg 8 "整整一千……这怎么可能？"
    scene cm_party_80 with Dissolve(0.3)
    dai 2 "对你来说说不定是个选择。" with dissolve
    dai 2 "我认识一个人，在她们脸上打手枪，小费特别多。" with dissolve
    scene cm_party_84 with Dissolve(0.3)
    me 2 "我觉得你真去上她们能赚更多。" with dissolve
    scene cm_party_87 with Dissolve(0.3)
    dai 2 "嗯，听着就很爽！" with dissolve
    if ishti == True:
        scene cm_party_89 with Dissolve(0.3)
    if juice_apple == True:
        scene cm_party_90 with Dissolve(0.3)
    if juice_orange == True:
        scene cm_party_91 with Dissolve(0.3)
    if juice_pineapple == True:
        scene cm_party_92 with Dissolve(0.3)
    if juice_cherry == True:
        scene cm_party_93 with Dissolve(0.3)
    li 2 "等等，你的意思是她们还会陪他睡？" with dissolve
    li 2 "也许只是陪聊，像个男公关一样。"
    li 2 "这在现在的年轻人里其实挺吃香的工作。"
    scene cm_party_94 with Dissolve(0.3)
    dai 2 "你要是真以为那些人不上她们，可就太天真了。" with dissolve
    dai 2 "换成是你，你会拒绝吗？"
    dai 2 "她们绝大多数都是大美女。"
    scene cm_party_95 with Dissolve(0.3)
    me 2 "[dai]，你可是大帅哥。去应聘啊！" with dissolve
    scene cm_party_96 with Dissolve(0.3)
    dai 2 "滚开！" with dissolve
    if ishti == True:
        scene cm_party_97 with Dissolve(0.3)
    if juice_apple == True:
        scene cm_party_98 with Dissolve(0.3)
    if juice_orange == True:
        scene cm_party_99 with Dissolve(0.3)
    if juice_pineapple == True:
        scene cm_party_76 with Dissolve(0.3)
    if juice_cherry == True:
        scene cm_party_100 with Dissolve(0.3)
    li 2 "[gg]，你真的那么缺钱吗？" with dissolve
    li 2 "就没有别的办法吗？"
    if ishti == True:
        scene cm_party_101 with Dissolve(0.3)
    if juice_apple == True:
        scene cm_party_102 with Dissolve(0.3)
    if juice_orange == True:
        scene cm_party_103 with Dissolve(0.3)
    if juice_pineapple == True:
        scene cm_party_77 with Dissolve(0.3)
    if juice_cherry == True:
        scene cm_party_104 with Dissolve(0.3)
    gg 8 "确实缺。但我还没决定。" with dissolve
    gg 8 "（我肯定不打算去当小姐。不过……也不是完全不可能。）"
    dai 2 "话说……" with dissolve
    if ishti == False:
        scene cm_party_105 with Dissolve(0.3)
    if ishti == True:
        scene cm_party_106 with Dissolve(0.3)
    dai 2 "有没有发现什么有趣的事？" with dissolve
    scene cm_party_107 with Dissolve(0.3)
    dai 2 "好像已经有人喝趴了。" with dissolve
    scene cm_party_108 with Dissolve(0.3)
    pause 1.5
    scene cm_party_109 with Dissolve(0.3)
    pause 0.5
    da 3 "{cps=5}……{/cps}"
    dai 2 "{cps=5}……{/cps}"
    scene cm_party_110 with Dissolve(0.3)
    dai 2 "靠，我还以为他睡着了。" with dissolve
    play sound zahvat_1 volume 0.3
    scene cm_party_111 with vpunch
    da 3 "谁给我再倒一杯？！" with dissolve
    play sound woosh2 volume 0.3
    scene cm_party_112 with Dissolve(0.3)
    me 2 "别总说丧气话！" with dissolve
    da 3 "敬我的健康！" with dissolve
    dai 2 "敬我们所有人！" with dissolve
    $ renpy.music.set_volume(0.3, delay=2, channel=u'music2')
    scene black with Dissolve(1.0)
    pause 1.0
    $ renpy.music.set_volume(1, delay=3, channel=u'music2')
    pause 1.0

    if ishti == True:

        scene cm_party_113 with Dissolve(1.0)
        pause 2.0
        scene cm_party_114 with Dissolve(0.5)
        gg t8 "呃……几点了？" with dissolve
        scene cm_party_115 with Dissolve(0.3)
        gg 8 "{cps=5}……{/cps}" with dissolve
        show cm_party_118 with Dissolve(0.3)

    if ishti == False:
        scene cm_party_116 with Dissolve(1.0)
        pause 2.0
        scene cm_party_117 with Dissolve(0.5)
        pause 0.5
        gg 8 "{cps=5}……{/cps}" with dissolve
        show cm_party_118 with Dissolve(0.3)
        gg 8 "（不过……她还是喝了一点。）" with dissolve
        gg 8 "你没事吧？"
        li 2 "{cps=8}[gg]{cps=5}……{/cps} {cps=8}你怎么不喝？{/cps}" with dissolve
        gg 8 "我不想喝。" with dissolve

    pause 1.5
    gg 8 "[li]？" with dissolve
    gg 8 "{cps=5}……{/cps}"
    li 2 "{cps=5}……{/cps}" with dissolve
    menu:
        "叫醒她":
            pause 1.0
            gg 8 "[li]！" with vpunch
    li 2 "嗯？" with dissolve
    gg 8 "你没事吧？" with dissolve
    li 2 "{cps=5}……{/cps}" with dissolve
    scene cm_party_119 with Dissolve(0.3)
    li 2 "我没事……别担心。" with dissolve
    scene cm_party_120 with Dissolve(0.3)
    li 2 "你干嘛这么生气？" with dissolve
    scene cm_party_121 with Dissolve(0.3)
    gg 8 "我没生气。不过今晚就到此为止吧。" with dissolve
    da 3 "这还能解释……" with dissolve
    show cm_party_122 with Dissolve(0.1)
    $ renpy.pause(2,hard=True)
    $ skip_dialogue_label = "classmates_party_2"
    $ skip_dialogue = True
    scene cm_party_123 with Dissolve(0.3)
    da 3 "男人是什么。" with dissolve
    scene cm_party_124 with Dissolve(0.3)
    da 3 "对她们来说……你看……天性。" with dissolve
    scene cm_party_125 with Dissolve(0.3)
    da 3 "天性……我懂了！" with dissolve
    scene cm_party_126 with Dissolve(0.3)
    da 3 "男人需要某种东西……" with dissolve
    scene cm_party_127 with Dissolve(0.3)
    da 3 "带一张长椅背的，这样他能坐着。" with dissolve
    scene cm_party_128 with Dissolve(0.3)
    da 3 "有了它能跑得更快。" with dissolve
    scene cm_party_129 with Dissolve(0.3)
    da 3 "还有那个东西……" with dissolve
    da 3 "就是马呀。"
    da 3 "它吃干草！"
    scene cm_party_130 with Dissolve(0.3)
    da 3 "那不就是烧焦的草吗？里面什么都没有！" with dissolve
    scene cm_party_131 with Dissolve(0.3)
    da 3 "没有蛋白质，啥都没有。"
    play sound swing2 volume 0.5
    show cm_party_132 with Dissolve(0.2):
        zoom 1.2 xalign 0.5 yalign 0.5
        easein 0.2 zoom 1.0
    da 3 "可它他妈结实得很！" with dissolve
    scene cm_party_133 with Dissolve(0.3)
    da 3 "要是你一辈子都吃干草，会变成什么样？！" with dissolve
    scene cm_party_134 with Dissolve(0.3)
    da 3 "一天就死了！" with dissolve
    scene cm_party_135 with Dissolve(0.3)
    da 3 "可那东西，妈的……" with dissolve
    scene cm_party_136 with vpunch
    da 3 "哒哒哒哒——它能跑啊，混蛋！"
    play sound3 woosh2 volume 0.8
    scene cm_party_137 with PushMove(0.1, 'pushright')
    dai 2 "[da]，我跟你讲。首先，马需要很多照顾……" with dissolve
    play sound2 woosh3 volume 0.8
    scene cm_party_138 with PushMove(0.1, 'pushleft')
    da 3 "它自己能活！" with dissolve
    play sound3 woosh2 volume 0.8
    scene cm_party_139 with PushMove(0.1, 'pushright')
    dai 2 "瘦得跟柴火棍似的，还浑身是屎！" with dissolve
    play sound2 woosh3 volume 0.8
    scene cm_party_140 with PushMove(0.1, 'pushleft')
    da 3 "那是野马！野马在没有人之前也活了那么久！野马根本不需要人！" with dissolve
    play sound3 woosh2 volume 0.8
    scene cm_party_141 with PushMove(0.1, 'pushright')
    dai 2 "它们瘦骨嶙峋还浑身是泥！" with dissolve
    play sound2 woosh3 volume 0.8
    scene cm_party_138 with PushMove(0.1, 'pushleft')
    da 3 "斑马谁照顾？！" with dissolve
    scene cm_party_142 with Dissolve(0.3)
    da 3 "它们根本不在乎人类！" with dissolve
    scene cm_party_140 with Dissolve(0.3)
    da 3 "斑马谁照顾？！" with dissolve
    scene cm_party_143 with Dissolve(0.3)
    da 3 "可照样坚韧得很！" with dissolve
    play sound3 woosh2 volume 0.8
    scene cm_party_144 with PushMove(0.1, 'pushright')
    dai 2 "斑马？！" with dissolve
    play sound2 woosh3 volume 0.8
    scene cm_party_145 with PushMove(0.1, 'pushleft')
    da 3 "对！" with dissolve
    play sound3 woosh2 volume 0.8
    scene cm_party_139 with PushMove(0.1, 'pushright')
    dai 2 "斑、斑马……斑马是脆弱的动物！" with dissolve
    play sound2 woosh3 volume 0.8
    scene cm_party_146 with PushMove(0.1, 'pushleft')
    da 3 "斑马是脆弱的动物？！" with dissolve
    scene cm_party_147 with vpunch
    da 3 "你才是脆弱的动物！"
    play sound3 woosh2 volume 0.8
    scene cm_party_137 with PushMove(0.1, 'pushright')
    dai 2 "你见过有人骑斑马吗？！" with dissolve
    play sound2 woosh3 volume 0.8
    scene cm_party_145 with PushMove(0.1, 'pushleft')
    da 3 "你要是站在斑马旁边，它会直接顶你嘴，我发誓！" with dissolve
    play sound3 woosh2 volume 0.8
    scene cm_party_139 with PushMove(0.1, 'pushright')
    dai 2 "这跟现在说的有什么关系？！这匹斑马……你见过有人骑吗？！" with dissolve
    play sound2 woosh3 volume 0.8
    scene cm_party_143 with PushMove(0.1, 'pushleft')
    da 3 "根本不用骑！重点是——它存在！它存在啊！" with dissolve
    play sound as1 volume 0.8
    scene cm_party_148 with vpunch
    me 2 "够了，你们他妈给我闭嘴！"
    me 2 "我脑袋都被你吵疼了。"
    play sound3 swing1 volume 0.5
    scene cm_party_142 with vpunch
    da 3 "我发誓，这事我们回头再算。" with dissolve
    play sound2 woosh3 volume 0.8
    scene cm_party_139 with PushMove(0.1, 'pushright')
    dai 2 "哦，我们一定会算的。" with dissolve
    $ skip_dialogue = False
    play sound3 woosh2 volume 0.8
    scene cm_party_147 with PushMove(0.1, 'pushleft')
    da 3 "我保证会跟你算清楚的，该死。" with dissolve
    jump classmates_party_2
    
label classmates_party_2:
    $ skip_dialogue = False
    scene cm_party_149 with Dissolve(1.0)
    gg 8 "{cps=5}……{/cps}"
    scene cm_party_150 with Dissolve(0.3)
    li 2 "[gg]，有件事我很好奇……" with dissolve
    scene cm_party_151 with Dissolve(0.3)
    li 2 "是问你容不容易被惹毛吗？" with dissolve
    show cm_party_152 with Dissolve(0.3)
    $ choice_var = 1
    $ classmates_party_choice_1 = []
    menu classmates_party_choice_1:
        set classmates_party_choice_1
        "非常容易。\\n[red](莉莲 -2)":
            gg 8 "非常容易。"
            gg 8 "我这人一点就着。"
            $ love_li -= 2
            gg 8 "你只要干点恶心我的事，我马上就想杀人。"
            scene cm_party_153 with Dissolve(0.3)
            li 2 "哈……我看你是在耍我。你不像是那种爱生气的人。"
            show cm_party_152 with Dissolve(0.3)
            gg 8 "大概是彼此还不够了解吧。"
            scene cm_party_153 with Dissolve(0.3)
            li 2 "我们可以改善。"
            pause 1.0

        "「我不太容易被惹毛。」\\n[gold](莉莲 +2)":
            gg 8 "我不太容易被惹毛。"
            gg 8 "要是我遇上什么倒霉事，不是我的错，就是我也无能为力。"
            gg 8 "不管哪种，都得想办法应对——发泄的方式有很多种。"
            $ love_li += 2
            show screen rel_up_lillian
            scene cm_party_154 with Dissolve(0.3)
            li 2 "这样挺好！我最讨厌急性子。"

        "「看情况吧。」":
            gg 8 "不好说……"
            gg 8 "{cps=5}……{/cps}"
            gg 8 "大概看情况吧。还没发生过什么恶心到能让我真正生气的事。"
            gg 8 "（除非把梦里那些事算进去。）"
            scene cm_party_155 with Dissolve(0.3)
            li 2 "懂了。"

        "「你为什么问这个？」\\n[blue](更多内容)":
            gg 8 "你为什么问这个？"
            scene cm_party_156 with Dissolve(0.3)
            li 2 "只是好奇……"
            show cm_party_152 with Dissolve(0.3)
            gg 8 "真的？"
            scene cm_party_157 with Dissolve(0.3)
            li 2 "对、对！真的！"
            scene cm_party_158 with Dissolve(0.3)
            li 2 "那你觉得呢？"
            scene cm_party_159 with Dissolve(0.3)
            li 2 "你容易冲动吗？"
            show cm_party_152 with Dissolve(0.3)
            jump classmates_party_choice_1

    scene cm_party_151 with Dissolve(0.3)
    li 2 "你以前交过男朋友吗？"
    show cm_party_152 with Dissolve(0.3)
    gg 8 "才不要。"
    scene cm_party_156 with Dissolve(0.3)
    li 2 "在原来的学校没有喜欢的人吗？"
    show cm_party_152 with Dissolve(0.3)
    gg 8 "我们家老搬家，所以我换了好几所学校。"
    gg 8 "班上是有可爱的女生，但我一直没时间好好了解她们。"
    scene cm_party_159 with Dissolve(0.3)
    li 2 "但这一次……"
    show cm_party_152 with Dissolve(0.3)
    gg 8 "这次，我希望[may]和我至少能待满一年。"
    gg 8 "尤其现在我们得自己撑起一个家了。是时候停止东奔西走，好好活一活了。"
    gg 8 "（我们之所以老搬家，是因为爸爸的工作。）"
    gg 8 "（就好像在寻找什么……或者在逃避什么。）"
    gg 8 "（但现在他已经不在了……）"
    gg 8 "{cps=5}……{/cps}"
    gg 8 "只剩一年，学业就结束了。"
    gg 8 "看来我永远不会知道那种「电影里的高中生活」是什么感觉了。"
    gg 8 "不过话说回来，拥有的东西还是得好好享受，对吧？"
    scene cm_party_154 with Dissolve(0.3)
    li 2 "没错！"
    show cm_party_152 with Dissolve(0.3)
    gg 8 "那你呢？"
    scene cm_party_156 with Dissolve(0.3)
    li 2 "你是问我会不会一直留在这所学校？"
    show cm_party_152 with Dissolve(0.3)
    gg 8 "不是。"
    gg 8 "不是。我是说——你交过男朋友吗？"
    scene cm_party_153 with Dissolve(0.3)
    li 2 "哦，你是指那个……"
    scene cm_party_162 with Dissolve(0.3)
    li 2 "唉，我还有点醉，话也太多了。"
    scene cm_party_155 with Dissolve(0.3)
    li 2 "不过……{w=0.8}嗯，我交过。"
    show cm_party_152 with Dissolve(0.3)
    gg 8 "那家伙是个混蛋吗？"
    scene cm_party_159 with Dissolve(0.3)
    li 2 "哇，好敏锐。"
    scene cm_party_155 with Dissolve(0.3)
    li 2 "不过他大概也会这么说我——或者更难听。"
    show cm_party_152 with Dissolve(0.3)
    gg 8 "在这儿，他的看法不重要。"
    scene cm_party_160 with Dissolve(0.3)
    li 2 "哈！有道理。"
    show cm_party_152 with Dissolve(0.3)
    li 2 "{cps=5}……{/cps}"
    scene cm_party_156 with Dissolve(0.3)
    li 2 "那么……你现在觉得我怎么样？"
    show cm_party_152 with Dissolve(0.3)
    menu:
        "「真没想什么。」":
            gg 8 "真没想什么。"
            scene cm_party_159 with Dissolve(0.3)
            li 2 "一点都没想？"
            show cm_party_152 with Dissolve(0.3)
            gg 8 "现在手头事情太多了……而且我急着要钱。"
            gg 8 "脑子里几乎全是这些。"
            scene cm_party_157 with Dissolve(0.3)
            li 2 "哦，对。抱歉提这个。"
            show cm_party_163 with Dissolve(0.3)
            gg 8 "别误会——你肯定是个很棒的女孩。"
            gg 8 "只是……我现在不想那种事。"
            li 2 "{cps=5}……{/cps}"

        "[red]「妆可能化得有点过了。」\\n[red](莉莲 -2)[blue] 或 [red](莉莲 -4)":
            gg 8 "……我觉得你的妆可能化得有点过了。"
            scene cm_party_161 with Dissolve(0.3)
            li 2 "那个。我只是……"
            scene cm_party_162 with Dissolve(0.3)
            li 2 "我只是想换个风格试试。"
            show cm_party_163 with Dissolve(0.3)
            gg 8 "看起来有点太招摇了。"
            gg 8 "可能是因为[may]基本不化妆，我也没资格评价太多，不过……"
            gg 8 "别担心，你还是很好看的！"
            gg 8 "我觉得只是稍微有点过头了。"
            $ love_li -= 2
            if lillian_compliment_appearance == True:
                scene cm_party_157 with Dissolve(0.3)
                li 2 "等等。我们刚见面的时候，你不是说挺好看的吗？"
                show cm_party_163 with Dissolve(0.3)
                gg 8 "我一开始也这么觉得。"
                gg 8 "乍一看没什么问题。"
                gg 8 "但现在总觉得太招摇了。"
                $ love_li -= 2
                scene cm_party_153 with Dissolve(0.3)
                li 2 "好，我知道了。"
                show cm_party_163 with Dissolve(0.3)
                li 2 "{cps=5}……{/cps}"
                gg 8 "我不是想伤你的感情。只是跟不太熟的人，我更喜欢直说。"
                gg 8 "从一开始就坦诚相待比较好。"
                gg 8 "不管怎么说，能多了解彼此一点总归是好的。"

        "[gr]「幸好你来了。」\\n[gold](莉莲 +1)[blue] 或 [gold](莉莲 +4)":
            gg 8 "幸好你来了，[li]。"
            gg 8 "想想我要是一个人来的话"
            gg 8 "我跟这群白痴还能聊什么？斑马？"
            $ love_li += 1
            show screen rel_up_lillian
            scene cm_party_158 with Dissolve(0.3)
            li 2 "很高兴有我陪着你！"
            if lillian_compliment_appearance == True:
                scene cm_party_151 with Dissolve(0.3)
                li 2 "你说我今天这身好看。"
                scene cm_party_155 with Dissolve(0.3)
                li 2 "其实我还挺紧张的……"
                scene cm_party_159 with Dissolve(0.3)
                li 2 "我平时并不是这样的，突然这样打扮自己。"
                scene cm_party_154 with Dissolve(0.3)
                li 2 "所以，谢谢你！"
                $ love_li += 3
                show screen rel_up_lillian
                show cm_party_152 with Dissolve(0.3)
                gg 8 "只是说了实话，不用谢。你美极了！"

    li 2 "{cps=5}……{/cps}"
    scene cm_party_164 with Dissolve(0.3)
    li 2 "说点关于你自己的事吧。"
    show cm_party_165 with Dissolve(0.3)
    gg 8 "关于我……"
    gg 8 "你到底想知道什么？"
    li 2 "{cps=5}……{/cps}"
    scene cm_party_166 with Dissolve(0.3)
    li 2 "女生身上你最看重哪三个优点？"
    show cm_party_165 with Dissolve(0.3)
    gg 8 "嗯……得小心别说得太像性别歧视。"
    scene cm_party_164 with Dissolve(0.3)
    li 2 "哎呀，[gg]，你肯定能答得很好的！"
    show cm_party_165 with Dissolve(0.3)
    gg 8 "你说的是外表还是性格？"
    scene cm_party_167 with Dissolve(0.3)
    li 2 "{cps=5}……{/cps}"
    scene cm_party_168 with Dissolve(0.3)
    li 2 "先从外表开始吧。"
    scene cm_party_169 with Dissolve(0.3)
    li 2 "黑发还是金发？"
    show cm_party_165 with Dissolve(0.3)
    gg 8 "我眼前就坐着一个金发美女。正确答案当然是金发。"
    scene cm_party_170 with Dissolve(0.3)
    li 2 "我喜欢——举一反三！"
    scene cm_party_171 with Dissolve(0.3)
    li 2 "不过行吧，这次你可以说实话。我保证不会打你。"
    show cm_party_172 with Dissolve(0.3)
    li 2 "{cps=5}……{/cps}"
    scene cm_party_173 with Dissolve(0.3)
    li 2 "所以……你更喜欢黑发？"
    show cm_party_172 with Dissolve(0.3)
    menu:
        "「我更喜欢金发。」\\n[gold](莉莲 +2)":
            gg 8 "我更喜欢金发。"
            $ lillian_choice_blond = True
            scene cm_party_174 with Dissolve(0.3)
            li 2 "所以我是你喜欢的类型？"
            show cm_party_175 with Dissolve(0.3)
            gg 8 "毫无疑问。"
            scene cm_party_176 with Dissolve(0.3)
            $ love_li += 2
            show screen rel_up_lillian
            li 2 "*窃笑* 我就知道！"
            
        "「我更喜欢黑发。」":
            gg 8 "我更喜欢黑发。她们有种神秘……撩人的味道。"
            $ lillian_choice_brunet = True
            scene cm_party_177 with Dissolve(0.3)
            li 2 "欣赏你的坦率，[gg]。"
            
        "「发色对我来说无所谓。」\\n[gold](莉莲 +1)":
            gg 8 "发色对我来说无所谓。"
            $ lillian_choice_allhaircolors = True
            gg 8 "金发、黑发、红发——每一种都有自己的美。"
            $ love_li += 1
            show screen rel_up_lillian
            scene cm_party_178 with Dissolve(0.3)
            li 2 "你这是想鱼与熊掌兼得。你只是不想伤害任何人的感情，对吧？"
    
    play sound swing1 volume 0.3
    scene cm_party_179 with Dissolve(0.3)
    li 2 "呃……为什么我的脸颊还在发烫……"
    show cm_party_180 with Dissolve(0.3)
    gg 8 "大概是酒精的关系吧。不过……也可能是别的原因。"
    gg 8 "你经常喝酒吗？"
    scene cm_party_181 with Dissolve(0.3)
    li 2 "其实……这是我第二次喝酒。"
    scene cm_party_182 with Dissolve(0.3)
    li 2 "能给我来点冰的吗？"
    scene cm_party_183 with Dissolve(0.3)
    cm_barmen "「蓝湖」、「乌龙茶」、「沙滩之春」？"
    scene cm_party_184 with Dissolve(0.3)
    li 2 "无所谓，哪杯快上哪杯。"
    show cm_party_185 with Dissolve(0.3)
    cm_barmen "知道了，马上就来。"
    scene cm_party_186 with Dissolve(0.3)
    li 2 "你喜欢日落吗？"
    show cm_party_175 with Dissolve(0.3)
    menu:
        "[gr]「当然了。谁不喜欢呢？」":
            gg 8 "当然了。谁不喜欢呢？"
            scene cm_party_187 with Dissolve(0.3)
            li 2 "我给你看个东西。"
            $ lillian_choice_sunset = True
            scene cm_party_188 with Dissolve(0.3)
            li 2 "来，看。"
            scene cm_party_189 with Dissolve(0.3)
            gg 8 "这是你自己拍的？"
            scene cm_party_190 with Dissolve(0.3)
            li 2 "对。"
            scene cm_party_191 with Dissolve(0.3)
            pause 0.3
            scene cm_party_192 with Dissolve(0.3)
            li 2 "唔，这个可算不上日落……"
            li 2 "只是……我以前在学校拍的一张照片。"
            gg 8 "拍得不错，你挺有天赋的。"
            li 2 "*窃笑* 谢谢……"
            scene cm_party_193 with Dissolve(0.3)
            pause 0.3
            scene cm_party_194 with Dissolve(0.3)
            pause 1.0
            play sound woosh2 volume 0.5
            show cm_party_195 with Dissolve(0.2):
                zoom 0.8 xalign 0.5 yalign 0.5
                easein 0.2 zoom 1.0
            li 2 "哎呀……"
            
        "[gr]「没有啊。每天都这样。」":
            gg 8 "没有啊。每天都这样。有什么特别的？"
            scene cm_party_186 with Dissolve(0.3)
            li 2 "喂！天天都能看到，不代表就不美了。"
            
    play sound glass_bottles_3 volume 0.8
    scene cm_party_196 with Dissolve(0.1)
    cm_barmen "你的「不夜城」。"
    li 2 "谢啦！"
    show cm_party_197 with Dissolve(0.3)
    pause 2.0
    li 2 "{cps=5}……{/cps}" with dissolve
    li 2 "嗯嗯！"
    li 2 "好喝！"
    me 2 "喂，[dai]，快看[li]。" with dissolve
    scene cm_party_198 with Dissolve(0.3)
    me 2 "你不觉得她一直在盯着那个新来的小子看吗？" with dissolve
    scene cm_party_199 with Dissolve(0.3)
    dai 2 "你这人真是想太多……" with dissolve
    dai 2 "不过……他们俩肯定有点什么。"
    play sound woosh1 volume 0.6
    show cm_party_200 with Dissolve(0.3):
        zoom 0.8 xalign 0.5 yalign 0.5
        easein 0.3 zoom 1.0
    me 2 "我从没见过[li]这样——整个人都在发光！" with dissolve
    scene cm_party_201 with hpunch
    dai 2 "嘘，小声点！"
    scene cm_party_202 with hpunch
    li 2 "你们两个在嘀咕什么呢？！我以前可从没在派对上见过你！" with dissolve
    scene cm_party_203 with Dissolve(0.3)
    gg 8 "他们喝醉了，别管他们。" with dissolve
    scene cm_party_204 with Dissolve(0.3)
    li 2 "听着……我有个小忙想请你帮。" with dissolve
    scene cm_party_205 with Dissolve(0.3)
    gg 8 "我猜猜看。" with dissolve
    show cm_party_206 with Dissolve(0.3)
    ''
    gg 8 "你想溜出这里？" with dissolve
    scene cm_party_207 with Dissolve(0.3)
    li 2 "对！" with dissolve
    stop music2 fadeout 3
    play music3 japan_streets_2 fadein 6
    scene black with Dissolve(1.0)
    pause 2.0

label party_to_hotel:
    show party_to_hotel_1
    $ renpy.pause(2,hard=True)
    pause 5
    scene party_to_hotel_2 with Dissolve(0.3)
    gg 8 "你早该告诉我你走不动路的。"
    scene party_to_hotel_3 with Dissolve(0.3)
    li 2 "{cps=5}……{/cps}"
    scene party_to_hotel_4 with Dissolve(0.3)
    li 2 "可是我不知道啊……"
    li 2 "我以为我已经酒醒了。"
    scene party_to_hotel_5 with Dissolve(0.3)
    gg 8 "最后那杯鸡尾酒你真不该点的……"
    gg 8 "最后那一杯太猛了。酒就是酒——你当然又会醉。"
    gg 8 "你家住哪儿？"
    scene party_to_hotel_6 with Dissolve(0.3)
    li 2 "我回不了家……"
    scene party_to_hotel_7 with Dissolve(0.3)
    gg 8 "为什么？"
    scene party_to_hotel_8 with Dissolve(0.3)
    li 2 "我就是……回不去……"
    scene party_to_hotel_9 with Dissolve(0.3)
    gg 8 "{cps=5}……{/cps}"
    scene party_to_hotel_10 with Dissolve(0.3)
    ''
    stop music3 fadeout 3
    scene black with Dissolve(1.0)
    pause 2.0
    
label lillian_hotel:
    play music2 lofi_study fadein 5 volume 0.6
    $ aksha -= 70
    scene lillian_hotel_1 with Dissolve(1.0):
        center
        zoom 1.3
        ease 2.0 zoom 1
    pause 2.0
    scene lillian_hotel_2 with Dissolve(0.3)
    gg 8 "（真是的……）"
    gg 8 "（都午夜了，我在旅馆里。躺在旁边的，是那个明显有家庭问题的醉鬼朋友。）"
    scene lillian_hotel_3 with Dissolve(0.3)
    gg 8 "（难道我要把她一个人丢在街上吗？）"
    scene lillian_hotel_4 with Dissolve(0.3)
    gg 8 "（她已经睡着了……）"
    scene lillian_hotel_5 with Dissolve(0.3)
    gg 8 "（算一下……去酒吧的车费 19 美元，旅馆房间 70 美元……）"
    gg 8 "（总共 89 美元。我还剩……$[aksha]。）"
    gg 8 "（唔……）"
    if yumiko_ry and dolg_alexxis == True:
        gg 8 "（早知道还是收下那个金发男的钱好了？）"
        gg 8 "{cps=5}……{/cps}"
        gg 8 "（去他的。我和[yumiko]玩得很开心。）"
        gg 8 "（但我还欠[so] 800 美元。）"
    elif dolg_alexxis == True:
        gg 8 "（我还欠[so] 800 美元。）"
    gg 8 "（每天都有意外开销。得想个办法堵住这个口子。）"
    gg 8 "（[li]该怎么办？带她回我们家倒可以，可是……）"
    gg 8 "（算了。那只会让[li]和[may]都很尴尬。）"
    scene lillian_hotel_6 with Dissolve(0.3)
    gg 8 "{cps=5}……{/cps}"
    scene lillian_hotel_7 with Dissolve(0.3)
    gg 8 "你没事吧？"
    gg 8 "[li]？"
    scene lillian_hotel_8 with Dissolve(0.3)
    li 2 "我好晕……"
    scene lillian_hotel_9 with Dissolve(0.3)
    gg 8 "今天玩得很开心，不过我该走了。"
    scene lillian_hotel_10 with Dissolve(0.3)
    li 2 "你不能就这么走掉……"
    scene lillian_hotel_11 with Dissolve(0.3)
    gg 8 "怎么了？"
    scene lillian_hotel_12 with Dissolve(0.3)
    li 2 "留下来陪我……"
    show lillian_hotel_13 with Dissolve(0.3)
    li 2 "{cps=5}……{/cps}"
    gg 8 "（她自己知不知道在说什么啊？）"
    gg 8 "{cps=5}……{/cps}"
    gg 8 "[li]，你醉了。试着睡吧。"
    scene lillian_hotel_14 with Dissolve(0.3)
    li 2 "别走……"
    li 2 "我现在真的不想一个人。"
    show lillian_hotel_13 with Dissolve(0.3)
    gg 8 "（可恶，要是我留下来……）"
    gg 8 "（我要不要趁这个机会……）"
    show lillian_hotel_15 with Dissolve(0.3):
        center
        zoom 1.3
        ease 0.6 zoom 1
    hide lillian_hotel_13
    call screen lillian_hotel_choice_1
    ## ВЫБОР 
label lillian_hotel_leave:
    pause 0.5
    gg 8 "你现在脑子不清楚。"
    show lillian_hotel_13 with Dissolve(0.3)
    hide lillian_hotel_15
    gg 8 "你需要好好休息。"
    gg 8 "等天亮了就不一样了。"
    gg 8 "别忘了定闹钟——你得回家准备上课。"
    gg 8 "我先走了。明天见。"
    $ lillian_hotel_choice_leave = True
    jump school_lillian_missing
    
label lillian_hotel_stay:
    pause 0.5
    show lillian_hotel_13 with Dissolve(0.3)
    hide lillian_hotel_15
    gg 8 "我等你睡着再走。"
    gg 8 "放轻松。"
    scene lillian_hotel_16 with Dissolve(0.3)
    li 2 "{cps=5}……{/cps}"
    scene lillian_hotel_17 with Dissolve(0.3)
    li 2 "[gg]……"
    scene lillian_hotel_18 with Dissolve(0.3)
    li 2 "是酒精的关系……好吗？"
    scene lillian_hotel_19 with Dissolve(0.3)
    pause 1.5
    scene lillian_hotel_20 with dissolve
    ''
    scene lillian_hotel_21 with dissolve
    li 2 "唔唔……"
    scene lillian_hotel_22 with dissolve
    li 2 "啊……唔嗯……"
    scene lillian_hotel_23 with Dissolve(0.3)
    li 2 "嗯！"
    scene lillian_hotel_24 with Dissolve(0.3)
    li 3 "啊{cps=5}……{/cps}"
    gg 8 "{cps=5}……{/cps}"
    scene lillian_hotel_25 with Dissolve(0.3)
    gg 8 "真是个美人……"
    gg 8 "把手举起来。"
    scene lillian_hotel_26 with dissolve
    ''
    scene lillian_hotel_27 with dissolve
    ''
    scene lillian_hotel_28 with dissolve
    pause 0.5
    gg 8 "该死……这曲线真顺滑！"
    gg 8 "简直是完美。"
    scene lillian_hotel_29 with dissolve
    pause 0.5
    li 3 "哇……"
    scene lillian_hotel_30 with dissolve
    li 3 "你还真是会给女孩惊喜啊！"
    scene lillian_hotel_31 with dissolve
    li 3 "诶？！"
    scene lillian_hotel_32 with dissolve
    li 3 "哈啊……这么着急？"
    scene lillian_hotel_33 with dissolve
    li 3 "等等。"
    scene lillian_hotel_34 with dissolve
    li 3 "我也帮你脱衣服。"
    gg 0 "等一下。"
    scene black with dissolve
    pause 1.0
    scene lillian_hotel_35 with dissolve
    pause 1.0
    li 3 "哎呀……可真不小！"
    scene lillian_hotel_36 with dissolve
    gg 0 "（她盯着我鸡巴看的眼神，让我更兴奋了。）"
    scene lillian_hotel_37 with dissolve
    gg 0 "你的身体简直性感得要命，[li]。"
    scene lillian_hotel_38 with dissolve
    li 3 "看看你这位朋友，就知道你很享受嘛。"
    show lillian_hotel_39 with dissolve
    $ persistent.gallery_lillian = True
    pause 0.5
    call screen lillian_hotel_choice_start

label lillian_hotel_sex_boobs:
    
    scene black with dissolve
    pause 0.8
    show lillian_hotel_40 with dissolve
    hide lillian_hotel_39
    pause 1.0
    gg 0 "[li]……可以摸你的胸吗？"
    li 3 "可以{cps=5}……{/cps}"
    li 3 "随便你。"
    show lillian_hotel_41 with dissolve
    hide lillian_hotel_40
    li 3 "啊……好痒。"
    gg 0 "好软！"
    show lillian_hotel_42 with dissolve
    hide lillian_hotel_41
    li 3 "唔唔……"
    gg 0 "柔软……又有弹性。"
    gg 0 "我还想多玩一会儿。"
    li 3 "啊……"
    show lillian_hotel_43 with dissolve
    hide lillian_hotel_42
    gg 0 "天啊，简直是天堂！"
    li 3 "唔唔……"
    ''
    $ persistent.gallery_lillian_boobs = True
    $ lillian_hotel_choice_boobs_complete = True
    call screen lillian_hotel_choice_start

label lillian_hotel_sex_fingering:
    scene black with Dissolve(0.5)
    pause 0.5
    scene lillian_hotel_98 with vpunch
    li 3 "{cps=5}……{/cps}！"
    scene lillian_hotel_99 with dissolve
    li 3 "诶？"
    scene lillian_hotel_100 with dissolve
    li 3 "喂！"
    scene lillian_hotel_101 with dissolve
    gg 0 "让我让你舒服起来……"
    scene lillian_hotel_102 with dissolve
    gg 0 "用我的手。"
    scene lillian_hotel_103 with dissolve
    li 3 "{cps=5}……{/cps}"
    show lillian_hotel_104 with Dissolve(0.1)
    $ renpy.pause(3.9,hard=True)
    show lillian_hotel_105 with Dissolve(0.3):
        top
        zoom 1.1
        ease 0.6 zoom 1
    hide lillian_hotel_104
    play voice2 voice_lillian_fingering_1 fadein 2
    li 3 "呀！"
    ''
    li 3 "啊啊……你的手指动得好快……"
    gg 0 "（我可以更快。）"
    ''
    show lillian_hotel_106 with Dissolve(0.1)
    hide lillian_hotel_105
    stop voice2 fadeout 1
    play voice3 voice_lillian_fingering_2
    li 3 "嗯……"
    $ love_li += 2
    show screen rel_up_lillian
    li 3 "啊……[gg]！"
    ''
    stop voice3 fadeout 2
    show lillian_hotel_107 with Dissolve(0.1)
    hide lillian_hotel_106
    $ renpy.pause(3.9, hard=True)
    gg 0 "看来你很享受嘛。"
    gg 0 "你都已经湿了。"
    show lillian_hotel_108 with Dissolve(0.1)
    hide lillian_hotel_107
    $ renpy.pause(0.9, hard=True)
    li 3 "唔……"
    play voice2 voice_lillian_fingering_1 fadein 1
    play sound2 lillian_hotel_109_sound loop
    show lillian_hotel_109 with Dissolve(0.1)
    hide lillian_hotel_108
    pause 1.0
    li 3  "等、等一下……"
    stop voice2 fadeout 1
    stop sound2 fadeout 1
    play voice3 voice_lillian_fingering_2 fadein 1
    play sound3 lillian_hotel_110_sound loop
    show lillian_hotel_110 with Dissolve(0.1)
    hide lillian_hotel_109
    pause 0.5
    li 3  "天啊……太多了……"
    li 3  "求你了，停下！"
    show lillian_hotel_111 with Dissolve(0.1)
    hide lillian_hotel_110
    pause 0.5
    li 3  '啊……'
    ''
    stop sound3 fadeout 1
    stop voice3 fadeout 4
    show lillian_hotel_112 with Dissolve(0.3)
    hide lillian_hotel_111
    $ renpy.pause(3.1,hard=True)
    show lillian_hotel_113 with Dissolve(0.1)
    hide lillian_hotel_112
    pause 1.0
    $ persistent.gallery_lillian_fingering = True
    $ lillian_hotel_choice_fingering_complete = True
    $ lillian_hotel_choice_handjob_unlock = True
    call screen lillian_hotel_choice_start

label lillian_hotel_sex_lick:

    scene black with dissolve
    pause 0.8
    show lillian_hotel_44 with dissolve
    gg 0 "放松，让我来伺候你。"
    li 3 "{cps=5}……{/cps}"
    show lillian_hotel_45 with dissolve
    hide lillian_hotel_44
    ''
    play voice1 voice_lillian_hotel_moan1 volume 0.5
    show lillian_hotel_46 with dissolve
    hide lillian_hotel_45
    li 3 "嗝！"
    $ love_li += 3
    show screen rel_up_lillian
    li 3 "啊……"
    li 3 "等、等一下！"
    li 3 "唔唔……"
    show lillian_hotel_47 with dissolve
    hide lillian_hotel_46
    li 3 "停、停下……求你了……啊！"
    li 3 "求你了，停下！"
    li 3 "我……我什么都依你！"
    li 3 "哈啊……哈啊……"
    stop voice1 fadeout 1
    show lillian_hotel_48 with dissolve
    hide lillian_hotel_47
    gg 0 "什么都依我？……"
    gg 0 "那么……"
    $ persistent.gallery_lillian_lick = True
    $ lillian_hotel_choice_lick_complete = True
    $ lillian_hotel_choice_handjob_unlock = True
    call screen lillian_hotel_choice_start

label lillian_hotel_sex_handjob:
    pause 0.5
    gg 0 "来吧，[li]……用你的手。"
    li 3 "{cps=5}……{/cps}好。"
    scene black with dissolve
    pause 1.0
    show lillian_hotel_49 with Dissolve(0.3)
    $ renpy.pause(3.5,hard=True)
    show lillian_hotel_50 with dissolve
    hide lillian_hotel_49
    pause 0.5
    li 3 "天啊……[gg]{cps=5}……{/cps}"
    li 3 "我的手掌……好烫……"
    ''
    show lillian_hotel_51 with dissolve
    hide lillian_hotel_50
    ''
    show lillian_hotel_52 with dissolve
    hide lillian_hotel_51
    ''
    gg 0 "就是这样……再快一点，[li]。"
    show lillian_hotel_53 with dissolve
    hide lillian_hotel_52
    ''
    show lillian_hotel_54 with dissolve
    hide lillian_hotel_53
    ''
    show lillian_hotel_55 with dissolve
    hide lillian_hotel_54
    ''
    $ persistent.gallery_lillian_handjob = True
    $ lillian_hotel_choice_handjob_complete = True
    $ lillian_hotel_choice_footjob_unlock = True
    $ lillian_hotel_choice_blowjob_unlock = True
    call screen lillian_hotel_choice_start
            
label lillian_hotel_sex_footjob_from_handjob:
    pause 0.5
    gg 0 "我想操你的脚。"
    scene lillian_hotel_74 with dissolve
    li 3 "诶？我的脚？"
    scene lillian_hotel_75 with dissolve
    gg 0 "你愿意那样做吗？"
    scene lillian_hotel_76 with dissolve
    li 3 "……我试试看。"
    jump lillian_hotel_sex_footjob

label lillian_hotel_sex_footjob_from_blowjob:
    pause 0.5
    gg 0 "我想操你的脚。"
    jump lillian_hotel_sex_footjob

label lillian_hotel_sex_footjob:
    scene black with Dissolve(0.5)
    pause 1.0
    show lillian_hotel_56 with dissolve
    pause 0.5
    li 3 "你想这样吗？"
    gg 0 "嗯。"
    ''
    show lillian_hotel_57 with dissolve
    hide lillian_hotel_56
    ''
    show lillian_hotel_58 with dissolve
    hide lillian_hotel_57
    li 3 "你好色……"
    gg 0 "你是想让我羞死人吗？"
    show lillian_hotel_59 with dissolve
    hide lillian_hotel_58
    li 3 "才、才不是！"
    ''
    show lillian_hotel_60 with dissolve
    hide lillian_hotel_59
    li 3 "你真的……喜欢吗？"
    gg 0 "当然啦。你要是能看到从我这边看过去有多性感就好了。"
    li 3 "嘻嘻……色狼。"
    ''
    show lillian_hotel_61 with dissolve
    hide lillian_hotel_60
    ''
    show lillian_hotel_62 with dissolve
    hide lillian_hotel_61
    ''
    show lillian_hotel_63 with dissolve
    hide lillian_hotel_62
    ''
    show lillian_hotel_64 with dissolve
    hide lillian_hotel_63
    ''
    show lillian_hotel_65 with dissolve
    hide lillian_hotel_64
    ''
    show lillian_hotel_66 with dissolve
    hide lillian_hotel_65
    ''
    gg 0 "[li]，脚动得再快一点。"
    show lillian_hotel_67 with dissolve
    hide lillian_hotel_66
    ''
    li 3 "这样？……"
    gg 0 "（可恶……我快……）"
    gg 0 "再快点！"
    show lillian_hotel_68 with dissolve
    hide lillian_hotel_67
    ''
    gg 0 "（对了……快到了……）"
    show lillian_hotel_69 with dissolve
    hide lillian_hotel_68
    ''
    gg 0 "我要去了！"
    li 3 "快点啊，[gg]！"
    show black with Dissolve(0.3)
    pause 0.2
    hide black with Dissolve(0.3)
    show black with Dissolve(0.5)
    pause 0.2
    hide black with Dissolve(0.3)
    show black with Dissolve(0.3)
    pause 0.1
    hide black with Dissolve(0.2)
    show black with Dissolve(0.3)
    pause 0.1
    hide black with Dissolve(0.2)
    show black with Dissolve(0.2)
    pause 0.8
    play sound cumming
    show lillian_hotel_70 with Dissolve(0.3)
    hide black
    hide lillian_hotel_69
    pause 0.5
    li 3 "啊！天啊……你射了好多……"
    li 3 "你的精液弄得我全身都是。"
    li 3 "我得擦干净……"
    $ persistent.gallery_lillian_footjob = True
    $ lillian_hotel_choice_footjob_complete = True
    call screen lillian_hotel_choice_from_footjob
    
label lillian_hotel_sex_blowjob_from_footjob:
    pause 1.0
    gg 0 "含在嘴里。"
    scene lillian_hotel_71 with dissolve
    li 3 "什么？"
    li 3 "可是……要怎么……我不知道怎么做！"
    scene lillian_hotel_72 with dissolve
    gg 0 "试试看嘛。这样我会很舒服的。"
    li 3 "{cps=5}……{/cps}"
    scene lillian_hotel_73 with dissolve
    li 3 "好吧，我试试。"
    jump lillian_hotel_sex_blowjob

label lillian_hotel_sex_blowjob_from_handjob:
    pause 1.0
    gg 0 "把它含进嘴里。"
    scene lillian_hotel_74 with dissolve
    li 3 "什么？"
    li 3 "可是……就是……我不知道怎么做！"
    scene lillian_hotel_75 with dissolve
    gg 0 "试试嘛，会很舒服的。"
    li 3 "{cps=5}……{/cps}"
    scene lillian_hotel_76 with dissolve
    li 3 "好吧，我试试。"
    jump lillian_hotel_sex_blowjob

label lillian_hotel_sex_blowjob:
    scene black with Dissolve(0.5)
    pause 0.5
    play voice1 voice_lillian_hotel_77 fadein 1
    show lillian_hotel_77 with Dissolve(0.5)
    $ renpy.pause(8.5,hard=True)
    play voice2 voice_lillian_hotel_78 fadein 1
    stop voice1 fadeout 1
    show lillian_hotel_78 with Dissolve(0.1)
    hide lillian_hotel_77
    li 3 "嗯{cps=5}……{/cps}"
    gg 0 "（她真的把我含进嘴里了？！）"
    play voice3 voice_lillian_hotel_79 fadein 1
    stop voice2 fadeout 1
    show lillian_hotel_79 with Dissolve(0.5)
    hide lillian_hotel_78
    $ renpy.pause(9.6,hard=True)
    stop voice3 fadeout 1
    play voice1 voice_lillian_hotel_80 fadein 1
    show lillian_hotel_80 with Dissolve(0.1)
    hide lillian_hotel_79
    gg 0 "这感觉太爽了……"
    play sound lillian_hotel_81_sound loop
    show lillian_hotel_81 with Dissolve(0.3)
    hide lillian_hotel_80
    stop voice1 fadeout 1
    stop sound fadeout 1
    $ renpy.pause (5.5,hard=True)
    play voice2 voice_lillian_hotel_82
    show lillian_hotel_82 with Dissolve(0.1)
    hide lillian_hotel_81
    ''
    gg 0 "再多一点！"
    stop voice2 fadeout 1
    play voice3 voice_lillian_hotel_83
    show lillian_hotel_83 with Dissolve(0.3)
    hide lillian_hotel_82
    ''
    gg 0 "我快忍不住了！"
    call screen lillian_hotel_sex_blowjob_cum
    
label lillian_hotel_sex_blowjob_cum_mouth:
    stop voice3 fadeout 1
    play voice2 voice_lillian_hotel_84 noloop volume 0.5
    show lillian_hotel_84 with Dissolve(0.3)
    hide lillian_hotel_83
    $ renpy.pause (3.5,hard=True)
    li 3 "...!"
    $ renpy.pause (2,hard=True)
    if juice_pineapple == True:
        $ love_li += 1
        show screen rel_up_lillian
        scene lillian_hotel_86 with Dissolve(0.3)
        li 3 "嗯嗯……好甜！"
        show lillian_hotel_88 with Dissolve(0.3)
        gg 0 "菠萝汁有用！"
        li 3 "{cps=5}……{/cps}"
        scene lillian_hotel_89 with Dissolve(0.3)
        li 3 "以后要常喝！"
        show lillian_hotel_90 with Dissolve(0.3)
        gg 0 "（以后……常喝？）"
        gg 0 "这话听起来像是在暗示什么。"
        
    if juice_pineapple == False:
        scene lillian_hotel_87 with Dissolve(0.3)
        li 3 "呃……味道好奇怪。"
        show lillian_hotel_88 with Dissolve(0.3)
        gg 0 "哦……真的有那么难喝吗？"
        li 3 "{cps=5}……{/cps}"
        scene lillian_hotel_89 with Dissolve(0.3)
        li 3 "至少我现在知道你是什么味道了。"
        show lillian_hotel_90 with Dissolve(0.3)
        gg 0 "真好。"
        gg 0 "（大概吧。）"
        
    scene lillian_hotel_91 with Dissolve(0.3)
    li 3 "你射了好多……"
    li 3 "不过还是好硬……"
    show lillian_hotel_92 with Dissolve(0.3)
    pause 0.5
    $ persistent.gallery_lillian_blowjob = True
    $ lillian_hotel_choice_blowjob_complete = True
    call screen lillian_hotel_choice_from_blowjob
        
label lillian_hotel_sex_blowjob_cum_face:
    stop voice3 fadeout 1
    show lillian_hotel_85 with Dissolve(0.3)
    hide lillian_hotel_83
    $ renpy.pause (2.8,hard=True)
    play sound cumming
    $ renpy.pause (2.4,hard=True)
    scene lillian_hotel_93 with Dissolve(0.3)
    li 3 "我现在满脑子都是它了。"
    scene lillian_hotel_94 with Dissolve(0.3)
    li 3 "我得去把自己弄干净……"
    play voice1 voice_lillian_hotel_mmm noloop volume 0.5
    scene lillian_hotel_95 with Dissolve(0.3)
    li 3 "嗯嗯。"
    scene lillian_hotel_96 with Dissolve(0.3)
    li 3 "你射了好多……"
    li 3 "不过还是好硬……"
    show lillian_hotel_97 with Dissolve(0.3)
    pause 0.5
    $ persistent.gallery_lillian_blowjob = True
    $ lillian_hotel_choice_blowjob_complete = True
    call screen lillian_hotel_choice_from_blowjob


label lillian_hotel_sex_1:
    
    scene black with Dissolve(0.5)
    pause 1.5
    show lillian_hotel_114 with Dissolve(0.3)
    $ renpy.pause(5.3, hard=True)
    show lillian_hotel_115 with Dissolve(0.3)
    hide lillian_hotel_114
    li 3 "小心点……" with dissolve
    li 3 "以你的尺寸，我怕会很痛。"
    
    show lillian_hotel_116 with Dissolve(0.3)
    hide lillian_hotel_115
    $ renpy.pause(5.3, hard=True)
    show lillian_hotel_117 with Dissolve(0.3)
    hide lillian_hotel_116
    if lillian_hotel_choice_lick_complete and lillian_hotel_choice_fingering_complete:
        gg 0 "你已经湿了——不会痛的。" with dissolve
        gg 0 "放松，好好享受。"
    else:
        gg 0 "放轻松。" with dissolve
        gg 0 "痛的话就告诉我。"
    
    show lillian_hotel_118 with Dissolve(0.3)
    hide lillian_hotel_117
    $ renpy.pause(2.8, hard=True)
    show lillian_hotel_119 with Dissolve(0.2)
    hide lillian_hotel_118
    gg 0 "（好温柔……）" with dissolve
    
    show lillian_hotel_120 with Dissolve(0.3)
    hide lillian_hotel_119
    $ renpy.pause(2.0, hard=True)
    show lillian_hotel_121 with Dissolve(0.2)
    hide lillian_hotel_120
    gg 0 "我要射了。" with dissolve
    
    play sound lillian_hotel_122_sound
    show lillian_hotel_122 with Dissolve(0.2)
    hide lillian_hotel_121
    $ renpy.pause(2.0, hard=True)
    show lillian_hotel_123 with Dissolve(0.2)
    hide lillian_hotel_122
    if lillian_hotel_choice_lick_complete and lillian_hotel_choice_fingering_complete:
        li 3 "啊……" with dissolve
        gg 0 "痛？" with dissolve
        li 3 "不、不痛，只是感觉……" with dissolve
        gg 0 "（我才刚进去一点，就已经能感觉到这股热度……）" with dissolve
        gg 0 "我要再深一点。"
    else:
        li 3 "哦……" with dissolve
        gg 0 "（她里面也太窄了！）" with dissolve
        li 3 "比我想的还要痛……" with dissolve
        gg 0 "要停下吗？" with dissolve
        li 3 "不、不要……继续动……" with dissolve
        
    play voice1 voice_lillian_hotel_moan2 volume 0.4
    play sound2 lillian_hotel_124_sound
    show lillian_hotel_124 with Dissolve(0.1)
    hide lillian_hotel_123
    $ renpy.pause(4.9, hard=True)
    play sound3 lillian_hotel_125_sound loop
    show lillian_hotel_125 with Dissolve(0.3)
    hide lillian_hotel_124
    pause 0.5
    gg 0 "（天啊，她里面好湿！）" with dissolve
    gg 0 "（而且好紧……）"
    li 3 "天啊！" with dissolve
    li 3 "啊……"
    ''
    $ persistent.gallery_lillian_sex1 = True
    $ lillian_hotel_choice_sex1_complete = True
    stop sound3 fadeout 1
    play sound2 lillian_hotel_126_sound
    show lillian_hotel_126 with Dissolve(0.1)
    hide lillian_hotel_125
    $ renpy.pause(0.9, hard=True)
    play sound3 lillian_hotel_127_sound loop
    show lillian_hotel_127 with Dissolve(0.3)
    hide lillian_hotel_126
    li 3 "[gg]……嗯……" with dissolve
    ''
    scene black with Dissolve(0.5)
    pause 0.5
    stop sound3 fadeout 1
    stop voice1 fadeout 1
    play voice2 voice_lillian_hotel_moan2 volume 0.5
    play sound2 lillian_hotel_128_sound loop
    show lillian_hotel_128 with Dissolve(0.3)
    gg 0 "哈？" with dissolve
    gg 0 "看来你挺喜欢的。"
    ''
    show lillian_hotel_129 with Dissolve(0.3)
    hide lillian_hotel_128
    gg 0 "你越夹越紧了。"
    ''
    show lillian_hotel_130 with Dissolve(0.3)
    hide lillian_hotel_129
    li 3 "啊……好……" with dissolve
    li 3 "好深！"
    ''
    show lillian_hotel_131 with Dissolve(0.3)
    hide lillian_hotel_130
    gg 0 "我快了。" with dissolve
    li 3 "对，对！"with dissolve
    ''
    scene black with Dissolve(0.5)
    pause 0.3
    show lillian_hotel_132 with Dissolve(0.3)
    hide lillian_hotel_131
    ''
    gg 0 "要射出来了！" with dissolve
    stop voice2 fadeout 3
    stop sound2 fadeout 1
    play sound3 lillian_hotel_133_sound
    show lillian_hotel_133 with Dissolve(0.3)
    hide lillian_hotel_132
    $ renpy.pause(3.5,hard=True)
    play voice3 voice_lillian_hotel_orgasm noloop
    $ renpy.pause(1.0,hard=True)
    scene black with Dissolve(0.5)
    pause 0.3
    show lillian_hotel_134 with Dissolve(0.3)
    $ renpy.pause(2.1,hard=True)
    show lillian_hotel_135 with Dissolve(0.1)
    hide lillian_hotel_134
    ''
    jump school_lillian_missing

label school_lillian_missing:
    
    stop music2 fadeout 3
    play music3 city_bird volume 0.6 fadein 3
    $ renpy.music.set_volume(1, delay=0, channel=u'music3')
    scene black with Dissolve(1.0)
    pause 2.0
    show school_corrior_dolg_1 with Dissolve(0.5)
    $ renpy.music.set_volume(0.3, delay=3, channel=u'music3')
    $ renpy.pause(4.4, hard=True)
    show school_corrior_dolg_1_1 with Dissolve(0.1)
    hide school_corrior_dolg_1
    pause 2.0
    show school_lillian_missing_1 with Dissolve(0.3)
    $ renpy.pause(3.6, hard=True)
    show school_lillian_missing_2 with Dissolve(0.3)
    teacher 1 "下课，下次见。" with dissolve
    mob 1 "谢谢您的授课！" with dissolve
    scene school_lillian_missing_3 with Dissolve(0.5)
    gg 3 "（[li]今天没来。）" with dissolve
    gg 3 "（她不像是会翘课的人，所以大概是跟昨天的事有关。）"
    scene school_lillian_missing_4 with Dissolve(0.5)
    if lillian_hotel_choice_leave:
        gg 3 "（她是在生我的气吗？）" with dissolve
    else:
        gg 3 "（还是说……她怕我？）" with dissolve
    gg 3 "（可恶……希望她没事……）"
    scene school_lillian_missing_5 with Dissolve(0.5)
    pause 0.5
    scene school_lillian_missing_6 with Dissolve(0.5)
    gg 3 "（没回。）" with dissolve
    gg 3 "（我打了一整天的电话都联系不上她。）"
    gg 3 "{cps=5}……{/cps}"
    scene school_lillian_missing_7 with Dissolve(0.3)
    gg 3 "（要是我做错了什么……）" with dissolve
    if lillian_hotel_choice_leave:
        gg 3 "（我把她一个人丢在旅馆。房间锁着，但不会出什么事吧？）" with dissolve
        gg 3 "（早知道我该留下来的。但谁知道那样会变成什么样。）"
    else:
        gg 3 "（是她主动的，但那真的是她自己的意思，还是酒后失言？）" with dissolve
        gg 3 "（也许她缺席另有原因，但不管怎样……昨晚的事必须说清楚。）"
    scene school_lillian_missing_8 with Dissolve(0.3)
    if lillian_hotel_choice_leave:
        gg 3 "（她喝醉了，而我……该死，这一切都不对劲。）" with dissolve
    else:
        gg 3 "（这是个错误吗？）" with dissolve
        gg 3 "（我是不是该更小心一点，更……体贴一点？）"
    scene school_lillian_missing_9 with Dissolve(0.3)
    leah 1 "呃，[gg]……" with dissolve
    scene school_lillian_missing_10 with Dissolve(0.3)
    gg 3 "哦，嗨，[leah]。" with dissolve
    stop music3 fadeout 3
    play music2 dreams_of_success_loopable_by_chilledmusic volume 0.5 fadein 3
    scene school_lillian_missing_11 with Dissolve(0.3)
    leah 1 "希望我没打扰到你……" with dissolve
    $ renpy.music.set_volume(1, delay=3, channel=u'music3')
    scene school_lillian_missing_12 with Dissolve(0.3)
    leah 1 "不过[li]呢？" with dissolve
    leah 1 "她从来不翘课的……就算身体不舒服也照样会来。"
    show school_lillian_missing_13 with Dissolve(0.3)
    gg 3 "对，[li]……她……我不知道。" with dissolve
    gg 3 "你的意思是她没来上学很反常？"
    scene school_lillian_missing_14 with Dissolve(0.3)
    leah 1 "这让我很担心。" with dissolve
    leah 1 "我可以帮她带作业，可是……没在这里看到她，总觉得怪怪的。"
    show school_lillian_missing_13 with Dissolve(0.3)
    gg 3 "我相信她有她的理由。" with dissolve
    gg 3 "你没跟她联系过吗？"
    scene school_lillian_missing_15 with Dissolve(0.3)
    leah 1 "没、没有，她不接电话。" with dissolve
    scene school_lillian_missing_16 with Dissolve(0.3)
    gg 3 "嗯……" with dissolve
    gg 3 "（至少不是故意不理我。这多少让人安心一点，但还是担心。）"
    gg 3 "（我走的时候她睡得很熟。门也锁了，钥匙就放在显眼的地方……）" with dissolve
    scene school_lillian_missing_17 with Dissolve(0.3)
    gg 3 "坐吧。" with dissolve
    scene school_lillian_missing_18 with Dissolve(0.3)
    leah 1 "你觉得她没事吗？" with dissolve
    show school_lillian_missing_19 with Dissolve(0.3)
    gg 3 "我觉得你想太多了。" with dissolve
    leah 1 "{cps=5}……{/cps}" with dissolve
    scene school_lillian_missing_20 with Dissolve(0.3)
    leah 1 "{cps=5}……{/cps}" with dissolve
    scene school_lillian_missing_21 with Dissolve(0.3)
    leah 1 "[gg]，请你老实告诉我。" with dissolve
    leah 1 "昨天发生什么事了吗？"
    show school_lillian_missing_19 with Dissolve(0.3)
    gg 3 "我们昨天只是在咖啡馆偶遇，聊了几句。" with dissolve
    gg 3 "仅此而已。"
    scene school_lillian_missing_22 with Dissolve(0.3)
    leah 1 "[gg]，你知道我是她朋友。" with dissolve
    leah 1 "还有别的吗？不能再多说一点细节吗？"
    show school_lillian_missing_19 with Dissolve(0.3)
    if not lillian_hotel_choice_leave:
        menu:
            "[gr]告诉她实话":
                pause 0.5
                jump school_lillian_missing_truth
            "隐瞒":
        
                gg 3 "我们就是在咖啡馆吃了顿午饭，聊了些有的没的。没什么特别的。" with dissolve
                scene school_lillian_missing_18 with Dissolve(0.3)
                leah 1 "就算你没撒谎，那也只是你的说法。或者说不定……" with dissolve
                show school_lillian_missing_19 with Dissolve(0.3)
                leah 1 "{cps=5}……{/cps}" with dissolve
                scene school_lillian_missing_22 with Dissolve(0.3)
                leah 1 "[gg]……我知道你们两个之间发生了什么！" with dissolve
                show school_lillian_missing_19 with Dissolve(0.3)
                gg 3 "（她知道了？）" with dissolve
                gg 3 "（那她为什么还要问？）"
            
    menu:
        "[gr]告诉她实话":
            pause 0.5
            if lillian_hotel_choice_leave:
                jump school_lillian_missing_truth_nosex
            else:
                jump school_lillian_missing_truth
            
        "「别插手。」":
            stop music2 fadeout 5
            play music3 city_bird volume 0.3 fadein 5
            gg 3 "[leah]，别往心里去，但请不要插手。这是我和她之间的事。" with dissolve
            leah 1 "{cps=5}……{/cps}" with dissolve
            $ school_lillian_missing_phone_leah_rude = True
            scene school_lillian_missing_23 with Dissolve(0.3)
            leah 1 "{cps=5}……{/cps}对、对不起。我走了。" with dissolve
            
            jump school_lillian_missing_leave
            
        "「等她准备好了再问她吧。」":
            gg 3 "[li]现在需要一点空间。" with dissolve
            gg 3 "你想知道细节的话，等她准备好自己去问她。"
            gg 3 "没有她的同意，我不能什么都告诉你，[leah]。"
            scene school_lillian_missing_23 with Dissolve(0.3)
            leah 1 "{cps=5}……{/cps}好。" with dissolve
        
            jump school_lillian_missing_call

label school_lillian_missing_truth:

    gg 3 "其实……昨晚[li]和我在一起。" with dissolve
    $ school_lillian_missing_phone_leah_know = True
    leah 1 "{cps=5}……{/cps}" with dissolve
    scene school_lillian_missing_24 with Dissolve(0.3)
    leah 1 "在、在一起……你是说你们……" with dissolve
    scene school_lillian_missing_25 with Dissolve(0.3)
    gg 3 "我们上床了。" with dissolve
    scene school_lillian_missing_26 with Dissolve(0.3)
    leah 1 "哦，我……我还以为只是……" with dissolve
    show school_lillian_missing_27 with Dissolve(0.3)
    leah 1 "我们只是接了吻……" with dissolve
    gg 3 "我不是想让你难堪。" with dissolve
    gg 3 "但事情已经发生了，也许她只是觉得害羞。"
    leah 1 "这、这有点……太尴尬了……我……" with dissolve
    leah 1 "这倒是有意思……"
    scene school_lillian_missing_28 with Dissolve(0.3)
    leah 1 "抱歉，我只是……没想到会是这样。" with dissolve
    scene school_lillian_missing_29 with Dissolve(0.3)
    gg 3 "我知道了。" with dissolve
    scene school_lillian_missing_30 with Dissolve(0.3)
    leah 1 "我不追问细节，但……你有没有对她温柔一点？" with dissolve
    scene school_lillian_missing_31 with Dissolve(0.3)
    gg 3 "我不是禽兽，[leah]，别担心。" with dissolve
    gg 3 "我没有伤害她。"
    
    jump school_lillian_missing_call
    
label school_lillian_missing_truth_nosex:

    gg 3 "昨天从咖啡馆出来之后，我和[li]在旅馆房间里。" with dissolve
    gg 3 "她喝醉了……"
    $ school_lillian_missing_phone_leah_know = True
    leah 1 "{cps=5}……{/cps}" with dissolve
    scene school_lillian_missing_24 with Dissolve(0.3)
    leah 1 "在、在一起……在房间里，你们……" with dissolve
    scene school_lillian_missing_25 with Dissolve(0.3)
    gg 3 "不，我们没有做越轨的事。趁人之危那种事，我做不出来。" with dissolve
    gg 3 "别误会，[li]是很美，但我们之间并不一定需要什么浪漫的关系。"
    scene school_lillian_missing_28 with Dissolve(0.3)
    leah 1 "哦，我……" with dissolve
    scene school_lillian_missing_29 with Dissolve(0.3)
    leah 1 "还以为只是接了吻……" with dissolve
    scene school_lillian_missing_25 with Dissolve(0.3)
    gg 3 "我把她留在那里休息了。" with dissolve
    gg 3 "她可能是宿醉，但明天肯定就没事了。"
    scene school_lillian_missing_31 with Dissolve(0.3)
    gg 3 "总之，别担心。" with dissolve
    gg 3 "我绝不会伤害她。"
    
    jump school_lillian_missing_call
    
label school_lillian_missing_call:
    
    play sound call_start
    scene school_lillian_missing_32 with Dissolve(0.3)
    "*[leah]的手机响了。*" with dissolve
    scene school_lillian_missing_33 with Dissolve(0.3)
    leah 1 "[li]？"
    
    menu:
        "接过她的手机":
            scene school_lillian_missing_34 with Dissolve(0.3)
            pause 0.5
            scene school_lillian_missing_35 with Dissolve(0.3)
            gg 3 "[li]，是我，[gg]。" with dissolve
            show school_lillian_missing_36:
                xpos 0
                ease 0.5 xpos -240
            play sound woosh1 volume 0.5
            show school_lillian_missing_37 with Dissolve(0.3):
                xpos 1930
                ease 0.5 xpos 0
            li 4 "[gg]？" with dissolve
            play sound as4 volume 0.3
            scene school_lillian_missing_38 with hpunch
            leah 1 "喂！" with Dissolve(0.3)
            $ school_lillian_missing_phone_leah_took = True

        "要过手机\\n[gr](推荐)":
            scene school_lillian_missing_39 with Dissolve(0.3)
            gg 3 "[leah]，拜托了，让我跟她说句话。" with dissolve
            scene school_lillian_missing_40 with Dissolve(0.3)
            leah 1 "诶？……好、好吧。等一下。" with dissolve
            scene school_lillian_missing_41 with Dissolve(0.3)
            leah 1 "[li]，给你。[gg]想跟你说话。" with dissolve
            scene school_lillian_missing_35 with Dissolve(0.3)
            gg 3 "[li]，是我。" with dissolve
            show school_lillian_missing_36:
                xpos 0
                ease 0.5 xpos -240
            play sound woosh1 volume 0.5
            show school_lillian_missing_37 with Dissolve(0.3):
                xpos 1930
                ease 0.5 xpos 0
            li 4 "嗨。" with dissolve
            
        '「替我问候。」':
            scene school_lillian_missing_39 with Dissolve(0.3)
            gg 3 "替我问候。" with dissolve
            scene school_lillian_missing_40 with Dissolve(0.3)
            leah 1 "[gg]向你问好。" with dissolve
            scene school_lillian_missing_41 with Dissolve(0.3)
            leah 1 "对，他现在跟我在一起。" with dissolve
            scene school_lillian_missing_42 with Dissolve(0.3)
            leah 1 "她也向你问好。" with dissolve
            scene school_lillian_missing_43 with Dissolve(0.3)
            leah 1 "我们很担心。你没事吧？" with dissolve
            show school_lillian_missing_44 with Dissolve(0.3)
            leah 1 "{cps=5}……{/cps}" with dissolve
            li 4 "*听不清*" with dissolve
            scene school_lillian_missing_45 with Dissolve(0.3)
            leah 1 "她没事。" with dissolve
            show school_lillian_missing_44 with Dissolve(0.3)
            leah 1 "{cps=5}……{/cps}" with dissolve
            li 4 "*听不清*" with dissolve
            scene school_lillian_missing_46 with Dissolve(0.3)
            leah 1 "我先走开，我们私下聊。" with dissolve
            
            jump school_lillian_missing_leave
    
    scene school_lillian_missing_48 with Dissolve(0.3)
    gg 3 "你没回我电话。我们得谈谈。" with dissolve
    scene school_lillian_missing_49 with Dissolve(0.3)
    $ school_lillian_missing_phone_lillian_talk = True
    li 4 "嗯，抱歉。我需要点时间消化这一切。" with dissolve
    li 4 "昨天……发生了太多事。太不寻常了……"
    scene school_lillian_missing_50 with Dissolve(0.3)
    gg 3 "我没做错什么吧？……" with dissolve
    scene school_lillian_missing_51 with Dissolve(0.3)
    li 4 "不，[gg]，不是你的错。" with dissolve
    scene school_lillian_missing_52 with Dissolve(0.3)
    li 4 "我喝醉了，然后……我们俩都……" with dissolve
    scene school_lillian_missing_53 with Dissolve(0.3)
    gg 3 "我和[leah]只是想确认你没事。" with dissolve
    scene school_lillian_missing_54 with Dissolve(0.3)
    li 4 "我知道，抱歉让你担心了……" with dissolve
    li 4 "我……本来打算回电话的，但脑子还是一团乱……"
    scene school_lillian_missing_55 with Dissolve(0.3)
    gg 3 "你要是愿意的话，我们可以晚点再谈。" with dissolve
    gg 3 "就我们两个，等你准备好。"
    scene school_lillian_missing_56 with Dissolve(0.3)
    li 4 "好！那我们晚点聊。" with dissolve
    scene school_lillian_missing_57 with Dissolve(0.3)
    gg 3 "嗯，打电话或者见面，你方便就好。" with dissolve
    gg 3 "要我把你还给[leah]吗？"
    scene school_lillian_missing_58 with Dissolve(0.3)
    li 4 "我晚点再打给她，谢谢。" with dissolve
    scene school_lillian_missing_35 with Dissolve(0.3)
    gg 3 "好，那待会儿见。" with dissolve
    scene school_lillian_missing_59 with Dissolve(0.3)
    leah 1 "她怎么样？" with dissolve
    scene school_lillian_missing_60 with Dissolve(0.3)
    gg 3 "她没事。说好晚点回你电话。给你。" with dissolve
    if school_lillian_missing_phone_leah_took == True:
        scene school_lillian_missing_61 with Dissolve(0.3)
        leah 1 "别这样直接抢我手机！" with dissolve
    scene school_lillian_missing_62 with Dissolve(0.3)
    gg 3 "谢谢。" with dissolve
    if school_lillian_missing_phone_leah_took == True:
        scene school_lillian_missing_63 with Dissolve(0.3)
        leah 1 "{cps=5}……{/cps}" with dissolve
    if school_lillian_missing_phone_leah_took == False:
        scene school_lillian_missing_64 with Dissolve(0.3)
        leah 1 "不客气。" with dissolve
        
    jump cafe_minami


label school_lillian_missing_leave:

    scene school_lillian_missing_47 with Dissolve(1.0)
    gg 3 "{cps=5}……{/cps}" with dissolve
    jump cafe_minami

label cafe_minami:

    stop music2 fadeout 3
    play music3 japan_streets_2 fadein 3
    scene black with Dissolve(1.0)
    pause 2.0
    show cafe_minami_1 with Dissolve(0.3)
    $ renpy.pause(4.2,hard=True)
    show cafe_minami_2 with Dissolve(0.1)
    gg 9 "我在等人。" with dissolve
    stop music3 fadeout 5
    play music2 breathe_easy_and_relax_by_musiclfiles fadein 6 volume 0.4
    scene cafe_minami_3 with Dissolve(0.1)
    gg 9 "你晚点再来吧。" with dissolve
    scene cafe_minami_4 with Dissolve(0.3)
    gg 9 "（[mi]应该快到了。）" with dissolve
    gg 9 "（女生迟到是常事，所以目前来说，约会一切顺利。）"
    gg 9 "（不知道她穿便装是什么样子？）"
    show cafe_minami_5 with Dissolve(0.1)
    $ renpy.pause(5.3,hard=True)
    show cafe_minami_6 with Dissolve(0.1)
    hide cafe_minami_5
    $ renpy.pause(2.9,hard=True)
    show cafe_minami_7 with Dissolve(0.1)
    hide cafe_minami_6
    pause 1.0
    play sound3 sms3
    show cafe_minami_chat_may_1:
        alpha 0
        xpos 1400
        ypos 500
        ease 0.3 alpha 1 ypos 600 xpos 1300
    ''
    play sound2 sms2
    show cafe_minami_chat_may_2:
        alpha 0
        xpos 1400
        ypos 500
        ease 0.3 alpha 1 ypos 600 xpos 1300
    show cafe_minami_chat_may_1:
        ease 0.3 ypos 400
    ''
    play sound sms1
    show cafe_minami_chat_mc_1:
        alpha 0
        xpos 1100
        ypos 500
        ease 0.3 alpha 1 ypos 600 xpos 1200
    show cafe_minami_chat_may_2:
        ease 0.3 ypos 400
    show cafe_minami_chat_may_1:
        ease 0.3 ypos 200
    ''
    play sound sms1 volume 0.5
    show cafe_minami_chat_mc_2:
        alpha 0
        xpos 1100
        ypos 500
        ease 0.3 alpha 1 ypos 600 xpos 1200
    show cafe_minami_chat_mc_1:
        ease 0.3 ypos 400
    show cafe_minami_chat_may_2:
        ease 0.3 ypos 200
    show cafe_minami_chat_may_1:
        ease 0.3 alpha 0 ypos 0
    ''
    hide cafe_minami_chat_may_1
    play sound2 sms2 volume 0.5
    show cafe_minami_chat_may_3:
        alpha 0
        xpos 1400
        ypos 500
        ease 0.3 alpha 1 ypos 600 xpos 1300
    show cafe_minami_chat_mc_2:
        ease 0.3 ypos 355
    show cafe_minami_chat_mc_1:
        ease 0.3 ypos 155
    show cafe_minami_chat_may_2:
        ease 0.3 alpha 0 ypos -45
    ''
    hide cafe_minami_chat_may_2
    play sound sms1 volume 0.5
    show cafe_minami_chat_mc_3:
        alpha 0
        xpos 1100
        ypos 500
        ease 0.3 alpha 1 ypos 600 xpos 1200
    show cafe_minami_chat_may_3:
        ease 0.3 ypos 400
    show cafe_minami_chat_mc_2:
        ease 0.3 ypos 150
    show cafe_minami_chat_mc_1:
        ease 0.3 alpha 0 ypos 0
    ''
    hide cafe_minami_chat_mc_1
    play sound sms1 volume 0.5
    show cafe_minami_chat_mc_4:
        alpha 0
        xpos 1100
        ypos 500
        ease 0.3 alpha 1 ypos 600 xpos 1200
    show cafe_minami_chat_mc_3:
        ease 0.3 ypos 400
    show cafe_minami_chat_may_3:
        ease 0.3 ypos 200
    show cafe_minami_chat_mc_2:
        ease 0.3 alpha 0 ypos 0
    ''
    hide cafe_minami_chat_mc_2
    play sound sms1 volume 0.5
    show cafe_minami_chat_mc_5:
        alpha 0
        xpos 1100
        ypos 500
        ease 0.3 alpha 1 ypos 600 xpos 1200
    show cafe_minami_chat_mc_4:
        ease 0.3 ypos 355
    show cafe_minami_chat_mc_3:
        ease 0.3 ypos 155
    show cafe_minami_chat_may_3:
        ease 0.3 alpha 0 ypos -45
    ''
    play sound2 sms2 volume 0.5
    show cafe_minami_chat_may_4:
        alpha 0
        xpos 1400
        ypos 500
        ease 0.3 alpha 1 ypos 600 xpos 1300
    show cafe_minami_chat_mc_5:
        ease 0.3 ypos 355
    show cafe_minami_chat_mc_4:
        ease 0.3 ypos 110
    show cafe_minami_chat_mc_3:
        ease 0.3  alpha 0 ypos -45
    ''
    play sound swing4 volume 0.3
    show cafe_minami_chat_may_4:
        ease 0.3 alpha 0 xpos 1450
    show cafe_minami_chat_mc_5:
        ease 0.3 alpha 0 xpos 1350
    show cafe_minami_chat_mc_4:
        ease 0.3 alpha 0 xpos 1350
    show cafe_minami_chat_mc_3:
        ease 0.3 alpha 0 xpos 1350
    $ renpy.pause(0.3,hard=True)
    hide cafe_minami_chat_may_4
    hide cafe_minami_chat_mc_5
    hide cafe_minami_chat_mc_4
    hide cafe_minami_chat_mc_3
    $ renpy.pause(0.3,hard=True)
    show cafe_minami_8 with Dissolve(0.1)
    hide cafe_minami_7
    stop music2 fadeout 6
    play music3 japan_streets_1 volume 0.5 fadein 3
    play music2 jazz_brunch_by_kevin_macleod fadein 1
    $ renpy.pause(5.9,hard=True)
    show cafe_minami_9 with Dissolve(0.1)
    hide cafe_minami_8
    $ renpy.pause(2.4,hard=True)
    show cafe_minami_10 with Dissolve(0.1)
    hide cafe_minami_9
    stop music3 fadeout 3
    $ renpy.pause(2.9,hard=True)
    show cafe_minami_11 with Dissolve(0.1)
    hide cafe_minami_10
    $ renpy.pause(3.7,hard=True)
    scene cafe_minami_12 with Dissolve(0.1)
    mi 2 "嗨。" with dissolve
    show cafe_minami_13 with Dissolve(0.3)
    $ choice_var = 0
    menu:
        '「很高兴见到你。」':
            gg 9 "很高兴见到你。" with dissolve
            
        '[gr]「你长得像我一个同学。」':
            gg 9 "我从没见过这么年轻又漂亮的老师。" with dissolve
            scene cafe_minami_14 with Dissolve(0.3)
            gg 9 "你长得像我一个同学。" with dissolve
            scene cafe_minami_15 with Dissolve(0.3)
            mi 2 "别恭维我了。不过谢谢。" with Dissolve(0.3)
            $ cafe_minami_look_cm = True
            pause 1.5
        
    $ choice_var = 1
    scene cafe_minami_16 with Dissolve(0.3)
    mi 2 "要喝咖啡吗？" with dissolve
    mi 2 "我请客。"
    scene cafe_minami_17 with Dissolve(0.3)
    gg 9 "一般来说，是男方请女方，不是反过来。" with dissolve
    gg 9 "不过我现在手头真的很紧，所以不拒绝。"
    scene cafe_minami_18 with Dissolve(0.3)
    waitress "晚上好。准备好点单了吗？" with dissolve
    scene cafe_minami_19 with Dissolve(0.3)
    mi 2 "两杯咖啡，还有一块蓝莓巧克力蛋糕。" with dissolve
    scene cafe_minami_20 with Dissolve(0.3)
    mi 2 "还要甜点吗？" with dissolve
    scene cafe_minami_17 with Dissolve(0.3)
    gg 9 "只要咖啡，谢谢。" with dissolve
    scene cafe_minami_21 with Dissolve(0.3)
    mi 2 "再来一份淋上巧克力酱的舒芙蕾。" with dissolve
    scene cafe_minami_22 with Dissolve(0.3)
    gg 9 "看来你很爱吃甜食。" with dissolve
    $ minami_unlock = True
    show screen rel_open_minami
    scene cafe_minami_23 with Dissolve(0.3)
    mi 2 "那份舒芙蕾是给你的。人看着别人吃就会胃口大开。" with dissolve
    stop music2 fadeout 6
    play music3 japan_streets_1 fadein 3 volume 0.3
    scene black with Dissolve(0.5)
    pause 0.5
    scene cafe_minami_24 with Dissolve(0.5)
    mi 2 "那么，[gg]，你猜自己的能力是怎么来的吗？" with dissolve
    show cafe_minami_25 with Dissolve(0.1)
    $ renpy.pause(2.4,hard=True)
    scene cafe_minami_26 with Dissolve(0.3)
    gg 9 "没有。" with dissolve
    gg 9 "也许跟那些噩梦有关。"
    show cafe_minami_27 with Dissolve(0.3)
    gg 9 "可我以前也做过那些梦，这些奇怪的能力却是最近才开始的。" with dissolve
    gg 9 "最明显的就是你看到的那件事。"
    scene cafe_minami_28 with Dissolve(0.3)
    mi 2 "还有别的拥有能力的人。他们大多是没有灵魂、贪婪的怪物。" with dissolve
    scene cafe_minami_29 with Dissolve(0.3)
    mi 2 "冷血，强大得可怕。" with dissolve
    show cafe_minami_30 with Dissolve(0.3)
    gg 9 "听起来完全是胡扯。" with dissolve
    stop music3 fadeout 8
    play music2 the_question_is_quizpackage_by_sascha_ende fadein 4 volume 0.6
    scene cafe_minami_31 with Dissolve(0.3)
    mi 2 "也许吧。但这就是我们必须对普通人隐瞒的现实。" with dissolve
    show cafe_minami_30 with Dissolve(0.3)
    gg 9 "「我们」？你……也有能力？" with dissolve
    gg 9 "你就是因为这个才知道的？"
    scene cafe_minami_32 with Dissolve(0.3)
    mi 2 "要扯远点——不，我没有超自然的能力。但接下来我要说的话，绝对不许告诉别人！" with dissolve
    scene cafe_minami_33 with Dissolve(0.3)
    mi 2 "不过就算说了也没人会信你……" with dissolve
    show cafe_minami_34 with Dissolve(0.3)
    mi 2 "但还是别说得太多为好。" with dissolve
    mi 2 "如果你还想活着的话。"
    show cafe_minami_35 with Dissolve(0.3)
    hide cafe_minami_34
    gg 9 "真有那么严重吗？那我们为什么要在这可能被人听见的咖啡馆里谈这个？" with dissolve
    show cafe_minami_34 with Dissolve(0.3)
    hide cafe_minami_35
    mi 2 "这里看起来挺安全的，又是第一次谈话，我也没注意到有人在看我们。" with dissolve
    mi 2 "而且要是真有人在看，我们早就完蛋了。所以担不担心都没意义。"
    show cafe_minami_35 with Dissolve(0.3)
    hide cafe_minami_34
    gg 9 "真是棒极了。" with dissolve
    show cafe_minami_34 with Dissolve(0.3)
    hide cafe_minami_35
    mi 2 "习惯就好。" with dissolve
    show cafe_minami_35 with Dissolve(0.3)
    hide cafe_minami_34
    mi 2 "{cps=5}……{/cps}" with dissolve
    show cafe_minami_36 with Dissolve(0.3)
    hide cafe_minami_35
    mi 2 "我以前在一家私立研究所工作。" with dissolve
    mi 2 "我们研究的是超自然现象。"
    mi 2 "不管愿不愿意，我知道了些不该知道的事。"
    mi 2 "这是个危险又复杂的话题……"
    show cafe_minami_37 with Dissolve(0.3)
    hide cafe_minami_36
    mi 2 "但我觉得你和它有某种关联。" with dissolve
    show cafe_minami_38 with Dissolve(0.3)
    hide cafe_minami_37
    gg 9 "我不知道自己准备好了没有。" with dissolve
    gg 9 "但如果这能解释我的梦和这些能力，我愿意听。"
    scene cafe_minami_39 with Dissolve(0.3)
    mi 2 "两者之间肯定有关联。" with dissolve
    mi 2 "也有可能你……并不属于那一类。"
    scene cafe_minami_40 with Dissolve(0.3)
    mi 2 "{cps=5}……{/cps}" with dissolve
    show cafe_minami_37 with Dissolve(0.3)
    mi 2 "拥有超自然能力的人，被称为{color=ffa500}信徒。{/color}" with dissolve
    mi 2 "通常来说，这些能力会在与恶魔实体接触的人身上觉醒。"
    mi 2 "他们的人生，介于奇迹与诅咒之间。"
    mi 2 "能力的极限、能力的种类、使用能力的后果——每个人都各不相同。"
    mi 2 "我也不知道他们有多少人，甚至不知道究竟有哪些能力是可能的。"
    mi 2 "你以前说不定就遇到过他们。"
    mi 2 "据我所知，这些能力的代价是……人的灵魂。如果那东西能叫灵魂的话。"
    mi 2 "这个部分至今仍是个未解之谜。"
    show cafe_minami_38 with Dissolve(0.3)
    hide cafe_minami_37
    gg 9 "一个人成为信徒之后，灵魂会怎么样？" with dissolve
    show cafe_minami_37 with Dissolve(0.3)
    hide cafe_minami_38
    mi 2 "没有人确切知道。" with dissolve
    mi 2 "严格来说，我们所谓的「灵魂」，只是指一个人为换取力量而舍弃的东西。"
    
    show cafe_minami_38 with Dissolve(0.3)
    hide cafe_minami_37
    gg 9 "……他们舍弃的究竟是什么？" with dissolve
    show cafe_minami_37 with Dissolve(0.3)
    hide cafe_minami_38
    mi 2 "灵魂。" with dissolve
    show cafe_minami_38 with Dissolve(0.3)
    hide cafe_minami_37
    mi 2 "问题就在这里——连基础概念都还没被研究定义清楚。" with dissolve
    mi 2 "但他们确实舍弃了某种东西。我们姑且称之为灵魂吧。也许它消失了，也许它转移到了别的什么存在那里。"
    mi 2 "但有一点是确定的：人一旦获得这些能力，就会变得冷酷、嗜权、贪婪。"
    mi 2 "信徒会失去人性。"
    
    show cafe_minami_38 with Dissolve(0.3)
    hide cafe_minami_37
    gg 9 "我猜他们是被迫侍奉恶魔的？" with dissolve
    show cafe_minami_37 with Dissolve(0.3)
    hide cafe_minami_38
    mi 2 "他们是自己力量的囚徒，乖顺地随着未知力量的乐起舞。" with dissolve
    mi 2 "当然，一部分原因在于突然获得的力量会让人飘飘然。"
    mi 2 "但这已经超出了普通道德的范畴。所谓恶魔，对这些力量的运用不加任何限制。"
    mi 2 "只要一声令下，就能让暴力在夜里袭击无辜的人。"
    show cafe_minami_38 with Dissolve(0.3)
    hide cafe_minami_37
    gg 9 "那种东西怎么可能存在于地球上？" with dissolve
    show cafe_minami_36 with Dissolve(0.3)
    mi 2 "世界没有看上去那么简单，[gg]。" with dissolve
    mi 2 "而且我怕这一切的根源根本不在地球上。"
    mi 2 "人类自认为进化的顶点，可跟某些存在相比，我们只是……虫子。"
    mi 2 "但我们必须学会对抗他们。不管用什么方法。"
    scene cafe_minami_26 with Dissolve(0.3)
    gg 9 "所以……我到底该拿这个怎么办……" with dissolve
    gg 9 "魔法，能力，力量，还是……不管那东西叫什么？"
    show cafe_minami_36 with Dissolve(0.3)
    mi 2 "也许有办法控制这些力量，或者跟赋予你力量的存在谈判……" with dissolve
    mi 2 "奇怪的是，我并不完全确信你是信徒。"
    mi 2 "你跟他们完全不一样，而且如果你真是信徒，根本不会对这个话题感兴趣。"
    mi 2 "有什么地方对不上……"
    mi 2 "也许你的力量来源不同，或者……还不清楚。"
    mi 2 "我没办法掌握全部信息，有很多事我也不知道。"
    mi 2 "但信徒获得能力后会变得极度残忍这一点，已经被无数观察证实了。"
    mi 2 "所以我才这么担心你，[gg]。"
    mi 2 "我在学校走廊里看到过你是怎么使用能力的。"
    mi 2 "那既让人印象深刻，又让人恐惧。"
    scene cafe_minami_26 with Dissolve(0.3)
    gg 9 "是啊，我自己也觉得很奇怪。就好像它突然……自己开始了。" with dissolve
    gg 9 "这些信徒也会做我做的梦吗？"
    show cafe_minami_37 with Dissolve(0.3)
    mi 2 "梦或许是连接我们的世界与彼岸的某种桥梁。" with dissolve
    mi 2 "我不知道他们梦到什么。"
    mi 2 "也许你获得的是另一个精神存在给予的力量……我也不知道。"
    mi 2 "只是猜测。"
    mi 2 "别用那种眼神看我！"
    mi 2 "我知道这听起来像什么。但很遗憾，我并非全知。"
    scene cafe_minami_41 with Dissolve(0.3)
    gg 9 "听起来有点绕。" with dissolve
    scene cafe_minami_42 with Dissolve(0.3)
    gg 9 "{cps=5}……{/cps}" with dissolve
    scene cafe_minami_43 with Dissolve(0.3)
    gg 9 "（我到底这是怎么了？！）" with dissolve
    gg 9 "（我要怎么控制这些力量？）"
    show cafe_minami_26 with Dissolve(0.3)
    gg 9 "我觉得自己开始有点理解这些信徒了。" with dissolve
    gg 9 "但真的像你说的那么恐怖吗？"
    show cafe_minami_36 with Dissolve(0.3)
    hide cafe_minami_26
    mi 2 "他们的人生时刻处在危险中，永远不知道明天会怎样。" with dissolve
    mi 2 "但最难的是，他们永远不知道{color=ffa500}救赎{/color}的时刻何时会到来。"
    mi 2 "而完成那个任务，通常就意味着他们生命的终点。"
    show cafe_minami_26 with Dissolve(0.3)
    hide cafe_minami_36
    gg 9 "救赎？" with dissolve
    gg 9 "大致就是……完成契约上的条件，之后契约就失效了？"
    gg 9 "这名字本身就说明一切了。"
    show cafe_minami_37 with Dissolve(0.3)
    hide cafe_minami_26
    mi 2 "没错。我们发现救赎原本被设定为信徒的最后一个任务。" with dissolve
    mi 2 "完成它，他们就会失去力量，但也能摆脱奴役他们的人。"
    mi 2 "也就是取回自己的自由。"
    mi 2 "但实际上……似乎没有任何人生还。"
    mi 2 "所有的救赎——至少我所知道的那些——都以信徒的死亡告终。"
    mi 2 "我不知道为什么。关于这个我也只能说到这儿。"
    show cafe_minami_44 with Dissolve(0.3)
    hide cafe_minami_37
    gg 9 "这听起来绝望得可怕……" with dissolve
    gg 9 "我永远无法想象自己变成那样。"
    gg 9 "这些信徒也可以试着逃跑吧？"
    gg 9 "既然他们带着这种力量活着，其中应该也有活得很久的。"
    gg 9 "他们应该有足够的时间找到逃出这个陷阱的方法。"
    show cafe_minami_37 with Dissolve(0.3)
    hide cafe_minami_30
    mi 2 "确实有些人会试图逃走，或者寻找切断联系的办法。" with dissolve
    mi 2 "但恶魔总能重新夺回控制权。"
    mi 2 "前提是，它曾经失去过控制权。"
    scene cafe_minami_43 with Dissolve(0.3)
    gg 9 "{cps=5}……{/cps}" with dissolve
    show cafe_minami_34 with Dissolve(0.3)
    mi 2 "我知道的就都告诉你了。" with dissolve
    mi 2 "有什么问题，尽管问。"
    show cafe_minami_35 with Dissolve(0.3)
    hide cafe_minami_34
    hide cafe_minami_44
    hide cafe_minami_45
    
    $ cafe_minami_choice_1 = []
    menu cafe_minami_choice_1:
        set cafe_minami_choice_1
        ## CHOICE 1
        "成为信徒的动机":
            gg 9 "究竟是什么驱使人们去做恶魔的奴隶？" with dissolve
            show cafe_minami_34 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "这个问题可不简单。" with dissolve
            mi 2 "动机有很多种。很大程度上取决于每个人的想法与目的。"
            mi 2 "通常，人们为了获得非同寻常的能力或力量而不顾后果地与恶魔缔约。"
            mi 2 "遗憾的是，为了追求那种惊人的力量，他们愿意采取极端手段。"
            mi 2 "有人为了复仇。有人想拯救挚爱的人，或是想征服世界。"
            mi 2 "而恶魔乐于把他们想要的送到他们手上。"
            $ cafe_minami_choice_1_value += 1
            if not cafe_minami_choice_1_value == 6:
                show cafe_minami_35 with Dissolve(0.3)
                hide cafe_minami_34
                jump cafe_minami_choice_1


        ## CHOICE 2
        "与恶魔缔约":
            gg 9 "具体是怎么进行的？" with dissolve
            gg 9 "我是说，他们要怎么和恶魔缔约？"
            gg 9 "是某种神秘的仪式吗？"
            show cafe_minami_34 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "我不能确定。关于恶魔契约有各种假说。" with dissolve
            mi 2 "或许是某种自古就存在于地球上的古老仪式。"
            mi 2 "某种源自恶魔学的东西……"
            mi 2 "我们推测可能是某种特殊仪式，或许涉及血祭。"
            mi 2 "但没有确凿的数据。"
            $ cafe_minami_choice_1_value += 1
            if not cafe_minami_choice_1_value == 6:
                show cafe_minami_35 with Dissolve(0.3)
                hide cafe_minami_34
                jump cafe_minami_choice_1

        ## CHOICE 3
        '「如果恶魔注意到我怎么办？」':
            gg 9 "如果被恶魔盯上，我会遭遇什么？" with dissolve
            gg 9 "就连你都注意到我了。"
            show cafe_minami_45 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "我们不确定你现在算不算信徒。你的力量来源有可能和他们不同。" with dissolve
            mi 2 "这可能带来难以预料的后果。"
            mi 2 "他们可能会研究你，试图把你召唤到他们那边，或者利用你的力量达成目的。"
            mi 2 "你可能会落入他们的影响之下，或成为他们关注的目标——考虑到他们的冷酷，这极其危险。"         
            $ cafe_minami_choice_1_value += 1
            show cafe_minami_35 with Dissolve(0.3)
            hide cafe_minami_45
            menu:
                '「我能躲起来吗？」':
                    gg 9 "如果我学会控制自己的能力，是不是就能避开他们？" with dissolve
                    show cafe_minami_36 with Dissolve(0.3)
                    hide cafe_minami_35
                    mi 2 "那需要自律。但如果能帮你避开麻烦，也许有用。" with dissolve
                    mi 2 "你绝不能任由情绪完全支配自己——要保持头脑清醒。"
                    mi 2 "你必须清楚自己的界线，以及愿意为何而战。"
                    mi 2 "恶魔难以捉摸，务必谨慎行事。"
                    if not cafe_minami_choice_1_value == 6:
                        show cafe_minami_35 with Dissolve(0.3)
                        hide cafe_minami_36
                        jump cafe_minami_choice_1
                
                '返回':
                    pause 0.3
                    if not cafe_minami_choice_1_value == 6:
                        jump cafe_minami_choice_1


        ## CHOICE 4
        "「如果违抗恶魔会怎样？」":
            gg 9 "如果信徒拒绝服从主人的命令，会发生什么？" with dissolve
            show cafe_minami_34 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "据我所知，违抗是极为严重的罪行。" with dissolve
            mi 2 "老实说，我们以前从没遇到过这种情况。"
            mi 2 "他们从不犹豫地服从命令。"
            mi 2 "我觉得，不管你愿不愿意，他们都会让你去做。"
            mi 2 "何况恶魔拥有压倒性的力量——光是试图违抗，都可能毫无意义。"
            $ cafe_minami_choice_1_value += 1
            if not cafe_minami_choice_1_value == 6:
                show cafe_minami_35 with Dissolve(0.3)
                hide cafe_minami_34
                jump cafe_minami_choice_1


        ## CHOICE 5
        "「政府知道吗？」":
            gg 9 "政府知道恶魔的存在吗？" with dissolve
            show cafe_minami_34 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "当然知道。许多高层官员和国家元首都清楚它们的存在。" with dissolve
            mi 2 "但这个信息并未公开，被严格保密。"
            show cafe_minami_26 with Dissolve(0.3)
            hide cafe_minami_34
            gg 9 "所以即使这构成威胁，他们也在对公众隐瞒？" with dissolve
            show cafe_minami_45 with Dissolve(0.3)
            hide cafe_minami_26
            mi 2 "没错。" with dissolve
            mi 2 "想想人们得知恶魔存在后会引发什么吧？"
            mi 2 "他们害怕这个信息一旦在民众中传开，会引发恐慌与混乱。"
            mi 2 "那可能导致社会秩序彻底崩溃，届时恶魔和它们的爪牙就会找到大量新的客户。"
            mi 2 "后果将是灾难性的。"
            $ cafe_minami_choice_1_value += 1
            if not cafe_minami_choice_1_value == 6:
                show cafe_minami_35 with Dissolve(0.3)
                hide cafe_minami_45
                jump cafe_minami_choice_1


        ## CHOICE 6
        "信徒的日常生活":
            hide cafe_minami_34
            hide cafe_minami_44
            hide cafe_minami_45
            gg 9 "信徒在日常生活中都做些什么？" with dissolve
            show cafe_minami_34 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "他们假装成普通人，隐藏自己的异常之处，融入人群，避免引人注目。" with dissolve
            mi 2 "达成目的之后，其中有些人其实会停止使用能力。"
            mi 2 "或许是为了避免加重依赖，或避免累积使用力量的潜在代价。"
            mi 2 "有些人努力过普通生活，只在紧急关头才动用力量。"
            show cafe_minami_45 with Dissolve(0.3)
            hide cafe_minami_34
            mi 2 "但也有人抵挡不住使用黑暗力量的诱惑。" with dissolve
            mi 2 "他们可能成为雇佣兵，为报酬完成任务，或效力于各种犯罪与军事组织。"
            mi 2 "他们的本事让他们既危险，又抢手。"
            mi 2 "也有一些信徒选择用能力行善。"
            mi 2 "他们可能会加入对抗其他信徒的特殊组织，或许是为了维持平衡。"
            mi 2 "我怀疑他们也处于严密监视之下。因为只要精神上的主人一声令下，他们就可能开始制造混乱……"
            mi 2 "别太纠结这个。"
            show cafe_minami_36 with Dissolve(0.3)
            hide cafe_minami_45
            mi 2 "无论作何选择，信徒的人生从来都不简单。" with dissolve
            $ cafe_minami_choice_1_value += 1
            if not cafe_minami_choice_1_value == 6:
                show cafe_minami_35 with Dissolve(0.3)
                hide cafe_minami_6
                jump cafe_minami_choice_1
        
        '「不问。」':
            if cafe_minami_choice_1_value == 0:
                gg 9 "不问了。" with dissolve
            else:
                gg 9 "我已经听得够多了。" with dissolve

    gg 9 "哦，对！"
    stop music2 fadeout 3
    play music japan_streets_1 volume 0.5 fadein 2
    play music3 jazz_brunch_by_kevin_macleod volume 0.5 fadein 8
    play sound2 clothes_2 volume 0.5
    scene cafe_minami_46 with Dissolve(0.3)
    gg 9 "我把枪带来了……就是那个[asami]留给我的。" with dissolve
    stop music fadeout 3
    scene cafe_minami_47 with Dissolve(0.3)
    mi 2 "什么？……" with dissolve
    play sound pistol_2
    scene cafe_minami_48 with Dissolve(0.3)
    gg 9 "你看！" with dissolve
    scene cafe_minami_49 with Dissolve(0.3)
    mi 2 "天啊，[gg]！" with dissolve
    mi 2 "快把那个收起来！"
    show cafe_minami_30 with Dissolve(0.3)
    mi 2 "{cps=5}……{/cps}" with dissolve
    scene cafe_minami_50 with Dissolve(0.3)
    mi 2 "你百分之百确定那女孩是留给你的？" with dissolve
    scene cafe_minami_51 with Dissolve(0.3)
    gg 9 "一万个百分点确定！" with dissolve
    scene cafe_minami_52 with Dissolve(0.3)
    mi 2 "好吧{cps=5}……{/cps}" with dissolve
    mi 2 "可是这把武器……"
    scene cafe_minami_50 with Dissolve(0.3)
    mi 2 "你该不会是想用它吧？" with dissolve
    scene cafe_minami_53 with Dissolve(0.3)
    gg 9 "我可没经验。" with dissolve
    scene cafe_minami_54 with Dissolve(0.3)
    gg 9 "但……总觉得说不定能派上用场。" with dissolve
    scene cafe_minami_49 with Dissolve(0.3)
    mi 2 "你小心点。放在安全的地方！" with dissolve
    play sound paper1
    scene cafe_minami_55 with Dissolve(0.3)
    gg 9 "对了，还有一张纸条。" with dissolve
    scene cafe_minami_56 with Dissolve(0.3)
    gg 9 "也许有什么特别的意思？看看吧。" with dissolve
    show cafe_minami_57 with Dissolve(0.3)
    mi 2 "{cps=5}……{/cps}" with dissolve
    mi 2 "{cps=5}……{/cps}"
    scene cafe_minami_58 with Dissolve(0.3)
    mi 2 "我都不确定我们该不该看这个。" with dissolve
    scene cafe_minami_59 with Dissolve(0.3)
    mi 2 "不过……" with dissolve
    scene cafe_minami_60 with Dissolve(0.3)
    pause 1.0
    scene cafe_minami_61 with Dissolve(0.3)
    pause 0.5
    play sound snap1
    scene cafe_minami_62 with Dissolve(0.3)
    pause 0.5
    scene cafe_minami_63 with Dissolve(0.3)
    pause 0.5
    scene cafe_minami_64 with Dissolve(0.3)
    mi 2 "等等。我试试看……" with dissolve
    play sound button1
    scene cafe_minami_65 with Dissolve(0.3)
    pause 1.5
    scene cafe_minami_66 with Dissolve(0.3)
    pause 1.5
    scene cafe_minami_67 with Dissolve(0.3)
    play sound dm2
    $ renpy.music.set_volume(0.3, delay=1, channel=u'music3')
    pause 1.0
    mi 2 "有意思……" with dissolve
    gg 9 "搞什么……" with dissolve
    scene cafe_minami_68 with Dissolve(0.3)
    mi 2 "这个我能先留着吗？" with dissolve
    mi 2 "我想回家再好好想想。"
    scene cafe_minami_69 with Dissolve(0.3)
    gg 9 "没问题。" with dissolve
    $ renpy.music.set_volume(1, delay=5, channel=u'music3')
    show cafe_minami_34 with Dissolve(0.3)
    mi 2 "那么……我们差不多该收尾了。" with dissolve
    mi 2 "你还有其他问题吗？" with dissolve
    show cafe_minami_35 with Dissolve(0.3)
    hide cafe_minami_34
    $ cafe_minami_choice_2 = []
    menu cafe_minami_choice_2:
        set cafe_minami_choice_2
        
        
        ## CHOICE 1
        "「他们在哪里与恶魔见面？」":

            gg 9 "人们是如何、在哪里与恶魔接触并成为信徒的？" with dissolve
            show cafe_minami_34 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "这类接触发生在维度的夹缝中。" with dissolve
            mi 2 "遗憾的是，我不知道确切细节。"
            $ cafe_minami_choice_2_value += 1
            if not cafe_minami_choice_2_value == 6:
                show cafe_minami_35 with Dissolve(0.3)
                hide cafe_minami_34
                jump cafe_minami_choice_2
                
                
        ## CHOICE 2
        "「[asami]是恶魔吗？」":

            gg 9 "[asami]是恶魔吗？" with dissolve
            show cafe_minami_34 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "关于信徒我了解很多……但[asami]完全是另一回事。" with dissolve
            mi 2 "[gg]，如果你再见到她，千万要小心。她可能很危险。"
            $ cafe_minami_choice_2_value += 1
            if not cafe_minami_choice_2_value == 6:
                show cafe_minami_35 with Dissolve(0.3)
                hide cafe_minami_34
                jump cafe_minami_choice_2

        ## CHOICE 3
        "用科学方法切断联系":
        
            gg 9 "有没有科学手段能斩断与恶魔的羁绊？" with dissolve
            gg 9 "有人在实验室里试过吗？"
            scene cafe_minami_70 with Dissolve(0.3)
            mi 2 "{cps=5}……{/cps}" with dissolve
            scene cafe_minami_71 with Dissolve(0.3)
            gg 9 "你没事吧？" with dissolve
            scene cafe_minami_72 with Dissolve(0.3)
            mi 2 "有……不过……算了。别再想了。" with dissolve
            scene cafe_minami_73 with Dissolve(0.3)
            $ choice_var = 0
            menu:
                "[gr]握住她的手":
                    stop music2 fadeout 2
                    pause 0.3
                    play sound cafe_minami_74_sound
                    show cafe_minami_74 with Dissolve(0.1)
                    $ renpy.pause(2.5,hard=True)
                    play music3 the_fog_of_war_by_tim_kulig fadein 3
                    scene black with Dissolve(0.5)
                    pause 0.5
                    scene cafe_minami_fb_0 with Dissolve(1.0):
                        top
                        ypos -2000
                        ease 13 ypos 0
                    pause 5
                    scene cafe_minami_fb_1 with Dissolve(0.5)
                    sideman1 "我们以涉嫌开始执行命令为由将她拘留。" with dissolve
                    sideman1 "恐怕这是必要的。"
                    scene cafe_minami_fb_2 with Dissolve(0.5)
                    mi 3 "证据已经足够充分，但……" with dissolve
                    scene cafe_minami_fb_3 with Dissolve(0.5)
                    mi 3 "你确定这样对她有好处吗？" with dissolve
                    scene cafe_minami_fb_4 with Dissolve(0.5)
                    pause 1.0
                    scene cafe_minami_fb_5 with Dissolve(0.5)
                    pause 1.0
                    scene cafe_minami_fb_6 with Dissolve(0.5)
                    pause 1.0
                    scene cafe_minami_fb_7 with Dissolve(0.5)
                    sideman2 "不能出任何差错。" with dissolve
                    sideman2 "我们必须弄清她与恶魔沟通的方式。"
                    scene cafe_minami_fb_8 with Dissolve(0.5)
                    sideman3 "古川在说话。" with dissolve
                    scene cafe_minami_fb_9 with Dissolve(0.5)
                    sidegirl1 "我受不了了……" with dissolve
                    sidegirl1 "求你……杀了我。"
                    scene cafe_minami_fb_10 with Dissolve(0.5)
                    mi 3 "对这么年轻的女孩来说，这太沉重了。" with dissolve
                    scene cafe_minami_fb_11 with Dissolve(0.5)
                    sidegirl1 "他们所有人都是因为我才受苦。" with dissolve
                    scene cafe_minami_fb_12 with Dissolve(0.5)
                    sidegirl1 "实在受不了……" with dissolve
                    scene cafe_minami_fb_13 with Dissolve(0.5)
                    sidegirl1 "对……我确定。" with dissolve
                    sidegirl1 "嗯、是的……"
                    scene cafe_minami_fb_14 with Dissolve(0.5)
                    sideman1 "会不会是暗影在死前操纵她的行为？" with dissolve
                    scene cafe_minami_fb_6 with Dissolve(0.5)
                    sideman2 "她快失去意识了。" with dissolve
                    scene cafe_minami_fb_7 with Dissolve(0.5)
                    sideman2 "注射药物！" with dissolve
                    scene black with Dissolve(1.0)
                    pause 1.0
                    $ cafe_minami_choice_flashback = True
                    stop music3 fadeout 3
                    scene cafe_minami_73 with Dissolve(1.0)
                    pause 0.5
                    play music2 jazz_brunch_by_kevin_macleod fadein 23
                    
                "什么都不做":
                    pause 0.3
            
            $ choice_var = 1
            scene cafe_minami_75 with Dissolve(0.3)
            mi 2 "我认为那不可能。" with dissolve
            
            if cafe_minami_choice_flashback == True:
                scene cafe_minami_76 with Dissolve(0.3)
                gg 9 "（我的天……）" with dissolve
                gg 9 "（我刚才看到的是什么？！）"
                gg 9 "（那些是她的记忆？）"
                
            $ cafe_minami_choice_2_value += 1
            if not cafe_minami_choice_2_value == 6:
                show cafe_minami_35 with Dissolve(0.3)
                jump cafe_minami_choice_2
            

        ## CHOICE 4
        "超自然能力的种类":
            gg 9 "人们能从恶魔那里获得哪些超自然能力？" with dissolve
            gg 9 "使用这些力量是否有限制或代价？"
            show cafe_minami_34 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "范围非常广。元素操控、念动力、能量干涉……" with dissolve
            mi 2 "但有一个关键问题：信徒的力量永远反映其主人的实力。"
            mi 2 "只不过更弱、更不稳定，也更难控制。"
            $ cafe_minami_choice_2_value += 1
            if not cafe_minami_choice_2_value == 6:
                show cafe_minami_35 with Dissolve(0.3)
                hide cafe_minami_34
                jump cafe_minami_choice_2

        ## CHOICE 5
        "「恶魔存在多久了？」":
            gg 9 "恶魔已经存在多久？" with dissolve
            show cafe_minami_34 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "无法精确地说。" with dissolve
            mi 2 "也许它们从远古时代就与我们同在。数百年，甚至数千年。"
            mi 2 "长久以来，它们与人类历史交织，却始终藏身于阴影之中。"
            mi 2 "只留下与这个世界传说混为一体的神话与故事。"
            mi 2 "它们的存在，处在古老知识与绝对保密的边界上。"
            $ cafe_minami_choice_2_value += 1
            if not cafe_minami_choice_2_value == 6:
                show cafe_minami_35 with Dissolve(0.3)
                hide cafe_minami_34
                jump cafe_minami_choice_2

        ## CHOICE 6
        "「你怎么会当老师？」":

            gg 9 "你怎么会成为老师？" with dissolve
            show cafe_minami_34 with Dissolve(0.3)
            hide cafe_minami_35
            mi 2 "感觉像活在两种不同的人生里，对吧？" with dissolve
            mi 2 "你知道，命运有时会出人意料地拐个弯。"
            mi 2 "研究所的工作很有价值，但……那不是我想要走的路。"
            show cafe_minami_35 with Dissolve(0.3)
            hide cafe_minami_34
            menu:
                ## CHOICE 6-1
                "「为什么离开？」":

                    gg 9 "那么，究竟是什么让你离开研究所去当老师？" with dissolve
                    show cafe_minami_45 with Dissolve(0.3)
                    mi 2 "很多原因。" with dissolve
                    mi 2 "我一直觉得教育很重要。而把知识传递给他人的机会——那是值得为之努力的。"
                    mi 2 "但在研究所……我看到他们怎么对待人。冷酷无情，只为牟利。"
                    mi 2 "他们在那些人身上进行骇人的实验，强迫他们做些连提起来都困难的事……"
                    mi 2 "那不是科学——那是暴力。我没办法继续参与那种事。"
                    mi 2 "我们……别再往下说了。我连想都不想再提。"
                    
                    $ cafe_minami_choice_2_value += 1
                    if not cafe_minami_choice_2_value == 6:
                        show cafe_minami_35 with Dissolve(0.3)
                        hide cafe_minami_45
                        jump cafe_minami_choice_2
                    
                "返回":
                    pause 0.3
                    $ cafe_minami_choice_2_value += 1
                    if not cafe_minami_choice_2_value == 6:
                        jump cafe_minami_choice_2
                        
        '「不问。」':
            if cafe_minami_choice_2_value == 0:
                gg 9 "不问了。" with dissolve
            else:
                gg 9 "我已经听得够多了。" with dissolve
    
    scene cafe_minami_77 with Dissolve(0.3)
    stop music2 fadeout 4
    pause 2.0
    play music3 marty_gots_a_plan_by_kevin_macleod fadein 1 volume 0.5
    scene cafe_minami_78 with Dissolve(0.3)
    me 3 "喂，[gg]！" with dissolve
    scene cafe_minami_79 with Dissolve(0.3)
    me 3 "你旁边那位美女是谁啊？" with dissolve
    scene cafe_minami_80 with Dissolve(0.3)
    mi 2 "{cps=5}……{/cps}" with dissolve
    scene cafe_minami_81 with Dissolve(0.3)
    me 3 "{cps=5}……{/cps}" with dissolve
    play sound2 as3 volume 0.3
    scene cafe_minami_82 with Dissolve(0.3)
    me 3 "栗、栗原老师？" with dissolve
    scene cafe_minami_83 with Dissolve(0.3)
    dai 3 "你们两个在约会吗？" with dissolve
    scene cafe_minami_84 with Dissolve(0.3)
    gg 9 "我们是来办正事的。" with dissolve
    play sound3 swing1 volume 0.3
    scene cafe_minami_85 with Dissolve(0.3)
    me 3 "走啦小胖，别去打扰人家。" with dissolve
    scene cafe_minami_86 with Dissolve(0.3)
    mi 2 "没、没事。我们正准备走了。" with dissolve
    scene cafe_minami_87 with Dissolve(0.3)
    mi 2 "我去结账，在外面等你。" with dissolve
    mi 2 "我得透透气。"
    scene cafe_minami_88 with Dissolve(1.0)
    ''
    scene cafe_minami_89 with Dissolve(0.3)
    me 3 "那是你女朋友？" with dissolve
    scene cafe_minami_90 with Dissolve(0.3)
    dai 3 "哥们，你是怎么做到的？" with dissolve
    scene cafe_minami_91 with Dissolve(0.3)
    gg 9 "我们先走了，各位。下次再聊。" with dissolve
    scene cafe_minami_92 with Dissolve(0.3)
    dai 3 "他们饭都没吃完就跑了……" with dissolve
    play sound slap1
    scene cafe_minami_93 with Dissolve(0.3)
    dai 3 "嘿，白吃一顿！" with dissolve
    
label after_cafe_minami:
    stop music3 fadeout 3
    play music2 japan_streets_1 fadein 3
    scene black with Dissolve(1.0)
    pause 2.0
    scene after_cafe_minami_1 with Dissolve(1.0)
    mi 2 "傍晚的空气真清爽。" with dissolve
    scene after_cafe_minami_2 with Dissolve(0.5)
    gg 9 "刚才在里面是不是不自在？" with dissolve
    scene after_cafe_minami_3 with Dissolve(0.5)
    mi 2 "也谈不上。就是……有点冷。而且现在只想快点回家。" with dissolve
    play sound pat_cloth_2
    scene after_cafe_minami_4 with Dissolve(0.3)
    ''
    scene after_cafe_minami_5 with Dissolve(0.3)
    gg 10 "这样好些了吗？" with dissolve
    scene after_cafe_minami_6 with Dissolve(0.5)
    mi 4 "谢谢。" with dissolve
    scene after_cafe_minami_7 with Dissolve(0.5)
    ''
    scene after_cafe_minami_8 with Dissolve(0.3)
    gg 10 "你现在看起来好害羞。" with dissolve
    gg 10 "还在为被他们看见我们在一起而尴尬？"
    scene after_cafe_minami_9 with Dissolve(0.3)
    mi 4 "我尴尬的是这么晚还和你在外面走。" with dissolve
    scene after_cafe_minami_10 with Dissolve(0.3)
    mi 4 "我已经记不清上一次有人这样关心我是什么时候了。" with dissolve
    scene after_cafe_minami_11 with Dissolve(0.5)
    gg 10 "你可以依靠我，[mi]。" with dissolve
    scene after_cafe_minami_12 with Dissolve(0.3)
    gg 10 "你现在不就已经在帮我了吗。以后要是需要我帮忙……" with dissolve
    gg 10 "只要说一声。任何时候都行。"
    play music3 march_on_utopia_loop_by_troyificus fadein 1
    stop music2 fadeout 1
    play sound as2 volume 0.6
    scene after_cafe_minami_13 with hpunch
    robber0 "别动！" with dissolve
    robber0 "现金、戒指，还有值钱的东西，快交出来！"
    scene after_cafe_minami_14 with Dissolve(0.3)
    robber2 "这是抢劫！" with dissolve
    scene after_cafe_minami_15 with Dissolve(0.3)
    mi 4 "诶？" with dissolve
    scene after_cafe_minami_16 with Dissolve(0.3)
    gg 10 "（搞什么啊……）" with dissolve
    scene after_cafe_minami_17 with Dissolve(0.3)
    pause 1.0
    gg 10 "（光头矮子，拿着一把生锈的刀。）" with dissolve
    scene after_cafe_minami_18 with Dissolve(0.3)
    gg 10 "（第二个家伙块头更大，看不到武器。）" with dissolve
    scene after_cafe_minami_19 with Dissolve(0.3)
    gg 10 "（最好保持警惕。谁知道他们藏了什么。）" with dissolve
    scene after_cafe_minami_20 with Dissolve(0.3)
    mi 4 "我要报警了！" with dissolve
    scene after_cafe_minami_21 with Dissolve(0.3)
    robber1 "等警察来之前，我们先好好招待你们三个。" with dissolve
    scene after_cafe_minami_22 with Dissolve(0.3)
    robber2 "哈哈哈！" with dissolve
    scene after_cafe_minami_23 with Dissolve(0.3)
    robber2 "这你女朋友啊，靓仔？" with dissolve
    show after_cafe_minami_24 with Dissolve(0.3)
    $ choice_var = 0
    menu:
        "「对，她是我的。」\\n[gold](美波 +1 / 之后)":
            gg 10 "对，她是我的。" with dissolve
            scene after_cafe_minami_25 with Dissolve(0.3)
            mi 4 "...!" with dissolve
            $ minami_my_girl = True
            scene after_cafe_minami_26 with Dissolve(0.3)
            robber2 "哦，原来如此。" with dissolve
            robber2 "那这样吧，兄弟……"
            scene after_cafe_minami_27 with Dissolve(0.3)
            robber2 "你把身上值钱的东西全交出来。至于她，跟我们去巷子里待到天亮。" with dissolve
            robber2 "听明白了吗？"
        
        "「关你什么事？」":
            gg 10 "关你什么事？" with dissolve
            scene after_cafe_minami_28 with Dissolve(0.3)
            robber2 "我们抢定你了，女人也一起带走。现在！" with dissolve
    
    $ choice_var = 1
    scene after_cafe_minami_29 with Dissolve(0.3)
    gg 10 "（该死，我身上还真有那把枪……）" with dissolve
    play sound woosh_dm
    scene after_cafe_minami_30 with Dissolve(0.3)
    ''
    scene after_cafe_minami_31 with Dissolve(0.3)
    robber1 "喂小子，你疯了吗？" with dissolve
    play sound pistol_1
    scene after_cafe_minami_32 with Dissolve(0.3)
    ''
    play sound2 pistol_2
    scene after_cafe_minami_33 with Dissolve(0.3)
    ''
    scene after_cafe_minami_34 with Dissolve(0.3)
    gg 10 "再往前一步就试试看。" with dissolve
    scene after_cafe_minami_35 with Dissolve(0.3)
    robber1 "{cps=5}……{/cps}" with dissolve
    scene after_cafe_minami_36 with Dissolve(0.3)
    robber2 "等、等……" with dissolve
    scene after_cafe_minami_37 with Dissolve(0.3)
    mi 4 "住手！你这样会坐牢的！" with dissolve
    mi 4 "你就不能放他们走吗？"
    scene after_cafe_minami_38 with Dissolve(0.3)
    gg 10 "不然呢？" with dissolve
    scene after_cafe_minami_39 with Dissolve(0.3)
    robber2 "靠，Toshi，这混蛋还真把我唬住了。" with dissolve
    scene after_cafe_minami_40 with Dissolve(0.3)
    robber2 "差点就信了他真有那玩意儿。" with dissolve
    scene after_cafe_minami_41 with Dissolve(0.3)
    gg 10 "（还是该确认一下……）" with dissolve
    scene after_cafe_minami_42 with Dissolve(0.3)
    mi 4 "...!" with dissolve
    scene after_cafe_minami_43 with Dissolve(0.3)
    robber1 "先解决这个男人，再去玩那个女的。" with dissolve
    scene after_cafe_minami_44 with Dissolve(0.3)
    gg 10 "（希望这力量别在这种时候掉链子。）" with dissolve
    gg 10 "（看来这就是[asami]留这份礼给我的原因……）"
    gg 10 "（以防万一。）"
    gg 10 "（只要想象该怎么用就行了……）"
    gg 10 "（集中精神……）"
    show after_cafe_minami_45 with Dissolve(0.3)
    pause 0.05
    show after_cafe_minami_45 with Dissolve(0.1):
        top
        zoom 1
        ease 0.3 zoom 1.1
    gg 10 "（想象时间变慢……）" with dissolve
    play music2 last_minute_failure_loop_by_troyificus fadein 1
    stop music3 fadeout 1
    scene after_cafe_minami_46 with hpunch
    robber2 "吃我一记，贱人！" with dissolve
    play sound after_cafe_minami_fight_1
    show after_cafe_minami_47 with Dissolve(0.1)
    $ renpy.pause(0.9,hard=True)
    show after_cafe_minami_48 with Dissolve(0.1)
    hide after_cafe_minami_47
    gg 10 "太慢了。" with dissolve
    play sound2 after_cafe_minami_fight_2
    show after_cafe_minami_49 with Dissolve(0.1)
    hide after_cafe_minami_48
    $ renpy.pause(1.0,hard=True)
    show after_cafe_minami_50 with Dissolve(0.1)
    hide after_cafe_minami_49
    ''
    play sound3 after_cafe_minami_fight_3
    show after_cafe_minami_51 with Dissolve(0.1)
    hide after_cafe_minami_50
    $ renpy.pause(1.0,hard=True)
    show after_cafe_minami_52 with Dissolve(0.1)
    hide after_cafe_minami_51
    ''
    play sound after_cafe_minami_fight_4
    show after_cafe_minami_53 with Dissolve(0.1)
    hide after_cafe_minami_52
    $ renpy.pause(1.0,hard=True)
    show after_cafe_minami_54 with Dissolve(0.1)
    hide after_cafe_minami_53
    ''
    play sound2 after_cafe_minami_fight_5
    show after_cafe_minami_55 with Dissolve(0.1)
    hide after_cafe_minami_54
    $ renpy.pause(2.0,hard=True)
    show after_cafe_minami_56 with Dissolve(0.1)
    hide after_cafe_minami_55
    ''
    play sound3 after_cafe_minami_fight_6
    show after_cafe_minami_57 with Dissolve(0.1)
    hide after_cafe_minami_56
    $ renpy.pause(2.5,hard=True)
    show after_cafe_minami_58 with Dissolve(0.1)
    hide after_cafe_minami_57
    ''
    play sound after_cafe_minami_fight_7
    show after_cafe_minami_59 with Dissolve(0.1)
    hide after_cafe_minami_58
    $ renpy.pause(0.5,hard=True)
    show after_cafe_minami_60 with Dissolve(0.1)
    hide after_cafe_minami_59
    ''
    play sound2 after_cafe_minami_fight_8
    show after_cafe_minami_61 with Dissolve(0.1)
    hide after_cafe_minami_60
    $ renpy.pause(2.5,hard=True)
    show after_cafe_minami_62 with Dissolve(0.1)
    hide after_cafe_minami_61
    pause 0.5
    stop music2 fadeout 3
    play music3 japan_streets_2 fadein 3
    scene after_cafe_minami_63 with Dissolve(0.5)
    gg 10 "（搞定。结束。）" with dissolve
    scene after_cafe_minami_64 with Dissolve(1.0)
    gg 10 "[mi]，我们走。" with dissolve
    scene after_cafe_minami_65 with Dissolve(1.0)
    mi 4 "刚才那真是……太不可思议了……" with dissolve
    play sound pat_cloth_2
    scene after_cafe_minami_66 with Dissolve(0.3)
    gg 10 "快，我们离开这里！" with dissolve
    scene after_cafe_minami_67 with Dissolve(0.3)
    mi 4 "我们不报警吗？" with dissolve
    scene after_cafe_minami_68 with Dissolve(0.3)
    gg 10 "没时间浪费。就像你说的——最好别招来不必要的注意。" with dissolve
    scene after_cafe_minami_69 with Dissolve(0.3)
    ''
    stop music3 fadeout 6
    scene black with Dissolve(1.5)
    pause 1.0
    jump cdr_2
