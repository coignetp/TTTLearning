from main import rVr


# iterations
n = 15000

# Draw, win1, win2
data = [0, 0, 0]

for i in range(n):
    data[rVr(False)] += 1

wins = data[1] + data[2]
draws = data[0]

print(f'Number of wins: {wins}')
print(f'Number of draws: {draws}')
print(f'Proportion of wins from p1: {data[1]/n}')
print(f'Proportion of wins from p2: {data[2]/n}')
print(f'Proportion of draws: {draws/wins}')