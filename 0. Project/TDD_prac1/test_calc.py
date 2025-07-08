from calc import Calc


def test_calc():
    calc = Calc()
    assert calc.get_minus(5, 2) == 3
    assert calc.get_minus(6, 2) == 4
    assert calc.get_minus(1, 5) == 4


def test_fibo():
    calc = Calc()
    assert calc.fibo(1) == 1
    assert calc.fibo(2) == 1
    assert calc.fibo(3) == 1 + 1
    assert calc.fibo(4) == 1 + 2
    assert calc.fibo(5) == 2 + 3
    assert calc.fibo(6) == 3 + 5
    assert calc.fibo(999) == 89
