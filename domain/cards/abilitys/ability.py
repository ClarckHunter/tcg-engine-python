from ..conditions import Condition
from ..effects import Effect
from ..selects import Select
from ...game import GameInterface

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..card import Card

class Ability():
    def __init__(self, conditions:list[Condition], effects:list[Effect], selects:list[Select]):
        self.conditions = conditions
        self.effects = effects
        

    def create_effect(self, name:str, targets:list[Card])->Effect:
        effect:Effect = self.effects[name].create_effect()
        if targets is not None:
            effect.set_targets(targets)
        return effect
        
    def get_select(self, name:str)->Select:
        select:Select = self.effects[name].select

        return select


    def check_conditions(self, game_interface:GameInterface)->bool:
        """Retorna True si TODAS las condiciones se cumplen."""
        for condition in self.conditions:
            if not condition.check(game_interface):
                return False
        return True

    
