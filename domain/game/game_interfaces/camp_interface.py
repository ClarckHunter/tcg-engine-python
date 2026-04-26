from .card_query import CardQuery

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..game import Game

class CampInterface():
    def __init__(self, game:Game):
        self._game = game


    def player(self):
        return CardQuery(self._game.get_player_camp())
    
    def enemy(self):
        return CardQuery(self._game.get_enemy_camp())
    
    def all(self):
        return CardQuery(
            self._game.get_player_camp() +
            self._game.get_enemy_camp()
        )