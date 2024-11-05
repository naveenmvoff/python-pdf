# Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly.

def check(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
input1 = int(input("Enter: "))
result = check(input1)
print(result)