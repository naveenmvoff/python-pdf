# Write a program that calculates the factorial of a given number.

input1 = int(input("Enter: "))

fact = 1  

if input1 < 0:
    print("NO factorial")
else:
    for i in range(1, input1+1):  
        fact = fact * i
    print(fact)