from . import Effect

class EffectDamageCard(Effect):
    def __init__(self, select, damage:int):
        super().__init__(select)
        self.damage = damage

    def _effect(self):
        for target in self.targets:
            target.health -= self.damage
            if target.health <= 0:
                target.die()
        