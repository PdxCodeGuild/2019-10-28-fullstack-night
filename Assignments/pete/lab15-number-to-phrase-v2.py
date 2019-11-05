'''
lab15-number-to-phrase-v2

Version2:
Handle numbers from 100-999
'''

print("Welcome to Number to Phrase v2.0.  We'll convert your number between 0-999 to easily readable letters.")

while True:
    n = int(input("Please enter an integer between 0 and 999: "))
    if n not in range(0, 1000):
        print("Please enter an acceptable number.")
        continue
    else:
        break

x = n // 100 #hundreds_digit
y = n % 100 // 10 #tens_digit
z = n % 10 #ones_digit
tn = n % 100 #teen exception finder
x2a = {# this is the dictionary to convert 100s to hundreds
    9: 'nine-hundred',
    8: 'eight-hundred',
    7: 'seven-hundred',
    6: 'six-hundred',
    5: 'five-hundred',
    4: 'four-hundred',
    3: 'three-hundred',
    2: 'two-hundred',
    1: 'one-hundred',
    0: '',
}

y2b = {# this is the dictionary to convert 10s to tens
    9: 'ninety-',
    8: 'eighty-',
    7: 'seventy-',
    6: 'sixty-',
    5: 'fifty-',
    4: 'forty-',
    3: 'thirty-',
    2: 'twenty-',
    1: 'ten',
    0: '',
}

z2c = {# this is the dictionary to convert 1s to ones
    9: 'nine',
    8: 'eight',
    7: 'seven',
    6: 'six',
    5: 'five',
    4: 'four',
    3: 'three',
    2: 'two',
    1: 'one',
    0: '',
}

a = x2a[x]
b = y2b[y]
if n % 10 == 0:#this if statement gets rid of unecessary hyphens
    b = b.strip('-')
c = z2c[z]

l = a + ' ' + b + c

if 20 > tn > 10:#this addresses the teen exceptions
    if tn == 19:
        bc = 'nineteen'
    if tn == 18:
        bc = 'eighteen'
    if tn == 17:
        bc = 'seventeen'
    if tn == 16:
        bc = 'sixteen'
    if tn == 15:
        bc = 'fifteen'
    if tn == 14:
        bc = 'fourteen'
    if tn == 13:
        bc = 'thirteen'
    if tn == 12:
        bc = 'twelve'
    if tn == 11:
        bc = 'eleven'
    l = a + ' ' + bc


print(f"{n} is {l}.")