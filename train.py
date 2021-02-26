from agent import Agent
from rules import Board

from time import sleep
from datetime import datetime


class Simulation:
    '''
        Class constructor - returns empty object (None)
        if wrong agent strategies parameters have been
        passed.
        Else objects is correctly instantiated.
    '''
    def __new__(cls, agent_strategies):
        if agent_strategies not in ["RQ", "QQ"]:
            print("Wrong agent behaviour passed, must be: 'RQ' or 'QQ'.")
            return None
        else:
            return object.__new__(cls)

    def __init__(self, agent_strategies):
        self.board = Board()
        self.agent_strategies = agent_strategies

        self.agentX = Agent(self.board.setting, "X")
        self.agentO = Agent(self.board.setting, "O")

        if agent_strategies == "QQ":
            self.simulateGame = self.__simulateQQGame

        elif agent_strategies == "RQ":
            self.simulateGame = self.__simulateRQGame

        '''
            Simulation setting can be one of 3 states:
                RR (Random agent vs. Random agent)
                RQ (Random agent vs. Q-learning agent)
                QQ (Q-learning agent vs. Q-learning agent)

            States represent learning strategy of agent that
            are being simulated.
        '''

        # strategy_X = ""
        # strategy_O = ""

        # if agent_strategies == "RQ":
        #     strategy_X = "random"
        #     strategy_O = "q"

        # elif agent_strategies == "QQ":
        #     strategy_X = "q"
        #     strategy_O = "q"

        # self.agentX = Agent(self.board.setting, "X", strategy=strategy_X)
        # self.agentO = Agent(self.board.setting, "O", strategy=strategy_O)

    # Agents play agains the agent with same strategy.
    def __simulateQQGame(self):

        print("QQ igra")

        self.board.resetBoard()

        self.agentX.setStrategy("q")
        self.agentO.setStrategy("q")

        while self.board.isGameOver() is False:

            self.agentX.states = self.board.setting
            self.agentX.actions = self.agentX.getAvailablePos()
            posX = self.agentX.makeMove()
            self.board.setting[posX] = self.agentX.sign

            if self.board.checkWinner() == self.agentX.sign:
                self.agentX.beRewarded(1)
                self.agentO.beRewarded(-1)

            elif self.board.checkWinner() == self.agentO.sign:
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

            if self.board.checkWinner() == self.agentO.sign:
                self.agentO.beRewarded(1)
                self.agentX.beRewarded(-1)

            elif self.board.checkWinner() == self.agentX.sign:
                self.agentO.beRewarded(-1)
                self.agentX.beRewarded(1)

            else:
                self.agentO.beRewarded(0.1)
                self.agentX.beRewarded(0.1)

        self.agentO.strategy.resetHistoricStates()
        self.agentX.strategy.resetHistoricStates()

    # Agents play againt agent with different strategy.
    def __simulateRQGame(self):

        print("RQ igra")

        self.board.resetBoard()

        self.agentX.setStrategy("random")
        self.agentO.setStrategy("q")

        while self.board.isGameOver() is False:

            self.agentX.states = self.board.setting
            self.agentX.actions = self.agentX.getAvailablePos()

            posX = self.agentX.makeMove()
            self.board.setting[posX] = self.agentX.sign

            if self.board.checkWinner() == self.agentX.sign:
                self.agentX.beRewarded(1)
                self.agentO.beRewarded(-1)

            elif self.board.checkWinner() == self.agentO.sign:
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

            if self.board.checkWinner() == self.agentO.sign:
                self.agentO.beRewarded(1)
                self.agentX.beRewarded(-1)

            elif self.board.checkWinner() == self.agentX.sign:
                self.agentO.beRewarded(-1)
                self.agentX.beRewarded(1)

            else:
                self.agentO.beRewarded(0.1)
                self.agentX.beRewarded(0.1)

        self.agentO.strategy.resetHistoricStates()
        self.agentX.strategy.resetHistoricStates()

        self.board.resetBoard()

        self.agentX.setStrategy("q")
        self.agentO.setStrategy("random")

        while self.board.isGameOver() is False:

            self.agentX.states = self.board.setting
            self.agentX.actions = self.agentX.getAvailablePos()

            posX = self.agentX.makeMove()
            self.board.setting[posX] = self.agentX.sign

            if self.board.checkWinner() == self.agentX.sign:
                self.agentX.beRewarded(1)
                self.agentO.beRewarded(-1)

            elif self.board.checkWinner() == self.agentO.sign:
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

            if self.board.checkWinner() == self.agentO.sign:
                self.agentO.beRewarded(1)
                self.agentX.beRewarded(-1)

            elif self.board.checkWinner() == self.agentX.sign:
                self.agentO.beRewarded(-1)
                self.agentX.beRewarded(1)

            else:
                self.agentO.beRewarded(0.1)
                self.agentX.beRewarded(0.1)

        self.agentO.strategy.resetHistoricStates()
        self.agentX.strategy.resetHistoricStates()

    # Simulates one game.
    def simulateGame(self):
        pass

    def saveAgents(self):

        now = datetime.now()
        datetime_str = now.strftime("%m_%d_%Y_%H_%M_%S")

        self.agentO.saveQStates(
            f"trained_O_{str(self.agentO.strategy)}_{datetime_str}.pkl")
        self.agentX.saveQStates(
            f"trained_X_{str(self.agentX.strategy)}_{datetime_str}.pkl")
