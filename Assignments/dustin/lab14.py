'''
By: Dustin DeShane
Filename: lab14.py
'''
import random

def pick6():
    pick6_list = []
    for i in range(0, 6):
        number = random.randint(0, 99)
        pick6_list.append(number)
    return pick6_list

winner = pick6()
cost_total = 0
winnings_total = 0

for i in range(0, 100000):
    ticket = pick6()
    match = 0
    for x in range(0, 6):
        if ticket[x] == winner[x]:
            match += 1
    if match == 1:
        winnings = 4
    elif match == 2:
        winnings = 7
    elif match == 3:
        winnings = 100
        print("You hit the mini jackpot!")
        print(f"You bought {i} tickets.")
        print(ticket)
        break
    elif match == 4:
        winnings = 50000
    elif match == 5:
        winnings = 1000000
    elif match == 6:
        winnings = 25000000
        print("You hit the jackpot!")
        print(f"You bought {i} tickets.")
        print(ticket)
        break
    else:
        winnings = 0
    winnings_total = winnings_total + winnings
    cost_total += 2

print(f"The winning numbers were: {winner}")
print(f"You spent: ${cost_total}")
print(f"You won: ${winnings_total}")
#print(ticket)