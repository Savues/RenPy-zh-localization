default persistent.name = False
image bg:
    "gui/msp1/main_menu/bg.png"
label gallery_name:
    show bg at temp_gallery()
    if not persistent.name:
        $ persistent.replay_PlayerName = renpy.input("请输入你的名字：", default="杰克")
        $ persistent.name = True
    return

default persistent.akari_testing_unlocked = False

define photo_gallery_chars = [
    { "name": "lucy"         , "images": [], }, 
    { "name": "victoria"     , "images": [], },
    { "name": "sarah"        , "images": [], },
    { "name": "akatsuki"     , "images": [], },
    { "name": "rachel"       , "images": [], },
    { "name": "hannah"       , "images": [], },
    { "name": "alison"       , "images": [], },
    { "name": "misaki"       , "images": [], },
    { "name": "akari"        , "images": [], },
    { "name": "catherine"    , "images": [], },
    { "name": "elizabeth"    , "images": [], },
    { "name": "annabelle"    , "images": [], },
    { "name": "group"        , "images": [], },
]

# """

# ## Gallery replay content notes: "scenes" key 
# # [0] First index must always be the scene's title (if it has one. If it doesn't, it should have one.)
# # [1] Second index must always be the scene's genre
# # [2] Third index must always be the replay's label. (label replay_lucy1:)
# # [3] Fourth index must always be the the exact name of the thumbnail image file.

# """

