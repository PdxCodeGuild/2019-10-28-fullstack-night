'''
lab19-blackjack-advice-v1.py
Version1

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

    *Less than 17, advise to "Hit"

    *Greater than or equal to 17, but less than 21, advise to "Stay"

    *Exactly 21, advise "Blackjack!"

    *Over 21, advise "Already Busted"

Print out the current total point value and the advice.
'''

#make a dictionary to retrieve point values of cards
blackjack_dict = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

first = input("What's your first card? ").upper()
second = input("What's your second card? ").upper()
third = input("What's your third card? ").upper()

def point_adder(card1, card2, card3):
    total_points = blackjack_dict[card1] + blackjack_dict[card2] + blackjack_dict[card3]
    return total_points


def advisor(total_points):
    if total_points < 17:
        advice = 'Hit'
    elif total_points < 22:
        advice = 'Stay'
    elif total_points == 21:
        advice = 'Blackjack!'
    else:
        advice = 'Already Busted'
    return advice

total_points = point_adder(first, second, third)
advice = advisor(total_points)
print(f"Points: {total_points}   Advice: {advice}")