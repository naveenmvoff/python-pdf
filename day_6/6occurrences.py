# Write a Python program to count the occurrences of each element in a given list.
def occur(input1):
     
    occurrences = {}  # store the value in dict

    for i in input1:
          if i in occurrences:            #check the value already present in occurrences 
               occurrences[i] += 1          # if yes add 1
          else:                             
               occurrences[i] = 1            # or no initialize the count
    return occurrences


input1 = input("Enter: ").split()
result = occur(input1)
print(result)