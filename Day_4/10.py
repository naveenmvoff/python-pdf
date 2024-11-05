# Create a function that takes a number as input and prints its multiplication table.

def table(input1):

    store = []  # collect all the value and send in the return     

    for i in range(1, 11):
        ans = i * input1
        store.append(f"{i} x {input1} = {ans}")           #we need to complete the loop, so, we store the value then return
    return store

input1 = int(input("Enter: "))
result = table(input1)

for i in result:  # print in next line
    print(i)