from .action import Action
from ...cards.abilitys import Ability

class ActionActivateEffect(Action):
    def __init__(self, ability:Ability):
        super().__init__()
        self.ability = ability

    def on_resolve(self):
        self.ability.try_apply()