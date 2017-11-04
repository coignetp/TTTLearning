from AI.AINeuralNetwork import AINeuralNetwork
from TTT_API.Game import Game
from TTT_API.Player import Player
from AI.AIRandom import AIRandom
from copy import deepcopy

class Generation:
	"""
	Define a brotherhood of AINeuralNetwork
		- size : number of AI
		- ai
		- hiddenLayerSizes
		- boardSize
		- history
	"""

	def __init__(self, size, ai, hiddenLayerSizes, boardSize):
		"""
		Parameters :
			- size of the brotherhood
			- ai : list of the ai
			- hiddenLayerSizes : list of the hidden layers
			- boardSize : size of the board game
		"""
		self.size = size
		self.hiddenLayerSizes = hiddenLayerSizes
		self.boardSize = boardSize

		self.ai = ai
		self.historic = []

	def getHistory(self):
		"""
		Clarify the history for the neural network learning
		"""
		h = []

		for i in range(0, len(self.history)):
			for j in range(0, len(self.history[i]) - 1):
				if (self.history[i][-1] == 0 or self.history[i][-1] == ((j-1)%2) + 1) and len(self.history[i][j][0]) > 0:
					b = [[0] * self.boardSize * self.boardSize, deepcopy(self.history[i][j][1])]

					for k1 in range(0, self.boardSize):
						for k2 in range(0, self.boardSize):
							b[0][k1*self.boardSize + k2] = self.history[i][j][0][k1][k2]

					h.append(b)

		return h

	def run(self, n):
		"""
		Run the games between all the AI
		"""
		self.history = [[ [ [], (-1, -1)]for _ in range(self.boardSize*self.boardSize)] + ["X"] for _ in range(0, n*self.size*(self.size-1)//2)]

		# Store the number of win
		self.stats = [0] * (self.size + 1)

		p = 0

		# Looping for n games for i against j
		for i in range(0, self.size):
			for j in range(i+1, self.size):
				for k in range(0, n):

					for a in range(0, self.size):
						if isinstance(self.ai[a], AIRandom):
							self.ai[a].reset()

					g = Game(self.boardSize, 2)
					pl = 0
					finished = -1
					c = 0
					player = i
					idp = 1

					while finished == -1:
						finished = g.playTurn(self.ai[player].play, idp)

						self.history[p][c] = [deepcopy(g.board.cells), g.histories[-1]["history"][-1]]

						# Change the player
						if player == i:
							player = j
							idp = 2
						else:
							player = i
							idp = 1
						c += 1

					self.history[p][-1] = finished
					self.stats[finished] += 1
					p += 1

		#print(self.history)
		print(self.stats)
		return self.stats