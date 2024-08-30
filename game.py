
from deck import Deck
from player import Player
import math

class Game:

    def __init__(self, players):
        self.players = players

        self.deck = Deck(math.floor(players / 2))
        


    def start(self):
        tmp = []
        self.deck.shuffle()
        for _ in range(self.players):
            tmp.append(Player())

        self.players = tmp


