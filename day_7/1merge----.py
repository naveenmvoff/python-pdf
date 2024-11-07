# Given two dictionaries, merge them into a single dictionary.
def merge(a, b):
    a.update(b)
    return a

input1 = {'a':1, 'b':2}
input2 = {'c':3, 'd':4}
result = merge(input1, input2)
print(result)



"""
# Function to get dictionary input from the user
def get_dict_input(name):
    print(f"Enter key-value pairs for {name} (type 'done' to finish):")
    user_dict = {}
    while True:
        key = input("Enter key (or 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input("Enter value: ")
        user_dict[key] = int(value)  # Convert value to an integer; adjust as needed
    return user_dict

# Get input for both dictionaries
dict1 = get_dict_input("dict1")
dict2 = get_dict_input("dict2")

# Merging dict2 into dict1
dict1.update(dict2)

# Display the merged dictionary
print("Merged dictionary:", dict1)

""" 