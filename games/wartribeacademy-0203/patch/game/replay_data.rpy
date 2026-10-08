init -100:
    # These are initialized first because they are used by the screen structure
    define replay_max_width = 4
    define replay_max_height = 3
    define replay_max_per_page = replay_max_width * replay_max_height
    define replay_max_per_page_f = float(replay_max_per_page)
    define replay_title_size = 60
    define replay_x_align = 0.25
    define replay_y_align = 0.5
    define replay_item_spacing = 40
    define replay_control_hover_color = '#f00'
    define replay_scene_thumbnail_width = 362
    define replay_scene_thumbnail_height = 201
    define config.replay_scope |= {"player_name": persistent.pname, "tribe_name": persistent.tname, "cat_n": persistent.cname, "potion_name": persistent.potname }

#362 x 618

init python:
    # These are labels that are treated as the same: view one, view them all
    assign_labels_eq('cleo6juna_slut', 'cleo6juna_damsel', 'cleo6juna_fighter')
    assign_labels_eq('cleo16_a', 'cleo16_b')
    assign_labels_eq('morning1', 'morning1_n')
    assign_labels_eq('leona23_1', 'leona24_1')

    # These are one way relations, play the one on the right unlock the latter, but not vice versa
    assign_label_unlock('rhea5_1a', 'rhea5_1b')

    # These are initialized last because it's the screen data not structure
    replay_root_obj = ReplayMetaData('root_obj', '回放', '', '', '', 'mc_replay_bg')
    def replay_make_titles(*names):
        ret = []
        for name in names:
            key = name.lower() if type(name) == str else name[1]
            name = name if type(name) == str else name[0]
            icon = key + '_gallery'
            ret.append(ReplayMetaData(key, name, icon, At(icon, greyscale_image), At(key + '_locked', replay_control_hover), key + '_replay_bg'))
        return ret

    def replay_make_scenes(*data):
        ret = []
        for d in data:
            key = d[1]
            name = d[0]
            thumb = d[2] if len(d) > 2 else 'scene_placeholder'
            idle_image_key = key + '_replay_idle'
            hover_image_key = key + '_replay_hover'
            lock_image_key = key + '_replay_insensitive'
            renpy.image(idle_image_key, At(thumb, scene_thumbnail, greyscale_image))
            renpy.image(hover_image_key, At(thumb, scene_thumbnail, do_nothing)) # add do_nothing or nothing replaces greyscale
            renpy.image(lock_image_key, At(thumb, scene_thumbnail, scene_locked))
            ret.append(ReplayMetaData(key, name, hover_image_key, idle_image_key, lock_image_key))
        return ret
        
    replay_categories = replay_make_titles(('候选人', 'candidates'), ('仆人们', 'servants'), ('妓院', 'brothel'), ('其他', 'other'))
    
    replay_characters = {}
    replay_characters['candidates'] = replay_make_titles(('克莉奥', 'cleo'), ('露丝', 'luce'), ('蕾娅', 'rhea'), ('玛格娜', 'magna'), ('普里西拉', 'priscilla'), ('伊莎', 'isha'), ('玛丽昂', 'marion'), ('莱奥娜', 'leona'), ('菲塔娜', 'featana'))
    replay_characters['servants'] = replay_make_titles(('乔茜', 'josie'), ('菲尔', 'fir'), ('埃兹拉', 'ezra'), ('茱娜', 'juna'), ('蒂娜', 'tima'))
    replay_characters['brothel'] = replay_make_titles(('芭斯特', 'bastet'), ('英格内塔', 'ingnetta'), ('尤尔', 'yuel'), ('萨什与莫妮卡', 'sash'))
    replay_characters['other'] = replay_make_titles(('斯嘉丽', 'scarlet'), ('博纳德姐妹', 'bona'), ('娜塔莉与塔莉娅', 'nattal'), ('祖基', 'zuki'))
    
    replay_scenes = {}
    replay_scenes['cleo'] = replay_make_scenes(
        ("快速沐浴", 'cleoscene1', 'cleo1_24'),
        ("克莉奥的计划", 'cleoscene2', 'cscene3_43'),
        ("监视玛格娜", 'cleopmag1', 'cpm2'),
        ("监视露丝", 'cleopluce1', 'cpl7'),
        ("监视普里西拉", 'cleoppris1', 'cpp5'),
        ("监视蕾娅", 'cleoprhea1', 'cpr3'),
        ("监视克莉奥", 'cleoscene4', 'cleo4_13'),
        ("不开心的克莉奥", 'cleoscene5', 'cleo5_7'),
        ("初访城市", 'cleoscene7', 'cleo7_95'),
        ("见到母亲", 'cleoscene8', 'cleo8_46'),
        ("偷俯克莉奥", 'cleoscene9', 'luce_BJ6'),
        ("惩罚偷俯者", 'cleoscene10', 'cleo10_9'),
        ("某个雨天", 'cleoscene11', 'cleo11_16'),
        ("妖精祭典", 'cleoscene12_1', 'cleo13_4'),
        ("启航", 'cleoscene15_1', 'cleo15_16'),
        ("亲切的克莉奥", 'cleo16_a', 'cleo16_6'),
        ("不开心的克莉奥", 'cleo16_b', 'cleo16_24'),
        ("偷俯克莉奥 II", 'cleo17_a', 'cleo17_55'),
        ("年龄测试", 'cleo17_b', 'cleo17_31'),
        ("和解", 'cleo18_b', 'cleo18_17'),
        ("豪赌", 'cleo19_1', 'cleo19_2'),
        ("克莉奥之夜", 'cleo20_1', 'cleo20_9'),
        ("见遇伊格尼斯", 'cleo21_1', 'cleo21_26'),
        ("伊格尼斯的仆人", 'cleo22_1', 'cleo22_33'),
        ("克莉奥", 'cleo23_1', 'cleo23_1', 'cleo23_13'),
        ("与克莉奥共度一夜", 'cleo24_1', 'cleo24_12'),
        ("微光指环", 'glimmering1_1', 'cleoring1_11'),
        ("克莉奥与普里西拉", 'pris_swap2_1', 'prisxcleo1_36'),
        ("擦肩而过", 'thepast1_1', 'thepast1_10'),
        ("美人鱼", 'themermaid1_1', 'themermaid1_4'),
    )

    replay_scenes['luce'] = replay_make_scenes(
        ("人物介绍", 'lucescene1', 'l1scene20'),
        ("露内特", 'lucescene2', 'l2scene4'),
        ("暧昧小知识", 'lucescene3', 'luce3_1'),
        ("混混", 'lucescene4', 'lucebandit2'),
        ("对峙露内特", 'lucescene5', 'lunevisit1'),
        ("神秘来客", 'lucescene6', 'luce6_2'),
        ("见遇乔安娜", 'lucescene7go', 'partyintro2'),
        ("舞女", 'lucePartydancer', 'dancer22'),
        ("派对之后", 'lucePartyroom', 'partyintro9'),
        ("与露丝共度一夜", 'luceroomx_wall_1', 'luceroom_wall_2'),
        ("与露丝共度一夜 II", 'luceroomx_mis_1', 'luceroom_mis_3'),
        ("入侵者", 'violetscene1_1', 'violet1_3'),
        ("入侵者疑云", 'violetscene2_1', 'violet2_2'),
        ("审讯 I", 'violetscene4_1', 'violet4_4'),
        ("新兵", 'lune_room0', 'lune0_29'),
        ("露内特归来", 'lun_intro_1', 'lune1_1'),
        ("抓老鼠", 'violetscene5_0', 'violet6_2'),
        ("审讯 II", 'violetscene6_1', 'joana1_1'),
        ("审讯 III", 'joana1_1', 'joana2_1'),
        ("审讯 IV", 'joana2_1', 'joana2_28'),
        ("事后汇报", 'joana3_1', 'violet5_2'),
        ("露丝重逢", 'joana4_1', 'joana3_19'),
        ("新制服", 'servants13_1', 'luce_uni_7'),
        ("谜题（答对）", 'isha14_luce', 'isha14_52'),
        ("谜题（答错）", 'isha14_mag', 'isha14_64'),
        ("微光指环", 'glimmering1_1', 'cleoring1_63'),
        ("共浴", 'rheaxmag_1', 'bath_ljmr_2'),
        ("擦肩而过", 'thepast1_1', 'thepast1_10'),
        ("情同姐妹", 'joana4plus_1', 'joana4_1'),
        ("她的心事", 'joana5_1', 'joana5_1'),        
        ("一滴自由", 'joana6_1', 'joana6_2'),
        ("阴谋", 'joana7_1', 'joana7_1'),
        ("诱饵", 'joana8_1', 'joana8_1'),
        ("受祝福者", 'theblessed1_1', 'theblessed1_1'),
    )

    replay_scenes['rhea'] = replay_make_scenes(
        ("人物介绍", 'rheascene1', 'rhea1_3'),
        ("人物介绍 II", 'rheascene2', 'black'),
        ("客栈探访", 'rheascene3', 'black'),
        ("酒馆探访", 'rhea4_1', 'rhea4r_6'),
        ("心烦的蕾娅", 'rhea5_1a', 'rhea5r_14'),
        ("她的新工作", 'rhea6_1a', 'rhea6a_1'),
        ("乔伊的心思", 'rhea7_1a', 'rhea7a_4'),
        ("她的选择", 'rhea8_1a', 'rhea8a_1'),
        ("新来的仆人", 'rhea9_1', 'rhea7_18'),
        ("蕾娅的计策", 'rhea10_1a', 'rhea10a_18'),
        ("蕾娅的让步", 'rhea11_1a', 'rhea11a_2'),
        ("夫人的朋友", 'rhea5_1b', 'rhea5r_18'),
        ("酒馆探访 II", 'rhea6_1b', 'rhea6a_7'),
        ("与蕾娅约会", 'rhea7_1b', 'rhea7b_4'),
        ("逗弄乔伊", 'rhea8_1b', 'rhea9r_2'),
        ("乔伊与蕾娅", 'rhea10_1b', 'rhea10b_5'),
        ("至少还在一起", 'rhea11_1b', 'rhea11b_4'),
        ("蕾娅的交易", 'rhea13_1', 'rheaboobs_6'),
        ("副作用", 'rhea14_1', 'rheaboobs_18'),
        ("蕾娅的感敬", 'rhea15_1', 'rheaboobs_36'),
        ("地牢", 'dungeon_intro', 'rheaBDSM1_1'),
        ("不太顶用", 'rhea15_x_1', 'rhea15_11'),
        ("跟踪她", 'rhea16_1', 'rhea16_20'),
        ("有用的门路", 'rhea17_1', 'rhea17_18'),
        ("共进退", 'rhea18_1', 'rhea18_1'),
        ("招募帮手", 'rhea19_1', 'rhea19_6'),
        ("商议对策", 'rhea20_1', 'rhea20_23'),
        ("熟能生巧", 'rhea21_1', 'rhea21_5'),
        ("健壮的精灵", 'rhea22_1', 'rhea22_15'),
        ("通行令", 'rhea23_1', 'rhea23_17'),
        ("拍卖会", 'rhea24_1', 'rhea24_2_23'),
        ("说出你的秘密", 'rhea25_1', 'rhea25_2'),
        ("暧昧撑找", 'rhea26_1', 'rhea26_8'),
        ("惩罚俘虏", 'mc_pun_chy_1', 'mcpunc_18'),
        ("共浴", 'rheaxmag_1', 'bath_ljmr_2'),
        ("黑衣夫人", 'theviscount1_1', 'theviscount1_8'),
    )

    replay_scenes['magna'] = replay_make_scenes(
        ("人物介绍", 'magscene1', 'ms111'),
        ("与优妮切磋", 'magscene2', '19mxy'),
        ("分享优妮", 'magscene3', '26mxy'),
        ("贵族那些事", 'magscene4', 'mag4_9'),
        ("村庄活动", 'magscene5', 'mag5_3'),
        ("惩罚西奇", 'mag_punishxichi', 'punishxi_49'),
        ("惩罚优妮", 'mag_punishyuni', 'punishyuni2'),
        ("讨伐强盗", 'magscene6', 'mag6v_56'),
        ("玛格娜的感敬", 'magscene7', 'mag7_18'),
        ("继母", 'magscene8', 'mag_8_19'),
        ("竞技场", 'magscene9', 'mag_9_1'),
        ("与斯塔西亚", 'stacia1', 'stacia_1_8'),
        ("开始训练", 'magscene10_1', 'mag10_6'),
        ("体力 I", 'magscene11_1', 'magvit_1'),
        ("体力 II", 'magscene11_vit2', 'magvit_35'),
        ("体力 III", 'magscene12_vit3', 'magvit_57'),
        ("力量 I", 'magscene12_1', 'magstr_6'),
        ("力量 II", 'magscene12_str2', 'magstr_32'),
        ("力量 III", 'magscene12_str3', 'magstr_54'),
        ("速度 I", 'magscene13_1', 'magspd_18'),
        ("速度 II", 'magscene13_spd2', 'magspd_73'),
        ("速度 III", 'magscene13_spd3', 'magsped_3_6'),
        ("预选赛", 'magscene14_1', 'mag_14_19'),
        ("违规", 'magscene15_1', 'mag_15_3'),
        ("老对手", 'magscene16', 'mag16_29'),
        ("关切的盟友", 'magscene17', 'mag_17_shino_16'),
        ("对阵威尔德", 'wilford_prefight', 'bat_wil_7'),
        ("对阵尼科", 'niko_prefight', 'bat_niko_13'),
        ("对阵格拉迪克斯", 'gladix_prefight', 'gladix_bat_5'),
        ("对阵达里乌斯", 'darius_prefight', 'darius_bat_3'),
        ("治疗", 'mag_josie_4', 'jos_mag_sick_20'),
        ("康复", 'magscene18', 'mag18_25'),
        ("斯塔西亚留下？", 'stacia_aftermath', 'mag18_3'),
        ("玛格娜的心意", 'mag_aftermath', 'mag19_14'),
        ("玛格娜的感敬", 'mag_mis_1', 'mag_room_xxx_1'),
        ("抱住玛格娜", 'mag_lift_1', 'mag_room_xxx_30'),
        ("严厉的玛格娜", 'mag_pun_chy_1', 'magpunc_1'),
        ("与玛格娜约会", 'mag_date_1', 'mag1_date_1'),
        ("谜题（答对）", 'isha14_luce', 'isha14_52'),
        ("谜题（答错）", 'isha14_mag', 'isha14_65'),
        ("共浴", 'rheaxmag_1', 'bath_ljmr_2'),
        ("擦肩而过", 'thepast1_1', 'thepast1_10'),
        #NEEDS MORE UNLOCKS
        ("闯入者！", "keiko1_1"),
        ("正当惩罚", "keiko2_1"),
        ("喝吧……", "keiko3_1"),
        ("铁匠", 'thesmith1_1', 'thesmith1_2'),
    )

    replay_scenes['priscilla'] = replay_make_scenes(
        ("人物介绍", 'prisscene1', 'pris1_1'),
        ("在集市", 'prisscene2', 'pris2_7'),
        ("私人课程", 'prisroom1x', 'prisroom13'),
        ("逛集市", 'prisscene7', 'pris7_23'),
        ("领养宠物", 'prisscene8', 'pris8_16'),
        ("奴隶市场", 'prisscene9', 'pris9_15'),
        ("精灵精粹", 'prisscene10_1', 'pris10_41'),
        ("露丝与猫", 'prisscene12', 'pris12_11'),
        ("生病的小猫", 'prisscene13', 'pris13_9'),
        ("泰克之行", 'prisscene15_trip', 'pris15_intro_25'),
        ("喷发 I", 'prisroomxhj', 'prisroom44'),
        ("喷发 II", 'prisroomxbj', 'prisroom48'),
        ("村中女子", 'prisscene15_woman', 'pris15_vil_wom_3'),
        ("普里西拉的裙子", 'prisscene15_sleep', 'pris15_vil_sleep_8'),
        ("夜猎", 'prisscene15_nymphs4', 'pris15_nymph2_41'),
        ("海滩插曲", 'prisscene15_outing', 'pris15_lake_55'),
        ("古树之下", 'prisscene15_priscilla', 'pris15_castle5_48'),
        ("与普里西拉的一夜", 'priscilla15_priscilla_x', 'pris15_prisx_11'),
        ("芙蕾德莉卡与普里西拉", 'priscilla15_crestmoor_x', 'pris15_crestmoorx_10'),
        ("逛集市 II", 'pclone16_1', 'prisc16_22'),
        ("拜访法师", 'pris17_1', 'pris17_16'),
        ("吓到普里西拉", 'pris18_1', 'pris18_10'),
        ("漫长的一天", 'pris19_1', 'pris19_8'),
        ("重逢", 'pris20_1', 'pris20_1'),
        ("芙蕾德莉卡", 'fredrika0_1', 'fredrika1_2'),
        ("逛集市 III", 'pris16_1', 'pris16_1'),
        ("一个请求", 'pclone17_1', 'prisc18_3'),
        ("湖畔灯火", 'pclone18_1', 'prisc19_45'),
        ("普里西拉的身体", 'pris21_1', 'pris21_1'),
        ("新朋友", 'pris22_1', 'pris22_17'),
        ("心灵话题", 'pris23_1', 'pris23_1'),
        ("试探羁绊", 'pris24_1', 'pris24_26'),
        ("克莉奥与普里西拉", 'pris_swap2_1', 'prisxcleo1_36'),
        ("普里西拉的热情", 'pris25_1', 'pris25_9'),
        ("找熊", 'pris26_1', 'pris26_5'),
        ("大公夫人", 'pris27_1', 'pris27_3'),
        ("改良", 'pris28_1', 'pris28_18'),
        ("另一种选择", 'pris29_1', 'pris29_27'),
        ("科学与自然", 'pris30_1', 'pris30_2'),
        ("感应者", 'theempath2_1', 'theempath2_1'),
    )

    replay_scenes['isha'] = replay_make_scenes(
        ("伊莎登场", 'isha_scene1', 'isha1_16'),
        ("普里西拉的想法", 'ishascene2_1', 'isha2_5'),
        ("村庄祭典", 'ishascene3_1', 'isha3_5'),
        ("与伊莎共浴", 'ishascene4_1', 'isha4_15'),
        ("宗教话题", 'ishascene5_1', 'isha5_6'),
        ("娶伊莎", 'ishascene6_1', 'isha6_4'),
        ("伊莎的姐妹们", 'bona1_1', 'bona1_22'),
        ("露营之旅", 'bona2_1', 'bona2_10'),
        ("旅途之后", 'isha7_1', 'isha7_4'),
        ("疑虑", 'isha8_1', 'isha7_17'),
        ("浴场", 'bona5_1', 'bona5a_1'),
        ("伊莎的烦恼", 'isha9_1', 'isha7_45'),
        ("丰收祭", 'isha10_1', 'isha10b_32'),
        ("伊莎的担忧", 'isha11_1', 'isha11_1'),
        ("村中奇遇", 'isha12_1', 'isha12_19'),
        ("与普莉莎约会", 'isha13_1', 'isha13_2'),
        ("一个谜语", 'isha14_1', 'isha14_7'),
        ("中了埋伏", 'isha15_1', 'isha15_4'),
        ("遇见赫玛尔", 'isha16_1', 'isha16_29'),
        ("伊莎的衣服", 'isha17_1', 'isha17_1'),
        ("木偶之旅", 'isha18_1', 'isha18_23'),
        ("糟糕的糕点", 'isha19_1', 'isha19_1'),
        ("老家伙", 'isha20_1', 'isha20_2'),
        ("玛卡根", 'isha21_1', 'isha21_80'),
        ("被捕", 'isha22_1', 'isha22_104'),
        ("姐妹相见", 'isha23_1', 'isha23_1'),
        ("关于伊莎", 'isha24_1', 'isha24_12'),
        ("欲望", 'isha25_1', 'isha25_12'),
        ("幻想", 'isha26_1', 'isha26_3'),
        ("触手", 'isha_tent_1', 'ishadream_tent_10'),
        ("巫女", 'isha_dem_1', 'ishadream_dem_1'),
        ("小偷", 'isha_lord_1', 'ishadream_lord_1'),
        ("赫玛尔的青春？", 'dream_hemal_1', 'hemslut_1'),
        ("太阳仪式", 'isha27_1', 'isha27_17'),
        ("仪式完成", 'isha28_1', 'isha28_1'),
        ("博纳德人", 'thebonadeans1_1', 'thebonadeans1_2'),
    )

    replay_scenes['leona'] = replay_make_scenes(
        ("遇见莱奥娜", 'leo1_1', 'leo1_8'),
        ("城防工事", 'leo2_1', 'leo2_12'),
        ("帮老人们忙", 'leo3_1', 'leo3_12'),
        ("跑腿", 'leo4_1', 'leo4_22'),
        ("最好的肉", 'leo5_1', 'leo5_12'),
        ("求婚", 'leo6_1', 'leo6_18'),
        ("月下雄狮", 'leo7_leona_1', 'leo7l_18'),
        ("雄狮的帮手", 'leo7_arjenta_1', 'leo7a_13'),
        ("克莉奥谈里奥", 'leona8_1', 'leo8_1'),
        ("图书馆的雄狮", 'leona9_1', 'leo9_11'),
        ("阿尔真塔的希望", 'leona10_1', 'leo10_6'),
        ("普莉莎的八卦", 'leona11_1', 'leo11_1'),
        ("雄狮守望", 'leona12_1', 'leo12_9'),
        ("雄狮授课", 'leona13_1', 'leo13_4'),
        ("雄狮的颂歌", 'leona14_1', 'leo14_39'),
        ("蕾娅潜行", 'leona15_1', 'leo15_38'),
        ("病倒的仆人", 'leona16_1', 'leo16_5'),
        ("冒险者公会", 'leona17_1', 'leo17_3'),
        ("遗物搜寻", 'leona18_1', 'leo18_3'),
        ("剑之秘密", 'leona19_1', 'leo19_1'),
        ("试炼 I", 'leona20_1', 'leo20_21'),
        ("试炼 II", 'leona21_1', 'leo21_5'),
        ("试炼 III", 'leona22_1', 'leo22_3'),
        ("阿尔真塔的呼吁", 'leona23_1', 'leo23_16'),
        ("莱奥娜的呼吁", "leona24_1", 'leo24_25'),
        ("对抗恶魔", 'leona25_1', 'leo25_12'),
        ("城市守望者", 'leona26_1', 'leo26_10'),
        ("女巫的药剂", 'leona27_1', 'leo27_23'),
        ("一夜", 'leona28_1', 'leo28_33'),
        ("魔物臣服", 'leona29_1', 'leo29_32'),
        ("雄狮", 'thedemoness1_1', 'thedemoness1_2'),
    )

    replay_scenes['featana'] = replay_make_scenes(
        ("神秘旅人", 'fea1_1', 'fea1_3'),
        ("饥饿的陌生人", 'fea2_1', 'fea2_2'),
        ("奇怪的信件", 'fea3_1', 'fea3_10'),
        ("被囚的龙", 'fea4_1', 'fea4_8'),
        ("新候选人？", 'fea5_1', 'fea5_16'),
        ("普莉莎的鼻子", 'fea6_1', 'fea6_10'),
        ("牧羊人", 'fea7_1', 'fea7_19'),
        ("米娜的建议", 'fea8_1', 'fea8_23'),
        ("体能训练", 'fea9_1', 'fea9_25'),
        ("礼仪", 'fea10_1', 'fea10_6'),
        ("文化", 'fea11_1', 'fea11_11'),
        ("新朋友？", 'fea12_1', 'fea12_1'),
        ("信仰与责任", 'fea13_1', 'fea13_1'),
        ("克莉奥的意见", 'fea14_1', 'fea14_1'),
        ("龙穴", 'fea15_1', 'fea15_4'),
        ("亚麻与里拉琴", 'fea16_1', 'fea16_8'),
        ("稻草与卷轴", 'fea18_1', 'fea18_4'),
        ("黑暗交易", 'fea19_1', 'fea19_6'),
        ("圣像", 'fea20_1', 'fea20_8'),
        ("观星", 'fea21_1', 'fea21_1'),
        ("成为一条龙", 'fea22_1', 'fea22_22'),
        ("林苑", 'fea23_1', 'fea23_1'),
        ("像休姆人那样", 'fea24_1', 'fea24_25'),
        ("拟态丝绸", 'fea_mim_x', 'fea_mim_1'),
        ("我是一条龙", 'thedragon1_1', 'thedragon1_1'),
        
    )

    replay_scenes['juna'] = replay_make_scenes(
        ("学院序章", 'enteracademy2', 'intro_start_16'),
        ("早安", 'enteracademy3', 'morny2'),
        ("简报", 'morning1', 'intro_start_26'),
        ("简报（裸）", 'morning1_n', 'intro_start_68'),
        ("魅魔茱娜", 'cleo6juna_slut', 'juna_suc14'),
        ("少女茱娜", 'cleo6juna_damsel', 'juna_dam26'),
        ("瓦尔基莉茱娜", 'cleo6juna_fighter', 'juna_val8'),
        ("克莱斯特穆尔城", 'prisscene15_castle_sleep1', 'pris15_juna_13'),
        ("监守", 'juna1_1', 'junamain1_18'),
        ("蒂娜登场", 'juna2_1', 'junamain2_10'),
        ("茱娜与米娜", 'juna3_1', 'junamain3_4'),
        ("年幼的蒂娜", 'juna4_1', 'junamain4_7'),
        ("埃兹拉的新职务", 'juna5_1', 'junamain5_4'),
        ("酒吧里的两个精灵", 'juna6_1', 'junamain6_33'),
        ("米娜的报告", 'juna7_1', 'junamain7_8'),
        ("招募帮手", 'juna8_1', 'junamain8_6'),
        ("对象：茱娜", 'juna9_1', 'junamain9_5'),
        ("生命之血", 'juna10_1', 'junamain10_3'),
        ("狩猎开始", 'juna11_1', 'junamain11_9'),
        ("狩猎结束", 'juna12_1', 'junamain12_17'),
        ("意志胜于物质", 'juna13_1', 'junamain13_1'),
        ("复仇", 'juna14_1', 'junamain14_12'),
        ("她过得如何？", 'juna15_1', 'junamain15_1'),
        ("幻影子爵", 'juna16_1', 'junamain16_5'),
        ("泥泞的营地", 'juna17_1', 'junamain17_76'),
        ("妹妹的请求", 'juna18_1', 'junamain18_25'),
        ("暗影魔的差事", 'juna19_1', 'junamain19_1'),
        ("妹妹的决定", "juna20_1", 'junamain20_13'),
        ("一夜安眠", 'juna21_1', 'junamain20_13'),
        ("主人的帐篷", 'juna22_1', 'junamain22_8'),
        ("茱娜的新任务", 'fea17_1', 'fea17_9'),
        ("新的任务", 'juna23_1', 'juna23_4'),
        ("他的……", 'juna24_1', 'juna24_5'),
        ("逃走了！", 'invasion1_1', 'invasion1_10'),
        ("新的命令", 'invasion2_1', 'invasion2_7'),
        ("集结", 'invasion3_1', 'invasion3_9'),
        ("林中精灵", 'invasion4_1', 'invasion4_6'),
        ("反间谍", 'invasion5_1', 'invasion5_6'),
        ("眼熟的敌人", 'invasion6_1', 'invasion6_7'),
        ("小心你的盟友", 'invasion7_1', 'invasion7_1'),
        ("出手之前", 'invasion8_1', 'invasion8_8'),
        ("我敌人的朋友", 'invasion9_1', 'invasion9_22'),
        ("继续上路", 'invasion10_1', 'invasion10_9'),
        ("忠诚的精灵", 'theloyalelf1_1', 'theexposition3_34'),
        
    )

    replay_scenes['josie'] = replay_make_scenes(
        ("茱娜的侍从", 'servants2', 'servants1_2'),
        ("乔茜的职责", 'servants3', 'servants2_4'),
        ("夜晚的宁芙", 'servants5_nymph', 'servants5_22'),
        ("克莱斯特穆尔的任务", 'prisscene15_nymphs4', 'pris15_nymph2_41'),
        ("药水出岔子", 'josie1_1', 'josie3_48'),
        ("少女幻影", 'josie2_1', 'josie4_29'),
        ("愉快的泡澡", 'josie3_1', 'josie5_6'),
        ("只看一眼", 'josie4_1', 'josie6_6'),
        ("更友好的泡澡", 'josie5_1', 'josie7_11'),
        ("短暂的噩梦", 'josie5_3', 'josie8_8'),
        ("清醒梦", 'josie6_1', 'josie9_55'),
        ("全套服务", 'josie8_1', 'josie7_63'),
        ("炼金术师", 'fea17_1', 'fea17_8'),
        ("鲁莽", 'pris30_1', 'pris30_8'),
        ("顺应天性", 'josie11_1', 'josie11_24'),
        ("好奇心", 'josie12_1', 'josie12_8'),
        ("炼金术师", 'thealchemist1_1', 'thealchemist1_1'),
        
    )

    replay_scenes['ezra'] = replay_make_scenes(
        ("茱娜的侍从", 'servants2', 'servants1_2'),
        ("乔茜的药水", 'ezragirl', 'ezra1_25'),
        ("四处逛街", 'ezras2_1', 'ezra3_29'),
        ("水灵", 'ezras3_1', 'ezra4_8'),
        ("乔茜的建议", 'ezra5_1', 'ezra5_1'),
        ("宁芙宿舍", 'nymph0_1', 'servants6_76'),
        ("埃兹拉的挣扎", 'ezra7_1', 'ezra7_20'),
        ("乔茜的对策", 'ezra8_1', 'ezra8_43'),
        ("女孩对决", 'ezra10_1', 'ezra10_28'),
        ("性情相投", 'ezra11_1', 'ezra11_26'),
        ("遗忘", 'ezra12_1', 'ezra12_28'),
        ("埃兹拉的努力", 'ezra13_1', 'ezra13_11'),
        ("私密癖好 I", 'ezraroom_mate_1', 'ezraroom_mis_1'),
        ("私密癖好 II", 'ezraroom_dog_1', 'ezraroom_dog_2'),
        ("私密癖好 III", 'ezraroom_lap_1', 'ezraroom_lap_1'),
        ("埃兹拉的新职务", 'juna5_1', 'junamain5_8'),
        ("切磋赛", 'servants19_1', 'servants19_22'),
        ("盛装打扮", 'thesoldier1_1', 'thesoldier1_8'),
        ("水之大师", 'thesoldier2_1', 'thesoldier2_1'),
        
    )

    replay_scenes['fir'] = replay_make_scenes(
        ("野性宁芙", 'servants5_nymph', 'servants5_22'),
        ("宁芙药水", 'nymph0_1', 'servants6_41'),
        ("新衣服", 'nymph2_1', 'nymph1_35'),
        ("娇嫩柔韧", "nymph3_1", 'nymph1_11'),
        ("生长中的幼苗", 'nymph4_1', 'nymph1_18'),
        ("成熟健壮", 'nymphx_mature', 'nymph1_36'),
        ("林苑之心", 'grove1_1', 'grove1_11'),
        ("我的守护者", 'grove2_1', 'grove2_1'),
        ("顺应天性", 'josie11_1', 'josie11_31'),
    )
    
    replay_scenes['tima'] = replay_make_scenes(
        ("宗族和睦", 'servants16_1', 'servants16_2'),
        ("监守", 'juna1_1', 'junamain1_2'),
        ("蒂娜的发现", 'tima1_1', 'tima1_2'),
        ("大人不在家", 'juna2_1', 'junamain2_13'),
        ("年幼的蒂娜", 'juna4_1', 'junamain4_7'),
        ("「泥浴」", 'juna17_1', 'junamain17_9'),
        ("剑之秘密", 'leona19_1', 'leo19_33'),
        ("玩火", "tima2_1", 'tima2_4'),
    )

    replay_scenes['scarlet'] = replay_make_scenes(
        ("鲜血与强盗", 'sword_secret', 'mag6_50'),
        ("不够快", 'demon_niko_1', 'niko_demon_10'),
        ("格拉迪克斯的读心术", 'demon_gladix_0', 'arena_day2_19'),
        ("在我的床上？", 'scarlet1_1', 'scar_luce1_10'),
        ("在我的兵营？", 'scarlet2_1', 'scar_mag1_10'),
        ("在我的学院？", 'scarlet3_1', 'scar_pris1_10'),
        ("斯嘉丽的身体", 'scarlet4_1', 'scar1_3'),
        ("她现在在哪儿？", 'tima1_1', 'tima1_30'),
        ("切磋赛", 'servants19_1', 'servants19_20'),
    )

    replay_scenes['nattal'] = replay_make_scenes(
        ("营救", 'natxtal1', 'nxt19'),
        ("酒馆商议", 'natxtal2', 'nxt25'),
        ("被认领", 'ftaliya', 'ftal17'),
        ("麻烦精", 'natxtal_4', 'natxtal_xxx_3'),
    ) 

    replay_scenes['bona'] = replay_make_scenes(
        ("博纳德姐妹", 'bona1_1', 'bona1_24'),
        ("露营之旅", 'bona2_1', 'bona2_20'),
        ("萨巴的厨艺", 'bona3_1', 'bona3_1'),
        ("普莉莎的约会", 'bona4_1', 'bona4_7'),
        ("浴场", 'bona5_1', 'bona5b_45'),
        ("法蒂玛的沉思", 'bona6_1', 'bona6_27'),
        ("萨巴的卡库姆", 'bona7_1', 'bona7_49'),
        ("萨巴包办", 'bona8_1', 'bona8_49'),
        ("普莉莎开口", 'bona9_1', 'bona9_9'),
        ("博纳德人", 'thebonadeans1_1', 'thebonadeans1_2'),
    ) 

    replay_scenes['zuki'] = replay_make_scenes(
        ("敌人", 'zuki1_1', 'zuki1_1'),
        ("盟友", 'zuki2_1', 'zuki2_3'),
        ("荣誉", 'zuki3_1', 'zuki3_8'),
        ("感激", 'zuki4_1', 'zuki4_14'),
        ("家庭", 'zuki5_1', 'zuki5_27'),
    )

    replay_scenes['sash'] = replay_make_scenes(
        ("试骑", 'cherrybite7', 'sash1_30'),
        ("与狼共舞", 'sash_bro2', 'sash_dream_85'),
        ("不可能的任务", "marion11_1"),
        ("不可能的任务 II", 'cherry8_1', 'cherry8_11'),
    )

    replay_scenes['bastet'] = replay_make_scenes(
        ("乖狗狗", 'brothelbas1', 'bastet1_28'),
        ("听命令？", 'bastet2_1', 'bastet2_24'),
        ("小鸡与猫", 'bastet3_1', 'bastet3_54'),
        ("偷窥狂", "bastet_cn", 'bastet4_2'),
        ("湿漉漉的猫", "bastet_cn_x", 'bastet5_24'),
    )

    replay_scenes['ingnetta'] = replay_make_scenes(
        ("抉择，抉择", 'brothelingn1', 'ingn1_3'),
        ("遇险少女(?)", 'brothelingn3_1', 'ingn3_3'),
        ("爸爸是谁？", 'brothelingn4_1', 'ingn4_51'),
        ("按摩手法", 'rummi1', 'rummi1_xxx_5'),
    )

    replay_scenes['yuel'] = replay_make_scenes(
        ("尝鲜", 'brothelyuel1', 'yuel1_60'),
        ("最美之人", 'broyuel4_1', 'yuel4_6'),
        ("别碰", 'broyuel5_1', 'yuel5_19'),
        ("一家人", 'broyuel6_1', 'yuel6_17'),
        ("哈埃尔的交易", "hael1_1", 'hael1_23'),
    )
    
    replay_scenes['marion'] = replay_make_scenes(
        ("扇子风波", 'marion1_1', 'marion1_26'),
        ("双胞胎", 'marion2_1', 'marion2_22'),
        ("我的班底", 'marion3_1', 'marion3_20'),
        ("公事公办", 'marion4_1', 'marion4_32'),
        ("头号粉丝", 'marion5_1', 'marion5_20'),
        ("和婊子一样", 'marion6_1', 'marion6_4'),
        ("艺术眼光", 'marion7_1', 'marion7_9'),
        ("我与好友们", 'marion8_1', 'marion8_15'),
        ("骄傲的缪斯", 'marion9_1', 'marion9_14'),
        ("天黑以后", 'marion10_1', 'marion10_17'),
        ("一对讨厌鬼", 'marion11_1', 'marion11_14'),
        ("仪式", 'marion12_1', 'marion12_23'),
        ("一对扇子", 'marion13_1', 'marion13_11'),
        ("女巫自有安排", 'marion14_1', 'marion14_1'),
        ("生动想象", 'marion15_1', 'marion15_15'),
        ("梦中", 'marion16_1', 'marion16_9'),
        ("冒牌货", 'marion17_1', 'marion17_29'),
        ("帮手", 'marion18_1', 'marion18_12'),
        ("名流", 'marion19_1', 'marion19_21'),
        ("怪人", 'marion20_1', 'marion20_13'),
        ("终章", 'marion21_1', 'marion21_50'),
        ("噩梦续篇", 'marion22_1', 'marion22_15'),
        ("茱蒂的拒绝", 'jdy_thedate1_1', 'jdydate1_37'),
        ("知名贵妇", 'jdy_thedate2_1', 'jdydate1_8'),
        ("服药过量", 'marion23_1', 'marion23_1'),
        ("艾米的顾虑", 'marion24_1', 'marion24_1'),
        ("回心转意", 'marion25_1', 'marion25_10'),
        ("筹谋一小时", 'marion26_1', 'marion26_5'),
        ("侦查", 'marion27_1', 'marion27_12'),
        ("面具之间", 'marion28_1', 'marion28_1'),
        ("回来了", 'marion29_1', 'marion29_19'),
        ("心绪不宁", 'marion30_1', 'marion30_18'),
        ("沟通不良", 'marion31_1', 'marion31_13'),        
        ("三人共浴", 'marion32_1', 'marion32_5'),
        ("天堂之门", 'marion33_1', 'marion33_3'),
        ("失去之后", 'marion34_1', 'marion34_24'),
        ("汇报", 'marion35_1', 'marion35_9'),
        ("又是平常一天", 'marion36_1', 'marion36_7'),
        ("妹妹的阴谋", 'marion37_1', 'marion37_12'),
        ("妹妹的阴谋 II", 'marion38_1', 'marion38_11'),
        ("在我们开始之前……", "judy_xd_1", 'marionroom1_20'),
        ("双生面容", 'amy_jdy1_1', 'amyxjdy1_11'),
        ("茱蒂·玛丽昂", 'thetwin_judy_1', 'thetwin_judy_5'),
        ("艾米·玛丽昂", 'thetwin_amy_1', 'thetwin_amy_1'),
        
        #NEEDS IMAGES
        ("换装", "judy_xd2_1"),
        ("茱蒂的房间 I", "judy_hj"),
        ("茱蒂的房间 II", "judy_dog"),
        ("艾米的房间 I", "amy_cow"),
        ("艾米的房间 II", "amy_mis"),
    )