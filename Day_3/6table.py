# Implement a program that prints the multiplication table of a given number.

input1 = int(input("Enter: "))

for i in range(1,11):   #provide table for 1 to 10
    ans = input1 * i
    print(f"{input1} x {i} = {ans}")