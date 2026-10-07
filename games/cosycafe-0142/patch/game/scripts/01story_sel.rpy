init python:

    class ChapterItem:
        def __init__(self, name, background, thumb, content):
            self.name       = name
            self.background = background
            self.thumb      = thumb
            self.content    = content

    chapter1 = ChapterItem('第1章 - 新的开始', 'images/img_black.png', 'images/GUI/DaySelect/img_main31_460.webp'        , [
        ['Blank', 'Blank', 'Blank'], # just follow the same template, ['label to load', 'date in button', 'update number text'] 
        ['Blank', 'Blank', 'Blank'],
        ['Blank', 'Blank', 'Blank'],
        ['Blank', 'Blank', 'Blank'],
        ['Blank', 'Blank', 'Blank'],
        ['Blank', 'Blank', 'Blank'],
        ['start_beginning', 'Sept 1', '更新至 0.1'], 
        ['start_day2', 'Sept 2', '更新至 0.1'], 
        ['start_day3', 'Sept 3', '更新至 0.1'],
        ['start_day4', 'Sept 4', '更新至 0.1'],
        ['start_day5', 'Sept 5', '更新至 0.1'],
        ['start_day6', 'Sept 6', '更新至 0.1'],
        ['start_day7', 'Sept 7', '更新至 0.1'],
        ['start_day8', 'Sept 8', '更新至 0.1'],
        ['start_day9', 'Sept 9', '更新至 0.1'],
        ['start_day10', 'Sept 10', '更新至 0.1'],
        ['start_day11', 'Sept 11', 'Update 0.1/0.2'],
        ['start_day12', 'Sept 12', '更新至 0.2'],
        ['start_day13', 'Sept 13', '更新至 0.3'],
        ['start_day14', 'Sept 14', '更新至 0.3'],
        ['start_day15', 'Sept 15', '更新至 0.4'],
        ['start_day16', 'Sept 16', '更新至 0.5'],
        ['start_day17', 'Sept 17', '更新至 0.5'],
        ['start_day18', 'Sept 18', '更新至 0.6'],
        ['start_day19', 'Sept 19', '更新至 0.7'],
        ['start_day20', 'Sept 20', '更新至 0.7'],
        ['start_day21', 'Sept 21', '更新至 0.8'],
        ['start_day22', 'Sept 22', '更新至 0.9'],
        ['start_day23', 'Sept 23', '更新至 0.9'],
        ['start_day24', 'Sept 24', '更新至 0.10'],
        ['start_day25', 'Sept 25', '更新至 0.10'],
        ['start_day26', 'Sept 26', '更新至 0.11'],
        ['start_day27', 'Sept 27', '更新至 0.12'],
        ['start_day28', 'Sept 28', '更新至 0.12'],
        ['start_day29', 'Sept 29', '更新至 0.13'],
        ['start_day30', 'Sept 30', '更新至 0.13'],
        ['start_day31', 'Oct 1', '更新至 0.14'],
        ['start_day32', 'Oct 2', '更新至 0.14'], 
    ])
    chapter2 = ChapterItem('第2章 - 圣诞咖啡馆', 'images/img_black.png', 'images/GUI/DaySelect/chapter_locked.webp', None)
    chapter3 = ChapterItem('第3章 - 考试季', 'images/img_black.png', 'images/GUI/DaySelect/chapter_locked.webp', None)
    chapter4 = ChapterItem('第4章 - 夏日小插曲', 'images/img_black.png', 'images/GUI/DaySelect/chapter_locked.webp', None)
    chapter5 = ChapterItem('第5章 - 大学', 'images/img_black.png', 'images/GUI/DaySelect/chapter_locked.webp', None)
    chapter6 = ChapterItem('第6章 - 幸福美满', 'images/img_black.png', 'images/GUI/DaySelect/chapter_locked.webp', None)

    chapters = [
        chapter1,
        chapter2,
        chapter3,
        chapter4,
        chapter5,
        chapter6,
    ]

    import re as _re

    def zh_date(s):
        # 'Sept 12' -> '9月12日'; the raw string doubles as a preview-image name,
        # so only the on-screen copy may be translated
        m = _re.match(r'^([A-Za-z]+)\s+(\d+)$', s)
        if not m:
            return s
        months = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4',
                  'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8',
                  'Sept': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        return months.get(m.group(1), m.group(1)) + '月' + m.group(2) + '日'

