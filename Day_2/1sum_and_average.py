#Given a list of numbers, find the sum and average.

input1 = list(map(int, input().split()))

sum_value = sum(input1)

average = sum_value/len(input1)

print("sum of the number is: ", sum_value)
print("average of the number is: ", average)