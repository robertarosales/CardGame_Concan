from pydantic import BaseModel
from card import Card

class Deck(BaseModel):
    cards : list[Card]
    