import pytest
import split_and_sum, split_and_sum_refac


def test_split_and_sum1():
    text = "0-1-2-3-4-5"
    assert split_and_sum.split_and_sum(text) == split_and_sum_refac.split_and_sum(text)


def test_split_and_sum2():
    text = "A-V-D-E"
    assert split_and_sum.split_and_sum(text) == split_and_sum_refac.split_and_sum(text)


