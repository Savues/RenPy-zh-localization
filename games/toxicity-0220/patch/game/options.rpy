## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("TOXICity")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "0.22.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""想了解本项目的最新消息，请关注我们的 {a=https://www.patreon.com/ilsproductions}Patreon{/a}、{a=https://subscribestar.adult/ilsproductions}Subscribestar{/a} 或 {a=https://twitter.com/IlsProductions}Twitter{/a}。
""")
define gui.credit = _p("""
感谢所有为本作提供素材内容、支持其开发的朋友。{p}
感谢 HS2 模组社区提供了大量地图、道具与特效。部分动画改编自 {a=https://www.patreon.com/cw/RealGoodStuffPro}RealGoodStuff Production{/a} 的作品。{a=https://www.patreon.com/cw/ziglomods}Ziglo mods{/a} 提供了部分便利性模组。{p}{p}
对话框透明度与快捷菜单代码由用户 {b}shreek{/b} 提供。{p}{p}
代码与脚本清理工作参考了 {b}Anime Sins{/b} 与 {b}Mordred93{/b} 的建议。{p}{p}
{b}字体：{/b}{p}
DCC Ash by {a=http://dccanim.deviantart.com}Draghia Cornel{/a}{p}
Designer Notes by {a=http://www.fontfuel.com}Roger Ridpath{/a}{p}
Ikusuteito by {a=http://extate.blogspot.com/}Audrius Skersys aka Extate{/a}{p}
Cavity by {a=https://www.1001fonts.com/users/TheCrownIsMine/}TheCrownIsMine{/a}{p}
部分摄影素材来自 {a=http://www.pexels.com}Pexels{/a} 与 {a=www.pixabay.com}Pixabay{/a}。
{p}"high rise buildings at daytime" by {a=https://www.pexels.com/@olly/}Andrea Piacquadio{/a}{p}
{p}{b}音乐：{/b}{p}
All audio is covered under {a=https://creativecommons.org/licenses/by/3.0/}Creative Commons Attribution License 3.0{/a} or {a=https://creativecommons.org/licenses/by-sa/4.0/}4.0{/a}.{p}
{i}"The Spiders Of Battersea Park"{/i} by {a=https://freemusicarchive.org/music/Doctor_Turtle/}Doctor Turtle{/a}{p}
{i}"Don't Look Back"{/i}, {i}"Atmosphere for Documentaries"{/i}, {i}"Corpse Rot"{/i}, {i}"Dark Thriller"{/i}, {i}"Black Rose"{/i}, and {i}"Ethereal Landscapes{/i} by {a=https://freemusicarchive.org/music/universfield/}UNIVERSFIELD{/a}{p}
{i}"Ambient Dream"{/i} and {i}"Haunted By The Past"{/i} by {a=https://freemusicarchive.org/music/malictusmusic/}Malictusmusic{/a}{p}
{i}"Unsettling Ambience"{/i} by {a=https://freemusicarchive.org/music/kirk-osamayo/}Kirk Osamayo{/a}{p}
{i}"Design For Dreaming"{/i} by {a=https://freemusicarchive.org/music/lo-fi-astronaut/lo-fi-and-beyond}Lo-Fi Astronaut{/a}{p}
{i}"Dark decision"{/i} by {a=https://freemusicarchive.org/music/serat/}Serat{/a}{p}
{i}"Lavander"{/i}, {i}"Moonstone"{/i}, {i}"Creature Comforts"{/i}, and {i}"Introvert"{/i} by {a=https://www.patreon.com/c/Holizna/}Holizna{/a}{p}
{i}"A Killer In Me"{/i} and {i}"Terror Drome"{/i} by {a=https://freemusicarchive.org/music/mark-wilson-x}Mark Wilson X{/a}{p}
{i}"The Farthest Star (Cinematic Documentary Ambient Soundscape)"{/i} and {i}"Calming Time (Cool Relaxed Electronic Hip Hop)."{/i} by {a=https://freemusicarchive.org/music/musinova/discography}Musinova{/a}{p}
{i}"Touching"{/i} by {a=https://freemusicarchive.org/music/lite-saturation/}Lite Saturation{/a}{p}
{p}{b}音效：{/b}{p}
{i}"Door close 3"{/i} by {a=https://freesound.org/people/THE_bizniss/}THE_bizniss{/a}{p}
{i}"Shower"{/i} by {a=https://freesound.org/people/geodylabs/}geodylabs{/a}{p}
{i}"20 gauge shotgun gunshot"{/i} by {a=https://freesound.org/people/michorvath/}michorvath{/a}{p}
{i}"The famous Belgrade Police Department chopper flying over the city..."{/i} by {a=https://freesound.org/people/Tomlija/}Tomlija{/a}{p}
{i}"Smoke Bomb Teleport"{/i} by {a=https://freesound.org/people/moogleoftheages/}moogleoftheages{/a}{p}
{i}"Axe Impact 2 - Pitch down"{/i} by {a=https://freesound.org/people/LiamG_SFX/}LiamG_SFX{/a}{p}
{i}"Decapitation (softer head impact)"{/i} by {a=https://freesound.org/people/SilverIllusionist/}SilverIllusionist{/a}{p}
{i}"Scraping Pavement Chalk 1"{/i} and {i}"Scraping Pavement Chalk 2"{/i} by {a=https://freesound.org/people/cribbler/}Cribbler{/a}{p}
{i}"Horror/gore sound effect"{/i} by {a=https://freesound.org/people/AdrianoAnjos/}AdrianoAnjos{/a}{p}
{i}"Glass Smash"{/i} by {a=https://freesound.org/people/chewiesmissus/}chewiesmissus{/a}{p}
{i}"Heavy Smash 002"{/i} by {a=https://freesound.org/people/JoelAudio/}JoelAudio{/a}{p}
{i}"Fire"{/i} by {a=https://freesound.org/people/mmutua/}mmutua{/a}{p}
{i}"MP5 submachine gun down the block"{/i} by {a=https://freesound.org/people/Franki-01234/}Franki-01234{/a}{p}
{i}"helicopterRaw_30sec"{/i} by {a=https://freesound.org/people/lorenzosu/}lorenzosu{/a}{p}
{i}"Rain in a quiet neighborhood"{/i} by {a=https://freesound.org/people/AngeliqueGross/}AngeliqueGross{/a}{p}
""")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "TOXICity"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True
init python:
    renpy.music.register_channel("ambient","music",loop=True,tight=True)
init python:
    renpy.music.register_channel("voice_loop", "voice", loop=True)

## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "audio/Doctor Turtle - The Spiders Of Battersea Park.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "TOXICity"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.ico"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.
    build.archive("scripts", "all")
    build.archive("images", "all")

    # Put script files into the scripts archive.
    build.classify("game/**.rpy", "scripts")
    build.classify("game/**.rpyc", "scripts")

    # Put images into the images archive.
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.webm", "images")
    build.classify("game/**.webp", "images")
    build.classify("game/**.ogv", "images")
    build.classify('game/**.png', 'images')
    # build.classify('game/**.jpg', 'archive')
    # build.include_i686 = False
    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
