# Calculate the area of a triangle given its base and height using a function.
def area(base, height):
    # area = (1/2) * b * h 
    value = (1/2) * base * height
    return value


base = float(input("Enter: "))
height = float(input("Enter: "))
result = area(base, height)
print(result)