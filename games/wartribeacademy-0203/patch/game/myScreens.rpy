# ALL POSSIBLE FLAGS
# FASTTRAVEL SCREEN
# FAST TRAVEL SCREEN
#FAST TRACK MAP
screen mainScreen():
    imagemap:
        ground "images/bg/fast_travel.webp"
        hotspot(758, 335, 119, 47) action Jump("mainend")
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "images/icon/xbutton0.png"
        hover "images/icon/xbutton.png"
        focus_mask True
        action Jump("mainend") alt "卧室"
    imagebutton:
        xalign 0.9
        yalign 0.05
        idle "images/icon/minimap.webp"
        hover "images/icon/minimap_hover.webp"
        focus_mask True
        action Jump("worldmap1") alt "世界地图"

#ISHA
    if servants >= 3 and loveisha == 0:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha_scene1") alt "伊莎快速旅行"
    elif loveisha == 1:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("ishascene2_1") alt "伊莎快速旅行"
    elif loveisha == 2:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("ishascene3_1") alt "伊莎快速旅行"
    elif loveisha == 3:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("ishascene4_1") alt "伊莎快速旅行"
    elif loveisha == 4:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("ishascene5_1") alt "伊莎快速旅行"
    elif loveisha == 5:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("ishascene6_1") alt "伊莎快速旅行"
    elif servants < 13 and loveisha == 6:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("servantsx") alt "伊莎快速旅行"
    elif servants >= 13 and loveisha == 6:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("bona1_1") alt "伊莎快速旅行"
    elif loveisha == 7:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("bona2_1") alt "伊莎快速旅行"
    elif loveisha == 8:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha7_1") alt "伊莎快速旅行"
    elif loveisha == 9:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("bona3_1") alt "伊莎快速旅行"
    elif loveisha == 10:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha8_1") alt "伊莎快速旅行"
    elif loveisha == 11:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("bona4_1") alt "伊莎快速旅行"
    elif loveisha == 12:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("bona5_1") alt "伊莎快速旅行"
    elif loveisha == 13:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("bona6_1") alt "伊莎快速旅行"
    elif loveisha == 14:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("bona7_1")
    elif loveisha == 15:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("bona8_1")
    elif loveisha == 16:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha9_1")
    elif loveisha == 17:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha10_1")
    #1.4.0
    elif loveisha == 18:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha11_1")
    elif loveisha == 19:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha12_1")
    elif loveisha == 20:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha13_1")
    elif loveisha == 21:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha14_1")
    elif loveisha == 22:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha15_1")
    elif loveisha == 23:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha16_1")
    elif loveisha == 24:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("zuki1_1")
    elif loveisha == 25:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha17_1")
    elif loveisha == 26:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("zuki2_1")
    elif loveisha == 27:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha18_1")
    elif loveisha == 28:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha19_1")
    elif loveisha == 29:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha20_1")
    elif loveisha == 30:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("zuki3_1")
    elif loveisha == 31:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha21_1")
    elif loveisha == 32:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha22_1")
    elif loveisha == 33:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("zuki4_1")
    elif loveisha == 34:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha23_1")
    elif loveisha == 35:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("zuki5_1")
    elif loveisha == 36:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha24_1")
    elif loveisha == 37:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha25_1")
    elif loveisha == 38:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha26_1")
    elif loveisha == 39:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha27_1")
    elif loveisha == 40:
        imagebutton:
            xalign 0.0
            yalign 0.7
            idle "images/icon/ishaicon1.png"
            hover "images/icon/ishaicon.png"
            focus_mask True
            action Jump("isha28_1")
#CLEO
    if lovecleo == 0:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene1")
            alt "克莉奥快速旅行"
    elif lovecleo == 1:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene2") alt "克莉奥快速旅行"
    elif cleopmag == 1:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleopmag1") alt "克莉奥快速旅行"
    elif cleopluce == 1:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleopluce1") alt "克莉奥快速旅行"
    elif cleoprhea == 1:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoprhea1") alt "克莉奥快速旅行"
    elif cleoppris == 1:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoppris1") alt "克莉奥快速旅行"
    elif lovecleo == 3 and cleopotion == 1 and metjosie == 0:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("servants2") alt "克莉奥快速旅行"
    elif lovecleo == 3 and cleopotion == 1 and metjosie == 1:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("seejosiex") alt "克莉奥快速旅行"
    elif cleoppris == 2 and cleoprhea == 2 and cleopmag == 2 and cleopluce == 2 and cleopotion == 2 and lovecleo == 3:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene4") alt "克莉奥快速旅行"
    elif lovecleo == 4:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene5") alt "克莉奥快速旅行"
    elif lovecleo == 5:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("worldmap1") alt "克莉奥快速旅行"
    elif lovecleo == 6:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene7") alt "克莉奥快速旅行"
    elif lovecleo == 7:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene8") alt "克莉奥快速旅行"
    elif lovecleo == 8 and loveluce < 7:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleob4luce") alt "克莉奥快速旅行"
    elif lovecleo == 8 and loveluce >= 7:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene9") alt "克莉奥快速旅行"
    elif lovecleo == 9:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene10") alt "克莉奥快速旅行"
    elif lovecleo == 10:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene11") alt "克莉奥快速旅行"
#0.9.5
    elif lovecleo == 11 and cleoroom == 1:
            imagebutton:
                xalign 0.0
                yalign 0.9
                idle "images/icon/cleoicon1.png"
                hover "images/icon/cleoicon.png"
                focus_mask True
                action Jump("cleoroom1") alt "克莉奥快速旅行"
    elif lovecleo == 11 and cleoroom == 2:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene12_1") alt "克莉奥快速旅行"
    elif lovecleo == 12:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene13_1") alt "克莉奥快速旅行"
    elif loverhea < 9 or lovepris < 16 or lovemag < 23 or loveluce < 14:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene14_no") alt "克莉奥快速旅行"
    elif lovecleo == 13:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene14_yes") alt "克莉奥快速旅行"
    elif lovecleo == 14:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleoscene15_1") alt "克莉奥快速旅行"
    elif lovecleo == 15 and cleo_grat == 1:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo16_a") alt "克莉奥快速旅行"
    elif lovecleo == 15 and cleo_grat == 0:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo16_b") alt "克莉奥快速旅行"
    elif lovecleo == 16 and cleo_grat == 0:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo17_b") alt "克莉奥快速旅行"
    elif lovecleo == 16 and cleo_grat == 1:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo17_a") alt "克莉奥快速旅行"
    elif lovecleo == 17 and cleo_grat == 0:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo18_b") alt "克莉奥快速旅行"
    elif lovecleo == 18:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo19_1") alt "克莉奥快速旅行"
    elif lovecleo == 19:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo20_1") alt "克莉奥快速旅行"
    elif lovecleo == 20:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo21_1") alt "克莉奥快速旅行"
    elif lovecleo == 21:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo22_1") alt "克莉奥快速旅行"
    elif lovecleo == 22:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo23_1") alt "克莉奥快速旅行"
    elif lovecleo == 23:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("cleo24_1") alt "克莉奥快速旅行"
    elif lovecleo == 24 and servants >= 35:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("theadmiral1_1") alt "克莉奥快速旅行"
    elif servants >= 16 and lovemarion >= 22 and glimmering == 0:
        imagebutton:
            xalign 0.0
            yalign 0.9
            idle "images/icon/cleoicon1.png"
            hover "images/icon/cleoicon.png"
            focus_mask True
            action Jump("glimmering1_1") alt "克莉奥快速旅行"
