import sys

from accounts.account import Account
from accounts.minimum_balannce_reached_exception import MinimumBalanceBreachedException


class SavingAccount(Account):

    def __init__(self, amount, firstname, lastname, minimum_balance):
        super().__init__(amount,firstname,lastname)
        self._minimum_balance = minimum_balance

    def __str__(self):
        msg = super().__str__()
        output = "Saving" + msg
        return output


    def withdraw(self,amount):
        if amount >= 0 and self._balance - amount > self._minimum_balance:
            self._balance -= amount
        else:
            # print("You can not withdraw beyond your min balance", file=sys.stderr)
            breach_amount = self._minimum_balance - (self.get_balance() - amount)
            raise MinimumBalanceBreachedException(breach_amount)

        # else:
        #     print("You can not withdraw a negative amount",file=sys.stderr)