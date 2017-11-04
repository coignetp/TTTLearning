from TTT_API.Player import Player
from TTT_API.Board import Board
from random import randint

class AIRandom(Player):
	"""
	A full random AI
	"""

	def __init__(self, boardSize):
		Player.__init__(self)

		self.availableMove = []
		self.boardSize = boardSize

		for i in range(0, boardSize):
			for j in range(0, boardSize):
				self.availableMove.append((i,j))

	def play(self, board, idPlayer):
		# Remove all the case not available #
		sup = []

		for t in self.availableMove:
			if not board.isFree(t[0], t[1]):
				sup.append(t)

		for i in sup:
			self.availableMove.remove(i)

		# Select a random move #
		z = randint(0, len(self.availableMove)-1)

		return self.availableMove[z]

	def reset(self):
		self.availableMove = []

		for i in range(0, self.boardSize):
			for j in range(0, self.boardSize):
				self.availableMove.append((i,j))