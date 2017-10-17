class Game:
    def __init__(self, nbPlayers: int, gameType: str):
        self.nbPlayers = nbPlayers
        self.gameType = gameType
    
    def __repr__(self) -> str:
        return f'A tic tac toe game of type {self.gameType} with {self.nbPlayers} players'