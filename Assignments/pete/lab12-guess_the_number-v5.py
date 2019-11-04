'''
lab12-guess_the_number-v5.py
V5
Swap the user with the computer: the user will pick a number, and the computer will make random guesses until they get it right.
'''
import random
import time
user_num = int(input("Welcome to Guess the Number v5.\nIn this program, computer guess you!\nPlease enter a number between 1 and 10: "))
while True:
    if user_num not in list(range(1, 11)):
        user_num = int(input(f"No cheating computer now.  {user_num} is not a number between 1 and 10.  Please enter a new number: "))
    else:
        break
guesses = []
count = 0
while True:
    time.sleep(1)
    guess = random.randint(1, 10)
    if guess == user_num:
        print(f"Computer guessed your number {user_num}.\n")
        time.sleep(1)
        while True:
            print("CONGRATULATION: COMPUTER GUESS YOU!" * count)
            count = count + 1
            time.sleep(.25)
    else:
        if guess in guesses:
            print(f"Computer guess {guess} again.  Computer can never be too sure.")
        else:
            print(f"Computer guessed {guess}.  Computer wrong.  Computer try again.")
        guesses.append(guess)
