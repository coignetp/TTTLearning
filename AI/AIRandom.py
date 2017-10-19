from TTT_API.Player import Player
from TTT_API.Board import Board
from random import randint

class AIRandom(Player):
	"""
	A full random AI
	"""

	def __init__(self, idPlayer, board):
		Player.__init__(self, idPlayer)

		self.availableMove = []

		for i in range(0, board.size):
			for j in range(0, board.size):
				self.availableMove.append((i,j))

	def play(self, board):
		# Remove all the case not available #
		for t in self.availableMove:
			if not board.isFree(t[0], t[1]):
				self.availableMove.remove(t)

		# Select a random move #
		z = randint(0, len(self.availableMove)-1)

		return self.availableMove[z]