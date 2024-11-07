# Implement a function that takes two lists and returns their union (all unique elements from both lists).
def union(a, b):
    a1 = set(a)
    b1 = set(b)
    return list(a1.union(b1))  # or another method a1 | b1


input1 = list(map(int, input("Enter: ").split()))
input2 = list(map(int, input("Enter: ").split()))
result = union(input1, input2)
print(result)