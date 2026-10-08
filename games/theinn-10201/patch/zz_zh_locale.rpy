# 《The Inn》简体中文本地化 · 语言启用
#
# 本作没有可用的语言选择入口，Ren'Py 的 config.enable_language_autodetect 也保持关闭，
# 因此必须在这里显式把语言钉死在简体中文，中文翻译才会生效。
#
# 光写 config.default_language 是不够的，原因有两条，都在本文件里处理：
#
# 1) 老存档已经记住了 language
#    Ren'Py 的 _apply_default_preferences()（renpy/common/00defaults.rpy，init 1500）
#    只在玩家「第一次运行」——即 persistent._set_preferences 为 False——时才会把
#    config.default_language 写进 _preferences.language。已经玩过的存档里 language
#    早已是 english，单独写 config.default_language 对老存档完全无效。
#    所以 init 1999 直接写 _preferences.language；这个时机晚于
#    main() 里的 renpy.persistent.update()（读存档）和 init 1500 的偏好套用，
#    同时早于 label _start 里 00start.rpy:217 的 _init_language()。
#
# 2) 启动画面会把语言改回英文
#    label _start 在 _init_language() 之后还会走 splashscreen，
#    game/game_splashscreen.rpy:9 调用了 game/game_classes.rpy:1496 的 auto_lang()，
#    它内部执行 renpy.change_language("english")，把刚设好的中文又覆盖回英文，
#    结果就是 1761 条中文字幕全部不加载（实测 preferences.language 变回 'english'，
#    translate_string("EXTRAS") 从「特典」退回 "EXTRAS"，字体映射同时被清掉）。
#    init 2999 在 splashscreen 之前给 renpy.change_language 包一层，
#    把这个回退请求改写回简体中文。
#
# 语言真正切换成功后，tl/simplified_chinese/zzz_fonts.rpy 里的中文字体替换
# 会由 Ren'Py 一并执行（实测 font_name_map 填充 39 项）。
#
# 想改回英文原版？删除本文件即可。

define config.default_language = "simplified_chinese"

init 1999 python:
    config.language = "simplified_chinese"
    _preferences.language = "simplified_chinese"

init 2999 python:
    def _inn_language_guard(_orig_change_language):
        # 用闭包把原始函数锁住：init 块里的名字都挂在 store 上，
        # 直接引用全局名会在 store 被清理后变成 NameError。
        def _change_language(language, force=False, rebuild=False):
            # auto_lang() 想切回 english；简体中文本地化下不予放行。
            if language == "english":
                language = "simplified_chinese"
            return _orig_change_language(language, force=force, rebuild=rebuild)
        return _change_language

    renpy.change_language = _inn_language_guard(renpy.change_language)