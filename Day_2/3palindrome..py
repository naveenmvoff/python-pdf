# Implement a program that checks if a given string is a palindrome.

input1 = input("Enter the string: ")

lower = input1.replace(" ", "").lower()

rev = lower[::-1]

if input1 == rev:
    print("Palindrome")
else:
        print("Not a Palindrome")