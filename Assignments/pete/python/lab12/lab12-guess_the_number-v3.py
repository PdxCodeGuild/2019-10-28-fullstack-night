'''
lab12-guess_the_number-v3.py
Guess a random number between 1 and 10.
V3
Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.'''
import random
x = random.randint(1, 10)

guess = int(input("Welcome to Guess the Number v3.  The computer is thinking of a number between 1 and 10.\nEnter your guess: "))
count = 0
while True:
    count = count + 1
    if guess == x:
        print(f"Congrats.  You guessed the computer's number and it only took you {count} times!")
        break
    else:
        if guess > x:
            guess = int(input("Too high...  Try again: "))
        if guess < x:
            guess = int(input("Too low...  Try again: "))
