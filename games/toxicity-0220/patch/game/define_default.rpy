define config.gestures = {
    "n" : "game_menu",
    "s" : "hide_windows",
    "w" : "rollback",
    "e" : "skip"
    }

default persistent.dialogueBoxOpacity = 1.0

define j = Character("[player_name]", color="#99ffcc")
define jm = Character("[player_name]", color="#99ffcc", what_font="fonts/msyh.ttc", what_size=70)
define o = Character("奥蒂斯", color="#d6d6d6")
define om = Character("奥蒂斯", color="#d6d6d6", what_font="fonts/msyh.ttc", what_size=70)
define tv = Character("电视", color="#d6d6d6")
define ch = Character("查尔斯", color="#d6d6d6")
define u = Character("？？？？", color="#d6d6d6")
define k = Character("卡莉", color="#ffcccc")
define l = Character("劳拉", color="#66ff33")
define s = Character("雪莉", color="#8bc7ff")
define e = Character("伊芙", color="#EEF527")
define a = Character("安妮", color="#8bc7ff")
define r = Character("劳尔", color="#F22F07")
define g1 = Character("女孩1号", color="#d6d6d6")
define g2 = Character("女孩2号", color="#d6d6d6")
define an = Character("安德鲁", color="#d6d6d6")
define anm = Character("安德鲁", color="#d6d6d6", what_font="fonts/msyh.ttc", what_size=70)
define ke = Character("基思", color="#d6d6d6")
define b1 = Character("大学男生", color="#d6d6d6")
define na = Character("南希", color="FBD1FF")
define naw = Character("南希", color="FBD1FF", what_font="fonts/msyh.ttc", what_size=70)
define cr = Character("？？？？", color="#ff6666", what_font="fonts/msyh.ttc", what_size=70)
define hor = Character(" ", color="#ff6666", what_font="fonts/msyh.ttc", what_size=70)
define w = Character("？？？？", color="#FF0000", what_font="fonts/msyh.ttc")
define mg = Character("梅茜", color="#ff6666", what_font="fonts/msyh.ttc", what_size=70)

define flash = Fade(.25, 0.0, .75, color="#fff")
define flashyellow = Fade(.25, 0.0, .75, color="#f4fca2")
define flashred = Fade(.25, 0.0, .75, color="#b6181d")
define flashblack = Fade(.25, 0.0, .75, color="#000000")
define flashpink = Fade(.25, 0.0, .75, color="#fba1f6")
define vibrate = Move((0, 5), (0, -5), .10, bounce=True, repeat=True, delay=0)
define vpunch_soft = Move((0, 5), (0, -5), .10, bounce=True, repeat=True, delay=0.125)
define hpunch_soft = Move((0, 5), (0, -5), .10, bounce=True, repeat=True, delay=0.125)
#music
define audio.menumain = "audio/Doctor Turtle - The Spiders Of Battersea Park.ogg"
define audio.officemain = "audio/Lo-Fi Astronaut - Design For Dreaming.ogg"
define audio.nightmain = "audio/UNIVERSFIELD - Don't Look Back.ogg"
define audio.nightmain2 = "audio/UNIVERSFIELD - Ethereal Landscapes.ogg"
define audio.insideday = "audio/malictusmusic - Ambient Dream.ogg"
#define audio.insideday2 = "audio/Musinova - The Farthest Star (Cinematic Documentary Ambient Soundscape).ogg"
define audio.insideday2 = "audio/HoliznaCC0 - Creature Comforts.ogg"
define audio.insideday3 = "audio/Lite Saturation - Touching.ogg"
define audio.insidedark = "audio/Serat - Dark decision.ogg"
define audio.outsideday = "audio/Kirk Osamayo - Unsettling Ambience.ogg"
define audio.outsideday2 = "audio/Mark Wilson X - A Killer In Me.ogg"
define audio.horror = "audio/Mark Wilson X - Terror Drome.ogg"
define audio.monster = "audio/UNIVERSFIELD - Dark Thriller.ogg"
define audio.nightmare = "audio/nightmare.ogg"
define audio.lauratheme = "audio/HoliznaPATREON - Lavander.ogg"
define audio.kallietheme = "audio/HoliznaPATREON - Introvert.ogg"
define audio.shelleytheme = "audio/Moonstone.ogg"
define audio.evetheme = "audio/Musinova - Calming Time (Cool Relaxed Electronic Hip Hop).ogg"
define audio.morning = "audio/UNIVERSFIELD - Black Rose.ogg"
define audio.school = "audio/UNIVERSFIELD - Corpse Rot.ogg"
define audio.hotel = "audio/malictusmusic - Haunted By The Past.ogg"

