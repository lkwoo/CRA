import pytest
from calc import Calc

def test_calc1():
    c = Calc()
    result = c.get_sum(1, 2)
    assert result == 3

def test_calc2():
    c = Calc()
    result = c.get_sum(10, 20)
    assert result == 30


if __name__ == "__main__":
    test_calc1()
    test_calc2()