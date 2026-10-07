####################################################################################################################################################
####### DayEnd Function ######################################################################################################################
label day_end: #Ends day, updates time/weekday/daycount
    # call DailyStats from _call_DailyStats_1 #Resets daily stat variables


    scene img_dusk
    with fade
    pause 1.0
    stop music fadeout 1.0
    pause 0.5

    if CurrentWeekDay == 6:
        $ CurrentWeekDay = 0
    else:
        $ CurrentWeekDay += 1
    $ Day += 1
    $ WeekDayOutput = WeekDays[CurrentWeekDay]
    $ CurrentTime = 0
    $ TimeOutput = Time[CurrentTime]

    #Check and advance month
    if Month == "Sept" and Day == 31:
        $ Month = "Oct"
        $ Day = 1 

    # NIGHT EVENTS
    if flag_main_3dream_active == True:
        jump event_main_3dream
    if flag_main_28_active == True:
        stop ambiance

    scene img_dawn
    with dissolve
    play music "audio/bgm/morning.mp3" noloop fadein 1.0
    pause 0.5
    show screen Dawn_Screen
    with dissolve
    pause 2
    hide screen Dawn_Screen

    # QUEUE MUSIC TO PLAY AFTER NIGHT/DAY TRANSITION
    if flag_main_26_active == True:
        queue music "audio/bgm/akatsuki_theme.mp3" loop
    elif flag_main_28_active == True:
        queue music "audio/bgm/catherine_theme.mp3" loop
    elif flag_main_31_active == True:
        queue music "audio/bgm/victoria_sadness.mp3" loop
    else:
        queue music "audio/bgm/home.mp3" loop

    # scene upstairs_attic
    # with fade

    # MORNING EVENTS
    if flag_main_2_active == True:
        jump event_main_2
    elif flag_main_3_active == True:
        jump event_main_3
    elif flag_main_4_active == True:
        jump event_main_4
    elif flag_main_5_active == True:
        jump event_main_5
    elif flag_main_6_active == True:
        jump event_main_6
    elif flag_main_7_active == True:
        jump event_main_7
    elif flag_main_8_active == True:
        jump event_main_8
    elif flag_main_9_active == True:
        jump event_main_9
    elif flag_main_10_active == True:
        jump event_main_10
    elif flag_main_11_active == True:
        jump event_main_11
    elif flag_main_12_active == True:
        jump event_main_12
    elif flag_main_13_active == True:
        jump event_main_13
    elif flag_main_14_active == True:
        jump event_main_14
    elif flag_main_15_active == True:
        jump event_main_15
    elif flag_main_16_active == True:
        jump event_main_16
    elif flag_main_17_active == True:
        jump event_main_17
    elif flag_main_18_active == True:
        jump event_main_18
    elif flag_main_19_active == True:
        jump event_main_19
    elif flag_main_20_active == True:
        jump event_main_20
    elif flag_main_21_active == True:
        jump event_main_21
    elif flag_main_22_active == True:
        jump event_main_22
    elif flag_main_23_active == True:
        jump event_main_23
    elif flag_main_24_active == True:
        jump event_main_24
    elif flag_main_25_active == True:
        jump event_main_25
    elif flag_main_26_active == True:
        jump event_main_26
    elif flag_main_27_active == True:
        jump event_main_27
    elif flag_main_28_active == True:
        jump event_main_28
    elif flag_main_29_active == True:
        jump event_main_29
    elif flag_main_30_active == True:
        jump event_main_30
    elif flag_main_31_active == True:
        jump event_main_31
    elif flag_main_32_active == True:
        jump event_main_32

    # scene upstairs_attic
    # with fade

screen Dawn_Screen():
    frame:
        xalign 0.5
        yalign 0.2
        background None
        text "{b}[WeekDayOutput] - [Month] [Day]{/b}" size 80 # color ("#000000")



####################################################################################################################################################
####### Save/Load Screen +/-10 ######################################################################################################################

# default CurrentPagePlus = 1

# init python:
#     def increment10():
#         CurrentPagePlus = str(int(FileCurrentPage()) + 10)


# init python:
#     def upd_file_page():
#         persistent._file_page = str(persistent.file_page + 1)
#         renpy.restart_interaction()

#     def next_file_page():
#         if persistent.file_page < 0:
#             persistent.file_page += 1
#             upd_file_page()

#     def prev_file_page():
#         if persistent.file_page > 0:
#             persistent.file_page -= 1
#             upd_file_page()