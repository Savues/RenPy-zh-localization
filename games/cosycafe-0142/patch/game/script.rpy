################################################################################################################################
############ Characters ########################################################################################################

define gui.dialogue_text_outlines = [ (0, "#00000080", 2, 3) ]
define gui.name_text_outlines = [ (0, "#00000080", 2, 3) ]

#----------------- GAME -----------------

define narrator = Character(what_italic=True)
define SayMoney = Character(what_color="#e3e9ff")

define MC = Character("[PlayerName]", color="#0059a7")
define MCi = Character("[PlayerName]", color="#0059a7", what_italic=True)


#----------------- MAIN GIRLS -----------------

define Lucy = Character("露西", color="#d97cd7")
define Victoria = Character("维多利亚", color="#4fb0f0")
define Sarah = Character("莎拉", color="#24ab20")
define Akatsuki = Character("晓月", color="#e31728")
define Rachel = Character("瑞秋", color="#edab1c")
#define Charlotte = Character("Charlotte", color="#fff2c7") Rename to Evelyn / Evie or scarlett/red?
define Hannah = Character("汉娜", color="#80370f")
define Catherine = Character("凯瑟琳", color="#edca6b")
define Elizabeth = Character("伊丽莎白", color="#776de3")
define Ellie = Character("艾莉", color="#776de3")
define Akari = Character("明里", color="#de8a91")
define Taka = Character("高村小姐", color="#fc0377")
define Misaki = Character("美咲", color="#fc0377")
define Headmistress = Character("校长", color="#692460")
define Alison = Character("埃莉森", color="#692460")
define Annabelle = Character("安娜贝尔", color="#ffffff")


#----------------- SIDE CHARACTERS -----------------

define Brian = Character("布莱恩", color="#00ff9d")
define Mika = Character("米卡", color="#ff82ee")
define Chloe = Character("克洛伊", color="#919190")
define Baker = Character("面包师傅", color="#7a3d20")
define Wong = Character("高村先生", color="#7a3d20")
define Danny = Character("丹尼", color="#135a8d")
define Lily = Character("莉莉", color="#1b7519")
define Regi = Character("雷金纳德·贝内特", color="#999571")
define Mary = Character("玛丽·贝内特", color="#805928")
define Cassandra = Character("卡珊德拉·汉密尔顿", color="#00bd8a")
define Hamilton = Character("汉密尔顿先生", color="#8f8e8d")
define Mira = Character("米拉", color="#ffa1b5")
define Akane = Character("茜", color="#592227") #Akatsuki's mother
define Sam = Character("山姆", color="#db87ff")
define Stalker = Character("雅各布·莱利", color="#7a3d20")
define Harriet = Character("哈丽雅特", color="#611b00")
define Gilbert = Character("吉尔伯特先生", color="#5e596e")
define Russell = Character("拉塞尔太太", color="#329973")
define HeadFun = Character("教务干事", color="#19692e")
define MrRussell = Character("拉塞尔先生", color="#164d38")
define Ivy = Character("艾薇", color="#ffa43b") #Younger Sister
define Ella = Character("艾拉", color="#ffc582") #Older Sister
define Eleanor = Character("埃莉诺·汉密尔顿", color="#e80000")
define Mike = Character("迈克", color="#19692e")
define Margaret = Character("玛格丽特", color="#d68800")





#----------------- BACKGROUND CHARACTERS -----------------

define Thug1 = Character("混混1号", color="#00380f")
define Thug2 = Character("混混2号", color="#19692e")
define Goon = Character("丹尼的手下", color="#19692e")
define SexshopGirl = Character("成人用品店的女孩", color="#ff82ee")
define PhoneshopGirl = Character("手机店的女孩", color="#eb0033")
define ClothesshopGirl = Character("服装店的女孩", color="#ffb23e")
define WongWaitress = Character("女服务员", color="#ff82ee")
define Servant = Character("女佣", color="#ff82ee")
define PETeacher = Character("女校体育老师", color="#ff82ee")
define FemaleStudent4 = Character("女学生1号", color="#fa70ff")
define FemaleStudent5 = Character("女学生2号", color="#f600ff")
define FemaleStudent6 = Character("女学生", color="#f5b642")
define DrunkGirl1 = Character("醉酒的女孩", color="#fa70ff")
define AurumHost = Character("女招待", color="#832add")
define AurumWaitress = Character("女服务员", color="#fa70ff")
define Harold = Character("哈罗德·博蒙特", color="#420080")
define Tori = Character("托里", color="#fa70ff")
define Handyman = Character("维修工", color="#00380f")
define DeliveryGuy = Character("送货员", color="#0063bf")
define DeputyFun = Character("干事", color="#408d55")
define Penelope = Character("佩内洛普", color="#fa70ff")
define CouncilSecretary1 = Character("学生会书记", color="#fa70ff")
define CouncilSecretary2 = Character("学生会书记", color="#ff5b5b")



#----------------- UNKNOWN CHARACTERS -----------------

define MissTakamuraUnknown = Character("老师", color="#fc0377")
define RachelUnknown = Character("女学生", color="#edab1c")
define LucyWho = Character("???", color="#d97cd7")
define VictoriaWho = Character("???", color="#4fb0f0")
define SarahWho = Character("女孩", color="#24ab20")
define MaleStudent1 = Character("男学生1号", color="#00ff9d")
define MaleStudent2 = Character("男学生2号", color="#1b6b30")
define MaleStudent3 = Character("男学生", color="#00380f")
define FemaleStudent1 = Character("女学生1号", color="#4fb0f0")
define FemaleStudent2 = Character("女学生2号", color="#80370f")
define FemaleStudent3 = Character("女学生3号", color="#ff82ee")
define UnknownTeacher = Character("女性", color="#692460")
define WongUnknown = Character("男性", color="#7a3d20")
define AkatsukiUnknown = Character("女孩", color="#e31728")
define LucyMother = Character("露西的母亲", color="#7a3d20")
define SarahSis1 = Character("金发妹妹", color="#e0ff82")
define SarahSis2 = Character("棕发妹妹", color="#ffa1b5") #Mira
define LadyUnknown = Character("女士", color="#1b7519")
define CassandraUnknown = Character("女性", color="#00bd8a")
define AnnabelleUnknown = Character("白发少女", color="#ffffff")
define PizzaGirl = Character("披萨店的女孩", color="#edca6b")
define UniversityGirl = Character("女孩", color="#db87ff")
define AkaneUnknown = Character("神秘女士", color="#592227")
define DrunkSam = Character("醉酒的女孩2", color="#db87ff")
define YoungerSister = Character("妹妹", color="#ffa43b")
define OlderGirl = Character("姐姐", color="#ffc582")
define HaroldUnknown = Character("店主", color="#420080")
define MargaretUnknown = Character("老奶奶", color="#d68800")

#----------------- CHARACTER COMBOS -----------------

define AlisonVicky = Character("{color=#692460}埃莉森{/color} & {color=#4fb0f0}维多利亚{/color}", color="#ffffff")
define MCLily = Character("{color=#0059a7}[PlayerName]{/color} & {color=#1b7519}莉莉{/color}", color="#ffffff")
define MCAkari = Character("{color=#0059a7}[PlayerName]{/color} & {color=#de8a91}明里{/color}", color="#ffffff")
define CatherineHannah = Character("{color=#edca6b}凯瑟琳{/color} & {color=#80370f}汉娜{/color}", color="#ffffff")
define SarahVicky = Character("{color=#24ab20}莎拉{/color} & {color=#4fb0f0}维多利亚{/color}", color="#ffffff")
define AkatsukiVicky = Character("{color=#e31728}晓月{/color} & {color=#4fb0f0}维多利亚{/color}", color="#ffffff")
define AkatsukiSarah = Character("{color=#e31728}晓月{/color} & {color=#24ab20}莎拉{/color}", color="#ffffff")
define CouncilSecretary12 = Character("{color=#ff5b5b}学生会书记{/color} & {color=#fa70ff}学生会书记{/color}", color="#ffffff")

#----------------- PHONE/TEXT -----------------

define Phone = Character("手机", color="#ffffff")
define Alarm = Character("闹钟", color="#e3392d")

define MCPhone = Character("[PlayerName]", color="#0059a7")
define SarahPhone = Character("莎拉", color="#24ab20")
define HarrietPhone = Character("哈丽雅特", color="#611b00")

