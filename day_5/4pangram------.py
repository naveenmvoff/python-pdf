#  Implement a function that checks if a given string is a pangram (contains all letters of the alphabet).
import string

def pangram(input1):
    low = input1.lower().replace(" ", "")

    atoz = set(string.ascii_lowercase)

    if atoz.issubset(set(low)):
        return "Panagaram"
    else:
        return "Not a Panagaram"

input1 = input("Enter: ")
result = pangram(input1)
print(result)