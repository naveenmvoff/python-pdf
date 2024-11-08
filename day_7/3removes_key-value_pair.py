#  Implement a function that removes a key-value pair from a dictionary.
def remove(my_dict, i):
    if i in my_dict:
        del my_dict[i]

my_dict = {"name": "Alice", "age": 25, "city": "New York"}  

print(f"This is the avliabe dict", my_dict)

i = input("Enter the key you need to remove: ")
remove(my_dict, i)
print(my_dict)
