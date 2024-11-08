#  Implement a function that takes a list of strings and returns a set of unique characters present in all strings.
def unique(a):

    special_char = set(a[0])

    for i in a[1:]:
        special_char &= set(i)
    return special_char



input1 = input("Enter: ").split()
result = unique(input1)
print(result)