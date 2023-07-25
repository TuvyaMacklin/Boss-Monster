import csv
import random
from card import *

class Deck():
    '''
    A class to represent a deck of cards

    Attributes
    ----------
    cards : stack
        The cards in the deck
    
    Methods
    -------
    shuffle()
        Shuffle the cards in the deck
    
    draw(n = 1) -> list
        Draw n cards from the deck
    '''

    def __init__(self, cards: list):
        # Store the cards as a stack
        self.cards = cards

    def __repr__(self):
        output = ""
        for card in self.cards:
            output += str(card) + "\n"

        return output
    
    def shuffle(self):
        # Shuffle the cards
        random.shuffle(self.cards)

    def draw(self, n: int = 1):
        # Draw n cards from the deck
        if n > len(self.cards):
            raise ValueError("Not enough cards in the deck")

        drawn = []
        for i in range(n):
            drawn.append(self.cards.pop())

        return drawn
    
def cardify(details):
   match details[5]:
      case "Boss":
         return BossCard(details[1], details[6], details[3], details[4])
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

def loadCards():
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
    return decks