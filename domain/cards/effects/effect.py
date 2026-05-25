from abc import ABC, abstractmethod
from copy import deepcopy

from ...game import GameInterface
from ..selects import Select

from ...game.gameInterfaces import CardResolver

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..card import Card

'''
Clase encargada de guardar la logica del efecto y los targets
'''
class Effect(ABC):
    def __init__(self, select:Select):
        self.select = select
        self.targets:list[Card] = []
    
    
    def apply(self, game_interface:GameInterface, cards:list[Card] | None = None):
        self._effect()
    
    def set_targets(self, cards:list[Card]):
        for card in cards:
            self.targets.append(card)

    def create_effect(self)->Effect:
        return deepcopy(self)

    @abstractmethod
    def _effect(self):
        pass