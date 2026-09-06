from .phase import Phase
from ..game import Game
from .manaPhase import ManaPhase

from ..events import EventDraw

class DrawPhase(Phase):
    def __init__(self, state_machine, game:Game):
        super().__init__(state_machine, game)


    def start(self):
        self._current_player.draw()
        self._emmit_phase()

    def next_phase(self):
        self._state_machine.change_state(
            ManaPhase(self._state_machine ,self._game)
            )
        
    