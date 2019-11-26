
#y = (0.299*r + 0.587*g + 0.114*b)


from PIL import Image
img = Image.open("Jackson_Kelly.jpg") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        #r = 2
        #g = 2
        #b = 2

        # your code here

        y = int(0.299*r + 0.587*g + 0.114*b)

        pixels[i, j] = (y, y, y)




img.show()
