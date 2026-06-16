# Tuples are Immutable Sequences


# Create a tuple "cardinal_numbers" with "first", "second" and "third"
cardinal_numbers = ("first", "second", "third")


# Display the second object in the tuple
print(cardinal_numbers[1])


# Unpack the tuple into three strings and display them
position1, position2, position3 = cardinal_numbers
print(position1)
print(position2)
print(position3)

# Create a tuple containing the letters of your name from a string
my_name = tuple("David")

# Check whether or not x is in my_name
print("x" in my_name)

# Create tuple containing all but the first letter in my_name
print(my_name[1:])