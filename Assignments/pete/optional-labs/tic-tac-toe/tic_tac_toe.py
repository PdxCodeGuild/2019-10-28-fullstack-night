'''
Tic-Tac-Toe
'''
import numpy

class Player:
    def __init__(self, name, token):
        self.name = name 
        self.token = token

class Game:
    def __init__(self):
        board = []
        for row in range(3):
            row_list = []
            for column in range(3):
                column = ' '
                row_list.append(column)
            board.append(row_list)
        self.board = board

    def __repr__(self):
        board = self.board
        return board[0][0] + '|' + board[0][1] + '|' + board[0][2] + '\n' + board[1][0] + '|' + board[1][1] + '|' + board[1][2] + '\n' + board[2][0] + '|' + board[2][1] + '|' + board[2][2]

    def move(self, player):
        while True:
            x = int(input(f"{player.name} x: "))
            y = int(input(f"{player.name} y: "))
            if self.board[y - 1][x - 1] == ' ':
                self.board[y - 1][x - 1] = player.token
                break
            else:
                print("You can't do that")
                continue
        print(self)
        Game.calc_winner(self)
        if Game.is_full(self) == True:
            print("Board full.  Game Over")
            quit()
        # return __r

    def calc_winner(self):
        X_O = ['X', 'O']
        for token in X_O:
            for row in self.board:
                if set(row) == {token}:
                    print(f"{token} wins!")
                    quit()


    def is_full(self):
        long_board = []
        for row in self.board:
            for column in row:
                long_board.append(column)
        return ' ' not in long_board

player1_name = 'Pete'
player2_name = 'Al'
test = Game()
player1 = Player(player1_name, 'X')
# test.move(1, 2, player1)
player2 = Player(player2_name, 'O')
# test.move(2, 1, player2)
print(test)

while True:
    # player1_x = int(input("Player1 x: "))
    # player1_y = int(input("Player1 y: "))
    test.move(player1)
    # print(test)
    # player2_x = int(input("Player2 x: "))
    # player2_y = int(input("Player2 y: "))
    test.move(player2)
    # print(test)
