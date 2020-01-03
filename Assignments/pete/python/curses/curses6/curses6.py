import curses
import time
import random
'''
Here I'm going to try to make background tiles.
'''

game_screen = curses.initscr()
game_screen.keypad(True)
# print(game_screen.getmaxyx())

'{00}'  '|><|'
'-__-'  '|==|'

# class Tile():
#     def __init__(self)
game_screen.clear()
for y in range(1, 33):
    for x in range(2, 58):
        if (y // 2) % 2 == 1 and (x // 4) % 4 == 1:
            game_screen.addstr(y + 2, x + 2, '-')
        else:
            game_screen.addstr(y + 2, x + 2, '|')

in_key = game_screen.getkey()
if in_key == 'q':
    curses.endwin()