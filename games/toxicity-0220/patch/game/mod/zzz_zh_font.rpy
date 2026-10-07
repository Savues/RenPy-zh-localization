# zzz_zh_font.rpy
# -*- coding: utf-8 -*-
#
# 汉化字体接管
#
# 插件原本给界面文字指定了两款装饰字体:
#     mod/Monster Racing - Personal Used.otf
#     fonts/DCC - Ash.otf
# 这两款字体各自只有一百多个码位,完全不含中文字形,
# 直接写中文会全部变成豆腐块(空白方框)。
#
# 这里不去改动插件脚本里的任何 font 写法,而是在初始化阶段
# 把这两个字体整体「替换」成可以显示中文的字体,
# 因此本文件可以随补丁一起覆盖安装,不影响原文件的其它内容。
#
# 想关掉接管:把下面的 ZH_FONT_REMAP 改成 False 即可。

define ZH_FONT_REMAP = True

init 20 python:
    # 优先使用 MiSans;没有则退回微软雅黑(同样含中文字形)
    ZH_FONT_REGULAR_CANDIDATES = ["fonts/MiSans-Regular.ttf", "fonts/msyh.ttc"]
    ZH_FONT_BOLD_CANDIDATES = ["fonts/MiSans-Bold.ttf", "fonts/msyh.ttc"]

    # 需要接管的装饰字体
    ZH_FONT_SOURCES = [
        "mod/Monster Racing - Personal Used.otf",
        "fonts/DCC - Ash.otf",
    ]

    def zh_font_pick(candidates):
        for path in candidates:
            if renpy.loadable(path):
                return path
        return None

    def zh_font_apply():
        if not ZH_FONT_REMAP:
            return
        regular = zh_font_pick(ZH_FONT_REGULAR_CANDIDATES)
        if not regular:
            return
        bold = zh_font_pick(ZH_FONT_BOLD_CANDIDATES) or regular
        for source in ZH_FONT_SOURCES:
            for is_bold in (False, True):
                for is_italic in (False, True):
                    config.font_replacement_map[(source, is_bold, is_italic)] = (
                        bold if is_bold else regular, False, is_italic,
                    )

    zh_font_apply()