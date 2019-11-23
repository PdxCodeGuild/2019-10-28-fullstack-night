import random
pick_a_number = input("Pick a number")
computer = random.randint(1,9)
pick_a_number = 0

while True:
    pick_a_number = input('guess the number, you have 10 tries')
    pick_a_number = int(pick_a_number)
    if pick_a_number == computer:
        print('correct')
        print('you took', count, 'tries')
        break
    else:
        print('wrong')
    if numbers_remaining == 0:
        print('out of tries')
        break
    else:
        print('try again')
