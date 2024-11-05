# Write a program that takes a sentence as input and counts the number of words in it.
def word(input1):
    sep = input1.split()
    return len(sep)

input1 = input("Enter: ")
value = word(input1)
print(value)