#RHEA
    if loverhea == 0:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rheascene1") alt "蕾娅快速旅行"
    elif loverhea == 1:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rheascene2") alt "蕾娅快速旅行"
    elif loverhea == 2:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rheascene3") alt "蕾娅快速旅行"
    elif loverhea == 3:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea4_1") alt "蕾娅快速旅行"
        #AFFECTION ROUTE
    elif loverhea == 4 and joyhelps >= 1:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea5_1b") alt "蕾娅快速旅行"
    elif loverhea == 5 and joyhelps >= 1:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea6_1b") alt "蕾娅快速旅行"
    elif loverhea == 6 and joyhelps >= 1:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea7_1b") alt "蕾娅快速旅行"
    elif loverhea == 7 and joyhelps >= 1:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea8_1b") alt "蕾娅快速旅行"
    elif loverhea == 8:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea9_1") alt "蕾娅快速旅行"
    elif loverhea == 9 and joyhelps >= 1:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea10_1b") alt "蕾娅快速旅行"
    elif loverhea == 10 and joyhelps >= 1:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea11_1b") alt "蕾娅快速旅行"

        #MANIPULATION ROUTE
    elif loverhea == 4 and joyhelps == 0:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea5_1a") alt "蕾娅快速旅行"
    elif loverhea == 5 and joyhelps == 0:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea6_1a") alt "蕾娅快速旅行"
    elif loverhea == 6 and joyhelps == 0:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea7_1a") alt "蕾娅快速旅行"
    elif loverhea == 7 and joyhelps == 0:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea8_1a") alt "蕾娅快速旅行"
    elif loverhea == 9 and joyhelps == 0:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea10_1a") alt "蕾娅快速旅行"
    elif loverhea == 10 and joyhelps == 0:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea11_1a") alt "蕾娅快速旅行"
            #END OF MANIPULATION ROUTE FLAGS
    elif loverhea == 11:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea13_1") alt "蕾娅快速旅行"
    elif loverhea == 12:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea15_1") alt "蕾娅快速旅行"
    elif loverhea == 13:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("dungeon_intro") alt "蕾娅快速旅行"
    #FAST TRAVEL TO ACCOUNT FOR SERVANT LOGIC
    elif loverhea == 14 and servants >= 13:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea15_x_1") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 0:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("servants2") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 1:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("servants3") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 3:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("isha_scene1") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 4:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("servants5_nymph") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 5:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("nymph0_1") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 6:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("seejosiex1") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 7:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("ezras1_1") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 8:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("ezras2_1") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 9:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("servantsx") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 10:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("ezra5_1") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 11:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("josie1_1") alt "蕾娅快速旅行"
    elif loverhea == 14 and servants == 12:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("servants13_1") alt "蕾娅快速旅行"
    #FAST TRAVEL TO ACCOUNT FOR SERVANT LOGIC
    elif loverhea == 15:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea16_1") alt "蕾娅快速旅行"
    elif loverhea == 16:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea17_1") alt "蕾娅快速旅行"
    elif loverhea == 17:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea18_1") alt "蕾娅快速旅行"
    elif loverhea == 18:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea19_1") alt "蕾娅快速旅行"
    elif loverhea == 19:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea20_1") alt "蕾娅快速旅行"
    elif loverhea == 20:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea21_1") alt "蕾娅快速旅行"
    elif loverhea == 21:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea22_1") alt "蕾娅快速旅行"
    elif loverhea == 22:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea23_1") alt "蕾娅快速旅行"
    elif loverhea == 23:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea24_1") alt "蕾娅快速旅行"
    elif loverhea == 24:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea25_1") alt "蕾娅快速旅行"
    elif loverhea == 25:
        imagebutton:
            xalign 0.25
            yalign 0.9
            idle "images/icon/rheaicon1.png"
            hover "images/icon/rheaicon.png"
            focus_mask True
            action Jump("rhea26_1") alt "蕾娅快速旅行"
#MAGNA
    if lovemag == 0:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene1") alt "玛格娜快速旅行"
    elif lovemag == 1:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene2") alt "玛格娜快速旅行"
    elif lovemag == 2:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene3") alt "玛格娜快速旅行"
    elif lovemag == 3 and magroom == 1:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magroom1x") alt "玛格娜快速旅行"
    elif lovemag == 3 and magroom == 2:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene4") alt "玛格娜快速旅行"
    elif lovemag == 3 and magroom == 10:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene4") alt "玛格娜快速旅行"
    elif lovemag == 4:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene5") alt "玛格娜快速旅行"
    elif lovemag == 5:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("mag6prompt") alt "玛格娜快速旅行"
    elif lovemag == 6:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene7") alt "玛格娜快速旅行"
    elif lovemag == 7 and servants < 3:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magNoCity") alt "玛格娜快速旅行"
    elif lovemag == 7 and servants >= 3:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene8") alt "玛格娜快速旅行"
    elif lovemag == 8:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene9") alt "玛格娜快速旅行"
    #0.8.0
    elif lovemag == 9:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene10_1") alt "玛格娜快速旅行"
    elif lovemag == 10:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene11_1") alt "玛格娜快速旅行"
    elif lovemag == 11:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene12_1") alt "玛格娜快速旅行"
    elif lovemag == 12:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene13_1") alt "玛格娜快速旅行"
    elif lovemag == 13:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene14_0") alt "玛格娜快速旅行"
    elif lovemag == 14:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene14_1") alt "玛格娜快速旅行"
    elif lovemag == 15:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene15_1") alt "玛格娜快速旅行"
    elif lovemag == 16:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene16") alt "玛格娜快速旅行"
    elif lovemag == 17:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene17") alt "玛格娜快速旅行"
    elif lovemag == 18:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("wilford_prefight") alt "玛格娜快速旅行"
    elif lovemag == 19:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("gladix_prefight") alt "玛格娜快速旅行"
    elif lovemag == 20:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("magscene18") alt "玛格娜快速旅行"
    elif lovemag == 21:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("stacia_aftermath") alt "玛格娜快速旅行"
    elif lovemag == 22:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("mag_aftermath") alt "玛格娜快速旅行"
    elif lovemag == 23 and servants >= 35:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("thehammerfells1_1") alt "玛格娜快速旅行"
    elif lovemag == 24:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("thehammerfells2_1") alt "玛格娜快速旅行"
    elif lovemag == 25:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("thehammerfells3_1") alt "玛格娜快速旅行"
    elif loverhea >= 24 and lovemag >= 21 and magdate == 0:
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle "images/icon/magnaicon1.png"
            hover "images/icon/magnaicon.png"
            focus_mask True
            action Jump("city_map1") alt "玛格娜快速旅行"
