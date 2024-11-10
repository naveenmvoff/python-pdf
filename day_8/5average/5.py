# Given a CSV file with employee details (name, age, salary), calculate the average salary of all employees.
import csv

csvfile = r"C:\WORKS\Learning\Python Learn\python-pdf\day_8\5average\csvfile.csv"

sallry = 0
employ = 0

with open(csvfile, 'r') as file:
    reader = csv.DictReader(file)
    for i in reader:
        sal = int(i['salary'])
        sallry = sallry + sal
        employ += 1
avg = sallry/employ
print("The Average salary of all the employ is:",avg)