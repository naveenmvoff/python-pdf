# Create a function to count the number of vowels in a given string.

input1 = input("Enter: ")

abl ="aeiouAEIOU"
count = 0

for i in input1:
    if i in abl:
        count = count + 1

print(count)