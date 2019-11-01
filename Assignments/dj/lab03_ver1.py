"""
Lab 03
DJ Thomas
10-31-2019
filename: lab03_ver1.py

lab covers the following:
    - float()
    - input()
    - var for input()
    - str()
    - print()
notes:
float()- this allows us to multiply the decimal number (meters) by the user input(). * if meters was a whole number we would replace float() with int().
input()- This allows us to ask a question so the user can answer.
var for input()- the var (meters) creates the input(golf_putt) into a function.
str()- this puts all previous functions together.

in short:
i was able to ask the user, " what was his/her longet putt made in feet"
user answered and i was able to convert feet answer to meters.

    """

golf_putt= float(input(" What is the longest putt you have made in feet: "))

meters= golf_putt * 0.3048

print('Great putt! In meters that would be,' + str(meters))
