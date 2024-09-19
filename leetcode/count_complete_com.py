from collections import deque
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        visited = [False]*n
        ans = 0
        for v in range(n):
            if not visited[v]:
                q = deque([v])
                vertices_num = 0
                edge_num = 0
                while q:
                    top = q.popleft()
                    if not visited[top]:
                        visited[top] = True
                        vertices_num += 1
                        for nei in graph[top]:
                            if not visited[nei]:
                                edge_num += 1
                                q.append(nei)

                if edge_num == vertices_num*(vertices_num-1)//2:
                    ans += 1
                    
        return ans
s = Solution()
print(s.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))  # Output: 2
