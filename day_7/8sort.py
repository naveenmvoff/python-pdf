# Create a function that takes a list of dictionaries and sorts them based on a specified key.
def sorting(dict_list, a):
    sort_value = sorted(dict_list, key=lambda d: d.get(a, float('-inf')))    
    return sort_value


dict_list = [
    {"name": "Alice", "age": 100},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

result = sorting(dict_list, "age")
print(result)