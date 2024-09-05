from constants import RANK


class Player:

    def __init__(self, name):
        """deck, discard_pile"""
        self.name = name
        # self.deck = deck
        # self.discard_pile = discard_pile
        self.is_turn = False
        self.hand = []
        self.points_in_hand = 0

    def __str__(self):
        return self.name

    def turn(self):
        if self.is_turn:
            pass
        pass

    def play_points(self, run):
        for card in range(len(run) - 1):
            pass

    # def discard(self, card):
    #     if card in self.hand:
    #         self.discard_pile.append(self.hand.remove(card))
    #         return True 
    #     return False

    # def pickup(self, deck):
    #     if deck: #normal pickup from deck
    #         self.cards.append(self.deck.draw_card())
    #     else: #discard pile
    #         self.cards.append(self.discard_pile.draw_card())
