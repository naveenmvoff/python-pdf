# Create a class to represent a Student with attributes like name, age, and grades.

class theStudent:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def avgmark(self):
        if not self.grade:
            return 0
        return sum(self.grade) / len(self.grade)

    def outofthevalue(self):
        return f"Name: {self.name}, Age: {self.age}, Average mark: {self.avgmark()} "


result = theStudent("Naveen", 20, [10, 9, 8, 7])
print(result.outofthevalue())