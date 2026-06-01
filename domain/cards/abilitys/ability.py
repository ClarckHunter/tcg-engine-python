from ..conditions import Condition
from ..effects import Effect
from ..selects import Select
from ...game import GameInterface

from ...game.actionStack import ActionActivateEffect

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..card import Card

class Ability():
    def __init__(self, conditions:list[Condition], effects:dict[str, Effect], selects:list[Select]):
        self.conditions = conditions
        
        

    def create_acton(self)->ActionActivateEffect:
        
        
    def get_select(self, name:str)->Select:
        select:Select = self.effects[name].select

        return select


    def check_conditions(self, game_interface:GameInterface)->bool:
        """Retorna True si TODAS las condiciones se cumplen."""
        for condition in self.conditions:
            if not condition.check(game_interface):
                return False
        return True

    def apply(self):
        for effect in self.effects:
            effect.apply()