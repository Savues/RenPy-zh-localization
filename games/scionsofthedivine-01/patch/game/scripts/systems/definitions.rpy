init offset = -2

#Who/What######################################################################
define syst = Character(" ", what_italic=True)
define unkn = Character("？？？", color="？？？")
define scrn = Character(None, screen="center_say")
#Main##########################################################################
define ever = Character("众人", color="#ffffff")
define toge = Character("众人", color="#ffffff")
define mc = Character("[mc_name]", color="#d386ff")
define mcdad = Character("爸爸", color="#00a72c")
define mcmom = Character("妈妈", color="#aa2fcf")
define sara = Character("莎拉", color="#a3c4df")
define layl = Character("莱拉", color="#d8cf51")
define asta = Character("阿斯塔拉", color="#468dcf")
define chri = Character("克里斯汀", color="#39c979")
define mela = Character("梅拉妮", color="#cc3c3c")
define king = Character("纳索斯国王", color="#008b0c")
define queen = Character("安妮丝女王", color="#4db0bd")
define vero = Character("维罗妮卡", color="#665c3c")
define soul = Character("索尔", color="#9c3bb9")
define sila = Character("塞拉斯", color="#a36e4f")
define rayn = Character("雷恩", color="#e770c3")
define kate = Character("凯特", color="#75ccdb")
define layldad = Character("莱拉的爸爸", color="#b46600")
define laylmom = Character("莱拉的妈妈", color="#6a8343")
define scif = Character("里昂", color="#ff7300")
define eddi = Character("埃迪", color="#297cc9")
define barth = Character("巴思", color="#919191")
define ash = Character("阿什", color="#660000")
define rile = Character("莱利", color="#bdb762")
#Others########################################################################
define bart = Character("酒保", color="#91719b")
define prim = Character("{purplemagic}？？？{/purplemagic}", color="#ffffff", what_font=zh_rune_font, what_prefix="{purplemagic}", what_suffix="{/purplemagic}")
define prim2 = Character("{purplemagic}？？？{/purplemagic}", color="#ffffff", what_prefix="{purplemagic}", what_suffix="{/purplemagic}")
define prim3 = Character("{purplemagic}原初者{/purplemagic}", color="#ffffff", what_prefix="{purplemagic}", what_suffix="{/purplemagic}")
define sentl = Character("守望者", color="#94006f")
define sentm = Character("守望者", color="#007694")
define ssent = Character("守望者", color="#3158ac")
define nurs = Character("护士", color="#ffffff")
define teac = Character("老师", color="#866743")
define bul1 = Character("混混 1", color="#4480a8")
define bul2 = Character("混混 2", color="#47724b")
define bul3 = Character("混混 3", color="#7e654b")
define bulsn = Character("混混们", color="#5e6a8b")
define clerk = Character("店员", color="#797979")
define saram = Character("莎拉的妈妈", color="#6682b6")
define inter = Character("广播", color="#993333")
define tlg = Character("最后的真神", color="#dab22f")
define resh = Character("雷什蒙", color="#dab22f")
define saut = Character("自动系统", color="#ffffff")
#Player Names###################################################################
default mc_name = "Flynn"
default takenfirstnames = [chara[char].name for char in chara if char != "mc"]
#GUI############################################################################
define gui_nullbutton = False
define mm_var = False
default persistent.theme_color = '#0066cc'
default effect_color = '#0066cc'
default persistent.outfit_selections = {}
default all_characters_order = {}
default persistent.save_names = {}
#Gameplay#######################################################################
default persistent.profiles = []
default persistent.profiles_unlocked = []
default persistent.unlocked_outfits = {}
default persistent.unlocked_memories = {}
default persistent.outfit_selections = {}
default persistent.notifications_unlocks = True
default persistent.walkthrough_mode = False
default persistent.dev_menu = False
#Story##########################################################################
#Layl
default layldinner = False
default layl_shoppingoutfits = 0
default laylconfess = False
default layl_postponesex = False
#Asta
default asta_rayn_eavesdrop = False
default asta_lonely = 0
default asta_lonely_c4 = False
#Chri

#Vero

#Mela

#Soul
default soul_sd = False
#Rayne
default rayngw = False
#Sila

#Primordial

#Transitions####################################################################
define mdiss = { "master" : Dissolve(0.5) }
define mdism = { "master" : Dissolve(1) }
define mdisl = { "master" : Dissolve(2) }
define mfadeb = { "master" : Fade(0.25, 0.5, 0.25, color="#000000") }
define mfadew = { "master" : Fade(0.5, 0.0, 0.5, color="#ffffff") }
define mhpunch = { "master" : Move((15, 0), (-15, 0), .20, bounce=True, repeat=True, delay=0.275)}
define diss = Dissolve(0.5)
define dism = Dissolve(1.0)
define disl = Dissolve(3.0)
define fadeb = Fade(0.5, 1.0, 0.5, color="#000000")
define fadew = Fade(0.5, 0.0, 0.5, color="#ffffff")
define hpunch = Move((15, 0), (-15, 0), .20, bounce=True, repeat=True, delay=0.275)
define hpunchr = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=3.0)
define hpunchs = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=1.0)
define hpunchs2 = Move((15, 0), (-15, 0), .20, bounce=True, repeat=True, delay=1.0)
define splashdis = Dissolve(1.0)
define splashdis2 = Dissolve(0.5)
define grunge = ImageDissolve("images/dissolvers/grunge.jpg", 1.0)
define grunger = ImageDissolve("images/dissolvers/grunge.jpg", 1.0, reverse=True)
define staticflow = ImageDissolve("images/dissolvers/staticflow.jpg", 3.0)
define pushl = PushMove(0.2, "pushleft")
define pushr = PushMove(0.2, "pushright")
#Transforms#######################################################################
transform blink:
    alpha 1.0
    linear 1.0 alpha 0.2
    linear 1.0 alpha 1.0
    repeat
