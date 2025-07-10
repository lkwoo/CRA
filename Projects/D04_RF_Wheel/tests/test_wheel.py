import pytest
from wheel import get_award


def test_get_award_1():
    strs = ["BUILDLEV", "EATREALROBOT"]
    userdata = "ERABCDFGHIJKLMNOPQSTUVWXYZ"
    expected = 6500

    actual = get_award(strs, userdata)
    assert actual == expected


def test_get_award_2():
    strs = ["ABS", "ABS", "AAAAAKBA"]
    userdata = "XASBKQDJHMNPTLVUCGEWFORIYZ"
    expected = 9500

    actual = get_award(strs, userdata)
    assert actual == expected
