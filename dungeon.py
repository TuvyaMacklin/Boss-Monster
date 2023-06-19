from card import Card, RoomCard

class Dungeon():
    def _init(self, boss: Card):
        self._rooms = ([], [], [], [], [])
        self._boss = boss
    
    def get_boss(self):
        return self._boss

    def get_room(self, index: int):
        if self._rooms[index] is None:
            raise Exception("No room at that location")
        return self._rooms[index]

    def build(self, card: RoomCard, position: int):
        if position < 0 or position > 4:
            raise Exception("Invalid room location")
        
        farthest_room = self.get_farthest_room()
        if 

    def get_farthest_room(self):
        for index, location in enumerate(self._rooms):
            if len(location) == 0:
                return index - 1
        
        return 4