from .select import Select
from ...game import GameInterface
from ...game.gameInterfaces import CampInterface


class SelectByName(Select):
    def __init__(self):
        super().__init__()
		
    def select_card(self, game_interface:GameInterface, **kwargs):
        name = kwargs['name']
        card_query = game_interface.camp.all()
        return card_query.name(name).cards()
