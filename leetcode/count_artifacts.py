class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        h={}
        excavated = set(tuple(d) for d in dig)
        
        for idx, artifact in enumerate(artifacts):
            r1, c1, r2, c2 = artifact
            cells = []
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    cells.append((r, c))
            h[idx] = cells 
        
        c=0
        for cells in h.values():
            if all(cell in excavated for cell in cells):
                c += 1
        print(c)
        
        

s=Solution()
s.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]])