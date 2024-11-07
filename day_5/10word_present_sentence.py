# Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence.
def check(input1, word):
    if word in input1:
        return True
    else:
        return False


input1 = input("Enter the sentance: ")
word = input("Enter the word: ")

if check(input1, word):
    print("Yes")
else:
    print("No")