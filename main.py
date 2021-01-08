import tkinter as tk

from rules import Board
from agent import Agent

# setting = [None, None, None, None, None, None, None, None, None]
boardButtons = []


class GameBoard(tk.Frame):

    def __init__(self, root=None):
        tk.Frame.__init__(self, root)

        self.master.title("Križic Kružic")
        self.master.configure(background='black')
        self.master.resizable(width=False, height=False)

        self.board = Board()
        self.playerSign = "X"
        self.agentSign = "O"
        self.agent = Agent(self.board.setting, self.agentSign)

        self.createBoard()

        self.pack(fill="both")

    def createBoard(self):
        # Create Frames
        self.boardFrame = tk.Frame(self, bg="black")
        self.boardFrame.grid(row=0, column=0, columnspan=3, sticky='ew')

        # Create and place Title label
        self.titlelabel = tk.Label(self.boardFrame, height=2, width=6,
                                   text="TIC TAC TOE", font='SegoeUI 20 bold', fg="white", bg="black")
        self.titlelabel.grid(row=0, column=0, columnspan=3, sticky="ew")

        # Create buttons
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: self.playerSetMove(0)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: self.playerSetMove(1)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: self.playerSetMove(2)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: self.playerSetMove(3)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: self.playerSetMove(4)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: self.playerSetMove(5)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: self.playerSetMove(6)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: self.playerSetMove(7)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: self.playerSetMove(8)))

        self.reset_btn = tk.Button(self.boardFrame, height=2, width=16, text='RESET GAME',
                                   font='SegoeUI 10 bold', bg='green', fg='white', command=lambda: self.reset())
        self.train_btn = tk.Button(self.boardFrame, height=2, width=16, text='TRAIN AGENT',
                                   font='SegoeUI 10 bold', bg='green', fg='white', command=lambda: self.reset())

        # Place buttons
        boardButtons[0].grid(row=2, column=0)
        boardButtons[1].grid(row=2, column=1)
        boardButtons[2].grid(row=2, column=2)
        boardButtons[3].grid(row=3, column=0)
        boardButtons[4].grid(row=3, column=1)
        boardButtons[5].grid(row=3, column=2)
        boardButtons[6].grid(row=4, column=0)
        boardButtons[7].grid(row=4, column=1)
        boardButtons[8].grid(row=4, column=2)

        self.reset_btn.grid(row=5, column=0, columnspan=3, sticky='ew')
        self.train_btn.grid(row=6, column=0, columnspan=3, sticky='ew')

        # Create and place labels
        # self.train_label = tk.Label(self, text = "Agent još nije treniran", font='SegoeUI 10' )

    def playerSetMove(self, buttonNumber):
        self.board.setting[buttonNumber] = self.playerSign
        boardButtons[buttonNumber].configure(
            text=self.playerSign, bg='blue', fg='red', state=tk.DISABLED)
        print(self.board.setting, "set move")

        if self.checkGameOver():
            return

        self.agentSetMove()

    def agentSetMove(self):
        print("Agent radi potez")

        self.agent.states = self.board.setting
        self.agent.actions = self.agent.getAvailablePos()
        print("\n", self.agent.actions, "\n")
        pos = self.agent.makeRandomMove()
        self.board.setting[pos] = self.agentSign

        self.updateBoardSetting()
        print(self.board.setting)

    def updateBoardSetting(self):
        for i in range(9):
            if self.board.setting[i] is None:
                boardButtons[i].configure(
                    text=" ", bg='black', fg='white', state=tk.NORMAL)
            else:
                boardButtons[i].configure(
                    text=self.board.setting[i], bg='blue', fg='red', state=tk.DISABLED)
        self.checkGameOver()

    def checkGameOver(self):
        if self.board.isGameOver() is True:
            print("Igra gotova")
            winner = self.board.checkWin()
            print("Pobijedio je: ", winner)
            for i in range(9):
                boardButtons[i].configure(state=tk.DISABLED)
            return True
        else:
            False
            # ispisi pobjednika

    def reset(self):
        self.board.resetBoard()
        self.updateBoardSetting()
        if self.playerSign == "X":
            self.playerSign = "O"
            self.agentSign = "X"
            self.agentSetMove
        else:
            self.playerSign = "X"
            self.agentSign = "O"
        print(self.board.setting, "reset")


if __name__ == "__main__":
    GameBoard()
    tk.mainloop()
