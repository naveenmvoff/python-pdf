# Write a program that converts a given number of days into years, weeks and days.

input1 = int(input())

year = input1//356
year_day = input1%365

week = input1//7
week_day = input1%7



# print("In the given number of", input1, "Days, There is", year, "year and", year_day, "Days are avilable")
# print("In the given number of", input1, "Days, There is", week, "week and", week_day, "Days are avilable")
print("In the given number of", input1, "Days, There is", year, "year and", week, "week and", input1,"days are avilable")
