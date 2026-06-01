from .phase import Phase
from .stateMachine import StateMachine


from ...cards import Card, CardSpace
from ...cards.abilitys import Ability
from ..actionStack import ActionPlayCard, ActionActivateAbility


from ..events import EventMain
from .battlePhase import BattlePhase

class MainPhase(Phase):
    def __init__(self, state_machine, game):
        super().__init__(state_machine, game)
        self._phase_event = EventMain()

    def start(self):
        self._emmit_phase()
        self.reset_attack()

    def play_card(self, card:Card, card_space:CardSpace):
        self._game.current_player.play_card(card)
        self._action_stack.push(ActionPlayCard(card_space, card))
        
    def activate_hability(self, ability:Ability):
        self._action_stack.push(
            ActionActivateAbility(ability)
        )
        

    def next_phase(self):
        self._state_machine.change_state(
            BattlePhase(self._state_machine, self._game)
        )

    def reset_attack(self):
        player_camp = self._game.get_player_camp()
        for card_space in player_camp:
            card_space.can_attack = True