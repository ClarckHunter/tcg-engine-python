from domain.game.game import Game
from domain.game.player import Player, Deck
from domain.cards import Card, CardSpace


class GameService:
    """
    Fachada/API del motor. Traduce llamadas del exterior (CLI, FastAPI, tests)
    a operaciones del dominio. NO contiene reglas del juego.
    Stateless: recibe `game` como parámetro en cada operación.
    """

    # ---------------- Casos de uso ----------------

    def start_game(self, deck1: Deck, deck2: Deck) -> Game:
        p1 = Player("Player 1", deck1)
        p2 = Player("Player 2", deck2)
        game = Game()
        game.start_game(p1, p2)
        return game

    def play_card(self, game: Game, player_id: int, card_index: int, card_space_index: int) -> None:
        player = self._resolve_player(game, player_id)
        card = player.hand[card_index]
        card_space = self._resolve_card_space(game, player_id, card_space_index)
        game.play_card(card, player, card_space)

    def activate_effect(self, game: Game, player_id: int, card_index: int, effect_name: str) -> None:
        player = self._resolve_player(game, player_id)
        card = player.hand[card_index]
        game.activate_effect(card, player, effect_name)

    def end_turn(self, game: Game) -> None:
        game.change_turn()

    def is_game_over(self, game: Game) -> bool:
        # tu lógica real (por ejemplo, si algún jugador no tiene cartas)
        return False

    # ---------------- Consultas (DTOs) ----------------

    def get_state(self, game: Game) -> dict:
        return {
            "turn_number": game.turn_number,
            "current_player_id": self._current_player_id(game),
            "current_phase": type(game.get_current_fase()).__name__,
            "players": [
                self._player_dto(p, game)
                for p in (game.player_1, game.player_2)
            ],
        }

    # ---------------- Helpers privados ----------------

    def _resolve_player(self, game: Game, player_id: int) -> Player:
        if player_id == 1: return game.player_1
        if player_id == 2: return game.player_2
        raise ValueError(f"player_id inválido: {player_id}")

    def _resolve_card_space(self, game: Game, player_id: int, index: int) -> CardSpace:
        # ajusta según cómo estén representados los card spaces
        # por ejemplo: player.field[index] o game.camp.get(...)["player_1"][index]
        player = self._resolve_player(game, player_id)
        return player.field[index]   # <-- ajústalo a tu modelo real

    def _current_player_id(self, game: Game) -> int:
        return 1 if game.current_player is game.player_1 else 2

    def _player_dto(self, player: Player, game: Game) -> dict:
        return {
            "name": player.name,
            "hand": [self._card_dto(c) for c in player.hand],
            "field": [self._card_dto(c) for c in player.field],
            "is_current": player is game.current_player,
        }

    def _card_dto(self, card: Card) -> dict:
        return {
            "name": getattr(card, "name", str(card)),
            "id": getattr(card, "id", None),
        }