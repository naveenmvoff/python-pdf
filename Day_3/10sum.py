# Calculate the sum of digits of a given number.

input1 = int(input("Enter: "))

sum_value = 0

while input1 > 0:  #grester than zero
    last_digit = input1 % 10 #This is will give the value of reminder the division
    sum_value = sum_value + last_digit      #add
    input1 = input1 // 10       # remove last value by using floor division

print("sum of the number is: ", sum_value)