# Write a function to remove all duplicate characters from a given string.
def dup(input1):
    dictionary = set()
    store = []
    
    for i in input1:
        if i not in dictionary:
            dictionary.add(i)                                # but there is small proble once space come next time thst doesn't come, so, its is only work for single word
            store.append(i)
    return "".join(store)


input1 = input("Enter: ")
result = dup(input1)   
print(result)