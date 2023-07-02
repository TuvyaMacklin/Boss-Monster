class Game():
    #deck of cards
    #town
    #players
    
    def __init__(self, decks):
        self._town = []
        self._hero_deck = decks.hero_deck
        self._epic_hero_deck = decks.epic_hero_deck
        self._room_deck = decks.room_deck
        self._spell_deck = decks.spell_deck
        self._boss_deck = decks.boss_deck