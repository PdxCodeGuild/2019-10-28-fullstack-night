'''
By: Dustin DeShane
Filename: lab16.py
'''

from PIL import Image
img = Image.open("opossum_2.jpg") # must be in same folder
width, height = img.size
pixels = img.load()



for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        Y = int(0.299*r + 0.587*g + 0.114*b)
        r = Y
        g = Y
        b = Y


        pixels[i, j] = (r, g, b)

img.show()