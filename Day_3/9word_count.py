# Given a list of words, count the number of words with more than five characters.

input1 = input("Enter: ").split()  # get input as a lsit

count = 0

for i in input1:   # move to the each word in the list
    if len(i) > 5:  # check the word have a more than 5 letter
        count = count +1   #increment
print(count)