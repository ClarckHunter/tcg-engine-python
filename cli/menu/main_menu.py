from .menu import Menu
from cli.context import AppContext
from cli.routes import Route

class MainMenu(Menu):

    def display(self):
        print("=== Main Menu ===")
        print("1. Play")
        print("2. Change decks (coming soon)")
        print("4. Exit")

    def handle(self)->str:
        cmd = input("> ").strip().split()
        
        match cmd:
            case ["1"]:
                return Route.NEW_GAME_MENU
            case ["2"]:
                return Route.CHANGE_DECK_MENU
            case ["4"]:
                return Route.EXIT
            case _:
                return Route.MAIN_MENU
