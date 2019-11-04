'''
lab12-guess_the_number-v4.py
Guess a random number between 1 and 10.
V4
Tell the user whether their current guess is closer than their last. This can be done by maintaining a variable containing the last guess outside the loop, then comparing the last guess to the current guess, and check if it's closer. Hint: you're interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).
'''
import random
x = random.randint(1, 10)

print("Welcome to Guess the Number v4.  The computer is thinking of a number between 1 and 10.\n")
count = 0
first_run = True
while True:
    count = count + 1
    guess = int(input("Enter your guess: "))
    if first_run == True:
        if guess == x:
            print(f"Congrats.  You guessed the computer's number {x} on the first try!")
            break
        first_run = False
        old_guess = guess
        print("Wrong, but try again.")
        continue
    old_close = abs(old_guess - x)
    new_close = abs(guess - x)
    if guess == x:
        print(f"Congrats.  You guessed the computer's number and it only took you {count} times!")
        break
    elif old_close > new_close:
        print("Wrong.  But you're getting warmer.")
    elif new_close > old_close:
        print("Wrong.  And you're getting colder.  Ugh, I'm dissapointed in you..")
    else:
        print("You're neither warmer nor colder... huh...")
    old_guess = guess