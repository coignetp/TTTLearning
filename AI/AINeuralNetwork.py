from TTT_API.Player import Player
from TTT_API.Board import Board


class AINeuralNetwork(Player):
	"""
	An AI that uses a neural network
	"""

	def __init__(self, clf):
		self.clf = clf

	def play(self, board):
		prediction = self.clf.predict([board.toArray()])

		return prediction