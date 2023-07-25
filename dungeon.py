from card import Card, RoomCard

class Dungeon():
    def _init(self, boss: Card):
        self._rooms = ([], [], [], [], [])
        self._boss = boss
    
    def __repr__(self) -> str:
        output = ""

        for room in self._rooms:
            if len(room) > 0:
                output += str(room[-1]) + "\n"

        output += str(self._boss)

        return output
    
    def addRoom(self, room: RoomCard, position: int):
        '''
        Adds a room to the dungeon
        
        Args:
            room (RoomCard): The room to add
            position (int): The position to add the room
        '''
        pass