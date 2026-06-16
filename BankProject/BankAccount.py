import random

class BankAccount:
    bankName = "Money Mart Bank"
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        # private account number variable
        self.__account_number = random.randint(100000000, 999999999)

    def deposit(self, amount):
        if amount <=0:
            print(f'You must deposit an amount less than or equal to zero\nDeposits of ${amount:,.2f} are invalid!\n')
        else:
            self.current_balance += amount
            print(f'You deposit of ${amount:,.2f} was successful\nYour current balance is: ${self.current_balance:,.2f}\n')

    def withdraw(self, amount):

        projected_balance = self.current_balance - amount

        if projected_balance < self.minimum_balance:
            print(f'Not enough money in the bank to withdraw: ${amount:,.2f}\nYou would have ${projected_balance:,.2f} left which is below minimum balance of ${self.minimum_balance:,.2f} that is required.\n')

        elif projected_balance > self.minimum_balance:
            self.current_balance -= amount
            return True
        else:
            print("Not enough money in the bank to withdraw that amount.\n")
        return False

    def print_customer_information_including_bank_title(self):
        return f'Customer Name: {self.customer_name} \nBalance: ${self.current_balance:,.2f}\nRequired Minimum Balance: ${self.minimum_balance:,.2f}\nBank Name: {self.bankName}\nAccount Number: {self.__account_number}'

    def get_account_number(self):
        return self.__account_number

    # unused getter and setter functions
    def set_current_balance(self, amount):
        self.current_balance = amount

    def get_current_balance(self):
        return self.current_balance


    def set_minimum_balance(self, amount):
        self.minimum_balance = amount

    def get_minimum_balance(self):
        return self.minimum_balance


