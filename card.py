from constants import SUIT_SYMBOLS

class Card:

    def __init__(self, suit, rank, isJoker):
        self.suit = suit
        self.rank = rank
        self.isJoker = isJoker

    def __str__(self): 
        return (self.rank + SUIT_SYMBOLS[self.suit])


    def is_joker(self):
        return self.isJoker
    
    def set_joker(self, rank):
        if self.isJoker:
            self.rank = rank