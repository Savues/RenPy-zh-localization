translate schinese python:
        _realm_invader_name_replacements = (
            ("Kid that only says goon shit like \"I dunno about this one, boss\"", "只会说“我不知道这个，老板”这种蠢话的孩子"),
            ("Kid that might be some kind of gangster", "可能是某种黑帮分子的孩子"),
            ("Kid that looks like the boss", "看起来像老板的孩子"),
            ("Home Economics Teacher", "家政课老师"),
            ("Disgruntled Employee", "不满的职员"),
            ("DJ with unspecified name", "姓名不详的 DJ"),
            ("Animal Handler", "动物管理员"),
            ("Young Elf Girl", "年轻精灵女孩"),
            ("Female voice", "女声"),
            ("Male voice", "男声"),
            ("Good Grace", "善良的格蕾丝"),
            ("Evil Grace", "邪恶的格蕾丝"),
            ("Big Kelly", "大凯莉"),
            ("Slobby Bobby", "邋遢鲍比"),
            ("Bumzilla Gumz", "布姆吉拉·古姆兹"),
            ("Samuel Harper", "塞缪尔·哈珀"),
            ("Dr. Bashford", "巴什福德博士"),
            ("Miss. Greenslade", "格林斯莱德小姐"),
            ("Mr. Stewart", "斯图尔特先生"),
            ("Shady Guy", "可疑男子"),
            ("Marcello", "马尔切洛"),
            ("Marcus", "马库斯"),
            ("Meryl", "梅瑞尔"),
            ("Mikey", "迈基"),
            ("Vineeta", "维妮塔"),
            ("Cadence", "凯登丝"),
            ("Clement", "克莱门特"),
            ("Doomchild", "末日之子"),
            ("Guillaume", "纪尧姆"),
            ("Liliana", "莉莉安娜"),
            ("Noelle", "诺艾尔"),
            ("Philica", "菲莉卡"),
            ("Ronald", "罗纳德"),
            ("Sandrelle", "桑德雷尔"),
            ("Security", "安保人员"),
            ("Selvo", "塞尔沃"),
            ("Stranger", "陌生人"),
            ("Student", "学生"),
            ("Teacher", "老师"),
            ("Cashier", "收银员"),
            ("Kid", "孩子"),
            ("Bumzilla", "布姆吉拉"),
            ("Gumz", "古姆兹"),
            ("Ashley", "阿什莉"),
            ("Butler", "管家"),
            ("Cardi", "卡迪"),
            ("Chase", "蔡斯"),
            ("Chloe", "克洛伊"),
            ("Croupier", "荷官"),
            ("Developer", "开发者"),
            ("Doctor", "医生"),
            ("Freda", "芙蕾达"),
            ("Grace", "格蕾丝"),
            ("Hannah", "汉娜"),
            ("Helga", "海尔加"),
            ("Hobo", "流浪汉"),
            ("Hugo", "雨果"),
            ("Kelly", "凯莉"),
            ("Lecturer", "讲师"),
            ("Lexi", "莱克西"),
            ("Miya", "米娅"),
            ("Philly", "菲利"),
            ("Radio", "电台"),
            ("Ricky", "瑞奇"),
            ("Staff", "店员"),
            ("Stella", "斯特拉"),
            ("Stewart", "斯图尔特"),
            ("T-Dot", "泰·多特"),
            ("Tisha", "蒂莎"),
            ("Trent", "特伦特"),
            ("Woman", "女人"),
            ("Zoe", "佐伊"),
            ("[name] (Past)", "[name]（过去）"),
            ("[name] (Present)", "[name]（现在）"),
            ("???", "？？？"),
            ("Ron", "罗纳德"),
            ("Carlos", "卡洛斯"),
            ("Nala", "娜拉"),
            ("Clarissa", "克拉丽莎"),
            ("Neeta", "维妮塔"),
        )
        _realm_invader_name_replacements = sorted(
            _realm_invader_name_replacements,
            key=lambda item: len(item[0]),
            reverse=True,
        )
        for _realm_invader_value in list(globals().values()):
            if type(_realm_invader_value).__name__ not in ("ADVCharacter", "NVLCharacter"):
                continue
            _realm_invader_name = _realm_invader_value.name
            if type(_realm_invader_name).__name__ not in ("str", "unicode"):
                continue
            if not hasattr(_realm_invader_value, "_realm_invader_original_name"):
                _realm_invader_value._realm_invader_original_name = _realm_invader_name
            for _realm_invader_old, _realm_invader_new in _realm_invader_name_replacements:
                _realm_invader_name = _realm_invader_name.replace(_realm_invader_old, _realm_invader_new)
            _realm_invader_value.name = _realm_invader_name
        del _realm_invader_name_replacements

translate None python:
        for _realm_invader_value in list(globals().values()):
            if type(_realm_invader_value).__name__ not in ("ADVCharacter", "NVLCharacter"):
                continue
            if hasattr(_realm_invader_value, "_realm_invader_original_name"):
                _realm_invader_value.name = _realm_invader_value._realm_invader_original_name
