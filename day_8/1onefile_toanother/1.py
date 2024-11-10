# # Write a Python program to copy the contents of one text file into another.

# fileold = r"C:\WORKS\Learning\Python Learn\python-pdf\day_8\1onefile_toanother\oldfile.txt"     # Directrly use the name or use the file path
# filenew = r"C:\WORKS\Learning\Python Learn\python-pdf\day_8\1\newfile.txt"     # Directrly use the name or use the file path

with open("oldfile.txt", 'r') as old:
    content = old.read()

with open("newfile.txt", 'w') as new:
    new.write(content)
print("Completed")