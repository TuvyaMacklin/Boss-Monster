class Card():
    def __init__(self, name: str, description: str):
        self.name = name 
        self.description = description

class RoomCard(Card):
    def __init__(self, name: str, description: str, damage: int, treasures: list, type: str, advanced: bool):
        super().__init__(name, description)
        self.damage = damage
        self.treasures = treasures
        self.type = type
        self.advanced = advanced

    def can_be_built_on_top(self, new_card: RoomCard):
        pass

class HeroCard(Card):
    def __init__(self, name: str, description: str, health: int, treasure: str, value: int):
        super().__init__(name, description)
        self.health = health
        self.treasure = treasure
        self.value = value 

class BossCard(Card):
    def __init__(self, name: str, description: str, treasure: str):
        super().__init__(name, description)
        self.treasure = treasure