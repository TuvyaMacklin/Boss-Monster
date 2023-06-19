from dungeon import Dungeon

class Player():

    def __init__(self, hand, boss):
        self._dungeon = Dungeon(boss)
        self._hand = hand
        self._heroes_at_entrance = []
    
    def get_card(self, cardName):
        for i in self._hand:
            if i.cardName == cardName:
                return i
            
    def add_card(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self._hand
    
    def remove_card(self, cardName):
        for i in 0..len(self._hand):
            if self._hand.i.cardName == cardName:
                del self._hand.i
    
    def add_hero(self, hero):
        self._heroes_at_entrance.append(hero)

    def remove_hero(self, heroName):
        for i in 0..len(self._heroes_at_entrance):
            if self._heroes_at_entrance.i.heroName == heroName:
                del self._heroes_at_entrance.i