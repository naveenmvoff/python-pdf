# Create a class to represent a basic calculator with add, subtract, multiply, and divide methods.

class cal:
    def adding(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def multi(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero is not working"
        return a / b
    
calc = cal()
input1 = int(input("Enter: "))
input2 = int(input("Enter: "))
print(f"The addtiton value is: {calc.adding(input1, input2)}")
print(f"The subraction value is: {calc.sub(input1, input2)}")
print(calc.multi(input1, input2))
print(calc.div(input1, input2))
print(calc.div(10, 0))