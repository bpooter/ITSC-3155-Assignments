from bankAccount import BankAccount
from savingAccounts import SavingsAccount
from checkingAccounts import CheckingAccount

john = BankAccount("john", 3000, 500)
john.deposit(500)
john.withdraw(3500)
steve = BankAccount("steve", 4000, 1000)
steve.deposit(1000)
steve.withdraw(500)
john.transfer(steve, 100)
john.print_Customer_Information()
steve.print_Customer_Information()

jerry = SavingsAccount("jerry", 1000, 400, .05)
jerry.print_Customer_Information()
jerry.addYears(5)
jerry.calculateInterest()
jerry.print_Customer_Information()

sam = CheckingAccount("sam", 3000, 500, 1000)
sam.transfer(jerry, 1100)
sam.transfer(jerry, 500)
sam.print_Customer_Information()
jerry.print_Customer_Information()

james = SavingsAccount("james", 6000, 1000, .10)
james.print_Customer_Information()
james.transfer(jerry, 1000)
james.print_Customer_Information()
jerry.print_Customer_Information()