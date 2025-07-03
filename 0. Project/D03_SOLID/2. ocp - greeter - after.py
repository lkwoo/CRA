import pytest
from abc import ABC, abstractmethod


class Greeter:
    def __init__(self) -> None:
        super().__init__()
        self.__formality = "normal"

    @abstractmethod
    def greet(self) -> str:
        pass
        if self.__formality == "formal":
            return "Good evening, sir."
        elif self.__formality == "casual":
            return "Sup bro?"
        elif self.__formality == "intimate":
            return "Hello Darling!"
        else:
            return "Hello."

    def set_formality(self, formality: str):
        self.__formality = formality


class GreeterFormal(Greeter):
    def greet(self) -> str:
        return "Hello."


class GreeterCreator():
    def __init__(self, formality):
        g = Greeter()
        g.set_formality(formality)


def test_formal():
    g = Greeter()
    assert g.greet() == "Hello."

    g.set_formality("formal")
    assert g.greet() == "Good evening, sir."

    g.set_formality("casual")
    assert g.greet() == "Sup bro?"

    g.set_formality("intimate")
    assert g.greet() == "Hello Darling!"
