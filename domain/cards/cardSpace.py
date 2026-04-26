from .card import Card

class CardSpace:
    

    def __init__(self):
        self.card:Card | None = None
        #self.equipment:Card

    def is_empty(self)->bool:
        return self.card is None