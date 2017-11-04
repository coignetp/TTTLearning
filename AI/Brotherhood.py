class Brotherhood:
	"""
	Define a brotherhood of AINeuralNetwork
	- size : number of AI
	- ai
	- hiddenLayerNumber
	- hiddenLayerSize
	- boardSize
	"""

	def __init__(self, size, hiddenLayerNumber, hiddenLayerSize, boardSize):
		self.size = size
		self.hiddenLayerNumber = hiddenLayerNumber
		self.hiddenLayerSize = hiddenLayerSize
		self.boardSize = boardSize

		self.ai = [0] * self.size