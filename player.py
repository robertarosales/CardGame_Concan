


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

    def play_points(self):
        pass

    def discard(self, card):
        """
            if hand has card and card isn't played
        """
        pass

    def pickup(self):
        """
            pickup from deck or discardpile
            if pickingup
        """
        pass  
