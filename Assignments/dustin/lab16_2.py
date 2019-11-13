'''
By: Dustin DeShane
Filename: lab16_2.py
'''
import random
import colorsys
from PIL import Image


img = Image.open("opossum_2.jpg") # must be in same folder
width, height = img.size
pixels = img.load()



for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # Y = int(0.299*r + 0.587*g + 0.114*b)
        # r = Y
        # g = Y
        # b = Y
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        h = h + .7
        s = s - .2
        v = v + .1
        # do some math on h, s, v

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)

# colorsys uses colors in the range [0, 1]


img.show()