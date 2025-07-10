from abc import ABC, abstractmethod

# Before
# class Bird(ABC):
#     @abstractmethod
#     def fly(self): pass
#
#     @abstractmethod
#     def molt(self): pass


class Bird(ABC):
    @abstractmethod
    def molt(self): pass


class FlyBird:
    @abstractmethod
    def fly(self): pass


class SwimBird:
    @abstractmethod
    def swim(self): pass
