from domain.cards import Card

class DeckService:

    @staticmethod
    def create_card(name:str, stats:dict)->Card:
        damage = stats["damage"]
        health = stats["health"]
        cost = stats["cost"]
        card = Card(name, damage, health, cost)

        return card

    @staticmethod
    def create_test_card()->Card:
        stats = {
            "damage": 2,
            "health": 2,
            "cost": 1
        }

        card = DeckService.create_card("test_001", stats)

        return card

    @staticmethod
    def create_test_deck()->list:
        deck = []
        for i in range(40):
            deck.append(
                DeckService.create_test_card()
            )

        return deck