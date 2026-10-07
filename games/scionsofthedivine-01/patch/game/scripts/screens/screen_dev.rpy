default dev_char_name_hovered = False
default dev_outfit_select_idx = 1
default dev_outfit_hovered = False
default dev_memory_select_idx = 0
default dev_memory_hovered = False
default dev_chapter_select = 1
default dev_chapter_hovered = False
default dev_part_select = 1
default dev_part_hovered = False
default dev_scene_select = 1
default dev_scene_hovered = False

init python:
    import re
    config.developer = False

    def get_chapters_parts_scenes():
        """
        Returns a dict mapping chapter numbers to dicts of part numbers to sorted list of scene numbers.
        Example: {1: {1: [1,2], 2: [1]}, 2: {1: [1]}}
        """
        chapters = {}
        for label in renpy.get_all_labels():
            m = re.match(r"c(\d+)p(\d+)s(\d+)$", label)
            if m:
                chap = int(m.group(1))
                part = int(m.group(2))
                scene = int(m.group(3))
                chapters.setdefault(chap, {}).setdefault(part, set()).add(scene)
        # Convert sets to sorted lists
        return {chap: {part: sorted(scenes) for part, scenes in parts.items()} for chap, parts in chapters.items()}

    def get_memory_description(memory_id):
        for r in memories:
            if r[0] == memory_id:
                return r[4][0] if r[4] else memory_id
        return memory_id

    config.overlay_screens.append("dev_menu_key_listener")

    #All
    def dev_lock_profiles():
        """Remove all unlocked profiles from persistent data."""
        persistent.profiles_unlocked = ["mc"]
        for char_id, profile in chara.items():
            if char_id == "mc":
                profile.profile = True
            elif char_id == "mcdad":
                profile.profile = True
            elif char_id == "mcmom":
                profile.profile = True
            else:
                profile.profile = False

    def dev_lock_outfits():
        """Remove all unlocked outfits from persistent data."""
        persistent.unlocked_outfits = {}
        for profile in chara.values():
            profile.unlocked_outfits = [0]
            profile.selected_outfit = 0

    def dev_lock_memories():
        """Remove all unlocked memories from persistent data."""
        persistent.unlocked_memories = {}
        for profile in chara.values():
            profile.memories_unlocked = set()

    def dev_lock_profiles_database():
        """lock all profiles, outfits, and memories."""
        dev_lock_profiles()
        dev_lock_outfits()
        dev_lock_memories()

    def dev_unlock_all_profiles():
        """Unlock all profiles and update persistent data."""
        persistent.profiles_unlocked = []
        for char_id, profile in chara.items():
            profile.profile = True
            if char_id not in persistent.profiles_unlocked:
                persistent.profiles_unlocked.append(char_id)

    def dev_unlock_all_outfits():
        """Unlock all outfits for all characters and update persistent data."""
        persistent.unlocked_outfits = {}
        for char_id, profile in chara.items():
            total = profile.get_total_outfits() if hasattr(profile, "get_total_outfits") else 1
            profile.unlocked_outfits = list(range(total))
            profile.selected_outfit = 0
            if total > 0:
                persistent.unlocked_outfits[char_id] = list(range(total))

    def dev_unlock_all_memories():
        """Unlock all memories for all characters and update persistent data."""
        persistent.unlocked_memories = {}
        all_memories = get_all_memories_by_character()
        for char_id, profile in chara.items():
            if char_id in all_memories:
                profile.memories_unlocked = set(all_memories[char_id])
                persistent.unlocked_memories[char_id] = list(all_memories[char_id])

    def dev_unlock_all_database():
        """Unlock all profiles, outfits, and memories."""
        dev_unlock_all_profiles()
        dev_unlock_all_outfits()
        dev_unlock_all_memories()

    #Specific
    def dev_lock_profile(char_id):
        """Lock the profile for a specific character."""
        if char_id in chara:
            chara[char_id].profile = False
            if char_id in persistent.profiles_unlocked:
                persistent.profiles_unlocked.remove(char_id)

    def dev_lock_outfits_for(char_id):
        """Lock all outfits for a specific character."""
        if char_id in chara:
            chara[char_id].unlocked_outfits = [0]
            chara[char_id].selected_outfit = 0
            if char_id in persistent.unlocked_outfits:
                persistent.unlocked_outfits[char_id] = [0]

    def dev_lock_memories_for(char_id):
        """Lock all memories for a specific character."""
        if char_id in chara:
            chara[char_id].memories_unlocked = set()
            if char_id in persistent.unlocked_memories:
                persistent.unlocked_memories[char_id] = []

    def dev_unlock_profile(char_id):
        """Unlock the profile for a specific character."""
        if char_id in chara:
            chara[char_id].profile = True
            if char_id not in persistent.profiles_unlocked:
                persistent.profiles_unlocked.append(char_id)

    def dev_unlock_outfits_for(char_id):
        """Unlock all outfits for a specific character."""
        if char_id in chara:
            total = chara[char_id].get_total_outfits()
            chara[char_id].unlocked_outfits = list(range(total))
            chara[char_id].selected_outfit = 0
            persistent.unlocked_outfits[char_id] = list(range(total))

    def dev_unlock_memories_for(char_id):
        """Unlock all memories for a specific character."""
        all_memories = get_all_memories_by_character()
        if char_id in chara and char_id in all_memories:
            chara[char_id].memories_unlocked = set(all_memories[char_id])
            persistent.unlocked_memories[char_id] = list(all_memories[char_id])

    def dev_unlock_outfit_for(char_id, outfit_idx):
        """Unlock a specific outfit for a specific character."""
        if char_id in chara:
            if outfit_idx not in chara[char_id].unlocked_outfits:
                chara[char_id].unlocked_outfits.append(outfit_idx)
                persistent.unlocked_outfits.setdefault(char_id, []).append(outfit_idx)

    def dev_lock_outfit_for(char_id, outfit_idx):
        """Lock a specific outfit for a specific character."""
        if char_id in chara:
            if outfit_idx in chara[char_id].unlocked_outfits:
                chara[char_id].unlocked_outfits.remove(outfit_idx)
            if char_id in persistent.unlocked_outfits and outfit_idx in persistent.unlocked_outfits[char_id]:
                persistent.unlocked_outfits[char_id].remove(outfit_idx)

    def dev_unlock_memory_for(char_id, memory_id):
        """Unlock a specific memory for a specific character."""
        if char_id in chara:
            chara[char_id].memories_unlocked.add(memory_id)
            persistent.unlocked_memories.setdefault(char_id, []).append(memory_id)

    def dev_lock_memory_for(char_id, memory_id):
        """Lock a specific memory for a specific character."""
        if char_id in chara and memory_id in chara[char_id].memories_unlocked:
            chara[char_id].memories_unlocked.remove(memory_id)
        if char_id in persistent.unlocked_memories and memory_id in persistent.unlocked_memories[char_id]:
            persistent.unlocked_memories[char_id].remove(memory_id)

    def dev_unlock_all_for(char_id):
        """Unlock profile, outfits, and memories for a specific character."""
        dev_unlock_profile(char_id)
        dev_unlock_outfits_for(char_id)
        dev_unlock_memories_for(char_id)

    def dev_lock_all_for(char_id):
        """Lock profile, outfits, and memories for a specific character."""
        dev_lock_profile(char_id)
        dev_lock_outfits_for(char_id)
        dev_lock_memories_for(char_id)


