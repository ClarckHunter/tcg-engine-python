from abc import ABC, abstractmethod
class CardDataSource(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def search_card(self, card_name:str):
        pass

    @abstractmethod
    def get_all_cards(self):
        pass