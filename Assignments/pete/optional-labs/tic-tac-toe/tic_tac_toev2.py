'''
Tic-Tac-Toe
'''
# import numpy

class Player:
    def __init__(self, name, token):
        self.name = name 
        self.token = token

class Game:
    def __init__(self):
        board = {
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
        }
        # for row in range(3):
        #     row_list = []
        #     for column in range(3):
        #         column = ' '
        #         row_list.append(column)
        #     board.append(row_list)
        self.board = board

    def __repr__(self):
        board = self.board
        return board[1] + '|' + board[2] + '|' + board[3] + '\n' + board[4] + '|' + board[5] + '|' + board[6] + '\n' + board[7] + '|' + board[8] + '|' + board[9]

    def move(self, player):
        while True:
            move = int(input("Which move? (1-9): "))
            if self.board[move] in '123456789':
                self.board[move] = player.token
                break
            else:
                print("You can't do that")
                continue

            # x = int(input(f"{player.name} x: "))
            # y = int(input(f"{player.name} y: "))
            # if self.board[y - 1][x - 1] == ' ':
            #     self.board[y - 1][x - 1] = player.token
            #     break
            # else:
            #     print("You can't do that")
            #     continue
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

            for i in range(3):
                column = []
                for row in self.board:
                    column.append(row[i])
                if set(column) == {token}:
                    print(f"{token} wins!")
                    quit()
            diagonal_1 = self.board[0][0], self.board[1][1], self.board[2][2]
            diagonal_2 = self.board[0][2], self.board[1][1], self.board[2][0]
            if set(diagonal_1) == {token} or set(diagonal_2) == {token}:
                print(f"{token} wins!")
                quit()

    def is_full(self):
        long_board = []
        for row in self.board:
            for column in row:
                long_board.append(column)
        return ' ' not in long_board

player1_name = 'Pete'
player2_name = 'Matt'
test = Game()
player1 = Player(player1_name, 'X')
player2 = Player(player2_name, 'O')
print(test)

while True:
    test.move(player1)
    test.move(player2)
