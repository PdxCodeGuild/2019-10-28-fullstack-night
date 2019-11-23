import random

computer = random.randint(1,9)
pick_a_number = 0
numbers_remaining = 10
count = 0
first_run = True

while True:
    pick_a_number = input('guess the number, you have 10 tries')
    pick_a_number = int(pick_a_number)
    count += 1
    numbers_remaining = numbers_remaining - 1
    if pick_a_number == computer:
        print('correct')
        print('you took', count, 'tries')
        break
    else:
        print('wrong')
    if pick_a_number > computer:
        print('too low!')
        break
    else:
        print('too high!')
    if numbers_remaining == 0:
        print('out of tries')
        break
    else:
        print('try again')
    if first_run == True:
        print(f"you guessed {pick_a_number}")
        old_guess = pick_a_number
        first_run = False
    else:
        print(f"you guessed {old_guess} and then {pick_a_number}")
        old_guess = pick_a_number


print("Great Job, the number was", computer)
