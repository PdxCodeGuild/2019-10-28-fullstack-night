# Python Program to Check a Given String is Palindrome or Not

string = input("Please enter enter a word : ")
str1 = ""

for i in string:
    str1 = i + str1  
print("Your word backwards is :  ", str1)

if(string == str1):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")