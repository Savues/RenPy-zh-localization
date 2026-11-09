# =========================================================
# Walkthrough Mod - Wild Cats (中文汉化适配版)
# =========================================================

default persistent.wt_hints_on = True

init 1 python:

    wt_separator = "\n"
    wt_compact_from = 5
    wt_compact_separator = " "
    wt_compact_size = -6
    wt_compact_text_size = -6
    wt_choice_spacing = 10

    def wt_G(t):
        return "{color=#3dff8a}(" + t + "){/color}"

    def wt_R(t):
        return "{color=#ff4d6d}(" + t + "){/color}"

    def wt_B(t):
        return "{color=#5cfff0}(" + t + "){/color}"

    def wt_P(t):
        return "{color=#ff3fb4}(" + t + "){/color}"

    def wt_flag(name):
        return bool(getattr(renpy.store, name, False))

    walkthrough_hints = {
        "No way!": wt_R("坏结局！"),
        "没门！": wt_R("坏结局！"),
        "Left": wt_G("下个选项 伊芙 +2"),
        "左": wt_G("下个选项 伊芙 +2"),
        "Right": wt_G("下个选项 伊芙 +1"),
        "右": wt_G("下个选项 伊芙 +1"),
        "I've come to know you better.": wt_G("伊芙 +2"),
        "我比你想的更了解你": wt_G("伊芙 +2"),
        "It was alright...": wt_G("伊芙 +1"),
        "还行吧……": wt_G("伊芙 +1"),
        "Let anger take over": wt_R("坏结局！"),
        "让愤怒占据上风": wt_R("坏结局！"),
        "Say a snarky comment": wt_R("佐伊 -1"),
        "说句刻薄话": wt_R("佐伊 -1"),
        "Take her hand": wt_G("黛丝瑞 +1"),
        "牵起她的手": wt_G("黛丝瑞 +1"),
        "Bring her some flowers and apologize": wt_G("伊芙心情 +1 · 解锁送花剧情"),
        "带些花去向她道歉": wt_G("伊芙心情 +1 · 解锁送花剧情"),
        "I'd like to apologize properly. Can we talk?": wt_G("伊芙心情 +1"),
        "我想郑重跟你道个歉,咱们能见一面聊聊吗？": wt_G("伊芙心情 +1"),
        "None of your business": wt_R("伊芙心情 -1"),
        "这个不关你的事": wt_R("伊芙心情 -1"),
        "I'm fine. It's just a little bruise": wt_G("伊芙心情 +1"),
        "我没事。只是块小瘀青罢了": wt_G("伊芙心情 +1"),
        "I fell off the stairs": wt_R("伊芙心情 -1"),
        "我从楼梯上摔下去了": wt_R("伊芙心情 -1"),
        "It was the best thing I could think of to make it up to you.": wt_G("伊芙心情 +3"),
        "这是我能想到的最好的补偿你的办法了": wt_G("伊芙心情 +3"),
        "Just take the flowers already. You're making me look bad here.": wt_R("伊芙心情 -2"),
        "快把花收下吧。你这让我也很为难": wt_R("伊芙心情 -2"),
        "Ask if she wants something": wt_G("伊芙心情 +1"),
        "问问她想要点什么": wt_G("伊芙心情 +1"),
        "Ask for a sip of her coffee": wt_R("伊芙心情 -1"),
        "问她能不能喝一口她的咖啡": wt_R("伊芙心情 -1"),
        "Latte": wt_G("正确的饮品"),
        "拿铁": wt_G("正确的饮品"),
        "Capuccino": wt_R("错误的饮品"),
        "卡布奇诺": wt_R("错误的饮品"),
        "Americano": wt_R("错误的饮品"),
        "美式咖啡": wt_R("错误的饮品"),
        "Tequila": wt_R("恶搞选项，需重新选择"),
        "龙舌兰酒": wt_R("恶搞选项，需重新选择"),
        "Introduce yourself this time": wt_G("伊芙心情 +2 · 若心情高则伊芙 +1~+2"),
        "这次先自我介绍": wt_G("伊芙心情 +2 · 若心情高则伊芙 +1~+2"),
        "I want you there.": wt_G("伊芙 +1"),
        "我想要你来": wt_G("伊芙 +1"),
        "Flirty response": wt_G("莱茜 +1"),
        "调情地回复": wt_G("莱茜 +1"),
        "Touch her breasts": wt_G("莱茜 +1"),
        "触摸她的胸部": wt_G("莱茜 +1"),
        "Message Eve goodnight": wt_G("伊芙 +1"),
        "给伊芙发晚安消息": wt_G("伊芙 +1"),
        "You look good.": wt_G("莱茜 +1"),
        "你看起来不错": wt_G("莱茜 +1"),
        "Say hi": wt_G("黛丝瑞 +1"),
        "打个招呼": wt_G("黛丝瑞 +1"),
        "She's with her friends, leave them be": wt_R("黛丝瑞 -1"),
        "她和朋友们在一起，别去打扰她们": wt_R("黛丝瑞 -1"),
        "Do it": wt_R("莱茜 -2"),
        "要": wt_R("莱茜 -2"),
        "It's not that I'm not interested at all...": wt_G("莱茜 +1"),
        "也不是说我完全不感兴趣……": wt_G("莱茜 +1"),
        "Someone sweet, loves to tease you, brunette, and wears glasses.": wt_B("伊芙 (Eve)"),
        "一个温柔体贴、喜欢捉弄人、深褐色头发、戴眼镜的女生？": wt_B("伊芙 (Eve)"),
        "Someone kind, brimming with positivity, and darker skinned.": wt_B("黛丝瑞 (Desiree)"),
        "一个善良、充满正能量、黑皮肤的女生？": wt_B("黛丝瑞 (Desiree)"),
        "Someone prim and proper, blonde, and behaves like a lady.": wt_B("佐伊 (Zoe)"),
        "一个端庄得体、金发碧眼、举止淑女的人？": wt_B("佐伊 (Zoe)"),
        "Someone tatooed and pierced, cool, and mysterious.": wt_B("菲奥娜 (Fiona)"),
        "一个有纹身、打耳洞、酷酷的、很神秘的人？": wt_B("菲奥娜 (Fiona)"),
        "Someone blonde, tanned, spontaneous, and a party girl.": wt_B("莱茜 (Lexi)") + " " + wt_G("莱茜 +1"),
        "金发、小麦色皮肤、随性自然，还是个派对女孩。": wt_B("莱茜 (Lexi)") + " " + wt_G("莱茜 +1"),
        "Someone with Asian features, black hair, a petite build, and just makes you feel like you can't leave her alone": wt_B("纱纪 (Saki)"),
        "有亚洲人特征、黑发、身材娇小，让你觉得不能抛下她不管的人": wt_B("纱纪 (Saki)"),
        "Because you're worth it.": wt_G("莱茜 +1"),
        "因为你值得": wt_G("莱茜 +1"),
        "Join her": wt_G("莱茜 +1") + " " + wt_P("特殊剧情(H)"),
        "和她一起加入": wt_G("莱茜 +1") + " " + wt_P("特殊剧情(H)"),
        "Kindly refuse": wt_R("莱茜 -1"),
        "委婉拒绝": wt_R("莱茜 -1"),
        "I jerked off while thinking of you twice.": wt_G("莱茜 +1"),
        "我想着你的画面撸了两回": wt_G("莱茜 +1"),
        "Want me to go with you to the place? It's a little late already.": wt_G("莱茜 +1"),
        "要我送你到那个地方吗？已经有点晚了": wt_G("莱茜 +1"),
        "You look lovely with you hair up.": wt_G("伊芙 +1"),
        "你把头发盘起来真好看": wt_G("伊芙 +1"),
        "Pat her head": wt_G("伊芙 +1"),
        "摸摸她的头": wt_G("伊芙 +1"),
        "Tap her head with the clip board": wt_R("伊芙 -1"),
        "用写字板轻敲她的头": wt_R("伊芙 -1"),
        "Carpentry": wt_G("黛丝瑞 +1"),
        "木工": wt_G("黛丝瑞 +1"),
        "Play along": wt_G("纱纪 +1"),
        "配合": wt_G("纱纪 +1"),
        "Don't play along": wt_R("纱纪 -1"),
        "不配合": wt_R("纱纪 -1"),
        "You're beautiful, Desiree.": wt_G("黛丝瑞 +1"),
        "你很美,黛丝瑞": wt_G("黛丝瑞 +1"),
        "Ask Bianca to tell Zoe to take it easy": wt_G("佐伊 +1"),
        "让比安卡告诉佐伊要劳逸结合": wt_G("佐伊 +1"),
        "Tease her back": wt_G("伊芙 +1"),
        "反过来逗她一下": wt_G("伊芙 +1"),
        "Be sarcastic": wt_R("伊芙 -1"),
        "出言讽刺": wt_R("伊芙 -1"),
        "Carry her books for her": wt_G("伊芙 +1") + " " + wt_B("若伊芙≥5则有更多后续剧情"),
        "帮她拿书": wt_G("伊芙 +1") + " " + wt_B("若伊芙≥5则有更多后续剧情"),
        "Wanna touch..?": wt_G("伊芙 +1"),
        "想摸吗..？": wt_G("伊芙 +1"),
        "Maybe someday": wt_G("伊芙 +1"),
        "也许有一天吧": wt_G("伊芙 +1"),
        "You have a lot of muscle knots on your back, let me take care of them.": wt_P("特殊剧情(H)") + " " + wt_G("伊芙 → 浪漫关系"),
        "你肩膀和后背好多地方都是硬的": wt_P("特殊剧情(H)") + " " + wt_G("伊芙 → 浪漫关系"),
        "I'll be happy to have you, Saki.": wt_G("纱纪 +1"),
        "我很高兴能拥有你,纱纪": wt_G("纱纪 +1"),
        "Message Lexi and ask how she is": wt_G("莱茜 +1"),
        "给莱茜发消息，问问她怎么样": wt_G("莱茜 +1"),
        "It's pretty hard not to miss you.": wt_G("莱茜 +1"),
        "不想你才怪": wt_G("莱茜 +1"),
        "Not really.": wt_R("莱茜 -1"),
        "其实不然": wt_R("莱茜 -1"),
        "I like being with you.": wt_G("纱纪 +1"),
        "我喜欢和你在一起": wt_G("纱纪 +1"),
        "I really do want you, Zoe.": wt_G("佐伊 +1"),
        "我真的想要你,佐伊": wt_G("佐伊 +1"),
        "You know what? I think I actually might.": wt_G("纱纪 +1"),
        "你知道吗？我觉得我可能还真会": wt_G("纱纪 +1"),
        "Tease her": wt_G("纱纪 +2"),
        "调戏她": wt_G("纱纪 +2"),
        "Thank her": wt_G("纱纪 +1"),
        "感谢她": wt_G("纱纪 +1"),
        "Act uninterested": wt_R("纱纪 -1"),
        "装作不感兴趣": wt_R("纱纪 -1"),
        "I want to get to know you better.": wt_G("菲奥娜 +1"),
        "我想更深入地了解你": wt_G("菲奥娜 +1"),
        "Hide Saki in the showers.": wt_G("纱纪 +1") + " " + wt_P("若纱纪≥6则触发特殊剧情(H)"),
        "把纱纪藏在淋浴间里": wt_G("纱纪 +1") + " " + wt_P("若纱纪≥6则触发特殊剧情(H)"),
        "Calmly explain the situation to the guys.": wt_R("跳过纱纪剧情"),
        "冷静地向那些家伙解释情况": wt_R("跳过纱纪剧情"),
        "Spank her": wt_B("连续点击100次触发额外彩蛋剧情"),
        "打她屁股": wt_B("连续点击100次触发额外彩蛋剧情"),
        "How've you been?": wt_G("佐伊 +1"),
        "你最近怎样？": wt_G("佐伊 +1"),
        "Goodnight, Zoe.": wt_G("佐伊 +1"),
        "晚安,佐伊。": wt_G("佐伊 +1"),
        "Impeccable": wt_G("佐伊 +1"),
        "无懈可击": wt_G("佐伊 +1"),
        "I'm looking forward to our \\\"next game\\\" then.": wt_G("纱纪 +1"),
        "我很期待我们“下一次比赛”": wt_G("纱纪 +1"),
        "Sorry. But let's stop it right there.": wt_R("纱纪 -1 · 纱纪 → 知己关系"),
        "抱歉。不过就到这儿吧": wt_R("纱纪 -1 · 纱纪 → 知己关系"),
        "I did.": wt_G("伊芙 +1"),
        "确实想你了": wt_G("伊芙 +1"),
        "I'm not taking sides here.": wt_G("伊芙 +1 · 纱纪 +1"),
        "我不偏袒任何一方": wt_G("伊芙 +1 · 纱纪 +1"),
        "Saki, Eve gets a little too playful sometimes. I'm sure she didn't mean anything bad by what she said.": wt_G("伊芙 +1") + " " + wt_R("纱纪 -1"),
        "纱纪,伊芙有时候有点太爱闹了。她说的话没有恶意": wt_G("伊芙 +1") + " " + wt_R("纱纪 -1"),
        "Eve, you knew how Saki was even before you met her, right? She's not the friendliest person out there.": wt_G("纱纪 +1") + " " + wt_R("伊芙 -1"),
        "伊芙,你在认识纱纪之前就知道她是什么样的人了吧？她可不是什么好相处的人": wt_G("纱纪 +1") + " " + wt_R("伊芙 -1"),
        "Zoe": wt_R("佐伊 -1"),
        "佐伊": wt_R("佐伊 -1"),
        "Catch her": wt_G("莱茜 +1"),
        "接住她": wt_G("莱茜 +1"),
        "Stop her": wt_R("莱茜 -1"),
        "阻止她": wt_R("莱茜 -1"),
        "Maybe I should consider showering here too.": wt_G("伊芙 +1"),
        "也许我也该考虑在这儿洗澡": wt_G("伊芙 +1"),
        "Didn't I tell you to come talk to me whenever something's on your mind?": wt_G("纱纪 +1"),
        "我不是告诉过你，有心事就来找我谈吗？": wt_G("纱纪 +1"),
        "So I don't really have much of a choice but to keep learning.": wt_R("佐伊 -1"),
        "所以我也没什么选择,只能继续学": wt_R("佐伊 -1"),
        "I want to be the best coach for all of you.": wt_G("佐伊 +1"),
        "我想成为你们所有人最好的教练": wt_G("佐伊 +1"),
        "Encourage her": wt_G("佐伊 +1"),
        "鼓励她": wt_G("佐伊 +1"),
        "Continue to be petty": wt_R("佐伊 -1"),
        "继续斤斤计较": wt_R("佐伊 -1"),
        "Hug her back": wt_G("佐伊 +2"),
        "回抱她": wt_G("佐伊 +2"),
        "You too, Zoe.": wt_R("佐伊 → 知己关系"),
        "你也是,佐伊": wt_R("佐伊 → 知己关系"),
        "Wanna play some more GS2, Zoe?": wt_B("若佐伊≥5则有更多后续剧情") + " " + wt_R("若更低则佐伊 → 知己关系"),
        "佐伊,还想再玩会儿GS2吗？": wt_B("若佐伊≥5则有更多后续剧情") + " " + wt_R("若更低则佐伊 → 知己关系"),
        "Try to make small talk": wt_G("菲奥娜 +1"),
        "试着闲聊": wt_G("菲奥娜 +1"),
        "Call out to her": wt_G("黛丝瑞 +1"),
        "呼唤她": wt_G("黛丝瑞 +1"),
        "Hug her": wt_G("莱茜 +1"),
        "抱住她": wt_G("莱茜 +1"),
        "You looked great in there.": wt_G("莱茜 +1"),
        "你刚才在里面看起来很棒": wt_G("莱茜 +1"),
        "Though I think you toning it down would help me out a bit.": wt_R("莱茜 -1"),
        "不过我觉得你稍微收敛一点会对我有帮助": wt_R("莱茜 -1"),
        "I love you just the way you are.": wt_G("莱茜 +1"),
        "我就爱你现在的样子": wt_G("莱茜 +1"),
        "Will you be mine?": wt_G("莱茜 +1"),
        "你愿意成为我的人吗？": wt_G("莱茜 +1"),
        "I remember you saying it earlier when we were talking at the park.": wt_R("莱茜 -1"),
        "我记得之前在公园聊天时你说过这话": wt_R("莱茜 -1"),
        "I remember you saying it back when we were talking over the phone the other day.": wt_G("莱茜 +1"),
        "我记得前几天通电话时你说过这话": wt_G("莱茜 +1"),
        "I remember you saying it back when we first met.": wt_R("莱茜 -1"),
        "我记得我们第一次见面时你说过这话": wt_R("莱茜 -1"),
        "I could use a hug though.": wt_P("特殊剧情(H)"),
        "不过我需要一个拥抱": wt_P("特殊剧情(H)"),
        "You have fun over there.": wt_R("莱茜 → 知己关系"),
        "你在那边玩得开心": wt_R("莱茜 → 知己关系"),
        "Return the favor": wt_G("莱茜 +1") + " " + wt_P("额外剧情"),
        "回报她": wt_G("莱茜 +1") + " " + wt_P("额外剧情"),
        "Compliment her": wt_G("黛丝瑞 +1"),
        "夸她": wt_G("黛丝瑞 +1"),
        "I wanted to see you.": wt_G("黛丝瑞 +1"),
        "我想见你": wt_G("黛丝瑞 +1"),
        "You're very cute.": wt_G("黛丝瑞 +1"),
        "你很可爱": wt_G("黛丝瑞 +1"),
        "Rest her head on your shoulder": wt_G("黛丝瑞 +2"),
        "让她把头靠在你肩膀上": wt_G("黛丝瑞 +2"),
        "Accept": wt_G("菲奥娜 +1"),
        "接受": wt_G("菲奥娜 +1"),
        "Try to comfort her": wt_R("菲奥娜 -1"),
        "试着安慰她": wt_R("菲奥娜 -1"),
        "Give her a minute": wt_G("菲奥娜 +1"),
        "给她一点时间": wt_G("菲奥娜 +1"),
        "Message Eve": wt_G("伊芙 +1"),
        "给伊芙发消息": wt_G("伊芙 +1"),
        "Send a selfie": wt_G("伊芙 +1"),
        "发张自拍": wt_G("伊芙 +1"),
        "Are you on your period?": wt_R("伊芙 -1"),
        "你来大姨妈了？": wt_R("伊芙 -1"),
        "Message Zoe": wt_G("佐伊 +1"),
        "给佐伊发消息": wt_G("佐伊 +1"),
        "Can I ask you to do a pose for me?": wt_G("若佐伊≥8则佐伊 +1") + " " + wt_R("若更低则 -1"),
        "能请你为我摆个姿势吗？": wt_G("若佐伊≥8则佐伊 +1") + " " + wt_R("若更低则 -1"),
        "Message Saki": wt_G("纱纪 +1"),
        "给纱纪发消息": wt_G("纱纪 +1"),
        "Rely on me for once. I don't want to lose you.": wt_G("若为浪漫关系则纱纪 +1") + " " + wt_R("若否则 -1"),
        "就依赖我一次吧。我不想失去你": wt_G("若为浪漫关系则纱纪 +1") + " " + wt_R("若否则 -1"),
        "Message Lexi": wt_G("莱茜 +1"),
        "给莱茜发消息": wt_G("莱茜 +1"),
        "I really want to be able to play with her.": wt_G("黛丝瑞 +1"),
        "我真的很想能和她一起打球": wt_G("黛丝瑞 +1"),
        "I'm going to spoil you like crazy.": wt_G("黛丝瑞 +1"),
        "我要把你宠上天": wt_G("黛丝瑞 +1"),
        "Say": wt_R("菲奥娜 -1"),
        "说": wt_R("菲奥娜 -1"),
        "Don't say": wt_G("菲奥娜 +1"),
        "不要说": wt_G("菲奥娜 +1"),
        "Thought you could use a hand at least.": wt_G("菲奥娜 +1"),
        "想着你至少需要搭把手。": wt_G("菲奥娜 +1"),
        "Fiona. Thoughts?": wt_G("菲奥娜 +1 · 伊芙 +1"),
        "菲奥娜，你有什么想法？": wt_G("菲奥娜 +1 · 伊芙 +1"),
        "Meet halfway.": wt_B("更多后续剧情"),
        "各退一步。": wt_B("更多后续剧情"),
        "Insist on calling her club": wt_R("菲奥娜 -2 · 菲奥娜 → 知己关系"),
        "坚持给她的俱乐部打电话。": wt_R("菲奥娜 -2 · 菲奥娜 → 知己关系"),
        "Try to cheer her up": wt_G("菲奥娜 +1"),
        "试着逗她开心。": wt_G("菲奥娜 +1"),
        "Get the tablet and ask her to go since it's already late": wt_R("佐伊 → 知己关系"),
        "拿上平板电脑，让她走，毕竟已经这么晚了。": wt_R("佐伊 → 知己关系"),
        "Let her have a closer look": wt_G("佐伊 +2"),
        "拿过来给她看看。": wt_G("佐伊 +2"),
        "Turn around.": wt_G("佐伊 +1"),
        "转过身去。": wt_G("佐伊 +1"),
        "Want to stay here for the night?": wt_P("若佐伊≥12则触发特殊剧情(H)"),
        "想留在这儿过夜吗？": wt_P("若佐伊≥12则触发特殊剧情(H)"),
        "Give her a hug": wt_G("佐伊 +1"),
        "给她一个拥抱": wt_G("佐伊 +1"),
        "Not gonna lie, I was actually hoping it did": wt_R("伊芙 -1 · 菲奥娜 -1"),
        "说实话，我其实还希望它真发生了": wt_R("伊芙 -1 · 菲奥娜 -1"),
        "I knew she wouldn't do it.": wt_G("菲奥娜 +1"),
        "我就知道她不会这么做。": wt_G("菲奥娜 +1"),
        "Check on Desiree": wt_G("黛丝瑞 +2 · 伊芙、纱纪、佐伊、菲奥娜各 +1"),
        "去看看黛丝瑞的情况": wt_G("黛丝瑞 +2 · 伊芙、纱纪、佐伊、菲奥娜各 +1"),
        "Scold Zoe": wt_G("佐伊 +1"),
        "训斥佐伊": wt_G("佐伊 +1"),
        "I'll join you.": wt_G("黛丝瑞 +1") + " " + wt_B("更多后续剧情"),
        "我来帮你。": wt_G("黛丝瑞 +1") + " " + wt_B("更多后续剧情"),
        "And if there's anyone I wouldn't mind at all causing me trouble, it's you.": wt_G("黛丝瑞 +1"),
        "如果这世上真有人给我添麻烦而我完全不介意，那个人就是你。": wt_G("黛丝瑞 +1"),
        "Kiss her": wt_G("黛丝瑞 +1") + " " + wt_P("特殊剧情(H)"),
        "吻她": wt_G("黛丝瑞 +1") + " " + wt_P("特殊剧情(H)"),
        "It's a date then": wt_G("伊芙 +1"),
        "那就算约会了。": wt_G("伊芙 +1"),
        "She looks as attractive as ever to me": wt_G("菲奥娜 +1"),
        "在我看来，她还是和从前一样迷人。": wt_G("菲奥娜 +1"),
        "Mess with her": wt_G("纱纪 +1"),
        "逗弄她": wt_G("纱纪 +1"),
        "You look lovely.": wt_G("伊芙 +1"),
        "你看起来真可爱。": wt_G("伊芙 +1"),
        "I do know you want to be a star player in volleyball": wt_R("伊芙 -1"),
        "我确实知道你想成为排球明星球员。": wt_R("伊芙 -1"),
        "Books? Oh, okay.": wt_R("伊芙 -2"),
        "书？哦，好吧。": wt_R("伊芙 -2"),
        "Books? What kind of books do you read?": wt_G("伊芙 +1"),
        "书？你读什么样的书？": wt_G("伊芙 +1"),
        "tease her back": wt_G("伊芙 +1"),
        "回撩她。": wt_G("伊芙 +1"),
        "Woof": wt_G("伊芙 +1") + " " + wt_P("特殊剧情(H)"),
        "汪。": wt_G("伊芙 +1") + " " + wt_P("特殊剧情(H)"),
        "I need to stay focused. First and foremost, I'm her coach. I was specifically hired by the institution to help the team qualify for playoffs two and a half months from now. Dean Campbell gave me a once in a lifetime chance to turn my life around. He entrusted me with this responsibility and I intend to see it through. If we get our asses beat, I can kiss my scholarship and my ass here goodbye. We don't have much time so I need to prioritize my job first. And think about it. There is a chance I can also get fired if I get caught fooling around with my players. I can't risk it. I only have one chance at this and I can't waste it.": wt_R("伊芙 → 知己关系"),
        "我必须保持专注。首先，我是她的教练。我是校方专门聘请来帮助球队在两个半月后打进季后赛的。坎贝尔院长给了我一次改变人生的机会。他把这份责任托付给我，我打算坚持到底。如果我们被打爆，我就得跟我的奖学金和这里的一切说再见。我们时间不多了，所以我必须先把工作放在第一位。而且你想想——如果被人发现我跟我的球员乱搞，我也可能会被开除。我不能冒这个险。我只有这一次机会，我不能浪费。": wt_R("伊芙 → 知己关系"),
    }

    wt_en_to_cn_captions = {
        "Accept": "接受",
        "Act uninterested": "装作不感兴趣",
        "Americano": "美式咖啡",
        "And if there's anyone I wouldn't mind at all causing me trouble, it's you.": "如果这世上真有人给我添麻烦而我完全不介意，那个人就是你。",
        "Are you on your period?": "你来大姨妈了？",
        "Ask Bianca to tell Zoe to take it easy": "让比安卡告诉佐伊要劳逸结合",
        "Ask for a sip of her coffee": "问她能不能喝一口她的咖啡",
        "Ask if she wants something": "问问她想要点什么",
        "Be sarcastic": "出言讽刺",
        "Because you're worth it.": "因为你值得",
        "Books? Oh, okay.": "书？哦，好吧。",
        "Books? What kind of books do you read?": "书？你读什么样的书？",
        "Bring her some flowers and apologize": "带些花去向她道歉",
        "Call out to her": "呼唤她",
        "Calmly explain the situation to the guys.": "冷静地向那些家伙解释情况",
        "Can I ask you to do a pose for me?": "能请你为我摆个姿势吗？",
        "Capuccino": "卡布奇诺",
        "Carpentry": "木工",
        "Carry her books for her": "帮她拿书",
        "Catch her": "接住她",
        "Check on Desiree": "去看看黛丝瑞的情况",
        "Compliment her": "夸她",
        "Continue to be petty": "继续斤斤计较",
        "Didn't I tell you to come talk to me whenever something's on your mind?": "我不是告诉过你，有心事就来找我谈吗？",
        "Do it": "要",
        "Don't play along": "不配合",
        "Don't say": "不要说",
        "Encourage her": "鼓励她",
        "Eve, you knew how Saki was even before you met her, right? She's not the friendliest person out there.": "伊芙,你在认识纱纪之前就知道她是什么样的人了吧？她可不是什么好相处的人",
        "Fiona. Thoughts?": "菲奥娜，你有什么想法？",
        "Flirty response": "调情地回复",
        "Get the tablet and ask her to go since it's already late": "拿上平板电脑，让她走，毕竟已经这么晚了。",
        "Give her a hug": "给她一个拥抱",
        "Give her a minute": "给她一点时间",
        "Goodnight, Zoe.": "晚安,佐伊。",
        "Hide Saki in the showers.": "把纱纪藏在淋浴间里",
        "How've you been?": "你最近怎样？",
        "Hug her": "抱住她",
        "Hug her back": "回抱她",
        "I could use a hug though.": "不过我需要一个拥抱",
        "I did.": "确实想你了",
        "I do know you want to be a star player in volleyball": "我确实知道你想成为排球明星球员。",
        "I fell off the stairs": "我从楼梯上摔下去了",
        "I jerked off while thinking of you twice.": "我想着你的画面撸了两回",
        "I knew she wouldn't do it.": "我就知道她不会这么做。",
        "I like being with you.": "我喜欢和你在一起",
        "I love you just the way you are.": "我就爱你现在的样子",
        "I need to stay focused. First and foremost, I'm her coach. I was specifically hired by the institution to help the team qualify for playoffs two and a half months from now. Dean Campbell gave me a once in a lifetime chance to turn my life around. He entrusted me with this responsibility and I intend to see it through. If we get our asses beat, I can kiss my scholarship and my ass here goodbye. We don't have much time so I need to prioritize my job first. And think about it. There is a chance I can also get fired if I get caught fooling around with my players. I can't risk it. I only have one chance at this and I can't waste it.": "我必须保持专注。首先，我是她的教练。我是校方专门聘请来帮助球队在两个半月后打进季后赛的。坎贝尔院长给了我一次改变人生的机会。他把这份责任托付给我，我打算坚持到底。如果我们被打爆，我就得跟我的奖学金和这里的一切说再见。我们时间不多了，所以我必须先把工作放在第一位。而且你想想——如果被人发现我跟我的球员乱搞，我也可能会被开除。我不能冒这个险。我只有这一次机会，我不能浪费。",
        "I really do want you, Zoe.": "我真的想要你,佐伊",
        "I really want to be able to play with her.": "我真的很想能和她一起打球",
        "I remember you saying it back when we first met.": "我记得我们第一次见面时你说过这话",
        "I remember you saying it back when we were talking over the phone the other day.": "我记得前几天通电话时你说过这话",
        "I remember you saying it earlier when we were talking at the park.": "我记得之前在公园聊天时你说过这话",
        "I want to be the best coach for all of you.": "我想成为你们所有人最好的教练",
        "I want to get to know you better.": "我想更深入地了解你",
        "I want you there.": "我想要你来",
        "I wanted to see you.": "我想见你",
        "I'd like to apologize properly. Can we talk?": "我想郑重跟你道个歉,咱们能见一面聊聊吗？",
        "I'll be happy to have you, Saki.": "我很高兴能拥有你,纱纪",
        "I'll join you.": "我来帮你。",
        "I'm fine. It's just a little bruise": "我没事。只是块小瘀青罢了",
        "I'm going to spoil you like crazy.": "我要把你宠上天",
        "I'm looking forward to our \\\"next game\\\" then.": "我很期待我们“下一次比赛”",
        "I'm not taking sides here.": "我不偏袒任何一方",
        "I've come to know you better.": "我比你想的更了解你",
        "Impeccable": "无懈可击",
        "Insist on calling her club": "坚持给她的俱乐部打电话。",
        "Introduce yourself this time": "这次先自我介绍",
        "It was alright...": "还行吧……",
        "It was the best thing I could think of to make it up to you.": "这是我能想到的最好的补偿你的办法了",
        "It's a date then": "那就算约会了。",
        "It's not that I'm not interested at all...": "也不是说我完全不感兴趣……",
        "It's pretty hard not to miss you.": "不想你才怪",
        "Join her": "和她一起加入",
        "Just take the flowers already. You're making me look bad here.": "快把花收下吧。你这让我也很为难",
        "Kindly refuse": "委婉拒绝",
        "Kiss her": "吻她",
        "Latte": "拿铁",
        "Left": "左",
        "Let anger take over": "让愤怒占据上风",
        "Let her have a closer look": "拿过来给她看看。",
        "Maybe I should consider showering here too.": "也许我也该考虑在这儿洗澡",
        "Maybe someday": "也许有一天吧",
        "Meet halfway.": "各退一步。",
        "Mess with her": "逗弄她",
        "Message Eve": "给伊芙发消息",
        "Message Eve goodnight": "给伊芙发晚安消息",
        "Message Lexi": "给莱茜发消息",
        "Message Lexi and ask how she is": "给莱茜发消息，问问她怎么样",
        "Message Saki": "给纱纪发消息",
        "Message Zoe": "给佐伊发消息",
        "No way!": "没门！",
        "None of your business": "这个不关你的事",
        "Not gonna lie, I was actually hoping it did": "说实话，我其实还希望它真发生了",
        "Not really.": "其实不然",
        "Pat her head": "摸摸她的头",
        "Play along": "配合",
        "Rely on me for once. I don't want to lose you.": "就依赖我一次吧。我不想失去你",
        "Rest her head on your shoulder": "让她把头靠在你肩膀上",
        "Return the favor": "回报她",
        "Right": "右",
        "Saki, Eve gets a little too playful sometimes. I'm sure she didn't mean anything bad by what she said.": "纱纪,伊芙有时候有点太爱闹了。她说的话没有恶意",
        "Say": "说",
        "Say a snarky comment": "说句刻薄话",
        "Say hi": "打个招呼",
        "Scold Zoe": "训斥佐伊",
        "Send a selfie": "发张自拍",
        "She looks as attractive as ever to me": "在我看来，她还是和从前一样迷人。",
        "She's with her friends, leave them be": "她和朋友们在一起，别去打扰她们",
        "So I don't really have much of a choice but to keep learning.": "所以我也没什么选择,只能继续学",
        "Someone blonde, tanned, spontaneous, and a party girl.": "金发、小麦色皮肤、随性自然，还是个派对女孩。",
        "Someone kind, brimming with positivity, and darker skinned.": "一个善良、充满正能量、黑皮肤的女生？",
        "Someone prim and proper, blonde, and behaves like a lady.": "一个端庄得体、金发碧眼、举止淑女的人？",
        "Someone sweet, loves to tease you, brunette, and wears glasses.": "一个温柔体贴、喜欢捉弄人、深褐色头发、戴眼镜的女生？",
        "Someone tatooed and pierced, cool, and mysterious.": "一个有纹身、打耳洞、酷酷的、很神秘的人？",
        "Someone with Asian features, black hair, a petite build, and just makes you feel like you can't leave her alone": "有亚洲人特征、黑发、身材娇小，让你觉得不能抛下她不管的人",
        "Sorry. But let's stop it right there.": "抱歉。不过就到这儿吧",
        "Spank her": "打她屁股",
        "Stop her": "阻止她",
        "Take her hand": "牵起她的手",
        "Tap her head with the clip board": "用写字板轻敲她的头",
        "Tease her": "调戏她",
        "Tease her back": "反过来逗她一下",
        "Tequila": "龙舌兰酒",
        "Thank her": "感谢她",
        "Though I think you toning it down would help me out a bit.": "不过我觉得你稍微收敛一点会对我有帮助",
        "Thought you could use a hand at least.": "想着你至少需要搭把手。",
        "Touch her breasts": "触摸她的胸部",
        "Try to cheer her up": "试着逗她开心。",
        "Try to comfort her": "试着安慰她",
        "Try to make small talk": "试着闲聊",
        "Turn around.": "转过身去。",
        "Wanna play some more GS2, Zoe?": "佐伊,还想再玩会儿GS2吗？",
        "Wanna touch..?": "想摸吗..？",
        "Want me to go with you to the place? It's a little late already.": "要我送你到那个地方吗？已经有点晚了",
        "Want to stay here for the night?": "想留在这儿过夜吗？",
        "Will you be mine?": "你愿意成为我的人吗？",
        "Woof": "汪。",
        "You have a lot of muscle knots on your back, let me take care of them.": "你肩膀和后背好多地方都是硬的",
        "You have fun over there.": "你在那边玩得开心",
        "You know what? I think I actually might.": "你知道吗？我觉得我可能还真会",
        "You look good.": "你看起来不错",
        "You look lovely with you hair up.": "你把头发盘起来真好看",
        "You look lovely.": "你看起来真可爱。",
        "You looked great in there.": "你刚才在里面看起来很棒",
        "You too, Zoe.": "你也是,佐伊",
        "You're beautiful, Desiree.": "你很美,黛丝瑞",
        "You're very cute.": "你很可爱",
        "Zoe": "佐伊",
        "tease her back": "回撩她。",
    }

    walkthrough_hints_ctx = {
        ("Yes", "Give up?"): wt_R("坏结局！"),
        ("Don't", "Do it"): wt_G("下个选项 莱茜 +1"),
        ("Don't", "Hug her"): wt_R("莱茜 -1"),
        ("Alright, then.", "Want to stay here for the night?"): wt_R("佐伊 → 知己关系"),
        ("Don't", "Kiss her"): wt_R("黛丝瑞 → 知己关系"),
        ("是", "放弃吗？"): wt_R("坏结局！"),
        ("不要", "要"): wt_G("下个选项 莱茜 +1"),
        ("不要", "抱住她"): wt_R("莱茜 -1"),
        ("好吧,那就这样", "想留在这儿过夜吗？"): wt_R("佐伊 → 知己关系"),
        ("不要", "吻她"): wt_R("黛丝瑞 → 知己关系"),
    }

    walkthrough_hints_dynamic = {
        "Ask if the seat is empty.": lambda: wt_G('伊芙心情 +1') if wt_flag('flowers1') else '',
        "问问座位是不是空的": lambda: wt_G('伊芙心情 +1') if wt_flag('flowers1') else '',
        "Sit down without asking.": lambda: wt_R('伊芙心情 -2') if wt_flag('flowers1') else wt_R('伊芙心情 -1'),
        "不问就直接坐下": lambda: wt_R('伊芙心情 -2') if wt_flag('flowers1') else wt_R('伊芙心情 -1'),
        "I do know you're good at cooking": lambda: wt_R('伊芙 -1') if wt_flag('libraryeve') else wt_G('伊芙 +1'),
        "我确实知道你厨艺很好。": lambda: wt_R('伊芙 -1') if wt_flag('libraryeve') else wt_G('伊芙 +1'),
    }

    def wt_current_menu_captions():
        try:
            node = renpy.game.script.lookup(renpy.game.context().current)
            items = getattr(node, "items", None)
            if items is None:
                return None
            return [i[0] for i in items if i and i[0]]
        except Exception:
            return None

    def wt_find_orig_caption(caption, siblings):
        caption_clean = caption.strip()
        if caption_clean in walkthrough_hints or caption_clean in walkthrough_hints_dynamic:
            return caption_clean
        if siblings:
            for cand in siblings:
                cand_clean = cand.strip()
                if cand_clean == caption_clean:
                    return cand_clean
                try:
                    if renpy.translation.translate_string(cand_clean).strip() == caption_clean:
                        return cand_clean
                except Exception:
                    pass
                try:
                    if renpy.translation.translate_string(cand).strip() == caption_clean:
                        return cand_clean
                except Exception:
                    pass
        return caption_clean

    def wt_hint_for(caption, siblings):
        for sib in siblings:
            h = walkthrough_hints_ctx.get((caption, sib))
            if h:
                return h
            try:
                sib_trans = renpy.translation.translate_string(sib).strip()
                h = walkthrough_hints_ctx.get((caption, sib_trans))
                if h:
                    return h
            except Exception:
                pass
        dyn = walkthrough_hints_dynamic.get(caption)
        if dyn is not None:
            try:
                return dyn()
            except Exception:
                return ""
        return walkthrough_hints.get(caption, "")

    _wt_previous_filter = config.say_menu_text_filter

    def wt_menu_text_filter(s):
        if _wt_previous_filter is not None:
            s = _wt_previous_filter(s)
        try:
            siblings = wt_current_menu_captions()
            if siblings is None:
                siblings = []
            s_clean = s.strip()
            key = wt_find_orig_caption(s_clean, siblings)

            # 先将选项正文转换为中文，避免附加提示后 textbutton 无法匹配翻译字典
            trans = None
            try:
                trans = renpy.translation.translate_string(s)
            except Exception:
                pass
            if not trans or trans == s:
                trans = wt_en_to_cn_captions.get(s_clean)
            if trans:
                s = trans

            big = bool(wt_compact_from) and len(siblings) >= wt_compact_from
            if persistent.wt_hints_on:
                hint = wt_hint_for(key, siblings)
                if not hint and key != s_clean:
                    hint = wt_hint_for(s_clean, siblings)
                if hint:
                    if big:
                        s = (s + wt_compact_separator + "{size=" + str(wt_compact_size) + "}" + hint + "{/size}")
                    else:
                        s = s + wt_separator + hint
            if big and wt_compact_text_size:
                s = "{size=" + str(wt_compact_text_size) + "}" + s + "{/size}"
        except Exception:
            pass
        return s

    config.say_menu_text_filter = wt_menu_text_filter

    if wt_choice_spacing is not None:
        try:
            style.choice_vbox.spacing = wt_choice_spacing
        except Exception:
            pass

    wt_choice_skin = True
    wt_choice_img_idle  = "BladeSSRMod/ChoiceUI/choice_idle.png"
    wt_choice_img_hover = "BladeSSRMod/ChoiceUI/choice_hover.png"
    wt_choice_corner = 32
    wt_choice_xpad = 30
    wt_choice_ypad = 12
    wt_choice_hover_color = "#FFD166"

