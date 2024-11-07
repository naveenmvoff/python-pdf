# Create a function that takes a sentence as input and returns the sentence in reverse order.
def rev(input1):
    splt = input1.split()
    revv = [i[::-1] for i in splt]
    return " ".join(revv)
    
    # return input1[::-1]

input1 = input("Enter: ")
result = rev(input1)
print(result)