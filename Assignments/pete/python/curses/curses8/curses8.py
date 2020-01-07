'''
next time: see why shoot isn't working!
'''

'''
The purpose of this file is to restructure the code I've already written in a better way.  First I'll import everything I need.  I haven't used argparse so I'll exclude it this time.
Possible additions outside of restructuring:
Health bar for hero
'''
import curses
import random
import time

'''
Below:  I establish classes.  In this version, I will convert some functions into methods.  Such as:
aim() to hero.aim()
shoot() to hero.shoot()
I may also turn the game board into a class.
Also I'll want to clean up the main loop in favor of functions or methods defined elsewhere.
'''
class Sprite():
    def __init__(self, y, x, uni):
        self.y = y
        self.x = x
        self.uni = uni
    def __str__(self):
        return self.uni

class Item(Sprite):
    def __init__(self, y, x, uni, id, uses, range):
        super().__init__(y, x, uni)
        self.id = id
        self.uses = uses
        self.range = range
    def __repr__(self):
        return f"{self.uni}:{self.uses}/{self.range}"

class Character(Sprite):
    def __init__(self, y, x, uni, uni2):
        super().__init__(y, x, uni)
        self.uni2 = uni2
        self.alive = True

    def __str__(self):
        return self.uni#, self.uni2
    
    def mouth_string(self): #I need a second method to help __str__ draw the sprites for characters too tall
        return self.uni2
    
    def move(self, dir): #made this a Character method for movement
        if dir == 'up':
            self.y -= 3
        elif dir == 'down':
            self.y += 3
        elif dir == 'left':
            self.x -= 5
        elif dir == 'right':
            self.x += 5
    
    def fix_pos(self): #converted this from function to method.  This method corrects the Character position in the case of exceeding the boundaries of the screen.
        if self.y < 1:
            self.y = 1
        if self.y > 22:
            self.y = 22
        if self.x < 1:
            self.x = 1
        if self.x > 96:
            self.x = 96

    # def attack(self, direction, weapon):
    #     #attack and everything Perhaps I will think of different types of attacks for enemies soon
    #     pass

'''
aim(wasd) is below.  I'd like to get this working so that the direction is drawn on the game screen.
Same with shoot.  I'd like to get the effect of briefly replacing the enemy string working.
'''
class Hero(Character):
    def __init__(self, y, x, uni, uni2, aim_dir=''):
        super().__init__(y, x, uni, uni2)
        self.inv = []
        self.won = False
        self.aim_dir = aim_dir
        # self.uni2 = uni2 #do I need this?

    # def move(self, dir):
    #     super().move(self, dir)

    def aim(self, wasd): #This aims the hero's weapon
        if wasd == 'w':
            aim_dir = 'up'
        elif wasd == 'a':
            aim_dir = 'left'
        elif wasd == 's':
            aim_dir = 'down'
        elif wasd == 'd':
            aim_dir = 'right'
        return aim_dir

    def pick_up(self, items):
        for item in items:
            if item.y == self.y and item.x == self.x:
                self.inv.append(item)
                items.remove(item)
    
    def select(self):
        #Here I'll want to write a method to select different items for use
        pass
    
    def shoot(self, enemies, aim_dir=''):#here definitely want to fix the bug of killing multiple enemies with one shot maybe that'll have to wait until later
        if self.inv:
            in_line_enemies = []
            for enemy in enemies:
                if (aim_dir == 'up' and self.x == enemy.x and self.y > enemy.y) or (aim_dir == 'left' and self.y == enemy.y and self.x > enemy.x) or (aim_dir == 'down' and self.x == enemy.x and self.y < enemy.y) or (aim_dir == 'right' and self.y == enemy.y and self.x < enemy.x):
                    in_line_enemies.append(enemy)
            for enemy in in_line_enemies:
                enemy.alive = False
                enemy.uni = '|xx|'
            self.inv[0].uses -= 1
            if self.inv[0].uses == 0:
                self.inv.remove(self.inv[0])

class Enemy(Character):
    def __init__(self, y, x, uni, uni2):
        super().__init__(y, x, uni, uni2)
    
    def enemy_move(self, hero):
        y_or_x = random.choice(['y', 'x'])
        if self.y == hero.y:
            y_or_x = 'x'
        elif self.x == hero.x:
            y_or_x = 'y'
        
        if y_or_x == 'y':
            if self.y > hero.y:
                self.y -= 3
            else:
                self.y += 3
        else:
            # y_or_x == 'x'
            if self.x > hero.x:
                self.x -= 5
            else:
                self.x += 5

        self.fix_pos()

        if self.y == hero.y and self.x == hero.x:
            hero.alive = False
            hero.uni = '{xx}'

    def generate(self, hero):
        #gonna start here next time
        pass
