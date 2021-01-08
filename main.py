import tkinter as tk


setting = [None, None, None, None, None, None, None, None, None]
boardButtons = []

class GameBoard(tk.Frame):
    def __init__(self, root = None):
        tk.Frame.__init__(self, root)

        self.master.title("Krizic Kruzic")
        self.master.configure(background='black')

        global playerSign
        playerSign = "X"
        global agentSign
        agentSign = "O"
        
        self.createBoard()

        self.pack(fill="both")
    
    def createBoard(self):
        # Create labels
        self.info_label = tk.Label(self, text = "TIC TAC TOE", font='SegoeUI 30 bold' )
        self.train_label = tk.Label(self, text = "Agent još nije treniran", font='SegoeUI 10' )

        # Create buttons
        boardButtons.append(tk.Button(self, height = 4, width = 8, text=' ', font='SegoeUI 20 bold', bg='black', fg='white', command = lambda : self.setMove(0)))
        boardButtons.append(tk.Button(self, height = 4, width = 8, text=' ', font='SegoeUI 20 bold', bg='black', fg='white', command = lambda : self.setMove(1)))
        boardButtons.append(tk.Button(self, height = 4, width = 8, text=' ', font='SegoeUI 20 bold', bg='black', fg='white', command = lambda : self.setMove(2)))
        boardButtons.append(tk.Button(self, height = 4, width = 8, text=' ', font='SegoeUI 20 bold', bg='black', fg='white', command = lambda : self.setMove(3)))
        boardButtons.append(tk.Button(self, height = 4, width = 8, text=' ', font='SegoeUI 20 bold', bg='black', fg='white', command = lambda : self.setMove(4)))
        boardButtons.append(tk.Button(self, height = 4, width = 8, text=' ', font='SegoeUI 20 bold', bg='black', fg='white', command = lambda : self.setMove(5)))
        boardButtons.append(tk.Button(self, height = 4, width = 8, text=' ', font='SegoeUI 20 bold', bg='black', fg='white', command = lambda : self.setMove(6)))
        boardButtons.append(tk.Button(self, height = 4, width = 8, text=' ', font='SegoeUI 20 bold', bg='black', fg='white', command = lambda : self.setMove(7)))
        boardButtons.append(tk.Button(self, height = 4, width = 8, text=' ', font='SegoeUI 20 bold', bg='black', fg='white', command = lambda : self.setMove(8)))

        self.reset_btn = tk.Button(self, height=2, width=16, text='RESET GAME', font='SegoeUI 10 bold', bg='green', fg='white', command = lambda : self.reset())
        self.train_btn = tk.Button(self, height=2, width=16, text='TRAIN AGENTS', font='SegoeUI 10 bold', bg='green', fg='white', command = lambda : self.reset())

        # Place buttons
        # self.button0.grid(row = 1, column = 0)
        # self.button1.grid(row = 1, column = 1)
        # self.button2.grid(row = 1, column = 2)
        # self.button3.grid(row = 2, column = 0)
        # self.button4.grid(row = 2, column = 1)
        # self.button5.grid(row = 2, column = 2)  
        # self.button6.grid(row = 3, column = 0)
        # self.button7.grid(row = 3, column = 1)
        # self.button8.grid(row = 3, column = 2)

        boardButtons[0].grid(row = 1, column = 0)
        boardButtons[1].grid(row = 1, column = 1)
        boardButtons[2].grid(row = 1, column = 2)
        boardButtons[3].grid(row = 2, column = 0)
        boardButtons[4].grid(row = 2, column = 1)
        boardButtons[5].grid(row = 2, column = 2)  
        boardButtons[6].grid(row = 3, column = 0)
        boardButtons[7].grid(row = 3, column = 1)
        boardButtons[8].grid(row = 3, column = 2)

        self.reset_btn.grid(row=4, column=0)
        self.train_btn.grid(row=4, column=2)

    def setMove(self, buttonNumber):
        setting[buttonNumber] = playerSign
        boardButtons[buttonNumber].configure(text=playerSign, state=tk.DISABLED)
        print(setting)

    def updateMove(self, setting):
        self.setting = setting
        for i in range(9):
            if setting[i] is None:
                boardButtons[i].configure(text=" ", state=tk.NORMAL)
            else:
                boardButtons[i].configure(text=setting[i], state=tk.DISABLED)
    
    def reset(self):
        self.setting = [None, None, None, None, None, None, None, None, None]
        self.updateMove(self.setting)
        # POSALJI MARKU DA RESETIRA PLOCU 

if __name__ == "__main__":
    GameBoard()
    tk.mainloop()