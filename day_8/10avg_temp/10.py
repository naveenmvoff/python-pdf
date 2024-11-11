#  Given a CSV file with temperature data for each day of the week, find the average temperature for each day.

import csv

def avg_temp(file_path):



    # use to store the temp of specify value in this dict
    temperatures_store = {    
        'Monday' : [],
        'Tuesday' : [],
        'Wednesday' : [],
        'Thursday' : [],
        'Friday' : [],
        'Saturday' : [],
        'Sunday' : []
    }

    #open the file
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)  # use to read the file

        for i in reader:        #  loop through the reader
            day = i['day']      # assign the value
            tem = float(i['temperature'])   

            if day in temperatures_store:    # check the day(mondau, tuesday, and ...)
                temperatures_store[day].append(tem)   # append the day to the temp value

    averages = {}  # use to store as a dict

    for day_a, temps_b in temperatures_store.items():     # the temp_a and temp_b both are loop in temperatures_store, The day_a - represent the value of day(Monday, tuesday and ..)
        if temps_b:                      # check the temp_b(tempuratere value) in the particular day
            averages[day_a] = sum(temps_b) / len(temps_b)   # find avg
        else:
            averages[day_a] = None  
    
    return averages


file_path = r'C:\python-pdf\day_8\10avg_temp\data.csv'
result = avg_temp(file_path)
print(result)