#  Implement a function to check if a given year is a leap year or not.
def leap(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return(f"The {year} is a leap year")
    else:
        return(f"The {year} is not a leap year")

input1 = int(input("Enter: "))
result = leap(input1)
print(result)