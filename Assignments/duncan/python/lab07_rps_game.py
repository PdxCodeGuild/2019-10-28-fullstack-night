
import random

rps = {
"rock" : ["paper", "scissors", "rock"],
"paper" : ["scissors", "rock", "paper"],
"scissors" : ["rock", "paper", "scissors"]
}

# wins
# rps[player[0]]

# all keys
options = list(rps.keys())

game_in_session = "yes"

print("\nWelcome to Rock, Paper, Scissors!")

while game_in_session == "yes":
    player = input("\nMake your selection; Rock, Paper, or Scissors: ").lower()

    computer = random.choice(list(rps.keys()))
    print(f"The computer has chosen: {computer}.\n")
    if computer == rps[player][0]:
        print("You lose.")
    elif computer == rps[player][1]:
        print("You win.")
    elif computer == rps[player][2]:
        print("You tied.")
    else:
        print("Error")

    game_in_session = input("\nDo you want to play another game? ").lower()
else:
    print("\nThank you for playing.")


'''
game_in_session = "yes"

print("\nWelcome to Rock, Paper, Scissors!")

while game_in_session == "yes":

    player = input("\nMake your selection: Rock, Paper, or Scissors: ")

    computer = random.choice(rps)

    print(f"The computer has chosen: {computer}")

    if player is rps[0] and computer is rps[2]:
        print("You have lost.")

    elif((player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper")):
        print("You have won.")

    elif player == computer:
        print("You have tied.")

    game_in_session = input("Do you want to play another game? ")
else:
    print("Thank you for playing.")
'''
