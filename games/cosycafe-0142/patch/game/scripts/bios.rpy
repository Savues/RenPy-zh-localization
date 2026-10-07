init python:
    real_names = {
            "Headmistress": "Alison",
            "Ms. Takamura": "Misaki",
            "Lucy's Mother": "Lucy's Mother",
        }
    items = {
        "main": { # DO NOT TOUCH THE H VALUES! 
        #Lucy
            1  : { "name" : [] , "color": "#d97cd7", "age" : "18", "occupation": [], "note": [], "family": []},
        #Victoria
            2  : { "name" : [] , "color": "#4fb0f0", "age" : "18", "occupation": [], "note": [], "family": []},
        #Sarah
            3  : { "name" : [] , "color": "#24ab20", "age" : "18", "occupation": [], "note": [], "family": []},
        #Akatsuki
            4  : { "name" : [] , "color": "#e31728", "age" : "18", "occupation": [], "note": [], "family": []},
        #Rachel
            5  : { "name" : [] , "color": "#edab1c", "age" : "18", "occupation": [], "note": [], "family": []},
        #Hannah
            6  : { "name" : [] , "color": "#80370f", "age" : "18", "occupation": [], "note": [], "family": []},
        #Alison
            7  : { "name" : [] , "color": "#692460", "age" : "27", "occupation": [], "note": [], "family": []},
        #Misaki
            8  : { "name" : [] , "color": "#fc0377", "age" : "22", "occupation": [], "note": [], "family": []},
        #Akari
            9  : { "name" : [] , "color": "#de8a91", "age" : "20", "occupation": [], "note": [], "family": []},
        #Catherine
            10 : { "name" : [] , "color": "#edca6b", "age" : "18", "occupation": [], "note": [], "family": []},
        #Elizabeth
            11 : { "name" : [] , "color": "#776de3", "age" : "20", "occupation": [], "note": [], "family": []},
        #Annabelle
            12 : { "name" : [] , "color": "#ffffff", "age" : "20", "occupation": [], "note": [], "family": []},
        },
        "side": {
        #Mika
            1  : { "name" : [] , "color": "#ff82ee", "age" : "18", "occupation": [], "note": [], "family": []},
        #Brian
            2  : { "name" : [] , "color": "#00ff9d", "age" : "18", "occupation": [], "note": [], "family": []},
        #Lenny
            3  : { "name" : [] , "color": "#0eda9f", "age" : "18", "occupation": [], "note": [], "family": []},
        #Baker
            4  : { "name" : [] , "color": "#7a3d20", "age" : "64", "occupation": [], "note": [], "family": []},
        #Mr Takamura
            5  : { "name" : [] , "color": "#7a3d20", "age" : "48", "occupation": [], "note": [], "family": []},
        #Lucy's Mother
            6  : { "name" : [] , "color": "#7a3d20", "age" : "49", "occupation": [], "note": [], "family": []},
        #Chloe
            7  : { "name" : [] , "color": "#919190", "age" : "18", "occupation": [], "note": [], "family": []},
        #Danny
            8  : { "name" : [] , "color": "#00055c", "age" : "25", "occupation": [], "note": [], "family": []},
        #Lily
            9  : { "name" : [] , "color": "#1b7519", "age" : "36", "occupation": [], "note": [], "family": []},
        #Mr Hamilton
            10 : { "name" : [] , "color": "#8f8e8d", "age" : "55", "occupation": [], "note": [], "family": []},
        #Cassandra
            11 : { "name" : [] , "color": "#00bd8a", "age" : "42", "occupation": [], "note": [], "family": []},
        # #Annabelle
        #     12 : { "name" : [] , "color": "#ffffff", "age" : "20", "occupation": [], "note": [], "family": []},
        #Mary
            13 : { "name" : [] , "color": "#805928", "age" : "48", "occupation": [], "note": [], "family": []},
        #Reginald
            14 : { "name" : [] , "color": "#999571", "age" : "46", "occupation": [], "note": [], "family": []},
        #Sarah Sis 1
            15 : { "name" : [] , "color": "#e0ff82", "age" : "20", "occupation": [], "note": [], "family": []},
        #Mira
            16 : { "name" : [] , "color": "#ffa1b5", "age" : "20", "occupation": [], "note": [], "family": []},
        #Samantha
            17 : { "name" : [] , "color": "#db87ff", "age" : "20", "occupation": [], "note": [], "family": []},
        #Harriet
            18 : { "name" : [] , "color": "#611b00", "age" : "24", "occupation": [], "note": [], "family": []},
        #Mr Gilbert
            19 : { "name" : [] , "color": "#5e596e", "age" : "63", "occupation": [], "note": [], "family": []},
        #Gloria Russell
            20 : { "name" : [] , "color": "#329973", "age" : "61", "occupation": [], "note": [], "family": []},
        #Mr Russell
            21 : { "name" : [] , "color": "#164d38", "age" : "46", "occupation": [], "note": [], "family": []},
        #Akane
            22 : { "name" : [] , "color": "#592227", "age" : "41", "occupation": [], "note": [], "family": []},
        #Ella
            23 : { "name" : [] , "color": "#ffc582", "age" : "13", "occupation": [], "note": [], "family": []},
        #Ivy
            24 : { "name" : [] , "color": "#ffa43b", "age" : "11", "occupation": [], "note": [], "family": []},
        #HeadFun
            25 : { "name" : [] , "color": "#19692e", "age" : "80", "occupation": [], "note": [], "family": []},
        #Eleanor
            26 : { "name" : [] , "color": "#ffc582", "age" : "49", "occupation": [], "note": [], "family": []},

        }
    }

    current_state = "main"
    def refresh_character_stats():
        global items
        for character_id, character_data in items["main"].items():
            character_data['name']       = []
            character_data['occupation'] = []
            character_data['note']       = []
            character_data['family']     = []
        for character_id, character_data in items["side"].items():
            character_data['name']       = []
            character_data['occupation'] = []
            character_data['note']       = []
            character_data['family']     = []
    
