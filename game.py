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
            
    def _getInput(self, prompt: str, min: int, max: int):
        response = input(prompt)
        if (int(response) >= min and int(response) <= max):
            return response
        else:
            print("Please enter a number between", min, "and", max)
            return self._getInput(prompt, min, max)
        
