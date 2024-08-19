class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        c=0
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]<0:
                    c+=1
        print(c)
        
        

s=Solution()
s.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])