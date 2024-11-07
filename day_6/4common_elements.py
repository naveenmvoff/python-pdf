#  Create a program that finds the common elements between two lists and stores them in a new list.
def common(input1, input2):
    # common_element = [i for i in input1 if i in input2]
    a = set(input1)
    b = set(input2)
    common_element = list(a & b)         #if need remove list the value will, show output as a dictionary
    return common_element

input1 = list(map(int, input("Enter: ").split()))
input2 = list(map(int, input("Enter: ").split()))
result = common(input1, input2)
print(result)