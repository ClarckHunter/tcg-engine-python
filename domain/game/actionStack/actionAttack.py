from __future__ import annotations

from .action import Action
from ..gameInterfaces import CardResolver

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...cards import CardSpace


class ActionAttack(Action):
    def __init__(self, target:CardSpace, source:CardSpace, damage:int):
        super.__init__()
        self.target = target
        self.source = source
        self.damage = damage

    
    def on_resolve(self, game):
        card = self.target.get_card()
        CardResolver.damage_card(card, self.damage)

    def can_resolve(self)->bool:
        if self.target.has_card(): return True
        else: return False