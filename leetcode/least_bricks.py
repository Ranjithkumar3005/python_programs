class Solution:
    def leastBricks(self, wall):
        h = {}
        for i in wall:
            tot = 0
            for j in range(0, len(i) - 1):
                tot += i[j]
                if tot in h:
                    h[tot] += 1
                else:
                    h[tot] = 1
        val1 = len(wall)
        return val1 - max(h.values(), default=0)
