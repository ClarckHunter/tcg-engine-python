from ...cards import Card

class CardResolver:
    
    @staticmethod
    def add_damage(card:Card, damage:int):
        card.damage += damage

    @staticmethod
    def add_max_health(card:Card, health:int):
        card.max_health += health
        card.health += health

    @staticmethod
    def heal_card(card:Card, heal:int):
        card.health += heal
        if card.health > card.max_health:
            card.health = card.max_health
    
    @staticmethod
    def damage_card(card:Card, damage):
        card.health -= damage
        if card.health <= 0:
            card.die()