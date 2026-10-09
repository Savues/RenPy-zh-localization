# ============================================================
#  中文本体配置 —— City Devil: Restart 中文版
#
#  注意：gui.rpy 顶部有 `init offset = -2`，它把里面的字体 define
#  （gui.text_font 等，默认指向不含中文字形的拉丁字体
#  titilliumwebrusbydaymarius）放到 init -2 执行。若在更早的
#  init（如 -100）里覆盖 gui.*_font，会被 gui.rpy 反向覆盖；
#  而 gui.rpy 在 init -2 注册的同名 @gui.variant 也会顶掉我们的
#  variant，导致所有分支最终都用拉丁字体，中文渲染成空白。
#
#  解决办法：本文件全部放在 init 999（远晚于 gui.rpy 的 -2）执行，
#  1) 直接改写 gui.*_font 变量；
#  2) 显式给默认样式和全部文本样式设置 font —— 因为 say_dialogue 等
#     样式在 gui 初始化时已各自持有 gui.text_font 的（拉丁）值，
#     只改 gui 变量不会追溯更新它们，必须逐个显式覆盖。
# ============================================================

init 999 python:
    zh_font      = "tl/schinese/schinese.ttf"
    zh_name_font = "tl/schinese/schinese2.ttf"

    # 覆盖 gui 字体变量（优先级高于 gui.rpy 的 init -2）
    for _a in ("system_font", "main_font", "text_font", "interface_text_font",
               "button_text_font", "choice_button_text_font", "label_text_font",
               "notify_text_font", "tooltip_font", "italic_font", "keymap_font",
               "game_menu_font"):
        setattr(gui, _a, zh_font)
    for _a in ("name_text_font", "nvl_name_text_font", "history_name_text_font"):
        setattr(gui, _a, zh_name_font)

# 显式给默认样式与所有文本样式设置字体，确保中文可见。
init 999:
    style default:
        font "tl/schinese/schinese.ttf"
    # 对白（ADV / NVL）
    style say_dialogue:
        font "tl/schinese/schinese.ttf"
    style say_label:
        font "tl/schinese/schinese2.ttf"
    style nvl_dialogue:
        font "tl/schinese/schinese.ttf"
    style nvl_thought:
        font "tl/schinese/schinese.ttf"
    style nvl_name:
        font "tl/schinese/schinese2.ttf"
    # 界面 / 按钮 / 菜单
    style button_text:
        font "tl/schinese/schinese.ttf"
    style choice_button_text:
        font "tl/schinese/schinese.ttf"
    style label_text:
        font "tl/schinese/schinese.ttf"
    style notify:
        font "tl/schinese/schinese.ttf"
    style tooltip:
        font "tl/schinese/schinese.ttf"
    style gui_tooltip:
        font "tl/schinese/schinese.ttf"
    style keymap:
        font "tl/schinese/schinese.ttf"
    style game_menu:
        font "tl/schinese/schinese.ttf"
    style italic:
        font "tl/schinese/schinese.ttf"
    style name_label:
        font "tl/schinese/schinese2.ttf"
    style history_name:
        font "tl/schinese/schinese2.ttf"
