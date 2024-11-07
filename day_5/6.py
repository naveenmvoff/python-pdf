# Write a Python program to find the length of the longest word in a sentence.
def long(input1):
   
   spliting = input1.split()
   store = 0
   
   for i in spliting:
      if len(i) > store:
         store = len(i)
   return store



input1 = input("Enter: ")
result = long(input1)
print("The value is: ",result)