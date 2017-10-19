from TTT_API.Game import Game
from TTT_API.Human import Human
from AI.AIRandom import AIRandom
from TTT_API.Player import Player
from typing import List

def rVr(show = True, size: int=3, nbPlayers: int=2) -> int:
    # size = int(input("Enter a size of the board: \n> "))
    # nbPlayers = int(input("Enter a number of players: \n> "))
    game = Game(size, nbPlayers)
    ## pl = [Human(id+1) for id in range(0, nbPlayers)]

    pl = [AIRandom(i + 1, size) for i in range(0, nbPlayers)]

    return battle(pl, show, size)

def battle(players: List[Player], show = True, size: int=3) -> int:
    nbPlayers = len(players)
    game = Game(size, nbPlayers)

    player = 0

    while 1:
        if show:
            print(game.board)
        """inpt = input("Play in (x, y): \n> ")
        finished = game.playTurn(lambda b: map(int, inpt.split(' ')), player%nbPlayers + 1)"""
        #x, y = pl[player%nbPlayers].play(game.board)
        finished = game.playTurn(players[player%nbPlayers].play, (player%nbPlayers + 1))
        #print("Finished")
        if finished != -1:
            if show:
                print(game.board)            
            break
        player += 1
    
    return finished

# Main function
if __name__ == '__main__':
    print('Winner is : ' + str(rVr()))