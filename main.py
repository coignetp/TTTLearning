from TTT_API.Game import Game
from TTT_API.Human import Human
from AI.AIRandom import AIRandom

# Main function
if __name__ == '__main__':
    size = int(input("Enter a size of the board: \n> "))
    nbPlayers = int(input("Enter a number of players: \n> "))

    game = Game(size, nbPlayers)
    ##pl = [Human(id+1) for id in range(0, nbPlayers)]

    pl = [AIRandom(1, game.board), AIRandom(2, game.board)]

    player = 0

    while 1:
        print(game.board)
        """inpt = input("Play in (x, y): \n> ")
        finished = game.playTurn(lambda b: map(int, inpt.split(' ')), player%nbPlayers + 1)"""
        #x, y = pl[player%nbPlayers].play(game.board)
        finished = game.playTurn(pl[player%nbPlayers].play, (player%nbPlayers + 1))
        if finished != -1:
            print(game.board)            
            break
        player += 1
    
    print(f'Winner is {finished}')