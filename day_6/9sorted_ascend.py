#  Write a program that checks if a given list is sorted in ascending order.
def check_sort(input1):
    a = sorted(input1)
    if a == input1:
        return True
    else:
        return False

input1 = list(map(int, input("Enter: ").split()))
if check_sort(input1):
    print("True")
else:
    print("False")