from .action import Action
from .actionStack import ActionStack
from ..gameInterfaces import GameInterface

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..game import Game
    from ..gameInterfaces import GameInterface

class ActionResolver:
    def __init__(self, game:Game):
        self._stack = ActionStack
        self._game = game
        
        


    def add_action(self, action:Action)->None:
        self._stack.push(action)

    def resolve_all(self)->None:
        while not self._stack.empty():
            self.resolve_top()
            

    def resolve_top(self)->None:
        if self._stack.empty():
            return
        action:Action = self._stack.pop()

        if not action.can_resolve():
            return
        
        action.execute()
