import json
from ..card import Card


class CardFactory:
    def __init__(self, cards:list[str, any]):
        self._cards = cards
        
    def create_card(self, card_data:list[str, any])->Card:
        return