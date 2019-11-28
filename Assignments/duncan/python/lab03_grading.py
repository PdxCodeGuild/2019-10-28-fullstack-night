'''
A = range(90, 100)
B = range(80, 89)
C = range(70, 79)
D = range(60, 69)
F = range(0, 59)
'''

import random

print("Welcome to the Grading Program!")

user_grade = int(input("What is your numerical score?"))

# set up +/-
if user_grade % 10 in range(1,6):
    sign = "-"
elif user_grade % 10 in range(6,11):
    sign = "+"

# 90 <= grade <= 100:
# if user_grade in range(min, max)

if user_grade in range(90, 101):
    print(f"You received the grade A{sign}")
elif 80 <= user_grade <= 89:
    print(f"You received the grade: B{sign}")
elif user_grade in range(70, 80):
    print(f"You received the grade: C{sign}")
elif user_grade in range(60, 70):
    print(f"You received the grade: D{sign}")
else:
    print(f"You received the grade: F{sign}")

rival = random.randint(1,100)

print(f"Your rival's score is {rival}.")

if rival > user_grade:
    print("Your rival is better than you.")
elif rival < user_grade:
    print("You are better than your rival")
else:
    print("You have tied with your rival. That's the worst.")
