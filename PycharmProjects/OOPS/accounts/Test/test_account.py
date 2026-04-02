import pytest

from accounts.account import Account
from accounts.minimum_balannce_reached_exception import MinimumBalanceBreachedException
from accounts.savings_account import SavingAccount


def test_placeholder():
    assert True == True

def test_deposit_positive_succeeds():
    # Triple 'A' Pattern
    # arrange -> Act ->Assert

    #Arrange
    test_account = Account(intial_amount=0, firstname="Julie", lastname="Dooley")

    # Starting_balance = test_account.get_balance()
    # Act
    test_account.deposit(10)
    ending_balance = test_account.get_balance()

    #Assert
    assert ending_balance == 10


