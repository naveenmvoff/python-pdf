# Given two sets, find the union, intersection, and difference between them.
def finding(a, b):
    
    union = a.union(b)    # or a | b 
    intersection = a.intersection(b) # or a & b
    difference = a.difference(b) # or a - b

    return union, intersection, difference


input1 = set(map(int, input("Enter: ").split()))
input2 = set(map(int, input("Enter: ").split()))
uni, inte, difff = finding(input1, input2)
print(f"The value are {uni} and {inte} and {difff}")