'''
lab12-guess_the_number-v2.py
Guess a random number between 1 and 10.
V2
Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the user has made, and tell them at the end.
'''
import random
x = random.randint(1, 10)

guess = int(input("Welcome to Guess the Number v2.  The computer is thinking of a number between 1 and 10.\nEnter your guess: "))
count = 0
while True:
    count = count + 1
    if guess == x:
        print(f"Congrats.  You guessed the computer's number and it only took you {count} times!")
        break
    else:
        guess = int(input("Try again, yo..."))