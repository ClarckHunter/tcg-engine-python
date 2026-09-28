from .menu import Menu
from ..routes import Route

class InitPhaseMenu(Menu):
    def display(self):
       print("=== Init Phase Menu ===")
       print("Drawing initial hand...")


    def handle(self) -> str:
        pass

    def draw_initial_hand(self):
        pass 

    def display_initial_hand(self):
        pass