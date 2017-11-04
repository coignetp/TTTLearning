from TTT_API.Player import Player
from TTT_API.Board import Board

class AIMinmax(Player):
	"""
	A full random AI
	"""

	def __init__(self, idPlayer, depth):
			""" This AI need a depth attribut """
			Player.__init__(self)
			self.depth = depth

	def minmax(self, board, depth, avaibleMove, idPlayer):
		""" Implementation of the minmax algorithm """
		w = board.getWinner()
		id =  (idPlayer + (self.depth - depth) - 1)%board.numberOfPlayers + 1

		# If the game is over, stop the minmax #
		if w >= 1 and w != idPlayer:
			return 0, 0, -1*(depth+1)
		elif w >= 1 and w == idPlayer:
			return 0, 0, 1*(depth+1)

		if depth <= 0:
				return 0, 0, 0

		max = -3*(depth+1)
		min = 3*(depth+1)
		x = 0
		y = 0

		for i in range(0,len(avaibleMove)):
			if avaibleMove[i]["available"]  == True:
				# Simulate a move to see what will happen next #
				avaibleMove[i]["available"] = False
				board.cells[avaibleMove[i]["y"]][avaibleMove[i]["x"]] = id

				# Recursive call of minmax #
				_, _, temp = self.minmax(board, depth-1, avaibleMove)

				# Cancel the simulated move #
				avaibleMove[i]["available"] = True
				board.cells[avaibleMove[i]["y"]][avaibleMove[i]["x"]] = -1

				# Take the max or the min score, depending on who is the current player #
				if (id == idPlayer and temp > max):
					max = temp
					x = avaibleMove[i]["x"]
					y = avaibleMove[i]["y"]

				elif (id != idPlayer and temp < min):
					min = temp
					x = avaibleMove[i]["x"]
					y = avaibleMove[i]["y"]

		# Return the max score if it's the AI turn, else return the min #
		if(id == idPlayer):	
			return x, y, max
		return x, y, min

	def play(self, board, idPlayer):
		avaibleMove = []

		for i in range(0, board.size):
			for j in range(0, board.size):
				if board.isFree(i, j):
					avaibleMove.append({"available": True, "x": i, "y": j})

		x, y, max = self.minmax(board, self.depth, avaibleMove, idPlayer)

		return x, y