transform text_pulse:
    zoom 1.0
    on idle:
        linear 1.0 zoom 1.07
        linear 1.0 zoom 0.97
        repeat
    on hover:
        linear 0.4 zoom 1.0

screen story_sel():
    tag menu
    key 'game_menu' action Return()

    default overlay_hovered = False
    default day_preview = None
    default day_preview_text = None
    default i_active = chapter1
    default sel_focus = 0

    timer 0.05 action MouseMove(900, 100, duration=0.4)

    # Background layer
    if sel_focus is not None:
        add chapters[sel_focus].background:
            at transform:
                xycenter (.5, .5)
                zoom 1.25
                blur 5
                ease_quint (1.0 * persistent.ui_speed_multiplier) zoom 1.0 blur 0.0
        
        add 'gui/msp1/story_sel/bg_overlay.png' align (.5, 1.0)

    # ====================== MAIN MENU CONTENT ======================
    frame:
        xysize (config.screen_width, config.screen_height)
        align (.5, .5)
        padding (25, 25, 25, 25)

        vbox:
            spacing 24
            align (.5, .0)

            # Top buttons
            hbox:
                align (.5, .0)
                spacing 24

                button:
                    xysize (923, 160)
                    align (.5, .5)
                    action Jump('start_beginning')
                    image 'gui/msp1/story_sel/btn1.png' align (.5, .0) offset (0, -13):
                        at transform:
                            matrixcolor ColorizeMatrix('#000', '#ff4848') * BrightnessMatrix(.125)

                    text '重新开始游戏！':
                        size 65 
                        font "fonts/MiSans-Regular.ttf" 
                        align (.5, .5) 
                        offset (0, -2)
                        at text_pulse

                    at transform:
                        subpixel True
                        offset (0, -1080)
                        pause .0
                        easein_quart (1.25 * persistent.ui_speed_multiplier) offset (0, 0)
                        matrixcolor BrightnessMatrix(.0)
                        on idle:
                            easein_quart (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                        on hover:
                            easein_quart (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.125)

                button:
                    xysize (923, 160)
                    align (.5, .5)
                    action Jump('start_day31')
                    image 'gui/msp1/story_sel/btn2.png' align (.5, .0) offset (0, -13):
                        at transform:
                            matrixcolor ColorizeMatrix('#000', '#d06a6c') * BrightnessMatrix(.225)
                    text '从最新进度开始' size 45 font "fonts/MiSans-Regular.ttf" align (.5, .5) offset (0, -2)
                    at transform:
                        subpixel True
                        offset (0, -1080)
                        pause .05
                        easein_quart (1.25 * persistent.ui_speed_multiplier) offset (0, 0)
                        matrixcolor BrightnessMatrix(.0)
                        on idle:
                            easein_quart (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                        on hover:
                            easein_quart (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.125)

            # Chapter Selector
            frame:
                xysize (1870, 318)
                align (.5, .0)
                at transform:
                    subpixel True
                    offset (0, -512)
                    pause .1
                    easein_quart (1.25 * persistent.ui_speed_multiplier) offset (0, 0)

                viewport:
                    xysize (1870, 318)
                    align (.5, .5)
                    draggable True
                    mousewheel 'horizontal'
                    hbox:
                        align (.0, 1.0)
                        spacing 24
                        at transform:
                            subpixel True
                            easein_quart (.5 * persistent.ui_speed_multiplier) offset (-(565+24) * sel_focus, 0)
                        for x, y in enumerate(chapters):
                            button:
                                xysize (565, 318)
                                align (.5, .0)
                                action [
                                    SetScreenVariable('sel_focus', x),
                                    SetScreenVariable('i_active', y)
                                ]
                                image 'gui/msp1/story_sel/shadow.png' align (.5, .0) offset (0, -13)
                                image AlphaMask(Transform(y.thumb, zoom=.2944444444444444), 'gui/msp1/story_sel/mask.png') align (.5, .5)
                                image 'gui/msp1/story_sel/overlay.png' align (.5, 1.0) offset (0, 6)
                                frame:
                                    xysize (None, 35)
                                    align (.0, 1.0)
                                    offset (18, -18)
                                    text y.name size 40 font 'fonts/MiSans-Regular.ttf' align (.0, .5) offset (-9, -2)
                                at transform:
                                    matrixcolor BrightnessMatrix(.0)
                                    easein_quart (.5 * persistent.ui_speed_multiplier) zoom 1.0 alpha 1.0
                                    on idle:
                                        easein_quart (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)
                                    on hover:
                                        easein_quart (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.25)

            # Day Selector
            frame:
                background Frame('gui/msp1/story_sel/day_plate_new.png')
                xysize (1388, 502)
                align (.0, .0)
                offset (0, -6)
                padding (16, 16, 16, 16)
                at transform:
                    subpixel True
                    offset (0, 1080)
                    pause .15
                    easein_quart (1.25 * persistent.ui_speed_multiplier) offset (0, 0)

                frame:
                    xysize (1356, 35)
                    align (.5, .0)
                    offset (0, -6)
                    text '从指定日期开始' size 40 font "fonts/MiSans-Regular.ttf" align (.5, .5):
                        if overlay_hovered:
                            at transform:
                                linear 0.25 alpha 1.0
                        else:
                            at transform:
                                linear 0.32 alpha 0.0

                # Day labels (Sunday to Saturday)
                for i, day in enumerate(["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]):
                    frame:
                        xysize (192, 70)
                        align (.0, .0)
                        offset (i * 192, 35)
                        text day size 24 font "fonts/MiSans-Regular.ttf" align (.5, .0)

                hbox:
                    align (.0, .0)
                    spacing 0

                    #Day Button Grid
                    vpgrid:
                        xysize (1356, 421)
                        offset (0, 75)
                        align (.5, .0)
                        cols 7
                        spacing 12
                        draggable True
                        mousewheel True
                        if chapters[sel_focus].content is not None:
                            for x in chapters[sel_focus].content:
                                button:
                                    xysize (180, 56)
                                    if x[1] != "Blank":
                                        action [Jump(x[0])]
                                        image 'gui/msp1/story_sel/day_btn.png' align (.5, .0) offset (0, -13):
                                            at transform:
                                                on idle:
                                                    easein_quart .5 matrixcolor BrightnessMatrix(.0) * ColorizeMatrix('#000', '#fff')
                                                on hover:
                                                    easein_quart .5 matrixcolor BrightnessMatrix(.5) * ColorizeMatrix('#000', '#ffb1df')
                                        text zh_date(x[1]) size 24 font "fonts/MiSans-Regular.ttf" align (.5, .5)
                                        hovered [
                                            SetScreenVariable("day_preview", "images/GUI/DaySelect/preview/" + x[1] + ".webp"),
                                            SetScreenVariable("day_preview_text", x[2])
                                        ]

                    #Day Preview
                    vbox:
                        frame:
                            offset (0, 73)
                            if chapters[sel_focus].content is not None:
                                add day_preview xysize (490, 280)
                        frame:
                            xysize (490, 100)
                            offset (0, 73)
                            text "[day_preview_text]" size 24 font "fonts/MiSans-Regular.ttf"

    # Day Select overlay

        image 'images/img_black.png' align (.5, 1.0) xysize (1920, 865):
            if overlay_hovered:
                at transform:
                    linear 0.25 alpha 0.0
            else:
                at transform:
                    linear 0.32 alpha 0.75

        text '从指定日期开始' size 60 font "fonts/MiSans-Regular.ttf" align (.5, .52):
            if overlay_hovered:
                at transform:
                    linear 0.25 alpha 0.0
            else:
                at transform:
                    linear 0.32 alpha 1.0
        

        mousearea:
            xysize (1920, 900)
            align (0.5, 1.0)
            hovered SetScreenVariable("overlay_hovered", True)
            unhovered SetScreenVariable("overlay_hovered", False)