screen dev_menu_key_listener():
    if persistent.dev_menu:
        key "`" action Show("dev_menu")

screen dev_menu():
    modal True
    $ chapters_parts_scenes = get_chapters_parts_scenes()
    $ available_chapters = sorted(chapters_parts_scenes.keys())
    $ dev_chapter_select = dev_chapter_select if dev_chapter_select in available_chapters else (available_chapters[0] if available_chapters else 1)
    $ available_parts = sorted(chapters_parts_scenes.get(dev_chapter_select, {}).keys())
    $ dev_part_select = dev_part_select if dev_part_select in available_parts else (available_parts[0] if available_parts else 1)
    $ available_scenes = chapters_parts_scenes.get(dev_chapter_select, {}).get(dev_part_select, [1])
    $ dev_scene_select = dev_scene_select if 'dev_scene_select' in locals() and dev_scene_select in available_scenes else (available_scenes[0] if available_scenes else 1)
    if dev_outfit_select_idx == 0:
        $ dev_outfit_select_idx = 1
    if dev_char_name_hovered:
        key ["rollback"] action SetScreenVariable("dev_char_select_idx", (dev_char_select_idx - 1) % len(dev_char_list))
        key ["rollforward"] action SetScreenVariable("dev_char_select_idx", (dev_char_select_idx + 1) % len(dev_char_list))
    if dev_chapter_hovered:
        key ["rollback"] action SetScreenVariable("dev_chapter_select", available_chapters[(available_chapters.index(dev_chapter_select) - 1) % len(available_chapters)])
        key ["rollforward"] action SetScreenVariable("dev_chapter_select", available_chapters[(available_chapters.index(dev_chapter_select) + 1) % len(available_chapters)])
    if dev_part_hovered:
        key ["rollback"] action SetScreenVariable("dev_part_select", available_parts[(available_parts.index(dev_part_select) - 1) % len(available_parts)])
        key ["rollforward"] action SetScreenVariable("dev_part_select", available_parts[(available_parts.index(dev_part_select) + 1) % len(available_parts)])
    if dev_scene_hovered:
        key ["rollback"] action SetScreenVariable("dev_scene_select", available_scenes[(available_scenes.index(dev_scene_select) - 1) % len(available_scenes)])
        key ["rollforward"] action SetScreenVariable("dev_scene_select", available_scenes[(available_scenes.index(dev_scene_select) + 1) % len(available_scenes)])
    if dev_outfit_hovered:
        key ["rollback"] action SetScreenVariable("dev_outfit_select_idx", max(1, dev_outfit_select_idx - 1))
        key ["rollforward"] action SetScreenVariable("dev_outfit_select_idx", min(total_outfits - 1, dev_outfit_select_idx + 1))
    if dev_memory_hovered:
        key ["rollback"] action SetScreenVariable("dev_memory_select_idx", (dev_memory_select_idx - 1) % total_memories)
        key ["rollforward"] action SetScreenVariable("dev_memory_select_idx", (dev_memory_select_idx + 1) % total_memories)
    frame:
        background "#00000088"
        style_prefix "dev"
        vbox:
            label "开发菜单" text_size 24
            hbox:
                if config.developer:
                    vbox:
                        xsize 200
                        spacing -10
                        label "章节选择" text_size 16 xpos 5
                        hbox:
                            textbutton "<" action SetScreenVariable("dev_chapter_select", available_chapters[(available_chapters.index(dev_chapter_select) - 1) % len(available_chapters)]) yalign 0.5
                            textbutton "第 [dev_chapter_select] 章":
                                text_size 16
                                yalign 0.5
                                hovered SetScreenVariable("dev_chapter_hovered", True)
                                unhovered SetScreenVariable("dev_chapter_hovered", False)
                                action NullAction()
                            textbutton ">" action SetScreenVariable("dev_chapter_select", available_chapters[(available_chapters.index(dev_chapter_select) + 1) % len(available_chapters)]) yalign 0.5
                        hbox:
                            textbutton "<" action SetScreenVariable("dev_part_select", available_parts[(available_parts.index(dev_part_select) - 1) % len(available_parts)]) yalign 0.5
                            textbutton "第 [dev_part_select] 部分":
                                text_size 16
                                yalign 0.5
                                hovered SetScreenVariable("dev_part_hovered", True)
                                unhovered SetScreenVariable("dev_part_hovered", False)
                                action NullAction()
                            textbutton ">" action SetScreenVariable("dev_part_select", available_parts[(available_parts.index(dev_part_select) + 1) % len(available_parts)]) yalign 0.5
                        hbox:
                            textbutton "<" action SetScreenVariable("dev_scene_select", available_scenes[(available_scenes.index(dev_scene_select) - 1) % len(available_scenes)]) yalign 0.5
                            textbutton "场景 [dev_scene_select]":
                                text_size 16
                                yalign 0.5
                                hovered SetScreenVariable("dev_scene_hovered", True)
                                unhovered SetScreenVariable("dev_scene_hovered", False)
                                action NullAction()
                            textbutton ">" action SetScreenVariable("dev_scene_select", available_scenes[(available_scenes.index(dev_scene_select) + 1) % len(available_scenes)]) yalign 0.5
                        textbutton "Jump" action [Stop("bgm"), Stop("sound"), Stop("bgs"), Hide('dev_menu'), Jump("c%dp%ds%d" % (dev_chapter_select, dev_part_select, dev_scene_select))] yalign 0.5
                    null width 25
                vbox:
                    xsize 250
                    spacing -10
                    label "Variables" text_size 16 xpos -3
                    hbox:
                        text "莱拉的晚餐："size 14 outlines [(2, "#000000", 0, 0)] yalign 0.5
                        textbutton "[layldinner]" action SetVariable("layldinner", not layldinner) yalign 0.5
                    hbox:
                        text "阿斯塔拉与雷恩偷听："size 14 outlines [(2, "#000000", 0, 0)] yalign 0.5
                        textbutton "[asta_rayn_eavesdrop]" action SetVariable("asta_rayn_eavesdrop", not asta_rayn_eavesdrop) yalign 0.5
                    hbox:
                        text "与索尔裸泳："size 14 outlines [(2, "#000000", 0, 0)] yalign 0.5
                        textbutton "[soul_sd]" action SetVariable("soul_sd", not soul_sd) yalign 0.5
                null width 25
                vbox:
                    xsize 500
                    spacing -10
                    label "Profiles" text_size 16
                    default dev_char_list = ["All"] + [c for c in chara.keys()]
                    default dev_char_select_idx = 0
                    $ dev_char_select = dev_char_list[dev_char_select_idx]
                    null height 25
                    hbox:
                        frame:
                            style "empty"
                            xysize (20, 20)
                            textbutton "<" action SetScreenVariable("dev_char_select_idx", (dev_char_select_idx - 1) % len(dev_char_list)) yalign 0.5
                        frame:
                            style "empty"
                            xysize (150, 20)
                            if dev_char_select != "All":
                                $ char_color = chara[dev_char_select].color if hasattr(chara[dev_char_select], "color") else "#FFFFFF"
                                textbutton "[chara[dev_char_select].name]":
                                    text_color char_color
                                    text_size 16
                                    xalign 0.5
                                    yalign 0.5
                                    hovered SetScreenVariable("dev_char_name_hovered", True)
                                    unhovered SetScreenVariable("dev_char_name_hovered", False)
                                    action NullAction()
                            else:
                                textbutton "All":
                                    text_size 16
                                    xalign 0.5
                                    yalign 0.5
                                    hovered SetScreenVariable("dev_char_name_hovered", True)
                                    unhovered SetScreenVariable("dev_char_name_hovered", False)
                                    action NullAction()
                        frame:
                            style "empty"
                            xysize (20, 20)
                            textbutton ">" action SetScreenVariable("dev_char_select_idx", (dev_char_select_idx + 1) % len(dev_char_list)) yalign 0.5
                    null height 25
                    if dev_char_select == "All":
                        hbox:
                            textbutton "Unlock" yalign 0.5 action Function(dev_unlock_all_profiles)
                            text "/"
                            textbutton "Lock" yalign 0.5 action Function(dev_lock_profiles)
                            text "全部档案"
                        hbox:
                            textbutton "Unlock" yalign 0.5 action Function(dev_unlock_all_outfits)
                            text "/"
                            textbutton "Lock" yalign 0.5 action Function(dev_lock_outfits)
                            text "全部服装"
                        hbox:
                            textbutton "Unlock" yalign 0.5 action Function(dev_unlock_all_memories)
                            text "/"
                            textbutton "Lock" yalign 0.5 action Function(dev_lock_memories)
                            text "全部回忆"
                        hbox:
                            textbutton "Unlock" yalign 0.5 action Function(dev_unlock_all_database)
                            text "/"
                            textbutton "Lock" yalign 0.5 action Function(dev_lock_profiles_database)
                            text "Everything"
                    elif dev_char_select == "mc":
                        if "Outfits" in chara[dev_char_select].tags:
                            hbox:
                                textbutton "Unlock" yalign 0.5 action Function(dev_unlock_outfits_for, dev_char_select)
                                text "/"
                                textbutton "Lock" yalign 0.5 action Function(dev_lock_outfits_for, dev_char_select)
                                text "全部服装"
                        if "Outfits" in chara[dev_char_select].tags and hasattr(chara[dev_char_select], "get_total_outfits"):
                            $ total_outfits = chara[dev_char_select].get_total_outfits()
                            if total_outfits > 0:
                                hbox:
                                    textbutton "Unlock" action Function(dev_unlock_outfit_for, dev_char_select, dev_outfit_select_idx) yalign 0.5
                                    text "/"
                                    textbutton "Lock" action Function(dev_lock_outfit_for, dev_char_select, dev_outfit_select_idx) yalign 0.5
                                    text "Outfit"
                                    textbutton "<" action SetScreenVariable("dev_outfit_select_idx", max(1, dev_outfit_select_idx - 1)) yalign 0.5
                                    textbutton "[dev_outfit_select_idx]":
                                        text_size 14
                                        yalign 0.5
                                        hovered SetScreenVariable("dev_outfit_hovered", True)
                                        unhovered SetScreenVariable("dev_outfit_hovered", False)
                                        action NullAction()
                                    textbutton ">" action SetScreenVariable("dev_outfit_select_idx", min(total_outfits - 1, dev_outfit_select_idx + 1)) yalign 0.5
                        null height 20
                        hbox:
                            xpos 7
                            text "善恶值："
                            fixed:
                                xsize 200
                                ysize 15
                                yalign 0.6
                                bar:
                                    xsize 100
                                    ysize 15
                                    yalign 0.6
                                    right_bar (Solid(
                                        "#aa2626" if chara[dev_char_select].karma <= -40 else
                                        "#b3b3b3" if -40 < chara[dev_char_select].karma < 0 else
                                        "#00000000"
                                    ))
                                    left_bar Solid("#333")
                                    value FieldValue(chara[dev_char_select], "karma", min=-100, max=0)
                                    xalign 0.0
                                bar:
                                    xsize 100
                                    ysize 15
                                    yalign 0.6
                                    left_bar (Solid(
                                        "#e2ff92" if chara[dev_char_select].karma >= 40 else
                                        "#b3b3b3" if 0 < chara[dev_char_select].karma < 40 else
                                        "#00000000"
                                    ))
                                    right_bar Solid("#333")
                                    value FieldValue(chara[dev_char_select], "karma", min=0, max=100)
                                    xalign 1.0
                                bar:
                                    xsize 200
                                    ysize 15
                                    yalign 0.6
                                    left_bar Solid("#00000000")
                                    right_bar Solid("#00000000")
                                    thumb Solid("#fff", xsize=2, ysize=15)
                                    value FieldValue(chara[dev_char_select], "karma", min=-100, max=100)
                                    xalign 0.5
                            text " [chara[dev_char_select].karma]"
                    else:
                        hbox:
                            textbutton "Unlock" yalign 0.5 action Function(dev_unlock_profile, dev_char_select)
                            text "/"
                            textbutton "Lock" yalign 0.5 action Function(dev_lock_profile, dev_char_select)
                            text "Profile"
                        if "Outfits" in chara[dev_char_select].tags:
                            hbox:
                                textbutton "Unlock" yalign 0.5 action Function(dev_unlock_outfits_for, dev_char_select)
                                text "/"
                                textbutton "Lock" yalign 0.5 action Function(dev_lock_outfits_for, dev_char_select)
                                text "全部服装"
                        if "Outfits" in chara[dev_char_select].tags and hasattr(chara[dev_char_select], "get_total_outfits"):
                            $ total_outfits = chara[dev_char_select].get_total_outfits()
                            if total_outfits > 0:
                                hbox:
                                    textbutton "Unlock" action Function(dev_unlock_outfit_for, dev_char_select, dev_outfit_select_idx) yalign 0.5
                                    text "/"
                                    textbutton "Lock" action Function(dev_lock_outfit_for, dev_char_select, dev_outfit_select_idx) yalign 0.5
                                    text "Outfit"
                                    textbutton "<" action SetScreenVariable("dev_outfit_select_idx", max(1, dev_outfit_select_idx - 1)) yalign 0.5
                                    textbutton "[dev_outfit_select_idx]":
                                        text_size 14
                                        yalign 0.5
                                        hovered SetScreenVariable("dev_outfit_hovered", True)
                                        unhovered SetScreenVariable("dev_outfit_hovered", False)
                                        action NullAction()
                                    textbutton ">" action SetScreenVariable("dev_outfit_select_idx", min(total_outfits - 1, dev_outfit_select_idx + 1)) yalign 0.5
                        if "Memories" in chara[dev_char_select].tags:
                            hbox:
                                textbutton "Unlock" yalign 0.5 action Function(dev_unlock_memories_for, dev_char_select)
                                text "/"
                                textbutton "Lock" yalign 0.5 action Function(dev_lock_memories_for, dev_char_select)
                                text "全部回忆"
                        if "Memories" in chara[dev_char_select].tags and hasattr(chara[dev_char_select], "memories_unlocked"):
                            $ all_memories = get_all_memories_by_character()
                            $ mem_list = list(all_memories.get(dev_char_select, []))
                            $ total_memories = len(mem_list)
                            if total_memories > 0:
                                hbox:
                                    textbutton "Unlock" action Function(dev_unlock_memory_for, dev_char_select, mem_list[dev_memory_select_idx]) yalign 0.5
                                    text "/"
                                    textbutton "Lock" action Function(dev_lock_memory_for, dev_char_select, mem_list[dev_memory_select_idx]) yalign 0.5
                                    text "Memory"
                                    textbutton "<" action SetScreenVariable("dev_memory_select_idx", (dev_memory_select_idx - 1) % total_memories) yalign 0.5
                                    textbutton "[get_memory_description(mem_list[dev_memory_select_idx])]":
                                        text_size 14
                                        yalign 0.5
                                        hovered SetScreenVariable("dev_memory_hovered", True)
                                        unhovered SetScreenVariable("dev_memory_hovered", False)
                                        action NullAction()
                                    textbutton ">" action SetScreenVariable("dev_memory_select_idx", (dev_memory_select_idx + 1) % total_memories) yalign 0.5
                        if "Outfits" and "Memories" in chara[dev_char_select].tags:
                            hbox:
                                textbutton "Unlock" yalign 0.5 action Function(dev_unlock_all_for, dev_char_select)
                                text "/"
                                textbutton "Lock" yalign 0.5 action Function(dev_lock_all_for, dev_char_select)
                                text "Everything"
                        if "Romanceable" in chara[dev_char_select].tags:
                            null height 20
                            hbox:
                                xpos 7
                                text "Affection: "
                                bar:
                                    xsize 100
                                    ysize 15
                                    yalign 0.6
                                    left_bar Solid("#ff8bdd")
                                    right_bar Solid("#333")
                                    thumb Solid("#fff", xsize=2, ysize=15)
                                    value FieldValue(chara[dev_char_select], "affection", min=0, max=100)
                                text " [chara[dev_char_select].affection]"
            vbox:
                xsize 200
                spacing -10
                label "Utilities" text_size 16
                textbutton "紧急更新" action Function(initialize_characters)
                text "！！！这会用新数据重新更新旧存档。大多数情况下你不需要使用它。！！！" color "#d3b050" italic True

    key "`" action Hide("dev_menu")
    key "game_menu" action Hide("dev_menu")

style dev_text:
    size 14
    yalign 0.5
    outlines [(2, "#000000", 0, 0)]

style dev_button is gui_button:
    size 14

style dev_button_text is gui_button_text:
    size 14