define MCText = Character("短信 - [PlayerName]", color="#0059a7", who_italic=True)
define UnknownNumber = Character("短信 - 未知号码", color="#808080", who_italic=True)
define VictoriaText = Character("短信 - 维多利亚", color="#4fb0f0", who_italic=True)
define SarahText = Character("短信 - 莎拉", color="#24ab20", who_italic=True)
define CatherineText = Character("短信 - 凯瑟琳", color="#edca6b", who_italic=True)
define MisakiText = Character("短信 - 美咲", color="#fc0377", who_italic=True)
define LucyText = Character("短信 - 露西", color="#d97cd7", who_italic=True)
define AkatsukiText = Character("短信 - 晓月", color="#e31728", who_italic=True)
define AkariText = Character("短信 - 明里", color="#de8a91", who_italic=True)


################################################################################################################################
############ VIDEOS ############################################################################################################

# 0.1
image vid_main10_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.1/vid_main10_1.webm", start_image="vid_main10_1_start")
image vid_main10_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.1/vid_main10_2.webm", start_image="vid_main10_2_start")
image vid_main10_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.1/vid_main10_3.webm", start_image="vid_main10_3_start")
image vid_main10_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.1/vid_main10_4.webm", start_image="vid_main10_4_start")
image vid_main10_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.1/vid_main10_5.webm", start_image="vid_main10_5_start")
image vid_main10_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.1/vid_main10_6.webm", start_image="vid_main10_6_start")
image vid_main11_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.1/vid_main11_1.webm", start_image="vid_main11_1_start")
image vid_main11_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.1/vid_main11_2.webm", start_image="vid_main11_2_start")
image vid_main11_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.1/vid_main11_3.webm", start_image="vid_main11_3_start")
image vid_main11_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.1/vid_main11_4.webm", start_image="vid_main11_4_start")

# 0.2
image vid_main11_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_5.webm", start_image="vid_main11_5_start")
image vid_main11_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_6.webm", start_image="vid_main11_6_start")
image vid_main11_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_7.webm", start_image="vid_main11_7_start")
image vid_main11_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_8.webm", start_image="vid_main11_8_start")
image vid_main11_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_9.webm", start_image="vid_main11_9_start")
image vid_main11_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_10.webm", start_image="vid_main11_10_start")
image vid_main11_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_11.webm", start_image="vid_main11_11_start")
image vid_main11_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_12.webm", start_image="vid_main11_12_start")
image vid_main11_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_13.webm", start_image="vid_main11_13_start")
image vid_main11_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_14.webm", start_image="vid_main11_14_start")
image vid_main11_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_15.webm", start_image="vid_main11_15_start")
image vid_main11_16 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_16.webm", start_image="vid_main11_16_start")
image vid_main11_17 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_17.webm", start_image="vid_main11_17_start")
image vid_main11_18 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_18.webm", start_image="vid_main11_18_start")
image vid_main11_19 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_19.webm", start_image="vid_main11_19_start")
image vid_main11_20 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_20.webm", start_image="vid_main11_20_start")
image vid_main11_21 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_21.webm", start_image="vid_main11_21_start")
image vid_main11_22 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_22.webm", start_image="vid_main11_22_start")
image vid_main11_23 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_23.webm", start_image="vid_main11_23_start")
image vid_main11_24 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_24.webm", start_image="vid_main11_24_start")
image vid_main11_25 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_25.webm", start_image="vid_main11_25_start")
image vid_main11_26 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_26.webm", start_image="vid_main11_26_start")
image vid_main11_27 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.2/vid_main11_27.webm", start_image="vid_main11_27_start")

# 0.3
image vid_main13_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_1.webm", start_image="vid_main13_1_start")
image vid_main13_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_2.webm", start_image="vid_main13_2_start")
image vid_main13_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_3.webm", start_image="vid_main13_3_start")
image vid_main13_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_4.webm", start_image="vid_main13_4_start")
image vid_main13_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_5.webm", start_image="vid_main13_5_start")
image vid_main13_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_6.webm", start_image="vid_main13_6_start")
image vid_main13_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_7.webm", start_image="vid_main13_7_start")
image vid_main13_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_8.webm", start_image="vid_main13_8_start")
image vid_main13_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_9.webm", start_image="vid_main13_9_start")
image vid_main13_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_10.webm", start_image="vid_main13_10_start")
image vid_main13_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_11.webm", start_image="vid_main13_11_start")
image vid_main13_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main13_12.webm", start_image="vid_main13_12_start")

image vid_main14_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main14_1.webm", start_image="vid_main14_1_start")
image vid_main14_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main14_2.webm", start_image="vid_main14_2_start")
image vid_main14_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main14_3.webm", start_image="vid_main14_3_start")
image vid_main14_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main14_4.webm", start_image="vid_main14_4_start")
image vid_main14_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main14_5.webm", start_image="vid_main14_5_start")
image vid_main14_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main14_6.webm", start_image="vid_main14_6_start")
image vid_main14_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.3/vid_main14_7.webm", start_image="vid_main14_7_start")

# 0.4
image vid_main15_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_1.webm", start_image="vid_main15_1_start")
image vid_main15_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_2.webm", start_image="vid_main15_2_start")
image vid_main15_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_3.webm", start_image="vid_main15_3_start")
image vid_main15_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_4.webm", start_image="vid_main15_4_start")
image vid_main15_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_5.webm", start_image="vid_main15_5_start")
image vid_main15_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_6.webm", start_image="vid_main15_6_start")
image vid_main15_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_7.webm", start_image="vid_main15_7_start")
image vid_main15_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_8.webm", start_image="vid_main15_8_start")
image vid_main15_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_9.webm", start_image="vid_main15_9_start")
image vid_main15_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_10.webm", start_image="vid_main15_10_start")
image vid_main15_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_11.webm", start_image="vid_main15_11_start")
image vid_main15_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_12.webm", start_image="vid_main15_12_start")
image vid_main15_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_13.webm", start_image="vid_main15_13_start")
image vid_main15_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_14.webm", start_image="vid_main15_14_start")
image vid_main15_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_15.webm", start_image="vid_main15_15_start")
image vid_main15_16 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_16.webm", start_image="vid_main15_16_start")
image vid_main15_17 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_17.webm", start_image="vid_main15_17_start")
image vid_main15_18 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_18.webm", start_image="vid_main15_18_start")
image vid_main15_19 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_19.webm", start_image="vid_main15_19_start")
image vid_main15_20 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_20.webm", start_image="vid_main15_20_start")
image vid_main15_21 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.4/vid_main15_21.webm", start_image="vid_main15_21_start")

# 0.5
image vid_main16_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_1.webm", start_image="vid_main16_1_start")
image vid_main16_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_2.webm", start_image="vid_main16_2_start")
image vid_main16_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_3.webm", start_image="vid_main16_3_start")
image vid_main16_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_4.webm", start_image="vid_main16_4_start")
image vid_main16_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_5.webm", start_image="vid_main16_5_start")
image vid_main16_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_6.webm", start_image="vid_main16_6_start")
image vid_main16_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_7.webm", start_image="vid_main16_7_start")
image vid_main16_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_8.webm", start_image="vid_main16_8_start")
image vid_main16_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_9.webm", start_image="vid_main16_9_start")
image vid_main16_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_10.webm", start_image="vid_main16_10_start")
image vid_main16_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_11.webm", start_image="vid_main16_11_start")
image vid_main16_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_12.webm", start_image="vid_main16_12_start")
image vid_main16_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_13.webm", start_image="vid_main16_13_start")
image vid_main16_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main16_14.webm", start_image="vid_main16_14_start")

image vid_main17_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_1.webm", start_image="vid_main17_1_start")
image vid_main17_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_2.webm", start_image="vid_main17_2_start")
image vid_main17_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_3.webm", start_image="vid_main17_3_start")
image vid_main17_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_4.webm", start_image="vid_main17_4_start")
image vid_main17_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_5.webm", start_image="vid_main17_5_start")
image vid_main17_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_6.webm", start_image="vid_main17_6_start")
image vid_main17_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_7.webm", start_image="vid_main17_7_start")
image vid_main17_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_8.webm", start_image="vid_main17_8_start")
image vid_main17_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_9.webm", start_image="vid_main17_9_start")
image vid_main17_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_10.webm", start_image="vid_main17_10_start")
image vid_main17_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.5/vid_main17_11.webm", start_image="vid_main17_11_start")

# 0.6
image vid_main18_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_1.webm", start_image="vid_main18_1_start")
image vid_main18_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_2.webm", start_image="vid_main18_2_start")
image vid_main18_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_3.webm", start_image="vid_main18_3_start")
image vid_main18_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_4.webm", start_image="vid_main18_4_start")
image vid_main18_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_5.webm", start_image="vid_main18_5_start")
image vid_main18_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_6.webm", start_image="vid_main18_6_start")
image vid_main18_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_7.webm", start_image="vid_main18_7_start")
image vid_main18_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_8.webm", start_image="vid_main18_8_start")
image vid_main18_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_9.webm", start_image="vid_main18_9_start")
image vid_main18_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_10.webm", start_image="vid_main18_10_start")
image vid_main18_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_11.webm", start_image="vid_main18_11_start")
image vid_main18_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_12.webm", start_image="vid_main18_12_start")
image vid_main18_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_13.webm", start_image="vid_main18_13_start")
image vid_main18_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_14.webm", start_image="vid_main18_14_start")
image vid_main18_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_15.webm", start_image="vid_main18_15_start")
image vid_main18_16 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.6/vid_main18_16.webm", start_image="vid_main18_16_start")

