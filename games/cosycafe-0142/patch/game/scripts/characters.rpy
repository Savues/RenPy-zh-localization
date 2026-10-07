screen characters1():

    tag menu
    use game_menu("角色一览"):

        fixed:

            vbox:

                xalign 0.0
                yalign 0.0
                # xpos 230
                spacing 15

                hbox:
                    spacing 15

                    if persistent.characters_lucy == True:
                        imagebutton auto "characters_lucy_%s":
                                focus_mask True
                                action Show("characters_lucy", transition = dissolve)
                    else:
                        add "characters_locked"
                    
                    if persistent.characters_victoria == True:
                        imagebutton auto "characters_victoria_%s":
                                focus_mask True
                                action Show("characters_victoria", transition = dissolve)
                    else:
                        add "characters_locked"

                    if persistent.characters_sarah == True:
                        imagebutton auto "characters_sarah_%s":
                                focus_mask True
                                action Show("characters_sarah", transition = dissolve)
                    else:
                        add "characters_locked"

                    if persistent.characters_akatsuki == True:
                        imagebutton auto "characters_akatsuki_%s":
                                focus_mask True
                                action Show("characters_akatsuki", transition = dissolve)
                    else:
                        add "characters_locked"

                    if persistent.characters_rachel == True:
                        imagebutton auto "characters_rachel_%s":
                                focus_mask True
                                action Show("characters_rachel", transition = dissolve)
                    else:
                        add "characters_locked"

                    if persistent.characters_hannah == True:
                        imagebutton auto "characters_hannah_%s":
                                focus_mask True
                                action Show("characters_hannah", transition = dissolve)
                    else:
                        add "characters_locked"

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 15

                    hbox:
                        spacing 15

                        if persistent.characters_headmistress == True:
                            imagebutton auto "characters_headmistress_%s":
                                    focus_mask True
                                    action Show("characters_headmistress", transition = dissolve)
                        else:
                            add "characters_locked"
                        
                        if persistent.characters_taka == True:
                            imagebutton auto "characters_taka_%s":
                                    focus_mask True
                                    action Show("characters_taka", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_akari == True:
                            imagebutton auto "characters_akari_%s":
                                    focus_mask True
                                    action Show("characters_akari", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_catherine == True:
                            imagebutton auto "characters_catherine_%s":
                                    focus_mask True
                                    action Show("characters_catherine", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_elizabeth == True:
                            imagebutton auto "characters_elizabeth_%s":
                                    focus_mask True
                                    action Show("characters_elizabeth", transition = dissolve)
                        else:
                            add "characters_locked"

            hbox:
                # style_prefix "quick"

                xalign 0.0
                yalign 0.9
                spacing 40

                textbutton _("主要角色") text_size 45 action ShowMenu("characters1")
                textbutton _("次要角色") text_size 45 action ShowMenu("characters2")

screen characters2():

    tag menu
    use game_menu("角色一览"):

        fixed:

            vbox:

                xalign 0.0
                yalign 0.0
                # xpos 230
                spacing 15

                hbox:
                    spacing 15

                    if persistent.characters_mika == True:
                        imagebutton auto "characters_mika_%s":
                                focus_mask True
                                action Show("characters_mika", transition = dissolve)
                    else:
                        add "characters_locked"
                    
                    if persistent.characters_brian == True:
                        imagebutton auto "characters_brian_%s":
                                focus_mask True
                                action Show("characters_brian", transition = dissolve)
                    else:
                        add "characters_locked"

                    if persistent.characters_lenny == True:
                        imagebutton auto "characters_lenny_%s":
                                focus_mask True
                                action Show("characters_lenny", transition = dissolve)
                    else:
                        add "characters_locked"

                    if persistent.characters_baker == True:
                        imagebutton auto "characters_baker_%s":
                                focus_mask True
                                action Show("characters_baker", transition = dissolve)
                    else:
                        add "characters_locked"

                    if persistent.characters_wong == True:
                        imagebutton auto "characters_wong_%s":
                                focus_mask True
                                action Show("characters_wong", transition = dissolve)
                    else:
                        add "characters_locked"

                    if persistent.characters_lucymother == True:
                        imagebutton auto "characters_lucymother_%s":
                                focus_mask True
                                action Show("characters_lucymother", transition = dissolve)
                    else:
                        add "characters_locked"


                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 15

                    hbox:
                        spacing 15

                        if persistent.characters_chloe == True:
                            imagebutton auto "characters_chloe_%s":
                                focus_mask True
                                action Show("characters_chloe", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_danny == True:
                            imagebutton auto "characters_danny_%s":
                                    focus_mask True
                                    action Show("characters_danny", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_lily == True:
                            imagebutton auto "characters_lily_%s":
                                    focus_mask True
                                    action Show("characters_lily", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_hamilton == True:
                            imagebutton auto "characters_hamilton_%s":
                                    focus_mask True
                                    action Show("characters_hamilton", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_cassandra == True:
                            imagebutton auto "characters_cassandra_%s":
                                    focus_mask True
                                    action Show("characters_cassandra", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_annabelle == True:
                            imagebutton auto "characters_annabelle_%s":
                                    focus_mask True
                                    action Show("characters_annabelle", transition = dissolve)
                        else:
                            add "characters_locked"



                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 15

                    hbox:
                        spacing 15

                        if persistent.characters_mary == True:
                            imagebutton auto "characters_mary_%s":
                                focus_mask True
                                action Show("characters_mary", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_regi == True:
                            imagebutton auto "characters_regi_%s":
                                focus_mask True
                                action Show("characters_regi", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_sis1 == True:
                            imagebutton auto "characters_sis1_%s":
                                focus_mask True
                                action Show("characters_sis1", transition = dissolve)
                        else:
                            add "characters_locked"

                        if persistent.characters_sis2 == True:
                            imagebutton auto "characters_sis2_%s":
                                focus_mask True
                                action Show("characters_sis2", transition = dissolve)
                        else:
                            add "characters_locked"



            hbox:
                # style_prefix "quick"

                xalign 0.0
                yalign 0.9
                spacing 40

                textbutton _("主要角色") text_size 45 action ShowMenu("characters1")
                textbutton _("次要角色") text_size 45 action ShowMenu("characters2")



###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################

#MAIN CHARACTER SCREENS

screen characters_lucy():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_lucy_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "露西" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                if persistent.characters_lucy_job1 == True:
                                    text "学生" size 32
                                if persistent.characters_lucy_job2 == True:
                                    text "、女招待" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                if persistent.characters_lucy_family1 == True:
                                    text "母亲" size 32
                                if persistent.characters_lucy_family2 == True:
                                    text "、父亲（关系不睦）" size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "某天走进你咖啡馆的一个害羞女孩。" size 32

                        if persistent.characters_lucy_note1 == True:
                            text "稍微熟络之后，露西成了你的女招待长。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                        if persistent.characters_lucy_note2 == True:
                            text "露西为了逃离暴虐的母亲，搬来和你同住。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                        if persistent.characters_lucy_note3 == True:
                            text "露西成为了你的第一个女朋友。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")

screen characters_victoria():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_victoria_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "维多利亚" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                if persistent.characters_victoria_job1 == True:
                                    text "学生" size 32
                                if persistent.characters_victoria_job2 == True:
                                    text "、女招待" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                if persistent.characters_victoria_family1 == True:
                                    text "母亲（已故）" size 32
                                if persistent.characters_victoria_family2 == True:
                                    text "、父亲（关系不睦）" size 32
                                if persistent.characters_victoria_family3 == True:
                                    text "、哥哥（丹尼）" size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "你在通学列车上遇见的刻薄女孩。" size 32

                        if persistent.characters_victoria_note1 == True:
                            text "维多利亚苦苦哀求要当女招待。你答应了她，条件是她得听话。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                        if persistent.characters_victoria_note2 == True:
                            text "维多利亚开始做女招待后，你们渐渐熟络起来，最后她成了你的女朋友，还搬进了咖啡馆。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")

screen characters_sarah():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_sarah_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "莎拉" size 32
                                if persistent.characters_sarah_foundingfamily == True:
                                    text " 汉密尔顿（创始家族）" color ("#d90d32") size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                if persistent.characters_sarah_job1 == True:
                                    text "学生" size 32
                                if persistent.characters_sarah_job2 == True:
                                    text "、市场企划兼女招待" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                if persistent.characters_sarah_family1 == True:
                                    text "母亲（莉莉）" size 32
                                if persistent.characters_sarah_family2 == True:
                                    text "、父亲" size 32
                                if persistent.characters_sarah_family3 == True:
                                    text "、姐妹们" size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "给你做衣服的小恶魔。露西最好的朋友。" size 32

                        if persistent.characters_sarah_note1 == True:
                            text "莎拉成了你的市场企划兼兼职女招待。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                        if persistent.characters_sarah_note2 == True:
                            text "莎拉因为网上的角色扮演被人盯上了，你不得不保护她。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")

screen characters_akatsuki():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_akatsuki_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "晓月" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                if persistent.characters_akatsuki_job1 == True:
                                    text "学生" size 32
                                if persistent.characters_akatsuki_job2 == True:
                                    text "、见习厨师" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                if persistent.characters_akatsuki_family1 == True:
                                    text "父亲" size 32
                                if persistent.characters_akatsuki_family4 == True:
                                    text "、母亲" size 32
                                if persistent.characters_akatsuki_family3 == True:
                                    text "、姐姐（明里）" size 32
                                if persistent.characters_akatsuki_family2 == True:
                                    text "、表姐（高村小姐）" size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "一个寡言的女孩，你在一场厨艺对决中赢下了她。她后来成了你的学徒。" size 32

                        if persistent.characters_akatsuki_note1 == True:
                            text "晓月答应用爷爷的厨艺秘方，换取成为你的专属猫娘。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                        if persistent.characters_akatsuki_note2 == True:
                            text "你和晓月决定联手，击败她那位天才姐姐。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                        if persistent.characters_akatsuki_note3 == True:
                            text "你发现晓月一直在替父亲对你撒谎。最终她选择了你，成了你的女朋友。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")

screen characters_rachel():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_rachel_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "瑞秋" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                if persistent.characters_rachel_job1 == True:
                                    text "学生" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "学生会长，外加一个疯狂女权主义者。" size 32

                        if persistent.characters_rachel_note1 == True:
                            text "瑞秋似乎把「解救」你的那些女孩当成了使命，方式就是不断纠缠你。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")

screen characters_hannah():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_hannah_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "汉娜" size 32
                                if persistent.characters_hannah_foundingfamily == True:
                                    text " 吉尔伯特（创始家族）" color ("#d90d32") size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                if persistent.characters_hannah_job1 == True:
                                    text "学生" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                if persistent.characters_hannah_family1 == True:
                                    text "姐姐（校长）" size 32
                                if persistent.characters_hannah_family2 == True:
                                    text "、父亲" size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "一个优柔寡断的女孩。她和欺负露西的那帮人走得很近，但没人在时看起来还挺不错。" size 32

                        if persistent.characters_hannah_note1 == True:
                            text "汉娜和布莱恩之间有某种「政治婚约」，校长想让你把它搅黄。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                        if persistent.characters_hannah_note2 == True:
                            text "校长决定让汉娜到咖啡馆当女招待。你勉强同意。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")

screen characters_headmistress():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_headmistress_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                if persistent.characters_headmistress_name == True:
                                    text "埃莉森" size 32
                                elif persistent.characters_headmistress_foundingfamily == True:
                                    text "???" size 32
                                if persistent.characters_headmistress_foundingfamily == True:
                                    text " 吉尔伯特（创始家族）" color ("#d90d32") size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "27" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                if persistent.characters_headmistress_job1 == True:
                                    text "校长" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                if persistent.characters_headmistress_family1 == True:
                                    text "妹妹（汉娜）" size 32
                                if persistent.characters_headmistress_family2 == True:
                                    text "、父亲" size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "芬兹伯勒学院的校长。以这个职位而论，她看起来相当年轻。" size 32

                        if persistent.characters_headmistress_note1 == True:
                            text "校长对你爷爷的事讳莫如深，你很想知道原因。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32
                        if persistent.characters_headmistress_note2 == True:
                            text "看来她是想把你挡在创始家族之外，可你逼她说出了实情。现在她希望你能靠取得一定的地位，把她的妹妹汉娜从那桩婚约里救出来。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32
                        if persistent.characters_headmistress_note3 == True:
                            text "校长同意做我的秘书，替我处理创始家族的事务。我能不能信任她，只有时间能证明。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")

screen characters_taka():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_taka_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                if persistent.characters_taka_name == True:
                                    text "高村美咲" size 32
                                else:
                                    text "高村小姐" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "22" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                if persistent.characters_taka_job1 == True:
                                    text "老师" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                if persistent.characters_taka_family1 == True:
                                    text "表姐妹（晓月与明里）、叔叔（高村先生（Wong？））" size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "你在学校里的老师。她非常年轻，显然没什么经验。" size 32

                        if persistent.characters_taka_note1 == True:
                            text "你在电车上摸了她一把，她似乎挺享受，却又神色纠结。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                        if persistent.characters_taka_note2 == True:
                            text "在多次摸奶之后，她吐露心声说自己想要改变。她想变成一个更外向、更自信的女人，也许还能成为我的专属肉便器。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32

                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")

screen characters_akari():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_akari_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "明里" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "20" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "天才厨师" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                if persistent.characters_akatsuki_family1 == True:
                                    text "父亲" size 32
                                if persistent.characters_akatsuki_family4 == True:
                                    text "、母亲" size 32
                                if persistent.characters_akatsuki_family3 == True:
                                    text "、妹妹（晓月）" size 32
                                if persistent.characters_akatsuki_family2 == True:
                                    text "、表妹（高村小姐）" size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "一个张扬外放的女孩。她在厨艺对决中把你彻底打败，证明了自己在厨房里的天赋。" size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")

screen characters_catherine():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_catherine_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "凯瑟琳" size 32
                                if persistent.characters_catherine_foundingfamily == True:
                                    text " 贝内特（创始家族）" color ("#d90d32") size 32


                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "学生" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                if persistent.characters_catherine_family1 == True:
                                    text "父亲（雷金纳德）、母亲（玛丽）" size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "一个傲慢的富家女。米卡和布莱恩的朋友。" size 32

                        if persistent.characters_catherine_note1 == True:
                            text "你发现凯瑟琳的父母逼她去送外卖。你答应替她保密，条件是她别那么讨人厌。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32
                        if persistent.characters_catherine_note2 == True:
                            text "汉密尔顿家的派对之后，凯瑟琳开始黏着你，并表明她打算嫁给你。你拒绝了。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")

screen characters_elizabeth():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_elizabeth_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "伊丽莎白" size 32
                                text " 拉塞尔（创始家族）" color ("#d90d32") size 32


                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "20" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                #text "Student" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                text "母亲（拉塞尔太太）、哥哥（布莱恩）" size 32

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "布莱恩的妹妹。她冲进你的厨房，要求你拒绝她母亲的提议。" size 32

                        # if persistent.characters_catherine_note1 == True:
                        #     text "You discovered that Catherine's parents made her take a part-time job delivering pizzas. You agreed to keep this secret in exchange for her being less bitchy." size 32
                        # else:
                        #     text "{i}**Locked.**{/i}" color ("#9e9e9e") size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters1")




###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################

#SIDE CHARACTER SCREENS

screen characters_mika():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_mika_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "米卡" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "学生" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "你在电车上遇见的一个恶毒贱货，当时她正在欺负露西。和布莱恩走得很近。" size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_brian():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_brian_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "布莱恩" size 32
                                if persistent.characters_brian_foundingfamily == True:
                                    text " 拉塞尔（创始家族）" color ("#d90d32") size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "学生" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "你在电车上遇见的一只油滑黄鼠狼，当时米卡正在欺负露西。" size 32

                        if persistent.characters_brian_note1 == True:
                            text "布莱恩警告你离维多利亚远一点，因为她是「他的」。可维多利亚对他毫无兴趣。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_lenny():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_lenny_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "兰尼" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "学生" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "你在电车上遇见的一个大块头蠢货。布莱恩的跟班。可能正迷恋着米卡。" size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_baker():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_baker_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "62" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "面包师" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                text "大家庭" size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "为你的咖啡馆供货的友善面包师。他周末会带着一大家子来吃饭，而且认识你爷爷。" size 32
                        if persistent.characters_baker_note1 == True:
                            text "面包师跟你讲了一些创始家族的事。据说你爷爷是其中之一，那你就是他的继承人？" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_wong():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_wong_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "高村先生（Wong？）" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "48" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "「Wong’s Chinese Dragon」餐厅的老板兼主厨。" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                
                                if persistent.characters_akatsuki_family3 == True:
                                    text "女儿（晓月与明里）" size 32
                                else:
                                    text "女儿（晓月）" size 32
                                if persistent.characters_akatsuki_family4 == True:
                                    text "、妻子" size 32
                                if persistent.characters_akatsuki_family2 == True:
                                    text "、侄女（高村小姐）" size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "镇上另一家餐厅的老板。为人极其古怪，视你为竞争对手。" size 32
                        if persistent.characters_akari == True:
                            text "你在厨艺对决中输给明里之后，他单方面宣布晓月要嫁给你。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_lucymother():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_lucymother_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "49" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                text "女儿（露西）" size 32
                                text "、丈夫（已离婚）" size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "露西那位压迫人、动辄虐待她的母亲。" size 32
                        if persistent.characters_lucymother_note1 == True:
                            text "露西离开之后，她跑去学校，试图在校长那里给你找麻烦。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_chloe():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_chloe_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "克洛伊" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "18" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "学生" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32                              

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "米卡和凯瑟琳的朋友。" size 32

                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_danny():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_danny_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "丹尼" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "25" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                if persistent.characters_victoria_family1 == True:
                                    text "母亲（已故）" size 32
                                if persistent.characters_victoria_family2 == True:
                                    text "、父亲（关系不睦）" size 32
                                if persistent.characters_victoria_family3 == True:
                                    text "、妹妹（维多利亚）" size 32                        

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "维多利亚的哥哥。听起来像是在做些见不得光的勾当，不过他似乎是个好人，维多利亚也信任他。" size 32

                        text "初次见面时丹尼试探过你；你通过之后，他问你维多利亚能不能留下来和你一起住。还让你答应保护她。" size 32

                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_lily():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_lily_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "莉莉" size 32
                                text " 汉密尔顿（创始家族）" color ("#d90d32") size 32


                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "35" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                #text "Student" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                text "丈夫（汉密尔顿先生）、女儿（莎拉）" size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "莎拉的母亲。代表丈夫——汉密尔顿家族的当家——邀请你参加派对。" size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_annabelle():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_annabelle_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "安娜贝尔" size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "20" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                #text "Student" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "在汉密尔顿家的派对上试图自我介绍、手足无措的女孩。" size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_cassandra():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_cassandra_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "卡珊德拉" size 32
                                text " 汉密尔顿（创始家族）" color ("#d90d32") size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "42" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                #text "Student" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                text "丈夫（汉密尔顿先生）、女儿" size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "汉密尔顿先生的其中一位妻子。莎拉那群刻薄的姐妹中，至少有一位是她生的。" size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_hamilton():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_hamilton_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "汉密尔顿先生（家族当家）" color ("#d90d32") size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "55" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "家族当家" size 32

                            hbox:
                                vbox:
                                    hbox:
                                        text "家族：" color ("#99ccff") size 32
                                        text "妻子（莉莉、卡珊德拉）、女儿（莎拉）、子女（众多）、姐姐（玛丽·贝内特）、姐夫（雷金纳德·贝内特）" size 32
                                

                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "莎拉的父亲，汉密尔顿家族的当家。" size 32
                        text "他在派对宾客面前揭露了你身为第五大家族当家的身份，还暗示你与莎拉已经订婚。" size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_mary():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_mary_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "玛丽" size 32
                                text " 贝内特（创始家族）" color ("#d90d32") size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "48" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                #text "Student" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                text "丈夫（雷金纳德）、女儿（凯瑟琳）、哥哥（汉密尔顿先生）" size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "凯瑟琳的母亲。傲慢又刻薄，显然打心眼里瞧不起创始家族以外的人。" size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_regi():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_regi_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "雷金纳德" size 32
                                text " 贝内特（家族当家）" color ("#d90d32") size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "46" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                text "家族当家" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                text "妻子（玛丽）、女儿（凯瑟琳）、姐夫（汉密尔顿先生）" size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "凯瑟琳的父亲，贝内特家族的当家。" size 32
                        text "一个和蔼开朗的男人。显然完全听老婆的。" size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_sis1():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_sis1_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:
                                text "姓名：" color ("#99ccff") size 32
                                text "?" size 32
                                text " 汉密尔顿（创始家族）" color ("#d90d32") size 32

                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "20" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                #text "Student" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                text "父亲（汉密尔顿先生）、姐姐（莎拉）、兄弟姐妹（众多）" size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "莎拉那些刻薄的同父异母姐妹之一。" size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")

screen characters_sis2():

    tag menu
    use game_menu("角色一览"):

        fixed:

                vbox:

                    xalign 0.0
                    yalign 0.0
                    # xpos 230
                    spacing 35

                    hbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 25

                        add "characters_sis2_idle"

                        vbox:

                            xalign 0.0
                            yalign 0.0
                            # xpos 230
                            spacing 15

                            hbox:

                                if persistent.characters_sis2_name == True:
                                    text "姓名：" color ("#99ccff") size 32
                                    text "米拉" size 32
                                    text " 汉密尔顿（创始家族）" color ("#d90d32") size 32
                                else:
                                    text "姓名：" color ("#99ccff") size 32
                                    text "?" size 32
                                    text " 汉密尔顿（创始家族）" color ("#d90d32") size 32



                            hbox:
                                text "年龄：" color ("#99ccff") size 32
                                text "20" size 32

                            hbox:
                                text "职业：" color ("#99ccff") size 32
                                #text "Student" size 32

                            hbox:
                                text "家族：" color ("#99ccff") size 32
                                text "父亲（汉密尔顿先生）、姐姐（莎拉）、兄弟姐妹（众多）" size 32
                                

                    vbox:

                        xalign 0.0
                        yalign 0.0
                        # xpos 230
                        spacing 15

                        text "备注" color ("#99ccff") size 40

                        text "莎拉那些刻薄的同父异母姐妹之一。" size 32
                        if persistent.characters_sis2_note1 == True:
                            text "你在莎拉卧室的一张照片背景里发现了那个跟踪狂。看来他们以前是同学。" size 32
                        else:
                            text "{i}**未解锁。**{/i}" color ("#9e9e9e") size 32


                hbox:
                
                    xalign 0.0
                    yalign 0.9
                    spacing 25

                    textbutton _("返回") text_size 50 action ShowMenu("characters2")