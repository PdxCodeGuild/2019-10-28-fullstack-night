import random
import string

quarter = 0
dime = 0
nickel = 0
penny = 0

'''
penny = int(input("How many pennies do you have?"))
if penny > 25:
    quarter = penny // 25
    penny = penny % 25
    if penny > 10:
        dime = penny // 10
        penny = penny % 10
        if penny > 5:
            nickel = penny // 5
            penny = penny % 5
else:
    print("Error")

print(f"You have {quarter} quarters, {dime} dimes, {nickel} nickels, and {penny} pennies.")
'''

penny = round(float(input("How much money do you have in dollars and cents? "))*100)
if penny > 25:
    quarter = penny // 25
    penny = penny % 25
    if penny > 10:
        dime = penny // 10
        penny = penny % 10
        if penny > 5:
            nickel = penny // 5
            penny = penny % 5
            # if penny >= 0.01:
            #     penny = penny, 4)
else:
    print("Error")

print(f"You have {quarter} quarters, {dime} dimes, {nickel} nickels, and {penny} pennies.")
