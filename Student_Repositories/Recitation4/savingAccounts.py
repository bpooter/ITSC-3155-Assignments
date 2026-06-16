
import math
import random
from bankAccount import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, customer_name, balance, minimum_balance, interest_rate):
        super().__init__(customer_name, balance, minimum_balance)
        self.interest_rate = interest_rate
        self.yearnum = 0
        self.__routingnum = random.randint(20, 40)

    def addYears(self, years):
        self.yearnum += years

    def calculateInterest(self):
        self.balance = round(self.balance*(math.pow((1 + self.interest_rate), self.yearnum)), 2)

    def print_Customer_Information(self):
        print(self.customer_name, " has ", self.balance, " dollars in their account at ", self.bankName,
              ". This is a Savings Account, the account number is ", self._accountnum, " and the routing number is ",
              self.__routingnum, ". The interest rate is ", self.interest_rate, " for ", self.yearnum, " year(s)")