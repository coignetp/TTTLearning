from TTT_API.Game import Game
from TTT_API.Human import Human
from AI.AINeuralNetwork import AINeuralNetwork

from sklearn.externals import joblib
import argparse
from pathlib import Path


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

# Main function
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Make games of Tic Tac Toe between 2 people/AI.')

	parser.add_argument("player1", help="Name of the first player.")
	parser.add_argument("player2", help="Name of the second player.")
	parser.add_argument("-n", type=int, help="Number of game")
	parser.add_argument("--mute", help="No output at the end")

	args = parser.parse_args()

	ai1 = getPlayer(args.player1)
	ai2 = getPlayer(args.player2)