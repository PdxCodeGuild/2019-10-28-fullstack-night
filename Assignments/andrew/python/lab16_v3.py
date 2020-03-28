import PIL


from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((275, 150), (200, 400)), fill="white")

circle_x = width/2
circle_y = height/2
circle_radius = 40
draw.ellipse((175, 0, 300, 200), fill='lightgreen')
color = (256, 128, 128)  # pink
draw.line((20, 200, 200, 250), fill=color)
draw.line((480, 190, 280, 250), fill=color)

img.show()