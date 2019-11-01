'''
By: Dustin D
Filename: lab2.py
'''

import random

#user input
part = input("Please enter a car part: ")
vehicle = input("Please enter a type of vehicle: ")
sound = input("Please input a sound you might hear: ")
landscape = input("Please enter a type of landscape: ")

#program output
print(f"The {part} on the {vehicle} goes {sound} {sound} {sound}. {sound.upper()} {sound.upper()} {sound.upper()}. The {part} on the {vehicle} goes {sound} {sound} {sound} all through the {landscape}.")

#create and build list using user input
adjectives = []
adjective1 = adjectives.append(input("Please enter an adjective: "))
adjective2 = adjectives.append(input("Please enter another adjective: "))
animal = input("Please enter an animal: ")

#program output using random items from input list
print(f"The {random.choice(adjectives)} {random.choice(adjectives)} {animal} jumped over the lazy dog.")