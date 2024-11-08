#  Create a program that checks if two sets have any elements in common.

def check_common(a, b):
    c = a.intersection(b)    # or use a & b
    return " ".join(map(str, c))        # use to provide normall output

set1 = set(map(int, input("Enter: ").split()))
set2 = set(map(int, input("Enter: ").split()))

result = check_common(set1, set2)
print(result)