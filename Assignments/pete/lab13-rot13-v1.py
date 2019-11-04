'''
lab13-rot13.py
v1
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.
'''
import string
print("Welcome to ROT13 v1.\nThis program will encrypt your secret message.")
in_string = input("Please enter your message to be encoded: ").lower()#take message in
in_list = list(in_string)#convert message to list of individual letters
in_num_list = []
for letter in in_list:
    in_num_list.append(string.ascii_lowercase.index(letter))#this actually worked--it converts the list of letters to their corresponding numbers then adds 13 to shift over
out_num_list = []
for number in in_num_list:
    out_num_list.append((number + 13) % 26)#this should add 13 to each number in the list
out_list = []
for number in out_num_list:
    out_list.append(string.ascii_uppercase[number])#and convert those new numbers to their corresponding letters
out_string = ''.join(out_list)#this turns the list into a string the .join thing is what makes it work
print(f"Your encoded message is {out_string}.")