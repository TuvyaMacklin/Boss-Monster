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
    
    def __repr__(self):
        # Return a string representation of a room card
        # Monster's Ballroom (Advanced Monster Room) - Treasures: Fighter | Damage: *


        output = ""
        output += self.name + " (" + self.type + ") - Treasures: "

        for treasure in self.treasures[:-1]:
            output += treasure + ", "
        output += self.treasures[-1] + " | "

        output += "Damage: " + self.damage

        return output

class HeroCard(Card):
    def __init__(self, name: str, description: str, health: int, treasure: str, value: int):
        super().__init__(name, description)
        self.health = health
        self.treasure = treasure
        self.value = value 

    def __repr__(self):
        # Cleric (Ordinary Hero)4,Cleric

        output = ""
        output += self.name + " (" + str(self.value) + ") - HP: " + 

        output += self.treasure

        return output

class BossCard(Card):
    def __init__(self, name: str, description: str, treasure: str):
        super().__init__(name, description)
        self.treasure = treasure