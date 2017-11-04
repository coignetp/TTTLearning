from TTT_API.Board import Board

class Player:
	"""
	Basic class where all AI or Human player come from it.
	"""

	def __init__(self):
		self.idPlayer = 0

	def play(self, board: Board, idPlayer: int) -> (int, int):
		""" Makes the player play according to the actual board 
			Returns the (x,y) position of the move """

		self.idPlayer = idPlayer

		return -1,-1