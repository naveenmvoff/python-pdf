#  Write a program that finds the most frequent element in a list.
def fin_large(input1):

    frequen = {}

    for i in input1:
        frequen[i] = frequen.get(i, 0) + 1         # use to store the value in dict(frequen),   frequen[i] #(use to take the key value) = frequen.get(i, 0) + 1                     
#                                                                                                                                          #(.get is used to take the value of i, its check the i value is there, if it is there that return the value or return 0)
#                                                                                                                                           #then the +1 add the returned value, its use to add the count
    check_max = max(frequen, key=frequen.get)  # max use to find the max # key use to tell, check what the key
    return check_max

input1 = list(map(int, input("Enter: ").split()))
result = fin_large(input1)
print(result)