init python:
    
    replay_gallery_content = [
        { "name": "lucy",           "scenes": [ #0

            ]
        },
        { "name": "victoria",       "scenes": [ #1

            ]
        },
        { "name": "sarah",          "scenes": [ #2

            ]
        },
        { "name": "akatsuki",       "scenes": [ #3

            ]
        },
        { "name": "rachel",         "scenes": [ #4

            ]
        },
        { "name": "hannah",         "scenes": [ #5

            ]
        },
        { "name": "alison",   "scenes": [ #6
                
            ]
        },
        { "name": "misaki",  "scenes": [ #7
                
            ]
        },
        { "name": "akari",          "scenes": [ #8

            ]
        },
        { "name": "catherine",      "scenes": [ #9

            ]
        },
        { "name": "elizabeth",      "scenes": [ #10

            ]
        },
        { "name": "annabelle",      "scenes": [ #11

            ]
        },
        { "name": "group"    ,      "scenes": [ #12

            ]
        },

    ]

    def refresh_replay_gallery_content():
        global replay_gallery_content
        for character in replay_gallery_content:
            character['scenes'] = []

    #Lucy
        if persistent.gallery_lucy1:
            replay_gallery_content[0]['scenes'].append(["新女友", "抚摸", "replay_lucy1", "img_main11_14"])
        if persistent.gallery_lucy2:
            replay_gallery_content[0]['scenes'].append(["「王者游戏」之后", "手活／口交", "replay_lucy2", "img_main11_411"])
        if persistent.gallery_lucy3:
            replay_gallery_content[0]['scenes'].append(["献给维多利亚的表演", "手交", "replay_lucy3", "img_main13_416"])
        if persistent.gallery_lucy4:
            replay_gallery_content[0]['scenes'].append(["露西的第一次", "性交", "replay_lucy4", "img_main15_504"])
        if persistent.gallery_lucy5:
            replay_gallery_content[0]['scenes'].append(["课桌下的乐趣", "手活／性交", "replay_lucy5", "img_main18_145"])
        if persistent.gallery_lucy6:
            replay_gallery_content[0]['scenes'].append(["露西的奖赏", "手活", "replay_lucy6", "img_main21_67"])
        if persistent.gallery_lucy7:
            replay_gallery_content[0]['scenes'].append(["跳蛋乐趣", "性交", "replay_lucy7", "img_main25_691"])
        if persistent.gallery_lucy8:
            replay_gallery_content[0]['scenes'].append(["惩罚时间", "打屁股／手活", "replay_lucy8", "img_main30_510"])
        
    #Victoria
        if persistent.gallery_victoria1:
            replay_gallery_content[1]['scenes'].append(["才没那么恶心", "手交", "replay_victoria1", "img_main10_131"])
        if persistent.gallery_victoria2:
            replay_gallery_content[1]['scenes'].append(["更衣室的乐趣", "夹腿", "replay_victoria2", "img_main12_237"])
        if persistent.gallery_victoria3:
            replay_gallery_content[1]['scenes'].append(["手铐", "口交", "replay_victoria3", "img_main16_437"])
        if persistent.gallery_victoria4:
            replay_gallery_content[1]['scenes'].append(["维多利亚的第一次", "性交", "replay_victoria4", "img_main19_266"])
        if persistent.gallery_victoria5:
            replay_gallery_content[1]['scenes'].append(["维多利亚终于高潮了", "性交", "replay_victoria5", "img_main22_603"])
        
    #Akatsuki
        if persistent.gallery_akatsuki1:
            replay_gallery_content[3]['scenes'].append(["无数第一次中的第一次", "口交", "replay_akatsuki1", "img_main14_285"])
        if persistent.gallery_akatsuki2:
            replay_gallery_content[3]['scenes'].append(["清晨的满足", "口交", "replay_akatsuki2", "img_main15_18"])
        if persistent.gallery_akatsuki3:
            replay_gallery_content[3]['scenes'].append(["晓月的第一次（算是吧）", "口交", "replay_akatsuki3", "img_main21_864"])
        if persistent.gallery_akatsuki4:
            replay_gallery_content[3]['scenes'].append(["淋浴时光 1", "口交", "replay_akatsuki4", "img_main22_30"])
        if persistent.gallery_akatsuki5:
            replay_gallery_content[3]['scenes'].append(["淋浴时光 2 - 薇琪特别版", "口交", "replay_akatsuki5", "img_main23_28"])
        if persistent.gallery_akatsuki6:
            replay_gallery_content[3]['scenes'].append(["不需要泳装", "口交", "replay_akatsuki6", "img_main23_446"])
        if persistent.gallery_akatsuki7:
            replay_gallery_content[3]['scenes'].append(["晓月的第一次（这次是真的）", "性交", "replay_akatsuki7", "img_main26_23"])
        if persistent.gallery_akatsuki8:
            replay_gallery_content[3]['scenes'].append(["暴露", "口交", "replay_akatsuki8", "img_main27_645"])
        if persistent.gallery_akatsuki9:
            replay_gallery_content[3]['scenes'].append(["淋浴时光 3", "手活", "replay_akatsuki9", "img_main30_46"])
                
    #Alison
        if persistent.gallery_headmistress1:
            replay_gallery_content[6]['scenes'].append(["证明自己", "口交", "replay_headmistress1", "img_main17_146"])
        if persistent.gallery_headmistress2:
            replay_gallery_content[6]['scenes'].append(["权力之争", "口交", "replay_headmistress2", "img_main30_692"])
                
    #Misaki
        if persistent.gallery_taka1:
            replay_gallery_content[7]['scenes'].append(["车站洗手间 1", "手活", "replay_taka1", "img_main21_478"])
        if persistent.gallery_taka2:
            replay_gallery_content[7]['scenes'].append(["车站洗手间 2", "口交", "replay_taka2", "img_main24_586"])
        if persistent.gallery_taka3:
            replay_gallery_content[7]['scenes'].append(["办公室乐趣 1", "自慰", "replay_taka3", "img_main28_317"])

    #Catherine
        if persistent.gallery_catherine1:
            replay_gallery_content[9]['scenes'].append(["要命的初吻", "手交", "replay_catherine1", "img_main29_336"])

    #Group
        if persistent.gallery_group1:
            replay_gallery_content[12]['scenes'].append(["燃烧的甜品", "口交", "replay_group1", "img_main20_575"])
        if persistent.gallery_group2:
            replay_gallery_content[12]['scenes'].append(["在脸上作画", "口交／手活", "replay_group2", "img_main23_618"])
        if persistent.gallery_group3:
            replay_gallery_content[12]['scenes'].append(["抢先冲刺", "手交／口交／乳交／性交", "replay_group3", "img_main26_1360"])
        if persistent.gallery_group4:
            replay_gallery_content[12]['scenes'].append(["两只小猫咪", "口交", "replay_group4", "img_main29_1303"])
        if persistent.gallery_group5:
            replay_gallery_content[12]['scenes'].append(["比分：露西 5，薇琪 1", "三P", "replay_group5", "img_main32_1221"])

