transform rot_text: # the simple transform
    rotate 180
    xzoom -1
transform custom_fade_in: # https://lemmasoft.renai.us/forums/viewtopic.php?t=32626
    alpha 0
    linear 0.5 alpha 1
label after_load:
    # Capture Player Name
    $ persistent.player_name = player_name
    $ persistent.player_lastname = player_lastname

    return
##############tips/warnings
screen Prologue_open():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}序章{/color}{/size}{/font}"
screen tobecontinued():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}未完待续{/color}{/size}{/font}"
screen warning():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}警告{/color}{/size}{/font}"
screen june_10_1015():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月10日 星期三 上午10:15{/color}{/size}{/font}"
screen june_10_520():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午5:20{/color}{/size}{/font}"
screen june_10_610():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:10{/color}{/size}{/font}"
screen june_13_905():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月13日 星期五 上午9:05{/color}{/size}{/font}"
screen june_13_135():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午1:35{/color}{/size}{/font}"
screen june_13_615():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:15{/color}{/size}{/font}"
screen june_14_815():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月14日 星期六 下午8:15{/color}{/size}{/font}"
screen june_16_812():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月16日 星期一 上午8:12{/color}{/size}{/font}"
screen june_16_525():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午5:25{/color}{/size}{/font}"
screen june_17_823():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月17日 星期二 上午8:23{/color}{/size}{/font}"
screen june_17_915():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:15{/color}{/size}{/font}"
screen june_17_1142():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:42{/color}{/size}{/font}"
screen chapter01():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第1章{/color}{/size}{/font}"
screen june_18_715():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月18日 星期三 上午7:15{/color}{/size}{/font}"
screen june_18_645():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:45{/color}{/size}{/font}"
screen june_18_1042():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午10:42{/color}{/size}{/font}"
screen june_18_1043():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午10:43{/color}{/size}{/font}"
screen june_19_708():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月19日 星期四 上午7:08{/color}{/size}{/font}"
screen chapter02():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第2章{/color}{/size}{/font}"
screen june_20_701():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月20日 星期五 上午7:01{/color}{/size}{/font}"
screen june_20_823():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午8:23{/color}{/size}{/font}"
screen june_20_1135():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:35{/color}{/size}{/font}"
screen june_20_635():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:35{/color}{/size}{/font}"
screen june_21_737():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月21日 星期六 上午7:37{/color}{/size}{/font}"
screen june_21_632():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:32{/color}{/size}{/font}"
screen june_21_1112():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午11:12{/color}{/size}{/font}"
screen chapter03():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第3章{/color}{/size}{/font}"
screen june_22_728():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月22日 星期日 上午7:28{/color}{/size}{/font}"
screen june_22_1121():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:21{/color}{/size}{/font}"
screen june_22_203():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:03{/color}{/size}{/font}"
screen june_22_548():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午5:48{/color}{/size}{/font}"
screen june_22_822():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:22{/color}{/size}{/font}"
screen june_23_822():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月23日 星期一 上午8:22{/color}{/size}{/font}"
screen june_23_713():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:13{/color}{/size}{/font}"
screen june_24_848():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月24日 星期二 上午8:48{/color}{/size}{/font}"
screen chapter04():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第4章{/color}{/size}{/font}"
screen june_24_1020():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午10:20{/color}{/size}{/font}"
screen june_24_204():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:04{/color}{/size}{/font}"
screen june_24_532():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午5:32{/color}{/size}{/font}"
screen june_24_748():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:48{/color}{/size}{/font}"
screen june_25_814():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月25日 星期三 上午8:14{/color}{/size}{/font}"
screen june_25_120():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午1:20{/color}{/size}{/font}"
screen june_25_631():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:31{/color}{/size}{/font}"
screen june_26_903():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月26日 星期四 上午9:03{/color}{/size}{/font}"
screen june_26_1232():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午12:32{/color}{/size}{/font}"
screen june_26_756():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:56{/color}{/size}{/font}"
screen june_26_1123():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午11:23{/color}{/size}{/font}"
screen june_27_1011():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月27日 星期五 上午10:11{/color}{/size}{/font}"
screen chapter05():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第5章{/color}{/size}{/font}"
screen june_27_142():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午1:42{/color}{/size}{/font}"
screen june_27_304():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午3:04{/color}{/size}{/font}"
screen june_27_719():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:19{/color}{/size}{/font}"
screen june_28_734():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月28日 星期六 上午7:34{/color}{/size}{/font}"
screen june_29_824():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月29日 星期日 上午8:24{/color}{/size}{/font}"
screen june_29_936():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:36{/color}{/size}{/font}"
screen chapter06():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第6章{/color}{/size}{/font}"
screen june_29_348():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午3:48{/color}{/size}{/font}"
screen june_29_812():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:12{/color}{/size}{/font}"
screen june_30_818():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}6月30日 星期一 上午8:18{/color}{/size}{/font}"
screen june_30_143():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午1:43{/color}{/size}{/font}"
screen june_30_836():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:36{/color}{/size}{/font}"
screen july_1_904():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月1日 星期二 上午9:04{/color}{/size}{/font}"
screen july_2_738():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月2日 星期三 上午7:38{/color}{/size}{/font}"
screen chapter07():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第7章{/color}{/size}{/font}"
screen july_2_1020():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午10:20{/color}{/size}{/font}"
screen july_2_1118():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:18{/color}{/size}{/font}"
screen july_3_815():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月3日 星期四 上午8:15{/color}{/size}{/font}"
screen july_4_828():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月4日 星期五 上午8:28{/color}{/size}{/font}"
screen july_4_623():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:23{/color}{/size}{/font}"
screen july_4_842():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:42{/color}{/size}{/font}"
screen july_5_729():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月5日 星期六 上午7:29{/color}{/size}{/font}"
screen chapter08():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第8章{/color}{/size}{/font}"
screen july_5_640():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:40{/color}{/size}{/font}"
screen july_5_919():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午9:19{/color}{/size}{/font}"
screen july_6_832():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月6日 星期日 上午8:32{/color}{/size}{/font}"
screen july_6_812():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:12{/color}{/size}{/font}"
screen july_7_845():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月7日 星期一 上午8:45{/color}{/size}{/font}"
screen july_7_1004():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午10:04{/color}{/size}{/font}"
screen nightmare1():
    vbox:
        xalign 0.1 ypos 800
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}3r4mThgIn{/color}{/size}{/font}" at rot_text
screen july_8_736():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月8日 星期二 上午7:36{/color}{/size}{/font}"
screen chapter09():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第9章{/color}{/size}{/font}"
screen july_8_1213():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午12:13{/color}{/size}{/font}"
screen july_8_835():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:35{/color}{/size}{/font}"
screen july_9_612():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月9日 星期三 上午6:12{/color}{/size}{/font}"
screen july_9_826():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月9日 星期三 上午8:26{/color}{/size}{/font}"
screen july_9_213():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:13{/color}{/size}{/font}"
screen july_9_642():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:42{/color}{/size}{/font}"
screen july_9_827():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:27{/color}{/size}{/font}"
screen chapter10():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第10章{/color}{/size}{/font}"
screen july_10_705():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月10日 星期四 上午7:05{/color}{/size}{/font}"
screen july_10_508():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午5:08{/color}{/size}{/font}"
screen july_10_814():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:14{/color}{/size}{/font}"
screen july_10_942():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午9:42{/color}{/size}{/font}"
screen july_11_732():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月11日 星期五 上午7:32{/color}{/size}{/font}"
screen july_11_917():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:17{/color}{/size}{/font}"
screen july_11_802():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:02{/color}{/size}{/font}"
screen chapter11():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第11章{/color}{/size}{/font}"
screen july_12_741():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月12日 星期六 上午7:41{/color}{/size}{/font}"
screen july_12_918():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:18{/color}{/size}{/font}"
screen july_12_130():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午1:30{/color}{/size}{/font}"
screen july_12_245():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:45{/color}{/size}{/font}"
screen july_12_436():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午4:36{/color}{/size}{/font}"
screen july_12_842():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:42{/color}{/size}{/font}"
screen july_13_812():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月13日 星期日 上午8:12{/color}{/size}{/font}"
screen july_13_948():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:48{/color}{/size}{/font}"
screen nightmare2():
    vbox:
        xalign 0.1 ypos 800
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}3clff0 34+{/color}{/size}{/font}" at rot_text
screen july_14_826():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月14日 星期一 上午8:26{/color}{/size}{/font}"
screen chapter12():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第12章{/color}{/size}{/font}"
screen july_14_1118():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:18{/color}{/size}{/font}"
screen july_14_255():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:55{/color}{/size}{/font}"
screen unknown():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}？？？{/color}{/size}{/font}"
screen july_15_712():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月15日 星期二 上午7:12{/color}{/size}{/font}"
screen july_15_822():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午8:22{/color}{/size}{/font}"
screen july_15_902():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:02{/color}{/size}{/font}"
screen july_15_604():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:04{/color}{/size}{/font}"
screen july_15_814():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:14{/color}{/size}{/font}"
screen july_16_624():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月16日 星期三 上午6:24{/color}{/size}{/font}"
screen chapter13():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第13章{/color}{/size}{/font}"
screen july_16_930():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:30{/color}{/size}{/font}"
screen july_16_1020():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午10:20{/color}{/size}{/font}"
screen july_16_1126():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:26{/color}{/size}{/font}"
screen july_16_1248():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午12:48{/color}{/size}{/font}"
screen july_16_136():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午1:36{/color}{/size}{/font}"
screen july_16_408():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午4:08{/color}{/size}{/font}"
screen july_16_824():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:24{/color}{/size}{/font}"
screen july_17_714():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月17日 星期四 上午7:14{/color}{/size}{/font}"
screen chapter14():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第14章{/color}{/size}{/font}"
screen july_18_724():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月18日 星期五 上午7:24{/color}{/size}{/font}"
screen july_18_1012():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午10:12{/color}{/size}{/font}"
screen july_18_241():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:41{/color}{/size}{/font}"
screen july_18_523():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午5:23{/color}{/size}{/font}"
screen july_18_945():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午9:45{/color}{/size}{/font}"
screen july_19_104():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月19日 星期六 上午1:04{/color}{/size}{/font}"
screen july_19_514():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午5:14{/color}{/size}{/font}"
screen july_19_822():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午8:22{/color}{/size}{/font}"
screen july_19_908():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:08{/color}{/size}{/font}"
screen nightmare3():
    vbox:
        xalign 0.1 ypos 750
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}4om3 ag@ln{/color}{/size}{/font}" at rot_text
screen chapter15():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第15章{/color}{/size}{/font}"
screen july_19_446():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午4:46{/color}{/size}{/font}"
screen july_19_912():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午9:12{/color}{/size}{/font}"
screen july_20_322():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月20日 星期日 上午3:22{/color}{/size}{/font}"
screen july_20_908():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:08{/color}{/size}{/font}"
screen july_20_1117():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:17{/color}{/size}{/font}"
screen july_20_210():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:10{/color}{/size}{/font}"
screen july_20_403():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午4:03{/color}{/size}{/font}"
screen july_20_921():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午9:21{/color}{/size}{/font}"
screen july_21_752():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月21日 星期一 上午7:52{/color}{/size}{/font}"
screen july_21_710():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:10{/color}{/size}{/font}"
screen july_21_1120():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午11:20{/color}{/size}{/font}"
screen july_22_106():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月22日 星期二 上午1:06{/color}{/size}{/font}"
screen chapter16():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第16章{/color}{/size}{/font}"
screen july_22_756():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午7:56{/color}{/size}{/font}"
screen july_22_842():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午8:42{/color}{/size}{/font}"
screen july_22_1108():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:08{/color}{/size}{/font}"
screen july_22_904():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午9:04{/color}{/size}{/font}"
screen july_23_512():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月23日 星期二 上午5:12{/color}{/size}{/font}"
screen july_23_824():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午8:24{/color}{/size}{/font}"
screen july_23_142():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午1:42{/color}{/size}{/font}"
screen july_23_358():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午3:58{/color}{/size}{/font}"
screen july_23_548():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午5:48{/color}{/size}{/font}"
screen july_23_812():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:12{/color}{/size}{/font}"
screen chapter17():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第17章{/color}{/size}{/font}"
screen july_24_828():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月24日 星期三 上午8:28{/color}{/size}{/font}"
screen july_24_109():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午1:09{/color}{/size}{/font}"
screen july_24_612():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午6:12{/color}{/size}{/font}"
screen july_24_840():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:40{/color}{/size}{/font}"
screen july_24_840():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:40{/color}{/size}{/font}"
screen july_25_812():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月25日 星期四 上午8:12{/color}{/size}{/font}"
screen july_25_1117():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:17{/color}{/size}{/font}"
screen july_25_910():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午9:10{/color}{/size}{/font}"
screen july_26_847():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月26日 星期五 上午8:47{/color}{/size}{/font}"
screen july_26_746():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:46{/color}{/size}{/font}"
screen july_27_801():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月27日 星期六 上午8:01{/color}{/size}{/font}"
screen chapter18():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第18章{/color}{/size}{/font}"
screen july_27_1054():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午10:54{/color}{/size}{/font}"
screen july_27_1033():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午10:33{/color}{/size}{/font}"
screen july_26_247():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月27日 星期六 上午2:47{/color}{/size}{/font}"
screen july_26_712():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午7:12{/color}{/size}{/font}"
screen july_26_836():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午8:36{/color}{/size}{/font}"
screen july_26_1120():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:20{/color}{/size}{/font}"
screen july_26_1226():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午12:26{/color}{/size}{/font}"
screen july_26_512():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午5:12{/color}{/size}{/font}"
screen july_28_247():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月28日 星期日 上午7:47{/color}{/size}{/font}"
screen july_28_944():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:44{/color}{/size}{/font}"
screen july_28_1106():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:06{/color}{/size}{/font}"
screen july_29_703():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月29日 星期一 上午7:03{/color}{/size}{/font}"
screen chapter19():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第19章{/color}{/size}{/font}"
screen july_29_1108():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:08{/color}{/size}{/font}"
screen july_29_235():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:35{/color}{/size}{/font}"
screen july_29_347():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午3:47{/color}{/size}{/font}"
screen july_29_512():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午5:12{/color}{/size}{/font}"
screen july_29_734():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:34{/color}{/size}{/font}"
screen july_29_1023():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午9:34{/color}{/size}{/font}"
screen july_30_609():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月30日 星期二 上午6:09{/color}{/size}{/font}"
screen july_30_823():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午8:23{/color}{/size}{/font}"
screen july_30_916():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:16{/color}{/size}{/font}"
screen july_30_723():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:23{/color}{/size}{/font}"
screen july_31_310():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}7月31日 星期三 上午3:10{/color}{/size}{/font}"
screen july_31_822():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午8:22{/color}{/size}{/font}"
screen july_31_706():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:06{/color}{/size}{/font}"
screen chapter20():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第20章{/color}{/size}{/font}"
screen august_1_814():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}8月1日 星期四 上午8:14{/color}{/size}{/font}"
screen august_1_1032():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午10:32{/color}{/size}{/font}"
screen august_1_1226():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午12:26{/color}{/size}{/font}"
screen august_1_208():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:08{/color}{/size}{/font}"
screen august_1_352():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午3:52{/color}{/size}{/font}"
screen august_1_718():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:18{/color}{/size}{/font}"
screen august_1_922():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午9:22{/color}{/size}{/font}"
screen august_2_808():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}8月2日 星期五 上午8:08{/color}{/size}{/font}"
screen august_2_137():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午1:37{/color}{/size}{/font}"
screen august_2_822():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:22{/color}{/size}{/font}"
screen august_3_131():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}8月3日 星期六 上午1:31{/color}{/size}{/font}"
screen august_3_157h():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午1:57{/color}{/size}{/font}"
screen august_3_157():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午1:57{/color}{/size}{/font}"
screen august_3_743():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午7:43{/color}{/size}{/font}"
screen august_3_902():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:02{/color}{/size}{/font}"
screen chapter21():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第21章{/color}{/size}{/font}"
screen august_3_1208():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午12:08{/color}{/size}{/font}"
screen august_3_206():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:06{/color}{/size}{/font}"
screen august_3_433():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午4:33{/color}{/size}{/font}"
screen august_3_742():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:42{/color}{/size}{/font}"
screen august_4_145():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}8月4日 星期日 上午1:45{/color}{/size}{/font}"
screen august_4_452():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午4:52{/color}{/size}{/font}"
screen august_4_806():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午8:06{/color}{/size}{/font}"
screen august_4_214():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:14{/color}{/size}{/font}"
screen august_4_734():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:34{/color}{/size}{/font}"
screen august_4_nightmare():
    vbox:
        xalign 0.1 ypos 800
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午12:18{/color}{/size}{/font}" at rot_text
screen august_5_214():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}8月5日 星期一 上午2:14{/color}{/size}{/font}"
screen august_5_745():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午7:45{/color}{/size}{/font}"
screen august_5_1022():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午10:22{/color}{/size}{/font}"
screen august_5_1213():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午12:13{/color}{/size}{/font}"
screen august_5_857():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:57{/color}{/size}{/font}"
screen elsewhere():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}别处{/color}{/size}{/font}"
screen chapter22():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}第22章{/color}{/size}{/font}"
screen august_6_718():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}8月6日 星期二 上午7:18{/color}{/size}{/font}"
screen august_6_942():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午9:42{/color}{/size}{/font}"
screen august_6_1122():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午11:22{/color}{/size}{/font}"
screen august_6_145():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午1:45{/color}{/size}{/font}"
screen august_6_302():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午3:02{/color}{/size}{/font}"
screen august_6_506():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午5:06{/color}{/size}{/font}"
screen august_6_815():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午8:15{/color}{/size}{/font}"
screen august_7_755():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}8月7日 星期三 上午7:55{/color}{/size}{/font}"
screen august_7_1012():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}上午10:12{/color}{/size}{/font}"
screen august_7_215():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午2:15{/color}{/size}{/font}"
screen august_7_718():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}下午7:18{/color}{/size}{/font}"
screen august_8_845():
    vbox:
        xalign 0.1 ypos 900
        text "{font=fonts/msyh.ttc}{size=+60}{color=#FFFFFF}8月8日 星期四 上午8:45{/color}{/size}{/font}"