transform wing_flap:
    subpixel True
    xalign 0.5 yalign 0.5 alpha 0.0 xzoom 0.0 yzoom 0.8
    pause 0.75
    easein 0.5 zoom 1.0 alpha 1.0 xzoom 1.0 yzoom 1.0
transform theme_ember:
    matrixcolor TintMatrix(persistent.theme_color) 
transform colored_ember:
    matrixcolor TintMatrix(effect_color) 
transform text_glow:
    matrixcolor TintMatrix(persistent.theme_color) * BrightnessMatrix(1.0)
    additive 1.0
    blur 15.0
    alpha 1.0
    xoffset -4
transform zoomshake:
    zoom 1.5 align (0.5, 0.5)
    parallel:
        easein 0.5 zoom 1.0
transform magic_glow:
    matrixcolor TintMatrix("#4aaeff") * OpacityMatrix(1.0) * BrightnessMatrix(0.2)
    linear 1.0 matrixcolor TintMatrix("#ffffff") * OpacityMatrix(1.0) * BrightnessMatrix(0.0)
transform pref_buttons:
    on idle:
        linear 0.2 matrixcolor TintMatrix("#00000000") * BrightnessMatrix(0.0)
    on hover:
        linear 0.5 matrixcolor TintMatrix("#ffffff00") * BrightnessMatrix(0.1)
transform scrollbars_color:
    on idle:
        linear 0.2 matrixcolor TintMatrix(persistent.theme_color) * BrightnessMatrix(0.0)
    on hover:
        linear 0.5 matrixcolor TintMatrix(persistent.theme_color) * BrightnessMatrix(0.1)
transform slidein_left(delay=0.0):
    xoffset 200
    alpha 0.0
    pause delay
    linear 0.3 xoffset 0 alpha 0.7
    linear 0.1 xoffset 12 alpha 0.9
    linear 0.1 xoffset 0 alpha 1.0
    on idle:
        linear 0.1 xoffset 0
    on hover:
        linear 0.1 xoffset -12
transform shiftr_hover:
    align (0.5, 0.5)
    on idle:
        linear 0.1 zoom 1.0 xoffset 0
    on hover:
        linear 0.1 zoom 1.1 xoffset 12
transform shiftl_hover:
    align (0.5, 0.5)
    on idle:
        linear 0.1 xoffset 0
    on hover:
        linear 0.1 xoffset -12
transform shiftu_hover:
    align (0.5, 0.5)
    on idle:
        linear 0.1 zoom 1.0 yoffset 0
    on insensitive:
        linear 0.1 zoom 1.0 yoffset 0
    on hover:
        linear 0.1 zoom 1.1 yoffset -6
transform center_hover:
    align (0.5, 0.5)
    on idle:
        linear 0.1 zoom 1.0  matrixcolor TintMatrix("#ffffffff") * BrightnessMatrix(0.0)
    on hover:
        linear 0.1 zoom 1.1 matrixcolor TintMatrix("#ffffffff") * BrightnessMatrix(0.5)
transform center_hover2:
    align (0.5, 0.5)
    on idle:
        linear 0.1 zoom 1.0
    on hover:
        linear 0.1 zoom 1.1
transform memory_hover:
    align (0.5, 0.5)
    yoffset -13
    on idle:
        linear 0.1 zoom 1.0
    on hover:
        linear 0.1 zoom 1.1
transform memory_hover_glow:
    align (0.5, 0.5)
    on idle:
        linear 0.1 zoom 1.0 additive 0.0 blur 0.0 alpha 0.0 matrixcolor TintMatrix(persistent.theme_color) * BrightnessMatrix(1.0),
    on hover:
        linear 0.1 zoom 1.116 additive 2.0 blur 5.0 alpha 1.0 matrixcolor TintMatrix(persistent.theme_color) * BrightnessMatrix(1.0),
transform save_hover:
    align (0.5, 0.5)
    yoffset 6
    yoffset 6
    on idle:
        linear 0.1 zoom 1.0
    on hover:
        linear 0.1 zoom 1.1
transform portrait_transform:
    xoffset 500
    linear 0.5 xoffset 0
transform bio_transform:
    xoffset -500
    linear 0.5 xoffset 0
transform bio_transform2:
    xoffset -500
    linear 0.1 xoffset -500
    linear 0.5 xoffset 0
transform bio_transform3:
    xoffset -500
    linear 0.2 xoffset -500
    linear 0.5 xoffset 0
transform bio_transform4:
    xoffset -500
    linear 0.3 xoffset -500
    linear 0.5 xoffset 0
transform bio_transform5:
    xoffset -500
    linear 0.4 xoffset -500
    linear 0.5 xoffset 0
#Videos#######################################################################
#image c1p1s1 l = Movie(play="videos/layl_intro.webm", loop=False)
#image c1p2s1 17a = Movie(play="videos/chri_intro.webm", loop=False)
#image c1p2s3 22b = Movie(play="videos/vero_intro.webm", loop=False)
#image c1p2s3 27a = Movie(play="videos/asta_intro.webm", loop=False)
image c1p6b1s1 v1 = Movie(play="videos/rayngw1.webm", loop=True)
image c1p6b1s1 v2 = Movie(play="videos/rayngw2.webm", loop=True)
image c1p7b1s1 v1 = Movie(play="videos/laylconfess1.webm", loop=True)
image c1p7b1s1 v2 = Movie(play="videos/laylconfess2.webm", loop=True)
image c1p7b1s1 v3 = Movie(play="videos/laylconfess3.webm", loop=True)