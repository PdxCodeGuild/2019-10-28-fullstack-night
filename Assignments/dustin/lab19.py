'''
By: Dustin DeShane
Filename: lab19.py
'''
import random

cards = {
        'A':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'J':10,
        'Q':10,
        'K':10,
        }
card_choices = list(cards.keys())

card_1 = random.choice(card_choices)
card_2 = random.choice(card_choices)
card_3 = random.choice(card_choices)

print(f"What's your first card?: {card_1}")
print(f"What's your second card?: {card_2}")
print(f"What's your third card?: {card_3}")

total = cards[card_1] + cards[card_2] + cards[card_3]

if total < 17:
    print(f"{total} Hit.")
elif total >= 17 and total < 21:
    print(f"{total} Stay.")
elif total == 21:
    print(f"{total} Blackjack!")
else:
    print(f"{total} Bust!")
