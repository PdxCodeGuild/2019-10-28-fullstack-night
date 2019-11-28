import colorsys
import math
from PIL import Image

img = Image.open("/Users/duncanweir/Desktop/pdx_code/full_stack_class/Opossum_2.jpg") # must be in same folder
width, height = img.size # x, y = z means that this will be a tup.le
                         # a.k.a. Tuple:
                         # A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
pixels = img.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y] # == itterable list

        # c = 0.299*r + 0.587*g + 0.114*b
        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        h = math.sin(x * s) / 10 #rotate the hue
        s += 0.5 #increase saturation
        v += 0.4 # increase value (brightness)

        r, g, b = colorsys.hsv_to_rgb(h/1, s/1, v/1)

        # convert back to [0, 255]
        # r = int(r*255)
        # g = int(g*255)
        # b = int(b*255)

        pixels[x, y] = (int(r*255), int(g*255), int(b*255))

img.show()
