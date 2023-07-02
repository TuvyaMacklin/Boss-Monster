from dungeon import Dungeon
from card import *

class Player():

    def __init__(self, hand, boss):
        self._dungeon = Dungeon(boss)
        self._hand = hand
        self._heroes_won = []
        self._heroes_lost = []
    
    def get_card(self, cardName):
        for i in self._hand:
            if i.cardName == cardName:
                return i
            
    def deal_card(self, card):
        self._hand.append(card)

    def get_hand(self):
        return self._hand
    
    def remove_card(self, cardName):
        for i in 0..len(self._hand):
            if self._hand.i.cardName == cardName:
                del self._hand.i
    
    def award_soul(self, hero: HeroCard):
        self._heroes_won.append(hero)

    def award_wound(self, hero: HeroCard):
        self._heroes_lost.append(hero)