init python:
    def unlock_image(character_name, image_name):
        source_path = f"images/Gallery/{character_name}/{image_name}"
        
        if renpy.file(source_path):
            setattr(persistent, f"{character_name}_{os.path.splitext(image_name)[0]}_unlocked", True)
            print(f"Image {image_name} unlocked for {character_name}")
        else:
            print(f"Image {image_name} not found in archive")

    def load_images(character_name):
        images = []
        directory = f"images/Gallery/{character_name}/"

        # Check the unlocked status of each image before adding it to the list
        for file in renpy.list_files():
            if file.startswith(directory) and file.endswith(('.png', '.jpg', '.jpeg', '.webp')):
                image_name = os.path.basename(file)
                if getattr(persistent, f"{character_name}_{os.path.splitext(image_name)[0]}_unlocked", False):
                    images.append(file)
        
        print(f"Loaded images for {character_name} from archive: {images}")

        return images

    def refresh_images():
        for char in photo_gallery_chars:
            char_name = char['name']
            directory = f"images/Gallery/{char_name}/"
            locked_images = [file for file in renpy.list_files() if file.startswith(directory) and file.endswith(('.png', '.jpg', '.jpeg', '.webp'))]

            for image_name in locked_images:
                if getattr(persistent, f"{char_name}_{os.path.splitext(image_name)[0]}_unlocked", False):
                    unlock_image(char_name, image_name)
            char['images'] = load_images(char_name)
        renpy.restart_interaction()

    def lock_image(character_name, image_name):
        setattr(persistent, f"{character_name}_{os.path.splitext(image_name)[0]}_unlocked", False)
        print(f"Image {image_name} locked for {character_name}")

    # Initial load of images
    refresh_images()

    def init_images():
        #Lucy
        # if persistent.lucy_img_main8_201_unlocked:
        #     unlock_image('lucy', 'img_main8_201.webp')
        # if persistent.lucy_img_main17_324_unlocked:
        #     unlock_image('lucy', 'img_main17_324.webp')

        #Victoria
        # if persistent.victoria_img_main6_386_unlocked:
        #     unlock_image('victoria', 'img_main6_386.webp')
        # if persistent.victoria_img_main8_202_unlocked:
        #     unlock_image('victoria', 'img_main8_202.webp')
        # if persistent.victoria_img_main8_203_unlocked:
        #     unlock_image('victoria', 'img_main8_203.webp')
        # if persistent.victoria_img_main12_20_unlocked:
        #     unlock_image('victoria', 'img_main12_20.webp')
        # if persistent.victoria_img_main12_21_unlocked:
        #     unlock_image('victoria', 'img_main12_21.webp')
        # if persistent.victoria_img_main12_22_unlocked:
        #     unlock_image('victoria', 'img_main12_22.webp')
        # if persistent.victoria_img_main12_261_unlocked:
        #     unlock_image('victoria', 'img_main12_261.webp')
        # if persistent.victoria_img_main13_187_unlocked:
        #     unlock_image('victoria', 'img_main13_187.webp')
        # if persistent.victoria_img_main13_188_unlocked:
        #     unlock_image('victoria', 'img_main13_188.webp')
        # if persistent.victoria_img_main17_318_unlocked:
        #     unlock_image('victoria', 'img_main17_318.webp')

        # #Akatsuki
        # if persistent.akatsuki_img_main21_796_unlocked:
        #     unlock_image('akatsuki', 'img_main21_796.webp')

        # #Sarah
        # if persistent.sarah_img_main17_361_unlocked:
        #     unlock_image('sarah', 'img_main17_361.webp')
        # if persistent.sarah_img_main17_362_unlocked:
        #     unlock_image('sarah', 'img_main17_362.webp')
        # if persistent.sarah_img_main20_366_unlocked:
        #     unlock_image('sarah', 'img_main20_366.webp')
        # if persistent.sarah_img_main20_369_unlocked:
        #     unlock_image('sarah', 'img_main20_369.webp')
        # if persistent.sarah_img_main20_373_unlocked:
        #     unlock_image('sarah', 'img_main20_373.webp')
        # if persistent.sarah_img_main20_374_unlocked:
        #     unlock_image('sarah', 'img_main20_374.webp')
        # if persistent.sarah_img_main20_375_unlocked:
        #     unlock_image('sarah', 'img_main20_375.webp')
        # if persistent.sarah_img_main20_378_unlocked:
        #     unlock_image('sarah', 'img_main20_378.webp')
        # if persistent.sarah_img_main20_379_unlocked:
        #     unlock_image('sarah', 'img_main20_379.webp')
        # if persistent.sarah_img_main20_382_unlocked:
        #     unlock_image('sarah', 'img_main20_382.webp')
        # if persistent.sarah_img_main20_383_unlocked:
        #     unlock_image('sarah', 'img_main20_383.webp')
        # if persistent.sarah_img_main20_384_unlocked:
        #     unlock_image('sarah', 'img_main20_384.webp')
        # if persistent.sarah_img_main20_385_unlocked:
        #     unlock_image('sarah', 'img_main20_385.webp')
        # if persistent.sarah_img_main20_390_unlocked:
        #     unlock_image('sarah', 'img_main20_390.webp')
        # if persistent.sarah_img_main23_400_unlocked:
        #     unlock_image('sarah', 'img_main23_400.webp')

        # #Hannah

        # #Alison
        # if persistent.alison_img_main17_158_unlocked:
        #     unlock_image('alison', 'img_main17_158.webp')

        # #Misaki
        # if persistent.alison_img_main26_349_unlocked:
        #     unlock_image('misaki', 'img_main17_158.webp')

        # #Rachel

        # #Akari

        # #Elizabeth

        # #Group
        # if persistent.group_img_main16_144_unlocked:
        #     unlock_image('group', 'img_main16_144.webp')
        # if persistent.group_img_main17_331_unlocked:
        #     unlock_image('group', 'img_main17_331.webp')
        # if persistent.group_img_main21_673_unlocked:
        #     unlock_image('group', 'img_main21_673.webp')
        # if persistent.group_img_main23_608_unlocked:
        #     unlock_image('group', 'img_main23_608.webp')
        # if persistent.group_img_main25_916_unlocked:
        #     unlock_image('group', 'img_main25_916.webp')


        # if persistent.group_test_unlocked:
        #     unlock_image('group', 'test.jpg')

        renpy.restart_interaction()


