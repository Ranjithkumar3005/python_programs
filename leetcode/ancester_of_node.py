class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = [[] for _ in range(n)]
        inDeg = [0] * n
        
        for i in range(0,n):
            graph[edges[i][1]].append(edges[i][0])
        print(graph)
        


s=Solution()
s.getAncestors( n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])