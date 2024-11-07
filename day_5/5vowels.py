# Given a string, write a function to remove all vowels from it and return the modified string.
def vowels(input1):
   vowel = "aeiouAEIOU"
   final = [char for char in input1 if char not in vowel]          #check the vowel word in the input1 and remove, if it's avilable
   return "".join(final)
   
   
input1 = input("Enter: ")
result = vowels(input1)
print(result)