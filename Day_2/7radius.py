# Calculate the area and circumference of a circle given its radius.
import math

input1 = float(input("Enter: "))

area = math.pi * input1**2    # pi * r^2

circumference = 2 * math.pi * input1    # 2*pi*r

print("The area is: ", area)
print("The circumference is: ", circumference)