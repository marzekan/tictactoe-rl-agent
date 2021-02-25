import tkinter as tk

from time import sleep
from rules import Board
from agent import Agent
from train import Simulation

boardButtons = []


class GameBoard(tk.Frame):

    def __init__(self, root=None):
        tk.Frame.__init__(self, root)

        self.master.title("Tic Tac Toe")
        self.master.configure(background='black')
        self.master.resizable(width=False, height=False)

        self.board = Board()
        self.playerSign = "X"
        self.agentSign = "O"
        self.agent = Agent(self.board.setting, self.agentSign, strategy="q")

        self.createBoard()
        self.checkIfAgentTrained()

        self.pack(fill="both")

    def createBoard(self):
        # Create Frames
        self.boardFrame = tk.Frame(self, bg="black")
        self.boardFrame.grid(row=0, column=0, columnspan=3, sticky='ew')

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

        # Place board buttons
        boardButtons[0].grid(row=2, column=0)
        boardButtons[1].grid(row=2, column=1)
        boardButtons[2].grid(row=2, column=2)
        boardButtons[3].grid(row=3, column=0)
        boardButtons[4].grid(row=3, column=1)
        boardButtons[5].grid(row=3, column=2)
        boardButtons[6].grid(row=4, column=0)
        boardButtons[7].grid(row=4, column=1)
        boardButtons[8].grid(row=4, column=2)

        # Create and place Status label
        self.statusLabel = tk.Label(self.boardFrame, height=5, width=6,
                                    text="You: " + self.playerSign + "\nAgent: " + self.agentSign,
                                    font='SegoeUI 10 bold', fg="green", bg="white")
        self.statusLabel.grid(row=5, column=0, columnspan=3, sticky="ew")

        # Create and place command buttons
        self.reset_btn = tk.Button(self.boardFrame, height=2, width=16, text='RESET GAME',
                                   font='SegoeUI 10 bold', bg='green', fg='white', command=lambda: self.reset())
        self.train_btn = tk.Button(self.boardFrame, height=2, width=16, text='TRAIN AGENT',
                                   font='SegoeUI 10 bold', bg='green', fg='white', command=lambda: self.startTraining())
        self.reset_btn.grid(row=6, column=0, columnspan=3, sticky='ew')
        self.train_btn.grid(row=7, column=0, columnspan=3, sticky='ew')

        # Create and place training label
        self.progressLabel = tk.Label(self.boardFrame, height=1, width=6,
                                      text="Agent is not treined yet.",
                                      font='SegoeUI 10', fg="green", bg="white")
        self.progressLabel.grid(row=8, column=0, columnspan=3, sticky="ew")

    # When player clicks on the board. Area is marked with players sign.
    # Afterwards player signals agent to play if the game is not over.
    def playerSetMove(self, buttonNumber):
        self.board.setting[buttonNumber] = self.playerSign
        boardButtons[buttonNumber].configure(
            text=self.playerSign, bg='blue', fg='red', state=tk.DISABLED)

        if self.checkGameOver():
            return

        self.agentSetMove()

    def agentSetMove(self):
        sleep(0.2)

        self.agent.states = self.board.setting
        self.agent.actions = self.agent.getAvailablePos()
        pos = self.agent.makeMove()
        if self.board.checkWin() == self.agent.sign:
            self.agent.beRewarded(1)
        elif self.board.checkWin() == self.playerSign:
            self.agent.beRewarded(-1)
        else:
            self.agent.beRewarded(0.1)

        self.board.setting[pos] = self.agentSign

        self.updateBoardSetting()

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
            winner = self.board.checkWin()
            for i in range(9):
                boardButtons[i].configure(state=tk.DISABLED)
            if winner is None:
                statusText = "It's a draw."
            else:
                statusText = "Game over!\nThe winner is:" + winner
            self.statusLabel.configure(text=statusText)
            return True
        else:
            return False

    # resets tje board anc checks if the agent is trained
    def reset(self):
        self.board.resetBoard()
        self.updateBoardSetting()
        self.statusLabel.configure(
            text="You: " + self.playerSign + "\nAgent: " + self.agentSign)
        self.checkIfAgentTrained()

    # start training the agent
    def startTraining(self):
        self.board.resetBoard()

        simulation = Simulation("RR")
        print(simulation)
        if simulation != None:
            self.setGuiToStartTraining()

            numberOfIterations = 2000

            for i in range(numberOfIterations):
                simulation.simulateGame()
                self.trainProgress(i, numberOfIterations)

            simulation.agentO.saveQStates("trained_O.pkl")

            self.setGuiToEndTraining()

    # disable all buttons on the screen
    def setGuiToStartTraining(self):
        for i in range(9):
            boardButtons[i].configure(state=tk.DISABLED)
        self.reset_btn.configure(bg='gray', state=tk.DISABLED)
        self.train_btn.configure(bg='gray', state=tk.DISABLED)
        self.statusLabel.configure(text="Training in progress")
        self.statusLabel.update()

    # enable all buttons on the screen
    def setGuiToEndTraining(self):
        for i in range(9):
            boardButtons[i].configure(state=tk.NORMAL)
        self.reset_btn.configure(bg='green', state=tk.NORMAL)
        self.train_btn.configure(bg='green', state=tk.NORMAL)
        self.statusLabel.configure(
            text="Training ended.\nPress restart to start game")
        self.checkIfAgentTrained()

    # show iteration E.G. "00% 128/10000"
    def trainProgress(self, current, numberOfIterations):
        percentage = "{0:.0f}%".format(current/numberOfIterations * 100)
        self.progressLabel.configure(
            text=str(percentage) + " " + str(current) + "/" + str(numberOfIterations))
        print(str(percentage), " ", str(current), "/", str(numberOfIterations))
        if current % 500 == 0:
            self.progressLabel.update()

    # check if .pkl file exists
    def checkIfAgentTrained(self):
        filesExists = False
        try:
            self.agent.loadQStates("trained_O.pkl")
            filesExists = True
        except IOError:
            print("File not accessible")
        if filesExists is True:
            self.progressLabel.configure(
                text="Agent is trained and ready to play.")
        return filesExists


if __name__ == "__main__":
    GameBoard()
    tk.mainloop()
