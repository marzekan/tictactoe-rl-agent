import random
import pickle
from brain import QLearning, Random


class Agent:
    def __new__(cls, setting, agentSign, strategy="random"):
        if strategy not in ['random', 'q']:
            print("Passed agent strategy is not correct, must be: 'random' or 'q'.")
            return None
        else:
            return object.__new__(cls)

    def __init__(self, setting, agentSign, strategy="random"):

        self.states = setting
        self.sign = agentSign

        if strategy == "q":
            self.strategy = QLearning()
        elif strategy == "random":
            self.strategy = Random()

        self.actions = self.getAvailablePos()

    # Gets all possible available positions.
    def getAvailablePos(self) -> list:
        actions = []
        for i in range(len(self.states)):
            if self.states[i] == None:
                actions.append(i)

        return actions

    # Updates agent states on every agent move.
    def updateStates(self, board_setting):
        self.states = board_setting

    # Updates available positions every agent move.
    def updateAvailablePos(self):
        self.actions = self.getAvailablePos()

    # Agent makes a move by choosing the best move from current strategy.
    def makeMove(self) -> int:
        return self.strategy.chooseBestMove(self.sign, self.actions, self.states)

    # Reward agent if he is using the Q-learning strategy.
    def beRewarded(self, value):
        self.strategy.calculateReward(value)

    # Sets exploration_rate to 0 so that agent doesn't make random moves.
    def turnOffExploration(self):
        self.strategy.exploration_rate = 0

    # Sets agent strategy.
    def setStrategy(self, strategy):
        if strategy == "random":
            self.strategy = Random()
        elif strategy == "q":
            self.strategy = QLearning()
        else:
            print("Wrong strategy passed, must be: 'random' or 'q'.")
            return

    # Saves Q values to pickle file.
    def saveQStates(self, file_name):
        Qvalues = self.strategy.states
        with open(file_name, "wb") as file:
            pickle.dump(Qvalues, file)

    # Loads Q values from pickle file.
    def loadQStates(self, file_name):
        with open(file_name, "rb") as file:
            Qvalues = pickle.load(file)
        self.strategy.states = Qvalues
