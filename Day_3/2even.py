# Given a list of integers, find all the even numbers and store them in a new list.

input1 = list(map(int, input("Enter: ").split()))

store = []

for i in input1:
    if i % 2 == 0:
        store.append(i)

print(store)