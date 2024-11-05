# Create a Python function to check if a given string is a palindrome

"""
# SIMPLE METHOD

input1 = input()

# rev = input1[::-1]
rev = ''.join(reversed(input1))

if rev == input1:
    print("The given string", input1, "is palindrom")
else:
    print("The given number", input1, "is   not a palindrom")

"""
# LOGICAL METHOD
input1 = input()

rev_store = "" # assign as a string
for char in input1:
    rev_store = char + rev_store #prepend the character
print(rev_store)