from domain.game.game import Game
from domain.game.player import Player, Deck
from domain.cards import Card

game = Game()


card = Card('test', 1, 1, 1, 1)

cards = []

for i in range(0,39):
    cards.append(card)

#print(cards)

deck_1 = Deck(cards)
player_1 = Player(deck_1)

deck_2 = Deck(cards)
player_2 = Player(deck_2)


game.start_game(player1 = player_1, player2 = player_2)

#print(game.camp.player_1_spaces[0])

game.play_card(player_1.hand[0], player_1, game.camp.player_1_spaces[0])
game.play_card(player_1.hand[0], player_1, game.camp.player_1_spaces[1])



print(game.camp.player_1_spaces[0].card.name_id)
print(game.camp.player_1_spaces[1].card.name_id)