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
        self.agentScore = 0
        self.playerScore = 0

        score = (self.playerScore, self.agentScore)

        self.agent = Agent(self.board.setting, self.agentSign, strategy="q")

        self.game_name = "New (random)"

        self.gui = GameGUI()
        self.gui.createBoard(self.playerSetMove, self.reset,
                             self.agentSign, self.playerSign, self.loadGame, self.game_name, score)

        self.checkIfAgentTrained()

    # Makes agent play first if his sign is 'X'.
    def decideFirstPlayer(self):
        if self.agentSign == "X":
            self.agentSetMove()

    # When player clicks on the board. Area is marked with players sign.
    # Afterwards player signals agent to play if the game is not over.
    def playerSetMove(self, buttonNumber):
        self.board.setSignToPos(buttonNumber, self.playerSign)
        self.gui.setSignIntoBoardPosition(self.playerSign, buttonNumber)

        if self.checkGameOver():
            self.playerScore += 1
            return

        self.agentSetMove()

    def agentSetMove(self):
        sleep(0.2)

        self.agent.updateStates(self.board.setting)
        self.agent.updateAvailablePos()

        new_agent_position = self.agent.makeMove()

        self.board.setSignToPos(new_agent_position, self.agentSign)

        self.gui.updateBoardBySetting(self.board.setting)

        if self.checkGameOver():
            self.agentScore += 1
            return

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

        # Switch player signs.
        self.playerSign = "O" if self.playerSign == "X" else "X"
        self.agentSign = "O" if self.playerSign == "X" else "X"

        score = (self.playerScore, self.agentScore)

        if self.agent.game_loaded:
            self.agent.setQvalues(self.agentSign)

        self.board.resetBoard()

        self.gui.updateBoardBySetting(self.board.setting)
        self.gui.updateStatusLabelText(
            "You: " + self.playerSign
                    + "\nAgent: " + self.agentSign
                    + "\n"
                    + "\nPlaying: " + self.game_name
                    + "\n\n"
                    + "Score:\n"
                    + f"You: {score[0]} - Agent: {score[1]}"
        )
        self.gui.setResetBtnToDefaultColor()
        self.checkIfAgentTrained()

        self.decideFirstPlayer()

    def loadGame(self, folder):

        if folder == "":
            return

        folder = folder.replace("/", "\\")

        self.game_name = folder.split("\\")[-1]

        try:
            self.agent.loadQStates(f"{folder}")
            self.agent.turnOffExploration()

        except IOError:
            print("File not accessible")
            return

        self.gui.updateProgressLabelText("Agent is trained and ready to play.")
        self.gui.updateStatusLabelText("Agent loaded. Restart to play.")
        self.gui.disableAllBoardButtons()
        self.gui.hightlightResetBtn()
        self.gui.setLoadBtnToDefaultColor()

        self.agentScore = 0
        self.playerScore = 0

    # check if .pkl file exists
    def checkIfAgentTrained(self):

        if self.agent.strategy.states == {}:
            self.gui.updateProgressLabelText(
                "Agent not trained. He will play random moves.")
            return


if __name__ == "__main__":
    game = GameBoard()
    game.gui.startGui()
