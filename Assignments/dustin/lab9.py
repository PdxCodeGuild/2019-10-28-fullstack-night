'''
By: Dustin DeShane
Filename: lab9.py
'''


''' Version 1

feet = int(input("How many feet?: "))
yards = round((feet * .3048), 5)

print(f"That's {yards} yards!")
'''

#  Version 2 / 3

# User numerical and unit input
print("Let's convert distances to meters!")
distance = float(input("Please enter a number: "))
units = input("Please enter a unit(ft, mi, m, km, yd, in): ")

# 
if units == "ft":
    meters = round((distance*.3048), 5)
    print(f"That's {meters} meters!")
elif units == "mi":
    meters = round((distance*1609.34), 5)
    print(f"That's {meters} meters!")
elif units == "yd":
    meters = round((distance*0.9144), 5)
    print(f"That's {meters} meters!")
elif units == "in":
    meters = round((distance*0.0254), 5)
    print(f"That's {meters} meters!")
elif units == "m":
    meters = distance
    print(f"That's {meters} meters!")
elif units == "km":
    meters = distance * 1000
    print(f"That's {meters} meters!")
else:
    print("That wasn't one of the options. Please rerun the program.")