# 0.7
image vid_main19_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_1.webm", start_image="vid_main19_1_start")
image vid_main19_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_2.webm", start_image="vid_main19_2_start")
image vid_main19_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_3.webm", start_image="vid_main19_3_start")
image vid_main19_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_4.webm", start_image="vid_main19_4_start")
image vid_main19_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_5.webm", start_image="vid_main19_5_start")
image vid_main19_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_6.webm", start_image="vid_main19_6_start")
image vid_main19_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_7.webm", start_image="vid_main19_7_start")
image vid_main19_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_8.webm", start_image="vid_main19_8_start")
image vid_main19_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_9.webm", start_image="vid_main19_9_start")
image vid_main19_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_10.webm", start_image="vid_main19_10_start")
image vid_main19_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.7/vid_main19_11.webm", start_image="vid_main19_11_start")

# 0.8
image vid_main21_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_1.webm", start_image="vid_main21_1_start")
image vid_main21_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_2.webm", start_image="vid_main21_2_start")
image vid_main21_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_3.webm", start_image="vid_main21_3_start")
image vid_main21_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_4.webm", start_image="vid_main21_4_start")
image vid_main21_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_5.webm", start_image="vid_main21_5_start")
image vid_main21_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_6.webm", start_image="vid_main21_6_start")
image vid_main21_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_7.webm", start_image="vid_main21_7_start")
image vid_main21_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_8.webm", start_image="vid_main21_8_start")
image vid_main21_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_9.webm", start_image="vid_main21_9_start")
image vid_main21_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_10.webm", start_image="vid_main21_10_start")
image vid_main21_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_11.webm", start_image="vid_main21_11_start")
image vid_main21_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_12.webm", start_image="vid_main21_12_start")
image vid_main21_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_13.webm", start_image="vid_main21_13_start")
image vid_main21_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_14.webm", start_image="vid_main21_14_start")
image vid_main21_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.8/vid_main21_15.webm", start_image="vid_main21_15_start")

# 0.9
image vid_main22_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_1.webm", start_image="vid_main22_1_start")
image vid_main22_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_2.webm", start_image="vid_main22_2_start")
image vid_main22_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_3.webm", start_image="vid_main22_3_start")
image vid_main22_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_4.webm", start_image="vid_main22_4_start")
image vid_main22_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_5.webm", start_image="vid_main22_5_start")
image vid_main22_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_6.webm", start_image="vid_main22_6_start")
image vid_main22_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_7.webm", start_image="vid_main22_7_start")
image vid_main22_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_8.webm", start_image="vid_main22_8_start")
image vid_main22_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_9.webm", start_image="vid_main22_9_start")
image vid_main22_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_10.webm", start_image="vid_main22_10_start")
image vid_main22_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_11.webm", start_image="vid_main22_11_start", loop = False, keep_last_frame = True)
image vid_main22_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_12.webm", start_image="vid_main22_12_start")
image vid_main22_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_13.webm", start_image="vid_main22_13_start")
image vid_main22_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_14.webm", start_image="vid_main22_14_start")
image vid_main22_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_15.webm", start_image="vid_main22_15_start")
image vid_main22_16 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_16.webm", start_image="vid_main22_16_start")
image vid_main22_17 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_17.webm", start_image="vid_main22_17_start")
image vid_main22_18 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_18.webm", start_image="vid_main22_18_start")
image vid_main22_19 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_19.webm", start_image="vid_main22_19_start")
image vid_main22_20 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_20.webm", start_image="vid_main22_20_start")
image vid_main22_21 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_21.webm", start_image="vid_main22_21_start")
image vid_main22_22 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_22.webm", start_image="vid_main22_22_start")
image vid_main22_23 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_23.webm", start_image="vid_main22_23_start")
image vid_main22_24 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_24.webm", start_image="vid_main22_24_start")
image vid_main22_25 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_25.webm", start_image="vid_main22_25_start")
image vid_main22_26 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_26.webm", start_image="vid_main22_26_start", loop = False, keep_last_frame = True)
image vid_main22_27 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main22_27.webm", start_image="vid_main22_27_start")

image vid_main23_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_1.webm", start_image="vid_main23_1_start")
image vid_main23_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_2.webm", start_image="vid_main23_2_start")
image vid_main23_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_3.webm", start_image="vid_main23_3_start")
image vid_main23_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_4.webm", start_image="vid_main23_4_start")
image vid_main23_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_5.webm", start_image="vid_main23_5_start")
image vid_main23_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_6.webm", start_image="vid_main23_6_start")
image vid_main23_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_7.webm", start_image="vid_main23_7_start")
image vid_main23_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_8.webm", start_image="vid_main23_8_start")
image vid_main23_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_9.webm", start_image="vid_main23_9_start")
image vid_main23_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_10.webm", start_image="vid_main23_10_start")
image vid_main23_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_11.webm", start_image="vid_main23_11_start")
image vid_main23_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_12.webm", start_image="vid_main23_12_start")
image vid_main23_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_13.webm", start_image="vid_main23_13_start")
image vid_main23_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.9/vid_main23_14.webm", start_image="vid_main23_14_start")

# 0.10
image vid_main24_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_1.webm", start_image="vid_main24_1_start")
image vid_main24_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_2.webm", start_image="vid_main24_2_start")
image vid_main24_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_3.webm", start_image="vid_main24_3_start")
image vid_main24_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_4.webm", start_image="vid_main24_4_start")
image vid_main24_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_5.webm", start_image="vid_main24_5_start")
image vid_main24_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_6.webm", start_image="vid_main24_6_start")
image vid_main24_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_7.webm", start_image="vid_main24_7_start")
image vid_main24_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_8.webm", start_image="vid_main24_8_start")
image vid_main24_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_9.webm", start_image="vid_main24_9_start")
image vid_main24_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_10.webm", start_image="vid_main24_10_start")
image vid_main24_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_11.webm", start_image="vid_main24_11_start")
image vid_main24_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_12.webm", start_image="vid_main24_12_start")
image vid_main24_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_13.webm", start_image="vid_main24_13_start")
image vid_main24_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_14.webm", start_image="vid_main24_14_start")
image vid_main24_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_15.webm", start_image="vid_main24_15_start")
image vid_main24_16 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main24_16.webm", start_image="vid_main24_16_start", loop = False, keep_last_frame = True)

image vid_main25_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_1.webm", start_image="vid_main25_1_start", loop = False, keep_last_frame = True)
image vid_main25_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_2.webm", start_image="vid_main25_2_start")
image vid_main25_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_3.webm", start_image="vid_main25_3_start")
image vid_main25_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_4.webm", start_image="vid_main25_4_start")
image vid_main25_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_5.webm", start_image="vid_main25_5_start")
image vid_main25_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_6.webm", start_image="vid_main25_6_start")
image vid_main25_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_7.webm", start_image="vid_main25_7_start")
image vid_main25_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_8.webm", start_image="vid_main25_8_start")
image vid_main25_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_9.webm", start_image="vid_main25_9_start")
image vid_main25_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_10.webm", start_image="vid_main25_10_start")
image vid_main25_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_11.webm", start_image="vid_main25_11_start")
image vid_main25_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_12.webm", start_image="vid_main25_12_start")
image vid_main25_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_13.webm", start_image="vid_main25_13_start", loop = False, keep_last_frame = True)
image vid_main25_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_14.webm", start_image="vid_main25_14_start")
image vid_main25_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.10/vid_main25_15.webm", start_image="vid_main25_15_start", loop = False, keep_last_frame = True)

