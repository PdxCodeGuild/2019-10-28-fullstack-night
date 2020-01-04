import argparse
import curses
parser = argparse.ArgumentParser()
parser.add_argument('-lvl', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
LEVEL = parsed_args.version_arg or 1
import random
import time
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
        self.inv = []

    def __str__(self):
        return self.uni#, self.uni2
    
    def mouth_string(self):
        return self.uni2
    
    def move(self, direction, steps):
        # change the y/x position of the character
        pass

    def attack(self, direction, weapon):
        #attack and everything
        pass

hero = Character(13, 46, '{00}', '-__-')

enemies = [
    Character(1, 96, '|><|', '|==|'),
    Character(7, 26, '|><|', '|==|'),
    Character(10, 61, '|><|', '|==|'),
    Character(13, 41, '|><|', '|==|'),
]

def gen_enemies(hero, enemies, num=4):
    tiles = []
    # [tiles.append(coord) for ]
    for y in range(23):
        for x in range(97):
            if y % 3 == 1 and x % 5 == 1:
                tiles.append((y, x))
    tiles.remove((hero.y, hero.x))
    for i in range(num):
        co_ord = random.choice(tiles)
        y = co_ord[0]
        x = co_ord[1]
        enemy = Character(y, x, '|><|', '|==|')
        enemies.append(enemy)
        tiles.remove((co_ord))
    return tiles
enemies = []
enemies_num = random.randrange(3, 7)
tiles = gen_enemies(hero, enemies, enemies_num)
def gen_items(item_attr_list, tiles, num=3):
    items = []
    for i in range(num):
        co_ord = random.choice(tiles)
        tiles.remove(co_ord)
        y = co_ord[0]
        x = co_ord[1]
        item_attr = random.choice(item_attr_list)
        item = Item(y, x, item_attr[0], item_attr[1], item_attr[2], item_attr[3])
        items.append(item)
    return items

# items = [
#     Item(20, 16, '🏹', 'bow'),
#     Item(19, 5, '🔫', 'gun')
# ]
item_attr_list = [
    ('🏹', 'bow', 1, 10),
    ('🗡', 'sword', 3, 1),
    ('🔫', 'gun', 2, 5)
]
items_num = random.randrange(2, 5)
items = gen_items(item_attr_list, tiles, items_num)
unicode_storage_list = ['🗡', '⚔', '🔫', '🏹', '🛡', '🔑', '🗝', '❤', '☠', '☠', '⬆', '➡', '⬇', '⬅']

moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

key_list = ['KEY_UP', 'KEY_DOWN', 'KEY_RIGHT', 'KEY_LEFT']

def fix_pos(sprite): #converted this from function to method
    if sprite.y < 1:
        sprite.y = 1
    if sprite.y > 22:
        sprite.y = 22
    if sprite.x < 1:
        sprite.x = 1
    if sprite.x > 96:
        sprite.x = 96

def aim(hero, wasd):#converted
    if wasd == 'w':
        game_screen.addstr(hero.y - 1, hero.x, '⬆')
    elif wasd == 'a':
        game_screen.addstr(hero.y, hero.x - 1, '⬅')
    elif wasd == 's':
        game_screen.addstr(hero.y + 1, hero.x, '⬇')
    elif wasd == 'd':
        game_screen.addstr(hero.y, hero.x + 2, '➡')
    draw_screen(hero, enemies, items, game_screen)

def shoot(hero, enemies, aim_dir, game_screen):#converted
    if hero.inv:
        for enemy in enemies:
            if (aim_dir == 'w' and hero.x == enemy.x and hero.y > enemy.y) or (aim_dir == 'a' and hero.y == enemy.y and hero.x > enemy.x) or (aim_dir == 's' and hero.x == enemy.x and hero.y < enemy.y) or (aim_dir == 'd' and hero.y == enemy.y and hero.x < enemy.x):
                enemy.uni = '☠'
                draw_screen(hero, enemies, items, game_screen)
                time.sleep(1)
                enemies.remove(enemy)
        hero.inv[0].uses -= 1
        if hero.inv[0].uses == 0:
            hero.inv.remove(hero.inv[0])

def enemy_move(hero, enemies):
    for enemy in enemies:
        y_or_x = random.choice(['y', 'x'])
        if enemy.y == hero.y:
            y_or_x = 'x'
        elif enemy.x == hero.x:
            y_or_x = 'y'
        if y_or_x == 'y':
            if enemy.y > hero.y:
                enemy.y -= 3
            else:
                enemy.y += 3
        else:
            y_or_x == 'x'
            if enemy.x > hero.x:
                enemy.x -= 5
            else:
                enemy.x += 5
        fix_pos(enemy)


def draw_screen(hero, enemies, items, game_screen):
    game_screen.clear()
    for y in range(26):
        for x in range(100):
            if x % 5 == 0 :
                game_screen.addstr(y, x, '|')
            if y % 3 == 0:
                game_screen.addstr(y, x, '-')
    if dead == True:
        hero.uni = '☠'
        game_screen.addstr(1, 1, "AND YOU DEAD")
    [game_screen.addstr(item.y + 1, item.x + 1, str(item)) for item in items]
    [game_screen.addstr(enemy.y, enemy.x, str(enemy)) for enemy in enemies]
    [game_screen.addstr(enemy.y + 1, enemy.x, enemy.mouth_string()) for enemy in enemies]
    game_screen.addstr(hero.y, hero.x, str(hero))
    game_screen.addstr(hero.y + 1, hero.x, hero.mouth_string())
    game_screen.addstr(25, 1, f"Inventory: {hero.inv}")
    game_screen.addstr(25, 35, f"Screen Size: {game_screen.getmaxyx()}")
    game_screen.addstr(25, 70, f"Hero Postion: {hero.y, hero.x}")
    if won:
        game_screen.addstr(1, 1, "YOU WON!")
        # game_screen.addstr(2, 1, f"{game_screen.getmaxyx()}")

game_screen = curses.initscr()
curses.curs_set(0)
 
print(game_screen.getmaxyx())
won = False
dead = False
game_screen.keypad(True)
game_screen.clear()
draw_screen(hero, enemies, items, game_screen)
game_screen.addstr(2, 41, "Arrow Keys To Move")
game_screen.addstr(5, 41, "WASD     To    Aim")
game_screen.addstr(8, 41, "SPACE   To   Shoot")
# game_screen.addstr(hero.y, hero.x, str(hero))
# game_screen.addstr(hero.y + 1, hero.x, hero.mouth_string())
# [game_screen.addstr(item.y, item.x, str(item)) for item in items]
# [game_screen.addstr(enemy.y, enemy.x, str(enemy)) for enemy in enemies]
# [game_screen.addstr(enemy.y + 1, enemy.x, enemy.mouth_string()) for enemy in enemies]
# game_screen.addstr(21, 5, f"Inventory: {hero.inv}")

# for enemy in enemies:
#     game_screen.addstr(enemy.y, enemy.x, str(enemy))
while True:
    in_key = game_screen.getkey()
    if in_key == 'q':
        curses.endwin()
        break
    for enemy in enemies:
        if enemy.x == hero.x and enemy.y == hero.y:
            dead = True

    if dead == False and in_key in ['KEY_UP', 'KEY_DOWN', 'KEY_RIGHT', 'KEY_LEFT']:
        
        if in_key == key_list[0]:
            hero.y -= 3
        elif in_key == key_list[1]:
            hero.y += 3
        elif in_key == key_list[2]:
            hero.x += 5
        elif in_key == key_list[3]:
            hero.x -= 5
        fix_pos(hero)
        for item in items:
            if item.y == hero.y and item.x == hero.x:
                hero.inv.append(item)
                items.remove(item)
        enemy_move(hero, enemies)
    if dead == False and in_key in ['w', 'a', 's', 'd']:
        aim(hero, in_key)
        aim_dir = in_key
        draw_screen(hero, enemies, items, game_screen)
    if dead == False and in_key == ' ':
        shoot(hero, enemies, aim_dir, game_screen)
        enemy_move(hero, enemies)
    if enemies == []:
        won = True

    draw_screen(hero, enemies, items, game_screen)
    # print(game_screen.getmaxyx())