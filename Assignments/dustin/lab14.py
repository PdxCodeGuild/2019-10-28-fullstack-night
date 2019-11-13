'''
By: Dustin DeShane
Filename: lab14.py
'''
import random

#generate random numbers for winning ticket and iterated tickets
def pick6():
    pick6_list = []
    for i in range(0, 6):
        number = random.randint(0, 99)
        pick6_list.append(number)
    return pick6_list

#winning ticket numbers
winner = pick6()
cost_total = 0
winnings_total = 0
one_match = 0
two_match = 0
three_match = 0
four_match = 0
five_match = 0
six_match = 0

for i in range(0, 100000):
    ticket = pick6()
    match = 0
    # calculate number of matching numbers on each ticket
    for x in range(0, 6):
        if ticket[x] == winner[x]:
            match += 1
    #calculate earnings per ticket
    if match == 1:
        winnings = 4
        one_match += 1
    elif match == 2:
        winnings = 7
        two_match += 1
    elif match == 3:
        winnings = 100
        three_match += 1
        #print("You hit the mini jackpot!")
        #print(f"You bought {i} tickets.")
        #print(ticket)
        #break
    elif match == 4:
        winnings = 50000
        four_match += 1
    elif match == 5:
        winnings = 1000000
        five_match += 1
    elif match == 6:
        winnings = 25000000
        six_match += 1
        print("You hit the jackpot!")
        print(f"You bought {i} tickets.")
        print(ticket)
        break
    else:
        winnings = 0
    winnings_total = winnings_total + winnings
    #calculate total cost of tickets bought
    cost_total += 2
print(f"Matches(1-6 respectively): {one_match}, {two_match}, {three_match}, {four_match}, {five_match}, {six_match}")
print(f"The winning numbers were: {winner}")
print(f"You spent: ${cost_total}")
print(f"You won: ${winnings_total}")
#print(ticket)