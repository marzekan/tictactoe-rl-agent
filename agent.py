import random
import pickle
from brain import QLearning


class Agent:
    def __new__(cls, setting, agentSign, strategy):
        if strategy not in ['random', 'q']:
            print("Passed agent strategy is not correct, must be: 'random' or 'q'.")
            return None
        else:
            return object.__new__(cls)

    def __init__(self, setting, agentSign, strategy):

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
    def updateStates(self, new_states):
        pass

    # Updates available positions every agent move.
    def updateAvailablePos(self, positions):
        pass

    def makeRandomMove(self):
        return self.actions[random.randrange(0, len(self.actions))]

    def makeMove(self):
        return self.strategy.chooseBestMove(self.sign, self.actions, self.states)

    def beRewarded(self, value):
        self.strategy.calculateReward(value)

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
