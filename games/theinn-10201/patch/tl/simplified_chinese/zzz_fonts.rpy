# 《The Inn》简体中文本地化 · 中文字体
#
# 游戏原本使用的字体（arialround.ttf 等）不含任何中文字形，直接显示会出现方框。
# 这里把正文与界面会用到的字体统一映射到 Noto Sans SC（思源黑体系列的免费版本，
# SIL Open Font License 1.1，可自由分发与修改）。
#
# NotoSansSC-Regular.ttf 由 NotoSansSC-VF.ttf 实例化而来：
# 仅把 fvar 表中 wght 轴的默认值由 100 改为 400，其余数据未作任何改动。
translate simplified_chinese python:

    _cjk_font = "fonts/NotoSansSC-Regular.ttf"

    for _f in (
        "fonts/arialround.ttf",
        "fonts/arialround.TTF",
        "fonts/ShareTechMono-Regular.ttf",
        "fonts/impact.ttf",
        "fonts/Computerfont.ttf",
        "fonts/NotoSans-Regular.ttf",
        "fonts/sharkbite.ttf",
        "fonts/stay.otf",
        "fonts/arrow_crafter.otf",
        "fonts/LEMONMILK-Regular.otf",
        "fonts/LEMONMILK-Medium.otf",
        "fonts/LEMONMILK-Bold.otf",
        "fonts/Classic Robot.otf",
        "fonts/Classic Robot Bold.otf",
        "fonts/Classic Robot Italic.otf",
        "fonts/Classic Robot Bold Italic.otf",
        "fonts/Classic Robot Condensed.otf",
        "fonts/Classic Robot Condensed Bold.otf",
        "fonts/Classic Robot Condensed Italic.otf",
        "fonts/Classic Robot Condensed Bold Italic.otf",
        "fonts/COMPUTERRobot.ttf",
        "fonts/DigitalDisco.ttf",
        "fonts/DigitalDisco-Thin.ttf",
        "fonts/digital-7.ttf",
        "fonts/DS-DIGIB.TTF",
        "fonts/16Segments-Basic.otf",
        "fonts/14 Segment LED.ttf",
        "fonts/Counter-Dial.ttf",
        "fonts/LCDAT&TPhoneTimeDate.ttf",
        "fonts/LazenbyCompSmooth.ttf",
        "fonts/Road_Rage.otf",
        "fonts/Dystopian Future.ttf",
        "fonts/korneuburg.ttf",
        "fonts/punk kid.ttf",
        "fonts/whoaskssatan.ttf",
        "fonts/demonsker.ttf",
        "fonts/cargo_crate.ttf",
        "fonts/computer_pixel-7.ttf",
        "fonts/SawarabiMincho-Regular.ttf",
    ):
        renpy.config.font_name_map[_f] = _cjk_font

    del _f, _cjk_font
