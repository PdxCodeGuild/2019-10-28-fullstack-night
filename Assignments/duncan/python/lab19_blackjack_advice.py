card_value = {
"a": 1,
"2": 2,
"3": 3,
"4": 4,
"5": 5,
"6": 6,
"7": 7,
"8": 8,
"9": 9,
"10": 10,
"j": 10,
"q": 10,
"k": 10,
}

game_in_session = "yes"

while game_in_session == "yes":
# def blackjack_hand(card1, card2, card3):
    card1 = input("What is your first card? ").lower()
    card1a = card_value[card1]

    card2 = input("What is your second card? ").lower()
    card2a = card_value[card2]

    card3 = input("What is your third card? ").lower()
    card3a = card_value[card3]

    if card1a + card2a + card3a < 17:
        print(f"{(card1a + card2a + card3a)} - Hit")
        game_in_session = input("Do you want to check another hand? ").lower()

    elif 17 < card1a + card2a + card3a < 21:
        print(f"{(card1a + card2a + card3a)} - Stay")
        game_in_session = input("Do you want to check another hand? ").lower()

    elif card1a + card2a + card3a == 21:
        print(f"{(card1a + card2a + card3a)} - Blackjack!")
        game_in_session = input("Do you want to check another hand? ").lower()

    elif card1a + card2a + card3a > 21:
        print(f"{(card1a + card2a + card3a)} - Already Busted")
        game_in_session = input("Do you want to check another hand? ").lower()

else:
    print("Goodbye.")

# blackjack_hand("a", "q", "k")
