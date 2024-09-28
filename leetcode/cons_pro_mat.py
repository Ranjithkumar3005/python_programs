class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        pro = 1
        for i in grid:
            for j in i:
                pro *= j
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = (pro // grid[i][j]) % 12345
        return grid


s = Solution()
s.constructProductMatrix(grid=[[1, 2], [3, 4]])
