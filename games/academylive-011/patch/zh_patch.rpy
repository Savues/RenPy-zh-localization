# ============================================================================
#  AcademyLive 0.11 - 简体中文本地化补丁
# ----------------------------------------------------------------------------
#  本文件是纯附加补丁，不修改任何原版脚本。
#  原版脚本仍完整保留在 scripts.rpa 内，未被解包、未被修改。
#  所有翻译文本均放在 game/tl/schinese/ 下，由 Ren'Py 官方翻译机制覆盖。
#
#  回滚到纯英文原版：删除 game/tl/ 目录与本文件即可。
# ============================================================================

## 首次运行默认使用简体中文；若玩家已保存过语言偏好，则以保存值为准。
default preferences.language = "schinese"

define zh_font = "fonts/NotoSansSC-VariableFont_wght.ttf"


## ---------------------------------------------------------------------------
## 中文字体注入
##
## gui.*_font 是被 gui.text_properties() 读进样式的，而样式一旦建好、屏幕分析
## 结束就固化在内存里，改变量不再生效。原补丁在 init 999 才改 gui 变量，
## 那时 style default / say_dialogue 早已用英文字体建好，于是中文全部落到
## AtkinsonHyperlegible（无 CJK 字形）上，渲染成一排方块。
##
## gui.rpy 是 `init offset = -2`，screens.rpy 的 style 语句在 init 0。
## 所以 -1 是唯一既能盖过 gui.rpy 的 define、又早于全部 style 的时机。
## ---------------------------------------------------------------------------

init -1 python:

    ## `define zh_font` 是 init 0，这里还拿不到，所以直接写字面量。
    _zh_font_early = "fonts/NotoSansSC-VariableFont_wght.ttf"

    if renpy.loader.loadable(_zh_font_early):

        gui.text_font = _zh_font_early
        gui.name_text_font = _zh_font_early
        gui.interface_text_font = _zh_font_early
        gui.button_text_font = _zh_font_early
        gui.choice_button_text_font = _zh_font_early

        ## 底底为网：原版脚本里写死了英文字体的地方，通过
        ## config.font_replacement_map 统一换成中文字体。这个映射在字体加载时生效，
        ## 所以它能盖住 style default（引擎在 renpy/common/00style.rpy:139 写死 DejaVuSans）、
        ## 各样式的硬编码字体，以及文本里的 {font=...} 内联标签。
        for _zh_old_font in [
                "DejaVuSans.ttf",
                "gui/fonts/DejaVuSans.ttf",
                "gui/fonts/AtkinsonHyperlegible-Bold.ttf",
                "gui/fonts/CrimsonText-SemiBold.ttf",
                "gui/fonts/JosefinSans-SemiBold.ttf",
                "gui/fonts/YsabeauOffice-Regular.ttf",
        ]:
            for _zh_bold in (False, True):
                for _zh_italic in (False, True):
                    config.font_replacement_map[(_zh_old_font, _zh_bold, _zh_italic)] = (
                        _zh_font_early, False, False)


## ---------------------------------------------------------------------------
## 姓名本地化
##
## 游戏在八处对角色名做相等比较，例如 events.rpy:
##     if em.name == "Emiko":
## 因此不能直接把 name 改成中文 —— 那正是上一版汉化改坏比较逻辑的原因。
##
## 这里改在「显示层」：用 str 子类显示中文，同时 == 仍与英文原名相等。
## 姓名在名牌与 [x.name] / [x.surname] 插值中都显示中文，
## 而相等比较、字典查找、字符串拼接的行为完全不变。
## ---------------------------------------------------------------------------



