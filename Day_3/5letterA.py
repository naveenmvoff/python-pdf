# Given a list of names, print all names starting with the letter 'A'.

input1 = input("Enter: ").split()

for i in input1:
    if i.startswith('A') or i.startswith('a'):
        print(i)