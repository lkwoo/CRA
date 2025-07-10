import pytest
import sum_checker


def test_sum_1():
    res = sum_checker.get_result("25+61=86")
    assert "PASS" == res


def test_sum_2():
    res = sum_checker.get_result("12345+12345=24690")
    assert "PASS" == res


def test_sum_3():
    res = sum_checker.get_result("5++5=10")
    assert "ERROR" == res


def test_sum_4():
    res = sum_checker.get_result("12345+=123")
    assert "ERROR" == res


def test_sum_5():
    res = sum_checker.get_result("10000+1=10002")
    assert "FAIL" == res
