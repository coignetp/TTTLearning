
class Game:
    PvP = "PvP"
    PvAI = "PvAI"
    AIvAI = "AIvAI"

    gameTypes = [ PvP, PvAI, AIvAI ]

    def __init__(self, nbPlayers: int=2, gameType: str=PvP):
        """ Initialize a new Game with parameters
            Parameters:
                - nbPlayers: The number of players that want to play the game (default is 2)             
                - gameType: The type of the game (default is Player vs Player)
        """

        # Throw error if wrong gameType
        if not(gameType in Game.gameTypes):
            raise ValueError("Wrong gameType used (should be PvP, PvAI or AIvAI)")

        self.nbPlayers = nbPlayers
        self.gameType = gameType

            

    def start():
        """ Starts a game  """
        print("Start game")
    
    def __repr__(self) -> str:
        return f'A tic tac toe game of type {self.gameType} with {self.nbPlayers}'