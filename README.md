# TTTLearning
AI for the tic tac toe game

## Generate a new AI

You can generate a new AI with the `generate.py` file by doing for example:
`python generate.py -nA 3 -o 3gen`
Which will train a new AI on a Simulation with 3 AI per generation

For more details `python generate.py -h` outputs:
```
usage: generate.py [-h] -o OUTPUT [-bs BOARDSIZE] [-kR KEEPRATE] [-nA NAI]
                   [-nF NFIGHTS] [-nG NGEN]
                   [-hdl [HIDDENLAYERSIZES [HIDDENLAYERSIZES ...]]]

Generate a new AI

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        The output file which will hold the model (required)
  -bs BOARDSIZE, --boardSize BOARDSIZE
                        The boardSize (default is 3)
  -kR KEEPRATE, --keepRate KEEPRATE
                        The proportion on records on which we learn (default
                        is 0.6)
  -nA NAI, --nAI NAI    The number of AI per generation (default is 5)
  -nF NFIGHTS, --nFights NFIGHTS
                        The number of fights at the first generation (default
                        is 200) for generation i the number of fights will be
                        i*nFights
  -nG NGEN, --nGen NGEN
                        The number of generations (default is 10)
  -hdl [HIDDENLAYERSIZES [HIDDENLAYERSIZES ...]], --hiddenLayerSizes [HIDDENLAYERSIZES [HIDDENLAYERSIZES ...]]
                        The number of generations (default is (10, 10, 5))
```

## Playing against an AI

You can play against an AI with the play.py file by doing:
`python play.py human 3gen -n 2`
If you don't want to begin the game you can do:
`python play.py 3gen human -n 2`

for more details `python play.py -h` outputs the following:
```
usage: play.py [-h] [-n N] [--mute MUTE] player1 player2

Make games of Tic Tac Toe between 2 people/AI.

positional arguments:
  player1      Name of the first player.
  player2      Name of the second player.

optional arguments:
  -h, --help   show this help message and exit
  -n N         Number of game
  --mute MUTE  No output at the end
```