#############################################################################################################################################################################################################
#############################################################################################################################################################################################################
    #Lucy

        #Character Details
        if persistent.characters_lucy:
            items['main'][1]['name'].append('露西')
        if persistent.characters_lucy_name:
            items['main'][1]['name'].append('库珀')
        if persistent.characters_lucy_job1:
            items['main'][1]['occupation'].append('学生')
        if persistent.characters_lucy_job2:
            items['main'][1]['occupation'].append('女招待')
        if persistent.characters_lucy_family1:
            items['main'][1]['family'].append('母亲')
        if persistent.characters_lucy_family2:
            items['main'][1]['family'].append('父亲（关系不睦）')
        
        #Notes
        items['main'][1]['note'].append('某天走进你咖啡馆的一个害羞女孩。')
        if persistent.characters_lucy_note1:
            items['main'][1]['note'].append('稍微熟络之后，露西成了你的女招待长。')
        if persistent.characters_lucy_note2:
            items['main'][1]['note'].append('露西为了逃离暴虐的母亲，搬来和你同住。')
        if persistent.characters_lucy_note3:
            items['main'][1]['note'].append('露西成为了你的第一个女朋友。')


    ##################################################################################################################################
    #Victoria
    
        #Character Details
        if persistent.characters_victoria:
            items['main'][2]['name'].append('维多利亚')
        if persistent.characters_victoria_name:
            items['main'][2]['name'].append('特纳')
        if persistent.characters_victoria_job1:
            items['main'][2]['occupation'].append('学生')
        if persistent.characters_victoria_job2:
            items['main'][2]['occupation'].append('女招待')
        if persistent.characters_victoria_family1:
            items['main'][2]['family'].append('母亲（已故）')
        if persistent.characters_victoria_family2:
            items['main'][2]['family'].append('父亲（关系不睦）')
        if persistent.characters_victoria_family3:
            items['main'][2]['family'].append('哥哥（丹尼）')
        
        #Notes
        items['main'][2]['note'].append('你在通学列车上遇见的刻薄女孩。')
        if persistent.characters_victoria_note1:
            items['main'][2]['note'].append('维多利亚苦苦哀求要当女招待。你答应了她，条件是她得听话。')
        if persistent.characters_victoria_note2:
            items['main'][2]['note'].append('维多利亚开始做女招待后，你们渐渐熟络起来，最后她成了你的女朋友，还搬进了咖啡馆。')
        if persistent.characters_victoria_note3:
            items['main'][2]['note'].append('薇琪的父亲在列车上遇到她，当场情绪崩溃。她向你袒露了一些藏起来的心结，让你有些担心她。')
        if persistent.characters_victoria_note4:
            items['main'][2]['note'].append('之后一整天他反复联系她，直到她在被毁的咖啡馆废墟上冲他吼了一句「别再来烦我」。')


    ##################################################################################################################################
    # #Sarah
    
        #Character Details
        if persistent.characters_sarah:
            items['main'][3]['name'].append('莎拉')
        if persistent.characters_sarah_foundingfamily:
            items['main'][3]['name'].append('汉密尔顿（创始家族）')
        if persistent.characters_sarah_job1:
            items['main'][3]['occupation'].append('学生')
        if persistent.characters_sarah_job2:
            items['main'][3]['occupation'].append('市场企划兼女招待')
        if persistent.characters_sarah_family1:
            items['main'][3]['family'].append('母亲（莉莉）')
        if persistent.characters_sarah_family2:
            items['main'][3]['family'].append('父亲（汉密尔顿先生）')
        if persistent.characters_sarah_family3:
            items['main'][3]['family'].append('姐妹们')
        
        #Notes
        items['main'][3]['note'].append('给你做衣服的小恶魔。露西最好的朋友。')
        if persistent.characters_sarah_note1:
            items['main'][3]['note'].append('莎拉成了你的市场企划兼兼职女招待。')
        if persistent.characters_sarah_note2:
            items['main'][3]['note'].append('莎拉因为网上的角色扮演被人盯上了，你不得不保护她。')
        if persistent.characters_sarah_note3:
            items['main'][3]['note'].append('跟踪莎拉的人其实都是她父亲针对你的布局的一部分。作为回应，莎拉决定以双重间谍的身份与他作对来帮你。')
        if persistent.characters_sarah_note4:
            items['main'][3]['note'].append('经过几周越来越亲近，莎拉终于成了你的第四位女朋友。')


    ##################################################################################################################################
    # #Akatsuki
    
        #Character Details
        if persistent.characters_akatsuki:
            items['main'][4]['name'].append('晓月')
            items['main'][4]['name'].append('高村')
        if persistent.characters_akatsuki_job1:
            items['main'][4]['occupation'].append('学生')
        if persistent.characters_akatsuki_job2:
            items['main'][4]['occupation'].append('见习厨师')
        if persistent.characters_akatsuki_family1:
            items['main'][4]['family'].append('父亲（高村先生）')
        if persistent.characters_akatsuki_family4:
            items['main'][4]['family'].append('母亲（茜）')
        if persistent.characters_akatsuki_family3:
            items['main'][4]['family'].append('姐姐（明里）')
        if persistent.characters_akatsuki_family2:
            items['main'][4]['family'].append('表姐（美咲）')
        
        #Notes
        items['main'][4]['note'].append('一个寡言的女孩，你在一场厨艺对决中赢下了她。她后来成了你的学徒。')
        if persistent.characters_akatsuki_note1:
            items['main'][4]['note'].append('晓月答应用爷爷的厨艺秘方，换取成为你的专属猫娘。')
        if persistent.characters_akatsuki_note2:
            items['main'][4]['note'].append('你和晓月决定联手，击败她那位天才姐姐。')
        if persistent.characters_akatsuki_note3:
            items['main'][4]['note'].append('你发现晓月一直在替父亲对你撒谎。最终她选择了你，成了你的女朋友。')
        if persistent.characters_akatsuki_note4:
            items['main'][4]['note'].append('多亏她母亲从中斡旋，晓月与父亲和解了，当年因她选择你而裂开的家族关系也随之弥合。')


    ##################################################################################################################################
    #Rachel
    
        #Character Details
        if persistent.characters_rachel:
            items['main'][5]['name'].append('瑞秋')
        if persistent.characters_rachel_job1:
            items['main'][5]['occupation'].append('学生')
        
        #Notes
        items['main'][5]['note'].append('学生会长，外加一个疯狂女权主义者。')
        if persistent.characters_rachel_note1:
            items['main'][5]['note'].append('瑞秋似乎把「解救」你的那些女孩当成了使命，方式就是不断纠缠你。')
        if persistent.characters_rachel_note2:
            items['main'][5]['note'].append('你撞见她在办公室窥探，抓住这点把柄，逼她答应不再来烦你。')
        if persistent.characters_rachel_note3:
            items['main'][5]['note'].append('瑞秋承认自己偷走了检票簿。你让她去莎拉的社团活动室，这样才好给她记过。')
        if persistent.characters_rachel_note4:
            items['main'][5]['note'].append('和汉娜她们聊过之后，你决定给瑞秋打一顿屁股。可真到了那一刻，你下不去手，反而冲她吼了起来。她哭着跑出了房间，羞辱难当。')


    ##################################################################################################################################
    # Hannah
    
        #Character Details
        if persistent.characters_hannah:
            items['main'][6]['name'].append('汉娜')
        if persistent.characters_hannah_foundingfamily:
            items['main'][6]['name'].append('吉尔伯特（创始家族）')
        if persistent.characters_hannah_job1:
            items['main'][6]['occupation'].append('学生')
        if persistent.characters_hannah_family1:
            items['main'][6]['family'].append('姐姐（埃莉森）')
        if persistent.characters_hannah_family2:
            items['main'][6]['family'].append('父亲（吉尔伯特先生）')
        if persistent.characters_harriet:
            items['main'][6]['family'].append('姐姐（哈丽雅特）')
        
        #Notes
        items['main'][6]['note'].append('一个优柔寡断的女孩。她和欺负露西的那帮人走得很近，但没人在时看起来还挺不错。')
        if persistent.characters_hannah_note1:
            items['main'][6]['note'].append('汉娜和布莱恩之间有某种「政治婚约」，校长想让你把它搅黄。')
        if persistent.characters_hannah_note2:
            items['main'][6]['note'].append('校长决定让汉娜到咖啡馆当女招待。你勉强同意。')
        if persistent.characters_hannah_note3:
            items['main'][6]['note'].append('每当布莱恩对她呼来喝去，汉娜就喜欢用和你做些下流事来当作一种反抗。')


    ##################################################################################################################################
    #Headmistress
    
        #Character Details

        # if persistent.characters_headmistress:
        #     if 'Headmistress' not in items['main'][7]['name']:
        #         items['main'][7]['name'].insert(0, 'Headmistress')
        # if persistent.characters_headmistress_name:
        #     if 'Alison' in items['main'][7]['name']:
        #         items['main'][7]['name'].remove('Alison')
        #     items['main'][7]['name'].insert(0, 'Alison')

        if persistent.characters_headmistress:
            if 'Headmistress' not in items['main'][7]['name'] and 'Alison' not in items['main'][7]['name']:
                items['main'][7]['name'].insert(0, 'Headmistress')
        if persistent.characters_headmistress_name:
            if 'Headmistress' in items['main'][7]['name']:
                items['main'][7]['name'].remove('Headmistress')
            items['main'][7]['name'].insert(0, 'Alison')

        if persistent.characters_headmistress_foundingfamily:
            items['main'][7]['name'].append('吉尔伯特（创始家族）')
        if persistent.characters_headmistress_job1:
            items['main'][7]['occupation'].append('校长')
        if persistent.characters_headmistress_family1:
            items['main'][7]['family'].append('妹妹（汉娜）')
        if persistent.characters_headmistress_family2:
            items['main'][7]['family'].append('父亲（吉尔伯特先生）')
        
        #Notes
        items['main'][7]['note'].append('芬兹伯勒学院的校长。以这个职位而论，她看起来相当年轻。')
        if persistent.characters_headmistress_note1:
            items['main'][7]['note'].append('校长对你爷爷的事讳莫如深，你很想知道原因。')
        if persistent.characters_headmistress_note2:
            items['main'][7]['note'].append('看来她是想把你挡在创始家族之外，可你逼她说出了实情。现在她希望你能靠取得一定的地位，把她的妹妹汉娜从那桩婚约里救出来。')
        if persistent.characters_headmistress_note3:
            items['main'][7]['note'].append('校长同意做你的秘书，替你处理创始家族的事务。你能不能信任她，只有时间能证明。')
        if persistent.characters_headmistress_note4:
            items['main'][7]['note'].append('埃莉森有一个大计划。她要打破创始家族之间现有的平衡，建立属于你自己的势力。')


    ##################################################################################################################################
    # #Taka
    
        #Character Details

        # if persistent.characters_taka:
        #     if 'Ms. Takamura' not in items['main'][8]['name']:
        #         items['main'][8]['name'].insert(0, 'Ms. Takamura')
        # if persistent.characters_taka_name:
        #     if 'Misaki' in items['main'][8]['name']:
        #         items['main'][8]['name'].remove('Misaki')
        #     items['main'][8]['name'].insert(0, 'Misaki')

        if persistent.characters_taka:
            if 'Miss Takamura' not in items['main'][8]['name'] and 'Misaki' not in items['main'][8]['name']:
                items['main'][8]['name'].insert(0, 'Miss Takamura')
        if persistent.characters_taka_name:
            if 'Miss Takamura' in items['main'][8]['name']:
                items['main'][8]['name'].remove('Miss Takamura')
            items['main'][8]['name'].insert(0, 'Misaki')
            items['main'][8]['name'].append('高村')

        if persistent.characters_taka_job1:
            items['main'][8]['occupation'].append('老师')
        if persistent.characters_taka_family1:
            items['main'][8]['family'].append('表姐妹（晓月与明里）、叔叔（高村先生（Wong？））')
        if persistent.characters_akane:
            items['main'][8]['family'].append('姑妈（茜）')
        
        #Notes
        items['main'][8]['note'].append('你在学校里的老师。她非常年轻，显然没什么经验。')
        if persistent.characters_taka_note1:
            items['main'][8]['note'].append('你在电车上摸了她一把，她似乎挺享受，却又神色纠结。')
        if persistent.characters_taka_note2:
            items['main'][8]['note'].append('在多次摸奶之后，她吐露心声说自己想要改变。她想变成一个更外向、更自信的女人，也许还能成为你的专属肉便器。')
        if persistent.characters_taka_note3:
            items['main'][8]['note'].append('事情并非如你所料，但你的秘密已经暴露了。高村小姐——也就是你现在知道的美咲——在课堂上正好发现你就是那个「神秘男人」。也许现在，你们的关系可以正式开始了。')
        if persistent.characters_taka_note4:
            items['main'][8]['note'].append('和美咲在学校里幽会了几次之后，你定下了计划：提升她的自信，把她培养成你的专属肉便器——就在她那位强势父母眼皮底下。')


    ##################################################################################################################################
    # #Akari
    
        #Character Details

        items['main'][9]['occupation'].append('天才厨师')

        if persistent.characters_akari:
            items['main'][9]['name'].append('明里')
            items['main'][9]['name'].append('高村')
        if persistent.characters_akatsuki_family1:
            items['main'][9]['family'].append('父亲（高村先生）')
        if persistent.characters_akatsuki_family4:
            items['main'][9]['family'].append('母亲（茜）')
        if persistent.characters_akatsuki_family3:
            items['main'][9]['family'].append('妹妹（晓月）')
        if persistent.characters_akatsuki_family2:
            items['main'][9]['family'].append('表妹（美咲）')

        #Notes
        items['main'][9]['note'].append('一个张扬外放的女孩。她在厨艺对决中把你彻底打败，证明了自己在厨房里的天赋。')
        if persistent.characters_akari_note1:
            items['main'][9]['note'].append('自从初次见面以来调情不断，有一天明里来到你的办公室，多少有些暗示地开口要你的裸照。她回应的方式却天真得惊人。')


    ##################################################################################################################################
    # #Catherine
    
        #Character Details
        
        items['main'][10]['occupation'].append('学生')

        if persistent.characters_catherine:
            items['main'][10]['name'].append('凯瑟琳')
        if persistent.characters_catherine_foundingfamily:
            items['main'][10]['name'].append('贝内特（创始家族）')
        if persistent.characters_catherine_family1:
            items['main'][10]['family'].append('父亲（雷金纳德）、母亲（玛丽）')
        if persistent.characters_ella:
            items['main'][10]['family'].append('妹妹（艾拉与艾薇）')
        
        #Notes
        items['main'][10]['note'].append('一个傲慢的富家女。米卡和布莱恩的朋友。')
        if persistent.characters_catherine_note1:
            items['main'][10]['note'].append('你发现凯瑟琳的父母逼她去送外卖。你答应替她保密，条件是她别那么讨人厌。')
        if persistent.characters_catherine_note2:
            items['main'][10]['note'].append('汉密尔顿家的派对之后，凯瑟琳开始黏着你，并表明她打算嫁给你。你拒绝了。')
        if persistent.characters_catherine_note3:
            items['main'][10]['note'].append('她想摆你一道却失败了，欠了你一大笔钱。不幸的是，你发现她家其实已经破产了。她同意到咖啡馆洗盘子还债，同时也充当你的专属公主。')
        if persistent.characters_catherine_note4:
            items['main'][10]['note'].append('凯瑟琳为了避雨把你请进了她的公寓。你发现她父亲酗酒，因此她不得不独自照顾两个妹妹。')
        if persistent.characters_catherine_note5:
            items['main'][10]['note'].append('考虑到这一切，你修改了凯瑟琳的合同，决定给她发正常薪水，相信她会主动还清欠款。')


    ##################################################################################################################################
    #Elizabeth
    
        #Character Details
        items['main'][11]['family'].append('母亲（拉塞尔太太）、哥哥（布莱恩）')

        if persistent.characters_elizabeth:
            items['main'][11]['name'].append('伊丽莎白')
            items['main'][11]['name'].append('拉塞尔')
        if persistent.characters_russell:
            items['main'][11]['family'].append('父亲（拉塞尔先生）')
        
        #Notes
        items['main'][11]['note'].append('布莱恩的妹妹。她冲进你的厨房，要求你拒绝她母亲的提议。')
        if persistent.characters_elizabeth_note1:
            items['main'][11]['note'].append('伊丽莎白想和你联手毁掉她的母亲。她离开去想办法了，所以你知道她早晚会回来。')
        if persistent.characters_elizabeth_note2:
            items['main'][11]['note'].append('伊丽莎白告诉你，你的爷爷和她的爷爷曾一起做过些见不得光的勾当，而她母亲正是借此毁掉了他们两人。你怀疑这大概不是全部真相。')


    ##################################################################################################################################
    #Annabelle
    
        #Character Details
        items['main'][12]['note'].append('在汉密尔顿家的派对上试图自我介绍、手足无措的女孩。')
        
        if persistent.characters_annabelle:
            items['main'][12]['name'].append('安娜贝尔') 
        
        #Notes   
        if persistent.characters_annabelle_note1:
            items['main'][12]['note'].append('安娜贝尔拿下了哥特角色扮演大赛的冠军，并以奖品为由要求做你的朋友。你不太确定这到底算什么意思，不过她是个可爱的女孩，试着了解一下也无妨。')


