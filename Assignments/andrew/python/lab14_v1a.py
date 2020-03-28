import random


def pick6():

    return [random.randint(1, 99) for i in range(6)]



def calc_payout(winning, ticket):
 
    payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1

    if matches == 1:
        print(winning)
        print(ticket)
        print(f'Won ${payout[matches]}')
    
    if matches == 2:
        print(winning)
        print(ticket)
        print(f'Won ${payout[matches]}')
    
    if matches == 3:
        print(winning)
        print(ticket)
        print(f'Won ${payout[matches]}')

    if matches == 4:
        print(winning)
        print(ticket)
        print(f'Won ${payout[matches]}')

    if matches == 5:
        print(winning)
        print(ticket)
        print(f'Won ${payout[matches]}')

    if matches == 6:
        print(winning)
        print(ticket)
        print(f'Won ${payout[matches]}')

    return payout[matches]


def play_length():
    win = pick6()
    bal = 0

    for i in range(100):
        ticket = pick6()
        bal -= 2
        payout = calc_payout(win, ticket)
        bal += payout

    print('bal:', bal)
    return bal

def main():
    for i in range(100):
        play_length()
    print(f'complete')


main()