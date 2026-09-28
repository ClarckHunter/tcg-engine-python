from .menu import Menu
from cli.context import AppContext

class MainMenu(Menu):

    def display(self, context: AppContext):
        print("=== Main Menu ===")
        print("1. Start Game")
        print("2. Change deck (coming soon)")
        print("4. Exit")

    def handle(self)->str:
        cmd = input("> ").split().split()
        if not cmd:
            return "game"

        if cmd[0] == "1":
            return "game"

        if cmd[0] == "2":
            return "change_deck"

        if cmd[0] == "4":
            return "exit"
