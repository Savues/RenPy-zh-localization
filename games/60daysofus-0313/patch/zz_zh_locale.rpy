# 60 Days Of Us 3.1.3 -- 简体中文补丁 / Simplified Chinese patch
#
# 游戏的英文脚本全部封在 archive.rpa 里，而它自带的 tl/Chinese 也在**归档内部**。
# 只把中文文件丢进 game/tl/Chinese/ 是不够的：Ren'Py 会同时从磁盘和归档收集翻译，
# 于是每个 translate Chinese strings: 的 old/new 都被注册两遍，
# TranslationStringRegistry.add() 在启动时抛
#     Exception: A translation for "..." already exists.
# 菜单都进不去。所以安装器先做 RPA-3 索引手术把归档里那 24 条 tl/Chinese/* 摘掉
# （tools/rpa_drop_prefix.py，2.5 GB 素材一字节不动），再放这 12 个文件。
#
# 这个 shim 只做一件事：让中文成为默认语言。

init python:

    config.language = "Chinese"


# 字体不动。游戏自己的 th_font_map["Chinese"] 指向思源宋体 CJK，归档和 game/Fonts/
# 里都有，本补丁不重新分发任何字体文件。
