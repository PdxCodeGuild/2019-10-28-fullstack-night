'''
Lab: LCR Simulator
https://github.com/PdxCodeGuild/2019-10-28-fullstack-night/blob/master/1%20Python/labs/optional-LCR.md
'''
import random

#this is the function for each player turn:
def player_roll(player_name, chips, player_L, player_R):
    die_sides = ["L", "C", "R", "*", "*", "*"]
    player_roll = []
    if chips[player_name] < 3:
        for die in range(chips[player_name]):
            player_roll.append(random.choice(die_sides))
    else:
        for roll in range(3):
            player_roll.append(random.choice(die_sides))
    print(f"{player_name} rolled {player_roll}.")
    for die in player_roll:
        if die in ['L', 'C', 'R']:
            chips[player_name] -= 1
            if die == 'L':
                chips[player_L] += 1
                print(f"{player_name} passed a chip to {player_L}.")
            elif die == 'C':
                chips['Center'] += 1
                print(f"{player_name} passed a chip to Center.")
            elif die == 'R':
                chips[player_R] += 1
                print(f"{player_name} passed a chip to {player_R}.")
    print(f"The chip count is:\n{chips}")
    return chips

#break function:
def break_out(chips, player1, player2, player3):
    if chips[player1] + chips['Center'] == 9 or chips[player1] + chips['Center'] == 9 or chips[player3] + chips['Center'] == 9:
        return True

# #turn counter function:  ##FUNCTION DIDN'T WORK
# def turn_counter(turns):
#     print(f"Turn {turns}:")
#     turns += 1
#     return turns

#we get the player names:
player1 = input("Enter Player One's name: ")
player2 = input("Enter Player Two's name: ")
player3 = input("Enter Player Three's name: ")

#we establish the starting chip count:
chips = {
    player1: 3,
    player2: 3,
    player3: 3,
    'Center': 0,
}

turns= 0
#this loop runs the whole game
while True:
    
    #player 1 turn:
    # turn_counter(turns)
    turns += 1
    print(f"\nTurn {turns}:")
    player_roll(player1, chips, player2, player3)
    if break_out(chips, player1, player2, player3) == True:
        break

    #player 2 turn:
    # turn_counter(turns)
    turns += 1
    print(f"\nTurn {turns}:")
    player_roll(player2, chips, player3, player1)
    if break_out(chips, player1, player2, player3) == True:
        break

    #player 3 turn:
    # turn_counter(turns)
    turns += 1
    print(f"\nTurn {turns}:")
    player_roll(player3, chips, player1, player2)
    if break_out(chips, player1, player2, player3) == True:
        break

print()
for player in chips:
    if chips[player] > 0:
        print(f"{player} won with {chips[player]} chip(s) left.  {player} takes the pot.  Congrats")
        break
print(f"\nAfter {turns} turns, here is the final chip count:\n{chips}")