## 角色：(Actor 变量, Character 变量, 英文名, 中文名)
## Character 变量决定名牌显示，Actor 变量决定 [x.name] 插值显示。
define _ZH_CHARS = [
        ("ayumi", "ay", "Ayumi", "亚由美"),
        ("emiko", "em", "Emiko", "惠美子"),
        ("haruka", "ha", "Haruka", "春香"),
        ("maiya", "ma", "Mai", "舞"),
        ("kiyomi", "k", "Kiyomi", "清美"),
        ("kaito", "bf", "Kaito", "海斗"),
        ("kaori", "ka", "Kaori", "佳织"),
        ("masayuki", "mas", "Masayuki", "正幸"),
        ("genpachi", "gen", "Genpachi", "源八"),
        ("hiroshige", "hiro", "Hiroshige", "博重"),
        ("izo", "iz", "Izo", "伊藏"),
        ("miyako", "miy", "Miyako", "美夜子"),
        ("nanako", "nan", "Nanako", "七菜子"),
        ("natsuha", "nat", "Natsuha", "菜摘"),
        ("rina", "ri", "Rina", "莉奈"),
        ("ryoichi", "ryo", "Ryoichi", "亮一"),
        ("satsuki", "sats", "Satsuki", "皐月"),
        ("sayoko", "sayo", "Sayoko", "沙织子"),
        ("suzu", "suz", "Suzu", "铃"),
        ("soushi", "sou", "Soushi", "宗士"),
        ("sotaro", "sot", "Sotaro", "悟太郎"),
        ("yoko", "yo", "Yoko", "洋子"),
        ("yuna", "yun", "Yuna", "优奈"),
        ("masaru", "masa", "Masaru", "雅春"),
        ("koji", "ph", "Koji", "浩二"),
        ("marcus", "mar", "Marcus", "马库斯"),
        ("hidetoshi", "hi", "Hidetoshi", "秀俊"),
        ("satoe", "sat", "Satoe", "里惠"),
        ("president", "ap", "Academy President", "理事长"),
]

## 不对应 Actor、只需改名牌的角色。
define _ZH_CHARS_EXTRA = [
        ("mm", "Mysterious Man", "神秘男子"),
        ("barman", "Bar Man", "酒保"),
]

## 名字里带 _() 拼接或文本标签的角色，需单独指定。
define _ZH_CHARS_SPECIAL = [
        ("mct", "[mcname] {size=-6}{i}(Thinking){/i}{/size}", "[mcname] {size=-6}{i}（思考）{/i}{/size}"),
        ("mcT", "[mcname] {size=-6}{i}(Thinking){/i}{/size}", "[mcname] {size=-6}{i}（思考）{/i}{/size}"),
        ("mi", "Mrs. Mikumo", "三云夫人"),
]

## Actor 的名是字面量而非 Character 名的两个角色。
define _ZH_ACTOR_NAMES = [
        ("president", "Eiichi", "英一"),
        ("maiya", "Maiya", "舞"),
]

## Actor 数据对象：(store 变量, 英文姓, 中文姓)
## 姓只用于插值显示，代码中从不参与比较，因此可以安全替换。
define _ZH_SURNAMES = [
        ("main", "Watanabe", "渡边"),
        ("kiyomi", "Yamashita", "山下"),
        ("president", "Matsuzaki", "松崎"),
        ("masaru", "Nakagawa", "中川"),
        ("koji", "Fujima", "藤间"),
        ("masayuki", "Suzuki", "铃木"),
        ("kaito", "Harada", "原田"),
        ("hidetoshi", "Kawaguchi", "川口"),
        ("marcus", "Crawford", "克劳福德"),
        ("satoe", "Okamoto", "冈本"),
        ("kaori", "Nakamura", "中村"),
        ("ayumi", "Suzuki", "铃木"),
        ("emiko", "Brown", "布朗"),
        ("haruka", "Ito", "伊藤"),
        ("maiya", "Sato", "佐藤"),
        ("genpachi", "Keiho", "京邦"),
        ("hiroshige", "Yagami", "八神"),
        ("izo", "Takei", "武井"),
        ("miyako", "Higashi", "东"),
        ("nanako", "Ueda", "上田"),
        ("natsuha", "Kazumiya", "一宫"),
        ("rina", "Hoshino", "星野"),
        ("ryoichi", "Tanaka", "田中"),
        ("sayoko", "Kamiya", "神谷"),
        ("satsuki", "Morikawa", "森川"),
        ("soushi", "Nagai", "永井"),
        ("sotaro", "Kogane", "小金"),
        ("suzu", "Akibara", "秋原"),
        ("yoko", "Iwasaki", "岩崎"),
        ("yuna", "Uyehara", "上原"),
]

## 记录原始英文值，切回英文时据此还原。
define _ZH_ORIGINALS = dict()

## 供 Actor.__init__ 使用的查表。
define _ZH_SURNAME_MAP = dict((en, zh) for _a, en, zh in _ZH_SURNAMES)
define _ZH_LITERAL_NAME_MAP = dict((en, zh) for _a, en, zh in _ZH_ACTOR_NAMES)


