'''
Lab Connect Four

Connect Four is a board game. Players take turns placing tokens of their color into a vertical grid. They drop to the bottom, and if anyone has four of their color in a straight line, they've won!

Define a module that simulates a Connect Four game.

This will consist of the following classes:

Player:

    Properties
        name
        color

Game:

    Properties
        board: 7x6 board representation

'''
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Game:
    def __init__(self):
        board = []
        for row in range(6):
            row = []
            for column in range(7):
                column = ' '
                row.append(column)
            board.append(row)
        self.board = board
        with open('moves_list.txt', 'w') as moves_list:
            moves_list.write('')


    def __repr__(self):
        return ' |' + self.board[0][0] + '|' + self.board[0][1] + '|' + self.board[0][2] + '|' + self.board[0][3] + '|' + self.board[0][4] + '|' + self.board[0][5] + '|' + self.board[0][6] + '|\n |' + self.board[1][0] + '|' + self.board[1][1] + '|' + self.board[1][2] + '|' + self.board[1][3] + '|' + self.board[1][4] + '|' + self.board[1][5] + '|' + self.board[1][6] + '|\n |' + self.board[2][0] + '|' + self.board[2][1] + '|' + self.board[2][2] + '|' + self.board[2][3] + '|' + self.board[2][4] + '|' + self.board[2][5] + '|' + self.board[2][6] + '|\n |' + self.board[3][0] + '|' + self.board[3][1] + '|' + self.board[3][2] + '|' + self.board[3][3] + '|' + self.board[3][4] + '|' + self.board[3][5] + '|' + self.board[3][6] + '|\n |' + self.board[4][0] + '|' + self.board[4][1] + '|' + self.board[4][2] + '|' + self.board[4][3] + '|' + self.board[4][4] + '|' + self.board[4][5] + '|' + self.board[4][6] + '|\n |' + self.board[5][0] + '|' + self.board[5][1] + '|' + self.board[5][2] + '|' + self.board[5][3] + '|' + self.board[5][4] + '|' + self.board[5][5] + '|' + self.board[5][6] + '|\n  1 2 3 4 5 6 7'
    

    def get_height(self, position):
        for i, row in enumerate(self.board):
            if row[position - 1] != ' ':
                return 6 - i
        # return 0 if the column is totally empty
        return 0
            
    

    def move(self, player):
        position = int(input(f"{player.name}'s turn: Which position (1-7)? "))
        row_index = abs(self.get_height(position) - 5)
        self.board[row_index][position - 1] = player.color
        print(self)
        with open('moves_list.txt', 'a') as moves_list:
            moves_list.write(f"{position}\n")
        self.calc_winner()

    def calc_winner(self):
        R_Y = ['R', 'Y']
        for color in R_Y:
            for row in self.board:
                row_string = ''.join(row)
                if (color * 4) in row_string:
                    print(f"{color} wins!")
                    quit()
            for i in range(7):
                column = []
                for row in self.board:
                    column.append(row[i])
                column_string = ''.join(column)
                if (color * 4) in column_string:
                    print(f"{color} wins!")
                    quit()
            # diagonal_list = []
            # for i, row in enumerate(self.board):
            #     diagonal_list.append(row[i])
            #     ''.join(diagonal_list)
            #     if (color * 4) in diagonal_list:
            #         print(f"{color} wins!")
            #         quit()
            b = self.board

            #forward diagonals
            self.check_list(color, [b[0][0], b[1][1], b[2][2], b[3][3]])
            self.check_list(color, [b[0][1], b[1][2], b[2][3], b[3][4]])
            self.check_list(color, [b[0][2], b[1][3], b[2][4], b[3][5]])
            self.check_list(color, [b[0][3], b[1][4], b[2][5], b[3][6]])

            self.check_list(color, [b[1][0], b[2][1], b[3][2], b[4][3]])
            self.check_list(color, [b[1][1], b[2][2], b[3][3], b[4][4]])
            self.check_list(color, [b[1][2], b[2][3], b[3][4], b[4][5]])
            self.check_list(color, [b[1][3], b[2][4], b[3][5], b[4][6]])

            self.check_list(color, [b[2][0], b[3][1], b[4][2], b[5][3]])
            self.check_list(color, [b[2][1], b[3][2], b[4][3], b[5][4]])
            self.check_list(color, [b[2][2], b[3][3], b[4][4], b[5][5]])
            self.check_list(color, [b[2][3], b[3][4], b[4][5], b[5][6]])

            #backward diagonals
            self.check_list(color, [b[0][3], b[1][2], b[2][1], b[3][0]])
            self.check_list(color, [b[0][4], b[1][3], b[2][2], b[3][1]])
            self.check_list(color, [b[0][5], b[1][4], b[2][3], b[3][2]])
            self.check_list(color, [b[0][6], b[1][5], b[2][4], b[3][3]])

            self.check_list(color, [b[1][3], b[2][2], b[3][1], b[4][0]])
            self.check_list(color, [b[1][4], b[2][3], b[3][2], b[4][1]])
            self.check_list(color, [b[1][5], b[2][4], b[3][3], b[4][2]])
            self.check_list(color, [b[1][6], b[2][5], b[3][4], b[4][3]])

            self.check_list(color, [b[2][3], b[3][2], b[4][1], b[5][0]])
            self.check_list(color, [b[2][4], b[3][3], b[4][2], b[5][1]])
            self.check_list(color, [b[2][5], b[3][4], b[4][3], b[5][2]])
            self.check_list(color, [b[2][6], b[3][5], b[4][4], b[5][3]])


    def check_list(self, color, index_list):
        if ''.join(index_list) == (color * 4):
            print(f"{color} wins!")
            quit()




    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
            else:
                print("Board full.  Game over")
                quit()
                return True

player_1_name = input("Player 1: ")
player_2_name = input("Player 2: ")
player_1 = Player(player_1_name, 'R')
player_2 = Player(player_2_name, 'Y')        

game = Game()
# print(game)
# print(game.get_height(7))
# game.move(player_1)
print(game)
while True:
    game.move(player_1)
    game.move(player_2)
print(game.is_full())