import random

def generate_ticket():
  ticket = []
  for _ in range(6):
    r = random.randint(0, 99)
    ticket.append(r)
  return ticket

def number_of_matches(ticket, winning_ticket):
  matches = 0

  if ticket[0] == winning_ticket[0]:
    matches += 1
  if ticket[1] == winning_ticket[1]:
    matches += 1
  if ticket[2] == winning_ticket[2]:
    matches += 1
  if ticket[3] == winning_ticket[3]:
    matches += 1
  if ticket[4] == winning_ticket[4]:
    matches += 1
  if ticket[5] == winning_ticket[5]:
    matches += 1

  return matches

def calculate_earnings(matches):
  if matches == 1:
    return 4
  elif matches == 2:
    return 7
  elif matches == 3:
    return 100
  elif matches == 4:
    return 50000
  elif matches == 5:
    return 1000000
  elif matches == 6:
    return 25000000


winning_ticket = generate_ticket()

spent = 0
earnings = 0

for _ in range(1000000):
  ticket = generate_ticket()
  spent += 2

  matches = number_of_matches(ticket, winning_ticket)
  if matches > 0:
    earnings += calculate_earnings(matches)


print(f"Your balance is ${earnings - spent}")
print(f"Your ROI is ${(earnings - spent) / spent}")