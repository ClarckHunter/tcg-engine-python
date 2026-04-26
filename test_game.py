from domain.game.game import Game

from portafolio1.domain.game.player.player import Player

from domain.cards.card import Card


p1 = Player()
p2 = Player()

game = Game()


new_game = game.start_game(p1, p2)

empty_card = Card()
new_game.play_card(empty_card, p1, 1)