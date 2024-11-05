# Given a list of words, concatenate them into a single string separated by spaces.
def single(input1):
    a = " ".join(input1)
    return a

input1 = input("Enter: ").split()  #get input as a list
result = single(input1)
print(result)