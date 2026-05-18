from ...game import GameInterface
from ..card import Card
from ...game.gameInterfaces import CardQuery

class Select:


    def select_card(self, game_interface:GameInterface, **kwargs)->list[Card]:
        pass