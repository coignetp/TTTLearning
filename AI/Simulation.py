from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
import numpy as np
from AI.AIRandom import AIRandom
from AI.AINeuralNetwork import AINeuralNetwork
from AI.Generation import Generation


class Simulation():
    """
        Defines a simulation (multiple generations)
    """

    def __init__(self, nGen: int=20, nAI: int=4, nFights: int=1000, hiddenLayerSizes=(10, 10, 5), keepRate: float=0.6, boardSize: int=3, outputFile="sim.pkl"):
        """
            Parameters:
                - nGen is the number of generations (default is 20)
                - nAI is the number of AI per generation (default is 4)
                - nFights is the number of fights per AI per generation (default is 1000)
                - hiddenLayerSizes is a list that represents the number of units per hidden layer (default is (10, 10))
                - keepRate is the rate of won/draw games to keep per generation (default is 0.6)
                - boardSize is the board size of the tic tac toe (default is 3)
        """
        self.nGen = nGen
        self.nAI = nAI
        self.nFights = nFights
        self.hiddenLayerSizes = hiddenLayerSizes
        self.keepRate = keepRate
        self.boardSize = boardSize
        self.outputFile = "sim.pkl"

        # The first generation is only random AI
        self.AIlist = [AIRandom(self.boardSize) for i in range(self.nAI)]
        self.gen = Generation(self.nAI, self.AIlist,
                              self.hiddenLayerSizes, self.boardSize)

        self.lastID = self.nAI

    def save(self, AI):
        """
            Save the best AI currently holded in a file
        """
        joblib.dump(AI, f'./save/{self.outputFile}')

    def run(self):
        """
            Run a simulation
        """

        # Loop over the number of generations
        for i in range(self.nGen):
            # Run the generation and get statistics
            draws, *statistics = self.gen.run((i + 1) * self.nFights)

            # Get the history
            history = self.gen.getHistory()

            # Print the statistics
            print(self.AIlist)
            print(f'Generation {i} report:')
            print(f'  - Number of draws: {draws}')
            print(f'  - Number of wins {sum(statistics)}')
            print('-'*15)

            # Generate the new AIList
            # Keep half of the best AI of the last generation
            median = np.median(statistics)

            # If simulation is going to end
            if i == self.nGen - 1:
                # save the best AI (the one which has the highest number of wins)
                self.save(max([(ai, stat) for (ai, stat) in zip(self.AIlist, statistics)], key=lambda v : v[1]))

            else:
                # Compare the number of wins to the median
                self.AIlist = [ai for (ai, stat) in zip(
                    self.AIlist, statistics) if stat >= median]

                # Generate the new generation
                sampleSize = int(self.keepRate * len(history))
                for _ in range(self.nAI - len(self.AIlist)):
                    # Create the classifier and fit it
                    clf = MLPClassifier(
                        hidden_layer_sizes=self.hiddenLayerSizes, max_iter=500)
                    np.random.shuffle(history)
                    hist_sample = np.array(history)[:sampleSize, :]
                    clf.fit(list(hist_sample[:, 0]), [
                            x * 3 + y for x, y in hist_sample[:, 1]])

                    self.AIlist.append(AINeuralNetwork(clf))
                    self.gen = Generation(
                        self.nAI, self.AIlist, self.hiddenLayerSizes, self.boardSize)

        print('Simulation ended !')
