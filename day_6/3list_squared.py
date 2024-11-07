#  Implement a function that takes a list of numbers and returns a new list with the squared values.
def sqr(input1):
    a = input1
    store = []
    for i in a:
        store.append(i**2)
    return " ".join(map(str, store))
    



input1 = list(map(int, input("Enter: ").split()))
result = sqr(input1)
print(result)