# 0.11
image vid_main26_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_1.webm", start_image="vid_main26_1_start")
image vid_main26_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_2.webm", start_image="vid_main26_2_start")
image vid_main26_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_3.webm", start_image="vid_main26_3_start")
image vid_main26_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_4.webm", start_image="vid_main26_4_start")
image vid_main26_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_5.webm", start_image="vid_main26_5_start")
image vid_main26_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_6.webm", start_image="vid_main26_6_start", loop = False, keep_last_frame = True)
image vid_main26_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_7.webm", start_image="vid_main26_7_start")
image vid_main26_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_8.webm", start_image="vid_main26_8_start")
image vid_main26_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_9.webm", start_image="vid_main26_9_start")
image vid_main26_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_10.webm", start_image="vid_main26_10_start")
image vid_main26_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_11.webm", start_image="vid_main26_11_start")
image vid_main26_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_12.webm", start_image="vid_main26_12_start")
image vid_main26_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_13.webm", start_image="vid_main26_13_start")
image vid_main26_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_14.webm", start_image="vid_main26_14_start")
image vid_main26_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_15.webm", start_image="vid_main26_15_start")
image vid_main26_16 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_16.webm", start_image="vid_main26_16_start")
image vid_main26_17 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_17.webm", start_image="vid_main26_17_start", loop = False, keep_last_frame = True)
image vid_main26_18 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_18.webm", start_image="vid_main26_18_start")
image vid_main26_19 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_19.webm", start_image="vid_main26_19_start")
image vid_main26_20 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_20.webm", start_image="vid_main26_20_start")
image vid_main26_21 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_21.webm", start_image="vid_main26_21_start")
image vid_main26_22 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_22.webm", start_image="vid_main26_22_start")
image vid_main26_23 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_23.webm", start_image="vid_main26_23_start")
image vid_main26_24 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_24.webm", start_image="vid_main26_24_start")
image vid_main26_25 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_25.webm", start_image="vid_main26_25_start")
image vid_main26_26 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_26.webm", start_image="vid_main26_26_start")
image vid_main26_27 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_27.webm", start_image="vid_main26_27_start")

image vid_main26_28 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_28.webm", start_image="vid_main26_28_start")
image vid_main26_29 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_29.webm", start_image="vid_main26_29_start")
image vid_main26_30 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_30.webm", start_image="vid_main26_30_start")
image vid_main26_31 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_31.webm", start_image="vid_main26_31_start")
image vid_main26_32 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_32.webm", start_image="vid_main26_32_start")
image vid_main26_33 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_33.webm", start_image="vid_main26_33_start")
image vid_main26_34 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_34.webm", start_image="vid_main26_34_start")
image vid_main26_35 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_35.webm", start_image="vid_main26_35_start")
image vid_main26_36 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_36.webm", start_image="vid_main26_36_start")
image vid_main26_37 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_37.webm", start_image="vid_main26_37_start")
image vid_main26_38 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_38.webm", start_image="vid_main26_38_start")
image vid_main26_39 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_39.webm", start_image="vid_main26_39_start")
image vid_main26_40 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_40.webm", start_image="vid_main26_40_start")
image vid_main26_41 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_41.webm", start_image="vid_main26_41_start")
image vid_main26_42 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_42.webm", start_image="vid_main26_42_start")
image vid_main26_43 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_43.webm", start_image="vid_main26_43_start")
image vid_main26_44 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_44.webm", start_image="vid_main26_44_start")
image vid_main26_45 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_45.webm", start_image="vid_main26_45_start")
image vid_main26_46 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_46.webm", start_image="vid_main26_46_start")
image vid_main26_47 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_47.webm", start_image="vid_main26_47_start")
image vid_main26_48 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_48.webm", start_image="vid_main26_48_start")
image vid_main26_49 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_49.webm", start_image="vid_main26_49_start")
image vid_main26_50 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_50.webm", start_image="vid_main26_50_start")
image vid_main26_51 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_51.webm", start_image="vid_main26_51_start")
image vid_main26_52 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_52.webm", start_image="vid_main26_52_start")
image vid_main26_53 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_53.webm", start_image="vid_main26_53_start")
image vid_main26_54 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_54.webm", start_image="vid_main26_54_start")
image vid_main26_55 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_55.webm", start_image="vid_main26_55_start")
image vid_main26_56 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_56.webm", start_image="vid_main26_56_start")
image vid_main26_57 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_57.webm", start_image="vid_main26_57_start")
image vid_main26_58 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_58.webm", start_image="vid_main26_58_start")
image vid_main26_59 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_59.webm", start_image="vid_main26_59_start")
image vid_main26_60 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_60.webm", start_image="vid_main26_60_start")
image vid_main26_61 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_61.webm", start_image="vid_main26_61_start")
image vid_main26_62 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_62.webm", start_image="vid_main26_62_start")
image vid_main26_63 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_63.webm", start_image="vid_main26_63_start")
image vid_main26_64 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_64.webm", start_image="vid_main26_64_start", loop = False, keep_last_frame = True)
image vid_main26_65 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_65.webm", start_image="vid_main26_65_start")
image vid_main26_66 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_66.webm", start_image="vid_main26_66_start")
image vid_main26_67 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_67.webm", start_image="vid_main26_67_start")
image vid_main26_68 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_68.webm", start_image="vid_main26_68_start")
image vid_main26_69 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.11/vid_main26_69.webm", start_image="vid_main26_69_start", loop = False, keep_last_frame = True)

# 0.12
image vid_main27_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_1.webm", start_image="vid_main27_1_start")
image vid_main27_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_2.webm", start_image="vid_main27_2_start")
image vid_main27_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_3.webm", start_image="vid_main27_3_start")
image vid_main27_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_4.webm", start_image="vid_main27_4_start")
image vid_main27_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_5.webm", start_image="vid_main27_5_start")
image vid_main27_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_6.webm", start_image="vid_main27_6_start")
image vid_main27_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_7.webm", start_image="vid_main27_7_start")
image vid_main27_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_8.webm", start_image="vid_main27_8_start")
image vid_main27_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_9.webm", start_image="vid_main27_9_start")
image vid_main27_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_10.webm", start_image="vid_main27_10_start")
image vid_main27_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_11.webm", start_image="vid_main27_11_start")
image vid_main27_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_12.webm", start_image="vid_main27_12_start")
image vid_main27_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_13.webm", start_image="vid_main27_13_start")
image vid_main27_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main27_14.webm", start_image="vid_main27_14_start")

image vid_main28_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_1.webm", start_image="vid_main28_1_start")
image vid_main28_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_2.webm", start_image="vid_main28_2_start")
image vid_main28_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_3.webm", start_image="vid_main28_3_start")
image vid_main28_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_4.webm", start_image="vid_main28_4_start")
image vid_main28_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_5.webm", start_image="vid_main28_5_start")
image vid_main28_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_6.webm", start_image="vid_main28_6_start")
image vid_main28_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_7.webm", start_image="vid_main28_7_start")
image vid_main28_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_8.webm", start_image="vid_main28_8_start")
image vid_main28_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_9.webm", start_image="vid_main28_9_start")
image vid_main28_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_10.webm", start_image="vid_main28_10_start")
image vid_main28_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_11.webm", start_image="vid_main28_11_start")
image vid_main28_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_12.webm", start_image="vid_main28_12_start")
image vid_main28_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_13.webm", start_image="vid_main28_13_start")
image vid_main28_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_14.webm", start_image="vid_main28_14_start")
image vid_main28_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_15.webm", start_image="vid_main28_15_start")
image vid_main28_16 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_16.webm", start_image="vid_main28_16_start")
image vid_main28_17 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_17.webm", start_image="vid_main28_17_start")
image vid_main28_18 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_18.webm", start_image="vid_main28_18_start")
image vid_main28_19 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_19.webm", start_image="vid_main28_19_start")
image vid_main28_20 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_20.webm", start_image="vid_main28_20_start")
image vid_main28_21 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_21.webm", start_image="vid_main28_21_start")
image vid_main28_22 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_22.webm", start_image="vid_main28_22_start")
image vid_main28_23 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_23.webm", start_image="vid_main28_23_start")
image vid_main28_24 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_24.webm", start_image="vid_main28_24_start")
image vid_main28_25 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_25.webm", start_image="vid_main28_25_start")
image vid_main28_26 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_26.webm", start_image="vid_main28_26_start")
image vid_main28_27 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_27.webm", start_image="vid_main28_27_start")
image vid_main28_28 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_28.webm", start_image="vid_main28_28_start")
image vid_main28_29 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_29.webm", start_image="vid_main28_29_start")
image vid_main28_30 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.12/vid_main28_30.webm", start_image="vid_main28_30_start", loop = False, keep_last_frame = True)

