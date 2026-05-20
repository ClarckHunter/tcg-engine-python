from ...cards.cardSpace import CardSpace
from ...cards.card import Card

class Camp:
    

    def __init__(self):
        
        
        self.player_1_spaces: list[CardSpace] = [
            CardSpace(),
            CardSpace(),
            CardSpace(),
        ]

        self.player_2_spaces: list[CardSpace] = [
            CardSpace(),
            CardSpace(),
            CardSpace(),
        ]

    

    def get_camp(self)->dict:
        current_camp = {
            "player_1": self.player_1_spaces,
            "player_2": self.player_2_spaces
        }
        return current_camp
