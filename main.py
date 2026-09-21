from domain.game import Game
from domain.game.player import Player
from game_builder import GameBuilder
from domain.cards import Card
from cli.main_menu import MainMenu

card = Card("Card 1", "Description of Card 1", 5, 3, 2)


game_builder = GameBuilder()
game = game_builder.add_player("Player 1", 1)

main_menu = MainMenu()
main_menu.display_menu()