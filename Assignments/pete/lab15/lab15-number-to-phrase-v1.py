'''
lab15-number-to-phrase-v1.py

Version 1:

Convert a given number into its english representation.  For example: 67 becomes 'sixty-seven'.  Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10

Hint 2: use the digit as an index for a list of strings.
'''

print("Welcome to Number to Phrase v1.0.  We'll convert your integer into plain English so you don't have to--It's that Easy!")
while True:
    number_number = int(input("Please enter a number between 0-99: "))
    if number_number not in range(0, 99):
        print("Acceptable numbers only, please.")
        continue
    else:
        break
tens_digit = number_number // 10
ones_digit = number_number % 10
#tens digit conv
if tens_digit == 9:
    tens_letter = 'ninety-'
if tens_digit == 8:
    tens_letter = 'eighty-'
if tens_digit == 7:
    tens_letter = 'seventy-'
if tens_digit == 6:
    tens_letter = 'sixty-'
if tens_digit == 5:
    tens_letter = 'fifty-'
if tens_digit == 4:
    tens_letter = 'forty-'
if tens_digit == 3:
    tens_letter = 'thirty-'
if tens_digit == 2:
    tens_letter = 'twenty-'
#ones digit conv
if ones_digit == 9:
    ones_letter = 'nine'
if ones_digit == 8:
    ones_letter = 'eight'
if ones_digit == 7:
    ones_letter = 'seven'
if ones_digit == 6:
    ones_letter = 'six'
if ones_digit == 5:
    ones_letter = 'five'
if ones_digit == 4:
    ones_letter = 'four'
if ones_digit == 3:
    ones_letter = 'three'
if ones_digit == 2:
    ones_letter = 'two'
if ones_digit == 1:
    ones_letter = 'one'
#concatenation
try:    
    letter_number = tens_letter + ones_letter
except NameError:
#special
    if number_number == 90:
        letter_number = 'ninety'
    if number_number == 80:
        letter_number = 'eighty'
    if number_number == 70:
        letter_number = 'seventy'
    if number_number == 60:
        letter_number = 'sixty'
    if number_number == 50:
        letter_number = 'fifty'
    if number_number == 40:
        letter_number = 'forty'
    if number_number == 30:
        letter_number = 'thirty'
    if number_number == 20:
        letter_number = 'twenty'
    if number_number == 19:
        letter_number = 'nineteen'
    if number_number == 18:
        letter_number = 'eightteen'
    if number_number == 17:
        letter_number = 'seventeen'
    if number_number == 16:
        letter_number = 'sixteen'
    if number_number == 15:
        letter_number = 'fifteen'
    if number_number == 14:
        letter_number = 'fourteen'
    if number_number == 13:
        letter_number = 'thirteen'
    if number_number == 12:
        letter_number = 'twelve'
    if number_number == 11:
        letter_number = 'eleven'
    if number_number == 10:
        letter_number = 'ten'
    if number_number == 9:
        letter_number = 'nine'
    if number_number == 8:
        letter_number = 'eight'
    if number_number == 7:
        letter_number = 'seven'
    if number_number == 6:
        letter_number = 'six'
    if number_number == 5:
        letter_number = 'five'
    if number_number == 4:
        letter_number = 'four'
    if number_number == 3:
        letter_number = 'three'
    if number_number == 2:
        letter_number = 'two'
    if number_number == 1:
        letter_number = 'one'
    if number_number == 0:
        letter_number = 'zero'

print(f"{number_number} is {letter_number}.")
    