#PRISCILLA
    if lovepris == 0:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene0") alt "普里西拉快速旅行"
    elif lovepris == 1:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene1") alt "普里西拉快速旅行"
    elif lovepris == 2 and prispotion == 0:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisroom0x") alt "普里西拉快速旅行"
    elif lovepris == 2 and prispotion == 1 and metjosie == 1:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("seejosiex") alt "普里西拉快速旅行"
    elif lovepris == 2 and prispotion == 1 and metjosie == 0:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("servants2") alt "普里西拉快速旅行"
    elif lovepris == 2 and prispotion == 2:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisroom1x") alt "普里西拉快速旅行"
    elif lovepris == 3:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene2") alt "普里西拉快速旅行"
    elif lovepris == 4:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisroom2x") alt "普里西拉快速旅行"
    elif lovepris == 5:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene6") alt "普里西拉快速旅行"
    elif lovepris == 6 and servants >= 3:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene7") alt "普里西拉快速旅行"
    elif lovepris == 6 and servants <= 2:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris_nocity") alt "普里西拉快速旅行"
    elif lovepris == 7:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene8") alt "普里西拉快速旅行"
    elif lovepris == 8:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene9") alt "普里西拉快速旅行"
    elif lovepris == 9:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene10") alt "普里西拉快速旅行"
    elif lovepris == 11:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene12") alt "普里西拉快速旅行"
    elif lovepris == 12:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene13") alt "普里西拉快速旅行"
    elif lovepris == 13:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene14_1") alt "普里西拉快速旅行"
    elif lovepris == 14:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("prisscene15_readycheck") alt "普里西拉快速旅行"
    elif lovepris == 15 and pris_grat == 0:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pclone16_1") alt "普里西拉快速旅行"
    elif lovepris == 15 and pris_grat == 1:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris16_1") alt "普里西拉快速旅行"
    elif lovepris == 16 and pris_grat == 0:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pclone16_1") alt "普里西拉快速旅行"
    elif lovepris == 16 and pris_grat == 1:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris16_1") alt "普里西拉快速旅行"
    elif lovepris == 17 and pris_grat == 0:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pclone17_1") alt "普里西拉快速旅行"
    elif lovepris == 17 and pris_grat == 1:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris17_1") alt "普里西拉快速旅行"
    elif lovepris == 18 and pris_grat == 0:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pclone18_1") alt "普里西拉快速旅行"
    elif lovepris == 18 and pris_grat == 1:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris18_1") alt "普里西拉快速旅行"
    elif lovepris == 19 and pris_grat == 0:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("fredrika0_1") alt "普里西拉快速旅行"
    elif lovepris == 19 and pris_grat == 1:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris19_1") alt "普里西拉快速旅行"
    elif lovepris == 20:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris20_1") alt "普里西拉快速旅行"
    elif lovepris == 21:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris21_1") alt "普里西拉快速旅行"
    elif lovepris == 22:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris22_1") alt "普里西拉快速旅行"
    elif lovepris == 23:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris23_1") alt "普里西拉快速旅行"
    elif lovepris == 24:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris24_1") alt "普里西拉快速旅行"
    elif lovepris == 25 and lovefea >= 4: 
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris25_1") alt "普里西拉快速旅行"
    elif lovepris == 26:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris26_1") alt "普里西拉快速旅行"
    elif lovepris == 27:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris27_1") alt "普里西拉快速旅行"
    elif lovepris == 28:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris28_1") alt "普里西拉快速旅行"
    elif lovepris == 29:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris29_1") alt "普里西拉快速旅行"
    elif lovepris == 30:
        imagebutton:
            xalign 0.75
            yalign 0.9
            idle "images/icon/prisicon1.png"
            hover "images/icon/prisicon.png"
            focus_mask True
            action Jump("pris30_1") alt "普里西拉快速旅行"
#LUCE
    if loveluce == 0:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lucescene1") alt "露丝快速旅行"
    elif loveluce == 1:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lucescene2") alt "露丝快速旅行"
    elif loveluce == 2:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lucescene3") alt "露丝快速旅行"
    elif lucewrong == True and loveluce == 2:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lucetryagain") alt "露丝快速旅行"
    elif loveluce == 3:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lucescene4") alt "露丝快速旅行"
    elif loveluce == 4:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lucescene5") alt "露丝快速旅行"
    elif loveluce == 5:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lucescene6") alt "露丝快速旅行"
    #The scene below is the partyscene
    elif loveluce == 6:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lucescene7") alt "露丝快速旅行"
    elif loveluce == 7 and luneparty1 == 1:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lucetolune") alt "露丝快速旅行"
    #luneparty1 = 0 means we did not go after Lunette
    elif loveluce >= 7 and loveluce <= 9 and luneparty1 == 0:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("luceroomx") alt "露丝快速旅行"
    elif loveluce == 10:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("violetscene1_1") alt "露丝快速旅行"
    elif loveluce == 11:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("violetscene2_1") alt "露丝快速旅行"
    elif loveluce == 12:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("violetscene3_1") alt "露丝快速旅行"
    elif loveluce == 13:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("violetscene4_1") alt "露丝快速旅行"
    elif loveluce == 14:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lun_intro_0") alt "露丝快速旅行"
    elif loveluce == 15:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lune_room0") alt "露丝快速旅行"
    elif loveluce == 16:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lun_intro_1") alt "露丝快速旅行"
    elif loveluce == 17:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lun_rhea_1") alt "露丝快速旅行"
    elif loveluce == 18:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("lun_mag_1") alt "露丝快速旅行"
    elif loveluce == 19:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("violetscene5_0") alt "露丝快速旅行"
        #violetscene5_0
    elif loveluce == 20:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("violetscene5_1") alt "露丝快速旅行"
    elif loveluce == 21:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("violetscene6_1") alt "露丝快速旅行"
    elif loveluce == 22:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("joana1_1") alt "露丝快速旅行"
    elif loveluce == 23:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("joana2_1") alt "露丝快速旅行"
    elif loveluce == 24:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("joana3_1") alt "露丝快速旅行"
    elif loveluce == 25:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("joana4_1") alt "露丝快速旅行"
    elif loveluce == 26 and servants >= 35:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("joana4plus_1") alt "露丝快速旅行"
    elif loveluce == 27:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("joana5_1") alt "露丝快速旅行"
    elif loveluce == 28:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("joana6_1") alt "露丝快速旅行"
    elif loveluce == 29:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("joana7_1") alt "露丝快速旅行"
    elif loveluce == 30:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("joana8_1") alt "露丝快速旅行"
    elif loveluce == 31:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("thegracen1_1") alt "露丝快速旅行"
    elif servants >= 16 and lovemarion >= 22 and glimmering == 0:
        imagebutton:
            xalign 1.0
            yalign 0.9
            idle "images/icon/luceicon1.png"
            hover "images/icon/luceicon.png"
            focus_mask True
            action Jump("glimmering1_1") alt "露丝快速旅行"
