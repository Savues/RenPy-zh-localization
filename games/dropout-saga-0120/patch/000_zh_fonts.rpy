# -*- coding: utf-8 -*-
# =============================================================================
#  DropOut Saga 简体中文本地化补丁 —— 中文字体
#
#  字体：MiSans（小米），Regular + Bold 两套静态字重。
#  选静态版而非 "MiSans VF.ttf" 可变版：Ren'Py 8.3 的粗体走
#  config.font_replacement_map 直接换字体文件，可变字重的 weight 轴用不上，
#  而静态版少占 12MB。
#
#  为什么必须动 style default：
#  引擎 renpy/common/00style.rpy 把默认样式字体硬编码成 "DejaVuSans.ttf"，
#  而游戏 gui.rpy 虽然定义了 gui.text_font 等变量，很多样式却没套用它们。
#  只改 gui.* 不生效，中文会显示成方块。
# =============================================================================

init python:

    CJK_FONT = "Fonts/MiSans-Regular.ttf"
    CJK_BOLD = "Fonts/MiSans-Bold.ttf"

    # 引擎解析粗体的位置是 renpy/text/font.py:714
    #     (font, bold, italic) -> renpy.config.font_replacement_map.get(...)
    # 命中后把 bold 置 False，否则 FreeType 会在真粗体上再叠一层伪粗体糊字。
    # 斜体 MiSans 没有对应字重，保持缺省——引擎自己合成倾斜，观感与之前一致。
    config.font_replacement_map[(CJK_FONT, True, False)] = (CJK_BOLD, False, False)
    config.font_replacement_map[(CJK_FONT, True, True)] = (CJK_BOLD, False, True)

init 999 python:

    # 优先级 999 晚于引擎 00style.rpy 里那个优先级 0 的 style default，
    # 否则这里赋的值会被引擎随后覆盖回 DejaVuSans。
    style.default.font = CJK_FONT

# =============================================================================
#  快进指示三角：游戏原本刻意指定 DejaVuSans，源码注释写得很明白——
#  全游戏只有它带 BLACK RIGHT-POINTING SMALL TRIANGLE (U+25B8)。
#  MiSans 和 Noto 都没有这个字形，一旦被中文字体接管就是方块，所以钉死。
#  apply.py 那边也把这个 style 排除在字体替换之外，两处互为保险。
# =============================================================================

style skip_triangle:
    font "DejaVuSans.ttf"

# =============================================================================
#  引擎内置字符串（renpy/common/00gui.rpy）的中文化。
#
#  这些字符串写死在引擎里，不在 scripts.rpa 中，改不了源码，
#  所以在比引擎 init 块（init -1150）更晚的优先级里直接覆盖变量。
#  覆盖的是"确定吗？"这类确认框提示，配合 screens.rpy 里已汉化的
#  是/否按钮，整个 confirm 对话框就都是中文了。
# =============================================================================

init -1149 python:

    import store.gui as _gui

    _gui.ARE_YOU_SURE = "确定吗？"
    _gui.DELETE_SAVE = "确定要删除这个存档吗？"
    _gui.OVERWRITE_SAVE = "确定要覆盖这个存档吗？"
    _gui.LOADING = "读取存档会丢失尚未保存的进度。\n确定要继续吗？"
    _gui.QUIT = "确定要退出游戏吗？"
    _gui.MAIN_MENU = "确定要返回主菜单吗？\n这会丢失尚未保存的进度。"
    _gui.CONTINUE = "确定要从上次的地方继续吗？"
    _gui.END_REPLAY = "确定要结束回放吗？"
    _gui.SLOW_SKIP = "确定要开始快进吗？"
    _gui.FAST_SKIP_SEEN = "确定要快进到下一个选项吗？"
    _gui.FAST_SKIP_UNSEEN = "确定要跳过未读对话直到下一个选项吗？"
    _gui.UNKNOWN_TOKEN = "此存档来自另一台设备。恶意伪造的存档可能损坏你的电脑。你信任这个存档的作者，以及所有可能改动过它的人吗？"
    _gui.TRUST_TOKEN = "你信任创建此存档时所用的设备吗？只有当这台设备的使用者只有你时，才应选择「是」。"
# =============================================================================
#  Shawn's Mod 自带字体 -> MiSans
#
#  MOD 在 game/mod/ 下面塞了 6 个拉丁字体，并在 Shawn_Styles.rpyc / Shawn_Screens.rpyc
#  里把它们写死到 style 和 screen 的 font / text_font 上：
#      mod/OS.ttf                      style say_label / window 等（正文）
#      mod/OSB.ttf                     按钮文字（本来是粗体字重）
#      mod/fonts/Proxima Nova Semibold.otf   MOD 标题
#      mod/fonts/Roboto-Light.ttf      攻略正文
#      mod/fonts/Roboto-Thin.ttf       攻略正文
#      mod/fonts/AktivGrotesk-Light.otf     随包附带，暂未被引用
#      mod/fonts/BebasNeue Regular.otf      随包附带，暂未被引用
#  外加 fonts/Firestarter_Z.ttf（游戏自带、MOD 用来画 screen_tooltip 提示条），
#  这几个字体都没有中文字形，不接管的话 MOD 菜单和攻略全是方块。
#
#  走 config.font_replacement_map 而不是改 style：MOD 的样式定义在 .rpyc 里，
#  init 优先级未知，硬改 style 容易和它打架；而 renpy/text/font.py:714 的
#  get_font() 是所有字体请求（含 text_font）的唯一收口，映射一次就全覆盖，
#  也不会碰到 MOD 自己文件里的字节。
# =============================================================================

init python:

    MOD_FONT_MAP = {
        "mod/OS.ttf": CJK_FONT,
        "mod/OSB.ttf": CJK_BOLD,
        "mod/fonts/Proxima Nova Semibold.otf": CJK_BOLD,
        "mod/fonts/Roboto-Light.ttf": CJK_FONT,
        "mod/fonts/Roboto-Thin.ttf": CJK_FONT,
        "mod/fonts/AktivGrotesk-Light.otf": CJK_FONT,
        "mod/fonts/BebasNeue Regular.otf": CJK_BOLD,
        "fonts/Firestarter_Z.ttf": CJK_BOLD,
    }

    # 替换过去后一律 bold=False：CJK_BOLD 本身就是粗体字重，再让 FreeType
    # 叠一层合成粗体只会糊字。斜体 MiSans 没有对应字重，保持原样由引擎合成。
    for _mod_font, _zh_font in MOD_FONT_MAP.items():
        for _b in (False, True):
            for _i in (False, True):
                config.font_replacement_map[(_mod_font, _b, _i)] = (_zh_font, False, _i)

    del _mod_font, _zh_font, _b, _i
