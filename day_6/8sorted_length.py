#  Create a function that takes a list of strings and returns the list sorted by the length of the strings.
def leng(input1):
    # input1.sort(key=len)   #sort by length
    a = sorted(input1, key=lambda x: len(x))   #sort by length by using lambda
    return a

input1 = input("Enter: ").split()
result = leng(input1)
print(result)