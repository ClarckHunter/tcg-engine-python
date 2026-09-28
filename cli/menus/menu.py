from abc import ABC, abstractmethod
from cli.context import AppContext

class Menu(ABC):
    def __init__(self, context: AppContext):
        self.context = context

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def handle(self, user_input: str):
        pass