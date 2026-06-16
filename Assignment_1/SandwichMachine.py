### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    ## function for verifying if a sandwich is able to be made.
    def check_resources(self, order_ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount_needed in order_ingredients.items():
            if amount_needed > resources[ingredient]:
                return False

        return True

    # function for adding coins to machine
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

        #indefinite loop to continue trying for numerical input
        while True:
            try:
                dollars = float(input("Enter the amount of large dollars"))
                half_dollars = float(input("Enter the amount of half dollars"))
                quarters = float(input("Enter the amount of quarters"))
                nickels = float(input("Enter the amount of nickels"))
                break

            # throw value error if input is not numerical
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        total = self.machine_resources + dollars + (.5 * half_dollars) + (.25 * quarters) + (.05 * nickels)
        print(f'You added ${total:.2f} worth of coins.')
        return total

    # function that returns a result which is bool, and coins or change which is float
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < self.machine_resources:
            return False, coins
        else:
            change = coins - cost
            return True, change

    ## will remove the ingredients from the resources dictionary
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient in order_ingredients:
            resources[ingredient] -= recipes[sandwich_size]["ingredients"][ingredient]



### Make an instance of SandwichMachine class and write the rest of the codes ###