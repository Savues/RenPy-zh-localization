init -999 python:
    ''' 
    版权所有 (C) 2021-2022 由 3 Pood Productions 制作

    特此免费授予任何获得本软件
    及其相关文档文件（"本软件"）副本的人许可，
    可在不受限制的情况下
    使用、复制、修改、合并、发布、分发、再许可和/或出售
    本软件的副本，并允许获得本软件的人
    从事上述操作，但须遵守以下条件：

    上述版权声明及本许可声明
    应包含在本软件的所有副本或实质性部分中。

    本软件按"现状"提供，不附带任何明示或默示的担保，
    包括但不限于对适销性及特定用途适用性的默示保证。
    在任何情况下，作者或版权持有人
    均不对任何索赔、损害或其他
    责任负责，无论其因合同、侵权
    还是其他原因引起，也不论是否
    与本软件的使用或其他行为有关。
'''
    renpy.add_python_directory('code/core/python/')

    import json
    import zipfile

    # Class decorator, marks the class as unpickleable
    def unpickleable(cls):
        def getstate(self):
            raise Exception("This class is not meant to be saved, use define only and reference from the id")
        cls.__getstate__ = getstate
        return cls
    
    
    def merge_dicts(first, *dicts):
        ret = first.copy()
        for d in dicts:
            ret.update(d)
        return ret


    def saveWithNewName(slot, name):
        page = persistent._file_page
        slotname = str(page) + '-' + str(slot)
        log = renpy.loadsave.location.load(slotname)
        extra_info = name
        screenshot = renpy.slot_screenshot(slotname)
        with zipfile.ZipFile(screenshot.zipfilename, 'r') as zf:
            screenshot = zf.read(screenshot.filename)

        old_json = renpy.slot_json(slotname)
        old_json['_save_name'] = name
        json_str = json.dumps(old_json)

        record = renpy.loadsave.SaveRecord(screenshot, extra_info, json_str, log)
        renpy.loadsave.location.save(slotname, record)
    