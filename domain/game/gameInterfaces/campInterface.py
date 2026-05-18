from .cardQuery import CardQuery

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..game import Game

class CampInterface():
    def __init__(self, game:Game):
        self._game = game


    def player(self, include_empty=False):
        return CardQuery(self._game.get_player_camp(), include_empty)
    
    def enemy(self, include_empty=False):
        return CardQuery(self._game.get_enemy_camp(),include_empty)
    
    def all(self, include_empty=False):
        return CardQuery(
            self._game.get_player_camp() +
            self._game.get_enemy_camp(), include_empty
        )