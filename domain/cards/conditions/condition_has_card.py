from .condition import Condition
from ...game import GameInterface

class ConditionPlayerCampNameCard(Condition):
    def __init__(self, name:str):
        super().__init__()
        self.name = name
        
    def check(self, game_interface:GameInterface, name:str)->bool:
        return game_interface.camp.player().name(self.name).exists()
		