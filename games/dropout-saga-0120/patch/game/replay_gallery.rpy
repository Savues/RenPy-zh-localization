init -1:
    $ persistent.unlock_replay = False

init python:
    def get_custom_name(c, d=None):
        if c in d.keys():
            if d.get(c, None) is not None:
                return d.get(c)
            else:
                return c
        else:
            return c

    def ToggleSet(set, i):
        if i in set:
            RemoveFromSet(set, i)
        else:
            AddToSet(set, i)
        return

    def check_list(l1, l2):
        return any(i in l1 for i in l2)

style category_button_text is text:
    font "Fonts/MiSans-Regular.ttf"
    idle_color "#fff3e6"
    hover_color "#ff0000"
    selected_color "#ff0000"
    size 30

style list_button_text is text:
    font "Fonts/MiSans-Regular.ttf"
    idle_color "#fff3e6"
    hover_color "#ff0000"
    selected_color "#ff0000"
    size 20

style gallery_vscrollbar:
    unscrollable 'hide'

label patreon_gallery_unlock:
    if patreon == True:
        if persistent.unlock_replay == True:
            $persistent.unlock_replay = False
        else:
            $persistent.unlock_replay = True
    else:
        $patreoncheck = renpy.input("你真的是我们的赞助者吗，[name]？")
        $patreoncheck = patreoncheck.strip()
        
        if patreoncheck == patreoncode:
            play sound "audio/Lockpick_Success.ogg"
            "谢谢！代码已激活！"
            $patreon = True 
            $ persistent.unlock_replay = True
        else:
            "抱歉。你确定自己是赞助者吗？"
            "如果不是，欢迎去看看我们的赞助页面！"
            "赞助者专属内容里有作弊码、可反复观看的场景画廊等一大堆好东西！:)"
            $patreon = False
            $ persistent.unlock_replay = False
    call screen replay_gallery

screen replay_gallery():
    default parent = 'Household'
    default cat = set(replay_categories.get(parent))
    $ button_width = 370
    $ button_height = 208
    tag menu
    add 'gui/gallery/prefs-overlay.png'
    use game_menu(_("画廊"), scroll=None):
        text "{image=gui/gallery/left-separator.png} 回放画廊 {image=gui/gallery/right-separator.png} " style "main_menu_text" font "Fonts/MiSans-Regular.ttf" xalign 0.5
        vbox:
            spacing 10
            xfill True
            ypos 70
            hbox:
                xfill True
                xalign 0.5
                style_prefix "category"
                spacing gui.navigation_spacing
                for p in ['Household', 'College', 'Wolfpack', 'Russians', 'Germans', 'Police', 'Herd']:
                    textbutton "[p]":
                        action [SetScreenVariable('parent', p), SetScreenVariable('cat', replay_categories.get(p))]
                        selected parent == p
            text "{image=gui/gallery/center-separator.png}" xalign 0.5
            frame padding(0,0):
                background None
                hbox:
                    style_prefix "list"
                    vbox xalign 1.0 spacing 10:
                        textbutton "全部" action SetScreenVariable('cat', replay_categories.get(parent)) xalign 1.0
                        for c in replay_categories[parent]:
                            if c in character_conditions.keys() and not character_conditions[c] and not persistent.unlock_replay:
                                textbutton "????" xalign 1.0
                            else:
                                textbutton "%s"%(get_custom_name(c, d = custom_names)) action SetScreenVariable('cat', c) xalign 1.0

                vpgrid:
                    cols 3 
                    spacing 20 
                    xalign 0.7 
                    ysize 0.9
                    style_prefix 'gallery'
                    draggable True
                    mousewheel True
                    allow_underfull True
                    scrollbars "vertical"
                    for item in replay_scenes:
                        if check_list(cat, item.category):
                            if renpy.seen_label(item.label) or persistent.unlock_replay:
                                vbox:
                                    button xsize button_width ysize button_height padding(0,0) :
                                        hover_background im.Scale('gui/gallery/gallery_hover.png', button_width, button_height)
                                        add AlphaMask(im.Scale(item.cover, button_width, button_height), im.Scale('gui/gallery/save-thumbnail-alpha.png', button_width, button_height))
                                        action Replay(item.label, locked=False, scope=item.arguments)
                                    text "[item.title]" xalign 0.5 style "main_menu_text" size 35
                            else:
                                vbox:
                                    button xsize button_width ysize button_height padding(0,0) :
                                        idle_background AlphaMask(im.Scale(item.cover, button_width, button_height), im.Scale('gui/gallery/save-thumbnail-alpha.png', button_width, button_height))
                                        add AlphaMask(im.Scale(im.Blur(item.cover, 25), button_width, button_height), im.Scale('gui/gallery/save-thumbnail-alpha.png', button_width, button_height))
                                        action NullAction()
                                    text _("-机密-") xalign 0.5 style "main_menu_text" size 35
                                    
                                    
                #textbutton "Patreon" action ToggleField(persistent, "unlock_replay", True, False)
                textbutton "赞助代码（解锁全部场景）" action Jump("patreon_gallery_unlock") xalign 0.01 yalign 0.9