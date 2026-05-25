from .phase import Phase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .drawPhase import DrawPhase
'''
Clase encargada de recordad en que momento de la batalla estamos, no 
sabe quien esta jugando
'''

class StateMachine:
    
    def __init__(self):
        self.current_state:Phase

    def start_state_machine(self, game):
        self.current_state = DrawPhase(self, game)
        self.state.start()

    def change_state(self, new_phase:Phase):
        self.state.finish()
        self.state = new_phase
        self.state.start()
