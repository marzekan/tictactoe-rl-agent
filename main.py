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


if __name__ == "__main__":
    game = GameBoard()
    game.gui.startGui()
