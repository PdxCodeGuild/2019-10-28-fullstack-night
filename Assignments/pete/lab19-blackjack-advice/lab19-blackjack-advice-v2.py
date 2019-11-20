'''
lab19-blackjack-advice-v2.py

Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.
'''
import random
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

def rand_hand():
    cards = list(blackjack_dict.keys())
    hand = []
    for i in range(3):
        hand.append(random.choice(cards))
    card1, card2, card3 = hand
    return card1, card2, card3
print(rand_hand())