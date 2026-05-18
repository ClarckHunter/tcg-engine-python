from .campInterface import CampInterface
from .cardQuery import CardQuery

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..game import Game

class GameInterface:
    def __init__(self, game:'Game'):
        self._game = game
        self.camp = CampInterface(self._game)
        self.player = game.current_player
        self.enemy = game.waiting_player
        self.current_turn = game.turn_number
        
        self.current_face = game.get_current_fase()
