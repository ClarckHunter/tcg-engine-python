from .action import Action
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