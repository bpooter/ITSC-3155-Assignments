from BankAccount import BankAccount
from typing import override
import random

class CheckingAccount(BankAccount):

    # daily transfer limit variable
    daily_transfer_limit = 500

    # constructor for child class
    def __init__(self, customer_name, current_balance, minimum_balance):

        # call super constructor to set values
        super().__init__(customer_name, current_balance, minimum_balance)

        # protected routing randomly generated 8 digit number and transferred_today variables
        self._routing_number = random.randint(10000000, 99999999)
        self._transferred_today = 0


    # function for transferring money
    def transfer_money(self, amount):
        projected_total_transfers = self._transferred_today + amount

        # if the amount transferred is less than daily limit then proceed
        if self._transferred_today < self.daily_transfer_limit:

            # if amount is greater than the daily limit then notify user
            if amount > self.daily_transfer_limit or projected_total_transfers > self.daily_transfer_limit:
                print('This amount exceeds transfer limit\nTry another amount.\n')

            # else call withdraw of parent class, if withdraw is successful
            # increase amount transferred_today by the amount
            else:
                if self.withdraw(amount):

                    self._transferred_today += amount
                    print(f'Transfer of ${amount:.2f} Success!\nCurrent Balance: ${self.current_balance:,.2f}\n')

        # if the transfer limit has already been reached show message
        else:
            print(f'Transfer limit reached for {self.customer_name}\nTry again tomorrow\n')

    # set the daily transfer limit
    def set_daily_transfer_limit(self, amount):
        self.daily_transfer_limit = amount

    # return the routing number
    def get_routing_number(self):
        return self._routing_number

    # overridden function that provides additional details of child class
    @override
    def print_customer_information_including_bank_title(self):
        return super().print_customer_information_including_bank_title() + f'\nAccount Type: Savings\nAccount Routing Number: {self._routing_number}\nDaily transfer limit: ${self.daily_transfer_limit:.2f}\nAmount transferred today: ${self._transferred_today:.2f}\n'