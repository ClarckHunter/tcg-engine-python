from domain.game.game import Game
from portafolio1.domain.game.player.player import Player

class GameBuilder:

    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
		#self.game = Game().start_game(self.p1, self.p2)