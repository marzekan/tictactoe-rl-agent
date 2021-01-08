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

    # Checks if there is a win on the board.
    def checkWin(self) -> str:

        colWin, rowWin, diagonWin = self.checkColsWin(
        ), self.checkRowsWin(), self.checkDiagonalsWin()

        for win in [colWin, rowWin, diagonWin]:
            if win != None:
                return win

    def isGameOver(self) -> bool:

        if self.checkWin() != None:
            return True

        elif None not in self.setting:
            return True

        else:
            return False

    def resetBoard(self):

        # Reset the board to beggining state.
        self.setting = [None for x in range(self.rows * self.cols)]
