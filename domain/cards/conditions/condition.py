from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...game import GameInterface

#clase 
class Condition:
    def __init__(self, *args, **kwargs):
        pass
    
    def check(self, game_interface:GameInterface)->bool:
        pass