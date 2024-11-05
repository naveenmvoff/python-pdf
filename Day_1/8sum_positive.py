# Given a list of integers, find the sum of all positive numbers.

input1 = list(map(int, input().split()))

store = 0
for i in input1:
    if i > 0:
        store = i + store
    else:
        continue
print(store)