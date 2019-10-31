'''
By: Dustin D.
Filename: lab1.py
'''

from turtle import *
import random

#draw a star
for i in range(0, 5):
    forward(100)
    right(144)
    color(random.choice(["red", "yellow", "green", "blue", "orange"])) #change line color
done()