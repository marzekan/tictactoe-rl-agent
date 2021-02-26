from time import sleep
from rules import Board
from agent import Agent
from train import Simulation
from game_gui import GameGUI


class GameBoard():

    def __init__(self):
        self.board = Board()
        self.playerSign = "X"
        self.agentSign = "O"
        self.agent = Agent(self.board.setting, self.agentSign, strategy="q")

        self.gui = GameGUI()
        self.gui.createBoard(self.playerSetMove, self.reset,
                             self.startTraining, self.agentSign, self.playerSign)

        self.checkIfAgentTrained()

    # When player clicks on the board. Area is marked with players sign.
    # Afterwards player signals agent to play if the game is not over.
    def playerSetMove(self, buttonNumber):
        self.board.setting[buttonNumber] = self.playerSign
        self.gui.setSignIntoBoardPosition(self.playerSign, buttonNumber)

        if self.checkGameOver():
            return

        self.agentSetMove()

    def agentSetMove(self):
        sleep(0.2)

        self.agent.states = self.board.setting
        self.agent.actions = self.agent.getAvailablePos()
        pos = self.agent.makeMove()
        if self.board.checkWin() == self.agent.sign:
            self.agent.beRewarded(1)
        elif self.board.checkWin() == self.playerSign:
            self.agent.beRewarded(-1)
        else:
            self.agent.beRewarded(0.1)

        self.board.setting[pos] = self.agentSign

        self.updateBoardSetting()

    def updateBoardSetting(self):
        self.gui.updateBoardBySetting(self.board.setting)
        self.checkGameOver()

    def checkGameOver(self):
        if self.board.isGameOver() is True:
            winner = self.board.checkWin()
            self.gui.disableAllBoardButtons()
            if winner is None:
                statusText = "It's a draw."
            else:
                statusText = "Game over!\nThe winner is:" + winner
            self.gui.updateStatusLabelText(statusText)
            return True
        else:
            return False

    # resets the board anc checks if the agent is trained
    def reset(self):
        self.board.resetBoard()
        self.updateBoardSetting()
        self.gui.updateStatusLabelText(
            "You: " + self.playerSign + "\nAgent: " + self.agentSign)
        self.checkIfAgentTrained()

    # start training the agent
    def startTraining(self):
        self.board.resetBoard()
        self.gui.setGuiToStartTraining()

        simulation = Simulation()
        numberOfIterations = 200000
        for i in range(numberOfIterations):
            simulation.simulateGame()
            self.trainProgress(i, numberOfIterations)

        simulation.agentO.saveQStates("trained_O.pkl")

        self.gui.setGuiToEndTraining()
        self.checkIfAgentTrained()
        pass

    # show iteration E.G. "00% 128/10000"

    def trainProgress(self, current, numberOfIterations):
        percentage = "{0:.0f}%".format(current/numberOfIterations * 100)
        progressMessage = str(percentage) + " " + \
            str(current) + "/" + str(numberOfIterations)
        self.gui.updateProgressLabel(progressMessage, current, 500)
        print(str(percentage), " ", str(current), "/", str(numberOfIterations))

    # check if .pkl file exists
    def checkIfAgentTrained(self):
        filesExists = False
        try:
            self.agent.loadQStates("trained_O.pkl")
            filesExists = True
        except IOError:
            print("File not accessible")
        if filesExists is True:
            self.gui.updateProgressLabelText(
                "Agent is trained and ready to play.")
        return filesExists


if __name__ == "__main__":
    game = GameBoard()
    game.gui.startGui()
