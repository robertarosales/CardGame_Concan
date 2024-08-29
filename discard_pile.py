from collections import deque

class Discard_Pile:
    
    def __init__(self):
        self.cards = deque()

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

    def draw_card(self, index):
        pickups = []
        for _ in range(index):
            pickups.append(self.cards.pop())
        return pickups
