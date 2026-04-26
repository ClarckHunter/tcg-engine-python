from .deck import Deck
from ...cards.card import Card

class Player:

    


    def __init__(self):
        self.deck = Deck()
        self.hand = []
        self.turn: bool = False
        self.pieces:int = 0
        self.food:int = 0

    def on_start_game(self):
        self.deck.set_deck()

    def is_card_in_hand(self, playing_card:Card)->bool:
        for card in self.hand:
            if card is playing_card:
                return True
        return False

    def draw(self, amoun:int):
        self.deck.draw()
    
    def start_turn(self):
        pass
    