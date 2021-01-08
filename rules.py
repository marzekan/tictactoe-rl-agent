class Board:
    def __init__(self):
        self.rows = 3
        self.cols = 3

        self.setting = [None for x in range(self.rows * self.cols)]

    def checkCols(self):

        for i in range(9):
            if i in [0, 1, 2]:
                if self.setting[i] == self.setting[i+3] == self.setting[i+6]:
                    pass

    # Checks if there is a win on the board.
    def checkWin(self) -> str:

        # Win is in the first row.
        if len(set(self.setting[0:3])) == 1:
            return self.setting[0]
        # Win is in the second row.
        elif len(set(self.setting[3:6])) == 1:
            return self.setting[3]
        # Win is in the third row.
        elif len(set(self.setting[6:9])) == 1:
            return self.setting[6]

        elif checkCols():
            return

    def isGameOver(self) -> str:

        # Return 'X'
        if isWinningMove():
            pass
        #
        elif None not in self.setting:
            return True


def resetBoard(self):
    # Reset the board to beggining state.
    self.setting = [None for x in range(self.rows * self.cols)]


board = Board()
print(board.setting)
print(len(board.setting))

lis = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(lis[0:3])
print(lis[3:6])
print(lis[6:9])