#LEONA
    if lovecleo >= 14 and servants >= 13 and checkpoint1 == 0:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leo1_1") alt "莱奥娜快速旅行"
    elif loveleo == 1:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leo2_1") alt "莱奥娜快速旅行"
    elif loveleo == 2:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leo3_1") alt "莱奥娜快速旅行"
    elif loveleo == 3:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leo4_1") alt "莱奥娜快速旅行"
    elif loveleo == 4:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leo5_1") alt "莱奥娜快速旅行"
    elif loveleo == 5:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leo6_1") alt "莱奥娜快速旅行"
    elif loveleo == 6 and truearj == 1:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leo7_arjenta_1") alt "莱奥娜快速旅行"
    elif loveleo == 6 and trueleo == 1:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leo7_leona_1") alt "莱奥娜快速旅行"
    elif loveleo == 7 and servants >= 16 and lovejuna >= 21:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona8_1") alt "莱奥娜快速旅行"
    elif servants == 13:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("josie9_1") alt "莱奥娜快速旅行"
    elif servants == 14 and loverhea >= 25:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("josie10_1") alt "莱奥娜快速旅行"
    elif servants == 15:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("servants16_1") alt "莱奥娜快速旅行"    
    elif loveleo == 8:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona9_1") alt "莱奥娜快速旅行"
    elif loveleo == 9:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona10_1") alt "莱奥娜快速旅行"
    elif loveleo == 10:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona11_1") alt "莱奥娜快速旅行"
    elif loveleo == 11:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona12_1") alt "莱奥娜快速旅行"
    elif loveleo == 12:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona13_1") alt "莱奥娜快速旅行"
    elif loveleo == 13:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona14_1") alt "莱奥娜快速旅行"
    elif loveleo == 14:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona15_1") alt "莱奥娜快速旅行"
    elif loveleo == 15:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona16_1") alt "莱奥娜快速旅行"
    elif loveleo == 16:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona17_1") alt "莱奥娜快速旅行"
    elif loveleo == 17 and elder_sword <= 9:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("scarlet1_1") alt "莱奥娜快速旅行"
    elif loveleo == 17 and elder_sword == 10:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("scarlet2_1") alt "莱奥娜快速旅行"
    elif loveleo == 17 and elder_sword == 11:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("scarlet3_1") alt "莱奥娜快速旅行"
    elif loveleo == 17 and elder_sword == 12:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("scarlet4_1") alt "莱奥娜快速旅行"
    #BEFORE THIS ONE we have scarlet
    elif loveleo == 17:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona18_1") alt "莱奥娜快速旅行"
    elif loveleo == 18:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona19_1") alt "莱奥娜快速旅行"
    elif loveleo == 19:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona20_1") alt "莱奥娜快速旅行"
    elif loveleo == 20:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona21_1") alt "莱奥娜快速旅行"
    elif loveleo == 21:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona22_1") alt "莱奥娜快速旅行"
    elif loveleo == 22:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona24_1") alt "莱奥娜快速旅行"
    elif loveleo == 23:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona23_1") alt "莱奥娜快速旅行"
    elif loveleo == 24:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona25_1") alt "莱奥娜快速旅行"
    elif loveleo == 25:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona26_1") alt "莱奥娜快速旅行"
    elif loveleo == 26:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona27_1") alt "莱奥娜快速旅行"
    elif loveleo == 27:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona28_1") alt "莱奥娜快速旅行"
    elif loveleo == 28:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle "images/icon/leoicon1.png"
            hover "images/icon/leoicon.png"
            focus_mask True
            action Jump("leona29_1") alt "莱奥娜快速旅行"
#EZRA
    if loveezra == 1:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/ezraicon1.png"
            hover "images/icon/ezraicon.png"
            focus_mask True
            action Jump("ezra8_1") alt "埃兹拉快速旅行"
    elif loveezra == 2:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/ezraicon1.png"
            hover "images/icon/ezraicon.png"
            focus_mask True
            action Jump("ezra9_1") alt "埃兹拉快速旅行"
    elif loveezra == 3:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/ezraicon1.png"
            hover "images/icon/ezraicon.png"
            focus_mask True
            action Jump("ezra10_1") alt "埃兹拉快速旅行"
    elif loveezra == 4:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/ezraicon1.png"
            hover "images/icon/ezraicon.png"
            focus_mask True
            action Jump("ezra11_1") alt "埃兹拉快速旅行"
    elif loveezra == 5:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/ezraicon1.png"
            hover "images/icon/ezraicon.png"
            focus_mask True
            action Jump("ezra12_1") alt "埃兹拉快速旅行"
    elif loveezra == 6 and ezra_morph == 1:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/ezraicon1.png"
            hover "images/icon/ezraicon.png"
            focus_mask True
            action Jump("ezra13_1") alt "埃兹拉快速旅行"
