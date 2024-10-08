class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i==j or (i+j) ==n-1:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0: 
                    return False
        return True
        
        

s=Solution()
print(s.checkXMatrix(grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))