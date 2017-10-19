from TTT_API.Player import Player
from TTT_API.Board import Board

class AIMinmax(Player):
	"""
	A full random AI
	"""

	def __init__(self, idPlayer, depth):
			Player.__init__(self, idPlayer)
			self.depth = depth

	def minmax(self, board, depth, avaibleMove):
		w = board.getWinner()
		id =  (self.idPlayer + (self.depth - depth) - 1)%board.numberOfPlayers + 1

		if w >= 1 and w != self.idPlayer:
			return 0, 0, -1*(depth+1)
		elif w >= 1 and w == self.idPlayer:
			return 0, 0, 1*(depth+1)

		if depth <= 0:
				return 0, 0, 0

		max = -3*(depth+1)
		min = 3*(depth+1)
		x = 0
		y = 0

		for i in range(0,len(avaibleMove)):
			if avaibleMove[i]["available"]  == True:
				avaibleMove[i]["available"] = False
				board.cells[avaibleMove[i]["y"]][avaibleMove[i]["x"]] = id

				_, _, temp = self.minmax(board, depth-1, avaibleMove)

				avaibleMove[i]["available"] = True
				board.cells[avaibleMove[i]["y"]][avaibleMove[i]["x"]] = -1

				if (id == self.idPlayer and temp > max):
					max = temp
					x = avaibleMove[i]["x"]
					y = avaibleMove[i]["y"]

				elif (id != self.idPlayer and temp < min):
					min = temp
					x = avaibleMove[i]["x"]
					y = avaibleMove[i]["y"]

		if(id == self.idPlayer):	
			return x, y, max
		return x, y, min

	def play(self, board):
		avaibleMove = []

		for i in range(0, board.size):
			for j in range(0, board.size):
				if board.isFree(i, j):
					avaibleMove.append({"available": True, "x": i, "y": j})

		x, y, max = self.minmax(board, self.depth, avaibleMove)

		return x, y