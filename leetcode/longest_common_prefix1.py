class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        h = {}
        for i in arr1:
            val = str(i)
            for j in range(len(val)):
                if val[: j + 1] not in h:
                    h[val[: j + 1]] = 1
        max1 = 0
        for i in arr2:
            val = str(i)
            for j in range(len(val)):
                if val[: j + 1] in h:
                    max1 = max(max1, j + 1)
        print(max1)


s = Solution()
s.longestCommonPrefix(arr1=[1, 10, 100], arr2=[1000])
