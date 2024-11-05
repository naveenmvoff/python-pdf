# Create a program that takes a year as input and checks if it is a leap year or not.

input1 = int(input("Enter: "))

if (input1 % 4 == 0 and input1 % 100 !=0) or (input1 % 400 == 0):
    print("Leap year")
else:
    print("Not a Leap year")