class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cols=[]
        for i in range(0,len(grid)):
            dum=[]
            for j in range(0,len(grid)):
                dum.append(grid[j][i])
            cols.append(dum)
        tot=0
        for i in grid:
            c=cols.count(i)
            tot+=c
        print(tot)

s=Solution()
s.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])