screen photo_gallery():

    tag menu
    add "gui/msp1/main_menu/bg.png":
        at transform:
            xycenter (.5, .5)
            zoom      .5
    add "gui/msp1/bg.webp" at bg_in()

    default sort_state = None

    frame:
        image "gui/msp1/gallery_ui/i/inner_plates.png" at plate_in()
        pos    (75  , 75 )
        xysize (1770, 930)

        hbox:
            spacing 8
            at photo_gallery_general_in()
            frame:
                xysize (1178, 930)
                offset (-6  , -6 )

                frame:
                    xysize (1147, 915)
                    offset (2, 2)
                    if all(not char['images'] for char in photo_gallery_chars):
                        text "没有找到图片 :(" font "fonts/MiSans-Regular.ttf" color "#f1f1f1" align (.5, .5) size 64 at transform:
                            alpha .0
                            pause .75
                            easein_quint .5 alpha 1.0
                    else:
                        vpgrid id 'pg':
                            align (.5, .5)
                            xysize     (1147, 914)
                            spacing    8
                            draggable  True
                            mousewheel True
                            cols 3
                            for char in photo_gallery_chars:
                                if sort_state is None or char['name'] == sort_state:
                                    for x, image in enumerate(char['images']):
                                        $ import os
                                        $ normalized_image = image.replace("\\", "/")
                                        frame:
                                            xysize (377, 300)
                                            align (.5, .5)
                                            button:
                                                focus_mask True
                                                align (.5, .5)
                                                action ShowMenu('gallery_image_view', images=char['images'], index=x)
                                                image AlphaMask(Transform(normalized_image, zoom = .3, crop=(377, 0, 1920, 1080)), 'gui/msp1/gallery_ui/i/photo_item.png') offset (-6, -6)
                                                # text os.path.basename(normalized_image).upper() font "fonts/MiSans-Regular.ttf" color "#0eda9f" align (.5, .5)
                                                xysize (377, 300)

                        vbar value YScrollValue ('pg') align (1.0, .5) xysize (8, 914) offset (20, 0)
            frame:

                xysize (585 , 930)
                offset (-6  , -6 )

                vbox:

                    spacing 8

                    frame:

                        xysize (585, 730)
                        offset (-6 , -6 )

                        frame:

                            xysize (569, 714)
                            offset (2  , 2  )

                            viewport id 'pc':

                                spacing    8
                                xysize     (569, 714)
                                offset     (-6, -6)
                                draggable  True
                                mousewheel True

                                at transform:

                                    offset (0, -1080)

                                    easein_quart (1.25 * persistent.ui_speed_multiplier) offset (0, 0)

                                vbox:

                                    spacing 8

                                    for index, char in enumerate(photo_gallery_chars):

                                        frame:

                                            xysize (553, 112)

                                            button:

                                                xysize (553, 112)
                                                align  (.5 ,  .5)

                                                focus_mask True
                                                
                                                action [ Function(refresh_images), SetScreenVariable('sort_state', char['name']), Function(init_images) ]

                                                image AlphaMask(Transform(im.Blur("gui/msp1/bios/" + str(char['name']) + "/" + str(char['name']) + "_bg.webp", 4), zoom = .3, crop = (0, 0, 1920, 1080)), "gui/msp1/gallery_ui/i/char_plate.png") offset (-6, -6):

                                                    at transform:

                                                        on idle:

                                                            easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(-.125)

                                                        on hover:

                                                            easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(-.225)

                                                image "gui/msp1/bios/" + str(char['name']) + "/" + str(char['name']) + "_close.png" align (.0, 1.0) offset (9, 6)

                                                text char['name'].upper() font "fonts/MiSans-Regular.ttf" align (.0 , 1.0) offset (175, -25) color "#ffffff"
                                                
                                                # at cascade_image_gallery_char(index*.1)

                        vbar value YScrollValue ('pc') align (1.0, .5) xysize (8, 714) offset (-2, 0)

                    frame:

                        xysize (585, 192)
                        offset (-6 , -6 )

                        frame:

                            xysize (569, 176)
                            align  (.5 ,  .5)

                            vbox:

                                align (.5, .5)
                                spacing 8

                                frame:

                                    xysize (569, 84)

                                    button:

                                        xysize (569, 84)
                                        align  (.5 , .5)

                                        focus_mask True

                                        action [ Function(refresh_images), SetScreenVariable('sort_state', None), Function(init_images) ]

                                        image "gui/msp1/gallery_ui/i/no_filter.png" align (.5 , .5):
                                            at transform:

                                                on idle:

                                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#000', '#fff')

                                                on hover:

                                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#ffb1df', '#fff')


                                        at cascade_image_gallery_char(.1)

                                frame:
                                    xysize (569, 84)
                                    button:

                                        xysize (569, 84)
                                        align  (.5 , .5)

                                        focus_mask True

                                        action Return()

                                        image "gui/msp1/gallery_ui/i/return.png" align (.5 , .5):
                                            at transform:

                                                on idle:

                                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#000', '#fff')

                                                on hover:

                                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#ffb1df', '#fff')

                                        at cascade_image_gallery_char(.2)

