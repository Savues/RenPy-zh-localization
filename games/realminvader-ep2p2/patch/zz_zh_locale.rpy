# ===========================================================================
#  Realm Invader Episode 2 Part 2 -- Simplified Chinese, single shim.
#
#  Concatenation of the two shims the patch shipped as:
#
#      zz_zh_cn.rpy        language, font group, font_transform
#      zz_zh_cn_menu.rpy   main-menu text rendering
#
#  games.patch_entries() reads one `shim` from game.json and package_release.py
#  writes that one file, so the pair was merged rather than left as two files a
#  packager would silently drop one of.
#
#  Order is safe. The init priorities do not collide: 100 and 1501 appear only
#  in zz_zh_cn.rpy, and zz_zh_cn_menu.rpy declares no init block at all -- only a
#  transform and `screen main_menu()`. Screens are evaluated lazily on first
#  display, well after init 100 has bound _ZH_CN_FONT, so the menu's
#  `text_font _ZH_CN_FONT` resolves.
#
#  One change beyond concatenation: the bundled face is referenced as
#  `fonts/NotoSansSC-VF.ttf` rather than `Fonts/NotoSansSC-VF.ttf`, because
#  tools/install.py and tools/package_release.py can only write game/fonts/.
#
#  The MiSans branches below are left exactly as written: MiSans carries no
#  redistribution grant, so this package does not ship it. Drop MiSans-Regular.ttf
#  and MiSans-Bold.ttf into the game's game/Fonts/ yourself and the shim picks
#  them up automatically.
# ===========================================================================

define config.default_language = "schinese"

init 100 python:
    # 中文字体选择:
    #   补丁自带 fonts/NotoSansSC-VF.ttf (SIL OFL 1.1, 允许随补丁一起分发)
    #   MiSans 的许可协议禁止再分发字体文件, 因此不随补丁附带; 想用的话把
    #   MiSans-Regular.ttf / MiSans-Bold.ttf 放进 game/Fonts/, 脚本会自动启用。
    _ZH_CN_FALLBACK = "fonts/NotoSansSC-VF.ttf"

    # MiSans 没有收录的符号区段, 交给 Noto 兜底, 避免出现豆腐块
    _ZH_CN_SYMBOL_RANGES = (
        (0x1d00, 0x1d7f),   # phonetic extensions
        (0x2190, 0x21ff),   # arrows
        (0x2600, 0x26ff),   # miscellaneous symbols
        (0x2700, 0x27bf),   # dingbats
        (0x2b00, 0x2bff),   # arrows supplement
    )

    def _zh_cn_make_font_group():
        regular = _ZH_CN_FALLBACK
        if renpy.loader.loadable("Fonts/MiSans-Regular.ttf"):
            regular = "Fonts/MiSans-Regular.ttf"
            bold = "Fonts/MiSans-Bold.ttf" if renpy.loader.loadable("Fonts/MiSans-Bold.ttf") else regular
            for is_bold in (False, True):
                for italics in (False, True):
                    # 有真 Bold 字重时关掉合成粗体, 避免二次加粗过粗
                    config.font_replacement_map[(regular, is_bold, italics)] = (bold if is_bold else regular, False, italics)

        group = FontGroup()
        group.add(regular, None, None)
        for start, end in _ZH_CN_SYMBOL_RANGES:
            group.add(_ZH_CN_FALLBACK, start, end)
        return group

    _ZH_CN_FONT = _zh_cn_make_font_group()

    def _zh_cn_font_transform(font):
        # 只接管游戏正文用的 DejaVuSans, 装饰字体保持原样
        if font != "DejaVuSans.ttf":
            return font
        return _ZH_CN_FONT

    config.font_transforms["zh_cn"] = _zh_cn_font_transform

    # 兜底: 走不到 font_transform 的 DejaVuSans 文本
    for is_bold in (False, True):
        for italics in (False, True):
            config.font_replacement_map[("DejaVuSans.ttf", is_bold, italics)] = (_ZH_CN_FALLBACK, is_bold, italics)

    def _zh_cn_apply_fonts():
        _preferences.font_transform = "zh_cn"
        style.say_label.font = _ZH_CN_FONT
        style.nvl_label.font = _ZH_CN_FONT

    config.change_language_callbacks.append(_zh_cn_apply_fonts)

init 1501 python:
    _zh_cn_apply_fonts()
    if not getattr(persistent, "realm_invader_zh_cn_enabled", False):
        _preferences.language = "schinese"
        persistent.realm_invader_zh_cn_enabled = True

