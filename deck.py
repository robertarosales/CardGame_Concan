
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
            for j in range(self.jokers):
                self.cards.append(Card('Joker', '-J', True))

    def shuffle(self):
        random.shuffle(self.cards)



    