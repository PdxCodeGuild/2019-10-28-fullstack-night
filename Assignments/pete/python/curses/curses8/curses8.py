'''
The purpose of this file is to restructure the code I've already written in a better way.  First I'll import everything I need.  I haven't used argparse so I'll exclude it this time.
Possible additions outside of restructuring:
Health bar for hero
'''
import curses
import random
import time

'''hjk hjkl hjlk 
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
            self.x += 5
        elif dir == 'right':
            self.x -= 5
    
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
class Hero(Sprite):
    def __init__(self, y, x, uni, uni2):
        super().__init__(y, x, uni, uni2)
        self.inv = []
        # self.uni2 = uni2 #do I need this?

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
    
    def select(self):
        #Here I'll want to write a method to select different items for use
        pass
    
    def shoot(self, enemies, aim_dir):#here definitely want to fix the bug of killing multiple enemies with one shot maybe that'll have to wait until later
        if self.inv:
            in_line_enemies = []
            for enemy in enemies:
                if (aim_dir == 'up' and self.x == enemy.x and self.y > enemy.y) or (aim_dir == 'left' and self.y == enemy.y and self.x > enemy.x) or (aim_dir == 'down' and self.x == enemy.x and self.y < enemy.y) or (aim_dir == 'right' and self.y == enemy.y and self.x < enemy.x):
                    in_line_enemies.append(enemy)
            for enemy in in_line_enemies:
                enemy.alive = False
            self.inv[0].uses -= 1
            if self.inv[0].uses == 0:
                self.inv.remove(self.inv[0])

class Enemy(Character):
    def __init__(self, y, x, uni, uni2):
        super().__init__(self, y, x, uni, uni2)
    
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

    def generate(self):
        #gonna start here next time
        pass
'''
Okay below I'll try making the game board a class as well.
'''
class Board():
    pass
