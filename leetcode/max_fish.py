class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        max_sum = 0
        
        # Loop through each cell
        for i in range(rows):
            for j in range(cols):
                # Start with the current cell's value
                total = grid[i][j]
                
                # Check for valid neighbors (up, down, left, right)
                if i > 0:  # Up
                    total += grid[i - 1][j]
                if i < rows - 1:  # Down
                    total += grid[i + 1][j]
                if j > 0:  # Left
                    total += grid[i][j - 1]
                if j < cols - 1:  # Right
                    total += grid[i][j + 1]
                
                max_sum = max(max_sum, total)
        
        print(max_sum)
        return max_sum

s = Solution()
s.findMaxFish(grid=[[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]])
