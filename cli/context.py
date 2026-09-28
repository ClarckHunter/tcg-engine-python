from dataclasses import dataclass, field
from typing import Optional

from game_service import GameService
from domain.game import Game

@dataclass
class AppContext:
    service: GameService = field(default_factory=GameService)
    current_game: Optional[Game] = None

    