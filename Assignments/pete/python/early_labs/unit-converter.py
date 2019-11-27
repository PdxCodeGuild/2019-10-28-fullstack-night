'''
unit-converter.py
Make a program that converts distance units.
'''

#Ver1 Convert ft to m
ft = float(input("Welcome to Unit Converter Version 1.  Please enter a distance in feet to be converted to meters: "))
m = round((ft * 0.3048), 3)
print(f"\n{ft} ft is {m} m.")

#Ver2 Add units and allow user to convert from ft, mi, m, and km
unit = input("\nWelcomme to Unit Converter Version 2.  Please enter the unit (ft, mi, m, or km) that you'd like to convert to meters: ").lower()
while True:
    if unit == 'ft':
        conv = 0.3058
        break
    if unit == 'mi':
        conv = 1609.34
        break
    if unit == 'm':
        conv = 1
        break
    if unit == 'km':
        conv = 1000
        break
    else:
        unit = input("Please enter ft, mi, m, or km: ").lower()
    
dist1 = float(input(f"\nPlease enter the distance in {unit} you'd like to convert to m: "))
dist2 = round((dist1 * conv), 3)
print(f"\n{dist1} {unit} is  {dist2} m.")

#Ver3 Add yards and inches
unit = input("\nWelcome to Unit Converter Version 3.  You can do yards and inches now.  Please enter the unit (in, ft, yd, mi, m or km): ").lower()
joke = 'y'
while True:
    if unit == 'in':
        conv = 0.0254
        break
    if unit == 'ft':
        conv = 0.3058
        break
    if unit == 'yd':
        conv = 0.9144
        break
    if unit == 'mi':
        conv == 1609.34
        break
    if unit == 'm':
        joke = input("Do you really need a program to convert meters to meters? (Y/N): ").lower()
        if joke == 'y':
            conv = 1
        break
    if unit == 'km':
        conv = 1000
        break
    else:
        unit = input("Please enter in, ft, yd, mi, m, or km: ")
if joke == 'n':
    print("Didn't think so...")
else:
    dist1 = float(input(f"How many {unit} would you like to convert to m? "))
    dist2 = round((dist1 * conv), 3)
    print(f"\n{dist1} {unit} is {dist2} m.")

#Ver4 Allow user to choose both units
units = ['in', 'ft', 'yd', 'mi', 'm', 'km']
unit1 = input("\nWelcome to Unit Converter Version 4.  What unit would you like to convert FROM? (in, ft, yd, mi, m, km): ").lower()
while True:
    if unit1 in units:
        break
    else:
        unit1 = input("Please enter in, ft, yd, mi, m or km: ").lower()

dist1 = float(input(f"Please enter the value of {unit1} that you'd like to convert: "))
unit2 = input(f"What unit would you like to convert {dist1} {unit1} TO? (in, ft, yd, mi, m, km): ").lower()
while True:
    if unit2 in units:
        break
    else:
        unit1 = input("Please enter in, ft, yd, mi, m or km: ").lower()
#unit1
if unit1 == 'in':
    conv1 = 0.0254
if unit1 == 'ft':
    conv1 = 0.3058
if unit1 == 'yd':
    conv1 = 0.9144
if unit1 == 'mi':
    conv1 = 1609.34
if unit1 == 'm':
    conv1 = 1
if unit1 == 'km':
    conv1 = 1000
#unit2
if unit2 == 'in':
    conv2 = 1 / 0.0254
if unit2 == 'ft':
    conv2 = 1 / 0.3058
if unit2 == 'yd':
    conv2 = 1 / 0.9144
if unit2 == 'mi':
    conv2 = 1 / 1609.34
if unit2 == 'm':
    conv2 = 1 / 1 #teehee
if unit2 == 'km':
    conv2 = 1 / 1000

dist2 = round((dist1 * conv1 * conv2), 3)

print(f"\n{dist1} {unit1} is {dist2} {unit2}.\n\nThanks for using Unit Converter!")
