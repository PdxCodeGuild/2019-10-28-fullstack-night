'''
By: Dustin DeShane
Filename: connect-four.py
'''

class Player:

    def __init__(self):
        self.name = input("Please enter your name: ")
        self.color = input("Would you like to play as Red or Black pieces?: ").lower()
        self.piece = ""
        if self.color == "red":
            self.piece = "X"
        else:
            self.piece = "O"

class Game:
    def __init__(self, x=7, y=6):
        self.x = x
        self.y = y
        board_list = []
        for i in range(self.y):
            one_row = []
            for j in range(self.x):
                one_row.append("|_|")
            board_list.append(one_row)
        new_board = ""
        for one_list in board_list:
            new_board = new_board + ''.join(one_list)
            new_board = new_board + '\n'
        print(new_board)

    def board(self):
        width = self.x
        height = self.y
        # for columns in range(height):
        #     print('\n')
        #     for rows in range(width):
        #         print("|_|", end='')

    def piece(self, p_color):
        piece_color = p_color
        piece_shape = "X"
    
    def get_height(position):
        pass

    def move(self, player, position):
        board_list = []
        for i in range(self.y):
            one_row = []
            for j in range(self.x):
                if position == j:
                    one_row.append(self.piece)
                else:
                    one_row.append("|_|")
            board_list.append(one_row)
        new_board = ""
        for one_list in board_list:
            new_board = new_board + ''.join(one_list)
            new_board = new_board + '\n'
        print(new_board)
    
    def calc_winner(self):
        pass

    def is_full(self):
        pass

    def is_game_over(self, move_counter):
        if move_counter == 5:
            return False
        return True

player_one = Player()
player_two = Player()
new_game = Game()
game_board = new_game.board()
move_counter = 0
current_player = player_one
game_progress = new_game.is_game_over(move_counter)

while game_progress:
    if move_counter % 2 == 0:
        current_player = player_one
        position = int(input(f"{player_one.name}, please choose a column: "))
        new_game.move(current_player, position)
        move_counter += 1
        print(move_counter)
    elif move_counter % 2 == 1:
        current_player = player_two
        position = int(input(f"{player_two.name}, please choose a column: "))
        new_game.move(current_player, position)
        move_counter += 1
        print(move_counter)
    game_progress = new_game.is_game_over(move_counter)


    
