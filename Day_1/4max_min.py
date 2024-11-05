# Given a list of numbers, find the maximum and minimum values

"""
# SIMPLE METHOD
input1 = list(map(int, input().split()))

ordermin = sorted(input1)
min = ordermin[0]

reverse = list(reversed(ordermin))
max = reverse[0]

print(min)
print(max)
"""
#LOGICAL METHOD
input1 = list(map(int, input().split()))

maxvalue = input1[0]
minvalue = input1[0]


for i in input1:
    if i > maxvalue:
        maxvalue = i
    elif i < minvalue:
        minvalue = i
    else:
        continue

print("Max value ", maxvalue)
print("Min value ", minvalue)
        
        