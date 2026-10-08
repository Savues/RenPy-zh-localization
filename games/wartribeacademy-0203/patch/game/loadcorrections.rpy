#.# a special label, called when loading a saved game
label after_load:
    #.# unlikely edge case: someone saved the game before player and tribe name were set
    python:
        try:
            player_name
        except NameError:
            player_name = "Gin"
        try:
            tribe_name
        except NameError:
            tribe_name = "Wartribe"
        # it should be impossible to run a replay using the cat name w/o playing the cat naming scene before - but better safe than sorry
        try:
            cat_n
        except NameError:
            cat_n = "Whiskers"
    #.# copy player and tribe name to persistent variables
    #$ persistent.pname = player_name
    #$ persistent.tname = tribe_name
    #.# only used in a few scenes but it's nicer to use the name chosen by the player
    #$ persistent.cname = cat_n
    #x# it only works when loading a save actually sets the persistent variable
    #$ persistent.cname = cat_n
    #$ persistent.cleoname = cleo_name
    # unlock redone Rhea scenes (Bar Visit .. At Least Together) when the following scene was already seen (Rhea's Deal)
    # (possible issue: when some scenes can only be unlocked on specific paths this crude approach b0rks it, all are unlocked now)
        if renpy.seen_label("rhea13_1"):
            renpy.mark_label_seen("rhea4_1")
            renpy.mark_label_seen("rhea5_1a")
            renpy.mark_label_seen("rhea6_1a")
            renpy.mark_label_seen("rhea7_1a")
            renpy.mark_label_seen("rhea8_1a")
            renpy.mark_label_seen("rhea9_1")
            renpy.mark_label_seen("rhea10_1a")
            renpy.mark_label_seen("rhea11_1a")
            renpy.mark_label_seen("rhea5_1b")
            renpy.mark_label_seen("rhea6_1b")
            renpy.mark_label_seen("rhea7_1b")
            renpy.mark_label_seen("rhea8_1b")
            renpy.mark_label_seen("rhea10_1b")
            renpy.mark_label_seen("rhea11_1b")
        if renpy.seen_label("invasion1_1"):
            renpy.mark_label_seen("juna24_1")
            renpy.mark_label_seen("juna23_1")
        if lovejuna == 23 and servants > 20:
            servants = 20
    return