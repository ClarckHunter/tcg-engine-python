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
    
    def play_card(self, card:Card)->bool:
        if self.is_card_in_hand(card):
            self.remove_card_in_hand(card)
            return True
        else: return False

    def draw(self, amoun:int):
        self.deck.draw()

    def load_mana(self):
        pass
    
    def start_turn(self):
        pass
    
    def remove_card_in_hand(self, playing_card:Card):
        for card in self.hand:
            if card is playing_card:
                self.hand.remove(playing_card)