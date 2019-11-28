import random
import string

# cypher = {
# 'Alpha': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
# 'Rot13': ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
# }

# new_code = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

player = input("Provide the string you wish to encrypt: ")
rot_list = []
s = ""
for letter in player:
    rot_list.append(chr(ord(letter) + 13))

print(s.join(rot_list))
# print(cypher['Alpha'[player]])

### INSTRUCTOR SOLUTION

message = input("Enter your secret message: ")

# encoded_message = []
#
# for c in message:
#     print(c)

def rot13(message):
    encoded_message = [] # currently the variable "encoded message" only exists inside this function
    for c in message:
        e = ord(c)
        if e >= 97 and e <= 97 + 26:
            e -= 97
            e %= 26
            e += 97
            encoded_message.append(char(e))
        elif e >= 65 and e <= 65 + 26: # For user input with capital letters
            e -= 65
            e %= 26
            e += 65
            encoded_message.append(char(e))
        else:
            encoded_message.append(char(e))

    return "".join(encoded_message)
        # print(chr(e))

print(rot13("hello"))
print(rot13("goodbye")) # rot13 is called a "ceasar cypher" because he used it in battle

### INSTRUCTOR SOLUTION: Version 2###

import codecs

def rot13(message)
    return codecs.encode(message, 'rot13')

print(rot13)
