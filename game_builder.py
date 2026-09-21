from domain.game import Game
from domain.game.phases import InitialPhase


class GameBuilder:
    def __init__(self):
        self.game = Game()
    
    def build(self):
        return self.game

    #has una funcion que reciba a un jugador y el numero de jugador que es, despues que lo asigne en game a player 1 y a player 2 dependiendo de lo solicitado
    def add_player(self, player, player_number):
        if player_number == 1:
            self.game.player_1 = player
        elif player_number == 2:
            self.game.player_2 = player
        else:
            raise ValueError("Player number must be 1 or 2")

    #pide un deck y un numero de jugador, y lo asigna al jugador correspondiente
    def add_deck_to_player(self, deck:list, player_number):
        if player_number == 1:
            self.game.player_1.deck = deck
        elif player_number == 2:
            self.game.player_2.deck = deck
        else:
            raise ValueError("Player number must be 1 or 2")

    def start_game(self):
        self.game.start_game(self.game.player_1, self.game.player_2)
        
    