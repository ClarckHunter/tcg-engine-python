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
        if not cmd:
            return Route.MAIN_MENU

        if cmd[0] == "1":
            return Route.NEW_GAME_MENU

        if cmd[0] == "2":
            return Route.CHANGE_DECK_MENU

        if cmd[0] == "4":
            return "exit"
