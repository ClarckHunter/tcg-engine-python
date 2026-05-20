from ..gameInterfaces import GameInterface
from ..gameInterfaces import CardResolver
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..game import Game
    from ..gameInterfaces import GameInterface

class Action:
    def __init__(self):
        self._cancel = False

    def execute(self, game:Game):
        if self._cancel:
            return
        
        self.on_resolve()

    def can_resolve(self)->bool:
        return True
    
    def on_resolve(self)->bool:
        pass

    