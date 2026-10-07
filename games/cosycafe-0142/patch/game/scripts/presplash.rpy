# remove this screen in the following versions if the issue with saves does not persist
image clr = Solid('#0d0d0d')

label splashscreen:

    scene clr
    show screen warning
    pause
    hide screen warning
    show black
    with dissolve

    if persistent.lucy_img_main8_201_unlocked == True:
        $ persistent.lucy_img_main8_201_unlocked = False
        $ persistent.lucy_img_main08_201_unlocked = True

    if persistent.victoria_img_main6_386_unlocked == True:
        $ persistent.victoria_img_main6_386_unlocked = False
        $ persistent.victoria_img_main06_386_unlocked = True

    if persistent.victoria_img_main8_202_unlocked == True:
        $ persistent.victoria_img_main8_202_unlocked = False
        $ persistent.victoria_img_main08_202_unlocked = True

    if persistent.victoria_img_main8_203_unlocked == True:
        $ persistent.victoria_img_main8_203_unlocked = False
        $ persistent.victoria_img_main08_203_unlocked = True

    return

screen warning():

    vbox:
        align (.5, .5)
        spacing 16
        frame:
            background None
            xysize (None, 100)
            align (.5, .5)
            text '{b}警告！{/b}' size 78 color '#ff696c' align (.5, .5):
                at transform:
                    subpixel True
                    ease 1.0 zoom 1.0
                    ease 1.0 zoom 1.1
                    repeat
        null height 50
        text '请注意：0.12 版本的改动会导致旧存档无法读取。' size 33 color '#f1f1f1' align (.5, .5)
        text '就算勉强能用，也很可能在游戏里引发各种其他问题。' size 20 color '#f1f1f1' align (.5, .5)
        text '\n新开游戏时可以直接跳过，直达新内容，避免进度丢失。' size 33 color '#f1f1f1' align (.5, .5)