# Write a program that reads a text file and prints its contents.
hello = 'C:/WORKS/Learning/Python Learn/python-pdf/day_8/ex1test.txt'

with open(hello, 'r') as file:
    content = file.read()
    print(content)