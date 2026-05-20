from .action import Action
from ...cards import CardSpace
from ...cards import Card

class ActionPlayCard(Action):
    def __init__(self, card_space:CardSpace, Card:Card):
        super().__init__()
        self.card_space = card_space
        self.card = Card

    def can_resolve(self):
        if self.card_space.is_empty(): return True
        else: return False

    def on_resolve(self):
        self.card_space.set_card(self.card)
        
    