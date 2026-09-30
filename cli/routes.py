from enum import Enum

class Route(Enum):
    MAIN_MENU = "main_menu"
    NEW_GAME_MENU = "new_game_menu"
    CHANGE_DECK_MENU = "change_deck_menu"
    INIT_PHASE_MENU = "init_phase_menu"
    EXIT = "exit"