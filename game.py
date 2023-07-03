import csv
from card import *
from deck import Deck
from player import Player

class Game():
    #deck of cards
    #town
    #players
    
    def __init__(self, decks):
        self._town = []
        self._hero_deck = decks["hero_deck"]
        self._epic_hero_deck = decks["epic_hero_deck"]
        self._room_deck = decks["room_deck"]
        self._spell_deck = decks["spell_deck"]
        self._boss_deck = decks["boss_deck"]
        self.players = []

    def _deal_hands(self, amount_of_players: int):
        '''
        Shuffles decks and deals hands to all players

        Parameters
        ----------
        amount_of_players : int
            The amount of players in the game
        
        Returns
        -------
        None

        Raises
        ------
        ValueError
            If there are not enough cards in the deck
        '''

        # Shuffle all the decks
        self._hero_deck.shuffle()
        self._epic_hero_deck.shuffle()
        self._room_deck.shuffle()
        self._spell_deck.shuffle()
        self._boss_deck.shuffle()

        # For each player:
        #   Deal a hand
        #   Deal a boss
        for i in range(amount_of_players):
            hand = self._room_deck.draw(5) + self._spell_deck.draw(2)
            boss = self._boss_deck.draw()[0]

            self.players.append(Player(hand, boss))

def cardify(details):
   match details[5]:
      case "Boss":
         return BossCard(details[1], details[6], details[4])
      case "Room":
         match details[2]:
            case "Monster Room":
                return RoomCard(details[1], details[6], details[3], [details[4]], "Monster", False)
            case "Trap Room": 
                return RoomCard(details[1], details[6], details[3], [details[4]], "Trap", False)
            case "Advanced Monster Room":
                return RoomCard(details[1], details[6], details[3], [details[4]], "Monster", True)
            case "Advanced Trap Room":
                return RoomCard(details[1], details[6], details[3], [details[4]], "Trap", True)
      case "Hero":
         match details[2]:
            case "Ordinary Hero":
                return HeroCard(details[1], details[6], details[3], details[4], 1)
            case "Epic Hero":
                return HeroCard(details[1], details[6], details[3], details[4], 2)

decks = {
   "hero_deck":[],
   "epic_hero_deck":[],
   "room_deck":[],
   "boss_deck":[],
   "spell_deck":[],
}
with open("./boss_monster_cards.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    match row[5]:
        case "Boss":
            for i in range(int(row[8])):
                decks["boss_deck"].append(cardify(row))
        case "Hero":
            for i in range(int(row[8])):
                decks["hero_deck"].append(cardify(row))
        case "Room":
            for i in range(int(row[8])):
                decks["room_deck"].append(cardify(row))
        case "Spell":
            for i in range(int(row[8])):
                decks["spell_deck"].append(row)
decks["boss_deck"] = Deck(decks["boss_deck"])
decks["epic_hero_deck"] = Deck(decks["epic_hero_deck"])
decks["hero_deck"] = Deck(decks["hero_deck"])
decks["room_deck"] = Deck(decks["room_deck"])
decks["spell_deck"] = Deck(decks["spell_deck"])
print(decks)
