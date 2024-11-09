# Read a CSV file and process its data.
import csv

file = 'C:\WORKS\Learning\Python Learn\python-pdf\day_8\ex3\data.csv'

with open(file, mode='r', newline='') as csvfile:
    openCsvFile = csv.reader(csvfile)    #use to open the data file in openCsvFile   viva csvfile
    
    head = next(openCsvFile)  #for the heading perpose
    print(f"Head: {head}")  
    
    for i in openCsvFile:
        name = i[0]
        age = int(i[1])
        occupation = i[2]
        
        
        print(f"Name: {name}, age: {age}, occupation: {occupation}")
        