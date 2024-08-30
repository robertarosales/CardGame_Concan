from collections import deque

class Discard_Pile:
    
    def __init__(self):
        self.cards = []

    # for testing contents of dicard pile
    # def __str__(self):
    #     rtn = ''
    #     for x in self.cards:
    #         rtn += str(x) + ','
    #     return rtn[:-1]

    # for gameplayer purposes as only last card discarded is available for pickup
    def __str__(self):
        return self.cards[len(self.cards) - 1]
    
    def __len__(self):
        length = 0
        for _ in self.cards:
            length += 1
        return length

    def draw_card(self):
        return self.cards.pop(0)
