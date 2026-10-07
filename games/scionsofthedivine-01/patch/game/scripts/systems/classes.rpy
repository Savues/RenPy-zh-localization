init offset = -3

init -2 python:

    STAT_COLORS = {
        "affection": "#ff8bdd",
        "karma": "#ffffff",
        # add more if needed
    }

    CHARACTER_DATA = {
        "mc": {
            "color": "#d386ff",
            "bio_info": {"name": "[mc_name]", "age": "23", "height": "170 cm", "weight": "61 kg"},
            "bios": [
                ("1", "我的人生一直很坎坷。父亲总是长时间离家，到最后干脆一去不回。我的一切从此每况愈下。十九岁那年，我决定独自生活，指望能走出那些悲剧与失去。"),
            ],
            "tags": ["Men", "Outfits", "Karma", "Scions"],
        },
        "mcdad": {
            "color": "#00a72c",
            "bio_info": {"name": "爸爸", "age": "44", "height": "173 cm", "weight": "64 kg"},
            "bios": [
                ("1", "我那个疯狂的父亲。他几乎把大半辈子都投入在研究神裔与神明的失踪事件上。作为考古学家，他能接触许多可能与神明相关的远古神庙与遗迹。也正因如此，他总是外出考察，我几乎是在他缺席的状态下长大的。"),
            ],
            "tags": ["Men", "Outfits"],
        },
        "mcmom": {
            "color": "#aa2fcf",
            "bio_info": {"name": "妈妈", "age": "42", "height": "160 cm", "weight": "54 kg"},
            "bios": [
                ("1", "我慈爱的母亲。她是父亲的好妻子，更是个好家长。父亲总是奔赴一个又一个挖掘现场，所以基本上是她独自把我带大的。父亲去世后她变了很多，但依然是个好家长，把我拉扯得很好。"),
            ],
            "tags": ["Women", "Outfits"],
        },
        "sara": {
            "color": "#a3c4df",
            "bio_info": {"name": "莎拉", "age": "本该 22", "height": "157 cm", "weight": "51 kg"},
            "bios": [
                ("1", "我最初的挚爱……她是世界上最体贴的人，教会了我认真去在意一件事或一个人究竟意味着什么。她在人生的许多方面都很挣扎，尽管有真正爱她、想帮她的人，她最后还是选择结束自己的生命……"),
            ],
            "tags": ["Women", "Outfits"],
        },
        "layl": {
            "color": "#d8cf51",
            "bio_info": {"name": "莱拉", "age": "21", "height": "168 cm", "weight": "54 kg"},
            "bios": [
                ("1", "任何人都求之不得的好朋友。从我们还是小孩起，她就一直在我身边，一路支撑我走到现在。她的头脑让人惊叹：只要你能想出什么东西，她通常都能找到办法把它变成现实。"),
            ],
            "tags": ["Women", "Outfits", "Romanceable", "Memories"],
        },
        "layldad": {
            "color": "#b46600",
            "bio_info": {"name": "韦克斯特罗斯先生", "age": "47", "height": "178 cm", "weight": "71 kg"},
            "bios": [
                ("1", "莱拉的父亲，一位专做市场调控与公司融资的知名商人。他心地非常善良，在我父亲去世之后，他对我而言几乎成了父亲的角色。"),
            ],
            "tags": ["Men", "Outfits"],
        },
        "laylmom": {
            "color": "#6a8343",
            "bio_info": {"name": "韦克斯特罗斯太太", "age": "43", "height": "168 cm", "weight": "61 kg"},
            "bios": [
                ("1", "莱拉的母亲。她是个温柔的女人，厨艺无人能及。我小时候她常常帮忙照看我，好让我母亲在父亲不在之后能拼命工作维持生计。"),
            ],
            "tags": ["Women", "Outfits"],
        },
        "chri": {
            "color": "#39c979",
            "bio_info": {"name": "克里斯汀", "age": "24", "height": "155 cm", "weight": "49 kg"},
            "bios": [
                ("1", "在我昏迷期间照顾我的医生。她性格体贴，而且似乎对帮助别人充满热情——不只是医学上的帮助。"),
            ],
            "tags": ["Women", "Outfits", "Romanceable", "Memories"],
        },
        "vero": {
            "color": "#665c3c",
            "bio_info": {"name": "维罗妮卡", "age": "20", "height": "163 cm", "weight": "66 kg"},
            "bios": [
                ("1", "守望者军团的一员。她给人的印象强硬又刻薄，但她的目光里带着温柔，让我知道她并非一直如此。"),
            ],
            "tags": ["Women", "Outfits", "Romanceable", "Memories"],
        },
        "kate": {
            "color": "#75ccdb",
            "bio_info": {"name": "凯特", "age": "20", "height": "163 cm", "weight": "59 kg"},
            "bios": [
                ("1", "和维罗妮卡关系很好的守望者。她看起来甜美又无忧无虑，但说话完全不过脑子。"),
            ],
            "tags": ["Women", "Outfits", "Memories"],
        },
        "asta": {
            "color": "#468dcf",
            "bio_info": {"name": "阿斯塔拉", "age": "23", "height": "160 cm", "weight": "58 kg"},
            "bios": [
                ("1", "一个神秘的女人，似乎比我见过的所有人都更自信。她身上有种漫不经心的气质，会让人放下戒心，但相信我，她不是能随便招惹的人。"),
            ],
            "tags": ["Women", "Outfits", "Romanceable", "Memories", "Scions"],
        },
        "sila": {
            "color": "#a36e4f",
            "bio_info": {"name": "塞拉斯", "age": "32", "height": "183 cm", "weight": "75 kg"},
            "bios": [
                ("1", "三度夺冠的BFC（残暴格斗锦标赛）冠军。过去他还是我的格斗教练时我很了解他，但后来生活把我拉向太多方向，我们就断了联系。"),
            ],
            "tags": ["Men", "Outfits", "Mages"],
        },
        "rayn": {
            "color": "#e770c3",
            "bio_info": {"name": "雷恩", "age": "19", "height": "157 cm", "weight": "59 kg"},
            "bios": [
                ("1", "她是塞拉斯的学生之一，就像以前的我。既然塞拉斯在训练她，她肯定很强，我应该小心些，别惹她不高兴。"),
            ],
            "tags": ["Women", "Outfits", "Memories"],
        },
        "mela": {
            "color": "#cc3c3c",
            "bio_info": {"name": "梅拉妮", "age": "18", "height": "165 cm", "weight": "52 kg"},
            "bios": [
                ("1", "她是个矜持谨慎的女人，看起来出身贵族。她在使用神裔之力方面极有天赋，也正因为这点让人有点害怕。"),
                ("2", "国王的女儿，也是王族唯一的继承人。她一直被藏在公众视野之外，所以几乎没人知道她的存在。"),
            ],
            "tags": ["Women", "Outfits", "Romanceable", "Memories", "Scions"],
        },
        "king": {
            "color": "#008b0c",
            "bio_info": {"name": "纳索斯国王", "age": "39", "height": "175 cm", "weight": "66 kg"},
            "bios": [
                ("1", "（暂无内容）"),
            ],
            "tags": ["Men", "Outfits"],
        },
        "queen": {
            "color": "#4db0bd",
            "bio_info": {"name": "安妮丝女王", "age": "35", "height": "168 cm", "weight": "52 kg"},
            "bios": [
                ("1", "（暂无内容）"),
            ],
            "tags": ["Women", "Outfits"],
        },
        "barth": {
            "color": "#919191",
            "bio_info": {"name": "巴塞洛缪", "age": "57", "height": "170 cm", "weight": "64 kg"},
            "bios": [
                ("1", "他看起来像是管家，同时也是个有荣誉感的人。以他的年纪来说，他的力气大得反常。"),
            ],
            "tags": ["Men"],
        },
        "soul": {
            "color": "#9c3bb9",
            "bio_info": {"name": "索尔", "age": "22", "height": "155 cm", "weight": "58 kg"},
            "bios": [
                ("1", "在「最后一滴」工作的甜美女酒保。她很擅长倾听别人的烦恼并给出可靠的建议。她也非常直率，想说什么就说什么，不怕被评判。"),
            ],
            "tags": ["Women", "Outfits", "Romanceable", "Memories", "Mages"],
        },
        "leon": {
            "color": "#ff7300",
            "bio_info": {"name": "里昂", "age": "30", "height": "175 cm", "weight": "63 kg"},
            "bios": [
                ("1", "火之神裔，一个傲慢的混蛋。他一直在猎杀其他神裔，妄图征服世界。看来连世间的人渣都能被选中获得神力。"),
            ],
            "tags": ["Men", "Scions"],
        },
        "eddi": {
            "color": "#297cc9",
            "bio_info": {"name": "埃德温", "age": "17", "height": "163 cm", "weight": "59 kg"},
            "bios": [
                ("1", "一个获得神力的少年。他看起来很封闭，但很快就敞开心扉，大概是因为孤独。"),
            ],
            "tags": ["Men", "Outfits"],
        },
        "ash": {
            "color": "#660000",
            "bio_info": {"name": "阿什琳", "age": "573", "height": "165 cm", "weight": "55 kg"},
            "bios": [
                ("1", "（暂无内容）"),
            ],
            "tags": ["Women", "Outfits", "Memories"],
        },
        "rile": {
            "color": "#bdb762",
            "bio_info": {"name": "莱利", "age": "358", "height": "160 cm", "weight": "63 kg"},
            "bios": [
                ("1", "（暂无内容）"),
            ],
            "tags": ["Women", "Outfits", "Memories"],
        },
    }

    def oxford_comma(items):
        """Applies the Oxford Comma structure."""
        if not items:
            return ""
        if len(items) == 1:
            return items[0]
        if len(items) == 2:
            return " and ".join(items)
        return ", ".join(items[:-1]) + ", and " + items[-1]

    def possessive(name):
        """Check for proper comma placement in possessives."""
        return name + "'" if name.lower().endswith("s") else name + "'s"

    class CharacterProfile:
        def __init__(self, color, tags=None, stats=None):
            """Initialize a customizable character instance."""
            self.color = color
            self.profile = False
            self.tags = []
            self.unlocked_bios = set()
            self.stats = stats if stats is not None else {
                "affection": 10,
                "karma": 0
            }
            self.unlocked_outfits = [0]
            self.selected_outfit = 0
            self._total_outfits_known = 0
            self.memories_unlocked = set()

        @property
        def name(self):
            """Always return the name from CHARACTER_DATA, so changes are reflected in old saves."""
            char_id = self.get_id() if hasattr(self, "get_id") else None
            if char_id == "mc":
                return mc_name
            if char_id and char_id in CHARACTER_DATA:
                return CHARACTER_DATA[char_id]["bio_info"].get("name", char_id.capitalize())
            return "未知"

        @property
        def affection(self):
            return self.stats.get("affection", 0)

        @affection.setter
        def affection(self, value):
            self.stats["affection"] = int(max(0, min(value, 100)))

        @property
        def karma(self):
            return self.stats.get("karma", 0)

        @karma.setter
        def karma(self, value):
            self.stats["karma"] = int(max(-100, min(value, 100)))

        # Tag management methods
        def add_tag(self, tag):
            """Adds a tag to a character."""
            if tag not in self.tags:
                self.tags.append(tag)

        def remove_tag(self, tag):
            """Removes a tag from a character."""
            if tag in self.tags:
                self.tags.remove(tag)
                
        def has_tag(self, tag):
            """Checks if a character has a tag."""
            return tag in self.tags
            
        def set_tags(self, tags_list):
            """Sets a list of tags to replace existing tags."""
            self.tags = tags_list if tags_list is not None else []
        
        # Stat management methods
        def change_stat(self, stat_name, amount):
            """Changes a stat for a character by an amount."""
            if stat_name in self.stats:
                new_value = self.stats[stat_name] + amount
                if stat_name == "karma":
                    self.stats[stat_name] = max(-100, min(new_value, 100))
                else:
                    self.stats[stat_name] = max(0, min(new_value, 100))

        def set_stat(self, stat_name, value):
            """Sets a stat for a character to a value."""
            if stat_name in self.stats:
                if stat_name == "karma":
                    self.stats[stat_name] = max(-100, min(value, 100))
                else:
                    self.stats[stat_name] = max(0, min(value, 100))
        
        def get_stat(self, stat_name):
            """Gets the value of a stat for a character."""
            return self.stats.get(stat_name, 0)

        # Bio management methods
        @property
        def bio_info(self):
            char_id = self.get_id()
            return CHARACTER_DATA.get(char_id, {}).get("bio_info", {})

        def get_bio_info(self, key):
            """Gets the contents of a bio entry."""
            return self.bio_info.get(key, "未知")
        
        def unlock_bio(self, bio_id):
            """Unlock a bio entry by its ID."""
            self.unlocked_bios.add(bio_id)

        def has_bio(self, bio_id):
            """Check if a bio entry is unlocked."""
            return bio_id in self.unlocked_bios

        def get_visible_bios(self):
            """
            Return a list with only the highest unlocked bio (by numeric ID).
            """
            char_id = self.get_id()
            bios = CHARACTER_DATA.get(char_id, {}).get("bios", [])
            unlocked_bios = [(int(b_id), text) for b_id, text in bios if b_id in self.unlocked_bios]
            if not unlocked_bios:
                return []
            highest_bio = max(unlocked_bios, key=lambda x: x[0])
            return [highest_bio[1]]

        # Outfit management methods
        def get_total_outfits(self):
            """Count how many outfits this character has available"""
            outfits = 0
            while renpy.has_image(f"{self.get_id()}_outf{outfits}"):
                outfits += 1
            if outfits > self._total_outfits_known:
                self._total_outfits_known = outfits
            return outfits

        @classmethod
        def unlock_outfit(cls, unlock_list):
            """Unlocks specified outfits for each profile and sends a notification."""
            unlocked = []
            for profile, outfit_indices in unlock_list:
                if not isinstance(outfit_indices, (list, set, tuple)):
                    outfit_indices = [outfit_indices]
                newly_unlocked = []
                char_id = profile.get_id()
                if not hasattr(persistent, "unlocked_outfits"):
                    persistent.unlocked_outfits = {}
                for outfit_index in outfit_indices:
                    if outfit_index not in profile.unlocked_outfits:
                        profile.unlocked_outfits.append(outfit_index)
                        if char_id:
                            if char_id not in persistent.unlocked_outfits:
                                persistent.unlocked_outfits[char_id] = []
                            if outfit_index not in persistent.unlocked_outfits[char_id]:
                                persistent.unlocked_outfits[char_id].append(outfit_index)
                        newly_unlocked.append(outfit_index)
                if newly_unlocked:
                    unlocked.append((profile, newly_unlocked))
            if unlocked and persistent.notifications_unlocks:
                total_profiles = len(unlocked)
                all_single = all(len(indices) == 1 for _, indices in unlocked)
                if total_profiles == 1:
                    profile, indices = unlocked[0]
                    if len(indices) == 1:
                        message = f"已为 {{color={profile.color}}}{profile.name}{{/color}} 解锁新服装！"
                    else:
                        message = f"已为 {{color={profile.color}}}{profile.name}{{/color}} 解锁 {{color=#e8f8a1}}{len(indices)}{{/color}} 套新服装！"
                elif all_single:
                    names = oxford_comma([f"{{color={p.color}}}{p.name}{{/color}}" for p, _ in unlocked])
                    message = f"已为 {names} 解锁新服装！"
                else:
                    parts = [
                        f"{{color={p.color}}}{p.name}{{/color}}" if len(indices) == 1
                        else f"{{color={p.color}}}{p.name}{{/color}} ({{color=#e8f8a1}}{len(indices)}{{/color}})"
                        for p, indices in unlocked
                    ]
                    message = f"已为 {oxford_comma(parts)} 解锁新服装！"
                renpy.sound.play("ui/Unlock Notification.ogg")
                renpy.notify(message)
        
        def is_outfit_unlocked(self, outfit_index):
            """Check if an outfit is unlocked"""
            return outfit_index in self.unlocked_outfits
        
        def select_outfit(self, outfit_index):
            """Select an outfit for display"""
            if self.is_outfit_unlocked(outfit_index):
                self.selected_outfit = outfit_index
                return True
            return False
        
        def get_id(self):
            """Get character ID from the global chara dictionary"""
            for char_id, profile in chara.items():
                if profile is self:
                    return char_id
            return None
        
        # Profile methods
        @classmethod
        def unlock_profile(cls, unlock_list):
            """Unlocks profiles for each character and sends a notification."""
            if unlock_list and isinstance(unlock_list[0], tuple):
                profiles = [p for p, _ in unlock_list]
            else:
                profiles = unlock_list

            unlocked = []
            for profile in profiles:
                profile.profile = True
                char_id = profile.get_id()
                if char_id and char_id not in persistent.profiles_unlocked:
                    persistent.profiles_unlocked.append(char_id)
                    unlocked.append(profile)
            if unlocked and persistent.notifications_unlocks:
                if len(unlocked) == 1:
                    p = unlocked[0]
                    message = f"{{color={p.color}}}{p.name}{{/color}} 的档案已解锁！"
                else:
                    names = oxford_comma([f"{{color={p.color}}}{p.name}{{/color}}" for p in unlocked])
                    message = f"已为 {names} 解锁新档案！"
                renpy.sound.play("ui/Unlock Notification.ogg")
                renpy.notify(message)

        def lock_profile(self):
            """Lock a specific profile"""
            self.profile = False
            char_id = self.get_id()
            if char_id and char_id in persistent.profiles_unlocked:
                persistent.profiles_unlocked.remove(char_id)

        # Memory management methods
        @classmethod
        def unlock_memory(cls, unlock_list):
            """Unlocks specified memories for each profile and sends a notification."""
            unlocked = []
            for profile, memory_ids in unlock_list:
                if not isinstance(memory_ids, (list, set, tuple)):
                    memory_ids = [memory_ids]
                newly_unlocked = []
                char_id = profile.get_id()
                if not hasattr(persistent, "unlocked_memories"):
                    persistent.unlocked_memories = {}
                for memory_id in memory_ids:
                    if memory_id not in profile.memories_unlocked:
                        profile.memories_unlocked.add(memory_id)
                        if char_id:
                            if char_id not in persistent.unlocked_memories:
                                persistent.unlocked_memories[char_id] = []
                            if memory_id not in persistent.unlocked_memories[char_id]:
                                persistent.unlocked_memories[char_id].append(memory_id)
                        newly_unlocked.append(memory_id)
                if newly_unlocked:
                    unlocked.append((profile, newly_unlocked))
            if unlocked and persistent.notifications_unlocks:
                total_profiles = len(unlocked)
                all_single = all(len(ids) == 1 for _, ids in unlocked)
                if total_profiles == 1:
                    profile, ids = unlocked[0]
                    if len(ids) == 1:
                        message = f"已为 {{color={profile.color}}}{profile.name}{{/color}} 解锁一段新回忆！"
                    else:
                        message = f"已为 {{color={profile.color}}}{profile.name}{{/color}} 解锁 {{color=#e8f8a1}}{len(ids)}{{/color}} 段新回忆！"
                elif all_single:
                    names = oxford_comma([f"{{color={p.color}}}{p.name}{{/color}}" for p, _ in unlocked])
                    message = f"已为 {names} 解锁一段新回忆！"
                else:
                    parts = [
                        f"{{color={p.color}}}{p.name}{{/color}}" if len(ids) == 1
                        else f"{{color={p.color}}}{p.name}{{/color}} ({{color=#e8f8a1}}{len(ids)}{{/color}})"
                        for p, ids in unlocked
                    ]
                    message = f"已为 {oxford_comma(parts)} 解锁新回忆！"
                renpy.sound.play("ui/Unlock Notification.ogg")
                renpy.notify(message)

        def has_memory(self, memory_id):
            """Check if a memory is unlocked for this character."""
            return memory_id in self.memories_unlocked

        def get_unlocked_memories(self):
            """Return a set of unlocked memory IDs."""
            return self.memories_unlocked

    def get_all_memories_by_character():
        """Returns a dict mapping each character id to a set of all their memory ids."""
        char_memories = {}
        for mem in memories:
            mem_id = mem[0]
            char_ids = mem[3]
            for char_id in char_ids:
                if char_id not in char_memories:
                    char_memories[char_id] = set()
                char_memories[char_id].add(mem_id)
        return char_memories

    #Walkthrough Mode Choice Methods
    class ChoiceOption:
        """Creates choice text with additional info to display."""
        def __init__(self, text, stats=None, character_name=None, extra_text=None, path_info=None):
            self.text = text
            self.stats = stats or {}
            self.character_name = character_name
            self.extra_text = extra_text
            self.path_info = path_info
        
        def get_display_text(self):
            """Gets the text and additional info to display."""
            base_text = self.text
            additional_info = []
            
            if persistent.walkthrough_mode and self.path_info:
                if (
                    isinstance(self.path_info, tuple)
                    and isinstance(self.path_info[0], (tuple, list))
                    and isinstance(self.path_info[1], str)
                ):
                    char_ids, path_name = self.path_info
                    chars = [
                        f"{{color={chara[char_id].color}}}{chara[char_id].name}{{/color}}"
                        for char_id in char_ids if char_id in chara
                    ]
                    if chars:
                        chars_text = oxford_comma(chars)
                        path_text = f"({chars_text} {path_name})"
                        additional_info.append(path_text)
                elif (
                    isinstance(self.path_info, tuple)
                    and len(self.path_info) == 2
                    and isinstance(self.path_info[0], str)
                ):
                    char_id, path_name = self.path_info
                    if char_id in chara:
                        color = chara[char_id].color
                        path_text = f"({{color={color}}}{chara[char_id].name}{{/color}} {path_name})"
                        additional_info.append(path_text)
                elif isinstance(self.path_info, list):
                    for path_tuple in self.path_info:
                        if isinstance(path_tuple, tuple) and len(path_tuple) == 2:
                            char_id, path_name = path_tuple
                            if char_id in chara:
                                color = chara[char_id].color
                                path_text = f"({{color={color}}}{chara[char_id].name}{{/color}} {path_name})"
                                additional_info.append(path_text)
            
            if self.extra_text:
                additional_info.append(self.extra_text)

            if not persistent.walkthrough_mode:
                if additional_info:
                    return f"{base_text}\n{{size=16}}{' '.join(additional_info)}{{/size}}"
                return base_text
            
            if isinstance(self.stats, dict):
                all_stats_text = []
                for char_id, char_stats in self.stats.items():
                    if char_id in chara:
                        stats_text = []
                        for stat_type, value in char_stats.items():
                            if value == 0:
                                continue
                            prefix = "+" if value > 0 else ""
                            value_color = "#6fff6f" if value > 0 else "#ff6f6f" if value < 0 else "#ffffff"
                            stat_color = STAT_COLORS.get(stat_type)
                            if stat_type == "karma":
                                if value > 0:
                                    stat_display = f"{{color=#e2ff92}}Benevolence{{/color}} {{color={value_color}}}+{value}{{/color}}"
                                else:
                                    stat_display = f"{{color=#aa2626}}Malevolence{{/color}} {{color={value_color}}}+{abs(value)}{{/color}}"
                            else:
                                stat_display = (
                                    f"{{color={stat_color}}}{stat_type.capitalize()}{{/color}} {{color={value_color}}}{prefix}{value}{{/color}}"
                                    if stat_color else
                                    f"{stat_type.capitalize()} {{color={value_color}}}{prefix}{value}{{/color}}"
                                )
                            stats_text.append(stat_display)
                        if stats_text:
                            if char_id == "mc" and "karma" in char_stats and len(char_stats) == 1:
                                all_stats_text.append(f"({', '.join(stats_text)})")
                            else:
                                char_color = chara[char_id].color
                                char_stats_display = f"({{color={char_color}}}{chara[char_id].name}{{/color}}: {', '.join(stats_text)})"
                                all_stats_text.append(char_stats_display)
                if all_stats_text:
                    additional_info.extend(all_stats_text)
                    
            if additional_info:
                return f"{base_text}\n{{size=16}}{' '.join(additional_info)}{{/size}}"
            else:
                return base_text

        def apply_stats(self):
            """Applies the stat changes in a choice option to the relevant characters."""
            if isinstance(self.stats, dict):
                for char_id, char_stats in self.stats.items():
                    if char_id in chara:
                        profile = chara[char_id]
                        for stat_name, value in char_stats.items():
                            profile.change_stat(stat_name, value)

