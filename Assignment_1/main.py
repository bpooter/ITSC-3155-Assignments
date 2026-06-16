import sys
from SandwichMachine import SandwichMachine
from SandwichMachine import recipes, resources


""" GITHUB REPO URL: https://github.com/bpooter/Assignment_1.git"""

def main():
    show_menu()

def show_menu():
    print("\nWelcome to the Sandwich Machine!\n")

    ## object instantiation with 2.50 balance
    sandwich_machine = SandwichMachine(2.50)

    ## object with 0 balance
    ##sandwich_machine = SandwichMachine(0.0)

    ## indefinite loop till off is chosen
    while True:

        ## retrieving user input and shifting to lower case and stripping whitespace
        choice = input("\nWhat would you like? (small/ medium/ large/ off/ report)")
        choice = choice.lower().strip()

        ## match for options chosen off menu
        match choice:

            case "small" | "medium" | "large":

                #fetching ingredients for sandwich that was chosen
                ingredients = recipes[choice]["ingredients"]

                #fetching cost of chosen sandwich
                cost = recipes[choice]["cost"]

                ## checking to see if resources are available first
                if sandwich_machine.check_resources(ingredients):
                    print("\nSure thing we can make that!\n")

                    ## checking if machine balance allows transaction without adding coins
                    if sandwich_machine.machine_resources < cost:
                        print(f'Your sandwich costs ${cost:.2f}\n'
                                f'And you currently have ${sandwich_machine.machine_resources:.2f} available.\n')

                        ## variable to hold amount of coins added
                        total_added = sandwich_machine.process_coins()

                        ## returning 2 values from transaction_result transaction = bool, change = float
                        transaction, change = sandwich_machine.transaction_result(total_added, recipes[choice]["cost"])

                        ## if transaction is successful make sandwich deducting from resources
                        if transaction:
                            print(f'We are making the sandwich now!\nHere is your change of ${change:.2f}\n')
                            sandwich_machine.make_sandwich(choice, ingredients)
                        else:
                            print(f'Sorry, that is not enough money. Refunding ${change:.2f} to you\n')

                    ## else if there is money on machine already
                    else:
                        ## transaction = bool, change = float. using credit on machine in this call
                        transaction, change = sandwich_machine.transaction_result(sandwich_machine.machine_resources, recipes[choice]["cost"])

                        ## called to deduct ingredients from resources and reset balance after giving change
                        if transaction:
                            print(f'We are making the sandwich now!\nHere is your change of ${change:.2f}\n')
                            sandwich_machine.machine_resources = 0.0
                            sandwich_machine.make_sandwich(choice, ingredients)
                            print(f'{choice} sandwich is ready. Bon appetit!\n')

                ## if resources are too low to make a sandwich display message
                else:
                    print("\nSorry, we don't have enough ingredients.\n")

            ## exit the sandwich machine program
            case "off":
                sys.exit(0)

            ## case for report viewing of resources available
            case "report":
                ## show the resources that are available
                for ingredient, quantity in resources.items():
                    print(ingredient, quantity)

            ## default case for error in main menu
            case _:
                print("You must enter a valid choice from the menu.")


if __name__ == '__main__':
    main()
