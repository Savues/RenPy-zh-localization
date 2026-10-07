init offset = 99

default persistent.save_naming = True


init -999 python:

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

    class FilePage(Action, DictEquality):
        
        #:doc: file_action

        #把文件页设为 `page`,取值可以是 "auto"、"quick"
        #或者一个整数。
        

        def __init__(self, page):
            self.page = str(page)

            if page == "auto":
                self.alt = _("文件页 自动")
            elif page == "quick":
                self.alt = _("文件页 快速")
            else:
                self.alt = _("文件页 [text]")

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


    class FilePageNext(Action, DictEquality):
        # """
        # :doc: file_action

        # 跳到下一个文件页。

        # `max`(最大页码)
        #     若已设置,这里应为整数,表示
        #     可跳转的最大文件页编号。

        # `wrap`(循环翻页)
        #     若为真,则在最后一页时也可以回到
        #     第一页(需已设置 `max`)。

        # `auto`(自动存档页)
        #     若为真且已启用循环翻页,可让玩家跳到
        #     自动存档所在的那一页。

        # `quick`(快速存档页)
        #     若为真且已启用循环翻页,可让玩家跳到
        #     自动存档所在的那一页。
        # """

        alt = _("下一页。")

        def __init__(self, max=None, wrap=False, auto=True, quick=True, increment=1):

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


    class FilePagePrevious(Action, DictEquality):
        # """
        #  :doc: file_action

        #  跳到上一个文件页(如果还有上一页)。

        # `max`(最大页码)
        #     若已设置,这里应为整数,表示
        #     可跳转的最大文件页编号。必须设置该项才能
        #     启用循环翻页。

        # `wrap`(循环翻页)
        #     若为真,则在第一页时也可以跳到最后一页(需已设置 max)。

        # `auto`(自动存档页)
        #     若为真,可让玩家跳到
        #     自动存档所在的那一页。

        # `quick`(快速存档页)
        #     若为真,可让玩家跳到
        #     自动存档所在的那一页。

        #  """

        alt = _("上一页。")

        def __init__(self, max=None, wrap=False, auto=True, quick=True, decrement=1):

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



screen screen_save_name(slot):
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            spacing 25
            xsize 650

            if FileLoadable(slot):
                label _("存档名称({color=#f00}覆盖{/color})：") style "confirm_prompt"
            else:
                label _("存档名称({color=#0f0}新建{/color})：") style "confirm_prompt"

            input:
                value VariableInputValue('save_name')
                length 30
                xalign 0.5
                exclude "\\[{"

            hbox:
                xfill True
                textbutton _("是") action FileAction(slot, confirm=False), Hide("screen_save_name") xalign 0.5
                textbutton _("否") action Hide("screen_save_name") xalign 0.5

    ## 右键或按 ESC 视为选择「否」。
    key "game_menu" action Hide("screen_save_name")

    ## 回车键视为选择「是」。
    key "K_RETURN" action FileAction(slot, confirm=False), Hide("screen_save_name")
    key "K_KP_ENTER" action FileAction(slot, confirm=False), Hide("screen_save_name")
