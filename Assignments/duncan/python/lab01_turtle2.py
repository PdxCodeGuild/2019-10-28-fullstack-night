from turtle import *

## drawing a square ##

# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(50)

## drawing a square with a 'for' loop ##

# i = 0
# while i < 4:
#     forward(100)
#     left(90)
#     i += 1

## drawing a staircase ##

# i = 0
# while i < 6:
#     forward(100)
#     left(90)
#     forward(100)
#     right(90)
#     i += 1

## filling a square ##

# fillcolor('red')
# begin_fill()
#
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
#
# end_fill()

## draw an n-sided figure ##

edge_length = 100
n_sides = 100

i = 0
while i < n_sides:
    forward(edge_length/n_sides)
    right(360/n_sides)
    i += 1

right(90)
penup()
forward(32)
pendown()
forward(10)
right(90)
forward(100)
right(180)
forward(200)
right(180)
forward(100)
left(90)
forward(100)
right(90)
forward(20)
left(90)
forward(100)
left(90)
penup()
forward(40)
pendown()
left(90)
forward(100)
left(90)
forward(20)





done()
