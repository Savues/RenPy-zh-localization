# DropOut Saga 0.12.0b  x  Shawn's Mod  --  compatibility shim
#
# The mod was written against DropOut 0.6.9a. In 0.12.0b four of the progress
# variables its walkthrough screens read no longer exist, so every guide screen
# (and the mod menu that hosts them) dies with NameError the moment it is shown.
# Declaring them is what brings the walkthrough feature back to life.
#
# The values are mirrors of the 0.12.0b equivalents, refreshed on every label
# change so guide checkmarks keep up with the player's progress.

default lila_var = 0
default lila_black_love = 0
default event_school = 0
default relation_ash = 0

init 100 python:

    def zh_modcompat_sync():
        # lila_var was a 0-10 story-step counter; love_lila is the 0.12.0b
        # cumulative counter for the same storyline, so it tracks the same
        # progression (steps light up in order, with the same off-by-a-few).
        store.lila_var = getattr(store, 'love_lila', 0)

        # lila_black_love gated Lila's dark route -> corruption_lila.
        store.lila_black_love = 1 if getattr(store, 'corruption_lila', 0) > 0 else 0

        # relation_ash was a 0-2 relationship stage; love_ash is uncapped.
        store.relation_ash = min(2, getattr(store, 'love_ash', 0))

        # 0.12.0b dropped the school-event storyline entirely, so those guide
        # entries have no counterpart and stay locked.
        store.event_school = 0

    def zh_modcompat_hook(label=None, abnormal=None, **kwargs):
        zh_modcompat_sync()

    # config.label_callbacks is the list Ren'Py 8 actually invokes; the mod
    # registers its own tracker there too. Appending is additive, so the mod's
    # callback keeps running exactly as before.
    if zh_modcompat_hook not in config.label_callbacks:
        config.label_callbacks.append(zh_modcompat_hook)

    # Make the values sane before the first label runs. getattr() guards this
    # because default statements are not executed during init.
    zh_modcompat_sync()