init 999 python:
    wt_skin_debug = False
    wt_skin_status = "WT skin: not run"
    wt_skin_ok = False
    if not wt_choice_skin:
        wt_skin_status = "WT skin: disabled (wt_choice_skin = False)"
    elif not (renpy.loadable(wt_choice_img_idle) and renpy.loadable(wt_choice_img_hover)):
        wt_skin_status = "WT skin: IMAGES NOT FOUND in game/" + wt_choice_img_idle
    else:
        wt_skin_ok = True
        wt_skin_status = "WT skin: choice screen override active"

    if wt_choice_spacing is None:
        wt_choice_spacing_eff = gui.choice_spacing
    else:
        wt_choice_spacing_eff = wt_choice_spacing

    if wt_skin_debug and "wt_skin_debug" not in config.overlay_screens:
        config.overlay_screens.append("wt_skin_debug")

init 5:
    screen choice(items):
        style_prefix "choice"
        vbox:
            spacing wt_choice_spacing_eff
            for i in items:
                if wt_skin_ok:
                    textbutton i.caption action i.action:
                        background Frame(wt_choice_img_idle, wt_choice_corner, wt_choice_corner, tile=False)
                        idle_background Frame(wt_choice_img_idle, wt_choice_corner, wt_choice_corner, tile=False)
                        hover_background Frame(wt_choice_img_hover, wt_choice_corner, wt_choice_corner, tile=False)
                        selected_idle_background Frame(wt_choice_img_idle, wt_choice_corner, wt_choice_corner, tile=False)
                        selected_hover_background Frame(wt_choice_img_hover, wt_choice_corner, wt_choice_corner, tile=False)
                        left_padding wt_choice_xpad
                        right_padding wt_choice_xpad
                        top_padding wt_choice_ypad
                        bottom_padding wt_choice_ypad
                        text_hover_color wt_choice_hover_color
                else:
                    textbutton i.caption action i.action

    screen choice_custom(items):
        use choice(items)

screen wt_skin_debug():
    zorder 300
    text "[wt_skin_status]":
        size 22
        color "#ffffff"
        outlines [ (2, "#000000", 0, 0) ]
        xpos 10
        ypos 10
