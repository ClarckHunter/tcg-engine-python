from domain.game import Game

class GameService:

    def start_game(self, player1, player2)->Game:
        game = Game(player1, player2)

        game.start_game(player1, player2)

        return game

    def play_card(self, game:Game, card, player, card_space):
        game.play_card(card, player, card_space)
        return game

    def activate_effect(self, game:Game, card, player, effect, selector=None):
        game.activate_effect(card, player, effect, selector)
        return game

    def end_turn(self, game:Game):
        game.end_turn()
        return game

    def change_turn(self, game:Game):
        game.change_turn()
        return game