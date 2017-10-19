from Player import Player

class Human(Player):
	"""
	Player instance for human players
	"""

	def play(self, board):
		""" Asks the human what he would like to play """

		availableChoice = False

		while not availableChoice:
			inpt = input("Enter an available case:\n")
			(letter, number) = inpt.split(' ')

			# Convert the input
			y = int(number) - 1
			x = ord(letter) - ord('a')

			availableChoice = board.isFree(x, y)

		return x, y