import sys
from collections import defaultdict, deque

MOD = 10**9 + 7

def get_ans(N, M, cols, X, edges):
    # Create graph
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Find original tree diameter
    original_diameter = find_tree_diameter(graph, N)
    
    total_expected = 0
    
    for u in range(1, N + 1):
        # For each node U, compute the impact of adding a new edge
        for c in range(1, X + 1):
            # New longest path considering U and weight c
            new_diameter = original_diameter + c
            total_expected += new_diameter
            total_expected %= MOD
    
    total_expected *= (1 / N) * (1 / X)
    return int(total_expected) % MOD

def bfs_farthest(node, graph, n):
    distance = [-1] * (n + 1)
    distance[node] = 0
    q = deque([node])
    farthest_node = node
    max_dist = 0
    
    while q:
        current = q.popleft()
        for neighbor, weight in graph[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + weight
                q.append(neighbor)
                if distance[neighbor] > max_dist:
                    max_dist = distance[neighbor]
                    farthest_node = neighbor
                    
    return farthest_node, max_dist

def find_tree_diameter(graph, n):
    # Find one endpoint of the longest path
    farthest, _ = bfs_farthest(1, graph, n)
    # Find the longest path from this endpoint
    _, diameter = bfs_farthest(farthest, graph, n)
    return diameter

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    cols = int(sys.stdin.readline().strip())
    X = int(sys.stdin.readline().strip())

    edges = []
    for _ in range(M):
        edges.append(list(map(lambda x: int(x), sys.stdin.readline().strip().split(" "))))

    result = get_ans(N, M, cols, X, edges)
    print(result)

if __name__ == "__main__":
    main()
