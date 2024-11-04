class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Initialize DP arrays for max and min products
        max_prod = [[0] * n for _ in range(m)]
        min_prod = [[0] * n for _ in range(m)]

        # Initialize the starting point
        max_prod[0][0] = min_prod[0][0] = grid[0][0]

        # Fill the first row
        for j in range(1, n):
            max_prod[0][j] = max_prod[0][j - 1] * grid[0][j]
            min_prod[0][j] = min_prod[0][j - 1] * grid[0][j]

        # Fill the first column
        for i in range(1, m):
            max_prod[i][0] = max_prod[i - 1][0] * grid[i][0]
            min_prod[i][0] = min_prod[i - 1][0] * grid[i][0]

        # Fill the rest of the DP tables
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] >= 0:
                    max_prod[i][j] = (
                        max(max_prod[i - 1][j], max_prod[i][j - 1]) * grid[i][j]
                    )
                    min_prod[i][j] = (
                        min(min_prod[i - 1][j], min_prod[i][j - 1]) * grid[i][j]
                    )
                else:
                    max_prod[i][j] = (
                        min(min_prod[i - 1][j], min_prod[i][j - 1]) * grid[i][j]
                    )
                    min_prod[i][j] = (
                        max(max_prod[i - 1][j], max_prod[i][j - 1]) * grid[i][j]
                    )

        # Get the result from the bottom-right corner
        result = max_prod[m - 1][n - 1]
        return result % MOD if result >= 0 else -1
