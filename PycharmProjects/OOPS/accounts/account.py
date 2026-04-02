import sys

class Account:
    #constructor : a specia method that initializes the object
    def __init__(self, intial_amount, firstname, lastname):
        self._balance = intial_amount
        self.first_name = firstname
        self.__last_name = lastname
        self._account_holder = firstname + " " + lastname


    def __str__(self):
        return f"Account:\nFirstname: {self.get_balance()}\nlastname: {self.get_lastname()}" \
        f"\nBalance: ${self.get_balance()}\n**********"


    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("You can not deposit a negative amount", file=sys.stderr)

    def __repr__(self):
        return f"Account Holder: {self._account_holder} Balance:${self.get_balance()}"

    def __add__(self, other):
        return self.get_balance()  + other.get_balance()

    def __gt__(self, other):
        return self.get_balance()  > other.get_balance()


    def withdraw(self,amount):
        if amount >= 0:
            self._balance -= amount
        else:
            print("You can not withdraw a negative amount",file=sys.stderr)

         # getters and setters
         # only a getter make a field readonly
         # only a setter make a field readonly

    def get_balance(self):
        # getters often translate data
        return self._balance

    def get_lastname(self):
        return self.__last_name.capitalize()

    def set_lastname(self, lastname):
        # common to have validation here
         self.__last_name = lastname

# properties are an alternative syntax to getters and setters
# properties are decorators

    @property
    def account_holder(self):
        return self._account_holder

    @account_holder.setter
    def account_holder(self, name):
        self._account_holder = name
        name_parts = name.split()
        self.first_name = name_parts[0]
        lastname = " ".join(name_parts[0])
        # self.__last_name = new_lastname



