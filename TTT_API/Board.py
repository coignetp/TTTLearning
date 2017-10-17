# Board class

class Board:
	"""
	Define the board of the game with :
	- size
	- cells
	- symbols 
	"""

	size = 0
	cells = []
	symbols = ['X', 'O']

	def __init__(self, size, symbols=['X', 'O']):
		""" Board contructor """
		if size <= 0 or len(symbols) <= 0:
			return

		self.size = size
		self.symbols = symbols

		for i in range(0, size):
			self.cells.append([-1 for k in range(0, size)])