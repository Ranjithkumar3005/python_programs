#Python Code
import heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        def buildGraph():
            d = {}
            for i,v in enumerate(edges):
                d.setdefault(v[0], [])
                d.setdefault(v[1], [])
                d[v[0]].append([v[1], succProb[i]])
                d[v[1]].append([v[0], succProb[i]])
            return d

        graph = buildGraph()
        if not start_node in graph or not end_node in graph:
            return 0
        queue = [[-1.0,start_node]]
        dist = [None] * n
        # visited = [False] * n
        # visited[start_node] = True
        heapq.heapify(queue)
        while queue:
            curr = heapq.heappop(queue)
            cost = -curr[0]
            node = curr[1]
            if node == end_node:
                return cost
            edges = graph[node]
            for edge,edgeCost in edges:
                newCost = cost * edgeCost
                prevCost = dist[edge]
                if not prevCost or prevCost < newCost:
                    dist[edge] = newCost
                else:
                    continue
                heapq.heappush(queue,[-newCost,edge])
        return 0


s=Solution()
print(s.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))