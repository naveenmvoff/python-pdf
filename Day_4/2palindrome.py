# Write a Python function to check if a given string is a palindrome.

input1 = input("Enter: ")

rev = input1[::-1]

if input1 == rev:
    print("palindrome")
else:
    print("Not a palindrome")