class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        
        
        for i in range(0,len(grid)-1):
            for j in range(0,len(grid[0])):
                if grid[i][j] != grid[i + 1][j]:
                    return False
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == grid[i][j + 1]:
                    return False
        return True
        

s=Solution()
print(s.satisfiesConditions(grid = [[1,7],
                                    [1,1]]))