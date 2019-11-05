'''
lab14-pick6-v1.py
v1
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).
'''
#1.Generate a list of 6 random numbers representing the winning tickets...so define a pick6() function here.
import random
def pick6():
    ticket = []
    count = 0
    while count != 6:
        ticket.append(random.randint(1, 100))
        count = count + 1
    return ticket #I HAD to do this to make ANYTHING work
winning_ticket = pick6()
print(winning_ticket)
#2. Start your balance at 0.
balance = 0
#3. Loop 100,000 times, for each loop:
count = 0
while count != 100000:
#4. Generate a list of 6 random numbers representing the ticket
    ticket = pick6()
#5. Subtract 2 from your balance (you bought a ticket)
    balance = balance - 2
#6. Find how many numbers match
    match = 0
    if ticket[0] == winning_ticket[0]:
        match = match + 1
    if ticket[1] == winning_ticket[1]:
        match = match + 1
    if ticket[2] == winning_ticket[2]:
        match = match + 1
    if ticket[3] == winning_ticket[3]:
        match = match + 1
    if ticket[4] == winning_ticket[4]:
        match = match + 1
    if ticket[5] == winning_ticket[5]:
        match = match + 1
#7. Add to your balance the winnings from your matches
    if match == 1:
        balance = balance + 4
    if match == 2:
        balance = balance + 7
    if match == 3:
        balance = balance + 100
    if match == 4:
        balance = balance + 50000
    if match == 5:
        balance = balance + 1000000
    if match == 6:
        balance = balance + 25000000
    count = count + 1
#8. After the loop, print the final balance
print(f"${balance}")