'''
By: Dustin DeShane 
Filename: lab16_3.py
'''
from PIL import Image, ImageDraw

width = 800
height = 800

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
#draw.rectangle(((100, 100), (300, 300)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink

circle_x = width/2
circle_y = height/4
circle_radius = 100
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')
color = (256, 128, 128)  # pink
draw.line((400, 300, 400, 650), fill=color)
draw.line((200, 380, 600, 380), fill=color)
draw.line((400, 650, 200, 780), fill=color)
draw.line((400, 650, 600, 780), fill=color)


img.show()