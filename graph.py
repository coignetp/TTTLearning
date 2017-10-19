from main import rVr


# iterations
n = 1500
# size of the grid
size = 3
# number of player
nbPlayer = 2

# Draw, win1, win2
data = [0 for i in range(0, nbPlayer+1)]

for i in range(n):
    data[rVr(False, size, nbPlayer)] += 1


for i in range(1, len(data)):
	print(f'Statistics for player {i} : Wins = {data[i]} ; Proportion = {data[i]/n}')
print(f'Draws : Number = {data[0]} ; Proportion = {data[0]/n}')

"""wins = data[1] + data[2]
draws = data[0]

print(f'Number of wins: {wins}')
print(f'Number of draws: {draws}')
print(f'Proportion of wins from p1: {data[1]/n}')
print(f'Proportion of wins from p2: {data[2]/n}')
print(f'Proportion of draws: {draws/n}')"""