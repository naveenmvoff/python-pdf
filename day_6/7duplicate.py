# Given a list of names, remove all duplicate names and print the unique names.
def counting(input1):
    store = []

    for i in input1:
        if i not in store:
            store.append(i)

    return " ".join(store)


input1 = input("Enter: ").split()
result = counting(input1)
print(result)