##############achiements
screen achievement_chapter1():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter1_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}无偿加班{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter2():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter2_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}三人行{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter3():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter3_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}内部调岗{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter4():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter4_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}高层的风景{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter5():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter5_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}校园探访{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter6():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter6_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}四人同行{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter7():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter7_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}破碎的女人{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter8():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter8_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}迷路的小女孩{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter9():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter9_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}我见过那个女巫{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter10():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter10_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}秘密与恐怖{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter11():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter11_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}初来乍到{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter12():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter12_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}关于伊芙{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter13():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter13_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}全员到齐{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter14():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter14_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}样板间{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter15():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter15_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}糟糕的邻居{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter16():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter16_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}内心地狱{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter17():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter17_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}长住{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter18():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter18_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}火力全开{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter19():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter19_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}闹鬼{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter20():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter20_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}我们需要这场雨{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter21():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter21_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}病假{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_chapter22():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_chapter22_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}血肉横飞{/color}{/font}" xpos 425 ypos -270 xalign 0.5

screen achievement_laura_firstime():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_laurafirsttime_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}办公室恋情{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_kallie_firstime():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_kalliefirsttime_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}安静的女孩{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_shelley_firstime():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_shelleyfirsttime_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}狂野精灵女孩{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_eve_firstime():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_evefirsttime_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}泼辣女人{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_allfour_firstime():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_allfirsttime_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}四条同花{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_firstlove():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_firstlove_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}坠入爱河{/color}{/font}" xpos 425 ypos -270 xalign 0.5
screen achievement_threesome():
    vbox:
        xalign -0.15 ypos 100
        image "/gui/gallery/achievement_swatch.webp"
        image "/gui/gallery/ach_threesom_hover.webp" xpos 275 ypos -275
        vbox:
            xsize 355
            text "{font=fonts/msyh.ttc}{color=#323232}三P{/color}{/font}" xpos 425 ypos -270 xalign 0.5

