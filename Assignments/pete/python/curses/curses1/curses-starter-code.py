import argparse
import curses
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
VERSION = parsed_args.version_arg or 1
'''
'''
if VERSION == 1:
    # Let's paint our terminal with curses!
    my_screen = curses.initscr()  # create the curses screen
    my_screen.keypad(True)  # enable the keypad
    my_screen.clear()  # clear the screen
    my_screen.addstr(1, 5, ':)')  # add a smiley face at 1 down, 5 right
    my_screen.addstr(5, 1, '&:O->-<')  # add a surprised face at 5 down, 1 right
    my_screen.getkey()  # let the user enter a key
    curses.endwin()  # close curses
elif VERSION == 2:
    # Lets create a player, and then use that info
    # The player will basically just hold info to put into the addstr method
    class Player:
        def __init__(self, y, x, uni):
            self.y = y  # how far down
            self.x = x  # how far right
            self.uni = uni  # what you look like
        def __str__(self):  # this will be used when we convert to a string
            return self.uni
    my_screen = curses.initscr()
    my_screen.keypad(True)
    my_screen.clear()
    hero = Player(1, 5, ':)')
    my_screen.addstr(hero.y, hero.x, str(hero))
    villain = Player(5, 1, ':O')
    my_screen.addstr(villain.y, villain.x, str(villain))
    my_screen.getkey()
    curses.endwin()
elif VERSION == 3:
    # Lets create a hero, and let them move up!
    class Player:
        def __init__(self, y, x, uni):
            self.y = y
            self.x = x
            self.uni = uni
        def __str__(self):
            return self.uni
    hero = Player(5, 5, '(~˘▾˘)~')  # make a hero at 5, 5
    my_screen = curses.initscr()
    my_screen.keypad(True)
    my_screen.clear()
    my_screen.addstr(hero.y, hero.x, str(hero))
    while True:
        in_key = my_screen.getkey()  # This time we are capturing the key
        if in_key == 'q':  # If they type q, we want to quit
            curses.endwin()
            break
        elif in_key == 'KEY_UP':  # If they push up, we want to move up
            hero.y -= 1
        my_screen.addstr(hero.y, hero.x, str(hero))
elif VERSION == 4:
    # Let's clear the screen when we move!
    class Player:
        def __init__(self, y, x, uni):
            self.y = y
            self.x = x
            self.uni = uni
        def __str__(self):
            return self.uni
    hero = Player(5, 5, '(~˘▾˘)~')
    my_screen = curses.initscr()
    my_screen.keypad(True)
    my_screen.clear()
    my_screen.addstr(hero.y, hero.x, str(hero))
    while True:
        in_key = my_screen.getkey()
        if in_key == 'q':
            curses.endwin()
            break
        elif in_key == 'KEY_UP':
            hero.y -= 1  # How far up can we move?
        my_screen.clear()  # Added clear
        my_screen.addstr(hero.y, hero.x, str(hero))
elif VERSION == 5:
    #  Let's make sure we can't move up too far
    class Player:
        def __init__(self, y, x, uni):
            self.y = y
            self.x = x
            self.uni = uni
        def __str__(self):
            return self.uni
    hero = Player(5, 5, '(~˘▾˘)~')
    my_screen = curses.initscr()
    my_screen.keypad(True)
    my_screen.clear()
    my_screen.addstr(hero.y, hero.x, str(hero))
    while True:
        in_key = my_screen.getkey()
        if in_key == 'q':
            curses.endwin()
            break
        elif in_key == 'KEY_UP':
            if hero.y - 1 >= 0:  # If we can't move up more
                hero.y -= 1
        my_screen.clear()
        my_screen.addstr(hero.y, hero.x, str(hero))
elif VERSION == 6:
    #  Let's let the player pick up a sword
    class Item:
        def __init__(self, y, x, uni):
            self.y = y
            self.x = x
            self.uni = uni
        def __str__(self):
            return self.uni
    class Player(Item):
        def __init__(self, y, x, uni):
            super().__init__(y, x, uni)
            self.inv = []  # added inventory
        def __str__(self):
            if self.inv:
                return self.uni + str(self.inv[0])
            return self.uni
    hero = Player(5, 5, '(~˘▾˘)~')
    item_list = [Item(2, 5, '🔨'), Item(5, 2, '🔨')]
    my_screen = curses.initscr()
    my_screen.keypad(True)
    my_screen.clear()
    for one_item in item_list:
        my_screen.addstr(one_item.y, one_item.x, str(one_item))
    my_screen.addstr(hero.y, hero.x, str(hero))
    while True:
        in_key = my_screen.getkey()
        if in_key == 'q':
            curses.endwin()
            break
        elif in_key == 'KEY_UP':
            if hero.y - 1 >= 0:  # If we can't move up more
                hero.y -= 1
        my_screen.clear()
        for one_item in reversed(item_list):
            if one_item.y == hero.y and one_item.x == hero.x:
                hero.inv.append(one_item)
                item_list.remove(one_item)
            else:
                my_screen.addstr(one_item.y, one_item.x, str(one_item))
        my_screen.addstr(hero.y, hero.x, str(hero))