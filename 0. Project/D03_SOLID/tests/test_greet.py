import pytest
from Greeter import greet
def test_formal():
    g = Greeter()
    assert g.greet() == "Hello."

    g.set_formality("formal")
    assert g.greet() == "Good evening, sir."

    g.set_formality("casual")
    assert g.greet() == "Sup bro?"

    g.set_formality("intimate")
    assert g.greet() == "Hello Darling!"