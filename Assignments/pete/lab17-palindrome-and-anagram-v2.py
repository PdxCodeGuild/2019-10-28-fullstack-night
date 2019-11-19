'''
lab17-palindrome-and-anagram-v2.py
Version2

Anagram

Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

    Convert each word to lower case (lower)
    Remove all the spaces from each word (replace)
    Sort the letters of each word (sorted)
    Check if the two are equal

'''

def check_anagram(string1, string2):
    string1.lower()
    string2.lower()
    string1 = string1.replace(' ', '')
    string2 = string2.replace(' ', '')
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

x = input("Welcome to Anagram checker.\nEnter the first word or phrase: ")
y = input("Enter the second word or phrase: ")
status = check_anagram(x, y)
if status == True:
    print(f"{x} and {y} are anagrams")
if status == False:
    print(f"{x} and {y} are not anagrams")