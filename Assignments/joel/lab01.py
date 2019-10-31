'''
Lab: 06
Filename: lab01.py
Joel Weitzel
Objective: Draw something with Python turtle
'''

from turtle import *

'''
edge_length = 0
i = 0
while i < 100:
    forward(edge_length)
    right(144)
    edge_length += 4
    i += 1
done()
'''

fillcolor('blue')

n_sides = 8
edge_length = 0

i = 0
begin_fill()
while i < 150:
    forward(edge_length)
    right(360/n_sides)
    i = i + 1
    edge_length = edge_length + 1
end_fill()
done()