#############################################################################################################################################################################################################
#############################################################################################################################################################################################################
    #Side Characters

    #Mika
        items['side'][1]['note'].append('你在电车上遇见的一个恶毒贱货，当时她正在欺负露西。和布莱恩走得很近。')
        items['side'][1]['occupation'].append('学生') 
        if persistent.characters_mika:
            items['side'][1]['name'].append('米卡')  


    #Brian
        items['side'][2]['note'].append('你在电车上遇见的一只油滑黄鼠狼，当时米卡正在欺负露西。')
        items['side'][2]['occupation'].append('学生') 
        if persistent.characters_brian:
            items['side'][2]['name'].append('布莱恩')
        if persistent.characters_brian_foundingfamily:
            items['side'][2]['name'].append('拉塞尔（创始家族）')
        #family
        if persistent.characters_elizabeth:
            items['side'][2]['family'].append('妹妹（伊丽莎白）')
        if persistent.characters_gloria:
            items['side'][2]['family'].append('母亲（格洛丽亚·拉塞尔）')
        if persistent.characters_russell:
            items['side'][2]['family'].append('父亲（拉塞尔先生）')
        #notes
        if persistent.characters_brian_note1:
            items['side'][2]['note'].append('布莱恩警告你离维多利亚远一点，因为她是「他的」。可维多利亚对他毫无兴趣。')
        if persistent.characters_brian_note2:
            items['side'][2]['note'].append('布莱恩当着半个学校的面宣布了他与汉娜的婚约。现在所有人都以为你们三个卷进了某种三角关系。')   


    #Lenny
        items['side'][3]['note'].append('你在电车上遇见的一个大块头蠢货。布莱恩的跟班。可能正迷恋着米卡。')
        items['side'][3]['occupation'].append('学生') 
        if persistent.characters_lenny:
            items['side'][3]['name'].append('兰尼')    


    #Baker
        items['side'][4]['note'].append('为你的咖啡馆供货的友善面包师。他周末会带着一大家子来吃饭，而且认识你爷爷。')
        items['side'][4]['occupation'].append('面包师') 
        if persistent.characters_baker:
            items['side'][4]['name'].append('面包师')
        if persistent.characters_baker_note1:
            items['side'][4]['note'].append('面包师跟你讲了一些创始家族的事。据说你爷爷是其中之一，那你就是他的继承人？')    


    #Mr Takamura
        items['side'][5]['note'].append('镇上另一家餐厅的老板。为人极其古怪，视你为竞争对手。')
        items['side'][5]['occupation'].append('「Wong’s Chinese Dragon」餐厅的老板兼主厨') 
        if persistent.characters_wong:
            items['side'][5]['name'].append('高村先生')
        #family
        if persistent.characters_akatsuki:
            items['side'][5]['family'].append('女儿（晓月）')
        if persistent.characters_akari:
            items['side'][5]['family'].append('女儿（明里）')
        if persistent.characters_akatsuki_family4:
            items['side'][5]['family'].append('妻子（茜）') 
        if persistent.characters_akatsuki_family2:
            items['side'][5]['family'].append('侄女（高村美咲）') 
        #notes
        if persistent.characters_akari:
            items['side'][5]['note'].append('你在厨艺对决中输给明里之后，他单方面宣布晓月要嫁给你。')    


    #Lucy's Mother
        items['side'][6]['note'].append('露西那位压迫人、动辄虐待她的母亲。')
        if persistent.characters_lucymother:
            items['side'][6]['name'].append('露西的母亲')
        if persistent.characters_lucymother_note1:
            items['side'][6]['note'].append('露西离开之后，她跑去学校，试图在校长那里给你找麻烦。')  


    #Chloe
        items['side'][7]['note'].append('米卡和凯瑟琳的朋友。')
        items['side'][7]['occupation'].append('学生')
        if persistent.characters_chloe:
            items['side'][7]['name'].append('克洛伊')    


    #Danny
        items['side'][8]['note'].append('维多利亚的哥哥。听起来像是在做些见不得光的勾当，不过他似乎是个好人，维多利亚也信任他。')
        items['side'][8]['note'].append('初次见面时丹尼试探过你；你通过之后，他问你维多利亚能不能留下来和你一起住。他还让你答应保护她。')
        if persistent.characters_danny:
            items['side'][8]['name'].append('丹尼')
        if persistent.characters_victoria_name:
            items['side'][8]['name'].append('特纳')
        #family
        if persistent.characters_victoria_family1:
            items['side'][8]['family'].append('母亲（已故）')
        if persistent.characters_victoria_family2:
            items['side'][8]['family'].append('父亲（关系不睦）')
        if persistent.characters_victoria_family3:
            items['side'][8]['family'].append('妹妹（维多利亚）')


    #Lily
        items['side'][9]['note'].append('莎拉的母亲。代表丈夫——汉密尔顿家族的当家——邀请你参加派对。')
        if persistent.characters_lily:
            items['side'][9]['name'].append('莉莉')
            items['side'][9]['name'].append('汉密尔顿')
        #family
        items['side'][9]['family'].append('丈夫（汉密尔顿先生）、女儿（莎拉）')
        #notes
        if persistent.characters_lily_note1:
            items['side'][9]['note'].append('莉莉坚称对丈夫指使跟踪莎拉一事毫不知情。你则要她去查清那张跟踪照片的来源——如果她真想向女儿证明自己的话。')
        if persistent.characters_lily_note2:
            items['side'][9]['note'].append('莉莉意识到莎拉站在你这边，而不是他们那边。她为失去与女儿的亲情而崩溃痛哭。也许她终于会努力把莎拉的信任赢回来？')  
 
 
    #Mr Hamilton
        items['side'][10]['note'].append('莎拉的父亲，汉密尔顿家族的当家。')
        items['side'][10]['note'].append('他在派对宾客面前揭露了你身为第五大家族当家的身份，还暗示你与莎拉已经订婚。')
        items['side'][10]['occupation'].append('家族当家')
        if persistent.characters_hamilton:
            items['side'][10]['name'].append('汉密尔顿先生') 
        #family   
        items['side'][10]['family'].append('妻子（莉莉、卡珊德拉）、女儿（莎拉）、子女（众多）、姐姐（玛丽·贝内特）、姐夫（雷金纳德·贝内特）')

  
    #Cassandra
        items['side'][11]['note'].append('汉密尔顿先生的其中一位妻子。莎拉那群刻薄的姐妹中，至少有一位是她生的。')
        if persistent.characters_cassandra:
            items['side'][11]['name'].append('卡珊德拉')
            items['side'][11]['name'].append('汉密尔顿')
  
  
    # #Annabelle
    #     items['side'][12]['note'].append('A clumsy girl who tried to introduce herself at the Hamilton party.')
    #     if persistent.characters_annabelle:
    #         items['side'][12]['name'].append('Annabelle')    


    #Mary Bennett
        items['side'][13]['note'].append('凯瑟琳的母亲。傲慢又刻薄，显然打心眼里瞧不起创始家族以外的人。')
        if persistent.characters_mary:
            items['side'][13]['name'].append('玛丽')
            items['side'][13]['name'].append('贝内特')
        #family   
        items['side'][13]['family'].append('丈夫（雷金纳德）、女儿（凯瑟琳）、哥哥（汉密尔顿先生）')


    #Reginald Bennett
        items['side'][14]['note'].append('凯瑟琳的父亲，贝内特家族的当家。')
        items['side'][14]['note'].append('一个和蔼开朗的男人。显然完全听老婆的。')
        items['side'][14]['occupation'].append('家族当家')
        if persistent.characters_regi:
            items['side'][14]['name'].append('雷金纳德')
            items['side'][14]['name'].append('贝内特')
        #family   
        items['side'][14]['family'].append('妻子（玛丽）、女儿（凯瑟琳）、姐夫（汉密尔顿先生）')
        if persistent.characters_ella:
            items['side'][14]['family'].append('女儿（艾拉与艾薇）')
        #Notes
        if persistent.characters_regi_note1:
            items['side'][14]['note'].append('你发现雷吉自从破产后染上了严重的酒瘾。他喝起酒来倒不像会撒酒疯的人，但丢下凯瑟琳一个人照顾其他女儿。')


    #Sarah Sis 1
        items['side'][15]['note'].append('莎拉那些刻薄的同父异母姐妹之一。')
        if persistent.characters_sis1:
            items['side'][15]['name'].append('金发妹妹')
        #family   
        items['side'][15]['family'].append('父亲（汉密尔顿先生）、姐姐（莎拉）、兄弟姐妹（众多）')   


    #Mira
        items['side'][16]['note'].append('莎拉那些刻薄的同父异母姐妹之一。')

        # if persistent.characters_sis2:
        #     items['side'][16]['name'].append('Brunette Sister')
        # if persistent.characters_sis2_name:
        #     items['side'][16]['name'].append('Mira')

        if persistent.characters_sis2:
            if 'Brunette Sister' not in items['side'][16]['name'] and 'Mira' not in items['side'][16]['name']:
                items['side'][16]['name'].insert(0, 'Brunette Sister')
        if persistent.characters_sis2_name:
            if 'Brunette Sister' in items['side'][16]['name']:
                items['side'][16]['name'].remove('Brunette Sister')
            items['side'][16]['name'].insert(0, 'Mira')
            items['side'][16]['name'].append('汉密尔顿')
        #family   
        items['side'][16]['family'].append('父亲（汉密尔顿先生）、姐姐（莎拉）、兄弟姐妹（众多）')  
        #Notes
        if persistent.characters_sis2_note1:
            items['side'][16]['note'].append('你在莎拉卧室的一张照片背景里发现了那个跟踪狂。看来他们以前是同学。')
        if persistent.characters_sis2_note2:
            items['side'][16]['note'].append('米拉在她们父亲的布局里，负责把跟踪狂引向莎拉。你觉得莎拉永远不会原谅她。')


    #Samantha
        items['side'][17]['note'].append('明里的朋友。你的超级无敌大粉丝。总是在咖啡馆里吃饭。')
        items['side'][17]['occupation'].append('学生') 
        if persistent.characters_samantha:
            items['side'][17]['name'].append('萨曼莎')    


    #Harriet
        items['side'][18]['note'].append('一个礼貌而公事公办的女人。她第一次出现在你的咖啡馆，是代表父亲吉尔伯特先生来的。')
        items['side'][18]['occupation'].append('私人助理')
        if persistent.characters_harriet:
            items['side'][18]['name'].append('哈丽雅特')
        #Family
        items['side'][18]['family'].append('妹妹（汉娜）、姐姐（埃莉森）、父亲（吉尔伯特）')
        #Notes
        if persistent.characters_harriet_note1:
            items['side'][18]['note'].append('你与哈丽雅特见面并同意保持联系。她警告你，她父亲到年底时一定会要看到你做出些进展。')


    #Mr Gilbert
        items['side'][19]['note'].append('汉娜和埃莉森的父亲，吉尔伯特家族的当家。')
        items['side'][19]['note'].append('一个人还不坏，但完全不肯变通。为了不让其他任何一家当上绝对的主导者，他会不择手段。')
        items['side'][19]['note'].append('在你爷爷被放逐之前，他曾是你爷爷的好友。')
        items['side'][19]['occupation'].append('家族当家')
        if persistent.characters_gilbert:
            items['side'][19]['name'].append('吉尔伯特先生') 
        #Family
        items['side'][19]['family'].append('女儿（埃莉森）、女儿（汉娜）、女儿（哈丽雅特）')
        #Notes
        if persistent.characters_gilbert_note1:
            items['side'][19]['note'].append('吉尔伯特通过哈丽雅特给了你大量援助和一笔巨额贷款，用来重建被毁的咖啡馆。你欠他一个天大的人情。')


    #Gloria Russell
        items['side'][20]['note'].append('伊丽莎白和布莱恩的母亲，拉塞尔家族的当家。')
        items['side'][20]['note'].append('她十几岁时就毁掉了自己的哥哥，最终把拉塞尔家族的大权抢到了自己手里。')
        items['side'][20]['note'].append('吉尔伯特形容她是个以毁掉他人为乐的施虐者，而现在她把目标对准了你。')
        items['side'][20]['occupation'].append('家族当家') 
        if persistent.characters_gloria:
            items['side'][20]['name'].append('拉塞尔太太')
        #Family
        items['side'][20]['family'].append('丈夫（拉塞尔先生）、女儿（伊丽莎白）、儿子（布莱恩）')
        #Notes
        if persistent.characters_headfun_sister:
                items['side'][20]['note'].append('教务干事的姐姐证实了毁掉你爷爷的人就是格洛丽亚，还说她利用了他与拉塞尔家族前任当家之间保守的某个黑暗秘密。')

    #Mr Russell
        items['side'][21]['note'].append('格洛丽亚·拉塞尔的丈夫，布莱恩与伊丽莎白的父亲。')
        items['side'][21]['note'].append('一个粗鲁、暴躁的男人。')
        if persistent.characters_russell:
            items['side'][21]['name'].append('拉塞尔先生')
        #Family
        items['side'][21]['family'].append('妻子（格洛丽亚·拉塞尔）、女儿（伊丽莎白）、儿子（布莱恩）')
        #Notes

    #Akane
        items['side'][22]['note'].append('高村先生的妻子，晓月与明里的母亲。')
        items['side'][22]['note'].append('看看她丈夫的样子，她算得上是个正派、而且出人意料地清醒的女人。她请你帮忙说服晓月修复与父亲的关系。')
        items['side'][22]['occupation'].append('家庭主妇，在「Wong’s Chinese Dragon」餐厅帮忙') 
        if persistent.characters_akane:
            items['side'][22]['name'].append('茜')
            items['side'][22]['name'].append('高村')
        # if persistent.characters_akane:
        #     items['side'][22]['name'].append('Takamura')
        #Family
        items['side'][22]['family'].append('丈夫（高村先生）、女儿（晓月）、女儿（明里）、侄女（高村美咲）')
        #Notes

    #Ella
        items['side'][23]['note'].append('凯瑟琳的妹妹之一。')
        items['side'][23]['note'].append('一个自信又爱玩闹的女孩。和凯瑟琳、艾薇以及父亲一起住在她们那间小公寓里。')
        items['side'][23]['occupation'].append('中学生') 
        if persistent.characters_ella:
            items['side'][23]['name'].append('艾拉')
            items['side'][23]['name'].append('贝内特')
        # if persistent.characters_catherine_foundingfamily:
        #     items['side'][23]['name'].append('Bennett (Founding Family)')
        #Family
        items['side'][23]['family'].append('父亲（雷吉）、姐姐（凯瑟琳）、妹妹（艾薇）')
        #Notes

    #Ivy
        items['side'][24]['note'].append('凯瑟琳的妹妹之一。')
        items['side'][24]['note'].append('一个安静而敏锐的女孩。和凯瑟琳、艾拉以及父亲一起住在她们那间小公寓里。')
        items['side'][24]['occupation'].append('中学生') 
        if persistent.characters_ivy:
            items['side'][24]['name'].append('艾薇')
            items['side'][24]['name'].append('贝内特')
        # if persistent.characters_catherine_foundingfamily:
        #     items['side'][24]['name'].append('Bennett (Founding Family)')
        #Family
        items['side'][24]['family'].append('父亲（雷吉）、姐姐（凯瑟琳）、妹妹（艾拉）')
        #Notes


    #HeadFun
        items['side'][25]['note'].append('干事会的最高领袖——那群让议会得以正常运转、不偏不倚的行政人员与官僚。')
        if persistent.characters_headfun:
            items['side'][25]['name'].append('教务干事')
        #Family
        items['side'][25]['family'].append('姐姐（？？？）')
        #Notes
        items['side'][25]['note'].append('初次见面时，他告诉你他姐姐曾与你爷爷有过一段婚姻。你请他安排一次会面，好多了解一些你爷爷失势的经过。')
        if persistent.characters_headfun_sister:
            items['side'][25]['note'].append('在你主持了第一次议会会议之后，教务干事把你介绍给他的姐姐玛格丽特。她把爷爷的事全盘告诉了你，包括他是怎么栽在格洛丽亚手里的——她用某个黑暗秘密来勒索他。')


    #Eleanor
        items['side'][26]['note'].append('汉密尔顿的第一任妻子与左膀右臂，汉密尔顿家族的女主人。')
        if persistent.characters_eleanor:
            items['side'][26]['name'].append('埃莉诺')
            items['side'][26]['name'].append('汉密尔顿')
        #Family
        items['side'][26]['family'].append('丈夫（汉密尔顿）')
        #Notes
        items['side'][26]['note'].append('她一面维持着可靠盟友的假象，一面把你逼到只能接受再次拜见汉密尔顿先生的邀请。')


