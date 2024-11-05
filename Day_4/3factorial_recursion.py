# Implement a function that returns the factorial of a given number using recursion.

def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        # n! = n * (n-1)!  
        return n * fac(n-1)   # recursive factorial, #fac(n-1) - Repeat call the value

input1 = int(input("Enter: "))
result = fac(input1)
print(result)