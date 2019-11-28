import random
import string

computer = random.randint(1,11)
player = ""
guess = 1

while guess < 11:
    player = int(input("What number did the computer guess?"))
    if player > computer:
        print("The number you guessed is too high.")
        guess += 1
    elif player < computer:
        print("The number you guessed is too low.")
        guess += 1
    elif player == computer:
        print(f"Correct, the computer selected {computer}. You guessed the correct number after {guess} attempts!")
        break
else:
    print("You have guessed incorrectly 10 times. You lose.")
