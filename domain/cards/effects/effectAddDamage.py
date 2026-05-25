from .effect import Effect
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..card import Card

class EffectAddDamage(Effect):
    def __init__(self, add_damage:int):
        super().__init__()
        self.add_damage = add_damage


    def _effect(self):
        for target in self.targets:
            target.damage += self.add_damage