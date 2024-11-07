# Given a list of names, count the number of names that start with a vowel.
def cou(input1):
    vowels = "aeiouAEIOU"
    count = 0
    for i in input1:
        if i[0] in vowels:
            count = count + 1
    return count

input1 = input("Enter: ").split()
result = cou(input1)
print(result)