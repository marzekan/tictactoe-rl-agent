from agent import Agent
from rules import Board

from time import sleep


class Simulation:
    def __init__(self):
        self.board = Board()
        self.agentX = Agent(self.board.setting, "X", strategy="q")
        self.agentO = Agent(self.board.setting, "O", strategy="q")

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
