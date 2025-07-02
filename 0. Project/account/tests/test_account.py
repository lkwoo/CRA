import pytest
from bank import Account


def test_transfer_to():
    account1 = Account(500)
    account2 = Account(300)
    account1.transfer_to(account2, 300)
    assert account1.balance == 200 and account2.balance == 600


def tester_transfer_to_except():
    # arrange
    account1 = Account(200)
    account2 = Account(300)

    # act & assert
    with pytest.raises(ValueError):
        account1.transfer_to(account2, 300)
