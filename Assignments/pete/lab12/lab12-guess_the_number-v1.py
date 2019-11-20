'''
lab12-guess_the_number-v1.py
Guess a random number between 1 and 10.
V1 using a while loop, user gets 10 guesses.
'''
import random
x = random.randint(1, 10)

guess = int(input("Welcome to Guess the Number v1.  The computer is thinking of a number between 1 and 10.\nEnter your guess: "))
count = 0
while count < 10:
    count = count + 1
    if guess == x:
        print(f"Congrats.  You guessed the computer's number and it only took you {count} times!")
        quit()
    else:
        guess = int(input("Try again, yo..."))
print("You had 10 guesses but you couldn't do it...")