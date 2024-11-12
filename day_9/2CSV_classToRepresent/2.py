# Given a CSV file with employee details (name, position, salary), create a class to represent an Employee.

import csv

class EMPLOYEES:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def show_output(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"
    
    def __str__(self):
        return self.show_output()

def data_get_csv(filename):
    store_employees = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row['name']
            position = row['position']
            salary = float(row['salary'])
            employees_data_to_store = EMPLOYEES(name, position, salary)
            store_employees.append(employees_data_to_store)
        return store_employees

hello = r"C:\python-pdf\day_9\2\data.csv"
result  = data_get_csv(hello)
for i in result:
    print(i)