###############
############camera change
screen ChangeCamera_s_ch8():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch8_s == "shelley_ch8_sex2":
                action ToggleVariable("current_movie_ch8_s","shelley_ch8_sex3")
            else:
                action ToggleVariable("current_movie_ch8_s","shelley_ch8_sex2")
screen ChangeCamera_l_ch9():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch9_l == "laura_ch9_fuck":
                action ToggleVariable("current_movie_ch9_l","laura_ch9_fuck2")
            else:
                action ToggleVariable("current_movie_ch9_l","laura_ch9_fuck")
screen ChangeCamera_s_ch9():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch9_s == "shelley_ch9_fuck2":
                action ToggleVariable("current_movie_ch9_s","shelley_ch9_fuck3")
            else:
                action ToggleVariable("current_movie_ch9_s","shelley_ch9_fuck2")
screen ChangeCamera_l_ch10():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch10_l == "laura_ch10_fuck4":
                action ToggleVariable("current_movie_ch10_l","laura_ch10_fuck5")
            else:
                action ToggleVariable("current_movie_ch10_l","laura_ch10_fuck4")
screen ChangeCamera_k_ch11():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch11_k == "kallie_ch11_fuck2":
                action ToggleVariable("current_movie_ch11_k","kallie_ch11_fuck3")
            else:
                action ToggleVariable("current_movie_ch11_k","kallie_ch11_fuck2")
