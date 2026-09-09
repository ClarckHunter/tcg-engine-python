from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from ..player import Player
from ..events import Event


if TYPE_CHECKING:
    from .stateMachine import StateMachine
    from ..game import Game

class Phase(ABC):
    def __init__(self, state_machine:StateMachine, game:Game):
        self._state_machine = state_machine
        self._game = game
       
        self._current_player:Player = game.current_player
        self._waiting_player:Player = game.waiting_player
       
        self._event_manager = game.event_manager
        self._phase_event = Event()
        self._action_stack = game.action_stack

        
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def finish(self):
        pass


    def _emmit_phase(self):
        self._event_manager.emit(self._phase_event)