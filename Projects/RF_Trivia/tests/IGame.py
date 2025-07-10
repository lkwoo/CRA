from abc import ABC, abstractmethod


class IGame(ABC):
    @abstractmethod
    def add(self, game):
        ...

    @abstractmethod
    def rolling(self, seed_num):
        ...

    @abstractmethod
    def wrong_answer(self):
        ...

    @abstractmethod
    def was_correctly_answered(self):
        ...
