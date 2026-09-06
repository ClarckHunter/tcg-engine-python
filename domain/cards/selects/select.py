from __future__ import annotations
from ...game.gameInterfaces import CardQuery
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...game import GameInterface
    from ..card import Card

class Select:


    def select_card(self, game_interface:GameInterface, **kwargs)->list[Card]:
        pass