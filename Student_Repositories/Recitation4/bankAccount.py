import random


class BankAccount:
    bankName = "Bank of America"

    def __init__(self, customer_name, balance, minimum_balance):
        self.customer_name = customer_name
        self.balance = balance
        self.minimum_balance = minimum_balance
        self._accountnum = random.randint(0, 20)
        self.__routingnum = random.randint(20, 40)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        num = self.balance - amount
        if num < self.minimum_balance:
            print("Error, not enough balance")
            return False
        else:
            self.balance = self.balance - amount
            return True

    def print_Customer_Information(self):
        print(self.customer_name, " has ", self.balance, " dollars in their account at ", self.bankName,
              ". This is a Bank Account, the account number is ", self._accountnum, " and the routing number is ",
              self.__routingnum)

    def transfer(self, account2, amount):
        if self.withdraw(amount):
            account2.deposit(amount)
