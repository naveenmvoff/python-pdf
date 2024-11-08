# Given a list of dictionaries, find the dictionary with the highest value for a specific key.
def find_max(dict_list, just_now):
    find = max(dict_list, key=lambda d:d.get(just_now, float('-inf')))    # use to find max, # d helps to check the specific dict in list, #float('-inf') - is used to return, when the value is not presen in the dict particular dict
    return find


dict_list = [
    {"name": "Alice", "age": 100},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

result = find_max(dict_list, "age")
print(result)