import argparse
import curses
parser = argparse.ArgumentParser()
parser.add_argument('-lvl', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
LEVEL = parsed_args.version_arg or 1

'''
Above argparse and curses are imported and set up.
Below I will establish the Classes before getting into the different LEVELs.
'''

class Sprite():
    def __init__(self, y, x, uni):
        self.y = y
        self.x = x
        self.uni = uni
    def __str__(self):
        return self.uni

class Item(Sprite):
    def __init__(self, y, x, uni):
        super().__init__(y, x, uni)
    def __str__(self):
        pass#get back to this later

class Hero(Sprite):
    def __init__(self, y, x, uni):
        super().__init__(y, x, uni)
        self.inv = []
        self.health = 3
        pass#get back to this later

class Enemy(Sprite):
    def __init__(self, y, x, uni, health):
        super().__init__(y, x, uni)
        self.health = health
    def __str__(self):
        super().__str__(self)
    def move(self):
        pass
    def attack(self):
        pass