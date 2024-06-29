class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max=0
        index=0
        for i in range(0,len(grid)):
            length=grid[i].count(1)
            if max<length:
                max=length
                index=i
        print(index)
        
s=Solution()
s.findChampion(grid = [[0,0,1],[1,0,1],[0,0,0]])