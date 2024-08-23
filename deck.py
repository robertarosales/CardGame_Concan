
from card import Card
from constants import SUIT,RANK
import random

class Deck:

    def __init__(self, packs):
        self.cards = []
        self.packs = packs
        self.jokers = packs * 2

        for _ in range(self.packs):
            for s in SUIT:
                for r in RANK:
                    self.cards.append(Card(s, r, False))
            for _ in range(self.jokers):
                self.cards.append(Card('Joker', '-J', True))

    def __str__(self):
        rtn = ''
        for x in self.cards:
            rtn += str(x) + ','
        return rtn[:-1]
    
    def __len__(self):
        length = 0
        for _ in self.cards:
            length += 1
        return length

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0)


    