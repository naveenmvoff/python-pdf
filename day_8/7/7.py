# Given a text file with a list of numbers, write a function that finds the sum of all numbers in the file.

def adding(txtfile):
    
    total = 0
    
    with open(txtfile, 'r') as file:
        
        for i in file:
            numbers = i.strip().split()   #if the csv file input has sapce empty and the data is there !
            for a in numbers:
                total += float(i.strip())    #the float for consider each line have one input    
        
    return total


txtfile = r"C:\WORKS\Learning\Python Learn\python-pdf\day_8\7\sample.txt"

result = adding(txtfile)
print("The total sum is: ", result) 