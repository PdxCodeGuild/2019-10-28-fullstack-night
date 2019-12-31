from random import randrange
class Ticket:
    def __init__(self):
        # self.ticket = []
        self.ticket = [randrange(100) for i in range(6)]
        # for i in range(6):
        #     self.ticket.append(randrange(0, 100))

    def __getitem__(self, key):
        return self.ticket[key]

    def __and__(self, other_ticket):
        # match_list = []
        # for i in range(6):
        #     if self[i] == other_ticket[i]:
        #         match_list.append(self[i])
        # return match_list
        return [self[i] for i in range(6) if self[i] == other_ticket[i]]

    def get_matches(self, bought_ticket):
        matches = 0
        for i in range(6):
            if self[i] == bought_ticket[i]:
                matches += 1
        return matches
    
    @staticmethod
    def winnings(matches):
        # match_win = {
        #     1: 4,
        #     2: 7,
        #     3: 100,
        #     4: 50000,
        #     5: 1000000,
        #     6: 25000000,
        # }
        match_win = [0, 4, 7, 100, 5000, 1000000, 25000000]
        return match_win[matches] - 2
        

winning_ticket = Ticket() # Ticket.__init__()
total_matches = 0
total_winnings = 0
for i in range(100000):
    bought_ticket = Ticket() # Ticket.__init__()
    # matches = winning_ticket.get_matches(bought_ticket)
    matches = len(winning_ticket & bought_ticket)
    total_matches += matches
    total_winnings += Ticket.winnings(matches)
print(total_matches)
print(total_winnings)