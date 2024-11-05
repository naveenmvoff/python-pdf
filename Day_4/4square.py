# Create a function to find the square of each element in a given list. 

def squ(n):
    store = []
    for i in n:
        store.append(i**2)
    return store

input1 = list(map(int, input("Enter: ").split()))
result = squ(input1)
print(result)