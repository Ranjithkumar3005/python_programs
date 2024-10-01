class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        h = {}
        for i in pick:
            if i[0] not in h:
                h[i[0]] = {}
            if i[1] in h[i[0]]:
                h[i[0]][i[1]] += 1
            else:
                h[i[0]][i[1]] = 1
        c = 0
        for i in h:
            if max(h[i].values()) > i:
                c += 1
        print(c)


s = Solution()
s.winningPlayerCount(n=4, pick=[[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]])
