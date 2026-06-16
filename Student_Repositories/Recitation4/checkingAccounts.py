import random
from bankAccount import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, customer_name, balance, minimum_balance, transferlimit):
        super().__init__(customer_name, balance, minimum_balance)
        self.transferlimit = transferlimit
        self.__routingnum = random.randint(20, 40)

    def withdraw(self, amount):
        if(amount > self.transferlimit):
            print("Sorry, this exceeds your transfer/withdrawal limit")
            return False
        else:
            num = self.balance - amount

            if num < self.minimum_balance:
                print("Error, not enough balance")
                return False
            else:
                self.balance = self.balance - amount
                return True

    def transfer(self, account2, amount):
            if self.withdraw(amount):
                account2.deposit(amount)
            else:
                print("Sorry, this exceeds your transfer limit")

    def print_Customer_Information(self):
        print(self.customer_name, " has ", self.balance, " dollars in their account at ", self.bankName,
              ". This is a Checking Account, the account number is ", self._accountnum, " and the routing number is ",
              self.__routingnum, ". The transfer limit is $", self.transferlimit, " dollars")
