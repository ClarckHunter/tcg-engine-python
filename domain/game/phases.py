'''
Docstring for portafolio1.domain.game.phases

Son los estados de la maquina de estados y adicionalmente son las fases del juego
'''

class Phase:

    def start(self):
        pass

    def finish(self):
        pass

    def event(self, event:str):
        return False

class Draw(Phase):
    pass

class Feed(Phase):
    pass

class Harvest(Phase):
    pass

class PreparationDay(Phase):
    def event(self, event:str):
        match event:
            case "play_card": True

        return False

class BattleDay(Phase):
    pass

class BreakCamp(Phase):
    pass