screen ChangeCamera_k_ch12():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch12_k == "kallie_ch12_oral":
                action ToggleVariable("current_movie_ch12_k","kallie_ch12_oral2")
            else:
                action ToggleVariable("current_movie_ch12_k","kallie_ch12_oral")
screen ChangeCamera_k_ch13():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch13_k == "kallie_ch13_69":
                action ToggleVariable("current_movie_ch13_k","kallie_ch13_69_2")
            else:
                action ToggleVariable("current_movie_ch13_k","kallie_ch13_69")
screen ChangeCamera_s_ch14():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch14_s == "shelley_ch14_fuck4":
                action ToggleVariable("current_movie_ch14_s","shelley_ch14_fuck5")
            else:
                action ToggleVariable("current_movie_ch14_s","shelley_ch14_fuck4")
screen ChangeCamera_s_ch15():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch15_s == "shelley_ch15_fuck3":
                action ToggleVariable("current_movie_ch15_s","shelley_ch15_fuck4")
            else:
                action ToggleVariable("current_movie_ch15_s","shelley_ch15_fuck3")
screen ChangeCamera_l_ch17():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch17_l == "laura_ch17_anal5":
                action ToggleVariable("current_movie_ch17_l","laura_ch17_anal6")
            else:
                action ToggleVariable("current_movie_ch17_l","laura_ch17_anal5")
screen ChangeCamera_e_ch22():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch22_e == "eve_ch22_fuck":
                action ToggleVariable("current_movie_ch22_e","eve_ch22_fuck2")
            else:
                action ToggleVariable("current_movie_ch22_e","eve_ch22_fuck")
screen ChangeCamera_k_ch22():
    vbox:
        xpos 0.925
        ypos 0.025
        xsize 120
        ysize 120
        imagebutton:
            #focus_mask True
            idle "gui/camerachange_idle.webp"
            hover "gui/camerachange_hover.webp"
            if current_movie_ch22_k == "kallie_ch22_fuck2":
                action ToggleVariable("current_movie_ch22_k","kallie_ch22_fuck3")
            else:
                action ToggleVariable("current_movie_ch22_k","kallie_ch22_fuck2")
##################
screen gamepoints():
    if s_met == "yes" and e_met == "yes":
        add "gui/stats_menu_background3.webp"
    elif s_met == "yes" and e_met == "no":
        add "gui/stats_menu_background2.webp"
    else:
        add "gui/stats_menu_background.webp"
    imagebutton auto "gui/return_%s.webp" xalign 0.5 ypos 1000 action Return()
    hbox:
        xsize 368
        xpos 489
        ypos 343
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[k_trust]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[k_desire]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[k_love]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[k_friend]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[k_anxiety]{/color}" xalign 0.5
    hbox:
        xsize 368
        xpos 1144
        ypos 343
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[l_trust]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[l_desire]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[l_love]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[l_friend]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[l_anxiety]{/color}" xalign 0.5
    #if s_met == "yes":
    hbox:
        xsize 368
        xpos 489
        ypos 702
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[s_trust]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[s_desire]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[s_love]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[s_friend]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[s_anxiety]{/color}" xalign 0.5
    #if e_met == "yes":
    hbox:
        xsize 368
        xpos 1144
        ypos 702
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[e_trust]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[e_desire]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[e_love]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[e_friend]{/color}" xalign 0.5
        vbox:
            xsize 76
            textbutton "{color=#ffffff}[e_anxiety]{/color}" xalign 0.5
