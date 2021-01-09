import random
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
        return [i for i, field in enumerate(self.states) if field == None]

        # actions = []
        # for i in range(len(self.states)):
        #     if self.states[i] == None:
        #         actions.append(i)

        # return actions

    def makeRandomMove(self):
        return self.actions[random.randrange(0, len(self.actions))]

    def makeMove(self):
        return self.strategy.chooseBestMove(self.sign, self.actions, self.states)

    def printQ(self):
        print("Q stanja:")
        print(self.strategy.states)

# agent = Agent(setting=["x", "O", None, None, None,
#                        None, None, None, None], agentSign="O")


# # [2,3,4,5,6,7,8]

# print(agent.getAvailablePos())
# print(agent.makeRandomMove())

# []
