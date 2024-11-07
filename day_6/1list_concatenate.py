# Given two lists of numbers, concatenate them into a single list.

#first method by + Operator
def add(input1, input2):
    return input1 + input2

def ext(input1, input2):
    input1.extend(input2)
    return input1




input1 = list(map(int, input("Enter: ").split()))
input2 = list(map(int, input("Enter: ").split()))
result1 = add(input1, input2)
result2 = ext(input1, input2)
print(result1)
print(result2)