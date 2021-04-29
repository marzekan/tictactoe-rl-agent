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

        '''
            Implementation od simulateGame method is 
            dynamically set based on passed agent_strategies 
            parameter.

            This way we can always call the same 'simulateGame'
            method in other functions without needing to worry
            about what game strategy agents use.
        '''
        if agent_strategies == "QQ":
            self.agentX.setStrategy("q")
            self.agentO.setStrategy("q")

            self.simulateGame = self.__simulateQQGame

        elif agent_strategies == "RQ":
            self.simulateGame = self.__simulateRQGame

    # Agents play agains the agent with same strategy.
    def __simulateQQGame(self):

        self.board.resetBoard()

        while self.board.isGameOver() is False:

            self.agentX.updateStates(self.board.setting)
            self.agentX.updateAvailablePos()
            posX = self.agentX.makeMove()
            self.board.setSignToPos(posX, self.agentX.sign)

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

            self.agentO.updateStates(self.board.setting)
            self.agentO.updateAvailablePos()
            posO = self.agentO.makeMove()
            self.board.setSignToPos(posO, self.agentO.sign)

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

        self.board.resetBoard()

        self.agentX.setStrategy("q")
        self.agentO.setStrategy("q")

        # In this game agent takes turn playing against the random agent.
        agent_rand = Agent(self.board.setting, "O", "random")

        while self.board.isGameOver() is False:

            self.agentX.updateStates(self.board.setting)
            self.agentX.updateAvailablePos()

            posX = self.agentX.makeMove()
            self.board.setSignToPos(posX, self.agentX.sign)

            if self.board.checkWinner() == self.agentX.sign:
                self.agentX.beRewarded(1)

            elif self.board.checkWinner() == agent_rand.sign:
                self.agentX.beRewarded(-1)
            else:
                self.agentX.beRewarded(0.1)

            if self.board.isGameOver() is True:
                break

            agent_rand.updateStates(self.board.setting)
            agent_rand.updateAvailablePos()
            posRand = agent_rand.makeMove()

            self.board.setSignToPos(posRand, agent_rand.sign)

            if self.board.checkWinner() == agent_rand.sign:
                self.agentX.beRewarded(-1)

            elif self.board.checkWinner() == self.agentX.sign:
                self.agentX.beRewarded(1)

            else:
                self.agentX.beRewarded(0.1)

        agent_rand.strategy.resetHistoricStates()
        self.agentX.strategy.resetHistoricStates()

        self.board.resetBoard()

        agent_rand.switchSign()

        while self.board.isGameOver() is False:

            agent_rand.updateStates(self.board.setting)
            agent_rand.updateAvailablePos()
            posRand = agent_rand.makeMove()

            self.board.setSignToPos(posRand, agent_rand.sign)

            if self.board.checkWinner() == agent_rand.sign:
                self.agentO.beRewarded(-1)

            elif self.board.checkWinner() == self.agentO.sign:
                self.agentO.beRewarded(1)
            else:
                self.agentO.beRewarded(0.1)

            if self.board.isGameOver() is True:
                break

            self.agentO.updateStates(self.board.setting)
            self.agentO.updateAvailablePos()
            posO = self.agentO.makeMove()
            self.board.setSignToPos(posO, self.agentO.sign)

            if self.board.checkWinner() == self.agentO.sign:
                self.agentO.beRewarded(1)

            elif self.board.checkWinner() == agent_rand.sign:
                self.agentO.beRewarded(-1)

            else:
                self.agentO.beRewarded(0.1)

        self.agentO.strategy.resetHistoricStates()
        agent_rand.strategy.resetHistoricStates()

    def saveAgents(self):

        now = datetime.now()
        datetime_str = now.strftime("%m_%d_%Y_%H_%M_%S")

        self.agentO.saveQStates(
            f"saves/trained_O_{str(self.agent_strategies)}_{datetime_str}.pkl")
        self.agentX.saveQStates(
            f"saves/trained_X_{str(self.agent_strategies)}_{datetime_str}.pkl")