#sound effects
define audio.gunshot = "audio/michorvath__20-gauge-shotgun-gunshot.ogg"
define audio.pistolshot = "audio/9mm.ogg"
define audio.doorclose = "audio/the-bizniss__door-close-3.ogg"
define audio.male_cum = "audio/male_cum.ogg"
define audio.kiss = "audio/kiss_1.ogg"
define audio.kissfuck = "audio/kissfuck.ogg"
define audio.shower = "audio/122810__geodylabs__shower.ogg"
define audio.axehit = "audio/silverillusionist__decapitation-softer-head-impact.ogg"
define audio.gas = "audio/729536__moogleoftheages__smoke-bomb-teleport_edit.ogg"
define audio.woodchop = "audio/2021-09-18T10-48-00.ogg"
define audio.blowjob1 = "audio/blowjob1.mp3"
define audio.blowjob2 = "audio/blowjob2.mp3"
define audio.hit = "audio/damnsatinist__intense-punch.ogg"
define audio.zipper = "audio/Zipper_01.ogg"
define audio.squish = "audio/squish.ogg"
define audio.rain = "audio/angeliquegross__rain-in-a-quiet-neighborhood.ogg"
define scratch_short = "audio/440441__cribbler__scraping_pavement_chalk_2.ogg"
define scratch_long = "audio/440442__cribbler__scraping_pavement_chalk_1.ogg"
define grendel_growl = "audio/grendel breath.ogg"
define monster_thump = "audio/monsterthump.ogg"
define glasssmash = "audio/chewiesmissus__glass-smash.ogg"
define smashhouse = "audio/joelaudio__heavy_smash_002.ogg"
define fire = "audio/mmutua__fire.ogg"
define chopper = "audio/tomlija__the-famous-belgrade-police-department-chopper.ogg"
define chopperloop = "audio/lorenzosu__helicopterraw_30sec.ogg"
define sniper = "audio/sniper-rifle-shot-sound-effect.ogg"
define mp5 = "audio/franki-01234__mp5-submachine-gun-down-the-block.ogg"
define splash = "audio/water-splash-02-352021.ogg"
define bedsprings = "audio/daimon-zero__bedsprings.mp3"

define audio.laura_slow = "audio/07_slow.ogg"
define audio.laura_fast = "audio/07_fast.ogg"
define audio.laura_preorgasm = "audio/07_preorgasm.ogg"
define audio.laura_cum = "audio/07_cum.ogg"
define audio.kallie_slow = "audio/k_slow.ogg"
define audio.kallie_med = "audio/k_med.ogg"
define audio.kallie_fast = "audio/k_fast.ogg"
define audio.kallie_preorgasm = "audio/k_preorgasm.ogg"
define audio.kallie_cum = "audio/k_orgasm.ogg"
define audio.shelley_slow = "audio/s_slow.ogg"
define audio.shelley_med = "audio/s_med.ogg"
define audio.shelley_fast = "audio/s_fast.ogg"
define audio.shelley_preorgasm = "audio/s_preorgasm.ogg"
define audio.shelley_cum = "audio/s_cum.ogg"
define audio.eve_slow = "audio/e_slow.ogg"
define audio.eve_med = "audio/e_med.ogg"
define audio.eve_fast = "audio/e_fast.ogg"
define audio.eve_preorgasm = "audio/e_preorgasm.ogg"
define audio.eve_cum = "audio/e_cum.ogg"


