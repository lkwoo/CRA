from abc import ABC, abstractmethod


# Product
class Doll(ABC):
    @abstractmethod
    def push(self):
        ...


class RedDoll(Doll):

    def push(self):
        print("빨강빨강")


class BlueDoll(Doll):
    def push(self):
        print("파랑파랑")

# Creator
class DollPlayer:
    @abstractmethod
    def create_doll(self):
        ...

    # 공통 로직 (템플릿)
    def play_doll_with(self):
        doll = self.create_doll()
        doll.push()


class RedDollPlayer(DollPlayer):

    def create_doll(self):
        return RedDoll()


player = RedDollPlayer()
player.play_doll_with()