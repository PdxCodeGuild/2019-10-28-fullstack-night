import random

computer_guess = random.randint(1, 10)

while True:
  guess = float(input("Guess a number between 1 and 10: "))
  if guess == computer_guess:
    print("You won!")
    break
  
  print("You guessed wrong")