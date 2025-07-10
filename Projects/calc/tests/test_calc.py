import pytest
from calc import Calc

def test_get_sum():
    c = Calc()
    assert 3 == c.get_sum(1, 2)