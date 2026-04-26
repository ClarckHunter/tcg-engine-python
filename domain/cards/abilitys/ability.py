from ..conditions import Condition
from ..effects import Effect
from ..selects import Select
from ...game import GameInterface

class Ability:
    def __init__(self, conditions:list[Condition], effects:list[Effect], selects:list[Select]):
        self.conditions = conditions
        self.effects = effects
        self.selects = selects





    def try_apply(self, game_interface:GameInterface):
        if not self._check_conditions(game_interface):
            return
        
        if not self.selects:
            self._apply_effects(game_interface)
            return
        
        cards = self._try_select_cards(game_interface)

        self._apply_effects(game_interface, cards)
            
        
        



    def _check_conditions(self, game_interface:GameInterface)->bool:
        """Retorna True si TODAS las condiciones se cumplen."""
        for condition in self.conditions:
            if not condition.check(game_interface):
                return False
        return True
    

    def _try_select_card(self, game_interface: GameInterface) -> list:
        """Ejecuta todas las selecciones y devuelve las cartas obtenidas."""
        selected = []
        for select in self.selects:
            card = select.select_card(game_interface)
            if card is not None:
                selected.append(card)
        return selected

    def _apply_effects(self, game_interface:GameInterface, cards:list | None = None):
        """Aplica todos los efectos, opcionalmente con una lista de cartas objetivo."""
        for effect in self.effects:
            effect.apply(game_interface, cards)
    
            

