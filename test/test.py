import os

def _set_path():
    # Add the root of the venv to the path
    # This is necessary to import the selective_search module

    # Get the path to the venv
    venv_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Add the venv path to the path
    import sys
    sys.path.append(venv_path)

_set_path()
import csv
from card import *
from game import Game
from deck import Deck

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
    with open("../boss_monster_cards.csv", 'r') as file:
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
gameManager = Game(loadCards())
print(gameManager._getInput("Pick a card: ", 1, 5))