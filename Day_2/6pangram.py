# Write a Python program to check if a given string is a pangram (contains all letters of the alphabet).

import string  #Library for alphabet

input1 = input("Enter: ")

low = input1.lower().replace(" ", "")

atoz = set(string.ascii_lowercase)

if atoz.issubset(set(low)):
    print("pangram")
else:
    print("Not a pangram")