from ..game_interfaces.game_interface import GameView


class Event:
    
    def __init__(self, game_view:GameView):
        self.game_view = game_view