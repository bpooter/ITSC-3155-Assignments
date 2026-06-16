def enrollment_stats(list_of_universities):
    # Variables
    total_students = []
    total_tuition = []

    # Iterate through lists, adding values
    for university in list_of_universities:
        total_students.append(university[1])
        total_tuition.append(university[2])

    # Return variables
    return total_students, total_tuition


def mean(values):
    """Return the mean value in the list `values`"""
    return sum(values) / len(values)


universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]

totals = enrollment_stats(universities)

print("*****" * 6)
print(f"Total students:   {sum(totals[0]):,}")
print(f"Total tuition:  $ {sum(totals[1]):,}")
print(f"\nStudent mean:     {mean(totals[0]):,.2f}")
print(f"Tuition mean:   $ {mean(totals[1]):,.2f}")
print("*****" * 6)
print("\n")