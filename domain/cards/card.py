from .abilitys import Ability
from ..game import GameView

class Card:
    #los efectos y condisiones se instancian en otra clase

    def __init__(self,name_id,  damage:int, health:int, mana_cost:int, metal_cost:int):
        
        self.name_id = name_id
        
        self.damage = damage
        self.health = health
        self.max_health = health
        self.mana_cost = mana_cost
        self.metal_cost = metal_cost

        self.triggers:dict [str, Ability]
        self.place_effect:list [Ability]
        self.cast:dict [str, Ability]
        self.defeat:dict [str, Ability]



    def on_cast(self, effect_name:str):
        effect = self.cast[effect_name]
        

    def on_place_card(self, cxt:dict, game_view:GameView):	
        pass

    def on_defeat(self):
        pass
	
    def on_die(self):
        pass