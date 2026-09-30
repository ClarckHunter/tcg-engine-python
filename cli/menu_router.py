from .menu import MainMenu, Menu, NewGameMenu, InitPhaseMenu
from .context import AppContext
from .routes import Route

class MenuRouter:
    def __init__(self, context: AppContext):
        self.context = context
        self.menus = {
            Route.MAIN_MENU: MainMenu(context),
            Route.NEW_GAME_MENU: NewGameMenu(context),
            Route.INIT_PHASE_MENU: InitPhaseMenu(context)
            #Route.CHANGE_DECK_MENU: Menu(context),  # Placeholder for the change deck menu
        }
        self.current_menu = Route.MAIN_MENU

    def run(self):
        while self.current_menu != "exit":
            menu = self.menus[self.current_menu]
            if menu is None:
                print(f"Menu '{self.current_menu}' not found.")
                self.current_menu = "main"
                continue
            
            menu.display()
            self.current_menu = menu.handle()