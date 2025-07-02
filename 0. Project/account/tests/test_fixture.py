import pytest

@pytest.fixture
def ingredient():
    print()
    print("## 닭 준비 ##")
    yield "chicken"
    print()
    print("요리 끝, 청소")

def test_bbq(ingredient):
    assert ingredient == "chicken"
    print("## BBQ 치킨 요리 ##")

def test_kfc(ingredient):
    assert ingredient == "chicken"
    print("## KFC 치킨 요리 ##")