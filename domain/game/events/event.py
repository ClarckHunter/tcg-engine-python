from ..gameInterfaces.gameInterface import GameInterface


class Event:
    
    def __init__(self, game_view:GameInterface):
        self.game_view = game_view