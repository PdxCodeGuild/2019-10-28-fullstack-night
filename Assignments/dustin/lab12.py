'''
By: Dustin DeShane
Filename: lab12.py
'''

import random

counter = 0
number = random.randint(0, 10)
guessdistance = 10
#print(number)  || Troubleshooting purposes

while counter < 10:
    guess = int(input("Please enter a number between 1 and 10: "))
    while guess not in range(0, 11):
        guess = int(input("Please enter a number between 1 and 10: "))
    if guess == number:
        print("You got it!")
        break
    if counter < 1:
        guessdistance = abs(guess-number)
        print("Nope! Try again!")
    elif counter >= 1:
        newdistance = abs(guess-number)
        if guessdistance < newdistance:
            print("Getting colder!")
            guessdistance = newdistance

        elif guessdistance > newdistance:
            print("Getting warmer!")
            guessdistance = newdistance

        elif guessdistance == newdistance:
            print("Just as far!")
    else:
        print("Nope!")
    counter = counter + 1
    timesleft = 10 - counter
    timesleftstr = str(timesleft)
    print(f"You have {timesleftstr} attempts left!")

if counter == 10:
    print("The number was: " + str(number))
    print("You lost!")
