init offset = -1

default persistent.pages_range = 0

init python:

    def pages_range():
        page = int(persistent._file_page)

        if page % 10 == 0:
            return (page // 10) - 1
        else:
            return page // 10

    if persistent.pages_range is None:
        if unicode(persistent._file_page).isnumeric():
            persistent.pages_range = pages_range()
        else:
            persistent.pages_range = 0

    class FilePageLabel(Action, DictEquality):

        def __init__(self, page):
            self.page = str(page)

            if page == "auto":
                self.alt = _("自动存档页")
            elif page == "quick":
                self.alt = _("快速存档页")
            else:
                self.alt = _("存档页 [text]")

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page

            if unicode(self.page).isnumeric():
                persistent.pages_range = pages_range()

            renpy.restart_interaction()

        def get_selected(self):
            return self.page == persistent._file_page

        def predict(self):
            _predict_file_page(self.page)

    class FilePageForward(Action, DictEquality):
        alt = _("下一页存档。")

        def __init__(self, max=99, wrap=False, auto=False, quick=False, increment=1):
            page = persistent._file_page

            if page == "auto":
                if increment == 10:
                    page = str((persistent.pages_range + 1) * 10 + 1)
                elif config.has_quicksave and quick:
                    page = "quick"
                else:
                    page = "1"

            elif page == "quick":
                if increment == 10:
                    page = str((persistent.pages_range + 1) * 10 + 1)
                else:
                    page = "1"

            else:
                page = int(page) + increment

                if max is not None:
                    if page > max:
                        if wrap:
                            if config.has_autosave and auto:
                                page = "auto"
                            elif config.has_quicksave and quick:
                                page = "quick"
                            else:
                                page = "1"
                        else:
                            page = None

                if page is not None:
                    page = str(page)

            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page

            if unicode(self.page).isnumeric():
                persistent.pages_range = pages_range()

            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page is not None

        def predict(self):
            _predict_file_page(self.page)

    class FilePageBack(Action, DictEquality):
        alt = _("上一页存档。")

        def __init__(self, max=None, wrap=False, auto=False, quick=False, decrement=1):

            if wrap and max is not None:
                max = str(max)
            else:
                max = None

            page = persistent._file_page

            if page == "auto":
                if decrement == 10 and persistent.pages_range > 0:
                    page = str((persistent.pages_range - 1) * 10 + 1)
                else:
                    page = max

            elif page == "quick":
                if decrement == 10 and persistent.pages_range > 0:
                    page = str((persistent.pages_range - 1) * 10 + 1)
                elif decrement == 1 and config.has_autosave and auto:
                    page = "auto"
                else:
                    page = max

            elif page == "1":
                if decrement == 1 and config.has_quicksave and quick:
                    page = "quick"
                elif decrement == 1 and config.has_autosave and auto:
                    page = "auto"
                else:
                    page = max

            else:
                if int(page) <= decrement:
                    page = max
                else:
                    page = str(int(page) - decrement)

            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page

            if unicode(self.page).isnumeric():
                persistent.pages_range = pages_range()

            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page

        def predict(self):
            _predict_file_page(self.page)

    def save_with_sound(slot):
        if FileTime(slot):
            renpy.play("ui/Menu Button Press.ogg", channel="sfx")
            FileAction(slot)()
        else:
            renpy.play("ui/Save.ogg", channel="sfx")
            FileSave(slot)()

screen save():
    tag menu
    if mm_var:
        add "fog_effect"
        add "magic_effect" at theme_ember
    use file_slots(_("保存"))

screen load():
    tag menu
    if mm_var:
        add "fog_effect"
        add "magic_effect" at theme_ember
    use file_slots(_("读取"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):

        fixed:
            order_reverse True

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.294
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        if FileTime(slot):
                            style "slot_button"
                        else:
                            style "slot_button2"
                        align (0.5, 0.5)
                        if renpy.current_screen().screen_name[0] == "load":
                            action FileAction(slot) activate_sound "ui/Menu Button Press.ogg"
                        else:
                            selected (str(persistent._file_page) + "-" + str(slot) == renpy.newest_slot("[0-9]"))
                            action Function(save_with_sound, slot)

                        has vbox
                        add FileScreenshot(slot) xalign 0.5 yalign 0.5

                        text FileTime(slot, format=_("{#file_time} %Y年%m月%d日 %H:%M"), empty=_("暂无数据")):
                            style "slot_time_text"

                        text FileSaveName(slot).replace("[","[[").replace("{","{{"):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)
                        at save_hover


            hbox:
                style_prefix "page"
                xalign 0.52
                yalign 0.9
                spacing 40

                if config.has_autosave:
                    frame:
                        style "empty"
                        xysize (40, 40)
                        textbutton _("{#auto_page}A") action FilePageLabel("auto") at shiftu_hover

                if config.has_quicksave:
                    frame:
                        style "empty"
                        xysize (40, 40)
                        textbutton _("{#quick_page}Q") action FilePageLabel("quick") at shiftu_hover

                frame:
                    style "empty"
                    xysize (40, 40)
                    textbutton _("«") action FilePageBack(decrement=10) at shiftu_hover
                frame:
                    style "empty"
                    xysize (40, 40)
                    textbutton _("<") action FilePageBack() at shiftu_hover

                for page in range( (persistent.pages_range * 10) + 1 , (persistent.pages_range * 10) + 11 ):
                    frame:
                        style "empty"
                        xysize (40, 40)
                        textbutton "[page]" action FilePageLabel(page) at shiftu_hover

                frame:
                    style "empty"
                    xysize (40, 40)
                    textbutton _(">") action FilePageForward() at shiftu_hover
                frame:
                    style "empty"
                    xysize (40, 40)
                    textbutton _("»") action FilePageForward(increment=10) at shiftu_hover
                

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    layout "subtitle"
    textalign 0.5

style page_button:
    properties gui.button_properties("page_button")
    xminimum 80

style page_button_text:
    properties gui.text_properties("page_button")
    size 32
    xalign 0.5
    
style slot_button:
    properties gui.button_properties("slot_button")
    activate_sound None
    xalign 0.5
    yalign 0.5
    hover_background Fixed(
        At(Transform(
            "gui/button/slot.png",
            matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(1.0),
            additive=2.0,
            blur=6.0,
            alpha=1.0,
            zoom=1.116,
        ), Position(xoffset=-26, yoffset=-18)),
        "gui/button/slot.png",
        fit_first=True
    )

style slot_button2:
    properties gui.button_properties("slot_button")
    activate_sound None
    xalign 0.5
    yalign 0.5
    idle_background "gui/button/slot.png"
    hover_background Fixed(
        At(Transform(
            "gui/button/slot.png",
            matrixcolor=TintMatrix(persistent.theme_color) * BrightnessMatrix(1.0),
            additive=2.0,
            blur=5.0,
            alpha=1.0
        ), Position(xoffset=-1.5, yoffset=-1.5)),
        "gui/button/slot.png",
        fit_first=True
    )
    background "gui/button/slot.png"

style slot_button_text:
    properties gui.text_properties("slot_button")