screen gallery_image_view(images, index):

    modal True

    imagebutton:
        action Hide('gallery_image_view')
        idle images[index]


    if index > 0:
        button:

            align  ( .0, 1.0)
            xysize (120,  50)
            offset ( 24, -24)

            action ShowMenu("gallery_image_view", images=images, index=index-1)

            background Frame("gui/msp1/confirm/button.png", Borders(16, 16, 16, 16))
            text "◂―" size 32 font "fonts/MiSans-Regular.ttf" text_align .5 align (.5, .5) offset (0, -2)
            alt 'Previous Image'

            at transform:

                matrixcolor ColorizeMatrix('#000', '#fff')

                on idle:
                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor InvertMatrix(.0)
                on hover:
                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor InvertMatrix(1.0)

    if index < len(images) - 1:
        button:

            align  (1.0, 1.0)
            xysize (120,  50)
            offset (-24, -24)

            action ShowMenu("gallery_image_view", images=images, index=index+1)

            background Frame("gui/msp1/confirm/button.png", Borders(16, 16, 16, 16))
            text "―▸" size 32 font "fonts/MiSans-Regular.ttf" text_align .5 align (.5, .5) offset (0, -2)
            alt 'Next Image'

            at transform:

                matrixcolor ColorizeMatrix('#000', '#fff')

                on idle:
                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor InvertMatrix(.0)
                on hover:
                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor InvertMatrix(1.0)


