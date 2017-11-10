from TTT_API.Player import Player
from TTT_API.Board import Board


class AINeuralNetwork(Player):
    """
        An AI that uses a neural network
    """

    def __init__(self, clf):
        Player.__init__(self)
       	self.clf = clf

    def formatPred(self, pred):
        return pred//3, pred%3

    def play(self, board, idPlayer):
        prediction = self.clf.predict([board.toArray()])[0]
        proba = self.clf.predict_proba([board.toArray()])[0]

        l = sorted(list(zip(self.clf.classes_, proba)), key=lambda x: x[1])
        x, y = self.formatPred(l.pop()[0])
        while not(board.isFree(x, y)):
            try:
                x, y = self.formatPred(l.pop()[0])
            except IndexError:
                print(board.cells)
                print(l)
                print('#'*500)
                break
        return x, y

    def __repr__(self):
        return 'Neural Network AI'