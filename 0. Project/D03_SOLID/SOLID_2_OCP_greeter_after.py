from abc import ABC, abstractmethod


class Formality(ABC):
    @abstractmethod
    def greet(self):
        ...


class Formal(Formality):
    def greet(self):
        return "Good evening, sir."


class Casual(Formality):
    def greet(self):
        return "Sup bro?"


class Intimate(Formality):
    def greet(self):
        return "Hello Darling!"


class Normal(Formality):
    def greet(self):
        return "Hello."


class Greeter:
    def __init__(self) -> None:
        super().__init__()
        self.formality : Formality
        self.set_formality("normal")

    def greet(self) -> str:
        return self.formality.greet()

    def set_formality(self, formality: str):
        if formality == "formal":
            self.formality = Formal()
        elif formality == "casual":
            self.formality = Casual()
        elif formality == "intimate":
            self.formality = Intimate()
        else:
            self.formality = Normal()


def test_formal():
    greeter = Greeter()
    greeter.set_formality("formal")

    assert greeter.greet() == "Good evening, sir."


def test_casual():
    greeter = Greeter()
    greeter.set_formality("casual")

    assert greeter.greet() == "Sup bro?"


def test_intimate():
    greeter = Greeter()
    greeter.set_formality("intimate")

    assert greeter.greet() == "Hello Darling!"


def test_normal():
    greeter = Greeter()
    greeter.set_formality("normal")

    assert greeter.greet() == "Hello."