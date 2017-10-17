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
	symbols = {1: 'X', 2: 'O'}
	numberOfPlayer = 2

	def __init__(self, size, symbols={1: 'X', 2: 'O'}):
		""" Board contructor """
		if size <= 0 or len(symbols) <= 0:
			return

		self.size = size
		self.symbols = symbols
		self.numberOfPlayer = len(self.symbols)

		for i in range(0, size):
			self.cells.append([-1 for k in range(0, size)])

	def isFree(self, x, y):
		""" Tells if the cell is free to play """

		if (x < 0 or x >= self.size) or (y < 0 or y >=self.size):
			return False

		return (self.cells[y][x] == -1)

	def play(self, x, y, id):
		""" Plays for the player id """
		if not self.isFree(x, y) or id < 0 or id > self.numberOfPlayer:
			return False

		self.cells[y][x] = id

		return True

	def isComplete(self):
		""" Tells if the board is full """
		for i in range(0, self.size):
			for j in range(0, self.size):
				if self.isFree(i, j):
					return False
		return True

	def getLineSize(self, x, y, visited):
		""" Tells the length of (x,y) id line 
			and update the visited cells """
		lineSize=0
		i = 0

		while x-i >=0 and self.cells[y][x] == self.cells[y][x-i]:
			visited[y][x-i] = True
			i += 1

		lineSize += i

		i = 0
		while x+i+1 < self.size and self.cells[y][x] == self.cells[y][x+i+1]:
			visited[y][x+i+1] = True
			i += 1

		lineSize += i

		return lineSize