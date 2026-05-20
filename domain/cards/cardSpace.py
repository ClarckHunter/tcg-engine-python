from .card import Card

class CardSpace:
    

    def __init__(self):
        self.card:Card | None = None
        self.can_attack = True
        #self.equipment:Card

    def set_card(self, card:Card):
        self.card = card

    def get_ammount_damage(self):
        damage = self.card.damage

    def is_empty(self)->bool:
        return self.card is None
    
    def get_card(self)->Card:
        return self.card
    
    def has_card(self)->bool:
        if self.card is None: return False
        else: return True
