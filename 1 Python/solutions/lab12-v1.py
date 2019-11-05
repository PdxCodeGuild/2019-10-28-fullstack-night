import random

computer_guess = random.randint(1, 10)
won = False
print(computer_guess)
for i in range(10):
  guess = float(input("Guess a number between 1-10: "))
  if guess == computer_guess:
    won = True
    break

  print(f"Guess again, you meat bag! You have {9 - i} tries left...")

if won:
  print("You won!")