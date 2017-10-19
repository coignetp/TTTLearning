from main import rVr, battle
import matplotlib.pyplot as plt
from AI.AIRandom import AIRandom

# iterations
n = 15
# size of the grid
size = 4
# players
players = [AIRandom(1, size), AIRandom(2, size)]
# number of player
nbPlayer = len(players)

# Draw, win1, win2
data = [0 for i in range(0, nbPlayer+1)]

for i in range(n):
    data[battle([AIRandom(1, size), AIRandom(2, size)], False, size)] += 1


for i in range(1, len(data)):
	print(f'Statistics for player {i} : Wins = {data[i]} ; Proportion = {data[i]/n}')
print(f'Draws : Number = {data[0]} ; Proportion = {data[0]/n}')

"""wins = data[1] + data[2]
draws = data[0]

plt.bar([0, 1, 2], height=[x/n for x in data])
plt.xticks([0, 1, 2], ['P_draw', 'P_win1', 'P_win2'])
plt.yticks([0.05*i for i in range(20)])
plt.ylabel('Probability')
plt.grid(linestyle='dashdot')
plt.show()

print(f'Number of wins: {wins}')
print(f'Number of draws: {draws}')
print(f'Proportion of wins from p1: {data[1]/n}')
print(f'Proportion of wins from p2: {data[2]/n}')
print(f'Proportion of draws: {draws/n}')"""