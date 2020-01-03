import curses

class Item:
    def __init__(self, y, x, uni):#item x, y, and unicode
        self.y = y
        self.x = x
        self.uni = uni
    
    def __str__(self):#print string of item unicode
        return self.uni

class Player(Item):
    def __init__(self, y, x, uni):
        super().__init__(y, x, uni)
        self.inv = [] #inventory
    
    def __str__(self):
        if self.inv:
            return self.uni + str(self.inv[0])#print if hero has item
        return self.uni

hero = Player(5, 5, 'ᖱㅎᖲ')
villain1 = Player(5, 10, '🤷')
villain2 = Player(7, 11, '🦹')
villain3 = Player(14, 7, '🧟‍♂️')
villain4 = Player(7, 15, '🤺')
villain_list = [villain1, villain2, villain3, villain4]
fairy = Player(3, 3, '🧚‍♀️')
item_list = [Item(2, 5, '💣'), Item(5, 2, '🔪'), Item(9, 9, '🗝'), Item(8, 7, '🗡')]

my_screen = curses.initscr()
my_screen.keypad(True)
my_screen.clear()

for item in item_list:
    my_screen.addstr(item.y, item.x, str(item))


# my_screen.addstr(hero.x, hero.y, str(hero))

max_y, max_x = my_screen.getmaxyx()
while True:
    my_screen.addstr(hero.y, hero.x, str(hero))
    for villain in villain_list:
        my_screen.addstr(villain.y, villain.x, str(villain))
    in_key = my_screen.getkey()
    if in_key == 'q':
        curses.endwin()
        break
    elif in_key == 'KEY_UP':
        if hero.y - 1 >= 0: #can't move up more
            hero.y -= 1
    elif in_key == 'KEY_DOWN':
        if hero.y + 1 <= max_y:
            hero.y += 1
    elif in_key == 'KEY_LEFT':
        if hero.x -1 >= 0:
            hero.x -= 1
    elif in_key == 'KEY_RIGHT':
        if hero.x + 1 <= max_x:
            hero.x += 1
    my_screen.clear()
    for item in reversed(item_list):
        if item.y == hero.y and item.x == hero.x:
            hero.inv.append(item)
            item_list.remove(item)
        else:
            my_screen.addstr(item.y, item.x, str(item))