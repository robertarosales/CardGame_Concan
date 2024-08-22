from constants import SUIT_SYMBOLS

class Card:

    def __init__(self, suit, rank, is_joker):
        self.suit = suit
        self.rank = rank
        self.isJoker = is_joker

    def is_joker(self):
        return self.isJoker
    
    def __str__(self):
        return (self.rank + SUIT_SYMBOLS[self.suit])