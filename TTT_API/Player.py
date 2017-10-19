from Board import Board

class Player:
	"""
	Basic class where all AI or Human player come from it.
	"""

	def __init__(self, idPlayer: int):
		self.idPlayer = idPlayer

	def play(self, board: Board) -> (int, int):
		""" Makes the player play according to the actual board 
			Returns the (x,y) position of the move """

		return -1,-1