init python:
    def set_preview_values(index):
        if isinstance(index, int) and index < len(replay_gallery_content) and replay_gallery_content[index]['scenes'] and len(replay_gallery_content[index]['scenes']) > 0:
            renpy.store.preview_ident = replay_gallery_content[index]['name']
            renpy.store.preview_title = replay_gallery_content[index]['scenes'][0][0]
            renpy.store.preview_genre = replay_gallery_content[index]['scenes'][0][1]
            renpy.store.preview_label = replay_gallery_content[index]['scenes'][0][2]
            renpy.store.preview_thumb = replay_gallery_content[index]['scenes'][0][3]
        elif index == "default":
            preview_ident = "???"
            preview_title = "???"
            preview_genre = "???"
            preview_label = None
            preview_thumb = "gui/msp1/gallery_ui/r/default.png"
        else:
            renpy.store.preview_ident = ""
            renpy.store.preview_title = ""
            renpy.store.preview_genre = ""
            renpy.store.preview_label = None
            renpy.store.preview_thumb = "gui/msp1/gallery_ui/r/locked.png"

default preview_ident = "" # replay_gallery_content[0]['name']
default preview_title = "" # replay_gallery_content[0]['scenes'][0][0]
default preview_genre = "Select a scene" # replay_gallery_content[0]['scenes'][0][1]
default preview_label = None # replay_gallery_content[0]['scenes'][0][2]
default preview_thumb = "gui/msp1/gallery_ui/r/default.png" # replay_gallery_content[0]['scenes'][0][3]

