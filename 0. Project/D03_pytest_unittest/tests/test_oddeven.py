import pytest
from OddEven import OddEven


@pytest.fixture()
def arrange():
    return OddEven()


def test_get_result_1(arrange):
    res = arrange.get_result([1, 2, 3, 4])
    assert ['X', 'O', 'X', 'O'] == res


def test_get_result_2(arrange):
    res = arrange.get_result([2, 2, 2, 2])
    assert None is res


def test_get_result_3(arrange):
    res = arrange.get_result([1, 23, 33, 24])
    assert ['X', 'X', 'X', 'O'] == res