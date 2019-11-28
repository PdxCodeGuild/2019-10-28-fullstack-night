
### INSTRUCTOR SOLUTION

# DRY == Dont Repeat Yourself
# If you see code repeated a lot you need a function
import random

def generate_ticket():
    ticket = []
    for _ in range(6): #propogates a list 6 times
        r = random.randint(0, 99)
        ticket.append(r)
    return ticket # saves the variable ticket outside this function

winning_ticket = generate_ticket()

spent = 0
earnings = 0

for _ in range(100000):
    matches = 0
    ticket = generate_ticket()
    spent -= 2

    if ticket[0] == winning_ticket[0]:
        matches +=1
    if ticket[1] == winning_ticket[1]:
        matches +=1
    if ticket[2] == winning_ticket[2]:
        matches +=1
    if ticket[3] == winning_ticket[3]:
        matches +=1
    if ticket[4] == winning_ticket[4]:
        matches +=1
    if ticket[5] == winning_ticket[5]:
        matches +=1

    if matches == 1:
        earnings += 4
    elif matches == 2:
        earnings += 7
    elif matches == 3:
        earnings += 100
    elif matches == 4:
        earnings += 50000
    elif matches == 5:
        earnings += 1000000
    elif matches == 6:
        earnings += 25000000

print(f"Your balance is ${spent + earnings}.")
