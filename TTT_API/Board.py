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

		self.symbols[-1] = ' '

		for i in range(0, size):
			self.cells.append([-1 for k in range(0, size)])

	def isFree(self, x, y):
		""" Tells if the cell is free to play """

		if (x < 0 or x >= self.size) or (y < 0 or y >=self.size):
			return False

		return (self.cells[y][x] == -1)

	def play(self, x, y, id):
		""" Plays for the player id """
		if not self.isFree(x, y) or id <= 0 or id > self.numberOfPlayer:
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

	def getColumnSize(self, x, y, visited):
		""" Tells the size of the (x,y) id column
			and update the visited cells """
		columnSize=0
		i = 0

		while y-i >=0 and self.cells[y][x] == self.cells[y-i][x]:
			visited[y-i][x] = True
			i += 1

		columnSize += i

		i = 0
		while y+i+1 < self.size and self.cells[y][x] == self.cells[y+i+1][x]:
			visited[y+i+1][x] = True
			i += 1

		columnSize += i

		return columnSize

	def getDiagTopLeftSize(self, x, y, visited):
		""" Tells the size of one of the diagonal
			and update visited cells """

		diagSize = 0
		i = 0

		while (x-i >= 0 and y-i >= 0) and self.cells[y][x] == self.cells[y-i][x-i]:
			visited[y-i][x-i] = True
			i += 1

		diagSize += i

		i = 0
		while (x+i+1 < self.size and y+i+1 < self.size) and self.cells[y][x] == self.cells[y+i+1][x+i+1]:
			visited[y+i+1][x+i+1] = True
			i += 1

		diagSize += i

		return diagSize

	def getDiagTopRightSize(self, x, y, visited):
		""" Tells the size of one of the diagonal
			and update visited cells """

		diagSize = 0
		i = 0

		while (x+i < self.size and y-i >= 0) and self.cells[y][x] == self.cells[y-i][x+i]:
			visited[y-i][x+i] = True
			i += 1

		diagSize += i

		i = 0
		while (x-i-1 >= 0 and y+i+1 < self.size) and self.cells[y][x] == self.cells[y+i+1][x-i-1]:
			visited[y+i+1][x-i-1] = True
			i += 1

		diagSize += i

		return diagSize

	def getWinner(self):
		""" Returns the winner of the game """
		visited = []
		for i in range(0, self.size):
			visited.append([False for k in range(0, self.size)])

		for i in range(0, self.size):
			for j in range(0, self.size):
				if not self.isFree(i, j) \
				and visited[j][i] == False \
				and(self.getLineSize(i, j, visited) >= self.size\
				or self.getColumnSize(i, j, visited) >= self.size\
				or self.getDiagTopLeftSize(i, j, visited) >= self.size\
				or self.getDiagTopRightSize(i, j, visited) >= self.size):
					return self.cells[j][i]

		if self.isComplete():
			return 0

		return -1

	def __repr__(self):
		""" Prints the board with the line
			and column names """
		ret = "    "

		begLine = "+---"

		for i in range(1, self.size+1):
			ret += (" " * (len(begLine)-1)) + str(i)

		ret += "\n"

		for i in range(0, self.size):
			ret += "     "
			for j in range(0, self.size):
				ret += begLine
			ret += "+\n  " + chr(ord('a') + i) + "  |"
			for j in range(0, self.size):
				ret += " " + self.symbols[self.cells[j][i]] + " |"
			ret += "\n"
		ret += (" " * (len(begLine)+1))

		for j in range(0, self.size):
			ret += begLine
		ret += "+"

		return ret