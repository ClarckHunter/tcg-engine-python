from ...game import GameInterface
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..card import Card

'''
Clase encargada de los efectos, recibe siempre un GameInterface y
si lo necesita una lista de cartas
'''
class Effect:
    def __init__(self, *args, **kwargs):
        pass
    
    def apply(self, game_interface:GameInterface, cards:list[Card] | None = None):
        pass
    