#persistent
default persistent.show_quick_menu = True
default persistent.laura_firstime = False
default persistent.kallie_firstime = False
default persistent.shelley_firstime = False
default persistent.eve_firstime = False
default persistent.all_firstime = False
default persistent.all_firstlove = False
default persistent.ch1_complete = False
default persistent.ch2_complete = False
default persistent.ch3_complete = False
default persistent.ch4_complete = False
default persistent.ch5_complete = False
default persistent.ch6_complete = False
default persistent.ch7_complete = False
default persistent.ch8_complete = False
default persistent.ch9_complete = False
default persistent.ch10_complete = False
default persistent.ch11_complete = False
default persistent.ch12_complete = False
default persistent.ch13_complete = False
default persistent.ch14_complete = False
default persistent.ch15_complete = False
default persistent.ch16_complete = False
default persistent.ch17_complete = False
default persistent.ch18_complete = False
default persistent.ch19_complete = False
default persistent.ch20_complete = False
default persistent.ch21_complete = False
default persistent.ch22_complete = False
default persistent.ch23_complete = False
default persistent.threesome =  False

####persistent video
default current_movie_ch8_s = "shelley_ch8_sex2"
default current_movie_ch9_l = "laura_ch9_fuck"
default current_movie_ch9_s = "shelley_ch9_fuck2"
default current_movie_ch10_l = "laura_ch10_fuck4"
default current_movie_ch11_k = "kallie_ch11_fuck2"
default current_movie_ch12_k = "kallie_ch12_oral"
default current_movie_ch13_k = "kallie_ch13_69"
default current_movie_ch14_s = "shelley_ch14_fuck4"
default current_movie_ch15_s = "shelley_ch15_fuck3"
default current_movie_ch17_l = "laura_ch17_anal5"
default current_movie_ch22_e = "eve_ch22_fuck"
default current_movie_ch22_k = "kallie_ch22_fuck2"
##stats
default warning_suicide = "no"
default k_trust = 0
default k_desire = 0
default k_love = 0
default k_friend = 0
default k_anxiety = 0
default k_sex = 0
default l_trust = 0
default l_desire = 0
default l_love = 0
default l_friend = 0
default l_anxiety = 0
default l_sex = 0
default s_trust = 0
default s_desire = 0
default s_love = 0
default s_friend = 0
default s_anxiety = 0
default s_sex = 0
default s_met = "no"
default e_trust = 0
default e_desire = 0
default e_love = 0
default e_friend = 0
default e_anxiety = 0
default e_sex = 0
default e_met = "no"
#########story defaults
default bicontent = "no"
default ch2_l_lookaway = "no"
default ch2_tell_deadbody = "no"
default ch3_takeshower = "no"
default ch3_laura_kiss = "no"
default ch3_laura_sex = "no"
default ch4_laura_sex = "no"
default ch5_laura_sex = "no"
default ch6_laura_sex = "no"
default ch6_kallie_sex = "no"
default ch6_kallie_sex_cum = "no"
default ch6_s_dormtalk = "no"
default ch7_kallie_sex = "no"
default ch7_shelley_sex = "no"
default ch7_shelleyvisits = "no"
default ch4_burnedone_1_seen = "no"
default ch4_burnedone_callie_seen = "no"
default ch5_kallieseenoff = "no"
default ch5_kshowerhug = "no"
default ch6_backearly = "no"
default ch6_givecellphone = "no"
default ch6_staywithkallie = "no"
default ch7qs_1 = False
default ch7qs_2 = False
default ch7qs_3 = False
default ch7qs_4 = False
default ch7_sh_look = "no"
default ch8_laura_stay = "no"
default ch8_laura_witch = "no"
default ch8_shelley_sex = "no"
default ch8_kallie_sex = "no"
default ch8_kallie_flash = "no"
default ch8_kallie_flash2 = "no"
default ch9_kill = "no"
default ch9_laura_sex = "no"
default ch9_shelley_sex = "no"
default ch9_kallie_mm = "no"
default ch9_tell_laura = "no"
default ch10_kalliehit = "no"
default ch10_goresseen = "no"
default ch10_lauragoreseen = "no"
default ch10_lauramood = 0 #0=okay, no sex for either, #1=upset but will be okay, #2=mad, #3=relationship over
default ch10_kallie_sex = "no"
default ch10_laura_sex = "no"
default ch10_tell_laura = "no"
default ch10_laura_argue = "no"
default shelley_secret_told = "no"
default ch11_laurastay = "no"
default ch11_convenience_talk = 0
default ch11_convenience_s = "no"
default ch11_convenience_l = "no"
default ch11_convenience_k = "no"
default ch11_shelley_sex = "no"
default ch11_kallie_sex = "no"
default ch11_tell_robbery = "no"
default ch12_walkout = "no"
default ch12_laura_sex = "no"
default ch12_laurahug = "no"
default ch12_laura_tellfriend = "no"
default ch12_shelley_sex = "no"
default ch12_kallie_sex = "no"
default kallie_tellheriloveyou = "no"
default ch12_evestay = "no"
default ch12_telleve = "no"
default ch13_eve_sex = "no"
default ch13_kallie_sex = "no"
default ch13_shelley_sex = "no"
default ch14_getlaura = "no"
default ch14_comewith = "none"
default ch14_eve_sex = "no"
default ch14_laura_sex = "no"
default ch14_shelley_sex = "no"
default ch14_kallie_sex = "no"
default ch14_shelleytellskallie = "no"
default ch14_everest = "no"
default ch14_evetalksaboutsis = "no"
default shelley_admitlike = "no"
default ch15_shelleytellsmckallie = "no"
default ch15_eve_sex = "no"
default ch15_shelley_sex = "no"
default ch15_shelley_stay = "no"
default ch15_laura_sex = "no"
default ch15_lauratold = "no"
default ch16_shelley_sex = "no"
default ch16_kallie_sex = "no"
default ch16_laura_sex = "no"
default ch16_kallie_tellfriend = "no"
default kallie_lover = "no"
default shelley_lover = "no"
default laura_lover = "no"
default eve_lover = "no"
default ch17_shelley_sex = "no"
default ch17_kallie_sex = "no"
default ch17_kallie_shelley_sex = "no"
default ch17_laura_sex = "no"
default ch17_eve_sex = "no"
default ch17_ks_know_laura = "no"
default ch17_eve_ask = "no"
default ch17_laura_tell = "none"
default ch17_laura_tell_e = "no"
default ch18_shelleyvisithotel = "no"
default ch18_laura_sex = "no"
default ch18_eve_sex = "no"
default ch18_shelley_sex = "no"
default ch18_kallie_sex = "no"
default ch18_shop_eve = "no"
default ch18_shop_kallie = "no"
default ch18_shop_shelley = "no"
default ch18_shop_laura = "no"
default ch18_freakout = "none"
default ch18_tellshelleylove = "no"
default ch19_laura_sex = "no"
default ch19_eve_sex = "no"
default ch19_shelley_sex = "no"
default ch19_kallie_sex = "no"
default ch19_eve_shelley_bi_sex = "no"
default ch20_shelley_sex = "no"
default ch20_kallie_sex = "no"
default ch20_eve_sex = "no"
default ch21_laura_sex = "no"
default ch21_shelley_sex = "no"
default ch21_kallie_sex = "no"
default ch21_eve_sex = "no"
default ch22_takewith = "none"
default ch22_shelley_sex = "no"
default ch22_eve_sex = "no"
default ch22_kallie_sex = "no"
default ch22_laura_sex = "no"
