# Write a program that finds the largest and smallest elements in a list.
def find(input1):

    sort = sorted(input1)
    sort_rev = sorted(input1)
    sort_rev.reverse()
    small = sort[0]
    large = sort_rev[0]
    return small , large
    # return rev





input1 = list(map(int, input("Enter: ").split()))
result1, result2 = find(input1)
# result1 = find(input1)
print("small Value is: ", result1)
print("large Value is: ",result2)
