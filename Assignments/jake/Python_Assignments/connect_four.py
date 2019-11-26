import re
import string
import sys


PLAYING = "PLAYING"
WAITING = "WAITING"
WINNERX = "XXXX"
WINNERO = "OOOO"

## User Class
class User:
    state = ""
    name = ""
    def __init__(self,name, stateParam):
        self.name = name
        self.state = stateParam

    def userInfo(self):
        return self.name

    def getState(self):
        return self.state
    def setState(self, stateParam):
        self.state = stateParam

def printBoard(matrix):
    for num in range(1, 7):
        print(" "+ str(num) +" ", end = " ")
    print()

    for row in range(0, 6):
        for col in range(0, 6):
            print(" "+ str(matrix[row][col]) +" ", end = " ")
        print("")

def createMatrix(row, column) :
    mat = ["*"] * row
    for i in range(row):
        # mat[i] = ["" + str(i)] * column
        mat[i] = ["*"] * column
    return mat



def findMatrixMatched(matrix) :
    winFlg = False
    rowStrArr = []
    # get rows in String format
    for row in range(0, 6):
        str = ""
        for col in range(0, 6):
            str = str + matrix[row][col]
        rowStrArr.append(str)

    for rowStr in rowStrArr:
        # print("Row-" , rowStr)
        if WINNERX in rowStr or WINNERO in rowStr:
            winFlg = True
            break


    # get columns in String format
    colStrArr = []
    for col in range(0, 6):
        str = ""
        for row in range(0, 6):
            str = str + matrix[row][col]
        colStrArr.append(str)

    for colStr in colStrArr:
        # print("Col-" , colStr)
        if WINNERX in colStr or WINNERO in colStr :
            winFlg = True
            break

    # get diagonal match
    diagStrArr = [""] * 25
    for col in range(0, 6):
        diagNum = col

        for row in range(0, 6):
            if row + col > 5 :
                break
            if col == 0:
                diagStrArr[diagNum] = diagStrArr[diagNum] + matrix[row][row]  # middle
            else :
                diagStrArr[diagNum] = diagStrArr[diagNum] + matrix[row][row + col]  # upper
                diagStrArr[diagNum + 5] = diagStrArr[diagNum + 5] + matrix[row + col][row]  # lower

    # get diagonal match
    for col in range(0, 6):
        diagNum = col + 12

        for row in range(0,6):
            rowId = 5-row
            # print(col , " ---- " , rowId, " ---- " , row)
            if rowId - col < 0 :
                break

            if col == 0:
                diagStrArr[diagNum] = diagStrArr[diagNum] + matrix[row][rowId]  # middle
            else :
                diagStrArr[diagNum] = diagStrArr[diagNum] + matrix[row][rowId - col]  # upper
                diagStrArr[diagNum + 5] = diagStrArr[diagNum + 5] + matrix[row + col][rowId]  # lower


    for diagStr in diagStrArr:
        # print("Diag-" , diagStr)
        if WINNERX in diagStr or WINNERO in diagStr:
            winFlg = True
            break

    return winFlg



def appConnect():
    userA = User("A" , PLAYING)
    userB = User("B" , WAITING)

    matBoard = createMatrix(6,6)
    printBoard(matBoard)

    turn = 0
    while True:
        user = userA
        if turn % 2 == 0 :
            user = userA
            userA.setState(PLAYING)
            userB.setState(WAITING)
        else :
            user = userB
            userB.setState(PLAYING)
            userA.setState(WAITING)

        print(".................................................. ")
        print("Preference : ", user.userInfo() , " SEQ : ", str(turn + 1))
        print(".................................................. ")

        try:
            print( user.userInfo() , " turn >>>>>......................... ")
            color = str(input("Please select X or O > "))
            if color != 'X' and color != 'O' :
                print("Wrong Entry", color)
                continue

            colNum = int(input("Please Enter column Number >"))
            if colNum > 6 and colNum < 0:
                print("Wrong Entry -> Please Enter 1 - 5 :", colNum)
                continue

            colNum = colNum - 1; # column starting from 0
            for row in range(5, -1, -1):
                if matBoard[row][colNum] == "*" :
                    matBoard[row][colNum] = color
                    break;

            turn += 1
        except ValueError:
            print('Invalid Number !! Please try again')

        printBoard(matBoard)
        if findMatrixMatched(matBoard) :
            print(".................................................. ")
            print("User : ", user.userInfo() , " Win the Match by ", str(turn / 2) , " Steps")
            print(".................................................. ")
            break

        if turn >= 20:
            print("You have crossed maximum limits. Please start again.")
            break

if __name__ == '__main__':
    appConnect()