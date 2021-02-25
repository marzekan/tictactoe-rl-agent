import tkinter as tk

board_buttons = []

class GameGUI(tk.Frame):
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)

        self.master.title("Tic Tac Toe")
        self.master.configure(background='black')
        self.master.resizable(width=False, height=False)

    def startGui(self):
        self.pack(fill="both")
        tk.mainloop()

    def createBoard(self, playerSetMove, reset, startTraining, agent_sign, player_sign):
        # Create Frames
        self.board_frame = tk.Frame(self, bg="black")
        self.board_frame.grid(row=0, column=0, columnspan=3, sticky='ew')

        # Create buttons
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(0)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(1)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(2)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(3)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(4)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(5)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(6)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(7)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                      font='SegoeUI 20 bold', bg='black', fg='white', command=lambda: playerSetMove(8)))

        # Place board buttons
        board_buttons[0].grid(row=2, column=0)
        board_buttons[1].grid(row=2, column=1)
        board_buttons[2].grid(row=2, column=2)
        board_buttons[3].grid(row=3, column=0)
        board_buttons[4].grid(row=3, column=1)
        board_buttons[5].grid(row=3, column=2)
        board_buttons[6].grid(row=4, column=0)
        board_buttons[7].grid(row=4, column=1)
        board_buttons[8].grid(row=4, column=2)

        # Create and place Status label
        self.status_label = tk.Label(self.board_frame, height=5, width=6,
                                    text="You: " + player_sign + "\nAgent: " + agent_sign,
                                    font='SegoeUI 10 bold', fg="green", bg="white")
        self.status_label.grid(row=5, column=0, columnspan=3, sticky="ew")

        # Create and place command buttons
        self.reset_btn = tk.Button(self.board_frame, height=2, width=16, text='RESET GAME',
                                   font='SegoeUI 10 bold', bg='green', fg='white', command=lambda: reset())
        self.train_btn = tk.Button(self.board_frame, height=2, width=16, text='TRAIN AGENT',
                                   font='SegoeUI 10 bold', bg='green', fg='white', command=lambda: startTraining())
        self.reset_btn.grid(row=6, column=0, columnspan=3, sticky='ew')
        self.train_btn.grid(row=7, column=0, columnspan=3, sticky='ew')

        # Create and place training label
        self.progress_label = tk.Label(self.board_frame, height=1, width=6,
                                      text="Agent is not treined yet.",
                                      font='SegoeUI 10', fg="green", bg="white")
        self.progress_label.grid(row=8, column=0, columnspan=3, sticky="ew")

    def updateBoardBySetting(self, setting):
        for i in range(9):
            if setting[i] is None:
                board_buttons[i].configure(
                    text=" ", bg='black', fg='white', state=tk.NORMAL)
            else:
                board_buttons[i].configure(
                    text=setting[i], bg='blue', fg='red', state=tk.DISABLED)

    def updateProgressLabel(self, text, current_value, refresh_rate=500):
        self.updateProgressLabelText(text)
        if current_value % refresh_rate == 0:
            self.progress_label.update()

    def updateProgressLabelText(self, textProgress):
        self.progress_label.configure(text=textProgress)

    def updateStatusLabelText(self, statusText):
        self.status_label.configure(text=statusText)

    def disableAllBoardButtons(self):
        for i in range(9):
            board_buttons[i].configure(state=tk.DISABLED)

    def setSignIntoBoardPosition(self, sign, position):
        board_buttons[position].configure(
            text=sign, bg='blue', fg='red', state=tk.DISABLED)

    # disable all buttons on the screen
    def setGuiToStartTraining(self):
        for i in range(9):
            board_buttons[i].configure(state=tk.DISABLED)
        self.reset_btn.configure(bg='gray', state=tk.DISABLED)
        self.train_btn.configure(bg='gray', state=tk.DISABLED)
        self.status_label.configure(text="Training in progress")
        self.status_label.update()

    # enable all buttons on the screen
    def setGuiToEndTraining(self):
        for i in range(9):
            board_buttons[i].configure(state=tk.NORMAL)
        self.reset_btn.configure(bg='green', state=tk.NORMAL)
        self.train_btn.configure(bg='green', state=tk.NORMAL)
        self.status_label.configure(
            text="Training ended.\nPress restart to start game")
