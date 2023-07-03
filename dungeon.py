from card import Card, RoomCard

class Dungeon():
    def _init(self, boss: Card):
        self._rooms = ([], [], [], [], [])
        self._boss = boss