screen achievements():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("成就")):
        style_prefix "gui_text"
        hbox:
            if renpy.variant("phone"):
                xpos -500
            else:
                pass
            ypos -25
            textbutton _("{size=40}回放画廊  {/size}") action ShowMenu("gallery")
            textbutton _("{size=40}成就  {/size}") action ShowMenu("achievements")
        viewport:
            xmaximum 1405
            ymaximum 850
            xfill True
            yfill True
            mousewheel True
            scrollbars "vertical"
            if renpy.variant("phone"):
                xpos -500
                xsize 1800
            else:
                xpos -20
            ypos 25
            vbox:
                style_prefix "gallery"
                #xsize 2000
                #row one
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch1_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter1_hover.webp"
                                    idle "gui/gallery/ach_chapter1_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter1", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch1_complete:
                                textbutton "{color=#ffffff}{size=40}Unpaid Overtime{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 1{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch2_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter2_hover.webp"
                                    idle "gui/gallery/ach_chapter2_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter2", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch2_complete:
                                textbutton "{color=#ffffff}{size=40}Three's Company{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 2{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"

        #row two
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch3_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter3_hover.webp"
                                    idle "gui/gallery/ach_chapter3_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter3", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch3_complete:
                                textbutton "{color=#ffffff}{size=40}Inter-office Transfer{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 3{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch4_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter4_hover.webp"
                                    idle "gui/gallery/ach_chapter4_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter4", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch4_complete:
                                textbutton "{color=#ffffff}{size=40}A View From the \nTop Floor{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 4{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row three
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch5_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter5_hover.webp"
                                    idle "gui/gallery/ach_chapter5_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter5", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch5_complete:
                                textbutton "{color=#ffffff}{size=40}Campus Visit{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 5{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch6_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter6_hover.webp"
                                    idle "gui/gallery/ach_chapter6_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter6", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch6_complete:
                                textbutton "{color=#ffffff}{size=40}Four's Company{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 6{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row four
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch7_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter7_hover.webp"
                                    idle "gui/gallery/ach_chapter7_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter7", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch7_complete:
                                textbutton "{color=#ffffff}{size=40}A Broken Woman{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 7{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch8_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter8_hover.webp"
                                    idle "gui/gallery/ach_chapter8_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter8", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch8_complete:
                                textbutton "{color=#ffffff}{size=40}Lost Little Girl{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 8{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row five
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch9_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter9_hover.webp"
                                    idle "gui/gallery/ach_chapter9_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter9", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch9_complete:
                                textbutton "{color=#ffffff}{size=40}I've Seen The Witch{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 9{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch10_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter10_hover.webp"
                                    idle "gui/gallery/ach_chapter10_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter10", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch10_complete:
                                textbutton "{color=#ffffff}{size=40}Secrets and Horrors{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 10{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row five
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch11_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter11_hover.webp"
                                    idle "gui/gallery/ach_chapter11_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter11", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch11_complete:
                                textbutton "{color=#ffffff}{size=40}New to the Block{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 11{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #col 2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch12_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter12_hover.webp"
                                    idle "gui/gallery/ach_chapter12_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter12", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch12_complete:
                                textbutton "{color=#ffffff}{size=40}About Eve{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 12{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row seven
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch13_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter13_hover.webp"
                                    idle "gui/gallery/ach_chapter13_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter13", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch13_complete:
                                textbutton "{color=#ffffff}{size=40}Full Crew{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 13{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch14_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter14_hover.webp"
                                    idle "gui/gallery/ach_chapter14_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter14", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch14_complete:
                                textbutton "{color=#ffffff}{size=40}Show Home{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 14{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row eight
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch15_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter15_hover.webp"
                                    idle "gui/gallery/ach_chapter15_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter15", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch15_complete:
                                textbutton "{color=#ffffff}{size=40}Bad Neighbors{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 15{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch16_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter16_hover.webp"
                                    idle "gui/gallery/ach_chapter16_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter16", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch16_complete:
                                textbutton "{color=#ffffff}{size=40}Hell Inside{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 16{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row nine
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch17_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter17_hover.webp"
                                    idle "gui/gallery/ach_chapter17_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter17", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch17_complete:
                                textbutton "{color=#ffffff}{size=40}Extended Stay{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 17{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch18_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter18_hover.webp"
                                    idle "gui/gallery/ach_chapter18_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter18", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch18_complete:
                                textbutton "{color=#ffffff}{size=40}Fire Good{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 18{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row tena
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch19_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter19_hover.webp"
                                    idle "gui/gallery/ach_chapter19_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter19", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch19_complete:
                                textbutton "{color=#ffffff}{size=40}Haunted{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 19{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch20_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter20_hover.webp"
                                    idle "gui/gallery/ach_chapter20_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter20", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch20_complete:
                                textbutton "{color=#ffffff}{size=40}We Needed This Rain{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 20{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row thirteen
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch21_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter21_hover.webp"
                                    idle "gui/gallery/ach_chapter21_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter21", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch21_complete:
                                textbutton "{color=#ffffff}{size=40}Sick Leave{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 21{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.ch22_complete:
                                imagebutton:
                                    hover "gui/gallery/ach_chapter22_hover.webp"
                                    idle "gui/gallery/ach_chapter22_idle.webp"
                                    xsize 340
                                    action Replay("ach_chapter22", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.ch22_complete:
                                textbutton "{color=#ffffff}{size=40}Flesh and Gore{/size}{/color} \n {color=#000000}{size=30}Finish Chapter 22{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row ten
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.laura_firstime:
                                imagebutton:
                                    hover "gui/gallery/ach_laurafirsttime_hover.webp"
                                    idle "gui/gallery/ach_laurafirsttime_idle.webp"
                                    xsize 340
                                    action Replay("ach_laura_firsttime", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.laura_firstime:
                                textbutton "{color=#ffffff}{size=40}Office Romance{/size}{/color} \n {color=#000000}{size=30}Have Sex with Laura for \nthe First Time{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.kallie_firstime:
                                imagebutton:
                                    hover "gui/gallery/ach_kalliefirsttime_hover.webp"
                                    idle "gui/gallery/ach_kalliefirsttime_idle.webp"
                                    xsize 340
                                    action Replay("ach_kallie_firsttime", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.kallie_firstime:
                                textbutton "{color=#ffffff}{size=40}A Quiet Girl{/size}{/color} \n {color=#000000}{size=30}Have Sex with Kallie for \nthe First Time{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row 11
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.shelley_firstime:
                                imagebutton:
                                    hover "gui/gallery/ach_shelleyfirsttime_hover.webp"
                                    idle "gui/gallery/ach_shelleyfirsttime_idle.webp"
                                    xsize 340
                                    action Replay("ach_shelley_firsttime", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.shelley_firstime:
                                textbutton "{color=#ffffff}{size=40}Manic Pixie Girl{/size}{/color} \n {color=#000000}{size=30}Have Sex with Shelley for \nthe First Time{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.eve_firstime:
                                imagebutton:
                                    hover "gui/gallery/ach_evefirsttime_hover.webp"
                                    idle "gui/gallery/ach_evefirsttime_idle.webp"
                                    xsize 340
                                    action Replay("ach_eve_firsttime", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.eve_firstime:
                                textbutton "{color=#ffffff}{size=40}Hard-ass Woman{/size}{/color} \n {color=#000000}{size=30}Have Sex with Eve for \nthe First Time{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row 12
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.all_firstime:
                                imagebutton:
                                    hover "gui/gallery/ach_allfirsttime_hover.webp"
                                    idle "gui/gallery/ach_allfirsttime_idle.webp"
                                    xsize 340
                                    action Replay("ach_allfour_firsttime", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.all_firstime:
                                textbutton "{color=#ffffff}{size=40}Four of a Kind{/size}{/color} \n {color=#000000}{size=30}Have Sex with All Four \nLove Interests{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.all_firstlove:
                                imagebutton:
                                    hover "gui/gallery/ach_firstlove_hover.webp"
                                    idle "gui/gallery/ach_firstlove_idle.webp"
                                    xsize 340
                                    action Replay("ach_firstlove", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.all_firstlove:
                                textbutton "{color=#ffffff}{size=40}In Love{/size}{/color} \n {color=#000000}{size=30}Have a Love Interest Confess{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        #row thirteen
                hbox:
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            if persistent.threesome:
                                imagebutton:
                                    hover "gui/gallery/ach_threesom_hover.webp"
                                    idle "gui/gallery/ach_threesom_idle.webp"
                                    xsize 340
                                    action Replay("ach_threesome", locked=False)
                            else:
                                imagebutton:
                                    idle "gui/gallery/gallery_locked.webp"
                            if persistent.threesome:
                                textbutton "{color=#ffffff}{size=40}MFF{/size}{/color} \n {color=#000000}{size=30}Enjoy Time With Two Love \n Interests at the Same Time{/size}{/color}"
                            else:
                                pass
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
        ######col2
                    vbox:
                        image "/gui/gallery/box_left.webp"
                    vbox:
                        image "/gui/gallery/box_top.webp"
                        hbox:
                            imagebutton:
                                idle "gui/gallery/gallery_empty.webp"
                                xsize 340
                        hbox:
                            image "/gui/gallery/box_bottom.webp"
                    vbox:
                        image "/gui/gallery/box_right.webp"
#######
#                    vbox:
#                        image "/gui/gallery/box_left.webp"
#                    vbox:
#                        image "/gui/gallery/box_top.webp"
#                        hbox:
#                            imagebutton:
#                                idle "gui/gallery/gallery_empty.webp"
#                                xsize 340
#                        hbox:
#                            image "/gui/gallery/box_bottom.webp"
#                    vbox:
#                        image "/gui/gallery/box_right.webp"
        #row five
#                    vbox:
#                        image "/gui/gallery/box_left.webp"
#                    vbox:
#                        image "/gui/gallery/box_top.webp"
#                        hbox:
#                            imagebutton:
#                                idle "gui/gallery/gallery_locked.webp"
#                                xsize 340
#                        hbox:
#                            image "/gui/gallery/box_bottom.webp"
#                    vbox:
#                        image "/gui/gallery/box_right.webp"

        ######col2
#                    vbox:
#                        image "/gui/gallery/box_left.webp"
#                    vbox:
#                        image "/gui/gallery/box_top.webp"
#                        hbox:
#                            imagebutton:
#                                idle "gui/gallery/gallery_locked.webp"
#                                xsize 340
#                        hbox:
#                            image "/gui/gallery/box_bottom.webp"
#                    vbox:
#                        image "/gui/gallery/box_right.webp"
screen gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("回放画廊")):
        style_prefix "gui_text"
        hbox:
            if renpy.variant("small"):
                xpos -500
            else:
                pass
            ypos -25
            textbutton _("{size=40}回放画廊  {/size}") action ShowMenu("gallery")
            textbutton _("{size=40}成就  {/size}") action ShowMenu("achievements")

        viewport:
            xmaximum 1405
            ymaximum 850
            xfill True
            yfill True
            mousewheel True
            scrollbars "vertical"
            if renpy.variant("phone"):
                xpos -500
                xsize 1800
            else:
                xpos -20
            ypos 25
            vbox:
                style_prefix "gallery"
                #xsize 2000
                #row one
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch3_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_001_hover.webp"
                                idle "gui/gallery/laura_001_idle.webp"
                                xsize 311
                                action Replay("ch3_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch3_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: More than Coworkers{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row1col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch4_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_002_hover.webp"
                                idle "gui/gallery/laura_002_idle.webp"
                                xsize 311
                                action Replay("ch4_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch4_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: A Time of Need{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row1col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch5_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_003_hover.webp"
                                idle "gui/gallery/laura_003_idle.webp"
                                xsize 311
                                action Replay("ch5_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch5_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Romantic-like Activities{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row1col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch6_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_004_hover.webp"
                                idle "gui/gallery/laura_004_idle.webp"
                                xsize 311
                                action Replay("ch6_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch6_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: A Lot Drunk{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row2col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch6_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_001_hover.webp"
                                idle "gui/gallery/kallie_001_idle.webp"
                                xsize 311
                                action Replay("ch6_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch6_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: My Own Decision{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row2col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch7_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_002_hover.webp"
                                idle "gui/gallery/kallie_002_idle.webp"
                                xsize 311
                                action Replay("ch7_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch7_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Awkward But Cute{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row2col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch7_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_001_hover.webp"
                                idle "gui/gallery/shelley_001_idle.webp"
                                xsize 311
                                action Replay("ch7_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch7_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Horny Since Spring{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row2col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch8_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_002_hover.webp"
                                idle "gui/gallery/shelley_002_idle.webp"
                                xsize 311
                                action Replay("ch8_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch8_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Fool Around{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row3col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch8_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_003_hover.webp"
                                idle "gui/gallery/kallie_003_idle.webp"
                                xsize 311
                                action Replay("ch8_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch8_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: A Rainy Night{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row2col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch9_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_005_hover.webp"
                                idle "gui/gallery/laura_005_idle.webp"
                                xsize 311
                                action Replay("ch9_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch9_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Feeling Normal-ish{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row2col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch9_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_003_hover.webp"
                                idle "gui/gallery/shelley_003_idle.webp"
                                xsize 311
                                action Replay("ch9_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch9_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Bathroom Break{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row3col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch10_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_004_hover.webp"
                                idle "gui/gallery/kallie_004_idle.webp"
                                xsize 311
                                action Replay("ch10_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch10_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Bibliophile{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row4col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch10_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_006_hover.webp"
                                idle "gui/gallery/laura_006_idle.webp"
                                xsize 311
                                action Replay("ch10_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch10_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Gym Performance{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row4col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch11_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_004_hover.webp"
                                idle "gui/gallery/shelley_004_idle.webp"
                                xsize 311
                                action Replay("ch11_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch11_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Make Love To Me{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row4col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch11_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_005_hover.webp"
                                idle "gui/gallery/kallie_005_idle.webp"
                                xsize 311
                                action Replay("ch11_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch11_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Come to Bed{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row4col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch12_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_007_hover.webp"
                                idle "gui/gallery/laura_007_idle.webp"
                                xsize 311
                                action Replay("ch12_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch12_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Make-Up Sex{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row5col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch12_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_005_hover.webp"
                                idle "gui/gallery/shelley_005_idle.webp"
                                xsize 311
                                action Replay("ch12_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch12_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Get You Back to Sleep{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row5col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch12_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_006_hover.webp"
                                idle "gui/gallery/kallie_006_idle.webp"
                                xsize 311
                                action Replay("ch12_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch12_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Laundry Time{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row5col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch13_eve_sex:
                            imagebutton:
                                hover "gui/gallery/eve_001_hover.webp"
                                idle "gui/gallery/eve_001_idle.webp"
                                xsize 311
                                action Replay("ch13_eve_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch13_eve_sex:
                                textbutton "{color=#ffffff}{size=30}Eve: Up for a Fuck{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row5col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch13_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_007_hover.webp"
                                idle "gui/gallery/kallie_007_idle.webp"
                                xsize 311
                                action Replay("ch13_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch13_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Make Up Sex{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row6col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch13_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_006_hover.webp"
                                idle "gui/gallery/shelley_006_idle.webp"
                                xsize 311
                                action Replay("ch13_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch13_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: A New Bed{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row6col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch14_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_008_hover.webp"
                                idle "gui/gallery/laura_008_idle.webp"
                                xsize 311
                                action Replay("ch14_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch14_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Fuck Being Smart{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row6col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch14_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_007_hover.webp"
                                idle "gui/gallery/shelley_007_idle.webp"
                                xsize 311
                                action Replay("ch14_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch14_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: A House Break{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row6col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch14_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_008_hover.webp"
                                idle "gui/gallery/kallie_008_idle.webp"
                                xsize 311
                                action Replay("ch14_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch14_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Am I Pretty{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row7col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch14_eve_sex:
                            imagebutton:
                                hover "gui/gallery/eve_002_hover.webp"
                                idle "gui/gallery/eve_002_idle.webp"
                                xsize 311
                                action Replay("ch14_eve_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch14_eve_sex:
                                textbutton "{color=#ffffff}{size=30}Eve: Backseat{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row7col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch15_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_008_hover.webp"
                                idle "gui/gallery/shelley_008_idle.webp"
                                xsize 311
                                action Replay("ch15_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch15_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Night Relief{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"

###row7col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch15_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_009_hover.webp"
                                idle "gui/gallery/laura_009_idle.webp"
                                xsize 311
                                action Replay("ch15_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch15_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Hot Coffee{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row7col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch15_eve_sex:
                            imagebutton:
                                hover "gui/gallery/eve_003_hover.webp"
                                idle "gui/gallery/eve_003_idle.webp"
                                xsize 311
                                action Replay("ch15_eve_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch15_eve_sex:
                                textbutton "{color=#ffffff}{size=30}Eve: Fooling Around{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row8col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch16_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_010_hover.webp"
                                idle "gui/gallery/laura_010_idle.webp"
                                xsize 311
                                action Replay("ch16_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch16_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Stay Seated{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row8col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch16_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_009_hover.webp"
                                idle "gui/gallery/shelley_009_idle.webp"
                                xsize 311
                                action Replay("ch16_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch16_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Making Me Happy{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"

###row8col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch16_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_009_hover.webp"
                                idle "gui/gallery/kallie_009_idle.webp"
                                xsize 311
                                action Replay("ch16_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch16_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Love You{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row8col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch17_kallie_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/harem_001_hover.webp"
                                idle "gui/gallery/harem_001_idle.webp"
                                xsize 311
                                action Replay("ch17_kallie_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch17_kallie_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie/Shelley Poolside{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row9col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch17_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_010_hover.webp"
                                idle "gui/gallery/kallie_010_idle.webp"
                                xsize 311
                                action Replay("ch17_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch17_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Poolside{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row9col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch17_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_010_hover.webp"
                                idle "gui/gallery/shelley_010_idle.webp"
                                xsize 311
                                action Replay("ch17_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch17_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Poolside{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"

###row9col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch17_eve_sex:
                            imagebutton:
                                hover "gui/gallery/eve_004_hover.webp"
                                idle "gui/gallery/eve_004_idle.webp"
                                xsize 311
                                action Replay("ch17_eve_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch17_eve_sex:
                                textbutton "{color=#ffffff}{size=30}Eve: Back to My Room{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row9col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch17_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_011_hover.webp"
                                idle "gui/gallery/laura_011_idle.webp"
                                xsize 311
                                action Replay("ch17_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch17_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: First Time{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row10col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch18_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_011_hover.webp"
                                idle "gui/gallery/shelley_011_idle.webp"
                                xsize 311
                                action Replay("ch18_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch18_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Not The L Word{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row10col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch18_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_012_hover.webp"
                                idle "gui/gallery/laura_012_idle.webp"
                                xsize 311
                                action Replay("ch18_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch18_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Librarian{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row10col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch18_eve_sex:
                            imagebutton:
                                hover "gui/gallery/eve_005_hover.webp"
                                idle "gui/gallery/eve_005_idle.webp"
                                xsize 311
                                action Replay("ch18_eve_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch18_eve_sex:
                                textbutton "{color=#ffffff}{size=30}Eve: In the Stands{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row10col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch18_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_011_hover.webp"
                                idle "gui/gallery/kallie_011_idle.webp"
                                xsize 311
                                action Replay("ch18_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch18_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Summer School{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row11col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch19_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_012_hover.webp"
                                idle "gui/gallery/shelley_012_idle.webp"
                                xsize 311
                                action Replay("ch19_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch19_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Cheerleader{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row11col2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch19_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_012_hover.webp"
                                idle "gui/gallery/kallie_012_idle.webp"
                                xsize 311
                                action Replay("ch19_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch19_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Love isn't one-way{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row11col3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch19_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_013_hover.webp"
                                idle "gui/gallery/laura_013_idle.webp"
                                xsize 311
                                action Replay("ch19_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch19_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Being Irresponsible{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row11col4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch19_eve_shelley_bi_sex:
                            imagebutton:
                                hover "gui/gallery/shelleyeve_001_hover.webp"
                                idle "gui/gallery/shelleyeve_001_idle.webp"
                                xsize 311
                                action Replay("ch19_eve_shelley_bi_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch19_eve_shelley_bi_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley and Eve{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row12col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch19_eve_sex:
                            imagebutton:
                                hover "gui/gallery/eve_006_hover.webp"
                                idle "gui/gallery/eve_006_idle.webp"
                                xsize 311
                                action Replay("ch19_eve_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch19_eve_sex:
                                textbutton "{color=#ffffff}{size=30}Eve: No Internet{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row#12col#2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch20_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_013_hover.webp"
                                idle "gui/gallery/shelley_013_idle.webp"
                                xsize 311
                                action Replay("ch20_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch20_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Cuddling{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row#12col#3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch20_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_013_hover.webp"
                                idle "gui/gallery/kallie_013_idle.webp"
                                xsize 311
                                action Replay("ch20_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch20_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Poking You{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row#12col#4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch20_eve_sex:
                            imagebutton:
                                hover "gui/gallery/eve_007_hover.webp"
                                idle "gui/gallery/eve_007_idle.webp"
                                xsize 311
                                action Replay("ch20_eve_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch20_eve_sex:
                                textbutton "{color=#ffffff}{size=30}Eve: No Pants{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row13col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch21_eve_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_014_hover.webp"
                                idle "gui/gallery/kallie_014_idle.webp"
                                xsize 311
                                action Replay("ch21_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch21_eve_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: The Man I Want{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row#13col#2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch21_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_014_hover.webp"
                                idle "gui/gallery/shelley_014_idle.webp"
                                xsize 311
                                action Replay("ch21_shelley_sex", scope={"player_name":persistent.player_name or "John", "player_lastname":persistent.player_lastname or "Houston"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch21_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Office Role Play{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row#13col#3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch21_eve_sex:
                            imagebutton:
                                hover "gui/gallery/eve_008_hover.webp"
                                idle "gui/gallery/eve_008_idle.webp"
                                xsize 311
                                action Replay("ch21_eve_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch21_eve_sex:
                                textbutton "{color=#ffffff}{size=30}Eve: What We Are{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row#13col#4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch21_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_014_hover.webp"
                                idle "gui/gallery/laura_014_idle.webp"
                                xsize 311
                                action Replay("ch21_laura_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch21_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Feeling Better{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row14col1
                hbox:
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch22_shelley_sex:
                            imagebutton:
                                hover "gui/gallery/shelley_015_hover.webp"
                                idle "gui/gallery/shelley_015_idle.webp"
                                xsize 311
                                action Replay("ch22_shelley_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch22_shelley_sex:
                                textbutton "{color=#ffffff}{size=30}Shelley: Down To Clown{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row#14col#2
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch22_laura_sex:
                            imagebutton:
                                hover "gui/gallery/laura_015_hover.webp"
                                idle "gui/gallery/laura_015_idle.webp"
                                xsize 311
                                action Replay("ch22_laura_sex", scope={"player_name":persistent.player_name or "John", "player_lastname":persistent.player_lastname or "Houston"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch22_laura_sex:
                                textbutton "{color=#ffffff}{size=30}Laura: Functional Meat{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row#14col#3
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch22_eve_sex:
                            imagebutton:
                                hover "gui/gallery/eve_009_hover.webp"
                                idle "gui/gallery/eve_009_idle.webp"
                                xsize 311
                                action Replay("ch22_eve_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch22_eve_sex:
                                textbutton "{color=#ffffff}{size=30}Eve: I Want To Fuck{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row#14col#4
                    vbox:
                        image "/gui/gallery/box_gallery_left.webp"
                    vbox:
                        image "/gui/gallery/box_gallery_top.webp"
                        if persistent.ch22_kallie_sex:
                            imagebutton:
                                hover "gui/gallery/kallie_015_hover.webp"
                                idle "gui/gallery/kallie_015_idle.webp"
                                xsize 311
                                action Replay("ch22_kallie_sex", scope={"player_name":persistent.player_name or "John"}, locked=False)
                        else:
                            imagebutton:
                                idle "gui/gallery/gallery_locked.webp"
                        hbox:
                            if persistent.ch22_kallie_sex:
                                textbutton "{color=#ffffff}{size=30}Kallie: Bath Check In{/size}{/color}"
                                xalign 0.5
                            else:
                                textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
                                xalign 0.5
                        hbox:
                            imagebutton:
                                idle "/gui/gallery/box_gallery_bottom.webp"
                    vbox:
                        imagebutton:
                            idle "/gui/gallery/box_gallery_right.webp"
###row#col#
#                    vbox:
#                        image "/gui/gallery/box_gallery_left.webp"
#                    vbox:
#                        image "/gui/gallery/box_gallery_top.webp"
#                        imagebutton:
#                            idle "gui/gallery/gallery_locked.webp"
#                        hbox:
#                            textbutton "{color=#000000}{size=30}LOCKED{/size}{/color}"
#                            xalign 0.5
#                        hbox:
#                            imagebutton:
#                                idle "/gui/gallery/box_gallery_bottom.webp"
#                    vbox:
#                        imagebutton:
#                            idle "/gui/gallery/box_gallery_right.webp"
####achievement pictures
label ach_chapter1:
    $ quick_menu = False
    scene ach_c001_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter2:
    $ quick_menu = False
    scene ach_c002_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter3:
    $ quick_menu = False
    scene ach_c003_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter4:
    $ quick_menu = False
    scene ach_c004_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter5:
    $ quick_menu = False
    scene ach_c005_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter6:
    $ quick_menu = False
    scene ach_c006_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter7:
    $ quick_menu = False
    scene ach_c007_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter8:
    $ quick_menu = False
    scene ach_c008_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter9:
    $ quick_menu = False
    scene ach_c009_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter10:
    $ quick_menu = False
    scene ach_c010_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter11:
    $ quick_menu = False
    scene ach_c011_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter12:
    $ quick_menu = False
    scene ach_c012_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter13:
    $ quick_menu = False
    scene ach_c013_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter14:
    $ quick_menu = False
    scene ach_c014_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter15:
    $ quick_menu = False
    scene ach_c015_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter16:
    $ quick_menu = False
    scene ach_c016_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter17:
    $ quick_menu = False
    scene ach_c017_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter18:
    $ quick_menu = False
    scene ach_c018_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter19:
    $ quick_menu = False
    scene ach_c019_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter20:
    $ quick_menu = False
    scene ach_c020_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter21:
    $ quick_menu = False
    scene ach_c021_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_chapter22:
    $ quick_menu = False
    scene ach_c022_001 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_laura_firsttime:
    $ quick_menu = False
    scene ach_c003_002 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_kallie_firsttime:
    $ quick_menu = False
    scene ach_c006_002 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_shelley_firsttime:
    $ quick_menu = False
    scene ach_c007_002 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_eve_firsttime:
    $ quick_menu = False
    scene ach_c013_002 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_allfour_firsttime:
    $ quick_menu = False
    scene ach_c013_003 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_firstlove:
    $ quick_menu = False
    scene ach_c016_002 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True
label ach_threesome:
    $ quick_menu = False
    scene ach_c017_002 with Dissolve(0.5)
    $ renpy.pause ()
    $ renpy.end_replay()
    $ quick_menu = True

label misc_achievement_check:
    if k_sex >= 1 and e_sex >= 1 and s_sex >= 1 and l_sex >= 1 and persistent.all_firstime == False:
        scene blank with Dissolve(2)
        $ persistent.all_firstime = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_allfour_firstime", transition=slideright)()
        pause
        $ Hide("achievement_allfour_firstime", transition=dissolve)()
        $ quick_menu = True
    if kallie_lover == "yes" and persistent.all_firstlove == False or shelley_lover == "yes" and persistent.all_firstlove == False or laura_lover == "yes" and persistent.all_firstlove == False or eve_lover == "yes" and persistent.all_firstlove == False:
        scene blank with Dissolve(2)
        $ persistent.all_firstlove = True
        $ quick_menu = False
        scene blank with Dissolve(2)
        window hide
        $ Show("achievement_firstlove", transition=slideright)()
        pause
        $ Hide("achievement_firstlove", transition=dissolve)()
        $ quick_menu = True
    return