#############################################################################################################################################################################################################
#############################################################################################################################################################################################################

screen bios():

    key ["K_ESCAPE", "mouseup_3"] action Return()

    tag menu
    add "gui/msp1/main_menu/bg.png":
        at transform:
            xycenter (.5, .5)
            zoom      .5
    add im.Blur("gui/msp1/bg.webp", 1) at bg_in()

    # Workspace
    
    frame:

        xysize   (1770, 930)
        xycenter (.5  , .5 )
    
        hbox:
            spacing 8
            align (.5, .5)

            # Characters

            frame:
                align  (.5  , .5 )
                xysize (1495, 930)

                vpgrid id "bios":
                    offset    (-6  , -6 )
                    xysize    (1495, 930)
                    draggable True
                    mousewheel True
                    cols 5
                    spacing 8

                    at transform:

                        offset (0, -1080)

                        easein_quart (1.25 * persistent.ui_speed_multiplier) offset (0, 0)

                    $ current_items = items[current_state]
                    $ item_list = list(current_items.items())

                    for index, (item_key, item_data) in enumerate(item_list):
                        $ name_text    = item_data['name'][0] if item_data['name'] else "???"
                        $ action_value = [ ShowMenu('profile', what=item_data, index=index, item_list=item_list), Function(refresh_character_stats) ] if item_data['name'] else [ Function(refresh_character_stats) ]
                        $ real_name    = real_names.get(item_data['name'][0].lower(), item_data['name'][0]).lower() if item_data['name'] else "Unknown"
                        $ thumbnail_path = "gui/msp1/bios/" + real_name + "/" + real_name + "_half.webp"

                        frame:
                            xysize (289, 461)
                            button:
                                xysize (289, 461)
                                align (.5, .5)

                                focus_mask True

                                action action_value

                                image "gui/msp1/bios_ui/item_3.png" align (.5, .5):
                                    at transform:
                                        on idle:
                                            easein_quint(0.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix(str(item_data['color']), "#00000080")
                                        on hover:
                                            easein_quint(0.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#ffb1df80", "#000000")
                                if real_name != "Unknown":
                                    image thumbnail_path:
                                        at transform:
                                            zoom     0.17
                                            xycenter (0.5, 0.5)
                                            offset   (0, -25)

                                text name_text align (0.0, 1.0) text_align 0.0 font "fonts/MiSans-Regular.ttf" color "#f1f1f1" offset (25, -15)
                                
                                alt name_text
                                at shrink()
                            # at item_in(wait=index * 0.075)

                vbar value YScrollValue ("bios") xalign 1.0 xysize (9, 930) offset (6, -6)

            # Navigation bar

            frame:
                align (.5, .5)
                xysize (267, 930)
                vbox:
                    align  (.5, .0)
                    offset ( 0, -6)
                    spacing 8

                    use scr_bios_draw(SetVariable("current_state", "main"), "gui/msp1/bios_ui/mainc.png", "Main", 0)
                    use scr_bios_draw(SetVariable("current_state", "side"), "gui/msp1/bios_ui/sidec.png", "Side", 1)

                frame:
                    xysize (267, 115)
                    offset (-12, 0  )
                    align  (.0 , 1.0)

                    use scr_bios_draw(Return()                            , "gui/msp1/global/return.png", "Return", 2)

init python:
    def get_xoffset(name):
        class_1 = {'a','v','w','x','y','z'}
        class_2 = {'t'}
        if name[0].lower() in class_1:
            return -7
        elif name[0].lower() in class_2:
            return -9
        else:
            return -12

screen profile(what=None, index=0, item_list=[]):

    key ["K_ESCAPE", "mouseup_3"] action ShowMenu('bios')

    tag menu

    add "gui/msp1/bg.webp":
        at transform:
            blur 5

    $ name_key = what['name'][0].lower() if what.get('name') else "unknown"
    $ real_name = real_names.get(name_key, name_key).lower()

    $ bg_image = "gui/msp1/bios/" + real_name + "/" + real_name + "_bg.webp"
    $ half_image = "gui/msp1/bios/" + real_name + "/" + real_name + "_half.webp"
    
    # if not os.path.exists(os.path.join(renpy.config.gamedir, bg_image)):
    #     add None
    # else:
    #     add bg_image at bios_bg_in()
    # add "gui/msp1/bios_ui/foreground.png" at fade_in()
    # if not os.path.exists(os.path.join(renpy.config.gamedir, bg_image)):
    #     add None
    # else:
    #     add half_image at bios_char_slide_in()

    add bg_image at bios_bg_in()
    add "gui/msp1/bios_ui/foreground.png" at fade_in()
    add half_image at bios_char_slide_in()

    add "gui/msp1/bios_ui/text_bg.png" at fade_in()

    frame background "gui/msp1/global/bar.png":
        xysize (1820, 4  )
        ypos    989
        xalign .5
        at bar_in()

    frame:
        pos    (50  , 50 )
        xysize (1820, 970)

        frame:
            align  (1.0, .0 )
            xysize (267, 238)
            offset (6  , -6 )

            vbox:
                spacing 8
                if main_menu:
                    use scr_bios_draw(Return()    , 'gui/msp1/bios_ui/main_menuc.png', 0)
                use scr_bios_draw(ShowMenu('bios'), 'gui/msp1/global/return.png'     , 1)
                hbox:
                    spacing 9
                    button:

                        align (.5, .5)
                        
                        focus_mask True

                        if index > 0:
                            action ShowMenu("profile", what=item_list[index-1][1], index=index-1, item_list=item_list)
                        else:
                            action NullAction()

                        alt 'previous'
                        
                        xysize (130, 87)

                        image 'gui/msp1/bios_ui/bios_np.png' align (.5, .5)

                        text '上一页' size 24 align (.5, .5) offset (0, -2) font "fonts/MiSans-Regular.ttf"

                        if index > 0:
                            at transform:

                                on idle:

                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#000", "#ffffff") alpha 1.0

                                on hover:
                    
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#ffb1df", "#ffffff") alpha 1.0
                        else:
                            at transform:

                                easein_quint (.5 * persistent.ui_speed_multiplier) alpha .0
                    button:

                        align (.5, .5)
                        
                        focus_mask True

                        if index < len(item_list)-1 and item_list[index+1][1].get('name'):
                            action ShowMenu("profile", what=item_list[index+1][1], index=index+1, item_list=item_list)
                        else:
                            action NullAction()

                        alt 'next'
                        
                        xysize (130, 87)

                        image 'gui/msp1/bios_ui/bios_np.png' align (.5, .5)

                        text '下一页' size 24 align (.5, .5) offset (0, -2) font "fonts/MiSans-Regular.ttf"

                        if index < len(item_list)-1:
                            at transform:

                                on idle:

                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#000", "#ffffff") alpha 1.0

                                on hover:
                    
                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix("#ffb1df", "#ffffff") alpha 1.0
                        else:
                            at transform:

                                easein_quint (.5 * persistent.ui_speed_multiplier) alpha .0

        frame:
            xysize (None, 179)
            align  (.0  , 1.0)
            offset (-5  , -31)
            at bios_text_in()
            $ name_text = what.get('name', '???')[0].upper() if what.get('name') else "???"
            text name_text align (.0, .5) size 256 font "fonts/MiSans-Regular.ttf" offset (get_xoffset(what['name'][0]), 12)

        frame background "gui/msp1/bios_ui/profile_text_bg.png":
            xysize (647, 590)
            align  (1.0, 1.0)
            offset (5, -31)
            frame:
                xysize     (647, 590)
                offset     (-6 , -6 )
                padding(16, 16, 0, 16)
                viewport id "profile":
                    offset     (-6 , -6 )
                    draggable  True
                    mousewheel True
                    vbox:
                        offset  (6, 6)
                        spacing 24
                        $      name_list       = what.get('name', [])
                        $      name_text       = " ".join(name_list) if name_list else "???"
                        #$      name_text       = " ".join([name.capitalize() for name in name_list]) if name_list else "???"
                        $      age_text        = str(what.get('age', 'N/A')).upper()
                        $      occupation_list = what.get('occupation', [])
                        $      occupation_text = ", ".join(occupation_list) if occupation_list else "N/A"
                        $      family_list     = what.get('family', [])
                        $      family_text     = ", ".join(family_list) if family_list else "N/A"                      
                        $      note_list       = what.get('note', [])
                        $      note_text       = "\n{p}".join(note_list) if note_list else "N/A"


                        null
                        text   str(current_state).upper()      size 45 font "fonts/MiSans-Regular.ttf" at cascade_info(.0)
                        text   "———————————————————————"       size 27 font "fonts/MiSans-Regular.ttf" at cascade_info(.1)
                        text   "姓名：[name_text]"             size 27 font "fonts/MiSans-Regular.ttf" at cascade_info(.2)
                        text   "年龄：[age_text]"               size 27 font "fonts/MiSans-Regular.ttf" at cascade_info(.3)
                        text   "职业：[occupation_text]" size 27 font "fonts/MiSans-Regular.ttf" at cascade_info(.4)
                        text   "家族：[family_text]"         size 27 font "fonts/MiSans-Regular.ttf" at cascade_info(.5)
                        text   "———————————————————————"       size 27 font "fonts/MiSans-Regular.ttf" at cascade_info(.6)
                        text   "备注："                        size 27 font "fonts/MiSans-Regular.ttf" at cascade_info(.7)
                        text   "[note_text]"                   size 27 font "fonts/MiSans-Regular.ttf" at cascade_info(.8)
                        text   "———————————————————————"       size 27 font "fonts/MiSans-Regular.ttf" at cascade_info(.9)

                        null

            vbar value YScrollValue ("profile") xalign 1.0 xysize (8, 590) offset (6, -6)