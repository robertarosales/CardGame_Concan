


class Player:

    def __init__(self, name, deck, discard_pile):
        self.name = name
        self.deck = deck
        self.discard_pile = discard_pile
        self.is_turn = False
        self.hand = []
        self.played_points = 0

    def turn(self):
        if self.is_turn:
            pass
        pass

    def play_points(self, run):
        """
            
        """
        pass

    def discard(self, card):
        if card in self.hand:
            self.discard_pile.append(self.hand.remove(card))
            return True 
        return False

    def pickup(self, deck, cards=1):
        if deck: #normal pickup from deck
            self.deck.draw_card()
        else: #discard pile
            self.cards.extend(self.discard_pile.draw_card(cards))
