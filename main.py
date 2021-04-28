from time import sleep
from rules import Board
from agent import Agent
from train import Simulation
from game_gui import GameGUI

import os


class GameBoard():

    def __init__(self):
        self.board = Board()
        self.playerSign = "X"
        self.agentSign = "O"
        self.agent = Agent(self.board.setting, self.agentSign, strategy="q")

        self.gui = GameGUI()
        self.gui.createBoard(self.playerSetMove, self.reset,
                             self.agentSign, self.playerSign)

        self.checkIfAgentTrained()

    # When player clicks on the board. Area is marked with players sign.
    # Afterwards player signals agent to play if the game is not over.
    def playerSetMove(self, buttonNumber):
        self.board.setSignToPos(buttonNumber, self.playerSign)
        self.gui.setSignIntoBoardPosition(self.playerSign, buttonNumber)

        if self.checkGameOver():
            return

        self.agentSetMove()

    def agentSetMove(self):
        sleep(0.2)

        self.agent.updateStates(self.board.setting)
        self.agent.updateAvailablePos()

        new_agent_position = self.agent.makeMove()

        self.board.setSignToPos(new_agent_position, self.agentSign)

        self.gui.updateBoardBySetting(self.board.setting)

        self.checkGameOver()

    def checkGameOver(self):
        if self.board.isGameOver() is True:

            winner = self.board.checkWinner()

            self.gui.disableAllBoardButtons()

            if winner is None:
                statusText = "It's a draw."

            else:
                statusText = "Game over!\nThe winner is:" + winner

            self.gui.updateStatusLabelText(statusText)
            return True
        else:
            return False

    # resets the board and checks if the agent is trained
    def reset(self):
        self.board.resetBoard()
        self.gui.updateBoardBySetting(self.board.setting)
        self.gui.updateStatusLabelText(
            "You: " + self.playerSign + "\nAgent: " + self.agentSign)
        self.gui.setResetBtnToDefaultColor()
        self.checkIfAgentTrained()

    # start training the agent
    def startTraining(self):
        self.board.resetBoard()
        self.gui.setGuiToStartTraining()

        simulation = Simulation("RQ")

        if simulation is not None:

            numberOfIterations = 2000

            for i in range(numberOfIterations):
                simulation.simulateGame()
                self.trainProgress(i, numberOfIterations)

            simulation.saveAgents()

            self.gui.setGuiToEndTraining()
            self.checkIfAgentTrained()

    # show iteration E.G. "00% 128/10000"
    def trainProgress(self, current, numberOfIterations):
        percentage = "{0:.0f}%".format(current/numberOfIterations * 100)
        progressMessage = str(percentage) + " " + \
            str(current) + "/" + str(numberOfIterations)
        self.gui.updateProgressLabel(progressMessage, current, 500)
        print(str(percentage), " ", str(current), "/", str(numberOfIterations))

    # check if .pkl file exists
    def checkIfAgentTrained(self):

        files = os.listdir('.')
        save_file = ""

        for file in files:
            if "trained_O" in file:
                save_file = file
        try:
            self.agent.loadQStates(save_file)
            self.agent.turnOffExploration()

        except IOError:
            print("File not accessible")
            return

        self.gui.updateProgressLabelText("Agent is trained and ready to play.")

        # if filesExists is True:
        #     self.gui.updateProgressLabelText(
        #         "Agent is trained and ready to play.")
        # return filesExists

    # def openTrainingModal(self):
    #     self.gui.build_traning_modal()


if __name__ == "__main__":
    game = GameBoard()
    game.gui.startGui()
