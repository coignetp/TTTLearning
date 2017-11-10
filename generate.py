from AI.Simulation import Simulation
import argparse

# Main function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a new AI")
    # Parser arguments
    parser.add_argument('-o', '--output', type=str, help="The output file which will hold the model (required)", required=True)
    parser.add_argument('-bs', '--boardSize', type=int, help="The boardSize (default is 3)", default=3)
    parser.add_argument('-kR', '--keepRate', type=float, help="The proportion on records on which we learn (default is 0.6)", default=0.6)
    parser.add_argument('-nA', '--nAI', type=int, help="The number of AI per generation (default is 5)", default=5)
    parser.add_argument('-nF', '--nFights', type=int, help="The number of fights at the first generation (default is 200) for generation i the number of fights will be i*nFights", default=200)
    parser.add_argument('-nG', '--nGen', type=int, help="The number of generations (default is 10)", default=10)
    parser.add_argument('-hdl', '--hiddenLayerSizes', type=int, nargs="*", help="The number of generations (default is (10, 10, 5)", default=(10, 10, 5))

    args = parser.parse_args()
    
    s = Simulation(boardSize=args.boardSize, keepRate=args.keepRate, nAI=args.nAI, nFights=args.nFights, nGen=args.nGen, hiddenLayerSizes=args.hiddenLayerSizes, outputFile=args.output)
    s.run()