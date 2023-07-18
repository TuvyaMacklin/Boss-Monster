# add root directory to path

import os

def _set_path():
    # Add the root of the venv to the path
    # This is necessary to import the selective_search module

    # Get the path to the venv
    venv_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Add the venv path to the path
    import sys
    sys.path.append(venv_path)

_set_path()

from card import *

hero = HeroCard("theif", "likes money", 6, ["money"], 1)
room = RoomCard("crushinator", "crushes rooms", 3, ["money"], "trap", True)
boss = BossCard("Gorgona", "eats humans", 750, "Money")

print(hero)
print(room)
print(boss)