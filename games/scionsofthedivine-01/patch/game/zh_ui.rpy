# -*- coding: utf-8 -*-
# Added by the Chinese localization.
#
# Internal data (profile tags, Ren'Py confirm prompts) stays in English because
# the engine compares against it. These helpers translate it at display time only.

init -998 python:

    def filter_label(value):
        """Show a readable label for an internal profile-filter tag."""
        return {
            "Women": "女性",
            "Men": "男性",
            "Romanceable": "可攻略",
            "Mages": "法师",
        }.get(value, value)

    def memory_tag_zh(value):
        """Show a readable label for an internal gallery-filter tag."""
        return {
            "Blowjob": "口交",
            "Fingering": "手交",
            "Squirting": "潮吹",
        }.get(value, value)

    def confirm_zh(message):
        """Ren'Py confirm prompts arrive as English; map them to Chinese."""
        return {
            "Are you sure you want to quit?":
                "确定要退出吗？",
            "Are you sure you want to return to the main menu?\nThis will lose unsaved progress.":
                "确定要返回主菜单吗？\n这将丢失未保存的进度。",
            "Are you sure you want to delete this save?":
                "确定要删除这个存档吗？",
            "Are you sure you want to overwrite your save?":
                "确定要覆盖存档吗？",
            "Loading will lose unsaved progress.\nAre you sure you want to do this?":
                "读取将丢失未保存的进度。\n确定要继续吗？",
            "Are you sure you want to continue where you left off?":
                "确定要从上次进度继续吗？",
            "Are you sure you want to end the replay?":
                "确定要结束回放吗？",
            "Are you sure you want to begin skipping?":
                "确定要开始快进吗？",
            "Are you sure you want to skip to the next choice?":
                "确定要快进到下一个选项吗？",
            "Are you sure you want to skip unseen dialogue to the next choice?":
                "确定要跳过没看过的对话，直到下一个选项吗？",
        }.get(message, message)
