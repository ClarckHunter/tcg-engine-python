from cli.routes import Route

from .menu import Menu

class NewGameMenu(Menu):
    def display(self):
        print("=== New Game Menu ===")
        print("1. Start New Game")
        print("2. Select Deck (coming soon)")
        print("3. Back to Main Menu")

    def handle(self) -> str:
        cmd = input("> ").strip()
        match cmd:
            case "1":
                self.context.current_game = self.context.service.start_game()
                return Route.INIT_PHASE_MENU
            case "2":
                print("Deck selection is not implemented yet.")
                return Route.NEW_GAME_MENU
            case "3":
                return Route.MAIN_MENU
            case _:
                print("Invalid option. Please try again.")
                return Route.NEW_GAME_MENU