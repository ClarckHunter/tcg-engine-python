from .phases import StateMachine as PhaseManager
from .phases import MainPhase

from .events import EventManager
from .gameInterfaces.gameInterface import GameInterface

from .player import Player, Camp, Deck

from ..cards import Card, CardSpace

from ..exeptions import InvalidMove

from .actionStack import Action, ActionStack

#TO DO refactorizar, cambiar el waiting player y current a enemy y player para mejor legibilidad


class Game:

    def __init__(self):
        self.current_player:Player
        self.waiting_player:Player
        self.turn_number: int = 1
        self.player_1:Player
        self.player_2:Player

        self.phase_manager = PhaseManager()

        self.event_manager = EventManager()
        self.camp = Camp()

        self.action_stack = ActionStack()
        

    #funcion que se llama al inicializar una partida
    def start_game(self, player1:Player, player2:Player):
        self.player_1 = player1
        self.player_2 = player2

        self.current_player = self.player_1
        self.waiting_player = self.player_2

        #unicamente para tests
        self.player_1.draw(5)
        self.player_2.draw(5)


        main_phase = MainPhase(self.phase_manager, self)
        
        self.phase_manager.current_state = main_phase
        self.phase_manager.start_state_machine(self)

        return self
        

    #se encarga de cambiar el turno y decirle a los players si es su turno
    def change_turn(self):
        if self.current_player is self.player_1:
            self.current_player = self.player_2
            self.waiting_player = self.player_1

        else:
            self.current_player = self.player_1
            self.waiting_player = self.player_2
            self.turn_number += 1

    #esta funcion se llama desde el game service para jugar la carta, valida si la carta es
    #jugable, coloca la carta y llama al efecto on_place
    def play_card(self, card:Card, player:Player, card_space:CardSpace):
        self.validate_card_played(card, player, card_space)
        card_space.set_card(card)
        ctxt = {}
        card.on_place_card(ctxt, self.create_game_interface())
        

    def activate_effect(self, card:Card, player:Player, effect_name:str):
        card.activate_effect(effect_name)
        

    def finish_game():
        pass

    def push_action(self, action:Action):
        self._action_stack.push(action)

    def create_game_interface(self)->GameInterface:
        return GameInterface(self)


    #valida si se puede jugar la carta
    #esto deberia de ir en su clase propia
    def validate_card_played(self, card:Card, player:Player, card_space:CardSpace):
        if player is not self.current_player:
            raise InvalidMove("Is not your turn")
        if not player.is_card_in_hand(card):
            raise InvalidMove("You dont have this card in your hand")
        if not card_space.is_empty():
            raise InvalidMove("No space to play card")
        #if not self.phase_manager.current_state == MainPhase()
        #    raise InvalidMove("Your not in preparation day")
        
    
    # region getters


    def get_player_id(self)->int:
        if self.current_player is self.player_1: return 1
        else: return 2

    def get_current_fase(self):
        return self.phase_manager.current_state
        
    def get_player_camp(self)->dict:
        current_camp = self.camp.get_camp()

        if self.get_player_id == 1:
            return current_camp["player_1"]
        else:
            return current_camp["player_2"]
        
    
    def get_enemy_camp(self)->dict:
        current_camp = self.camp.get_camp()

        if self.get_player_id == 2:
            return current_camp["player_1"]
        else:
            return current_camp["player_2"]
        
    # endregion