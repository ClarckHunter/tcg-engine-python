from domain.game.game import Game
from domain.game.player import Player, Deck

game = Game()

cards = []
deck_1 = Deck(cards)
player_1 = Player(deck_1)

deck_2 = Deck(cards)
player_2 = Player(deck_2)


game.start_game(player1 = player_1, player2 = player_2)

print(game)