import sys

from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount


def main():
    """ Creating Accounts """
    # checking account for Patrick Star
    account_1 = CheckingAccount("Patrick Star", 500, 100)

    # checking account for Spongebob Squarepants
    account_3 = CheckingAccount("Spongebob Squarepants", 5000, 100)

    # savings account for Squidward Tentacles
    account_2 = SavingsAccount("Squidward Tentacles", 500, 100)

    # savings account for Eugene Krabs
    account_4 = SavingsAccount("Eugene Krabs", 500, 100)

    """ THESE ARE FOR CHECKING ACCOUNTS """

    """ Showing error when accessing private varaiable """
    # showing invalid print of protected and private variables
    try:
        print(account_3.__account_number)
    except AttributeError as e:
        print(f'\nPrint of caught error: {e}\n')

    # successful print of account number
    print(f'Account number for {account_3.customer_name}: {account_3.get_account_number()}\n')

    """ Showing transfer logic working """
    # setting daily transfer limit to 0 and then trying to transfer money
    # to see a failed transfer
    account_1.set_daily_transfer_limit(0)
    account_1.transfer_money(100)


    # showing that transfer does indeed work
    account_3.transfer_money(500)
    account_3.transfer_money(400)

    """ Demonstrating polymorphism """
    print("\n"+ account_3.print_customer_information_including_bank_title())

    '''END OF CHECKING ACCOUNTS'''

    '''START OF SAVINGS ACCOUNTS'''
    # account 2 and 4 are savings

    # calling overridden function to print full details of account_4
    print(account_4.print_customer_information_including_bank_title())

    # calling method on account 2 to simulate ending balance in 1 year using current balance
    print(account_2.simulate_one_year_ending_balance())

    ''' END OF SAVINGS ACCOUNTS '''

## unused menu function I was developing from misunderstanding assignment
'''def show_menu():

    while True:
        try:
            choice = int(input("Choose an option from the menu\n1. Open a Checking Account\n2. Open a Savings Account\n3. Exit"))

            match choice:
                case 1 | 2:
                    account = open_account(choice)
                    account.print_customer_information_including_bank_title()
                case 3:
                    sys.exit(0)
        except ValueError:
            print('Invalid choice enter a number')
def open_account(choice):
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    full_name = f_name + " " + l_name
    try:
        initial_deposit = float(input("Enter your initial deposit: "))
    except ValueError:
        print('Please enter a numeric value')
    try:
        minimum_balance = float(input("Enter your minimum balance: "))
    except ValueError:
        print('Please enter a numeric value')

    if choice == 1:
        checking_account = CheckingAccount(full_name, initial_deposit, minimum_balance)
        return checking_account
    elif choice == 2:
        savings_account = SavingsAccount(full_name, initial_deposit, minimum_balance)
        return savings_account'''

if __name__ == '__main__':
    main()

