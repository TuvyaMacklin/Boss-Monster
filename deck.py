import random

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