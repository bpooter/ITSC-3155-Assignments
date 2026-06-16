# Take input from the user and display that input back
my_input = input("Type something: ")
print(my_input)


# Display the input string converted to lower-case letters
print(my_input.lower())


# Take user input and display the number of input characters.
input_string = input("Type something else: ")
print(len(input_string))

# Return the upper-case first letter entered by the user

user_input = input("Tell me your password: ")
first_letter = user_input[0]
print("The first letter you entered was: " + first_letter.upper())