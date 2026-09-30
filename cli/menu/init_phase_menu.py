from .menu import Menu
from ..routes import Route

class InitPhaseMenu(Menu):
    def display(self):
       print("=== Init Phase Menu ===")
       print("Drawing initial hand...")
       self.display_initial_hand()


    def handle(self) -> str:
        pass

    

    def display_initial_hand(self)->None:
        hand = self.context.service.get_current_player_hand(self.context.current_game)
        print(hand)