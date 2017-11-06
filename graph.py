from main import rVr
import matplotlib.pyplot as plt
from AI.Generation import Generation

from AI.AIRandom import AIRandom
from AI.Simulation import Simulation

s = Simulation(keepRate=0.6, nAI=5, nFights=500, nGen=10)
s.run()
"""
ai = [AIRandom(3), AIRandom(3)]
b = Generation(2, ai, [3, 3, 3], 3)
b.run(20)
print(b.getHistory())"""
#print(b.historic)

#print(b.historic)

"""
# iterations#b.historic[3][3][0] = [1, 2, 3]
#b.historic[3][3] = [9, 9, 9]
#b.historic[3] = [9, 9, 9]


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
print(f'Draws : Number = {data[0]} ; Proportion = {data[0]/n}')"""

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