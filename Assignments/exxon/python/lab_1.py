from turtle import *

color("purple")
circle(50)

right(90)
color("green")
forward(50)
right(90)
color("yellow")
forward(25)
backward(50)
color("orange")
forward(25)
left(90)
color("red")
forward(50)

left(45)
color("pink")
forward(30)
backward(30)
right(90)
color("brown")
forward(30)

# right eye
penup()
goto(10,60)
pendown()
circle(10)
penup()

# left eye
goto(-25,60)
pendown()
circle(10)
penup()

# smile
goto(-30,30)
pendown()
left(90)
circle(90,30)
left(90)
forward(10)
left(90)
forward(42)
penup()

goto(100,100)



done()