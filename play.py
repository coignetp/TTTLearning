from TTT_API.Game import Game
from TTT_API.Human import Human
from AI.AINeuralNetwork import AINeuralNetwork

from sklearn.externals import joblib
import argparse
from pathlib import Path
import numpy as np


def getPlayer(pl):
	"""
	Return the Player type given in parameter
	"""

	# used to construct the filename
	prePath = "save/"
	extension = ".pkl"
	filename = prePath + pl + extension

	# return a human player
	if(pl.lower() == "human"):
		return Human()

	# if the ai file exists, it loads it
	file = Path(filename)
	if file.is_file():
		clf = joblib.load(filename)
		return AINeuralNetwork(clf)

	print(f'{pl} doesn\'t exist')

	return Human()


def getBoardSize(ai1, ai2):
	"""
	Return the board size thanks to the AI
	Return -1 if there is a problem
	"""

	n1 = 0
	n2 = 0

	if isinstance(ai1, AINeuralNetwork):
		n1 = len(ai1.clf.coefs_[0])
	if isinstance(ai2, AINeuralNetwork):
		n2 = len(ai2.clf.coefs_[0])

	# Check if the IA are for different board size
	if n1 != n2 and (n1 != 0 and n2 != 0):
		print("Error : the AI are for different board size")

	if n1 != 0:
		return int(np.sqrt(n1))
	return int(np.sqrt(max(n2, 3)))

# Main function
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Make games of Tic Tac Toe between 2 people/AI.')

	parser.add_argument("player1", help="Name of the first player.")
	parser.add_argument("player2", help="Name of the second player.")
	parser.add_argument("-n", type=int, help="Number of game")
	parser.add_argument("--mute", help="No output at the end")

	args = parser.parse_args()

	ai = []
	ai.append(getPlayer(args.player1))
	ai.append(getPlayer(args.player2))

	size = getBoardSize(ai[0], ai[1])

	# save the game results
	results = [0] * 3

	# play the games
	args.n = max(args.n, 1)
	for _ in range(args.n):
		g = Game(size)
		pl = 0

		while g.board.getWinner() == -1:
			if args.mute == None:
				print(g.board)

			g.playTurn(ai[pl].play, pl+1)

			pl = (pl + 1)%2


		winner = g.board.getWinner()
		if args.mute == None:
			print(g.board)
			if winner == 0:
				print('Draw !')
			else:
				print(f'{winner} won !')

		results[winner] += 1

	if args.mute == None:
		print(f'Results : {results}')