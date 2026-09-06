from .phase import Phase
from ..game import Game

from ..events import EventMana
from .mainPhase import MainPhase



class ManaPhase(Phase):
    def __init__(self, state_machine, game:Game):
        super().__init__(state_machine, game)

    def start(self):
        self._current_player.load_mana()
        self._emmit_phase()
        
    def next_phase(self):
        self._state_machine.change_state(
            MainPhase(self._state_machine, self._game
            ))
