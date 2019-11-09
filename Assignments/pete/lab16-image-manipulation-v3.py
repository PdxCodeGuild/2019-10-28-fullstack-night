'''
lab16-image-manipulation-v3.py
Version 3:
Pillow can also be used to draw.  The code below demonstrates some funcions that Pillow provides.  Use these functions to draw a stick figure.  You can find more documentation here.
'''

from PIL import Image, ImageDraw

width = 1000
height = 1000

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((250, 485), (750, 515)), fill='blue') #arms
draw.rectangle(((400, 400), (600, 600)), fill="lightblue") #shirt
draw.rectangle(((450, 600), (475, height)), fill='tan')#pant
draw.rectangle(((525, 600), (550, height)), fill='tan')#pant

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128) # pink
draw.line((0, 0, width, height), fill=color)
draw.line((0, height, width, 0), fill=color)

circle_x = width / 2
circle_y = height / 4
circle_radius = 100
draw.ellipse((circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius, circle_y + circle_radius), fill="lightgreen")

img.show()