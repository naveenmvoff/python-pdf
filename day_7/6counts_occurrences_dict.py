# Write a Python program that counts the number of occurrences of each character in a given string using a dictionary.
def count_check(element):
    
    store = {}

    for i in element:
        if i in store:
            store[i] += 1
        else:
            store[i] = 1
    return store

input1 = input("Enter: ")
result = count_check(input1)
print(f"The occurrences of the given string is: {result}")