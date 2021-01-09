import random
import pickle
from brain import QLearning


class Agent:
    def __init__(self, setting, agentSign, strategy='random'):

        self.states = setting
        self.sign = agentSign

        try:
            strategy in ['random', 'q']
        except Exception as e:
            print("KRIVI STRATEGY JE PROSLJEDEN U KONSTRUKTOR")

        if strategy == "q":
            self.strategy = QLearning()

        self.actions = self.getAvailablePos()

    def getAvailablePos(self) -> list:
        # Gets all possible available positions.
        actions = []
        for i in range(len(self.states)):
            if self.states[i] == None:
                actions.append(i)

        return actions

    def makeRandomMove(self):
        return self.actions[random.randrange(0, len(self.actions))]

    def makeMove(self):
        return self.strategy.chooseBestMove(self.sign, self.actions, self.states)

    def beRewarded(self, value):
        self.strategy.calculateReward(value)

    def printQ(self):
        print("Q stanja:")
        print(self.strategy.states)

    # Saves Q values to pickle file.
    def saveQStates(self, file_name):
        Qvalues = self.strategy.states
        with open("trained.pkl", "wb") as file:
            pickle.dump(Qvalues, file)

    # Loads Q values from pickle file.
    def loadQStates(self, file_name):
        with open("trained.pkl", "rb") as file:
            Qvalues = pickle.load(file)
        self.strategy.states = Qvalues

# agent = Agent(setting=["x", "O", None, None, None,
#                        None, None, None, None], agentSign="O")


# # [2,3,4,5,6,7,8]

# print(agent.getAvailablePos())
# print(agent.makeRandomMove())

# []
