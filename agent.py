import random


class Agent:
    def __init__(self, setting, agentSign):

        self.states = setting
        self.sign = agentSign

        self.actions = self.getAvailablePos()

    def getAvailablePos(self) -> list:
        # Gets all possible available positions.
        return [i for i, field in enumerate(self.states) if field == None]

        # actions = []
        # for i in range(len(self.states)):
        #     if self.states[i] == None:
        #         actions.append(i)

        return actions

    def makeRandomMove(self):
        return self.actions[random.randrange(0, len(self.actions))]


# agent = Agent(setting=["x", "O", None, None, None,
#                        None, None, None, None], agentSign="O")


# # [2,3,4,5,6,7,8]

# print(agent.getAvailablePos())
# print(agent.makeRandomMove())

# []
