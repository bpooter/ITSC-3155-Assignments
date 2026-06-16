from typing import override
from BankAccount import BankAccount
import random

class SavingsAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance):

        # account number is private and inherited from BankAccount
        super().__init__(customer_name, current_balance, minimum_balance)

        # protected routing and transfer limit variables
        # randomly generated 8 digit routing number
        self._routing_number = random.randint(10000000, 99999999)

        # randomly generated interest rate
        self._interest_rate = random.uniform(0.00, 0.70)

    # function for finding 1 year ending balance
    def one_year_ending_balance(self):

        ending_balance = self.current_balance * (1 + self._interest_rate/100)

        return ending_balance

    # returns a string of account details and simulated balance in 1 year due to interest and balance
    def simulate_one_year_ending_balance(self):
        ending_balance = self.one_year_ending_balance()
        return f'Account Name: {self.customer_name}\nCurrent Balance: ${self.current_balance:.2f}\nInterest Rate: {self.get_interest_rate():.2f}\nBalance in 1 year: ${ending_balance:.2f}\n'

    # returns interest rate of account
    def get_interest_rate(self):
        return self._interest_rate

    # overridden to string method with additional details of child class
    @override
    def print_customer_information_including_bank_title(self):
        return super().print_customer_information_including_bank_title() + f'\nAccount Type: Savings\nAccount Routing Number: {self._routing_number}\nInterest Rate: {self._interest_rate:.2f}\n'
