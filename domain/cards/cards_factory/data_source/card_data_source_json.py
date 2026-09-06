from . import CardDataSource
import json
import os

class CardDataSourceJson(CardDataSource):
    def __init__(self):
        self.json_rute:str


    @classmethod
    def search_card(self, card_name):
        return super().search_card(card_name)