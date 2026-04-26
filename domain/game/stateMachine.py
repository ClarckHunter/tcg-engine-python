from .phases import Phase, Draw, Feed, Harvest, PreparationDay, BattleDay, BreakCamp

'''
Clase encargada de recordad en que momento de la batalla estamos, no 
sabe quien esta jugando
'''
class StateMachine:
    
    def __init__(self):
        self.current_state = Draw()

    def start_state_machine(self):
        self.state = self.initial_state
        self.state.start()

    def change_state(self, new_phase:Phase):
        self.state.finish()
        self.state = new_phase
        self.state.start()

    def event(self, new_event):
        self.state.event(new_event)

    def can_play_event(self, evet)->bool:
        pass