class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        up = left = float('inf')
        down = right = float('-inf')
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    up = min(up, row)
                    down = max(down, row)
                    right = max(right, col)
                    left = min(left, col)
        area: int = (right - left + 1) * (down - up + 1)
        return area
        

s=Solution()
print(s.minimumArea(grid = [[0,1,0],[1,0,1]]))