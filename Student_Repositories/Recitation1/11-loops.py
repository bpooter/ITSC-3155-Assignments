
# print the integer 2 through 10 using a "for" loop
for i in range(2, 11):
    print(i)


# print the integer 2 through 10 using a "while" loop
i = 2
while i < 11:
    print(i)
    i = i + 1


def doubles(num):
    """Return the result of multiplying an input number by 2."""
    return num * 2


# Call doubles() to double the number 2 three times
my_num = 2
for i in range(0, 3):
    my_num = doubles(my_num)


# Calculate interest to track the growth of an investment


def invest(amount, rate, years):
    """Display year on year growth of an initial investment"""
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:,.2f}")


amount = float(input("Enter a principal amount: "))
rate = float(input("Enter an anual rate of return: "))
years = int(input("Enter a number of years: "))

invest(amount, rate, years)