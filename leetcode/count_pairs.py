from collections import deque

class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        h = {}
        for i in edges:
            if i[0] in h:
                h[i[0]].append(i[1])
            else:
                h[i[0]] = [i[1]]
                
            if i[1] in h:
                h[i[1]].append(i[0])
            else:
                h[i[1]] = [i[0]]
        
        que = deque([edges[0][0]])
        visited = set([edges[0][0]])
        c = 0
        
        while que:
            pople = que.popleft()
            for i in h[pople]:
                if i not in visited:
                    visited.add(i)
                    que.append(i)
                    c += 1
        
        print(c)

s = Solution()
s.countPairs( n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]])
