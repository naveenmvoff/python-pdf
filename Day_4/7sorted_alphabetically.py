# Create a function that takes a list of strings and returns the list sorted alphabetically.
def alph(input1):
    sort_value = sorted(input1)
    return sort_value


input1 = input("Enter: ").split()
result = alph(input1)
print(result)