class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            for j in str(i):
                if j not in h:
                    h[j] = 1
                else:
                    h[j] += 1
        c = 0
        sum1 = sum(h.values())
        print(h)
        tot = 0
        for i in nums:
            for j in str(i):
                tot += sum1 - h[j]
                h[j] -= 1
                if h[j] == 0:
                    del h[j]
        print(tot)


s = Solution()
s.sumDigitDifferences(nums=[13, 23, 12])