screen replay_gallery():

    tag menu
    add "gui/msp1/main_menu/bg.png":
        at transform:
            xycenter (.5, .5)
            zoom      .5
    add "gui/msp1/bg.webp" at bg_in()

    default sort_state = None

    frame:
        xycenter (.5, .5)
        xysize   (1770, 930)
        at photo_gallery_general_in()
        
        # ██╗      █████╗ ██████╗  ██████╗ ███████╗    ████████╗██╗  ██╗██╗   ██╗███╗   ███╗██████╗ ███╗   ██╗ █████╗ ██╗██╗     
        # ██║     ██╔══██╗██╔══██╗██╔════╝ ██╔════╝    ╚══██╔══╝██║  ██║██║   ██║████╗ ████║██╔══██╗████╗  ██║██╔══██╗██║██║     
        # ██║     ███████║██████╔╝██║  ███╗█████╗         ██║   ███████║██║   ██║██╔████╔██║██████╔╝██╔██╗ ██║███████║██║██║     
        # ██║     ██╔══██║██╔══██╗██║   ██║██╔══╝         ██║   ██╔══██║██║   ██║██║╚██╔╝██║██╔══██╗██║╚██╗██║██╔══██║██║██║     
        # ███████╗██║  ██║██║  ██║╚██████╔╝███████╗       ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║██████╔╝██║ ╚████║██║  ██║██║███████╗
        # ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚══════╝

        frame:
            offset (-6  , -6 )
            xysize (1416, 700)
            align  (.0  , .0 )
            button:

                xysize (1416, 700)
                align (.5, .5)
                
                action If(preview_label != None, Replay(preview_label, scope={"name": persistent.gallery_name}, locked=False), NullAction())

                image AlphaMask(Transform(preview_thumb, zoom = .755),"gui/msp1/gallery_ui/r/thumbnail_large.png") offset (-6, -6)
                image AlphaMask("gui/msp1/gallery_ui/r/thumbnail_large_overlay.png","gui/msp1/gallery_ui/r/thumbnail_large.png") offset (0, 6) align (.5, 1.0)
                if preview_ident != "???" and preview_ident != "Feels":
                    image "gui/msp1/gallery_ui/r/play.png" xycenter (.5 , .5):
                        at transform:
                            subpixel True
                            on idle:
                                easein_quint (.5 * persistent.ui_speed_multiplier) zoom 1.0
                            on hover:
                                easein_quint (.5 * persistent.ui_speed_multiplier) zoom 1.05
                hbox:
                    align (.0, 1.0)
                    offset (15, -15)
                    spacing 8
                    if preview_ident and preview_title and preview_genre:
                        text preview_ident.upper() font "fonts/MiSans-Regular.ttf"
                        text "-"
                        text preview_title.upper() font "fonts/MiSans-Regular.ttf"
                        text "-"
                        text preview_genre.upper() font "fonts/MiSans-Regular.ttf"

                    at transform:
                        subpixel True
                        on idle:
                            easein_quint (.5 * persistent.ui_speed_multiplier) zoom 1.0
                        on hover:
                            easein_quint (.5 * persistent.ui_speed_multiplier) zoom 1.05
                    
                at transform:
                    on hover:
                        easein_quint (.5 * persistent.ui_speed_multiplier) zoom .99
                    on idle:
                        easein_quint (.5 * persistent.ui_speed_multiplier) zoom 1.0

        # ███████╗███╗   ███╗ █████╗ ██╗     ██╗         ████████╗██╗  ██╗██╗   ██╗███╗   ███╗██████╗ ███╗   ██╗ █████╗ ██╗██╗     ███████╗
        # ██╔════╝████╗ ████║██╔══██╗██║     ██║         ╚══██╔══╝██║  ██║██║   ██║████╗ ████║██╔══██╗████╗  ██║██╔══██╗██║██║     ██╔════╝
        # ███████╗██╔████╔██║███████║██║     ██║            ██║   ███████║██║   ██║██╔████╔██║██████╔╝██╔██╗ ██║███████║██║██║     ███████╗
        # ╚════██║██║╚██╔╝██║██╔══██║██║     ██║            ██║   ██╔══██║██║   ██║██║╚██╔╝██║██╔══██╗██║╚██╗██║██╔══██║██║██║     ╚════██║
        # ███████║██║ ╚═╝ ██║██║  ██║███████╗███████╗       ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║██████╔╝██║ ╚████║██║  ██║██║███████╗███████║
        # ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝

        frame:
            xysize (1416, 220)
            align  (.0  , 1.0)
            offset (-12 , 0  )
            viewport id 'rg':
                # offset (-6, -6)
                xysize (1416, 220)
                draggable  True
                mousewheel "horizontal"
                hbox:
                    spacing 8
                    for i, item in enumerate(replay_gallery_content):
                        if sort_state is None or item['name'] == sort_state:
                            $ content = item['scenes']
                            for sub in content:
                                $ title = sub[0]
                                $ genre = sub[1]
                                $ label = sub[2]
                                $ thumb = sub[3]
                                frame:
                                    xysize (348, 206)
                                    button:

                                        xysize (348, 206)
                                        align (.5, .5)

                                        focus_mask True

                                        hovered   [ SetVariable('preview_ident', item['name']), SetVariable('preview_title', title), SetVariable('preview_genre', genre), SetVariable('preview_thumb', thumb), SetVariable('preview_label', label) ]
                                        unhovered [ SetVariable('preview_ident', item['name']), SetVariable('preview_title', title), SetVariable('preview_genre', genre), SetVariable('preview_thumb', thumb), SetVariable('preview_label', label) ]

                                        action Replay(label, scope={"name": persistent.gallery_name}, locked=False)

                                        image AlphaMask(Transform(thumb, zoom = .2), "gui/msp1/gallery_ui/r/thumbnail_small.png") offset (-6, -6)
                                        image AlphaMask(Transform("gui/msp1/gallery_ui/r/foreground.png", zoom = .755, crop = (0, 800, 1920, 1080)), "gui/msp1/gallery_ui/r/thumbnail_small.png") alpha .75 offset (-6, -6)
                                        image "gui/msp1/gallery_ui/r/play.png" align (.5, .5) zoom .5

                                        at shrink()
                                    at item_in(i*.1)
            bar value XScrollValue ('rg') align (.5, 1.0) xysize (1416, 8) offset (6, 12)

        #  ██████╗██╗  ██╗ █████╗ ██████╗  █████╗  ██████╗████████╗███████╗██████╗ ███████╗
        # ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝
        # ██║     ███████║███████║██████╔╝███████║██║        ██║   █████╗  ██████╔╝███████╗
        # ██║     ██╔══██║██╔══██║██╔══██╗██╔══██║██║        ██║   ██╔══╝  ██╔══██╗╚════██║
        # ╚██████╗██║  ██║██║  ██║██║  ██║██║  ██║╚██████╗   ██║   ███████╗██║  ██║███████║
        #  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝

        frame:
            xysize (345, 700)
            align  (1.0, .0 )
            offset (6  , -6 )
            viewport id "rc":
                xycenter   (.5 , .5)
                offset     (-6 , 0 )
                xysize     (332, 700)
                draggable  True
                mousewheel True
                vbox:
                    
                    spacing 8
                    for index, char in enumerate(photo_gallery_chars):
                        frame:
                            xysize (330, 110)
                            button:
                                xysize (330, 110)
                                align (.5, .5)

                                focus_mask True

                                action [ SetScreenVariable('sort_state', char['name']), Function(set_preview_values, index), Function(print, [char['name']]) ]

                                image AlphaMask(Transform("gui/msp1/bios/" + str(char['name']) + "/" + str(char['name']) + "_bg.webp", zoom = .175, crop = (0, 0, 1920, 1080)), "gui/msp1/gallery_ui/r/char_plate.png") offset (-6, -6):
                                    at transform:

                                        on idle:
                                            easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                                        on idle:
                                            easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(-.5)

                                image AlphaMask(Transform("gui/msp1/gallery_ui/r/foreground.png", zoom = .755, crop = (0, 800, 1920, 1080)), "gui/msp1/gallery_ui/r/char_plate.png") alpha .7 offset (-6, -6)

                                text char['name'].upper() font "fonts/MiSans-Regular.ttf" align (.0 , 1.0) offset (25, -5) color "#ffffff":
                                    at transform:

                                        subpixel True

                                        on idle:
                                            easein_quint (.5 * persistent.ui_speed_multiplier) zoom 1.0
                                        on hover:
                                            easein_quint (.5 * persistent.ui_speed_multiplier) zoom 1.05
                                at cascade_image_gallery_char(index*.1)
            vbar value YScrollValue ('rc') align (1.0, .5) xysize (8, 700) offset (6, 0)

        # ███╗   ██╗ █████╗ ██╗   ██╗██╗ ██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
        # ████╗  ██║██╔══██╗██║   ██║██║██╔════╝ ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
        # ██╔██╗ ██║███████║██║   ██║██║██║  ███╗███████║   ██║   ██║██║   ██║██╔██╗ ██║
        # ██║╚██╗██║██╔══██║╚██╗ ██╔╝██║██║   ██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
        # ██║ ╚████║██║  ██║ ╚████╔╝ ██║╚██████╔╝██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
        # ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

        frame:
            xysize (345, 220)
            align  (1.0, 1.0)
            offset (6  , 6  )

            vbox:

                spacing 8
                xycenter (.5 , .5)
                
                frame:
                    xysize (345, 107)
                    xycenter (.5, .5)
                    button:

                        xysize (345, 107)
                        xycenter (.5 , .5)
                        
                        focus_mask True

                        action [ SetScreenVariable('sort_state', None), Function(set_preview_values, "default") ]
                        
                        image "gui/msp1/gallery_ui/r/no_filter.png" align (.5, .5):
                            at transform:

                                on idle:

                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#000', '#fff')

                                on hover:

                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#ffb1df', '#fff')

                frame:
                    xysize (345, 107)
                    xycenter (.5 , .5)
                    button:

                        xysize (345, 107)
                        xycenter (.5 , .5)

                        focus_mask True

                        action Return()

                        image "gui/msp1/gallery_ui/r/return.png" align (.5, .5):
                            at transform:

                                on idle:

                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#000', '#fff')

                                on hover:

                                    easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor ColorizeMatrix('#ffb1df', '#fff')
