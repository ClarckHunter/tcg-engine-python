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

    #esta funcion determina si el espacio para jugar la carta esta disponible en el arreglo
    #regresa falso si no esta disponible el espacio
    #regresa verdadero si el espacio esta vacio
    def is_card_space_empty(self, id_player:int, card_space:int)->bool:
        if id_player == 1:
            if not self.player_1_spaces[card_space].have_card():
                return True
        return False
    
    #establece la carta en el espacio recibido
    def set_card(self, card:Card, player_id, card_space:int):
        if player_id == 1:self.player_1_spaces[card_space] = card
        else: self.player_2_spaces[card_space] = card

    def get_camp(self)->dict:
        current_camp = {
            "player_1": self.player_1_spaces,
            "player_2": self.player_2_spaces
        }
        return current_camp