from .condition import Condition

class ConditionPlayerHasAtLeastCopies(Condition):
    def __init__(self, name:str,copies:int):
        super().__init__()
        self.name = name
        self.copies = copies

    def check(self, game_interface):
        return game_interface.camp.player().name(self.name).al_least(self.copies)