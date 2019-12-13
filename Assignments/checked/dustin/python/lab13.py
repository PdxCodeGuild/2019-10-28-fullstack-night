'''
By: Dustin DeShane
Filename: lab13.py
'''

import string
import random #idea to generate and use random cipher to further encode


user_string = input("Please enter a string: ").lower()
user_list = list(user_string)
#print(user_list)
letter_list = list(string.ascii_lowercase)
new_string = []
output = ""

for k in range(0, len(user_list)): #iterates through list
    user_letter = user_list[k]
    if user_letter in string.ascii_lowercase: #only converts ascii characters
        number = string.ascii_lowercase.index(user_letter) + 1 #converts letter to ascii lowercase number
        new_letter_number = number + 13 #shifts the letter
        new_letter = letter_list[(new_letter_number - 1) % len(letter_list)] #converts new ascii number back to character
        new_string.append(new_letter)
    else:
        new_string.append(user_letter) #doesn't convert non characters
for k in range(0, len(new_string)):
    output = output + new_string[k] #converts list back to string
print(output)
