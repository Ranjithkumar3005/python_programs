class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dum = []
        d = []
        for i in grid:
            for j in i:
                d.append(j)
        while k != 0:
            val = d.pop()
            d.insert(0, val)
            k -= 1
        c = 0
        che = []
        for i in range(0, len(d)):
            che.append(d[i])
            c += 1
            if c == len(grid[0]):
                c = 0
                dum.append(che)
                che = []
        print(dum)


s = Solution()
s.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1)