#MARIONS
    if lovemarion == 0 and servants >= 16:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion1_1") alt "玛丽昂姐妹快速旅行" 
    elif lovemarion == 1:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion2_1") alt "玛丽昂姐妹快速旅行" 
    elif lovemarion == 2:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion3_1") alt "玛丽昂姐妹快速旅行" 
    elif lovemarion == 3:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion4_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 4:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("mina_brief_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 5:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion5_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 6:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion6_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 7:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion7_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 8:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion8_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 9:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion9_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 10:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion10_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 11:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion11_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 12:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion12_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 13:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion13_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 14:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion14_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 15:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion15_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 16:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion16_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 17:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion17_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 18 and lovenatxtal == 0:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("natxtal1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 18 and lovenatxtal == 1:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("natxtal2") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 18 and lovenatxtal == 2:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("ftaliya") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 18 and lovenatxtal >= 3 and lovenatxtal <= 4:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("natxtal_2") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 18 and lovenatxtal == 5:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("natxtal_4") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 18 and lovenatxtal >= 6:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion18_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 19:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion19_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 20:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion20_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 21:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion21_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 22:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion22_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 23:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion23_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 24:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion24_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 25:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion25_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 26:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion26_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 27:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion27_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 28:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion28_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 29:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion29_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 30:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion30_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 31:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion31_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 32:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion32_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 33:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion33_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 34:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion34_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 35:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion35_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 36:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion36_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 37:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion37_1") alt "玛丽昂姐妹快速旅行"
    elif lovemarion == 38:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle "images/icon/marionicon1.png"
            hover "images/icon/marionicon.png"
            focus_mask True
            action Jump("marion38_1") alt "玛丽昂姐妹快速旅行"

#JUNA
    if lovejuna == 0 and servants >= 16 and lovemarion >= 23:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna1_1") alt "茱娜快速旅行"
    elif lovejuna == 1:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna2_1") alt "茱娜快速旅行"
    elif lovejuna == 2:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna3_1") alt "茱娜快速旅行"
    elif lovejuna == 3:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna4_1") alt "茱娜快速旅行"
    elif lovejuna == 4:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna5_1") alt "茱娜快速旅行"
    elif lovejuna == 5:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna6_1") alt "茱娜快速旅行"
    elif lovejuna == 6:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna7_1") alt "茱娜快速旅行"
    elif lovejuna == 7:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna8_1") alt "茱娜快速旅行"
    elif lovejuna == 8:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna9_1") alt "茱娜快速旅行"
    elif lovejuna == 9:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna10_1") alt "茱娜快速旅行"
    elif lovejuna == 10:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna11_1") alt "茱娜快速旅行"
    elif lovejuna == 11:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna12_1") alt "茱娜快速旅行"
    elif lovejuna == 12:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna13_1") alt "茱娜快速旅行"
    elif lovejuna == 13:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna14_1") alt "茱娜快速旅行"
    elif lovejuna == 14:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna15_1") alt "茱娜快速旅行"
    elif lovejuna == 15:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna16_1") alt "茱娜快速旅行"
    elif lovejuna == 16:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna17_1") alt "茱娜快速旅行"
    elif lovejuna == 17:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna18_1") alt "茱娜快速旅行"
    elif lovejuna == 18:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna19_1") alt "茱娜快速旅行"
    elif lovejuna == 19:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna20_1") alt "茱娜快速旅行"
    elif lovejuna == 20:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna21_1") alt "茱娜快速旅行"
    elif lovejuna == 21:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna22_1") alt "茱娜快速旅行"
    elif lovejuna == 23 and servants == 20:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna23_1") alt "茱娜快速旅行"
    elif servants == 19 and lovepris >= 30 and loveluce >= 25 and lovemag >= 22 and loverhea >= 26 and loveleo >= 29 and lovemarion >= 39 and lovefea >= 24 and lovecleo >= 23:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("servants19_1") alt "茱娜快速旅行"
    elif servants == 20:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("grove1_1") alt "茱娜快速旅行"
    elif servants == 21:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("grove2_1") alt "茱娜快速旅行"
    elif servants == 22:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("josie11_1") alt "茱娜快速旅行"
    elif servants == 23:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("josie12_1") alt "茱娜快速旅行"
    elif servants == 24:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("thepast1_1") alt "茱娜快速旅行"
    elif lovejuna == 24 and servants == 25:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("juna24_1") alt "茱娜快速旅行"
    elif servants == 35:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("theinvasion11_1") alt "茱娜快速旅行"
    elif servants == 36:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("theinvasion12_1") alt "茱娜快速旅行"
    elif servants == 37:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("theinvasion13_1") alt "茱娜快速旅行"
    elif servants == 38:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("theinvasion14_1") alt "茱娜快速旅行"
    elif servants == 39:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("theinvasion15_1") alt "茱娜快速旅行"
    elif servants == 40 and loveluce >= 31 and lovemag >= 26 and lovecleo >= 25:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("theprep1_1") alt "茱娜快速旅行"
    elif servants == 41:
        imagebutton:
            xalign 1.0
            yalign 0.7
            idle "images/icon/junaicon1.png"
            hover "images/icon/junaicon.png"
            focus_mask True
            action Jump("theprep2_1") alt "茱娜快速旅行"
#FEATANA
    if lovefea == 0 and servants >= 12:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea1_1") alt "菲塔娜快速旅行"
    elif lovefea == 1 and servants >= 16:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea2_1") alt "菲塔娜快速旅行"
    elif lovefea == 2 and servants >= 17:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea3_1") alt "菲塔娜快速旅行"
    elif lovefea == 3:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea4_1") alt "菲塔娜快速旅行"
    elif lovefea == 4:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea5_1") alt "菲塔娜快速旅行"
    elif lovefea == 5:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea6_1") alt "菲塔娜快速旅行"
    elif lovefea == 6:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea7_1") alt "菲塔娜快速旅行"
    elif lovefea == 7:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea8_1") alt "菲塔娜快速旅行"
    elif lovefea == 8:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea9_1") alt "菲塔娜快速旅行"
    elif lovefea == 9:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea10_1") alt "菲塔娜快速旅行"
    elif lovefea == 10:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea11_1") alt "菲塔娜快速旅行"
    elif lovefea == 11:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea12_1") alt "菲塔娜快速旅行"
    elif lovefea == 12:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea13_1") alt "菲塔娜快速旅行"
    elif lovefea == 13:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea14_1") alt "菲塔娜快速旅行"
    elif lovefea == 14:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea15_1") alt "菲塔娜快速旅行"
    elif lovefea == 15:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea16_1") alt "菲塔娜快速旅行"
    elif lovefea == 16:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea17_1") alt "菲塔娜快速旅行"
    elif lovefea == 17:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea18_1") alt "菲塔娜快速旅行"
    elif lovefea == 18:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea19_1") alt "菲塔娜快速旅行"
    elif lovefea == 19:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea20_1") alt "菲塔娜快速旅行"
    elif lovefea == 20:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea21_1") alt "菲塔娜快速旅行"
    elif lovefea == 21:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea22_1") alt "菲塔娜快速旅行"
    elif lovefea == 22:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea23_1") alt "菲塔娜快速旅行"
    elif lovefea == 23:
        imagebutton:
            xalign 0.5
            yalign 0.7
            
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("fea24_1") alt "菲塔娜快速旅行"
    elif lovefea == 24 and servants == 20:
        imagebutton:
            xalign 0.5
            yalign 0.7
            idle "images/icon/feaicon1.png"
            hover "images/icon/feaicon.png"
            focus_mask True
            action Jump("grove1_1") alt "菲塔娜快速旅行"



#The area before the exit
screen exit1():
    imagemap:
        ground "images/map/exit1.webp"
        hotspot(758, 335, 119, 47) action Jump("mainend")
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "images/icon/xbutton0.png"
        hover "images/icon/xbutton.png"
        focus_mask True
        action Jump("mainend") alt "卧室"
    imagebutton:
        idle "images/map/leave_idle.webp"
        hover "images/map/leave_hover.webp"
        focus_mask True
        action Jump("worldmap1") alt "世界地图"
    if loveluce == 2:
        imagebutton:
            idle "images/map/farm_idle.webp"
            hover "images/map/farm_hover.webp"
            focus_mask True
            action Jump("lucescene3") alt "农场"
    elif loveluce == 0:
        imagebutton:
            xalign 1.0
            yalign 1.0
            idle "images/map/farm_idle.webp"
            hover "images/map/farm_hover.webp"
            focus_mask True
            action Jump("lucescene1") alt "农场"
    else:
        imagebutton:
            idle "images/map/farm_idle.webp"
            hover "images/map/farm_hover.webp"
            focus_mask True
            action Jump("farm1") alt "农场"
    imagebutton:
        idle "images/map/return_idle.webp"
        hover "images/map/return_hover.webp"
        focus_mask True
        action Jump("mainmap") alt "学院园区"
# The main academy campus
screen mainmap():
    imagemap:
        ground "images/map/map2.webp"
        hotspot(758, 335, 119, 47) action Jump("mainend")
    imagebutton:
        idle "images/map/acehall_idle.webp"
        hover "images/map/acehall_hover.webp"
        focus_mask True
        action Jump("acehall1") alt "学院走廊"
    if lovemag == 1:
        imagebutton:
            idle "images/map/barracks_idle.webp"
            hover "images/map/barracks_hover.webp"
            focus_mask True
            action Jump("barracks1") alt "兵营"
    elif lovemag == 0:
        imagebutton:
            idle "images/map/barracks_idle.webp"
            hover "images/map/barracks_hover.webp"
            focus_mask True
            action Jump("barracks1") alt "兵营"
    else:
        imagebutton:
            idle "images/map/barracks_idle.webp"
            hover "images/map/barracks_hover.webp"
            focus_mask True
            action Jump("barracks1") alt "兵营"
#Bathhouse
    if lovecleo == 0:
        imagebutton:
            idle "images/map/bath_idle.webp"
            hover "images/map/bath_hover.webp"
            focus_mask True
            action Jump("cleoscene1") alt "浴场"
    else:
        imagebutton:
            idle "images/map/bath_idle.webp"
            hover "images/map/bath_hover.webp"
            focus_mask True
            action Jump("bathhouse1") alt "浴场"
# Servant's quarters
    imagebutton:
        idle "images/map/juna_idle.webp"
        hover "images/map/juna_hover.webp"
        focus_mask True
        action Jump("servantsx") alt "仆从宿舍"
# Bedroom
    if loverhea == 4 and joypotion == 2 and joyhelps == 1:
        imagebutton:
            idle "images/map/room_idle.webp"
            hover "images/map/room_hover.webp"
            focus_mask True
            action Jump("rhea5_1b") alt "卧室"
    elif loverhea == 4 and joypotion == 2 and joyhelps == 0:
        imagebutton:
            idle "images/map/room_idle.webp"
            hover "images/map/room_hover.webp"
            focus_mask True
            action Jump("rhea5_1a") alt "卧室"
    else:
        imagebutton:
            idle "images/map/room_idle.webp"
            hover "images/map/room_hover.webp"
            focus_mask True
            action Jump("mainend") alt "卧室"
    if lovecleo == 10:
        imagebutton:
            idle "images/map/bridge_idle.webp"
            hover "images/map/bridge_hover.webp"
            focus_mask True
            action Jump("cleoscene11") alt "学院出口"
    else:
        imagebutton:
            idle "images/map/bridge_idle.webp"
            hover "images/map/bridge_hover.webp"
            focus_mask True
            action Jump("exit1") alt "学院出口"
#Icons
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "images/icon/xbutton0.png"
        hover "images/icon/xbutton.png"
        focus_mask True
        action Jump("mainend") alt "卧室"
    #WORLD MAP
    imagebutton:
        xalign 0.975
        yalign 0.125
        idle "images/icon/minimap.webp"
        hover "images/icon/minimap_hover.webp"
        focus_mask True
        action Jump("worldmap1") alt "世界地图"
# world map
screen worldmap1():
    imagemap:
        ground "images/map/worldmap1.webp"
        xalign 0.5
        hotspot(758, 335, 119, 47) action Jump("mainend")
    imagebutton:
        xalign 0.5
        idle "images/map/acemap_idle.webp"
        hover "images/map/acemap_hover.webp"
        focus_mask True
        action Jump("mainmap") alt "返回学院"
    imagebutton:
        xalign 0.5
        idle "images/map/compass_idle.webp"
        hover "images/map/compass_hover.webp"
        focus_mask True
        action Jump("compass1") alt "罗盘"
    imagebutton:
        xalign 0.5
        idle "images/map/vilmap_idle.webp"
        hover "images/map/vilmap_hover.webp"
        focus_mask True
        action Jump("village1") alt "村庄"
    imagebutton:
        xalign 0.5
        idle "images/map/marketmap_idle.webp"
        hover "images/map/marketmap_hover.webp"
        focus_mask True
        action Jump("market1") alt "市场"
    if lovejuna >= 6:
        imagebutton:
            xalign 0.5
            idle "images/map/father_fort_idle.webp"
            hover "images/map/father_fort_hover.webp"
            focus_mask True
            action Jump("fathers_fort") alt "废弃堡垒"
    if servants < 2 and lovecleo == 5:
        imagebutton:
            xalign 0.5
            idle "images/map/city_idle.webp"
            hover "images/map/city_hover.webp"
            focus_mask True
            action Jump("cleofix6_3") alt "城市"
    elif servants < 2 and lovecleo < 5:
        imagebutton:
            xalign 0.5
            idle "images/map/city_idle.webp"
            hover "images/map/city_hover.webp"
            focus_mask True
            action Jump("cleofix6_1") alt "城市"
    elif servants == 2 and lovecleo < 5:
        imagebutton:
            xalign 0.5
            idle "images/map/city_idle.webp"
            hover "images/map/city_hover.webp"
            focus_mask True
            action Jump("cleofix6_2") alt "城市"
    elif servants == 2 and lovecleo == 5:
        imagebutton:
            xalign 0.5
            idle "images/map/city_idle.webp"
            hover "images/map/city_hover.webp"
            focus_mask True
            action Jump("juna_cityvisit") alt "城市"
    elif city_open == True:
        imagebutton:
            xalign 0.5
            idle "images/map/city_idle.webp"
            hover "images/map/city_hover.webp"
            focus_mask True
            action Jump("city_map1") alt "城市"
screen vil6_map():
    imagemap:
        ground "images/mag/6/vil6_map.webp"
        hotspot(758, 335, 119, 47) action Jump("mainend")
    if mag6_vil == 0:
        imagebutton:
            idle "images/mag/6/vil6_idle.webp"
            hover "images/mag/6/vil6_hover.webp"
            focus_mask True
            action Jump("magscene6villlager1") alt "随机村民"
    elif mag6_vil == 1:
        imagebutton:
            idle "images/mag/6/vil6_idle.webp"
            hover "images/mag/6/vil6_hover.webp"
            focus_mask True
            action Jump("magscene6villlager2") alt "随机村民"
    else:
        imagebutton:
            idle "images/mag/6/vil6_idle.webp"
            hover "images/mag/6/vil6_hover.webp"
            focus_mask True
            action Jump("magscene6villlager3") alt "随机村民"
    if mag6_girls == 0:
        imagebutton:
            idle "images/mag/6/girls6_idle.webp"
            hover "images/mag/6/girls6_hover.webp"
            focus_mask True
            action Jump("magscene6girls1") alt "村中少女们"
    elif mag6_girls == 1:
        imagebutton:
            idle "images/mag/6/girls6_idle.webp"
            hover "images/mag/6/girls6_hover.webp"
            focus_mask True
            action Jump("magscene6girls2") alt "村中少女们"
    else:
        imagebutton:
            idle "images/mag/6/girls6_idle.webp"
            hover "images/mag/6/girls6_hover.webp"
            focus_mask True
            action Jump("magscene6girls3") alt "村中少女们"
    if mag6_ved == 0:
        imagebutton:
            idle "images/mag/6/ved6_idle.webp"
            hover "images/mag/6/ved6_hover.webp"
            focus_mask True
            action Jump("magscene6elder1") alt "村长"
    elif mag6_ved == 1:
        imagebutton:
            idle "images/mag/6/ved6_idle.webp"
            hover "images/mag/6/ved6_hover.webp"
            focus_mask True
            action Jump("magscene6elder2") alt "村长"
    else:
        imagebutton:
            idle "images/mag/6/ved6_idle.webp"
            hover "images/mag/6/ved6_hover.webp"
            focus_mask True
            action Jump("magscene6elder3") alt "村长"
    imagebutton:
        idle "images/mag/6/mag6_idle.webp"
        hover "images/mag/6/mag6_hover.webp"
        focus_mask True
        action Jump("magscene6mag")
screen innmap1():
    imagemap:
        ground "images/rhea/3/17.webp"
        hotspot(758, 335, 119, 47) action Jump("mainend")
    if rdoor1 == 0:
        imagebutton:
            idle "images/rhea/3/17e.webp"
            hover "images/rhea/3/17f.webp"
            focus_mask True
            action Jump("rhea3door1") alt "一号门"
    if rdoor2 == 0:
        imagebutton:
            idle "images/rhea/3/17c.webp"
            hover "images/rhea/3/17d.webp"
            focus_mask True
            action Jump("rhea3door2") alt "二号门"
    if rdoor3 == 0:
        imagebutton:
            idle "images/rhea/3/17g.webp"
            hover "images/rhea/3/17h.webp"
            focus_mask True
            action Jump("rhea3door3") alt "三号门"
    if inn1 == 0:
        imagebutton:
            idle "images/rhea/3/17a.webp"
            hover "images/rhea/3/17b.webp"
            focus_mask True
            action Jump("rhea3stall1") alt "客栈伙计"
    if inn1 == 1:
        imagebutton:
            idle "images/rhea/3/17a.webp"
            hover "images/rhea/3/17b.webp"
            focus_mask True
            action Jump("rhea3keepup") alt "客栈伙计"
#BROTHEL INTRO - After events with Magna
screen brothel_entrance():
    imagemap:
        ground "images/map/brothel/brothel_entrance.webp"
        xalign 0.5
        hotspot(758, 335, 119, 47) action Jump("mainend")
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "images/icon/xbutton0.png"
        hover "images/icon/xbutton.png"
        focus_mask True
        action Jump("city_map1") alt "返回城市"
    if lovemag >= 6 and brothel == 1:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/brothelmatron_idle.webp"
            hover "images/map/brothel/brothelmatron_hover.webp"
            focus_mask True
            action Jump("brothelaccess1") alt "与老板娘交谈"
    elif brothel == 2:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/brothelmatron_idle.webp"
            hover "images/map/brothel/brothelmatron_hover.webp"
            focus_mask True
            action Jump("brothelaccess2") alt "与老板娘交谈"
    elif brothel == 3:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/brothelmatron_idle.webp"
            hover "images/map/brothel/brothelmatron_hover.webp"
            focus_mask True
            action Jump("brothelaccess3") alt "与老板娘交谈"
    elif brothel == 4:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/brothelmatron_idle.webp"
            hover "images/map/brothel/brothelmatron_hover.webp"
            focus_mask True
            action Jump("brothelaccess4") alt "与老板娘交谈"
    elif brothel >= 5:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/brothelmatron_idle.webp"
            hover "images/map/brothel/brothelmatron_hover.webp"
            focus_mask True
            action Jump("brothelmatron1_1") alt "与老板娘交谈"
#BROTHEL HALL 1
screen brothel_hall1():
    imagemap:
        ground "images/map/brothel/brothel_halls1.webp"
        xalign 0.5
        hotspot(758, 335, 119, 47) action Jump("mainend")
    imagebutton:
        xalign 0.5
        idle "images/map/brothel/lab_brothel_halls1_idle.webp"
        hover "images/map/brothel/lab_brothel_halls1_hover.webp"
        focus_mask True
        action Jump("brothel_lab") alt "妓院实验室"
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "images/icon/xbutton0.png"
        hover "images/icon/xbutton.png"
        focus_mask True
        action Jump("brothelentrance") alt "返回入口"
    imagebutton:
        xalign 0.5
        idle "images/map/brothel/rooms_brothel_halls1_idle.webp"
        hover "images/map/brothel/rooms_brothel_halls1_hover.webp"
        focus_mask True
        action Jump("brothelscreen_rooms1") alt "探索房间"
    if cherry_bite == 8 and brothel >= 5:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/office_brothel_halls1_idle.webp"
            hover "images/map/brothel/office_brothel_halls1_hover.webp"
            focus_mask True
            action Jump("sash_bro2") alt "妓院办公室"
    else:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/office_brothel_halls1_idle.webp"
            hover "images/map/brothel/office_brothel_halls1_hover.webp"
            focus_mask True
            action Jump("brothel_office") alt "妓院办公室"

#BROTHEL HALL 2
screen brothel_hall2():
    imagemap:
        ground "images/map/brothel/brothel_halls2.webp"
        xalign 0.5
        hotspot(758, 335, 119, 47) action Jump("mainend")
    imagebutton:
        xalign 0.5
        idle "images/map/brothel/lab_brothel_halls2_idle.webp"
        hover "images/map/brothel/lab_brothel_halls2_hover.webp"
        focus_mask True
        action Jump("brothel_lab") alt "妓院实验室"
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "images/icon/xbutton0.png"
        hover "images/icon/xbutton.png"
        focus_mask True
        action Jump("brothelentrance") alt "返回入口"
    imagebutton:
        xalign 0.75
        yalign 0.0
        idle "images/icon/xbutton0.png"
        hover "images/icon/xbutton.png"
        focus_mask True
        action Jump("brothelentrance") alt "返回入口"
    imagebutton:
        xalign 0.5
        idle "images/map/brothel/rooms_brothel_halls2_idle.webp"
        hover "images/map/brothel/rooms_brothel_halls2_hover.webp"
        focus_mask True
        action Jump("brothelscreen_rooms1") alt "探索房间"
    if cherry_bite == 8 and brothel >= 5:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/office_brothel_halls2_idle.webp"
            hover "images/map/brothel/office_brothel_halls2_hover.webp"
            focus_mask True
            action Jump("sash_bro2") alt "妓院办公室"
    else:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/office_brothel_halls2_idle.webp"
            hover "images/map/brothel/office_brothel_halls2_hover.webp"
            focus_mask True
            action Jump("brothel_office") alt "妓院办公室"
    
    imagebutton:
        xalign 0.5
        idle "images/map/brothel/entrance_brothel_halls2_idle.webp"
        hover "images/map/brothel/entrance_brothel_halls2_hover.webp"
        focus_mask True
        action Jump("brothelentrance") alt "返回入口"
#BROTHEL rooms 1
screen brothel_rooms1():
    imagemap:
        ground "images/map/brothel/brothel_rooms1.webp"
        xalign 0.5
        hotspot(758, 335, 119, 47) action Jump("mainend")
    imagebutton:
        xalign 0.5
        idle "images/map/brothel/halls_brothel_rooms1_idle.webp"
        hover "images/map/brothel/halls_brothel_rooms1_hover.webp"
        focus_mask True
        action Jump("brothelscreen_hall2") alt "探索房间"
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "images/icon/xbutton0.png"
        hover "images/icon/xbutton.png"
        focus_mask True
        action Jump("brothelentrance") alt "返回入口"
    imagebutton:
        xalign 0.50
        yalign 0.0
        idle "images/icon/sun0.png"
        hover "images/icon/sun.png"
        focus_mask True
        action Jump("brothelreset_1") alt "结束今天并回到这里"
    #BASTET
    if bastetopen == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("brothelbastet_none") alt "芭斯特的房间"
    elif lovebastet == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("brothelbas1") alt "芭斯特的房间"
    elif lovebastet == 1:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("bastet2_1") alt "芭斯特的房间"
    elif lovebastet == 2:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("bastet3_1") alt "芭斯特的房间"
    elif lovebastet == 3:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("bastet_cn") alt "芭斯特的房间"
    elif lovebastet == 4:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("bastet_cn_x") alt "芭斯特的房间"
    elif lovebastet == 5:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("bastet_none") alt "芭斯特的房间"

    #INGNETTA
    if ingnopen == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("brothelingn_none") alt "英格内塔的房间"
    elif loveingn == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("brothelingn1") alt "英格内塔的房间"
    elif loveingn == 1:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("brothelingn2") alt "英格内塔的房间"
    elif loveingn == 2:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("brothelingn2_proposal") alt "英格内塔的房间"
    elif loveingn == 3:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("brothelingn3_1") alt "英格内塔的房间"
    elif loveingn == 4:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("brothelingn4_1") alt "英格内塔的房间"
    else:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("broingnx_director") alt "英格内塔的房间"
    #YUEL
    if yuelopen == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("brothelyuel_none") alt "尤尔的房间"
    elif loveyuel == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("brothelyuel1") alt "尤尔的房间"
    elif loveyuel == 1:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("broyuel2_1") alt "尤尔的房间"
    elif loveyuel == 2:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("broyuel3_1") alt "尤尔的房间"
    elif loveyuel == 3:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("broyuel4_1") alt "尤尔的房间"
    elif loveyuel == 4:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("broyuel5_1") alt "尤尔的房间"
    elif loveyuel == 5:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("broyuel6_1") alt "尤尔的房间"
    elif loveyuel == 6:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms1_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms1_hover.webp"
            focus_mask True
            action Jump("yuel_none") alt "尤尔的房间"
    #END ROOMS SET
#BROTHEL rooms 2
screen brothel_rooms2():
    imagemap:
        ground "images/map/brothel/brothel_rooms2.webp"
        xalign 0.5
        hotspot(758, 335, 119, 47) action NullAction()
    imagebutton:
        xalign 0.50
        yalign 0.0
        idle "images/icon/sun0.png"
        hover "images/icon/sun.png"
        focus_mask True
        action Jump("brothelreset_2") alt "结束今天并回到这里"
    imagebutton:
        xalign 0.5
        idle "images/map/brothel/halls_brothel_rooms2_idle.webp"
        hover "images/map/brothel/halls_brothel_rooms2_hover.webp"
        focus_mask True
        action Jump("brothelscreen_hall2") alt "探索房间"
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "images/icon/xbutton0.png"
        hover "images/icon/xbutton.png"
        focus_mask True
        action Jump("brothelentrance") alt "返回入口"
#BASTET
    if bastetopen == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("brothelbastet_none") alt "芭斯特的房间"
    elif lovebastet == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("brothelbas1") alt "芭斯特的房间"
    elif lovebastet == 1:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("bastet2_1") alt "芭斯特的房间"
    elif lovebastet == 2:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("bastet3_1") alt "芭斯特的房间"
    elif lovebastet == 3:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("bastet_cn") alt "芭斯特的房间"
    elif lovebastet == 4:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("bastet_cn_x") alt "芭斯特的房间"
    elif lovebastet == 5:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room1_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room1_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("bastet_none") alt "芭斯特的房间"
#INGN
    if ingnopen == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("brothelingn_none") alt "英格内塔的房间"
    elif loveingn == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("brothelingn1") alt "英格内塔的房间"
    elif loveingn == 1:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("brothelingn2") alt "英格内塔的房间"
    elif loveingn == 2:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("brothelingn2_proposal") alt "英格内塔的房间"
    elif loveingn == 3:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("brothelingn3_1") alt "英格内塔的房间"
    elif loveingn == 4:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("brothelingn4_1") alt "英格内塔的房间"
    else:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room2_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room2_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("broingnx_director") alt "英格内塔的房间"
#YUEL
    if yuelopen == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("brothelyuel_none") alt "尤尔的房间"
    elif loveyuel == 0:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("brothelyuel1") alt "尤尔的房间"
    elif loveyuel == 1:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("broyuel2_1") alt "尤尔的房间"
    elif loveyuel == 2:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("broyuel3_1") alt "尤尔的房间"
    elif loveyuel == 3:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("broyuel4_1") alt "尤尔的房间"
    elif loveyuel == 4:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("broyuel5_1") alt "尤尔的房间"
    elif loveyuel == 5:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("broyuel6_1") alt "尤尔的房间"
    elif loveyuel == 5:
        imagebutton:
            xalign 0.5
            idle "images/map/brothel/room3_brothel_rooms2_idle.webp"
            hover "images/map/brothel/room3_brothel_rooms2_hover.webp"
            focus_mask True
            action Jump("yuel_none") alt "尤尔的房间"

#p15 Village
screen p15_village():
    imagemap:
        ground "images/pris/15/village/p15_village.webp"
        xalign 0.5
        hotspot(758, 335, 119, 47) action NullAction()
    #SLEEP
    imagebutton:
        xalign 0.5
        idle "images/pris/15/village/p15_village_sleep_idle.webp"
        hover "images/pris/15/village/p15_village_sleep_hover.webp"
        focus_mask True
        action Jump("prisscene15_sleep0") alt "上床休息"
    #GUARD
    imagebutton:
        xalign 0.5
        idle "images/pris/15/village/p15_village_guard_idle.webp"
        hover "images/pris/15/village/p15_village_guard_hover.webp"
        focus_mask True
        action Jump("prisscene15_guard") alt "与女守卫交谈"
    #WOMAN
    if pris_15_woman == 0:
        imagebutton:
            xalign 0.5
            idle "images/pris/15/village/p15_village_woman_idle.webp"
            hover "images/pris/15/village/p15_village_woman_hover.webp"
            focus_mask True
            action Jump("prisscene15_woman") alt "与村中女子交谈"
    #GOSSIP
    if pris_15_gossip == 0:
        imagebutton:
            xalign 0.5
            idle "images/pris/15/village/p15_village_gossip_idle.webp"
            hover "images/pris/15/village/p15_village_gossip_hover.webp"
            focus_mask True
            action Jump("prisscene15_gossip1") alt "听听八卦"
    elif pris_15_gossip == 1:
        imagebutton:
            xalign 0.5
            idle "images/pris/15/village/p15_village_gossip_idle.webp"
            hover "images/pris/15/village/p15_village_gossip_hover.webp"
            focus_mask True
            action Jump("prisscene15_gossip2") alt "听听八卦"
    elif pris_15_gossip == 2:
        imagebutton:
            xalign 0.5
            idle "images/pris/15/village/p15_village_gossip_idle.webp"
            hover "images/pris/15/village/p15_village_gossip_hover.webp"
            focus_mask True
            action Jump("prisscene15_gossip3") alt "听听八卦"
screen relation_up():
    vbox:
        text "好感上升！" size 20 xalign 0.2 yalign 0.1
screen relation_down():
    vbox:
        text "好感下降……" size 20 xalign 0.2 yalign 0.1