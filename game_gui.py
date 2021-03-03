import tkinter as tk
from tkinter import messagebox
from typing import Callable

board_buttons = []


class GameGUI(tk.Frame):
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.defineColorsAndFont()
        self.master.title("Tic Tac Toe")
        self.master.configure(background='#00022E')
        self.master.resizable(width=False, height=False)

    def startGui(self):
        self.pack(fill="both")
        tk.mainloop()

    def defineColorsAndFont(self):
        self.font_big_bold = 'SegoeUI 20 bold'
        self.font_normal_bold = 'SegoeUI 10 bold'
        self.dark_blue_col = '#00022E'
        self.navy_blue_col = '#02066F'
        self.honeydew_col = '#E0F2E9'
        self.red_col = '#FF4365'
        self.yellow_col = '#E8C547'
        self.gray_col = '#71697A'

    def createBoard(self, playerSetMove, reset, agent_sign, player_sign):

        # Create Frames
        self.board_frame = tk.Frame(self, bg=self.dark_blue_col)
        self.board_frame.grid(row=0, column=0, columnspan=3, sticky='ew')

        # Create buttons
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                       font=self.font_big_bold, bg=self.dark_blue_col, fg=self.honeydew_col, command=lambda: playerSetMove(0)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                       font=self.font_big_bold, bg=self.dark_blue_col, fg=self.honeydew_col, command=lambda: playerSetMove(1)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                       font=self.font_big_bold, bg=self.dark_blue_col, fg=self.honeydew_col, command=lambda: playerSetMove(2)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                       font=self.font_big_bold, bg=self.dark_blue_col, fg=self.honeydew_col, command=lambda: playerSetMove(3)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                       font=self.font_big_bold, bg=self.dark_blue_col, fg=self.honeydew_col, command=lambda: playerSetMove(4)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                       font=self.font_big_bold, bg=self.dark_blue_col, fg=self.honeydew_col, command=lambda: playerSetMove(5)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                       font=self.font_big_bold, bg=self.dark_blue_col, fg=self.honeydew_col, command=lambda: playerSetMove(6)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                       font=self.font_big_bold, bg=self.dark_blue_col, fg=self.honeydew_col, command=lambda: playerSetMove(7)))
        board_buttons.append(tk.Button(self.board_frame, height=3, width=6, text=' ',
                                       font=self.font_big_bold, bg=self.dark_blue_col, fg=self.honeydew_col, command=lambda: playerSetMove(8)))

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
                                     font=self.font_normal_bold, fg=self.red_col, bg=self.dark_blue_col)

        self.status_label.grid(row=5, column=0, columnspan=3, sticky="ew")

        # Create and place command buttons
        self.reset_btn = tk.Button(self.board_frame, height=2, width=16, text='RESET GAME',
                                   font=self.font_normal_bold, bg=self.red_col, fg=self.dark_blue_col, command=lambda: reset())
        self.train_btn = tk.Button(self.board_frame, height=2, width=16, text='TRAIN AGENT',
                                   font=self.font_normal_bold, bg=self.red_col, fg=self.dark_blue_col, command=lambda: self.build_traning_modal())
        self.reset_btn.grid(row=6, column=0, columnspan=3, sticky='ew')
        self.train_btn.grid(row=7, column=0, columnspan=3, sticky='ew')

        # Create and place training label
        self.progress_label = tk.Label(self.board_frame, height=1, width=6,
                                       text="Agent is not treined yet.",
                                       font='SegoeUI 10', fg=self.red_col, bg=self.dark_blue_col)

        self.progress_label.grid(row=8, column=0, columnspan=3, sticky="ew")

    def updateBoardBySetting(self, setting):
        for i in range(9):
            if setting[i] is None:
                board_buttons[i].configure(
                    text=" ", bg=self.dark_blue_col, fg=self.honeydew_col, state=tk.NORMAL)
            else:
                board_buttons[i].configure(
                    text=setting[i], bg=self.navy_blue_col, fg=self.red_col, state=tk.DISABLED)

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
            text=sign, bg=self.navy_blue_col, fg=self.red_col, state=tk.DISABLED)

    # disable all buttons on the screen
    def setGuiToStartTraining(self):
        for i in range(9):
            board_buttons[i].configure(state=tk.DISABLED)
        self.reset_btn.configure(
            bg=self.dark_blue_col, fg=self.gray_col, state=tk.DISABLED)
        self.train_btn.configure(
            bg=self.dark_blue_col, fg=self.gray_col, state=tk.DISABLED)
        self.updateStatusLabelText("Training in progress")
        self.progress_label.configure(fg=self.yellow_col)
        self.status_label.update()

    # enable all buttons on the screen
    def setGuiToEndTraining(self):
        for i in range(9):
            board_buttons[i].configure(
                bg=self.dark_blue_col, fg=self.honeydew_col, state=tk.NORMAL)
        self.reset_btn.configure(
            bg=self.yellow_col, fg=self.dark_blue_col, state=tk.NORMAL)
        self.train_btn.configure(
            bg=self.red_col, fg=self.dark_blue_col, state=tk.NORMAL)
        self.updateStatusLabelText(
            "Training ended.\nPress restart to start game")
        self.progress_label.configure(fg=self.red_col)

    def setResetBtnToDefaultColor(self):
        self.reset_btn.configure(bg=self.red_col, fg=self.dark_blue_col)

    def build_traning_modal(self):

        modal = TrainingModal(
            self.master,
            self.setGuiToStartTraining,
            self.setGuiToEndTraining
        )


class TrainingModal(tk.Toplevel):

    def __init__(self, master, lock_gui: Callable, unlock_gui: Callable):

        self.main_gui_master = master
        self.__lock_gui_function = lock_gui
        self.__unlock_gui_function = unlock_gui

        # Training options.
        self.training_options = {
            "QQ": "Q Agent vs. Q Agent",
            "RQ": "Random vs. Q Agent"
        }

        self.base = tk.Toplevel()
        self.base.geometry("800x250")
        self.base.resizable(width=False, height=False)

        self.base.protocol("WM_DELETE_WINDOW", self.__onClosing)

        self.base.title = "Agent training window"

        # Locking parent window when TrainingModal is created.
        self.__lock_gui_function()

        # Creating the frame to place all the widgets in.
        self.modal_frame = self.__build_frame()

        # Building the dropdown modal component
        self.__build_dropdown()

        # self.testLabel()

    def __print_test(self):
        print(3*'\n', "TEST", 3*'\n')

    def testLabel(self):
        label = tk.Label(self.modal_frame, text="test")
        label.grid(row=0, column=1)
        # label.pack()

    # Bulding the
    def __build_frame(self) -> tk.Frame:

        frame = tk.Frame(self.base)
        frame.grid(row=0, column=0, columnspan=2, rowspan=3, sticky='ew')

        return frame

    # Builds the dropdown component of the training modal.
    def __build_dropdown(self):

        options = tk.StringVar(self.main_gui_master)

        # Default value is 'q agent vs q agent'.
        options.set(self.training_options['QQ'])

        # Creating the dropdown element
        dropdown = tk.OptionMenu(self.modal_frame,
                                 options,
                                 *self.training_options.values()
                                 )

        # Placing the dropdown in the grid.
        dropdown.grid(row=0, column=0)

        # dropdown.pack()

    # Event callback that happens on closing the Training modal.
    def __onClosing(self):
        """Event that handles destroying TrainingModal and 
           unlocking parent UI window on TrainingModal close
           event.

        """
        self.base.destroy()
        self.__unlock_gui_function()