init 999 python:

    import os

    class _ZhName(str):
        """显示为中文、但仍与英文原名相等比较的字符串。"""

        def __new__(cls, zh, en):
            self = str.__new__(cls, zh)
            self.en = en
            return self

        def __eq__(self, other):
            if isinstance(other, str) and not isinstance(other, _ZhName):
                if other == self.en:
                    return True
            return str.__eq__(self, other)

        def __ne__(self, other):
            r = self.__eq__(other)
            return r if r is NotImplemented else not r

        def __hash__(self):
            return str.__hash__(self)

    def _zh_font_exists():
        return os.path.exists(os.path.join(renpy.config.gamedir, *zh_font.split("/")))

    ## 这些样式在原版脚本里把字体写死了，不走 gui 变量，
    ## 所以 style default 的覆盖对它们无效，只能逐个改。
    ##   say_dialogue          screens.rpy       AtkinsonHyperlegible-Bold  <- 对话正文
    ##   centered_text         screens.rpy       AtkinsonHyperlegible-Bold
    ##   menu_text_button_custom screens.rpy     JosefinSans-SemiBold
    ##   header_title_text     defines and defaults.rpy  CrimsonText-SemiBold
    ##   screen_text           phone_game_view_screen.rpy JosefinSans-SemiBold
    ##   skip_triangle / japanese_text 保留原版（纯符号 / 韩文字体）。
    ## style default 是所有样式的根，它的 font 来自
    ## gui.text_properties() 读取的 gui.text_font。实测这里实际落到了
    ## Ren'Py 内置的 DejaVuSans.ttf（无任何 CJK 字形），所以必须直接强制。
    _ZH_STYLE_FONTS = [
        "default",
        "say_dialogue",
        "say_thought",
        "say_label",
        "centered_text",
        "button_text",
        "label_text",
        "namebox",
        "namebox_name",
        "namebox_prefixes",
        "namebox_button",
        "notify",
        "input",
        "gui_text",
        "gui_label",
        "gui_label_text",
        "main_menu",
        "title",
        "version",
        "menu_text_button_custom",
        "header_title_text",
        "screen_text",
        "pref_label_text",
        "radio_button_text",
        "check_button_text",
        "slider_button_text",
        "jump_button_text",
    ]

    def _zh_apply_font():
        """把字体统一指向 Noto Sans SC（含完整汉字字形）。"""
        if not _zh_font_exists():
            return

        gui.text_font = zh_font
        gui.name_text_font = zh_font
        gui.interface_text_font = zh_font
        gui.button_text_font = zh_font
        gui.choice_button_text_font = zh_font

        ## StyleManager.__getattr__ 对不存在的样式会直接抛异常（而不是返回 None），
        ## 所以逐个 try：只改存在的样式，缺失的跳过。
        for _style_name in _ZH_STYLE_FONTS:
            try:
                getattr(style, _style_name).font = zh_font
            except Exception as _e:
                _ZH_STYLE_FAIL.append("%s: %r" % (_style_name, _e))

    _ZH_STYLE_FAIL = []

    def _zh_apply_names():
        """名牌与字面量姓名。Character 由 define 在 init 期创建，可直接改。"""
        if _preferences.language != "schinese":
            for key, value in list(_ZH_ORIGINALS.items()):
                setattr(key[0], key[1], value)
            _ZH_ORIGINALS.clear()
            return

        for _actor_var, char_var, en, zh in _ZH_CHARS:
            put_name(char_var, en, zh)
        for char_var, en, zh in _ZH_CHARS_EXTRA:
            put_name(char_var, en, zh)
        for char_var, en, zh in _ZH_CHARS_SPECIAL:
            put_name(char_var, en, zh)

    def put_name(char_var, en, zh):
        obj = getattr(renpy.store, char_var, None)
        if obj is None or not hasattr(obj, "name"):
            return
        key = (obj, "name")
        if key not in _ZH_ORIGINALS:
            _ZH_ORIGINALS[key] = getattr(obj, "name")
        obj.name = _ZhName(zh, en)

    def _zh_patch_actor_init():
        """
        Actor 对象由 default 语句在 store 创建时构造，比 init 晚，
        因此这里 hook Actor.__init__，连游戏中途新增的角色也能覆盖到。
        """
        Actor = getattr(renpy.store, "Actor", None)
        if Actor is None or getattr(Actor, "_zh_patched", False):
            return

        original = Actor.__init__

        def __init__(self, character, surname, name, nametag, title, gender,
                     personality, topics, dictionary, location, outfit,
                     available, met, virgin, sexstats):
            original(self, character, surname, name, nametag, title, gender,
                     personality, topics, dictionary, location, outfit,
                     available, met, virgin, sexstats)
            if _preferences.language != "schinese":
                return
            zh = _ZH_SURNAME_MAP.get(surname)
            if zh:
                self.surname = _ZhName(zh, surname)
            zh = _ZH_LITERAL_NAME_MAP.get(name)
            if zh:
                self.name = _ZhName(zh, name)

        __init__.__doc__ = original.__doc__
        Actor.__init__ = __init__
        Actor._zh_patched = True

    def _zh_apply_all():
        _zh_apply_font()
        _zh_apply_names()
        _zh_patch_actor_init()

    ## change_language 会在回调之后重建样式并重启交互，因此这里改完即生效。
    config.change_language_callbacks.append(_zh_apply_all)
    _zh_apply_all()

    ## -----------------------------------------------------------------------
    ## 菜单选项特殊：标题前会被先拼上 {size=[choice_text_size]} 这类前缀
    ##
    ## Ren'Py 渲染 menu: 选项时，会把选项文本包装成
    ##     {size=[choice_text_size]}I have some questions...
    ## 再去查 strings: 表。而 tl/schinese 里的 key 是素原文（未前缀的），
    ## 完全对不上，菜单就退回英文。
    ## Ren'Py 自带的兜底只剥 {#...}（注释型标签），对这种前缀无效。
    ##
    ## 解决：在每次查表失败时，再把所有 {...} 标签剥掉重试一次，
    ## 命中后把前缀原样存回去，保留原有字号。这一个兜底只是放宽查找规则，
    ## 不会改动任何已正常命中的查询。
    ## -----------------------------------------------------------------------

    def _zh_patch_string_lookup():
        import re as _re
        import types as _types

        _stl = renpy.game.script.translator.strings.get("schinese")
        if _stl is None or getattr(_stl, "_zh_lookup_patched", False):
            return

        _orig = _stl.translate
        _tag_re = _re.compile(r"\{[^{}]*\}")
        _prefix_re = _re.compile(r"^((?:\{[^{}]*\}[ \t]*)+)")

        def _translate(self, s):
            new = self.translations.get(s, None)
            if new is not None:
                return new

            stripped = _tag_re.sub("", s)
            if stripped != s:
                new = self.translations.get(stripped, None)
                if new is not None:
                    m = _prefix_re.match(s)
                    if m:
                        return m.group(1) + new
                    return new

            ## _orig 已经是绑定过的方法，不能再传 self。
            return _orig(s)

        _stl.translate = _types.MethodType(_translate, _stl)
        _stl._zh_lookup_patched = True

    _zh_patch_string_lookup()



screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton _("English") action Language(None)
                    textbutton _("简体中文") action Language("schinese")


                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

                vbox:
                    style_prefix "slider"
                    label _("Dialogue box opacity")
                    bar value FieldValue(persistent, "dialogueBoxOpacity", range=1.0, style="slider")

                vbox:
                    # style_prefix "slider"
                    # label _("Text Size")
                    # bar value Preference("font size")
                    # textbutton _("Reset"):
                    #     action [SetVariable("_preferences.font_size", 1.0), Function(gui.rebuild)]
                    style_prefix "radio"
                    label _("Text Size")
                    hbox:
                        textbutton _("Small"):
                            action [SetVariable("_preferences.font_size", 0.8), Function(gui.rebuild)]
                        textbutton _("Normal"):
                            action [SetVariable("_preferences.font_size", 1.0), Function(gui.rebuild)]
                        textbutton _("Big"):
                            action [SetVariable("_preferences.font_size", 1.3), Function(gui.rebuild)]                                 

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")
            

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Animation Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

## 下方为原版 screen preferences() 的完整副本，
## 唯一改动是启用了开发者预留的语言切换块（原被注释掉）。


## ---------------------------------------------------------------------------
