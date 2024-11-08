#  Write a program that finds the average value of all the elements in a list of dictionaries.
def average(dict_list, a):
    value = [d.get(a, 0) for d in dict_list if a in d]   # in the dict_list, d is move each dict in the list, if a found in the dict that return the a value else return the 0

    #return value  # to check the value's value

    if value:
        average = sum(value)/len(value)
    else:
        average = 0
    return average


dict_list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

result = average(dict_list, "age")
print(result)