# 0.13
image vid_main29_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_1.webm", start_image="vid_main29_1_start")
image vid_main29_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_2.webm", start_image="vid_main29_2_start")
image vid_main29_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_3.webm", start_image="vid_main29_3_start")
image vid_main29_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_4.webm", start_image="vid_main29_4_start")
image vid_main29_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_5.webm", start_image="vid_main29_5_start")
image vid_main29_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_6.webm", start_image="vid_main29_6_start")
image vid_main29_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_7.webm", start_image="vid_main29_7_start")
image vid_main29_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_8.webm", start_image="vid_main29_8_start")
image vid_main29_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_9.webm", start_image="vid_main29_9_start")
image vid_main29_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_10.webm", start_image="vid_main29_10_start")
image vid_main29_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_11.webm", start_image="vid_main29_11_start")
image vid_main29_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_12.webm", start_image="vid_main29_12_start")
image vid_main29_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_13.webm", start_image="vid_main29_13_start")
image vid_main29_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_14.webm", start_image="vid_main29_14_start", loop = False, keep_last_frame = True)
image vid_main29_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_15.webm", start_image="vid_main29_15_start")
image vid_main29_16 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_16.webm", start_image="vid_main29_16_start")
image vid_main29_17 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_17.webm", start_image="vid_main29_17_start")
image vid_main29_18 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_18.webm", start_image="vid_main29_18_start")
image vid_main29_19 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_19.webm", start_image="vid_main29_19_start")
image vid_main29_20 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_20.webm", start_image="vid_main29_20_start")
image vid_main29_21 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_21.webm", start_image="vid_main29_21_start")
image vid_main29_22 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_22.webm", start_image="vid_main29_22_start")
image vid_main29_23 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_23.webm", start_image="vid_main29_23_start")
image vid_main29_24 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_24.webm", start_image="vid_main29_24_start")
image vid_main29_25 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_25.webm", start_image="vid_main29_25_start")
image vid_main29_26 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_26.webm", start_image="vid_main29_26_start")
image vid_main29_27 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_27.webm", start_image="vid_main29_27_start")
image vid_main29_28 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_28.webm", start_image="vid_main29_28_start")
image vid_main29_29 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main29_29.webm", start_image="vid_main29_29_start", loop = False, keep_last_frame = True)

image vid_main30_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_1.webm", start_image="vid_main30_1_start")
image vid_main30_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_2.webm", start_image="vid_main30_2_start")
image vid_main30_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_3.webm", start_image="vid_main30_3_start")
image vid_main30_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_4.webm", start_image="vid_main30_4_start")
image vid_main30_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_5.webm", start_image="vid_main30_5_start")
image vid_main30_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_6.webm", start_image="vid_main30_6_start")
image vid_main30_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_7.webm", start_image="vid_main30_7_start")
image vid_main30_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_8.webm", start_image="vid_main30_8_start")
image vid_main30_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_9.webm", start_image="vid_main30_9_start")
image vid_main30_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_10.webm", start_image="vid_main30_10_start")
image vid_main30_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_11.webm", start_image="vid_main30_11_start")
image vid_main30_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_12.webm", start_image="vid_main30_12_start")
image vid_main30_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_13.webm", start_image="vid_main30_13_start")
image vid_main30_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_14.webm", start_image="vid_main30_14_start")
image vid_main30_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_15.webm", start_image="vid_main30_15_start")
image vid_main30_16 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_16.webm", start_image="vid_main30_16_start", loop = False, keep_last_frame = True)
image vid_main30_17 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_17.webm", start_image="vid_main30_17_start")
image vid_main30_18 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_18.webm", start_image="vid_main30_18_start")
image vid_main30_19 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_19.webm", start_image="vid_main30_19_start")
image vid_main30_20 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_20.webm", start_image="vid_main30_20_start")
image vid_main30_21 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_21.webm", start_image="vid_main30_21_start")
image vid_main30_22 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_22.webm", start_image="vid_main30_22_start")
image vid_main30_23 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_23.webm", start_image="vid_main30_23_start")
image vid_main30_24 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_24.webm", start_image="vid_main30_24_start")
image vid_main30_25 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_25.webm", start_image="vid_main30_25_start")
image vid_main30_26 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_26.webm", start_image="vid_main30_26_start")
image vid_main30_27 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_27.webm", start_image="vid_main30_27_start")
image vid_main30_28 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_28.webm", start_image="vid_main30_28_start")
image vid_main30_29 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_29.webm", start_image="vid_main30_29_start")
image vid_main30_30 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_30.webm", start_image="vid_main30_30_start")
image vid_main30_31 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_31.webm", start_image="vid_main30_31_start")
image vid_main30_32 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_32.webm", start_image="vid_main30_32_start")
image vid_main30_33 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_33.webm", start_image="vid_main30_33_start")
image vid_main30_34 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_34.webm", start_image="vid_main30_34_start")
image vid_main30_35 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_35.webm", start_image="vid_main30_35_start")
image vid_main30_36 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_36.webm", start_image="vid_main30_36_start")
image vid_main30_37 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_37.webm", start_image="vid_main30_37_start")
image vid_main30_38 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_38.webm", start_image="vid_main30_38_start")
image vid_main30_39 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_39.webm", start_image="vid_main30_39_start")
image vid_main30_40 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_40.webm", start_image="vid_main30_40_start")
image vid_main30_41 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_41.webm", start_image="vid_main30_41_start")
image vid_main30_42 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_42.webm", start_image="vid_main30_42_start")
image vid_main30_43 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_43.webm", start_image="vid_main30_43_start")
image vid_main30_44 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_44.webm", start_image="vid_main30_44_start")
image vid_main30_45 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_45.webm", start_image="vid_main30_45_start")
image vid_main30_46 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_46.webm", start_image="vid_main30_46_start")
image vid_main30_47 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_47.webm", start_image="vid_main30_47_start")
image vid_main30_48 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_48.webm", start_image="vid_main30_48_start")
image vid_main30_49 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_49.webm", start_image="vid_main30_49_start")
image vid_main30_50 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_50.webm", start_image="vid_main30_50_start")
image vid_main30_51 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_51.webm", start_image="vid_main30_51_start")
image vid_main30_52 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_52.webm", start_image="vid_main30_52_start")
image vid_main30_53 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_53.webm", start_image="vid_main30_53_start")
image vid_main30_54 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_54.webm", start_image="vid_main30_54_start")
image vid_main30_55 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.13/vid_main30_55.webm", start_image="vid_main30_55_start")

# 0.14
image vid_main32_1 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_1.webm", start_image="vid_main32_1_start")
image vid_main32_2 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_2.webm", start_image="vid_main32_2_start")
image vid_main32_3 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_3.webm", start_image="vid_main32_3_start")
image vid_main32_4 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_4.webm", start_image="vid_main32_4_start")
image vid_main32_5 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_5.webm", start_image="vid_main32_5_start")
image vid_main32_6 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_6.webm", start_image="vid_main32_6_start")
image vid_main32_7 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_7.webm", start_image="vid_main32_7_start")
image vid_main32_8 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_8.webm", start_image="vid_main32_8_start")
image vid_main32_9 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_9.webm", start_image="vid_main32_9_start")
image vid_main32_10 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_10.webm", start_image="vid_main32_10_start")
image vid_main32_11 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_11.webm", start_image="vid_main32_11_start")
image vid_main32_12 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_12.webm", start_image="vid_main32_12_start")
image vid_main32_13 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_13.webm", start_image="vid_main32_13_start")
image vid_main32_14 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_14.webm", start_image="vid_main32_14_start")
image vid_main32_15 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_15.webm", start_image="vid_main32_15_start")
image vid_main32_16 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_16.webm", start_image="vid_main32_16_start")
image vid_main32_17 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_17.webm", start_image="vid_main32_17_start")
image vid_main32_18 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_18.webm", start_image="vid_main32_18_start")
image vid_main32_19 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_19.webm", start_image="vid_main32_19_start")
image vid_main32_20 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_20.webm", start_image="vid_main32_20_start")
image vid_main32_21 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_21.webm", start_image="vid_main32_21_start")
image vid_main32_22 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_22.webm", start_image="vid_main32_22_start")
image vid_main32_23 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_23.webm", start_image="vid_main32_23_start")
image vid_main32_24 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_24.webm", start_image="vid_main32_24_start")
image vid_main32_25 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_25.webm", start_image="vid_main32_25_start")
image vid_main32_26 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_26.webm", start_image="vid_main32_26_start")
image vid_main32_27 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_27.webm", start_image="vid_main32_27_start")
image vid_main32_28 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_28.webm", start_image="vid_main32_28_start")
image vid_main32_29 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_29.webm", start_image="vid_main32_29_start")
image vid_main32_30 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_30.webm", start_image="vid_main32_30_start")
image vid_main32_31 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_31.webm", start_image="vid_main32_31_start")
image vid_main32_32 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_32.webm", start_image="vid_main32_32_start")
image vid_main32_33 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_33.webm", start_image="vid_main32_33_start")
image vid_main32_34 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_34.webm", start_image="vid_main32_34_start")
image vid_main32_35 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_35.webm", start_image="vid_main32_35_start")
image vid_main32_36 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_36.webm", start_image="vid_main32_36_start")
image vid_main32_37 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_37.webm", start_image="vid_main32_37_start")
image vid_main32_38 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_38.webm", start_image="vid_main32_38_start")
image vid_main32_39 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_39.webm", start_image="vid_main32_39_start")
image vid_main32_40 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_40.webm", start_image="vid_main32_40_start")
image vid_main32_41 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_41.webm", start_image="vid_main32_41_start")
image vid_main32_42 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_42.webm", start_image="vid_main32_42_start")
image vid_main32_43 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_43.webm", start_image="vid_main32_43_start")
image vid_main32_44 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_44.webm", start_image="vid_main32_44_start")
image vid_main32_45 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_45.webm", start_image="vid_main32_45_start")
image vid_main32_46 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_46.webm", start_image="vid_main32_46_start")
image vid_main32_47 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_47.webm", start_image="vid_main32_47_start")
image vid_main32_48 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_48.webm", start_image="vid_main32_48_start")
image vid_main32_49 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_49.webm", start_image="vid_main32_49_start")
image vid_main32_50 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_50.webm", start_image="vid_main32_50_start")
image vid_main32_51 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_51.webm", start_image="vid_main32_51_start")
image vid_main32_52 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_52.webm", start_image="vid_main32_52_start")
image vid_main32_53 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_53.webm", start_image="vid_main32_53_start")
image vid_main32_54 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_54.webm", start_image="vid_main32_54_start")
image vid_main32_55 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_55.webm", start_image="vid_main32_55_start")
image vid_main32_56 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_56.webm", start_image="vid_main32_56_start")
image vid_main32_57 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_57.webm", start_image="vid_main32_57_start")
image vid_main32_58 = Movie(size=(1920,1080), channel="movie", play="images/videos/0.14/vid_main32_58.webm", start_image="vid_main32_58_start")




