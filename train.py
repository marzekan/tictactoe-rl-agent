from agent import Agent
from rules import Board

from time import sleep


class Simulation:

    def __new__(cls, agent_strategies):
        if agent_strategies not in ["RR", "RQ", "QR", "QQ"]:
            print("Wrong agent behaviour passed, must be: 'RR', 'RQ', 'QR' or 'QQ'.")
            return None
        else:
            return object.__new__(cls)

    def __init__(self, agent_strategies):

        self.board = Board()

        '''
            Simulation setting can be one of 3 states:
                RR (Random agent vs. Random agent)
                RQ (Random agent vs. Q-learning agent)
                QQ (Q-learning agent vs. Q-learning agent)

            States represent learning strategy of agent that
            are being simulated.
        '''

        # try:

        # except Exception as e:

        strategy_X = ""
        strategy_O = ""

        if agent_strategies == "RR":
            strategy_X = "random"
            strategy_O = "random"

        elif agent_strategies == "RQ":
            strategy_X = "random"
            strategy_O = "q"

        elif agent_strategies == "QR":
            strategy_X = "q"
            strategy_O = "random"

        elif agent_strategies == "QQ":
            strategy_X = "q"
            strategy_O = "q"

        self.agentX = Agent(self.board.setting, "X", strategy=strategy_X)
        self.agentO = Agent(self.board.setting, "O", strategy=strategy_O)

    def simulateGame(self):

        self.board.resetBoard()

        while self.board.isGameOver() is False:

            self.agentX.states = self.board.setting
            self.agentX.actions = self.agentX.getAvailablePos()
            posX = self.agentX.makeMove()
            self.board.setting[posX] = self.agentX.sign

            if self.board.checkWin() == self.agentX.sign:
                self.agentX.beRewarded(1)
                self.agentO.beRewarded(-1)

            elif self.board.checkWin() == self.agentO.sign:
                self.agentX.beRewarded(-1)
                self.agentO.beRewarded(1)
            else:
                self.agentX.beRewarded(0.1)
                self.agentO.beRewarded(0.1)

            if self.board.isGameOver() is True:
                break

            self.agentO.states = self.board.setting
            self.agentO.actions = self.agentO.getAvailablePos()
            posO = self.agentO.makeMove()
            self.board.setting[posO] = self.agentO.sign

            if self.board.checkWin() == self.agentO.sign:
                self.agentO.beRewarded(1)
                self.agentX.beRewarded(-1)

            elif self.board.checkWin() == self.agentX.sign:
                self.agentO.beRewarded(-1)
                self.agentX.beRewarded(1)

            else:
                self.agentO.beRewarded(0.1)
                self.agentX.beRewarded(0.1)

        self.agentO.strategy.resetHistoricStates()
        self.agentX.strategy.resetHistoricStates()
