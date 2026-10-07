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
#     3. 能用 MiSans 真实字重(500),而不是 Ren'Py 合成的假粗体。
#
# 覆盖度已实测(见 fontcheck.py / fonttofu.py):
#   译文用到 2956 个非 ASCII 字符,MiSans 命中 2955 个,
#   唯一未覆盖的 U+FEFF 是零宽字符(BOM),渲染为空白属正常。
#   另外逐字渲染比对 .notdef,没有出现「cmap 有字但画出豆腐块」的情况。

init 20 python:
    # 改成 False 即整体切回微软雅黑(fonts/msyh.ttc 仍保留在 game/fonts/)。
    ZH_FONT_USE_MISANS = True

    _MS_OLD = "fonts/msyh.ttc"
    _MS_REG = "fonts/MiSans-Regular.ttf"
    # 强调字重。MiSans 有 400/500/700 三档,实测着墨量是
    # Regular 1.00x / Medium 1.11x / Bold 1.64x。对 CJK 正文而言 700 偏重,
    # 实机对比后改用 500。想回到 700 就把下面这个路径改回去。
    _MS_STRONG = "fonts/MiSans-Medium.ttf"

    def _apply_zh_font():
        # font_replacement_map 的值只能是字符串元组,不能塞 FontGroup,
        # 所以回退链不放这里。
        #
        # 分发补丁时未必附带 MiSans 字体文件,这里先确认字体确实存在,
        # 缺字体就整个跳过接管 —— 脚本仍按原样引用 fonts/msyh.ttc,
        # 中文一样能正常显示,只是字体回落成微软雅黑。
        #
        # NOTE: this has to use a local. Assigning to _MS_STRONG here would make
        # Python treat the name as function-local for the whole body, so the
        # renpy.loadable(_MS_STRONG) read below it would raise UnboundLocalError
        # and take the entire init phase -- and the game -- down with it.
        if not renpy.loadable(_MS_REG):
            return
        bold_face = _MS_STRONG if renpy.loadable(_MS_STRONG) else _MS_REG
        for bold, ital in ((False, False), (False, True),
                           (True, False),  (True, True)):
            face = bold_face if bold else _MS_REG
            # 右边 bold 一律给 False -> 交给真字重,避免二次合成加粗把字糊掉
            config.font_replacement_map[(_MS_OLD, bold, ital)] = (face, False, ital)

    if ZH_FONT_USE_MISANS:
        _apply_zh_font()

    # ---- 对话正文可读性 ------------------------------------------------
    #
    # 原游戏 style.say_dialogue 的描边来自 gui.dialogue_text_outlines
    # 的 [(2, "#00000080", 3, 3)]。按 renpy/text/text.py 的实现:
    #   size -> outline_blits(),把字形对称膨胀出 size 像素的真实光晕;
    #   xo/yo -> 绘制时整块 blit 的偏移量。
    # 两者相抵:2px 光晕被右下平移 3px,左上只剩 -1px(等于没有),
    # 所以实际观感是投影而非描边 -- 笔画偏细的 MiSans 压在亮背景上就发虚。
    #
    # 这里拆成「真对称光晕 + 一层轻投影」,保住原设计的立体感,
    # 同时四个方向都有底;再叠上 MiSans 的真 Bold 字重。
    #
    # 只改样式对象,不动 screens.rpy / gui.rpy。优先级上一定生效:
    # 引擎主题跑在 init -1110,游戏样式语句在 init 0,本文件在 init 20。
    # style.say_thought is say_dialogue,内心独白会一并生效。

    ZH_DIALOGUE_TUNING = True
    ZH_DIALOGUE_BOLD   = True

    # 对称光晕(size 2) + 轻投影(size 1,右下偏移)。
    # 想更收敛就把光晕的 size 调小,或把整段改成 []。
    # 注意:size 不只是光晕宽度,它同时会把字形向外膨胀,
    # 对粗字体说就是一次额外的加粗。Bold 本身已经够重,
    # 所以光晕只留 1px,提供分离度而不再叠加重量。
    ZH_DIALOGUE_OUTLINES = [
        (1, "#000000a0", 0, 0),
        (1, "#00000050", 3, 3),
    ]

    def _apply_dialogue_tuning():
        if not ZH_DIALOGUE_TUNING:
            return
        style.say_dialogue.outlines = ZH_DIALOGUE_OUTLINES
        if ZH_DIALOGUE_BOLD:
            # 请求 bold -> 命中 font_replacement_map 里的真 MiSans-Bold。
            # 映射右值的 bold 恒为 False,所以不会再叠一层合成加粗。
            style.say_dialogue.bold = True

    _apply_dialogue_tuning()

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
