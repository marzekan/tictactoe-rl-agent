import tkinter as tk


class GameGUI(tk.Frame):
    def __init__(self):
        super().__init__()

    def createBoard(self, reset_function, start_training, player_move):
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
                                   font='SegoeUI 10 bold', bg='green', fg='white', command=lambda: reset_function())
        self.train_btn = tk.Button(self.boardFrame, height=2, width=16, text='TRAIN AGENT',
                                   font='SegoeUI 10 bold', bg='green', fg='white', command=lambda: self.startTraining())
        self.reset_btn.grid(row=6, column=0, columnspan=3, sticky='ew')
        self.train_btn.grid(row=7, column=0, columnspan=3, sticky='ew')

        # Create and place training label
        self.progressLabel = tk.Label(self.boardFrame, height=1, width=6,
                                      text="Agent is not treined yet.",
                                      font='SegoeUI 10', fg="green", bg="white")
        self.progressLabel.grid(row=8, column=0, columnspan=3, sticky="ew")
