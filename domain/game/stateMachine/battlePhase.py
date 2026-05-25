from .phase import Phase
from ..events import EventBattle
from ...cards import CardSpace
from ..actionStack import ActionAttack
from .drawPhase import DrawPhase

class BattlePhase(Phase):
    def __init__(self, state_machine, game):
        super().__init__(state_machine, game)

    def start(self):
        self._emmit_phase(
            EventBattle()
        )

    def attackCard(self, target:CardSpace, source:CardSpace):
        source.can_attack = False
        damage = source.get_ammount_damage()
        
        self._game.action_stack.push(
            ActionAttack(target, source, damage)
        )

    def next_phase(self):
        self._state_machine.change_state(
            DrawPhase(self._state_machine, self._game)
        )

    def finish(self):
        self._game.change_turn()