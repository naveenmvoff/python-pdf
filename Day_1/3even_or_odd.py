# Write a program to check if a number is even or odd.
input1 = list(map(int, input("Enter the number: ").split()))  #to get input of number in list

result = []
for i in input1:  #seprate the each number from the list
    if i % 2 == 0:
        result.append("Even")    # store value in the lsit
    else:
        result.append("Odd")
print(" ".join(map(str, result)))   # the output should be s string formate 