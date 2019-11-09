'''
lab16-image-manipulation-v1.py
Version2:

Use the colorsys library to increase the saturation, decrease the brightness, and rotate the hue.  Colorsys represents colors as floats in the range 0.0 - 1.0, whereas pillow uses ints in the range 0-255.  You'll have to convert between these two representations.
'''

from PIL import Image
img = Image.open("lenna.png") #must be in same folder
width, height = img.size
pixels = img.load()

import colorsys #v2 import this to play with colors

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        #colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        #do some math on h, s, v
        #yo this is the part where I did the assignment right
        if h != 0:
            h = 1 / h
        else:
            h = 1
        # if h > 0.5:
        #     h /= 2
        # if h < 0.5:
        #     h *= 2
        # s = 0.5
        # v = 0.5

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

#This is where I was doing stuff in the wrong place
        #negative
        # r %= 0.5
        # g %= 0.5
        # b %= 0.5

        # super dark negative
        # r %= 0.1
        # g %= 0.1
        # b %= 0.1



        #convert back to [0, 255]
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
       

        pixels[i, j] = (r, g, b)

img.show()