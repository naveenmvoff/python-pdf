# Write a function that takes two lists and returns their intersection (common elements).
def com(input1, input2):
    value1 = set(input1)
    value2 = set(input2)
    
    return value1 & value2


input1 = list(map(int, input("Enter: ").split()))
input2 = list(map(int, input("Enter: ").split()))
result = com(input1, input2)
print(result)