'''
Okay below I'll try making the game board a class as well.
'''
class Board():
    def __init__(self, height=26, width=100):
        self.height = height
        self.width = width

    def draw_screen(self, hero, enemies, items, game_screen):
        game_screen.clear()
        for y in range(26):
            for x in range(100):
                if x % 5 == 0:
                    game_screen.addstr(y, x, '|')
                if y % 3 == 0:
                    game_screen.addstr(y, x, '-')
        #items
        [game_screen.addstr(item.y + 1, item.x + 1, str(item)) for item in items]
        #enemies
        [game_screen.addstr(enemy.y, enemy.x, str(enemy)) for enemy in enemies]
        [game_screen.addstr(enemy.y + 1, enemy.x, enemy.mouth_string()) for enemy in enemies]
        #hero
        game_screen.addstr(hero.y, hero.x, str(hero))
        game_screen.addstr(hero.y + 1, hero.x, hero.mouth_string())
        #inventory
        game_screen.addstr(25, 1, f"Inventory: {hero.inv}")
        #feedback
        game_screen.addstr(25, 35, f"Screen Size: {game_screen.getmaxyx()}")
        game_screen.addstr(25, 70, f"Hero Position: {hero.y, hero.x}")
'''
Below I'll define 2 functions to generate and place enemies as well as items.  As far as I know, I think it makes sense to just write functions for these instead of OOP, but I should ask Al about it.
'''
def gen_enemies(hero, enemies, num=4):
    tiles = []
    for y in range(23):
        for x in range(97):
            if y % 3 == 1 and x % 5 == 1:
                tiles.append((y, x))
    tiles.remove((hero.y, hero.x))
    for i in range(num):
        yx = random.choice(tiles)
        y = yx[0]
        x = yx[1]
        enemy = Enemy(y, x, '|><|', '|==|')
        enemies.append(enemy)
        tiles.remove(yx)
    return tiles

def gen_items(item_attr_list, tiles, num=3):
    items = []
    for i in range(num):
        yx = random.choice(tiles)
        y = yx[0]
        x = yx[1]
        item_attr = random.choice(item_attr_list)
        item = Item(y, x, item_attr[0], item_attr[1], item_attr[2], item_attr[3])
        items.append(item)
    return items
'''
Classes done, I'll initialize the screen below and create instances of class.
'''
#hero
hero = Hero(13, 46, '{00}', '-__-')
#enemies
enemies = []
enemies_num = random.randrange(3, 7)
tiles = gen_enemies(hero, enemies, enemies_num)
#items
item_attr_list = [
    ('🏹', 'bow', 1, 10),
    ('🗡', 'sword', 3, 1),
    ('🔫', 'gun', 2, 5)
]
items_num = random.randrange(2, 5)
items = gen_items(item_attr_list, tiles, items_num)
board = Board()
#init screen
game_screen = curses.initscr()
curses.curs_set(0)#this makes the cursor invisible
game_screen.keypad(True)

udlr = ['KEY_UP', 'KEY_DOWN', 'KEY_RIGHT', 'KEY_LEFT']
wasd = ['w', 'a', 's', 'd']
dir_conv = {
    'KEY_UP': 'up',
    'w': 'up',
    'KEY_DOWN': 'down',
    's': 'down',
    'KEY_RIGHT': 'right',
    'd': 'right',
    'KEY_LEFT': 'left',
    'w': 'left'
}
while True:
    board.draw_screen(hero, enemies, items, game_screen)
    in_key = game_screen.getkey()
    if in_key == 'q':
        curses.endwin()
        break
    for enemy in enemies:
        if enemy.x == hero.x and enemy.y == hero.y:
            hero.alive = False
            hero.__str__ = '{xx}'
    if hero.alive:
        if in_key in udlr:
            hero.move(dir_conv[in_key])
            hero.fix_pos()
            hero.pick_up(items)
            [enemy.enemy_move(hero) for enemy in enemies]
        if in_key in wasd:
            aim_dir = hero.aim(in_key)
        if hero.aim_dir:
            if in_key == ' ':
                hero.shoot(enemies, aim_dir)
                [enemy.enemy_move(hero) for enemy in enemies if enemy.alive]