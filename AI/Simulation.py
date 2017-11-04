from sklearn.neural_network import MLPClassifier
import numpy as np
from AI.AIRandom import AIRandom
from AI.AINeuralNetwork import AINeuralNetwork
from AI.Generation import Generation


class Simulation():
    """
        Defines a simulation (multiple generations)
    """

    def __init__(self, nGen: int=20, nAI: int=4, nFights: int=1000, hiddenLayerSizes=(10, 10), keepRate: float=0.6, boardSize: int=3):
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

        # The first generation is only random AI
        self.AIlist = [AIRandom(self.boardSize) for i in range(self.nAI)]
        self.gen = Generation(self.nAI, self.AIlist, self.hiddenLayerSizes, self.boardSize)
        
        self.lastID = self.nAI

    def run(self):
        """
            Run a simulation
        """

        # Loop over the number of generations
        for i in range(self.nGen):
            # Run the generation and get statistics
            statistics = self.gen.run(self.nFights)

            # Get the history
            history = self.gen.getHistory()

            # Print the statistics
            draws = statistics.pop()
            print(f'Generation {i} report:')
            print(f'  - Number of draws: {draws}')
            print(f'  - Number of wins {sum(statistics)}')

            # Generate the new AIList
            # Keep half of the best AI of the last generation
            median = np.median(statistics)
            # Compare the number of wins to the median
            self.AIlist = [ai for (ai, stat) in zip(self.AIlist, statistics) if stat >= median]


            # Generate the new generation
            sampleSize = int(self.keepRate*len(history))
            for _ in range(self.nAI - len(self.AIlist)):
                # Create the classifier and fit it
                clf = MLPClassifier(hidden_layer_sizes=self.hiddenLayerSizes)
                np.random.shuffle(history)
                hist_sample = np.array(history)[:sampleSize, :]
                clf.fit(list(hist_sample[:, 0]), [x*3+y for x, y in hist_sample[:, 1]])
                self.AIlist.append(AINeuralNetwork(self.lastID + 1, clf))
                self.gen = Generation(self.nAI, self.AIlist, self.hiddenLayerSizes, self.boardSize)

        print('-'*20)
        print('Simulation ended !')