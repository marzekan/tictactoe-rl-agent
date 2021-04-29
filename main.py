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

        self.game_name = "New (random)"

        self.gui = GameGUI()
        self.gui.createBoard(self.playerSetMove, self.reset,
                             self.agentSign, self.playerSign, self.loadGame, self.game_name)

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
                statusText = "Game over!\nThe winner is: " + winner

            self.gui.updateStatusLabelText(statusText)
            return True
        else:
            return False

    # resets the board and checks if the agent is trained
    def reset(self):
        self.board.resetBoard()
        self.gui.updateBoardBySetting(self.board.setting)
        self.gui.updateStatusLabelText(
            "You: " + self.playerSign + "\nAgent: " + self.agentSign + "\nPlaying: " + self.game_name)
        self.gui.setResetBtnToDefaultColor()
        self.checkIfAgentTrained()

    def loadGame(self, folder):

        if folder == "":
            return

        folder = folder.replace("/", "\\")

        self.game_name = folder.split("\\")[-1]

        save_files = os.listdir(folder)

        for file in save_files:
            if f"trained_{self.agent.sign}" in file:
                save_file = file

        try:
            self.agent.loadQStates(f"{folder}\\{save_file}")
            self.agent.turnOffExploration()

        except IOError:
            print("File not accessible")
            return

        self.gui.updateProgressLabelText("Agent is trained and ready to play.")
        self.gui.updateStatusLabelText("Agent loaded. Restart to play.")
        self.gui.hightlightResetBtn()
        self.gui.setLoadBtnToDefaultColor()

    # check if .pkl file exists
    def checkIfAgentTrained(self):

        if self.agent.strategy.states == {}:
            self.gui.updateProgressLabelText(
                "Agent not trained. He will play random moves.")
            return


if __name__ == "__main__":
    game = GameBoard()
    game.gui.startGui()
