import math #'''import math-The math module is a standard module in Python and is always 
#available. To use mathematical functions under this module, you have to import the module using import math . 
#It gives access to the underlying C library functions.'''

number = int(input("Enter in a number 0-99: "))

number_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
teen_list = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
decades_list =["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"] 
'''used a dictionary to implement numbers to be written as words'''


if number <= 9:
    print(number_list[number].capitalize())
elif number >= 10 and number <= 19:
    tens = number % 10
    print(teen_list[tens].capitalize())
elif number > 19 and number <= 99:
    ones = math.floor(number/10)
    twos = ones - 2
    tens = number % 10
    if tens == 0:
        print(decades_list[twos].capitalize())
    elif tens != 0:
        print(decades_list[twos].capitalize() + " " + number_list[tens])