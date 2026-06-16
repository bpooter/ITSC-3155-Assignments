# Create a tuple called data with two values, (1, 2) and (3, 4)
data = ((1, 2), (3, 4))


# Loop over data and print the sum of each nested tuple
index = 1
for row in data:
    print(f"Row {index} sum: {sum(row)}")
    index += 1


# Create the list [4, 3, 2, 1] and assign it to variable numbers
numbers = [4, 3, 2, 1]
print(numbers)


# Create a copy of the number list using [:]
numbers_copy = numbers[:]
print(numbers_copy)

# Sort the numbers list in numerical order
numbers.sort()
print(numbers)