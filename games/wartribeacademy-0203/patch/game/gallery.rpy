# GALLERY TEST LINE BELOW
screen gallery():
    tag menu

    add "black"

    $start = gallery_page * maxperpage
    $end = min(start + maxperpage - 1, len(gallery_items) - 1)

    #Grid for images
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
#There's a bug in the gallery that makes some of these scenes bleed a little
            else:
                imagebutton idle gallery_items[i].thumb:
                    action ToggleScreen("gallery_closeup", dissolve, gallery_items[i].images)
                    xalign 0.5
                    yalign 0.5

        for i in range(end + - start + 1, maxperpage):
            null


    #grid for info
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end +1):
            hbox:
                xalign 0.5
                yalign 0.1
                $total = gallery_items[i].num_images()
                $partial = gallery_items[i].num_unlocked
                text gallery_items[i].name
                text "[partial]/[total]"

        for i in range(end - start + 1, maxperpage):
            null

    #Previous/Next Buttons
    if gallery_page > 0:
        textbutton "Previous":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.1
            yalign 0.98
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        textbutton "Next":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 0.98

    #Return Button
    textbutton "返回":
        action Return()
        xalign 0.5
        yalign 0.98

#report of a bug that seems to originate here, While running game code:
# File "game/gallery.rpy", line 72, in execute
#    screen gallery_closeup(images):
# File "game/gallery.rpy", line 72, in execute
#    screen gallery_closeup(images):
#  File "game/gallery.rpy", line 74, in execute
#    add images[closeup_page] at truecenter
#IndexError: list index out of range
screen gallery_closeup(images):

    add images[closeup_page] at truecenter

    if closeup_page > 0:
        textbutton "Previous":
            action SetVariable("closeup_page", closeup_page - 1)
            xalign 0.1
            yalign 0.98
            background "black"
    if closeup_page < len(images) - 1:
        textbutton "Next":
            action SetVariable("closeup_page", closeup_page + 1)
            xalign 0.9
            yalign 0.98
            background "black"

    textbutton "返回":
        action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
        xalign 0.5
        yalign 0.98
