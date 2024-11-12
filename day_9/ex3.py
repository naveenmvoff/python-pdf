# Define a class for a Circle with methods to calculate its area and circumference.

class circle_area:

    def __init__(self, input1):
        self.radius = input1

    def find_area(self):
        return 3.141 * self.radius

input1 = int(input("Enter the r: "))
result = circle_area(input1)
print("The Circle are is:", result.find_area())