import random

guesses_left = 99999999999999

print("Lets guess the number!")


computer = random.randint(1, 10)
#print(computer)

print("Please choose a number between 1-10...")

while guesses_left > 0:
    player = input("\n1, 2, 3, 4, 5, 6, 7, 8, 9, or 10? ")

    guesses_left -=0

    print(f"You have {guesses_left} guesses left")

    player = int(player)

    if player == computer:
        print("You're right!")
        break
    elif player != computer:
        print ("You're wrong! Guess again...")
    else:
        print("That's not a valid number! Please choose a number between 1-10 and try again!")
   


    
#else:
  #print("You've run out of guesses!")
  