from accounts.account import Account
from accounts.minimum_balannce_reached_exception import MinimumBalanceBreachedException
from accounts.savings_account import SavingAccount

import sys

lisa_account = Account(100,'Lisa','Simpson')

print(lisa_account)
print(lisa_account.first_name)
print(lisa_account._Account__last_name) # not recommended
print(lisa_account._balance) # not recommeded
print(lisa_account.get_balance()) # use the getter instead

bart_account = Account(0,'Bart','Simpson')
print(bart_account.first_name)

bart_account.deposit(50)
print(bart_account.first_name)

# bart_account.deposit(-25)
print(bart_account.get_balance())
print(bart_account.get_lastname())
bart_account.set_lastname("Smith")

print(lisa_account.account_holder)
lisa_account._account_holder = "Lisa Van Outsen"
print(lisa_account._account_holder)

print(lisa_account.get_lastname())

print(bart_account)
print(lisa_account)

total_simpson_money =lisa_account + bart_account
print(total_simpson_money)

current_account = [lisa_account, bart_account]
print("Acounts in list ORIGINAL","~"* 30)
print(current_account)

current_account.sort()
print(current_account)

compare = lambda a: a.get_balance()

current_account.sort(key=compare)
print("Account in list SORTED by Balance", "~"*30)
print(current_account)

# compare = lambda a:a.first_name
current_account.sort(key=lambda a:a.first_name, reverse=True)
print("Accounts in list SORTED ny Firstname","~"* 30)
print(current_account)

print(lisa_account.get_balance())
bart_account.withdraw(20)
print(lisa_account.get_balance())

print(lisa_account.get_balance())
bart_account.withdraw(80)
print(lisa_account.get_balance())

bart_account.withdraw(-100)


# saving account
lisa_saving_account = SavingAccount(300, firstname='Lias',lastname='Simpson',minimum_balance=100)
balance = lisa_saving_account.get_balance()
print(balance)

lisa_saving_account.deposit(100)
print(lisa_saving_account)

try:

    lisa_saving_account.withdraw(150)
    print(lisa_saving_account)

    lisa_saving_account.withdraw(50)
    print(lisa_saving_account)

    lisa_saving_account.withdraw(500)
    print(lisa_saving_account)

except MinimumBalanceBreachedException as ex:
  # log this error
  print("An exception has occured")
  print(f"You would have breached your minimum balance by {ex.get_breach_amount()}")
  ex_type, value, trace_back = sys.exc_info()
  print("Exception type:", ex_type)
  print("Exception value:", value)
  print("Exception traceback:", trace_back)
  print("Line number:", trace_back.tb_lineno)
  print("#"*30)


else:
    print("No exception occurred")
finally:
    print("This is the FINALLY block")
    print(lisa_saving_account)


all_accounts = current_account
all_accounts.append(lisa_saving_account)
print(all_accounts)

for account in all_accounts:
    account.deposit(10)

print(all_accounts)

for account in all_accounts:
    account.withdraw(25)

print(all_accounts)


if hasattr(lisa_saving_account,"__str__"):
    print(lisa_saving_account)

if isinstance(lisa_saving_account, SavingAccount):
    print("Yep - that's a saving account")

 if issubclass(SavingAccount, Account):
     print("Yep - that's a subclass account")