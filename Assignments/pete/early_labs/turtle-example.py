'''
turtle-example.py
'''

userinput = input("User input (Y/N)? ").lower()
if userinput == 'y':
    rplus = float(input("Input r: "))
    fplus = float(input("Input f: "))
    # feedback_r = copy(rplus) #doesn't work
    # feedback_f = copy(fplus) #figure out copy
feedback = input("Feedback (Y/N)? ").lower()

from turtle import *
fastmode = input("Fast mode (Y/N)? ").lower()
if fastmode == 'y':
    speed('fastest')
bgcolor('black')
import random
f = 0
r = 0
color_pool = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
first_run = True
count = 0
# left(22) #for spiral fractal thing
while True:
    # bgcolor(random.choice(color_pool))
    color(random.choice(color_pool))
    forward(f)
    if r <= 180:
        right(r)
    if r > 180:
        left(360 - r)
    if userinput == 'n':
        if first_run == True:
            penup()
            setposition(-10,100)
            pendown()
            first_run = False
        #Ver1
        # r = r + 1
        # f = f + 1
        #Ver2 Solar Flare pos(-10,55)
        r = r + 0.5
        f = f + 1
        #Ver3
        # r = r + 0.1
        # f = f + 0.1
        #Ver4
        # r = r + 0.01
        # f = f + 0.01
        # Ver4 Spiral/Fractal pos(0,0)
        # r = r + 1
        # f = f + 0.01
        #Ver5 pos(-10,250)
        # r = r + 0.5
        # f = f + 3
        #Ver6 pos(-10,200)
        # r = r + 0.5
        # f = f + 2
        # Ver7 pos(0,0) Cool Spiral
        # r = r - 0.25
        # f = f = 0.05
        # Ver8
        # if first_run == True:
        #     r = .01
        #     f = .01
        #     first_run = False
        # r = r + (r * 0.1)
        # f = f + (f * 0.01)
    if userinput == 'y':
        r = r + rplus
        f = f + fplus
        # print(f"input r = {feedback_r}  input f = {feedback_f}") #figure out copy
    r = r % 360
    count = count + 1
    if feedback == 'y':
        print(f"Count {count}")
        print(f"r is {r}")
        print(f"f is {f}")