################################################################################################################################
############ AUDIO #############################################################################################################

#///////// MUSIC

# Home:
    # "someday_in_your_summer.mp3"
    # play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
# School:
    # "autumn_days.mp3"
    # play music "audio/bgm/school.mp3" loop fadeout 1.0 fadein 1.0
# Sad:
    # "footsteps_of_autumn.mp3"
    # play music "audio/bgm/sad.mp3" loop fadeout 1.0 fadein 1.0
# Fight:
    # "challenge_time.mp3"
    # play music "audio/bgm/fight.mp3" loop fadeout 1.0 fadein 1.0
# Night:
    # "sparks_of_the_night_wind.mp3"
    # play music "audio/bgm/night.mp3" loop fadeout 1.0 fadein 1.0
# Sexy:
    # "deep_breath_of_sunset.mp3"
    # play music "audio/bgm/sexy.mp3" loop fadeout 1.0 fadein 1.0
# Train:
    # "rainy_season.mp3"
    # play music "audio/bgm/train.mp3" loop fadeout 1.0 fadein 1.0
# Working:
    # "illumination.mp3"
    # play music "audio/bgm/working.mp3" loop fadeout 1.0 fadein 1.0
# Date:
    # "morning.mp3"
    # play music "audio/bgm/date.mp3" loop fadeout 1.0 fadein 3.0 volume 0.6
# Sinister:
    # "betreyal.mp3"
    # play music "audio/bgm/sinister.mp3" loop fadeout 1.0 fadein 3.0 volume 1.0
# Confrontation:
    # "crammer_rock.mp3"
    # play music "audio/bgm/confrontation.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
# Date_Lucy:
    # "sentimental_light.mp3"
    # play music "audio/bgm/date_lucy.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
# Headmistress:
    # "wholeheartedly.mp3"
    # play music "audio/bgm/headmistress.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
# Sarah's House:
    # "Classical Beauty main.wav"
    # play music "audio/bgm/sarah_house.mp3" loop fadeout 1.0 fadein 1.0 volume 2.4
# Sarah's theme:
    # "memories.mp3"
    # play music "audio/bgm/sarah_bedroom.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
# Founding Party:
    # "politeness_of_the_butler.mp3"
    # play music "audio/bgm/founding_party.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
# Akatsuki Sad:
    # "in_the_basket.mp3.mp3"
    # play music "audio/bgm/akatsuki_sad.mp3" loop fadeout 1.0 fadein 1.0 volume 2.0
# Miss Takamura's Theme:
    # "the_truth_spirited_away.mp3"
    # play music "audio/bgm/taka_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
# Maid Town:
    # "leva-eternity-149473.mp3"
    # play music "audio/bgm/maid_town.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
#Lucy's Theme
    # play music "audio/bgm/lucy_theme.mp3" loop volume 1.2 fadeout 1.0 fadein 1.0
#Victoria's Theme
    # play music "audio/bgm/victoria_theme.mp3" loop volume 1.0 fadeout 1.0 fadein 1.0
#Akatsuki's Theme
    # play music "audio/bgm/akatsuki_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
#Alison's theme
    # play music "audio/bgm/alison_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0
#Hannah's theme
    # play music "audio/bgm/hannah_theme.mp3" loop fadeout 1.0 fadein 1.0 volume 1.0

#///////// SOUNDS
# Train:
    # play sound "audio/sounds/train.mp3" loop fadeout 1.0 fadein 1.0

# TRAIN
# play music "audio/bgm/train.mp3" loop fadeout 1.0 fadein 1.0
# play ambiance "audio/ambiance/train.mp3" loop fadein 1.0

# CAFETERIA
# play sound "audio/sounds/cafeteria.mp3" loop fadein 1.0 volume 0.7

# MISC
# play sound "audio/sounds/camera.wav"


#    play music "audio/bgm/founding_party.mp3" loop fadeout 1.0 fadein 1.0 volume 0.5
#    play ambiance "audio/ambiance/dinnerparty.mp3" loop fadein 1.0 volume 0.4

#############################
default flash = Fade(.15, 0, .5, color="#fff")




# ----- START ----------------------------------------------------------------------------------------------------------------------------------------
label start:

    $ DateTime_Show = False

    call variables from _call_variables
    # call DailyStats
    call flags from _call_flags

    $ PlayerName = renpy.input("请输入你的名字：", default="杰克", length=15)

    $ persistent.replay_PlayerName = PlayerName


    #window hide
    scene img_opening12 with fade
    pause
    scene img_black with dissolve
    
    call screen story_sel

    return

label start_day2:
    $ DateTime_Show = True
    $ Day = 2
    $ CurrentWeekDay = 6
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_2

label start_day3:
    $ DateTime_Show = True
    $ Day = 3
    $ CurrentWeekDay = 0
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_3

label start_day4:
    $ DateTime_Show = True
    $ Day = 4
    $ CurrentWeekDay = 1
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_4

label start_day5:
    $ DateTime_Show = True
    $ Day = 5
    $ CurrentWeekDay = 2
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_5

label start_day6:
    $ DateTime_Show = True
    $ Day = 6
    $ CurrentWeekDay = 3
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_6

label start_day7:
    $ DateTime_Show = True
    $ Day = 7
    $ CurrentWeekDay = 4
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_7

label start_day8:
    $ DateTime_Show = True
    $ Day = 8
    $ CurrentWeekDay = 5
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_8

label start_day9:
    $ DateTime_Show = True
    $ Day = 9
    $ CurrentWeekDay = 6
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_9

label start_day10:
    $ DateTime_Show = True
    $ Day = 10
    $ CurrentWeekDay = 0
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_10

label start_day11:
    $ DateTime_Show = True
    $ Day = 11
    $ CurrentWeekDay = 1
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_11

label start_day12:
    $ DateTime_Show = True
    $ Day = 12
    $ CurrentWeekDay = 2
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_12

label start_day13:
    $ DateTime_Show = True
    $ Day = 13
    $ CurrentWeekDay = 3
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_13

label start_day14:
    $ DateTime_Show = True
    $ Day = 14
    $ CurrentWeekDay = 4
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_14

label start_day15:
    $ DateTime_Show = True
    $ Day = 15
    $ CurrentWeekDay = 5
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_15

label start_day16:
    $ DateTime_Show = True
    $ Day = 16
    $ CurrentWeekDay = 6
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_16

label start_day17:
    $ DateTime_Show = True
    $ Day = 17
    $ CurrentWeekDay = 0
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_17

label start_day18:
    $ DateTime_Show = True
    $ Day = 18
    $ CurrentWeekDay = 1
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_18

label start_day19:
    $ DateTime_Show = True
    $ Day = 19
    $ CurrentWeekDay = 2
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_19

label start_day20:
    $ DateTime_Show = True
    $ Day = 20
    $ CurrentWeekDay = 3
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_20

label start_day21:
    $ DateTime_Show = True
    $ Day = 21
    $ CurrentWeekDay = 4
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_21

label start_day22:
    $ DateTime_Show = True
    $ Day = 22
    $ CurrentWeekDay = 5
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_22

label start_day23:
    $ DateTime_Show = True
    $ Day = 23
    $ CurrentWeekDay = 6
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_23

label start_day24:
    $ DateTime_Show = True
    $ Day = 24
    $ CurrentWeekDay = 0
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_24

