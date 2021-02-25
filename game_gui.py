import tkinter as tk

boardButtons = []

class GameGUI(tk.Frame):
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)

        self.master.title("Tic Tac Toe")
        self.master.configure(background='black')
        self.master.resizable(width=False, height=False)

    def startGui(self):
        self.pack(fill="both")
        tk.mainloop()

    def createBoard(self, playerSetMove, reset, startTraining, agentSign, playerSign):
        # Create Frames
        self.boardFrame = tk.Frame(self, bg="black")
        self.boardFrame.grid(row=0, column=0, columnspan=3, sticky='ew')

        # Create buttons
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(0)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(1)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(2)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(3)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(4)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(5)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(6)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(7)))
        boardButtons.append(tk.Button(self.boardFrame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(8)))

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
                                    text="You: " + playerSign + "\nAgent: " + agentSign,
                                    font='SegoeUI 10 bold', fg="green", bg="white")
        self.statusLabel.grid(row=5, column=0, columnspan=3, sticky="ew")

        # Create and place command buttons
        self.reset_btn = tk.Button(self.boardFrame, height=2, width=16, text='RESET GAME',
                                   font='SegoeUI 10 bold', bg='green', fg='white', command=lambda: reset())
        self.train_btn = tk.Button(self.boardFrame, height=2, width=16, text='TRAIN AGENT',
                                   font='SegoeUI 10 bold', bg='green', fg='white', command=lambda: startTraining())
        self.reset_btn.grid(row=6, column=0, columnspan=3, sticky='ew')
        self.train_btn.grid(row=7, column=0, columnspan=3, sticky='ew')

        # Create and place training label
        self.progressLabel = tk.Label(self.boardFrame, height=1, width=6,
                                      text="Agent is not treined yet.",
                                      font='SegoeUI 10', fg="green", bg="white")
        self.progressLabel.grid(row=8, column=0, columnspan=3, sticky="ew")

    def updateBoardBySetting(self, setting):
        for i in range(9):
            if setting[i] is None:
                boardButtons[i].configure(
                    text=" ", bg='black', fg='white', state=tk.NORMAL)
            else:
                boardButtons[i].configure(
                    text=setting[i], bg='blue', fg='red', state=tk.DISABLED)

    def updateProgressLabel(self, text, current_value, refresh_rate=20):
        self.progressLabel.configure(text)
        if current_value % refresh_rate == 0:
            self.progressLabel.update()

    def updateProgressLabelText(self, text):
        self.progressLabel.configure(text=text)

    def updateStatusLabelText(self, statusText):
        self.statusLabel.configure(text=statusText)

    def disableAllBoardButtons(self):
        for i in range(9):
            boardButtons[i].configure(state=tk.DISABLED)

    def setSignIntoBoardPosition(self, sign, position):
        boardButtons[position].configure(
            text=sign, bg='blue', fg='red', state=tk.DISABLED)

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
