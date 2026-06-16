# Exercise 1
def cube(num):
    """Return the cube of the input number."""
    cube_num = num**3  # Could also use pow(num, 3)
    return cube_num


print(f"0 cubed is {cube(0)}")
print(f"2 cubed is {cube(2)}")


# Exercise 2
def greet(name):
    """Display a greeting."""
    print(f"Hello {name}!")


greet("Guido")

def convert_cel_to_far(temp_cel):
    """Return the Celsius temperature temp_cel converted to Fahrenheit."""
    temp_far = temp_cel * (9 / 5) + 32
    return temp_far


def convert_far_to_cel(temp_far):
    """Return the Fahrenheit temperature temp_far converted to Celsius."""
    temp_cel = (temp_far - 32) * (5 / 9)
    return temp_cel


# Prompt the user to input a Fahrenheit temperature.
temp_far = input("Enter a temperature in degrees F: ")

# Convert the temperature to Celsius.
# Note that `temp_far` must be converted to a `float`
# since `input()` returns a string.
temp_cel = convert_far_to_cel(float(temp_far))

# Display the converted temperature
print(f"{temp_far} degrees F = {temp_cel:.2f} degrees C")

# You could also use `round()` instead of the formatting mini-language:
# print(f"{temp_far} degrees F = {round(temp_cel, 2)} degrees C"")

# Prompt the user to input a Celsius temperature.
temp_cel = input("\nEnter a temperature in degrees C: ")

# Convert the temperature to Fahrenheit.
temp_far = convert_cel_to_far(float(temp_cel))

# Display the converted temperature
print(f"{temp_cel} degrees C = {temp_far:.2f} degrees F")