label start_day25:
    $ DateTime_Show = True
    $ Day = 25
    $ CurrentWeekDay = 1
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_25

label start_day26:
    $ DateTime_Show = True
    $ Day = 26
    $ CurrentWeekDay = 2
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/akatsuki_theme.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_26

label start_day27:
    $ DateTime_Show = True
    $ Day = 27
    $ CurrentWeekDay = 3
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_27

label start_day28:
    $ DateTime_Show = True
    $ Day = 28
    $ CurrentWeekDay = 4
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/catherine_theme.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_28

label start_day29:
    $ DateTime_Show = True
    $ Day = 29
    $ CurrentWeekDay = 5
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_29

label start_day30:
    $ DateTime_Show = True
    $ Day = 30
    $ CurrentWeekDay = 6
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_30

label start_day31:
    $ DateTime_Show = True
    $ Day = 1
    $ CurrentWeekDay = 0
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    $ Month = "Oct"
    play music "audio/bgm/victoria_sadness.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_31

label start_day32:
    $ DateTime_Show = True
    $ Day = 2
    $ CurrentWeekDay = 1
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]
    $ Month = "Oct"
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0
    jump event_main_32

label start_beginning:

    $ DateTime_Show = True

    scene img_main1_1 with fade
    # $ CurrentLocation = "home_front"

    play music "audio/bgm/home.mp3" loop #fadein 1.0
    play ambiance "audio/ambiance/birds.mp3" loop fadein 1.0 volume 0.25

    MCi "（我终于到了。这里是我的咖啡馆。）"
    scene img_main1_2 with dissolve
    MCi "（本该是个「小小」的咖啡馆——爷爷留给我时就是这么说的，可这地方居然这么大！）"
    scene img_main1_3 with dissolve
    MCi "（真奇怪，他从来没跟我提过这件事？）"
    MCi "（恐怕永远不会知道了。现在它是我的了，我只要专心把它经营起来就好。）"
    MCi "（可惜我手头没多少启动资金，所以要忙的事多得很。尤其我还得把一半时间浪费在去新学校的路上。）"
    MCi "（反正再读一年学校又有什么意义？我早就知道自己想做什么了。）"
    MCi "（我要用从爷爷那里学来的超凡厨艺，开出一家史上最棒的餐厅！）"
    MCi "（不过眼下第一步，是把这地方变成一家能正常营业的咖啡馆。学校的事，等周一开学再操心不迟。）"
    scene img_main1_4 with dissolve
    MCi "（我该趁天还没黑先进去看看。从今往后我就住这儿了，希望能找到一张床，最好是别太脏、也不太潮的那种。）"

    $ persistent.victoria_img_main6_386_unlocked = True

    jump event_main_1

# ----- END --------------------------------------------------------------------------------------------------------------------------------------
    
label afterword:
    stop sound
    play music "audio/bgm/home.mp3" loop fadeout 1.0 fadein 1.0



#######################################################################################################################
# Photo Gallery Unlocks

#Lucy
    $ persistent.lucy_img_main8_201_unlocked = False
    $ persistent.lucy_img_main08_201_unlocked = True

    $ persistent.lucy_img_main17_324_unlocked = True

#Victoria
    $ persistent.victoria_img_main6_386_unlocked = False
    $ persistent.victoria_img_main06_386_unlocked = True

    $ persistent.victoria_img_main8_202_unlocked = False
    $ persistent.victoria_img_main08_202_unlocked = True

    $ persistent.victoria_img_main8_203_unlocked = False
    $ persistent.victoria_img_main08_203_unlocked = True

    $ persistent.victoria_img_main12_20_unlocked = True
    $ persistent.victoria_img_main12_21_unlocked = True
    $ persistent.victoria_img_main12_22_unlocked = True
    $ persistent.victoria_img_main12_261_unlocked = True
    $ persistent.victoria_img_main13_187_unlocked = True
    $ persistent.victoria_img_main13_188_unlocked = True
    $ persistent.victoria_img_main17_318_unlocked = True
    $ persistent.victoria_img_main27_1104_unlocked = True

#Akatsuki
    $ persistent.akatsuki_img_main21_796_unlocked = True
    $ persistent.akatsuki_img_main27_1105_unlocked = True

#Sarah
    $ persistent.sarah_img_main17_361_unlocked = True
    $ persistent.sarah_img_main17_362_unlocked = True
    $ persistent.sarah_img_main20_366_unlocked = True
    $ persistent.sarah_img_main20_369_unlocked = True
    $ persistent.sarah_img_main20_373_unlocked = True
    $ persistent.sarah_img_main20_374_unlocked = True
    $ persistent.sarah_img_main20_375_unlocked = True
    $ persistent.sarah_img_main20_378_unlocked = True
    $ persistent.sarah_img_main20_379_unlocked = True
    $ persistent.sarah_img_main20_382_unlocked = True
    $ persistent.sarah_img_main20_383_unlocked = True
    $ persistent.sarah_img_main20_384_unlocked = True
    $ persistent.sarah_img_main20_385_unlocked = True
    $ persistent.sarah_img_main20_390_unlocked = True
    $ persistent.sarah_img_main23_400_unlocked = True
    $ persistent.sarah_img_main28_780_unlocked = True
    $ persistent.sarah_img_main28_781_unlocked = True
    $ persistent.sarah_img_main28_782_unlocked = True
    $ persistent.sarah_img_main28_783_unlocked = True
    $ persistent.sarah_img_main28_788_unlocked = True
    $ persistent.sarah_img_main28_789_unlocked = True
    $ persistent.sarah_img_main28_790_unlocked = True
    $ persistent.sarah_img_main28_791_unlocked = True
    $ persistent.sarah_img_main28_794_unlocked = True
    $ persistent.sarah_img_main28_800_unlocked = True
    $ persistent.sarah_img_main28_801_unlocked = True
    $ persistent.sarah_img_main28_802_unlocked = True
    $ persistent.sarah_img_main28_803_unlocked = True
    $ persistent.sarah_img_main28_804_unlocked = True
    $ persistent.sarah_img_main28_808_unlocked = True
    $ persistent.sarah_img_main28_812_unlocked = True
    $ persistent.sarah_img_main28_813_unlocked = True
    $ persistent.sarah_img_main28_814_unlocked = True
    $ persistent.sarah_img_main28_815_unlocked = True
    $ persistent.sarah_img_main28_816_unlocked = True
    $ persistent.sarah_img_main28_819_unlocked = True
    $ persistent.sarah_img_main28_820_unlocked = True
    $ persistent.sarah_img_main28_832_unlocked = True
    $ persistent.sarah_img_main28_833_unlocked = True
    $ persistent.sarah_img_main28_835_unlocked = True
    $ persistent.sarah_img_main28_836_unlocked = True
    $ persistent.sarah_img_main28_915_unlocked = True
    $ persistent.sarah_img_main28_927_unlocked = True
    $ persistent.sarah_img_main28_928_unlocked = True
    $ persistent.sarah_img_main28_929_unlocked = True
    $ persistent.sarah_img_main28_936_unlocked = True
    $ persistent.sarah_img_main28_937_unlocked = True

#Catherine
    $ persistent.catherine_img_main23_683_unlocked = True
    $ persistent.catherine_img_main24_933_unlocked = True
    $ persistent.catherine_img_main24_934_unlocked = True
    $ persistent.catherine_img_main25_774_unlocked = True
    $ persistent.catherine_img_main25_778_unlocked = True
    $ persistent.catherine_img_main26_1183_unlocked = True
    $ persistent.catherine_img_main27_1207_unlocked = True
    $ persistent.catherine_img_main28_645_unlocked = True
    $ persistent.catherine_img_main29_1127_unlocked = True
    $ persistent.catherine_img_main29_1128_unlocked = True
    $ persistent.catherine_img_main30_719_unlocked = True

#Hannah
    $ persistent.hannah_img_main27_241_unlocked = True

#Alison
    $ persistent.alison_img_main17_158_unlocked = True

#Misaki
    $ persistent.misaki_img_main26_349_unlocked = True
    $ persistent.misaki_img_main27_595_unlocked = True
    $ persistent.misaki_img_main27_596_unlocked = True
    $ persistent.misaki_img_main28_643_unlocked = True
    $ persistent.misaki_img_main28_644_unlocked = True
    $ persistent.misaki_img_main30_558_unlocked = True
    $ persistent.misaki_img_main32_217_unlocked = True
    $ persistent.misaki_img_main32_833_unlocked = True
    $ persistent.misaki_img_main32_834_unlocked = True
    $ persistent.misaki_img_main32_835_unlocked = True

#Rachel

#Akari
    $ persistent.akari_img_main32_50_unlocked = True

#Elizabeth

