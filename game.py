
from deck import Deck
from player import Player
import math

class Game:

    def __init__(self, players):
        self.players = players
        self.deck = Deck()


    def start(self):
        tmp = []
        self.deck.shuffle()
        for x in range(self.players):
            name = input("Input player " + str(x + 1) + "'s name: ")
            tmp.append(Player(name))

        self.players = tmp
        



""" Testing purposes only """
if __name__ == "__main__":
    g = Game(2)
    g.start()
    for x in g.players:
        print(x)