from __future__ import annotations

from .action import Action

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...cards.abilitys import Ability



class ActionActivateAbility(Action):
    def __init__(self, ability:Ability):
        super().__init__()
        self.ability = ability
        self.canceled = False

    def on_resolve(self):
        if self.cancel:
            return
        self.ability.apply()

    def cancel(self):
        self.cancel = True