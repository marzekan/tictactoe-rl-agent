class Board:
    def __init__(self):
        '''
            [0,1,2,3,4,5,6,7,8]

            | 0, 1, 2 |
            | 3, 4, 5 |
            | 6, 7, 8 |
        '''
        self.rows = 3
        self.cols = 3

        self.setting = [None for x in range(self.rows * self.cols)]

    def checkColsWin(self) -> str:

        # Check if some column contains same values.
        for i in [0, 1, 2]:
            if self.setting[i] == self.setting[i+3] == self.setting[i+6]:
                if self.setting[i] != None:
                    return self.setting[i]

    def checkRowsWin(self) -> str:

        # Check if some column contains same values.
        for i in [0, 3, 6]:
            if self.setting[i] == self.setting[i+1] == self.setting[i+2]:
                if self.setting[i] != None:
                    return self.setting[i]

    def checkDiagonalsWin(self) -> str:

        # Check left diagonal.
        if self.setting[0] == self.setting[4] == self.setting[8]:
            return self.setting[0]

        # Check right diagonal.
        elif self.setting[2] == self.setting[4] == self.setting[6]:
            return self.setting[2]

    # Checks if there is a win on the board and returns winner.
    def checkWinner(self) -> str:

        colWin, rowWin, diagonWin = self.checkColsWin(
        ), self.checkRowsWin(), self.checkDiagonalsWin()

        for winner in [colWin, rowWin, diagonWin]:
            if winner != None:
                return winner

    # Checks if there is a winner on the board returns true of there is.
    def isGameOver(self) -> bool:

        # If there is no empty fields on the board -> game is over.
        if None not in self.setting:
            return True

        # If there is a winner -> game is over.0
        elif self.checkWinner() != None:
            return True

        else:
            return False

    # Sets passed sign to passed position in board array.
    def setSignToPos(self, position, sign):
        self.setting[position] = sign

    def resetBoard(self):

        # Reset the board to beggining state.
        self.setting = [None for x in range(self.rows * self.cols)]