# --------------------------------------------------------------------------
#  zz_zh_cn_menu.rpy, verbatim from here down.
# --------------------------------------------------------------------------

## Simplified Chinese main menu.
##
## The original menu drew its title and buttons through the custom
## "MakeVisualNormals.SimulatedLighting" shader (TitleShader / ButtonShader).
## On this machine that shader renders the glyphs almost white, so on the
## menu's white panel the text was effectively invisible while the buttons
## stayed clickable. It also left the text at alpha 0 for the first two
## seconds. The layout, artwork and actions below are unchanged; only the
## text rendering is replaced with plain high-contrast text.

transform zh_cn_menu_fade:
    alpha 0.0
    xoffset 40/scale
    easein 0.35 alpha 1.0 xoffset 0.0

screen main_menu():

    default changemenu = False
    default everchangemenu = False
    default changingmusic = True
    default selectedmenu = 1 if persistent.mainmenuindex == 0 else 0

    python:

        def indexhop(direction, selectedmenu=selectedmenu):
            if direction == "left":
                return (selectedmenu - 1 - (selectedmenu == (persistent.mainmenuindex + 1) % len(allmenus))) % len(allmenus)
            return (selectedmenu + 1 + (selectedmenu == (persistent.mainmenuindex - 1) % len(allmenus))) % len(allmenus)

    if changingmusic:
        timer epsilon action [Play("MainMenuMusic", mmenu().audio), SetScreenVariable("changingmusic", False)]

    add mmenu().background

    frame:
        background None
        add Solid("#ffffff") at MenuBox

        text "{u}Realm Invader{/u}" align (0.5, 0.05) size 150/scale font "Fonts/Megrim.ttf" color "#ffffff" outlines [(absolute(5), "#14141c", 0, 0)] at zh_cn_menu_fade

        vbox:
            spacing 40/scale
            pos (0.09, 0.2)

            textbutton "开始游戏":
                text_font _ZH_CN_FONT
                text_size 90/scale
                text_idle_color "#ffffff"
                text_hover_color "#99ccff"
                text_selected_color "#ffffff"
                text_outlines [(absolute(4), "#14141c", 0, 0)]
                at zh_cn_menu_fade
                action Show("menulandingscreen", _transition=Dissolve(0.5))

            textbutton "读取存档":
                text_font _ZH_CN_FONT
                text_size 90/scale
                text_idle_color "#ffffff"
                text_hover_color "#99ccff"
                text_selected_color "#ffffff"
                text_outlines [(absolute(4), "#14141c", 0, 0)]
                at zh_cn_menu_fade
                action ShowMenu("load")

            textbutton "偏好设置":
                text_font _ZH_CN_FONT
                text_size 90/scale
                text_idle_color "#ffffff"
                text_hover_color "#99ccff"
                text_selected_color "#ffffff"
                text_outlines [(absolute(4), "#14141c", 0, 0)]
                at zh_cn_menu_fade
                action ShowMenu("preferences")

            if renpy.variant("pc"):
                textbutton "退出游戏":
                    text_font _ZH_CN_FONT
                    text_size 90/scale
                    text_idle_color "#ffffff"
                    text_hover_color "#99ccff"
                    text_selected_color "#ffffff"
                    text_outlines [(absolute(4), "#14141c", 0, 0)]
                    at zh_cn_menu_fade
                    action Quit(confirm=not main_menu)

        imagebutton:
            idle "gui/arrow1l.webp"
            action SetScreenVariable("selectedmenu", indexhop("left"))
            at LeftMMButton

        imagebutton:
            anchor (0.5, 1.0)
            pos (0.5, 0.93)
            at MMThumb
            if allmenus[selectedmenu] in persistent.unlockedmenus:
                idle "Main Menu/" + allmenus[selectedmenu] + ".webp"
                action [SetVariable("persistent.mainmenuindex", selectedmenu), SetScreenVariable("changingmusic", True), SetScreenVariable("selectedmenu", indexhop("left"))]
            else:
                idle "Main Menu/LockedMenu.webp"
                action NullAction()

        imagebutton:
            idle "gui/arrow1r.webp"
            action SetScreenVariable("selectedmenu", indexhop("right"))
            at RightMMButton

    hbox:
        align (0.96, 0.96)

        button:
            action OpenURL("https://www.patreon.com/realminvader")
            add "patreonlogo"

        button:
            action OpenURL("https://subscribestar.adult/realminvader")
            add "sslogo"

        button:
            action OpenURL("https://discord.gg/PhswjUryn5")
            add "discordlogo"
