# Create a loop that prints all prime numbers between 1 and 50.

def prim(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

print("The number is: ")
for let in range(1, 51):
    if prim(let):
        print(let)