import random

target = random.randint(1,10)

guess = ''

while True:
    guess = input('guess the number! ')
    guess = int(guess)
    if guess == target:
        print('that\'s correct!')
        break
    else:
        print('that\'s incorrect!')
