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

sandwich_size = input("Input the size: ")
print(recipes[sandwich_size])
print("Cost: ",float(recipes[sandwich_size]['cost']))
print("Resources: ", resources)
print(resources['bread'])


for i in recipes[sandwich_size]["ingredients"]:
    resources[i] = resources[i] - recipes[sandwich_size]["ingredients"][i]

print("Updated resources: ", resources)


is_on=True
order=[]

while is_on:
    option = input("What would you like? ")
    if option =="q":
        is_on = False
    else:
        order.append(option)


print("\n")
print("Your order:")
for i in order:
    print(i)

