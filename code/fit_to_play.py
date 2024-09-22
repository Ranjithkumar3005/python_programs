import sys

# Fast input and output for large inputs
input = sys.stdin.read
output = sys.stdout.write

def find_maximum_improvement(goals):
    min_goals = goals[0]
    max_diff = -1
    
    for i in range(1, len(goals)):
        max_diff = max(max_diff, goals[i] - min_goals)
        min_goals = min(min_goals, goals[i])
    
    return max_diff

data = input().split()
index = 0
T = int(data[index])
index += 1

results = []
for _ in range(T):
    N = int(data[index]) 
    index += 1
    goals = list(map(int, data[index:index + N]))
    index += N
    
    max_improvement = find_maximum_improvement(goals)
    
    if max_improvement > 0:
        results.append(str(max_improvement) + '\n')
    else:
        results.append("UNFIT\n")

# Output all results at once for fast output
output(''.join(results))
