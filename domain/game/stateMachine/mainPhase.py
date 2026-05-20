from .phase import Phase
from .stateMachine import StateMachine


from ...cards import Card
from ...cards import CardSpace
from ..actionStack import ActionPlayCard

from ..events import EventMain
from .battlePhase import BattlePhase

class MainPhase(Phase):
    def __init__(self, state_machine, game):
        super().__init__(state_machine, game)

    def start(self):
        self._emmit_phase()

    def play_card(self, card:Card, card_space:CardSpace):
        self._game.current_player.play_card(card)
        self._action_stack.push(ActionPlayCard(card, card_space))
        

    def next_phase(self):
        self._state_machine.change_state(
            BattlePhase(self._state_machine, self._game)
        )

    def reset_attack(self):
        player_camp = self._game.get_player_camp()
        for cs in player_camp:
            cs.can_attack = True