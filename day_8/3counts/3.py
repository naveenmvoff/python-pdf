# Implement a program that reads a text file and counts the number of words and lines in it.

file = r"C:\WORKS\Learning\Python Learn\python-pdf\day_8\3counts\sample.txt"

word_count = 0
line_count = 0

with open(file, 'r') as counting:
    for i in counting:
        line_count += 1
        word_count += len(i.split())
print("The count of word in the file is", word_count)
print("The count of line in the file is", line_count)