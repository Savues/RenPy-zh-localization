# zzz_font_misans.rpy
# -*- coding: utf-8 -*-
#
# 汉化界面字体:微软雅黑 -> MiSans
#
# 为什么不直接改 295 处 "fonts/msyh.ttc":
#   全工程对该字体的引用是同一个字面量(gui.text_font / name_text_font /
#   interface_text_font / Character(what_font=) / {font=...} 标签)。
#   用 config.font_replacement_map 一次性接管,好处是:
#     1. 不动任何脚本文本 -> 译文与标签校验(tags.py)完全不受影响;
#     2. 改一个开关即可切回;
#     3. 能用 MiSans 的真 Bold 字重,而不是 Ren'Py 合成的假粗体。
#
# 覆盖度已实测(见 fontcheck.py / fonttofu.py):
#   译文用到 2956 个非 ASCII 字符,MiSans 命中 2955 个,
#   唯一未覆盖的 U+FEFF 是零宽字符(BOM),渲染为空白属正常。
#   另外逐字渲染比对 .notdef,没有出现「cmap 有字但画出豆腐块」的情况。

init 20 python:
    # 改成 False 即整体切回微软雅黑(fonts/msyh.ttc 仍保留在 game/fonts/)。
    ZH_FONT_USE_MISANS = True

    _MS_OLD  = "fonts/msyh.ttc"
    _MS_REG  = "fonts/MiSans-Regular.ttf"
    _MS_BOLD = "fonts/MiSans-Bold.ttf"

    def _apply_zh_font():
        # font_replacement_map 的值只能是字符串元组,不能塞 FontGroup,
        # 所以回退链不放这里。
        #
        # 分发补丁时未必附带 MiSans 字体文件,这里先确认字体确实存在,
        # 缺字体就整个跳过接管 —— 脚本仍按原样引用 fonts/msyh.ttc,
        # 中文一样能正常显示,只是字体回落成微软雅黑。
        #
        # NOTE: this has to use a local. Assigning to _MS_BOLD here would make
        # Python treat the name as function-local for the whole body, so the
        # renpy.loadable(_MS_BOLD) read below it would raise UnboundLocalError
        # and take the entire init phase -- and the game -- down with it.
        if not renpy.loadable(_MS_REG):
            return
        bold_face = _MS_BOLD if renpy.loadable(_MS_BOLD) else _MS_REG
        for bold, ital in ((False, False), (False, True),
                           (True, False),  (True, True)):
            face = bold_face if bold else _MS_REG
            # 右边 bold 一律给 False -> 交给真字重,避免二次合成加粗把字糊掉
            config.font_replacement_map[(_MS_OLD, bold, ital)] = (face, False, ital)

    if ZH_FONT_USE_MISANS:
        _apply_zh_font()

    # 运行时探针:确认引擎真的把请求换成了 MiSans
    def _zh_font_report():
        try:
            from renpy.text.font import load_face
            lines = []
            for label, b in (("regular", False), ("bold", True)):
                f = load_face(_MS_OLD, b, False)
                name = getattr(getattr(f, "face", None), "family_name", None)
                lines.append("%-8s -> %s" % (label, name if name else repr(f)))
            return "\n".join(lines)
        except Exception as e:
            return "probe failed: %r" % (e,)
