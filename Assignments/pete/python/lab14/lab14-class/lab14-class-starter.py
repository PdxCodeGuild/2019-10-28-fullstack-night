from random import randrange
class Ticket:
    pass
winning_ticket = Ticket() # Ticket.__init__()
total_matches = 0
total_winnings = 0
for i in range(100000):
    bought_ticket = Ticket() # Ticket.__init__()
    matches = len(winning_ticket.get_matches(bought_ticket))
    total_matches += matches
    total_winnings += Ticket.winnings(matches)
print(total_matches)
print(total_winnings)