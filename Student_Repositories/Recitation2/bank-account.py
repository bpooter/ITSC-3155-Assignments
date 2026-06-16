
class BankAccount:

    bank = "Wells Fargo"
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance = self.current_balance + amount
        return self.current_balance

    def withdraw(self, amount):
        if amount > self.current_balance - self.minimum_balance:
            print("Your current balance is not enough!")
        else:
            self.current_balance = self.current_balance - amount
        return self.current_balance

    def print_info (self):
        print(f"{self.customer_name} has ${self.current_balance:,.2f} deposit in {BankAccount.bank}")

customer_1 = BankAccount("John Doe", 1000, 100)

customer_1.deposit(5000)
customer_1.deposit(300)
customer_1.withdraw(1000)

customer_1.print_info()