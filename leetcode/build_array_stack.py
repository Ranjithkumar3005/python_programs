class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """

        stac = []
        c = 0
        for i in range(1, n + 1):
            if target[c] == i:
                c += 1
                stac.append("Push")
                if c == len(target):
                    break
            else:
                stac.append("Push")
                stac.append("Pop")
        print(stac)


s = Solution()
s.buildArray(target=[1, 2], n=4)
