a
total = []

def face_value(card):
    if card == 'a':
        return 1
    elif card == 'j' or card == 'k' or card =='q':
        return 10
    return int(card)


def main():
    card_1 = input("input first card")
    card_2 = input("input second card")
    card_3 = input("input third card")
    total = face_value(card_1) + face_value(card_2) +face_value(card_3)
    if card_1 == 'a' and total <= 11:
        total += 10
    elif card_2 == 'a' and total <= 11:
        total += 10
    elif card_3 == 'a' and total <= 11:
        total += 10
    elif total < 17:
        print('hit')
    elif total < 21:
        print('stay')
    elif total == 21:
        print('winner winner chicken dinner')
    else:
        print('bust')
main()