default chara = {}
        
# Create character instances
init -1 python:
    def initialize_characters():
        """Creates and updates the character information."""
        all_characters = {
            char_id: CharacterProfile(
                color=CHARACTER_DATA[char_id]["color"],
                stats={"affection": 20} if char_id == "layl" else None
            )
            for char_id in CHARACTER_DATA
        }

        #Ensure persistent variables are always initialized
        if not hasattr(persistent, "profiles"):
            persistent.profiles = []
        if not hasattr(persistent, "profiles_unlocked"):
            persistent.profiles_unlocked = []
        if not hasattr(persistent, "unlocked_outfits"):
            persistent.unlocked_outfits = {}
        if not hasattr(persistent, "unlocked_memories"):
            persistent.unlocked_memories = {}
        if not hasattr(persistent, "outfit_selections"):
            persistent.outfit_selections = {}
        if not hasattr(persistent, "notifications_unlocks"):
            persistent.notifications_unlocks = True
        if not hasattr(persistent, "walkthrough_mode"):
            persistent.walkthrough_mode = False

        #Init Profiles
        for char_id, profile in all_characters.items():
            if char_id not in store.chara:
                store.chara[char_id] = profile
        
        #Init Bios
        for char_id, profile in chara.items():
            if char_id in CHARACTER_DATA and CHARACTER_DATA[char_id]["bios"]:
                profile.unlocked_bios.add("1")

        #Init Tags: Merge default tags from CHARACTER_DATA, preserving runtime-added tags
        for char_id, profile in chara.items():
            default_tags = CHARACTER_DATA.get(char_id, {}).get("tags", [])
            for tag in default_tags:
                if tag not in profile.tags:
                    profile.add_tag(tag)

        #Init Outfits
        for char_id, char in chara.items():
            if "Outfits" in char.tags:
                if char_id in persistent.outfit_selections:
                    char.selected_outfit = persistent.outfit_selections[char_id]
                
                current_total = char.get_total_outfits()
                if current_total > char._total_outfits_known:
                    char._total_outfits_known = current_total

        #MC Profile Unlock at Start
        for char_id, profile in chara.items():
            if char_id == "mc":
                profile.profile = True
                if char_id not in persistent.profiles_unlocked:
                    persistent.profiles_unlocked.append(char_id)
            elif char_id == "mcdad":
                profile.profile = True
                if char_id not in persistent.profiles_unlocked:
                    persistent.profiles_unlocked.append(char_id)
            elif char_id == "mcmom":
                profile.profile = True
                if char_id not in persistent.profiles_unlocked:
                    persistent.profiles_unlocked.append(char_id)
            else:
                profile.profile = char_id in persistent.profiles_unlocked

        #Unlocked Profiles
        for char_id, profile in chara.items():
            profile.profile = char_id in persistent.profiles_unlocked
        
        #Unlocked Outfits
        for char_id, profile in chara.items():
            if char_id in persistent.unlocked_outfits:
                for outfit_index in persistent.unlocked_outfits[char_id]:
                    if outfit_index not in profile.unlocked_outfits:
                        profile.unlocked_outfits.append(outfit_index)

        #Unlocked Memories
        if hasattr(persistent, "unlocked_memories"):
            for char_id, memory_list in persistent.unlocked_memories.items():
                if char_id in chara:
                    chara[char_id].memories_unlocked.update(memory_list)

        # Use the keys of all_characters as the valid IDs
        valid_ids = set(all_characters.keys())
        # --- CLEANUP: Remove deleted characters from chara ---
        to_remove = [cid for cid in store.chara if cid not in valid_ids]
        for cid in to_remove:
            del store.chara[cid]
        # --- END CLEANUP ---
        # --- CLEANUP persistent lists ---
        if hasattr(persistent, "profiles_unlocked"):
            persistent.profiles_unlocked = [cid for cid in persistent.profiles_unlocked if cid in valid_ids]
        if hasattr(persistent, "unlocked_outfits"):
            persistent.unlocked_outfits = {cid: v for cid, v in persistent.unlocked_outfits.items() if cid in valid_ids}
        if hasattr(persistent, "unlocked_memories"):
            persistent.unlocked_memories = {cid: v for cid, v in persistent.unlocked_memories.items() if cid in valid_ids}
        # --- END CLEANUP ---

        store.all_characters_order = list(all_characters.keys())