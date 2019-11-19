'''
lab17-palindrome-and-anagram-v1.py
Version1:
Palindrome

A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome() which takes a string, and returns True if the string's a palindrome, or False if it's not.
'''

def check_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input("Palindrome?: ")

print(check_palindrome(word))