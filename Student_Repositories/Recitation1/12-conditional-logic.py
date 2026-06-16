# Test whether these expressions are True or False

print(2 == 2)
print(1 < 0)
print(1 <= 1)
print(1 != 1)
print(1 != 2)
print("good" != "bad")
print("good" != "Good")
print(123 == "123")


print((1 <= 1) and (1 != 1))
print(not (1 != 2))
print(("good" != "bad") or False)
print(("good" != "Good") and not (1 == 1))

# Add parentheses so that the following expressions all
# evaluate to True

# False == not True
print(False == (not True))
# True and False == True and False
print((True and False) == (True and False))
# not True and "A" == "B"
print(not (True and "A" == "B"))