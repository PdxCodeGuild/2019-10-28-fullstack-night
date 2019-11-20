'''
lab25-number-to-phrase.py
Version3
Convert a number to roman numerals
'''
import time
print("Welcome to Number to Phrase v3.0\n\nWe've all been there: fallen through a time portal to the year 257 AD. You landed in a rich merchants caravan and were lucky enough to escape with your life and a pocketful of dinarii.  Now you're at an Ancient Roman food pod and you're just trying to say how many skewers of dormice in garum sauce you want but you don't know how to express it in the local numerals...")
time.sleep(1)
print("\nWell Worry No More!  With this handy converter, any number you wish can be converted into Roman Numerals!*")
time.sleep(1)
print("\n*number to be converted cannot exceed 1000")
time.sleep(1)
while True:
    n = int(input("\nPlease enter a number from 0 to 1000: "))
    if n not in range(0, 1001):
        print("Please enter a valid number: ")
        continue
    else:
        break

x = n // 100
y = n % 100 // 10
z = n % 10

x2a = {
    0: '',
    1: 'C',
    2: 'CC',
    3: 'CCC',
    4: 'CD',
    5: 'D',
    6: 'DC',
    7: 'DCC',
    8: 'DCCC',
    9: 'CM',
    10: 'M',
}

y2b = {
    0: '',
    1: 'X',
    2: 'XX',
    3: 'XXX',
    4: 'XL',
    5: 'L',
    6: 'LX',
    7: 'LXX',
    8: 'LXXX',
    9: 'XC'
}

z2c = {
    0: '',
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX'
}

a = x2a[x]
b = y2b[y]
c = z2c[z]

print("Converting")
time.sleep(0.1)
print("Converting.")
time.sleep(0.1)
print("Converting..")
time.sleep(0.1)
print("Converting...")
time.sleep(0.1)




rn = a + b + c
if n == 0:
    rn = 'ERROR!!!1!!!!1!!!'
print(f"\n{n} is {rn}.\n\nThanks for using Number to Phrase v3.0 and good luck on your journey back to the present.")