#Group
    $ persistent.group_img_main16_144_unlocked = True
    $ persistent.group_img_main17_331_unlocked = True
    $ persistent.group_img_main21_673_unlocked = True
    $ persistent.group_img_main23_608_unlocked = True
    $ persistent.group_img_main25_916_unlocked = True
    $ persistent.group_img_main29_867_unlocked = True
    $ persistent.group_img_main29_1160_unlocked = True
    $ persistent.group_img_main29_1164_unlocked = True
    $ persistent.group_img_main30_373_unlocked = True


#######################################################################################################################
# Replay Gallery Unlocks

    $ persistent.gallery_lucy1 = True
    $ persistent.gallery_lucy2 = True
    $ persistent.gallery_lucy3 = True
    $ persistent.gallery_lucy4 = True
    $ persistent.gallery_lucy5 = True
    $ persistent.gallery_lucy6 = True
    $ persistent.gallery_lucy7 = True
    $ persistent.gallery_lucy8 = True
    $ persistent.gallery_victoria1 = True
    $ persistent.gallery_victoria2 = True
    $ persistent.gallery_victoria3 = True
    $ persistent.gallery_victoria4 = True
    $ persistent.gallery_victoria5 = True
    $ persistent.gallery_akatsuki1 = True
    $ persistent.gallery_akatsuki2 = True
    $ persistent.gallery_akatsuki3 = True
    $ persistent.gallery_akatsuki4 = True
    $ persistent.gallery_akatsuki5 = True
    $ persistent.gallery_akatsuki6 = True
    $ persistent.gallery_akatsuki7 = True
    $ persistent.gallery_akatsuki8 = True
    $ persistent.gallery_akatsuki9 = True
    $ persistent.gallery_headmistress1 = True
    $ persistent.gallery_headmistress2 = True
    $ persistent.gallery_taka1 = True
    $ persistent.gallery_taka2 = True
    $ persistent.gallery_taka3 = True
    $ persistent.gallery_catherine1 = True
    $ persistent.gallery_group1 = True
    $ persistent.gallery_group2 = True
    $ persistent.gallery_group3 = True
    $ persistent.gallery_group4 = True
    $ persistent.gallery_group5 = True

#######################################################################################################################
# Character Bio Unlocks

#Lucy
    $ persistent.characters_lucy = True
    $ persistent.characters_lucy_name = True
    $ persistent.characters_lucy_job1 = True
    $ persistent.characters_lucy_job2 = True
    $ persistent.characters_lucy_family1 = True
    $ persistent.characters_lucy_family2 = True
    $ persistent.characters_lucy_note1 = True
    $ persistent.characters_lucy_note2 = True
    $ persistent.characters_lucy_note3 = True

#Victoria
    $ persistent.characters_victoria = True
    $ persistent.characters_victoria_name = True
    $ persistent.characters_victoria_job1 = True
    $ persistent.characters_victoria_job2 = True
    $ persistent.characters_victoria_family1 = True
    $ persistent.characters_victoria_family2 = True
    $ persistent.characters_victoria_family3 = True
    $ persistent.characters_victoria_note1 = True
    $ persistent.characters_victoria_note2 = True
    $ persistent.characters_victoria_note3 = True
    $ persistent.characters_victoria_note4 = True

#Sarah
    $ persistent.characters_sarah = True
    $ persistent.characters_sarah_foundingfamily = True
    $ persistent.characters_sarah_job1 = True
    $ persistent.characters_sarah_job2 = True
    $ persistent.characters_sarah_family1 = True
    $ persistent.characters_sarah_family2 = True
    $ persistent.characters_sarah_family3 = True
    $ persistent.characters_sarah_note1 = True
    $ persistent.characters_sarah_note2 = True
    $ persistent.characters_sarah_note3 = True
    $ persistent.characters_sarah_note4 = True

#Akatsuki
    $ persistent.characters_akatsuki = True
    $ persistent.characters_akatsuki_job1 = True
    $ persistent.characters_akatsuki_job2 = True
    $ persistent.characters_akatsuki_family1 = True
    $ persistent.characters_akatsuki_family4 = True
    $ persistent.characters_akatsuki_family3 = True
    $ persistent.characters_akatsuki_family2 = True
    $ persistent.characters_akatsuki_note1 = True
    $ persistent.characters_akatsuki_note2 = True
    $ persistent.characters_akatsuki_note3 = True
    $ persistent.characters_akatsuki_note4 = True

#Rachel
    $ persistent.characters_rachel = True
    $ persistent.characters_rachel_job1 = True
    $ persistent.characters_rachel_note1 = True
    $ persistent.characters_rachel_note2 = True
    $ persistent.characters_rachel_note3 = True
    $ persistent.characters_rachel_note4 = True

#Hannah
    $ persistent.characters_hannah = True
    $ persistent.characters_hannah_foundingfamily = True
    $ persistent.characters_hannah_job1 = True
    $ persistent.characters_hannah_family1 = True
    $ persistent.characters_hannah_family2 = True
    $ persistent.characters_hannah_note1 = True
    $ persistent.characters_hannah_note2 = True
    $ persistent.characters_hannah_note3 = True

#Headmistress
    $ persistent.characters_headmistress = True
    $ persistent.characters_headmistress_name = True
    $ persistent.characters_headmistress_foundingfamily = True
    $ persistent.characters_headmistress_job1 = True
    $ persistent.characters_headmistress_family1 = True
    $ persistent.characters_headmistress_family2 = True
    $ persistent.characters_headmistress_note1 = True
    $ persistent.characters_headmistress_note2 = True
    $ persistent.characters_headmistress_note3 = True
    $ persistent.characters_headmistress_note4 = True

#Taka
    $ persistent.characters_taka = True
    $ persistent.characters_taka_name = True
    $ persistent.characters_taka_job1 = True
    $ persistent.characters_taka_family1 = True
    $ persistent.characters_taka_note1 = True
    $ persistent.characters_taka_note2 = True
    $ persistent.characters_taka_note3 = True
    $ persistent.characters_taka_note4 = True


#Akari
    $ persistent.characters_akari = True
    $ persistent.characters_akari_note1 = True

#Catherine
    $ persistent.characters_catherine = True
    $ persistent.characters_catherine_foundingfamily = True
    $ persistent.characters_catherine_family1 = True
    $ persistent.characters_catherine_note1 = True
    $ persistent.characters_catherine_note2 = True
    $ persistent.characters_catherine_note3 = True
    $ persistent.characters_catherine_note4 = True
    $ persistent.characters_catherine_note5 = True

#Elizabeth
    $ persistent.characters_elizabeth = True
    $ persistent.characters_elizabeth_note1 = True
    $ persistent.characters_elizabeth_note2 = True

#Annabelle
    $ persistent.characters_annabelle = True
    $ persistent.characters_annabelle_note1 = True


#Side Characters
    $ persistent.characters_mika = True
    $ persistent.characters_brian = True
    $ persistent.characters_brian_foundingfamily = True
    $ persistent.characters_brian_note1 = True
    $ persistent.characters_brian_note2 = True
    $ persistent.characters_lenny = True
    $ persistent.characters_baker = True
    $ persistent.characters_baker_note1 = True
    $ persistent.characters_wong = True
    $ persistent.characters_lucymother = True
    $ persistent.characters_lucymother_note1 = True
    $ persistent.characters_chloe = True
    $ persistent.characters_danny = True
    $ persistent.characters_lily = True
    $ persistent.characters_lily_note1 = True
    $ persistent.characters_lily_note2 = True
    $ persistent.characters_hamilton = True
    $ persistent.characters_cassandra = True
    $ persistent.characters_mary = True
    $ persistent.characters_regi = True
    $ persistent.characters_sis1 = True
    $ persistent.characters_sis2 = True
    $ persistent.characters_sis2_note1 = True
    $ persistent.characters_sis2_note2 = True
    $ persistent.characters_sis2_name = True
    $ persistent.characters_samantha = True
    $ persistent.characters_harriet = True
    $ persistent.characters_harriet_note1 = True
    $ persistent.characters_gilbert = True
    $ persistent.characters_gilbert_note1 = True
    $ persistent.characters_gloria = True
    $ persistent.characters_russell = True
    $ persistent.characters_regi_note1 = True
    $ persistent.characters_akane = True
    $ persistent.characters_ella = True
    $ persistent.characters_ivy = True
    $ persistent.characters_headfun = True
    $ persistent.characters_headfun_sister = True
    $ persistent.characters_eleanor = True

# Afterword
    scene img_black with fade
    scene to_be_continued with fade
    pause
    jump afterword2
label afterword2:
    scene afterword_14 with dissolve
    pause
    jump credits
label credits:
    scene credits_14 with dissolve
    pause
    jump afterword2
    
    return



