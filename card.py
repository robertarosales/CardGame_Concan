from pydantic import BaseModel

class Card(BaseModel):
    suit : str
    rank : str

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def is_joker(self):
        return self.rank == 'J'