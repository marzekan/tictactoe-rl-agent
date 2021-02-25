import random
import copy


class Random:
    def __init__(self):
        self.states = {}

    def __makeRandomMove(self, availablePos) -> int:
        return availablePos[random.randrange(0, len(availablePos))]

    def chooseBestMove(self, agentSign, availablePos, board_setting) -> int:
        return self.__makeRandomMove(availablePos)

    def calculateReward(self, reward_amount):
        pass

    def resetHistoricStates(self):
        pass


class QLearning:
    def __init__(self, learning_rate=0.1, decay=0.8, exploration_rate=0.1):

        self.learn_rate = learning_rate
        self.decay = decay
        self.exploration_rate = exploration_rate
        self.states = {}

        self.historic_states = []

    def chooseBestMove(self, agentSign, availablePos, board_setting) -> int:
        # Will decide if agent uses QLearning for making a move or if he makes a random move.
        strategy_chance = random.uniform(0, 1)

        if strategy_chance <= self.exploration_rate:
            # If strategy_chance is less then or equal to exploration_rate then make random move.
            bestMove = availablePos[random.randrange(0, len(availablePos))]
        else:
            # Initialize as some small number.
            maxActionValue = -1000

            # Set best move to be the fist possible move.
            bestMove = availablePos[0]

            # Iterate through all possible moves.
            for move in availablePos:
                # Make a copy of the board
                boardSettingCopy = copy.copy(board_setting)
                # Make move.
                boardSettingCopy[move] = agentSign

                # Get the action value for the move made.
                if self.states.get(str(boardSettingCopy)):
                    action_value = self.states.get(str(boardSettingCopy))
                # If move made doesn't exist, set its value to 0.
                else:
                    action_value = 0

                # If action value of the move is max, declare that move as the best move.
                if action_value > maxActionValue:
                    maxActionValue = action_value
                    bestMove = move

        # Save current state.
        boardSettingCopy = copy.copy(board_setting)
        boardSettingCopy[bestMove] = agentSign
        self.historic_states.append(str(boardSettingCopy))

        return bestMove

    # Contains Bellman equation implementation for Q learning.
    def calculateReward(self, reward_amount):
        # Iteratue through historic states.
        for state in reversed(self.historic_states):

            # If state doesn't exist set its value to 0.
            if self.states.get(state) is None:
                self.states[state] = 0

            # Calculate Q value (reward) for the move made.
            self.states[state] += self.learn_rate * \
                (self.decay * reward_amount - self.states[state])
            reward_amount = self.states[state]

    def resetHistoricStates(self):
        self.historic_states = []
