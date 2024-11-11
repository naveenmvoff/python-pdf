# Write a function that reads a JSON file and extracts specific information from it.

import json  # help to use json file in python to read and write a json file
 
def extrat_json(file_path):

    with open(file_path, 'r') as file:
        value = json.load(file)
    
    name = value.get('name', 'Not Available')    # use to get the value from the name in json, if that value is not available that return "Not Avilable"
    age = value.get('age', 'Not Available')      
    city = value.get('city', 'Not Available')
    job_title = value.get('job', {}).get('title', 'Not Available')    # use to get the value from the job and then nested loop of get value
    hobbies = value.get('hobbies', [])


    # use to return the value
    return{               
        'name' : name,     
        'age' : age,
        'city' : city,
        'job_title' : job_title,
        'hobbies' : hobbies
    }

file_path = r'C:\python-pdf\day_8\9\sample.json'
result = extrat_json(file_path)
print(result)