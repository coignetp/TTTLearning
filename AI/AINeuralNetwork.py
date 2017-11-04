from TTT_API.Player import Player
from TTT_API.Board import Board


class AINeuralNetwork(Player):
    """
        An AI that uses a neural network
    """

    def __init__(self, idPlayer, clf):
        Player.__init__(self)
       	self.clf = clf

    def play(self, board, idPlayer):
        prediction = self.clf.predict([board.toArray()])[0]
        print(prediction//3, prediction%3)
        return [prediction//3, prediction%3]