from TTT_API.Board import Board

class Game:
    """
        Class to manage a Game that takes
            - size the size of the board
            - nbPlayers the number of players 
    """

    def __init__(self, size: int=2, nbPlayers: int=2):
        """ Initialize a new Game with parameters
            Parameters:
                - size the size of the board
                - nbPlayers the number of players 
        """

        self.nbPlayers = nbPlayers

        if (nbPlayers > len(Board.symbols)):
            raise ValueError("Too much players in this game !")
        self.board = Board(size, nbPlayers)

        # Stores the history of played cells
        self.histories = [{
            "size": size,
            "nbPlayers": nbPlayers,
            "history": []
        }]

            
    def playTurn(self, f, ID) -> int:
        """
            Play the turn with the function f (that corresponds to a player with id ID)
            Returns: 
                - Int from -1 to nbPlayers (-1 is game is not finished, 0 is a draw and others are the id of winners)
        """
        x, y = f(self.board)
        # Add the play to the history
        self.histories[-1]["history"].append((x, y))
        self.board.play(x, y, ID)

        return self.board.getWinner()

    def reset(self, size: int=2, nbPlayers: int=2):
        """
            Just reset a game
        """
        self.board = Board(size, nbPlayers)
        self.histories.append({
            "size": size,
            "nbPlayers": nbPlayers,
            "history": []
        })


    def __repr__(self) -> str:
        return f'A tic tac toe game of size {self.board.size} with {self.nbPlayers} players'