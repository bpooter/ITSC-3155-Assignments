"""
Use single-quotes for string literals, e.g. 'software engineering' ,
but use double-quotes for strings that are likely to contain single-quote
characters as part of the string itself (such as error messages,
or any strings containing natural language), e.g. "You've got an error!"
"""

print('There are "double quotes" in this string.')


print("This string's got an apostrophe.")


print(
    """This string was written on multiple lines,
      and it displays across multiple lines"""
)


print(
    "This one-line string was written out \
      using multiple lines"
)

weight = 0.2
animal = "newt"

# Concatenate a number and a string in one print call
print(str(weight) + " kg is the weight of the " + animal + ".")


# Use format() to print a number and a string inside of another string
print("{} kg is the weight of the {}.".format(weight, animal))


# Use formatted string literal (f-string) to reference objects inside a string
print(f"{weight} kg is the weight of the {animal}.")