import argparse
import curses
parser = argparse.ArgumentParser()
parser.add_argument('-lvl', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
LEVEL = parsed_args.version_arg or 1
import numpy
'''
Above argparse and curses are imported and set up.#and numpy
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

class Character(Sprite):
    def __init__(self, y, x, uni):
        super().__init__(y, x, uni)

    def __str__(self):
        return self.uni
    
    def move(self, direction, steps):
        # change the y/x position of the character
        pass

    def attack(self, direction, weapon):
        #attack and everything
        pass

hero = Character(10, 15, '😶')

enemies = [
    Character(7, 7, '👿'),
    Character(7, 23, '😈'),
    Character(13, 7, '😈'),
    Character(13, 23, '👿'),
]

moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

game_screen = curses.initscr()
game_screen.keypad(True)
game_screen.clear()

[game_screen.addstr(enemy.y, enemy.x, str(enemy)) for enemy in enemies]
game_screen.addstr(hero.y, hero.x, str(hero))
for enemy in enemies:
    game_screen.addstr(enemy.y, enemy.x, str(enemy))
print(game_screen.getmaxyx())
while True:
    in_key = game_screen.getkey()
    if in_key == 'q':
        curses.endwin()
        break

    if in_key in ['KEY_UP', 'KEY_DOWN', 'KEY_RIGHT', 'KEY_LEFT']:






