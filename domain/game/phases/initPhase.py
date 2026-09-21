from .phase import Phase

class InitialPhase(Phase):
    def __init__(self, state_machine, game):
        super().__init__(state_machine, game)

    def start(self):
        return super().start()