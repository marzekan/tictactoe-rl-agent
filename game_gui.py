import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import HORIZONTAL
from typing import Callable
from tkinter.ttk import Progressbar

from train import Simulation

board_buttons = []


class GameGUI(tk.Frame):
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.defineColorsAndFont()
        self.master.title("Tic Tac Toe")
        self.master.configure(background='#00022E')
        self.master.resizable(width=False, height=False)

        # These values will be passed to agent training simulation.
        self.iter_num = 0
        self.strategy = ""

    # Returns tuple (<iteration number>, <strategy>)
    def getTrainingValues(self):
        return (self.iter_num, self.strategy)

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

    def createBoard(self, playerSetMove, reset, agent_sign, player_sign, load_game, game_name, score):

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
        self.status_label = tk.Label(self.board_frame, height=8, width=6,
                                     text="You: " + player_sign
                                     + "\nAgent: " + agent_sign
                                     + "\n"
                                     + "\nPlaying: " + game_name
                                     + "\n\n"
                                     + "Score:\n"
                                     + f"You: {score[0]} - Agent: {score[1]}",
                                     font=self.font_normal_bold, fg=self.red_col, bg=self.dark_blue_col)

        self.status_label.grid(row=5, column=0, columnspan=3, sticky="ew")

        # Create and place command buttons
        self.reset_btn = tk.Button(self.board_frame, height=2, width=16, text='RESET GAME',
                                   font=self.font_normal_bold, bg=self.red_col, fg=self.dark_blue_col, command=lambda: reset())
        self.train_btn = tk.Button(self.board_frame, height=2, width=16, text='TRAIN AGENT',
                                   font=self.font_normal_bold, bg=self.red_col, fg=self.dark_blue_col, command=lambda: self.build_traning_modal())
        self.load_btn = tk.Button(self.board_frame, height=2, width=16, text="LOAD AGENT",
                                  font=self.font_normal_bold, bg=self.red_col, fg=self.dark_blue_col, command=lambda: self.open_load_dialog(load_game))

        self.reset_btn.grid(row=6, column=0, columnspan=3, sticky='ew')
        self.train_btn.grid(row=7, column=0, columnspan=3, sticky='ew')
        self.load_btn.grid(row=8, column=0, columnspan=3, sticky='ew')

        # Create and place training label
        self.progress_label = tk.Label(self.board_frame, height=1, width=6,
                                       text="Agent is not trained yet.",
                                       font='SegoeUI 10', fg=self.red_col, bg=self.dark_blue_col)

        self.progress_label.grid(row=9, column=0, columnspan=3, sticky="ew")

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
        self.load_btn.configure(
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
            bg=self.red_col, fg=self.dark_blue_col, state=tk.NORMAL)

        self.train_btn.configure(
            bg=self.red_col, fg=self.dark_blue_col, state=tk.NORMAL)

        self.load_btn.configure(
            bg=self.yellow_col, fg=self.dark_blue_col, state=tk.NORMAL)

        self.updateStatusLabelText(
            "Training ended.\nLoad Agent to play him.")

        self.progress_label.configure(fg=self.red_col)

    def setResetBtnToDefaultColor(self):
        self.reset_btn.configure(bg=self.red_col, fg=self.dark_blue_col)

    def setLoadBtnToDefaultColor(self):
        self.load_btn.configure(bg=self.red_col, fg=self.dark_blue_col)

    def hightlightResetBtn(self):
        self.reset_btn.configure(bg=self.yellow_col, fg=self.dark_blue_col)

    def build_traning_modal(self):

        modal = TrainingModal(
            self.master,
            self.setGuiToStartTraining,
            self.setGuiToEndTraining
        )

    def open_load_dialog(self, load_game_function):
        load_dialog = filedialog.askdirectory(
            initialdir="saves/"
        )

        save_folder = load_dialog.title()

        load_game_function(save_folder)


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

        # Training strategy information
        self.strategy_info_text = {
            "Q Agent vs. Q Agent": "Agent will learn by playing against itself using the Q - Learning strategy.",
            "Random vs. Q Agent": "Agent will try to learn by playing an agent who only makes random moves (without Q-learning)."
        }

        # Default info label text.
        self.info_label_default = "Select strategy and number of iterations"

        # Info about what training iterations represent.
        self.iteration_info_text = "Represents the number of games agent will play agains itself before playing you."

        # Progress label text.
        self.progress_text = ""

        self.base = tk.Toplevel()
        self.base.geometry("450x375")
        self.base.resizable(width=False, height=False)
        self.base.configure(background='white')

        self.base.protocol("WM_DELETE_WINDOW", self.__onClosing)

        self.base.title("Agent training window")

        # Locking parent window when TrainingModal is created.
        self.__lock_gui_function()

        # Creating the frame to place all the widgets in.
        self.modal_frame = self.__create_frame()

        # Declaring the strategy info label.
        self.strategy_info_label: tk.Label

        # User selected strategy.
        self.selected_strategy: str

        # Number of training iterations that the user has selected.
        self.selected_num_of_iter: int

        # Create feedback label.
        self.info_label = self.__create_info_label()

        # Create button to start the training.
        self.train_btn = self.__build_train_button()

        # Building the strategy info label and frame.
        self.__build_strategy_info()

        # Building the dropdown modal component.
        self.__build_dropdown(self.strategy_info_label)

        # Building iterations selection textbox.
        self.__build_iterations_textbox()

        # Building iterations info label frame.
        self.__build_iterations_info()

        # Frame that holds progress bar and label.
        self.progress_frame = self.__build_progress_frame()

        # Shows training progress.
        self.progress_bar = self.__build_progress_bar()

        # Shows training progress but in text.
        self.progress_label = self.__build_progress_label()

    # =========== TRAINING METHODS =========== #

    # Trains agents.
    def train(self):

        self.info_label.configure(text="Training...")

        self.train_btn.configure(
            bg="white",
            fg="forest green",
            text="Training...",
            state=tk.DISABLED,
        )

        simulation = Simulation(self.strategy)

        self.progress_bar['maximum'] = self.iter_num

        if simulation is not None:

            for i in range(self.iter_num):
                simulation.simulateGame()

                if i % 100 == 0 or i+1 == self.iter_num:

                    self.progress_label.configure(
                        text=f"{i} / {self.iter_num}")

                    self.progress_bar['value'] = i
                    self.progress_bar.update()

            self.progress_label.configure(
                text=f"{self.iter_num} / {self.iter_num}")

        self.train_btn.configure(
            state=tk.NORMAL,
            bg="forest green",
            fg="white",
            text="Train!"
        )

        self.info_label.configure(text="Done!", fg="green")

        direc = filedialog.asksaveasfilename(
            defaultextension=".pkl",
            filetypes=[("pickle files", "*.pkl")],
            initialdir="saves/",
            title="new_agent"
        )

        filename = direc.title()

        simulation.saveAgents(filename)

        self.__onClosing()

    # Gets the number of training iterations inputed by the user.
    def getNumberOfIterations(self) -> int:

        if not self.selected_num_of_iter:
            return

        # Converts passed text to string.
        iter_num = str(self.selected_num_of_iter)

        # Entry isn't number or larger then 0.
        if not iter_num.isdecimal():

            print("Iterations must be a number and larger then 0.")

            self.info_label.configure(
                foreground="red",
                text="Iterations must be a number and larger then 0."
            )

            return

        self.info_label.configure(
            foreground="black",
            text=self.info_label_default
        )

        return int(iter_num)

    # Gets user selected strategy.
    def getSelectedStrategy(self) -> str:

        for key, value in self.training_options.items():
            if value == self.selected_strategy:
                strategy = key

        return strategy

    # Train button callback. Starts agent training.
    def start_training(self):

        self.iter_num = self.getNumberOfIterations()
        self.strategy = self.getSelectedStrategy()

        data = (self.iter_num, self.strategy)

        if not all(data):
            print("Some values are None.")
            return

        self.train()

    # ============== COMPONENTS ============== #

    # Gives user feedback about the app.
    def __create_info_label(self):

        info_label = tk.Label(
            self.modal_frame,
            text=self.info_label_default,
            bg="white"
        )

        info_label.grid(
            row=12, column=0,
            columnspan=4,
            sticky="ew",
            pady=(55, 0)
        )

        return info_label

    # Build strategy info label.
    def __build_strategy_info(self):
        """Builds the label frame and label that describe the learning strategy
           selected in the dropdown.

           This component aims to explain user options back to the user.
        """
        strategy_info_frame = tk.LabelFrame(
            self.modal_frame,
            text="Strategy info",
            bg="white",
            fg="green"
        )

        strategy_info_frame.grid(
            row=0, column=2,
            rowspan=4,
            padx=(50, 5),
            pady=(5, 5)
        )

        self.strategy_info_label = tk.Label(
            strategy_info_frame,
            width=25,
            height=5,
            text=next(iter(self.strategy_info_text.values())),
            relief="flat",
            background="white",
            wraplength=150,
            justify="left",
        )

        self.strategy_info_label.grid(
            row=0, column=2,
            rowspan=4,
        )

    # Build textbox where user enters iteration number.
    def __build_iterations_textbox(self):

        # Creating title label for the iteration entry.
        iter_label = tk.Label(self.modal_frame,
                              text="Enter number of iterations:",
                              bg="white"
                              )

        # Placing dropdown menu on the modal frame grid.
        iter_label.grid(
            row=5, column=0,
            padx=(5, 5),
            # pady=(0, 10)
        )

        # Frame containing label and Entry box for iteration number.
        iter_frame = tk.Frame(self.modal_frame, bg="white")
        iter_frame.grid(
            row=6, column=0,
            columnspan=2,
            rowspan=1,
            sticky="ew",
            padx=(10, 0),
            pady=(0, 40)
        )

        # Iteration entrybox prompt.
        iter_entry_label = tk.Label(
            iter_frame,
            text="Num. iter:",
            bg="white"
        )

        iter_entry_label.grid(
            row=0, column=0,
            padx=(5, 0),
            pady=(0, 20)
        )

        # Variable that stores Entry text that is shown to the user.
        entry_text = tk.StringVar()
        entry_text.set("200")

        def on_change(entry_text):
            self.selected_num_of_iter = entry_text.get()
            return True

        entry_text.trace_add("write", lambda name, index,
                             mode, sv=entry_text: on_change(entry_text))

        # Entry box for number of iterations.
        iter_entry = tk.Entry(
            iter_frame,
            width=13,
            relief="flat",
            bg="ghost white",
            fg="navy blue",
            textvariable=entry_text,
        )

        iter_entry.grid(
            row=0, column=1,
            padx=(5, 0),
            pady=(0, 20)
        )

        # Set number of training iterations to default begin value.
        self.selected_num_of_iter = entry_text.get()

    # Build iteration info label frame.
    def __build_iterations_info(self):

        strategy_info_frame = tk.LabelFrame(
            self.modal_frame,
            text="Iterations info",
            bg="white",
            fg="navy blue",
        )

        strategy_info_frame.grid(
            row=4, column=2,
            rowspan=4,
            padx=(50, 5),
            pady=(5, 5)
        )

        self.strategy_info_label = tk.Label(
            strategy_info_frame,
            width=25,
            height=5,
            text=self.iteration_info_text,
            relief="flat",
            background="white",
            wraplength=150,
            justify="left",
        )

        self.strategy_info_label.grid(
            row=4, column=2,
            rowspan=4,
        )

    # Bulding the modal frame to place other widgets.
    def __create_frame(self) -> tk.Frame:
        """Builds tkinter Frame that will contain all widgets of
           the modal.
        """
        frame = tk.Frame(self.base, bg="white")
        frame.grid(row=0,
                   column=0,
                   columnspan=8,
                   rowspan=12,
                   sticky='ew')

        frame.columnconfigure(0, minsize=30)

        return frame

    # Builds the dropdown component of the training modal.
    def __build_dropdown(self, info_label):
        """Builds the dropdown menu where the user can an agent
            training strategy.
        """

        # Creating title label for the dropdown menu.
        dropdown_label = tk.Label(self.modal_frame,
                                  text="Pick agent training strategy:",
                                  bg="white"
                                  )
        # Placing dropdown menu on the modal frame grid.
        dropdown_label.grid(
            row=0, column=0,
            padx=(5, 5),
            pady=(5, 0)
        )

        dropdown_options = tk.StringVar(self.main_gui_master)

        # Default value is 'q agent vs q agent'.
        dropdown_options.set(self.training_options['QQ'])

        # Creating the dropdown element
        dropdown = tk.OptionMenu(self.modal_frame,
                                 dropdown_options,
                                 *self.training_options.values(),
                                 )

        dropdown.configure(
            relief="flat",
            bg="white",
            width=20,
            fg="green"
        )

        # Placing the dropdown in the grid.
        dropdown.grid(
            row=1, column=0,
            padx=(10, 0),
            pady=(0, 50),
            sticky="ew"
        )

        self.selected_strategy = dropdown_options.get()

        # Inline function that updates the info label based on
        # the strategy selected.
        def update_info_label(*args):

            user_selection = dropdown_options.get()
            self.selected_strategy = user_selection

            for option in self.training_options.values():
                if option == user_selection:
                    info_label.configure(text=self.strategy_info_text[option])

        dropdown_options.trace('w', update_info_label)

    # Event callback that happens on closing the Training modal.
    def __onClosing(self):
        """Event that handles destroying TrainingModal and
           unlocking parent UI window on TrainingModal close
           event.

        """
        self.base.destroy()
        self.__unlock_gui_function()

    # Builds frame that hold progress bar and label.
    def __build_progress_frame(self):

        progress_frame = tk.LabelFrame(
            self.base,
            bg="white",
            fg="dark green",
            text="Train info",
            height=70
        )
        progress_frame.grid(
            row=10, column=1,
            columnspan=6,
            rowspan=3,
            sticky="ew",
            pady=(30, 30)
        )

        progress_frame.grid_propagate(0)

        return progress_frame

    # Build label that shows progress info.
    def __build_progress_label(self):

        progress_label = tk.Label(
            self.progress_frame,
            text="0 / 200",
            bg="white"
        )

        progress_label.grid(
            row=0, column=0,
            pady=(0, 0)
        )

        return progress_label

    # Builds progress bar showing training progress.
    def __build_progress_bar(self):

        progress_bar = Progressbar(
            self.progress_frame,
            orient=HORIZONTAL,
            length=self.selected_num_of_iter,
            mode='determinate'
        )

        progress_bar.grid(
            row=2, column=0,
            columnspan=6,
            rowspan=1,
            padx=(50, 0),
            pady=(0, 0)
        )

        return progress_bar

    # Builds training button. Starts agent training.
    def __build_train_button(self):

        train_btn = tk.Button(
            self.modal_frame,
            text="Train!",
            bg="forest green",
            fg="white",
            relief="groove",
            width=20,
            height=2,
            command=self.start_training
        )

        train_btn.grid(
            row=9, column=0,
            columnspan=4,
            rowspan=2,
            pady=(10, 20)
        )

        return train_btn
