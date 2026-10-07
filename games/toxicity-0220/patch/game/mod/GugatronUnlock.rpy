default unlocked = False

init 999:
    python:
        def toggle_gallery():
            if unlocked:
                Gugatron_mod_image_unlock()
            else:
                Gugatron_mod_image_lock()

        def Gugatron_mod_image_unlock():
            """ Gugatron 插件解锁全部图库,并记录哪些是被本插件解锁的。 """
            global Gugatron_mod_unlocked
            Gugatron_mod_unlocked = []  # 重置插件解锁列表

            images = [
                "ch3_laura_sex",
                "ch4_laura_sex",
                "ch5_laura_sex",
                "ch6_laura_sex",
                "ch9_laura_sex",
                "ch10_laura_sex",
                "ch12_laura_sex",
                "ch14_laura_sex",
                "ch15_laura_sex",
                "ch16_laura_sex",
                "ch17_laura_sex",
                "ch18_laura_sex",
                "ch19_laura_sex",
                "ch21_laura_sex",
                "ch22_laura_sex",
                "ch6_kallie_sex",
                "ch7_kallie_sex",
                "ch8_kallie_sex",
                "ch10_kallie_sex",
                "ch11_kallie_sex",
                "ch12_kallie_sex",
                "ch13_kallie_sex",
                "ch14_kallie_sex",
                "ch16_kallie_sex",
                "ch17_kallie_sex",
                "ch18_kallie_sex",
                "ch19_kallie_sex",
                "ch20_kallie_sex",
                "ch21_kallie_sex",
                "ch22_kallie_sex",
                "ch7_shelley_sex",
                "ch8_shelley_sex",
                "ch9_shelley_sex",
                "ch11_shelley_sex",
                "ch12_shelley_sex",
                "ch13_shelley_sex",
                "ch14_shelley_sex",
                "ch15_shelley_sex",
                "ch16_shelley_sex",
                "ch17_shelley_sex",
                "ch18_shelley_sex",
                "ch19_shelley_sex",
                "ch20_shelley_sex",
                "ch21_shelley_sex",
                "ch22_shelley_sex",
                "ch13_eve_sex",
                "ch14_eve_sex",
                "ch15_eve_sex",
                "ch17_eve_sex",
                "ch18_eve_sex",
                "ch19_eve_sex",
                "ch20_eve_sex",
                "ch21_eve_sex",
                "ch22_eve_sex",
                "ch17_kallie_shelley_sex",
                "ch19_eve_shelley_bi_sex",
                "ch1_complete",
                "ch2_complete",
                "ch3_complete",
                "ch4_complete",
                "ch5_complete",
                "ch6_complete",
                "ch7_complete",
                "ch8_complete",
                "ch9_complete",
                "ch10_complete",
                "ch11_complete",
                "ch12_complete",
                "ch13_complete",
                "ch14_complete",
                "ch15_complete",
                "ch16_complete",
                "ch17_complete",
                "ch18_complete",
                "ch19_complete",
                "ch20_complete",
                "ch21_complete",
                "ch22_complete",
                "ch23_complete",
                "laura_firstime",
                "kallie_firstime",
                "shelley_firstime",
                "eve_firstime",
                "all_firstime",
                "all_firstlove",
                "threesome",
            ]

            for img in images:
                if not getattr(persistent, img, False):  # 若玩家尚未解锁
                    setattr(persistent, img, True)  # 解锁
                    Gugatron_mod_unlocked.append(img)  # 记入插件解锁列表

            print("插件解锁的图片:", Gugatron_mod_unlocked)

        def Gugatron_mod_image_lock():
            # 仅锁定由本插件解锁的图片。
            global Gugatron_mod_unlocked
            for img in Gugatron_mod_unlocked:
                setattr(persistent, img, False)  # 只锁定插件解锁的

            print("已锁定插件解锁的图片:", Gugatron_mod_unlocked)
            Gugatron_mod_unlocked = []  # 清空插件解锁列表
