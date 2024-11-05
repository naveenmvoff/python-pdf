# Given a list of numbers, create a function to find the sum of all positive numbers.

input1 = list(map(int, input("Enter: ").split()))

sum_value = 0
for i in input1:
    if i>0:
        sum_value = sum_value + i
print(sum_value)