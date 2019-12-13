'''
By: Dustin DeShane
Filename: lab13.py
'''

import string
import random #idea to generate and use random cipher to further encode


user_string = input("Please enter a string: ").lower()
user_list = list(user_string)  # unneccessary
#print(user_list)
letter_list = list(string.ascii_lowercase)  # unneccessary
new_string = []  #
output = ""

for k in range(0, len(user_list)): # 0 is unneccessary
    user_letter = user_list[k]  # consider enumerate instead of this
    if user_letter in string.ascii_lowercase: # nice!
        number = string.ascii_lowercase.index(user_letter) # nice!
        new_letter_number = number + 13 # nice!
        new_letter = letter_list[(new_letter_number) % len(letter_list)] #converts new ascii number back to character
        new_string.append(new_letter)
    else:
        new_string.append(user_letter) #doesn't convert non characters
for k in range(0, len(new_string)):
    output = output + new_string[k] # This can be done with the wonky command ''.join(list)
print(output)


'''
Consider:
use the str.isupper method, and use string.ascii_uppercase as well as string.ascii_lowercase

use the ord, chr method
>>> ord('a')
97
>>> ord('A')
65
You'd have to change the number by an offset to get the number between 0 and 25, then use %26, then add the offset. Offsets are case-sensitive

'''
