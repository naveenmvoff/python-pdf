# Create a program that generates the Fibonacci sequence up to a given number of terms.

input1 = int(input("Enter: "))

fab = []

for i in range(input1):
    if i == 0:
        fab.append(0)
    elif i == 1:
        fab.append(1)
    else:
        next = fab[i - 1] + fab[i - 2]
        fab.append(next)
print(fab)